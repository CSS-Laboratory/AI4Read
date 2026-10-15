#!/usr/bin/env python3
"""AI4Read knowledge graph builder (phase 2): deterministic extraction from digests plus
curated data files.

Reads wiki/works/<work>/<unit>.md digests (skips *.cc.md and *.pipeline.md, except
that cover-2006-elements/ch02-entropy is read from its .pipeline.md), canon/catalog.json,
canon/<field>.md, and the curated phase-2 files in wiki/kg/:

  aliases.json            variant concept id -> canonical id (curated by judgment)
  field-map.json          free-text bridge target field -> canon field id or other:<name>
  work-fields.json        field overrides for works (and units) that span several fields
  instance-matches.json   confirmed canon-instance matches (manual confirm list)

and writes:

  wiki/kg/concepts.jsonl, instances.jsonl, bridges.jsonl   one record per line
  wiki/kg/merge-candidates.md                               remaining groups to review
  wiki/kg/unmatched-instances.md                            canon instances with no match
  wiki/kg/index.md                                          statistics
  wiki/concepts/<id>.md, wiki/instances/<id>.md             generated pages
  wiki/kg/hub-sources/<id>.md                               generated page for a curated hub

Generated pages carry `generated_by: build_kg.py`; only such pages are deleted on a rebuild.
A page whose frontmatter has a `curated:` key is never overwritten or deleted: its generated
version goes to wiki/kg/hub-sources/<id>.md instead.
Stdlib only; output is deterministic. Usage: python3 scripts/build_kg.py
"""
import fnmatch
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKS = ROOT / "wiki" / "works"
KG = ROOT / "wiki" / "kg"
CONCEPT_DIR = ROOT / "wiki" / "concepts"
INSTANCE_DIR = ROOT / "wiki" / "instances"
HUB_SOURCES = KG / "hub-sources"
CANON = ROOT / "canon"
PIPELINE_OVERRIDES = {("cover-2006-elements", "ch02-entropy")}
GEN_MARK = "generated_by: build_kg.py"
CURATED_RE = re.compile(r"\A---\s*\n(?:.*\n)*?curated:\s*\S", re.M)
BRIDGE_CAP = 50  # bridge lines shown per page (the total is always stated)
INSTANCE_CAP = 50

SECTION_CONCEPTS = "Concepts"
SECTION_INSTANCES = "Canonical instances"
SECTION_BRIDGES = "Bridges (candidates)"

FIELDS = ["analytic-philosophy", "bayesian", "communication-theory", "complex-systems",
          "control-theory", "decision-game-theory", "economics-finance",
          "information-theory", "linear-algebra", "llm", "political-science",
          "theory-of-mind"]
TIER_RANK = {"core": 0, "deep": 1, "reference": 2}

# Keyword rules mapping a bridge's free-text target field to a canon field slug, used only
# for target texts that are not in field-map.json. The earliest match in the text wins.
TARGET_RULES = {
    "analytic-philosophy": [r"analytic.philosophy", r"philosoph", r"epistemolog", r"metaphysic",
                            r"\b(formal|modal|predicate|propositional|first.order|mathematical|epistemic|philosophical|boolean) logic\b",
                            r"^logic$", r"\bsemantics\b", r"\bpragmatics\b", r"implicature",
                            r"speech.act"],
    "bayesian": [r"bayes", r"causal", r"\bmcmc\b", r"hierarchical model", r"multilevel",
                 r"partial pooling", r"variational inference", r"gibbs sampl"],
    "communication-theory": [r"communication", r"\bmedia\b", r"journalism", r"framing",
                             r"agenda.setting", r"two.step.flow", r"persuasion", r"rhetoric",
                             r"selective exposure", r"encoding/decoding", r"spiral of silence",
                             r"cultivation", r"uses and gratifications", r"diffusion (of innovations|research)",
                             r"misinformation", r"\bnews\b", r"public sphere", r"propaganda"],
    "complex-systems": [r"complex.systems?", r"network science", r"network analysis",
                        r"statistical physics", r"statistical mechanics", r"dynamical systems?",
                        r"nonlinear dynamics", r"complex contagion", r"agent.based", r"opinion dynamics",
                        r"\bchaos\b", r"bifurcation", r"self.organi[sz]", r"percolation",
                        r"social network"],
    "control-theory": [r"\bcontrol", r"cybernetic", r"reinforcement learning", r"dynamic programming",
                       r"\bfeedback", r"kalman", r"\blqr\b", r"state.space model", r"\bpid\b",
                       r"homeosta", r"thermostat"],
    "decision-game-theory": [r"decision.game", r"game.theor", r"decision theor", r"mechanism design",
                             r"social choice", r"bounded rationality", r"repeated games?",
                             r"\bsignal+ing\b", r"coordination game", r"bargaining", r"auction",
                             r"prospect theory", r"expected utility", r"heuristics and biases",
                             r"behavioral decision", r"nash", r"evolutionar\w* game"],
    "economics-finance": [r"econom", r"financ", r"\bmarkets?\b", r"monetary", r"portfolio",
                          r"asset pric"],
    "information-theory": [r"information.theor", r"information \(shannon\)", r"coding theory",
                           r"\bshannon\b", r"channel coding", r"source coding", r"rate.distortion",
                           r"kolmogorov complexity", r"minimum description length", r"\bmdl\b",
                           r"\bentropy\b"],
    "linear-algebra": [r"linear.algebra", r"\bmatri(x|ces)\b", r"eigen", r"spectral", r"\bpca\b",
                       r"principal component", r"\bsvd\b", r"singular value", r"least squares",
                       r"graph laplacian"],
    "llm": [r"\bllms?\b", r"language model", r"transformer", r"\bnlp\b", r"natural language processing",
            r"machine learning", r"deep learning", r"neural net", r"\bml\b", r"word embedding",
            r"word vectors?", r"in-context learning", r"\brlhf\b", r"supervised learning"],
    "political-science": [r"politic", r"\bvot(e|ing|er)", r"\bveto\b", r"collective action",
                          r"institution", r"public opinion", r"\belections?\b", r"democra", r"agenda control",
                          r"legislat", r"partisan", r"polariz", r"international relations"],
    "theory-of-mind": [r"theory.of.mind", r"mind.?reading", r"mentali[sz]", r"false.belief",
                       r"intentional stance", r"folk psychology", r"social cognition"],
}
TARGET_RES = [(f, re.compile(p, re.I)) for f, ps in TARGET_RULES.items() for p in ps]

PAGE_RE = re.compile(r"\(([^()]*(?:\bpp?\.\s*[ivxlcdm\d]|\bpdf\s*\d|§|\bn\.\s*\d)[^()]*)\)", re.I)
SEP_RE = re.compile(r"\s+[—–]\s+|\s+--\s+|\s+-\s+")
WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
BACKTICK_RE = re.compile(r"`([^`]+)`")
NOTE_RE = re.compile(r"^\(\s*(none|no\b|n/a|not\b|nothing)", re.I)
# a further "[[id]] (new) — definition" entry packed into one bullet after ; or .
EMBEDDED_RE = re.compile(r"(?:(?<=;)|(?<=\.))\s+(?=\[\[[^\]]+\]\](?:\s*\(\s*new\s*\))?\s+[—–]\s+)")
# definitions that say the concept is not really used in the unit (canon link only, loose)
WEAK_RE = re.compile(
    r"canon link[^)]*\bnot (stated|used|named|defined|discussed)|not stated in (this|the) unit|"
    r"not (used|named|defined|mentioned|stated|discussed)( as such)? (here|in this unit|on these pages|in this chapter)|"
    r"only loosely|loosely related|related only loosely|only a loose link|\bloose link|"
    r"the term (itself )?is not used|does not use (this|the) term|neither term appears|"
    r"is not used in this unit|^\W*not used here|^\W*not in this unit", re.I)
BRIDGE_ALT_SPLIT = re.compile(r"\s+(?:vs\.?|versus|like)\s+")


# ---------------------------------------------------------------- normalisation
def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def norm_id(raw):
    """lowercase, hyphens for spaces/underscores/slashes/dashes, strip punctuation and (new)."""
    s = strip_accents(raw).strip()
    s = re.sub(r"\(\s*new[^)]*\)\s*$", "", s, flags=re.I).strip()
    s = s.lower()
    s = re.sub(r"[\s_/&+–—−‐-]+", "-", s)
    s = re.sub(r"[^\w-]", "", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s


def fold_token(t):
    if len(t) > 4 and t.endswith("ies"):
        return t[:-3] + "y"
    if t.endswith("sses"):
        return t[:-2]
    if len(t) > 3 and t.endswith("s") and not t.endswith(("ss", "us", "is")):
        return t[:-1]
    return t


def fold_id(nid):
    """singular/plural folding per token; hyphens kept."""
    return "-".join(fold_token(t) for t in nid.split("-") if t)


STOP = {"the", "a", "an", "of", "and", "as", "vs", "v", "with", "to", "in", "on", "for",
        "is", "what", "by", "at", "or", "s"}
# generic words dropped when comparing instance titles
GENERIC = STOP | {"example", "task", "problem", "game", "experiment", "puzzle", "case", "study",
                  "test", "model", "story", "illustration", "demo", "toy"}


def content_tokens(nid):
    return {fold_token(t) for t in re.sub(r"(?<=[a-z])s-", "-", nid + "-").split("-") if t and t not in STOP} - {""}


def title_key(nid):
    """order-free key of the informative tokens of an instance title."""
    toks = {fold_token(t) for t in re.sub(r"(?<=[a-z])s-", "-", nid + "-").split("-") if t}
    return frozenset(t for t in toks if t and t not in GENERIC and not t.isdigit())


def tokens(text):
    s = strip_accents(text).lower()
    s = re.sub(r"[’']", "", s)
    return [fold_token(t) for t in re.split(r"[^\w]+|_", s) if t]


def norm_target(t):
    """key used for field-map.json lookups."""
    s = strip_accents(t).strip().strip("*_ ").lower()
    s = re.sub(r"\s+", " ", s)
    return s.rstrip(" .;,")


def load_json(path, default):
    if not path.exists():
        return default
    data = json.loads(path.read_text())
    if isinstance(data, dict):
        return {k: v for k, v in data.items() if not k.startswith("_")}
    return data


# ---------------------------------------------------------------- canon
def load_catalog():
    """id -> list of catalog records (a work can be listed under several fields)."""
    out = defaultdict(list)
    for c in json.loads((CANON / "catalog.json").read_text()):
        out[c["id"]].append(c)
    return out


def canon_section(text, name):
    m = re.search(r"^## " + re.escape(name) + r"\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def bold_items(section):
    out = []
    for line in section.splitlines():
        m = re.match(r"^- \*\*(.+?)\*\*\s*[—–-]\s*(.*)$", line.strip())
        if m:
            out.append((m.group(1).strip(), m.group(2).strip()))
    return out


def name_aliases(name):
    """Deterministic alias forms of a canon name: full, without parentheticals,
    the parenthetical contents, and each part split on / & , 'vs.'."""
    base = re.sub(r"[\"“”*]", "", name)
    forms = {base, re.sub(r"\([^)]*\)", " ", base), re.sub(r"['’]s\b", "", base)}
    forms.update(re.findall(r"\(([^)]*)\)", base))
    forms.add(re.sub(r"\s+[A-Z]\w{0,2}\([^)]*\)\s*$", "", base))
    parts = set()
    for f in forms:
        for p in re.split(r"\s+/\s+|/|\s+&\s+|\s+vs\.?\s+|,\s+", f):
            parts.add(p)
    forms |= parts
    return {norm_id(f) for f in forms if norm_id(f)}


WORK_ID_RE = re.compile(r"\b[a-z0-9]+(?:-[a-z0-9]+)*-\d{4}-[a-z0-9]+(?:-[a-z0-9]+)*\b")


def load_canon():
    spine, inst = {}, {}
    for f in sorted(CANON.glob("*.md")):
        text = f.read_text()
        m = re.search(r"^slug:\s*(\S+)", text, re.M)
        if not m:
            continue
        slug = m.group(1)
        for name, desc in bold_items(canon_section(text, "Concept spine")):
            cid = norm_id(name)
            spine.setdefault(cid, {"id": cid, "name": name, "field": slug, "def": desc,
                                   "aliases": name_aliases(name)})
        for name, desc in bold_items(canon_section(text, "Canonical instances")):
            iid = norm_id(name)
            works = []
            if " — " in desc:
                tail = desc.rsplit(" — ", 1)[1]
                works = sorted(set(WORK_ID_RE.findall(tail)), key=tail.find)
            inst.setdefault(iid, {"id": iid, "name": name, "field": slug, "def": desc,
                                  "aliases": name_aliases(name), "works": works})
    return spine, inst


# ---------------------------------------------------------------- work fields
class WorkFields:
    """Field(s) of each digest: catalog listing(s), then work-fields.json overrides."""

    def __init__(self, catalog, overrides):
        self.catalog, self.over = catalog, overrides.get("works", {})

    def get(self, work, unit, fm_fields):
        recs = self.catalog.get(work, [])
        recs = sorted(recs, key=lambda c: (TIER_RANK.get(c.get("tier"), 9), FIELDS.index(c["slug"]) if c["slug"] in FIELDS else 99))
        fields = [c["slug"] for c in recs]
        tier = recs[0].get("tier", "") if recs else ""
        source = "catalog" if len(fields) > 1 else ""
        o = self.over.get(work)
        if o:
            fields = list(o.get("fields") or fields)
            source = "work-fields.json"
            for u in o.get("units", []):
                if any(fnmatch.fnmatchcase(unit, pat) for pat in u["units"]):
                    fields += [f for f in u["add"] if f not in fields]
                    source = "work-fields.json (unit)"
        if not fields:
            fields = fm_fields[:1] or ["unknown"]
        return fields, tier, source


# ---------------------------------------------------------------- digests
def digest_files():
    out = []
    for wdir in sorted(p for p in WORKS.iterdir() if p.is_dir()):
        for f in sorted(wdir.glob("*.md")):
            if f.name.endswith((".cc.md", ".pipeline.md")):
                continue
            unit = f.stem
            if (wdir.name, unit) in PIPELINE_OVERRIDES:
                f = wdir / f"{unit}.pipeline.md"
            out.append((wdir.name, unit, f))
    return out


def sections(text):
    secs, cur = defaultdict(list), None
    for line in text.splitlines():
        if line.startswith("## "):
            cur = line[3:].strip()
            continue
        if cur:
            secs[cur].append(line)
    return secs


def frontmatter_fields(text):
    m = re.search(r"^fields:\s*\[(.*?)\]", text, re.M)
    return [x.strip() for x in m.group(1).split(",") if x.strip()] if m else []


def split_page(text):
    """Return (text without trailing page ref, page ref) using the last page parenthetical."""
    refs = list(PAGE_RE.finditer(text))
    if not refs:
        return text.strip(), ""
    last = refs[-1]
    page = last.group(1).strip()
    tail = text[last.end():].strip()
    if re.fullmatch(r"[.;,]?", tail):
        text = text[:last.start()].rstrip(" ;,")
    return text.strip(), page


def plain_words(s):
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"[*_]", "", s)
    return s.split()


def parse_entry(line):
    """Parse '- <head> — <definition>' into ([(raw, new)], definition, page),
    'note' for an explanatory note such as '(none ...)', or None if unparseable."""
    s = line.strip()
    if not s.startswith(("- ", "* ")):
        return None
    s = s[2:].strip()
    if not s:
        return None
    if NOTE_RE.match(s):
        return "note"
    m = SEP_RE.search(s)
    if m:
        head, rest = s[:m.start()], s[m.end():]
    else:
        head, rest = s, ""
    raws = []
    links = list(WIKILINK_RE.finditer(head)) or list(BACKTICK_RE.finditer(head))
    if links:
        for i, lk in enumerate(links):
            nxt = links[i + 1].start() if i + 1 < len(links) else len(head)
            after = head[lk.end():nxt]
            raw = lk.group(1).split("|")[0].strip()
            raws.append((raw, bool(re.search(r"\(\s*new\b", after, re.I))))
        if not m:  # no separator: everything after the last link is the "definition"
            rest = head[links[-1].end():]
    else:
        if not m:
            # a bare description with a page ref, e.g. "Random threshold rounding ... (p. 178)."
            text, page = split_page(s)
            words = plain_words(text)
            if not page or not words or len(words) > 12:
                return None
            return [(" ".join(words), False)], "", page
        plain = re.sub(r"\([^)]*\)", " ", head)
        plain = re.sub(r"[*_]", "", plain).strip()
        if len(plain.split()) > 8:
            # long head: use the label before the first comma, keeping a numbered parenthetical
            short = re.split(r",|:", head, maxsplit=1)[0]
            short = re.sub(r"[*_]", "", short).strip()
            plain = short if 0 < len(short.split()) <= 8 else ""
        if not plain:
            return None
        raws.append((plain, bool(re.search(r"\(\s*new\b", head, re.I))))
    rest = rest.strip()
    if re.match(r"\(\s*new\)", rest, re.I):
        rest = re.sub(r"^\(\s*new\)\s*", "", rest, flags=re.I)
        raws = [(r, True) for r, _ in raws]
    rest = re.sub(r"^[—–-]\s*", "", rest)
    definition, page = split_page(rest)
    if definition.startswith("(") and definition.endswith(")") and not page:
        page = definition[1:-1]
        definition = ""
    return raws, definition, page


def parse_entries(line):
    """A bullet may pack several '[[id]] — definition' entries separated by ; or ."""
    s = line.strip()
    parts = EMBEDDED_RE.split(s)
    if len(parts) == 1:
        return [parse_entry(line)]
    out = [parse_entry(parts[0])]
    out += [parse_entry("- " + p.strip()) for p in parts[1:]]
    return out


def outside_math(text, ch_pred):
    inmath = False
    for i, ch in enumerate(text):
        if ch == "$":
            inmath = not inmath
        elif not inmath and ch_pred(text, i):
            return i
    return -1


def parse_bridge(line):
    s = line.strip()
    m = re.match(r"^[-*]\s+\[([^\]]+)\]\s*(.*)$", s)
    if not m:
        return None
    ltype = norm_id(m.group(1))
    body = m.group(2).strip()
    arrow = "↔" in body
    if arrow:
        left, after = body.split("↔", 1)
    else:
        # no ↔: split "A vs. B — why" or "A like B (...)" at the first such word outside math
        d = body.find(" — ")
        main_part = body if d < 0 else body[:d]
        mm = None
        for cand in BRIDGE_ALT_SPLIT.finditer(main_part):
            if outside_math(main_part[:cand.start()] + "#", lambda t, i: t[i] == "#") == cand.start():
                mm = cand
                break
        if mm:
            left, after = main_part[:mm.start()], main_part[mm.end():] + ("" if d < 0 else body[d:])
        else:
            left, after = body, ""
    left, after = left.strip(), after.strip()
    dash = outside_math(after, lambda t, i: t[i] in "—" and t[i - 1:i] == " ")
    if dash < 0:
        dash = outside_math(after, lambda t, i: t[i] == "–" and t[i - 1:i] == " " and t[i + 1:i + 2] == " ")
    main = after if dash < 0 else after[:dash]
    why = "" if dash < 0 else after[dash + 1:].strip()
    colon = outside_math(main, lambda t, i: t[i] == ":") if arrow else -1
    if colon >= 0:
        target, right = main[:colon].strip(), main[colon + 1:].strip()
    else:
        target, right = "", main.strip()
    if not after:
        d = left.find(" — ")
        if d >= 0:
            left, why = left[:d], left[d + 3:]
    _, page = split_page(s)
    return {"type": ltype, "left": left.strip(), "target_raw": target, "right": right,
            "why": why.strip(), "page": page, "arrow": arrow}


def map_target_rules(target):
    best = None
    for f, rx in TARGET_RES:
        m = rx.search(target)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), f)
    return best[1] if best else None


def field_root(f):
    return f.split(":", 1)[0]


# ---------------------------------------------------------------- main build
def main():
    catalog = load_catalog()
    spine, canon_inst = load_canon()
    aliases = load_json(KG / "aliases.json", {})
    field_map = load_json(KG / "field-map.json", {})
    wf = WorkFields(catalog, load_json(KG / "work-fields.json", {}))
    inst_conf = load_json(KG / "instance-matches.json", {})
    for v, c in aliases.items():
        if c in aliases:
            sys.exit(f"aliases.json: canonical id {c} is itself a variant (from {v})")
    canon_of = lambda i: aliases.get(i, i)

    concepts, instances, bridges = [], [], []
    problems = Counter()
    problem_examples = defaultdict(list)
    notes = Counter()
    work_field_source = {}

    files = digest_files()
    for work, unit, path in files:
        text = path.read_text()
        fm = frontmatter_fields(text)
        fields, tier, src = wf.get(work, unit, fm)
        if work not in catalog:
            problems["work not in catalog"] += 1
        if src:
            work_field_source[work] = src
        meta = {"work": work, "unit": unit, "digest": f"{work}/{unit}", "field": fields[0],
                "fields": fields, "fm_fields": fm, "tier": tier}
        secs = sections(text)
        for sec, store in ((SECTION_CONCEPTS, concepts), (SECTION_INSTANCES, instances)):
            if sec not in secs:
                problems[f"missing section {sec}"] += 1
            seen = OrderedDict()
            for line in secs.get(sec, []):
                if not line.strip().startswith(("- ", "* ")):
                    continue
                for parsed in parse_entries(line):
                    if parsed == "note":
                        notes[sec] += 1
                        continue
                    if not parsed:
                        problems[f"unparsed {sec} line"] += 1
                        problem_examples[f"unparsed {sec} line"].append(f"{meta['digest']}: {line.strip()[:120]}")
                        continue
                    raws, definition, page = parsed
                    for raw, new in raws:
                        nid = norm_id(raw)
                        if not nid:
                            problems[f"empty id after normalisation ({sec})"] += 1
                            continue
                        cid = canon_of(nid) if sec == SECTION_CONCEPTS else nid
                        if cid in seen:
                            r = seen[cid]
                            r["other_definitions"].append(definition)
                            r["new"] = r["new"] or new
                            if nid not in r["variants"]:
                                r["variants"].append(nid)
                            continue
                        seen[cid] = dict(id=cid, norm_id=nid, raw=raw, **meta, definition=definition,
                                         page=page, new=new, multi_id_line=len(raws) > 1,
                                         other_definitions=[], variants=[nid])
            for r in seen.values():
                r["weak"] = bool(WEAK_RE.search(r["definition"])) and not any(
                    od and not WEAK_RE.search(od) for od in r["other_definitions"])
            store.extend(seen.values())
        for line in secs.get(SECTION_BRIDGES, []):
            if not line.strip().startswith(("- ", "* ")):
                continue
            b = parse_bridge(line)
            if not b:
                problems["unparsed bridge line"] += 1
                problem_examples["unparsed bridge line"].append(f"{meta['digest']}: {line.strip()[:120]}")
                continue
            if not b["arrow"]:
                notes["bridge without ↔ (split on vs./like)"] += 1
            if b["type"] not in ("same-math", "structural-analogy", "metaphor"):
                problems["bridge with nonstandard type"] += 1
            if b["target_raw"]:
                key = norm_target(b["target_raw"])
                if key in field_map:
                    b["target_field"], b["target_rule"] = field_map[key], "field-map"
                else:
                    f = map_target_rules(b["target_raw"])
                    b["target_field"], b["target_rule"] = (f, "keyword") if f else ("other", "none")
            else:
                b["target_field"], b["target_rule"] = "unspecified", ""
            b.update(source=meta["digest"], work=work, unit=unit, source_field=fields[0],
                     source_fields=fields, tier=tier)
            bridges.append(b)

    KG.mkdir(parents=True, exist_ok=True)
    for name, recs in (("concepts", concepts), ("instances", instances), ("bridges", bridges)):
        with open(KG / f"{name}.jsonl", "w") as fh:
            for r in recs:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # ---- aggregate by id
    def group(recs):
        g = defaultdict(list)
        for r in recs:
            g[r["id"]].append(r)
        return g
    cg, ig = group(concepts), group(instances)

    # canon spine entries per canonical id (several spine names can alias to one id)
    spine_by = defaultdict(list)
    for sid in sorted(spine):
        spine_by[canon_of(sid)].append(spine[sid])
    variants_by = defaultdict(set)
    for v, c in aliases.items():
        variants_by[c].add(v)

    # token index over bridges and instance lines for "mentions"
    def index(texts):
        inv = defaultdict(set)
        toks = []
        for i, t in enumerate(texts):
            tk = tokens(t)
            toks.append(tk)
            for x in set(tk):
                inv[x].add(i)
        return inv, toks
    btexts = [" ".join([b["left"], b["target_raw"], b["right"], b["why"]]) for b in bridges]
    binv, btoks = index(btexts)
    itexts = [r["raw"].replace("-", " ") + " " + r["definition"] for r in instances]
    iinv, itoks = index(itexts)

    def mentions1(cid, inv, toks):
        q = [fold_token(t) for t in cid.split("-") if t]
        if not q:
            return set()
        cand = set.intersection(*(inv.get(t, set()) for t in q))
        n = len(q)
        return {i for i in cand if any(toks[i][j:j + n] == q for j in range(len(toks[i]) - n + 1))}

    def mentions(cid, inv, toks, extra=()):
        out = set()
        for x in (cid, *extra):
            out |= mentions1(x, inv, toks)
        return sorted(out)

    def all_fields(recs, strong_only=False):
        c = Counter()
        for r in recs:
            if strong_only and r.get("weak"):
                continue
            for f in r["fields"]:
                c[f] += 1
        return c

    def ordered_fields(recs, strong_only=False):
        c = all_fields(recs, strong_only)
        return [f for f, _ in sorted(c.items(), key=lambda x: (-x[1], x[0]))]

    def ordered_tiers(recs):
        c = Counter(r["tier"] for r in recs if r["tier"])
        return [t for t, _ in sorted(c.items(), key=lambda x: (-x[1], x[0]))]

    def n_digests(recs):
        return len({r["digest"] for r in recs})

    def yaml_list(xs):
        return "[" + ", ".join(json.dumps(x, ensure_ascii=False) if re.search(r"[,:\[\]{}#&*!|>'\"%@`]", x) else x for x in xs) + "]"

    def page_ref(p):
        if not p:
            return ""
        return f" ({p})" if re.match(r"(pp?\.|pdf|§|n\.)", p) else f" (p. {p})"

    def source_lines(recs):
        out = []
        by_field = defaultdict(list)
        for r in recs:
            by_field[r["field"]].append(r)
        for f in sorted(by_field, key=lambda f: (-len(by_field[f]), f)):
            out.append(f"\n### {f}\n")
            for r in sorted(by_field[f], key=lambda r: r["digest"]):
                notes_ = []
                al = [v for v in r.get("variants", []) if v != r["id"]]
                if r["raw"] != r["id"] and r["raw"] not in al:
                    notes_.append(f"as `{r['raw']}`")
                if al:
                    notes_.append("alias " + ", ".join(f"`{v}`" for v in al))
                if r["new"]:
                    notes_.append("new")
                if r.get("weak"):
                    notes_.append("weak: not really used in this unit")
                if len(r["fields"]) > 1:
                    notes_.append("work fields: " + ", ".join(r["fields"]))
                note = f" [{'; '.join(notes_)}]" if notes_ else ""
                d = r["definition"] or "(no definition given)"
                out.append(f"- [[{r['digest']}]]{page_ref(r['page'])}: {d}{note}")
                for od in r["other_definitions"]:
                    out.append(f"  - also: {od}")
        return out

    def bridge_lines(idxs):
        out = []
        for i in idxs[:BRIDGE_CAP]:
            b = bridges[i]
            tgt = f"{b['target_raw']}: " if b["target_raw"] else ""
            why = f" — {b['why']}" if b["why"] else ""
            out.append(f"- [{b['type']}] {b['left']} ↔ {tgt}{b['right']}{why} — from [[{b['source']}]] ({b['source_field']} → {b['target_field']})")
        if len(idxs) > BRIDGE_CAP:
            out.append(f"- … {len(idxs) - BRIDGE_CAP} more bridge lines mention this id (see wiki/kg/bridges.jsonl)")
        return out

    def is_curated(path):
        return path.exists() and bool(CURATED_RE.search(path.read_text()[:4000]))

    def clear(d):
        d.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*.md"):
            t = f.read_text()[:4000]
            if GEN_MARK in t and not CURATED_RE.search(t):
                f.unlink()

    curated_hubs = []

    def write_page(d, pid, content):
        path = d / f"{pid[:150]}.md"
        if is_curated(path):
            HUB_SOURCES.mkdir(parents=True, exist_ok=True)
            (HUB_SOURCES / path.name).write_text(content)
            curated_hubs.append(pid)
            return
        path.write_text(content)

    # ---- concept pages
    clear(CONCEPT_DIR)
    if HUB_SOURCES.exists():
        for f in HUB_SOURCES.glob("*.md"):
            f.unlink()
    # ids linked from curated hub pages get a page even with a single digest
    hub_linked = set()
    for f in CONCEPT_DIR.glob("*.md"):
        t = f.read_text()
        if CURATED_RE.search(t[:4000]):
            hub_linked |= {canon_of(norm_id(x.split("|")[0])) for x in WIKILINK_RE.findall(t) if "/" not in x}
            m = re.search(r"^links:\s*\[(.*?)\]", t, re.M)
            if m:
                hub_linked |= {canon_of(norm_id(x)) for x in m.group(1).split(",") if x.strip()}
    concept_page_ids = sorted({c for c, rs in cg.items() if n_digests(rs) >= 2} | set(spine_by)
                              | (hub_linked & set(cg)))
    for cid in concept_page_ids:
        recs = cg.get(cid, [])
        sps = spine_by.get(cid, [])
        fields = ordered_fields(recs) or sorted({sp["field"] for sp in sps})
        used_variants = sorted({v for r in recs for v in r.get("variants", []) if v != cid})
        all_variants = sorted(variants_by.get(cid, set()) | set(used_variants))
        fm = ["---", f"id: {cid}", "type: concept", f"fields: {yaml_list(fields)}",
              f"fields_strong: {yaml_list(ordered_fields(recs, True))}",
              f"n_sources: {n_digests(recs)}", f"n_works: {len({r['work'] for r in recs})}",
              f"tiers: {yaml_list(ordered_tiers(recs))}",
              "grounding: digests", f"sources: {yaml_list(sorted({r['digest'] for r in recs}))}"]
        if all_variants:
            fm.append(f"aliases: {yaml_list(all_variants)}")
        raws = sorted({r["raw"] for r in recs if r["raw"] != cid and norm_id(r["raw"]) not in all_variants})
        if raws:
            fm.append(f"raw_ids: {yaml_list(raws)}")
        if sps:
            fm.append(f"canon_spine: {yaml_list(sorted({sp['field'] for sp in sps}))}")
        fm += [GEN_MARK, "---", "", f"# {cid}", ""]
        body = []
        if all_variants:
            body += ["## Aliases", "", "Variant ids merged into this page (curated in `wiki/kg/aliases.json`):", ""]
            for v in all_variants:
                n = len({r["digest"] for r in recs if v in r.get("variants", [])})
                body.append(f"- `{v}` — {n} digest(s)")
            body.append("")
        for sp in sps:
            body += ["## Canon spine entry", "", f"- **{sp['name']}** ({sp['field']}): {sp['def']}", ""]
        body.append("## Definitions in the sources")
        body += source_lines(recs) if recs else ["", "(no digest uses this id yet)"]
        imen = mentions(cid, iinv, itoks)
        if imen:
            body += ["", "## Instances that use it", ""]
            for i in imen[:INSTANCE_CAP]:
                r = instances[i]
                body.append(f"- [[{r['id']}]] — {r['definition']} — from [[{r['digest']}]]")
            if len(imen) > INSTANCE_CAP:
                body.append(f"- … {len(imen) - INSTANCE_CAP} more instance lines mention this id")
        bmen = mentions(cid, binv, btoks, [v for v in all_variants if len(v.split("-")) > 1 or len(v) > 6])
        if bmen:
            body += ["", "## Candidate bridges", ""] + bridge_lines(bmen)
        write_page(CONCEPT_DIR, cid, "\n".join(fm + body) + "\n")
    # alias stub pages keep [[variant]] links in the digests working
    alias_stub_ids = sorted({v for c in concept_page_ids for v in variants_by.get(c, set())
                             | {v for r in cg.get(c, []) for v in r.get("variants", [])}} - set(concept_page_ids))
    for v in alias_stub_ids:
        c = canon_of(v)
        write_page(CONCEPT_DIR, v, "\n".join(["---", f"id: {v}", "type: alias", f"alias_of: {c}", GEN_MARK, "---", "",
                                              f"# {v}", "", f"Alias of [[{c}]] (see `wiki/kg/aliases.json`)."]) + "\n")

    # ---- instance matching
    clear(INSTANCE_DIR)
    canon_inst_alias = defaultdict(set)
    canon_title = defaultdict(set)
    for iid, ci in canon_inst.items():
        for a in ci["aliases"] | {iid}:
            canon_inst_alias[fold_id(a)].add(iid)
            k = title_key(a)
            if len(k) >= 1:
                canon_title[k].add(iid)
    inst_canon_match, inst_match_rule = defaultdict(set), {}
    canon_tok = {c: content_tokens(c) for c in canon_inst}
    for iid, recs in ig.items():
        match = set(canon_inst_alias.get(fold_id(iid), set()))
        rule = "alias" if match else ""
        tk = title_key(iid)
        if not match and len(tk) >= 2 and tk in canon_title:
            match |= canon_title[tk]
            rule = "title-key"
        works = {r["work"] for r in recs}
        dt = content_tokens(iid)
        for c, ct in canon_tok.items():
            if c in match or not dt or not ct or not (works & set(canon_inst[c]["works"])):
                continue
            inter = len(dt & ct)
            if dt <= ct or ct <= dt or inter / len(dt | ct) >= 0.5:
                match.add(c)
                rule = rule or "same-work-tokens"
        if match:
            inst_canon_match[iid] |= match
            inst_match_rule[iid] = rule
    concept_match = defaultdict(set)
    rejected = {c: set(v) for c, v in inst_conf.get("rejected", {}).items()}
    for c, ids in sorted(inst_conf.get("confirmed", {}).items()):
        if c not in canon_inst:
            problems["instance-matches.json: unknown canon instance"] += 1
            problem_examples["instance-matches.json: unknown canon instance"].append(c)
            continue
        for x in ids:
            if x.startswith("concept:"):
                cc = canon_of(x[8:])
                if cc in cg:
                    concept_match[c].add(cc)
                else:
                    problems["instance-matches.json: unknown concept id"] += 1
            elif x in ig:
                if c not in inst_canon_match[x]:
                    inst_canon_match[x].add(c)
                    prev = inst_match_rule.get(x)
                    inst_match_rule[x] = f"{prev}+confirmed" if prev else "confirmed"
            else:
                problems["instance-matches.json: unknown instance id"] += 1
                problem_examples["instance-matches.json: unknown instance id"].append(f"{c}: {x}")
    for iid in list(inst_canon_match):
        inst_canon_match[iid] = {c for c in inst_canon_match[iid] if iid not in rejected.get(c, set())}
        if not inst_canon_match[iid]:
            del inst_canon_match[iid]
            inst_match_rule.pop(iid, None)
    instance_page_ids = sorted(i for i, recs in ig.items() if i in inst_canon_match or n_digests(recs) >= 2)
    for iid in instance_page_ids:
        recs = ig[iid]
        fm = ["---", f"id: {iid}", "type: instance", f"fields: {yaml_list(ordered_fields(recs))}",
              f"n_sources: {n_digests(recs)}", f"tiers: {yaml_list(ordered_tiers(recs))}",
              "grounding: digests", f"sources: {yaml_list(sorted({r['digest'] for r in recs}))}"]
        raws = sorted({r["raw"] for r in recs if r["raw"] != iid})
        if raws:
            fm.append(f"raw_ids: {yaml_list(raws)}")
        if iid in inst_canon_match:
            fm.append(f"canon_instance: {yaml_list(sorted(inst_canon_match[iid]))}")
            fm.append(f"canon_match_rule: {inst_match_rule.get(iid, 'confirmed')}")
        fm += [GEN_MARK, "---", "", f"# {iid}", ""]
        body = []
        for cm in sorted(inst_canon_match.get(iid, [])):
            ci = canon_inst[cm]
            body += ["## Canon entry", "", f"- **{ci['name']}** ({ci['field']}): {ci['def']}", ""]
        body.append("## Descriptions in the sources")
        body += source_lines(recs)
        bmen = mentions(iid, binv, btoks)
        if bmen:
            body += ["", "## Candidate bridges", ""] + bridge_lines(bmen)
        write_page(INSTANCE_DIR, iid, "\n".join(fm + body) + "\n")

    # ---- merge candidates (on canonical ids)
    write_merge_candidates(cg, spine, canon_of, n_digests)
    rev = defaultdict(set)
    for iid, cs in inst_canon_match.items():
        for c in cs:
            rev[c].add(iid)
    extra = [f"## 5. Instances: digest ids matched to canon canonical instances ({len(rev)} canon instances by instance record; "
             f"{len(set(concept_match) - set(rev))} more only as a concept)", "",
             "Match rules: alias (as for spine names), title-key (same informative title tokens), same-work-tokens",
             "(digest from a work the canon entry names, and one content-token set contains the other or Jaccard ≥ 0.5),",
             "confirmed (manual list `wiki/kg/instance-matches.json`).", ""]
    for c in sorted(set(rev) | set(concept_match)):
        ci = canon_inst[c]
        extra.append(f"- canon: **{ci['name']}** ({ci['field']}) → `{c}`")
        for iid in sorted(rev.get(c, ())):
            r = ig[iid][0]
            d = r["definition"] if len(r["definition"]) <= 140 else r["definition"][:137] + "…"
            extra.append(f"  - `{iid}` — {n_digests(ig[iid])} digest(s); rule {inst_match_rule.get(iid, 'confirmed')} — e.g. [[{r['digest']}]]: {d}")
        for cc in sorted(concept_match.get(c, ())):
            extra.append(f"  - concept `{cc}` — {n_digests(cg[cc])} digest(s); rule confirmed (appears as a concept, not an instance)")
    with open(KG / "merge-candidates.md", "a") as fh:
        fh.write("\n".join(extra) + "\n")

    write_unmatched(canon_inst, rev, concept_match, ig, n_digests)

    # ---- index
    stats = write_index(concepts, instances, bridges, cg, ig, concept_page_ids, instance_page_ids,
                        spine, spine_by, canon_inst, rev, concept_match, n_digests, problems, problem_examples,
                        notes, len(files), aliases, alias_stub_ids, curated_hubs, work_field_source, all_fields)

    print(f"digests: {len(files)}")
    print(f"concept records: {len(concepts)}  distinct ids: {len(cg)}  pages: {len(concept_page_ids)}  alias stubs: {len(alias_stub_ids)}")
    print(f"instance records: {len(instances)}  distinct ids: {len(ig)}  pages: {len(instance_page_ids)}")
    print(f"canon instances matched: {stats['inst_matched']} by instance record, {stats['inst_matched_any']} incl. concept matches (of {len(canon_inst)})")
    print(f"bridge records: {len(bridges)}  canon-field target rate: {stats['rate_all']:.1%} of all, {stats['rate_named']:.1%} of named")
    print(f"cross-field concepts (≥3 fields, strong records): {stats['cross3']}  (≥2: {stats['cross2']})")
    print(f"curated hubs kept: {len(curated_hubs)}")
    for k, v in problems.most_common():
        print(f"problem: {k}: {v}")
    for k, v in notes.most_common():
        print(f"note: {k}: {v}")


# ---------------------------------------------------------------- merge candidates
def levenshtein_le(a, b, k=2):
    if abs(len(a) - len(b)) > k:
        return False
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * len(b)
        lo = i
        for j, cb in enumerate(b, 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb))
            lo = min(lo, cur[j])
        if lo > k:
            return False
        prev = cur
    return prev[-1] <= k


def deletions(s, k=2):
    out = {s}
    frontier = {s}
    for _ in range(k):
        nxt = set()
        for w in frontier:
            for i in range(len(w)):
                nxt.add(w[:i] + w[i + 1:])
        out |= nxt
        frontier = nxt
    return out


class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        self.p[self.find(a)] = self.find(b)

    def groups(self):
        g = defaultdict(set)
        for x in list(self.p):
            g[self.find(x)].add(x)
        return [s for s in g.values() if len(s) > 1]


def reviewed_pairs():
    """pairs already judged in merge-review.md: `a` ≟ `b` (parts split on ' / ')."""
    out = set()
    p = KG / "merge-review.md"
    if not p.exists():
        return out
    for m in re.finditer(r"^- `([^`]+)` ≟ `([^`]+)`", p.read_text(), re.M):
        for a in m.group(1).split(" / "):
            for b in m.group(2).split(" / "):
                out.add(frozenset((a.split(" ")[0], b.split(" ")[0])))
    return out


def write_merge_candidates(cg, spine, canon_of, n_digests):
    ids = sorted(cg)
    fields_of = {i: {f for r in cg[i] for f in r["fields"]} for i in ids}
    done = reviewed_pairs()

    def member(i):
        recs = cg.get(i, [])
        n = n_digests(recs)
        fs = ", ".join(sorted(fields_of.get(i, set())))
        if recs:
            r = recs[0]
            d = (r["definition"] or "(no definition)").replace("\n", " ")
            d = d if len(d) <= 140 else d[:137] + "…"
            return f"  - `{i}` — {n} digest(s); {fs} — e.g. [[{r['digest']}]]: {d}"
        return f"  - `{i}` — 0 digests (canon spine only)"

    def open_group(g):
        g = sorted(g)
        return any(frozenset((a, b)) not in done for x, a in enumerate(g) for b in g[x + 1:])

    lines = ["# Merge candidates (phase 2, deterministic, after aliases)", "",
             "Groups of canonical concept ids (after `aliases.json`) that may still be the same concept.",
             "Groups whose every pair is already judged in `merge-review.md` are left out.",
             "Rules: (1) identical after singular/plural folding or hyphen removal; (2) matches an alias",
             "of a canon spine name (full name, name without parentheses, parenthetical, parts split on",
             "/ & , vs.); (3) Levenshtein distance ≤ 2, both ids ≥ 8 chars; (4) one id contained in",
             "another as a whole-token run, sharing a field. Each id: number of digests, fields, one example definition.",
             "Regenerated by scripts/build_kg.py.", ""]

    key = defaultdict(list)
    for i in ids:
        key[fold_id(i).replace("-", "")].append(i)
    g1 = [sorted(v) for v in key.values() if len(v) > 1 and open_group(v)]
    lines += [f"## 1. Plural / hyphen variants ({len(g1)} groups)", ""]
    for g in sorted(g1, key=lambda g: (-sum(n_digests(cg[i]) for i in g), g)):
        lines.append(f"- group: {' = '.join(g)}")
        lines += [member(i) for i in g]
    lines.append("")

    alias_to_spine = defaultdict(set)
    for sid, sp in spine.items():
        for a in sp["aliases"] | {sid}:
            alias_to_spine[fold_id(a).replace("-", "")].add(canon_of(sid))
    g2 = defaultdict(set)
    for i in ids:
        for sid in alias_to_spine.get(fold_id(i).replace("-", ""), ()):
            g2[sid].add(i)
    g2 = {s: m for s, m in g2.items() if m - {s} and open_group(m | {s})}
    lines += [f"## 2. Matches to canon spine names ({len(g2)} spine concepts with variant ids)", ""]
    for sid in sorted(g2, key=lambda s: (-sum(n_digests(cg[i]) for i in g2[s]), s)):
        lines.append(f"- spine → canonical id `{sid}`")
        lines += [member(i) for i in sorted(g2[sid] | {sid})]
    lines.append("")

    long_ids = [i for i in ids if len(i) >= 8]
    buckets = defaultdict(set)
    for i in long_ids:
        for d in deletions(i):
            buckets[d].add(i)
    uf3 = UF()
    pairs = set()
    for b in buckets.values():
        if len(b) < 2:
            continue
        bl = sorted(b)
        for x in range(len(bl)):
            for y in range(x + 1, len(bl)):
                a, c = bl[x], bl[y]
                if (a, c) in pairs or frozenset((a, c)) in done:
                    continue
                if fold_id(a).replace("-", "") == fold_id(c).replace("-", ""):
                    continue
                if levenshtein_le(a, c):
                    pairs.add((a, c))
                    uf3.union(a, c)
    g3 = [sorted(g) for g in uf3.groups()]
    lines += [f"## 3. Edit distance ≤ 2 ({len(g3)} groups from {len(pairs)} pairs)", ""]
    for g in sorted(g3, key=lambda g: (-len(g), -sum(n_digests(cg[i]) for i in g), g)):
        lines.append(f"- group: {' ~ '.join(g)}")
        lines += [member(i) for i in g]
    lines.append("")

    tokset = {i: tuple(fold_token(t) for t in i.split("-")) for i in ids}
    by_tok = defaultdict(list)
    for i, t in tokset.items():
        by_tok[t].append(i)
    g4 = defaultdict(set)
    for b, tb in tokset.items():
        n = len(tb)
        for L in range(1, n):
            for s in range(0, n - L + 1):
                for a in by_tok.get(tb[s:s + L], ()):
                    if a != b and len(a) >= 3 and fields_of[a] & fields_of[b] and frozenset((a, b)) not in done:
                        g4[a].add(b)
    lines += [f"## 4. Containment within a shared field ({len(g4)} contained ids)", "",
              "Each group: the shorter id, then the longer ids (same field) that contain it.", ""]
    for a in sorted(g4, key=lambda a: (-len(g4[a]), a)):
        lines.append(f"- contained: `{a}` in {len(g4[a])} id(s)")
        lines.append(member(a))
        lines += [member(b) for b in sorted(g4[a])]
    lines.append("")
    (KG / "merge-candidates.md").write_text("\n".join(lines) + "\n")
    write_merge_candidates.stats = {"rule1": len(g1), "rule2": len(g2), "rule3": len(g3),
                                    "rule3_pairs": len(pairs), "rule4": len(g4)}


# ---------------------------------------------------------------- unmatched instances
def write_unmatched(canon_inst, rev, concept_match, ig, n_digests):
    import difflib
    digested = {p.name for p in WORKS.iterdir() if p.is_dir()}
    ids = sorted(ig)
    keys = {i: " ".join(sorted(title_key(i))) for i in ids}
    by_tok = defaultdict(set)
    for i in ids:
        for t in title_key(i):
            by_tok[t].add(i)
    L = ["# Unmatched canon instances (phase 2)", "",
         "Canon canonical instances (`canon/<field>.md`) that no digest instance id matches and that the manual",
         "confirm list (`instance-matches.json`) does not link to a concept. Grouped by why. Fuzzy candidates",
         "(difflib ratio ≥ 0.6 on informative title tokens) are suggestions only, not matches.", ""]
    un = [c for c in sorted(canon_inst) if c not in rev and c not in concept_match]
    nd = [c for c in un if canon_inst[c]["works"] and not set(canon_inst[c]["works"]) & digested]
    rest = [c for c in un if c not in nd]
    for title, sel in ((f"Work(s) not digested yet ({len(nd)})", nd),
                       (f"Work digested (or no work named), but no matching instance ({len(rest)})", rest)):
        L += [f"## {title}", ""]
        for c in sel:
            ci = canon_inst[c]
            ck = " ".join(sorted(title_key(c)))
            cands = []
            if ck:
                pool = sorted(set().union(*(by_tok.get(t, set()) for t in title_key(c))))
                for i in pool:
                    sm = difflib.SequenceMatcher(None, ck, keys[i])
                    if sm.quick_ratio() >= 0.6 and sm.ratio() >= 0.6:
                        cands.append((-sm.ratio(), i))
            cands = [f"`{i}` ({-r:.2f})" for r, i in sorted(cands)[:3]]
            w = ", ".join(ci["works"]) or "no work named"
            L.append(f"- **{ci['name']}** ({ci['field']}; {w})" + (f" — candidates: {', '.join(cands)}" if cands else ""))
        L.append("")
    (KG / "unmatched-instances.md").write_text("\n".join(L) + "\n")
    write_unmatched.stats = {"unmatched": len(un), "not_digested": len(nd)}


# ---------------------------------------------------------------- index
def write_index(concepts, instances, bridges, cg, ig, cpages, ipages, spine, spine_by, canon_inst,
                rev, concept_match, n_digests, problems, problem_examples, notes, n_files, aliases,
                alias_stubs, curated_hubs, work_field_source, all_fields):
    def nf(rs, strong=True):
        return len(all_fields(rs, strong))

    def nworks(rs):
        return len({r["work"] for r in rs})

    canon_hits = sum(1 for b in bridges if field_root(b["target_field"]) in FIELDS)
    named = sum(1 for b in bridges if b["target_field"] != "unspecified")
    stats = {"inst_matched": len(rev), "inst_matched_any": len(set(rev) | set(concept_match)),
             "rate_all": canon_hits / max(1, len(bridges)), "rate_named": canon_hits / max(1, named),
             "cross3": sum(1 for c in cg if nf(cg[c]) >= 3), "cross2": sum(1 for c in cg if nf(cg[c]) >= 2)}
    L = ["# Knowledge graph index (phase 2)", "",
         "Generated by `scripts/build_kg.py` from the digests in `wiki/works/` and the curated files in `wiki/kg/`",
         "(`aliases.json`, `field-map.json`, `work-fields.json`, `instance-matches.json`). See `PHASE2.md` for what",
         "changed. Field(s) of a digest = the catalog field(s) of its work, plus `work-fields.json` overrides.",
         "**Strong** records exclude definitions that say the concept is only a canon link / loosely related /",
         "not used in the unit; cross-field counts use strong records only.", ""]
    once = sum(1 for rs in cg.values() if n_digests(rs) == 1)
    spine_used = sum(1 for s in spine_by if s in cg)
    weak = sum(1 for r in concepts if r.get("weak"))
    raw_ids = len({r["norm_id"] for r in concepts})
    L += ["## Counts", "",
          f"- digests parsed: {n_files}",
          f"- concept records: {len(concepts)} ({weak} weak); distinct normalised ids: {raw_ids}; "
          f"distinct canonical ids after aliases: {len(cg)}; concept pages: {len(cpages)} (+ {len(alias_stubs)} alias stubs)",
          f"- curated aliases: {len(aliases)} variant ids → {len(set(aliases.values()))} canonical ids",
          f"- concept ids marked (new) in at least one digest: {sum(1 for rs in cg.values() if any(r['new'] for r in rs))}",
          f"- canon spine concepts: {len(spine)} → {len(spine_by)} canonical ids; used by ≥ 1 digest: {spine_used}",
          f"- instance records: {len(instances)}; distinct instance ids: {len(ig)}; instance pages: {len(ipages)}",
          f"- canon canonical instances: {len(canon_inst)}; matched by a digest instance id: {len(rev)}; "
          f"matched incl. confirmed concept-level matches: {stats['inst_matched_any']}; unmatched: "
          f"{write_unmatched.stats['unmatched']} ({write_unmatched.stats['not_digested']} because the work is not digested)",
          f"- bridge records: {len(bridges)}; target field matched to a canon field: {canon_hits} "
          f"({stats['rate_all']:.1%} of all bridges, {stats['rate_named']:.1%} of the {named} that name a target)",
          f"- concepts in ≥ 3 fields (strong records): {stats['cross3']}; in ≥ 2 fields: {stats['cross2']}",
          f"- concept ids appearing in only one digest: {once}",
          f"- works with several fields: {len(work_field_source)} ({', '.join(sorted(work_field_source))})",
          f"- merge-candidate groups: " + ", ".join(f"{k} {v}" for k, v in write_merge_candidates.stats.items()),
          ""]
    hubs = sorted(set(curated_hubs) | {p.stem for p in CONCEPT_DIR.glob("*.md")
                                        if CURATED_RE.search(p.read_text()[:4000])})
    L += [f"## Curated hub pages ({len(hubs)})", "",
          "Hand-written pages (`curated:` frontmatter) that the builder never overwrites; the generated",
          "version of each is in `wiki/kg/hub-sources/`.", ""]
    for h in hubs:
        rs = cg.get(h, [])
        L.append(f"- [[{h}]] — {nf(rs)} fields, {nworks(rs)} works, {n_digests(rs)} digests")
    L.append("")
    if problems or notes:
        L += ["## Parse problems and notes", ""]
        for k, v in problems.most_common():
            L.append(f"- problem: {k}: {v}")
            for ex in problem_examples.get(k, [])[:5]:
                L.append(f"  - {ex}")
        for k, v in notes.most_common():
            L.append(f"- note (not a problem): {k}: {v}")
        L.append("")

    ranked = sorted(cg, key=lambda c: (-n_digests(cg[c]), -nf(cg[c]), c))
    L += ["## Top 50 concepts by number of sources", "", "| # | concept | digests | works | fields (strong) |", "|---|---|---|---|---|"]
    for k, c in enumerate(ranked[:50], 1):
        rs = cg[c]
        L.append(f"| {k} | [[{c}]] | {n_digests(rs)} | {nworks(rs)} | {', '.join(sorted(all_fields(rs, True)))} |")
    L.append("")

    cross = [c for c in cg if nf(cg[c]) >= 3]
    cross.sort(key=lambda c: (-nf(cg[c]), -nworks(cg[c]), -n_digests(cg[c]), c))
    L += [f"## Cross-field concepts (strong records in ≥ 3 fields): {len(cross)}", "",
          "Ranked by fields, then works, then digests. A record of a multi-field work counts in each of its fields.", "",
          "| concept | fields | works | digests | field list (records) |", "|---|---|---|---|---|"]
    for c in cross:
        rs = cg[c]
        fc = all_fields(rs, True)
        fl = ", ".join(f"{f} ({n})" for f, n in sorted(fc.items(), key=lambda x: (-x[1], x[0])))
        L.append(f"| [[{c}]] | {nf(rs)} | {nworks(rs)} | {n_digests(rs)} | {fl} |")
    L.append("")

    icross = [i for i in ig if nf(ig[i], False) >= 2]
    icross.sort(key=lambda i: (-nf(ig[i], False), -n_digests(ig[i]), i))
    L += [f"## Instances used in ≥ 2 fields: {len(icross)}", ""]
    for i in icross[:50]:
        L.append(f"- [[{i}]] — {nf(ig[i], False)} fields, {n_digests(ig[i])} digests: {', '.join(sorted(all_fields(ig[i])))}")
    L.append("")

    tc = Counter(b["type"] for b in bridges)
    L += ["## Bridges by link type", "", "| type | count |", "|---|---|"]
    for t, n in tc.most_common():
        L.append(f"| {t} | {n} |")
    L.append("")
    cols = FIELDS + ["other", "unspecified"]
    abbrev = {"decision-game-theory": "dec-gm", "communication-theory": "comm", "complex-systems": "cplx",
              "control-theory": "ctrl", "economics-finance": "econ", "information-theory": "info",
              "linear-algebra": "linalg", "political-science": "polsci", "theory-of-mind": "tom",
              "analytic-philosophy": "phil", "unspecified": "unspec", "bayesian": "bayes", "llm": "llm",
              "other": "other"}

    def matrix(sel, title):
        m = Counter((b["source_field"], field_root(b["target_field"])) for b in sel)
        out = [f"### {title} ({len(sel)})", "",
               "| source \\ target | " + " | ".join(abbrev[c] for c in cols) + " | total |",
               "|---|" + "---|" * (len(cols) + 1)]
        for s in FIELDS:
            row = [m[(s, c)] for c in cols]
            out.append(f"| {s} | " + " | ".join(str(x) if x else "·" for x in row) + f" | {sum(row)} |")
        tot = [sum(m[(s, c)] for s in FIELDS) for c in cols]
        out.append("| total | " + " | ".join(str(x) for x in tot) + f" | {sum(tot)} |")
        return out + [""]

    L += ["## Bridge matrix (source field × target field)", "",
          "Source = primary field of the digest's work. Target = `field-map.json` lookup of the free text before",
          "the first colon after `↔` (keyword rules for texts not in the map). `other` = outside the 12 fields",
          "(`other:<name>` in the map); `unspecified` = no `field:` prefix. Diagonal cells are within-field bridges.", ""]
    L += matrix(bridges, "All bridges")
    for t, _ in tc.most_common():
        L += matrix([b for b in bridges if b["type"] == t], f"Type: {t}")
    oc = Counter(b["target_field"] for b in bridges if field_root(b["target_field"]) == "other")
    L += ["### Most frequent targets outside the 12 fields", ""]
    for t, n in oc.most_common(40):
        L.append(f"- {t} — {n}")
    L.append("")
    (KG / "index.md").write_text("\n".join(L) + "\n")
    return stats


if __name__ == "__main__":
    sys.exit(main())
