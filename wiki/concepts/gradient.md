---
id: gradient
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 4
n_works: 2
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/app-appendices, boyd-2018-vmls/ch02-linear, deisenroth-2020-mml/ch01-introduction, deisenroth-2020-mml/ch05-vector]
generated_by: build_kg.py
---

# gradient

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/app-appendices]] (p. 445): vector of partial derivatives of a scalar function of a vector; $\nabla\|x\|^2=2x$ [new]
- [[boyd-2018-vmls/ch02-linear]] (p. 36): $n$-vector of partial derivatives of $f$ at $z$ [new]
- [[deisenroth-2020-mml/ch01-introduction]] (p. 15): in this unit, the quantity that gives the direction in which to search for a solution [new]
- [[deisenroth-2020-mml/ch05-vector]] (pp. 140, 146): row vector (1×n) of partials of a scalar function; points in the direction of steepest ascent [new]

## Instances that use it

- [[incremental-gradient-region-of-confusion]] — scalar least squares example showing fast far-field progress, oscillation inside $R$ — from [[bertsekas-2026-rlcourse/ch03-learning-p1]]
- [[policy-gradient-discounted-dp]] — Example 3.5.1, trajectory score $\sum_m\nabla\log p(u_m\mid i_m;r)$ with no transition model — from [[bertsekas-2026-rlcourse/ch03-learning-p4]]
- [[two-state-policy-gradient-local-minima]] — $J_\alpha(r)$ with local minima at $r=0,1$ — from [[bertsekas-2026-rlcourse/ch03-learning-p5]]
- [[satellite-orbit-analogy]] — planet = mode, gravity = gradient, orbit = typical set — from [[betancourt-2017-hmc/main-p1]]
- [[random-walk-metropolis]] — non-gradient method with a smaller geometrically ergodic class than HMC — from [[betancourt-2017-hmc/main-p3]]
- [[gradient-of-sum-of-squares]] — $\nabla\|x\|^2=2z$ at $z$ — from [[boyd-2018-vmls/app-appendices]]
- [[gradient-of-squared-norm-of-vector-function]] — $\nabla h(z)=2Df(z)^Tf(z)$ — from [[boyd-2018-vmls/app-appendices]]
- [[gradient-of-linear-map]] — $\mathbf f=\mathbf A\mathbf x$ has Jacobian $\mathbf A$ — from [[deisenroth-2020-mml/ch05-vector]]
- [[least-squares-gradient]] — $\partial L/\partial\boldsymbol\theta=-2\mathbf e^\top\boldsymbol\Phi$ for the linear model — from [[deisenroth-2020-mml/ch05-vector]]
- [[deep-network-backprop]] — layered loss gradients reuse partial products — from [[deisenroth-2020-mml/ch05-vector]]
- [[gram-matrix-gradient]] — $d(\mathbf R^\top\mathbf R)/d\mathbf R$ — from [[deisenroth-2020-mml/ch05-vector]]
- [[quadratic-gd-example]] — Example 7.1: gradient descent on a 2-D quadratic, zigzag — from [[deisenroth-2020-mml/ch07-continuous]]
- [[husband-gradient]] — husbands: 53% / 32% / 18% across the three criteria — from [[katz-1955-personalinfluence/ch01-criteria]]
- [[status-gregariousness-gradient]] — high gregariousness rises from 15% at low status to 39% at high status — from [[katz-1955-personalinfluence/ch09-describing]]
- [[molecule-design-vae]] — latent-space gradient ascent on a property of SMILES-encoded molecules — from [[murphy-2023-pml2/ch21-variational]]
- [[natural-evolution-strategies]] — search gradient, empirical FIM, relaxation to $\min E_{p_\lambda}[f]$ — from [[nielsen-2020-elementary/main-p2]]
- [[linear-regression-gradient-descent]] — convex loss; after four iterations the parameters are already close to the minimum — from [[prince-2023-udl/ch06-fitting]]
- [[trivial-lqr-random-search-variance]] — $R(u)=\|u\|^2$ with Gaussian sampling shows dimension scaling of the gradient norm — from [[recht-2019-tour/main]]
- [[linear-gaussian-parametric-model]] — model (A.65) whose energy gradient is Theorem A.10 — from [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]]
- [[baird-counterexample]] — seven-state MDP where semi-gradient TD and DP both diverge; also test bed for TDC and Emphatic-TD — from [[sutton-2018-rl/ch11-off]]
- [[a-split-example]] — naive residual gradient finds B=¾, C=¼ because true values have higher TDE — from [[sutton-2018-rl/ch11-off]]
- [[gradient-bandit-algorithm]] — the one earlier method that learned a policy parameter directly — from [[sutton-2018-rl/ch13-policy]]
- [[williams-1992-reinforce-teams]] — Bernoulli-logistic REINFORCE teams ascend the average reward gradient — from [[sutton-2018-rl/ch15-neuroscience-p2]]

## Candidate bridges

- [structural-analogy] Adaptive law $\dot a=-\alpha we$, $\dot b=-\alpha ne$ ↔ machine learning: stochastic-gradient / LMS-style parameter updates driven by an error signal. — from [[astrom-2021-feedbacksystems/ch05-dynamic]] (control-theory → llm)
- [structural-analogy] MIT rule (15.17) ↔ neuron gradient rule (15.22): both adjust parameters along the error times a sensitivity or input, as the author notes. — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → other:biology-neuroscience)
- [same-math] PDE (9.3), $\partial f/\partial T=\max_z(\dot x,\nabla f)$ ↔ control theory: HJB equation with time-to-go — same maximization of drift against the value gradient. — from [[bellman-1957-dp/ch06-vi]] (control-theory → control-theory)
- [metaphor] Frequency-count policy update in MCTS ↔ gradient-style policy improvement (p. 274, "reminiscent of gradient-type methods"). — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (control-theory → unspecified)
- [same-math] Incremental gradient (3.10) ↔ machine learning: stochastic gradient descent with random index choice (the text itself makes this link, p. 366). — from [[bertsekas-2026-rlcourse/ch03-learning-p1]] (control-theory → llm)
- [structural-analogy] SARSA update (3.27) ↔ temporal-difference learning: parameter moves along a gradient times the Q prediction error — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → control-theory)
- [same-math] likelihood-ratio gradient (3.47) ↔ statistics: score-function estimator, since $E\{\nabla\log p\}=0$ is the same identity. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other:statistics)
- [structural-analogy] FIM scaling ↔ Newton's method: both rescale the gradient by curvature, in different norms. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other:optimization)
- [metaphor] Gradient crashing into the mode ↔ optimization: gradient ascent/MAP finds the mode, which the typical set avoids. — from [[betancourt-2017-hmc/main-p1]] (bayesian → other:optimization)
- [metaphor] Satellite orbit ↔ gradient flow around a mode: momentum prevents falling in. — from [[betancourt-2017-hmc/main-p2]] (bayesian → other:gradient-flow-around-a)
- [same-math] SVI's noisy unbiased gradient with $\sum\epsilon_t=\infty$, $\sum\epsilon_t^2<\infty$ ↔ stochastic approximation (Robbins–Monro): the step-size conditions are the same ones — from [[blei-2017-variational/main-p1]] (bayesian → other:stochastic-approximation-robbins-monro)
- [structural-analogy] Black-box MC-gradient VI ↔ Monte Carlo integration: the ELBO gradient is written as an expectation and estimated by sampling (pp. 25–26). — from [[blei-2017-variational/main-p2]] (bayesian → bayesian)
- [same-math] Chain rule as $Dh=Df\cdot Dg$ ↔ calculus/optimization: gradient of f(Ax+b) is $A^T\nabla f$ — the same Jacobian product. — from [[boyd-2018-vmls/ch10-matrix]] (linear-algebra → other:optimization)
- [metaphor] Training as hill climbing ↔ optimization: following the gradient to a maximum of a performance measure (pp. 13, 15). — from [[deisenroth-2020-mml/ch01-introduction]] (linear-algebra → other:optimization)
- [same-math] condition number $\sigma_{\max}/\sigma_{\min}$ ↔ linear-algebra: condition number from the SVD — same quantity, here controlling gradient-descent speed. — from [[deisenroth-2020-mml/ch07-continuous]] (linear-algebra → linear-algebra)
- [structural-analogy] Local modes from periodic data ↔ optimization: local optima that trap gradient methods by starting point — both depend on initialization. — from [[gelman-2020-workflow/main-p3]] (bayesian → other:optimization)
- [structural-analogy] Critical batch size from gradient noise scale ↔ optimization: noise-limited vs. curvature-limited regimes of SGD — authors rely on [MKAT18] (p. 12–13). — from [[kaplan-2020-scaling/main]] (llm → other:optimization)
- [structural-analogy] Covariant costate propagating backward ↔ backpropagation of gradients (canon link; not stated in this unit). — from [[liberzon-2012-calculus/ch07-advanced]] (control-theory → unspecified)
- [same-math] Boltzmann-machine learning gradient (data minus model moments) ↔ information-theory: maximum-entropy / exponential-family fitting, where parameters are tuned until model expectations match data expectations — same moment-matching condition. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → information-theory)
- [same-math] CRF/MRF log-likelihood gradient (features minus expected features) ↔ exponential-family MLE: derivative of log-partition is expected sufficient statistics (Sec. 2.4.3, cited p. 183). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → other:exponential-family-mle)
- [structural-analogy] KL $\approx\frac12\delta^\top F\delta$ ↔ squared Mahalanobis distance with the Fisher matrix as metric (an approximation), the basis of natural gradient (§5.1.9). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → unspecified)
- [same-math] Reparameterization gradient ↔ variational inference: the pathwise ELBO gradient used in stochastic VI (p. 275) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → bayesian)
- [structural-analogy] Natural parameters vs moment parameters ↔ exponential-family duality: ordinary gradient in $\mu$ equals natural gradient in $\lambda$ (p. 284) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → other:exponential-family-duality)
- [same-math] Evolution-strategies gradient (6.190) ↔ machine learning: score-function (REINFORCE) estimator, cited as Section 6.3.4. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → llm)
- [same-math] marginals as $\nabla_\eta\log Z$ ↔ exponential families: mean of sufficient statistics equals gradient of the log partition (p. 435). — from [[murphy-2023-pml2/ch09-message]] (bayesian → information-theory)
- [same-math] Reparameterized gradient $\mathbb E_{p(\epsilon)}[\nabla_\phi f(g(\phi,\epsilon))]$ ↔ Monte Carlo integration: a single-sample Monte Carlo estimate of an expectation of a gradient. — from [[murphy-2023-pml2/ch10-variational-p1]] (bayesian → bayesian)
- [structural-analogy] Noisy SGD ↔ Langevin sampling: both are gradient steps plus noise; temperature $\eta/B$ (p. 523). — from [[murphy-2023-pml2/ch12-markov-p1]] (bayesian → bayesian)
- [same-math] SGLD-CV / SVRG gradient (12.124) ↔ Monte Carlo variance reduction: a control variate subtracts a correlated term of known mean. — from [[murphy-2023-pml2/ch12-markov-p2]] (bayesian → bayesian)
- [same-math] $\nabla_\theta\log Z_\theta=\mathbb E_{p_\theta}[-\nabla_\theta E_\theta]$ ↔ exponential families: gradient of the log-normaliser equals the expected sufficient statistic — same identity for $E_\theta=-\theta^T\phi(x)$ (added link; not stated here). — from [[murphy-2023-pml2/ch24-energy]] (bayesian → information-theory)
- [structural-analogy] Score-function estimator for text GANs ↔ REINFORCE-style gradient estimators for discrete variables, also relevant to GAIL (p. 923). — from [[murphy-2023-pml2/ch26-generative]] (bayesian → unspecified)
- [same-math] Natural gradient with Fisher metric ↔ machine learning: the natural-gradient update $\theta-\alpha g^{-1}\nabla L$ used in NES — the same formula, with $g$ the (empirical) FIM (pp. 34, 36). — from [[nielsen-2020-elementary/main-p2]] (information-theory → llm)
- [structural-analogy] Mirror descent in the dual space ↔ optimization: gradient step in coordinates where the loss gradient has the right (covariant) type (p. 35). — from [[nielsen-2020-elementary/main-p2]] (information-theory → other:optimization)
- [metaphor] Pretraining gradient mix during PPO ↔ regularization toward a prior distribution; here an extra loss term, not a Bayesian prior. — from [[ouyang-2022-instructgpt/main-p2]] (llm → unspecified)
- [structural-analogy] Minimising $L[\phi]$ by gradient steps ↔ LLM pretraining: minimising cross-entropy over parameters — same loop with a different loss (not stated in this unit). — from [[prince-2023-udl/ch02-supervised]] (llm → llm)
- [structural-analogy] SGD with minibatches ↔ llm: pretraining on huge text, where each step uses a sampled batch of tokens — same noisy-gradient idea (canon link; not stated in this unit) — from [[prince-2023-udl/ch06-fitting]] (llm → llm)
- [structural-analogy] Hessian-eigenvalue classification of zero-gradient points ↔ dynamical systems: stability of fixed points — from [[prince-2023-udl/ch06-fitting]] (llm → complex-systems)
- [structural-analogy] Reverse-mode differentiation on acyclic graphs ↔ LLM training (canon link; not stated in this unit): gradients for Transformer parameters are obtained by such graph sweeps. — from [[prince-2023-udl/ch07-gradients]] (llm → llm)
- [structural-analogy] REINFORCE with $\partial\log\pi$ weighted by return ↔ llm: maximum-likelihood next-token training, but weighted by reward and using sampled sequences (the text compares policy-gradient smoothness to maximum likelihood in classification, p. 389). — from [[prince-2023-udl/ch19-reinforcement]] (llm → llm)
- [structural-analogy] Chebyshev acceleration ↔ Krylov methods (Conjugate Gradient, announced for the next chapter): both are polynomial-in-$A$ solvers — from [[spielman-2025-sagt/ch34-iterative]] (linear-algebra → other:krylov-methods-conjugate-gradient)
- [structural-analogy] Liapunov function / gradient potential ↔ optimisation: a loss function that decreases along update steps rules out cycling — both use a strictly decreasing quantity to forbid loops. — from [[strogatz-2024-nonlinear/ch07-limit-p1]] (complex-systems → other:optimization)
- [structural-analogy] Gradient bandit with baseline ↔ stochastic approximation: noisy-gradient ascent with variance reduction. — from [[sutton-2018-rl/ch02-multi]] (control-theory → other:optimization)
- [same-math] Off-policy semi-gradient factor $1+\alpha(2\gamma-1)$ ↔ control-theory/stability: scalar linear recursion $x_{k+1}=ax_k$ unstable iff $|a|>1$ — same recursion form (here the text's condition is "greater than 1") — from [[sutton-2018-rl/ch11-off]] (control-theory → control-theory)
- [structural-analogy] parameterized policy $\pi_\theta$ updated by gradient ascent on $J$ ↔ control theory: state feedback $u=-Kx$ with gain tuned to optimize a cost — both tune a feedback law's parameters. — from [[sutton-2018-rl/ch13-policy]] (control-theory → control-theory)
- [same-math] TD model (14.4–14.6) ↔ RL: backward-view semi-gradient TD($\lambda$) with linear approximation — stated as equivalent, except for what $R_t$ represents. — from [[sutton-2018-rl/ch14-psychology]] (control-theory → control-theory)
- [same-math] ∇ ln π(A|S,θ) = (A − π(1))x for a logistic unit ↔ statistics: the gradient of the Bernoulli log-likelihood under a logistic link — same expression form. — from [[sutton-2018-rl/ch15-neuroscience-p2]] (control-theory → other:statistics)
