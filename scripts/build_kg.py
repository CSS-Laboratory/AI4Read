#!/usr/bin/env python3
"""Phase 1 of the AI4Read knowledge graph: deterministic extraction from digests.

Reads wiki/works/<work>/<unit>.md digests (skips *.cc.md and *.pipeline.md, except
that cover-2006-elements/ch02-entropy is read from its .pipeline.md), plus
canon/catalog.json and canon/<field>.md, and writes:

  wiki/kg/concepts.jsonl, instances.jsonl, bridges.jsonl   one record per line
  wiki/kg/merge-candidates.md                               groups to review (no merging)
  wiki/kg/index.md                                          statistics
  wiki/concepts/<id>.md, wiki/instances/<id>.md             generated pages

No model judgement: every rule below is string processing. Pages carry
`generated_by: build_kg.py`; only such pages are deleted on a rebuild.
Usage: python3 scripts/build_kg.py
"""
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
CANON = ROOT / "canon"
PIPELINE_OVERRIDES = {("cover-2006-elements", "ch02-entropy")}
GEN_MARK = "generated_by: build_kg.py"
BRIDGE_CAP = 50  # bridge lines shown per page (the total is always stated)
INSTANCE_CAP = 50

SECTION_CONCEPTS = "Concepts"
SECTION_INSTANCES = "Canonical instances"
SECTION_BRIDGES = "Bridges (candidates)"

FIELDS = ["analytic-philosophy", "bayesian", "communication-theory", "complex-systems",
          "control-theory", "decision-game-theory", "economics-finance",
          "information-theory", "linear-algebra", "llm", "political-science",
          "theory-of-mind"]

# Keyword rules mapping a bridge's free-text target field to a canon field slug.
# The earliest match in the target text wins. Unmatched targets are "other".
TARGET_RULES = {
    "analytic-philosophy": [r"analytic.philosophy", r"philosoph", r"epistemolog",
                            r"metaphysic", r"\blogic\b"],
    "bayesian": [r"bayes", r"causal"],
    "communication-theory": [r"communication", r"\bmedia\b", r"journalism", r"framing",
                             r"agenda.setting", r"two.step.flow", r"persuasion",
                             r"rhetoric", r"selective exposure", r"encoding/decoding"],
    "complex-systems": [r"complex.systems?", r"network science", r"network analysis",
                        r"statistical physics", r"statistical mechanics",
                        r"dynamical systems?", r"nonlinear dynamics", r"complex contagion"],
    "control-theory": [r"\bcontrol", r"cybernetic", r"reinforcement learning",
                       r"dynamic programming", r"\bfeedback"],
    "decision-game-theory": [r"decision.game", r"game.theor", r"decision theor",
                             r"mechanism design", r"social choice", r"bounded rationality",
                             r"repeated games?", r"\bsignal+ing\b", r"coordination game"],
    "economics-finance": [r"econom", r"financ", r"\bmarkets?\b"],
    "information-theory": [r"information.theor", r"information \(shannon\)", r"coding theory"],
    "linear-algebra": [r"linear.algebra", r"\bmatri(x|ces)\b", r"eigen", r"spectral", r"\bpca\b"],
    "llm": [r"\bllms?\b", r"language model", r"transformer", r"\bnlp\b",
            r"natural language processing"],
    "political-science": [r"politic", r"\bvot(e|ing|er)", r"\bveto\b", r"collective action",
                          r"institution", r"public opinion", r"election"],
    "theory-of-mind": [r"theory.of.mind", r"mind.?reading", r"mentali[sz]", r"false.belief"],
}
TARGET_RES = [(f, re.compile(p, re.I)) for f, ps in TARGET_RULES.items() for p in ps]

PAGE_RE = re.compile(r"\(([^()]*(?:\bpp?\.\s*[ivxlcdm\d]|\bpdf\s*\d|§|\bn\.\s*\d)[^()]*)\)", re.I)
SEP_RE = re.compile(r"\s+[—–]\s+|\s+--\s+|\s+-\s+")
WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
BACKTICK_RE = re.compile(r"`([^`]+)`")


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


def content_tokens(nid):
    return {fold_token(t) for t in re.sub(r"(?<=[a-z])s-", "-", nid + "-").split("-") if t and t not in STOP} - {""}


def tokens(text):
    s = strip_accents(text).lower()
    s = re.sub(r"[’']", "", s)
    return [fold_token(t) for t in re.split(r"[^\w]+|_", s) if t]


# ---------------------------------------------------------------- canon
def load_catalog():
    cat = json.loads((CANON / "catalog.json").read_text())
    return {c["id"]: c for c in cat}


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
    # drop trailing math symbol like H(X), I(X;Y), K(x)
    forms.add(re.sub(r"\s+[A-Z]\w{0,2}\([^)]*\)\s*$", "", base))
    parts = set()
    for f in forms:
        for p in re.split(r"\s+/\s+|/|\s+&\s+|\s+vs\.?\s+|,\s+", f):
            parts.add(p)
    forms |= parts
    return {norm_id(f) for f in forms if norm_id(f)}


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
                works = [w.strip() for w in re.split(r"[,;]\s*", tail) if re.fullmatch(r"[a-z0-9-]+-\d{4}-[a-z0-9-]+", w.strip())]
            inst.setdefault(iid, {"id": iid, "name": name, "field": slug, "def": desc,
                                  "aliases": name_aliases(name), "works": works})
    return spine, inst


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


def parse_entry(line):
    """Parse '- <head> — <definition>' into ([(raw, new)], definition, page) or None."""
    s = line.strip()
    if not s.startswith(("- ", "* ")):
        return None
    s = s[2:].strip()
    if not s or s.startswith("("):
        return None
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
            return None
        plain = re.sub(r"\([^)]*\)", " ", head)
        plain = re.sub(r"[*_]", "", plain).strip()
        if not plain or len(plain.split()) > 8:
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


def parse_bridge(line):
    s = line.strip()
    m = re.match(r"^[-*]\s+\[([^\]]+)\]\s*(.*)$", s)
    if not m:
        return None
    ltype = norm_id(m.group(1))
    body = m.group(2).strip()
    if "↔" in body:
        left, after = body.split("↔", 1)
    else:
        left, after = body, ""
    left, after = left.strip(), after.strip()
    # positions outside $...$
    def outside_math(text, ch_pred):
        inmath = False
        for i, ch in enumerate(text):
            if ch == "$":
                inmath = not inmath
            elif not inmath and ch_pred(text, i):
                return i
        return -1
    dash = outside_math(after, lambda t, i: t[i] in "—" and t[i - 1:i] == " ")
    if dash < 0:
        dash = outside_math(after, lambda t, i: t[i] == "–" and t[i - 1:i] == " " and t[i + 1:i + 2] == " ")
    main = after if dash < 0 else after[:dash]
    why = "" if dash < 0 else after[dash + 1:].strip()
    colon = outside_math(main, lambda t, i: t[i] == ":")
    if colon >= 0:
        target, right = main[:colon].strip(), main[colon + 1:].strip()
    else:
        target, right = "", main.strip()
    if not after:
        # no ↔: keep the whole text as left; why after the first em dash
        d = left.find(" — ")
        if d >= 0:
            left, why = left[:d], left[d + 3:]
    _, page = split_page(s)
    return {"type": ltype, "left": left.strip(), "target_raw": target, "right": right,
            "why": why.strip(), "page": page}


def map_target(target):
    best = None
    for f, rx in TARGET_RES:
        m = rx.search(target)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), f)
    return best[1] if best else "other"


# ---------------------------------------------------------------- main build
def main():
    catalog = load_catalog()
    spine, canon_inst = load_canon()
    concepts, instances, bridges = [], [], []
    problems = Counter()
    problem_examples = defaultdict(list)

    files = digest_files()
    for work, unit, path in files:
        text = path.read_text()
        cat = catalog.get(work, {})
        field = cat.get("slug") or (frontmatter_fields(text) or ["unknown"])[0]
        if not cat:
            problems["work not in catalog"] += 1
        meta = {"work": work, "unit": unit, "digest": f"{work}/{unit}", "field": field,
                "fields": frontmatter_fields(text) or [field], "tier": cat.get("tier", "")}
        secs = sections(text)
        for sec, store in ((SECTION_CONCEPTS, concepts), (SECTION_INSTANCES, instances)):
            if sec not in secs:
                problems[f"missing section {sec}"] += 1
            seen = OrderedDict()
            for line in secs.get(sec, []):
                if not line.strip().startswith(("- ", "* ")):
                    continue
                parsed = parse_entry(line)
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
                    if nid in seen:
                        seen[nid]["other_definitions"].append(definition)
                        seen[nid]["new"] = seen[nid]["new"] or new
                        continue
                    seen[nid] = dict(id=nid, raw=raw, **meta, definition=definition,
                                     page=page, new=new, multi_id_line=len(raws) > 1,
                                     other_definitions=[])
            store.extend(seen.values())
        for line in secs.get(SECTION_BRIDGES, []):
            if not line.strip().startswith(("- ", "* ")):
                continue
            b = parse_bridge(line)
            if not b:
                problems["unparsed bridge line"] += 1
                problem_examples["unparsed bridge line"].append(f"{meta['digest']}: {line.strip()[:120]}")
                continue
            if "↔" not in line:
                problems["bridge without ↔"] += 1
            if b["type"] not in ("same-math", "structural-analogy", "metaphor"):
                problems[f"bridge with nonstandard type"] += 1
            b["target_field"] = map_target(b["target_raw"]) if b["target_raw"] else "unspecified"
            b.update(source=meta["digest"], work=work, unit=unit, source_field=field,
                     tier=meta["tier"])
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

    def mentions(cid, inv, toks):
        q = [fold_token(t) for t in cid.split("-") if t]
        if not q:
            return []
        cand = set.intersection(*(inv.get(t, set()) for t in q))
        out = []
        n = len(q)
        for i in sorted(cand):
            tk = toks[i]
            if any(tk[j:j + n] == q for j in range(len(tk) - n + 1)):
                out.append(i)
        return out

    def ordered_fields(recs):
        c = Counter(r["field"] for r in recs)
        return [f for f, _ in sorted(c.items(), key=lambda x: (-x[1], x[0]))]

    def ordered_tiers(recs):
        c = Counter(r["tier"] for r in recs if r["tier"])
        return [t for t, _ in sorted(c.items(), key=lambda x: (-x[1], x[0]))]

    def n_digests(recs):
        return len({r["digest"] for r in recs})

    def yaml_list(xs):
        return "[" + ", ".join(json.dumps(x, ensure_ascii=False) if re.search(r"[,:\[\]{}#&*!|>'\"%@`]", x) else x for x in xs) + "]"

    def source_lines(recs):
        out = []
        by_field = defaultdict(list)
        for r in recs:
            by_field[r["field"]].append(r)
        for f in ordered_fields(recs):
            out.append(f"\n### {f}\n")
            for r in sorted(by_field[f], key=lambda r: r["digest"]):
                page = f" (p. {r['page']})" if r["page"] and not re.match(r"(pp?\.|pdf|§|n\.)", r["page"]) else (f" ({r['page']})" if r["page"] else "")
                notes = []
                if r["raw"] != r["id"]:
                    notes.append(f"as `{r['raw']}`")
                if r["new"]:
                    notes.append("new")
                note = f" [{'; '.join(notes)}]" if notes else ""
                d = r["definition"] or "(no definition given)"
                out.append(f"- [[{r['digest']}]]{page}: {d}{note}")
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

    def clear(d):
        d.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*.md"):
            if GEN_MARK in f.read_text()[:2000]:
                f.unlink()

    # ---- concept pages
    clear(CONCEPT_DIR)
    concept_page_ids = sorted({c for c, rs in cg.items() if n_digests(rs) >= 2} | set(spine))
    for cid in concept_page_ids:
        recs = cg.get(cid, [])
        sp = spine.get(cid)
        fields = ordered_fields(recs) or ([sp["field"]] if sp else [])
        fm = ["---", f"id: {cid}", "type: concept", f"fields: {yaml_list(fields)}",
              f"n_sources: {n_digests(recs)}", f"tiers: {yaml_list(ordered_tiers(recs))}",
              "grounding: digests", f"sources: {yaml_list(sorted({r['digest'] for r in recs}))}"]
        raws = sorted({r["raw"] for r in recs if r["raw"] != cid})
        if raws:
            fm.append(f"raw_ids: {yaml_list(raws)}")
        if sp:
            fm.append(f"canon_spine: {sp['field']}")
        fm += [GEN_MARK, "---", "", f"# {cid}", ""]
        body = []
        if sp:
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
        bmen = mentions(cid, binv, btoks)
        if bmen:
            body += ["", "## Candidate bridges", ""] + bridge_lines(bmen)
        (CONCEPT_DIR / f"{cid[:150]}.md").write_text("\n".join(fm + body) + "\n")

    # ---- instance pages
    clear(INSTANCE_DIR)
    canon_inst_alias = defaultdict(set)
    for iid, ci in canon_inst.items():
        for a in ci["aliases"] | {iid}:
            canon_inst_alias[fold_id(a)].add(iid)
    instance_page_ids = []
    inst_canon_match, inst_match_rule = {}, {}
    canon_tok = {c: content_tokens(c) for c in canon_inst}
    for iid, recs in ig.items():
        match = set(canon_inst_alias.get(fold_id(iid), set()))
        rule = "alias" if match else ""
        # same-work token rule: digest from a work the canon entry names, and one
        # content-token set contains the other or Jaccard >= 0.5
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
            inst_canon_match[iid] = sorted(match)
            inst_match_rule[iid] = rule
        if match or n_digests(recs) >= 2:
            instance_page_ids.append(iid)
    instance_page_ids.sort()
    for iid in instance_page_ids:
        recs = ig[iid]
        fm = ["---", f"id: {iid}", "type: instance", f"fields: {yaml_list(ordered_fields(recs))}",
              f"n_sources: {n_digests(recs)}", f"tiers: {yaml_list(ordered_tiers(recs))}",
              "grounding: digests", f"sources: {yaml_list(sorted({r['digest'] for r in recs}))}"]
        raws = sorted({r["raw"] for r in recs if r["raw"] != iid})
        if raws:
            fm.append(f"raw_ids: {yaml_list(raws)}")
        if iid in inst_canon_match:
            fm.append(f"canon_instance: {yaml_list(inst_canon_match[iid])}")
            fm.append(f"canon_match_rule: {inst_match_rule[iid]}")
        fm += [GEN_MARK, "---", "", f"# {iid}", ""]
        body = []
        for cm in inst_canon_match.get(iid, []):
            ci = canon_inst[cm]
            body += ["## Canon entry", "", f"- **{ci['name']}** ({ci['field']}): {ci['def']}", ""]
        body.append("## Descriptions in the sources")
        body += source_lines(recs)
        bmen = mentions(iid, binv, btoks)
        if bmen:
            body += ["", "## Candidate bridges", ""] + bridge_lines(bmen)
        (INSTANCE_DIR / f"{iid[:150]}.md").write_text("\n".join(fm + body) + "\n")

    # ---- merge candidates
    write_merge_candidates(cg, spine, n_digests)
    rev = defaultdict(set)
    for iid, cs in inst_canon_match.items():
        for c in cs:
            rev[c].add(iid)
    extra = [f"## 5. Instances: digest ids matched to canon canonical instances ({len(rev)} canon instances)", "",
             "Match rules: alias (as for spine names) or same-work-tokens (digest from a work the canon entry",
             "names, and one content-token set contains the other or Jaccard ≥ 0.5).", ""]
    for c in sorted(rev):
        ci = canon_inst[c]
        extra.append(f"- canon: **{ci['name']}** ({ci['field']}) → `{c}`")
        for iid in sorted(rev[c]):
            r = ig[iid][0]
            d = r["definition"] if len(r["definition"]) <= 140 else r["definition"][:137] + "…"
            extra.append(f"  - `{iid}` — {n_digests(ig[iid])} digest(s); rule {inst_match_rule[iid]} — e.g. [[{r['digest']}]]: {d}")
    with open(KG / "merge-candidates.md", "a") as fh:
        fh.write("\n".join(extra) + "\n")

    # ---- index
    write_index(concepts, instances, bridges, cg, ig, concept_page_ids, instance_page_ids,
                spine, canon_inst, inst_canon_match, n_digests, problems, problem_examples, len(files))

    print(f"digests: {len(files)}")
    print(f"concept records: {len(concepts)}  distinct ids: {len(cg)}  pages: {len(concept_page_ids)}")
    print(f"instance records: {len(instances)}  distinct ids: {len(ig)}  pages: {len(instance_page_ids)}")
    print(f"bridge records: {len(bridges)}")
    for k, v in problems.most_common():
        print(f"problem: {k}: {v}")


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


def write_merge_candidates(cg, spine, n_digests):
    ids = sorted(cg)
    fields_of = {i: {r["field"] for r in cg[i]} for i in ids}

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

    lines = ["# Merge candidates (phase 1, deterministic)", "",
             "Groups of concept ids that are probably the same concept. Nothing has been merged.",
             "Rules: (1) identical after singular/plural folding or hyphen removal; (2) matches an alias",
             "of a canon spine name (full name, name without parentheses, parenthetical, parts split on",
             "/ & , vs.); (3) Levenshtein distance ≤ 2, both ids ≥ 8 chars; (4) one id contained in",
             "another as a whole-token run, sharing a field. Each id: number of digests, fields, one example definition.",
             "Regenerated by scripts/build_kg.py.", ""]

    # rule 1
    uf = UF()
    key = defaultdict(list)
    for i in ids:
        key[fold_id(i).replace("-", "")].append(i)
    g1 = [sorted(v) for v in key.values() if len(v) > 1]
    lines += [f"## 1. Plural / hyphen variants ({len(g1)} groups)", ""]
    for g in sorted(g1, key=lambda g: (-sum(n_digests(cg[i]) for i in g), g)):
        lines.append(f"- group: {' = '.join(g)}")
        lines += [member(i) for i in g]
    lines.append("")

    # rule 2
    alias_to_spine = defaultdict(set)
    for sid, sp in spine.items():
        for a in sp["aliases"] | {sid}:
            alias_to_spine[fold_id(a).replace("-", "")].add(sid)
    g2 = defaultdict(set)
    for i in ids:
        for sid in alias_to_spine.get(fold_id(i).replace("-", ""), ()):
            g2[sid].add(i)
    g2 = {s: m for s, m in g2.items() if m - {s}}
    lines += [f"## 2. Matches to canon spine names ({len(g2)} spine concepts with variant ids)", ""]
    for sid in sorted(g2, key=lambda s: (-sum(n_digests(cg[i]) for i in g2[s]), s)):
        sp = spine[sid]
        lines.append(f"- spine: **{sp['name']}** ({sp['field']}) → canonical id `{sid}`")
        lines += [member(i) for i in sorted(g2[sid] | {sid})]
    lines.append("")

    # rule 3
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
                if (a, c) in pairs:
                    continue
                if fold_id(a).replace("-", "") == fold_id(c).replace("-", ""):
                    continue  # already in rule 1
                if levenshtein_le(a, c):
                    pairs.add((a, c))
                    uf3.union(a, c)
    g3 = [sorted(g) for g in uf3.groups()]
    lines += [f"## 3. Edit distance ≤ 2 ({len(g3)} groups from {len(pairs)} pairs)", ""]
    for g in sorted(g3, key=lambda g: (-len(g), -sum(n_digests(cg[i]) for i in g), g)):
        lines.append(f"- group: {' ~ '.join(g)}")
        lines += [member(i) for i in g]
    lines.append("")

    # rule 4
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
                    if a != b and len(a) >= 3 and fields_of[a] & fields_of[b]:
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


# ---------------------------------------------------------------- index
def write_index(concepts, instances, bridges, cg, ig, cpages, ipages, spine, canon_inst,
                inst_canon_match, n_digests, problems, problem_examples, n_files):
    L = ["# Knowledge graph index (phase 1, deterministic)", "",
         "Generated by `scripts/build_kg.py` from the digests in `wiki/works/`. No merging, no model judgement.",
         "Field of a digest = the catalog field (`canon/catalog.json` slug) of its work.", ""]
    once = sum(1 for rs in cg.values() if n_digests(rs) == 1)
    spine_used = sum(1 for s in spine if s in cg)
    L += ["## Counts", "",
          f"- digests parsed: {n_files}",
          f"- concept records: {len(concepts)}; distinct concept ids: {len(cg)}; concept pages: {len(cpages)}",
          f"- concept ids marked (new) in at least one digest: {sum(1 for rs in cg.values() if any(r['new'] for r in rs))}",
          f"- canon spine concepts: {len(spine)}; used verbatim (as normalised id) by ≥ 1 digest: {spine_used}",
          f"- instance records: {len(instances)}; distinct instance ids: {len(ig)}; instance pages: {len(ipages)}",
          f"- canon canonical instances: {len(canon_inst)}; matched by ≥ 1 digest instance id (alias match): {len({c for v in inst_canon_match.values() for c in v})}",
          f"- bridge records: {len(bridges)}",
          f"- concept ids appearing in only one digest: {once}",
          f"- merge-candidate groups: " + ", ".join(f"{k} {v}" for k, v in write_merge_candidates.stats.items()),
          ""]
    if problems:
        L += ["## Parse problems", ""]
        for k, v in problems.most_common():
            L.append(f"- {k}: {v}")
            for ex in problem_examples.get(k, [])[:5]:
                L.append(f"  - {ex}")
        L.append("")

    def nf(rs):
        return len({r["field"] for r in rs})

    ranked = sorted(cg, key=lambda c: (-n_digests(cg[c]), -nf(cg[c]), c))
    L += ["## Top 50 concepts by number of sources", "", "| # | concept | digests | works | fields |", "|---|---|---|---|---|"]
    for k, c in enumerate(ranked[:50], 1):
        rs = cg[c]
        L.append(f"| {k} | [[{c}]] | {n_digests(rs)} | {len({r['work'] for r in rs})} | {', '.join(sorted({r['field'] for r in rs}))} |")
    L.append("")

    cross = [c for c in cg if nf(cg[c]) >= 3]
    cross.sort(key=lambda c: (-nf(cg[c]), -n_digests(cg[c]), c))
    L += [f"## Cross-field concepts (digests in ≥ 3 fields): {len(cross)}", "",
          "Same normalised id used by digests of works in at least three fields. Most valuable for cross-disciplinary posts.", "",
          "| concept | fields | digests | field list |", "|---|---|---|---|"]
    for c in cross:
        rs = cg[c]
        fc = Counter(r["field"] for r in rs)
        fl = ", ".join(f"{f} ({n})" for f, n in sorted(fc.items(), key=lambda x: (-x[1], x[0])))
        L.append(f"| [[{c}]] | {nf(rs)} | {n_digests(rs)} | {fl} |")
    L.append("")

    icross = [i for i in ig if nf(ig[i]) >= 2]
    icross.sort(key=lambda i: (-nf(ig[i]), -n_digests(ig[i]), i))
    L += [f"## Instances used in ≥ 2 fields: {len(icross)}", ""]
    for i in icross[:50]:
        L.append(f"- [[{i}]] — {nf(ig[i])} fields, {n_digests(ig[i])} digests: {', '.join(sorted({r['field'] for r in ig[i]}))}")
    L.append("")

    tc = Counter(b["type"] for b in bridges)
    L += ["## Bridges by link type", "", "| type | count |", "|---|---|"]
    for t, n in tc.most_common():
        L.append(f"| {t} | {n} |")
    L.append("")
    cols = FIELDS + ["other", "unspecified"]
    abbrev = {f: f.split("-")[0][:6] for f in cols}
    abbrev.update({"decision-game-theory": "dec-gm", "communication-theory": "comm", "complex-systems": "cplx",
                   "control-theory": "ctrl", "economics-finance": "econ", "information-theory": "info",
                   "linear-algebra": "linalg", "political-science": "polsci", "theory-of-mind": "tom",
                   "analytic-philosophy": "phil", "unspecified": "unspec"})

    def matrix(sel, title):
        m = Counter((b["source_field"], b["target_field"]) for b in sel)
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
          "Target field is mapped from the free text before the first colon after `↔` by fixed keyword rules",
          "(see TARGET_RULES in the script). `other` = target text named but not matched to a canon field;",
          "`unspecified` = no `field:` prefix. Diagonal cells are within-field bridges.", ""]
    L += matrix(bridges, "All bridges")
    for t, _ in tc.most_common():
        L += matrix([b for b in bridges if b["type"] == t], f"Type: {t}")
    oc = Counter(b["target_raw"].lower() for b in bridges if b["target_field"] == "other")
    L += ["### Most frequent unmatched target texts (`other`)", ""]
    for t, n in oc.most_common(40):
        L.append(f"- {t} — {n}")
    L.append("")
    (KG / "index.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    sys.exit(main())
