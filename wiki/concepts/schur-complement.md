---
id: schur-complement
type: concept
fields: [linear-algebra, bayesian]
n_sources: 3
tiers: [core, deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch02-probability-p2, spielman-2025-sagt/ch12-effective, strang-2023-introduction/ch09-linear]
generated_by: build_kg.py
---

# schur-complement

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch12-effective]] (pp. 118–119): $M(B,B)-M(B,S)M(S,S)^{-1}M(S,B)$; Gaussian elimination of $S$ [new]
- [[strang-2023-introduction/ch09-linear]] (p. 359): block −AᵀS⁻¹A that appears in the 2,2 position after block elimination [new]

### bayesian

- [[murphy-2023-pml2/ch02-probability-p2]] (p. 26): $\mathbf M/\mathbf H=\mathbf E-\mathbf F\mathbf H^{-1}\mathbf G$, appears in block inverses and conditional covariances (new)

## Candidate bridges

- [same-math] Gaussian conditioning (6.66)–(6.67) ↔ linear-algebra: least squares/projection, where the conditional mean is a linear regression of $x$ on $y$ with the Schur complement as residual covariance — the formulas are the same block-matrix algebra (the text itself does not state this link). — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] Bayesian marginalization of $B$ and Gaussian completion with Schur complements ↔ linear algebra: the block-determinant identity $\det M=\det W_0\det U$ with $U$ the Schur complement (p. 548; see Reading notes on (17.157)). — from [[jaynes-2003-probability/ch17-principles-p2]] (information-theory → linear-algebra)
- [same-math] Schur complement $M_B$ ↔ linear-algebra: block Gaussian elimination, with $(M^{-1})(B,B)=(M_B)^{-1}$ — the same block formulas. — from [[spielman-2025-sagt/ch12-effective]] (linear-algebra → linear-algebra)
- [same-math] Elimination with Schur complement ↔ Gaussian elimination / sparse Cholesky: eliminating vertices leaves the Schur complement. — from [[spielman-2025-sagt/ch37-augmented]] (linear-algebra → other)
- [same-math] Block elimination on K giving −AᵀS⁻¹A ↔ linear-algebra: Schur complement and pivots — elimination on a 2×2 block matrix. — from [[strang-2023-introduction/ch09-linear]] (linear-algebra → linear-algebra)
