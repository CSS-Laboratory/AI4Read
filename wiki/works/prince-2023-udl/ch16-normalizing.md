---
id: prince-2023-udl/ch16-normalizing
work: prince-2023-udl
unit: "Chapter 16 — Normalizing flows"
pages: 304-326
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
# Normalizing flows

## L0 — One line
A normalizing flow turns a simple base density into a complex one with an invertible deep network, so it can both sample and compute exact likelihoods, at the price that every layer must be invertible and have a cheap Jacobian determinant.

## L1 — The gist (≤ 120 words)
GANs generate samples but define no distribution, so a new example's probability is hard to assess. This chapter asks how to build a generative model that does both. The answer is to push a simple base density (usually a standard normal) through an invertible network. The change-of-variables rule then gives the exact likelihood, which can be maximized directly. Each layer must be invertible, cheap to invert, and have a cheap Jacobian determinant. Linear and elementwise flows are too weak alone. Coupling, autoregressive and residual flows are more expressive. Applications are density modeling, image synthesis (GLOW) and approximating other densities. This matters because flows are the one model in this book with exact log-likelihood.

**Prerequisites:** probability density and change of variables; maximum likelihood; Jacobian and determinant; matrix inverse and triangular matrices; Big-O; KL divergence.

## L2 — Key ideas
- Pushing a base density through a function $f$ stretches or compresses probability. The model density is the base density divided by $|\partial f/\partial z|$ (p. 306, eq. 16.1; p. 307, eq. 16.3).
- Sampling needs the forward (generative) map. Likelihood needs the inverse (normalizing) map. So $f$ must be invertible (p. 306).
- Training minimizes negative log-likelihood. It needs $z_i=f^{-1}[x_i]$ and $\log|\det|$ of the Jacobian. A deep flow's determinant is the product of its layers' determinants (pp. 307–309).
- Four desiderata for layers: expressive, invertible, efficiently invertible, efficient Jacobian determinant (p. 309).
- Linear flows ($\beta+\Omega h$; writing $\Omega$ through an LU decomposition makes them efficient) map a normal to a normal. Elementwise flows cannot correlate variables. Hence coupling flows (one half of the input is copied and the other half is transformed with parameters computed from the copied half), autoregressive flows (each output dimension is computed from the matching input dimension and the earlier ones) and residual flows (layers that add a function of the input to the input) (pp. 310–315).
- Autoregressive flows are fast in one direction and slow in the other. Teacher–student training can combine fast learning and fast (but approximate) sampling (p. 314).
- Residual flows are inverted by reversing the computation (iRevNet, which splits the input into two parts) or by fixed-point iteration (iResNet, which makes each residual layer a contraction mapping). The iResNet log-determinant is approximated with a power series and Hutchinson's trace estimator (a random-vector estimate of a trace) (pp. 315–317).
- Multi-scale flows introduce latent parts at different depths (p. 318). GLOW (a multi-scale coupling flow for images) synthesizes images, but samples are worse than GANs or diffusion (pp. 319–321).
- Reverse KL lets a flow imitate a target density that is easy to evaluate but hard to sample (p. 321).

## L3 — Walkthrough

### Introduction (p. 304)
GANs (chapter 15) pass a latent variable through a network, but they define no distribution over data, so the probability of a new example is not straightforward to assess. Normalizing flows transform a simple distribution into a complicated one with a deep network. They can sample and evaluate probability. The cost is a specialized architecture in which each layer must be invertible (p. 304).

### 16.1 1D example (pp. 304–307)
Start with a tractable base distribution $Pr(z)$ and set $x=f[z,\phi]$. Sampling: draw $z^*$, compute $x^*=f[z^*,\phi]$ (p. 304).

**16.1.1 Measuring probability.** Where $f$ stretches its input, density falls. Where it compresses, density rises, so the total area stays one. Stretching is governed by the size of the gradient (pp. 304, 306, fig. 16.2). The density is

$$Pr(x|\phi)=\left|\frac{\partial f[z,\phi]}{\partial z}\right|^{-1}\cdot Pr(z),\tag{16.1}$$

where $z=f^{-1}[x,\phi]$ created $x$. A derivative above one lowers the probability. A derivative below one raises it (p. 306).

*Intuition note:* Probability mass in a small interval is conserved. If the map spreads the interval over a wider range of $x$, the height (density) must drop. The derivative measures that spreading.

**16.1.2 Forward and inverse.** Sampling needs the forward map. Likelihood needs $z=f^{-1}[x,\phi]$, so $f$ must be invertible. The forward map is the *generative direction*. With a standard normal base, the inverse is the *normalizing direction*, because it turns the complex density into a normal one (p. 306).

**16.1.3 Learning.** With i.i.d. data, maximum likelihood equals minimizing negative log-likelihood (p. 307):

$$\hat\phi=\operatorname*{argmax}_\phi\Big[\prod_{i=1}^{I}Pr(x_i|\phi)\Big]=\operatorname*{argmin}_\phi\Big[\sum_{i=1}^{I}-\log Pr(x_i|\phi)\Big]=\operatorname*{argmin}_\phi\Big[\sum_{i=1}^{I}\log\Big|\frac{\partial f[z_i,\phi]}{\partial z_i}\Big|-\log Pr(z_i)\Big]\tag{16.2}$$

The third line uses eq. 16.1 (p. 307).

### 16.2 General case (pp. 307–309)
Now $\mathbf z\in\mathbb R^D$, $\mathbf x\in\mathbb R^D$ and $\mathbf f$ is a deep network. Sampling is the same two steps (p. 307). Likelihood:

$$Pr(\mathbf x|\phi)=\left|\frac{\partial \mathbf f[\mathbf z,\phi]}{\partial \mathbf z}\right|^{-1}\cdot Pr(\mathbf z)\tag{16.3}$$

The first factor is the inverse of the absolute determinant of the $D\times D$ Jacobian, with element $\partial f_j/\partial z_i$ at position $(i,j)$. The absolute determinant measures the change of volume, as the absolute derivative measured the change of area in 1D (p. 307).

**16.2.1 Deep forward mapping.** The network is a composition of layers (p. 308):

$$\mathbf x=\mathbf f_K\Big[\mathbf f_{K-1}\big[\dots\mathbf f_2[\mathbf f_1[\mathbf z,\phi_1],\phi_2],\dots\phi_{K-1}\big],\phi_K\Big]\tag{16.4}$$

The inverse applies the inverse layers in opposite order:

$$\mathbf z=\mathbf f_1^{-1}\Big[\mathbf f_2^{-1}\big[\dots\mathbf f_{K-1}^{-1}[\mathbf f_K^{-1}[\mathbf x,\phi_K],\phi_{K-1}],\dots\phi_2\big],\phi_1\Big]\tag{16.5}$$

The base density is usually a multivariate standard normal (mean zero, identity covariance). Each inverse layer "flows" the data density toward it, which gives the name (p. 308, fig. 16.4). The Jacobian is a chain of Jacobians:

$$\frac{\partial\mathbf f[\mathbf z,\phi]}{\partial\mathbf z}=\frac{\partial\mathbf f_1[\mathbf z,\phi_1]}{\partial\mathbf z}\cdot\frac{\partial\mathbf f_2[\mathbf f_1,\phi_2]}{\partial\mathbf f_1}\cdots\frac{\partial\mathbf f_K[\mathbf f_{K-1},\phi_K]}{\partial\mathbf f_{K-1}}\tag{16.6}$$

Here $\mathbf f_k$ also denotes the output of layer $k$. The absolute determinant is the product of the layers' absolute determinants (eq. 16.7, pp. 308–309). The inverse mapping's determinant is the reciprocal of the forward one (p. 309). Training uses

$$\hat\phi=\operatorname*{argmax}_\phi\Big[\prod_{i=1}^{I}Pr(\mathbf z_i)\cdot\Big|\frac{\partial\mathbf f[\mathbf z_i,\phi]}{\partial\mathbf z_i}\Big|^{-1}\Big]=\operatorname*{argmin}_\phi\Big[\sum_{i=1}^{I}\log\Big|\frac{\partial\mathbf f[\mathbf z_i,\phi]}{\partial\mathbf z_i}\Big|-\log Pr(\mathbf z_i)\Big]\tag{16.8}$$

with $\mathbf z_i=\mathbf f^{-1}[\mathbf x_i,\phi]$, $Pr(\mathbf z_i)$ under the base density, and the determinant from eq. 16.7 (p. 309).

*Intuition note:* The model's log-likelihood is the base log-density of the encoded point, minus the log of how much each layer stretches space (the log absolute Jacobian determinants). Both terms need the layers' inverse and their Jacobian determinants, which is why the layers are restricted.

**16.2.2 Desiderata (p. 309).** Layers need: (1) together, enough expressiveness to map a standard normal to an arbitrary density; (2) invertibility (a bijection: a unique one-to-one map); (3) efficient inverse (needed at every likelihood evaluation during training); (4) efficient Jacobian determinant, in either direction.

### 16.3 Invertible network layers (pp. 309–318)
Linear and elementwise flows are easy but not expressive enough alone. They are building blocks of the more expressive coupling, autoregressive and residual flows (p. 309).

**16.3.1 Linear flows.** $\mathbf f[\mathbf h]=\beta+\Omega\mathbf h$, invertible if $\Omega$ is. For $\Omega\in\mathbb R^{D\times D}$, inversion and the determinant (the Jacobian's determinant is $|\Omega|$) cost $O[D^3]$, which is expensive for large $D$ (p. 310). Special forms are cheaper but less general (p. 310):
- Diagonal: $O[D]$, but elements of $\mathbf h$ do not interact.
- Orthogonal: easier to invert, fixed determinant, but no scaling of individual dimensions.
- Triangular: inverted by back-substitution in $O[D^2]$. The determinant is the product of the diagonal.

A general and efficient option is the LU parameterization (p. 310):

$$\Omega=\mathbf P\mathbf L(\mathbf U+\mathbf D)\tag{16.9}$$

Here $\mathbf P$ is a predetermined permutation matrix, $\mathbf L$ lower triangular, $\mathbf U$ upper triangular with zero diagonal, and $\mathbf D$ diagonal. Inversion costs $O[D^2]$. The log determinant is the sum of the log absolute values on the diagonals of $\mathbf L$ and $\mathbf D$ (p. 310).

*Limit:* A linear map of $\mathrm{Norm}_{\mathbf h}[\mu,\Sigma]$ is normal with mean $\beta+\Omega\mu$ and covariance $\Omega\Sigma\Omega^T$. So linear flows alone cannot map a normal to an arbitrary density (p. 310).

**16.3.2 Elementwise flows.** Apply the same pointwise function with parameters $\phi$ to each element (p. 310):

$$\mathbf f[\mathbf h]=\big[f[h_1,\phi],f[h_2,\phi],\dots f[h_D,\phi]\big]^T\tag{16.10}$$

The Jacobian is diagonal, so

$$\left|\frac{\partial\mathbf f[\mathbf h]}{\partial\mathbf h}\right|=\prod_{d=1}^{D}\left|\frac{\partial f[h_d]}{\partial h_d}\right|\tag{16.11}$$

$f$ may be a fixed invertible nonlinearity (e.g. leaky ReLU) or a parameterized invertible map (p. 310). Example: piecewise linear map on $[0,1]$ with $K$ equal bins (fig. 16.5):

$$f[h,\phi]=\Big(\sum_{k=1}^{b-1}\phi_k\Big)+(hK-b+1)\phi_b\tag{16.12}$$

The $\phi_k$ are positive and sum to 1, and $b=\lfloor Kh\rfloor+1$ is the bin containing $h$. The first term sums the preceding bins. The second is the proportion of the way through the current bin. It is easy to invert, and its gradient exists almost everywhere. Smoother versions use monotonic splines (p. 311). Elementwise flows do not mix dimensions, so they cannot create correlations. Alternated with linear flows they can model more. In practice they are components of coupling flows (p. 311).

**16.3.3 Coupling flows.** Split $\mathbf h=[\mathbf h_1^T,\mathbf h_2^T]^T$ (pp. 311–312):

$$\mathbf h_1'=\mathbf h_1,\qquad \mathbf h_2'=\mathbf g\big[\mathbf h_2,\phi[\mathbf h_1]\big]\tag{16.13}$$

$\mathbf g$ is an elementwise flow (or other invertible layer). Its parameters $\phi[\mathbf h_1]$ come from a network that need not be invertible. Inversion:

$$\mathbf h_1=\mathbf h_1',\qquad \mathbf h_2=\mathbf g^{-1}\big[\mathbf h_2',\phi[\mathbf h_1]\big]\tag{16.14}$$

If $\mathbf g$ is elementwise, the Jacobian is lower triangular. It has the identity in the top-left block and the elementwise derivatives in the bottom-right. Its determinant is the product of the diagonal values (p. 312). Only the second half is transformed, in a way that depends on the first. So elements are shuffled by permutation matrices between layers. These are initialized randomly and frozen, because they are difficult to learn. For images, channels are split in halves and permuted with $1\times1$ convolutions (p. 312).

**16.3.4 Autoregressive flows.** Each dimension is its own block (p. 313):

$$h_d'=g\big[h_d,\phi[\mathbf h_{1:d-1}]\big]\tag{16.15}$$

$g$ is called the *transformer* (footnote: unrelated to chapter 12's transformer layers). The $\phi$'s are *conditioners*. $g$ must be invertible. Conditioners can be any form, usually neural networks. If transformer and conditioner are sufficiently flexible, autoregressive flows are universal approximators, able to represent any probability distribution (p. 313). With masks, so that $\phi$ at position $d$ depends only on earlier positions, all outputs can be computed in parallel. This is a *masked autoregressive flow*, with a principle similar to masked self-attention (pp. 313–314). Forward (eq. 16.16): $h_1'=g[h_1,\phi]$, $h_2'=g[h_2,\phi[h_1]]$, $h_3'=g[h_3,\phi[h_{1:2}]]$, $h_4'=g[h_4,\phi[h_{1:3}]]$. Inverse (eq. 16.17): $h_1=g^{-1}[h_1',\phi]$, $h_2=g^{-1}[h_2',\phi[h_1]]$, $h_3=g^{-1}[h_3',\phi[h_{1:2}]]$, $h_4=g^{-1}[h_4',\phi[h_{1:3}]]$. The inverse must be computed sequentially, since $h_d$ needs $h_{1:d-1}$, so it is slow for large inputs (p. 314).

**16.3.5 Inverse autoregressive flows.** A masked autoregressive flow is defined in the normalizing direction. Likelihood and training are efficient, but sampling is slow. Using an autoregressive flow as the forward map gives fast sampling but slow likelihood and training. This is an *inverse autoregressive flow*. A trick: train a masked autoregressive flow (teacher), then use it to train an inverse autoregressive flow (student) for efficient but approximate sampling. This needs learning from a function rather than samples (see 16.5.3) (p. 314).

*Intuition note:* Autoregressive structure makes one direction parallel (all dimensions at once) and the other sequential (each needs the previous ones). You pick which direction to make fast, or use teacher–student to get fast learning and fast (but approximate) sampling.

**16.3.6 Residual flows: iRevNet.** Split as in coupling (pp. 314–315):

$$\mathbf h_1'=\mathbf h_1+\mathbf f_1[\mathbf h_2,\phi_1],\qquad \mathbf h_2'=\mathbf h_2+\mathbf f_2[\mathbf h_1',\phi_2]\tag{16.18}$$

$\mathbf f_1,\mathbf f_2$ need not be invertible. Inverse by reversing the order:

$$\mathbf h_2=\mathbf h_2'-\mathbf f_2[\mathbf h_1',\phi_2],\qquad \mathbf h_1=\mathbf h_1'-\mathbf f_1[\mathbf h_2,\phi_1]\tag{16.19}$$

Inputs are permuted between layers. For general $\mathbf f_1,\mathbf f_2$ there is no efficient Jacobian. The form is sometimes used to save memory when training residual networks, because stored activations are unnecessary (p. 315).

**16.3.7 Residual flows and contraction mappings: iResNet.** The Banach fixed point (contraction mapping) theorem states that every contraction mapping has a fixed point. A contraction mapping satisfies

$$\mathrm{dist}\big[f[z'],f[z]\big]<\beta\cdot\mathrm{dist}[z',z]\quad\forall z,z',\tag{16.20}$$

with $0<\beta<1$. Iterating such a function converges to a fixed point $f[z]=z$. Reason: the fixed point stays put, the distance to it shrinks, so the current point approaches it (p. 316, fig. 16.9). To invert $y=z+f[z]$ (eq. 16.21) when $f$ is a contraction, pick any $z_0$ and iterate $z_{k+1}=y^*-f[z_k]$. Its fixed point satisfies $z+f[z]=y^*$ (p. 316).

The same works for layers $\mathbf h'=\mathbf h+\mathbf f[\mathbf h,\phi]$ if $\mathbf f$ is a contraction, i.e. its Lipschitz constant is below one. If activation slopes are at most one, this is equivalent to the largest singular value of each weight matrix $\Omega$ being below one. A crude method is clipping weights to small magnitudes (pp. 316–317).

The Jacobian determinant is hard, but its log can be approximated (p. 317):

$$\log\Big|\mathbf I+\frac{\partial\mathbf f[\mathbf h,\phi]}{\partial\mathbf h}\Big|=\operatorname{trace}\Big[\log\Big[\mathbf I+\frac{\partial\mathbf f}{\partial\mathbf h}\Big]\Big]=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}\operatorname{trace}\Big[\frac{\partial\mathbf f}{\partial\mathbf h}\Big]^k\tag{16.22}$$

The first line uses $\log|\mathbf A|=\operatorname{trace}[\log\mathbf A]$. The second expands a power series. Even truncated, the traces are expensive. So *Hutchinson's trace estimator* is used: for $\epsilon$ normal with mean $\mathbf 0$ and variance $\mathbf I$,

$$\begin{aligned}\operatorname{trace}[\mathbf A]&=\operatorname{trace}[\mathbf A\,\mathbb E[\epsilon\epsilon^T]]=\operatorname{trace}[\mathbb E[\mathbf A\epsilon\epsilon^T]]=\mathbb E[\operatorname{trace}[\mathbf A\epsilon\epsilon^T]]\\&=\mathbb E[\operatorname{trace}[\epsilon^T\mathbf A\epsilon]]=\mathbb E[\epsilon^T\mathbf A\epsilon]\end{aligned}\tag{16.23}$$

Justifications: $\mathbb E[\epsilon\epsilon^T]=\mathbf I$; properties of expectation; linearity of trace; invariance of trace to cyclic permutation; the last argument is a scalar (p. 317). Estimate with $I$ samples:

$$\operatorname{trace}[\mathbf A]=\mathbb E[\epsilon^T\mathbf A\epsilon]\approx\frac1I\sum_{i=1}^{I}\epsilon_i^T\mathbf A\epsilon_i\tag{16.24}$$

This approximates the traces of the powers in eq. 16.22 and hence the log probability (p. 317).

**16.4 Multi-scale flows.** The latent space must equal the data space in size, yet data often need fewer variables. It is inefficient to pass all variables through the whole network (pp. 317–318). Generative direction: partition $\mathbf z=[\mathbf z_1,\dots,\mathbf z_N]$. $\mathbf z_1$ passes through reversible layers of its own size. Later partitions are appended at later points until the size equals $\mathbf x$. In the normalizing direction, when the point where $\mathbf z_n$ was added is reached, that part is assessed against the base distribution (p. 318, fig. 16.10).

### 16.5 Applications (pp. 318–322)
**16.5.1 Modeling densities.** The author states that, of the four generative models in the book, normalizing flows is the only one that computes the exact log-likelihood. GANs are not probabilistic. VAEs and diffusion models return only a lower bound (pp. 318–319). Footnote: the diffusion bound can exceed the flow's exact value, but generation is much slower (p. 319). Fig. 16.11 shows iResNet densities on toy 2D data. Use for anomaly detection: fit a flow to clean data and flag low-probability examples. Caution: outliers with high probability may lie outside the typical set (p. 319).

**16.5.2 Synthesis (GLOW).** Described in the normalizing direction (p. 319):
- Input is a $256\times256\times3$ RGB tensor.
- Coupling layers split the channels in halves. The second half gets an affine transform at each spatial position, with parameters from a 2D CNN run on the other half.
- Coupling layers alternate with $1\times1$ convolutions parameterized by LU decomposition, which mix channels.
- Periodically, each $2\times2$ patch becomes one position with four times the channels, halving the resolution.
- GLOW is multi-scale: some channels periodically become part of $\mathbf z$.
- Noise is added to the discrete inputs (*dequantization*) to stop the training likelihood rising without bound.

For more realistic samples, GLOW samples from the base density raised to a positive power. This favors the centre over the tails, like the GAN truncation trick. Samples are not as good as GANs or diffusion models. It is unknown whether this is a fundamental restriction of invertible layers or reflects less research effort (pp. 319–321, fig. 16.12). Interpolation: encode two real images, interpolate linearly in latent space, decode. The results interpolate realistically (p. 321, fig. 16.13).

**16.5.3 Approximating other densities.** A flow (*student*, $Pr(\mathbf x|\phi)$) can approximate a target $q(\mathbf x)$ (*teacher*) that is easy to evaluate but hard to sample. Generate $\mathbf x_i=\mathbf f[\mathbf z_i,\phi]$. Since $\mathbf z_i$ is known, the student likelihood needs no inversion, so a masked autoregressive flow can be used. The loss is the reverse KL divergence (p. 321, fig. 16.14):

$$\hat\phi=\operatorname*{argmin}_\phi\Big[\mathrm{KL}\Big[\frac1I\sum_{i=1}^{I}\delta\big[\mathbf x-\mathbf f[\mathbf z_i,\phi]\big]\,\Big\|\,q(\mathbf x)\Big]\Big]\tag{16.25}$$

The usual maximum-likelihood use relies on the cross-entropy term of the forward KL (section 5.7):

$$\hat\phi=\operatorname*{argmin}_\phi\Big[\mathrm{KL}\Big[\frac1I\sum_{i=1}^{I}\delta[\mathbf x-\mathbf x_i]\,\Big\|\,Pr(\mathbf x_i,\phi)\Big]\Big]\tag{16.26}$$

Flows can model the VAE posterior this way (chapter 17) (p. 321).

### 16.6 Summary (pp. 321–322)
Flows evaluate likelihood exactly and generate samples, but each layer must be invertible. It is important that the Jacobian can be estimated efficiently to evaluate the likelihood, which must be done repeatedly to learn the density. Invertible layers are useful even without an efficient Jacobian: they reduce training memory for a $K$-layer network from $O[K]$ to $O[1]$ (p. 322).

### Notes (pp. 322–325), brief
- Flows were first introduced by Rezende & Mohamed (2015). In a quantitative comparison reported by Kobyzev et al. (2020), Flow++ performed best at the time (pp. 322–323).
- Planar and radial flows have no easy inverse (p. 323).
- Elementwise and coupling functions must be monotone to be invertible (p. 324).
- Coupling flows can be seen as autoregressive: a series of $D$ coupling flows can form an autoregressive flow by growing $\mathbf h_1$ by one each layer. Whether coupling flows are universal with fewer than $D$ layers is not known (p. 325).
- Neural ODEs extend residual flows to infinitesimal steps and do not need the Jacobian (p. 325).

## Toy example (ours, not from the text)
Piecewise linear flow, eq. 16.12, with $K=2$, $\phi=(0.8,0.2)$ and base density $Pr(h)=1$ on $[0,1]$.

- Forward, $h=0.25$: $b=\lfloor0.5\rfloor+1=1$. $f=0+(0.25\cdot2-1+1)\cdot0.8=0.5\cdot0.8=0.4$.
- Forward, $h=0.75$: $b=\lfloor1.5\rfloor+1=2$. $f=0.8+(1.5-2+1)\cdot0.2=0.8+0.1=0.9$.
- Slope in bin $b$ is $K\phi_b$ (added step: differentiate eq. 16.12 in $h$). Bin 1: $2\cdot0.8=1.6$. Bin 2: $2\cdot0.2=0.4$.
- Eq. 16.1: $Pr(x=0.4)=1/1.6=0.625$. $Pr(x=0.9)=1/0.4=2.5$.
- Check mass: $x\in[0,0.8]$ has density $0.625$, so mass $0.8\cdot0.625=0.5$. $x\in[0.8,1]$ has density $2.5$, so mass $0.2\cdot2.5=0.5$. Total $1$.
- Inverse of $x=0.9$: $x>0.8$ so bin 2. $0.8+(2h-1)\cdot0.2=0.9$ gives $2h-1=0.5$, so $h=0.75$. This recovers the input.
- Per-example loss term (eq. 16.2): $\log1.6-\log1=0.470$ for $x=0.4$.

## Concepts
- [[normalizing-flow]] (new) — generative model: base density pushed through an invertible network; exact likelihood plus sampling (p. 304)
- [[change-of-variables-density]] (new) — model density = base density divided by absolute Jacobian determinant (pp. 306–307)
- [[jacobian-determinant]] (new) — volume change of the map; product over layers (pp. 307–309)
- [[invertible-layer]] (new) — bijective layer with efficient inverse and determinant (p. 309)
- [[coupling-flow]] (new) — copies one half, transforms the other with parameters computed from the copied half (p. 312)
- [[autoregressive-flow]] (new) — output $d$ depends on inputs $1{:}d$; fast in one direction, sequential in the other (p. 313)
- [[residual-flow]] (new) — invertible residual layers, by reversal (iRevNet) or fixed-point iteration (iResNet) (pp. 314–316)
- [[multi-scale-flow]] (new) — latent parts introduced at different depths (p. 318)
- [[hutchinson-trace-estimator]] (new) — estimates trace by $\mathbb E[\epsilon^T A\epsilon]$ with random $\epsilon$ (p. 317)
- [[causal masking]] — masking in masked autoregressive flows is likened to masked self-attention (pp. 313–314)
- [[cross-entropy / log-loss]] — negative log-likelihood training objective (p. 307)

## Canonical instances
- [[glow-model]] (new) — multi-scale coupling flow with $1\times1$ LU convolutions for faces (pp. 319–320)
- [[irevnet-iresnet]] (new) — two residual-flow designs (pp. 314–316)
- [[parallel-wavenet-style-distillation]] (new) — teacher–student training of an inverse autoregressive flow (pp. 314, 324)

## Bridges (candidates)
- [structural-analogy] Masked autoregressive flow ↔ llm: causal masking in self-attention, which prunes dependence on later positions (p. 314)
- [structural-analogy] Autoregressive conditioning $\phi[h_{1:d-1}]$ ↔ llm: next-token factorization $p(x_t|x_{<t})$, with sequential generation versus parallel scoring
- [structural-analogy] Flow training by negative log-likelihood ↔ llm: cross-entropy minimization, here with an added log-determinant term
- [metaphor] Normalizing direction ↔ encoding data to a simple latent code; interpolation in latent space (p. 321)

## Questions this raises
- Why do flow samples look worse than GAN or diffusion samples: a limit of invertibility, or less research (p. 321)?
- Can coupling flows be universal with fewer than $D$ layers (p. 325)?
- How should high-probability outliers outside the typical set be handled in anomaly detection (p. 319)?
- How much bias does truncating the power series in eq. 16.22 introduce (p. 325)?

## Exercises worth doing
- Ex. 16.1 (p. 325) — change of variables for $x=z^2$ with uniform base — difficulty: easy
- Ex. 16.4 (p. 326) — invert and take determinants of diagonal and triangular matrices — difficulty: easy
- Ex. 16.6 (p. 326) — affine map of a normal using eq. 16.30 — difficulty: medium
- Ex. 16.7 (p. 326) — inverse and determinant for the leaky ReLU flow — difficulty: easy
- Ex. 16.10 (p. 326) — Jacobian sparsity of a residual flow — difficulty: medium
- Ex. 16.11 (p. 326) — reverse KL, unnormalized $q$, invertibility — difficulty: hard

## Reading notes
- Printed page = pdf − 14.
- Text layer is garbled in equations. All equations were checked against the page images.
- Eq. 16.26 prints the model as $Pr(\mathbf x_i,\phi)$ where $Pr(\mathbf x|\phi)$ seems intended; this is reproduced as printed.
- Eq. 16.24 uses $I$ both for the sample count and (in 16.23) the identity matrix.
- Section 16.3.5 correctly points to "section 16.5.3" for teacher–student training. The Notes refer to the LU parameterization as being in "section 16.5.2", but it is described in 16.3.1 and mentioned in 16.5.2.
- Notes pages (322–325) are summarized only briefly. Problems on pp. 325–326 are listed but not solved.
