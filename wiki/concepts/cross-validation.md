---
id: cross-validation
type: concept
fields: [bayesian, political-science, information-theory, linear-algebra, llm]
fields_strong: [bayesian, political-science, information-theory, linear-algebra, llm]
n_sources: 22
n_works: 11
tiers: [core, reference, deep]
grounding: digests
sources: [boyd-2018-vmls/ch13-least, deisenroth-2020-mml/ch08-when, efron-1986-bayesian/main, gelman-2013-bda3/ch06-model, gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch21-gaussian, gelman-2013-bda3/ch22-finite, gelman-2020-workflow/main-p2, grimmer-2013-textasdata/main, grimmer-2022-textasdata/ch17-overview, grimmer-2022-textasdata/ch20-checking, hernan-2020-whatif/ch18-variable, mackay-2003-information/ch28-model, mackay-2003-information/ch44-supervised, mcelreath-2020-rethinking/ch06-overfitting-p2, mcelreath-2020-rethinking/ch07-interactions, mcelreath-2020-rethinking/ch09-big, mcelreath-2020-rethinking/ch10-counting, mcelreath-2020-rethinking/ch12-multilevel, mcelreath-2020-rethinking/ch13-adventures, murphy-2023-pml2/ch03-statistics-p3, murphy-2023-pml2/ch28-latent-p2]
aliases: [cross-validation-loo-waic]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# cross-validation

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `cross-validation-loo-waic` — 17 digest(s)

## Canon spine entry

- **Cross-validation / LOO / WAIC** (bayesian): estimating out-of-sample predictive accuracy to compare models without overfitting (grad)

## Definitions in the sources

### bayesian

- [[efron-1986-bayesian/main]] (p. 3): the nearest spine concept; Efron's bootstrap analysis for the tree is described as much like a cross-validation, correcting the apparent success rate [alias `cross-validation-loo-waic`]
- [[gelman-2013-bda3/ch06-model]] (p. 153): only touched here via cross-validation predictive p-values [alias `cross-validation-loo-waic`]
- [[gelman-2013-bda3/ch07-evaluating]] (pp. 175–176): Bayesian LOO-CV (7.14), with bias correction $b$, PSIS shortcut, $k$-fold alternative [alias `cross-validation-loo-waic`]
- [[gelman-2013-bda3/ch21-gaussian]] (pp. 509, 511): lppd$_{\text{loo-cv}}$ used to compare GP models [alias `cross-validation-loo-waic`]
- [[gelman-2013-bda3/ch22-finite]] (p. 536): WAIC is theoretically justified for mixtures; DIC is not [alias `cross-validation-loo-waic`]
- [[gelman-2020-workflow/main-p2]] (p. 30–31): leave-out evaluation; here LOO-CV for calibration, hard-to-predict points and influence, approximated by importance sampling [alias `cross-validation-loo-waic`]
- [[hernan-2020-whatif/ch18-variable]] (p. 244): repeated training/validation splitting to estimate out-of-sample prediction accuracy; the chapter covers leave-$v$-out and $k$-fold only. [alias `cross-validation-loo-waic`]
- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (pp. 187, 194): tune priors or compare models by test-sample deviance; WAIC is derived as an approximate Bayesian cross-validation [alias `cross-validation-loo-waic`]
- [[mcelreath-2020-rethinking/ch07-interactions]] (pp. 215, 218): WAIC is used for comparing models and read as a flexibility/overfitting measure, even if the train/test story isn't literal [alias `cross-validation-loo-waic`]
- [[mcelreath-2020-rethinking/ch09-big]] (p. 288): information criteria are comparable only across models with the same likelihood type [alias `cross-validation-loo-waic`]
- [[mcelreath-2020-rethinking/ch10-counting]] (pp. 295, 318): used with ensemble weights to compare models, with the caveat that it is not divination [as `Cross-validation / LOO / WAIC`; alias `cross-validation-loo-waic`]
- [[mcelreath-2020-rethinking/ch12-multilevel]] (pp. 360, 375): WAIC and pWAIC compare the multilevel and fixed models [alias `cross-validation-loo-waic`]
- [[mcelreath-2020-rethinking/ch13-adventures]] (pp. 402, 406–407): WAIC used to compare varying slopes with simpler models and to estimate effective parameters [alias `cross-validation-loo-waic`]
- [[murphy-2023-pml2/ch03-statistics-p3]] (pp. 122–127): LOO-CV, PSIS-LOO, WAIC as predictive-accuracy estimates [alias `cross-validation-loo-waic`]
- [[murphy-2023-pml2/ch28-latent-p2]] (p. 967): test-set log likelihood for choosing the number of topics [alias `cross-validation-loo-waic`]

### political-science

- [[grimmer-2013-textasdata/main]] (p. 13): V-fold out-of-sample assessment of a model [new]
- [[grimmer-2022-textasdata/ch17-overview]] (p. 299): repeated split, fit and assess on held-out data, then average [new]
- [[grimmer-2022-textasdata/ch20-checking]] (p. 340): $V$-fold out-of-sample assessment; accurate only if the labeled sample is random from the population [new]

### information-theory

- [[mackay-2003-information/ch28-model]] (p. 353): here leave-one-out is contrasted with the evidence: it examines the average of just the last term of the on-line sum under random re-orderings [alias `cross-validation-loo-waic`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch44-supervised]] (p. 531): contrasted: a cross-validation measure is noisy, unlike the Bayesian objective [as `Cross-validation / LOO / WAIC`; alias `cross-validation-loo-waic`; work fields: information-theory, bayesian, llm]

### linear-algebra

- [[boyd-2018-vmls/ch13-least]] (pp. 264–265): k-fold rotation; checks a choice of basis functions via RMS cross-validation error (13.4) [new]
- [[deisenroth-2020-mml/ch08-when]] (p. 263): K-fold estimate of generalization error, (8.13) [new]

## Instances that use it

- [[house-price-cross-validation]] — Sacramento sales, 774 records; RMS cross-validation error 75.41 (simple), 119.93 (constant), 69.29 (engineered) — from [[boyd-2018-vmls/ch13-least]]
- [[k-fold-cross-validation]] — split into $k$ parts, each used once for validation; $k=10$ is common. — from [[hernan-2020-whatif/ch18-variable]]

## Candidate bridges

- [structural-analogy] train/test split and k-fold cross-validation ↔ computational social science: held-out evaluation of predictive models, and avoiding leakage when data are ordered in time. — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → other:computational-social-science)
- [structural-analogy] Marginal/cross-validation predictive p-values ↔ leave-one-out predictive checks (Chapter 7): same conditional predictive idea. — from [[gelman-2013-bda3/ch06-model]] (bayesian → other:leave-one-out-predictive)
- [structural-analogy] Model selection as a decision with data-collection costs (p. 239) ↔ cross-validation/LOO: both frame model choice by predictive utility. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → bayesian)
- [structural-analogy] Stacking of chains/models with cross-validation weights ↔ model averaging in predictive ensembles — weights are chosen by predictive performance, not by posterior probability (p. 25). — from [[gelman-2020-workflow/main-p1]] (bayesian → unspecified)
- [structural-analogy] Bias–variance trade-off in choosing the number of parameters ↔ bayesian: Bayesian Occam's razor and cross-validation for model choice. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [structural-analogy] $k$-fold cross-validation (p. 244) ↔ Bayesian model checking: LOO-type estimates of out-of-sample accuracy — both estimate predictive accuracy without overfitting. — from [[hernan-2020-whatif/ch18-variable]] (bayesian → bayesian)
- [structural-analogy] evidence vs leave-one-out cross-validation ↔ bayesian: model-comparison scores — one rewards all sequential predictions, the other only the last (p. 353) — from [[mackay-2003-information/ch28-model]] (information-theory → bayesian)
- [structural-analogy] evidence maximization ↔ cross-validation: both choose complexity, one without held-out data. — from [[mackay-2003-information/ch44-supervised]] (information-theory → bayesian)
- [structural-analogy] Overfitting versus predictive accuracy (p. 15) ↔ bayesian: cross-validation/LOO/WAIC — judge on out-of-sample prediction. — from [[mcelreath-2020-rethinking/ch01-golem]] (bayesian → bayesian)
- [structural-analogy] train/test deviance simulation ↔ cross-validation: estimating out-of-sample error from held-out data. — from [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (bayesian → bayesian)
- [structural-analogy] Cross-fitting ↔ bayesian: cross-validation — data folds so each prediction comes from a model that did not see that point. — from [[murphy-2023-pml2/ch36-causality-p1]] (bayesian → bayesian)
