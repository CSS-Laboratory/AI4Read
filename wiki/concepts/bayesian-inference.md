---
id: bayesian-inference
type: concept
fields: [bayesian, control-theory, decision-game-theory, linear-algebra, llm]
fields_strong: [bayesian, control-theory, decision-game-theory, linear-algebra, llm]
n_sources: 4
n_works: 4
tiers: [core, deep, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch08-when, kahneman-2011-thinking/ch16-causes, prince-2023-udl/ch09-regularization, sarkka-2023-bayesianfiltering/ch02-bayesian]
generated_by: build_kg.py
---

# bayesian-inference

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 17): parameters are random variables; probability is certainty in a single trial [new; work fields: control-theory, bayesian]

### decision-game-theory

- [[kahneman-2011-thinking/ch16-causes]] (pdf 163): combine a prior (base rate) with case evidence to get a posterior [new]

### linear-algebra

- [[deisenroth-2020-mml/ch08-when]] (p. 274): compute the full posterior p(θ | X) (8.22) and predict by (8.23) [new]

### llm

- [[prince-2023-udl/ch09-regularization]] (p. 150): treat parameters as a distribution and average predictions over it [new]

## Candidate bridges

- [structural-analogy] Script-based constraints on relevance ↔ priors in Bayesian inference: shared background knowledge shrinks the hypothesis space (the author does not use Bayesian language). — from [[apperly-2011-mindreaders/ch06-cognitive]] (theory-of-mind → bayesian)
- [same-math] Prop. 9 ↔ Bayesian inference: posterior $\propto x^p(1-x)^q$ on $[0,1]$ under a uniform prior — the curve drawn is this function. — from [[bayes-1763-essay/main]] (bayesian → bayesian)
- [structural-analogy] Stratum-level shrinkage in the CBS poll ↔ Bayesian inference: partial pooling in the Ch. 5 hierarchical models. — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → bayesian)
- [structural-analogy] identifying assumption external to the data ↔ Bayesian inference: where data fit many effect values, a prior or assumption must supply the rest (here the prior is a point-mass-like assumption of exchangeability). — from [[hernan-2020-whatif/ch03-observational]] (bayesian → bayesian)
- [structural-analogy] Standardization $\sum_l \mathrm{E}[Y|A,L=l]\Pr[L=l]$ ↔ Bayesian inference: marginalizing a nuisance variable by averaging over its distribution. — from [[hernan-2020-whatif/ch07-confounding]] (bayesian → bayesian)
- [structural-analogy] Collider conditioning inducing association ↔ Bayesian inference: observing a shared effect makes independent causes dependent in the posterior. — from [[hernan-2020-whatif/ch08-selection]] (bayesian → bayesian)
- [structural-analogy] Testing a known non-zero $\alpha_1$ for sensitivity analysis ↔ Bayesian inference: a prior or fixed value for a bias parameter, with results shown across its range. — from [[hernan-2020-whatif/ch14-g]] (bayesian → bayesian)
- [structural-analogy] Nuisance parameters in outcome versus treatment models ↔ Bayesian inference: parameters not of interest are handled in a separate model component (the unit does not discuss this). — from [[hernan-2020-whatif/ch15-outcome]] (bayesian → bayesian)
- [structural-analogy] Non-identified parameter needs an extra untestable assumption ($\beta_1=0$) ↔ Bayesian inference: when data cannot identify a parameter, the posterior depends on the prior — both fill a gap the data cannot. — from [[hernan-2020-whatif/ch16-instrumental]] (bayesian → bayesian)
- [structural-analogy] Weak instrument and small denominator blow up the ratio estimate ↔ Bayesian inference: weakly identified parameters give unstable, highly variable estimates. — from [[hernan-2020-whatif/ch16-instrumental]] (bayesian → bayesian)
- [structural-analogy] Lasso/ridge penalty (p. 243) ↔ Bayesian inference: priors that pull coefficients toward zero — both stabilize estimates by trading variance against bias. — from [[hernan-2020-whatif/ch18-variable]] (bayesian → bayesian)
- [structural-analogy] Minimum-error decoding with unequal codeword probabilities (Ex. 15.10) ↔ Bayesian inference: prior over codewords combined with the channel likelihood — the best decoder depends on both. — from [[mackay-2003-information/ch15-further]] (information-theory → bayesian)
- [structural-analogy] Message passing on a trellis ↔ Bayesian inference: sum-product on a chain (the chapter reuses Chapter 16's local message passing, p. 248). — from [[mackay-2003-information/ch17-communication]] (information-theory → bayesian)
- [structural-analogy] Prior strength as $n=1/\sigma^2_{\text{post}}$ ↔ Bayesian inference: conjugate priors act like pseudo-observations (Beta–Binomial). — from [[mcelreath-2020-rethinking/ch04-linear-p1]] (bayesian → bayesian)
- [structural-analogy] Gaussian as the least-committal shape given mean and variance ↔ Bayesian inference: maximum entropy (developed later in the book). — from [[mcelreath-2020-rethinking/ch04-linear-p1]] (bayesian → bayesian)
- [same-math] `lm` with flat priors ↔ Bayesian inference: under flat priors and a Gaussian likelihood the OLS estimates equal the MAP estimates (p. 159). — from [[mcelreath-2020-rethinking/ch05-multivariate-p2]] (bayesian → bayesian)
- [structural-analogy] Laplace's switch to frequentism with abundant data ↔ Bayesian inference: our gloss on the prior's role in the Bayesian method; the author says only that with large amounts of data both approaches generally give much the same results. — from [[mcgrayne-2011-theory/ch02-man]] (bayesian → bayesian)
- [structural-analogy] prior swamped by strong data ↔ Bayesian inference: posterior insensitive to prior with large samples (the astronaut's lunar-dust example, p. 161). — from [[mcgrayne-2011-theory/ch12-who]] (bayesian → bayesian)
- [same-math] Dirichlet prior over die probabilities ↔ Bayesian inference: Dirichlet-multinomial conjugate prior — the text treats Dir as the multivariate beta; conjugacy itself is not stated here — from [[murphy-2023-pml2/ch02-probability-p1]] (bayesian → bayesian)
- [same-math] Dirichlet-multinomial update of CPT rows ↔ Bayesian inference: posterior mean $=(N+\alpha)/\sum(N+\alpha)$ is the conjugate update. — from [[murphy-2023-pml2/ch04-graphical-p1]] (bayesian → bayesian)
- [same-math] Abduction step ↔ Bayesian inference: the posterior over latent noise $p(U_i|\text{evidence})$ is ordinary Bayesian conditioning, then propagated forward. — from [[murphy-2023-pml2/ch04-graphical-p3]] (bayesian → bayesian)
- [same-math] Reverse-KL/I-projection ↔ variational inference in Bayesian inference (canon: KL divergence & ELBO; not developed in this unit): the KL being minimized is $D_{KL}(q\|p)$. — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → bayesian)
- [structural-analogy] NGD with Fisher preconditioner ↔ Bayesian inference: the text says it is equivalent to EKF sequential inference in the online exponential-family case (p. 281) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → bayesian)
- [same-math] EM's ELBO (6.140–6.145) ↔ Bayesian inference: variational ELBO and KL to the posterior — the text itself says this bound is the basis of variational inference. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → bayesian)
- [metaphor] Catastrophic forgetting vs regularization to past posterior ↔ Sequential updating: yesterday's posterior as today's prior (the author says online Bayesian inference is of this type, p. 763). — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → bayesian)
- [structural-analogy] Structure discovery $p(\boldsymbol z|\mathcal D)$ over graphs ↔ Bayesian inference over latent structure — a posterior over model structure. — from [[murphy-2023-pml2/ch20-generative]] (bayesian → unspecified)
- [same-math] Responsibilities $r_{nk}$ (28.8) ↔ Bayesian inference: posterior over a discrete hypothesis from prior × likelihood, normalised — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → bayesian)
- [structural-analogy] Analysis-by-synthesis (posterior $p_\theta(z\mid x)$ as representation) ↔ Bayesian inference: the representation is a posterior summary of latent variables. — from [[murphy-2023-pml2/ch32-representation]] (bayesian → bayesian)
- [same-math] Bayes' rule with prior ↔ Bayesian inference: posterior ∝ likelihood × prior — same formula (1.8), with the hypothesis as $A$ and the evidence as $B$. — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → bayesian)
- [structural-analogy] Collider conditioning ↔ Bayesian inference: "explaining away" of one cause given the effect (named on p. 51) — the posterior over causes becomes dependent. — from [[pearl-2016-primer/ch02-graphical]] (bayesian → bayesian)
- [structural-analogy] Abduction step (update $P(U)$ by evidence) ↔ Bayesian inference: posterior over latent variables given data, then prediction from it. Updating the latent $U$ from evidence and then predicting uses the same logic as posterior-then-predictive, but with an intervention step in between. — from [[pearl-2016-primer/ch04-counterfactuals]] (bayesian → bayesian)
- [structural-analogy] Do-calculus proof as symbol manipulation ↔ Bayesian inference: both turn one kind of probability into another by licensed rewrites (conditioning, Bayes' theorem) — different rules, same "format change" spirit. — from [[pearl-2018-bookofwhy/ch07-beyond]] (bayesian → bayesian)
- [structural-analogy] Abduction (infer $U$ from observed data) ↔ Bayesian inference: posterior over latent variables given evidence — here $U$ is solved exactly because functions are deterministic. — from [[pearl-2018-bookofwhy/ch08-counterfactuals]] (bayesian → bayesian)
- [structural-analogy] ToMnet embedding as posterior ↔ Bayesian inference: Bayes-optimal posterior over agent type — compared with Bayes-optimal curves only in the Dirichlet case (pdf 3) — from [[rabinowitz-2018-machine-tom/main]] (theory-of-mind → bayesian)
- [same-math] MI as expected posterior-vs-prior KL, E_y[D_KL(p(X|y)‖p(X))] ↔ Bayesian inference: expected information gain from an observation — same expression (Eq. 6.51). — from [[stone-2022-information/ch06-mutual]] (information-theory → bayesian)
