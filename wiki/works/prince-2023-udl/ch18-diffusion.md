---
id: prince-2023-udl/ch18-diffusion
work: prince-2023-udl
unit: "Chapter 18 — Diffusion models"
pages: 349-373
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Diffusion models

## L0 — One line
A diffusion model fixes a process that gradually turns data into white noise, then trains a network to undo it one small step at a time. The ELBO training objective reduces to predicting the added noise by least squares.

## L1 — The gist (≤ 120 words)
How can we build a probabilistic generative model that is easy to train and has no invertibility constraint on its network? The answer: the encoder is fixed and adds Gaussian noise step by step until only noise remains. A decoder is learned that removes noise step by step. Each reverse step is approximately normal when the steps are small, so the evidence lower bound (ELBO, a tractable lower bound on log-likelihood) becomes a simple least-squares loss for predicting the noise. Sampling starts from pure noise and runs the network many times, which is slow. Class or text conditioning, cascades and deterministic samplers give high-quality, faster image generation.

**Prerequisites:** normal distributions and their means and variances; Bayes' rule; Markov chain; the VAE and its ELBO (Jensen's inequality, KL divergence); U-Net as an image-to-image network.

## L2 — Key ideas (5–10 bullets)
- The encoder (forward process) is prespecified and has no parameters. It mixes data with noise, so all learning happens in the decoder (p. 349, p. 358).
- A closed-form "diffusion kernel" $q(\mathbf z_t|\mathbf x)$ lets us sample any noisy level directly, without simulating the intermediate steps. This makes training cheap (p. 353).
- The true reverse distribution $q(\mathbf z_{t-1}|\mathbf z_t)$ is intractable and complex. But $q(\mathbf z_{t-1}|\mathbf z_t,\mathbf x)$ is normal in closed form, and it is the training target (p. 354–356).
- The ELBO becomes a reconstruction term plus KL terms between normals. These reduce to squared differences of means (p. 358–359).
- Reparameterizing the network to predict the noise $\boldsymbol\epsilon$ gives a very simple loss (equation 18.40). Training samples a random $t$ and noise (p. 361–364).
- Sampling is ancestral and serial: $T$ network evaluations, possibly about 1000 for images. This is a major drawback (p. 363–364).
- The same loss is valid for a family of forward processes, including deterministic DDIM. Skipping steps gives good samples with about 50 steps when the forward process is no longer stochastic (p. 364–365).
- Class guidance, classifier-free guidance, cascades and text embeddings give controllable, high-resolution images (p. 365–368).

## L3 — Walkthrough

### 18.1 Overview (p. 349–350)
Diffusion models are probabilistic like normalizing flows, with latents of the same dimension as the data. Like VAEs, they use a lower bound built on an encoder. The encoder is predetermined and the decoder is learned. The author says they are easy to train and can exceed GAN realism (p. 349).

The encoder maps $\mathbf x\to\mathbf z_1\to\dots\to\mathbf z_T$ stochastically. With enough steps, $q(\mathbf z_T|\mathbf x)$ and $q(\mathbf z_T)$ are both standard normal. The decoder is a series of networks, each inverting one encoder step. To generate, draw $\mathbf z_T\sim q(\mathbf z_T)$ and decode (p. 349–350).

### 18.2 Encoder (forward process) (p. 350–355)
The latents have the same size as $\mathbf x$:
$$\mathbf z_1=\sqrt{1-\beta_1}\,\mathbf x+\sqrt{\beta_1}\,\boldsymbol\epsilon_1,\qquad \mathbf z_t=\sqrt{1-\beta_t}\,\mathbf z_{t-1}+\sqrt{\beta_t}\,\boldsymbol\epsilon_t\ \ \forall t\in 2..T \tag{18.1}$$
Here $\boldsymbol\epsilon_t$ is standard normal noise. The first term attenuates the data plus noise so far, and the second adds noise. The $\beta_t\in[0,1]$ form the *noise schedule* (p. 350). In probabilistic form:
$$q(\mathbf z_1|\mathbf x)=\mathrm{Norm}_{\mathbf z_1}\!\big[\sqrt{1-\beta_1}\mathbf x,\beta_1\mathbf I\big],\quad q(\mathbf z_t|\mathbf z_{t-1})=\mathrm{Norm}_{\mathbf z_t}\!\big[\sqrt{1-\beta_t}\mathbf z_{t-1},\beta_t\mathbf I\big]\tag{18.2}$$
This is a Markov chain: $\mathbf z_t$ depends only on $\mathbf z_{t-1}$. The joint is
$$q(\mathbf z_{1\ldots T}|\mathbf x)=q(\mathbf z_1|\mathbf x)\prod_{t=2}^{T}q(\mathbf z_t|\mathbf z_{t-1}).\tag{18.3}$$
In the 1D example ($T=100$, $\beta=0.03$), paths drift toward zero (p. 351). Footnote 1 says "forward" here is the opposite of the normalizing-flow naming (p. 350).

**18.2.1 Diffusion kernel.** Simulating step by step is slow for large $t$. Substitute $\mathbf z_1$ into $\mathbf z_2$ (p. 353):
$$\mathbf z_2=\sqrt{1-\beta_2}\big(\sqrt{1-\beta_1}\mathbf x+\sqrt{\beta_1}\boldsymbol\epsilon_1\big)+\sqrt{\beta_2}\boldsymbol\epsilon_2 \tag{18.5}$$
$$=\sqrt{(1-\beta_2)(1-\beta_1)}\,\mathbf x+\sqrt{1-\beta_2-(1-\beta_2)(1-\beta_1)}\,\boldsymbol\epsilon_1+\sqrt{\beta_2}\boldsymbol\epsilon_2 .$$
The last two terms are independent mean-zero normals with variances $1-\beta_2-(1-\beta_2)(1-\beta_1)$ and $\beta_2$. The variances add (problem 18.2), so
$$\mathbf z_2=\sqrt{(1-\beta_2)(1-\beta_1)}\,\mathbf x+\sqrt{1-(1-\beta_2)(1-\beta_1)}\,\boldsymbol\epsilon .\tag{18.6}$$
Continuing the substitution gives (problem 18.3), with $\alpha_t=\prod_{s=1}^t(1-\beta_s)$:
$$\mathbf z_t=\sqrt{\alpha_t}\,\mathbf x+\sqrt{1-\alpha_t}\,\boldsymbol\epsilon,\qquad q(\mathbf z_t|\mathbf x)=\mathrm{Norm}_{\mathbf z_t}\!\big[\sqrt{\alpha_t}\mathbf x,(1-\alpha_t)\mathbf I\big].\tag{18.7, 18.8}$$
The mean shrinks toward zero and the variance grows with $t$ (figure 18.3, p. 352).

*Intuition note.* Many small noisy steps equal one big noisy step with known mean and variance. So we can jump to any noise level in one draw. Training uses this, so it never simulates the chain.

**18.2.2 Marginal $q(\mathbf z_t)$.** Marginalizing the joint gives
$$q(\mathbf z_t)=\iint q(\mathbf z_{1\ldots t}|\mathbf x)\Pr(\mathbf x)\,d\mathbf z_{1\ldots t-1}d\mathbf x \tag{18.9}$$
$$q(\mathbf z_t)=\int q(\mathbf z_t|\mathbf x)\Pr(\mathbf x)\,d\mathbf x .\tag{18.10}$$
Superimposing the kernel on samples from $\Pr(\mathbf x)$ gives $q(\mathbf z_t)$ (figure 18.4). It has no closed form because $\Pr(\mathbf x)$ is unknown (p. 354).

**18.2.3 Conditional $q(\mathbf z_{t-1}|\mathbf z_t)$.** Bayes' rule gives
$$q(\mathbf z_{t-1}|\mathbf z_t)=\frac{q(\mathbf z_t|\mathbf z_{t-1})q(\mathbf z_{t-1})}{q(\mathbf z_t)}\tag{18.11}$$
This is intractable because $q(\mathbf z_{t-1})$ cannot be computed. In the 1D example it can be evaluated numerically. In general its form is complex, but in many cases a normal is a good approximation, and the decoder will use one (p. 354, figure 18.5).

**18.2.4 Conditional diffusion distribution $q(\mathbf z_{t-1}|\mathbf z_t,\mathbf x)$.** If $\mathbf x$ is known, $q(\mathbf z_{t-1}|\mathbf x)$ is the normal diffusion kernel, so this distribution is closed-form. It is available during training, when $\mathbf x$ is known (p. 354–356):
$$q(\mathbf z_{t-1}|\mathbf z_t,\mathbf x)=\frac{q(\mathbf z_t|\mathbf z_{t-1},\mathbf x)q(\mathbf z_{t-1}|\mathbf x)}{q(\mathbf z_t|\mathbf x)}\propto q(\mathbf z_t|\mathbf z_{t-1})\,q(\mathbf z_{t-1}|\mathbf x)$$
$$=\mathrm{Norm}_{\mathbf z_t}\!\big[\sqrt{1-\beta_t}\mathbf z_{t-1},\beta_t\mathbf I\big]\mathrm{Norm}_{\mathbf z_{t-1}}\!\big[\sqrt{\alpha_{t-1}}\mathbf x,(1-\alpha_{t-1})\mathbf I\big]$$
$$\propto\mathrm{Norm}_{\mathbf z_{t-1}}\!\Big[\tfrac{1}{\sqrt{1-\beta_t}}\mathbf z_t,\tfrac{\beta_t}{1-\beta_t}\mathbf I\Big]\mathrm{Norm}_{\mathbf z_{t-1}}\!\big[\sqrt{\alpha_{t-1}}\mathbf x,(1-\alpha_{t-1})\mathbf I\big]\tag{18.12}$$
- The first step uses $q(\mathbf z_t|\mathbf z_{t-1},\mathbf x)=q(\mathbf z_t|\mathbf z_{t-1})$, because the process is Markov.
- The third line uses the Gaussian change-of-variables identity
$$\mathrm{Norm}_{\mathbf v}[\mathbf A\mathbf w,\mathbf B]\propto\mathrm{Norm}_{\mathbf w}\!\big[(\mathbf A^T\mathbf B^{-1}\mathbf A)^{-1}\mathbf A^T\mathbf B^{-1}\mathbf v,(\mathbf A^T\mathbf B^{-1}\mathbf A)^{-1}\big].\tag{18.13}$$
- The two normals in $\mathbf z_{t-1}$ are combined with
$$\mathrm{Norm}_{\mathbf w}[\mathbf a,\mathbf A]\,\mathrm{Norm}_{\mathbf w}[\mathbf b,\mathbf B]\propto\mathrm{Norm}_{\mathbf w}\!\big[(\mathbf A^{-1}+\mathbf B^{-1})^{-1}(\mathbf A^{-1}\mathbf a+\mathbf B^{-1}\mathbf b),(\mathbf A^{-1}+\mathbf B^{-1})^{-1}\big].\tag{18.14}$$
Result (the proportionality constants must cancel, since the result is already normalized):
$$q(\mathbf z_{t-1}|\mathbf z_t,\mathbf x)=\mathrm{Norm}_{\mathbf z_{t-1}}\!\Big[\tfrac{(1-\alpha_{t-1})}{1-\alpha_t}\sqrt{1-\beta_t}\,\mathbf z_t+\tfrac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf x,\ \tfrac{\beta_t(1-\alpha_{t-1})}{1-\alpha_t}\mathbf I\Big]\tag{18.15}$$

### 18.3 Decoder (reverse process) (p. 356–357)
The true reverse distributions are complex and multimodal and depend on $\Pr(\mathbf x)$. The decoder approximates them by normals:
$$\Pr(\mathbf z_T)=\mathrm{Norm}[\mathbf 0,\mathbf I],\ \ \Pr(\mathbf z_{t-1}|\mathbf z_t,\boldsymbol\phi_t)=\mathrm{Norm}[\mathbf f_t[\mathbf z_t,\boldsymbol\phi_t],\sigma_t^2\mathbf I],\ \ \Pr(\mathbf x|\mathbf z_1,\boldsymbol\phi_1)=\mathrm{Norm}[\mathbf f_1[\mathbf z_1,\boldsymbol\phi_1],\sigma_1^2\mathbf I]\tag{18.16}$$
$\mathbf f_t$ is a neural network giving the mean. The $\sigma_t^2$ are predetermined. The normal approximation is reasonable if the $\beta_t$ are near zero and $T$ is large. New examples come from *ancestral sampling* (draw $\mathbf z_T$, then each $\mathbf z_{t-1}$ from $\mathbf z_t$ in turn, finally $\mathbf x$) (p. 357).

### 18.4 Training (p. 357–361)
The joint is
$$\Pr(\mathbf x,\mathbf z_{1\ldots T}|\boldsymbol\phi)=\Pr(\mathbf x|\mathbf z_1,\boldsymbol\phi_1)\prod_{t=2}^T\Pr(\mathbf z_{t-1}|\mathbf z_t,\boldsymbol\phi_t)\cdot\Pr(\mathbf z_T)\tag{18.17}$$
The likelihood is $\Pr(\mathbf x|\boldsymbol\phi)=\int\Pr(\mathbf x,\mathbf z_{1\ldots T}|\boldsymbol\phi)d\mathbf z_{1\ldots T}$ (18.18). We want $\hat{\boldsymbol\phi}=\arg\max\sum_i\log\Pr(\mathbf x_i|\boldsymbol\phi)$ (18.19). This integral is intractable, so a lower bound is used as in the VAE (p. 357).

**18.4.1 ELBO.** Multiply and divide by $q(\mathbf z_{1\ldots T}|\mathbf x)$ and apply Jensen's inequality (p. 357):
$$\log\Pr(\mathbf x|\boldsymbol\phi)=\log\!\int q(\mathbf z_{1\ldots T}|\mathbf x)\frac{\Pr(\mathbf x,\mathbf z_{1\ldots T}|\boldsymbol\phi)}{q(\mathbf z_{1\ldots T}|\mathbf x)}d\mathbf z\ \ge\ \int q(\mathbf z_{1\ldots T}|\mathbf x)\log\frac{\Pr(\mathbf x,\mathbf z_{1\ldots T}|\boldsymbol\phi)}{q(\mathbf z_{1\ldots T}|\mathbf x)}d\mathbf z\tag{18.20}$$
The right side is the ELBO (18.21). In a VAE the encoder tightens the bound. Here the encoder has no parameters, so the decoder does all the work. It tightens the bound by (i) making the static encoder approximate the posterior and (ii) optimizing its own parameters on the bound (p. 358).

**18.4.2 Simplifying the ELBO.** Substitute 18.17 and 18.3, and split the log (p. 358):
$$\log\frac{\Pr(\mathbf x,\mathbf z_{1\ldots T}|\boldsymbol\phi)}{q(\mathbf z_{1\ldots T}|\mathbf x)}=\log\frac{\Pr(\mathbf x|\mathbf z_1,\boldsymbol\phi_1)}{q(\mathbf z_1|\mathbf x)}+\log\frac{\prod_{t=2}^T\Pr(\mathbf z_{t-1}|\mathbf z_t,\boldsymbol\phi_t)}{\prod_{t=2}^Tq(\mathbf z_t|\mathbf z_{t-1})}+\log\Pr(\mathbf z_T)\tag{18.22}$$
Rewrite the denominator by Markov-ness and Bayes' rule:
$$q(\mathbf z_t|\mathbf z_{t-1})=q(\mathbf z_t|\mathbf z_{t-1},\mathbf x)=\frac{q(\mathbf z_{t-1}|\mathbf z_t,\mathbf x)q(\mathbf z_t|\mathbf x)}{q(\mathbf z_{t-1}|\mathbf x)}\tag{18.23}$$
Substituting gives
$$=\log\Pr(\mathbf x|\mathbf z_1,\boldsymbol\phi_1)+\log\frac{\prod_{t=2}^T\Pr(\mathbf z_{t-1}|\mathbf z_t,\boldsymbol\phi_t)}{\prod_{t=2}^Tq(\mathbf z_{t-1}|\mathbf z_t,\mathbf x)}+\log\frac{\Pr(\mathbf z_T)}{q(\mathbf z_T|\mathbf x)}\approx\log\Pr(\mathbf x|\mathbf z_1,\boldsymbol\phi_1)+\sum_{t=2}^T\log\frac{\Pr(\mathbf z_{t-1}|\mathbf z_t,\boldsymbol\phi_t)}{q(\mathbf z_{t-1}|\mathbf z_t,\mathbf x)}\tag{18.24}$$
In the product of ratios $q(\mathbf z_{t-1}|\mathbf x)/q(\mathbf z_t|\mathbf x)$ all but the $q(\mathbf z_1|\mathbf x)$ and $q(\mathbf z_T|\mathbf x)$ terms cancel. The $q(\mathbf z_1|\mathbf x)$ term cancels with the first fraction. The last term is about $\log 1=0$, since $q(\mathbf z_T|\mathbf x)$ is standard normal and equals the prior (p. 359). The simplified ELBO is
$$\text{ELBO}[\boldsymbol\phi]\approx\mathbb E_{q(\mathbf z_1|\mathbf x)}\big[\log\Pr(\mathbf x|\mathbf z_1,\boldsymbol\phi_1)\big]-\sum_{t=2}^T\mathbb E_{q(\mathbf z_{t,t-1}|\mathbf x)}\Big[D_{KL}\big[q(\mathbf z_{t-1}|\mathbf z_t,\mathbf x)\,\big\|\,\Pr(\mathbf z_{t-1}|\mathbf z_t,\boldsymbol\phi_t)\big]\Big]\tag{18.25}$$
This uses marginalization of irrelevant variables and the KL definition (problem 18.7). The source writes the expectation index as $q(\mathbf z_{t,t-1}|\mathbf x)$ (p. 359).

**18.4.3 Analyzing the ELBO.** The first term (18.26) is the VAE-style reconstruction term. It is estimated by Monte Carlo with a sample from $q(\mathbf z_1|\mathbf x)$. Each KL term compares the two normals in 18.27. KL between normals has a closed form. Terms independent of $\boldsymbol\phi$ collapse into a constant $C$ (problem 18.8):
$$D_{KL}[\cdot\|\cdot]=\frac1{2\sigma_t^2}\Big\|\tfrac{(1-\alpha_{t-1})}{1-\alpha_t}\sqrt{1-\beta_t}\,\mathbf z_t+\tfrac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf x-\mathbf f_t[\mathbf z_t,\boldsymbol\phi_t]\Big\|^2+C\tag{18.28}$$

**18.4.4 Loss.** Negate the ELBO and use samples (p. 360), with $\mathbf z_{it}$ the latent for data point $i$ at step $t$:
$$L[\boldsymbol\phi]=\sum_{i=1}^I\Big(-\log\mathrm{Norm}_{\mathbf x_i}[\mathbf f_1[\mathbf z_{i1},\boldsymbol\phi_1],\sigma_1^2\mathbf I]+\sum_{t=2}^T\frac1{2\sigma_t^2}\Big\|\tfrac{1-\alpha_{t-1}}{1-\alpha_t}\sqrt{1-\beta_t}\,\mathbf z_{it}+\tfrac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf x_i-\mathbf f_t[\mathbf z_{it},\boldsymbol\phi_t]\Big\|^2\Big)\tag{18.29}$$
The first two terms in the norm are the "target", the mean of $q(\mathbf z_{t-1}|\mathbf z_t,\mathbf x)$. The last is the predicted $\mathbf z_{t-1}$.

**18.4.5 Training procedure** (p. 361). One network per time step is trained to match the most likely previous latent given the clean data. For the 1D example: (i) take many $\mathbf x$ from the data density, (ii) use the diffusion kernel to get $\mathbf z_t$ at each $t$, (iii) fit $\mathbf f_t$ to minimize 18.29. Here the models were nonparametric lookup tables. Figures 18.7–18.8 show the learned reverse process matching the true densities.

*Intuition note.* Each decoder step is trained to move a noisy latent to the average of where the clean data says it came from. The "teacher" is the closed-form posterior given $\mathbf x$, so training is plain regression.

### 18.5 Reparameterization of loss (p. 361–363)
Diffusion models are found to work better if the model predicts the noise that was mixed into the data (p. 361).

**18.5.1 Target.** From 18.30 ($\mathbf z_t=\sqrt{\alpha_t}\mathbf x+\sqrt{1-\alpha_t}\boldsymbol\epsilon$):
$$\mathbf x=\tfrac1{\sqrt{\alpha_t}}\mathbf z_t-\tfrac{\sqrt{1-\alpha_t}}{\sqrt{\alpha_t}}\boldsymbol\epsilon\tag{18.31}$$
Substitute into the target (the mean in 18.29), using $\sqrt{\alpha_t}/\sqrt{\alpha_{t-1}}=\sqrt{1-\beta_t}$ (problem 18.9):
$$\tfrac{1-\alpha_{t-1}}{1-\alpha_t}\sqrt{1-\beta_t}\mathbf z_t+\tfrac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf x=\tfrac{1-\alpha_{t-1}}{1-\alpha_t}\sqrt{1-\beta_t}\mathbf z_t+\tfrac{\beta_t}{1-\alpha_t}\Big(\tfrac1{\sqrt{1-\beta_t}}\mathbf z_t-\tfrac{\sqrt{1-\alpha_t}}{\sqrt{1-\beta_t}}\boldsymbol\epsilon\Big)\tag{18.32}$$
Collect terms (18.33): the $\mathbf z_t$ coefficient is $\tfrac{(1-\alpha_{t-1})\sqrt{1-\beta_t}}{1-\alpha_t}+\tfrac{\beta_t}{(1-\alpha_t)\sqrt{1-\beta_t}}$. Multiply the first fraction's top and bottom by $\sqrt{1-\beta_t}$ to get a common denominator. The numerator becomes $(1-\alpha_{t-1})(1-\beta_t)+\beta_t=1-\alpha_t$ (problem 18.10). The coefficient is therefore $1/\sqrt{1-\beta_t}$, and
$$\text{target}=\tfrac1{\sqrt{1-\beta_t}}\mathbf z_t-\tfrac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\boldsymbol\epsilon\tag{18.33}$$
Substituting into 18.29 gives 18.34, with the squared norm $\big\|\big(\tfrac1{\sqrt{1-\beta_t}}\mathbf z_{it}-\tfrac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\boldsymbol\epsilon_{it}\big)-\mathbf f_t[\mathbf z_{it},\boldsymbol\phi_t]\big\|^2$.

**18.5.2 Network.** Replace $\mathbf f_t$ by a network $\mathbf g_t$ predicting the noise, $\hat{\boldsymbol\epsilon}=\mathbf g_t[\mathbf z_t,\boldsymbol\phi_t]$, with the same size as $\mathbf z_t$:
$$\mathbf f_t[\mathbf z_t,\boldsymbol\phi_t]=\tfrac1{\sqrt{1-\beta_t}}\mathbf z_t-\tfrac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf g_t[\mathbf z_t,\boldsymbol\phi_t]\tag{18.35}$$
The $\mathbf z_t$ terms cancel inside the norm, leaving
$$L=\sum_i-\log\mathrm{Norm}_{\mathbf x_i}[\mathbf f_1[\mathbf z_{i1},\boldsymbol\phi_1],\sigma_1^2\mathbf I]+\sum_{t=2}^T\tfrac{\beta_t^2}{(1-\alpha_t)(1-\beta_t)2\sigma_t^2}\|\mathbf g_t[\mathbf z_{it},\boldsymbol\phi_t]-\boldsymbol\epsilon_{it}\|^2\tag{18.36}$$
The log normal is least squares plus a constant $C_i$ (18.37). Using 18.31 and 18.35, the first term simplifies to
$$\tfrac1{2\sigma_1^2}\|\mathbf x_i-\mathbf f_1[\mathbf z_{i1},\boldsymbol\phi_1]\|^2=\tfrac1{2\sigma_1^2}\Big\|\tfrac{\beta_1}{\sqrt{1-\alpha_1}\sqrt{1-\beta_1}}\mathbf g_1[\mathbf z_{i1},\boldsymbol\phi_1]-\tfrac{\beta_1}{\sqrt{1-\alpha_1}\sqrt{1-\beta_1}}\boldsymbol\epsilon_{i1}\Big\|^2\tag{18.38}$$
Dropping the constants $C_i$:
$$L=\sum_{i=1}^I\sum_{t=1}^T\tfrac{\beta_t^2}{(1-\alpha_t)(1-\beta_t)2\sigma_t^2}\|\mathbf g_t[\mathbf z_{it},\boldsymbol\phi_t]-\boldsymbol\epsilon_{it}\|^2\tag{18.39}$$
In practice the scaling factors are ignored:
$$L=\sum_i\sum_t\|\mathbf g_t[\mathbf z_{it},\boldsymbol\phi_t]-\boldsymbol\epsilon_{it}\|^2=\sum_i\sum_t\big\|\mathbf g_t\big[\sqrt{\alpha_t}\mathbf x_i+\sqrt{1-\alpha_t}\boldsymbol\epsilon_{it},\boldsymbol\phi_t\big]-\boldsymbol\epsilon_{it}\big\|^2\tag{18.40}$$

*Intuition note.* Predicting the noise and predicting the previous latent are equivalent up to known scalings (18.35). The text says diffusion models have been found to work better with this parameterization (p. 361). The loss says: add known noise to the data, then ask the network to guess that noise.

### 18.6 Implementation (p. 363–368)
**Algorithms** (p. 364). *Training (18.1):* repeat for each example in a batch: sample $t\sim\text{Uniform}[1..T]$ and $\boldsymbol\epsilon\sim\mathrm{Norm}[\mathbf 0,\mathbf I]$. Compute $\ell_i=\|\mathbf g_t[\sqrt{\alpha_t}\mathbf x_i+\sqrt{1-\alpha_t}\boldsymbol\epsilon,\boldsymbol\phi_t]-\boldsymbol\epsilon\|^2$. Accumulate the loss and take a gradient step. *Sampling (18.2):* draw $\mathbf z_T\sim\mathrm{Norm}[\mathbf 0,\mathbf I]$. For $t=T..2$: $\hat{\mathbf z}_{t-1}=\tfrac1{\sqrt{1-\beta_t}}\mathbf z_t-\tfrac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf g_t[\mathbf z_t,\boldsymbol\phi_t]$, then draw $\boldsymbol\epsilon$ and set $\mathbf z_{t-1}=\hat{\mathbf z}_{t-1}+\sigma_t\boldsymbol\epsilon$. Finally $\mathbf x=\tfrac1{\sqrt{1-\beta_1}}\mathbf z_1-\tfrac{\beta_1}{\sqrt{1-\alpha_1}\sqrt{1-\beta_1}}\mathbf g_1[\mathbf z_1,\boldsymbol\phi_1]$ (no noise added). Training is simple and naturally augments data: each $\mathbf x_i$ can be reused with different noise. Sampling needs serial evaluation of many networks and is slow (p. 363).

**18.6.1 Images.** The architecture is a U-Net (figure 18.9). Training and storing a U-Net per step is inefficient, so one U-Net is used for all steps. A predetermined time-step vector, a sinusoidal embedding passed through a shallow network, is resized to the channels at each stage and offsets and/or scales the representation. The U-Net has residual blocks and periodic global self-attention (p. 364–365). Many steps are needed because $q(\mathbf z_{t-1}|\mathbf z_t)$ is nearer to normal when $\beta_t$ is near zero. Sampling may need $T=1000$ steps for good images (p. 364).

**18.6.2 Speed.** Loss 18.40 requires the diffusion kernel to have the form $q(\mathbf z_t|\mathbf x)=\mathrm{Norm}[\sqrt{\alpha_t}\mathbf x,(1-\alpha_t)\mathbf I]$. It is valid for any forward process with this kernel, and a family of such processes exists. They differ in the forward rule and in how the estimated noise gives $\mathbf z_{t-1}$ (figure 18.10). Members include *denoising diffusion implicit models* (DDIM), which are not stochastic after the first step. Another is *accelerated sampling*, where the forward process is defined on a subsequence of steps, so the reverse process skips steps. Good samples can be made with 50 steps when the forward process is not stochastic. This is still slower than most other generative models (p. 365).

**18.6.3 Conditional generation.** *Classifier guidance* adds a gradient term to the last step of algorithm 18.2:
$$\mathbf z_{t-1}=\hat{\mathbf z}_{t-1}+\sigma_t^2\frac{\partial\log\Pr(c|\mathbf z_t)}{\partial\mathbf z_t}+\sigma_t\boldsymbol\epsilon\tag{18.41}$$
$\Pr(c|\mathbf z_t)$ is a classifier on $\mathbf z_t$, usually shared across time steps and taking time as input. It makes class $c$ more likely (p. 366). *Classifier-free guidance* puts $c$ into the main model $\mathbf g_t[\mathbf z_t,\boldsymbol\phi_t,c]$, typically through an embedding added like the time step. It is trained jointly on conditional and unconditional objectives by randomly dropping $c$. At test time the model can generate unconditional data, conditional data, or a weighted mix. If conditioning is over-weighted, the model tends to give very high-quality but slightly stereotypical examples, somewhat analogous to truncation in GANs (p. 366–367).

**18.6.4 Quality.** (i) Estimating the variances $\sigma_t^2$ as well as the means helps, especially with fewer steps. (ii) The noise schedule $\beta_t$ can vary by step and may improve results. (iii) A cascade of diffusion models makes high-resolution images. Each model conditions on the resized lower-resolution image appended to its U-Net layers, plus any class information (figure 18.11: $64\to256\to1024$). Figure 18.12 shows ImageNet-class-conditioned samples. Figure 18.13 shows text-conditioned samples, where captions encoded by a language model like BERT are inserted like the time step. The model is stochastic, so one caption can give many images (p. 367–368).

### 18.7 Summary (p. 368)
Data pass through latents by repeated noise blending until they look like white noise. Small steps let each denoising step be approximately normal and predicted by a deep network. The ELBO loss ends up as least squares. Image sampling is slow because each step is a U-Net. Deterministic formulations allow fewer steps. Conditioning on class, image and text gives impressive text-to-image results.

### Notes (p. 368–372), selected
- **History.** The author says Ho et al. (2020) produced samples competitive with GANs and that most of this chapter's exposition follows that paper. Dhariwal & Nichol (2021) showed images quantitatively superior to GANs by FID (p. 368).
- **Other data types and applications.** The author lists images (inpainting, super-resolution, medical imaging), video, 3D shapes, discrete data and audio (p. 370).
- **Alternatives to noise.** Blurring and non-stochastic degradations such as masking, morphing and pixelating also work (p. 370).
- **Versus other models.** A diffusion model can be viewed as a hierarchical VAE with a fixed encoder and a data-sized latent space. In basic form it gives only a lower bound on likelihood. Likelihood can be computed via an ODE or a continuous normalizing flow. Main disadvantages: slow, and a latent space with no semantic interpretation (p. 370).
- **Speed.** Stable diffusion runs diffusion in a smaller autoencoder latent space. Most processes in the compatible family are non-Markovian; DDIM is one with non-stochastic updates, which effectively turns the model into an ODE with low-curvature trajectories. Other speedups: distilling adjacent steps, more complex per-step distributions (e.g., conditional GANs) (p. 371).
- **Conditioning.** Text conditioning: a linearly transformed embedding is added to a U-Net layer like the time embedding. Control networks fine-tune models on edge maps, depth, etc. Before diffusion, text-to-image used transformers. GLIDE and DALL·E 2 use CLIP embeddings, and Imagen uses a large language model's embeddings (p. 371–372).
- **Connections.** Diffusion models are linked to stochastic differential equations, score matching and normalizing flows (p. 372).

## Toy example (ours)
Scalar data $x=2$, $T=2$, $\beta_1=0.19$, $\beta_2=0.36$.
1. $1-\beta_1=0.81$ and $1-\beta_2=0.64$, so $\alpha_1=0.81$ and $\alpha_2=0.81\times0.64=0.5184$. So $\sqrt{\alpha_2}=0.72$.
2. Kernel (18.8): $q(z_2|x)=\mathrm{Norm}[0.72\cdot2,\ 1-0.5184]=\mathrm{Norm}[1.44,\ 0.4816]$.
3. Cross-check with 18.5: variance $=(1-\beta_2)\beta_1+\beta_2=0.64\cdot0.19+0.36=0.1216+0.36=0.4816$ ✓.
4. Take noise $\epsilon=0.5$. $\sqrt{0.4816}\approx0.694$, so $z_2=1.44+0.694\cdot0.5\approx1.787$.
5. Recover $x$ with 18.31: $(1.787-0.347)/0.72=2$ ✓.
6. Training target for $g_2$ (18.40): the value $\epsilon=0.5$ itself.
7. Posterior mean (18.15), with $\alpha_1=0.81$, $1-\alpha_1=0.19$, $\sqrt{1-\beta_2}=0.8$: coefficient of $z_2$ is $\tfrac{0.19}{0.4816}\cdot0.8\approx0.3156$. Coefficient of $x$ is $\tfrac{0.9\cdot0.36}{0.4816}\approx0.6728$. Mean $\approx0.3156\cdot1.787+0.6728\cdot2\approx0.564+1.346=1.909$.
8. Noise-form check (18.33): $z_2/0.8-\tfrac{0.36}{0.694\cdot0.8}\cdot0.5\approx2.234-0.324=1.909$ ✓. Both forms give the same target mean.

## Concepts
- [[diffusion-model]] (new) — generative model with a fixed noising encoder and a learned denoising decoder; latents have the data's size (p. 349)
- [[forward-process]] (new) — Markov chain $\mathbf z_t=\sqrt{1-\beta_t}\mathbf z_{t-1}+\sqrt{\beta_t}\boldsymbol\epsilon_t$, prespecified (p. 350)
- [[noise-schedule]] (new) — the hyperparameters $\beta_t\in[0,1]$ controlling noise blending (p. 350)
- [[diffusion-kernel]] (new) — closed-form $q(\mathbf z_t|\mathbf x)=\mathrm{Norm}[\sqrt{\alpha_t}\mathbf x,(1-\alpha_t)\mathbf I]$ (p. 353)
- [[ancestral-sampling]] (new) — sampling $\mathbf z_T$, then each earlier latent in turn, up to $\mathbf x$ (p. 357)
- [[elbo]] (new; VAE concept reused) — lower bound on log-likelihood; here it needs no encoder parameters (p. 358)
- [[noise-prediction-loss]] (new) — least-squares loss for predicting the noise added to data (eq. 18.40, p. 363)
- [[ddim-accelerated-sampling]] (new) — deterministic or step-skipping reverse processes compatible with the same loss (p. 365)
- [[classifier-free-guidance]] (new) — conditional model trained with randomly dropped labels; the conditional and unconditional outputs can be weighted (p. 366)
- [[self-attention]] — used periodically inside the diffusion U-Net (p. 365)
- [[kl-divergence-normals]] (new) — closed-form KL; here it reduces to a squared difference of means plus a constant (p. 359)

## Canonical instances
- [[1d-diffusion-example]] — toy 1D density with T=100, β=0.03, used for figures 18.2–18.8 (p. 351–361)
- [[cascaded-text-to-image]] — 64→256→1024 pixel cascade conditioned on a language-model caption embedding (p. 367)
- [[imagenet-class-conditional-generation]] — one model producing varied classes via classifier guidance (p. 369)

## Bridges (candidates)
- [same-math] Diffusion ELBO ↔ VAE: the Jensen lower bound with a reconstruction term and KL terms is the same derivation as in chapter 17, with a fixed encoder.
- [structural-analogy] Classifier-free guidance ↔ GAN truncation: both trade variety for typicality (the text says "somewhat analogous", p. 367).
- [structural-analogy] Ancestral sampling over $T$ denoising steps ↔ LLM: autoregressive next-token sampling, both sequential draws that build a sample (our proposal).
- [structural-analogy] Sinusoidal time embedding added to channels ↔ LLM: positional encoding injected into an otherwise position-blind network (figure caption cites a sinusoidal embedding, p. 365).
- [structural-analogy] Text conditioning via a language-model embedding ↔ LLM: an LLM acts as a text encoder for another model (p. 367–368).

## Questions this raises
- If only a lower bound on likelihood is available, how can diffusion models be compared with flows and autoregressive models? (p. 370 hints at ODE-based likelihoods.)
- How many steps $T$ and what schedule $\beta_t$ are needed so the normal reverse approximation is accurate yet sampling stays cheap?
- Why does dropping the loss weights in 18.39 help in practice? The text reports only that it is done.
- What does over-weighting conditioning do to diversity, and is limiting variation inevitable? (Problem 18.12.)

## Exercises worth doing
- Ex. 18.1 (p. 372) — shows the variance-preserving update keeps $\mathrm{Cov}=\mathbf I$ — difficulty: easy
- Ex. 18.2 (p. 372) — mean and variance of a sum of two scaled noises; used in the kernel derivation — difficulty: easy
- Ex. 18.3 (p. 372) — extends the kernel derivation to $\mathbf z_3$ — difficulty: medium
- Ex. 18.9 (p. 373) — $\sqrt{\alpha_t/\alpha_{t-1}}=\sqrt{1-\beta_t}$, used in the reparameterization — difficulty: medium
- Ex. 18.10 (p. 373) — the algebra identity behind equation 18.33 — difficulty: medium
- Ex. 18.12 (p. 373) — compares guidance with variation-reducing tricks in other generative models — difficulty: easy

## Reading notes
- Printed page = pdf − 14 (e.g., pdf 363 = printed 349). Page labels give printed numbers.
- In section 18.6.2 (p. 364) the page prints the kernel covariance as $\sqrt{1-\alpha_t}\cdot\mathbf I$, while equation 18.8 (p.8 form.
- Equation 18.25's third line writes the expectation subscript as $q(\mathbf z_{t,t-1}|\mathbf x)$, as printed (p. 359).
- The unit contains Problems 18.1–18.12, with no solutions printed.
- Edition facts as printed: "Draft: please send errata to udlbookmail@gmail.com", CC-BY-NC-ND license, © MIT Press.
