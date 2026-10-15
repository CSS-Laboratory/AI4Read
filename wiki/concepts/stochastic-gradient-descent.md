---
id: stochastic-gradient-descent
type: concept
fields: [linear-algebra, bayesian, control-theory, llm]
n_sources: 6
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch07-continuous, murphy-2023-pml2/ch06-optimization-p1, prince-2023-udl/ch07-gradients, strang-2023-introduction/ch09-linear, strang-2023-introduction/ch10-learning, sutton-2018-rl/ch09-policy-p1]
generated_by: build_kg.py
---

# stochastic-gradient-descent

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch07-continuous]] (pp. 231–232): gradient descent with an unbiased estimate from a data subset [new]
- [[strang-2023-introduction/ch09-linear]] (p. 348): each step uses one random sample (or batch B) instead of all N [new]
- [[strang-2023-introduction/ch10-learning]] (pp. 371, 373–374): named as the algorithm and chain-rule subroutine for weights [new]

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 271): $\theta_{t+1}=\theta_t-\eta_tg_t$ with unbiased gradient estimate $g_t$ [new]

### control-theory

- [[sutton-2018-rl/ch09-policy-p1]] (p. 201): move $\mathbf w$ a small step along the negative gradient of one example's squared error [new]

### llm

- [[prince-2023-udl/ch07-gradients]] (p. 97): updates parameters by $-\alpha\times$ summed per-example gradients over a batch [new]

## Candidate bridges

- [same-math] Incremental gradient (3.10) ↔ machine learning: stochastic gradient descent with random index choice (the text itself makes this link, p. 366). — from [[bertsekas-2026-rlcourse/ch03-learning-p1]] (control-theory → other)
