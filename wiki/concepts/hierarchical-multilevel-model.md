---
id: hierarchical-multilevel-model
type: concept
fields: [bayesian, information-theory]
n_sources: 12
tiers: [core, reference, deep]
grounding: digests
sources: [gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch16-generalized, gelman-2013-bda3/ch17-models, gelman-2013-bda3/ch22-finite, gelman-2013-bda3/ch23-dirichlet, gelman-2013-philosophy/main, mackay-2003-information/ch30-efficient, mcelreath-2020-rethinking/ch12-multilevel, mcelreath-2020-rethinking/ch13-adventures, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch12-markov-p2, murphy-2023-pml2/ch29-state-p3]
canon_spine: bayesian
generated_by: build_kg.py
---

# hierarchical-multilevel-model

## Canon spine entry

- **Hierarchical (multilevel) model** (bayesian): parameters for groups are themselves drawn from a population distribution, learned from data (UG)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch07-evaluating]] (p. 169): used for the eight schools; replication can be for existing or new groups
- [[gelman-2013-bda3/ch16-generalized]] (p. 409): normal prior on coefficients with hyperparameters estimated from data
- [[gelman-2013-bda3/ch17-models]] (p. 441): t population model for the eight schools
- [[gelman-2013-bda3/ch22-finite]] (p. 520): the authors read the mixing distribution as describing population variation in $\theta$, like a hierarchical model
- [[gelman-2013-bda3/ch23-dirichlet]] (p. 558): DP/DPM priors on group-varying parameters
- [[gelman-2013-philosophy/main]] (p. 8): varying-intercept/slope logistic regressions with partial pooling
- [[mcelreath-2020-rethinking/ch12-multilevel]] (pp. 356, 359): parameters for clusters are drawn from a population distribution whose parameters are also learned
- [[mcelreath-2020-rethinking/ch13-adventures]] (p. 387): parameters for groups drawn from a population distribution; here extended to slopes and several cluster types
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 108): hyperparameters $\boldsymbol\xi$ with their own prior; $\boldsymbol\xi\to\boldsymbol\theta\to\mathcal D$
- [[murphy-2023-pml2/ch12-markov-p2]] (p. 532): source of funnel geometry
- [[murphy-2023-pml2/ch29-state-p3]] (p. 1030): national chain plus state chains

### information-theory

- [[mackay-2003-information/ch30-efficient]] (p. 397): parameters coupled by a hyperparameter; here an example where widely spread starts do not help

## Candidate bridges

- [structural-analogy] Hierarchical VAE layers ↔ hierarchical (multilevel) models: each layer's distribution is conditioned on a more abstract layer. — from [[murphy-2023-pml2/ch21-variational]] (bayesian → other)
