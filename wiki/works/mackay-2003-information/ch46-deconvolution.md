---
id: mackay-2003-information/ch46-deconvolution
work: mackay-2003-information
unit: "46 Deconvolution"
pages: 549-554
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Deconvolution

## L0 — One line
Under Gaussian assumptions, the most probable deblurred image is a regularized linear filter of the data, which a minimum-square-error argument also gives; better image priors, such as positive-only ones, improve on it.

## L1 — The gist (≤ 120 words)
How can we recover a true image $\mathbf f$ from blurred, noisy data $\mathbf d$? MacKay derives the optimal linear filter in two ways: as the most probable image under a Gaussian likelihood and prior, and as the linear estimator with minimum expected squared error. Both give the same filter. The Bayesian route lets us criticise the assumptions, for example that a Gaussian prior ignores positivity, and replace them (maximum-entropy priors). It also gives error bars, which can be visualised as a "movie". The chapter then briefly discusses neural networks as improvable algorithms, and speculates that human early vision deconvolves the eye's chromatic aberration.

**Prerequisites:** Bayes' theorem; Gaussian densities; matrix transpose and inverse; expectation; log-posterior maximisation.

## L2 — Key ideas
- The data model is linear: $d_n=\sum_k R_{nk}f_k+n_n$. Blur is the operator $\mathbf R$ and the noise is $\mathbf n$ (p. 549).
- A Gaussian likelihood times a Gaussian prior gives a Gaussian posterior. Its mean $\mathbf f_{\rm MP}$ is a regularized pseudoinverse of $\mathbf R$ (a matrix inverse stabilised by an extra term) applied to $\mathbf d$ (p. 550).
- A non-Bayesian minimum-square-error derivation gives the same filter without explicit Gaussian assumptions, once $\mathbf F=\sigma_f^2\mathbf C^{-1}$. Its ad hoc choices are the quadratic error and the linear estimator (p. 551).
- Gaussian priors do not require pixel values to be positive; optimal linear filters then give artefacts such as negative sky patches. Maximum-entropy priors (priors built from an entropy function $S$) enforce positivity, and the maximum-entropy model improved reconstructions greatly (p. 551).
- Error bars $\boldsymbol\Sigma_{\mathbf f|\mathbf d}$ can be visualised with a correlated random walk around the posterior (p. 551–552).
- A standard algorithm can be recast as a neural network and then tuned to data. MacKay argues this can only improve it (p. 552).
- MacKay argues that centre-surround colour-opponent cells (retinal ganglion and lateral geniculate cells) serve deconvolution of chromatic aberration (the colour-dependent blur of the eye's optics). He speculates that the McCollough effect (a long-lasting colour–orientation aftereffect) and microsaccades (tiny eye movements) are also involved (p. 553–554).

## L3 — Walkthrough

### 46.1 Traditional image reconstruction methods

**Setup.** Data are linearly related to the image (p. 549):
$$d_n=\sum_k R_{nk}f_k+n_n.\tag{46.1}$$
Here $n=1..N$ indexes data and $k,k'=1..K$ indexes pixels. So $\mathbf R$ is $N\times K$, $\mathbf f$ is $K$-vector and $\mathbf d$ is $N$-vector. For a blurry camera, $\mathbf R$ is a convolution with the point spread function (the image of a single point source). Image and data live in the same space here, but should be kept distinct (p. 549).

**Bayesian derivation.** Assumptions: $\mathbf R$ known; noise Gaussian, independent, with known $\sigma_\nu$ (p. 549).
$$P(\mathbf d\mid\mathbf f,\sigma_\nu,\mathcal H)=\frac{1}{(2\pi\sigma_\nu^2)^{N/2}}\exp\Big(-\sum_n\big(d_n-\sum_kR_{nk}f_k\big)^2\big/(2\sigma_\nu^2)\Big)\tag{46.2}$$
$$P(\mathbf f\mid\sigma_f,\mathcal H)=\frac{\det{}^{-\frac12}\mathbf C}{(2\pi\sigma_f^2)^{K/2}}\exp\Big(-\sum_{k,k'}f_kC_{kk'}f_{k'}\big/(2\sigma_f^2)\Big)\tag{46.3}$$
(as printed; see Reading notes). With uncorrelated pixels, $\mathbf C=\mathbf I$. The "intrinsic correlation function" model uses $\mathbf C=[\mathbf G\mathbf G^{\rm T}]^{-1}$. Here $\mathbf G$ maps an uncorrelated hidden image to the real correlated image. It should not be confused with $\mathbf R$ (p. 549). MacKay notes a zero-mean Gaussian prior is a poor assumption if it is known that all pixels are positive, "but let us proceed" (p. 550).

Bayes' theorem (p. 550):
$$P(\mathbf f\mid\mathbf d,\sigma_\nu,\sigma_f,\mathcal H)=\frac{P(\mathbf d\mid\mathbf f,\sigma_\nu,\mathcal H)P(\mathbf f\mid\sigma_f,\mathcal H)}{P(\mathbf d\mid\sigma_\nu,\sigma_f,\mathcal H)}\tag{46.4}$$
Posterior = Likelihood × Prior / Evidence (46.5). The evidence is only a normalizer here. In a more sophisticated analysis it compares values of $\sigma_\nu,\sigma_f$ or different $\mathbf R$ (p. 550).

A product of two Gaussians in $\mathbf f$ is Gaussian. It is summarised by its mean, the most probable image $\mathbf f_{\rm MP}$, and its covariance, which gives joint error bars (p. 550):
$$\boldsymbol\Sigma_{\mathbf f|\mathbf d}\equiv[-\nabla\nabla\log P(\mathbf f\mid\mathbf d,\sigma_\nu,\sigma_f,\mathcal H)]^{-1}\tag{46.6}$$
Setting the derivative of the log posterior to zero gives:
$$\mathbf f_{\rm MP}=\Big[\mathbf R^{\rm T}\mathbf R+\frac{\sigma_\nu^2}{\sigma_f^2}\mathbf C\Big]^{-1}\mathbf R^{\rm T}\mathbf d\tag{46.7}$$
The operator $[\mathbf R^{\rm T}\mathbf R+\frac{\sigma_\nu^2}{\sigma_f^2}\mathbf C]^{-1}\mathbf R^{\rm T}$ is the *optimal linear filter*. If $\frac{\sigma_\nu^2}{\sigma_f^2}\mathbf C$ can be neglected, it becomes the pseudoinverse $[\mathbf R^{\rm T}\mathbf R]^{-1}\mathbf R^{\rm T}$. That term regularizes this ill-conditioned inverse (p. 550). An equivalent form (p. 550):
$$\text{Optimal linear filter}=\mathbf C^{-1}\mathbf R^{\rm T}\Big[\mathbf R\mathbf C^{-1}\mathbf R^{\rm T}+\frac{\sigma_\nu^2}{\sigma_f^2}\mathbf I\Big]^{-1}\tag{46.8}$$

*Intuition note:* The pseudoinverse tries to undo the blur exactly; the source calls it an ill-conditioned inverse (p. 550), and in practice such an inverse amplifies noise (our gloss). The extra term pulls the answer toward the zero-mean Gaussian prior and regularizes the inverse. For fixed $\sigma_f$, a larger $\sigma_\nu$ makes the ratio $\sigma_\nu^2/\sigma_f^2$ larger, so the extra term weighs more.

**Minimum square error derivation.** Estimate the image by a linear function of the data (p. 550):
$$\hat{\mathbf f}=\mathbf W\mathbf d.\tag{46.9}$$
Minimise the expected squared error. The average is over the noise and the ensemble of images. The noise has zero mean and $\langle n_nn_{n'}\rangle=\sigma_\nu^2\delta_{nn'}$, and is uncorrelated to second order with everything else. Repeated indices are summed (p. 550).
$$\langle E\rangle=\tfrac12\langle(W_{kn}d_n-f_k)^2\rangle\tag{46.10}$$
$$=\tfrac12\langle(W_{kn}R_{nj}f_j-f_k)^2\rangle+\tfrac12W_{kn}W_{kn}\sigma_\nu^2\tag{46.11}$$
Differentiating with respect to $\mathbf W$, with $\mathbf F\equiv\langle f_{j'}f_j\rangle$, gives (p. 551):
$$\mathbf W_{\rm opt}=\mathbf F\mathbf R^{\rm T}\big[\mathbf R\mathbf F\mathbf R^{\rm T}+\sigma_\nu^2\mathbf I\big]^{-1}\tag{46.12}$$
With $\mathbf F=\sigma_f^2\mathbf C^{-1}$ this is (46.8). The ad hoc assumptions are the quadratic error measure and the linear estimator. Without explicit Gaussian assumptions, the derivation reproduces the Bayesian $\mathbf f_{\rm MP}$. The Bayesian advantage is that we can criticise the assumptions and modify them (p. 551).

**Other image models.** The better $P(\mathbf f\mid\mathcal H)$ matches the real world, the better the reconstructions and the less data needed (p. 551). The Gaussian prior does not specify that pixel intensities are positive. This causes the worst artefacts for high-contrast images or large black patches. MacKay says optimal linear filters applied to astronomical data give reconstructions with negative areas, "patches of sky that suck energy out of telescopes" (p. 551). The maximum entropy model (Gull and Daniell, 1978) succeeded principally because it forces positivity (p. 551).

*Classic maxent* entropic prior (Skilling, 1989), with default image $\mathbf m$ and normalizer $Z$ (p. 551):
$$P(\mathbf f\mid\alpha,\mathbf m,\mathcal H_{\rm Classic})=\exp(\alpha S(\mathbf f,\mathbf m))/Z\tag{46.13}$$
$$S(\mathbf f,\mathbf m)=\sum_i\big(f_i\ln(m_i/f_i)+f_i-m_i\big)\tag{46.14}$$
This enforces positivity. $\alpha$ sets the characteristic dynamic range by which pixels differ from $\mathbf m$. The *ICF maxent* model (Gull, 1989) writes $\mathbf f=\mathbf G\mathbf h$ and puts a classic maxent prior on the hidden image $\mathbf h$, which brings in spatial correlations (p. 551).

**Probabilistic movies.** To visualise $\boldsymbol\Sigma_{\mathbf f|\mathbf d}$, use a correlated random walk. For a Gaussian posterior, make a correlated sequence of unit normal vectors ($\mathbf z$ is a fresh unit normal vector; $c^2+s^2=1$; $c$ controls how persistent the memory is) (p. 551–552):
$$\mathbf n^{(t+1)}=c\,\mathbf n^{(t)}+s\,\mathbf z\tag{46.15}$$
Render the image sequence, with $\boldsymbol\Sigma^{1/2}_{\mathbf f|\mathbf d}$ the Cholesky decomposition of $\boldsymbol\Sigma_{\mathbf f|\mathbf d}$ (p. 552):
$$\mathbf f^{(t)}=\mathbf f_{\rm MP}+\boldsymbol\Sigma^{1/2}_{\mathbf f|\mathbf d}\,\mathbf n^{(t)}\tag{46.16}$$

### 46.2 Supervised neural networks for image deconvolution
**MacKay's account of a common strategy:** take a standard algorithm, read it as a parameterized input-output mapping, call it a neural network, and adapt the parameters to data. By construction the network can reproduce the algorithm, so adaptation "can only make the performance better" (p. 552). Two reasons are given. (1) Algorithms often do not optimize the real objective. His example: a speech-recognition hidden Markov model is fitted for generative probability, but the real goal is discriminating words, and discriminative training does improve performance. (2) The network can be more flexible, since parameters the designers treated as fixed may become adaptive (p. 552).

### 46.3 Deconvolution in humans
Retinal images are severely blurred. Most people resolve about 1 arcminute, yet the retinal point spread function can be as wide as 5 arcminutes. So we resolve pixels twenty-five times smaller in area than the blob from a point source (p. 552). MacKay discusses chromatic aberration (blue light is refracted more strongly than red) in this context. The eye focuses for green, so a white dot gives a sharp green dot, a broader red blob and an even broader blue blob. Their width scales with pupil diameter (p. 552).

**Demonstration (p. 553).** Cut a 1.5 mm slit in card. View small red, blue, magenta and white objects on black, from a distance where you can only just read the text (perhaps about 4 m, for normal vision). Waggle the slit near one eye. The author sees red and blue objects move in opposite directions, by more than 5 arcminutes in a dim room. White objects appear to stay still and are negligibly distorted. He asks whether, through the whole pupil, you can see features far smaller than that movement, and says the retinal image must then be blurred by a diameter equal to the waggling amplitude (p. 553).

**MacKay's claims and speculations:**
- He says one of the main functions of early visual processing must be to deconvolve this aberration. He thinks the "feature extraction/edge detection" explanation of centre-surround colour-opponent cells is mistaken, and that they serve deconvolution, in the fovea at least (p. 553).
- He speculates the McCollough effect is produced by the adaptation mechanism that tunes these circuits. Pupil size changes within seconds, and the effect can be induced within 30 seconds yet is long-lasting, even when an eye is covered; he suggests it is in our interests that the circuits stay well-tuned during sleep (p. 553–554).
- He wonders whether colour vision evolved to see black and white sharper, since colour information makes deconvolution easier (p. 554).
- Microsaccades are 5–10 arcminutes (Ratliff and Riggs, 1950), similar to the size of the chromatic aberration. He asks whether this is a coincidence and says microsaccades "surely" must play an essential role in deconvolution (p. 554).

### 46.4 Exercise
Exercise 46.1 asks for a blur, noise, optimal-linear-filter deconvolution, error bars and a probabilistic movie (p. 554).

## Toy example (ours)
One pixel and one measurement ($K=N=1$): $R=r=2$, $C=1$, $\sigma_\nu^2=1$, $\sigma_f^2=4$, so $\sigma_\nu^2/\sigma_f^2=0.25$. Data $d=3$.
- Pseudoinverse: $d/r=3/2=1.5$.
- (46.7): $f_{\rm MP}=\dfrac{r\,d}{r^2+0.25}=\dfrac{6}{4.25}\approx1.412$. (46.8) gives $\frac{2}{4+0.25}$ times 3, the same.
- (46.6): $-\partial^2\log P=r^2/\sigma_\nu^2+1/\sigma_f^2=4+0.25=4.25$, so $\Sigma=1/4.25\approx0.235$.
- Weak blur, $r=0.1$, $d=1$: pseudoinverse $=10$; regularized $=0.1/(0.01+0.25)\approx0.385$. The regularizer stops noise amplification.

## Concepts
- [[deconvolution]] (new) — recovering the image from data blurred by a known operator and corrupted by noise (p. 549)
- [[point-spread-function]] (new) — the image of a point source; defines the convolution $\mathbf R$ (p. 549)
- [[optimal-linear-filter]] (new) — $[\mathbf R^{\rm T}\mathbf R+\frac{\sigma_\nu^2}{\sigma_f^2}\mathbf C]^{-1}\mathbf R^{\rm T}$, giving $\mathbf f_{\rm MP}$ (p. 550)
- [[regularization]] (new) — the $\frac{\sigma_\nu^2}{\sigma_f^2}\mathbf C$ term that stabilises the ill-conditioned inverse (p. 550)
- [[bayes-theorem]] — posterior = likelihood × prior / evidence (p. 550)
- [[prior-distribution]], [[likelihood]], [[posterior-distribution]] — Gaussian here (p. 549–550)
- [[marginal-likelihood]] — the "evidence"; here only a normalizer (p. 550)
- [[intrinsic-correlation-function]] (new) — $\mathbf G$ mapping a hidden uncorrelated image to a correlated one (p. 549)
- [[entropic-prior]] (new) — $\exp(\alpha S(\mathbf f,\mathbf m))/Z$, enforcing positivity (p. 551)
- [[maximum-entropy-principle]] — used here as an image-prior family, with $S$ from (46.14) (p. 551)

## Canonical instances
- [[gaussian-linear-deblurring]] — Gaussian prior and likelihood give a closed-form $\mathbf f_{\rm MP}$ (p. 550)
- [[human-chromatic-aberration]] — retinal blur of about 5 arcminutes versus 1 arcminute acuity (p. 552)

## Bridges (candidates)
- [same-math] $\mathbf f_{\rm MP}$ with Gaussian prior ↔ ridge regression: $\mathbf R^{\rm T}\mathbf R+\lambda\mathbf C$ regularizes least squares.
- [same-math] Probabilistic movie ↔ time series: $\mathbf n^{(t+1)}=c\mathbf n^{(t)}+s\mathbf z$ is an AR(1)-type correlated Gaussian walk.
- [structural-analogy] Entropic prior ↔ KL divergence: $S(\mathbf f,\mathbf m)$ resembles a relative-entropy term against a default $\mathbf m$.

## Questions this raises
- How does the posterior change if the prior enforces positivity? Is it still Gaussian, and how are error bars found?
- How can $\sigma_f$, $\sigma_\nu$ or $\mathbf R$ be chosen using the evidence?
- Is the claim that a neural network "can only" improve a standard algorithm true after training on finite data?
- What evidence would test the speculations about microsaccades and the McCollough effect?

## Exercises worth doing
- Ex. 46.1 (p. 554) — blur with a top-hat PSF, add noise, apply the optimal linear filter, get error bars and a movie — difficulty: medium

## Reading notes
- Printed = pdf − 12.
- Eq. 46.3 as printed in the image shows $\det^{-1/2}\mathbf C$ and $f_kC_{kk'}f'_k$ (the last should be $f_{k'}$). For the stated exponent, the Gaussian normaliser would be $\det^{1/2}\mathbf C$ (our check). In the 46.3 equation above I kept the printed $\det^{-1/2}$ but wrote $f_{k'}$ in the exponent.
- Eq. 46.4 has an extra closing parenthesis in the print.
- The symbol $\mathbf n$ means noise in 46.1 and a unit normal vector in 46.15.
- The derivation of (46.7) and (46.12) is not shown step by step in the source.
- Only the final-form results were given; the steps from (46.11) to (46.12) are omitted by the author.
