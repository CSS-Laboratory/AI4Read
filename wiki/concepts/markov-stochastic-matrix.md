---
id: markov-stochastic-matrix
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 7
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [bryan-2006-eigenvector/main, deisenroth-2020-mml/ch04-matrix-p1, spielman-2025-sagt/ch16-lov, spielman-2025-sagt/ch31-psrgs, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch06-eigenvalues-p1, vonluxburg-2007-spectralclustering/main]
aliases: [markov-matrix]
raw_ids: [Markov (stochastic) matrix]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# markov-stochastic-matrix

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `markov-matrix` — 1 digest(s)

## Canon spine entry

- **Markov (stochastic) matrix** (linear-algebra): non-negative columns summing to 1; the steady state is the eigenvector for eigenvalue 1 (UG)

## Definitions in the sources

### linear-algebra

- [[bryan-2006-eigenvector/main]] (p. 3): column-stochastic: entries $\ge0$, columns sum to 1; always has eigenvalue 1
- [[deisenroth-2020-mml/ch04-matrix-p1]] (pp. 113–114): the PageRank transition matrix of click probabilities; the limit vector $x^*$ of $x,Ax,A^2x,\dots$ is an eigenvector with eigenvalue 1 [as `Markov (stochastic) matrix`]
- [[spielman-2025-sagt/ch16-lov]] (p. 142): W, the walk's transition matrix, acting as g = Wf
- [[spielman-2025-sagt/ch31-psrgs]] (p. 254): $W=M/d$, the ordinary random-walk transition matrix [alias `markov-matrix`]
- [[strang-2023-introduction/app1-ranks]] (pp. 408–409): nonnegative entries, columns add to 1; eigenvalue 1 is always present; example A reaches a steady state, example B does not [as `Markov (stochastic) matrix`]
- [[strang-2023-introduction/ch06-eigenvalues-p1]] (p. 219): columns add to 1; λ = 1 with a steady-state eigenvector [as `Markov (stochastic) matrix`]
- [[vonluxburg-2007-spectralclustering/main]] (p. 14): $P=D^{-1}W$, $L_{\rm rw}=I-P$; stationary $\pi_i=d_i/\mathrm{vol}(V)$

## Candidate bridges

- [same-math] Epidemic matrix ↔ Markov (stochastic) matrix: each column of the $4\times4$ matrix is non-negative and sums to 1 (0.95+0.05; 0.04+0.85+0.10+0.01; 1; 1). This is our observation, not stated in the unit. — from [[boyd-2018-vmls/ch09-linear]] (linear-algebra → linear-algebra)
- [structural-analogy] conditional probability tables $P(Y\mid X)$ (columns sum to 1) ↔ Markov (stochastic) matrix — nonnegative columns summing to 1. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → unspecified)
- [structural-analogy] Convex-hull weights ($\alpha_n\ge0$, $\sum\alpha_n=1$) ↔ Markov (stochastic) matrix columns — both are probability-like weight vectors. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → unspecified)
- [structural-analogy] Markov steady state (eigenvector for λ = 1) ↔ web search: the text says a giant Markov matrix is the key to Google (p. 219). — from [[strang-2023-introduction/ch06-eigenvalues-p1]] (linear-algebra → other:computer-science)
- [structural-analogy] Problem 3's "continuous Markov equation" (columns of A sum to 0) ↔ Markov matrix: a steady state is the eigenvector for the zero eigenvalue, as for eigenvalue 1 in the discrete case. — from [[strang-2023-introduction/ch06-eigenvalues-p3]] (linear-algebra → linear-algebra)
