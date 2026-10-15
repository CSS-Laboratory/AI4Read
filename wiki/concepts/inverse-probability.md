---
id: inverse-probability
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [mcgrayne-2011-theory/ch01-causes, mcgrayne-2011-theory/ch03-many, pearl-2018-bookofwhy/ch03-evidence]
generated_by: build_kg.py
---

# inverse-probability

## Definitions in the sources

### bayesian

- [[mcgrayne-2011-theory/ch01-causes]] (p. 6, p. 12): reasoning from observed effects to their probable cause; the old name for Bayes' rule [new]
- [[mcgrayne-2011-theory/ch03-many]] (p. 54): the chapter's term for reasoning back from data to causes; Chrystal's 1891 obituary names it (p. 37) and Jeffreys's earthquake problem is called a classic case [new]
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 97): Bayes-era name for P(cause | effect), the hard direction [new]

## Instances that use it

- [[eleven-urns]] — inverse probability, posterior table, prediction 0.333 — from [[mackay-2003-information/ch02-probability]]
- [[binary-file-compression]] — compression as inverse probability; 29 ones and 271 zeros — from [[mackay-2003-information/ch02-probability]]

## Candidate bridges

- [structural-analogy] Importance weights $q/g$ and $S_{\rm eff}$ ↔ causal inference: inverse-probability weighting — reweighting draws from one distribution to represent another, with a few huge weights hurting precision. — from [[gelman-2013-bda3/ch10-introduction]] (bayesian → bayesian)
- [structural-analogy] IP weighting by $1/\Pr[C=0|L,A]$ ↔ Monte Carlo: reweighting samples by inverse probability to mimic another distribution. — from [[hernan-2020-whatif/ch08-selection]] (bayesian → other:statistics)
- [structural-analogy] inverse probability weighting ($1/P(x|z)$) ↔ Bayesian computation: importance sampling — both reweight samples drawn from one distribution to mimic another. — from [[pearl-2016-primer/ch03-effects]] (bayesian → bayesian)
