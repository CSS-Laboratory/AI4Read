---
id: sarkka-2023-bayesianfiltering/ch02-bayesian
work: sarkka-2023-bayesianfiltering
unit: "2 Bayesian Inference"
pages: 17-26
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Bayesian Inference

## L0 — One line
Treat unknown parameters as random variables, compute their posterior with Bayes' rule, pick a point estimate by minimising expected loss, and use numerical methods when the integrals cannot be solved.

## L1 — The gist (≤ 120 words)
The chapter asks how to estimate unknown parameters while keeping track of uncertainty. Maximum likelihood maximises the likelihood of an unknown parameter; Bayesian inference starts by treating the parameter as a random variable. A prior (belief before the data) and a measurement model (how the data depend on the parameter) give a posterior (belief after the data) through Bayes' rule. A loss function (a cost for wrong estimates) then turns the posterior into a point estimate: for the common losses, the mean, median or mode. The needed integrals are rarely analytic. The chapter therefore sketches Gaussian approximation, quadrature, Monte Carlo, Markov chain Monte Carlo (MCMC) and importance sampling. The chapter says these methods also apply in higher-dimensional problems.

**Prerequisites:** probability densities, conditional probability and independence, expectation as an integral, Dirac delta, gradients and Hessians (for the exercises).

## L2 — Key ideas (5–10 bullets)
- In Bayesian inference, probability means certainty about an event in a single trial, not a long-run proportion. The ordinary rules of probability then apply (p. 17).
- The ML estimate maximises the likelihood $L(\theta)$. The Bayesian posterior adds a prior (p. 18).
- The ML estimate can be seen as a MAP estimate under a uniform prior (p. 18).
- A Bayesian model has a prior, a measurement model, a posterior and a predictive posterior (the distribution of a new, not yet observed measurement) (pp. 19–20).
- A point estimate is a statistical decision. The natural choice is the action that minimises the posterior expected loss (pp. 20–21).
- Quadratic loss gives the posterior mean, absolute loss gives the median, and 0–1 loss gives the mode, the maximum a posteriori (MAP) estimate (pp. 21–22).
- Exact integrals are rare. A Gaussian approximation replaces the posterior by a Gaussian, quadrature forms its sample points deterministically, and Monte Carlo and MCMC use random samples (pp. 22–23).
- Importance sampling draws samples from an approximate importance distribution and gives each a weight. The weights correct for the difference from the target (p. 24).

## L3 — Walkthrough

### 2.1 Philosophy (p. 17)
Bayesian inference models uncertain systems and makes decisions by rational principles, using probability distributions and probability calculus (p. 17). The frequentist reading of probability is a proportion in infinitely many trials. The Bayesian reading is certainty of an event in a single trial (p. 17).

### 2.2 Connection to maximum likelihood (pp. 17–18)
Setting: measurements $\mathbf y_{1:T}$ are conditionally independent given an unknown $\boldsymbol\theta\in\mathbb R^d$, and $p(\mathbf y_k\mid\boldsymbol\theta)$ is known (p. 17).
$$L(\boldsymbol\theta)=\prod_{k=1}^T p(\mathbf y_k\mid\boldsymbol\theta)\tag{2.1}$$
$$\hat{\boldsymbol\theta}=\arg\max_{\boldsymbol\theta} L(\boldsymbol\theta)\tag{2.2}$$
Bayesian inference treats $\boldsymbol\theta$ as a random variable (p. 18).
$$p(\boldsymbol\theta\mid\mathbf y_{1:T})=\frac{p(\mathbf y_{1:T}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)}{p(\mathbf y_{1:T})}\tag{2.3}$$
Here $p(\boldsymbol\theta)$ is the prior, and $p(\mathbf y_{1:T})$ is a normaliser that does not depend on $\boldsymbol\theta$. With conditional independence:
$$p(\boldsymbol\theta\mid\mathbf y_{1:T})\propto p(\boldsymbol\theta)\prod_{k=1}^T p(\mathbf y_k\mid\boldsymbol\theta)\tag{2.4}$$
- The MAP estimate is the maximum of the posterior. The posterior mean is the MMSE estimate, which is optimal in the mean-squared sense (p. 18).
- Many other point estimates exist. The best one depends on the assumed loss (p. 18).
- The ML estimate can be seen as a MAP estimate with uniform prior $p(\boldsymbol\theta)\propto1$ (p. 18).
- Bayes can also be read as a way to add regularisation to ML; the basic ML framework has no self-consistent way to include regularisation or prior information (p. 18). The authors call this reading "quite limited" (p. 18).

*Intuition note:* Maximum likelihood looks only at how well each $\theta$ explains the data. The Bayesian posterior also weighs how plausible $\theta$ was before the data. With a flat prior the two agree on the peak.

### 2.3 Building blocks (pp. 19–20)
- **Prior model:** $p(\boldsymbol\theta)$ is the information about $\boldsymbol\theta$ before any observation (2.5). A non-informative prior expresses lack of prior information (p. 19).
- **Measurement model:** $p(\mathbf y\mid\boldsymbol\theta)$ is the distribution of $\mathbf y$ given $\boldsymbol\theta$ (2.6). It models a causal but noisy link (p. 19).
- **Posterior:**
$$p(\boldsymbol\theta\mid\mathbf y)=\frac{p(\mathbf y\mid\boldsymbol\theta)p(\boldsymbol\theta)}{p(\mathbf y)}\propto p(\mathbf y\mid\boldsymbol\theta)p(\boldsymbol\theta)\tag{2.7}$$
$$p(\mathbf y)=\int p(\mathbf y\mid\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta\tag{2.8}$$
For conditionally independent measurements the posterior is (2.9), the same as (2.4). The normaliser comes from integrating the right-hand side over $\boldsymbol\theta$, or from summing if $\boldsymbol\theta$ is discrete (p. 20).
- **Predictive posterior:** the distribution of the not-yet-observed $\mathbf y_{T+1}$ (p. 20):
$$p(\mathbf y_{T+1}\mid\mathbf y_{1:T})=\int p(\mathbf y_{T+1}\mid\boldsymbol\theta)\,p(\boldsymbol\theta\mid\mathbf y_{1:T})\,d\boldsymbol\theta\tag{2.10}$$
- **Tracking example:** the parameter can be a target's state sequence (position, velocity), measured by noisy radar distance and direction. The book splits parameters into dynamic states and static parameters, but both are unknown random parameters in the Bayesian view (p. 20).

### 2.4 Bayesian point estimates (pp. 20–22)
Choosing a point is a statistical decision, so it is formulated with decision theory (p. 20).

**Definition 2.1 (loss function).** A loss $C(\boldsymbol\theta,\mathbf a)$ is a scalar giving the loss of taking action $\mathbf a$ when the true value is $\boldsymbol\theta$. The action (or control) is the decision made from the available information (p. 21). A utility is $U=-C$ (sign not visible in text layer; see Reading notes) (p. 21).

If knowledge of $\boldsymbol\theta$ is the posterior, the natural action minimises the expected loss, or maximises the expected utility (p. 21):
$$\mathrm E[C(\boldsymbol\theta,\mathbf a)\mid\mathbf y_{1:T}]=\int C(\boldsymbol\theta,\mathbf a)\,p(\boldsymbol\theta\mid\mathbf y_{1:T})\,d\boldsymbol\theta\tag{2.11}$$

| Loss | Formula | Optimal action |
|---|---|---|
| Quadratic | $C=(\boldsymbol\theta-\mathbf a)^{\mathsf T}(\boldsymbol\theta-\mathbf a)$ (2.12) | posterior mean $\mathbf a_o=\int\boldsymbol\theta\,p(\boldsymbol\theta\mid\mathbf y_{1:T})d\boldsymbol\theta$ (2.13), the MMSE estimate |
| Absolute | $C=\sum_i\lvert\theta_i-a_i\rvert$ (2.14) | median (marginal medians in several dimensions) |
| 0–1 | $C=-\delta(\mathbf a-\boldsymbol\theta)$ (2.15) | mode of the posterior, the MAP estimate |

(Table: pp. 21–22.) Discrete case: $C=0$ if $\boldsymbol\theta=\mathbf a$, and $C=1$ if $\boldsymbol\theta\ne\mathbf a$ (2.16) (p. 22). The quadratic loss is the most common for regression. It is easy to handle mathematically. For a Gaussian posterior, the MAP estimate and the median coincide with the posterior mean (p. 21).

*Intuition note:* The loss says what kind of mistake hurts. Squared loss punishes big misses heavily, so the mean wins. Absolute loss punishes all misses in proportion, so the median wins. The 0–1 loss rewards only an exact hit, so the mode wins.

### 2.5 Numerical methods (pp. 22–24)
Analytic computation of the integrals is rare, so numerical methods are needed (p. 22).
- **Gaussian approximation:** $p(\boldsymbol\theta\mid\mathbf y_{1:T})\simeq\mathrm N(\boldsymbol\theta\mid\mathbf m,\mathbf P)$ (2.17). Match the first two moments, or take $\mathbf m$ as the mode and get $\mathbf P$ from the curvature at the mode. The authors note that the approximation is only assumed, will not be exact in most practical situations, and that its error cannot be controlled in any practical way (p. 22).
- **Quadrature/cubature** (moderate dimension): deterministic sample points (sigma points) $\boldsymbol\theta^{(i)}$ and weights $W_i$ set by the algorithm (pp. 22–23):
$$\mathrm E[\mathbf g(\boldsymbol\theta)\mid\mathbf y_{1:T}]\approx\sum_{i=1}^N W_i\,\mathbf g(\boldsymbol\theta^{(i)})\tag{2.18}$$
- **Direct Monte Carlo:** draw $\boldsymbol\theta^{(i)}\sim p(\boldsymbol\theta\mid\mathbf y_{1:T})$, $i=1,\dots,N$ (2.19). Then:
$$\mathrm E[\mathbf g(\boldsymbol\theta)\mid\mathbf y_{1:T}]\approx\frac1N\sum_i\mathbf g(\boldsymbol\theta^{(i)})\tag{2.20}$$
$$p(\boldsymbol\theta\mid\mathbf y_{1:T})\approx\frac1N\sum_{i=1}^N\delta(\boldsymbol\theta-\boldsymbol\theta^{(i)})\tag{2.21}$$
The central limit theorem guarantees convergence. At least in theory, under certain ideal conditions, the error does not depend on the dimension of $\boldsymbol\theta$. The rule of thumb is that the error should decrease as the square root of the number of samples, regardless of the dimensions (p. 23).
- **MCMC:** build a Markov chain whose stationary distribution is the target, then simulate it to get samples (p. 23).
- **Importance sampling:** weighted samples correct for the difference between the target and an importance distribution $\pi$ (p. 24):
$$\boldsymbol\theta^{(i)}\sim\pi(\boldsymbol\theta\mid\mathbf y_{1:T})\tag{2.22}$$
$$\tilde w^{(i)}=\frac1N\frac{p(\boldsymbol\theta^{(i)}\mid\mathbf y_{1:T})}{\pi(\boldsymbol\theta^{(i)}\mid\mathbf y_{1:T})}\tag{2.23}$$
$$\mathrm E[\mathbf g(\boldsymbol\theta)\mid\mathbf y_{1:T}]\approx\sum_{i=1}^N\tilde w^{(i)}\mathbf g(\boldsymbol\theta^{(i)})\tag{2.24}$$
$$\mathrm E[\mathbf g(\boldsymbol\theta)\mid\mathbf y_{1:T}]\approx\frac{\sum_i\tilde w^{(i)}\mathbf g(\boldsymbol\theta^{(i)})}{\sum_i\tilde w^{(i)}}\tag{2.25}$$

*Intuition note:* If you cannot integrate against the posterior, you replace it by a cloud of points, either chosen on purpose or drawn at random. Averaging over the cloud then replaces the integral.

## Toy example (ours, not from the text)
Let $\theta\in\{0,1,2\}$ with prior $(0.2,0.3,0.5)$. One measurement has likelihoods $p(y\mid\theta)=(0.6,0.3,0.1)$.
- Products (2.7): $0.12,\ 0.09,\ 0.05$. Sum $=0.26$ (the discrete form of 2.8).
- Posterior: $0.12/0.26=0.4615$, $0.09/0.26=0.3462$, $0.05/0.26=0.1923$.
- MAP (0–1 loss): $\theta=0$. The prior mode was $\theta=2$, but the data moved it.
- Mean (quadratic loss): $1(0.3462)+2(0.1923)=0.7308$.
- Median: the cumulative posterior is $0.4615$, then $0.8077$, so it is $\theta=1$.
- Expected absolute loss at $a=0,1,2$:
  - $a=0$: $0.3462+2(0.1923)=0.7308$.
  - $a=1$: $0.4615+0.1923=0.6538$.
  - $a=2$: $2(0.4615)+0.3462=1.2692$.

  Among these three, $a=1$ (the median) is smallest.
- A uniform prior would give posterior $\propto(0.6,0.3,0.1)$, the ML case, with mode $0$.

## Concepts
- [[bayesian-inference]] (new) — parameters are random variables; probability is certainty in a single trial (p. 17)
- [[maximum-likelihood]] (new) — maximise $L(\theta)=\prod p(y_k\mid\theta)$ (p. 18)
- [[prior-distribution]] (new) — $p(\theta)$, belief before data; may be non-informative (p. 19)
- [[measurement-model]] (new) — $p(y\mid\theta)$, noisy causal link from parameter to data (p. 19)
- [[posterior-distribution]] (new) — $p(\theta\mid y)\propto p(y\mid\theta)p(\theta)$ (p. 19)
- [[predictive-posterior]] (new) — distribution of the next measurement, from (2.10) (p. 20)
- [[loss-function]] (new) — $C(\theta,a)$; the natural choice is the action minimising posterior expected loss (p. 21)
- [[map-mmse-estimates]] (new) — MAP is the mode, MMSE the mean of the posterior (p. 18)
- [[monte-carlo-integration]] (new) — approximate expectations by sample averages (p. 23)
- [[importance-sampling]] (new) — weighted samples from an importance distribution $\pi$ (p. 24)

## Canonical instances
- [[tracking-radar-example]] — target state (position, velocity) from noisy radar distance and direction (p. 20)
- [[bayesian-linear-regression]] — Exercise 2.4 (pp. 25–26)

## Bridges (candidates)
- [structural-analogy] Loss $C(\theta,a)$ with action as "control" ↔ control theory: cost functional and control input — the source itself calls the action a control (p. 21).
- [structural-analogy] Gaussian posterior from linear model and Gaussian prior (Ex. 2.4) ↔ the measurement update of a Kalman filter — candidate only; the Kalman filter is not covered in these pages.
- [structural-analogy] Prior as regularisation ↔ penalised least squares (suggested by p. 18 and Ex. 2.4(d)).

## Questions this raises
- When does a Gaussian approximation of the posterior fail badly, since the error cannot be controlled (p. 22)?
- How does importance sampling behave when $\pi$ is a poor match for the target?
- How do these static-parameter ideas extend to a sequence of states updated over time?

## Exercises worth doing
- Ex. 2.1 (p. 24) — the median minimises expected absolute loss — medium
- Ex. 2.2 (p. 24) — optimal estimate for a weighted quadratic loss with positive definite $\mathbf R$ — medium
- Ex. 2.3 (p. 25) — least squares in matrix form — easy
- Ex. 2.4 (p. 25) — Gaussian posterior mean and covariance for Bayesian regression, compared with least squares — hard
- Ex. 2.5 (p. 26) — importance sampling check against the exact result of 2.4 — medium

## Reading notes
- Printed page = pdf − 30. Printed numbers are visible in the page labels.
- The text layer drops Greek letters, minus signs and some symbols. I restored the equations from context.
- The sign in $U=-C$ (p. 21) and in the 0–1 loss $C=-\delta(\mathbf a-\boldsymbol\theta)$ (2.15, p. 21) is lost in the text layer. The sign in (2.15) is on p. 21, not p. 22. No page images were supplied for pp. 17–22, so these equations are text-only. The minus sign in (2.15) is inferred from the stated optimal action (the mode), and the one in $U=-C$ from the statement that losses and utilities convert into each other (p. 21).
- Pages 23, 24, 25 were checked against their images.
