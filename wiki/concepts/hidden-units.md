---
id: hidden-units
type: concept
fields: [llm, bayesian, information-theory]
fields_strong: [llm, bayesian, information-theory]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [mackay-2003-information/ch43-boltzmann, prince-2023-udl/ch03-shallow]
aliases: [hidden-unit]
generated_by: build_kg.py
---

# hidden-units

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `hidden-unit` — 1 digest(s)

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch43-boltzmann]] (p. 525): latent variables inducing higher-order visible correlations with pairwise weights [new; work fields: information-theory, bayesian, llm]

### llm

- [[prince-2023-udl/ch03-shallow]] (pp. 27, 35): activation $h_d=a[\theta_{d0}+\sum_i\theta_{di}x_i]$; also called neuron [alias `hidden-unit`; new]

## Instances that use it

- [[shifter-ensemble]] — plain and labelled; not learnable from second-order statistics alone (p. 524); Hinton and Sejnowski learned the labelled one with hidden units — from [[mackay-2003-information/ch43-boltzmann]]
- [[bars-and-stripes-ensemble]] — exercise on learnability without hidden units — from [[mackay-2003-information/ch43-boltzmann]]
- [[14-hidden-unit-regression-fit]] — toy network fitted with different $\lambda$, training stages, ensembles and priors — from [[prince-2023-udl/ch09-regularization]]

## Candidate bridges

- [structural-analogy] Hidden units inducing higher-order visible correlations ↔ bayesian: latent-variable and hierarchical models explaining dependence among observables. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → bayesian)
- [metaphor] "Neurons" and hidden units ↔ neuroscience: the author calls the link "tenuous" (p. 36). — from [[prince-2023-udl/ch03-shallow]] (llm → other:neuroscience)
