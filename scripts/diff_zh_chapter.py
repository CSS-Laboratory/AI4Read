"""Show where a Chinese audio chapter departs from its script (speech recognition vs text).
Usage: /tmp/zh312/bin/python scripts/diff_zh_chapter.py posts/<slug> <chapter-id> [--model small]"""
import sys, re, difflib, pathlib, subprocess
import numpy as np
from faster_whisper import WhisperModel
post, cid = pathlib.Path(sys.argv[1]), sys.argv[2]
model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "small"
src = (post / "audio-script-zh.md").read_text(encoding="utf-8").split("\n---\n", 1)[-1]
text = re.search(rf"^## {re.escape(cid)} \|.*?\n(.*?)(?=^## |\Z)", src, re.S | re.M).group(1)
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(post / "audio-zh" / f"{cid}.mp3"), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
segs, _ = WhisperModel(model, device="cpu", compute_type="int8", cpu_threads=2).transcribe(np.frombuffer(raw, dtype=np.float32), language="zh", initial_prompt="以下是普通话的句子。")
heard = "".join(s.text for s in segs)
norm = lambda s: re.sub(r"[^\w]", "", s)
a, b = norm(text), norm(heard)
print("HEARD (first 300):", heard[:300])
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if op != "equal" and (i2 - i1 >= 6 or j2 - j1 >= 6):
        print(f"{op:8} script[{i1}:{i2}] {a[i1:i2][:60]!r}  →  heard {b[j1:j2][:60]!r}")
