---
id: rayleigh-quotient
type: concept
fields: [linear-algebra]
n_sources: 19
tiers: [deep, core]
grounding: digests
sources: [spielman-2025-sagt/ch02-eigenvalues, spielman-2025-sagt/ch03-laplacian, spielman-2025-sagt/ch04-adjacency, spielman-2025-sagt/ch05-fundamental, spielman-2025-sagt/ch06-comparing, spielman-2025-sagt/ch08-eigenvalues, spielman-2025-sagt/ch10-random, spielman-2025-sagt/ch19-independent, spielman-2025-sagt/ch20-graph, spielman-2025-sagt/ch21-cheeger, spielman-2025-sagt/ch22-local, spielman-2025-sagt/ch24-nodal, spielman-2025-sagt/ch25-second, spielman-2025-sagt/ch27-properties, spielman-2025-sagt/ch35-conjugate, spielman-2025-sagt/ch36-preconditioning, strang-2023-introduction/ch06-eigenvalues-p3, strang-2023-introduction/ch07-singular, vonluxburg-2007-spectralclustering/main]
raw_ids: [Rayleigh quotient]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# rayleigh-quotient

## Canon spine entry

- **Rayleigh quotient** (linear-algebra): xᵀSx / xᵀx; its max and min are the extreme eigenvalues (Courant–Fischer) (grad)

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch02-eigenvalues]] (p. 21): $x^TMx/x^Tx$; equals $\mu$ at an eigenvector
- [[spielman-2025-sagt/ch03-laplacian]] (p. 31): Theorem 2.0.1 (cited) says a unit $\lambda_2$-eigenvector minimizes $x^TLx$ under (3.6)–(3.7) [as `Rayleigh quotient`]
- [[spielman-2025-sagt/ch04-adjacency]] (p. 35): $x^TMx/x^Tx$; its maximum is $\mu_1$, and a test vector gives lower bounds
- [[spielman-2025-sagt/ch05-fundamental]] (p. 48): vᵀLv/vᵀv, upper-bounds λ₂ for v ⊥ 1 (Courant–Fischer) [as `Rayleigh quotient`]
- [[spielman-2025-sagt/ch06-comparing]] (p. 55): $x^TLx/x^Tx$, used via Courant–Fischer min–max
- [[spielman-2025-sagt/ch08-eigenvalues]] (p. 71–72): $x^TRx/x^Tx$, bounded for fixed $x$ by Hoeffding
- [[spielman-2025-sagt/ch10-random]] (p. 97): ν₂ = min_{y⊥d} yᵀLy/yᵀDy
- [[spielman-2025-sagt/ch19-independent]] (p. 165): $x^TLx/x^Tx$; its maximum is $\lambda_n$ (Courant–Fischer)
- [[spielman-2025-sagt/ch20-graph]] (p. 172): $x^TLx/x^Tx$; its minimum over $x\perp\mathbf 1$ is $\lambda_2$
- [[spielman-2025-sagt/ch21-cheeger]] (p. 176): here the generalized one with respect to $L$ and $D$; equals $\nu_2$ for $y=D^{1/2}\psi_2$
- [[spielman-2025-sagt/ch22-local]] (p. 182): used here in generalized form $p^TD^{-1}LD^{-1}p/p^TD^{-1}p$
- [[spielman-2025-sagt/ch24-nodal]] (p. 199): $x^TMx/x^Tx$; used via Courant–Fischer in the Sylvester proof
- [[spielman-2025-sagt/ch25-second]] (p. 205): here in vector-valued form (25.1), the ratio of edge energy to norm for a mean-zero embedding
- [[spielman-2025-sagt/ch27-properties]] (p. 224): $x^TLx/x^Tx$; used with test vectors to upper-bound $\lambda_2$ [as `Rayleigh quotient`]
- [[spielman-2025-sagt/ch35-conjugate]] (p. 281): measures quality of the approximate eigenvector
- [[spielman-2025-sagt/ch36-preconditioning]] (p. 287): $\max_y y^TAy/y^TBy$ gives $\beta$
- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 264): x̄ᵀSx / x̄ᵀx; real; max and min give extreme eigenvalues
- [[strang-2023-introduction/ch07-singular]] (p. 293): $x^TSx/x^Tx\le\lambda_1$; for $S=A^TA$ its max is $\sigma_1^2$
- [[vonluxburg-2007-spectralclustering/main]] (pp. 11–12): Rayleigh–Ritz theorem gives solutions of relaxed cut problems as bottom eigenvectors

## Candidate bridges

- [same-math] PCA's maximize $b^\top Sb$ s.t. $\|b\|=1$ ↔ linear algebra: Rayleigh quotient maximization — the maximum is the top eigenvalue, attained at its eigenvector. — from [[deisenroth-2020-mml/ch10-dimensionality]] (linear-algebra → linear-algebra)
- [same-math] Rayleigh quotient maximization ↔ PCA: choosing the direction of maximal variance of a covariance matrix. — from [[spielman-2025-sagt/ch02-eigenvalues]] (linear-algebra → linear-algebra)
- [same-math] $x^TLx=\sum_j\lambda_j(\psi_j^Tx)^2$ minimized over orthonormal frames ↔ linear-algebra: Rayleigh quotient / Courant–Fischer — Theorem 3.2.1 is the multi-vector (trace) version. — from [[spielman-2025-sagt/ch03-laplacian]] (linear-algebra → linear-algebra)
- [structural-analogy] Rayleigh quotient with test vector $1$ or $1_S$ ↔ lower bounds in optimisation: any feasible test vector bounds the maximum from below. — from [[spielman-2025-sagt/ch04-adjacency]] (linear-algebra → other)
- [same-math] Lemma 6.2.1 ↔ Courant–Fischer / Rayleigh quotient: $\succcurlyeq$ on matrices passes to ordered eigenvalues. — from [[spielman-2025-sagt/ch06-comparing]] (linear-algebra → other)
- [structural-analogy] ν₂ via Rayleigh quotient ↔ Fiedler value / algebraic connectivity — a similar minimum over y ⊥ d, but with D-weighting, so not identical to λ₂ — from [[spielman-2025-sagt/ch10-random]] (linear-algebra → unspecified)
- [structural-analogy] Hoffman bound (test vector $\mathbf 1_S-s\mathbf 1$ in the Rayleigh quotient) ↔ spectral partitioning: both use indicator vectors orthogonalized against $\mathbf 1$ and Rayleigh quotients to bound combinatorial quantities. — from [[spielman-2025-sagt/ch19-independent]] (linear-algebra → linear-algebra)
- [same-math] vector-valued Rayleigh quotient (25.1) ↔ Rayleigh quotient: coordinate-wise application of the λ₂ characterization. — from [[spielman-2025-sagt/ch25-second]] (linear-algebra → other)
- [same-math] Test-vector upper bound on λ₂ ↔ linear-algebra: Rayleigh quotient of a trial vector orthogonal to $\mathbf 1$ upper-bounds $\lambda_2$ (the variational idea; not developed on these pages). — from [[spielman-2025-sagt/ch27-properties]] (linear-algebra → linear-algebra)
- [same-math] $\sigma_1=\max\|Ax\|/\|x\|$ ↔ Rayleigh quotient of $A^TA$ (variational characterization of top eigenvalue). — from [[strang-2023-introduction/ch07-singular]] (linear-algebra → unspecified)
- [same-math] Trace minimization $\min\mathrm{Tr}(H'LH)$ s.t. $H'H=I$ ↔ linear-algebra spine: Rayleigh quotient / Courant–Fischer extreme eigenvalues — same optimization, bottom-$k$ eigenvectors. — from [[vonluxburg-2007-spectralclustering/main]] (linear-algebra → linear-algebra)
