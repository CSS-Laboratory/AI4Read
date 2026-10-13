"""Deterministic checks on a digest (DESIGN.md): no model call.

check(md, row) -> list of {"level": "error"|"warn", "check": ..., "msg": ...}
"""
import json
import re
import subprocess

import yaml

from . import PIPE

REQUIRED_FM = ["id", "work", "unit", "pages", "fields", "level", "grounding", "digested_by", "digested_on"]
SECTIONS = ["L0", "L1", "L2", "L3", "Toy example", "Concepts", "Canonical instances", "Bridges",
            "Questions this raises", "Exercises worth doing", "Reading notes"]
OPTIONAL = {"Exercises worth doing"}
# model-chatter markers only; phrases like "I cannot" occur in sources (e.g. Wittgenstein) and are not leaks
LEAKS = ["DIGEST SPEC", "UNIT METADATA", "{{", "As an AI", "as a language model", "<page pdf=",
         "[page image:"]
INLINE = re.compile(r"(?<![\\$])\$(?![\s$])([^$\n]+?)(?<![\s\\])\$(?![\d$])")
DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.S)
KATEX_DIR = PIPE / "katex"


def split_frontmatter(md):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", md, re.S)
    if not m:
        return None, md
    try:
        return yaml.safe_load(m.group(1)) or {}, md[m.end():]
    except yaml.YAMLError:
        return "bad", md[m.end():]


def sections(body):
    """[(name, text)] for '## ' headings, name normalised to the SECTIONS key."""
    out = []
    parts = re.split(r"^## +(.+?)\s*$", body, flags=re.M)
    for i in range(1, len(parts), 2):
        h = parts[i]
        key = next((s for s in SECTIONS if h.startswith(s)), h)
        out.append((key, parts[i + 1]))
    return out


def strip_code(md):
    md = re.sub(r"```.*?```", " ", md, flags=re.S)
    return re.sub(r"`[^`\n]*`", " ", md)


def katex_errors(md):
    body = strip_code(md)
    items = [{"tex": m.group(1), "display": True} for m in DISPLAY.finditer(body)]
    body2 = DISPLAY.sub(" ", body)
    items += [{"tex": m.group(1), "display": False} for m in INLINE.finditer(body2)]
    if not items:
        return []
    r = subprocess.run(["node", str(KATEX_DIR / "check.js")], input=json.dumps(items),
                       capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        return [{"tex": "", "error": "katex checker failed: " + r.stderr[:200]}]
    return [{"tex": items[e["i"]]["tex"][:120], "error": e["error"]} for e in json.loads(r.stdout or "[]")]


def _range(s):
    m = re.fullmatch(r"c?(\d+)[a-z]?-(\d+)[a-z]?", s or "")      # also '95e-110e'
    return (int(m.group(1)), int(m.group(2))) if m else None


def page_refs(text):
    """Yield ('p'|'pdf', n) for (p. N), (pp. N–M), (§N, p. Me), (pdf N)."""
    for m in re.finditer(r"\([^()]*?\b(p{1,2})\.\s*(\d+)[a-z]?(?:\s*[–-]\s*(\d+)[a-z]?)?", text):
        yield "p", int(m.group(2))
        if m.group(3):
            yield "p", int(m.group(3))
    for m in re.finditer(r"\(pdf\.?\s*(\d+)(?:\s*[–-]\s*(\d+))?", text):
        yield "pdf", int(m.group(1))
        if m.group(2):
            yield "pdf", int(m.group(2))


def check(md, row, uid=None):
    issues = []

    def err(c, msg, level="error"):
        issues.append({"level": level, "check": c, "msg": msg})

    md = md.strip()
    if not md.startswith("---"):
        err("format", "output does not start with '---' frontmatter")
    fm, body = split_frontmatter(md)
    if fm is None or fm == "bad":
        err("frontmatter", "frontmatter missing or not valid YAML")
    else:
        for k in REQUIRED_FM:
            if k not in fm:
                err("frontmatter", f"missing key '{k}'")
        if uid and fm.get("id") != uid:
            err("frontmatter", f"id is '{fm.get('id')}', expected '{uid}'")
    if not re.search(r"^# \S", body, re.M):
        err("format", "missing '# Title' line")

    secs = sections(body)
    names = [s for s, _ in secs]
    want = [s for s in SECTIONS if s not in OPTIONAL or s in names]
    present = [s for s in names if s in SECTIONS]
    for s in want:
        if s not in names:
            err("sections", f"missing section '{s}'")
    if present != [s for s in want if s in present]:
        err("sections", f"sections out of order: {present}")
    extra = [s for s in names if s not in SECTIONS]
    if extra:
        err("sections", f"unexpected sections: {extra}", "warn")
    sec = dict(secs)

    if "L1" in sec:
        n = len([w for w in re.sub(r"\$[^$]*\$", "x", sec["L1"]).split() if re.search(r"\w", w)])
        if n > 120:
            err("L1", f"L1 has {n} words (> 120)")
    if "L2" in sec:
        b = len(re.findall(r"^\s*[-*] ", sec["L2"], re.M))
        if not 5 <= b <= 10:
            err("L2", f"L2 has {b} bullets (want 5–10)")

    # page references inside the unit's range (±2 for chapter openers)
    is_html = (row.get("pdf_pages") or "").startswith("c")
    pr, pdf = _range(row.get("printed_pages")), _range(row.get("pdf_pages"))
    bad = set()
    for name in ("L2", "L3", "Concepts", "Canonical instances", "Exercises worth doing"):
        for kind, n in page_refs(sec.get(name, "")):
            r = pr if kind == "p" else pdf
            if r and not (r[0] - 2 <= n <= r[1] + 2):
                bad.add(f"{kind} {n}")
    if bad:   # warn only: refs to other works' pages are legitimate; the verifier checks page refs (C)
        err("pages", f"page refs outside unit range {row.get('printed_pages') or row.get('pdf_pages')}: "
                     f"{sorted(bad)[:12]}", "warn")
    # spec 1.2: Prerequisites line (between L1 and L2)
    if not re.search(r"^\s*\*\*Prerequisites:?\*\*:?\s*\S", body, re.M):
        err("prereq", "Prerequisites line missing")
    # printed labels exist -> no (pdf N) citations (gate2 review, request 5)
    if not is_html and row.get("printed_pages"):
        n_pdf = sum(1 for k, _ in page_refs(md) if k == "pdf")
        if n_pdf:
            err("pages", f"{n_pdf} (pdf N) citation(s) although printed pages {row['printed_pages']} are known")
    if re.search(r"\b(is correct as printed|the digest (says|states|has)|this digest|the verifier)\b", body, re.I):
        err("residue", "verifier chatter in the digest", "warn")
    if "L2" in sec and not is_html and not list(page_refs(sec["L2"])):
        err("pages", "L2 has no page references")

    for e in katex_errors(md)[:20]:
        err("katex", f"{e['error']} in `{e['tex']}`")

    for leak in LEAKS:
        if leak.lower() in md.lower():
            err("leak", f"contains '{leak}'")
    return issues


def errors(issues):
    return [i for i in issues if i["level"] == "error"]
