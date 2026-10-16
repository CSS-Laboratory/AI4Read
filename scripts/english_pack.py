"""Build an AI4Read English pack (JSON) from a post's 'How to say it in English' section.
Usage: python3 scripts/english_pack.py posts/<slug>  →  site/mewiki/packs/<slug>.json
Definitions and parts of speech come from posts/<slug>/english-gloss.json (written by the post author)."""
import re, html, json, sys, pathlib
post = pathlib.Path(sys.argv[1]); slug = post.name
s = (post / "src/content.html").read_text()
title = html.unescape(re.sub("<.*?>", "", re.search(r"<h1>(.*?)</h1>", s, re.S).group(1)))
gloss = json.loads((post / "english-gloss.json").read_text())
i = s.index('<section id="english"'); sec = s[i:s.index("</section>", i)]
plain = lambda t: html.unescape(re.sub(r"<.*?>", "", t)).strip()
u16 = lambda t: len(t.encode("utf-16-le")) // 2
url = f"https://khyang-lab.org/ai4read/{slug}/#english"
items = []
groups = {"Show phrases": ("expression", "topic-phrases"), "Expressions for discussing evidence": ("expression", "evidence-talk"),
          "Four sentence patterns that sound C1": ("pattern", "c1-patterns"), "Small fixes that make a big difference": ("fix", "error-fixes"),
          "How to practise (15 minutes a day)": ("tip", "practice")}
for summ, body in re.findall(r'<details class="phrases"[^>]*><summary>(.*?)</summary>(.*?)</details>', sec, re.S):
    kind, group = groups[plain(summ)]
    for dt, dd in re.findall(r"<dt>(.*?)</dt><dd>(.*?)</dd>", body, re.S):
        head, sent = plain(dt), plain(dd)
        g = gloss.get(head, {})
        it = {"externalId": f"ai4read:{slug}:{re.sub(r'[^a-z0-9]+', '-', head.lower()).strip('-')}", "kind": kind, "group": group,
              "headword": head, "sentence": sent, "tags": ["ai4read", f"ai4read-{slug[:7]}", group], "source": {"label": f"AI4Read · {title}", "url": url}}
        tg = re.findall(r"<i>(.*?)</i>", dd)
        if tg and kind in ("expression", "pattern"):
            t = plain(tg[0]); k = sent.find(t)
            if k >= 0: it["target"] = {"text": t, "start": u16(sent[:k]), "end": u16(sent[:k]) + u16(t)}
        it.update({k2: v for k2, v in g.items()})
        items.append(it)
loop = re.search(r'<blockquote class="loop-para"[^>]*>(.*?)</blockquote>', sec, re.S)
if loop:
    items.append({"externalId": f"ai4read:{slug}:loop-paragraph", "kind": "shadowing", "group": "loop", "headword": "A paragraph to loop",
                  "sentence": re.sub(r"\s+", " ", plain(loop.group(1))), "targets": [plain(x) for x in re.findall(r"<i>(.*?)</i>", loop.group(1))],
                  "audio": {"url": f"https://khyang-lab.org/ai4read/{slug}/audio/c1-loop.mp3", "voice": "Kokoro af_heart (US English)"},
                  "tags": ["ai4read", f"ai4read-{slug[:7]}", "loop"], "source": {"label": f"AI4Read · {title}", "url": url}})
missing = [x["headword"] for x in items if x["kind"] in ("expression", "pattern", "fix") and "definition" not in x]
out = pathlib.Path("site/mewiki/packs"); out.mkdir(parents=True, exist_ok=True)
(out / f"{slug}.json").write_text(json.dumps({"schema": "ai4read.english-pack/1", "post": {"slug": slug, "title": title, "url": url}, "items": items}, ensure_ascii=False, indent=1))
print(f"{len(items)} items → {out}/{slug}.json; missing glosses: {missing}")
