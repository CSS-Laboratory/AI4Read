---
id: murphy-2023-pml2/ch25-diffusion
work: murphy-2023-pml2
unit: "25 Diffusion models"
pages: 867-892
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
# Diffusion models

## L0 — One line
Diffusion models generate data by learning to reverse a fixed process that gradually turns data into Gaussian noise. Training reduces to predicting the added noise (equivalently, the score), and the same model can be run as a stochastic or a deterministic sampler.

## L1 — The gist (≤ 120 words)
How can we build a generative model that is easy to train at scale and gives diverse, high-quality samples? The chapter starts from a fixed noising chain and a learned denoising chain (DDPM). Fitting it by the evidence lower bound (ELBO) reduces to a weighted least-squares noise-prediction loss. It then shows that this is equivalent to learning scores at many noise scales (SGM). The continuous-time limit gives stochastic differential equations (SDEs) and a deterministic ordinary differential equation (ODE), which lead to faster samplers, flow matching, distillation, latent-space diffusion, conditional generation with guidance, and diffusion on discrete states. This matters because one simple objective supports very large models and many data types.

**Prerequisites:** Gaussian conditioning and Bayes' rule; ELBO and KL divergence (VAEs); score function and score matching; basic ODE/SDE notation; row-stochastic matrices.

## L2 — Key ideas (5–10 bullets)
- The forwards process is a fixed linear-Gaussian Markov chain with closed-form marginal $q(x_t|x_0)$. In the basic DDPM only the reverse (decoder) process is learned (the VDM extension also learns the noise level), which keeps training simple (pp. 867–869, 872).
- The negative ELBO splits into $L_T$, $L_{t-1}$ and $L_0$ via a telescoping sum. Each KL term is Gaussian and computable analytically (pp. 870–871).
- Predicting the noise $\epsilon$ instead of the mean gives a weighted least-squares loss. Empirically, setting the weight to 1 ($L_{\text{simple}}$) gives better-looking samples (p. 871).
- Score-based generative models with multi-scale noise are equivalent to the DDPM loss, up to the weights $\lambda_t$ (pp. 876–877).
- In continuous time, DDPM is a variance-preserving SDE and SGM a variance-exploding SDE. Each has a reverse-time SDE and a deterministic probability-flow ODE with the same marginals (pp. 877–880).
- Speed-ups: DDIM, GAN/EBM decoders, progressive distillation, latent-space diffusion (pp. 882–885).
- Conditioning uses conditional training, classifier guidance, or classifier-free guidance. A larger guidance weight usually gives better samples but less diversity (p. 886).
- For discrete data, Markov transition matrices replace Gaussian noise. Special cases recover the BERT objective and the any-order autoregressive cross-entropy loss. Generative masked language models correspond to discrete diffusion, and MaskGIT uses a similar parallel masked-decoding procedure (pp. 887–891).

## L3 — Walkthrough

### 25.1 Introduction (p. 867)
Converting structured data to noise is easy. Converting noise to data is hard. A forwards (diffusion) process maps $x_0$ to $x_T$ through $T$ stochastic encoder steps $q(x_t|x_{t-1})$. After enough steps $x_T\sim\mathcal N(0,I)$ (or another reference distribution). A learned reverse process $p_\theta(x_{t-1}|x_t)$ undoes this. Diffusion models are related to VAEs, flows and EBMs (p. 867).

### 25.2 DDPMs (pp. 867–874)
A DDPM resembles a hierarchical VAE, but all latents $x_t$ have the dimension of $x_0$. Unlike a flow, the layers are stochastic and need not be invertible. The encoder is a simple linear Gaussian model that is not learned in the basic DDPM (extensions such as §25.2.4 learn its noise level), and the decoder is shared across time steps. This gives a simple objective without risk of posterior collapse (pp. 867–868).

**25.2.1 Encoder.** For $\beta_t\in(0,1)$ from a noise schedule:
$$q(x_t|x_{t-1})=\mathcal N\big(x_t\mid\sqrt{1-\beta_t}\,x_{t-1},\beta_t I\big)\tag{25.1}$$
$$q(x_{1:T}|x_0)=\prod_{t=1}^T q(x_t|x_{t-1})\tag{25.2}$$
Because the chain is linear Gaussian, marginals are closed-form (p. 869). With $\alpha_t\triangleq1-\beta_t$ and $\bar\alpha_t=\prod_{s=1}^t\alpha_s$:
$$q(x_t|x_0)=\mathcal N\big(x_t\mid\sqrt{\bar\alpha_t}\,x_0,(1-\bar\alpha_t)I\big)\tag{25.3}$$
$$\alpha_t\triangleq1-\beta_t,\quad\bar\alpha_t=\prod_{s=1}^t\alpha_s\tag{25.4}$$
The schedule is chosen so that $\bar\alpha_T\approx0$, hence $q(x_T|x_0)\approx\mathcal N(0,I)$. $q(x_t|x_0)$ is the *diffusion kernel*. The marginal $q(x_t)=\int q_0(x_0)q(x_t|x_0)dx_0$ (25.5) is a Gaussian convolution of the data distribution. For images, high-frequency content (texture) is removed first and low-frequency "semantic" content (shape) later (p. 869).

**25.2.2 Decoder.** If $x_0$ is known, one reverse step follows from Bayes' rule for Gaussians (p. 869):
$$q(x_{t-1}|x_t,x_0)=\mathcal N\big(x_{t-1}\mid\tilde\mu_t(x_t,x_0),\tilde\beta_tI\big)\tag{25.6}$$
$$\tilde\mu_t(x_t,x_0)=\frac{\sqrt{\bar\alpha_{t-1}}\beta_t}{1-\bar\alpha_t}x_0+\frac{\sqrt{\alpha_t}(1-\bar\alpha_{t-1})}{1-\bar\alpha_t}x_t\tag{25.7}$$
$$\tilde\beta_t=\frac{1-\bar\alpha_{t-1}}{1-\bar\alpha_t}\beta_t\tag{25.8}$$
At generation time $x_0$ is unknown. The generator is trained to approximate this distribution averaged over $x_0$:
$$p_\theta(x_{t-1}|x_t)=\mathcal N\big(x_{t-1}\mid\mu_\theta(x_t,t),\Sigma_\theta(x_t,t)\big)\tag{25.9}$$
Often $\Sigma_\theta=\sigma_t^2I$. Two natural choices are $\sigma_t^2=\beta_t$ and $\sigma_t^2=\tilde\beta_t$. They correspond to upper and lower bounds on the reverse-process entropy [HJA20] (p. 869). The generative joint is $p_\theta(x_{0:T})=p(x_T)\prod_{t=1}^Tp_\theta(x_{t-1}|x_t)$ with $p(x_T)=\mathcal N(0,I)$.

**25.2.3 Model fitting (ELBO).** For each $x_0$ (p. 870):
$$\log p_\theta(x_0)=\log\!\Big[\int dx_{1:T}\,q(x_{1:T}|x_0)\frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\Big]\tag{25.10}$$
$$\ge\int dx_{1:T}\,q(x_{1:T}|x_0)\log\!\Big(p(x_T)\prod_{t=1}^T\frac{p_\theta(x_{t-1}|x_t)}{q(x_t|x_{t-1})}\Big)\tag{25.11}$$
$$=\mathbb E_q\Big[\log p(x_T)+\sum_{t=1}^T\log\frac{p_\theta(x_{t-1}|x_t)}{q(x_t|x_{t-1})}\Big]\triangleq \mathrm{ELBO}(x_0)\tag{25.12}$$
The Markov property gives $q(x_t|x_{t-1})=q(x_t|x_{t-1},x_0)$, and Bayes' rule gives
$$q(x_t|x_{t-1},x_0)=\frac{q(x_{t-1}|x_t,x_0)q(x_t|x_0)}{q(x_{t-1}|x_0)}\tag{25.13}$$
Plugging in (the $t=1$ term is kept separate):
$$\mathrm{ELBO}(x_0)=\mathbb E_{q(x_{1:T}|x_0)}\Big[\log p(x_T)+\sum_{t=2}^T\log\frac{p_\theta(x_{t-1}|x_t)}{q(x_{t-1}|x_t,x_0)}+\underbrace{\sum_{t=2}^T\log\frac{q(x_{t-1}|x_0)}{q(x_t|x_0)}}_{*}+\log\frac{p_\theta(x_0|x_1)}{q(x_1|x_0)}\Big]\tag{25.14}$$
The starred term telescopes:
$$*=\log q(x_{T-1}|x_0)+\dots+\log q(x_1|x_0)-\log q(x_T|x_0)-\log q(x_{T-1}|x_0)-\dots-\log q(x_2|x_0)\tag{25.15–25.16}$$
$$=-\log q(x_T|x_0)+\log q(x_1|x_0)\tag{25.17}$$
(Added step: the $\log q(x_1|x_0)$ cancels the denominator of the last term in (25.14).) So the negative ELBO is
$$\mathcal L(x_0)=-\mathbb E_{q(x_{1:T}|x_0)}\Big[\log\frac{p(x_T)}{q(x_T|x_0)}+\sum_{t=2}^T\log\frac{p_\theta(x_{t-1}|x_t)}{q(x_{t-1}|x_t,x_0)}+\log p_\theta(x_0|x_1)\Big]\tag{25.18}$$
$$=\underbrace{D_{\mathbb{KL}}(q(x_T|x_0)\|p(x_T))}_{L_T(x_0)}\tag{25.19}$$
$$+\sum_{t=2}^T\mathbb E_{q(x_t|x_0)}\underbrace{D_{\mathbb{KL}}(q(x_{t-1}|x_t,x_0)\|p_\theta(x_{t-1}|x_t))}_{L_{t-1}(x_0)}-\underbrace{\mathbb E_{q(x_1|x_0)}\log p_\theta(x_0|x_1)}_{L_0(x_0)}\tag{25.20}$$
So (25.20) is a prior KL $L_T$, plus one Gaussian KL $L_{t-1}$ per step, plus a reconstruction term $L_0$.

*Intuition note.* Each reverse step is trained to match the "ideal" step that would be possible if $x_0$ were known. The telescoping sum removes all the intermediate terms that do not involve $p_\theta$.

All KL terms are analytic because every distribution is Gaussian (p. 871). Focus on $L_{t-1}$. Since $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon_t$:
$$\tilde\mu_t(x_t,x_0)=\frac1{\sqrt{\alpha_t}}\Big(x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\epsilon\Big)\tag{25.21}$$
So we train the model to predict the noise, and compute the mean from it:
$$\mu_\theta(x_t,t)=\frac1{\sqrt{\alpha_t}}\Big(x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\epsilon_\theta(x_t,t)\Big)\tag{25.22}$$
$$L_{t-1}=\mathbb E_{x_0\sim q_0,\epsilon\sim\mathcal N(0,I)}\Big[\underbrace{\frac{\beta_t^2}{2\sigma_t^2\alpha_t(1-\bar\alpha_t)}}_{\lambda_t}\big\|\epsilon-\epsilon_\theta(\underbrace{\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon}_{x_t},t)\big\|^2\Big]\tag{25.23}$$
The weight $\lambda_t$ corresponds to maximum-likelihood training (assuming the bound is tight). Empirically, setting $\lambda_t=1$ gives better-looking samples. With $t$ also averaged:
$$L_{\text{simple}}=\mathbb E_{x_0,\epsilon,t\sim\text{Unif}(1,T)}\big\|\epsilon-\epsilon_\theta(\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,t)\big\|^2\tag{25.24}$$
Algorithm 25.1 (training, p. 871): repeat until converged: draw $x_0\sim q_0$, $t\sim\text{Unif}\{1..T\}$, $\epsilon\sim\mathcal N(0,I)$. Take a gradient step on $\|\epsilon-\epsilon_\theta(\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,t)\|^2$. Other weightings can improve perceptual quality [Cho+22]. Optimizing the noise schedule can improve likelihood (p. 871).

Algorithm 25.2 (ancestral sampling, p. 872): $x_T\sim\mathcal N(0,I)$. For $t=T,\dots,1$: draw $\epsilon_t\sim\mathcal N(0,I)$ and set
$$x_{t-1}=\tfrac1{\sqrt{\alpha_t}}\big(x_t-\tfrac{1-\alpha_t}{\sqrt{1-\bar\alpha_t}}\epsilon_\theta(x_t,t)\big)+\sigma_t\epsilon_t.$$
Return $x_0$.

*Intuition note.* The network is a noise detector. Given a noisy image and the time, it guesses which noise was added. Subtracting that guess, plus a little fresh noise, moves one step toward the data.

**25.2.4 Learning the noise schedule (VDM, [Kin+21]).** Parameterize the encoder as
$$q(x_t|x_0)=\mathcal N(x_t\mid\alpha_tx_0,\sigma_t^2I)\tag{25.25}$$
(this $\alpha_t$ differs from (25.4)). Learn the signal-to-noise ratio
$$R(t)=\alpha_t^2/\sigma_t^2\tag{25.26}$$
It should decrease monotonically in $t$. This is ensured by $R(t)=\exp(-\gamma_\phi(t))$ with $\gamma_\phi$ a monotonic neural network. One usually sets $\alpha_t=\sqrt{1-\sigma_t^2}$, matching the variance-preserving SDE of §25.4 (p. 872). The negative ELBO is
$$\mathcal L(x_0)=\underbrace{D_{\mathbb{KL}}(q(x_T|x_0)\|p(x_T))}_{\text{prior loss}}+\underbrace{\mathbb E_{q(x_1|x_0)}[-\log p_\theta(x_0|x_1)]}_{\text{reconstruction loss}}+\underbrace{\mathcal L_D(x_0)}_{\text{diffusion loss}}\tag{25.27}$$
$$\mathcal L_D(x_0)=\tfrac12\mathbb E_{\epsilon\sim\mathcal N(0,I)}\int_0^1R'(t)\,\|x_0-\hat x_\theta(z_t,t)\|_2^2\,dt\tag{25.28}$$
Here $z_t=\alpha_tx_0+\sigma_t\epsilon_t$. This is a simplified continuous-time form; the derivation is in [Kin+21] (p. 872). Since $R$ is invertible, change variables to $v=R(t)$, with $z_v=\alpha_vx_0+\sigma_v\epsilon$ and $\tilde x_\theta(z,v)=\hat x_\theta(z,R^{-1}(v))$:
$$\mathcal L_D(x_0)=\tfrac12\mathbb E_{\epsilon}\int_{R_{\min}}^{R_{\max}}\|x_0-\tilde x_\theta(z_v,v)\|_2^2\,dv\tag{25.29}$$
with $R_{\min}=R(1)$, $R_{\max}=R(0)$. So the shape of the SNR schedule does not matter, except at its two endpoints (p. 873). The integral can be estimated with a uniformly sampled timestep. For a minibatch of $k$ examples, a low-discrepancy sampler gives lower variance: draw one $u_0\sim\text{Unif}(0,1)$ and set $t^i=\bmod(u_0+i/k,1)$. The schedule can also be optimized with respect to the variance of the diffusion loss (p. 873).

**25.2.5 Image generation (pp. 873–874).** The common architecture is a U-net. The time step is encoded by sinusoidal positional encoding or random Fourier features. It is fed into residual blocks by spatial addition or by conditioning the group-norm layers. Transformers have been proposed as replacements for the convolutional layers. A small U-net VDM on EMNIST gives the samples in Fig. 25.4. Training big models (billions of parameters) for days on millions of images can give very high quality images (p. 874).

### 25.3 Score-based generative models (pp. 874–877)
An SGM learns the score $s_\theta(x)\approx\nabla_x\log p_{\mathcal D}(x)$ directly, rather than via a scalar energy as in an EBM. It can be fit by basic, sliced or denoising score matching (p. 874).

**25.3.1 Example.** Swiss roll data, with an MLP (2 hidden layers of 128 units), basic score matching and 10,000 SGD steps. The learned vector field points toward high-density regions and away from an unstable empty region. Langevin sampling gives samples (HMC could give more plausible ones) (p. 874).

**25.3.2 Noise at multiple scales.** Let $p_{\mathcal D}=\pi p_0+(1-\pi)p_1$ with disjoint supports $S_0,S_1$:
$$\nabla_x\log p_{\mathcal D}(x)=\begin{cases}\nabla_x\log p_0(x),&x\in S_0\\\nabla_x\log p_1(x),&x\in S_1\end{cases}\tag{25.30}$$
This does not depend on $\pi$. Score matching therefore cannot recover the mixture weights, and Langevin sampling struggles to move between modes. The same happens in practice for approximately disjoint supports (p. 874). The remedy [SE19; SE20b; Son+21b] is to perturb the data:
$$q_\sigma(\tilde x|x)=\mathcal N(\tilde x|x,\sigma^2I),\qquad q_\sigma(\tilde x)=\int p_{\mathcal D}(x)q_\sigma(\tilde x|x)dx\tag{25.31–25.32}$$
Large noise connects the modes, so their weights are estimated accurately. Small noise stays closer to the data. Sampling starts at the largest noise and reduces it step by step (annealed Langevin dynamics or diffusion sampling). This keeps the weights learned at high noise (p. 876). A single *noise conditional score network* $s_\theta(x,\sigma)$ shares weights across scales. With denoising score matching:
$$\mathcal L(\theta;\sigma)=\mathbb E_{q(x,\tilde x)}\Big[\tfrac12\|\nabla_x\log p_\theta(\tilde x,\sigma)-\nabla_x\log q_\sigma(\tilde x|x)\|_2^2\Big]\tag{25.33}$$
$$=\tfrac12\mathbb E_{p_{\mathcal D}(x)}\mathbb E_{\tilde x\sim\mathcal N(x,\sigma^2I)}\Big\{\Big\|s_\theta(\tilde x,\sigma)+\frac{\tilde x-x}{\sigma^2}\Big\|_2^2\Big\}\tag{25.34}$$
using the Gaussian score
$$\nabla\log\mathcal N(\tilde x|x,\sigma^2I)=-\nabla\tfrac1{2\sigma^2}(x-\tilde x)^\top(x-\tilde x)=\frac{x-\tilde x}{\sigma^2}\tag{25.35}$$
(the gradient is with respect to $\tilde x$; see Reading notes). Over $T$ scales $\sigma_1>\dots>\sigma_T$ with $\lambda_t>0$:
$$\mathcal L(\theta;\sigma_{1:T})=\sum_{t=1}^T\lambda_t\mathcal L(\theta;\sigma_t)\tag{25.36}$$

**25.3.3 Equivalence to DDPM (pp. 876–877).** Replace $p_{\mathcal D}\to q_0(x_0)$, $\tilde x\to x_t$, $s_\theta(\tilde x,\sigma)\to s_\theta(x_t,t)$, and sample $t$ uniformly:
$$\mathcal L=\mathbb E\Big[\lambda_t\Big\|s_\theta(x_t,t)+\frac{x_t-x_0}{\sigma_t^2}\Big\|_2^2\Big]\tag{25.37}$$
Use $x_t=x_0+\sigma_t\epsilon$ and define $s_\theta(x_t,t)=-\epsilon_\theta(x_t,t)/\sigma_t$. (Added step: then $s_\theta+(x_t-x_0)/\sigma_t^2=(\epsilon-\epsilon_\theta)/\sigma_t$.) This gives
$$\mathcal L=\mathbb E\Big[\frac{\lambda_t}{\sigma_t^2}\|\epsilon-\epsilon_\theta(x_t,t)\|_2^2\Big]\tag{25.38}$$
Setting $\lambda_t=\sigma_t^2$ recovers $L_{\text{simple}}$ (25.24) (p. 877).

*Intuition note.* Predicting the noise and predicting the score are the same task up to a scale factor $-1/\sigma_t$. So DDPM training and multi-scale score matching are one loss with different weights.

### 25.4 Continuous-time models (pp. 877–882)
This section takes DDPM to infinitely many layers (SGM: infinitely many noise levels). The advantage is access to the large literature on ODE/SDE solvers for faster generation (p. 877).

**25.4.1 Forwards SDE.** Write $\beta_t=\beta(t)\Delta t$:
$$x_t=\sqrt{1-\beta_t}x_{t-1}+\sqrt{\beta_t}\mathcal N(0,I)=\sqrt{1-\beta(t)\Delta t}\,x_{t-1}+\sqrt{\beta(t)\Delta t}\,\mathcal N(0,I)\tag{25.39}$$
A first-order Taylor expansion for small $\Delta t$ gives
$$x_t\approx x_{t-1}-\tfrac{\beta(t)\Delta t}2x_{t-1}+\sqrt{\beta(t)\Delta t}\,\mathcal N(0,I)\tag{25.40}$$
$$\frac{x_t-x_{t-1}}{\Delta t}\approx-\frac{\beta(t)}2x_{t-1}+\frac{\sqrt{\beta(t)}}{\sqrt{\Delta t}}\mathcal N(0,I)\tag{25.41}$$
In the continuous-time limit this is the SDE
$$\frac{dx(t)}{dt}=-\tfrac12\beta(t)x(t)+\sqrt{\beta(t)}\frac{dw(t)}{dt}\tag{25.42}$$
where $w(t)$ is a Wiener process (Brownian noise). In general Itô notation:
$$dx=\underbrace{f(x,t)}_{\text{drift}}dt+\underbrace{g(t)}_{\text{diffusion}}dw\tag{25.43}$$
Sample paths come from Euler–Maruyama integration (Fig. 25.6):
$$x(t+\Delta t)=x(t)+f(x(t),t)\Delta t+g(t)\sqrt{\Delta t}\,\mathcal N(0,I)\tag{25.44}$$
[Son+21b] show that as $T\to\infty$ DDPM corresponds to
$$dx=-\tfrac12\beta(t)x\,dt+\sqrt{\beta(t)}\,dw,\qquad\beta(t/T)=T\beta_t\tag{25.45}$$
The drift is proportional to $-x$, which pulls toward 0. This is a *variance preserving* process. The SDE for SGMs,
$$dx=\sqrt{\frac{d[\sigma(t)^2]}{dt}}\,dw,\qquad\sigma(t/T)=\sigma_t\tag{25.46}$$
has zero drift and is a *variance exploding* process (p. 878).

**25.4.2 Forwards ODE.** Instead of adding noise at every step, sample the initial state and evolve it deterministically:
$$dx=\Big[f(x,t)-\tfrac12g(t)^2\nabla_x\log p_t(x)\Big]dt,\quad h(x,t)\text{ = the bracket}\tag{25.47}$$
This is the *probability flow ODE* [Son+21b]. It is solved by $x(t)=x(0)+\int_0^th(x,\tau)d\tau$ (25.48). Starting from random $x(0)$, the induced marginals are the same as for the SDE model (p. 879).

**25.4.3 Reverse SDE (pp. 879–880).** [And82] showed that any forwards SDE (25.43) can be reversed in time:
$$dx=\big[f(x_t,t)-g(t)^2\nabla_x\log q_t(x)\big]dt+g(t)d\bar w\tag{25.49}$$
where $\bar w$ is a Wiener process with time flowing backwards and $dt$ is a negative time step. For DDPM:
$$dx_t=\big[-\tfrac12\beta(t)x_t-\beta(t)\nabla_{x_t}\log q_t(x_t)\big]dt+\sqrt{\beta(t)}d\bar w_t\tag{25.50}$$
Estimate the score by denoising score matching, $\nabla\log q_t(x_t)\approx s_\theta(x_t,t)$ (25.51). Variance reduction such as importance sampling is advisable in practice. Then:
$$dx_t=-\tfrac12\beta(t)[x_t+2s_\theta(x_t,t)]dt+\sqrt{\beta(t)}d\bar w_t\tag{25.52}$$
Sampling uses ancestral sampling or Euler–Maruyama:
$$x_{t-1}=x_t+\tfrac12\beta(t)[x_t+2s_\theta(x_t,t)]\Delta t+\sqrt{\beta(t)\Delta t}\,\mathcal N(0,I)\tag{25.53}$$

**25.4.4 Reverse ODE.** The probability-flow ODE derived from (25.49) is
$$dx_t=\big[f(x_t,t)-\tfrac12g(t)^2s_\theta(x_t,t)\big]dt\tag{25.54}$$
With $f=-\tfrac12\beta(t)x_t$ and $g=\sqrt{\beta(t)}$ (as in DDPM):
$$dx_t=-\tfrac12\beta(t)[x_t+s_\theta(x_t,t)]dt\tag{25.55}$$
Euler's method gives $x_{t-1}=x_t+\tfrac12\beta(t)[x_t+s_\theta(x_t,t)]\Delta t$ (25.56). Higher-order solvers such as Heun's method often work better in practice [Kar+22] (p. 880). This model is a special case of a neural ODE, also called a continuous normalizing flow (§23.2.6). So the exact log marginal likelihood can be derived. Score matching is used instead of maximizing it directly, which is expensive (p. 880).

The deterministic ODE also guarantees identifiability. The ODE is uniquely determined by the score. If the architecture is flexible enough and there is enough data, score matching will recover the true score. A datapoint then maps to a unique latent code, regardless of architecture or initialization (Fig. 25.8). This allows "semantic interpolation" in latent space (pp. 880–881).

**25.4.5 SDE vs ODE (p. 881).** The reverse SDE can be rewritten as
$$dx_t=\underbrace{-\tfrac12\beta(t)[x_t+s_\theta(x_t,t)]dt}_{\text{probability flow ODE}}\underbrace{-\tfrac12\beta(t)s_\theta(x_t,t)dt+\sqrt{\beta(t)}d\bar w_t}_{\text{Langevin diffusion SDE}}\tag{25.57}$$
Continuous noise injection can compensate for numerical errors in the ODE term, so SDE samples often look better. The ODE approach can be faster. [Kar+22] combine them: alternate an ODE-solver step with adding a small amount of noise (Fig. 25.9).

*Intuition note.* The SDE and the ODE are two ways to run the same marginal distributions backwards. The ODE is a smooth, deterministic path; the SDE adds randomness that can correct small solver errors.

**25.4.6 Example.** `diffusion_mnist.ipynb` fits a small model to MNIST with denoising score matching and samples by solving the probability-flow ODE with `diffrax` (p. 881).

**25.4.7 Flow matching (pp. 881–882).** Viewing the ODE as a continuous-time normalizing flow, one can drop Gaussian noise and learn a deterministic map from a source $p_0$ to a target $p_1$. The network approximates the velocity field $v_\theta(x_t,t)\approx\frac d{dt}x_t=\frac d{dt}I_t(x_0,x_1)$, with interpolant $I_t=\alpha_tx_0+\beta_tx_1$ (e.g. $\alpha_t=1-t$, $\beta_t=t$). A sample is $x_1=\int_0^1\frac{dx_t}{dt}dt$ with $x_0\sim p_0$. Advantages: non-Gaussian $p_0$ is allowed, and the exact likelihood is $p_1(x)=p_0(x)\exp\!\big(-\int_0^1\mathrm{div}(v_\theta(x_t,t))dt\big)$ (as printed). The flow can also be optimized to solve an optimal-transport problem, which can speed up sampling.

### 25.5 Speeding up diffusion models (pp. 882–885)
Sampling needs many small steps, and simply taking fewer, larger steps gives much worse results (p. 882).

**25.5.1 DDIM.** Use a non-Markovian forward process that also conditions on $x_0$:
$$q(x_{t-1}|x_t,x_0)=\mathcal N\Big(\sqrt{\bar\alpha_{t-1}}x_0+\sqrt{1-\bar\alpha_{t-1}-\tilde\sigma_t^2}\frac{x_t-\sqrt{\bar\alpha_t}x_0}{\sqrt{1-\bar\alpha_t}},\tilde\sigma_t^2I\Big)\tag{25.58}$$
The reverse process is the same with $x_0$ replaced by the model's prediction $\hat x_0=\hat x_\theta(x_t,t)$ (25.59). Setting $\tilde\sigma_t^2=0$ makes the reverse process fully deterministic given the initial prior sample. The resulting probability-flow ODE gives better results with few steps than §25.4.4. The weighted negative VLB equals $L_{\text{simple}}$, so DDIM can be applied to a trained DDPM (p. 883).

**25.5.2 Non-Gaussian decoders.** Larger reverse steps make $p(x_{t-1}|x_t)$ multimodal (Fig. 25.11). [Gao+21] fit it with an EBM, which still needs MCMC. [XKV22] fit it with a GAN, which allows easy sampling. Compared with a single-stage GAN this gives better mode coverage and training stability. Compared with a standard diffusion model it needs far fewer steps (p. 883).

**25.5.3 Progressive distillation [SH22].** Train a DDPM and sample it with DDIM as the "teacher". Train a "student" to predict the teacher's output over two teacher steps at once (Fig. 25.12). The student then generates samples as good as the teacher's in half the steps, and becomes the next teacher. Algorithm 25.4 repeats this, halving $N$ each round. Teachers get faster each round, so total distillation time is relatively small. High-quality samples are possible in as few as 4 steps (p. 884).

**25.5.4 Latent-space diffusion.** Embed the images in a lower-dimensional space and diffuse there. The LDM [Rom+22] first fits a VAE (with a perceptual loss), then fits the diffusion model to the embeddings (Fig. 25.13). It underlies stable diffusion. The LSGM [VKK21] trains a hierarchical VAE and then trains the VAE and diffusion model jointly. Autoencoders also let diffusion apply to text or graphs, given an embedding into a continuous space. One can also fit a VAE on top of a DDPM [Pan+22] (p. 885).

### 25.6 Conditional generation (pp. 885–887)
**25.6.1 Conditional model.** Train on $(c,x)$ pairs to maximize $p(x|c)$. A scalar $c$ is embedded and added spatially or used to modulate group norm. An image $c$ is concatenated with $x_t$ as extra channels. A text $c$ is embedded and used by spatial addition or cross-attention (p. 885).

**25.6.2 Classifier guidance [DN21b].** This uses a pre-trained classifier $p_\phi(c|x)$, so no retraining is needed:
$$\log p(x|c)=\log p(c|x)+\log p(x)-\log p(c)\tag{25.60}$$
$$\nabla_x\log p(x|c)=\nabla_x\log p(x)+\nabla_x\log p(c|x)\tag{25.61}$$
The conditioning can be amplified by a factor $w>1$:
$$\nabla_x\log p_w(x|c)=\nabla_x\log p(x)+w\nabla_x\log p(c|x)\tag{25.62}$$
In practice, sample
$$x_{t-1}\sim\mathcal N(\mu+w\Sigma g,\Sigma),\ \mu=\mu_\theta(x_t,t),\ \Sigma=\Sigma_\theta(x_t,t),\ g=\nabla_{x_t}\log p_\phi(c|x_t)\tag{25.63}$$

**25.6.3 Classifier-free guidance [HS21].** A discriminative $p(c|x_t)$ may ignore many details of $x_t$. Following its gradient can then give poor results, like adversarial images. It also needs a classifier per time step, since $x_t$ varies in blurriness. Instead, derive the classifier from the generative model:
$$\log p(c|x)=\log p(x|c)+\log p(c)-\log p(x)\tag{25.64}$$
Use one network, with $c=\emptyset$ for the unconditional case. The modified score is
$$\nabla_x[\log p(x|c)+w\log p(c|x)]=\nabla_x[\log p(x|c)+w(\log p(x|c)-\log p(x))]\tag{25.65}$$
$$=\nabla_x[(1+w)\log p(x|c)-w\log p(x)]\tag{25.66}$$
(the constant $\log p(c)$ has zero gradient; added step). Larger guidance weight usually gives better individual sample quality but lower diversity (p. 886).

**25.6.4 High resolution.** Cascaded generation [Ho+21] trains a 64×64 generator and then super-resolution models to 256×256 or 1024×1024. Google's Imagen [Sah+22b] uses this with a large pre-trained T5-XXL text encoder and a U-net VDM (Fig. 25.14). Image-conditioned models (grey-scale to colour, or corrupted to clean) can be trained as a multi-task conditional diffusion model [Sah+22a] (pp. 886–887).

### 25.7 Diffusion for discrete state spaces (pp. 887–891)
Discrete data can be handled through a continuous embedding (§25.5.4) or by defining diffusion directly on the discrete space (p. 887).

**25.7.1 D3PM [Aus+21].** Requirements: sampling $q(x_t|x_0)$ for any $t$; a tractable $q(x_{t-1}|x_t,x_0)$ so the KL terms (25.67) are computable; and ideally a known stationary distribution $\pi(x_T)$ used as prior, making $D_{\mathbb{KL}}(q(x_T|x_0)\|p(x_T))=0$ (p. 888). The state is $D$ independent categorical blocks $x_t\in\{1..K\}$, with $x$ a one-hot row vector (shape $1\times K$). Transition matrix $Q_t$ is $K\times K$ and row stochastic, $[Q_t]_{ij}=q(x_t=j|x_{t-1}=i)$:
$$q(x_t|x_{t-1})=\text{Cat}(x_t|x_{t-1}Q_t)\tag{25.68}$$
$$q(x_t|x_0)=\text{Cat}(x_t|x_0\bar Q_t),\quad\bar Q_t=Q_1Q_2\cdots Q_t\tag{25.69}$$
$$q(x_{t-1}|x_t,x_0)=\frac{q(x_t|x_{t-1},x_0)q(x_{t-1}|x_0)}{q(x_t|x_0)}=\text{Cat}\Big(x_{t-1}\Big|\frac{x_tQ_t^\top\odot x_0\bar Q_{t-1}}{x_0\bar Q_tx_t^\top}\Big)\tag{25.70}$$
Both distributions factorize, so the KL is a sum over dimensions (p. 888).

**25.7.2 Choice of $Q_t$ (pp. 889–890).**
- *Uniform kernel:* $[Q_t]_{ij}=1-\frac{K-1}K\beta_t$ if $i=j$, and $\frac1K\beta_t$ if $i\ne j$ (25.71). It adds a little uniform noise. It is doubly stochastic with positive entries, so the stationary distribution is uniform. The marginal is $q(x_t|x_0)=\text{Cat}(x_t|\bar\alpha_tx_0+(1-\bar\alpha_t)/K)$ (25.72), with $\alpha_t=1-\beta_t$ and $\bar\alpha_t=\prod_{\tau\le t}\alpha_\tau$ [Hoo+21]. The posterior is $\text{Cat}(x_{t-1}|\theta_{\text{post}})$ with $\theta_{\text{post}}=\tilde\theta/\sum_k\tilde\theta_k$ and $\tilde\theta=[\alpha_tx_t+(1-\alpha_t)/K]\odot[\bar\alpha_{t-1}x_0+(1-\bar\alpha_{t-1})/K]$ (25.73–25.74).
- *Absorbing state $m$ (MASK):* $Q_t=(1-\beta_t)I+\beta_t\mathbf 1e_m^\top$. Entries: 1 if $i=j=m$; $1-\beta_t$ if $i=j\neq m$; $\beta_t$ if $j=m,i\ne m$ (25.75). It converges to a point mass on $m$.
- *Discretized Gaussian* for ordinal values: transitions to nearby states. If doubly stochastic, the stationary distribution is uniform.

**25.7.3 Reverse process.** Instead of predicting $p_\theta(x_{t-1}|x_t)$ directly, predict logits of the clean output $\tilde p_\theta(\tilde x_0|x_t)$ and combine:
$$p_\theta(x_{t-1}|x_t)\propto\sum_{\tilde x_0}q(x_{t-1}|x_t,\tilde x_0)\tilde p_\theta(\tilde x_0|x_t)\tag{25.76}$$
The sum costs $O(DK)$. The model then automatically satisfies sparsity constraints in $Q_t$. Multi-step inference is also possible:
$$p_\theta(x_{t-k}|x_t)\propto\sum_{\tilde x_0}q(x_{t-k}|x_t,\tilde x_0)\tilde p_\theta(\tilde x_0|x_t)\tag{25.77}$$
Discrete distributions already have the multimodal flexibility that multi-step Gaussian decoders lack (p. 890).

**25.7.4 Noise schedules (p. 890).** Discretized Gaussian: linearly increase the Gaussian variance before discretizing. Uniform: cosine schedule $\alpha_t=\cos\big(\frac{t/T+s}{1+s}\frac\pi2\big)$, $s=0.008$ [ND21]. Masked: $\beta_t=1/(T-t+1)$ [SD+15].

**25.7.5 Connections (pp. 890–891).** Take $Q=\alpha\mathbf 1e_m^\top+\beta\mathbf 1\mathbf 1^\top/K+(1-\alpha-\beta)I$. Let a one-step process replace $\alpha=10\%$ of tokens with MASK and $\beta=5\%$ uniformly at random. Then the objective is the BERT objective $L_0(x_0)=-\mathbb E_{q(x_1|x_0)}\log p_\theta(x_0|x_1)$ (25.78). This holds since $L_T=0$ and no other time steps are used.
*Masking diffusion* masks tokens deterministically one by one. For length $N=T$, $q([x_t]_i|x_0)=[x_0]_i$ if $i<N-t$, else MASK. The posterior is a delta function on $x_t$ with one fewer mask. The KL term becomes $-\log p_\theta([x_0]_i|x_t)$, the standard cross-entropy of an any-order autoregressive model [Ou+24]. Generative masked language models also correspond to discrete diffusion. MaskGIT [Cha+22] does this for images after vector quantization. It takes 8 parallel steps versus 256 sequential steps for a transformer (Fig. 25.17).

## Toy example (ours, not from the text)
One scalar data point $x_0=2$, $T=2$, with $\beta_1=0.19$, $\beta_2=0.36$.

- $\alpha_1=0.81$, $\alpha_2=0.64$. $\bar\alpha_1=0.81$, $\bar\alpha_2=0.81\times0.64=0.5184$.
- By (25.3): $q(x_1|x_0)=\mathcal N(\sqrt{0.81}\cdot2,\,0.19)=\mathcal N(1.8,0.19)$. $q(x_2|x_0)=\mathcal N(\sqrt{0.5184}\cdot2,\,1-0.5184)=\mathcal N(1.44,0.4816)$, since $\sqrt{0.5184}=0.72$.
- Check by chaining two steps: mean $0.8\times1.8=1.44$; variance $0.64\times0.19+0.36=0.1216+0.36=0.4816$. This agrees.
- Posterior (25.7), (25.8): $\tilde\mu_2=\frac{0.9\times0.36}{0.4816}x_0+\frac{0.8\times0.19}{0.4816}x_2=0.6728\,x_0+0.3156\,x_2$, and $\tilde\beta_2=\frac{0.19}{0.4816}\times0.36=0.142$.
- Take noise $\epsilon=1$: $x_2=1.44+\sqrt{0.4816}=1.44+0.694=2.134$. Then $\tilde\mu_2=0.6728\cdot2+0.3156\cdot2.134=1.3455+0.6735=2.019$.
- Via the noise form (25.21): $\frac1{0.8}\big(2.134-\frac{0.36}{0.694}\cdot1\big)=1.25\,(2.134-0.5187)=2.019$. This agrees with (25.7).
- So a network that outputs $\epsilon_\theta=1$ at $(x_2=2.134,t=2)$ gives the exact reverse mean. If it output $0.8$, the loss term is $\|1-0.8\|^2=0.04$.

## Concepts
- [[diffusion-model]] (new) — generative model: fixed noising chain plus learned denoising chain (p. 867)
- [[forward-diffusion-process]] (new) — linear-Gaussian Markov chain turning data into noise; marginal in closed form (p. 868)
- [[diffusion-kernel]] (new) — $q(x_t|x_0)=\mathcal N(\sqrt{\bar\alpha_t}x_0,(1-\bar\alpha_t)I)$ (p. 869)
- [[noise-schedule]] (new) — choice of $\beta_t$ (or the SNR $R(t)$); in VDM it is learned (pp. 868, 872)
- [[variational-inference-elbo]] — here the ELBO splits into $L_T$, $L_{t-1}$, $L_0$ (p. 870)
- [[kl-divergence]] — each $L_{t-1}$ is a KL between Gaussians, analytic (p. 870)
- [[noise-prediction-loss]] (new) — weighted least squares on $\epsilon$; $\lambda_t=1$ gives $L_{\text{simple}}$ (p. 871)
- [[score-based-generative-model]] (new) — directly learn $\nabla_x\log p(x)$ at several noise scales (p. 874)
- [[stochastic-differential-equation-view]] (new) — continuous-time limit; drift plus diffusion; reverse-time SDE (pp. 877, 879)
- [[probability-flow-ode]] (new) — deterministic ODE with the same marginals as the SDE (p. 878)
- [[classifier-free-guidance]] (new) — mix conditional and unconditional scores with weight $w$ (p. 886)
- [[markov-chain-monte-carlo]] — Langevin sampling is mentioned as a score-based sampler (p. 874)
- [[discrete-diffusion-d3pm]] (new) — diffusion with row-stochastic matrices $Q_t$ on categorical states (p. 888)

## Canonical instances
- [[swiss-roll-score-matching]] — score learned on 2d Swiss roll; Langevin samples (p. 874)
- [[mixture-disjoint-support-failure]] — score ignores mixture weight $\pi$ (p. 874)
- [[stable-diffusion-ldm]] — VAE plus latent diffusion (p. 885)
- [[imagen-cascade]] — text-to-image with 64→256→1024 super-resolution (p. 886)
- [[bert-as-d3pm]] — BERT objective from one-step masking/uniform noise (p. 891)
- [[maskgit]] — parallel masked decoding, 8 vs 256 steps (p. 891)

## Bridges (candidates)
- [same-math] DDPM ELBO (§25.2.3) ↔ Bayesian: ELBO and KL from variational inference with a fixed (non-learned) variational posterior $q(x_{1:T}|x_0)$.
- [same-math] Gaussian posterior $q(x_{t-1}|x_t,x_0)$ (25.6) ↔ Bayesian: conjugate Gaussian update (prior from the chain, likelihood from the step).
- [structural-analogy] Noise-scale annealing in SGMs ↔ Bayesian: tempering/annealed sampling in MCMC; both move from a smoothed distribution to the target.
- [structural-analogy] Classifier guidance (25.61) ↔ Bayesian: posterior score = prior score + likelihood score, with $w$ as a likelihood power.
- [same-math] Probability-flow ODE with exact likelihood ↔ normalizing flows: neural ODE / continuous normalizing flow.
- [structural-analogy] Hierarchical VAE with fixed encoder ↔ hierarchical model: layers of latents, but a non-learned top-down pass.

## Questions this raises
- If $\lambda_t=1$ gives better samples but is not the maximum-likelihood weighting, what is lost in the likelihood, and how does the learned schedule of §25.2.4 recover it?
- Under what conditions does the claim "score matching recovers the true score" hold, and how does approximation error affect the identifiability argument?
- Why does the noise term in (25.57) help correct ODE-solver errors, and how many steps are needed before it stops helping?
- How do the discrete noise schedules and kernels choose between uniform, absorbing and Gaussian corruption for a given data type?

## Reading notes
- Printed page = pdf page − 34 (pdf 901 → p. 867). The last supplied page (pdf 926, printed 892) is blank; content ends on p. 891.
- Running footer: "Probabilistic Machine Learning: Advanced Topics". Online version. December 10, 2025.
- Text layer problems: in the sentence after (25.26) the text layer loses a square root. The image shows $\alpha_t=\sqrt{1-\sigma_t^2}$ (p. 872). Many equations were checked against the images.
- Possible misprint (our observation): (25.28) integrates $R'(t)$ from $t=0$ to 1. Changing variables gives $\int_{R_{\max}}^{R_{\min}}$, so the limits of (25.29) look reversed relative to (25.28), up to a sign. Copied as printed.
- (25.35): the gradient is written $\nabla_x$, but the printed result $(x-\tilde x)/\sigma^2$ is the gradient with respect to $\tilde x$, which is what (25.34) uses.
- (25.71): printed $Q_t=(1-\beta_t)I+\beta_t/K$. The scalar form implies $\beta_t\mathbf 1\mathbf 1^\top/K$.
- §25.3.3 uses $x_t=x_0+\sigma_t\epsilon$ while (25.24) uses the scaled form. The text says $\lambda_t=\sigma_t^2$ "recovers" $L_{\text{simple}}$; this is stated as printed.
- §25.3 text has a missing parenthesis after "Section 24.3.3" (p. 874). Several figure captions contain typos ("mulit-modal", "Generatng").
- Algorithm 25.4 is summarized only; its lines 8–11 are not reproduced in detail.
