---
id: polyanskiy-2025-information/ch22-channels
work: polyanskiy-2025-information
unit: "Chapter 20 (unit ch22-channels): Channels with input constraints. Gaussian channels."
pages: 394-409
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Channels with input constraints. Gaussian channels.

## L0 — One line
With a cost constraint on codewords, capacity of an information-stable channel equals the information capacity, which for memoryless channels is the single-letter supremum of $I(X;Y)$ over inputs meeting the constraint on average; for the AWGN channel this is $\tfrac12\log(1+P/\sigma^2)$, and for parallel, colored or intersymbol-interference Gaussian channels it becomes water-filling over noise levels.

## L1 — The gist (≤ 120 words)
Real transmitters cannot use arbitrary inputs; with Gaussian noise (AWGN channel), unrestricted inputs give infinite capacity. The chapter extends the coding theorems to separable cost constraints and shows that for information-stable channels capacity equals the information capacity, $C(P)=\sup_{E c(X)\le P} I(X;Y)$ in the memoryless case. For the AWGN channel this gives $\tfrac12\log(1+P/\sigma^2)$ with Gaussian inputs. Parallel channels give water-filling power allocation. Colored noise reduces to this recipe by whitening, and intersymbol interference (ISI) reduces to colored noise by inverse filtering. The chapter then states results without proof for amplitude constraints, and surveys fading and multi-antenna (MIMO) channels. It matters because the AWGN formula and water-filling explain power–rate trade-offs and MIMO spatial multiplexing.

**Prerequisites:** mutual information and its concavity in $P_X$; Fano's inequality; weak law of large numbers; Lagrange multipliers; orthogonal diagonalization of covariance matrices; Gaussian saddle point (Thm 5.11).

## L2 — Key ideas (5–10 bullets)
- A cost constraint is separable if $c(x^n)=\frac1n\sum c(x_k)$. The code must lie in $F_n=\{c(x^n)\le P\}$ (p. 395).
- The information capacity maximizes over the relaxed set $E\sum c(X_k)\le nP$. This makes $\phi(P)$ concave and gives single-letterization for memoryless channels (pp. 396–397).
- Weak converse plus an extended Feinstein lemma (a coding lemma) give $C(P)=C^{(I)}(P)$ for information-stable channels (pp. 397–399).
- AWGN capacity is $\tfrac12\log(1+P/\sigma^2)$. The energy per bit is minimal as $P\to0$. The sphere-packing picture is 'tantalizingly convincing' but, the author says, flawed in at least two ways (pp. 399–401).
- Non-Gaussian noise: capacity is at least the Gaussian value and exceeds it by at most $D(P_Z\|\mathcal N)$ (p. 401).
- Parallel AWGN: water-filling, $P_k=|T-\sigma_k^2|^+$. MIMO often reduces to $L=\min(n_r,n_t)$ parallel branches, giving spatial multiplexing (about an $L$-fold capacity gain at high SNR) (pp. 402–403).
- Non-stationary and colored noise: water-filling in the spectrum; ISI reduces to colored noise by inverse filtering (pp. 404–407).
- Amplitude constraints give discrete optimal inputs. Fading with CSIR (the receiver knows the fading gain $H$) gives $E[\tfrac12\log(1+P|H|^2/\sigma^2)]$ for stationary ergodic $H$; without CSIR, for i.i.d. Rayleigh fading, capacity is $O(\log\log P)$ (pp. 407–409).

## L3 — Walkthrough

### Intro (p. 394)
With $A=\mathbb R$ and no constraint, $\sup_{P_X} I(X;X+Z)=\infty$. For example, take $X\sim\mathcal N(0,P)$ and $P\to\infty$. So the encoder is limited to $\frac1n\sum x_t^2\le P$ (power constraint) (p. 394).

### 20.1 Channel coding with input constraints (pp. 394–397)
- An $(n,M,\epsilon)$-code *satisfies* $F_n\subset A^n$ if $f:[M]\to F_n$ (p. 394).
- Average power: $\frac1n\sum|x_i|^2\le P \Leftrightarrow \|x^n\|_2\le\sqrt{nP}$. Peak power $\|x^n\|_\infty\le A$ is just a restricted input alphabet $[-A,A]$. From now on the chapter restricts itself exclusively to separable costs (p. 395).
- **Def 20.1.** A channel with separable cost has input space $A$, output space $B$, Markov kernels $P_{Y^n|X^n}$, and a per-letter cost $c:A\to\mathbb R\cup\{\pm\infty\}$, with $c(x^n)\triangleq\frac1n\sum_{k=1}^n c(x_k)$ (p. 395).
- **Def 20.2.** An $(n,M,\epsilon,P)$-code has $F_n=\{x^n:c(x^n)\le P\}$. $M^*(n,\epsilon,P)=\max\{M:\exists(n,M,\epsilon,P)\text{-code}\}$, and likewise $M^*_{\max}$. $C_\epsilon(P)=\liminf_n\frac1n\log M^*(n,\epsilon,P)$, and $C(P)=\lim_{\epsilon\downarrow0}C_\epsilon(P)$ (p. 395).
- Information capacity: $C^{(I)}(P)=\liminf_n \frac1n\sup_{P_{X^n}:E[\sum c(X_k)]\le nP} I(X^n;Y^n)$ (p. 396).
- Information stability: for every admissible $P$ there are $P_{X^n}$ with $\frac1n i_{P_{X^n,Y^n}}(X^n;Y^n)\xrightarrow{\mathbb P}C^{(I)}(P)$ (20.1) and $\mathbb P[c(X^n)>P+\delta]\to0$ for all $\delta>0$ (20.2) (p. 396).
- The key difference from the unconstrained case (see also the remark on p. 396): the supremum runs over distributions meeting the cost only *in expectation*, not supported on $F_n$. This is crucial for single-letterization (p. 396).
- **Def 20.3.** $P$ is admissible if $\exists x_0$ with $c(x_0)\le P$. The set is $D_c$, of the form $(P_0,\infty)$ or $[P_0,\infty)$, with $P_0=\inf_x c(x)$. Assume $P\in D_c$ (p. 396).
- **Prop 20.4.** $\phi(P)\triangleq\sup_{E c(X)\le P}I(X;Y)$ is concave and non-decreasing, with domain $D_c$. Either $\phi$ is continuous and finite on $(P_0,\infty)$ or $\phi=\infty$ there. The same holds for $C^{(I)}$ (p. 396).
  - Proof of concavity: take $P_{X_i}$ with $E c(X_i)\le P_i$ and $X\sim\bar\lambda P_{X_0}+\lambda P_{X_1}$. Then $E c(X)\le\bar\lambda P_0+\lambda P_1$, and by concavity of $P_X\mapsto I(X;Y)$, $I(X;Y)\ge\bar\lambda I(X_0;Y_0)+\lambda I(X_1;Y_1)$. Hence $\phi(\bar\lambda P_0+\lambda P_1)\ge\bar\lambda\phi(P_0)+\lambda\phi(P_1)$ (p. 396).
  - For $C^{(I)}$: for each $n$, $P\mapsto\frac1n\sup I(X^n;Y^n)$ is concave. Take $\liminf$ (pp. 396–397).
- **Cor 20.5 (single-letterization).** For a stationary memoryless channel with separable cost, $C^{(I)}(P)=\phi(P)=\sup_{E c(X)\le P}I(X;Y)$ (p. 397).
  - "$\ge$": use $P_{X^n}=P_X^{\otimes n}$.
  - "$\le$": for any admissible $P_{X^n}$,
$$I(X^n;Y^n)\overset{(a)}\le\sum_j I(X_j;Y_j)\overset{(b)}\le\sum_j\phi(E c(X_j))\overset{(c)}\le n\phi\Big(\tfrac1n\sum_j E c(X_j)\Big)\le n\phi(P).$$
  - (a) is Thm 6.1, (b) is the definition of $\phi$, and (c) is Jensen with concavity. (added step) The last step uses $\sum_jEc(X_j)\le nP$ and monotonicity of $\phi$ (p. 397).

*Intuition note.* Relaxing "every codeword has cost $\le P$" to "average cost $\le P$" makes the optimization concave. Then, for a memoryless channel, repeating one good single-letter input is optimal.

### 20.2 Capacity under separable cost (pp. 397–399)
- **Thm 20.6 (weak converse).** $C_\epsilon(P)\le C^{(I)}(P)/(1-\epsilon)$. Take any $(n,M,\epsilon,P)$-code. Fano and data processing give $-h(\epsilon)+(1-\epsilon)\log M\le I(W;\hat W)\le I(X^n;Y^n)\le\sup I(X^n;Y^n)$. Normalize by $n$ and take $\liminf$ (p. 397).
- **Thm 20.7 (extended Feinstein).** For a kernel $P_{Y|X}$, any $P_X$, measurable $F\subset\mathcal X$, $\gamma>0$ and $M\ge1$, there is an $(M,\epsilon)_{\max}$-code with $f:[M]\to F$ and
$$\epsilon P_X(F)\le\mathbb P[i(X;Y)<\log\gamma]+\frac M\gamma.$$
  Proof idea (p. 398):
  - Set $E_c=\{y:i(c;y)\ge\log\gamma\}$. By Cor 18.4 there is $F_0$ with $P_X[F_0]=1$ and $P_Y(E_x)\le1/\gamma$ on $F_0$.
  - Let $F'=F\cap F_0$ and pick codewords greedily from $F'$ until $M$ is maximal, with decoding regions $D_j=E_{c_j}\setminus\cup_{k<j}D_k$.
  - Maximality gives, for all $x_0$, $P_Y[E_{x_0}\setminus\cup D_j|X=x_0]<(1-\epsilon)1[x_0\in F']+1[x_0\in F'^c]$.
  - Averaging over $x_0\sim P_X$ gives $\mathbb P[\{i\ge\log\gamma\}\setminus\cup D_j]\le1-\epsilon P_X[F]$. The rest follows the original lemma (Thm 18.7).
- **Thm 20.8 (achievability).** For an information-stable channel and $P>P_0$, $C(P)\ge C^{(I)}(P)$ (20.3) (p. 398).
  - The proof is given for the stationary memoryless case. Choose $P_X$ with $E c(X)<P$, $\log M=n(I(X;Y)-2\delta)$, $\log\gamma=n(I(X;Y)-\delta)$, i.i.d. input and $F_n=\{c(x^n)\le P\}$.
  - Then $\epsilon_n P_{X^n}[F_n]\le\mathbb P[i(X^n;Y^n)\le n(I-\delta)]+e^{-n\delta}$. The first term $\to0$ by the weak law of large numbers, and $P_{X^n}(F_n)\to1$ because $E c(X)<P$ (p. 398).
  - So $C_\epsilon(P)\ge\sup_{E c(X)<P}I(X;Y)=C^{(I)}(P-)=C^{(I)}(P)$, using continuity on $(P_0,\infty)$ (Prop 20.4) (pp. 398–399).
  - For a general information-stable channel one shows $\mathbb P[i(X^n;Y^n)\le n(C^{(I)}-\delta)]\to0$ from the definition (p. 399).
- **Thm 20.9.** For an information-stable channel and admissible $P$, $C(P)=C^{(I)}(P)$. The boundary $P=P_0$ is covered by Ex. IV.23. For $P>P_0$, combine Thm 20.6 ($\epsilon\to0$) with Thm 20.8 (p. 399).

### 20.3 Stationary AWGN channel (pp. 399–402)
- **Def 20.10.** $A=B=\mathbb R$, $c(x)=x^2$, $Y=X+Z$ with $Z\sim\mathcal N(0,\sigma^2)$ independent of $X$. SNR is $P/\sigma^2$. "White" means noise is uncorrelated across time, so the spectral density is flat. The complex version has $c(x)=|x|^2$ and circularly symmetric complex Gaussian noise (p. 399).
- **Thm 20.11.** $C(P)=C^{(I)}(P)=\tfrac12\log(1+P/\sigma^2)$ for real AWGN (20.4), and $\log(1+P/\sigma^2)$ for complex AWGN (p. 400).
  - Proof: by Cor 20.5, $C^{(I)}=\sup_{EX^2\le P}I(X;X+Z)$. By the Gaussian saddle point (Thm 5.11), $X\sim\mathcal N(0,P)$ (or $\mathcal N_c(0,P)$) is the unique maximizer (p. 400).
  - The author notes that Section 6.2* derives the Gaussian capacity essentially without solving the maximization: Euclidean rotational symmetry implies the optimal input should be Gaussian (p. 400).
- Consequences (p. 400):
  - More rate costs more power, but only logarithmically. Good codes look like white Gaussian samples.
  - Energy per bit: $\inf_{P>0}\frac{P\log2}{C(P)}=2\sigma^2\log_e2$ (20.5), reached as $P\to0$. So minimal energy per bit means a quiet, low-rate "whisper". At very low power, binary $\pm\sqrt P$ (BPSK) loses virtually no capacity.
- Geometry: $\|Z^n\|_2\approx\sqrt{n\sigma^2}$ and $E\|Y^n\|^2\le n(P+\sigma^2)$. Packing balls of radius $\sqrt{n\sigma^2}$ into a ball of radius $\sqrt{n(P+\sigma^2)}$ gives a volume ratio $(1+P/\sigma^2)^{n/2}$, so $\frac1n\log M^*\approx\frac12\log(1+P/\sigma^2)$ (p. 401).
  - The author calls this argument flawed in at least two ways. (a) A volume ratio gives only an upper bound on the maximal number of disjoint balls. (b) With non-zero error the balls overlap slightly (p. 401).
- **Thm 20.12 (Ihara).** For $Z$ independent of $X$ with $EZ^2<\infty$ and $\sigma^2=\mathrm{Var}Z$:
$$\tfrac12\log\Big(1+\tfrac P{\sigma^2}\Big)\le\sup_{EX^2\le P}I(X;X+Z)\le\tfrac12\log\Big(1+\tfrac P{\sigma^2}\Big)+D(P_Z\|\mathcal N(EZ,\sigma^2))\tag{20.6}$$
  (proof: Ex. IV.24) (p. 401).
- Remark 20.1: if $Z$ is, e.g., uniform on $[0,1]$, capacity differs from AWGN by a constant. If $Z$ is discrete, $D=\infty$ and capacity is infinite ("noise too weak") (pp. 401–402).

*Intuition note.* Gaussian noise is the worst noise of a given variance. Its capacity is a floor, and the extra capacity from other noise is limited by how far the noise is from Gaussian in KL divergence.

### 20.4 Parallel AWGN (pp. 402–403)
- **Def 20.13.** $A=B=\mathbb R^L$, $c(x)=\sum_k|x_k|^2$, $Y_k=X_k+Z_k$, $Z_k\sim\mathcal N(0,\sigma_k^2)$ independent (p. 402).
- **Thm 20.14 (water-filling).** $C=\frac12\sum_{j=1}^L\log^+\frac T{\sigma_j^2}$, where $\log^+x=\max(\log x,0)$ and $T\ge0$ solves $P=\sum_j|T-\sigma_j^2|^+$ (p. 402).
  - Proof: $C^{(I)}(P)=\sup I(X^L;Y^L)\le\sup_{\sum P_k\le P,P_k\ge0}\sum_k\sup_{EX_k^2\le P_k}I(X_k;Y_k)=\sup\sum_k\frac12\log(1+P_k/\sigma_k^2)$, with equality for independent $X_k\sim\mathcal N(0,P_k)$.
  - Maximize with multipliers $\lambda$ for $\sum P_k\le P$ and $\mu_k$ for $P_k\ge0$. The first-order condition is $\frac12\frac1{\sigma_k^2+P_k}=\lambda-\mu_k$, $\mu_kP_k=0$. Hence $P_k=|T-\sigma_k^2|^+$ (p. 402).
- Fig. 20.2: a branch whose noise level is above $T$ gets zero power (p. 403).
- Practical points (p. 403): water-filling gave a precise power allocation recipe for cable modems/ADSL, replacing costly simulations, and it adapts dynamically to noise.
- MIMO with $n_r$ receive and $n_t$ transmit antennas often gives $L=\min(n_r,n_t)$ parallel branches. Capacity is about $\frac L2\log(P/L)\approx\frac L2\log P$ at large $P$, versus $\frac12\log P$ for one antenna. This is an $L$-fold gain (spatial multiplexing). Sending one stream over all branches (multipath diversity) averages the noise and gives only $\frac12\log(LP)$ (p. 403).

*Intuition note.* Pour power like water into a vessel whose floor is the noise level. Quiet branches get the most, and branches noisier than the water level $T$ get none.

### 20.5* Non-stationary AWGN (pp. 403–404)
- **Def 20.15.** Memoryless, $Y_j=X_j+Z_j$, $Z_j\sim\mathcal N(0,\sigma_j^2)$ independent, $c(x)=x^2$ (p. 403).
- **Thm 20.16.** Assume for every $T>0$ the limits exist: $\tilde C^{(I)}(T)=\lim\frac1n\sum_j\frac12\log^+\frac T{\sigma_j^2}$ and $\tilde P(T)=\lim\frac1n\sum_j|T-\sigma_j^2|^+$. Then capacity is $C=\tilde C^{(I)}(T)$ at power constraint $\tilde P(T)$ (p. 404).
  - Proof: by Thm 20.14, $\sup I(X^n;Y^n)=\sum_j\frac12\log^+\frac T{\sigma_j^2}$ (20.7) over $P_{X^n}$ with $E c(X^n)\le\frac1n\sum|T-\sigma_j^2|^+$ (20.8). Since the right side of (20.8) $\to\tilde P(T)$, we get $C^{(I)}(\tilde P(T)\mp\delta)\lessgtr\tilde C^{(I)}(T)$. Continuity of $C^{(I)}$ gives $C^{(I)}(\tilde P(T))=\tilde C^{(I)}(T)$.
  - Information stability: $\mathrm{Var}(i(X_j;Y_j))=\frac{\log^2e}2\frac{P_j}{P_j+\sigma_j^2}\le\frac{\log^2e}2$ (19.32), so $\sum_j n^{-2}\mathrm{Var}<\infty$. Then use Thm 19.16 (p. 404).

### 20.6* Additive colored Gaussian noise (pp. 405–406)
- **Def 20.17.** $Y^n=X^n+Z^n$, with $\{Z_j\}$ a stationary Gaussian process of power spectral density $f_Z(\omega)\ge0$ on $[-\pi,\pi]$ (p. 405).
- **Thm 20.18.** If $f_Z>0$ almost everywhere, capacity is given parametrically by
$$C(T)=\frac1{2\pi}\int_{-\pi}^{\pi}\tfrac12\log^+\frac T{f_Z(\omega)}\,d\omega,\qquad P(T)=\frac1{2\pi}\int_{-\pi}^{\pi}|T-f_Z(\omega)|^+d\omega.$$
  - Proof (pp. 405–406): diagonalize $\mathrm{Cov}(Z^n)=\Sigma=U^\top\tilde\Sigma U$ with $U$ orthogonal. Set $\tilde X^n=UX^n$, $\tilde Y^n=UY^n$. Then $\tilde Y^n=\tilde X^n+UZ^n$ and $\mathrm{Cov}(UZ^n)=U\,\mathrm{Cov}(Z^n)U^\top=\tilde\Sigma$, so the noise is independent $\mathcal N(0,\sigma_j^2)$.
  - Orthogonal maps preserve norms, so the power constraint and capacity are unchanged. Apply Thm 20.16, with Szegő's theorem (6.12) turning $\frac1n\sum\frac12\log^+\frac T{\sigma_j^2}$ into the integral (p. 406).
- Real noise is often born white (thermal), but linear circuit elements make it effectively colored (p. 406).

### 20.7* AWGN with intersymbol interference (pp. 406–407)
- **Def 20.19.** $Y_k=\sum_{j=1}^nh_{k-j}X_j+Z_k$, with $Z_k$ i.i.d. $\mathcal N(0,\sigma^2)$ and $\{h_k\}$ a discrete-time channel filter (p. 406).
- **Thm 20.20.** Let $h_k=\frac1{2\pi}\int_{-\pi}^{\pi}e^{i\omega k}H(\omega)d\omega$ with $H$ continuous. Then
$$C(T)=\frac1{2\pi}\int_{-\pi}^{\pi}\tfrac12\log^+(T|H(\omega)|^2)d\omega,\qquad P(T)=\frac1{2\pi}\int_{-\pi}^{\pi}\Big|T-\frac1{|H(\omega)|^2}\Big|^+d\omega.$$
  - Proof sketch: apply the inverse filter $1/H(\omega)$ at the decoder. This gives $\tilde Y_j=X_j+\tilde Z_j$ with $f_{\tilde Z}=1/|H|^2$, then apply Thm 20.18. The author says full rigor needs analysis of truncating the deconvolution filter to finite $n$, which is not done (p. 407).

### 20.8* Amplitude constraints (pp. 407–408), stated without proof
- **Thm 20.21.** For $|X_i|\le A$, $C(A)=\max_{|X|\le A}I(X;X+Z)$. The optimal input is discrete with finitely many atoms on $[-A,A]$. The number of atoms is $\Omega(A)$ and $O(A^2)$ as $A\to\infty$. Also $\frac12\log(1+\frac{2A^2}{e\pi})\le C(A)\le\frac12\log(1+A^2)$ (p. 407).
- **Thm 20.22.** With both $|X|\le A$ and $E|X|^2\le P$, the optimal input is discrete and finitely supported. $C(A,P)\to\frac12\log(1+P)$ as $A\to\infty$ at rate $e^{-O(A^2)}$ (p. 408).

### 20.9* Fading (pp. 408–409)
- Model: $Y_i=H_iX_i+Z_i$, $Z_i\sim\mathcal N(0,\sigma^2)$, with $E[X_i^2]\le P$ (p. 408).
- **CSIR (coherent):** the receiver knows $H_i$. If $H_j$ is stationary ergodic, $C(P)=E[\frac12\log(1+P|H|^2/\sigma^2)]$ with $P_X=\mathcal N(0,P)$. Capacity is of order $\log P$ ("energy efficient") (pp. 408–409).
- **No CSIR:** there is no simple formula. For i.i.d. Rayleigh $H_i$ the optimal input is discrete and $C(P)=O(\log\log P)$ as $P\to\infty$ (20.9). The channel is "energy inefficient" (p. 409).
- **MIMO** (20.10): $Y_i=H_iX_i+Z_i$ with $Z_i\sim\mathcal{CN}(0,\sigma^2I_{n_r})$. Mentioned: Alamouti's 2×2 code, space-time coding, Telatar (coherent capacity scales as $\min(n_t,n_r)\log P$, the pre-log or degrees of freedom), and Zheng–Tse (a different pre-log in the non-coherent block-fading case) (p. 409).

## Toy example (ours, not from the text)
Two parallel branches with $\sigma_1^2=1$, $\sigma_2^2=3$. Rates in bits.
- **$P=4$.** Try both branches active: $P=(T-1)+(T-3)=2T-4=4$ gives $T=4$. This is $\ge3$, so it is consistent. Then $P_1=3$, $P_2=1$. $C=\frac12\log_2\frac41+\frac12\log_2\frac43=1+\frac12(0.4150)=1.2075$.
- **$P=1$.** Both active would need $2T-4=1$, so $T=2.5<3$, which contradicts branch 2 being active. So only branch 1 is active: $T-1=1$, $T=2$. Then $P_1=1$, $P_2=0$, and $C=\frac12\log_22=0.5$.
- **Check against equal split** at $P=1$ ($P_k=0.5$): $\frac12\log_2(1+0.5)+\frac12\log_2(1+0.5/3)=0.2925+0.1112=0.4037<0.5$. Water-filling is better.

## Concepts
- [[channel-capacity]] — here $C(P)$: the highest rate at which codewords satisfying a cost constraint can be sent with vanishing error (p. 395)
- [[input-cost-constraint]] (new) — separable constraint $c(x^n)=\frac1n\sum c(x_k)\le P$, e.g. power $c(x)=x^2$ (p. 395)
- [[capacity-cost-function]] (new) — $\phi(P)=\sup_{E c(X)\le P}I(X;Y)$, concave and non-decreasing (p. 396)
- [[information-stability]] (new) — the normalized information density converges in probability to $C^{(I)}(P)$ and $\mathbb P[c(X^n)>P+\delta]\to0$ for every $\delta>0$; this is used to get $C=C^{(I)}$ (p. 396)
- [[noisy-channel-coding-theorem]] — here, $C(P)=C^{(I)}(P)$ via the weak converse and extended Feinstein (pp. 397–399)
- [[awgn-channel]] (new) — $Y=X+Z$, $Z\sim\mathcal N(0,\sigma^2)$, power constraint; capacity $\frac12\log(1+P/\sigma^2)$ per real use (pp. 399–400)
- [[shannon-hartley-formula]] — appears here only as the per-use AWGN formula; no bandwidth $W$ appears in this unit (p. 400)
- [[water-filling]] (new) — optimal power $P_k=|T-\sigma_k^2|^+$ across parallel or spectral branches (p. 402)
- [[relative-entropy]] — $D(P_Z\|\mathcal N)$ measures non-Gaussianness and bounds the capacity gain (p. 401)
- [[csir-fading-channel]] (new) — fading $Y=HX+Z$; capacity of order $\log P$ with receiver channel knowledge (stationary ergodic $H$); $O(\log\log P)$ without it for i.i.d. Rayleigh $H_i$ (pp. 408–409)

## Canonical instances
- [[awgn-sphere-packing]] — heuristic packing of $\sqrt{n\sigma^2}$-balls in a $\sqrt{n(P+\sigma^2)}$-ball (p. 401)
- [[mimo-spatial-multiplexing]] — $L$-fold capacity gain via parallel branches, versus $\frac12\log(LP)$ for multipath diversity (p. 403)
- [[adsl-power-allocation]] — water-filling for cable modems and ADSL (p. 403)
- [[deep-space-communication]] — low power and low rate give minimal energy per bit (p. 400)

## Bridges (candidates)
- [structural-analogy] Water-filling over $\sigma_j^2$ ↔ reverse water-filling in rate–distortion for parallel Gaussians (not in this unit; to be checked by the Knowledge Manager).
- [structural-analogy] Concavity of $\phi(P)$ plus Jensen ↔ concavity of the capacity-cost trade-off in rational inattention (cost-limited information intake).
- [same-math] Szegő limit of $\frac1n\sum\log\sigma_j^2$ to the spectral integral ↔ entropy rate of a Gaussian process (the chapter points to (6.12)).
- [metaphor] Pouring water into a vessel ↔ allocating a fixed budget across noisy sources.

## Questions this raises
- When is capacity under average cost achievable with strict per-codeword constraints at finite $n$? Only the first-order limit is shown here.
- How tight is $D(P_Z\|\mathcal N)$ in Ihara's bound for specific non-Gaussian noises?
- Why does a discrete input become optimal under amplitude constraints?
- What is the exact capacity without CSIR, beyond $O(\log\log P)$?

## Exercises worth doing
- Ex. IV.23 (p. 399) — the boundary case $P=P_0$ of Thm 20.9 — difficulty: hard
- Ex. IV.24 (p. 401) — proof of Ihara's bound (20.6) — difficulty: hard
- Ex. I.9 and I.10 (p. 403, p. 409) — reduction of MIMO to parallel AWGN; MIMO capacity under CSIR — difficulty: medium

## Reading notes
- The printed chapter number is 20, but the unit id says ch22. Printed pages 394–409. printed = pdf − 25.
- Misprints and looseness seen in the images:
  - Prop 20.4 writes $\{x:f(x)>-\infty\}$; $\phi$ is meant.
  - Def 20.10 writes $Z^n\sim\mathcal N(0,I_n)$ while the single-letter variance is $\sigma^2$; $\sigma^2I_n$ is presumably meant.
  - In Thm 20.18's proof, $\tilde\Sigma=\mathrm{diag}(\sigma_1,\dots,\sigma_n)$ is used for variances ($\sigma_j^2$ afterwards).
  - Thm 20.20 assumes $H$ is continuous on $[0,2\pi]$ but integrates over $[-\pi,\pi]$.
  - $H_i\in\mathbb C^{n_t\times n_r}$ in (20.10) is printed in that order, although $Y_i\in\mathbb C^{n_r}$ would suggest $n_r\times n_t$.
- The text layer of the Thm 20.14 proof prints a stray "P" before "sup"; the image shows only the supremum.
- Sections 20.5–20.9 are starred in the source. 20.8 says it lists results without proof; 20.9 also gives no proofs and cites the literature.
