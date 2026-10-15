---
id: directed-graphical-model
type: concept
fields: [bayesian, linear-algebra]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch08-when, murphy-2023-pml2/ch04-graphical-p1]
generated_by: build_kg.py
---

# directed-graphical-model

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch04-graphical-p1]] (pp. 143–144): DAG whose nodes are variables and whose joint is a product of CPDs given parents; "Bayesian" only in name [new]

### linear-algebra

- [[deisenroth-2020-mml/ch08-when]] (pp. 278–280): a joint factorized as ∏ p(x_k | Pa_k) (8.31) [new]

## Candidate bridges

- [same-math] Markov factorization $f(v)=\prod_j f(v_j\mid pa_j)$ ↔ Bayesian: factorisation of a joint distribution in a directed graphical model (Bayesian network) — same product of conditionals. — from [[hernan-2020-whatif/ch06-graphical]] (bayesian → bayesian)
- [metaphor] "listens to" ↔ bayesian: conditional dependence in a directed graphical model, as in Bayesian networks, which Pearl says underlie causal diagrams (pdf 24). — from [[pearl-2018-bookofwhy/ch00-introduction]] (bayesian → bayesian)
