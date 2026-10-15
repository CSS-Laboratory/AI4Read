---
id: posterior-predictive
type: concept
fields: [linear-algebra, llm]
n_sources: 2
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch09-linear, xie-2022-icl/main]
generated_by: build_kg.py
---

# posterior-predictive

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch09-linear]] (p. 308): $\mathcal N(\phi^\top m_N,\phi^\top S_N\phi+\sigma^2)$ [new]

### llm

- [[xie-2022-icl/main]] (p. 2): $p(\text{output}|\text{prompt})$ with the latent concept marginalized out [new]

## Candidate bridges

- [structural-analogy] Posterior predictive p-value ↔ frequentist p-value: both compare a statistic with replications; the Bayesian one averages over $p(\theta\mid y)$ rather than fixing $\theta$. — from [[gelman-2013-bda3/ch06-model]] (bayesian → other)
- [structural-analogy] Posterior predictive check ↔ simulation-based fake-data checking (Bayesian workflow): simulate from the fitted model and look for discrepancies. — from [[gelman-2013-bda3/ch06-model]] (bayesian → bayesian)
- [same-math] LOO-CV with the log score ↔ machine learning: cross-validated log-loss (negative log predictive probability on held-out points) — the same quantity, computed with a posterior predictive. — from [[gelman-2013-bda3/ch07-evaluating]] (bayesian → other)
- [structural-analogy] checking imputations against observed data (Fig. 18.2b) ↔ posterior predictive checks: systematic difference signals model misfit. — from [[gelman-2013-bda3/ch18-models]] (bayesian → other)
- [structural-analogy] posterior predictive p-value ↔ frequentist parametric-bootstrap goodness-of-fit: both simulate replicates from the fitted model, but the Bayesian one averages over the posterior and the bootstrap plugs in a point estimate (pp. 12, 15) — from [[gelman-2013-philosophy/main]] (bayesian → other)
- [structural-analogy] Standardization $\sum_l P(Y\mid L,a)P(L)$ ↔ bayesian: marginalising over a nuisance variable, as in a posterior predictive average — both average a conditional distribution over another variable's distribution. — from [[hernan-2020-whatif/ch02-randomized]] (bayesian → bayesian)
- [structural-analogy] Marginal effect = weighted average of conditional effects with weights $w(l)$ ↔ bayesian: posterior predictive averaging over parameter uncertainty — both marginalize over a distribution. — from [[hernan-2020-whatif/ch04-effect]] (bayesian → bayesian)
- [metaphor] Searching $\psi^\dagger$ until $H$ looks unrelated to $A$ ↔ posterior predictive checking: tune a parameter until a data-based diagnostic shows no leftover structure. — from [[hernan-2020-whatif/ch14-g]] (bayesian → other)
- [structural-analogy] Parametric g-formula ↔ bayesian: posterior predictive averaging — model outcome given covariates, then average over the covariate distribution. — from [[hernan-2020-whatif/ch17-causal]] (bayesian → bayesian)
- [same-math] $P(R_1|B)=\langle F\rangle$ (3.72) ↔ bayesian: posterior predictive for a Bernoulli trial is the posterior mean of $\theta$ — both are the law of total probability applied to a fraction. — from [[jaynes-2003-probability/ch03-elementary]] (information-theory → bayesian)
- [metaphor] Randomization as discarding relevant information ↔ bayesian: modelling assumptions and prior/posterior predictive checks — both ask what a simplification throws away. — from [[jaynes-2003-probability/ch03-elementary]] (information-theory → bayesian)
- [structural-analogy] Mr A / Mr B: a persistent mismatch reveals a missing constraint ↔ Bayesian workflow: posterior predictive checks revealing misfit — from [[jaynes-2003-probability/ch11-discrete]] (information-theory → bayesian)
- [structural-analogy] Marginalizing over $u$ for prediction ↔ bayesian: posterior predictive vs. plug-in estimates — both average over hypotheses. — from [[mackay-2003-information/ch02-probability]] (information-theory → bayesian)
- [same-math] Laplace rule in the coder ↔ bayesian: posterior predictive of a Beta–Bernoulli model with a uniform prior — MacKay derives it from the uniform prior (p. 117). — from [[mackay-2003-information/ch06-stream]] (information-theory → bayesian)
- [structural-analogy] Moderated output $f(\kappa a_{\rm MP})$ ↔ bayesian: posterior predictive shrinking toward 0.5 with uncertainty. — from [[mackay-2003-information/ch41-learning]] (information-theory → bayesian)
- [same-math] Posterior predictive averaging ↔ marginalization: $\sum_p \Pr(p\mid\text{data})\Pr(\tilde w\mid p)$ (the formula is ours; the text describes it in words) — from [[mcelreath-2020-rethinking/ch03-sampling]] (bayesian → other)
- [same-math] Simulating heights from each posterior sample's (μ, σ) ↔ bayesian: posterior predictive distribution; the procedure is the same Monte Carlo averaging over parameters — from [[mcelreath-2020-rethinking/ch04-linear-p2]] (bayesian → bayesian)
- [same-math] Solomonoff mixture $\xi$ and posterior weights (5.195) ↔ bayesian: posterior predictive of a Bayesian model average. — from [[murphy-2023-pml2/ch05-information-p2]] (bayesian → bayesian)
- [structural-analogy] Multiple imputation $p(\mathbf X_m|\mathbf X_o)$ ↔ Bayesian posterior predictive for missing data — sampling unknowns given observed. — from [[murphy-2023-pml2/ch20-generative]] (bayesian → unspecified)
- [structural-analogy] Aleatoric vs epistemic split in BALD (34.99) ↔ posterior predictive distribution: predictive entropy minus expected entropy given parameters. — from [[murphy-2023-pml2/ch34-decision]] (bayesian → other)
- [structural-analogy] Bayes-adaptive MDP belief state ↔ bayesian: sequential updating, with the posterior predictive as transition model (p. 1149). — from [[murphy-2023-pml2/ch35-reinforcement]] (bayesian → bayesian)
- [metaphor] Placebo checks ↔ prior/posterior predictive checks: testing a model against something it should or should not predict. — from [[murphy-2023-pml2/ch36-causality-p2]] (bayesian → other)
- [structural-analogy] Monty Hall: evidence depends on how it was generated ↔ likelihoods depend on the data-collection or selection process (e.g. a posterior predictive model of the sampling). — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → unspecified)
- [structural-analogy] Testing a graph by vanishing partial regression coefficients ↔ posterior predictive checks: derive a checkable implication, compare with data. — from [[pearl-2016-primer/ch02-graphical]] (bayesian → other)
- [structural-analogy] Eq. 9.5 as a sum over $m$ weighted by $P(M{=}m\mid X)$ ↔ Posterior predictive distribution: averaging over a distribution of an intermediate quantity — from [[pearl-2018-bookofwhy/ch09-mediation-p2]] (bayesian → other)
