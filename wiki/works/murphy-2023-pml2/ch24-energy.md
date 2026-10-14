---
id: murphy-2023-pml2/ch24-energy
work: murphy-2023-pml2
unit: "24 Energy-based models"
pages: 849-866
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
# Energy-based models (Murphy, ch. 24)

## L0 — One line
An energy-based model defines a density up to an intractable constant $Z_\theta$, so training must avoid computing $Z_\theta$: either by sampling the model (MCMC, contrastive divergence) or by using objectives in which $Z_\theta$ cancels (score matching, noise contrastive estimation, and others).

## L1 — The gist (≤ 120 words)
How do we fit $p_\theta(x)=\exp(-E_\theta(x))/Z_\theta$ when $Z_\theta$ cannot be computed? The chapter gives several routes. (1) Maximum likelihood, where $\nabla_\theta \log Z_\theta$ equals a model expectation that MCMC can estimate; contrastive divergence (CD) and persistent CD are cheaper approximations. (2) Score matching, which matches $\nabla_x \log p$ and so never touches $Z_\theta$, with denoising and sliced versions. (3) Noise contrastive estimation, which turns density fitting into classification against noise. (4) Other methods: KL-derivative, Stein-discrepancy and adversarial methods. Flexible energies (any neural network) are the payoff.

**Prerequisites:** Gibbs distribution; KL divergence; MCMC and Langevin dynamics; gradients and Jacobians; integration by parts; Bayes' rule; Jensen's inequality.

## L2 — Key ideas
- An EBM needs only an unnormalised energy, so energies can be added to combine "experts" (product of experts). The price is an intractable $Z_\theta$ (p. 849–850).
- The likelihood gradient is $-\nabla_\theta E_\theta(x)$ plus a model expectation, $\mathbb{E}_{p_\theta}[\nabla_\theta E_\theta]$, which sampling can estimate without bias (p. 851–852).
- Contrastive divergence starts a short MCMC chain at the data point; persistent CD keeps chains alive across steps. Truncated chains can give biased gradients (p. 852–855).
- Score matching minimises the Fisher divergence (the expected squared gap between the data score and the model score). The score of an EBM is $-\nabla_x E_\theta$, free of $Z_\theta$, and under regularity conditions integration by parts removes the unknown data score (p. 855–856).
- Denoising score matching is scalable but is inconsistent for clean data, and its variance explodes as $\sigma\to0$. Sliced score matching is consistent, and its second-derivative term costs only $O(d)$ (p. 857–859).
- Score matching is linked to one-step Langevin CD, and its Fisher divergence to the derivative of KL (de Bruijn) (p. 859–860).
- Noise contrastive estimation fits a noise-vs-data classifier. It yields $Z_\theta$ as a by-product, and with a shifted-data noise distribution it recovers sliced score matching (p. 860–862).
- Further routes include KL differences/derivatives, Stein discrepancy and adversarial training with a sampler $q_\phi$ (p. 863–865).

## L3 — Walkthrough

### 24.1 Introduction (p. 849)
VAEs, autoregressive models and flows are directed models that generate data step by step with locally normalised distributions. Sometimes it is easier to state constraints that valid samples must satisfy; an undirected model does this (p. 849).

An **energy-based model (EBM)** is a Gibbs distribution (p. 849):
$$p_\theta(x)=\frac{\exp(-E_\theta(x))}{Z_\theta}\tag{24.1}$$
$$Z_\theta=\int \exp(-E_\theta(x))\,dx\tag{24.2}$$
$Z_\theta$ is the **partition function**: constant in $x$, a function of $\theta$. EBMs usually make no Markov assumptions, so the integral is usually intractable. Approximate methods such as annealed importance sampling are then needed (p. 849).

The advantage is that the energy can be any function returning a non-negative scalar (the author's wording) and need not integrate to 1, so many neural architectures can define it (p. 849).

**24.1.1 Products of experts (p. 850).** Take $p_1$ (stable proteins) and $p_2$ (proteins that bind the COVID-19 spike receptor). The **product of experts** is
$$p_{12}(x)=\tfrac{1}{Z_{12}}p_1(x)p_2(x)\tag{24.3}$$
It gives high probability to proteins that are both stable and binding. A mixture of experts would generate from $p_1$ or from $p_2$ but would not combine features (p. 850). If experts are EBMs, the PoE is an EBM with
$$E_{12}(x)=E_1(x)+E_2(x)\tag{24.4}$$
Each energy term acts as a "soft constraint" (Fig. 24.1, p. 850).

*Intuition note.* Adding energies multiplies densities. A point must score well on every expert to keep low total energy, so the model asks for A and B together.

**24.1.2 Difficulties (p. 850).** Computing the likelihood and drawing samples are generally intractable; the chapter surveys approximations.

### 24.2 Maximum likelihood training (p. 850–855)
Maximise the expected log-likelihood (p. 851):
$$\ell(\theta)=\mathbb{E}_{x\sim p_D}[\log p_\theta(x)]\tag{24.5}$$
$$\ell(\theta)=-D_{KL}(p_D\,\|\,p_\theta)+\text{const}\tag{24.6}$$
The constant is $\mathbb{E}_{p_D}[\log p_D]$, which does not depend on $\theta$. The likelihood itself is not computable, but its gradient can be estimated with MCMC (p. 851):
$$\nabla_\theta\log p_\theta(x)=-\nabla_\theta E_\theta(x)-\nabla_\theta\log Z_\theta\tag{24.7}$$
The first term is easy by automatic differentiation. The second is rewritten step by step (p. 851):
$$\nabla_\theta\log Z_\theta=\nabla_\theta\log\int e^{-E_\theta(x)}dx\tag{24.8}$$
$$\overset{(i)}{=}\Big(\int e^{-E_\theta}dx\Big)^{-1}\nabla_\theta\int e^{-E_\theta}dx\tag{24.9}$$
$$=\Big(\int e^{-E_\theta}dx\Big)^{-1}\int\nabla_\theta e^{-E_\theta}dx\tag{24.10}$$
$$\overset{(ii)}{=}\Big(\int e^{-E_\theta}dx\Big)^{-1}\int e^{-E_\theta}(-\nabla_\theta E_\theta)dx\tag{24.11}$$
$$=\int\Big(\int e^{-E_\theta}dx\Big)^{-1}e^{-E_\theta}(-\nabla_\theta E_\theta)dx\tag{24.12}$$
$$\overset{(iii)}{=}\int\tfrac{1}{Z_\theta}e^{-E_\theta}(-\nabla_\theta E_\theta)dx\tag{24.13}$$
$$\overset{(iv)}{=}\int p_\theta(x)(-\nabla_\theta E_\theta(x))dx\tag{24.14}$$
$$=\mathbb{E}_{x\sim p_\theta}[-\nabla_\theta E_\theta(x)]\tag{24.15}$$
Steps (i), (ii) use the chain rule; (iii), (iv) use (24.1)–(24.2). Hence an unbiased Monte Carlo estimate is
$$\nabla_\theta\log Z_\theta\simeq-\frac1S\sum_{s=1}^S\nabla_\theta E_\theta(\tilde x_s),\quad \tilde x_s\sim p_\theta\tag{24.16}$$
With model samples we can do stochastic gradient ascent (p. 851–852).

*Intuition note.* Raising the likelihood lowers the energy of data points. The correction term raises the energy of points the model itself currently likes, so the model cannot give low energy to everything.

**24.2.1 Gradient-based MCMC (p. 852).** Langevin MCMC and Hamiltonian Monte Carlo use the gradient wrt $x$, called the Hyvärinen score function, which is easy because $Z_\theta$ drops out:
$$\nabla_x\log p_\theta(x)=-\nabla_xE_\theta(x)-\underbrace{\nabla_x\log Z_\theta}_{=0}=-\nabla_xE_\theta(x)\tag{24.17}$$
Langevin sampling: draw $x^0$ from a simple prior, then for $k=0,\dots,K-1$, step size $\epsilon>0$:
$$x^{k+1}\leftarrow x^k+\tfrac{\epsilon^2}{2}\nabla_x\log p_\theta(x^k)+\epsilon z^k,\quad z^k\sim\mathcal N(0,I)\tag{24.18}$$
As $\epsilon\to0$, $K\to\infty$, $x^K$ is guaranteed to follow $p_\theta$ under some regularity conditions. In practice a small finite $\epsilon$ is used; the discretisation error is typically negligible or can be corrected with a Metropolis–Hastings step (p. 852).

**24.2.2 Contrastive divergence (CD) (p. 852).** Running MCMC to convergence is expensive. In CD the chain is initialised at the data point $x$ and run for a fixed number of steps. One can show $T$ steps of CD minimise
$$CD_T=D_{KL}(p_0\,\|\,p_\infty)-D_{KL}(p_T\,\|\,p_\infty)\tag{24.19}$$
with $p_T$ the distribution after $T$ updates and $p_0$ the data distribution. Small $T$, sometimes $T=1$, typically works well (p. 852).

**24.2.2.1 RBMs with CD (p. 853–854).** CD was developed for restricted Boltzmann machines (latent-variable EBMs built for fast block Gibbs sampling). With binary units, energy (p. 853):
$$E(x,z;\theta)=\sum_{d=1}^D\sum_{k=1}^K x_dz_kW_{dk}+\sum_d x_db_d+\sum_k z_kc_k\tag{24.20}$$
Bias terms are then dropped (emulated by clamping $z_k=1$ or $x_d=1$). The log-likelihood gradient is clamped minus unclamped expectations:
$$\frac{\partial\ell}{\partial w_{dk}}=\frac1N\sum_{n=1}^N\mathbb E[x_dz_k|x_n,\theta]-\mathbb E[x_dz_k|\theta]\tag{24.21}$$
$$\nabla_w\ell=\mathbb E_{p_D(x)p(z|x,\theta)}[xz^T]-\mathbb E_{p(z,x|\theta)}[xz^T]\tag{24.22}$$
The first term is the clamped phase ($x$ fixed to data), the second the unclamped phase. When model and empirical expectations match, the gradient is zero and learning stops. The first term is Hebbian, the second anti-Hebbian: Hebb's rule says connections between simultaneously active neurons strengthen, "Cells that fire together wire together" (p. 853). Using the bipartite structure, the expectations are approximated by
$$z_n\sim p(z|x_n,\theta)\tag{24.23}$$
$$x_n'\sim p(x|z_n,\theta)\tag{24.24}$$
$$z_n'\sim p(z|x_n',\theta)\tag{24.25}$$
$$\mathbb E_{p(\cdot|\theta)}[xz^T]\approx x_n(z_n')^T\tag{24.26}$$
$x_n'$ is a reconstruction ("fantasy data", Fig. 24.2). In practice $\mathbb E[z|x_n']$ replaces $z_n'$ to reduce variance. Replacing the sample $z_n$ in (24.23) by $\mathbb E[z|x_n]$ is not valid: each hidden unit could then pass more than 1 bit, so it would not act as much of a bottleneck (p. 854).

Algorithm 24.1 (CD-1, shapes $W\in\mathbb R^{D\times K}$, $x_n\in\mathbb R^D$, $\mu_n\in\mathbb R^K$): per case, compute $\mu_n=\mathbb E[z|x_n]$; sample $z_n$, then $x_n'$; compute $\mu_n'=\mathbb E[z|x_n']$; gradient $x_n\mu_n^T-x_n'\mu_n'^T$ ($D\times K$); average over the minibatch; $W:=W+\eta_t\frac1Bg$ (p. 854).

**24.2.2.2 Persistent CD (PCD) (p. 854–855).** One chain with persistent state is used; it is not restarted at each new data point. Its state carries over and initialises the next training step's chain (Algorithm 24.2). Two processes run at different time scales: states $x$ fast, parameters $\theta$ slow. Justification [You89]: $p(x|\theta_t)$ is likely close to $p(x|\theta_{t-1})$ since one SGD step changes parameters little, so a few steps from the old state suffice (p. 855).

**24.2.2.3 Other methods (p. 855).** Replay buffers of past chain states can further improve PCD. Variants include mean-field and multi-grid CD. EBMs trained with CD may not capture the data distribution faithfully, because truncated MCMC can lead to biased gradient updates. Remedies include coupled-MCMC unbiased estimators and differentiating through the sampler with an entropy correction (Du et al.) (p. 855).

### 24.3 Score matching (SM) (p. 855–860)
If two continuously differentiable log-densities have equal first derivatives everywhere, they differ by a constant. Normalisation then forces them to be equal, so matching $x$-gradients of log densities can learn an EBM; if they match, the EBM captures the data distribution exactly (p. 855–856). The (Stein) score is $\nabla_x\log p_\theta(x)$, distinct from the Fisher score $\nabla_\theta\log p_\theta(x)$. For an EBM:
$$s_\theta(x)\triangleq\nabla_x\log p_\theta(x)=-\nabla_xE_\theta(x)\tag{24.27}$$
which does not involve $Z_\theta$. SM minimises the **Fisher divergence** (p. 856):
$$D_F(p_D\|p_\theta)=\mathbb E_{p_D}\Big[\tfrac12\|\nabla_x\log p_D(x)-\nabla_x\log p_\theta(x)\|^2\Big]\tag{24.28}$$
The expectation can be estimated by the empirical mean, but $\nabla_x\log p_D$ is unknown (p. 856).

**24.3.1 Basic SM (p. 856).** Under regularity conditions [Hyv05b], integration by parts replaces the unknown data score with second derivatives of $E_\theta$ ($d=\dim x$, $J_x s_\theta$ the Jacobian of the score):
$$D_F=\mathbb E_{p_D}\Big[\tfrac12\sum_{i=1}^d\Big(\tfrac{\partial E_\theta}{\partial x_i}\Big)^2-\tfrac{\partial^2E_\theta}{\partial x_i^2}\Big]+\text{const}\tag{24.29}$$
$$=\mathbb E_{p_D}\Big[\tfrac12\|s_\theta(x)\|^2+\mathrm{tr}(J_xs_\theta(x))\Big]+\text{const}\tag{24.30}$$
The constant can be dropped. Estimators are consistent under some regularity conditions: minimising (24.28) converges to the true parameters with infinite data. Downside: the trace costs $O(d^2)$, so the objective has only been applied to relatively simple energies. SM assumes a continuous data distribution with positive density; generalisations to discrete or bounded data and to higher-order gradients exist (p. 856).

*Intuition note.* Matching slopes of the log-density needs no normaliser. Integration by parts trades the unknown data slope for curvature of the model, which we can differentiate.

**24.3.2 Denoising SM (DSM) (p. 857–858).** SM needs $\log p_D$ continuously differentiable and finite. Digital images are discrete and bounded, so $\log p_D=-\infty$ outside the pixel range and SM does not apply. Add smooth noise, $\tilde x=x+\epsilon$; the noisy density $q(\tilde x)=\int q(\tilde x|x)p_D(x)dx$ is smooth, so $D_F(q\|p_\theta)$ is a proper objective. [KL10]: this approximates noiseless SM plus a regulariser but still needs second derivatives. [Vin11] shows (p. 857):
$$D_F(q(\tilde x)\|p_\theta(\tilde x))=\mathbb E_{q(\tilde x)}\Big[\tfrac12\|\nabla_{\tilde x}\log p_\theta(\tilde x)-\nabla_{\tilde x}\log q(\tilde x)\|_2^2\Big]\tag{24.31}$$
$$=\mathbb E_{q(x,\tilde x)}\Big[\tfrac12\|\nabla_{\tilde x}\log p_\theta(\tilde x)-\nabla_{\tilde x}\log q(\tilde x|x)\|_2^2\Big]\tag{24.32}$$
$$=\tfrac12\mathbb E_{q(x,\tilde x)}\Big[\Big\|s_\theta(\tilde x)-\tfrac{x-\tilde x}{\sigma^2}\Big\|_2^2\Big]+\text{const}\tag{24.33}$$
with, for Gaussian noise,
$$\nabla\log q(\tilde x|x)=\nabla\log\mathcal N(\tilde x|x,\sigma^2I)=\frac{-(\tilde x-x)}{\sigma^2}\tag{24.34}$$
The target $x-\tilde x$ points from noisy to clean input, so the score learns to denoise. To estimate: sample $x\sim p_D$, then noise. Related to Tweedie's formula and Stein's unbiased risk estimation (p. 857).

*Difficulties (p. 857–858).* If $p_D$ already satisfies SM's conditions, then $D_F(q\|p_\theta)\ne D_F(p_D\|p_\theta)$. DSM is then not consistent, since the optimum matches $q$, not $p_D$, and this matters when $q$ differs much from $p_D$. Choosing $q\approx p_D$ (small $\sigma$) raises variance. With $\sigma\approx0$:
$$D_F=\mathbb E_{p_D}\mathbb E_{z\sim\mathcal N(0,I)}\Big[\tfrac12\Big\|\tfrac z\sigma+\nabla_x\log p_\theta(x+\sigma z)\Big\|_2^2\Big]\simeq\tfrac1{2N}\sum_{i=1}^N\Big\|\tfrac{z^{(i)}}\sigma+\nabla_x\log p_\theta(x^{(i)}+\sigma z^{(i)})\Big\|_2^2\tag{24.35}$$
and as $\sigma\to0$, a Taylor expansion gives
$$\tfrac1{2N}\sum_{i=1}^N\Big[\tfrac2\sigma(z^{(i)})^T\nabla_x\log p_\theta(x^{(i)})+\tfrac{\|z^{(i)}\|_2^2}{\sigma^2}\Big]+\text{const}\tag{24.36}$$
The variances of $(z^{(i)})^T\nabla_x\log p_\theta(x^{(i)})/\sigma$ and $\|z^{(i)}\|_2^2/\sigma^2$ grow unbounded as $\sigma\to0$ (p. 858).

**24.3.3 Sliced SM (SSM) (p. 858–859).** SSM [Son+19] is both consistent and computationally efficient. It projects both scores on a random vector $v$ and compares scalars. The **sliced Fisher divergence**, with $p(v)$ such that $\mathbb E_{p(v)}[vv^T]$ is positive definite, is
$$D_{SF}=\mathbb E_{p_D}\mathbb E_{p(v)}\Big[\tfrac12(v^T\nabla_x\log p_D-v^T\nabla_x\log p_\theta)^2\Big]\tag{24.37}$$
with the implicit form (as printed)
$$D_{SF}=\mathbb E_{p_D}\mathbb E_{p(v)}\Big[\tfrac12\sum_{i}\Big(\tfrac{\partial E_\theta}{\partial x_i}v_i\Big)^2+\sum_i\sum_j\tfrac{\partial^2E_\theta}{\partial x_i\partial x_j}v_iv_j\Big]+C\tag{24.38}$$
The second-derivative term costs $O(d)$ because
$$\sum_i\sum_j\tfrac{\partial^2E_\theta}{\partial x_i\partial x_j}v_iv_j=\sum_i\tfrac{\partial}{\partial x_i}\underbrace{\Big(\sum_j\tfrac{\partial E_\theta}{\partial x_j}v_j\Big)}_{:=f(x)}v_i\tag{24.39}$$
and $f(x)$ is the same for all $i$: one $O(d)$ computation, plus $O(d)$ for the outer sum, versus $O(d^2)$ for SM (p. 859). For $p(v)=\mathcal N(0,I)$ the first term is available in closed form:
$$\mathbb E_{p_D}\mathbb E_{p(v)}\Big[\tfrac12\sum_i\Big(\tfrac{\partial E_\theta}{\partial x_i}v_i\Big)^2\Big]=\mathbb E_{p_D}\Big[\tfrac12\sum_i\Big(\tfrac{\partial E_\theta}{\partial x_i}\Big)^2\Big]\tag{24.40}$$
(added step: this holds because $\mathbb E[v_iv_j]=\delta_{ij}$.) Hence
$$D_{SF}=\mathbb E_{p_D}\mathbb E_{v\sim\mathcal N(0,I)}\Big[\tfrac12\sum_i\Big(\tfrac{\partial E_\theta}{\partial x_i}\Big)^2+\sum_i\sum_j\tfrac{\partial^2E_\theta}{\partial x_i\partial x_j}v_iv_j\Big]+C\tag{24.41}$$
$$=\mathbb E_{p_D}\mathbb E_{v\sim\mathcal N(0,I)}\Big[\tfrac12(v^Ts_\theta(x))^2+v^T[Jv]\Big]\tag{24.42}$$
with $J=J_xs_\theta(x)$; $Jv$ is a Jacobian–vector product. (24.41) also arises by applying the Hutchinson trace estimator to (24.30). It often (but not always) has lower variance than (24.38) (p. 859).

**24.3.4 Link to CD (p. 859–860).** SM can be viewed as a special instance of CD in the limit of a particular MCMC sampler [Hyv07a]; the Fisher divergence is related to the derivative of KL [Cov99]. Langevin in this form:
$$x^{k+1}\leftarrow x^k-\tfrac\epsilon2\nabla_xE_\theta(x^k)+\sqrt\epsilon\,z^k\tag{24.43}$$
With one Langevin step in CD, the gradient is
$$\mathbb E_{p_D}[\nabla_\theta\log p_\theta]=-\mathbb E_{p_D}[\nabla_\theta E_\theta]+\mathbb E_{x\sim p_\theta}[\nabla_\theta E_\theta]\simeq-\mathbb E_{p_D}[\nabla_\theta E_\theta]+\mathbb E_{p_\theta,z}\Big[\nabla_\theta E_\theta\Big(x-\tfrac{\epsilon^2}2\nabla_xE_{\theta'}(x)+\epsilon z\Big)\Big|_{\theta'=\theta}\Big]\tag{24.44}$$
After Taylor expansion in $\epsilon$ and algebra [Hyv07a], this becomes
$$\tfrac{\epsilon^2}2\nabla_\theta D_F(p_D\|p_\theta)+o(\epsilon^2)\tag{24.45}$$
For small $\epsilon$ this is a re-scaled gradient of the SM objective. The deeper reason is de Bruijn's identity, with $q_t,p_{\theta,t}$ the data and model smoothed by Gaussian noise of variance $t$:
$$\tfrac{d}{dt}D_{KL}(q_t\|p_{\theta,t})=-\tfrac12D_F(q_t\|p_{\theta,t})$$

**24.3.5 Score-based generative models (p. 860).** One can learn $s_\theta(x)$ directly (Section 25.3). Such unconstrained score models need not be conservative vector fields (gradients of some function). Both approaches seem to give comparable results [SH21].

### 24.4 Noise contrastive estimation (NCE) (p. 860–861)
NCE [GH10] learns an EBM by contrasting it with a noise distribution $p_n$ of known, tractable density. Let $y$ be Bernoulli, with mixture $p_{n,data}(x)=p(y=0)p_n(x)+p(y=1)p_D(x)$. Bayes' rule gives (p. 861):
$$p_{n,data}(y=0|x)=\frac{p_n(x)}{p_n(x)+\nu p_D(x)},\quad\nu=\frac{p(y=1)}{p(y=0)}\tag{24.46}$$
The model is $p_\theta(x)=\exp(-E_\theta(x))/Z_\theta$ (24.47), with $Z_\theta$ treated as a **learnable scalar parameter** (unlike most EBMs). The noise/model posterior is
$$p_{n,\theta}(y=0|x)=\frac{p_n(x)}{p_n(x)+\nu p_\theta(x)}\tag{24.48}$$
Fit it by conditional maximum likelihood:
$$\theta^*=\arg\min_\theta\mathbb E_{p_{n,data}(x)}[D_{KL}(p_{n,data}(y|x)\|p_{n,\theta}(y|x))]=\arg\max_\theta\mathbb E_{p_{n,data}(x,y)}[\log p_{n,\theta}(y|x)]\tag{24.49–24.50}$$
If the model is powerful enough, the posteriors match at the optimum:
$$p_{n,\theta^*}(y{=}0|x)\equiv p_{n,data}(y{=}0|x)\iff\frac{p_n}{p_n+\nu p_{\theta^*}}\equiv\frac{p_n}{p_n+\nu p_D}\iff p_{\theta^*}\equiv p_D\tag{24.51–24.53}$$
So $E_{\theta^*}$ is an unnormalised energy matching the data and $Z_{\theta^*}$ is its normaliser. Unlike CD and SM, NCE gives the normalising constant as a by-product. For very expressive EBMs one can absorb $Z_\theta$ into the energy (fix $Z_\theta=1$), giving a self-normalised EBM with a normaliser close to 1 (p. 861).

The choice of $p_n$ is critical, especially for structured, high-dimensional data. NCE works best when the noise is close to, but not exactly, the data distribution [GH12]. Adversarial, conditional and flow-based methods tune the noise. NCE generalises via Bregman divergences (p. 861).

**24.4.1 Link to score matching (p. 862).** With suitable $p_n$ and parameterisation, NCE recovers score matching [GH12]. Take a small deterministic vector $v$ and $p_n(x)=p_D(x-v)$. Sampling is easy ($x=x'+v$), but its density is unknown, so replace $p_n(x)$ by $p_\theta(x-v)$:
$$p_{n,\theta}(y=0|x):=\frac{p_\theta(x-v)}{p_\theta(x)+p_\theta(x-v)}\tag{24.54}$$
The NCE objective (24.50) reduces to (as printed)
$$\theta^*=\arg\min_\theta\mathbb E_{p_D}[\log(1+\exp(E_\theta(x)-E_\theta(x-v)))+\log(1+\exp(E_\theta(x)-E_\theta(x+v)))]\tag{24.55}$$
At the optimum, (24.56)–(24.57) give $\frac{p_{\theta^*}(x-v)}{p_{\theta^*}(x)+p_{\theta^*}(x-v)}\equiv\frac{p_D(x-v)}{p_D(x)+p_D(x-v)}$, which implies $p_{\theta^*}\equiv p_D$. For $\|v\|_2\approx0$, a Taylor expansion gives the equivalent form
$$\arg\min_\theta\tfrac14\mathbb E_{p_D}\Big[\tfrac12\sum_i\Big(\tfrac{\partial E_\theta}{\partial x_i}v_i\Big)^2+\sum_i\sum_j\tfrac{\partial^2E_\theta}{\partial x_i\partial x_j}v_iv_j\Big]+2\log2+o(\|v\|_2^2)\tag{24.58}$$
This equals the SSM objective (24.38) if the $o(\|v\|_2^2)$ terms are ignored and $v$ is drawn from a user-chosen $p(v)$ (p. 862).

### 24.5 Other methods (p. 862–865)
**24.5.1 Differences/derivatives of KL (p. 863).** The partition function often cancels when taking a difference of two closely related KLs, or a derivative. In minimum velocity learning and minimum probability flow, a Markov chain has $p_0\equiv p_D$ and $p_\infty\equiv p_\theta$. These methods minimise the "velocity" of its evolution:
$$\tfrac d{dt}D_{KL}(p_t\|p_\theta)\big|_{t=0}\ \text{ or }\ \tfrac d{dt}D_{KL}(p_D\|p_t)\big|_{t=0}\tag{24.59}$$
These typically do not need $Z_\theta$. In minimum KL contraction, a transformation $\Phi$ satisfies
$$D_{KL}(p\|q)\ge D_{KL}(\Phi\{p\}\|\Phi\{q\})\tag{24.60}$$
with equality if and only if $p=q$. Minimise
$$D_{KL}(p_D\|p_\theta)-D_{KL}(\Phi\{p_D\}\|\Phi\{p_\theta\})\tag{24.61}$$
which does not require $Z_\theta$ whenever $\Phi$ is linear. All three can be viewed as generalisations of SM and NCE (p. 863).

**24.5.2 Stein discrepancy (p. 863–864).**
$$D_{Stein}(p_D\|p_\theta):=\sup_{f\in\mathcal F}\mathbb E_{p_D}[\nabla_x\log p_\theta(x)^Tf(x)+\mathrm{trace}(\nabla_xf(x))]\tag{24.62}$$
$\mathcal F$ is a family of vector-valued functions. With regularity conditions, $D_S\ge0$, with equality iff $p_D\equiv p_\theta$. Only the score of $p_\theta$ appears, so $Z_\theta$ is not needed. The trace term may be expensive. Two fixes: take $\mathcal F$ as the unit ball of an RKHS (kernelised Stein discrepancy; the trace term is then constant), or approximate the trace with the Skilling–Hutchinson estimator (p. 864).

**24.5.3 Adversarial training (p. 864–865).** To avoid costly MCMC, introduce a variational $q_\phi$:
$$\mathbb E_{p_D}[\log p_\theta]=\mathbb E_{p_D}[-E_\theta]-\log\!\int q_\phi\tfrac{e^{-E_\theta}}{q_\phi}dx\ \overset{(i)}{\le}\ \mathbb E_{p_D}[-E_\theta]-\mathbb E_{q_\phi}[-E_\theta]-H(q_\phi)\tag{24.63}$$
Step (i) is Jensen's inequality, so this is an upper bound on the expected log-likelihood. Minimise it over $\phi$ (to tighten it), then maximise over $\theta$ as a surrogate for likelihood:
$$\max_\theta\min_\phi\ \mathbb E_{q_\phi}[E_\theta(x)]-\mathbb E_{p_D}[E_\theta(x)]-H(q_\phi)\tag{24.64}$$
This is similar to GAN training. $q_\phi$ needs fast sampling and tractable entropy, which usually restricts it to invertible models (e.g. inverse autoregressive flow) (p. 864). Alternatives (p. 864–865):
- Neural samplers $x=g_\phi(z)$ make sampling cheap but $H(q_\phi)$ intractable. Proposed fixes: heuristics; a mutual-information estimate, $H(q_\phi(z))=I(g_\phi(z),z)$; or, when $p_\theta=p_0e^{-E_\theta}/Z_\theta$, replacing $-H(q_\phi)$ by $D_{KL}(q_\phi\|p_0)$.
- A noisy sampler $g_\phi(z)+\sigma\epsilon$ makes $\nabla_\phi H$ easy to estimate.
- Xie et al. train a noisy sampler on MCMC samples and use its output to initialise new chains. This may still need several MCMC steps and does not optimise (24.63).
- Yu et al.: with adversarial training plus MCMC, EBMs can be trained with an arbitrary $f$-divergence.

## Toy example (ours)
Let $x\in\mathbb R$ and $E_\theta(x)=\theta x^2/2$ with $\theta>0$. Then $p_\theta=\mathcal N(0,1/\theta)$ and $Z_\theta=\sqrt{2\pi/\theta}$, so $\log Z_\theta=\tfrac12\log2\pi-\tfrac12\log\theta$ and $\nabla_\theta\log Z_\theta=-\tfrac1{2\theta}$.

Check (24.15): $\mathbb E_{p_\theta}[-\nabla_\theta E_\theta]=-\tfrac12\mathbb E[x^2]=-\tfrac12\cdot\tfrac1\theta=-\tfrac1{2\theta}$ ✓.

Take $\theta=2$: $\nabla_\theta\log Z=-0.25$. With four hypothetical draws from $\mathcal N(0,0.5)$, $\tilde x=0.5,-1,0,0.7$, estimate (24.16): $-\tfrac14\sum\tilde x^2/2=-(0.25+1+0+0.49)/8=-1.74/8=-0.2175$, close to $-0.25$.

If the data have $\mathbb E_{p_D}[x^2]=1$, the likelihood gradient by (24.7) is $-\tfrac12\cdot1-(-0.25)=-0.25$ at $\theta=2$, so $\theta$ decreases. It is zero when $-\tfrac12+\tfrac1{2\theta}=0$, i.e. $\theta=1$: the model's $\mathbb E[x^2]=1/\theta$ matches the data's. This mirrors the clamped-minus-unclamped logic: learning stops when model and data expectations agree.

## Concepts
- [[energy-based-model]] (new) — density $\propto\exp(-E_\theta(x))$ with arbitrary energy function (p. 849)
- [[partition-function]] (new) — $Z_\theta=\int e^{-E_\theta}dx$; constant in $x$, usually intractable (p. 849)
- [[product-of-experts]] (new) — product of densities; energies add; conjunction of features (p. 850)
- [[kl-divergence]] — MLE equals minimising $D_{KL}(p_D\|p_\theta)$ (p. 851) (reuse: KL divergence)
- [[monte-carlo-integration]] — unbiased estimate of $\nabla\log Z$ from model samples (p. 851) (reuse)
- [[mcmc]] — sampling the EBM inside the training loop (p. 852) (reuse: Markov chain Monte Carlo)
- [[langevin-mcmc]] (new) — gradient-plus-noise sampler using $-\nabla_xE_\theta$ (p. 852)
- [[contrastive-divergence]] (new) — MCMC from data points for $T$ steps; minimises (24.19) (p. 852)
- [[persistent-contrastive-divergence]] (new) — chains carried over between parameter updates (p. 854)
- [[restricted-boltzmann-machine]] (new) — bipartite latent-variable EBM supporting block Gibbs (p. 853)
- [[score-function-stein]] (new) — $\nabla_x\log p$, free of $Z_\theta$ for EBMs; not the Fisher score (p. 856)
- [[score-matching]] (new) — minimise the Fisher divergence via integration by parts (p. 856)
- [[denoising-score-matching]] (new) — match the noisy-data score; not consistent for clean data (p. 857)
- [[sliced-score-matching]] (new) — compare random 1-d projections of scores; consistent; second-derivative term $O(d)$ (p. 858)
- [[noise-contrastive-estimation]] (new) — noise-vs-data classification; $Z_\theta$ learned as a parameter (p. 860)
- [[stein-discrepancy]] (new) — sup over test functions $f$; needs only the model score (p. 863)

## Canonical instances
- [[protein-poe]] — stable plus binding proteins as a product of two experts (p. 850)
- [[rbm-cd1]] — CD-1 training of a binary RBM, Algorithm 24.1 (p. 853–854)
- [[image-pixel-dsm]] — discrete bounded pixels make plain SM inapplicable, motivating DSM (p. 857)
- [[nce-shifted-data-noise]] — noise $p_D(x-v)$ recovers sliced SM (p. 862)

## Bridges (candidates)
- [same-math] $\nabla_\theta\log Z_\theta=\mathbb E_{p_\theta}[-\nabla_\theta E_\theta]$ ↔ exponential families: gradient of the log-normaliser equals the expected sufficient statistic — same identity for $E_\theta=-\theta^T\phi(x)$ (added link; not stated here).
- [structural-analogy] CD clamped vs unclamped phases ↔ Hebbian vs anti-Hebbian learning (p. 853).
- [structural-analogy] NCE ↔ logistic regression / classifier-based density-ratio estimation: the classifier is linked to the density ratio via Bayes' rule (p. 861).
- [structural-analogy] Adversarial EBM objective (24.64) ↔ GAN training, with $q_\phi$ as generator and $E_\theta$ as critic (p. 864).
- [structural-analogy] DSM target $(x-\tilde x)/\sigma^2$ ↔ diffusion models' denoising (the text points to Section 25.3) (p. 857).

## Questions this raises
- When do truncated CD chains give biased gradients large enough to matter, and how do the debiasing methods in 24.2.2.3 compare?
- How should $\sigma$ in DSM be chosen to trade off bias (inconsistency) against the variance blow-up?
- Why does NCE work best when noise is close to, but not equal to, the data distribution?
- Which of the Fisher, KL, Stein and $f$-divergence objectives is best for which data type, given their different assumptions?

## Reading notes
- Page offset: printed = pdf − 34. pdf 900 (printed 866) is blank.
- Algorithm 24.2 line 10 as printed is $g_t=-(\frac1B\sum g_b)-(\frac1S\sum\tilde g_s)$. By (24.7) and (24.16) the model-sample term should enter with a plus sign; this looks like a misprint in the image. The text says "See Algorithm 12", but the algorithm shown is 24.2. The Langevin paragraph points to "Figure 25.5d", which is not in this unit.
- Sign conventions look inconsistent as printed. (24.20) has $+x_dz_kW_{dk}$ in the energy, but (24.21) has clamped minus unclamped, which would match a negative-sign energy. In (24.38), (24.41) and (24.58) the Hessian term of $E_\theta$ enters with +, whereas (24.29) has −. In (24.42) the term is $v^TJv$ with $J=J_xs_\theta$, and by (24.27) $J_xs_\theta=-\nabla^2E_\theta$. I copied the equations as printed.
- (24.18) uses $\epsilon^2/2$ and $\epsilon z$; (24.43) uses $\epsilon/2$ and $\sqrt\epsilon z$. These are the same scheme under a reparameterisation of $\epsilon$ (my reading). (24.34) is printed with $\nabla_x$ although the gradient used in (24.32) is wrt $\tilde x$. On p. 865 the text calls the adversarial objective "minimax objective in Equation (24.63)", but the objective is (24.64) (p. 864).
- The text says the energy "returns a non-negative scalar" (p. 849); (24.1) only needs $\int e^{-E}$ to be finite (my remark, not stated in the text). Exercises: none in this unit.
