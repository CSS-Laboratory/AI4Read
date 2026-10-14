---
id: prince-2023-udl/ch17-variational
work: prince-2023-udl
unit: "Chapter 17 — Variational autoencoders"
pages: 327-348
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Variational autoencoders

## L0 — One line
A VAE is a neural network that computes a lower bound (the ELBO) on the log-likelihood of a nonlinear latent variable model, so that a model whose likelihood cannot be computed exactly can still be trained.

## L1 — The gist (≤ 120 words)
The chapter asks how to learn a distribution Pr(x) when the likelihood is an intractable integral over hidden variables. The answer has three steps. First, define a lower bound on the log-likelihood (the ELBO). Second, make the bound as tight as a simple family allows, by approximating the latent posterior (the distribution of z given x) with a Gaussian predicted by an encoder network. Third, estimate the remaining expectation by sampling, using the reparameterization trick so gradients can flow. The final model contains neither the "variational" nor the "autoencoder" part (p. 327). The author notes that diffusion models can be viewed as VAEs with hierarchical priors (p. 342).

**Prerequisites:** probability densities, marginalization, conditional probability and Bayes' rule, expectation, normal distributions, KL divergence (named only), backpropagation, concave functions.

## L2 — Key ideas
- A latent variable model writes Pr(x) as an integral of Pr(x|z)Pr(z) over hidden z. Simple pieces can define a complex distribution (pp. 327–328).
- In the nonlinear model, the prior is Normal(0, I) and the likelihood is a Gaussian whose mean is a deep network f[z, ϕ]. The result is an infinite mixture of Gaussians (p. 329).
- The likelihood integral is intractable (no closed form, no easy way to evaluate it). Jensen's inequality gives a lower bound, the ELBO, which depends on ϕ and on extra parameters θ (pp. 331–333).
- ELBO = log Pr(x|ϕ) − KL[q ‖ posterior]. The bound is tight when q equals the true posterior (the distribution of z given x); the gap is a KL divergence, a non-negative "distance" between distributions (p. 334).
- The ELBO can also be written as reconstruction accuracy minus KL distance to the prior. This is the form the VAE uses (pp. 335–336).
- Variational approximation: a simple Gaussian q(z|x,θ), whose parameters are predicted by an encoder network, stands in for the intractable posterior. The expectation is estimated by sampling, and the KL term has a closed form (pp. 336–337).
- The reparameterization trick, z* = μ + Σ^{1/2}ε*, moves the random sampling into a separate noise input ε* so that backpropagation can reach the encoder (p. 339).
- Applications: approximating Pr(x) by importance sampling (sampling from an auxiliary distribution and rescaling), generation, resynthesis (encode, modify, decode) and disentanglement (latent dimensions matching independent real-world factors). Vanilla VAE samples are generally low quality (pp. 340–343).

## L3 — Walkthrough

### Introduction (p. 327)
GANs learn a sampler. VAEs, like normalizing flows, are probabilistic models of Pr(x), and you can sample from them. The probability of a new x* cannot be evaluated exactly (p. 327). The author says "the VAE" is really an architecture that helps learn the model. The final model has neither the "variational" nor the "autoencoder" part and is better called a *nonlinear latent variable model* (p. 327).

### 17.1 Latent variable models (pp. 327–328)
A latent variable z is hidden and unobserved. The model specifies a joint Pr(x, z), and Pr(x) is its marginalization (integrating out z):
$$Pr(\mathbf x)=\int Pr(\mathbf x,\mathbf z)\,d\mathbf z \tag{17.1}$$
The joint splits into a likelihood Pr(x|z) and a prior Pr(z):
$$Pr(\mathbf x)=\int Pr(\mathbf x|\mathbf z)Pr(\mathbf z)\,d\mathbf z \tag{17.2}$$
This is indirect, but simple Pr(x|z) and Pr(z) can define complex Pr(x) (p. 328).

**17.1.1 Mixture of Gaussians (p. 328).** Here z is discrete, with a categorical prior and a Gaussian likelihood:
$$Pr(z=n)=\lambda_n,\qquad Pr(x|z=n)=\text{Norm}_x[\mu_n,\sigma_n^2] \tag{17.3}$$
Marginalizing means summing over $n$:
$$Pr(x)=\sum_{n=1}^N Pr(x|z=n)\,Pr(z=n)=\sum_{n=1}^N \lambda_n\,\text{Norm}_x[\mu_n,\sigma_n^2] \tag{17.4}$$
Simple pieces give a complex multi-modal distribution (p. 328).

*Intuition note:* Pick a hidden "cause" first, then generate the data from it. The visible distribution is the blend over all causes.

### 17.2 Nonlinear latent variable model (pp. 328–330)
Both x and z are continuous and multivariate.
$$Pr(\mathbf z)=\text{Norm}_{\mathbf z}[\mathbf 0,\mathbf I] \tag{17.5}$$
$$Pr(\mathbf x|\mathbf z,\boldsymbol\phi)=\text{Norm}_{\mathbf x}\big[\mathbf f[\mathbf z,\boldsymbol\phi],\sigma^2\mathbf I\big] \tag{17.6}$$
Here f is a deep network with parameters ϕ, and the covariance is spherical (p. 329). The latent z has lower dimension than x. f describes the important aspects of the data, and the rest is ascribed to the noise σ²I (p. 329).
$$Pr(\mathbf x|\boldsymbol\phi)=\int \text{Norm}_{\mathbf x}[\mathbf f[\mathbf z,\boldsymbol\phi],\sigma^2\mathbf I]\cdot\text{Norm}_{\mathbf z}[\mathbf 0,\mathbf I]\,d\mathbf z \tag{17.7}$$
This is an infinite mixture of spherical Gaussians. The weights are Pr(z) and the means are the network outputs f[z, ϕ] (p. 329).

**17.2.1 Generation (p. 329).** Use ancestral sampling (sample the parents first, then the children). Draw z* from the prior and compute the mean f[z*, ϕ]. Then draw x* from Pr(x|z*, ϕ). Both distributions are normal, so this is easy (p. 329).

### 17.3 Training (pp. 331–333)
Maximize the log-likelihood over the data {x_i}, with σ² assumed known:
$$\hat{\boldsymbol\phi}=\arg\max_{\boldsymbol\phi}\Big[\sum_{i=1}^I\log Pr(\mathbf x_i|\boldsymbol\phi)\Big] \tag{17.8}$$
with Pr(x_i|ϕ) given by the integral in (17.7), written as eq. 17.9. This is intractable. There is no closed form for the integral and no easy way to evaluate it for a given x (p. 331).

**17.3.1 ELBO.** The remedy is a lower bound: a function always ≤ the log-likelihood for a given ϕ. It also depends on extra parameters θ (p. 331).

**17.3.2 Jensen's inequality.** For a concave function g (the straight line between two points on the curve lies under it) (pp. 331–332):
$$g[\mathbb E[y]]\ge\mathbb E[g[y]] \tag{17.10}$$
For the logarithm:
$$\log[\mathbb E[y]]\ge\mathbb E[\log y] \tag{17.11}$$
$$\log\Big[\int Pr(y)\,y\,dy\Big]\ge\int Pr(y)\log[y]\,dy \tag{17.12}$$
The more general form holds for any function h[y], because h[y] is just another random variable (p. 332):
$$\log\Big[\int Pr(y)h[y]\,dy\Big]\ge\int Pr(y)\log[h[y]]\,dy \tag{17.13}$$
*Intuition note:* The log compresses large values. Averaging after the log gives a smaller number than taking the log of the average.

**17.3.3 Deriving the bound (p. 333).** Multiply and divide by an arbitrary distribution q(z) over the latent variables, then apply (17.12):
$$\log[Pr(\mathbf x|\boldsymbol\phi)]=\log\Big[\int Pr(\mathbf x,\mathbf z|\boldsymbol\phi)d\mathbf z\Big]=\log\Big[\int q(\mathbf z)\frac{Pr(\mathbf x,\mathbf z|\boldsymbol\phi)}{q(\mathbf z)}d\mathbf z\Big] \tag{17.14}$$
$$\log\Big[\int q(\mathbf z)\frac{Pr(\mathbf x,\mathbf z|\boldsymbol\phi)}{q(\mathbf z)}d\mathbf z\Big]\ge\int q(\mathbf z)\log\Big[\frac{Pr(\mathbf x,\mathbf z|\boldsymbol\phi)}{q(\mathbf z)}\Big]d\mathbf z \tag{17.15}$$
The right-hand side is the *evidence lower bound* (ELBO). Pr(x|ϕ) is called the "evidence" in Bayes' rule (p. 333). With q parameterized by θ:
$$\text{ELBO}[\boldsymbol\theta,\boldsymbol\phi]=\int q(\mathbf z|\boldsymbol\theta)\log\Big[\frac{Pr(\mathbf x,\mathbf z|\boldsymbol\phi)}{q(\mathbf z|\boldsymbol\theta)}\Big]d\mathbf z \tag{17.16}$$
We maximize this over both ϕ and θ. The network that computes it is the VAE (pp. 333–334).

### 17.4 ELBO properties (pp. 334–336)
For fixed θ, the ELBO is a function of ϕ lying below the log-likelihood curve. Changing θ modifies this curve, which may move closer to or further from the log-likelihood. Changing ϕ moves along the curve (p. 334; fig. 17.6).

**17.4.1 Tightness (p. 334).** Factor the joint with the definition of conditional probability, $Pr(\mathbf x,\mathbf z|\boldsymbol\phi)=Pr(\mathbf z|\mathbf x,\boldsymbol\phi)Pr(\mathbf x|\boldsymbol\phi)$:
$$\begin{aligned}\text{ELBO}[\boldsymbol\theta,\boldsymbol\phi]&=\int q\log\Big[\frac{Pr(\mathbf z|\mathbf x,\boldsymbol\phi)Pr(\mathbf x|\boldsymbol\phi)}{q}\Big]d\mathbf z\\&=\int q\log[Pr(\mathbf x|\boldsymbol\phi)]d\mathbf z+\int q\log\Big[\frac{Pr(\mathbf z|\mathbf x,\boldsymbol\phi)}{q}\Big]d\mathbf z\\&=\log[Pr(\mathbf x|\boldsymbol\phi)]+\int q\log\Big[\frac{Pr(\mathbf z|\mathbf x,\boldsymbol\phi)}{q}\Big]d\mathbf z\\&=\log[Pr(\mathbf x|\boldsymbol\phi)]-D_{KL}\big[q(\mathbf z|\boldsymbol\theta)\,\|\,Pr(\mathbf z|\mathbf x,\boldsymbol\phi)\big]\end{aligned}\tag{17.17}$$
Here q means q(z|θ). The first integral drops out between lines 3 and 4 because log Pr(x|ϕ) does not depend on z and q integrates to one. The last line uses the definition of KL divergence (p. 334). The KL divergence measures a "distance" between distributions and is never negative. So the ELBO is a lower bound on the log-likelihood. The bound is tight when $q(\mathbf z|\boldsymbol\theta)=Pr(\mathbf z|\mathbf x,\boldsymbol\phi)$, the posterior: which latent values could have produced x (p. 334; fig. 17.7 uses Bayes' rule $Pr(\mathbf z|\mathbf x^*,\boldsymbol\phi)\propto Pr(\mathbf x^*|\mathbf z,\boldsymbol\phi)Pr(\mathbf z)$, p. 335).

*Intuition note:* The gap between the ELBO and the true log-likelihood is exactly how far q is from the true posterior. A better q gives a tighter bound.

**17.4.2 Reconstruction minus KL to the prior (pp. 335–336).** Factor the joint as Pr(x|z,ϕ)Pr(z) instead:
$$\text{ELBO}[\boldsymbol\theta,\boldsymbol\phi]=\int q(\mathbf z|\boldsymbol\theta)\log[Pr(\mathbf x|\mathbf z,\boldsymbol\phi)]d\mathbf z-D_{KL}\big[q(\mathbf z|\boldsymbol\theta)\,\|\,Pr(\mathbf z)\big] \tag{17.18}$$
The first term is the average agreement of latent and data, i.e. reconstruction accuracy. The second measures how well q matches the prior. The VAE uses this form (p. 336).

### 17.5 Variational approximation (p. 336)
The bound is tight when q is the posterior, which Bayes' rule gives:
$$Pr(\mathbf z|\mathbf x,\boldsymbol\phi)=\frac{Pr(\mathbf x|\mathbf z,\boldsymbol\phi)Pr(\mathbf z)}{Pr(\mathbf x|\boldsymbol\phi)} \tag{17.19}$$
In practice this is intractable, because the evidence in the denominator cannot be evaluated. So choose a simple parametric family for q, here a multivariate normal with mean μ and diagonal covariance Σ. It will not always match the posterior well. Training finds the member of the family "closest" to the posterior, which means minimizing the KL in (17.17) and raising the colored curves of fig. 17.6 (p. 336). Because the optimal q depends on x, the approximation does too:
$$q(\mathbf z|\mathbf x,\boldsymbol\theta)=\text{Norm}_{\mathbf z}\big[\mathbf g_{\boldsymbol\mu}[\mathbf x,\boldsymbol\theta],\mathbf g_{\boldsymbol\Sigma}[\mathbf x,\boldsymbol\theta]\big] \tag{17.20}$$
Here g is a second neural network with parameters θ (p. 336). If the true posterior is multi-modal, the Gaussian approximation will be poor (fig. 17.8b, p. 337).

### 17.6 The variational autoencoder (pp. 336–338)
$$\text{ELBO}[\boldsymbol\theta,\boldsymbol\phi]=\int q(\mathbf z|\mathbf x,\boldsymbol\theta)\log[Pr(\mathbf x|\mathbf z,\boldsymbol\phi)]d\mathbf z-D_{KL}\big[q(\mathbf z|\mathbf x,\boldsymbol\theta)\,\|\,Pr(\mathbf z)\big] \tag{17.21}$$
The first term is an expectation under q, so approximate it by sampling (Monte Carlo estimate):
$$\mathbb E_{\mathbf z}[a[\mathbf z]]=\int a[\mathbf z]q(\mathbf z|\mathbf x,\boldsymbol\theta)d\mathbf z\approx\frac1N\sum_{n=1}^N a[\mathbf z_n^*] \tag{17.22}$$
A very approximate estimate uses a single sample z*:
$$\text{ELBO}[\boldsymbol\theta,\boldsymbol\phi]\approx\log[Pr(\mathbf x|\mathbf z^*,\boldsymbol\phi)]-D_{KL}\big[q(\mathbf z|\mathbf x,\boldsymbol\theta)\,\|\,Pr(\mathbf z)\big] \tag{17.23}$$
The KL term between $q=\text{Norm}[\boldsymbol\mu,\boldsymbol\Sigma]$ and the standard normal prior has a closed form (p. 337):
$$D_{KL}\big[q\,\|\,Pr(\mathbf z)\big]=\frac12\Big(\text{Tr}[\boldsymbol\Sigma]+\boldsymbol\mu^T\boldsymbol\mu-D_{\mathbf z}-\log\det[\boldsymbol\Sigma]\Big) \tag{17.24}$$
$D_{\mathbf z}$ is the latent dimension. (Added shapes: $\boldsymbol\mu\in\mathbb R^{D_z}$ and $\boldsymbol\Sigma$ is $D_z\times D_z$, diagonal.)

**17.6.1 Algorithm (p. 338).** To compute the ELBO for a point x:
1. The encoder g[x,θ] gives μ and Σ.
2. Draw a sample z* from q.
3. Evaluate (17.23).

Why the name: it is *variational* because it computes a Gaussian approximation to the posterior. It is an *autoencoder* because x is mapped to a lower-dimensional z (encoder) and then rebuilt (decoder f[z,ϕ]) (p. 338). The loss is the negative ELBO. Training uses mini-batches with SGD or Adam, with gradients from automatic differentiation. Each step moves between the colored curves (θ) and along them (ϕ) (p. 338; fig. 17.10, p. 339).

### 17.7 Reparameterization trick (p. 339)
Differentiating through the sampling step is difficult, yet differentiating past it is necessary to update θ. Move the randomness into a side branch that draws ε* from Norm[0, I]:
$$\mathbf z^*=\boldsymbol\mu+\boldsymbol\Sigma^{1/2}\boldsymbol\epsilon^* \tag{17.25}$$
This gives a sample from the intended Gaussian. Backpropagation need not pass down the stochastic branch (p. 339).

*Intuition note:* Randomness enters as an input, like noise fed in from outside. The path from μ and Σ to the loss is then ordinary, differentiable arithmetic.

### 17.8 Applications (pp. 340–344)
**17.8.1 Approximating sample probability (p. 340).** Pr(x) = E_z[Pr(x|z)] (17.26). A naive Monte Carlo estimate from prior samples is
$$Pr(\mathbf x)\approx\frac1N\sum_n Pr(\mathbf x|\mathbf z_n) \tag{17.27}$$
Because of the curse of dimensionality, almost all prior samples have very low Pr(x|z_n), so an enormous number would be needed (p. 340). *Importance sampling* draws z from an auxiliary q(z) and rescales:
$$Pr(\mathbf x)=\mathbb E_{q(\mathbf z)}\Big[\frac{Pr(\mathbf x|\mathbf z)Pr(\mathbf z)}{q(\mathbf z)}\Big]\approx\frac1N\sum_{n=1}^N\frac{Pr(\mathbf x|\mathbf z_n)Pr(\mathbf z_n)}{q(\mathbf z_n)} \tag{17.28}$$
Since Pr(x|z)Pr(z) is proportional to the posterior, a sensible choice is the encoder's q(z|x). With enough samples this beats the lower bound. It can be used to evaluate test log-likelihood or to flag anomalous examples (pp. 340–341).

**17.8.2 Generation (pp. 341–342).** Sample z from the prior, decode, and add noise. Samples from vanilla VAEs are generally low quality (fig. 17.12a–c). The author gives two partial reasons: the naïve spherical Gaussian noise model, and the Gaussian prior and posterior. One trick is to sample from the *aggregated posterior* $q(\mathbf z|\boldsymbol\theta)=(1/I)\sum_i q(\mathbf z|\mathbf x_i,\boldsymbol\theta)$. It is a mixture of Gaussians, more representative of the true latent distribution. Modern VAEs reach high quality only with hierarchical priors, specialized architectures and regularization (fig. 17.12d). Diffusion models (chapter 18) can be viewed as VAEs with hierarchical priors (p. 342).

**17.8.3 Resynthesis (p. 342).** Project x into latent space by taking the encoder mean, or by optimizing for the z that maximizes the posterior, which is proportional to Pr(x|z)Pr(z). In fig. 17.13, a "neutral → smiling" direction is the difference between the latent means of labeled groups, and similarly for "mouth closed → open". Adding or subtracting these vectors modifies an image. Intermediate images use spherical linear interpolation (Slerp). In 3D this is interpolating along a sphere's surface rather than digging a straight tunnel through it. Encoding, modifying and decoding is called *resynthesis*. GANs can do it too, but have no encoder, so a separate procedure is needed to find z (p. 342).

**17.8.4 Disentanglement (pp. 342–343).** A latent space is *disentangled* when each dimension represents an independent real-world factor. Methods add regularizers on the posterior or the aggregated posterior:
$$L_{\text{new}}=-\text{ELBO}[\boldsymbol\theta,\boldsymbol\phi]+\lambda_1\mathbb E_{Pr(\mathbf x)}\big[r_1[q(\mathbf z|\mathbf x,\boldsymbol\theta)]\big]+\lambda_2 r_2[q(\mathbf z|\boldsymbol\theta)] \tag{17.29}$$
The *beta VAE* upweights the KL term, with β > 1:
$$\text{ELBO}[\boldsymbol\theta,\boldsymbol\phi]\approx\log[Pr(\mathbf x|\mathbf z^*,\boldsymbol\phi)]-\beta\cdot D_{KL}\big[q(\mathbf z|\mathbf x,\boldsymbol\theta)\,\|\,Pr(\mathbf z)\big] \tag{17.30}$$
The prior's dimensions are independent, so upweighting this term encourages less correlated posteriors (p. 343). The *total correlation VAE* adds a term that decreases the total correlation between latent variables. It also maximizes mutual information between a small subset of latents and the observations. On chair images, some dimensions correspond to rotation, size and legs (fig. 17.14, p. 344).

### 17.9 Summary (p. 344)
The likelihood cannot be computed in closed form, so maximize a lower bound. For the bound to be tight, the intractable posterior is needed, so use a variational approximation with parameters from an encoder network. To get high-quality samples, it "seems to be necessary" to use more sophisticated latent distributions than Gaussians, e.g. hierarchical priors (p. 344).

### Notes (pp. 344–347), compressed
- The VAE was introduced by Kingma & Welling (2014) (p. 344).
- A plain autoencoder has a bottleneck but aims at a low-dimensional representation, not a distribution. With linear encoder and decoder it is PCA. Probabilistic PCA adds spherical Gaussian noise and factor analysis adds diagonal Gaussian noise. Making these nonlinear returns the VAE (p. 345).
- The conditional VAE passes class information to encoder and decoder, so the latent space need not encode it (p. 345).
- Posterior collapse: the encoder always predicts the prior. It can be mitigated by gradually increasing the KL term during training (p. 346).
- Blurry reconstructions: Zhao et al. give evidence that they are partly due to the Gaussian noise and partly due to sub-optimal variational posteriors (p. 346).
- Other problems: the "information preference" problem and "holes" in latent space (p. 346).
- The reparameterization trick usually gives a low-variance gradient estimator. The REINFORCE alternative is Problem 17.5 (p. 347).
- EM algorithm: alternately set q to the exact posterior (E-step, tight bound) and maximize over ϕ (M-step). It is viable for mixtures of Gaussians, where the posterior is closed-form. It cannot be used for the nonlinear latent variable model (p. 347).

## Toy example (ours, not from the text)
One observed x and a latent $z\in\{1,2\}$, discrete so the integral becomes a sum. Take prior Pr(z=1)=Pr(z=2)=0.5 and likelihoods Pr(x|z=1)=0.8, Pr(x|z=2)=0.2.
- Evidence: Pr(x) = 0.5·0.8 + 0.5·0.2 = 0.5, so log Pr(x) = ln 0.5 = −0.6931.
- Posterior: Pr(z=1|x) = 0.4/0.5 = 0.8 and Pr(z=2|x) = 0.1/0.5 = 0.2.
- Take q = (0.5, 0.5). ELBO (17.16) = 0.5 ln(0.4/0.5) + 0.5 ln(0.1/0.5) = 0.5(−0.2231) + 0.5(−1.6094) = −0.9163.
- KL[q‖posterior] = 0.5 ln(0.5/0.8) + 0.5 ln(0.5/0.2) = 0.5(−0.4700) + 0.5(0.9163) = 0.2231.
- Check (17.17): −0.6931 − 0.2231 = −0.9163 ✓.
- Check (17.18): E_q log Pr(x|z) = 0.5 ln 0.8 + 0.5 ln 0.2 = −0.9163, and KL[q‖prior] = 0 because q equals the prior, so the ELBO is −0.9163 ✓.
- Take q = posterior (0.8, 0.2). ELBO = 0.8 ln(0.4/0.8) + 0.2 ln(0.1/0.2) = ln 0.5 = −0.6931. The bound is tight.

## Concepts
- [[latent-variable-model]] (new) — model Pr(x,z) with hidden z, get Pr(x) by marginalizing z (p. 327)
- [[nonlinear-latent-variable-model]] (new) — Normal(0,I) prior plus Gaussian likelihood with network mean f[z,ϕ]; the model the VAE helps learn (p. 328)
- [[elbo]] (new) — lower bound on log Pr(x|ϕ) from Jensen's inequality; equals log-likelihood minus KL to the posterior (p. 333)
- [[jensens-inequality]] (new) — for concave g, g[E[y]] ≥ E[g[y]]; used for the log (p. 331)
- [[kl-divergence]] (new) — non-negative "distance" between distributions; zero when they match (p. 334)
- [[variational-approximation]] (new) — replace the intractable posterior by a simple Gaussian predicted by an encoder (p. 336)
- [[vae]] (new) — encoder g[x,θ] plus decoder f[z,ϕ], trained on the negative ELBO (p. 338)
- [[reparameterization-trick]] (new) — z* = μ + Σ^{1/2}ε*, moving the randomness outside the differentiated path (p. 339)
- [[monte-carlo-estimate]] (new) — approximate an expectation by averaging samples (p. 337)
- [[importance-sampling]] (new) — estimate Pr(x) by sampling from auxiliary q and rescaling (p. 340)
- [[aggregated-posterior]] (new) — average of the encoder posteriors over the training data (p. 342)
- [[disentanglement]] (new) — latent dimensions correspond to independent real-world factors (p. 342)
- [[beta-vae]] (new) — VAE whose KL term is multiplied by β > 1 (p. 343)

## Canonical instances
- [[mixture-of-gaussians]] — discrete latent variable giving a multi-modal Pr(x) (p. 328)
- [[vae-celeba-samples]] — vanilla VAE samples look too smooth or too noisy; hierarchical VAEs give high quality (p. 341)
- [[latent-smile-direction]] — resynthesis by vector arithmetic in latent space (p. 342)
- [[total-correlation-vae-chairs]] — latent dimensions for rotation, size, legs (p. 344)

## Bridges (candidates)
- [structural-analogy] ELBO gap equals KL to posterior ↔ llm (cross-entropy / log-loss): both are likelihood-based training objectives, here approximated by a bound.
- [structural-analogy] Diffusion models as hierarchical VAEs (p. 342) ↔ generative modeling: the next chapter's model class.
- [metaphor] Decoder f[z,ϕ] mapping a low-dimensional z to data ↔ llm (residual stream): a compressed internal code that generates outputs.
- [same-math] KL term in ELBO ↔ llm (KL penalty): the same KL divergence between two distributions, though used for a different purpose.

## Questions this raises
- When the true posterior is multi-modal, how much does a single Gaussian q loosen the bound (fig. 17.8b)?
- How would a hierarchical prior change the ELBO derivation?
- How many importance samples (17.28) are needed before the estimate beats the lower bound in practice?
- Can posterior collapse be detected during training, and does annealing the KL term fix it fully?

## Exercises worth doing
- Ex. 17.1 (p. 347) — count and range of parameters in a 1D mixture of Gaussians with 5 components — difficulty: easy
- Ex. 17.2 (p. 348) — show log is concave via its second derivative — difficulty: easy
- Ex. 17.3 (p. 348) — convex x^{2n}; (E[x])² ≤ E[x²] — difficulty: medium
- Ex. 17.4 (p. 348) — derive the ELBO (17.18) from the KL to the true posterior — difficulty: hard
- Ex. 17.5 (p. 348) — REINFORCE / score-function estimator as an alternative to reparameterization — difficulty: medium
- Ex. 17.7 (p. 348) — derive EM for a 1D mixture of Gaussians, with Lagrange multipliers — difficulty: hard

## Reading notes
- Printed page = pdf page − 14 (pdf 341 = p. 327).
- The Jensen figure 17.4 caption writes log[E[y]] > E[log[y]], while the text (17.11) uses ≥. The text's ≥ is the general statement.
- The notation q(z|θ, x) (p. 338) and q(z|x, θ) (p. 336) are used interchangeably.
- Figure 17.15's caption uses h for the latent variable, where the text uses z.
- Equation 17.28 and 17.13 are reproduced from the page images, which agree with the text layer.
- Figures were read from captions. Problems 17.1–17.5 and 17.7 are listed only, not solved; Problem 17.6 is omitted.
