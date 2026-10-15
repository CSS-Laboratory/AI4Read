---
id: basis
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 12
n_works: 4
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch02-finite, axler-2024-ladr/ch03-linear-p1, axler-2024-ladr/ch04-polynomials, boyd-2018-vmls/ch02-linear, boyd-2018-vmls/ch05-linear, boyd-2018-vmls/ch06-matrices, boyd-2018-vmls/ch11-matrix, deisenroth-2020-mml/ch02-linear-p1, deisenroth-2020-mml/ch02-linear-p2, deisenroth-2020-mml/ch03-analytic, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch03-four-p2]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# basis

## Canon spine entry

- **basis** (linear-algebra): an independent set that spans; a coordinate system (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch02-finite]] (pp. 39–40): a list that is independent and spans; gives unique coordinates
- [[axler-2024-ladr/ch03-linear-p1]] (p. 54, 62–63): used throughout the proofs
- [[axler-2024-ladr/ch04-polynomials]] (p. 124): here the explicit basis (4.10) of 𝒫_n(F) used for division
- [[boyd-2018-vmls/ch02-linear]] (p. 31): the unit vectors $e_i$ are used to decompose $x$, though the word is not used
- [[boyd-2018-vmls/ch05-linear]] (p. 92): here, $n$ independent $n$-vectors; each $n$-vector has a unique expansion
- [[boyd-2018-vmls/ch06-matrices]] (p. 121): square $A$ with independent columns; each $b$ has a unique $x$ with $Ax=b$
- [[boyd-2018-vmls/ch11-matrix]] (p. 205): used for the dual basis: rows of $A^{-1}$ give coefficients $\beta=A^{-1}x$
- [[deisenroth-2020-mml/ch02-linear-p1]] (p. 40): only previewed: a set of vectors that can represent every vector of the space
- [[deisenroth-2020-mml/ch02-linear-p2]] (pp. 44–45): a linearly independent generating set. Equivalently a minimal generating set, a maximal independent set, or a set giving unique combinations
- [[deisenroth-2020-mml/ch03-analytic]] (p. 79, 86): here used for ONB and for coordinates of a projection
- [[strang-2023-introduction/ch01-vectors]] (p. 33): only previewed here: the r columns of C are a basis, dimension r; defined in Section 3.4
- [[strang-2023-introduction/ch03-four-p2]] (p. 118): independent and spanning; gives unique coordinates

## Instances that use it

- [[example-basis-of-p3-derivative-condition]] — $1,(x-5)^2,(x-5)^3$ is a basis of $\{p\in\mathcal P_3(\mathbf R):p'(5)=0\}$ — from [[axler-2024-ladr/ch02-finite]]
- [[example-3-83-identity-two-bases]] — change-of-basis matrix for (4,2),(5,3) — from [[axler-2024-ladr/ch03-linear-p2]]
- [[example-551-diagonalization-by-new-basis]] — $\operatorname{diag}(69,46)$ in basis $(1,4),(7,5)$ — from [[axler-2024-ladr/ch05-eigenvalues-p2]]
- [[orthonormal-basis-of-p2]] — Gram–Schmidt on $1,x,x^2$ with $\int_{-1}^1$ — from [[axler-2024-ladr/ch06-inner-p2]]
- [[orthonormal-coordinates-example-f4]] — expansion of $(1,2,4,7)$ in a $\pm\frac12$ orthonormal basis — from [[axler-2024-ladr/ch06-inner-p2]]
- [[real-spectral-example-3x3]] — eigenvalues $27,9,-15$ with explicit orthonormal basis — from [[axler-2024-ladr/ch07-operators-p1]]
- [[complex-spectral-example-2x2]] — eigenvalues $2\pm3i$, basis $(\pm i,1)/\sqrt2$ — from [[axler-2024-ladr/ch07-operators-p1]]
- [[polynomial-basis-approximation]] — global quadratic features, $1+n+n^2$ basis functions — from [[bertsekas-2026-rlcourse/ch03-learning-p1]]
- [[radial-basis-functions]] — Gaussian features around anchor states, as in (3.4) — from [[bertsekas-2026-rlcourse/ch03-learning-p1]]
- [[standard-unit-vectors]] — $e_1,\dots,e_n$ are independent, orthonormal and a basis — from [[boyd-2018-vmls/ch05-linear]]
- [[single-period-loans-basis]] — $e_1,l_1,\dots,l_{n-1}$ are a basis for cash flows, and $\alpha_1$ is the NPV — from [[boyd-2018-vmls/ch05-linear]]
- [[orthonormal-basis-example-5-3]] — a 3-vector orthonormal basis used to expand $(1,2,3)$ — from [[boyd-2018-vmls/ch05-linear]]
- [[example-basis-from-pivot-columns]] — Example 2.17: $\{x_1,x_2,x_4\}$ is a basis of $U\subseteq\mathbb R^5$ — from [[deisenroth-2020-mml/ch02-linear-p2]]
- [[example-coordinates-in-two-bases]] — Example 2.20: the vector with standard coordinates $[2,3]^\top$ has coordinates $\tfrac12[-1,5]^\top$ in basis $([1,-1]^\top,[1,1]^\top)$ — from [[deisenroth-2020-mml/ch02-linear-p2]]
- [[example-diagonalising-basis-change]] — Example 2.23: $\begin{bmatrix}2&1\\1&2\end{bmatrix}\to\mathrm{diag}(3,1)$ — from [[deisenroth-2020-mml/ch02-linear-p2]]
- [[example-basis-change-r3-r4]] — Example 2.24: $\tilde A_\Phi=T^{-1}A_\Phi S$ computed — from [[deisenroth-2020-mml/ch02-linear-p2]]
- [[witness-perjury-court]] — a court's perjury threat gives a basis to trust a speaker whose interests conflict — from [[lupia-1998-dilemma/ch03-people]]
- [[rbf-infinite-limit-to-gaussian-kernel]] — infinitely many radial basis functions give a Gaussian covariance — from [[mackay-2003-information/ch45-gaussian]]
- [[galton-regression-to-the-mean]] — sons of tall/short fathers closer to the mean; shrinkage as a basis of multilevel models — from [[mcelreath-2020-rethinking/ch04-linear-p2]]
- [[keynes-beauty-contest]] — the model's basis — from [[morris-2002-public/main]]
- [[rbf-network-rjmcmc]] — posterior over number of basis functions $k$, most support at $k=2$ — from [[murphy-2023-pml2/ch12-markov-p2]]
- [[sally-anne-test]] — unexpected transfer false-belief test, basis for ToMi and ToM-k — from [[shapira-2024-clever-hans/main]]
- [[solution-space-y-double-prime-minus-y]] — basis $\sin x,\cos x$; dimension 2 — from [[strang-2023-introduction/ch03-four-p2]]
- [[projection-eigenbasis]] — projection onto y = −x becomes diag(1,0) in an eigenvector basis — from [[strang-2023-introduction/ch08-linear]]
- [[reversed-basis-svd]] — reversing the bases for d/dx gives Σ with σ = 3, 2, 1 — from [[strang-2023-introduction/ch08-linear]]
- [[turing-test-critique]] — behaviour alone is a narrow basis for attributing intelligence — from [[ullman-2023-trivial-alterations/main]]

## Candidate bridges

- [metaphor] Parties as "coalitions of groups with loose edges" ↔ social capital/network membership as basis for collective action — membership shapes behavior more than stated goals (p. 266). — from [[achen-2016-realists/ch09-partisan]] (political-science → unspecified)
- [structural-analogy] basis and unique coordinates (2.28) ↔ linear-algebra canon: change of basis — a basis gives the coordinates that the canon's change-of-basis acts on. — from [[axler-2024-ladr/ch02-finite]] (linear-algebra → linear-algebra)
- [structural-analogy] reducing a spanning list to a basis (2.30) ↔ numerical methods: a greedy, left-to-right procedure that keeps only vectors outside the span of earlier ones — compare with Gram–Schmidt in the canon. — from [[axler-2024-ladr/ch02-finite]] (linear-algebra → other:numerical-methods)
- [same-math] 3.84 A=C⁻¹BC ↔ linear-algebra spine: change of basis A ↦ P⁻¹AP — from [[axler-2024-ladr/ch03-linear-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] Dual basis as coordinate functionals ↔ statistics/data: a regression coefficient or weight vector as a linear readout of a feature vector. — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → other:statistics)
- [structural-analogy] Best polynomial approximation as projection ↔ machine learning: regression on basis functions. — from [[axler-2024-ladr/ch06-inner-p2]] (linear-algebra → llm)
- [same-math] spectral theorem for real symmetric matrices ($S=Q\Lambda Q^{\mathrm t}$) ↔ linear-algebra canon "spectral theorem": 7.29 in matrix form (orthonormal basis ↔ columns of $Q$). — from [[axler-2024-ladr/ch07-operators-p1]] (linear-algebra → linear-algebra)
- [same-math] $C^{\mathrm t}BC$ rule for the matrix of a bilinear form ↔ inner products: the Gram matrix $\langle e_j,e_k\rangle$ changes this way under a basis change — the inner product is a symmetric bilinear form here (9.10). — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → other:inner-products)
- [same-math] quadratic form $q(v)=\beta(v,v)$ on $\mathbf R^n$ with symmetric matrix ↔ canon "quadratic form $x^{\mathsf T}Sx$": the same function, shown diagonalisable by an orthonormal basis (9.23b). — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → other:canon-quadratic-form-xmathsf)
- [same-math] Diagonalising a symmetric form in an orthonormal basis (9.13) ↔ spectral theorem: it follows from that theorem, using $C^{-1}=C^{\mathrm t}$. — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → linear-algebra)
- [structural-analogy] $e_i^Ta=a_i$ and $b=\sum b_ie_i$ ↔ basis and coordinates: unit vectors play the role of a coordinate system. — from [[boyd-2018-vmls/ch01-vectors]] (linear-algebra → linear-algebra)
- [structural-analogy] Determining $f$ from $f(e_i)$ ↔ matrix as transformation: columns of $A$ are the images of the basis vectors (the scalar case is a single row). — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → linear-algebra)
- [structural-analogy] Unique coefficients in a basis ↔ linear-algebra: injectivity of a map $\beta\mapsto\sum\beta_ia_i$ — independence means this map never sends two coefficient lists to the same vector. — from [[boyd-2018-vmls/ch05-linear]] (linear-algebra → linear-algebra)
- [same-math] Orthonormal expansion $x=\sum(a_i^Tx)a_i$ ↔ linear-algebra: coordinates in an orthonormal basis (canon link; not stated in this unit). — from [[boyd-2018-vmls/ch05-linear]] (linear-algebra → linear-algebra)
- [same-math] linear function determined by $f(e_k)$ ↔ linear-algebra: matrix as transformation (columns are images of basis vectors) — same statement. — from [[boyd-2018-vmls/ch08-linear]] (linear-algebra → linear-algebra)
- [same-math] dual basis coefficients $\beta=A^{-1}x$ ↔ change of basis: $A^{-1}$ converts standard coordinates into coordinates in the basis of columns of $A$ — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → linear-algebra)
- [structural-analogy] adding basis functions until test error rises ↔ model selection generally: complexity versus generalization. — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → other:statistics)
- [same-math] Basis change $T^{-1}AS$ ↔ linear-algebra: diagonalisation $A=X\Lambda X^{-1}$ — the diagonal case $\tilde A=\mathrm{diag}$ of Example 2.23 is this with a well-chosen $S$ (the author defers this to Chapter 4). — from [[deisenroth-2020-mml/ch02-linear-p2]] (linear-algebra → linear-algebra)
- [metaphor] Coordinates in a basis ↔ choice of feature representation in machine learning — the same object, different numbers. — from [[deisenroth-2020-mml/ch02-linear-p2]] (linear-algebra → unspecified)
- [structural-analogy] Projection onto an orthonormal basis $\lambda=B^\top x$ ↔ Fourier series: coordinates are inner products with orthogonal functions (p. 81, 88). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other:signal-processing)
- [structural-analogy] Eigendecomposition as $P^{-1}$, then $D$, then $P$ ↔ change of basis: do the easy operation in the right coordinates, then return. — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → linear-algebra)
- [metaphor] Domain basis change, scaling, codomain basis change ↔ "rotate, stretch, rotate" as a general picture of any linear map. — from [[deisenroth-2020-mml/ch04-matrix-p2]] (linear-algebra → unspecified)
- [same-math] Jacobian of a linear map ↔ linear-algebra: matrix of a linear map. $\mathbf f=\mathbf A\mathbf x$ has Jacobian $\mathbf A$, and the basis-change matrix equals the Jacobian (pp. 151–153). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → linear-algebra)
- [structural-analogy] Shrinkage of basis coefficients ↔ Bayesian partial pooling: coefficients are pulled toward a common centre by a prior scale learned from data. — from [[gelman-2013-bda3/ch20-basis]] (bayesian → bayesian)
- [same-math] Basis model with Gaussian coefficient prior ↔ GP with $k=b(x)^T\Sigma_\beta b(x')$ (p. 502). — from [[gelman-2013-bda3/ch21-gaussian]] (bayesian → unspecified)
- [structural-analogy] Hall's denotative errors as channel noise ↔ Shannon noise: Hall calls literal errors a kind of noise in the channel but treats connotative misreadings as a different matter with a societal, not communicative, basis (p. 16). — from [[hall-1973-encoding/main]] (communication-theory → information-theory)
- [structural-analogy] Fundamental domain of a symmetry group fixing the prior ↔ bayesian: Principle of indifference / maximum entropy — symmetry as the formal basis for uninformative priors. — from [[jaynes-2003-probability/ch10-physics]] (bayesian → bayesian)
- [structural-analogy] MAP basis dependence (22.29) ↔ Bayesian: Jacobian of a density under change of variables — densities transform with $|\partial\theta/\partial u|$, so maxima move. — from [[mackay-2003-information/ch22-maximum]] (information-theory → bayesian)
- [same-math] softmax basis (23.33) ↔ machine learning: softmax output layer of a classifier — same normalized-exponential map. — from [[mackay-2003-information/ch23-useful]] (information-theory → llm)
- [structural-analogy] KL $\approx\frac12\delta^\top F\delta$ ↔ squared Mahalanobis distance with the Fisher matrix as metric (an approximation), the basis of natural gradient (§5.1.9). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → unspecified)
- [same-math] EM's ELBO (6.140–6.145) ↔ Bayesian inference: variational ELBO and KL to the posterior — the text itself says this bound is the basis of variational inference. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → bayesian)
- [same-math] Product decomposition (1.29) ↔ Bayesian network factorization: the book itself says it became the semantic basis of Bayesian networks (p. 33). — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → bayesian)
- [same-math] JS variational formula (Example 7.5) ↔ machine learning: the text says this characterization is the basis of the GAN objective. — from [[polyanskiy-2025-information/ch08-f-p2]] (information-theory → llm)
- [structural-analogy] Choosing a representation basis ↔ feature engineering: structure sometimes becomes visible only after a change of basis. — from [[polyanskiy-2025-information/ch11-lossless]] (information-theory → other:statistics)
- [structural-analogy] CG's A-orthogonal basis ↔ linear-algebra: Lanczos-type bases for Krylov subspaces — both build a basis of a Krylov subspace by a short recurrence. — from [[spielman-2025-sagt/ch35-conjugate]] (linear-algebra → linear-algebra)
- [structural-analogy] Decoupling by A-orthogonality ↔ PCA: diagonalizing a covariance matrix — a good basis removes cross terms. — from [[spielman-2025-sagt/ch35-conjugate]] (linear-algebra → linear-algebra)
- [structural-analogy] translate–act–translate back, T₋PT₊ ↔ change of basis: A ↦ P⁻¹AP — conjugating by an invertible map. — from [[strang-2023-introduction/app10-computer]] (linear-algebra → linear-algebra)
- [structural-analogy] $V=WB$ with B invertible ↔ change of basis: the same space described by different basis vectors (p. 123). — from [[strang-2023-introduction/ch03-four-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] Choosing a basis that diagonalizes A (U⁻¹AV = Σ) ↔ principal component analysis: finding axes in which a data matrix is simple. — from [[strang-2023-introduction/ch08-linear]] (linear-algebra → linear-algebra)
