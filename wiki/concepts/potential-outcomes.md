---
id: potential-outcomes
type: concept
fields: [bayesian, political-science]
n_sources: 23
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch08-modeling, gelman-2013-bda3/ch14-introduction, grimmer-2022-textasdata/ch24-causal, hernan-2020-whatif/ch01-definition, hernan-2020-whatif/ch02-randomized, hernan-2020-whatif/ch03-observational, hernan-2020-whatif/ch05-interaction, hernan-2020-whatif/ch07-confounding, hernan-2020-whatif/ch08-selection, hernan-2020-whatif/ch12-ip, hernan-2020-whatif/ch14-g, hernan-2020-whatif/ch16-instrumental, hernan-2020-whatif/ch19-time, hernan-2020-whatif/ch20-treatment, hernan-2020-whatif/ch21-g, hernan-2020-whatif/ch22-target, hernan-2020-whatif/ch23-causal, holland-1986-statistics/main, murphy-2023-pml2/ch04-graphical-p3, murphy-2023-pml2/ch36-causality-p1, pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch04-confounding, pearl-2018-bookofwhy/ch08-counterfactuals]
raw_ids: [Potential outcomes]
canon_spine: bayesian
generated_by: build_kg.py
---

# potential-outcomes

## Canon spine entry

- **Potential outcomes** (bayesian): each unit has an outcome under each possible treatment; a causal effect is their difference (UG)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch08-modeling]] (pp. 198, 214): complete data hold outcomes under all treatments
- [[gelman-2013-bda3/ch14-introduction]] (p. 359): $y^I_{\text{complete}}$ and $y^O_{\text{complete}}$ define the incumbency advantage
- [[hernan-2020-whatif/ch01-definition]] (p. 4): $Y^{a}$: the outcome that would be observed under treatment value $a$; called counterfactual when it may not occur
- [[hernan-2020-whatif/ch02-randomized]] (pp. 13, 15): $Y^a$, the outcome had treatment been $a$; here, it can be thought of as a fixed characteristic of the person existing before treatment is assigned
- [[hernan-2020-whatif/ch03-observational]] (p. 33): counterfactuals $Y^a$ taken as primitives; observed $Y=AY^{a=1}+(1-A)Y^{a=0}$ for binary $A$
- [[hernan-2020-whatif/ch05-interaction]] (p. 61): counterfactual outcomes $Y^{a}$, $Y^{a,e}$; used with consistency $Y=Y^{A,E}$
- [[hernan-2020-whatif/ch07-confounding]] (p. 91): counterfactual $Y^a$ used throughout
- [[hernan-2020-whatif/ch08-selection]] (p. 116): counterfactual $Y^{a,c=0}$ for the contrast with censoring removed
- [[hernan-2020-whatif/ch12-ip]] (p. 163, 173): $Y^a$ and $Y^{a,c=0}$ as the target quantities
- [[hernan-2020-whatif/ch14-g]] (p. 194): $Y^{a=1}$ and $Y^{a=0}$; $H(\psi^\dagger)$ is a candidate for $Y^{a=0}$
- [[hernan-2020-whatif/ch16-instrumental]] (pp. 210, 217): counterfactual notation $Y^{z,a}$, $A^z$ used throughout
- [[hernan-2020-whatif/ch19-time]] (p. 256): counterfactual $Y^g$ indexed by strategy
- [[hernan-2020-whatif/ch20-treatment]] (p. 268): strategy effects defined as $\mathrm{E}[Y^{\bar a}]$ contrasts
- [[hernan-2020-whatif/ch21-g]] (p. 277): counterfactuals $Y^{\bar a}$ for strategies
- [[hernan-2020-whatif/ch22-target]] (pp. 310–311): counterfactual contrasts $D_k^{z,\bar c}$, $D_k^{g,\bar c}$ define each effect
- [[hernan-2020-whatif/ch23-causal]] (p. 323): the nested notation $Y^{a,m}$ and $M^{a}$ [as `Potential outcomes`]
- [[holland-1986-statistics/main]] (p. 946–947): each unit has $Y_t(u)$ and $Y_c(u)$; the effect is their difference
- [[murphy-2023-pml2/ch04-graphical-p3]] (p. 216): $Y^{a'}$: outcome had action $a'$ been taken
- [[murphy-2023-pml2/ch36-causality-p1]] (pp. 1192–1194): $Y_i(a)=f_Y(G_i,H_i,a,\xi_{3,i})$; equivalent to graphs, with different practical strengths
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 125–126): $Y_x(u)$ as a unit's response under treatment $x$; the author says it is equivalent to the structural account
- [[pearl-2018-bookofwhy/ch04-confounding]] (pdf 147): Rubin's counterfactual variables, both treatments for each person
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 246): $Y_x(u)$, value $Y$ would take for unit $u$ had $X=x$; assumed to have objective reality

### political-science

- [[grimmer-2022-textasdata/ch24-causal]] (p. 410): each unit has an outcome under each treatment; only one is observed (p. 410) (new)

## Candidate bridges

- [structural-analogy] unobserved outcome under the treatment not received (p. 4) ↔ causal inference: potential outcomes and the fundamental problem. The text only notes it as an estimand needing inference. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → bayesian)
- [structural-analogy] Predicting outcomes under each candidate incentive (p. 243) ↔ potential outcomes: the decision problem needs outcomes under each option, though only one is ever realized. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → other)
- [structural-analogy] Mixture indicators $z$ as missing data ↔ missing-data and potential-outcomes inference (canon): both treat unobserved quantities as unknowns to impute or average over. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → other)
- [structural-analogy] individual effects unidentified because the other potential outcome is missing ↔ Bayesian: unobserved quantities treated as unknowns with a prior. — from [[hernan-2020-whatif/ch01-definition]] (bayesian → bayesian)
- [structural-analogy] Three-block dataset with missing $Y$ imputed by a model ↔ Potential outcomes: filling in the unobserved outcome under each treatment (the missing-data view of causal inference). — from [[hernan-2020-whatif/ch13-standardization]] (bayesian → other)
- [same-math] mediation formula as a g-formula ↔ potential outcomes: a standardization (mixing over $\Pr[M|A=0]$) of a conditional mean. — from [[hernan-2020-whatif/ch23-causal]] (bayesian → other)
- [same-math] Holland's $(Y_t, Y_c)$ and $T=E(Y_t-Y_c)$ ↔ bayesian/causal canon: potential outcomes and the average treatment effect — same definitions. — from [[holland-1986-statistics/main]] (bayesian → bayesian)
- [metaphor] The Fundamental Problem ↔ missing-data problem: each unit has one unobserved potential outcome. — from [[holland-1986-statistics/main]] (bayesian → other)
- [structural-analogy] Missing neocortex values as parameters ↔ causal inference: unobserved potential outcomes — both treat unobserved quantities as unknowns inferred from a model. — from [[mcelreath-2020-rethinking/ch14-missing]] (bayesian → bayesian)
- [same-math] SCM ↔ potential outcomes (causal inference): the author says the two frameworks are mathematically equivalent. — from [[murphy-2023-pml2/ch04-graphical-p3]] (bayesian → bayesian)
- [structural-analogy] Causal-impact counterfactual forecast ↔ potential outcomes: treated unit's untreated outcome is the missing quantity, here predicted by a model. — from [[murphy-2023-pml2/ch29-state-p3]] (bayesian → other)
- [structural-analogy] Randomization in user-study design "marginalizes over" confounds ↔ causal inference: randomized assignment makes the assignment mechanism independent of potential outcomes (canon link; not stated in this unit). — from [[murphy-2023-pml2/ch33-interpretability]] (bayesian → bayesian)
- [same-math] Potential outcomes with consistency ↔ potential outcomes framework in canon: $Y_x(u)$ and $Y=XY_1+(1-X)Y_0$. — from [[pearl-2016-primer/ch04-counterfactuals]] (bayesian → other)
- [structural-analogy] Table 4.4 randomization (missing entries independent of potential outcomes) ↔ missing-data view of causal inference: unobserved potential outcomes missing at random. — from [[pearl-2016-primer/ch04-counterfactuals]] (bayesian → bayesian)
- [structural-analogy] Vaccination counterfactual (everyone unvaccinated vs actual) ↔ potential outcomes: outcomes of the same units under different treatments. — from [[pearl-2018-bookofwhy/ch01-ladder]] (bayesian → other)
- [structural-analogy] Instrument as natural experiment ↔ potential outcomes/assignment mechanism: Z behaves like random assignment to X (Snow's "ready-made" experiment). — from [[pearl-2018-bookofwhy/ch07-beyond]] (bayesian → other)
- [same-math] Back-door formula (Eq. 7.2) ↔ standardization over covariate strata in potential-outcomes adjustment: a weighted average of stratum-specific conditional probabilities by the covariate distribution. — from [[pearl-2018-bookofwhy/ch07-beyond]] (bayesian → other)
