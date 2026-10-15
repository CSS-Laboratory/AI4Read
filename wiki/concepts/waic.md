---
id: waic
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [mcelreath-2020-rethinking/ch06-overfitting-p2, mcelreath-2020-rethinking/ch11-monsters]
raw_ids: [WAIC]
generated_by: build_kg.py
---

# waic

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (pp. 191–192): $-2(\text{lppd}-p_{\text{WAIC}})$; pointwise, no Gaussian assumption [new]
- [[mcelreath-2020-rethinking/ch11-monsters]] (pp. 340, 351): used to compare the ordered models m11.1–m11.3; caution against WAIC for beta-binomial and gamma-Poisson models [as `WAIC`]

## Instances that use it

- [[eight-schools]] — no pooling vs complete pooling vs hierarchical compared by AIC/DIC/WAIC/CV (Table 7.1); Bayes factor failure — from [[gelman-2013-bda3/ch07-evaluating]]
- [[primate-milk-model-comparison]] — m6.11–m6.14; WAIC, weights, masking, averaged predictions — from [[mcelreath-2020-rethinking/ch06-overfitting-p2]]
- [[cars-waic-calculation]] — step-by-step WAIC with 50 × 1000 log-likelihood matrix — from [[mcelreath-2020-rethinking/ch06-overfitting-p2]]
- [[oceanic-tool-kits-kline]] — Poisson regression with log population and contact; counterfactual and WAIC analysis — from [[mcelreath-2020-rethinking/ch10-counting]]
- [[reed-frog-tadpoles]] — 48 tanks, multilevel binomial model, shrinkage and WAIC — from [[mcelreath-2020-rethinking/ch12-multilevel]]
- [[ucb-admissions-varying-slopes]] — departments differ in intercepts; slopes near zero but WAIC favors varying slopes — from [[mcelreath-2020-rethinking/ch13-adventures]]

## Candidate bridges

- [structural-analogy] WAIC/LOO penalty $p_{\rm WAIC}$ ↔ machine learning: held-out validation and degrees of freedom of regularised fits — both estimate the optimism of in-sample fit. — from [[gelman-2013-bda3/ch07-evaluating]] (bayesian → llm)
- [structural-analogy] Overfitting versus predictive accuracy (p. 15) ↔ bayesian: cross-validation/LOO/WAIC — judge on out-of-sample prediction. — from [[mcelreath-2020-rethinking/ch01-golem]] (bayesian → bayesian)
