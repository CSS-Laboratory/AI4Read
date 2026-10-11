"""Parse canon/*.md into canon/catalog.json (one record per item)."""
import json, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[1]
items = []
for f in sorted((root / "canon").glob("*.md")):
    text = f.read_text()
    fm = dict(re.findall(r"^(\w+):\s*(.+)$", text.split("---")[1], re.M))
    canon = text.split("## Canon", 1)[1].split("\n## ", 1)[0]
    strand = None
    for block in re.split(r"\n(?=#{3,4} )", canon):
        h = block.strip().splitlines()[0] if block.strip() else ""
        if h.startswith("### Strand:"):
            strand = h.split(":", 1)[1].strip(); continue
        if not h.startswith("#### "): continue
        rec = {"id": h[5:].strip().split()[0], "field": fm["field"], "slug": fm["slug"],
               "layer": fm.get("layer"), "strand": strand}
        for k, v in re.findall(r"^- \*\*(\w+):\*\*\s*(.*)$", block, re.M):
            rec[k] = v.strip()
        acc = rec.get("access", "")
        rec["free"] = acc.startswith("free")
        m = re.search(r"https?://\S+", acc)
        rec["url"] = m.group(0).rstrip(").,;") if m else None
        items.append(rec)
(root / "canon" / "catalog.json").write_text(json.dumps(items, ensure_ascii=False, indent=1))
from collections import Counter
print(len(items), "items")
print(Counter((i["slug"], i.get("tier")) for i in items))
print("free:", sum(i["free"] for i in items), " need-copy:", sum(not i["free"] for i in items))
print("need-copy core:", sum((not i["free"]) and i.get("tier")=="core" for i in items))
print("need-copy with partial free url:", sum((not i["free"]) and bool(i["url"]) for i in items))
