---
id: polyanskiy-2025-information/ch03-divergence
work: polyanskiy-2025-information
unit: "Chapter 2 (printed numbering; unit id ch03) — Divergence"
pages: 20-40
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Divergence (KL divergence, chain rule, data processing, Fisher information)

## L0 — One line
KL divergence $D(P\|Q)=\mathbb E_Q[\frac{dP}{dQ}\log\frac{dP}{dQ}]$ is non-negative, obeys a chain rule, and therefore cannot increase under any random processing (data-processing inequality); in smooth parametric families (under regularity conditions) it is locally quadratic with the Fisher information as Hessian.

## L1 — The gist (≤ 120 words)
The chapter asks how to measure the dissimilarity of two distributions $P$ and $Q$ in full generality, and what properties follow. The answer is the KL divergence, defined through Radon–Nikodym derivatives. It is non-negative (Jensen), asymmetric, and satisfies a chain rule. The chain rule gives monotonicity and the data-processing inequality: passing both distributions through the same channel cannot increase divergence. The chapter also treats differential entropy as a divergence from Lebesgue measure, and shows that for nearby distributions divergence typically behaves like a quadratic form. In a smooth parametric family, under regularity conditions, that form is given by the Fisher information. These facts underlie testing, large deviations and statistics.

**Prerequisites:** discrete entropy; Jensen's inequality; expectation and densities; Taylor expansion; basic matrix algebra (trace, determinant); optional measure theory (absolute continuity). Terms used in L2: a *Markov kernel* is a rule that gives a distribution of $Y$ for each value $x$ (a channel); *disintegration* writes a joint law as marginal times kernel; *standard Borel* is a well-behaved class of measurable spaces (countable sets, $\mathbb R^n$, ...); *tensorization* means divergence of product measures is the sum of divergences; $\chi^2(P\|Q)=\int dQ(\frac{dP}{dQ}-1)^2$; *score* $V=\nabla_\theta\ln p_\theta(X)$ and *Fisher information* $J_F=\mathbb E[VV^\top]$; $o(\lambda)$ means smaller than $\lambda$ as $\lambda\to0$.

## L2 — Key ideas
- Definition: $D(P\|Q)=\mathbb E_Q[\frac{dP}{dQ}\log\frac{dP}{dQ}]$ if $P\ll Q$, else $+\infty$; it equals $\mathbb E_P[\log\frac{dP}{dQ}]$ and reduces to the usual sums and integrals in the discrete and density cases (pp. 21–22, 25–26).
- $D$ is in general not symmetric, so it is not a distance. The coin example gives $D(P\|Q)=\infty$ but $D(Q\|P)=1$ bit (p. 22).
- Information inequality: $D(P\|Q)\ge0$, with equality iff $P=Q$, by Jensen. Consequence: $Q=P_X$ uniquely minimizes expected log-loss $\mathbb E\log\frac1{Q(X)}$, giving $H(X)$ (p. 24).
- Differential entropy is $-D(P\|\mathrm{Leb})$. It can be negative and can increase under deterministic processing (e.g. scaling), but it keeps uniform-maximality, a chain rule, and Gaussian maximality under covariance constraints (pp. 26–28).
- Markov kernels (channels) and disintegration formalize conditioning. Standard Borel assumptions are needed: Example 2.5 shows pathologies otherwise (pp. 29–31).
- Chain rule $D(P_{X,Y}\|Q_{X,Y})=D(P_{Y|X}\|Q_{Y|X}|P_X)+D(P_X\|Q_X)$ gives monotonicity, tensorization and the data-processing inequality (pp. 32–35).
- Large-deviations estimate: $d(P[E]\|Q[E])\le D(P\|Q)$, from processing with an indicator (p. 35).
- Local behaviour: $D(\lambda P+\bar\lambda Q\|Q)$ is $o(\lambda)$ when $D(P\|Q)<\infty$ and typically $\sim\frac{\lambda^2\log e}{2}\chi^2(P\|Q)$ (pp. 36–38).
- In smooth families $D(P_{\theta_0}\|P_{\theta_0+\xi})=\frac{\log e}{2}\xi^\top J_F(\theta_0)\xi+o(\|\xi\|^2)$ under suitable conditions (p. 39).

## L3 — Walkthrough

### Opening and review box (p. 20)
The chapter defines $D(P\|Q)$ (also called information divergence, KL divergence, relative entropy), the first example of a dissimilarity measure; KL is later shown to be a special case of $f$-divergences (Ch. 7). Measure-theoretic machinery (Radon–Nikodym derivatives, Markov kernels) can be ignored for finite or countable alphabets. The review box fixes two conventions. Integrals are of extended-real functions, and a null set contributes $0$. Alphabets are standard Borel spaces (countable sets, $\mathbb R^n$, $\mathbb R^\infty$; products of standard Borel spaces; singletons and the diagonal are measurable) (p. 20).

### 2.1 Divergence and Radon–Nikodym derivatives
**Special cases** (p. 21).
$$D(P\|Q)\triangleq\begin{cases}\sum_{a:P(a),Q(a)>0}P(a)\log\frac{P(a)}{Q(a)} & \mathrm{supp}(P)\subset\mathrm{supp}(Q)\\ +\infty&\text{otherwise}\end{cases}\tag{2.1}$$
$$D(P\|Q)=\begin{cases}\int_{\{p>0,q>0\}}p\log\frac pq\,dx & \mathrm{Leb}\{p>0,q=0\}=0\\+\infty&\text{otherwise}\end{cases}\tag{2.2}$$
These do not cover measures on manifolds or on sequence spaces, so one needs absolute continuity: $P\ll Q$ means $Q(E)=0\Rightarrow P(E)=0$. Then there is $f\ge0$ with $P(E)=\int_E f\,dQ$ (2.3), and $f=\frac{dP}{dQ}$ is the relative density (Radon–Nikodym derivative). The author notes it may not be unique. In simple cases it is the likelihood ratio (ratio of pmfs or pdfs) (p. 21).

**Definition 2.1** (reference measure $Q$), with $0\log0=0$ (pp. 21–22):
$$D(P\|Q)=\begin{cases}\mathbb E_Q\big[\frac{dP}{dQ}\log\frac{dP}{dQ}\big]&P\ll Q\\+\infty&\text{otherwise}\end{cases}\tag{2.4}$$
It is shown below (Lemma 2.5) that this is well defined and equals $\mathbb E_P[\log\frac{dP}{dQ}]$ when $P\ll Q$ (p. 22).

For densities $f_P,f_Q$ w.r.t. a common dominating measure $\mu$ (e.g. $\mu=P+Q$):
$$D(P\|Q)=\begin{cases}\int_{f_Q>0,f_P>0}d\mu\,f_P\log\frac{f_P}{f_Q}&\mu(\{f_Q=0,f_P>0\})=0\\+\infty&\text{otherwise}\end{cases}\tag{2.5}$$
Reason: $P\ll Q$ iff $\mu(\{f_Q=0,f_P>0\})=0$, and then $\frac{dP}{dQ}=\frac{f_P}{f_Q}$ $Q$-a.e. (p. 22).

**Infinite divergence** (p. 22). $D$ can be $+\infty$ even if $P\ll Q$, e.g. $D(\text{Cauchy}\|\text{Gaussian})=\infty$. The author says these are not two different kinds of infinity. In both cases some sequence of finer finite partitions makes the discretized divergence grow without bound (Theorem 4.5, later).

**Asymmetry** (p. 22). $D(P\|Q)\ne D(Q\|P)$ in general, so $D$ is not a distance. This reflects asymmetry in hypothesis testing. Coin example: under $P$ the coin is fair, under $Q$ it always lands heads. After HHHHHHH one leans to $Q$ but can never be absolutely sure. After HHT one knows it is $P$. Indeed $D(P\|Q)=\infty$ and $D(Q\|P)=1$ bit.

**Theorem 2.2.** If $P$ is supported on a finite set $\mathcal A$, then $H(P)=\log|\mathcal A|-D(P\|U_{\mathcal A})$. Proof: $D(P\|U_\mathcal A)=\mathbb E_P[\log\frac{P(X)}{1/|\mathcal A|}]=\log|\mathcal A|-H(P)$ (p. 22).

**Example 2.1 (binary divergence)** (p. 22–23). For $P=\mathrm{Ber}(p)$, $Q=\mathrm{Ber}(q)$:
$$D(P\|Q)=d(p\|q)\triangleq p\log\frac pq+\bar p\log\frac{\bar p}{\bar q}\tag{2.6}$$
Plots show $d(p\|q)$ vanishing at $q=p$ and growing away from it, as a function of $q$ for fixed $p$ and of $p$ for fixed $q$. A quadratic lower bound "easily checked" is $d(p\|q)\ge2(p-q)^2\log e$, a special case of Pinsker's inequality (Thm 7.10) (p. 23).

**Example 2.2 (real Gaussian)** (p. 23):
$$D(\mathcal N(m_1,\sigma_1^2)\|\mathcal N(m_0,\sigma_0^2))=\frac{\log e}{2}\frac{(m_1-m_0)^2}{\sigma_0^2}+\frac12\Big[\log\frac{\sigma_0^2}{\sigma_1^2}+\Big(\frac{\sigma_1^2}{\sigma_0^2}-1\Big)\log e\Big]\tag{2.7}$$
The first term compares means, the second compares variances. For $\mathbb R^k$ with $\det\Sigma_0\ne0$:
$$D(\mathcal N(m_1,\Sigma_1)\|\mathcal N(m_0,\Sigma_0))=\frac{\log e}{2}(m_1-m_0)^\top\Sigma_0^{-1}(m_1-m_0)+\frac12\Big(\log\det\Sigma_0-\log\det\Sigma_1+\mathrm{tr}(\Sigma_0^{-1}\Sigma_1-I)\log e\Big)\tag{2.8}$$
(derivation is Exercise I.8, not in this unit).

**Example 2.3 (complex Gaussian)** (pp. 23–24). $\mathcal N_c(m,\sigma^2)$ has density $\frac1{\pi\sigma^2}e^{-|z-m|^2/\sigma^2}$; real and imaginary parts are independent real Gaussians with variance $\sigma^2/2$ each. The author says the scalar formula (2.9) follows from (2.8); as printed it does not match that substitution (see Reading notes):
$$D(\mathcal N_c(m_1,\sigma_1^2)\|\mathcal N_c(m_0,\sigma_0^2))=\frac{\log e}{2}\frac{|m_1-m_0|^2}{\sigma_0^2}+\log\frac{\sigma_0^2}{\sigma_1^2}+\Big(\frac{\sigma_1^2}{\sigma_0^2}-1\Big)\log e\tag{2.9}$$
For complex vectors in $\mathbb C^k$, $\det\Sigma_0\neq0$ (p. 24):
$$D=(m_1-m_0)^H\Sigma_0^{-1}(m_1-m_0)\log e+\log\det\Sigma_0-\log\det\Sigma_1+\mathrm{tr}(\Sigma_0^{-1}\Sigma_1-I)\log e.$$
(See Reading notes on a possible factor $\tfrac12$ in (2.9).)

*Intuition note.* $D(P\|Q)$ is the average log-likelihood ratio, taken under $P$. It is infinite when $P$ puts mass where $Q$ puts none, which is why the order of arguments matters.

### 2.2 Main inequality and equivalent expressions
**Theorem 2.3 (information inequality).** $D(P\|Q)\ge0$, with equality iff $P=Q$. Proof: take $P\ll Q$ (otherwise $D=\infty$). With $\varphi(x)=x\log x$, strictly convex on $\mathbb R_+$, Jensen gives
$$D(P\|Q)=\mathbb E_Q\Big[\varphi\Big(\tfrac{dP}{dQ}\Big)\Big]\ge\varphi\Big(\mathbb E_Q\tfrac{dP}{dQ}\Big)=\varphi(1)=0,$$
with equality iff $\frac{dP}{dQ}=1$ $Q$-a.e., i.e. $P=Q$ (p. 24).

**Corollary 2.4.** For discrete $X$ with $H(X)<\infty$: $\min_Q\mathbb E[\log\frac1{Q(X)}]=H(P)$, with unique minimizer $Q=P_X$. Proof: for $Q\ne P_X$ with finite left side, $\mathbb E\log\frac1{Q(X)}-H(X)=\mathbb E\log\frac{P_X(X)}{Q(X)}=D(P_X\|Q)>0$. The author notes this shows minimizing average cross-entropy loss recovers the true distribution (p. 24).

The proof of Thm 2.3 explains why $D$ is defined with $\mathbb E_Q[\cdots]$ (the proof applies Jensen to $\varphi(\frac{dP}{dQ})$ under $\mathbb E_Q$). Lemma 2.5 shows it agrees with the $\mathbb E_P$ form (p. 25).

**Lemma 2.5.** Let $P,Q,R\ll\mu$ with densities $f_P,f_Q,f_R$. Define $\mathrm{Log}\frac ab$ by
$$\mathrm{Log}\frac ab=\begin{cases}-\infty&a=0,b>0\\+\infty&a>0,b=0\\0&a=b=0\\\log\frac ab&a,b>0\end{cases}\tag{2.10}$$
Then:
- $\mathbb E_P\big[\mathrm{Log}\frac{f_R}{f_Q}\big]=D(P\|Q)-D(P\|R)$, provided at least one of the divergences is finite (2.11).
- $\mathbb E_P\big[\mathrm{Log}\frac{f_P}{f_Q}\big]$ is well defined (possibly infinite) and equals $D(P\|Q)$ (2.12). When $P\ll Q$: $D(P\|Q)=\mathbb E_P[\log\frac{dP}{dQ}]$ (2.13) (p. 25).

Remark 2.1: ignoring zeros, (2.12) is the identity $\log\frac{dR}{dQ}=\log\frac{dP}{dQ}-\log\frac{dP}{dR}$. $\mathrm{Log}$ satisfies $\mathrm{Log}\frac ab=-\mathrm{Log}\frac ba$ and $\mathrm{Log}\frac ab=\mathrm{Log}\frac ac+\mathrm{Log}\frac cb=\mathrm{Log}\frac{ac}b-\log c$ for $c>0$, except when $a=b=0$ (p. 25).

*Proof, key steps* (pp. 25–26).
1. If $D(P\|Q)=\infty$ and $D(P\|R)<\infty$: $P[f_R=0]=0$ and $f_P>0$ $P$-a.s., so $\mathrm{Log}\frac{f_R}{f_Q}=\mathrm{Log}\frac{f_R}{f_P}+\mathrm{Log}\frac{f_P}{f_Q}$ (2.14). The first term has expectation $-D(P\|R)$ (finite), the second is infinite, so (2.11) is $+\infty$ on both sides.
2. If $D(P\|Q)<\infty$: $P[f_Q=0]=0$, (2.14) holds again, the second term has finite expectation and the first is non-negative, so (2.11) holds (both sides possibly $-\infty$).
3. For (2.12), first the negative part is bounded: $\mathbb E_P[\min(\mathrm{Log}\frac{f_P}{f_Q},0)]\ge-\frac{\log e}{e}$ (2.15). Proof: with $g(x)=\min(x\log x,0)\in[-\frac{\log e}e,0]$, the left side equals $\int_{\{f_Q>0\}}f_Q\,g(f_P/f_Q)\,d\mu$.
4. If $P[f_Q=0]>0$, both sides are $+\infty$. Otherwise, on $E=\{f_P>0,f_Q>0\}$ with $P[E]=1$, $\mathbb E_P\mathrm{Log}\frac{f_P}{f_Q}=\int_E d\mu f_Q\varphi(\frac{f_P}{f_Q})=\mathbb E_Q[1_E\varphi(\frac{f_P}{f_Q})]$. The indicator can be dropped because $\varphi=0$ on $\{f_P=0,f_Q>0\}$, which gives (2.12).
5. (2.13) follows by taking $\mu=Q$ (p. 26).

*Intuition note.* The two definitions of $D$ agree. The special function $\mathrm{Log}$ is just $\log$ with sensible values when a density is zero, so that the "subtract two log-ratios" identity survives zeros.

### 2.3 Differential entropy
$D$ extends verbatim to non-probability measures, where it can be negative. A sufficient condition for $D(P\|Q)\ge0$: $P$ is a probability measure and $Q$ is sub-probability ($\int dQ\le1=\int dP$) (p. 26).

**Definition 2.6.** $h(X)=h(P_X)\triangleq-D(P_X\|\mathrm{Leb})$ (2.16). If $X$ has pdf $p$, $h(X)=\mathbb E\log\frac1{p(X)}$; otherwise $h(X)=-\infty$. Conditional: $h(X|Y)\triangleq\mathbb E\log\frac1{p_{X|Y}(X|Y)}$ (p. 27).

**Example 2.4 (Gaussian).** $h(X)=\frac12\log(2\pi e\sigma^2)$ for $X\sim\mathcal N(\mu,\sigma^2)$ (2.17); $h(X)=\frac12\log((2\pi e)^d\det\Sigma)$ for $\mathcal N(\mu,\Sigma)$ in $\mathbb R^d$ (2.18) (p. 27).

**Warning** (p. 27). $h(X)$ can be positive, negative, $\pm\infty$ or undefined. Differences from Shannon entropy: processing can increase $h$ (e.g. scaling), whereas $H(f(X))\le H(X)$. For integer-valued independent $X,Y$, $H(X+Y)\le H(X)+H(Y)$ is finite. For differential entropy there is a real $X$ with finite $h(X)$ such that $h(X+Y)=\infty$ for every independent $Y$ with $h(Y)>-\infty$; there are also $X,Y$ with finite $h$ such that $h(X+Y)$ does not exist.

**Theorem 2.7** (assuming all entropies exist and are finite) (pp. 27–28):
- (a) If $\mathbb P[X^n\in S]=1$ then $h(X^n)\le\log\mathrm{Leb}(S)$, with equality iff $X^n$ is uniform on $S$.
- (b) $h(X^n+x)=h(X^n)$; $h(\alpha X^n)=h(X^n)+k\log|\alpha|$; for invertible $A$, $h(AX^n)=h(X^n)+\log|\det A|$.
- (c) $h(X|Y)\le h(X)$ ($Y$ arbitrary).
- (d) Chain rule: $h(X^n)=\sum_{k=1}^nh(X_k|X^{k-1})$.
- (e) $T\mapsto h(X_T)$ is submodular.
- (f) Han's inequality: $k\mapsto\frac1{k\binom nk}\sum_{T\in\binom{[n]}{k}}h(X_T)$ is decreasing in $k$.

Proof (p. 28): (a), (c), (d) follow as in Thm 1.4, (b) by change of variables, (e), (f) as in Thms 1.6, 1.7.

**Theorem 2.8** ($\mathrm{Cov}(X)=\mathbb E[XX^\top]-\mathbb E[X]\mathbb E[X]^\top$; $\Sigma$ positive definite):
$$\max_{P_X:\mathrm{Cov}(X)\preceq\Sigma}h(X)=h(\mathcal N(0,\Sigma))=\tfrac12\log((2\pi e)^d\det\Sigma)\tag{2.19}$$
$$\max_{P_X:\mathbb E[\|X\|^2]\le a}h(X)=h\big(\mathcal N(0,\tfrac adI_d)\big)=\tfrac d2\log\tfrac{2\pi ea}{d}\ (a>0)\tag{2.20}$$
Proof of (2.19): assume $\mathbb E X=0$; then
$$0\le D(P_X\|\mathcal N(0,\Sigma))=-h(X)+\tfrac12\log((2\pi)^d\det\Sigma)+\tfrac{\log e}2\mathbb E[X^\top\Sigma^{-1}X]\le-h(X)+h(\mathcal N(0,\Sigma)),$$
using $\mathbb E[X^\top\Sigma^{-1}X]=\mathrm{Tr}(\mathbb E[XX^\top]\Sigma^{-1})\le\mathrm{Tr}(I)$ and (2.18). (2.20) is analogous with reference $\mathcal N(0,\frac adI_d)$ (p. 28).

**Corollary 2.9.** $\Sigma\mapsto\log\det\Sigma$ is concave on positive definite $n\times n$ matrices. Proof: $Y\sim\mathrm{Ber}(1/2)$, $X|Y=0\sim\mathcal N(0,\Sigma_1)$, $X|Y=1\sim\mathcal N(0,\Sigma_2)$, $\mathrm{Cov}(X)=\Sigma=\frac12\Sigma_1+\frac12\Sigma_2$. Then $h(X|Y)\le h(X)\le\frac12\log((2\pi e)^n\det\Sigma)$; applying (2.18) to $h(X|Y)$ gives $\frac12\log\det\Sigma_1+\frac12\log\det\Sigma_2\le\log\det(\frac12\Sigma_1+\frac12\Sigma_2)$ (p. 28).

**Quantization link** (p. 29). With $X_m=\frac1m\lfloor mX\rfloor$ (componentwise), Rényi: if $H(\lfloor X\rfloor)<\infty$ and $h(X)$ is defined,
$$H(X_m)=d\log m+h(X)+o(1),\quad m\to\infty.\tag{2.21}$$
For $d=1$, $m=2^k$, $X\in[0,1]$, this suggests the $k$ quantization bits behave like independent fair coin flips, because for "nice" densities small intervals are approximately uniform.

*Intuition note.* Differential entropy is minus a divergence from Lebesgue measure, so it inherits some properties (maximality, chain rule) but not others (it can be negative, and processing can increase it); Lebesgue measure is not a probability measure.

### 2.4 Markov kernels
**Definition 2.10.** A Markov kernel $K:\mathcal X\to\mathcal Y$ is $K(\cdot|\cdot)$ with (1) $K(\cdot|x)$ a probability measure on $\mathcal Y$ for every $x$, and (2) $x\mapsto K(A|x)$ measurable for every measurable $A$. Written $P_{Y|X}$ or $X\xrightarrow{P_{Y|X}}Y$; in information theory it is a *channel* (input $X$, output $Y$) (p. 29).

Explicit examples (p. 29): deterministic $Y=f(X)$ ($P_{Y|X=x}=\delta_{f(x)}$); decoupled $Y\perp X$ ($P_{Y|X=x}=P_Y$); additive noise $Y=X+Z$, $Z\perp X$ ($P_{Y|X=x}=P_Z(\cdot-x)$, so $P_Y=P_X*P_Z$, a convolution). Other channels come later (Examples 3.3, 3.4, 3.6).

**Theorem 2.11 (disintegration).** If $P_{X,Y}$ is on $\mathcal X\times\mathcal Y$ with $\mathcal Y$ standard Borel, there is a kernel $K$ with
$$P_{X,Y}[E]=\int_{\mathcal X}P_X(dx)K(E^x|x),\quad E^x\triangleq\{y:(x,y)\in E\}\tag{2.22}$$
and $\int f\,dP_{X,Y}=\int P_X(dx)\int f(x,y)K(dy|x)$ for integrable $f$. A joint law can have many versions of $P_{Y|X}$, differing on a $P_X$-null set of $x$ (p. 30).

Operations (p. 30): *multiplication* $P_{X,Y}\triangleq P_XP_{Y|X}$ (discrete: $P_{X,Y}(x,y)=P_{Y|X}(y|x)P_X(x)$); *composition* $P_{Y|X}\circ P_X\triangleq P_Y$, i.e. $P_Y[E]=\int P_X(dx)P_{Y|X}(E|x)$, also written $P_X\xrightarrow{P_{Y|X}}P_Y$.

**Example 2.5 (cautionary)** (pp. 30–31). Let $\mathcal X=[0,1]$ with Borel sets, $\mathcal Y=[0,1]$ with the $\sigma$-algebra $\sigma_\mathcal Y$ of sets that are countable or have countable complement. Define $K(A|x)=1\{x\in A\}$ (so $Y=X$), $X\sim\mathrm{Unif}(0,1)$. For $E=B\times C$, $P_{X,Y}[B\times C]=P_X[B\cap C]$. If $C$ is countable both $P_{X,Y}[E]$ and $P_XP_Y[E]$ are $0$; if $C^c$ is countable both equal $P_X[B]$. So $P_{X,Y}=P_XP_Y$, i.e. $X\perp Y$ and $X=Y$ at the same time. Both $P_{Y|X}=K$ and $P_{Y|X}=P_Y$ are valid versions. Since $P_Y[\{x\}]=0$, $K(\cdot|x)\not\ll P_Y$ for every $x$. So $D(P_{Y|X=x}\|P_Y)$ can be $0$ or $+\infty$ for every $x$, depending on the version. The author advises staying with standard Borel spaces (p. 31).

**Theorem 2.12 (Doob's Radon–Nikodym).** If $\mathcal Y$ has a separable $\sigma$-algebra and $P_{Y|X=x}\ll R_{Y|X=x}$ for every $x$, there is a jointly measurable $f(y|x)\ge0$ with $P_{Y|X}(E|x)=\int_Ef(y|x)R_{Y|X}(dy|x)$. So $\frac{dP_{Y|X=x}}{dR_{Y|X=x}}$ can be chosen jointly measurable in $(x,y)$ (p. 31).

### 2.5 Conditional divergence, chain rule, data processing
Fix kernels $P_{Y|X},Q_{Y|X}$ and $P_X$. For discrete $\mathcal X$: $D(P_{Y|X}\|Q_{Y|X}|P_X)\triangleq\sum_xP_X(x)D(P_{Y|X=x}\|Q_{Y|X=x})$ (p. 31).

**Lemma 2.13.** If $\mathcal Y$ is standard Borel, the set $A_0=\{x:P_{Y|X=x}\ll Q_{Y|X=x}\}$ and the map $x\mapsto D(P_{Y|X=x}\|Q_{Y|X=x})$ are measurable. Proof sketch: take $R_{Y|X}=\frac12P_{Y|X}+\frac12Q_{Y|X}$, densities $f_P,f_Q$ jointly measurable (Thm 2.12), $B_0=\{(x,y):f_P>0,f_Q=0\}$; $x\in A_0$ iff $R_{Y|X=x}[B_0^x]=0$. Then, from (2.12),
$$D(P_{Y|X=x}\|Q_{Y|X=x})=\mathbb E_{Y\sim P_{Y|X=x}}\Big[\mathrm{Log}\frac{f_P(Y|x)}{f_Q(Y|x)}\Big]\tag{2.23}$$
which is measurable (pp. 31–32).

**Definition 2.14.** $D(P_{Y|X}\|Q_{Y|X}|P_X)\triangleq\mathbb E_{x\sim P_X}[D(P_{Y|X=x}\|Q_{Y|X=x})]$. It can be finite even if $D(P_{Y|X=x}\|Q_{Y|X=x})=\infty$ on a $P_X$-null set of $x$ (p. 32).

**Theorem 2.15 (chain rule).**
$$D(P_{X,Y}\|Q_{X,Y})=D(P_{Y|X}\|Q_{Y|X}|P_X)+D(P_X\|Q_X)\tag{2.24}$$
regardless of the versions of the conditionals. Proof (pp. 32–33):
1. Discrete case with $Q_{X,Y}>0$: $\mathbb E\log\frac{P_X(X)P_{Y|X}(Y|X)}{Q_X(X)Q_{Y|X}(Y|X)}$ splits into the two terms.
2. General case: if $P_X\not\ll Q_X$ then $P_{X,Y}\not\ll Q_{X,Y}$ and both sides are $\infty$. Otherwise let $\lambda_P=\frac{dP_X}{dQ_X}$, and $f_P,f_Q,R_{Y|X}$ as in Lemma 2.13. With $R_{X,Y}\triangleq Q_XR_{Y|X}$, $P_{X,Y}[E]=\int_E\lambda_P(x)f_P(y|x)\,dR_{X,Y}$ and $Q_{X,Y}[E]=\int_Ef_Q(y|x)\,dR_{X,Y}$. By (2.12):
$$D(P_{X,Y}\|Q_{X,Y})=\mathbb E_{P_{X,Y}}\Big[\mathrm{Log}\frac{f_P(Y|X)\lambda_P(X)}{f_Q(Y|X)}\Big]\tag{2.25}$$
3. Use $\mathrm{Log}\frac{ac}b=\log c+\mathrm{Log}\frac ab$ (valid unless $a=b=0$). It applies because $P_{X,Y}[f_P>0,\lambda_P>0]=1$, so $P_{X,Y}$-a.s. $\mathrm{Log}\frac{f_P\lambda_P}{f_Q}=\log\lambda_P+\mathrm{Log}\frac{f_P}{f_Q}$. The negative parts have finite expectation by (2.15), so linearity is legitimate. The first term is $D(P_X\|Q_X)$ by (2.12), the second $D(P_{Y|X}\|Q_{Y|X}|P_X)$ by (2.23).

**Theorem 2.16 (properties).** For standard Borel $\mathcal X,\mathcal Y$ (p. 33):
- (a) $D(P_{Y|X}\|Q_{Y|X}|P_X)=D(P_XP_{Y|X}\|P_XQ_{Y|X})$.
- (b) Monotonicity: $D(P_{X,Y}\|Q_{X,Y})\ge D(P_Y\|Q_Y)$.
- (c) Full chain rule: $D(P_{X_1\cdots X_n}\|Q_{X_1\cdots X_n})=\sum_{i=1}^nD(P_{X_i|X^{i-1}}\|Q_{X_i|X^{i-1}}|P_{X^{i-1}})$ (2.26). If $Q_{X^n}=\prod Q_{X_i}$:
$$D(P_{X^n}\|Q_{X_1}\cdots Q_{X_n})=D(P_{X^n}\|P_{X_1}\cdots P_{X_n})+\sum_iD(P_{X_i}\|Q_{X_i})\ge\sum_iD(P_{X_i}\|Q_{X_i})\tag{2.27}$$
with equality iff $P_{X^n}=\prod_jP_{X_j}$.
- (d) Tensorization: $D(\prod_jP_{X_j}\|\prod_jQ_{X_j})=\sum_jD(P_{X_j}\|Q_{X_j})$.
- (e) Conditioning increases divergence: with $P_Y=P_{Y|X}\circ P_X$, $Q_Y=Q_{Y|X}\circ P_X$, $D(P_Y\|Q_Y)\le D(P_{Y|X}\|Q_{Y|X}|P_X)$, with equality iff $D(P_{X|Y}\|Q_{X|Y}|P_Y)=0$.

Proofs (p. 34): (a) from (2.24) since the two $X$-marginals are equal. (b) apply (2.24) with $X,Y$ swapped and use non-negativity of conditional divergence. (c) telescoping the factorizations. (d) from (c). (e) inequality from (a)+(b); for equality, $D(P_{X,Y}\|Q_{X,Y})=D(P_{Y|X}\|Q_{Y|X}|P_X)+\underbrace{D(P_X\|P_X)}_{=0}=D(P_{X|Y}\|Q_{X|Y}|P_Y)+D(P_Y\|Q_Y)$. Without standard Borel, (a) can fail: Example 2.5 gives $P_XP_{Y|X}=P_XQ_{Y|X}$ with $P_{Y|X}\ne Q_{Y|X}$ and conditional divergence $\infty$ (p. 34).

Remarks (p. 34): the full chain rule decomposes the "distance" from $P_{X^n}$ to $Q_{X^n}$ into steps (cf. Ex. I.43). $D(P_{X,Y}\|Q_{X,Y})$ and $D(P_X\|Q_X)+D(P_Y\|Q_Y)$ are in general incomparable. If $X=Y$ under both, the first equals $D(P_X\|Q_X)$, less than the sum $2D(P_X\|Q_X)$. If $P_X=Q_X$, $P_Y=Q_Y$ but $P_{X,Y}\ne Q_{X,Y}$, the first is $>0$ and the second is $0$.

**Theorem 2.17 (DPI).** With $P_Y=P_{Y|X}\circ P_X$ and $Q_Y=P_{Y|X}\circ Q_X$ (same channel),
$$D(P_Y\|Q_Y)\le D(P_X\|Q_X)\tag{2.28}$$
with equality iff $D(P_{X|Y}\|Q_{X|Y}|P_Y)=0$. Proof: chain rule applied both ways, $D(P_{X,Y}\|Q_{X,Y})=\underbrace{D(P_{Y|X}\|P_{Y|X}|P_X)}_{=0}+D(P_X\|Q_X)=D(P_{X|Y}\|Q_{X|Y}|P_Y)+D(P_Y\|Q_Y)$ (pp. 34–35). The author's reading: it is easier to distinguish two distributions from clean or full data than from noisy or partial data.

**Corollary 2.18.** If $Y=f(X)$, $D(P_Y\|Q_Y)\le D(P_X\|Q_X)$, with equality if $f$ is one-to-one. Equality does not imply one-to-one: take $P_X$ Gaussian, $Q_X$ Laplace, $Y=|X|$. Equality happens precisely when $f(X)$ is a sufficient statistic for testing $P$ against $Q$ (Example 3.9, later) (p. 35).

**Corollary 2.19 (large deviations estimate).** For any $E\subset\mathcal X$: $d(P_X[E]\|Q_X[E])\le D(P_X\|Q_X)$, via $Y=1\{X\in E\}$. It is used later with $E$ highly likely under $P$ and highly unlikely under $Q$ (p. 35).

*Intuition note.* The chain rule splits the divergence of a pair into "what the first variable already reveals" plus "what the second adds". Throwing away information (processing) can only remove distinguishing power, hence DPI. The gap is the conditional divergence of the lost part.

### 2.6* Local behaviour of divergence and Fisher information
KL is in general not continuous (Section 4.5), but for smooth approach one expects $D\to0$ quadratically, since $x\log x$ is smooth and strictly convex at $1$ (p. 36).

**2.6.1 Mixtures.** **Proposition 2.20.** If $D(P\|Q)<\infty$, then $\frac d{d\lambda}\big|_{\lambda=0}D(\lambda P+\bar\lambda Q\|Q)=0$ (one-sided). With arguments exchanged,
$$\frac d{d\lambda}\Big|_{\lambda=0}D(Q\|\lambda P+\bar\lambda Q)=0\iff P\ll Q\tag{2.29}$$
Proof (pp. 36–37):
1. With $f=\frac{dP}{dQ}$: $\frac1\lambda D(\lambda P+\bar\lambda Q\|Q)=\mathbb E_Q[\frac1\lambda(\lambda f+\bar\lambda)\log(\lambda f+\bar\lambda)]$. The function $g(\lambda)=(\lambda f+\bar\lambda)\log(\lambda f+\bar\lambda)$ is convex with $g(0)=0$, so $g(\lambda)/\lambda$ increases in $\lambda$. As $\lambda\to0$ it decreases monotonically to $(f-1)\log e$, and it is bounded above by $f\log f$ (convexity of $x\log x$), which is $Q$-integrable. Monotone convergence gives the limit $\mathbb E_Q[f-1]\log e=0$.
2. (2.29), "$\Rightarrow$" direction (contrapositive): if $P\not\ll Q$, take $E$ with $p=P[E]>0=Q[E]$. DPI with $1_E$ gives $D(Q\|\lambda P+\bar\lambda Q)\ge d(0\|\lambda p)=\log\frac1{1-\lambda p}$, whose derivative is non-zero.
3. "$\Leftarrow$": if $P\ll Q$, $f=\frac{dP}{dQ}$, then $\log\bar\lambda\le\log(\bar\lambda+\lambda f)\le\lambda(f-1)\log e$. For $\lambda<\frac12$, $|\frac1\lambda\log(\bar\lambda+\lambda f)|\le c_1f+c_2$ (absolute constants). Dominated convergence gives $\frac1\lambda D(Q\|\lambda P+\bar\lambda Q)=-\int dQ\frac1\lambda\log(\bar\lambda+\lambda f)\to\int dQ(1-f)=0$.

Remark 2.2 (p. 37): under suitable technical conditions $\frac d{d\lambda}|_{0}D(\lambda P+\bar\lambda Q\|R)=\mathbb E_P[\log\frac{dQ}{dR}]-D(Q\|R)$, and
$\frac d{d\lambda}|_0D(\bar\lambda P_1+\lambda Q_1\|\bar\lambda P_0+\lambda Q_0)=\mathbb E_{Q_1}[\log\frac{dP_1}{dP_0}]-D(P_1\|P_0)+\mathbb E_{P_1}[1-\frac{dQ_0}{dP_0}]\log e$ (Ex. I.22).

So $\lambda\mapsto D(\lambda P+\bar\lambda Q\|Q)$ is $o(\lambda)$, in most cases quadratic. Define $\chi^2(P\|Q)\triangleq\int dQ(\frac{dP}{dQ}-1)^2$. It satisfies $D(P\|Q)\le\log(1+\chi^2(P\|Q))$ (cf. (7.34)) (p. 37).

**Proposition 2.21 (KL is locally $\chi^2$-like).**
$$\liminf_{\lambda\to0}\frac1{\lambda^2}D(\lambda P+\bar\lambda Q\|Q)=\frac{\log e}2\chi^2(P\|Q)\tag{2.30}$$
both sides finite or infinite simultaneously. Proof (p. 38):
1. Assume $\chi^2<\infty$. Write $D(P\|Q)=\mathbb E_Q[g(\frac{dP}{dQ})]$ with $g(x)=x\log x-(x-1)\log e$.
2. $\frac{g(x)}{(x-1)^2\log e}=\int_0^1\frac{s\,ds}{x(1-s)+s}$ is decreasing in $x$, so $0\le g(x)\le(x-1)^2\log e$ and $0\le\frac1{\lambda^2}g(\bar\lambda+\lambda\frac{dP}{dQ})\le(\frac{dP}{dQ}-1)^2\log e$.
3. Dominated convergence: $\lim\frac1{\lambda^2}\mathbb E_Q[g(\bar\lambda+\lambda\frac{dP}{dQ})]=\frac{g''(1)}2\mathbb E_Q[(\frac{dP}{dQ}-1)^2]=\frac{\log e}2\chi^2(P\|Q)$.
4. Unconditionally, Fatou's lemma gives $\liminf\ge\frac{\log e}2\chi^2$ (2.31), so if $\chi^2=\infty$ the left side of (2.30) is also infinite.

**2.6.2 Parametrized family.** Let $\{P_\theta:\theta\in\Theta\}$, $\Theta\subset\mathbb R^d$ open, $P_\theta(dx)=p_\theta(x)\mu(dx)$, $p_\theta(x)$ smooth in $\theta$. The *Fisher information matrix* is
$$J_F(\theta)\triangleq\mathbb E_\theta[VV^\top],\quad V\triangleq\nabla_\theta\ln p_\theta(X)\tag{2.32}$$
($V$ is the *score*) (pp. 38–39). Under regularity conditions:
$$\mathbb E_\theta[V]=0\tag{2.33}$$
and $J_F(\theta)=\mathrm{cov}_\theta(V)=4\int\mu(dx)(\nabla_\theta\sqrt{p_\theta})(\nabla_\theta\sqrt{p_\theta})^\top=-\mathbb E_\theta[\mathrm{Hess}_\theta\ln p_\theta(X)]$; the last follows by differentiating (2.33) in each $\theta_j$ (p. 39).

Under suitable technical conditions,
$$D(P_{\theta_0}\|P_{\theta_0+\xi})=\frac{\log e}2\xi^\top J_F(\theta_0)\xi+o(\|\xi\|^2)\tag{2.34}$$
obtained by integrating the Taylor expansion $\ln p_{\theta_0+\xi}(x)=\ln p_{\theta_0}(x)+\xi^\top\nabla_\theta\ln p_{\theta_0}(x)+\frac12\xi^\top\mathrm{Hess}_\theta(\ln p_{\theta_0}(x))\xi+o(\|\xi\|^2)$. Rigorous proof is deferred to Section 7.11. Slogan: divergence is locally quadratic on parameter space, with Hessian the Fisher information. For the Gaussian location model $P_\theta=\mathcal N(\theta,\Sigma)$, (2.34) is exact with $J_F\equiv\Sigma^{-1}$ (Example 2.2). Prop. 2.21 is a special case with $P_\lambda=\bar\lambda Q+\lambda P$, where the Fisher information at $\lambda=0$ is $\chi^2(P\|Q)$. Prop. 2.21 holds generally, while (2.34) needs regularity (p. 39).

Footnote 2 (p. 39): for a scalar location family $p_\theta(x)=f_0(x-\theta)$, $J_F=\int\frac{(f_0')^2}{f_0}$ is finite even for compactly supported $f_0$ (if $f_0'$ vanishes fast enough at the endpoints), but the left side of (2.34) is infinite for $\xi>0$. A more general reading is $D(P_{\theta_0}\|\frac12P_{\theta_0}+\frac12P_{\theta_0+\xi})=\frac{\xi^2}8J_F(\theta_0)+o(\xi^2)$ (Sec. 7.11).

**Remark 2.3** (pp. 39–40).
- *Reparametrization:* for a smooth invertible $\tilde\Theta\to\Theta$ with Jacobian $A=\frac{d\theta}{d\tilde\theta}$, $J_F(\tilde\theta)=A^\top J_F(\theta)A$ (2.35). $J_F$ thus transforms like a Riemannian metric tensor, giving the Fisher–Rao metric (information geometry).
- *Additivity:* for $n$ iid observations the score is an iid sum, and $J_F^{\otimes n}(\theta)=nJ_F(\theta)$ (2.36).

**Example 2.6 (finite alphabet)** (p. 40). $P_\theta=(\theta_0,\dots,\theta_d)$ on $\{0,\dots,d\}$, free parameter $\theta=(\theta_1,\dots,\theta_d)$, $\theta_0=1-\sum_{i\ge1}\theta_i$. Then
$$J_F(\theta)=\mathrm{diag}\Big(\frac1{\theta_1},\dots,\frac1{\theta_d}\Big)+\frac1{1-\sum_{i=1}^d\theta_i}\mathbf 1\mathbf 1^\top\tag{2.37}$$
($\mathbf 1$ is the $d\times1$ all-ones vector). By the matrix inversion lemma $(A+UCV)^{-1}=A^{-1}-A^{-1}U(C^{-1}+VA^{-1}U)^{-1}VA^{-1}$:
$$J_F^{-1}(\theta)=\mathrm{diag}(\theta)-\theta\theta^\top\tag{2.38}$$
For the determinant, $\det(A+xy^\top)=\det A\cdot\det(I+A^{-1}xy^\top)=\det A\,(1+y^\top A^{-1}x)$, using $\det(I+AB)=\det(I+BA)$. Hence
$$\det J_F(\theta)=\prod_{i=0}^d\frac1{\theta_i}\tag{2.39}$$

**Example 2.7 (location family)** (p. 40). For a density $p_0$ on $\mathbb R^d$, $P_\theta(dx)=p_0(x-\theta)dx$; $J_F(\theta)$ does not depend on $\theta$. For $X\sim p_0$:
$$J(X)\equiv J(p_0)\triangleq\mathbb E[(\nabla\ln p_0(X))(\nabla\ln p_0(X))^\top]=-\mathbb E[\mathrm{Hess}(\ln p_0(X))]\tag{2.40}$$
the second equality requiring integration by parts. This is the sense in which "the Fisher information of a random variable" is meant.

*Intuition note.* Close to $\theta_0$, telling $P_{\theta_0}$ from $P_{\theta_0+\xi}$ is governed by a quadratic form in $\xi$. The Fisher matrix $J_F(\theta_0)$ is the coefficient of that quadratic form: directions $\xi$ with larger $\xi^\top J_F\xi$ give larger divergence.

## Toy example (ours, not from the text)
Alphabet $\{a,b,c\}$, logs base 2. $P=(\tfrac12,\tfrac14,\tfrac14)$, $Q=(\tfrac14,\tfrac14,\tfrac12)$.

- $D(P\|Q)=\tfrac12\log_2\frac{1/2}{1/4}+\tfrac14\log_2\frac{1/4}{1/4}+\tfrac14\log_2\frac{1/4}{1/2}=\tfrac12(1)+0+\tfrac14(-1)=0.25$ bit.
- $D(Q\|P)=\tfrac14\log_2\frac12+\tfrac14\cdot0+\tfrac12\log_22=-0.25+0.5=0.25$. Equal here by coincidence of this symmetric choice; asymmetry is shown after merging below.
- **DPI.** Merge $b,c$ into one symbol (a deterministic map). Then $P'=(\tfrac12,\tfrac12)$, $Q'=(\tfrac14,\tfrac34)$.
 - $D(P'\|Q')=\tfrac12\log_22+\tfrac12\log_2\frac{2}{3}=0.5+0.5(-0.58496)=0.20752$ bit $\le0.25$.
 - Reverse: $D(Q'\|P')=\tfrac14\log_2\frac12+\tfrac34\log_2\frac32=-0.25+0.43872=0.18872\ne0.20752$, which shows asymmetry.
- **Chain-rule gap.** The loss $0.25-0.20752=0.04248$ should equal $P_Y(\{b,c\})\cdot D(P_{X|Y}\|Q_{X|Y})$. Given $\{b,c\}$: $P$ conditional $=(\tfrac12,\tfrac12)$, $Q$ conditional $=(\tfrac13,\tfrac23)$. Then $D=\tfrac12\log_2\frac{3}{2}+\tfrac12\log_2\frac34=0.29248-0.20752=0.08496$, and $\tfrac12\times0.08496=0.04248$ ✓. The gap is positive because the conditionals differ, so merging loses distinguishing information (equality condition of Thm 2.17).

## Concepts
- [[relative entropy / KL divergence]] — $D(P\|Q)=\mathbb E_Q[\frac{dP}{dQ}\log\frac{dP}{dQ}]$ if $P\ll Q$, else $\infty$; equals $\mathbb E_P\log\frac{dP}{dQ}$; asymmetric (pp. 21–22, 25)
- [[cross-entropy]] — $\mathbb E\log\frac1{Q(X)}$ is minimized uniquely by $Q=P_X$, with minimum $H(X)$ (p. 24)
- [[data processing inequality]] — same channel applied to $P_X,Q_X$ cannot increase $D$; equality iff $D(P_{X|Y}\|Q_{X|Y}|P_Y)=0$ (p. 35)
- [[chain rule]] — here the divergence version, $D(P_{X,Y}\|Q_{X,Y})=D(P_{Y|X}\|Q_{Y|X}|P_X)+D(P_X\|Q_X)$ (p. 32)
- [[differential entropy]] — $h(X)=-D(P_X\|\mathrm{Leb})$; can be negative, $\pm\infty$ or undefined (p. 27)
- [[maximum entropy principle]] — Gaussian maximizes $h$ under covariance bound or second-moment bound (Thm 2.8, p. 28)
- [[Fisher information]] — $J_F(\theta)=\mathbb E_\theta[VV^\top]$, the local quadratic coefficient of $D$ (pp. 38–39)
- [[Fisher–Rao metric / information geometry]] — $J_F$ transforms like a metric tensor under reparametrization (p. 40)
- [[f-divergence]] — KL and $\chi^2$ are members; $\chi^2(P\|Q)=\int dQ(\frac{dP}{dQ}-1)^2$ (pp. 20, 37)
- [[noisy channel]] — a Markov kernel $P_{Y|X}$ with input $X$ and output $Y$ (p. 29)
- [[Markov kernel]] (new) — $K(\cdot|x)$ a probability measure for each $x$, measurable in $x$ (p. 29)
- [[Radon–Nikodym derivative]] (new) — density $\frac{dP}{dQ}$ of $P\ll Q$; the likelihood ratio in simple cases (p. 21)
- [[conditional divergence]] (new) — $\mathbb E_{x\sim P_X}D(P_{Y|X=x}\|Q_{Y|X=x})$ (p. 32)
- [[score function]] (new) — $V=\nabla_\theta\ln p_\theta(X)$, mean zero under regularity (p. 39)
- [[tensorization]] (new) — divergence between product measures is the sum of the factors' divergences (p. 33)

## Canonical instances
- [[coin-asymmetry-example]] — fair coin $P$ vs always-heads $Q$: $D(P\|Q)=\infty$, $D(Q\|P)=1$ bit (p. 22)
- [[binary-divergence]] — $d(p\|q)$ and $d(p\|q)\ge2(p-q)^2\log e$ (pp. 22–23)
- [[gaussian-divergence]] — closed forms (2.7)–(2.9), the mean and variance terms (pp. 23–24)
- [[cauchy-gaussian-infinite-divergence]] — $P\ll Q$ yet $D=\infty$ (p. 22)
- [[pathological-sigma-algebra-example]] — Example 2.5: $X\perp Y$ and $X=Y$ simultaneously (pp. 30–31)
- [[gaussian-laplace-abs-sufficiency]] — $Y=|X|$ preserves $D$ without being one-to-one (p. 35)
- [[multinomial-fisher-information]] — Example 2.6, (2.37)–(2.39) (p. 40)
- [[location-family-fisher-information]] — Example 2.7, $J(p_0)$ (p. 40)

## Bridges (candidates)
- [same-math] Corollary 2.4 (expected log-loss minimized by the true distribution) ↔ machine learning: cross-entropy training recovers the data distribution — the author states this link (p. 24).
- [same-math] Fisher information as Hessian of $D$ ↔ statistics: curvature of log-likelihood — the chapter gives $J_F=-\mathbb E[\mathrm{Hess}\ln p_\theta]$ (p. 39).
- [structural-analogy] DPI (processing cannot increase $D$) ↔ hypothesis testing: coarser data makes $P$ and $Q$ harder to tell apart (p. 34).
- [structural-analogy] $J_F$ transforming as $A^\top J_FA$ ↔ differential geometry: Riemannian metric tensor (p. 40).
- [same-math] Concavity of $\log\det$ proved via Gaussian entropy ↔ linear algebra: concavity of $\log\det$ on positive definite matrices (p. 28).

## Questions this raises
- When $D(P_{f(X)}\|Q_{f(X)})=D(P_X\|Q_X)$, exactly when is $f(X)$ sufficient? (promised in Example 3.9.)
- Why is KL not continuous in general (Section 4.5), and how do finite partitions recover it (Theorem 4.5)?
- Does the local quadratic form (2.34) survive without regularity, and what replaces it (Section 7.11)?
- How do the other $f$-divergences (e.g. $\chi^2$) behave under DPI and how do they relate to KL (Chapter 7)?

## Reading notes
- Printed page number = pdf − 25 (pdf 45 = printed 20). The unit id says "ch03", but the chapter's printed heading is "2 Divergence"; section numbers 2.1–2.6 are used here.
- Exercises (I.6, I.8, I.22, I.43, III.11) are only cited, not printed, in these pages, so no exercise list is given.
- Text-layer garbling was resolved from the images: Eq. (2.6) is $p\log\frac pq+\bar p\log\frac{\bar p}{\bar q}$; in Prop. 2.20's proof "$f=\frac{dP}{dQ}$"; in Remark 2.2 and (2.34) $\bar\lambda$ and $\mathrm{Hess}$ were broken in the text layer.
- Possible misprint (my check, not flagged by the author): in (2.9) the image shows a factor $\frac{\log e}2$ on the mean term. Setting $\Sigma_0=\frac{\sigma_0^2}2I_2$ in (2.8) gives $\log e\,\frac{|m_1-m_0|^2}{\sigma_0^2}$ without the $\frac12$, as in the complex-vector formula on p. 24. I copied (2.9) as printed.
- Proposition 2.20 step 2 states that "the derivative is non-zero" without computing it; the toy and the L3 do not add the value.
- The source writes "Not that $\frac{dP}{dQ}$ may not be unique" (p. 21); read "Note".
- Remark 2.2, (2.34) and the Theorem 2.7 proofs are stated or sketched in the source with "suitable technical conditions" or references to other chapters; I did not supply them.
