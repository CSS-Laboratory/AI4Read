---
id: normal-equations
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/ch12-least, strang-2023-introduction/ch04-orthogonality-p1]
generated_by: build_kg.py
---

# normal-equations

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch12-least]] (p. 229): $A^TA\hat x=A^Tb$, from setting $\nabla f=2A^T(Ax-b)$ to zero [new]
- [[strang-2023-introduction/ch04-orthogonality-p1]] (p. 155): AᵀAx̂ = Aᵀb, meaning Aᵀ(b − Ax̂) = 0 [new]

## Candidate bridges

- [same-math] Minimizing $\|v-u\|$ over $u\in U$ via $P_U$ ↔ statistics: least-squares fit — the same projection onto a subspace (normal equations are not in this unit). — from [[axler-2024-ladr/ch06-inner-p2]] (linear-algebra → other:statistics)
- [same-math] Linear least squares fit (3.7) ↔ statistics: ordinary least squares normal equations $\sum\phi\phi'\,r=\sum\phi\beta$. — from [[bertsekas-2026-rlcourse/ch03-learning-p1]] (control-theory → other:statistics)
- [same-math] condition $2Df(\hat x)^Tf(\hat x)=0$ ↔ least squares normal equations — the condition reduces to $A^T(Ax-b)=0$ when $f(x)=Ax-b$, since then $Df=A$ (our step; the text does not state this). — from [[boyd-2018-vmls/app-appendices]] (linear-algebra → unspecified)
- [same-math] pseudo-inverse $(A^TA)^{-1}A^T$ ↔ least squares: the normal-equations matrix (canon: least squares; the text defers the interpretation to later chapters) — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → linear-algebra)
- [structural-analogy] Normal equations, $\hat r\perp$ columns ↔ projection: $A\hat x$ is the closest point in the column space (the text uses the word "closest", not "projection", in the chapter; exercise 12.8 names it). — from [[boyd-2018-vmls/ch12-least]] (linear-algebra → linear-algebra)
- [structural-analogy] Normal equations in row form (12.8) ↔ sequential updating of Gram sums (exercise 12.14 builds on it). — from [[boyd-2018-vmls/ch12-least]] (linear-algebra → unspecified)
- [same-math] ŷᵈ = Aθ̂ as a projection ↔ linear-algebra: projection of yᵈ onto the column space of A (P = A(AᵀA)⁻¹Aᵀ) — the same normal-equation solution. — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → linear-algebra)
- [same-math] $x=(A^\top A)^{-1}A^\top b$ ↔ least squares: normal equations $A^\top Ax=A^\top b$ — same equation, which the unit equates with the minimum-norm least-squares solution. — from [[deisenroth-2020-mml/ch02-linear-p1]] (linear-algebra → linear-algebra)
- [same-math] Normal equation $B^\top B\lambda=B^\top x$ ↔ linear regression (Ch. 9, as stated in the unit): the least-squares fit is a projection of the target onto the column space (p. 88). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other:statistics)
- [structural-analogy] Pseudo-inverse step (6.90) ↔ linear-algebra: least-squares normal equations $A^\top Ax=A^\top y$ — the same expression, used here to invert a Gaussian mean map. — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] ML normal equations $\Phi^\top\Phi\theta=\Phi^\top y$ ↔ linear algebra: least-squares solution of an overdetermined $A x\approx b$ — identical equations. — from [[deisenroth-2020-mml/ch09-linear]] (linear-algebra → linear-algebra)
- [same-math] normal equations AᵀAx̂ = Aᵀb ↔ statistics/regression: ordinary least squares estimator (Problems 13–14 on p. 173–174 call x̂ unbiased and give its covariance σ²(AᵀA)⁻¹) — from [[strang-2023-introduction/ch04-orthogonality-p1]] (linear-algebra → other:statistics)
- [same-math] Forming $AA^T$ squares $\sigma_1/\sigma_r$ ↔ numerical analysis: squaring the condition number when solving via normal equations. — from [[strang-2023-introduction/ch07-singular]] (linear-algebra → other:numerical-analysis)
