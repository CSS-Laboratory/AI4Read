"""Build model requests for one unit (P1 digest, P2 verify, P3 re-digest, P4 work map).

Request body = Anthropic Messages API on Vertex (rawPredict / batch `request` field).
"""
import base64
import csv
import hashlib
import io
import json
import re
import subprocess
import tempfile
import time
from functools import lru_cache
from pathlib import Path

from PIL import Image

from . import PIPE, REPO
from .pages import page_kind, page_texts
from .planner import CFG, LIB, UNITS_CSV, catalog, html_clean, H2

SPEC_VERSION = "1.2"
PROMPT_VERSION = "v2.2"
MAX_TOKENS = {"p1": 64000, "p2": 64000, "p3": 64000, "p4": 16000}   # v2.1: P2 with 80 mandatory items reached 40k
IMG_CACHE = PIPE / "_work" / "img"
LONG_SIDE = CFG["image"]["long_side_px"]
QUALITY = CFG["image"]["jpeg_quality"]


# ------------------------------------------------------------------ inputs

@lru_cache(maxsize=None)
def units():
    return {f"{r['work_id']}/{r['unit_id']}": r for r in csv.DictReader(open(UNITS_CSV))}


@lru_cache(maxsize=None)
def spec_text():
    t = (REPO / "DIGEST_SPEC.md").read_text()
    m = re.search(r"\(v(\d+\.\d+)\)", t)
    assert m and m.group(1) == SPEC_VERSION, f"DIGEST_SPEC version {m and m.group(1)} != {SPEC_VERSION}"
    return re.sub(r"^---.*?---\s*", "", t, count=1, flags=re.S)


@lru_cache(maxsize=None)
def concept_spine(field):
    f = REPO / "canon" / f"{field}.md"
    if not f.exists():
        return "(none)"
    t = f.read_text()
    m = re.search(r"^## Concept spine\s*\n(.*?)(?=^## |\Z)", t, flags=re.M | re.S)
    return m.group(1).strip() if m else "(none)"


@lru_cache(maxsize=None)
def fields_of(work_id, primary=""):
    """All catalog fields of a work (gate2 review: multi-field works), primary field first."""
    fs = []
    for e in json.loads((REPO / "canon" / "catalog.json").read_text()):
        if e["id"] == work_id and e.get("slug") and e["slug"] not in fs:
            fs.append(e["slug"])
    if primary and primary in fs:
        fs.remove(primary)
    return tuple(([primary] if primary else []) + fs)


def spines(fields):
    if len(fields) == 1:
        return concept_spine(fields[0])
    return "\n\n".join(f"### {f}\n{concept_spine(f)}" for f in fields)


@lru_cache(maxsize=None)
def system_prompt(kind, fields):
    name = {"p1": "digest", "p3": "digest", "p2": "verify", "p4": "work_index"}[kind]
    t = (PIPE / "prompts" / f"{name}.md").read_text()
    t = t.replace("{{DIGEST_SPEC}}", spec_text()).replace("{{CONCEPT_SPINE}}", spines(fields))
    left = set(re.findall(r"\{\{(\w+)\}\}", t)) - UNIT_PLACEHOLDERS
    assert not left, f"unfilled placeholder in {name}.md: {left}"
    return t


# ------------------------------------------------------------------ images

def _is_spread(pdf, n):
    out = subprocess.run(["pdfinfo", "-f", str(n), "-l", str(n), str(pdf)], capture_output=True, text=True).stdout
    m = re.search(r"Page\s+\d+ size:\s+([\d.]+) x ([\d.]+)", out)
    if not m:
        return False
    w, h = float(m.group(1)), float(m.group(2))
    return w > 1.25 * h


def page_images(pdf, n, scanned, long_side=None):
    """JPEG bytes for pdf page n: one image, or [left, right] halves for a scanned two-page spread."""
    LONG_SIDE = long_side or globals()["LONG_SIDE"]
    key = hashlib.sha1(f"{pdf}:{n}:{LONG_SIDE}:{QUALITY}:v2".encode()).hexdigest()[:16]
    IMG_CACHE.mkdir(parents=True, exist_ok=True)
    cached = sorted(IMG_CACHE.glob(f"{key}-*.jpg"))
    if cached:
        return [c.read_bytes() for c in cached]
    def render(scale):
        with tempfile.TemporaryDirectory() as td:
            subprocess.run(["pdftoppm", "-f", str(n), "-l", str(n), "-png", "-scale-to", str(scale),
                            str(pdf), f"{td}/p"], check=True, capture_output=True)
            return Image.open(next(Path(td).glob("p*.png"))).convert("RGB")
    im = render(LONG_SIDE)
    spread = im.width > 1.25 * im.height              # landscape after rotation = two-page spread (any work)
    if spread:
        im = render(LONG_SIDE * 2)
    parts = [im] if not spread else [im.crop((0, 0, im.width // 2, im.height)),
                                     im.crop((im.width // 2, 0, im.width, im.height))]
    out = []
    for i, p in enumerate(parts):
        if max(p.size) > LONG_SIDE:
            p.thumbnail((LONG_SIDE, LONG_SIDE))
        buf = io.BytesIO()
        p.save(buf, "JPEG", quality=QUALITY, optimize=True)
        (IMG_CACHE / f"{key}-{i}.jpg").write_bytes(buf.getvalue())
        out.append(buf.getvalue())
    return out


# ------------------------------------------------------------------ source blocks

def _printed(row, pdf_pages):
    """Map pdf page -> printed label using the unit's printed range when it is a plain arabic offset."""
    a, b = map(int, pdf_pages.split("-"))
    pr = row.get("printed_pages") or ""
    m = re.fullmatch(r"(\d+)-(\d+)", pr)
    if m and int(m.group(2)) - int(m.group(1)) == b - a:
        off = int(m.group(1)) - a
        return {p: str(p + off) for p in range(a, b + 1)}
    return {}


@lru_cache(maxsize=None)
def _spread_offset(work_id):
    f = PIPE / "toc" / f"{work_id}.json"
    if f.exists():
        return json.loads(f.read_text()).get("spread_offset")
    return None


@lru_cache(maxsize=64)
def _labels(pdf):
    from pypdf import PdfReader
    try:
        return tuple(PdfReader(str(pdf)).page_labels)
    except Exception:
        return None


def printed_map(pdf, pages, work_id=None):
    from .planner import printed_labels
    pr, _ = printed_labels(work_id or "", catalog().get(work_id, {}), pages, list(_labels(pdf) or []) or None)
    return {i + 1: p for i, p in enumerate(pr) if p}


def source_blocks(row, long_side=None):
    """Content blocks for the unit's source, plus stats {text_chars, images}."""
    f = LIB / row["file"]
    rng = row["pdf_pages"]
    blocks, stats = [], {"text_chars": 0, "images": 0, "pages": 0}
    if rng.startswith("c"):
        s, e = map(int, rng[1:].split("-"))
        txt = html_clean(f)[s:e].replace(H2, "").strip()
        blocks.append({"type": "text", "text": f"<source format=\"html\">\n{txt}\n</source>"})
        stats["text_chars"] = len(txt)
        return blocks, stats
    pages = page_texts(f)
    a, b = map(int, rng.split("-"))
    words = sum(len(t.split()) for t in pages) / max(len(pages), 1)
    scanned = words < 30
    printed = printed_map(f, pages, row["work_id"])
    spread_k = _spread_offset(row["work_id"])
    for n in range(a, b + 1):
        text = pages[n - 1].rstrip() if n <= len(pages) else ""
        kind = page_kind(text, words)
        pm = printed.get(n, "?")
        if spread_k is not None and n >= spread_k:
            pm = f"{max(1, 2 * (n - spread_k))}-{2 * (n - spread_k) + 1}"
        blocks.append({"type": "text", "text": f'<page pdf="{n}" printed="{pm}">\n{text}\n</page>'})
        stats["text_chars"] += len(text)
        stats["pages"] += 1
        if kind not in ("prose", "blank"):
            imgs = page_images(f, n, scanned, long_side)
            for i, jpg in enumerate(imgs):
                side = "" if len(imgs) == 1 else (" left half" if i == 0 else " right half")
                hp = pm
                if len(imgs) == 2 and spread_k is not None:
                    hp = str(2 * (n - spread_k) + i) if 2 * (n - spread_k) + i >= 1 else "?"
                elif len(imgs) == 2 and re.fullmatch(r"\d+-\d+", pm or ""):
                    hp = pm.split("-")[i]
                blocks.append({"type": "text", "text": f"[page image: pdf {n}{side} / printed {hp}]"})
                blocks.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg",
                                                           "data": base64.b64encode(jpg).decode()}})
                stats["images"] += 1
    return blocks, stats


def unit_header(row, task):
    cat = catalog().get(row["work_id"], {})
    rng = row["pdf_pages"]
    pr = row.get("printed_pages") or "unknown — use (pdf N) page references"
    lines = [
        "UNIT METADATA",
        f"work_id: {row['work_id']}",
        f"unit_id: {row['unit_id']}",
        f"unit title: {row['title']}",
        f"work citation: {cat.get('citation', '')}",
        f"fields: [{', '.join(fields_of(row['work_id'], row['field']))}]",
        f"level: {cat.get('level', '')}",
        f"source: {'HTML text' if rng.startswith('c') else 'PDF pages ' + rng}; printed pages: {pr}",
        f"spec_version: {SPEC_VERSION}",
        f"prompt_version: {PROMPT_VERSION}",
        f"digested_by: {CFG['model']}",
        f"digested_on: {time.strftime('%Y-%m-%d')}",
    ]
    if re.search(r"-p\d+$", row["unit_id"]):
        lines.append("note: this unit is ONE PART of a longer chapter. Cover only the pages given; "
                     "say in Reading notes where the part starts and ends.")
    if row.get("note"):
        lines.append(f"source notes (mention in Reading notes where relevant): {row['note']}")
    lines.append("")
    lines.append(task)
    return {"type": "text", "text": "\n".join(lines)}


# ------------------------------------------------------------------ requests

MANDATORY_MARK = "=== MANDATORY ITEMS"
UNIT_PLACEHOLDERS = {"MANDATORY_ITEMS", "SOURCE_WORDS", "TARGET_WORDS"}
ARGUMENTATIVE_FIELDS = {"analytic-philosophy"}
ARGUMENTATIVE_WORKS = {"dennett-1987-intentional-stance", "habermas-1989-publicsphere", "carey-1989-cultural",
                       "popper-1959-logic", "kuhn-1962-structure", "lippmann-1922-publicopinion"}
VOICE = re.compile(r"[\"“”‘’]|\*\*[^*\n]{1,40}:\*\*|\b(objection|reply|replies|interlocutor|asks)\b|\?\s*(\(|$)", re.I)
MAX_ITEMS = 120
LOGICAL = re.compile(r"\b(only|always|never|iff|exactly|all|every|must|cannot|proves|shows|necessary|sufficient"
                     r"|alone|merely|unless|conditions?)\b", re.I)
QUOTE_SPAN = re.compile(r"[\"“]([^\"”\n]{3,}?)[\"”]")
QUOTE_BUDGET = 10
WORDS_PER_SCAN_PAGE = 450


def is_argumentative(row):
    return row["work_id"] in ARGUMENTATIVE_WORKS or bool(
        set(fields_of(row["work_id"], row["field"])) & ARGUMENTATIVE_FIELDS)


def source_words(row):
    """Words in the unit's text layer; scanned pages count 450 (two-page spreads 900)."""
    rng = row["pdf_pages"]
    f = LIB / row["file"]
    if rng.startswith("c"):
        s, e = map(int, rng[1:].split("-"))
        return len(html_clean(f)[s:e].replace(H2, " ").split())
    a, b = map(int, rng.split("-"))
    pages = page_texts(f)
    spread = _spread_offset(row["work_id"]) is not None
    n = 0
    for i in range(a - 1, min(b, len(pages))):
        w = len(pages[i].split())
        n += w if w >= 30 else (WORDS_PER_SCAN_PAGE * (2 if spread else 1) if w == 0 or "scan" in row["structure"] else w)
    return n


def target_words(row, sw=None):
    """wave-1 review: min(max(1200, f*sw), 0.80*sw), f = 0.40 (0.55 if >= 40% image pages); 6000 upper bound kept."""
    sw = source_words(row) if sw is None else sw
    n = max(int(row["n_pages"] or 1), 1)
    f = 0.55 if int(row["image_pages"] or 0) / n >= 0.4 else 0.40
    return max(1, min(6000, round(min(max(1200, f * sw), 0.80 * sw))))


def quoted_spans(md):
    """Quoted spans of >= 4 words (quote budget, wave-1 review)."""
    return [m.group(1) for m in QUOTE_SPAN.finditer(md) if len(m.group(1).split()) >= 4]
STRONG = re.compile(r"\b(only|always|never|iff|exactly|all|every|must|cannot|proves|shows)\b", re.I)


def _sentences(text):
    text = re.sub(r"^\*\*Prerequisites:\*\*.*$", "", text, flags=re.M)
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z$*\[(\"“])|\n\s*[-*]\s+|\n\s*\n", text):
        s = " ".join(s.replace("> ", " ").split()).strip(" -*")
        if len(s) > 3:
            yield s


def mandatory_items(md, row=None):
    """Mandatory items for the verifier (verify.md v2.2, item 3), in the wave-1 review's priority order:
    summary (every L0–L2 sentence) → index (Concepts / Canonical-instances lines) → intuition-note →
    strength (L3 sentences with strong/logical words; worked-example "if" conditions) → reading-notes →
    voice (argumentative units). Capped at 120; a quote-budget item is added first when > 10 quoted spans."""
    from .checks import sections, split_frontmatter
    _, body = split_frontmatter(md)
    secs = dict(sections(body))
    out, seen = [], set()

    def add(kind, where, s):
        s = " ".join(s.split()).strip()
        if s and s not in seen:
            seen.add(s)
            out.append({"kind": kind, "where": where, "text": s})

    q = quoted_spans(body)
    if len(q) > QUOTE_BUDGET:
        add("quotes", "whole digest", f"The digest has {len(q)} quoted spans of 4+ words. "
            f"Reduce quotations to <= {QUOTE_BUDGET}; paraphrase the rest.")
    for s_name in ("L0", "L1", "L2"):                                  # 1. summary
        for s in _sentences(secs.get(s_name, "")):
            add("summary", s_name, s)
    for s_name in ("Concepts", "Canonical instances"):                 # 2. index lines
        for line in secs.get(s_name, "").splitlines():
            if re.match(r"^\s*[-*]\s+\S", line):
                add("index", s_name, line.strip(" -*"))
    l3 = secs.get("L3", "")
    lines = l3.splitlines()
    notes = []
    for i, line in enumerate(lines):                                   # 3. intuition notes
        if re.match(r"^\s*>?\s*(?:[-*]\s*)?\**\s*Intuition note\b", line, re.I):
            note = [line]
            for nxt in lines[i + 1:]:
                if not nxt.strip() or (line.lstrip().startswith(">") and not nxt.lstrip().startswith(">")):
                    break
                note.append(nxt)
            notes.append(re.sub(r"^\s*>\s?", "", "\n".join(note), flags=re.M))
    for n_ in notes:
        add("intuition-note", "L3", n_)
    l3_plain = l3
    for n_ in notes:
        l3_plain = l3_plain.replace(n_, " ")
    l3_sents = list(_sentences(l3_plain))
    for s in l3_sents:                                                 # 4. strength / conditions
        if LOGICAL.search(s) or (re.search(r"\b(example|ex\.)", s, re.I) and re.search(r"\bif\b", s, re.I)):
            add("strength", "L3", s)
    for s in _sentences(secs.get("Reading notes", "")):                # 5. reading notes
        add("reading-notes", "Reading notes", s)
    if row is not None and is_argumentative(row):                      # 6. voice
        for s in l3_sents:
            if VOICE.search(s):
                add("voice", "L3", s)
    return out[:MAX_ITEMS]


def _req(kind, fields, content, subs=None):
    """System = cached shared prefix + uncached unit-specific tail (from the first unit placeholder's paragraph)."""
    sys_text = system_prompt(kind, fields)
    subs = subs or {}
    pos = [sys_text.find("{{" + k + "}}") for k in UNIT_PLACEHOLDERS if "{{" + k + "}}" in sys_text]
    if pos:
        cut = sys_text.rfind("\n\n", 0, min(pos))
        cut = cut if cut > 0 else min(pos)
        head, tail = sys_text[:cut], sys_text[cut:]
        for k in UNIT_PLACEHOLDERS:
            tail = tail.replace("{{" + k + "}}", str(subs.get(k, "")))
        system = [{"type": "text", "text": head, "cache_control": {"type": "ephemeral"}},
                  {"type": "text", "text": tail}]
    else:
        system = [{"type": "text", "text": sys_text, "cache_control": {"type": "ephemeral"}}]
    return {
        "anthropic_version": CFG["anthropic_version"],
        "max_tokens": MAX_TOKENS[kind],
        "system": system,
        "messages": [{"role": "user", "content": content}],
    }


LONG_SIDE_P1 = CFG["image"].get("long_side_px_p1", LONG_SIDE)


def p1_request(uid, issues=None):
    row = units()[uid]
    src, stats = source_blocks(row, LONG_SIDE_P1)
    task = "TASK: write the digest of this unit, following the DIGEST SPEC exactly."
    content = [unit_header(row, task)] + src
    kind = "p1"
    if issues:
        kind = "p3"
        content.append({"type": "text", "text":
                        "An independent checker rejected the previous digest of this unit. Its issue list:\n"
                        + json.dumps(issues, ensure_ascii=False, indent=1)
                        + "\nWrite a new digest that avoids all of these problems."})
    sw = source_words(row)
    stats.update(source_words=sw, target_words=target_words(row, sw))
    return _req(kind, fields_of(row["work_id"], row["field"]), content,
                {"SOURCE_WORDS": f"{sw:,}", "TARGET_WORDS": f"{stats['target_words']:,}"}), stats


def p2_request(uid, digest_md):
    row = units()[uid]
    src, stats = source_blocks(row)
    task = "TASK: check the digest at the end against the source pages, following your instructions."
    content = [unit_header(row, task)] + src + [
        {"type": "text", "text": "=== DIGEST TO CHECK ===\n" + digest_md}]
    items = mandatory_items(digest_md, row)
    stats["mandatory_items"] = len(items)
    return _req("p2", fields_of(row["work_id"], row["field"]), content,
                {"MANDATORY_ITEMS": json.dumps(items, ensure_ascii=False, indent=1)}), stats


def content_hash(req):
    return hashlib.sha256(json.dumps(req, sort_keys=True).encode()).hexdigest()[:16]
