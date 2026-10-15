---
id: likelihood
type: concept
fields: [bayesian, information-theory, llm, analytic-philosophy, decision-game-theory, linear-algebra]
fields_strong: [bayesian, information-theory, llm, analytic-philosophy, decision-game-theory, linear-algebra]
n_sources: 54
n_works: 15
tiers: [core, reference, deep]
grounding: digests
sources: [bayes-1763-essay/main, deisenroth-2020-mml/ch09-linear, efron-1986-bayesian/main, gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch04-asymptotics, gelman-2013-philosophy/main, gelman-2020-workflow/main-p3, griffiths-2006-optimal/main, jaynes-2003-probability/ch04-elementary, jaynes-2003-probability/ch05-queer, jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch07-central-p1, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch16-orthodox, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, jaynes-2003-probability/ch19-physical, jaynes-2003-probability/ch20-model, jaynes-2003-probability/ch21-outliers, mackay-2003-information/ch01-introduction, mackay-2003-information/ch02-probability, mackay-2003-information/ch03-more, mackay-2003-information/ch11-error, mackay-2003-information/ch12-hash, mackay-2003-information/ch21-exact, mackay-2003-information/ch22-maximum, mackay-2003-information/ch25-exact, mackay-2003-information/ch28-model, mackay-2003-information/ch34-independent, mackay-2003-information/ch35-random, mackay-2003-information/ch36-decision, mackay-2003-information/ch37-bayesian, mackay-2003-information/ch41-learning, mackay-2003-information/ch43-boltzmann, mackay-2003-information/ch44-supervised, mackay-2003-information/ch45-gaussian, mackay-2003-information/ch46-deconvolution, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch04-linear-p1, mcelreath-2020-rethinking/ch04-linear-p2, mcelreath-2020-rethinking/ch06-overfitting-p1, mcgrayne-2011-theory/ch01-causes, mcgrayne-2011-theory/ch02-man, mcgrayne-2011-theory/ch06-arthur, mcgrayne-2011-theory/ch07-tool, mcgrayne-2011-theory/ch15-navy, murphy-2023-pml2/ch02-probability-p1, murphy-2023-pml2/ch03-statistics-p1, pearl-2018-bookofwhy/ch03-evidence, prince-2023-udl/ch23-probability, tenenbaum-2011-grow/main]
raw_ids: [Likelihood]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# likelihood

## Canon spine entry

- **Likelihood** (bayesian): how probable the observed data are under each possible parameter value; a function of the parameter, not a probability over it (UG)

## Definitions in the sources

### bayesian

- [[bayes-1763-essay/main]] (pp. 17, 20): the binomial $Ex^pr^q$ as a function of the single-trial chance $x$
- [[efron-1986-bayesian/main]] (p. 3): Efron says tree-building has no effect on the likelihood function, so it makes no difference to the Bayesian
- [[gelman-2013-bda3/ch01-probability]] (pp. 7, 10): $p(y|\theta)$ as a function of $\theta$ for fixed $y$; the authors stress it is not a probability distribution
- [[gelman-2013-bda3/ch02-single]] (p. 34): as a function of θ, e.g. $\theta^a(1-\theta)^b$ in the binomial case
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 88–89): dominates the prior for large n; flat for nonidentified parameters
- [[gelman-2013-philosophy/main]] (p. 4): the model's p(y|θ); the full joint distribution makes it a conditional density [work fields: bayesian, analytic-philosophy]
- [[gelman-2020-workflow/main-p3]] (p. 55): here, a binomial likelihood with huge counts can be "too strong" and make the fit sticky
- [[griffiths-2006-optimal/main]] (p. 767): $p(t\mid t_{total})=1/t_{total}$ for $t\le t_{total}$
- [[jaynes-2003-probability/ch04-elementary]] (p. 89): $P(D|HX)$ as a function of $H$ for fixed $D$; not a probability for $H$; constant factors irrelevant [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch05-queer]] (pp. 121, 123): $P(D|H)$; for hypotheses about reports it includes deception mechanisms [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch06-elementary-p1]] (pp. 150, 164, 175): hypergeometric (6.1), binomial (6.67), $p(c|\phi n)$ as a function of $n$ [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch06-elementary-p2]] (pp. 179, 178 fn. 11): $p(c_1|\phi n_1)$ has its maximum at $c_1/\phi$ and falls off for larger $n_1$; a prior can make a large difference only by modulating it near the peak, not its tails [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch07-central-p1]] (p. 216): after the data are in, what remains significant for inference is the likelihood function [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch08-sufficiency]] (p. 250): the only place data enter the posterior [as `Likelihood`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 294): p(D|H); the likelihood ratio sets the evidence shift between two hypotheses [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch16-orthodox]] (p. 494): per Jaynes, with no cogent and detailed prior information, the likelihood determines Jeffreys' best estimators [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 526): the evidence of the data as a function of the parameters; not used by the orthodox tail-area test (p. 523) or by Feller's sampling distributions [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p2]] (p. 533): here $\log L$ as a sum over the actual data points [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch19-physical]] (p. 593): the Gaussian sampling density (19.14) with weights $w_i=1/\langle\delta_i^2\rangle$ [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch20-model]] (p. 602): as used throughout [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch21-outliers]] (pp. 622–623): product of mixture densities (21.12); leave-out versions $L_j$ are good-data likelihoods [work fields: bayesian, information-theory]
- [[mcelreath-2020-rethinking/ch02-small]] (p. 33): formula giving the relative number of ways the data arise for each parameter value; here the binomial
- [[mcelreath-2020-rethinking/ch04-linear-p1]] (pp. 77–78, 81): the first line of a model definition; here $h_i\sim\text{Normal}(\mu,\sigma)$
- [[mcelreath-2020-rethinking/ch04-linear-p2]] (p. 93): the Gaussian line $h_i\sim\text{Normal}(\mu_i,\sigma)$; μ now varies by row
- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 176): here, the joint probability of the observed data; the right accuracy measure
- [[mcgrayne-2011-theory/ch01-causes]] (p. 8): as McGrayne puts it, the probability of competing hypotheses for the fixed observed data
- [[mcgrayne-2011-theory/ch02-man]] (p. 20): $P(E|C)$, the probability of the event given the cause
- [[mcgrayne-2011-theory/ch06-arthur]] (p. 92): Bailey rejects Fisher's maximum likelihood for insurance because it assigns zero probability to nonevents
- [[mcgrayne-2011-theory/ch07-tool]] (p. 104): the part of Bayes' theorem giving the probability of new data
- [[mcgrayne-2011-theory/ch15-navy]] (p. 205): in the Coast Guard system, sensor and weather data turned into likelihood functions
- [[murphy-2023-pml2/ch02-probability-p1]] (p. 8): $p(E|X=k)$, probability of the evidence given each state
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 64): p(D|θ); here Bernoulli/Binomial, proportional in θ
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 103–104): here $P(T\mid D)$, the forward probability, e.g., test sensitivity
- [[tenenbaum-2011-grow/main]] (p. 1280): $P(d\mid h)$, how expected the data are under $h$ relative to other hypotheses

### information-theory

- [[mackay-2003-information/ch01-introduction]] (p. 6): the data-dependent term P(**r** | s) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch02-probability]] (p. 29): $P(\text{data}\mid\text{parameters})$ as a function of the parameters; not a probability distribution over them [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch03-more]] (p. 49): $P(\text{data}|\text{parameter})$ viewed as a function of the parameter [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch11-error]] (p. 179): $P(\mathbf y\mid s)$, used in Shannon's pulse detector [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch12-hash]] (pp. 202–203): here P(datum | hypothesis); a matching bit gives ratio 2; a casting-out-nines match gives 9 only under a random-error model [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch21-exact]] (p. 296): P(data | μ, σ) evaluated at each grid point [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch22-maximum]] (p. 300): probability of the data as a function of the parameters; in practice, work with its log [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch25-exact]] (pp. 324–325): for a memoryless channel, a product of per-bit terms; only the ratio matters for decoding [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch28-model]] (p. 347): as in (28.4) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch34-independent]] (p. 438): $P(D\mid\mathbf G,\mathcal H)$, obtained by marginalizing out latent variables [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch35-random]] (p. 450): probability of data as a function of the parameter, e.g. $L(a)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch36-decision]] (p. 452): $P(d_n\mid x_n)$, a noisy Gaussian measurement [work fields: information-theory, bayesian, decision-game-theory]
- [[mackay-2003-information/ch37-bayesian]] (p. 460): the probability of the data as a function of the parameters, e.g. (37.12) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch41-learning]] (p. 492): $P(D\mid\mathbf w)=\exp(-G)$; the error is minus its log [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch43-boltzmann]] (pp. 522–523): posterior (43.5), of which only the likelihood is used [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch44-supervised]] (p. 529, p. 530): $\beta E_D$ or $G$ is the negative log likelihood [as `Likelihood`; work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch45-gaussian]] (p. 535): $P(\mathbf t_N\mid y(x),\mathbf X_N)$, often separable Gaussian noise [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch46-deconvolution]] (p. 549–550): Gaussian here [work fields: information-theory, bayesian]

### linear-algebra

- [[deisenroth-2020-mml/ch09-linear]] (pp. 291, 293): density of the targets given inputs and parameters. It is normalized in $y$, not in $\theta$ [new]

### llm

- [[prince-2023-udl/ch23-probability]] (p. 451): $Pr(x|y)$ viewed as a function of $y$; need not sum to one [new]

## Instances that use it

- [[gaussian-likelihood-linear-regression]] — Gaussian noise gives least squares (Ex. 8.4–8.5) — from [[deisenroth-2020-mml/ch08-when]]
- [[heart-attack-decision-tree]] — apparent 96.7% versus bootstrap about 70%; the likelihood is unaffected by how the tree was built — from [[efron-1986-bayesian/main]]
- [[hemophilia-carrier-example]] — prior ½, likelihood from unaffected sons, posterior 0.20 and then 0.111 — from [[gelman-2013-bda3/ch01-probability]]
- [[radom-spelling-example]] — priors and likelihoods multiplied to a posterior of 0.673 for 'radom'; disputing the posterior shows missing context — from [[gelman-2013-bda3/ch01-probability]]
- [[t-model-as-normal-mixture]] — t likelihood written with auxiliary variances $V_i$; Gibbs steps, then parameter expansion with $\alpha$ — from [[gelman-2013-bda3/ch12-computationally]]
- [[binomial-vs-negative-binomial-sampling]] — same likelihood for θ, different generative models and predictive checks — from [[gelman-2020-workflow/main-p1]]
- [[stewart-esp-experiment]] — 25.8 sd result and its likelihoods; why deception wins — from [[jaynes-2003-probability/ch05-queer]]
- [[tom-w-problem]] — three tasks (no-information likelihood, similarity, probability) showing probability judged as similarity — from [[kahneman-2011-thinking/ch14-tom]]
- [[two-urn-likelihood-principle]] — Examples 2.10 and 2.11 — from [[mackay-2003-information/ch02-probability]]
- [[blood-evidence]] — likelihood ratio 0.83 for Oliver, 50 for Alberto; general result $(n_O/N)/p_O$ — from [[mackay-2003-information/ch03-more]]
- [[phone-number-busy-signal]] — likelihood ratio of 100–1000 from a busy signal — from [[mackay-2003-information/ch03-more]]
- [[euro-coin-spin]] — 140 and 141 heads in 250 spins; p-values vs. likelihood ratios — from [[mackay-2003-information/ch03-more]]
- [[kmeans-spike-kaboom]] — a cluster on one point makes the likelihood infinite — from [[mackay-2003-information/ch22-maximum]]
- [[hamming-7-4-trellis]] — worked decoding with likelihoods $(0.1,0.4,0.9,0.1,0.1,0.1,0.3)$ — from [[mackay-2003-information/ch25-exact]]
- [[gaussian-channel-likelihood-ratio]] — $\exp(2xy_n/\sigma^2)$ — from [[mackay-2003-information/ch25-exact]]
- [[gp-evidence-multimodality]] — Figure 45.2, two local maxima of the likelihood — from [[mackay-2003-information/ch45-gaussian]]
- [[gaussian-linear-deblurring]] — Gaussian prior and likelihood give a closed-form $\mathbf f_{\rm MP}$ — from [[mackay-2003-information/ch46-deconvolution]]
- [[globe-tossing]] — W L W W W L W L W (6 W, 3 L); binomial likelihood; grid and quadratic approximation — from [[mcelreath-2020-rethinking/ch02-small]]
- [[cars-waic-calculation]] — step-by-step WAIC with 50 × 1000 log-likelihood matrix — from [[mcelreath-2020-rethinking/ch06-overfitting-p2]]
- [[coin-fair-bayes-factor]] — $M_0$ vs $M_1$, $N=5$, marginal likelihood vs heads — from [[murphy-2023-pml2/ch03-statistics-p3]]
- [[poisson-categorical-cmgf]] — Poisson and softmax likelihood moments for CMGF — from [[murphy-2023-pml2/ch08-gaussian-p2]]
- [[logistic-factor-ep]] — logistic likelihood with Gaussian cavity (Fig. 10.15) — from [[murphy-2023-pml2/ch10-variational-p2]]
- [[rademacher-free-random-label-cifar]] — Zhang et al.: CNN fits random CIFAR-10 labels yet generalizes; resolved via marginal likelihood (p. 668). *(Not an established id; proposal.)* — from [[murphy-2023-pml2/ch17-bayesian]]
- [[marglik-local-minima-1d]] — two local optima in the marginal likelihood — from [[murphy-2023-pml2/ch18-gaussian-p2]]
- [[fashion-mnist-vs-mnist-ood-likelihood]] — pixel-CNN and flow models trained on Fashion-MNIST give higher likelihood to MNIST — from [[murphy-2023-pml2/ch19-beyond]]
- [[noisy-mixture-vs-likelihood]] — $q_2=0.01q_0+0.99q_1$ keeps log-likelihood — from [[murphy-2023-pml2/ch20-generative]]
- [[memorizing-gmm]] — GMM on training images: good samples, poor test likelihood — from [[murphy-2023-pml2/ch20-generative]]
- [[two-delta-mixture]] — GMM on two deltas gives infinite likelihood, wrong weights — from [[murphy-2023-pml2/ch20-generative]]
- [[two-component-gmm-label-switching]] — swapped means give equal likelihood — from [[murphy-2023-pml2/ch28-latent-p1]]
- [[poisson-hmm-changepoint]] — segmentation of count data; $K$ chosen by approximate marginal likelihood — from [[murphy-2023-pml2/ch29-state-p1]]
- [[locatello-nonidentifiability]] — an entangling bijection keeps the marginal likelihood, so disentanglement is not identifiable from it alone — from [[murphy-2023-pml2/ch32-representation]]
- [[gaussian-mixture-mle-nonexistence]] — likelihood unbounded as $\sigma_1\to0$ with $\mu_1=X_1$ — from [[polyanskiy-2025-information/ch32-classical]]
- [[unlikelihood-degeneration]] — unlikelihood training produced generally meaningless outputs, which the authors believe results from unconstrained likelihood minimization of $\log p(y_l|x)$, with outputs ("when when…", Table 3) — from [[rafailov-2023-dpo/main]]
- [[michael-reunion-story]] — three-variant belief likelihood item (Methods: Belief likelihood test) — from [[strachan-2024-llm-humans/main]]
- [[cough-diagnosis]] — John's cough: likelihood favours cold and lung disease, prior favours cold and heartburn — from [[tenenbaum-2011-grow/main]]

## Candidate bridges

- [same-math] Eq. 1 with softmax and log-likelihood training ↔ LLM: next-token prediction trained by cross-entropy (the same objective with a different $g$) — from [[bengio-2003-nplm/main]] (llm → llm)
- [same-math] likelihood-ratio gradient (3.47) ↔ statistics: score-function estimator, since $E\{\nabla\log p\}=0$ is the same identity. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other:statistics)
- [same-math] ELBO maximization ↔ bayesian: the Bayesian posterior as the optimum of "expected log likelihood − KL to prior" — Eq. (13) rewrites exactly as this balance — from [[blei-2017-variational/main-p1]] (bayesian → bayesian)
- [structural-analogy] "Partial" evaluation of Winograd completions ↔ likelihood-ratio comparison between two hypotheses — the choice is made by comparing probabilities of the same data under two conditions. — from [[brown-2020-gpt3/main-p3]] (llm → unspecified)
- [structural-analogy] $x_{\min}$ choice (BIC versus KS) ↔ model selection: penalised likelihood versus distance-to-model — from [[clauset-2009-powerlaw/main-p1]] (complex-systems → other:statistics)
- [structural-analogy] Likelihood-ratio test between non-nested models ↔ model selection in agent-based/many-model work — rival generative models compared on one data set. — from [[clauset-2009-powerlaw/main-p2]] (complex-systems → unspecified)
- [structural-analogy] Rare-event exponent $D(P^*\|Q)$ ↔ cross-entropy / likelihood-ratio testing: the cost of a wrong model is measured in $D$. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → information-theory)
- [structural-analogy] A stopping rule or data-dependent model building has no Bayesian consequence ↔ Bayesian workflow: likelihood principle versus data-adaptive modelling and the need for predictive checks. — from [[efron-1986-bayesian/main]] (bayesian → bayesian)
- [structural-analogy] Heavy-tailed t as a robust replacement for the normal ↔ bayesian: scale-mixture representations of outlier-robust likelihoods. — from [[gelman-2013-bda3/appa-standard]] (bayesian → bayesian)
- [same-math] posterior odds = prior odds × likelihood ratio ↔ Bayes' theorem in HS form (e.g. medical-test base rates): the same rule on a different scale. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → bayesian)
- [structural-analogy] converting a score into a match probability via prior and likelihood (record linkage) ↔ base-rate neglect: the prior proportion of true matches matters for the posterior. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → decision-game-theory)
- [structural-analogy] Nonidentified $\rho$ with posterior = prior ↔ any parameter with a flat likelihood: data add no information, so the prior carries all inference. — from [[gelman-2013-bda3/ch04-asymptotics]] (bayesian → other:any-parameter-with-a)
- [structural-analogy] Censored likelihood term $\Phi(\theta-\phi)$ ↔ survival analysis: contributions from right-censored observations. — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → other:statistics)
- [structural-analogy] Boundary-avoiding priors for a mode ↔ penalized likelihood — the author notes that the log prior acts as a penalty (p. 311). — from [[gelman-2013-bda3/ch13-modal]] (bayesian → unspecified)
- [same-math] Gibbs step for $z_{i}$ (22.5, p. 527; p. 534 step 1) ↔ Bayes' theorem: posterior component probability ∝ prior weight × component likelihood. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → bayesian)
- [metaphor] Choosing $a=n_0/H$ so that unneeded components empty out ↔ Bayesian Occam's razor: complexity is penalised through the marginal likelihood rather than a selection rule. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → bayesian)
- [structural-analogy] Marginal-likelihood penalty on extra clusters ↔ Bayesian Occam's razor: more parameters spread mass thinner. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → bayesian)
- [structural-analogy] posterior under misspecification concentrating where d(θ) is smallest ↔ maximum-likelihood/quasi-likelihood under a wrong model (White, p. 11, fn. 8): both target the best-fitting member of a wrong family — from [[gelman-2013-philosophy/main]] (bayesian → other:maximum-likelihood-quasi-likelihood)
- [structural-analogy] Weights $\alpha_i$ on likelihood terms ↔ influence functions in robust statistics: differentiating with respect to data weights measures influence (p. 34). — from [[gelman-2020-workflow/main-p2]] (bayesian → other:statistics)
- [metaphor] "Approximate aliasing" in the likelihood (Fig. 33 caption, p. 59) ↔ signal processing: periodic sampling makes distinct frequencies look alike. — from [[gelman-2020-workflow/main-p3]] (bayesian → other:signal-processing)
- [structural-analogy] TIRM's treatment projection ↔ causal inference: propensity score — a low-dimensional score for treatment likelihood used for matching — from [[grimmer-2022-textasdata/ch27-text]] (political-science → bayesian)
- [metaphor] The g-null paradox (each model component is fine but together they cannot all be correct) ↔ Bayesian workflow: priors/likelihood that are individually reasonable but jointly incoherent. — from [[hernan-2020-whatif/ch21-g]] (bayesian → bayesian)
- [structural-analogy] $\partial^2\ln Z/\partial\lambda^2$ as variance ↔ Fisher information: curvature of log-likelihood — the same second-derivative-of-log-normalizer structure (relation not stated in the paper). — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [structural-analogy] Sampling distribution vs. inverse problem ↔ bayesian: likelihood vs. posterior — $P(D|H)$ as a function of $D$ versus $P(H|D)$ needing a prior. — from [[jaynes-2003-probability/ch03-elementary]] (bayesian → bayesian)
- [same-math] Evidence in db (log-likelihood ratio) ↔ information-theory: difference of surprisals $-\log P(D|\overline H)+\log P(D|H)$ (change of base and factor 10) — the same quantity. — from [[jaynes-2003-probability/ch04-elementary]] (bayesian → information-theory)
- [structural-analogy] $\sigma^{-2}=-L''(\hat f)$ in (4.70)–(4.71) ↔ Fisher information: curvature of log-likelihood sets the posterior width ($1/\sqrt N$ shrinkage), here with a flat prior. — from [[jaynes-2003-probability/ch04-elementary]] (bayesian → information-theory)
- [same-math] $H(f,p)$, entropy of $(f,1-f)$ relative to $(p,1-p)$ ↔ information-theory: negative KL divergence $-D(f\|p)$; likelihood ratio $=e^{-nD}$. — from [[jaynes-2003-probability/ch05-queer]] (bayesian → information-theory)
- [same-math] $P(N|X)=P(N|TX)P(T|X)+P(N|\bar TX)P(\bar T|X)$ (5.36) ↔ bayesian: marginal likelihood (evidence) as a prior-weighted average over hypotheses. — from [[jaynes-2003-probability/ch05-queer]] (bayesian → bayesian)
- [same-math] Evidence in db, $10\log_{10}$ odds ↔ information-theory: log-likelihood ratio in bits (change of log base). — from [[jaynes-2003-probability/ch05-queer]] (bayesian → information-theory)
- [structural-analogy] Polarisation from different trust in a source ↔ bayesian: different priors and likelihood models on the same data. — from [[jaynes-2003-probability/ch05-queer]] (bayesian → bayesian)
- [same-math] Uniform prior + binomial likelihood → posterior $\propto\theta^r(1-\theta)^{n-r}$ (6.71) ↔ bayesian: Beta–Binomial conjugate updating — same posterior form; the text does not use the Beta name. — from [[jaynes-2003-probability/ch06-elementary-p1]] (bayesian → bayesian)
- [structural-analogy] B's posterior as a product of two routes' distributions (6.136) ↔ information-theory: combining independent evidence by adding log-likelihoods (bits) — from [[jaynes-2003-probability/ch06-elementary-p2]] (bayesian → information-theory)
- [metaphor] $H_S$ with likelihood 1 ↔ information-theory: a model that memorizes the data (overfitting) and is penalised by description length (MDL) — from [[jaynes-2003-probability/ch06-elementary-p2]] (bayesian → information-theory)
- [structural-analogy] Posterior becoming Gaussian with width about $1/\sqrt c$ ↔ information-theory: Fisher information as local curvature of log-likelihood — from [[jaynes-2003-probability/ch06-elementary-p2]] (bayesian → information-theory)
- [structural-analogy] averaging risk over g(α) ↔ bayesian: hierarchical or marginal likelihood — a weighted average over unknowns turns an ill-posed pointwise problem into a solvable one. — from [[jaynes-2003-probability/ch13-decision]] (bayesian → bayesian)
- [same-math] Likelihood-ratio threshold test (14.34) ↔ bayesian: posterior odds = prior odds × likelihood ratio, thresholded at loss ratio — literally the same rule (14.54). — from [[jaynes-2003-probability/ch14-simple]] (bayesian → bayesian)
- [structural-analogy] Weight of evidence as sharpness of the A_p density ↔ information-theory: Fisher information as curvature of log-likelihood — narrower density means more information — from [[jaynes-2003-probability/ch18-p]] (bayesian → information-theory)
- [structural-analogy] Ockham factor / marginal likelihood ↔ information-theory: Minimum Description Length — model complexity is charged against fit, as bits for the model plus bits for the data. — from [[jaynes-2003-probability/ch20-model]] (bayesian → information-theory)
- [metaphor] Fair judge vs cruel realist ↔ bayesian: maximised (profile) likelihood versus prior-averaged evidence. — from [[jaynes-2003-probability/ch20-model]] (bayesian → bayesian)
- [same-math] Quasi-likelihood mixture over good/bad labels ↔ bayesian: marginal likelihood averaged over a latent discrete variable — the sum over labellings is a marginalisation. — from [[jaynes-2003-probability/ch21-outliers]] (bayesian → bayesian)
- [same-math] Base-rate neglect ↔ Bayes' rule: posterior odds = prior odds × likelihood ratio; the 5.44 factor is the ratio of the prior odds in the two conditions, $(7/3)\div(3/7)=(.7/.3)^2$. — from [[kahneman-2011-thinking/appa-judgment]] (decision-game-theory → bayesian)
- [same-math] Bayes's rule with prior and likelihood ratio ↔ Bayesian statistics generally: posterior odds = prior odds × likelihood ratio (our added step reproduces the author's 3% → 11% example). — from [[kahneman-2011-thinking/ch14-tom]] (decision-game-theory → bayesian)
- [same-math] Base rate plus witness reliability ↔ probability: Bayes' rule with prior 0.15 and likelihood ratio 4:1 gives 0.12/0.29. — from [[kahneman-2011-thinking/ch16-causes]] (decision-game-theory → other:probability)
- [same-math] Optimal decoding of R₃ (maximize P(s|**r**) with equal priors = maximize likelihood) ↔ bayesian: posterior ∝ likelihood × prior; it is the same equation (1.18). — from [[mackay-2003-information/ch01-introduction]] (information-theory → bayesian)
- [structural-analogy] Majority vote as likelihood ratio γ^(votes) ↔ bayesian: independent observations multiply likelihood ratios (evidence accumulation). — from [[mackay-2003-information/ch01-introduction]] (information-theory → bayesian)
- [same-math] log posterior-ratio = log likelihood-ratio + log prior-ratio, (2.51) ↔ bayesian: the logistic (sigmoid) form of Ex. 2.17 is the inverse of log-odds — same algebra. — from [[mackay-2003-information/ch02-probability]] (information-theory → bayesian)
- [same-math] "Evidence" as normalizing constant, evidence ratio ↔ bayesian: marginal likelihood and model comparison. — from [[mackay-2003-information/ch03-more]] (information-theory → bayesian)
- [same-math] Optimal block decoder argmax P(s|y) ↔ bayesian: MAP estimation with the codeword as the hypothesis and the channel as the likelihood. — from [[mackay-2003-information/ch09-communication]] (information-theory → bayesian)
- [same-math] bit-by-bit match, ratio 2^r ↔ bayesian: sequential updating with likelihood ratios — odds multiply by the likelihood ratio. — from [[mackay-2003-information/ch12-hash]] (information-theory → bayesian)
- [structural-analogy] Minimum-error decoding with unequal codeword probabilities (Ex. 15.10) ↔ Bayesian inference: prior over codewords combined with the channel likelihood — the best decoder depends on both. — from [[mackay-2003-information/ch15-further]] (information-theory → bayesian)
- … 80 more bridge lines mention this id (see wiki/kg/bridges.jsonl)
