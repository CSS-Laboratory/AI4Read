---
id: cover-2006-elements/ch10-gaussian
work: cover-2006-elements
unit: "10 The Gaussian Channel"
pages: 239-265
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# The Gaussian Channel

## L0 — One line
With additive Gaussian noise of variance $N$ and input power limit $P$, the capacity is $\tfrac12\log(1+P/N)$ bits per use, and the same method gives band-limited, parallel (water-filling), coloured-noise and feedback results.

## L1 — The gist (≤ 120 words)
How many bits can be sent reliably through a channel that adds Gaussian noise to a real-valued input with limited power? The chapter shows that the capacity is $\tfrac12\log(1+P/N)$ per transmission. Achievability uses random Gaussian codes and joint typicality; the converse uses Fano's inequality and Jensen's inequality. For bandwidth $W$ this becomes $W\log(1+P/N_0W)$ bits per second. With several channels or coloured (correlated, non-white) noise, power should be "water-filled" (poured like water, lowest noise first) onto the quietest components. Feedback does not help memoryless channels, but for channels with memory it can add at most half a bit per transmission. The Gaussian channel is used as a model for radio, satellite and telephone links.

**Prerequisites:** differential entropy and the fact that the normal maximizes it for a given variance; mutual information; joint AEP and Fano's inequality from the discrete channel theorem; Jensen's inequality; covariance matrices, determinants, eigen-decomposition; Lagrange multipliers.

## L2 — Key ideas (5–10 bullets)
- The Gaussian channel is $Y_i=X_i+Z_i$ with i.i.d. $\mathcal N(0,N)$ noise. Capacity is infinite if the input is unconstrained (or the noise variance is zero), so one imposes an average power limit $P$ (pp. 239–240).
- Capacity is $C=\max_{EX^2\le P}I(X;Y)=\tfrac12\log(1+P/N)$, attained by $X\sim\mathcal N(0,P)$. It follows from $I=h(Y)-h(Z)$ and the maximum-entropy property of the normal (pp. 241–242).
- Achievability uses random Gaussian codebooks of variance $P-\epsilon$, joint-typicality decoding, and discarding the worst half of the codewords. The converse is Fano plus Jensen (pp. 244–247). A sphere-packing picture gives the same $C$ heuristically (p. 243).
- Sampling a signal band-limited to $W$ at $2W$ samples per second determines it. A band-limited channel is therefore $2W$ Gaussian channels per second, giving $C=W\log(1+P/N_0W)$ (pp. 248–250).
- For $k$ parallel Gaussian channels with a shared power budget, the optimal allocation is $P_i=(\nu-N_i)^+$ ("water-filling"). More power goes to quieter channels (pp. 252–253).
- For coloured noise the same rule applies to the eigenvalues of the noise covariance. For stationary noise it becomes water-filling over the noise spectrum (pp. 254–256).
- Feedback does not raise capacity for memoryless channels, but can for channels with memory. It raises capacity by at most $\tfrac12$ bit per transmission: $C_{n,FB}\le C_n+\tfrac12$ (pp. 256, 259–261).

## L3 — Walkthrough

### Introduction (pp. 239–241)
- Model: $Y_i=X_i+Z_i$, $Z_i\sim\mathcal N(0,N)$ i.i.d., independent of $X_i$ \tag{10.1} (p. 239).
- Without further conditions the capacity may be infinite (p. 239).
  - If $N=0$, any real number passes without error.
  - If $N>0$ and the input is unconstrained, one can pick infinitely many inputs arbitrarily far apart that are distinguishable with arbitrarily small error probability.
- Power constraint: every codeword satisfies $\frac1n\sum_{i=1}^n x_i^2\le P$ \tag{10.2} (p. 239).
- Why Gaussian noise: by the central limit theorem, many small random effects add up to approximately normal noise (p. 240).
- **A simple suboptimal scheme** (p. 240). Send 1 bit per use with levels $\pm\sqrt P$, both equally likely. The optimal rule decides $+\sqrt P$ if $Y>0$ and $-\sqrt P$ if $Y<0$. The error probability is
$$P_e=\tfrac12\Pr(Y<0\mid X=+\sqrt P)+\tfrac12\Pr(Y>0\mid X=-\sqrt P)\tag{10.3}$$
$$=\tfrac12\Pr(Z<-\sqrt P\mid X=+\sqrt P)+\tfrac12\Pr(Z>\sqrt P\mid X=-\sqrt P)\tag{10.4}$$
$$=\Pr(Z>\sqrt P)\tag{10.5}$$
$$=1-\Phi\!\left(\sqrt{P/N}\right),\qquad \Phi(x)=\int_{-\infty}^{x}\tfrac{1}{\sqrt{2\pi}}e^{-t^2/2}dt\tag{10.6, 10.7}$$
  - This turns the Gaussian channel into a binary symmetric channel with crossover probability $P_e$. A four-level input gives a four-input discrete channel.
  - Gain: the output is easier to process for error correction. Cost: some information is lost in the quantization (pp. 240–241).

### 10.1 Definitions; capacity and achievability (pp. 241–245)
**Definition (p. 241).** The information capacity with power constraint $P$ is
$$C=\max_{p(x):\,EX^2\le P}I(X;Y).\tag{10.8}$$

**Computation (pp. 241–242).**
$$I(X;Y)=h(Y)-h(Y|X)=h(Y)-h(X+Z|X)=h(Y)-h(Z|X)=h(Y)-h(Z)\tag{10.9–10.12}$$
The last step holds because $Z$ is independent of $X$. Here $h(Z)=\tfrac12\log 2\pi eN$ and
$$EY^2=E(X+Z)^2=EX^2+2EX\,EZ+EZ^2=P+N\tag{10.13}$$
since $X,Z$ are independent and $EZ=0$. By Theorem 9.6.5 (the normal maximizes entropy for a given variance), $h(Y)\le\tfrac12\log 2\pi e(P+N)$. Hence
$$I(X;Y)=h(Y)-h(Z)\le\tfrac12\log2\pi e(P+N)-\tfrac12\log2\pi eN=\tfrac12\log\!\left(1+\tfrac PN\right)\tag{10.14–10.16}$$
$$C=\max_{EX^2\le P}I(X;Y)=\tfrac12\log\!\left(1+\tfrac PN\right),\ \text{attained when } X\sim\mathcal N(0,P)\tag{10.17}$$

*Intuition note.* The noise adds a fixed amount of uncertainty, $h(Z)$. The best the sender can do is make the output as spread out as the power allows, and the normal is the most spread-out shape for a given variance. The capacity is the gap between those two entropies.

**Definitions (p. 242).**
- A $(M,n)$ code has an index set $\{1,\dots,M\}$, an encoding map $x^n(\cdot)$, and a decoder $g:\mathcal Y^n\to\{1,\dots,M\}$. Every codeword must satisfy $\sum_{i=1}^n x_i^2(w)\le nP$ for $w=1,\dots,M$ \tag{10.18, 10.19}.
- Rate and error probability are defined as in Chapter 8.
- A rate $R$ is *achievable* if there is a sequence of $(2^{nR},n)$ codes satisfying the power constraint whose maximal error probability $\lambda^{(n)}\to0$. Capacity is the supremum of achievable rates.

**Theorem 10.1.1.** The capacity is $C=\tfrac12\log(1+P/N)$ bits per transmission \tag{10.20} (p. 242).

**Plausibility (sphere packing) (pp. 242–243).**
- The received vector is normal around the true codeword with variance $N$ per coordinate. With high probability it lies in a sphere of radius $\sqrt{n(N+\epsilon)}$ around it, so each decoding sphere has radius about $\sqrt{nN}$.
- Received vectors have energy at most $n(P+N)$, so they lie in a sphere of radius $\sqrt{n(P+N)}$. A sphere of radius $r$ has volume $A_nr^n$.
- The number of non-intersecting decoding spheres is no more than
$$\frac{A_n\,(n(P+N))^{n/2}}{A_n\,(nN)^{n/2}}=2^{\frac n2\log(1+P/N)}\tag{10.21}$$
so the rate is $\tfrac12\log(1+P/N)$ (Figure 10.2).
- The author says this indicates that rates above $C$ cannot be sent with low error. The proofs follow (p. 243).

**Proof of achievability (pp. 244–245).** The method is random codes plus joint-typicality decoding, modified for the power constraint and for continuous variables.
1. *Codebook.* Draw all $X_i(w)$, $i=1..n$, $w=1..2^{nR}$, i.i.d. $\mathcal N(0,P-\epsilon)$. For large $n$, $\frac1n\sum X_i^2\to P-\epsilon$, so a codeword violates the constraint with small probability. Bad codewords are not deleted, to keep the symmetry of later arguments.
2. *Encoding.* The codebook is known to both sides. Message $w$ is sent as $X^n(w)$.
3. *Decoding.* The receiver looks for a codeword jointly typical with $Y^n$. If there is exactly one, it declares that one. Otherwise it declares an error. It also declares an error if the chosen codeword violates the power constraint.
4. *Error probability.* Assume codeword 1 was sent, so $Y^n=X^n(1)+Z^n$. Define
$$E_0=\Big\{\tfrac1n\sum_{i=1}^nX_i^2(1)>P\Big\},\qquad E_i=\{(X^n(i),Y^n)\in A_\epsilon^{(n)}\}\tag{10.22, 10.23}$$
An error occurs if $E_0$ occurs, or $E_1^c$ occurs, or $E_2\cup\dots\cup E_{2^{nR}}$ occurs. Writing $\mathcal E$ for the event $\hat W\ne W$ and $P$ for probability given $W=1$, the union bound gives
$$\Pr(\mathcal E|W=1)=P(E_0\cup E_1^c\cup E_2\cup\dots\cup E_{2^{nR}})\le P(E_0)+P(E_1^c)+\sum_{i=2}^{2^{nR}}P(E_i)\tag{10.24, 10.25}$$
   - $P(E_0)\to0$ by the law of large numbers.
   - $P(E_1^c)\to0$ by the joint AEP, so $P(E_1^c)\le\epsilon$ for $n$ large \tag{10.26}.
   - $X^n(1)$ and $X^n(i)$ are independent, so $Y^n$ and $X^n(i)$ are independent. By the joint AEP, the probability that $X^n(i)$ and $Y^n$ are jointly typical is $\le2^{-n(I(X;Y)-3\epsilon)}$.
   - Therefore
$$P_e^{(n)}\le\epsilon+\epsilon+\sum_{i=2}^{2^{nR}}2^{-n(I(X;Y)-3\epsilon)}=2\epsilon+(2^{nR}-1)2^{-n(I(X;Y)-3\epsilon)}\le2\epsilon+2^{3n\epsilon}2^{-n(I(X;Y)-R)}\le3\epsilon\tag{10.27–10.32}$$
   for $n$ large and $R<I(X;Y)-3\epsilon$.
5. *Expurgation.* Choose a good codebook and delete the worst half of the codewords. This gives low *maximal* error probability. Every remaining codeword satisfies the power constraint, because codewords violating it have error probability 1 and so lie in the worst half. Thus rates arbitrarily close to capacity are achievable (p. 245).

*Intuition note.* Random codes work because a wrong codeword is almost never jointly typical with the received word. Its chance is at most about $2^{-nI}$ (p. 245), so the union bound allows up to about $2^{nI}$ codewords. Drawing codewords with variance slightly below $P$ keeps almost all of them within the power limit.

### 10.2 Converse (pp. 245–247)
Claim: if $P_e^{(n)}\to0$ for a sequence of $(2^{nR},n)$ codes with power constraint $P$, then $R\le C=\tfrac12\log(1+P/N)$ \tag{10.33}. The code satisfies $\frac1n\sum x_i^2(w)\le P$ \tag{10.34}. Take $W$ uniform on the indices. Fano's inequality gives
$$H(W|Y^n)\le1+nRP_e^{(n)}=n\epsilon_n,\quad\epsilon_n\to0\ \text{as}\ P_e^{(n)}\to0\tag{10.35}$$
Then
$$nR=H(W)=I(W;Y^n)+H(W|Y^n)\le I(W;Y^n)+n\epsilon_n\le I(X^n;Y^n)+n\epsilon_n\tag{10.36–10.38}$$
$$=h(Y^n)-h(Y^n|X^n)+n\epsilon_n=h(Y^n)-h(Z^n)+n\epsilon_n\tag{10.39, 10.40}$$
$$\le\sum_i h(Y_i)-h(Z^n)+n\epsilon_n=\sum_i h(Y_i)-\sum_ih(Z_i)+n\epsilon_n=\sum_iI(X_i;Y_i)+n\epsilon_n\tag{10.41–10.43}$$
- (added step) (10.38) uses the data processing inequality ($W\to X^n\to Y^n$). (10.41) uses the chain rule and "conditioning reduces entropy".
- Let $P_i=\frac1{2^{nR}}\sum_wx_i^2(w)$ be the average power of column $i$ \tag{10.44}. The power of $Y_i$ is $P_i+N$, so $h(Y_i)\le\tfrac12\log2\pi e(P_i+N)$ \tag{10.45}.
- Then
$$nR\le\sum_i\big(h(Y_i)-h(Z_i)\big)+n\epsilon_n\le\sum_i\tfrac12\log\!\left(1+\tfrac{P_i}N\right)+n\epsilon_n\tag{10.46–10.48}$$
- Each codeword meets the constraint, so does the average: $\frac1n\sum_iP_i\le P$ \tag{10.49}.
- Since $x\mapsto\tfrac12\log(1+x)$ is concave, Jensen gives
$$\frac1n\sum_{i=1}^n\tfrac12\log\!\left(1+\tfrac{P_i}N\right)\le\tfrac12\log\!\left(1+\tfrac1n\sum_i\tfrac{P_i}N\right)\le\tfrac12\log\!\left(1+\tfrac PN\right)\tag{10.50, 10.51}$$
- So $R\le\tfrac12\log(1+P/N)+\epsilon_n$. The author notes that the power constraint enters this proof at (10.44) (p. 247).

*Intuition note.* Power can be spread unevenly over time, but because $\log(1+x)$ is concave, an uneven spread gives no larger bound than the even one (Jensen, p. 247). That is why the bound depends only on the average power.

### 10.3 Band-limited channels (pp. 247–250)
- Model: $Y(t)=(X(t)+Z(t))*h(t)$ \tag{10.52}. Here $h$ is the impulse response of an ideal bandpass filter that removes frequencies above $W$, and $Z$ is white Gaussian noise (pp. 247–248).
- **Theorem 10.3.1 (Nyquist–Shannon sampling)** (p. 248). If $f(t)$ is band-limited to $W$ (spectrum zero above frequency $W$), it is completely determined by samples spaced $\frac1{2W}$ seconds apart.
- Proof (pp. 248–249).
  - Let $F(\omega)$ be the spectrum of $f(t)$. It vanishes outside $-2\pi W\le\omega\le2\pi W$ [equations 10.53–10.55 `[unreadable p. 248]`; described here from the prose only].
  - The right-hand side of (10.55), which gives the sample value at $t=n/2W$, is also the definition of the Fourier-series coefficients of the periodic extension of $F$ with fundamental period $(-2\pi W,2\pi W)$. So the samples determine $F$ on that interval, hence $f$.
  - Explicit reconstruction: $\operatorname{sinc}(t)=\frac{\sin(2\pi Wt)}{2\pi Wt}$ \tag{10.56}. It equals 1 at $t=0$ and 0 at $t=n/2W$, $n\ne0$. Its spectrum is constant in $(-W,W)$ and zero outside.
$$g(t)=\sum_{n=-\infty}^{\infty}f\!\left(\tfrac n{2W}\right)\operatorname{sinc}\!\left(t-\tfrac n{2W}\right)\tag{10.57}$$
  - $g$ is band-limited to $W$ and equals $f(n/2W)$ at the sample points. Only one function satisfies these constraints, so $g=f$ (p. 249).
- A general function has infinitely many degrees of freedom. A band-limited one has $2W$ per second (p. 249).
- A function cannot be both band-limited and time-limited. For functions with most energy in bandwidth $W$ and in a time interval $(0,T)$, there are about $2TW$ orthonormal prolate spheroidal basis functions. White noise projected on them is an i.i.d. Gaussian process. Such functions are therefore vectors in a $2TW$-dimensional space (p. 249).
- Channel (p. 249). Input and output are represented by samples $\frac1{2W}$ s apart. With noise power spectral density $N_0/2$ and bandwidth $W$, the noise power is $\frac{N_0}{2}2W=N_0W$. Each of the $2WT$ noise samples in time $T$ has variance $N_0WT/2WT=N_0/2$.
- Over $[0,T]$ the power per sample is $PT/2WT=P/2W$ (p. 250). Hence
$$C=\tfrac12\log\!\left(1+\frac{P/2W}{N_0/2}\right)=\tfrac12\log\!\left(1+\frac P{N_0W}\right)\ \text{bits per sample}\tag{10.59}$$
- With $2W$ samples per second:
$$C=W\log\!\left(1+\frac P{N_0W}\right)\ \text{bits per second}\tag{10.60}$$
  The author calls this one of the most famous formulae of information theory.
- As $W\to\infty$: $C=\frac P{N_0}\log_2e$ bits per second \tag{10.61}. For infinite bandwidth, capacity grows linearly with power (p. 250).
- **Example 10.3.1 (telephone line)** (p. 250). Bandwidth 3300 Hz and SNR 20 dB (i.e. $P/N_0W=100$) give a capacity of about 22,000 bits per second. Practical modems reach up to 19,200 bits per second. Real lines have crosstalk, echoes, non-flat response and so on, which must be compensated for.

*Intuition note.* A band-limited signal carries $2W$ independent real numbers per second, and each is a Gaussian channel use. Capacity per second is therefore $2W$ times the per-use capacity, with the noise per sample set by the noise density.

### 10.4 Parallel Gaussian channels (pp. 250–253)
- Setup: $Y_j=X_j+Z_j$, $Z_j\sim\mathcal N(0,N_j)$ independent across channels, $j=1..k$ \tag{10.62, 10.63}. Shared constraint $E\sum_jX_j^2\le P$ \tag{10.64}. This models non-white noise, with one channel per frequency (p. 250).
- $C=\max_{f(x_1..x_k):\sum EX_j^2\le P}I(X_1..X_k;Y_1..Y_k)$ \tag{10.65}. That this is the supremum of achievable rates is proved as for the single channel, and omitted (p. 251).
- Bound (p. 252), using independence of the $Z_j$:
$$I(X_1..X_k;Y_1..Y_k)=h(Y_1..Y_k)-h(Z_1..Z_k)=h(Y_1..Y_k)-\sum_ih(Z_i)\tag{10.66, 10.67}$$
$$\le\sum_i\big(h(Y_i)-h(Z_i)\big)\le\sum_i\tfrac12\log\!\left(1+\tfrac{P_i}{N_i}\right)\tag{10.68, 10.69}$$
  with $P_i=EX_i^2$ and $\sum P_i=P$. Equality holds for $(X_1..X_k)\sim\mathcal N(0,\operatorname{diag}(P_1,\dots,P_k))$ \tag{10.70}.
- Lagrange multipliers:
$$J(P_1..P_k)=\sum_i\tfrac12\log\!\left(1+\tfrac{P_i}{N_i}\right)+\lambda\Big(\sum_iP_i\Big)\tag{10.71}$$
$$\tfrac12\,\tfrac1{P_i+N_i}+\lambda=0\ \Rightarrow\ P_i=\nu-N_i\tag{10.72, 10.73}$$
- Since $P_i\ge0$ this form may not be possible. The Kuhn–Tucker conditions then give
$$P_i=(\nu-N_i)^+,\qquad\sum_i(\nu-N_i)^+=P,\qquad (x)^+=\begin{cases}x&x\ge0\\0&x<0\end{cases}\tag{10.74–10.76}$$
- **Water-filling** (Figure 10.4, p. 253). Noise levels are vertical heights. As power grows from zero, it goes first to the channels with lowest noise. With more power, noisier channels start to receive some too, like water filling a vessel.

*Intuition note.* A unit of power gives most extra information where noise is smallest. So the best split fills the quietest channels up to a common level $\nu$. Channels whose noise is above $\nu$ get no power.

### 10.5 Coloured Gaussian noise (pp. 253–256)
- This covers dependent noise across parallel channels, and also channels with memory: $n$ consecutive uses are $n$ parallel channels with dependent noise. Only the information capacity is computed (p. 253).
- $K_Z$ is the noise covariance and $K_X$ the input covariance, both $n\times n$. The constraint is $\frac1n\sum EX_i^2\le P$, equivalently $\frac1n\operatorname{tr}(K_X)\le P$ \tag{10.77, 10.78}. It depends on $n$, so capacity must be computed for each $n$ (p. 254).
- $I(X^n;Y^n)=h(Y^n)-h(Z^n)$ \tag{10.79}. The term $h(Z^n)$ does not depend on the input, so one maximizes $h(Y^n)$. This is done by a normal $Y$, which comes from a normal input. Then $K_Y=K_X+K_Z$ and
$$h(Y_1..Y_n)=\tfrac12\log\big((2\pi e)^n|K_X+K_Z|\big)\tag{10.80}$$
- Decompose $K_Z=Q\Lambda Q^t$, $QQ^t=I$ \tag{10.81}. Then
$$|K_X+K_Z|=|K_X+Q\Lambda Q^t|=|Q||Q^tK_XQ+\Lambda||Q^t|=|Q^tK_XQ+\Lambda|=|A+\Lambda|,\quad A=Q^tK_XQ\tag{10.82–10.85}$$
- Since $\operatorname{tr}(BC)=\operatorname{tr}(CB)$ \tag{10.86}: $\operatorname{tr}(A)=\operatorname{tr}(Q^tK_XQ)=\operatorname{tr}(QQ^tK_X)=\operatorname{tr}(K_X)$ \tag{10.87–10.89}. So we maximize $|A+\Lambda|$ subject to $\operatorname{tr}(A)\le nP$ (p. 255).
- Hadamard's inequality (from Chapter 9): for positive definite $K$, $|K|\le\prod_iK_{ii}$, with equality iff $K$ is diagonal \tag{10.90}. Hence $|A+\Lambda|\le\prod_i(A_{ii}+\lambda_i)$, with equality iff $A$ is diagonal \tag{10.91}.
- With $\frac1n\sum A_{ii}\le P$ and $A_{ii}\ge0$ \tag{10.92}, the product is maximized when $A_{ii}+\lambda_i=\nu$ \tag{10.93}. If that is impossible with positive $A_{ii}$, the Kuhn–Tucker conditions (stated by the author, not worked out) give
$$A_{ii}=(\nu-\lambda_i)^+,\qquad\sum A_{ii}=nP\tag{10.94}$$
  This is water-filling over the eigenvalues of $K_Z$ (Figure 10.4).
- Stationary noise (p. 255). $K_Z^{(n)}$ is Toeplitz. Its eigenvalues tend to a limit as $n\to\infty$, and their density tends to the power spectrum of the process. Water-filling then happens in the spectral domain (Figure 10.5, p. 256).
- The input should be a Gaussian process whose spectrum is large where the noise spectrum is small. The capacity with noise spectrum $N(f)$ "can be shown" (cited, not proved) to be
$$C=\int\tfrac12\log\!\left(1+\frac{(\nu-N(f))^+}{N(f)}\right)df,\qquad\int(\nu-N(f))^+df=P\tag{10.95}$$

*Intuition note.* Rotating to the eigenbasis of the noise covariance turns correlated noise into independent parallel channels. The problem is then the previous section's water-filling, with eigenvalues playing the role of noise levels.

### 10.6 Gaussian channels with feedback (pp. 256–261)
- Statements (p. 256).
  - Feedback does not increase capacity for discrete memoryless channels (Chapter 8) or for memoryless Gaussian channels. It can greatly simplify encoding or decoding.
  - For channels with memory (correlated noise), feedback does increase capacity.
  - There is no simple explicit characterization of capacity with feedback.
- Model (p. 257): $Y_i=X_i+Z_i$, $Z^n\sim\mathcal N(0,K_Z^{(n)})$ \tag{10.96}. A $(2^{nR},n)$ code is a sequence of maps $x_i(W,Y^{i-1})$, a code *function* rather than a codeword. Power constraint: $E\big[\frac1n\sum_ix_i^2(w,Y^{i-1})\big]\le P$ for all $w$ \tag{10.97}, with the expectation over noise. $X^n$ and $Z^n$ are no longer independent, since $X_i$ depends causally on past $Z$.
- Informal characterizations (pp. 257–258). The converse for the feedback capacity is proved below. Achievability is stated, not proved.
  - **With feedback:**
$$C_{n,FB}=\max_{\frac1n\operatorname{tr}(K_X^{(n)})\le P}\frac1{2n}\log\frac{|K_{X+Z}^{(n)}|}{|K_Z^{(n)}|}\tag{10.98}$$
    where the maximum is over $X^n$ of the form $X_i=\sum_{j=1}^{i-1}b_{ij}Z_j+V_i$, with $V^n$ independent of $Z^n$ \tag{10.99}. The author argues this loses no generality. The maximizing distribution on $X^n+Z^n$ is Gaussian, so a jointly Gaussian $(X^n,Z^n,X^n+Z^n)$ achieves the maximum "it can be verified". The most general jointly normal causal dependence of $X^n$ on $Y^n=X^n+Z^n$ is then of the form (10.99), with $V^n$ the innovations process. With $X=BZ+V$ ($B$ strictly lower triangular):
$$C_{n,FB}=\max\frac1{2n}\log\frac{|(B+I)K_Z^{(n)}(B+I)^t+K_V|}{|K_Z^{(n)}|}\tag{10.100}$$
    over nonnegative definite $K_V$ and strictly lower triangular $B$ with $\operatorname{tr}(BK_Z^{(n)}B^t+K_V)\le nP$ \tag{10.101}. Without feedback $B=0$.
  - **Without feedback:**
$$C_n=\max_{\frac1n\operatorname{tr}(K_X)\le P}\frac1{2n}\log\frac{|K_X^{(n)}+K_Z^{(n)}|}{|K_Z^{(n)}|}\tag{10.102}$$
    This reduces to water-filling on the eigenvalues $\lambda_i^{(n)}$ of $K_Z^{(n)}$:
$$C_n=\frac1{2n}\sum_{i=1}^n\log\!\left(1+\frac{(\lambda-\lambda_i^{(n)})^+}{\lambda_i^{(n)}}\right),\qquad\sum_{i=1}^n(\lambda-\lambda_i^{(n)})^+=nP\tag{10.103, 10.104}$$

**Theorem 10.6.1 (p. 259).** For any $(2^{nR_n},n)$ code with $P_e^{(n)}\to0$ for the feedback channel,
$$R_n\le\frac1n\,\frac12\log\frac{|K_Y^{(n)}|}{|K_Z^{(n)}|}+\epsilon_n,\quad\epsilon_n\to0\tag{10.105}$$
Proof. Fano gives $H(W|Y^n)\le1+nR_nP_e^{(n)}=n\epsilon_n$ \tag{10.106}. Then
$$nR_n=H(W)=I(W;Y^n)+H(W|Y^n)\le I(W;Y^n)+n\epsilon_n=\sum_iI(W;Y_i|Y^{i-1})+n\epsilon_n\tag{10.107–10.110}$$
$$\overset{(a)}=\sum_i\big[h(Y_i|Y^{i-1})-h(Y_i|W,Y^{i-1},X_i,X^{i-1},Z^{i-1})\big]+n\epsilon_n\tag{10.111}$$
$$\overset{(b)}=\sum_i\big[h(Y_i|Y^{i-1})-h(Z_i|W,Y^{i-1},X_i,X^{i-1},Z^{i-1})\big]+n\epsilon_n\tag{10.112}$$
$$\overset{(c)}=\sum_i\big[h(Y_i|Y^{i-1})-h(Z_i|Z^{i-1})\big]+n\epsilon_n=h(Y^n)-h(Z^n)+n\epsilon_n\tag{10.113, 10.114}$$
- (a): $X_i$ is a function of $W$ and past $Y$, and $Z^{i-1}=Y^{i-1}-X^{i-1}$.
- (b): $Y_i=X_i+Z_i$ and $h(X+Z|X)=h(Z|X)$.
- (c): $Z_i$ and $(W,Y^{i-1},X^i)$ are conditionally independent given $Z^{i-1}$.
- Dividing by $n$ and using the entropy-maximizing property of the normal:
$$R_n\le\tfrac1n[h(Y^n)-h(Z^n)]+\epsilon_n\le\frac1{2n}\log\frac{|K_Y^{(n)}|}{|K_Z^{(n)}|}+\epsilon_n\tag{10.115}$$
This is an upper bound in terms of $K_{X+Z}$ (the covariance of $Y$). Bounds in terms of $K_X$ and $K_Z$ follow (p. 259). Notation: the superscript $n$ is dropped from covariance matrices (p. 260).

**Lemma 10.6.1.** For $n$-dimensional random vectors $X,Z$: $K_{X+Z}+K_{X-Z}=2K_X+2K_Z$ \tag{10.116} (p. 260).
Proof. $K_{X+Z}=E(X+Z)(X+Z)^t=EXX^t+EXZ^t+EZX^t+EZZ^t=K_X+K_{XZ}+K_{ZX}+K_Z$ \tag{10.117–10.119}. Similarly $K_{X-Z}=K_X-K_{XZ}-K_{ZX}+K_Z$ \tag{10.120}. Adding the two completes the proof.

**Lemma 10.6.2 (p. 260).** For positive definite $n\times n$ matrices $A,B$: if $A-B$ is positive definite, then $|A|\ge|B|$.
Proof. Let $C=A-B$. Take independent $\mathbf X_1\sim\mathcal N(0,B)$, $\mathbf X_2\sim\mathcal N(0,C)$ and $\mathbf Y=\mathbf X_1+\mathbf X_2$. Then
$$h(\mathbf Y)\ge h(\mathbf Y|\mathbf X_2)=h(\mathbf X_1|\mathbf X_2)=h(\mathbf X_1)\tag{10.121–10.123}$$
The inequality holds because conditioning reduces differential entropy; the last equality holds by independence. Substituting the normal entropies gives (10.124), equivalent to the lemma (p. 261). (added step) $\mathbf Y$ has covariance $B+C=A$, so this reads $\tfrac12\log(2\pi e)^n|A|\ge\tfrac12\log(2\pi e)^n|B|$.

**Lemma 10.6.3 (p. 261).** $|K_{X+Z}|\le2^n|K_X+K_Z|$ \tag{10.125}.
Proof. By Lemma 10.6.1, $2(K_X+K_Z)-K_{X+Z}=K_{X-Z}\ge0$ (non-negative definite) \tag{10.126}. By Lemma 10.6.2, $|K_{X+Z}|\le|2(K_X+K_Z)|=2^n|K_X+K_Z|$ \tag{10.127}.

**Theorem 10.6.2 (p. 261).** $C_{n,FB}\le C_n+\tfrac12$ bits per transmission \tag{10.128}.
Proof (p. 261; equations 10.129–10.131 are garbled in the text layer, rebuilt from the justifications the author lists). Start from the upper bound of Theorem 10.6.1: $C_{n,FB}\le\max_{\operatorname{tr}(K_X)\le nP}\frac1{2n}\log\frac{|K_{X+Z}|}{|K_Z|}$. Lemma 10.6.3 bounds this by $\max\frac1{2n}\log\frac{2^n|K_X+K_Z|}{|K_Z|}=\max\frac1{2n}\log\frac{|K_X+K_Z|}{|K_Z|}+\frac12$. By the definition of capacity without feedback this is $\le C_n+\frac12$ \tag{10.129–10.132}.

*Intuition note.* Feedback lets the sender see past noise and use its correlation, but the determinant of the output covariance can grow by at most a factor $2^n$. That is one half bit per use.

### Summary, problems, notes (pp. 262–265)
- The chapter summary (p. 262) restates (10.133)–(10.139): the capacity formulas above, and the feedback bound $C_{n,FB}\le C_n+\frac12$.
- Historical notes (pp. 264–265).
  - Shannon first analyzed the Gaussian channel in his original paper.
  - Holsinger developed the water-filling solution.
  - Pinsker and Ebert showed that feedback at most doubles the capacity of a non-white Gaussian channel.
  - A simple proof of that doubling result can be found in Cover and Pombra. They also show that feedback increases the capacity of the non-white Gaussian channel by at most half a bit.

## Toy example (ours, not from the text)
**Single channel.** Let $P=3$, $N=1$. Then $C=\tfrac12\log_2(1+3/1)=\tfrac12\log_24=1$ bit per use. The sphere-packing bound (10.21) is $\big(\sqrt{n(P+N)}/\sqrt{nN}\big)^n=4^{n/2}=2^n$. For $n=10$ this is at most $1024$ codewords, i.e. rate $10/10=1$ bit per use.

**Two parallel channels.** Let $N_1=1$, $N_2=3$, total power $P=4$. Water-filling needs $(\nu-1)^++(\nu-3)^+=4$. Try $\nu\ge3$: $(\nu-1)+(\nu-3)=2\nu-4=4$, so $\nu=4$. That is $\ge3$, consistent. Then $P_1=3$, $P_2=1$.
- $C=\tfrac12\log_2(1+3/1)+\tfrac12\log_2(1+1/3)=1+\tfrac12\log_2(4/3)=1+\tfrac12(0.4150)\approx1.2075$ bits.
- Compare: all power on channel 1 gives $\tfrac12\log_2(1+4)=\tfrac12(2.3219)\approx1.161<1.2075$.
- With $P=1$ instead: $\nu=2<3$, so channel 2 gets $(2-3)^+=0$, $P_1=1$, and $C=\tfrac12\log_2(1+1)=0.5$ bit.

## Concepts
- [[gaussian-channel]] (new) — $Y=X+Z$ with i.i.d. $\mathcal N(0,N)$ noise independent of $X$, with average power constraint on the input (p. 239).
- [[channel-capacity]] — here $C=\max_{EX^2\le P}I(X;Y)$, and also the supremum of achievable rates (pp. 241–242).
- [[noisy-channel-coding-theorem]] — Theorem 10.1.1: rates below $\frac12\log(1+P/N)$ are achievable; rates above are not (pp. 242–247).
- [[shannon-hartley-formula]] — $C=W\log(1+P/N_0W)$ bits per second for the band-limited white-noise channel (p. 250).
- [[differential-entropy]] — used with $h(Z)=\frac12\log2\pi eN$; the normal maximizes it for given variance (p. 241).
- [[maximum-entropy-principle]] — the normal maximizes entropy for fixed variance; this fixes the optimal input (pp. 241–242).
- [[typical-set-aep]] — joint AEP used in decoding and in the error bound (pp. 244–245).
- [[fanos-inequality]] — gives $H(W|Y^n)\le n\epsilon_n$ in both converses (pp. 246, 259).
- [[power-constraint]] (new) — average energy limit $\frac1n\sum x_i^2\le P$ per codeword; avoids infinite capacity (p. 239).
- [[sphere-packing-argument]] (new) — counting non-overlapping noise spheres inside the received-signal sphere to get $2^{\frac n2\log(1+P/N)}$ codewords (p. 243).
- [[nyquist-shannon-sampling]] (new) — a signal band-limited to $W$ is determined by samples $\frac1{2W}$ s apart; $2W$ degrees of freedom per second (pp. 248–249).
- [[water-filling]] (new) — optimal power $P_i=(\nu-N_i)^+$ over parallel channels; extends to eigenvalues and spectra (pp. 252–256).
- [[coloured-noise-channel]] (new) — Gaussian noise with covariance $K_Z$ and memory; capacity by diagonalizing $K_Z$ (pp. 253–255).
- [[feedback-capacity]] (new) — capacity when the input may depend on past outputs; at most $\frac12$ bit above the no-feedback capacity (pp. 256–261).
- [[hadamard-inequality]] (new) — $|K|\le\prod K_{ii}$ for positive definite $K$, equality iff diagonal (p. 255).

## Canonical instances
- [[binary-antipodal-gaussian]] — $\pm\sqrt P$ signalling gives a BSC with $P_e=1-\Phi(\sqrt{P/N})$ (p. 240).
- [[telephone-line-capacity]] — 3300 Hz, 20 dB SNR gives about 22,000 bit/s; modems reach 19,200 (p. 250).
- [[parallel-channel-water-filling]] — Figure 10.4: power poured into channels of different noise levels (p. 253).
- [[spectral-water-filling]] — Figure 10.5: input spectrum large where the noise spectrum is small (p. 256).

## Bridges (candidates)
- [same-math] Optimal Gaussian input via maximum entropy ↔ information-theory: maximum entropy principle — a normal maximizes entropy for fixed variance.
- [same-math] $C=W\log(1+S/N)$ here ↔ Shannon–Hartley formula in the canon list — the same formula, with $S/N=P/N_0W$.
- [structural-analogy] Water-filling of power over noise levels ↔ rate–distortion: reverse water-filling — both allocate a budget over independent Gaussian components with a common level.

## Questions this raises
- How tight is the sphere-packing argument as a proof, and what replaces it for finite block length?
- Is the half-bit feedback bound ever attained? The text states only the bound and cites Cover and Pombra.
- How do real modulation schemes (e.g. four-level inputs) compare with the capacity bound once the output is quantized?
- What happens when noise is non-Gaussian? Does the Gaussian remain the worst case (cf. Problem 1)?

## Exercises worth doing
- Ex. 1 (p. 263) — mutual information game: show the saddlepoint conditions (10.142) for $X^*\sim\mathcal N(0,P)$, $Z^*\sim\mathcal N(0,N)$; uses the entropy power inequality — difficulty: hard
- Ex. 2 (p. 263) — two independent looks at $Y$: $I(X;Y_1,Y_2)=2I(X;Y_1)-I(Y_1;Y_2)$, and capacity is less than twice the single-look capacity — difficulty: medium
- Ex. 3 (p. 264) — two-look Gaussian channel with correlated noise; find $C$ for $\rho=1,0,-1$ — difficulty: medium
- Ex. 4 (p. 264) — parallel channels: at what power does the pair stop behaving like a single channel and start behaving like two? — difficulty: easy

## Reading notes
- The PDF is the 1991 first edition (Wiley, copyright line on p. 239, "Print ISBN 0-471-06259-6"), not the 2006 second edition cited in the metadata. Numbering and content may differ from the 2nd edition.
- Page offset: printed = pdf − 22.
- Text layer is heavily garbled in equations. I checked against page images where they were provided (printed pp. 240–247, 249–260, 262–264). No image of printed pp. 239, 248, 261 or 265 was provided; those pages rest on the text layer only, and equations 10.53–10.55 (p. 248) are `[unreadable p. 248]`.
- Because no image of p. 261 was provided, everything on it (Lemma 10.6.3, Theorem 10.6.2) is read from the text layer only; equations 10.124 and 10.129–10.131 are garbled there. I rebuilt them from the author's own prose and stated justifications, marked as such.
- Lemma 10.6.2 is stated for positive definite $A-B$, but Lemma 10.6.3 applies it to a non-negative definite matrix $K_{X-Z}$. The source does not comment on this.
- In (10.69) the text writes $\sum P_i=P$ (equality) while the constraint is $\le P$; I followed the printed text.
- Section 10.6 mentions "the next section" for a feedback converse (p. 257); in these pages the converse (Theorem 10.6.1) is in the same section.
