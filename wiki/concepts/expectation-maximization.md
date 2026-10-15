---
id: expectation-maximization
type: concept
fields: [bayesian, information-theory]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch04-graphical-p1, polyanskiy-2025-information/ch06-extremization]
generated_by: build_kg.py
---

# expectation-maximization

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch04-graphical-p1]] (pp. 160–161): for hidden variables: E step gives expected counts, M step normalizes them [new]

### information-theory

- [[polyanskiy-2025-information/ch06-extremization]] (p. 105): E-step sets $P_{Y|X}=Q^{(\theta)}_{Y|X}$; M-step maximizes over $\theta$ [new]

## Candidate bridges

- [same-math] Soft K-means update (22.21) ↔ Expectation–Maximization for Gaussian mixtures — the same weighted-mean update; these pages never mention EM, and say only that a proof that the algorithm maximizes the likelihood is deferred to section 33.7 (p. 305). — from [[mackay-2003-information/ch22-maximum]] (information-theory → unspecified)
