---
id: murphy-2023-pml2/ch11-monte
work: murphy-2023-pml2
unit: 11 Monte Carlo methods
pages: 483-498
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Monte Carlo methods

## L0 — One line
Replace a hard integral (an expectation) by an average over random samples, whose error shrinks like $1/\sqrt{N_s}$ in principle whatever the dimension, and then work on how to generate good samples and how to cut the variance.

## L1 — The gist (≤ 120 words)
How can we compute $\mathbb{E}[f(X)]$ when grid integration fails in high dimension? Draw samples from the target and average $f$ over them. The standard error is $\hat\sigma/\sqrt{N_s}$, in principle independent of dimension. The catch is generating samples. The chapter covers exact sampling for simple distributions (inverse cdf, Box-Muller), rejection sampling (which degrades exponentially with dimension), and importance sampling, including self-normalized and annealed versions that also estimate normalizing constants. It ends with variance-reduction tools: common random numbers, Rao-Blackwellization, control variates, antithetic sampling and quasi-Monte Carlo. This matters because posterior expectations in Bayesian inference are such integrals.

**Prerequisites:** expectation and variance; cdf and change of variables; central limit theorem; Markov chain (basic idea); covariance and correlation; derivative of a quadratic.

## L2 — Key ideas (5–10 bullets)
- MC integration approximates $\mathbb{E}[f(x)]$ by $\frac1{N_s}\sum f(x_n)$ and evaluates $f$ only where probability is non-negligible (p. 483–484).
- By the central limit theorem (CLT), the error is approximately $\mathcal N(0,\sigma^2/N_s)$. For large $N_s$, an approximate 95% interval is $\hat\mu \pm 1.96\,\hat\sigma/\sqrt{N_s}$. The error is dimension-independent in principle, but sampling is the hard part (p. 485).
- Inverse-cdf sampling is exact: $F^{-1}(U)\sim F$ for uniform $U$. Box-Muller (uniform points in a circle) and a Cholesky factor of the covariance matrix turn uniforms into Gaussian samples (p. 486–487).
- Rejection sampling needs an envelope $Cq\ge\tilde p$; accepted points follow $p$ and the acceptance rate is $1/C$ for a normalized target. In a Gaussian example $C=(\sigma_q/\sigma_p)^D$, so the acceptance rate falls exponentially with dimension, which the author calls a fundamental weakness (p. 488–490).
- Importance sampling reweights proposal samples by $\pi/q$. The direct version is unbiased. The self-normalized version works with unnormalized targets, is biased, and also estimates $Z$ (p. 491–492).
- Annealed importance sampling links an easy distribution to a hard one through a ladder of intermediate (tempered) distributions. It can estimate ratios of normalizing constants, and is generally considered the method of choice for difficult partition functions (p. 492–494).
- Variance reduction: Rao-Blackwellization (replace a sample by its conditional expectation), control variates (subtract a correlated term with known mean), antithetic sampling (use negatively correlated pairs) and common random numbers (reuse the same noise). On the worked example, the standard error falls from 0.0037 to 0.0007 (p. 494–497).
- Quasi-MC uses low-discrepancy (evenly spread) point sequences with error $O((\log N)^D/N)$; randomized QMC restores an uncertainty estimate (p. 497–498).

## L3 — Walkthrough

### 11.1 Introduction (p. 483)
MC methods solve numerical integration problems stochastically. The chapter is a brief introduction. MCMC comes in Chapter 12 and SMC in Chapter 13.

### 11.2 Monte Carlo integration (p. 483–485)
Target: $\mathbb{E}[f(x)]=\int f(x)p(x)\,dx$ with $x\in\mathbb R^n$, $f:\mathbb R^n\to\mathbb R^m$ \tag{11.1}. If $p$ is a posterior, one may work with the unnormalized $\tilde p(x)=p(x,y)$ and normalize with $Z=\int p(x,y)dx=p(y)$ (footnote 1, p. 483).

Grid-based numerical integration (quadrature in 1d, cubature in higher dimensions) is efficient in low dimension (up to, say, 3) but does not scale (p. 483). MC integration draws $x_n\sim p(x)$ and computes
$$\mathbb{E}[f(x)]\approx\frac1{N_s}\sum_{n=1}^{N_s}f(x_n)\tag{11.2}$$
It evaluates $f$ only where there is non-negligible probability. Its accuracy is in principle independent of dimension and depends only on $N_s$. The catch is that we need a way to sample from $p$, and the estimator may have high variance (p. 483–484).

**11.2.1 Example: estimating $\pi$ (p. 484).** The circle's area is $\pi r^2$ and also
$$I=\int_{-r}^{r}\int_{-r}^{r}\mathbb I(x^2+y^2\le r^2)\,dx\,dy,\tag{11.3}$$
so $\pi=I/r^2$. Let $f(x,y)=\mathbb I(x^2+y^2\le r^2)$ and $p(x)=p(y)=1/(2r)$ uniform on $[-r,r]$. Then
$$I=(2r)(2r)\iint f\,p(x)p(y)\,dx\,dy=4r^2\iint f\,p(x)p(y)\,dx\,dy\approx 4r^2\frac1{N_s}\sum_{n=1}^{N_s}f(x_n,y_n)\tag{11.4–11.6}$$
With 5000 samples: $\hat\pi=3.10$, standard error 0.09, true value 3.14 (p. 484).

**11.2.2 Accuracy (p. 484–485).** Let $\mu=\mathbb E[f(X)]$ and $\hat\mu$ the MC estimate. With independent samples,
$$(\hat\mu-\mu)\to\mathcal N\!\left(0,\frac{\sigma^2}{N_s}\right)\tag{11.7}$$
$$\sigma^2=\mathbb V[f(X)]=\mathbb E[f(X)^2]-\mathbb E[f(X)]^2\tag{11.8}$$
This follows from the central limit theorem. Since $\sigma^2$ is unknown, estimate it by MC:
$$\hat\sigma^2=\frac1{N_s}\sum_{n=1}^{N_s}(f(x_n)-\hat\mu)^2\tag{11.9}$$
For large enough $N_s$,
$$P\left\{\hat\mu-1.96\frac{\hat\sigma}{\sqrt{N_s}}\le\mu\le\hat\mu+1.96\frac{\hat\sigma}{\sqrt{N_s}}\right\}\approx0.95\tag{11.10}$$
The term $\sqrt{\hat\sigma^2/N_s}$ is the (numerical or empirical) **standard error**. To be accurate within $\pm\epsilon$ with probability at least 95%, require $1.96\sqrt{\hat\sigma^2/N_s}\le\epsilon$. Approximating 1.96 by 2 gives $N_s\ge 4\hat\sigma^2/\epsilon^2$ (p. 485). Figure 11.2 shows 10 and 100 Gaussian samples; the kernel density curve is only for plotting, not part of the estimate (p. 484–485).

*Intuition note.* The average of $N_s$ independent draws wobbles around the truth by about $\sigma/\sqrt{N_s}$. To halve the error you need four times the samples. The dimension of $x$ never appears; it only hides inside how hard sampling is.

### 11.3 Sampling from simple distributions (p. 486–487)
The main challenge is generating samples from $p^*(x)$, possibly a posterior. This section gives building blocks for univariate parametric distributions (p. 486).

**11.3.1 Inverse cdf (p. 486–487).** *Theorem 11.3.1:* if $U\sim U(0,1)$ then $F^{-1}(U)\sim F$. Proof:
$$\Pr(F^{-1}(U)\le x)=\Pr(U\le F(x))=F(x)\tag{11.11–11.12}$$
The first step uses that $F$ is monotonic, the second that $U$ is uniform. Recipe: draw $u$, read off $x=F^{-1}(u)$ (Figure 11.3). Example: $\mathrm{Expon}(x|\lambda)=\lambda e^{-\lambda x}\mathbb I(x\ge0)$ \tag{11.13}, with $F(x)=1-e^{-\lambda x}$ \tag{11.14}, so $F^{-1}(p)=-\ln(1-p)/\lambda$ \tag{11.15}. Since $1-U\sim\mathrm{Unif}(0,1)$, one can use $-\ln(u)/\lambda$ (p. 487).

**11.3.2 Box-Muller (p. 487).** Sample $z_1,z_2\in(-1,1)$ uniformly and discard pairs with $z_1^2+z_2^2>1$. The kept points are uniform in the unit circle, $p(z)=\frac1\pi\mathbb I(z\text{ inside circle})$. Define, with $r^2=z_1^2+z_2^2$,
$$x_i=z_i\left(\frac{-2\ln r^2}{r^2}\right)^{1/2},\quad i=1,2\tag{11.16}$$
The multivariate change-of-variables formula gives
$$p(x_1,x_2)=p(z_1,z_2)\left|\frac{\partial(z_1,z_2)}{\partial(x_1,x_2)}\right|=\Big[\tfrac1{\sqrt{2\pi}}e^{-x_1^2/2}\Big]\Big[\tfrac1{\sqrt{2\pi}}e^{-x_2^2/2}\Big]\tag{11.17}$$
so $x_1,x_2$ are two independent univariate Gaussian samples. For a multivariate Gaussian: compute the Cholesky factor $\Sigma=LL^\top$ ($L$ lower triangular), sample $x\sim\mathcal N(0,I)$, set $y=Lx+\mu$. This is valid because
$$\mathrm{Cov}[y]=L\,\mathrm{Cov}[x]\,L^\top=LIL^\top=\Sigma\tag{11.18}$$

### 11.4 Rejection sampling (p. 487–490)
Target $p(x)=\tilde p(x)/Z_p$ \tag{11.19}, $Z_p=\int\tilde p(x)dx$ \tag{11.20}, possibly unknown (p. 487).

**11.4.1 Basic idea (p. 488–489).** We need a proposal $q$ and constant $C$ with $Cq(x)\ge\tilde p(x)$ (an upper envelope). Sample $x_0\sim q$, then $u_0\sim\mathrm{Unif}(0,Cq(x_0))$. Reject if $u_0>\tilde p(x_0)$, else accept. Proof of correctness:
$$q(\text{accept}|x_0)=\int_0^{\tilde p(x_0)}\frac{du}{Cq(x_0)}=\frac{\tilde p(x_0)}{Cq(x_0)}\tag{11.21}$$
$$q(\text{propose and accept }x_0)=q(x_0)\,q(\text{accept}|x_0)=\frac{\tilde p(x_0)}{C}\tag{11.22}$$
$$\int q(x_0)q(\text{accept}|x_0)dx_0=q(\text{accept})=\frac{\int\tilde p(x_0)dx_0}{C}=\frac{Z_p}{C}\tag{11.23}$$
$$q(x_0|\text{accept})=\frac{q(x_0,\text{accept})}{q(\text{accept})}=\frac{\tilde p(x_0)}{C}\frac{C}{Z_p}=\frac{\tilde p(x_0)}{Z_p}=p(x_0)\tag{11.24}$$
If $\tilde p$ is normalized, the acceptance probability is $1/C$, so choose $C$ as small as possible while keeping $Cq\ge\tilde p$ (p. 489).

**11.4.2 Example: gamma (p. 489).** $\mathrm{Ga}(x|\alpha,\lambda)=\frac1{\Gamma(\alpha)}x^{\alpha-1}\lambda^\alpha e^{-\lambda x}$ \tag{11.25}. If $X_i\overset{iid}\sim\mathrm{Expon}(\lambda)$ and $Y=X_1+\dots+X_k$, then $Y\sim\mathrm{Ga}(k,\lambda)$. This trick fails for non-integer $\alpha$, so use the proposal $\mathrm{Ga}(k,\lambda-1)$ with $k=\lfloor\alpha\rfloor$:
$$\frac{p(x)}{q(x)}=\frac{x^{\alpha-1}\lambda^\alpha e^{-\lambda x}/\Gamma(\alpha)}{x^{k-1}(\lambda-1)^k e^{-(\lambda-1)x}/\Gamma(k)}=\frac{\Gamma(k)\lambda^\alpha}{\Gamma(\alpha)(\lambda-1)^k}x^{\alpha-k}e^{-x}\tag{11.26–11.27}$$
This ratio is maximal at $x=\alpha-k$, so
$$C=\frac{\mathrm{Ga}(\alpha-k|\alpha,\lambda)}{\mathrm{Ga}(\alpha-k|k,\lambda-1)}\tag{11.28}$$
Figure 11.4(b) uses $\alpha=5.7$, $\lambda=2$, $k=5$; the curves touch at $\alpha-k=0.7$ (p. 488–489).

**11.4.3 Adaptive rejection sampling (p. 489).** For a log-concave 1d density, bound the log density by a piecewise linear function with tangent lines at grid points. The envelope is then piecewise exponential:
$$q(x)=C_i\lambda_i\exp(-\lambda_i(x-x_{i-1})),\quad x_{i-1}<x\le x_i\tag{11.29}$$
Sampling from it is "relatively straightforward". When a sample is rejected, add a grid point there. The envelope tightens and the rejection rate falls. This is ARS and it works on unnormalized densities.

**11.4.4 High dimensions (p. 490).** Take $p=\mathcal N(0,\sigma_p^2I)$ and $q=\mathcal N(0,\sigma_q^2I)$, with $\sigma_q^2\ge\sigma_p^2$ needed for an upper bound. In $D$ dimensions the optimum is $C=(\sigma_q/\sigma_p)^D$ and the acceptance rate $1/C$ falls exponentially. If $\sigma_q$ exceeds $\sigma_p$ by 1%, in 1000 dimensions acceptance is about $1/20{,}000$. The author calls this a fundamental weakness.

*Intuition note.* Rejection sampling throws darts under an envelope and keeps those under the target curve. Any gap between envelope and target wastes darts, and in many dimensions the gap multiplies across coordinates.

### 11.5 Importance sampling (p. 490–494)
Goal: $\mathbb E[\varphi(x)]=\int\varphi(x)\pi(x)dx$ \tag{11.30}, where $\varphi$ is the target function and $\pi$ the target distribution (often $p(x|y)$). Draw from a proposal $q$ and attach weights: $\mathbb E[\varphi]\approx\sum_nW_n\varphi(x_n)$ \tag{11.31} (p. 490).

**11.5.1 Direct IS (p. 491).** Assume $\pi$ can be evaluated (normalized) but not sampled. Write $\int\varphi\pi\,dx=\int\varphi\frac{\pi}{q}q\,dx$ \tag{11.32}. The support of $q$ must be at least that of $\pi$. Then
$$\mathbb E[\varphi]\approx\frac1{N_s}\sum_n\frac{\pi(x_n)}{q(x_n)}\varphi(x_n)=\frac1{N_s}\sum_n\tilde w_n\varphi(x_n),\quad\tilde w_n=\frac{\pi(x_n)}{q(x_n)}\tag{11.33–11.34}$$
This is an unbiased estimate.

**11.5.2 Self-normalized IS (p. 491–492).** Often it is much easier to evaluate the unnormalized $\tilde\gamma(x)=Z\pi(x)$ \tag{11.35}, where $Z=\int\tilde\gamma$ \tag{11.36} (e.g. $\tilde\gamma=p(x,y)$, $Z=p(y)$). Approximate $Z$ by IS too:
$$\mathbb E[\varphi]=\frac{\int\varphi\tilde\gamma\,dx}{\int\tilde\gamma\,dx}=\frac{\int\left[\frac{\tilde\gamma}{q}\varphi\right]q\,dx}{\int\frac{\tilde\gamma}{q}q\,dx}\approx\frac{\frac1{N_s}\sum_n\tilde w_n\varphi(x_n)}{\frac1{N_s}\sum_n\tilde w_n}\tag{11.37–11.38}$$
with unnormalized weights $\tilde w_n=\tilde\gamma(x_n)/q(x_n)$ \tag{11.39}. Compactly $\mathbb E[\varphi]\approx\sum_nW_n\varphi(x_n)$ \tag{11.40} with $W_n=\tilde w_n/\sum_{n'}\tilde w_{n'}$ \tag{11.41}. This equals approximating $\pi$ by weighted deltas, $\hat\pi(x)=\sum_nW_n\delta(x-x_n)$ \tag{11.42}, and gives $Z\approx\hat Z=\frac1{N_s}\sum_n\tilde w_n$ \tag{11.43}. The estimate is a ratio of two estimates, hence biased. The bias goes to zero as $N_s\to\infty$ under some weak assumptions.

**11.5.3 Choosing the proposal (p. 492).** Performance depends crucially on $q$. It must cover the target's support ($\tilde\gamma>0\Rightarrow q>0$) but not too loosely. Ideally it also accounts for $\varphi$ (Figure 11.6; "target aware Bayesian inference" of [Rai+20]), but usually $\varphi$ is unknown or ignored. One can learn $q$ by optimizing the ELBO. With the generative model's parameters fixed, importance weighted autoencoders can be seen as learning a good proposal.

**11.5.4 Annealed IS (p. 492–494).** Target $p_0\propto f_0$ is hard (e.g. high-dimensional or multimodal); an easy $p_n\propto f_n$ (e.g. the prior) can be sampled. Intermediate distributions:
$$f_j(x)=f_0(x)^{\beta_j}f_n(x)^{1-\beta_j},\quad1=\beta_0>\beta_1>\dots>\beta_n=0\tag{11.44}$$
($\beta_j$ is an inverse temperature.) Suppose Markov chains $T_j(x,x')=p_j(x'|x)$ are available that leave the distribution invariant (as printed: $p_0$; see Reading notes). Procedure: sample $v_n\sim p_n$, $v_{n-1}\sim T_{n-1}(v_n,\cdot)$, …, $v_0\sim T_0(v_1,\cdot)$. Set $x=v_0$ with weight
$$w=\frac{f_{n-1}(v_{n-1})}{f_n(v_{n-1})}\frac{f_{n-2}(v_{n-2})}{f_{n-1}(v_{n-2})}\cdots\frac{f_1(v_1)}{f_2(v_1)}\frac{f_0(v_0)}{f_1(v_0)}\tag{11.45}$$
*Why it is correct:* view it as IS on the extended space $v=(v_0,\dots,v_n)$. The target is
$$p(v)\propto\varphi(v)=f_0(v_0)\tilde T_0(v_0,v_1)\tilde T_2(v_1,v_2)\cdots\tilde T_{n-1}(v_{n-1},v_n)\propto p(v_0)p(v_1|v_0)\cdots p(v_n|v_{n-1})\tag{11.46–11.47}$$
where $\tilde T_j$ is the reversal of $T_j$:
$$\tilde T_j(v,v')=T_j(v',v)p_j(v')/p_j(v)=T_j(v',v)f_j(v')/f_j(v)\tag{11.48}$$
Summing out $v_1,\dots,v_n$ gives $f_0(v_0)$, so sampling $p(v)$ effectively samples $p_0$. The algorithm uses the proposal
$$q(v)\propto g(v)=f_n(v_n)T_{n-1}(v_n,v_{n-1})\cdots T_2(v_2,v_1)T_0(v_1,v_0)\propto p(v_n)p(v_{n-1}|v_n)\cdots p(v_1|v_0)\tag{11.49–11.50}$$
The author states that the weights $\varphi(v)/g(v)$ equal (11.45); no derivation is given (p. 494).

**11.5.4.1 Normalizing constants (p. 494).** $Z_0=\int f_0=\int\varphi(v)dv$ and $Z_n=\int f_n=\int g(v)dv$, hence
$$\frac{Z_0}{Z_n}=\frac{\int\frac{\varphi}{g}g\,dv}{\int g\,dv}=\mathbb E_g\!\left[\frac{\varphi(v)}{g(v)}\right]\approx\frac1S\sum_{s=1}^Sw_s\tag{11.51}$$
If $f_0$ is a prior with known $Z_0$ and $f_n$ the posterior, this estimates $Z_n=p(\mathcal D)$. It is "generally considered the method of choice" for difficult partition functions.

*Intuition note.* IS fixes a wrong sampling distribution by reweighting, so a sample the proposal over-produces counts less. AIS moves gradually from an easy distribution to the hard one through intermediate distributions.

### 11.6 Controlling MC variance (p. 494–498)
The standard error is $O(1/\sqrt S)$, so many samples may be needed; hence variance-reduction tricks (p. 494).

**11.6.1 Common random numbers (p. 494).** To compare $\mathbb E_{p(z)}[f(\theta,z)]$ and $\mathbb E_{p(z)}[f(\theta',z)]$, use the same samples $z_s$ for both. Differences are then due to $\theta$ rather than noise. This can often turn a stochastic optimization problem into a deterministic one.

**11.6.2 Rao-Blackwellization (p. 494–495).** To estimate $\bar f=\mathbb E[f(X,Y)]$: naive $\hat f_{MC}=\frac1S\sum f(X_s,Y_s)$ with $(X_s,Y_s)\sim p(X,Y)$ \tag{11.52} is unbiased but may have high variance. If $Y$ can be marginalized analytically given $X$,
$$f_X(X_s)=\int dY\,p(Y|X_s)f(X_s,Y)=\mathbb E[f(X,Y)|X=X_s]\tag{11.53}$$
$$\hat f_{RB}=\frac1S\sum_{s=1}^Sf_X(X_s),\ X_s\sim p(X)\tag{11.54}$$
It is unbiased since $\mathbb E[\hat f_{RB}]=\mathbb E[\mathbb E[f|X]]=\bar f$, and it can have lower variance (we sample in a reduced-dimensional space). By the law of iterated variance,
$$\mathbb V[\mathbb E[f(X,Y)|X]]=\mathbb V[f(X,Y)]-\mathbb E[\mathbb V[f(X,Y)|X]]\le\mathbb V[f(X,Y)]\tag{11.55}$$
Examples are pointed to in Sections 6.3.4.2, 13.4 and 12.3.8.

**11.6.3 Control variates (p. 495–496).** Let $m(\mathcal X)=\frac1S\sum m(x_s)$ be unbiased for $\mu=\mathbb E[f(X)]$, i.e. $\mathbb E[m(X)]=\mu$. With baseline $b$ (known mean),
$$m^*(\mathcal X)=m(\mathcal X)+c\,(b(\mathcal X)-\mathbb E[b(\mathcal X)])\tag{11.56}$$
It is unbiased, and can have lower variance provided $b$ is correlated with $m$:
$$\mathbb V[m^*]=\mathbb V[m]+c^2\mathbb V[b]+2c\,\mathrm{Cov}[m,b]\tag{11.57}$$
Setting the derivative in $c$ to 0 gives
$$c^*=-\frac{\mathrm{Cov}[m(X),b(X)]}{\mathbb V[b(X)]}\tag{11.58}$$
(added step: substituting, $\mathbb V[m]+\frac{\mathrm{Cov}^2}{\mathbb V[b]}-2\frac{\mathrm{Cov}^2}{\mathbb V[b]}=\mathbb V[m]-\frac{\mathrm{Cov}^2}{\mathbb V[b]}$.)
$$\mathbb V[m^*]=\mathbb V[m]-\frac{\mathrm{Cov}[m,b]^2}{\mathbb V[b]}=(1-\rho_{m,b}^2)\mathbb V[m]\le\mathbb V[m]\tag{11.59}$$
Intuitively, the estimator uses the error on a known quantity, $\mathbb E[b]$, to correct the error on the unknown $\mu$.

*Worked example (p. 496).* $\mu=\mathbb E[1/(1+X)]$, $X\sim\mathrm{Unif}(0,1)$; exact $\mu=\int_0^1\frac{dx}{1+x}=\ln2\approx0.693$ \tag{11.60}. Naive MC with $S=1500$: $0.6935$, se $0.0037$. Baseline $b(X)=1+X$ with $\mathbb E[b]=\int_0^1(1+x)dx=\tfrac32$, giving $m^*=\frac1S\sum f(x_s)+c(\frac1S\sum b(x_s)-\frac32)$ \tag{11.61}. With $c^*\approx0.4773$ estimated from samples via (11.58), $S=1500$: $0.6941$, se $0.0007$.

**11.6.4 Antithetic sampling (p. 496–497).** For $\theta=\mathbb E[Y]$, use $\hat\theta=(Y_1+Y_2)/2$:
$$\mathbb V[\hat\theta]=\frac{\mathbb V[Y_1]+\mathbb V[Y_2]+2\mathrm{Cov}[Y_1,Y_2]}{4}\tag{11.62}$$
The variance is reduced if $\mathrm{Cov}[Y_1,Y_2]<0$, so set $Y_2$ to an "opposite" with the same mean. For $Y\sim\mathrm{Unif}(0,1)$, use $y_i'=1-y_i$, still $\mathrm{Unif}(0,1)$. *Example (p. 497):* same integral. Classic MC with $2N=1500$ samples ($N=750$): $0.69365$, se $0.0037$. Antithetic with $N=750$ base samples: $0.6939$, se $0.0007$, matching control variates.

**11.6.5 Quasi-MC (p. 497–498).** QMC replaces random points by low-discrepancy (space-filling) sequences such as Halton or Sobol (Figure 11.7). For $\bar f=\int_{[0,1]^D}f\approx\hat f_N=\frac1N\sum f(x_n)$ \tag{11.63}, with error $\epsilon_N=|\bar f-\hat f_N|$: standard MC has $\epsilon_N\sim O(1/\sqrt N)$; QMC has $\epsilon_N\sim O((\log N)^D/N)$, which is smaller for $N>2^D$. QMC gives only a point estimate, with no uncertainty estimate. Randomized QMC repeats QMC $R$ times with random shifts
$$y_{i,r}=x_i+u_r\ (\mathrm{mod}\ 1),\ u_r\sim\mathrm{Unif}(0,1)^D\tag{11.64}$$
The set $\{y_j\}$ is low discrepancy, each $y_j\sim\mathrm{Unif}(0,1)^D$ ($j=1{:}N\times R$), and variance is much lower than standard MC. [OR20] proved a strong law of large numbers for RQMC. QMC/RQMC can be used inside MCMC and variational inference and to pick initial query points in Bayesian optimization. Orthogonal MC conditions samples to be pairwise orthogonal while keeping the marginals (p. 498).

*Intuition note.* Variance reduction can work in several ways: pair opposite samples, use a correlated quantity with known mean, integrate part of the problem analytically, or spread points evenly instead of randomly.

## Toy example (ours)
Estimate $\mu=\mathbb E[X^2]$, $X\sim\mathrm{Unif}(0,1)$, exact value $1/3$. Take four uniform draws (made up): $0.1,0.3,0.6,0.9$.
- $f$ values: $0.01,\,0.09,\,0.36,\,0.81$; sum $=1.27$; $\hat\mu=1.27/4=0.3175$ (11.2).
- Deviations squared: $(-0.3075)^2=0.094556$; $(-0.2275)^2=0.051756$; $(0.0425)^2=0.001806$; $(0.4925)^2=0.242556$. Sum $=0.390675$.
- $\hat\sigma^2=0.390675/4=0.09767$ (11.9); $\hat\sigma\approx0.3125$.
- Standard error $=\hat\sigma/\sqrt4=0.1563$ (11.10). The 95% interval is $0.3175\pm1.96(0.1563)=0.3175\pm0.306$, which contains $1/3$.
- Samples needed for $\pm0.01$: $N_s\ge4\hat\sigma^2/\epsilon^2=4(0.09767)/0.0001\approx3907$ (p. 485 rule).

## Concepts
- [[monte-carlo-integration]] — approximate $\mathbb E[f(x)]$ by the sample average of $f$ at draws from $p$; the error is dimension-independent in principle (p. 483)
- [[mc-standard-error]] (new) — $\sqrt{\hat\sigma^2/N_s}$, estimated uncertainty of the MC estimate (p. 485)
- [[inverse-cdf-sampling]] (new) — sample $u\sim U(0,1)$, return $F^{-1}(u)$ (p. 486)
- [[box-muller]] (new) — turn uniform points in the unit circle into two independent Gaussian samples (p. 487)
- [[rejection-sampling]] (new) — accept proposals under an envelope $Cq\ge\tilde p$; the acceptance rate is $1/C$ for a normalized target (p. 487–488)
- [[importance-sampling]] (new) — weight proposal samples by $\pi/q$ to estimate expectations under $\pi$ (p. 490–491)
- [[self-normalized-importance-sampling]] (new) — IS with unnormalized weights divided by their sum; biased, also estimates $Z$ (p. 491–492)
- [[annealed-importance-sampling]] (new) — IS over a tempered path of distributions from easy to hard; estimates $Z_0/Z_n$ (p. 492–494)
- [[marginal-likelihood]] — the constant $Z=p(y)$, estimable by SNIS or AIS (p. 491, 494)
- [[variational-inference-elbo]] — ELBO optimization can learn a good IS proposal (p. 492)
- [[rao-blackwellization]] (new) — replace a sample by its conditional expectation to lower variance (p. 494–495)
- [[control-variates]] (new) — subtract a correlated, known-mean baseline term; variance factor $1-\rho^2$ at the optimal $c$ (p. 495–496)
- [[antithetic-sampling]] (new) — use negatively correlated sample pairs (p. 496)
- [[common-random-numbers]] (new) — reuse the same noise when comparing parameter settings (p. 494)
- [[quasi-monte-carlo]] (new) — low-discrepancy points; error $O((\log N)^D/N)$; RQMC adds random shifts (p. 497–498)

## Canonical instances
- [[estimate-pi-mc]] — circle indicator with uniform samples; $\hat\pi=3.10$, se 0.09 (p. 484)
- [[exponential-inverse-cdf]] — $x=-\ln(1-u)/\lambda$ (p. 487)
- [[gamma-rejection-sampling]] — $\mathrm{Ga}(\alpha,\lambda)$ with $\mathrm{Ga}(k,\lambda-1)$ proposal (p. 489)
- [[gaussian-rejection-dimension-curse]] — acceptance $1/C=(\sigma_p/\sigma_q)^D$ (p. 490)
- [[control-variate-1-over-1-plus-x]] — se 0.0037 → 0.0007 (p. 496)
- [[antithetic-uniform]] — $y'=1-y$ with same se as control variates (p. 497)

## Bridges (candidates)
- [same-math] Rao-Blackwellization (law of iterated variance) ↔ statistics: conditioning never increases variance — the same identity (11.55).
- [structural-analogy] Importance weights $\pi/q$ ↔ causal inference: reweighting a sample to mimic another distribution (e.g. inverse-propensity weights).
- [structural-analogy] Control variate with $c^*$ ↔ regression: $c^*=-\mathrm{Cov}/\mathbb V$ is a regression slope on the baseline.
- [metaphor] AIS temperature ladder ↔ physics: slowly cooling from an easy to a hard distribution.
- [structural-analogy] AIS estimate of $p(\mathcal D)$ ↔ Bayesian model comparison via the marginal likelihood.

## Questions this raises
- How does MCMC (Ch. 12) produce samples when no exact or envelope-based sampler exists, and what does it do to the "independent samples" assumption in (11.7)?
- How can one diagnose a poor importance-sampling proposal, since variance of the weights is not discussed here?
- How does QMC's $(\log N)^D/N$ rate behave for large $D$, given that the comparison with MC is stated for $N>2^D$?
- Can control variates, antithetic sampling and Rao-Blackwellization be combined, and does the gain add up?

## Reading notes
- Printed page = pdf − 34. Pages 483–498 are all printed-numbered.
- Eq. (11.36) is printed with $d\boldsymbol z$ where $d\boldsymbol x$ is clearly meant.
- Eq. (11.46) lists $\tilde T_0,\tilde T_2,\dots$ with no $\tilde T_1$; the image shows this. Probably a typo for $\tilde T_1$ (my inference).
- p. 493 says $T_j$ "leaves $p_0$ invariant", and the displayed integral condition also uses $p_0$ (with $p_j(x'|x)$ as the kernel). The reversal (11.48) uses $p_j$, which may suggest $p_j$ was intended (my inference). I report the text as printed.
- p. 496 (antithetic) states $\mathrm{Cov}[y_i,y_i']<1$; the argument needs $<0$. The image shows "$<1$". I treat this as a misprint of the printed claim.
- The exact value is written $\ln 2\approx0.693$ (p. 496) and $0.6935$ (p. 497).
- Figure 11.7 and the (11.45) weights are described but not derived beyond what is summarized. The Jacobian in (11.17) is stated without computation.
- No exercises appear in this unit.
