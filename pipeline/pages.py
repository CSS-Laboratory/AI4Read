"""Per-page text and printed page numbers for one source file."""
import re
from collections import Counter
from pathlib import Path

from . import PIPE

TEXT_CACHE = PIPE / "_work" / "text"
NUM = re.compile(r"^\s*(\d{1,4})([a-z]?)\b|\b(\d{1,4})([a-z]?)\s*$")
EDGE_TOP, EDGE_BOTTOM = 5, 3      # lines scanned at the top / bottom of each page (banners push numbers down)


def page_texts(pdf: Path):
    t = TEXT_CACHE / (pdf.name + ".txt")
    if not t.exists():
        import subprocess
        t.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["pdftotext", "-layout", str(pdf), str(t)], check=True, capture_output=True)
    pages = t.read_text(errors="replace").split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def _edge_numbers(text):
    """{(number, suffix)} found at the start or end of the first/last lines (running heads/feet)."""
    lines = [l for l in text.splitlines() if l.strip()]
    edge = lines[:EDGE_TOP] + lines[-EDGE_BOTTOM:]
    out = set()
    for l in edge:
        for m in NUM.finditer(l.strip()):
            n, suf = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
            out.add((int(n), suf or ""))
    return out


def printed_numbers(pages, labels=None, window=12):
    """Printed page label (str) per pdf page, or None if unknown.

    1. PDF page labels, when they are not just 1..n.
    2. Else the offset (pdf_index - printed) voted by running heads/feet in a +-window.
    3. Else, inside the span where heads were found, the work's dominant offset.
    A letter suffix seen on most heads (e.g. Wittgenstein's '95e') is kept.
    """
    n = len(pages)
    if labels and any(l != str(i + 1) for i, l in enumerate(labels[:n])):
        return list(labels[:n])
    cand = [{(i + 1 - k, s) for k, s in _edge_numbers(p) if 0 < k <= i + 1} for i, p in enumerate(pages)]
    glob = Counter(c for cs in cand for c in cs)
    g_best = glob.most_common(1)[0] if glob else None
    supported = [i for i, cs in enumerate(cand) if g_best and g_best[0] in cs]
    need = 2 if n <= 40 else 3                 # short papers have only a few numbered pages
    out = []
    for i in range(n):
        c = Counter()
        for j in range(max(0, i - window), min(n, i + window + 1)):
            c.update(cand[j])
        best = c.most_common(1)[0] if c else None
        if best and best[1] >= need and i + 1 - best[0][0] > 0:
            off, suf = best[0]
        elif (g_best and g_best[1] >= max(need if n <= 40 else 5, len(supported) * 0.5) and supported
              and supported[0] <= i <= supported[-1] and i + 1 - g_best[0][0] > 0):
            off, suf = g_best[0]
        else:
            out.append(None)
            continue
        out.append(f"{i + 1 - off}{suf}")
    return out


def clean_label(l):
    if l is None:
        return None
    l = re.sub(r"^(p\.|page)\s*", "", str(l).strip(), flags=re.I)
    return l if re.fullmatch(r"[0-9]{1,4}[a-z]?|[ivxlcdmIVXLCDM]{1,8}", l) else None


MATH_CHARS = set("∑∏∫∂∇≤≥≠≈∈∉⊂⊆∪∩→←↔⇒⇔∀∃∞±×÷√∝∼≡⊥∧∨¬αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ")
WORD = re.compile(r"[A-Za-z]{2,}")


def page_kind(text, file_words_per_page=None):
    """Classify a page: 'scan' | 'math' | 'table' | 'garbled' | 'prose' | 'blank'.

    Pages other than 'prose' and 'blank' get a page image. When unsure, include the image.
    """
    s = text.strip()
    if not s:
        return "scan" if file_words_per_page is not None and file_words_per_page < 30 else "blank"
    words = WORD.findall(s)
    nchar = len(s.replace(" ", ""))
    if len(words) < 25 and nchar < 200:
        return "scan" if (file_words_per_page or 999) < 30 else "blank"
    lines = [l for l in s.splitlines() if l.strip()]
    math = sum(c in MATH_CHARS for c in s)
    eq_lines = sum(1 for l in lines if "=" in l or re.search(r"[<>]\s*\w", l))
    # isolated single symbols/letters: typical of broken equation layout
    toks = s.split()
    singles = sum(1 for t in toks if len(t) == 1 and not t.isdigit() and t not in "aAI,.;:-—()")
    weird = sum(1 for c in s if c == "�" or (ord(c) > 0x2000 and c not in MATH_CHARS and c not in "‘’“”–—…•"))
    numeric_lines = sum(1 for l in lines if len(re.findall(r"\d+(?:\.\d+)?", l)) >= 3)
    if weird / max(nchar, 1) > 0.02:
        return "garbled"
    if math >= 4 or eq_lines >= 4 or singles / max(len(toks), 1) > 0.08:
        return "math"
    if numeric_lines / max(len(lines), 1) > 0.25:
        return "table"
    if re.search(r"^\s*(Figure|Fig\.|FIGURE|Table|TABLE)\s*\d", s, re.M):
        return "table"
    return "prose"


def paper_numbers(pages):
    """Printed numbers for short papers (journal layouts): find one offset k so that page i carries the number
    i+1-k on a line of its own (anywhere on the page). Needs >= 2 supporting pages and >= 30% of text pages."""
    n = len(pages)
    lone = []
    for p in pages:
        nums = set()
        for l in p.splitlines():
            s = l.strip()
            if re.fullmatch(r"\d{1,4}", s):
                nums.add(int(s))
            m = re.match(r"^(\d{1,4})\s{3,}\S|\S\s{3,}(\d{1,4})$", s)     # number separated from a running head
            if m:
                nums.add(int(m.group(1) or m.group(2)))
        lone.append(nums)
    votes = Counter()
    for i, nums in enumerate(lone):
        for k in nums:
            if 0 < k and k != i + 1 or (k == i + 1 and n > 1):
                votes[i + 1 - k] += 1
    text_pages = sum(1 for p in pages if len(p.split()) >= 30)
    if not votes or not text_pages:
        return [None] * n
    off, cnt = votes.most_common(1)[0]
    if cnt < 2 or cnt < 0.3 * text_pages:
        return [None] * n
    return [str(i + 1 - off) if i + 1 - off > 0 else None for i in range(n)]


def spread_labels(pages):
    """Two-page spreads with a text layer (e.g. Ashby, Putnam): a running foot/head line shows 'a ... a+1'.
    Returns per-page labels 'a-(a+1)' (or a single number on chapter-opening pages), or None if not a spread work."""
    n = len(pages)
    pair = [None] * n
    single = [None] * n
    for i, p in enumerate(pages):
        lines = [l for l in p.splitlines() if l.strip()]
        for l in lines[:EDGE_TOP] + lines[-EDGE_BOTTOM:]:
            m = re.match(r"^\s*(\d{1,4})\s{4,}.*?(\d{1,4})\s*$", l) or re.match(r"^\s*(\d{1,4})\s{4,}(\d{1,4})\s*$", l)
            if m and int(m.group(2)) == int(m.group(1)) + 1:
                pair[i] = int(m.group(1))
                break
        if pair[i] is None:
            nums = {k for k, s in _edge_numbers(p) if not s}
            if len(nums) == 1:
                single[i] = nums.pop()
    text_pages = sum(1 for p in pages if len(p.split()) >= 30)
    if not text_pages or sum(1 for x in pair if x) < 0.4 * text_pages:
        return None
    # fill gaps between two known pairs when the step is exactly 2 printed pages per pdf page
    known = [i for i in range(n) if pair[i] is not None]
    for a, b in zip(known, known[1:]):
        if b - a > 1 and pair[b] - pair[a] == 2 * (b - a):
            for j in range(a + 1, b):
                if single[j] is None:
                    pair[j] = pair[a] + 2 * (j - a)
    out = [None] * n
    for i in range(n):
        if pair[i] is not None:
            out[i] = f"{pair[i]}-{pair[i] + 1}"
        elif single[i] is not None:
            out[i] = str(single[i])
    return out
