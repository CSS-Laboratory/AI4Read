---
id: belief-propagation
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [murphy-2023-pml2/ch09-message, pearl-2018-bookofwhy/ch03-evidence]
generated_by: build_kg.py
---

# belief-propagation

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch09-message]] (pp. 401, 415): local messages between neighbouring nodes/cliques that let nodes agree on global marginals; exact on trees (pp. 401, 415) (new)
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 110): repeated message passing between nodes using Bayes's rule [new]

## Instances that use it

- [[turbo-codes]] — belief propagation in phone decoding — from [[pearl-2018-bookofwhy/ch03-evidence]]

## Candidate bridges

- [same-math] Sum–product decoding ↔ bayesian: belief propagation on a factor graph, computing marginal posteriors exactly on trees — the text itself gives the name belief propagation (p. 557). — from [[mackay-2003-information/ch47-low]] (information-theory → bayesian)
- [structural-analogy] Peeling decoder with certain/uncertain messages ↔ bayesian: belief propagation on a factor graph — the text calls it sum–product with extreme messages. — from [[mackay-2003-information/ch50-digital]] (information-theory → bayesian)
- [structural-analogy] VMP ↔ belief propagation: message passing, but messages are expected sufficient statistics (p. 470) — from [[murphy-2023-pml2/ch10-variational-p2]] (bayesian → bayesian)
