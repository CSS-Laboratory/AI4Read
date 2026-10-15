---
id: marginal-likelihood-evidence
type: concept
fields: [bayesian, information-theory]
n_sources: 20
tiers: [core, reference, deep]
grounding: digests
sources: [blei-2017-variational/main-p1, gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch21-gaussian, gelman-2013-philosophy/main, mackay-2003-information/ch02-probability, mackay-2003-information/ch03-more, mackay-2003-information/ch18-crosswords, mackay-2003-information/ch26-exact, mackay-2003-information/ch28-model, mackay-2003-information/ch29-monte, mackay-2003-information/ch33-variational, mackay-2003-information/ch35-random, mackay-2003-information/ch44-supervised, mcelreath-2020-rethinking/ch06-overfitting-p2, murphy-2023-pml2/ch10-variational-p1, murphy-2023-pml2/ch13-sequential, murphy-2023-pml2/ch18-gaussian-p2, murphy-2023-pml2/ch28-latent-p2, murphy-2023-pml2/ch29-state-p1, murphy-2023-pml2/ch32-representation]
raw_ids: [Marginal likelihood (evidence), marginal likelihood (evidence)]
canon_spine: bayesian
generated_by: build_kg.py
---

# marginal-likelihood-evidence

## Canon spine entry

- **Marginal likelihood (evidence)** (bayesian): probability of the data averaged over the prior; the normalizing constant and the basis of model comparison (grad)

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p1]] (pp. 5, 7): $p(\mathbf x)=\int p(\mathbf z,\mathbf x)d\mathbf z$; its intractability is why inference is hard; ELBO lower-bounds its log
- [[gelman-2013-bda3/ch07-evaluating]] (p. 182): $p(y|H)$; the authors say it is highly sensitive to arbitrary, untestable model aspects
- [[gelman-2013-bda3/ch21-gaussian]] (p. 504): (21.1), $\mu$ integrated out analytically; used for hyperparameter inference
- [[gelman-2013-philosophy/main]] (pp. 5, 16): p(y|Θ_k) enters model posteriors; the authors doubt such probabilities are a general vehicle for learning
- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (p. 192): the average likelihood behind BIC and Bayes factors
- [[murphy-2023-pml2/ch10-variational-p1]] (p. 440): $\log p_\theta(x)$, the intractable "evidence" that upper-bounds the ELBO
- [[murphy-2023-pml2/ch13-sequential]] (pp. 550, 570): SMC gives estimate $\hat Z_T$; log of it is a lower bound in variational SMC
- [[murphy-2023-pml2/ch18-gaussian-p2]] (pp. 710, 718): $p(y|X,\theta)$ with latent $f$ integrated out; used to learn kernel hyperparameters and inducing points
- [[murphy-2023-pml2/ch28-latent-p2]] (p. 967): evidence approximation for choosing the number of topics
- [[murphy-2023-pml2/ch29-state-p1]] (p. 986): probability of data given $K$, approximated here by maximising over $\lambda$
- [[murphy-2023-pml2/ch32-representation]] (p. 1069): here: a quantity that stays unchanged under the entangling bijection, so it cannot identify the disentangled model

### information-theory

- [[mackay-2003-information/ch02-probability]] (p. 29): normalizing constant $P(D\mid\mathcal H)$, in (2.27)–(2.28)
- [[mackay-2003-information/ch03-more]] (p. 53): $P(\mathbf s|F,\mathcal H)$, usually the normalizing constant of an earlier parameter inference; used to compare models
- [[mackay-2003-information/ch18-crosswords]] (p. 264): here $\log P(D|\mathcal H_i)$, the "log evidence", the negative of the data's information content under $\mathcal H_i$ [as `marginal likelihood (evidence)`]
- [[mackay-2003-information/ch26-exact]] (p. 334–335): in the book's terms, $Z$ is the normalizer of a product of likelihood and constraint factors; the chapter does not call it evidence
- [[mackay-2003-information/ch28-model]] (pp. 347–348): $P(D\mid H)=\int P(D\mid\mathbf{w},H)P(\mathbf{w}\mid H)d\mathbf{w}$; the normalizer of the parameter posterior and the score used to rank models
- [[mackay-2003-information/ch29-monte]] (p. 379): the normalizing constant Z, which MCMC does not readily give; author considers it often the most important number
- [[mackay-2003-information/ch33-variational]] (p. 429): P(D|H); F̃ is bounded below by its negative log
- [[mackay-2003-information/ch35-random]] (p. 450): probability of the data averaged over the prior; used to compare $\mathcal H_{A\to B}$ and $\mathcal H_{B\to A}$
- [[mackay-2003-information/ch44-supervised]] (p. 531): $P(\text{Data}\mid\text{control parameters})$, used to set $\alpha$ [as `Marginal likelihood (evidence)`]

## Candidate bridges

- [same-math] $P(N|X)=P(N|TX)P(T|X)+P(N|\bar TX)P(\bar T|X)$ (5.36) ↔ bayesian: marginal likelihood (evidence) as a prior-weighted average over hypotheses. — from [[jaynes-2003-probability/ch05-queer]] (information-theory → bayesian)
- [same-math] Each term P(D|H0), P(D|H1) in the ratio (37.26) ↔ bayesian: marginal likelihood (evidence) — each is the data probability averaged over the prior (37.19, 37.22). — from [[mackay-2003-information/ch37-bayesian]] (information-theory → bayesian)
- [same-math] Prequential log-loss $\sum_t\log \hat p_{t|t-1}$ ↔ Marginal likelihood (evidence): chain-rule decomposition into one-step-ahead predictive terms (p. 763). — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → other)
