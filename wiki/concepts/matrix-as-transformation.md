---
id: matrix-as-transformation
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra, llm]
n_sources: 10
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p2, axler-2024-ladr/ch03-linear-p3, axler-2024-ladr/ch05-eigenvalues-p2, boyd-2018-vmls/ch07-matrix, boyd-2018-vmls/ch08-linear, boyd-2018-vmls/ch09-linear, deisenroth-2020-mml/ch02-linear-p2, mikolov-2013-regularities/main, strang-2023-introduction/app10-computer, strang-2023-introduction/ch08-linear]
raw_ids: [matrix as transformation]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# matrix-as-transformation

## Canon spine entry

- **matrix as transformation** (linear-algebra): the columns of A are where the basis vectors land (HS)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p2]] (p. 69): M(T): column k lists the target-basis coordinates of Tv_k; depends on both bases [as `matrix as transformation`]
- [[axler-2024-ladr/ch03-linear-p3]] (p. 113): here ℳ(T′) is ℳ(T)ᵗ in dual bases [as `matrix as transformation`]
- [[axler-2024-ladr/ch05-eigenvalues-p2]] (p. 154): matrix of an operator $\mathcal M(T)$ w.r.t. one basis; column $k$ = coefficients of $Tv_k$ [as `matrix as transformation`]
- [[boyd-2018-vmls/ch07-matrix]] (p. 130): the $i$th column of the matrix is the image of $e_i$; used to build rotation, reflection, etc. [as `matrix as transformation`]
- [[boyd-2018-vmls/ch08-linear]] (p. 148): columns of $A$ are $f(e_1),\dots,f(e_n)$
- [[boyd-2018-vmls/ch09-linear]] (p. 163): here, $A$ maps today's state to tomorrow's [as `matrix as transformation`]
- [[deisenroth-2020-mml/ch02-linear-p2]] (p. 51): here the transformation matrix: columns are $C$-coordinates of $\Phi(b_j)$
- [[mikolov-2013-regularities/main]] (p. 747): $\mathbf U\mathbf w(t)$ selects a column of $\mathbf U$ when $\mathbf w$ is one-hot; the paper does not say this in matrix terms [work fields: linear-algebra, llm]
- [[strang-2023-introduction/app10-computer]] (pp. 413–416): here T, S, R, P are all 4 by 4 maps [as `matrix as transformation`]
- [[strang-2023-introduction/ch08-linear]] (p. 320): column j of the matrix is T(v_j) written in the output basis

## Candidate bridges

- [structural-analogy] Determining $f$ from $f(e_i)$ ↔ matrix as transformation: columns of $A$ are the images of the basis vectors (the scalar case is a single row). — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → linear-algebra)
- [same-math] linear function determined by $f(e_k)$ ↔ linear-algebra: matrix as transformation (columns are images of basis vectors) — same statement. — from [[boyd-2018-vmls/ch08-linear]] (linear-algebra → linear-algebra)
