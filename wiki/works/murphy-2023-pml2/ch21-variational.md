---
id: murphy-2023-pml2/ch21-variational
work: murphy-2023-pml2
unit: "21 Variational autoencoders"
pages: 791–820
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
# Variational autoencoders

## L0 — One line
A VAE trains a decoder (generative model) and an encoder (amortized approximate posterior) together by maximizing the ELBO, and the chapter then presents variants that reweight the ELBO terms, change the latent structure or change the encoder or decoder, and several methods address the recurring problem of posterior collapse.

## L1 — The gist (≤ 120 words)
Question: how can we fit a deep latent variable model when the posterior and the marginal likelihood are intractable? Answer: train an encoder network $q_\phi(z|x)$ together with a decoder $p_\theta(x|z)$ by maximizing the ELBO (a lower bound on log-likelihood). The chapter gives several rewritings of the ELBO (equal up to additive constants), then variants: β-VAE, InfoVAE, multimodal, semi-supervised, sequence, hierarchical and vector-quantized VAEs. A recurring difficulty is posterior collapse, where the latent code is ignored. Several fixes are presented. The main advantage of a VAE over a deterministic autoencoder is that it defines a proper generative model, so decoding prior samples gives sensible new images.

**Prerequisites:** KL divergence and the ELBO; Gaussian distributions (precision, product of Gaussians); reparameterization trick; mutual information; basic neural nets (CNN, RNN, transformer) as black boxes.

## L2 — Key ideas (5–10 bullets)
- A VAE is a deep latent variable model plus an amortized inference network. Both are trained on one ELBO objective (p. 791–792).
- Versus a deterministic autoencoder, a VAE can generate sensible images from prior samples. Its reconstructions are blurrier (p. 794).
- The ELBO can be rewritten as a joint KL, or as two KL terms in $x$-space and $z$-space. If the two objectives conflict (e.g. limited model power), the VAE will favor reconstruction accuracy over posterior inference (p. 796).
- β-VAE and InfoVAE reweight the terms. Squared-error decoders give blur because the decoder predicts an average (p. 797–800).
- With a product-of-experts posterior (the prior multiplied by one Gaussian "expert" per observed modality), multimodal VAEs can compute a posterior for any subset of modalities, though training covers only a fixed number of missingness patterns. The M2 model (which adds a latent class label $y$) handles labeled and unlabeled data (p. 801–803).
- Posterior collapse (latent ignored) has many remedies: KL annealing (slowly raising the KL weight), limiting the flexibility of $q$ to lower-bound the rate, free bits (a hinge floor on each latent dimension's KL), skip connections (more direct links from $z$ to the decoder), better inference, other objectives (p. 806–809).
- Hierarchical VAEs (stacked latent layers; top-down inference means each layer's posterior also uses the layers above it) can emulate any autoregressive model if they have at least $D$ layers, and a tree-like latent code can enable generation in $O(\log D)$ time. Their training needs stabilizing tricks (p. 809–814).
- VQ-VAE uses discrete codes chosen from a codebook of vectors. It is trained with straight-through gradients (decoder-input gradients copied to the encoder output, past the quantization step) plus a codebook loss (pulls codewords toward encoder outputs) and a commitment loss (keeps encoder outputs near their codewords) (p. 815–817).

## L3 — Walkthrough

### 21.1 Introduction (p. 791)
The model is $z\sim p_\theta(z)$, $x|z\sim \mathrm{Expfam}(x|d_\theta(z))$ \tag{21.1–21.2}. Here $d_\theta$ is a deep network, the **decoder**. This is a deep latent variable model (DLVM); with a Gaussian prior it is a deep latent Gaussian model (DLGM). Both $p_\theta(z|x)$ and $p_\theta(x)=\int p_\theta(x|z)p_\theta(z)\,dz$ \tag{21.3} are intractable. Hence we use **amortized inference**: a second network $q_\phi(z|x)$, the recognition or inference network, is trained at the same time. The combination is the VAE (p. 791).

### 21.2 VAE basics
**21.2.1 Assumptions (p. 792).** $p_\theta(z,x)=p_\theta(z)p_\theta(x|z)$ \tag{21.4}. Example for binary data: $p_\theta(x|z)=\prod_{d=1}^D \mathrm{Ber}(x_d|\sigma(d_\theta(z)))$ \tag{21.5}. The recognition model is $q_\phi(z|x)=q(z|e_\phi(x))\approx p_\theta(z|x)$ \tag{21.6}, usually Gaussian:
$$q_\phi(z|x)=\mathcal N(z|\mu,\mathrm{diag}(\exp(\ell))),\quad (\mu,\ell)=e_\phi(x),\quad \ell=\log\sigma \tag{21.7–21.8}$$
So $x$ is encoded into a stochastic bottleneck $z$ and decoded back (Fig. 21.1). The idea first appeared in the Helmholtz machine, which used wake-sleep training rather than one unified objective. Murphy says the VAE optimizes a variational lower bound on the log-likelihood, so convergence to a locally optimal MLE is guaranteed. He adds that an inference network is often faster than other ways of fitting a DLGM and can have regularization benefits (p. 792).

**21.2.2 Fitting (p. 793).** Use amortized stochastic variational inference. Algorithm 21.1 (Bernoulli likelihood, full-covariance Gaussian posterior):
1. Sample $x$ from the data and $\epsilon\sim q_0$.
2. Compute $(\mu,\log\sigma,L')=e_\phi(x)$.
3. Build $L=M\odot L'+\mathrm{diag}(\sigma)$ with $M=\mathrm{np.triu}(\mathrm{np.ones}(K),-1)$, then $z=L\epsilon+\mu$ (shapes implied by the sums: $\epsilon,\mu,z\in\mathbb R^K$, $L,L'\in\mathbb R^{K\times K}$, $p_\theta\in\mathbb R^D$).
4. Decode $p_\theta=d_\theta(z)$ and compute the three log-density terms for $q_\phi(z|x)$, $p_\theta(z)$, $p_\theta(x|z)$.
5. Combine them as $\mathcal L=\mathcal L_{\log px}+\mathcal L_{\log pz}-\mathcal L_{\log qz}$.
6. Take gradient steps $\theta:=\theta-\eta\nabla_\theta\mathcal L$ and $\phi:=\phi-\eta\nabla_\phi\mathcal L$ (p. 793).

**21.2.3 VAE vs autoencoder (p. 793–795).** An AE has no KL term, and its encoder is deterministic (only $\mathbb E[z|x]$). Murphy compares both on CelebA with the same convolutional architecture. Encoder channels are (32, 64, 128, 256, 512) and the latent has size 256. Training is 5 epochs, batch 256. The main advantage of the VAE: it is a proper generative model, so decoding $z\sim\mathcal N(0,I)$ gives sensible novel images (Fig. 21.2). An AE only decodes codes derived from the training set and does poorly on random inputs. Both reconstruct reasonably (Fig. 21.3), but VAE reconstructions are somewhat blurrier. Scaling down the KL by $\beta$ reduces blur (p. 794).

**21.2.4 The ELBO in augmented space (p. 794–796).** Definitions:
- $p_\theta(x,z)=p_\theta(z)p_\theta(x|z)$ \tag{21.9}, with marginal $p_\theta(x)=\int p_\theta(x,z)dz$ \tag{21.10} and posterior $p_\theta(z|x)=p_\theta(x,z)/p_\theta(x)$ \tag{21.11}.
- Joint inference distribution $q_{\mathcal D,\phi}(z,x)=p_{\mathcal D}(x)q_\phi(z|x)$ \tag{21.12}, with $p_{\mathcal D}(x)=\frac1N\sum_n\delta(x_n-x)$ \tag{21.13}.
- Aggregated posterior $q_{\mathcal D,\phi}(z)=\int q_{\mathcal D,\phi}(x,z)dx$ \tag{21.14}, and inference likelihood $q_{\mathcal D,\phi}(x|z)=q_{\mathcal D,\phi}(x,z)/q_{\mathcal D,\phi}(z)$ \tag{21.15}.

The data-averaged ELBO (following [ZSE19]):
$$\begin{aligned}\mathcal L(\theta,\phi|\mathcal D)&=\mathbb E_{p_{\mathcal D}(x)}\big[\mathbb E_{q_\phi(z|x)}[\log p_\theta(x|z)]\big]-\mathbb E_{p_{\mathcal D}(x)}[D_{KL}(q_\phi(z|x)\|p_\theta(z))] &&(21.16)\\&=\mathbb E_{q_{\mathcal D,\phi}(x,z)}[\log p_\theta(x|z)+\log p_\theta(z)-\log q_\phi(z|x)] &&(21.17)\\&=\mathbb E_{q_{\mathcal D,\phi}(x,z)}\Big[\log\frac{p_\theta(x,z)}{q_{\mathcal D,\phi}(x,z)}+\log p_{\mathcal D}(x)\Big] &&(21.18)\\&=-D_{KL}(q_{\mathcal D,\phi}(x,z)\|p_\theta(x,z))+\mathbb E_{p_{\mathcal D}(x)}[\log p_{\mathcal D}(x)] &&(21.19)\end{aligned}$$
(added step: 21.17→21.18 uses $q_{\mathcal D,\phi}(x,z)=p_{\mathcal D}(x)q_\phi(z|x)$.) With $\stackrel{c}{=}$ meaning equal up to additive constants:
$$\mathcal L\stackrel{c}{=}-D_{KL}(q_\phi(x,z)\|p_\theta(x,z)) \tag{21.20}$$
$$\stackrel{c}{=}-D_{KL}(p_{\mathcal D}(x)\|p_\theta(x))-\mathbb E_{p_{\mathcal D}(x)}[D_{KL}(q_\phi(z|x)\|p_\theta(z|x))] \tag{21.21}$$
$$\stackrel{c}{=}-D_{KL}(q_{\mathcal D,\phi}(z)\|p_\theta(z))-\mathbb E_{q_{\mathcal D,\phi}(z)}[D_{KL}(q_\phi(x|z)\|p_\theta(x|z))] \tag{21.22}$$
Maximizing the ELBO means minimizing two KL terms. The first is minimized by MLE and the second by fitting the true posterior. If the posterior family is limited, the two may conflict (p. 796). Figure 21.4 states that the ELBO objective upper-bounds $D_{KL}(p_{\mathcal D}\|p_\theta)$ (p. 797).

From (21.22), the VAE shrinks the gap between aggregated posterior and prior, and also the reconstruction KL. Since $x$ usually has much higher dimension than $z$, the latter term usually dominates. So under a conflict the VAE favors reconstruction over posterior inference, and the learned posterior may be a poor approximation of the true one (p. 796).

*Intuition note.* The ELBO is one number that can be read as "match the joint distributions". Maximum likelihood only asks the data marginal to match. The extra term asks the encoder to be a good posterior too. When these pull apart, the $x$-space (reconstruction) term usually dominates, because $x$ is typically higher-dimensional than $z$.

### 21.3 VAE generalizations
**21.3.1 β-VAE (p. 797–799).** VAEs often give blurry images, unlike models optimizing exact likelihood (pixelCNNs, flows). For a Gaussian decoder with fixed variance, $\log p_\theta(x|z)=-\frac1{2\sigma^2}\|x-d_\theta(z)\|_2^2+\text{const}$ \tag{21.23}. Let $e_\phi(x)=\mathbb E[q_\phi(z|x)]$ and $\mathcal X(z)=\{x:e_\phi(x)=z\}$. For a fixed inference network and squared loss, the optimal decoder is $d_\theta(z)=\mathbb E[x:x\in\mathcal X(z)]$. It predicts the average of all inputs mapped to $z$, hence the blur. Murphy lists fixes: a richer posterior, a richer generator, or a simpler one, namely reducing the KL penalty:
$$\mathcal L_\beta(\theta,\phi|x)=\underbrace{-\mathbb E_{q_\phi(z|x)}[\log p_\theta(x|z)]}_{\mathcal L_E}+\beta\underbrace{D_{KL}(q_\phi(z|x)\|p_\theta(z))}_{\mathcal L_R} \tag{21.24}$$
$\beta=1$ gives the standard VAE and $\beta=0$ the standard AE. Varying $\beta$ from 0 to infinity moves along the rate-distortion curve. With $\beta<1$ more bits about each input are stored, so reconstructions are less blurry. With $\beta>1$ the code is more compressed (p. 798).

*Disentanglement (21.3.1.1).* Intuitively, "disentangled" means each latent dimension is a different factor of variation. It is formalized by total correlation:
$$\mathrm{TC}(z)=\sum_k\mathbb H(z_k)-\mathbb H(z)=D_{KL}\Big(p(z)\,\Big\|\,\prod_kp_k(z_k)\Big) \tag{21.25}$$
TC is zero iff the components are mutually independent. Murphy reports that [AS18] prove $\beta>1$ decreases TC. He also reports that [Loc+18] prove nonlinear latent variable models are unidentifiable: any disentangled representation has an equivalent fully entangled one with the same likelihood. So adjusting $\beta$ alone is not sufficient; some inductive bias (encoder, decoder, prior, dataset or learning algorithm) is needed (p. 798).

*Information bottleneck (21.3.1.2).* The unsupervised IB objective, with input $x$, bottleneck $z$ and target $\tilde x$, is
$$\mathcal L_{UIB}=\beta\,\mathbb I(z;x)-\mathbb I(z;\tilde x)=\beta\mathbb E_{p(x,z)}\Big[\log\frac{p(x,z)}{p(x)p(z)}\Big]-\mathbb E_{p(z,\tilde x)}\Big[\log\frac{p(z,\tilde x)}{p(z)p(\tilde x)}\Big] \tag{21.26–21.27}$$
with $p(x,z)=p_{\mathcal D}(x)p(z|x)$ \tag{21.28} and $p(z,\tilde x)=\int p_{\mathcal D}(x)p(z|x)p(\tilde x|z)dx$ \tag{21.29}. Its variational upper bound (from Eq. 5.181) is
$$\mathcal L_{UVIB}=-\mathbb E_{q_{\mathcal D,\phi}(z,x)}[\log p_\theta(x|z)]+\beta\mathbb E_{p_{\mathcal D}(x)}[D_{KL}(q_\phi(z|x)\|p_\theta(z))] \tag{21.30}$$
This matches (21.24) averaged over $x$. So the β-VAE is an unsupervised IB (p. 798–799).

*Intuition note.* β is a price on information stored in $z$. A low price lets $z$ remember more, which sharpens reconstructions. A high price forces compression, and a compact code tends toward independent coordinates. This alone cannot recover the "true" factors.

**21.3.2 InfoVAE (p. 799–800).** To fix these problems to some degree (the tendency to ignore the latent code and to learn a poor posterior), use
$$\mathcal L(\theta,\phi|x)=-\lambda D_{KL}(q_\phi(z)\|p_\theta(z))-\mathbb E_{q_\phi(z)}[D_{KL}(q_\phi(x|z)\|p_\theta(x|z))]+\alpha\,\mathbb I_q(x;z) \tag{21.31}$$
with $\alpha\ge0$ and $\lambda\ge0$. $\alpha=0,\lambda=1$ recovers the ELBO (21.22). The MI term is intractable as written: $\mathbb I_q(x;z)=\mathbb E_{q_\phi(x,z)}[\log\frac{q_\phi(x,z)}{q_\phi(x)q_\phi(z)}]=-\mathbb E_{q_\phi(x,z)}[\log\frac{q_\phi(z)}{q_\phi(z|x)}]$ \tag{21.32}. Using $q_\phi(x|z)=p_{\mathcal D}(x)q_\phi(z|x)/q_\phi(z)$:
$$\mathcal L=\mathbb E_{q_\phi(x,z)}\Big[-\lambda\log\frac{q_\phi(z)}{p_\theta(z)}-\log\frac{q_\phi(x|z)}{p_\theta(x|z)}-\alpha\log\frac{q_\phi(z)}{q_\phi(z|x)}\Big] \tag{21.33}$$
$$=\mathbb E_{q_\phi(x,z)}\Big[\log p_\theta(x|z)-\log\frac{q_\phi(z)^{\lambda+\alpha-1}p_{\mathcal D}(x)}{p_\theta(z)^\lambda q_\phi(z|x)^{\alpha-1}}\Big] \tag{21.34}$$
$$=\mathbb E_{p_{\mathcal D}(x)}\big[\mathbb E_{q_\phi(z|x)}[\log p_\theta(x|z)]\big]-(1-\alpha)\mathbb E_{p_{\mathcal D}(x)}[D_{KL}(q_\phi(z|x)\|p_\theta(z))]-(\alpha+\lambda-1)D_{KL}(q_\phi(z)\|p_\theta(z))-\mathbb E_{p_{\mathcal D}(x)}[\log p_{\mathcal D}(x)] \tag{21.35}$$
The last term is constant. The first two terms can be optimized with the reparameterization trick. The third needs $q_\phi(z)=\int q_\phi(x,z)dx$, which is intractable but easy to sample (draw $x\sim p_{\mathcal D}$, $z\sim q_\phi(z|x)$). So $q_\phi(z)$ is an implicit probability model, as in a GAN.

**Theorem 1** (Prop. 2 of [ZSE19]). Let $\mathcal X,\mathcal Z$ be continuous, $\alpha<1$ (to bound the MI) and $\lambda>0$. For any fixed $\mathbb I_q(x;z)$, the approximate InfoVAE loss with any strict divergence $D(q_\phi(z),p_\theta(z))$ (meaning $D(q,p)=0$ iff $q=p$) is globally optimized if $p_\theta(x)=p_{\mathcal D}(x)$ and $q_\phi(z|x)=p_\theta(z|x)$ (p. 799).

*MMD VAE (21.3.2.1).* With $\alpha=1$: $\mathcal L\stackrel{c}{=}\mathbb E_{p_{\mathcal D}}[\mathbb E_{q_\phi(z|x)}\log p_\theta(x|z)]-\lambda D_{KL}(q_\phi(z)\|p_\theta(z))$ \tag{21.36}. The MMD VAE replaces this KL by the squared maximum mean discrepancy, which the theorem permits. Its advantage is tractability. With $\lambda=1$ and the sign swapped:
$$\mathcal L=\mathbb E_{p_{\mathcal D}}[\mathbb E_{q_\phi(z|x)}[-\log p_\theta(x|z)]]+\mathrm{MMD}(q_\phi(z),p_\theta(z)) \tag{21.37}$$
$$\mathrm{MMD}(p,q)=\mathbb E_{p(z),p(z')}[\mathcal K(z,z')]+\mathbb E_{q(z),q(z')}[\mathcal K(z,z')]-2\mathbb E_{p(z),q(z')}[\mathcal K(z,z')] \tag{21.38}$$
Here $\mathcal K$ is a kernel such as the RBF kernel $\exp(-\frac1{2\sigma^2}\|z-z'\|_2^2)$. In practice, take $z_n=e_\phi(x_n)$ for the $B$ minibatch samples and compare them to $B$ draws from $\mathcal N(0,I)$. With a fixed-variance Gaussian decoder, $-\log p_\theta(x|z)=\|x-d_\theta(z)\|_2^2$ \tag{21.39}, so the whole model is deterministic (p. 800).

*Other special cases (p. 800).* $\alpha=0,\lambda=1$ gives the original ELBO. For freely chosen $\lambda>0$ with $\alpha=1-\lambda$ one gets the β-VAE. $\alpha=\lambda=1$ with $D$ the Jensen–Shannon divergence (trainable with a binary discriminator) gives an adversarial autoencoder.

**21.3.3 Multimodal VAEs (p. 800–802).** For $M$ modalities, assume conditional independence given $z$: $p_\theta(x_1..x_M,z)=p(z)\prod_m p_\theta(x_m|z)$ \tag{21.40}, with fixed prior $p(z)$. Standard ELBO: $\mathbb E_{q_\phi(z|X)}[\sum_m\log p_\theta(x_m|z)]-D_{KL}(q_\phi(z|X)\|p(z))$ \tag{21.41}. Likelihoods may have different dynamic ranges, so weight them with $\lambda_m\ge0$ and use $\beta\ge0$ on the KL \tag{21.42}. For missing data, let $O_m=1$ if $x_m$ is observed and sum only over observed modalities:
$$\mathcal L=\mathbb E_{q_\phi(z|X)}\Big[\sum_{m:O_m=1}\lambda_m\log p_\theta(x_m|z)\Big]-\beta D_{KL}(q_\phi(z|X)\|p(z)) \tag{21.43}$$
The problem is computing $q_\phi(z|X)$ for every subset of modalities, since an inference network assumes all inputs. By conditional independence the exact posterior is
$$p(z|X)=\frac{p(z)p(x_1..x_M|z)}{p(x_1..x_M)}=\frac{p(z)}{p(x_1..x_M)}\prod_mp(x_m|z)=\frac{p(z)}{p(x_1..x_M)}\prod_m\frac{p(z|x_m)p(x_m)}{p(z)}\propto p(z)\prod_m\frac{p(z|x_m)}{p(z)}\approx p(z)\prod_m\tilde q(z|x_m) \tag{21.44–21.46}$$
This is a product of experts: one $\tilde q(z|x_m)$ per modality plus the prior. Any subset is handled by changing the product. For Gaussians, $p(z)=\mathcal N(z|\mu_0,\Lambda_0^{-1})$ and $\tilde q(z|x_m)=\mathcal N(z|\mu_m,\Lambda_m^{-1})$ (Eq. 2.154):
$$\prod_{m=0}^M\mathcal N(z|\mu_m,\Lambda_m^{-1})\propto\mathcal N(z|\mu,\Sigma),\quad\Sigma=\Big(\sum_m\Lambda_m\Big)^{-1},\ \mu=\Sigma\Big(\sum_m\Lambda_m\mu_m\Big) \tag{21.47}$$
Precisions add, and the mean is precision-weighted (Fig. 21.5b). For a linear Gaussian (factor analysis) model one can ensure $q(z|x_m)=p(z|x_m)$, and then this is the exact posterior [WN18]; in general it is an approximation. To train expert and joint networks, [WG18] optimize the ELBO of the full vector, all marginals, and a random set $\mathcal J$ of joint subsets:
$$\mathcal L(\theta,\phi|X)=\mathcal L(\theta,\phi|x_1..x_M)+\sum_{m=1}^M\mathcal L(\theta,\phi|x_m)+\sum_{j\in\mathcal J}\mathcal L(\theta,\phi|X_j) \tag{21.48}$$
This also covers semi-supervised settings with few aligned examples. It handles only a fixed number of missingness patterns; arbitrary missingness is treated in [CNW20] (p. 802).

*Intuition note.* Each modality gives a Gaussian "vote" about $z$. More certain votes (higher precision) count more, and a missing modality simply casts no vote.

**21.3.4 Semi-supervised VAEs, M2 model (p. 803).** Data: labeled $\mathcal D_L=\{(x_n,y_n)\}$ and unlabeled $\mathcal D_U=\{x_n\}$. Generative model: $p_\theta(x,y)=p_\theta(y)\int p_\theta(x|y,z)p_\theta(z)dz$ \tag{21.49}, with $p_\theta(z)=\mathcal N(0,I)$, $p_\theta(y)=\mathrm{Cat}(y|\pi)$, and $p_\theta(x|y,z)=p(x|f_\theta(y,z))$. The innovation is a latent class $y$ plus a continuous $z$. Labeled data use $q_\phi(z|y,x)=\mathcal N(z|\mu_\phi(y,x),\mathrm{diag}(\sigma_\phi(y,x)))$ \tag{21.50} and the bound
$$\log p_\theta(x,y)\ge\mathbb E_{q_\phi(z|x,y)}[\log p_\theta(x|y,z)+\log p_\theta(y)+\log p_\theta(z)-\log q_\phi(z|x,y)]=-\mathcal L(x,y) \tag{21.51}$$
Unlabeled data use $q_\phi(z,y|x)=q_\phi(z|x)q_\phi(y|x)$ with Gaussian $q_\phi(z|x)$ and $q_\phi(y|x)=\mathrm{Cat}(y|\pi_\phi(x))$ \tag{21.52–21.54}, a classifier that imputes labels, and
$$\log p_\theta(x)\ge\mathbb E_{q_\phi(z,y|x)}[\log p_\theta(x|y,z)+\log p_\theta(y)+\log p_\theta(z)-\log q_\phi(z,y|x)]=-\sum_yq_\phi(y|x)\mathcal L(x,y)+\mathbb H(q_\phi(y|x))=-\mathcal U(x) \tag{21.55–21.56}$$
Since $q_\phi(y|x)$ is then used only for unlabeled data, add a classification loss on labeled data:
$$\mathcal L(\theta)=\mathbb E_{\mathcal D_L}[\mathcal L(x,y)]+\mathbb E_{\mathcal D_U}[\mathcal U(x)]+\alpha\,\mathbb E_{\mathcal D_L}[-\log q_\phi(y|x)] \tag{21.57}$$
$\alpha$ weights generative against discriminative learning (p. 803).

**21.3.5 Sequential encoders/decoders (p. 804–806).** Data $x$ is a variable-length sequence and $z\in\mathbb R^K$ is fixed-size; only $p(x|z)$ and $q(z|x)$ are changed. *Models:* VAE-RNN [Bow+16a]: $p(z,x_{1:T})=p(z)\mathrm{RNN}(x_{1:T}|z)$, with $z$ given as the initial state or as input at each step. The encoder is $q(z|x_{1:T})=\mathcal N(z|\mu(h),\Sigma(h))$ with $h=[h_T^\to,h_1^\leftarrow]$ from a bidirectional RNN (Fig. 21.6). Optimus [Li+20]: a BERT encoder (using a dummy "class" token's embedding) and an autoregressive GPT-like decoder. The latent is injected either by $h_i'=h_i+Wz$ with $W\in\mathbb R^{H\times K}$, or, with better results in their experiments, by a memory vector $h_m=Wz$, $W\in\mathbb R^{LH\times K}$, $h_m\in\mathbb R^{L\times H}$, appended to the embeddings at each layer. Transformer VAE [Gre20]: a funnel-transformer encoder, a T5 decoder, and an MMD VAE to avoid posterior collapse.

*Applications.*
- **Text** [Bow+16b]: perplexity does not improve, but the latent space supports interpolation giving grammatical, related intermediate sentences (Fig. 21.7a). A deterministic AE with the same networks gives much less meaningful interpolations (Fig. 21.7b), because it has "holes" in latent space. Powerful decoders risk posterior collapse; KL annealing is common, and InfoVAE-type methods are said to be more effective (p. 805).
- **Sketches** (sketch-rnn [HE18]): the emission model is a GMM for pen offsets plus a softmax for pen state. A temperature $\tau$ multiplies GMM variances and divides discrete probabilities before renormalizing. At low temperature the model reconstructs closely, while untypical inputs (a three-eyed cat) are "regularized" toward a canonical cat (Fig. 21.8, p. 806).
- **Molecules** [GB+18]: VAE-RNN on SMILES strings, plus a map from latent space to a property such as solubility. Gradient-based optimization in latent space seeks better molecules (Fig. 21.9). The main problem is making latent points decode to valid molecules; a grammar VAE (stochastic context-free grammar decoder) is one solution (p. 806).

### 21.4 Avoiding posterior collapse (p. 806–809)
If the decoder is powerful, the VAE need not use $z$: this is **posterior collapse** or variational overpruning. Argument via (21.21): suppose some $\theta^*$ gives $p_{\theta^*}(x|z)=p_{\mathcal D}(x)$ for every $z$. Then $D_{KL}(p_{\mathcal D}\|p_\theta)=0$. The generator ignores $z$, so $p_\theta(z|x)=p_\theta(z)$. Setting $q_\phi(z|x)=p_\theta(z)$ makes the second KL zero. The ELBO is then maximized yet no useful latent representation is learned (p. 807). Footnote 5 reports that collapse also occurs in linear VAEs, where the ELBO equals the exact marginal likelihood, so it also relates to spurious local maxima.

- **KL annealing** [Bow+16a]: scale the KL by $\beta$, raised from 0 (AE) to 1 (standard training). This contrasts with β-VAE's $\beta>1$. It needs a schedule; cyclical annealing repeats the ramp and warm-starts each cycle (p. 807).
- **Lower bounding the rate** (p. 808): keep the plain ELBO but limit $q$. Examples: a von Mises–Fisher prior and posterior with fixed concentration $\kappa$, which controls the rate; or the δ-VAE, with a Gaussian autoregressive prior and diagonal Gaussian posterior, where the rate is at least $\delta$ by adjusting the AR regression parameter.
- **Free bits** [Kin+16]: replace $\mathcal L_R=\sum_iD_{KL}(q_\phi(z_i|x)\|p_\theta(z_i))$ \tag{21.58} by the hinge version $\mathcal L_R'=\sum_i\max(\lambda,D_{KL}(q_\phi(z_i|x)\|p_\theta(z_i)))$ \tag{21.59}. Dimensions already below rate $\lambda$ are "free" (p. 808).
- **Skip connections** (skip-VAE [Die+19a]): connect $z$ more directly to $x$ (Fig. 21.10).
- **Improved inference** [He+19]: update the inference network more aggressively before each generator step. This addresses only the amortization-gap part of collapse, not variational pruning. Tighter bounds, better posteriors or hierarchical models may help the latter (p. 808).
- **Alternative objectives:** InfoVAE, which includes an explicit MI term. Murphy says this effectively solves the problem (p. 809).

### 21.5 Hierarchical VAEs (p. 809–814)
HVAE with $L$ stochastic layers (top layer $z_L$, "more abstract"):
$$p_\theta(x,z_{1:L})=p_\theta(z_L)\Big[\prod_{l=L-1}^1p_\theta(z_l|z_{l+1})\Big]p_\theta(x|z_1) \tag{21.60}$$
A non-Markovian version lets each layer depend on all higher ones: $p_\theta(x,z)=p_\theta(z_L)[\prod_{l=L-1}^1p_\theta(z_l|z_{l+1:L})]p_\theta(x|z_{1:L})$ \tag{21.61}. It is implemented with a deterministic residual "backbone" that accumulates stochastic decisions (Fig. 21.11 left) (p. 809).

**21.5.1 Bottom-up vs top-down inference (p. 810–811).** Bottom-up: $q_\phi(z|x)=q_\phi(z_1|x)\prod_{l=2}^Lq_\phi(z_l|x,z_{1:l-1})$ \tag{21.62}. Murphy calls the following better: top-down, $q_\phi(z|x)=q_\phi(z_L|x)\prod_{l=L-1}^1q_\phi(z_l|x,z_{l+1:L})$ \tag{21.63}. Chain rule for KL gives the ELBO:
$$\mathcal L=\mathbb E_{q_\phi(z|x)}[\log p_\theta(x|z)]-D_{KL}(q_\phi(z_L|x)\|p_\theta(z_L))-\sum_{l=L-1}^1\mathbb E_{q_\phi(z_{>l}|x)}[D_{KL}(q_\phi(z_l|x,z_{>l})\|p_\theta(z_l|z_{>l}))] \tag{21.64–21.65}$$
with $q_\phi(z_{>l}|x)=\prod_{i=l+1}^Lq_\phi(z_i|x,z_{>i})$ \tag{21.66}. Top-down is better because it is closer to the true layer posterior $p_\theta(z_l|x,z_{l+1:L})\propto p_\theta(z_l|z_{l+1:L})p_\theta(x|z_l,z_{l+1:L})$ \tag{21.67}, a top-down prior times a bottom-up likelihood. Approximate it by $q_\phi(z_l|x,z_{l+1:L})\propto p_\theta(z_l|z_{l+1:L})\tilde q_\phi(z_l|x,z_{l+1:L})$ \tag{21.68}, with $\tilde q_\phi$ a learned Gaussian approximation to the likelihood. This product is closed-form when both factors are Gaussian (ladder network). A more flexible option shares parameters between posterior and learned prior [Kin+16], reducing parameters and keeping the two somewhat close (p. 811).

**21.5.2 Very deep VAE (VD-VAE) [Chi21a] (p. 811–812).** A simple convolutional VAE with bidirectional inference (Fig. 21.12) and diagonal Gaussian prior and posterior per layer. Nearest-neighbor upsampling in the decoder worked much better than transposed convolution and avoided posterior collapse, so the vanilla objective sufficed. Low-resolution top latents capture global structure; high-resolution latents fill in details. Murphy suggests this could suit lossy compression, since low-level details could be drawn from the prior. Fig. 21.13 shows multi-resolution samples from a 78-layer model on FFHQ-256.

**21.5.3 Link to autoregressive (AR) models (p. 812–813).** Deep HVAEs can outperform AR models in likelihood and sample quality with fewer parameters and less compute [Chi21a; VK20a; Maa+19]. Any AR model is a degenerate VAE (Fig. 21.14 left). The encoder copies $z_{1:D}=x_{1:D}$, the prior is autoregressive $p_\theta(z_{1:D})=\prod_dp(z_d|z_{1:d-1})$, and the decoder copies $z$ to $x$. The encoder computes the exact posterior, $q_\phi(z|x)=p_\theta(z|x)$, so the ELBO is tight:
$$\log p_\theta(x)=\log p_\theta(z)=\sum_d\log p_\theta(x_d|x_{<d}) \tag{21.69}$$
So an HVAE with at least $D$ stochastic layers emulates any AR model. Since data usually lies on a lower-dimensional manifold, a compact hierarchical code is possible. In a tree-like code, lower-level latents are conditionally independent given higher ones and can be generated in parallel, in $O(\log D)$ time against $O(D)$ for AR (Fig. 21.14 right). Hierarchical models also need fewer parameters. Typical multi-scale architectures start from a small spatial latent grid and raise resolution (usually ×2) at each layer, so high layers capture global correlations and low layers fine detail.

**21.5.4 Variational pruning (p. 814).** Higher latent layers are often ignored. A heuristic is KL balancing, $\sum_{l=1}^L\gamma_l\mathbb E_{q_\phi(z_{>l}|x)}[D_{KL}(q_\phi(z_l|x,z_{>l})\|p_\theta(z_l|z_{>l}))]$ \tag{21.70}. During warm-up, $\gamma_l$ is small when a layer's KL is small (to encourage its use) and large when it is large. [VK20a] set $\gamma_l\propto s_l\,\mathbb E_{x\sim\mathcal B}[\mathbb E_{q_\phi(z_{>l}|x)}D_{KL}(\cdot)]$ \tag{21.71}, where $s_l$ is the layer size and $\mathcal B$ the minibatch.

**21.5.5 Optimization difficulties (p. 814).** The loss can be unstable because the KL is unbounded. VD-VAE [Chi21a]: scale the initial weights of the final convolution in each residual bottleneck block by $1/\sqrt L$, and skip an update when the gradient norm exceeds a threshold. NVAE [VK20a]: tweaked batch normalization; spectral regularization $\beta\sum_i\lambda_i$ ($\lambda_i$ the largest singular value of conv layer $i$, from one power-iteration step); inverse autoregressive flows per layer; and a residual posterior. With prior $p_\theta(z_l^i|z_{>l})=\mathcal N(\mu_i(z_{>l}),\sigma_i(z_{>l}))$ \tag{21.72}, the posterior is
$$q_\phi(z_l^i|x,z_{>l})=\mathcal N\big(\mu_i(z_{>l})+\Delta\mu_i(z_{>l},x),\ \sigma_i(z_{>l})\cdot\Delta\sigma_i(z_{>l},x)\big) \tag{21.73}$$
$$D_{KL}=\frac12\Big(\frac{\Delta\mu_i^2}{\sigma_i^2}+\Delta\sigma_i^2-\log\Delta\sigma_i^2-1\Big) \tag{21.74}$$
As long as $\sigma_i$ is bounded below, the KL can be controlled just by adjusting the encoder parameters.

### 21.6 Vector-quantized VAE (p. 815–819)
**21.6.1 Binary code (p. 815).** Add a discretization layer to the encoder, $z_e(x)\in\{0..S-1\}^K$ (e.g. $S=2$). With a uniform prior and a deterministic encoder, the KL is a constant, stated as $\log K$. This avoids posterior collapse. Quantization blocks gradients, so use the straight-through estimator [OVK17]. With a Gaussian likelihood, $\mathcal L=\|x-d(e(x))\|_2^2$ \tag{21.75}, with $e(x)\in\{0,1\}^K$, $d(z)\in\mathbb R^{28\times28}$ (Fig. 21.15: MNIST, 256 binary latents).

**21.6.2 VQ-VAE (p. 815–817).** Use a tensor of discrete latents $z\in\mathbb R^{H\times W\times K}$ (as printed) and a codebook $\{e_k\in\mathbb R^D\}_{k=1}^K$. Each encoder vector is assigned its nearest codebook entry:
$$q(z_{ij}=k|x)=\begin{cases}1&k=\arg\min_{k'}\|z_e(x)_{i,j,:}-e_{k'}\|_2\\0&\text{otherwise}\end{cases} \tag{21.76}$$
The decoder receives $(z_q)_{ij}=e_k$ where $z_{ij}=k$ \tag{21.77}. Example: a $32\times32$ grid with $K=512$ gives $512^{32\times32}=2^{9216}$ distinct images. The straight-through estimator passes gradients from decoder input $z_q$ to encoder output $z_e$, but then the codebook gets no learning signal. So add a codebook loss with stop-gradient $\mathrm{sg}$ (identity forward, zero gradient backward):
$$\mathcal L=-\log p(x|z_q(x))+\|\mathrm{sg}(z_e(x))-e\|_2^2 \tag{21.78}$$
Alternatively update codewords by moving averages. In batch form, with $n_i$ encoder outputs $z_{i,j}$ nearest to $e_i$, minimize $\sum_{j=1}^{n_i}\|z_{i,j}-e_i\|_2^2$ \tag{21.79}, giving $e_i=\frac1{n_i}\sum_jz_{i,j}$ \tag{21.80}. Murphy compares this to the M step for GMM means. For minibatches, with $\gamma$ (found to work well at 0.9):
$$N_i^t=\gamma N_i^{t-1}+(1-\gamma)n_i^t,\quad m_i^t=\gamma m_i^{t-1}+(1-\gamma)\sum_jz^t_{i,j},\quad e_i^t=\frac{m_i^t}{N_i^t} \tag{21.81–21.83}$$
A **commitment loss** stops the encoder from "changing its mind" too often:
$$\mathcal L=-\log p(x|z_q(x))+\|\mathrm{sg}(z_e(x))-e\|_2^2+\beta\|z_e(x)-\mathrm{sg}(e)\|_2^2 \tag{21.84}$$
$\beta=0.25$ was found to work well, though it depends on the scale of the NLL. The decoder optimizes only the first term, the encoder the first and last, and the embeddings the middle one.

*Intuition note.* Two stop-gradients split one distance into two jobs: codewords chase encoder outputs, and encoder outputs stay near their codewords. With straight-through gradients alone, the codebook gets no learning signal; the codebook term (or a moving-average update) provides one.

**21.6.3 Learning the prior (p. 817).** After training, encode the data into discrete sequences $\{z_n\}$ and fit any sequence model $p(z)$ (PixelCNN originally, transformers later). Decode samples with the VQ-VAE decoder.

**21.6.4 VQ-VAE-2 (p. 817–818).** Hierarchical codes for $256\times256\times3$ images: a first latent layer quantized to $64\times64$, a second to $32\times32$. The top level handles high-level semantics, the lower level texture. The top prior is PixelCNN with self-attention (PixelSNAIL); the lower prior is plain PixelCNN, because attention would be too expensive (Fig. 21.17).

**21.6.5 Discrete VAE (p. 818–819).** VQ-VAE's one-hot encoding captures no uncertainty in the code and needs straight-through training. DALL-E uses the Gumbel-softmax relaxation. An exact sample is $w_k=\arg\max_k g_k+\log q(z=k|x)$ with Gumbel $g_k$. The relaxation with temperature $\tau>0$ is
$$w_k=\frac{\exp\big(\frac{g_k+\log q(z=k|x)}{\tau}\big)}{\sum_{j=1}^K\exp\big(\frac{g_j+\log q(z=j|x)}{\tau}\big)},\qquad z_q=\sum_{k=1}^Kw_ke_k \tag{21.85–21.86}$$
As $\tau\to0$, $w$ becomes one-hot. For finite $\tau$ the space between codewords is "filled in". The ELBO is then differentiable: $\mathcal L=-\mathbb E_{q(z|x)}[\log p(x|z)]+\beta D_{KL}(q(z|x)\|p(z))$ \tag{21.87}. Here the KL is not constant because the encoder is stochastic. The Gumbel noise is independent of the encoder parameters, so the reparameterization trick applies.

**21.6.6 VQ-GAN (p. 819).** VQ-VAE's MSE reconstruction loss can give blur. VQ-GAN [ERO21] uses a patch-wise GAN loss plus a perceptual loss, and a transformer prior on the codes (Fig. 21.18). VIM [Yu+21] replaces the CNN encoder and decoder with transformers, with improved results.

## Toy example (ours, not from the text)
Use (21.74) in 1-D. Prior $p_\theta(z)=\mathcal N(\mu=0,\sigma=1)$. The encoder outputs the relative changes $\Delta\mu=1$, $\Delta\sigma=0.5$, so $q=\mathcal N(1,0.5)$. KL $=\frac12\big(\frac{1^2}{1^2}+0.5^2-\log 0.5^2-1\big)=\frac12(1+0.25+1.3863-1)=\frac12(1.6363)=0.8181$.
Assume (invented number) the expected reconstruction NLL is $\mathcal L_E=2.0$. Then, by (21.24), $\mathcal L_\beta=\mathcal L_E+\beta\cdot0.8181$:
- $\beta=0$ (AE-like): $2.0$
- $\beta=0.5$: $2.0+0.4091=2.4091$
- $\beta=1$ (VAE): $2.0+0.8181=2.8181$

Collapse case: $\Delta\mu=0$, $\Delta\sigma=1$ gives KL $=\frac12(0+1-0-1)=0$. The posterior equals the prior and the code carries no information about $x$, which is the collapse situation of Section 21.4. Larger $\beta$ penalizes the informative posterior more, pushing toward this case. In reality $\mathcal L_E$ would rise as $\beta$ grows; it is held fixed here only to show the arithmetic.

## Concepts
- [[variational-inference-elbo]] — the VAE objective: expected log-likelihood minus a KL to the prior; data-averaged forms in (21.16–21.22) (p. 796)
- [[kl-divergence]] — divergence between distributions; appears as rate term, and the ELBO equals a negative joint KL up to constants (p. 796)
- [[amortized-inference]] (new) — one network $q_\phi(z|x)$ gives the approximate posterior for any $x$ (p. 791)
- [[variational-autoencoder]] (new) — decoder $p_\theta(x|z)$ plus encoder $q_\phi(z|x)$ trained jointly on the ELBO (p. 791)
- [[aggregated-posterior]] (new) — $q_{\mathcal D,\phi}(z)=\int q_{\mathcal D,\phi}(x,z)dx$ (p. 796)
- [[beta-vae]] (new) — ELBO with the KL scaled by $\beta$; $\beta<1$ less blur, $\beta>1$ more compression (p. 797–798)
- [[total-correlation-disentanglement]] (new) — TC measures dependence among latent coordinates; $\beta>1$ lowers it, but this does not give identifiability (p. 798)
- [[information-bottleneck]] (new) — trade $\mathbb I(z;x)$ against $\mathbb I(z;\tilde x)$; the β-VAE is its unsupervised variational form (p. 798)
- [[rate-distortion-tradeoff]] (new) — KL term as rate, reconstruction error as distortion (p. 798)
- [[infovae]] (new) — objective with $\lambda$ and $\alpha$ weights; includes MMD VAE and adversarial AE (p. 799–800)
- [[maximum-mean-discrepancy]] (new) — kernel-based distance between two sample sets (p. 800)
- [[product-of-experts-posterior]] (new) — posterior $\propto$ prior × per-modality experts; Gaussian precisions add (p. 802)
- [[posterior-collapse]] (new) — the latent code is ignored while the ELBO is maximized (p. 806)
- [[kl-annealing-free-bits]] (new) — scheduling β, or hinge-flooring each KL dimension, to keep the latents used (p. 807–808)
- [[top-down-inference]] (new) — hierarchical posterior $q(z_l|x,z_{>l})$ combining prior and bottom-up likelihood (p. 810–811)
- [[hierarchical-model]] — stacked latent layers; HVAE (p. 809)
- [[vq-vae]] (new) — discrete latents from a nearest-neighbor codebook; codebook and commitment losses (p. 815–817)
- [[straight-through-estimator]] (new) — copy decoder-input gradients to the encoder output, bypassing quantization (p. 815)
- [[gumbel-softmax-relaxation]] (new) — temperature softmax over Gumbel-perturbed logits as a differentiable discrete sample (p. 818)

## Canonical instances
- [[celeba-vae-vs-ae]] — VAE samples are sensible, AE samples poor; VAE reconstructions blurrier (p. 794)
- [[vae-rnn-text-interpolation]] — VAE gives grammatical intermediate sentences, AE does not (p. 805)
- [[sketch-rnn]] — temperature-controlled sketch generation and reconstruction (p. 806)
- [[molecule-design-vae]] — latent-space gradient ascent on a property of SMILES-encoded molecules (p. 806)
- [[vd-vae]] — very deep hierarchical VAE with 78 stochastic layers (p. 811–812)
- [[ar-as-degenerate-vae]] — an AR model written as a VAE with identity encoder and decoder (p. 813)
- [[mnist-binary-autoencoder]] — 256 binary latents (p. 815)
- [[vq-vae-2]] and [[vq-gan]] — hierarchical and GAN-loss versions of VQ-VAE (p. 817–819)

## Bridges (candidates)
- [same-math] Gaussian product of experts (21.47) ↔ Bayesian conjugate updating: precisions add and means are precision-weighted, as when combining a Gaussian prior with Gaussian evidence.
- [structural-analogy] Amortized inference network ↔ rational analysis: a learned procedure approximately inverts the generative model of the environment.
- [structural-analogy] Hierarchical VAE layers ↔ hierarchical (multilevel) models: each layer's distribution is conditioned on a more abstract layer.
- [structural-analogy] VQ codebook moving-average update (21.80–21.83) ↔ EM M-step for GMM means: means are re-estimated from assigned points. The assignment is hard here.
- [structural-analogy] Posterior collapse ↔ prior-dominated posterior: when the data term carries no information, the posterior equals the prior.
- [metaphor] KL annealing ↔ tempering/annealing in sampling: gradually increasing a weight to ease optimization.

## Questions this raises
- When the posterior family is limited, how can we tell whether a VAE's reconstruction gain comes at the cost of a useless posterior (21.22)?
- Does an InfoVAE or MMD objective keep the "proper generative model" property in practice, given that the theorem holds only for strict divergences and global optima?
- Which data support the claim that hierarchical VAEs can match AR likelihoods with fewer parameters (21.5.3), and what is the cost in sampling quality?
- How do commitment and codebook losses relate to a proper probabilistic objective (the text points to [Hen+18])?

## Reading notes
- Printed page = pdf − 34 (pdf 825 = printed 791). The last page (pdf 854, printed 820) has no text and no image content in the material provided.
- No exercises are given in this unit.
- Algorithm 21.1 as printed: line 11 ($\mathcal L_{\log pz}$) and line 12 ($\mathcal L_{\log px}$) have a leading minus sign, line 12 gives a negative log-likelihood, and line 13 is $\mathcal L_{\log px}+\mathcal L_{\log pz}-\mathcal L_{\log qz}$. The signs look mutually inconsistent for a loss minimized by gradient descent (lines 14–15). I did not correct this.
- Eq. (21.48) has a stray "()" in $\mathcal L(\theta,\phi|()x_1,\dots,x_M)$.
- Sect. 21.6.1 states the constant KL as $\log K$. For $K$ binary latents with a uniform prior over $\{0,1\}^K$ I would expect $K\log 2$. I report the text as printed.
- The text says $D$ is the number of pixels but gives $D=3072$ for $32\times32$. This count includes three colour channels.
- Footnote 2 (p. 792–793) continues across pages; footnote 9 has the typo "resoution". Figure 21.4's caption says $p_{\mathcal D}(x)$ is denoted $q_{\mathcal D}(x)$ in the figure.
- Many cross-references (Sections 10.x, 5.x, 22.x, 26.x) point to chapters not in this unit; I only report what these pages say about them.
