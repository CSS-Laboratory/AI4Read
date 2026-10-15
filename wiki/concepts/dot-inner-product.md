---
id: dot-inner-product
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra, llm]
n_sources: 14
n_works: 6
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/ch01-vectors, boyd-2018-vmls/ch02-linear, boyd-2018-vmls/ch03-norm, boyd-2018-vmls/ch06-matrices, boyd-2018-vmls/ch10-matrix, brin-1998-anatomy/main, deerwester-1990-lsa/main, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch06-probability-p1, deisenroth-2020-mml/ch07-continuous, deisenroth-2020-mml/ch12-classification, mikolov-2013-regularities/main, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch02-solving-p2]
aliases: [dot-product]
raw_ids: [dot (inner) product]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# dot-inner-product

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `dot-product` — 2 digest(s)

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
- [[deerwester-1990-lsa/main]] (pdf 8–9): dot product or cosine between vectors in the factor space estimates similarity; cosine is used to rank documents [alias `dot-product`; work fields: linear-algebra, llm]
- [[deisenroth-2020-mml/ch03-analytic]] (p. 72–73): $x^\top y=\sum x_iy_i$; general inner product is symmetric, positive definite, bilinear [as `dot (inner) product`]
- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 196): here $\langle X,Y\rangle=\mathrm{Cov}[x,y]$ on zero-mean random variables [as `dot (inner) product`]
- [[deisenroth-2020-mml/ch07-continuous]] (p. 243): used in conjugate definition [as `dot (inner) product`]
- [[deisenroth-2020-mml/ch12-classification]] (p. 372): inner product $\langle\boldsymbol w,\boldsymbol x\rangle$ used as score, similarity, and in the dual; ties to angle and projection
- [[mikolov-2013-regularities/main]] (p. 748): numerator $x_w\cdot y$ in the answer-selection rule [work fields: linear-algebra, llm]
- [[strang-2023-introduction/ch01-vectors]] (p. 9): v·w = Σvᵢwᵢ; gives length, perpendicularity, angle [alias `dot-product`]
- [[strang-2023-introduction/ch02-solving-p2]] (pp. 68–69): xᵀy; for functions an integral ∫x(t)y(t)dt [as `dot (inner) product`]

## Candidate bridges

- [structural-analogy] additive alignment score $v_a^\top\tanh(W_as+U_ah)$ ↔ LLM canon, attention: query–key similarity then a weighted average of values. Here keys and values are both $h_j$ and the score is an MLP, not a dot product. — from [[bahdanau-2015-attention/main]] (llm → llm)
- [same-math] IR score = count-weights · type-weights ↔ linear models: weighted sum of features — literally a dot product (pdf 12). — from [[brin-1998-anatomy/main]] (linear-algebra → other:statistics)
