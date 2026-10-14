---
id: polyanskiy-2025-information/ch33-mutual
work: polyanskiy-2025-information
unit: "Chapter 30 (file label ch33) — Mutual information method"
pages: 585-593
fields: [information-theory]
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
# Mutual information method

## L0 — One line
To lower-bound estimation error, compare the information the data carry about the parameter (an upper bound on $I(\theta;X)$) with the information any estimator needs to reach a given accuracy (the rate-distortion function).

## L1 — The gist (≤ 120 words)
How can we prove that no estimator beats a given risk? The Mutual Information Method (MIM) picks a prior on the parameter and uses the data-processing inequality. Any estimator with error at most $D$ must carry at least $\phi(D)$ of information about $\theta$. The data supply at most $I(\theta;X)$, which can often be bounded further by a channel capacity. So $\phi(D)\le I(\theta;X)$, and inverting $\phi$ gives a risk bound. The chapter applies this to Gaussian location models, sparse vectors, and a planted community in a graph. It also shows how MIM handles "better than chance" estimation, where coarser lower-bound methods lose constants.

**Prerequisites:** mutual information and the data-processing inequality; Gaussian channel capacity; rate-distortion function; differential entropy; binary entropy $h$; KL divergence; Bayes and minimax risk.

## L2 — Key ideas (5–10 bullets)
- MIM chain: $\phi(D)\le I(\theta;\hat\theta)\le I(\theta;X)\le C$, so $R^*_\pi\ge\phi^{-1}(I(\theta;X))\ge\phi^{-1}(C)$. The lower bound $\phi$ depends only on the prior and the loss; the capacity bound $C$ depends only on the model (p. 585). The last step ($\le C$) is used only when $I(\theta;X)$ is further bounded by capacity.
- In the unconstrained Gaussian location model, MIM with a Gaussian prior gives the matching lower bound $d/n$ (the sample mean gives the upper bound) without computing a Bayes risk (p. 587).
- For the bounded-mean model, the sharp rate is $R^*(B(\rho))\asymp \frac dn\wedge\rho^2$. The lower bound uses the Shannon lower bound (a bound on the rate-distortion function in terms of the differential entropy of $\theta$), because the rate-distortion function of the uniform law on a ball has no closed form (pp. 587–588).
- With the $r$-th power of an arbitrary norm as loss, the SLB-based MIM bound is, for squared $\ell_q$ loss ($r=2$), tight for $1\le q<\infty$ but loses the dimension dependence at $q=\infty$ (p. 588).
- For $k$-sparse means, a prior on the Hamming sphere (uniform over 0/1 vectors with exactly $k$ ones) plus entropy bounds gives the lower bound $R^*_n\gtrsim\frac kn\log\frac{ed}k$ (pp. 589–591).
- For community detection, an upper bound on $I(G;\xi^*)$ (variational formula with the comparison graph $\mathrm{ER}(n,q)$, then KL tensorization) gives a necessary condition for almost exact recovery, i.e. $\mathbb E|C^*\triangle\hat C|=o(k)$ (pp. 591–592).
- MIM suits the regime of estimating better than chance; the three methods of the next chapter (Fano, Assouad, Le Cam) lose constants there (pp. 586, 592).

## L3 — Walkthrough

### Introduction: the method (p. 585)
Fix a prior $\pi$ on $\Theta$. Let $\hat\theta$ satisfy $\mathbb E[\ell(\theta,\hat\theta)]\le D$. Then $\theta\to X\to\hat\theta$ is a Markov chain (p. 585). Data processing (Theorem 3.7) gives
$$\inf_{P_{\tilde\theta|\theta}:\ \mathbb E\ell(\theta,\tilde\theta)\le D} I(\theta;\tilde\theta)\ \le\ I(\theta;\hat\theta)\ \le\ I(\theta;X).\tag{30.1}$$
The left side is the rate-distortion function $\phi(D)$: the minimum information needed for accuracy $D$. The right side is the information the data give. It may be bounded by the capacity of the channel $P_{X|\theta}$:
$$I(\theta;X)\le \sup_{\pi}I(\theta;X)\triangleq C.\tag{30.2}$$
Hence
$$R^*_\pi\ \ge\ \phi^{-1}(I(\theta;X))\ \ge\ \phi^{-1}(C).\tag{30.3}$$
The author notes a "source-channel separation" flavour. The lower bound (30.1) depends only on prior and loss; the bound (30.2) only on the model (p. 585).

Le Cam, Assouad and Fano (next chapter) follow from MIM with different priors: the uniform distribution over a two-point set, over the hypercube $\{0,1\}^d$, and over a packing (the source names the methods in the order Le Cam, Assouad, Fano). They are often loose in constants relative to MIM (p. 586).

*Intuition note:* An estimator is a compression of the data into a guess. A guess of accuracy $D$ needs $\phi(D)$ of information, and the data cannot supply more than $I(\theta;X)$. If the data carry little information, accuracy must be poor.

### 30.1 GLM revisited and the Shannon lower bound (pp. 586–589)
Model: $X=(X_1,\dots,X_n)\overset{\text{iid}}\sim\mathcal N(\theta,I_d)$, quadratic loss (p. 586).

**Unconstrained, $\Theta=\mathbb R^d$.** The sample mean gives $R^*(\mathbb R^d)\le d/n$ (p. 586). Take prior $\theta\sim\mathcal N(0,sI_d)$. By the Gaussian rate-distortion function (Theorem 26.2):
$$\phi(D)=\tfrac d2\log\tfrac{sd}{D}\ \ (D<sd),\qquad 0\ \text{otherwise}.$$
By sufficiency of $\bar X$ and Gaussian capacity, $I(\theta;X)=I(\theta;\bar X)=\frac d2\log(1+sn)$ (p. 587). Then (30.3) gives $R^*_\pi\ge \frac{sd}{1+sn}$, which equals the exact Bayes risk (28.7). Letting $s\to\infty$:
$$R^*(\mathbb R^d)=\frac dn.\tag{30.4}$$

**Theorem 30.1 (bounded GLM).** For $\Theta=B(\rho)=\{\|\theta\|_2\le\rho\}$:
$$R^*(B(\rho))\asymp \frac dn\wedge\rho^2.\tag{30.5}$$
(Remark 30.1: if $\rho\gtrsim\sqrt{d/n}$, ignoring the constraint is rate-optimal. If $\rho\lesssim\sqrt{d/n}$, estimating by zero is rate-optimal.) (p. 587)

*Proof.* Upper bound: use $\hat\theta=\bar X$ and $\hat\theta=0$. Lower bound: prior $\theta\sim\mathrm{Unif}(B(r))$, $r\in[0,\rho]$ to be optimized. By AWGN capacity (p. 587):
$$I(\theta;X)=I(\theta;\bar X)\le\sup_{P_\theta:\mathbb E\|\theta\|_2^2\le r^2} I(\theta;\theta+\tfrac1{\sqrt n}Z)=\tfrac d2\log\!\Big(1+\tfrac{nr^2}{d}\Big)\le\tfrac{nr^2}{2}.\tag{30.6}$$
Alternatively, capacity as information radius is at most the KL diameter (Corollary 5.8), which gives $2nr^2$, the same up to constants (30.7) (p. 587).

For $\phi$, the Shannon lower bound (SLB; Theorem 26.3) applies since $\theta$ is isotropic (p. 588):
$$\inf_{\mathbb E\|\theta-\hat\theta\|^2\le D} I(\theta;\hat\theta)\ \ge\ h(\theta)+\tfrac d2\log\tfrac{2\pi e d}{D}\ \ge\ \tfrac d2\log\tfrac{cr^2}{D}.$$
Here $h(\theta)=\log\mathrm{vol}(B(r))=d\log r+\log\mathrm{vol}(B(1))$ and $\mathrm{vol}(B(1))^{1/d}\asymp 1/\sqrt d$. Applying (30.3): $\frac d2\log\frac{cr^2}{R^*}\le\frac{nr^2}2$ (the page appears to print $\frac12$ in front of the log; $\frac d2$ is what the next step needs), i.e. $R^*\ge cr^2e^{-nr^2/d}$. Using $\sup_{0<x<1}xe^{-ax}=\frac1{ea}$ for $a\ge1$ and $e^{-a}$ for $a<1$, optimizing over $r$ gives $R^*\gtrsim \frac dn\wedge\rho^2$. $\square$ (p. 588)

*Intuition note:* Data supply about $nr^2/2$ units of information, while pinning $\theta$ down inside a ball to accuracy $D$ costs about $\frac d2\log(r^2/D)$. Balancing the two sets how small $D$ can be.

**Non-quadratic loss** $\|\hat\theta-\theta\|^r$ (any norm). Anderson's lemma gives the exact minimax risk
$$\inf_{\hat\theta}\sup_\theta\mathbb E\|\hat\theta-\theta\|^r=n^{-r/2}\,\mathbb E\|Z\|^r.\tag{30.8}$$
With prior $\mathcal N(0,sI_d)$ and $\mathbb E\|\hat\theta-\theta\|^r\le D$, data processing and the general SLB (26.5) give (p. 588)
$$\tfrac d2\log(1+ns)\ge I(\theta;X)\ge I(\theta;\hat\theta)\ge\tfrac d2\log(2\pi es)-\log\Big\{V_{\|\cdot\|}\big(\tfrac{Dre}{d}\big)^{d/r}\Gamma\big(1+\tfrac dr\big)\Big\}.$$
Rearranging and sending $s\to\infty$, then using Stirling and Urysohn's inequality (27.21):
$$\inf_{\hat\theta}\sup_\theta\mathbb E\|\hat\theta-\theta\|^r\ \ge\ \frac d{re}\Big(\frac{2\pi e}{n}\Big)^{r/2}\Big[V_{\|\cdot\|}\Gamma\big(1+\tfrac dr\big)\Big]^{-r/d}\asymp n^{-r/2}V_{\|\cdot\|}^{-r/d}\gtrsim\Big(\frac{d}{\sqrt n\,\mathbb E\|Z\|_*}\Big)^r.\tag{30.9}$$
Here $\|\cdot\|_*$ is the dual norm. Check with $r=2$ and $\ell_q$ norms:
- $q=2$: the first bound is exact and equals (30.4).
- $1\le q<\infty$: it gives the tight rate $d^{2/q}/n$.
- $q=\infty$: it gives only $1/n$, independent of $d$. By (30.8) the sharp rate is $\frac{\log d}{n}$, since $\mathbb E\|Z\|_\infty\asymp\sqrt{\log d}$. The optimal dimension dependence is deferred to Section 31.4 (p. 588).

**Remark 30.2.** For $r=1$ and $\theta$ uniform on a compact set $\Theta$, $h(\theta)=\log\mathrm{vol}(\Theta)$. With Stirling's approximation, (26.5) becomes $\log\frac{\mathrm{vol}(\Theta)}{\mathrm{vol}(B_{\|\cdot\|}(c\epsilon))}$. This has the form of the volume ratio for metric entropy. So SLB is a volume-based lower bound on the rate-distortion function (p. 589). The author adds that in statistical applications SLB gives basically the same lower bound as Fano's method on a packing from the volume bound, although SLB does not use a packing explicitly (Section 31.4) (p. 589).

### 30.2 GLM with sparse means (pp. 589–591)
Parameter space: $B_0(k)=\{\theta\in\mathbb R^d:\|\theta\|_0\le k\}$, where $\|\theta\|_0$ counts nonzero entries. Risk: $R_n^*(B_0(k))=\inf_{\hat\theta}\sup_{\theta\in B_0(k)}\mathbb E_\theta\|\hat\theta-\theta\|_2^2$ (p. 589).

**Theorem 30.2.**
$$R^*_n(B_0(k))\gtrsim\frac kn\log\frac{ed}{k}.\tag{30.10}$$
Remark 30.3: this is tight. It is attained by the MLE $\hat\theta_{\rm MLE}=\arg\min_{\|\theta\|_0\le k}\|\bar X-\theta\|_2$ (30.11), which keeps the $k$ largest-magnitude entries of $\bar X$. It is also attained by hard thresholding $\hat\theta^\tau_i=X_i\mathbf 1\{|X_i|\ge\tau\}$ (30.12) with suitable $\tau$. For $k=o(d)$, $R^*_n=(2+o(1))\frac kn\log\frac dk$; for $k=(\eta+o(1))d$, $R^*_n=(\beta(\eta)+o(1))d$ for some constant $\beta(\eta)$ (as printed) (pp. 589–590).

*Proof.* $B_0(k)$ is a union of linear subspaces, hence homogeneous. So $R^*_n(B_0(k))=\frac1nR^*_1(B_0(k))\triangleq\frac1nR^*(k,d)$ (30.13), and we take $n=1$, $X=\theta+Z$. The oracle bound $R^*(k,d)\ge k$ (support known, via (30.4)) means it suffices to treat $k\le d/4$ (p. 590).

Let $S^d_k=\{b\in\{0,1\}^d:w_H(b)=k\}$ be the Hamming sphere. Take $b$ uniform on $S_k^d$ and $\theta=\tau b$, $\tau=\sqrt{\log(d/k)}$. From any $\hat\theta$ define $\hat b_i=\mathbf 1\{\hat\theta_i>\tau/2\}$. Then
$$\|\theta-\hat\theta\|_2^2\ge\frac{\tau^2}{4}d_H(b,\hat b).\tag{30.14}$$
Let $\mathbb E d_H(b,\hat b)=\delta k$ and assume $\delta\le\frac14$ (otherwise done). From the chain $b\to\theta\to X\to\hat\theta\to\hat b$, data processing, $\|\theta\|_2^2=k\tau^2$ and Gaussian capacity:
$$I(b;\hat b)\le I(\theta;X)\le\tfrac d2\log\!\Big(1+\tfrac{k\tau^2}d\Big)\le\tfrac{k\tau^2}2=\tfrac k2\log\tfrac dk.$$
Conversely (p. 590),
$$I(\hat b;b)\ge\min_{\mathbb E d_H\le\delta k}I(\hat b;b)=H(b)-\max H(b|\hat b)\ge\log\binom dk-\max_{\mathbb E w_H(b\oplus\hat b)\le\delta k}H(b\oplus\hat b)=\log\binom dk-d\,h\!\Big(\frac{\delta k}d\Big),\tag{30.15}$$
the last step by Exercise I.7 (p. 591). Combine with $\binom dk\ge(d/k)^k$: $d\,h(\delta k/d)\ge\frac k2\log\frac dk$ (added step: this is what subtracting the two bounds gives; the printed inequality after "we get" does not obviously match it, see Reading notes). Since $h(p)\le-p\log p+p$ and $k/d\le\frac14$, the author concludes $\delta\ge ck/d$ for an absolute $c$, and then (30.10) via (30.14) (p. 591). (Added step: the inequality yields $\delta\ge c$, a constant; with this, (30.14) gives $\ge \frac{\tau^2}4\delta k\gtrsim k\log\frac dk$. See Reading notes.) $\square$

*Intuition note:* Recovering which $k$ of $d$ coordinates are active needs about $\log\binom dk\approx k\log(d/k)$ bits. The data give only about $\frac k2\log(d/k)$ at signal strength $\tau$, so a constant fraction of the support must be wrong.

### 30.3 Community detection (pp. 591–592)
Planted dense subgraph: $C^*$ is uniform among $k$-subsets of $[n]$, $k\ge2$. Graph $G$ on $[n]$: edge $i\ne j$ appears independently with probability $p$ if both $i,j\in C^*$, otherwise $q$, with $p>q$. So $\mathrm{ER}(k,p)$ is planted in $\mathrm{ER}(n,q)$. *Almost exact recovery* means $\mathbb E|C^*\triangle\hat C|=o(k)$ (p. 591).

**Theorem 30.3.** If $k/n$ is bounded away from one and almost exact recovery is possible, then
$$d(p\|q)\ge\frac{2+o(1)}{k-1}\log\frac nk.\tag{30.16}$$
Remark 30.4: another necessary condition is $d(p\|q)=\omega(1/k)$ (30.17), shown by reduction to testing two nodes' membership given the rest. Conditions (30.16) and (30.17) are optimal: maximum likelihood achieves almost exact recovery if (30.17) holds and $d(p\|q)\ge\frac{2+\epsilon}{k-1}\log\frac nk$ for any constant $\epsilon>0$ (details in [208]) (p. 591).

*Proof.* Let $\xi^*,\hat\xi\in\{0,1\}^n$ be indicator vectors, with $\mathbb E\,d_H(\xi^*,\hat\xi)=\epsilon_nk$, $\epsilon_n\to0$. Lower bound (a: as in (30.15); b: $k/n\le1-c$):
$$I(G;\xi^*)\ge I(\hat\xi;\xi^*)\overset{(a)}\ge\log\binom nk-n\,h\!\Big(\frac{\epsilon_nk}n\Big)\overset{(b)}\ge k\log\frac nk(1+o(1)).$$
Upper bound (p. 592): (a) variational representation of mutual information (Corollary 4.2); (b) choose $Q=\mathrm{ER}(n,q)$; (c) tensorization of KL (Theorem 2.16(d)):
$$I(G;\xi^*)\overset{(a)}=\min_QD(P_{G|\xi^*}\|Q|P_{\xi^*})\overset{(b)}\le D\big(P_{G|\xi^*}\|\mathrm{Ber}(q)^{\otimes\binom n2}\,\big|\,P_{\xi^*}\big)\overset{(c)}=\binom k2d(p\|q).$$
Combining: $k\log\frac nk(1+o(1))\le\binom k2d(p\|q)$, which is (30.16) (added step: dividing by $\binom k2=k(k-1)/2$). $\square$

### 30.4 Estimation better than chance (pp. 592–593)
Goal: error strictly below the trivial error, in regimes where vanishing risk is impossible (weak or correlated recovery). MIM is "particularly suited" here; the three methods of the next chapter fall short by losing constants (p. 592).

**Theorem 30.4 (bounded GLM continued).** $X_i\overset{\rm iid}\sim\mathcal N(\theta,I_d)$, $\theta$ in the unit ball $B$. For a universal $C_0$:
$$e^{-\frac{n+C_0}{d-1}}\le\inf_{\hat\theta}\sup_{\theta\in B}\mathbb E_\theta\|\hat\theta-\theta\|^2\le\frac d{d+n}.$$
The trivial error is 1. So non-trivial estimation is possible iff $n$ grows proportionally with $d$; for $d\gg n\gg1$ the optimal error is $1-\frac nd(1+o(1))$ (p. 592).

*Proof.* Take $X=\theta+Z/\sqrt n$. Upper bound: shrinkage $\hat\theta=\frac1{1+d/n}X$ gives $\le\frac d{n+d}$ (the Bayes estimator for $\mathcal N(0,\frac1dI_d)$). Lower bound: MIM with prior $\mathrm{Unif}(S^{d-1})$ and (30.6), so $I(\theta;X)\le n/2$. The constant $1/2$ matters, so the diameter bound (30.7) is too loose. Theorem 27.17 gives $I(\theta;\hat\theta)\ge\frac{d-1}2\log\frac1{\mathbb E\|\hat\theta-\theta\|^2}-C$. Data processing then yields the bound (pp. 592–593); explicitly $\frac{d-1}2\log\frac1E-C\le\frac n2$ (added step). $\square$

**Discrete distributions** (p. 593): to estimate $P$ on $k$ points from $n$ samples under total variation (at most 1): the error of any estimator is $1-o(1)$ if $n\ll k$ (Ex. VI.10f). An estimator has $\mathbb E\chi^2(P\|\hat P)\le\frac{k-1}{n+1}$ (Ex. VI.10b). With the TV–$\chi^2$ joint range (7.32) and Jensen:
$$\mathbb E\,\mathrm{TV}(P,\hat P)\le\begin{cases}\frac12\sqrt{\frac{k-1}{n+1}}&n\ge k-2\\[2pt]\frac{k-1}{k+n}&n\le k-2,\end{cases}$$
which is bounded away from one when $n=\Omega(k)$. So non-trivial TV estimation is possible iff $n$ scales at least proportionally with $k$. The author adds that the information-theoretic threshold for correlated recovery in the stochastic block model can be established by bounding an appropriate mutual information; see Section 33.9 for the Gaussian version (spiked Wigner model) (p. 593).

## Toy example (ours)
Scalar case $d=1$, $n=1$, prior $\theta\sim\mathcal N(0,3)$, so $s=3$. Take logs base 2.
- $I(\theta;X)=\frac12\log_2(1+sn)=\frac12\log_2 4=1$ bit.
- $\phi(D)=\frac12\log_2\frac{3}{D}$. Setting $\phi(D)=1$ gives $3/D=4$, so $D=0.75$.
- So no estimator has mean squared error below $0.75$ under this prior. This equals $\frac{sd}{1+sn}=\frac34$.
- Check: the posterior variance is $1/(1/3+1)=3/4$.
Here MIM is tight, because the Gaussian channel and Gaussian source both meet their bounds with equality.

## Concepts
- [[mutual-information-method]] (new) — lower-bound risk by $\phi(D)\le I(\theta;X)\le C$ and invert $\phi$ (p. 585)
- [[mutual information I(X;Y)]] — information the data give about $\theta$; capped by channel capacity (p. 585)
- [[rate–distortion function]] — here $\phi(D)$, the minimum $I(\theta;\hat\theta)$ at expected loss $\le D$ (p. 585)
- [[data processing inequality]] — applied to $\theta\to X\to\hat\theta$ (p. 585)
- [[channel capacity]] — $\sup_\pi I(\theta;X)$ for the model $P_{X|\theta}$ (p. 585)
- [[shannon-lower-bound]] (new) — $h(\theta)+\frac d2\log\frac{2\pi ed}D$ bound on rate-distortion for isotropic $\theta$ (p. 588)
- [[bayes-minimax-risk]] (new) — $R^*_\pi$ for prior $\pi$; minimax risk is at least any Bayes risk (p. 585)
- [[almost-exact-recovery]] (new) — $\mathbb E|C^*\triangle\hat C|=o(k)$ (p. 591)
- [[weak-recovery]] (new) — error strictly better than the trivial (no-data) error (p. 592)
- [[relative entropy / KL divergence]] — used for the information-radius bound and tensorization (pp. 587, 592)

## Canonical instances
- [[gaussian-location-model]] — unconstrained, ball, sparse and non-quadratic-loss minimax risk by MIM (pp. 586–590)
- [[planted-dense-subgraph]] — necessary condition (30.16) for almost exact recovery (p. 591)
- [[sparse-vector-denoising]] — rate $\frac kn\log\frac{ed}k$ (p. 589)
- [[discrete-distribution-estimation-tv]] — non-trivial TV estimation iff $n\gtrsim k$ (p. 593)

## Bridges (candidates)
- [structural-analogy] MIM ↔ information-theory: converse of joint source–channel coding — same "rate-distortion ≤ capacity" chain (p. 585)
- [same-math] SLB for $\phi$ ↔ rate-distortion theory: Shannon lower bound (Section 26.1)
- [structural-analogy] Volume bound for metric entropy ↔ SLB for rate-distortion (Remark 30.2)
- [structural-analogy] Weak recovery thresholds ↔ rational inattention: limited information capacity limits attainable accuracy

## Questions this raises
- Why does the diameter-based bound (30.7) fail at the $n/2$ constant, while capacity (30.6) works?
- How do Fano, Assouad and Le Cam arise from MIM, and where exactly do they lose constants?
- Can the $\ell_\infty$ loss attain the $\frac{\log d}{n}$ rate by MIM with a better prior (Section 31.4)?
- Is $n\gtrsim d$ also sufficient in Theorem 30.4 for general parameter sets?

## Reading notes
- Printed pages 585–593; the printed offset is pdf − 25. The source heading numbers the chapter 30 (the unit label says ch33); sections are 30.1–30.4.
- (30.6): the image prints the sup constraint as $\mathbb E\|\theta\|_2^2\le r$; the context ($\theta\in B(r)$) suggests $r^2$. (30.7) prints $\theta$ twice in the KL term; the second is presumably $\theta'$.
- First line of the lower bound in the proof of Thm 30.2 prints "$\delta d$" in the constraint; the next line has $\delta k$.
- p. 591: the inequality printed after "we get" does not obviously match the subtraction of the two mutual-information bounds, and the printed conclusion is "$\delta\ge ck/d$". My own derivation (not printed) from $\log\binom dk\ge k\log\frac dk$ minus $\frac k2\log\frac dk$ gives $d\,h(\delta k/d)\ge\frac k2\log\frac dk$ and then $\delta\ge c$; the L3 steps marked "added step" use this.
- p. 588: the line after "applying (30.3) yields" appears to print $\frac12\log\frac{cr^2}{R^*}$; the digest writes $\frac d2$, which is needed for $R^*\ge cr^2e^{-nr^2/d}$.
- Section 30.4 says "bounded away from one whenever $n=\Omega(k)$" as printed.
