---
id: projection
type: concept
fields: [linear-algebra, analytic-philosophy]
n_sources: 17
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch06-inner-p2, boyd-2018-vmls/ch07-matrix, boyd-2018-vmls/ch12-least, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch09-linear, deisenroth-2020-mml/ch10-dimensionality, deisenroth-2020-mml/ch12-classification, godfreysmith-2003-theory/ch03-induction, spielman-2025-sagt/ch09-strongly, spielman-2025-sagt/ch13-random, spielman-2025-sagt/ch19-independent, spielman-2025-sagt/ch32-sparsification, spielman-2025-sagt/ch33-linear, strang-2023-introduction/app10-computer, strang-2023-introduction/ch04-orthogonality-p1, strang-2023-introduction/ch04-orthogonality-p2, strang-2023-introduction/ch06-eigenvalues-p1]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# projection

## Canon spine entry

- **projection** (linear-algebra): the closest point in a subspace; P = A(AᵀA)⁻¹Aᵀ (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch06-inner-p2]] (pp. 214–217): here $P_U$, defined via $V=U\oplus U^\perp$; $P_U v$ is the closest point of $U$ to $v$
- [[boyd-2018-vmls/ch07-matrix]] (p. 130): closest point of a set (here a line through the origin) to $x$, written as a matrix
- [[boyd-2018-vmls/ch12-least]] (p. 231): $A\hat x$ is the closest point to $b$ in the span of the columns
- [[deisenroth-2020-mml/ch03-analytic]] (p. 82–87): linear $\pi$ with $\pi^2=\pi$; orthogonal case $P=B(B^\top B)^{-1}B^\top$
- [[deisenroth-2020-mml/ch09-linear]] (p. 314): $\Phi(\Phi^\top\Phi)^{-1}\Phi^\top y$ is the orthogonal projection of $y$ onto the column space of $\Phi$
- [[deisenroth-2020-mml/ch10-dimensionality]] (p. 329): $\tilde x=BB^\top x$, the optimal linear reconstruction
- [[deisenroth-2020-mml/ch12-classification]] (p. 374–375): the nearest point $\boldsymbol x_a'$ on the hyperplane is the orthogonal projection of $\boldsymbol x_a$
- [[spielman-2025-sagt/ch09-strongly]] (p. 88): $UU^T$, $WW^T$, $\frac1nJ$ are orthogonal projections
- [[spielman-2025-sagt/ch13-random]] (pp. 123, 127): here $\Pi_{a}$ and $\Gamma$ are symmetric projections
- [[spielman-2025-sagt/ch19-independent]] (p. 165): $\mathbf 1_S-s\mathbf 1$ is the projection of $\mathbf 1_S$ orthogonal to $\mathbf 1$
- [[spielman-2025-sagt/ch32-sparsification]] (p. 260): $\Pi=L_G^{+/2}L_GL_G^{+/2}$ projects onto range($L_G$)
- [[spielman-2025-sagt/ch33-linear]] (p. 265): $\Pi=\frac1nL_{K_n}$ is the projection orthogonal to constants
- [[strang-2023-introduction/app10-computer]] (p. 415): I − nnᵀ onto a plane with unit normal n
- [[strang-2023-introduction/ch04-orthogonality-p1]] (p. 151): closest point p in a subspace to b; e = b − p is orthogonal to the subspace
- [[strang-2023-introduction/ch04-orthogonality-p2]] (p. 179): with orthonormal columns $P=QQ^{\mathsf T}$, $p=Q\hat x$
- [[strang-2023-introduction/ch06-eigenvalues-p1]] (p. 219): eigenvalues only 0 and 1; keeps column space, kills nullspace

### analytic-philosophy

- [[godfreysmith-2003-theory/ch03-induction]] (p. 42): inference from observed cases to the next case [new]

## Instances that use it

- [[hart-mondale-1984-projection]] — larger projection for little-known Hart than for Mondale — from [[achen-2016-realists/ch10-it]]
- [[projection-onto-line-example]] — $b=[1,2,2]^\top$, $P_\pi=\tfrac19 bb^\top$-type matrix — from [[deisenroth-2020-mml/ch03-analytic]]
- [[projection-onto-plane-example]] — $x=[6,0,0]^\top$ projected to $[5,2,-1]^\top$, error $\sqrt6$ — from [[deisenroth-2020-mml/ch03-analytic]]
- [[fitting-line-through-origin]] — $y=\theta x+\epsilon$; $\theta_{ML}=X^\top y/X^\top X$ as a 1-D projection — from [[deisenroth-2020-mml/ch09-linear]]
- [[diagonal-gaussian-approx]] — under- vs over-confidence of M- and I-projection — from [[murphy-2023-pml2/ch05-information-p1]]
- [[projection-inequality]] — $N_1N_2N_3\ge N^2$ from Shearer's lemma — from [[polyanskiy-2025-information/ch02-entropy]]
- [[loomis-whitney]] — volume bounded by projection volumes — from [[polyanskiy-2025-information/ch09-entropy]]
- [[gaussian-two-moment-projection]] — P=N(0,1), φ=(x,x²): optimal Q=N(γ₁,γ₂−γ₁²) for γ₂>γ₁² — from [[polyanskiy-2025-information/ch17-information]]
- [[projection-onto-a-flat]] — T₋PT₊ — from [[strang-2023-introduction/app10-computer]]
- [[pulse-average-projection]] — best single value for 70, 80, 120 is the average 90 — from [[strang-2023-introduction/ch04-orthogonality-p1]]
- [[projection-eigenbasis]] — projection onto y = −x becomes diag(1,0) in an eigenvector basis — from [[strang-2023-introduction/ch08-linear]]
- [[kaczmarz-random-row]] — SGD for least squares via row projections; fast start, oscillating finish — from [[strang-2023-introduction/ch09-linear]]
- [[score-gramophone-symphony]] — shared logical structure, with projection rules between very different media — from [[wittgenstein-1922-tractatus/ch04-proposition]]

## Candidate bridges

- [structural-analogy] Persuasion and projection as reverse causation (p. 42) ↔ causal inference: endogeneity, and panel data to untangle it. — from [[achen-2016-realists/ch02-elusive]] (political-science → bayesian)
- [structural-analogy] "Reality bias / curse of knowledge" ↔ judgement under hindsight or informational asymmetry in social science — both are projection of one's own information onto another. — from [[apperly-2011-mindreaders/ch02-evidence]] (theory-of-mind → unspecified)
- [same-math] Orthogonal decomposition 6.13 ↔ projection: the coefficient $c=\langle u,v\rangle/\|v\|^2$ is the projection of $u$ onto the line spanned by $v$. — from [[axler-2024-ladr/ch06-inner-p1]] (linear-algebra → other)
- [same-math] Minimizing $\|v-u\|$ over $u\in U$ via $P_U$ ↔ statistics: least-squares fit — the same projection onto a subspace (normal equations are not in this unit). — from [[axler-2024-ladr/ch06-inner-p2]] (linear-algebra → other)
- [structural-analogy] Best polynomial approximation as projection ↔ machine learning: regression on basis functions. — from [[axler-2024-ladr/ch06-inner-p2]] (linear-algebra → other)
- [metaphor] Expansion coefficients $a_i^Tx$ ↔ projection: each coefficient measures $x$'s alignment with $a_i$ (canon link; projection is not stated in this unit). — from [[boyd-2018-vmls/ch05-linear]] (linear-algebra → other)
- [structural-analogy] Normal equations, $\hat r\perp$ columns ↔ projection: $A\hat x$ is the closest point in the column space (the text uses the word "closest", not "projection", in the chapter; exercise 12.8 names it). — from [[boyd-2018-vmls/ch12-least]] (linear-algebra → other)
- [same-math] ŷᵈ = Aθ̂ as a projection ↔ linear-algebra: projection of yᵈ onto the column space of A (P = A(AᵀA)⁻¹Aᵀ) — the same normal-equation solution. — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → linear-algebra)
- [structural-analogy] Pythagorean inequality for D ↔ Euclidean geometry: projection onto a convex set gives an obtuse angle, so $l_{AC}^2\ge l_{AB}^2+l_{BC}^2$ — stated by the author as a analogy (p. 299). — from [[cover-2006-elements/ch12-information-p2]] (information-theory → other)
- [same-math] $D_q=X_q'TS^{-1}$ ↔ linear-algebra: coordinates of the projection of a vector onto the span of the columns of $T$ (since $T'T=I$, $T'X_q$ gives the coordinates, then rescaled by $S^{-1}$). — from [[deerwester-1990-lsa/main]] (linear-algebra → linear-algebra)
- [same-math] Normal equation $B^\top B\lambda=B^\top x$ ↔ linear regression (Ch. 9, as stated in the unit): the least-squares fit is a projection of the target onto the column space (p. 88). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other)
- [structural-analogy] Projection onto an orthonormal basis $\lambda=B^\top x$ ↔ Fourier series: coordinates are inner products with orthogonal functions (p. 81, 88). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other)
- [structural-analogy] Projection onto a line ↔ cosine similarity: $\|\pi_U(x)\|=|\cos\omega|\|x\|$ links projection length to angle (p. 84). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other)
- [same-math] Gaussian conditioning (6.66)–(6.67) ↔ linear-algebra: least squares/projection, where the conditional mean is a linear regression of $x$ on $y$ with the Schur complement as residual covariance — the formulas are the same block-matrix algebra (the text itself does not state this link). — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] Least-squares ERM (8.9) ↔ linear-algebra: least squares by projecting y onto the column space of X (the book defers the closed form to Sec. 9.2 (p. 261); the projection reading is from the field list, not this unit). — from [[deisenroth-2020-mml/ch08-when]] (linear-algebra → linear-algebra)
- [same-math] ML fit $\Phi(\Phi^\top\Phi)^{-1}\Phi^\top y$ ↔ projection onto the column space; $\Phi\Phi^\top y$ for orthonormal columns. — from [[deisenroth-2020-mml/ch09-linear]] (linear-algebra → unspecified)
- [same-math] Margin distance $r$ via orthogonal projection onto the hyperplane (12.8) ↔ projection onto a subspace (Ch. 3.8 of this book) — it is literally a projection error. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → unspecified)
- [structural-analogy] TIRM's treatment projection ↔ causal inference: propensity score — a low-dimensional score for treatment likelihood used for matching — from [[grimmer-2022-textasdata/ch27-text]] (political-science → bayesian)
- [metaphor] Mind projection fallacy ↔ bayesian: probability as a state of knowledge rather than a property of the world (canon link; not stated in this unit) — from [[jaynes-2003-probability/ch01-plausible]] (information-theory → bayesian)
- [structural-analogy] Orthogonal-projection estimate ↔ statistics: least-squares regression as projection onto a span — both minimize squared error by making the residual orthogonal to the regressors. — from [[kalman-1960-filtering/main]] (control-theory → other)
- [same-math] Reverse-KL/I-projection ↔ variational inference in Bayesian inference (canon: KL divergence & ELBO; not developed in this unit): the KL being minimized is $D_{KL}(q\|p)$. — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → bayesian)
- [structural-analogy] ADF moment projection ↔ expectation propagation: EP iterates ADF-style projections with past and future factors. — from [[murphy-2023-pml2/ch08-gaussian-p2]] (bayesian → other)
- [structural-analogy] Dual Pythagorean identity (Theorem 6) ↔ information-theory: Pythagorean-type identities for projections — same shape (projection as divergence minimization, Thm 7), not derived here — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [structural-analogy] Text as a low-dimensional projection of thought ↔ dynamical systems: Packard/Takens delay-embedding reconstruction — both recover hidden structure from a limited view; the paper itself says "analogy". — from [[piantadosi-2022-meaning/main]] (llm → complex-systems)
- [structural-analogy] Pythagorean inequality for KL ↔ Euclidean projection onto a convex set: D behaves like (is similar to) squared distance, with obtuse/right triangles (p. 303). — from [[polyanskiy-2025-information/ch17-information]] (information-theory → other)
- [structural-analogy] I-projection with P uniform ↔ maximum entropy principle: the author notes this link (p. 308). — from [[polyanskiy-2025-information/ch17-information]] (information-theory → other)
- [same-math] E1*(E0) = min_{D(Q′‖P) ≤ E0} D(Q′‖Q) ↔ large deviations: Sanov-type I-projection onto a KL ball. — from [[polyanskiy-2025-information/ch18-hypothesis]] (information-theory → other)
- [structural-analogy] Edge leverage $\ell_e=\Gamma(e,e)$, diagonal of a projection ↔ statistics: hat-matrix leverage in regression. Both are diagonal entries of a projection matrix. — from [[spielman-2025-sagt/ch13-random]] (linear-algebra → other)
- [metaphor] Product of projections-with-damping ↔ probability: each "bad" visit multiplies by at most $1/5$, like independent trials. — from [[spielman-2025-sagt/ch31-psrgs]] (linear-algebra → other)
- [same-math] projection onto a flat, "v₀ + nullspace" ↔ solutions of Av = b — the author says a flat is like the solutions of Av = b: one particular solution added to the nullspace (p. 416). — from [[strang-2023-introduction/app10-computer]] (linear-algebra → unspecified)
- [structural-analogy] Projected Bellman operator iteration ↔ control-theory/state-space: projection to representable subspace then dynamics step, fixed point as equilibrium — from [[sutton-2018-rl/ch11-off]] (control-theory → control-theory)
- [metaphor] Projection in geometry ↔ translation between languages: invariants survive any projection (p. 9). — from [[wittgenstein-1922-tractatus/ch00-introduction]] (analytic-philosophy → other)
