---
id: estimand
type: concept
fields: [bayesian]
n_sources: 3
tiers: [core]
grounding: digests
sources: [pearl-2018-bookofwhy/ch00-introduction, pearl-2018-bookofwhy/ch01-ladder, pearl-2018-bookofwhy/ch07-beyond]
generated_by: build_kg.py
---

# estimand

## Definitions in the sources

### bayesian

- [[pearl-2018-bookofwhy/ch00-introduction]] (pdf 20): formula from data quantities equivalent to the causal query, given the model [new]
- [[pearl-2018-bookofwhy/ch01-ladder]] (pdf 52): a recipe for answering a query from data; valid while the diagram is unchanged [new]
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 210): A do-free recipe for answering a causal query [new]

## Instances that use it

- [[clinical-trial-estimands]] — survival under two treatments; the outcome under the other treatment is unobserved — from [[gelman-2013-bda3/ch01-probability]]
- [[slovenia-plebiscite-survey]] — "don't know" as missing data, estimand α, EM/SEM/data augmentation, actual 88.5% — from [[gelman-2013-bda3/ch18-models]]
- [[drug-sex-overlap]] — a drug given only to males makes the estimand non-identifiable — from [[murphy-2023-pml2/ch36-causality-p1]]
- [[drug-lifespan-example]] — running $D$, $L$, $Z$ example for do, estimand, confounding — from [[pearl-2018-bookofwhy/ch00-introduction]]

## Candidate bridges

- [structural-analogy] unobserved outcome under the treatment not received (p. 4) ↔ causal inference: potential outcomes and the fundamental problem. The text only notes it as an estimand needing inference. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → bayesian)
- [metaphor] LD50 summarized conditional on $\beta>0$ ↔ causal/estimand definition: a quantity is only defined in part of parameter space, so report the probability of that region plus the conditional distribution. — from [[gelman-2013-bda3/ch03-introduction]] (bayesian → bayesian)
- [structural-analogy] Finite-population vs superpopulation sd ↔ causal inference (sample vs population estimand) — whether you care about the units at hand or the population they represent. — from [[gelman-2013-bda3/ch15-hierarchical]] (bayesian → unspecified)
- [same-math] DiD estimation after taking $Y_1-Y_0$ ↔ adjustment-based ATT estimation (36.4.5.3) — the source says the statistical estimand is identical. — from [[murphy-2023-pml2/ch36-causality-p2]] (bayesian → unspecified)
- [structural-analogy] estimand as a recipe fixed before data ↔ bayesian: model specified before fitting; the likelihood and prior are chosen before data arrive. — from [[pearl-2018-bookofwhy/ch00-introduction]] (bayesian → bayesian)
- [metaphor] adaptability of estimands ↔ bayesian: reusing structure across populations resembles hierarchical sharing, but the text does not say this. — from [[pearl-2018-bookofwhy/ch00-introduction]] (bayesian → bayesian)
