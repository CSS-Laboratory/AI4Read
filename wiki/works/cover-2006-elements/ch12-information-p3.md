---
id: cover-2006-elements/ch12-information-p3
work: cover-2006-elements
unit: "Chapter 12 (part 3/3): Information Theory and Statistics — §12.10 Lempel–Ziv coding, §12.11 Fisher information and the Cramér–Rao inequality, chapter summary, problems, historical notes"
pages: 319-335
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Lempel–Ziv coding, Fisher information and the Cramér–Rao bound

## L0 — One line
Lempel–Ziv parsing compresses any stationary ergodic source, asymptotically and with probability 1, to a length per symbol of at most its entropy rate, without knowing the source, and Fisher information gives the lower bound $1/J(\theta)$ on the variance of any unbiased estimator.

## L1 — The gist (≤ 120 words)
Two questions. (1) Can one simple algorithm compress any stationary ergodic binary source to its entropy rate without knowing the source's distribution? Lempel–Ziv parses the string into new phrases and codes each as a pointer plus one bit. The proof bounds the phrase count $c(n)$ and compares the code to every $k$th-order Markov model (Ziv's inequality). It shows $\limsup \frac1n l \le H(\mathcal X)$ with probability 1. (2) How well can a parameter be estimated from data? The variance of any unbiased estimator is at least $1/J(\theta)$, where $J$ is the Fisher information (variance of the score, i.e. of the derivative of the log-likelihood). The unit ends with the Chapter 12 summary, problems and historical notes.

**Prerequisites:** entropy rate; stationary ergodic processes; Jensen's and Cauchy–Schwarz inequalities; expectation, variance, i.i.d. samples; Markov chains of order $k$; partial derivatives.

## L2 — Key ideas
- Lempel–Ziv splits the input into the shortest strings not seen before ("distinct parsing"). Each phrase is coded as (index of its prefix phrase, last bit). The code length is $c(n)(\log c(n)+1)$ bits (p. 319–320).
- Lemma 12.10.1 bounds the number of phrases: $c(n)\le n/((1-\epsilon_n)\log n)$ with $\epsilon_n\to0$. So $c(n)/n\to0$, which means the one-bit-per-phrase part of the code length, $c(n)/n$ per symbol, vanishes in the limit (p. 320–321).
- Ziv's inequality gives $\log Q_k(x_1^n\mid s_1)\le-\sum c_{ls}\log c_{ls}$ for any distinct parsing. Its right side does not depend on $Q_k$ (p. 323).
- Theorem 12.10.1 and 12.10.2: $\limsup \frac{c(n)\log c(n)}{n}\le H(\mathcal X)$ and $\limsup \frac1n l(X_1^n)\le H(\mathcal X)$, with probability 1. Lempel–Ziv is therefore a universal code, i.e. one that does not depend on the source distribution (p. 324–326).
- The score $V=\partial_\theta\ln f(X;\theta)$ has mean 0. Fisher information is $J(\theta)=\mathrm{var}(V)$, and $J_n=nJ$ for $n$ i.i.d. samples (p. 327–329).
- Cramér–Rao: any unbiased estimator has $\mathrm{var}(T)\ge 1/J(\theta)$, by Cauchy–Schwarz applied to score and estimator. For $N(\theta,\sigma^2)$ the sample mean attains it (p. 329–330).
- The unit gives a bias-corrected bound, a matrix version $\Sigma\ge J^{-1}$, and a pointer to later chapters linking Fisher information to the surface of the typical set (p. 330–331).

## L3 — Walkthrough

### 12.10 Lempel–Ziv coding
**Algorithm** (binary source; the author says it generalises to any finite alphabet) (p. 319). The sequence is parsed left to right into strings not seen before. Each new phrase is the shortest string not yet marked off, so all its prefixes occurred earlier. Each phrase is coded by the location of its prefix (all but the last bit) plus its last bit (p. 319).

Example: $1011010100010\ldots$ is parsed as $1,0,11,01,010,00,10,\ldots$. The code is $(000,1)(000,0)(001,1)(010,1)(100,0)(010,0)(001,0)$. The first entry of each pair is the prefix index (000 = empty prefix). The second is the last bit (p. 319).

With $c(n)$ phrases, each pointer needs $\log c(n)$ bits and the last bit needs 1, so the code length is $c(n)(\log c(n)+1)$ (p. 319–320). The basic version uses two passes: the first computes $c(n)$, the second writes the pointers. Variants with one pass and shorter early pointers exist and do not change the asymptotic efficiency (p. 319–320).

On the short example the string is expanded by more than a factor of 2. The author expects longer strings to compress, because phrases get longer (p. 320).

**Definition.** A *parsing* divides a string into phrases separated by commas. A *distinct parsing* has no two identical phrases. Example: $0,111,1$ is a distinct parsing of $01111$; $0,11,11$ is not (p. 320). The Lempel–Ziv parsing is distinct (p. 320).

**Lemma 12.10.1 (Lempel–Ziv).** In a distinct parsing of a binary sequence of length $n$,
$$c(n)\le \frac{n}{(1-\epsilon_n)\log n},\qquad \epsilon_n\to0 .\tag{12.259}$$
*Proof* (p. 320–321). Let
$$n_k=\sum_{j=1}^k j2^j=(k-1)2^{k+1}+2\tag{12.260}$$
be the total length of all distinct strings of length $\le k$. The number of phrases is largest when phrases are as short as possible. If $n=n_k$, all phrases have length $\le k$, so
$$c(n_k)\le\sum_{j=1}^k2^j=2^{k+1}-2<2^{k+1}\le\frac{n_k}{k-1}.\tag{12.261}$$
If $n_k\le n<n_{k+1}$, write $n=n_k+\Delta$ with $\Delta<(k+1)2^{k+1}$. The shortest-phrase parsing has all phrases of length $\le k$ plus $\Delta/(k+1)$ phrases of length $k+1$. So
$$c(n)\le\frac{n_k}{k-1}+\frac{\Delta}{k+1}\le\frac{n_k+\Delta}{k-1}=\frac{n}{k-1}.\tag{12.262}$$
Now bound $k$. From $n\ge n_k=(k-1)2^{k+1}+2\ge2^k$ (12.263) we get $k\le\log n$ (12.264). Also
$$n\le n_{k+1}=k2^{k+2}+2\le(k+2)2^{k+2}\le(\log n+2)2^{k+2}\tag{12.265}$$
by (12.264). Hence $k+2\ge\log\frac{n}{\log n+2}$ (12.266). For $n\ge4$:
$$k-1\ge\log n-\log(\log n+2)-3=\Big(1-\tfrac{\log(\log n+2)+3}{\log n}\Big)\log n\ \ge\Big(1-\tfrac{\log(2\log n)+3}{\log n}\Big)\log n=\Big(1-\tfrac{\log\log n+4}{\log n}\Big)\log n=(1-\epsilon_n)\log n,$$
(12.267–12.271), with $\epsilon_n=\min\{1,\frac{\log\log n+4}{\log n}\}$. Combining with (12.262) gives the lemma (p. 321).

*Intuition note.* There are only about $2^{k+1}$ strings of length $\le k$. So many phrases force long phrases, and long phrases mean few phrases. That keeps the number of phrases per input symbol, $c(n)/n$, small.

**Lemma 12.10.2.** If $Z$ is positive-integer-valued with mean $\mu$, then
$$H(Z)\le(\mu+1)\log(\mu+1)-\mu\log\mu .\tag{12.272}$$
Proof (p. 322): by Chapter 11 the maximum-entropy pmf under a mean constraint is geometric. Computing its entropy is left as an exercise.

**Markov approximation** (p. 322). Let $\{X_i\}$ be stationary ergodic with pmf $P$. For fixed $k$ define, with $x_i^j=(x_i,\dots,x_j)$ and the initial state $x_{-(k-1)}^0$ part of the specification of $Q_k$,
$$Q_k(x_{-(k-1)},\dots,x_0,x_1,\dots,x_n)\triangleq P(x_{-(k-1)}^0)\prod_{j=1}^nP(x_j\mid x_{j-k}^{j-1}).\tag{12.273}$$
Since $P(X_n|X_{n-k}^{n-1})$ is itself an ergodic process (author's statement),
$$-\tfrac1n\log Q_k(X_1,\dots,X_n\mid X^0_{-(k-1)})=-\tfrac1n\sum_{j=1}^n\log P(X_j|X_{j-k}^{j-1})\to-E\log P(X_j|X_{j-k}^{j-1})=H(X_j|X_{j-k}^{j-1}).\tag{12.274–12.276}$$
The plan is to bound the Lempel–Ziv rate by this Markov entropy rate for every $k$. It converges to the process entropy rate as $k\to\infty$ (p. 322).

**Notation.** Fix $x_{-(k-1)}^n$ and let $x_1^n$ be parsed into $c$ distinct phrases $y_1,\dots,y_c$. Let $\nu_i$ be the start index of $y_i$, so $y_i=x_{\nu_i}^{\nu_{i+1}-1}$. Let $s_i=x_{\nu_i-k}^{\nu_i-1}$ be the $k$ bits preceding $y_i$, with $s_1=x^0_{-(k-1)}$. Let $c_{ls}$ be the number of phrases with length $l$ and preceding state $s\in\mathcal X^k$. Then
$$\sum_{l,s}c_{ls}=c,\qquad\sum_{l,s}lc_{ls}=n.\tag{12.277–12.278}$$

**Lemma 12.10.3 (Ziv's inequality).** For any distinct parsing of $x_1\dots x_n$,
$$\log Q_k(x_1,\dots,x_n\mid s_1)\le-\sum_{l,s}c_{ls}\log c_{ls}.\tag{12.279}$$
The right side does not depend on $Q_k$ (p. 323).
*Proof* (p. 323). $Q_k(x_1^n|s_1)=Q(y_1,\dots,y_c|s_1)=\prod_{i=1}^cP(y_i|s_i)$ (12.280–12.281). Then
$$\log Q_k=\sum_i\log P(y_i|s_i)=\sum_{l,s}\ \sum_{i:|y_i|=l,s_i=s}\log P(y_i|s_i)=\sum_{l,s}c_{ls}\sum_{i:|y_i|=l,s_i=s}\tfrac1{c_{ls}}\log P(y_i|s_i)$$
$$\le\sum_{l,s}c_{ls}\log\Big(\sum_{i:|y_i|=l,s_i=s}\tfrac1{c_{ls}}P(y_i|s_i)\Big),$$
(12.282–12.285). The inequality is Jensen's, using concavity of log. Because the $y_i$ are distinct, $\sum_{i:|y_i|=l,s_i=s}P(y_i|s_i)\le1$. So
$$\log Q_k(x_1^n|s_1)\le\sum_{l,s}c_{ls}\log\frac1{c_{ls}}.\tag{12.286}$$

*Intuition note.* Phrases that share length and context must be different strings. Their conditional probabilities $P(y_i|s_i)$ therefore sum to at most 1, and Jensen's inequality then caps how likely the whole string can be under $Q_k$.

**Theorem 12.10.1.** For a stationary ergodic process with entropy rate $H(\mathcal X)$, and $c(n)$ the number of phrases in a distinct parsing of a length-$n$ sample,
$$\limsup_{n\to\infty}\frac{c(n)\log c(n)}{n}\le H(\mathcal X)\quad\text{with probability 1.}\tag{12.287}$$
*Proof* (p. 324–325). Rewrite Ziv's inequality:
$$\log Q_k(x_1^n|s_1)\le-\sum c_{ls}\log\frac{c_{ls}c}{c}=-c\log c-c\sum\frac{c_{ls}}{c}\log\frac{c_{ls}}{c}.\tag{12.288–12.289}$$
Put $\pi_{ls}=c_{ls}/c$. Then $\sum\pi_{ls}=1$ and $\sum l\pi_{ls}=n/c$ (12.290). Define $(U,V)$ with $\Pr(U=l,V=s)=\pi_{ls}$ (12.291), so $EU=n/c$ and
$$\log Q_k(x_1^n|s_1)\le cH(U,V)-c\log c,\quad\text{i.e.}\quad -\tfrac1n\log Q_k\ge\tfrac cn\log c-\tfrac cnH(U,V).\tag{12.292–12.293}$$
Now $H(U,V)\le H(U)+H(V)$ (12.294) and $H(V)\le\log|\mathcal X|^k=k$. By Lemma 12.10.2,
$$H(U)\le(EU+1)\log(EU+1)-EU\log EU=\big(\tfrac nc+1\big)\log\big(\tfrac nc+1\big)-\tfrac nc\log\tfrac nc=\log\tfrac nc+\big(\tfrac nc+1\big)\log\big(\tfrac cn+1\big).\tag{12.295–12.297}$$
Thus
$$\tfrac cnH(U,V)\le\tfrac cnk+\tfrac cn\log\tfrac nc+o(1).\tag{12.298}$$
For given $n$, $\frac cn\log\frac nc$ is largest at the largest $c$ (for $c/n\le1/e$). By Lemma 12.10.1, $c\le\frac n{\log n}(1+o(1))$. So $\frac cn\log\frac nc\le O\big(\frac{\log\log n}{\log n}\big)$ (12.299), and $\frac cnH(U,V)\to0$. Therefore
$$\frac{c(n)\log c(n)}n\le-\tfrac1n\log Q_k(x_1^n|s_1)+\epsilon_k(n),\quad\epsilon_k(n)\to0.\tag{12.300}$$
With probability 1,
$$\limsup\frac{c(n)\log c(n)}n\le\lim-\tfrac1n\log Q_k(X_1^n|X^0_{-(k-1)})=H(X_0|X_{-1},\dots,X_{-k})\to H(\mathcal X)\ \text{as }k\to\infty.\tag{12.301–12.303}$$

**Theorem 12.10.2.** Let $l(X_1,\dots,X_n)$ be the Lempel–Ziv codeword length. For a stationary ergodic process,
$$\limsup\frac1nl(X_1,\dots,X_n)\le H(\mathcal X)\quad\text{with probability 1.}\tag{12.304}$$
*Proof* (p. 325). $l=c(n)(\log c(n)+1)$. By Lemma 12.10.1, $\limsup c(n)/n=0$. Hence $\limsup\frac ln=\limsup\big(\frac{c\log c}n+\frac cn\big)\le H(\mathcal X)$ by Theorem 12.10.1 (12.305).

*Intuition note.* The code never uses the source distribution, yet its length per symbol is asymptotically no greater than the entropy rate (the theorem proved is an upper bound). The proof compares the code with the $k$th-order Markov approximation for every $k$, and the Markov entropy rate converges to $H(\mathcal X)$ as $k\to\infty$ (p. 322, 325).

**Remarks** (p. 326). The author calls Lempel–Ziv a simple *universal code*: one that does not depend on the source distribution. It is the standard file-compression algorithm (the author names the `compress` and `arc` programs). It typically compresses ASCII text by about a factor of 2. It has also been implemented in hardware to roughly double the capacity of communication links for text (p. 326).

### 12.11 Fisher information and the Cramér–Rao inequality
**Motivation** (p. 326). Example: $X_1,\dots,X_n$ i.i.d. $N(\theta,1)$; to estimate $\theta$ one could use $X_1$, but the author guesses and states that the sample mean $\bar X_n$ is better. It "can be shown" that $\bar X_n$ is the minimum mean-squared-error unbiased estimator (p. 326).

**Definitions** (p. 326–327). Let $\{f(x;\theta)\}$, $\theta\in\Theta$, be a family of densities; $\Theta$ is the parameter set. An *estimator* is a function $T:\mathcal X^n\to\Theta$. The *error* is $T-\theta$ (a random variable). The *bias* is $E_\theta T-\theta$; the estimator is *unbiased* if the bias is zero.

*Example 12.11.1.* For i.i.d. exponential $f(x)=\frac1\lambda e^{-x/\lambda}$, $x\ge0$, both $X_1$ and $\bar X_n$ are unbiased estimators of $\lambda$ (p. 327).

Zero bias does not guarantee a small error, so a loss is used; the usual one is expected squared error. An estimator is *consistent in probability* if $T(X_1,\dots,X_n)\to\theta$ in probability as $n\to\infty$. $T_1$ *dominates* $T_2$ if for all $\theta$
$$E_\theta(T_1-\theta)^2\le E_\theta(T_2-\theta)^2.\tag{12.306}$$
(p. 327)

**Score and Fisher information.** The *score* is
$$V=\frac\partial{\partial\theta}\ln f(X;\theta)=\frac{\frac\partial{\partial\theta}f(X;\theta)}{f(X;\theta)},\qquad X\sim f(x;\theta).\tag{12.307}$$
Its mean:
$$EV=\int\frac{\frac\partial{\partial\theta}f(x;\theta)}{f(x;\theta)}f(x;\theta)dx=\int\frac\partial{\partial\theta}f(x;\theta)dx=\frac\partial{\partial\theta}\int f(x;\theta)dx=\frac\partial{\partial\theta}1=0,\tag{12.308–12.312}$$
so $EV^2=\mathrm{var}(V)$ (p. 327–328). The *Fisher information* is the variance of the score:
$$J(\theta)=E_\theta\Big[\frac\partial{\partial\theta}\ln f(X;\theta)\Big]^2.\tag{12.313}$$
For i.i.d. $X_1,\dots,X_n$ with $f(x_1,\dots,x_n;\theta)=\prod f(x_i;\theta)$ (12.314), the score is a sum of i.i.d. zero-mean scores:
$$V(X_1,\dots,X_n)=\sum_{i=1}^n\frac\partial{\partial\theta}\ln f(X_i;\theta)=\sum_iV(X_i).\tag{12.315–12.317}$$
Hence
$$J_n(\theta)=E_\theta V^2(X_1,\dots,X_n)=E_\theta\Big(\sum V(X_i)\Big)^2=\sum E_\theta V^2(X_i)=nJ(\theta).\tag{12.318–12.322}$$
(Added step: cross terms vanish because the $V(X_i)$ are independent with mean 0.) (p. 328–329.)

**Theorem 12.11.1 (Cramér–Rao).** The mean squared error of any unbiased estimator $T(X)$ of $\theta$ satisfies
$$\mathrm{var}(T)\ge\frac1{J(\theta)}.\tag{12.323}$$
*Proof* (p. 329–330). Cauchy–Schwarz gives
$$\big(E_\theta[(V-E_\theta V)(T-E_\theta T)]\big)^2\le E_\theta(V-E_\theta V)^2E_\theta(T-E_\theta T)^2.\tag{12.324}$$
Since $E_\theta V=0$, the left side is $[E_\theta(VT)]^2$, and $\mathrm{var}(V)=J(\theta)$. So $[E_\theta(VT)]^2\le J(\theta)\mathrm{var}(T)$ (12.325). Now
$$E_\theta(VT)=\int\frac{\frac\partial{\partial\theta}f}{f}T f\,dx=\int\frac\partial{\partial\theta}f(x;\theta)T(x)dx=\frac\partial{\partial\theta}\int f(x;\theta)T(x)dx=\frac\partial{\partial\theta}E_\theta T=\frac\partial{\partial\theta}\theta=1.\tag{12.326–12.331}$$
The interchange of derivative and integral (12.328) can be justified by the bounded convergence theorem "for appropriately well behaved" $f(x;\theta)$. Step (12.330) uses unbiasedness. Substituting gives $1\le J(\theta)\mathrm{var}(T)$, i.e. (12.332).

*Intuition note.* The score measures how fast the likelihood changes when $\theta$ moves. Unbiasedness gives $\frac{\partial}{\partial\theta}E_\theta T=1$, which is $E_\theta(VT)=1$ (12.326–12.331); so $T$ is correlated with the score. Cauchy–Schwarz then limits how small $\mathrm{var}(T)$ can be (12.325).

**Biased estimators.** By essentially the same argument, for any estimator,
$$E_\theta(T-\theta)^2\ge\frac{[1+b_T'(\theta)]^2}{J(\theta)}+b_T^2(\theta),\tag{12.333}$$
where $b_T(\theta)=E_\theta T-\theta$. The proof is left as an exercise (p. 330).

*Example 12.11.2.* For $X_i$ i.i.d. $N(\theta,\sigma^2)$ with $\sigma^2$ known, $J(\theta)=n/\sigma^2$. For $T=\bar X_n$, $E_\theta(\bar X_n-\theta)^2=\sigma^2/n=1/J(\theta)$. So $\bar X_n$ is the minimum-variance unbiased estimator, since it meets the bound (p. 330).

**Efficiency.** An unbiased $T$ is *efficient* if $\mathrm{var}(T)=1/J(\theta)$. Fisher information measures the "information" about $\theta$ in the data and gives a lower bound on estimation error. The author notes that an estimator meeting the bound may not exist (p. 330).

**Multiparameter case.** The Fisher information matrix has entries
$$J_{ij}(\theta)=\int f(x;\theta)\frac\partial{\partial\theta_i}\ln f(x;\theta)\frac\partial{\partial\theta_j}\ln f(x;\theta)dx.\tag{12.334}$$
The inequality becomes $\Sigma\ge J^{-1}(\theta)$ (12.335). Here $\Sigma$ is the covariance matrix of unbiased estimators, and "$\ge$" means $\Sigma-J^{-1}$ is non-negative definite. The proof is not given (p. 330).

**Link to entropy** (p. 331). Fisher information needs a parametric family; entropy does not. Any density $f(x)$ can be given a location parameter via the family $\{f(x-\theta)\}$. The author defers details to Section 16.7 (not in this unit), saying entropy relates to the volume of the typical set and Fisher information to its surface area. Relations to relative entropy are left to the exercises (p. 331).

### Summary of Chapter 12 (p. 331–332)
The chapter summary restates results from earlier parts, which this unit does not derive:
- Types: $Q^n(x)=2^{-n(D(P_x\|Q)+H(P_x))}$ (12.336); $|\mathcal P_n|\le(n+1)^{|\mathcal X|}$ (12.337); $|T(P)|\le2^{nH(P)}$ (12.338); $Q^n(T(P))\doteq2^{-nD(P\|Q)}$ (12.339).
- Universal compression: $P_e^{(n)}\doteq2^{-nD(P^*_R\|Q)}$ for all $Q$ (12.340). The formula (12.341) defining $P^*_R$ is not legible in the text layer. Problem 3 says $P^*$ minimises $D(P\|Q)$ over $P$ with $H(P)\ge R$.
- Sanov: $Q^n(E)=Q^n(E\cap\mathcal P_n)\le(n+1)^{|\mathcal X|}2^{-nD(P^*\|Q)}$ (12.342), with $D(P^*\|Q)=\min_{P\in E}D(P\|Q)$ (12.343). If $E$ is the closure of its interior, $Q^n(E)\doteq2^{-nD(P^*\|Q)}$ (12.344).
- Pythagorean theorem: for a convex set $E$ of types, $Q\notin E$, and $P^*$ the minimiser, $D(P\|Q)\ge D(P\|P^*)+D(P^*\|Q)$ for all $P\in E$ (12.346).
- Conditional limit: $\Pr(X_1=a|P_{X^n}\in E)\to P^*(a)$ in probability (12.347). In particular $\Pr\{X_1=a\mid\frac1n\sum X_i\ge\alpha\}\to\frac{Q(a)e^{\lambda a}}{\sum_xQ(x)e^{\lambda x}}$ (12.348).
- Neyman–Pearson: the optimal test has region "accept $P_1$ if $P_1(x^n)/P_2(x^n)>T$".
- Stein: $\beta_n^\epsilon=\min_{A_n\subset\mathcal X^n,\alpha_n<\epsilon}\beta_n$ (12.349); $\lim_{\epsilon\to0}\lim_{n\to\infty}\frac1n\log\beta_n^\epsilon=-D(P_1\|P_2)$ (12.350).
- Chernoff information: $D^*=D(P_{\lambda^*}\|P_1)=D(P_{\lambda^*}\|P_2)$ (12.351), with $P_\lambda=\frac{P_1^\lambda(x)P_2^{1-\lambda}(x)}{\sum_aP_1^\lambda(a)P_2^{1-\lambda}(a)}$ (12.352), and $\lambda^*$ chosen so $D(P_\lambda\|P_1)=D(P_\lambda\|P_2)$ (12.353).
- Lempel–Ziv (12.354), Fisher information (12.355) and Cramér–Rao (12.356) as above.
- An $L_1$ bound on relative entropy (12.345) is listed but its formula is not legible here.

### Problems and historical notes (p. 333–335)
Twelve problems: Stein's lemma divergences, the $\chi^2$ statistic as twice the first term of the Taylor expansion of $D(P\|Q)$, error exponents for universal codes, sequential projection, counting with a constraint, biased estimators, Fisher information versus relative entropy (12.364), Fisher-information examples, two looks doubling $J$, joint versus product distributions, Cramér–Rao with a bias term (12.367), and a Lempel–Ziv parsing task (p. 333–335).

Historical notes (p. 335), as printed: the method of types was fully developed by Csiszár and Körner. The Lempel–Ziv parsing was introduced by Lempel and Ziv, and Ziv proved it achieves the entropy rate. The proof in §12.10 follows the "more transparent" proof of Wyner and Ziv. Variants are in Bell, Cleary and Witten.

## Toy example (ours, not from the text)
**A. Lempel–Ziv parse.** String $0010101$. Scan: "0" is new (phrase 1). Next "0" is seen, "01" is new (phrase 2). Next "0" and "01" are seen, "010" is new (phrase 3). Next "1" is new (phrase 4). Parsing: $0,01,010,1$, which is distinct, with $c=4$. Pairs (prefix phrase index, last bit), index 0 = empty prefix:
- phrase "0": prefix empty, last bit 0, giving $(0,0)$;
- phrase "01": prefix "0" = phrase 1, giving $(1,1)$;
- phrase "010": prefix "01" = phrase 2, giving $(2,0)$;
- phrase "1": prefix empty, giving $(0,1)$.

Decoding rebuilds $0\,|\,0{+}1\,|\,01{+}0\,|\,1$. By the author's formula the length is $c(\log c+1)=4(2+1)=12$ bits for 7 input symbols. It expands, as in the author's example, because the string is short.

**B. Fisher information.** Bernoulli($p$) with $p=1/4$. Score: $V=x/p-(1-x)/(1-p)$. For $x=1$, $V=4$; for $x=0$, $V=-1/(3/4)=-4/3$. $EV=\frac14\cdot4+\frac34\cdot(-\frac43)=1-1=0$. $EV^2=\frac14\cdot16+\frac34\cdot\frac{16}9=4+\frac43=\frac{16}3=J(p)$, which equals $1/(p(1-p))=1/(3/16)$. For $n=8$ samples, $J_8=8\cdot\frac{16}3$, so the bound is $\frac{3}{128}$. The sample mean has variance $p(1-p)/n=\frac3{16}/8=\frac3{128}$, so it meets the bound (efficient).

## Concepts
- [[universal-coding]] — a code needing no knowledge of the source distribution; Lempel–Ziv is the unit's example (p. 326)
- [[lempel-ziv-coding]] (new) — parse into shortest unseen phrases; code each as (prefix index, last bit) (p. 319)
- [[distinct-parsing]] (new) — a division of a string into phrases with no repeats (p. 320)
- [[ziv-inequality]] (new) — $\log Q_k(x_1^n|s_1)\le-\sum c_{ls}\log c_{ls}$ for any distinct parsing (p. 323)
- [[entropy-rate]] — here $H(\mathcal X)$ of a stationary ergodic process; limit of $H(X_j|X_{j-k}^{j-1})$ as $k\to\infty$ (p. 322)
- [[score-function]] (new) — $\partial_\theta\ln f(X;\theta)$; has mean zero (p. 327)
- [[fisher-information]] — variance of the score, $J(\theta)=E_\theta[\partial_\theta\ln f]^2$; $J_n=nJ$ for i.i.d. data (p. 328)
- [[cramer-rao-bound]] (new) — any unbiased estimator has $\mathrm{var}\ge1/J(\theta)$ (p. 329)
- [[efficient-estimator]] (new) — an unbiased estimator that meets the Cramér–Rao bound with equality (p. 330)
- [[unbiased-estimator]] (new) — an estimator with $E_\theta T=\theta$ for all $\theta$ (p. 326–327)
- [[method-of-types]] — recalled only in the chapter summary (p. 331)

## Canonical instances
- [[lz-parsing-example]] — $1011010100010\ldots\to1,0,11,01,010,00,10$ with its code pairs (p. 319)
- [[exponential-estimators-example]] — $X_1$ and $\bar X_n$ both unbiased for $\lambda$ (Ex. 12.11.1, p. 327)
- [[gaussian-mean-efficiency]] — $\bar X_n$ attains $\sigma^2/n=1/J(\theta)$ for $N(\theta,\sigma^2)$ (Ex. 12.11.2, p. 330)

## Bridges (candidates)
- [structural-analogy] Lempel–Ziv universality (no source model needed) ↔ Kolmogorov complexity / universal coding: both compress without knowing the source.
- [same-math] Fisher information $J(\theta)$ ↔ relative entropy: Problem 7 asks the reader to show $\lim_{\theta'\to\theta}\frac{D(p_\theta\|p_{\theta'})}{(\theta-\theta')^2}=\frac1{\ln4}J(\theta)$. Fisher information is the local, second-order form of KL.
- [structural-analogy] Ziv's inequality (distinct phrases cap string probability) ↔ Kraft inequality: both turn a counting constraint into a bound on code length.

## Questions this raises
- The theorems give only $\limsup\le H(\mathcal X)$. Does the limit actually equal $H(\mathcal X)$ (a matching lower bound)?
- When does an efficient estimator exist, given that the author says it may not?
- How fast does $c(n)\log c(n)/n$ approach the entropy rate for finite $n$? The example expands the data.
- How exactly are the typical set's volume and surface area linked to entropy and Fisher information (the promised §16.7)?

## Exercises worth doing
- Ex. 12 (p. 335) — hand-run the Lempel–Ziv parse and encode a 23-bit string — difficulty: easy
- Ex. 9 (p. 334) — two i.i.d. looks double $J(\theta)$ — difficulty: easy
- Ex. 8 (p. 334) — compute $J(\theta)$ for Gaussian-variance and exponential families, then the Cramér–Rao bound — difficulty: easy
- Ex. 6 (p. 334) — a biased variance estimator can have lower MSE — difficulty: medium
- Ex. 7 (p. 334) — Fisher information as the local form of relative entropy — difficulty: medium
- Ex. 11 (p. 335) — Cramér–Rao with a bias term (12.367) — difficulty: medium

## Reading notes
- This part covers printed pp. 319–335; pdf pages 341–357. Offset: printed = pdf − 22.
- It starts with a short fragment at the top of p. 319, the end of the previous section's proof (eq. 12.258, apparently applying Markov's inequality), that is garbled in the text layer and not digested. §12.10 starts on p. 319. The unit ends with Historical Notes (p. 335).
- The PDF is the 1991 first edition, as the source note says, so numbering and content differ from the 2nd edition.
- OCR problems. Several equations (12.259, 12.261, 12.263–12.269, 12.274–12.276 and others) were garbled in the text layer. I checked them against the page images for pdf 343–347, 349–352, 354–357. Page images for pdf 341, 342, 348 and 353 were not supplied, so (12.258–12.260), the text on pp. 319–320 and 326, and the chapter-summary text on p. 331 (including 12.336–12.345) rely on the text layer.
- The sentence on p. 320 announcing the target result is garbled in the text layer (it seems to concern $c(n)(\log c(n)+1)/n$ and $H$; no page image was supplied). Only the $\limsup\le H(\mathcal X)$ results (12.287, 12.304) are actually proved, and these are what I report.
- In (12.290) the page prints "(12.227)", which looks like a misprint for (12.277). I used (12.277)–(12.278).
- In the summary, formulas (12.341) and (12.345) are not legible. In the text layer $\theta$ often appears as "0", "8", "e" or "6" (e.g. p. 326 "N( 0, 1)", Problems 6–8, (12.356)); I read $\theta$ from the images where supplied and from context otherwise.
- The Historical Notes cite the same reference numbers ([175], [289]) for different works; I report the text as printed.
