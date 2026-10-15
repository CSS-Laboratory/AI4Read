---
id: probability-weighting
type: concept
fields: [decision-game-theory]
n_sources: 4
tiers: [core]
grounding: digests
sources: [kahneman-1979-prospect/main, kahneman-2011-thinking/appb-choices, kahneman-2011-thinking/ch29-fourfold, kahneman-2011-thinking/ch30-rare]
raw_ids: [probability weighting]
canon_spine: decision-game-theory
generated_by: build_kg.py
---

# probability-weighting

## Canon spine entry

- **probability weighting** (decision-game-theory): overweighting small probabilities and underweighting moderate and large ones (grad)

## Definitions in the sources

### decision-game-theory

- [[kahneman-1979-prospect/main]] (pp. 275, 280–282): decision weights $\pi(p)$ replace probabilities: overweight low $p$, subcertain, not probabilities [as `probability weighting`]
- [[kahneman-2011-thinking/appb-choices]] (pdf 439): decision weights regressive: low probabilities overweighted, moderate and high underweighted, with category-boundary effects [as `probability weighting`]
- [[kahneman-2011-thinking/ch29-fourfold]] (pdf 304, 306): decision weights differ from probabilities: small ones overweighted, near-certain ones underweighted [as `probability weighting`]
- [[kahneman-2011-thinking/ch30-rare]] (pdf 315, 325): here, rare outcomes get a decision weight above their probability when they capture attention; underweighted or ignored otherwise [as `probability weighting`]

## Candidate bridges

- [structural-analogy] Importance weights $q/g$ and $S_{\rm eff}$ ↔ causal inference: inverse-probability weighting — reweighting draws from one distribution to represent another, with a few huge weights hurting precision. — from [[gelman-2013-bda3/ch10-introduction]] (bayesian → bayesian)
- [structural-analogy] $\pi(p)$ overweighting small $p$ and compressing mid-range $p$ ↔ decision-game-theory: probability weighting in cumulative/rank-dependent models — a nonlinear map from stated to effective probability. — from [[kahneman-1979-prospect/main]] (decision-game-theory → decision-game-theory)
- [structural-analogy] probability neglect ↔ prospect theory: probability weighting — both involve misweighted small probabilities. — from [[kahneman-2011-thinking/ch13-availability]] (decision-game-theory → other)
- [structural-analogy] inverse probability weighting ($1/P(x|z)$) ↔ Bayesian computation: importance sampling — both reweight samples drawn from one distribution to mimic another. — from [[pearl-2016-primer/ch03-effects]] (bayesian → bayesian)
