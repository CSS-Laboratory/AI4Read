---
id: missing-at-random
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch08-modeling, gelman-2013-bda3/ch18-models]
generated_by: build_kg.py
---

# missing-at-random

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch08-modeling]] (p. 202): $p(I|x,y,\phi)=p(I|x,y_{\rm obs},\phi)$; includes deterministic rules based on $x$ [new]
- [[gelman-2013-bda3/ch18-models]] (p. 450): $p(I|y_{\rm obs},y_{\rm mis},\phi)=p(I|y_{\rm obs},\phi)$; mechanism may depend on observed values only [new]

## Candidate bridges

- [structural-analogy] conditional exchangeability / ignorable assignment ↔ missing data: $Y^a$ is missing for those with $A\neq a$; ignorability plays the role of "missing at random" given $L$. — from [[hernan-2020-whatif/ch03-observational]] (bayesian → bayesian)
- [structural-analogy] Table 4.4 randomization (missing entries independent of potential outcomes) ↔ missing-data view of causal inference: unobserved potential outcomes missing at random. — from [[pearl-2016-primer/ch04-counterfactuals]] (bayesian → bayesian)
