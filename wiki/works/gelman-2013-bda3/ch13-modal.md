---
id: gelman-2013-bda3/ch13-modal
work: gelman-2013-bda3
unit: "13 Modal and distributional approximations"
pages: 311–350
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Modal and distributional approximations (BDA3, Chapter 13)

## L0 — One line
When posterior simulation is too slow or impossible, one can approximate the posterior by a simpler distribution fitted at its modes, or fitted by iterative optimisation (EM, variational Bayes, expectation propagation).

## L1 — The gist (≤ 120 words)
When direct or Markov chain simulation is too slow, how can we approximate a posterior quickly? The chapter covers mode finding (conditional maximization, Newton, EM and its variants). It also covers normal and t-mixture approximations at the modes, with Laplace's method for integrals. Variational Bayes fits a simple factorised g by reducing KL(g||p). Expectation propagation matches moments factor by factor. The chapter also sketches INLA, CCD, ABC and unknown normalizing factors. These methods give quick inferences, starting values for MCMC and comparison points. Variational Bayes converges to an approximation, not to the posterior, and the chapter notes that it can make sense to fit a model in several ways and compare.

**Prerequisites:** posterior density, log density, Taylor expansion, gradient and Hessian, conditional/marginal distributions, normal and exponential-family forms, importance sampling, KL divergence (defined in the text), hierarchical normal model.

## L2 — Key ideas (5–10 bullets)
- Modes are searched for to start mapping the posterior, not for their own sake. Conditional maximization and Newton's method are the two basic tools; the marginal mode of a parameter subset is preferred when available (pp. 311–313).
- A posterior mode can be a poor summary when the posterior is asymmetric, for example when the mode sits on a boundary. If a mode will be the summary, it can make sense to use a "boundary-avoiding" prior (gamma(2, ·) for scales, $(1-\rho)(1+\rho)$ for correlations, Wishart$(d+3,AI)$ for covariance matrices). For full Bayes this is not needed (pp. 313–318).
- The normal (or $t_4$) approximation is centred at the mode with variance equal to the inverse curvature. Multimodal posteriors give mixtures (for fairly widely separated modes) weighted by $q(\hat\theta_k|y)|V_{\theta_k}|^{1/2}$. Laplace's method approximates integrals, and importance resampling can improve the draws (pp. 318–319).
- EM finds marginal posterior modes and raises $\log p(\phi|y)$ at every step. ECM, ECME, AECM, SEM/SECM and PX-EM extend it, and monotone increase is a debugging check (pp. 320–325).
- With a good analytic approximation to $p(\gamma|\phi,y)$, the marginal $p(\phi|y)$ is approximated by joint over approximate conditional, as in (13.9). Importance sampling over $\gamma$ can refine this (pp. 325–326).
- Variational Bayes minimises $\mathrm{KL}(g\|p)$ over a factorised family by cycling through coordinate updates. When its expectations can be evaluated, each update provably lowers KL, but the result is only the closest fit in its class. EM is a special case (pp. 331–338).
- Expectation propagation factorises $g$ by data points, using cavity, tilted distribution and moment matching. It fits the joint distribution, but has no convergence guarantee and needs factors with tractable integrals (pp. 338–343).
- Other tools handle special difficulties: INLA, CCD, ABC and unknown normalizing factors $z(\theta)$ (bridge/path sampling) (pp. 343–348).

## L3 — Walkthrough

### Chapter intro (p. 311)
Iterative simulation (Chapters 11–12) can be too slow. Distributional approximations give quick inferences, starting points for MCMC, and information about model fit. Different approximations can be fitted and compared with the tools of Chapters 6–7 (p. 311).

### 13.1 Finding posterior modes (pp. 311–313)
- Modes are searched for to begin mapping the posterior density, not for their own sake. If many modes exist, one should try to find them all, or at least all those with non-negligible posterior mass nearby. This sometimes needs several starting points (p. 311).
- Better, where possible, is to find the mode of the marginal posterior of a subset of the parameters, then analyse the rest conditional on it (pp. 311–312).

**Conditional maximization (stepwise ascent).** Start at rough estimates, then change one block of $\theta$ at a time, keeping the others fixed, so that the log posterior increases at each step. If the posterior density is bounded, the steps converge to a local mode. Iterative proportional fitting is an example. For many standard models each conditional maximum has an analytic form (p. 312).

**Newton's method.** Let $L(\theta)=\log p(\theta|y)$. An unnormalized density is fine, because a multiplicative constant in $p$ is an additive constant in $L$. The quadratic approximation is generally fairly accurate when the number of data points is large relative to the number of parameters (p. 312).
1. Choose a start $\theta^0$.
2. For $t=1,2,\dots$: compute $L'(\theta^{t-1})$ (vector) and $L''(\theta^{t-1})$ (matrix), then maximise the quadratic approximation centred there:
$$\theta^t=\theta^{t-1}-[L''(\theta^{t-1})]^{-1}L'(\theta^{t-1}).$$

Convergence is not guaranteed from every start, particularly where $-L''$ is not positive definite. Conditional maximization or crude estimates can supply starts. Convergence is extremely fast once the iterates are near the solution. If it fails, iterates typically move quickly towards the edge of the parameter space, and one retries from a new start (pp. 312–313).

**Quasi-Newton and conjugate gradient.** BFGS builds an approximation of $-L''$ iteratively from gradients only. Conjugate gradient uses only gradients, with conjugate directions rather than steepest descent. It likely needs more iterations than Newton or quasi-Newton, but costs less per iteration and needs less storage (p. 313).

**Numerical derivatives.** With $e_i$ the $i$th unit vector and $\delta_i$ small (e.g. 0.0001):
$$L_i'(\theta)=\frac{dL}{d\theta_i}\approx\frac{L(\theta+\delta_ie_i|y)-L(\theta-\delta_ie_i|y)}{2\delta_i}\tag{13.1}$$
$$L''_{ij}(\theta)=\frac{d^2L}{d\theta_i d\theta_j}\approx\frac{L'_i(\theta+\delta_je_j|y)-L'_i(\theta-\delta_je_j|y)}{2\delta_j}\approx\frac{L(\theta+\delta_ie_i+\delta_je_j)-L(\theta-\delta_ie_i+\delta_je_j)-L(\theta+\delta_ie_i-\delta_je_j)+L(\theta-\delta_ie_i-\delta_je_j)}{4\delta_i\delta_j}\tag{13.2}$$
The value of $\delta_i$ should be low enough to approximate the derivative and high enough to avoid roundoff error (p. 313).

*Intuition note.* Conditional maximization climbs one coordinate at a time. Newton jumps to the top of a local parabola. Newton is fast near a mode but can wander from bad starts.

### 13.2 Boundary-avoiding priors for modal summaries (pp. 313–318)
**Problem.** The mode is a good summary of a symmetric posterior but can be poor for an asymmetric one (p. 313).
- In the 8-schools example the marginal posterior mode of $\tau$ is at $\tau=0$ (Figure 13.1). That is consistent with the data, but substantively the true variation is not believed to be exactly zero (pp. 313–314).
- Full Bayes has no problem here. The uniform prior gives $\tau=0$ zero probability, and the posterior median (4.9) is reasonable (p. 314).

**Simulated example.** $y_j\sim N(\theta_j,1)$, $\theta_j\sim N(0,\tau^2)$, $J=10$, true $\tau=0.5$. The maximum marginal likelihood estimate solves $1+\hat\tau^2=\frac1J\sum y_j^2$, with $\hat\tau=0$ if $\frac1J\sum y_j^2<1$. In almost half of 1000 simulations $\hat\tau=0$. The data allow little more than bounding the group-level variance (pp. 314–315, Figure 13.2).

**Zero-avoiding prior for a scale.** If the mode will be the summary, choose the prior accordingly. Then $p(\tau)$ must be zero at $\tau=0$ (p. 315).
- Lognormal and inverse-gamma have effective lower bounds below which the prior shuts off a range of $\tau$ near zero. Making them vague enough to avoid this makes the prior strongly peaked. So there is no reasonable default setting (pp. 315–316).
- Preferred: $\tau\sim\mathrm{Gamma}(2,\tfrac2A)$ with $A$ large. The density starts at 0 and increases linearly, then curves gently back to zero. The linear behaviour at 0 means that, however concentrated the likelihood is near zero, the posterior stays consistent with the data (p. 316).
- This prior is meant for mode summaries. If posterior simulation is planned, the author would generally see no advantage in it and would use uniform or half-Cauchy defaults (p. 316; see Section 5.7).

**Correlation parameter.** Varying-intercept, varying-slope model (pp. 316–317):
- $y_{ij}\sim N(\theta_{j1}+\theta_{j2}x_i,1)$, $x_i\sim N(0,1)$, $n_j=5$, $J=10$.
- $(\theta_{j1},\theta_{j2})\sim N\big(0,\begin{pmatrix}\tau_1^2&\rho\tau_1\tau_2\\ \rho\tau_1\tau_2&\tau_2^2\end{pmatrix}\big)$.
- Marginal likelihood: $p(y|\tau_1,\tau_2,\rho)=\prod_{j=1}^J N(\hat\theta_j|0,V_j+T)$, with $\hat\theta_j,V_j$ the least-squares estimate and covariance in group $j$, and $T$ the group-level covariance matrix.
- True $\tau_1=\tau_2=0.5$, $\rho=0$, which should be a best case.
- Profile likelihood: $L_{\rm profile}(\rho|y)=\max_{\tau_1,\tau_2}p(y|\tau_1,\tau_2,\rho)$.
- Result: in 1000 simulations the maximum marginal likelihood $\hat\rho$ is on the boundary ($\pm1$) over 10% of the time, and the profile likelihood is typically uninformative (Figure 13.4).

For mode summaries, replace $U(-1,1)$ by $p(\rho)\propto(1-\rho)(1+\rho)$, i.e. Beta(2,2) on $(\rho+1)/2$. It is zero at the boundaries but linear near them, so it will not contradict any likelihood (p. 317).

**Covariance matrices.** For a $d\times d$ covariance matrix use a Wishart$(d+3,AI)$ prior density. It is zero with positive constant derivative at the degenerate boundary, so the mode estimate is always positive definite. For large $A$ it corresponds to independent Gamma$(2,\delta)$ priors on the $d$ eigenvalues with $\delta\to0$. In two dimensions it gives $p(\rho)\propto(1+\rho)(1-\rho)$ (pp. 317–318). For full Bayes the author would prefer something like a scaled inverse-Wishart (p. 318).

*Intuition note.* A mode can sit on a boundary even when the posterior has plenty of mass away from it. A prior that vanishes linearly at the boundary pushes the mode inside without overruling strong data. It is a tool for mode summaries, not a general default.

### 13.3 Normal and related mixture approximations (pp. 318–319)
**Normal at a single mode.** $p_{\text{normal approx}}(\theta)=N(\theta|\hat\theta,V_\theta)$ with $V_\theta=\Big[-\frac{d^2\log p(\theta|y)}{d\theta^2}\Big|_{\theta=\hat\theta}\Big]^{-1}$. The second derivative can be analytic or numerical as in (13.2). Transform parameters first (logs, logits) so they live on the whole line and are roughly symmetric, and multiply by the Jacobian (p. 318).

**Laplace's method.** To approximate $\mathrm E(h(\theta)|y)$, let $u(\theta)=\log(h(\theta)p(\theta|y))$ and let $\theta_0$ maximise $u$. With $d$ the dimension of $\theta$:
$$\mathrm E(h(\theta)|y)\approx h(\theta_0)p(\theta_0|y)(2\pi)^{d/2}|-u''(\theta_0)|^{-1/2}.$$
This can be reasonable if $h$ is fairly smooth, given approximate posterior normality. It works best for unimodal posteriors, or separately for each mode (p. 318).
- With an unnormalized density $q$, apply Laplace to $hq$ and to $q$:
$$\mathrm E(h(\theta)|y)=\frac{\int h(\theta)q(\theta|y)d\theta}{\int q(\theta|y)d\theta}\tag{13.3}$$

**Mixture for $K$ modes.** $p_{\text{normal approx}}(\theta)\propto\sum_{k=1}^K\omega_kN(\theta|\hat\theta_k,V_{\theta_k})$. Set the masses by equating $q(\hat\theta_k|y)$ with the approximation at each mode. If the modes are fairly widely separated and the normal approximation suits each mode:
$$\omega_k=q(\hat\theta_k|y)|V_{\theta_k}|^{1/2}\tag{13.4}$$
so $p_{\text{normal approx}}(\theta)\propto\sum_k q(\hat\theta_k|y)\exp\!\big(-\tfrac12(\theta-\hat\theta_k)^TV_{\theta_k}^{-1}(\theta-\hat\theta_k)\big)$ (p. 319).

**Multivariate $t$.** For a broader distribution, replace each normal by a $t$ with $\nu$ degrees of freedom:
$$p_{t\text{ approx}}(\theta)\propto\sum_kq(\hat\theta_k|y)\big(\nu+(\theta-\hat\theta_k)^TV_{\theta_k}^{-1}(\theta-\hat\theta_k)\big)^{-(d+\nu)/2}.$$
$\nu=4$ (three finite moments) has worked in some examples. Further improvements: fit at saddle points or tails, integrate out some components, or move to variational Bayes or expectation propagation (p. 319).

**Sampling.** Choose a component with multinomial probabilities $\omega_k$, then draw from that normal or $t$ (Cholesky factorization, Appendix A). The draws can be used in importance sampling or importance resampling (Section 10.4) (p. 319).

*Intuition note.* Near a mode the log density looks like a downward parabola, and the curvature gives the width. Each mode's mass is roughly height times width, which is what $q(\hat\theta_k|y)|V_{\theta_k}|^{1/2}$ expresses.

### 13.4 Finding marginal posterior modes using EM (pp. 320–325)
In problems with many parameters, normal approximations to the joint are often useless and the joint mode is typically not helpful. Write $\theta=(\gamma,\phi)$ and approximate $p(\phi|y)$ first (this section), then $p(\gamma|\phi,y)$ (next section) (p. 320).

EM is an iterative method for finding the mode of $p(\phi|y)$. It is useful when $p(\phi|y)$ is hard to maximise directly but $p(\gamma|\phi,y)$ and $p(\phi|\gamma,y)$ are easy to work with. Viewing $\gamma$ as missing data, it formalises the old idea of alternately filling in missing values and re-estimating parameters. It estimates the needed functions of the missing data (sufficient statistics) jointly. "E" is the expectation step and "M" is the maximization step. Many models (mixtures, some hierarchical models) can be recast with $\gamma$ as added parameters playing the role of missing data (p. 320).

**Derivation.** Start from $\log p(\phi|y)=\log p(\gamma,\phi|y)-\log p(\gamma|\phi,y)$. Take expectations over $\gamma\sim p(\gamma|\phi^{\rm old},y)$. The left side does not depend on $\gamma$, so
$$\log p(\phi|y)=\mathrm E_{\rm old}(\log p(\gamma,\phi|y))-\mathrm E_{\rm old}(\log p(\gamma|\phi,y)).\tag{13.5}$$
The last term is maximised at $\phi=\phi^{\rm old}$ (Exercise 13.6). The other term, $\mathrm E_{\rm old}(\log p(\gamma,\phi|y))=\int\log p(\gamma,\phi|y)\,p(\gamma|\phi^{\rm old},y)d\gamma$, is called $Q(\phi|\phi^{\rm old})$ in the EM literature (pp. 320–321).

If $\phi^{\rm new}$ has $\mathrm E_{\rm old}\log p(\gamma,\phi^{\rm new}|y)>\mathrm E_{\rm old}\log p(\gamma,\phi^{\rm old}|y)$, the first term of (13.5) rises and the second does not rise, so $\log p(\phi^{\rm new}|y)>\log p(\phi^{\rm old}|y)$ (p. 321).
- **GEM** (generalized EM): at each iteration only increase $Q$.
- **EM**: maximise $Q$.
- Both increase $p(\phi|y)$ at each iteration. EM converges to a local mode except in some special cases. GEM does not necessarily converge to a local mode.
- The convergence rate depends on the proportion of information about $\phi$ in the joint density that is missing from the marginal. It can be slow if that proportion is large (p. 321).

**Algorithm.** Start with $\phi^0$. For $t=1,2,\dots$:
- **E-step:** compute $\mathrm E_{\rm old}\log p(\gamma,\phi|y)=\int p(\gamma|\phi^{\rm old},y)\log p(\gamma,\phi|y)d\gamma$, with $\phi^{\rm old}=\phi^{t-1}$.
- **M-step:** $\phi^t$ maximises it (GEM: merely increases it) (p. 321).

Search for multiple modes by starting from many points. Compare masses with the normal approximation of 13.3. As a debugging check, compute $\log p(\phi^t|y)$ every iteration and verify that it increases monotonically (p. 321).

**Example: normal, unknown mean and variance, partially conjugate prior** (pp. 322–323). The model is $y_1..y_n\sim N(\mu,\sigma^2)$, prior $\mu\sim N(\mu_0,\tau_0^2)$ with $\mu_0,\tau_0$ known, and uniform on $\log\sigma$. Here $\phi=\mu$ and $\gamma=\sigma$.
$$\log p(\mu,\sigma|y)=-\tfrac{1}{2\tau_0^2}(\mu-\mu_0)^2-(n+1)\log\sigma-\tfrac1{2\sigma^2}\sum_i(y_i-\mu)^2+\text{const}\tag{13.6}$$
E-step:
$$\mathrm E_{\rm old}\log p(\mu,\sigma|y)=-\tfrac1{2\tau_0^2}(\mu-\mu_0)^2-(n+1)\mathrm E_{\rm old}(\log\sigma)-\tfrac12\mathrm E_{\rm old}\!\big(\tfrac1{\sigma^2}\big)\sum_i(y_i-\mu)^2+\text{const}\tag{13.7}$$
$\mathrm E_{\rm old}(\log\sigma)$ is not linked to $\mu$, so it does not affect the M-step. Given $\mu$, $\sigma^2\sim\text{Inv-}\chi^2\big(n,\tfrac1n\sum(y_i-\mu)^2\big)$, so $1/\sigma^2$ is a scaled $\chi^2$ and
$$\mathrm E_{\rm old}(1/\sigma^2)=\Big(\tfrac1n\sum_i(y_i-\mu^{\rm old})^2\Big)^{-1}.$$
Hence
$$\mathrm E_{\rm old}\log p(\mu,\sigma|y)=-\tfrac1{2\tau_0^2}(\mu-\mu_0)^2-\tfrac12\Big(\tfrac1n\sum_i(y_i-\mu^{\rm old})^2\Big)^{-1}\sum_i(y_i-\mu)^2+\text{const}\tag{13.8}$$
M-step: (13.8) is a normal log posterior with prior $N(\mu_0,\tau_0^2)$ and $n$ data points each of variance $\frac1n\sum(y_i-\mu^{\rm old})^2$. Its mode is
$$\mu^{\rm new}=\frac{\frac1{\tau_0^2}\mu_0+\frac{n}{\frac1n\sum(y_i-\mu^{\rm old})^2}\bar y}{\frac1{\tau_0^2}+\frac{n}{\frac1n\sum(y_i-\mu^{\rm old})^2}}.$$
Iterating converges to the marginal mode of $p(\mu|y)$ (p. 323).

*Intuition note.* EM replaces unknown quantities by their expected role under the current guess, then optimises as if they were known. The decomposition (13.5) shows why the true marginal density cannot go down.

**Extensions** (p. 323 onward).
- **ECM:** the M-step is replaced by $S$ conditional maximizations (CM-steps). At step $s$, maximise $Q$ over all $\phi$ with $g_s(\phi)=g_s(\phi^{t+(s-1)/S})$. The common choice of constraint function partitions $\phi$ into $S$ subsets, so only one subset moves at a time. This is a GEM. If each CM-step sets first derivatives to zero, ECM converges to a local mode. $p(\phi|y)$ still increases every iteration (p. 323).
- **Multicycle ECM:** extra E-steps within an iteration, e.g. before each CM-step. More work per iteration, sometimes fewer total iterations (p. 323).
- **ECME:** some CM-steps maximise the actual $\log p(\phi|y)$ instead of the expected log joint. It also increases $\log p(\phi|y)$ each iteration and converges to a local mode if each CM-step sets first derivatives to zero. It can speed convergence dramatically, e.g. by applying Newton's method to the marginal density in some CM-steps (pp. 323–324).
- **AECM:** allows different definitions of $\gamma$ (different ways of completing the data) at different CM-steps. It keeps the local-mode convergence and monotone increase (p. 324).

**Supplemented EM (SEM) and SECM** (pp. 324–325). These give an asymptotic variance matrix at the mode. Let $M(\phi)$ be the EM map, $\phi^{t+1}=M(\phi^t)$, and $D_M$ its Jacobian at the marginal mode $\hat\phi$.
$$V=V_{\rm joint}+V_{\rm joint}D_M(I-D_M)^{-1},\qquad V_{\rm joint}=\Big[\mathrm E\Big(-\tfrac{d^2\log p(\phi,\gamma|y)}{d\theta^2}\Big|\phi,y\Big)\Big|_{\phi=\hat\phi}\Big]^{-1}$$
(the image prints $d\theta^2$; see Reading notes). $V_{\rm joint}$ can typically be computed analytically, so only $D_M$ is needed. Numerical algorithm:
1. Run EM to convergence to get $\hat\phi$ (apply the rest separately per mode).
2. Choose a start $\phi^0$ with no component equal to $\hat\phi$.
3. For each $t$: (a) run one E- and M-step from $\phi^t$ to get $\phi^{t+1}$. (b) For each $i$, let $\phi^t(i)$ equal $\hat\phi$ except the $i$th element, which is $\phi_i^t$. Run one E- and M-step from $\phi^t(i)$ to get $\phi^{t+1}(i)$, and set
$$r^t_{ij}=\frac{\phi_j^{t+1}(i)-\hat\phi_j}{\phi_i^t-\hat\phi_i}\ \text{for each } j.$$
When $r_{ij}$ stops changing it estimates $(D_M)_{ij}$. Elements of $\phi$ independent of $\gamma$ have zero rows (p. 325).

For ECM:
$$V=V_{\rm joint}+V_{\rm joint}(D_M^{\rm ECM}-D_M^{\rm CM})(I-D_M^{\rm ECM})^{-1},$$
where $D_M^{\rm CM}$ is the convergence rate of conditional maximization applied directly to $\log p(\phi|y)$. It depends only on $V_{\rm joint}$ and $\nabla_s=\nabla g_s(\hat\phi)$:
$$D_M^{\rm CM}=\prod_{s=1}^S\big[\nabla_s(\nabla_s^TV_{\rm joint}\nabla_s)^{-1}\nabla_s^TV_{\rm joint}\big]$$
(p. 325). SECM needs analytic work for $V_{\rm joint}$ and $\nabla_s$ as well as numerical work for $D_M^{\rm ECM}$ (p. 325).

**PX-EM.** The Gibbs-sampler efficiency ideas of Section 12.1 have analogues for mode finding (they were originally built for it). In the $t$ model, the latent variances $V_i$ are missing data, and ECM maximises over $\mu,\tau,\alpha$ (p. 325).

### 13.5 Conditional and marginal posterior approximations (pp. 325–326)
Often $p(\gamma|\phi,y)$ can be well approximated analytically, depending on $\phi$: $p_{\rm approx}(\gamma|\phi,y)$. (In the hierarchical model of Section 5.4 the normal fit to $p(\theta,\mu|\tau,y)$ is exact.) If $p(\phi|y)$ cannot be approximated directly, use the ratio trick of (5.19):
$$p_{\rm approx}(\phi|y)=\frac{p(\gamma,\phi|y)}{p_{\rm approx}(\gamma|\phi,y)}\tag{13.9}$$
- A value of $\gamma$ must be specified (possibly a function of $\phi$).
- If the approximation is exact, the $\gamma$ factors cancel and the marginal is exact.
- Otherwise a natural choice is the centre of the approximate conditional, e.g. $\mathrm E(\gamma|\phi,y)$.
- For a $d$-dimensional normal (or $t$) approximation with mean $\hat\gamma(\phi)$ and scale matrix $V_\gamma(\phi)$:
$$p_{\rm approx}(\phi|y)\propto p(\hat\gamma(\phi),\phi|y)\,|V_\gamma(\phi)|^{1/2}\tag{13.10}$$
because the normalizing factor of the denominator is proportional to $|V_\gamma(\phi)|^{-1/2}$ (p. 326).

**Improvement by importance sampling.** For a given $\phi$,
$$p(\phi|y)=\int\frac{p(\gamma,\phi|y)}{p_{\rm approx}(\gamma|\phi,y)}p_{\rm approx}(\gamma|\phi,y)d\gamma=\mathrm E_{\rm approx}\Big(\frac{p(\gamma,\phi|y)}{p_{\rm approx}(\gamma|\phi,y)}\Big)\tag{13.11}$$
Simulate $S$ draws $\gamma^s$ from $p_{\rm approx}(\gamma|\phi,y)$ and average the ratios. Repeat over a grid of $\phi$. If the joint density's normalizing constant is unknown, more complicated procedures are needed (p. 326).

*Intuition note.* The marginal of $\phi$ is the joint density divided by the conditional density of $\gamma$. If we can normalise the conditional approximately, we get the marginal up to the error of that approximation, evaluated at one $\gamma$.

### 13.6 Example: hierarchical normal model (pp. 326–330)
This continues the coagulation example of Section 11.6. The aim is approximate inference by finding the mode of $p(\mu,\log\sigma,\log\tau|y)$ and a normal approximation there. Given $(\mu,\log\sigma,\log\tau)$, the $\theta_j$ are independent normal (p. 326).

**Crude estimates (p. 327).** $\hat\theta_j=\bar y_{\cdot j}$, $\hat\sigma^2$ = average of the $J$ within-group sample variances, $\mu$ and $\tau^2$ = mean and variance of the $\hat\theta_j$ (first column of Table 13.1).

**Conditional maximization of the joint mode** (p. 327). Update each parameter in turn by its conditional mode: each $\theta_j$ by (11.10), $\mu$ by (11.13), $\log\sigma$ by $\log\hat\sigma$ from (11.15), $\log\tau$ by $\log\hat\tau$ from (11.17) (p. 328). For $\log\sigma$, the conditional mode of $\sigma^2$ is $\frac{n}{n+2}\hat\sigma^2$, but the factor $\frac n{n+2}$ does not appear in the mode of $\log\sigma$ because of the Jacobian (Exercise 13.7) (p. 327).

| Parameter | Crude | 1st | 2nd | 3rd |
|---|---|---|---|---|
| $\theta_1$ | 61.00 | 61.28 | 61.29 | 61.29 |
| $\theta_2$ | 66.00 | 65.87 | 65.87 | 65.87 |
| $\theta_3$ | 68.00 | 67.74 | 67.73 | 67.73 |
| $\theta_4$ | 61.00 | 61.15 | 61.15 | 61.15 |
| $\mu$ | 64.00 | 64.01 | 64.01 | 64.01 |
| $\sigma$ | 2.29 | 2.17 | 2.17 | 2.17 |
| $\tau$ | 3.56 | 3.32 | 3.31 | 3.31 |
| $\log p$ | −63.70 | −61.42 | −61.42 | −61.42 |

(Table 13.1, p. 327.) Convergence took three iterations. The mode is very close to the crude estimate because the shrinkage factors $\frac{\sigma^2/n_j}{\sigma^2/n_j+\tau^2}$ are all near zero. This is only a local mode. Another mode lies at the boundary of the parameter space, but the region around it has little posterior mass (Exercise 13.8) (p. 328). With more pooling (as in Section 5.5) one should continue the analysis (p. 328).

**Factoring into conditional and marginal.** The joint mode often does not summarise well, especially when $J$ is large relative to the $n_j$. Take $\gamma=\theta=(\theta_1..\theta_J)$ and $\phi=(\mu,\log\sigma,\log\tau)$. This $\phi$ has only three components however large $J$ is, so asymptotic approximations should work better for $\phi$ than for the joint. $p(\theta|\mu,\sigma,\tau,y)$ is a product of independent normals with means $\hat\theta_j$ and variances $V_{\theta_j}$ (11.9) (p. 328). Using (13.9), where the conditional is exact:
$$p(\mu,\log\sigma,\log\tau|y)=\frac{p(\theta,\mu,\log\sigma,\log\tau|y)}{p(\theta|\mu,\log\sigma,\log\tau,y)}\propto\frac{\tau\prod_jN(\theta_j|\mu,\tau^2)\prod_j\prod_iN(y_{ij}|\theta_j,\sigma^2)}{\prod_jN(\theta_j|\hat\theta_j,V_{\theta_j})}.$$
Because the denominator is exact, this holds for any $\theta$. Setting $\theta=\hat\theta$:
$$p(\mu,\log\sigma,\log\tau|y)\propto\tau\prod_{j=1}^JN(\hat\theta_j|\mu,\tau^2)\prod_{j=1}^J\prod_{i=1}^{n_j}N(y_{ij}|\hat\theta_j,\sigma^2)\prod_{j=1}^JV_{\theta_j}^{1/2}\tag{13.12}$$
with $\hat\theta_j,V_{\theta_j}$ from (11.11) (p. 328).

**EM for the marginal mode** (p. 329). Maximising (13.12) analytically fails because $\hat\theta_j,V_{\theta_j}$ depend on $(\mu,\sigma,\tau)$. Newton's method would need derivatives, so EM is used, averaging over $\theta$:
$$\log p(\theta,\mu,\log\sigma,\log\tau|y)=-n\log\sigma-(J-1)\log\tau-\tfrac1{2\tau^2}\sum_j(\theta_j-\mu)^2-\tfrac1{2\sigma^2}\sum_j\sum_i(y_{ij}-\theta_j)^2+\text{const}\tag{13.13}$$
E-step: $\mathrm E_{\rm old}((\theta_j-\mu)^2)=(\hat\theta_j-\mu)^2+V_{\theta_j}$ and $\mathrm E_{\rm old}((y_{ij}-\theta_j)^2)=(y_{ij}-\hat\theta_j)^2+V_{\theta_j}$, with $\hat\theta_j,V_{\theta_j}$ from (11.11) at the old values. M-step (derivation: Exercise 13.9):
$$\mu^{\rm new}=\tfrac1J\sum_j\hat\theta_j,\quad\sigma^{\rm new}=\Big(\tfrac1n\sum_j\sum_i\big((y_{ij}-\hat\theta_j)^2+V_{\theta_j}\big)\Big)^{1/2},\quad\tau^{\rm new}=\Big(\tfrac1{J-1}\sum_j\big((\hat\theta_j-\mu^{\rm new})^2+V_{\theta_j}\big)\Big)^{1/2}\tag{13.14}$$
Debugging: compute $\log$ of (13.12) at each iteration. If it does not increase, there is a mistake or roundoff error (p. 329).

| | Joint mode | 1st | 2nd | 3rd |
|---|---|---|---|---|
| $\mu$ | 64.01 | 64.01 | 64.01 | 64.01 |
| $\sigma$ | 2.17 | 2.33 | 2.36 | 2.36 |
| $\tau$ | 3.31 | 3.46 | 3.47 | 3.47 |
| $\log p(\mu,\log\sigma,\log\tau|y)$ | −61.99 | −61.835 | −61.832 | −61.832 |

(Table 13.2, p. 330.) Approximate convergence in three steps. As is typical, $\sigma$ and $\tau$ are larger at the marginal mode than at the joint mode (p. 330).

**Joint approximation** (p. 330). Fit a normal using the $3\times3$ second-derivative matrix of (13.12). Draw $(\mu,\log\sigma,\log\tau)$ from it, then $\theta$ from the exact normal conditional. Table 13.3 gives the resulting quantiles. For example, the $\tau$ row is 1.44, 2.62, 3.43, 4.65, 8.19 at 2.5%, 25%, 50%, 75%, 97.5%. The median of $\mu$ is 64.05 and of $\sigma$ is 2.37.

**Comparison.** If these inferences are not adequate, the approximation can still serve as a comparison point and for starting values. Draw from the $t_4$ approximation for $(\mu,\log\sigma,\log\tau)$ to get a roughly overdispersed distribution, then subsample by importance resampling to start iterative simulation (p. 330).

### 13.7 Variational inference (pp. 331–338)
Variational Bayes (VB) is an algorithmic framework, similar to EM, for approximating a joint distribution. EM converges to point estimates of hyperparameters. VB iterates to a closed-form approximation that is the closest fit to the posterior within a specified class (p. 331).

**KL divergence.** VB builds $g(\theta)$ so as to minimise
$$\mathrm{KL}(g\|p)=-\mathrm E_g\Big(\log\frac{p(\theta|y)}{g(\theta)}\Big)=-\int\log\Big(\frac{p(\theta|y)}{g(\theta)}\Big)g(\theta)d\theta\tag{13.15}$$
Its absolute minimum is 0, attained at $g\equiv p$. The difficulty is that VB is used where we cannot summarise $p$ directly, so we work with a simpler parametric class $g(\theta|\phi)$ ($\phi$ = variational hyperparameters). Iterations are mathematically guaranteed to decrease the KL at each step, until $\phi$ stops changing. It can make sense to check the results by running from several starts (p. 331).

**Class of approximations.** A standard choice is independence, $g(\theta|\phi)=\prod_{j=1}^Jg_j(\theta_j|\phi_j)$. The form of each $g_j$ is determined by looking at $\mathrm E_{g_{-j}}\log p(\theta|y)$ as a function of $\theta_j$. This is like Gibbs sampling, but with the average rather than the conditional density. VB works best for exponential-family models with conditionally conjugate priors. In nonconjugate models one can use restricted forms such as normals (pp. 331–332).

**Algorithm.** Start with guesses for all $\phi$. Cycle through $j$, setting $\log g_j(\theta_j|\phi_j)=\mathrm E_{g_{-j}}(\log p(\theta|y))=\int\log p(\theta|y)\,g_{-j}(\theta_{-j}|\phi_{-j})d\theta_{-j}$ up to a constant. This is a $(J-1)$-dimensional integral, often analytic (p. 332).

**Example: 8 schools** (pp. 332–335). School effects are labelled $\alpha_j$. $\theta=(\alpha_1..\alpha_8,\mu,\tau)$ has 10 dimensions.
$$\log p(\theta|y)=-\tfrac12\sum_{j=1}^8\frac{(y_j-\alpha_j)^2}{\sigma_j^2}-8\log\tau-\tfrac12\tfrac1{\tau^2}\sum_j(\alpha_j-\mu)^2+\text{const}\tag{13.16}$$
$$g(\theta)=g(\alpha_1)\cdots g(\alpha_8)g(\mu)g(\tau)\tag{13.17}$$
Forms (the $\sigma_j$ are known):
- For $\alpha_j$: $\mathrm E\log p=-\tfrac12\frac{(y_j-\alpha_j)^2}{\sigma_j^2}-\tfrac12\mathrm E(\tau^{-2})\mathrm E((\alpha_j-\mu)^2)+\text{const}$. This is quadratic in $\alpha_j$, so $g(\alpha_j)$ is normal. It combines two pieces of information, one at $y_j$ with inverse-variance $\sigma_j^{-2}$ and one at $\mathrm E(\mu)$ with inverse-variance $\mathrm E(\tau^{-2})$:
$$g(\alpha_j)=N\Big(\alpha_j\Big|\frac{\frac1{\sigma_j^2}y_j+\mathrm E(\frac1{\tau^2})\mathrm E(\mu)}{\frac1{\sigma_j^2}+\mathrm E(\frac1{\tau^2})},\ \frac1{\frac1{\sigma_j^2}+\mathrm E(\frac1{\tau^2})}\Big)\tag{13.18}$$
- For $\mu$ (eight pieces of information):
$$g(\mu)=N\Big(\mu\Big|\tfrac18\sum_j\mathrm E(\alpha_j),\ \tfrac18\tfrac1{\mathrm E(1/\tau^2)}\Big)\tag{13.19}$$
- For $\tau$:
$$g(\tau^2)=\text{Inv-}\chi^2\Big(\tau^2\Big|7,\tfrac17\sum_j\mathrm E((\alpha_j-\mu)^2)\Big)\tag{13.20}$$

These match the Gibbs conditionals (Section 11.6) and EM (Section 13.6), except that $\sigma_j$ are known here (p. 333).

Generic notation: $g(\alpha_j)=N(M_{\alpha_j},S_{\alpha_j}^2)$ (13.21), $g(\mu)=N(M_\mu,S_\mu^2)$ (13.22), $g(\tau^2)=\text{Inv-}\chi^2(7,M_\tau^2)$ (13.23). The needed expectations are $\mathrm E(\mu)=M_\mu$, $\mathrm E(1/\tau^2)=1/M_\tau^2$, $\mathrm E(\alpha_j)=M_{\alpha_j}$ and $\mathrm E((\alpha_j-\mu)^2)=(M_{\alpha_j}-M_\mu)^2+S_{\alpha_j}^2+S_\mu^2$, using independence (p. 333).

Run: draw $M_{\alpha_j},M_\mu\sim N(0,1)$ and $S_{\alpha_j},S_\mu\sim U(0,1)$. Iterate through $\alpha_1..\alpha_8,\mu,\tau$, plug in the current $M,S$ to (13.18)–(13.20), and relabel the results as the new $M,S$. This looks like EM, but distributions rather than point estimates are updated. About 50 iterations to approximate convergence from this random start (Figure 13.5, p. 334).

KL check: the author evaluates the KL analytically (up to a constant) and reports it decreases steadily (Figure 13.5). The expression is given on pp. 334–335 (see Reading notes for printing issues).

Comparison to full Bayes (Figure 13.6): the Gaussian form necessarily fails to capture some subtleties of the posterior, as the asymmetric full-Bayes intervals show. There is no dependence among the $\alpha_j$, so the fit would be inappropriate for some purposes. But the approximation fits the marginals fairly well, and VB is "a fast and scalable approach" for such problems with large datasets. VB converges to the closest fit within a restricted class, unlike MCMC, which eventually converges to the posterior. Where both are possible, compare them (p. 335).

**Proof that each step decreases KL** (pp. 335–336). Write $p(\theta|y)=p(\theta,y)/p(y)$:
$$\mathrm{KL}(g\|p)=-\int\log\Big(\frac{p(\theta,y)}{g(\theta)}\Big)g\,d\theta+\int\log p(y)\,g\,d\theta=-\mathrm E_g\Big(\log\frac{p(\theta,y)}{g(\theta)}\Big)+\log p(y)\tag{13.24}$$
$\log p(y)$ does not depend on $g$, so decreasing the first term decreases KL. $\mathrm E_g\log\frac{p(\theta,y)}{g(\theta)}$ is the **variational lower bound**. Update $g_j$ with $g=g_jg_{-j}$ (both normalised):
$$-\mathrm E_g\log\frac{p(\theta,y)}{g}=-\int g_j\Big(\int g_{-j}\log p(\theta,y)d\theta_{-j}\Big)d\theta_j+\int g_j\log g_jd\theta_j+\int g_{-j}\log g_{-j}d\theta_{-j}\tag{13.25}$$
The last term does not involve $g_j$ and is dropped. Define $\mathrm E_{g_{-j}}\log p(\theta,y)=\int g_{-j}\log p(\theta,y)d\theta_{-j}$ (13.26), a function of $\theta_j$ only, and $\log\tilde p(\theta_j)=\mathrm E_{g_{-j}}\log p(\theta,y)+\text{const}$ (13.27). Then
$$-\mathrm E_g\log\frac{p(\theta,y)}{g}=-\int g_j\log\frac{\tilde p(\theta_j)}{g_j(\theta_j)}d\theta_j+\text{const}\tag{13.28}$$
This is $\mathrm{KL}(g_j\|\tilde p)$, minimised at $g_j\equiv\tilde p$. So when the expectations are available, each update decreases the global KL. If (13.26) is not closed form, any update to $g_j$ that decreases (13.28) will do (p. 336).

*Intuition note.* When the expectations can be evaluated, each coordinate update sets $g_j$ to the exact optimum given the other factors. Since the total objective cannot rise at any step, KL falls. The limit is the closest fit the algorithm reaches within the factorised family, which need not be the posterior.

**Model checking.** The VB fit is a proper distribution, so one can draw $\theta^s$ from $g$ and replicated data $y^{\rm rep,s}$ (8 schools: 1000 draws of $\alpha_1..\alpha_8$ from the final $g$, then data; for new schools, draw $(\mu,\tau)$ from $g$, then 8 new schools from $N(\mu,\tau^2)$ and one observation each, given some assumed $\sigma$). Compared to full Bayes, variational inference would be expected to fit the observed data better, and as a point estimate it can overfit. A check can still reveal problems (pp. 336–337).

**VB then importance sampling or particle filtering** (p. 337).
- Direct importance weights $p(\theta^s|y)/g(\theta^s)$ with draws from $g$ "can be disastrous". The VB fit tends to be less variable than the target, so the ratios have long tails and averages are unstable.
- The author recommends importance resampling: draw from $g$, then resample without replacement using the weights. Resampling without replacement is crucial so that extremely high-weight points do not dominate.
- Particle filtering uses VB draws as a start, moves them through the target with Metropolis or HMC, and splits and removes points. It may need a large programming investment.

**EM as special case of VB** (p. 337): (a) parameters split into $\phi,\gamma$; (b) $g(\phi)$ is required to be a point mass; (c) $g(\gamma)$ is unconstrained, so $g(\gamma)=p(\gamma|\phi,y)$ at the latest $\phi$.

**More general VB** (p. 338): where closed forms fail (non-conjugate), the objective $\mathrm{KL}(g\|p)$ can be replaced by an approximation (good ones exist e.g. for logistic regression). The approximation typically changes each step, defined from the latest $g$.

### 13.8 Expectation propagation (pp. 338–343)
EP is another deterministic iterative algorithm approximating $p(\theta|y)$ by a best-fit member of a parametric family. It differs from VB in its criterion and in how it computes (p. 338).

**Setup.** Write the target as $f(\theta)=\prod_{i=0}^nf_i(\theta)$ (13.29), with unnormalized factors: $f_0$ the prior and each $f_i$ one data point's likelihood. The approximation is factorised by data, $g(\theta)=\prod_{i=0}^ng_i(\theta)$ (13.30). VB instead factorises by parameter. Each $g_i$ approximates $f_i$, one at a time but within the context of the whole (p. 338).

**Exponential families.** $g$ should be in the exponential family: normalizing function times exp of a linear function of sufficient statistics. For $N(\theta|\mu,\sigma^2)=\frac1{\sqrt{2\pi}\sigma}\exp(-\frac1{2\sigma^2}\theta^2+\frac\mu{\sigma^2}\theta-\frac{\mu^2}{2\sigma^2})$ the sufficient statistics are $\theta,\theta^2$ and the coefficients are natural parameters. For a multivariate normal $N(\mu,\Sigma)$ the sufficient statistics are $\theta,\theta\theta^T$ and the natural parameters are proportional to $\Sigma^{-1}\mu$ and $\Sigma^{-1}$ (pp. 338–339).

**One EP step** (p. 339). Remove $g_i$ and put $f_i$ in its place.
- Cavity distribution (unnormalized): $g_{-i}(\theta)\propto g(\theta)/g_i(\theta)$.
- Tilted distribution: $g_{-i}(\theta)f_i(\theta)$.
- Approximate the tilted distribution within the parametric family by **moment matching**: set expectations of the sufficient statistics of $g$ equal to those under the tilted distribution. For $g=N(\mu,\Sigma)$: $\mu=\mathrm E_{\rm tilted}(\theta)=\int\theta g_{-i}f_id\theta$ and $\Sigma=\mathrm{var}_{\rm tilted}(\theta)$.
- This is the updated $g$. Back out $g_i=g/g_{-i}$. The context changes each step, hence the iteration.
- The hard part is computing the expectations. They work because the tilted distribution is mostly $g_{-i}$, with only one difficult factor $f_i$.
- *Sequential EP* updates $g$ after each step. *Parallel EP* updates $g$ only after all tilted moments are computed, and is typically much faster.

Moment matching corresponds to minimising KL from the tilted distribution to the new approximation. The iterative marginal matching does not guarantee that KL from the full posterior to the overall approximation is minimised. There is no convergence guarantee. For models with log-concave $f_i$ and initialization at the prior it has been used successfully in many applications (p. 340).

**EP for logistic regression** (pp. 340–341). $y_i\sim\text{Bin}(m_i,\text{logit}^{-1}(X_i\theta))$, $\theta\sim N(\mu_0,\Sigma_0)$, $X$ is $n\times k$. EP can give a better normal approximation than the mode-centred one (Section 16.2). Take $g_i=N(\mu_i,\Sigma_i)$, $g_0$ = prior, and start each $g_i$ ($i\ge1$) with $\Sigma_i^{-1}\mu_i=0$ and $\Sigma_i^{-1}=cI_k$, $c$ a positive number. For each $i$:
1. Cavity $N(\mu_{-i},\Sigma_{-i})$: $\Sigma_{-i}^{-1}\mu_{-i}=\Sigma^{-1}\mu-\Sigma_i^{-1}\mu_i$; $\Sigma_{-i}^{-1}=\Sigma^{-1}-\Sigma_i^{-1}$.
2. Project onto the direction $X_i$: $M_{-i}=X_i\mu_{-i}$, $V_{-i}=X_i\Sigma_{-i}X_i^T$. Steps 1–2 combine as $M_{-i}=V_{-i}\big((X_i\Sigma X_i^T)^{-1}X_i\mu-V_i^{-1}M_i\big)$ and $V_{-i}=\big((X_i\Sigma X_i^T)^{-1}-V_i^{-1}\big)^{-1}$.
3. Tilted distribution of $\eta=X_i\theta$: $N(\eta|M_{-i},V_{-i})\text{Bin}(y_i|m_i,\text{logit}^{-1}(\eta))$. Compute $E_k=\int\eta^kg_{-i}(\eta)f_i(\eta)d\eta$ for $k=0,1,2$ by numerical integration (Gauss–Kronrod). Then $M=E_1/E_0$ and $V=E_2/E_0-(E_1/E_0)^2$. For bounds, one may simply use $M_{-i}\pm\delta\sqrt{V_{-i}}$ with $\delta$ large, such as 10.
4. Updated factor $g_i(\eta)=N(M_i,V_i)$: $\frac{M_i}{V_i}=\frac MV-\frac{M_{-i}}{V_{-i}}$; $\frac1{V_i}=\frac1V-\frac1{V_{-i}}$.
5. Back to the full space: $\Sigma_i^{-1}\mu_i=X_i^T\frac{M_i}{V_i}$ ($k\times1$); $\Sigma_i^{-1}=X_i^T\frac1{V_i}X_i$ ($k\times k$).
6. Combine: $\Sigma^{-1}\mu=\Sigma_{-i}^{-1}\mu_{-i}+\Sigma_i^{-1}\mu_i$; $\Sigma^{-1}=\Sigma_{-i}^{-1}+\Sigma_i^{-1}$. Skipped in parallel EP until all factors are updated (saves time for large $n,k$).
7. Return to step 1 with a new $i$.

It is feasible because each likelihood factor depends on $\theta$ only through $X_i\theta$, so integrals are one-dimensional. Any fixed normal prior folds into $g_0$. A hierarchical model with hyperparameters needs another step (p. 341).

**Example: bioassay** (pp. 341–343). 20 rats, four groups of 5, $y_i\sim\text{Bin}(m_i,\text{logit}^{-1}(\theta_1+\theta_2x_i))$, $i=1..4$, $X_i=(1,x_i)$, flat prior. The mode-based normal gave a point estimate of (0.8, 7.7). The exact posterior is skewed with a long tail toward large $\theta_1,\theta_2$. EP started from $\Sigma_i^{-1}\mu_i=0$, $\Sigma_i^{-1}=I$ and was run for 10 iterations (40 steps), "more than enough". Figure 13.7 shows approximate convergence after 4 iterations. In Figure 13.8 the EP ellipse is closer to the exact posterior than the mode-based one and is shifted toward the mass (contours at 0.05 times the mode).

**Summary** (p. 343): EP is fast and direct to implement. Unlike EM it approximates the entire distribution. Unlike usual VB it fits the joint rather than margins. But it requires a likelihood or prior factorisation with simple integrals, so general-purpose versions are an active research goal.

**Extensions** (p. 343): a provably convergent but slower double-loop algorithm, usable only when regular EP fails to converge; damping (partial updates); fractional (power) EP, which minimises an $\alpha$-divergence, improves stability and can recover EP with $\alpha$ close to 1 in the final iterations. Improved marginals of $\theta_i$ come from (13.9).

*Intuition note.* EP asks, for each data point, "if everything else is held at the current approximation, what normal best matches the posterior with this one true factor put back?" It then keeps the part that this factor adds. VB instead fits each parameter's factor given the others.

### 13.9 Other approximations (pp. 343–345)
- **INLA** (p. 343): partition into many parameters $\gamma$ given few hyperparameters $\phi$. Build a joint Gaussian approximation for $p(\gamma|\phi,y)$ and apply (13.9) to approximate $p(\phi|y)$ and $p(\gamma_i|\phi,y)$. Approximate $p(\gamma_i|y)$ by numerical integration over the low-dimensional $p_{\rm approx}(\phi|y)$. It works best with few hyperparameters (a discrete grid is then enough). It was developed for hierarchical models with jointly normal prior for the data-model parameters.
- **CCD** (p. 344): deterministic placement of few points around the mode, using a fractional factorial design to avoid exponential growth (27 points for a 5-dimensional model, 287 for 15 dimensions). The integration is a finite weighted sum. Accuracy is between modal approximation and full grid or Monte Carlo integration. It is used in Chapter 21 for Gaussian processes.
- **ABC** (p. 344): needs only the ability to simulate $y^{\rm rep}|\theta$, not the likelihood. Basic rejection form: draw $\theta$ from the prior and $y^{\rm rep}$ from $p(y^{\rm rep}|\theta)$, compute a discrepancy $d(y^{\rm rep},y)$ (zero if identical), and accept $\theta$ if $d<\epsilon$. Accepted draws approximate the posterior. Three challenges: choosing $d$ (ideally capturing sufficient statistics, not noise); choosing $\epsilon$ (small enough to be informative, not so small that nearly everything is rejected); high rejection with a broad prior. Partial remedies: draw from another distribution and correct by importance sampling, or use MCMC steps.
- **Substitution likelihood** (pp. 344–345): use a rank or quantile-based likelihood in place of the full likelihood. This allows a specified joint model (a copula) to be applied where the marginal distribution would not fit.

### 13.10 Unknown normalizing factors (pp. 345–348)
For standard models $p(\theta|y)\propto p(\theta)p(y|\theta)$ has a single unknown constant, $p(y)$ (and likewise $p(\gamma,\phi|y)\propto p(\phi)p(\gamma|\phi)p(y|\gamma,\phi)$). A new problem arises when the sampling density has a normalizing factor that depends on $\theta$ (common in conditionally specified models such as spatial statistics). Ignoring e.g. the factor $1/\sigma$ of a normal would give a wrong posterior (p. 345). Write
$$p(y|\theta)=\tfrac1{z(\theta)}q(y|\theta),\qquad z(\theta)=\int q(y|\theta)dy\tag{13.31}$$
so $p(\theta|y)\propto p(\theta)\frac1{z(\theta)}q(y|\theta)$. An unknown constant in the prior is harmless. In hierarchical models, if the population distribution is known only as $q(\gamma|\phi)=z(\phi)p(\gamma|\phi)$, then $p(\gamma,\phi|y)\propto p(\phi)\frac1{z(\phi)}q(\gamma|\phi)p(y|\gamma)$ (pp. 345–346).

**Basic strategy** (p. 346): (1) get an analytic estimate of $z(\theta)$, e.g. Laplace centred at a crude estimate of $\theta$; (2) build an approximation to the posterior (Chapter 13); (3) for more exact computation, evaluate $z(\theta)$ whenever the density is needed at a new $\theta$, treating $z$ as an approximately known but expensive function. For one- or two-dimensional $\theta$, compute $z$ on a grid and interpolate. There is no need to compute $z$ where posterior probability is essentially zero.

**Computing $z$.** Importance sampling: $z(\theta)=\int\frac{q(y|\theta)}{g(y)}g(y)dy=\mathrm E_g\big(\frac{q(y|\theta)}{g(y)}\big)$, estimated by $\frac1S\sum_sq(y^s|\theta)/g(y^s)$ with $y^s\sim g$. The same $g$ and draws can be reused over a local range of $\theta$ where the densities $q(y|\theta)$ are similar. $g$ need not be normalized, provided the same $g$ is used for all $\theta$ (or relative normalizing constants are known), because $z$ is needed only up to a $\theta$-free constant (pp. 346–347).

**Bridge and path sampling** (p. 347). For a family $p(\gamma|\phi,y)$ indexed by $\phi$, densities are needed only up to normalizing constants.
- One option is importance sampling with $p(\gamma|\phi_*,y)$ at a central $\phi_*$ as the approximating distribution.
- If no single $\phi_*$ covers the range, use *bridge sampling*: sample from the two end distributions $p(\gamma|\phi_0,y)$ and $p(\gamma|\phi_1,y)$. The estimate at any $\phi$ is a weighted average of the two importance-sampling estimates, with weights from a simple iterative formula. It generalises to more points.
- In the limit of the continuous range, *path sampling* (a differential form) uses the identity
$$\tfrac{d}{d\phi}\log p(\phi|y)=\mathrm E\big(U(\gamma,\phi,y)\,\big|\,\phi,y\big),\quad U=\tfrac{d\log p(\gamma,\phi|y)}{d\phi}.$$
Numerically integrating gives $\log p(\phi|y)$ up to an additive constant.

Both are related to parallel tempering (discussed on p. 299, outside this unit), which uses a similar structure of samples from an indexed family (pp. 347–348).

### 13.11–13.12 Bibliographic note and exercises (pp. 348–350)
The bibliographic note credits sources for each method (e.g. boundary-avoiding priors: Chung, Rabe-Hesketh et al. 2013a,b; EM: Dempster, Laird, Rubin 1977; EP: Minka 2001; INLA/CCD: Rue, Martino, Chopin 2009; bridge sampling: Meng and Wong 1996) (p. 348). Exercises 13.1–13.11 are on pp. 349–350; selected ones are listed below.

## Toy example (ours, not from the text)
Data: 3 successes, 1 failure; uniform prior. The unnormalized posterior is $q(\theta)=\theta^3(1-\theta)$, i.e. Beta(4,2). The exact mean is $4/6=0.667$ and the exact sd is $\sqrt{4\cdot2/(36\cdot7)}=\sqrt{0.031746}=0.178$.

1. **Newton (Section 13.1).** $L=3\log\theta+\log(1-\theta)$, $L'=3/\theta-1/(1-\theta)$, $L''=-3/\theta^2-1/(1-\theta)^2$. Start at $\theta^0=0.5$: $L'=6-2=4$, $L''=-12-4=-16$. So $\theta^1=0.5-4/(-16)=0.75$. Check: $L'(0.75)=4-4=0$, so $\hat\theta=0.75$ is the mode.
2. **Normal approximation (13.3).** $L''(0.75)=-3/0.5625-1/0.0625=-5.333-16=-21.333$. So $V=1/21.333=0.0469$ and sd $=0.2165$. The approximation is $N(0.75,0.2165^2)$. With only four data points it is crude (mean 0.75 vs exact 0.667, sd 0.217 vs 0.178).
3. **Laplace for the posterior mean (13.3).** Numerator uses $u=\log(\theta\,q)=4\log\theta+\log(1-\theta)$. Its mode is where $4/\theta=1/(1-\theta)$, so $\theta_0=0.8$. $u''=-4/0.64-1/0.04=-6.25-25=-31.25$.
 - Numerator $=0.8\cdot q(0.8)\cdot\sqrt{2\pi}\cdot31.25^{-1/2}$ with $q(0.8)=0.512\cdot0.2=0.1024$, so $0.08192\times2.5066\times0.17889=0.03673$.
 - Denominator $=q(0.75)\sqrt{2\pi}\,21.333^{-1/2}=0.10547\times2.5066\times0.21651=0.05724$.
 - Ratio $=0.03673/0.05724\approx0.642$.
 
 The mode (0.75) is further from the exact mean (0.667) than the Laplace ratio (0.642) is.

## Concepts
- [[newton-raphson-mode-finding]] (new) — iterate $\theta^t=\theta^{t-1}-[L'']^{-1}L'$, maximising a local quadratic of the log posterior (p. 312)
- [[conditional-maximization]] (new) — maximise over one block of parameters at a time, raising the log posterior each step (p. 312)
- [[boundary-avoiding-prior]] (new) — a prior vanishing linearly at the boundary, meant for use when the mode will be the summary (pp. 315–318)
- [[normal-approximation-at-mode]] (new) — $N(\hat\theta,V_\theta)$ with $V_\theta$ the inverse negative Hessian of the log posterior at the mode; mixtures or $t$ for several modes (p. 318)
- [[laplace-approximation]] (new) — approximate $\int h\,p$ by $h(\theta_0)p(\theta_0|y)(2\pi)^{d/2}|-u''|^{-1/2}$ (p. 318)
- [[em-algorithm]] (new) — alternate E-step (expected log joint) and M-step; $p(\phi|y)$ increases each iteration (pp. 320–321)
- [[ecm-sem-px-em-family]] (new) — ECM, ECME, AECM, SEM/SECM, PX-EM: variants for speed or for variance estimates (pp. 323–325)
- [[variational-inference-elbo]] — fit factorised $g$ by minimising $\mathrm{KL}(g\|p)$, equivalently raising the variational lower bound $\mathrm E_g\log(p(\theta,y)/g)$ (pp. 331, 336)
- [[kl-divergence]] — here $\mathrm{KL}(g\|p)=-\mathrm E_g\log(p/g)$, minimum 0, attained when $g\equiv p$ (p. 331)
- [[expectation-propagation]] (new) — approximate by moment-matching each data factor in the context of the others (cavity, tilted distribution) (pp. 338–339)
- [[approximate-bayesian-computation]] (new) — accept prior draws whose simulated data are within $\epsilon$ of observed data (p. 344)
- [[unknown-normalizing-factor]] (new) — $p(y|\theta)=q/z(\theta)$ with $z$ unknown and parameter-dependent; bridge and path sampling (pp. 345–347)
- [[hierarchical-model]] — group parameters drawn from a population distribution; the main example class (p. 326)
- [[partial-pooling-shrinkage]] — shrinkage factors $\frac{\sigma^2/n_j}{\sigma^2/n_j+\tau^2}$ near zero imply little pooling here (p. 328)
- [[mcmc]] — approximations serve as starting points and comparison points for Markov chain simulation (pp. 311, 330)

## Canonical instances
- [[eight-schools]] — boundary mode $\tau=0$ (Fig. 13.1) and the VB example (pp. 313–314, 332–335)
- [[coagulation-hierarchical-normal]] — conditional maximization, EM and normal approximation (pp. 326–330)
- [[bioassay-logistic-regression]] — EP versus mode-based approximation (pp. 341–343)
- [[unseen-species-problem]] — exercise 13.5 (pp. 349–350)

## Bridges (candidates)
- [same-math] VB lower bound $\mathrm E_g\log(p(\theta,y)/g)$ ↔ bayesian canon, variational inference and ELBO — same objective, up to the constant $\log p(y)$.
- [same-math] EM as VB with point-mass $g(\phi)$ and unconstrained $g(\gamma)$ ↔ variational inference — the author states this equivalence (p. 337).
- [structural-analogy] ABC rejection sampling ↔ prior predictive simulation — both simulate data from prior draws, but ABC keeps draws close to observed data.
- [structural-analogy] Boundary-avoiding priors for a mode ↔ penalized likelihood — the author notes that the log prior acts as a penalty (p. 311).
- [structural-analogy] Cavity/tilted distribution and moment matching ↔ Gibbs-style "all others fixed" updates — each step updates one piece in the context of the rest.

## Questions this raises
- When does the mode-centred normal fail so badly that mixture, $t$ or EP approximations become necessary, and how can one detect this without running MCMC?
- VB is said to give narrower fits than the target. How can one quantify the error beyond comparing marginal quantiles, e.g. from importance ratios?
- Why does EP lack a convergence guarantee, and how do damping and fractional EP restore stability?
- How are the weights of a normal mixture affected when modes are close, so that the "widely separated" assumption behind (13.4) fails?

## Exercises worth doing
- Ex. 13.6 (p. 350) — prove $\mathrm E_{\rm old}\log p(\gamma|\phi,y)$ is maximised at $\phi^{\rm old}$ (Jensen); the core of EM's monotonicity — difficulty: medium
- Ex. 13.9 (p. 350) — derive the EM M-step (13.14) for the hierarchical normal model and test on fake data — difficulty: medium
- Ex. 13.10 (p. 350) — set up and program VB for probit regression with latent data — difficulty: hard
- Ex. 13.4 (p. 349) — show the normal and $t$ versions of (13.10) agree — difficulty: easy
- Ex. 13.3 (p. 349) — compare rejection sampling, mode-based normal and $t_4$ importance sampling for a small logistic model — difficulty: medium
- Ex. 13.5 (pp. 349–350) — unseen species: marginal likelihood, mode, posterior predictive checks and sensitivity — difficulty: hard

## Reading notes
- Printed page = pdf − 10 (pdf 321 = printed 311). Page images printed numbers match the labels.
- The text layer shows the parameter as $\omega$ (and shows garbled symbols such as "→" for "∼"). The images show $\theta$.
- In the $V_{\rm joint}$ display (p. 324) the image has $d\theta^2$ in the denominator, although the parameter being differentiated is $\phi$. This appears to be a typo in the source; I copied it as printed and did not decide which is intended.
- In the 8-schools KL display (pp. 334–335) the image shows $p(y|\theta)$ inside the expectation, where the surrounding text (13.24) uses $p(\theta,y)$. The displayed result has $+8\log M_\tau$ and $-J\log M_\tau$ terms, and "$(y-M_\alpha)^2$" without an index $j$. I did not reproduce this formula in full.
- On p. 316 the text names the prior Gamma$(2,\frac2A)$, and the Figure 13.3 caption (p. 315) calls it "gamma with 2 degrees of freedom" and plots gamma(2, 0.1). I report the text version.
- On p. 328 the sentence about shrinkage factors (near zero) is as printed.
- Section 13.11 (bibliographic note) is only summarised, and the exercise statements are condensed. No solutions are printed in this unit.
