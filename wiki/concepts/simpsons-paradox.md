---
id: simpsons-paradox
type: concept
fields: [bayesian]
n_sources: 11
tiers: [core, deep]
grounding: digests
sources: [hernan-2020-whatif/ch08-selection, mcelreath-2020-rethinking/ch05-multivariate-p1, mcelreath-2020-rethinking/ch10-counting, pearl-2009-causality/main, pearl-2016-primer/ch01-preliminaries, pearl-2016-primer/ch02-graphical, pearl-2016-primer/ch03-effects, pearl-2018-bookofwhy/ch00-introduction, pearl-2018-bookofwhy/ch02-buccaneers, pearl-2018-bookofwhy/ch06-paradoxes, pearl-2018-bookofwhy/ch09-mediation-p1]
raw_ids: ["Simpson's paradox"]
canon_spine: bayesian
generated_by: build_kg.py
---

# simpsons-paradox

## Canon spine entry

- **Simpson's paradox** (bayesian): an association that reverses when data are split by a third variable; only causal assumptions say which answer to trust (HS)

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch08-selection]] (p. 115): margin note: result of ignoring common cause versus common effect
- [[mcelreath-2020-rethinking/ch05-multivariate-p1]] (p. 119): a confound can reverse the direction of an apparent association; only mentioned here
- [[mcelreath-2020-rethinking/ch10-counting]] (p. 309): association reversed within strata (department); the author says the intuition, not the logic, is violated
- [[pearl-2009-causality/main]] (p. 425): a statistical relation may reverse when further factors are included
- [[pearl-2016-primer/ch01-preliminaries]] (p. 1): an association in a whole population reverses in every subpopulation; which version is right depends on the causal story
- [[pearl-2016-primer/ch02-graphical]] (p. 44): only mentioned: Rule 3 will help resolve it in later chapters
- [[pearl-2016-primer/ch03-effects]] (p. 58): the graph tells which table to use; the adjustment formula resolves it
- [[pearl-2018-bookofwhy/ch00-introduction]] (pdf 24): named as a paradox revealing causal intuition
- [[pearl-2018-bookofwhy/ch02-buccaneers]] (pdf 73): Pearl calls the skull-data aggregation effect a case of it; Chapter 6 treats it
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 186–189): a trend in each subgroup that reverses in the pooled data, and so seems to contradict a causal belief; Pearl argues the causal diagram resolves it
- [[pearl-2018-bookofwhy/ch09-mediation-p1]] (pdf 283): Berkeley data [as `Simpson's paradox`]

## Instances that use it

- [[simpsons-paradox]] — Tables 8.1–8.3: the old treatment wins in each experiment but loses when pooled (pp. 260–261). The text does not use this name. — from [[jaynes-2003-probability/ch08-sufficiency]]
- [[death-penalty-simpsons-paradox]] — the data of exercise 28.4 — from [[mackay-2003-information/ch28-model]]
- [[berkeley-admissions]] — Simpson's paradox with competitive departments — from [[pearl-2009-causality/main]]
- [[exercise-cholesterol-age]] — continuous Simpson's paradox — from [[pearl-2018-bookofwhy/ch06-paradoxes]]
- [[berkeley-admissions-paradox]] — Simpson's paradox as a mediation question; Bickel vs. Kruskal — from [[pearl-2018-bookofwhy/ch09-mediation-p1]]

## Candidate bridges

- [structural-analogy] Simpson's paradox analogy (p. 5) ↔ statistics: aggregate trends can differ from subgroup trends — from [[argyle-2023-silicon/main-p1]] (llm → other)
- [structural-analogy] Pooling reversal (8.10) ↔ bayesian: Simpson's paradox and confounding by an unmodelled variable. — from [[jaynes-2003-probability/ch08-sufficiency]] (information-theory → bayesian)
- [structural-analogy] ruggedness slope reversing between groups (p. 212) ↔ Simpson's paradox: association changes sign when split by a third variable. — from [[mcelreath-2020-rethinking/ch07-interactions]] (bayesian → other)
- [structural-analogy] Department intercepts and the within-department comparison ↔ causal inference: adjusting for a confounder that changes the sign of an association (Simpson's paradox; the author points to causal thinking, p. 309) — from [[mcelreath-2020-rethinking/ch10-counting]] (bayesian → bayesian)
- [structural-analogy] Berkeley admissions ↔ Simpson's paradox / collider bias: the aggregate rate and the within-department rates disagree, and conditioning on $D$ is valid only if no hidden confounder exists. — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → other)
- [structural-analogy] Pearson's mixed skull populations ↔ Simpson's paradox: aggregation creates or reverses an association. — from [[pearl-2018-bookofwhy/ch02-buccaneers]] (bayesian → other)
- [structural-analogy] Mediation Fallacy ↔ Simpson's paradox: both show that stratifying can change the sign of an association, and only causal assumptions say which answer to trust. — from [[pearl-2018-bookofwhy/ch09-mediation-p1]] (bayesian → other)
