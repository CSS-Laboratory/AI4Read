---
id: sutva
type: concept
fields: [bayesian, political-science]
fields_strong: [bayesian, political-science]
n_sources: 6
n_works: 5
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch08-modeling, grimmer-2022-textasdata/ch24-causal, hernan-2020-whatif/ch01-definition, hernan-2020-whatif/ch04-effect, murphy-2023-pml2/ch04-graphical-p3, pearl-2018-bookofwhy/ch08-counterfactuals]
raw_ids: [SUTVA]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# sutva

## Canon spine entry

- **SUTVA** (bayesian): one unit's treatment doesn't affect another's outcome and there is only one version of each treatment (grad)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch08-modeling]] (p. 200): stability: no interference, $y$ unaffected by $I$
- [[hernan-2020-whatif/ch01-definition]] (p. 5): here "no interference": an individual's outcome does not depend on others' treatments. Fine Point 1.1 names it as a component of Rubin's SUTVA [as `SUTVA`]
- [[hernan-2020-whatif/ch04-effect]] (p. 54): interference is mentioned as a reason effects differ across populations
- [[murphy-2023-pml2/ch04-graphical-p3]] (p. 217): here: independent noise across units (no interference)
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 255): one unit's effect does not depend on others' treatments

### political-science

- [[grimmer-2022-textasdata/ch24-causal]] (p. 411): a unit's outcome depends only on its own treatment status; no interference, consistent treatment (p. 411) (new)

## Instances that use it

- [[news-story-spillover-example]] — treated group re-shares story to control group; SUTVA violated — from [[grimmer-2022-textasdata/ch24-causal]]
