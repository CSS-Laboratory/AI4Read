---
id: cover-2006-elements/ch13-rate
work: cover-2006-elements
unit: "13 Rate Distortion Theory"
pages: 336-373
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Rate Distortion Theory (Cover & Thomas, ch. 13)

## L0 — One line
The minimum rate for describing an i.i.d. source within expected distortion $D$ equals $R(D)=\min I(X;\hat X)$ over conditional distributions $p(\hat x|x)$ meeting the distortion constraint, and it is approached by coding long blocks jointly.

## L1 — The gist (≤ 120 words)
A continuous source cannot be described exactly with finitely many bits. The chapter asks: given a source and a distortion measure, what is the least rate that achieves expected distortion $D$? The answer (Theorem 13.2.1) is $R(D)=\min I(X;\hat X)$ over conditional distributions with expected distortion at most $D$. A converse uses convexity of $R(D)$. Achievability uses random codebooks and distortion-typical sequences (jointly typical pairs whose distortion is near its mean). Closed forms follow for the binary source ($H(p)-H(D)$), the Gaussian source ($\tfrac12\log\sigma^2/D$) and parallel Gaussians (reverse water-filling). The Blahut–Arimoto algorithm (an alternating-minimization procedure) computes $R(D)$ numerically. Independent samples are better described jointly than one by one; the geometry is sphere covering.

**Prerequisites:** entropy, mutual information and its convexity in the conditional distribution; the joint AEP and typical sets; differential entropy and the Gaussian maximum-entropy property; Lagrange multipliers and Kuhn–Tucker conditions; Jensen's inequality.

## L2 — Key ideas
- A distortion measure $d(x,\hat x)\ge0$ turns "how good is a representation" into a number. Sequence distortion is the per-symbol average (p. 339–340).
- Main theorem: for an i.i.d. source with bounded distortion, the operational $R(D)$ equals the information function $\min I(X;\hat X)$ (Thm 13.2.1, p. 342).
- Binary source with Hamming distortion: $R(D)=H(p)-H(D)$ for $0\le D\le\min\{p,1-p\}$, else $0$ (p. 342–344).
- Gaussian source: $R(D)=\tfrac12\log\sigma^2/D$, so $D(R)=\sigma^22^{-2R}$. Each bit cuts distortion by a factor of 4, beating the best 1-bit scalar quantizer ($0.3633\sigma^2$ versus $\sigma^2/4$) (p. 344–346).
- Parallel independent Gaussians: reverse water-filling. Use equal distortion $\lambda$ on components with variance above $\lambda$ and spend no bits on the rest (Thm 13.3.3, p. 348–349).
- Converse: $R(D)$ is non-increasing and convex. Then $nR\ge H(\hat X^n)\ge\dots\ge nR(D)$ for any code (p. 349–351).
- Achievability: random codebook drawn from $p(\hat x)$, encoding by distortion-typical pairs, error probability bounded using $(1-xy)^n\le1-x+e^{-yn}$ (p. 351–356). A strong-typicality outline gives a stronger statement (p. 358–362).
- Geometry: channel coding is sphere packing, rate distortion is sphere covering. Alternating minimization (Blahut–Arimoto) computes $R(D)$ and capacity (p. 357–367).

## L3 — Walkthrough

### Chapter introduction (p. 336)
- A real number needs infinitely many bits, so a finite representation is imperfect. A **distortion measure** (distance between the variable and its representation) defines "goodness". The basic problem: given a source and a distortion measure, what is the minimum expected distortion at a given rate, or equivalently the minimum rate for a given distortion? (p. 336)
- The author notes that joint descriptions are more efficient than individual ones, even for independent variables. The explanation offered is geometric, stated with a hedge: apparently, rectangular grid points from independent descriptions do not fill space efficiently. Zero-error compression (Ch. 5) is the special case of a discrete source with zero distortion. (p. 336)

### 13.1 Quantization (p. 337–338)
- To represent one sample $X$ with $R$ bits, $\hat X(X)$ takes at most $2^R$ values, the **reproduction points** (codepoints), each with an assigned region. (p. 337)
- Example: $X\sim N(0,\sigma^2)$, squared error, 1 bit. The bit says whether $X>0$, and each reproduction point is the conditional mean of its region (Fig. 13.1):
$$\hat X(x)=\begin{cases}\sqrt{2/\pi}\,\sigma,& x\ge0,\\ -\sqrt{2/\pi}\,\sigma,& x<0.\end{cases}\tag{13.1}$$
(For $\sigma=1$ the points are $\pm0.7979$.) (p. 337)
- For 2 bits the optimal regions and points are no longer obvious, but two properties hold (p. 338):
  1. Given the reproduction points, distortion is minimized by mapping $X$ to the nearest point. The resulting regions form a Voronoi (Dirichlet) partition.
  2. Given the regions, the points should minimize conditional expected distortion within each region. These are the centroids for squared error.
- Iterating the two steps lowers expected distortion each time, so it converges to a local minimum. This is the Lloyd algorithm (generalized Lloyd for vectors). (p. 338)
- For $n$ i.i.d. Gaussians described with $nR$ bits, coding the whole sequence by one index in $2^{nR}$ values achieves lower distortion than quantizing each sample separately. The chapter's results show this. (p. 338)

### 13.2 Definitions (p. 338–342)
Source $X_1,\dots,X_n$ i.i.d. $\sim p(x)$, finite alphabet $\mathcal X$ for the proofs; most proofs extend to continuous variables. The encoder gives an index $f_n(X^n)\in\{1,\dots,2^{nR}\}$ and the decoder outputs $\hat X^n\in\hat{\mathcal X}^n$ (Fig. 13.2). (p. 338–339)

- **Distortion function:** $d:\mathcal X\times\hat{\mathcal X}\to\mathbb R^+$, the cost of representing $x$ by $\hat x$ (13.2). It is **bounded** if $d_{\max}=\max_{x,\hat x}d(x,\hat x)<\infty$ (13.3). (p. 339)
- **Hamming distortion:** $d(x,\hat x)=0$ if $x=\hat x$, $1$ otherwise (13.4). Then $Ed(X,\hat X)=\Pr(X\ne\hat X)$. (p. 339)
- **Squared error:** $d(x,\hat x)=(x-\hat x)^2$ (13.5). It is popular for continuous alphabets because it is simple and tied to least squares. For speech and image coding, others point out it does not match human perception (a time-shifted waveform has large squared error but sounds similar). The Itakura–Saito distance is a speech alternative; for images there is "at present no real alternative" (p. 339–340).
- **Sequence distortion** is the per-symbol average:
$$d(x^n,\hat x^n)=\frac1n\sum_{i=1}^n d(x_i,\hat x_i).\tag{13.6}$$
The author says this is not the only reasonable definition (for example, the maximum per-symbol distortion), and the theory below does not apply directly to that case. (p. 340)
- **$(2^{nR},n)$ rate distortion code:** $f_n:\mathcal X^n\to\{1,\dots,2^{nR}\}$ (13.7), $g_n:\{1,\dots,2^{nR}\}\to\hat{\mathcal X}^n$ (13.8). Its distortion is
$$D=Ed(X^n,g_n(f_n(X^n)))=\sum_{x^n}p(x^n)\,d(x^n,g_n(f_n(x^n))).\tag{13.9, 13.10}$$
The $2^{nR}$ values $g_n(1),\dots$ form the **codebook**; the sets $f_n^{-1}(i)$ are the assignment regions. (p. 340–341)
- **Achievable pair $(R,D)$:** there is a sequence of $(2^{nR},n)$ codes with $\lim_{n\to\infty}Ed(X^n,g_n(f_n(X^n)))\le D$. The **rate distortion region** is the closure of the achievable pairs. $R(D)$ is the infimum of rates $R$ with $(R,D)$ in the region. $D(R)$ is the analogous infimum of distortions. The two describe the same boundary. (p. 341)
- **Information rate distortion function:**
$$R^{(I)}(D)=\min_{p(\hat x|x):\ \sum_{(x,\hat x)}p(x)p(\hat x|x)d(x,\hat x)\le D} I(X;\hat X).\tag{13.11}$$
(p. 341)

**Theorem 13.2.1.** For an i.i.d. source $X\sim p(x)$ with bounded $d(x,\hat x)$,
$$R(D)=R^{(I)}(D)=\min_{p(\hat x|x):\ \sum p(x)p(\hat x|x)d(x,\hat x)\le D}I(X;\hat X)\tag{13.12}$$
is the minimum achievable rate at distortion $D$. The operational definition equals the information definition, so $R(D)$ now denotes both. (p. 342)

*Intuition note:* "Minimum bits" is defined by coding schemes. Here it equals the smallest mutual information between source and reproduction under a distortion budget. The theorem is proved in 13.4 (converse) and 13.5 (achievability), in parallel with channel capacity. (p. 342)

### 13.3 Calculation of the rate distortion function (p. 342–349)

#### 13.3.1 Binary source (p. 342–344)
**Theorem 13.3.1.** For a Bernoulli($p$) source with Hamming distortion,
$$R(D)=\begin{cases}H(p)-H(D),&0\le D\le\min\{p,1-p\},\\0,&D>\min\{p,1-p\}.\end{cases}\tag{13.13, 13.23}$$

*Proof.* WLOG $p\le\frac12$. Minimization is as in (13.14). With $\oplus$ the modulo-2 sum, $X\oplus\hat X=1$ means $X\ne\hat X$. Lower bound: for any joint distribution meeting the constraint,
$$\begin{aligned}I(X;\hat X)&=H(X)-H(X|\hat X)\quad(13.15)\\&=H(p)-H(X\oplus\hat X|\hat X)\quad(13.16)\\&\ge H(p)-H(X\oplus\hat X)\quad(13.17)\\&\ge H(p)-H(D),\quad(13.18)\end{aligned}$$
because $\Pr(X\ne\hat X)\le D$ and $H(D)$ increases with $D$ for $D\le\frac12$. So $R(D)\ge H(p)-H(D)$ (13.19). (p. 343)

Achievability of the bound, for $0\le D\le p$: take the joint distribution of the binary symmetric channel in Fig. 13.3. It has input $\hat X$, crossover probability $D$, and output $X$ with the given Bernoulli($p$) distribution. Let $r=\Pr(\hat X=1)$ and require
$$r(1-D)+(1-r)D=p,\quad\text{so}\quad r=\frac{p-D}{1-2D}.\tag{13.20, 13.21}$$
If $D\le p\le\frac12$, then $\Pr(\hat X=1)\ge0$ and $\Pr(\hat X=0)\ge0$. Then
$$I(X;\hat X)=H(X)-H(X|\hat X)=H(p)-H(D),\tag{13.22}$$
and $\Pr(X\ne\hat X)=D$. If $D\ge p$, set $\hat X=0$ with probability 1, giving $I=0$ and distortion $p$. Similarly, if $D\ge1-p$, set $\hat X=1$. (p. 343–344)

*Intuition note:* Distortion $D$ acts like channel noise of flip probability $D$. The rate saved is the entropy of the noise, $H(D)$, subtracted from the source entropy $H(p)$. The author remarks the calculation seems unmotivated until Theorem 13.2.1 is proved. (p. 344)

#### 13.3.2 Gaussian source (p. 344–346)
Theorem 13.2.1 is proved only for discrete sources with bounded distortion. The author states it can also be proved for well-behaved continuous sources and unbounded distortion measures, and assumes this general theorem here. (p. 344)

**Theorem 13.3.2.** For $X\sim N(0,\sigma^2)$ with squared error,
$$R(D)=\begin{cases}\tfrac12\log\frac{\sigma^2}{D},&0\le D\le\sigma^2,\\0,&D>\sigma^2.\end{cases}\tag{13.24, 13.36}$$

*Proof.* $R(D)=\min_{f(\hat x|x):E(X-\hat X)^2\le D}I(X;\hat X)$ (13.25). Lower bound, using $E(X-\hat X)^2\le D$ (p. 345):
$$\begin{aligned}I(X;\hat X)&=h(X)-h(X|\hat X)\quad(13.26)\\&=\tfrac12\log(2\pi e)\sigma^2-h(X-\hat X|\hat X)\quad(13.27)\\&\ge\tfrac12\log(2\pi e)\sigma^2-h(X-\hat X)\quad(13.28)\\&\ge\tfrac12\log(2\pi e)\sigma^2-h\big(N(0,E(X-\hat X)^2)\big)\quad(13.29)\\&=\tfrac12\log(2\pi e)\sigma^2-\tfrac12\log(2\pi e)E(X-\hat X)^2\quad(13.30)\\&\ge\tfrac12\log(2\pi e)\sigma^2-\tfrac12\log(2\pi e)D\quad(13.31)\\&=\tfrac12\log\frac{\sigma^2}{D}.\quad(13.32)\end{aligned}$$
Step (13.28) holds because conditioning reduces entropy. Step (13.29) holds because the normal distribution maximizes entropy for a given second moment (Theorem 9.6.5). Hence $R(D)\ge\frac12\log\sigma^2/D$ (13.33). (p. 345)

Achievability: it is usually more convenient to specify $f(x|\hat x)$, called the **test channel** (the duality with channel capacity). For $D\le\sigma^2$ choose (Fig. 13.5)
$$X=\hat X+Z,\quad \hat X\sim N(0,\sigma^2-D),\quad Z\sim N(0,D),\tag{13.34}$$
with $\hat X,Z$ independent. Then $I(X;\hat X)=\frac12\log\frac{\sigma^2}{D}$ (13.35) and $E(X-\hat X)^2=D$. For $D>\sigma^2$ take $\hat X=0$, giving $R(D)=0$. (p. 345–346)

Distortion in terms of rate: $D(R)=\sigma^22^{-2R}$ (13.37). Each bit of description reduces the expected distortion by a factor of 4. With 1 bit the best expected squared error is $\sigma^2/4$. Simple 1-bit scalar quantization (Section 13.1) gives $\frac{\pi-2}{\pi}\sigma^2=0.3633\sigma^2$ (Problem 1). The rate distortion limit is approached by long block lengths, so considering several independent problems together beats treating them separately. The author calls this "somewhat surprising". (p. 346)

*Intuition note:* The Gaussian lower bound uses two facts: conditioning cannot increase entropy, and the Gaussian has the largest entropy for a given second moment. The test channel is the case where both are equalities.

#### 13.3.3 Simultaneous description of independent Gaussians (p. 347–349)
Sources $X_i\sim N(0,\sigma_i^2)$, $i=1,\dots,m$, independent but not identically distributed, with $d(x^m,\hat x^m)=\sum_i(x_i-\hat x_i)^2$. The question is how to allot bits to components. The information function is $R(D)=\min_{f(\hat x^m|x^m):Ed(X^m,\hat X^m)\le D}I(X^m;\hat X^m)$ (13.38). (p. 347) Let $D_i=E(X_i-\hat X_i)^2$.
$$\begin{aligned}I(X^m;\hat X^m)&=h(X^m)-h(X^m|\hat X^m)\quad(13.39)\\&=\sum_i h(X_i)-\sum_i h(X_i|X^{i-1},\hat X^m)\quad(13.40)\\&\ge\sum_i h(X_i)-\sum_i h(X_i|\hat X_i)\quad(13.41)\\&=\sum_i I(X_i;\hat X_i)\quad(13.42)\\&\ge\sum_i R(D_i)\quad(13.43)\\&=\sum_i\Big(\tfrac12\log\frac{\sigma_i^2}{D_i}\Big)^+.\quad(13.44)\end{aligned}$$
Step (13.41) holds because conditioning reduces entropy. Equality in (13.41) holds with $f(\hat x^m|x^m)=\prod_i f(\hat x_i|x_i)$, and equality in (13.43) with each $\hat X_i\sim N(0,\sigma_i^2-D_i)$. So the problem becomes (in nats)
$$R(D)=\min_{\sum D_i=D}\ \sum_{i=1}^m\max\Big\{\tfrac12\ln\frac{\sigma_i^2}{D_i},0\Big\}.\tag{13.45}$$
(p. 347)

Lagrange functional and derivative:
$$J(D)=\sum_i\tfrac12\ln\frac{\sigma_i^2}{D_i}+\lambda\sum_iD_i,\tag{13.46}$$
$$\frac{\partial J}{\partial D_i}=-\frac12\frac1{D_i}+\lambda=0,\quad\text{so}\quad D_i=\lambda'.\tag{13.47, 13.48}$$
Equal distortion across components is possible if $\lambda'<\sigma_i^2$ for all $i$. As $D$ grows, $\lambda'$ eventually exceeds some $\sigma_i^2$, and the solution reaches the boundary of the allowed region. Then Kuhn–Tucker conditions apply:
$$\frac{\partial J}{\partial D_i}=-\frac12\frac1{D_i}+\lambda,\quad\text{where }\lambda\text{ is chosen so that }\frac{\partial J}{\partial D_i}\begin{cases}=0,&D_i<\sigma_i^2,\\ \le0,&D_i\ge\sigma_i^2.\end{cases}\tag{13.49, 13.50}$$
(p. 348)

**Theorem 13.3.3 (parallel Gaussian source).** With $X_i\sim N(0,\sigma_i^2)$ independent and $d(x^m,\hat x^m)=\sum(x_i-\hat x_i)^2$,
$$R(D)=\sum_{i=1}^m\tfrac12\log\frac{\sigma_i^2}{D_i},\qquad D_i=\begin{cases}\lambda,&\lambda<\sigma_i^2,\\ \sigma_i^2,&\lambda\ge\sigma_i^2,\end{cases}\tag{13.51, 13.52}$$
where $\lambda$ is chosen so that $\sum D_i=D$. (p. 348)

This is **reverse water-filling** (Fig. 13.7). Choose a level $\lambda$ and describe only components with variance above $\lambda$. Components with variance below $\lambda$ get no bits. The author states that for a multivariate normal vector the same is done on the eigenvalues. For a Gaussian stochastic process, the spectral representation lets one apply it to the spectrum. (p. 348–349)

*Intuition note:* Every described component ends with the same error $\lambda$. A component whose variance is already below $\lambda$ is simply guessed (reproduced as $0$) and costs nothing.

### 13.4 Converse to the rate distortion theorem (p. 349–351)
Goal: no code with rate below $R(D)$ achieves distortion $D$, where $R(D)$ is as in (13.53). (p. 349)

**Lemma 13.4.1 (convexity).** $R(D)$ is a non-increasing convex function of $D$.

*Proof.* As $D$ grows, the minimization runs over larger sets, so $R(D)$ is non-increasing. For convexity, take pairs $(R_1,D_1),(R_2,D_2)$ on the curve, achieved by $p_1(x,\hat x)=p(x)p_1(\hat x|x)$ and $p_2$. Let $p_\lambda=\lambda p_1+(1-\lambda)p_2$. Distortion is linear in the distribution, so $D(p_\lambda)=\lambda D_1+(1-\lambda)D_2$. Mutual information is convex in the conditional distribution (Thm 2.7.4):
$$I_{p_\lambda}(X;\hat X)\le\lambda I_{p_1}(X;\hat X)+(1-\lambda)I_{p_2}(X;\hat X).\tag{13.54}$$
Hence
$$R(D_\lambda)\le I_{p_\lambda}\le\lambda R(D_1)+(1-\lambda)R(D_2).\tag{13.55–13.57}$$
(p. 349–350)

**Converse.** Take any $(2^{nR},n)$ code with distortion $\le D$, and let $\hat X^n=g_n(f_n(X^n))$. Then
$$\begin{aligned}nR&\overset{(a)}{\ge}H(\hat X^n)\overset{(b)}{\ge}H(\hat X^n)-H(\hat X^n|X^n)\overset{(c)}{=}I(\hat X^n;X^n)\\&=H(X^n)-H(X^n|\hat X^n)\overset{(d)}{=}\sum_iH(X_i)-H(X^n|\hat X^n)\\&\overset{(e)}{=}\sum_iH(X_i)-\sum_iH(X_i|\hat X^n,X_{i-1},\dots,X_1)\overset{(f)}{\ge}\sum_iH(X_i)-\sum_iH(X_i|\hat X_i)\\&\overset{}{=}\sum_iI(X_i;\hat X_i)\overset{(g)}{\ge}\sum_iR(Ed(X_i,\hat X_i))=n\sum_i\tfrac1nR(Ed(X_i,\hat X_i))\\&\overset{(h)}{\ge}nR\Big(\tfrac1n\sum_iEd(X_i,\hat X_i)\Big)\overset{(i)}{=}nR(Ed(X^n,\hat X^n))=nR(D).\end{aligned}$$
This is (13.58)–(13.70), with the following justifications (p. 351):
- (a) at most $2^{nR}$ values of $\hat X^n$.
- (b) $\hat X^n$ is a function of $X^n$, so $H(\hat X^n|X^n)=0$.
- (c) definition of mutual information.
- (d) the $X_i$ are independent.
- (e) chain rule.
- (f) conditioning reduces entropy.
- (g) definition of $R(D)$.
- (h) convexity (Lemma 13.4.1) and Jensen.
- (i) block distortion definition.

Conclusion: the rate $R$ of any code exceeds $R(D)$ at the distortion $D=Ed(X^n,\hat X^n)$ it achieves. (p. 351)

### 13.5 Achievability of the rate distortion function (p. 351–358)

**Distortion $\epsilon$-typical pairs.** For $p(x,\hat x)$ and $d(x,\hat x)$, a pair $(x^n,\hat x^n)$ is distortion typical if
$$\Big|-\tfrac1n\log p(x^n)-H(X)\Big|<\epsilon,\quad\Big|-\tfrac1n\log p(\hat x^n)-H(\hat X)\Big|<\epsilon,\quad\Big|-\tfrac1n\log p(x^n,\hat x^n)-H(X,\hat X)\Big|<\epsilon,\tag{13.71–13.73}$$
$$|d(x^n,\hat x^n)-Ed(X,\hat X)|<\epsilon.\tag{13.74}$$
The set is $A^{(n)}_{d,\epsilon}$. It is the jointly typical set with an extra distortion condition, so $A^{(n)}_{d,\epsilon}\subset A^{(n)}_\epsilon$. (p. 351–352)

- **Lemma 13.5.1.** If $(X_i,\hat X_i)$ are i.i.d. $\sim p(x,\hat x)$, then $\Pr(A^{(n)}_{d,\epsilon})\to1$ as $n\to\infty$. Proof: the four conditions are normalized sums of i.i.d. variables, so the law of large numbers applies. (p. 352)
- **Lemma 13.5.2.** For all $(x^n,\hat x^n)\in A^{(n)}_{d,\epsilon}$,
$$p(\hat x^n)\ge p(\hat x^n|x^n)\,2^{-n(I(X;\hat X)+3\epsilon)}.\tag{13.76}$$
Proof: write $p(\hat x^n|x^n)=p(\hat x^n)\,\frac{p(x^n,\hat x^n)}{p(x^n)p(\hat x^n)}$. Bound the numerator by $2^{-n(H(X,\hat X)-\epsilon)}$ and the denominator below by $2^{-n(H(X)+\epsilon)}2^{-n(H(\hat X)+\epsilon)}$. This gives $p(\hat x^n)2^{n(I(X;\hat X)+3\epsilon)}$ (13.77–13.80). (p. 352–353)
- **Lemma 13.5.3.** For $0\le x,y\le1$, $n>0$:
$$(1-xy)^n\le1-x+e^{-yn}.\tag{13.81}$$
Proof: let $f(y)=e^{-y}-1+y$. Then $f(0)=0$ and $f'(y)=-e^{-y}+1>0$ for $y>0$, so $f\ge0$. Hence $1-y\le e^{-y}$ and $(1-y)^n\le e^{-yn}$ (13.82). This is the case $x=1$; $x=0$ is clear. The function $g_y(x)=(1-xy)^n$ is convex in $x$, so for $0\le x\le1$
$$(1-xy)^n\le(1-x)g_y(0)+xg_y(1)=(1-x)+x(1-y)^n\le1-x+xe^{-yn}\le1-x+e^{-yn}.$$
(13.83–13.87) (p. 353)

**Proof of achievability (Theorem 13.2.1).** Take a bounded $d$ and $R>R(D)$. Fix $p(\hat x|x)$ achieving equality in (13.53), so $I(X;\hat X)=R(D)$. Compute $p(\hat x)=\sum_xp(x)p(\hat x|x)$. Choose $\delta>0$; the goal is a code with rate $R$ and distortion $\le D+\delta$. (p. 353–354)
- *Codebook:* generate $2^{nR}$ sequences $\hat X^n$ i.i.d. $\sim\prod_ip(\hat x_i)$, indexed by $w\in\{1,\dots,2^{nR}\}$. The codebook is revealed to encoder and decoder. (p. 354)
- *Encoding:* send the least $w$ with $(X^n,\hat X^n(w))\in A^{(n)}_{d,\epsilon}$. If none exists, send $w=1$. $nR$ bits suffice. (p. 354)
- *Decoding:* output $\hat X^n(w)$. (p. 354)
- *Distortion:* $\bar D=E_{X^n,\mathcal C}d(X^n,\hat X^n)$ (13.88). For a fixed codebook, split sequences into two categories (p. 354):
  1. $x^n$ with a distortion-typical codeword, so $d<D+\epsilon$. This contributes at most $D+\epsilon$.
  2. $x^n$ with none, of total probability $P_e$. This contributes at most $P_ed_{\max}$.

So
$$Ed(X^n,\hat X^n(X^n))\le D+\epsilon+P_ed_{\max},\tag{13.89}$$
which is below $D+\delta$ for suitable $\epsilon$ if $P_e$ is small. (p. 354)

*Bounding $P_e$* (p. 355–356). Let $J(\mathcal C)$ be the set of $x^n$ with at least one distortion-typical codeword in $\mathcal C$. Then $P_e=\sum_{\mathcal C}P(\mathcal C)\sum_{x^n\notin J(\mathcal C)}p(x^n)$ (13.90). Swap the sums (13.91). With $K(x^n,\hat x^n)=1$ if $(x^n,\hat x^n)\in A^{(n)}_{d,\epsilon}$ and $0$ otherwise (13.92), a single random codeword fails to represent $x^n$ with probability $1-\sum_{\hat x^n}p(\hat x^n)K(x^n,\hat x^n)$ (13.93). The $2^{nR}$ codewords are independent, so
$$P_e=\sum_{x^n}p(x^n)\Big[1-\sum_{\hat x^n}p(\hat x^n)K(x^n,\hat x^n)\Big]^{2^{nR}}.\tag{13.94, 13.95}$$
Lemma 13.5.2 gives $\sum p(\hat x^n)K\ge\sum p(\hat x^n|x^n)2^{-n(I+3\epsilon)}K$ (13.96), so
$$P_e\le\sum_{x^n}p(x^n)\Big(1-2^{-n(I(X;\hat X)+3\epsilon)}\sum_{\hat x^n}p(\hat x^n|x^n)K(x^n,\hat x^n)\Big)^{2^{nR}}.\tag{13.97}$$
Lemma 13.5.3 (with $x=\sum p(\hat x^n|x^n)K$, $y=2^{-n(I+3\epsilon)}$) bounds the bracket power (13.98), and
$$P_e\le1-\sum_{x^n}\sum_{\hat x^n}p(x^n)p(\hat x^n|x^n)K(x^n,\hat x^n)+e^{-2^{-n(I(X;\hat X)+3\epsilon)}2^{nR}}.\tag{13.99}$$
The last term equals $e^{-2^{n(R-I(X;\hat X)-3\epsilon)}}$ (13.100). It goes to zero exponentially fast if $R>I(X;\hat X)+3\epsilon$. This holds for small $\epsilon$, since $R>R(D)=I(X;\hat X)$. The first two terms equal $\Pr((X^n,\hat X^n)\notin A^{(n)}_{d,\epsilon})$ (13.101), which is $<\epsilon$ for large $n$ by Lemma 13.5.1 (13.102). So $P_e$ can be made as small as desired. (p. 356)

Conclusion: for any $\delta>0$ the expected distortion over random rate-$R$ codes is below $D+\delta$, so at least one code $\mathcal C^*$ achieves it. As $\delta$ is arbitrary, $(R,D)$ is achievable for $R>R(D)$. (p. 356)

*Intuition note:* A random codeword is jointly typical with a given source sequence with probability about $2^{-nI}$. With more than $2^{nI}$ codewords, some codeword almost surely fits well enough. The converse shows fewer will not do.

**Geometric view (Gaussian case)** (p. 357–358).
- *Channel coding for $Y_i=X_i+Z_i$, $Z_i\sim N(0,N)$, power $P$:* codewords lie in a sphere in $\mathbb R^n$ set by the power constraint. The problem is to pack $2^{nR}$ codewords so that the noise spheres around them are almost disjoint. The number $M$ of codewords is at most the ratio of volumes, i.e. the $n$th power of the ratio of the radii (13.103). The channel coding theorem shows roughly this many codewords can be found with almost disjoint noise spheres (13.104). [Radii and formulas unreadable, p. 357.]
- *Rate distortion for a Gaussian source of variance $\sigma^2$:* a $(2^{nR},n)$ code is a set of $2^{nR}$ sequences such that most source sequences (those in a sphere of radius set by $\sigma^2$) lie within distance set by $D$ of a codeword. By the same volume-ratio argument, this fixes the minimum number of codewords (13.105). [Formula unreadable, p. 357.] The theorem shows this minimum is asymptotically achievable, so spheres of radius set by $D$ cover the space except for a set of arbitrarily small probability. (p. 357–358)
- Channel coding is sphere packing and rate distortion is sphere covering. A set meeting the sphere-packing bound for one meets it for the other, so a good channel code can be turned into a good rate distortion code. In the Gaussian case, Gaussian codewords with the appropriate variance are asymptotically optimal for both. (p. 357–358)

### 13.6 Strongly typical sequences and rate distortion (p. 358–362)
Here the author only outlines a stronger result. Not only is the average distortion close to $D$, but the probability that the distortion exceeds $D+\delta$ is close to $0$. The proof uses strong typicality (Berger; Csiszár–Körner). (p. 358)

- **Strongly typical sequence:** $x^n$ is $\epsilon$-strongly typical for $p(x)$ if (1) for all $a$ with $p(a)>0$, the frequency $\frac1nN(a|x^n)$ is within $\epsilon$-scaled distance of $p(a)$ [formula (13.106) unreadable, p. 358], and (2) $N(a|x^n)=0$ whenever $p(a)=0$. Here $N(a|x^n)$ counts occurrences of $a$. The set is $A^{*(n)}_\epsilon$. (p. 358–359)
- **Jointly strongly typical pair:** (1) for all $(a,b)$ with $p(a,b)>0$, $\big|\frac1nN(a,b|x^n,y^n)-p(a,b)\big|<\frac{\epsilon}{|\mathcal X||\mathcal Y|}$ (13.107; the right-hand side was read from garbled text, p. 359); (2) $N(a,b|x^n,y^n)=0$ if $p(a,b)=0$. If $(x^n,y^n)$ is strongly jointly typical, then $x^n$ is strongly typical. (p. 359)
- **Lemma 13.6.1.** For i.i.d. $(X_i,Y_i)\sim p(x,y)$, $\Pr(A^{*(n)}_\epsilon)\to1$ (strong law of large numbers). (p. 359)
- **Lemma 13.6.2.** Let $Y_1,\dots,Y_n$ be i.i.d. $\sim p(y)$. For $x^n\in A^{*(n)}_\epsilon$,
$$2^{-n(I(X;Y)+\epsilon_1)}\le\Pr\big((x^n,Y^n)\in A^{*(n)}_\epsilon\big)\le2^{-n(I(X;Y)-\epsilon_1)},\tag{13.108}$$
with $\epsilon_1\to0$ as $\epsilon\to0$, $n\to\infty$. This gives a *lower* bound for every fixed typical $x^n$, which Theorem 8.6.1 (weak typicality) did not. The proof is not given; Problem 10 outlines it via the size of the conditionally typical set. (p. 359–360)

*Proof outline:* the codebook, encoding (first jointly strongly typical $w$ in lexicographic order, else $w=1$) and decoding are as in 13.5. Source sequences fall into three categories (Fig. 13.8) (p. 360–361):
1. Non-typical $x^n$: probability $<\epsilon$ for large $n$, contributing at most $\epsilon d_{\max}$.
2. Typical with a jointly typical codeword: by continuity of distortion in the joint distribution these are also distortion typical, so the distortion is at most $D+\epsilon d_{\max}$.
3. Typical with no jointly typical codeword: probability $P_e$, contributing at most $P_ed_{\max}$.

The expected number of jointly typical codewords is $2^{nR}2^{-nI(X;\hat X)}$, exponentially large if $R>I(X;\hat X)$. The author stresses this alone does not show that at least one exists with high probability. (p. 361–362) So expand
$$P_e=\sum_{x^n\in A^{*(n)}_\epsilon}p(x^n)\big[1-\Pr((x^n,\hat X^n)\in A^{*(n)}_\epsilon)\big]^{2^{nR}}.\tag{13.112}$$
With (13.113), $\Pr\ge2^{-n(I(X;\hat X)+\epsilon_1)}$, and $(1-x)^n\le e^{-nx}$:
$$P_e\le e^{-(2^{nR}2^{-n(I(X;\hat X)+\epsilon_1)})},\tag{13.114}$$
which goes to $0$ if $R>I(X;\hat X)+\epsilon_1$. So with probability going to 1 a codeword exists with distortion below $D+\delta$. (p. 362)

### 13.7 Characterization of the rate distortion function (p. 362–364)
The minimization (13.115) is a convex function over the convex set of $q(\hat x|x)\ge0$ with $\sum_{\hat x}q(\hat x|x)=1$ and $\sum q(\hat x|x)p(x)d(x,\hat x)\le D$. Use Lagrange multipliers:
$$J(q)=\sum_x\sum_{\hat x}p(x)q(\hat x|x)\log\frac{q(\hat x|x)}{\sum_xp(x)q(\hat x|x)}+\lambda\sum_x\sum_{\hat x}p(x)q(\hat x|x)d(x,\hat x)+\sum_x\nu(x)\sum_{\hat x}q(\hat x|x).\tag{13.116, 13.117}$$
With $q(\hat x)=\sum_xp(x)q(\hat x|x)$ this is (13.118, 13.119). Differentiating (p. 363):
$$\frac{\partial J}{\partial q(\hat x|x)}=p(x)\log\frac{q(\hat x|x)}{q(\hat x)}+p(x)-\sum_{x'}p(x')q(\hat x|x')\frac1{q(\hat x)}p(x)+\lambda p(x)d(x,\hat x)+\nu(x)=0.\tag{13.120}$$
Set $\log\mu(x)=\nu(x)/p(x)$:
$$p(x)\Big[\log\frac{q(\hat x|x)}{q(\hat x)}+\lambda d(x,\hat x)+\log\mu(x)\Big]=0,\quad q(\hat x|x)=\frac{q(\hat x)e^{-\lambda d(x,\hat x)}}{\mu(x)}.\tag{13.121, 13.122}$$
Since $\sum_{\hat x}q(\hat x|x)=1$: $\mu(x)=\sum_{\hat x}q(\hat x)e^{-\lambda d(x,\hat x)}$ (13.123), so
$$q(\hat x|x)=\frac{q(\hat x)e^{-\lambda d(x,\hat x)}}{\sum_{\hat x}q(\hat x)e^{-\lambda d(x,\hat x)}}.\tag{13.124}$$
Multiply by $p(x)$ and sum over $x$:
$$q(\hat x)=q(\hat x)\sum_x\frac{p(x)e^{-\lambda d(x,\hat x)}}{\sum_{\hat x'}q(\hat x')e^{-\lambda d(x,\hat x')}}.\tag{13.125}$$
If $q(\hat x)>0$, divide by it:
$$\sum_x\frac{p(x)e^{-\lambda d(x,\hat x)}}{\sum_{\hat x'}q(\hat x')e^{-\lambda d(x,\hat x')}}=1.\tag{13.126}$$
These $|\hat{\mathcal X}|$ equations plus the distortion equation determine $\lambda$ and the $|\hat{\mathcal X}|$ unknowns $q(\hat x)$. (p. 363–364)

This assumes all output symbols are active ($q(\hat x)>0$). In general the Kuhn–Tucker conditions give $\partial J/\partial q(\hat x|x)=0$ if $q(\hat x|x)>0$ and $\ge0$ if $q(\hat x|x)=0$ (13.127). Substituting the derivative, the minimum is characterized by
$$\sum_x\frac{p(x)e^{-\lambda d(x,\hat x)}}{\sum_{\hat x'}q(\hat x')e^{-\lambda d(x,\hat x')}}=1\ \text{ if }q(\hat x)>0,\qquad\le1\ \text{ if }q(\hat x)=0.\tag{13.128, 13.129}$$
This lets one *check* whether a given $q(\hat x)$ is optimal, but the author says it is not easy to *solve* for the optimum. (p. 364)

### 13.8 Computation of channel capacity and the rate distortion function (p. 364–367)
*Alternating minimization.* For convex sets $A,B\subset\mathbb R^n$, $d_{\min}=\min_{a\in A,b\in B}d(a,b)$ (13.130). Take $x\in A$, find the closest $y\in B$, fix $y$ and find the closest point in $A$, and repeat. The distance decreases at each stage. Csiszár and Tusnády showed that if the sets are convex and the distance satisfies certain conditions, the procedure converges to the minimum. For sets of probability distributions with relative entropy as the distance, it converges to the minimum relative entropy between the sets. (p. 364–365)

**Lemma 13.8.1.** For a given joint $p(x)p(y|x)$, the $r(y)$ minimizing $D(p(x)p(y|x)\|p(x)r(y))$ is the marginal $r^*(y)=\sum_xp(x)p(y|x)$:
$$D(p(x)p(y|x)\|p(x)r^*(y))=\min_{r(y)}D(p(x)p(y|x)\|p(x)r(y)).\tag{13.131}$$
Also
$$\max_{r(x|y)}\sum_{x,y}p(x)p(y|x)\log\frac{r(x|y)}{p(x)}=\sum_{x,y}p(x)p(y|x)\log\frac{r^*(x|y)}{p(x)},\quad r^*(x|y)=\frac{p(x)p(y|x)}{\sum_xp(x)p(y|x)}.\tag{13.132, 13.133}$$
Proof of the first part starts from the difference $D(\cdot\|p(x)r)-D(\cdot\|p(x)r^*)$ (13.134). Intermediate lines (13.135–13.139) are unreadable on p. 366. The difference works out to $\sum_yr^*(y)\log\frac{r^*(y)}{r(y)}=D(r^*\|r)\ge0$ *(added step)*. The second part is left as an exercise. (p. 365–366)

*Application to $R(D)$:* by the lemma,
$$R(D)=\min_{r(\hat x)}\ \min_{q(\hat x|x):\sum p(x)q(\hat x|x)d(x,\hat x)\le D}\ \sum_x\sum_{\hat x}p(x)q(\hat x|x)\log\frac{q(\hat x|x)}{r(\hat x)}.\tag{13.140}$$
Let $A$ be the set of joint distributions with marginal $p(x)$ meeting the distortion constraint, and $B$ the set of product distributions $p(x)r(\hat x)$. Then $R(D)$ is the minimum over $A\times B$ of the relative entropy (13.141, formula garbled; read from the text sentence). (p. 366)

**Blahut–Arimoto algorithm.** Start with an initial $r(\hat x)$.
1. Compute the $q(\hat x|x)$ minimizing mutual information under the distortion constraint (Lagrange multipliers):
$$q(\hat x|x)=\frac{r(\hat x)e^{-\lambda d(x,\hat x)}}{\sum_{\hat x}r(\hat x)e^{-\lambda d(x,\hat x)}}.\tag{13.142}$$
2. Compute the output distribution minimizing mutual information, which by Lemma 13.8.1 is the marginal $r(\hat x)=\sum_xp(x)q(\hat x|x)$ (13.143). Use it for the next iteration.

Each step reduces the right-hand side of (13.140), so a limit exists. Csiszár showed it equals $R(D)$. The values of $D$ and $R(D)$ depend on $\lambda$, so choosing $\lambda$ sweeps out the curve. (p. 366–367)

*Capacity.* Rewrite $C=\max_{r(x)}I(X;Y)$ (13.144) as a double maximization using Lemma 13.8.1:
$$C=\max_{r(x)}\max_{q(x|y)}\sum_x\sum_yr(x)p(y|x)\log\frac{q(x|y)}{r(x)}.\tag{13.145}$$
The Csiszár–Tusnády algorithm becomes alternating maximization. Given $r(x)$, the best $q$ is $q(x|y)=\frac{r(x)p(y|x)}{\sum_xr(x)p(y|x)}$ (13.146). Given $q$, the best input distribution found by Lagrange multipliers is (read from garbled text)
$$r(x)=\frac{\prod_yq(x|y)^{p(y|x)}}{\sum_{x'}\prod_yq(x'|y)^{p(y|x')}}.\tag{13.147}$$
(p. 367) The algorithms are due to Blahut and Arimoto, with Csiszár proving convergence for $R(D)$. The author says the alternating-minimization procedure also specializes to the EM algorithm and to the log-optimal portfolio algorithm. (p. 367)

### Summary of Chapter 13 (p. 367–368)
- $R(D)=\min_{p(\hat x|x):\ \sum p(x)p(\hat x|x)d\le D}I(X;\hat X)$ (13.148).
- If $R>R(D)$, there is a sequence of codes with at most $2^{nR}$ codewords and $Ed(X^n,\hat X^n(X^n))\to D$. If $R<R(D)$, no such codes exist.
- Bernoulli with Hamming: $R(D)=H(p)-H(D)$ (13.149). Gaussian with squared error: $\frac12\log\sigma^2/D$ (13.150). Multivariate Gaussian: reverse water-filling on the eigenvalues. (p. 368)

### Problems and Historical Notes (p. 368–373)
Ten problems are listed (see Exercises). Problem 10 outlines strong typicality facts: $|A^{*(n)}_\epsilon|\doteq2^{nH(X)}$; at most $(n+1)^{|\mathcal X||\mathcal Y|}$ conditional types; conditional type class sizes between $\frac{1}{(n+1)^{|\mathcal X||\mathcal Y|}}2^{nH(Y|X)}$ and $2^{nH(Y|X)}$; and (13.169) $2^{-n(I(X;Y)+\epsilon_3)}\le\Pr((x^n,Y^n)\in A^{*(n)}_\epsilon)\le2^{-n(I(X;Y)-\epsilon_3)}$. (p. 370–372)

Historical notes (p. 372–373):
- Shannon introduced rate distortion in his original paper and treated it exhaustively in his 1959 paper, which proved the first rate distortion theorem.
- Kolmogorov and his school began developing the theory in 1956.
- Berger's book proves stronger versions for general sources.
- McDonald and Schultheiss established inverse water-filling for parallel Gaussians.
- Blahut, Arimoto and Csiszár gave the iterative algorithm, a special case of Csiszár–Tusnády alternating minimization.

## Toy example (ours, not from the text)
Source: fair bit, $p=\frac12$, Hamming distortion, target $D=\frac14$.

1. Formula (13.13): $R(\tfrac14)=H(\tfrac12)-H(\tfrac14)$. $H(\tfrac12)=1$. $H(\tfrac14)=\tfrac14\log_24+\tfrac34\log_2\tfrac43=0.5+0.75(0.41504)=0.5+0.31128=0.81128$. So $R(\tfrac14)=1-0.81128=0.18872$ bits per symbol.
2. Test channel (13.21): $r=\frac{p-D}{1-2D}=\frac{0.25}{0.5}=0.5$. Check output: $r(1-D)+(1-r)D=0.5(0.75)+0.5(0.25)=0.375+0.125=0.5=p$ ✓. Then $I=H(X)-H(X|\hat X)=1-H(0.25)=0.18872$ and $\Pr(X\ne\hat X)=0.25$ ✓.
3. Naive alternative (time-sharing): describe half the symbols perfectly (rate 1, distortion 0) and guess "0" for the other half (rate 0, distortion $\frac12$). Overall rate is $0.5$ and distortion is $0.5\cdot0+0.5\cdot0.5=0.25$. So $R(\frac14)\le0.5$, and the formula's $0.1887$ is much lower. The point is also on the line between $(1,0)$ and $(0,\frac12)$, as convexity (Lemma 13.4.1) requires: $R$ lies below that chord.

## Concepts
- [[rate-distortion-function]] — $R(D)$: minimum rate of a code with expected distortion at most $D$; equals $\min I(X;\hat X)$ for i.i.d. sources (p. 341–342)
- [[distortion-measure]] (new) — cost function $d(x,\hat x)\ge0$; block distortion is the per-symbol average (p. 339–340)
- [[hamming-distortion]] (new) — $d=0$ if $x=\hat x$, else 1; expected value is $\Pr(X\ne\hat X)$ (p. 339)
- [[squared-error-distortion]] (new) — $(x-\hat x)^2$, standard for continuous alphabets; criticized for perceptual coding (p. 339–340)
- [[scalar-quantization-lloyd-algorithm]] (new) — nearest-neighbour regions plus centroid points, iterated to a local minimum (p. 338)
- [[test-channel]] (new) — conditional density $f(x|\hat x)$ used to achieve equality in the lower bound; dual to a channel (p. 345)
- [[reverse-water-filling]] (new) — parallel Gaussians: distortion $\min(\lambda,\sigma_i^2)$ per component; no bits for components below $\lambda$ (p. 348–349)
- [[distortion-typical-set]] (new) — jointly typical pairs with $d(x^n,\hat x^n)$ close to $Ed(X,\hat X)$ (p. 351–352)
- [[strongly-typical-set]] (new) — sequences whose symbol (pair) frequencies are close to $p$ (p. 358–359)
- [[typical-set-aep]] — used for random-coding achievability (p. 351–356)
- [[mutual-information]] — objective of the minimization; convex in $p(\hat x|x)$ (p. 350)
- [[differential-entropy]] — used in the Gaussian lower bound (p. 345)
- [[maximum-entropy-principle]] — normal has maximum entropy for a given second moment (p. 345)
- [[channel-capacity]] — dual of $R(D)$; same alternating algorithm computes it (p. 367)
- [[blahut-arimoto-algorithm]] (new) — alternating minimization of relative entropy over conditional and output distributions (p. 366)
- [[relative-entropy-kl-divergence]] — distance minimized in Lemma 13.8.1 and the algorithm (p. 365–366)
- [[sphere-covering-vs-packing]] (new) — rate distortion covers the space with distortion spheres, channel coding packs noise spheres (p. 357–358)

## Canonical instances
- [[binary-source-rate-distortion]] — $R(D)=H(p)-H(D)$ with a BSC test channel (p. 342–344)
- [[gaussian-source-rate-distortion]] — $R(D)=\frac12\log\sigma^2/D$; $D(R)=\sigma^22^{-2R}$ (p. 344–346)
- [[one-bit-gaussian-quantizer]] — points $\pm\sqrt{2/\pi}\sigma$, distortion $0.3633\sigma^2$ versus the block bound $\sigma^2/4$ (p. 337, 346)
- [[parallel-gaussian-water-filling]] — Thm 13.3.3 (p. 347–349)

## Bridges (candidates)
- [structural-analogy] rate distortion $\min I(X;\hat X)$ s.t. distortion ↔ information-theory: channel capacity $\max I(X;Y)$ s.t. cost — dual optimizations with a random-coding proof and a shared alternating algorithm.
- [structural-analogy] Reverse water-filling for parallel Gaussians ↔ information-theory: water-filling power allocation for parallel Gaussian channels — only structurally similar here; the text does not state the channel version, so confirm before using.
- [structural-analogy] Blahut–Arimoto alternating minimization ↔ statistics: EM algorithm — the text says the Csiszár–Tusnády alternating-minimization procedure specializes to many situations, including EM (p. 367).
- [structural-analogy] Gaussian R(D) with test channel $X=\hat X+Z$ ↔ statistics: posterior shrinkage in Gaussian estimation — proposed only; not in the text.
- [metaphor] Quantizing with spheres covering the signal space ↔ geometry: packing and covering problems.

## Questions this raises
- Why does the minimizing mutual information, rather than some other functional, end up equal to the operational minimum rate, and how does this mirror the capacity theorem?
- The theorem covers i.i.d. sources and additive average distortion. What changes for sources with memory, or for the maximum-distortion criterion, which the author says the theory does not directly cover (p. 340)?
- How fast does the finite-blocklength gap close, given that $R(D)$ is reached only as $n\to\infty$ (p. 346)?
- When some output symbols are inactive ($q(\hat x)=0$), how does the Kuhn–Tucker solution behave numerically in Blahut–Arimoto (p. 364)?

## Exercises worth doing
- Ex. 1 (p. 368) — one-bit scalar Gaussian quantizer: derive the points $\pm\sqrt{2/\pi}\sigma$ and distortion $\frac{\pi-2}{\pi}\sigma^2$, and compare with $D(R)$ at $R=1$ — difficulty: easy
- Ex. 5 (p. 369) — $R(D)$ for a uniform $m$-ary source with Hamming distortion — difficulty: medium
- Ex. 7 (p. 370) — erasure distortion for Bernoulli($\frac12$); asks for a simple scheme achieving the $R(D)$ — difficulty: medium
- Ex. 8 (p. 370) — bounds $h(X)-\frac12\log(2\pi e)D\le R(D)\le\frac12\log\sigma^2/D$ and whether Gaussians are harder or easier to describe — difficulty: medium
- Ex. 6 (p. 369) — Shannon lower bound for permutation-structured distortion matrices — difficulty: hard
- Ex. 9 (p. 370) — equality conditions in (13.58–13.70) as properties of a good code — difficulty: hard

## Reading notes
- The scan is the 1991 first edition: copyright line "Copyright 1991 John Wiley & Sons, Inc." on the chapter's first page, printed pages 336–373. Printed = pdf − 22. Content may differ from the 2nd edition cited in the metadata.
- Page images were supplied only for some pages (e.g. pdf 359, 361, 364–370, 372–378, 382–387, 390–393). For others I relied on the text layer.
- Equations lost or unreliable in the text layer with no image: the sphere radii and formulas (13.103)–(13.105) on pp. 357–358; (13.106) on p. 358; (13.135)–(13.139) on p. 366; (13.141) was reconstructed from the surrounding sentence; (13.143) and (13.147) were read from garbled text. I wrote `[unreadable]` or flagged these where used.
- The text gives $\frac{\pi-2}{\pi}\sigma^2=0.3633\sigma^2$ (p. 346); direct arithmetic gives $1-2/\pi=0.36338\ldots$, so the printed value is truncated rather than rounded.
- Section 13.6 is explicitly an outline; Lemma 13.6.2 is not proved in the text (its proof is only outlined in Problem 10), and Lemma 13.8.1's second part is left as an exercise.
- The extension of reverse water-filling to multivariate normal vectors (eigenvalues) and Gaussian processes (spectrum) is stated in words only, without formulas or proof (p. 349). Also, (13.107) on p. 359 was read from a garbled text layer (no image).
