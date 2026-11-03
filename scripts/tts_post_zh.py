"""Render a post's Chinese reference audio (audio-script-zh.md) into one MP3 per chapter.
Owner-only material (Kunhao, 2026-11-04): it is never placed in the public site build; see site/ai4read/API.md.

Usage: /tmp/zh312/bin/python scripts/tts_post_zh.py posts/<slug> [--voice zf_003] [--speed 0.9]
  → posts/<slug>/audio-zh/<id>.mp3, chapters.json, all.mp3 (tagged "AI4Read from CSS Lab")
Engine: Kokoro-82M-v1.1-zh (hexgrad) with misaki[zh]; English words go through the English G2P.
Environment: /tmp/zh312 (Python 3.12; kokoro, misaki[zh], en_core_web_sm). Only changed chapters are re-rendered.
The chapter ids must equal those of the English audio-script.md, in the same order (checked).

Memory: the Kokoro pipeline's memory grows by about 1.5 GB every few minutes of synthesis, and the session's processes
share a 6.3 GB limit, so long chapters were OOM-killed (exit 137). Each batch of sentences is therefore rendered in a
fresh worker process (--worker mode), which returns its audio as a .npy file and exits, releasing the memory."""
import sys, re, json, hashlib, subprocess, pathlib, tempfile, warnings
import numpy as np, soundfile as sf
warnings.filterwarnings("ignore")
SR, BATCH = 24000, 12
REPO = "hexgrad/Kokoro-82M-v1.1-zh"


def worker(job_path, out_path):
    """Render a list of items: ["s", sentence] or ["gap", seconds]. Writes one float32 array."""
    job = json.loads(pathlib.Path(job_path).read_text(encoding="utf-8"))
    from kokoro import KModel, KPipeline
    import torch
    torch.set_num_threads(2)
    model = KModel(repo_id=REPO).eval()
    en_g2p = KPipeline(lang_code="a", repo_id=REPO, model=False)
    pipe = KPipeline(lang_code="z", repo_id=REPO, model=model, en_callable=lambda t: next(en_g2p(t)).phonemes)
    pieces = []
    with torch.inference_mode():
        for kind, val in job["items"]:
            if kind == "gap": pieces.append(np.zeros(int(val * SR), dtype=np.float32)); continue
            for r in pipe(val, voice=job["voice"], speed=job["speed"]):
                if r.audio is not None: pieces.append(r.audio.numpy().astype(np.float32))
    np.save(out_path, np.concatenate(pieces) if pieces else np.zeros(0, dtype=np.float32))


if len(sys.argv) > 1 and sys.argv[1] == "--worker":
    worker(sys.argv[2], sys.argv[3]); sys.exit(0)

post = pathlib.Path(sys.argv[1]); out = post / "audio-zh"; out.mkdir(exist_ok=True)
opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
VOICE, SPEED = opt("--voice", "zf_003"), float(opt("--speed", "0.9"))
CH_RE = r"^## ([\w-]+) \| (.+?)\n(.*?)(?=^## |\Z)"


def chapters(p):
    src = p.read_text(encoding="utf-8").split("\n---\n", 1)[-1]
    return [(m.group(1).strip(), m.group(2).strip(), m.group(3).strip()) for m in re.finditer(CH_RE, src, re.S | re.M)]


def speakable_n1(text):
    """A hyphen before a digit is read as 'minus' (GPT-2 -> 'GPT fu er'), so a hyphen between a letter and a digit
    becomes a space (GPT-2 -> GPT 2). Found by the bilingual check of post 03."""
    return re.sub(r"(?<=[A-Za-z])-(?=\d)", " ", text)


# n2 (checked by speech recognition, 2026-11-04): "AI4Read" came out as "AI-3" and "Qwen3" as "QN3".
N2 = [("AI4Read", "AI for Read"), ("Qwen3", "千问3")]


def speakable(text):
    for a, b in N2: text = text.replace(a, b)
    return speakable_n1(text)


def items_for(body):
    items = []
    for para in [p.strip() for p in speakable(body).split("\n\n") if p.strip()]:
        for sent in [s.strip() for s in re.split(r"(?<=[。！？])", para) if s.strip()]:
            items += [["s", sent], ["gap", 0.18]]
        items.append(["gap", 0.5])
    return items


def render(items):
    """Render items in batches of BATCH sentences, each in a fresh worker process."""
    batches, cur, n = [], [], 0
    for it in items:
        cur.append(it); n += it[0] == "s"
        if n >= BATCH and it[0] == "gap": batches.append(cur); cur, n = [], 0
    if cur: batches.append(cur)
    parts = []
    with tempfile.TemporaryDirectory() as td:
        for k, b in enumerate(batches):
            jp, op = pathlib.Path(td, f"job{k}.json"), pathlib.Path(td, f"out{k}.npy")
            jp.write_text(json.dumps({"items": b, "voice": VOICE, "speed": SPEED}, ensure_ascii=False), encoding="utf-8")
            r = subprocess.run([sys.executable, __file__, "--worker", str(jp), str(op)], capture_output=True, text=True)
            if r.returncode != 0:
                sys.exit(f"worker failed (exit {r.returncode}) on batch {k}:\n{r.stderr[-2000:]}")
            parts.append(np.load(op))
    return np.concatenate(parts)


zh = chapters(post / "audio-script-zh.md"); en = chapters(post / "audio-script.md")
if [c[0] for c in zh] != [c[0] for c in en]:
    sys.exit(f"chapter ids differ from the English script:\n zh {[c[0] for c in zh]}\n en {[c[0] for c in en]}")
meta_p = out / "chapters.json"
old = {c["id"]: c for c in json.loads(meta_p.read_text())} if meta_p.exists() else {}
meta = []
for cid, title, body in zh:
    # chapters that the n2 fixes do not touch keep their n1 hash, so they are not re-rendered
    tag = "n1" if speakable(body) == speakable_n1(body) else "n2"
    h = hashlib.sha1(f"{VOICE}|{SPEED}|{tag}|{body}".encode()).hexdigest()[:12]
    mp3 = out / f"{cid}.mp3"
    if cid in old and old[cid]["hash"] == h and mp3.exists():
        meta.append(old[cid]); print("skip", cid, flush=True); continue
    audio = render(items_for(body)); wav = out / f"{cid}.wav"; sf.write(wav, audio, SR)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-ac", "1", "-b:a", "64k", str(mp3)], check=True)
    wav.unlink()
    meta.append({"id": cid, "title": title, "hash": h, "dur": round(len(audio) / SR, 1)})
    print("done", cid, meta[-1]["dur"], flush=True)
    keep = {m["id"] for m in meta}
    meta_p.write_text(json.dumps(meta + [c for c in old.values() if c["id"] not in keep], ensure_ascii=False, indent=1))
meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
# all.mp3: the Chinese audio runs longer than the English, and each artifact file must stay under 16 MB, so take the
# highest of 40/32/24 kb/s that keeps it under 15 MB (66 minutes need 24 kb/s). The chapter files stay at 64 kb/s.
total_s = sum(c["dur"] for c in meta)
kbps = next((k for k in (40, 32, 24) if total_s * k * 1000 / 8 < 15e6), 24)
lst = out / "concat.txt"; lst.write_text("".join(f"file '{c['id']}.mp3'\n" for c in meta))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-ac", "1", "-b:a", f"{kbps}k", str(out / "all.mp3")], check=True)
lst.unlink()
print("total min", round(sum(c["dur"] for c in meta) / 60, 1))
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tag_audio; tag_audio.main(post, sub="audio-zh", album_suffix=" (中文参考音频)")  # source mark: "AI4Read from CSS Lab"
