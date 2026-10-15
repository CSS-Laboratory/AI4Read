---
id: overdispersion
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 4
n_works: 2
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch16-generalized, gelman-2013-bda3/ch17-models, mcelreath-2020-rethinking/ch11-monsters, mcelreath-2020-rethinking/ch12-multilevel]
aliases: [over-dispersion]
generated_by: build_kg.py
---

# overdispersion

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `over-dispersion` — 2 digest(s)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch16-generalized]] (p. 407): variation beyond the sampling distribution; handled by hierarchical or per-observation error terms [new]
- [[gelman-2013-bda3/ch17-models]] (p. 437): variance exceeding what the standard model implies; the extensions here can never be underdispersed [new]
- [[mcelreath-2020-rethinking/ch11-monsters]] (p. 346): observed variance larger than the count likelihood implies after conditioning on predictors [alias `over-dispersion`; new]
- [[mcelreath-2020-rethinking/ch12-multilevel]] (pp. 363, 382): more variation than a binomial or Poisson model expects; a varying intercept per observation can model it [alias `over-dispersion`; new]

## Instances that use it

- [[oceanic-societies-overdispersion]] — Poisson model with an intercept per society to model over-dispersion — from [[mcelreath-2020-rethinking/ch12-multilevel]]

## Candidate bridges

- [structural-analogy] Extra variance $\sigma_y^2$ on binned proportions ↔ random effects/overdispersion in multilevel models — absorbs unexplained variation. The text itself compares it to a saturated interaction term in ANOVA (p. 55). — from [[gelman-2020-workflow/main-p3]] (bayesian → unspecified)
- [structural-analogy] Varying intercept on every observation ↔ over-dispersed count models (beta-binomial, gamma-Poisson): the text says both allow over-dispersion; whether the math is identical is not claimed. — from [[mcelreath-2020-rethinking/ch12-multilevel]] (bayesian → other:over-dispersed-count-models)
