"""Record the loop paragraph of an English pack with Kokoro and tag it 'AI4Read from CSS Lab'.
Usage: /tmp/ttsenv/bin/python scripts/tts_english_loop.py <slug>  →  site/mewiki/packs/audio/<slug>-loop.mp3"""
import sys, re, json, pathlib, subprocess, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
slug = sys.argv[1]; root = pathlib.Path(__file__).resolve().parent.parent
pack = json.loads((root / "site/mewiki/packs" / f"{slug}.json").read_text())
loop = next(i for i in pack["items"] if i["kind"] == "shadowing")
k = Kokoro("/tmp/kmodel/kokoro-v1.0.onnx", "/tmp/kmodel/voices-v1.0.bin")
pieces, sr, chunk = [], 24000, ""
for s in re.split(r"(?<=[.?!])\s+", loop["sentence"]) + [None]:
    if s is not None and len(chunk) + len(s) < 380: chunk = (chunk + " " + s).strip(); continue
    if chunk:
        a, sr = k.create(chunk, voice="af_heart", speed=0.95, lang="en-us"); pieces += [a, np.zeros(int(0.25 * sr), dtype=np.float32)]
    chunk = s or ""
out = root / "site/mewiki/packs/audio"; out.mkdir(parents=True, exist_ok=True)
wav = out / f"{slug}-loop.wav"; mp3 = out / f"{slug}-loop.mp3"; sf.write(wav, np.concatenate(pieces), sr)
src = "AI4Read from CSS Lab"
meta = {"title": f"Loop paragraph · {pack['post']['title']}", "artist": src, "album_artist": src, "album": f"AI4Read English · {pack['post']['title']}",
        "genre": "Speech", "date": "2026", "publisher": src, "copyright": f"2026 {src}", "comment": f"{src} · {pack['post']['url']}"}
args = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-ac", "1", "-b:a", "64k", "-id3v2_version", "3"]
for a, v in meta.items(): args += ["-metadata", f"{a}={v}"]
subprocess.run(args + [str(mp3)], check=True); wav.unlink()
print(mp3, round(sum(len(p) for p in pieces) / sr, 1), "s")
