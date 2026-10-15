---
id: toeplitz-matrix
type: concept
fields: [linear-algebra]
n_sources: 2
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/ch07-matrix, strang-2023-introduction/ch02-solving-p2]
generated_by: build_kg.py
---

# toeplitz-matrix

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch07-matrix]] (p. 138): entries constant along diagonals; $T(a)$ has shifted copies of $a$ as columns [new]
- [[strang-2023-introduction/ch02-solving-p2]] (p. 78): constant diagonals; tied to filters, convolution and Fourier [new]

## Candidate bridges

- [structural-analogy] Toeplitz matrix $T(a)$ ↔ shift-invariant (time-invariant) linear systems: each column is the previous one shifted. — from [[boyd-2018-vmls/ch07-matrix]] (linear-algebra → other)
- [same-math] Convolution matrix with constant diagonals ↔ linear algebra: Toeplitz/band matrix — the text identifies the filter as a Toeplitz matrix (p. 383) — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → linear-algebra)
