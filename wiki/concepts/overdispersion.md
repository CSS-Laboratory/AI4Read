---
id: overdispersion
type: concept
fields: [bayesian]
n_sources: 2
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch16-generalized, gelman-2013-bda3/ch17-models]
generated_by: build_kg.py
---

# overdispersion

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch16-generalized]] (p. 407): variation beyond the sampling distribution; handled by hierarchical or per-observation error terms [new]
- [[gelman-2013-bda3/ch17-models]] (p. 437): variance exceeding what the standard model implies; the extensions here can never be underdispersed [new]

## Instances that use it

- [[oceanic-societies-overdispersion]] — Poisson model with an intercept per society to model over-dispersion — from [[mcelreath-2020-rethinking/ch12-multilevel]]

## Candidate bridges

- [structural-analogy] Extra variance $\sigma_y^2$ on binned proportions ↔ random effects/overdispersion in multilevel models — absorbs unexplained variation. The text itself compares it to a saturated interaction term in ANOVA (p. 55). — from [[gelman-2020-workflow/main-p3]] (bayesian → unspecified)
