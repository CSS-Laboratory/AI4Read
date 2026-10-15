---
id: orthogonality
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 14
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch06-inner-p1, axler-2024-ladr/ch06-inner-p2, boyd-2018-vmls/ch01-vectors, boyd-2018-vmls/ch03-norm, boyd-2018-vmls/ch05-linear, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch06-probability-p1, deisenroth-2020-mml/ch12-classification, spielman-2025-sagt/ch03-laplacian, spielman-2025-sagt/ch05-fundamental, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch02-solving-p2, strang-2023-introduction/ch04-orthogonality-p1, strang-2023-introduction/ch06-eigenvalues-p3]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# orthogonality

## Canon spine entry

- **orthogonality** (linear-algebra): inner product zero; independent directions that do not interfere (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch06-inner-p1]] (p. 187): $\langle u,v\rangle=0$
- [[axler-2024-ladr/ch06-inner-p2]] (p. 211): inner product zero; here extended to sets via $U^\perp$
- [[boyd-2018-vmls/ch01-vectors]] (p. 24): not defined in this unit; only the sparse non-overlapping case $x^Ty=0$ appears [weak: not really used in this unit]
- [[boyd-2018-vmls/ch03-norm]] (pp. 58, 60): aᵀb = 0, angle 90°; norm-squares then add (Pythagoras)
- [[boyd-2018-vmls/ch05-linear]] (p. 95): $a_i\perp a_j$ for $i\neq j$; used for orthogonal and orthonormal lists
- [[deisenroth-2020-mml/ch03-analytic]] (p. 77): $\langle x,y\rangle=0$; depends on the chosen inner product
- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 196): here: uncorrelated ⟺ $\mathrm{Cov}=0$
- [[deisenroth-2020-mml/ch12-classification]] (p. 373): $\boldsymbol w$ is orthogonal to every vector lying in the hyperplane
- [[spielman-2025-sagt/ch03-laplacian]] (p. 32): constraints $\mathbf 1^Tx=0$, $x\perp y$ keep drawings non-degenerate
- [[spielman-2025-sagt/ch05-fundamental]] (p. 45–46): used to force eigenvector structure in stars
- [[strang-2023-introduction/ch01-vectors]] (p. 10): v·w = 0, the angle is 90°
- [[strang-2023-introduction/ch02-solving-p2]] (p. 65): columns of a permutation matrix have zero dot products
- [[strang-2023-introduction/ch04-orthogonality-p1]] (pp. 143–144): vᵀw = 0; for subspaces, every vector of one is orthogonal to every vector of the other
- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 264): in the complex case x̄ᵀy = 0

## Candidate bridges

- [structural-analogy] generalized eigenspace decomposition ↔ linear-algebra: spectral theorem — both split $V$ into $T$-invariant pieces, one per eigenvalue, without needing orthogonality in the first. — from [[axler-2024-ladr/ch08-operators]] (linear-algebra → linear-algebra)
- [structural-analogy] Decoupling by A-orthogonality ↔ PCA: diagonalizing a covariance matrix — a good basis removes cross terms. — from [[spielman-2025-sagt/ch35-conjugate]] (linear-algebra → linear-algebra)
- [structural-analogy] CP tensor decomposition ↔ data science: low-rank matrix factorization, extended to three indices without orthogonality. — from [[strang-2023-introduction/app1-ranks]] (linear-algebra → other:statistics)
