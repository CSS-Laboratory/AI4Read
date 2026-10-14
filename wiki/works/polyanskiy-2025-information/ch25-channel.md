---
id: polyanskiy-2025-information/ch25-channel
work: polyanskiy-2025-information
unit: "Chapter 23 (unit id ch25-channel) — Channel coding with feedback, with Exercises for Part IV"
pages: 442–472
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Channel coding with feedback

## L0 — One line
Noiseless feedback cannot raise the capacity of a stationary memoryless channel, but used adaptively it can give zero error, variable length and variable power schemes with much better reliability and complexity.

## L1 — The gist (≤ 120 words)
The question is what a transmitter gains if it sees the receiver's past outputs. For stationary memoryless channels the capacity stays $C=\sup_{P_X} I(X;Y)$. A second, meta-converse proof of this uses Massey's directed information rather than ordinary mutual information. Feedback does help in three settings. With zero or very small error probability, the zero-error capacity and low-rate error exponents can improve. With variable-length transmission it removes the $\sqrt n$ dispersion penalty, and Burnashev's exponent is simple. With an expected-power constraint on the Gaussian-noise (AWGN) channel, Elias' linear scheme shrinks the estimation error exponentially, and Schalkwijk–Kailath's version for digital data gives doubly exponential error decay. Feedback does not change the rate limit, but it cuts latency and coding complexity.

**Prerequisites:** mutual information, chain rule, Fano's inequality, data processing; KL divergence; graphical models and d-separation; channel capacity; sequential testing (SPRT); Gaussian MMSE estimation.

## L2 — Key ideas
- A feedback code lets the input depend on the past outputs, $X_t=f_t(W,Y^{t-1})$. This breaks both the Markov chain $W\to X^n\to Y^n$ and the memorylessness of $X^n\to Y^n$ (pp. 442–445).
- Shannon (1956): for a stationary memoryless channel, $C_{fb}=C=C^{(I)}$. Achievability ($C_{fb}\ge C$) is obvious; a direct, non-rigorous construction is "posterior matching". The converse is by Fano plus a chain-rule argument (pp. 443–446).
- With feedback, fixed-length codes keep the dispersion expansion $nC-\sqrt{nV}Q^{-1}(\epsilon)+O(\log n)$ for weakly input-symmetric DMCs (p. 446).
- Massey's directed information $\vec I(X^n;Y^n)=\sum_t I(X^t;Y_t|Y^{t-1})$ is exactly the minimal divergence to a "causally conditioned" auxiliary model. It gives a meta-converse proof of $C_{fb}\le C$ (pp. 448–450).
- Zero-error capacity with feedback has the closed form $C_{fb,0}=\max_{P_X}\min_y\log\frac1{P_X(S_y)}$. It can strictly exceed $C_0$ and can be strictly below $C$ (pp. 450–454).
- Feedback leaves the sphere-packing bound (an upper bound on the error exponent) valid, but error exponents improve at rates below the critical rate: shown for the BEC (where $E_{fb}=E_{sp}$ up to $C$) and, as $R\to0+$, for the BSC (pp. 454–455).
- Variable-length feedback (VLF) codes have "zero dispersion": $\log M^*_{VLF}(\ell,\epsilon)=\frac{\ell C}{1-\epsilon}+O(\log\ell)$. Burnashev's exponent is $\frac{C_1}{C}(C-R)^+$ (pp. 455–457).
- For AWGN with an expected power constraint, Elias' scheme shrinks the estimation error variance as $2^{-2nC}$ (exponentially in $n$). Schalkwijk–Kailath uses it for digital data, with doubly exponential decay of the error probability at rates below capacity (pp. 457–459).

## L3 — Walkthrough

### Introduction (p. 442)
- The usual paradigm is one-way: encode, transmit, decode. Often the receiver can send feedback to the transmitter (p. 442).
- Motivating example: satellite downlink is costly (power) but uplink is cheap, so nearly noiseless feedback is available at the satellite (p. 442).
- Plan: first, following Shannon, noiseless feedback gives no capacity gain in the conventional setup, and Massey's directed information appears. Second, feedback helps for low error probability, variable length and variable power (p. 442).

### 23.1 Feedback does not increase capacity for stationary memoryless channels

**Definition 23.1 (code with feedback).** An $(n,M,\epsilon)$-code with feedback is a pair $(f,g)$.
- Time-varying encoder: $f_1:[M]\to\mathcal A$, $f_2:[M]\times\mathcal B\to\mathcal A$, …, $f_n:[M]\times\mathcal B^{n-1}\to\mathcal A$.
- Decoder: $g:\mathcal B^n\to[M]$, with $\mathbb P[W\neq\hat W]\le\epsilon$ (pp. 442–443).

Causality constraint: $X_t=f_t(W,Y_1^{t-1})$, with $W$ uniform on $[M]$, $\hat W=g(Y^n)$ (p. 443).

**Definition 23.2.**
$M^*_{fb}(n,\epsilon)=\max\{M:\exists\,(n,M,\epsilon)\text{ code with feedback}\}$, $C_{fb,\epsilon}=\liminf_{n}\frac1n\log M^*_{fb}(n,\epsilon)$, $C_{fb}=\lim_{\epsilon\to0}C_{fb,\epsilon}$ (p. 443).

**Theorem 23.3 (Shannon 1956).** For a stationary memoryless channel,
$$C_{fb}=C=C^{(I)}=\sup_{P_X}I(X;Y).$$

*Achievability (sketch, not rigorous).*
- The author notes $C_{fb}\ge C$ is obvious. He wants to show capacity-achieving feedback codes can be built directly, without the harder non-feedback problem (pp. 443–444).
- Let $\pi_t(\cdot)\triangleq P_{W|Y^t}(\cdot|Y^t)$ be the posterior after $t$ steps. Both ends know $Y^t$, so both know $\pi_t$ exactly (p. 444).
- Initialise $\pi_0=1/M$. At step $t+1$ the encoder sends $X_{t+1}=f_{t+1}(W,Y^t)$. Choosing $f_{t+1}$ is the same as partitioning $[M]$ into classes $\mathcal P_a=\{j:f_{t+1}(j,Y^t)=a\}$, $a\in\mathcal A$ (p. 444).
- Both parties update $\pi_{t+1}(j)=\pi_t(j)B_{t+1}(j)$ with
$$B_{t+1}(j)=\frac{P_{Y|X}(Y_{t+1}|f_{t+1}(j,Y^t))}{\sum_{a}\pi_t(\mathcal P_a)P_{Y|X}(Y_{t+1}|a)}$$
(denominator as intended; see Reading notes) (p. 444).
- The key identity:
$$\mathbb E[\log B_{t+1}(W)\mid Y^t]=\sum_{a}\sum_{y}\pi_t(\mathcal P_a)P_{Y|X}(y|a)\log\frac{P_{Y|X}(y|a)}{\sum_{a'}\pi_t(\mathcal P_{a'})P_{Y|X}(y|a')}=I(\tilde\pi_{t+1},P_{Y|X})\tag{23.1}$$
where $\tilde\pi_{t+1}(a)\triangleq\pi_t(\mathcal P_a)$ is the input law induced by the encoder's partition (p. 444).
- Taking logs, $\log\pi_t(j)=\sum_{s=1}^t\log B_s+\log\pi_0(j)$. The author expects $\log\pi_t(W)$ to behave like a random walk from $-\log M$ with positive drift (law of large numbers, more exactly martingales): $\log\pi_t(W)-\log\pi_0(W)\approx\sum_s\mathbb E[\log B_s]$ (p. 444).
- Best choice: partition so that $\tilde\pi_{t+1}\approx P_X^*$ (capacity-achieving input law). Then $\log\pi_t(W)\approx tC-\log M$, so transmission ends in time $\approx\frac{\log M}{C}$ (p. 444).
- Lesson, called *posterior matching* [384]: the induced input law $P_{X_{t+1}|Y^t}$ should be approximately the one maximising $I(X;Y)$ (pp. 444–445). Making this rigorous is possible via martingale convergence, as for SPRT in Section 16.3*, but is omitted since the theorem does not need it (p. 445).
- Footnote 1: Shannon's non-feedback theorem shows the (almost) optimal partitions can be preselected, independent of $\pi_t$ and the actual outputs (though dependent on $t$), so that $\pi_t(\mathcal P_a)\approx P^*_X(a)$ with overwhelming probability and for almost all $t\in[n]$ (p. 445).

> **Intuition note.** With feedback both sides track the receiver's belief about $W$. Each step should "spend" the channel's full information capacity on shrinking that belief. Capacity-sized steps give about $\log M/C$ steps in total, so this scheme runs at capacity (that nothing does better is the converse that follows).

*Converse.*
- Without feedback: $W\to X^n\to Y^n\to\hat W$ (23.2) and $-h(\epsilon)+\bar\epsilon\log M\le I(W;\hat W)\le I(X^n;Y^n)\le nC^{(I)}$ (p. 445).
- With feedback (Figure 23.2, $n=3$) the d-separation criterion shows (23.2) fails. Also $P_{Y^n|X^n}(y^n|x^n)\neq\prod_jP_{Y|X}(y_j|x_j)$, e.g. $X_2=Y_1$ makes $P_{Y_1|X_1X_2}=\delta_{X_1}$ (pp. 445–446).
- Still there are two Markov chains:
$$(Y^{t-1},W)\to X_t\to Y_t,\ t=1,\dots,n \tag{23.3}$$
$$W\to Y^n\to\hat W\tag{23.4}$$
- Then:
$$\begin{aligned}-h(\epsilon)+\bar\epsilon\log M&\le I(W;\hat W)&&\text{(Fano)}\\&\le I(W;Y^n)&&\text{(data processing, (23.4))}\\&=\sum_{t=1}^nI(W;Y_t|Y^{t-1})&&\text{(chain rule)}\\&\le\sum_{t=1}^nI(W,Y^{t-1};Y_t)&&\text{(since }I(W;Y_t|Y^{t-1})=I(W,Y^{t-1};Y_t)-I(Y^{t-1};Y_t))\\&\le\sum_{t=1}^nI(X_t;Y_t)&&\text{(data processing, (23.3))}\\&\le nC.\end{aligned}$$
(p. 446).

> **Intuition note.** Past outputs and the message together carry no more about $Y_t$ than the current input $X_t$ does. So each channel use contributes at most $C$ bits, feedback or not.

**Theorem 23.4 (dispersion with feedback [131, 336]).** For weakly input-symmetric DMCs (e.g. additive noise, BSC, BEC),
$$\log M^*_{fb}(n,\epsilon)=nC-\sqrt{nV}\,Q^{-1}(\epsilon)+O(\log n).$$
With fixed-length block coding, feedback does not improve the speed of approach to capacity; it can at most improve the third-order $\log n$ term (p. 446).

### 23.2* Massey's directed information
This section gives an alternative converse proof in the "channel substitution" (meta-converse) spirit, and defines directed information (p. 446).

*Recap without feedback.*
- Take an arbitrary $(n,M,\epsilon)$ code. Define $\mathbb P:W\to X^n\to Y^n\to\hat W$ (23.5) and $\mathbb Q:W\to X^n,\ Y^n\to\hat W$ (23.6), where $Y^n$ is disconnected from $X^n$ (p. 446).
- Observation 1: under $\mathbb Q$, $W\perp\!\!\!\perp\hat W$, so $\mathbb Q[W=\hat W]=\frac1M$, while $\mathbb P[W=\hat W]\ge1-\epsilon$ (p. 447).
- Observation 2: $P=P_{W,X^n}P_{Y^n|X^n}P_{\hat W|Y^n}$ and $Q=Q_{W,X^n}Q_{Y^n}Q_{\hat W|Y^n}$. Choosing the factors equal to those of $\mathbb P$ minimises $D(\mathbb P\|\mathbb Q)$:
$$\min D(\mathbb P\|\mathbb Q)=I(X^n;Y^n)\tag{23.7}$$
This is the information flow through the removed link $X^n\to Y^n$ (p. 447).
- Then, using data processing for divergence and the memoryless channel at $(*)$:
$$-h(\epsilon)+\bar\epsilon\log M=d\!\left(1-\epsilon\Big\|\tfrac1M\right)\overset{\text{DPI}}\le D(\mathbb P\|\mathbb Q)=I(X^n;Y^n)\overset{(*)}\le\sum_{i=1}^nI(X_i;Y_i)\le nC^{(I)}\tag{23.8}$$
(p. 447; see Reading notes on the first "=").

*Why this fails with feedback.*
- $X^n\to Y^n$ is no longer memoryless. Worse, with $\mathbb Q$ as in (23.6) and no Markov chain (23.5) under $\mathbb P$, the minimum becomes $\min D(\mathbb P\|\mathbb Q)=I(W,X^n;Y^n)$ (p. 447).
- This can be far above capacity. Take the useless channel $\mathrm{BSC}_{1/2}$ with $X_{t+1}=Y_t$: $I(W,X^n;Y^n)\ge H(Y^{n-1})=(n-1)\log2$, while $C=0$ (p. 447).
- Explanation: this value measures information flow through both the channel links ($\Rightarrow$) and the feedback links ($\rightsquigarrow$) of Figure 23.2. The goal is a $\mathbb Q$ whose minimum divergence counts only the $X_i\to Y_i$ links, while still $W\perp\!\!\!\perp\hat W$ (p. 447).

*The auxiliary family.* Restrict $\mathbb Q$ to the set $\mathcal Q$ of laws factorising as
$$Q_{W,X^n,Y^n,\hat W}=Q_WQ_{X_1|W}Q_{Y_1}Q_{X_2|W,Y_1}Q_{Y_2|Y_1}\cdots Q_{X_n|W,Y^{n-1}}Q_{Y_n|Y^{n-1}}Q_{\hat W|Y^n}$$
(Figure 23.3, right graph) (p. 448).
- By d-separation, $W\perp\!\!\!\perp\hat W$ for any $Q\in\mathcal Q$, because $X^n$ separates $W$ and $\hat W$. Conditioning on $W=w$ affects $X^n$ but not $Y^n,\hat W$ (p. 448).
- The directed links among the $Y_i$ keep as much dependence as possible, so $\mathbb Q$ can be close to $\mathbb P$. They were implicitly present in the non-feedback case. Footnote 3 calls this removal of one-directional links *causal conditioning* (p. 448).
- So $d(1-\epsilon\|\frac1M)\le D(\mathbb P\|\mathbb Q)$ for every $Q\in\mathcal Q$ (p. 448).

*Chain using Lemma 23.6 (stated below).*
$$d\!\left(1-\epsilon\Big\|\tfrac1M\right)\le\inf_{Q\in\mathcal Q}D(P\|Q)=\sum_{t=1}^nI(X_t;Y_t|Y^{t-1})=\sum_{t=1}^n\mathbb E_{Y^{t-1}}\big[I(P_{X_t|Y^{t-1}},P_{Y|X})\big]$$
$$\le\sum_{t=1}^nI\big(\mathbb E_{Y^{t-1}}[P_{X_t|Y^{t-1}}],P_{Y|X}\big)=\sum_{t=1}^nI(P_{X_t},P_{Y|X})\le nC^{(I)}$$
The inequality uses concavity of $I(\cdot,P_{Y|X})$ (pp. 448–449).
- Hence $-h(\epsilon)+\bar\epsilon\log M\le nC^{(I)}$, so $\log M\le\frac{nC+h(\epsilon)}{1-\epsilon}$, $C_{fb,\epsilon}\le\frac{C}{1-\epsilon}$, and $C_{fb}\le C$ (p. 449).
- The proof adapts essentially unchanged to cost constraints and capacity per unit cost [337] (p. 449).

**Definition 23.5 (Massey's directed information).** For blocklength-$n$ variables,
$$\vec I(X^n;Y^n)\triangleq\sum_{t=1}^nI(X^t;Y_t|Y^{t-1}).$$
It is not symmetric. According to [294] and later work it quantifies causal information transfer from the $X$-process to the $Y$-process (p. 449).

**Lemma 23.6.** Take a non-anticipatory channel, given by Markov kernels $P_{Y_t|X^t,Y^{t-1}}$, with
$$P_{W,X^n,Y^n,\hat W}=P_W\prod_{t=1}^nP_{X_t|W,X^{t-1},Y^{t-1}}P_{Y_t|X^t,Y^{t-1}}\tag{23.9}$$
(the product is followed by $P_{\hat W|Y^n}$). Let $\mathcal Q$ be the laws with
$$Q_{W,X^n,Y^n,\hat W}=Q_W\prod_tQ_{X_t|W,Y^{t-1}}Q_{Y_t|Y^{t-1}}\tag{23.10}$$
(also followed by $Q_{\hat W|Y^n}$). Then
$$\inf_{Q\in\mathcal Q}D(P_{W,X^n,Y^n,\hat W}\|Q_{W,X^n,Y^n,\hat W})=\vec I(X^n;Y^n).\tag{23.11}$$
If in addition the channel is memoryless, $P_{Y_t|X^t,Y^{t-1}}=P_{Y_t|X_t}$, then $\vec I(X^n;Y^n)=\sum_tI(X_t;Y_t|Y^{t-1})$ (pp. 449–450).

*Proof (pp. 449–450).*
- Compare (23.9), (23.10) and use the chain rule for divergence (2.26). The terms can be optimised at $Q_{X,W}=P_{X,W}$, $Q_{X_t|W,Y^{t-1}}=P_{X_t|W,Y^{t-1}}$, $Q_{\hat W|Y^n}=P_{W|Y^n}$ (as printed; the author leaves the justification as an exercise).
- What remains is
$$\inf_Q\Big[D(P_{Y_1|X_1}\|Q_{Y_1}|X_1)+D(P_{Y_2|X^2,Y_1}\|Q_{Y_2|Y_1}|X^2,Y_1)+\cdots+D(P_{Y_n|X^n,Y^{n-1}}\|Q_{Y_n|Y^{n-1}}|X^n,Y^{n-1})\Big]$$
$$=I(X_1;Y_1)+I(X^2;Y_2|Y_1)+\cdots+I(X^n;Y_n|Y^{n-1}),$$
by conditional versions of Corollary 4.2.
- Memoryless case: $I(X^t;Y_t|Y^{t-1})=I(X_t;Y_t|Y^{t-1})+I(X^{t-1};Y_t|Y^{t-1},X_t)$. The last term is zero by d-separation: without channel memory every undirected path from $X^{t-1}$ to $Y_t$ passes through $X_t$, a conditioned non-collider.

> **Intuition note.** Ordinary mutual information would also count information that travels back through the feedback links. Directed information counts only what flows forward, input to output, given the past outputs, and that is bounded by $C$ per use.

The section ends with an unfinished sentence ("instead of using", p. 450; see Reading notes).

### 23.3 When is feedback really useful?
Theorems 23.3 and 23.4 say feedback improves the rate neither asymptotically nor for moderate blocklengths. Three cases are examined where it helps a lot (p. 450).

#### 23.3.1 Codes with very small (e.g. zero) error probability
**Theorem 23.7 (Shannon [379]).** For any DMC $P_{Y|X}$,
$$C_{fb,0}=\max_{P_X}\min_{y\in\mathcal B}\log\frac1{P_X(S_y)}\tag{23.12}$$
where $S_y=\{x\in\mathcal A:P_{Y|X}(y|x)>0\}$ is the set of inputs that can lead to output $y$ (pp. 450–451). Here $C_{fb,0}$ is $C_{fb,\epsilon}$ at $\epsilon=0$.

**Remark 23.1.** For stationary memoryless channels, $C_0\overset{(a)}\le C_{fb,0}\overset{(b)}\le C_{fb}=\lim_{\epsilon\to0}C_{fb,\epsilon}\overset{(c)}=C=\lim_{\epsilon\to0}C_\epsilon\overset{(d)}=C^{(I)}$. (a), (b) are by definition, (c) is Theorem 23.3, (d) is Theorem 19.9. All use fixed-length block codes (p. 451).

**Remark 23.2.**
1. For a DMC, both zero-error capacities depend only on the support of $P_{Y|X}$, i.e. on the bipartite graph between $\mathcal A$ and $\mathcal B$. $C_0$ (but not $C_{fb,0}$) is a function of the *confusability graph*: vertices $\mathcal A$, with $a\ne a'$ joined iff $\exists b$ with $P_{Y|X}(b|a)P_{Y|X}(b|a')>0$ (p. 451).
2. $C_{fb,0}$ is not a function of the confusability graph alone. The polygon channel with $L=3$ has $C_{fb,0}=\log\frac32$, and the useless channel with $\mathcal A=\{1,2,3\},\mathcal B=\{1\}$ has $C_{fb,0}=0$. Both have a triangle as confusability graph (p. 451).
3. $C_0$ is often very hard to compute, but $C_{fb,0}$ has the closed form (23.12). In the *polygon channel* (input and output $\{1..L\}$, inputs confusable with a neighbour; confusability graph an $L$-cycle, as described in Exercise IV.36, p. 471), the known $C_0$ values are (pp. 451–452):
   - $L=3$: $C_0=0$.
   - $L=5$: $C_0=\frac12\log5$ ("capacity of a pentagon"). Blocklength one gives rate 1 bit with $\{1,3\}$. Blocklength two gives rate $\frac12\log5$ with the codebook $\{(1,1),(2,3),(3,5),(4,2),(5,4)\}$ (Shannon, 1956). Lovász later proved optimality by a semidefinite programming relaxation.
   - Even $L$: $C_0=\log\frac L2$ (Exercise IV.36).
   - $L=7$: $\frac35\log7\le C_0\le\log3.32$. The exact value for odd $L\ge7$ is a famous open problem.
   - Odd $L$: $C_0=\log\frac L2+o(1)$ [66].
   - With feedback, $C_{fb,0}=\log\frac L2$ for any $L$, so it can strictly exceed $C_0$ (Exercise IV.36).
4. $C_{fb,0}$ need not equal $C_{fb}=C$. Example (bipartite graph on inputs/outputs 1–4: inputs 1, 2, 3 each reach two of the outputs 1–3; input 4 reaches only output 4): $C_0=\log2$; $C_{fb,0}=\max_\delta-\log\max(\frac23\delta,1-\delta)$ with $P^*_X=(\delta/3,\delta/3,\delta/3,\bar\delta)$, giving $\log\frac52>C_0$ at $\delta^*=\frac35$. Meanwhile $C=C_{fb}$ can be made arbitrarily close to $\log4$ by taking the crossover probabilities near zero, with the same confusability graph. So $C_0<C_{fb,0}<C_{fb}=C$ (p. 452).

*Proof of Theorem 23.7* (pp. 452–454).
1. Fix an $(n,M,0)$-code. The confusability set after $y^t$ is $E_t(y^t)=\{m:f_1(m)\in S_{y_1},f_2(m,y_1)\in S_{y_2},\dots\}$ (the printed last entry reads $f_n(m,y^{t-1})\in S_{y_t}$, where $f_t$ is meant), the messages that could have produced $y^t$. Zero error means
$$\epsilon=0\iff\forall y^n,\ |E_n(y^n)|\in\{0,1\}\tag{23.13}$$
2. Define $\theta_{fb}\triangleq\min_{P_X}\max_yP_X(S_y)$, with minimiser $P_X^*$. The goal is $C_{fb,0}=\log\frac1{\theta_{fb}}$. By definition
$$\forall P_X\ \exists y\text{ with }P_X(S_y)\ge\theta_{fb}\tag{23.14}$$
$P^*_X$ is in general not the usual capacity-achieving input law (p. 453).
3. "$\le$" (converse): take $P_{X^n}$ to be the law of the codewords, and $E_0=[M]$. At $t=1$, (23.14) gives $y_1^*$ with $|E_1(y_1^*)|/|E_0|\ge\theta_{fb}$. At $t=2$, applying (23.14) to $P_{X_2|X_1\in S_{y_1^*}}$ gives $y_2^*$ with $|E_2(y_1^*,y_2^*)|/|E_1(y_1^*)|\ge\theta_{fb}$. Continue to $t=n$. By (23.13) and this selection,
$$\frac1M\ge\frac{|E_n(y_1^*..y_n^*)|}{|E_0|}\ge\theta_{fb}^n.$$
So $\log M\le-n\log\theta_{fb}$ (printed "$M\le-n\log\theta_{fb}$", see Reading notes) and $C_{fb,0}\le-\log\theta_{fb}$ (p. 453).
4. "$\ge$" (achievability): in stage one, $f_1$ splits the $M$ messages into groups of sizes $\propto P^*_X(a_i)$, and sends the group's symbol (Figure 23.4, $|\mathcal A|=|\mathcal B|=3$). If the output is, say, $y_1$ with $S_{y_1}=\{a_1,a_2\}$, the decoder eliminates $MP_X^*(a_3)$ candidates. The remaining $MP^*_X(S_{y_1})\le M\theta_{fb}$ messages are re-partitioned in round two, and so on. Each round shrinks the confusability set by a factor of at least $\theta_{fb}$. After $n$ rounds its size is at most $M\theta_{fb}^n$. If that is $\le1$ the error is zero, which holds for $\log M=-n\log\theta_{fb}$. So $-n\log\theta_{fb}$ bits are delivered reliably with $n+O(1)$ uses, giving $C_{fb,0}\ge-\log\theta_{fb}$ (pp. 453–454). Footnote 4: rounding fixes are needed in the last steps, with no effect on the asymptotics (p. 454).

> **Intuition note.** Each output tells the encoder which messages are still possible. The encoder then splits only the survivors, so the survivors shrink by at least a fixed factor per use.

*Beyond zero error.*
- For generic DMCs such as $\mathrm{BSC}_\delta$, $\delta\in(0,1)$, $C_0=C_{fb,0}=0$, so one must study $\epsilon>0$. For weakly input-symmetric channels, [336] gives the dispersion expansion above, so up to second order the fundamental limits are unchanged by feedback (p. 454).
- Error exponent: $E_{fb}(R)\triangleq\lim_n-\frac1n\log\epsilon^*_{fb}(n,\exp\{nR\})$, if the limit exists (p. 454).
- The sphere-packing bound (22.14) still holds with feedback [312]: $E_{fb}(R)\le E_{sp}(R)$. Hence for $R\in(R_{cr},C)$, $E_{fb}(R)=E(R)$ and feedback changes nothing there (pp. 454–455).
- Exponents do improve below the critical rate. For $\mathrm{BEC}_\delta$, retransmitting each bit until it is unerased gives error probability $\mathbb P[\mathrm{Bin}(n,\delta)>n(1-R/\log2)]$ and $E_{fb}(R)=E_{sp}(R)$ for $0<R<C$, strictly above $E(R)$ for $R<R_{cr}$ (p. 455).
- For $\mathrm{BSC}_\delta$, Berlekamp's result (as printed):
$$E_{fb}(0+)=-\log\!\big((1-\delta)^{1/3}\delta^{2/3}+(1-\delta)^{2/3}\delta^{1/3}\big)>E(0+)=E_{ex}(0)=-\tfrac14\log(4\delta(1-\delta)).$$
So the error probability of optimal codes of size $M=\exp\{o(n)\}$ improves significantly with feedback, at least for BSC and BEC (p. 455).

#### 23.3.2 Codes with variable length
- BEC$_\delta$ scheme for $k$ bits: send each bit repeatedly until it arrives unerased. Feedback tells the transmitter when. The expected number of uses is $\ell=\mathbb E[n]=\frac k{1-\delta}$. Capacity is reached by coding each bit independently, with no finite-blocklength penalty (p. 455).

**Definition 23.8 (VLF code).** An $(\ell,M,\epsilon)$ variable-length feedback code consists of (pp. 455–456):
1. A space $\mathcal U$ and law $P_U$; $U$ is common randomness revealed to both sides before transmission (footnote 5: $|\mathcal U|\le3$ suffices [336]).
2. Encoders $f_n:\mathcal U\times[M]\times\mathcal B^{n-1}\to\mathcal A$ with $X_n=f_n(U,W,Y^{n-1})$ (23.15), $W$ equiprobable.
3. Decoders $g_n:\mathcal U\times\mathcal B^n\to[M]$.
4. A stopping time $\tau$ of $\mathcal G_n=\sigma\{U,Y_1..Y_n\}$ with $\mathbb E[\tau]\le\ell$ (23.16). The decision is $\hat W=g_\tau(U,Y^\tau)$ (23.17) with $\mathbb P[\hat W\ne W]\le\epsilon$ (23.18).

$M^*_{VLF}(\ell,\epsilon)=\max\{M:\exists(\ell,M,\epsilon)\text{-VLF code}\}$ (23.19). The BEC example shows $\log M^*_{VLF}(\ell,0)\ge(1-\delta)\ell\log2+O(1)$ as $\ell\to\infty$. The $\sqrt{nV}Q^{-1}(\epsilon)$ term is gone, which is why such results are called *zero-dispersion* (p. 456).

**Theorem 23.9 (VLF zero dispersion [336]).** For any DMC with capacity $C$,
$$\log M^*_{VLF}(\ell,\epsilon)=\frac{\ell C}{1-\epsilon}+O(\log\ell)\tag{23.20}$$
Proof omitted. The achievability uses ideas like SPRT (Section 16.3*): keep transmitting until the information density $i(c_j;Y^n)$ of some codeword exceeds $\log M$. In VLFT codes the transmitter decides the stopping time (Exercise IV.35(d)); (23.20) still holds for them [336] (p. 456).

**Example 23.1.** For $\mathrm{BSC}_{0.11}$ without feedback, $n=3000$ is the minimal blocklength to reach 90% of capacity. A VLF code with $\ell=\mathbb E[n]=200$ achieves it [336]. This shows how much feedback can cut latency and decoding complexity (p. 456).

**Burnashev's exponent [79].** For every DMC, with $\log M=\ell R$,
$$\epsilon^*_{VLF}(\ell,\exp\{\ell R\})=\exp\{-\ell E_{VLF}(R)+o(\ell)\},\quad E_{VLF}(R)=\frac{C_1}{C}(C-R)^+,\quad C_1=\max_{x_1,x_2}D(P_{Y|X=x_1}\|P_{Y|X=x_2}).$$
This is strikingly simple compared with the largely open non-feedback and fixed-length-feedback exponents (pp. 456–457).

> **Intuition note.** With a variable stopping time the decoder simply waits until it is confident. In the BEC example unlucky noise costs extra time instead of an error, and in general VLF codes lose the finite-length $\sqrt n$ penalty (for $\epsilon>0$ as well).

#### 23.3.3 Codes with variable power
- Under the fixed power constraint $\sum_jx_j^2\le nP$ for every codeword, feedback does not help much in any dispersion, finite-blocklength or exponent sense. The potential is unlocked by the relaxed constraint $\mathbb E[\sum_jX_j^2]\le nP$, the expectation being over the channel noise and the transmitter's randomness (p. 457).

**Elias' scheme.**
- Send $A\sim\mathcal N(0,1)$ over $Y_k=X_k+Z_k$, $Z_k\sim\mathcal N(0,\sigma^2)$ i.i.d., $\mathbb E[X_k^2]\le P$, with full noiseless feedback. The expectation constraint does not raise capacity (converse of Theorem 20.6) but allows simple algorithms. If each codeword must satisfy $\sum X_k^2\le nP$ almost surely, Elias' scheme does not work (p. 457).
- Linear processing (Figure 23.5): $X_1=c_1A$; $Y_1=c_1A+Z_1$, $\hat A_1=\mathbb E[A|Y_1]=\frac{\sqrt P}{P+\sigma^2}Y_1$; then $X_t=c_t(A-\hat A_{t-1})$, $Y_t=X_t+Z_t$, and $\hat A_t=\mathbb E[A|Y^t]$ is a linear combination of $Y^t$. Each $c_t$ is chosen so that $\mathbb E[X_t^2]=P$ (p. 458).
- By the orthogonality principle $A=\hat A_t+N_t$ with $N_t\perp\!\!\!\perp Y^t$ (jointly Gaussian since everything is linear). Since $X_t\propto N_{t-1}\perp\!\!\!\perp Y^{t-1}$, each transmission is independent of the past output history ("innovation") (p. 457).
- $Y^n\to\hat A_n\to A$, and $\hat A_n$ is a sufficient statistic of $Y^n$ for $A$ by Gaussianity:
$$I(A;Y^n)=I(A;\hat A_n,Y^n)=I(A;\hat A_n)+I(A;Y^n|\hat A_n)=I(A;\hat A_n)=\tfrac12\log\frac{\mathrm{Var}(A)}{\mathrm{Var}(N_n)}$$
using $\hat A_n\perp\!\!\!\perp N_n$ and the Gaussian mutual information formula (Example 3.3) (p. 458).
- Also, by the chain rule and since $X_t\perp\!\!\!\perp Y^{t-1}$ (the "key" step):
$$I(A;Y^n)=\sum_tI(A;Y_t|Y^{t-1})=\sum_tI(X_t;Y_t|Y^{t-1})\overset{\text{key}}=\sum_tI(X_t;Y_t)=\tfrac n2\log(1+P)=nC$$
(pp. 458–459).
- Therefore $\mathrm{Var}N_n=\mathrm{Var}(\hat A_n-A)=2^{-2nC}\mathrm{Var}A$. The printed closed form is $(P/(P+\sigma^2))^n$ (see Reading notes). Uncertainty falls exponentially fast in $n$ (p. 459).

**Schalkwijk–Kailath scheme (digital data).**
- Let $W$ be uniform on the $M$-PAM constellation in $[-1,1]$, $\{-1,-1+\frac2M,\dots,-1+\frac{2k}M,\dots,1\}$. First send $X_0=\sqrt PW$, $Y_0=X_0+Z_0$. The encoder knows $Y_0,X_0$, hence $Z_0$, so describing $W$ amounts to describing $Z_0$. This is done by Elias' scheme for $n-1$ uses (p. 459).
- The equivalent output is $\tilde Y_0=X_0+\tilde Z_0$, $\mathrm{Var}(\tilde Z_0)=2^{-2(n-1)C}$. The decoder rounds to the nearest PAM point (p. 459).
- As printed: $\epsilon\le\mathbb P[|\tilde Z_0|>\frac1{2M}]=\mathbb P[2^{-(n-1)C}|Z|>\frac{\sqrt P}{2M}]=2Q\!\big(\frac{2^{(n-1)C}\sqrt P}{2M}\big)$. Hence $\log M\ge(n-1)C+\log\frac{\sqrt P}2-\log Q^{-1}(\frac\epsilon2)=nC+O(1)$ (p. 459).
- For any rate strictly below capacity the error probability decays *doubly exponentially* in $n$. The scheme gains a $\sqrt n$ term in $\log M$ compared with $\log M^*(n,\epsilon)=nC-\sqrt{nV}Q^{-1}(\epsilon)+O(\log n)$ (Theorem 22.2) (p. 459).
- Example as printed: $P=1$, $C=0.5$ bit per use. For $\epsilon=10^{-3}$, $2Q(\cdot)\approx10^{-3}$ gives a ratio $\approx3$ and $\frac{\log M}n\approx\frac{n-1}nC-\frac{\log8}n$. Capacity is reached within 99% in as few as $n=50$ uses, while block codes without feedback need $n\approx2800$ to reach 90% (p. 459).

**Take-away.** "Feedback is best harnessed with adaptive strategies." It does not raise capacity under block coding, but it can greatly boost reliability and reduce coding complexity (p. 459).

### Exercises for Part IV (pp. 460–471)
Pages 460–471 list Exercises IV.1–IV.37 for the whole of Part IV. They cover many topics (finite blocklength, random linear codes, universal codes, constrained and non-stationary channels, strong converses and so on). Only the exercises tied to this chapter are listed under "Exercises worth doing". Feedback-specific ones are IV.34–IV.37 (pp. 470–471); the VLF/VLFT variant is in IV.35(d). Solutions are not printed.

## Toy example (ours, not from the text)
**Posterior matching on a BEC with $\delta=\frac12$.** Take $M=4$ messages and inputs $\mathcal A=\{0,1\}$. $\mathrm{BEC}_{1/2}$ has $C=1-\delta=0.5$ bit, and the uniform input achieves it.
1. Start with $\pi_0(j)=\frac14$ for $j=1..4$. Partition $\mathcal P_0=\{1,2\}$, $\mathcal P_1=\{3,4\}$, so $\tilde\pi_1=(\frac12,\frac12)$.
2. Suppose $W=3$, so the encoder sends $a=1$. The output is $y=1$ (prob. $\frac12$) or erasure $e$ (prob. $\frac12$).
3. If $y=1$: denominator $\sum_a\pi_0(\mathcal P_a)P(1|a)=\frac12\cdot0+\frac12\cdot\frac12=\frac14$. For $j\in\{3,4\}$ the numerator is $P(1|1)=\frac12$, so $B=\frac{1/2}{1/4}=2$ and $\pi_1(3)=\frac14\cdot2=\frac12$. For $j\in\{1,2\}$ the numerator is 0, so $\pi_1(j)=0$.
4. If $y=e$: denominator $=\frac12\cdot\frac12+\frac12\cdot\frac12=\frac12$, numerator $=\frac12$, so $B=1$ and the posterior is unchanged.
5. $\mathbb E[\log B(W)|Y^0]=\frac12\log_22+\frac12\log_21=0.5$ bit. This equals $I(\tilde\pi_1,\mathrm{BEC})=(1-\delta)H(\tilde\pi_1)=0.5\cdot1=0.5$, as (23.1) says. It also equals $C$, because the partition induces the capacity-achieving input law.
6. Time to reach $\log\pi_t(W)=0$ is $\approx\frac{\log M}{C}=\frac{2}{0.5}=4$ uses. This matches the retransmission scheme: $k=2$ bits, $\ell=\frac{k}{1-\delta}=\frac2{0.5}=4$.

## Concepts
- [[channel-with-feedback]] (new) — code whose input $X_t=f_t(W,Y^{t-1})$ may depend on past outputs; here the feedback is noiseless and instantaneous (p. 443)
- [[channel-capacity]] — here $C=\sup_{P_X}I(X;Y)$ and $C_{fb}=C$ for stationary memoryless channels (p. 443)
- [[noisy-channel-coding-theorem]] — Theorem 23.3 extends the converse side to feedback (p. 443)
- [[fanos-inequality]] — used as $-h(\epsilon)+\bar\epsilon\log M\le I(W;\hat W)$ (p. 446)
- [[data-processing-inequality]] — applied to (23.3), (23.4) and to divergences (pp. 446–447)
- [[chain-rule]] — mutual-information chain rule; divergence chain rule (2.26) in Lemma 23.6 (pp. 446, 450)
- [[relative-entropy-kl-divergence]] — $D(\mathbb P\|\mathbb Q)$ minimised over $\mathcal Q$ gives information flow (p. 447)
- [[mutual-information]] — $I(\tilde\pi,P_{Y|X})$ is the drift of the log-posterior (p. 444)
- [[directed-information]] (new) — $\vec I(X^n;Y^n)=\sum_tI(X^t;Y_t|Y^{t-1})$, not symmetric, causal transfer $X\to Y$ (p. 449)
- [[posterior-matching]] (new) — choose the partition so the induced input law matches the capacity-achieving law (p. 445)
- [[zero-error-capacity]] (new) — rate with $\epsilon=0$; with feedback $C_{fb,0}=\max_{P_X}\min_y\log\frac1{P_X(S_y)}$ (pp. 450–451)
- [[confusability-graph]] (new) — graph on inputs, edge iff a common output is possible; determines $C_0$ but not $C_{fb,0}$ (p. 451)
- [[variable-length-feedback-code]] (new) — VLF: stopping time $\tau$ with $\mathbb E\tau\le\ell$, common randomness $U$ (p. 455)
- [[zero-dispersion]] (new) — VLF expansion lacks the $\sqrt{n}$ term: $\ell C/(1-\epsilon)+O(\log\ell)$ (p. 456)
- [[burnashev-exponent]] (new) — $E_{VLF}(R)=\frac{C_1}{C}(C-R)^+$ (p. 457)
- [[elias-scheme]] (new) — linear scheme sending a Gaussian by repeatedly transmitting the scaled estimation error (p. 457)
- [[schalkwijk-kailath-scheme]] (new) — Elias' scheme applied to PAM data, giving doubly exponential error decay (p. 459)
- [[shannon-hartley-formula]] — per-use $C=\frac12\log(1+P)$ in the AWGN computation, with $\sigma^2=1$ implicit (p. 458)

## Canonical instances
- [[bsc]] — useless $\mathrm{BSC}_{1/2}$ with $X_{t+1}=Y_t$ breaks the naive converse; $\mathrm{BSC}_{0.11}$ latency example; Berlekamp's exponent (pp. 447, 455–456)
- [[bec]] — retransmit-until-unerased: capacity with variable length, $E_{fb}=E_{sp}$ (p. 455)
- [[polygon-channel]] (new) — zero-error capacities with and without feedback; pentagon (pp. 451–452)
- [[awgn-channel]] — Elias and Schalkwijk–Kailath schemes under an expected power constraint (pp. 457–459)

## Bridges (candidates)
- [structural-analogy] directed information $\vec I(X^n;Y^n)$ ↔ information-theory: transfer entropy — both are sums of conditional mutual informations measuring causally directed flow, though the conditioning sets differ.
- [structural-analogy] VLF decoder stopping when $i(c_j;Y^n)$ exceeds $\log M$ ↔ statistics: sequential probability ratio test (SPRT) — the source itself says the achievability uses ideas similar to SPRT.
- [structural-analogy] Elias' scheme (send the innovation, orthogonal to past outputs) ↔ estimation theory: recursive linear MMSE/innovations estimation.
- [metaphor] Posterior-matching partition (halve the surviving candidates) ↔ twenty-questions search with adaptive questions.

## Questions this raises
- The achievability sketch of Theorem 23.3 is not rigorous. How exactly does martingale convergence give the time-to-termination $\approx\log M/C$ (pp. 444–445)?
- Berlekamp's $E_{fb}(0+)$ for the BSC is stated without proof. Which feedback strategy attains it, and does it exceed the BEC-style retransmission intuition (p. 455)?
- Why does an almost-sure power constraint defeat Elias' scheme, and how much of the gain survives under a per-codeword constraint (p. 457)?
- What changes with noisy or partial feedback, which the introduction mentions (p. 442)?

## Exercises worth doing
- Ex. IV.34 (p. 470) — show feedback of a second output $U$ does not increase capacity, and capacity per unit cost is still $\max_{x\ne x_0}D(P_{Y|X=x}\|P_{Y|X=x_0})/c(x)$ — difficulty: medium
- Ex. IV.35 (p. 471) — compute $C$, $C_0$, $C_{fb,0}$ (and the VLFT variant) for a BSC whose noise is also seen through a BEC — difficulty: medium
- Ex. IV.36 (p. 471) — prove $C_{fb,0}=\log\frac L2$ for the polygon channel and $C_0$ for even $L$ and the path channel — difficulty: hard
- Ex. IV.37 (p. 471) — design a fixed-length capacity-achieving feedback scheme for the BEC with exponent equal to the sphere-packing bound — difficulty: medium

## Reading notes
- Printed chapter number is 23; the unit id is "ch25". Printed page labels are present (printed = pdf − 25). Page pdf 497 (printed 472) is blank.
- Printed (23.1) shows a trailing "$a$" in its denominator, and both (23.1) and the printed $B_{t+1}$ omit the weight $P_{Y|X}(y|a)$ in the denominator sum ((23.1) also omits it in front of the log); I wrote the intended $\sum_{a'}\pi_t(\mathcal P_{a'})P_{Y|X}(y|a')$ with the weights.
- In (23.8) the page shows $-h(\epsilon)+\bar\epsilon\log M=d(1-\epsilon\|\frac1M)$. By direct computation $d(1-\epsilon\|\frac1M)=-h(\epsilon)+\bar\epsilon\log M+\epsilon\log\frac M{M-1}$, so "$\le$" is the correct direction.
- The proof of Theorem 23.7 prints "$M\le-n\log\theta_{fb}$"; from $\frac1M\ge\theta_{fb}^n$ it should read $\log M\le-n\log\theta_{fb}$.
- The sentence ending Section 23.2 ("instead of using") is cut off in the source.
- On p. 459 the closed form $\mathrm{Var}N_n=(P/(P+\sigma^2))^n$ does not match $2^{-2nC}\mathrm{Var}A$ with $C=\frac12\log(1+P/\sigma^2)$. Checking $\mathrm{Var}(A-\hat A_1)=1-\frac P{P+\sigma^2}$, I get $\sigma^2/(P+\sigma^2)$ per step. The step "$\frac n2\log(1+P)=nC$" implicitly takes $\sigma^2=1$.
- Schalkwijk–Kailath example, p. 459: "log M ≥ …" reads as the largest size achievable at error $\epsilon$ (the condition bounds $M$ from above). The printed "$e^{(n-1)C}/2M\approx3$" seems to mean $2^{(n-1)C}$. Using the printed formula at $n=50$ with $C=0.5$ I get rate $\approx0.49-0.06=0.43$ bit, i.e. about 86% of $C$, not the printed "99%". I could not reconcile this.
- The chapter's own examples (BSC$_{0.11}$ latencies, $n=3000$, $\ell=200$) are quoted from [336] without derivation.
- Exercises IV.1–IV.33 are not about feedback and are not digested.
