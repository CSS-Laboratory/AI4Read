---
id: g-formula
type: concept
fields: [bayesian]
n_sources: 2
tiers: [core]
grounding: digests
sources: [hernan-2020-whatif/ch21-g, hernan-2020-whatif/ch23-causal]
generated_by: build_kg.py
---

# g-formula

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch21-g]] (p. 278, 280): outcome mean standardized to the confounder distribution, each factor conditioned on past treatment and covariate history [new]
- [[hernan-2020-whatif/ch23-causal]] (p. 326): identification formula needing exchangeability and consistency. Here positivity is shown sufficient, not necessary [new]

## Instances that use it

- [[nhefs-smoking-cessation]] — 1629 smokers, 120-month follow-up; crude survival 76.2% vs 82.0%, IP-weighted adjusted 80.7% vs 80.5% (g-formula 80.4% vs 80.6%) — from [[hernan-2020-whatif/ch17-causal]]
- [[sequentially-randomized-experiment-table-21-1]] — two-time-point dataset where g-formula, IP weighting and g-estimation all give 60 for both strategies — from [[hernan-2020-whatif/ch21-g]]
- [[front-door-formula-big-g-proof]] — front door formula derived from the big g-formula — from [[hernan-2020-whatif/ch21-g]]
- [[g-null-paradox-example]] — parametric g-formula that, under feedback and the sharp null, might theoretically falsely reject the null (p. 286); a theoretical argument, not a numerical example — from [[hernan-2020-whatif/ch21-g]]

## Candidate bridges

- [structural-analogy] Parametric g-formula ↔ bayesian: posterior predictive averaging — model outcome given covariates, then average over the covariate distribution. — from [[hernan-2020-whatif/ch17-causal]] (bayesian → bayesian)
- [structural-analogy] g-formula simulation of $(Y^{\bar a},\bar L^{\bar a})$ and Monte Carlo of Technical Point 21.9 ↔ Bayesian computation: ancestral sampling from a sequential generative model, drawing each $L_k$ given the history set by the strategy. — from [[hernan-2020-whatif/ch21-g]] (bayesian → bayesian)
- [same-math] mediation formula as a g-formula ↔ potential outcomes: a standardization (mixing over $\Pr[M|A=0]$) of a conditional mean. — from [[hernan-2020-whatif/ch23-causal]] (bayesian → other)
- [structural-analogy] the *The $F$ is $G$* formula ↔ analytic-philosophy canon: theory of descriptions (canon link; not stated in this unit). — from [[magnus-2025-forallx/ch100-quick]] (analytic-philosophy → analytic-philosophy)
