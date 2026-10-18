"""Fill content-v2.tpl.html placeholders from content-v1.html (or v2-blocks/<id>.html overrides)."""
import re, sys, pathlib
here = pathlib.Path(__file__).parent
v1 = (here / "content-v1.html").read_text()
tpl = (here / "content-v2.tpl.html").read_text()

def grab_script(cid):
    m = re.search(r'[ \t]*<script type="application/json" id="%s">.*?</script>' % re.escape(cid), v1, re.S)
    return m.group(0) if m else None

def grab_elem(eid):
    m = re.search(r'[ \t]*<(details|section|div)\b[^>]*\bid="%s"[^>]*>' % re.escape(eid), v1)
    if not m: return None
    tag = m.group(1); i = m.end(); depth = 1
    pat = re.compile(r'<(/?)%s\b[^>]*>' % tag)
    while depth:
        n = pat.search(v1, i)
        depth += -1 if n.group(1) else 1
        i = n.end()
    return v1[m.start():i]

missing = []
def sub(m):
    kind, pid = m.group(1), m.group(2)
    o = here / "v2-blocks" / f"{pid}.html"
    if o.exists(): return o.read_text().rstrip("\n")
    got = grab_script(pid) if kind == "CFG" else grab_elem(pid)
    if got is None: missing.append(pid); return m.group(0)
    return got
out = tpl
for _ in range(3):
    out = re.sub(r'<!--(CFG|BLOCK):([a-z0-9-]+)-->', sub, out)
(here / "content.html").write_text(out)
print("missing:", missing or "none")
