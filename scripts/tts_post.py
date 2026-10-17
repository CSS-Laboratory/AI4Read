"""Render a post's audio-script.md into one MP3 per chapter with Kokoro (local, offline).
Usage: /tmp/ttsenv/bin/python scripts/tts_post.py posts/<slug>
Only chapters whose text changed are re-rendered (hash cache in audio/chapters.json)."""
import sys, re, json, hashlib, subprocess, pathlib, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

post = pathlib.Path(sys.argv[1]); out = post / "audio"; out.mkdir(exist_ok=True)
src = (post / "audio-script.md").read_text(encoding="utf-8").split("\n---\n", 1)[-1]
chapters = [(m.group(1).strip(), m.group(2).strip(), m.group(3).strip())
            for m in re.finditer(r"^## ([\w-]+) \| (.+?)\n(.*?)(?=^## |\Z)", src, re.S | re.M)]
meta_p = out / "chapters.json"
old = {c["id"]: c for c in json.loads(meta_p.read_text())} if meta_p.exists() else {}
k = Kokoro("/tmp/kmodel/kokoro-v1.0.onnx", "/tmp/kmodel/voices-v1.0.bin")
meta = []
for cid, title, body in chapters:
    h = hashlib.sha1(body.encode()).hexdigest()[:12]
    mp3 = out / f"{cid}.mp3"
    if cid in old and old[cid]["hash"] == h and mp3.exists():
        meta.append(old[cid]); print("skip", cid, flush=True); continue
    pieces, sr = [], 24000
    for para in [p.strip() for p in body.split("\n\n") if p.strip()]:
        sents = re.split(r"(?<=[.?!])\s+", para); chunk = ""
        for s in sents + [None]:
            if s is not None and len(chunk) + len(s) < 380:
                chunk = (chunk + " " + s).strip(); continue
            if chunk:
                a, sr = k.create(chunk, voice="af_heart", speed=0.95, lang="en-us"); pieces.append(a)
                pieces.append(np.zeros(int(0.12 * sr), dtype=np.float32))
            chunk = s or ""
        pieces.append(np.zeros(int(0.45 * sr), dtype=np.float32))
    audio = np.concatenate(pieces); wav = out / f"{cid}.wav"; sf.write(wav, audio, sr)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-ac", "1", "-b:a", "64k", str(mp3)], check=True)
    wav.unlink()
    meta.append({"id": cid, "title": title, "hash": h, "dur": round(len(audio) / sr, 1)})
    print("done", cid, meta[-1]["dur"], flush=True)
    meta_p.write_text(json.dumps(meta + [c for c in old.values() if c["id"] not in {m["id"] for m in meta}], indent=1))
meta_p.write_text(json.dumps(meta, indent=1))
lst = out / "concat.txt"; lst.write_text("".join(f"file '{c['id']}.mp3'\n" for c in meta))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(out / "all.mp3")], check=True)
lst.unlink()
print("total min", round(sum(c["dur"] for c in meta) / 60, 1))
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tag_audio; tag_audio.main(post)  # source mark: "AI4Read from CSS Lab"
