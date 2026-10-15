---
id: p-value
type: concept
fields: [bayesian, information-theory]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [jaynes-2003-probability/ch09-repetitive-p2, mackay-2003-information/ch37-bayesian, mcgrayne-2011-theory/ch03-many, murphy-2023-pml2/ch03-statistics-p1]
generated_by: build_kg.py
---

# p-value

## Definitions in the sources

### bayesian

- [[mcgrayne-2011-theory/ch03-many]] (p. 55): probability, under the hypothesis, of an outcome as extreme as observed [new]
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 81): tail probability of the test statistic under H₀, eq. (3.86) [new]

### information-theory

- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 303–304): tail probability P(χ²_obs); better reported than a fixed-level verdict [new]
- [[mackay-2003-information/ch37-bayesian]] (p. 457): the probability, under the null, of an outcome as or more extreme than the observed one; not the posterior probability of the null [new]

## Instances that use it

- [[p-value-y1-example]] — $y=1$, $\mathrm N(\theta,1)$: p-values 0.16/0.32 but posterior $\Pr(\theta>0)=84\%$ — from [[gelman-2013-bda3/ch04-asymptotics]]
- [[euro-coin-spin]] — 140 and 141 heads in 250 spins; p-values vs. likelihood ratios — from [[mackay-2003-information/ch03-more]]
- [[congress-p-value-example]] — p-value reasoning fallacy vs Bayes with LR=∞ — from [[murphy-2023-pml2/ch03-statistics-p1]]

## Candidate bridges

- [structural-analogy] Monte Carlo $p$-value with refitting ↔ parametric bootstrap: simulate from the fitted model, repeat the same fit on each simulation — from [[clauset-2009-powerlaw/main-p1]] (complex-systems → other)
- [structural-analogy] Posterior predictive p-value ↔ frequentist p-value: both compare a statistic with replications; the Bayesian one averages over $p(\theta\mid y)$ rather than fixing $\theta$. — from [[gelman-2013-bda3/ch06-model]] (bayesian → other)
- [structural-analogy] Marginal/cross-validation predictive p-values ↔ leave-one-out predictive checks (Chapter 7): same conditional predictive idea. — from [[gelman-2013-bda3/ch06-model]] (bayesian → other)
- [structural-analogy] posterior predictive p-value ↔ frequentist parametric-bootstrap goodness-of-fit: both simulate replicates from the fitted model, but the Bayesian one averages over the posterior and the bootstrap plugs in a point estimate (pp. 12, 15) — from [[gelman-2013-philosophy/main]] (bayesian → other)
- [structural-analogy] Reporting P-values/ψ rather than a reject/accept verdict ↔ bayesian: reporting full posterior evidence and leaving the decision to decision theory. — from [[jaynes-2003-probability/ch09-repetitive-p2]] (information-theory → bayesian)
