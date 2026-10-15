---
id: regression-toward-the-mean
type: concept
fields: [decision-game-theory, economics-finance]
n_sources: 3
tiers: [core]
grounding: digests
sources: [kahneman-2011-thinking/appa-judgment, thaler-2015-misbehaving/ch22-does, tversky-1974-heuristics/main]
raw_ids: [regression toward the mean]
generated_by: build_kg.py
---

# regression-toward-the-mean

## Definitions in the sources

### decision-game-theory

- [[kahneman-2011-thinking/appa-judgment]] (pdf 417): values selected for being extreme on one measure are usually less extreme on another [new]
- [[tversky-1974-heuristics/main]] (p. 1126): extreme scores on one measure tend to be less extreme on a second equivalent measure [new]

### economics-finance

- [[thaler-2015-misbehaving/ch22-does]] (p. 175): extreme outcomes tend to be followed by less extreme ones; here the proposed source of Loser/Winner return reversal [as `regression toward the mean`; new]

## Candidate bridges

- [structural-analogy] Regression toward the mean ↔ statistics: shrinkage toward the mean under noisy measurement — extreme observations include noise that does not repeat. — from [[kahneman-2011-thinking/appa-judgment]] (decision-game-theory → other)
- [structural-analogy] Pooling across intercepts and slopes via correlation ↔ regression toward the mean in two dimensions — from [[mcelreath-2020-rethinking/ch13-adventures]] (bayesian → unspecified)
- [structural-analogy] Success = talent + luck, with regression toward the mean ↔ partial pooling/shrinkage in hierarchical models: noisy extreme values are pulled toward the average. — from [[pearl-2018-bookofwhy/ch02-buccaneers]] (bayesian → other)
- [structural-analogy] Regression toward the mean here ↔ statistics: extreme observations of a noisy variable move back toward the average. This is used as a story for prices, not a derived result. — from [[thaler-2015-misbehaving/ch22-does]] (economics-finance → other)
- [same-math] Regression toward the mean ↔ statistics of correlation: the regression of $Y$ on $X$ when $r<1$ gives the shrinkage the text describes. — from [[tversky-1974-heuristics/main]] (decision-game-theory → other)
