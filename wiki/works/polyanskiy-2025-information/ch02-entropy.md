---
id: polyanskiy-2025-information/ch02-entropy
work: polyanskiy-2025-information
unit: "Chapter 1 (file id ch02-entropy): Entropy"
pages: 8-19
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Entropy

## L0 — One line
Shannon entropy $H(X)=\mathbb E[\log 1/P_X(X)]$ measures the randomness of a discrete variable, obeys a chain rule and "conditioning reduces entropy", and has axiomatic, physical and combinatorial justifications.

## L1 — The gist (≤ 120 words)
The chapter defines entropy, joint entropy and conditional entropy, and proves their basic properties: non-negativity, the uniform maximum, the chain rule, and conditioning reducing entropy. It then asks why this is the right formula. Answers: an axiomatic characterization, the thermodynamic history (Clausius, Boltzmann, Gibbs), and the method of types, which says a multinomial coefficient (a count of arrangements) is within a polynomial factor of $e^{nH}$. It ends with submodularity of entropy (adding a variable helps less when more is already known) and its consequences, Han's inequality and Shearer's lemma. These give inequalities about subsets of variables and even a geometric projection bound.

**Prerequisites:** expectation of a function of a random variable; logarithms; Jensen's inequality (reviewed on p. 11); conditional probability; multinomial coefficients.

## L2 — Key ideas
- Entropy is the expected value of $\log(1/P_X(X))$ (we call this the "surprisal" of the outcome; the book does not). Its unit depends on the log base: bits, nats, bytes (p. 8).
- Entropy is non-negative, at most $\log|\mathcal X|$ (equality iff uniform), unchanged by relabeling, and not increased by conditioning (p. 11).
- Chain rule: $H(X^n)=\sum_i H(X_i|X^{i-1})\le\sum_i H(X_i)$, with equality iff the variables are independent (p. 12).
- Operational preview: in 20 Questions the best average number of yes/no questions lies between $H(X)$ and $H(X)+1$ bits (p. 13).
- Shannon's six axioms single out $\sum p_i\log(1/p_i)$ as the only possibility. The author says one can check that Rényi entropies (other measures of randomness) satisfy the six axioms except subadditivity (p. 13–14).
- Method of types: $(n+1)^{-(k-1)}e^{nH(P)}\le\binom{n}{n_1,\dots,n_k}\le e^{nH(P)}$. This links counting microstates to entropy (p. 15).
- Entropy is submodular (adding an element helps less to a larger set) and monotone. Yet a non-Shannon inequality (one not implied by submodularity) shows that, for $n\ge 4$, the set of entropy functions is strictly smaller than the cone $\Gamma_n$ of non-negative, monotone, submodular functions (p. 16–17).
- Han's inequality and Shearer's lemma are proved via submodularity, and Han's inequality is the special case of Shearer's lemma with $S$ uniform over $k$-subsets. Shearer's lemma with $n=3$, $k=2$ yields $N_1N_2N_3\ge N^2$ for projections of $N$ points in $\mathbb R^3$ (p. 17–18).

## L3 — Walkthrough

### 1.1 Entropy and conditional entropy
**Definition 1.1.** For discrete $X$ with PMF $P_X$ on $\mathcal X$ (p. 8):
$$H(X)=\mathbb E\Big[\log\tfrac{1}{P_X(X)}\Big]=\sum_{x\in\mathcal X}P_X(x)\log\tfrac{1}{P_X(x)},\qquad 0\log\tfrac10=0\tag{1.1}$$
Entropy depends only on the distribution, so $H(P_X)$ is also written. Base 2 gives bits, base $e$ nats, base 256 bytes. "Baseless" $\log$/$\exp$ means the base matches that of $\exp$ (p. 8).

**Definition 1.2 (joint entropy).** $H(X^n)=\mathbb E\big[\log \frac{1}{P_{X_1\dots X_n}(X_1,\dots,X_n)}\big]$. It is Definition 1.1 applied to the vector $X^n$ (p. 9).

**Remark 1.1.** The name comes from thermodynamics (Section 1.3). Other justifications are axioms (Section 1.2) and experiments. In ant scouts, the time to describe food at a leaf of a full binary tree of depth $d$ was proportional to the entropy of the food location (p. 9).

Uniform $X$ on finite $\mathcal X$ gives $H(X)=\log|\mathcal X|$. More spread-out PMFs have higher entropy (p. 9).

**Examples.**
- **1.1 Bernoulli.** $H(X)=h(p)=p\log\frac1p+\bar p\log\frac1{\bar p}$. The function $h$ is continuous, concave, symmetric around $\frac12$, with $h'(p)=\log\frac{\bar p}{p}$ (infinite slope at 0 and 1). The maximum is at $p=\frac12$, the minimum at $p\in\{0,1\}$ (p. 9).
- **1.2 Geometric.** $P_X(i)=p\bar p^{\,i}$, $i=0,1,\dots$, $\mathbb E[X]=\bar p/p$. Then $H(X)=\log\frac1p+\mathbb E[X]\log\frac1{\bar p}=h(p)/p$ (p. 10).
- **1.3 Infinite entropy.** $H(X)=+\infty$ is possible, e.g. $\mathbb P[X=k]\propto\frac{1}{k\ln^2k}$, $k=2,3,\dots$ (p. 10).

**Definition 1.3 (conditional entropy).** For discrete $X$ and arbitrary $Y$:
$$H(X|Y)=\mathbb E_{y\sim P_Y}[H(P_{X|Y=y})]=\mathbb E\Big[\log\tfrac{1}{P_{X|Y}(X|Y)}\Big].$$
For discrete $Y$ it equals $\sum_{x,y}P_{X,Y}(x,y)\log\frac1{P_{X|Y}(x|y)}$. It is the randomness left in $X$ once $Y$ is revealed. It equals $H(X)$ if $Y$ is independent of $X$ (p. 10).

**Example 1.4 (noisy channel).** $X\sim\mathrm{Ber}(\frac12)$.
1. $Y=X\oplus Z$ (XOR), $Z\sim\mathrm{Ber}(\delta)$ independent of $X$. Then $P_{X|Y=0}=\mathrm{Ber}(\delta)$, $P_{X|Y=1}=\mathrm{Ber}(\bar\delta)$, and $h(\delta)=h(\bar\delta)$, so $H(X|Y)=h(\delta)$. At $\delta=\frac12$, $H(X|Y)=H(X)=1$ bit. At $\delta\in\{0,1\}$, $H(X|Y)=0$ (p. 10).
2. $Y=X+Z$, $Z\sim\mathcal N(0,\sigma^2)$. Then $H(X|Y)=\mathbb E[h(\mathbb P[X=1|Y])]$ with $\mathbb P[X=1|Y=y]=\frac{\varphi(\frac{y-1}{\sigma})}{\varphi(\frac y\sigma)+\varphi(\frac{y-1}{\sigma})}$. The author says it "can be shown" to increase monotonically from 0 to 1 bit in $\sigma^2$ (hint: Theorem 1.4(d); Fig. 1.1) (p. 10–11).

**Convexity review (p. 11).** A function is convex if $f(\alpha x+\bar\alpha y)\le\alpha f(x)+\bar\alpha f(y)$, strictly convex if "$<$" for $x\ne y$, $\alpha\in(0,1)$. Jensen: $f$ convex $\Rightarrow f(\mathbb EX)\le\mathbb Ef(X)$. If $f$ is strictly convex, the inequality is strict unless $X$ is a.s. constant.

**Theorem 1.4 (properties).**
- (a) $H(X)\ge0$, equality iff $X$ is constant.
- (b) For finite $\mathcal X$, $H(X)\le\log|\mathcal X|$, equality iff $X$ is uniform.
- (c) $H(X)=H(f(X))$ for bijective $f$.
- (d) $H(X|Y)\le H(X)$, equality iff $X,Y$ independent (p. 11).
- (e) Simple chain rule: $H(X,Y)=H(X)+H(Y|X)\le H(X)+H(Y)$ (1.2).
- (f) $H(X)=H(X,f(X))\ge H(f(X))$, equality iff $f$ is one-to-one on the support of $P_X$.
- (g) Full chain rule (p. 12):
$$H(X_1,\dots,X_n)=\sum_{i=1}^nH(X_i|X^{i-1})\le\sum_{i=1}^nH(X_i)\tag{1.3}$$
Equality holds iff $X_1,\dots,X_n$ are mutually independent.

*Proof steps (p. 12).*
- (a) $\log\frac1{P_X(X)}$ is a non-negative random variable, so its mean is. The mean is 0 iff it is 0 a.s., i.e. $P_X$ is a point mass.
- (b) Jensen for strictly concave $\log$: $H(X)=\mathbb E\log\frac1{P_X(X)}\le\log\mathbb E\frac1{P_X(X)}=\log|\mathcal X|$.
- (c) The sum depends on the values of $P_X$, not their locations.
- (d) Write $P(x)=\mathbb E_Y[P(x|Y)]$. Jensen for strictly concave $x\mapsto x\log\frac1x$ gives $H(X|Y)=\sum_x\mathbb E_Y[P(x|Y)\log\frac1{P(x|Y)}]\le\sum_xP(x)\log\frac1{P(x)}=H(X)$.
- (e) $\mathbb E\log\frac1{P_{X,Y}}=\mathbb E\log\frac{1}{P_X(X)P_{Y|X}(Y|X)}=H(X)+H(Y|X)$. Then (d) gives the inequality.
- (f) $x\mapsto(x,f(x))$ is one-to-one, so by (c) and (e) $H(X)=H(f(X))+H(X|f(X))\ge H(f(X))$. Equality iff $X$ is constant given $f(X)$.
- (g) Telescope $P_{X^n}=P_{X_1}P_{X_2|X_1}\cdots P_{X_n|X^{n-1}}$ and take logs. The inequality is (d), with equality iff $P_{X_i|X^{i-1}}=P_{X_i}$ for all $i$.

*Intuition note.* Entropy adds up step by step: first the uncertainty of $X_1$, then what is new in $X_2$ given $X_1$, and so on. On average, extra knowledge cannot increase what remains uncertain, so the pieces never sum to more than the separate entropies.

**20 Questions preview (p. 13).** Take $P[a]=\frac12$, $P[b]=\frac14$, $P[c]=P[d]=\frac18$. Ask "$X=a$?", then "$X=b$?", then "$X=c$?". The average number of questions is $\frac12+\frac14\cdot2+\frac18\cdot3+\frac18\cdot3=1.75=H(X)$ bits. Asking "$\{a,b\}$ or $\{c,d\}$?" first always needs two questions, which is worse. The minimum average is between $H(X)$ and $H(X)+1$ bits (proved in Section 10.3, not here) (p. 13).

### 1.2 Axiomatic characterization
Shannon (1948) showed that a functional $H_m(p_1,\dots,p_m)$ satisfying the following axioms must be $\sum p_i\log\frac1{p_i}$ (p. 13):
- (a) permutation invariance;
- (b) expansibility: $H_m(p_1,\dots,p_{m-1},0)=H_{m-1}(p_1,\dots,p_{m-1})$;
- (c) normalization: $H_2(\frac12,\frac12)=\log2$;
- (d) subadditivity: $H(X,Y)\le H(X)+H(Y)$;
- (e) additivity: $H(X,Y)=H(X)+H(Y)$ if $X\perp\!\!\!\perp Y$;
- (f) continuity: $H_2(p,1-p)\to0$ as $p\to0$.

**Rényi entropy** (p. 13–14):
$$H_\alpha(P)=\tfrac1{1-\alpha}\log\sum_ip_i^\alpha\ \ (\alpha\in(0,1)\cup(1,\infty)),\qquad H_\infty(P)=\min_i\log\tfrac1{p_i}\tag{1.4}$$
$H_\infty$ is the min-entropy of cryptography. The author says "one can check" three facts. First, $0\le H_\alpha\le\log m$, with the bounds attained at a point mass and at the uniform law. Second, $H_\alpha$ is non-increasing in $\alpha$ and tends to $H(P)$ as $\alpha\to1$. Third, it satisfies the six axioms except subadditivity (p. 14).

### 1.3 History of entropy
Perpetual-motion attempts led to the first law (energy conservation). Machines that turn heat from a warm body fully into work also failed. This led Clausius and Kelvin to the second law: no cyclic machine produces useful work while only drawing heat from a warm body. An equivalent form: no cyclic process moves heat from cold to warm without external work (p. 14).

Clausius introduced a hidden state quantity, entropy. Under reversible (very slow) processes
$$\Delta S=\Delta Q/T\tag{1.5}$$
If heat $Q$ is absorbed at $T_{\rm hot}$, some heat $Q'$ must be returned to get back to the original state; $Q'$ can be much smaller than $Q$ but is never zero if it is returned at $0<T_{\rm cold}<T_{\rm hot}$. The author adds that further logical arguments can convince one that for irreversible cyclic processes the entropy change at the end of the cycle can only be positive, so entropy cannot reduce (p. 15).

Entropy had no formula until Boltzmann and Gibbs. For $n$ independent particles, each in one of $\ell$ states with fractions $p_j$ (p. 15):
$$S=kn\sum_{j=1}^\ell p_j\log\tfrac1{p_j}\tag{1.6}$$
Here $k$ is Boltzmann's constant. Their innovation was twofold: separate micro-state (one state per particle) from macro-state (the proportions $\{p_j\}$), and postulate that the multiplicity of a macro-state is the exponential of its entropy. The link is the next result.

**Proposition 1.5 (method of types).** Let $\sum n_i=n$ and $p_i=n_i/n$. Then (p. 15)
$$\frac1{(1+n)^{k-1}}e^{nH(P)}\le\binom{n}{n_1,\dots,n_k}\le e^{nH(P)}$$
*Proof (p. 15–16).* Let $X_1,\dots,X_n$ be i.i.d. $\sim P$ and $N_i$ the count of symbol $i$. Then $(N_1,\dots,N_k)$ is multinomial: $\mathbb P[N=n']=\binom{n}{n'_1,\dots,n'_k}\prod p_i^{n'_i}$.
- Upper bound: $\mathbb P[N=(n_1,\dots,n_k)]\le1$. With $p_i=n_i/n$, $\prod p_i^{n_i}=e^{-nH(P)}$ (added step).
- Lower bound: $N$ takes at most $(n+1)^{k-1}$ values, so it suffices to show $(n_1,\dots,n_k)$ is the mode. With $\Delta_i=n'_i-n_i$:
$$\frac{\mathbb P[N=n']}{\mathbb P[N=n]}=\prod_i\frac{n_i!}{(n_i+\Delta_i)!}p_i^{\Delta_i}\le\prod_in_i^{-\Delta_i}p_i^{\Delta_i}=1$$
The inequality uses $\frac{m!}{(m+\Delta)!}\le m^{-\Delta}$. The last equality uses $\sum\Delta_i=0$.

*Intuition note.* The number of sequences with given letter proportions $P$ is about $e^{nH(P)}$, up to a polynomial factor. So entropy is the exponential growth rate of the count of micro-states matching a macro-state.

Sharper estimates (Ex. I.2): for $p=k/n\in(0,1)$ (p. 16)
$$e^{-1/6}\le\binom nk\Big/\Big(\tfrac1{\sqrt{2\pi np(1-p)}}e^{nh(p)}\Big)\le1\tag{1.7}$$

### 1.4* Submodularity
A set function $f:2^S\to\mathbb R$ is submodular if for all $T_1,T_2\subset S$
$$f(T_1\cup T_2)+f(T_1\cap T_2)\le f(T_1)+f(T_2)\tag{1.8}$$
The author likens this to concavity, in the sense that "adding elements gives diminishing returns"; indeed, for $T'\subset T$, $b\notin T$, $f(T\cup b)-f(T)\le f(T'\cup b)-f(T')$ (p. 16).

**Theorem 1.6.** $T\mapsto H(X_T)$ is submodular.
*Proof (p. 16).* With $A=X_{T_1\setminus T_2}$, $B=X_{T_1\cap T_2}$, $C=X_{T_2\setminus T_1}$, show $H(A,B,C)+H(B)\le H(A,B)+H(B,C)$:
$$H(A,B,C)+H(B)=H(A,C|B)+2H(B)\tag{1.9}$$
$$\le H(A|B)+H(C|B)+2H(B)\tag{1.10}$$
$$=H(A,B)+H(B,C)\tag{1.11}$$
*Intuition note.* Adding a variable tells you less new when you already know more (diminishing returns, p. 16). Step (1.10) uses that, given $B$, the joint entropy of $A$ and $C$ is at most the sum of their separate conditional entropies.

Entropy is also monotone: $T_1\subset T_2\Rightarrow H(X_{T_1})\le H(X_{T_2})$. Let $\Gamma_n$ be the non-negative, monotone, submodular set functions on $[n]$, a closed convex cone. Let $\Gamma^*_n$ be the set functions arising from distributions on $X^n$, and $\bar\Gamma^*_n$ its closure, also a closed convex cone. Then $\Gamma^*_n\subset\bar\Gamma^*_n\subset\Gamma_n$ (p. 17). The result of [473] is
$$\Gamma^*_2=\bar\Gamma^*_2=\Gamma_2,\quad\Gamma^*_3\subsetneq\bar\Gamma^*_3=\Gamma_3,\quad\Gamma^*_n\subsetneq\bar\Gamma^*_n\subsetneq\Gamma_n\ (n\ge4)\tag{1.12–1.14}$$
This follows from a non-Shannon inequality, valid for any four discrete variables:
$$I(X_3;X_4)-I(X_3;X_4|X_1)-I(X_3;X_4|X_2)\le\tfrac12I(X_1;X_2)+\tfrac14I(X_1;X_3,X_4)+\tfrac14I(X_2;X_3,X_4)$$
So even linear constraints on the entropy set-function go beyond generic submodularity (p. 17).

### 1.5* Han's inequality and Shearer's lemma
**Theorem 1.7 (Han).** Let $\bar H_k=\binom nk^{-1}\sum_{T\in\binom{[n]}{k}}H(X_T)$. Then (p. 17)
$$\tfrac1n\bar H_n\le\dots\le\tfrac1k\bar H_k\le\dots\le\bar H_1\tag{1.15}$$
$$\bar H_{k+1}-\bar H_k\le\bar H_k-\bar H_{k-1}\tag{1.16}$$
The sequence $\bar H_k$ is also increasing, with decreasing slope (concave) as in (1.16).
*Proof (p. 17–18).* Set $\bar H_0=0$. Then $\frac1m\bar H_m=\frac1m\sum_{k=1}^m(\bar H_k-\bar H_{k-1})$ is an average of differences. By (1.16) the differences shrink, so adding one more adds a smaller element and (1.16) implies (1.15). For (1.16), submodularity gives $H(X_1..X_{k+1})+H(X_1..X_{k-1})\le H(X_1..X_k)+H(X_1..X_{k-1},X_{k+1})$. Averaging over all $n!$ permutations yields $\bar H_{k+1}+\bar H_{k-1}\le2\bar H_k$. Alternative: average $H(X_{k+1}|X_1..X_k)\le H(X_{k+1}|X_2..X_k)$ over permutations.

**Theorem 1.8 (Shearer).** Let $S\subset[n]$ be random, independent of $X^n$. Then
$$H(X_S|S)\ge H(X^n)\cdot\min_{i\in[n]}\mathbb P[i\in S]\tag{1.17}$$
**Remark 1.2.** For $S$ uniform over $k$-subsets, this is $\frac1nH(X^n)\le\frac1k\bar H_k$. The case $n=3$, $k=2$ gives an entropy proof of: for $N$ points in $\mathbb R^3$ with $N_1,N_2,N_3$ distinct projections onto the $xy$, $xz$, $yz$ planes, $N_1N_2N_3\ge N^2$ (p. 18).

*Proof (p. 18–19).* It suffices to prove, for a list $\mathcal C=(S_1,\dots,S_M)$ of subsets of $[n]$ (repeats allowed), with $\deg(i)=\#\{j:i\in S_j\}$:
$$\sum_jH(X_{S_j})\ge H(X^n)\min_i\deg(i)\tag{1.18}$$
- **Chain case** ($S_1\subseteq\dots\subseteq S_M$): the minimum is 0 if $S_M\ne[n]$, otherwise the multiplicity of $S_M$. Then $\sum_jH(X_{S_j})\ge H(X_{S_M})\#\{j:S_j=S_M\}=H(X^n)\min_i\deg(i)$.
- **Non-chain case:** replace two sets $S_1,S_2$ unrelated by inclusion with $S_1\cap S_2$, $S_1\cup S_2$. By (1.8) the sum does not increase, and the degrees are unchanged. The number of unrelated pairs strictly decreases, so the process ends in a chain.

**Remark 1.3.** (1.16) holds for any submodular set function. (1.15) also needs $f(\emptyset)=0$. Shearer's lemma holds for any submodular function that is also non-negative (p. 19).

**Example 1.5.** $S\mapsto I(X_S;X_{S^c})$ is submodular. Han's inequality reads $0=\frac1nI_n\le\dots\le\frac1kI_k\le\dots\le I_1$, where $I_k=\binom nk^{-1}\sum_{|S|=k}I(X_S;X_{S^c})$ measures $k$-subset coupling (p. 19).

## Toy example (ours)
Let $(X,Y)\in\{0,1\}^2$ with $P(0,0)=\frac14$, $P(0,1)=\frac14$, $P(1,0)=\frac12$, $P(1,1)=0$ (using $0\log\frac10=0$). All logs base 2.
- $P_X=(\frac12,\frac12)$, so $H(X)=1$. $P_Y=(\frac34,\frac14)$, so $H(Y)=\frac34\log\frac43+\frac14\cdot2=0.3113+0.5=0.8113$.
- Joint: $H(X,Y)=\frac14\cdot2+\frac14\cdot2+\frac12\cdot1=1.5$.
- Chain rule: $H(Y|X)=1.5-1=0.5$. Check directly: $X=0$ (prob $\frac12$) gives $Y$ uniform, 1 bit. $X=1$ gives $Y=0$ surely, 0 bits. Average $0.5$ ✓.
- $H(X|Y)=1.5-0.8113=0.6887$. Check: $Y=0$ (prob $\frac34$) gives $P(X=0|Y=0)=\frac13$, so $h(\frac13)=\log3-\frac23=0.9183$. $Y=1$ gives $X=0$ surely, 0 bits. $\frac34\cdot0.9183=0.6887$ ✓.
- Conditioning reduces entropy: $0.6887\le1$ and $0.5\le0.8113$. Subadditivity: $1.5\le1+0.8113=1.8113$, strict because $X,Y$ are dependent.

## Concepts
- [[entropy]] — $\mathbb E[\log 1/P_X(X)]$, units set by the log base (p. 8)
- [[bit]] — entropy unit with $\log_2$; nats use $\log_e$, bytes $\log_{256}$ (p. 8)
- [[self-information-surprisal]] (new; our label, not used in the pages) — the random variable $\log 1/P_X(X)$ whose mean is $H(X)$ (p. 8)
- [[joint-and-conditional-entropy]] — $H(X^n)$ and $H(X|Y)=\mathbb E_y[H(P_{X|Y=y})]$ (p. 9–10)
- [[chain-rule]] — $H(X^n)=\sum H(X_i|X^{i-1})\le\sum H(X_i)$ (p. 12)
- [[binary-entropy-function]] (new) — $h(p)$, the entropy of Ber($p$) (p. 9)
- [[jensen-inequality]] (new) — $f(\mathbb EX)\le\mathbb Ef(X)$ for convex $f$; used for properties (b), (d) (p. 11)
- [[renyi-entropy]] (new) — $H_\alpha$, with min-entropy at $\alpha=\infty$ (p. 13)
- [[method-of-types]] (new) — multinomial coefficient $\approx e^{nH(P)}$ up to a polynomial factor (p. 15)
- [[submodularity]] (new) — $f(T_1\cup T_2)+f(T_1\cap T_2)\le f(T_1)+f(T_2)$; entropy has it (p. 16)
- [[han-shearer-inequalities]] (new) — averaged subset entropies per coordinate decrease with subset size; Shearer's lemma generalizes this (p. 17–18)
- [[mutual-information]] — within these pages appears only in the non-Shannon inequality and Example 1.5, with its definition deferred (p. 17, 19)

## Canonical instances
- [[bernoulli-entropy]] — $h(p)$ is maximal at $\frac12$, zero at 0 and 1 (p. 9)
- [[noisy-channel-conditional-entropy]] — $H(X|Y)=h(\delta)$ for XOR noise (p. 10)
- [[twenty-questions]] — a 1.75-question average equals $H(X)$ for the example $(\frac12,\frac14,\frac18,\frac18)$ (p. 13)
- [[ant-scout-experiment]] — communication time proportional to entropy of the food location (p. 9)
- [[ideal-gas-entropy]] — $S=kn\sum p_j\log(1/p_j)$ (p. 15)
- [[projection-inequality]] — $N_1N_2N_3\ge N^2$ from Shearer's lemma (p. 18)

## Bridges (candidates)
- [same-math] Boltzmann–Gibbs entropy $S=kn\sum p_j\log\frac1{p_j}$ ↔ statistical physics: the same sum as $nH(P)$, times $k$ (p. 15)
- [same-math] Min-entropy $H_\infty$ ↔ cryptography: the book names the same quantity (p. 14)
- [structural-analogy] Submodularity as diminishing returns ↔ concavity: the book itself compares the two (p. 16)

## Questions this raises
- Does $H(P_{X|Y=y})\le H(X)$ hold for every single value $y$, or only on average (the book states only the averaged version, $H(X|Y)\le H(X)$)?
- Which inequalities make up the non-Shannon inequality's entropy form, and what does $\Gamma_n^*\subsetneq\Gamma_n$ imply for proving entropy bounds?
- How does $\log$ in $\frac1{1-\alpha}\log\sum p_i^\alpha$ tie Rényi orders to different tasks, given that $H_\alpha$ fails subadditivity?
- What exactly is the optimal expected number of yes/no questions for a general $X$ (promised in Section 10.3)?

## Reading notes
- Printed page = pdf page − 25. The source calls this "Chapter 1 Entropy", though the unit id says ch02.
- Sections 1.4 and 1.5 carry an asterisk in the headings. The pages do not say what it means, and I did not interpret it.
- Proof of 1.4(a) says "positive random variable"; non-negative is meant, since $\log\frac1{P}=0$ is allowed.
- Example 1.4(1) says $Y$ "agrees with $X$ with probability $\delta$". With $Z\sim\mathrm{Ber}(\delta)$ meaning $P[Z=1]=\delta$ (as in Example 1.1), $Y=X\oplus Z$ disagrees with probability $\delta$. The resulting $P_{X|Y=0}=\mathrm{Ber}(\delta)$ and $H(X|Y)=h(\delta)$ are unaffected.
- In the proof of Prop. 1.5, the printed sum "$\sum_{i=1}^n\Delta_i=0$" should run to $k$.
- Figure 1.1 shows no readable tick values on the $\sigma^2$ axis.
- References such as [115], [358], [472], [473], Chapters 3, 5, 8, 9, 10, Section 12.5* and Exercises I.1–I.3 are cited but not included in these pages.
- The pages contain no exercises of their own.
