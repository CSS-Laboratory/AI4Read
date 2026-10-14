---
id: mackay-2003-information/ch34-independent
work: mackay-2003-information
unit: "34 Independent Component Analysis and Latent Variable Modelling"
pages: 437-444
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Independent Component Analysis and Latent Variable Modelling

## L0 — One line
Independent component analysis (ICA) is maximum-likelihood fitting of a noise-free linear latent variable model with independent, non-Gaussian sources, and a covariant (unit-independent, natural-gradient) update makes it simple and fast.

## L1 — The gist (≤ 120 words)
How can we recover hidden independent source signals $\mathbf s$ from observations $\mathbf x = \mathbf{Gs}$ when $\mathbf G$ is unknown? MacKay writes the likelihood, differentiates it, and gets a learning rule. The assumed source distribution $p_i$ defines the nonlinearity $\phi$. Gaussian sources give a rotation-invariant model that cannot recover the sources, so non-Gaussian, often heavier-tailed, priors such as $1/\cosh$ are used. Plain steepest ascent is ill-conditioned (slow) and not covariant (its result depends on the units used), so he builds a covariant rule from an approximate curvature. That rule needs no matrix inversion. The chapter ends with infinite mixture models and exercises.

**Prerequisites:** matrix inverse and determinant; partial derivatives; likelihood and marginalization; delta function; gradient ascent; Gaussian distribution.

## L2 — Key ideas (5–10 bullets)
- Latent variable models describe observables through hidden variables with a simple, often separable, distribution. Decoding an error-correcting code can be viewed this way, but there $\mathbf G$ is normally known in advance (p. 437).
- ICA assumes $\mathbf x=\mathbf{Gs}$ with no noise, independent sources, and (for the simplest algorithm) $I=J$. This makes the likelihood a determinant term plus a sum of log source densities (p. 438).
- Maximum likelihood gives $\Delta\mathbf W\propto[\mathbf W^{\mathsf T}]^{-1}+\mathbf{zx}^{\mathsf T}$, with $z_i=d\ln p_i/da_i$ (p. 439).
- Gaussian sources give a rotation-invariant model, so the linear (Gaussian) algorithm will never recover the sources. The only hope is non-Gaussian sources (often with heavier tails); $\phi=-\tanh$ implies $p\propto1/\cosh$ (p. 439).
- Steepest ascent is dimensionally inconsistent (not covariant) and ill-conditioned. A rule of the form (34.20) is covariant if $\mathbf M$ is positive definite with the right dimensions; two sources of such an $\mathbf M$ are metrics and curvatures (p. 441).
- Dropping the data-dependent curvature term leaves a matrix that is not positive definite. MacKay therefore approximates the data-dependent term to get $\Delta W_{ij}=\eta(W_{ij}+x'_jz_i)$, with no matrix inversion (pp. 442–443).
- MacKay would like infinite (possibly hierarchical) mixture models in which new clusters can always arise. Most of the ideas he cites build on the Dirichlet process (pp. 443–444).

## L3 — Walkthrough

### 34.1 Latent variable models (p. 437)
- A generative model specifies a full probability density over all variables. Latent variables are hidden variables used to describe the distribution of the observables (p. 437).
- Examples: mixture models (latent variables = unknown class labels), hidden Markov models, factor analysis (p. 437).
- Error-correcting code decoding can also be seen this way. The $K$ source bits are latent and $\mathbf G$ is the generator matrix. There $\mathbf G$ is normally known in advance. In latent variable modelling the equivalent parameters are usually unknown and are inferred together with $\mathbf s$ (p. 437).
- Fitting such a model gives a description in terms of "independent components". ICA is perhaps the simplest latent variable model with continuous latent variables (p. 437).

### 34.2 The generative model for ICA (pp. 437–440)
**Model.** $N$ observations $\{\mathbf x^{(n)}\}$; each $J$-dimensional $\mathbf x$ is a linear mixture of $I$ sources:
$$\mathbf x=\mathbf{Gs}\tag{34.1}$$
$\mathbf G$ is unknown. The simplest algorithm assumes $I=J$. The aim is to recover $\mathbf s$ up to multiplicative factors and possible permutation. Equivalently, we want $\mathbf G^{-1}$ up to a post-multiplicative factor. Sources are independent with $P(s_i\mid\mathcal H)\equiv p_i(s_i)$, where $\mathcal H$ is the assumed model form and source distributions (p. 437).

**Joint probability** (p. 438):
$$P(\{\mathbf x^{(n)},\mathbf s^{(n)}\}\mid \mathbf G,\mathcal H)=\prod_n\big[P(\mathbf x^{(n)}\mid\mathbf s^{(n)},\mathbf G,\mathcal H)P(\mathbf s^{(n)}\mid\mathcal H)\big]\tag{34.2}$$
$$=\prod_n\Big[\Big(\prod_j\delta\big(x^{(n)}_j-\textstyle\sum_iG_{ji}s^{(n)}_i\big)\Big)\Big(\prod_i p_i(s^{(n)}_i)\Big)\Big]\tag{34.3}$$
$\mathbf x$ is generated without noise. This is not usually assumed, since noise-free data are rare, but it makes inference far simpler (p. 438).

**Likelihood.** $P(D\mid\mathbf G,\mathcal H)=\prod_nP(\mathbf x^{(n)}\mid\mathbf G,\mathcal H)$ (34.4). Each factor marginalizes over the latent variables. Use $\int ds\,\delta(x-vs)f(s)=\frac1v f(x/v)$ and the summation convention (p. 438):
$$P(\mathbf x^{(n)}\mid\mathbf G,\mathcal H)=\int d^I\mathbf s\,P(\mathbf x\mid\mathbf s,\mathbf G,\mathcal H)P(\mathbf s\mid\mathcal H)\tag{34.5}$$
$$=\int d^I\mathbf s\prod_j\delta\big(x_j-G_{ji}s_i\big)\prod_ip_i(s_i)\tag{34.6}$$
$$=\frac1{|\det\mathbf G|}\prod_ip_i(G^{-1}_{ij}x_j)\tag{34.7}$$
$$\Rightarrow\ \ln P(\mathbf x^{(n)}\mid\mathbf G,\mathcal H)=-\ln|\det\mathbf G|+\sum_i\ln p_i(G^{-1}_{ij}x_j)\tag{34.8}$$
With $\mathbf W\equiv\mathbf G^{-1}$ (and $\det\mathbf W>0$ assumed, so the absolute value is dropped):
$$\ln P(\mathbf x^{(n)}\mid\mathbf G,\mathcal H)=\ln\det\mathbf W+\sum_i\ln p_i(W_{ij}x_j)\tag{34.9}$$
Identities needed (p. 438):
$$\frac{\partial}{\partial G_{ji}}\ln\det\mathbf G=G^{-1}_{ij}=W_{ij}\tag{34.10}$$
$$\frac{\partial}{\partial G_{ji}}G^{-1}_{lm}=-G^{-1}_{lj}G^{-1}_{im}=-W_{lj}W_{im}\tag{34.11}$$
$$\frac{\partial}{\partial W_{ij}}f=-G_{jm}\Big(\frac{\partial}{\partial G_{lm}}f\Big)G_{li}\tag{34.12}$$

**Gradient.** Define $a_i\equiv W_{ij}x_j$, $\phi_i(a_i)\equiv d\ln p_i(a_i)/da_i$ (34.13), and $z_i=\phi_i(a_i)$. This shows in which direction $a_i$ must change to make the data more probable (pp. 438–439).
$$\frac{\partial}{\partial G_{ji}}\ln P(\mathbf x^{(n)}\mid\mathbf G,\mathcal H)=-W_{ij}-a_iz_{i'}W_{i'j}\tag{34.14}$$
$$\frac{\partial}{\partial W_{ij}}\ln P(\mathbf x^{(n)}\mid\mathbf G,\mathcal H)=G_{ji}+x_jz_i\tag{34.15}$$
Ascending the gradient in $\mathbf W$ gives the learning rule
$$\Delta\mathbf W\propto[\mathbf W^{\mathsf T}]^{-1}+\mathbf{zx}^{\mathsf T}\tag{34.16}$$
Algorithm 34.2 (online): for each $\mathbf x$, compute $\mathbf a=\mathbf{Wx}$, then $z_i=\phi_i(a_i)$ (popular choice $\phi=-\tanh$), then update by (34.16) (p. 439).

*Intuition note.* The $[\mathbf W^{\mathsf T}]^{-1}$ term comes from the $\ln\det\mathbf W$ part of the log likelihood. The $\mathbf{zx}^{\mathsf T}$ term comes from the log source densities: $z_i$ shows in which direction $a_i$ must change to make the data more probable.

**Choices of $\phi$ (pp. 439–440).** $\phi$ defines the assumed source distribution.
- Linear $\phi_i=-\kappa a_i$ implies a Gaussian. A Gaussian is invariant under rotation of the latent space, so no evidence favours any alignment. The linear algorithm will never recover $\mathbf G$ or the sources. The only hope is non-Gaussian sources. Most real sources are non-Gaussian, often with heavier tails (p. 439).
- $\phi_i=-\tanh(a_i)$ (34.17) implies $p_i(s_i)\propto1/\cosh(s_i)\propto1/(e^{s_i}+e^{-s_i})$ (34.18), which is heavier-tailed than a Gaussian (p. 439).
- Gain $\beta$: $\phi_i=-\tanh(\beta a_i)$ implies $p_i\propto1/[\cosh(\beta s_i)]^{1/\beta}$. For large $\beta$ this becomes biexponential, $\propto\exp(-|s|)$. As $\beta\to0$ it approaches a zero-mean Gaussian with variance $1/\beta$. Student and Cauchy distributions are heavier-tailed options (p. 440).

**Example distributions (Fig. 34.3, p. 440).** The figure shows distributions over two observables from $1/\cosh$ sources for $\mathbf G=\begin{bmatrix}3/4&1/2\\1/2&1\end{bmatrix}$ and $\begin{bmatrix}2&-1\\-1&3/2\end{bmatrix}$, and for Cauchy sources. Learning fits this shape to the data to maximize likelihood. The Cauchy case, being more heavy-tailed, shows most clearly how the predictive distribution depends on $\mathbf G$ (p. 440).

### 34.3 A covariant, simpler, faster algorithm (pp. 440–443)
- The algorithm so far is slow even on toy data. It is ill-conditioned, and it involves a matrix inverse that can be arbitrarily large or undefined. The general lesson: finding a gradient is splendid, but ascending it directly may not be (p. 440).

**Covariant optimization (p. 441).** The principle of covariance says a consistent algorithm should give the same results independent of the units in which quantities are measured. Steepest descent
$$\Delta w_i=\eta\,\partial L/\partial w_i\tag{34.19}$$
is dimensionally inconsistent: the left side has dimensions $[w_i]$, the right $1/[w_i]$. It is not covariant under linear rescaling of $\mathbf w$. If $\eta$ falls as $1/n$ in online learning, the Munro–Robbins theorem (as cited by MacKay) shows asymptotic convergence to the maximum likelihood parameters, but possibly after very many iterations. The defence "$\eta$ is a dimensional constant" fails if the $w_i$ have different dimensions (p. 441). A covariant form is
$$\Delta w_i=\eta\sum_{i'}M_{ii'}\frac{\partial L}{\partial w_{i'}}\tag{34.20}$$
with $\mathbf M$ positive definite and $M_{ii'}$ of dimensions $[w_iw_{i'}]$. (The source prints the derivative index as $w_i$; with the sum over $i'$ it should read $w_{i'}$.) Two sources of $\mathbf M$ are metrics and curvatures (p. 441).
- **Metric:** if a quadratic metric defines vector length, $\mathbf M$ comes from its quadratic form. For length $\mathbf w^2$, $\mathbf M=\mathbf I$ and steepest descent is appropriate (p. 441).
- **Curvature:** let $\mathbf A\equiv-\nabla\nabla L$. Then $\mathbf M=\mathbf A^{-1}$ is covariant. It is the Newton algorithm, which eases slow convergence when the objective is ill-conditioned. It converges in one step if $L$ is quadratic (p. 441).
- If the curvature has data-dependent and data-independent parts, one may define the metric from the data-independent part only (Gull, 1989). The result is covariant but not an exact Newton step. There is no unique covariant algorithm, but covariant algorithms are a small subset of all algorithms (p. 441).

**Back to ICA (p. 442).** Steepest ascent in $\mathbf W$ is not covariant. The second derivative of the log likelihood w.r.t. $\mathbf W$ has two terms:
$$\frac{\partial G_{ji}}{\partial W_{kl}}=-G_{jk}G_{li}\quad\text{(data-independent)}\tag{34.21}$$
$$\frac{\partial(z_ix_j)}{\partial W_{kl}}=x_jx_l\delta_{ik}z'_i\quad\text{(data-dependent; no sum over }i)\tag{34.22}$$
- Using only the first term, $[\mathbf M^{-1}]_{(ij)(kl)}=[G_{jk}G_{li}]$, is tempting. But this matrix is not positive definite (at least one non-positive eigenvalue). It is a poor curvature approximation, because the log-likelihood curvature must be positive definite near a maximum (p. 442).
- So consult the data-dependent term. The aim is a convenient curvature approximation and a covariant algorithm, not necessarily an exact Newton step. If the true matrix is $\mathbf G^*$:
$$\langle x_jx_l\delta_{ik}z'_i\rangle=\langle G^*_{jm}s_ms_nG^*_{ln}\delta_{ik}z'_i\rangle\tag{34.23}$$
- "Several severe approximations": replace $\mathbf G^*$ by the current $\mathbf G$, and replace $\langle s_ms_nz'_i\rangle$ by $\langle s_ms_n\rangle\langle z'_i\rangle\equiv\Sigma_{mn}D_i$. Here $\Sigma$ is the latent variance–covariance matrix, and $D_i$ is the typical value of $d^2\ln p_i(a)/da^2$. Independent sources make $\Sigma$ and $\mathbf D$ diagonal (p. 442).
$$[\mathbf M^{-1}]_{(ij)(kl)}=G_{jm}\Sigma_{mn}G_{ln}\delta_{ik}D_i\tag{34.24}$$
$$M_{(ij)(kl)}=W_{mj}\Sigma^{-1}_{mn}W_{nl}\delta_{ik}D_i^{-1}\tag{34.25}$$
- Assume similar sources, so $\Sigma$ and $\mathbf D$ are homogeneous with $\Sigma D=1$. The result is covariant under linear rescaling of the data $\mathbf x$, but not of the latent variables:
$$M_{(ij)(kl)}=W_{mj}W_{ml}\delta_{ik}\tag{34.26}$$
- Multiplying by the gradient (34.15):
$$\Delta W_{ij}=\eta\big(W_{ij}+W_{i'j}a_{i'}z_i\big)\tag{34.27}$$
This needs no inversion of $\mathbf W$. After $\mathbf z$, only one backward pass is needed: $x'_j=W_{i'j}a_{i'}$ (34.28), giving
$$\Delta W_{ij}=\eta\big(W_{ij}+x'_jz_i\big)\tag{34.29}$$
(p. 443). The bracket is "sometimes called the natural gradient" (p. 443). Algorithm 34.4: $\mathbf a=\mathbf{Wx}$; $z_i=\phi_i(a_i)$; $\mathbf x'=\mathbf W^{\mathsf T}\mathbf a$; $\Delta\mathbf W\propto\mathbf W+\mathbf{zx}'^{\mathsf T}$ (p. 443).

*(added step)* From (34.26), $\Delta\mathbf W=\eta\,(\text{gradient})\,\mathbf W^{\mathsf T}\mathbf W$, because $\sum_mW_{mj}W_{ml}=(\mathbf W^{\mathsf T}\mathbf W)_{jl}$. With gradient $[\mathbf W^{\mathsf T}]^{-1}+\mathbf{zx}^{\mathsf T}$ this gives $\mathbf W+\mathbf z(\mathbf W^{\mathsf T}\mathbf a)^{\mathsf T}$, which is (34.29).

*Intuition note.* Multiplying the gradient by $\mathbf W^{\mathsf T}\mathbf W$ makes the step respect the units of the data. It also cancels the matrix inverse, so the rule is cheaper and better behaved.

### Further reading and infinite models (pp. 443–444)
- ICA was originally derived by information maximization (Bell and Sejnowski, 1995). Other views and generalizations: energy functions (Hinton et al., 2001); Pearlmutter and Parra; variational free energy (Miskin and MacKay); blind separation references (p. 443).
- Often our beliefs are best captured by a very large number of latent variables. Example: a cluster model of words for speech recognition. The number of possible words is unbounded, so we would like a model in which it is always possible for new clusters to arise. A word's cluster may itself contain clusters (speaker sex, region, accent, down to villages, streets or families), so some hierarchies are nested and others flat (pp. 443–444).
- Open questions MacKay poses: how to implement infinite models in finite computers, and how to set up Bayesian models to avoid silly answers (p. 444). Pointers: Neal (1991) for categorical data with a Monte Carlo method; Rasmussen (2000) for flat infinite Gaussian mixtures; Neal (2001) for Dirichlet diffusion trees. Most of these ideas build on the Dirichlet process (section 18.2). This is an active research area (p. 444).

### 34.4 Exercises (p. 444)
Factor analysis: $\mathbf x=\mathbf{Gs}+\mathbf n$ (34.30), with independent latent variables and independent additive noise, often zero-mean Gaussians. Noise variances $\sigma_i^2$ may differ (p. 444).

## Toy example (ours, not from the text)
Compare the plain rule (34.16) and the covariant rule (34.29) for $I=J=2$, $\mathbf W=\begin{bmatrix}2&0\\0&1\end{bmatrix}$, $\mathbf x=(1,1)^{\mathsf T}$, $\phi=-\tanh$. Take $\eta=1$.
- $\mathbf a=\mathbf{Wx}=(2,1)$. $\tanh2\approx0.9640$, $\tanh1\approx0.7616$, so $\mathbf z=(-0.9640,-0.7616)$.
- Plain: $[\mathbf W^{\mathsf T}]^{-1}=\mathrm{diag}(0.5,1)$ and $\mathbf{zx}^{\mathsf T}=\begin{bmatrix}-0.9640&-0.9640\\-0.7616&-0.7616\end{bmatrix}$. Sum: $\begin{bmatrix}-0.4640&-0.9640\\-0.7616&0.2384\end{bmatrix}$.
- Covariant: $\mathbf x'=\mathbf W^{\mathsf T}\mathbf a=(2\cdot2,\,1\cdot1)=(4,1)$. $\mathbf{zx}'^{\mathsf T}=\begin{bmatrix}-3.856&-0.964\\-3.0464&-0.7616\end{bmatrix}$. Add $\mathbf W$: $\begin{bmatrix}-1.856&-0.964\\-3.0464&0.2384\end{bmatrix}$. No inverse was needed.
- Check: plain result times $\mathbf W^{\mathsf T}\mathbf W=\mathrm{diag}(4,1)$ multiplies column 1 by 4: $-0.4640\cdot4=-1.856$ and $-0.7616\cdot4=-3.0464$. Column 2 is unchanged. This matches the covariant result.

## Concepts
- [[latent-variable-model]] (new) — generative model where hidden variables, with simple distribution, give rise to observables (p. 437)
- [[independent-component-analysis]] (new) — noise-free linear latent model $\mathbf x=\mathbf{Gs}$ with independent non-Gaussian sources, fitted by maximum likelihood (p. 437)
- [[likelihood]] — $P(D\mid\mathbf G,\mathcal H)$, obtained by marginalizing out latent variables (p. 438)
- [[heavy-tailed-source-prior]] (new) — non-Gaussian source density (e.g. $1/\cosh$, Cauchy) whose non-Gaussianity is the "only hope" for recovering the sources; $\phi=d\ln p/da$ encodes it (p. 439)
- [[covariant-optimization]] (new) — update whose result does not depend on measurement units; the form (34.20) with positive-definite $\mathbf M$ is covariant (p. 441)
- [[natural-gradient]] (new) — the quantity $W_{ij}+x'_jz_i$ of the covariant ICA rule (p. 443)
- [[infinite-mixture-model]] (new) — mixture with unbounded number of clusters, possibly hierarchical; most of the cited ideas build on the Dirichlet process (pp. 443–444)
- [[factor-analysis]] (new) — $\mathbf x=\mathbf{Gs}+\mathbf n$ with independent latent variables and independent noise (p. 444)

## Canonical instances
- [[error-correcting-code-as-latent-variable-model]] — source bits are latent; $\mathbf G$ normally known in advance (p. 437)
- [[cauchy-source-ica-samples]] — Fig. 34.3: heavy tails show how data shape depends on $\mathbf G$ (p. 440)
- [[speech-word-clusters]] — hierarchical infinite cluster model of words, speakers, accents (pp. 443–444)

## Bridges (candidates)
- [structural-analogy] curvature-based covariant step $\mathbf M=\mathbf A^{-1}$ ↔ information-theory: Fisher information as local curvature and Fisher–Rao metric — both turn curvature of a log-likelihood into a metric (not stated in this unit)
- [structural-analogy] Gaussian-source rotation invariance ↔ bayesian: unidentifiability of parameters when the likelihood is flat in some directions
- [structural-analogy] infinite mixture models ↔ bayesian: nonparametric priors (Dirichlet process) letting model size grow with data
- [metaphor] ICA as information maximization ↔ information-theory: choosing a transformation to maximize output information

## Questions this raises
- With non-Gaussian sources, how wrong can the assumed $p_i$ be before recovery fails?
- Which of the severe approximations in (34.23)–(34.26) matters most, and how well does the rule work with unequal sources?
- Does noise change the algorithm? (Exercise 34.1 asks the reader to show that sufficiently small noise gives the identical algorithm.)
- How can a Bayesian model have unboundedly many clusters yet give sensible answers in finite computation?

## Exercises worth doing
- Ex. 34.1 (p. 444) — show that sufficiently small noise in $\mathbf x$ gives the identical algorithm; tests understanding of the delta-function marginalization — difficulty: medium
- Ex. 34.2 (p. 444) — implement covariant ICA on toy data — difficulty: medium
- Ex. 34.3 (p. 444) — extend to substantial noise, $J>I$, $J<I$ — difficulty: hard
- Ex. 34.4 (p. 444) — maximum likelihood for Gaussian factor analysis with per-component noise variances — difficulty: hard
- Ex. 34.5 (p. 444) — implement Rasmussen's infinite Gaussian mixture — difficulty: hard

## Reading notes
- Printed page = pdf − 12. Pages 437–444 of the printed book.
- Section 34.3 says the derived algorithm "performs steepest descents on the likelihood" (p. 440), though it ascends the likelihood. This looks like a slip in wording.
- Eq. (34.20) prints $\partial L/\partial w_i$ inside the sum over $i'$. The image shows this; it should be $w_{i'}$.
- The text layer showed $x'$ as "x0" and $z'$ as "z0"; the images show primes.
- Exercise difficulty marks as printed: [3], [3], [4-5], [4], [4C]. I mapped them to easy/medium/hard myself.
