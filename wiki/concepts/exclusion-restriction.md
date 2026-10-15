---
id: exclusion-restriction
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 3
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch16-instrumental, hernan-2020-whatif/ch22-target, murphy-2023-pml2/ch36-causality-p2]
generated_by: build_kg.py
---

# exclusion-restriction

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch16-instrumental]] (p. 210): condition (ii), "no direct effect of $Z$ on $Y$"; individual or population level [new]
- [[hernan-2020-whatif/ch22-target]] (p. 306): assumption of no direct arrow $Z\to Y$, i.e., assignment affects the outcome only through received treatment [new]
- [[murphy-2023-pml2/ch36-causality-p2]] (p. 1209): all directed paths from $Z$ to $Y$ pass through $A$ [new]

## Instances that use it

- [[vaccine-plus-antiviral-trial]] — non-adherence, $U$ and the exclusion restriction — from [[hernan-2020-whatif/ch22-target]]

## Candidate bridges

- [structural-analogy] CACE with exclusion restriction ↔ econometrics: instrumental variables (Wald-type ratio, (8.19)). — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → economics-finance)
