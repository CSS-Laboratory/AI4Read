# Exercise 1: Shannon's F_0 ... F_3 for any text, plus held-out cross-entropy.
TRAIN_FRACTION = 0.9                                # make smaller to see D grow
import math, re, sys
from collections import Counter

text = open(sys.argv[1] if len(sys.argv) > 1 else "book.txt", encoding="utf-8").read()
text = re.sub(r"[^a-z ]+", " ", text.lower())      # at most 27 symbols: a-z and space
text = re.sub(r" +", " ", text)
cut = int(TRAIN_FRACTION * len(text))
train, test = text[:cut], text[cut:]
A = sorted(set(train))                              # the alphabet
print(f"{len(train):,} training letters, alphabet of {len(A)}")

def counts(s, n):                                   # n-letter blocks
    return Counter(s[i:i + n] for i in range(len(s) - n + 1))

def F(n):                                           # Shannon's F_N: next letter given the N-1 before it
    if n == 0:
        return math.log2(len(A))
    c, prev = counts(train, n), counts(train, n - 1) if n > 1 else None
    total = sum(c.values())
    h = 0.0
    for block, k in c.items():
        p_block = k / total
        p_cond = k / prev[block[:-1]] if n > 1 else p_block
        h -= p_block * math.log2(p_cond)
    return h

def cross_entropy(n, k=0.5):                        # add-k smoothing, bits per letter on test
    if n == 0:
        return math.log2(len(A))
    c, prev = counts(train, n), counts(train, n - 1) if n > 1 else None
    total = len(train)
    bits = 0.0
    for i in range(n - 1, len(test)):
        block = test[i - n + 1:i + 1]
        denom = (prev[block[:-1]] if n > 1 else total) + k * len(A)
        bits -= math.log2((c[block] + k) / denom)
    return bits / (len(test) - n + 1)

for n in range(4):
    f, ce = F(n), cross_entropy(n)
    print(f"N={n}:  F_N = {f:.3f} bits   held-out = {ce:.3f} bits   gap = {ce - f:+.3f}   perplexity = {2**ce:.2f}")
