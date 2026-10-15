---
id: dot-inner-product
type: concept
fields: [linear-algebra]
n_sources: 12
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/ch01-vectors, boyd-2018-vmls/ch02-linear, boyd-2018-vmls/ch03-norm, boyd-2018-vmls/ch06-matrices, boyd-2018-vmls/ch10-matrix, brin-1998-anatomy/main, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch06-probability-p1, deisenroth-2020-mml/ch07-continuous, deisenroth-2020-mml/ch12-classification, mikolov-2013-regularities/main, strang-2023-introduction/ch02-solving-p2]
raw_ids: [dot (inner) product]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# dot-inner-product

## Canon spine entry

- **dot (inner) product** (linear-algebra): Σxᵢyᵢ; measures alignment and induces length and angle (HS)

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch01-vectors]] (p. 19): $a^Tb=\sum a_ib_i$, called inner or dot product here [as `dot (inner) product`]
- [[boyd-2018-vmls/ch02-linear]] (pp. 30–31): $a^Tx$ is the weighted sum of the entries of $x$; every linear scalar function has this form with a unique $a$
- [[boyd-2018-vmls/ch03-norm]] (pp. 47, 60): xᵀy; ties norm of a sum to angles via (3.1) and (3.6)
- [[boyd-2018-vmls/ch06-matrices]] (p. 121): $a^Tb$ is a special case of matrix-vector multiplication [as `dot (inner) product`]
- [[boyd-2018-vmls/ch10-matrix]] (p. 178): $a^Tb$ as the product of a 1×n and an n×1 matrix [as `dot (inner) product`]
- [[brin-1998-anatomy/main]] (pdf 12): used to combine count-weights with type or type–proximity weights into an IR score [as `dot (inner) product`]
- [[deisenroth-2020-mml/ch03-analytic]] (p. 72–73): $x^\top y=\sum x_iy_i$; general inner product is symmetric, positive definite, bilinear [as `dot (inner) product`]
- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 196): here $\langle X,Y\rangle=\mathrm{Cov}[x,y]$ on zero-mean random variables [as `dot (inner) product`]
- [[deisenroth-2020-mml/ch07-continuous]] (p. 243): used in conjugate definition [as `dot (inner) product`]
- [[deisenroth-2020-mml/ch12-classification]] (p. 372): inner product $\langle\boldsymbol w,\boldsymbol x\rangle$ used as score, similarity, and in the dual; ties to angle and projection
- [[mikolov-2013-regularities/main]] (p. 748): numerator $x_w\cdot y$ in the answer-selection rule
- [[strang-2023-introduction/ch02-solving-p2]] (pp. 68–69): xᵀy; for functions an integral ∫x(t)y(t)dt [as `dot (inner) product`]
