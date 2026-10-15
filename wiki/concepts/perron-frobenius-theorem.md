---
id: perron-frobenius-theorem
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 8
n_works: 3
tiers: [deep, core]
grounding: digests
sources: [bryan-2006-eigenvector/main, spielman-2025-sagt/ch04-adjacency, spielman-2025-sagt/ch10-random, spielman-2025-sagt/ch11-walks, spielman-2025-sagt/ch24-nodal, spielman-2025-sagt/ch30-simple, spielman-2025-sagt/ch38-fast, strang-2023-introduction/app1-ranks]
raw_ids: [Perron–Frobenius theorem]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# perron-frobenius-theorem

## Canon spine entry

- **Perron–Frobenius theorem** (linear-algebra): positive matrices have a unique positive dominant eigenvector; guarantees well-defined PageRank and eigenvector centrality (grad)

## Definitions in the sources

### linear-algebra

- [[bryan-2006-eigenvector/main]] (p. 5, 6): the authors' analysis is a special case; Perron eigenvector for substochastic $A$
- [[spielman-2025-sagt/ch04-adjacency]] (p. 39): symmetric case: connected $G$ gives positive top eigenvector, $\mu_1\ge-\mu_n$, $\mu_1>\mu_2$
- [[spielman-2025-sagt/ch10-random]] (p. 94): gives eigenvalues of A in [−1,1]
- [[spielman-2025-sagt/ch11-walks]] (p. 106): used for nonnegative $B$: largest eigenvalue below 1 gives $\|B\|<1$
- [[spielman-2025-sagt/ch24-nodal]] (p. 201): applied to $\sigma I-M$, giving a simple smallest eigenvalue with positive eigenvector
- [[spielman-2025-sagt/ch30-simple]] (p. 247): used to bound λ_max(G) ≤ 2d
- [[spielman-2025-sagt/ch38-fast]] (p. 301): used to show $D\succ-A$ [as `Perron–Frobenius theorem`]
- [[strang-2023-introduction/app1-ranks]] (p. 409): here only Perron's case: positive A has a strictly positive top eigenvector [as `Perron–Frobenius theorem`]

## Candidate bridges

- [same-math] Lemma 3.2 / Props. 2–5 ↔ Perron–Frobenius theorem for positive matrices — authors call their analysis a special case (p. 6) — from [[bryan-2006-eigenvector/main]] (linear-algebra → unspecified)
