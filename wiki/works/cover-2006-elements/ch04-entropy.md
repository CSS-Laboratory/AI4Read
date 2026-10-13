---
id: cover-2006-elements/ch04-entropy
work: cover-2006-elements
unit: "4 Entropy Rates of a Stochastic Process"
pages: 60-77
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Entropy Rates of a Stochastic Process

## L0 — One line
For a stationary process, the entropy per symbol, $\frac1n H(X_1,\dots,X_n)$, and the conditional entropy of the next symbol given the whole past have the same limit, called the entropy rate; it is easy to compute for Markov chains and can be bracketed for functions of Markov chains.

## L1 — The gist (≤ 120 words)
Chapter 3 treated independent symbols. This chapter asks how the entropy of $n$ symbols grows when they are dependent. For a stationary process, two natural "rates" exist: entropy per symbol, $H(\mathscr X)$, and the conditional entropy of the last symbol given the past, $H'(\mathscr X)$. Both limits exist and are equal. For a stationary Markov chain the rate is $-\sum_{ij}\mu_iP_{ij}\log P_{ij}$. Examples are a random walk on a weighted graph and a function of a Markov chain (hidden Markov model), where upper and lower bounds converge to the rate. The rate matters because, via the AEP for stationary ergodic processes, it is the description length per symbol.

**Prerequisites:** conditional entropy and chain rule; "conditioning reduces entropy"; mutual information; matrices and stationary vectors; limits of sequences.

## L2 — Key ideas
- A stationary process has joint laws invariant to time shifts; a Markov chain makes each symbol depend only on its predecessor, so $p(x_1,\dots,x_n)=p(x_1)\prod p(x_i|x_{i-1})$ (pp. 60–61).
- The entropy rate $H(\mathscr X)=\lim \frac1n H(X_1,\dots,X_n)$ need not exist for every process (for stationary ones it does, Theorem 4.2.1): a carefully built independent, non-identical sequence has an oscillating running average (p. 63).
- Theorem 4.2.1: for a stationary process, $H(\mathscr X)=H'(\mathscr X)$. The proof uses monotonicity of $H(X_n|X_{n-1},\dots,X_1)$, the chain rule and the Cesàro mean (the running average of a convergent sequence has the same limit) (pp. 64–65).
- The AEP (asymptotic equipartition property: a typical set of about $2^{nH(\mathscr X)}$ sequences, each of probability about $2^{-nH(\mathscr X)}$, has probability close to 1) for stationary ergodic processes (a condition this chapter does not define; proved later, §15.7) makes $H(\mathscr X)$ the number of bits per symbol for describing typical sequences (p. 65).
- Stationary Markov chain: $H(\mathscr X)=H(X_2|X_1)=-\sum\mu_iP_{ij}\log P_{ij}$ (p. 66).
- Random walk on a weighted graph: $\mu_i=W_i/2W$, and the rate is the entropy of the edge distribution minus that of the node distribution. A king on a chessboard has rate $0.92\log 8$ (pp. 67–68).
- For $Y_i=\phi(X_i)$, the quantities $H(Y_n|Y_{n-1},\dots,Y_1,X_1)$ and $H(Y_n|Y_{n-1},\dots,Y_1)$ bound $H(\mathscr Y)$ from below and above and converge to it (pp. 69–71).

## L3 — Walkthrough

**Opening (p. 60).** Chapter 3's AEP says $nH(X)$ bits suffice on the average for $n$ i.i.d. variables. Here the variables may be dependent. The claim: for a stationary process $H(X_1,\dots,X_n)$ grows linearly in $n$ at rate $H(\mathscr X)$. Reading this as the best achievable compression awaits Chapter 5.

### 4.1 Markov chains (pp. 60–62)
- A *stochastic process* is an indexed sequence of random variables, described by joint pmfs $p(x_1,\dots,x_n)$ (p. 60).
- *Stationary*: for every shift $l$,
$$\Pr\{X_1=x_1,\dots,X_n=x_n\}=\Pr\{X_{1+l}=x_1,\dots,X_{n+l}=x_n\}\tag{4.1}$$
- *Markov chain*: each variable depends on the past only through its predecessor:
$$\Pr(X_{n+1}=x_{n+1}|X_n=x_n,\dots,X_1=x_1)=\Pr(X_{n+1}=x_{n+1}|X_n=x_n)\tag{4.2}$$
Hence
$$p(x_1,\dots,x_n)=p(x_1)p(x_2|x_1)\cdots p(x_n|x_{n-1}).\tag{4.3}$$
- *Time invariant*: $\Pr\{X_{n+1}=b|X_n=a\}=\Pr\{X_2=b|X_1=a\}$ (4.4). Assumed unless otherwise stated. The chain is described by its initial state and the transition matrix $P=[P_{ij}]$, $P_{ij}=\Pr(X_{n+1}=j|X_n=i)$ (p. 61).
- *Irreducible*: from any state one can reach any other with positive probability in finitely many steps (p. 61).
- Distribution update: $p(x_{n+1})=\sum_{x_n}p(x_n)P_{x_nx_{n+1}}$ (4.5). A *stationary distribution* is one left unchanged by this update. If the initial state is drawn from it, the chain is a stationary process (p. 61).
- If the finite chain is irreducible and aperiodic, the stationary distribution is unique and any starting distribution converges to it (p. 62).

**Example 4.1.1 (two-state chain).** $P=\begin{bmatrix}1-\alpha&\alpha\\ \beta&1-\beta\end{bmatrix}$ (4.6). Balancing probability flow across the cut between the states gives
$$\mu_1\alpha=\mu_2\beta\tag{4.7}$$
With $\mu_1+\mu_2=1$:
$$\mu_1=\frac{\beta}{\alpha+\beta},\quad \mu_2=\frac{\alpha}{\alpha+\beta}\tag{4.8}$$
The state entropy is $H(X_n)=H\!\left(\frac{\beta}{\alpha+\beta},\frac{\alpha}{\alpha+\beta}\right)$ (4.9). This is *not* the growth rate of $H(X_1,\dots,X_n)$, because dependence "will take a steady toll" (p. 62).

### 4.2 Entropy rate (pp. 63–66)
**Definition.**
$$H(\mathscr X)=\lim_{n\to\infty}\frac1nH(X_1,\dots,X_n)\tag{4.10}$$
when the limit exists (p. 63).

Examples (p. 63):
1. Typewriter with $m$ equally likely letters: $H(X_1,\dots,X_n)=\log m^n$, so the rate is $\log m$ bits per symbol.
2. I.i.d.: the rate is $H(X_1)$ (4.11).
3. Independent, not identically distributed: $H(X_1,\dots,X_n)=\sum H(X_i)$ (4.12), but the limit of the average may not exist. Example: $p_i=0.5$ if $2k<\log\log i\le 2k+1$ and $p_i=0$ if $2k+1<\log\log i\le 2k+2$ (4.13). There are arbitrarily long stretches with $H(X_i)=1$, then exponentially longer ones with $H(X_i)=0$. The running average oscillates between 0 and 1, so $H(\mathscr X)$ is undefined.

A related quantity:
$$H'(\mathscr X)=\lim_{n\to\infty}H(X_n|X_{n-1},\dots,X_1)\tag{4.14}$$
The first is per-symbol entropy; the second is the entropy of the last symbol given the past (p. 64).

**Theorem 4.2.1.** For a stationary process both limits exist and $H(\mathscr X)=H'(\mathscr X)$ (4.15) (p. 64).

**Theorem 4.2.2.** For a stationary process, $H(X_n|X_{n-1},\dots,X_1)$ is decreasing in $n$ and has a limit $H'(\mathscr X)$.
Proof (p. 64):
$$H(X_{n+1}|X_1,\dots,X_n)\le H(X_{n+1}|X_n,\dots,X_2)\tag{4.16}$$
$$=H(X_n|X_{n-1},\dots,X_1)\tag{4.17}$$
The inequality holds because conditioning reduces entropy; the equality holds by stationarity. A decreasing sequence of non-negative numbers has a limit.

**Theorem 4.2.3 (Cesàro mean).** If $a_n\to a$ and $b_n=\frac1n\sum_{i=1}^na_i$, then $b_n\to a$ (p. 64).
Proof: pick $N(\epsilon)$ with $|a_n-a|\le\epsilon$ for $n\ge N(\epsilon)$. Then for $n\ge N(\epsilon)$ (pp. 64–65):
$$|b_n-a|=\Big|\frac1n\sum_{i=1}^n(a_i-a)\Big|\le\frac1n\sum_{i=1}^n|a_i-a|\tag{4.18–4.19}$$
$$\le\frac1n\sum_{i=1}^{N(\epsilon)}|a_i-a|+\frac{n-N(\epsilon)}{n}\epsilon\tag{4.20}$$
$$\le\frac1n\sum_{i=1}^{N(\epsilon)}|a_i-a|+\epsilon\tag{4.21}$$
The first term tends to 0, so $|b_n-a|\le2\epsilon$ for large $n$.

**Proof of Theorem 4.2.1** (p. 65). By the chain rule,
$$\frac{H(X_1,\dots,X_n)}{n}=\frac1n\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1)\tag{4.22}$$
This is the time average of conditional entropies, which tend to $H'(\mathscr X)$ by Thm 4.2.2. By Thm 4.2.3 the average has the same limit:
$$H(\mathscr X)=\lim\frac{H(X_1,\dots,X_n)}{n}=\lim H(X_n|X_{n-1},\dots,X_1)=H'(\mathscr X)\tag{4.23}$$

> *Intuition note.* Each new symbol adds a conditional entropy, and for a stationary process these additions can only shrink toward a limit. An average of numbers that settle down also settles to the same value, so the per-symbol entropy equals the "last symbol given the past" entropy.

**Significance (p. 65).** For a stationary ergodic process the author states (proof in §15.7, not given here) that
$$-\frac1n\log p(X_1,\dots,X_n)\to H(\mathscr X)\ \text{with probability 1}\tag{4.24}$$
So the Chapter 3 typical-set arguments carry over: about $2^{nH(\mathscr X)}$ typical sequences, each of probability about $2^{-nH(\mathscr X)}$, describable with about $nH(\mathscr X)$ bits.

**Markov chains (p. 66).** For a stationary Markov chain,
$$H(\mathscr X)=H'(\mathscr X)=\lim H(X_n|X_{n-1},\dots,X_1)=\lim H(X_n|X_{n-1})=H(X_2|X_1)\tag{4.25}$$
computed under the stationary distribution.

**Theorem 4.2.4.** With stationary distribution $\mu$ and transition matrix $P$:
$$H(\mathscr X)=-\sum_{ij}\mu_iP_{ij}\log P_{ij}\tag{4.26}$$
Proof: $H(X_2|X_1)=\sum_i\mu_i\big(\sum_j-P_{ij}\log P_{ij}\big)$.

**Example 4.2.1 (two-state chain).**
$$H(\mathscr X)=H(X_2|X_1)=\frac{\beta}{\alpha+\beta}H(\alpha)+\frac{\alpha}{\alpha+\beta}H(\beta)\tag{4.27}$$

**Remark (p. 66).** If the chain is irreducible and aperiodic, the rate is still given by (4.25)–(4.26) even when the initial distribution is not stationary.

> *Intuition note.* Once the chain is in stationary regime, the surprise at each step is just the uncertainty in the next state given the current one, averaged over how often each state occurs.

### 4.3 Random walk on a weighted graph (pp. 66–68)
Graph with nodes $\{1,\dots,m\}$, undirected edge weights $W_{ij}=W_{ji}\ge0$ ($W_{ij}=0$ if not connected). From node $i$ the walker picks $j$ with probability proportional to the edge weight: $P_{ij}=W_{ij}/\sum_kW_{ik}$ (p. 67).

Let $W_i=\sum_jW_{ij}$ (4.28) and $W=\sum_{i,j:j>i}W_{ij}$ (4.29), so $\sum_iW_i=2W$. Guess
$$\mu_i=\frac{W_i}{2W}\tag{4.30}$$
Verification of $\mu P=\mu$:
$$\sum_i\mu_iP_{ij}=\sum_i\frac{W_i}{2W}\frac{W_{ij}}{W_i}=\sum_i\frac1{2W}W_{ij}=\frac{W_j}{2W}=\mu_j\tag{4.31–4.34}$$
The distribution is *local*: it depends only on the total weight and the weights at the node.

Entropy rate: $H(\mathscr X)=H(X_2|X_1)$ (4.35). Steps (4.36)–(4.39) are unreadable in the supplied text layer, and no page image was supplied for p. 68. The result printed in (4.40) is
$$H(\mathscr X)=H\!\Big(\dots,\frac{W_{ij}}{2W},\dots\Big)-H\!\Big(\dots,\frac{W_i}{2W},\dots\Big)\tag{4.40}$$
*(added step, consistent with 4.26 and 4.30)*: $-\sum_{ij}\frac{W_{ij}}{2W}\log\frac{W_{ij}}{W_i}=-\sum_{ij}\frac{W_{ij}}{2W}\log\frac{W_{ij}}{2W}+\sum_{ij}\frac{W_{ij}}{2W}\log\frac{W_i}{2W}$, and $\sum_jW_{ij}=W_i$ turns the last sum into $-H(\dots,W_i/2W,\dots)$.

With equal weights, $E_i$ edges at node $i$, $E$ edges in total (p. 68):
$$H(\mathscr X)=\log(2E)-H\!\Big(\frac{E_1}{2E},\dots,\frac{E_m}{2E}\Big)\tag{4.41}$$
The author calls this "almost misleading": apparently the rate (the average transition entropy) depends only on the entropy of the stationary distribution and the total number of edges.

**Example 4.3.1 (king on 8×8 board).** The king has 8 moves in the interior, 5 at edges, 3 at corners. Stationary probabilities are proportional to 8, 5, 3 (the fractions are garbled in the text layer; with 420 = total degree, they are 8/420, 5/420, 3/420 — *added*). The rate is $0.92\log 8$; the factor 0.92 comes from edge effects, and an infinite board would give $\log 8$ (p. 68). A rook has rate $\log 14$ bits, since it always has 14 moves. The author asks whether a queen has more or less freedom than a rook plus bishop (p. 68).

**Remark (pp. 68–69).** A stationary random walk on a graph is time-reversible (4.42). The author states the converse: any time-reversible Markov chain is a random walk on an undirected weighted graph.

### 4.4 Hidden Markov models (pp. 69–71)
Let $X_1,X_2,\dots$ be a stationary Markov chain and $Y_i=\phi(X_i)$. The $Y$'s need not form a Markov chain, but they are stationary, so $H(\mathscr Y)$ is defined (p. 69). Computing $H(Y_n|Y_{n-1},\dots,Y_1)$ for growing $n$ gives no stopping rule, since convergence can be arbitrarily slow and small differences between successive values do not prove closeness (p. 69). So we want a lower bound that converges from below. The upper bound $H(Y_n|Y_{n-1},\dots,Y_1)\downarrow H(\mathscr Y)$ is already known. The trick is to also condition on $X_1$ (p. 69).

**Lemma 4.4.1.**
$$H(Y_n|Y_{n-1},\dots,Y_1,X_1)\le H(\mathscr Y)\tag{4.43}$$
Proof (pp. 69–70), for $k=1,2,\dots$. The text of (4.44)–(4.46) is garbled and no page image was supplied for p. 69. The author's chain of steps starts from $H(Y_n|Y_{n-1},\dots,Y_1,X_1)$, then adds $X_0,\dots,X_{-k}$ to the conditioning, then $Y_1,\dots,Y_{-k}$. It ends with
$$\le H(Y_n|Y_{n-1},\dots,Y_1,Y_0,\dots,Y_{-k})\tag{4.47}$$
$$=H(Y_{n+k+1}|Y_{n+k},\dots,Y_1)\tag{4.48}$$
Justifications given: (a) $Y_1$ is a function of $X_1$; (b) Markov property of $X$; (c) each $Y_i$ is a function of $X_i$; (d) conditioning reduces entropy; (e) stationarity (p. 70). Since this holds for all $k$,
$$H(Y_n|Y_{n-1},\dots,Y_1,X_1)\le\lim_kH(Y_{n+k+1}|Y_{n+k},\dots,Y_1)=H(\mathscr Y)\tag{4.49–4.50}$$

**Lemma 4.4.2.**
$$H(Y_n|Y_{n-1},\dots,Y_1)-H(Y_n|Y_{n-1},\dots,Y_1,X_1)\to0\tag{4.51}$$
Proof (pp. 70–71). The gap equals $I(X_1;Y_n|Y_{n-1},\dots,Y_1)$ (4.52). Since $I(X_1;Y_1,\dots,Y_n)\le H(X_1)$ (4.53), $\lim_nI(X_1;Y_1,\dots,Y_n)\le H(X_1)$ (4.54). By the chain rule,
$$\lim_nI(X_1;Y_1,\dots,Y_n)=\lim_n\sum_{i=1}^nI(X_1;Y_i|Y_{i-1},\dots,Y_1)=\sum_{i=1}^\infty I(X_1;Y_i|Y_{i-1},\dots,Y_1)\tag{4.55–4.56}$$
The infinite sum is finite with non-negative terms, so the terms tend to 0:
$$\lim I(X_1;Y_n|Y_{n-1},\dots,Y_1)=0\tag{4.57}$$

**Theorem 4.4.1.** If $X_1,\dots,X_n$ is a stationary Markov chain and $Y_i=\phi(X_i)$:
$$H(Y_n|Y_{n-1},\dots,Y_1,X_1)\le H(\mathscr Y)\le H(Y_n|Y_{n-1},\dots,Y_1)\tag{4.58}$$
and both bounds converge to $H(\mathscr Y)$ (4.59) (p. 71).

> *Intuition note.* Conditioning on the extra variable $X_1$ can only lower the uncertainty about $Y_n$, so this quantity sits below the upper bound; Lemma 4.4.1 shows it also stays below $H(\mathscr Y)$ itself. The extra help from $X_1$ fades as $n$ grows, so the two bounds squeeze together and tell you when to stop computing.

**Summary (p. 71).** Restates (4.60)–(4.65): the two rates, their equality for stationary processes, the Markov formula, and the bounds for functions of Markov chains.

## Toy example (ours)
Two-state chain with $\alpha=0.2$, $\beta=0.4$, started stationary.
- $\mu_1=0.4/0.6=2/3$, $\mu_2=1/3$. Check (4.7): $\mu_1\alpha=0.1333=\mu_2\beta$.
- $H(0.2)=0.2(2.3219)+0.8(0.3219)=0.7219$; $H(0.4)=0.4(1.3219)+0.6(0.7370)=0.9710$.
- (4.27): $H(\mathscr X)=\tfrac23(0.7219)+\tfrac13(0.9710)=0.4813+0.3237=0.8050$ bits.
- State entropy: $H(2/3,1/3)=\tfrac23(0.5850)+\tfrac13(1.5850)=0.9183$, larger than the rate.
- Per-symbol entropies, using the chain rule $H(X_1,\dots,X_n)=0.9183+(n-1)(0.8050)$: $n=2$: $1.7233/2=0.8617$; $n=3$: $2.5282/3=0.8427$. They decrease toward 0.8050, in line with Ex. 4(a).

## Concepts
- [[entropy-rate]] — $\lim\frac1nH(X_1,\dots,X_n)$, entropy growth per symbol, for a process with memory (p. 63)
- [[stationary-process]] (new) — joint law invariant under time shifts (p. 60)
- [[markov-chain]] (new) — next symbol depends on the past only through the current symbol (p. 61)
- [[stationary-distribution]] (new) — state distribution unchanged by one step; with it as initial law the chain is stationary (p. 61)
- [[joint-and-conditional-entropy]] — $H(X_n|X_{n-1},\dots,X_1)$ decreases to $H'(\mathscr X)$ (p. 64)
- [[typical-set-aep]] — for stationary ergodic processes $-\frac1n\log p\to H(\mathscr X)$ a.s.; about $2^{nH}$ typical sequences (p. 65)
- [[cesaro-mean]] (new) — running average of a convergent sequence has the same limit (p. 64)
- [[random-walk-on-graph]] (new) — Markov chain moving to neighbours in proportion to edge weight; $\mu_i=W_i/2W$ (p. 67)
- [[hidden-markov-model]] (new) — here, $Y_i=\phi(X_i)$ for a Markov chain $X$; bounded entropy rate (p. 69)
- [[mutual-information]] — used to show the bound gap equals $I(X_1;Y_n|Y_{n-1},\dots,Y_1)$ (p. 70)

## Canonical instances
- [[typewriter-source]] — $m$ equally likely letters, rate $\log m$ (p. 63)
- [[non-converging-entropy-average]] — independent source with $p_i$ from (4.13); no entropy rate (p. 63)
- [[two-state-markov-chain]] — rate $\frac{\beta}{\alpha+\beta}H(\alpha)+\frac{\alpha}{\alpha+\beta}H(\beta)$ (p. 66)
- [[king-on-chessboard]] — rate $0.92\log8$ (p. 68)

## Bridges (candidates)
- [same-math] Cesàro mean in Thm 4.2.3 ↔ analysis: averaging a convergent sequence — the identical lemma.
- [same-math] $-\sum\mu_iP_{ij}\log P_{ij}$ ↔ conditional entropy $H(X_2|X_1)$ under the stationary law — literally the same quantity.
- [structural-analogy] Hidden Markov entropy bounds ↔ estimation with a latent state: observing the hidden state sandwiches the true rate.

## Questions this raises
- When the chain is not irreducible or not aperiodic, is the entropy rate still given by (4.26), and which stationary distribution applies?
- How fast does $H(Y_n|Y_{n-1},\dots,Y_1)-H(Y_n|Y_{n-1},\dots,Y_1,X_1)$ shrink for a given $\phi$ and $P$?
- What does "ergodic" add beyond stationarity for the almost-sure AEP (4.24)?
- Why does the rate of the weighted-graph walk depend on the graph only through $W_{ij}$ and $W_i$ (4.40)?

## Exercises worth doing
- Ex. 1 (p. 72) — doubly stochastic matrices: mixing raises entropy; uniform stationary distribution iff doubly stochastic — medium
- Ex. 2 (p. 72) — "time's arrow": conditional entropy given the past equals that given the future for stationary processes — medium
- Ex. 4 (p. 74) — per-symbol entropy is non-increasing in $n$ and at least $H(X_n|X_{n-1},\dots,X_1)$ — easy
- Ex. 5 (pp. 74–75) — rates of two-state chains and counting allowed sequences — medium
- Ex. 13 (pp. 76–77) — constrained sequences: log of largest eigenvalue equals maximum Markov entropy rate — hard
- Ex. 14 (p. 77) — waiting time to next occurrence: $EN=m$ and $E\log N\le H(X)$ — medium

## Reading notes
- The PDF is the 1991 first edition (header of the chapter-opening page, p. 60: "Copyright © 1991 John Wiley & Sons, Inc.", Print ISBN 0-471-06259-6), not the 2006 second edition cited in the metadata. The unit's source notes warn that content and numbering may differ from the 2nd edition; this cannot be checked from these pages.
- Printed page = pdf − 22 (pdf 82 = p. 60).
- Page images for pdf 90 (p. 68) and pdf 91 (p. 69) were not supplied. Equations (4.36)–(4.39) and (4.44)–(4.46) are garbled in the text layer and are not reconstructed, apart from the marked added step. The text layer for p. 68 also garbles the king's stationary probabilities.
- The text layer labels two lines "(4.46)" (both on p. 69); this is a numbering duplication in the extraction.
- In the problems, some OCR in the text layer is garbled (e.g. Ex. 6, where the text layer reads "H(X)IEZ," for the printed $H(X)/El_X$); the images were checked where supplied.
