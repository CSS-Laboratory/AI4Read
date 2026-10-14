---
id: polyanskiy-2025-information/ch29-evaluating
work: polyanskiy-2025-information
unit: "Chapter 26 (given as ch29 in the unit metadata) — Evaluating rate-distortion function. Lossy Source-Channel separation."
pages: 507–521
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
# Evaluating the rate-distortion function; lossy source–channel separation

## L0 — One line
The rate-distortion function can be computed in closed form for Bernoulli and Gaussian sources by guessing the optimal "backward channel" (the channel from the reconstruction to the source), and for lossy joint source-channel coding over a channel of capacity $C$ the best rate is $C/R(D)$, reached by separate compression and channel coding under a technical assumption on the distortion.

## L1 — The gist (≤ 120 words)
How can we evaluate $R(D)=\inf I(S;\hat S)$ in practice, and how well can a source be sent over a noisy channel within distortion $D$? The chapter computes $R(D)$ for Bernoulli/Hamming and Gaussian/quadratic cases, bounds it for non-Gaussian sources (Shannon lower bound), and proves a general optimality criterion (saddle-point property). For lossy joint source-channel coding it proves $R_{\rm JSCC}(D)=C/R(D)$: the converse uses data processing, and achievability uses separation under a technical assumption on the distortion. It ends with limitations: no graceful degradation for separated schemes, and an unclear convergence rate for joint source-channel coding.

**Prerequisites:** mutual information and KL divergence; differential entropy and the max-entropy fact for Gaussians; the rate-distortion theorem $R(D)=\inf I(S;\hat S)$; channel capacity; data processing inequality.

## L2 — Key ideas (5–10 bullets)
- Bernoulli($p$) with Hamming distortion has $R(D)=(h(p)-h(D))_+$. The bound is achieved when the backward channel $P_{S|\hat S}$ (from reconstruction to source) is BSC($D$), a binary symmetric channel that flips each bit with probability $D$ (p. 507–508).
- Gaussian with MSE (mean-squared error) has $R(D)=\tfrac12\log^+\sigma^2/D$. The converse uses a KL-divergence trick, because $\hat S$ may be discrete and its differential entropy undefined (p. 509–510).
- For any source with mean 0 and variance $\sigma^2$, $R(D)$ lies between $\tfrac12\log^+\sigma^2/D-D(P_S\|\mathcal N(0,\sigma^2))$ and $\tfrac12\log^+\sigma^2/D$. The lower bound is the Shannon lower bound (p. 511).
- Theorem 26.4 formalizes the guess-and-verify trick: (26.6) is sufficient for optimality, and necessary under extra conditions (p. 512).
- Lossy joint source-channel coding (JSCC) converse: $R_{\rm JSCC}(D)\le C/R(D)$, where $C$ is the channel capacity, by data processing (p. 515–516).
- Achievability by separation gives equality, provided Assumption 26.1 holds. Bounded distortions satisfy it, as do metrics raised to a power $q\ge1$ when $\mathcal S=\hat{\mathcal S}$ and $D_{\max}<\infty$ (p. 516–518).
- Separated schemes can degrade catastrophically when the channel worsens (in the example, distortion becomes $1/2$ for $\delta>\delta^*$); uncoded transmission degrades gracefully in that example (p. 520–521).

## L3 — Walkthrough

**Intro.** Standing result: for iid sources, separable distortion and $D_{\max}<\infty$, $R(D)=R^{(I)}(D)=\inf_{P_{\hat S|S}:\mathbb E d(S,\hat S)\le D} I(S;\hat S)$. The chapter evaluates this minimization (§26.1), formalizes the technique (§26.2*), treats lossy JSCC (§26.3) and discusses limitations (§26.4) (p. 507).

### 26.1.1 Bernoulli source
Setup: $S\sim\mathrm{Ber}(p)$, $p\le 1/2$, Hamming distortion $\mathbb 1\{S\ne\hat S\}$; for $n$ letters $d$ is the bit-error rate (p. 507).

**Theorem 26.1.**
$$R(D)=(h(p)-h(D))_+ \tag{26.1}$$
Example: $p=1/2$, $D=.11$ gives $R(D)\approx 1/2$ bit. So 100 bits can be compressed to 50 with 11% average distortion, versus 25% for storing half the string and guessing the rest (p. 507).

*Proof.* $D_{\max}=p$, so assume $D<p$ (p. 508).
- Converse. For any $P_{\hat S|S}$ with $\mathbb P[S\ne\hat S]\le D\le p\le\frac12$ (the sum $S+\hat S$ is mod 2):
$$I(S;\hat S)=H(S)-H(S|\hat S)=H(S)-H(S+\hat S|\hat S)\ge H(S)-H(S+\hat S)=h(p)-h(\mathbb P[S\ne\hat S])\ge h(p)-h(D).$$
The last step uses that $h$ is increasing on $[0,\frac12]$ (added step).
- Achievability. Equality needs $S+\hat S$ independent of $\hat S$. Take $S=\hat S+Z$, $\hat S\sim\mathrm{Ber}(p')\perp Z\sim\mathrm{Ber}(D)$, with $p'*D=p'(1-D)+(1-p')D=p$, i.e. $p'=\frac{p-D}{1-2D}$. The backward channel $P_{S|\hat S}$ is BSC($D$). Then $I(S;\hat S)=H(S)-H(Z)=h(p)-h(D)$, so $R(D)\le h(p)-h(D)$ (p. 508).

*Intuition note:* Compression is the reverse of a noisy channel. The best reconstruction $\hat S$ is the "input" of a BSC($D$) whose "output" is the source. Its noise costs $h(D)$ bits, which is subtracted from $h(p)$.

**Remark 26.1 (general strategy).** Let $P^*_{\hat S|S}$ be the optimal forward channel and $P^*_{S|\hat S}$ the backward channel (BSC($D$)). For any feasible $P_{\hat S|S}$:
$$I(P_S,P_{\hat S|S})=D(P_{S|\hat S}\|P_S|P_{\hat S})=D(P_{S|\hat S}\|P^*_{S|\hat S}|P_{\hat S})+\mathbb E_P\!\left[\log\frac{P^*_{S|\hat S}}{P_S}\right]\ge H(S)+\mathbb E_P[\log D\mathbb 1\{S\ne\hat S\}+\log\bar D\mathbb 1\{S=\hat S\}]\ge h(p)-h(D),$$
where the last step uses $\mathbb P[S\ne\hat S]\le D\le\frac12$ (p. 508).

**Remark 26.2.** By the WLLN, $P_S^n$ concentrates near the Hamming sphere of radius $np$. The optimal codebook is drawn from $\mathrm{Ber}(p')^n$. Here $p'=1/2$ if $p=1/2$, but $p'<p$ if $p<1/2$. Then the codewords lie on a smaller sphere of radius $np'$ and none of them is a typical source realization (Figure 26.1, p. 508–509).

### 26.1.2 Gaussian source
**Theorem 26.2.** For $S\sim\mathcal N(0,\sigma^2)$ and $d(s,\hat s)=(s-\hat s)^2$:
$$R(D)=\tfrac12\log^+\frac{\sigma^2}{D}\tag{26.2}$$
For $S\sim\mathcal N(0,\sigma^2I_d)$ and $d=\|s-\hat s\|_2^2$:
$$R(D)=\tfrac d2\log^+\frac{d\sigma^2}{D}\tag{26.3}$$
(p. 509). Here $D_{\max}=\sigma^2$, so assume $D<\sigma^2$.
- Achievability. $S=\hat S+Z$ with $\hat S\sim\mathcal N(0,\sigma^2-D)\perp Z\sim\mathcal N(0,D)$. The backward channel is AWGN with noise power $D$. The forward channel is $P_{\hat S|S}=\mathcal N\!\big(\frac{\sigma^2-D}{\sigma^2}S,\frac{\sigma^2-D}{\sigma^2}D\big)$. Then $I(S;\hat S)=\frac12\log\frac{\sigma^2}{D}$ (p. 509).
- Converse. Mimicking Theorem 26.1 with differential entropy is problematic, because $h(\hat S)$ may be undefined when $\hat S$ is discrete. So use Remark 26.1's route. For any $P_{\hat S|S}$ with $\mathbb E(S-\hat S)^2\le D$, with $P^*_{S|\hat S}=\mathcal N(\hat S,D)$:
$$I\ge \mathbb E_P\log\frac{\frac1{\sqrt{2\pi D}}e^{-(S-\hat S)^2/2D}}{\frac1{\sqrt{2\pi\sigma^2}}e^{-S^2/2\sigma^2}}=\tfrac12\log\frac{\sigma^2}{D}+\frac{\log e}{2}\,\mathbb E_P\!\left[\frac{S^2}{\sigma^2}-\frac{(S-\hat S)^2}{D}\right]\ge\tfrac12\log\frac{\sigma^2}{D}.$$
The last step holds since $\mathbb E S^2/\sigma^2=1$ and $\mathbb E(S-\hat S)^2/D\le1$ (added step) (p. 509–510).
- Vector case: (26.3) follows from (26.2) by the single-letterization argument of Theorem 24.8, using convexity of $R(D)$ (Theorem 24.4(a)) (p. 510).

*Intuition note:* In the Gaussian case, the best reconstruction is a shrunken, less noisy copy of the source, with variance $\sigma^2-D$. Rate grows by half a bit for each halving of $D$.

**Geometry (p. 510).** The source vector concentrates on the sphere $S(0,\sqrt{n\sigma^2})$. Each codeword drawn from $(P^*_{\hat S})^n$ is close to $S(0,\sqrt{n(\sigma^2-D)})$: two nested spheres, as in Fig. 26.1.
Errors of optimal quantizers $X^n\to W\to\hat X^n$ with $\frac1n\log M\to R(D)$:
- WLOG $\hat X^n=\mathbb E[X^n|W]$. Let $\Sigma=\mathrm{Cov}[X^n|W]$, so $\frac1n\mathrm{tr}\,\Sigma\le D$.
- $\log M=I(X^n;W)=h(X^n)-h(X^n|W)$.
- Max-entropy (2.19), with Jensen and Cor. 2.9, gives $\log M\ge\frac n2\log\sigma^2-\frac12\log\det\Sigma$.
- With eigenvalues $\lambda_j$ of $\Sigma$, dividing by $n$ gives $\frac12\log\frac{\sigma^2}{D}+o(1)\ge\frac1n\sum_j\frac12\log\frac{\sigma^2}{\lambda_j}$.
- By strict convexity of $\lambda\mapsto\frac12\log\frac{\sigma^2}{\lambda}$, the empirical distribution $\frac1n\sum_j\delta_{\lambda_j}$ must converge to $\delta_D$. So $\Sigma\approx D\cdot I_n$: the uncertainty regions are approximately spherical.

**Theorem 26.3 (sensitivity to Gaussianity).** If $\mathbb ES=0$, $\mathrm{Var}\,S=\sigma^2$ and the distortion is MSE:
$$\tfrac12\log^+\frac{\sigma^2}{D}-D(P_S\|\mathcal N(0,\sigma^2))\le R(D)=\inf_{P_{\hat S|S}:\mathbb E(\hat S-S)^2\le D}I(S;\hat S)\le\tfrac12\log^+\frac{\sigma^2}{D}.$$
*Proof (assume $D<\sigma^2$, $S_G\sim\mathcal N(0,\sigma^2)$)* (p. 511–512):
- "≤": use the Gaussian forward channel $P^*_{\hat S|S}$. Then $R(D)\le I(S;\frac{\sigma^2-D}{\sigma^2}S+W)$ with $W\sim\mathcal N(0,\frac{\sigma^2-D}{\sigma^2}D)$. This is $\le I(S_G;\cdot)$ by the Gaussian saddle point (Thm 5.11), which equals $\frac12\log\frac{\sigma^2}{D}$.
- "≥": for feasible $P_{\hat S|S}$, with $P^*_{S|\hat S}=\mathcal N(\hat S,D)$, decompose as in Remark 26.1 with a Gaussian reference: $I=D(P_{S|\hat S}\|P^*_{S|\hat S}|P_{\hat S})+\mathbb E_P\log\frac{P^*_{S|\hat S}}{P_{S_G}}-D(P_S\|P_{S_G})$. The same computation as above gives $\ge\frac12\log\frac{\sigma^2}{D}-D(P_S\|P_{S_G})$.

**Remark 26.3.** If $D(P_S\|\mathcal N(0,\sigma^2))<\infty$ and $P_S$ has a density, $R(D)$ grows like $\frac12\log\frac1D$ as $D\to0$. The left inequality is the *Shannon lower bound* (SLB). Under appropriate conditions on $P_S$ it is asymptotically tight (refs [281, 247]):
$$R(D)=\tfrac12\log\frac{\sigma^2}{D}-D(P_S\|\mathcal N(0,\sigma^2))+o(1),\quad D\to0.\tag{26.4}$$
Comparing with (2.21), the author concludes that for small distortion, uniform scalar quantization is asymptotically optimal within $\frac12\log(2\pi e)\approx2.05$ bits (p. 511). General SLB (proof in Exercise V.22), for any norm on $\mathbb R^d$, $r>0$ and $h(X)$ finite:
$$\inf_{P_{\hat X|X}:\mathbb E[\|\hat X-X\|^r]\le D}I(X;\hat X)\ge h(X)+\frac dr\log\frac{d}{Dre}-\log\!\Big(\Gamma\big(\tfrac dr+1\big)V\Big),\tag{26.5}$$
with $V$ the volume of the unit ball. It will be used for statistical lower bounds in §30.1 (p. 511).

### 26.2* Saddle-point property for rate-distortion
Both converses guessed the form of $R(D)$ and showed every feasible channel does no better. Typically no trick is needed: one can solve $\min_{P_{\hat S|S}}I(S;\hat S)+\lambda\mathbb E[d(S,\hat S)]$ parametrically, or use Blahut–Arimoto (§5.6). The theorem tells us when the trick is guaranteed to work (p. 512).

**Theorem 26.4.**
1. Suppose $P_{Y^*}$ and $P_{X|Y^*}\ll P_X$ satisfy $\mathbb E[d(X,Y^*)]\le D$, and for every $P_{X,Y}$ with $\mathbb E[d(X,Y)]\le D$
$$\mathbb E\!\left[\log\frac{dP_{X|Y^*}}{dP_X}(X|Y)\right]\ge I(X;Y^*).\tag{26.6}$$
Then $R(D)=I(X;Y^*)$.
2. Suppose $I(X;Y^*)=R(D)$. Then for any regular branch of $P_{X|Y^*}$ and any $P_{X,Y}$ with $\mathbb E[d(X,Y)]\le D$, $P_Y\ll P_{Y^*}$ and $I(X;Y)<\infty$, inequality (26.6) holds.

Remarks (p. 512–513):
- Part 1 is a sufficient condition and part 2 a necessary one. Typically the admissible $P_{X,Y}$ are rich enough to infer $\log\frac{dP_{X|Y^*}}{dP_X}(x|y)=R(D)-\theta[d(x,y)-D]$ for some $\theta>0$.
- Part 2 fails without $P_Y\ll P_{Y^*}$. Counterexample: $\mathcal A=\{0,1\}$, $P_X=\mathrm{Ber}(1/2)$, $\hat{\mathcal A}=\{0,1,0',1'\}$, $d(0,0)=d(0,0')=1-d(0,1)=1-d(0,1')=0$. Then $R(D)=|1-h(D)|^+$, but there are several non-equivalent optimal $P_{Y|X}$, $P_{X|Y}$, $P_Y$.

*Proof of part 2.* Part 1 repeats the earlier proofs. For part 2, suppose a counterexample $P_{X,Y}$ has $I_1=\mathbb E\log\frac{dP_{X|Y^*}}{dP_X}(X|Y)<I^*=R(D)$ (p. 513).
- When $I(X;Y)<\infty$: $I_1=I(X;Y)-D(P_{X|Y}\|P_{X|Y^*}|P_Y)$, so $D(P_{X|Y}\|P_{X|Y^*}|P_Y)<\infty$ (26.7).
- Idea: mix $P_{X,Y_\lambda}=\lambda P_{X,Y}+(1-\lambda)P_{X,Y^*}$. Then $I(X;Y_\lambda)=D(P_{X|Y_\lambda}\|P_{X|Y^*}|P_{Y_\lambda})+\lambda I_1+(1-\lambda)I^*$. The divergence term is $o(\lambda)$ (similar to Prop. 2.20), so for small $\lambda$, $I(X;Y_\lambda)<R(D)$. This contradicts optimality, since the mixture still meets the distortion constraint (added step: $\mathbb E d$ is linear in the mixture, so it is $\le D$).
- Details. Define $\rho_1=\frac{dP_Y}{dP_{Y^*}}$, $\lambda(y)=\frac{\lambda\rho_1(y)}{\lambda\rho_1(y)+\bar\lambda}$, $P^{(\lambda)}_{X|Y=y}=\lambda(y)P_{X|Y=y}+\bar\lambda(y)P_{X|Y^*=y}$, $D(y)=D(P_{X|Y=y}\|P_{X|Y^*=y})$, $D_\lambda(y)=D(P^{(\lambda)}_{X|Y=y}\|P_{X|Y^*=y})$.
- On $\{\rho_1=0\}$ all of $\lambda(y),D(y),D_\lambda(y)$ vanish (p. 514). By convexity of divergence $D_\lambda(y)\le\lambda(y)D(y)$, so $\frac1{\lambda(y)}D_\lambda(y)\mathbb 1\{\rho_1>0\}\le D(y)\mathbb 1\{\rho_1>0\}$. By (26.7), $\rho_1D$ is non-negative and $P_{Y^*}$-integrable, so dominated convergence applies:
$$\lim_{\lambda\to0}\int_{\{\rho_1>0\}}dP_{Y^*}\frac{1}{\lambda(y)}D_\lambda(y)\rho_1(y)=\int dP_{Y^*}\rho_1\lim_{\lambda\to0}\frac1{\lambda(y)}D_\lambda(y)=0\tag{26.8}$$
using $D(P\|Q)<\infty\Rightarrow D(\lambda P+\bar\lambda Q\|Q)=o(\lambda)$ (Ch. 5).
- The same integral equals $\frac1\lambda D(P^{(\lambda)}_{X|Y}\|P_{X|Y^*}|P_{Y_\lambda})$. Hence this divergence is $o(\lambda)$.
- Since $P^{(\lambda)}_{X|Y}\circ P_{Y_\lambda}=P_X$, one gets $I(X;Y_\lambda)=I^*+\lambda(I_1-I^*)+o(\lambda)$, contradicting $I(X;Y_\lambda)\ge I^*=R(D)$.

*Intuition note:* If one feasible alternative beats the guessed optimum in the "tilted" sense of (26.6), mixing a tiny amount of it into the optimum would lower the mutual information below $R(D)$. That is impossible, so the optimum satisfies (26.6) against every competitor that meets the conditions of part 2 (distortion $\le D$, $P_Y\ll P_{Y^*}$, $I(X;Y)<\infty$).

### 26.3 Lossy joint source-channel coding
**Setup.** A source $S^k$, a distortion $d$ and a channel $P_{Y^n|X^n}$. A $(k,n,D)$-JSCC has encoder $f:\mathcal S^k\to\mathcal A^n$ and decoder $g:\mathcal B^n\to\hat{\mathcal S}^k$ with $\mathbb E[d(S^k,\hat S^k)]\le D$, along the chain $S^k\to X^n\to Y^n\to\hat S^k$. The rate is $k/n$, and
$$R_{\rm JSCC}(D)\triangleq\liminf_{n\to\infty}\tfrac1n\max\{k:\exists(k,n,D)\text{-JSCC}\}.$$
The unit then restricts to iid sources, memoryless channels and separable distortion (p. 515).

**Theorem 26.5 (converse).** $R_{\rm JSCC}(D)\le \frac{C}{R(D)}$, with $C=\sup_{P_X}I(X;Y)$ and $R(D)=\inf_{P_{\hat S|S}:\mathbb E d\le D}I(S;\hat S)$ (p. 515).
*Proof* (p. 516): for a $(k,n,D)$-code,
$$kR(D)\overset{(a)}{=}\inf_{P_{\hat S^k|S^k}:\mathbb E d\le D}I(S^k;\hat S^k)\le I(S^k;\hat S^k)\overset{(b)}{\le}I(X^n;Y^n)\le\sup_{P_{X^n}}I(X^n;Y^n)\overset{(c)}{=}nC.$$
(b) is data processing; (a) and (c) are single-letterization (Thm 24.8, Prop. 19.10). It also holds with cost constraints, using the corresponding capacity (p. 515).

**Remark 26.4.** For a Ber(1/2) source with Hamming distortion this gives $R=\frac kn\le\frac{C}{1-h(P_b)}$, matching Thm 19.21 (earlier proved by ad hoc methods). For AWGN: $P_b\ge h^{-1}\!\big(1-\frac{C(\mathrm{SNR})}{R}\big)$, often called the Shannon limit. The author says that comparing practical codes' BER to this limit is erroneous: $P_b$ is the error rate of data (systematic) bits, whereas BER in coding theory usually refers to all codeword bits (p. 516).

**Theorem 26.6.** For a stationary memoryless source with $R(D)$ satisfying Assumption 26.1 and a stationary memoryless channel with capacity $C$: $R_{\rm JSCC}(D)=\frac{C}{R(D)}$ (p. 516).
*Proof (achievability by separation)* (p. 517):
- Source code $(f_s,g_s)$: a $(k,2^{kR(D)+o(k)},D)$-code. By Lemma 26.8 WLOG all reconstruction points satisfy $d(s_0^k,g_s(i))\le L$ (26.9).
- Channel code $(f_c,g_c)$: an $(n,2^{nC+o(n)},\epsilon_n)_{\max}$-code with $kR(D)+o(k)\le nC+o(n)$ and $\epsilon_n\to0$ (Thm 19.9, Cor. 19.5). The maximal error probability is needed because $W$, the compressor's output, need not be uniform.
- The system is $S^k\to W\to X^n\to Y^n\to\hat W\to\hat S^k$. Split $\mathbb E d=\mathbb E[d(S^k,g_s(W))\mathbb 1\{W=\hat W\}]+\mathbb E[d(S^k,g_s(\hat W))\mathbb 1\{W\ne\hat W\}]$. The first term is $\le D$.
- Second term: $\le\lambda\,\mathbb E[\mathbb 1\{W\ne\hat W\}d(S^k,\hat s_0^k)]+\lambda L\,\mathbb P[W\ne\hat W]=o(1)$. This uses the generalized triangle inequality (a), then (26.9), then Lemma 25.4. So for all $R>C/R(D)$ there are $(k,n,D+o(1))$-JSCC codes.

**Assumption 26.1.** For fixed $D$, there exist $\lambda\ge0$, $s_0\in\mathcal S$, $\hat s_0\in\hat{\mathcal S}$ with (p. 517–518):
- (a) $d(s,\hat s)\le\lambda(d(s,\hat s_0)+d(s_0,\hat s))$ for all $s,\hat s$ (the text prints $a,\hat a$);
- (b) $\mathbb E[d(S,\hat s_0)]<\infty$ (so $D_{\max}<\infty$);
- (c) $\mathbb E[d(s_0,\hat S)]<\infty$ for any $P_{\hat S}$ achieving $R(D)$;
- (d) $d(s_0,\hat s_0)<\infty$.

Meaning: the spaces have "nice centers". It controls the distortion when the channel decoder errs. It is trivially satisfied by bounded distortion (e.g. Hamming), and can be shown to hold for Gaussian sources with MSE (p. 516–517).

**Theorem 26.7.** If $\mathcal S=\hat{\mathcal S}$, $d=\rho^q$ for a metric $\rho$ and $q\ge1$, and $D_{\max}=\inf_{\hat s_0}\mathbb E d(S,\hat s_0)<\infty$, then Assumption 26.1 holds (p. 518).
*Proof.* Take $s_0=\hat s_0$ achieving $D_{\max}$. By the triangle and Jensen inequalities, $(\frac12\rho(s,\hat s))^q\le(\frac12\rho(s,s_0)+\frac12\rho(s_0,\hat s))^q\le\frac12\rho^q(s,s_0)+\frac12\rho^q(s_0,\hat s)$. So $d(s,\hat s)\le2^{q-1}(d(s,s_0)+d(s_0,\hat s))$; $\lambda=2^{q-1}$ gives (a),(b). For (c): $\mathbb E d(s_0,\hat S)\le2^{q-1}(D_{\max}+D)<\infty$.

**Lemma 26.8.** Under Assumption 26.1, let $P_{\hat S|S}$ be arbitrary, $R>I(S;\hat S)$, $L>\max\{\mathbb E d(s_0,\hat S),d(s_0,\hat s_0)\}$, $D>\mathbb E d(S,\hat S)$. Then there is a $(k,2^{kR},D)$-code with $d(s_0^k,\hat s^k)\le L$ for every reconstruction point (p. 519).
*Proof sketch.* Apply the excess-distortion bound of Thm 25.3 with $\gamma=2^{k(R+I(S;\hat S))/2}$ to the non-separable distortion $d_1=d$ if $d(s_0^k,\hat x)\le L$ and $+\infty$ otherwise. For $D'\in(\mathbb E d(S,\hat S),D)$ there are $M=2^{kR}$ points with $\mathbb P[\min_jd(S^k,c_j)>D']\le\mathbb P[d_1(S^k,\hat S^k)>D']+o(1)$. The WLLN makes the right side $\to0$. Points with $d(s_0^k,c_j)>L$ can be dropped. Adding the point $\hat s_0^k$ gives $\mathbb E\min_{j\le M+1}d\le D'+o(1)$, via the argument for (25.15).

### 26.4 What is lacking in classical lossy compression?
- Lossy theory relies on independence and separable distortion. Scalar quantization is widely used (ADCs), vector quantization theory so far is not. Images have strong spatial correlation, unlike a novel's first and last sentences. So the practical problem is finding good "whitening" bases, "an art still being refined" (p. 519–520).
- Separation has been a guiding light, but separated systems lack *graceful degradation* (dropped calls, "snow" on TV) (p. 520).
- Example: Ber(1/2) source, $R(D)=1-h(D)$, BSC$_\delta$ with $C(\delta)=1-h(\delta)$, $\rho=n/k=1$. (1) Separated: compress at rate $R(D^*)$, use a channel code of rate $R(D^*)$. It works when $R(D^*)<C(\delta)$, i.e. $\delta<D^*$, and codes exist that work simultaneously for all $\delta<\delta^*=D^*$ (Ex. IV.8, IV.10). (2) Uncoded: $X_i=S_i$. The separated scheme's distortion stays constant at $D^*$ for $\delta<\delta^*$ and becomes $1/2$ (catastrophic failure) for $\delta>\delta^*$; the uncoded scheme's distortion deteriorates gradually with $\delta$ (Fig. 26.2, p. 520–521).
- Graceful schemes are known only for few cases with $\rho=1$ and "perfect match" (Gastpar) conditions. Finding non-catastrophic schemes for general pairs and $\rho$ is a long-standing open problem (p. 521).
- Convergence rates: channel coding converges to capacity at $1/\sqrt n$, rate-distortion almost at $1/n$ (Ex. V.3, V.4). For a binary source over BSC$_\delta$, it was recently shown [248] that $k/n$ converges to $C/R(D)$ at speed $\Theta(1/\sqrt n)$ unless $R(D)=C(\delta)$. Other pairs are open (p. 521).

## Toy example (ours)
Source Ber($p=0.3$), Hamming distortion, target $D=0.1$.
- $h(0.3)=-0.3\log_2 0.3-0.7\log_2 0.7=0.3(1.7370)+0.7(0.5146)=0.5211+0.3602=0.8813$.
- $h(0.1)=0.1(3.3219)+0.9(0.1520)=0.3322+0.1368=0.4690$.
- So $R(0.1)=0.8813-0.4690\approx0.412$ bits per symbol.
- Optimal reconstruction: $p'=\frac{0.3-0.1}{1-0.2}=0.25$. Check: $0.25(0.9)+0.75(0.1)=0.225+0.075=0.3$ ✓. Since $p'<p$, codewords sit on a smaller Hamming sphere (Remark 26.2).
- Forward channel: $P(\hat S=1|S=1)=0.225/0.3=0.75$, $P(\hat S=1|S=0)=0.25\cdot0.1/0.7\approx0.036$. Error probability $=0.025+0.075=0.1=D$ ✓.
- JSCC use: over a channel with $C=0.531$, $R_{\rm JSCC}=C/R(D)=0.531/0.412\approx1.29$ source symbols per channel use.

## Concepts
- [[rate-distortion-function]] — $R(D)=\inf_{P_{\hat S|S}:\mathbb E d\le D}I(S;\hat S)$; here evaluated in closed form (p. 507)
- [[mutual-information]] — the quantity minimized in $R(D)$; rewritten as $D(P_{S|\hat S}\|P_S|P_{\hat S})$ (p. 508)
- [[relative-entropy-kl-divergence]] — used to prove converses via a reference backward channel (p. 508)
- [[differential-entropy]] — used in the Gaussian error-geometry argument; may be undefined for discrete $\hat S$ (p. 509–510)
- [[maximum-entropy-principle]] — Gaussian maximizes entropy for given covariance; bounds $h(X^n|W)$ (p. 510)
- [[shannon-lower-bound]] (new) — $R(D)\ge\frac12\log\frac{\sigma^2}{D}-D(P_S\|\mathcal N(0,\sigma^2))$; tight as $D\to0$ under conditions (p. 511)
- [[rd-saddle-point-condition]] (new) — Theorem 26.4 criterion (26.6) for optimality of a coupling (p. 512)
- [[lossy-jscc]] (new) — transmit a source over a channel within expected distortion $D$; limit $R_{\rm JSCC}(D)$ (p. 515)
- [[channel-capacity]] — $C=\sup_{P_X}I(X;Y)$, appears in $C/R(D)$ (p. 515)
- [[source-channel-separation]] — compress, then channel-code; optimal for lossy JSCC under Assumption 26.1 (p. 516)
- [[data-processing-inequality]] — step (b) in the JSCC converse (p. 516)
- [[generalized-triangle-inequality]] (new) — Assumption 26.1(a), "nice centers"; holds for $\rho^q$ (p. 518)
- [[graceful-degradation]] (new) — distortion worsens gradually with channel quality; separated schemes lack it (p. 520)

## Canonical instances
- [[bernoulli-hamming-rd]] — $R(D)=(h(p)-h(D))_+$, backward channel BSC($D$) (p. 507–508)
- [[gaussian-mse-rd]] — $R(D)=\frac12\log^+\sigma^2/D$; nested spheres geometry (p. 509–510)
- [[uncoded-vs-separated-bsc]] — Ber(1/2) over BSC$_\delta$ with $\rho=1$: separated vs uncoded distortion (p. 520–521)
- [[tolstoy-vs-image]] — a novel and an image, whose uncompressed sizes could easily be equal, differ in correlation structure (p. 520)

## Bridges (candidates)
- [structural-analogy] Backward-channel construction for $R(D)$ ↔ information-theory: capacity-achieving input distributions and the saddle-point in Ch. 5 — the same KL-decomposition trick is used on both sides.
- [same-math] Gaussian $R(D)=\frac12\log\sigma^2/D$ ↔ Shannon–Hartley formula $C=\frac12\log(1+\mathrm{SNR})$ — both are a Gaussian mutual information with a noise-ratio inside the log.
- [structural-analogy] Shannon lower bound for estimation (§30.1 preview) ↔ statistics: lower bounds on estimation error via rate-distortion.
- [metaphor] Catastrophic "snow" failure of separated schemes ↔ threshold effects in other systems, e.g. cliff behaviour of capacity-achieving codes.

## Questions this raises
- When does the saddle-point condition (26.6) hold for sources where $P_Y\ll P_{Y^*}$ fails, and what characterizes the multiple optimizers in the counterexample?
- Can any scheme with $\rho\ne1$ or without a Gastpar match degrade gracefully?
- Which second-order term governs lossy JSCC, and why is it $1/\sqrt n$ unless $R(D)=C(\delta)$?
- How should one choose "whitening" bases so that the iid rate-distortion formulas become useful for images?

## Reading notes
- The printed chapter number is 26; the unit metadata calls it ch29. Printed pages 507–521 correspond to pdf 532–546 (printed = pdf − 25).
- Running headers show "itbook-export CUP/HE2-design August 16, 2024", an export header with a date and time stamp.
- The text layer is garbled in equations; all formulas were checked against the page images.
- Minor misprints: "cannot exceeds" (p. 515); Lemma 26.8's proof says "sufficiently large $n$" where $k$ is meant (p. 519); Assumption 26.1(a) is printed with $a,\hat a$ in "$\forall a,\hat a$" where $s,\hat s$ are meant (p. 518).
- The unit refers to Exercises IV.8, IV.10, V.3, V.4, V.6, V.21, V.22 but does not contain them, so no exercise list is given. Theorem 26.4's proof is condensed here to its key steps; the references [248, 281, 247, 181, 359] are cited as printed only.
