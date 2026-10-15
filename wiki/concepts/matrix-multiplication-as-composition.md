---
id: matrix-multiplication-as-composition
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 11
n_works: 4
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p1, axler-2024-ladr/ch03-linear-p2, axler-2024-ladr/ch09-multilinear-p2, boyd-2018-vmls/app-appendices, boyd-2018-vmls/ch09-linear, boyd-2018-vmls/ch10-matrix, deisenroth-2020-mml/ch02-linear-p2, strang-2023-introduction/app10-computer, strang-2023-introduction/ch08-linear, strang-2023-introduction/ch09-linear, strang-2023-introduction/ch10-learning]
raw_ids: [matrix multiplication as composition]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# matrix-multiplication-as-composition

## Canon spine entry

- **matrix multiplication as composition** (linear-algebra): AB means "do B, then A" (HS)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p1]] (p. 55): here the product $ST$ of linear maps means "do $T$, then $S$"; no matrices yet [as `matrix multiplication as composition`]
- [[axler-2024-ladr/ch03-linear-p2]] (pp. 72–74): product defined by $(AB)_{j,k}=\sum_rA_{j,r}B_{r,k}$ so that M(ST)=M(S)M(T) [as `matrix multiplication as composition`]
- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 357): $\det(ST)=\det S\det T$ [as `matrix multiplication as composition`]
- [[boyd-2018-vmls/app-appendices]] (p. 447): the matrix chain rule uses matrix products for composed functions [as `matrix multiplication as composition`]
- [[boyd-2018-vmls/ch09-linear]] (p. 163): implicitly: iterating the update applies $A$ repeatedly [as `matrix multiplication as composition`]
- [[boyd-2018-vmls/ch10-matrix]] (p. 183): AB is the matrix of "apply B, then A"; $h(x)=A(Bx)=(AB)x$ [as `matrix multiplication as composition`]
- [[deisenroth-2020-mml/ch02-linear-p2]] (p. 56): $A_{\Psi\circ\Phi}=A_\Psi A_\Phi$
- [[strang-2023-introduction/app10-computer]] (pp. 414–415): order of products is order of operations [as `matrix multiplication as composition`]
- [[strang-2023-introduction/ch08-linear]] (p. 321): AB represents TS when A's input basis equals B's output basis
- [[strang-2023-introduction/ch09-linear]] (p. 347): the layered chain gives a product of L Jacobians
- [[strang-2023-introduction/ch10-learning]] (p. 379): here: a chain of linear F_k would collapse to one matrix A₃A₂A₁; with ReLU it does not [as `matrix multiplication as composition`]

## Candidate bridges

- [same-math] Matrix of $ST$ equals $\mathcal M(S)\mathcal M(T)$ (used in 5.74, 5.81) ↔ matrix multiplication as composition. — from [[axler-2024-ladr/ch05-eigenvalues-p2]] (linear-algebra → unspecified)
- [same-math] chain rule $Df=Dg\,Dh$ ↔ linear-algebra: matrix multiplication as composition — the Jacobian of a composition is the product of Jacobians. — from [[boyd-2018-vmls/app-appendices]] (linear-algebra → linear-algebra)
- [structural-analogy] Chain rule as product of Jacobians ↔ matrix multiplication as composition: neighbouring dimensions must match (p. 148). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → linear-algebra)
- [same-math] Chain-rule product of Jacobians ↔ linear-algebra: matrix multiplication as composition — each ∂F_k/∂F_{k−1} is a matrix and the whole is their product. — from [[strang-2023-introduction/ch09-linear]] (linear-algebra → linear-algebra)
