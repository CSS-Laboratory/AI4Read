---
id: marginal-likelihood
type: concept
fields: [bayesian, information-theory, control-theory, linear-algebra]
n_sources: 28
tiers: [reference, core, deep]
grounding: digests
sources: [bayes-1763-essay/main, deisenroth-2020-mml/ch09-linear, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch05-hierarchical, gelman-2013-bda3/ch20-basis, gelman-2013-bda3/ch23-dirichlet, jaynes-2003-probability/ch20-model, mackay-2003-information/ch21-exact, mackay-2003-information/ch24-exact, mackay-2003-information/ch37-bayesian, mackay-2003-information/ch45-gaussian, mackay-2003-information/ch46-deconvolution, mcelreath-2020-rethinking/ch02-small, murphy-2023-pml2/ch02-probability-p1, murphy-2023-pml2/ch02-probability-p2, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch03-statistics-p3, murphy-2023-pml2/ch05-information-p1, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch08-gaussian-p1, murphy-2023-pml2/ch09-message, murphy-2023-pml2/ch11-monte, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch17-bayesian, murphy-2023-pml2/ch18-gaussian-p1, murphy-2023-pml2/ch19-beyond, sarkka-2023-bayesianfiltering/ch16-parameter]
generated_by: build_kg.py
---

# marginal-likelihood

## Definitions in the sources

### bayesian

- [[bayes-1763-essay/main]] (pp. 21–22): $AiB/CA$, the probability of the observed counts before $W$ is thrown
- [[gelman-2013-bda3/ch02-single]] (p. 44): computed as $p(y)=p(y|\theta)p(\theta)/p(\theta|y)$ under conjugacy
- [[gelman-2013-bda3/ch05-hierarchical]] (p. 116): $p(y|\mu,\tau)$ with $\theta$ integrated out, e.g. $\bar y_{.j}\sim\text{N}(\mu,\sigma_j^2+\tau^2)$
- [[gelman-2013-bda3/ch20-basis]] (p. 491): p(y|X,γ), analytic for each basis subset; drives posterior model probabilities (20.4)
- [[gelman-2013-bda3/ch23-dirichlet]] (pp. 551, 553): controls new-cluster probability and acts as complexity penalty
- [[mcelreath-2020-rethinking/ch02-small]] (p. 37): $\Pr(w)=\int\Pr(w\mid p)\Pr(p)\,dp$, the likelihood averaged over the prior; standardises the posterior
- [[murphy-2023-pml2/ch02-probability-p1]] (p. 8): $p(E)$, the normalization constant in Bayes' rule
- [[murphy-2023-pml2/ch02-probability-p2]] (p. 29): $p(\mathbf y)=\mathcal N(\mathbf y|\mathbf m,\mathbf S)$, the posterior's normalizing constant
- [[murphy-2023-pml2/ch03-statistics-p1]] (pp. 69–70): p(D|M), ratio of posterior to prior normalizers in beta–Bernoulli; KT estimator for the Jeffreys prior
- [[murphy-2023-pml2/ch03-statistics-p2]] (pp. 85, 97): ratio of normalizers, e.g. $B(\mathbf N+\boldsymbol\alpha)/B(\boldsymbol\alpha)$, and $Z(\widehat{\boldsymbol\tau},\widehat\nu)h(\mathcal D)/Z(\breve{\boldsymbol\tau},\breve\nu)$
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 119): $p(\mathcal D|m)=\int p(\mathcal D|\theta,m)p(\theta|m)d\theta$, the evidence for model $m$
- [[murphy-2023-pml2/ch05-information-p1]] (p. 225): $\Pr(D)$, cancels in the ratio of hypotheses
- [[murphy-2023-pml2/ch07-inference]] (pp. 346, 353): $p(\mathcal D|M)$ as the prior expectation of the likelihood; also called the evidence
- [[murphy-2023-pml2/ch08-gaussian-p1]] (p. 362): $\log p(y_{1:T})=\sum_t\log Z_t$ from filter normalizers
- [[murphy-2023-pml2/ch09-message]] (p. 404): here $Z_t=p(y_t|y_{1:t-1})$, the filtering normaliser
- [[murphy-2023-pml2/ch11-monte]] (p. 491, 494): the constant $Z=p(y)$, estimable by SNIS or AIS
- [[murphy-2023-pml2/ch15-generalized]] (p. 606): $\mathcal N(y\mid0,C_\alpha)$, the ARD objective
- [[murphy-2023-pml2/ch17-bayesian]] (pp. 650, 668, 671): evidence $p(\mathcal D|\alpha,\beta)$; used to learn priors, choose models and explain why random labels are unlikely under a CNN
- [[murphy-2023-pml2/ch18-gaussian-p1]] (p. 697): $p(\mathcal D\mid\theta)$ with $f$ integrated out; fit plus complexity
- [[murphy-2023-pml2/ch19-beyond]] (p. 763): for log-loss, cumulative online loss equals conditional log marginal likelihood

### information-theory

- [[jaynes-2003-probability/ch20-model]] (p. 602): $p(D|MI)$, prior expectation of the likelihood; here the fundamental quantity for ranking models
- [[mackay-2003-information/ch21-exact]] (p. 298): P({x}|H), a prior-weighted sum of likelihoods over θ
- [[mackay-2003-information/ch24-exact]] (p. 322): the evidence $P(D\mid\sigma)$ obtained by integrating out μ
- [[mackay-2003-information/ch37-bayesian]] (p. 462): the probability of the data under a model, used as the evidence for model comparison
- [[mackay-2003-information/ch45-gaussian]] (pp. 539, 546): the evidence $P(\mathbf t_N\mid\mathbf X_N,\boldsymbol\theta)$; used to adapt hyperparameters
- [[mackay-2003-information/ch46-deconvolution]] (p. 550): the "evidence"; here only a normalizer

### control-theory

- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (p. 321): $p(y_{1:T}\mid\theta)$, states integrated out; computed as product of one-step predictive densities [new]

### linear-algebra

- [[deisenroth-2020-mml/ch09-linear]] (pp. 306, 312): $p(\mathcal Y\mid\mathcal X)=\mathbb E_\theta[p(\mathcal Y\mid\mathcal X,\theta)]$, here $\mathcal N(y\mid Xm_0,XS_0X^\top+\sigma^2I)$ [new]

## Instances that use it

- [[coin-fair-bayes-factor]] — $M_0$ vs $M_1$, $N=5$, marginal likelihood vs heads — from [[murphy-2023-pml2/ch03-statistics-p3]]
- [[rademacher-free-random-label-cifar]] — Zhang et al.: CNN fits random CIFAR-10 labels yet generalizes; resolved via marginal likelihood (p. 668). *(Not an established id; proposal.)* — from [[murphy-2023-pml2/ch17-bayesian]]
- [[marglik-local-minima-1d]] — two local optima in the marginal likelihood — from [[murphy-2023-pml2/ch18-gaussian-p2]]
- [[poisson-hmm-changepoint]] — segmentation of count data; $K$ chosen by approximate marginal likelihood — from [[murphy-2023-pml2/ch29-state-p1]]
- [[locatello-nonidentifiability]] — an entangling bijection keeps the marginal likelihood, so disentanglement is not identifiable from it alone — from [[murphy-2023-pml2/ch32-representation]]

## Candidate bridges

- [metaphor] Choosing $a=n_0/H$ so that unneeded components empty out ↔ Bayesian Occam's razor: complexity is penalised through the marginal likelihood rather than a selection rule. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → bayesian)
- [structural-analogy] Marginal-likelihood penalty on extra clusters ↔ Bayesian Occam's razor: more parameters spread mass thinner. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → bayesian)
- [same-math] $P(N|X)=P(N|TX)P(T|X)+P(N|\bar TX)P(\bar T|X)$ (5.36) ↔ bayesian: marginal likelihood (evidence) as a prior-weighted average over hypotheses. — from [[jaynes-2003-probability/ch05-queer]] (information-theory → bayesian)
- [structural-analogy] averaging risk over g(α) ↔ bayesian: hierarchical or marginal likelihood — a weighted average over unknowns turns an ill-posed pointwise problem into a solvable one. — from [[jaynes-2003-probability/ch13-decision]] (information-theory → bayesian)
- [structural-analogy] Ockham factor / marginal likelihood ↔ information-theory: Minimum Description Length — model complexity is charged against fit, as bits for the model plus bits for the data. — from [[jaynes-2003-probability/ch20-model]] (information-theory → information-theory)
- [same-math] Quasi-likelihood mixture over good/bad labels ↔ bayesian: marginal likelihood averaged over a latent discrete variable — the sum over labellings is a marginalisation. — from [[jaynes-2003-probability/ch21-outliers]] (information-theory → bayesian)
- [same-math] "Evidence" as normalizing constant, evidence ratio ↔ bayesian: marginal likelihood and model comparison. — from [[mackay-2003-information/ch03-more]] (information-theory → bayesian)
- [same-math] evidence as a prior-weighted grid sum (21.9) ↔ bayesian: marginal likelihood as the average of the likelihood over the prior — from [[mackay-2003-information/ch21-exact]] (information-theory → bayesian)
- [structural-analogy] $Z$ ↔ bayesian: marginal likelihood — both are sums of an unnormalized product over latent states. — from [[mackay-2003-information/ch26-exact]] (information-theory → bayesian)
- [same-math] Dirichlet-multinomial evidence (35.13) ↔ bayesian: marginal likelihood with conjugate priors — the same integral over the prior. — from [[mackay-2003-information/ch35-random]] (information-theory → bayesian)
- [same-math] Each term P(D|H0), P(D|H1) in the ratio (37.26) ↔ bayesian: marginal likelihood (evidence) — each is the data probability averaged over the prior (37.19, 37.22). — from [[mackay-2003-information/ch37-bayesian]] (information-theory → bayesian)
- [structural-analogy] counting labellings realizable by a model class (VC dimension) ↔ bayesian: how many datasets a model can fit, as in the marginal likelihood — both measure the flexibility of a model class. — from [[mackay-2003-information/ch40-capacity]] (information-theory → bayesian)
- [structural-analogy] Partition function $Z$ ↔ bayesian: marginal likelihood as normalizing constant — both are sums over all states or parameters that normalize an unnormalized weight. — from [[mackay-2003-information/ch51-appendices]] (information-theory → bayesian)
- [structural-analogy] Bayes factor ↔ marginal-likelihood model comparison — both compare how well hypotheses predict data. — from [[mcgrayne-2011-theory/ch08-jerome]] (bayesian → unspecified)
- [structural-analogy] Doubly intractable posterior over MRF parameters ↔ marginal likelihood $p(\mathcal D)$ as hard normaliser in Bayesian model comparison (p. 182). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → unspecified)
- [structural-analogy] AIS estimate of $p(\mathcal D)$ ↔ Bayesian model comparison via the marginal likelihood. — from [[murphy-2023-pml2/ch11-monte]] (bayesian → unspecified)
- [structural-analogy] Random labels getting low marginal likelihood ↔ Bayesian Occam's razor: a model spreading mass over many datasets gives each less. — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → bayesian)
- [structural-analogy] Fit-plus-complexity split of the log marginal likelihood (18.74) ↔ bayesian-occam-razor (canon link; the text does not use that name). — from [[murphy-2023-pml2/ch18-gaussian-p1]] (bayesian → unspecified)
- [structural-analogy] Marginal likelihood fit-vs-complexity (18.163) and BIC kernel search ↔ model comparison: both penalise complexity. — from [[murphy-2023-pml2/ch18-gaussian-p2]] (bayesian → other)
- [same-math] Prequential log-loss $\sum_t\log \hat p_{t|t-1}$ ↔ Marginal likelihood (evidence): chain-rule decomposition into one-step-ahead predictive terms (p. 763). — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → other)
- [structural-analogy] ARD pruning of weights ↔ Bayesian Occam's razor: marginal-likelihood-based models shrink as data shrink (p. 949) — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → bayesian)
- [structural-analogy] $K$ selection by marginal likelihood ↔ Bayesian Occam's razor: more states fit no better, so evidence falls (p. 986). — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → bayesian)
- [same-math] Law of total probability (1.9) ↔ marginal likelihood: averaging a conditional probability over a distribution of the conditioning variable. — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → other)
- [structural-analogy] Automatic introduction of new classes only when data demand it (CRP/Occam's razor) ↔ bayesian: Bayesian Occam's razor via marginal likelihood — complexity is penalized without a hand-set cost. — from [[tenenbaum-2011-grow/main]] (bayesian → bayesian)
