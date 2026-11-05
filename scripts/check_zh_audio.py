"""Check Chinese reference audio against its script by speech recognition (faster-whisper), chapter by chapter.
LLM-based voices (Gemini-TTS) can skip, repeat or reword text, so every chapter is transcribed and compared.
Usage: /tmp/zh312/bin/python scripts/check_zh_audio.py posts/<slug> [--model small]  → posts/<slug>/review/zh-audio-asr.md
Similarity is difflib's ratio on Chinese characters and letters only (punctuation and spaces removed). Homophones and
digits-versus-words cost a little, so about 0.85 or higher is normal; a chapter below 0.80, or a long missing run of
script text, is flagged for listening."""
import sys, re, json, difflib, pathlib, subprocess
import numpy as np
from faster_whisper import WhisperModel

post = pathlib.Path(sys.argv[1]); model_name = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "small"
CH_RE = r"^## ([\w-]+) \| (.+?)\n(.*?)(?=^## |\Z)"
src = (post / "audio-script-zh.md").read_text(encoding="utf-8").split("\n---\n", 1)[-1]
script = {m.group(1): m.group(3) for m in re.finditer(CH_RE, src, re.S | re.M)}
from opencc import OpenCC
_t2s = OpenCC("t2s").convert  # the recogniser sometimes writes Traditional characters
norm = lambda s: re.sub(r"[^\w]", "", _t2s(s)).upper()
m = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=2)
rows, flags = [], []
for c in json.loads((post / "audio-zh" / "chapters.json").read_text()):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(post / "audio-zh" / f"{c['id']}.mp3"), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    segs, _ = m.transcribe(np.frombuffer(raw, dtype=np.float32), language="zh", initial_prompt="以下是普通话的句子。", vad_filter=False)
    heard = "".join(s.text for s in segs)
    a, b = norm(script[c["id"]]), norm(heard)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False); r = sm.ratio()
    ops = sm.get_opcodes()
    missing = [a[i1:i2] for op, i1, i2, j1, j2 in ops if op in ("delete", "replace") and i2 - i1 >= 15 and not re.fullmatch(r"[零一二三四五六七八九十百千万亿点负]+", a[i1:i2])]
    # added speech: an LLM voice can invent text after a short line (seen 2026-11-05); digits for number words are not counted
    added = [b[j1:j2] for op, i1, i2, j1, j2 in ops if op in ("insert", "replace") and (j2 - j1) - (i2 - i1) >= 10 and not re.fullmatch(r"[0-9.%]+", b[j1:j2])]
    rows.append((c["id"], r, len(a), len(b), missing, added))
    if r < 0.80 or missing or added: flags.append(c["id"])
    print(c["id"], round(r, 3), len(a), len(b), "missing:", len(missing), "added:", [x[:30] for x in added], flush=True)
out = post / "review" / "zh-audio-asr.md"; out.parent.mkdir(exist_ok=True)
md = [f"# Chinese audio check by speech recognition ({post.name})", "", f"faster-whisper `{model_name}`, int8, CPU. Similarity on characters only; ≥ 0.85 is normal (homophones, digits).", "",
      "| chapter | similarity | script chars | heard chars | script runs of ≥ 15 chars not heard | heard runs not in the script (≥ 10 chars more) |", "|---|---|---|---|---|---|"]
md += [f"| {i} | {r:.3f} | {la} | {lb} | {'; '.join(x[:40] for x in mi) or '—'} | {'; '.join(x[:40] for x in ad) or '—'} |" for i, r, la, lb, mi, ad in rows]
md += ["", f"Flagged for listening: {', '.join(flags) or 'none'}."]
out.write_text("\n".join(md) + "\n", encoding="utf-8")
print("flagged:", flags or "none", "→", out)
