---
id: data-augmentation
type: concept
fields: [bayesian, llm]
n_sources: 3
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch12-computationally, gelman-2013-bda3/ch18-models, prince-2023-udl/ch09-regularization]
generated_by: build_kg.py
---

# data-augmentation

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch12-computationally]] (p. 293): adding auxiliary variables (e.g., mixture indicators, the $V_i$) to simplify Gibbs or speed convergence [new]
- [[gelman-2013-bda3/ch18-models]] (pp. 451, 465): alternate imputing $y_{\rm mis}$ and drawing parameters; a special case of Gibbs sampling here [new]

### llm

- [[prince-2023-udl/ch09-regularization]] (p. 154): label-preserving transformations that expand the training set [new]

## Instances that use it

- [[1988-presidential-polls-imputation]] — hierarchical normal model for 51 polls with monotone data augmentation — from [[gelman-2013-bda3/ch18-models]]
- [[slovenia-plebiscite-survey]] — "don't know" as missing data, estimand α, EM/SEM/data augmentation, actual 88.5% — from [[gelman-2013-bda3/ch18-models]]
- [[tanner-wong-1987-data-augmentation]] — near-Gibbs scheme, limited impact — from [[robert-2011-mcmc/main]]

## Candidate bridges

- [same-math] adding $J$ prior rows to the regression (16.7) ↔ ridge-type penalized regression: normal prior as data augmentation — same weighted least-squares algebra — from [[gelman-2013-bda3/ch16-generalized]] (bayesian → other)
- [same-math] data augmentation ↔ Gibbs sampling: alternately draw $y_{\rm mis}$ and parameters from full conditionals (the text calls it a special case of Gibbs) (p. 465). — from [[gelman-2013-bda3/ch18-models]] (bayesian → other)
