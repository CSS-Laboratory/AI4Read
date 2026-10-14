---
id: sarkka-2023-bayesianfiltering/ch11-particle
work: sarkka-2023-bayesianfiltering
unit: "11 Particle Filtering"
pages: 229–252
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
# Particle Filtering

## L0 — One line
A particle filter approximates the Bayesian filtering distribution by weighted random samples that are propagated, reweighted by the new measurement, and resampled when the weights degenerate.

## L1 — The gist (≤ 120 words)
Gaussian approximations can be inappropriate when the filtering distribution is multi-modal, partly discrete or contaminated by outliers. This chapter builds Monte Carlo filters for such cases. Importance sampling corrects samples from an easy distribution with weights. Doing this sequentially gives sequential importance sampling (SIS). Resampling counters weight degeneracy and gives the particle filter (sequential importance resampling, SIR). Its easiest-to-implement form is the bootstrap filter. The auxiliary filter uses the new measurement when choosing which particles to propagate. The Rao–Blackwellized filter samples only the latent part of a conditionally linear Gaussian model and runs Kalman filters on the rest. A pendulum example with 50% clutter (outlier) measurements shows the gain over a Gaussian filter.

**Prerequisites:** Bayesian filtering equations; Gaussian densities; Kalman filter prediction/update; expectations and unbiased estimators; Dirac delta.

## L2 — Key ideas (5–10 bullets)
- Posterior expectations $E[g(x)\mid y_{1:T}]$ are estimated by sample averages. The Monte Carlo error is $O(N^{-1/2})$ regardless of dimension; the resulting advantage in high dimension holds at least in theory, not necessarily in practice (p. 230).
- Importance sampling draws from an easy distribution $\pi$ and fixes the mismatch with weights. Self-normalized weights need the posterior only up to its normalization constant (pp. 231–233).
- SIS updates weights recursively, $w_k\propto w_{k-1}\,p(y_k\mid x_k)p(x_k\mid x_{k-1})/\pi(\cdot)$. In SIS the weights can easily degenerate: almost all particles may end up with near-zero weight (pp. 235–236).
- Resampling is unbiased and removes low-weight particles, but adds variance. Multinomial resampling has high variance; stratified resampling is guaranteed lower variance, and systematic resampling is recommended in practice though its theory is less clear (pp. 237–239).
- SIR is the particle filter. It resamples adaptively when the effective number of particles $n_{\text{eff}}$ is low. The bootstrap filter uses the dynamic model as importance distribution (pp. 239–242).
- Low process noise causes sample impoverishment (many particles become identical copies). Pure recursive estimation is therefore hard for basic particle filters (p. 242).
- Bootstrap PF reaches about the same error as the best Gaussian filters on the plain pendulum (RMSE, root-mean-square error, 0.10). With 50% clutter it gets 0.20 against 0.89 for a Gauss–Hermite Kalman filter (GHKF) (pp. 243–244).
- The auxiliary filter picks ancestors using $p(y_k\mid\mu_k)$ before sampling (pp. 244–246).
- The Rao–Blackwellized filter samples only $u_k$ and keeps a Kalman filter per particle, which reduces variance (pp. 247–250).

## L3 — Walkthrough

### 11.1 Monte Carlo approximations in Bayesian inference (pp. 229–230)
Many Bayesian inference problems reduce to computing
$$E[g(x)\mid y_{1:T}]=\int g(x)\,p(x\mid y_{1:T})\,dx,\tag{11.1}$$
with $g:\mathbb R^n\to\mathbb R^m$ (p. 229). Closed forms exist only in special cases. *Monte Carlo* replaces the integral by sample averages (p. 229).

In a (perfect) Monte Carlo approximation, draw $x^{(i)}\sim p(x\mid y_{1:T})$ independently, $i=1,\dots,N$, and use
$$E[g(x)\mid y_{1:T}]\approx\frac1N\sum_{i=1}^N g(x^{(i)}).\tag{11.2}$$
Convergence follows from the law of large numbers and the central limit theorem. The error is $O(N^{-1/2})$ regardless of the dimension of $x$. The authors note this makes Monte Carlo superior in theory when dimension is large, "not necessarily in practice" (p. 230).

*Intuition note:* A cloud of samples stands in for the density. Averages over the cloud stand in for integrals. The error shrinks with the square root of the sample count, not with dimension.

### 11.2 Importance sampling (pp. 231–234)
Often one cannot sample from $p(x\mid y_{1:T})$ directly. Use an *importance distribution* $\pi(x\mid y_{1:T})$ that is easy to sample. It must be non-zero wherever $p$ is non-zero (its support must contain that of $p$) (p. 231):
$$\int g(x)p(x\mid y_{1:T})dx=\int\Big[g(x)\frac{p(x\mid y_{1:T})}{\pi(x\mid y_{1:T})}\Big]\pi(x\mid y_{1:T})dx.\tag{11.3}$$
Drawing $x^{(i)}\sim\pi(x\mid y_{1:T})$ (11.4) gives
$$E[g(x)\mid y_{1:T}]\approx\frac1N\sum_{i}\frac{p(x^{(i)}\mid y_{1:T})}{\pi(x^{(i)}\mid y_{1:T})}g(x^{(i)})=\sum_i\tilde w^{(i)}g(x^{(i)}),\quad \tilde w^{(i)}=\frac1N\frac{p(x^{(i)}\mid y_{1:T})}{\pi(x^{(i)}\mid y_{1:T})}.\tag{11.5, 11.6}$$
The weights correct for the samples not following the target (Figure 11.2, p. 232).

*Drawback:* evaluating $p(x^{(i)}\mid y_{1:T})$ needs the normalization constant in Bayes' rule,
$$p(x^{(i)}\mid y_{1:T})=\frac{p(y_{1:T}\mid x^{(i)})p(x^{(i)})}{\int p(y_{1:T}\mid x)p(x)dx},\tag{11.7}$$
and this integral often cannot be computed (p. 232). The fix is to approximate the denominator by importance sampling too:
$$\begin{aligned}E[g\mid y_{1:T}]&=\frac{\int g(x)p(y_{1:T}\mid x)p(x)dx}{\int p(y_{1:T}\mid x)p(x)dx}
=\frac{\int\big[\frac{p(y_{1:T}\mid x)p(x)}{\pi(x\mid y_{1:T})}g(x)\big]\pi\,dx}{\int\big[\frac{p(y_{1:T}\mid x)p(x)}{\pi(x\mid y_{1:T})}\big]\pi\,dx}\\
&\approx\frac{\frac1N\sum_i\frac{p(y_{1:T}\mid x^{(i)})p(x^{(i)})}{\pi(x^{(i)}\mid y_{1:T})}g(x^{(i)})}{\frac1N\sum_j\frac{p(y_{1:T}\mid x^{(j)})p(x^{(j)})}{\pi(x^{(j)}\mid y_{1:T})}}
=\sum_i w^{(i)}g(x^{(i)}).\end{aligned}\tag{11.8}$$
(p. 233)

**Algorithm 11.1 (Importance sampling)** (p. 233):
1. Draw $x^{(i)}\sim\pi(x\mid y_{1:T})$ (11.9).
2. Unnormalized weights $w^{*(i)}=\dfrac{p(y_{1:T}\mid x^{(i)})p(x^{(i)})}{\pi(x^{(i)}\mid y_{1:T})}$ (11.10). Normalized: $w^{(i)}=w^{*(i)}/\sum_j w^{*(j)}$ (11.11).
3. $E[g(x)\mid y_{1:T}]\approx\sum_i w^{(i)}g(x^{(i)})$ (11.12).

The posterior is formally $p(x\mid y_{1:T})\approx\sum_i w^{(i)}\delta(x-x^{(i)})$ (11.13), with $\delta$ the Dirac delta (p. 234).

*Intuition note:* Samples from a wrong but convenient distribution are reweighted by how much more the target likes them. Dividing by the weight sum removes the need for the unknown normalizing constant.

### 11.3 Sequential importance sampling (pp. 234–236)
SIS targets filtering in the generic model
$$x_k\sim p(x_k\mid x_{k-1}),\qquad y_k\sim p(y_k\mid x_k),\tag{11.14}$$
with $x_k\in\mathbb R^n$, $y_k\in\mathbb R^m$. Both may have discrete and continuous parts (p. 234). A set of *particles* $\{(w_k^{(i)},x_k^{(i)})\}$ gives $E[g(x_k)\mid y_{1:k}]\approx\sum_i w_k^{(i)}g(x_k^{(i)})$ (11.15), equivalently $p(x_k\mid y_{1:k})\approx\sum_i w_k^{(i)}\delta(x_k-x_k^{(i)})$ (11.16) (p. 234).

*Derivation.* Using the Markov properties of the model, the full posterior satisfies
$$p(x_{0:k}\mid y_{1:k})\propto p(y_k\mid x_{0:k},y_{1:k-1})p(x_{0:k}\mid y_{1:k-1})=p(y_k\mid x_k)p(x_k\mid x_{k-1})p(x_{0:k-1}\mid y_{1:k-1}).\tag{11.17}$$
Sampling $x^{(i)}_{0:k}\sim\pi(x_{0:k}\mid y_{1:k})$ gives weights
$$w_k^{(i)}\propto\frac{p(y_k\mid x_k^{(i)})p(x_k^{(i)}\mid x_{k-1}^{(i)})p(x_{0:k-1}^{(i)}\mid y_{1:k-1})}{\pi(x_{0:k}^{(i)}\mid y_{1:k})}.\tag{11.18}$$
Build the importance distribution recursively,
$$\pi(x_{0:k}\mid y_{1:k})=\pi(x_k\mid x_{0:k-1},y_{1:k})\,\pi(x_{0:k-1}\mid y_{1:k-1}).\tag{11.19}$$
Then
$$w_k^{(i)}\propto\frac{p(y_k\mid x_k^{(i)})p(x_k^{(i)}\mid x_{k-1}^{(i)})}{\pi(x_k^{(i)}\mid x_{0:k-1}^{(i)},y_{1:k})}\cdot\frac{p(x_{0:k-1}^{(i)}\mid y_{1:k-1})}{\pi(x_{0:k-1}^{(i)}\mid y_{1:k-1})}.\tag{11.20}$$
The last factor is proportional to the previous weight,
$$w_{k-1}^{(i)}\propto\frac{p(x_{0:k-1}^{(i)}\mid y_{1:k-1})}{\pi(x_{0:k-1}^{(i)}\mid y_{1:k-1})},\tag{11.21}$$
so
$$w_k^{(i)}\propto\frac{p(y_k\mid x_k^{(i)})p(x_k^{(i)}\mid x_{k-1}^{(i)})}{\pi(x_k^{(i)}\mid x_{0:k-1}^{(i)},y_{1:k})}\,w_{k-1}^{(i)}.\tag{11.22}$$
(p. 235)

**Algorithm 11.2 (SIS)** (p. 236): draw $x_0^{(i)}\sim p(x_0)$ (11.23) and set $w_0^{(i)}=1/N$. For $k=1,\dots,T$: (1) draw $x_k^{(i)}\sim\pi(x_k\mid x_{0:k-1}^{(i)},y_{1:k})$ (11.24); (2) update weights by (11.25), which is the same as (11.22) with $w_{k-1}^{(i)}$ in front, and normalize.

A *Markovian* importance distribution, $\pi(x_k\mid x_{0:k-1},y_{1:k})=\pi(x_k\mid x_{k-1},y_{1:k})$ (11.26), means only current states need storing. It also avoids history problems in resampling. The rest of the chapter assumes it (p. 236).

*Intuition note:* Each step multiplies the old weight by "how well the new state fits the measurement and dynamics, relative to how likely we were to propose it".

### 11.4 Resampling (pp. 236–239)
*Degeneracy problem:* in SIS, almost all particles can end up with zero or nearly zero weight. This held back practical particle filters for years (p. 236). *Resampling* draws $N$ new samples from the discrete distribution defined by the weights.

**Algorithm 11.3** (p. 237): treat $w_k^{(i)}$ as the probability of index $i$; draw $N$ indices; replace the sample set; set all weights to $1/N$.

*Why it is valid* (p. 237). Draw an index $A$ with probabilities $w_k^{(i)}$. Then
$$E_A[g(x_k^{(A)})\mid y_{1:k}]=\sum_i p(A=i)g(x_k^{(i)})=\sum_i w_k^{(i)}g(x_k^{(i)}).\tag{11.28}$$
With $N$ indices $A_{1:N}$, the plain average $\frac1N\sum_i g(x_k^{(A_i)})$ (11.29) has expectation
$$E_{A_{1:N}}\Big[\frac1N\sum_i g(x_k^{(A_i)})\Big]=\sum_i w_k^{(i)}g(x_k^{(i)}),\tag{11.30}$$
so resampling is unbiased. It removes small-weight particles and duplicates large-weight ones. The represented distribution does not change in theory, but resampling adds variance. The amount depends on the method (p. 237).

*Methods* (pp. 238–239). Naive multinomial resampling (independent draws from the weights) has high variance and is not recommended. Many resampling methods can be seen as drawing sorted uniforms $u^{(1)}<\dots<u^{(N)}$ and passing them to an inverse-transform sampler.
- **Algorithm 11.4:** set $m=1$, $s=w^{(1)}$. For $n=1,\dots,N$: while $s<u^{(n)}$, set $m\leftarrow m+1$, $s\leftarrow s+w^{(m)}$; then $A_n=m$.
- **Algorithm 11.5 (multinomial):** draw $v^{(j)}\sim U(0,1)$, $j=1,\dots,N+1$. Set $t^{(j)}=-\sum_{i=1}^j\log v^{(i)}$ and $u^{(i)}=t^{(i)}/t^{(N+1)}$.
- **Algorithm 11.6 (stratified):** $u^{(n)}\sim U\big((n-1)/N,\,n/N\big)$ independently.
- **Algorithm 11.7 (systematic):** one $u\sim U(0,1)$, then $u^{(n)}=(n-1)/N+u/N$.

All are unbiased. Chopin and Papaspiliopoulos recommend systematic resampling in practice, though its theory is less clear. Stratified resampling is a safe choice because it is ensured to have lower variance than multinomial (p. 239).

### 11.5 Particle filter (pp. 239–244)
Adding resampling to SIS gives *sequential importance resampling* (SIR), usually called the particle filter (p. 239). Resampling is usually not done every step. *Adaptive resampling* monitors the effective number of particles,
$$n_{\text{eff}}\approx\frac1{\sum_{i=1}^N\big(w_k^{(i)}\big)^2},\tag{11.31}$$
and resamples when it is significantly below $N$, for example $n_{\text{eff}}<N/10$ (p. 240).

**Algorithm 11.8 (SIR / PF)** (p. 240): draw $x_0^{(i)}\sim p(x_0)$ (11.32), $w_0^{(i)}=1/N$. For $k=1,\dots,T$: (1) $x_k^{(i)}\sim\pi(x_k\mid x_{k-1}^{(i)},y_{1:k})$ (11.33); (2) weights $w_k^{(i)}\propto w_{k-1}^{(i)}\dfrac{p(y_k\mid x_k^{(i)})p(x_k^{(i)}\mid x_{k-1}^{(i)})}{\pi(x_k^{(i)}\mid x_{k-1}^{(i)},y_{1:k})}$ (11.34), normalized; (3) resample if (11.31) is too low. The result is $p(x_k\mid y_{1:k})\approx\sum_i w_k^{(i)}\delta(x_k-x_k^{(i)})$ (11.35) and $E[g(x_k)\mid y_{1:k}]\approx\sum_iw_k^{(i)}g(x_k^{(i)})$ (11.36) (p. 241).

*Choice of importance distribution* (p. 241). Performance depends on it. It should be easy to sample, with evaluable density. The optimal one in terms of variance is
$$\pi(x_k\mid x_{0:k-1},y_{1:k})=p(x_k\mid x_{k-1},y_k).\tag{11.37}$$
If it cannot be used directly, importance distributions can sometimes be obtained by local linearization, where a mixture of EKFs, UKFs or other non-linear Kalman filters is used to form the importance distribution. Examples are the unscented particle filter (UPF), the Gauss–Hermite PF and the cubature PF. A Metropolis–Hastings step can also be used. Such proposals can make the filter fail to converge, so they "should be used with extreme care". It may be advisable to inflate the covariance or use a Student's t distribution (p. 241).

*Further remarks* (pp. 241–242). Tuning resampling and the order of weighting and sampling can improve efficiency. Sampling without replacement is more efficient. In some situations a deterministic rule that keeps the $N$ most likely particles is better. Punskaya et al. show this for digital demodulation, where the sampled space is discrete and the criterion is minimum error.

**Bootstrap filter** (Algorithm 11.9, p. 242): use the dynamic model as importance distribution. It is easy to implement but may need very many samples. Resampling is normally done every step.
1. $x_k^{(i)}\sim p(x_k\mid x_{k-1}^{(i)})$ (11.38).
2. $w_k^{(i)}\propto p(y_k\mid x_k^{(i)})$ (11.39), normalized.
3. Resample.

*Sample impoverishment* (p. 242): when dynamic-model noise is very small, resampling produces many identical particles. Remedies include resample-move, regularization or MCMC steps. Since low noise causes impoverishment, pure recursive estimation (process noise formally zero) is hard for a basic SIR filter. Rao–Blackwellization may help (Section 16.3.6, referred to only).

**Example 11.10** (p. 243). Bootstrap filter with 10,000 particles on the pendulum of Example 7.6 gives RMSE 0.10, about the same as the best Gaussian filters (Figure 11.3). In this case the filtering distribution is therefore quite well approximated by a Gaussian, and the particle filter is not particularly beneficial here.

**Example 11.11** (pp. 243–244). The sensor outputs clutter (random number in $[-2,2]$) with probability 50%, modelled as in Example 5.6. The bootstrap filter gets RMSE 0.20. A GHKF with no clutter model gets 0.89 (Figure 11.4). The authors say a clutter model cannot easily be implemented in Gaussian filters.

*Intuition note:* Propagate guesses through the dynamics, keep the ones the measurement supports, and discard the rest. In the clutter example this worked where a Gaussian filter did not. When the posterior is nearly Gaussian, as in the plain pendulum, it is not particularly beneficial.

### 11.6 Auxiliary particle filter (pp. 244–247)
Idea: introduce an auxiliary variable $\kappa$ so that $y_k$ can adjust the probability of sampling each particle. The result resembles a filter with the optimal importance distribution (p. 244).

From the weighted set at $k-1$, the prediction is $p(x_k\mid y_{1:k-1})\approx\sum_ip(x_k\mid x_{k-1}^{(i)})w_{k-1}^{(i)}$ (11.40). The approximate filtering distribution is
$$\hat p(x_k\mid y_{1:k})\propto p(y_k\mid x_k)\sum_ip(x_k\mid x_{k-1}^{(i)})w_{k-1}^{(i)}.\tag{11.41}$$
Problem: many particles explain $y_k$ poorly and get small weights if sampled as before (p. 245). Use the augmented target ($\kappa=1,\dots,N$):
$$\hat p(x_k,\kappa\mid y_{1:k})\propto p(y_k\mid x_k)\,p(x_k\mid x_{k-1}^{(\kappa)})\,w_{k-1}^{(\kappa)}.\tag{11.42}$$
Sampling from it and discarding $\kappa$ gives a sample from (11.41). With $x_k^{(i)},\kappa^{(i)}\sim\pi_k(x_k,\kappa\mid y_{1:k})$, the SIS weights are
$$w_k^{(i)}\propto\frac{p(y_k\mid x_k^{(i)})p(x_k^{(i)}\mid x_{k-1}^{(\kappa^{(i)})})w_{k-1}^{(\kappa^{(i)})}}{\pi_k(x_k^{(i)},\kappa^{(i)}\mid y_{1:k})}.\tag{11.43}$$
A convenient choice (Pitt and Shephard) is
$$\pi_k(x_k,\kappa\mid y_{1:k})\propto p(y_k\mid\mu_k^{(\kappa)})\,p(x_k\mid x_{k-1}^{(\kappa)})\,w_{k-1}^{(\kappa)},\tag{11.44}$$
where $\mu_k^{(\kappa)}$ is for example the mean, the mode, a draw, or another likely value associated with $p(x_k\mid x_{k-1}^{(\kappa)})$. Its marginal and conditional are
$$\pi_k(\kappa\mid y_{1:k})\propto w_{k-1}^{(\kappa)}p(y_k\mid\mu_k^{(\kappa)}),\qquad\pi_k(x_k\mid\kappa,y_{1:k})=p(x_k\mid x_{k-1}^{(\kappa)}).\tag{11.45}$$
So one first draws $\kappa$ with probability $\lambda^{(\kappa)}\propto\pi_k(\kappa\mid y_{1:k})$, the *first-stage weights*, then samples from $p(x_k\mid x_{k-1}^{(\kappa)})$ (pp. 245–246). The weights reduce to
$$w_k^{(i)}\propto\frac{p(y_k\mid x_k^{(i)})}{p(y_k\mid\mu_k^{(\kappa^{(i)})})}.\tag{11.46}$$
(added step: in (11.43) the factors $p(x_k^{(i)}\mid x_{k-1}^{(\kappa^{(i)})})w_{k-1}^{(\kappa^{(i)})}$ cancel against the denominator from (11.44).) An extra resampling with these weights is "not required or beneficial" (Johansen and Doucet) (p. 246).

**Algorithm 11.12 (APF)** (p. 246): draw $x_0^{(i)}$ from the prior, $w_0^{(i)}=1/N$. For each $k$:
1. Generate $\mu_k^{(i)}$ from $p(x_k\mid x_{k-1}^{(i)})$.
2. First-stage weights $\lambda^{(i)}\propto w_{k-1}^{(i)}p(y_k\mid\mu_k^{(i)})$ (11.47), normalized.
3. Resample $\{(\cdot,\lambda^{(i)})\}$ to get indices $\kappa^{(i)}$.
4. Draw $x_k^{(i)}\sim p(x_k\mid x_{k-1}^{(\kappa^{(i)})})$ (11.48).
5. Weights $w_k^{(i)}\propto p(y_k\mid x_k^{(i)})/p(y_k\mid\mu_k^{(\kappa^{(i)})})$ (11.49), normalized.

In step 3 the indices are stored and used in steps 4–5, instead of selecting resampled particles directly (pp. 246–247).

*Intuition note:* The APF takes a quick look at the new measurement before propagating. Particles whose predicted position fits $y_k$ are chosen more often as ancestors, so fewer samples are wasted.

### 11.7 Rao–Blackwellized particle filter (pp. 247–250)
RBPF (also called the mixture Kalman filter) evaluates part of the filtering equations analytically and the rest by sampling. By the Rao–Blackwell theorem this gives estimators with less variance than pure Monte Carlo. The authors' intuition: marginalization replaces a finite particle set by an infinite closed-form one, "always more accurate than any finite set" (p. 247).

*Model* (conditionally linear Gaussian, p. 247):
$$\begin{aligned}p(x_k\mid x_{k-1},u_{k-1})&=N(x_k\mid A_{k-1}(u_{k-1})x_{k-1},Q_{k-1}(u_{k-1})),\\ p(y_k\mid x_k,u_k)&=N(y_k\mid H_k(u_k)x_k,R_k(u_k)),\\ p(u_k\mid u_{k-1})&=\text{(any given form)},\end{aligned}\tag{11.50}$$
with $x_k$ the state, $y_k$ the measurement and $u_k$ an arbitrary latent variable. With a Gaussian prior for $x_k$, $x_k$ can be integrated out analytically and only $u_k$ needs sampling. Shapes (added step, from $x_k\in\mathbb R^n$, $y_k\in\mathbb R^m$): $A,Q$ are $n\times n$; $H$ is $m\times n$; $R$ is $m\times m$.

*Derivation.* The posterior factors as
$$p(u_{0:k},x_{0:k}\mid y_{1:k})=p(x_{0:k}\mid u_{0:k},y_{1:k})\,p(u_{0:k}\mid y_{1:k}),\tag{11.51}$$
where the first factor is Gaussian, computable by Kalman filter and RTS smoother. For the second, analogously to (11.17) and using Markovianity of $u_k$ (the middle step is $p(y_k\mid u_{0:k},y_{1:k-1})\,p(u_k\mid u_{0:k-1},y_{1:k-1})\,p(u_{0:k-1}\mid y_{1:k-1})$):
$$p(u_{0:k}\mid y_{1:k})\propto p(y_k\mid u_{0:k},y_{1:k-1})\,p(u_k\mid u_{k-1})\,p(u_{0:k-1}\mid y_{1:k-1}).\tag{11.52}$$
The measurements are not conditionally independent given $u_k$, so the first term differs from (11.17). It is computed by running the Kalman filter with fixed $u_{0:k}$ (p. 248). With the recursive importance distribution
$$\pi(u_{0:k}\mid y_{1:k})=\pi(u_k\mid u_{0:k-1},y_{1:k})\pi(u_{0:k-1}\mid y_{1:k-1}),\tag{11.53}$$
the same derivation as in Section 11.3 gives
$$w_k^{(i)}\propto\frac{p(y_k\mid u_{0:k}^{(i)},y_{1:k-1})\,p(u_k^{(i)}\mid u_{k-1}^{(i)})}{\pi(u_k^{(i)}\mid u_{0:k-1}^{(i)},y_{1:k})}\,w_{k-1}^{(i)}.\tag{11.54}$$
The full-history posterior of $x_{0:k}$ would need Kalman filter and RTS smoother. For only $x_k$, the Kalman filter suffices (p. 248).

**Algorithm 11.13 (RBPF)** (p. 249). Input: weighted particles $\{w_{k-1}^{(i)},u_{k-1}^{(i)},m_{k-1}^{(i)},P_{k-1}^{(i)}\}$ ($m$: $n$-vector, $P$: $n\times n$). Process $y_k$:
1. Kalman predictions given $u_{k-1}^{(i)}$:
$$m_k^{-(i)}=A_{k-1}(u_{k-1}^{(i)})m_{k-1}^{(i)},\quad P_k^{-(i)}=A_{k-1}P_{k-1}^{(i)}A_{k-1}^\top+Q_{k-1}\ \text{(all at }u_{k-1}^{(i)}).\tag{11.55}$$
2. Draw $u_k^{(i)}\sim\pi(u_k\mid u_{0:k-1}^{(i)},y_{1:k})$ (11.56).
3. Weights by (11.57), the same form as (11.54), where the likelihood is the Kalman filter's marginal measurement likelihood
$$p(y_k\mid u_{0:k}^{(i)},y_{1:k-1})=N\big(y_k\mid H_k(u_k^{(i)})m_k^{-(i)},\,H_k(u_k^{(i)})P_k^{-(i)}H_k^\top(u_k^{(i)})+R_k(u_k^{(i)})\big),\tag{11.58}$$
then normalize.
4. Kalman updates given $u_k^{(i)}$ ($H_k,R_k$ evaluated at $u_k^{(i)}$):
$$\begin{aligned}v_k^{(i)}&=y_k-H_km_k^{-(i)},& S_k^{(i)}&=H_kP_k^{-(i)}H_k^\top+R_k,\\ K_k^{(i)}&=P_k^{-(i)}H_k^\top[S_k^{(i)}]^{-1},& m_k^{(i)}&=m_k^{-(i)}+K_k^{(i)}v_k^{(i)},\\ P_k^{(i)}&=P_k^{-(i)}-K_k^{(i)}S_k^{(i)}[K_k^{(i)}]^\top.\end{aligned}\tag{11.59}$$
5. Resample if (11.31) is too low.

Output: $E[g(x_k,u_k)\mid y_{1:k}]\approx\sum_iw_k^{(i)}\int g(x_k,u_k^{(i)})N(x_k\mid m_k^{(i)},P_k^{(i)})dx_k$ (11.60), i.e. $p(x_k,u_k\mid y_{1:k})\approx\sum_iw_k^{(i)}\delta(u_k-u_k^{(i)})N(x_k\mid m_k^{(i)},P_k^{(i)})$ (11.61) (p. 250).

*Optimal importance distribution* (minimizing weight variance):
$$\pi(u_k\mid y_{1:k},u_{0:k-1}^{(i)})=p(u_k\mid y_{1:k},u_{0:k-1}^{(i)})\propto p(y_k\mid u_k,u_{0:k-1}^{(i)})p(u_k\mid u_{0:k-1}^{(i)},y_{1:k-1}).\tag{11.62}$$
In general it cannot be normalized or sampled directly, but if $u_k$ is discrete it can be normalized and used directly. The method extends beyond conditionally linear Gaussian models, for example with latent-variable-dependent non-linear terms (Schön et al.). EKF, UKF or other Gaussian filters can replace the exact Kalman steps in slightly non-linear cases (p. 250).

*Intuition note:* Where the model is linear and Gaussian given the latent variable, one Kalman filter per particle does exactly what many samples would only approximate. Samples are spent only on the hard variable $u_k$.

### 11.8 Exercises (pp. 250–252)
Listed under "Exercises worth doing".

## Toy example (ours, not from the text)
One bootstrap-filter step with $N=4$, scalar state. Suppose the propagated particles (step 1 of Algorithm 11.9) are $x^{(i)}=-1,\,0,\,1,\,3$ with prior weights $1/4$. Measurement $y_k=1$, likelihood $p(y\mid x)\propto\exp(-(y-x)^2/2)$ (unit-variance Gaussian).

1. Unnormalized weights (11.39): $e^{-2}=0.1353$, $e^{-0.5}=0.6065$, $e^{0}=1$, $e^{-2}=0.1353$. Sum $=1.8771$.
2. Normalized: $0.0721,\ 0.3231,\ 0.5327,\ 0.0721$.
3. Weighted mean (11.36): $-1(0.0721)+0+1(0.5327)+3(0.0721)=0.677$.
4. $n_{\text{eff}}$ (11.31): $\sum w^2=0.0052+0.1044+0.2838+0.0052=0.3986$, so $n_{\text{eff}}=2.51$. This is above $N/10=0.4$, so adaptive resampling would not trigger. The bootstrap filter resamples every step anyway (p. 242).
5. Systematic resampling with $u=0.3$ (Algorithm 11.7): $u^{(n)}=(n-1)/4+0.3/4=0.075,\,0.325,\,0.575,\,0.825$. Cumulative weights: $0.0721,\,0.3952,\,0.9279,\,1.0$. Algorithm 11.4 gives $A=(2,2,3,3)$.
6. New particles: $0,0,1,1$ with weights $1/4$. Their mean is $0.5$, not $0.677$. This is one random outcome. Unbiasedness (11.30) holds only on average over the resampling draw. The extra spread is the added variance (p. 237). The far particles ($-1$ and $3$) were dropped, which is the point of resampling.

## Concepts
- [[monte-carlo-approximation]] (new) — replace an integral by an average over samples from the distribution; error $O(N^{-1/2})$ (pp. 229–230)
- [[importance-sampling]] (new) — sample from $\pi$, correct with weights $p/\pi$; self-normalized when $p$ is known up to a constant (pp. 231–233)
- [[sequential-importance-sampling]] (new) — recursive weight update for state-space models, $w_k\propto w_{k-1}\times$ likelihood × transition / proposal (pp. 234–236)
- [[degeneracy-problem]] (new) — in SIS almost all particles can end up with ~zero weight (p. 236)
- [[resampling]] (new) — draw $N$ indices from the weights, reset weights to $1/N$; unbiased, adds variance (pp. 236–239)
- [[effective-sample-size]] (new) — $1/\sum w^2$, used to trigger adaptive resampling (p. 240)
- [[particle-filter]] (new) — SIR: SIS plus (adaptive) resampling (pp. 239–240)
- [[optimal-importance-distribution]] (new) — variance-minimizing proposal $p(x_k\mid x_{k-1},y_k)$ (p. 241)
- [[bootstrap-filter]] (new) — particle filter proposing from the dynamic model (p. 242)
- [[sample-impoverishment]] (new) — resampling yields identical copies when dynamic noise is tiny (p. 242)
- [[auxiliary-particle-filter]] (new) — uses $y_k$ to choose ancestors via first-stage weights (pp. 244–246)
- [[rao-blackwellization]] (new) — compute part of the filter analytically, sample the rest, lower variance (p. 247)
- [[kalman-filter]] — here run per particle, conditional on latent $u$ (pp. 248–249)
- [[state-space-model]] — model (11.14) with possibly discrete components (p. 234)

## Canonical instances
- [[pendulum-tracking-bootstrap-pf]] — bootstrap PF with 10,000 particles, RMSE 0.10, approximately the same as the best Gaussian filters (p. 243)
- [[cluttered-pendulum-tracking]] — 50% clutter: PF RMSE 0.20 vs GHKF 0.89 (pp. 243–244)

## Bridges (candidates)
- [same-math] $E_p[g]=E_\pi[g\,p/\pi]$ reweighting ↔ off-policy value estimation (reinforcement learning): the same importance-ratio identity (not discussed in this unit).
- [same-math] per-particle Kalman update in RBPF ↔ [[kalman-filter]]: literally the predict/update equations (11.55), (11.59).
- [structural-analogy] particle filter ↔ observer / state estimator: a model run forward and corrected by measurements, here for non-linear and non-Gaussian systems.
- [metaphor] resampling ↔ selection in evolution: low-weight particles die, high-weight ones are copied.

## Questions this raises
- How does the variance of the weights, and hence $n_{\text{eff}}$, grow with the state dimension? The chapter only says Monte Carlo's dimension-independence may not hold in practice (p. 230).
- How should one choose the resampling threshold (the text's example is $N/10$) and the proposal when the optimal one (11.37) is unavailable?
- How can the particle filter be made to work for static parameters, where process noise is zero (p. 242)?
- How does the particle approximation of $p(x_{0:k}\mid y_{1:k})$ turn into a smoother? The text defers this to Section 15.1 (p. 236).

## Exercises worth doing
- Ex. 11.1 (pp. 250–251) — Kalman filter, optimal importance distribution and CPU-cost comparison for a linear Gaussian model; asks which implementation to choose in a real implementation — difficulty: medium
- Ex. 11.2 (p. 251) — compare a Gaussian filter and a bootstrap filter on a random walk with log-normal measurements — difficulty: medium
- Ex. 11.3 (p. 251) — implement a bootstrap filter and test it against non-linear Kalman filters — difficulty: easy
- Ex. 11.4 (p. 251) — implement an auxiliary particle filter and compare with the bootstrap filter — difficulty: medium
- Ex. 11.6 (p. 251) — bootstrap filter for bearings-only tracking, RMSE versus Kalman filters — difficulty: medium
- Ex. 11.9 (p. 252) — Rao–Blackwellized filter for the clutter model, including its optimal importance distribution — difficulty: hard

## Reading notes
- Printed page = pdf − 30. Pages carry a pre-publication notice (Cambridge University Press, 2nd edition, © Särkkä and Svensson 2023).
- The text layer drops many symbols (tildes, hats, minus signs). All equations here were checked against the page images. For example, Algorithm 11.5 has $t^{(j)}=-\sum\log v^{(i)}$ in the image, with a minus sign.
- p. 237 says "sequential importance sampling (SIR)". From context this should be SIS.
- Algorithm 11.2 conditions on $x_{0:k-1}^{(i)}$. Algorithm 11.8 uses $x_{k-1}^{(i)}$, following the Markovian assumption (11.26).
- Exercise 11.1 refers to Exercise 7.1; Exercises 11.6–11.8 refer to Exercises 7.2 and 9.11 and Equations (4.61), (4.90). Those are not in this unit.
- Not digested beyond a brief mention: the references to Chapters 15–16 (smoothers, Rao–Blackwellized static-parameter estimation).
