"""Deterministic additions to the P4 work maps (no model calls).
1. Maps of works whose library edition differs from the catalog get the library-edition citation
   as their H1 and a one-line edition note (canon/library-editions.json).
2. Single-unit works get a stub index.md: citation, a link to the one digest, and its L0/L1/Prerequisites
   copied verbatim. Stubs carry `generated: deterministic` and are rewritten on each run; model-written maps are not.
Usage: python scripts/work_maps_extra.py"""
import json, re, pathlib
R = pathlib.Path(__file__).resolve().parents[1]; W = R / "wiki" / "works"
cat = {c["id"]: c for c in json.loads((R / "canon" / "catalog.json").read_text())}
ed = {k: v for k, v in json.loads((R / "canon" / "library-editions.json").read_text()).items() if not k.startswith("_")}
NOTE = "*Edition used in AI4Read: the library copy above. The catalog lists {c}; page numbers follow the library copy.*"

def units(wdir):
    return sorted(f for f in wdir.glob("*.md") if f.name != "index.md" and not f.name.endswith((".cc.md", ".pipeline.md")))

def section(text, head):
    m = re.search(rf"^## {re.escape(head)}[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""

fixed = stubs = 0
for wdir in sorted(p for p in W.iterdir() if p.is_dir()):
    w, idx = wdir.name, wdir / "index.md"
    us = units(wdir)
    cit = ed[w]["citation"] if w in ed else cat.get(w, {}).get("citation", w)
    if idx.exists() and "generated: deterministic" not in idx.read_text():
        if w in ed:
            t = idx.read_text()
            t = re.sub(r"^# .*$", "# " + cit, t, count=1, flags=re.M)
            t = re.sub(r"\n\*Edition used in AI4Read:.*?\*\n", "\n", t)
            t = t.replace("# " + cit + "\n", "# " + cit + "\n\n" + NOTE.format(c=ed[w]["catalog_edition"]) + "\n", 1)
            idx.write_text(re.sub(r"\n{3,}", "\n\n", t)); fixed += 1
        continue
    if len(us) != 1:
        continue
    d = us[0]; txt = d.read_text(); uid = f"{w}/{d.stem}"
    l1 = section(txt, "L1"); pre = ""
    m = re.search(r"\*\*Prerequisites:\*\*.*", l1)
    if m: pre, l1 = m.group(0), l1[:m.start()].strip()
    body = [f"---\nid: {w}/index\nwork: {w}\ntype: work-map\nunits: [{uid}]\ngenerated: deterministic\n---\n",
            f"# {cit}\n"]
    if w in ed: body.append(NOTE.format(c=ed[w]["catalog_edition"]) + "\n")
    body += ["## One digest\nThis work has a single digest, which is also its work-level summary: " + f"[[{uid}]].\n",
             "## In one line\n" + section(txt, "L0") + "\n", "## The gist\n" + l1 + "\n"]
    if pre: body.append(pre + "\n")
    idx.write_text("\n".join(body)); stubs += 1
print(f"edition headers fixed: {fixed}; single-unit stubs written: {stubs}")
