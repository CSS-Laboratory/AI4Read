---
id: base-rate-neglect
type: concept
fields: [decision-game-theory, bayesian]
fields_strong: [decision-game-theory, bayesian]
n_sources: 12
n_works: 5
tiers: [core]
grounding: digests
sources: [kahneman-2011-thinking/appa-judgment, kahneman-2011-thinking/ch07-machine, kahneman-2011-thinking/ch14-tom, kahneman-2011-thinking/ch16-causes, kahneman-2011-thinking/ch20-illusion, kahneman-2011-thinking/ch23-outside, mcelreath-2020-rethinking/ch03-sampling, mcgrayne-2011-theory/app-appendixes, mcgrayne-2011-theory/ch16-eureka, mcgrayne-2011-theory/ch17-rosetta, pearl-2018-bookofwhy/ch03-evidence, tversky-1974-heuristics/main]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# base-rate-neglect

## Canon spine entry

- **Base-rate neglect** (bayesian): ignoring the prior (base rate) when judging the probability of a hypothesis from evidence, e.g., a positive medical test (HS)

## Definitions in the sources

### decision-game-theory

- [[kahneman-2011-thinking/appa-judgment]] (pdf 411–412): ignoring prior probabilities when a description is given, even a worthless one [new]
- [[kahneman-2011-thinking/ch07-machine]] (pdf 87): a vivid description crowds out the statistical fact about group sizes [new]
- [[kahneman-2011-thinking/ch14-tom]] (pdf 147, 149): ignoring base rates once a description of the individual is available [new]
- [[kahneman-2011-thinking/ch16-causes]] (pdf 164): ignoring how common a category is when judging a case [new]
- [[kahneman-2011-thinking/ch20-illusion]] (pdf 206–207, 210): general statistics are often not applied to the individual case [new]
- [[kahneman-2011-thinking/ch23-outside]] (pdf 239, 241): ignoring class statistics when case information is available [new]
- [[tversky-1974-heuristics/main]] (p. 1124–1125): ignoring prior frequency of outcomes when a description is available [new]

### bayesian

- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 49): a low base rate makes most positives false even for an accurate test
- [[mcgrayne-2011-theory/app-appendixes]] (p. 255): surprise that a positive test on an accurate screen means low risk; the text does not use the term [weak: not really used in this unit]
- [[mcgrayne-2011-theory/ch16-eureka]] (p. 227): implicit in the screening cases: for PSA, the disease is so rare that almost everyone with a positive result lacks the cancer
- [[mcgrayne-2011-theory/ch17-rosetta]] (pp. 241–242): rare targets such as terrorists require an extremely accurate definition, or many innocent people are flagged
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 105): surprise at the mammogram result, arising from confusing forward and inverse probability

## Instances that use it

- [[steve-the-librarian]] — base-rate neglect — from [[kahneman-2011-thinking/ch07-machine]]

## Candidate bridges

- [structural-analogy] converting a score into a match probability via prior and likelihood (record linkage) ↔ base-rate neglect: the prior proportion of true matches matters for the posterior. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → decision-game-theory)
- [structural-analogy] Discrete Bayes update after a test (p. 245) ↔ base-rate neglect: the prior (0.9) and the test's error rates combine by Bayes' theorem. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → decision-game-theory)
- [same-math] Base-rate neglect ↔ Bayes' rule: posterior odds = prior odds × likelihood ratio; the 5.44 factor is the ratio of the prior odds in the two conditions, $(7/3)\div(3/7)=(.7/.3)^2$. — from [[kahneman-2011-thinking/appa-judgment]] (decision-game-theory → bayesian)
- [structural-analogy] Base-rate neglect ↔ bias–variance trade-off: relying only on the vivid specific evidence over-weights noisy data, while a prior stabilises estimates. — from [[kahneman-2011-thinking/ch14-tom]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Lawyer's mistake (P(murder | beater) vs. P(husband did it | murder, beater)) ↔ bayesian: base-rate neglect, ignoring how common alternative explanations are. — from [[mackay-2003-information/ch03-more]] (information-theory → bayesian)
- [structural-analogy] Coleman exam and strong department prior ↔ base-rate neglect: ignoring the prior would overweight a weak test — from [[mcgrayne-2011-theory/ch11-business]] (bayesian → decision-game-theory)
- [same-math] screening results (HIV, PSA) ↔ Bayes' theorem and base-rate neglect: a positive result is weighed against disease prevalence. — from [[mcgrayne-2011-theory/ch16-eureka]] (bayesian → bayesian)
