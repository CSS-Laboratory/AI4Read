"""List externalIds that were in an earlier pack and are not in the current one.
Usage: python3 scripts/retired_ids.py <dir with the earlier packs> <date YYYY-MM-DD> <note> <slug> [<slug> ...]
  → site/mewiki/packs/retired-<date>.json  (Margin suspends them only if Kunhao agrees; never deletes history)"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
old_dir, date, note, slugs = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4:]
out = {"date": date, "note": note, "retired": {}}
for s in slugs:
    old = json.loads((old_dir / f"{s}.json").read_text())
    new = json.loads((ROOT / "site/mewiki/packs" / f"{s}.json").read_text())
    keep = {i["externalId"] for i in new["items"]} | {new.get("passage", {}).get("externalId")}
    out["retired"][s] = [{"externalId": i["externalId"], "kind": i["kind"], "headword": i["headword"]}
                         for i in old["items"] if i["externalId"] not in keep and i["kind"] != "tip"]
    print(s, len(out["retired"][s]), "retired")
(ROOT / "site/mewiki/packs" / f"retired-{date}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
