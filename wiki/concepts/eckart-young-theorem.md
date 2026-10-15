---
id: eckart-young-theorem
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra]
n_sources: 6
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch07-operators-p3, deerwester-1990-lsa/main, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch10-dimensionality, eckart-1936-lowrank/main, strang-2023-introduction/ch07-singular]
raw_ids: [Eckart–Young theorem, eckart-young theorem]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# eckart-young-theorem

## Canon spine entry

- **Eckart–Young theorem** (linear-algebra): the truncated SVD is the best rank-k approximation (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch07-operators-p3]] (p. 284): 7.92: the truncated SVD $T_k$ is the best approximation with range dimension $\le k$, error $s_{k+1}$ (in the operator norm; the book gives no name)
- [[deerwester-1990-lsa/main]] (pdf 13): the paper states without proof that truncation gives the closest rank-$k$ matrix in the least-squares sense; no name or proof is given (canon link; not stated in this unit) [weak: not really used in this unit; work fields: linear-algebra, llm]
- [[deisenroth-2020-mml/ch04-matrix-p2]] (p. 131): the truncated SVD is the best rank-$k$ approximation in spectral norm, with error $\sigma_{k+1}$ [as `eckart-young theorem`]
- [[deisenroth-2020-mml/ch10-dimensionality]] (p. 334): the truncated SVD is the best rank-$M$ approximation of $X$ [as `Eckart–Young theorem`]
- [[eckart-1936-lowrank/main]] (p. 216): keeping the $r$ largest multipliers gives the closest rank-$r$ matrix in least-squares distance
- [[strang-2023-introduction/ch07-singular]] (p. 302, p. 303): truncated SVD $A_k$ is closest rank-$k$ matrix in these norms

## Candidate bridges

- [same-math] 7.92 ↔ Eckart–Young theorem (spectral-norm version) — same statement: truncated SVD is the best rank-$k$ approximation, error $s_{k+1}$. — from [[axler-2024-ladr/ch07-operators-p3]] (linear-algebra → unspecified)
