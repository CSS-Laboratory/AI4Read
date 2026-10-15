---
id: parameter
type: concept
fields: [bayesian, control-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch04-machine, mcelreath-2020-rethinking/ch02-small]
generated_by: build_kg.py
---

# parameter

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch02-small]] (p. 34): an unknown input of the likelihood that data are used to estimate; the datum/parameter line is fuzzy [new]

### control-theory

- [[ashby-1956-cybernetics/ch04-machine]] (p. 43): symbol whose value selects which transformation applies; the machine's input (new)

## Instances that use it

- [[haunted-house-letter]] — Singing and Laughter as a machine with two parameters (organ, incense) — from [[ashby-1956-cybernetics/ch04-machine]]
- [[lossy-four-state-coder-table]] — the 4-state, 3-parameter transducer whose output loses a distinction (BC duplicated), so it cannot be a perfect coder — from [[ashby-1956-cybernetics/ch08-transmission]]
- [[balance-system]] — scaling from 5 to 2 parameters — from [[astrom-2021-feedbacksystems/ch03-system-p2]]
- [[vehicle-steering]] — linearized lateral dynamics with single parameter $\gamma=a/b$ — from [[astrom-2021-feedbacksystems/ch06-linear]]
- [[parameter-parallel-softmax]] — output units split across CPUs; about 99.7% of the compute is in the output layer — from [[bengio-2003-nplm/main]]
- [[markov-jump-parameter-problem]] — augmented state, CE with most likely parameter path — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[treasure-hunting]] — adaptive control with parameter $\theta$ — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]]
- [[regression-as-linear-in-parameters]] — predictions linear, residuals affine in $(v,\beta)$ — from [[boyd-2018-vmls/ch08-linear]]
- [[sinusoid-ridge-example]] — five-parameter ridge fit, minimum test error near $\lambda=0.079$ — from [[boyd-2018-vmls/ch15-multi]]
- [[exponentially-decaying-sinusoid-fit]] — nonlinear model fit with four parameters, $N=60$ — from [[boyd-2018-vmls/ch18-nonlinear]]
- [[coin-flip-bernoulli]] — Bernoulli with parameter μ, repeated flips, plate notation, Beta hyperprior — from [[deisenroth-2020-mml/ch08-when]]
- [[bert-base-and-large]] — the two main model sizes (110M and 340M parameters) on which results are primarily reported; Table 6 also varies size — from [[devlin-2019-bert/main]]
- [[bivariate-normal-gibbs]] — Gibbs on N((y₁,y₂), [[1,ρ],[ρ,1]]), ρ = 0.8, shows slow correlated moves when parameters are highly correlated — from [[gelman-2013-bda3/ch11-basics]]
- [[t-model-as-normal-mixture]] — t likelihood written with auxiliary variances $V_i$; Gibbs steps, then parameter expansion with $\alpha$ — from [[gelman-2013-bda3/ch12-computationally]]
- [[age-income-missingness]] — three missingness cases (MCAR; MAR but not observed at random, ignorable if parameters are distinct; nonignorable) in a bivariate normal — from [[gelman-2013-bda3/ch18-models]]
- [[planetary-motion]] — ODE model with multimodal posterior, simplified to one parameter to understand local modes — from [[gelman-2020-workflow/main-p3]]
- [[pharaoh-reigns]] — right form, wrong parameter ($\beta$ 17.9 vs about 9.34) — from [[griffiths-2006-optimal/main]]
- [[nhefs-smoking-cessation]] — g-estimate 3.4 kg (95% CI 2.5, 4.5) in the one-parameter model; $\hat\beta_1=2.86$, $\hat\beta_2=0.03$ with a smoking-intensity product term — from [[hernan-2020-whatif/ch14-g]]
- [[borel-kolmogorov-paradox]] — ambiguity of $df\to0$ limits with an extra parameter — from [[jaynes-2003-probability/ch04-elementary]]
- [[euler-jupiter-saturn]] — Euler failed to see error cancellation: 75 observations, eight parameters — from [[jaynes-2003-probability/ch07-central-p1]]
- [[euler-jupiter-saturn]] — 8 parameters from 75 observations, which defeated Euler and was solved by Laplace — from [[jaynes-2003-probability/ch19-physical]]
- [[nested-model-parameter-addition]] — $M_n\subset M_{n+1}$ via $\theta_{n+1}=0$ — from [[jaynes-2003-probability/ch20-model]]
- [[webtext2-scaling-runs]] — Transformers from 768 to 1.5B non-embedding parameters on WebText2 — from [[kaplan-2020-scaling/main]]
- [[two-gaussian-mixture-grid]] — 800-point grid over five parameters, with model evidence — from [[mackay-2003-information/ch21-exact]]
- [[epicycles-vs-copernicus]] — more parameters and a coincidence in the extra parameters — from [[mackay-2003-information/ch28-model]]
- [[train-test-deviance-simulation]] — in- vs out-of-sample deviance for 1–5 parameters at $N=20$ and $N=100$ — from [[mcelreath-2020-rethinking/ch06-overfitting-p1]]
- [[bernoulli-as-exponential-family]] — logit natural parameter, sigmoid mean, $A=\log(1+e^\eta)$ — from [[murphy-2023-pml2/ch02-probability-p2]]
- [[uniform-non-example]] — parameter-dependent support excludes it from the family — from [[murphy-2023-pml2/ch02-probability-p2]]
- [[coupled-gaussian-ngd-example]] — 2-d Gaussian with coupled parameters, NGD vs steepest descent — from [[murphy-2023-pml2/ch06-optimization-p1]]
- [[gpt-3]] — 175B-parameter decoder-only transformer, in-context learning — from [[murphy-2023-pml2/ch22-autoregressive]]
- [[dirac-gan]] — GAN with one scalar parameter per player ($\theta$, $\phi$) that cycles under alternating descent — from [[murphy-2023-pml2/ch26-generative]]
- [[jeffreys-powers-of-x]] — $y=ax^n$: infinitely many same-parameter laws — from [[popper-1959-logic/appviii-untitled]]
- [[ellipse-vs-circle-parameters]] — equal parameter counts but unequal simplicity; an objection to Weyl that the formal vs. material reduction distinction can meet — from [[popper-1959-logic/ch07-simplicity]]
- [[ten-parameter-relu-network]] — three-unit scalar network of Eq. 3.1 and Fig. 3.3 — from [[prince-2023-udl/ch03-shallow]]
- [[regions-per-parameter]] — K = 5, D = 10: 471 parameters, 161,051 regions — from [[prince-2023-udl/ch04-deep]]
- [[linear-regression-gradient-descent]] — convex loss; after four iterations the parameters are already close to the minimum — from [[prince-2023-udl/ch06-fitting]]
- [[gabor-model-fitting]] — two-parameter non-convex loss with local minima and a saddle point; global loss 0.64 — from [[prince-2023-udl/ch06-fitting]]
- [[sin-exp-cos-toy-model]] — eight-parameter scalar model used to derive backpropagation — from [[prince-2023-udl/ch07-gradients]]
- [[mnist-1d-cnn-vs-fc]] — CNN (2,050 parameters, ~17% test error) beats a fully connected net (59,065, ~40%) — from [[prince-2023-udl/ch10-convolutional]]
- [[alexnet]] — 8 layers, ~60M parameters, 16.4% top-5 error — from [[prince-2023-udl/ch10-convolutional]]
- [[vgg-network]] — 19 layers, 144M parameters, 6.8% top-5 error — from [[prince-2023-udl/ch10-convolutional]]
- [[bert]] — encoder, 340M parameters, masked-word pre-training, fine-tuned for classification, NER, span prediction — from [[prince-2023-udl/ch12-transformers]]
- [[gpt3]] — decoder, 175B parameters, next-token prediction, few-shot completion — from [[prince-2023-udl/ch12-transformers]]
- [[vgg-19-pruning]] — 98.5% of parameters removed on CIFAR-10 — from [[prince-2023-udl/ch20-does]]
- [[training-emissions]] — 213M-parameter transformer, about 284 tonnes CO$_2$ — from [[prince-2023-udl/ch21-deep]]
- [[drift-regression-sine-tracking]] — tracking a sine with random-walk parameters (Fig. 3.5) and with a locally linear Kalman filter (Fig. 3.6) — from [[sarkka-2023-bayesianfiltering/ch03-batch]]
- [[gaussian-random-walk]] — filtering (6.7), smoothing (12.3), parameter posterior (16.10) — from [[sarkka-2023-bayesianfiltering/ch20-list]]
- [[beam-buckling]] — load as control parameter; vertical state becomes unstable and two buckled states are born — from [[strogatz-2024-nonlinear/ch03-bifurcations-p1]]
- [[gradient-bandit-algorithm]] — the one earlier method that learned a policy parameter directly — from [[sutton-2018-rl/ch13-policy]]
- [[dqn-atari]] — one architecture and parameter set across Atari games using raw frames — from [[sutton-2018-rl/ch16-applications]]

## Candidate bridges

- [same-math] machine $x'=f(x,a)$ with parameter $a$ ↔ control-theory: discrete-time state model with an input — $a$ plays the role of the input. — from [[ashby-1956-cybernetics/ch04-machine]] (control-theory → control-theory)
- [structural-analogy] coupling by setting the parameter as a function of the other machine's state ↔ control-theory: feedback law (state or output feedback) — the loop is closed by making input depend on state. — from [[ashby-1956-cybernetics/ch04-machine]] (control-theory → control-theory)
- [same-math] Mechanical spring–wheel–friction system, RLC circuit and $a\ddot z + b\dot z + cz = w$ (pp. 95–96) ↔ control-theory: systems sharing one second-order transfer function — the same differential equation with matched parameters. — from [[ashby-1956-cybernetics/ch06-black]] (control-theory → control-theory)
- [structural-analogy] Adaptive law $\dot a=-\alpha we$, $\dot b=-\alpha ne$ ↔ machine learning: stochastic-gradient / LMS-style parameter updates driven by an error signal. — from [[astrom-2021-feedbacksystems/ch05-dynamic]] (control-theory → other)
- [same-math] $dG/G=S\,dP/P$ ↔ sensitivity analysis: the relative-change (logarithmic) derivative of a closed-loop function with respect to a parameter. — from [[astrom-2021-feedbacksystems/ch13-robust]] (control-theory → other)
- [structural-analogy] MIT rule (15.17) ↔ neuron gradient rule (15.22): both adjust parameters along the error times a sensitivity or input, as the author notes. — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → other)
- [structural-analogy] Discount parameter $w$ ↔ economics/finance: discount factor on future payoffs. The same geometric weighting, but here $w$ also stands for the chance of the relationship ending. — from [[axelrod-1984-cooperation/ch01-problemof]] (decision-game-theory → economics-finance)
- [structural-analogy] Dynamical selection of a critical point ↔ equilibrium phase transitions: the same scale-free behaviour without tuning a parameter — from [[bak-1987-soc/main]] (complex-systems → other)
- [metaphor] imbedding in a family of problems ↔ computational social science: studying a model by sweeping its parameters rather than solving one run — only a loose parallel (p. 84) — from [[bellman-1957-dp/ch03-iii]] (control-theory → other)
- [structural-analogy] Belief-averaged Q-factors, with a fixed policy for each fixed $\theta^i$ ↔ certainty equivalence / indirect adaptive control — the unknown parameter is treated as known and the results are averaged (p. 312–314). — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (control-theory → unspecified)
- [structural-analogy] SARSA update (3.27) ↔ temporal-difference learning: parameter moves along a gradient times the Q prediction error — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → other)
- [structural-analogy] regression with features $X$ ↔ social-science modelling: a model linear in parameters, so fitting becomes a linear-algebra problem. — from [[boyd-2018-vmls/ch08-linear]] (linear-algebra → other)
- [same-math] Pareto line $w=w^0+\rho v$ ↔ affine combinations: the solution of a linear KKT system with a right-hand side affine in a parameter is an affine function of that parameter (p. 365). — from [[boyd-2018-vmls/ch17-constrained]] (linear-algebra → other)
- [metaphor] Trust parameter ↔ cautious steps in an uncertain terrain: take smaller steps when the local map has proved unreliable. — from [[boyd-2018-vmls/ch18-nonlinear]] (linear-algebra → other)
- [same-math] Compute accounting (2 flops × 3 for backward = 6 per parameter per token) ↔ llm: compute-optimal training — the same per-token flop count is used to budget compute versus data. — from [[brown-2020-gpt3/main-p2]] (llm → llm)
- [structural-analogy] Polynomially many types vs. exponentially many sequences ↔ MDL / universal coding: model cost is only $O(\log n)$ bits per parameter. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → other)
- [structural-analogy] Conjugate update as parameter-counting (Beta$(\alpha+h,\beta+N-h)$) ↔ network science: updating link-probability beliefs from observed edges (our suggestion, not in the text). — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → complex-systems)
- [metaphor] E-step/M-step alternation ↔ coordinate-wise optimization: update one block of parameters while holding the others fixed. — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → other)
- [metaphor] Objective prior choice depending on the parameter of interest ↔ Bayesian statistics: the parameterization-dependence of "uninformative" priors. — from [[efron-1986-bayesian/main]] (bayesian → bayesian)
- [structural-analogy] Negative binomial / beta-binomial as overdispersed versions of Poisson / binomial ↔ bayesian: hierarchical models, where letting a parameter vary across units widens the marginal distribution. — from [[gelman-2013-bda3/appa-standard]] (bayesian → bayesian)
- [structural-analogy] Posterior concentrating on the KL-minimizing $\theta_0$ ↔ model misspecification: a wrong model still has a best-approximating parameter. KL here is $\mathrm{KL}(f\|p_\theta)$. — from [[gelman-2013-bda3/appb-outline]] (bayesian → other)
- [metaphor] LD50 summarized conditional on $\beta>0$ ↔ causal/estimand definition: a quantity is only defined in part of parameter space, so report the probability of that region plus the conditional distribution. — from [[gelman-2013-bda3/ch03-introduction]] (bayesian → bayesian)
- [structural-analogy] Nonidentified $\rho$ with posterior = prior ↔ any parameter with a flat likelihood: data add no information, so the prior carries all inference. — from [[gelman-2013-bda3/ch04-asymptotics]] (bayesian → other)
- [structural-analogy] Posterior calibration ↔ frequentist bias: conditions on data instead of on the true parameter. — from [[gelman-2013-bda3/ch05-hierarchical]] (bayesian → other)
- [structural-analogy] Ignorability (MAR + distinct parameters) ↔ causal inference: ignorable assignment given covariates / unconfoundedness — the text treats assignment as a missing-data mechanism. — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → bayesian)
- [structural-analogy] Parameter expansion (extra unidentified scale) ↔ hierarchical models: the chapter points to Section 15.5 for the hierarchical use. — from [[gelman-2013-bda3/ch12-computationally]] (bayesian → other)
- [structural-analogy] Bayesian IPF ↔ Gibbs sampling: cycling over one parameter at a time with a random rescaling — from [[gelman-2013-bda3/ch16-generalized]] (bayesian → other)
- [same-math] data augmentation ↔ Gibbs sampling: alternately draw $y_{\rm mis}$ and parameters from full conditionals (the text calls it a special case of Gibbs) (p. 465). — from [[gelman-2013-bda3/ch18-models]] (bayesian → other)
- [structural-analogy] Predictor-dependent mixture weights (22.15) ↔ hierarchical models with group-varying parameters: the "group" membership probability varies smoothly with $x$. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → other)
- [structural-analogy] Marginal-likelihood penalty on extra clusters ↔ Bayesian Occam's razor: more parameters spread mass thinner. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → bayesian)
- [structural-analogy] Topology of models with shared-meaning parameters ↔ causal inference: a treatment effect estimated across a sequence of adjustment models (p. 42). — from [[gelman-2020-workflow/main-p2]] (bayesian → bayesian)
- [structural-analogy] $\mathrm{softmax}(xK^\top)V$ (Eq. 2) ↔ attention: weighted average of value vectors with query–key weights. Here keys and values are fixed parameters and no scaling is shown. — from [[geva-2021-ffn/main]] (llm → other)
- [structural-analogy] Unification as explanation ↔ model simplicity: explaining many facts with few principles resembles compressing data with a few parameters. — from [[godfreysmith-2003-theory/ch13-explanation]] (analytic-philosophy → other)
- [metaphor] Prediction by analogy ↔ hierarchical or transfer learning: form shared from familiar classes, parameters set by data — from [[griffiths-2006-optimal/main]] (bayesian → other)
- [structural-analogy] Wordfish's $\alpha_i+\psi_j+\beta_j\theta_i$ ↔ roll-call IRT scaling: discrimination parameter times latent position — same logic applied to words instead of votes. — from [[grimmer-2013-textasdata/main]] (political-science → other)
- [structural-analogy] choosing K with penalties (AIC/BIC) ↔ model selection in regression — more parameters always fit better in-sample (p. 227). — from [[grimmer-2022-textasdata/ch12-clustering]] (political-science → unspecified)
- [structural-analogy] individual-specific random probability $Q_{Y^a}$ with population mean $E[Q]$ ↔ Bayesian: hierarchical model with per-unit parameters drawn from a population. — from [[hernan-2020-whatif/ch01-definition]] (bayesian → bayesian)
- [structural-analogy] Marginal effect = weighted average of conditional effects with weights $w(l)$ ↔ bayesian: posterior predictive averaging over parameter uncertainty — both marginalize over a distribution. — from [[hernan-2020-whatif/ch04-effect]] (bayesian → bayesian)
- [structural-analogy] Faithfulness (no exact cancellation) ↔ Bayesian: a prior giving probability zero to parameter values that produce exact cancellation — both rely on "generic" parameters. — from [[hernan-2020-whatif/ch06-graphical]] (bayesian → bayesian)
- [structural-analogy] Hidden factor $H$ making a DAG causal ↔ hierarchical models with latent parameters — both add unobserved variables to make the structure coherent. — from [[hernan-2020-whatif/ch09-measurement]] (bayesian → unspecified)
- [structural-analogy] Bias–variance trade-off in choosing the number of parameters ↔ bayesian: Bayesian Occam's razor and cross-validation for model choice. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [same-math] CI by inverting the test of $\alpha_1=0$ ↔ frequentist inference: confidence set as all parameter values a test does not reject — same construction. — from [[hernan-2020-whatif/ch14-g]] (bayesian → other)
- [structural-analogy] Testing a known non-zero $\alpha_1$ for sensitivity analysis ↔ Bayesian inference: a prior or fixed value for a bias parameter, with results shown across its range. — from [[hernan-2020-whatif/ch14-g]] (bayesian → bayesian)
- [metaphor] Searching $\psi^\dagger$ until $H$ looks unrelated to $A$ ↔ posterior predictive checking: tune a parameter until a data-based diagnostic shows no leftover structure. — from [[hernan-2020-whatif/ch14-g]] (bayesian → other)
- [structural-analogy] Nuisance parameters in outcome versus treatment models ↔ Bayesian inference: parameters not of interest are handled in a separate model component (the unit does not discuss this). — from [[hernan-2020-whatif/ch15-outcome]] (bayesian → bayesian)
- [structural-analogy] Non-identified parameter needs an extra untestable assumption ($\beta_1=0$) ↔ Bayesian inference: when data cannot identify a parameter, the posterior depends on the prior — both fill a gap the data cannot. — from [[hernan-2020-whatif/ch16-instrumental]] (bayesian → bayesian)
- [structural-analogy] Weak instrument and small denominator blow up the ratio estimate ↔ Bayesian inference: weakly identified parameters give unstable, highly variable estimates. — from [[hernan-2020-whatif/ch16-instrumental]] (bayesian → bayesian)
- [structural-analogy] Integrating out $\sigma$ as a nuisance parameter ↔ Bayesian: hierarchical models averaging over group-level uncertainty (p. 219) — from [[jaynes-2003-probability/ch07-central-p1]] (information-theory → bayesian)
- [metaphor] "Mollusk-like" parameter space ↔ coordinate freedom in general relativity — the text uses it to motivate "rigidity". — from [[jaynes-2003-probability/ch12-ignorance]] (information-theory → unspecified)
- [structural-analogy] Marginalization (B₁ vs B₂) ↔ Bayesian: sufficiency and ancillary statistics — a statistic whose sampling distribution is free of the nuisance parameter is the structure DSZ exploit. — from [[jaynes-2003-probability/ch15-paradoxes]] (information-theory → bayesian)
- … 67 more bridge lines mention this id (see wiki/kg/bridges.jsonl)
