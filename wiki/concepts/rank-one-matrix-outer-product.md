---
id: rank-one-matrix-outer-product
type: concept
fields: [linear-algebra]
n_sources: 18
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch09-multilinear-p2, boyd-2018-vmls/ch10-matrix, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch05-vector, deisenroth-2020-mml/ch10-dimensionality, deisenroth-2020-mml/ch11-density, spielman-2025-sagt/ch03-laplacian, spielman-2025-sagt/ch08-eigenvalues, spielman-2025-sagt/ch33-linear, spielman-2025-sagt/ch41-expected, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch02-solving-p1, strang-2023-introduction/ch02-solving-p2, strang-2023-introduction/ch03-four-p1, strang-2023-introduction/ch03-four-p3, strang-2023-introduction/ch04-orthogonality-p1, strang-2023-introduction/ch07-singular, strang-2023-introduction/ch10-learning]
raw_ids: [rank-one matrix / outer product]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# rank-one-matrix-outer-product

## Canon spine entry

- **rank-one matrix / outer product** (linear-algebra): uvᵀ, a single column pattern times a single row pattern; the building block of low-rank structure (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 374): $v\otimes w$ identified with the matrix $(v_jw_k)$ (p. 374). Exercise 5 asks the reader to show these are exactly the matrices of rank at most one. [as `rank-one matrix / outer product`]
- [[boyd-2018-vmls/ch10-matrix]] (pp. 178, 181): $ab^T$ has entries $a_ib_j$; AB is a sum of p outer products of columns of A with rows of B [as `rank-one matrix / outer product`]
- [[deisenroth-2020-mml/ch04-matrix-p2]] (pp. 129–130): $A_i=u_iv_i^\top$; $A$ is the sum $\sum\sigma_iA_i$ [as `rank-one matrix / outer product`]
- [[deisenroth-2020-mml/ch05-vector]] (p. 166): $\boldsymbol\delta\otimes\boldsymbol\delta=\boldsymbol\delta\boldsymbol\delta^\top$; $k$-fold outer products give $k$-th order tensors [as `rank-one matrix / outer product`]
- [[deisenroth-2020-mml/ch10-dimensionality]] (p. 330): $BB^\top=\sum b_mb_m^\top$ is a sum of rank-one matrices, rank $M$ [as `rank-one matrix / outer product`]
- [[deisenroth-2020-mml/ch11-density]] (p. 356): each term $(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top$ in the covariance update is a $D\times D$ outer product
- [[spielman-2025-sagt/ch03-laplacian]] (p. 29): each edge contributes $(\delta_a-\delta_b)(\delta_a-\delta_b)^T$ [as `rank-one matrix / outer product`]
- [[spielman-2025-sagt/ch08-eigenvalues]] (p. 71): $J$ is rank one; adding it interlaces eigenvalues
- [[spielman-2025-sagt/ch33-linear]] (p. 264): edges are encoded as $v v^T$; sparsifier = weighted sum of few of them
- [[spielman-2025-sagt/ch41-expected]] (p. 329): $tvv^T$; adding it gives $\chi_x(A)-tq(x)$
- [[strang-2023-introduction/ch01-vectors]] (pp. 23, 34): column times row; all columns on one line; AB = Σ aₖbₖ*
- [[strang-2023-introduction/ch02-solving-p1]] (p. 60): column times row; A = Σ ℓ_k u_k
- [[strang-2023-introduction/ch02-solving-p2]] (p. 68): xyᵀ, an n×n matrix, versus the inner product xᵀy, a number [as `rank-one matrix / outer product`]
- [[strang-2023-introduction/ch03-four-p1]] (p. 88): A = uvᵀ has column space the line of u and row space the line of v [as `rank-one matrix / outer product`]
- [[strang-2023-introduction/ch03-four-p3]] (p. 136): uvᵀ; every rank r matrix is a sum of r of them [as `rank-one matrix / outer product`]
- [[strang-2023-introduction/ch04-orthogonality-p1]] (p. 154): aaᵀ/aᵀa is a column times a row, rank one
- [[strang-2023-introduction/ch07-singular]] (p. 286, p. 294): $A$ is a sum of $r$ pieces $\sigma_iu_iv_i^T$
- [[strang-2023-introduction/ch10-learning]] (p. 396): each V_ij = UUᵀ term [as `rank-one matrix / outer product`]

## Candidate bridges

- [same-math] $v\otimes w\leftrightarrow(v_jw_k)$ ↔ rank-one matrix / outer product $vw^{\rm t}$. — from [[axler-2024-ladr/ch09-multilinear-p2]] (linear-algebra → unspecified)
