---
id: prince-2023-udl/ch15-generative
work: prince-2023-udl
unit: "Chapter 15 — Generative adversarial networks"
pages: 276-303
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Generative adversarial networks

## L0 — One line
A GAN trains a generator to turn noise into samples by using a discriminator's ability to tell real from fake as the learning signal. Training is difficult: the discriminator can become too good, and the learning can be unstable.

## L1 — The gist (≤ 120 words)
How can we generate new data that looks like a training set without writing down its probability distribution? A GAN pairs a generator (noise → sample) with a discriminator (real or generated?). If training goes as planned, the generator is updated until the discriminator is at chance. With the original loss, the optimal discriminator turns the loss into (up to constants) a Jensen–Shannon distance. That distance gives almost no gradient when real and generated distributions barely overlap. The Wasserstein distance is a better-behaved alternative. Further tricks (progressive growing, minibatch discrimination, truncation), conditioning (conditional GAN, ACGAN, InfoGAN), image translation (Pix2Pix, SRGAN, CycleGAN) and StyleGAN extend the idea. GANs give samples, not probabilities.

**Prerequisites:** binary cross-entropy and sigmoid; expectations as integrals; KL divergence; convolutional nets and U-Nets; the idea of a constrained minimisation (linear programming).

## L2 — Key ideas
- A GAN is a sampler only. It builds no probability distribution, so it cannot score how likely a new point is (p. 276).
- Training is a minimax game (two players, one shared loss): the discriminator minimises a binary cross-entropy loss and the generator maximises it. If training goes as planned, at convergence the generated samples follow the data distribution and the discriminator outputs 0.5 (p. 278).
- With an optimal discriminator, the loss is, up to constants, the Jensen–Shannon divergence (a distance between two distributions). Its two terms enforce quality (no samples where there are no real data) and coverage (no real data left without samples). The generator does not depend on the coverage term, which is the putative reason for mode dropping (the generator covers only part of the data) (pp. 282–283).
- If the two distributions are disjoint, the distance is maximal and flat. Gradients vanish when the discriminator is too good (pp. 283–284).
- The Wasserstein (earth mover's) distance, the work needed to move probability mass from one distribution to create the other, is defined even for disjoint distributions and shrinks smoothly. The WGAN discriminator must have gradient norm below one (pp. 284–286).
- Further tricks improve output: progressive growing, minibatch discrimination, truncation (quality vs. diversity) (pp. 287–289).
- Conditioning gives control: conditional GAN, ACGAN, InfoGAN (pp. 289–291). Image translation uses the discriminator as a realism loss: Pix2Pix, SRGAN, CycleGAN (pp. 291–296).
- StyleGAN injects noise and style at several scales, separating style from noise (pp. 296–298).

## L3 — Walkthrough

### Introduction (p. 276)
- A GAN is an unsupervised model that generates samples indistinguishable from training examples. It does not model a probability distribution, so it cannot evaluate whether a new point belongs to the distribution (p. 276).
- The generator maps random noise to data space. A discriminator tries to tell generated from real. If it fails, the samples are "plausible"; if it succeeds, its output is a training signal (p. 276).
- Training is hard: it can be unstable, and learning realistic samples does not imply learning all possible samples (p. 276). Most success is on images, so the chapter focuses on them (p. 276).

### 15.1 Discrimination as a signal (pp. 276–277)
- A sample is made by drawing a latent variable $\mathbf z_j$ from a simple base distribution (e.g. a standard normal) and computing $\mathbf x^*_j=\mathbf g[\mathbf z_j,\boldsymbol\theta]$ (the generator). A discriminator $f[\bullet,\boldsymbol\phi]$ classifies input as real or generated (p. 276).
- **1D example (Figure 15.1).** The generator is
$$x^*_j=g[z_j,\theta]=z_j+\theta,\tag{15.1}$$
 with $z_j$ standard normal, so $\theta$ shifts samples along the axis. At initialisation $\theta=3.0$ and the samples lie left of the real data. Figure 15.1 shows $\theta=3.0,\,4.9,\,6.7$. The generator is trained to raise the probability that its samples are called real, so $\theta$ increases (p. 277).
- Updates alternate between discriminator and generator. As classification gets harder, the sigmoid flattens and the push on $\theta$ weakens. At the end the discriminator is at chance and is discarded, leaving the generator (p. 277).

*Intuition note.* The discriminator is a learned critic. Its slope tells the generator which way to move. When the critic cannot tell the two apart, the slope is flat and the push to change the generator fades.

#### 15.1.1 GAN loss function (p. 278)
- The discriminator returns a scalar that is higher when it believes the input is real. Binary cross-entropy (section 5.4) is
$$\hat{\boldsymbol\phi}=\operatorname*{argmin}_{\boldsymbol\phi}\Big[\sum_i-(1-y_i)\log\big[1-\mathrm{sig}[f[\mathbf x_i,\boldsymbol\phi]]\big]-y_i\log\big[\mathrm{sig}[f[\mathbf x_i,\boldsymbol\phi]]\big]\Big]\tag{15.2}$$
 with $y_i\in\{0,1\}$ and sig the logistic sigmoid.
- Real examples get $y=1$ and generated samples $y=0$ ($i$ indexes real, $j$ generated):
$$\hat{\boldsymbol\phi}=\operatorname*{argmin}_{\boldsymbol\phi}\Big[\sum_j-\log\big[1-\mathrm{sig}[f[\mathbf x^*_j,\boldsymbol\phi]]\big]-\sum_i\log\big[\mathrm{sig}[f[\mathbf x_i,\boldsymbol\phi]]\big]\Big]\tag{15.3}$$
- Substituting $\mathbf x^*_j=\mathbf g[\mathbf z_j,\boldsymbol\theta]$, the generator must *maximise* over $\boldsymbol\theta$, since we want generated samples to be misclassified:
$$\hat{\boldsymbol\theta}=\operatorname*{argmax}_{\boldsymbol\theta}\Big[\min_{\boldsymbol\phi}\Big[\sum_j-\log\big[1-\mathrm{sig}[f[\mathbf g[\mathbf z_j,\boldsymbol\theta],\boldsymbol\phi]]\big]-\sum_i\log\big[\mathrm{sig}[f[\mathbf x_i,\boldsymbol\phi]]\big]\Big]\Big]\tag{15.4}$$

#### 15.1.2 Training GANs (pp. 278–279)
- $\boldsymbol\phi$ minimises and $\boldsymbol\theta$ maximises the loss: a *minimax game*. The solution is technically a Nash equilibrium, a point that is simultaneously a minimum of one function and a maximum of the other. If training goes as planned, then at convergence $\mathbf g[\mathbf z,\boldsymbol\theta]$ is drawn from the data distribution and $\mathrm{sig}[f]$ is 0.5 (p. 278).
- Equation 15.4 is split into two losses:
$$L[\boldsymbol\phi]=\sum_j-\log\big[1-\mathrm{sig}[f[\mathbf g[\mathbf z_j,\boldsymbol\theta],\boldsymbol\phi]]\big]-\sum_i\log\big[\mathrm{sig}[f[\mathbf x_i,\boldsymbol\phi]]\big],\qquad L[\boldsymbol\theta]=\sum_j\log\big[1-\mathrm{sig}[f[\mathbf g[\mathbf z_j,\boldsymbol\theta],\boldsymbol\phi]]\big]\tag{15.5}$$
 The second was multiplied by $-1$ to turn maximisation into minimisation, and the term without $\boldsymbol\theta$ was dropped (p. 279).
- Each step: draw a batch of $\mathbf z_j$, generate $\mathbf x^*_j$, pick a batch of real $\mathbf x_i$, then take one or more gradient steps on each loss (Figure 15.2) (p. 279).

#### 15.1.3 Deep convolutional GAN (pp. 279–280)
- DCGAN (an early image GAN): a 100D latent $\mathbf z$ from a *uniform* distribution is mapped linearly to a 4×4 representation with 1024 channels. Four fractionally-strided convolutions (stride 0.5) each double the resolution. A final tanh gives a 64×64×3 image in $[-1,1]$ (p. 280).
- The discriminator is a standard convolutional net whose last convolution gives 1×1 with one channel, passed through a sigmoid. After training the discriminator is discarded (p. 280). Results are in Figure 15.4 (p. 281).

#### 15.1.4 Difficulty training GANs (pp. 280–281)
- GANs are "notoriously difficult" to train. DCGAN needed: (i) strided convolutions for up/down-sampling; (ii) BatchNorm in both networks except the generator's last and discriminator's first layer; (iii) leaky ReLU in the discriminator; (iv) Adam with a lower momentum coefficient than usual. The author calls this unusual, since most deep learning models are relatively robust to such choices (p. 280).
- **Mode dropping:** the generator makes plausible samples covering only a subset of the data (e.g. for faces, it might never generate faces with beards). **Mode collapse** is the extreme version: the generator mostly ignores $\mathbf z$ and collapses to one or a few points (Figure 15.5, an MLP generator on LSUN) (p. 281).

### 15.2 Improving stability (pp. 281–286)

#### 15.2.1 Analysis of GAN loss function (pp. 282–283)
- Dividing the sums by the counts $I,J$ gives expectations:
$$L[\boldsymbol\phi]=-\frac1J\sum_{j=1}^J\log\big[1-\mathrm{sig}[f[\mathbf x^*_j,\boldsymbol\phi]]\big]-\frac1I\sum_{i=1}^I\log\big[\mathrm{sig}[f[\mathbf x_i,\boldsymbol\phi]]\big]\tag{15.6}$$
$$\approx-\mathbb E_{\mathbf x^*}\big[\log[1-\mathrm{sig}[f[\mathbf x^*,\boldsymbol\phi]]]\big]-\mathbb E_{\mathbf x}\big[\log[\mathrm{sig}[f[\mathbf x,\boldsymbol\phi]]]\big]$$
$$=-\int Pr(\mathbf x^*)\log\big[1-\mathrm{sig}[f[\mathbf x^*,\boldsymbol\phi]]\big]d\mathbf x^*-\int Pr(\mathbf x)\log\big[\mathrm{sig}[f[\mathbf x,\boldsymbol\phi]]\big]d\mathbf x$$
 where $Pr(\mathbf x^*)$ is the distribution of generated samples and $Pr(\mathbf x)$ the true one (p. 282).
- When $I=J$, the optimal discriminator for a sample $\tilde{\mathbf x}$ of unknown origin is
$$Pr(\text{real}|\tilde{\mathbf x})=\mathrm{sig}[f[\tilde{\mathbf x},\boldsymbol\phi]]=\frac{Pr(\tilde{\mathbf x}|\text{real})}{Pr(\tilde{\mathbf x}|\text{generated})+Pr(\tilde{\mathbf x}|\text{real})}=\frac{Pr(\mathbf x)}{Pr(\mathbf x^*)+Pr(\mathbf x)}\tag{15.7}$$
- Substituting into 15.6, with (added step) the identity $1-\frac{Pr(\mathbf x)}{Pr(\mathbf x^*)+Pr(\mathbf x)}=\frac{Pr(\mathbf x^*)}{Pr(\mathbf x^*)+Pr(\mathbf x)}$:
$$L[\boldsymbol\phi]=-\int Pr(\mathbf x^*)\log\Big[\frac{Pr(\mathbf x^*)}{Pr(\mathbf x^*)+Pr(\mathbf x)}\Big]d\mathbf x^*-\int Pr(\mathbf x)\log\Big[\frac{Pr(\mathbf x)}{Pr(\mathbf x^*)+Pr(\mathbf x)}\Big]d\mathbf x\tag{15.8}$$
- "Disregarding additive and multiplicative constants," this is the Jensen–Shannon divergence:
$$D_{JS}\big[Pr(\mathbf x^*)\,\|\,Pr(\mathbf x)\big]=\tfrac12D_{KL}\Big[Pr(\mathbf x^*)\Big\|\tfrac{Pr(\mathbf x^*)+Pr(\mathbf x)}{2}\Big]+\tfrac12D_{KL}\Big[Pr(\mathbf x)\Big\|\tfrac{Pr(\mathbf x^*)+Pr(\mathbf x)}{2}\Big]\tag{15.9}$$
$$=\tfrac12\int Pr(\mathbf x^*)\log\Big[\frac{2Pr(\mathbf x^*)}{Pr(\mathbf x^*)+Pr(\mathbf x)}\Big]d\mathbf x^*+\tfrac12\int Pr(\mathbf x)\log\Big[\frac{2Pr(\mathbf x)}{Pr(\mathbf x^*)+Pr(\mathbf x)}\Big]d\mathbf x$$
 The first integral is labelled *quality*, the second *coverage*.
- Quality term: small when the mixture $(Pr(\mathbf x^*)+Pr(\mathbf x))/2$ is high wherever $Pr(\mathbf x^*)$ is high. It penalises regions with samples but no real examples. Coverage term: it penalises regions with real examples but no samples (p. 282–283).
- By equation 15.6, the coverage term does not depend on the generator, so the generator "doesn't care" about coverage. This is the *putative* reason for mode dropping (p. 283).

*Intuition note.* A perfect critic turns the game into a distance between "what the generator makes" and "what the data are". The generator is punished for making junk, but (putatively) not for missing parts of the data.

#### 15.2.2 Vanishing gradients (p. 283–284)
- With an optimal discriminator, the loss maximises a measure of distance between distributions. If they are completely disjoint, that distance is maximal and small changes to the generator do not decrease the loss. In the original formulation, a perfect discriminator likewise gives no change in score for small changes to the generated data (Figure 15.6) (p. 283).
- The distributions may really be disjoint. Generated samples lie in a subspace the size of $\mathbf z$. Real data also lie in a low-dimensional subspace. Little or no overlap gives very small or no gradients (p. 283).
- Evidence (Figure 15.7): freezing the DCGAN generator after 1, 10 and 25 epochs and training the discriminator further makes the generator gradients decrease rapidly (log scale). So if the discriminator becomes too good, generator updates are attenuated (p. 283–284).

#### 15.2.3 Wasserstein distance (p. 284)
- The Wasserstein (earth mover's, for discrete distributions) distance is the work needed to move probability mass from one distribution to create the other. Work is mass times distance moved. It is well-defined even for disjoint distributions and decreases smoothly as they approach (p. 284).

#### 15.2.4 Wasserstein distance for discrete distributions (pp. 284–286)
- For $Pr(x=i)$ and $q(x=j)$ over $K$ bins, with transport cost $|i-j|$, the transport plan is a matrix $\mathbf P$:
$$D_w\big[Pr(x)\|q(x)\big]=\min_{\mathbf P}\Big[\sum_{i,j}P_{ij}\cdot|i-j|\Big]\tag{15.10}$$
 subject to
$$\sum_jP_{ij}=Pr(x=i),\qquad\sum_iP_{ij}=q(x=j),\qquad P_{ij}\ge0\tag{15.11}$$
 The text labels the second constraint "initial distribution of $q(x)$" (p. 284).
- Figure 15.8: $\mathbf P$ is a joint distribution. Optimal $\mathbf P$ tends to lie near the diagonal, where the distance cost is lowest (p. 285).
- This is a linear programming problem. Primal form: minimise $\mathbf c^T\mathbf p$ such that $\mathbf A\mathbf p=\mathbf b$, $\mathbf p\ge\mathbf 0$. Here $\mathbf p$ is the vectorised $P_{ij}$, $\mathbf c$ the distances and $\mathbf A\mathbf p=\mathbf b$ the initial-distribution constraints (p. 285). Dual form: maximise $\mathbf b^T\mathbf f$ such that $\mathbf A^T\mathbf f\le\mathbf c$. The dual has the same solution:
$$D_w\big[Pr(x)\|q(x)\big]=\max_{\mathbf f}\Big[\sum_iPr(x=i)f_i-\sum_jq(x=j)f_j\Big]\tag{15.12}$$
 subject to
$$|f_{i+1}-f_i|<1\tag{15.13}$$
 i.e. adjacent values of $\{f_i\}$ cannot change by more than one (pp. 285–286).

#### 15.2.5 Continuous distributions (p. 286)
- Primal form:
$$D_w\big[Pr(\mathbf x),q(\mathbf x)\big]=\min_{\pi[\bullet,\bullet]}\Big[\iint\pi(\mathbf x_1,\mathbf x_2)\cdot\|\mathbf x_1-\mathbf x_2\|\,d\mathbf x_1d\mathbf x_2\Big]\tag{15.14}$$
 with constraints like 15.11 on the plan $\pi(\mathbf x_1,\mathbf x_2)$ (mass moved from $\mathbf x_1$ to $\mathbf x_2$). Dual form:
$$D_w\big[Pr(\mathbf x),q(\mathbf x)\big]=\max_{f[\mathbf x]}\Big[\int Pr(\mathbf x)f[\mathbf x]d\mathbf x-\int q(\mathbf x)f[\mathbf x]d\mathbf x\Big]\tag{15.15}$$
 subject to the Lipschitz constant of $f[\mathbf x]$ being less than one (absolute gradient below one).

#### 15.2.6 Wasserstein GAN loss (p. 286)
- Optimise over functions by using a network $f[\mathbf x,\boldsymbol\phi]$ and approximate the integrals with samples:
$$L[\boldsymbol\phi]=\sum_jf[\mathbf x^*_j,\boldsymbol\phi]-\sum_if[\mathbf x_i,\boldsymbol\phi]=\sum_jf[\mathbf g[\mathbf z_j,\boldsymbol\theta],\boldsymbol\phi]-\sum_if[\mathbf x_i,\boldsymbol\phi]\tag{15.16}$$
 The discriminator must satisfy, at every position $\mathbf x$,
$$\Big|\frac{\partial f[\mathbf x,\boldsymbol\phi]}{\partial\mathbf x}\Big|<1\tag{15.17}$$
- Options: clip discriminator weights to a small range (e.g. ±0.01), or use the gradient-penalty WGAN (WGAN-GP), which adds a regularisation term that increases as the gradient norm deviates from unity.

*Intuition note.* Wasserstein distance measures "how far" the distributions are, not just "whether they overlap". It is well defined even when the distributions are disjoint and decreases smoothly as they approach. The gradient limit (Lipschitz constant below one) is the constraint placed on the critic in the dual form.

### 15.3 Progressive growing, minibatch discrimination, truncation (pp. 287–289)
- Wasserstein makes training more stable, but more machinery is needed for high-quality images (p. 287).
- **Progressive growing (Fig. 15.9):** train a DCGAN-like GAN on 4×4 images. Then add generator layers (upsample, process) for 8×8, and matching discriminator layers, and so on (to 1024×1024 in the figure). The new layers "fade in": the higher-resolution image is first an upsampled version of the previous result, passed via a residual connection, and the new layers gradually take over (pp. 287–289).
- **Minibatch discrimination:** helps prevent mode collapse. Compute feature statistics across minibatches of synthesized and real data, summarise them, and add them as a feature map (usually toward the end of the discriminator). The discriminator can then signal the generator to include a similar amount of variation as the real data (p. 289).
- **Truncation (Fig. 15.10):** sample only latent variables close to the mean (reject those further than $\tau$ standard deviations). Variation falls but quality improves. At $\tau=2.0$ samples are varied but may have defects. At $\tau=0.04$ they look almost identical (pp. 288–289).
- Careful normalisation and regularisation also help. Combined, GANs make varied realistic images (Fig. 15.11). Smooth latent-space moves can sometimes give realistic interpolations, usually only for short trajectories (Fig. 15.12; p. 288–289).

### 15.4 Conditional generation (pp. 289–291)
Plain GANs do not let us choose attributes (hair colour, age) without training separate GANs. Conditional models give control (p. 289).
- **15.4.1 Conditional GAN:** an attribute vector $\mathbf c$ goes to both networks: $\mathbf g[\mathbf z,\mathbf c,\boldsymbol\theta]$ and $f[\mathbf x,\mathbf c,\boldsymbol\phi]$. The discriminator distinguishes a generated sample with the target attribute from a real example with its real attribute. $\mathbf c$ can be appended to $\mathbf z$. For the discriminator it may be appended to the input (1D data), or for images can be transformed linearly to 2D and added as an extra channel to the input or a hidden layer (p. 289).
- **15.4.2 ACGAN:** for a discrete attribute with $C$ categories the discriminator has $C+1$ outputs. The first goes through a sigmoid (real or generated). The other $C$ go through a softmax (class probabilities). It must predict the class correctly (Fig. 15.13b, 15.14; p. 291).
- **15.4.3 InfoGAN:** the generator takes noise $\mathbf z$ and *random* attribute variables $\mathbf c$. The discriminator predicts real/synthetic and estimates $\mathbf c$. The insight is that interpretable real-world characteristics should be easiest to predict, hence represented in $\mathbf c$. Discrete $\mathbf c$ uses a binary or multiclass cross-entropy loss. Continuous $\mathbf c$ uses a least squares loss. Discrete variables find categories, continuous ones gradual variation. On MNIST, a 10-category $c_1$ recovers the ten digits. $c_2$ seems to correspond to orientation and $c_3$ to stroke thickness (Fig. 15.15, pp. 290–292).

### 15.5 Image translation (pp. 291–296)
The discriminator can act as a prior favouring realism in tasks that translate one image to another (grayscale→colour, noisy→clean, blurry→sharp, sketch→photo). Three models use different amounts of manual labelling: Pix2Pix (before/after pairs), models with an adversarial loss (pairs for the main model, plus unpaired "after" images for the discriminator), and CycleGAN (unpaired) (pp. 291–292).
- **15.5.1 Pix2Pix (Fig. 15.16):** a U-Net $\hat{\mathbf x}=\mathbf g[\mathbf c,\boldsymbol\theta]$ maps image $\mathbf c$ to another style. The content loss penalises the $\ell_1$ norm $\|\mathbf x-\mathbf g[\mathbf c,\boldsymbol\theta]\|_1$ (the text says "between the input $\mathbf c$ and ground truth output $\mathbf x$"). The discriminator $f[\mathbf c,\mathbf x,\boldsymbol\phi]$ sees before/after pairs and tells real pairs from before/synthesized pairs (p. 292–293).
 - The content loss fixes large-scale structure. So the discriminator is mainly needed for local texture. The PatchGAN loss uses a purely convolutional classifier whose last-layer units each judge the region in their receptive field. The responses are averaged (p. 293).
 - One way to view it is as a conditional GAN conditioned on an image. The U-Net takes no noise. The original authors tried adding noise, but the network just learned to ignore it (p. 293).
- **15.5.2 Adversarial loss:** adds a penalty if a discriminator can distinguish a supervised network's output from real examples of the output domain. It can be applied to the whole output or to patches. It helps realism of complex outputs, but "doesn't necessarily lead to a better solution in terms of the original loss function" (p. 293).
 - **SRGAN:** a convolutional network with residual connections upsamples a low-resolution image (×4 in Fig. 15.17). Three losses: content (squared difference to the true high-res image), VGG/perceptual (squared difference of VGG-network activations; encourages semantic similarity) and adversarial (real vs. upsampled high-res) (pp. 293, 295).
- **15.5.3 CycleGAN (Fig. 15.18):** for two sets of images in different styles with no matching pairs (e.g. photos and Monet paintings). The idea is that converting one way and back should recover the original. The loss is a weighted sum of: content loss ($\ell_1$, before and after similar), adversarial loss (output indistinguishable from the target domain) and cycle-consistency loss. Two models (A→B and B→A) are trained together, and the cycle loss is low if a translated image translates successfully back (pp. 293–296).

### 15.6 StyleGAN (pp. 296–298)
- StyleGAN splits dataset variation into meaningful components, each controlled by a subset of the latent variables. It controls the image at different scales and separates style from noise. For faces, large scale means face shape and head pose, medium scale means facial features, and fine scale means hair and skin colour. Noise covers unimportant variation (exact hair placement, stubble, freckles, pores) (p. 296).
- Latent inputs can be introduced at various points and modify the representation in different ways (p. 296).
- **Main pipeline:** a learned constant 4×4×512 representation goes through convolutions that upsample. Style and noise variables enter at every scale; closer to the output means finer detail (p. 296).
- **Noise:** independent Gaussian vectors $\mathbf z_1,\mathbf z_2,\dots$ are added after each convolution. They match the spatial size of the representation at that point and are multiplied by learned per-channel scaling $\boldsymbol\psi_1,\boldsymbol\psi_2,\dots$ (p. 296).
- **Style:** a 1×1×512 noise tensor passes through a seven-layer fully connected network to give $\mathbf w$. This lets the network decorrelate aspects of style so that each dimension of $\mathbf w$ can represent an independent real-world factor. $\mathbf w$ is linearly transformed to a 2×1×512 tensor $\mathbf y$, which sets the per-channel mean and variance after noise addition: adaptive instance normalization (Fig. 11.14e). Vectors $\mathbf y_1,\mathbf y_2,\dots$ are injected at several points (pp. 296–298).

### 15.7 Summary (pp. 298–299)
GANs train a generator with a discriminator. The original formulation has a weak signal when real and generated are easy to separate, which led to the Wasserstein GAN. Tricks improve images. Conditional GANs add control. Image translation keeps the conditioning image but drops noise, and the discriminator becomes an extra realism loss. StyleGAN controls style and noise at different scales (pp. 298–299).

### Notes (pp. 299–303), compressed
- Goodfellow et al. (2014) introduced GANs. GANs are mainly for images (DCGAN, progressive GAN, StyleGAN), mostly convolutional. Others include graphs, voice, EEG, text, music, 3D, DNA, video (p. 300).
- **Loss functions:** the claim of convergence to Nash equilibria is not always supported by more recent evidence. Alternatives are least squares GAN, f-divergences, relativistic GAN and an energy-based view. The Wasserstein Lipschitz limit has been enforced by weight clipping, gradient penalty or spectral normalization (p. 300).
- **Tricks:** truncation (Marchesi; Brock et al. add an orthogonality regulariser so truncating $\mathbf z$ relates more closely to truncating output variance). Others: top-$K$ gradients, label smoothing, history of generated images, noise in the discriminator input (p. 300).
- **Diversity:** Arora et al. suggest a finite-capacity discriminator lets the objective approach its optimum even with limited output variation. Wu et al. found a mismatch with real distributions. Arora & Zhang's duplicate test: for DCGAN a duplicate occurs with probability >50% with 400 samples. Arora & Zhang infer a support size of about 400,000, smaller than the training set (p. 301).
- **Mode collapse remedies:** a regulariser for conditional GANs, VEEGAN, minibatch standard-deviation feature (Karras), MAD-GAN. Multi-scale work uses multiple discriminators (p. 301).
- **StyleGAN v2** fixed artifacts and added limited-data training and anti-aliasing. **Conditional GANs:** conditions include classes, text, attributes, boxes, images (pp. 301–302).
- **Inverting GANs** (to edit real images) uses an encoder or latent optimisation. Abdal et al. showed StyleGAN cannot be inverted without artifacts and proposed inverting to an extended style space. Pivotal tuning fine-tunes the generator. iGAN and EditGAN allow interactive edits (pp. 302–303).

### Problems (p. 303)
Problems 15.1–15.6 are listed under Exercises.

## Toy example (ours, not from the text)
**Goal:** show why the original GAN distance can give no signal while Wasserstein does (sections 15.2.2–15.2.4).

Take bins 1–4. Let the real distribution be all mass on bin 1: $P=(1,0,0,0)$. Let the generator's distribution $Q$ be all mass on bin 3, then on bin 2, then on bin 1.

*Jensen–Shannon (eq. 15.9, natural log).*
- $Q=\delta_3$: mixture $M=(P+Q)/2=(0.5,0,0.5,0)$. $D_{KL}(P\|M)=1\cdot\ln(1/0.5)=\ln2$ and $D_{KL}(Q\|M)=1\cdot\ln(1/0.5)=\ln 2$. So $D_{JS}=\tfrac12\ln2+\tfrac12\ln2=\ln2\approx0.693$.
- $Q=\delta_2$: $M=(0.5,0.5,0,0)$. The same arithmetic gives $\ln2\approx0.693$.
- $Q=\delta_1$: $M=P$, so $D_{JS}=0$.

*Wasserstein (eq. 15.10, cost $|i-j|$).* All mass 1 must move.
- $Q=\delta_3$: $W=1\times|1-3|=2$.
- $Q=\delta_2$: $W=1\times|1-2|=1$.
- $Q=\delta_1$: $W=0$.

**Reading:** while the distributions are disjoint, $D_{JS}$ stays at 0.693. Moving the generator from bin 3 to bin 2 does not change it, so there is no gradient. $W$ falls from 2 to 1 to 0, so every step toward the data is rewarded. (Both numbers are for exact distributions. The text's GAN uses a discriminator to approximate them.)

## Concepts
- [[generative-adversarial-network]] (new) — generator plus discriminator trained as a game to produce samples; gives no probability model (p. 276)
- [[generator]] (new) — network mapping latent noise $\mathbf z$ to a sample $\mathbf g[\mathbf z,\boldsymbol\theta]$ (p. 276)
- [[discriminator]] (new) — classifier $f[\bullet,\boldsymbol\phi]$ for real vs. generated, used as the training signal and then discarded (p. 276)
- [[minimax-game]] (new) — $\boldsymbol\phi$ minimises, $\boldsymbol\theta$ maximises one loss; solution is a Nash equilibrium (p. 278)
- [[cross-entropy / log-loss]] — binary form is the discriminator loss (p. 278)
- [[jensen-shannon-divergence]] (new) — average KL to the mixture; GAN loss with an optimal discriminator, up to constants (p. 282)
- [[mode-dropping-collapse]] (new) — generator covers only part of the data (dropping) or ignores $\mathbf z$ and outputs few points (collapse) (p. 281)
- [[vanishing-gradients-gan]] (new) — a too-good discriminator gives the generator almost no gradient (p. 283)
- [[wasserstein-distance]] (new) — cost of moving mass to turn one distribution into another; WGAN needs discriminator Lipschitz constant < 1 (pp. 284, 286)
- [[truncation-trick]] (new) — sample $\mathbf z$ near the mean to trade diversity for quality (p. 288)
- [[conditional-generation]] (new) — conditional GAN, ACGAN, InfoGAN give attribute control (p. 289)
- [[softmax]] — gives class probabilities in the ACGAN discriminator (p. 291)
- [[adversarial-loss]] (new) — penalty when a discriminator can tell supervised output from real examples (p. 293)
- [[cycle-consistency]] (new) — translate there and back should recover the input (p. 296)
- [[style-noise-separation]] (new) — StyleGAN style via adaptive instance normalisation at several scales, noise added separately (pp. 296–298)

## Canonical instances
- [[toy-1d-gan]] — $x^*=z+\theta$ walks toward the real data as the sigmoid flattens (p. 277)
- [[dcgan]] — early convolutional image GAN needing delicate tricks (p. 279)
- [[infogan-mnist]] — recovers the ten digits as a categorical attribute; two continuous attributes seem to correspond to orientation and stroke thickness (p. 292)
- [[pix2pix]] — U-Net with content loss and PatchGAN loss (p. 292)
- [[srgan]] — ×4 super-resolution with content, VGG and adversarial losses (p. 293)
- [[cyclegan]] — unpaired translation, e.g. horse↔zebra, photo↔Monet (pp. 295–297)
- [[stylegan]] — scale-wise style and noise control (p. 296)

## Bridges (candidates)
- [same-math] KL divergence inside $D_{JS}$ (eq. 15.9) ↔ llm: KL penalty — same divergence $D_{KL}$, here used between a distribution and a mixture
- [structural-analogy] Discriminator as learned critic for the generator ↔ llm: reward model scoring outputs — both are learned judges whose scores steer a generator
- [structural-analogy] Truncation: quality vs. diversity ↔ llm: sampling temperature — both reduce variation to raise typical quality
- [structural-analogy] Mode dropping (missing parts of the data) ↔ llm: algorithmic fidelity of silicon samples — both ask whether generated output covers all real subgroups

## Questions this raises
- If a GAN gives no likelihood, how can we measure whether it covers the whole data distribution? (The Notes describe indirect tests, e.g. duplicate counting, p. 301.)
- Does a good adversarial loss help the original task? (The text says it "doesn't necessarily" improve the original loss, p. 293.)
- How much of the quality–diversity trade-off can be recovered without truncation?
- Can the latent factors found by InfoGAN or StyleGAN be trusted as "real-world" factors, or are they only seemingly so (p. 292, "seems to correspond")?

## Exercises worth doing
- Ex. 15.1 (p. 303) — value of the Jensen–Shannon loss when $Pr(\mathbf x^*)=Pr(\mathbf x)$ — difficulty: easy
- Ex. 15.2 (p. 303) — relate loss $L$ (15.8) to $D_{JS}$ (15.9) — difficulty: medium
- Ex. 15.3 (p. 303) — write the 8×16 matrix $\mathbf A$ for the LP form of earth mover's distance on 4 bins — difficulty: medium
- Ex. 15.4 (p. 303) — KL, reverse KL, JS, Wasserstein between two shifted uniform distributions — difficulty: hard
- Ex. 15.5 (p. 303) — plot KL and Wasserstein between Gaussians versus mean difference — difficulty: easy
- Ex. 15.6 (p. 303) — probability mass discarded by truncation — difficulty: medium

## Reading notes
- Printed = pdf − 14. Page images were checked for all equations.
- Figure 15.18b–c (horse↔zebra) appear blank in the page image. Presumably a rendering omission in this copy.
- Eq. 15.11: the second constraint's label reads "initial distribution of $q(x)$" (it is the target distribution). Eq. 15.13 uses strict "<" in print.
- The Pix2Pix content-loss sentence (p. 292) says "between the input $\mathbf c$ and ground truth output $\mathbf x$"; the formula compares $\mathbf x$ and $\mathbf g[\mathbf c,\boldsymbol\theta]$.
- Problem 15.2 prints $D_{JS}[Pr(\mathbf x)^*\,\|\,Pr(\mathbf x)]$, apparently a notational slip for $Pr(\mathbf x^*)$. Problem 15.5 writes "Dkl" and "KL distance" for the divergence.
- Footer on pages: "Draft: please send errata to udlbookmail@gmail.com"; license CC-BY-NC-ND, MIT Press.
