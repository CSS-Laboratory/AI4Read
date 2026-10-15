---
id: singular-value-decomposition
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra, llm]
n_sources: 12
n_works: 6
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch07-operators-p3, axler-2024-ladr/ch09-multilinear-p2, deerwester-1990-lsa/main, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch10-dimensionality, eckart-1936-lowrank/main, spielman-2025-sagt/ch02-eigenvalues, spielman-2025-sagt/ch04-adjacency, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch05-determinants, strang-2023-introduction/ch07-singular, strang-2023-introduction/ch08-linear]
aliases: [singular-value-decomposition-svd]
raw_ids: [singular value decomposition]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# singular-value-decomposition

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `singular-value-decomposition-svd` — 5 digest(s)

## Canon spine entry

- **singular value decomposition (SVD)** (linear-algebra): A = UΣVᵀ; every matrix is rotate, then scale, then rotate (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch07-operators-p3]] (pp. 273–274): $Tv=\sum s_k\langle v,e_k\rangle f_k$ with orthonormal lists in $V$ and $W$ (7.70); gives a diagonal matrix in suitable orthonormal bases
  - also: $A=BDC^*$ with $B,C$ having orthonormal columns and $D$ positive diagonal (7.80); the author's form uses $m$ = rank, not full size
- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 362): here only singular values are used: $|\det T|$ is their product [as `singular value decomposition`]
- [[deerwester-1990-lsa/main]] (pdf 12–13): $X=T_0S_0D_0'$ with orthonormal $T_0$, $D_0$ and positive diagonal $S_0$ in decreasing order [work fields: linear-algebra, llm]
- [[deisenroth-2020-mml/ch04-matrix-p2]] (p. 119): $A=U\Sigma V^\top$ for any real $m\times n$ matrix, with $U,V$ orthogonal and $\Sigma$ diagonal, non-negative [as `singular value decomposition (SVD)`; alias `singular-value-decomposition-svd`]
- [[deisenroth-2020-mml/ch10-dimensionality]] (p. 333): $X=U\Sigma V^\top$; columns of $U$ are principal directions, $\lambda_d=\sigma_d^2/N$ [as `singular value decomposition (SVD)`; alias `singular-value-decomposition-svd`]
- [[eckart-1936-lowrank/main]] (p. 213): the paper's "canonic resolution" $\alpha=u'\lambda U$; the multipliers are what the canon calls singular values (canon link; not stated in this unit) [weak: not really used in this unit]
- [[spielman-2025-sagt/ch02-eigenvalues]] (p. 27): $A=U\Sigma V^T$, $\sigma_i\ge0$
- [[spielman-2025-sagt/ch04-adjacency]] (p. 41): singular values of $B$ give the spectrum of a bipartite $M$
- [[strang-2023-introduction/app1-ranks]] (p. 402): A = UΣVᵀ as a sum of r rank-one matrices [as `singular value decomposition (SVD)`; alias `singular-value-decomposition-svd`]
- [[strang-2023-introduction/ch05-determinants]] (p. 213): E = UΣVᵀ; |det E| = |det Σ| [as `singular value decomposition (SVD)`; alias `singular-value-decomposition-svd`]
- [[strang-2023-introduction/ch07-singular]] (p. 287): $A=U\Sigma V^T$ with orthonormal $U,V$ and $\sigma_1\ge\dots\ge\sigma_r>0$; works for every $m\times n$ matrix
- [[strang-2023-introduction/ch08-linear]] (p. 323): U⁻¹AV = Σ, with separate orthonormal input and output bases [alias `singular-value-decomposition-svd`]
