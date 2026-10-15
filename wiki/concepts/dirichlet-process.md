---
id: dirichlet-process
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch23-dirichlet, mackay-2003-information/ch18-crosswords]
generated_by: build_kg.py
---

# dirichlet-process

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch23-dirichlet]] (p. 547): random probability measure $P\sim\mathrm{DP}(\alpha P_0)$ whose bin probabilities on every finite partition are Dirichlet$(\alpha P_0(B_h))$ [new]

### information-theory

- [[mackay-2003-information/ch18-crosswords]] (p. 263): new symbol with probability $\alpha/(F+\alpha)$, symbol $w$ with $F_w/(F+\alpha)$; exchangeable, unbounded vocabulary [new; work fields: information-theory, bayesian]

## Candidate bridges

- [structural-analogy] Dirichlet process predictive rule (18.11–18.12) ↔ bayesian: exchangeable sequences with a growing vocabulary of values. — from [[mackay-2003-information/ch18-crosswords]] (information-theory → bayesian)
- [structural-analogy] infinite mixture models ↔ bayesian: nonparametric priors (Dirichlet process) letting model size grow with data — from [[mackay-2003-information/ch34-independent]] (information-theory → bayesian)
