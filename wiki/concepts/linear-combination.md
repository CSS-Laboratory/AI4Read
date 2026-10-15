---
id: linear-combination
type: concept
fields: [linear-algebra]
n_sources: 10
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch02-finite, axler-2024-ladr/ch03-linear-p2, boyd-2018-vmls/ch01-vectors, boyd-2018-vmls/ch05-linear, boyd-2018-vmls/ch06-matrices, boyd-2018-vmls/ch08-linear, deisenroth-2020-mml/ch02-linear-p1, deisenroth-2020-mml/ch12-classification, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch03-four-p1]
raw_ids: [linear combination]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# linear-combination

## Canon spine entry

- **linear combination** (linear-algebra): a weighted sum of vectors; every Ax is a linear combination of the columns of A (HS)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch02-finite]] (p. 28): a sum $a_1v_1+\dots+a_mv_m$ of scalar multiples of a list [as `linear combination`]
- [[axler-2024-ladr/ch03-linear-p2]] (p. 76): Ab is a combination of the columns of A with coefficients b; rows of CR are combinations of rows of R [as `linear combination`]
- [[boyd-2018-vmls/ch01-vectors]] (p. 17): $\beta_1a_1+\dots+\beta_ma_m$ with scalar coefficients [as `linear combination`]
- [[boyd-2018-vmls/ch05-linear]] (p. 89): weighted sum of vectors; coefficients may be unique or not [as `linear combination`]
- [[boyd-2018-vmls/ch06-matrices]] (p. 119): $Ax=x_1a_1+\dots+x_na_n$, a combination of the columns of $A$ with coefficients $x$ [as `linear combination`]
- [[boyd-2018-vmls/ch08-linear]] (p. 154): $Ax=b$ asks for coefficients expressing $b$ via the columns of $A$
- [[deisenroth-2020-mml/ch02-linear-p1]] (pp. 26, 40): $\sum\lambda_i\boldsymbol x_i$; Ax is a linear combination of the columns of A [as `linear combination`]
- [[deisenroth-2020-mml/ch12-classification]] (p. 384): the optimal $\boldsymbol w$ is a combination of the training examples, i.e. lies in their span
- [[strang-2023-introduction/ch01-vectors]] (pp. 2, 19): cv + dw, or Ax = x₁a₁ + … + xₙaₙ
- [[strang-2023-introduction/ch03-four-p1]] (p. 85): the weighted sum cv + dw; the basic operation of every vector space [as `linear combination`]

## Candidate bridges

- [same-math] Exercise 7.4's weights (7.39)–(7.40) ↔ statistics: minimum-variance linear combination under a known covariance matrix (p. 215) — from [[jaynes-2003-probability/ch07-central-p1]] (information-theory → other)
- [same-math] Portfolio variance $\sum\sum\sigma_{ij}X_iX_j$ ↔ statistics: variance of a linear combination of random variables — the same formula. — from [[markowitz-1952-portfolio/main]] (economics-finance → other)
