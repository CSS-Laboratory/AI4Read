"""Build an AI4Read English pack (JSON, schema ai4read.english-pack/1) for Margin.

Since 2026-10-25 the English material is NOT part of the blog post. It lives in
posts/<slug>/english/english.json and is C1/C2 only (Kunhao's request).

Usage: python3 scripts/english_pack.py posts/<slug>
  → site/mewiki/packs/<slug>.json   (the pack Margin imports)
  → site/mewiki/packs/<slug>.md     (a readable preview of the same items)

The pack keeps the v1 item shape that Margin's importer expects (externalId, kind,
group, headword, sentence, target{text,start,end}, definition, partOfSpeech, level,
register, tags, source) and adds `level` to every item. externalId depends only on
the slug and the headword, so an item kept from an earlier pack keeps its review history.
The script refuses to write a pack that fails validation."""
import re, html, json, sys, pathlib

post = pathlib.Path(sys.argv[1]); slug = post.name
src = json.loads((post / "english" / "english.json").read_text(encoding="utf-8"))
content = (post / "src" / "content.html").read_text(encoding="utf-8")
title = html.unescape(re.sub(r"<.*?>", "", re.search(r"<h1>(.*?)</h1>", content, re.S).group(1))).strip()
url = f"https://khyang-lab.org/ai4read/{slug}/"
u16 = lambda t: len(t.encode("utf-16-le")) // 2
LEVELS = {"C1", "C2"}
GROUPS = {"expression": "expressions", "pattern": "c1-c2-patterns", "fix": "error-fixes", "tip": "practice"}
source = {"label": f"AI4Read · {title}", "url": url}
errors, items = [], []


def ext_id(head):
    return f"ai4read:{slug}:{re.sub(r'[^a-z0-9]+', '-', head.lower()).strip('-')}"


for raw in src["items"]:
    kind, head, sent = raw["kind"], raw["headword"], raw["sentence"]
    it = {"externalId": ext_id(head), "kind": kind, "group": GROUPS[kind], "headword": head, "sentence": sent,
          "tags": ["ai4read", f"ai4read-{slug[:7]}", GROUPS[kind]], "source": source}
    if kind != "tip":
        lvl = raw.get("level")
        if lvl not in LEVELS: errors.append(f"{head}: level {lvl!r} is not C1/C2")
        it["level"] = lvl; it["tags"].append(lvl)
        if not raw.get("definition"): errors.append(f"{head}: no definition")
        for k in ("definition", "partOfSpeech", "register", "wrong", "right"):
            if k in raw: it[k] = raw[k]
    if kind in ("expression", "pattern"):
        t = raw.get("target", ""); k = sent.find(t)
        if not t or k < 0: errors.append(f"{head}: target {t!r} not in sentence")
        else: it["target"] = {"text": t, "start": u16(sent[:k]), "end": u16(sent[:k]) + u16(t)}
    if len(sent) > 5000 or len(it.get("definition", "")) > 1200 or len(it["tags"]) > 20: errors.append(f"{head}: over a Margin limit")
    items.append(it)

loop = src.get("loop")
if loop:
    text = re.sub(r"\s+", " ", loop["text"]).strip()
    missing = [t for t in loop["targets"] if t not in text]
    if missing: errors.append(f"loop: targets not in text: {missing}")
    if loop.get("level") not in LEVELS: errors.append("loop: level is not C1/C2")
    items.append({"externalId": ext_id("loop-paragraph-c1c2"), "kind": "shadowing", "group": "loop", "headword": loop["headword"],
                  "sentence": text, "targets": loop["targets"], "level": loop["level"],
                  "audio": {"file": f"audio/{slug}-loop.mp3", "url": None, "voice": "Kokoro af_heart (US English)",
                            "note": "Recorded by AI4Read and tagged 'AI4Read from CSS Lab'. Host it in Margin, or use Margin's own TTS."},
                  "tags": ["ai4read", f"ai4read-{slug[:7]}", "loop", loop["level"]], "source": source})

ids = [x["externalId"] for x in items]
dups = {i for i in ids if ids.count(i) > 1}
if dups: errors.append(f"duplicate externalIds: {sorted(dups)}")
for it in items:  # offsets must round-trip in UTF-16, as Margin checks them
    tg = it.get("target")
    if tg:
        s16 = it["sentence"].encode("utf-16-le")
        if s16[2 * tg["start"]:2 * tg["end"]].decode("utf-16-le") != tg["text"]: errors.append(f"{it['headword']}: offset check failed")
if errors:
    sys.exit("pack NOT written:\n  " + "\n  ".join(errors))

out = pathlib.Path(__file__).resolve().parent.parent / "site" / "mewiki" / "packs"; out.mkdir(parents=True, exist_ok=True)
pack = {"schema": "ai4read.english-pack/1", "levels": "C1-C2", "post": {"slug": slug, "title": title, "url": url}, "items": items}
(out / f"{slug}.json").write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")

md = [f"# English pack · {title}", "", f"C1/C2 only · {len(items)} items · source post: {url}", ""]
for kind, head in (("expression", "Expressions"), ("pattern", "Sentence patterns"), ("fix", "Fixes"), ("tip", "Practice"), ("shadowing", "Paragraph to loop")):
    rows = [x for x in items if x["kind"] == kind]
    if not rows: continue
    md += [f"## {head}", ""]
    for x in rows:
        lvl = f" ({x['level']})" if "level" in x else ""
        if kind == "fix": md.append(f"- **{x['headword']}**{lvl}: ~~{x['wrong']}~~ → {x['right']} {x['definition']}")
        elif kind == "shadowing": md.append(f"{x['sentence']}\n\nTargets: {', '.join(x['targets'])}")
        elif kind == "tip": md.append(f"- **{x['headword']}**: {x['sentence']}")
        else: md.append(f"- **{x['headword']}**{lvl}: {x.get('definition', '')}. *{x['sentence']}*")
    md.append("")
(out / f"{slug}.md").write_text("\n".join(md), encoding="utf-8")
c = {k: sum(1 for x in items if x["kind"] == k) for k in ("expression", "pattern", "fix", "tip", "shadowing")}
print(f"{len(items)} items {c} → {out}/{slug}.json (+ .md)")
