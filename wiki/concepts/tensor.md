---
id: tensor
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch05-vector, strang-2023-introduction/ch09-linear]
generated_by: build_kg.py
---

# tensor

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch05-vector]] (p. 155): multidimensional array; gradients of matrices are tensors [new]
- [[strang-2023-introduction/ch09-linear]] (p. 351): a derivative with three indices, e.g. T_ijk = v_kδ_ij; not a trivial extension of a matrix [new]

## Instances that use it

- [[tensor-of-two-column-vectors]] — $v\otimes w\leftrightarrow(v_jw_k)$ — from [[axler-2024-ladr/ch09-multilinear-p2]]
- [[color-image-tensor]] — R, G, B slices as a 3-way tensor — from [[strang-2023-introduction/app1-ranks]]
- [[joint-probability-tensor]] — $p_{ijk}$ for age, height, weight — from [[strang-2023-introduction/app1-ranks]]

## Candidate bridges

- [structural-analogy] $J_F$ transforming as $A^\top J_FA$ ↔ differential geometry: Riemannian metric tensor (p. 40). — from [[polyanskiy-2025-information/ch03-divergence]] (information-theory → other:mathematics)
- [structural-analogy] CP tensor decomposition ↔ data science: low-rank matrix factorization, extended to three indices without orthogonality. — from [[strang-2023-introduction/app1-ranks]] (linear-algebra → other:statistics)
