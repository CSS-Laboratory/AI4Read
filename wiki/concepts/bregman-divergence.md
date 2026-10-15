---
id: bregman-divergence
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 3
n_works: 2
tiers: [deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch05-information-p1, nielsen-2020-elementary/main-p1, nielsen-2020-elementary/main-p2]
generated_by: build_kg.py
---

# bregman-divergence

## Definitions in the sources

### information-theory

- [[nielsen-2020-elementary/main-p1]] (p. 14): $B_F$ of a strictly convex potential, eq. (57) [new]
- [[nielsen-2020-elementary/main-p2]] (pp. 28, 47): $B_F(\theta:\theta')=F(\theta)-F(\theta')-\langle\theta-\theta',\nabla F(\theta')\rangle$ for convex $F$; squared Mahalanobis is the symmetric case [new]

### bayesian

- [[murphy-2023-pml2/ch05-information-p1]] (p. 233): $f(w)-f(v)-(w-v)^\top\nabla f(v)$ [new; work fields: bayesian, information-theory]

## Candidate bridges

- [same-math] KL between exponential-family members = Bregman divergence of the log-normalizer ↔ information theory: coding-cost excess (relative entropy) — same quantity (p. 29). — from [[nielsen-2020-elementary/main-p2]] (information-theory → information-theory)
