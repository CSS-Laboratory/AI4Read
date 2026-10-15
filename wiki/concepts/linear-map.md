---
id: linear-map
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 7
n_works: 4
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p1, axler-2024-ladr/ch04-polynomials, boyd-2018-vmls/ch02-linear, boyd-2018-vmls/ch07-matrix, boyd-2018-vmls/ch08-linear, deisenroth-2020-mml/ch02-linear-p2, strang-2023-introduction/ch08-linear]
aliases: [linear-map-transformation]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# linear-map

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `linear-map-transformation` — 5 digest(s)

## Canon spine entry

- **linear map / transformation** (linear-algebra): a function that preserves addition and scaling; grid lines stay parallel and evenly spaced (HS)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p1]] (p. 52): function $T:V\to W$ with additivity and homogeneity; Axler writes $Tv$ and calls $\mathcal L(V,W)$ the set of them [as `linear map / transformation`; alias `linear-map-transformation`]
- [[axler-2024-ladr/ch04-polynomials]] (pp. 130–131): appears only in the exercises (Ex. 10, 14)
- [[boyd-2018-vmls/ch02-linear]] (pp. 30–31): here a scalar-valued function satisfying superposition (2.2), equivalently homogeneity plus additivity [alias `linear-map-transformation`]
- [[boyd-2018-vmls/ch07-matrix]] (p. 129): scaling, dilation, rotation, reflection and projection written as $y=Ax$ [as `linear map / transformation`; alias `linear-map-transformation`]
- [[boyd-2018-vmls/ch08-linear]] (pp. 147–148): a function satisfying superposition (8.1); always of the form $x\mapsto Ax$ [alias `linear-map-transformation`]
- [[deisenroth-2020-mml/ch02-linear-p2]] (p. 48): $\Phi(\lambda x+\psi y)=\lambda\Phi(x)+\psi\Phi(y)$
- [[strang-2023-introduction/ch08-linear]] (p. 309): a rule T with T(cv + dw) = cT(v) + dT(w); here V and W may be matrix or function spaces [alias `linear-map-transformation`]

## Instances that use it

- [[noncommuting-linear-maps-td-dt]] — $TD\neq DT$ — from [[axler-2024-ladr/ch03-linear-p1]]
- [[ellipsoid-volume-via-linear-map]] — Exercise 17 asks for the volume of an ellipsoid via a set $\Omega$ and an operator $T$ with $T(\Omega)$ equal to the ellipsoid — from [[axler-2024-ladr/ch09-multilinear-p2]]
- [[gradient-of-linear-map]] — $\mathbf f=\mathbf A\mathbf x$ has Jacobian $\mathbf A$ — from [[deisenroth-2020-mml/ch05-vector]]
- [[linear-map-of-standard-gaussian]] — Example 6.17: density of $Y=AX$, covariance $AA^\top$ — from [[deisenroth-2020-mml/ch06-probability-p2]]
- [[derivative-as-linear-map]] — d/dx on polynomials has matrix [[0,1,0],[0,0,2]], a kernel of constants, and the integral as pseudoinverse — from [[strang-2023-introduction/ch08-linear]]

## Candidate bridges

- [same-math] Fundamental theorem of linear maps ↔ linear-algebra spine: rank–nullity $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$ — same statement, stated without matrices. — from [[axler-2024-ladr/ch03-linear-p1]] (linear-algebra → linear-algebra)
- [metaphor] Domain basis change, scaling, codomain basis change ↔ "rotate, stretch, rotate" as a general picture of any linear map. — from [[deisenroth-2020-mml/ch04-matrix-p2]] (linear-algebra → unspecified)
- [same-math] Jacobian of a linear map ↔ linear-algebra: matrix of a linear map. $\mathbf f=\mathbf A\mathbf x$ has Jacobian $\mathbf A$, and the basis-change matrix equals the Jacobian (pp. 151–153). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → linear-algebra)
- [same-math] $\boldsymbol A\boldsymbol\Sigma\boldsymbol A^\top$ (6.51) ↔ linear-algebra: how a linear map transforms a quadratic form / covariance of linearly mapped data. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [same-math] Tent map (35) ↔ one-dimensional chaotic maps: the doubling of $\epsilon$ is the same iterated piecewise-linear map. — from [[lorenz-1963-nonperiodic/main]] (complex-systems → other:one-dimensional-chaotic-maps)
