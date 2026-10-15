---
id: gradient-descent
type: concept
fields: [llm, linear-algebra, bayesian, information-theory]
fields_strong: [llm, linear-algebra, bayesian, information-theory]
n_sources: 5
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch07-continuous, mackay-2003-information/ch39-single, prince-2023-udl/ch02-supervised, prince-2023-udl/ch06-fitting, strang-2023-introduction/ch09-linear]
aliases: [gradient-descent-learning]
generated_by: build_kg.py
---

# gradient-descent

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `gradient-descent-learning` — 1 digest(s)

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch07-continuous]] (p. 228): iterate $x_{i+1}=x_i-\gamma_i(\nabla f(x_i))^\top$ to reach a local minimum [new]
- [[strang-2023-introduction/ch09-linear]] (p. 337): step x_{k+1} = x_k − s_k∇F(x_k) in the steepest direction; s_k is the learning rate [new]

### llm

- [[prince-2023-udl/ch02-supervised]] (p. 22): iteratively stepping downhill on the loss using its gradient [new]
- [[prince-2023-udl/ch06-fitting]] (p. 78): iteratively subtract $\alpha$ times the loss gradient from the parameters [new]

### information-theory

- [[mackay-2003-information/ch39-single]] (pp. 475–476): adjust $\mathbf w$ opposite to the gradient of $G$; on-line is stochastic, batch is gradient descent [alias `gradient-descent-learning`; new; work fields: information-theory, bayesian, llm]

## Instances that use it

- [[quadratic-gd-example]] — Example 7.1: gradient descent on a 2-D quadratic, zigzag — from [[deisenroth-2020-mml/ch07-continuous]]
- [[linear-regression-gradient-descent]] — convex loss; after four iterations the parameters are already close to the minimum — from [[prince-2023-udl/ch06-fitting]]

## Candidate bridges

- [same-math] Incremental gradient (3.10) ↔ machine learning: stochastic gradient descent with random index choice (the text itself makes this link, p. 366). — from [[bertsekas-2026-rlcourse/ch03-learning-p1]] (control-theory → llm)
- [same-math] condition number $\sigma_{\max}/\sigma_{\min}$ ↔ linear-algebra: condition number from the SVD — same quantity, here controlling gradient-descent speed. — from [[deisenroth-2020-mml/ch07-continuous]] (linear-algebra → linear-algebra)
