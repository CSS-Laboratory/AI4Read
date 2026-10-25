"""Build an AI4Read English pack for Margin, schema ai4read.english-pack/2 (passage-centred, 2026-10-26).

The English material is NOT part of the blog post (Kunhao, 2026-10-25). It is C1/C2 only. Since 2026-10-26 the
pack is built around one passage (140-190 words) that Kunhao shadows, notices, rebuilds and reuses; every
expression and pattern is anchored inside it (request from the Margin agent, docs/PROMPT-ai4read-passage-pack.md).

Usage:
  python3 scripts/english_pack.py posts/<slug>            build site/mewiki/packs/<slug>.json (+ .md); needs the passage audio
  python3 scripts/english_pack.py posts/<slug> --check    validate the source only (no audio needed); writes nothing

Source: posts/<slug>/english/english.json (schema ai4read.english-source/2). Offsets are computed here, never typed.
Audio:  posts/<slug>/english/passage-audio.json + site/mewiki/packs/audio/<slug>-passage.mp3, written by
        scripts/tts_english_passage.py; a text hash ties the audio to the exact passage text.
The script refuses to write a pack that fails any check."""
import re, html, json, sys, pathlib, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from passage_util import u16, split_sentences, text_hash, words, ABBREV

ROOT = pathlib.Path(__file__).resolve().parent.parent
post = pathlib.Path(sys.argv[1]); slug = post.name; CHECK = "--check" in sys.argv
src = json.loads((post / "english" / "english.json").read_text(encoding="utf-8"))
content = (post / "src" / "content.html").read_text(encoding="utf-8")
title = html.unescape(re.sub(r"<.*?>", "", re.search(r"<h1>(.*?)</h1>", content, re.S).group(1))).strip()
url = f"https://khyang-lab.org/ai4read/{slug}/"
LEVELS = {"C1", "C2"}
GROUPS = {"expression": "expressions", "pattern": "c1-c2-patterns", "fix": "error-fixes", "tip": "practice"}
source = {"label": f"AI4Read · {title}", "url": url}
errors = []
err = errors.append


def ext_id(head):
    return f"ai4read:{slug}:{re.sub(r'[^a-z0-9]+', '-', head.lower()).strip('-')}"


def locate(text, needle, occurrence=1):
    """UTF-16 (start, end) of the n-th occurrence of needle in text, or None."""
    k = -1
    for _ in range(occurrence):
        k = text.find(needle, k + 1)
        if k < 0: return None
    return u16(text[:k]), u16(text[:k]) + u16(needle)


# ---------- passage ----------
P = src["passage"]; text = re.sub(r"\s+", " ", P["text"]).strip()
if ABBREV.search(text): err(f"passage: abbreviation with a full stop ({ABBREV.search(text).group(0)}) breaks sentence splitting")
sents = split_sentences(text)
if " ".join(s[2] for s in sents) != text: err("passage: sentences do not cover the text with single spaces")
for a, b in zip(sents, sents[1:]):
    if b[0] != a[1] + 1: err("passage: sentences overlap or leave a gap")
nw = words(text)
if not 140 <= nw <= 190: err(f"passage: {nw} words (need 140-190)")
core = P.get("core", [])
if not 3 <= len(core) <= 4 or any(not 0 <= c < len(sents) for c in core) or sorted(set(core)) != core:
    err(f"passage: core must list 3-4 distinct sentence indexes in order (got {core}; {len(sents)} sentences)")
else:
    cw = sum(words(sents[c][2]) for c in core)
    if not 60 <= cw <= 90: err(f"passage: core sentences have {cw} words (need 60-90)")
if P.get("level") not in LEVELS: err("passage: level is not C1/C2")
gist = P.get("gist", [])
if len(gist) != 2 or any(not g.get("question") or not g.get("answer") for g in gist): err("passage: need exactly 2 gist questions with answers")


def in_one_sentence(start, end):
    return any(s <= start and end <= e for s, e, _ in sents)


# ---------- items ----------
items, heads = [], {}
counts = {k: 0 for k in GROUPS}
for raw in src["items"]:
    kind, head = raw["kind"], raw["headword"]; counts[kind] = counts.get(kind, 0) + 1
    it = {"externalId": ext_id(head), "kind": kind, "group": GROUPS[kind], "headword": head,
          "tags": ["ai4read", f"ai4read-{slug[:7]}", GROUPS[kind]], "source": source}
    if kind != "tip":
        lvl = raw.get("level")
        if lvl not in LEVELS: err(f"{head}: level {lvl!r} is not C1/C2")
        it["level"] = lvl; it["tags"].append(lvl)
        if not raw.get("definition"): err(f"{head}: no definition")
        for k in ("definition", "partOfSpeech", "register"):
            if k in raw: it[k] = raw[k]
    if kind in ("expression", "pattern"):
        a = raw.get("anchor", ""); loc = locate(text, a, raw.get("occurrence", 1)) if a else None
        if not loc: err(f"{head}: anchor {a!r} not in the passage")
        else:
            if not in_one_sentence(*loc): err(f"{head}: anchor crosses a sentence boundary")
            it["anchor"] = {"start": loc[0], "end": loc[1], "text": a}
        s2, t2 = raw.get("sentence"), raw.get("target")
        if kind == "expression" and not (s2 and t2): err(f"{head}: expression needs a second-context sentence and target")
        if s2:
            if any(re.sub(r"\W+", " ", s2).strip().lower() == re.sub(r"\W+", " ", s[2]).strip().lower() for s in sents):
                err(f"{head}: second-context sentence copies a passage sentence")
            loc2 = locate(s2, t2 or "") if t2 else None
            if t2 and not loc2: err(f"{head}: target {t2!r} not in its second-context sentence")
            it["sentence"] = s2
            if loc2: it["target"] = {"text": t2, "start": loc2[0], "end": loc2[1]}
        if len(s2 or "") > 5000 or len(it.get("definition", "")) > 1200: err(f"{head}: over a Margin length limit")
    if kind == "fix":
        i = raw.get("anchorSentence")
        if not isinstance(i, int) or not 0 <= i < len(sents): err(f"{head}: anchorSentence {i!r} is not a sentence index")
        else:
            right = sents[i][2]
            if raw.get("right") not in (None, right): err(f"{head}: 'right' must equal passage sentence {i} exactly")
            if not raw.get("wrong") or raw["wrong"] == right: err(f"{head}: 'wrong' must differ from the sentence")
            it.update({"anchorSentence": i, "wrong": raw.get("wrong"), "right": right})
    if kind == "tip":
        it["sentence"] = raw["sentence"]
    heads[head] = it; items.append(it)

for k, (lo, hi) in {"expression": (8, 12), "pattern": (2, 4), "fix": (3, 4), "tip": (0, 2)}.items():
    if not lo <= counts.get(k, 0) <= hi: err(f"{k}: {counts.get(k, 0)} items (need {lo}-{hi})")
ids = [x["externalId"] for x in items] + [f"ai4read:{slug}:passage"]
dups = {i for i in ids if ids.count(i) > 1}
if dups: err(f"duplicate externalIds: {sorted(dups)}")

R = P.get("retell", {})
must = []
for h in R.get("mustUse", []):
    x = heads.get(h)
    if not x or x["kind"] != "expression": err(f"retell: mustUse {h!r} is not an expression headword in this pack")
    else: must.append(x["externalId"])
if len(R.get("mustUse", [])) != 3: err("retell: mustUse needs exactly 3 expression headwords")
if not R.get("instruction") or not R.get("modelAnswer"): err("retell: needs an instruction and a model answer")

# ---------- audio ----------
audio = None
if not CHECK:
    meta_f = post / "english" / "passage-audio.json"; mp3 = ROOT / "site/mewiki/packs/audio" / f"{slug}-passage.mp3"
    if not meta_f.exists() or not mp3.exists(): err("audio: missing; run scripts/tts_english_passage.py first (or use --check)")
    else:
        m = json.loads(meta_f.read_text())
        if m["textHash"] != text_hash(text): err("audio: recorded for a different passage text; re-record")
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)],
                                   capture_output=True, text=True, check=True).stdout) * 1000
        seg = m["segments"]
        if [s["sentence"] for s in seg] != list(range(len(sents))): err("audio: need one segment per sentence, in order")
        for a, b in zip(seg, seg[1:]):
            if not a["endMs"] <= b["startMs"]: err("audio: segments overlap")
        if any(s["startMs"] >= s["endMs"] for s in seg) or (seg and (seg[0]["startMs"] < 0 or seg[-1]["endMs"] > dur)):
            err(f"audio: a segment is empty or outside the file ({round(dur)} ms)")
        audio = {"file": f"audio/{slug}-passage.mp3", "voice": m["voice"], "durationMs": round(dur), "wpm": m.get("wpm"),
                 "segments": seg, "note": "Recorded by AI4Read sentence by sentence (en-GB) and tagged 'AI4Read from CSS Lab'."}

if errors:
    sys.exit("pack NOT written:\n  " + "\n  ".join(errors))
if CHECK:
    print(f"source OK · passage {nw} words, {len(sents)} sentences, core {sum(words(sents[c][2]) for c in core)} words · {counts}"); sys.exit(0)

passage = {"externalId": f"ai4read:{slug}:passage", "level": P["level"], "text": text,
           "sentences": [{"start": s, "end": e} for s, e, _ in sents], "core": core, "audio": audio, "gist": gist,
           "retell": {"instruction": R["instruction"], "mustUse": must, "modelAnswer": R["modelAnswer"]},
           "tags": ["ai4read", f"ai4read-{slug[:7]}", "passage", P["level"]], "source": source}
pack = {"schema": "ai4read.english-pack/2", "post": {"slug": slug, "title": title, "url": url}, "levels": "C1-C2", "passage": passage, "items": items}
out = ROOT / "site" / "mewiki" / "packs"; out.mkdir(parents=True, exist_ok=True)
(out / f"{slug}.json").write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- readable preview ----------
md = [f"# English pack · {title}", "", f"Schema /2 (passage-centred) · C1/C2 only · source post: {url}", "", "## Passage", ""]
for i, (s, e, t) in enumerate(sents):
    md.append(f"{i}. {'**' if i in core else ''}{t}{'**' if i in core else ''}")
md += ["", f"{nw} words · core (bold) {sum(words(sents[c][2]) for c in core)} words · audio {round(audio['durationMs']/1000, 1)} s, {audio['voice']}, {audio.get('wpm')} wpm", "", "### Gist", ""]
md += [f"- {g['question']} → {g['answer']}" for g in gist]
md += ["", "### Retell", "", R["instruction"], "", f"Must use: {', '.join(R['mustUse'])}", "", f"Model answer: {R['modelAnswer']}", ""]
for kind, head in (("expression", "Expressions"), ("pattern", "Patterns"), ("fix", "Fixes"), ("tip", "Practice")):
    rows = [x for x in items if x["kind"] == kind]
    if not rows: continue
    md += [f"## {head}", ""]
    for x in rows:
        lvl = f" ({x['level']})" if "level" in x else ""
        if kind == "fix": md.append(f"- **{x['headword']}**{lvl}, sentence {x['anchorSentence']}: ~~{x['wrong']}~~ → {x['right']} {x['definition']}")
        elif kind == "tip": md.append(f"- **{x['headword']}**: {x['sentence']}")
        else:
            second = f" Second context: *{x['sentence']}*" if x.get("sentence") else ""
            md.append(f"- **{x['headword']}**{lvl}: {x.get('definition', '').rstrip('.')}. In the passage: “{x['anchor']['text']}”.{second}")
    md.append("")
(out / f"{slug}.md").write_text("\n".join(md), encoding="utf-8")
print(f"{len(items)} items {counts} · passage {nw} words · audio {round(audio['durationMs']/1000, 1)} s → {out}/{slug}.json (+ .md)")
