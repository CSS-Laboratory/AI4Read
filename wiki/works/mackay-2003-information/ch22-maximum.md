---
id: mackay-2003-information/ch22-maximum
work: mackay-2003-information
unit: "22 Maximum Likelihood and Clustering"
pages: 300-310
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Maximum Likelihood and Clustering

## L0 — One line
Fitting a mixture of Gaussians by maximum likelihood gives the soft K-means clustering algorithm, but maximum likelihood is not a satisfactory general method (it can have likelihood spikes and unrepresentative maxima), and maximum a posteriori (MAP, maximizing the posterior density instead) often shares these problems and also depends on the parametrization.

## L1 — The gist (≤ 120 words)
Instead of enumerating all hypotheses, maximum likelihood picks the one parameter setting that makes the data most probable. The chapter derives it for one Gaussian, then for a mixture of Gaussians. For the mixture, the update is exactly soft K-means (a clustering algorithm that shares each point between clusters), which is extended to per-cluster widths and axis-aligned Gaussians. Then MacKay shows the method's flaws. A cluster centred on one data point with shrinking variance gives unbounded likelihood. Maxima are atypical in high dimensions. MAP (maximizing the posterior density instead) depends on the choice of parametrization. Exercises extend the ideas to exponential-family models, maximum entropy and ill-posed problems.

**Prerequisites:** logarithms; partial derivatives and Taylor expansion; Gaussian density; conditional probability and Bayes' theorem; the idea of a typical set.

## L2 — Key ideas (5–10 bullets)
- Work with log likelihoods: likelihoods multiply and tend to be very small, while log likelihoods add (p. 300).
- For one Gaussian, ML gives the sample mean, with error bars $\sigma/\sqrt N$; ML for $\ln\sigma$ gives $\sigma^2=S_{\rm tot}/N$, with error bars $1/\sqrt{2N}$ (pp. 300–302).
- Fitting a mixture of Gaussians by an approximate Newton–Raphson step gives the soft K-means update, so clustering can be viewed as mixture-density modelling (pp. 302–303).
- Soft K-means can be enhanced by learning per-cluster widths and weights, or axis-aligned variances; the spherical version is still no good for cigar-shaped clusters, while the axis-aligned version locates them (pp. 303–305).
- ML can blow up: putting a cluster on one data point and shrinking its variance gives arbitrarily large likelihood (overfitting) (p. 306).
- MAP does not make these problems go away: the posterior often has spikes too, its maximum is often unrepresentative, and the MAP answer will usually change under reparametrization (p. 306).
- For exponential-family models, ML sets each model average equal to the data average, which is also the form of the maximum-entropy solution (pp. 308, 310).
- In high dimensions a Gaussian's mass sits in a thin shell far from the density peak (p. 309).

## L3 — Walkthrough

### Introduction (p. 300)
The hypotheses may be exponential in number, so rather than enumerate them all, one can save time by homing in on one good hypothesis. Maximum likelihood instead finds the parameter vector $\boldsymbol\theta$ maximizing $P(\text{Data}\mid\boldsymbol\theta,\mathcal H)$. Sometimes the answer is instant; otherwise an iterative algorithm is needed. It is usually easier to use the log likelihood (p. 300).

### 22.1 Maximum likelihood for one Gaussian
For data $\{x_n\}_{n=1}^N$ (shapes: scalars, $N$ of them):
$$\ln P(\{x_n\}\mid\mu,\sigma)=-N\ln(\sqrt{2\pi}\sigma)-\sum_n (x_n-\mu)^2/(2\sigma^2)\tag{22.1}$$
Define the sample mean and the sum of square deviations:
$$\bar x\equiv\sum_{n=1}^N x_n/N\tag{22.2}$$
$$S\equiv\sum_n(x_n-\bar x)^2\tag{22.3}$$
Then
$$\ln P=-N\ln(\sqrt{2\pi}\sigma)-[N(\mu-\bar x)^2+S]/(2\sigma^2)\tag{22.4}$$
The data enter only through $\bar x$ and $S$, so these are called **sufficient statistics** (p. 300).

**Ex. 22.1 (mean).** For known $\sigma$:
$$\frac{\partial}{\partial\mu}\ln P=-\frac{N(\mu-\bar x)}{\sigma^2}=0\ \text{ when }\mu=\bar x\tag{22.5–22.6}$$
So the ML mean is $\bar x$ for any $\sigma$ (p. 300).

**Error bars.** Taylor-expand the log likelihood about its maximum. The quadratic approximation is used to estimate how far one can move before the likelihood falls by a standard factor such as $e^{1/2}$ or $e^{4/2}$. It is exact when the likelihood is Gaussian in the parameters (p. 301). Figure 22.1 plots the log likelihood against $\mu$ and $\sigma$ for a data set with $N=5$, $\bar x=1.0$, $S=1.0$ (p. 301).

**Ex. 22.2.** The second derivative is
$$\frac{\partial^2}{\partial\mu^2}\ln P=-\frac N{\sigma^2}\tag{22.7}$$
A Gaussian over $\mu$ with standard deviation $\sigma_\mu$ has log curvature $-1/\sigma_\mu^2$. Matching curvatures gives
$$\sigma_\mu=\frac{\sigma}{\sqrt N}\tag{22.8}$$
At $\mu=\bar x\pm\sigma_\mu$ the likelihood is smaller than its maximum by a factor $e^{1/2}$ (p. 301).

**Ex. 22.3 (σ, with known μ).** Let $S_{\rm tot}=\sum_n(x_n-\mu)^2$. Then
$$\ln P=-N\ln(\sqrt{2\pi}\sigma)-\frac{S_{\rm tot}}{2\sigma^2}\tag{22.9}$$
MacKay differentiates with respect to $\ln\sigma$, since $\sigma$ is a scale variable (using $du^n/d(\ln u)=nu^n$) (p. 302):
$$\frac{\partial\ln P}{\partial\ln\sigma}=-N+\frac{S_{\rm tot}}{\sigma^2}\tag{22.10}$$
This is zero when
$$\sigma^2=\frac{S_{\rm tot}}N,\quad\text{i.e. }\sigma=\sqrt{\frac{\sum_n(x_n-\mu)^2}{N}}\tag{22.11–22.12}$$
The second derivative is
$$\frac{\partial^2\ln P}{\partial(\ln\sigma)^2}=-2\frac{S_{\rm tot}}{\sigma^2}\tag{22.13}$$
At the ML value this equals $-2N$, so
$$\sigma_{\ln\sigma}=\frac1{\sqrt{2N}}\tag{22.14}$$
**Ex. 22.4** asks the reader to show that jointly maximizing over $\mu$ and $\ln\sigma$ gives $\{\mu,\sigma\}_{\rm ML}=\{\bar x,\sigma_N=\sqrt{S/N}\}$, with $\sigma_N\equiv\sqrt{\sum_n(x_n-\bar x)^2/N}$ (22.15) (p. 302).

*Intuition note:* The best mean is simply the average, and it is known more precisely when there are more points. The best width is the root-mean-square spread. Error bars measure how sharply the log likelihood curves at its peak.

### 22.2 Maximum likelihood for a mixture of Gaussians (Ex. 22.5)
Model: two Gaussians with a shared $\sigma$, labels $k=1,2$ with prior $p_1=p_2=1/2$:
$$P(x\mid\mu_1,\mu_2,\sigma)=\Big[\sum_{k=1}^2 p_k\tfrac1{\sqrt{2\pi\sigma^2}}\exp\!\Big(-\tfrac{(x-\mu_k)^2}{2\sigma^2}\Big)\Big]\tag{22.16}$$
The data $\{x_n\}$ are independent samples, and $k_n$ is the unknown label of point $n$. The reader is asked to show these claims (p. 302):

- With $\{\mu_k\},\sigma$ known, the class posterior is
$$P(k_n{=}1\mid x_n,\boldsymbol\theta)=\frac1{1+\exp[-(w_1x_n+w_0)]},\quad P(k_n{=}2\mid x_n,\boldsymbol\theta)=\frac1{1+\exp[+(w_1x_n+w_0)]}\tag{22.17}$$
Expressions for $w_1,w_0$ are to be found (p. 303).
- With $\{\mu_k\}$ unknown, the likelihood is $\prod_nP(x_n\mid\{\mu_k\},\sigma)$ (22.18). Let $L$ be its natural log and $p_{k|n}\equiv P(k_n{=}k\mid x_n,\boldsymbol\theta)$. Then
$$\frac{\partial L}{\partial\mu_k}=\sum_np_{k|n}\frac{x_n-\mu_k}{\sigma^2}\tag{22.19}$$
- Neglecting terms in $\partial P(k_n{=}k\mid x_n,\boldsymbol\theta)/\partial\mu_k$,
$$\frac{\partial^2L}{\partial\mu_k^2}\approx-\sum_np_{k|n}\frac1{\sigma^2}\tag{22.20}$$
- The Newton–Raphson update $\mu'=\mu-\big[\frac{\partial L}{\partial\mu}/\frac{\partial^2L}{\partial\mu^2}\big]$ becomes approximately
$$\mu_k'=\frac{\sum_np_{k|n}x_n}{\sum_np_{k|n}}\tag{22.21}$$
*(added step)* Substituting (22.19) and (22.20): $\mu_k'=\mu_k+\frac{\sum_np_{k|n}(x_n-\mu_k)}{\sum_np_{k|n}}=\frac{\sum_np_{k|n}x_n}{\sum_np_{k|n}}$.

The exercise also asks for a contour sketch of the likelihood against $(\mu_1,\mu_2)$ for a 32-point data set with $\sigma=1$ (p. 303). The printed solution (Figure 22.10) shows peaks near $(1,5)$ and $(5,1)$, with nearly circular contours and roughly Gaussian shape. Each peak has width $\sigma/\sqrt{16}=1/4$ (p. 310).

MacKay notes this algorithm is identical to soft K-means of section 20.4. Clustering can therefore be seen as mixture-density modelling, which allows enhancements (p. 303).

*Intuition note:* Each data point is shared between clusters in proportion to how probable each cluster is for it. Each mean moves to the weighted average of the points. Reading clustering as a probability model tells us how to improve it.

### 22.3 Enhancements to soft K-means
**Algorithm 22.2 (version 2).** Each cluster is a spherical Gaussian with its own width ($\beta^{(k)}=1/\sigma_k^2$) and weight $\pi_k$, and both are learned. Here $I$ is the dimension of $\mathbf x$, and $d(\cdot,\cdot)$ is not defined on these pages (p. 304).
$$r_k^{(n)}=\frac{\pi_k\frac1{(\sqrt{2\pi}\sigma_k)^I}\exp\!\big(-\frac1{\sigma_k^2}d(\mathbf m^{(k)},\mathbf x^{(n)})\big)}{\sum_{k'}\pi_{k'}\frac1{(\sqrt{2\pi}\sigma_{k'})^I}\exp\!\big(-\frac1{\sigma_{k'}^2}d(\mathbf m^{(k')},\mathbf x^{(n)})\big)}\tag{22.22}$$
$$\mathbf m^{(k)}=\frac{\sum_nr_k^{(n)}\mathbf x^{(n)}}{R^{(k)}}\tag{22.23}$$
$$\sigma_k^2=\frac{\sum_nr_k^{(n)}(\mathbf x^{(n)}-\mathbf m^{(k)})^2}{IR^{(k)}}\tag{22.24}$$
$$\pi_k=\frac{R^{(k)}}{\sum_kR^{(k)}},\qquad R^{(k)}=\sum_nr_k^{(n)}\tag{22.25–22.26}$$
Figure 22.3 shows it on two earlier data sets; for the "little 'n' large" set, convergence can take a long time, but eventually it identifies both clusters (pp. 303, 305). A proof that the algorithm maximizes the likelihood is deferred to section 33.7 (p. 305).

Version 2 fits spherical Gaussians, which have equal variance in all directions. It is still no good for the cigar-shaped clusters (p. 305).

**Algorithm 22.4 (version 3), axis-aligned Gaussians.** Replace (22.22) and (22.24) by (p. 304):
$$r_k^{(n)}=\frac{\pi_k\frac1{\prod_{i=1}^I\sqrt{2\pi}\sigma_i^{(k)}}\exp\!\big(-\sum_{i=1}^I(m_i^{(k)}-x_i^{(n)})^2/2(\sigma_i^{(k)})^2\big)}{\sum_{k'}(\text{numerator, with }k'\text{ in place of }k)}\tag{22.27}$$
$$\sigma_i^{2(k)}=\frac{\sum_nr_k^{(n)}(x_i^{(n)}-m_i^{(k)})^2}{R^{(k)}}\tag{22.28}$$
After 30 iterations it locates the two cigars, and it also finds the correct clusters in the "little 'n' large" data (Figs 22.5, 22.6) (p. 305).

### 22.4 A fatal flaw of maximum likelihood
With $K=4$ on the first toy data set, versions 2 and 3 sometimes form very small clusters covering one or two points (Fig. 22.7) (p. 305). **Ex. 22.6** asks the reader to show that if a mean sits on one data point and $\sigma_k^2$ is small enough, no return is possible: $\sigma_k^2$ keeps shrinking (p. 305).

"KABOOM!": a cluster on one data point with variance going to zero gives arbitrarily large likelihood. ML can find highly tuned models that fit part of the data perfectly; this is **overfitting**. These settings may have huge posterior *density*, but only over a tiny volume, so their probability *mass* is usually tiny (p. 306).

MacKay concludes that ML is not a satisfactory general solution. The likelihood may be infinite at some settings. Even without spikes, its maximum is often unrepresentative in high dimensions. Even in low dimensions the ML estimator $\sigma_N$ (22.15) is biased, a topic for Chapter 24 (p. 306).

**MAP.** Maximizing the posterior density instead does not remove these problems (p. 306):
- the posterior often has infinite spikes too;
- its maximum is often unrepresentative of the whole posterior;
- in high dimensions most mass is in a typical set, unlike the maximum-density points, so "maxima are atypical";
- MAP is basis-dependent. Under a nonlinear change $u=f(\theta)$,
$$P(u)=P(\theta)\left|\frac{\partial\theta}{\partial u}\right|\tag{22.29}$$
and the maximum of $P(u)$ will usually not coincide with that of $P(\theta)$.

*Intuition note:* A tall, narrow spike can hold almost no probability, so the highest point of a density is a poor summary. A good method should not change its answer when we rename the parameter.

Further reading: soft K-means is at the heart of the AutoClass package (p. 306).

### 22.5 Further exercises (pp. 306–310)
- **22.7:** build K-means for $K$ arbitrary (not axis-aligned) Gaussians (p. 306).
- **22.8:** Poisson photon counts (22.30), $P(r\mid\lambda)=e^{-\lambda}\lambda^r/r!$. Find the ML $\lambda$ for $r=9$ with error bars on $\ln\lambda$. Then repeat with known background $b=13$, and compare with the Bayesian posterior and the "unbiased" $\hat\lambda=r-b$ (p. 307).
- **22.9:** bent coin, with ML and MAP values of $p$ and of the logit $a=\ln[p/(1-p)]$, compared with the predictive probability (p. 307).
- **22.10:** stars seen through a rectangular window; find the ML window edges and sketch the likelihood against $x_{\max}$ (p. 307).
- **22.11:** a sailor locates himself from three noisy bearings by ML; compare with the "cocked hat" rule of thumb (p. 307).
- **22.12 (exponential family).** Let $P(\mathbf x\mid\mathbf w)=\frac1{Z(\mathbf w)}\exp(\sum_kw_kf_k(\mathbf x))$ (22.31). The printed solution (p. 310) is:
$$\ln P(\{\mathbf x^{(n)}\}\mid\mathbf w)=-N\ln Z(\mathbf w)+\sum_n\sum_kw_kf_k(\mathbf x^{(n)})\tag{22.37}$$
$$\frac{\partial}{\partial w_k}\ln P=-N\frac{\partial}{\partial w_k}\ln Z(\mathbf w)+\sum_nf_k(\mathbf x^{(n)})\tag{22.38}$$
$$\frac{\partial}{\partial w_k}\ln Z=\frac1{Z}\sum_{\mathbf x}\exp\Big(\sum_{k'}w_{k'}f_{k'}(\mathbf x)\Big)f_k(\mathbf x)=\sum_{\mathbf x}P(\mathbf x\mid\mathbf w)f_k(\mathbf x)\tag{22.39}$$
$$\frac{\partial}{\partial w_k}\ln P=-N\sum_{\mathbf x}P(\mathbf x\mid\mathbf w)f_k(\mathbf x)+\sum_nf_k(\mathbf x^{(n)})\tag{22.40}$$
Setting this to zero at the maximum gives
$$\sum_{\mathbf x}P(\mathbf x\mid\mathbf w_{\rm ML})f_k(\mathbf x)=\frac1N\sum_nf_k(\mathbf x^{(n)})\tag{22.41, = 22.32}$$
In shorthand, $\langle f_k\rangle_{P(\mathbf x\mid\mathbf w_{\rm ML})}=\langle f_k\rangle_{\rm Data}$ (22.33) (p. 308).
*Intuition note:* At the best fit, the model reproduces the data's averages of the chosen functions.
- **22.13 (maxent).** Maximize $H=\sum_{\mathbf x}P(\mathbf x)\log1/P(\mathbf x)$ (22.34) subject to $\langle f_k\rangle_{P}=F_k$ (22.35). Using Lagrange multipliers (one per constraint, including normalization), the solution has the form $P(\mathbf x)_{\rm Maxent}=\frac1Z\exp(\sum_kw_kf_k(\mathbf x))$ (22.36). So maxent matches ML fitting of an exponential-family model (p. 308). **MacKay's view:** he does not advocate maxent as *the* way to assign priors. He thinks maxent is a bad way to solve inference problems, because it can give silly answers; the correct way is Bayes' theorem (p. 308).
- **22.14 (typicality).** For a $k$-dimensional Gaussian with $\sigma_W$, nearly all mass is in a thin shell of radius $r=\sqrt k\sigma_W$ and thickness proportional to $r/\sqrt k$. For $k=1000$, $\sigma_W=1$: 90% of the mass is in a shell of radius 31.6 and thickness 2.8, yet the density at the origin is $e^{k/2}\simeq10^{217}$ times that at the shell. Two Gaussians whose $\sigma_W$ differ by 1% and which have equal mass: the density maximum is higher for the narrower one by a factor $\sim\exp(0.01k)\simeq20\,000$. The exercise adds that in ill-posed problems a typical posterior is often a weighted superposition of Gaussians, so the true posterior has a skew peak whose maximum density is located near the mean of the Gaussian with the smallest standard deviation, not the one with the greatest weight (p. 309).
- **22.15 (seven scientists).** Seven measurements of a common $\mu$ with unknown, different $\sigma_n$ (data in Fig. 22.9: $-27.020$, 3.570, 8.191, 9.898, 9.603, 9.945, 10.056). MacKay hopes the reader agrees that, intuitively, it looks pretty certain that A and B are inept, D–G better, and that $\mu$ is somewhere close to 10. The question is what maximizing the likelihood says (p. 309).
- **22.16 (MAP problems).** Widgets with Gaussian prior and unknown $\sigma_W$. Scenario 1 (four data points) gives two maxima of $P(\mathbf w\mid\mathbf d)$. Scenario 2 adds four vacuous measurements and leaves one maximum with all eight values near zero. In the printed answers, the Scenario 1 maximum near $\{1.8,-1.8,2.2,-2.2\}$ is absent in Scenario 2, although the added data are described as uninformative; the text asks what happens to the MAP method and states no conclusion (pp. 309–310).

## Toy example (ours)
**Soft K-means step in one dimension.** Take equal weights $p_1=p_2=1/2$, $\mu_1=0$, $\mu_2=4$, $\sigma=1$, data $\{1,3\}$.

- The log odds are $\ln\frac{P(k{=}1\mid x)}{P(k{=}2\mid x)}=\frac{(x-4)^2-x^2}{2}=8-4x$. So $w_1=-4$, $w_0=8$ in (22.17).
- At $x=1$: $p_{1|1}=1/(1+e^{-4})=1/1.0183=0.9820$, so $p_{2|1}=0.0180$.
- At $x=3$: log odds $=-4$, so $p_{1|2}=0.0180$ and $p_{2|2}=0.9820$.
- Update (22.21): $\mu_1'=(0.9820\cdot1+0.0180\cdot3)/(0.9820+0.0180)=1.036/1.000=1.036$. $\mu_2'=(0.0180\cdot1+0.9820\cdot3)/1.000=2.964$.

Both means move towards the data points they are responsible for.

**The spike.** Put $\mu_1$ on a data point and shrink $\sigma$. That point's density factor is $1/(\sqrt{2\pi}\sigma)$: 3.99 at $\sigma=0.1$ and 39.9 at $\sigma=0.01$, growing without bound as $\sigma\to0$.

## Concepts
- [[maximum-likelihood]] (new) — choose parameters $\boldsymbol\theta$ maximizing $P(\text{Data}\mid\boldsymbol\theta,\mathcal H)$ (p. 300)
- [[likelihood]] — probability of the data as a function of the parameters; in practice, work with its log (p. 300)
- [[sufficient-statistic]] (new) — functions of the data (here $\bar x$, $S$) through which the likelihood depends on the data (p. 300)
- [[error-bars-quadratic-approximation]] (new) — Taylor-expand the log likelihood at its peak to get widths; exact for Gaussian-shaped likelihood (p. 301)
- [[mixture-of-gaussians]] (new) — density as weighted sum of Gaussians with unknown class labels (p. 302)
- [[soft-k-means]] (new) — iterate responsibilities and weighted-mean updates; an ML algorithm for fitting a mixture of Gaussians (pp. 303–305)
- [[responsibility]] (new) — $r_k^{(n)}$ or $p_{k|n}$: posterior probability that point $n$ belongs to cluster $k$ (pp. 303–304)
- [[overfitting]] (new) — ML finds highly tuned models that fit part of the data perfectly (p. 306)
- [[map-estimate]] (new) — maximizing the posterior density; it often shares ML's problems, and its answer usually changes with the parametrization (p. 306)
- [[typical-set]] — in high dimensions most mass lies in a set unlike the max-density points (p. 306)
- [[maximum-entropy-principle]] — maximize $H$ under average constraints; the solution is exponential-family (p. 308)
- [[exponential-family]] — $P\propto\exp(\sum w_kf_k)$; ML matches model averages to data averages (p. 307)

## Canonical instances
- [[gaussian-ml-error-bars]] — $\bar x$, $\sigma/\sqrt N$, $\sigma_N$, $1/\sqrt{2N}$ (pp. 300–302)
- [[soft-kmeans-little-n-large]] — spherical and axis-aligned fits on the unequal-cluster data (pp. 303–305)
- [[kmeans-spike-kaboom]] — a cluster on one point makes the likelihood infinite (p. 306)
- [[seven-scientists]] — ML on unknown, unequal noise levels (p. 309)
- [[gaussian-shell-1000d]] — 1000-dimensional Gaussian mass concentrated in a thin shell (p. 309)
- [[cocked-hat-sailor]] — three bearings, ML position vs rule of thumb (p. 307)

## Bridges (candidates)
- [same-math] Soft K-means update (22.21) ↔ Expectation–Maximization for Gaussian mixtures — the same weighted-mean update; these pages never mention EM, and say only that a proof that the algorithm maximizes the likelihood is deferred to section 33.7 (p. 305).
- [same-math] ML for exponential families (22.32) ↔ information theory: maxent solution (22.36) — both give the same exponential form, as shown on p. 308.
- [structural-analogy] ML overfitting (likelihood spikes) ↔ Bayesian: mass vs density — a tall spike with tiny volume carries tiny probability (p. 306).
- [structural-analogy] MAP basis dependence (22.29) ↔ Bayesian: Jacobian of a density under change of variables — densities transform with $|\partial\theta/\partial u|$, so maxima move.

## Questions this raises
- If MAP and ML are unreliable, what does the full Bayesian treatment of a mixture model do (the book's next chapters)?
- How biased is $\sigma_N$, and what replaces it (Chapter 24, p. 306)?
- When is the "neglect $\partial p_{k|n}/\partial\mu_k$" Newton step a good approximation?
- Can a prior on $\sigma_k$ stop the spike in soft K-means, and would it avoid the basis problem?

## Exercises worth doing
- Ex. 22.5 (p. 302) — derive soft K-means from a Gaussian mixture by a Newton step, and sketch the likelihood contours — difficulty: medium
- Ex. 22.6 (p. 305) — show why a collapsing cluster never recovers (overfitting) — difficulty: medium
- Ex. 22.8 (p. 307) — Poisson ML with a known background, compared with the Bayesian and "unbiased" answers — difficulty: medium
- Ex. 22.9 (p. 307) — ML vs MAP in $p$ and in the logit, compared with the predictive probability (shows basis dependence) — difficulty: medium
- Ex. 22.14 (p. 309) — Gaussian shell and the density at the origin (why maxima are atypical) — difficulty: medium
- Ex. 22.15 (p. 309) — ML on the seven-scientists data (ML's failure in an ill-posed problem) — difficulty: hard

## Reading notes
- Printed page = pdf page − 12 (pdf 312 = printed 300).
- Figure/equation text layers are garbled for (22.22), (22.27), (22.28); equations here follow the page images.
- $d(\mathbf m,\mathbf x)$ in (22.22) is not defined on these pages. (Our observation: for exact Gaussian responsibilities the exponent would need $d=\tfrac12|\mathbf m-\mathbf x|^2$; the pages do not say this.)
- Exercise 22.5 states $\sigma$ as a standard deviation in (22.16); Ex. 22.4 uses $\{\mu,\sigma\}_{\rm ML}$ with $\sigma_N$ as printed.
- On these pages, solutions are printed only for Ex. 22.5 (Fig. 22.10) and Ex. 22.12; some answers to Ex. 22.16 are printed inside the exercise.
- In the printed solution to Ex. 22.12, equations (22.38) and (22.40) show $\sum_n f_k(\mathbf x)$; the digest writes $f_k(\mathbf x^{(n)})$, which is the evident intended form.
- Page heading: "22 — Maximum Likelihood and Clustering"; Copyright Cambridge University Press 2003.
