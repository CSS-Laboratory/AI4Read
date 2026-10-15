---
id: effective-number-of-parameters
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch07-evaluating, mcelreath-2020-rethinking/ch06-overfitting-p2, mcelreath-2020-rethinking/ch12-multilevel]
generated_by: build_kg.py
---

# effective-number-of-parameters

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch07-evaluating]] (pp. 172–174): data-based penalty ($k$, $p_{\rm DIC}$, $p_{\rm WAIC}$, $p_{\rm loo\text{-}cv}$); about 1 per unconstrained, 0 per prior-determined parameter [new]
- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (pp. 191–192): $p_D$ or $p_{\text{WAIC}}$; a measure of model flexibility that regularization lowers [new]
- [[mcelreath-2020-rethinking/ch12-multilevel]] (pp. 360, 375): pWAIC; how flexible the fit is, fewer than actual parameters under shrinkage [new]
