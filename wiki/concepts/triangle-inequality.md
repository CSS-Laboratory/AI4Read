---
id: triangle-inequality
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 4
n_works: 3
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch04-polynomials, axler-2024-ladr/ch06-inner-p1, boyd-2018-vmls/ch03-norm, strang-2023-introduction/ch01-vectors]
generated_by: build_kg.py
---

# triangle-inequality

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch04-polynomials]] (p. 121): |w + z| ≤ |w| + |z| for complex numbers [new]
- [[axler-2024-ladr/ch06-inner-p1]] (p. 190): $\|u+v\|\le\|u\|+\|v\|$ [new]
- [[boyd-2018-vmls/ch03-norm]] (pp. 46, 49): ‖x+y‖ ≤ ‖x‖+‖y‖; the distance form is (3.3) [new]
- [[strang-2023-introduction/ch01-vectors]] (p. 13): ‖v + w‖ ≤ ‖v‖ + ‖w‖, derived from Schwarz [new]

## Instances that use it

- [[three-vertex-reduction]] — eliminating $c$ gives edge $xy/(x+y)$, used for the triangle inequality — from [[spielman-2025-sagt/ch12-effective]]

## Candidate bridges

- [structural-analogy] Similarity–dissimilarity map $S=e^{-D}$ ↔ probability/likelihood: additive triangle inequality becomes multiplicative (p. 41). — from [[nielsen-2020-elementary/main-p2]] (information-theory → bayesian)
