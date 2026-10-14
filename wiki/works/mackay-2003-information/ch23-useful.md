---
id: mackay-2003-information/ch23-useful
work: mackay-2003-information
unit: "23 Useful Probability Distributions"
pages: 311-318
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Useful Probability Distributions

## L0 — One line
A short catalogue of the distributions that recur in Bayesian modelling, grouped by the kind of variable they describe, with the advice to distrust the Gaussian's light tails and to choose a good basis (log, logit, softmax).

## L1 — The gist (≤ 120 words)
Which distributions should you know when modelling data in a Bayesian way? MacKay lists them by variable type: integers (binomial, Poisson, exponential), unbounded reals (Gaussian, Student, Cauchy, biexponential, inverse-cosh), positive reals (exponential, gamma, inverse-gamma, log-normal), periodic variables (von Mises, wrapped Gaussian) and probabilities (beta, Dirichlet, entropic). He gives formulas, normalizing constants and typical uses. Two themes: the Gaussian has very light tails, so it can mislead; and quantities like scales and probabilities behave better in transformed bases (ln, logit, softmax), where, for example, the gamma's spike at $x=0$ and the beta's singularities at 0 and 1 do not appear. The chapter aims at recognition: there is no need to memorize them, except perhaps the Gaussian.

**Prerequisites:** probability densities and normalizing constants; change of variables for densities (Jacobian); logarithms and exponentials; Poisson and binomial counts (the book's page 2). Terms used in L0–L2: heavy tails = outliers are more probable than under a Gaussian; logit = $\ln\frac p{1-p}$; softmax basis = writing a probability vector as $p_i=e^{a_i}/\sum_j e^{a_j}$; Dirichlet = the beta distribution generalised to probability vectors; Cauchy, biexponential, inverse-cosh, von Mises and entropic distributions are defined in L3.

## L2 — Key ideas
- The chapter is a reference list meant so that these distributions "won't be intimidating" when met later; the author says there is no need to memorize any, "except perhaps the Gaussian" (p. 311).
- Integer distributions are tied to stories: binomial (N flips of a bent coin), Poisson (photon counts), exponential on integers (waiting for a six) (p. 311).
- The author doubts that Gaussians are common in the real world. Their tails are very light, and a heavier-tailed variable modelled as Gaussian can distort the rest of the model (p. 312).
- Heavier tails come from mixtures of Gaussians, the Student-t (Cauchy when n = 1), and the biexponential (p. 312–313).
- It is often natural to represent a positive variable by $l=\ln x$; the author calls a gamma 'spike' at $x=0$ an artefact of a bad choice of basis. The 1/x prior is the limit $sc=1$, $c\to0$, and is uniform in $l$ (p. 313–314).
- Beta and Dirichlet distributions are densities over probabilities. In the logit $l=\ln\frac p{1-p}$ the beta density is bell-shaped although it may be singular in $p$; in the softmax basis ($p_i=e^{a_i}/\sum_j e^{a_j}$) the Dirichlet's "minus-ones" in the exponents disappear (p. 316–317).
- The Dirichlet's α controls sharpness and the number of observations needed for data to dominate the prior (p. 317).

## L3 — Walkthrough

### Intro (p. 311)
Bayesian data modelling reuses a small set of distributions. The author says there is no need to memorize them, except perhaps the Gaussian (p. 311).

### 23.1 Distributions over integers (p. 311)
- **Binomial** (number of heads $r$ in $N$ flips of a coin with bias $f\in[0,1]$):
$$P(r\mid f,N)=\binom{N}{r}f^r(1-f)^{N-r},\quad r\in\{0,\dots,N\}\tag{23.1}$$
- **Poisson** (photon count $r$ in a pixel, mean $\lambda$): $$P(r\mid\lambda)=e^{-\lambda}\frac{\lambda^r}{r!},\quad r\in\{0,1,2,\dots\}\tag{23.2}$$
- **Exponential on integers**, for waiting problems: $$P(r\mid f)=f^r(1-f),\quad r\in\{0,1,\dots,\infty\}\tag{23.3}$$
 Waiting for a six on a fair die: this is the distribution of the number of rolls $r$, with $f=5/6$. Equivalently $$P(r\mid f)=(1-f)e^{-\lambda r},\ \ \lambda=\ln(1/f)\tag{23.4}$$

*Intuition note:* Each of these is introduced with a simple example: counting heads, counting photons, or waiting for a six.

### 23.2 Unbounded real numbers (p. 312–313)
- **Gaussian** with mean $\mu$, standard deviation $\sigma$: $$P(x\mid\mu,\sigma)=\frac1Z\exp\!\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big),\quad Z=\sqrt{2\pi\sigma^2}\tag{23.5, 23.6}$$ The precision is $\tau\equiv1/\sigma^2$ (p. 312).
- **Sampling.** With $u_1,u_2$ uniform on $(0,1)$, $$z=\cos(2\pi u_1)\sqrt{2\ln(1/u_2)}\tag{23.7}$$ is a standard Gaussian sample. $z_2=\sin(2\pi u_1)\sqrt{2\ln(1/u_2)}$ is a second, independent sample "for free" (p. 312).
- **Author's scepticism.** Unimodal distributions may be common, but a Gaussian is a special, rather extreme one. Its log-density falls quadratically. Probabilities of deviating from $\mu$ by more than $2\sigma,3\sigma,4\sigma,5\sigma$ are 0.046, 0.003, $6\times10^{-5}$, $6\times10^{-7}$. In his experience deviations of 4–5 typical widths are rare but not that rare. If a variable modelled as a Gaussian actually has heavier tails, the rest of the model will "contort itself" to reduce the outliers' deviations (p. 312). Exercise 23.1 asks the reader to check tails on a log histogram.
- **Mixture of Gaussians** (heavier tails): means, standard deviations and mixing coefficients $\pi_i\ge0$ with $\pi_1+\pi_2=1$ (two-component case) (p. 312).
- **Student-t:** an appropriately weighted mixture of infinitely many Gaussians, all with mean $\mu$: $$P(x\mid\mu,s,n)=\frac1Z\frac{1}{(1+(x-\mu)^2/(ns^2))^{(n+1)/2}},\quad Z=\sqrt{\pi ns^2}\,\frac{\Gamma(n/2)}{\Gamma((n+1)/2)}\tag{23.8, 23.9}$$ $n$ = degrees of freedom. If $n>1$ the mean exists and equals $\mu$. If $n>2$ the variance is finite, $\sigma^2=ns^2/(n-2)$. As $n\to\infty$ it approaches a normal with standard deviation $s$ (p. 313). It arises in classical statistics (sampling distributions) and in Bayesian inference, for a variable from a Gaussian whose standard deviation is uncertain. $n=1$ is the **Cauchy** distribution (p. 313).
- **Biexponential**, tails between Student and Gaussian: $$P(x\mid\mu,s)=\frac1Z\exp\!\Big(-\frac{|x-\mu|}{s}\Big),\ Z=2s\tag{23.10, 23.11}$$
- **Inverse-cosh**, popular in independent component analysis: $$P(x\mid\beta)\propto\frac{1}{[\cosh(\beta x)]^{1/\beta}}\tag{23.12}$$ For large $\beta$ it becomes biexponential. As $\beta\to0$ it approaches a zero-mean Gaussian with variance $1/\beta$ (p. 313).

*Intuition note:* Under a Gaussian a far outlier is very improbable (about $6\times10^{-7}$ at $5\sigma$), so if the real tails are heavier, the rest of the model contorts to reduce the outliers' deviations. Mixtures, Student-type and biexponential shapes have heavier tails than the Gaussian.

### 23.3 Positive real numbers (p. 313–315)
- **Exponential:** $P(x\mid s)=\frac1Z e^{-x/s}$, $Z=s$ (23.13, 23.14). Waiting for a bus that arrives independently at random, once every $s$ minutes on average, gives an exponential wait with mean $s$ (p. 313).
- **Gamma** (exponential times polynomial $x^{c-1}$; two parameters): $$P(x\mid s,c)=\frac1Z\Big(\frac xs\Big)^{c-1}e^{-x/s},\ Z=\Gamma(c)s\tag{23.15, 23.16}$$ Mean $sc$, variance $s^2c$ (p. 314).
- **Density over $l=\ln x$:** $$P(l)=P(x(l))\Big|\frac{\partial x}{\partial l}\Big|=P(x(l))\,x(l)=\frac1{Z_l}\Big(\frac{x(l)}s\Big)^{c}e^{-x(l)/s},\ Z_l=\Gamma(c)\tag{23.17–23.19}$$ A spike at $x=0$ in the $x$ density never appears in the $l$ density; the author calls the spike "an artefact of a bad choice of basis" (p. 314).
- **The 1/x prior.** In the limit $sc=1$, $c\to0$ the gamma becomes the noninformative prior for a scale parameter. It is improper, has no length scale, and is invariant under rescaling $x\to mx$ (printed "$x=mx$"; see Reading notes). In $l=\ln x$ it becomes uniform (p. 314). Exercise 23.2 asks for the density in $u=x^{1/3}$.
- The gamma is always unimodal in $l$ and, as the figures show, asymmetric. For $v=1/x$ the $l$-density is flipped left-for-right, giving the **inverse-gamma**: $$P(v\mid s,c)=\frac1{Z_v}\Big(\frac1{sv}\Big)^{c+1}e^{-1/(sv)},\ Z_v=\Gamma(c)/s\tag{23.20, 23.21}$$
- Uses: inferring the variance of Gaussian noise, or a Poisson rate from a count (p. 315). For a Poisson process with rate $\lambda$, the arrival time $x$ of the $m$-th event has density $$\frac{\lambda(\lambda x)^{m-1}}{(m-1)!}e^{-\lambda x}\tag{23.22}$$
- **Log-normal:** $l=\ln x$ is normal; $m$ is the median of $x$ and $s$ the standard deviation of $\ln x$: $$P(l\mid m,s)=\frac1Z\exp\!\Big(-\frac{(l-\ln m)^2}{2s^2}\Big),\ Z=\sqrt{2\pi s^2}\tag{23.23, 23.24}$$ $$P(x\mid m,s)=\frac1x\frac1Z\exp\!\Big(-\frac{(\ln x-\ln m)^2}{2s^2}\Big)\tag{23.25}$$ (p. 315).

*Intuition note:* For a positive variable, $l=\ln x$ is often a natural coordinate, and the gamma's spike at $x=0$ does not appear there. The 1/x prior has no characteristic value of $x$ and is uniform in $l$ (our gloss: equal prior mass for equal ratios of $x$).

### 23.4 Periodic variables (p. 315–316)
A periodic variable $\theta\in[0,2\pi]$ treats $0$ and $2\pi$ as equivalent.
- **Von Mises**, the Gaussian's analogue: $P(\theta\mid\mu,\beta)=\frac1Z\exp(\beta\cos(\theta-\mu))$, $Z=2\pi I_0(\beta)$, with $I_0$ a modified Bessel function (23.26).
- **Wrapped Gaussian**, from Brownian diffusion around the circle: $$P(\theta\mid\mu,\sigma)=\sum_{n=-\infty}^{\infty}\mathrm{Normal}(\theta;\mu+2\pi n,\sigma^2)\tag{23.27}$$ (p. 316).

### 23.5 Distributions over probabilities (p. 316–318)
- **Beta** over $p\in(0,1)$, with any positive $u_1,u_2$: $$P(p\mid u_1,u_2)=\frac1{Z(u_1,u_2)}p^{u_1-1}(1-p)^{u_2-1},\ Z=\frac{\Gamma(u_1)\Gamma(u_2)}{\Gamma(u_1+u_2)}\tag{23.28, 23.29}$$ Special cases: uniform $(1,1)$; Jeffreys prior $(0.5,0.5)$; improper Laplace prior $(0,0)$. In the logit $l=\ln\frac p{1-p}$ the density is "always a pleasant bell-shaped density", while in $p$ it may be singular at 0 and 1 (p. 316, fig. 23.7).
- **Dirichlet** over an $I$-vector $\mathbf p$ with positive components summing to 1. The beta is the case $I=2$. With $\mathbf u=\alpha\mathbf m$, $\sum m_i=1$, $\alpha>0$: $$P(\mathbf p\mid\alpha\mathbf m)=\frac1{Z(\alpha\mathbf m)}\prod_{i=1}^I p_i^{\alpha m_i-1}\,\delta\Big(\sum_ip_i-1\Big)\tag{23.30}$$ The delta function restricts $\mathbf p$ to the simplex. $$Z(\alpha\mathbf m)=\prod_i\Gamma(\alpha m_i)/\Gamma(\alpha)\tag{23.31}$$ The mean is $\mathbf m$: $\int\mathrm{Dirichlet}^{(I)}(\mathbf p\mid\alpha\mathbf m)\,\mathbf p\,d^I\mathbf p=\mathbf m$ (23.32) (p. 316).
- **Softmax basis:** $p_i=\frac1Ze^{a_i}$, $Z=\sum_ie^{a_i}$, with $\sum a_i=0$ (23.33). It is analogous to $\sigma\to\ln\sigma$ and to the logit. The "ugly minus-ones" vanish: $$P(\mathbf a\mid\alpha\mathbf m)\propto\frac1{Z(\alpha\mathbf m)}\prod_ip_i^{\alpha m_i}\,\delta\Big(\sum_ia_i\Big)\tag{23.34}$$ (p. 316–317).
- **Role of α**, two ways (p. 317):
 1. *Sharpness*, like the precision $\tau$ of a Gaussian: large α gives a distribution sharply peaked around $\mathbf m$. In Zipf plots (ranked $p_i$ vs rank, log–log; fig. 23.9, uniform $\mathbf m$, $I=100$ and $1000$, α from 0.1 to 1000) large α gives a shallow plot with many similar components. For small α, typically one component takes an overwhelming share, then another takes a large share of the remainder, and as $\alpha\to0$ the plot tends to an increasingly steep power law.
 2. *Prior strength:* α defines how many samples from $\mathbf p$ are needed for the data to dominate the prior in predictions, after observing counts $\mathbf F$.
- **Exercise 23.3** (p. 317–318): an additivity property. The exercise asks the reader to show that, for the red/blue Bayesian's inferences to be consistent with those of the six-face Bayesian (Dirichlet with $\mathbf u$), his prior should be Dirichlet with hyperparameters $(u_1+u_2,\ u_3+u_4+u_5+u_6)$.
- **Entropic distribution**, sometimes used in the "maximum entropy" image reconstruction community: $$P(\mathbf p\mid\alpha,\mathbf m)=\frac1{Z(\alpha,\mathbf m)}\exp[-\alpha D_{\rm KL}(\mathbf p\|\mathbf m)]\,\delta\Big(\sum_ip_i-1\Big),\ D_{\rm KL}=\sum_ip_i\log\frac{p_i}{m_i}\tag{23.35}$$ $\mathbf m$ is a positive measure (p. 318).

### 23.6 Further exercise (p. 318)
Exercise 23.4 asks for the maximum-likelihood $s,c$ of a gamma distribution from $N$ points. The chapter also points to MacKay and Peto (1995) for "fun with Dirichlets" (p. 318).

## Toy example (ours)
*Why the 1/x prior is "no length scale".* Take density $P(x)\propto1/x$.
- Mass on $[1,10]$: $\int_1^{10}dx/x=\ln10\approx2.303$.
- Mass on $[10,100]$: $\ln100-\ln10=4.605-2.303=2.303$.
- Equal masses for equal ratios. In $l=\ln x$ the intervals are $[0,2.303]$ and $[2.303,4.605]$, both of length 2.303, as expected for a uniform density in $l$.

*Softmax:* $\mathbf a=(\ln2,0,-\ln2)$ sums to 0. $e^{\mathbf a}=(2,1,0.5)$, $Z=3.5$, so $\mathbf p=(0.571,0.286,0.143)$, which sums to 1.

## Concepts
- [[gaussian-distribution]] (new) — normal density, $\sigma$ = typical deviation; very light tails (p. 312)
- [[heavy-tailed-distribution]] (new) — mixtures of Gaussians, Student-t, Cauchy, biexponential: outliers more probable than under a Gaussian (p. 312–313)
- [[student-t-distribution]] (new) — infinite Gaussian mixture; $n=1$ is Cauchy; $n\to\infty$ is Gaussian (p. 312–313)
- [[gamma-distribution]] (new) — positive-variable density, exponential × $x^{c-1}$ (p. 313)
- [[scale-invariant-prior]] (new) — the 1/x prior, uniform in $\ln x$ (p. 314)
- [[reparameterization-basis]] (new) — choice of ln, logit or softmax coordinates; spikes can be artefacts of basis (p. 314, 316)
- [[beta-distribution]] (new) — density over a probability $p$ (p. 316)
- [[dirichlet-distribution]] (new) — density over probability vectors; α = sharpness / prior strength (p. 316–317)
- [[relative-entropy-kl]] — $D_{\rm KL}(\mathbf p\|\mathbf m)$ in the entropic distribution (p. 318)
- [[maximum-entropy-principle]] — only named as a field using the entropic distribution (p. 318)

## Canonical instances
- [[bent-coin-binomial]] — $N$ flips with bias $f$ (p. 311)
- [[photon-counting-poisson]] — photons per pixel, mean $\lambda$ (p. 311)
- [[wait-for-a-six]] — exponential on integers, $f=5/6$ (p. 311)
- [[bus-in-poissonville]] — exponential wait with mean $s$ (p. 313)
- [[zipf-plot-dirichlet]] — samples for α from 0.1 to 1000 (p. 317)
- [[red-blue-die]] — Dirichlet additivity exercise (p. 317–318)

## Bridges (candidates)
- [same-math] softmax basis (23.33) ↔ machine learning: softmax output layer of a classifier — same normalized-exponential map.
- [structural-analogy] α as sample-size scale of the prior ↔ Bayesian: prior pseudo-counts in conjugate updating (canon link; not stated in this unit).
- [structural-analogy] entropic distribution $\exp[-\alpha D_{\rm KL}]$ ↔ information-theory: Gibbs / exponential-family form.
- [structural-analogy] Gaussian outlier sensitivity ↔ statistics: robust (heavy-tailed) likelihoods.

## Questions this raises
- How can one test, in practice, whether the tails of a real variable are Gaussian (exercise 23.1)?
- Why does the same α give both "sharpness" and "number of samples to dominate the prior"?
- What does the Student-t arise from when the Gaussian's standard deviation is uncertain, concretely?
- Which other bases (besides ln, logit, softmax) remove singularities?

## Exercises worth doing
- Ex. 23.1 (p. 312) — check Gaussian tails on real data in a log histogram — difficulty: easy
- Ex. 23.2 (p. 314) — transform the 1/x density to $u=x^{1/3}$; tests change of variables — difficulty: easy
- Ex. 23.3 (p. 317) — Dirichlet additivity under merging outcomes — difficulty: hard
- Ex. 23.4 (p. 318) — maximum-likelihood fit of gamma parameters — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 323–330 = p. 311–318).
- The text layer is clean enough; equations were checked on the page images.
- (23.3) is printed with a double comma ("on integers,,") and with parentheses for $r\in(0,1,\dots,\infty)$. I read this as the set of integers.
- Invariance is printed as "$x=mx$" (p. 314), presumably meaning rescaling $x\to mx$.
- The Student-t caption of fig. 23.3 labels the parameters $(m,s)$, whereas the text uses $(\mu,s,n)$. The pairing "(1,1) … a Cauchy distribution" suggests that $m$ plays the role of $n$.
- Fig. 23.4's caption prints "10, 0.3" without parentheses for $(s,c)$.
- Figures show parameters and shapes only qualitatively; no numbers were read from them.
