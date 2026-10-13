---
id: cover-2006-elements/ch12-information-p1
work: cover-2006-elements
unit: "12 Information Theory and Statistics (part 1/3): 12.1–12.5"
pages: 279–296
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
# The method of types, universal coding and Sanov's theorem

## L0 — One line
Grouping sequences by their empirical distribution ("type") gives sharp exponential estimates of class sizes and class probabilities (and an exact formula for a single sequence) in terms of entropy $H(P)$ and relative entropy $D(P\|Q)$, which yield the law of large numbers, universal codes and Sanov's large-deviation theorem.

## L1 — The gist (≤ 120 words)
How likely is a long i.i.d. sequence to look like a distribution other than the one that generated it? The method of types answers this. There are only polynomially many types, each type class has about $2^{nH(P)}$ sequences, and its probability under $Q$ is about $2^{-nD(P\|Q)}$. Consequences: the sample type converges to the true distribution; one fixed-rate code compresses every i.i.d. source with entropy below $R$; and the probability of a rare set $E$ of types is at most about $2^{-nD(P^*\|Q)}$, with the same exponent when $E$ is well-behaved (Sanov), where $P^*$ is the member of $E$ closest to $Q$. Examples: dice averages, coin heads, joint typicality.

**Prerequisites:** entropy, relative entropy, i.i.d. sequences, multinomial coefficients, binomial formula, Lagrange multipliers, the AEP.

## L2 — Key ideas
- A type is the empirical distribution of a sequence. There are at most $(n+1)^{|\mathcal X|}$ types, so polynomially many against exponentially many sequences (p. 280–281).
- Under i.i.d. $Q$, the probability of a sequence depends only on its type: $Q^n(x)=2^{-n(H(P_x)+D(P_x\|Q))}$ (p. 281).
- A type class has size between $(n+1)^{-|\mathcal X|}2^{nH(P)}$ and $2^{nH(P)}$. Its $Q^n$-probability is within the same polynomial factor of $2^{-nD(P\|Q)}$ (pp. 282, 285).
- Types far from $Q$ in $D$ have exponentially small probability. This gives a typical-set form of the law of large numbers and $D(P_{x^n}\|P)\to0$ with probability 1 (pp. 286–287).
- Universal source coding: index all sequences whose type has entropy $\le R_n$. This code does not depend on $Q$ and has vanishing error whenever $H(Q)<R$ (pp. 288–290).
- Sanov's theorem: $Q^n(E)\le (n+1)^{|\mathcal X|}2^{-nD(P^*\|Q)}$, with matching exponent for "nice" $E$ (pp. 292–294).
- The closest distribution $P^*$ under expectation constraints has exponential-tilting form $\propto Q\,e^{\sum\lambda_i g_i}$ (pp. 294–295).
- Examples: dice average $\ge4$, more than 700 heads in 1000 tosses, and joint typicality of a product-distribution sample, which gives $2^{-nI(X;Y)}$ (pp. 295–296).

## L3 — Walkthrough

### Chapter intro
The chapter links information theory and statistics: the method of types, large deviations, universal source codes, hypothesis testing (Stein's lemma) and Fisher information (p. 279). This part covers 12.1–12.5 only.

### 12.1 The method of types
The AEP concentrates attention on typical sequences. The method of types is stronger: it groups sequences with the same empirical distribution (p. 279). Alphabet $\mathcal X=\{a_1,\dots,a_{|\mathcal X|}\}$.

**Definitions** (pp. 279–280).
- **Type** $P_x$ of $x$: $P_x(a)=N(a|x)/n$, where $N(a|x)$ counts occurrences of $a$ in $x$.
- $\mathcal P_n$ is the set of types with denominator $n$. For a binary alphabet, $\mathcal P_n=\{(\tfrac0n,\tfrac nn),(\tfrac1n,\tfrac{n-1}n),\dots,(\tfrac nn,\tfrac0n)\}$ (12.1).
- **Type class** of $P\in\mathcal P_n$: $T(P)=\{x\in\mathcal X^n:P_x=P\}$ (12.2).

**Example 12.1.1.** $\mathcal X=\{1,2,3\}$, $x=11321$. Then $P_x=(3/5,1/5,1/5)$ (12.3). $T(P_x)$ is all length-5 sequences with three 1's, one 2 and one 3. Its size is $\binom{5}{3,1,1}=\frac{5!}{3!1!1!}=20$ (12.4–12.5) (p. 280).

**Theorem 12.1.1.** $|\mathcal P_n|\le(n+1)^{|\mathcal X|}$ (12.6). *Proof:* the type vector has $|\mathcal X|$ components, each numerator takes at most $n+1$ values. The components are not independent, but the bound suffices (p. 281).

Consequence: sequences number exponentially many in $n$ but types only polynomially many. So some type class is exponentially large, and the largest has the same count as all sequences to first order in the exponent (p. 281).

**Theorem 12.1.2.** For $X_i$ i.i.d. $\sim Q$, with $Q^n(x)=\prod_i Q(x_i)$:
$$Q^n(x)=2^{-n(H(P_x)+D(P_x\|Q))}\tag{12.7}$$
*Proof* (p. 281):
$$Q^n(x)=\prod_{i=1}^n Q(x_i)=\prod_{a}Q(a)^{N(a|x)}=\prod_a Q(a)^{nP_x(a)}=\prod_a 2^{nP_x(a)\log Q(a)}$$
$$=\prod_a 2^{n(P_x(a)\log Q(a)-P_x(a)\log P_x(a)+P_x(a)\log P_x(a))}=2^{n\sum_a(-P_x(a)\log\frac{P_x(a)}{Q(a)}+P_x(a)\log P_x(a))}=2^{n(-D(P_x\|Q)-H(P_x))}.$$
(12.8–12.14)

**Corollary.** If $x\in T(Q)$, then $Q^n(x)=2^{-nH(Q)}$ (12.15), because $P_x=Q$ (pp. 281–282).

**Example 12.1.2** (p. 282). A fair die yields a particular sequence with exactly $n/6$ of each face with probability $2^{-nH(1/6,\dots,1/6)}=6^{-n}$. For pmf $(\tfrac13,\tfrac13,\tfrac16,\tfrac1{12},\tfrac1{12},0)$ and $n$ a multiple of 12, a particular sequence with exactly these frequencies has probability $2^{-nH(\frac13,\frac13,\frac16,\frac1{12},\frac1{12},0)}$.

> *Intuition note.* Every sequence with the same counts has the same probability, so probability depends on the sequence only through its type. Its value is $2^{-n(H(P_x)+D(P_x\|Q))}$.

**Theorem 12.1.3** (size of a type class). For $P\in\mathcal P_n$:
$$\frac1{(n+1)^{|\mathcal X|}}2^{nH(P)}\le|T(P)|\le2^{nH(P)}\tag{12.16}$$
*Proof* (p. 282–284). The exact size is the multinomial coefficient $|T(P)|=\binom{n}{nP(a_1),\dots,nP(a_{|\mathcal X|})}$ (12.17). The author notes a Stirling-formula proof and gives an alternative.
- *Upper bound.* $1\ge P^n(T(P))=\sum_{x\in T(P)}P^n(x)=\sum_{x\in T(P)}2^{-nH(P)}=|T(P)|2^{-nH(P)}$ by Theorem 12.1.2 (12.18–12.21). So $|T(P)|\le2^{nH(P)}$ (12.22).
- *Lower bound, step 1:* $T(P)$ has the highest $P^n$-probability among all type classes: $P^n(T(P))\ge P^n(T(\hat P))$ for all $\hat P\in\mathcal P_n$ (12.23). The ratio is
$$\frac{P^n(T(P))}{P^n(T(\hat P))}=\frac{|T(P)|\prod_aP(a)^{nP(a)}}{|T(\hat P)|\prod_aP(a)^{n\hat P(a)}}=\prod_a\frac{(n\hat P(a))!}{(nP(a))!}P(a)^{n(P(a)-\hat P(a))}\tag{12.24–12.26}$$
Using $\frac{m!}{n!}\ge n^{m-n}$ (12.27; easy by cases $m\ge n$, $m<n$):
$$\ge\prod_a(nP(a))^{n\hat P(a)-nP(a)}P(a)^{n(P(a)-\hat P(a))}=\prod_a n^{n(\hat P(a)-P(a))}=n^{n(\sum\hat P-\sum P)}=n^{n(1-1)}=1.$$
(12.28–12.32)
- *Lower bound, step 2:* $1=\sum_{Q\in\mathcal P_n}P^n(T(Q))\le\sum_Q\max_QP^n(T(Q))=\sum_QP^n(T(P))\le(n+1)^{|\mathcal X|}P^n(T(P))=(n+1)^{|\mathcal X|}\sum_{x\in T(P)}P^n(x)=(n+1)^{|\mathcal X|}\sum_{x\in T(P)}2^{-nH(P)}=(n+1)^{|\mathcal X|}|T(P)|2^{-nH(P)}$. The inequality (12.36) uses Theorem 12.1.1 and the equality (12.38) uses Theorem 12.1.2 (12.33–12.39) (pp. 283–284).

**Example 12.1.3** (binary, p. 284–285). Type class size is $\binom nk$ and
$$\frac1{n+1}2^{nH(k/n)}\le\binom nk\le2^{nH(k/n)}\tag{12.40}$$
- *Upper:* in $\sum_k\binom nkp^k(1-p)^{n-k}=1$ (12.41), each term is $\le1$. Take $p=k/n$ and the $k$th term: $1\ge\binom nk(\tfrac kn)^k(1-\tfrac kn)^{n-k}=\binom nk2^{-nH(k/n)}$ (12.42–12.46).
- *Lower:* for $S\sim$ Binomial$(n,p)$, the most likely value is $\langle np\rangle$, from $\frac{P(S=i+1)}{P(S=i)}=\frac{n-i}{i+1}\frac p{1-p}$ (12.47). With $n+1$ terms, $1\le(n+1)\max_k\binom nkp^k(1-p)^{n-k}=(n+1)\binom n{\langle np\rangle}p^{\langle np\rangle}(1-p)^{n-\langle np\rangle}$ (12.48–12.49). Setting $p=k/n$ gives $\binom nk\ge\frac{2^{nH(k/n)}}{n+1}$ (12.50–12.52). Hence $\binom nk\doteq2^{nH(k/n)}$ (12.53), where $\doteq$ means equal to first order in the exponent.

**Theorem 12.1.4** (probability of a type class). For $P\in\mathcal P_n$ and any $Q$:
$$\frac1{(n+1)^{|\mathcal X|}}2^{-nD(P\|Q)}\le Q^n(T(P))\le2^{-nD(P\|Q)}\tag{12.54}$$
*Proof:* $Q^n(T(P))=\sum_{x\in T(P)}Q^n(x)=|T(P)|2^{-n(D(P\|Q)+H(P))}$ by Theorem 12.1.2. Then apply the bounds of Theorem 12.1.3 (12.55–12.58) (pp. 285–286).

**Summary** (12.59–12.62, p. 286):
$|\mathcal P_n|\le(n+1)^{|\mathcal X|}$; $Q^n(x)=2^{-n(D(P_x\|Q)+H(P_x))}$; $|T(P)|\doteq2^{nH(P)}$; $Q^n(T(P))\doteq2^{-nD(P\|Q)}$. The author lists coming uses: law of large numbers, universal source coding, Sanov's theorem, Stein's lemma and hypothesis testing, conditional probability and limit theorems (p. 286).

> *Intuition note.* Think of types as a small number of "bins" (polynomially many). Each bin holds exponentially many sequences. To first order in the exponent, a bin's total probability is set by how far its type is from $Q$, measured by $D$.

### 12.2 The law of large numbers
Because the probability of a type class falls exponentially in $D(P\|Q)$, classes far from $Q$ are exponentially unlikely (p. 287). Define the typical set $T_Q^\epsilon=\{x^n:D(P_{x^n}\|Q)\le\epsilon\}$ (12.63). Then
$$1-Q^n(T_Q^\epsilon)=\sum_{P:D(P\|Q)>\epsilon}Q^n(T(P))\le\sum_{P:D>\epsilon}2^{-nD(P\|Q)}\le\sum_{P:D>\epsilon}2^{-n\epsilon}\le(n+1)^{|\mathcal X|}2^{-n\epsilon}=2^{-n(\epsilon-|\mathcal X|\frac{\log(n+1)}n)}$$
using Theorem 12.1.4, then the definition of the set, then Theorem 12.1.1 (12.64–12.68). This tends to 0, so $Q^n(T_Q^\epsilon)\to1$, similar to the AEP (p. 287).

**Theorem 12.2.1.** For $X_i$ i.i.d. $\sim P$: $\Pr\{D(P_{x^n}\|P)>\epsilon\}\le2^{-n(\epsilon-|\mathcal X|\frac{\log(n+1)}n)}$ (12.69), and $D(P_{x^n}\|P)\to0$ with probability 1. *Proof:* (12.69) was shown in (12.68). The sum over $n$ is finite (12.70), so the expected number of $n$ with $D>\epsilon$ is finite. By the Borel–Cantelli lemma the actual number is finite with probability 1 (p. 287).

**Strongly typical set** (12.71): $A_\epsilon^{(n)}=\{x\in\mathcal X^n:|\frac1nN(a|x)-P(a)|<\frac\epsilon{|\mathcal X|}\ \forall a\}$. Its probability goes to 1 by the strong law of large numbers. It is said to help in universal coding, rate distortion and large deviation theory (p. 288).

### 12.3 Universal source coding
Huffman coding reaches $H(X)$ for known $p$. If designed for a wrong $q$, it pays a penalty $D(p\|q)$ (p. 288). **Question:** is there one code of rate $R$ that works for every i.i.d. source with $H<R$? The answer given is yes (p. 288).

Idea: there are $2^{nH(P)}$ sequences of type $P$ and only polynomially many types. So listing all sequences whose type has $H(P_{x^n})<R$ costs about $nR$ bits (p. 288).

**Definitions** (pp. 288–289). A *fixed-rate block code of rate $R$* for a source with unknown $Q$ has an encoder $f_n:\mathcal X^n\to\{1,\dots,2^{nR}\}$ (12.72) and a decoder $\phi_n:\{1,\dots,2^{nR}\}\to\mathcal X^n$ (12.73). Its error is $P_e^{(n)}=Q^n(\phi_n(f_n(X))\ne X)$ (12.74). The code is *universal* if $f_n,\phi_n$ do not depend on $Q$ and $P_e^{(n)}\to0$ whenever $R>H(Q)$.

**Theorem 12.3.1.** There exists a sequence of $(2^{nR},n)$ universal source codes with $P_e^{(n)}\to0$ for every source $Q$ with $H(Q)<R$ (scheme due to Csiszár and Körner) (p. 289).

*Proof.* Let $R_n=R-|\mathcal X|\frac{\log(n+1)}n$ (12.75) and $A=\{x:H(P_x)\le R_n\}$ (12.76). Then
$$|A|=\sum_{P\in\mathcal P_n:H(P)\le R_n}|T(P)|\le\sum2^{nH(P)}\le\sum2^{nR_n}\le(n+1)^{|\mathcal X|}2^{nR_n}=2^{n(R_n+|\mathcal X|\frac{\log(n+1)}n)}=2^{nR}$$
(12.77–12.82). Define $f_n(x)=$ index of $x$ in $A$ if $x\in A$, else $0$ (12.83); $\phi_n$ maps indices back to elements of $A$. Everything in $A$ is decoded correctly; everything else is an error (pp. 289–290).

For source $Q$ with $H(Q)<R$:
$$P_e^{(n)}=1-Q^n(A)=\sum_{P:H(P)>R_n}Q^n(T(P))\le(n+1)^{|\mathcal X|}\max_{P:H(P)>R_n}Q^n(T(P))\le(n+1)^{|\mathcal X|}2^{-n\min_{P:H(P)>R_n}D(P\|Q)}$$
(12.84–12.87). Since $R_n\uparrow R$ and $H(Q)<R$, there is $n_0$ with $R_n>H(Q)$ for $n\ge n_0$. Then the minimum is $>0$ and $P_e^{(n)}\to0$ exponentially fast. If $H(Q)>R$, the type is with high probability outside $A$, so error is close to 1 (p. 290).

Error exponent: $D^*_{R,Q}=\min_{P:H(P)>R}D(P\|Q)$ (12.88) (Figures 12.1–12.2) (p. 291).

**Remarks** (p. 291). This scheme is universal over i.i.d. sources. The Lempel–Ziv algorithm is a variable-rate universal code for all ergodic sources (discussed in 12.10, not in this unit). Universal codes need longer block length for the same performance as a code tuned to the distribution, and cost more encoder/decoder complexity. So a distribution-specific code is best when the distribution is known.

> *Intuition note.* The code simply gives a short label to every sequence whose type is "not too random". Such sequences number at most $2^{nR}$. For any source with $H(Q)<R$, the probability that the sequence lies in the indexed set tends to 1.

### 12.4 Large deviation theory
**Motivating example** (pp. 291–292). For i.i.d. Bernoulli(1/3), the event $\frac1n\sum X_i\approx1/3$ is a small deviation with probability near 1. The event $\frac1n\sum X_i>3/4$ is a large deviation with exponentially small probability. The central limit theorem is a poor estimate of that exponent beyond a few standard deviations. The event $\bar X_n=3/4$ means $P_x=(1/4,3/4)$, and its probability is about $2^{-nD((\frac14,\frac34)\|(\frac23,\frac13))}$.

For a set $E$ of pmfs: $Q^n(E)=Q^n(E\cap\mathcal P_n)=\sum_{x:P_x\in E\cap\mathcal P_n}Q^n(x)$ (12.89). If $E$ contains a relative-entropy neighbourhood of $Q$, then $Q^n(E)\to1$. If $E$ contains neither $Q$ nor a neighbourhood, then $Q^n(E)\to0$ exponentially fast (p. 292).

Example of a set: "sample mean of $g(X)\ge\alpha$" is $P_x\in E\cap\mathcal P_n$ with $E=\{P:\sum_ag(a)P(a)\ge\alpha\}$ (12.90–12.93). This $E$ is a half space in the probability simplex (Figure 12.3) (p. 292).

**Theorem 12.4.1 (Sanov).** For $X_i$ i.i.d. $\sim Q$ and $E\subseteq\mathcal P$:
$$Q^n(E)=Q^n(E\cap\mathcal P_n)\le(n+1)^{|\mathcal X|}2^{-nD(P^*\|Q)}\tag{12.94}$$
with $P^*=\arg\min_{P\in E}D(P\|Q)$ (12.95). If $E$ is also the closure of its interior, then $\frac1n\log Q^n(E)\to-D(P^*\|Q)$ (12.96) (p. 292–293).

*Proof, upper bound* (p. 293):
$$Q^n(E)=\sum_{P\in E\cap\mathcal P_n}Q^n(T(P))\le\sum2^{-nD(P\|Q)}\le\sum\max_{P\in E\cap\mathcal P_n}2^{-nD(P\|Q)}=\sum2^{-n\min_{P\in E\cap\mathcal P_n}D(P\|Q)}\le\sum2^{-n\min_{P\in E}D(P\|Q)}=\sum_{P\in E\cap\mathcal P_n}2^{-nD(P^*\|Q)}\le(n+1)^{|\mathcal X|}2^{-nD(P^*\|Q)}$$
(12.97–12.103), the last step by Theorem 12.1.1. $P^*$ need not be in $\mathcal P_n$.

*Lower bound* (pp. 293–294). Assume $E$ is the closure of its interior, so the interior is non-empty. Since $\bigcup_n\mathcal P_n$ is dense in all distributions, $E\cap\mathcal P_n\ne\emptyset$ for $n\ge n_0$. Pick $P_n\in E\cap\mathcal P_n$ with $D(P_n\|Q)\to D(P^*\|Q)$. Then
$$Q^n(E)=\sum_{P\in E\cap\mathcal P_n}Q^n(T(P))\ge Q^n(T(P_n))\ge\frac1{(n+1)^{|\mathcal X|}}2^{-nD(P_n\|Q)}$$
(12.104–12.106). So $\liminf\frac1n\log Q^n(E)\ge\liminf\big(-|\mathcal X|\frac{\log(n+1)}n-D(P_n\|Q)\big)=-D(P^*\|Q)$ (12.107). With the upper bound this proves the theorem. The argument extends to continuous distributions by quantization (p. 294).

> *Intuition note.* The probability of a rare set $E$ is governed by the member of $E$ closest to $Q$ in relative entropy: the exponent is $D(P^*\|Q)$ (exact for well-behaved $E$). That the type is then close to $P^*$ is only announced at the end of this part (p. 296).

### 12.5 Examples of Sanov's theorem
**General constraints** (p. 294–295). For $\Pr\{\frac1n\sum_ig_j(X_i)\ge\alpha_j,\ j=1..k\}$, $E=\{P:\sum_aP(a)g_j(a)\ge\alpha_j\}$ (12.108). Minimise $D(P\|Q)$ with
$$J(P)=\sum_xP(x)\log\frac{P(x)}{Q(x)}+\sum_i\lambda_i\sum_xP(x)g_i(x)+\nu\sum_xP(x)\tag{12.109}$$
Differentiating gives the closest distribution
$$P^*(x)=\frac{Q(x)e^{\sum_i\lambda_ig_i(x)}}{\sum_{a}Q(a)e^{\sum_i\lambda_ig_i(a)}}\tag{12.110}$$
with $\lambda_i$ chosen to meet the constraints. If $Q$ is uniform, $P^*$ is the maximum-entropy distribution. That $P^*$ is the minimum follows from arguments like those in Chapter 11 (p. 295).

**Example 12.5.1 (Dice)** (p. 295). Probability that the average of $n$ fair-die throws is $\ge4$: $Q^n(E)\doteq2^{-nD(P^*\|Q)}$ (12.111), where $P^*$ minimises $D(P\|Q)$ subject to $\sum_{i=1}^6iP(i)\ge4$ (12.112). By (12.110), $P^*(x)=\frac{2^{\lambda x}}{\sum_{i=1}^62^{\lambda i}}$ (12.113), with $\lambda$ set so that $\sum iP^*(i)=4$. Numerically $\lambda=0.2519$, $P^*=(0.1031,0.1227,0.1461,0.1740,0.2072,0.2468)$, $D(P^*\|Q)=0.0624$ bits. So for 10000 throws the probability is $\approx2^{-624}$.

**Example 12.5.2 (Coins)** (p. 295). More than 700 heads in 1000 tosses of a fair coin: $P(\bar X_n\ge0.7)\doteq2^{-nD(P^*\|Q)}$ (12.114), with $P^*=(0.7,0.3)$, $Q=(0.5,0.5)$. $D(P^*\|Q)=1-H(0.7)=0.119$, so the probability is about $2^{-119}$.

**Example 12.5.3 (Mutual dependence)** (pp. 295–296). Let $Q(x,y)$ be a joint distribution and $Q_0(x,y)=Q(x)Q(y)$ its marginal product. How likely is an i.i.d. $Q_0$ sample to look jointly distributed as $Q$? Joint typicality (as in Section 8.6) requires (bars read as absolute values; see Reading notes)
$$\Big|-\tfrac1n\log Q(x^n)-H(X)\Big|\le\epsilon,\quad\Big|-\tfrac1n\log Q(y^n)-H(Y)\Big|\le\epsilon,\quad\Big|-\tfrac1n\log Q(x^n,y^n)-H(X,Y)\Big|\le\epsilon\tag{12.115–12.117}$$
This is the event $P_{x^n,y^n}\in E\cap\mathcal P_n(\mathcal X,\mathcal Y)$ with $E=\{P:|-\sum P(x,y)\log Q(x)-H(X)|\le\epsilon,\ |-\sum P(x,y)\log Q(y)-H(Y)|\le\epsilon,\ |-\sum P(x,y)\log Q(x,y)-H(X,Y)|\le\epsilon\}$ (12.118). By Sanov, $Q_0^n(E)\doteq2^{-nD(P^*\|Q_0)}$ (12.119). As $\epsilon\to0$, $P^*=Q$ (verified in Problem 10, not shown here). So the probability is $2^{-nD(Q(x,y)\|Q(x)Q(y))}=2^{-nI(X;Y)}$, as in the joint AEP of Chapter 8 (p. 296).

The author previews the next section: given that the type lies in $E$, the conditional type is very likely close to $P^*$ (p. 296).

## Toy example (ours)
Binary alphabet, $n=4$, $Q(1)=1/4$, $Q(0)=3/4$. Take sequence $x=0110$. Then $P_x=(1/2,1/2)$ (listed as $(P(0),P(1))$).
- $H(P_x)=1$ bit.
- $D(P_x\|Q)=\tfrac12\log_2\frac{1/2}{3/4}+\tfrac12\log_2\frac{1/2}{1/4}=\tfrac12(-0.58496)+\tfrac12(1)=0.20752$ bits.
- Theorem 12.1.2: $Q^4(x)=2^{-4(1+0.20752)}=2^{-4.83008}\approx0.03516$. Direct: $(3/4)^2(1/4)^2=9/256=0.03516$. ✓.
- Type class size: $\binom42=6$. Bounds (12.16): $\frac{2^{4}}{(4+1)^2}=0.64\le6\le2^4=16$ ✓.
- $Q^4(T(P))=6\cdot9/256=0.2109$. Bounds (12.54): $2^{-nD}=2^{-0.83008}=9/16=0.5625$ (since $Q^4(x)\cdot2^{nH}=\tfrac9{256}\cdot16$). Lower $0.5625/25=0.0225\le0.2109\le0.5625$ ✓.

The bounds are loose at $n=4$. Only the exponent $2^{-nD}$ matters as $n$ grows.

## Concepts
- [[method-of-types]] (new) — group sequences by empirical distribution; polynomially many types, exponential class sizes (p. 279).
- [[type-class]] (new) — $T(P)$: all length-$n$ sequences with empirical distribution $P$ (p. 280).
- [[typical-set-aep]] — here, $\{x:D(P_x\|Q)\le\epsilon\}$ and the strongly typical set with component-wise closeness $\epsilon/|\mathcal X|$ (pp. 287–288).
- [[relative-entropy-kl]] — controls type-class probability $2^{-nD(P\|Q)}$ and the cost of a mismatched Huffman code (pp. 285, 288).
- [[universal-coding]] — one fixed-rate block code, independent of $Q$, with vanishing error whenever $R>H(Q)$ (p. 289).
- [[sanov-theorem]] (new) — $Q^n(E)\doteq2^{-nD(P^*\|Q)}$, with $P^*$ the $D$-closest point of $E$ to $Q$ (p. 292).
- [[large-deviation-theory]] (new) — exponential decay rates of rare events such as $\bar X_n>3/4$ (p. 291).
- [[exponential-family-gibbs]] — the tilted form (12.110) of $P^*$ under expectation constraints (p. 294).
- [[maximum-entropy-principle]] — $P^*$ is max-entropy when $Q$ is uniform (p. 295).
- [[mutual-information]] — appears as the exponent $2^{-nI(X;Y)}$ in Example 12.5.3 (p. 296).

## Canonical instances
- [[die-average-example]] (new) — fair die, average $\ge4$: $D(P^*\|Q)=0.0624$ bits, probability $\approx2^{-624}$ for $n=10000$ (p. 295).
- [[coin-700-heads-example]] (new) — 700 or more heads in 1000 tosses: exponent $1-H(0.7)=0.119$ (p. 295).
- [[joint-typicality-sanov-example]] (new) — product-distribution sample looks jointly typical with probability $2^{-nI(X;Y)}$ (p. 296).
- [[binary-type-class-bounds]] (new) — $\binom nk\doteq2^{nH(k/n)}$ (p. 284).

## Bridges (candidates)
- [same-math] Sanov's $P^*\propto Q\,e^{\sum\lambda_ig_i}$ ↔ maximum entropy / exponential families: the same tilted form as MaxEnt solutions under expectation constraints.
- [structural-analogy] Polynomially many types vs. exponentially many sequences ↔ MDL / universal coding: model cost is only $O(\log n)$ bits per parameter.
- [structural-analogy] Rare-event exponent $D(P^*\|Q)$ ↔ cross-entropy / likelihood-ratio testing: the cost of a wrong model is measured in $D$.

## Questions this raises
- How does the conditional type given $E$ concentrate around $P^*$ (the next section's claim, p. 296)?
- What is the best error exponent for deciding between two distributions (Stein's lemma, announced on p. 279)?
- How much does the universal code lose in block length compared with a code tuned to $Q$, quantitatively (p. 291)?
- For non-"nice" sets $E$ (not the closure of their interior), does the exponent still equal $D(P^*\|Q)$ (p. 293)?

## Reading notes
- This unit starts at the chapter opening (printed p. 279) and ends at the end of 12.5 (p. 296, after Example 12.5.3). Sections 12.6 onward are not included.
- Page offset: printed = pdf − 22.
- The PDF is the 1991 first edition (copyright line on p. 279), not the 2006 second edition cited in the metadata. The unit metadata warns that chapter numbering and content differ from the second edition; I have not verified this from these pages.
- OCR text is badly garbled in many equations. I checked them against the page images. The bars (absolute values) in (12.115)–(12.118) are hard to see; I read them as absolute values, matching the standard joint-typicality definition. The die pmf in Example 12.1.2 is small in print; I read it as $(1/3,1/3,1/6,1/12,1/12,0)$, which sums to 1.
- The source cites Problem 10 (12.5.3) and Lempel–Ziv in 12.10, neither in these pages. The unit contains no exercises of its own.
- The author writes $\doteq$ (e.g. (12.53), (12.62), (12.111)) and describes such statements as holding "to first order in the exponent" (pp. 281, 285); no separate formal definition of $\doteq$ appears on these pages. I use it in that sense.
