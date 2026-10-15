---
id: cross-validation-loo-waic
type: concept
fields: [bayesian, information-theory]
n_sources: 17
tiers: [core, reference]
grounding: digests
sources: [efron-1986-bayesian/main, gelman-2013-bda3/ch06-model, gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch21-gaussian, gelman-2013-bda3/ch22-finite, gelman-2020-workflow/main-p2, hernan-2020-whatif/ch18-variable, mackay-2003-information/ch28-model, mackay-2003-information/ch44-supervised, mcelreath-2020-rethinking/ch06-overfitting-p2, mcelreath-2020-rethinking/ch07-interactions, mcelreath-2020-rethinking/ch09-big, mcelreath-2020-rethinking/ch10-counting, mcelreath-2020-rethinking/ch12-multilevel, mcelreath-2020-rethinking/ch13-adventures, murphy-2023-pml2/ch03-statistics-p3, murphy-2023-pml2/ch28-latent-p2]
raw_ids: [Cross-validation / LOO / WAIC]
canon_spine: bayesian
generated_by: build_kg.py
---

# cross-validation-loo-waic

## Canon spine entry

- **Cross-validation / LOO / WAIC** (bayesian): estimating out-of-sample predictive accuracy to compare models without overfitting (grad)

## Definitions in the sources

### bayesian

- [[efron-1986-bayesian/main]] (p. 3): the nearest spine concept; Efron's bootstrap analysis for the tree is described as much like a cross-validation, correcting the apparent success rate
- [[gelman-2013-bda3/ch06-model]] (p. 153): only touched here via cross-validation predictive p-values
- [[gelman-2013-bda3/ch07-evaluating]] (pp. 175–176): Bayesian LOO-CV (7.14), with bias correction $b$, PSIS shortcut, $k$-fold alternative
- [[gelman-2013-bda3/ch21-gaussian]] (pp. 509, 511): lppd$_{\text{loo-cv}}$ used to compare GP models
- [[gelman-2013-bda3/ch22-finite]] (p. 536): WAIC is theoretically justified for mixtures; DIC is not
- [[gelman-2020-workflow/main-p2]] (p. 30–31): leave-out evaluation; here LOO-CV for calibration, hard-to-predict points and influence, approximated by importance sampling
- [[hernan-2020-whatif/ch18-variable]] (p. 244): repeated training/validation splitting to estimate out-of-sample prediction accuracy; the chapter covers leave-$v$-out and $k$-fold only.
- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (pp. 187, 194): tune priors or compare models by test-sample deviance; WAIC is derived as an approximate Bayesian cross-validation
- [[mcelreath-2020-rethinking/ch07-interactions]] (pp. 215, 218): WAIC is used for comparing models and read as a flexibility/overfitting measure, even if the train/test story isn't literal
- [[mcelreath-2020-rethinking/ch09-big]] (p. 288): information criteria are comparable only across models with the same likelihood type
- [[mcelreath-2020-rethinking/ch10-counting]] (pp. 295, 318): used with ensemble weights to compare models, with the caveat that it is not divination [as `Cross-validation / LOO / WAIC`]
- [[mcelreath-2020-rethinking/ch12-multilevel]] (pp. 360, 375): WAIC and pWAIC compare the multilevel and fixed models
- [[mcelreath-2020-rethinking/ch13-adventures]] (pp. 402, 406–407): WAIC used to compare varying slopes with simpler models and to estimate effective parameters
- [[murphy-2023-pml2/ch03-statistics-p3]] (pp. 122–127): LOO-CV, PSIS-LOO, WAIC as predictive-accuracy estimates
- [[murphy-2023-pml2/ch28-latent-p2]] (p. 967): test-set log likelihood for choosing the number of topics

### information-theory

- [[mackay-2003-information/ch28-model]] (p. 353): here leave-one-out is contrasted with the evidence: it examines the average of just the last term of the on-line sum under random re-orderings
- [[mackay-2003-information/ch44-supervised]] (p. 531): contrasted: a cross-validation measure is noisy, unlike the Bayesian objective [as `Cross-validation / LOO / WAIC`]

## Candidate bridges

- [structural-analogy] Overfitting versus predictive accuracy (p. 15) ↔ bayesian: cross-validation/LOO/WAIC — judge on out-of-sample prediction. — from [[mcelreath-2020-rethinking/ch01-golem]] (bayesian → bayesian)
