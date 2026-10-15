---
id: importance-sampling
type: concept
fields: [control-theory, bayesian, information-theory, llm]
n_sources: 7
tiers: [core, deep, reference]
grounding: digests
sources: [gelman-2013-bda3/ch10-introduction, mackay-2003-information/ch29-monte, murphy-2023-pml2/ch11-monte, prince-2023-udl/ch17-variational, sarkka-2023-bayesianfiltering/ch02-bayesian, sarkka-2023-bayesianfiltering/ch11-particle, sutton-2018-rl/ch05-monte]
generated_by: build_kg.py
---

# importance-sampling

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 24): weighted samples from an importance distribution $\pi$ [new]
- [[sarkka-2023-bayesianfiltering/ch11-particle]] (pp. 231–233): sample from $\pi$, correct with weights $p/\pi$; self-normalized when $p$ is known up to a constant [new]
- [[sutton-2018-rl/ch05-monte]] (p. 104): reweight returns by $\rho_{t:T-1}=\prod\pi/b$ to change the expectation from $b$ to $\pi$ [new]

### bayesian

- [[gelman-2013-bda3/ch10-introduction]] (p. 265): estimate expectations from draws of $g$ with weights $q/g$ via ratio estimator (10.3) (p. 265) (new)
- [[murphy-2023-pml2/ch11-monte]] (p. 490–491): weight proposal samples by $\pi/q$ to estimate expectations under $\pi$ [new]

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 361–362): estimate Φ from Q-samples using weights P*/Q* and a ratio estimator; needs heavy-tailed Q; not a sampler [new]

### llm

- [[prince-2023-udl/ch17-variational]] (p. 340): estimate Pr(x) by sampling from auxiliary q and rescaling [new]

## Instances that use it

- [[importance-sampling-sphere-gaussian]] — weight spread exp(√(2N)); about 10^19 for N = 1000 — from [[mackay-2003-information/ch29-monte]]
- [[infinite-variance-one-state-mdp]] — ordinary importance sampling has infinite variance and fails to converge — from [[sutton-2018-rl/ch05-monte]]

## Candidate bridges

- [same-math] Weighting draws by $p(\theta\mid y)/g(\theta)$ (p. 300) ↔ importance sampling: same ratio of target to proposal density. — from [[gelman-2013-bda3/ch12-computationally]] (bayesian → other)
- [structural-analogy] Static sensitivity analysis (reweight posterior draws by new-to-old prior ratio) ↔ importance sampling: the same reweighting idea, applied to prior changes (p. 35). — from [[gelman-2020-workflow/main-p2]] (bayesian → other)
- [same-math] LOO-CV approximation by importance weights ↔ importance sampling in Monte Carlo integration: weights correct draws from the full posterior toward a leave-out posterior (p. 31). — from [[gelman-2020-workflow/main-p2]] (bayesian → other)
- [structural-analogy] positivity and the IP-weighted mean $\mathrm E[I(A=a)Y/f[A\mid L]]$ ↔ Monte Carlo: importance sampling needs the proposal's support to cover the target's. — from [[hernan-2020-whatif/ch03-observational]] (bayesian → other)
- [structural-analogy] IP weights $1/f(A|L)$ and Hajek ratio ↔ importance sampling: reweighting draws from one distribution to mimic another; the Hajek ratio resembles the self-normalized estimator — the source does not make this link. — from [[hernan-2020-whatif/ch12-ip]] (bayesian → other)
- [structural-analogy] Weight spread exp(√N) in importance sampling ↔ information-theory: fluctuation of −ln P(x) around entropy (AEP), which the text invokes via typical sequences (p. 363–364, 384). — from [[mackay-2003-information/ch29-monte]] (information-theory → information-theory)
- [same-math] Importance weights $1/p(\mathcal D_n|\theta_s)$ for LOO ↔ Monte Carlo: self-normalized importance sampling — from [[murphy-2023-pml2/ch03-statistics-p3]] (bayesian → other)
- [same-math] IWAE estimator $\hat p_S$ ↔ importance sampling: it is the importance-sampling average of $p_\theta(x,z_s)/q_\phi(z_s|x)$ estimating $p(x)$ (the text ties IWAE to self-normalised importance sampling) (p. 473) — from [[murphy-2023-pml2/ch10-variational-p2]] (bayesian → other)
- [same-math] SMC with likelihood tempering and no resampling ↔ Monte Carlo: annealed importance sampling — the text states the equivalence (p. 565). — from [[murphy-2023-pml2/ch13-sequential]] (bayesian → other)
- [same-math] Importance weighting $w=q(x)/p(x)$ for target risk (19.12–19.16) ↔ Monte Carlo integration: importance sampling re-expresses an expectation under $q$ as one under $p$ times a density ratio. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → other)
- [structural-analogy] importance-sampling off-policy correction ↔ causal inference / covariate shift: reweighting to remove data–target mismatch (p. 1171). — from [[murphy-2023-pml2/ch35-reinforcement]] (bayesian → bayesian)
- [structural-analogy] Propensity weighting ↔ bayesian: importance sampling — reweight a sample from $P(X\mid A)$ to look like $P(X)$. — from [[murphy-2023-pml2/ch36-causality-p1]] (bayesian → bayesian)
- [structural-analogy] inverse probability weighting ($1/P(x|z)$) ↔ Bayesian computation: importance sampling — both reweight samples drawn from one distribution to mimic another. — from [[pearl-2016-primer/ch03-effects]] (bayesian → bayesian)
- [structural-analogy] Particle filter weight degeneracy ↔ importance sampling in high dimension: both have weights concentrating on one draw. — from [[robert-2011-mcmc/main]] (bayesian → other)
