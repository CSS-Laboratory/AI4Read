"""Record the passage of an AI4Read English pack (schema /2) sentence by sentence in British English,
with a clear pause between sentences, and write exact segment timings. Tagged 'AI4Read from CSS Lab'.

Usage: /tmp/ttsenv/bin/python scripts/tts_english_passage.py posts/<slug> [--voice bm_george] [--wpm 155]
  → site/mewiki/packs/audio/<slug>-passage.mp3
  → posts/<slug>/english/passage-audio.json  (voice, speed, measured wpm, text hash, segments in ms)
The speed is calibrated so the measured speaking rate (pauses excluded) is close to --wpm (150-160 asked by Margin)."""
import sys, re, json, pathlib, subprocess, numpy as np, soundfile as sf
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from passage_util import split_sentences, text_hash, words
from kokoro_onnx import Kokoro

ROOT = pathlib.Path(__file__).resolve().parent.parent
post = pathlib.Path(sys.argv[1]); slug = post.name
opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
voice, target = opt("--voice", "bm_george"), float(opt("--wpm", "155"))
src = json.loads((post / "english" / "english.json").read_text(encoding="utf-8"))
text = re.sub(r"\s+", " ", src["passage"]["text"]).strip()
sents = [s[2] for s in split_sentences(text)]
k = Kokoro("/tmp/kmodel/kokoro-v1.0.onnx", "/tmp/kmodel/voices-v1.0.bin")
SR, GAP, LEAD = 24000, 0.7, 0.25


def render(speed):
    clips = [k.create(s, voice=voice, speed=speed, lang="en-gb")[0] for s in sents]
    return clips, words(text) / (sum(len(c) for c in clips) / SR) * 60


speed = 0.9
clips, wpm = render(speed)
for _ in range(3):  # proportional correction: rate scales roughly linearly with speed
    if abs(wpm - target) <= 4: break
    speed = max(0.6, min(1.2, speed * target / wpm)); clips, wpm = render(speed)

pieces, segs, t = [np.zeros(int(LEAD * SR), dtype=np.float32)], [], LEAD
for i, c in enumerate(clips):
    segs.append({"sentence": i, "startMs": round(t * 1000), "endMs": round((t + len(c) / SR) * 1000)})
    pieces += [c.astype(np.float32), np.zeros(int(GAP * SR), dtype=np.float32)]
    t += len(c) / SR + GAP
out = ROOT / "site/mewiki/packs/audio"; out.mkdir(parents=True, exist_ok=True)
wav, mp3 = out / f"{slug}-passage.wav", out / f"{slug}-passage.mp3"
sf.write(wav, np.concatenate(pieces), SR)
title = re.sub(r"<.*?>", "", re.search(r"<h1>(.*?)</h1>", (post / "src/content.html").read_text(encoding="utf-8"), re.S).group(1)).strip()
s = "AI4Read from CSS Lab"
meta = {"title": f"Passage · {title}", "artist": s, "album_artist": s, "album": f"AI4Read English · {title}", "genre": "Speech",
        "date": "2026", "publisher": s, "copyright": f"2026 {s}", "comment": f"{s} · https://khyang-lab.org/ai4read/{slug}/"}
args = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-ac", "1", "-b:a", "64k", "-id3v2_version", "3"]
for a, v in meta.items(): args += ["-metadata", f"{a}={v}"]
subprocess.run(args + [str(mp3)], check=True); wav.unlink()
(post / "english" / "passage-audio.json").write_text(json.dumps(
    {"textHash": text_hash(text), "voice": f"Kokoro {voice} (en-GB)", "speed": round(speed, 3), "wpm": round(wpm),
     "pauseMs": int(GAP * 1000), "segments": segs}, indent=1) + "\n")
print(f"{mp3} · {len(sents)} sentences · speed {speed:.3f} · {wpm:.0f} wpm · {t:.1f} s")
