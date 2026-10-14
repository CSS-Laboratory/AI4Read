---
id: gelman-2013-bda3/appc-computation
work: gelman-2013-bda3
unit: Appendix C — Computation in R and Stan
pages: 591–608
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Computation in R and Stan: fitting the eight-schools model five ways

## L0 — One line
One small hierarchical model (eight schools) is fitted with Stan, with grid and conditional simulation, with Gibbs and Gibbs–Metropolis, and with hand-written Hamiltonian Monte Carlo (HMC), to show practical Bayesian computation, tuning and debugging.

## L1 — The gist (≤ 120 words)
Question: how do you actually compute a posterior for a hierarchical model? The authors fit the eight-schools normal model, and a t variant, in several ways. In Stan the user states the model (and supplies the data); the authors write it with school-level errors η because this makes the sampler more efficient. Direct R code can do grid-plus-conditional sampling or Gibbs; Metropolis steps handle the t degrees of freedom; HMC can be programmed by hand. The Metropolis and HMC runs are tuned using acceptance rates, and convergence is checked with R̂ (the potential scale reduction factor) and effective sample size (n_eff). The appendix ends with debugging advice: start simple, compare algorithms, and expect mistakes. This matters because the direct-programming methods are useful knowledge for more advanced models where Stan might not work.

**Prerequisites:** hierarchical normal model (Sec. 5.4–5.5); Gibbs and Metropolis sampling; R̂ and n_eff (Ch. 11); basic HMC and leapfrog steps (Ch. 12); reading R code.

## L2 — Key ideas (5–10 bullets)
- Stan code mirrors the book's model notation, but Stan's normal takes a standard deviation, not a variance. Vectorised code also runs faster (p. 592).
- Declaring θ as a transformation μ + τη of standardised errors η gives geometry that suits HMC better. This sort of hierarchical model shows better HMC convergence this way (pp. 592, 607).
- Stan output reports mean, se_mean, sd, quantiles, n_eff and R̂. Two runs gave similar but not identical results, so tail quantiles carry visible simulation noise (pp. 593–594).
- Saved draws in R support posterior and predictive checks, such as posterior probabilities, replicated data, and a best-minus-second-best test statistic (p. 595).
- Without Stan, one can draw τ from a grid approximation to its marginal posterior, then draw μ and θ from their normal conditionals (p. 597). A Gibbs sampler is simpler still (p. 598).
- Parameter expansion, and a Metropolis step for ν, extend the Gibbs code to the t model. Jump scale is tuned toward ≈44% acceptance for one parameter (pp. 599–603).
- Hand-written HMC needs the log density, its gradient, a mass vector, and tuned step size and step count. It was costly here, but HMC can work in complicated problems where Gibbs and Metropolis fail (pp. 603–607).
- Debugging means comparing programs and simpler models. Errors found included variance-for-sd mix-ups, ν versus 1/ν, and a poor prior (pp. 607–608).

## L3 — Walkthrough

### Introduction and C.1 Getting started (pp. 591)
- The appendix fits one example, the eight-schools model of Sec. 5.5 (p. 591).
- Sec. C.2 uses Stan called from R. Secs. C.3–C.4 program the model directly in R. This is "unnecessary for the Stan user" but useful for models where Stan might not work (p. 591).
- R is programmable and can also link Fortran or C code. Stan is a high-level language: the user states the model and a Markov chain simulation is run automatically (p. 591).
- In practice data are processed before and inferences after the fit, so Stan is run from R with `stan()` (p. 591).

### C.2 Fitting a hierarchical model in Stan (pp. 592–596)

**Stan program (p. 592).** Blocks:
- `data`: `J` (integer ≥ 0), `y[J]`, `sigma[J]` (> 0).
- `parameters`: `mu`, `tau` (> 0), vector `eta` of length J.
- `transformed parameters`: `theta`.
- `model`: the two statements below.

$$\theta_j=\mu+\tau\,\eta_j,\qquad \eta_j\sim \mathrm{N}(0,1),\qquad y_j\sim \mathrm{N}(\theta_j,\sigma_j^2).$$

- θ is a transformation of μ, τ, η, not a declared parameter. The text says this makes the sampler more efficient and the geometry better behaved for HMC (p. 592).
- Warning: the book's N(·,·) has a variance as second argument; Stan uses the standard deviation (p. 592).
- Vector notation is cleaner and faster because of more efficient autodifferentiation. A loop `for (j in 1:J) y[j] ~ normal(theta[j], sigma[j])` would also work (p. 592).

*Intuition note.* Instead of sampling θ directly, the sampler works with η. The η's are a priori independent N(0,1), whatever τ is. That removes the tight funnel-like link between τ and θ. (The unit says only "better behaved geometry"; the funnel picture is ours.)

**R script (p. 593).**
- Data file `schools.csv` has the eight rows (school, estimate, sd): A 28/15, B 8/10, C −3/16, D 7/11, E −1/9, F 1/11, G 18/10, H 12/18.
- Read with `read.csv`; set `J`, `y`, `sigma`; `library("rstan")`.
- Run `stan(file="schools.stan", data=c("J","y","sigma"), iter=1000, chains=4)`, then `print` and `plot`.
- Here R̂ is below 1.1 for all displayed quantities (p. 593).

**Reading the output (Fig. C.1, p. 594).**
- 4 chains, 1000 iterations, warmup 500, so 2000 post-warmup draws.
- `mean`: posterior mean from the draws.
- `se_mean`: Monte Carlo standard error of that mean. As draws grow, it goes to 0 while `sd` goes to the posterior sd.
- Then quantiles, $n_{\rm eff}$ (formula 11.8) and $\widehat R$ (formula 11.4).
- The last line, `lp__`, is the unnormalised log posterior density.
- Selected rows: μ mean 7.4, sd 4.8, n_eff 534; τ mean 6.9, sd 6.1, n_eff 138; θ[1] mean 12.1, sd 11.1, n_eff 72.

**Run-to-run variation (pp. 593–594).**

| Run | θ₁ mean | se_mean | sd | n_eff | 95% interval |
|---|---|---|---|---|---|
| First | 12.1 | 1.3 | 11.1 | 72 | [−3.0, 40.1] |
| Second | 11.4 | 0.3 | 8.2 | 830 | [−1.9, 31.5] |

- Posterior sd is "about 10". The means differ little relative to that (p. 593).
- Tail quantiles retain a fair amount of simulation variability even after approximate convergence. How much this matters depends on the use (pp. 593–594).
- $n_{\rm eff}$ is itself a random variable estimated from draws. The run with higher $n_{\rm eff}$ has lower se_mean and more stable estimates (p. 594).
- The 95% interval is not in the default print. Get it with `print(schools_fit,"theta[1]",probs=c(.025,.975))` (p. 593).

**Accessing draws (p. 595).** `extract()` returns a list: θ (matrix of draws × 8), η (same), vectors for μ and τ, and `lp__`. The text states 20,000 draws, which does not match Fig. C.1 (see Reading notes).
- `hist(schools_sim$tau)` displays the posterior draws of τ as a histogram (p. 595).
- `mean(schools_sim$theta[,1] > schools_sim$theta[,3])` estimates Pr(effect in school A > school C | y) (p. 595).

**Posterior predictive checks (pp. 595–596).**
- *Replicates in the existing schools:* for each draw s, $y^{\rm rep}_{s}\sim \mathrm{N}(\theta_s,\sigma^2)$, using `rnorm(J, theta[s,], sigma)`.
- Graphical check: the observed data's histogram next to 19 replicate histograms, as in Fig. 6.2. In this example they "look similar to the data" (p. 595).
- Test statistic $T(y)$ = best minus second-best of the 8 estimates. Compute $T(y^{\rm rep}_s)$ for all s and report $\Pr(T(y^{\rm rep})>T(y))$ plus a histogram (pp. 595–596).
- *Replicates in new schools* (Sec. 6.5): draw $\theta^{\rm rep}_j\sim \mathrm{N}(\mu_s,\tau_s^2)$, then $y^{\rm rep}_j\sim \mathrm{N}(\theta^{\rm rep}_j,\sigma_j^2)$. This needs an assumption about the $\sigma_j^2$. For illustration they are repeated from the original schools (p. 596).

**Alternative priors (p. 596).**
- The model as written has nearly uniform priors on the hyperparameters μ and τ.
- Adding `tau ~ cauchy(0,25);` gives a half-Cauchy prior on τ.
- Result: posterior mean and median of τ are lower, and shrinkage of the θ_j is greater than under the uniform prior.
- Reason: the prior density is decreasing in τ over the range where the posterior is substantial (Fig. 5.9). That shortens the posterior tail (p. 596).

**t model (p. 596).** Replace `eta ~ normal(0,1)` with `eta ~ student_t(nu,0,1)`. Declare `real<lower=1> nu;` and give it a prior (Sec. 17.4).

### C.3 Direct simulation, Gibbs, and Metropolis in R (pp. 596–603)
This section returns to the notation of Ch. 5 (p. 596).

**Marginal and conditional simulation (p. 597).**
- Grid for τ: 2000 equally spaced points from 0.01 to 40, used as a discrete approximation to $p(\tau\mid y)$ (eq. 5.21).
- With μ̂(τ) and $V_\mu(\tau)$ from (5.20), the code computes, per grid point:

$$\hat\mu(\tau)=\frac{\sum_j y_j/(\sigma_j^2+\tau^2)}{\sum_j 1/(\sigma_j^2+\tau^2)},\qquad V_\mu(\tau)=\frac{1}{\sum_j 1/(\sigma_j^2+\tau^2)},$$

$$\log p(\tau\mid y)=\tfrac12\log V_\mu-\tfrac12\sum_j\log(\sigma_j^2+\tau^2)-\tfrac12\sum_j\frac{(y_j-\hat\mu)^2}{\sigma_j^2+\tau^2}\quad\text{(up to a constant; as coded)}.$$

- Work on the log scale and subtract the maximum before exponentiating. This avoids overflow or underflow from multiplying many factors. Then normalise to sum 1 (p. 597).
- Draw 1000 values of τ from the grid with `sample(..., prob=p_tau)`. For each, draw μ from $\mathrm N(\hat\mu(\tau),V_\mu(\tau))$ and each θ_j from its normal conditional (as in Sec. 5.4):

$$\theta_j\sim \mathrm N\!\left(\frac{\mu/\tau^2+y_j/\sigma_j^2}{1/\tau^2+1/\sigma_j^2},\ \frac{1}{1/\tau^2+1/\sigma_j^2}\right)\quad\text{(as coded, p. 597)}.$$

- Result: 1000 draws from the joint posterior of (τ, μ, θ). Predictive draws are made as in the Stan section (p. 597).

*Intuition note.* Because τ is one-dimensional, a fine grid can serve as a discrete approximation to its marginal posterior (p. 597). Given τ, everything else is normal and can be drawn exactly, so the draws are independent, with no Markov chain.

**Gibbs sampler (pp. 597–598).** Follows Sec. 11.6 with known $\sigma_j^2$. The three updates, as coded:

$$\theta_j\mid\mu,\tau\sim\mathrm N\!\left(\frac{\mu/\tau^2+y_j/\sigma_j^2}{1/\tau^2+1/\sigma_j^2},\ \frac{1}{1/\tau^2+1/\sigma_j^2}\right),\quad \mu\mid\theta,\tau\sim\mathrm N(\bar\theta,\ \tau^2/J),\quad \tau^2=\frac{\sum_j(\theta_j-\mu)^2}{X},\ X\sim\chi^2_{J-1}.$$

- Run 5 chains of length 1000. Initialise overdispersed: μ ~ N(mean y, sd y), τ ~ Uniform(0, sd y). Store in `sims` of shape iter × chains × (J+2) = 1000 × 5 × 10 (p. 598).
- `monitor(sims)` (from rstan) returns R̂, $n_{\rm eff}$ and summaries from the last half of each chain (p. 598).

**Parameter-expanded Gibbs (pp. 598–599).** Writes θ_j = μ + α γ_j, with updates for γ, α, μ and τ² = Σγ_j²/χ²_{J−1}.
- Conditionals, as coded: $\gamma_j$ has mean $\frac{\alpha(y_j-\mu)/\sigma_j^2}{1/\tau^2+\alpha^2/\sigma_j^2}$ and variance $\frac{1}{1/\tau^2+\alpha^2/\sigma_j^2}$.
- α has mean $\hat\alpha=\sum\gamma_j(y_j-\mu)/\sigma_j^2\big/\sum\gamma_j^2/\sigma_j^2$ and variance $1/\sum\gamma_j^2/\sigma_j^2$.
- μ has mean $\sum (y_j-\alpha\gamma_j)/\sigma_j^2\big/\sum 1/\sigma_j^2$ and variance $1/\sum 1/\sigma_j^2$.
- Start α = 1. Save $\theta=\mu+\alpha\gamma$ and the original-scale $\tau_\theta=|\alpha|\tau$ (p. 599).

**Gibbs for the t model, fixed ν (pp. 599–600).** Each θ_j has its own variance $V_j\sim\text{Inv-}\chi^2(\nu,\tau^2)$ (Ch. 17), with a uniform prior on (μ, τ). Updates, as coded:
- θ_j: as above, with $V_j$ replacing $\tau^2$.
- μ: mean $\sum\theta_j/V_j\big/\sum1/V_j$, variance $1/\sum 1/V_j$.
- τ: $\tau=\sqrt{G}$, where $G\sim\text{Gamma}\big(J\nu/2+1,\ \text{rate }(\nu/2)\sum1/V_j\big)$.
- $V_j=\dfrac{\nu\tau^2+(\theta_j-\mu)^2}{X_j}$, $X_j\sim\chi^2_{\nu+1}$ (pp. 599–600).
- Fix ν = 4 "to provide a robust analysis" (p. 600). Initialise $V_j\sim U(0,\mathrm{sd}(y))^2$.

**Gibbs–Metropolis, ν unknown (pp. 600–601).**
- Prior: uniform on (μ, τ, 1/ν). Update 1/ν by a Metropolis step given all other parameters, on the log scale (Sec. 10.7).
- Only the last term of the log posterior involves ν, but the full density is coded for generality:

$$\log p=\sum_j\log\mathrm N(y_j\mid\theta_j,\sigma_j^2)+\sum_j\log\mathrm N(\theta_j\mid\mu,V_j)+\sum_j\Big[\tfrac{\nu}{2}\log\tfrac{\nu}{2}+\nu\log\tau-\log\Gamma(\tfrac{\nu}{2})-(\tfrac{\nu}{2}+1)\log V_j-\tfrac{\nu\tau^2}{2V_j}\Big].$$

- Jumping distribution: $1/\nu^*\sim\mathrm N(1/\nu,\ \texttt{sigma\_jump\_nu}^2)$. If $1/\nu^*\notin(0,1]$, the jump probability is set to 0 so it is rejected. Otherwise $r=\exp(\log p^*-\log p_{\rm old})$, accept if $U<r$, and $p_{\rm jump}=\min(r,1)$ (pp. 600–601).
- Tuning: Ch. 11 suggests an optimal acceptance rate of about 44% for a single parameter. A pilot run with `sigma_jump_nu = 1` gave about 0.4 (p. 601).

**Parameter expansion for the t model (pp. 601–603).**
- Same γ, α, μ updates as in the normal case, but with $V_j$. Then:
  - τ is updated as in the fixed-ν t model;
  - $V_j=(\nu\tau^2+\gamma_j^2)/X_j$ with $X_j\sim\chi^2_{\nu+1}$;
  - the Metropolis step evaluates `log_post` in the original parameterisation, with $(\mu+\alpha\gamma,\ \alpha^2V,\ \mu,\ |\alpha|\tau)$ (p. 602).
- Extra initialisation: γ ~ N(0,1) (J values), α ~ N(0,1). Save $(\mu+\alpha\gamma,\mu,|\alpha|\tau,\nu)$ (p. 602).
- Acceptance versus jump scale (p. 603):

| sigma_jump_nu | 1 | 0.5 | 0.3 |
|---|---|---|---|
| average acceptance | 17% | 32% | 46% |

  - 17% is below the one-dimensional optimum of 44%, so a smaller jump scale is expected to help (Sec. 12.2).
  - At 0.3 the draws of ν are less correlated and more accurate.
  - Going lower would make acceptance too high and reduce efficiency (p. 603).

*Intuition note.* A jump scale that is too large gets many rejections and too small gets many tiny accepted moves. Both give strongly correlated draws. The middle, near 44% for one parameter, is the compromise.

### C.4 Programming Hamiltonian Monte Carlo in R (pp. 603–607)
For eight schools, HMC is "overkill", but the code is offered as a template (p. 603).

**Setup (p. 603).** Parameter vector $\theta_{\rm vec}=(\theta_1,\dots,\theta_8,\mu,\tau)$, dimension d = 10.
- Log posterior: flat hyperprior (a constant), plus $\sum_j\log\mathrm N(\theta_j\mid\mu,\tau)$, plus $\sum_j\log\mathrm N(y_j\mid\theta_j,\sigma_j)$. It returns −∞ if τ is NaN or ≤ 0, so the density is zero there.

**Gradient (p. 604).** As coded:

$$\frac{\partial}{\partial\theta_j}=-\frac{\theta_j-y_j}{\sigma_j^2}-\frac{\theta_j-\mu}{\tau^2},\qquad \frac{\partial}{\partial\mu}=-\frac{\sum_j(\mu-\theta_j)}{\tau^2},\qquad \frac{\partial}{\partial\tau}=-\frac{J}{\tau}+\frac{\sum_j(\mu-\theta_j)^2}{\tau^3}.$$

- For τ ≤ 0 the gradient is set to zero.
- A numerical gradient (the text says 'first differences'; the code uses ±0.0001 around each coordinate) is also written for debugging (p. 604).

**One HMC iteration (p. 604).** Inputs: θ, y, σ, step size ε, number of leapfrog steps L, and a diagonal mass vector M (so $M^{-1}=1/M$). Steps as coded:
1. Draw momentum $\phi_k\sim\mathrm N(0,M_k)$.
2. $\log p_{\rm old}=\log p(\theta)-\tfrac12\sum_k\phi_k^2/M_k$.
3. Half step: $\phi\leftarrow\phi+\tfrac12\epsilon\,\nabla\log p(\theta)$.
4. For $l=1,\dots,L$: $\theta\leftarrow\theta+\epsilon M^{-1}\phi$, then $\phi\leftarrow\phi+c_l\,\epsilon\,\nabla\log p(\theta)$, with $c_l=1$ except $c_L=\tfrac12$.
5. Negate φ. Compute $\log p^*$ as in step 2 at the new point. $r=\exp(\log p^*-\log p_{\rm old})$, with r = 0 if NaN. Accept with probability $\min(r,1)$; otherwise keep the old θ (p. 604).

**Wrapper `hmc_run` (p. 605).**
- Inputs: an m × d matrix of starting values, the number of iterations, base step size ε₀, base steps L₀, and M.
- Chains run one at a time. At each iteration $\epsilon\sim U(0,2\epsilon_0)$ and $L=\lceil 2L_0U\rceil$. The authors randomise "to mix up the algorithm" and let it explore differently curved areas.
- Inference uses the last half of each chain (warmup = half). Acceptance probabilities are returned (p. 605).

**Tuning and use (pp. 605–607).**
- Mass vector: `rep(1/15^2, d)`, a diagonal matrix on the rough scale of the posterior inverse variance. The scale 15 is crude, from Table 5.2.
- Starts: N(0, 15) for each parameter, but τ ~ U(0, 15) (positive) (p. 605).
- 20 iterations with ε₀ = 0.1, L₀ = 10 to check the code runs (p. 606).

| Run | ε₀ | L₀ | Iterations | Avg acceptance by chain | Remarks |
|---|---|---|---|---|---|
| M2 | 0.1 | 10 | 100 | 0.27, 0.42, 0.59, 0.68 | τ: R̂ 1.5, n_eff 6; θ₁: R̂ 1.4 |
| M3 | 0.05 | 20 | 100 | 0.81, 0.75, 0.59, 0.82 | "looks better"; τ: R̂ 1.3, n_eff 11 |
| final | not stated | not stated | 10,000 (warmup 5000) | 0.57, 0.62, 0.62, 0.66 | R̂ ≈ 1 |

- The acceptance rates in M2 "seem low" against a goal of about 65%, so ε₀ was lowered and L₀ raised (p. 606).
- Final run results (p. 607): θ₁ mean 11.5, sd 8.5, n_eff 1129; μ mean 8.0, sd 5.4; τ mean 6.9, sd 5.5, n_eff 565.
- Verdict: for this small model, HMC cost more programming effort and computation time than Gibbs. HMC can work in complicated problems where Gibbs and Metropolis fail, which is why Stan implements it (via the no-U-turn sampler). Parameterising by η converges better for HMC (p. 607).

*Intuition note.* HMC proposes far-away moves by "rolling" with a momentum, using the gradient. With tuned ε and L it accepts them often. In the text, halving ε and doubling L raised acceptance (p. 606). The rolling picture, and the remark that too-large steps lower acceptance, are our general background.

### C.5 Further comments on computation (pp. 607–608)
- Follow Sec. 10.7: start with simple models, compare with earlier inferences as complexity grows, and (when it applies) start with smaller datasets (p. 607).
- Efficiency ideas: store the log density in `nu_update()` instead of computing it twice; use a more structured style (e.g. parameters and data in lists). The authors' approach: begin with transparent, possibly inefficient code, then reprogram once it works (p. 607).
- Debugging methods: run scripts one line at a time by cut and paste; insert print statements; compare Stan against R and each model against simpler fitted models (p. 607).
- Errors found:
  - variances used as standard deviations (`rnorm(1,alpha_hat,V_alpha)` instead of `sqrt(V_alpha)`);
  - confusing ν and 1/ν;
  - a missing term in the log posterior;
  - a miscalculated Metropolis condition;
  - saving the wrong output in `sims` (pp. 607–608).
- More serious errors: a poor prior choice, caught by comparing with another algorithm. A reparameterised model was also wrongly programmed, caught because its inferences "differed dramatically" from the simpler parameterisation (p. 608).
- Conclusion: Bayesian computation is not always easy even for relatively simple models. Once debugged, a model can be applied and generalised to a range of problems. The debugging steps often parallel the steps for building confidence in the model (p. 608).

### C.6 Bibliographic note (p. 608)
Cites R Project (2002), Becker et al. (1988) for S, and Fox (2002) and Venables and Ripley (2002) for R texts. Stan is cited as Stan Development Team (2012).

## Toy example (ours, not from the text)
One HMC iteration, following `hmc_iteration` exactly, on a one-dimensional target $\log p(\theta)=-\theta^2/2$ with gradient $-\theta$. Take M = 1, ε = 0.5, L = 1, current θ = 1, drawn momentum φ = 1.
1. $\log p_{\rm old}=-\tfrac12(1)^2-\tfrac12(1)^2=-1$.
2. Half step: φ = 1 + 0.5·0.5·(−1) = 0.75.
3. Loop (l = 1 = L): θ = 1 + 0.5·1·0.75 = 1.375. Then φ = 0.75 + 0.5·0.5·(−1.375) = 0.75 − 0.34375 = 0.40625.
4. Negate: φ = −0.40625.
5. $\log p^*=-\tfrac12(1.375)^2-\tfrac12(0.40625)^2=-0.9453125-0.0825195=-1.0278320$.
6. $r=\exp(-1.0278320+1)=\exp(-0.027832)\approx0.9726$. Accept with probability ≈ 0.97.

The energy changes only slightly (about 0.028), so the move is almost always accepted. A much larger ε would change the energy more and be accepted less often.

Non-centred check: μ = 8, τ = 2, η = 0.5 gives θ = 8 + 2·0.5 = 9.

## Concepts
- [[hamiltonian-monte-carlo]] — MCMC with gradient-based leapfrog trajectories; coded by hand in C.4 and used in Stan via NUTS (pp. 603–607)
- [[gibbs-sampling]] — cycle through exact conditionals θ | μ,τ; μ | θ,τ; τ | θ,μ (p. 598)
- [[metropolis-hastings]] — Metropolis step for 1/ν with a normal jump; about 44% acceptance is optimal for one parameter (pp. 600–601)
- [[convergence-diagnostics]] — R̂ (below 1.1 in the Stan example, where the chains appeared well mixed) and n_eff, via `print` or `monitor` (pp. 593–594, 598)
- [[posterior-predictive-check]] — replicated data in the same or new schools; test statistic = best minus second-best estimate (pp. 595–596)
- [[hierarchical-model]] — school effects θ_j drawn from N(μ, τ²), with a normal likelihood having known σ_j (pp. 592, 597)
- [[partial-pooling]] — a half-Cauchy prior on τ gives a lower posterior mean and median of τ and greater shrinkage of θ_j than the near-uniform prior (p. 596)
- [[non-centered-parameterization]] (new) — θ = μ + τη with η ~ N(0,1); this is "better behaved" for HMC (pp. 592, 607)
- [[parameter-expansion]] (new) — extra parameters α, γ with θ = μ + αγ, τ_θ = |α|τ, used for the normal model (pp. 598–599) and, for the t model, to make the computations more efficient (pp. 601–602)
- [[grid-approximation]] (new) — discretise τ, normalise on the log scale, and sample from the grid (p. 597)
- [[leapfrog-mass-vector]] (new) — step size ε, step count L and diagonal mass M as the HMC tuning knobs; ε and L randomised per iteration (pp. 604–605)
- [[effective-sample-size]] (new) — n_eff: crude measure of effective sample size; itself a random variable (pp. 594, 598)

## Canonical instances
- [[eight-schools]] — hierarchical normal model of eight coaching effects, fitted in C.2–C.4 and revisited in C.5 (pp. 591–608)
- [[student-t-hierarchical-model]] — t extension with fixed ν = 4, or ν unknown via Metropolis (pp. 596, 599–603)

## Bridges (candidates)
- [structural-analogy] non-centred θ = μ + τη ↔ Variational inference: reparameterising a random variable as a deterministic transform of a fixed-distribution noise variable — similar form, different purpose.
- [structural-analogy] Metropolis jump-scale tuning to ≈44% ↔ Optimisation: step-size tuning, where steps too large or too small both slow progress.
- [same-math] Gibbs and Metropolis acceptance logic here ↔ Markov chain Monte Carlo (canon): the same algorithms, in code form.
- [metaphor] Debugging by comparing against simpler fitted models ↔ Bayesian workflow: build up complexity and check each stage.

## Questions this raises
- Why does the η-parameterisation help HMC (and how does it depend on how informative the data are about each θ_j)?
- How should one pick the tuning targets: 44% for single-parameter Metropolis versus about 65% for HMC (pp. 601, 606)?
- How many effective draws are enough? Tail intervals varied between two Stan runs (p. 593).
- How would results change under other priors on τ or other t degrees of freedom?

## Reading notes
- Printed page = pdf − 10 (pdf 601 = p. 591). Only printed numbers are cited.
- The text layer shows θ as "ω" in several places.
- p. 595 says 20,000 draws, "four elements" for "five quantities", and uses `schools_fit1`. Fig. C.1 (p. 594) states 2000 post-warmup draws and the code objects are named `schools_fit`. These look inconsistent in the source.
- p. 602 cross-reference reads "bottom part of page 601 and the top of page 601".
- p. 603: for τ ≤ 0 the gradient returns `c(0,0,0)` (length 3), as printed.
- The printed R code for `nu_update` (p. 601) ends with `return(nu=nu, p_jump=p_jump)`. The code on pp. 592–605 is described rather than copied in full.
- p. 593 contains the typo "simular". The Figure C.1 timestamp is Apr 24, 2013.
- The posterior-draw counts in M2/M3 are from 100-iteration runs with small n_eff (6–110 in the displayed tables), so those summaries should be read cautiously; the authors say only that the 1000- and 10,000-iteration runs are "stable".
- No exercises appear in this unit.
