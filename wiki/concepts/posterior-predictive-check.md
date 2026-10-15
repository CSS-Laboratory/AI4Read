---
id: posterior-predictive-check
type: concept
fields: [bayesian, analytic-philosophy]
fields_strong: [bayesian, analytic-philosophy]
n_sources: 17
n_works: 5
tiers: [core, deep, reference]
grounding: digests
sources: [gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch06-model, gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch08-modeling, gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch15-hierarchical, gelman-2013-bda3/ch17-models, gelman-2013-bda3/ch19-parametric, gelman-2013-bda3/ch22-finite, gelman-2013-philosophy/main, gelman-2020-workflow/main-p2, gelman-2020-workflow/main-p3, mcelreath-2020-rethinking/ch03-sampling, mcelreath-2020-rethinking/ch05-multivariate-p1, mcelreath-2020-rethinking/ch10-counting, mcelreath-2020-rethinking/ch11-monsters, murphy-2023-pml2/ch03-statistics-p3]
raw_ids: [Posterior predictive check]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# posterior-predictive-check

## Canon spine entry

- **Posterior predictive check** (bayesian): compare replicated data from the fitted model with observed data to find misfit (grad)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/appc-computation]] (pp. 595–596): replicated data in the same or new schools; test statistic = best minus second-best estimate
- [[gelman-2013-bda3/ch06-model]] (p. 143): compare observed data/test quantity with replications drawn from $p(y^{\rm rep}\mid y)$
- [[gelman-2013-bda3/ch07-evaluating]] (pp. 189–191): used with a problem-relevant test statistic (sample total, sample median)
- [[gelman-2013-bda3/ch08-modeling]] (pp. 198, 210): depends on the design via $y^{\rm rep}$; used with $T=\min_j y_{\mathrm{obs}\,1j}/n_j$
- [[gelman-2013-bda3/ch14-introduction]] (p. 363): compare a test statistic of observed data with its distribution under replicated data; here the proportion of outliers
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 386): used with the test quantity $T(y,\beta)$ on nationwide residuals
- [[gelman-2013-bda3/ch17-models]] (p. 439): recommended for arbitrarily assigned models
- [[gelman-2013-bda3/ch19-parametric]] (pp. 483–485): comparing observed data with model-based expected data from posterior draws, plus external validation
- [[gelman-2013-bda3/ch22-finite]] (p. 531): use test quantities that are not sufficient statistics, e.g. $T_{\min}$, $T_{\max}$ of within-person SDs
- [[gelman-2013-philosophy/main]] (p. 11): compare y with replicates y^rep from p(y^rep|y); p-value Pr(T(y^rep) > T(y) | y) [work fields: bayesian, analytic-philosophy]
- [[gelman-2020-workflow/main-p2]] (p. 30): simulate replicated data from the fitted model and compare with observed data or summaries, possibly by subgroup
- [[gelman-2020-workflow/main-p3]] (pp. 57, 62): used chain by chain to see that minor modes do not fit the data
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 67): compare simulated predictions with data, in several ways, to see how the model fails
- [[mcelreath-2020-rethinking/ch05-multivariate-p1]] (pp. 131–134): compare model-implied predictions with observed data, to find fit errors and failures (pp. 131–134); the author calls these "posterior prediction plots"
- [[mcelreath-2020-rethinking/ch10-counting]] (pp. 306–307): the postcheck of m10.6 revealed the department problem [as `Posterior predictive check`]
- [[mcelreath-2020-rethinking/ch11-monsters]] (p. 350): `postcheck(m11.5)` compares the model's predicted intervals with the data [as `Posterior predictive check`]
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 128): compare test statistics on replicated and real data

## Candidate bridges

- [structural-analogy] Posterior predictive check ↔ simulation-based fake-data checking (Bayesian workflow): simulate from the fitted model and look for discrepancies. — from [[gelman-2013-bda3/ch06-model]] (bayesian → bayesian)
- [structural-analogy] checking imputations against observed data (Fig. 18.2b) ↔ posterior predictive checks: systematic difference signals model misfit. — from [[gelman-2013-bda3/ch18-models]] (bayesian → bayesian)
- [metaphor] Randomization as discarding relevant information ↔ bayesian: modelling assumptions and prior/posterior predictive checks — both ask what a simplification throws away. — from [[jaynes-2003-probability/ch03-elementary]] (bayesian → bayesian)
- [structural-analogy] Mr A / Mr B: a persistent mismatch reveals a missing constraint ↔ Bayesian workflow: posterior predictive checks revealing misfit — from [[jaynes-2003-probability/ch11-discrete]] (bayesian → bayesian)
- [metaphor] Placebo checks ↔ prior/posterior predictive checks: testing a model against something it should or should not predict. — from [[murphy-2023-pml2/ch36-causality-p2]] (bayesian → bayesian)
- [structural-analogy] Testing a graph by vanishing partial regression coefficients ↔ posterior predictive checks: derive a checkable implication, compare with data. — from [[pearl-2016-primer/ch02-graphical]] (bayesian → bayesian)
