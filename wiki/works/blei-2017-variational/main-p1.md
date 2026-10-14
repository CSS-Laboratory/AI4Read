---
id: blei-2017-variational/main-p1
work: blei-2017-variational
unit: paper (part 1/2) — Sections 1–4.3 (up to the start of "Probabilistic topic models")
pages: 1–21
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 4
---
# Variational Inference: A Review for Statisticians (part 1: Sections 1–4.3)

## L0 — One line
Variational inference turns posterior approximation into optimization: choose a simple family of densities and maximize the ELBO, which minimizes the KL divergence to the exact posterior.

## L1 — The gist (≤ 120 words)
Bayesian inference needs the posterior p(z|x), but its normalizer (the evidence) is often intractable. The authors review variational inference (VI). It posits a family of simple densities and picks the member closest in KL divergence to the posterior. Because the KL cannot be computed, one maximizes the ELBO (evidence lower bound), which equals the negative KL up to a constant. For the mean-field family (independent factors), coordinate ascent (CAVI) gives updates, worked out fully for a Gaussian mixture. For exponential-family models the updates become expected natural parameters, and stochastic natural-gradient steps scale VI to massive data. VI is usually faster than MCMC but has no exactness guarantee and tends to underestimate posterior variance.

**Prerequisites:** conditional and joint densities, expectation, KL divergence, Gaussian densities, exponential families (natural parameter, sufficient statistic, log normalizer), gradient ascent; Markov chains (only for the §1 context on MCMC).

## L2 — Key ideas (5–10 bullets)
- **VI replaces sampling by optimization.** Pick a family Q and solve q* = argmin KL(q‖p(z|x)), Eq. (1). MCMC is exact asymptotically; VI is typically faster but only finds a nearby density (pp. 2–3).
- **The evidence makes the posterior hard.** p(x)=∫p(z,x)dz is often intractable; in the Gaussian mixture the direct sum has Kⁿ terms (pp. 5–6).
- **ELBO.** KL(q‖p(z|x)) depends on log p(x), so one maximizes ELBO(q)=E[log p(z,x)]−E[log q(z)]. It equals log p(x) − KL, hence lower-bounds log evidence and balances likelihood against closeness to the prior (pp. 6–7).
- **Mean-field family.** Independent factors q(z)=∏q_j(z_j). It cannot capture correlation, and in the 2-D Gaussian example its marginal variances come out too small (a common effect, which the KL direction explains) (pp. 7–9).
- **CAVI.** Set each factor q_j ∝ exp{E_{−j}[log p(z_j, z_{−j}, x)]}. This goes uphill on the ELBO to a local optimum, so initialization matters (pp. 9–11).
- **Gaussian mixture example.** CAVI gives closed-form updates for the assignment probabilities φ_ik and the Gaussian parameters (m_k, s_k²). On 10,000 images it is "orders of magnitude" faster than the Hamiltonian-MC (Stan) baseline compared in Figure 6 (pp. 12–17).
- **Exponential-family complete conditionals.** Each optimal factor lies in the same family as its complete conditional, with variational parameter ν_j = E[η_j]. In conditionally conjugate models the local and global updates are Eq. (47)–(48) (pp. 17–19).
- **Stochastic VI.** The natural gradient of the ELBO is g(λ)=E[α̂]−λ. A single-data-point version is unbiased and cheap, and with Robbins–Monro step sizes it scales CAVI to big data (pp. 20–21).

## L3 — Walkthrough

### Abstract and 1 Introduction (pp. 1–4)
- **Problem.** A joint density of latent variables $\mathbf z=z_{1:m}$ and observations $\mathbf x=x_{1:n}$ is $p(\mathbf z,\mathbf x)=p(\mathbf z)p(\mathbf x\mid\mathbf z)$: prior times likelihood. Bayesian inference means computing the posterior $p(\mathbf z\mid\mathbf x)$, which in complex models often needs approximation (p. 2).
- **MCMC (the baseline).** Build an ergodic Markov chain (a random walk whose long-run behaviour does not depend on where it starts) on $\mathbf z$ whose stationary distribution (the long-run frequency of each state) is the posterior, collect samples, and form an empirical estimate (p. 2). The authors say it has been "the dominant paradigm" for decades (p. 2). It is hard to use when an approximate conditional is needed faster than simple MCMC can produce, e.g. with large data sets or very complex models (p. 2).
- **VI idea.** Posit a family $\mathcal Q$ of densities over the latent variables and find
$$q^*(\mathbf z)=\arg\min_{q(\mathbf z)\in\mathcal Q}\mathrm{KL}\big(q(\mathbf z)\,\|\,p(\mathbf z\mid\mathbf x)\big)\tag{1}$$
Then use $q^*$ as the approximation. The reach of $\mathcal Q$ manages the complexity of the optimization: $\mathcal Q$ should be flexible enough to be close to the posterior but simple enough for efficient optimization (p. 3). Footnote 1: the review focuses on KL(q‖p) ("Kullback–Leibler VI"). Wainwright and Jordan note that any optimization-based density approximation can be called "variational" (p. 3).
- **VI versus MCMC (authors' guidance).**
  - MCMC is more computationally intensive but guarantees (asymptotically) exact samples. VI has no such guarantee, can only find a density close to the target, but tends to be faster. It easily uses stochastic and distributed optimization (some MCMC methods can too) (p. 3).
  - Suggested uses: VI for large data sets and for quickly exploring many models (example: one billion text documents). MCMC for smaller data sets where one happily pays for more precise samples (example: a small, expensive 20-year data set with a trusted model) (p. 3).
  - Posterior geometry also matters. A mixture posterior has multiple modes from label permutations. Gibbs sampling, if the model permits, quickly focuses on one mode. Where Gibbs is not an option, VI may beat a general MCMC method such as HMC (Hamiltonian Monte Carlo, an MCMC method that uses the gradient of the log density to propose distant moves), even on small data (p. 3).
  - The authors' general caveat: VI has been studied less rigorously than MCMC, and its statistical properties are less well understood (p. 2; the abstract says VI "is not yet well understood", p. 1).
  - Accuracy: the relative accuracy of VI and MCMC "is still unknown". VI generally underestimates the posterior variance, a consequence of its objective. This may be acceptable depending on the task. Several empirical studies found no necessary loss in, e.g., posterior predictive densities. Other work targets the shortfall in posterior variance (pp. 3–4).
  - VI and MCMC apply beyond Bayesian models: they are tools for approximating or simulating intractable densities (p. 4).
- **History (as the authors tell it).** Two parallel tracks. Peterson and Anderson (1987) is "arguably" the first variational procedure for a particular model (a neural network). Hinton and Van Camp (1993) proposed a variational algorithm for a similar network. Neal and Hinton connected VI to EM (p. 4).
- **Modern directions.** Massive data, better optimization of Eq. (1) (usually subject to local minima), generic VI algorithms, and more accurate (richer) families (p. 4).
- **Organization.** §2 mean-field and coordinate ascent; §3 Gaussian mixture; §4.1–4.2 exponential-family models and a link to the Gibbs sampler; §4.3 stochastic VI; §5 perspective and open problems (p. 4).

> **Intuition note.** MCMC gives you samples that are exact in the limit but slow to get; VI gives you one fitted density quickly with no exactness guarantee. The authors frame the choice as a trade of precision against speed and scale.

### 2 Variational inference (pp. 4–11)
Goal: approximate the conditional density of latent variables given observed ones, using a family indexed by free "variational parameters". The fitted density is a proxy for the exact conditional. Vectors are column vectors (p. 4).

#### 2.1 The problem of approximate inference (pp. 5–6)
- Hyperparameters are omitted from the notation. The conditional is
$$p(\mathbf z\mid\mathbf x)=\frac{p(\mathbf z,\mathbf x)}{p(\mathbf x)}\tag{2}$$
The denominator is the marginal density of the observations, the **evidence**:
$$p(\mathbf x)=\int p(\mathbf z,\mathbf x)\,d\mathbf z\tag{3}$$
For many models this integral is unavailable in closed form or needs exponential time; that is why inference is hard (p. 5). All unknowns, global parameters and "local" per-data-point variables alike, are treated as latent random variables (p. 5).
- **Bayesian mixture of unit-variance Gaussians (running example).** $K$ components with means $\boldsymbol\mu=\{\mu_1,\dots,\mu_K\}$ and prior variance $\sigma^2$ (a hyperparameter). Each $c_i$ is an indicator $K$-vector (all zeros except one 1) (p. 5).
$$\mu_k\sim\mathcal N(0,\sigma^2),\quad k=1,\dots,K\tag{4}$$
$$c_i\sim\text{Categorical}(1/K,\dots,1/K),\quad i=1,\dots,n\tag{5}$$
$$x_i\mid c_i,\boldsymbol\mu\sim\mathcal N(c_i^\top\boldsymbol\mu,1),\quad i=1,\dots,n\tag{6}$$
$$p(\boldsymbol\mu,\mathbf c,\mathbf x)=p(\boldsymbol\mu)\prod_{i=1}^n p(c_i)\,p(x_i\mid c_i,\boldsymbol\mu)\tag{7}$$
Latent variables are $\mathbf z=\{\boldsymbol\mu,\mathbf c\}$: $K$ means and $n$ assignments. The evidence is
$$p(\mathbf x)=\int p(\boldsymbol\mu)\prod_{i=1}^n\sum_{c_i}p(c_i)\,p(x_i\mid c_i,\boldsymbol\mu)\,d\boldsymbol\mu\tag{8}$$
Each $\mu_k$ appears in all $n$ factors, so (8) does not factor into one-dimensional integrals. Numerically evaluating this $K$-dimensional integral costs $O(K^n)$ (pp. 5–6).
- Distributing the product over the sum gives a sum over all cluster configurations $\mathbf c$:
$$p(\mathbf x)=\sum_{\mathbf c}p(\mathbf c)\int p(\boldsymbol\mu)\prod_{i=1}^n p(x_i\mid c_i,\boldsymbol\mu)\,d\boldsymbol\mu\tag{9}$$
Each integral is computable by Gaussian conjugacy, but there are $K^n$ of them. Computing the evidence "remains exponential in K, hence intractable" (p. 6).

#### 2.2 The evidence lower bound (pp. 6–7)
- The goal is Eq. (10), the same as (1). But the objective is not computable because it needs the evidence. Recall (expectations are with respect to $q$):
$$\mathrm{KL}(q\|p(\mathbf z\mid\mathbf x))=\mathbb E[\log q(\mathbf z)]-\mathbb E[\log p(\mathbf z\mid\mathbf x)]\tag{11}$$
Expanding the conditional:
$$\mathrm{KL}(q\|p(\mathbf z\mid\mathbf x))=\mathbb E[\log q(\mathbf z)]-\mathbb E[\log p(\mathbf z,\mathbf x)]+\log p(\mathbf x)\tag{12}$$
So the KL depends on $\log p(\mathbf x)$ (p. 6).
- Optimize instead an objective equal to the KL up to a constant, the **evidence lower bound**:
$$\mathrm{ELBO}(q)=\mathbb E[\log p(\mathbf z,\mathbf x)]-\mathbb E[\log q(\mathbf z)]\tag{13}$$
It is the negative KL of (12) plus $\log p(\mathbf x)$, a constant in $q$. So maximizing the ELBO is equivalent to minimizing the KL (p. 6).
- Footnote 2: KL is asymmetric (KL(q‖p) ≠ KL(p‖q)), nonnegative, and minimized when $q=p$ (p. 6).
- **Reading the ELBO.** It rewrites as
$$\mathrm{ELBO}(q)=\mathbb E[\log p(\mathbf z)]+\mathbb E[\log p(\mathbf x\mid\mathbf z)]-\mathbb E[\log q(\mathbf z)]=\mathbb E[\log p(\mathbf x\mid\mathbf z)]-\mathrm{KL}(q\|p(\mathbf z))$$
The first term (expected likelihood) favors densities explaining the data. The second (negative divergence from the prior) favors densities close to the prior. The objective "mirrors the usual balance between likelihood and prior" (pp. 6–7).
- **Lower bound.** Equations (12) and (13) give
$$\log p(\mathbf x)=\mathrm{KL}(q(\mathbf z)\|p(\mathbf z\mid\mathbf x))+\mathrm{ELBO}(q)\tag{14}$$
Since $\mathrm{KL}\ge0$, $\log p(\mathbf x)\ge\mathrm{ELBO}(q)$ for any $q$ (the original literature used Jensen's inequality) (p. 7).

> **Intuition note.** The ELBO is log evidence minus a non-negative gap, and the gap is exactly the KL we want to shrink. Raising the ELBO therefore shrinks the gap without ever computing the evidence.

- **Model selection.** Using the ELBO as a model selection criterion has been explored on the premise that the bound approximates the marginal likelihood. "Though this sometimes works in practice, selecting based on a bound is not justified in theory." Other work uses variational approximations of the log predictive density for cross-validation-based selection (p. 7).
- **Relation to EM.** The ELBO's first term is the expected complete log-likelihood that EM optimizes. EM finds maximum likelihood estimates in latent-variable models and uses that the ELBO equals $\log p(\mathbf x)$ when $q(\mathbf z)=p(\mathbf z\mid\mathbf x)$. It alternates an E step (expected complete log likelihood under $p(\mathbf z\mid\mathbf x)$) and an M step (optimize over parameters). Unlike VI, EM assumes that expectation is computable. Unlike EM, VI does not estimate fixed parameters; it is often used where classical parameters are latent variables (p. 7). Footnote 3: variational EM is EM with a variational E-step; CAVI can look like EM, with "E step" updating local latent variables and "M step" the global ones (p. 7).

#### 2.3 The mean-field variational family (pp. 7–9)
- **Mean-field family:** latent variables are mutually independent, each with its own factor:
$$q(\mathbf z)=\prod_{j=1}^m q_j(z_j)\tag{15}$$
(p. 7). The family is not a model of the data (no $\mathbf x$ in it); the ELBO links the fitted density to data and model. Parametric forms of factors are not fixed in advance; for some models the model's properties determine their optimal forms (p. 8).
- Richer families exist: **structured VI** adds dependencies between variables; **mixtures** of variational densities add latent variables in the family. Both may improve fidelity but give harder optimization (p. 8).
- **Mixture of Gaussians (continued).**
$$q(\boldsymbol\mu,\mathbf c)=\prod_{k=1}^K q(\mu_k;m_k,s_k^2)\prod_{i=1}^n q(c_i;\varphi_i)\tag{16}$$
Each $\mu_k$ has a Gaussian factor (mean $m_k$, variance $s_k^2$). Each $c_i$ has a categorical factor with assignment-probability $K$-vector $\varphi_i$. The authors state that "in fact, these are the optimal forms" of the mean-field density for this model (p. 8). *(added step: $\mathbf m,\mathbf s^2\in\mathbb R^K$; $\varphi_i\in\mathbb R^K$, so $\varphi$ is $n\times K$.)*
- **Figure 1 (2-D Gaussian).** The mean-field family "can capture any marginal density of the latent variables" but cannot capture correlation. For a highly correlated 2-D Gaussian, the optimal mean-field fit is a product of two Gaussians with the same mean but decoupled covariance. Its marginal variances under-represent the target's. Reason: KL(q‖p) in Eq. (11) penalizes q-mass where p has little mass but penalizes the reverse less. To match marginal variances, the circular q would have to expand into territory where p has little mass (p. 9).

> **Intuition note.** Forcing independence cannot reproduce a tilted ellipse. And because q is punished for putting mass where p has none, it stays inside the target, so the fit comes out too narrow.

#### 2.4 Coordinate ascent mean-field variational inference (pp. 9–10)
- **CAVI** iteratively optimizes each factor while holding the others fixed, climbing the ELBO to a local optimum (p. 9).
- **Result.** The *complete conditional* of $z_j$ is $p(z_j\mid\mathbf z_{-j},\mathbf x)$. Fix the other factors $q_\ell$, $\ell\neq j$. The optimal factor satisfies
$$q_j^*(z_j)\propto\exp\{\mathbb E_{-j}[\log p(z_j\mid\mathbf z_{-j},\mathbf x)]\}\tag{17}$$
with the expectation taken under $\prod_{\ell\ne j}q_\ell(z_\ell)$. Equivalently,
$$q_j^*(z_j)\propto\exp\{\mathbb E_{-j}[\log p(z_j,\mathbf z_{-j},\mathbf x)]\}\tag{18}$$
By independence the right-hand expectations do not involve $q_j$, so this is a valid coordinate update (p. 9).
- **Algorithm 1 (CAVI).** Input: model $p(\mathbf x,\mathbf z)$, data $\mathbf x$. Initialize factors $q_j(z_j)$. While the ELBO has not converged: for $j=1..m$ set $q_j(z_j)\propto\exp\{\mathbb E_{-j}[\log p(z_j\mid\mathbf z_{-j},\mathbf x)]\}$; then compute $\mathrm{ELBO}(q)$. Return $q(\mathbf z)$ (p. 10).
- **Related ideas.** CAVI can be viewed as message passing: each variable's variational parameters are updated from those of its Markov blanket (the neighbouring variables that, once known, make it independent of all others). This enabled automated software and links VI to graphical-model theory (p. 10). CAVI is "closely related" to Gibbs sampling: Gibbs samples from each complete conditional; Eq. (18) uses the same complete conditional, takes the expected log, and sets the variational factor with it (p. 10). Footnote 4: collapsed Gibbs has a variational analogue, collapsed VI; out of scope (p. 10).
- **Derivation of (18)** (uses no gradients, unlike Bishop's argument) (p. 10). Write the ELBO as a function of $q_j$, absorbing terms not depending on it into a constant:
$$\mathrm{ELBO}(q_j)=\mathbb E_j\big[\mathbb E_{-j}[\log p(z_j,\mathbf z_{-j},\mathbf x)]\big]-\mathbb E_j[\log q_j(z_j)]+\text{const.}\tag{19}$$
The first term uses iterated expectation. The second keeps only the part of $\mathbb E[\log q]$ that depends on $q_j$, using independence. Up to a constant, (19) is the negative KL between $q_j(z_j)$ and $q_j^*(z_j)$ of (18). So the ELBO is maximized in $q_j$ when $q_j=q_j^*$ (p. 10).

> **Intuition note.** With all other factors frozen, the ELBO as a function of one factor is just minus a KL to a fixed target. The best factor is that target (Eq. 18, up to normalization), so each coordinate step sets $q_j$ to it and cannot decrease the ELBO.

#### 2.5 Practicalities (p. 11)
- **Initialization.** The ELBO is generally non-convex; CAVI only guarantees a local optimum, which can depend on initialization. Figure 2 (10 random initializations on the Gaussian mixture, fitted to images, §3.4) shows different final ELBO values, indicating many local optima. In terms of KL(q‖p), better optima give densities closer to the exact posterior. This is not always a disadvantage: mixture and mixed-membership models have many symmetric posterior modes from label switching, and representing one mode suffices for exploring clusters or predicting new observations (p. 11).
- **Convergence.** Stop when the ELBO change falls below a small threshold. Computing the full-data ELBO may be undesirable; the authors suggest the average log predictive of a small held-out set (the mean log probability the fitted model gives to data kept out of fitting) as a proxy (not guaranteed to increase monotonically, unlike the full ELBO) (p. 11).
- **Numerical stability.** Work with log probabilities. The log-sum-exp identity, usually with $\alpha=\max_i x_i$:
$$\log\Big[\sum_i\exp(x_i)\Big]=\alpha+\log\Big[\sum_i\exp(x_i-\alpha)\Big]\tag{20}$$

### 3 A complete example: Bayesian mixture of Gaussians (pp. 11–17)
Setup as in §2.1, with a fixed hyperparameter $\sigma^2$, observation variance one, and a uniform prior over components. The ELBO, a function of $\mathbf m,\mathbf s^2,\varphi$, is
$$\begin{aligned}\mathrm{ELBO}(\mathbf m,\mathbf s^2,\varphi)=&\sum_{k=1}^K\mathbb E[\log p(\mu_k);m_k,s_k^2]\\&+\sum_{i=1}^n\big(\mathbb E[\log p(c_i);\varphi_i]+\mathbb E[\log p(x_i\mid c_i,\boldsymbol\mu);\varphi_i,\mathbf m,\mathbf s^2]\big)\\&-\sum_{i=1}^n\mathbb E[\log q(c_i;\varphi_i)]-\sum_{k=1}^K\mathbb E[\log q(\mu_k;m_k,s_k^2)]\end{aligned}\tag{21}$$
Each expectation is computable in closed form (p. 12).

#### 3.1 Variational density of the mixture assignments (pp. 12–13)
From (18):
$$q^*(c_i;\varphi_i)\propto\exp\{\log p(c_i)+\mathbb E[\log p(x_i\mid c_i,\boldsymbol\mu);\mathbf m,\mathbf s^2]\}\tag{22}$$
The log prior is $-\log K$ for every value of $c_i$, so it is constant. Since $c_i$ is an indicator, $p(x_i\mid c_i,\boldsymbol\mu)=\prod_{k}p(x_i\mid\mu_k)^{c_{ik}}$, and
$$\mathbb E[\log p(x_i\mid c_i,\boldsymbol\mu)]=\sum_k c_{ik}\,\mathbb E[\log p(x_i\mid\mu_k);m_k,s_k^2]\tag{23}$$
$$=\sum_k c_{ik}\,\mathbb E[-(x_i-\mu_k)^2/2;m_k,s_k^2]+\text{const.}\tag{24}$$
$$=\sum_k c_{ik}\big(\mathbb E[\mu_k;m_k,s_k^2]\,x_i-\mathbb E[\mu_k^2;m_k,s_k^2]/2\big)+\text{const.}\tag{25}$$
Terms constant in $c_i$ are dropped in each line. This needs $\mathbb E[\mu_k]$ and $\mathbb E[\mu_k^2]$ from the Gaussian factor. Update:
$$\varphi_{ik}\propto\exp\{\mathbb E[\mu_k;m_k,s_k^2]\,x_i-\mathbb E[\mu_k^2;m_k,s_k^2]/2\}\tag{26}$$
It depends only on the component factors' parameters (p. 13).

#### 3.2 Variational density of the component means (p. 13)
From (18):
$$q(\mu_k)\propto\exp\Big\{\log p(\mu_k)+\sum_{i=1}^n\mathbb E[\log p(x_i\mid c_i,\boldsymbol\mu);\varphi_i,\mathbf m_{-k},\mathbf s^2_{-k}]\Big\}\tag{27}$$
Because $c_i$ is an indicator, $\varphi_{ik}=\mathbb E[c_{ik};\varphi_i]$. Then
$$\log q(\mu_k)=\log p(\mu_k)+\sum_i\mathbb E[\log p(x_i\mid c_i,\boldsymbol\mu);\varphi_i,\mathbf m_{-k},\mathbf s^2_{-k}]+\text{const.}\tag{28}$$
$$=\log p(\mu_k)+\sum_i\mathbb E[c_{ik}\log p(x_i\mid\mu_k);\varphi_i]+\text{const.}\tag{29}$$
$$=-\mu_k^2/2\sigma^2+\sum_i\mathbb E[c_{ik};\varphi_i]\log p(x_i\mid\mu_k)+\text{const.}\tag{30}$$
$$=-\mu_k^2/2\sigma^2+\sum_i\varphi_{ik}\big(-(x_i-\mu_k)^2/2\big)+\text{const.}\tag{31}$$
$$=-\mu_k^2/2\sigma^2+\sum_i\varphi_{ik}x_i\mu_k-\varphi_{ik}\mu_k^2/2+\text{const.}\tag{32}$$
$$=\Big(\sum_i\varphi_{ik}x_i\Big)\mu_k-\Big(1/2\sigma^2+\sum_i\varphi_{ik}/2\Big)\mu_k^2+\text{const.}\tag{33}$$
This is an exponential family with sufficient statistics $\{\mu_k,\mu_k^2\}$ and natural parameters $\{\sum_i\varphi_{ik}x_i,\ -1/2\sigma^2-\sum_i\varphi_{ik}/2\}$, i.e. a Gaussian. In mean and variance:
$$m_k=\frac{\sum_i\varphi_{ik}x_i}{1/\sigma^2+\sum_i\varphi_{ik}},\qquad s_k^2=\frac{1}{1/\sigma^2+\sum_i\varphi_{ik}}\tag{34}$$
*(added step: a Gaussian with mean $m$ and variance $s^2$ has natural parameters $m/s^2$ and $-1/(2s^2)$. Matching $-1/(2s^2)=-(1/2\sigma^2+\sum_i\varphi_{ik}/2)$ gives $s_k^2$; then $m_k=s_k^2\sum_i\varphi_{ik}x_i$.)*
These resemble the complete conditional of the $k$th component, a posterior Gaussian given the data assigned to it. The variational update is a weighted complete conditional, each point weighted by its variational probability of belonging to component $k$ (p. 13).

*Skip path:* carry forward Eq. (26) and (34).

> **Intuition note.** The component mean is estimated like a Gaussian posterior mean, but each point counts only as much as the probability that it belongs to that cluster.

#### 3.3 CAVI for the mixture of Gaussians (pp. 13–14)
- **Algorithm 2.** Input $x_{1:n}$, $K$, $\sigma^2$. Initialize $\mathbf m,\mathbf s^2,\varphi$. While the ELBO has not converged: for each $i$ set $\varphi_{ik}$ by (26); for each $k$ set $m_k$ and $s_k^2$ by (34); compute ELBO (21). Return $q(\mathbf m,\mathbf s^2,\varphi)$ (p. 14).
- The fitted density can be used like a posterior: assign $\hat c_i=\arg\max_k\varphi_{ik}$ and estimate cluster means by $m_k$ (p. 13). The approximate predictive for new data is a mixture of Gaussians (p. 14):
$$p(x_{\text{new}}\mid x_{1:n})\approx\frac1K\sum_{k=1}^K p(x_{\text{new}}\mid m_k)\tag{35}$$
with $p(x_{\text{new}}\mid m_k)$ Gaussian with mean $m_k$ and unit variance.

#### 3.4 Empirical study (pp. 14–17)
- **Simulation.** 2-D data from $K=5$ Gaussians with random means, covariances and assignments. The initial variational components are nearly centered and wide. The authors highlight "elbows" in the ELBO, phases where the variational approximation changes its shape (plateaus, then jumps); Figure 3 shows snapshots at iterations 20, 28, 35 and 50, and the ELBO curve is flat by about iteration 45. The authors attribute the elbows to non-convexity: CAVI iteratively reaches better plateaus. The average held-out log predictive is smoother than the ELBO (p. 14, Figure 3 on p. 15).
- **Images.** Each image is represented by red, green and blue histograms of length 192, concatenated into a 576-dimensional vector (Figure 4). A 30-cluster Gaussian mixture was fitted by CAVI to 10,000 randomly selected imageCLEF training images, with a different 10,000 for testing. Figure 5 shows similarly colored images per cluster. Figure 6 compares held-out average log predictive over time with a Stan implementation using a Hamiltonian-MC-based sampler (details in Appendix B, not in this unit). Result: "CAVI is orders of magnitude faster than this sampling algorithm", fitting in under a minute (pp. 16–17). Footnote 5: this is not a definitive VI–MCMC comparison; another sampler, such as collapsed Gibbs, might do better (p. 16).

### 4 Variational inference with exponential families (pp. 16–21)
The mixture of Gaussians belongs to the class of models in which every complete conditional is in the exponential family. The authors list Bayesian mixtures of exponential families, factorial mixtures, matrix factorization, certain hierarchical regressions (linear, probit), stochastic blockmodels, hierarchical mixtures of experts and mixed-membership models. In this class CAVI is easier to derive and VI can scale to massive data (p. 17).

#### 4.1 Complete conditionals in the exponential family (pp. 17–18)
Suppose
$$p(z_j\mid\mathbf z_{-j},\mathbf x)=h(z_j)\exp\{\eta_j(\mathbf z_{-j},\mathbf x)^\top z_j-a(\eta_j(\mathbf z_{-j},\mathbf x))\}\tag{36}$$
where $z_j$ is its own sufficient statistic, $h$ the base measure, $a$ the log normalizer, and $\eta_j$ depends on the conditioning set. For a mean-field $q$, Eq. (17) becomes
$$q(z_j)\propto\exp\{\mathbb E[\log p(z_j\mid\mathbf z_{-j},\mathbf x)]\}\tag{37}$$
$$=\exp\{\log h(z_j)+\mathbb E[\eta_j(\mathbf z_{-j},\mathbf x)]^\top z_j-\mathbb E[a(\eta_j(\mathbf z_{-j},\mathbf x))]\}\tag{38}$$
$$\propto h(z_j)\exp\{\mathbb E[\eta_j(\mathbf z_{-j},\mathbf x)]^\top z_j\}\tag{39}$$
Each optimal factor is in the same exponential family as its complete conditional, with the same parameter dimension, base measure $h$ and log normalizer $a$. With $\nu_j$ the variational parameter of the $j$th factor, each update sets it to the expected parameter of the complete conditional:
$$\nu_j=\mathbb E[\eta_j(\mathbf z_{-j},\mathbf x)]\tag{40}$$
(p. 18.)

> **Intuition note.** If the complete conditional has a known form, the optimal variational factor has the same form. The update then just averages the conditional's natural parameter under the other factors.

#### 4.2 Conditional conjugacy and Bayesian models (pp. 18–19)
- **Model.** $\boldsymbol\beta$ are global latent variables (may govern any data); $\mathbf z$ are local latent variables, with $z_i$ governing only the $i$th data context:
$$p(\boldsymbol\beta,\mathbf z,\mathbf x)=p(\boldsymbol\beta)\prod_{i=1}^n p(z_i,x_i\mid\boldsymbol\beta)\tag{41}$$
The mixture of Gaussians is an example: global = component means, local = assignments (p. 18).
- **Assumptions.** The joint of each $(x_i,z_i)$ given $\boldsymbol\beta$ is exponential family, with sufficient statistic $t$:
$$p(z_i,x_i\mid\boldsymbol\beta)=h(z_i,x_i)\exp\{\boldsymbol\beta^\top t(z_i,x_i)-a(\boldsymbol\beta)\}\tag{42}$$
and the prior on $\boldsymbol\beta$ is the conjugate prior, with natural hyperparameter $\alpha=[\alpha_1,\alpha_2]^\top$:
$$p(\boldsymbol\beta)=h(\boldsymbol\beta)\exp\{\alpha^\top[\boldsymbol\beta,-a(\boldsymbol\beta)]-a(\alpha)\}\tag{43}$$
The complete conditional of $\boldsymbol\beta$ is then in the same family, with natural parameter
$$\hat\alpha=\Big[\alpha_1+\sum_{i=1}^n t(z_i,x_i),\ \alpha_2+n\Big]^\top\tag{44}$$
- **Local complete conditional.** From the form of (41), $z_i$ is conditionally independent of the other locals and data given $\boldsymbol\beta$ and $x_i$:
$$p(z_i\mid x_i,\boldsymbol\beta,\mathbf z_{-i},\mathbf x_{-i})=p(z_i\mid x_i,\boldsymbol\beta)\tag{45}$$
assumed exponential family (a property of the local likelihood):
$$p(z_i\mid x_i,\boldsymbol\beta)=h(z_i)\exp\{\eta(\boldsymbol\beta,x_i)^\top z_i-a(\eta(\boldsymbol\beta,x_i))\}\tag{46}$$
(In the mixture, it is categorical.) (p. 19.)
- **CAVI here.** $q(\boldsymbol\beta\mid\lambda)$ has global variational parameter $\lambda$ and the prior's family. $q(z_i\mid\varphi_i)$ has local parameter $\varphi_i$ and the local conditional's family. CAVI alternates:
$$\varphi_i=\mathbb E_\lambda[\eta(\boldsymbol\beta,x_i)]\tag{47}$$
$$\lambda=\Big[\alpha_1+\sum_{i=1}^n\mathbb E_{\varphi_i}[t(z_i,x_i)],\ \alpha_2+n\Big]^\top\tag{48}$$
These apply (40) to (45) and (44) (p. 19).
- **ELBO for monitoring** (constants omitted):
$$\mathrm{ELBO}=\Big(\alpha_1+\sum_{i=1}^n\mathbb E_{\varphi_i}[t(z_i,x_i)]\Big)^\top\mathbb E_\lambda[\boldsymbol\beta]-(\alpha_2+n)\,\mathbb E_\lambda[a(\boldsymbol\beta)]-\mathbb E[\log q(\boldsymbol\beta,\mathbf z)]\tag{49}$$
$$\mathbb E[\log q(\boldsymbol\beta,\mathbf z)]=\lambda^\top\mathbb E_\lambda[t(\boldsymbol\beta)]-a(\lambda)+\sum_{i=1}^n\varphi_i^\top\mathbb E_{\varphi_i}[z_i]-a(\varphi_i)\tag{50}$$
Algorithm 2 is an instance of this scheme. Appendix C (not in this unit) treats latent Dirichlet allocation (p. 19).

> **Intuition note.** The global update (Eq. 48) is the prior hyperparameters plus expected sufficient statistics summed over all data points; it has the form of the conjugate-posterior natural parameter (44), with expected statistics in place of observed ones. The local update asks what each data point thinks given the current global belief.

#### 4.3 Stochastic variational inference (pp. 19–21; part ends before Algorithm 3)
- **Why CAVI does not scale.** Each iteration passes through the entire data set. An alternative is gradient-based optimization. *Stochastic variational inference* (SVI, Hoffman et al., 2013) combines natural gradients with stochastic optimization (pp. 19–20). SVI optimizes the global parameters $\lambda$ of a conditionally conjugate model. It repeatedly (a) subsamples a data point; (b) computes the optimal local parameters for it given current global ones; (c) adjusts the global parameters (p. 20).
- **Natural gradient.** It accounts for the geometry of probability parameters: moving the same distance in different directions gives equal change in symmetrized KL (KL taken in both directions, so neither density is privileged), which the Euclidean gradient does not. In exponential families it is the usual gradient premultiplied by $a''(\lambda)^{-1}$, the inverse Fisher information (inverse covariance of the sufficient statistic) (p. 20). Hoffman et al. derive the Euclidean gradient for the global parameter:
$$\nabla_\lambda\mathrm{ELBO}=a''(\lambda)\big(\mathbb E_\varphi[\hat\alpha]-\lambda\big)\tag{51}$$
where $\mathbb E_\varphi[\hat\alpha]$ is the right side of (48). Premultiplying by the inverse Fisher information:
$$g(\lambda)=\mathbb E_\varphi[\hat\alpha]-\lambda\tag{52}$$
This is the coordinate update minus the current parameter, and it is easier to compute than the Euclidean gradient (p. 20).
- **Update.** With step size $\epsilon_t$,
$$\lambda_t=\lambda_{t-1}+\epsilon_t\,g(\lambda_{t-1})\tag{53}$$
Substituting (52):
$$\lambda_t=(1-\epsilon_t)\lambda_{t-1}+\epsilon_t\,\mathbb E_\varphi[\hat\alpha]\tag{54}$$
*(added step: $\lambda_{t-1}+\epsilon_t(\mathbb E_\varphi[\hat\alpha]-\lambda_{t-1})$ regroups into (54).)* The new estimate is a weighted mix of the coordinate update and the current parameter; no new kinds of computation are needed (p. 20).
- **Cost problem.** The full natural gradient still sums over the entire data set and computes optimal local parameters for every point, "prohibitively expensive" with massive data (p. 21).
- **Stochastic optimization.** Follows noisy but cheap gradients and reaches a local optimum of the ELBO. Robbins and Monro (1951) proved results implying that noisy, unbiased gradients can be used successfully if the step sizes satisfy certain conditions (p. 21). Expanding (52) with (44), where $\varphi_i^*$ denotes the optimal local parameters at fixed $\lambda$ from (47):
$$g(\lambda)=\alpha+\Big[\sum_{i=1}^n\mathbb E_{\varphi_i^*}[t(z_i,x_i)],\ n\Big]^\top-\lambda\tag{55}$$
Sample an index and rescale the second term:
$$t\sim\mathrm{Unif}(1,\dots,n)\tag{56}$$
$$\hat g(\lambda)=\alpha+n\big[\mathbb E_{\varphi_t^*}[t(z_t,x_t)],\ 1\big]^\top-\lambda\tag{57}$$
The authors state $\hat g$ is unbiased, $\mathbb E_t[\hat g(\lambda)]=g(\lambda)$, and cheap (one data point, one set of local parameters). *(added step: the expectation over $t$ gives $\frac1n\sum_t n[\cdot,1]=[\sum_i\cdot,\,n]$, which is (55).)* It extends to minibatches of $B$ points with appropriate rescaling. The first two terms of (57) equal the coordinate update in a model with $n$ replicates of the sampled point (p. 21).
- **Step sizes** must satisfy the Robbins–Monro conditions
$$\sum_t\epsilon_t=\infty;\qquad\sum_t\epsilon_t^2<\infty\tag{58}$$
for example $\epsilon_t=t^{-\kappa}$ with $\kappa\in(0.5,1]$. The authors emphasize that SVI needs no new derivation beyond CAVI: any CAVI implementation can be scaled up to a stochastic algorithm (p. 21). (Algorithm 3 appears after this unit's last page.)
- **Topic models (start).** The part ends as the authors introduce probabilistic topic models as the SVI demonstration: mixed-membership models of text where each topic is a distribution over a vocabulary and each document mixes topics in its own proportions (p. 21).

> **Intuition note.** The exact natural gradient is a sum over all data points. Picking one point and multiplying its contribution by $n$ gives a noisy estimate with the right average, so many cheap steps replace a few expensive ones.

## Toy example (ours, not from the text)
**Part A: ELBO = log evidence − KL.** One binary latent $z\in\{0,1\}$, prior $p(z=1)=0.5$, likelihoods $p(x\mid z=1)=0.8$, $p(x\mid z=0)=0.2$ for the observed $x$.
- Joint: $p(z{=}1,x)=0.4$, $p(z{=}0,x)=0.1$. Evidence $p(x)=0.5$, so $\log p(x)=\ln0.5=-0.6931$. Posterior: $(0.8,\,0.2)$ for $z=1,0$.
- Take $q=(0.5,0.5)$. ELBO $=\sum_z q(z)[\ln p(z,x)-\ln q(z)]=0.5(\ln0.4-\ln0.5)+0.5(\ln0.1-\ln0.5)=0.5(-0.2231)+0.5(-1.6094)=-0.9163$.
- KL$(q\|p(z|x))=0.5\ln(0.5/0.8)+0.5\ln(0.5/0.2)=0.5(-0.4700)+0.5(0.9163)=0.2231$.
- Check Eq. (14): $0.2231+(-0.9163)=-0.6932\approx\ln0.5$ ✓. With $q=(0.8,0.2)$ the KL is 0 and the ELBO equals $\ln0.5$ (the bound is tight).

**Part B: a CAVI update and the mean-field limit.** Two binary latents with posterior (treated as the joint, evidence 1): $p(0,0)=p(1,1)=0.4$, $p(0,1)=p(1,0)=0.1$.
- Start with $q_2=(0.5,0.5)$. By (18), $q_1(z_1)\propto\exp\{\sum_{z_2}q_2(z_2)\ln p(z_1,z_2)\}$.
- For $z_1=0$: $0.5\ln0.4+0.5\ln0.1=0.5(-0.9163)+0.5(-2.3026)=-1.6094$. For $z_1=1$: the same $-1.6094$. So $q_1=(0.5,0.5)$ and the update leaves $q$ unchanged (by symmetry, the same for $q_2$).
- The resulting product has $q(z_1,z_2)=0.25$ everywhere. Its KL: $2\times0.25\ln(0.25/0.4)+2\times0.25\ln(0.25/0.1)=-0.2350+0.4581=0.2231>0$. The marginals (0.5, 0.5) match the posterior's, but a product cannot reproduce the correlation, as in Figure 1.

## Concepts
- [[variational-inference-elbo]] — approximate the posterior by optimizing a member of a family $\mathcal Q$ to minimize KL(q‖p(z|x)), equivalently maximize the ELBO (pp. 2, 6)
- [[kl-divergence]] — asymmetric, nonnegative measure of proximity between densities; VI minimizes KL(q‖p), here with q first (pp. 3, 6)
- [[marginal-likelihood-evidence]] — $p(\mathbf x)=\int p(\mathbf z,\mathbf x)d\mathbf z$; its intractability is why inference is hard; ELBO lower-bounds its log (pp. 5, 7)
- [[elbo-evidence-lower-bound]] (new) — $\mathbb E[\log p(\mathbf z,\mathbf x)]-\mathbb E[\log q(\mathbf z)]$ = expected log likelihood − KL(q‖prior); equals $\log p(\mathbf x)-\mathrm{KL}$ (pp. 6–7)
- [[mean-field-family]] (new) — variational family with fully independent factors $q(\mathbf z)=\prod_j q_j(z_j)$; cannot capture correlation (p. 7)
- [[cavi-coordinate-ascent-vi]] (new) — iteratively set $q_j\propto\exp\{\mathbb E_{-j}[\log p(z_j,\mathbf z_{-j},\mathbf x)]\}$; finds a local ELBO optimum (p. 9)
- [[markov-chain-monte-carlo-mcmc]] — the baseline: sample an ergodic chain with the posterior as stationary law; asymptotically exact but heavier (pp. 2–3)
- [[gibbs-sampling]] — sample each variable from its complete conditional; CAVI uses the same conditional via an expected log (p. 10)
- [[complete-conditional]] (new) — $p(z_j\mid\mathbf z_{-j},\mathbf x)$, the conditional of one latent given all others and the data (p. 9)
- [[conjugate-prior]] — prior in the family matching the likelihood, giving a posterior in the same family; used in §4.2 (pp. 6, 18)
- [[conditionally-conjugate-model]] (new) — local/global latent variable model with exponential-family complete conditionals (pp. 18–19)
- [[natural-gradient]] (new) — gradient premultiplied by the inverse Fisher information, $a''(\lambda)^{-1}$; for the ELBO it gives $g(\lambda)=\mathbb E[\hat\alpha]-\lambda$ (p. 20)
- [[stochastic-variational-inference]] (new) — noisy unbiased natural-gradient steps from one sampled data point, Robbins–Monro step sizes (pp. 20–21)
- [[em-algorithm]] (new) — maximum-likelihood method for latent-variable models; assumes the posterior expectation is computable, unlike VI (p. 7)
- [[label-switching]] (new) — symmetric posterior modes from permuting cluster labels; one mode suffices for clusters or prediction (p. 11)
- [[log-sum-exp-trick]] (new) — Eq. (20), for numerically stable sums of exponentials (p. 11)
- [[hamiltonian-monte-carlo]] — an MCMC method that uses gradients of the log density; the Stan sampler (legend: NUTS, the No-U-Turn Sampler, a self-tuning HMC variant) used as the comparison baseline in Figure 6 (p. 16)

## Canonical instances
- [[bayesian-gaussian-mixture]] — unit-variance mixture with Gaussian prior on means; full CAVI derivation and ELBO (pp. 5, 12–14)
- [[mean-field-2d-gaussian]] — mean-field fit to a correlated 2-D Gaussian: same mean, decoupled covariance, underestimated marginal variance (p. 9)
- [[imageclef-color-histogram-clustering]] — 30-cluster mixture on 576-dim histograms of 10,000 images; CAVI vs. HMC sampler (pp. 16–17)
- [[probabilistic-topic-model]] — mixed-membership model of text, introduced as the SVI demonstration (p. 21)

## Bridges (candidates)
- [same-math] ELBO maximization ↔ bayesian: the Bayesian posterior as the optimum of "expected log likelihood − KL to prior" — Eq. (13) rewrites exactly as this balance
- [structural-analogy] CAVI's coordinate updates ↔ bayesian: Gibbs sampling — both cycle through complete conditionals, one sampling and one setting a factor from the expected log
- [structural-analogy] Variational EM ↔ bayesian: EM algorithm — both alternate local and global updates, with a variational E-step
- [structural-analogy] Mean-field underestimating variance ↔ bayesian: asymmetry of KL divergence — the KL(q‖p) direction penalizes q-mass outside p's support
- [same-math] SVI's noisy unbiased gradient with $\sum\epsilon_t=\infty$, $\sum\epsilon_t^2<\infty$ ↔ stochastic approximation (Robbins–Monro): the step-size conditions are the same ones

## Questions this raises
- When does mean-field's variance underestimation matter for a task, and how can it be corrected (the authors point to §5.2 and Giordano et al.)?
- How many local optima does the ELBO have in realistic models, and how should one initialize or compare optima (Figure 2)?
- If the ELBO is only a lower bound, when can it be trusted for model comparison, given the authors' remark that this is "not justified in theory"?
- How does SVI behave with minibatches, and what do the Robbins–Monro conditions imply for practical step sizes ($\kappa\in(0.5,1]$)?

## Reading notes
- **Part boundaries.** This part starts at p. 1 (title, abstract) and ends on p. 21, mid-§4.3, at the paragraph introducing probabilistic topic models. Algorithm 3 (SVI), the topic-model results, §5 (perspective, theory, open problems) and the appendices are not in these pages. The split falls at a section boundary per the source notes, but the printed page 21 ends inside §4.3.
- **Edition and pages.** The pages show the arXiv version (arXiv:1601.00670v9, dated May 11, 2018); the unit metadata cites the JASA version, whose layout is not shown here. Printed page = pdf page.
- **OCR.** The text layer of p. 9 is garbled (two overlapping versions); the image was used for Eq. (17)–(18). The p. 15 text layer has a stray "Figure 1: Main caption" artifact and mangled axis numbers. Figure 3 values (ELBO between about −4,100 and −3,200) were read from the image.
- **Possible inconsistency.** Figure 6's legend reads "NUTS (Hoffman et al. 2013)", while the text (p. 16) cites Hoffman and Gelman (2014) for the HMC-based sampler. I report both without resolving this.
- **Wording.** The "elbows" in the Figure 3 text are the authors' loose description of plateaus in the ELBO curve. The iteration numbers (20, 28, 35, 50) are the Figure 3 snapshot panels, not elbow locations read from the curve.
