---
id: inner-product
type: concept
fields: [linear-algebra, political-science]
fields_strong: [linear-algebra, political-science]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch06-inner-p1, grimmer-2022-textasdata/ch07-vector]
generated_by: build_kg.py
---

# inner-product

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch06-inner-p1]] (p. 182): $\langle u,v\rangle$ obeying the five axioms of 6.2; first-slot linear, conjugate symmetric (p. 183). Generalizes the dot product

### political-science

- [[grimmer-2022-textasdata/ch07-vector]] (p. 129): sum of element-wise products; sensitive to vector magnitude [new]

## Instances that use it

- [[euclidean-inner-product]] — $\sum w_k\bar z_k$ on $\mathbf F^n$ — from [[axler-2024-ladr/ch06-inner-p1]]
- [[function-space-inner-product]] — $\int_{-1}^1fg$ on continuous functions — from [[axler-2024-ladr/ch06-inner-p1]]
- [[weighted-inner-product]] — positive weights $c_k$ on $\mathbf F^n$ — from [[axler-2024-ladr/ch06-inner-p1]]
- [[polynomial-evaluation-inner-product]] — $c^Tz=p(t)$ — from [[boyd-2018-vmls/ch01-vectors]]
- [[manhattan-vs-euclidean-norm]] — $\ell_1$ and $\ell_2$ unit sets differ; $\ell_1$ has no inner product — from [[deisenroth-2020-mml/ch03-analytic]]
- [[angle-depends-on-inner-product]] — $[1,1]$ and $[-1,1]$ are orthogonal under the dot product, 109.5° apart under diag(2,1) — from [[deisenroth-2020-mml/ch03-analytic]]
- [[federalist-papers-authorship]] — disputed paper #49 compared with Hamilton and Madison under inner product, cosine, and tf-idf — from [[grimmer-2022-textasdata/ch07-vector]]

## Candidate bridges

- [structural-analogy] (range T)⁰ = null T′ ↔ least squares: the left null space is orthogonal to the column space (the two are the same relation without an inner product). — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → linear-algebra)
- [same-math] $C^{\mathrm t}BC$ rule for the matrix of a bilinear form ↔ inner products: the Gram matrix $\langle e_j,e_k\rangle$ changes this way under a basis change — the inner product is a symmetric bilinear form here (9.10). — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → other:inner-products)
- [structural-analogy] Document scoring $s=Aw$ ↔ regression/text mining: a linear score on a count vector, computed row by row as inner products. — from [[boyd-2018-vmls/ch06-matrices]] (linear-algebra → other:statistics)
- [structural-analogy] "Similar vectors get similar predictions" ↔ linear algebra: inner-product similarity such as cosine similarity (p. 14). The unit does not name the operation. — from [[deisenroth-2020-mml/ch01-introduction]] (linear-algebra → linear-algebra)
- [structural-analogy] Projection onto an orthonormal basis $\lambda=B^\top x$ ↔ Fourier series: coordinates are inner products with orthogonal functions (p. 81, 88). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other:signal-processing)
- [structural-analogy] Inner product matrix $A_{ij}=\langle b_i,b_j\rangle$ ↔ kernel/Gram matrices: many algorithms expressible through inner products alone can be "kernelised" (p. 73, 95). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → linear-algebra)
- [metaphor] Different inner products ↔ different "rulers" for the same space: the same vectors get different lengths and angles (p. 75, 77). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other:different-rulers-for-the)
- [same-math] correlation $=\cos\theta$ (6.61) ↔ linear-algebra: cosine similarity — the inner product of normalised (centred) vectors. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [same-math] SVM Gram matrix $\boldsymbol K$ (symmetric PSD, 12.53) ↔ linear-algebra: positive semidefinite matrices — the Gram matrix of inner products is a PSD matrix. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → linear-algebra)
- [structural-analogy] Dual SVM in $N$ variables from inner products only ↔ PCA/dual view (Ch. 10, mentioned on p. 383) — both work with data via the table of inner products, not the feature dimension. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → unspecified)
- [structural-analogy] transpose of d/dt is −d/dt ↔ functional analysis: adjoint operator defined by ⟨Ax,y⟩ = ⟨x,A*y⟩ — same defining inner-product identity, on functions. — from [[strang-2023-introduction/ch02-solving-p2]] (linear-algebra → other:mathematics)
