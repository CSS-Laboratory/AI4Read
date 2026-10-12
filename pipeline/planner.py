"""Gate 1 unit planner: library files -> pipeline/units.csv.

Structure source per work, in order of preference:
  1. pipeline/toc/<work_id>.json  (reviewed table of contents; overrides everything)
  2. the PDF outline, if it passes sanity checks
  3. whole file as one unit (papers), split into parts if > SPLIT_PAGES

python -m pipeline plan
"""
import csv
import html as htmlmod
import json
import logging
import math
import os
import re
from collections import Counter
from pathlib import Path

import yaml
from pypdf import PdfReader

from . import PIPE, REPO
from .pages import clean_label, page_kind, page_texts, printed_numbers

logging.getLogger("pypdf").setLevel(logging.CRITICAL)

CFG = yaml.safe_load((PIPE / "config.yaml").read_text())
LIB = Path(os.path.expanduser(CFG["paths"]["library"]))
TOC_DIR = PIPE / "toc"
UNITS_CSV = PIPE / "units.csv"

SPLIT_PAGES = 40          # split units longer than this (gate1 review)
MERGE_PAGES = 3           # book units this short merge into the next unit (gate1 review)
TARGET_PART = 28          # aim for parts about this long
DESCEND_PAGES = 60        # outline entries longer than this are containers (Parts)
STUB_WORDS = 2000         # HTML pages with fewer words are landing/abstract pages

SKIP_TITLE = re.compile(
    r"^(book\s*)?cover|^half[- ]?title|^title( page)?$|^copyright|^dedication|^(table of )?contents|"
    r"^brief contents|^list of (figures|tables|illustrations)|^boxes, figures|^acknowledg|^index|"
    r"index$|^(subject|name|author|citation|topic|symbol) index|^bibliography|^references|^notes$|"
    r"^endnotes|^about the author|^also by|^photo credits|^colophon|^further reading|^glossary|"
    r"^frequently used notation|^notation$|^blank page|^praise for|^epigraph|^a bibliography of|"
    r"^issue table of contents|^article contents|translator|^list of symbols|^(list of )?notation|"
    r"^about the authors?|^praise\b|^editorial preface|^the text of|^dedication|^title and front|^german original|licen[cs]e$|^editor.?s (preface|introduction|note|foreword)|^back matter \(detected\)|\(title page\)|^supplement|^solutions|^corrections",
    re.I)
PART_TITLE = re.compile(r"^(part\b|appendi(ces|xes)$|[IVX]{1,4}\s(?!\d))", re.I)
CHAPTER_TITLE = re.compile(r"^(chapter\b|\d{1,2}\.?\s+(?!\d)[A-Za-z])", re.I)
SECTION_TITLE = re.compile(r"^(\d+\.\d+|\d+[A-Z]\b|§)")
SIDE_TITLE = re.compile(r"^(afterword|coda|conclusions?\b|epilogue|interlude|addenda|postscript|prologue|"
                        r"answers|overview|summary)", re.I)
TAIL_TITLE = re.compile(r"^(exercises|problems|summary|further reading|bibliographic notes|"
                        r"historical notes|notes and references|review questions)", re.I)
# prefaces the quality lead re-enabled (reviews/gate1.md); everything else FRONT is skipped
KEEP_FRONT = {("kripke-1980-naming", "front-preface"), ("jaynes-2003-probability", "front-preface"),
              ("kuhn-1962-structure", "front-preface"), ("popper-1959-logic", "front-preface"),
              ("popper-1959-logic", "front-preface-2"), ("shiller-2019-narrative", "front-preface"),
              ("mcelreath-2020-rethinking", "front-preface"), ("wittgenstein-1953-investigations", "front-preface")}
HOLD = {"lycan-2019-language": "HOLD: PDF is the wrong book (reviews/gate1.md) — Kunhao decides"}
SKIP_WORKS = {"johnson-2022-bayesrules": "online on-ramp, not needed (reviews/gate1.md)"}
FRONT_TITLE = re.compile(r"^(author.?s (preface|foreword|note)|preface|foreword|translators?.? note|series editor|a note for|note to)", re.I)

# token model (calibrate after the pilot)
CHARS_PER_TOKEN = 3.6
IMAGE_TOKENS = 1550          # ~1.15 MP after server-side resize; recheck with smoke test usage
PROMPT_OVERHEAD = 1600       # digest.md + DIGEST_SPEC
SPINE_TOKENS = 1400
PAGE_WRAP_TOKENS = 15


def catalog():
    return {c["id"]: c for c in json.loads((REPO / "canon" / "catalog.json").read_text())}


def file_stem(p):
    n = p.name
    for s in (".pdf.pdf", ".pdf", ".html"):
        if n.endswith(s):
            return n[: -len(s)]
    return p.stem


def match_id(stem, ids):
    c = [i for i in ids if stem == i or stem.startswith(i) or i.startswith(stem)]
    return max(c, key=len) if c else None


def source_files():
    out = []
    for p in sorted(LIB.rglob("*")):
        if not p.is_file() or p.suffix not in (".pdf", ".html"):
            continue
        rel = p.relative_to(LIB)
        if rel.parts[0] in ("_meta", "_incomplete"):
            continue
        out.append(p)
    return out


def slug(title, n=1):
    stop = {"the", "a", "an", "of", "and", "on", "in", "to", "for", "with", "as", "is", "what",
            "how", "why", "from", "its", "into", "some", "part", "chapter", "appendix"}
    t = re.sub(r"^(chapter|part|appendix)\s+[\w*]+[.:]?\s*", "", title.strip(), flags=re.I)
    for _ in range(3):
        t = re.sub(r"^([\dIVXLC]+|§+[\d–-]+)[.:)]?\s+", "", t)
    words = [w for w in re.findall(r"[a-z0-9]+", t.lower()) if w not in stop]
    return "-".join(words[:n]) or "untitled"


WORDNUM = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
    "sixteen seventeen eighteen nineteen twenty".split())}


def roman(s):
    v = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100}
    s = s.lower()
    if not s or any(ch not in v for ch in s):
        return None
    tot = 0
    for a, b in zip(s, s[1:] + " "):
        tot += -v[a] if b != " " and v[b] > v[a] else v[a]
    return tot


def chapter_number(title):
    t = title.strip()
    m = re.match(r"^(?:chapter|ch\.?)\s+(\d+|[ivxlc]+|\w+)\b", t, re.I)
    if m:
        g = m.group(1).lower()
        return int(g) if g.isdigit() else (WORDNUM.get(g) or roman(g))
    m = re.match(r"^(\d{1,2})(?:[.:)\s-]|$)", t)
    if m:
        return int(m.group(1))
    m = re.match(r"^([IVXLC]{1,6})[.:)\s]", t)
    if m:
        return roman(m.group(1))
    return None


# ---------------------------------------------------------------- structure

def outline_entries(reader):
    def walk(o, d=0):
        for x in o:
            if isinstance(x, list):
                yield from walk(x, d + 1)
            else:
                try:
                    pg = reader.get_destination_page_number(x) + 1
                except Exception:
                    pg = None
                title = re.sub(r"[\x00-\x1f\ufeff]", " ", str(x.title))
                yield {"level": d, "title": " ".join(title.split()), "pdf": pg}
    try:
        return list(walk(reader.outline)) if reader.outline else []
    except Exception:
        return []


def build_tree(entries):
    root = {"title": "ROOT", "pdf": 1, "children": [], "level": -1}
    stack = [root]
    for e in entries:
        node = {**e, "children": []}
        while stack[-1]["level"] >= e["level"]:
            stack.pop()
        stack[-1]["children"].append(node)
        stack.append(node)
    return root


def outline_ok(entries, n_pages):
    if len(entries) < 3:
        return False, "outline has < 3 entries"
    if any(e["pdf"] is None for e in entries):
        return False, "outline entries without page targets"
    top = [e for e in entries if e["level"] == 0]
    pages = [e["pdf"] for e in top]
    if pages != sorted(pages):
        return False, "outline top level out of order"
    body = [e for e in top if not SKIP_TITLE.search(e["title"])]
    if len(body) < 2:
        return False, "outline has < 2 body entries"
    return True, ""


def spans(nodes, end):
    """Attach 'end' (inclusive pdf page) to each node in a sibling list."""
    for i, n in enumerate(nodes):
        nxt = nodes[i + 1]["pdf"] if i + 1 < len(nodes) else end + 1
        n["end"] = max(n["pdf"], nxt - 1)


def chapters_from_tree(root, n_pages):
    """Return flat list of leaf 'chapter' nodes (with children = sections) in order."""
    out = []
    part_no = [0]

    def visit(nodes, end, depth):
        spans(nodes, end)
        # Rogers-style flat outlines: keep only "Chapter N" entries when present at this level
        chap_like = [n for n in nodes if re.match(r"^chapter\b", n["title"], re.I)]
        if depth == 0 and len(chap_like) >= 3 and len(nodes) > 3 * len(chap_like):
            keep = [n for n in nodes if chap_like.count(n) or SKIP_TITLE.search(n["title"])
                    or FRONT_TITLE.search(n["title"]) or re.match(r"^(appendix|introduction)", n["title"], re.I)]
            spans(keep, end)
            for n in keep:
                n["children"] = []
            nodes = keep
        for n in nodes:
            n_len = n["end"] - n["pdf"] + 1
            kids = [k for k in n["children"] if k["pdf"] is not None and n["pdf"] <= k["pdf"] <= n["end"]]
            if kids:
                spans(kids, n["end"])
            # children that look like sections ("3.1 ...", or short on average) mean n is a chapter
            sectiony = kids and (sum(bool(SECTION_TITLE.match(k["title"])) for k in kids) > len(kids) / 2
                                 or sum(k["end"] - k["pdf"] + 1 for k in kids) / len(kids) < 6)
            chaptery = kids and sum(bool(CHAPTER_TITLE.match(k["title"])) for k in kids) > len(kids) / 2
            is_part = (len(kids) >= 1 and PART_TITLE.match(n["title"]) and not sectiony) or \
                (len(kids) >= 2 and chaptery and not sectiony)
            is_container = is_part or (n_len > DESCEND_PAGES and len(kids) >= 2 and not sectiony and chaptery)
            if is_container:
                part_no[0] += 1
                for k in kids:
                    k["_part"] = part_no[0]
                # pages between container start and first child (part title page / intro)
                if kids[0]["pdf"] - n["pdf"] >= 3:
                    out.append({"title": n["title"] + " (opening)", "pdf": n["pdf"],
                                "end": kids[0]["pdf"] - 1, "children": []})
                visit(kids, n["end"], depth + 1)
            else:
                n["children"] = kids
                spans(kids, n["end"]) if kids else None
                out.append(n)

    top = root["children"]
    if top and top[0]["pdf"] > 1:
        pass
    visit(top, n_pages, 0)
    return out


def toc_chapters(work_id, pr_labels, n_pages):
    """Load pipeline/toc/<work_id>.json (entries carry pdf pages, verified)."""
    f = TOC_DIR / f"{work_id}.json"
    if not f.exists():
        return None
    d = json.loads(f.read_text())
    ents = [e for e in d["entries"] if e.get("pdf")]
    root = build_tree([{"level": e.get("level", 0), "title": e["title"], "pdf": int(e["pdf"])} for e in ents])
    return chapters_from_tree(root, d.get("last_pdf_page") or n_pages), d


# ---------------------------------------------------------------- units

def classify_title(t):
    if SKIP_TITLE.search(t):
        return "skip"
    if FRONT_TITLE.search(t):
        return "front"
    return "body"


def split_ranges(a, b, cut_candidates):
    """Split pdf range [a,b] into parts of about TARGET_PART pages, cutting at candidate pages."""
    n = b - a + 1
    k = math.ceil(n / TARGET_PART)
    if k <= 1:
        return [(a, b, "")]
    cuts = sorted(c for c in set(cut_candidates) if a + 5 <= c <= b - 4)
    bounds, how = [a], "sections"
    for j in range(1, k):
        ideal = a + round(j * n / k)
        if cuts:
            c = min(cuts, key=lambda x: abs(x - ideal))
            if abs(c - ideal) > TARGET_PART * 0.5 or c <= bounds[-1] + 4:
                c, how = ideal, "even"
        else:
            c, how = ideal, "even"
        bounds.append(c)
    bounds.append(b + 1)
    out = [(bounds[i], bounds[i + 1] - 1, how) for i in range(len(bounds) - 1)]
    if any(y - x + 1 > SPLIT_PAGES for x, y, _ in out):
        return split_ranges(a, b, [])
    return out


HEAD = re.compile(r"^\s{0,6}(\d{1,2}\.\d{1,2})\s+[A-Z]")


def heading_pages(pages, a, b):
    return [i + 1 for i in range(a - 1, b) if any(HEAD.match(l) for l in pages[i].splitlines()[:8])]


def unit_rows(work, cat, pdf, pages, pr, kinds, structure, note=""):
    rows = []
    n_pages = len(pages)

    def add(unit_id, title, a, b, kind, action="digest", why=""):
        a, b = max(1, a), min(n_pages, b)
        if b < a:
            return
        img = sum(1 for i in range(a - 1, b) if kinds[i] not in ("prose", "blank"))
        chars = sum(len(pages[i]) for i in range(a - 1, b))
        p_lo = next((pr[i] for i in range(a - 1, b) if pr[i]), None)
        p_hi = next((pr[i] for i in range(b - 1, a - 2, -1) if pr[i]), None)
        rows.append({
            "work_id": work, "unit_id": unit_id, "title": title,
            "pdf_pages": f"{a}-{b}", "printed_pages": f"{p_lo}-{p_hi}" if p_lo and p_hi else "",
            "n_pages": b - a + 1, "image_pages": img,
            "est_tokens": est_input_tokens(chars, img, b - a + 1),
            "tier": cat.get("tier", ""), "field": cat.get("slug", ""),
            "type": cat.get("type", ""), "kind": kind, "structure": structure,
            "action": action, "note": "; ".join(x for x in (why, note) if x),
        })

    return rows, add


def est_input_tokens(chars, img, n):
    return int(PROMPT_OVERHEAD + SPINE_TOKENS + chars / CHARS_PER_TOKEN + img * IMAGE_TOKENS + n * PAGE_WRAP_TOKENS)


def plan_pdf(p, work, cat, dup_note=""):
    reader = PdfReader(str(p))
    pages = page_texts(p)
    n = len(pages)
    try:
        labels = reader.page_labels[:n]
    except Exception:
        labels = None
    pr = [clean_label(x) for x in printed_numbers(pages, labels)]
    words = sum(len(t.split()) for t in pages) / max(n, 1)
    kinds = [page_kind(t, words) for t in pages]
    is_scan = words < 30

    toc = toc_chapters(work, pr, n)
    entries = outline_entries(reader)
    ok, why = outline_ok(entries, n)
    if toc:
        chs, tocd = toc
        structure = "toc-json"
    elif ok and cat.get("type") != "paper":
        chs = chapters_from_tree(build_tree(entries), n)
        structure = "outline"
    elif cat.get("type") == "paper" or n <= SPLIT_PAGES:
        chs = [{"title": "paper", "pdf": 1, "end": n, "children": [], "_whole": True}]
        structure = "whole"
        if ok:   # use outline sections as cut points for long papers
            chs[0]["children"] = [e for e in entries if e["pdf"]]
    else:
        chs = None
        structure = f"needs-toc ({why or 'no outline'})"

    if toc and tocd.get("warning"):
        dup_note = ("WARNING: " + tocd["warning"])[:300]
    rows, add = unit_rows(work, cat, p, pages, pr, kinds, structure + (" scan" if is_scan else ""), dup_note)
    if chs is None:
        add("whole", "(needs table of contents)", 1, n, "book", action="needs-toc",
            why=f"no usable outline: {why or 'none'}")
        return rows

    # fold short tail entries (Exercises, Summary, ...) and part title pages into neighbours
    merged = []
    for ch in chs:
        short = ch["end"] - ch["pdf"] + 1 <= 3
        if merged and TAIL_TITLE.match(ch["title"]) and not merged[-1].get("_whole") \
                and merged[-1]["end"] + 1 >= ch["pdf"] - 1:
            merged[-1] = {**merged[-1], "end": ch["end"]}
            continue
        if merged and short and re.match(r"^appendi", ch["title"], re.I) \
                and re.match(r"^appendi", merged[-1]["title"], re.I) \
                and merged[-1]["end"] - merged[-1]["pdf"] + 1 <= 12:
            first = merged[-1]["title"].split(" (+")[0]
            merged[-1] = {**merged[-1], "end": ch["end"], "title": f"{first} (+ following appendices)"}
            continue
        if short and PART_TITLE.match(ch["title"]) or ch["title"].endswith("(opening)") and short:
            ch = {**ch, "_parttitle": True}
        merged.append(ch)
    chs = merged

    BACK = re.compile(r"^\s*(notes|bibliography|references|index|works cited|glossary)\s*$", re.I)
    body_idx = [i for i, ch in enumerate(chs) if not ch.get("_whole") and classify_title(ch["title"]) == "body"]
    if body_idx and not ch_is_paper(chs):
        last = chs[body_idx[-1]]
        for pg in range(last["pdf"] + 2, last["end"] + 1):
            head = [l for l in pages[pg - 1].splitlines() if l.strip()][:3]
            if any(BACK.match(l) for l in head):
                tail = {"title": "Back matter (detected)", "pdf": pg, "end": last["end"], "children": []}
                last["end"] = pg - 1
                chs.insert(body_idx[-1] + 1, tail)
                break
    numbered = any(chapter_number(ch["title"]) is not None for ch in chs if not ch.get("_whole"))

    used_ids = Counter()
    seq = 0
    for ch in chs:
        t = ch["title"]
        cls = "body" if ch.get("_whole") else classify_title(t)
        a, b = ch["pdf"], ch["end"]
        if ch.get("_parttitle"):
            add(f"x-{slug(t, 2)}", t, a, b, "part-title", action="skip", why="part title page")
            continue
        if ch.get("_whole"):
            base, kind = "main", "paper"
        elif cls == "skip":
            base, kind = f"x-{slug(t, 2)}", "back"
        else:
            num = chapter_number(t)
            m2 = re.match(r"^appendix to chapter (\d+)", t, re.I)
            if m2:
                base, kind = f"app-ch{int(m2.group(1)):02d}", "appendix"
            elif re.match(r"^appendi", t, re.I):
                m = re.match(r"^appendi\w*\s*\*?([A-Z0-9ivx]+)?", t, re.I)
                base = f"app{(m.group(1) or '').lower()}-{slug(t)}".replace("app-", "app-")
                kind = "appendix"
            elif cls == "front":
                base, kind = f"front-{slug(t)}", "front"
            elif re.match(r"^introduction", t, re.I) and num is None and numbered:
                base, kind = "ch00-introduction", "chapter"
            elif num is None and SIDE_TITLE.match(t):
                base, kind = slug(t, 2), "chapter"       # Afterword, Coda, Conclusion, Interlude ...
            else:
                seq += 1
                base, kind = f"ch{(num if num is not None else seq):02d}-{slug(t)}", "chapter"
        if used_ids[base] and ch.get("_part"):      # chapter numbers restart in a new Part
            base = f"pt{ch['_part']}-{base}"
        used_ids[base] += 1
        if used_ids[base] > 1:
            base = f"{base}-{used_ids[base]}"
        if cls == "skip":
            add(base, t, a, b, "back", action="skip", why="front/back matter")
            continue
        if cls == "front" and (work, base) not in KEEP_FRONT:
            add(base, t, a, b, "front", action="skip", why="preface/foreword")
            continue
        if b - a + 1 > SPLIT_PAGES:
            cuts = [k["pdf"] for k in ch.get("children", []) if k.get("pdf")]
            cuts += heading_pages(pages, a, b) if len(cuts) < 2 else []
            parts = split_ranges(a, b, cuts)
            for i, (pa, pb, how) in enumerate(parts, 1):
                add(f"{base}-p{i}", f"{t} (part {i}/{len(parts)})", pa, pb, kind,
                    why=f"split at {how} boundary")
        elif b == a and kind == "chapter":
            add(base, t, a, b, kind, action="skip", why="1-page entry (title/placeholder page?)")
        else:
            add(base, t, a, b, kind)
    return rows


H2 = "\u00a7H2\u00a7"


def ch_is_paper(chs):
    return len(chs) == 1 and chs[0].get("_whole")


def html_clean(p):
    """HTML -> plain text with line breaks; <h1>/<h2> starts are marked with H2. Used by planner and runner."""
    b = p.read_bytes()
    try:
        raw = b.decode("utf-8")
    except UnicodeDecodeError:
        raw = b.decode("latin-1")
    x = re.sub(r"<(script|style|nav|header|footer)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    x = re.sub(r"<h[12]\b[^>]*>", "\n" + H2 + " ", x, flags=re.I)
    x = re.sub(r"<(br|p|div|h\d|li|tr|pre|section)\b[^>]*>", "\n", x, flags=re.I)
    x = htmlmod.unescape(re.sub(r"<[^>]+>", "", x))
    x = re.sub(r"[ \t\u00a0\r]+", " ", x)
    x = re.sub(r"\n\s*\n+", "\n\n", x)
    # drop Project Gutenberg licence boilerplate at the end
    m = None
    for m in re.finditer(r"\*\*\*\s*END OF|End of (the )?Project Gutenberg|SMALL PRINT|THE END\b|"
                         r"Project Gutenberg(-tm)? License|This eBook is made available", x, re.I):
        if m.start() > 0.8 * len(x):
            break
    if m and m.start() > 0.8 * len(x):
        x = x[:m.start()]
    return x


CHAP_LINE = re.compile(r"^\s*(?:%s\s*)?(Chapter|CHAPTER)\s+([0-9]{1,2}|[IVXLC]{1,6})\b\.?(.*)$" % H2, re.M)
WORDS_PER_PAGE = 400


def plan_html(p, work, cat):
    text = html_clean(p)
    words = len(text.replace(H2, " ").split())
    base = {"work_id": work, "tier": cat.get("tier", ""), "field": cat.get("slug", ""),
            "type": cat.get("type", ""), "printed_pages": "", "image_pages": 0, "structure": "html"}

    def row(uid, title, s, e, kind="html", why=""):
        seg = text[s:e]
        w = len(seg.split())
        n = max(1, round(w / WORDS_PER_PAGE))
        return {**base, "unit_id": uid, "title": " ".join(title.split())[:100], "pdf_pages": f"c{s}-{e}",
                "n_pages": n, "est_tokens": est_input_tokens(len(seg), 0, n), "kind": kind,
                "action": "digest", "note": why or f"{w} words (~{n} pages at {WORDS_PER_PAGE} w/p)"}

    if words < STUB_WORDS:
        return [{**base, "unit_id": "main", "title": "(html stub)", "pdf_pages": "", "n_pages": 0,
                 "est_tokens": 0, "kind": "html", "action": "skip",
                 "note": f"landing/abstract page only ({words} words); need full text"}]
    if words <= SPLIT_PAGES * WORDS_PER_PAGE:
        return [row("main", cat.get("citation", "")[:80], 0, len(text))]
    # 1) "Chapter N" lines
    marks = []
    found = list(CHAP_LINE.finditer(text))
    if sum(H2 in m.group(0) for m in found) >= 3:      # prefer real headings over a contents list
        found = [m for m in found if H2 in m.group(0)]
    for m in found:
        num = m.group(2)
        num = int(num) if num.isdigit() else roman(num)
        if num and (not marks or num != marks[-1][1]):
            title = m.group(3).strip(" .")
            if not title:
                nxt = text[m.end():m.end() + 200].strip().split("\n")[0]
                title = nxt.strip()
            marks.append((m.start(), num, f"Chapter {num}. {title}"))
    rows = []
    if len(marks) >= 3:
        for i, (s, num, title) in enumerate(marks):
            e = marks[i + 1][0] if i + 1 < len(marks) else len(text)
            if len(text[s:e].split()) < 150:
                continue
            rows.append(row(f"ch{num:02d}-{slug(title)}", title, s, e, "html-chapter"))
        return rows
    # 2) group <h1>/<h2> sections into parts of about TARGET_PART pages
    cuts = [m.start() for m in re.finditer(re.escape(H2), text)] or [0]
    target = TARGET_PART * WORDS_PER_PAGE
    parts, start, acc = [], 0, 0
    for i, c in enumerate(cuts + [len(text)]):
        if c <= start:
            continue
        acc = len(text[start:c].split())
        if acc >= target:
            parts.append((start, c))
            start = c
    if start < len(text):
        parts.append((start, len(text)))
    for i, (s, e) in enumerate(parts, 1):
        rows.append(row(f"main-p{i}", f"part {i}/{len(parts)}", s, e, "html",
                        f"split at <h2> boundary; {len(text[s:e].split())} words"))
    return rows


# ---------------------------------------------------------------- cost

def est_cost(r):
    """P1 + P2 batch cost in USD (us multi-region). Output model is a guess until the pilot."""
    if r["action"] != "digest":
        return 0.0
    p = CFG["prices_usd_per_mtok"]["batch_us"]
    n = max(int(r["n_pages"]), 1)
    out1 = min(16000, 1500 + 200 * n)
    in1 = int(r["est_tokens"])
    in2 = in1 + out1 + 600
    out2 = 1200 + 0.15 * out1        # edit-based repairs (verify.md 2026-10-12); ~5% full rewrites
    return ((in1 + in2) * p["input"] + (out1 + out2) * p["output"]) / 1e6


def _range(r):
    m = re.fullmatch(r"c?(\d+)-(\d+)", r.get("pdf_pages") or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


def merge_tiny(rs):
    """Merge digest units of <= MERGE_PAGES pages into the next digest unit (or the previous if last)."""
    dig = [i for i, r in enumerate(rs) if r.get("action") == "digest" and _range(r)]
    html = any((r.get("pdf_pages") or "").startswith("c") for r in rs)
    drop = set()
    for k, i in enumerate(dig):
        r = rs[i]
        if int(r["n_pages"]) > MERGE_PAGES or len(dig) < 2:
            continue
        a, b = _range(r)
        nxt = next((j for j in dig[k + 1:] if j not in drop), None)
        prv = next((j for j in reversed(dig[:k]) if j not in drop), None)
        tgt = None
        if nxt is not None and _range(rs[nxt])[0] - b <= (1 if html else 4):
            tgt = nxt
        elif nxt is None and prv is not None and a - _range(rs[prv])[1] <= (1 if html else 4):
            tgt = prv
        if tgt is None:
            r["action"], r["note"] = "skip", "tiny entry that cannot merge (title page?)"
            continue
        T = rs[tgt]
        ta, tb = _range(T)
        lo, hi = min(a, ta), max(b, tb)
        pre = "c" if html else ""
        T["pdf_pages"] = f"{pre}{lo}-{hi}"
        T["n_pages"] = (hi - lo + 1) if not html else int(T["n_pages"]) + int(r["n_pages"])
        T["image_pages"] = int(T["image_pages"]) + int(r["image_pages"])
        T["est_tokens"] = int(T["est_tokens"]) + int(r["est_tokens"]) - PROMPT_OVERHEAD - SPINE_TOKENS
        if not html and r.get("printed_pages") and T.get("printed_pages"):
            p1, p2 = (r["printed_pages"].split("-") + [""])[:2], (T["printed_pages"].split("-") + [""])[:2]
            T["printed_pages"] = f"{p1[0]}-{p2[1]}" if tgt > i else f"{p2[0]}-{p1[1]}"
        T["note"] = "; ".join(x for x in (T.get("note"), f"includes {r['unit_id']} ({r['title'][:40]})") if x)
        drop.add(i)
    return [r for i, r in enumerate(rs) if i not in drop]


# ---------------------------------------------------------------- main

FIELDS = ["work_id", "unit_id", "title", "pdf_pages", "printed_pages", "n_pages", "image_pages",
          "est_tokens", "tier", "field", "type", "kind", "structure", "action", "est_cost_usd",
          "file", "note"]


def plan():
    cat = catalog()
    files = source_files()
    by_work = {}
    for p in files:
        w = match_id(file_stem(p), cat)
        by_work.setdefault(w, []).append(p)
    # identical text content under two different work ids: digest it once
    import hashlib
    seen_hash, same_as = {}, {}
    for work, ps in sorted(by_work.items(), key=lambda kv: str(kv[0])):
        for p in ps:
            tc = PIPE / "_work" / "text" / (p.name + ".txt")
            if p.suffix == ".pdf" and tc.exists() and tc.stat().st_size > 1000:
                h = hashlib.sha1(tc.read_bytes()).hexdigest()
                if h in seen_hash and seen_hash[h] != work:
                    same_as[work] = seen_hash[h]
                seen_hash.setdefault(h, work)
    rows = []
    for work, ps in sorted(by_work.items(), key=lambda kv: str(kv[0])):
        if work in same_as:
            c = cat.get(work, {})
            rows.append({"work_id": work, "unit_id": "-", "title": "(same text as another work)", "action": "skip",
                         "tier": c.get("tier", ""), "field": c.get("slug", ""), "type": c.get("type", ""),
                         "file": str(ps[0].relative_to(LIB)),
                         "note": f"PDF text identical to {same_as[work]}; digested once there — need the real edition"})
            continue
        c = cat.get(work, {})
        if work is None:
            for p in ps:
                rows.append({"work_id": file_stem(p), "unit_id": "-", "action": "skip",
                             "file": str(p.relative_to(LIB)), "note": "no catalog id"})
            continue
        # duplicates: prefer PDF over HTML, then the largest file; report the rest
        ps = sorted(ps, key=lambda p: (p.suffix == ".pdf", p.stat().st_size), reverse=True)
        for extra in ps[1:]:
            rows.append({"work_id": work, "unit_id": "-", "title": "(duplicate file)", "action": "skip",
                         "tier": c.get("tier", ""), "field": c.get("slug", ""), "type": c.get("type", ""),
                         "file": str(extra.relative_to(LIB)),
                         "note": f"same catalog id as {ps[0].name}; skipped (reviews/gate1.md)"})
        p = ps[0]
        try:
            rs = plan_pdf(p, work, c) if p.suffix == ".pdf" else plan_html(p, work, c)
        except Exception as e:
            rs = [{"work_id": work, "unit_id": "-", "action": "error", "note": f"{type(e).__name__}: {e}"[:200]}]
        if c.get("type") != "paper":
            rs = merge_tiny(rs)
        for r in rs:
            r["file"] = str(p.relative_to(LIB))
            if r.get("action") == "digest" and (work in HOLD or work in SKIP_WORKS):
                r["action"], r["note"] = "skip", HOLD.get(work) or SKIP_WORKS[work]
        rows += rs
    for r in rows:
        r["est_cost_usd"] = f"{est_cost(r):.3f}" if r.get("action") == "digest" else ""
    UNITS_CSV.parent.mkdir(exist_ok=True)
    with open(UNITS_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return rows


def summary(rows):
    acts = Counter(r.get("action") for r in rows)
    dig = [r for r in rows if r.get("action") == "digest"]
    pages = sum(int(r["n_pages"]) for r in dig)
    imgs = sum(int(r["image_pages"]) for r in dig)
    toks = sum(int(r["est_tokens"]) for r in dig)
    cost = sum(float(r["est_cost_usd"]) for r in dig)
    works = len({r["work_id"] for r in rows})
    by_tier = Counter()
    for r in dig:
        by_tier[r["tier"]] += float(r["est_cost_usd"])
    return {"works": works, "actions": dict(acts), "digest_units": len(dig), "digest_pages": pages,
            "image_pages": imgs, "input_tokens_p1": toks, "est_cost_p1_p2_usd": round(cost, 2),
            "cost_by_tier": {k: round(v, 2) for k, v in by_tier.items()},
            "needs_toc": sorted({r["work_id"] for r in rows if r.get("action") == "needs-toc"})}
