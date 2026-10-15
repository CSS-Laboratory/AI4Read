---
id: hierarchical-model
type: concept
fields: [bayesian, political-science]
n_sources: 30
tiers: [core, reference, deep]
grounding: digests
sources: [blei-2017-variational/main-p2, gelman-2013-bda3/appa-standard, gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch04-asymptotics, gelman-2013-bda3/ch05-hierarchical, gelman-2013-bda3/ch06-model, gelman-2013-bda3/ch08-modeling, gelman-2013-bda3/ch09-decision, gelman-2013-bda3/ch11-basics, gelman-2013-bda3/ch13-modal, gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch15-hierarchical, gelman-2013-bda3/ch18-models, gelman-2013-bda3/ch19-parametric, grimmer-2022-textasdata/ch06-multinomial, mcelreath-2020-rethinking/ch01-golem, mcelreath-2020-rethinking/ch07-interactions, mcelreath-2020-rethinking/ch11-monsters, mcgrayne-2011-theory/ch10-46, mcgrayne-2011-theory/ch13-cold, mcgrayne-2011-theory/ch16-eureka, murphy-2023-pml2/ch03-statistics-p3, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch17-bayesian, murphy-2023-pml2/ch19-beyond, murphy-2023-pml2/ch21-variational, robert-2011-mcmc/main, tenenbaum-2011-grow/main]
raw_ids: [Hierarchical   model]
generated_by: build_kg.py
---

# hierarchical-model

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p2]] (pp. 27, 31): ARD and LDA both place priors on parameters of lower-level distributions
- [[gelman-2013-bda3/appa-standard]] (pp. 577, 582): the normal mixture property (and its multivariate form) gives the marginal law of a normal with a normally distributed mean
- [[gelman-2013-bda3/appc-computation]] (pp. 592, 597): school effects θ_j drawn from N(μ, τ²), with a normal likelihood having known σ_j
- [[gelman-2013-bda3/ch01-probability]] (p. 5): a model for data with several levels of units, with exchangeability at each level
- [[gelman-2013-bda3/ch02-single]] (pp. 46, 50): only previewed: α, β treated as unknowns (Chapter 5)
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 93, 96): preferred for many parameters and multiple comparisons
- [[gelman-2013-bda3/ch05-hierarchical]] (p. 101): observables given parameters, parameters given hyperparameters; here a population distribution on the $\theta_j$ with hyperprior on $\phi$
- [[gelman-2013-bda3/ch06-model]] (p. 155): batches of parameters compared with their prior as a check
- [[gelman-2013-bda3/ch08-modeling]] (pp. 207, 209, 211): used across strata, clusters and groups
- [[gelman-2013-bda3/ch09-decision]] (pp. 241, 250): used for incentives (surveys → conditions) and radon (houses → counties → geological types)
- [[gelman-2013-bda3/ch11-basics]] (pp. 288–290): the hierarchical normal model with unknown σ² is the chapter's worked example
- [[gelman-2013-bda3/ch13-modal]] (p. 326): group parameters drawn from a population distribution; the main example class
- [[gelman-2013-bda3/ch14-introduction]] (p. 373): mentioned as the setting where these computations recur (Chapter 15)
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 382): parameters for groups drawn from a population distribution learned from data; here, regression coefficients in batches
- [[gelman-2013-bda3/ch18-models]] (p. 458): per-survey means $\mu_s$ regressed on survey covariates, with common Ψ
- [[gelman-2013-bda3/ch19-parametric]] (p. 475): here: individual physiological parameters drawn from a population distribution with learned mean and SD (p. 479); the assay uses no pooling instead
- [[mcelreath-2020-rethinking/ch01-golem]] (p. 14): multilevel model; a parameter is a placeholder for a missing model
- [[mcelreath-2020-rethinking/ch07-interactions]] (p. 211): described as essentially massive interaction models
- [[mcelreath-2020-rethinking/ch11-monsters]] (p. 347): named as the second strategy for over-dispersion; developed in Chapter 12 [as `Hierarchical   model`]
- [[mcgrayne-2011-theory/ch10-46]] (p. 131): Bayesians' "hyperdistribution" reading of Stein
- [[mcgrayne-2011-theory/ch13-cold]] (p. 171): Wallace's description: historical data give between-county variation, which supplies the priors
- [[mcgrayne-2011-theory/ch16-eureka]] (pp. 214, 216): Lindley–Smith way of modelling a process in stages; used in the diesel meta-analysis
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 114): here, models whose group parameters share a prior with hyperparameters $\xi$; EB fits $\xi$ by a point estimate
- [[murphy-2023-pml2/ch15-generalized]] (p. 625): group parameters drawn from a shared prior
- [[murphy-2023-pml2/ch17-bayesian]] (p. 679): task weights = shared parent + per-layer-scaled offset, Eq. (17.57)
- [[murphy-2023-pml2/ch19-beyond]] (pp. 754–755): population-level $w^0$ generating task/environment parameters $w^j$
- [[murphy-2023-pml2/ch21-variational]] (p. 809): stacked latent layers; HVAE
- [[robert-2011-mcmc/main]] (p. 7): random-effects model (2) as the paradigm case for Gibbs
- [[tenenbaum-2011-grow/main]] (p. 1282): HBM: multiple levels, each generating a distribution for the level below; priors on priors

### political-science

- [[grimmer-2022-textasdata/ch06-multinomial]] (p. 125): model with stacked layers of latent variables, e.g. a prior on $\alpha$ [new]

## Instances that use it

- [[hierarchical-model-curvature]] — high-curvature neighborhoods characteristic of hierarchical models; centered/non-centered switch — from [[betancourt-2017-hmc/main-p3]]
- [[student-t-hierarchical-model]] — t extension with fixed ν = 4, or ν unknown via Metropolis — from [[gelman-2013-bda3/appc-computation]]
- [[adolescent-smoking-models]] — Table 6.1 compares two hierarchical models on three statistics — from [[gelman-2013-bda3/ch06-model]]
- [[home-radon-decision]] — hierarchical model plus measure/remediate tree, from single homes to national strategy comparison — from [[gelman-2013-bda3/ch09-decision]]
- [[beta-blocker-meta-analysis]] — bivariate normal hierarchical model on logits — from [[gelman-2013-bda3/ch16-generalized]]

## Candidate bridges

- [structural-analogy] Empirical Bayes as keeping the prior from carrying extra information ↔ hierarchical models: priors learned from data. — from [[efron-1986-bayesian/main]] (bayesian → other)
- [structural-analogy] Negative binomial / beta-binomial as overdispersed versions of Poisson / binomial ↔ bayesian: hierarchical models, where letting a parameter vary across units widens the marginal distribution. — from [[gelman-2013-bda3/appa-standard]] (bayesian → bayesian)
- [structural-analogy] $\operatorname{var}(u)=E(\operatorname{var}(u|v))+\operatorname{var}(E(u|v))$ ↔ hierarchical models: within-group vs. between-group variation, which is the information partial pooling uses. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → other)
- [structural-analogy] Posterior mean shrinks toward the population mean in the mother–daughter example ↔ partial pooling in hierarchical models: both weight own data against the population distribution. — from [[gelman-2013-bda3/ch04-asymptotics]] (bayesian → other)
- [structural-analogy] Stratum-level shrinkage in the CBS poll ↔ Bayesian inference: partial pooling in the Ch. 5 hierarchical models. — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → bayesian)
- [same-math] Normal–normal update (9.7) ↔ hierarchical models: precision-weighted average, as in partial pooling/shrinkage — the same weighted average of a group-level mean and noisy data. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → other)
- [structural-analogy] Parameter expansion (extra unidentified scale) ↔ hierarchical models: the chapter points to Section 15.5 for the hierarchical use. — from [[gelman-2013-bda3/ch12-computationally]] (bayesian → other)
- [structural-analogy] Heavy-tailed prior on group effects ↔ Hierarchical models: tail shape of the population distribution sets how strongly extreme groups are shrunk — from [[gelman-2013-bda3/ch17-models]] (bayesian → other)
- [same-math] Gamma–Poisson and beta–binomial mixtures ↔ Hierarchical models: unit-level rates drawn from a population distribution — from [[gelman-2013-bda3/ch17-models]] (bayesian → other)
- [structural-analogy] Separating prior uncertainty about the mean ($S$) from population variation ($\tau_0$) ↔ hierarchical-model hyperpriors: uncertainty about the population average versus spread among groups. — from [[gelman-2013-bda3/ch19-parametric]] (bayesian → other)
- [structural-analogy] Predictor-dependent mixture weights (22.15) ↔ hierarchical models with group-varying parameters: the "group" membership probability varies smoothly with $x$. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → other)
- [structural-analogy] HDP shared atoms with varying weights ↔ hierarchical models: groups borrow strength from a common parent. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → other)
- [metaphor] Pseudo-data shrinking sparse authors toward $\alpha/\alpha_0$ ↔ borrowing strength across units in hierarchical models of political data. — from [[grimmer-2022-textasdata/ch06-multinomial]] (political-science → unspecified)
- [structural-analogy] individual-specific random probability $Q_{Y^a}$ with population mean $E[Q]$ ↔ Bayesian: hierarchical model with per-unit parameters drawn from a population. — from [[hernan-2020-whatif/ch01-definition]] (bayesian → bayesian)
- [structural-analogy] sequential refinement of $Y^{a_0,a_1,a_2,a_3}$ (Technical Point 3.2) ↔ hierarchical models: unspecified components $A_j^{a_0=1}$ are random quantities whose population distribution drives transportability. — from [[hernan-2020-whatif/ch03-observational]] (bayesian → other)
- [structural-analogy] Pooling stratum-specific effects with variance-reducing weights ↔ bayesian: partial pooling/shrinkage in hierarchical models — both combine group estimates to reduce noise, but the text uses fixed-weight averages, not a prior. — from [[hernan-2020-whatif/ch04-effect]] (bayesian → bayesian)
- [structural-analogy] Effect modification by V ↔ hierarchical models: group-specific effects of A varying across levels of V. — from [[hernan-2020-whatif/ch05-interaction]] (bayesian → other)
- [structural-analogy] Frailty $U$ and conditioning on survival ↔ hierarchical models: a latent trait shapes who remains in the sample. — from [[hernan-2020-whatif/ch08-selection]] (bayesian → other)
- [structural-analogy] Hidden factor $H$ making a DAG causal ↔ hierarchical models with latent parameters — both add unobserved variables to make the structure coherent. — from [[hernan-2020-whatif/ch09-measurement]] (bayesian → unspecified)
- [structural-analogy] B's use of other intervals to estimate $s$, which then sharpens each $n_k$ ↔ bayesian: partial pooling in hierarchical models — from [[jaynes-2003-probability/ch06-elementary-p2]] (information-theory → bayesian)
- [structural-analogy] Integrating out $\sigma$ as a nuisance parameter ↔ Bayesian: hierarchical models averaging over group-level uncertainty (p. 219) — from [[jaynes-2003-probability/ch07-central-p1]] (information-theory → bayesian)
- [structural-analogy] Mixture-of-Gaussians resolution as an ill-posed inverse problem ↔ Bayesian: hierarchical models and regularizing priors — prior information selects among many consistent decompositions. — from [[jaynes-2003-probability/ch07-central-p2]] (information-theory → bayesian)
- [structural-analogy] Predictive variance V = V₀ + extra term (18.82) ↔ bayesian: hierarchical model / total variance — parameter uncertainty adds to sampling variance — from [[jaynes-2003-probability/ch18-p]] (information-theory → bayesian)
- [same-math] Mixture model $uG+(1-u)B$ with latent q_i ↔ bayesian: hierarchical model with exchangeable latent indicators (de Finetti). — from [[jaynes-2003-probability/ch21-outliers]] (information-theory → bayesian)
- [structural-analogy] Hidden units inducing higher-order visible correlations ↔ bayesian: latent-variable and hierarchical models explaining dependence among observables. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → bayesian)
- [same-math] Multilevel model: parameter as placeholder for a model ↔ bayesian: hierarchical model — parameters drawn from a higher-level distribution. — from [[mcelreath-2020-rethinking/ch01-golem]] (bayesian → bayesian)
- [structural-analogy] One intercept per category via an index ↔ hierarchical models: the unique-intercept form is the one the text says is common in multilevel models (p. 158). — from [[mcelreath-2020-rethinking/ch05-multivariate-p2]] (bayesian → other)
- [structural-analogy] interaction as slope conditional on cluster (p. 211) ↔ hierarchical models: group-specific slopes drawn from a population. — from [[mcelreath-2020-rethinking/ch07-interactions]] (bayesian → other)
- [structural-analogy] Vector of intercepts `a[actor]` ↔ hierarchical models: the same indexing structure that multilevel models will use (p. 299) — from [[mcelreath-2020-rethinking/ch10-counting]] (bayesian → other)
- [structural-analogy] Beta-binomial / gamma-Poisson integrals ↔ [[hierarchical-model]] (Bayesian): both let each row have its own parameter drawn from a distribution; the next chapter develops multilevel models. — from [[mcelreath-2020-rethinking/ch11-monsters]] (bayesian → bayesian)
- [structural-analogy] Shrinkage of noisy $D_{\text{EST}}$ toward the regression line ↔ hierarchical models: more uncertain units are pooled more. — from [[mcelreath-2020-rethinking/ch14-missing]] (bayesian → other)
- [structural-analogy] Credibility/Stein–James formula ↔ bayesian: partial pooling in hierarchical models — both pull related estimates toward a mean. — from [[mcgrayne-2011-theory/ch10-46]] (bayesian → bayesian)
- [structural-analogy] "Borrowing strength" across similar counties ↔ bayesian: partial pooling in hierarchical models — both pull sparse units toward information from related units. — from [[mcgrayne-2011-theory/ch13-cold]] (bayesian → bayesian)
- [structural-analogy] Aleatoric vs epistemic uncertainty ↔ hierarchical models: a flat versus peaky prior over the outcome distribution — from [[murphy-2023-pml2/ch02-probability-p1]] (bayesian → other)
- [structural-analogy] de Finetti's hidden common cause ↔ hierarchical models: shared latent θ makes observations conditionally iid (p. 72). — from [[murphy-2023-pml2/ch03-statistics-p1]] (bayesian → other)
- [structural-analogy] EM's latent scales $z_n$ and weights $\lambda_n$ ↔ hierarchical models: a per-observation latent variable controls how much each point influences the fit. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → other)
- [structural-analogy] Rational quadratic kernel as a gamma mixture of SE length scales ↔ hierarchical model: a hyperprior over a scale parameter (p. 688). — from [[murphy-2023-pml2/ch18-gaussian-p1]] (bayesian → other)
- [structural-analogy] Hierarchical Bayesian DG and meta-learning models (Figs. 19.13, 19.15) ↔ Hierarchical models / partial pooling: task parameters drawn from a shared population level. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → other)
- [structural-analogy] Hierarchical VAE with fixed encoder ↔ hierarchical model: layers of latents, but a non-learned top-down pass. — from [[murphy-2023-pml2/ch25-diffusion]] (bayesian → other)
- [structural-analogy] Scale mixture over $\epsilon$ (28.12) ↔ hierarchical model: a latent group-level variance integrated out gives heavy-tailed marginals — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → other)
- [structural-analogy] Blocked Gibbs for LDS ↔ Gibbs sampling in hierarchical models: alternate latent variables and parameters. — from [[murphy-2023-pml2/ch29-state-p2]] (bayesian → other)
- [structural-analogy] stochastic block model's latent community labels ↔ hierarchical models: latent group-level structure explains observed data. — from [[murphy-2023-pml2/ch30-graph]] (bayesian → other)
- [structural-analogy] Success = talent + luck, with regression toward the mean ↔ partial pooling/shrinkage in hierarchical models: noisy extreme values are pulled toward the average. — from [[pearl-2018-bookofwhy/ch02-buccaneers]] (bayesian → other)
- [metaphor] "Linear Wonderland" estimates failing under interaction ↔ Hierarchical models: a single global coefficient hides group-level differences — from [[pearl-2018-bookofwhy/ch09-mediation-p2]] (bayesian → other)
- [structural-analogy] Transportability with $S$ nodes ↔ bayesian: hierarchical models, where populations differ in some parameters and share others — both decide what to borrow across groups. — from [[pearl-2018-bookofwhy/ch10-big]] (bayesian → bayesian)
- [structural-analogy] Top level of an HBM supplying the hypothesis space for the level below ↔ bayesian: hierarchical models and partial pooling — higher-level parameters shared across groups are informed by all groups. — from [[tenenbaum-2011-grow/main]] (bayesian → bayesian)
