---
id: nuisance-parameter
type: concept
fields: [information-theory, bayesian]
n_sources: 9
tiers: [reference, core]
grounding: digests
sources: [gelman-2013-bda3/ch03-introduction, jaynes-2003-probability/ch07-central-p2, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch15-paradoxes, jaynes-2003-probability/ch16-orthodox, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, jaynes-2003-probability/ch21-outliers, mackay-2003-information/ch24-exact]
generated_by: build_kg.py
---

# nuisance-parameter

## Definitions in the sources

### information-theory

- [[jaynes-2003-probability/ch07-central-p2]] (p. 220): relevant but uninteresting parameter, included in the model and integrated out [new]
- [[jaynes-2003-probability/ch08-sufficiency]] (p. 250): a parameter not of interest, integrated out; sufficiency is then defined via the marginalized $F$ of (8.24) [new]
- [[jaynes-2003-probability/ch15-paradoxes]] (p. 471): parameter integrated out of the posterior; a prior on it still affects the marginal posterior [new]
- [[jaynes-2003-probability/ch16-orthodox]] (p. 497): unknown parameter not of interest; named as orthodoxy's difficulty [new]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 527): parameter integrated out (here $\mu,\sigma$) [new]
- [[jaynes-2003-probability/ch17-principles-p2]] (p. 535, 537): a parameter we must model but do not want to estimate; Bayes integrates it out [new]
- [[jaynes-2003-probability/ch21-outliers]] (p. 621): a parameter (here η, u) integrated out when estimating θ [new]
- [[mackay-2003-information/ch24-exact]] (p. 319): a continuous parameter we must model but do not want to infer [new]

### bayesian

- [[gelman-2013-bda3/ch03-introduction]] (p. 63): a parameter needed for the model but not of inferential interest, e.g. the error scale [new]

## Candidate bridges

- [structural-analogy] Nuisance parameters in outcome versus treatment models ↔ Bayesian inference: parameters not of interest are handled in a separate model component (the unit does not discuss this). — from [[hernan-2020-whatif/ch15-outcome]] (bayesian → bayesian)
- [structural-analogy] Integrating out $\sigma$ as a nuisance parameter ↔ Bayesian: hierarchical models averaging over group-level uncertainty (p. 219) — from [[jaynes-2003-probability/ch07-central-p1]] (information-theory → bayesian)
- [structural-analogy] Marginalization (B₁ vs B₂) ↔ Bayesian: sufficiency and ancillary statistics — a statistic whose sampling distribution is free of the nuisance parameter is the structure DSZ exploit. — from [[jaynes-2003-probability/ch15-paradoxes]] (information-theory → bayesian)
