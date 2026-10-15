---
id: latent-variable
type: concept
fields: [llm, linear-algebra]
fields_strong: [llm, linear-algebra]
n_sources: 3
n_works: 2
tiers: [reference, core]
grounding: digests
sources: [deisenroth-2020-mml/ch10-dimensionality, prince-2023-udl/ch01-introduction, prince-2023-udl/ch14-unsupervised]
raw_ids: [latent variable]
generated_by: build_kg.py
---

# latent-variable

## Definitions in the sources

### llm

- [[prince-2023-udl/ch01-introduction]] (p. 9): a few underlying variables, with a simple distribution, that a network maps to data [new]
- [[prince-2023-udl/ch14-unsupervised]] (p. 269): unseen, usually lower-dimensional variable capturing a dataset's structure [new]

### linear-algebra

- [[deisenroth-2020-mml/ch10-dimensionality]] (p. 340): an unobserved low-dimensional cause $z$ of the observed $x$ [as `latent variable`; new]

## Instances that use it

- [[error-correcting-code-as-latent-variable-model]] — source bits are latent; $\mathbf G$ normally known in advance — from [[mackay-2003-information/ch34-independent]]
- [[em-student-regression]] — scale-mixture latent variables turn robust regression into weighted least squares — from [[murphy-2023-pml2/ch06-optimization-p2]]
- [[face-latent-variables]] — roughly 42 face muscles; most variation in images of one person in the same lighting can be described with just 42 numbers (fig. 1.9 caption) — from [[prince-2023-udl/ch01-introduction]]
- [[image-interpolation]] — interpolating latent variables between two real images — from [[prince-2023-udl/ch01-introduction]]
- [[transformer-decoder-as-autoregressive-generator]] — probabilistic generative model without latent variables — from [[prince-2023-udl/ch14-unsupervised]]
- [[mixture-of-gaussians]] — discrete latent variable giving a multi-modal Pr(x) — from [[prince-2023-udl/ch17-variational]]

## Candidate bridges

- [structural-analogy] Constraint matrix suitable for factor analysis ↔ psychometrics/latent-variable modelling: an organizing dimension shows up as shared correlation — the author himself links the two (p. 32) — from [[converse-1964-beliefsystems/ch02-sections]] (political-science → other:statistics)
- [metaphor] "Latent concepts" as hidden causes of word choice ↔ latent-variable models in social science. — from [[deerwester-1990-lsa/main]] (linear-algebra → unspecified)
- [metaphor] Canonic components as latent "factors" ↔ latent-variable models in social science. — from [[eckart-1936-lowrank/main]] (linear-algebra → unspecified)
- [structural-analogy] Latent-variable regression via $y=F_0^{-1}(u)$ ↔ inverse-CDF sampling (p. 515). — from [[gelman-2013-bda3/ch21-gaussian]] (bayesian → unspecified)
- [structural-analogy] Mismeasured confounder as surrogate for unmeasured confounder ↔ Bayesian latent-variable models: observed indicator of a latent true variable — both treat the data as noisy proxies of a hidden quantity. — from [[hernan-2020-whatif/ch09-measurement]] (bayesian → bayesian)
- [structural-analogy] Hidden units inducing higher-order visible correlations ↔ bayesian: latent-variable and hierarchical models explaining dependence among observables. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → bayesian)
- [structural-analogy] Puncturing/state variables ↔ bayesian: latent variables that are marginalized, not observed. — from [[mackay-2003-information/ch49-repeat]] (information-theory → bayesian)
- [structural-analogy] E step with expected counts ↔ latent-variable MLE: both use posterior probabilities of the hidden variables, in (4.54) and in (4.62). — from [[murphy-2023-pml2/ch04-graphical-p1]] (bayesian → other:latent-variable-mle)
- [structural-analogy] EM's latent scales $z_n$ and weights $\lambda_n$ ↔ hierarchical models: a per-observation latent variable controls how much each point influences the fit. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → bayesian)
- [structural-analogy] Probit latent-variable model ↔ economic choice theory: threshold on a latent utility plus noise (p. 621). — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → economics-finance)
- [structural-analogy] Blocked Gibbs for LDS ↔ Gibbs sampling in hierarchical models: alternate latent variables and parameters. — from [[murphy-2023-pml2/ch29-state-p2]] (bayesian → bayesian)
- [structural-analogy] Analysis-by-synthesis (posterior $p_\theta(z\mid x)$ as representation) ↔ Bayesian inference: the representation is a posterior summary of latent variables. — from [[murphy-2023-pml2/ch32-representation]] (bayesian → bayesian)
- [structural-analogy] Abduction step (update $P(U)$ by evidence) ↔ Bayesian inference: posterior over latent variables given data, then prediction from it. Updating the latent $U$ from evidence and then predicting uses the same logic as posterior-then-predictive, but with an intervention step in between. — from [[pearl-2016-primer/ch04-counterfactuals]] (bayesian → bayesian)
- [structural-analogy] Abduction (infer $U$ from observed data) ↔ Bayesian inference: posterior over latent variables given evidence — here $U$ is solved exactly because functions are deterministic. — from [[pearl-2018-bookofwhy/ch08-counterfactuals]] (bayesian → bayesian)
- [structural-analogy] Wyner's common information as a minimal "common cause" $U$ ↔ causal modelling: shared latent variable that makes $A$ and $B$ conditionally independent. — from [[polyanskiy-2025-information/ch28-rate]] (information-theory → bayesian)
- [metaphor] Latent-variable interpolation (p. 10) ↔ llm: embedding geometry — moving between points in a learned low-dimensional space. — from [[prince-2023-udl/ch01-introduction]] (llm → llm)
- [structural-analogy] Latent-variable augmentation (probit, mixtures, slice sampler) ↔ EM's missing-data completion: both add unobserved variables to make conditionals easy. — from [[robert-2011-mcmc/main]] (bayesian → other:ems-missing-data-completion)
- [structural-analogy] Thresholded metric creates a jump ↔ measurement theory: applying a step function to a continuous latent variable gives an apparent discontinuity. — from [[schaeffer-2023-mirage/main]] (llm → other:statistics)
- [structural-analogy] Latent document-level concept ↔ topic models (LDA): the paper itself notes this shared latent-variable structure (p. 2), but uses no explicit inference algorithm. — from [[xie-2022-icl/main]] (llm → other:topic-models-lda)
