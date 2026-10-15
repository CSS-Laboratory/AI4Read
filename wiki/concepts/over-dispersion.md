---
id: over-dispersion
type: concept
fields: [bayesian]
n_sources: 2
tiers: [core]
grounding: digests
sources: [mcelreath-2020-rethinking/ch11-monsters, mcelreath-2020-rethinking/ch12-multilevel]
generated_by: build_kg.py
---

# over-dispersion

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch11-monsters]] (p. 346): observed variance larger than the count likelihood implies after conditioning on predictors [new]
- [[mcelreath-2020-rethinking/ch12-multilevel]] (pp. 363, 382): more variation than a binomial or Poisson model expects; a varying intercept per observation can model it [new]

## Instances that use it

- [[oceanic-societies-overdispersion]] — Poisson model with an intercept per society to model over-dispersion — from [[mcelreath-2020-rethinking/ch12-multilevel]]

## Candidate bridges

- [structural-analogy] Varying intercept on every observation ↔ over-dispersed count models (beta-binomial, gamma-Poisson): the text says both allow over-dispersion; whether the math is identical is not claimed. — from [[mcelreath-2020-rethinking/ch12-multilevel]] (bayesian → other)
