---
id: murphy-2023-pml2/ch12-markov-p2
work: murphy-2023-pml2
unit: "12 Markov chain Monte Carlo (part 2/2): end of 12.5 to 12.9"
pages: 524–542
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# MCMC convergence, stochastic-gradient MCMC, reversible jump and annealing

## L0 — One line
MCMC samples are only trustworthy after the chain has mixed, so we need theory and diagnostics for mixing, and extra tools (reparameterization, minibatch gradients, trans-dimensional moves, annealing) when geometry, data size, model size or multimodality break simple samplers.

## L1 — The gist (≤ 120 words)
Once a sampler is built, how do we know its samples can be trusted, and what can we do when plain MCMC fails? This unit gives mixing-time theory (eigengap, conductance). It gives practical checks: trace plots, R-hat and effective sample size. It shows a reparameterization that makes funnel-shaped posteriors easier to sample (non-centered parameterization). It also covers minibatch Langevin and HMC samplers for large data, reversible jump MCMC for models of varying dimension, and simulated annealing and parallel tempering for multimodal targets. It matters because MCMC output is valid only after convergence, and diagnosing convergence is hard in general.

**Prerequisites:** Markov chains and stationary distributions; Metropolis–Hastings and HMC basics; variance and covariance; Jacobian determinants; SGD and minibatches.

## L2 — Key ideas
- Early samples (burn-in) are usually discarded because the chain has not yet reached its stationary distribution, i.e. has not yet "forgotten" its start; the mixing time is the time this takes (p. 524–525).
- For a finite chain, mixing time is determined by the eigengap (the gap between the first two eigenvalues of the transition matrix). It is also bounded above using the conductance (a measure of how easily the chain crosses bottlenecks): low conductance means high mixing time. Distributions with well-separated modes usually have high mixing time (p. 525–526).
- Practical diagnostics are multi-chain trace plots, rank plots, R-hat (compares the variance between chains with the variance within chains; < 1.01 recommended) and split-R-hat (p. 526–529).
- Correlated samples are worth fewer than N independent ones: $N_{\rm eff}=N/\rho$ with autocorrelation time $\rho$ (p. 529–531).
- Funnel-shaped hierarchical posteriors are hard for a sampler; a non-centered parameterization (sample a standard variable $z$, then rescale) makes them easier to sample (p. 531–532).
- Stochastic-gradient MCMC replaces the $O(N)$ full gradient by an unbiased minibatch gradient costing $O(B)$ (SGLD, SG-HMC). Variance-reduced variants (SGLD-CV, SVRG-LD) reduce the minibatch noise, though SVRG needs a periodic full pass (p. 533–536).
- Reversible jump MCMC lets a chain move between models of different dimension by padding the smaller space and adding a Jacobian to the MH ratio (p. 536–539).
- Annealing smooths a multimodal target with a temperature. Simulated annealing seeks the global optimum; parallel tempering runs chains at several temperatures (p. 539–542).

## L3 — Walkthrough

### 12.5.8 (end) Marginalizing discrete variables; 12.5.9 Speeding up HMC
- HMC needs continuous, unconstrained variables. Discrete latent variables should be summed out. Figure 12.10 shows a mixture model before and after integrating out the discrete $z_i$. For an HMM one can use the forwards algorithm for $p(x_n|\theta)=\sum_{z_{1:T}}p(x_n,z_{n,1:T}|\theta)$ (p. 524).
- Remaining constrained variables are mapped by a bijector (invertible transform). Example: sample logits $\eta\in\mathbb R^K$ instead of $\pi$ in the simplex, then transform back (p. 524).
- HMC can be slowed by hard geometry (see mass-matrix estimation, §12.5.4.3) and by the cost of $\mathcal E(\theta)=-\log\tilde p(\theta)$, which is $O(N)$ when $\log\tilde p=\log p_0+\sum_n\log p(\theta_n|\theta)$ (as printed). Stochastic gradients (§12.7) address the cost (p. 524).

### 12.6 MCMC convergence
- Samples come from the stationary distribution only once the chain has "forgotten" its start. The time this takes is the **mixing time**. Samples before that are the **burn-in** and are usually discarded (p. 524).
- Example: a symmetric random walk on $\{0,\dots,20\}$ with target uniform. Starting from 10 or from 17, it takes over 200 steps to forget the start (Fig. 12.11). Proposals with larger changes can converge faster. The text cites proofs that about 7 riffle shuffles mix a 52-card deck (p. 525).
- Computing mixing time in practice can be very hard, "one of the fundamental weaknesses of MCMC" (p. 525).

### 12.6.1 Mixing rates
- Mixing time from state $x_0$, with $\delta_{x_0}$ a point mass, $T$ the transition matrix (depends on target $p^*$ and proposal $q$), and $\delta_{x_0}T^t$ the distribution after $t$ steps (p. 525):
$$\tau_\epsilon(x_0)\triangleq\min\{t:\|\delta_{x_0}(x)T^t-p^*\|_1\le\epsilon\}\tag{12.94}$$
$$\tau_\epsilon\triangleq\max_{x_0}\tau_\epsilon(x_0)\tag{12.95}$$
- It is determined by the eigengap $\gamma=\lambda_1-\lambda_2$ (first minus second eigenvalue of $T$). For a finite chain with $n$ states, $\tau_\epsilon=O\!\big(\tfrac1\gamma\log\tfrac n\epsilon\big)$ (p. 525).
- Geometric view: Figure 12.12 shows two "islands" joined by a narrow bottleneck. If fully disconnected, the chain would not be ergodic and the stationary distribution would not be unique. **Conductance** (p. 526):
$$\phi\triangleq\min_{S:\,0\le p^*(S)\le0.5}\frac{\sum_{x\in S,\,x'\in S^c}T(x\to x')}{p^*(S)}\tag{12.96}$$
- One can show $\tau_\epsilon\le O\big(\tfrac1{\phi^2}\log\tfrac n\epsilon\big)$, so low conductance means high mixing time. Distributions with well-separated modes usually mix slowly. Simple MH and Gibbs often fail there, and more advanced methods such as parallel tempering are needed (p. 526).
- *Intuition note:* If a chain must squeeze through a thin bottleneck to reach another region, it takes very long to visit both regions in the right proportions. Conductance (12.96) is the quantity that formalizes such a bottleneck, and low conductance goes with high mixing time.

### 12.6.2 Practical convergence diagnostics
Computing the mixing time is hard because $T$ is hard to compute, and diagnosing convergence is computationally intractable in general. The text follows [Veh+19] for the recommended heuristics (p. 526).

**12.6.2.1 Trace plots.** Run several chains (typically 3 or 4) from very different (overdispersed) starting points. Plot a quantity of interest. If the chains have mixed, the traces should overlap (p. 526).
- Example (from McElreath): $y_i\sim\mathcal N(\alpha,\sigma)$ with two observations $y_1=-1$, $y_2=+1$; HMC, 3 chains, 500 samples each (p. 526–527).
- Diffuse prior $\alpha\sim\mathcal N(0,1000)$, $\sigma\sim{\rm Expon}(0.0001)$ (Fig. 12.13): the traces barely overlap and HMC reports many divergences. The author's explanation: with only 2 datapoints, the likelihood does not overwhelm the prior, so the posterior is also diffuse (p. 527).
- Sensible prior $\alpha\sim\mathcal N(1,10)$, $\sigma\sim{\rm Expon}(1)$ (Fig. 12.14): traces overlap, per-chain marginals peak near the "right" place (MLE: $\alpha=0$, $\sigma=1$), and there are no divergence warnings (p. 527).
- **Trace rank plot ("trankplot")** [Veh+19]: rank every post-burn-in sample among all chains' samples, then histogram the ranks per chain. If converged, each chain's histogram should be uniform. Fig. 12.15 (diffuse prior, 3×500 = 1500 samples) shows clearly non-mixing chains; Fig. 12.16 (sensible prior) looks much better (p. 527–528).

**12.6.2.2 Estimated potential scale reduction (EPSR, R-hat).** Idea: if a chain has not mixed, the variance of all chains combined exceeds the within-chain variance. With $M$ chains of $N$ samples, $x_{nm}$ = quantity from sample $n$ of chain $m$ (p. 528–529):
$$B=\frac N{M-1}\sum_{m=1}^M(\overline x_{\cdot m}-\overline x_{\cdot\cdot})^2,\quad \overline x_{\cdot m}=\frac1N\sum_{n=1}^Nx_{nm},\ \ \overline x_{\cdot\cdot}=\frac1M\sum_{m=1}^M\overline x_{\cdot m}\tag{12.97}$$
$$W=\frac1M\sum_{m=1}^Ms_m^2,\quad s_m^2=\frac1{N-1}\sum_{n=1}^N(x_{nm}-\overline x_{\cdot m})^2\tag{12.98}$$
$$\hat V^+\triangleq\frac{N-1}{N}W+\frac1NB\tag{12.99}$$
$$\hat R\triangleq\sqrt{\hat V^+/W}\tag{12.100}$$
- $s_m^2$ is the usual unbiased variance estimate; $B$ is scaled by $N$ because it is based on the variance of means over $N$ values (p. 529).
- [Veh+19] recommend checking $\hat R<1.01$ before declaring convergence. For the univariate GMM example, the three MH samplers (Fig. 12.1) and the Gibbs sampler (Fig. 12.4) have $\hat R=1.493,\,1.039,\,1.005,\,1.007$. The diagnostic correctly flags the first two as unreliable (p. 529).
- **Split-$\hat R$**: split each chain into two halves (doubling $M$, halving $N$) before computing $\hat R$. This can detect non-stationarity within a single chain (p. 529).
- *Intuition note:* $W$ is how spread out each chain is by itself; $\hat V^+$ also counts how far apart the chain means are. If chains agree, the two are about equal and $\hat R\approx1$.

### 12.6.3 Effective sample size
- Independent samples: $\hat x=\frac1N\sum x_n$ has
$$\mathbb V[\hat x]=\frac1{N^2}\mathbb V\Big[\sum_{n=1}^Nx_n\Big]=\frac1{N^2}\sum_{n=1}^N\mathbb V[x_n]=\frac1N\sigma^2\tag{12.101}$$
 with $\sigma^2=\mathbb V[X]$ (p. 529).
- For correlated samples (p. 530):
$$\mathbb V\Big[\sum_{n=1}^Nx_n\Big]=\sum_{i=1}^N\sum_{j=1}^N{\rm Cov}[x_i,x_j]=\sum_{i=1}^N\mathbb V[x_i]+2\sum_{1\le i<j\le N}{\rm Cov}[x_i,x_j]\tag{12.102}$$
$$\mathbb V[\overline x]=\frac1{N^2}\sum_{i=1}^N\sum_{j=1}^N{\rm Cov}[x_i,x_j]\tag{12.103}$$
$${\rm corr}[x_i,x_j]=\frac{{\rm Cov}[x_i,x_j]}{\sqrt{\mathbb V[x_i]\mathbb V[x_j]}}\tag{12.104}$$
- Assuming samples are from the target, $\mathbb V[x_i]=\sigma^2$, so
$$\mathbb V[\overline x]=\frac{\sigma^2}{N^2}\sum_{i=1}^N\sum_{j=1}^N{\rm corr}[x_i,x_j]\tag{12.105}$$
- For fixed $i$, ${\rm corr}[x_i,x_j]$ usually decays as $j$ moves away from $i$. As $N\to\infty$, using ${\rm corr}[x_i,x_i]=1$ and symmetry in the lag $\ell$ (p. 531):
$$\sum_{j=1}^N{\rm corr}[x_i,x_j]\to\sum_{\ell=-\infty}^\infty{\rm corr}[x_i,x_{i+\ell}]=1+2\sum_{\ell=1}^\infty{\rm corr}[x_i,x_{i+\ell}]\tag{12.106}$$
- Under stationarity the index $i$ does not matter, so the **autocorrelation time** is
$$\rho=1+2\sum_{\ell=1}^\infty\rho(\ell)\tag{12.107}$$
 with the **autocorrelation function** (ACF) $\rho(\ell)\triangleq{\rm corr}[x_0,x_\ell]$ (12.108). The ACF can be approximated by convolving the signal with itself (p. 531).
- Fig. 12.17: the Gibbs sampler's ACF dies to 0 much faster than the MH samplers', so each Gibbs sample is "worth" more (p. 531).
- Then $\mathbb V[\overline x]=\frac{\sigma^2}{N^2}\sum_{i=1}^N\rho=\frac{\sigma^2}N\rho$. This is a factor $\rho$ larger than the independent case. Define
$$N_{\rm eff}\triangleq\frac N\rho=\frac N{1+2\sum_{\ell=1}^\infty\rho(\ell)}\tag{12.109}$$
- In practice, truncate at lag $L$, the last integer at which $\rho(L)$ is positive. With $M$ chains the numerator is $NM$ (p. 531):
$$\hat N_{\rm eff}=\frac{NM}{1+2\sum_{\ell=1}^L\hat\rho(\ell)}\tag{12.110}$$
- [Veh+19] propose more robust extensions (e.g., rank statistics) (p. 531).
- *Intuition note:* Positively correlated neighbouring samples repeat information. $N_{\rm eff}$ says how many independent samples would give the same mean-estimate variance.

### 12.6.4 Improving convergence speed
If $\hat R$ is too large or $N_{\rm eff}$ too low, try: non-centered parameterization (§12.6.5); blocked sampling (§12.3.7); Rao-Blackwellization, i.e. analytically integrating out some variables (§12.3.8); auxiliary variables (§12.4); adaptive proposals (§12.2.3.5). See [Rob+18] (p. 531–532).

### 12.6.5 Non-centered parameterizations and Neal's funnel
- Problem: in hierarchical models, parameters at one level can depend tightly on parameters one level up (examples cited: 8-schools §3.6.2.2, radon regression §15.5.2.2). Toy model (p. 532):
$$\nu\sim\mathcal N(0,3)\tag{12.111}$$
$$x\sim\mathcal N(0,\exp(\nu))\tag{12.112}$$
- The joint $p(x,\nu)$ is **Neal's funnel** (Fig. 12.18a). Samplers find it hard to descend the narrow "neck", where $\nu$ is small (p. 532).
- Equivalent **non-centered parameterization**:
$$\nu\sim\mathcal N(0,3),\quad z\sim\mathcal N(0,1),\quad x=z\exp(\nu)\tag{12.113–12.115}$$
- This is easier because $p(z,\nu)$ is a product of two independent Gaussians and $x$ is derived deterministically. Fig. 12.18 compares HMC samples from the two forms. [GMH20] discuss automatic derivation of such reparameterizations (p. 532–533).
- *Intuition note:* Instead of sampling a variable whose scale changes sharply with $\nu$, sample a fixed-scale variable $z$ and rescale it afterwards. Then $p(z,\nu)$ is a product of two independent Gaussians, which is easier to sample from.

### 12.7 Stochastic gradient MCMC
- Target $\pi(\theta)\propto p(\theta,\mathcal D)=p_0(\theta)\prod_{n=1}^Np(x_n|\theta)$ (12.116) $\propto\exp(-\mathcal E(\theta))$ (12.117), with $\mathcal E(\theta)=\sum_{n=1}^N\mathcal E_n(\theta)$ (12.118) and $\mathcal E_n(\theta)=-\log p(x_n|\theta)-\frac1N\log p_0(\theta)$ (12.119). A full energy or gradient costs $O(N)$, which does not scale to large data (p. 533).

**12.7.1 SGLD.** Langevin diffusion (p. 533):
$$d\theta_t=-\nabla\mathcal E(\theta_t)dt+\sqrt2\,dW_t\tag{12.120}$$
with $W_t$ a Wiener (Brownian) noise process. Euler discretization:
$$\theta_{t+1}\approx\theta_t-\eta_t\nabla\mathcal E(\theta_t)+\sqrt{2\eta_t}\,\mathcal N(0,\mathbf I)\tag{12.121}$$
An unbiased minibatch gradient over minibatch $\mathcal B_t$ of size $B$ costs $O(B)$:
$$\hat g(\theta_t)=\frac NB\sum_{n\in\mathcal B_t}\nabla\mathcal E_n(\theta_t)=-\frac NB\Big(\sum_{n\in\mathcal B_t}\nabla\log p(x_n|\theta_t)+\frac BN\nabla\log p_0(\theta_t)\Big)\tag{12.122}$$
$$\theta_{t+1}=\theta_t-\eta_t\hat g(\theta_t)+\sqrt{2\eta_t}\,\mathcal N(0,\mathbf I)\tag{12.123}$$
This is **SGLD** [Wel11]: identical to SGD except for added Gaussian noise. [Neg+21] analyze it and suggest $\eta_t\propto N^{-2/3}$ (p. 533).

**12.7.2 Preconditioning.** As in SGD, scaling updates can help, especially for neural networks. SGRLD [PT13] uses the Fisher information matrix, which is often hard to compute. Preconditioned SGLD [Li+16] uses an RMSprop-style diagonal approximation. SGLD-Adam [KSL21] uses an Adam-like preconditioner (p. 534).

**12.7.3 Variance reduction.** Minibatch noise variance can be large and hurt SGLD [BDM18]. SGLD-CV [Bak+17] uses a control variate with a fixed reference point $\hat\theta$, often an approximate MAP (e.g., from one SGD epoch), with $\mathcal S_t$ the minibatch (p. 534):
$$\hat\nabla_{cv}\mathcal E(\theta_t)=\nabla\mathcal E(\hat\theta)+\frac NB\sum_{n\in\mathcal S_t}\big(\nabla\mathcal E_n(\theta_t)-\nabla\mathcal E_n(\hat\theta)\big)\tag{12.124}$$
It is unbiased because the added and subtracted terms are equal in expectation:
$$\mathbb E[\hat\nabla_{cv}\mathcal E(\theta_t)]=\nabla\mathcal E(\hat\theta)+\mathbb E\Big[\frac NB\sum_{n\in\mathcal S_t}\big(\nabla\mathcal E_n(\theta_t)-\nabla\mathcal E_n(\hat\theta)\big)\Big]\tag{12.125}$$
$$=\nabla\mathcal E(\hat\theta)+\nabla\mathcal E(\theta_t)-\nabla\mathcal E(\hat\theta)=\nabla\mathcal E(\theta_t)\tag{12.126}$$
The first term needs one full pass, computed once. Drawback: $\hat\theta$ is fixed in advance. **SVRG-LD** instead refreshes a snapshot $\tilde\theta_t$ every $\tau$ steps (the epoch length):
$$\hat\nabla_{svrg}\mathcal E(\theta_t)=\nabla\mathcal E(\tilde\theta_t)+\frac NB\sum_{n\in\mathcal S_t}\big(\nabla\mathcal E_n(\theta_t)-\nabla\mathcal E_n(\tilde\theta_t)\big)\tag{12.127}$$
Algorithm 12.5 (p. 535): every $\tau$ steps set $\tilde\theta=\theta_t$ and $\tilde g=$ full-batch gradient at $\tilde\theta$. Each step, sample a minibatch, set $g_t=\tilde g+\frac NB\sum_{n\in\mathcal B_t}(\nabla\mathcal E_n(\theta_t)-\nabla\mathcal E_n(\tilde\theta))$, then $\theta_{t+1}=\theta_t-\eta_tg_t+\sqrt{2\eta_t}\mathcal N(0,\mathbf I)$. SVRG needs a full pass every $\tau$ steps. SAGA-LD avoids this by storing all $N$ gradient vectors, but the memory cost usually makes it impractical (p. 534).
- *Intuition note:* A minibatch gradient is noisy. Subtracting the same minibatch's gradient at a fixed reference point is meant to reduce the variance (it is a control variate), while adding back the full gradient there keeps the estimate unbiased (12.126).

**12.7.4 SG-HMC.** Leapfrog updates (p. 535):
$$v_{t+1/2}=v_t-\tfrac\eta2\nabla\mathcal E(\theta_t)\tag{12.128}$$
$$\theta_{t+1}=\theta_t+\eta v_{t+1/2}=\theta_t+\eta v_t-\tfrac\eta2\nabla\mathcal E(\theta_t)\tag{12.129}$$
$$v_{t+1}=v_{t+1/2}-\tfrac\eta2\nabla\mathcal E(\theta_{t+1})=v_t-\tfrac\eta2\nabla\mathcal E(\theta_t)-\tfrac\eta2\nabla\mathcal E(\theta_{t+1})\tag{12.130}$$
Replacing full gradients by stochastic ones $g(\theta,\xi)$, with independent randomness $\xi_t,\xi_{t+1/2}$ (e.g., batch indices):
$$\theta_{t+1}=\theta_t+\eta v_t-\tfrac{\eta^2}2g(\theta_t,\xi_t)\tag{12.131}$$
$$v_{t+1}=v_t-\tfrac\eta2g(\theta_t,\xi_t)-\tfrac\eta2g(\theta_{t+1},\xi_{t+1/2})\tag{12.132}$$
[ZG21] show that, even without the MH rejection step, this approximates the posterior well (small Wasserstein-2 distance) when the energy is strongly convex. Variance reduction (§12.7.3) can improve it considerably (p. 535).

**12.7.5 Underdamped Langevin dynamics (ULD).** With force $g(\theta_t)=\nabla\mathcal E(\theta_t)$ and friction $\gamma>0$ (p. 535–536):
$$d\theta_t=v_tdt,\qquad dv_t=-g(\theta_t)dt-\gamma v_tdt+\sqrt{2\gamma}\,dW_t\tag{12.133}$$
This is Langevin dynamics plus a momentum term. Integrators for ULD are accurate to second order, versus first order for standard (overdamped) Langevin, so the latter needs more steps for a given accuracy (p. 536).

### 12.8 Reversible jump (transdimensional) MCMC
- Setting: models $m$ with unknowns $x_m\in\mathcal X_m=\mathbb R^{n_m}$ (e.g., mixtures with unknown number of components). Sampling the model index and all parameters in the product space $\prod_m\mathcal X_m$ is very inefficient and works only for finite $M$. It is more parsimonious to sample in the union space $\mathcal X=\cup_{m=1}^M\{m\}\times\mathcal X_m$ (p. 536).
- Difficulty: the MH ratio would compare densities on spaces of different dimension, which is not well defined. The analogy: a density on a sphere vs. one on a circle. Solution [Gre95] (**RJMCMC**): augment the lower-dimensional space with extra random variables so both have a common measure (Fig. 12.19: map a 1-d density to 2-d to compare point-wise) (p. 536–537).

**12.8.1 Basic idea** (following [And+03]). Extend $\mathcal X_m,\mathcal X_n$ to $\mathcal X_{m,n}=\mathcal X_m\times\mathcal U_{m,n}$ and $\mathcal X_{n,m}=\mathcal X_n\times\mathcal U_{n,m}$. Define a deterministic, differentiable, invertible map (p. 536):
$$(x_m,u_{m,n})=f_{n\to m}(x_n,u_{n,m})=\big(f^x_{n\to m}(x_n,u_{n,m}),\,f^u_{n\to m}(x_n,u_{n,m})\big)\tag{12.134}$$
$$f_{m\to n}(f_{n\to m}(x_n,u_{n,m}))=(x_n,u_{n,m})\tag{12.135}$$
and proposals $q_{n\to m}(u_{n,m}|n,x_n)$, $q_{m\to n}(u_{m,n}|m,x_m)$. From $(n,x_n)$: draw $u_{n,m}\sim q_{n\to m}$, compute $(x_m,u_{m,n})=f_{n\to m}(x_n,u_{n,m})$, and accept with probability
$$A_{n\to m}=\min\Big\{1,\frac{p(m,x^*_m)}{p(n,x_n)}\times\frac{q(n|m)}{q(m|n)}\times\frac{q_{m\to n}(u_{m,n}|m,x^*_m)}{q_{n\to m}(u_{n,m}|n,x_n)}\times|\det\mathbf J_{f_{m\to n}}|\Big\}\tag{12.136}$$
where $x^*_m=f^x_{n\to m}(x_n,u_{n,m})$ and $J_{f_{m\to n}}$ is the Jacobian (12.137, as printed: $\partial f_{n\to m}(x_m,u_{m,n})/\partial(x_m,u_{m,n})$) (p. 536–537).

**12.8.2 Example** [AFD01]. RBF network for nonlinear regression (p. 537):
$$f(x)=\sum_{j=1}^ka_j\mathcal K(\|x-\mu_j\|)+\beta^\top x+\beta_0+\epsilon\tag{12.138}$$
with kernel $\mathcal K$, $k$ basis functions and Gaussian noise $\epsilon$. $k=0$ gives linear regression. In Fig. 12.20, $p(k|\mathcal D)$ has most posterior support at $k=2$, which fits the two "bumps" in the data (p. 537).
- **Split move** (p. 538): $\mu_1=\mu-u_{n,n+1}\beta$, $\mu_2=\mu+u_{n,n+1}\beta$ (12.139), with $\beta$ a proposal parameter and $u$ drawn from e.g. a uniform. **Merge move**: $\mu=(\mu_1+\mu_2)/2$ (12.140), with $\mu_1$ chosen at random and $\mu_2$ its nearest neighbour. Reversibility requires $\|\mu_1-\mu_2\|<2\beta$.
$$A_{split}=\min\Big\{1,\frac{p(k+1,\mu_{k+1})}{p(k,\mu_{k+1})}\times\frac{1/(k+1)}{1/k}\times\frac1{p(u_{n,m})}\times|\det\mathbf J_{split}|\Big\}\tag{12.141}$$
 where $1/k$ is the probability of choosing one of $k$ bases uniformly (as printed).
$$\mathbf J_{split}=\frac{\partial(\mu_1,\mu_2)}{\partial(\mu,u_{n,m})}=\det\begin{pmatrix}1&1\\-\beta&\beta\end{pmatrix}\tag{12.142}$$
 so $|\det\mathbf J_{split}|=2\beta$ (p. 538–539). (Added step: $1\cdot\beta-1\cdot(-\beta)=2\beta$.)
$$A_{merge}=\min\Big\{1,\frac{p(k-1,\mu_{k-1})}{p(k,\mu_k)}\times\frac{1/(k-1)}{1/k}\times|\det\mathbf J_{merge}|\Big\},\quad|\det\mathbf J_{merge}|=\frac1{2\beta}\tag{12.143}$$
- Algorithm 12.6 (one step, model index $k$): draw $u\sim U(0,1)$; birth if $u\le b_k$; death if $u\le b_k+d_k$; split if $u\le b_k+d_k+s_k$; merge if $u\le b_k+d_k+s_k+m_k$; otherwise update parameters (random-walk MH). Here $b_k,d_k,s_k,m_k$ are move probabilities (p. 539).

**12.8.3 Discussion.** RJMCMC is tricky to implement. If continuous parameters can be integrated out ("collapsed RJMCMC"), only a discrete space remains and no change of measure is needed. Example: fix the centers $\mu_j$ in (12.138) (from data samples or K-means). The model is then linear and parameters can be integrated out, leaving a discrete variable-selection problem [Den+02]. Chapter 31 (Bayesian nonparametrics) allows infinitely many models and is often easier computationally, "surprisingly" (p. 539).

### 12.9 Annealing methods
Idea, by analogy with heating then slowly cooling metal: use a temperature to smooth a multimodal distribution, then cool it to recover the bumpy original. It is first explained for optimization (p. 539).

**12.9.1 Simulated annealing** [KJV83; LA87]. A variant of MH aimed at the global optimum of a black-box function. Define (p. 540)
$$p_T(x)=\exp(-\mathcal E(x)/T)\tag{12.144}$$
with $T$ reduced over time. Example peaks function (Fig. 12.21):
$$p(x,y)\propto\Big|3(1-x)^2e^{-x^2-(y+1)^2}-10\Big(\frac x5-x^3-y^5\Big)e^{-x^2-y^2}-\frac13e^{-(x+1)^2-y^2}\Big|\tag{12.145}$$
- At $T\gg1$ the surface is roughly flat, so moving around is easy. As $T$ falls, the largest peaks grow and the smallest vanish (Fig. 12.22). By cooling slowly enough one can "track" the largest peak. This is a continuation method (p. 540).
- Proposal $x'\sim q(\cdot|x_t)$, often a random walk $x'=x_t+\epsilon_{t+1}$, $\epsilon\sim\mathcal N(0,\Sigma)$. Acceptance (p. 541):
$$\alpha_{t+1}=\exp\big(-(\mathcal E(x')-\mathcal E(x_t))/T_t\big)\tag{12.146}$$
 Accept with probability $\min(1,\alpha_{t+1})$, else stay. Lower-energy moves are always accepted; higher-energy ("downhill in probability") moves may be accepted, less often as $T$ drops (p. 541).
- Cooling schedule: a logarithmic schedule $T_t\propto1/\log(t+1)$ is guaranteed [Haj88] to find the global optimum "under certain assumptions", but is often too slow. Common practice is exponential: $T_{t+1}=\gamma T_t$, $\gamma\in(0,1]$. Cooling too fast can trap the chain in a local maximum; too slow wastes time. The best schedule is hard to determine, a main drawback (p. 541–542).
- Fig. 12.23: $\gamma=0.9$, Gaussian random-walk proposal with $\sigma=10$ on the peaks function; samples concentrate near the global optimum (peak on the middle right) (p. 542).

**12.9.2 Parallel tempering.** Run chains in parallel at different temperatures and let a chain sample from a neighbouring-temperature chain. High-temperature chains make long-distance moves and influence the colder ones. Details are in [ED05; Kat+06] (p. 542).
- *Intuition note:* A high-temperature chain targets a smoothed distribution and can make long-distance moves through the state space. Letting a chain sample from a neighbouring-temperature chain lets these moves influence the colder chains.

## Toy example (ours)
**R-hat by hand.** $M=2$ chains, $N=4$ samples of some quantity.
- Chain 1: 0, 1, 2, 1. Mean 1; deviations $-1,0,1,0$; sum of squares 2; $s_1^2=2/3$.
- Chain 2: 4, 5, 6, 5. Mean 5; $s_2^2=2/3$.
- $\overline x_{\cdot\cdot}=3$. $B=\frac4{1}\big((1-3)^2+(5-3)^2\big)=4\cdot8=32$. $W=\frac23$.
- $\hat V^+=\frac34\cdot\frac23+\frac14\cdot32=0.5+8=8.5$. $\hat R=\sqrt{8.5/(2/3)}=\sqrt{12.75}\approx3.57$, far above 1.01: not mixed.
- Replace chain 2 by 2, 1, 0, 1 (mean 1, $s_2^2=2/3$). Then $B=0$, $\hat V^+=0.5$, $\hat R=\sqrt{0.75}\approx0.87$. Chains agree. With tiny $N$, $\hat R$ can fall below 1 because of the factor $(N-1)/N$.

**ESS by hand.** If $N=100$, $\rho(1)=0.5$ and all other $\rho(\ell)=0$, then $\rho=1+2(0.5)=2$ and $N_{\rm eff}=100/2=50$.

## Concepts
- [[convergence-diagnostics-rhat-ess-divergences]] — checks that chains mixed: trace plots, rank plots, $\hat R$, split-$\hat R$, $N_{\rm eff}$ (p. 526–531)
- [[markov-chain-monte-carlo-mcmc]] — here with focus on when its samples are valid (p. 524)
- [[hamiltonian-monte-carlo-hmc-nuts]] — here: needs discrete variables marginalized and unconstrained continuous ones (p. 524)
- [[metropolis-hastings]] — basis of RJMCMC and simulated annealing acceptance rules (p. 536, 541)
- [[hierarchical-multilevel-model]] — source of funnel geometry (p. 532)
- [[burn-in]] (new) — initial samples before stationarity, discarded (p. 524)
- [[mixing-time]] (new) — steps until the chain's distribution is within $\epsilon$ of $p^*$ from the worst start, (12.94–12.95) (p. 525)
- [[eigengap]] (new) — $\lambda_1-\lambda_2$ of $T$; $\tau_\epsilon=O(\frac1\gamma\log\frac n\epsilon)$ (p. 525)
- [[conductance]] (new) — bottleneck measure (12.96); low conductance implies high mixing time (p. 526)
- [[trace-plot]] (new) — traces of several overdispersed chains; should overlap (p. 526)
- [[autocorrelation-time]] (new) — $\rho=1+2\sum_\ell\rho(\ell)$; $N_{\rm eff}=N/\rho$ (p. 531)
- [[non-centered-parameterization]] (new) — sample standardized $z$ and set $x=z\exp(\nu)$ (p. 532)
- [[stochastic-gradient-langevin-dynamics]] (new) — SGD step plus Gaussian noise using minibatch gradients (p. 533)
- [[control-variate-gradient-svrg]] (new) — reference-point gradient correction, unbiased (p. 534)
- [[reversible-jump-mcmc]] (new) — trans-dimensional MH with padding variables and Jacobian (p. 536)
- [[simulated-annealing]] (new) — MH with $p_T=\exp(-\mathcal E/T)$ and falling $T$ (p. 540)
- [[parallel-tempering]] (new) — chains run in parallel at different temperatures; a chain can sample from a neighbouring-temperature chain (p. 542)

## Canonical instances
- [[random-walk-on-integers]] — uniform target on $\{0,\dots,20\}$ takes over 200 steps to forget its start (p. 525)
- [[univariate-gaussian-two-points-diffuse-prior]] — diffuse prior gives traces that barely overlap and many HMC divergences; a sensible prior fixes it (p. 526–528)
- [[neals-funnel]] — hierarchical toy model that is hard for a sampler (Fig. 12.18 uses HMC); the non-centered form makes it easier to sample (p. 532)
- [[rbf-network-rjmcmc]] — posterior over number of basis functions $k$, most support at $k=2$ (p. 537–539)
- [[peaks-function-annealing]] — 2-d peaky target for simulated annealing (p. 540–542)

## Bridges (candidates)
- [same-math] SGLD update (12.123) ↔ optimization: SGD with an added Gaussian noise term — the text itself says the update is identical to SGD plus noise.
- [same-math] SGLD-CV / SVRG gradient (12.124) ↔ Monte Carlo variance reduction: a control variate subtracts a correlated term of known mean.
- [structural-analogy] $N_{\rm eff}=N/\rho$ ↔ time-series analysis: autocorrelation reduces the information in $N$ observations.
- [structural-analogy] Non-centered parameterization ↔ variational inference: reparameterizing a random variable as a deterministic transform of fixed noise (canon link; not stated in this unit).
- [metaphor] Simulated annealing temperature ↔ statistical physics: heating and slowly cooling a solid to a minimum-energy state.
- [structural-analogy] RJMCMC change of measure ↔ change of variables with Jacobian determinant in probability densities.

## Questions this raises
- When the transition matrix is unknown, how reliable are $\hat R$ and $N_{\rm eff}$ at detecting a chain stuck in one mode, given that diagnosing convergence is intractable in general?
- How does the bias of SGLD with a fixed step size $\eta_t$ and noisy $\hat g$ trade off against its $O(B)$ cost? The text only cites [Neg+21] for analysis.
- How should the proposal parameter $\beta$ and the move probabilities $b_k,d_k,s_k,m_k$ be chosen in RJMCMC?
- Is there a principled way to choose a cooling schedule, or the temperature ladder in parallel tempering?

## Reading notes
- This part starts at the end of the section preceding §12.5.9 (its heading is not on these pages; the passage is on marginalizing discrete latents, p. 524) and ends with §12.9.2 on parallel tempering (p. 542). The earlier sections (12.1–12.5, e.g., Langevin SDE 12.83, Figs. 12.1 and 12.4) are in part 1 and referenced here only by number. Printed page = pdf page − 34.
- Algorithm 12.5, line 5, is printed as $\tilde g=\sum_nE_n(\tilde\theta)$ without a gradient symbol; the text and (12.127) make clear it should be the gradient. In (12.137) the Jacobian subscript is printed $f_{m\to n}$ but the numerator is $f_{n\to m}$. In (12.141), $p(k,\mu_{k+1})$ is as printed. In (12.139) the index $u_{n,n+1}$ is used and later $u_{n,m}$.
- The notation $\rho$ is used both for the autocorrelation time (12.107) and the ACF $\rho(\ell)$.
- The text says "variance $\nu$" for the funnel, but (12.112) and (12.115) are consistent with $\exp(\nu)$ being the scale; the page does not state whether $\mathcal N(\cdot,\cdot)$'s second argument is variance or standard deviation, for either (0,3) or $\exp(\nu)$.
- The eigengap bound and the conductance bound are stated without proof ("one can show"). The sentence "for any constant $\epsilon>0$" before (12.94) is as printed. Figure values for $p(k|\mathcal D)$ (Fig. 12.20d) were not used beyond the text's statement.
