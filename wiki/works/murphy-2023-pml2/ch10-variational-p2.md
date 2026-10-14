---
id: murphy-2023-pml2/ch10-variational-p2
work: murphy-2023-pml2
unit: "Chapter 10 (part 2/2): Variational inference, from the end of §10.2.3.1 to §10.7.6"
pages: 455-482
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Variational inference, part 2: control variates, CAVI, VB(EM), tighter bounds, wake-sleep, EP

## L0 — One line
Beyond plain gradient ascent on the ELBO, one can optimise a mean-field posterior factor by factor (CAVI, with update $q_j\propto\exp\mathbb E[\log\tilde p]$), improve the family or the bound, replace the ELBO by wake-sleep objectives, or use expectation propagation (EP), which works with $D_{\mathbb{KL}}(p\|q)$ locally.

## L1 — The gist (≤ 120 words)
This part asks how to do variational inference (VI) more cleverly than plain gradient ascent on the ELBO. It first reduces gradient variance with control variates, then derives coordinate ascent VI (CAVI) for mean-field posteriors, with examples (Ising denoising, a Gaussian, Gaussian mixtures) and message passing. It then lists richer posteriors, tighter bounds (IWAE, EUBO), the wake-sleep family that avoids ELBO training, and expectation propagation, which can be seen as a local approximation to minimising KL(p‖q). It matters because mean field often underestimates uncertainty and ELBO training works poorly with discrete latents, which motivates these alternatives.

**Prerequisites:** KL divergence and its asymmetry; ELBO; exponential family and conjugacy; Dirichlet/Gaussian/gamma/Wishart basics; importance sampling; Jensen's inequality; digamma function.

## L2 — Key ideas
- Control variates subtract a zero-mean score-function baseline from the score-function gradient estimator, cutting its variance; the optimal constant is a covariance ratio (p. 455).
- Under mean field, the ELBO optimum for one factor with the others fixed is $q_j\propto\exp(\mathbb E[\log\tilde p(z_j,z_{\rm mb_j})])$. CAVI cycles through these updates, and the factor forms (free-form VI) come out of the log joint (pp. 456–457).
- Worked CAVI/VB examples: Ising denoising gives $\mu_i=\tanh(a_i)$ with damping (p. 459). A Gaussian with unknown mean and precision gives Gaussian × gamma factors, but the result is more compact than the exact posterior (pp. 460–462).
- VBEM for GMMs averages over parameters in the E step. With a sparse Dirichlet prior this "kills off" clusters (rich-get-richer), which can choose the number of clusters, though this "pruning" can be undesirable (pp. 464–468).
- VMP generalises CAVI to models whose full conditionals are conjugate, by passing expected sufficient statistics; autoconj derives the updates automatically for conditionally conjugate directed models (pp. 470–471).
- More accurate posteriors: structured mean field, auxiliary variables, flows, implicit posteriors, VI+MCMC (pp. 471–473). Tighter bounds: IWAE, TVO, EUBO (pp. 473–475).
- Wake-sleep (in its reweighted form), with wake, sleep and daydream updates, fits $\theta$ and $\phi$ without a single objective, so convergence is unclear. It handles discrete latents without reparameterisation (pp. 475–478).
- EP can be seen as a local approximation to minimising $D_{\mathbb{KL}}(p\|q)$, using cavity and tilted distributions. It is a batch-safe generalisation of ADF, can be unstable (damping helps), and has power-EP and stochastic-EP variants (pp. 478–482).

## L3 — Walkthrough

### 10.2.3.1 (end) and 10.2.3.2 Variance reduction with control variates
- The Monte Carlo score-function gradient is $\widehat{\nabla_\psi \text{Ł}}(\psi_t)=\frac1S\sum_{s}\tilde{\mathcal L}(\psi,z_s)\nabla_\psi\log q_\psi(z_s)|_{\psi=\psi_t}$ (10.67); it can be given to any optimiser such as SGD or Adam (p. 455). ($\tilde{\mathcal L}$ is defined earlier in the chapter, not on these pages.)
- This estimator has large variance in practice, so use control variates (CV) (p. 455). The naive estimator for component $i$ is
$$\widehat{\nabla_{\psi_i}\text{Ł}}^{\rm naive}=\tfrac1S\sum_s\tilde g_i(z_s),\quad \tilde g_i=g_i\times\tilde{\mathcal L}(\psi,z),\quad g_i=\nabla_{\psi_i}\log q_\psi(z)\tag{10.68–10.70}$$
- CV version, with baseline $b_i$ and constant $c_i$: $\tilde g_i^{cv}=\tilde g_i+c_i(\mathbb E[b_i]-b_i)$ (10.71).
- Choose the score function as baseline, $b_i=g_i$. It is correlated with $\tilde g_i$, and $\mathbb E[b_i]=0$ because the expected score is zero (Eq. 3.44) (p. 455). Then
$$\tilde g_i^{cv}=\tilde g_i-c_ig_i=g_i(\tilde{\mathcal L}-c_i)\tag{10.72}$$
$$\widehat{\nabla_{\psi_i}\text{Ł}}^{cv}=\tfrac1S\sum_s g_i(z_s)\,(\tilde{\mathcal L}(\psi,z_s)-c_i)\tag{10.73}$$
- One can show the variance-minimising constant is $c_i=\mathrm{Cov}[g_i\tilde{\mathcal L},g_i]/\mathbb V[g_i]$ (10.74); details are in the cited [TND21] (p. 455).

*Intuition note.* Subtracting something that has mean zero but moves with the noisy term leaves the average unchanged while cancelling part of the noise. $c_i$ sets how much to subtract.

### 10.3 Coordinate ascent VI (CAVI)
- Mean field: assume independence of all latents, $q_\psi(z)=\prod_{j=1}^Jq_j(z_j)$ (10.75), with $q_j(z_j)$ short for $q_{\psi_j}(z_j)$ (p. 456).
- The ELBO becomes $\text{Ł}(\psi)=\int q_\psi(z)\log p_\theta(x,z)dz+\sum_j\mathbb H(q_j)$ (10.76), since the entropy of a product is the sum of entropies. The first term often decomposes according to the Markov properties of the graphical model. This allows coordinate ascent (CAVI), an alternative to gradient-based VI (p. 456).

### 10.3.1 Derivation of CAVI
- Take 3 discrete latents and write $\tilde p(z)=p_\theta(z,x)$:
$$\text{Ł}(q_1,q_2,q_3)=\sum_{z_1,z_2,z_3}q_1q_2q_3\log\tilde p(z_1,z_2,z_3)+\sum_{j=1}^3\mathbb H(q_j)\tag{10.77}$$
- Optimise one $q_i$ at a time, keeping the others fixed. For $q_3$ (p. 456):
$$\text{Ł}_3(q_3)=\sum_{z_3}q_3(z_3)\Big[\sum_{z_1,z_2}q_1q_2\log\tilde p\Big]+\mathbb H(q_3)+\text{const}=\sum_{z_3}q_3[g_3-\log q_3]+\text{const}\tag{10.78–10.79}$$
$$g_3(z_3)\triangleq\sum_{z_1,z_2}q_1(z_1)q_2(z_2)\log\tilde p(z_1,z_2,z_3)=\mathbb E_{z_{-3}}[\log\tilde p]\tag{10.80}$$
 $g_3$ is read as an expected negative energy (log probability). Define $\tilde f_3=\exp(g_3)$ (10.81), normalised as $f_3=\tilde f_3/\sum_{z_3'}\tilde f_3\propto\exp(g_3)$ (10.82) (p. 456).
- Then $\text{Ł}_3(q_3)=\sum q_3[\log f_3-\log q_3]+\text{const}=-D_{\mathbb{KL}}(q_3\|f_3)+\text{const}$ (10.83). KL is minimal (0) at $q_3=f_3$, so $q_3^*=f_3$ (p. 457).
- Markov chain case $z_1\to z_2\to z_3$, so $z_1\perp z_3|z_2$: $\log\tilde p(z_1,z_2,z_3)=\log\tilde p(z_2,z_3|z_1)+\log\tilde p(z_1)$, and the last term does not involve $q_3$. Hence
$$\text{Ł}_3=\sum_{z_3}q_3\Big[\sum_{z_2}q_2\log\tilde p(z_2,z_3)\Big]+\mathbb H(q_3)+\text{const},\quad f_3(z_3)\propto\exp\big(\mathbb E_{z_{\rm mb_3}}[\log\tilde p(z_2,z_3)]\big)\tag{10.84–10.86}$$
 with $z_{\rm mb_3}=z_2$ the Markov blanket of $z_3$ (p. 457).
- General rule for group $j$ of variables:
$$q_j(z_j)\propto\exp\big[\mathbb E_{z_{\rm mb_j}}\log\tilde p(z_j,z_{\rm mb_j})\big]\tag{10.87}$$
 The author compares it to the Gibbs sampling equation (12.19) (p. 457).
- Algorithm 10.4 (CAVI): initialise all $q_j$; for $t=1{:}T$, for $j=1{:}J$ compute $g_j(z_j)=\mathbb E_{z_{\rm mb}}[\log\tilde p]$ and set $q_j\propto\exp(g_j)$. (The printed pseudocode mixes indices $i$ and $j$.) The author states convergence is guaranteed since the bound is concave wrt each factor [Bis06, p. 466] (p. 457).
- Free-form VI: the functional forms of the $q_i$ are not fixed in advance but determined by the log joint. Fixed-form VI instead chooses a distribution type (p. 457).

*Intuition note.* Each factor is set to the "average-field" version of the joint, with the other factors' uncertainty averaged out. Because this equals minimising a KL to $f_j$, each coordinate step cannot lower the ELBO.

### 10.3.2 Example: CAVI for the Ising model
- Setting: binary $z_i\in\{-1,+1\}$ on a 2d grid (Fig. 10.8), used for image denoising; $x_i\in\mathbb R$ is the noisy pixel. Local evidence $L_i(z_i)\triangleq\log p(x_i|z_i)$, so $p(x|z)=\prod_ip(x_i|z_i)=\exp(\sum_iL_i(z_i))$ (10.88) (p. 458).
- Prior: $p(z)=\frac1{Z_0}e^{-\mathcal E_0(z)}$, $\mathcal E_0(z)=-\sum_{i\sim j}W_{ij}z_iz_j$ (10.89–10.90). Posterior $p(z|x)=\frac1{Z(x)}e^{-\mathcal E(z)}$, $\mathcal E=\mathcal E_0-\sum_iL_i(z_i)$ (10.91–10.92) (p. 458).
- Approximation: $q(z)=\prod_i\mathrm{Ber}(z_i|\mu_i)$, $\mu_i=\mathbb E_{q_i}[z_i]$ (10.93) (p. 458).
- Dropping terms without $z_i$: $\log\tilde p(z)=z_i\sum_{j\in{\rm nbr}_i}W_{ij}z_j+L_i(z_i)+\text{const}$ (10.94). So $q_i(z_i)\propto\exp\big(z_i\sum_jW_{ij}\mu_j+L_i(z_i)\big)$ (10.95): neighbours' states are replaced by their average values, so binary variables become continuous ones (p. 459).
- Let $m_i=\sum_{j\in{\rm nbr}_i}W_{ij}\mu_j$ and $L_i^\pm=L_i(\pm1)$. Then
$$q_i(z_i{=}1)=\frac{e^{m_i+L_i^+}}{e^{m_i+L_i^+}+e^{-m_i+L_i^-}}=\frac1{1+e^{-2m_i+L_i^--L_i^+}}=\sigma(2a_i),\quad a_i\triangleq m_i+0.5(L_i^+-L_i^-)\tag{10.96–10.97}$$
 and $q_i(z_i{=}-1)=\sigma(-2a_i)$.
- New mean: $\mu_i=q_i(+1)-q_i(-1)=\frac1{1+e^{-2a_i}}-\frac1{1+e^{2a_i}}=\frac{e^{a_i}}{e^{a_i}+e^{-a_i}}-\frac{e^{-a_i}}{e^{-a_i}+e^{a_i}}=\tanh(a_i)$ (10.98–10.99) (p. 459).
- Fixed point: $\mu_i^t=\tanh\big(\sum_jW_{ij}\mu_j^{t-1}+0.5(L_i^+-L_i^-)\big)$ (10.100). Damped version following [MWJ99]: $\mu_i^t=(1-\lambda)\mu_i^{t-1}+\lambda\tanh(\cdot)$, $0<\lambda<1$ (10.101). Updates may be parallel or asynchronous (p. 459).
- Fig. 10.9: $W_{ij}=1$, parallel updates, $\lambda=0.5$, Gaussian noise $\sigma=2$; without damping one tends to get "checkerboard" artifacts (pp. 459–460).

### 10.3.3 Variational Bayes (VB)
- Parameters $\theta$ are treated as latent variables, and VI on $p(\theta|\mathcal D)\propto p(\theta)p(\mathcal D|\theta)$ is called variational Bayes (p. 459).
- Assuming no latent variables other than the shared global parameters: $p(\theta,\mathcal D)=p(\theta)\prod_np(\mathcal D_n|\theta)$ (10.102) (Fig. 10.5a). Maximise $\text{Ł}(\psi_\theta|\mathcal D)=\mathbb E_{q}[\log p(\theta,\mathcal D)]+\mathbb H(q)$ (10.103) with $q(\theta|\psi_\theta)=\prod_jq(\theta_j|\psi_{\theta_j})$ (10.104); each $\psi_{\theta_j}$ is updated by CAVI (p. 460).

### 10.3.4 Example: VB for a univariate Gaussian
- Likelihood $\prod_n\mathcal N(x_n|\mu,\lambda^{-1})$ ($\lambda$ = precision). Conjugate prior $p(\mu,\lambda)=\mathcal N(\mu|\mu_0,(\kappa_0\lambda)^{-1})\mathrm{Ga}(\lambda|a_0,b_0)$ (10.105). The exact posterior is known (Sec. 3.4.3.3), but here $q(\mu,\lambda)=q(\mu|\psi_\mu)q(\lambda|\psi_\lambda)$ (10.106). The optimal forms "fall out" and are Gaussian and gamma (p. 460).
- Target: $\log\tilde p(\mu,\lambda)=\frac N2\log\lambda-\frac\lambda2\sum_n(x_n-\mu)^2-\frac{\kappa_0\lambda}2(\mu-\mu_0)^2+\frac12\log(\kappa_0\lambda)+(a_0-1)\log\lambda-b_0\lambda+\text{const}$ (10.107–10.108) (p. 461).
- Update $q(\mu)$: $\log q(\mu)=\mathbb E_{q(\lambda)}[\log p(\mathcal D|\mu,\lambda)+\log p(\mu|\lambda)]+\text{const}=-\frac{\mathbb E[\lambda]}2\{\kappa_0(\mu-\mu_0)^2+\sum_n(x_n-\mu)^2\}+\text{const}$ (10.109–10.110). Completing the square, $q(\mu)=\mathcal N(\mu|\mu_N,\kappa_N^{-1})$ with $\mu_N=\frac{\kappa_0\mu_0+N\bar x}{\kappa_0+N}$, $\kappa_N=(\kappa_0+N)\mathbb E_{q(\lambda)}[\lambda]$ (10.111). $\mathbb E[\lambda]$ is not yet known (p. 461).
- Update $q(\lambda)$: $\log q(\lambda)=(a_0-1)\log\lambda-b_0\lambda+\frac12\log\lambda+\frac N2\log\lambda-\frac\lambda2\mathbb E_{q(\mu)}[\kappa_0(\mu-\mu_0)^2+\sum_n(x_n-\mu)^2]+\text{const}$ (10.112–10.113). This is a gamma log-density: $q(\lambda)=\mathrm{Ga}(\lambda|a_N,b_N)$, $a_N=a_0+\frac{N+1}2$, $b_N=b_0+\frac12\mathbb E_{q(\mu)}[\kappa_0(\mu-\mu_0)^2+\sum_n(x_n-\mu)^2]$ (10.114–10.115) (p. 461).
- Expectations: $\mathbb E[\mu]=\mu_N$ (10.116), $\mathbb E[\mu^2]=\frac1{\kappa_N}+\mu_N^2$ (10.117), $\mathbb E[\lambda]=a_N/b_N$ (10.118). Explicit updates: $\mu_N=\frac{\kappa_0\mu_0+N\bar x}{\kappa_0+N}$ (10.119), $\kappa_N=(\kappa_0+N)\frac{a_N}{b_N}$ (10.120), $a_N=a_0+\frac{N+1}2$ (10.121), and
$$b_N=b_0+\tfrac12\kappa_0(\mathbb E[\mu^2]+\mu_0^2-2\mathbb E[\mu]\mu_0)+\tfrac12\sum_n\big(x_n^2+\mathbb E[\mu^2]-2\mathbb E[\mu]x_n\big)\tag{10.122}$$
 So $\mu_N,a_N$ are fixed constants and only $\kappa_N,b_N$ are updated iteratively; the author notes their fixed points could be solved analytically (p. 462).
- Illustration (Fig. 10.10, converged after 5 iterations): the final approximation is reasonably close to the exact posterior but more "compact". Mean field often underestimates posterior uncertainty (reasons in Sec. 5.1.4.1) (p. 462).
- Lower bound: $\text{Ł}\le\log p(\mathcal D)=\log\iint p(\mathcal D|\mu,\lambda)p(\mu,\lambda)d\mu d\lambda$ (10.123). Three uses: assess convergence; check code (it should increase monotonically, otherwise there is a bug); approximate the marginal likelihood for model selection or empirical Bayes (pp. 462–463). Here $\text{Ł}=\text{const}+\frac12\ln\frac1{\kappa_N}+\ln\Gamma(a_N)-a_N\ln b_N$ (10.124) (p. 463).

*Intuition note.* Each factor sees the other only through an expectation ($\mathbb E[\lambda]$, $\mathbb E[\mu^2]$). The two updates therefore chase each other until stable. The factorisation forces $\mu$ and $\lambda$ to be independent; the author notes that mean field often underestimates posterior uncertainty (reasons are in Sec. 5.1.4.1, not on these pages).

### 10.3.5 Variational Bayes EM (VBEM)
- Local hidden $z_n$ plus global $\theta$ (Fig. 10.5b); $p(h,\mathcal D)=p(\theta)\prod_np(z_n|\theta)p(x_n|z_n,\theta)$ (10.125). Mean field: $q(\theta,z_{1:N})=q(\theta|\psi_\theta)\prod_nq(z_n|\psi_n)$ (10.126); ELBO (10.127) (pp. 463–464).
- Alternate: optimise the $q_n(z_n)$ in parallel with $q(\theta)$ fixed, then $q(\theta)$ with the $q_n$ fixed. This is VBEM [BG06]. Unlike regular EM, the E step averages out parameters (no point estimate) and the M step updates parameter-posterior parameters with expected sufficient statistics (p. 464).
- With $q(\theta)=\delta(\theta-\hat\theta)$ the ELBO becomes the LVM ELBO $\mathbb E_{q(z_{1:N})}[\log p(\theta,\mathcal D,z_{1:N})-\log q(z_{1:N})]$ (10.128), optimised by variational EM (VEM). VEM is simpler: the E step computes $q(z_n|x_n,\hat\theta)$ rather than $\mathbb E_\theta[q(z_n|x_n,\theta)]$ (p. 464).

### 10.3.6 Example: VBEM for a GMM
- Model: $p(z,x|\theta)=\prod_n\prod_k\pi_k^{z_{nk}}\mathcal N(x_n|\mu_k,\Lambda_k^{-1})^{z_{nk}}$ (10.129), with conjugate prior $p(\theta)=\mathrm{Dir}(\pi|\breve\alpha)\prod_k\mathcal N(\mu_k|\breve m,(\breve\kappa\Lambda_k)^{-1})\mathrm{Wi}(\Lambda_k|\breve L,\breve\nu)$ (10.130); symmetric $\breve\alpha=\alpha_0\mathbf 1$. (Shapes, our addition: $x_n,\mu_k\in\mathbb R^D$, $\Lambda_k$ is $D\times D$, $\pi$ has $K$ entries.) The exact posterior is a mixture of $K^N$ distributions, intractable. VBEM approximates it around a local mode, following [Bis06, Sec 10.2] (p. 464).
- Variational forms (shown below): $q_n(z_n)=\mathrm{Cat}(z_n|r_n)$ (10.131), $q(\theta)=\mathrm{Dir}(\pi|\widehat\alpha)\prod_k\mathcal N(\mu_k|\widehat m_k,(\widehat\kappa_k\Lambda_k)^{-1})\mathrm{Wi}(\Lambda_k|\widehat L_k,\widehat\nu_k)$ (10.132); $r_n$ are the responsibilities (p. 465).
- **Variational M step** (average $z_n$ over $q(z_n)$): $\log q(\theta)=\log p(\pi)+\sum_n\mathbb E[\log p(z_n|\pi)]+\sum_k[\log p(\mu_k,\Lambda_k)+\sum_n\mathbb E[z_{nk}]\log\mathcal N(x_n|\mu_k,\Lambda_k^{-1})]+\text{const}$ (10.133). It splits, so $q(\theta)=q(\pi)\prod_kq(\mu_k,\Lambda_k)$ (10.134). For $\pi$: $\log q(\pi)=(\alpha_0-1)\sum_k\log\pi_k+\sum_k\sum_nr_{nk}\log\pi_k+\text{const}$ (10.135), hence $q(\pi)=\mathrm{Dir}(\pi|\widehat\alpha)$, $\widehat\alpha_k=\alpha_0+N_k$, $N_k=\sum_nr_{nk}$ (10.136–10.138) (p. 465).
- For $(\mu_k,\Lambda_k)$: Gaussian–Wishart with
$$\widehat\kappa_k=\breve\kappa+N_k,\quad \widehat m_k=(\breve\kappa\breve m+N_k\bar x_k)/\widehat\kappa_k,\quad \widehat L_k^{-1}=\breve L^{-1}+N_kS_k+\tfrac{\breve\kappa N_k}{\breve\kappa+N_k}(\bar x_k-\breve m)(\bar x_k-\breve m)^{\!\top},\quad \widehat\nu_k=\breve\nu+N_k\tag{10.139–10.143}$$
 with $\bar x_k=\frac1{N_k}\sum_nr_{nk}x_n$, $S_k=\frac1{N_k}\sum_nr_{nk}(x_n-\bar x_k)(x_n-\bar x_k)^\top$ (10.144–10.145). This resembles the MAP M step but yields posterior parameters, not a point estimate (p. 466).
- **Variational E step:** it differs from regular EM because it averages over parameters:
$$\log q(z)=\sum_n\sum_kz_{nk}\Big(\mathbb E[\log\pi_k]+\tfrac12\mathbb E[\log|\Lambda_k|]-\tfrac D2\log2\pi-\tfrac12\mathbb E[(x_n-\mu_k)^\top\Lambda_k(x_n-\mu_k)]\Big)+\text{const}\tag{10.146}$$
 "One can show" (p. 466): $\exp(\mathbb E[\log\pi_k])=\frac{\exp\psi(\widehat\alpha_k)}{\exp\psi(\sum_{k'}\widehat\alpha_{k'})}\triangleq\tilde\pi_k$ (10.147), $\psi(x)=\frac d{dx}\log\Gamma(x)$ the digamma function (10.148); $\mathbb E[\log|\Lambda_k|]=\sum_{j=1}^D\psi\big(\frac{\widehat\nu_k+1-j}2\big)+D\log2+\log|\widehat L_k|$ (10.149); $\mathbb E[(x_n-\mu_k)^\top\Lambda_k(x_n-\mu_k)]=D\widehat\kappa_k^{-1}+\widehat\nu_k(x_n-\widehat m_k)^\top\widehat L_k(x_n-\widehat m_k)\triangleq\tilde\Lambda_k$ (10.150).
- Responsibility (as printed): $r_{nk}\propto\tilde\pi_k\tilde\Lambda_k^{1/2}\exp\big(-\frac D{2\widehat\kappa_k}-\frac{\widehat\nu_k}2(x_n-\widehat m_k)^\top\widehat\Lambda_k(x_n-\widehat m_k)\big)$ (10.151). Regular EM: $r^{EM}_{nk}\propto\hat\pi_k|\hat\Lambda_k|^{1/2}\exp(-\frac12(x_n-\hat\mu_k)^\top\hat\Lambda_k(x_n-\hat\mu_k))$ with $\hat\pi_k$ the MAP estimate (10.152) (pp. 466–467). (See Reading notes on the symbols in 10.150–10.151.)

**10.3.6.4 Automatic sparsity.** Ignore the likelihood and compare the prior parts: VB gives $r^{VB}_{nk}=\tilde\pi_k=\frac{\exp\psi(\widehat\alpha_k)}{\exp\psi(\sum_{k'}\widehat\alpha_{k'})}$ (10.153); EM-MAP gives $r^{EM}_{nk}=\hat\pi_k=\frac{\widehat\alpha_k-1}{\sum_{k'}(\widehat\alpha_{k'}-1)}$ (10.154), where $\widehat\alpha_k=\alpha_0+N_k$ (p. 467).
- $\alpha_0\ll1$ makes $\pi$ sparse (Fig. 2.6), encouraging sparse $r_n$ and killing clusters with $N_k\ll N$. Setting $\alpha_0=0$: $\tilde\pi_k=\frac{\exp\psi(N_k)}{\exp\psi(\sum_{k'}N_{k'})}$ (10.155), $\hat\pi_k=\frac{N_k-1}{\sum_{k'}(N_{k'}-1)}$ (10.156) (p. 468).
- For an empty cluster ($N_k=0$), regular EM's $\hat\pi_k$ may become negative [FJ02]. The author says this does not occur under maximum likelihood ($\alpha_0=1$), but then there is no sparsity either. VBEM avoids it because the digamma-based quantity is positive (Fig. 10.11a, which plots $\exp\psi(x)$) (p. 468).
- With random initial counts and likelihood ignored, VBEM makes small clusters go to zero and large ones grow: "rich get richer" (Fig. 10.11b; see Supplementary Sec. 31.2). The reason: $\exp(\psi(N_k))<N_k$ and it is zero for small enough $N_k$, like $\ell_1$ soft-thresholding, and the reduction is greater for small counts (p. 468).
- Real example: 6 Gaussians on Old Faithful, $\alpha_0=0.001$; 4 components are killed off, and $\widehat\alpha_k=0$ for all but two (Figs. 10.12–10.13). This is an efficient way to choose the number of clusters, and similar techniques apply to HMM states (p. 468). Caveat: this "variational pruning" (posterior collapse) can make the model ignore $z$ if $p(x|z)$ is powerful (Sec. 21.4) (p. 468).
- **10.3.6.5 Bound:** $\mathcal L=\sum_z\int d\theta\,q(z,\theta)\log\frac{p(x,z,\theta)}{q(z,\theta)}\le\log p(x)$ (10.157). It increases monotonically (Fig. 10.14: steep parts are component killing, plateaus are slow cluster movement) (pp. 468–469).
- **10.3.6.6 Model selection:** with a uniform prior on $K$, $p(K|\mathcal D)=\frac{p(\mathcal D|K)}{\sum_{K'}p(\mathcal D|K')}\approx\frac{e^{\mathcal L(K)}}{\sum_{K'}e^{\mathcal L(K')}}$ (10.158). [BG06] show the VB marginal-likelihood approximation is more accurate than BIC. VB covers only one local mode, but there are $K!$ equivalent label-permuted modes, so a better approximation is $\log p(\mathcal D|K)\approx\mathcal L(K)+\log(K!)$ (p. 470).

*Intuition note.* In VBEM each cluster's weight is shrunk by $\exp\psi(\cdot)$, which punishes small counts more than large ones. Under a sparse prior the weakest clusters lose members until they vanish.

### 10.3.7 Variational message passing (VMP)
- Assume every complete conditional is exponential family: $p(z_j|z_{-j},x)=h(z_j)\exp[\eta_j(z_{-j},x)^\top\mathcal T(z_j)-A_j(\eta_j)]$ (10.159) ($\mathcal T$ sufficient statistics, $\eta_j$ natural parameters, $A_j$ log partition, $h$ base measure). This holds if the prior $p(z_j)$ is conjugate to the likelihood $p(z_{-j},x|z_j)$ (p. 470).
- Then $q_j\propto\exp[\mathbb E\log p(z_j|z_{-j},x)]=\exp[\log h+\mathbb E[\eta_j]^\top\mathcal T(z_j)-\mathbb E[A_j]]\propto h(z_j)\exp[\mathbb E[\eta_j]^\top\mathcal T(z_j)]$ (10.160–10.162). The new variational parameters are $\psi_j=\mathbb E[\eta_j(z_{-j},x)]$ (10.163) (p. 470).
- Generalised to any model with conjugate full conditionals, this is VMP [WB05], for any directed graphical model. As in belief propagation, nodes collect messages from parents and children (possibly via co-parents). The messages are expected sufficient statistics (p. 470). Extensions to conditionally conjugate models via CVI (Suppl. 10.3.1), and local Laplace approximations in [ABV21] (p. 471).

### 10.3.8 Autoconj
- VMP needs the user to specify the graphical model, with a lookup table of update rules. Autoconj [HJT18] derives the updates automatically for any conditionally conjugate directed model, analogous to autodiff (and uses autodiff internally). The full conditionals can serve CAVI and Gibbs sampling (p. 471).

### 10.4 More accurate variational posteriors
- More flexible families can tighten the ELBO and reduce the KL, though optimisation may be slower and statistical error can arise at low sample size [Bha+21] (p. 471).
- **10.4.1 Structured mean field** [SJ95]: keep tractable dependencies exactly. For HMMs, treat each sequence as a block: $q(z_{1:N,1:T},\theta)=q(\theta)\prod_nq(z_{n,1:T})$, with $q(z_{n,1:T})=\prod_tq(z_{n,t}|z_{n,t-1})$ computed by forwards-backwards. An automatic method is in [AHG20] (p. 471).
- **10.4.2 Hierarchical (auxiliary-variable) posteriors:** a factorised $q_\phi(z|x)=\prod_kq_\phi(z_k|x)$ cannot capture dependencies, and a full covariance may be too expensive. Adding auxiliary $a$ gives $q_\phi(z|x)=\int q_\phi(z|x,a)q_\phi(a|x)da\ne\prod_kq_\phi(z_k|x)$ (10.164) (hierarchical variational model [Ran16]; auxiliary variable deep generative model [Maa+16]). [TRB16] model $q_\phi(z|x,a)$ as a GP with inducing points $a$: a variational GP (p. 472).
- **10.4.3 Normalizing flows** push a simple source distribution through invertible nonlinear maps, and can give more accurate posteriors than Gaussian VI (Sec. 23.1.2.2) (p. 472).
- **10.4.4 Implicit posteriors:** sampling is easy but the density is not evaluable (e.g., non-invertible $z=f(z_0)$), so $\log p_\theta(z)/q_\psi(z|x)$ is hard. As in GANs, train a classifier separating prior samples from variational-posterior samples, using $T(x,z)=\log q_\psi(z|x)-\log p_\theta(z)$ [TR19] (p. 472).
- **10.4.5 VI + MCMC:** [SKW15] Hamiltonian VI trains an inference network to initialise HMC. The needed gradient is $\nabla_z\log p_\theta(z|x)=\nabla_z\log p_\theta(x,z)$ (10.165) (the printed bracket reads $\log[p(x,z)-\log p(x)]$, see Reading notes). The final sample approximates $q_\phi(z|x)$, and an auxiliary inverse network gives the entropy. [Hof17] is simpler: the network is trained with the standard ELBO for $\phi$, but $\theta$ is trained with $\log p_\theta(z,x)$ at an HMC sample. This avoids a reverse network and variational pruning, since the generative model is not trained with the ELBO (pp. 472–473).

### 10.5 Tighter bounds
**10.5.1 Multi-sample ELBO (IWAE)** [BGS16] (p. 473).
- Treat $q_\phi(z|x)$ as proposal. Weights $w_s^*=\frac{p_\theta(x,z_s)}{q_\phi(z_s|x)}$, normalised $\bar w_s=w^*_s/\sum_{s'}w^*_{s'}$. Estimator $\hat p_S(x|z_{1:S})=\frac1S\sum_s\frac{p_\theta(x,z_s)}{q_\phi(z_s|x)}$ (10.166), unbiased: $\mathbb E[\hat p_S]=p(x)$.
- Since it is positive, take logs and use Jensen:
$$\text{Ł}_S=\mathbb E_{q(z_{1:S}|x)}\Big[\log\tfrac1S\sum_sw_s\Big]=\mathbb E[\log\hat p_S]\le\log\mathbb E[\hat p_S]=\log p(x)\tag{10.167–10.168}$$
- For $S=1$ this is the standard ELBO, $\text{Ł}_1=\mathbb E_q[\log w]$ (10.169). Per [BGS16], increasing $S$ is guaranteed to make the bound tighter. Intuition: averaging inside the log removes the need for every sample to explain $x$, encouraging $q$ to be less concentrated (p. 473).
- Pathology [Rai+18a]: larger $S$ can decrease the signal-to-noise ratio and lead to a worse model; intuitively the bound depends less on the inference network, so the $\phi$-gradient is less informative (higher variance). Remedies: doubly reparameterised gradient [TL18b]; TVO; reweighted wake-sleep (p. 474).

**10.5.2 TVO** [MLW19; Bre+20b]: an alternative tighter bound with advantages for non-reparameterisable posteriors (e.g., discrete latents), and close links to reweighted wake-sleep. It uses thermodynamic integration (path sampling), based on the insight that a ratio of two unknown constants is easier to compute than the constants. It is like annealed importance sampling but deterministic (p. 474).

**10.5.3 EUBO.** ELBO: $\text{Ł}=\log p_\theta(x)-D_{\mathbb{KL}}(q_\phi\|p_\theta)\le\log p_\theta(x)$ (10.170). EUBO: $\log p_\theta(x)+D_{\mathbb{KL}}(p_\theta(z|x)\|q_\phi(z|x))\ge\log p_\theta(x)$ (10.171). Minimising it wrt $\phi$ was proposed in [MLW19], where it can sometimes converge to the true $\log p_\theta(x)$ faster. With $x\sim p_\theta(x)$, minimising $\mathbb E[\text{EUBO}]$ recovers the sleep phase (Sec. 10.6.2). With $x$ from the empirical distribution and self-normalised importance sampling: $\nabla_\phi\text{EUBO}=\sum_s\bar w_s\nabla_\phi\log q_\phi(z^s|x)$ (10.172), equivalent to the "daydream" update (p. 474–475).

### 10.6 Wake-sleep algorithm
- Motivation: ELBO training works poorly with discrete latents (no reparameterisation; REINFORCE has higher variance), and the bound may be loose. The IWAE fix may not give a better model. Wake-sleep alternates two phases. Wake: fit $\theta$ by maximising $\log p_\theta(x)$, approximated with importance samples from $q_\phi$. Sleep: train $\phi$ on $(x,z)$ pairs with $x$ "dreamed" from $p_\theta$. It is a form of adaptive importance sampling (p. 475).
- **10.6.1 Wake:** $\mathcal L(\theta)=D_{\mathbb{KL}}(p_{\mathcal D}\|p_\theta)=\mathbb E_{p_{\mathcal D}}[-\log p_\theta(x)]+\text{const}$ (10.173), i.e., maximise $\ell(\theta)=\mathbb E_{p_{\mathcal D}}[\log p_\theta(x)]$ (10.174). The original paper approximates it with the ELBO; reweighted wake-sleep (RWS) uses the IWAE bound: $\ell(\theta|\phi,x)=\log(\frac1S\sum_sw_s)$, $w_s=\frac{p_\theta(x,z_s)}{q_\phi(z_s|x)}$, $z_s\sim q_\phi$ (10.175) (p. 475).
- Gradient steps. With $\nabla\log w_s=\frac1{w_s}\nabla w_s$ (10.176):
$$\nabla\ell=\frac1{\frac1S\sum_sw_s}\Big(\frac1S\sum_s\nabla w_s\Big)=\frac1{\sum_sw_s}\Big(\sum_sw_s\nabla\log w_s\Big)=\sum_s\bar w_s\nabla\log w_s\tag{10.177–10.179}$$
 For $\theta$: $\nabla_\theta\log w_s=\frac1{w_s}\nabla_\theta w_s=\frac{q_\phi}{p_\theta}\nabla_\theta\frac{p_\theta}{q_\phi}=\frac1{p_\theta(x,z_s)}\nabla_\theta p_\theta(x,z_s)=\nabla_\theta\log p_\theta(x,z_s)$ (10.180), so $\nabla_\theta\ell=\sum_s\bar w_s\nabla\log p_\theta(x,z_s)$ (10.181) (p. 476).
- **10.6.2 Sleep:** $\mathcal L(\phi|\theta)=\mathbb E_{p_\theta(x)}[D_{\mathbb{KL}}(p_\theta(z|x)\|q_\phi(z|x))]=\mathbb E_{p_\theta(z,x)}[-\log q_\phi(z|x)]+\text{const}$ (10.182); equivalently maximise $\ell(\phi|\theta)=\mathbb E_{p_\theta(z,x)}[\log q_\phi(z|x)]$ (10.183). This is maximum likelihood for the inference network on "fantasy" samples (ancestral sampling): $\ell=\frac1S\sum_s\log q_\phi(z'_s|x'_s)$ (10.184), gradient (10.185). Since samples do not depend on $\phi$, no reparameterisation is needed, so discrete latents are easy (pp. 476–477).
- **10.6.3 Daydream:** sleep chases a moving target and trains on synthetic data only. RWS [BB15b] also uses real data (the "wake-phase $q$ update", renamed "daydream" by the author); [Le+19] use only wake and daydream. Objective $\mathcal L(\phi|\theta)=\mathbb E_{p_{\mathcal D}}[D_{\mathbb{KL}}(p_\theta(z|x)\|q_\phi(z|x))]$ (10.186), $\ell(\phi|\theta,x)=\mathbb E_{p_\theta(z|x)}[\log q_\phi(z|x)]$ (10.187), with importance sampling using $q_\phi$ as proposal: $\nabla_\phi\ell=\int p_\theta(z|x)\nabla_\phi\log q_\phi dz\approx\sum_s\bar w_s\nabla_\phi\log q_\phi(z_s|x)$ (10.188). Key difference from sleep: samples are $(x,z_s)\sim p_{\mathcal D}(x)q_\phi(z|x)$, real $x$, rather than $(x'_s,z'_s)\sim p_\theta$ (p. 477).
- **10.6.4 Summary:** Algorithm 10.5, one SGD step: sample $x_n$; draw $z_s\sim q(z|x_n)$; weights $w_s$, $\bar w_s$; optional $\log p(x_n)$ estimate; wake: update $\theta$ with $\sum_s\bar w_s\nabla_\theta\log p_\theta(z_s,x_n)$; daydream: update $\phi$ with $\sum_s\bar w_s\nabla_\phi\log q_\phi(z_s|x_n)$; optional sleep update (p. 478).
- Disadvantage: no single well-defined objective, so convergence is unclear. Advantage: simple (two alternating weighted maximum-likelihood problems), and it can be shown to "sandwich" the log marginal likelihood between lower and upper bounds. With $p_\theta(x,z)$ and $q_{\mathcal D,\phi}(x,z)=p_{\mathcal D}(x)q_\phi(z|x)$: wake $\min_\theta D_{\mathbb{KL}}(q_{\mathcal D,\phi}\|p_\theta)$ (10.189); daydream $\min_\phi D_{\mathbb{KL}}(p_\theta\|q_{\mathcal D,\phi})$ (10.190) (pp. 477–478).

### 10.7 Expectation propagation (EP)
- Motivation: standard VI minimises $D_{\mathbb{KL}}(q\|p)$, which is zero-forcing: $q$ tends to be too compact (over-confident). This can be desirable for some multimodal posteriors but is less reasonable for many unimodal ones (Bayesian logistic regression, GPs with log-concave likelihoods). $D_{\mathbb{KL}}(p\|q)$ is zero-avoiding and tends to give broad posteriors. EP can be seen as a local approximation to it (p. 478).

**10.7.1 Algorithm.**
- Exact: $p(\theta|\mathcal D)=\frac1{Z_p}\hat p(\theta)$, $\hat p=p_0(\theta)\prod_{k=1}^Kf_k(\theta)$ (10.191), with $f_k$ local factors (site potentials), $Z_p=p(\mathcal D)Z_0$ (pp. 478–479).
- Approximation: $q(\theta)=\frac1{Z_q}\hat q(\theta)$, $\hat q=p_0(\theta)\prod_k\tilde f_k(\theta)$ (10.192), $\tilde f_k\in\mathcal Q$, a tractable exponential-family class, usually Gaussian. Factors are optimised one at a time and initialised uninformatively, so initially $q=p_0$ (p. 479).
- Steps for factor $i$ (p. 479):
 1. Cavity: $q_{-i}^{\rm cavity}(\theta)=q(\theta)/\tilde f_i(\theta)\propto\prod_{k\ne i}\tilde f_k$ (10.193); division is subtraction of natural parameters. It represents all factors except $f_i$.
 2. Tilted: $q_i^{\rm tilted}=\frac1{Z_i}f_i(\theta)q^{\rm cavity}_{-i}(\theta)$, $Z_i=\int q^{\rm cavity}_{-i}f_id\theta$ (10.194).
 3. Project: $q_i^{\rm proj}=\arg\min_{\tilde q\in\mathcal Q}D(q_i^{\rm tilted}\|\tilde q)$ (10.195), since the tilted distribution may leave the family. With $D=D_{\mathbb{KL}}(q^{\rm tilted}\|q)$ this is moment matching (Sec. 5.1.4.2).
 4. Gaussian cavity $\mathcal N_c(\theta|r_{-i},Q_{-i})$: $\log q_i^{\rm tilted}=\alpha\log f_i(\theta)-\frac12\theta^\top Q_{-i}\theta+r_{-i}^\top\theta+\text{const}$ (10.196) ($\alpha$ is not defined at this point in the text). With $\hat\theta$ a local maximum and $\mathcal Q$ Gaussian: $Q_{\backslash i}=-\nabla^2_\theta\log q_i^{\rm tilted}|_{\hat\theta}$, $r_{\backslash i}=Q_{\backslash i}\hat\theta$ (10.197). This is Laplace propagation [SVE04]; with Monte Carlo it is blackbox EP (p. 480).
 5. New factor: $\tilde f_i^{\rm new}=q_i^{\rm proj}/q^{\rm cavity}_{-i}$ (10.198), so $q^{\rm cavity}_{-i}\tilde f_i^{\rm new}=q_i^{\rm proj}$: the best approximation within $\mathcal Q$ to using the exact factor (p. 480).

**10.7.2 Example.** Fig. 10.15: a logistic likelihood factor with a Gaussian cavity gives a nearly Gaussian tilted distribution, then projected. Unlike "Gaussianizing" each likelihood term in isolation (as the EKF does), EP finds a local factor that works well in the context of all other factors (p. 480).

**10.7.3 EP as generalised ADF.** ADF is sequential: $\hat p_{t+1}\propto q_t(z)p(x_t|z)$, then $q_{t+1}=\arg\min_{q\in\mathcal Q}D_{\mathbb{KL}}(\hat p_{t+1}\|q)$. It minimises KL in the desired direction, but in batch it depends on update order, and multiple passes include the same likelihood repeatedly, giving an overconfident posterior. EP overcomes this (pp. 480–481).

**10.7.4 Optimisation issues.** EP can be numerically unstable (e.g., negative variance after subtracting natural parameters). Damping with step $\delta$: $\tilde f_i^{\rm new}=\tilde f_i^{1-\delta}\big(q_i^{\rm proj}/q_{-i}^{\rm cavity}\big)^\delta$ (10.199), implementable by scaling natural parameters. [ML02] suggest $\delta=1/K$ (safe but slow); [Gel+14b] suggest starting at 0.5 and reducing to $1/K$ over $K$ iterations. No guarantee of convergence in vanilla form, though empirically it can work well, especially with log-concave $f_i$ (e.g., GP classifiers) (p. 481).

**10.7.5 Power EP and α-divergence.** The divergence $D(q^{\rm tilted}\|q)$ is a choice. $D_{\mathbb{KL}}(q^{\rm tilted}\|q)$ gives classic EP; $D_{\mathbb{KL}}(q\|q^{\rm tilted})$ gives the reverse KL of standard VI. α-divergences (Sec. 2.7.1.2) interpolate between mode seeking and mode covering, optimised by power EP [Min04]: cavity $q_{-i}^{\rm cavity}\propto q/\tilde f_i^\alpha$; $q_i^{\rm proj}=\mathrm{proj}(q_{-i}^{\rm cavity}f_i^\alpha)$; $\tilde f_i^{\rm new}\propto(q_i^{\rm proj}/q_{-i}^{\rm cavity})^{1/\alpha}$ (p. 481).

**10.7.6 Stochastic EP (SEP)** [LHLT15]. EP must store $\tilde f_n$ for each datapoint: $O(ND^2)$ memory with full-covariance Gaussians. SEP uses a shared factor: $\prod_nf_n(\theta)\approx\tilde f(\theta)^N$ (10.200); it suffices for $\tilde f$ to approximate the average likelihood (pp. 481–482). Steps: cavity $q_{-1}\propto q/\tilde f$ (10.201); tilted $q_{\backslash n}\propto f_nq_{-1}$ (10.202); $\tilde f_n=\mathrm{proj}(q_{\backslash n})/q_{-1}$ (10.203); damped update $\tilde f^{\rm new}=\tilde f_{\rm old}^{1-1/N}\tilde f_n^{1/N}$ (10.204). ADF is similar but uses the previous posterior $q_{t-1}$ instead of the cavity as prior. This avoids storing $\tilde f$ but gives overconfidence in batch (p. 482).

## Toy example (ours, not from the text)
Mean-field Ising update (10.97, 10.99, 10.100) on two connected nodes with $W_{12}=1$. Take $L_1^+-L_1^-=2$ and $L_2^+-L_2^-=-1$. Then $0.5(L_1^+-L_1^-)=1$ and $0.5(L_2^+-L_2^-)=-0.5$. Start at $\mu_1=\mu_2=0$ and update asynchronously, no damping (allowed on p. 459).
1. $a_1=W\mu_2+1=0+1=1$, so $q_1(+1)=\sigma(2)=1/(1+e^{-2})=0.8808$ and $\mu_1=2(0.8808)-1=0.7616=\tanh(1)$.
2. $a_2=W\mu_1-0.5=0.7616-0.5=0.2616$, so $\mu_2=\tanh(0.2616)=0.2558$.
3. $a_1=0.2558+1=1.2558$, so $\mu_1=\tanh(1.2558)=0.8499$.
4. $a_2=0.8499-0.5=0.3499$, so $\mu_2=\tanh(0.3499)=0.3363$.

Each node's mean is the tanh of its local evidence plus the neighbour's current mean. After two sweeps the means change less each time ($\mu_1$: 0.7616→0.8499; $\mu_2$: 0.2558→0.3363), but we do not claim convergence here.

## Concepts
- [[variational-inference-elbo]] — maximising a lower bound on $\log p(x)$ over a family $q$; this part gives ways to optimise and improve it (p. 456)
- [[kl-divergence]] — $D_{\mathbb{KL}}(q\|p)$ is zero-forcing, $D_{\mathbb{KL}}(p\|q)$ zero-avoiding (p. 478)
- [[mean-field-approximation]] (new) — fully factorised $q(z)=\prod_jq_j(z_j)$ (p. 456)
- [[cavi]] (new) — coordinate ascent VI; $q_j\propto\exp\mathbb E_{\rm mb}[\log\tilde p]$ (p. 457)
- [[free-form-vi]] (new) — factor forms determined by the log joint, not chosen in advance (p. 457)
- [[control-variates]] (new) — subtract a zero-mean correlated baseline to cut gradient variance (p. 455)
- [[variational-bayes]] (new) — VI applied to parameter posteriors (p. 459)
- [[vbem]] (new) — alternate $q(z_n)$ and $q(\theta)$ updates, averaging over parameters in the E step (p. 464)
- [[variational-pruning]] (new) — sparse-prior VBEM kills components; also called posterior collapse (p. 468)
- [[vmp]] (new) — CAVI for conjugate directed models via expected sufficient statistics (p. 470)
- [[iwae-bound]] (new) — multi-sample bound $\mathbb E[\log\frac1S\sum_sw_s]$, tighter as $S$ grows (p. 473)
- [[wake-sleep]] (new) — alternating wake ($\theta$), sleep/daydream ($\phi$) updates without one objective (p. 475)
- [[expectation-propagation]] (new) — cavity/tilted/projection updates of local factors (p. 478)
- [[conjugate-prior]] — conjugacy is what makes VB factors and VMP updates closed-form (p. 470)

## Canonical instances
- [[ising-denoising-meanfield]] — $\mu_i=\tanh(a_i)$ with damping on a 2d grid (pp. 458–460)
- [[univariate-gaussian-vb]] — Gaussian × gamma factors; compact versus exact posterior (pp. 460–463)
- [[gmm-vbem-old-faithful]] — 6 components pruned to 2 with $\alpha_0=0.001$ (pp. 467–469)
- [[logistic-factor-ep]] — logistic likelihood with Gaussian cavity (Fig. 10.15) (p. 480)

## Bridges (candidates)
- [structural-analogy] CAVI update $q_j\propto\exp\mathbb E[\log\tilde p]$ ↔ Gibbs sampling: sample from the full conditional instead of averaging its log (the author says "compare", p. 457)
- [structural-analogy] $\exp(\psi(N_k))$ shrinkage in VBEM ↔ regularisation: $\ell_1$ soft-thresholding (the author's comparison, p. 468)
- [structural-analogy] VMP ↔ belief propagation: message passing, but messages are expected sufficient statistics (p. 470)
- [same-math] IWAE estimator $\hat p_S$ ↔ importance sampling: it is the importance-sampling average of $p_\theta(x,z_s)/q_\phi(z_s|x)$ estimating $p(x)$ (the text ties IWAE to self-normalised importance sampling) (p. 473)
- [structural-analogy] EP ↔ ADF/sequential Bayes: ADF projects one pass in order; EP revisits factors using cavities (p. 480)

## Questions this raises
- When does mean-field underestimation of uncertainty (p. 462) matter in practice, and does EP's $D_{\mathbb{KL}}(p\|q)$ direction reliably fix it?
- Can wake-sleep's lack of a single objective (p. 477) be repaired, or is the "sandwich" property enough?
- How is the pruning in VBEM (p. 468) separated from harmful posterior collapse (Sec. 21.4)?
- Why is the $K!$ correction for label permutations (p. 470) only a $\log(K!)$ shift, and what about symmetric modes in other models?

## Reading notes
- This unit starts mid-section, at the end of §10.2.3.1 (Eq. 10.67) on printed p. 455, and ends at the end of §10.7.6 on p. 482. Part 1 presumably contains §10.1–10.2.3.1; $\tilde{\mathcal L}$ and Fig. 10.5 are used on these pages but not defined here. Printed = pdf − 34.
- Footer reads "Online version. December 10, 2025"; author Kevin P. Murphy, CC-BY-NC-ND.
- Fig. 10.10: caption says orange is variational and blue exact; the legend shows Exact orange, VB blue; the text says green exact, dotted red variational.
- Eq. 10.150–10.151: the symbol $\tilde\Lambda_k$ is defined as the expected quadratic form in 10.150 but used as $\tilde\Lambda_k^{1/2}$ in 10.151, which looks like the $\exp(\mathbb E\log|\Lambda_k|)$ factor. The quadratic term uses $\widehat\Lambda_k$ where 10.150 has $\widehat L_k$. I copied 10.151 as printed.
- p. 468 says digamma is "always positive". Fig. 10.11a plots $\exp\psi(x)$, which is positive; positivity of $\psi$ itself is not shown on these pages.
- Fig. 10.14 caption refers to "Section 10.3.6.6" for killing off components, which is described in §10.3.6.4.
- Eq. 10.165 as printed has $\log[p_\theta(x,z)-\log p_\theta(x)]$; the intended meaning is $\log p_\theta(x,z)-\log p_\theta(x)$.
- Eq. 10.166 sums over index $k$ but the summand uses $s$. In 10.166–10.167 the source writes $w_s$ although $w_s$ was just defined as the normalised weight; I read it as the unnormalised weight $w_s^*$. In 10.133 the source prints no '+' before the second bracket; I inserted one. Algorithm 10.4 line 4 mixes $i$ and $j$. Algorithm 10.5 has a stray "9 b" (image shows it).
- 10.5.3 refers to "Equation (10.188)" for self-normalised importance sampling, a forward reference.
