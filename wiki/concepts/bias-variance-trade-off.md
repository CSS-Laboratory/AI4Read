---
id: bias-variance-trade-off
type: concept
fields: [bayesian, decision-game-theory]
fields_strong: [bayesian]
n_sources: 3
n_works: 3
tiers: [core]
grounding: digests
sources: [hernan-2020-whatif/ch11-model, kahneman-2011-thinking/ch18-taming, mcelreath-2020-rethinking/ch06-overfitting-p1]
aliases: [bias-variance-tradeoff]
canon_spine: [decision-game-theory]
generated_by: build_kg.py
---

# bias-variance-trade-off

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `bias-variance-tradeoff` — 2 digest(s)

## Canon spine entry

- **bias–variance trade-off** (decision-game-theory): simpler models err systematically but vary less across samples, and can predict better (grad)

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch11-model]] (p. 159): protection against misspecification bias costs wider confidence intervals [alias `bias-variance-tradeoff`; new]
- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 174): alternative name for the under/overfitting tension; "not exactly the same" [alias `bias-variance-tradeoff`; new]

### decision-game-theory

- [[kahneman-2011-thinking/ch18-taming]] (pdf 187, 189): here only the idea that unbiased forecasts are smaller-error but less extreme (pdf 187, 189); the term itself is not used [weak: not really used in this unit]

## Instances that use it

- [[linear-vs-quadratic-fit-at-a90]] — estimates 216.9 vs 197.1 at $A=90$ with different CI widths; shows the bias–variance trade-off — from [[hernan-2020-whatif/ch11-model]]

## Candidate bridges

- [structural-analogy] Bias–variance trade-off in choosing the number of parameters ↔ bayesian: Bayesian Occam's razor and cross-validation for model choice. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [structural-analogy] Small samples being more variable ↔ bias–variance trade-off: sample size controls how much results vary across samples. — from [[kahneman-2011-thinking/ch10-law]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Base-rate neglect ↔ bias–variance trade-off: relying only on the vivid specific evidence over-weights noisy data, while a prior stabilises estimates. — from [[kahneman-2011-thinking/ch14-tom]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Talent + luck regression ↔ decision-game-theory: bias–variance trade-off — shrinking noisy estimates toward the mean can predict better. — from [[kahneman-2011-thinking/ch17-regression]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Regress toward the mean for a small sample ↔ bias–variance trade-off: shrinking noisy estimates helps forecasts — from [[kahneman-2011-thinking/ch18-taming]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Equal weights beating optimal regression on new cases ↔ bias–variance trade-off: a simpler model can predict better because it is less affected by sampling accidents. — from [[kahneman-2011-thinking/ch21-intuitions]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Algorithms beat humans in noisy environments by using weak cues consistently ↔ statistics: bias–variance trade-off (consistent simple rules versus noisy flexible judgment) — from [[kahneman-2011-thinking/ch22-expert]] (decision-game-theory → other:statistics)
- [structural-analogy] Partial pooling ↔ bias–variance trade-off in estimation: the pooled estimate adds bias but cuts variance, most for noisy small clusters. — from [[mcelreath-2020-rethinking/ch12-multilevel]] (bayesian → other:bias-variance-trade-off)
- [structural-analogy] Double descent via weight norm ↔ classical bias/variance trade-off — from [[prince-2023-udl/ch20-does]] (llm → unspecified)
- [structural-analogy] ToMnet vs BIRL ↔ statistics: bias/variance trade-off between a fixed generative model and a flexible learner (pdf 4) — from [[rabinowitz-2018-machine-tom/main]] (theory-of-mind → other:statistics)
- [metaphor] randomizing a threat to limit failure cost ↔ bias–variance trade-off: accepting a weaker, more moderate policy to reduce the cost of error. — from [[schelling-1960-conflict/ch07-randomization]] (decision-game-theory → decision-game-theory)
