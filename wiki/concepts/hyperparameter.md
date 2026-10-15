---
id: hyperparameter
type: concept
fields: [llm, bayesian, information-theory]
fields_strong: [llm, bayesian, information-theory]
n_sources: 5
n_works: 3
tiers: [reference, core]
grounding: digests
sources: [mackay-2003-information/ch45-gaussian, mcelreath-2020-rethinking/ch12-multilevel, prince-2023-udl/ch04-deep, prince-2023-udl/ch06-fitting, prince-2023-udl/ch08-measuring]
generated_by: build_kg.py
---

# hyperparameter

## Definitions in the sources

### llm

- [[prince-2023-udl/ch04-deep]] (p. 46): quantity such as K or D_k chosen before learning the parameters [new]
- [[prince-2023-udl/ch06-fitting]] (p. 91): a training choice (batch size, schedule, momentum coefficients) that is not a model parameter [new]
- [[prince-2023-udl/ch08-measuring]] (p. 132): a choice of architecture (e.g. layers, units) or learning algorithm (e.g. learning rate) that affects test performance [new]

### bayesian

- [[mcelreath-2020-rethinking/ch12-multilevel]] (p. 359): a parameter of a prior on parameters, such as α and σ for tank intercepts; its prior is a hyperprior [new]

### information-theory

- [[mackay-2003-information/ch45-gaussian]] (p. 546): parameter $\boldsymbol\theta$ of covariance or noise model, learned from data [new; work fields: information-theory, bayesian]

## Instances that use it

- [[rat-tumor-example]] — crude hyperparameter estimates used to start (p. 263) (new) — from [[gelman-2013-bda3/ch10-introduction]]
- [[hierarchical-noise-hyperparameter-gibbs]] — $\beta$ and $\{x_n\}$ example of slow mixing despite scattered starts — from [[mackay-2003-information/ch30-efficient]]

## Candidate bridges

- [structural-analogy] Hyperparameter $\alpha$ ↔ Bayesian: parameters of a prior fixed outside the model — it shapes learning but not the activity rule. — from [[mackay-2003-information/ch39-single]] (information-theory → bayesian)
- [metaphor] hyperparameters as a "family of families" ↔ model selection: choosing K and D picks a function class before fitting. — from [[prince-2023-udl/ch04-deep]] (llm → other:statistics)
- [structural-analogy] validation set for hyperparameters ↔ model selection in statistics: choosing among models on data not used for the final evaluation. — from [[prince-2023-udl/ch08-measuring]] (llm → other:statistics)
