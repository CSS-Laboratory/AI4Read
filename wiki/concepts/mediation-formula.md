---
id: mediation-formula
type: concept
fields: [bayesian]
n_sources: 4
tiers: [core]
grounding: digests
sources: [hernan-2020-whatif/ch23-causal, pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch09-mediation-p1, pearl-2018-bookofwhy/ch09-mediation-p2]
generated_by: build_kg.py
---

# mediation-formula

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch23-causal]] (p. 324): $\sum_m E[Y|A=1,M=m]\Pr[M=m|A=0]$; identifies the cross-world mean under assumptions [new]
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 122–123): Eqs. 4.51–4.52 for natural effects without confounding (new)
- [[pearl-2018-bookofwhy/ch09-mediation-p1]] (pdf 290, 292): counterfactual-free expression for NDE (p. 290) and, assuming no M–Y confounding, for NIE (p. 292), estimable from observational data. Named but not stated here [new]
- [[pearl-2018-bookofwhy/ch09-mediation-p2]] (pdf 301–302): Eq. 9.5 and its NDE twin: estimates natural effects from observed data under graph assumptions [new]

## Candidate bridges

- [same-math] mediation formula as a g-formula ↔ potential outcomes: a standardization (mixing over $\Pr[M|A=0]$) of a conditional mean. — from [[hernan-2020-whatif/ch23-causal]] (bayesian → other)
