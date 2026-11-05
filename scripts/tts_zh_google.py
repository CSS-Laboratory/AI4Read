#!/usr/bin/env python3
"""Chinese reference audio with Google Cloud Text-to-Speech (more natural than the local Kokoro voice).
Kunhao runs this on his Mac, signed in with his own Google account; the script never sees a key or a password.

One-time setup (Kunhao, in Terminal):
  gcloud auth application-default login                      # opens the browser; you sign in yourself
  gcloud services enable texttospeech.googleapis.com --project=playground-491901
  brew install ffmpeg                                         # if `ffmpeg -version` fails

Steps:
  python3 scripts/tts_zh_google.py --voices                   # list the Mandarin (cmn-CN) voices (free)
  python3 scripts/tts_zh_google.py --samples                  # a dozen 15-second samples → audio-zh-samples/ (a few cents)
  python3 scripts/tts_zh_google.py posts/<slug>              # dry run: shows the estimate (default: gemini, Sulafat)
  python3 scripts/tts_zh_google.py posts/<slug> --yes        # records posts/<slug>/audio-zh/
  python3 scripts/tts_zh_google.py posts/<slug> --redo hook,work --yes   # re-record only these chapters

Engines (Cloud Text-to-Speech API, https://texttospeech.googleapis.com/v1/text:synthesize):
  gemini  Gemini-TTS, model gemini-2.5-flash-tts by default (--model to change), steered by a style prompt
          (cmn-CN is Preview for Gemini-TTS). About $10 per 1M audio tokens, 25 tokens per second: ~$0.15 per 10 minutes.
  chirp   Chirp 3: HD (cmn-CN is GA), voice name cmn-CN-Chirp3-HD-<Voice>. $30 per 1M characters after a monthly free tier
          of 1M characters, so these posts (~30,000 characters) cost nothing.
Prices: https://cloud.google.com/text-to-speech/pricing (read 2026-11-04). Check before large runs.

Output is identical in shape to scripts/tts_post_zh.py (chapters.json with the English chapter ids, one MP3 per chapter,
all.mp3 under 15 MB), so the player and the owner-only route work unchanged. Only chapters whose text, engine or voice
changed are re-recorded. Uses only the Python standard library plus ffmpeg."""
import sys, os, re, json, time, base64, hashlib, pathlib, subprocess, urllib.request, urllib.error, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROJECT = os.environ.get("AI4READ_TTS_PROJECT", "playground-491901")
API = os.environ.get("AI4READ_TTS_API", "https://texttospeech.googleapis.com/v1")  # override only for offline tests
HASH_PROMPT = ("Read the following aloud in natural Mandarin Chinese, in a calm, warm and measured voice, like a patient "
          "teacher explaining an idea to a colleague. Keep a steady, unhurried pace, articulate clearly, and pause "
          "briefly between sentences. Read English names and terms in English.")
# The 2026-11-05 run showed Gemini-TTS inventing speech after a very short standalone line (post 03: a made-up passage
# about grocery shopping after "分三部分。"). New recordings use a stricter prompt; HASH_PROMPT keeps the cache key of
# the chapters that were already recorded and checked.
PROMPT = (HASH_PROMPT + " Read exactly the text given, word for word, and nothing else: never add, continue, explain or "
          "repeat anything, even when a line is short or seems to announce a list.")
MAX_BYTES = 3000  # per request text; the API allows 4,000 bytes of text (Gemini: 8,000 with the prompt)
args = sys.argv[1:]
opt = lambda k, d=None: args[args.index(k) + 1] if k in args else d
CH_RE = r"^## ([\w-]+) \| (.+?)\n(.*?)(?=^## |\Z)"


def token():
    for cmd in (["gcloud", "auth", "application-default", "print-access-token"], ["gcloud", "auth", "print-access-token"]):
        try:
            t = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout.strip()
            if t: return t
        except Exception: pass
    sys.exit("No Google sign-in found. Run:  gcloud auth application-default login")


def call(method, path, body=None, tries=6):
    data = json.dumps(body).encode() if body is not None else None
    for k in range(tries):
        req = urllib.request.Request(API + path, data=data, method=method, headers={
            "Authorization": f"Bearer {token()}", "x-goog-user-project": PROJECT, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=300) as r: return json.loads(r.read())
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")[:600]
            if e.code in (429, 500, 502, 503, 504) and k < tries - 1:
                time.sleep(min(60, 4 * 2 ** k)); continue
            if e.code == 403 and "SERVICE_DISABLED" in msg:
                sys.exit(f"The Text-to-Speech API is off in {PROJECT}. Run:\n  gcloud services enable texttospeech.googleapis.com --project={PROJECT}")
            if e.code == 400 and "too long" in msg: raise TooLong(msg)
            sys.exit(f"HTTP {e.code} from Google: {msg}")
        except urllib.error.URLError as e:
            if k < tries - 1: time.sleep(4 * 2 ** k); continue
            sys.exit(f"Network error: {e}")


class TooLong(Exception):
    """Google refused a sentence as too long (seen with Chirp on long Chinese sentences, 2026-11-05)."""


def split_long(text):
    """Split a sentence in two at the comma or semicolon nearest its middle."""
    cuts = [m.end() for m in re.finditer(r"[，；：、,;]", text)]
    if not cuts: k = len(text) // 2
    else: k = min(cuts, key=lambda c: abs(c - len(text) / 2))
    return text[:k], text[k:]


def guarded(text, engine, voice, model, rate):
    """Retry a clip whose length is far from what the text needs (invented or dropped speech). Typical speech is about
    4 characters per second; a clip longer than 2x + 2 s or shorter than 0.35x of that is redone, up to 3 times."""
    n = len(re.sub(r"[^\w]", "", text)); want = n / 4.0
    best = None
    for k in range(4):
        audio = pcm(_synth(text, engine, voice, model, rate)); sec = len(audio) / 2 / 24000
        if 0.35 * want <= sec <= 2.0 * want + 2.0: return audio
        print(f"  retry {k + 1}: {sec:.1f} s of audio for {n} characters (expected about {want:.1f} s)", flush=True)
        if best is None or abs(len(audio) / 48000 - want) < abs(len(best) / 48000 - want): best = audio
    print("  WARNING: kept the closest take; listen to this chapter", flush=True)
    return best


def synth(text, engine, voice, model, rate, depth=0):
    try:
        return guarded(text, engine, voice, model, rate)
    except TooLong:
        if depth > 4 or len(text) < 8: raise
        a, b = split_long(text)
        return synth(a, engine, voice, model, rate, depth + 1) + silence(0.15) + synth(b, engine, voice, model, rate, depth + 1)


def _synth(text, engine, voice, model, rate):
    if engine == "gemini":
        body = {"input": {"prompt": PROMPT, "text": text}, "voice": {"languageCode": "cmn-CN", "name": voice, "model_name": model},
                "audioConfig": {"audioEncoding": "LINEAR16", "sampleRateHertz": 24000}}
    else:
        body = {"input": {"text": text}, "voice": {"languageCode": "cmn-CN", "name": f"cmn-CN-Chirp3-HD-{voice}"},
                "audioConfig": {"audioEncoding": "LINEAR16", "sampleRateHertz": 24000, "speakingRate": rate}}
    return base64.b64decode(call("POST", "/text:synthesize", body)["audioContent"])


def pcm(wav_bytes):
    """Raw 16-bit PCM from a WAV (LINEAR16 responses carry a WAV header)."""
    if wav_bytes[:4] == b"RIFF":
        i = wav_bytes.find(b"data")
        return wav_bytes[i + 8:] if i >= 0 else wav_bytes[44:]
    return wav_bytes


SHORT = 40  # characters: a paragraph shorter than this is never sent alone (it invites the model to continue it)


def paragraphs(body):
    paras, carry = [], ""
    for p in [p.strip() for p in body.split("\n\n") if p.strip()]:
        p = carry + p; carry = ""
        if len(re.sub(r"[^\w]", "", p)) < SHORT: carry = p; continue
        paras.append(p)
    if carry: paras.append(carry) if not paras else paras.__setitem__(-1, paras[-1] + carry)
    return paras


def chunks(body):
    """Paragraphs (short ones merged into the next), split at sentence ends so each request stays under MAX_BYTES."""
    out = []
    for para in paragraphs(body):
        cur = ""
        for s in [x for x in re.split(r"(?<=[。！？])", para) if x.strip()]:
            if cur and len((cur + s).encode()) > MAX_BYTES: out.append((cur, False)); cur = ""
            cur += s
        if cur: out.append((cur, True))  # True: paragraph end → a longer pause
    return out


def silence(sec, sr=24000): return b"\x00\x00" * int(sec * sr)


def to_mp3(raw, mp3, kbps=64):
    with tempfile.NamedTemporaryFile(suffix=".raw", delete=False) as f: f.write(raw); p = f.name
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", p, "-b:a", f"{kbps}k", str(mp3)], check=True)
    os.unlink(p)


def chapters(p):
    src = p.read_text(encoding="utf-8").split("\n---\n", 1)[-1]
    return [(m.group(1).strip(), m.group(2).strip(), m.group(3).strip()) for m in re.finditer(CH_RE, src, re.S | re.M)]


if "--voices" in args:
    v = call("GET", "/voices?languageCode=cmn-CN").get("voices", [])
    for x in v: print(x["name"], x.get("ssmlGender", ""))
    print(f"{len(v)} voices. Gemini-TTS uses the short names (Kore, Leda, ...) with model_name; Chirp uses cmn-CN-Chirp3-HD-<Name>.")
    sys.exit(0)

if "--samples" in args:
    text = ("让语言模型在工作到一半时停下来，把它为某一个词持有的那一串数字抄出来。各种软件库把这一串数字叫做隐藏状态。"
            "这串数字很长：GPT-2 small 里有七百六十八个数。")
    out = ROOT / "audio-zh-samples"; out.mkdir(exist_ok=True)
    voices = (opt("--sample-voices") or "Kore,Leda,Aoede,Despina,Sulafat,Achernar").split(",")
    for engine in ("gemini", "chirp"):
        for v in voices:
            f = out / f"{engine}-{v}.mp3"
            if f.exists(): print("exists", f.name); continue
            try: to_mp3(synth(text, engine, v, opt("--model", "gemini-2.5-flash-tts"), 1.0), f)
            except TooLong as e: print("skipped", f.name, "(Google: sentence too long)"); continue
            print("wrote", f.relative_to(ROOT))
    print(f"Listen to the files in {out}, then tell Claude which engine and voice you prefer.")
    sys.exit(0)

if not args or args[0].startswith("--"): sys.exit(__doc__)
post = (ROOT / args[0]) if not pathlib.Path(args[0]).is_absolute() else pathlib.Path(args[0])
ENGINE, VOICE = opt("--engine", "gemini"), opt("--voice", "Sulafat")  # Kunhao chose Sulafat (Gemini) on 2026-11-05
MODEL, RATE = opt("--model", "gemini-2.5-flash-tts"), float(opt("--rate", "0.95"))
if ENGINE not in ("gemini", "chirp"): sys.exit("--engine must be gemini or chirp")
zh, en = chapters(post / "audio-script-zh.md"), chapters(post / "audio-script.md")
if [c[0] for c in zh] != [c[0] for c in en]: sys.exit("chapter ids differ from the English script")
out = post / "audio-zh"; out.mkdir(exist_ok=True)
meta_p = out / "chapters.json"
old = {c["id"]: c for c in json.loads(meta_p.read_text())} if meta_p.exists() else {}
key = lambda body: hashlib.sha1(f"google|{ENGINE}|{MODEL if ENGINE == 'gemini' else RATE}|{VOICE}|{HASH_PROMPT if ENGINE == 'gemini' else ''}|{body}".encode()).hexdigest()[:12]
REDO = set((opt("--redo") or "").split(",")) - {""}
cached = lambda cid, b: cid not in REDO and cid in old and old[cid].get("hash") == key(b) and (out / f"{cid}.mp3").exists()
todo = [(cid, t, b) for cid, t, b in zh if not cached(cid, b)]
chars = sum(len(b) for _, _, b in todo)
est_sec = chars / 4.0  # about 240 Chinese characters per minute
cost = est_sec * 25 / 1e6 * 10 if ENGINE == "gemini" else 0.0
print(f"{post.name}: {len(todo)} of {len(zh)} chapters to record, {chars} characters, about {est_sec/60:.0f} min of audio")
print(f"engine {ENGINE} ({MODEL if ENGINE == 'gemini' else 'Chirp 3 HD'}), voice {VOICE}; estimated cost about ${cost:.2f}"
      + (" (inside the 1M-character free tier)" if ENGINE == "chirp" else ""))
if "--yes" not in args:
    print("Dry run only. Add --yes to record."); sys.exit(0)
meta = []
for cid, title, body in zh:
    if cached(cid, body):
        meta.append(old[cid]); print("skip", cid); continue
    raw = b""
    for text, para_end in chunks(body):
        try: raw += synth(text, ENGINE, VOICE, MODEL, RATE) + silence(0.7 if para_end else 0.3)
        except TooLong: sys.exit(f"Google says a sentence in chapter {cid} is too long even after splitting it. Try --engine gemini, or tell Claude the chapter.")
    to_mp3(raw, out / f"{cid}.mp3")
    meta.append({"id": cid, "title": title, "hash": key(body), "dur": round(len(raw) / 2 / 24000, 1),
                 "engine": f"google-{ENGINE}", "voice": VOICE})
    print("done", cid, meta[-1]["dur"], "s", flush=True)
    meta_p.write_text(json.dumps(meta + [c for c in old.values() if c["id"] not in {m["id"] for m in meta}], ensure_ascii=False, indent=1))
meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
total = sum(c["dur"] for c in meta)
kbps = next((k for k in (40, 32, 24) if total * k * 1000 / 8 < 15e6), 24)
lst = out / "concat.txt"; lst.write_text("".join(f"file '{c['id']}.mp3'\n" for c in meta))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-ac", "1", "-b:a", f"{kbps}k", str(out / "all.mp3")], check=True)
lst.unlink()
sys.path.insert(0, str(ROOT / "scripts"))
import tag_audio; tag_audio.main(post, sub="audio-zh", album_suffix=" (中文参考音频)")  # source mark: "AI4Read from CSS Lab"
print(f"total {total/60:.1f} min · {out}")
