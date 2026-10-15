---
id: instrumental-variable
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 5
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch03-observational, hernan-2020-whatif/ch16-instrumental, murphy-2023-pml2/ch36-causality-p2, pearl-2016-primer/ch03-effects, pearl-2018-bookofwhy/ch07-beyond]
generated_by: build_kg.py
---

# instrumental-variable

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch03-observational]] (p. 28): a treatment predictor assumed to be as-if randomized given measured covariates; deferred to Chapter 16 [new]
- [[hernan-2020-whatif/ch16-instrumental]] (p. 209): variable $Z$ meeting three conditions that lets $A$'s effect on $Y$ be estimated without measuring all confounders, given a fourth condition [new]
- [[murphy-2023-pml2/ch36-causality-p2]] (p. 1209): variable $Z$ that affects $Y$ only via $A$; relevance, unconfoundedness, exclusion [new]
- [[pearl-2016-primer/ch03-effects]] (p. 86): variable d-connected to $X$ and d-separated from $Y$ in $G_\alpha$; gives $\alpha=r_1/r_2$ [new]
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 226–228): Z with no confounder in common with the outcome, an effect on X, and no direct arrow to Y. Gives $b=r_{ZY}/r_{ZX}$ in linear models [new]

## Candidate bridges

- [same-math] ITT vs CACE ↔ causal inference: instrumental-variable estimation with random assignment as the instrument (the standard identity is not printed in this paper). — from [[bail-2018-opposingviews/main]] (political-science → bayesian)
- [structural-analogy] CACE with exclusion restriction ↔ econometrics: instrumental variables (Wald-type ratio, (8.19)). — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → economics-finance)
- [same-math] Franklin's two-sample instrumental variables (Appendix B) ↔ econometrics: constructing a proxy from auxiliaries estimated in a second dataset — the same regress-then-predict construction. — from [[zaller-1992-massopinion/ch09-two]] (political-science → economics-finance)
