---
id: sequential-exchangeability
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 3
n_works: 1
tiers: [core]
grounding: digests
sources: [hernan-2020-whatif/ch19-time, hernan-2020-whatif/ch20-treatment, hernan-2020-whatif/ch21-g]
generated_by: build_kg.py
---

# sequential-exchangeability

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch19-time]] (pp. 260, 263): $Y^g\perp\!\!\!\perp A_k\mid\bar A_{k-1}=g(\cdot),\bar L_k$ at every $k$; "static" version covers only $g=\bar a$ [new]
- [[hernan-2020-whatif/ch20-treatment]] (p. 274): conditional exchangeability at each time given past treatment and covariates; generally needs $\bar A_{k-1}$ [new]
- [[hernan-2020-whatif/ch21-g]] (p. 277): exchangeability at each time given measured past; identifies sustained-strategy effects [new]

## Candidate bridges

- [structural-analogy] sequential exchangeability ↔ sequential/adaptive Bayesian experimentation: assignment may depend on observed past but not on unobserved outcome drivers. — from [[hernan-2020-whatif/ch19-time]] (bayesian → bayesian)
