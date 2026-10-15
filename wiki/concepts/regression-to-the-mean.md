---
id: regression-to-the-mean
type: concept
fields: [decision-game-theory, bayesian, information-theory]
n_sources: 6
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch04-asymptotics, jaynes-2003-probability/ch07-central-p2, kahneman-2011-thinking/ch17-regression, kahneman-2011-thinking/ch18-taming, kahneman-2011-thinking/ch19-illusion, pearl-2018-bookofwhy/ch02-buccaneers]
generated_by: build_kg.py
---

# regression-to-the-mean

## Definitions in the sources

### decision-game-theory

- [[kahneman-2011-thinking/ch17-regression]] (pdf 172, 178): extreme results tend to be followed by less extreme ones when luck or imperfect correlation is involved [new]
- [[kahneman-2011-thinking/ch18-taming]] (pdf 185): extreme outcomes tend to be followed by less extreme ones; intuitive predictions ignore this [new]
- [[kahneman-2011-thinking/ch19-illusion]] (pdf 202): extreme luck-aided gaps shrink on average later [new]

### bayesian

- [[gelman-2013-bda3/ch04-asymptotics]] (p. 95): expected daughter height lies between mother's height and the population mean [new]
- [[pearl-2018-bookofwhy/ch02-buccaneers]] (pdf 61–62): extreme values tend to be followed by less extreme ones; statistical, not causal; symmetric in time [new]

### information-theory

- [[jaynes-2003-probability/ch07-central-p2]] (p. 228): Galton's "reversion", the systematic counter-drift balancing spreading [new]

## Instances that use it

- [[galton-regression-to-the-mean]] — sons of tall/short fathers closer to the mean; shrinkage as a basis of multilevel models — from [[mcelreath-2020-rethinking/ch04-linear-p2]]
- [[sophomore-slump]] — regression to the mean read as a causal story — from [[pearl-2018-bookofwhy/ch02-buccaneers]]

## Candidate bridges

- [same-math] straight-line slope ρ·std(y)/std(x) ↔ statistics: simple linear regression coefficient and "regression to the mean" (exercise 13.2). — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → other)
- [structural-analogy] regressive decision weights ↔ regression to the mean: stated probabilities map to weights that are pulled toward the middle, but this is a psychological curve, not a statistical effect. — from [[kahneman-2011-thinking/appb-choices]] (decision-game-theory → other)
- [structural-analogy] Last year's extreme counties need not be extreme this year ↔ regression to the mean (a term this unit does not use). — from [[kahneman-2011-thinking/ch10-law]] (decision-game-theory → unspecified)
- [same-math] Firm gaps shrinking (pdf 202) ↔ statistics: regression to the mean when a measure includes a luck component. — from [[kahneman-2011-thinking/ch19-illusion]] (decision-game-theory → other)
- [structural-analogy] Galton's regression to the mean / shrinkage ↔ bayesian: partial pooling, where noisy estimates are pulled toward a common mean (p. 92 links it to multilevel models) — from [[mcelreath-2020-rethinking/ch04-linear-p2]] (bayesian → bayesian)
