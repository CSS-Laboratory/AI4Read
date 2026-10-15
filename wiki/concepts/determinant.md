---
id: determinant
type: concept
fields: [linear-algebra]
n_sources: 8
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch07-operators-p3, axler-2024-ladr/ch09-multilinear-p2, deisenroth-2020-mml/ch04-matrix-p1, deisenroth-2020-mml/ch05-vector, deisenroth-2020-mml/ch06-probability-p2, spielman-2025-sagt/ch13-random, strang-2023-introduction/ch02-solving-p1, strang-2023-introduction/ch05-determinants]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# determinant

## Canon spine entry

- **determinant** (linear-algebra): the signed factor by which a map scales area or volume; zero means space is flattened (HS)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch07-operators-p3]] (p. 293): only as a forward reference: product of singular values $=|\det T|$
- [[axler-2024-ladr/ch09-multilinear-p2]] (pp. 354–355): scalar $\det T$ with $\alpha_T=(\det T)\alpha$ on $V_{\rm alt}^{(\dim V)}$. For a matrix, the determinant of its operator on $\mathbf F^n$
- [[deisenroth-2020-mml/ch04-matrix-p1]] (pp. 99–103): real number from a square matrix; $|\det|$ is the volume spanned by the columns, sign is orientation; non-zero iff invertible
- [[deisenroth-2020-mml/ch05-vector]] (p. 152): here, $|\det\mathbf J|$ gives the local area/volume scaling under a coordinate change
- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 219): here the Jacobian determinant measures volume change of the inverse map
- [[spielman-2025-sagt/ch13-random]] (pp. 123–124): volume of a parallelepiped; $\sigma_k$ acts as the determinant on a rank-$k$ span
- [[strang-2023-introduction/ch02-solving-p1]] (p. 50): ad − bc for 2 by 2; invertible iff nonzero
- [[strang-2023-introduction/ch05-determinants]] (pp. 198, 211): one number per square matrix; zero signals dependent columns; |det| is the volume of the edge box

## Instances that use it

- [[vandermonde-matrix]] — determinant $\prod_{j<k}(\beta_k-\beta_j)$, via $S$, $T$, $C=AB$ — from [[axler-2024-ladr/ch09-multilinear-p2]]
- [[toeplitz-determinant-monotonicity]] — stationary-process entropy rate analogue for $|K_k|^{1/k}$ — from [[cover-2006-elements/ch16-inequalities]]
- [[cesaro-limit-entropy-rate]] — $\lim h(X^n)/n=\lim h(X_n|X^{n-1})$ used for determinants — from [[cover-2006-elements/ch16-inequalities]]
- [[eigen-2d-gallery]] — five 2D maps (scaling, shear, rotation, collapse, shear-stretch) with their eigenvalues and determinants — from [[deisenroth-2020-mml/ch04-matrix-p1]]
- [[second-difference-matrix]] — 2, −1, −1 pattern: determinants 2, 3, 4, 5, pivots 2, 3/2, 4/3, 5/4 — from [[strang-2023-introduction/ch06-eigenvalues-p2]]

## Candidate bridges

- [same-math] Product of singular values $=|\det T|$ (p. 293, forward reference) ↔ determinant as signed volume-scaling factor. — from [[axler-2024-ladr/ch07-operators-p3]] (linear-algebra → unspecified)
- [same-math] Formula 9.36/9.38, a signed sum over permutations of products of entries ↔ determinant: the later chapter presumably identifies this expression with the determinant (not stated in these pages). — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → other)
- [same-math] Entropy power inequality ↔ Matrix theory: Minkowski determinant inequality (via Gaussians, p. 505). — from [[cover-2006-elements/ch16-inequalities]] (information-theory → linear-algebra)
- [metaphor] Trace and determinant as "sum and product of stretches" ↔ geometry: perimeter and area of the image of a unit square (valid only for the orthonormal-eigenvector picture on p. 113). — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → other)
- [same-math] Jacobian determinant ↔ probability: change-of-variables density factor. The text defers this to Section 6.7 (p. 152). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → other)
- [same-math] Jacobian determinant in (6.144) ↔ linear-algebra: determinant as signed volume scaling. — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] Bayesian marginalization of $B$ and Gaussian completion with Schur complements ↔ linear algebra: the block-determinant identity $\det M=\det W_0\det U$ with $U$ the Schur complement (p. 548; see Reading notes on (17.157)). — from [[jaynes-2003-probability/ch17-principles-p2]] (information-theory → linear-algebra)
- [metaphor] Determinates versus determinants ↔ modelling: endogenous outcomes versus exogenous drivers. — from [[keynes-1936-general/ch14-classical]] (economics-finance → other)
- [structural-analogy] RJMCMC change of measure ↔ change of variables with Jacobian determinant in probability densities. — from [[murphy-2023-pml2/ch12-markov-p2]] (bayesian → unspecified)
- [same-math] Flow density via change of variables ↔ probability: transformation of random variables — the same formula with the Jacobian determinant. — from [[murphy-2023-pml2/ch23-normalizing]] (bayesian → other)
- [same-math] Spectral-density formula for the information rate ↔ signal processing: log-determinant of Toeplitz covariances and Szegő's theorem. — from [[polyanskiy-2025-information/ch07-tensorization]] (information-theory → other)
- [structural-analogy] Flow training by negative log-likelihood ↔ llm: cross-entropy minimization, here with an added log-determinant term — from [[prince-2023-udl/ch16-normalizing]] (llm → llm)
- [same-math] $\sigma_{n-1}(L_G)$ and principal minors of $L_G$ ↔ combinatorics: counting spanning trees by determinants, as in the Matrix-Tree Theorem. — from [[spielman-2025-sagt/ch13-random]] (linear-algebra → other)
- [same-math] Lemma 44.5.1 rank-one update $\chi_x(A+tvv^T)=\chi_x(A)-tq$ ↔ linear algebra: determinant linearity in one entry plus rotation invariance. — from [[spielman-2025-sagt/ch44-bipartite]] (linear-algebra → linear-algebra)
- [same-math] $\mu_x[T]=\chi_x(A_T)$ for trees ↔ linear-algebra: determinant expansion over permutations — only involutions survive when there are no cycles. — from [[spielman-2025-sagt/ch45-matching]] (linear-algebra → linear-algebra)
- [same-math] Jacobian determinant as area/volume scaling ↔ change-of-variables for densities under a map: both use $|\det\mathbf J|$. — from [[strogatz-2024-nonlinear/ch12-strange]] (complex-systems → other)
