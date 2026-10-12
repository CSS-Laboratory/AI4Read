"""Validate pipeline/toc/<work_id>.json against the source PDF text.

python -m pipeline.toc_check <work_id> [...]   (or no args = all)

Checks: schema, pdf pages in range and non-decreasing per level, and that each entry's
title words appear near the top of its pdf page (skipped for scanned files).
"""
import json
import re
import sys

from . import PIPE
from .pages import page_texts
from .planner import LIB

TOC = PIPE / "toc"
STOP = {"the", "a", "an", "of", "and", "on", "in", "to", "for", "with", "chapter", "part", "appendix"}


def words(s):
    return [w for w in re.findall(r"[a-z]{3,}", s.lower()) if w not in STOP]


def check(work_id):
    d = json.loads((TOC / f"{work_id}.json").read_text())
    pdf = LIB / d["file"]
    pages = page_texts(pdf)
    n = len(pages)
    scanned = sum(len(p.split()) for p in pages) / max(n, 1) < 30
    errs, warns = [], []
    for k in ("work_id", "file", "entries"):
        if k not in d:
            errs.append(f"missing key {k}")
    last = {}
    for i, e in enumerate(d.get("entries", [])):
        p, lv, t = e.get("pdf"), e.get("level", 0), e.get("title", "")
        if not isinstance(p, int) or not 1 <= p <= n:
            errs.append(f"#{i} '{t}': pdf {p} out of range 1..{n}")
            continue
        for l2 in [x for x in last if x > lv]:
            del last[l2]
        if lv in last and p < last[lv]:
            errs.append(f"#{i} '{t}': pdf {p} < previous same-level entry {last[lv]}")
        last[lv] = p
        if scanned:
            continue
        top = " ".join(pages[p - 1].splitlines()[:25]).lower()
        ws = words(re.sub(r"^\s*[\dIVXLC.]+\s", "", t))[:4]
        if ws and sum(w in top for w in ws) < max(1, len(ws) // 2):
            warns.append(f"#{i} L{lv} '{t[:50]}' not found near top of pdf {p}")
    return d, errs, warns, scanned


def main(ids):
    ids = ids or sorted(f.stem for f in TOC.glob("*.json"))
    bad = 0
    for w in ids:
        try:
            d, errs, warns, scanned = check(w)
        except Exception as ex:
            print(f"{w}: ERROR {ex}")
            bad += 1
            continue
        lv0 = sum(1 for e in d["entries"] if e.get("level", 0) == 0)
        print(f"{w}: {len(d['entries'])} entries ({lv0} top-level){' [scanned: titles not checked]' if scanned else ''}"
              f" — {len(errs)} errors, {len(warns)} warnings")
        for m in errs + warns[:30]:
            print("   ", m)
        bad += bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
