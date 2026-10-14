---
id: murphy-2023-pml2/ch20-generative
work: murphy-2023-pml2
unit: "20 Generative models: an overview"
pages: 773–789
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Generative models: an overview

## L0 — One line
A generative model is a joint distribution p(x) (optionally p(x|c)); models differ in density, sampling, training, latents and architecture, serve many tasks, and are hard to evaluate: no single metric covers everything, and likelihood and sample quality can disagree.

## L1 — The gist (≤ 120 words)
The chapter asks what generative models are, what they are for, and how to judge and train them. Deep generative models (variational autoencoder, autoregressive, flow, diffusion, energy-based, adversarial) are compared on five criteria. Uses include sampling, density estimation, imputation, structure discovery, latent-space editing and compression. No single metric covers sample quality, diversity and generalization. Likelihood can be high with bad samples, or low with good ones. Feature-based scores (Inception score, FID, precision/recall) help but often rely on pretrained classifiers. For data on a low-dimensional manifold, plain maximum likelihood is flawed, and three fixes are given: add noise, use support-agnostic divergences, or train in two steps.

**Prerequisites:** KL divergence and cross entropy; Jensen's inequality; Gaussian mixtures; latent-variable models and autoencoders; basic hypothesis testing; trace and covariance matrices.

## L2 — Key ideas (5–10 bullets)
- A generative model is p(x), or p(x|c) when conditioned on inputs. A discriminative model arises when y is low-dimensional (e.g. a class label) (p. 776). It assumes one correct output, while a conditional generative model allows several (p. 776).
- Deep generative models are compared by density, sampling, training, latents and architecture. The deep models trade these off differently: for example, VAEs and GANs sample fast but have no exact density, while ARMs and flows have an exact density but sample slowly (pp. 773–775, Table 20.1).
- Typical tasks: generating data, density estimation, imputation, structure discovery, latent interpolation and arithmetic, design, world models, representation learning, compression (pp. 775–782).
- Latent-space editing uses linear interpolation $\lambda z_1+(1-\lambda)z_2$ and attribute offsets $\Delta_i=\bar z_i^+-\bar z_i^-$ (pp. 781–782).
- Evaluation must cover quality, diversity and generalization. No known metric meets all three (pp. 782–783).
- Likelihood can mislead: for large $D$, mixing in 99% white-noise samples barely changes the log-likelihood, and a model that memorizes the training set has good samples but will almost certainly have poor test likelihood (p. 784).
- IS (class labels), FID and precision/recall (features) rely on a pretrained classifier and are exposed to its drawbacks (pp. 785–787).
- Under the manifold hypothesis, MLE can give infinite likelihood to wrong models. Fixes: noise, support-agnostic divergences, two-step training (pp. 788–789).

## L3 — Walkthrough

### 20.1 Introduction (p. 773)
A generative model is a joint distribution $p(\boldsymbol x)$, $\boldsymbol x\in\mathcal X$. If it is conditioned on inputs $\boldsymbol c\in\mathcal C$, it is a conditional generative model $p(\boldsymbol x|\boldsymbol c)$ (p. 773).

### 20.2 Types of generative model (pp. 773–775)
- **DGM vs PGM.** Deep generative models (DGM) map a single latent vector $\boldsymbol z$ to $\boldsymbol x$ with a deep network. Classical probabilistic graphical models (PGM) map interconnected latents $z_1,\dots,z_L$ to $x_1,\dots,x_D$ with simpler, often linear, maps. Hybrids exist (p. 773).
- **Main DGMs:** VAE, autoregressive model (ARM), normalizing flow, diffusion, energy-based model (EBM), GAN (p. 773).
- **Five criteria:**
  - *Density.* Can $p(\boldsymbol x)$ be evaluated pointwise, and how? GANs are implicit, so there is no density. VAEs give only a lower bound. EBMs and undirected PGMs give an approximation (p. 773).
  - *Sampling.* Directed PGMs, VAEs and GANs sample fast. Undirected PGMs, EBMs, ARMs, diffusion and flows are slow (p. 773).
  - *Training.* Exact MLE is possible for ARMs, flows and directed PGMs, but the objective is usually non-convex, so only a local optimum is reached. VAEs maximize a lower bound. EBMs and undirected PGMs maximize an approximation. GANs use min-max training, which can be unstable and has no clear objective to monitor (pp. 773–775).
  - *Latents.* ARMs have none. Flows and diffusion have latents the same size as $\boldsymbol x$. Graphical models and EBMs may or may not have latents (p. 775).
  - *Architecture.* Flows need invertible networks with a tractable Jacobian. EBMs can use any model (p. 775).

Table 20.1 (p. 774), abridged (the Chapter and Architecture columns are omitted here; architecture is covered in the bullet above):

| Model | Density | Sampling | Training | Latents |
|---|---|---|---|---|
| PGM-D | Exact, fast | Fast | MLE | Optional |
| PGM-U | Approx, slow | Slow | MLE-A | Optional |
| VAE | LB, fast | Fast | MLE-LB | $\mathbb R^L$ |
| ARM | Exact, fast | Slow | MLE | None |
| Flows | Exact, slow/fast | Slow | MLE | $\mathbb R^D$ |
| EBM | Approx, slow | Slow | MLE-A | Optional |
| Diffusion | LB | Slow | MLE-LB | $\mathbb R^D$ |
| GAN | NA | Fast | Min-max | $\mathbb R^L$ |

*Intuition note:* among the deep models in the table the trade-offs differ. VAE and GAN sample fast but have no exact density (a lower bound, or none). ARM and flow have an exact density but sample slowly. (Directed PGMs are exact and fast on both.)

### 20.3 Goals of generative modeling (pp. 775–782)
**20.3.1 Generating data (pp. 775–776).** Sample new data (generative AI). Misuse for fake content gives deep fakes. Synthetic data can train discriminative models. Conditional models $p(\boldsymbol x|\boldsymbol c)$ control the output. Examples: text→image, image→text (captioning), image→image (colorization, inpainting, uncropping, JPEG restoration), speech→text (ASR), sequence-to-sequence (translation), prompt→text continuation (p. 775, p. 776). Figs 20.2–20.3 show Imagen (diffusion) and Parti (transformer) images generated from text prompts, and Fig. 20.4 shows Palette image-to-image tasks (pp. 776–777). If $\boldsymbol y$ is a low-dimensional label, we get a discriminative model. The difference is that a discriminative model assumes one correct output, while a conditional generative model assumes there may be several. This makes evaluation harder (p. 776).

**20.3.2 Density estimation (pp. 777–778).** Compute $p(\boldsymbol x)$ for an observed vector. Uses: outlier detection, compression, generative classifiers, model comparison (p. 777). In low dimensions, kernel density estimation (KDE) works:
$$p(\boldsymbol x|\mathcal D)=\frac1N\sum_{n=1}^N \mathcal K_h(\boldsymbol x-\boldsymbol x_n)\tag{20.1}$$
Here $\mathcal D=\{\boldsymbol x_1,\dots,\boldsymbol x_N\}$. The kernel $\mathcal K:\mathbb R\to\mathbb R_+$ satisfies $\int\mathcal K(x)dx=1$ and $\int x\mathcal K(x)dx=0$, and $h$ is the bandwidth (p. 778). Figure 20.5 uses 6 points, uniform and Gaussian kernels, $h=1,2$ (p. 778). In higher dimensions KDE suffers from the curse of dimensionality, so parametric $p_{\boldsymbol\theta}(\boldsymbol x)$ is needed (p. 778).

**20.3.3 Imputation (pp. 778–779).** Fill in missing entries $\mathbf X_m$ of an $N\times D$ matrix given observed $\mathbf X_o$. Mean imputation uses $\mathbb E[x_d]$ per column. It ignores dependencies within rows and gives no uncertainty (p. 779). In Fig. 20.6 the column means are 9, 8, 7.5, and NAs are replaced by them (p. 779). Multiple imputation fits $p(\mathbf X_o)$, e.g. with EM, and samples from $p(\mathbf X_m|\mathbf X_o)$ (p. 779). Image inpainting is a more complex case (p. 779).

**20.3.4 Structure discovery (pp. 779–780).** If latents $\boldsymbol z$ are the "causes" of $\boldsymbol x$, Bayes' rule gives $p(\boldsymbol z|\boldsymbol x)\propto p(\boldsymbol z)p(\boldsymbol x|\boldsymbol z)$ (p. 779). Example: flow-cytometry data with 5400 datapoints. Each datum is $\boldsymbol x_n\sim p(\cdot|\boldsymbol a_n,\boldsymbol z)$, with $\boldsymbol x\in\mathbb R^{11}$ (phosphorylations), $\boldsymbol a\in\{0,1\}^6$ (perturbations) and $\boldsymbol z$ the unknown signaling network. Dynamic programming [EM07] infers $p(\boldsymbol z|\mathcal D)$. The median graph keeps edges with $p(z_{ij}=1|\mathcal D)>0.5$. Fig. 20.7 reports one false negative (pp. 779–780).

**20.3.5 Latent space interpolation (pp. 780–781).** Let $\boldsymbol z_1=e(\boldsymbol x_1)$ and $\boldsymbol z_2=e(\boldsymbol x_2)$ be encodings. Then
$\boldsymbol z=\lambda\boldsymbol z_1+(1-\lambda)\boldsymbol z_2$ with $0\le\lambda\le1$, and $\boldsymbol x'=d(\boldsymbol z)$ with decoder $d$. The result combines semantic features of both inputs. Linear interpolation is justified because the learned manifold often has approximately zero curvature [SKTF18]. Nonlinear interpolation is sometimes better (p. 781). Examples: a β-VAE ($\beta=0.5$) on MNIST (7 to 2) and on CelebA (Figs 20.8, 20.9) (p. 780, p. 781).

**20.3.6 Latent space arithmetic (pp. 781–782).** For attribute $i$, let $\bar{\boldsymbol z}_i^+$ and $\bar{\boldsymbol z}_i^-$ be the mean embeddings of images with and without it, and $\boldsymbol\Delta_i=\bar{\boldsymbol z}_i^+-\bar{\boldsymbol z}_i^-$. Adding a positive multiple of $\boldsymbol\Delta_i$ to a point increases the attribute. Subtracting decreases it (p. 782). Reconstruction: $\hat{\boldsymbol x}_j=d(\boldsymbol z+s_j\boldsymbol\Delta)$, with $\boldsymbol z=e(\boldsymbol x)$. For sunglasses, $s_j>0$ adds them. $s_j<0$ removes them but also makes the face look younger and more female, "possibly a result of dataset bias" (p. 782).

*Intuition note:* the latent space behaves roughly like a flat map of semantic features. Moving between two codes, or along an attribute direction, gives new but plausible images. The author notes that the side effects (a younger, more female face) are possibly a result of dataset bias.

**20.3.7–20.3.10 (p. 782).**
- *Generative design:* generate candidate objects such as molecules with desired properties, e.g. Bayesian optimization in a VAE's latent space.
- *Model-based RL:* learn a "world model" so the agent can plan and learn "in its head" where real data is costly.
- *Representation learning:* learn possibly uninterpretable $\boldsymbol z$ for downstream supervised tasks.
- *Compression:* the optimal code length for $\boldsymbol x$ from a source $p(\boldsymbol x)$ is $l(\boldsymbol x)=-\log p(\boldsymbol x)$, as proved by Shannon.

### 20.4 Evaluating generative models (pp. 782–788)
(Section written by Rosca, Mohamed and Lakshminarayanan, p. 782.) Metrics should capture **sample quality**, **sample diversity** (all modes covered) and **generalization**. No known metric meets all three (pp. 782–783).

**20.4.1 Likelihood-based evaluation (p. 783).**
$$D_{\mathrm{KL}}(p\|q)=\int p(\boldsymbol x)\log\frac{p(\boldsymbol x)}{q(\boldsymbol x)}=-\mathbb H(p)+\mathbb H_{ce}(p,q)\tag{20.2}$$
$\mathbb H(p)$ is constant. With the empirical distribution for $p$, the cross entropy becomes the negative log likelihood
$$\mathrm{NLL}=-\frac1N\sum_{n=1}^N\log q(\boldsymbol x_n)\tag{20.3}$$
usually on held-out data (p. 783).

*20.4.1.1 Computing it (p. 783).* For discrete data (language models) NLL is easy. Perplexity is $2^H$ with $H=$ NLL. For images and audio the model is continuous but data are discrete, so the pdf can exceed 1 and average log-likelihood can be arbitrarily large. Standard fix: uniform dequantization, adding uniform noise to the data. This gives a lower bound on the discrete model's average log-likelihood. Derivation: $\boldsymbol z$ is continuous, $p(\boldsymbol x|\boldsymbol z)=\delta(\boldsymbol x-\mathrm{round}(\boldsymbol z))$, and $p(\boldsymbol x)=\int p(\boldsymbol x|\boldsymbol z)p(\boldsymbol z)d\boldsymbol z$. Let $q(\boldsymbol z|\boldsymbol x)$ have support only where $p(\boldsymbol x|\boldsymbol z)=1$. Jensen's inequality gives
$$\log p(\boldsymbol x)\ge\mathbb E_{q(\boldsymbol z|\boldsymbol x)}[\log p(\boldsymbol x|\boldsymbol z)+\log p(\boldsymbol z)-\log q(\boldsymbol z|\boldsymbol x)]\tag{20.4}$$
$$=\mathbb E_{q(\boldsymbol z|\boldsymbol x)}[\log p(\boldsymbol z)-\log q(\boldsymbol z|\boldsymbol x)]\tag{20.5}$$
(the term $\log p(\boldsymbol x|\boldsymbol z)$ drops out because it is 0 on the support of $q$; added step). So modelling the density of dequantized $\boldsymbol z\sim q(\boldsymbol z|\boldsymbol x)$ lower-bounds $p(\boldsymbol x)$ (p. 783). Footnote 4: bits per dimension is log-likelihood in base 2 divided by $|\boldsymbol x|$ (p. 783).

*20.4.1.2 Hard to compute (p. 784).* The likelihood needs the normalization constant. Remedies: variational inference (lower, sometimes upper, bounds) or annealed importance sampling (Monte Carlo estimate). For implicit models such as GANs the likelihood is not defined (p. 784).

*20.4.1.3 Likelihood is not related to sample quality (p. 784).* Likelihood is often uncorrelated with perceptual quality for images and sound. Both directions can fail:
- **Good likelihood, bad samples** (argument from [TOB16]). Let $q_0$ be an excellent density model and $q_1$ a bad one (white noise). Define
$$q_2(\boldsymbol x)=0.01\,q_0(\boldsymbol x)+0.99\,q_1(\boldsymbol x)\tag{20.6}$$
99% of its samples are poor. Yet
$$\log q_2(\boldsymbol x)\ge\log[0.01\,q_0(\boldsymbol x)]=\log q_0(\boldsymbol x)-2\tag{20.7}$$
For high-dimensional data $|\log q_0(\boldsymbol x)|\sim D\gg100$, so $\log q_2\approx\log q_0$.
- **Good samples, bad likelihood.** Take a GMM centered on the training images:
$$q(\boldsymbol x)=\frac1N\sum_{n=1}^N\mathcal N(\boldsymbol x|\boldsymbol x_n,\epsilon^2\mathbf I)\tag{20.8}$$
If $\epsilon$ is small, samples look good because they are the training images. But the test likelihood will almost certainly be poor: the model has memorized the training set.

*Intuition note:* likelihood is a sum of log-densities over many dimensions. Mixing a good model with a poor one changes $\log q$ by at most a constant (2 in (20.7)), which is tiny next to $|\log q_0|\sim D$ in high dimensions. And a model that copies the training data gives good samples but will almost certainly score badly on new data.

**20.4.2 Distances in feature space (pp. 784–785).** Most metrics compare feature distributions from a neural network, often a pretrained classifier. Inception score (IS):
$$\mathrm{IS}=\exp\big[\mathbb E_{p_{\boldsymbol\theta}(\boldsymbol x)}D_{\mathrm{KL}}(p_{\rm disc}(Y|\boldsymbol x)\|p_{\boldsymbol\theta}(Y))\big]\tag{20.9}$$
with $p_{\boldsymbol\theta}(y)=\int p_{\rm disc}(y|\boldsymbol x)p_{\boldsymbol\theta}(\boldsymbol x)d\boldsymbol x$. The log form is
$$\log(\mathrm{IS})=\mathbb H(p_{\boldsymbol\theta}(Y))-\mathbb E_{p_{\boldsymbol\theta}(\boldsymbol x)}[\mathbb H(p_{\rm disc}(Y|\boldsymbol x))]\tag{20.10}$$
A high-scoring model will be equally likely to generate samples from all classes (maximizing the marginal entropy), and each sample will be easy to classify (minimizing the conditional entropy) (p. 785). IS uses only class labels, so it misses overfitting and within-class diversity. One perfect example per class gives a perfect IS (p. 785). The Fréchet Inception distance (FID) fits Gaussians to classifier features of model samples ($\boldsymbol\mu_m,\boldsymbol\Sigma_m$) and data ($\boldsymbol\mu_d,\boldsymbol\Sigma_d$):
$$\mathrm{FID}=\|\boldsymbol\mu_m-\boldsymbol\mu_d\|_2^2+\mathrm{tr}\big(\boldsymbol\Sigma_d+\boldsymbol\Sigma_m-2(\boldsymbol\Sigma_d\boldsymbol\Sigma_m)^{1/2}\big)\tag{20.11}$$
Lower is better. The Fréchet distance has high bias that depends on sample count. The kernel Inception distance (squared MMD between feature sets) was introduced to mitigate this (p. 785).

**20.4.3 Precision and recall (pp. 785–786).** FID alone is hard to use as a diagnostic: a bad (high) FID can mean low-quality samples, too much mass around the data distribution, or coverage of only a subset of the data. Hence the motivation to seek separate precision (sample quality) and recall (sample diversity) metrics. For feature sets $\Phi$, with $\mathrm{NN}_k(\phi',\Phi)$ the $k$-th nearest neighbour of $\phi'$ in $\Phi$:
$$f_k(\phi,\Phi)=\begin{cases}1&\text{if }\exists\phi'\in\Phi\text{ s.t. }\|\phi-\phi'\|_2^2\le\|\phi'-\mathrm{NN}_k(\phi',\Phi)\|_2^2\\0&\text{otherwise}\end{cases}\tag{20.12}$$
$$\mathrm{precision}(\Phi_{model},\Phi_{data})=\frac1{|\Phi_{model}|}\sum_{\phi\in\Phi_{model}}f_k(\phi,\Phi_{data})\tag{20.13}$$
$$\mathrm{recall}(\Phi_{model},\Phi_{data})=\frac1{|\Phi_{data}|}\sum_{\phi\in\Phi_{data}}f_k(\phi,\Phi_{model})\tag{20.14}$$
Both lie in $[0,1]$. Precision asks whether samples are as close to data as data is to other data. Recall asks whether data is as close to model samples as model samples are to each other. Larger $k$ is more lenient and raises both. Together they give a trade-off curve between models (p. 786).

**20.4.4 Statistical tests (pp. 786–787).** Two-sample tests take as null hypothesis that both sample sets come from one distribution. Classifier-based statistics and MMD have been used, with learned features in high dimensions. The user can set the Type 1 error. The tests tend to be computationally expensive, so they cannot be used to monitor training and are best used to compare fully trained models (p. 787).

**20.4.5 Pretrained-classifier problems (p. 787).** A suitable classifier may be unavailable. Features from a classifier trained on another dataset may not be reliable, given the well-known challenges with neural-network generalization. On the same dataset, imperfect model samples are out-of-distribution for the classifier. These issues have been shown to affect evaluation in practice (p. 787).

**20.4.6 Training classifiers on samples (p. 787).** Train a classifier on conditional-model samples and check its performance, e.g. whether synthetic data added to real data helps. Ultimately performance depends on the downstream task (semi-supervised accuracy, RL agent performance) (p. 787).

**20.4.7 Assessing overfitting (pp. 787–788).** Inspect, for each sample, its $K$ nearest dataset neighbours in classifier feature space (Fig. 20.12). If the sample differs from them, it is not simply memorized. This is manual. Measuring diversity by searching a large sample pool is expensive and often needs human assessment (p. 787). For likelihood-based models (VAE, ARM, flows), check how much the log-likelihood changes when a sample is added to the training set (p. 788).

**20.4.8 Human evaluation (p. 788).** Raters compare model and data samples. Suitable for art or human-facing data, or when automated metrics are unreliable. Hard to standardize and automate, and costly (p. 788).

### 20.5 Training objectives (pp. 788–789)
(Section added September 2024, p. 788.) MLE maximizes $\mathbb E_{p(\boldsymbol x)}[\log q(\boldsymbol x)]=-D_{\mathrm{KL}}(p\|q)+\text{const}$ (p. 788). **Problem:** under the manifold hypothesis, $p(\boldsymbol x)>0$ only on a $d^*$-dimensional subspace $\mathcal M\subset\mathbb R^D$ with $d^*<D$. The likelihood objective assumes $p$ is defined on all of $\mathbb R^D$. Otherwise many $q$ can give infinite likelihood to $\mathcal M$ without matching $p$, since $\mathcal M$ is "too thin". Example: $p$ is a mixture of two delta functions and $q$ a GMM. The component variances go to 0 and the likelihood to infinity, but the mixture weights may be wrong (p. 789). Three solutions:
1. **Add noise** so $p$ and $q$ cover all $D$ dimensions. Options: diffusion models (noise at many levels), or the spread KL $D_{\mathrm{KL}\sigma}(p\|q)=D_{\mathrm{KL}}(p_\sigma\|q_\sigma)$, with $p_\sigma=p\circledast\mathcal N(\cdot|\mathbf 0,\sigma^2\mathbf I_D)$ and $q_\sigma$ likewise. This KL is always finite. Optimize with $q(\boldsymbol x)=\mathcal N(\boldsymbol x|g_{\boldsymbol\theta}(\boldsymbol z),\sigma^2\mathbf I)$, $g:\mathbb R^d\to\mathbb R^D$, $\boldsymbol z\sim\mathcal N(\mathbf 0,\mathbf I_d)$. After training, turn the decoder noise off (the delta-VAE) (p. 789).
2. **Support-agnostic divergences** that "metrize weak convergence", e.g. Wasserstein distance and MMD. Methods of this type are GANs (p. 789).
3. **Two-step methods.** Step 1: an autoencoder with $\boldsymbol z=f_{\boldsymbol\phi}(\boldsymbol x)$, $\boldsymbol x=g_{\boldsymbol\theta_1}(\boldsymbol z)$, $d\ll D$, minimizing $\mathcal L(\boldsymbol\phi,\boldsymbol\theta_1)=\mathbb E_{p(\boldsymbol x)}\big[\|\boldsymbol x-g_{\boldsymbol\theta_1}(f_{\boldsymbol\phi}(\boldsymbol x))\|_2^2\big]$. Step 2: fit a density $q_{\boldsymbol\theta_2}(\boldsymbol z)$ to $p_{\boldsymbol\phi^*}(\boldsymbol z)=\text{push-through}(p(\boldsymbol x),f_{\boldsymbol\phi^*})$. This target is low-dimensional with full support, so standard MLE is safe. Then $\boldsymbol z\sim q_{\boldsymbol\theta_2}$, $\boldsymbol x=g_{\boldsymbol\theta_1}(\boldsymbol z)$. [LG+24] prove this optimizes (an upper bound on) the Wasserstein distance between $q$ and $p$. It is used by latent diffusion, VQ-VAE and some VAEs (p. 789).

*Intuition note:* maximum likelihood needs $p$ to have a density everywhere. Data on a thin surface breaks this, so the fixes thicken the data (noise), change the divergence, or first shrink the space to the surface (autoencoder).

## Toy example (ours)
*Likelihood versus quality.* Let $D=1000$ and suppose $\log q_0(\boldsymbol x)=1000$ nats on a test point, i.e. 1 nat per dimension. Mix with noise: $q_2=0.01q_0+0.99q_1$. By (20.7), $\log q_2\ge1000+\ln0.01=1000-4.605=995.395$. So the per-dimension log-likelihood drops by at most $4.605/1000\approx0.0046$ nats, yet 99% of samples from $q_2$ are noise.

*Inception score for a "one sample per class" model.* Take 2 classes. The model emits one perfect image per class, each half the time. The classifier is one-hot, so $\mathbb H(p_{\rm disc}(Y|\boldsymbol x))=0$. The marginal is $(0.5,0.5)$, so $\mathbb H(p_{\boldsymbol\theta}(Y))=\ln2$. By (20.10), $\log\mathrm{IS}=\ln2-0$, so IS $=2$, the number of classes. This is the best possible here although there is no variety within a class.

## Concepts
- [[generative-model]] (new) — joint distribution $p(\boldsymbol x)$, or $p(\boldsymbol x|\boldsymbol c)$ if conditional (p. 773)
- [[deep-generative-model]] (new) — model mapping a latent $\boldsymbol z$ to $\boldsymbol x$ with a deep net: VAE, ARM, flow, diffusion, EBM, GAN (p. 773)
- [[implicit-generative-model]] (new) — model such as a GAN with no defined density $p(\boldsymbol x)$ (p. 773, p. 784)
- [[kernel-density-estimation]] (new) — $\frac1N\sum_n\mathcal K_h(\boldsymbol x-\boldsymbol x_n)$; fails in high dimensions (p. 778)
- [[imputation]] (new) — filling missing data; multiple imputation samples $p(\mathbf X_m|\mathbf X_o)$ (p. 778, p. 779)
- [[latent-space-interpolation]] (new) — decode $\lambda\boldsymbol z_1+(1-\lambda)\boldsymbol z_2$ (p. 781)
- [[latent-space-arithmetic]] (new) — shift a code by an attribute offset $\boldsymbol\Delta$ (p. 782)
- [[kl-divergence]] — KL divergence; equals $-\mathbb H(p)+\mathbb H_{ce}(p,q)$ (p. 783)
- [[uniform-dequantization]] (new) — add uniform noise to discrete data; gives a lower bound on log-likelihood (p. 783)
- [[perplexity]] (new) — $2^H$, with $H$ the NLL/cross entropy (p. 783)
- [[inception-score]] (new) — $\exp\mathbb E\,D_{\mathrm{KL}}(p_{\rm disc}(Y|\boldsymbol x)\|p_{\boldsymbol\theta}(Y))$ (p. 785)
- [[fid]] (new) — Fréchet distance between Gaussian fits of classifier features (p. 785)
- [[precision-recall-generative]] (new) — nearest-neighbour feature-space measures of quality and diversity (p. 786)
- [[manifold-hypothesis]] (new) — data lie on a $d^*<D$ dimensional subspace (p. 789)
- [[two-step-generative-training]] (new) — autoencoder first, then a density on the latents (p. 789)
- [[bayes-theorem]] — used as $p(\boldsymbol z|\boldsymbol x)\propto p(\boldsymbol z)p(\boldsymbol x|\boldsymbol z)$ for structure discovery (p. 779)

## Canonical instances
- [[text-to-image-samples]] — Imagen and Parti outputs from text prompts (pp. 775–776)
- [[mean-imputation-table]] — column means 9, 8, 7.5 fill the NAs (p. 779)
- [[flow-cytometry-network]] — signaling graph inferred from 5400 datapoints, 11 proteins (pp. 779–780)
- [[beta-vae-celeba-sunglasses]] — latent arithmetic with $s\in\{-2,\dots,2\}$ (p. 781, p. 782)
- [[noisy-mixture-vs-likelihood]] — $q_2=0.01q_0+0.99q_1$ keeps log-likelihood (p. 784)
- [[memorizing-gmm]] — GMM on training images: good samples, poor test likelihood (p. 784)
- [[two-delta-mixture]] — GMM on two deltas gives infinite likelihood, wrong weights (p. 789)

## Bridges (candidates)
- [same-math] $-\log p(\boldsymbol x)$ as optimal code length (p. 782) ↔ information theory: cross entropy as NLL on data (p. 783) — same quantity.
- [same-math] Eq. (20.8) GMM on training points ↔ KDE (20.1) with a Gaussian kernel — same form, bandwidth $\epsilon$.
- [structural-analogy] Multiple imputation $p(\mathbf X_m|\mathbf X_o)$ ↔ Bayesian posterior predictive for missing data — sampling unknowns given observed.
- [structural-analogy] Structure discovery $p(\boldsymbol z|\mathcal D)$ over graphs ↔ Bayesian inference over latent structure — a posterior over model structure.
- [structural-analogy] Two-sample tests with MMD ↔ frequentist hypothesis testing — null, statistic, Type 1 error.

## Questions this raises
- If likelihood can be uncorrelated with sample quality, which evaluation is appropriate for a given downstream use (compression, design, imputation)?
- How should FID or precision/recall be adapted when no suitable pretrained classifier exists for the domain?
- How does the spread-KL noise level $\sigma$ trade off against fidelity to the manifold?
- Why does the two-step approach bound the Wasserstein distance, and what is the proof in [LG+24]?

## Reading notes
- Printed page = pdf − 34 (pdf 807 = printed 773). The text layer for pdf 824 (printed 790) is empty and no image was provided, so it is treated as a blank final page. The sentence on p. 789 ends with a comma ("…one per stage),"), apparently unfinished.
- Section 20.4 is credited to Rosca, Mohamed and Lakshminarayanan (p. 782). Section 20.5 carries a footnote: added September 2024 (p. 788). Running footer: online version, December 10, 2025.
- Footnote 4 (p. 783) prints bpd as $\mathrm{NLL}\log_e(2)\frac1{|\boldsymbol x|}$. By the identity $\log_2L=\log_eL/\log_e2$ given in the same footnote, this should divide by $\log_e 2$. I left it uncorrected in L3 and only summarised the definition.
- Eq. (20.7) uses $\log 0.01=-2$. This holds for base-10 logs. For natural logs it is $-4.6$ (used in the toy). The conclusion is unchanged for large $D$.
- Eq. (20.1) states the kernel as $\mathcal K:\mathbb R\to\mathbb R_+$ while $\boldsymbol x$ is a vector. Reported as printed.
- Table 20.1 and Fig. 20.1 were checked in the image. The text layer's "RL"/"RD" are $\mathbb R^L$/$\mathbb R^D$.
- No exercises in this unit.
