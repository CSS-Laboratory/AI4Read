---
id: covariance-matrix
type: concept
fields: [linear-algebra]
n_sources: 6
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p1, deisenroth-2020-mml/ch06-probability-p2, deisenroth-2020-mml/ch10-dimensionality, eckart-1936-lowrank/main, strang-2023-introduction/ch07-singular, strang-2023-introduction/ch10-learning]
raw_ids: [covariance matrix]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# covariance-matrix

## Canon spine entry

- **covariance matrix** (linear-algebra): XᵀX/(n−1) for centred X; second-order structure of the data (UG)

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 190): $\mathbb E[\boldsymbol{xx}^\top]-\mathbb E[\boldsymbol x]\mathbb E[\boldsymbol x]^\top$; symmetric positive semidefinite [as `covariance matrix`]
- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 199): here $\Sigma$ in the Gaussian; blocks $\Sigma_{xx},\Sigma_{yy}$ are marginal covariances, $\Sigma_{xy}$ the cross-covariance
- [[deisenroth-2020-mml/ch10-dimensionality]] (pp. 318, 323): here $S=\frac1N\sum x_nx_n^\top=\frac1NXX^\top$ for centered data, with data points as columns of $X$ [as `covariance matrix`]
- [[eckart-1936-lowrank/main]] (pp. 213–214): the paper's "correlational matrices" $\alpha\alpha'$ and $\alpha'\alpha$, whose characteristic values are squared multipliers
- [[strang-2023-introduction/ch07-singular]] (p. 305): $S=AA^T/(n-1)$ for centred $A$; diagonal = variances, off-diagonal = covariances
- [[strang-2023-introduction/ch10-learning]] (pp. 395–396): V = E[(X−X̄)(X−X̄)ᵀ]; here built as a sum of p_ij UUᵀ [as `covariance matrix`]

## Instances that use it

- [[glued-coins]] — perfectly correlated coins with a singular covariance matrix — from [[strang-2023-introduction/ch10-learning]]

## Candidate bridges

- [same-math] Covariance-like Gram matrix $\tilde A^T\tilde A/n$ (exercise 10.16) ↔ statistics: covariance matrix of de-meaned data. — from [[boyd-2018-vmls/ch10-matrix]] (linear-algebra → other)
- [structural-analogy] $A^\top A$ and its eigenvectors ↔ statistics: the covariance-matrix route to principal components. The unit only says the SVD plays a key role in PCA. — from [[deisenroth-2020-mml/ch04-matrix-p2]] (linear-algebra → other)
- [same-math] covariance matrix symmetric PSD (p. 190) ↔ linear-algebra: spectral theorem — real symmetric PSD matrices have orthonormal eigenbases and nonnegative eigenvalues. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [structural-analogy] Weighted covariance update (11.30) ↔ PCA/covariance matrix: the same average of outer products of centered data, but with responsibility weights. — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → linear-algebra)
- [same-math] Exercise 7.4's weights (7.39)–(7.40) ↔ statistics: minimum-variance linear combination under a known covariance matrix (p. 215) — from [[jaynes-2003-probability/ch07-central-p1]] (information-theory → other)
- [same-math] Logistic output of a neuron ↔ Bayesian: posterior $P(s=1|\mathbf y)$ with Gaussian likelihoods and a shared covariance matrix (eqs. 39.8–39.9, section 11.2) — the formulas coincide. — from [[mackay-2003-information/ch39-single]] (information-theory → bayesian)
- [structural-analogy] $\psi_2,\psi_3$ as coordinates ↔ PCA: low-dimensional coordinates from eigenvectors, though PCA uses a covariance matrix. — from [[spielman-2025-sagt/ch01-introduction]] (linear-algebra → linear-algebra)
- [same-math] Rayleigh quotient maximization ↔ PCA: choosing the direction of maximal variance of a covariance matrix. — from [[spielman-2025-sagt/ch02-eigenvalues]] (linear-algebra → linear-algebra)
- [structural-analogy] Decoupling by A-orthogonality ↔ PCA: diagonalizing a covariance matrix — a good basis removes cross terms. — from [[spielman-2025-sagt/ch35-conjugate]] (linear-algebra → linear-algebra)
- [same-math] Spectral theorem S = QΛQᵀ ↔ PCA: eigen-decomposition of a covariance matrix gives orthogonal principal directions. — from [[strang-2023-introduction/ch06-eigenvalues-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] Cholesky S = AᵀA ↔ statistics: factoring a covariance matrix into a triangular factor (not in this unit). — from [[strang-2023-introduction/ch06-eigenvalues-p2]] (linear-algebra → other)
