---
id: posterior-distribution
type: concept
fields: [information-theory, bayesian, control-theory]
n_sources: 64
tiers: [core, reference, deep]
grounding: digests
sources: [bayes-1763-essay/main, blei-2017-variational/main-p2, gelman-2013-bda3/appb-outline, gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch03-introduction, gelman-2013-bda3/ch04-asymptotics, gelman-2013-bda3/ch21-gaussian, gelman-2013-philosophy/main, griffiths-2006-optimal/main, jaynes-2003-probability/ch04-elementary, jaynes-2003-probability/ch05-queer, jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch07-central-p1, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch16-orthodox, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, jaynes-2003-probability/ch18-p, jaynes-2003-probability/ch19-physical, jaynes-2003-probability/ch21-outliers, mackay-2003-information/ch01-introduction, mackay-2003-information/ch02-probability, mackay-2003-information/ch03-more, mackay-2003-information/ch09-communication, mackay-2003-information/ch11-error, mackay-2003-information/ch13-binary, mackay-2003-information/ch21-exact, mackay-2003-information/ch24-exact, mackay-2003-information/ch25-exact, mackay-2003-information/ch28-model, mackay-2003-information/ch33-variational, mackay-2003-information/ch36-decision, mackay-2003-information/ch37-bayesian, mackay-2003-information/ch39-single, mackay-2003-information/ch41-learning, mackay-2003-information/ch44-supervised, mackay-2003-information/ch45-gaussian, mackay-2003-information/ch46-deconvolution, mackay-2003-information/ch47-low, mackay-2003-information/ch48-convolutional, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch03-sampling, mcelreath-2020-rethinking/ch04-linear-p1, mcelreath-2020-rethinking/ch04-linear-p2, mcelreath-2020-rethinking/ch05-multivariate-p2, mcelreath-2020-rethinking/ch07-interactions, mcgrayne-2011-theory/ch01-causes, mcgrayne-2011-theory/ch02-man, mcgrayne-2011-theory/ch04-bayes, mcgrayne-2011-theory/ch08-jerome, mcgrayne-2011-theory/ch15-navy, murphy-2023-pml2/ch02-probability-p1, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch09-message, murphy-2023-pml2/ch10-variational-p1, murphy-2023-pml2/ch28-latent-p1, murphy-2023-pml2/ch34-decision, pearl-2018-bookofwhy/ch03-evidence, sarkka-2023-bayesianfiltering/ch02-bayesian, tenenbaum-2011-grow/main]
raw_ids: [Posterior distribution]
canon_spine: bayesian
generated_by: build_kg.py
---

# posterior-distribution

## Canon spine entry

- **Posterior distribution** (bayesian): updated beliefs about unknowns after conditioning on data; the full answer in Bayesian inference (UG)

## Definitions in the sources

### information-theory

- [[jaynes-2003-probability/ch04-elementary]] (pp. 89, 109): $P(H|DX)$, or the pdf $g(f|DX)$ for a continuous parameter
- [[jaynes-2003-probability/ch05-queer]] (pp. 122–123): result of (5.12)–(5.13); depends on the full hypothesis set
- [[jaynes-2003-probability/ch06-elementary-p1]] (pp. 149, 150, 165): joint/marginal posteriors for $N$, $R$, $\theta$; from one posterior come point and interval estimates
- [[jaynes-2003-probability/ch06-elementary-p2]] (pp. 180–187): the full answer; summarized by mode, mean and s.d.
- [[jaynes-2003-probability/ch07-central-p1]] (p. 212): posterior mean minimises expected squared error, median expected absolute error
- [[jaynes-2003-probability/ch13-decision]] (p. 415): expectation of the loss is always taken over it
- [[jaynes-2003-probability/ch16-orthodox]] (p. 501): $p(\theta|DI)$; its width answers Q2
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 514, fn. 3): gives the optimal estimator under quadratic loss as its mean
- [[jaynes-2003-probability/ch17-principles-p2]] (p. 533): here its width reflects data range, unlike the orthodox sampling-based accuracy claim
- [[jaynes-2003-probability/ch18-p]] (pp. 563, 572): (A_p|N_n), e.g. (18.22), (18.47)
- [[jaynes-2003-probability/ch19-physical]] (p. 594, 597): here Gaussian, with mean $\hat x$ and covariance $K^{-1}$
- [[jaynes-2003-probability/ch21-outliers]] (p. 622): marginal posterior for θ computed by (21.15)
- [[mackay-2003-information/ch01-introduction]] (p. 6): P(s | **r**), maximized by the optimal decoder
- [[mackay-2003-information/ch02-probability]] (p. 29): conditional probability of the unknown given the data
- [[mackay-2003-information/ch03-more]] (p. 50): what you know after the data; the author calls it the unique and complete solution
- [[mackay-2003-information/ch09-communication]] (p. 152): P(x|y); the optimal decoder maximizes it
- [[mackay-2003-information/ch11-error]] (p. 181): for Gaussian prior and likelihood, a Gaussian with the sum of the precisions
- [[mackay-2003-information/ch13-binary]] (p. 225): optimal decoders maximize the posterior over codewords or bits
- [[mackay-2003-information/ch21-exact]] (p. 294): P(b,e | a=1) over four hypotheses
- [[mackay-2003-information/ch24-exact]] (p. 321): joint posterior (24.8) and its conditionals and marginals
- [[mackay-2003-information/ch25-exact]] (p. 324): probabilities over codewords given $\mathbf y$
- [[mackay-2003-information/ch28-model]] (p. 347): as in (28.4)
- [[mackay-2003-information/ch33-variational]] (p. 427): P(w|D,H), the target Q approximates
- [[mackay-2003-information/ch36-decision]] (p. 452): $P(x_n\mid d_n)$ with precision-weighted mean
- [[mackay-2003-information/ch37-bayesian]] (p. 461): gives P(pA+<pB+|Data) by integration over a region
- [[mackay-2003-information/ch39-single]] (pp. 472, 480): $P(s=1|\mathbf y)$ has the logistic form of a neuron [as `Posterior distribution`]
- [[mackay-2003-information/ch41-learning]] (p. 493): $P(\mathbf w\mid D,\alpha)=\exp(-M)/Z_M$
- [[mackay-2003-information/ch44-supervised]] (p. 529): $\exp(-M)/Z_M$ [as `Posterior distribution`]
- [[mackay-2003-information/ch45-gaussian]] (pp. 535, 537): (45.1) over functions, (45.5) over parameters
- [[mackay-2003-information/ch46-deconvolution]] (p. 549–550): Gaussian here
- [[mackay-2003-information/ch47-low]] (pp. 559, 561): marginals $P(x_n=1\mid\mathbf z,\mathbf H)$, approximated by the pseudoposterior $q_n$
- [[mackay-2003-information/ch48-convolutional]] (p. 578): per-bit posterior from the sum–product (BCJR) algorithm

### bayesian

- [[bayes-1763-essay/main]] (p. 22): the area ratio of Prop. 9, giving the chance that the probability lies in a range
- [[blei-2017-variational/main-p2]] (pp. 27, 31): the target of approximation; closed form unavailable in ARD, GMM, LDA
- [[gelman-2013-bda3/appb-outline]] (p. 587): the object whose large-sample limit is studied
- [[gelman-2013-bda3/ch01-probability]] (pp. 3, 7): conditional distribution of unobserved quantities given observed data
- [[gelman-2013-bda3/ch02-single]] (pp. 32–33): all current information about the parameter; compromise between prior and data
- [[gelman-2013-bda3/ch03-introduction]] (p. 63): here the joint posterior of all unknowns, then marginalized to the parameters of interest
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 92): here used as the full inferential summary, preferred over a single point estimate
- [[gelman-2013-bda3/ch21-gaussian]] (p. 503): with Gaussian noise the conditional posterior of $\mu$ is again a GP
- [[gelman-2013-philosophy/main]] (pp. 2, 5): p(θ|y); on the usual story it is all of inference, for the authors it is only the output of the fitting step
- [[griffiths-2006-optimal/main]] (pp. 768, 773): $p(t_{total}\mid t)$, whose form is fixed by the prior
- [[mcelreath-2020-rethinking/ch02-small]] (p. 36): plausibility of parameter values conditional on the data, $\Pr(p\mid n,w)$
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 58): the whole estimate, a function mapping each parameter value to a plausibility
- [[mcelreath-2020-rethinking/ch04-linear-p1]] (p. 79): over $(\mu,\sigma)$ pairs; the "estimate" is the whole distribution, "a distribution of Gaussian distributions"
- [[mcelreath-2020-rethinking/ch04-linear-p2]] (pp. 92, 98): ranks all (α, β, σ) combinations by relative plausibility; the author reads it as relative compatibility of states of the world with data, given the model
- [[mcelreath-2020-rethinking/ch05-multivariate-p2]] (p. 143): here read as an honest answer to the question the model asks, even when wide
- [[mcelreath-2020-rethinking/ch07-interactions]] (p. 221): anything computed from parameters, such as a slope or a difference, has its own posterior, obtained by transforming samples
- [[mcgrayne-2011-theory/ch01-causes]] (p. 8): the probability of the newly revised belief
- [[mcgrayne-2011-theory/ch02-man]] (p. 20): $P(C|E)$, the updated probability of a cause given the data
- [[mcgrayne-2011-theory/ch04-bayes]] (p. 77): updated belief; information content is low if it is basically the same as the prior
- [[mcgrayne-2011-theory/ch08-jerome]] (p. 115): in Framingham, a logistic regression function giving risk
- [[mcgrayne-2011-theory/ch15-navy]] (p. 201): probabilities updated by daily search results: searched cells go down, unsearched go up
- [[murphy-2023-pml2/ch02-probability-p1]] (p. 8): $p(X=k|E)$, state probabilities after conditioning on $E$
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 63): p(θ|D), the full Bayesian answer
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 84): obtained by adding data statistics to prior parameters in conjugate models
- [[murphy-2023-pml2/ch07-inference]] (p. 345): target of inference; used via expectations $\mathbb E[g(\theta)|\mathcal D]$
- [[murphy-2023-pml2/ch09-message]] (p. 403): here marginals/pairwise marginals $p(z_t|\mathbf y)$, $\xi_{t,t+1}$
- [[murphy-2023-pml2/ch10-variational-p1]] (p. 439): target $p_\theta(z|x)$, assumed unnormalizable
- [[murphy-2023-pml2/ch28-latent-p1]] (p. 931, p. 941): used for responsibilities, $p(z|x)$ in FA, and posterior samples in imaging
- [[murphy-2023-pml2/ch34-decision]] (p. 1106): the object over which decision risk is averaged in the Bayesian approach
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 104): updated probability after evidence, e.g., 1/116
- [[tenenbaum-2011-grow/main]] (p. 1280): $P(h\mid d)$, beliefs updated on the observed data

### control-theory

- [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 19): $p(\theta\mid y)\propto p(y\mid\theta)p(\theta)$ [new]

## Candidate bridges

- [same-math] Sum–product (forward–backward) on a trellis ↔ bayesian: posterior distribution of each hidden variable given observations — the bit posterior given channel likelihoods. — from [[mackay-2003-information/ch48-convolutional]] (information-theory → bayesian)
