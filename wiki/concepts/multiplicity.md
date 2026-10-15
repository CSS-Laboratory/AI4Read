---
id: multiplicity
type: concept
fields: [information-theory, linear-algebra]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [axler-2024-ladr/ch08-operators, jaynes-2003-probability/ch03-elementary]
generated_by: build_kg.py
---

# multiplicity

## Definitions in the sources

### information-theory

- [[jaynes-2003-probability/ch03-elementary]] (p. 55): the number of orders in which an event $r$ can occur, $\binom nr$ [new]

### linear-algebra

- [[axler-2024-ladr/ch08-operators]] (pp. 310–311): $\dim G(\lambda,T)$, the book's "algebraic multiplicity" [new]

## Instances that use it

- [[ex-upper-triangular-6-7]] — matrix with eigenvalues 6 (multiplicity 2) and 7: multiplicity, characteristic polynomial, block form — from [[axler-2024-ladr/ch08-operators]]
- [[defective-2x2]] — $\begin{bmatrix}2&1\\0&2\end{bmatrix}$, algebraic multiplicity 2, geometric multiplicity 1 — from [[deisenroth-2020-mml/ch04-matrix-p1]]
- [[dodecahedron-graph]] — $\lambda_2$ has multiplicity 3, so draw in 3-D — from [[spielman-2025-sagt/ch01-introduction]]
- [[hypercube]] — eigenvalues 2i with multiplicity C(d,i); θ ≥ 1, tight — from [[spielman-2025-sagt/ch05-fundamental]]
- [[failed-generality-notations]] — notations for generality lack the required multiplicity — from [[wittgenstein-1922-tractatus/ch04-proposition]]

## Candidate bridges

- [same-math] trace $=$ sum of eigenvalues with multiplicity (8.52) ↔ linear-algebra: total variance in PCA equals the sum of covariance eigenvalues (covariance is symmetric, so it is a special case). — from [[axler-2024-ladr/ch08-operators]] (linear-algebra → linear-algebra)
- [same-math] Multiplicity $M\sim e^{nH}$ ↔ information-theory: number of sequences of a given type is $\approx 2^{nH}$ (method of types / typical set) — same counting by Stirling, in natural logs. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (information-theory → information-theory)
- [same-math] Wallis multiplicity and Stirling's approximation ↔ information theory: Shannon entropy as the rate of growth of log counts — the derivation is literally this. — from [[mcelreath-2020-rethinking/ch09-big]] (bayesian → information-theory)
- [metaphor] Folk-theorem multiplicity ↔ equilibrium selection: many outcomes sustainable, so theory alone does not pick one. — from [[osborne-2004-introduction/ch15-repeated]] (decision-game-theory → political-science)
