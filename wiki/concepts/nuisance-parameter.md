---
id: nuisance-parameter
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 10
n_works: 4
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch03-introduction, hernan-2020-whatif/ch15-outcome, jaynes-2003-probability/ch07-central-p2, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch15-paradoxes, jaynes-2003-probability/ch16-orthodox, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, jaynes-2003-probability/ch21-outliers, mackay-2003-information/ch24-exact]
aliases: [nuisance-parameters]
generated_by: build_kg.py
---

# nuisance-parameter

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `nuisance-parameters` — 1 digest(s)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch03-introduction]] (p. 63): a parameter needed for the model but not of inferential interest, e.g. the error scale [new]
- [[hernan-2020-whatif/ch15-outcome]] (p. 200): parameters not of primary interest, e.g. those of the outcome model or the treatment model [alias `nuisance-parameters`; new]
- [[jaynes-2003-probability/ch07-central-p2]] (p. 220): relevant but uninteresting parameter, included in the model and integrated out [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch08-sufficiency]] (p. 250): a parameter not of interest, integrated out; sufficiency is then defined via the marginalized $F$ of (8.24) [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch15-paradoxes]] (p. 471): parameter integrated out of the posterior; a prior on it still affects the marginal posterior [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch16-orthodox]] (p. 497): unknown parameter not of interest; named as orthodoxy's difficulty [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 527): parameter integrated out (here $\mu,\sigma$) [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p2]] (p. 535, 537): a parameter we must model but do not want to estimate; Bayes integrates it out [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch21-outliers]] (p. 621): a parameter (here η, u) integrated out when estimating θ [new; work fields: bayesian, information-theory]

### information-theory

- [[mackay-2003-information/ch24-exact]] (p. 319): a continuous parameter we must model but do not want to infer [new; work fields: information-theory, bayesian]

## Candidate bridges

- [structural-analogy] Nuisance parameters in outcome versus treatment models ↔ Bayesian inference: parameters not of interest are handled in a separate model component (the unit does not discuss this). — from [[hernan-2020-whatif/ch15-outcome]] (bayesian → bayesian)
- [structural-analogy] Integrating out $\sigma$ as a nuisance parameter ↔ Bayesian: hierarchical models averaging over group-level uncertainty (p. 219) — from [[jaynes-2003-probability/ch07-central-p1]] (bayesian → bayesian)
- [structural-analogy] Marginalization (B₁ vs B₂) ↔ Bayesian: sufficiency and ancillary statistics — a statistic whose sampling distribution is free of the nuisance parameter is the structure DSZ exploit. — from [[jaynes-2003-probability/ch15-paradoxes]] (bayesian → bayesian)
