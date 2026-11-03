"""Render a post's Chinese reference audio (audio-script-zh.md) into one MP3 per chapter.
Owner-only material (Kunhao, 2026-11-04): it is never placed in the public site build; see site/ai4read/API.md.

Usage: /tmp/zh312/bin/python scripts/tts_post_zh.py posts/<slug> [--voice zf_003] [--speed 0.9]
  → posts/<slug>/audio-zh/<id>.mp3, chapters.json, all.mp3 (tagged "AI4Read from CSS Lab")
Engine: Kokoro-82M-v1.1-zh (hexgrad) with misaki[zh]; English words go through the English G2P.
Environment: /tmp/zh312 (Python 3.12; kokoro, misaki[zh], en_core_web_sm). Only changed chapters are re-rendered.
The chapter ids must equal those of the English audio-script.md, in the same order (checked)."""
import sys, re, json, hashlib, subprocess, pathlib, warnings
import numpy as np, soundfile as sf
warnings.filterwarnings("ignore")

post = pathlib.Path(sys.argv[1]); out = post / "audio-zh"; out.mkdir(exist_ok=True)
opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
VOICE, SPEED = opt("--voice", "zf_003"), float(opt("--speed", "0.9"))
CH_RE = r"^## ([\w-]+) \| (.+?)\n(.*?)(?=^## |\Z)"
def chapters(p):
    src = p.read_text(encoding="utf-8").split("\n---\n", 1)[-1]
    return [(m.group(1).strip(), m.group(2).strip(), m.group(3).strip()) for m in re.finditer(CH_RE, src, re.S | re.M)]
zh = chapters(post / "audio-script-zh.md"); en = chapters(post / "audio-script.md")
if [c[0] for c in zh] != [c[0] for c in en]:
    sys.exit(f"chapter ids differ from the English script:\n zh {[c[0] for c in zh]}\n en {[c[0] for c in en]}")

from kokoro import KModel, KPipeline
REPO = "hexgrad/Kokoro-82M-v1.1-zh"
model = KModel(repo_id=REPO).eval()
en_g2p = KPipeline(lang_code="a", repo_id=REPO, model=False)
def en_callable(t):
    return next(en_g2p(t)).phonemes
pipe = KPipeline(lang_code="z", repo_id=REPO, model=model, en_callable=en_callable)
SR = 24000
NORM_VERSION = "n1"  # bump when speakable() changes, so every chapter is re-rendered


def speakable(text):
    """Fix what the Chinese G2P misreads. A hyphen before a digit is read as 'minus' (GPT-2 -> 'GPT fu er'), so a hyphen
    between a letter and a digit becomes a space (GPT-2 -> GPT 2). Found by the bilingual check of post 03."""
    return re.sub(r"(?<=[A-Za-z])-(?=\d)", " ", text)
meta_p = out / "chapters.json"
old = {c["id"]: c for c in json.loads(meta_p.read_text())} if meta_p.exists() else {}
meta = []
for cid, title, body in zh:
    h = hashlib.sha1(f"{VOICE}|{SPEED}|{NORM_VERSION}|{body}".encode()).hexdigest()[:12]
    mp3 = out / f"{cid}.mp3"
    if cid in old and old[cid]["hash"] == h and mp3.exists():
        meta.append(old[cid]); print("skip", cid, flush=True); continue
    pieces = []
    for para in [p.strip() for p in speakable(body).split("\n\n") if p.strip()]:
        for sent in [s for s in re.split(r"(?<=[。！？])", para) if s.strip()]:
            for r in pipe(sent.strip(), voice=VOICE, speed=SPEED):
                if r.audio is not None: pieces.append(r.audio.numpy().astype(np.float32))
            pieces.append(np.zeros(int(0.18 * SR), dtype=np.float32))
        pieces.append(np.zeros(int(0.5 * SR), dtype=np.float32))
    audio = np.concatenate(pieces); wav = out / f"{cid}.wav"; sf.write(wav, audio, SR)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-ac", "1", "-b:a", "64k", str(mp3)], check=True)
    wav.unlink()
    meta.append({"id": cid, "title": title, "hash": h, "dur": round(len(audio) / SR, 1)})
    print("done", cid, meta[-1]["dur"], flush=True)
    meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
# all.mp3 at 40 kb/s: the Chinese audio runs longer than the English, and each artifact file must stay under 16 MB
lst = out / "concat.txt"; lst.write_text("".join(f"file '{c['id']}.mp3'\n" for c in meta))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-ac", "1", "-b:a", "40k", str(out / "all.mp3")], check=True)
lst.unlink()
print("total min", round(sum(c["dur"] for c in meta) / 60, 1))
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tag_audio; tag_audio.main(post, sub="audio-zh", album_suffix=" (中文参考音频)")  # source mark: "AI4Read from CSS Lab"
