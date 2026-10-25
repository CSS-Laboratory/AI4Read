"""Shared helpers for AI4Read passage-centred English packs (ai4read.english-pack/2).

The passage is split into sentences in one way only (this function), so the builder
(english_pack.py) and the recorder (tts_english_passage.py) always agree on the boundaries."""
import re, hashlib

# A sentence ends at . ? ! followed by a space and a capital, digit, quote or bracket.
# Writers must avoid abbreviations with a full stop inside the passage (e.g., i.e., etc.); the builder checks this.
ABBREV = re.compile(r"\b(e\.g|i\.e|etc|cf|vs|Dr|Mr|Mrs|Ms|Fig|No)\.", re.I)


def u16(t: str) -> int:
    """Length in UTF-16 code units (what JavaScript's String.length counts)."""
    return len(t.encode("utf-16-le")) // 2


def split_sentences(text: str):
    """Return [(start, end, sentence_text)] with UTF-16 offsets. Sentences are separated by single spaces."""
    out, pos = [], 0
    nxt = r"(?=[\"'“‘(A-Z0-9])"
    parts = [p for p in re.split(r"(?:(?<=[.?!])|(?<=[.?!][\"'”’)]))\s+" + nxt, text) if p]
    for p in parts:
        k = text.index(p, pos)
        out.append((u16(text[:k]), u16(text[:k]) + u16(p), p))
        pos = k + len(p)
    return out


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def words(text: str) -> int:
    return len(text.split())
