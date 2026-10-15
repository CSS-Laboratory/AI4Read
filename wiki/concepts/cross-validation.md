---
id: cross-validation
type: concept
fields: [political-science, linear-algebra]
n_sources: 5
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/ch13-least, deisenroth-2020-mml/ch08-when, grimmer-2013-textasdata/main, grimmer-2022-textasdata/ch17-overview, grimmer-2022-textasdata/ch20-checking]
generated_by: build_kg.py
---

# cross-validation

## Definitions in the sources

### political-science

- [[grimmer-2013-textasdata/main]] (p. 13): V-fold out-of-sample assessment of a model [new]
- [[grimmer-2022-textasdata/ch17-overview]] (p. 299): repeated split, fit and assess on held-out data, then average [new]
- [[grimmer-2022-textasdata/ch20-checking]] (p. 340): $V$-fold out-of-sample assessment; accurate only if the labeled sample is random from the population [new]

### linear-algebra

- [[boyd-2018-vmls/ch13-least]] (pp. 264–265): k-fold rotation; checks a choice of basis functions via RMS cross-validation error (13.4) [new]
- [[deisenroth-2020-mml/ch08-when]] (p. 263): K-fold estimate of generalization error, (8.13) [new]

## Instances that use it

- [[house-price-cross-validation]] — Sacramento sales, 774 records; RMS cross-validation error 75.41 (simple), 119.93 (constant), 69.29 (engineered) — from [[boyd-2018-vmls/ch13-least]]
- [[k-fold-cross-validation]] — split into $k$ parts, each used once for validation; $k=10$ is common. — from [[hernan-2020-whatif/ch18-variable]]

## Candidate bridges

- [structural-analogy] train/test split and k-fold cross-validation ↔ computational social science: held-out evaluation of predictive models, and avoiding leakage when data are ordered in time. — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → other)
- [structural-analogy] Marginal/cross-validation predictive p-values ↔ leave-one-out predictive checks (Chapter 7): same conditional predictive idea. — from [[gelman-2013-bda3/ch06-model]] (bayesian → other)
- [structural-analogy] Model selection as a decision with data-collection costs (p. 239) ↔ cross-validation/LOO: both frame model choice by predictive utility. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → other)
- [structural-analogy] Stacking of chains/models with cross-validation weights ↔ model averaging in predictive ensembles — weights are chosen by predictive performance, not by posterior probability (p. 25). — from [[gelman-2020-workflow/main-p1]] (bayesian → unspecified)
- [structural-analogy] Bias–variance trade-off in choosing the number of parameters ↔ bayesian: Bayesian Occam's razor and cross-validation for model choice. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [structural-analogy] $k$-fold cross-validation (p. 244) ↔ Bayesian model checking: LOO-type estimates of out-of-sample accuracy — both estimate predictive accuracy without overfitting. — from [[hernan-2020-whatif/ch18-variable]] (bayesian → bayesian)
- [structural-analogy] evidence vs leave-one-out cross-validation ↔ bayesian: model-comparison scores — one rewards all sequential predictions, the other only the last (p. 353) — from [[mackay-2003-information/ch28-model]] (information-theory → bayesian)
- [structural-analogy] evidence maximization ↔ cross-validation: both choose complexity, one without held-out data. — from [[mackay-2003-information/ch44-supervised]] (information-theory → other)
- [structural-analogy] Overfitting versus predictive accuracy (p. 15) ↔ bayesian: cross-validation/LOO/WAIC — judge on out-of-sample prediction. — from [[mcelreath-2020-rethinking/ch01-golem]] (bayesian → bayesian)
- [structural-analogy] train/test deviance simulation ↔ cross-validation: estimating out-of-sample error from held-out data. — from [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (bayesian → other)
- [structural-analogy] Cross-fitting ↔ bayesian: cross-validation — data folds so each prediction comes from a model that did not see that point. — from [[murphy-2023-pml2/ch36-causality-p1]] (bayesian → bayesian)
