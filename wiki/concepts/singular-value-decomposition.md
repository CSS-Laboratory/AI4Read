---
id: singular-value-decomposition
type: concept
fields: [linear-algebra]
n_sources: 7
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch07-operators-p3, axler-2024-ladr/ch09-multilinear-p2, deerwester-1990-lsa/main, eckart-1936-lowrank/main, spielman-2025-sagt/ch02-eigenvalues, spielman-2025-sagt/ch04-adjacency, strang-2023-introduction/ch07-singular]
raw_ids: [singular value decomposition]
generated_by: build_kg.py
---

# singular-value-decomposition

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch07-operators-p3]] (pp. 273–274): $Tv=\sum s_k\langle v,e_k\rangle f_k$ with orthonormal lists in $V$ and $W$ (7.70); gives a diagonal matrix in suitable orthonormal bases
  - also: $A=BDC^*$ with $B,C$ having orthonormal columns and $D$ positive diagonal (7.80); the author's form uses $m$ = rank, not full size
- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 362): here only singular values are used: $|\det T|$ is their product [as `singular value decomposition`]
- [[deerwester-1990-lsa/main]] (pdf 12–13): $X=T_0S_0D_0'$ with orthonormal $T_0$, $D_0$ and positive diagonal $S_0$ in decreasing order
- [[eckart-1936-lowrank/main]] (p. 213): the paper's "canonic resolution" $\alpha=u'\lambda U$; the multipliers are what the canon calls singular values (canon link; not stated in this unit)
- [[spielman-2025-sagt/ch02-eigenvalues]] (p. 27): $A=U\Sigma V^T$, $\sigma_i\ge0$
- [[spielman-2025-sagt/ch04-adjacency]] (p. 41): singular values of $B$ give the spectrum of a bipartite $M$
- [[strang-2023-introduction/ch07-singular]] (p. 287): $A=U\Sigma V^T$ with orthonormal $U,V$ and $\sigma_1\ge\dots\ge\sigma_r>0$; works for every $m\times n$ matrix
