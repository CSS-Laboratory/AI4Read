"""Download legally-free canon items into library/<slug>/. Run on the machine holding the Drive folder.
Usage: python3 fetch_free.py manifest.json LIBRARY_DIR"""
import json, sys, os, urllib.request, concurrent.futures as cf
man = json.load(open(sys.argv[1])); lib = sys.argv[2]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
def get(m):
    d = os.path.join(lib, m["slug"]); os.makedirs(d, exist_ok=True)
    if m["type"] in ("website", "course", "video"):
        return m["id"], "link", m["url"]
    for ext in (".pdf", ".html"):
        if os.path.exists(os.path.join(d, m["id"] + ext)): return m["id"], "exists", ext
    try:
        req = urllib.request.Request(m["url"], headers={"User-Agent": UA, "Accept": "*/*"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read(); ct = r.headers.get("Content-Type", "")
        ext = ".pdf" if data[:5] == b"%PDF-" else ".html"
        with open(os.path.join(d, m["id"] + ext), "wb") as f: f.write(data)
        return m["id"], "ok" + ext, f"{len(data)//1024}KB {ct}"
    except Exception as e:
        return m["id"], "fail", repr(e)[:120]
with cf.ThreadPoolExecutor(8) as ex:
    res = list(ex.map(get, man))
json.dump(res, open(os.path.join(lib, "_fetch_log.json"), "w"), indent=1)
from collections import Counter
print(Counter(r[1] for r in res))
