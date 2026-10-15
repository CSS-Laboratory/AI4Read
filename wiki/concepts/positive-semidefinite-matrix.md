---
id: positive-semidefinite-matrix
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 24
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch07-operators-p2, axler-2024-ladr/ch07-operators-p3, axler-2024-ladr/ch09-multilinear-p2, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch04-matrix-p1, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch06-probability-p2, deisenroth-2020-mml/ch07-continuous, deisenroth-2020-mml/ch09-linear, deisenroth-2020-mml/ch12-classification, spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch06-comparing, spielman-2025-sagt/ch11-walks, spielman-2025-sagt/ch12-effective, spielman-2025-sagt/ch24-nodal, spielman-2025-sagt/ch32-sparsification, spielman-2025-sagt/ch36-preconditioning, spielman-2025-sagt/ch38-fast, strang-2023-introduction/ch02-solving-p2, strang-2023-introduction/ch06-eigenvalues-p2, strang-2023-introduction/ch06-eigenvalues-p3, strang-2023-introduction/ch09-linear, strang-2023-introduction/ch10-learning, vonluxburg-2007-spectralclustering/main]
aliases: [positive-definite-matrix]
raw_ids: [positive (semi)definite matrix]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# positive-semidefinite-matrix

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `positive-definite-matrix` — 1 digest(s)

## Canon spine entry

- **positive (semi)definite matrix** (linear-algebra): xᵀSx ≥ 0; covariance matrices, Gram matrices, and Laplacians are all of this kind (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch07-operators-p2]] (pp. 251, 266): Axler's "positive operator": self-adjoint with $\langle Tv,v\rangle\ge0$; "positive definite" (matrix) needs $>0$ for $x\neq0$ [as `positive (semi)definite matrix`]
- [[axler-2024-ladr/ch07-operators-p3]] (p. 270): here "positive operator" ($\langle Tv,v\rangle\ge0$, self-adjoint); $T^*T$ is always one
- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 362): positive operators have $\det\ge0$ [as `positive (semi)definite matrix`]
- [[deisenroth-2020-mml/ch03-analytic]] (p. 74): symmetric $A$ with $x^\top Ax>0$ ($\ge0$) for $x\ne0$; matches inner products in a basis [as `positive (semi)definite matrix`]
- [[deisenroth-2020-mml/ch04-matrix-p1]] (p. 111): $A^\top A$ is always symmetric PSD, and PD if $\operatorname{rk}A=n$ [as `positive (semi)definite matrix`]
- [[deisenroth-2020-mml/ch04-matrix-p2]] (p. 123): $A^\top A$ is symmetric PSD, so $\lambda_i\ge0$ [as `positive (semi)definite matrix`]
- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 204): here: $A^\top A$ is symmetric positive definite for full-rank $A$; covariance matrices are symmetric positive definite
- [[deisenroth-2020-mml/ch07-continuous]] (pp. 237, 241): Hessian psd iff $f$ convex; $Q$ pd in QPs [as `positive (semi)definite matrix`]
- [[deisenroth-2020-mml/ch09-linear]] (pp. 294, 302): $X^\top X$ is positive definite if $\mathrm{rk}(X)=D$. $\Phi^\top\Phi+\frac{\sigma^2}{b^2}I$ is strictly positive definite [as `positive (semi)definite matrix`]
- [[deisenroth-2020-mml/ch12-classification]] (p. 389): kernel (Gram) matrices satisfy $\boldsymbol z^\top\boldsymbol K\boldsymbol z\ge0$
- [[spielman-2025-sagt/ch01-introduction]] (p. 6): symmetric with nonnegative eigenvalues
- [[spielman-2025-sagt/ch06-comparing]] (p. 53): symmetric, with $v^TAv\ge0$ for all $v$, equivalently nonnegative eigenvalues
- [[spielman-2025-sagt/ch11-walks]] (pp. 105–106): here $L(S,S)$, $L+X$ are positive definite under stated conditions
- [[spielman-2025-sagt/ch12-effective]] (p. 112): used to define $M^{1/2}$ by the spectral decomposition [as `positive (semi)definite matrix`]
- [[spielman-2025-sagt/ch24-nodal]] (p. 198): $x^TAx\ge0$; preserved by $B^TAB$
- [[spielman-2025-sagt/ch32-sparsification]] (p. 259): hypothesis on the summands in Thm 32.3.1
- [[spielman-2025-sagt/ch36-preconditioning]] (p. 287): $A,B$ must be PSD; $\preceq$ is the order "difference is PSD"
- [[spielman-2025-sagt/ch38-fast]] (p. 300): the order $X\succeq Y$ means $X-Y$ is PSD; used to define $\approx_\epsilon$ [as `positive (semi)definite matrix`]
- [[strang-2023-introduction/ch02-solving-p2]] (p. 79): n positive (nonnegative) pivots; K, T positive definite, B semidefinite [as `positive (semi)definite matrix`]
- [[strang-2023-introduction/ch06-eigenvalues-p2]] (p. 247–250): S = Sᵀ with xᵀSx > 0 (definite) or ≥ 0 (semidefinite); five tests
- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 263): ĀᵀA and AĀᵀ have real eigenvalues ≥ 0
- [[strang-2023-introduction/ch09-linear]] (p. 335–336): here S(x) positive definite everywhere makes F convex; the model bowl has S symmetric positive definite [alias `positive-definite-matrix`]
- [[strang-2023-introduction/ch10-learning]] (pp. 396–397): V is semidefinite by cᵀVc ≥ 0, and by being a sum of rank-one terms [as `positive (semi)definite matrix`]
- [[vonluxburg-2007-spectralclustering/main]] (pp. 4–6): $L,L_{\rm sym},L_{\rm rw}$ all PSD, from the quadratic forms

## Candidate bridges

- [same-math] Cholesky sampling $\Sigma=AA^\top$ ↔ linear-algebra: Cholesky factorization of a symmetric positive definite matrix. — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
