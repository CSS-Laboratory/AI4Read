"""Per-page text and printed page numbers for one source file."""
import re
from collections import Counter
from pathlib import Path

from . import PIPE

TEXT_CACHE = PIPE / "_work" / "text"
NUM = re.compile(r"^\s*(\d{1,4})\b|\b(\d{1,4})\s*$")


def page_texts(pdf: Path):
    t = TEXT_CACHE / (pdf.name + ".txt")
    pages = t.read_text(errors="replace").split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def _edge_numbers(text):
    lines = [l for l in text.splitlines() if l.strip()]
    edge = lines[:2] + lines[-2:]
    out = set()
    for l in edge:
        for m in NUM.finditer(l.strip()):
            n = m.group(1) or m.group(2)
            out.add(int(n))
    return out


def printed_numbers(pages, labels=None, window=12):
    """Return list of printed page labels (str) per pdf page, or None if unknown.

    Uses PDF page labels when they look real; else infers a local offset
    (pdf_index - printed) from numbers in running headers/footers.
    """
    n = len(pages)
    if labels and any(l != str(i + 1) for i, l in enumerate(labels[:n])):
        return list(labels[:n])
    cand = [{i + 1 - k for k in _edge_numbers(p) if 0 < k <= i + 1} for i, p in enumerate(pages)]
    out = []
    for i in range(n):
        c = Counter()
        for j in range(max(0, i - window), min(n, i + window + 1)):
            c.update(cand[j])
        if not c:
            out.append(None)
            continue
        off, votes = c.most_common(1)[0]
        own = off in cand[i]
        # need support from several pages in the window
        out.append(str(i + 1 - off) if votes >= 3 and i + 1 - off > 0 else None)
    return out


def clean_label(l):
    if l is None:
        return None
    l = re.sub(r"^(p\.|page)\s*", "", str(l).strip(), flags=re.I)
    return l if re.fullmatch(r"[0-9]{1,4}|[ivxlcdmIVXLCDM]{1,8}", l) else None


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
