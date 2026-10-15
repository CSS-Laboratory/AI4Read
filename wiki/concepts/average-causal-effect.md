---
id: average-causal-effect
type: concept
fields: [bayesian, political-science]
n_sources: 4
tiers: [core]
grounding: digests
sources: [grimmer-2022-textasdata/ch24-causal, hernan-2020-whatif/ch01-definition, holland-1986-statistics/main, pearl-2016-primer/ch03-effects]
generated_by: build_kg.py
---

# average-causal-effect

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch01-definition]] (pp. 5–6): present if $E[Y^{a=1}]\neq E[Y^{a=0}]$; the contrast $E[Y^{a=1}]-E[Y^{a=0}]$ equals the mean of the individual effects [new]
- [[holland-1986-statistics/main]] (p. 947): $T=E(Y_t-Y_c)=E(Y_t)-E(Y_c)$ over $U$ [new]
- [[pearl-2016-primer/ch03-effects]] (p. 56): $P(y|do(x{=}1))-P(y|do(x{=}0))$ (ACE) [new]

### political-science

- [[grimmer-2022-textasdata/ch24-causal]] (p. 410): $\bar y^T-\bar y^C$, the mean of $y_i(1)-y_i(0)$ (p. 410) (new)
