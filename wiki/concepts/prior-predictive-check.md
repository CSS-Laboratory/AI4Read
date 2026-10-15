---
id: prior-predictive-check
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 5
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch06-model, gelman-2020-workflow/main-p1, gelman-2020-workflow/main-p2, mcelreath-2020-rethinking/ch04-linear-p1, murphy-2023-pml2/ch15-generalized]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# prior-predictive-check

## Canon spine entry

- **Prior predictive check** (bayesian): simulate data from the prior to see whether the model's assumptions produce plausible data (grad)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch06-model]] (p. 162): Box's alternative with $p(y^{\rm rep})=\int p(y^{\rm rep}\mid\theta)p(\theta)d\theta$, mentioned in the bibliographic note
- [[gelman-2020-workflow/main-p1]] (p. 10): simulate data from the prior and model to see what the prior implies, without using observed data
- [[gelman-2020-workflow/main-p2]] (p. 40): used here to see what weak priors imply, e.g. a strongly high-$R^2$ prior from 26 weak weights
- [[mcelreath-2020-rethinking/ch04-linear-p1]] (p. 83): simulating individual heights from the priors to see what they imply (author gives no name)
- [[murphy-2023-pml2/ch15-generalized]] (p. 602): simulate regression lines/outcomes from the prior to judge it

## Candidate bridges

- [structural-analogy] Sensitivity of Bayesian causal-discovery intervals to the prior (Technical Point 10.7) ↔ Bayesian: prior sensitivity / prior predictive checks — prior choice drives conclusions when data cannot discriminate. — from [[hernan-2020-whatif/ch10-random]] (bayesian → bayesian)
- [structural-analogy] Joy Pratt's calibration against data ↔ prior predictive checks: testing a prior against real data — from [[mcgrayne-2011-theory/ch11-business]] (bayesian → bayesian)
