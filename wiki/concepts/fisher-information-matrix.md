---
id: fisher-information-matrix
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch05-information-p1, murphy-2023-pml2/ch06-optimization-p1]
generated_by: build_kg.py
---

# fisher-information-matrix

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch05-information-p1]] (p. 233): metric in $D_{KL}\approx\frac12\delta^\top F\delta$ [new; work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 280): $F=\mathbb E[\nabla\log p\,\nabla\log p^\top]$, local quadratic form of KL [new]

## Candidate bridges

- [same-math] Fisher information matrix (8.54) ↔ information-theory: local curvature of KL divergence / Fisher–Rao metric (up to the sign issue in Reading notes). — from [[jaynes-2003-probability/ch08-sufficiency]] (bayesian → information-theory)
