---
id: posterior-predictive-distribution
type: concept
fields: [bayesian, information-theory]
n_sources: 37
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch03-introduction, gelman-2013-bda3/ch05-hierarchical, gelman-2013-bda3/ch06-model, gelman-2013-bda3/ch09-decision, gelman-2013-bda3/ch10-introduction, gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch15-hierarchical, gelman-2013-bda3/ch18-models, gelman-2013-bda3/ch22-finite, jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch16-orthodox, jaynes-2003-probability/ch18-p, mackay-2003-information/ch02-probability, mackay-2003-information/ch03-more, mackay-2003-information/ch06-stream, mackay-2003-information/ch28-model, mackay-2003-information/ch41-learning, mackay-2003-information/ch44-supervised, mackay-2003-information/ch45-gaussian, mcelreath-2020-rethinking/ch03-sampling, mcelreath-2020-rethinking/ch04-linear-p2, mcelreath-2020-rethinking/ch06-overfitting-p2, mcelreath-2020-rethinking/ch12-multilevel, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch05-information-p2, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch14-predictive, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch17-bayesian, murphy-2023-pml2/ch18-gaussian-p1, murphy-2023-pml2/ch18-gaussian-p2, murphy-2023-pml2/ch19-beyond, murphy-2023-pml2/ch29-state-p2, murphy-2023-pml2/ch29-state-p3]
raw_ids: [Posterior predictive distribution]
canon_spine: bayesian
generated_by: build_kg.py
---

# posterior-predictive-distribution

## Canon spine entry

- **Posterior predictive distribution** (bayesian): the distribution of new data averaging over posterior uncertainty in parameters (UG)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch01-probability]] (p. 7): $p(\tilde y|y)=\int p(\tilde y|\theta)p(\theta|y)d\theta$, a posterior average of conditional predictions
- [[gelman-2013-bda3/ch02-single]] (pp. 32, 41): $p(\tilde y|y)=\int p(\tilde y|\theta)p(\theta|y)d\theta$; normal case has variance $\sigma^2+\tau_1^2$
- [[gelman-2013-bda3/ch03-introduction]] (p. 66): for normal data, a $t$ with scale $(1+1/n)^{1/2}s$; simulated by drawing parameters, then $\tilde y$
- [[gelman-2013-bda3/ch05-hierarchical]] (p. 108): two kinds: for existing $\theta_j$ or for new $\tilde\theta_j$ from the population
- [[gelman-2013-bda3/ch06-model]] (p. 145): $p(y^{\rm rep}\mid y)=\int p(y^{\rm rep}\mid\theta)p(\theta\mid y)d\theta$, eq. (6.1)
- [[gelman-2013-bda3/ch09-decision]] (pp. 238, 250): the source of decision-relevant predictions, e.g. (9.5) for radon
- [[gelman-2013-bda3/ch10-introduction]] (p. 264): draw one $\tilde y$ from $p(\tilde y|\theta^s)$ for each posterior draw $\theta^s$
- [[gelman-2013-bda3/ch14-introduction]] (p. 357): ỹ distribution averaging over posterior of (β,σ); adds parameter uncertainty to σ²
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 387): forecasting requires simulating new varying coefficients from their population distribution
- [[gelman-2013-bda3/ch18-models]] (p. 449): $y_{\rm mis}$ is drawn from its posterior predictive given $y_{\rm obs}$
- [[gelman-2013-bda3/ch22-finite]] (p. 531): predictions for existing persons use $\alpha_j$; for new persons first draw $\tilde\alpha_j$
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 65): outcome distributions at each $p$, averaged over the posterior
- [[mcelreath-2020-rethinking/ch04-linear-p2]] (pp. 108–109): simulated heights that combine posterior uncertainty with Gaussian sampling variation
- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (p. 203): the ensemble is a weighted mix across models
- [[mcelreath-2020-rethinking/ch12-multilevel]] (pp. 376–381): retrodiction versus predictions for new clusters by simulating intercepts
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 68): ∫p(y|θ)p(θ|D)dθ
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 96): integrates out parameters; Student-$t$ for the NIW model
- [[murphy-2023-pml2/ch05-information-p2]] (p. 258): $\xi(\boldsymbol x_{1:t})$ and $\xi(x_t|\boldsymbol x_{<t})$ in the Solomonoff mixture
- [[murphy-2023-pml2/ch07-inference]] (pp. 346, 356): $g(\theta)=p(y_{N+1}|\theta)$ averaged over the posterior
- [[murphy-2023-pml2/ch14-predictive]] (pp. 578, 582): $p(y|x)=\int p_\theta(y|x)p(\theta|\mathcal D)d\theta$; evaluated jointly over $\tau$ outcomes
- [[murphy-2023-pml2/ch15-generalized]] (pp. 599, 615): Student for NIG linear regression; MC or probit-moderated for logistic
- [[murphy-2023-pml2/ch17-bayesian]] (pp. 647, 661): $\int p(y|x,\theta)p(\theta|\mathcal D)d\theta$, approximated by MC averaging (17.25)
- [[murphy-2023-pml2/ch18-gaussian-p1]] (p. 695): GP predictive $\mathcal N(\mu_{*|X},\Sigma_{*|X})$ at test inputs
- [[murphy-2023-pml2/ch18-gaussian-p2]] (p. 720): GP predictions, optionally averaged over kernel-parameter posterior (18.166)
- [[murphy-2023-pml2/ch19-beyond]] (p. 755): per-task predictive integrates over task-parameter posterior
- [[murphy-2023-pml2/ch29-state-p2]] (p. 1004): UPM predictive of $\mathbf y_t$ given the segment
- [[murphy-2023-pml2/ch29-state-p3]] (p. 1027): forecasts $p(\mathbf y_{t+h}|\mathbf y_{1:t})$

### information-theory

- [[jaynes-2003-probability/ch06-elementary-p1]] (pp. 154–155, 165): probability that the next draw is red (6.29, 6.73)
- [[jaynes-2003-probability/ch16-orthodox]] (p. 498): (16.4), the density of a new observation given the data
- [[jaynes-2003-probability/ch18-p]] (p. 563): P(M_m|N_n), eq. (18.24), the A_p density averaged over future trials
- [[mackay-2003-information/ch02-probability]] (p. 29): prediction by averaging over the posterior of the unknown
- [[mackay-2003-information/ch03-more]] (pp. 51–52): predictions that integrate or sum over uncertainty about parameters and models
- [[mackay-2003-information/ch06-stream]] (p. 117): the next-symbol distribution used by the coder is the Bayesian predictive distribution given the string so far
- [[mackay-2003-information/ch28-model]] (p. 347): ideal predictions sum over all models weighted by their probabilities
- [[mackay-2003-information/ch41-learning]] (p. 495): average of predictions over the posterior, eq. 41.14
- [[mackay-2003-information/ch44-supervised]] (p. 531): marginalization over parameters gives predictions and error bars [as `Posterior predictive distribution`]
- [[mackay-2003-information/ch45-gaussian]] (pp. 537, 543): (45.7); for a GP, Gaussian with mean (45.42) and variance (45.43)

## Candidate bridges

- [same-math] Simulating heights from each posterior sample's (μ, σ) ↔ bayesian: posterior predictive distribution; the procedure is the same Monte Carlo averaging over parameters — from [[mcelreath-2020-rethinking/ch04-linear-p2]] (bayesian → bayesian)
- [structural-analogy] Aleatoric vs epistemic split in BALD (34.99) ↔ posterior predictive distribution: predictive entropy minus expected entropy given parameters. — from [[murphy-2023-pml2/ch34-decision]] (bayesian → other)
- [structural-analogy] Eq. 9.5 as a sum over $m$ weighted by $P(M{=}m\mid X)$ ↔ Posterior predictive distribution: averaging over a distribution of an intermediate quantity — from [[pearl-2018-bookofwhy/ch09-mediation-p2]] (bayesian → other)
