---
id: effect-modification
type: concept
fields: [bayesian]
n_sources: 5
tiers: [core]
grounding: digests
sources: [hernan-2020-whatif/ch02-randomized, hernan-2020-whatif/ch04-effect, hernan-2020-whatif/ch05-interaction, hernan-2020-whatif/ch06-graphical, hernan-2020-whatif/ch12-ip]
generated_by: build_kg.py
---

# effect-modification

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch02-randomized]] (p. 18): stratum-specific causal effects differ across levels of $L$ [new]
- [[hernan-2020-whatif/ch04-effect]] (p. 48): average causal effect varies across levels of a pre-treatment $V$; depends on the effect measure [new]
- [[hernan-2020-whatif/ch05-interaction]] (p. 62): the effect of A varies across levels of V, where V is not intervened on (new)
- [[hernan-2020-whatif/ch06-graphical]] (pp. 87–88): effect varies across levels of $V$; causal versus surrogate modifiers [new]
- [[hernan-2020-whatif/ch12-ip]] (p. 171–172): treatment effect varying across levels of $V$; in an MSM, tested by a product term [new]

## Instances that use it

- [[hepatitis-history-confounder]] — mismeasured confounder and apparent effect modification — from [[hernan-2020-whatif/ch09-measurement]]

## Candidate bridges

- [structural-analogy] Effect modification by V ↔ hierarchical models: group-specific effects of A varying across levels of V. — from [[hernan-2020-whatif/ch05-interaction]] (bayesian → other)
