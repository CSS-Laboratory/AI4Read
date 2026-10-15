---
id: link-function
type: concept
fields: [bayesian]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch16-generalized, hernan-2020-whatif/ch11-model, mcelreath-2020-rethinking/ch09-big, murphy-2023-pml2/ch15-generalized]
generated_by: build_kg.py
---

# link-function

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch16-generalized]] (pp. 405, 407): maps the mean to the linear predictor scale; canonical link = the one in the exponential-family exponent [new]
- [[hernan-2020-whatif/ch11-model]] (p. 161): $g$ with $g\{\mathrm{E}[Y|X]\}=\sum\theta_iX_i$ [new]
- [[mcelreath-2020-rethinking/ch09-big]] (pp. 281, 284): maps the linear model onto the allowed range of a likelihood parameter [new]
- [[murphy-2023-pml2/ch15-generalized]] (pp. 591, 594): $\ell$ with $\ell(\mu)=w^\top x$; canonical link makes $\ell(\mu)=$ natural parameter [new]
