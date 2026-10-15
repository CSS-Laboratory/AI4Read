---
id: sensitivity-analysis
type: concept
fields: [bayesian, political-science]
n_sources: 8
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch06-model, gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch17-models, grimmer-2022-textasdata/ch22-principles, hernan-2020-whatif/ch13-standardization, mcelreath-2020-rethinking/ch09-big, murphy-2023-pml2/ch03-statistics-p2, pearl-2018-bookofwhy/ch05-smoke]
generated_by: build_kg.py
---

# sensitivity-analysis

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch06-model]] (p. 141): how much posterior inferences change under other reasonable models [new]
- [[gelman-2013-bda3/ch07-evaluating]] (p. 185): fit several reasonable models and see how inferences change [new]
- [[gelman-2013-bda3/ch17-models]] (p. 436, 439): varying distributional assumptions (via a hyperparameter $\phi$) and tracking posterior changes in estimands [new]
- [[hernan-2020-whatif/ch13-standardization]] (p. 183): re-analysis under varied assumptions to see how estimates change [new]
- [[mcelreath-2020-rethinking/ch09-big]] (p. 287): varying assumptions and reporting all results [new]
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 100): assessing the influence of the prior on the posterior [new]
- [[pearl-2018-bookofwhy/ch05-smoke]] (pdf 166): ask how strong an omitted causal link must be to explain the data, then judge plausibility [new]

### political-science

- [[grimmer-2022-textasdata/ch22-principles]] (p. 375): assume plausible confounding and assess how large it must be to change a finding [new]

## Instances that use it

- [[eight-schools]] — model checks and sensitivity analysis of the SAT coaching model — from [[gelman-2013-bda3/ch06-model]]
- [[spouse-smoking-unmeasured-confounding]] — example where $\alpha_1\ne0$, motivating the sensitivity analysis — from [[hernan-2020-whatif/ch14-g]]

## Candidate bridges

- [same-math] $dG/G=S\,dP/P$ ↔ sensitivity analysis: the relative-change (logarithmic) derivative of a closed-loop function with respect to a parameter. — from [[astrom-2021-feedbacksystems/ch13-robust]] (control-theory → other)
- [structural-analogy] Static sensitivity analysis (reweight posterior draws by new-to-old prior ratio) ↔ importance sampling: the same reweighting idea, applied to prior changes (p. 35). — from [[gelman-2020-workflow/main-p2]] (bayesian → other)
- [metaphor] Sensitivity analysis for unmeasured confounding ↔ prior sensitivity: rerunning an analysis under several assumptions about what cannot be checked. — from [[hernan-2020-whatif/ch07-confounding]] (bayesian → other)
- [structural-analogy] Testing a known non-zero $\alpha_1$ for sensitivity analysis ↔ Bayesian inference: a prior or fixed value for a bias parameter, with results shown across its range. — from [[hernan-2020-whatif/ch14-g]] (bayesian → bayesian)
