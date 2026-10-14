---
id: prince-2023-udl/ch23-probability
work: prince-2023-udl
unit: Appendix C — Probability (unit id "ch23")
pages: 449–462
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Probability (Appendix C)

## L0 — One line
Joint, marginal and conditional distributions, expectation rules, the normal distribution, sampling and distribution distances are the probability toolkit this appendix presents as a primer for machine learning, where the author says probability underlies losses, generative models and reinforcement learning.

## L1 — The gist (≤ 120 words)
This appendix is a probability primer for machine learning. It covers how joint, marginal and conditional distributions relate; how expectations behave; how the normal distribution works; how to draw samples; and how to measure distance between distributions. Bayes' rule comes from writing the joint two ways; independence factors the joint into marginals. Expectation obeys four simple rules (the last needs independence), from which the variance identity and standardization follow. Normal distributions have convenient closed-form properties. Sampling uses the inverse cumulative distribution or ancestral sampling. KL divergence is never negative but is not symmetric; Jensen–Shannon and Fréchet distances are alternatives. The opening paragraph says probability underlies supervised losses, generative models and reinforcement learning (p. 449).

**Prerequisites:** integrals and sums; basic matrix notation (transpose, inverse, determinant, trace); the exponential and logarithm.

## L2 — Key ideas
- Probability density can exceed one at a point, but it must integrate to one. The text treats continuous variables, and discrete ones need only sums in place of integrals (p. 449).
- Marginals come from integrating out the other variable. Conditionals come from slicing the joint and renormalizing (pp. 450–451).
- Bayes' rule turns a prior (belief before seeing $y$) into a posterior (belief after) using the likelihood and the evidence (the denominator) (p. 452).
- When two variables are independent (one tells nothing about the other), the joint equals the product of the marginals. Zero covariance (no tendency to vary together) does not imply independence (pp. 452, 455).
- Four rules of expectation (constants, scaling, sums, products of independent terms) give the variance identity and standardization (shift and scale to mean 0, variance 1) (pp. 453–456).
- A normal distribution is fixed by its mean and covariance. Spherical or diagonal covariance makes its variables independent, and two product/linear-mean relations hold up to proportionality (pp. 457–459).
- Sampling uses the inverse cumulative distribution, then the standardization transform for normals, and ancestral sampling for factored joints (sample the root variable first, then each conditional in turn) (p. 460).
- KL divergence (a measure of distance between distributions) is $\ge 0$ and infinite where $q=0$ but $p\neq0$. It is asymmetric, so symmetric alternatives exist, and normal distributions give closed forms (pp. 461–462).

## L3 — Walkthrough

### C.1 Random variables and distributions
A random variable is an uncertain quantity. It can be discrete or continuous, and its distribution $Pr(x)$ gives the relative propensity of each value. Discrete probabilities lie in $[0,1]$ and sum to one. A continuous density is non-negative and integrates to one, and it "can be greater than one for any point" (p. 449).

**C.1.1 Joint.** $Pr(x,y)$ is a non-negative density over pairs, with
$$\iint Pr(x,y)\,dx\,dy = 1 \tag{C.1}$$
It extends to $Pr(x,y,z)$ and to vectors $\mathbf{x},\mathbf{y}$ (p. 450).

**C.1.2 Marginalization.** Integrating over the other variable recovers each marginal:
$$\int Pr(x,y)\,dx = Pr(y),\qquad \int Pr(x,y)\,dy = Pr(x) \tag{C.2}$$
This gives the distribution of one variable regardless of the other. It extends to more variables: integrating $Pr(x,y,z)$ over $y$ gives $Pr(x,z)$ (p. 450).

**C.1.3 Conditional and likelihood.** The conditional is a slice of the joint at fixed $y$, divided by the area of the slice (figure C.2):
$$Pr(x|y)=\frac{Pr(x,y)}{Pr(y)}\tag{C.3}$$
$$Pr(y|x)=\frac{Pr(x,y)}{Pr(x)}\tag{C.4}$$
As a function of $x$, $Pr(x|y)$ sums to one. As a function of $y$ it is called the *likelihood* of $x$ given $y$ and need not sum to one (p. 451).

**C.1.4 Bayes' rule.** Both conditionals give
$$Pr(x,y)=Pr(x|y)Pr(y)=Pr(y|x)Pr(x)\tag{C.5}$$
so
$$Pr(x|y)=\frac{Pr(y|x)Pr(x)}{Pr(y)}\tag{C.6}$$
$Pr(y|x)$ is the likelihood, $Pr(x)$ the prior, $Pr(y)$ the evidence, and $Pr(x|y)$ the posterior. The rule maps what we know about $x$ before seeing $y$ to what we know after (pp. 451–452).

**C.1.5 Independence.** If $y$ tells us nothing about $x$ and vice versa, then $Pr(x|y)=Pr(x)$ and $Pr(y|x)=Pr(y)$. All conditionals $Pr(x|y=\bullet)$ are then identical, and
$$Pr(x,y)=Pr(x|y)Pr(y)=Pr(x)Pr(y)\tag{C.7}$$
(p. 452).

*Intuition note:* Marginalizing adds up what you don't care about. Conditioning cuts out the cases that match what you saw and rescales them. Bayes' rule comes from writing the joint probability in two ways and rearranging.

### C.2 Expectation
The expected value of $f[x]$ under $Pr(x)$ is
$$\mathbb{E}_x[f[x]]=\int f[x]Pr(x)\,dx\tag{C.8}$$
and for two variables
$$\mathbb{E}_{x,y}[f[x,y]]=\iint f[x,y]Pr(x,y)\,dx\,dy\tag{C.9}$$
The distribution subscript is dropped when it is obvious. The average of $f[x_i]$ over $I$ samples from $Pr(x)$ approximates the expectation (p. 453):
$$\mathbb{E}_x[f[x]]\approx\frac1I\sum_{i=1}^I f[x_i]\tag{C.10}$$

**C.2.1 Four rules** (for constant $k$; rule 4 only if $x,y$ independent) (p. 453):
$$\mathbb{E}[k]=k,\quad \mathbb{E}[k f[x]]=k\mathbb{E}[f[x]],\quad \mathbb{E}[f[x]+g[x]]=\mathbb{E}[f[x]]+\mathbb{E}[g[x]],\quad \mathbb{E}_{x,y}[f[x]g[y]]=\mathbb{E}_x[f[x]]\,\mathbb{E}_y[g[y]]\tag{C.11}$$
The proofs for the continuous case are:
- Rule 1: $\int k\,Pr(x)dx=k\int Pr(x)dx=k$ (C.12).
- Rule 2: pull $k$ out of the integral (C.13).
- Rule 3: split the integral of $(f+g)Pr(x)$ into two integrals (C.14).
- Rule 4: write $Pr(x,y)=Pr(x)Pr(y)$ by C.7, so the double integral factorizes (C.15) (pp. 453–454).

Multivariate versions, with constant matrix $\mathbf A$ and vector-valued $\mathbf f,\mathbf g$ (p. 454):
$$\mathbb{E}[\mathbf A]=\mathbf A,\ \mathbb{E}[\mathbf A\mathbf f[\mathbf x]]=\mathbf A\mathbb{E}[\mathbf f[\mathbf x]],\ \mathbb{E}[\mathbf f[\mathbf x]+\mathbf g[\mathbf x]]=\mathbb{E}[\mathbf f[\mathbf x]]+\mathbb{E}[\mathbf g[\mathbf x]],\ \mathbb{E}[\mathbf f[\mathbf x]^T\mathbf g[\mathbf y]]=\mathbb{E}[\mathbf f[\mathbf x]]^T\mathbb{E}[\mathbf g[\mathbf y]]\tag{C.16}$$
(the last only if $\mathbf x,\mathbf y$ independent).

**C.2.2 Mean, variance, covariance.** The mean is $\mu=\mathbb{E}[x]$ (centre). The variance is $\sigma^2=\mathbb{E}[(x-\mu)^2]$ (spread). The standard deviation $\sigma$ is its positive root, in the units of $x$. The covariance is $\mathbb{E}[(x-\mu_x)(y-\mu_y)]$. Independent variables have zero covariance, but zero covariance does not imply independence. Example: with probability uniform on the unit circle there is no average tendency for $x$ to rise with $y$. Yet knowing $x=0$ leaves $y=\pm1$ equally likely, so they are not independent. For $\mathbf x\in\mathbb R^D$ the covariance matrix is the $D\times D$ matrix $\mathbb{E}[(\mathbf x-\boldsymbol\mu_x)(\mathbf x-\boldsymbol\mu_x)^T]$, whose $(i,j)$ entry is the covariance of $x_i$ and $x_j$ (p. 455).

**C.2.3 Variance identity.**
$$\mathbb{E}[(x-\mu)^2]=\mathbb{E}[x^2]-\mathbb{E}[x]^2\tag{C.17}$$
Proof (p. 455), chain of equalities from C.18:
$\mathbb{E}[(x-\mu)^2]=\mathbb{E}[x^2-2\mu x+\mu^2]=\mathbb{E}[x^2]-\mathbb{E}[2\mu x]+\mathbb{E}[\mu^2]=\mathbb{E}[x^2]-2\mu\mathbb{E}[x]+\mu^2=\mathbb{E}[x^2]-2\mu^2+\mu^2=\mathbb{E}[x^2]-\mu^2=\mathbb{E}[x^2]-\mathbb{E}[x]^2$.
The author cites rule 3 for the first step, rules 1–2 for the second, and the definition $\mu=\mathbb{E}[x]$ in lines four and six.

**C.2.4 Standardization.** Setting mean 0 and variance 1:
$$z=\frac{x-\mu}{\sigma}\tag{C.19}$$
Mean: $\mathbb{E}[z]=\frac1\sigma\mathbb{E}[x-\mu]=\frac1\sigma(\mathbb{E}[x]-\mathbb{E}[\mu])=\frac1\sigma(\mu-\mu)=0$ (C.20).
Variance: $\mathbb{E}[(z-\mu_z)^2]=\mathbb{E}[z^2]=\mathbb{E}[((x-\mu)/\sigma)^2]=\frac1{\sigma^2}\mathbb{E}[(x-\mu)^2]=\frac{1}{\sigma^2}\sigma^2=1$ (C.21).
The reverse is
$$x=\mu+\sigma z\tag{C.22}$$
For a vector with mean $\boldsymbol\mu$ and covariance $\boldsymbol\Sigma$:
$$\mathbf z=\boldsymbol\Sigma^{-1/2}(\mathbf x-\boldsymbol\mu)\tag{C.23}$$
This gives $\mathbb{E}[\mathbf z]=\mathbf 0$ and identity covariance. The reverse is
$$\mathbf x=\boldsymbol\mu+\boldsymbol\Sigma^{1/2}\mathbf z\tag{C.24}$$
(p. 456).

*Intuition note:* The first three rules need no independence: constants, scalings and sums pass straight through the expectation. The product rule needs independence. Standardizing is shift-then-scale, and the reverse transform rebuilds any mean and spread from a standard variable.

### C.3 Normal distribution
It is the most common distribution in machine learning (p. 457).

**C.3.1 Univariate.**
$$Pr(x)=\text{Norm}_x[\mu,\sigma^2]=\frac1{\sqrt{2\pi\sigma^2}}\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right]\tag{C.25}$$
Its mean is $\mu$ and its variance is $\sigma^2$. Mean 0 with variance 1 is the *standard normal*. The exponent is a quadratic that falls away from $x=\mu$, faster for smaller $\sigma$. The exponential makes a bell shape, and the constant normalizes it. $\mu$ sets the centre and $\sigma$ the width (p. 457).

**C.3.2 Multivariate.** With a $D\times1$ mean $\boldsymbol\mu$ and a symmetric positive definite $D\times D$ covariance $\boldsymbol\Sigma$ (p. 457):
$$\text{Norm}_{\mathbf x}[\boldsymbol\mu,\boldsymbol\Sigma]=\frac{1}{(2\pi)^{D/2}|\boldsymbol\Sigma|^{1/2}}\exp\left[-\frac{(\mathbf x-\boldsymbol\mu)^T\boldsymbol\Sigma^{-1}(\mathbf x-\boldsymbol\mu)}{2}\right]\tag{C.26}$$
Covariance forms (2-D):
$$\boldsymbol\Sigma_{spher}=\begin{bmatrix}\sigma^2&0\\0&\sigma^2\end{bmatrix},\ \boldsymbol\Sigma_{diag}=\begin{bmatrix}\sigma_1^2&0\\0&\sigma_2^2\end{bmatrix},\ \boldsymbol\Sigma_{full}=\begin{bmatrix}\sigma_{11}^2&\sigma_{12}^2\\\sigma_{21}^2&\sigma_{22}^2\end{bmatrix}\tag{C.27}$$
Spherical gives circular contours, diagonal gives axis-aligned ellipses, and full gives general ellipses (figure C.4). For spherical or diagonal $\boldsymbol\Sigma$ the variables are independent. With $|\boldsymbol\Sigma|=\sigma_1^2\sigma_2^2$ and $\boldsymbol\Sigma^{-1}=\text{diag}(\sigma_1^{-2},\sigma_2^{-2})$ the density becomes
$$Pr(x_1,x_2)=\frac1{2\pi\sigma_1\sigma_2}\exp\left[-\tfrac12\left(\tfrac{x_1^2}{\sigma_1^2}+\tfrac{x_2^2}{\sigma_2^2}\right)\right]=\frac{1}{\sqrt{2\pi\sigma_1^2}}e^{-x_1^2/2\sigma_1^2}\cdot\frac{1}{\sqrt{2\pi\sigma_2^2}}e^{-x_2^2/2\sigma_2^2}=Pr(x_1)Pr(x_2)\tag{C.28}$$
(p. 458; shown with zero mean as printed; the expanded exponent in the middle expression is our added step).

**C.3.3 Product of two normals** (up to a constant) (p. 459):
$$\text{Norm}_{\mathbf x}[\mathbf a,\mathbf A]\,\text{Norm}_{\mathbf x}[\mathbf b,\mathbf B]\propto\text{Norm}_{\mathbf x}\!\left[(\mathbf A^{-1}+\mathbf B^{-1})^{-1}(\mathbf A^{-1}\mathbf a+\mathbf B^{-1}\mathbf b),\,(\mathbf A^{-1}+\mathbf B^{-1})^{-1}\right]\tag{C.29}$$
The author says it is proved by multiplying out the exponents and completing the square (problem 18.5).

**C.3.4 Change of variable.** If the mean is linear in $\mathbf y$ (p. 459):
$$\text{Norm}_{\mathbf x}[\mathbf A\mathbf y+\mathbf b,\boldsymbol\Sigma]\propto\text{Norm}_{\mathbf y}\!\left[(\mathbf A^T\boldsymbol\Sigma^{-1}\mathbf A)^{-1}\mathbf A^T\boldsymbol\Sigma^{-1}(\mathbf x-\mathbf b),\,(\mathbf A^T\boldsymbol\Sigma^{-1}\mathbf A)^{-1}\right]\tag{C.30}$$
Figure C.5 shows the scalar case. There $Pr(x|y)$ has a mean linear in $y$ and constant variance, and $Pr(y|x)$ is proportional to it. The proof is again completing the square (problem 18.4).

*Intuition note:* The normal curve is determined by a quadratic inside an exponential. The author states that a product of two normals is proportional to a normal (C.29), and that a normal whose mean is linear in $\mathbf y$ is proportional to a normal in $\mathbf y$ (C.30). He says both can be proved by multiplying out the exponents and completing the square.

### C.4 Sampling
Compute the cumulative distribution $F[x]$ (integral of $Pr(x)$). Draw $z^*$ uniform on $[0,1]$. Then
$$x^*=F^{-1}[z^*]\tag{C.31}$$
(p. 460).

**C.4.1 Normals.** Use C.31 for a standard normal, then C.22 for general $\mu,\sigma^2$. For $D$ dimensions, sample $D$ independent standard normals, then apply C.24 (p. 460).

**C.4.2 Ancestral sampling.** If the joint factors into conditionals, sample the root variable first, then each variable given its sampled parent. Example: $Pr(x,y,z)=Pr(x)Pr(y|x)Pr(z|y)$ (C.32). Draw $x^*\sim Pr(x)$, then $y^*\sim Pr(y|x^*)$, then $z^*\sim Pr(z|y^*)$ (p. 460).

### C.5 Distances between distributions
Supervised learning can be framed as minimizing the distance between the model's distribution and the discrete distribution implied by the samples (section 5.7). Unsupervised learning can often be framed as minimizing the distance between real-data and model distributions (p. 460).

**C.5.1 KL divergence.**
$$D_{KL}[p\|q]=\int p(x)\log\frac{p(x)}{q(x)}dx\tag{C.33}$$
It is $\ge0$, shown with $-\log y\ge1-y$ (figure C.6):
$D_{KL}=-\int p\log\frac qp\,dx\ \ge\int p\left(1-\frac qp\right)dx=\int(p-q)\,dx=1-1=0$ (C.34).
It is infinite where $q(x)=0$ but $p(x)\neq0$, which can cause problems in minimization (p. 461).

**C.5.2 Jensen–Shannon.** KL is not symmetric. The symmetric alternative is
$$D_{JS}[p\|q]=\tfrac12D_{KL}\!\left[p\Big\|\tfrac{p+q}2\right]+\tfrac12D_{KL}\!\left[q\Big\|\tfrac{p+q}2\right]\tag{C.35}$$
the mean divergence of $p$ and $q$ to their average (p. 461).

**C.5.3 Fréchet.**
$$D_{Fr}[p\|q]=\sqrt{\min_{\pi(x,y)}\iint\pi(x,y)|x-y|^2\,dx\,dy}\tag{C.36}$$
Here $\pi$ ranges over joint distributions compatible with the marginals $p(x)$ and $q(y)$. The author adds that it can also be formulated as a maximum distance between cumulative curves (p. 462).

**C.5.4 Between normals** (means $\boldsymbol\mu_1,\boldsymbol\mu_2$, covariances $\boldsymbol\Sigma_1,\boldsymbol\Sigma_2$, dimension $D$; closed forms) (p. 462):
$$D_{KL}[\text{Norm}[\boldsymbol\mu_1,\boldsymbol\Sigma_1]\|\text{Norm}[\boldsymbol\mu_2,\boldsymbol\Sigma_2]]=\tfrac12\Big(\log\tfrac{|\boldsymbol\Sigma_2|}{|\boldsymbol\Sigma_1|}-D+\text{tr}[\boldsymbol\Sigma_2^{-1}\boldsymbol\Sigma_1]+(\boldsymbol\mu_2-\boldsymbol\mu_1)^T\boldsymbol\Sigma_2^{-1}(\boldsymbol\mu_2-\boldsymbol\mu_1)\Big)\tag{C.37}$$
$$D^2_{Fr/W_2}[\cdot\|\cdot]=|\boldsymbol\mu_1-\boldsymbol\mu_2|^2+\text{tr}\big[\boldsymbol\Sigma_1+\boldsymbol\Sigma_2-2(\boldsymbol\Sigma_1\boldsymbol\Sigma_2)^{1/2}\big]\tag{C.38}$$

*Intuition note:* KL is the most common measure of distance between $p$ and $q$, and it cannot be negative. It is asymmetric, and it is infinite where $q$ is zero but $p$ is not. Jensen–Shannon is symmetric by construction.

## Toy example (ours, discrete)
Let $x,y\in\{0,1\}$ with joint $Pr(0,0)=0.3$, $Pr(0,1)=0.1$, $Pr(1,0)=0.2$, $Pr(1,1)=0.4$. The sum is $1.0$.
- Marginals (sums replace integrals): $Pr(x{=}1)=0.2+0.4=0.6$, $Pr(x{=}0)=0.4$, $Pr(y{=}1)=0.1+0.4=0.5$.
- Conditional: $Pr(x{=}1|y{=}1)=0.4/0.5=0.8$. Likewise $Pr(y{=}1|x{=}1)=0.4/0.6=2/3$.
- Bayes check: $\frac{(2/3)(0.6)}{0.5}=\frac{0.4}{0.5}=0.8$ ✓.
- Independence test: $Pr(0)Pr(0)$ would be $0.4\times0.5=0.2\neq0.3$, so $x,y$ are not independent.
- Expectation: $\mathbb E[x]=0\cdot0.4+1\cdot0.6=0.6$. Variance by C.17: $\mathbb E[x^2]-0.36=0.6-0.36=0.24$.

## Concepts
- [[random-variable]] (new) — an uncertain quantity, discrete or continuous, described by a distribution (p. 449)
- [[joint-distribution]] (new) — $Pr(x,y)$; propensity of combinations of values (p. 449)
- [[marginalization]] (new) — integrate a joint over the other variable (p. 450)
- [[conditional-probability]] (new) — slice of the joint divided by the slice's area (p. 450)
- [[likelihood]] (new) — $Pr(x|y)$ viewed as a function of $y$; need not sum to one (p. 451)
- [[bayes-rule]] (new) — posterior = likelihood × prior / evidence (p. 452)
- [[independence]] (new) — joint equals product of marginals (p. 452)
- [[expectation]] (new) — average of $f[x]$ weighted by $Pr(x)$; four rules (p. 453)
- [[variance-covariance]] (new) — expected squared deviation; co-variation of two variables (p. 455)
- [[standardization]] (new) — shift and scale to mean 0, variance 1 (p. 456)
- [[normal-distribution]] (new) — bell curve fixed by mean and (co)variance (p. 457)
- [[ancestral-sampling]] (new) — sample root variable, then each conditional in turn (p. 460)
- [[kl-divergence]] (new) — $\int p\log(p/q)$; $\ge0$, asymmetric (p. 461). Not the same as the canon's "KL penalty".
- [[jensen-shannon-divergence]] (new) — symmetric mean KL to the average distribution (p. 461)
- [[frechet-wasserstein-distance]] (new) — square root of the minimal expected squared distance $|x-y|^2$ over joint distributions with the given marginals (p. 462)
- [[softmax]] and [[cross-entropy-log-loss]] are not defined in this unit.

## Canonical instances
- [[zero-covariance-not-independent]] (new) — uniform on unit circle: covariance zero, yet dependent (p. 455)
- [[ancestral-sampling-chain]] (new) — $Pr(x)Pr(y|x)Pr(z|y)$ sampled in order (p. 460)
- [[bivariate-normal-covariance-types]] (new) — spherical, diagonal and full covariance shapes (p. 458)

## Bridges (candidates)
- [same-math] KL divergence ↔ language models: cross-entropy equals entropy plus KL, so minimizing log-loss minimizes KL to the data distribution (canon link; not stated in this unit).
- [metaphor] Bayes' rule posterior ↔ language models: Bayesian reading of conditioning on a prompt (canon link; not stated here).
- [structural-analogy] Ancestral sampling ↔ language models: autoregressive generation draws each token given earlier ones, like the chain in C.32.
- [structural-analogy] Standardization $z=(x-\mu)/\sigma$ ↔ normalization layers in neural networks.

## Questions this raises
- Why is KL the most common distance between distributions (p. 461) even though it is asymmetric and can be infinite, and when are Jensen–Shannon or Fréchet better?
- How is the density $Pr(x)$ in a normalizing flow or diffusion model related to the sampling in C.4?
- When a covariance is zero but variables are dependent, what other measure detects the dependence?
- Why is the closed-form KL between normals useful in practice?

## Reading notes
- Printed = pdf − 14 (pdf 463 = p. 449).
- Figure C.2 caption, panel c, says "The joint probability $Pr(x,y=-1.0)$"; the panel title shows the conditional $Pr(x|y=-1.0)$. The caption wording is inconsistent with panel b.
- C.3.1 text reads "the mean µ control"; a typo, as printed.
- In C.5.3 the text says $q(x)$ while the formula uses $q(y)$.
- C.36 is the author's formula as printed; the "maximum distance between cumulative curves" remark is stated without proof.
- C.29, C.30 are stated with a one-line proof sketch; full proofs are deferred to problems 18.5 and 18.4, which are not in this unit.
- No equations were unreadable. No page image was supplied for printed p. 460, so C.31–C.32 rest on the text layer.
- The unit has no exercises.
