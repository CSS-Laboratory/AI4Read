---
id: gelman-2013-bda3/ch10-introduction
work: gelman-2013-bda3
unit: "Chapter 10 — Introduction to Bayesian computation"
pages: 261-273
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Introduction to Bayesian computation

## L0 — One line
When the posterior cannot be handled in closed form, we approximate its integrals with random draws (rejection sampling, importance sampling) or deterministic rules. Then we check the results with fake data and simplified models.

## L1 — The gist (≤ 120 words)
The chapter asks how to compute the posterior p(θ|y) and the posterior predictive p(ỹ|y) when closed forms and simple grids fail. It surveys numerical integration, distributional approximations, direct simulation, rejection sampling and importance sampling. It argues that applied work needs few draws (often 100 independent ones), because Monte Carlo error (the error from using only finitely many draws) is small next to posterior uncertainty. It describes general software (Bugs, Stan) and debugging by crude estimates, fake-data simulation and simplified models. The practical message is to compute on the log scale, start with rough estimates, and check the computation in several ways. Chapters 11–13 supply the heavier algorithms.

**Prerequisites:** Bayes' theorem and the posterior; expectation as an integral; standard deviation of a sample mean; the normal approximation (Ch. 4); conjugate and hierarchical models (Ch. 5); the inverse-cdf method for drawing from a distribution.

## L2 — Key ideas (5–10 bullets)
- Bayesian computation means getting the posterior and the posterior predictive. We usually need only an unnormalized density q(θ|y), e.g. prior × likelihood. Work on the log scale and exponentiate late (p. 261).
- Posterior expectations are integrals. They can be estimated by an average of draws (stochastic), or by a weighted sum at chosen points (deterministic). Deterministic rules typically have lower variance but are hard to place in high dimensions (pp. 261–262).
- Start with a crude estimate that ignores part of the model or data. It gives a starting point, and a large gap from the full analysis suggests a programming or modelling error (p. 263).
- Rejection sampling needs a drawable g with a known bound p/g ≤ M. It is self-monitoring, because a poor g gives few accepted draws (pp. 264–265).
- Importance sampling reweights draws from g by w = q/g, using the ratio estimator (10.3). It is not useful when weights vary a lot, e.g. when q has wider tails than g. The effective sample size $S_{\rm eff}$ in (10.4) is a rough guide to this (pp. 265–266).
- About 100 independent draws usually suffice for summaries of a roughly normal posterior. Rare events and extreme quantiles need more draws, or semi-analytic help (pp. 267–268).
- General programs (Bugs, Stan) let users fit models without coding the inference. No program is fully general (pp. 268–270).
- Debug with fake data: simulate a "true" θ, simulate data, fit, and compare the posterior with the truth. Simplify the model step by step when results look wrong (pp. 270–271).

## L3 — Walkthrough

### Chapter opening: target distributions and log densities (p. 261)
- Bayesian computation has two steps: the posterior $p(\theta|y)$ and the posterior predictive $p(\tilde y|y)$ (p. 261).
- Earlier examples used closed forms, standard-distribution routines and grids. Complicated or high-dimensional models need more elaborate algorithms (Chapters 11–13). Combining algorithms is often most efficient (p. 261).
- The **target distribution** is the one to be simulated, $p(\theta|y)$. The book assumes (except in Section 13.10) that we can easily compute an **unnormalized density** $q(\theta|y)$, meaning $q/p$ is a constant depending only on $y$. Example: $p(\theta)p(y|\theta)$ (p. 261).
- **Log densities.** Compute with logs to avoid overflow and underflow. Exponentiate only when necessary and as late as possible. For example, the Metropolis ratio (11.1) should be the exponential of a difference of log-densities (p. 261).

### 10.1 Numerical integration (pp. 261–262)
- Numerical integration (quadrature) evaluates the integrand at finitely many points. More points give more accuracy. Methods are stochastic (Monte Carlo) or deterministic (quadrature rules) (p. 261).
- The posterior expectation is $\mathrm{E}(h(\theta)|y)=\int h(\theta)p(\theta|y)\,d\theta$. Any integral over $\theta$ can be written this way with a suitable $h$ (p. 261).
- With draws $\theta^s$ from the posterior, the integral is estimated by the sample average. Its accuracy is roughly gauged by the standard deviation of the $h(\theta^s)$ (detail in Section 10.5). If drawing is hard or the $h(\theta^s)$ are too variable, more sampling methods are needed (p. 262).
- **Simulation methods** use random samples:
$$\mathrm{E}(h(\theta)|y)=\int h(\theta)p(\theta|y)\,d\theta\approx\frac1S\sum_{s=1}^{S}h(\theta^s).\tag{10.1}$$
  - The estimate is random, but more draws improve it (p. 262).
  - Basic Monte Carlo gives independent samples (Sections 10.3–10.4). Markov chain Monte Carlo adapts better to high-dimensional complex distributions but gives dependent samples (Chapters 11–12) (p. 262).
  - MCMC has been important in making inference practical for generic hierarchical models (p. 262).
- **Deterministic methods** evaluate $h(\theta)p(\theta|y)$ at chosen points with weights:
$$\mathrm{E}(h(\theta)|y)\approx\sum_{s=1}^{S}w_s\,h(\theta^s)\,p(\theta^s|y),$$
  where $w_s$ is the volume of space represented by $\theta^s$ (p. 262).
  - Rules such as Simpson's use local polynomials. These rules typically have lower variance than simulation, but choosing locations gets difficult in high dimensions (p. 262).
  - The simplest rule is an equal-weight grid. Grids can be adaptive, starting from the posterior mode. Special quadrature rules exist for integrands with a Gaussian part, and for bounded and unbounded regions (p. 262).

*Intuition note.* An expectation is an average of $h$ over the posterior. We can estimate it with random points (simple, works in many dimensions, noisy) or with carefully placed points and weights (less noisy, but hard to place in many dimensions).

### 10.2 Distributional approximations (p. 262), and crude estimation (p. 263)
- Distributional approximations replace the posterior with a simpler parametric distribution. Integrals are then computed directly, or the approximation starts a simulation method. The normal approximation was in Chapter 4. More advanced ones are in Chapter 13 (p. 262).
- **Crude estimation by ignoring some information** (a subsection printed just before 10.3). Before elaborate methods, get a rough point estimate of the target's location with a simple non-iterative technique. This typically discards parts of the model and data (p. 263).
  - In a hierarchical model, estimate the hyperparameters $\phi$ crudely, then use the conditional posterior of $\gamma|\phi,y$. The rat tumor example (Section 5.1) did this with crude $(\alpha,\beta)$ (p. 263).
  - In the eight-schools analysis (Section 5.5), school effects $\theta_j$ are crudely estimated by the $y_j$. The between-school sd $\tau$ is estimated by the sd of the eight $y_j$, or by estimate (5.22) restricted to be nonnegative (p. 263).
  - With missing data, start by simplistically imputing the missing values. Ultimately they belong in the model (Chapter 18) (p. 263).
  - Crude inferences also serve as a comparison. If they differ greatly from the full analysis, the latter "may well have errors in programming or modeling" (p. 263).

### 10.3 Direct simulation and rejection sampling (pp. 263–265)
- In simple non-hierarchical models, especially with conjugate priors, direct drawing is often easy. In harder problems, factor the distribution analytically: sample the marginal posterior of the hyperparameters, then the other parameters given the data and those draws (p. 263).
- The methods below draw a sample of size 1 and can be repeated. Saving intermediate results (e.g. a Cholesky factor of a fixed multivariate normal) can save time (p. 263). Appendix A covers standard distributions (p. 263).

**Grid approximation (pp. 263–264).**
- Compute the target density at evenly spaced $\theta_1,\dots,\theta_N$ covering a broad range. Use probabilities $p(\theta_i|y)/\sum_{j=1}^N p(\theta_j|y)$. An unnormalized $q$ works equally well, because of the normalization (pp. 263–264).
- Draw $U\sim\text{Uniform}[0,1]$ and apply the inverse-cdf method (Section 1.9) to the discrete approximation. This works when the points are close enough and miss nothing important beyond their boundaries (p. 264).
- In higher dimensions, a dense grid becomes prohibitively expensive (p. 264).

**Simulating from predictive distributions (p. 264).**
- For each posterior draw $\theta$, draw one $\tilde y$ from $p(\tilde y|\theta)$. The set of $\tilde y$'s characterizes the posterior predictive distribution. It is crucial to the model checking of Chapter 6 (p. 264).

**Rejection sampling (pp. 264–265).**
- Goal: one draw from $p(\theta|y)$ or from unnormalized $q$ (with $p=q/\int q\,d\theta$). We need a positive function $g(\theta)$, defined wherever $p>0$, with two properties (p. 264):
  1. We can draw from the density proportional to $g$. $g$ need not integrate to 1, but its integral must be finite.
  2. The **importance ratio** $p(\theta|y)/g(\theta)$ has a known bound: a known constant $M$ with $p(\theta|y)/g(\theta)\le M$ for all $\theta$.
- Algorithm (p. 264):
  1. Sample $\theta$ from the density proportional to $g(\theta)$.
  2. With probability $p(\theta|y)/(Mg(\theta))$, accept $\theta$ as a draw from $p$. If rejected, return to step 1.
- Figure 10.1 shows the curve $Mg$ lying above $p$. The acceptance probability of a draw is the ratio of the heights of the two curves at that $\theta$ (p. 264).
- Accepted draws have distribution $p(\theta|y)$ (Exercise 10.4). The bound is necessary so the step-2 probability does not exceed 1 (p. 265).
- A good $g$ is roughly proportional to $p$. If $g\propto p$, then with a suitable $M$ every draw is accepted. If $g$ is not near proportional, $M$ must be so large that almost all draws are rejected (p. 265).
- Rejection sampling is **self-monitoring**: if it is inefficient, few draws are accepted (p. 265).
- It is used in some fast samplers for standard univariate distributions. It is also often used for generic truncated multivariate distributions, if the density mass in the truncated part is not close to 1 (p. 265).

*Intuition note.* Throw points under a tall curve $Mg$ that covers the target. Keep a point with probability equal to the target's height divided by the cover's height. The kept points follow the target, and the tighter the cover, the fewer points are wasted.

### 10.4 Importance sampling (pp. 265–266)
- Importance sampling is related to rejection sampling and is a precursor of the Metropolis algorithm. It computes expectations from draws of an approximation to the target. It is for the case where we cannot draw from $p(\theta|y)$ (p. 265).
- If $g(\theta)$ is a density we can draw from:
$$\mathrm{E}(h(\theta|y))=\frac{\int h(\theta)q(\theta|y)\,d\theta}{\int q(\theta|y)\,d\theta}=\frac{\int [h(\theta)q(\theta|y)/g(\theta)]\,g(\theta)\,d\theta}{\int [q(\theta|y)/g(\theta)]\,g(\theta)\,d\theta},\tag{10.2}$$
estimated from $S$ draws $\theta^1,\dots,\theta^S$ from $g$ by
$$\frac{\frac1S\sum_{s=1}^{S}h(\theta^s)w(\theta^s)}{\frac1S\sum_{s=1}^{S}w(\theta^s)},\qquad w(\theta^s)=\frac{q(\theta^s|y)}{g(\theta^s)}.\tag{10.3}$$
  The $w$ are the **importance ratios** or **importance weights** (p. 265).
- Use the same draws in numerator and denominator to reduce sampling error (p. 265).
- If $hq/g$ can be made roughly constant, fairly precise estimates are possible. The method is not useful if the ratios vary substantially. The worst case is ratios small with high probability but huge with low probability, as happens if $q$ has wide tails compared to $g$ (p. 265).

**Accuracy and efficiency (p. 266).**
- Without mathematical analysis of the exact and approximate densities, we may have missed extremely large but rare weights. It helps to inspect a histogram of the logs of the largest importance ratios. Estimates are often poor if the largest ratios are too large relative to the average. Small ratios matter little (pp. 265–266).
- If the weights have finite variance, the effective sample size can be approximated by
$$S_{\rm eff}=\frac{1}{\sum_{s=1}^{S}(\tilde w(\theta^s))^2},\qquad \tilde w(\theta^s)=\frac{w(\theta^s)}{\sum_{s'=1}^{S}w(\theta^{s'})}.\tag{10.4}$$
  - $S_{\rm eff}$ is small if a few extremely high weights dominate.
  - With occasional very large weights, this estimate is itself noisy, so it is "no more than a rough guide" (p. 266).

**Importance resampling (SIR) (p. 266).**
- Goal: independent samples with equal weights. Given $S$ draws from $g$, draw $k<S$ as follows (p. 266):
  1. Sample $\theta$ from $\{\theta^1,\dots,\theta^S\}$, with probability of each $\theta^s$ proportional to $w(\theta^s)=q(\theta^s|y)/g(\theta^s)$.
  2. Sample a second value the same way, excluding the already sampled value.
  3. Repeat without replacement $k-2$ more times.
- **Footnote 1 (p. 266).** With moderate weights, sampling with and without replacement gives similar results.
  - With a few large weights and many small ones, sampling with replacement repeats the same few $\theta$. Without replacement gives an intermediate approximation between the starting and target densities. For other purposes, with replacement could be better.
  - A "P.S." says the authors now recommend Pareto smoothed importance resampling with replacement instead (p. 266).

**Uses (p. 266).**
- It can improve analytic approximations (Chapter 13). If importance sampling is not accurate, resampling can still give starting points for iterative simulation (Chapter 11) (p. 266).
- It helps with mild changes to a posterior, e.g. normal→$t$ in the 8 schools model, or leave-one-out cross-validation. The original posterior serves as the approximation to the modified one (p. 266).
- To learn it, program simple examples: $t_3$ approximating the normal is good practice, the reverse is bad practice (Exercises 10.6, 10.7). $g$ should cover all important regions of the target (p. 266).

*Intuition note.* Draw from an easy distribution $g$, then correct by giving each draw the weight "target height / $g$ height". The ratio form (10.3) lets us use $q$ with unknown normalizing constant. Trouble comes when a few draws get enormous weights, since then the answer depends on very few points.

### 10.5 How many simulation draws are needed? (pp. 267–268)
- Posterior inference is usually summarized by draws. Reporting the 2.5%, 25%, 50%, 75% and 97.5% points gives a 50% and a 95% posterior interval and shows skewness. Scatterplots or contour plots serve in 2–3 dimensions. Quantities of interest may depend on parameters (e.g. LD50, Section 3.7) or on parameters and data (p. 267).
- Predictive quantities: for each $\theta^s$ draw $\tilde y^s\sim p(\tilde y|\theta^s)$ (or $p(\tilde y|\tilde X,\theta^s)$ in regression). Example: predicted probability of Clinton winning each state in 1992 (Fig. 6.1) (p. 267).
- For model checking, simulate a replicated dataset $y^{\mathrm{rep},s}$ from each $\theta^s$ (Chapter 6) (p. 267).
- The goal is a set of **independent** draws, with enough of them for reasonable accuracy. For most examples, $S=100$ independent draws are enough for reasonable posterior summaries (p. 267).
- Argument for the claim (p. 267): take a scalar $\theta$ with approximately normal posterior, mean $\mu_\theta$, sd $\sigma_\theta$, estimated by the draws' mean $\bar\theta$ and sd $s_\theta$.
  - The posterior mean is estimated to accuracy about $s_\theta/\sqrt S$.
  - The total sd of the computed estimate, including **Monte Carlo error** (uncertainty from a finite number of draws), is $s_\theta\sqrt{1+1/S}$.
  - For $S=100$, $\sqrt{1+1/S}=1.005$, so Monte Carlo error adds almost nothing to the actual posterior uncertainty.
  - More than 100 draws can make numerical summaries more stable, though this typically confers no important practical advantage.
- Some inferences need more draws. A posterior probability $p$ has estimation sd $\sqrt{p(1-p)/S}$. So $S=100$ gives accuracy 5% near $p=0.5$, and $S=2500$ gives 1%. Rare events need even more draws, unless analytic methods help (p. 267).

**Example: educational testing (8 schools) (pp. 267–268).**
- Parameter $\theta_1$ (school A effect), from 200 draws (Table 5.3): median 10, 50% interval [7, 16], 95% interval [−2, 31] (p. 267).
- Another 200 draws: median 9, 50% [6, 14], 95% [−4, 32]. With $S=10{,}000$: median 10, 50% [6, 15], 95% [−2, 31]. The intervals differ slightly but convey the same information (p. 267).
- $\Pr(\theta_1>\theta_3|y)$ was estimated as 0.73 from 200 draws. The accuracy is $\sqrt{0.73(1-0.73)/200}=0.03$, "good enough in this example" (p. 268).
- Rare event $\Pr(\theta_1>50)$: none of 200 draws exceeds 50, so the simple estimate is zero (or below 1/200). With $S=10{,}000$, 3 draws exceed 50, giving a crude estimate 0.0003 (p. 268).
- Semi-analytic alternative (p. 268): given $\mu,\tau$, the posterior of $\theta_1$ is $\mathrm N(\hat\theta_1,V_1)$ (see (5.17)), with mean and variance depending on $y_1,\mu,\tau$.
  - Then $\Pr(\theta_1>50|\mu,\tau,y)=\Phi\big((\hat\theta_1-50)/\sqrt{V_1}\big)$.
  - Average this over the draws $(\mu^s,\tau^s)$ to estimate $\Pr(\theta_1>50|y)$. With this approach $S=200$ draws are sufficient for a reasonably accurate estimate.
- General rule: fewer draws are needed for posterior medians, probabilities near 0.5 and low-dimensional summaries than for extreme quantiles, posterior means, rare-event probabilities and higher-dimensional summaries. The book typically uses 100–2000 draws, to stress that applied inferences do not typically need high simulation accuracy (p. 268).

*Intuition note.* The error of an average of $S$ independent draws shrinks like $1/\sqrt S$. But this error is added to a much larger posterior spread, so it stops mattering quickly. Rare events are different: with 200 draws you may see none of them.

### 10.6 Computing environments (pp. 268–270)
- Programs exist for full Bayesian inference in common models (hierarchical linear and logistic regression, some nonparametric models). They combine algorithms from later chapters (p. 268).
- Four reasons for an automatic, general program (pp. 268–269):
  1. Many researchers lack the skills to program inference themselves. They would like to fit Bayesian models, which include familiar models as special cases and allow robust errors, mixtures and prior information.
  2. Teaching: students can first focus on model structure and learn algebra and computing later. A deeper understanding is still useful, since models are understood by comparing them with similar ones and fitting by seeing it as a map from data and assumptions to inferences.
  3. A programming environment for implementing new models.
  4. Speed: an automatic program is used many times, so it pays to optimize it, parallelize it, and include harder algorithms.
- "No program can be truly general." Software should be open, so a sophisticated user can alter it (p. 269).
- **Bugs** (1990s–early 2000s; Bayesian inference using Gibbs sampling) (p. 269):
  - The user gives data and a model in a notation close to probability notation. The program uses Gibbs sampling, Metropolis and slice sampling.
  - Models can be assembled arbitrarily from many distributions.
  - Its limits are computational. It is good for complicated models with small datasets, but slow with large datasets and multivariate structures. It updates one scalar parameter at a time, so convergence is slow when parameters are strongly dependent, as can occur in hierarchical models.
- **Stan** (open-source, C++, named after Stanislaw Ulam) (p. 269):
  - Similar functionality to Bugs, with a Bugs-like language, but uses Hamiltonian Monte Carlo (Section 12.4).
  - It is extendable, serves general users and method developers, and is the authors' current tool. See Section 12.6 and Appendix C.
- Other software named: mcsim, PyMC, HBC, plus commercial programs under development (pp. 269–270).

### 10.7 Debugging Bayesian computing (pp. 270–271)
- Build confidence by fitting different versions of the model and noticing unexpected changes (crude inferences, Section 10.2). Check convergence with parallel simulations from different starting points (Section 11.4) (p. 270).
- **Fake-data debugging**, for complicated models or unbelievable inferences (p. 270):
  1. Pick a reasonable "true" $\theta$. Strictly it should be a draw from the prior. If the prior is noninformative, any reasonable value should work.
  2. For a hierarchical model, pick reasonable hyperparameters, then draw the other parameters from the prior given them.
  3. Simulate a large fake dataset $y^{\rm fake}$ from $p(y|\theta)$.
  4. Compute the posterior $p(\theta|y^{\rm fake})$.
  5. Compare with the true $\theta$. For any element, there should be a 50% probability that its 50% posterior interval contains the truth.
- Formally, the procedure requires proper priors and frequency evaluations averaged over many true $\theta$ drawn independently from the prior. In practice, one reasonable $\theta$ can be useful. If results are unreasonable, "there is probably something wrong" in the computation or model (p. 270).
- A single fake dataset can reveal problems if the true $\theta$ is far outside the computed posterior. With high-dimensional $\theta$, compute the proportion of 50% intervals containing the truth (p. 270).
- **Residual plot** (p. 270): for each scalar $\theta_j$, predicted value = average of posterior simulations; error = true $\theta_j$ − predicted. If the computation is correct, errors should have zero mean. Plot errors vs predicted values, one dot per parameter. For models with few parameters, repeat many fake-data simulations with new true $\theta$ and new $y^{\rm fake}$, and check zero-mean errors and correct interval coverage on average.
- **Model checking and convergence checking** (Chapters 6, 7, Section 11.4) can also be read as debugging. Gross misfit or odd replicated data are often computing errors: unrecoded discrete responses (1 = Yes, 0 = No, −9 = Don't Know), a misspelled predictor, or a miscomputed Metropolis ratio (Section 11.2). Poor convergence can come from programming or conceptual errors (p. 271).
- If it is unclear whether the bug is in the program or the model, **simplify**: remove parameters, fix them or give them highly informative priors, or analyze data sources separately. Do it in steps: remove a parameter; set it to a null value (e.g. zero) to check it has no effect; fix it at a nonzero value; give it a precise prior; then estimate it from the data. Model building goes back and forth between simpler and more complex models (p. 271).

### 10.8 Bibliographic note (pp. 271–272)
- References are given on simulation, numerical integration and Bayesian quadrature, importance sampling and resampling, and Bugs and Stan. Points stated: Rubin (1987b) introduced importance resampling. Skare et al. (2003) discuss why to resample without replacement for $k<S$. For $k=S$, stratified, deterministic and residual resampling have smaller variance than simple random resampling. Cook, Gelman and Rubin (2006) and Gelman and Hill (2007, ch. 8) show fake-data checking (pp. 271–272).

### 10.9 Exercises (pp. 272–273)
Eight exercises. They cover simulation-draw counts (1, 2), binomial two-sample posteriors (3), proof of rejection sampling (4), rejection and importance sampling in a logistic model (5), importance sampling with good and bad weights (6, 7), and resampling with and without replacement for the bioassay example (8). See "Exercises worth doing".

## Toy example (ours, not from the text)
Target: $p(\theta)=2\theta$ on $[0,1]$. Unnormalized: $q(\theta)=\theta$. Take $g(\theta)=1$ (uniform), which we can draw from.

**Rejection sampling.** $p/g=2\theta\le 2$, so $M=2$. Acceptance probability $p/(Mg)=2\theta/2=\theta$.
- Draw $\theta=0.8$. Second uniform $u=0.5$. Since $0.5<0.8$, accept.
- Draw $\theta=0.3$. Second uniform $u=0.6$. Since $0.6>0.3$, reject and return to step 1.
- Accepted values have density $\propto g(\theta)\cdot\theta=\theta$, which is $p$ (after normalizing). The overall acceptance rate is $\int_0^1\theta\,d\theta=0.5=1/M$.

**Importance sampling for $\mathrm E(\theta|y)$** with $h(\theta)=\theta$ and $w=q/g=\theta$. Use three uniform draws $0.2,\,0.5,\,0.8$:
- $w=0.2,\,0.5,\,0.8$.
- Numerator of (10.3): $\tfrac13(0.2\cdot0.2+0.5\cdot0.5+0.8\cdot0.8)=\tfrac13(0.04+0.25+0.64)=0.93/3=0.31$.
- Denominator: $\tfrac13(0.2+0.5+0.8)=1.5/3=0.5$.
- Estimate $=0.31/0.5=0.62$. The true value is $\int_0^1\theta\cdot2\theta\,d\theta=2/3\approx0.667$. Three draws give a crude answer.
- Normalized weights: $0.2/1.5=0.1333$, $0.5/1.5=0.3333$, $0.8/1.5=0.5333$. Squares: $0.01778$, $0.11111$, $0.28444$. Sum $=0.41333$.
- By (10.4), $S_{\rm eff}=1/0.41333\approx2.42$. This is below $S=3$ because the weights are unequal.

## Concepts
- [[unnormalized-density]] — a function $q(\theta|y)$ proportional to the posterior in $\theta$, e.g. prior × likelihood; enough for grids, rejection and importance sampling (p. 261) (new)
- [[monte-carlo-integration]] — approximate $\mathrm E(h(\theta)|y)$ by $\frac1S\sum h(\theta^s)$ using posterior draws (p. 262)
- [[monte-carlo-error]] — uncertainty from using finitely many draws; for a roughly normal posterior, mean error $\approx s_\theta/\sqrt S$ (p. 267) (new)
- [[posterior-predictive-distribution]] — draw one $\tilde y$ from $p(\tilde y|\theta^s)$ for each posterior draw $\theta^s$ (p. 264)
- [[credible-interval]] — 50% and 95% posterior intervals read from the 25/75 and 2.5/97.5 percentiles of draws (p. 267)
- [[rejection-sampling]] — accept a draw from $g$ with probability $p/(Mg)$, where $p/g\le M$; self-monitoring (p. 264) (new)
- [[importance-sampling]] — estimate expectations from draws of $g$ with weights $q/g$ via ratio estimator (10.3) (p. 265) (new)
- [[effective-sample-size]] — $S_{\rm eff}=1/\sum\tilde w^2$ for normalized importance weights; rough guide (p. 266) (new)
- [[importance-resampling]] — resample $k<S$ draws with probability proportional to weight, without replacement (p. 266) (new)
- [[fake-data-simulation]] — debug by simulating a "true" $\theta$ and data, fitting, and comparing with the truth (p. 270) (new)
- [[convergence-diagnostics]] — here, running parallel simulations from different starting points and checking they mix (p. 270)
- [[markov-chain-monte-carlo]], [[gibbs-sampling]], [[hamiltonian-monte-carlo]] — mentioned only as the engines of Bugs and Stan, developed in later chapters (pp. 262, 269)

## Canonical instances
- [[eight-schools]] — used for crude estimation, for simulation-count and rare-event examples, and for the semi-analytic estimate of $\Pr(\theta_1>50)$ (pp. 263, 267–268) (new)
- [[rat-tumor-example]] — crude hyperparameter estimates used to start (p. 263) (new)
- [[bioassay-example]] — LD50 as a quantity of interest (p. 267); Exercise 8 (p. 273) (new)
- [[bugs-and-stan]] — general-purpose Bayesian software and its limits (p. 269) (new)

## Bridges (candidates)
- [same-math] Monte Carlo error $s_\theta/\sqrt S$ ↔ statistics: standard error of a sample mean — same formula, applied to simulation draws.
- [structural-analogy] Importance weights $q/g$ and $S_{\rm eff}$ ↔ causal inference: inverse-probability weighting — reweighting draws from one distribution to represent another, with a few huge weights hurting precision.
- [structural-analogy] Fake-data debugging ↔ frequentist evaluation: interval coverage checked on simulated data — the 50% interval should cover the truth half the time.
- [metaphor] Crude estimate as a sanity anchor ↔ engineering: back-of-envelope check before a detailed simulation.

## Questions this raises
- When draws are dependent (MCMC, Chapters 11–12), how does the $s_\theta/\sqrt S$ argument change, and what replaces $S$?
- How can we detect, from the draws alone, that importance weights have infinite variance, so that $S_{\rm eff}$ in (10.4) is not valid?
- Why does the fake-data check require proper priors for its formal justification (p. 270)?
- If a general program such as Stan is used, how much of the debugging in Section 10.7 still falls on the user?

## Exercises worth doing
- Ex. 1 (p. 272) — how many independent draws specify the 2.5% and 97.5% quantiles to 0.1 sd; shows quantiles need more draws than means — difficulty: medium
- Ex. 2 (p. 272) — simulation sd of posterior mean and quantiles for 100 draws, and draws needed to reach 0.1; also ties to the 8 schools quantiles — difficulty: medium
- Ex. 4 (p. 273) — prove rejection sampling is correct and explain why the bound is needed — difficulty: medium
- Ex. 6 (p. 273) — importance sampling with a $t_3$ approximation to a normal posterior; log-ratio histogram and (10.4) — difficulty: medium
- Ex. 7 (p. 273) — reverse roles (normal approximating $t_3$); explain why $\mathrm{var}(\theta|y)$ estimates are too low — difficulty: hard
- Ex. 8 (p. 273) — importance resampling with and without replacement on the bioassay posterior — difficulty: medium

## Reading notes
- Pages are pdf 271–284. Printed = pdf − 10. Pdf 284 (printed 274) is blank apart from the running header; the unit text ends on printed p. 273.
- The text layer shows θ as ω in many places and garbles some symbols. I used the images, which show θ throughout.
- Running header on every page: "This electronic edition is for non-commercial purposes only." Chapter number and title as printed: "Chapter 10 / Introduction to Bayesian computation".
- Apparent misprints in the images: the sentence introducing (10.1) writes "any function $h(\theta|y)$" and "desired distribution $p(\theta)$", and (10.2) writes $\mathrm E(h(\theta|y))$, where the text elsewhere (including (10.1) itself) has $\mathrm E(h(\theta)|y)$. In Exercise 4(b) the bound is written $p(\theta|y)/q(\theta)$, while the text uses $g(\theta)$. Exercise 7 calls $g$ an "unnormalized density" without comment.
- The "Crude estimation" subsection (p. 263) sits under the 10.2 heading and before the 10.3 heading. Section 10.7 refers to it as "Section 10.2".
- Footnote 1 on p. 266 includes a later "P.S." recommending Pareto smoothed importance resampling with replacement. I report it as printed, without further detail.
- I did not detail the bibliographic note (10.8) beyond a few stated points. Exercise solutions are not printed in this unit.
