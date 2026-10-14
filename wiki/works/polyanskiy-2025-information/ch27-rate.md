---
id: polyanskiy-2025-information/ch27-rate
work: polyanskiy-2025-information
unit: "Chapter 24 (printed numbering). Rate-distortion theory (§§24.1–24.4)"
pages: 477–489
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Rate-distortion theory (quantization, the general converse, single-letterization)

## L0 — One line
Any lossy compressor with $M$ codewords and average distortion $\le D$ must satisfy $\log M \ge \inf I(X;Y)$ over channels meeting the distortion constraint, and for an iid source this bound is a single-letter quantity.

## L1 — The gist (≤ 120 words)
How well can a continuous source be described with few bits? The unit first covers classical low-dimensional quantization: the uniform quantizer, the 6 dB-per-bit rule, Lloyd's algorithm, and the Panter–Dite high-rate asymptotics. It then moves to high dimension with fixed rate. There, quantizing iid coordinates jointly beats quantizing each one alone. The unit defines $(n,M,D)$-codes and proves a general converse, $\log M\ge\phi_X(D)$. It defines the information rate-distortion function $R^{(I)}(D)$, which lower-bounds the operational $R(D)$, and single-letterizes it for iid sources. A last section turns an excess-distortion code into an average-distortion code.

**Prerequisites:** mutual information and its convexity and super-additivity; differential entropy; Hölder and Jensen inequalities; Markov chains; basic probability.

## L2 — Key ideas
- At high rate a uniform scalar quantizer has $D_U(R)\approx \frac{A^2}{12}2^{-2R}$, which gives about 6.02 dB of signal-to-noise ratio (SNR) per bit. The rule is valid only at high rate (p. 478).
- Lloyd's algorithm alternates two steps: a Voronoi partition (each cell is the set of points closest to one reconstruction point) and a centroid update (each point moves to the mean of the source inside its cell). It converges to a centroidal Voronoi tessellation (CVT), but may stop at a non-global optimum (p. 481).
- With a point density $\lambda$ and $N=2^R$, the optimal high-rate density is $\propto p^{1/3}$. This gives $D_{scalar}(R)\approx\frac1{12}2^{-2R}(\int p^{1/3})^3$ (p. 482).
- Under an entropy constraint, uniform quantization is asymptotically optimal. For iid sources, even optimal vector quantizers (which quantize several coordinates jointly) can gain at most 1.53 dB over it (p. 483).
- Even for iid sources, joint quantization in high dimension beats scalar quantization. Gaussian: $\sigma^2 2^{-2R}$ vs. about $\sigma^2 2^{-2R}\pi\sqrt3/2$ (p. 484).
- General converse: $\log M\ge\phi_X(D)=\inf_{P_{Y|X}:\mathbb E d\le D} I(X;Y)$, so $R(D)\ge R^{(I)}(D)$ (pp. 485–487).
- For a stationary memoryless source with separable distortion, $\phi_{S^n}(D)=n\phi_S(D)$, so $R^{(I)}(D)=\phi_S(D)$ (p. 487).
- An excess-distortion code (one with $\mathbb P[d>D]\le\epsilon$) can be turned into an average-distortion code by adding one codeword, at a cost controlled by $D_p\epsilon^{1-1/p}$ (p. 488).

## L3 — Walkthrough

### 24.1 Scalar and vector quantization (p. 477)
This section studies low-dimensional, high-rate quantization, "pre-Shannon". The next sections move to high dimension at fixed rate.

**24.1.1 Scalar uniform quantization (pp. 477–479).** Pulse-coded modulation (PCM) was patented by Reeves. His argument: digital signals can travel long routes without accumulating noise (p. 477). For $X\in[-A/2,A/2]$, $q_U$ uses $N$ equally spaced points $\{-\tfrac A2+\tfrac{kA}{N},\,k=0,\dots,N-1\}$ (p. 478). Quality is the mean squared error $D(N)=\mathbb E|X-q_U(X)|^2$, with $R=\log_2N$. In the high-rate regime ($R\gg1$) and with a smooth density, each interval $\Delta_j$ is nearly flat. Conditionally on $\Delta_j$, $X$ is therefore approximately uniform (p. 478). With $c_j$ the $j$-th point:
$$D_U(R)=\sum_{j=1}^N\mathbb E[|X-c_j|^2\mid X\in\Delta_j]\,\mathbb P[X\in\Delta_j]\tag{24.1}$$
$$\approx\sum_{j=1}^N\frac{|\Delta_j|^2}{12}\mathbb P[X\in\Delta_j]\tag{24.2}$$
$$=\frac{(A/N)^2}{12}=\frac{A^2}{12}2^{-2R}\tag{24.3}$$
using that $\mathrm{Var}\,\mathrm{Unif}(-a,a)=a^2/3$ (p. 478). Then
$$10\log_{10}\mathrm{SNR}=10\log_{10}\frac{\mathrm{Var}(X)}{\mathbb E|X-q_U(X)|^2}=10\log_{10}\frac{12\mathrm{Var}(X)}{A^2}+(20\log_{10}2)R=\text{const}+(6.02\,\text{dB})R.$$
The constant is 0 for $X$ uniform on $[-A/2,A/2]$. The "6 dB per bit" rule holds only at high rate, so claims like "16-bit PCM gives 96 dB" need caution (p. 478). For unbounded $X$, error has two parts: granular distortion and overload distortion (saturating large values) (pp. 478–479).

*Intuition note:* when intervals are tiny, the error inside each is that of a uniform variable on a short interval. One extra bit halves the interval width and cuts the error power by 4, which is 6 dB.

**24.1.2 Non-uniform quantization (pp. 479–480).** Place more points where $p_X$ is large. A *compander* (compressor + expander) $f$ implements this: $q(X)=f^{-1}(q_U(f(X)))$ (24.4). Taking $f$ = CDF of $X$ is one choice. The compander architecture is optimal at high rate, but the optimal $f$ is not the CDF (p. 479). A popular choice is the $\mu$-companding function $f(X)=\mathrm{sign}(X)\frac{\ln(1+\mu|X|)}{\ln(1+\mu)}$. The text motivates it by the logarithmic response of the human ear and by approximately Laplace natural signals, such as differences of consecutive speech samples (pp. 479–480). It gives the $\mu$-law (US); Europe uses the A-law (p. 480).

**24.1.3 Optimal quantizers (pp. 480–481).** $D_{scalar}(R)=\min_{q:|\mathrm{Im}\,q|\le2^R}\mathbb E|X-q(X)|^2$ (24.5). Intuitively the optimal regions are contiguous, so scalar quantizers are piecewise constant (p. 480).
*Example 24.1:* one-bit quantization of $X\sim\mathcal N(0,\sigma^2)$. Optimal points are $c_{1,2}=\pm\mathbb E|X|=\pm\sqrt{2/\pi}\,\sigma$. The error is $\mathrm{Var}(|X|)=(1-\tfrac2\pi)\sigma^2$ (p. 480).
*Lloyd's algorithm* (1957, unpublished until 1982): start from $N=2^k$ points and iterate (p. 480). (1) Draw the Voronoi regions (points closest to each $c_j$). (2) Move each point to the centroid $\mathbb E[X|X\in D]$ of its region. Fixed points are Centroidal Voronoi Tessellations (CVT) (p. 481).

**Theorem 24.1 (Lloyd).** (1) The algorithm always converges to a CVT. (2) The optimal quantizer is always a CVT. (3) CVTs need not be unique, and the algorithm may converge to non-global optima (p. 481).
*Remark 24.1:* log-concavity of the density of $X$ (e.g. Gaussian) is sufficient for a unique CVT. Even for Gaussian $P_X$ and $N>3$ the optimal points are not known in closed form (p. 481).
*Remark 24.2:* $k$-means minimizes $\sum_{i=1}^n\min_{j\in[k]}\|x_i-\mu_j\|^2$. This equals optimal vector quantization of the empirical distribution. It is NP-hard in the worst case, and Lloyd's algorithm is a common heuristic (p. 481).

**24.1.4 Fine quantization (pp. 481–483).** Following Panter–Dite, let $\lambda(x)$ be the density of quantization points. About $N\int_a^b\lambda$ points lie in $[a,b]$. The cell size $\Delta(x)$ satisfies $N\int_x^{x+\Delta(x)}\lambda\approx N\lambda(x)\Delta(x)\approx1$, so $\Delta(x)\approx\frac1{N\lambda(x)}$ (p. 482). Then
$$\mathbb E|X-q(X)|^2\approx\sum_j\mathbb P[X\in\Delta_j]\frac{|\Delta_j|^2}{12}\approx\int p(x)\frac{\Delta^2(x)}{12}dx=\frac1{12N^2}\int p(x)\lambda^{-2}(x)dx.$$
Hölder gives $\int p^{1/3}\le(\int p\lambda^{-2})^{1/3}(\int\lambda)^{2/3}$, so $\int p\lambda^{-2}\ge(\int p^{1/3})^3$. Equality holds iff $p\lambda^{-2}\propto\lambda$. Hence $\lambda^*=p^{1/3}/\int p^{1/3}$. For $N=2^R$:
$$D_{scalar}(R)\approx\frac1{12}2^{-2R}\Big(\int p^{1/3}(x)dx\Big)^3$$
(Panter–Dite approximation; footnote 4: "≈" can be replaced by "$=1+o(1)$" as $R\to\infty$, by Zador) (p. 482).
- For $X\in[-A/2,A/2]$, Hölder gives $\langle1,p^{1/3}\rangle\le\|1\|_{3/2}\|p^{1/3}\|_3=A^{2/3}$. So $D_{scalar}(R)\le\frac1{12}2^{-2R}A^2=D_U(R)$, with strict improvement unless the source is uniform (p. 482).
- For $X\sim\mathcal N(0,\sigma^2)$: $D_{scalar}(R)\approx\sigma^22^{-2R}\frac{\pi\sqrt3}{2}$ (24.6) (p. 482).

*Remark 24.3:* in the scalar case the optimal non-uniform quantizer can be realized by the compander (24.4). The text leaves the Taylor-expansion analysis as an exercise. The optimal compander is $f(x)=\int_{-\infty}^xp^{1/3}/\int_{-\infty}^\infty p^{1/3}$ (pp. 482–483).

*Intuition note:* cells should be small where the density is high, but not in proportion to the density. The cube root balances the number of points against the probability mass per cell.

**24.1.5 Fine quantization and variable rate (p. 483).** If the output is further compressed losslessly, a natural constraint is $H(q(X))$. Koshelev (1963): at high rate uniform quantization is asymptotically optimal under the entropy constraint. For a uniform quantizer with cell size $\Delta$, under appropriate assumptions
$$H(q_\Delta(X))=h(X)-\log\Delta+o(1),\tag{24.7}$$
with $h$ the differential entropy. If $H(q(X))=R$, then $D=\Delta^2/12\approx2^{-2R}\frac{2^{2h(X)}}{12}$. For a general quantizer with unnormalized point density $\Lambda$ ($\int_{-\infty}^{c_j}\Lambda=j$, $\Lambda\to\infty$ pointwise): $D\approx\frac1{12}\int p_X\Lambda^{-2}$ and $H(q(X))\approx\int p_X\log\frac{\Lambda}{p_X}$. Jensen's inequality gives
$$\frac1{12}\int p_X\frac1{\Lambda^2}\ge\frac1{12}\exp\Big\{-2\int p_X\log\Lambda\Big\}\approx2^{-2H(q(X))}\frac{2^{2h(X)}}{12}.$$
So the uniform quantizer is asymptotically optimal. Even optimal vector quantizers cannot beat $2^{-2R}\frac{2^{2h(X)}}{2\pi e}$, so for any iid source the maximal gain is 1.53 dB (0.255 bit/sample). This is one reason scalar uniform quantization followed by lossless compression is so popular (p. 483).

### 24.2 Information-theoretic formulation (pp. 483–485)
**Hamming game.** Given 100 unbiased bits and room for 50 bits, we later guess the originals. Storing half and guessing the rest gives 25% bit error rate (BER). The optimal strategy achieves 11% BER (Theorem 26.1, not proved here) (p. 484).
**Gaussian example.** For iid $\mathcal N(0,\sigma^2)$ at one bit per symbol, scalar quantization gives $(1-\frac2\pi)\sigma^2\approx0.36\sigma^2$. A scheme with MSE $\sigma^2/4$ per coordinate exists for large $n$ and is optimal (Theorem 26.2). At rate $R$, joint quantization gives $D_{vec}(R)=\sigma^22^{-2R}$, a gain of 4.35 dB (0.72 bit/sample) over (24.6) (p. 484).
Two intuitive explanations (p. 484): (1) componentwise quantization gives hypercube regions, which may not be good for covering in high dimension. (2) By concentration of measure, $(X_1,\dots,X_n)$ concentrates near a sphere, so large parts of $\mathbb R^n$ can be ignored.

*Intuition note:* even for independent coordinates, coding them together exploits the fact that the vector is almost always "typical". Separate coding must prepare for every coordinate being unusual at once.

**Formulation.** A lossy compressor is a pair $(f,g)$ forming $X\xrightarrow{f}W\xrightarrow{g}\hat X$, with $W$ discrete and $\hat X$ in an alphabet possibly different from $\mathcal X$. A distortion metric is a measurable $d:\mathcal X\times\hat{\mathcal X}\to\mathbb R\cup\{+\infty\}$ (p. 484). Formulations (p. 485): (1) fixed length, average distortion: $W\in[M]$, minimize $\mathbb E d$; (2) fixed length, excess distortion: minimize $\mathbb P[d>D]$; (3) variable length, max distortion: $d\le D$ a.s., minimize $\mathbb E\,l(W)$ or $H(W)$. The book focuses on (1). Under mild assumptions (1) and (2) have the same asymptotic limit (cf. Remark 25.2). The text says one version converges as $O(1/\sqrt n)$ with a rich dispersion theory, and another "much faster" as $O(\log n/n)$ (Ex. V.3); both are labelled "excess" in print (see Reading notes) (p. 485). Separable distortion:
$$d(s^n,\hat s^n)\triangleq\frac1n\sum_{i=1}^nd(s_i,\hat s_i).\tag{24.8}$$
**Definition 24.2.** An $(n,M,D)$-code is $f:\mathcal A^n\to[M]$, $g:[M]\to\hat{\mathcal A}^n$ with $\mathbb E[d(S^n,g(f(S^n)))]\le D$.
$$M^*(n,D)=\min\{M:\exists(n,M,D)\text{-code}\}\tag{24.9}$$
$$R(D)=\limsup_{n\to\infty}\tfrac1n\log M^*(n,D)\tag{24.10}$$
For iid sources the limit exists and equals the infimum over blocklengths (Ex. V.2) (p. 485).

### 24.3 Converse bounds (pp. 485–488)
**Theorem 24.3 (General converse).** If $X\to W\to\hat X$, $W\in[M]$, $\mathbb E d(X,\hat X)\le D$, then
$$\log M\ge\phi_X(D)\triangleq\inf_{P_{Y|X}:\mathbb E[d(X,Y)]\le D}I(X;Y).$$
*Proof:* $\log M\ge H(W)\ge I(X;W)\ge I(X;\hat X)\ge\phi_X(D)$. The last step holds because $P_{\hat X|X}$ is feasible (p. 486).

*Intuition note:* $\log M$ bounds the information the code can carry about $X$. A reconstruction of quality $D$ must carry at least $\phi_X(D)$ bits of information about $X$.

**Theorem 24.4 (Properties of $\phi_X$)** (p. 486). (a) Convex, non-increasing. (b) Continuous on $(D_0,\infty)$, $D_0=\inf\{D:\phi_X(D)<\infty\}$. (c) If $\mathcal X=\hat{\mathcal X}$, $d(x,x)=D_0$ and $d(x,y)>D_0$ for $x\ne y$, then $\phi_X(D_0)=I(X;X)$. (d) If $d$ is a proper metric and $\mathcal X$ a complete metric space, $D_0=0$ and $\phi_X(D_0+)=\phi_X(D_0)=I(X;X)$. (e) With $D_{\max}=\inf_{\hat x}\mathbb Ed(X,\hat x)$: $\phi_X(D)=0$ for $D>D_{\max}$, and also at $D_{\max}$ if $D_0>D_{\max}$ (as printed).
*Proof sketch* (p. 486): (a) from convexity of $P_{Y|X}\mapsto I(P_X,P_{Y|X})$ (Thm 5.3). (b) from convexity. (c) the only feasible choice is $Y=X$. (d) Take $Y_n$ with $\mathbb E d(X,Y_n)\le2^{-n}$ and $I(X;Y_n)\to\phi_X(D_0+)$. By Borel–Cantelli, $d(X,Y_n)\to0$ a.s., so $(X,Y_n)\to(X,X)$. Lower-semicontinuity of $I$ (4.28) gives $I(X;X)\le\phi_X(D_0+)$. (e) Set $\hat X=\hat x$ deterministic, so $I=0$.
*Remark 24.4:* $D_{\max}$ is the distortion attainable with no information (a default reconstruction). $D_0$ is the minimum hoped-for distortion. Example: Gaussian source with MSE has $\phi_X(D)=\frac12\log^+\frac{\sigma^2}{D}$ (to be shown later), $D_0=0$ (not attained), $D_{\max}=\sigma^2$ (p. 486).

**Definition 24.5.** $R^{(I)}(D)=\limsup_n\frac1n\phi_{S^n}(D)$, with $\phi_{S^n}(D)=\inf_{P_{\hat S^n|S^n}:\mathbb E d(S^n,\hat S^n)\le D}I(S^n;\hat S^n)$. It is not itself an operational quantity (p. 487).
**Corollary 24.6.** $\forall D$, $R(D)\ge R^{(I)}(D)$ (p. 487).
**Theorem 24.7.** $R^{(I)}$ is convex and non-increasing, and continuous on $(D_0,\infty)$. Under the 24.4(c) assumption and a stationary ergodic source, $R^{(I)}(D)=\mathcal H$ (entropy rate), or $+\infty$ if $S_k$ is not discrete. $R^{(I)}(D)=0$ for $D>D_{\max}$, where $D_{\max}=\limsup_n\inf_{\hat x^n}\mathbb Ed(X^n,\hat x^n)$ (p. 487).

**Theorem 24.8 (Single-letterization).** For $S_i\overset{iid}{\sim}P_S$ and separable $d$, for every $n$, $\phi_{S^n}(D)=n\phi_S(D)$. Hence $R^{(I)}(D)=\phi_S(D)=\inf_{P_{\hat S|S}:\mathbb E d(S,\hat S)\le D}I(S;\hat S)$ (p. 487).
*Proof* (p. 488). ($\le$) Use the product channel $P_{\hat S|S}^{\otimes n}$. ($\ge$) For any feasible $P_{\hat S^n|S^n}$:
$$I(S^n;\hat S^n)\ge\sum_jI(S_j;\hat S_j)\ \ge\sum_j\phi_S(\mathbb E d(S_j,\hat S_j))\ \ge n\phi_S\Big(\tfrac1n\sum_j\mathbb Ed(S_j,\hat S_j)\Big)\ \ge n\phi_S(D).$$
Reasons: first step, $S^n$ independent and super-additivity of $I$ (6.2); third, convexity of $\phi_S$; fourth, $\phi_S$ non-increasing. Non-stationary memoryless case: Ex. V.10.

### 24.4* Excess to average distortion (pp. 488–489)
**Theorem 24.9.** Suppose $(f,g)$ has $W\in[M]$ and $\mathbb P[d(X,g(W))>D]\le\epsilon$, and for some $p\ge1$, $\hat x_0$: $(\mathbb E[d(X,\hat x_0)^p])^{1/p}=D_p<\infty$. Then there is $(f',g')$ with $W'\in[M+1]$ and
$$\mathbb E[d(X,g(W'))]\le D(1-\epsilon)+D_p\epsilon^{1-1/p}.\tag{24.11}$$
*Proof* (p. 488): add one codeword. $f'(x)=f(x)$ if $d(x,g(f(x)))\le D$, else $M+1$; $g'(j)=g(j)$ for $j\le M$ and $g'(M+1)=\hat x_0$. Then, as printed, $\mathbb E d(X,g'(W'))\le\mathbb E[d\mid\hat W\ne M{+}1](1-\epsilon)+\mathbb E[d(X,\hat x_0)\mathbf 1\{\hat W=M{+}1\}]\le D(1-\epsilon)+D_p\epsilon^{1-1/p}$ (pp. 488–489), the last step by Hölder.
*Remark 24.5:* the result is useful only for $p>1$. For $p=1$ the right side does not tend to $D$ as $\epsilon\to0$. A different method (proof of Thm 25.1) gives a vanishing second term under $D_{\max}=D_1<\infty$, at an unspecified rate (p. 488).

## Toy example (ours, not from the text)
Let $X$ be uniform on $\{0,1,2,3\}$ and $d(x,y)=\mathbf 1\{x\ne y\}$, so $D_0=0$ and $d(x,x)=0$.
- $D=0$: by Thm 24.4(c), $\phi_X(0)=I(X;X)=H(X)=\log_24=2$ bits. So $\log_2M\ge2$, i.e. $M\ge4$. $M=4$ works (store $X$).
- $M=2$: take $W=\mathbf 1\{X\ge2\}$, $g(0)=0$, $g(1)=2$. Then $\hat X$ equals $X$ w.p. $1/2$, so $D=\mathbb P[X\ne\hat X]=1/2$. Chain of Thm 24.3: $\log_2M=1\ge H(W)=1\ge I(X;W)=H(W)=1$ (W is a function of $X$) $\ge I(X;\hat X)=H(\hat X)=1$ (also a function) $\ge\phi_X(1/2)$. So $\phi_X(1/2)\le1$, consistent.
- $D_{\max}=\inf_{\hat x}\mathbb P[X\ne\hat x]=3/4$. For $D>3/4$, $\phi_X(D)=0$: output a constant, $M=1$.
- Single-letterization ($n=2$, iid copies): $\phi_{S^2}(0)=2\phi_S(0)=4$ bits, matching $H(S_1,S_2)=\log_216=4$.

## Concepts
- [[rate–distortion function]] — here: operational $R(D)$ (24.10) lower-bounded by information version $R^{(I)}(D)$ (Def. 24.5) (p. 485, 487)
- [[mutual information I(X;Y)]] — the quantity minimized in $\phi_X(D)$; convex in $P_{Y|X}$, super-additive for independent inputs (p. 486, 488)
- [[differential entropy]] — $h(X)=-\int p\log p$; appears in the entropy of a uniform quantizer's output (p. 483)
- [[entropy rate]] — equals $R^{(I)}(D)$ in the discrete case for a stationary ergodic source, under the distortion assumption of Thm 24.4(c) (p. 487)
- [[distortion-metric]] (new) — measurable $d:\mathcal X\times\hat{\mathcal X}\to\mathbb R\cup\{+\infty\}$; separable version averages per-letter $d$ (p. 484–485)
- [[scalar-uniform-quantization]] (new) — $N$ equally spaced points, $D_U\approx\frac{A^2}{12}2^{-2R}$ at high rate (p. 478)
- [[companding]] (new) — $q=f^{-1}\circ q_U\circ f$; optimal $f$ uses $p^{1/3}$ (p. 479, 483)
- [[lloyd-algorithm]] (new) — alternate Voronoi partition and centroid update; converges to a CVT, maybe non-global (p. 480–481)
- [[panter-dite-approximation]] (new) — optimal point density $\propto p^{1/3}$; $D\approx\frac1{12}2^{-2R}(\int p^{1/3})^3$ (p. 482)
- [[single-letterization]] (new) — $\phi_{S^n}=n\phi_S$ for iid sources and separable $d$ (p. 487)
- [[excess-distortion]] (new) — $\mathbb P[d>D]$ criterion, versus average distortion (p. 485)

## Canonical instances
- [[gaussian-one-bit-quantizer]] — points $\pm\sqrt{2/\pi}\sigma$, error $(1-2/\pi)\sigma^2$ (p. 480)
- [[hamming-game]] — 100 bits, 50 stored: naive 25% BER vs. 11% optimal (p. 484)
- [[gaussian-source-mse]] — $\sigma^22^{-2R}$ jointly vs. $\sigma^22^{-2R}\pi\sqrt3/2$ scalar (pp. 482, 484)
- [[mu-law-companding]] — logarithmic compander used in US telephony (p. 479–480)
- [[k-means]] — optimal vector quantization of the empirical distribution (p. 481)

## Bridges (candidates)
- [same-math] Lloyd's algorithm ↔ machine learning: $k$-means heuristic — the text states the objective is the same (p. 481).
- [structural-analogy] $R(D)\ge R^{(I)}(D)$ via the general converse ↔ channel coding: Shannon vs. information capacity — the text draws this analogy (p. 487).
- [structural-analogy] Single-letterization of $\phi_{S^n}$ ↔ Corollary 20.5 for channel capacity with separable cost — the text says it parallels it (p. 487).
- [structural-analogy] Average vs. excess distortion ↔ statistics/ML: average vs. high-probability risk bounds (p. 485).

## Questions this raises
- Is $R(D)=R^{(I)}(D)$, i.e. is the converse achievable? The text says $R^{(I)}$ is not itself operational (p. 487).
- What are $\phi$ for the Hamming game and the Gaussian source? Their values are only announced (pp. 484, 486).
- How tight is the 1.53 dB bound at moderate rates, given the asymptotic nature of the high-rate results?
- What exact rate does excess-distortion coding achieve (dispersion), and how does it differ from average distortion (p. 485)?

## Exercises worth doing
- Remark 24.3 exercise (p. 482) — Taylor-expand the compander error to derive the optimal $f$ — difficulty: medium
- Ex. V.2 (p. 485) — existence of the iid limit and its equality to the infimum over blocklengths — difficulty: medium
- Ex. V.3 (p. 485) — fast $O(\log n/n)$ convergence rate mentioned in the text — difficulty: hard
- Ex. V.10 (p. 488) — single-letterization for memoryless non-stationary sources — difficulty: medium

## Reading notes
- Printed = pdf − 25. The unit metadata calls this ch27, but the printed chapter number is 24.
- Printed (p. 485): both "excess distortion" sentences, with rates $O(1/\sqrt n)$ and "much faster" $O(\log n/n)$, label the same formulation. The second likely means the average version; I could not resolve this from the pages.
- Printed (p. 486), Thm 24.4(b) proof, writes $\phi_S$ for $\phi_X$. Hölder's inequality in 24.1.4 was OCR-garbled but is confirmed by the image.
- Printed (p. 488): the Thm 24.9 proof uses $\hat W$ for $W'$. The first step bounds the good-event term by $D(1-\epsilon)$ without further justification as I read it. I reproduce it as printed.
- Printed (p. 487), Thm 24.7(d) writes $X^n$ (not $S^n$) in the definition of $D_{\max}$. The proofs of 24.3–24.8 are those printed; Theorem 24.9's proof ends on p. 489.
