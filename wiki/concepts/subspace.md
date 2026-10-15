---
id: subspace
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch01-vector, strang-2023-introduction/ch03-four-p1]
generated_by: build_kg.py
---

# subspace

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch01-vector]] (p. 18): subset that is itself a vector space under the same operations; test: $0$, closure under $+$ and scalar multiplication [new]
- [[strang-2023-introduction/ch03-four-p1]] (p. 86): a vector space inside another: contains 0, closed under v + w and cv [new]

## Instances that use it

- [[instance-subspace-examples-135]] — continuous, differentiable and null-limit sequences as subspaces — from [[axler-2024-ladr/ch01-vector]]
- [[instance-nondirect-sum-144]] — three subspaces of $\mathbf{F}^3$ with pairwise trivial intersection but non-unique decomposition of $0$ — from [[axler-2024-ladr/ch01-vector]]
- [[non-subspace-gallery]] — Figure 2.6, four subsets of R², of which only D is a subspace — from [[deisenroth-2020-mml/ch02-linear-p1]]
- [[example-lines-planes-hyperplanes]] — Example 2.26: affine subspaces by parametric equation — from [[deisenroth-2020-mml/ch02-linear-p2]]
- [[mnist-0-1-pca-embedding]] — a 2-D principal subspace roughly separates "0" and "1"; "0"s vary more — from [[deisenroth-2020-mml/ch10-dimensionality]]
- [[mfa-ard-dimension-recovery]] — ARD recovers six subspaces of dimension 1,2,2,3,4,7 as sample size grows — from [[murphy-2023-pml2/ch28-latent-p1]]
- [[quarter-plane-not-subspace]] — fails scaling by −1 — from [[strang-2023-introduction/ch03-four-p1]]
- [[two-quarter-planes-not-subspace]] — satisfies scaling but fails addition — from [[strang-2023-introduction/ch03-four-p1]]
- [[upper-triangular-and-diagonal-subspaces]] — subspaces U ⊃ D of the 2 by 2 matrices — from [[strang-2023-introduction/ch03-four-p1]]
- [[wall-and-floor-not-orthogonal]] — two 2-dim subspaces of R³ cannot be orthogonal since 2+2 > 3 — from [[strang-2023-introduction/ch04-orthogonality-p1]]

## Candidate bridges

- [structural-analogy] Sum of subspaces = smallest containing subspace ↔ span (canon link; not stated in this unit): both are "everything reachable by adding". — from [[axler-2024-ladr/ch01-vector]] (linear-algebra → linear-algebra)
- [structural-analogy] Subspace/sum/direct sum ↔ subset/union/disjoint union (the author's own analogy, p. 21, 24). — from [[axler-2024-ladr/ch01-vector]] (linear-algebra → unspecified)
- [structural-analogy] V/U (collapsing a subspace to zero) ↔ linear-algebra: null space of a map. T̃ identifies V/(null T) with range T, a "first isomorphism" pattern. — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → linear-algebra)
- [same-math] $v,Tv,T^2v,\dots$ dependent ⇒ polynomial kills $v$ ↔ Krylov subspaces: the span of $v,Tv,\dots,T^{k-1}v$ (Ex. 5B.23 says this span is invariant when $k=\dim V$). — from [[axler-2024-ladr/ch05-eigenvalues-p1]] (linear-algebra → other:krylov-subspaces)
- [same-math] Minimizing $\|v-u\|$ over $u\in U$ via $P_U$ ↔ statistics: least-squares fit — the same projection onto a subspace (normal equations are not in this unit). — from [[axler-2024-ladr/ch06-inner-p2]] (linear-algebra → other:statistics)
- [same-math] adjoint $T^*$ with real entries = transpose ↔ the transpose in $\operatorname{null}(A^{\mathrm t})=(\operatorname{col}A)^\perp$ (four fundamental subspaces): 7.6 over $\mathbf R$ with orthonormal bases. — from [[axler-2024-ladr/ch07-operators-p1]] (linear-algebra → other:the-transpose-in-operatornamenullamathrm)
- [structural-analogy] "closure under operations" for subspaces ↔ group closure: both ask whether operations stay inside the set. — from [[deisenroth-2020-mml/ch02-linear-p1]] (linear-algebra → other:group-closure)
- [structural-analogy] Affine subspace $x_0+U$ ↔ data analysis: mean-centred data plus a subspace (PCA, Chapter 10; the link is not discussed in these pages) — an offset plus a linear directions space. — from [[deisenroth-2020-mml/ch02-linear-p2]] (linear-algebra → other:statistics)
- [same-math] Margin distance $r$ via orthogonal projection onto the hyperplane (12.8) ↔ projection onto a subspace (Ch. 3.8 of this book) — it is literally a projection error. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → unspecified)
- [structural-analogy] Linear autoencoder ↔ PCA: both recover the top principal subspace under MSE. — from [[murphy-2023-pml2/ch32-representation]] (bayesian → linear-algebra)
- [structural-analogy] Courant-Fischer max-min over subspaces ↔ Eckart–Young / best low-rank approximation: both rank directions by singular or eigen values. — from [[spielman-2025-sagt/ch02-eigenvalues]] (linear-algebra → other:eckart-young-best-low)
- [same-math] Davis–Kahan angle bound ↔ linear-algebra: perturbation of invariant subspaces under symmetric noise — the theorem is the same statement. — from [[spielman-2025-sagt/ch23-spectral]] (linear-algebra → linear-algebra)
- [structural-analogy] CG's A-orthogonal basis ↔ linear-algebra: Lanczos-type bases for Krylov subspaces — both build a basis of a Krylov subspace by a short recurrence. — from [[spielman-2025-sagt/ch35-conjugate]] (linear-algebra → linear-algebra)
- [structural-analogy] Projected Bellman operator iteration ↔ control-theory/state-space: projection to representable subspace then dynamics step, fixed point as equilibrium — from [[sutton-2018-rl/ch11-off]] (control-theory → control-theory)
