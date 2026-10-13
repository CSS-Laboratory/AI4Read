---
id: cover-2006-elements/ch09-differential
work: cover-2006-elements
unit: 9 Differential Entropy
pages: 224-238
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Differential Entropy

## L0 — One line
Differential entropy $h(X)=-\int f\log f$ extends entropy to continuous variables: it is the log of the equivalent side length of the smallest set holding most of the probability, so it can be negative and changes under scaling, while relative entropy and mutual information keep their discrete properties.

## L1 — The gist (≤ 120 words)
How can entropy be defined for continuous random variables, and what carries over from the discrete case? The chapter defines $h(X)$ and shows that the AEP gives typical sets whose volume is about $2^{nh}$. Quantizing $X$ into bins of width $\Delta$ gives $H(X^\Delta)\approx h(X)-\log\Delta$. Relative entropy, mutual information and the chain rule keep their discrete properties, and mutual information is a limit of quantized versions. Unlike $H$, $h$ can be negative and changes under scaling. Among all zero-mean distributions with covariance matrix $K$, the normal has maximal entropy; this gives a bound on discrete entropy. Hadamard's inequality follows from $h(X_1,\dots,X_n)\le\sum h(X_i)$ applied to a normal.

**Prerequisites:** discrete entropy, relative entropy and mutual information; weak law of large numbers; Jensen's inequality; multiple integrals and change of variables; covariance matrix, determinant, trace.

## L2 — Key ideas (5–10 bullets)
- $h(X)=-\int_S f\log f\,dx$ depends only on the density, and unlike discrete entropy it can be negative (uniform on $[0,a]$ gives $\log a$) (pp. 224–225).
- Normal: $h=\tfrac12\log 2\pi e\sigma^2$ bits; multivariate normal: $\tfrac12\log(2\pi e)^n|K|$ (pp. 225, 230–231).
- The AEP holds for densities. The typical set has probability $>1-\epsilon$ and volume between $(1-\epsilon)2^{n(h-\epsilon)}$ and $2^{n(h+\epsilon)}$; it is the smallest set of probability $\ge 1-\epsilon$ to first order in the exponent (pp. 226–227).
- So $2^h$ is the side length of the smallest set holding most of the probability: low $h$ means concentrated, high $h$ means dispersed (p. 227).
- Quantizing with bin width $\Delta$: $H(X^\Delta)+\log\Delta\to h(X)$. An $n$-bit quantization has entropy about $h(X)+n$ (pp. 228–229).
- $D(f\|g)\ge0$ and $I(X;Y)\ge0$, with equality iff $f=g$ a.e. and iff independence respectively. $I$ is the limit of quantized mutual information, because the $\log\Delta$ terms cancel (pp. 231–232).
- $h$ is translation invariant and $h(AX)=h(X)+\log|A|$ (determinant of $A$) (pp. 233–234).
- Normal maximizes $h$ for given covariance; Hadamard's inequality follows from the chain-rule corollary (pp. 233–234).
- $H(p_1,p_2,\dots)\le\tfrac12\log\!\big(2\pi e(\mathrm{Var}(X_0)+\tfrac1{12})\big)$ for the integer-valued $X_0$ with $\Pr(X_0=i)=p_i$ (p. 235).

## L3 — Walkthrough

### 9.1 Definitions
- $X$ is *continuous* if its CDF $F(x)=\Pr(X\le x)$ is continuous. The density is $f=F'$ where it exists and integrates to 1. The *support set* $S$ is where $f>0$ (p. 224).
- **Definition.** $h(X)=-\int_S f(x)\log f(x)\,dx$ \tag{9.1}. It depends only on $f$, so it is also written $h(f)$ (p. 224).
- Remark: the density or the integral may fail to exist; read every result as "if it exists" (p. 225).
- **Example 9.1.1 (uniform on $[0,a]$).** $h(X)=-\int_0^a \tfrac1a\log\tfrac1a\,dx=\log a$ \tag{9.2}. For $a<1$ this is negative, so differential entropy can be negative. Still, $2^{h(X)}=a$ is the volume of the support, which is non-negative (p. 225).
- **Example 9.1.2 (normal, in nats).** For $\phi(x)=\frac1{\sqrt{2\pi\sigma^2}}e^{-x^2/2\sigma^2}$ (p. 225):
$$h(\phi)=-\int\phi\ln\phi \tag{9.3}$$
$$=-\int\phi(x)\Big[-\frac{x^2}{2\sigma^2}-\ln\sqrt{2\pi\sigma^2}\Big]\tag{9.4}$$
$$=\frac{EX^2}{2\sigma^2}+\frac12\ln2\pi\sigma^2\tag{9.5}$$
$$=\frac12+\frac12\ln2\pi\sigma^2=\frac12\ln e+\frac12\ln2\pi\sigma^2\tag{9.6–9.7}$$
$$=\frac12\ln2\pi e\sigma^2\ \text{nats},\qquad h(\phi)=\frac12\log2\pi e\sigma^2\ \text{bits}\tag{9.8–9.9}$$
(Step 9.6 uses $EX^2=\sigma^2$, since the mean is 0.)

### 9.2 The AEP for continuous random variables
- **Theorem 9.2.1.** For $X_1,\dots,X_n$ i.i.d. with density $f$: $-\frac1n\log f(X_1,\dots,X_n)\to E[-\log f(X)]=h(X)$ in probability \tag{9.10}. Proof: weak law of large numbers (p. 226).
- **Typical set:** $A_\epsilon^{(n)}=\{(x_1,\dots,x_n)\in S^n:\ |-\frac1n\log f(x_1,\dots,x_n)-h(X)|\le\epsilon\}$, with $f(x_1,\dots,x_n)=\prod_i f(x_i)$ \tag{9.11}. The role of cardinality is played by the volume $\mathrm{Vol}(A)=\int_A dx_1\cdots dx_n$ \tag{9.12} (p. 226).
- **Theorem 9.2.2.** (1) $\Pr(A_\epsilon^{(n)})>1-\epsilon$ for $n$ large. (2) $\mathrm{Vol}(A_\epsilon^{(n)})\le2^{n(h(X)+\epsilon)}$ for all $n$. (3) $\mathrm{Vol}(A_\epsilon^{(n)})\ge(1-\epsilon)2^{n(h(X)-\epsilon)}$ for $n$ large (p. 226).
- Proof of (1): Theorem 9.2.1. Proof of (2): on $A_\epsilon^{(n)}$, $f\ge2^{-n(h+\epsilon)}$, so
$$1=\int_{S^n}f\ \ge\int_{A_\epsilon^{(n)}}f\ \ge\int_{A_\epsilon^{(n)}}2^{-n(h+\epsilon)}dx=2^{-n(h+\epsilon)}\mathrm{Vol}(A_\epsilon^{(n)})\tag{9.13–9.17}$$
Proof of (3): for $n$ large enough that (1) holds, and using $f\le2^{-n(h-\epsilon)}$ on $A_\epsilon^{(n)}$,
$$1-\epsilon\le\int_{A_\epsilon^{(n)}}f\le2^{-n(h-\epsilon)}\mathrm{Vol}(A_\epsilon^{(n)})\tag{9.18–9.21}$$
Together: $(1-\epsilon)2^{n(h-\epsilon)}\le\mathrm{Vol}(A_\epsilon^{(n)})\le2^{n(h+\epsilon)}$ \tag{9.22} (p. 227).
- **Theorem 9.2.3.** $A_\epsilon^{(n)}$ is the smallest-volume set with probability $\ge1-\epsilon$, to first order in the exponent. Proof: same as the discrete case (p. 227).
- **Intuition note:** the smallest set holding most of the probability has volume about $2^{nh}$, so its side length is $(2^{nh})^{1/n}=2^h$. Low $h$ means the variable sits in a small effective volume; high $h$ means it is spread out (p. 227).
- Note: Fisher information is related to the surface area of the typical set (more in Section 16.7) (pp. 227–228).

### 9.3 Relation to discrete entropy
- Cut the range into bins of length $\Delta$, with $f$ continuous inside bins. By the mean value theorem there is $x_i$ in bin $i$ with $f(x_i)\Delta=\int_{i\Delta}^{(i+1)\Delta}f$ \tag{9.23}. Define $X^\Delta=x_i$ if $i\Delta\le X<(i+1)\Delta$ \tag{9.24}. Then $p_i=f(x_i)\Delta$ \tag{9.25} (p. 228).
- $H(X^\Delta)=-\sum p_i\log p_i=-\sum\Delta f(x_i)\log f(x_i)-\sum f(x_i)\Delta\log\Delta=-\sum\Delta f(x_i)\log f(x_i)-\log\Delta$ \tag{9.26–9.29}, because $\sum f(x_i)\Delta=\int f=1$ (pp. 228–229).
- **Theorem 9.3.1.** If $f$ is Riemann integrable, $H(X^\Delta)+\log\Delta\to h(f)=h(X)$ as $\Delta\to0$ \tag{9.30}. The first sum tends to $-\int f\log f$ by Riemann integrability. Hence an $n$-bit quantization has entropy about $h(X)+n$ (p. 229).
- **Intuition note:** $h$ is the entropy left after subtracting the "resolution cost" $-\log\Delta$ of the grid. This is why $h$ can be negative and why its value depends on the units chosen.
- **Examples (p. 229).** (1) Uniform on $[0,1]$, $\Delta=2^{-n}$: $h=0$, $H(X^\Delta)=n$. (2) Uniform on $[0,\tfrac18]$: the first 3 bits after the point are 0, so $n-3$ bits suffice, matching $h=-3$. In general $h(X)+n$ is the *average* number of bits for $n$-bit accuracy. A discrete variable can be regarded as having $h=-\infty$, consistent with $2^{-\infty}=0$ (zero support volume) (p. 229).

### 9.4 Joint and conditional differential entropy
- $h(X_1,\dots,X_n)=-\int f\log f\,dx_1\cdots dx_n$ \tag{9.31}. $h(X|Y)=-\int f(x,y)\log f(x|y)\,dx\,dy$ \tag{9.32}, and $h(X|Y)=h(X,Y)-h(Y)$ \tag{9.33}; care is needed if any entropy is infinite (p. 230).
- **Theorem 9.4.1.** For $X\sim\mathcal N_n(\mu,K)$: $h=\tfrac12\log(2\pi e)^n|K|$ bits \tag{9.34}, $|K|$ the determinant (p. 230).
- Proof. Density $f(\mathbf x)=\frac{1}{(\sqrt{2\pi})^n|K|^{1/2}}e^{-\frac12(\mathbf x-\mu)^TK^{-1}(\mathbf x-\mu)}$ \tag{9.35}. Then (pp. 230–231):
$$h(f)=\tfrac12E\Big[\sum_{i,j}(x_i-\mu_i)(K^{-1})_{ij}(x_j-\mu_j)\Big]+\tfrac12\ln(2\pi)^n|K|\tag{9.36–9.38}$$
$$=\tfrac12\sum_{i,j}E[(x_j-\mu_j)(x_i-\mu_i)](K^{-1})_{ij}+\tfrac12\ln(2\pi)^n|K|=\tfrac12\sum_j\sum_iK_{ji}(K^{-1})_{ij}+\cdots\tag{9.39–9.40}$$
$$=\tfrac12\sum_j(KK^{-1})_{jj}+\cdots=\tfrac12\sum_jI_{jj}+\cdots=\tfrac n2+\tfrac12\ln(2\pi)^n|K|\tag{9.41–9.43}$$
$$=\tfrac12\ln(2\pi e)^n|K|\ \text{nats}=\tfrac12\log(2\pi e)^n|K|\ \text{bits}\tag{9.44–9.45}$$

### 9.5 Relative entropy and mutual information
- $D(f\|g)=\int f\log\frac fg$ \tag{9.46}. It is finite only if the support of $f$ lies in the support of $g$ (with $0\log\frac00=0$). $I(X;Y)=\int f(x,y)\log\frac{f(x,y)}{f(x)f(y)}dx\,dy$ \tag{9.47}. Hence $I(X;Y)=h(X)-h(X|Y)=h(Y)-h(Y|X)$ \tag{9.48} and $I(X;Y)=D(f(x,y)\|f(x)f(y))$ \tag{9.49} (p. 231).
- Their properties are the same as in the discrete case. $I$ is the limit of quantized mutual information:
$$I(X^\Delta;Y^\Delta)=H(X^\Delta)-H(X^\Delta|Y^\Delta)\approx h(X)-\log\Delta-(h(X|Y)-\log\Delta)=I(X;Y)\tag{9.50–9.52}$$
The $\log\Delta$ terms cancel (p. 231). Some authors (Gallager) define $I$ directly as this limit and skip differential entropy (p. 232).

### 9.6 Properties
- **Theorem 9.6.1.** $D(f\|g)\ge0$, with equality iff $f=g$ a.e. \tag{9.53}. Proof, with $S$ the support of $f$: $-D=\int_Sf\log\frac gf\le\log\int_Sf\frac gf=\log\int_Sg\le\log1=0$ \tag{9.54–9.57}; the first step is Jensen's inequality, and equality in it holds iff $f=g$ a.e. (p. 232).
- Corollaries: $I(X;Y)\ge0$, with equality iff $X,Y$ independent; $h(X|Y)\le h(X)$, with equality iff independent (p. 232).
- **Theorem 9.6.2 (chain rule).** $h(X_1,\dots,X_n)=\sum_ih(X_i|X_1,\dots,X_{i-1})$ \tag{9.58}, from the definitions. Corollary: $h(X_1,\dots,X_n)\le\sum h(X_i)$, with equality iff independent \tag{9.59} (p. 232).
- **Application (Hadamard).** For $X\sim\mathcal N(0,K)$, substituting the entropies into (9.59) gives $|K|\le\prod_iK_{ii}$ \tag{9.60}. Further determinant inequalities can be derived this way (Chapter 16) (p. 233).
- **Theorem 9.6.3.** $h(X+c)=h(X)$ \tag{9.61}.
- **Theorem 9.6.4.** $h(aX)=h(X)+\log|a|$ \tag{9.62}. Proof: for $Y=aX$, $f_Y(y)=\frac1{|a|}f_X(y/a)$, and
$$h(aX)=-\int\tfrac1{|a|}f_X(\tfrac ya)\log\big(\tfrac1{|a|}f_X(\tfrac ya)\big)dy=-\int f_X(x)\log f_X(x)+\log|a|\tag{9.63–9.66}$$
by change of variables (p. 233). Vector corollary: $h(A\mathbf X)=h(\mathbf X)+\log|A|$, with $|A|$ the absolute value of the determinant \tag{9.67} (p. 234).
- **Theorem 9.6.5.** For $\mathbf X\in\mathbb R^n$ with zero mean and covariance $K=E\mathbf X\mathbf X^t$: $h(\mathbf X)\le\tfrac12\log(2\pi e)^n|K|$, with equality iff $\mathbf X\sim\mathcal N(0,K)$ (p. 234).
- Proof. Let $g$ be any density with $\int g\,x_ix_j=K_{ij}$, and $\phi_K$ the $\mathcal N(0,K)$ density. Then
$$0\le D(g\|\phi_K)=\int g\log(g/\phi_K)=-h(g)-\int g\log\phi_K=-h(g)-\int\phi_K\log\phi_K=-h(g)+h(\phi_K)\tag{9.68–9.72}$$
The substitution holds because $\log\phi_K$ is a quadratic form and $g,\phi_K$ have the same second moments (p. 234). (Added step: equality iff $g=\phi_K$ a.e., by Theorem 9.6.1.)
- **Intuition note:** with the spread (covariance) fixed, the normal is the most "uncertain" density. Any other density with the same covariance has a smaller effective volume.

### 9.7 Differential entropy bound on discrete entropy
- A discrete variable can have tiny variance and large entropy, so the bound uses an integer-valued variable with the same probabilities (p. 234).
- **Theorem 9.7.1.** For $\Pr(X=a_i)=p_i$:
$$H(p_1,p_2,\dots)\le\tfrac12\log\Big(2\pi e\Big(\sum_ip_ii^2-\big(\sum_iip_i\big)^2+\tfrac1{12}\Big)\Big)\tag{9.74}$$
and the same holds with $p_i$ replaced by $p_{\sigma(i)}$ for every permutation $\sigma$ \tag{9.75} (p. 235).
- Proof. Let $X_0$ be integer-valued with $\Pr(X_0=i)=p_i$ \tag{9.76}; let $U$ be uniform on $[0,1]$, independent of $X_0$; set $\tilde X=X_0+U$ \tag{9.77}. Its density is $p_i$ on $[i,i+1)$ (Fig. 9.2). Then $H(X)=H(X_0)$ (only probabilities matter), and
$$H(X_0)=-\sum p_i\log p_i=-\sum_i\Big(\int_i^{i+1}f_{\tilde X}\Big)\log\Big(\int_i^{i+1}f_{\tilde X}\Big)=-\int f_{\tilde X}\log f_{\tilde X}=h(\tilde X)\tag{9.78–9.82}$$
Then (pp. 235–236)
$$H(X)=H(X_0)=h(\tilde X)\le\tfrac12\log(2\pi e)\mathrm{Var}(\tilde X)=\tfrac12\log(2\pi e)(\mathrm{Var}(X_0)+\mathrm{Var}(U))\tag{9.83–9.86}$$
and $\mathrm{Var}(X_0)=\sum p_ii^2-(\sum ip_i)^2$ with $\mathrm{Var}(U)=\tfrac1{12}$ (added step: variance of uniform on $[0,1]$) gives (9.74) \tag{9.87}.
- Permuting the $p_i$ leaves $H$ unchanged, so the bound may be minimized over orderings. **Authors' conjecture:** a good bound comes when the large probabilities are adjacent, as in $\dots,p_5,p_3,p_1,p_2,p_4,\dots$ for $p_1\ge p_2\ge\cdots$ (p. 236).
- **Example.** Bernoulli($\tfrac12$): $H=1$; $\mathrm{Var}(X_0)=\tfrac14$, so $H\le\tfrac12\log(2\pi e(\tfrac14+\tfrac1{12}))=1.255$ bits \tag{9.88} (p. 236).

### Summary and problems (pp. 236–238)
- The summary restates (9.89)–(9.100) and adds: $2^{H(X)}$ is the effective alphabet size (discrete), $2^{h(X)}$ the effective support-set size (continuous), and $2^C$ the effective alphabet size of a channel of capacity $C$ (p. 237).
- Historical notes: Shannon's paper introduced differential entropy; Kolmogorov and Pinsker gave the rigorous general definitions, with $I$ as a supremum over finite partitions; the bound of 9.7 is credited to Massey and Willems (unpublished) (p. 238).

## Toy example (ours)
Let $X$ be uniform on $[0,\tfrac14]$, so $f=4$ there.
- $h(X)=-\int_0^{1/4}4\log4\,dx=-\log4=-2$ bits.
- Quantize with $\Delta=2^{-5}=\tfrac1{32}$. The interval holds $\tfrac14\div\tfrac1{32}=8$ bins, each with $p=4\cdot\tfrac1{32}=\tfrac18$. So $H(X^\Delta)=8\cdot\tfrac18\log8=3$ bits.
- Check of Theorem 9.3.1: $h-\log\Delta=-2-(-5)=3$. ✓ (here it is exact because $f$ is constant).
- Scaling check: $Y=4X$ is uniform on $[0,1]$, so $h(Y)=0=h(X)+\log4=-2+2$. ✓
- Interpretation: $2^{-2}=\tfrac14$ is the support volume. Describing $X$ to 5-bit accuracy needs $5-2=3$ bits.

## Concepts
- [[differential-entropy]] — $h(X)=-\int_Sf\log f$; can be negative; log of the effective side length of the smallest set holding most of the probability (pp. 224, 227)
- [[typical-set-aep]] — continuous AEP: $-\frac1n\log f(X^n)\to h$; typical set has volume about $2^{nh}$ (p. 226)
- [[relative-entropy-kl-divergence]] — $D(f\|g)=\int f\log(f/g)\ge0$ (p. 231)
- [[mutual-information]] — $I(X;Y)=D(f(x,y)\|f(x)f(y))$; limit of quantized versions (p. 231)
- [[chain-rule]] — $h(X_1..X_n)=\sum h(X_i|X_{<i})$ (p. 232)
- [[maximum-entropy-principle]] — normal maximizes $h$ for given covariance (p. 234)
- [[fisher-information]] — only mentioned: related to surface area of typical set (p. 227)
- [[quantization-entropy]] (new) — $H(X^\Delta)\approx h(X)-\log\Delta$ (p. 229)
- [[hadamard-inequality]] (new) — $|K|\le\prod K_{ii}$, derived from $h$ subadditivity for normals (p. 233)
- [[effective-support-size]] (new) — $2^{h(X)}$, the effective support-set size (p. 237)

## Canonical instances
- [[uniform-distribution]] — $h=\log a$, negative for $a<1$ (p. 225)
- [[normal-distribution]] — $h=\tfrac12\log2\pi e\sigma^2$; entropy maximizer (pp. 225, 234)
- [[bernoulli-half-bound]] — $H=1$ vs bound 1.255 bits (p. 236)

## Bridges (candidates)
- [same-math] Hadamard's inequality ↔ linear algebra: $|K|\le\prod K_{ii}$ for covariance matrices, from $h(X_1..X_n)\le\sum h(X_i)$ (p. 233).
- [structural-analogy] $2^{h}$ as effective volume ↔ discrete $2^H$ as effective alphabet size (p. 237).
- [structural-analogy] Quantization cost $-\log\Delta$ ↔ measurement resolution in applied statistics.

## Questions this raises
- Since $h$ depends on units, which quantities (e.g. $D$, $I$) are safe to compare across coordinate systems?
- How tight is the bound in 9.7 for other distributions, and does the conjectured ordering minimize it?
- How does the normal-maximizes-$h$ result enter channel capacity with Gaussian noise (the unit's summary refers to capacity)?
- What is the exact link between Fisher information and the surface area of the typical set (Section 16.7)?

## Exercises worth doing
- Ex. 1 (p. 237) — compute $h$ for exponential, Laplace, and sum of independent normals — difficulty: easy
- Ex. 3 (p. 238) — mutual information of correlated normals for $\rho=1,0,-1$ — difficulty: medium
- Ex. 5 (p. 238) — bits to describe radium decay time to 3-digit accuracy, using quantization — difficulty: medium
- Ex. 6 (p. 238) — prove $h(A\mathbf X)=\log|\det A|+h(\mathbf X)$ — difficulty: medium
- Ex. 4 (p. 238) — uniform input plus uniform noise: $I(X;Y)$ and peak-limited capacity — difficulty: hard
- Ex. 2 (p. 237) — Ky Fan determinant concavity via the entropy hint — difficulty: hard

## Reading notes
- The PDF is the 1991 first edition (Wiley copyright line on p. 224), not the 2006 second edition; numbering and content may differ from the 2nd edition.
- Printed page = pdf − 22.
- The text layer is heavily garbled in equations; all math was checked against the page images.
- In (9.65) the image omits the $dx$ and the grouping of the final $+\log|a|$ term is loosely typeset; (9.66) states the result.
- Theorem 9.6.5 states the equality case, but its proof does not spell it out; I marked my added step.
