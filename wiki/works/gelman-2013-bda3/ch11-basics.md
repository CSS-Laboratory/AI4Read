---
id: gelman-2013-bda3/ch11-basics
work: gelman-2013-bda3
unit: "11 Basics of Markov chain simulation"
pages: 275-292
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Basics of Markov chain simulation

## L0 — One line
Markov chain simulation (Gibbs sampler, Metropolis-Hastings) draws from a posterior by building a chain whose stationary distribution (one that a chain step leaves unchanged) is that posterior, and the draws are only usable after convergence is checked with several dispersed, split sequences (R̂, a between-/within-sequence variance ratio, and effective sample size, the equivalent number of independent draws).

## L1 — The gist (≤ 120 words)
When we cannot sample the posterior p(θ|y) directly, we can build a Markov chain whose long-run (stationary) distribution is p(θ|y). The chapter presents two basic constructions, the Gibbs sampler and the Metropolis-Hastings algorithm, and shows how to combine them. Draws are correlated and early ones reflect the starting point, so the chapter gives a practical protocol. Run several sequences from widely spread (overdispersed) starts, discard the first half as warm-up, and split each chain in two. Compare between- and within-chain variance with R̂ (a convergence measure that declines to 1), and estimate the effective number of independent draws. A hierarchical normal example (coagulation data) shows both algorithms working.

**Prerequisites:** conditional and joint probability; normal and conjugate distributions; sample mean and variance; hierarchical normal model (Chapter 5); autocorrelation.

## L2 — Key ideas (5–10 bullets)
- MCMC draws sequentially, each draw depending on the previous one. What matters is that the draws' distribution converges to p(θ|y), not the Markov property itself (p. 275).
- The Gibbs sampler updates each block of θ from its full conditional distribution (its distribution given the latest values of all other blocks). It is the simplest algorithm and the author's first choice when the conditionals are conjugate (pp. 276–277, 280).
- The Metropolis algorithm proposes a jump from a symmetric distribution and accepts it with probability min(r,1), r being the density ratio. It works because the joint distribution of consecutive draws is symmetric (pp. 278–279).
- Metropolis-Hastings drops the symmetry requirement by using a ratio of ratios, which corrects for the asymmetry. Gibbs is the special case in which every jump is accepted (pp. 279–281).
- Inference has two extra difficulties: unconverged early draws and within-sequence correlation. The remedies are multiple overdispersed (more spread out than the target) sequences, warm-up discarding, and splitting chains (pp. 282–284).
- R̂ compares between- and within-sequence variance. It tests mixing and stationarity, and the author has generally been satisfied with a threshold of 1.1 (pp. 284–285, 287).
- Effective sample size n_eff = mn / (1 + 2Σρ_t), with autocorrelations estimated from a variogram (mean squared difference between draws t steps apart) and a truncated sum. The default rule is n_eff ≥ 5m (pp. 286–287).
- Passing these checks is not a hypothesis test. Unreached regions of the target can still be missed (p. 288).
- In the hierarchical normal example, 100 Gibbs iterations and 500 Metropolis iterations were sufficient for approximate convergence (pp. 289–290).

## L3 — Walkthrough

### Introduction (pp. 275–276)
- MCMC draws θ from approximate distributions and corrects them toward the target p(θ|y). Draws are sequential, so they form a Markov chain: the distribution of θ^t given all earlier values depends only on θ^{t−1} (p. 275).
- The author says the key is that the approximate distributions improve at each step (converge to the target). The Markov property is helpful in proving that convergence (p. 275).
- Several independent sequences are run. Each starts at some θ^0 and draws θ^t from a transition distribution $T_t(\theta^t|\theta^{t-1})$. The subscript t lets the transition depend on iteration number, which is convenient when mixing Gibbs and Metropolis steps (p. 275).
- The transitions must give a unique stationary distribution, meaning one that stays the same under further steps, and it must equal p(θ|y). The simulation must run long enough for the current draws to be close to it (pp. 275–276).
- Figure 11.1 shows a Metropolis run for target θ ~ N(0, I) in two dimensions. Five sequences start from overdispersed points (more spread out than the target). After 50 iterations they are far from convergence. After 1000 they are nearer. The second halves are used as correlated draws (p. 276). The jumping rule was chosen to be inefficient on purpose, so the random-walk behaviour is visible (p. 276).
- Checking convergence is "absolutely necessary" (p. 276). Section 11.4 covers checking, Section 11.5 effective sample size, and Section 11.6 a hierarchical normal example (p. 276).

*Intuition note.* The chain is a tool: its draws do not need to be independent (p. 282); what matters is that their distribution converges to the target. Until then, the draws may be unrepresentative of the target.

### 11.1 Gibbs sampler (pp. 276–278)
- Split θ into d components (subvectors), θ = (θ_1,…,θ_d). One iteration t has d steps, in a chosen order. Each θ_j^t is drawn from $p(\theta_j|\theta_{-j}^{t-1},y)$, where
$$\theta_{-j}^{t-1}=(\theta_1^t,\dots,\theta_{j-1}^t,\theta_{j+1}^{t-1},\dots,\theta_d^{t-1}).$$
Components already updated use iteration-t values and the others use iteration t−1 values (p. 277).
- For many standard models most conditionals can be sampled directly. They are often conjugate (p. 277).
- **Example: bivariate normal (pp. 277–278).** One observation (y_1,y_2) comes from a bivariate normal with unknown mean θ = (θ_1,θ_2) and known covariance $\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}$. With a uniform prior, $\theta|y\sim N\big((y_1,y_2)^T,\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\big)$ (p. 277). The conditionals, from multivariate normal properties, are
$$\theta_1|\theta_2,y\sim N\big(y_1+\rho(\theta_2-y_2),\,1-\rho^2\big),\qquad \theta_2|\theta_1,y\sim N\big(y_2+\rho(\theta_1-y_1),\,1-\rho^2\big).$$
The sampler alternates between them. Direct sampling is easy here, so this is for exposition only (p. 277). Figure 11.2 uses ρ = 0.8, data (0,0), and four sequences started at (±2.5, ±2.5). After 500 iterations they have approximately converged (pp. 277–278).

### 11.2 Metropolis and Metropolis-Hastings (pp. 278–280)
**Metropolis algorithm (p. 278).**
1. Draw a start θ^0 with p(θ^0|y) > 0 from a starting distribution p_0(θ), for example one dispersed around a crude estimate.
2. For t = 1, 2, …:
 (a) Sample a proposal θ* from the jumping distribution $J_t(\theta^*|\theta^{t-1})$. For Metropolis (but not Metropolis-Hastings) it must be symmetric: $J_t(\theta_a|\theta_b)=J_t(\theta_b|\theta_a)$ for all θ_a, θ_b, t.
 (b) Compute
$$r=\frac{p(\theta^*|y)}{p(\theta^{t-1}|y)}.\tag{11.1}$$
 (c) Set θ^t = θ* with probability min(r,1), otherwise θ^t = θ^{t−1}.
- The transition distribution is a mixture of a point mass at θ^{t−1} and a rescaled jumping distribution. A rejected jump still counts as an iteration (p. 278).
- **Example (p. 278).** Target p(θ|y) = N(θ|0, I), with I the 2×2 identity. Jumping distribution $J_t(\theta^*|\theta^{t-1})=N(\theta^*|\theta^{t-1},0.2^2 I)$, so r = N(θ*|0,I)/N(θ^{t−1}|0,I). This scale is purposely too small, giving the slow runs of Figure 11.1. Section 12.2 discusses choosing the scale (pp. 278–279).
- **Relation to optimization (p. 279).** A jump that raises the posterior density is accepted. A jump that lowers it is accepted with probability r. So Metropolis can be viewed as a stochastic version of a stepwise mode-finding algorithm: it always accepts steps that increase the density but only sometimes accepts downward steps.

*Intuition note.* The chain always accepts a proposal that raises the density and sometimes accepts one that lowers it, with probability equal to the density ratio. The proof below shows that this rule leaves the target distribution unchanged.

**Why Metropolis works (p. 279).** The proof has two steps.
1. The chain has a unique stationary distribution if it is irreducible, aperiodic and not transient. Except for trivial exceptions, the latter two hold for a random walk on any proper distribution. Irreducibility holds as long as the jumping distributions can eventually reach every state from every other with positive probability (p. 279).
2. The stationary distribution equals the target. Start with θ^{t−1} drawn from p(θ|y). Take two points θ_a, θ_b labeled so that p(θ_b|y) ≥ p(θ_a|y). The density of a transition a→b is
$$p(\theta^{t-1}=\theta_a,\theta^t=\theta_b)=p(\theta_a|y)J_t(\theta_b|\theta_a),$$
since acceptance probability is 1. The density of a transition b→a, using (11.1), is
$$p(\theta^t=\theta_a,\theta^{t-1}=\theta_b)=p(\theta_b|y)J_t(\theta_a|\theta_b)\frac{p(\theta_a|y)}{p(\theta_b|y)}=p(\theta_a|y)J_t(\theta_a|\theta_b).$$
These are equal because J_t is symmetric. The joint distribution of (θ^{t−1}, θ^t) is therefore symmetric, so θ^t and θ^{t−1} have the same marginal, and p(θ|y) is stationary (p. 279).

*Intuition note.* If the chain is already in the target, the flow of probability from a to b equals the flow from b to a. So a step changes nothing about the distribution.

**Metropolis-Hastings (pp. 279–280).** Two generalizations: J_t need not be symmetric, and r becomes a ratio of ratios,
$$r=\frac{p(\theta^*|y)/J_t(\theta^*|\theta^{t-1})}{p(\theta^{t-1}|y)/J_t(\theta^{t-1}|\theta^*)}.\tag{11.2}$$
- r is always defined, because a jump from θ^{t−1} to θ* can only occur if both p(θ^{t−1}|y) and J_t(θ*|θ^{t−1}) are nonzero (p. 280).
- Asymmetric rules can speed up the random walk. The proof of a unique stationary distribution is identical. For the target, label θ_a, θ_b so that $p(\theta_b|y)J_t(\theta_a|\theta_b)\ge p(\theta_a|y)J_t(\theta_b|\theta_a)$. The author states that, if θ^{t−1} follows the target, it is "easy to show" the a→b and b→a transition densities are equal. The text gives no further detail here; Exercise 11.1 (p. 291) asks for the proof.

**Jumping rule and efficiency (p. 280).** The ideal rule samples from the target, J(θ*|θ) ≡ p(θ*|y). Then r in (11.2) is exactly 1 and the iterates are independent draws. Iteration is used when this is impossible. A good jumping distribution has four properties:
- it is easy to sample from;
- r is easy to compute;
- each jump goes a reasonable distance, since otherwise the walk is too slow;
- jumps are not rejected too often, since otherwise time is wasted standing still.

### 11.3 Gibbs and Metropolis as building blocks (pp. 280–281)
- The Gibbs sampler is the simplest algorithm and the author's first choice for conditionally conjugate models, for example the normal-normal hierarchical models of Chapter 5 (p. 280).
- Metropolis suits models that are not conditionally conjugate, such as the two-parameter logistic regression of the bioassay example (Section 3.7). It can jump in the joint (α,β) space or run one-dimensional Metropolis updates inside a Gibbs structure. It will probably need tuning of the acceptance rate (p. 280).
- If some conditionals can be sampled directly and others cannot, the parameters can be updated one at a time. Use Gibbs where possible and one-dimensional Metropolis otherwise. More generally, update in blocks (p. 280).
- Conditional sampling can be slow when parameters are highly correlated in the target (Figure 11.2). In simple problems this can be fixed by reparameterization (Section 12.1); more generally, by the advanced algorithms of Chapter 12 (p. 280).

**Gibbs as a special case of Metropolis-Hastings (p. 281).** Let step j of iteration t update θ_j. The jumping distribution moves only along θ_j:
$$J^{\rm Gibbs}_{j,t}(\theta^*|\theta^{t-1})=\begin{cases}p(\theta_j^*|\theta_{-j}^{t-1},y)&\text{if }\theta^*_{-j}=\theta^{t-1}_{-j}\\0&\text{otherwise.}\end{cases}$$
Then (11.2) gives
$$r=\frac{p(\theta^*|y)/J^{\rm Gibbs}_{j,t}(\theta^*|\theta^{t-1})}{p(\theta^{t-1}|y)/J^{\rm Gibbs}_{j,t}(\theta^{t-1}|\theta^*)}=\frac{p(\theta^*|y)/p(\theta_j^*|\theta_{-j}^{t-1},y)}{p(\theta^{t-1}|y)/p(\theta_j^{t-1}|\theta_{-j}^{t-1},y)}=\frac{p(\theta_{-j}^{t-1}|y)}{p(\theta_{-j}^{t-1}|y)}\equiv1.$$
Every jump is accepted. The second line follows because θ* differs from θ^{t−1} only in component j. The third follows from conditional probability applied to θ = (θ_j, θ_{−j}) with θ*_{−j} = θ^{t−1}_{−j} (p. 281).
- An iteration usually includes all d steps. Gibbs can also be defined without updating every component each iteration, as long as each is updated periodically (p. 281).

**Gibbs sampler with approximations (p. 281).** If a conditional $p(\theta_j|\theta_{-j},y)$ cannot be sampled, use an approximation $g(\theta_j|\theta_{-j})$ that can. Take $J_{j,t}(\theta^*|\theta^{t-1})=g(\theta_j^*|\theta_{-j}^{t-1})$ if θ*_{−j} = θ^{t−1}_{−j}, and 0 otherwise. Compute r from (11.2) and accept or reject, which compensates for the approximation (p. 281).

### 11.4 Inference and assessing convergence (pp. 281–288)
- Inference is as in Bayesian simulation generally: use all draws to summarize the posterior. Posterior predictive draws ỹ come from simulating conditional on drawn θ (p. 281).

**Two difficulties (p. 282).**
1. Unconverged runs may be grossly unrepresentative. Even near convergence, early iterations still reflect the starting approximation (p. 282).
2. Within-sequence correlation makes inference from correlated draws generally less precise than from the same number of independent draws. Serial correlation is not itself a problem at convergence, since the draws are identically distributed as p(θ|y). It costs efficiency. In Figure 11.1c, the patchy scatter would not be likely from 2500 independent draws, so in some sense the effective number is far below 2500 (p. 282).
- Three remedies: simulate multiple sequences with dispersed starts. Compare between- and within-sequence variation until they are roughly equal. If efficiency is unacceptably low, change the algorithm (Sections 12.1–12.2) (p. 282).

**Warm-up (p. 282).** To reduce the influence of the start, discard the first half of each sequence. Other fractions can be appropriate, and in Figure 11.2 only a few initial iterations would need discarding. Example: run 200 iterations and discard 100. If convergence is not reached, run 200 more and discard all of the first 200. The older term "burn-in" is avoided because it suggests stress-testing products to reveal defects (p. 282, footnote 1).

**Thinning (pp. 282–283).** Keeping every kth draw is sometimes useful when storage is a problem with many parameters. The author has perhaps set k so that no more than 1000 iterations are saved. Converged sequences, thinned or not, can be used directly (p. 283).

**Multiple sequences, scalar estimands, mixing and stationarity (pp. 283–284).**
- Convergence is assessed by comparing sequences. In Figure 11.1a the within-sequence variance is much less than the between-sequence variance. In Figure 11.1b the two components are essentially equal (p. 283). So simulate at least two independent sequences from an overdispersed start (p. 283).
- Monitor each scalar estimand separately: parameters, ratios, a predicted future observation. Monitoring the log posterior density is often useful (p. 283).
- Figure 11.3a shows two sequences that each look stable but sit in different places. They have not **mixed**. Figure 11.3b shows two sequences that cover a common distribution but neither looks stationary (p. 284). Convergence needs both mixing and stationarity (p. 284).
- **Splitting.** After discarding warm-up, split each chain into its first and second half. If all half-sequences mix, this tests mixing and also stationarity, since at stationarity both halves traverse the same distribution. Let m = number of chains after splitting and n = length of each. At least two sequences are run, so m ≥ 4 (p. 284).
- Example: 5 chains of length 1000. Discard the first half, leaving 5 × 500. Split into iterations 1–250 and 251–500 (originally 501–750 and 751–1000). This gives m = 10, n = 250 (p. 284).

**Between- and within-sequence variance (p. 284).** For scalar ψ with simulations ψ_ij (i = 1,…,n; j = 1,…,m):
$$B=\frac{n}{m-1}\sum_{j=1}^m(\bar\psi_{.j}-\bar\psi_{..})^2,\quad \bar\psi_{.j}=\frac1n\sum_{i=1}^n\psi_{ij},\quad \bar\psi_{..}=\frac1m\sum_{j=1}^m\bar\psi_{.j},$$
$$W=\frac1m\sum_{j=1}^m s_j^2,\quad s_j^2=\frac1{n-1}\sum_{i=1}^n(\psi_{ij}-\bar\psi_{.j})^2.$$
B contains a factor n because it is based on the variance of the chain means, each an average of n values. The marginal posterior variance is estimated by
$$\widehat{\rm var}^+(\psi|y)=\frac{n-1}{n}W+\frac1nB.\tag{11.3}$$
- This overestimates var(ψ|y) if the starting distribution is appropriately overdispersed. It is unbiased under stationarity (start distribution equals target) or in the limit n → ∞ (Exercise 11.5). It is analogous to the classical variance estimate with cluster sampling (p. 284).
- For finite n, W should underestimate var(ψ|y), because chains have not had time to range over the whole target. As n → ∞, E(W) approaches var(ψ|y) (pp. 284–285).

**Potential scale reduction (p. 285).**
$$\widehat R=\sqrt{\frac{\widehat{\rm var}^+(\psi|y)}{W}},\tag{11.4}$$
which declines to 1 as n → ∞. It estimates the factor by which the scale of the current distribution of ψ might shrink if simulation continued to n → ∞. If it is high, further simulation may improve inference (p. 285). In the current edition R̂ is computed on split chains. Since the second edition the book had applied R̂ to unsplit chains, which would not correctly diagnose Figure 11.3b; the first edition also defined R̂ without the square root (footnote 2, p. 285).

*Intuition note.* If chains have all found the same distribution, between-chain and within-chain variation are roughly equal and R̂ is near 1. If chains are still far apart, between-chain variation is larger than within-chain variation, var⁺ exceeds W, and R̂ is above 1.

**Example continued (Table 11.1, p. 285).** Second halves of five Metropolis sequences, 95% central intervals and R̂.

| Iterations | θ₁ | θ₂ | log p(θ₁,θ₂|y) |
|---|---|---|---|
| 50 | [−2.14, 3.74], 12.3 | [−1.83, 2.70], 6.1 | [−8.71, −0.17], 6.1 |
| 500 | [−3.17, 1.74], 1.3 | [−2.17, 2.09], 1.7 | [−5.23, −0.07], 1.3 |
| 2000 | [−1.83, 2.24], 1.2 | [−1.74, 2.09], 1.03 | [−4.07, −0.03], 1.10 |
| 5000 | [−2.09, 1.98], 1.02 | [−1.90, 1.95], 1.03 | [−3.70, −0.03], 1.00 |
| ∞ | [−1.96, 1.96], 1 | [−1.96, 1.96], 1 | [−3.69, −0.03], 1 |

The author concludes the sequences converged adequately after 2000 or certainly 5000 iterations. Some variability remains even then. That must be so, because even independent draws would need hundreds or thousands to estimate extreme quantiles precisely (p. 285).

**Advantages and limits of R̂ (pp. 285–286).** It avoids examining time-series plots, which are notoriously unreliable and unwieldy for many quantities. Because it uses means and variances, it is most effective for approximately normal marginal posteriors. For extreme quantiles or multimodal marginals, also monitor extreme quantiles of the between and within sequences (p. 286).

### 11.5 Effective number of simulation draws (pp. 286–288)
- If draws within each sequence were independent, B would be an unbiased estimate of var(ψ|y) and there would be mn independent draws. With autocorrelation, B is larger than var(ψ|y) in expectation (p. 286).
- The author defines effective sample size through the efficiency of $\bar\psi_{..}$ as an estimate of E(ψ|y). This is a reasonable baseline but not the only one, and may be inappropriate if tail events matter (p. 286). The usual asymptotic formula is
$$\lim_{n\to\infty}mn\,{\rm var}(\bar\psi_{..})=\Big(1+2\sum_{t=1}^\infty\rho_t\Big){\rm var}(\psi|y),\tag{11.5}$$
with ρ_t the lag-t autocorrelation. For independent draws var(ψ̄..) = var(ψ|y)/(mn). Hence
$$n_{\rm eff}=\frac{mn}{1+2\sum_{t=1}^\infty\rho_t}.\tag{11.6}$$
The asymptotic nature should not be a problem, since we already want long enough runs for approximate convergence (p. 286).
- **Estimating ρ_t.** Use the total variance estimate var⁺ from (11.3), then the variogram at lag t,
$$V_t=\frac1{m(n-t)}\sum_{j=1}^m\sum_{i=t+1}^n(\psi_{i,j}-\psi_{i-t,j})^2.$$
Invert $E(\psi_i-\psi_{i-t})^2=2(1-\rho_t){\rm var}(\psi)$:
$$\hat\rho_t=1-\frac{V_t}{2\,\widehat{\rm var}^+}.\tag{11.7}$$
- The full sum cannot be used because sample correlations at large t are too noisy. Use a partial sum from lag 0, stopping when the sum of two successive autocorrelation estimates $\hat\rho_{2t'}+\hat\rho_{2t'+1}$ is negative (p. 286). This gives
$$\hat n_{\rm eff}=\frac{mn}{1+2\sum_{t=1}^T\hat\rho_t},\tag{11.8}$$
where T is the first odd positive integer for which $\hat\rho_{T+1}+\hat\rho_{T+2}$ is negative (p. 287).
- Use only saved iterations after warm-up. Example: 4 chains of length 1000 with half discarded gives m = 8, n = 250. Lags go up to 249 at most, though T will in practice be much lower (p. 287).

*Intuition note.* Strong positive autocorrelation makes the denominator large, so n_eff is much smaller than mn. Each draw then carries little new information.

**Bounded or long-tailed distributions (p. 287).** Diagnostics based on means and variances work less well when the posterior is far from Gaussian. Asymptotic normality does not help when we have small samples or little data per hierarchical parameter. Transform before computing R̂ and n_eff: logarithm for positive quantities, logit for quantities in (0,1), rank transformation for long tails (p. 287).

**Stopping (pp. 287–288).**
- Compute R̂ and n_eff for every scalar summary of interest. If R̂ is not near 1 for all of them, continue, perhaps altering the algorithm. "Near" depends on the problem. The author has generally been satisfied with a threshold of 1.1 (p. 287).
- For many purposes it should suffice to have 100 or even 10 independent draws (Section 10.5). With n_eff = 10, the simulation standard error is increased by $\sqrt{1+1/10}=1.05$. As a default, run until $\hat n_{\rm eff}\ge 5m$, that is, at least 10 independent draws per sequence, because m is twice the number of sequences. More precision may need a higher threshold (p. 287).
- When R̂ is near 1 and n_eff exceeds 10 per chain for all estimands, collect the mn draws as a sample from the target (p. 288).
- **Caveat.** Passing all tests does not guarantee convergence if important regions of the target were not captured by the starting distribution and are hard to reach. Declaring convergence means each sequence appears stationary and the sequences mixed well. These checks are not hypothesis tests: no p-value, no statistical significance. Discrepancy is judged by practical significance, for example R̂ > 1.1 (p. 288).

### 11.6 Example: hierarchical normal model (pp. 288–290)
- **Data (Table 11.2, p. 288).** Coagulation time (seconds) for 24 animals randomly allocated to four diets: A: 62, 60, 63, 59. B: 63, 67, 71, 64, 65, 66. C: 68, 66, 71, 67, 68, 68. D: 56, 62, 60, 61, 63, 64, 63, 59. The author uses the data only to illustrate computation, not for a full analysis.
- **Model (p. 288).** y_ij independent normal within J groups, with means θ_j and common variance σ². Total n = Σ n_j. Group means θ_j ~ N(μ, τ²). The prior is uniform on (μ, log σ, τ), with σ, τ > 0, equivalently p(μ, log σ, log τ) ∝ τ. A uniform prior on log τ would give an improper posterior (Chapter 5). The joint posterior is
$$p(\theta,\mu,\log\sigma,\log\tau|y)\propto\tau\prod_{j=1}^JN(\theta_j|\mu,\tau^2)\prod_{j=1}^J\prod_{i=1}^{n_j}N(y_{ij}|\theta_j,\sigma^2).$$
- **Starting points (p. 289).** For each θ_j, take a random data point from group j, giving 10 starting points. Start μ at the average of the starting θ_j. No starts are needed for τ or σ, since they are drawn in the first Gibbs steps. Section 13.6 gives a more elaborate start (p. 289).
- **Gibbs conditionals (pp. 289–290), all conjugate.**
 1. Each group mean :
$$\theta_j|\mu,\sigma,\tau,y\sim N(\hat\theta_j,V_{\theta_j}),\tag{11.9}$$
$$\hat\theta_j=\frac{\frac1{\tau^2}\mu+\frac{n_j}{\sigma^2}\bar y_{.j}}{\frac1{\tau^2}+\frac{n_j}{\sigma^2}},\tag{11.10}$$
$$V_{\theta_j}=\frac1{\frac1{\tau^2}+\frac{n_j}{\sigma^2}}.\tag{11.11}$$
 These are independent across j, so drawing one at a time equals drawing the vector at once (p. 289).
 2. $$\mu|\theta,\sigma,\tau,y\sim N(\hat\mu,\tau^2/J),\tag{11.12}$$ $$\hat\mu=\frac1J\sum_{j=1}^J\theta_j.\tag{11.13}$$
 3. $$\sigma^2|\theta,\mu,\tau,y\sim\text{Inv-}\chi^2(n,\hat\sigma^2),\tag{11.14}$$ $$\hat\sigma^2=\frac1n\sum_{j=1}^J\sum_{i=1}^{n_j}(y_{ij}-\theta_j)^2.\tag{11.15}$$
 4. $$\tau^2|\theta,\mu,\sigma,y\sim\text{Inv-}\chi^2(J-1,\hat\tau^2),\tag{11.16}$$ $$\hat\tau^2=\frac1{J-1}\sum_{j=1}^J(\theta_j-\mu)^2.\tag{11.17}$$
 It has J−1 degrees of freedom rather than J because p(τ) ∝ 1 rather than τ^{−1} (p. 290).
- **Gibbs results (Table 11.3, p. 290).** Ten sequences of length 100, second halves used. 100 iterations were sufficient for approximate convergence. R̂ for σ and τ is computed on the log scale.

| Estimand | 2.5% | 25% | median | 75% | 97.5% | R̂ |
|---|---|---|---|---|---|---|
| θ₁ | 58.9 | 60.6 | 61.3 | 62.1 | 63.5 | 1.01 |
| θ₂ | 63.9 | 65.3 | 65.9 | 66.6 | 67.7 | 1.01 |
| θ₃ | 66.0 | 67.1 | 67.8 | 68.5 | 69.5 | 1.01 |
| θ₄ | 59.5 | 60.6 | 61.1 | 61.7 | 62.8 | 1.01 |
| μ | 56.9 | 62.2 | 63.9 | 65.5 | 73.4 | 1.04 |
| σ | 1.8 | 2.2 | 2.4 | 2.6 | 3.3 | 1.00 |
| τ | 2.1 | 3.6 | 4.9 | 7.6 | 26.6 | 1.05 |
| log p(μ,log σ,log τ\|y) | −67.6 | −64.3 | −63.4 | −62.6 | −62.0 | 1.02 |
| log p(θ,μ,log σ,log τ\|y) | −70.6 | −66.5 | −65.1 | −64.0 | −62.4 | 1.01 |

 The author notes τ is estimated less precisely than σ, which is typical of hierarchical models with a small number of batches (p. 290).
- **Metropolis version (p. 290).** Rather than the full joint, the Metropolis algorithm is run on the marginal posterior of (μ, log σ, log τ). This uses conjugacy (Section 13.6) and gives a lower-dimensional space. Then θ is drawn from its normal conditional (11.9). The jumping kernel is multivariate normal, centred at the current value. Its variance matrix is that of a normal approximation (Section 13.6) multiplied by 2.4²/d, with d = 3 the dimension of the jumping distribution (p. 290).
- **Metropolis results (p. 290).** Ten parallel sequences. 500 iterations gave R̂ < 1.1 for all parameters and results similar to Gibbs. The acceptance rate was 0.35, close to the expected value for a normal target with d = 3 and scale 2.4/√d (Section 12.2) (p. 290).

### 11.7 Bibliographic note (p. 291)
A list of references with some historical credits. It says Metropolis and Ulam (1949) and Metropolis et al. (1953) apparently were the first to describe the Metropolis algorithm, and that Hastings (1970) generalized it. It says the Gibbs sampler was named by Geman and Geman (1984). The Metropolis-approximate Gibbs algorithm appears in Gelman (1992b). The convergence-monitoring method of Section 11.4 is reviewed in Gelman and Rubin (1992b) and Brooks and Gelman (1998), and the rule for summing autocorrelations comes from Geyer (1992) (p. 291).

## Toy example
*(Ours, not from the text.)*

**Part A: Metropolis on two states.** Target on states {a, b}: p(a) = 0.75, p(b) = 0.25. The proposal always proposes the other state, so it is symmetric.
- From a: r = p(b)/p(a) = 0.25/0.75 = 1/3. Move to b with probability 1/3, stay with probability 2/3.
- From b: r = 0.75/0.25 = 3, so min(r,1) = 1. Always move to a.
- Joint flow check, as in the proof on p. 279: p(a)·P(a→b) = 0.75 × 1/3 = 0.25, and p(b)·P(b→a) = 0.25 × 1 = 0.25. They are equal.
- Stationarity: new P(a) = 0.75 × 2/3 + 0.25 × 1 = 0.5 + 0.25 = 0.75. ✓.

**Part B: R̂ on tiny chains.** Illustrative only, since the book uses split chains with m ≥ 4 (p. 284). Take m = 2 chains, n = 3. Chain 1: 1, 2, 3. Chain 2: 3, 4, 5.
- Chain means: 2 and 4. Grand mean: 3.
- B = (3/(2−1)) × [(2−3)² + (4−3)²] = 3 × 2 = 6.
- s₁² = [(1−2)² + 0 + (3−2)²]/2 = 1. Likewise s₂² = 1. So W = 1.
- var⁺ = (2/3)(1) + (1/3)(6) = 2/3 + 2 = 8/3 ≈ 2.667.
- R̂ = √(2.667/1) ≈ 1.63. This is well above 1.1: the chains sit at different levels, so they have not mixed.

## Concepts
- [[mcmc]] — Markov chain Monte Carlo: sequential draws whose distribution converges to p(θ|y); the Markov property helps prove this but is not the key (pp. 275–276).
- [[gibbs-sampling]] — cycle through subvectors, drawing each from its full conditional given the latest values of the rest; a special case of MH with every jump accepted (pp. 276–277, 281).
- [[metropolis-hastings]] — propose from J_t, accept with min(r,1); r uses (11.1) for symmetric J and (11.2) otherwise (pp. 278–280).
- [[jumping-distribution]] (new) — the proposal distribution J_t(θ*|θ^{t−1}); good ones are easy to sample, move a reasonable distance and are not rejected too often (pp. 278, 280).
- [[stationary-distribution]] (new) — a distribution unchanged by a chain step; the posterior must be the unique one (pp. 275, 279).
- [[warm-up]] (new) — discarding early iterations that still reflect the start; default is the first half (p. 282).
- [[thinning]] (new) — keeping every kth draw, mainly to save storage (pp. 282–283).
- [[overdispersed-starting-points]] (new) — starts more dispersed than the target, so that non-convergence shows as between-sequence variance (pp. 276, 283).
- [[convergence-diagnostics]] — here R̂ computed from B and W on split chains, with threshold about 1.1 (pp. 284–285, 287).
- [[effective-sample-size]] (new) — n_eff = mn/(1 + 2Σρ_t), the equivalent number of independent draws for estimating the posterior mean (pp. 286–287).
- [[conjugate-prior]] — used here for conjugate conditionals that make Gibbs easy (pp. 277, 289).
- [[hierarchical-model]] — the hierarchical normal model with unknown σ² is the chapter's worked example (pp. 288–290).

## Canonical instances
- [[bivariate-normal-gibbs]] — Gibbs on N((y₁,y₂), [[1,ρ],[ρ,1]]), ρ = 0.8, shows slow correlated moves when parameters are highly correlated (pp. 277–278, 280).
- [[bivariate-unit-normal-metropolis]] — Metropolis with N(θ^{t−1}, 0.2²I) jumps, deliberately inefficient (pp. 276, 278–279).
- [[convergence-failure-figure-11-3]] — two failure modes: chains that do not mix, and chains that mix but are not stationary (pp. 283–284).
- [[coagulation-hierarchical-normal]] — four diets, 24 animals; Gibbs and Metropolis both reach approximate convergence with similar results (pp. 288–290).

## Bridges (candidates)
- [same-math] Gibbs step ↔ Metropolis-Hastings step: with proposal equal to the full conditional, r ≡ 1, as shown on p. 281.
- [structural-analogy] Metropolis acceptance rule ↔ stochastic mode-finding: always accept uphill moves, sometimes accept downhill (p. 279).
- [structural-analogy] var⁺ from B and W ↔ classical cluster-sampling variance estimate, as the author says (p. 284).
- [structural-analogy] n_eff for MCMC ↔ survey sampling: effective sample size under dependence, like cluster sampling (our link; the text compares only the var⁺ estimator to cluster sampling, p. 284).
- [metaphor] Ideal MH rule J ≡ p(θ*|y) ↔ independent sampling: the chain then reduces to i.i.d. draws (p. 280).

## Questions this raises
- If all chains start in one region and the algorithm cannot reach another mode, R̂ and n_eff may both look fine. How can this be detected (p. 288)?
- How should the jumping scale be tuned to trade off step size against rejection rate (Section 12.2, p. 279)?
- Why does the truncated autocorrelation sum, stopping when a pair of lags turns negative, give a usable estimate (pp. 286–287)?
- When do reparameterization or the algorithms of Chapter 12 fix slow mixing under strong posterior correlation (p. 280)?

## Exercises worth doing
- Ex. 11.1 (p. 291) — prove the MH stationary distribution is the target (the text only says this is 'easy to show') — difficulty: medium
- Ex. 11.2 (p. 291) — replicate the bioassay posterior with Metropolis, including start points and jumping rule — difficulty: medium
- Ex. 11.3 (p. 291) — separate, pooled and hierarchical Gibbs models on machine data — difficulty: hard
- Ex. 11.5 (p. 292) — prove var⁺ is unbiased under stationarity and independent chains — difficulty: medium
- Ex. 11.6 (p. 292) — derive (11.5), and plot n_eff against iterations in your own simulation — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 10 (pdf 285 = printed 275). Every page carries a printed number.
- The text layer renders θ as "ω" and the minus sign as "→" in superscripts such as t−1. The images show θ and "−".
- Equations (11.1)–(11.17) and Tables 11.1 and 11.3 were checked against the images. The text layer garbles the variance matrix and the n_eff sum, but the images are clear.
- The header on every page reads "This electronic edition is for non-commercial purposes only."
- Exercise 11.5 (p. 292) uses ψ and φ interchangeably for the scalar estimand. The main text also uses ψ in §11.4 (pp. 284–286) and φ on p. 287.
- Sections 11.7 (bibliographic note) and 11.8 (exercises) are summarized only briefly. Table 11.4 (machine data) is not reproduced.
