"""Write source metadata (ID3) into a post's MP3s without re-encoding.
Usage: python3 scripts/tag_audio.py posts/<slug>
Every file is marked with the source "AI4Read from CSS Lab" (artist, album artist,
publisher, copyright, comment), the post title as album, and the chapter title and
track number. Called automatically at the end of tts_post.py; safe to re-run."""
import sys, re, json, pathlib, subprocess, datetime

SOURCE = "AI4Read from CSS Lab"
SITE = "https://khyang-lab.org/ai4read/"


def post_title(post: pathlib.Path) -> str:
    html = (post / "src" / "content.html").read_text(encoding="utf-8")
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else post.name


def tag(mp3: pathlib.Path, title: str, album: str, track: str, url: str, year: str):
    tmp = mp3.with_suffix(".tagged.mp3")
    meta = {
        "title": title, "artist": SOURCE, "album_artist": SOURCE, "album": album,
        "track": track, "genre": "Speech", "date": year, "publisher": SOURCE,
        "copyright": f"{year} {SOURCE}", "comment": f"{SOURCE} · {url}",
    }
    args = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp3), "-map", "0:a", "-c", "copy",
            "-map_metadata", "-1", "-id3v2_version", "3"]
    for k, v in meta.items():
        args += ["-metadata", f"{k}={v}"]
    subprocess.run(args + [str(tmp)], check=True)
    tmp.replace(mp3)


def main(post: pathlib.Path):
    out = post / "audio"
    chapters = json.loads((out / "chapters.json").read_text())
    album, year = post_title(post), str(datetime.date.today().year)
    url = SITE + post.name + "/"
    n = len(chapters)
    for i, c in enumerate(chapters, 1):
        tag(out / f"{c['id']}.mp3", c["title"], album, f"{i}/{n}", url, year)
    if (out / "all.mp3").exists():
        tag(out / "all.mp3", f"{album} (full audio)", album, f"0/{n}", url, year)
    print(f"tagged {n + 1} files with source '{SOURCE}'")


if __name__ == "__main__":
    main(pathlib.Path(sys.argv[1]))
