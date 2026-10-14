---
id: murphy-2023-pml2/ch05-information-p1
work: murphy-2023-pml2
unit: "5 Information theory (part 1/2): §5.1 KL divergence, §5.2.1–5.2.4 Entropy (start of cross entropy and perplexity)"
pages: 219-237
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Information theory (part 1/2): KL divergence and entropy

## L0 — One line
The size of an update from beliefs q to beliefs p is measured, uniquely up to a constant, by the KL divergence, and entropy is a shifted KL divergence from the uniform distribution.

## L1 — The gist (≤ 120 words)
How can we measure the size of a belief update from q to p? Murphy lists five desiderata: continuity, non-negativity, permutation invariance, monotonicity for uniform distributions, and a chain rule. He states that the KL divergence, $\sum_k p_k\log(p_k/q_k)$, is the only measure (up to a multiplicative constant) that satisfies them. The chapter then derives its properties: asymmetry, forward versus reverse KL, the data processing inequality, equivalence to maximum likelihood, a Bayesian-inference reading, closed forms, a Fisher-information approximation, and a link to Bregman divergence. Entropy follows as a shifted KL from the uniform distribution. The chapter's introduction names data compression and error correction as applications.

**Prerequisites:** discrete and continuous probability, expectation, logarithms; convex functions and Jensen's inequality; exponential families (natural parameters, log partition function); gradients and Hessians; Gaussians.

## L2 — Key ideas (5–10 bullets)
- Five desiderata (continuity, non-negativity, permutation invariance, uniform monotonicity, chain rule) are stated; KL divergence is said to be the unique measure, up to a constant, satisfying them (pp. 220–221).
- $D_{KL}(p\|q)\ge 0$, with equality iff $p=q$. This follows from Jensen's inequality (for convex $f$, $f$ of an average is at most the average of $f$). When an expression can be rearranged into KL terms, dropping them gives a bound (p. 222).
- KL is invariant under invertible reparameterization, and it is asymmetric because the chain rule takes expectations under $p$ (pp. 223–224).
- Forward KL $D_{KL}(p\|q)$ is mode-covering ($q$ spreads over all of $p$'s mass); for exponential-family $q$ its minimizer matches the expected sufficient statistics of $p$ (moment matching). Reverse KL $D_{KL}(q\|p)$ is mode-seeking ($q$ may sit on only part of $p$). For a diagonal Gaussian fitted to a correlated Gaussian, forward KL gives a too-broad (under-confident) fit and reverse KL a too-narrow (over-confident) fit, although reverse KL does not always give an overly compact fit (pp. 225–227).
- The data processing inequality says processing or marginalizing cannot increase KL (p. 229).
- Minimizing KL to the empirical distribution is maximum likelihood, which can overfit (pp. 230–231).
- Bayesian conditioning is the KL-minimizing update subject to a data constraint. Relaxing the constraint to a known distribution $p(D)$ gives Jeffrey's rule, $p(\theta)=\int p(D)q(\theta|D)dD$ (pp. 231–232).
- Exponential-family KL has a closed form. For a small parameter change $\delta$, KL is approximately $\tfrac12\delta^\top F\delta$ ($F$ = Fisher information matrix, the expected outer product of the score), and KL is a Bregman divergence (the gap between a convex function and its tangent) of the log partition function (pp. 232–234).
- Entropy is $\log K$ minus KL to the uniform. Differential entropy can be negative and depends on units (pp. 235–236).

## L3 — Walkthrough

### Intro (p. 219)
Information is treated as the magnitude of an update from beliefs $q(x)$ to $p(x)$, written $I[p\|q]$. The chapter promises compression (source coding), error correction (channel coding), and the information bottleneck (Section 5.6.2, outside this part). Both applications need an accurate probabilistic model of the data (p. 219).

### 5.1.1 Desiderata (pp. 220–221)
Running example: suit of the next card, $S\in\{♣,♠,♡,♢\}$, with uniform $q=[\tfrac14,\tfrac14,\tfrac14,\tfrac14]$. Two candidate updates are $q'=[\tfrac12,\tfrac12,0,0]$ (red cards removed) and $q''=[\tfrac38,\tfrac28,\tfrac28,\tfrac18]$ (some diamonds became clubs) (p. 220). A good measure should be:
1. **Continuous** in both arguments (p. 220).
2. **Non-negative**: $I[p\|q]\ge 0$ (p. 220).
3. **Permutation invariant**, if the same reordering is applied to both distributions (p. 220).
4. **Monotonic for uniform distributions**: going from uniform on $N$ elements to uniform on $N'$ elements, the gain increases in $N$ and decreases in $N'$ (p. 220).
5. **A natural chain rule**: describing the suit directly or as colour then suit must give the same total. For $p(S)=[\tfrac38,\tfrac28,\tfrac28,\tfrac18]$ the factorization is
$$p(C)=[\tfrac58,\tfrac38],\quad p(\{♣,♠\}|C{=}■)=[\tfrac35,\tfrac25],\quad p(\{♡,♢\}|C{=}□)=[\tfrac23,\tfrac13]\tag{5.1–5.2}$$
and the requirement is
$$I_S = I_C + p(C{=}■)I_■ + p(C{=}□)I_□ = I_C+\tfrac58 I_■+\tfrac38 I_□ .\tag{5.7}$$
In general, for $x=[x_L,x_R]$:
$$I[p(x)\|q(x)] = I[p(x_L)\|q(x_L)] + \mathbb{E}_{p(x_L)}\big[I[p(x_R|x_L)\|q(x_R|x_L)]\big].\tag{5.8}$$
The expectation is taken under $p$'s marginal, so this requirement breaks the symmetry between $p$ and $q$ (p. 221).

### 5.1.2 KL uniquely satisfies the desiderata (pp. 221–223)
Murphy states that KL is the only measure (up to a multiplicative constant) satisfying these desiderata. He cites [Hob69; Rén61] for the proof and does not prove it here (p. 221). Definition (also called information gain or relative entropy):
$$D_{KL}(p\|q)\triangleq\sum_{k=1}^K p_k\log\frac{p_k}{q_k}\tag{5.9}$$
$$D_{KL}(p\|q)\triangleq\int dx\,p(x)\log\frac{p(x)}{q(x)}\tag{5.10}$$

**Continuity (p. 221–222).** The KL is manifestly continuous except potentially where $p_k$ or $q_k$ is zero. $\lim_{p\to0}p\log\frac pq=0$ (5.11), so the integrand is defined as 0 at $p=0$. If $q=0$ where $p\ne0$, the divergence is infinite, so $q$ must have support wherever $p$ does (p. 222).

**Non-negativity (p. 222).** Jensen's inequality: for convex $f$, $\lambda_i\ge0$, $\sum\lambda_i=1$,
$$f\Big(\sum_i\lambda_i x_i\Big)\le\sum_i\lambda_i f(x_i).\tag{5.12}$$

*Theorem 5.1.1 (Information inequality).* $D_{KL}(p\|q)\ge0$ with equality iff $p=q$.

Proof (following [CT06]). Let $A=\{x:p(x)>0\}$.
$$-D_{KL}(p\|q)=-\sum_{x\in A}p(x)\log\frac{p(x)}{q(x)}=\sum_{x\in A}p(x)\log\frac{q(x)}{p(x)}\tag{5.13}$$
$$\le\log\sum_{x\in A}p(x)\frac{q(x)}{p(x)}=\log\sum_{x\in A}q(x)\tag{5.14}$$
$$\le\log\sum_{x\in\mathcal X}q(x)=\log1=0\tag{5.15}$$
Equality in (5.14) holds iff $p(x)=cq(x)$ for a constant $c$, because log is strictly concave. Equality in (5.15) holds iff $\sum_{x\in A}q=\sum_{x\in\mathcal X}q=1$, which forces $c=1$. Hence $D_{KL}=0$ iff $p=q$ (p. 222).

*Intuition note.* Because KL cannot be negative, when an expression can be rearranged into KL terms, dropping them immediately gives a bound. Murphy calls this a "good result to keep in your back pocket" (p. 222).

**Reparameterization invariance (pp. 222–223).** For an invertible map $y=f(x)$, $p(x)dx=p(y)dy$ and $q(x)dx=q(y)dy$, so
$$D_{KL}(p(x)\|q(x))=\int dy\,p(y)\log\frac{p(y)\left|\frac{dy}{dx}\right|}{q(y)\left|\frac{dy}{dx}\right|}=D_{KL}(p(y)\|q(y)).\tag{5.16}$$
The Jacobian factors cancel. KL measures something about the distributions, not about the coordinates, so we may change basis (e.g. Fourier) freely (p. 223).

**Uniform monotonicity (p. 223).** For uniform $q$ on $N$ elements and uniform $p$ on $N'$ elements:
$$D_{KL}(p\|q)=\sum_k\frac1{N'}\log\frac{1/N'}{1/N}=\log\frac N{N'}.\tag{5.17}$$
In bits, this is read as the number of well-designed yes/no questions (each halving the search space) needed on average to move from $q$ to $p$ (p. 223).

**Chain rule (p. 223).**
$$D_{KL}(p(x,y)\|q(x,y))=\int dx\,dy\,p(x,y)\Big[\log\frac{p(x)}{q(x)}+\log\frac{p(y|x)}{q(y|x)}\Big]\tag{5.18–5.19}$$
$$=D_{KL}(p(x)\|q(x))+\mathbb E_{p(x)}\big[D_{KL}(p(y|x)\|q(y|x))\big].\tag{5.20}$$
The conditional KL is defined as the expected value:
$$D_{KL}(p(y|x)\|q(y|x))\triangleq\int dx\,p(x)\int dy\,p(y|x)\log\frac{p(y|x)}{q(y|x)}.\tag{5.21}$$

### 5.1.3 Thinking about KL (pp. 224–225)
**Units.** Base-2 logs give bits and natural logs give nats. $1\text{ bit}=\log2\text{ nats}\approx0.693$ nats (5.22), and $1\text{ nat}=1/\log 2\text{ bits}\approx1.44$ bits (5.23) (p. 224).

**Asymmetry.** The asymmetry comes from requiring the chain rule, which takes the expectation under the first argument (p. 224). Example with Bernoulli success probabilities 0.443 and 0.975:
$$D_{KL}=0.975\log\tfrac{0.975}{0.443}+0.025\log\tfrac{0.025}{0.557}=0.692\text{ nats}\approx1.0\text{ bit}\tag{5.24}$$
$$D_{KL}=0.443\log\tfrac{0.443}{0.975}+0.557\log\tfrac{0.557}{0.025}=1.38\text{ nats}\approx2.0\text{ bits}\tag{5.25}$$
Going from a nearly even distribution to a nearly certain one costs about 1 bit. The reverse costs about twice as much (p. 224).

**Expected weight of evidence.** Bayes' rule (5.26) needs $\Pr(D)$. The ratio of two hypotheses cancels it:
$$\frac{\Pr(P|D)}{\Pr(Q|D)}=\frac{\Pr(D|P)}{\Pr(D|Q)}\frac{\Pr(P)}{\Pr(Q)}\tag{5.27}$$
$$\log\frac{\Pr(P|D)}{\Pr(Q|D)}=\log\frac{p(D)}{q(D)}+\log\frac{\Pr(P)}{\Pr(Q)}\tag{5.28}$$
The term $w[P/Q;D]\triangleq\log\frac{p(D)}{q(D)}$ (5.29) is I. J. Good's weight of evidence. KL is the expected weight of evidence for $P$ over $Q$ per observation, provided $P$ is correct. So on average data add evidence toward the correct hypothesis, since KL is non-negative (pp. 224–225).

### 5.1.4 Minimizing KL (pp. 225–227)
**Forwards vs reverse KL (p. 225).** Minimizing $D_{KL}(p\|q)$ (inclusive or forwards KL) requires $q>0$ wherever $p>0$. It gives mode-covering, zero-avoiding behaviour. Minimizing $D_{KL}(q\|p)$ (exclusive or reverse KL) requires $q=0$ wherever $p=0$. It gives mode-seeking, zero-forcing behaviour. In Fig. 5.1 a unimodal Gaussian fitted to a bimodal $p$ covers both modes under forward KL (orange) and sits on one mode under reverse KL (green) (pp. 225–226).

**Moment projection (M-projection), $q=\arg\min_q D_{KL}(p\|q)$ (5.30), pp. 226–227.** Assume an exponential family $q(x)=h(x)\exp[\eta^\top\mathcal T(x)-\log Z(\eta)]$ (5.31). First-order conditions:
$$\partial_{\eta_i}D_{KL}(p\|q)=-\partial_{\eta_i}\!\int p\log q=-\partial_{\eta_i}\!\int p\,(\eta^\top\mathcal T-\log Z)\tag{5.32–5.34}$$
$$=-\int p\,\mathcal T_i+\mathbb E_q[\mathcal T_i]=-\mathbb E_p[\mathcal T_i]+\mathbb E_q[\mathcal T_i]=0\tag{5.35–5.36}$$
The step uses that the derivative of the log partition function is the expected sufficient statistics (Eq. 2.216 of the book). So the optimal $q$ matches the moments of $p$ (moment matching). Example: $p=\mathcal N(\mu,\Sigma)=\mathcal N(\mu,\Lambda^{-1})$ in 2d (5.37), and $q=\mathcal N(x_1|m_1,v_1)\mathcal N(x_2|m_2,v_2)$ (5.38). Then
$$q(x)=\mathcal N(x_1|\mu_1,\Sigma_{11})\mathcal N(x_2|\mu_2,\Sigma_{22}).\tag{5.39}$$
$q$ covers $p$ but is too broad (under-confident), Fig. 5.2a (p. 227).

**Information projection (I-projection), $q=\arg\min_q D_{KL}(q\|p)$ (5.40).** The objective takes expectations under $q$, which can be a tractable family, so it is often easier. For the same $p$ and $q=\mathcal N(m,\mathrm{diag}(v))$, the optimum is $m=\mu$, $v_i=\Lambda_{ii}^{-1}$ (derivation in Supplementary 5.1.2, not given here). The approximation is too narrow, i.e. over-confident (Fig. 5.2b). Murphy notes reverse KL does not always give an overly compact approximation, citing [Tur+08] (p. 227).

*Intuition note.* Forward KL punishes $q$ for missing any place where $p$ has mass, so $q$ spreads out. Reverse KL punishes $q$ for putting mass where $p$ has none, so $q$ can shrink onto part of $p$.

### 5.1.5 Properties of KL (pp. 228–230)
**Compression lemma (Theorem 5.1.2).** For distributions $P,Q$ with well-defined KL and any scalar function $\phi$:
$$\mathbb E_P[\phi]\le\log\mathbb E_Q[e^{\phi}]+D_{KL}(P\|Q).\tag{5.41}$$
Proof: define $g(x)=\frac{q(x)}{\mathcal Z}e^{\phi(x)}$ (5.42) with $\mathcal Z=\int dx\,q(x)e^{\phi(x)}$ (5.43). Then
$$D_{KL}(P\|G)=D_{KL}(P\|Q)-\mathbb E_P[\phi]+\log\mathcal Z\ge0.\tag{5.44}$$
(Added step: this follows from $\log\frac{p}{g}=\log\frac pq-\phi+\log\mathcal Z$, averaged under $P$.) One way to view the lemma is as the Donsker–Varadhan variational representation of KL, assuming all values are finite:
$$D_{KL}(P\|Q)=\sup_\phi\ \mathbb E_P[\phi(x)]-\log\mathbb E_Q[e^{\phi(x)}].\tag{5.45}$$
For any fixed $\phi$ the right side is a lower bound on KL. The lemma can also be used to power PAC-Bayes bounds (p. 228).

**Data processing inequality (Theorem 5.1.3).** Let $t(y|x)$ be a probabilistic channel, with $p(y)$ and $q(y)$ the distributions obtained by sending $p(x)$ and $q(x)$ through it. Then
$$D_{KL}(p(x)\|q(x))\ge D_{KL}(p(y)\|q(y)).\tag{5.46}$$
Proof: set $p(x,y)=p(x)t(y|x)$ and $q(x,y)=q(x)t(y|x)$.
$$D_{KL}(p(x)\|q(x))=\int\!\!\int p(x)t(y|x)\log\frac{p(x)t(y|x)}{q(x)t(y|x)}=\int\!\!\int p(x,y)\log\frac{p(x,y)}{q(x,y)}\tag{5.47–5.49}$$
$$=-\int dy\,p(y)\int dx\,p(x|y)\log\frac{q(x,y)}{p(x,y)}\tag{5.50}$$
$$\ge-\int dy\,p(y)\log\Big(\int dx\,p(x|y)\frac{q(x,y)}{p(x,y)}\Big)\tag{5.51}$$
$$=-\int dy\,p(y)\log\Big(\frac{q(y)}{p(y)}\int dx\,q(x|y)\Big)\tag{5.52}$$
$$=\int dy\,p(y)\log\frac{p(y)}{q(y)}=D_{KL}(p(y)\|q(y)).\tag{5.53}$$
(Added step for 5.51→5.52: $p(x|y)\,q(x,y)/p(x,y)=q(x,y)/p(y)=\frac{q(y)}{p(y)}q(x|y)$, and $\int q(x|y)dx=1$.) Processing makes the two distributions harder to tell apart (p. 229).

*Corollary 5.1.1 (monotonicity).* Marginalizing is a special processing step: $D_{KL}(p(x,y)\|q(x,y))\ge D_{KL}(p(x)\|q(x))$ (5.54). The proof is the same Jensen step (5.55–5.58). Observing only part of the variables makes the two candidates harder to distinguish (pp. 229–230).

*Intuition note.* Processing samples cannot make two distributions easier to tell apart (the KL cannot increase).

### 5.1.6 KL and MLE (pp. 230–231)
With $p_{\mathcal D}(x)=\frac1N\sum_n\delta(x-x_n)$ (5.61) and the sifting property of delta functions:
$$D_{KL}(p_{\mathcal D}\|q)=-\int p_{\mathcal D}\log q+C=-\frac1N\sum_n\log q(x_n)+C,\tag{5.62–5.64}$$
where $C=\int p_{\mathcal D}\log p_{\mathcal D}$ does not depend on $q$. Equivalently $D_{KL}(p_{\mathcal D}\|q)=\mathbb H_{ce}(p_{\mathcal D},q)-\mathbb H(p_{\mathcal D})$ (5.65), with cross entropy $\mathbb H_{ce}(p,q)\triangleq-\sum_kp_k\log q_k$ (5.66). So minimizing KL to the empirical distribution is equivalent to maximizing likelihood. Murphy sees a flaw here: it puts too much weight on the training set (overfitting), because the empirical distribution is only "spikes" on finite points. He suggests smoothing it or regularizing $q$ (p. 231).

### 5.1.7 KL and Bayesian inference (pp. 231–232)
Prior joint $q(\theta,D)=q(\theta)q(D|\theta)$. After observing $D_0$, choose the joint closest to $q$ that respects the data constraint:
$$p(\theta,D)=\arg\min D_{KL}(p(\theta,D)\|q(\theta,D))\ \text{ s.t. }p(D)=\delta(D-D_0).\tag{5.67}$$
By the chain rule
$$D_{KL}(p(\theta,D)\|q(\theta,D))=D_{KL}(p(D)\|q(D))+D_{KL}(p(\theta|D)\|q(\theta|D)).\tag{5.68}$$
(Added step: $p(D)$ is fixed by the constraint, so the second term is made zero by taking $p(\theta|D)=q(\theta|D)$.) The solution is:
$$p(\theta,D)=p(D)p(\theta|D)=\delta(D-D_0)q(\theta|D)\tag{5.69}$$
$$p(\theta)=\int dD\,\delta(D-D_0)q(\theta|D)=q(\theta|D=D_0),\tag{5.70}$$
the usual posterior. By contrast, the usual statement of Bayes' rule (5.71) is a trivial consequence of the chain rule of probability. **Murphy's view:** Bayes' rule itself does not say how we ought to update, for which another principle is needed [Cat+11]; Section 5.1.7 frames Bayesian inference itself as the solution of a KL minimization problem (pp. 231–232). If measurement error is well understood, replace the delta by a known $p(D)$. The posterior $p(\theta|D)=q(\theta|D)$ is unchanged, but
$$p(\theta)=\int dD\,p(D)q(\theta|D),\tag{5.72}$$
called Jeffrey's conditionalization rule (p. 232).

### 5.1.8 KL and exponential families (p. 232–233)
For $p(x)=h(x)\exp[\eta^\top\mathcal T(x)-A(\eta)]$ (5.73) with log partition $A(\eta)=\log\int h\exp(\eta^\top\mathcal T)dx$ (5.74), a convex function:
$$D_{KL}(p(x|\eta_1)\|p(x|\eta_2))=\mathbb E_{\eta_1}\big[(\eta_1-\eta_2)^\top\mathcal T(x)-A(\eta_1)+A(\eta_2)\big]\tag{5.75}$$
$$=(\eta_1-\eta_2)^\top\mu_1-A(\eta_1)+A(\eta_2),\quad\mu_j\triangleq\mathbb E_{\eta_j}[\mathcal T(x)].\tag{5.76}$$
For $D$-dimensional Gaussians ($\Sigma_i$ is $D\times D$):
$$D_{KL}(\mathcal N(\mu_1,\Sigma_1)\|\mathcal N(\mu_2,\Sigma_2))=\tfrac12\Big[\mathrm{tr}(\Sigma_2^{-1}\Sigma_1)+(\mu_2-\mu_1)^\top\Sigma_2^{-1}(\mu_2-\mu_1)-D+\log\tfrac{\det\Sigma_2}{\det\Sigma_1}\Big]\tag{5.77}$$
Scalar case:
$$D_{KL}(\mathcal N(\mu_1,\sigma_1)\|\mathcal N(\mu_2,\sigma_2))=\log\frac{\sigma_2}{\sigma_1}+\frac{\sigma_1^2+(\mu_1-\mu_2)^2}{2\sigma_2^2}-\frac12.\tag{5.78}$$

### 5.1.9 Approximating KL with the Fisher information matrix (p. 233)
With $\theta'=\theta+\delta$ and $D_{KL}(p_\theta\|p_{\theta'})=\mathbb E_{p_\theta}[\log p_\theta-\log p_{\theta'}]$ (5.79), a second-order Taylor expansion gives
$$D_{KL}(p_\theta\|p_{\theta'})\approx-\delta^\top\mathbb E[\nabla\log p_\theta]-\tfrac12\delta^\top\mathbb E[\nabla^2\log p_\theta]\delta.\tag{5.80}$$
The expected score is zero (Eq. 3.44 of the book), so
$$D_{KL}(p_\theta\|p_{\theta'})\approx\tfrac12\delta^\top\mathbf F(\theta)\delta,\quad \mathbf F=-\mathbb E[\nabla^2\log p_\theta]=\mathbb E[(\nabla\log p_\theta)(\nabla\log p_\theta)^\top].\tag{5.81–5.82}$$
So KL is approximately a squared Mahalanobis distance with the Fisher information matrix (FIM) as metric. This is the basis of the natural gradient method (Section 6.4).

### 5.1.10 Bregman divergence (pp. 233–234)
For $f$ continuously differentiable and strictly convex on a closed convex $\Omega$:
$$B_f(w\|v)=f(w)-f(v)-(w-v)^\top\nabla f(v).\tag{5.83}$$
With the first-order Taylor approximation $\hat f_v(w)=f(v)+(w-v)^\top\nabla f(v)$ (5.84), $B_f(w\|v)=f(w)-\hat f_v(w)$ (5.85). It is $\ge0$ because $\hat f_v$ is a linear lower bound on convex $f$. Special cases: $f=\|w\|^2$ gives squared Euclidean distance. $f=w^\top Qw$ gives squared Mahalanobis distance. $f=\log Z$ on natural parameters gives KL (p. 234).

**KL is a Bregman divergence (5.1.10.1).** Using the convex $A(\eta)$ and $\nabla A(\eta_p)=\mathbb E_p[\mathcal T(x)]$:
$$B_f(\eta_q\|\eta_p)=A(\eta_q)-A(\eta_p)-(\eta_q-\eta_p)^\top\mathbb E_p[\mathcal T(x)]=D_{KL}(p\|q).\tag{5.86–5.88}$$
Murphy adds that KL is the only divergence that is both a Bregman divergence and an $f$-divergence [Ama09] (p. 234).

### 5.2 Entropy (pp. 234–237)
**5.2.1 Definition (p. 235).**
$$\mathbb H(X)\triangleq-\sum_{k=1}^Kp(X{=}k)\log p(X{=}k)=-\mathbb E_X[\log p(X)].\tag{5.89}$$
Entropy equals a constant minus the KL from the uniform $u$:
$$\mathbb H(X)=\log K-D_{KL}(p\|u),\qquad D_{KL}(p\|u)=\log K+\sum_kp_k\log p_k.\tag{5.90–5.92}$$
If $p$ is uniform, KL is zero and entropy is maximal at $\log K$. For binary $X$ with $p(X{=}1)=\theta$: $\mathbb H=-[\theta\log\theta+(1-\theta)\log(1-\theta)]$ (5.93–5.94), the binary entropy function. Its maximum is 1 bit at $\theta=0.5$ (Fig. 5.4).

**5.2.2 Differential entropy (pp. 235–236).** $h(X)\triangleq-\int_{\mathcal X}dx\,p(x)\log p(x)$ (5.95), when the integral exists. For Gaussians:
$$h(\mathcal N(\mu,\Sigma))=\tfrac12\log|2\pi e\Sigma|=\tfrac d2+\tfrac d2\log(2\pi)+\tfrac12\log|\Sigma|\tag{5.96}$$
$$h(\mathcal N(\mu,\sigma^2))=\tfrac12\log(2\pi e\sigma^2).\tag{5.97}$$
Unlike discrete entropy, it can be negative, because a pdf can exceed 1. For $X\sim U(0,a)$: $h(X)=-\int_0^a\frac1a\log\frac1a\,dx=\log a$ (5.98). With $a=1/8$, $h=\log_2(1/8)=-3$ bits (p. 236). Murphy cites [CT91] for the fact that an $n$-bit quantization has entropy about $h(X)+n$. For $U(0,\frac18)$ the first 3 binary digits are 0, so only $n-3$ bits are needed, matching $-3$ (p. 236). Differential entropy is not reparameterization-invariant. For $y=f(x)$, $p(y)=p(x)\left|\frac{dy}{dx}\right|^{-1}$ (5.99), so
$$h(X)=h(Y)-\int dy\,p(y)\log\Big|\frac{dy}{dx}\Big|.\tag{5.100}$$
Even a rescaling changes the value. For the adult-height distribution (Fig. 5.5) it is 0.43 bits in feet, 5.4 bits in cm, and $-1.3$ bits in metres. The feet–cm gap is $\log_2 30.48=4.9$ (p. 236).

*Intuition note.* Differential entropy is not unit-free: its value depends on the unit of measurement. Changing units shifts it by the log of the scale factor. KL has no such problem because the factor appears in both numerator and denominator.

**5.2.3 Typical sets (pp. 236–237).** The $\epsilon$-typical set $\mathcal A_\epsilon^N$ is the set of length-$N$ sequences with
$$\mathbb H(p)-\epsilon\le-\tfrac1N\log p(x_1,\dots,x_N)\le\mathbb H(p)+\epsilon.\tag{5.101}$$
For i.i.d. data the middle term is the $N$-sample empirical estimate of the entropy. The asymptotic equipartition property (AEP) says it converges in probability to the true entropy as $N\to\infty$ [CT06]. So the typical set has probability close to 1 (p. 237).

**5.2.4 Cross entropy and perplexity (p. 237; part ends here).**
$$D_{KL}(p\|q)=\mathbb H_{ce}(p,q)-\mathbb H(p),\quad\mathbb H_{ce}(p,q)=-\sum_xp(x)\log q(x),\quad\mathbb H(p)=\mathbb H_{ce}(p,p).\tag{5.102–5.103}$$
$\mathbb H(p)$ does not depend on the model. In language modelling, perplexity is $2^{\mathbb H_{ce}(p,q)}$ (5.104).

## Toy example (ours): the chain rule on the card suits
Take the text's $p=[\tfrac38,\tfrac28,\tfrac28,\tfrac18]$ and uniform $q$. Use $\log_2$.

Direct: $\tfrac38\log_2\tfrac32+\tfrac28\log_2 1+\tfrac28\log_2 1+\tfrac18\log_2\tfrac12=0.375(0.58496)+0+0-0.125=0.2194-0.125=0.0944$ bits.

Via colour (5.20): colour $p=[\tfrac58,\tfrac38]$ vs $[\tfrac12,\tfrac12]$:
- $I_C=0.625\log_2 1.25+0.375\log_2 0.75=0.625(0.32193)+0.375(-0.41504)=0.2012-0.1556=0.0456$.
- Black branch $[\tfrac35,\tfrac25]$: $I_■=0.6(0.26303)+0.4(-0.32193)=0.1578-0.1288=0.0290$.
- Red branch $[\tfrac23,\tfrac13]$: $I_□=0.6667(0.41504)+0.3333(-0.58496)=0.2767-0.1950=0.0817$.
- Total: $0.0456+\tfrac58(0.0290)+\tfrac38(0.0817)=0.0456+0.0182+0.0306=0.0944$ bits. ✓

Uniform case (5.17): $q\to q'=[\tfrac12,\tfrac12,0,0]$ gives $\log_2(4/2)=1$ bit. This is one yes/no question, "is the card black?".

## Concepts
- [[kl-divergence]] — expected log ratio $\sum p\log(p/q)$; size of an update from $q$ to $p$; unique under the five desiderata (p. 221)
- [[desiderata-for-information-gain]] (new) — continuity, non-negativity, permutation invariance, uniform monotonicity, chain rule (p. 220)
- [[forwards-vs-reverse-kl]] (new) — $D_{KL}(p\|q)$ mode-covering; $D_{KL}(q\|p)$ mode-seeking (p. 225)
- [[moment-matching-m-projection]] (new) — forward-KL optimum in an exponential family matches expected sufficient statistics (p. 226)
- [[data-processing-inequality]] (new) — a channel cannot increase KL between two distributions (p. 229)
- [[compression-lemma]] (new) — $\mathbb E_P[\phi]\le\log\mathbb E_Q e^\phi+D_{KL}(P\|Q)$; Donsker–Varadhan form (p. 228)
- [[weight-of-evidence]] (new) — $\log p(D)/q(D)$; KL is its expectation under $P$ (p. 225)
- [[cross-entropy]] (new) — $-\sum p\log q$; KL plus entropy (p. 231)
- [[entropy]] (new) — $-\sum p\log p$; $\log K$ minus KL to the uniform (p. 235)
- [[differential-entropy]] (new) — continuous analogue; can be negative; unit-dependent (p. 235)
- [[jeffreys-conditionalization]] (new) — update with uncertain data: $p(\theta)=\int p(D)q(\theta|D)dD$ (p. 232)
- [[fisher-information-matrix]] (new) — metric in $D_{KL}\approx\frac12\delta^\top F\delta$ (p. 233)
- [[bregman-divergence]] (new) — $f(w)-f(v)-(w-v)^\top\nabla f(v)$ (p. 233)
- [[typical-set]] — length-$N$ sequences whose per-sample negative log-probability is within $\epsilon$ of the entropy (p. 236)
- [[perplexity]] (new) — $2^{\mathbb H_{ce}}$ (p. 237)
- [[marginal-likelihood]] — $\Pr(D)$, cancels in the ratio of hypotheses (p. 225)

## Canonical instances
- [[card-suit-update]] — running example for the desiderata and the chain rule (pp. 220–221)
- [[bernoulli-kl-asymmetry]] — 0.443 vs 0.975: 1 bit one way, 2 bits the other (p. 224)
- [[bimodal-vs-gaussian-fit]] — forward vs reverse KL on a bimodal $p$ (p. 226)
- [[diagonal-gaussian-approx]] — under- vs over-confidence of M- and I-projection (p. 227)
- [[uniform-negative-entropy]] — $U(0,1/8)$ has $h=-3$ bits (p. 236)
- [[height-entropy-units]] — one height distribution, entropy 0.43, 5.4 or $-1.3$ bits by unit (p. 236)

## Bridges (candidates)
- [same-math] KL to the empirical distribution ↔ MLE: minimizing cross-entropy equals maximizing average log-likelihood (p. 230–231).
- [same-math] Reverse-KL/I-projection ↔ variational inference in Bayesian inference (canon: KL divergence & ELBO; not developed in this unit): the KL being minimized is $D_{KL}(q\|p)$.
- [structural-analogy] Bayesian posterior as the KL-minimizing constrained update ↔ Bayes' theorem: the text says Bayes' rule alone is a trivial chain-rule identity, while the KL view gives a principle for updating (§5.1.7).
- [structural-analogy] KL $\approx\frac12\delta^\top F\delta$ ↔ squared Mahalanobis distance with the Fisher matrix as metric (an approximation), the basis of natural gradient (§5.1.9).
- [structural-analogy] Expected weight of evidence ↔ Bayes factor / log posterior odds (§5.1.3.3).
- [metaphor] Yes/no questions to halve the search space ↔ bits of KL (§5.1.2.4).

## Questions this raises
- Which principle other than Bayes' rule fixes how to update, and why does minimizing KL to the prior justify conditioning?
- When does reverse KL fail to be over-confident (the [Tur+08] caveat on p. 227)?
- If differential entropy depends on units, which entropy-based quantities remain meaningful for continuous variables?
- How does the typical set explain why typical samples are not at the mode?

## Reading notes
- This is part 1 of a longer chapter. It starts at the beginning of Ch. 5 (p. 219) and ends on p. 237, partway through §5.2.4 (the perplexity definition). The split is described as at a section boundary, but the text stops mid-§5.2.4 (cross entropy and perplexity). Later sections (mutual information, compression, channel coding, information bottleneck) are not covered.
- Printed = pdf − 34.
- The intro lists entropy (Section 5.2) and mutual information (Section 5.3) as two special cases of the KL divergence. Mutual information is not covered here.
- In 5.1.3.2, the text introduces the Bernoulli with 0.443 first, but (5.24) computes the divergence in the direction from $[0.443,0.557]$ to $[0.975,0.025]$, i.e. $D_{KL}$ with the 0.975 distribution as the first argument.
- The $v_i=\Lambda_{ii}^{-1}$ result and the full I-projection derivation are in the book's Supplementary Section 5.1.2, not in these pages.
- Page 230 shows a stray equation number (5.59) with no equation. The proof of Corollary 5.1.1 jumps to (5.56) without comment.
- Figures 5.1–5.5 were checked in the page images. No equations were unreadable.
