---
id: mcelreath-2020-rethinking/ch08-markov
work: mcelreath-2020-rethinking
unit: Chapter 8. Markov Chain Monte Carlo
pages: 241-266
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Markov Chain Monte Carlo

## L0 — One line
A random walk that moves between parameter values with probabilities tied to posterior density can produce posterior samples without assuming a Gaussian shape, but you must inspect the chain to check that it worked.

## L1 — The gist (≤ 120 words)
How can we sample a posterior without assuming it is Gaussian? The chapter introduces Markov chain Monte Carlo (MCMC): a random walk that visits parameter values in proportion to their posterior probability. It builds the idea from King Markov's Metropolis algorithm. It then contrasts Gibbs sampling with Hamiltonian Monte Carlo (HMC), and shows how to fit earlier models with Stan through `map2stan`. Much of the chapter is diagnosis: trace plots, effective sample size, Rhat (a convergence check). Two pathological examples show how flat priors and non-identifiable parameters give wild chains, and how weakly informative priors can cure them. This matters because some later models cannot be fit without an MCMC approach.

**Prerequisites:** posterior distribution and samples from it (Ch. 3); quadratic approximation (`map`); linear and interaction regression (Ch. 5, 7); priors; basic R syntax.

## L2 — Key ideas (5–10 bullets)
- MCMC draws samples from the joint posterior without maximizing anything and without assuming a Gaussian shape. The price is that it may take much longer and usually needs more work to specify the model (p. 241).
- Metropolis algorithm: propose a neighbouring value, then move with probability given by the ratio of target values (proposal over current), capped at 1. In the long run, visits are proportional to the target. Proposals must be symmetric (pp. 243–245).
- Gibbs sampling makes adaptive proposals and is more efficient than Metropolis. It relies on conjugate pairs (prior–likelihood combinations with an exact posterior for a single parameter), and becomes very inefficient for models with very many parameters (pp. 245–246).
- HMC simulates a frictionless particle gliding over the log-posterior (the log of the posterior density). It is much more computationally costly, but its proposals are typically more efficient, especially for complex models. It needs continuous parameters and tuning, which Stan largely automates (pp. 246–247).
- `map2stan` turns a `map` formula list into Stan HMC code. Preprocess variable transformations first, and trim the data frame to the variables used (technically optional, but it avoids problems such as `NA` making Stan refuse to work) (pp. 247–249).
- Healthy chains are stationary (stay within the posterior) and well mixing (successive samples not highly correlated). The trace plot is nearly always the first check; `n_eff` (a crude count of independent samples) and Rhat (a convergence estimate) are further diagnostics. Rhat may be viewed "perhaps as a signal of danger, but never of safety" (pp. 250, 253, 257).
- Practical advice for typical regression models: four short chains to check, one long chain for inference. Warmup is not burn-in: Stan's warmup samples adapt the sampler and are not part of the target distribution (pp. 256–257).
- Flat priors can give wild chains. Non-identifiable parameters (here, two parameters of which only the sum is identified) can give chains that wander and mix badly. In the two examples, weakly informative priors (priors that only gently rule out absurd values) cured both, and weak priors can also speed up sampling (pp. 257–262).

## L3 — Walkthrough

### Introduction (p. 241)
- Chance used to be seen as a villain, but by the early 20th century chance and understanding cooperated. MCMC is one example (p. 241).
- Unlike earlier chapters, here we get samples from the joint posterior "without maximizing anything." We need no quadratic or other assumed shape (p. 241).
- Cost: it may take much longer, and more work is needed to specify the model. Benefit: no multivariate normality is assumed. Generalized linear and multilevel models routinely give non-Gaussian posteriors, and sometimes cannot be estimated with earlier techniques (p. 241).
- Tools: Stan is the engine. The `rethinking` package hides it for now (p. 241).
- Aside: Stan is named after Stanislaw Ulam, one of the inventors of MCMC (p. 242).

### 8.1 Good King Markov and his island kingdom (pp. 242–244)
- Setup: 10 islands in a ring, each with two neighbours. Island $k$ has relative population $k$. The king must visit each island in proportion to its population. He wants no schedule and moves only between adjacent islands (p. 242).
- Metropolis algorithm, as advisor Metropolis designs it (pp. 242–243):
  1. Each week the king chooses between staying and moving to a neighbour, using a coin flip.
  2. Heads nominates the clockwise neighbour, tails the counterclockwise one. This is the **proposal island**.
  3. He counts out seashells equal to the proposal island's population and stones equal to the current island's population.
  4. If shells exceed stones, he always moves. If shells are fewer, he discards as many stones as shells. He puts the rest in a bag and draws one object: a shell means move, a stone means stay. So $\Pr(\text{move})$ = shells / original stones (p. 243).
- Compact form (added step; equivalent to the rule above and to the code's `prob_move <- proposal/current`):
$$\Pr(\text{move}) = \min\!\left(1,\ \frac{\text{pop(proposal)}}{\text{pop(current)}}\right)$$
- The author's R code 8.1 loops over 1e5 weeks starting at island 10. It records the position, proposes `current + sample(c(-1,1))`, wraps 0 to 10 and 11 to 1, then moves if `runif(1) < proposal/current` (p. 243).
- Result (Fig. 8.2): in the first 100 weeks the path looks patternless. After 100,000 weeks the time on each island is almost exactly proportional to its population (p. 244).
- The author says the algorithm still works if the king may propose any island from any island, as long as he keeps the same move probability. It works for any size archipelago, even if he does not know how many islands there are. He needs only the current and proposal populations (p. 244).
- **Intuition note:** The rule uses only a ratio of two populations, so the king never needs the total population. Moving always to bigger islands and only sometimes to smaller ones gives the right long-run time shares. For posteriors, this suggests why a normalizing constant would not be needed (our remark; the text does not make this point).

### 8.2 Markov chain Monte Carlo (pp. 245–247)
- Mapping to inference (p. 245):
  - islands = parameter values, which may be continuous;
  - populations = posterior probabilities at each parameter value;
  - weeks = samples from the joint posterior.
- If proposals are symmetric (equal chance of proposing A→B and B→A), Metropolis will eventually give samples from the joint posterior. These are used like earlier samples (p. 245).
- Metropolis is the "grandparent" of other methods. The chapter explains Gibbs sampling and Hamiltonian Monte Carlo. The book uses HMC (p. 245).

**8.2.1 Gibbs sampling (pp. 245–246)**
- Metropolis–Hastings allows asymmetric proposals, as if the king's coin were biased (p. 245).
- Reasons for asymmetric proposals: easier handling of parameters bounded at zero, such as standard deviations. A better reason is that "savvy" proposals explore the posterior more efficiently, meaning an equally good picture in fewer steps (p. 245).
- Gibbs sampling is a variant of Metropolis–Hastings with adaptive proposals, which adjust to the current parameter values. It depends on **conjugate pairs** (prior and likelihood combinations with an analytical posterior for an individual parameter). These solutions allow smart jumps around the joint posterior (p. 245).
- It underlies BUGS and JAGS (p. 246).
- Limitations (p. 246):
  - you may not want conjugate priors, and picking a prior for efficient fitting is not a strong scientific argument;
  - with hundreds to tens of thousands of parameters, Gibbs becomes "shockingly inefficient".

**8.2.2 Hamiltonian Monte Carlo (pp. 246–247)**
- Jaynes (quoted by the author): when there is a randomized way of doing something, a nonrandomized way gives better performance but needs more thought. Metropolis and Gibbs are highly random, and Gibbs reduces randomness by exploiting knowledge of the target. HMC pushes this further (p. 246).
- HMC is much more computationally costly, but its proposals are typically much more efficient. It needs fewer samples and can outshine others with thousands of parameters (p. 246).
- Fable: King Monty rules a continuous valley and has an advisor, Hamilton. They travel back and forth along the valley, slowing down where houses are denser and speeding up where they are sparser. This needs the local rate of change of density, but not memory of past positions. The king sweeps the whole kingdom before revisiting anyone (p. 246).
- Analogy: the vehicle is the current vector of parameter values. With one parameter the log-posterior is like a bowl with the MAP at the bottom (p. 247).
- HMC runs a physics simulation of a frictionless particle gliding over the log-posterior surface (p. 247).
  - A flat surface lets it glide long before the slope turns it around.
  - A steep surface, from concentrated likelihood or priors, turns it around quickly.
- Limits (p. 247):
  - HMC requires continuous parameters, so techniques like imputing discrete missing data are not possible with HMC alone;
  - some models remain hard for any MCMC;
  - it needs tuning to a model and data (the particle's mass, plus other algorithm settings). Stan automates much of this.
- **Intuition note:** Metropolis wanders by trial and error. HMC's particle glides along the log-posterior surface: far when it is flat, turning back sooner when it is steep. The author reports that HMC stays efficient where ordinary Metropolis or Gibbs sampling wander slowly (p. 247).

### 8.3 Easy HMC: map2stan (pp. 247–253)
- `map2stan` compiles a formula list, like those used for `map`, into Stan HMC code (p. 247).
- Example: the terrain ruggedness model from Ch. 7. Data: `log_gdp <- log(rgdppc_2000)`, keeping complete cases (R code 8.2, p. 248). Model with `map` (R code 8.3):
$$\text{log\_gdp}_i \sim \text{Normal}(\mu_i,\sigma),\quad \mu_i = a + b_R\,\text{rugged}_i + b_A\,\text{cont\_africa}_i + b_{AR}\,\text{rugged}_i\,\text{cont\_africa}_i$$
  with $a\sim\text{Normal}(0,100)$; $b_R,b_A,b_{AR}\sim\text{Normal}(0,10)$; $\sigma\sim\text{Uniform}(0,10)$ (p. 248).
- Quadratic approximation estimates: $a$ 9.22, $b_R$ −0.20, $b_A$ −1.95, $b_{AR}$ 0.39, $\sigma$ 0.93 (p. 248).

**8.3.1 Preparation (p. 248–249).** Two extra steps:
1. Preprocess all variable transformations (log, squares, and so on) before fitting.
2. Make a trimmed data frame containing only the variables used (`dd.trim`, 170 observations, 3 variables). This is technically optional, but avoids problems. For example, `NA` in unused variables makes Stan refuse to work (p. 248–249).

**8.3.2 Estimation (p. 249–250).**
- Same formulas, but $\sigma\sim\text{HalfCauchy}(0,2)$ (`dcauchy(0,2)`) instead of uniform. The Cauchy is a thick-tailed distribution related to Student t. The author calls it a weakly regularizing prior for standard deviations (p. 249).
- A uniform or an exponential prior would also work here. There is so much data that the prior hardly matters (p. 249).
- Stan estimates (R code 8.6): $a$ 9.24, $b_R$ −0.21, $b_A$ −1.97, $b_{AR}$ 0.40, $\sigma$ 0.95. `n_eff` is 291, 306, 351, 350, 566, and Rhat is 1 for all (p. 249).
- Intervals are now HPDI (highest posterior density intervals) rather than percentile intervals. Two new columns:
  - `n_eff`: a crude estimate of the number of independent samples;
  - `Rhat`: a complicated estimate of convergence of the chains. It should approach 1.00 from above when all is well (p. 250).

**8.3.3 Sampling again, in parallel (p. 250).** Passing the fit back with `chains=4, cores=4` runs four independent chains in parallel. `n_eff` rises to 1029, 1057, 1154, 1144, 1960 (p. 250).

**8.3.4 Visualization (pp. 250–252).**
- `extract.samples` returns a list, not a data frame. There are 1000 samples per parameter by default (p. 250).
- `pairs(m8.1stan)` gives Fig. 8.3: densities on the diagonal and correlations below it. Examples: $a$–$b_R$ −0.79; $b_A$–$b_{AR}$ −0.68; $a$–$\sigma$ 0.03 (p. 251).
- The posterior is "quite nearly multivariate Gaussian". The density for $\sigma$ is skewed, but otherwise the quadratic approximation does almost as well. The author notes this is a simple model with Gaussian priors, so this is no surprise (p. 252).
- Overthinking: Stan messages. Stan translates the model to C++ and compiles it. Occasional warnings such as "Covariance matrix is not positive definite" are usually harmless if they occur only a handful of times, especially during warmup. Frequent occurrence may mean an ill-conditioned or misspecified model (p. 252).

**8.3.5 Using the samples (pp. 252–253).** With samples and the model you can simulate predictions, compute differences between parameters, and compute DIC and WAIC. `map2stan` reports DIC 468.73 (pD 4.94) and WAIC 469.3 (SE 14.8, pWAIC 5.14). `postcheck`, `link`, `sim`, `compare` and `ensemble` work as for `map` models (pp. 252–253).

**8.3.6 Checking the chain (pp. 253–254).**
- If the chain is defined correctly, it is guaranteed to converge in the long run to the posterior. But "the machine does sometimes malfunction" (p. 253).
- **Trace plot:** the samples in sequence, joined by a line. It is the king's path in the fable. It is nearly always the first check, not the last (p. 253).
- Fig. 8.4 (`plot(m8.1stan)`): the gray region is warmup (first 1000 samples) during which the chain adapts, so these samples are not necessarily reliable for inference. `extract.samples` discards them (p. 253).
- Two things to look for (p. 253–254):
  - **Stationarity:** the path stays within the posterior, around a stable central tendency. The mean is stable from start to end.
  - **Good mixing:** each sample is not highly correlated with the one before. This shows as rapid zig-zagging with no getting mired.
- Overthinking: `stancode(m8.1stan)` shows the raw Stan code. The model block reiterates the formulas in reverse order: priors, then `mu[i]`, then the likelihood `log_gdp ~ normal(mu, sigma)` (pp. 254–255).
- **Intuition note:** A healthy trace looks like fuzzy noise around a flat band. A drifting or sticky trace suggests the chain is not describing the posterior.

### 8.4 Care and feeding of your Markov chain (pp. 255–262)
- Most users do not understand MCMC internals, which is acceptable up to a point. HMC, unlike Gibbs and ordinary Metropolis, makes it easy to tell when things go wrong (p. 255).

**8.4.1 How many samples? (pp. 255–256)**
- `iter` defaults to 2000 and `warmup` to `iter/2`, giving 1000 warmup and 1000 inference samples. These defaults are meant to get you started (p. 255).
- What matters is the effective number of samples (an estimate of independent samples), not the raw number. Chains are autocorrelated. Stan chains tend to be less autocorrelated than others, but always somewhat (p. 255).
- It depends on what you want to know (p. 255):
  - posterior means: even a couple hundred samples do;
  - extreme tails, such as the 99th percentile: many more;
  - in typical regression, about 200 effective samples can give a very good posterior mean. If the posterior is approximately Gaussian, a good variance estimate needs about an order of magnitude more, in most cases.
- Warmup: use the shortest necessary, but more can mean more efficient sampling. As much as half of `iter` typically works well, and simple models need much less. If in trouble, try more; if not, try less (p. 256).
- **Warmup is not burn-in** (p. 256). Burn-in trims the early part of a chain, to hopefully remove the influence of the starting value. Stan's warmup samples are used to adapt the sampler and are not part of the target distribution at all. Real sampling is immediately from the target, assuming adaptation succeeded. For bad chains, warmup can look good while real sampling shows severe problems (p. 256).

**8.4.2 How many chains? (pp. 256–257)**
- Three answers: when debugging, use one chain. When deciding whether chains are valid, use more than one. For the final inference run, one chain is enough, though more is fine (p. 256).
- Multiple chains check that all converge to the same region. A single chain may settle to a stable-looking distribution, and a rerun may settle to a different one. 3 or 4 chains is conventional (p. 256).
- Example: with 1000 warmup and about 9000 real samples, one chain (`iter=10000`) versus 3 chains (`iter=4000`) makes no real difference for inference, according to the author. The 3 chains cost an extra 2000 warmup samples, and warmup is typically the slowest part. Separate cores could still make 3 chains finish faster (p. 257).
- Motto for typical regression: **four short chains to check, one long chain for inference** (p. 257).
- Rethinking: convergence diagnostics (p. 257).
  - `n_eff` much lower than the number of post-warmup iterations means inefficient chains, but possibly still okay.
  - Rhat above 1.00 usually indicates the chain has not converged, so probably don't trust the samples. More iterations may or may not fix it.
  - Do not rely too much on these. Rhat can reach 1.00 even for an invalid chain, so view it "perhaps as a signal of danger, but never of safety."

**8.4.3 Taming a wild chain (pp. 257–260)**
- Problem: broad, flat regions of the posterior, most often from flat priors. They produce a chain that erratically samples extreme positive and negative values (p. 257).
- Model m8.2: data $y=(-1,1)$, $\mu=\alpha$, completely flat priors, 2 chains, `iter=4000`, `warmup=1000` (R code 8.13, p. 257).
- Results (R code 8.14): $\alpha$ mean 21,583,691 (sd 54,448,550), `n_eff` 7, Rhat 1.36. $\sigma$ mean 139,399,593, `n_eff` 72, Rhat 1.02 (p. 258). The mean of the data is 0, so these are wrong.
- Rules of thumb stated by the author: a value of 1.01 is suspicious, and Rhat 1.10 indicates a catastrophe (p. 258).
- Trace (Fig. 8.5, top): drifting and spiking, not stationary (p. 258).
- Cause: two observations and flat priors. A flat prior says every value is equally plausible a priori, so for an unbounded parameter the chain must occasionally visit extreme values like negative 30 million, which overwhelm it. With a stronger likelihood, the chain would stay near zero (p. 258).
- Model m8.3 with weakly informative priors (p. 259):
$$y_i\sim\text{Normal}(\mu,\sigma),\quad \mu=\alpha,\quad \alpha\sim\text{Normal}(1,10),\quad \sigma\sim\text{HalfCauchy}(0,1)$$
- Results: $\alpha$ −0.01 (sd 1.60), $\sigma$ 1.98 (sd 1.91), `n_eff` 1121 and 1077, Rhat 1 (p. 259). The trace is healthy (Fig. 8.5, bottom) (p. 259).
- The priors are very gradual slopes, so the likelihood nearly overcomes them even with two observations. The prior mean of $\alpha$ is 1, but the posterior mean is 0. The posterior median of $\sigma$ is around 1.4, and the data's standard deviation is 1.4 (pp. 259–260).
- Such priors give "a very gentle nudge towards reasonable values". They are washed out almost at once, yet still make the difference between getting an answer or not (p. 260).
- **Intuition note:** In this example the likelihood almost completely overcomes such a prior, yet the prior still makes the difference between getting an answer and not, by giving a gentle nudge away from absurd values (p. 260).
- Overthinking: Cauchy distribution (p. 260).
  - It is the distribution of the ratio of two Gaussian draws, with location $x_0$ and scale $\gamma$:
$$p(x\mid x_0,\gamma) = \left(\pi\gamma\left[1+\left(\frac{x-x_0}{\gamma}\right)^2\right]\right)^{-1}$$
  - It has no defined mean or variance, so $x_0$ and $\gamma$ are not mean and standard deviation. It is thick-tailed, and any draw may be extreme enough to overwhelm all earlier ones, so the running mean never settles. The author's code 8.16 plots the running mean of 10,000 `rcauchy(1e4,0,5)` draws (p. 260).
  - Cauchy priors on $\sigma$ are implicitly half-Cauchy (positive reals only). Stan knows this from the `<lower=0>` constraint (p. 260).

**8.4.4 Non-identifiable parameters (pp. 260–262)**
- Ch. 5 showed non-identifiable parameters from highly correlated predictors. Here we see them inside a chain (p. 260).
- Data: 100 draws of `rnorm(100, 0, 1)`. Model m8.4: $y_i\sim\text{Normal}(\mu,\sigma)$, $\mu=\alpha_1+\alpha_2$, $\sigma\sim\text{HalfCauchy}(0,1)$. Only the sum $\alpha_1+\alpha_2$ can be identified, and it should be about zero (pp. 260–261).
- Results (R code 8.18, p. 261):

| | Mean | StdDev | `n_eff` | Rhat |
|---|---|---|---|---|
| a1 | −1194.76 | 1344.19 | 1 | 2.83 |
| a2 | 1194.81 | 1344.19 | 1 | 2.83 |
| sigma | 0.92 | 0.07 | 17 | 1.13 |

- The two means are about equally far from zero on opposite sides. The traces (Fig. 8.7, left) are neither stationary nor well mixing, and the author says: "Don't use these samples" (p. 261).
- Model m8.5 adds $\alpha_1,\alpha_2\sim\text{Normal}(0,10)$. Results: a1 −0.23 (sd 6.97), a2 0.28 (sd 6.97), `n_eff` about 1223, Rhat 1 (p. 262).
- With flat priors (m8.4), sampling may take 8 times as long as for m8.5. A very slow model is often under-identified. This is an aspect of Gelman's **folk theorem of statistical computing**: trouble fitting a model often indicates a bad model (p. 262).
- Complex models, especially with many predictors and interactions, can easily become unidentified or nearly so. "A flat prior really is flat, all the way to infinity." Weak priors can also speed sampling (p. 262).

### 8.5 Summary (p. 263)
The chapter covered Metropolis, Gibbs and HMC, `map2stan`, and general advice on diagnosing poor fits through two pathological examples (p. 263).

### 8.6 Practice (pp. 263–265)
Easy, medium and hard exercises (listed below; no solutions printed).

## Toy example (ours, not from the text)
A 3-island ring with populations 1, 2, 3. The proposal picks each of the other two islands with probability 1/2. Move probability is $\min(1,\text{pop(proposal)}/\text{pop(current)})$. The target is $\pi=(1/6,\,2/6,\,3/6)$.

Transition probabilities:
- From island 1: to 2: $\tfrac12\cdot\min(1,2)=\tfrac12$. To 3: $\tfrac12\cdot\min(1,3)=\tfrac12$. Stay: 0.
- From island 2: to 1: $\tfrac12\cdot\tfrac12=\tfrac14$. To 3: $\tfrac12\cdot1=\tfrac12$. Stay: $1-\tfrac14-\tfrac12=\tfrac14$.
- From island 3: to 1: $\tfrac12\cdot\tfrac13=\tfrac16$. To 2: $\tfrac12\cdot\tfrac23=\tfrac13$. Stay: $1-\tfrac16-\tfrac13=\tfrac12$.

Check that $\pi$ is preserved. The long-run probability of island 1 after one step is
$$\pi_1\cdot0+\pi_2\cdot\tfrac14+\pi_3\cdot\tfrac16=\tfrac13\cdot\tfrac14+\tfrac12\cdot\tfrac16=\tfrac1{12}+\tfrac1{12}=\tfrac16=\pi_1 .$$
Check island 3: $\pi_1\cdot\tfrac12+\pi_2\cdot\tfrac12+\pi_3\cdot\tfrac12=\tfrac1{12}+\tfrac16+\tfrac14=\tfrac{1+2+3}{12}=\tfrac12=\pi_3$. ✓. Island 2 then follows because the probabilities sum to 1: $1-\tfrac16-\tfrac12=\tfrac13=\pi_2$. ✓

The chain moves only by ratios, never uses the total 6, and still keeps the target distribution.

## Concepts
- [[markov-chain-monte-carlo-mcmc]] — a random walk whose long-run visits follow the posterior, so its states are posterior samples (p. 241, 245)
- [[metropolis-hastings]] — propose a move; accept with probability from the target ratio. Plain Metropolis needs symmetric proposals; Hastings allows asymmetric ones (pp. 243–245)
- [[gibbs-sampling]] — Metropolis–Hastings variant with adaptive proposals; relies on conjugate pairs; inefficient with very many parameters (pp. 245–246)
- [[conjugate-prior]] — prior–likelihood pairs with an analytical single-parameter posterior; here, what Gibbs sampling needs (p. 245)
- [[hamiltonian-monte-carlo-hmc-nuts]] — simulates a frictionless particle on the log-posterior; needs continuous parameters and tuning (pp. 246–247)
- [[convergence-diagnostics-rhat-ess-divergences]] — here `n_eff` (effective sample count) and Rhat (Gelman–Rubin). Rhat may be seen "perhaps as a signal of danger, but never of safety" (pp. 250, 257)
- [[trace-plot]] (new) — samples plotted in sequence; first check of a chain (p. 253)
- [[stationarity-and-mixing]] (new) — stationary: stays within the posterior. Well mixing: successive samples not highly correlated (p. 253)
- [[warmup-vs-burn-in]] (new) — in Stan, warmup samples adapt the sampler and are not from the target distribution (p. 256)
- [[weakly-informative-prior]] (new) — prior that gives a gentle nudge away from absurd values; in the examples it cured wild chains, though the likelihood washed it out (pp. 259–260)
- [[non-identifiable-parameters]] (new) — parameters of which only the sum is identified (e.g., $\alpha_1+\alpha_2$) gave wandering chains in the example (pp. 260–261)
- [[cauchy-distribution]] (new) — thick-tailed density with location and scale, no mean or variance; used as half-Cauchy prior for $\sigma$ (p. 260)
- [[folk-theorem-of-statistical-computing]] (new) — trouble fitting a model often indicates a bad model (p. 262)
- [[prior-distribution]] — flat priors say all values are equally plausible and can break chains (p. 258)

## Canonical instances
- [[king-markov-islands]] — Metropolis algorithm as a fable; time on islands proportional to population (pp. 242–244)
- [[terrain-ruggedness-stan-fit]] — `map` and `map2stan` give similar estimates; posterior nearly Gaussian (pp. 248–252)
- [[wild-chain-two-observations]] — flat priors with $y=(-1,1)$ give a drifting chain; weak priors fix it (pp. 257–259)
- [[non-identifiable-sum-alpha1-alpha2]] — wandering chains, `n_eff`=1, Rhat 2.83; weak priors fix it (pp. 260–262)
- [[cauchy-running-mean]] — running mean of Cauchy draws never settles (p. 260)

## Bridges (candidates)
- [structural-analogy] King's accept/reject by ratio of populations ↔ bayesian: Metropolis acceptance depends only on a ratio of posterior densities, so no normalizing constant is needed.
- [structural-analogy] Non-identifiable $\alpha_1+\alpha_2$ ↔ regression with collinear predictors (Ch. 5): both give a ridge of equally good parameter combinations.
- [metaphor] HMC's frictionless particle on the log-posterior ↔ physics: motion on a potential surface.
- [structural-analogy] Heavy-tailed Cauchy draws that never stabilize a mean ↔ flat prior chains that wander to extreme values.

## Questions this raises
- Why does the ratio rule leave the target distribution unchanged (detailed balance), and how does that change when proposals are asymmetric?
- What exactly does `n_eff` measure, and how is it computed from autocorrelation?
- How weak is "weakly informative"? When would a prior this weak still change inferences?
- What does HMC do about its tuning parameters during warmup, and which models remain hard for any MCMC?

## Exercises worth doing
- Ex. 8E6 (p. 263) — sketch good versus bad trace plots; builds the diagnostic eye — difficulty: easy
- Ex. 8M1 (p. 263) — refit the ruggedness model with uniform and exponential priors for $\sigma$; do priors matter here? — difficulty: medium
- Ex. 8M3 (p. 263) — vary warmup and compare `n_eff` — difficulty: medium
- Ex. 8H1 (p. 264) — compare Gaussian and Cauchy parameters' trace plots — difficulty: medium
- Ex. 8H3 (p. 264) — how a prior on one correlated parameter changes both (leg-length example) — difficulty: hard
- Ex. 8H5 (p. 265) — modify the Metropolis code so population differs from island label — difficulty: medium

## Reading notes
- Printed page = pdf − 14. Pages 241–265 are chapter content; the text layer of pdf 280 (printed 266) is empty.
- The `str(post)` output (p. 250) prints parameter names `br` and `brA`, while the model uses `bR` and `bAR`. This appears to be a naming mismatch in the printout.
- The `n_eff` values in Fig. 8.4 (e.g., 267 for $a$, p. 254) differ from the `precis` values on p. 249 (291 for $a$). The pages do not explain why.
- Text calls intervals in the m8.2 output "confidence intervals" (p. 258), but the table columns are labelled lower 0.89 and upper 0.89 (HPDI as stated on p. 250).
- The Cauchy density and the model definitions are legible in the page images. No unreadable material.
