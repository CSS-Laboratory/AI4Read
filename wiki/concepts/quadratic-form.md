---
id: quadratic-form
type: concept
fields: [linear-algebra]
n_sources: 7
tiers: [deep, core]
grounding: digests
sources: [axler-2024-ladr/ch09-multilinear-p1, spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch03-laplacian, spielman-2025-sagt/ch12-effective, spielman-2025-sagt/ch17-monotonicity, strang-2023-introduction/ch06-eigenvalues-p2, strang-2023-introduction/ch09-linear]
raw_ids: [quadratic form]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# quadratic-form

## Canon spine entry

- **quadratic form** (linear-algebra): xᵀSx; its level sets are ellipsoids whose axes are eigenvectors (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch09-multilinear-p1]] (p. 341): here $q(v)=\beta(v,v)$ for some bilinear $\beta$, defined on any $V$ (the canon's $x^{\mathsf T}Sx$ is the $\mathbf F^n$ case via 9.20 and a symmetric matrix)
- [[spielman-2025-sagt/ch01-introduction]] (p. 3): the function $x\mapsto x^TMx$, used here as the second way to use a matrix
- [[spielman-2025-sagt/ch03-laplacian]] (p. 29): $x^TLx$ as a sum of weighted squared edge differences [as `quadratic form`]
- [[spielman-2025-sagt/ch12-effective]] (p. 117): energy $v^TLv$, preserved by the Schur complement on harmonic extensions [as `quadratic form`]
- [[spielman-2025-sagt/ch17-monotonicity]] (p. 149): energy $v^TLv$
- [[strang-2023-introduction/ch06-eigenvalues-p2]] (p. 254): xᵀSx; level set xᵀSx = 1 is an ellipse with axes along eigenvectors
- [[strang-2023-introduction/ch09-linear]] (p. 335, 339): F = ½xᵀSx − bᵀx; gradient Sx − b, minimizer S⁻¹b

## Instances that use it

- [[quadratic-form-r3-example]] — $x_1^2-4x_1x_2+8x_1x_3-3x_3^2$ and its symmetric bilinear form — from [[axler-2024-ladr/ch09-multilinear-p1]]

## Candidate bridges

- [same-math] quadratic form $q(v)=\beta(v,v)$ on $\mathbf R^n$ with symmetric matrix ↔ canon "quadratic form $x^{\mathsf T}Sx$": the same function, shown diagonalisable by an orthonormal basis (9.23b). — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → other)
- [same-math] Dirichlet energy $\|A^Tv\|^2$ ↔ graph Laplacian: the unit itself calls it the Laplacian quadratic form of the graph. — from [[boyd-2018-vmls/ch07-matrix]] (linear-algebra → other)
- [same-math] Dirichlet energy $\|A^Tx\|^2$ (incidence matrix) ↔ linear-algebra canon: graph Laplacian quadratic form $\sum(x_i-x_j)^2$ — both are $x^T(AA^T)x$ for the incidence matrix $A$. — from [[boyd-2018-vmls/ch15-multi]] (linear-algebra → linear-algebra)
- [same-math] Hessian symmetry and $\boldsymbol\delta^\top\mathbf H\boldsymbol\delta$ ↔ quadratic forms and symmetric matrices (canon link; not stated in this unit). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → unspecified)
- [same-math] $\boldsymbol A\boldsymbol\Sigma\boldsymbol A^\top$ (6.51) ↔ linear-algebra: how a linear map transforms a quadratic form / covariance of linearly mapped data. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [same-math] $y=Ax$ gives covariance $A\Sigma A^\top$ ↔ linear-algebra: congruence/quadratic form $A\Sigma A^\top$ of a positive semi-definite matrix. — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] QP dual via $x=-Q^{-1}(c+A^\top\lambda)$ ↔ linear-algebra: solving a positive-definite linear system from a quadratic form. — from [[deisenroth-2020-mml/ch07-continuous]] (linear-algebra → linear-algebra)
- [structural-analogy] Laplacian quadratic form ↔ smoothness penalty in machine learning (the author mentions ML classification only as a Laplacian-solver application). — from [[spielman-2025-sagt/ch01-introduction]] (linear-algebra → unspecified)
- [structural-analogy] Hall's constraints ($\|x\|=1$, $\mathbf 1^Tx=0$, $x\perp y$) ↔ PCA: centred, orthonormal directions — both choose orthonormal vectors extremizing a quadratic form. — from [[spielman-2025-sagt/ch03-laplacian]] (linear-algebra → linear-algebra)
- [structural-analogy] Dominating a multiple of $K_n$ ↔ condition numbers: $c$-approximation bounds the ratio of quadratic forms, as relative bounds on a matrix pair. — from [[spielman-2025-sagt/ch06-comparing]] (linear-algebra → other)
- [same-math] Spring energy $\mathcal E(x)$ ↔ Laplacian quadratic form: (11.4) is a sum over edges of $w_{a,b}(x(a)-x(b))^2$ (the identification with $x^TLx$ is not stated in this unit). — from [[spielman-2025-sagt/ch11-walks]] (linear-algebra → other)
- [same-math] effective resistance $i^TL^+i$ ↔ linear algebra: pseudoinverse solving $Lv=b$ — the same quadratic form. — from [[spielman-2025-sagt/ch17-monotonicity]] (linear-algebra → linear-algebra)
- [same-math] Linear case $\Phi=\tfrac12v^2/r$ ↔ graph Laplacian: quadratic form $\sum(x(a)-x(b))^2$ (the source calls it the Lecture 13 energy). — from [[spielman-2025-sagt/ch18-dynamic]] (linear-algebra → other)
- [metaphor] Counting negative eigenvalues of a signed-weight Laplacian ↔ counting "unstable directions" of a quadratic form — from [[spielman-2025-sagt/ch24-nodal]] (linear-algebra → unspecified)
- [same-math] V_Z = A V_X Aᵀ ↔ linear algebra: Aᵀ-congruence acting on a symmetric (quadratic-form) matrix; the case K = 1 is cᵀVc ≥ 0 (p. 397) — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → linear-algebra)
