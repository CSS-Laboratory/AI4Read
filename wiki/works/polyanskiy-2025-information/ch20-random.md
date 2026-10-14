---
id: polyanskiy-2025-information/ch20-random
work: polyanskiy-2025-information
unit: "Chapter 18 (unit label ch20) — Random and maximal coding"
pages: 350-369
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Random and maximal coding

## L0 — One line
Good channel codes exist because the information density of the channel lets us bound the error of randomly drawn codebooks (Shannon, DT, RCU, Gallager) or greedily grown ones (Feinstein), and submodularity explains why both are near-optimal.

## L1 — The gist (≤ 120 words)
How can we show that good codes exist, when searching over encoders $f:[M]\to\mathcal X$ has no statistical analog? Test each codeword against the "average background" $P_Y$. This brings in the information density $i(x;y)$. Averaging over random codebooks gives achievability bounds: Shannon's, the DT bound, RCU and Gallager's. Feinstein's greedy construction gives almost the same bound. For additive-noise channels, random linear codes satisfy the same DT bound as fully random codes. The reason both methods work is that decoding success is a submodular function of the codebook, so greedy and random selection are near-optimal. This matters because these bounds later give capacity and dispersion.

**Prerequisites:** binary hypothesis testing (likelihood ratio, Neyman–Pearson); union bound; conditional expectation; finite fields and linear algebra over $\mathbb F_q$; submodular set functions.

## L2 — Key ideas
- The information density $i(x;y)=\log\frac{dP_{X,Y}}{dP_XP_Y}$ has mean $I(X;Y)$. It also obeys the tail bound $\mathbb P[i(\bar X;Y)>t]\le e^{-t}$ for an independent copy $\bar X$ (pp. 351–353).
- Shannon's bound: a threshold decoder plus a random codebook gives $\epsilon\le\mathbb P[i(X;Y)\le\log M+\tau]+e^{-\tau}$. Averaging over codebooks shows that some codebook is at least as good (p. 354–355).
- The DT bound removes the free parameter $\tau$. It equals $\mathbb E\,e^{-(i(X;Y)-\log\frac{M-1}{2})^+}$, and it equals $\frac{M+1}{2}$ times the minimum error of a Bayesian dependence test (pp. 356–357).
- Feinstein's greedy construction gives a code with *maximal* error $\epsilon\le\mathbb P[i<\log\gamma]+M/\gamma$. This has the same form as Shannon's bound (pp. 357–359).
- The RCU bound analyses the ML decoder and caps the union bound at 1 after conditioning on $(X,Y)$. Gallager's bound weakens RCU with the $\rho$-trick and gives error exponents (pp. 359–361).
- For additive-noise channels, an ML "syndrome decoder" exists for linear codes. Hence $P_e=P_{e,\max}$, and a random linear code with dithering satisfies the DT bound (pp. 362–365).
- The DT and Shannon bounds still hold when the codewords are only pairwise independent (p. 357). This allows ensembles with much less randomness than Shannon's (pp. 365–366).
- Greedy and random coding are near-optimal because $S(\mathcal C)=\sum_y\max_{x\in\mathcal C}P_{Y|X}(y|x)$ is submodular (pp. 366–369).

## L3 — Walkthrough

### Introduction (p. 350)
- Once the codebook $\{c_i=f(i)\}$ is fixed, decoding is M-ary hypothesis testing. Choosing $f$ has no exact statistical analog. The closest is design of experiments (p. 350).
- A simplification: run $M$ binary tests of $P_{Y|X=c_m}$ against the "average background noise" $P_Y$. By Neyman–Pearson (Theorem 14.11) the optimal test thresholds $\log\frac{P_{Y|X=x}}{P_Y}$ (p. 350).
- Notation: independent pairs $(X,Y)\perp\!\!\!\perp(\bar X,\bar Y)$ with
$$P_{X,Y,\bar X,\bar Y}(a,b,\bar a,\bar b)=P_X(a)P_{Y|X}(b|a)P_X(\bar a)P_{Y|X}(\bar b|\bar a).\tag{18.1}$$
$X$ is the sent and $\bar X$ the unsent codeword (p. 350).

### 18.1 Information density (pp. 351–353)
- **Definition 18.1.** Take $P_{X,Y},P_XP_Y\ll\mu$, with $f=\frac{dP_{X,Y}}{d\mu}$ and $\bar f=\frac{dP_XP_Y}{d\mu}$. Then
$$i_{P_{X,Y}}(x;y)\triangleq \mathrm{Log}\frac{f(x,y)}{\bar f(x,y)}=\begin{cases}\log\frac{f}{\bar f}& f>0,\bar f>0\\ +\infty & f>0,\bar f=0\\ -\infty & f=0,\bar f>0\\ 0& f=\bar f=0.\end{cases}\tag{18.2}$$
If $P_{X,Y}\ll P_XP_Y$, simply $i(x;y)=\log\frac{dP_{X,Y}}{dP_XP_Y}(x,y)$. The channel $P_{Y|X}$ is fixed, so $i$ depends only on $P_X$, and the subscript is dropped. In machine learning $i$ is called pointwise mutual information (p. 351).
- **Proposition 18.2.** $\mathbb E[i(X;Y)]$ is well-defined and non-negative (possibly infinite), and $I(X;Y)=\mathbb E[i(X;Y)]$ (p. 351).
- **Proposition 18.3 (conditioning–unconditioning trick).** Let $\bar X\perp\!\!\!\perp(X,Y)$ be a copy of $X$.
  1. For any $f:\mathcal X\times\mathcal Y\to\mathbb R$: $\mathbb E[f(\bar X,Y)\mathbf 1\{i(\bar X;Y)>-\infty\}]=\mathbb E[f(X,Y)\exp\{-i(X;Y)\}]$ (18.3).
  2. For non-negative $f_+$ and $P_X$-a.e. $x$: $\mathbb E[f_+(\bar X,Y)\mathbf 1\{i(\bar X;Y)>-\infty\}\mid\bar X=x]=\mathbb E[f_+(X,Y)e^{-i(X;Y)}\mid X=x]$ (18.4) (p. 352).
  - Proof of (1) is a restatement of (14.5). For (2), let $a(x)$ and $b(x)$ be the left and right conditional expectations. Assume $f_+$ is bounded. Let $S_\epsilon=\{a\ge b+\epsilon\}$. Apply (18.3) to $f_+\mathbf 1\{x\in S_\epsilon\}$ to get $\mathbb E[b(X)\mathbf 1_{S_\epsilon}]=\mathbb E[a(\bar X)\mathbf 1_{S_\epsilon}]\ge\mathbb E[b(X)\mathbf 1_{S_\epsilon}]+\epsilon P_X[S_\epsilon]$. So $P_X[S_\epsilon]=0$. The symmetric argument gives $b\le a$. Unbounded $f_+$ follows by truncating at $n$ and using monotone convergence (p. 352–353).
- **Corollary 18.4 (information tails).** For $P_X$-a.e. $x$: $\mathbb P[i(x;Y)>t]\le e^{-t}$ (18.5), and $\mathbb P[i(\bar X;Y)>t]\le e^{-t}$ (18.6). Take $f_+=\mathbf 1\{i>t\}$ in (18.4). This is the same estimate as $Q[\log\frac{dP}{dQ}\ge t]\le e^{-t}$ (18.7) in hypothesis testing, and as $|\{x:\log P_X(x)\ge t\}|\le e^{-t}$ in compression (p. 353).

*Intuition note.* $i(x;y)$ measures how much more likely $y$ is given $x$ than on average. An unrelated input rarely gets a high score. The tail bound $e^{-t}$ says this precisely. The Shannon and Feinstein proofs use it directly, and the DT and Gallager proofs use the related identity (18.3)/(18.4).

### 18.2 Shannon's random coding bound (pp. 353–355)
- Shannon placed codewords at random to test whether error correction is possible. The method is optimal asymptotically and almost optimal non-asymptotically; it is an instance of Erdős's probabilistic method (p. 353).
- For discrete alphabets the ML decoder is
$$g^*(y)=\arg\max_m P_{X|Y}(c_m|y)=\arg\max_m P_{Y|X}(y|c_m)=\arg\max_m i(c_m;y).\tag{18.8}$$
This holds for any $P_X$ used to define $i$. A threshold on $i(c_m;y)$ evaluates $c_i$ against $P_Y$, which approximates the average of the other $M-1$ codewords. $P_X$ is chosen to maximize $I(X;Y)$ (pp. 353–354).
- **Theorem 18.5 (Shannon).** Fix $P_{Y|X}$ and any $P_X$. For every $\tau>0$ there is an $(M,\epsilon)$-code with
$$\epsilon\le\mathbb P[i(X;Y)\le\log M+\tau]+\exp(-\tau).\tag{18.9}$$
- **Proof.**
  - Use the suboptimal decoder $g(y)=m$ if $c_m$ is the unique codeword with $i(c_m;y)\ge\log M+\tau$, and $g(y)=\mathrm e$ otherwise (18.10). The output e always counts as an error (p. 354).
  - Draw $c_m\sim P_X$ i.i.d. By symmetry we may condition on $W=1$. Then
$$\begin{aligned}\mathbb E[P_e]&\le\mathbb P[i(c_1;Y)\le\log M+\tau\mid W=1]+\sum_{\bar m=2}^M\mathbb P[i(c_{\bar m};Y)>\log M+\tau\mid W=1]\quad\text{(union bound)}\\&\overset{(a)}=\mathbb P[i(X;Y)\le\log M+\tau]+(M-1)\mathbb P[i(\bar X;Y)>\log M+\tau]\\&\le\mathbb P[i(X;Y)\le\log M+\tau]+(M-1)e^{-(\log M+\tau)}\le\mathbb P[i(X;Y)\le\log M+\tau]+e^{-\tau}.\end{aligned}$$
  - Step (a) holds because given $W=1$ and $\bar m\ne1$, $(c_1,c_{\bar m},Y)\overset d=(X,\bar X,Y)$. The inequality after (a) uses (18.6). Since the average over codebooks meets the bound, at least one codebook does (p. 355).
- **Remark 18.2.** For iid inputs and memoryless channels, classical decoders use "joint typicality" (empirical joint distribution $\hat P_{x^n,y^n}\approx P_{X_1,Y_1}$) or "entropic typicality". The event $\{i(x^n;y^n)\ge n\gamma_1\}$ is a version that works for much more general channels (p. 355).

*Intuition note.* The true codeword scores above $\log M+\tau$ unless the channel is unusually noisy. Each of the $M-1$ wrong codewords passes the threshold with probability at most $e^{-\log M-\tau}$. So the expected number of impostors is at most $e^{-\tau}$.

### 18.3 Dependence-testing (DT) bound (pp. 356–357)
- **Theorem 18.6.** Fix $P_{Y|X}$ and any $P_X$. There is an $(M,\epsilon)$-code with
$$\epsilon\le\mathbb E\Big[\exp\Big\{-\Big(i(X;Y)-\log\tfrac{M-1}{2}\Big)^+\Big\}\Big],\quad x^+=\max(x,0).\tag{18.11}$$
(The printed statement says "for every $\tau>0$", but $\tau$ does not appear in the bound.)
- **Proof.** Fix $\gamma$. Decoder: output the smallest $m$ with $i(c_m;y)\ge\gamma$, else e. Given a codebook, the union bound gives $\mathbb P[\hat W\ne j|W=j]\le\mathbb P[i(c_j;Y)\le\gamma|W=j]+\sum_{k=1}^{j-1}\mathbb P[i(c_k;Y)>\gamma|W=j]$. Average over random codebooks:
$$\begin{aligned}\mathbb E[P_e]&\le\tfrac1M\sum_{j=1}^M\Big(\mathbb P[i(X;Y)\le\gamma]+\sum_{k=1}^{j-1}\mathbb P[i(\bar X;Y)>\gamma]\Big)=\mathbb P[i(X;Y)\le\gamma]+\tfrac{M-1}{2}\mathbb P[i(\bar X;Y)>\gamma]\\&=\mathbb P[i(X;Y)\le\gamma]+\tfrac{M-1}{2}\mathbb E[e^{-i(X;Y)}\mathbf 1\{i(X;Y)>\gamma\}]\quad\text{(by (18.3))}\\&=\mathbb E\Big[\mathbf 1\{i\le\gamma\}+\tfrac{M-1}2e^{-i}\mathbf 1\{i>\gamma\}\Big].\end{aligned}$$
  - Since $U\mathbf 1_E+V\mathbf 1_{E^c}\ge\min\{U,V\}$, the integrand is $\ge\min(1,\frac{M-1}2e^{-i})$. Equality holds for $\gamma=\log\frac{M-1}2$, whatever $(x,y)$ is. So $\inf_\gamma\mathbb E[P_e]\le\mathbb E\min(1,\frac{M-1}2e^{-i(X;Y)})$, which equals (18.11) (pp. 356–357).
- **Remark 18.3.** The RHS of (18.11) is $\frac{M+1}2$ times the minimum Bayesian error of testing $H_0:(X,Y)\sim P_{X,Y}$ versus $H_1:(X,Y)\sim P_XP_Y$ (the unsent $\bar X$ with $Y$). The priors are $\pi_0=\frac2{M+1}$, $\pi_1=\frac{M-1}{M+1}$. The best threshold is $\log\frac{\pi_1}{\pi_0}$, as found above. No minimization over $\tau$ is needed. The DT bound can be shown stronger than Shannon's with optimized $\tau$ (Exercise IV.5). Both bounds hold unchanged if codewords are not iid but have the right marginal and are pairwise independent (Theorem 18.13) (p. 357).

*Intuition note.* Decoding becomes a test of "sent versus unsent codeword". The bound is the error of the best such test, scaled by $(M+1)/2$.

### 18.4 Feinstein's maximal coding bound (pp. 357–359)
- Feinstein's method is greedy rather than probabilistic. It gives an $(M,\epsilon)_{\max}$-code, i.e. one with *maximal* error probability at most $\epsilon$. Footnote 2: this is not a serious advantage, since from an $(M,\epsilon)$ code one can extract an $(M',\epsilon')_{\max}$ subcode with smaller $M'$ and larger $\epsilon'$ (Theorem 19.4) (p. 357).
- **Theorem 18.7 (Feinstein's lemma).** For every $\gamma>0$ and $\epsilon\in(0,1)$ there is an $(M,\epsilon)_{\max}$-code with
$$M\ge\gamma\big(\epsilon-\mathbb P[i(X;Y)<\log\gamma]\big).\tag{18.12}$$
- **Remark 18.4.** Equivalently, for fixed $M$ there is such a code with $\epsilon\le\mathbb P[i(X;Y)<\log\gamma]+\frac M\gamma$. With $\log\gamma=\log M+\tau$ this has exactly the form of (18.9). The two methods give essentially the same bound, apart from average versus maximal error (pp. 357–358).
- **Proof.**
  - Goal: codewords $c_1,\dots,c_M$ and disjoint decoding regions $D_i$ with $P_{Y|X}(D_i|c_i)\ge1-\epsilon$. Define preliminary regions $E_x=\{y:i(x;y)\ge\log\gamma\}$, which may overlap. By Corollary 18.4 there is $F\subset\mathcal X$ with $P_X[F]=1$ and $P_Y(E_x)\le1/\gamma$ for all $x\in F$ (18.13) (p. 358).
  - Assume $\mathbb P[i<\log\gamma]\le\epsilon$, otherwise (18.12) is trivial. Some $c\in F$ has $P_{Y|X}(E_c|c)\ge1-\epsilon$. Otherwise averaging over $c\sim P_X$ would give $\mathbb P[i(X;Y)\ge\log\gamma]<1-\epsilon$, a contradiction (p. 358).
  - Greedy step: pick $c_1\in F$ with $P_{Y|X}(E_{c_1}|c_1)\ge1-\epsilon$ and set $D_1=E_{c_1}$. Pick $c_2\in F$ with $P_{Y|X}(E_{c_2}\setminus D_1|c_2)\ge1-\epsilon$ and set $D_2=E_{c_2}\setminus D_1$, and so on. Stop when no further $c$ qualifies. The stopping condition is $\forall c\in F$, $P_{Y|X}(E_c\setminus\cup_{j=1}^MD_j|c)<1-\epsilon$ (p. 358).
  - Average over $c\sim P_X$: $\mathbb P[i(X;Y)\ge\log\gamma,\ Y\notin\cup D_j]<1-\epsilon$. Equivalently $\epsilon<\mathbb P[i<\log\gamma\text{ or }Y\in\cup D_j]$. By the union bound and $D_j\subset E_{c_j}$ with (18.13): $\epsilon<\mathbb P[i<\log\gamma]+\sum_jP_Y(D_j)\le\mathbb P[i<\log\gamma]+\sum_jP_Y(E_{c_j})\le\mathbb P[i<\log\gamma]+M/\gamma$ (p. 359).

*Intuition note.* Each new codeword claims a region of output space of $P_Y$-size at most $1/\gamma$. Once $M\approx\gamma\times$(fraction served) regions are used up, no room is left, and this gives the bound.

### 18.5 RCU and Gallager's bound (pp. 359–361)
These bounds analyse the optimal (ML) decoder instead of a threshold decoder (p. 359).
- **Theorem 18.8 (RCU).** For every integer $M\ge1$ there is an $(M,\epsilon)$-code with
$$\epsilon\le\mathbb E\Big[\min\big\{1,(M-1)\,\mathbb P[i(\bar X;Y)\ge i(X;Y)\mid X,Y]\big\}\Big].\tag{18.14}$$
- **Proof.**
  - For a codebook, the ML decoder gives $\epsilon\le\frac1M\sum_m\mathbb P[\cup_{j\ne m}\{i(c_j;Y)\ge i(c_m;Y)\}|X=c_m]$. This is pessimistic: ties are counted as errors (p. 359).
  - Average over $c_j\sim P_X$ i.i.d. Condition on $W=1$, so $(c_1,Y,c_2,\dots,c_M)\sim P_{X,Y}\prod_{j\ge2}P_X$. Then (a) condition on $(c_1,Y)=(x,y)$, and (b) apply the union bound capped at 1:
$$\mathbb P[\cup_{j=2}^M\{i(c_j;Y)\ge i(c_1;Y)\}\mid W=1]\overset{(a)}=\mathbb E_{(x,y)}\mathbb P[\cdots\mid c_1=x,Y=y]\overset{(b)}\le\mathbb E\min\{1,(M-1)\mathbb P[i(\bar X;Y)\ge i(X;Y)|X,Y]\}.$$
  - Step (b) uses $\mathbb P[\cup E_j]\le\min\{1,\sum_j\mathbb P[E_j]\}$. The cleverness is conditioning on $(c_1,Y)$ first. Applying the union bound from the start would give a much weaker estimate that would not achieve capacity (p. 360).
- Shannon's bound (18.9) is a weakening of (18.14): split the expectation on $\{i\le\log M+\tau\}$ and bound $\min\{x,1\}$ by 1 there and by $x$ elsewhere (p. 360).
- **Theorem 18.9 (Gallager).** For $\rho\in[0,1]$ there is an $(M,\epsilon)$-code with
$$\epsilon\le M^\rho\,\mathbb E\Big[\Big(\mathbb E\Big[\exp\frac{i(\bar X;Y)}{1+\rho}\,\Big|\,Y\Big]\Big)^{1+\rho}\Big].\tag{18.15}$$
- **Proof.**
  - Proposition 18.3 with $f_+=\exp\{\frac{i(x;y)}{1+\rho}\}$ and $X,Y$ interchanged, plus $(X,\bar Y)\overset d=(\bar X,Y)$, gives for $P_Y$-a.e. $y$
$$\mathbb E[e^{-i(X;Y)\frac\rho{1+\rho}}|Y=y]=\mathbb E[e^{i(\bar X;Y)\frac1{1+\rho}}|Y=y].\tag{18.16}$$
  - Use $\min\{t,1\}\le t^\rho$ for $t\ge0$ (18.17) in (18.14): $\epsilon\le M^\rho\mathbb E[\mathbb P[i(\bar X;Y)>i(X;Y)|X,Y]^\rho]$ (18.18) (p. 361).
  - Chernoff: $\mathbb P[i(\bar X;Y)>i(X;Y)|X,Y]\le e^{-i(X;Y)/(1+\rho)}\mathbb E[e^{i(\bar X;Y)/(1+\rho)}|Y]$. Raise to the power $\rho$ and take $\mathbb E[\cdot|Y]$: this is at most $\mathbb E^\rho[e^{i(\bar X;Y)/(1+\rho)}|Y]\cdot\mathbb E[e^{-\frac\rho{1+\rho}i(X;Y)}|Y]$. By (18.16) the last factor equals $\mathbb E[e^{i(\bar X;Y)/(1+\rho)}|Y]$. So the result is $\mathbb E^{1+\rho}[\cdots|Y]$, and plugging into (18.18) gives (18.15) (p. 361).
- The step (18.17) is the **$\rho$-trick**, a version of the union bound: $\mathbb P[\cup E_j]\le\min\{1,\sum_j\mathbb P[E_j]\}\le(\sum_j\mathbb P[E_j])^\rho$ for $0\le\rho\le1$. For memoryless channels with iid inputs, (18.15) optimized over $\rho$ gives $\epsilon\le\exp\{-nE_r(R)\}$, with $R=\frac{\log M}n$ and $E_r$ Gallager's random coding exponent. So the error vanishes exponentially fast in blocklength (Section 22.4*, not covered here) (p. 361).

### 18.6 Linear codes (pp. 362–366)
- A pleasant property of linear codes is $P_e=P_{e,\max}$ (p. 362).
- **Definition 18.10.** With $\mathcal X=\mathcal Y=\mathbb F_q^n$, a codebook $\mathcal C=\{c_u:u\in\mathbb F_q^k\}$ of size $M=q^k$ is *linear* if it is a $k$-dimensional subspace of $\mathbb F_q^n$. It is described by a generator matrix $G\in\mathbb F_q^{k\times n}$, with $c_u=uG$ and $\mathcal C=\mathrm{Im}(G)$. Equivalently it is the nullspace of a parity-check matrix $H\in\mathbb F_q^{(n-k)\times n}$: $Hc^\top=0$ for all $c\in\mathcal C$. Hence $HG^\top=0$ (p. 362).
- **Example 18.1 (Hamming $[7,4,3]_2$).**
$$G=\begin{bmatrix}1&0&0&0&1&1&0\\0&1&0&0&1&0&1\\0&0&1&0&0&1&1\\0&0&0&1&1&1&1\end{bmatrix},\quad H=\begin{bmatrix}1&1&0&1&1&0&0\\1&0&1&1&0&1&0\\0&1&1&1&0&0&1\end{bmatrix}.$$
The code is systematic ($G=[I;P]$, $H=[-P^\top;I]$). Each row of $H$ is a circle in the Venn picture whose four bits sum to zero. Minimum distance is 3, so it corrects 1 bit error and detects 2 (pp. 362–363).
- **Definition 18.11.** A channel is *additive-noise* if $P_{Y|X}(y|x)=P_Z(y-x)$ for a random vector $Z\in\mathbb F_q^n$, i.e. $Y=X+Z$ with $Z\perp\!\!\!\perp X$ (p. 363).
- **Theorem 18.12.** For a linear code over an additive-noise channel there is an ML decoder with: (1) $g(y)=y-g_{\rm synd}(Hy^\top)$, where $g_{\rm synd}(s)\triangleq\arg\max_{z:Hz^\top=s}P_Z(z)$ (it decodes the most likely noise); (2) decoding regions are translates $D_u=c_u+D_0$ with $D_0=\mathrm{Im}(g_{\rm synd})$; (3) $P_{e,\max}=P_e$. So the syndrome $Hy^\top$ is a sufficient statistic (p. 363). (The printed statement writes $[k,n]$ and $g:\mathbb F_q^n\to\mathbb F_q^k$; the formula in (1) returns an element of $\mathbb F_q^n$.)
- **Proof.** (1) $g(y)=\arg\max_{c:Hc^\top=0}P_Z(y-c)=y-\arg\max_{z:Hz^\top=Hy^\top}P_Z(z)$. (2) $D_u=\{y:y-g_{\rm synd}(Hy^\top)=c_u\}=\{y:y-c_u=g_{\rm synd}(H(y-c_u)^\top)\}=c_u+D_0$, using $Hc_u^\top=0$ and $c_0=0$. (3) $\mathbb P[\hat W\ne u|W=u]=\mathbb P[g_{\rm synd}(HZ^\top)\ne Z]$, which does not depend on $u$ (p. 363).
- **Remark 18.5 (BSC).** For $\mathrm{BSC}_\delta^{\otimes n}$ with $\delta<1/2$, $g_{\rm synd}(s)=\arg\min_{z:Hz^\top=s}w_H(z)$. The elements of $D_0$ are "minimal weight coset leaders". Counting them by weight is a hard open problem even for Reed–Muller codes. In Hamming space $D_0$ resembles a Voronoi region and the $D_u$ form a tessellation. Linearity was historically valued for cheap encoding and slightly cheaper ML decoding. For long codes syndrome decoding is impractical, so practical codes now have fast suboptimal decoders (pp. 363–364).
- **Theorem 18.13 (DT bound for linear codes).** For additive-noise $P_{Y|X}$ over $\mathbb F_q^n$ and any $k\ge1$ there is a linear code with
$$P_{e,\max}=P_e\le\mathbb E\Big[q^{-\left(n-k-\log_q\frac1{P_Z(Z)}\right)^+}\Big].\tag{18.19}$$
It is Theorem 18.6 with $P_X=\mathrm{Unif}(\mathbb F_q^n)$ (Remark 18.6) (p. 364).
- **Proof.** Take $P_X$ uniform and $M=q^k$.
  - *Step 1 (dithering).* $c_u=uG+h$, with the entries of $G$ ($k\times n$) and $h$ ($1\times n$) i.i.d. uniform on $\mathbb F_q$. The shift removes the special role of the zero codeword (p. 364).
  - *Step 2.* For $u\ne u'$, $(c_u,c_{u'})$ is uniform on pairs, $P_{X,\bar X}=1/q^{2n}$. Indeed $c_u$ is uniform given $G$ because of $h$, and $c_{u'}=c_u+(u'-u)G$ with $(u'-u)G$ uniform given $c_u$. So the codewords are pairwise independent and uniform (p. 365).
  - *Step 3.* The DT argument is repeated for symmetric, pairwise independent codewords: $\mathbb E[P_e]\le\mathbb E[q^{-(i(X;Y)-\log_q\frac{q^k-1}2)^+}]\le\mathbb E[q^{-(i(X;Y)-k)^+}]$, with logs in base $q$.
  - *Step 4.* $i(a;b)=\log_q\frac{P_Z(b-a)}{q^{-n}}=n-\log_q\frac1{P_Z(b-a)}$. Hence $P_e\le\mathbb E[q^{-(n-k-\log_q\frac1{P_Z(Z)})^+}]$ (18.20).
  - *Step 5 (remove dithering).* Encode $u\mapsto uG$ and decode with $g'(Y)=g(Y+h)$. Additivity of the channel makes the error probability the same, so a non-dithered linear code satisfies (18.20) (p. 365).
- **Ensembles** (p. 365): *Shannon* (fully random iid codewords); *Elias* ($\{uG\}$, $G$ uniform; used in Theorem 18.13); *Gallager* ($\{c:Hc^\top=0\}$, $H$ uniform; not the same as Elias). Elias's $G$ may fail to be full rank, giving identical codewords and $P_{e,\max}\ge1/2$. Fix: take $G$ (or $H$) uniform over full-rank matrices. Then $P_{X,\bar X}=\frac1{q^{2n}-q^n}\mathbf 1\{X\ne X'\}$, which is not pairwise independent (p. 366).
- The Elias ensemble with dithering has $H(c_1,\dots,c_M)=H(G)+H(h)=(nk+n)\log q$. The Shannon ensemble has $q^kn\log q$. Any pairwise-independent uniform ensemble has entropy $\ge H(c_1,c_2)=2n\log q$. The Wozencraft ensemble (Exercise IV.7, $n=2k$, pairs of distinct elements) achieves about $2n\log q$ (p. 366).

*Intuition note.* In the DT bound, linear codes lose nothing relative to fully random codes. The DT and Shannon bounds still hold with only pairwise independent codewords, and a random linear code with dithering provides these using far fewer random bits.

### 18.7 Why random and maximal coding work well (pp. 366–369)
Two questions, answered via Barman–Fawzi [36]: (1) why is the greedy procedure near-optimal? (2) why is random coding with a *simple* $P_X$ near-optimal? "Simple" means a product distribution for a memoryless channel, or uniform $P_X$ for additive noise $Y^n=X^n+Z^n$ with arbitrary $Z^n$ (pp. 366–367).
- For discrete $\mathcal Y$, define $S(\mathcal C)\triangleq\sum_{y}\max_{x\in\mathcal C}P_{Y|X}(y|x)$, $S(\emptyset)=0$. It is non-decreasing and submodular, as a sum of such functions ($T\mapsto\max_{x\in T}\phi(x)$ is submodular). Since $P_{e,MAP}(\mathcal C)=1-\frac1{|\mathcal C|}S(\mathcal C)$, finding a minimal-error codebook is equivalent to maximizing $S$. Write $S^*(M)=\max_{|\mathcal C|\le M}S(\mathcal C)$ (p. 367).
- **Greedy.** $\mathcal C_0=\emptyset$, $x_{t+1}\in\arg\max_{x\notin\mathcal C_t}S(\mathcal C_t\cup\{x\})$, $\mathcal C_{t+1}=\mathcal C_t\cup\{x_{t+1}\}$. The work [313] showed $S(\mathcal C_t)\ge(1-1/e)\max_{|\mathcal C|=t}S(\mathcal C)$ (p. 367).
- **Theorem 18.14 ([313]).** For non-negative submodular $f$ and a greedy sequence, for all $\ell,t$: $f(\mathcal C_\ell)\ge(1-e^{-\ell/t})\max_{|\mathcal C|=t}f(\mathcal C)$ (p. 368).
- Applied to $S$, a greedy codebook $\mathcal C'$ with $M'$ codewords satisfies $1-P_{e,MAP}(\mathcal C')\ge\frac M{M'}(1-e^{-M'/M})(1-\epsilon^*(M))$. With $M'=M2^{-10}$ the success probability is $\ge0.9995(1-\epsilon^*(M))$. So a greedy code carrying 10 bits fewer than the best code loses at most $5\cdot10^{-4}$ in error probability. Caveat: Feinstein's bound uses a suboptimal decoder, not MAP (p. 368).
- **Random coding.** Extend $S$ to $[0,1]^{|\mathcal X|}$:
$$S_{LP}(\pi)=\sup\Big\{\sum_{x,y}P_{Y|X}(y|x)r_{x,y}:0\le r_{x,y}\le\pi_x,\ \sum_xr_{x,y}\le1\Big\}.\tag{18.21}$$
$S_{LP}(\mathbf 1_{\mathcal C})=S(\mathcal C)$ and $S_{LP}$ is concave. So
$$S^*(M)\le S^*_{LP}(M)\triangleq\max\{S_{LP}(\pi):0\le\pi_x\le1,\ \textstyle\sum_x\pi_x\le M\}.\tag{18.22}$$
This bound coincides with the meta-converse (Section 22.3). [313] also showed $S(\mathcal C_M)\ge(1-e^{-1})S^*_{LP}(M)$ (18.23), an integrality-gap result: $(1-e^{-1})S^*_{LP}(M)\le S^*(M)\le S^*_{LP}(M)$. More generally $S(\mathcal C_{M'})\ge(1-e^{-M'/M})S^*_{LP}(M)$ (p. 368). Footnote 3: $S_{LP}$ is not any of the standard extensions (Lovász, least concave, multilinear) and is in general strictly larger than the least concave one.
- **Theorem 18.15 ([36]).** Fix $\pi\in[0,1]^{|\mathcal X|}$, $M=\sum_x\pi_x$, and $\mathcal C=\{c_1,\dots,c_{M'}\}$ with $c_j\sim P_X(x)=\pi_x/M$ i.i.d. Then $\mathbb E[S(\mathcal C)]\ge(1-e^{-M'/M})S_{LP}(\pi)$ (p. 369).
- **Lemma 18.16.** Let $g:\mathcal X\to\mathbb R$ and $T(\pi,g)=\max\{\sum_xr_xg(x):0\le r_x\le\pi_x,\sum_xr_x=1\}$. Then $\mathbb E[\max_{x\in\mathcal C}g(x)]\ge(1-e^{-M'/M})T(\pi,g)$. Apply it with $g=P_{Y|X}(y|\cdot)$ and sum over $y$ to get Theorem 18.15.
  - *Proof.* Take $\mathcal X=[m]$ with $g(1)\ge\dots\ge g(m)\ge g(m+1)\triangleq0$. Let $a=1-(1-\frac1M)^{M'}\ge1-e^{-M'/M}$ and $b(j)=\mathbb P[\{1,\dots,j\}\cap\mathcal C\ne\emptyset]$. Then $\mathbb P[\max g=g(j)]=b(j)-b(j-1)$, and summation by parts gives
$$\mathbb E[\max_{x\in\mathcal C}g(x)]=\sum_{j=1}^m(g(j)-g(j+1))b(j).\tag{18.24}$$
With $c(j)=\min(\sum_{i\le j}\pi_i,1)$: $b(j)=1-(1-\frac{\pi_1+\dots+\pi_j}M)^{M'}\ge1-(1-\frac{c(j)}M)^{M'}$. (The printed exponent is $\ell$; this is evidently a misprint for $M'$, since the next expression uses $M'$.) From $(1-\frac xM)^{M'}\le1-ax$ for $x\in[0,1]$ we get $b(j)\ge a\,c(j)$. Plug in; $r_j=c(j)-c(j-1)$ attains the maximum in $T(\pi,g)$ (p. 369).
- Conclusion: random and greedy coding are both almost optimal for $S^*(M)$. The best random-coding distribution is the one attaining $S^*_{LP}(M)$. For input-symmetric channels (e.g. additive noise) the optimal $\pi$ is constant, so codewords are drawn iid uniformly on $\mathcal X$ (p. 369).

*Intuition note.* Adding a codeword helps less the more codewords you already have, and this is submodularity. Under such diminishing returns, greedy growth and independent random picks both capture a constant fraction $1-e^{-\text{ratio}}$ of the best possible gain. So the two methods yield nearly the same bound.

## Toy example (ours)
Channel: BSC with $\delta=0.1$, one use ($n=1$), $\mathcal X=\mathcal Y=\{0,1\}$, uniform $P_X$, $M=2$, logs base 2. Then $P_Y$ is uniform, so $i(x;y)=\log_2\frac{P(y|x)}{1/2}$:
- $y=x$ (prob. 0.9): $i=\log_2 1.8\approx0.848$.
- $y\ne x$ (prob. 0.1): $i=\log_2 0.2\approx-2.322$.

*DT bound (18.11).* $\frac{M-1}2=0.5$ and $e^{-i}\to2^{-i}$. For $y=x$: $0.5/1.8=0.2778<1$. For $y\ne x$: $0.5\cdot5=2.5$, capped at 1. Bound $=0.9(0.2778)+0.1(1)=0.25+0.1=0.35$.

*Actual average error of the DT decoder* ($\gamma=\log_2 0.5=-1$; "$i\ge\gamma$" means $y=c_m$; decoder outputs the first $m$ with $y=c_m$). Codebook $(c_1,c_2)$ is uniform on 4 pairs.
- Distinct pair (prob. 1/2): $W=1$ errs iff $y\ne c_1$ (0.1); $W=2$ errs iff $y=c_1$, which means $y\ne c_2$ (0.1). Error $=0.1$.
- Identical pair (prob. 1/2): $W=1$ errs w.p. 0.1; $W=2$ always errs (output 1 or e). Mean error $=(0.1+1)/2=0.55$.
- Average $=0.5(0.1)+0.5(0.55)=0.325\le0.35$.

So the average over random codebooks is below the bound. Some codebook is at least as good as the average. Here the distinct pair has error 0.1.

## Concepts
- [[information-density]] (new) — $i(x;y)=\log\frac{dP_{X,Y}}{dP_XP_Y}$; its mean is $I(X;Y)$; also called pointwise mutual information (p. 351)
- [[mutual-information]] — $I(X;Y)=\mathbb E[i(X;Y)]$ (p. 351)
- [[noisy-channel]] — a fixed $P_{Y|X}$; the encoder is the design variable (p. 350)
- [[error-correcting-code]] — an $(M,\epsilon)$-code: codebook plus decoder with error at most $\epsilon$; "max" versions bound the worst message (pp. 350, 357)
- [[random-coding-bound]] (new) — average error over random codebooks bounds the best code: Shannon, DT, RCU, Gallager (pp. 353–361)
- [[feinstein-maximal-coding]] (new) — greedy codebook with disjoint decoding regions, giving maximal error probability (p. 358)
- [[rho-trick]] (new) — $\min\{t,1\}\le t^\rho$ for $\rho\in[0,1]$; gives Gallager's bound and exponents (p. 361)
- [[linear-code]] (new) — a $k$-dimensional subspace of $\mathbb F_q^n$, given by $G$ or $H$; syndrome decoding is ML for additive noise (pp. 362–363)
- [[submodularity-of-decoding]] (new) — $S(\mathcal C)=\sum_y\max_{x\in\mathcal C}P_{Y|X}(y|x)$ is submodular; greedy and random selection are near-optimal (pp. 367–369)

## Canonical instances
- [[hamming-code-7-4-3]] — $[7,4,3]_2$ linear code with explicit $G,H$, corrects 1 bit error (p. 362)
- [[bsc-syndrome-decoding]] — on BSC the syndrome decoder finds the minimum-weight noise; $D_0$ is the set of coset leaders (p. 364)

## Bridges (candidates)
- [same-math] Information tail $\mathbb P[i(\bar X;Y)>t]\le e^{-t}$ ↔ hypothesis testing: $Q[\log\frac{dP}{dQ}\ge t]\le e^{-t}$ — the same inequality with $Q=P_XP_Y$ (p. 353).
- [same-math] DT bound ↔ Bayesian binary hypothesis testing: the RHS is $\frac{M+1}2$ times the minimum weighted error (p. 357).
- [structural-analogy] Random linear codes vs fully random codes ↔ compression: Theorems 11.5 vs 11.8, as the text states (p. 364).
- [structural-analogy] Greedy/random codebook selection ↔ submodular maximization (greedy $1-1/e$ guarantee, integrality gap of an LP relaxation) (pp. 367–369).
- [metaphor] Shannon's random placement ↔ Erdős's probabilistic method (p. 353).

## Questions this raises
- How tight are these bounds for the BSC at finite blocklength? The text points to Figure 22.2 (p. 350).
- How do the bounds with iid inputs and memoryless channels turn into capacity and dispersion results (Chapter 19)?
- Is there a codebook distribution with pairwise independence and entropy near $2n\log q$ that is good beyond additive-noise channels (p. 366)?
- Can the integrality-gap view (18.22)–(18.23) be used to design $P_X$ for channels that are not input-symmetric (p. 369)?

## Exercises worth doing
The unit prints no exercise list. It points to the following (not stated here):
- Exercise IV.5 (p. 357) — the DT bound beats Shannon's bound with optimized $\tau$ — difficulty: medium
- Find $\mathbb P[\mathrm{rank}(G)<k]$ as a function of $n,k,q$ (p. 366) — failure of the Elias ensemble — difficulty: medium
- Exercise IV.7 (p. 366) — the Wozencraft ensemble — difficulty: hard

## Reading notes
- Printed chapter number is 18; the unit label "ch20" and the PDF numbering are the work-level labels. Printed = pdf − 25.
- Running header on every page: "itbook-export CUP/HE2-design August 16, 2024 18:58".
- Theorem 18.6 says "for every $\tau>0$" but $\tau$ does not appear in (18.11) (p. 356).
- Lemma 18.16 proof: the displayed exponent $\ell$ in $b(j)$ should be $M'$ (p. 369). The statement of Lemma 18.16 on p. 369 says "Let $\pi$ and $C$ be as in Theorem" without a number ("Let $\pi$ and $C$ be as in Theorem").
- Theorem 18.12 notation $[k,n]$ and codomain $\mathbb F_q^k$ are loose; see the note in L3 (p. 363).
- Text-layer equations were garbled in places (e.g. the cases in 18.2); I checked them against the images.
- Material referenced but not in this unit: Theorems 11.5/11.8, 14.11, 19.4, Sections 22.3–22.4, Figure 22.2, Exercises IV.5, IV.7.
