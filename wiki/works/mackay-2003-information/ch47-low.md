---
id: mackay-2003-information/ch47-low
work: mackay-2003-information
unit: "47 Low-Density Parity-Check Codes"
pages: 557-573
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Low-Density Parity-Check Codes

## L0 — One line
A block code whose parity-check matrix is sparse can be decoded well by passing probability messages along its graph (the sum–product algorithm), even though decoding LDPC codes is NP-complete.

## L1 — The gist (≤ 120 words)
Low-density parity-check (Gallager) codes are good codes under an optimal decoder, but decoding them is NP-complete. MacKay therefore presents the sum–product (belief-propagation) algorithm. It runs on the code's bipartite graph as if the graph had no cycles, and it stops as soon as all parity checks are satisfied. He then gives pictorial demonstrations and the cost of decoding. He explains density evolution, which predicts a noise threshold. He describes three ways to improve the codes: larger alphabets GF(q), irregular graphs, and algebraic redundancy. He also gives fast encoding methods. Optimized codes come very close to the Shannon limit.

**Prerequisites:** mod-2 arithmetic; parity-check matrix and syndrome of a linear code; bipartite graphs; conditional probability; binary symmetric and Gaussian channels. Terms used early: weight = number of 1s in a row or column; GF($q$) = finite field with $q$ elements; Shannon limit = the benchmark noise or signal-to-noise level for reliable communication; NP-complete = a class of computationally hard problems.

## L2 — Key ideas
- An LDPC code has a sparse $\mathbf H$. A regular code has column weight $j$ and row weight $k$, and is built at random under those constraints (p. 557).
- With an optimal decoder LDPC codes are good and have good distance, for any $j\ge 3$. No optimal decoder is available and decoding LDPC codes is NP-complete, so practical decoding uses message passing (p. 557).
- Codeword decoding and syndrome decoding are two views of one generic problem, "maximize $P(\mathbf x)\,\mathbb 1[\mathbf H\mathbf x=\mathbf z]$". The sum–product algorithm gives equivalent results in both (unless numerical errors intervene). MacKay tends to use the syndrome view because no encoder is needed to simulate decoding realistically (p. 559).
- Sum–product alternates a horizontal (check) step and a vertical (bit) step. It halts when the tentative decoding satisfies all checks. This separates detected from undetected errors (pp. 560–562).
- Density evolution (a Monte Carlo simulation of an infinite tree) finds a noise threshold. For regular $(j,k)=(4,8)$ it is about $f=0.075$ (pp. 566–567).
- Performance improves with larger blocklength. For regular codes of blocklength 816, $j=3$ was the best of the values shown, down to block error $10^{-5}$. Gains also come from GF($q$) codes, irregular degrees (about 0.4 dB for binary codes; a code that is both irregular and over GF(8) gains about 0.9 dB over regular binary) and redundant algebraic constraints (pp. 565–569).
- Encoding by Gaussian elimination costs order $M^3$ for setup and order $M^2$ per block. Certain staircase-structured codes encode in linear time. The Richardson–Urbanke method costs $N+g^2$ (pp. 569–571).

## L3 — Walkthrough

### Definitions (intro)
A low-density parity-check (LDPC, or Gallager) code is a block code whose parity-check matrix $\mathbf H$ has sparse rows and columns (p. 557). In a regular Gallager code every column has weight $j$ and every row has weight $k$. Such codes are constructed at random under those constraints (p. 557). Figure 47.1 shows $j=3$, $k=4$, $N=16$, $M=12$, rate 1/4. Each bit is a circle, each parity constraint a square, and each constraint forces the $k=4$ connected bits to have even sum (p. 557).

### 47.1 Theoretical properties
Gallager (1963) and MacKay (1999b) prove these results (p. 557):
- LDPC codes are good codes given an optimal decoder, and they have good distance. Both hold for any $j\ge3$.
- There are sequences of codes in which $j$ grows with $N$ with $j/N\to0$ that are *very good* and have very good distance.
- However, we do not have an optimal decoder, and decoding LDPC codes is NP-complete.

### 47.2 Practical decoding
The task is to find the codeword $\mathbf t$ maximizing $P(\mathbf r\mid\mathbf t)$. All effective strategies are message-passing algorithms. The best known is the sum–product algorithm, also called iterative probabilistic decoding or belief propagation (p. 557). The channel is assumed memoryless. Complex channels can be handled on a more complex graph (p. 557). Both approaches lead to the generic problem: maximize
$$P^*(\mathbf x)=P(\mathbf x)\,\mathbb 1[\mathbf H\mathbf x=\mathbf z]\tag{47.1}$$
where $P(\mathbf x)$ is a separable distribution on a binary vector and $\mathbf z$ is a binary vector (p. 557).

**Codeword decoding viewpoint (p. 558).** The prior over codewords is
$$P(\mathbf t)\propto\mathbb 1[\mathbf H\mathbf t=\mathbf 0 \bmod 2]\tag{47.2}$$
$$P(\mathbf t)\propto\prod_m \mathbb 1\Big[\sum_{n\in\mathcal N(m)}t_n=0\bmod 2\Big]\tag{47.3}$$
Multiplying by the likelihood adds $N$ factors, one per received bit:
$$P(\mathbf t\mid\mathbf r)\propto P(\mathbf t)P(\mathbf r\mid\mathbf t)\propto\prod_m\mathbb 1\Big[\sum_{n\in\mathcal N(m)}t_n=0\Big]\prod_n P(r_n\mid t_n)\tag{47.4}$$
Figure 47.2b shows this graph: the prior graph plus likelihood "dongles". Here $r_n$ can live in any alphabet, because only the values $P(r_n\mid t_n)$ matter (p. 558).

**Syndrome decoding viewpoint (pp. 558–559).** Treat the channel output as a binary $\mathbf r$ plus a noise vector $\mathbf n$ with distribution $P(\mathbf n)$. For a binary symmetric channel (BSC), $\mathbf r=\mathbf t+\mathbf n$, $\mathbf z=\mathbf H\mathbf r$, and $P(n_n=1)=f$. For other channels, such as the Gaussian channel, one may define $\mathbf r$ as one wishes and obtain an effective binary noise model $P(\mathbf n)$ (pp. 558–559). Since $\mathbf H\mathbf t=\mathbf 0$, $\mathbf z=\mathbf H\mathbf n$ (p. 559). The joint probability is
$$P(\mathbf n,\mathbf z)=P(\mathbf n)\,\mathbb 1[\mathbf z=\mathbf H\mathbf n]=\prod_n P(n_n)\prod_m\mathbb 1\Big[z_m=\sum_{n\in\mathcal N(m)}n_n\Big]\tag{47.5}$$
It can also be drawn as a belief network, with each bit the parent of $j$ checks and each check the child of $k$ bits (p. 559).

**Unification.** In the codeword view $\mathbf x=\mathbf t$ and $\mathbf z=\mathbf 0$. In the syndrome view $\mathbf x=\mathbf n$ and $\mathbf z$ is the syndrome (p. 559). Both lead to
$$P^*(\mathbf x)=P(\mathbf x)\,\mathbb 1[\mathbf H\mathbf x=\mathbf z]\tag{47.6}$$
The two sum–product algorithms are isomorphic and give equivalent outcomes unless numerical errors intervene. MacKay uses the syndrome view because one need not implement an encoder to simulate decoding realistically (p. 559).

*Intuition note.* Decoding is the same puzzle in both views: find a bit pattern that satisfies the parity checks and is most probable. Working with the noise pattern lets you test a decoder without ever building an encoder.

### 47.3 Decoding with the sum–product algorithm
**Aim.** Compute the marginal posteriors $P(x_n=1\mid\mathbf z,\mathbf H)$. This is hard to do exactly because the graph has many cycles. MacKay runs the algorithm appropriate for a cycle-free graph anyway, hoping the errors introduced are small (p. 559). The artificial intelligence literature has used this approach, but it is now frowned upon because it gives inaccurate probabilities. For a good code the aim is the correct codeword, not accurate marginals. The posterior of a good code at an achievable rate is expected to be hugely concentrated on the most probable decoding, a distinctive case to which experience from other fields may not apply (p. 559).

**Graph and notation (p. 560).** The graph is bipartite: bits connect only to checks. Define $\mathcal N(m)=\{n:H_{mn}=1\}$ (bits in check $m$) and $\mathcal M(n)=\{m:H_{mn}=1\}$ (checks containing bit $n$). $\mathcal N(m)\backslash n$ excludes bit $n$. Each edge carries two quantities:
- $q^x_{mn}$: the probability that bit $n$ has value $x$, given the information from checks other than $m$.
- $r^x_{mn}$: the probability that check $m$ is satisfied if bit $n$ is fixed at $x$ and the other bits have the separable distribution $\{q_{mn'}:n'\in\mathcal N(m)\backslash n\}$.

If the graph had no cycles, the algorithm would give the exact posterior probabilities of all bits after a fixed number of iterations (p. 560).

**Initialization.** $p^0_n=P(x_n=0)$ and $p^1_n=1-p^0_n$. For a BSC in the syndrome view, $p^1_n=f$. For a channel with varying noise (e.g. a binary-input Gaussian channel with real output), $p^1_n$ is the appropriate normalized likelihood. For every $(n,m)$ with $H_{mn}=1$, set $q^0_{mn}=p^0_n$ and $q^1_{mn}=p^1_n$ (p. 560).

**Horizontal step (p. 560).** For each check $m$ and each $n\in\mathcal N(m)$:
$$r^0_{mn}=\sum_{\{x_{n'}:n'\in\mathcal N(m)\backslash n\}}P\big(z_m\mid x_n=0,\{x_{n'}\}\big)\prod_{n'\in\mathcal N(m)\backslash n}q^{x_{n'}}_{mn'}\tag{47.7}$$
$$r^1_{mn}=\sum_{\{x_{n'}:n'\in\mathcal N(m)\backslash n\}}P\big(z_m\mid x_n=1,\{x_{n'}\}\big)\prod_{n'\in\mathcal N(m)\backslash n}q^{x_{n'}}_{mn'}\tag{47.8}$$
The conditional probabilities are 0 or 1, depending on whether the hypothesized values match the observed $z_m$ (p. 560). For large $|\mathcal N(m)|$, regard $z_m+x_n$ as the final state of a two-state Markov chain started in state 0, with transitions for each added $x_{n'}$. Then use the forward–backward algorithm (section 25.3) (p. 560).

A convenient implementation uses differences $\delta q_{mn}\equiv q^0_{mn}-q^1_{mn}$ and $\delta r_{mn}\equiv r^0_{mn}-r^1_{mn}$ with
$$\delta r_{mn}=(-1)^{z_m}\prod_{n'\in\mathcal N(m)\backslash n}\delta q_{mn'}\tag{47.9}$$
Derivation by iteration (p. 561). If $\zeta=x_\mu+x_\nu \bmod 2$ with $P(x_\mu=0)=q^0_\mu$, etc., then $P(\zeta=1)=q^1_\mu q^0_\nu+q^0_\mu q^1_\nu$ and $P(\zeta=0)=q^0_\mu q^0_\nu+q^1_\mu q^1_\nu$. Hence $P(\zeta=0)-P(\zeta=1)=(q^0_\mu-q^1_\mu)(q^0_\nu-q^1_\nu)$. Then
$$r^0_{mn}=\tfrac12(1+\delta r_{mn}),\qquad r^1_{mn}=\tfrac12(1-\delta r_{mn})\tag{47.10}$$
The change to differences and back may be viewed as a Fourier transform and its inverse (p. 561).

*Intuition note.* A check is satisfied when the number of 1s among its bits has the right parity. The difference "P(even) − P(odd)" of a sum of independent bits is simply the product of the individual differences. So the messy sum over many bit patterns becomes one product.

**Vertical step (p. 561).** For each $n$:
$$q^0_{mn}=\alpha_{mn}\,p^0_n\prod_{m'\in\mathcal M(n)\backslash m}r^0_{m'n}\tag{47.11}$$
$$q^1_{mn}=\alpha_{mn}\,p^1_n\prod_{m'\in\mathcal M(n)\backslash m}r^1_{m'n}\tag{47.12}$$
Here $\alpha_{mn}$ makes $q^0_{mn}+q^1_{mn}=1$. The products can be computed by a downward and an upward pass. The "pseudoposterior" probabilities use all checks:
$$q^0_n=\alpha_n\,p^0_n\prod_{m\in\mathcal M(n)}r^0_{mn}\tag{47.13}$$
$$q^1_n=\alpha_n\,p^1_n\prod_{m\in\mathcal M(n)}r^1_{mn}\tag{47.14}$$
These give a tentative decoding $\hat{\mathbf x}$. Halt if $\mathbf H\hat{\mathbf x}=\mathbf z$. Otherwise repeat from the horizontal step (p. 561).

**Stop-when-it's-done method (pp. 561–562).** Set $\hat x_n=1$ if $q^1_n>0.5$ and test whether all checks $\mathbf H\hat{\mathbf x}=\mathbf z \bmod 2$ hold. Halt when they do. Declare failure if a maximum number of iterations (e.g. 200 or 1000) passes without success. On failure, $\hat{\mathbf x}$ may still be reported but the block is flagged as failed (p. 561). MacKay contrasts this with turbo-code practice of running a fixed number of iterations, which he calls wasteful and which blurs the distinction between undetected and detected errors. An *undetected* error is a valid $\hat{\mathbf x}\neq$ the true $\mathbf x$. A *detected* error is a run that hits the iteration limit. Undetected errors reveal distance properties of the code, and flagging bad blocks seems preferable in practice (pp. 561–562).

**Cost (p. 562).** Brute-force creation of the generator matrix scales as $N^3$, and encoding as $N^2$. Encoding uses only binary arithmetic, so for these block lengths it is much cheaper than simulating the Gaussian channel. Decoding takes about $6Nj$ floating-point multiplies per iteration. With 20 iterations, the cost per decoded bit is about "$120t/R$" (as printed), independent of blocklength, about 800 operations for the codes in the next section. Encoding can be cheaper with tricks of Richardson and Urbanke (2001b) or specially constructed $\mathbf H$ (MacKay et al., 1999). Decoding can use low-precision messages with small loss (Richardson and Urbanke, 2001a) (p. 562).

### 47.4 Pictorial demonstration of Gallager codes
**Encoding (pp. 562–563).** The rate-1/2 code uses a $10\,000\times20\,000$ matrix $\mathbf H$ with three 1s per column and 6 per row (figure 47.4). A transmission has 10 000 source bits and 10 000 parity bits. Changing the first source bit changes many parity bits, since each parity bit depends on about half of the source bits (figure 47.3). So the generator matrix is dense (p. 563). The source images are deliberately redundant, so the correction is visible. The decoder does not use source redundancy and works the same for any source vector (p. 563).

**Iterative decoding (pp. 563–564).** With BSC noise $f=7.5\%$ the decoder halts after 13 iterations with an error-free result (figure 47.5). For this code at $f=7.5\%$, failures happen about once in 100 000 transmissions. Figure 47.6 compares this error rate with block error rates of classical codes (repetition, Hamming (7,4), Reed–Muller, BCH) (p. 563).

**Gaussian channel (p. 565).** At $x/\sigma=1.185$ ($E_b/N_0=1.47$ dB) the rate-1/2 code communicates reliably, with error probability $\simeq10^{-5}$. Reducing to $x/\sigma=1.0$ corresponds to the Shannon limit for rate 1/2 (figure 47.7).

**Dependence on parameters (p. 565, figure 47.8).** Increasing blocklength $N$ improves performance, as Shannon would predict. With an optimal decoder, the codes closest to random codes (largest $j$) would be best. But the sum–product decoder makes poor progress in dense graphs, so small $j$ does best. Among the values shown, $j=3$ is best for $N=816$ down to block error $10^{-5}$. This motivates codes with some weight-2 columns (figure 47.9b has $M/2$). Too many weight-2 columns make a much poorer code. Even more irregular codes do better still (p. 566).

### 47.5 Density evolution
**Idea (p. 566).** Imagine decoding on an infinite loop-free tree with the same local topology (figure 47.11): every bit has $j$ checks and every check has $k$ bits. The larger $\mathbf H$ is, the closer its decoding should be to this infinite graph. After $i$ iterations a bit has gathered information from radius $i$. Successful decoding occurs only if the average entropy of a bit decreases to zero as iterations increase.

**Monte Carlo method (pp. 566–567).** Gallager (1963) first used it. Exact simulation of the tree would take time growing exponentially with the radius $I$. Instead, keep for each iteration a representative sample (size 100, say) of pairs $\{r,x\}$. For a regular code, build each new pair at iteration $i$ as follows:
- Draw a new $x$ from its distribution.
- Draw $(j-1)(k-1)$ pairs, at random with replacement, from the list at iteration $i-1$.
- Assemble them into a tree fragment (figure 47.12) and run sum–product from top to bottom to get the new $r$.

**Results.** For $j=4$, $k=8$ with 10 000 samples per iteration (figure 47.10), low noise gives a collapse to zero entropy after few iterations. High noise leaves non-zero entropy, meaning decoding failure. The boundary is the *threshold* of the decoding algorithm for the BSC. Simulation gives about 0.075 for $(4,8)$. Richardson and Urbanke (2001a) derived thresholds analytically (p. 567):

| $(j,k)$ | $f_{\max}$ |
|---|---|
| (3,6) | 0.084 |
| (4,8) | 0.076 |
| (5,10) | 0.068 |

The Shannon limit for rate-1/2 codes is $f_{\max}=0.11$ (table 47.13). **Approximate density evolution** uses Gaussian approximations to the message distributions and updates only their parameters. This gives EXIT charts (p. 567).

*Intuition note.* In a large random sparse graph, the neighbourhood of a bit looks like a tree. So one can study the average behaviour on a tree and ask whether uncertainty shrinks to zero. The noise level at which it stops shrinking is the threshold.

### 47.6 Improving Gallager codes
**Clump bits and checks (pp. 567–568).** Group bits into metavariables (say 3 bits) and checks into metachecks. One way to wire them is to define $\mathbf H$ over a finite field GF($q$) (GF(4), GF(8)) and translate binary messages into GF($q$) (tables 47.14, 47.15). Table 47.15 turns an $M\times N$ GF(4) matrix into a $2M\times2N$ binary matrix. Messages then are probabilities over conjunctions of binary variables; for 3-bit clumps they cover the 8 states (p. 567). Optimized GF(4), GF(8) and GF(16) codes perform nearly 1 dB better than comparable binary Gallager codes (pp. 567–568).

Decoding cost in GF($q$) scales as $q\log q$ if a Fourier transform is used in the check nodes. The check-to-variable update
$$r^a_{mn}=\sum_{\mathbf x:x_n=a}\mathbb 1\Big[\sum_{n'\in\mathcal N(m)}H_{mn'}x_{n'}=z_m\Big]\prod_{j\in\mathcal N(m)\backslash n}q^{x_j}_{mj}\tag{47.15}$$
is a convolution of the $q^a_{mj}$. So the sum can be replaced by a product of Fourier transforms of $q^a_{mj}$ over $j\in\mathcal N(m)\backslash n$, followed by an inverse transform (p. 568). Over GF(2), $F^0=f^0+f^1$, $F^1=f^0-f^1$. Algorithm 47.16 gives GF(4):
$$F^0=[f^0+f^1]+[f^A+f^B],\quad F^1=[f^0-f^1]+[f^A-f^B],$$
$$F^A=[f^0+f^1]-[f^A+f^B],\quad F^B=[f^0-f^1]-[f^A-f^B]$$
Transforms over GF($2^k$) are a sequence of binary transforms in $k$ dimensions. The inverse is identical except for division by $2^k$ (p. 568).

**Make the graph irregular (p. 568).** Introduced by Luby et al. (2001b): variable nodes get different degrees (some 2, some 3, some 4, a few 20). Check nodes can also have unequal degrees, which helps on erasure channels, but for the Gaussian channel the best graphs have regular check degrees. For rate 1/4 (figure 47.17) irregular binary codes gain about 0.4 dB. Switching from GF(2) to GF(16) gains about 0.6 dB. Davey's irregular code over GF(8) gains about 0.9 dB over the regular binary Gallager code (pp. 568–569). Profile-optimization methods (Richardson et al., 2001) give codes within a hair's breadth of the Shannon limit under sum–product decoding (p. 569).

**Algebraic constructions (p. 569).** Regular codes can also be improved by redundant sparse constraints. A difference-set cyclic code has $N=273$, $K=191$ but satisfies $N=273$ low-weight constraints rather than $M=82$. Random Gallager codes cannot come near this redundancy. The difference-set cyclic code performs about 0.7 dB better than an equivalent random Gallager code (figure 47.18; the comparison code had $(j,k)=(4,13)$). The *Tanner challenge* is the open problem of finding codes with these properties at other blocklengths and rates.

### 47.7 Fast encoding
The standard method finds $\mathbf G$ by Gaussian elimination (order $M^3$) and encodes each block at order $M^2$ (p. 569).

**Staircase codes (pp. 569–570).** If $\mathbf H=[\mathbf H_s|\mathbf H_p]$ has a staircase structure on the right (eq. 47.16), the source $\mathbf s$ occupies the first $K$ bits, and the $M$ parity bits follow in linear time:
$$p_1=\sum_{n=1}^K H_{1n}s_n,\quad p_m=p_{m-1}+\sum_{n=1}^K H_{mn}s_n\ (m=2,\dots,M)\tag{47.17}$$
Equivalently, compute $\mathbf v=\mathbf H_s\mathbf s$ and pass $\mathbf v$ through an accumulator. The cost is linear if the sparsity of $\mathbf H$ is exploited (p. 570).

**General codes: Richardson–Urbanke (pp. 570–571).** Cost is reduced from $M^2$ to $N+g^2$, where the gap $g$ is hopefully a small constant and in the worst cases a small fraction of $N$. Rearrange $\mathbf H$ by row and column interchanges into approximate lower-triangular form (figure 47.19):
$$\mathbf H=\begin{bmatrix}\mathbf A&\mathbf B&\mathbf T\\\mathbf C&\mathbf D&\mathbf E\end{bmatrix}\tag{47.18}$$
**Shapes (added, inferred):** $\mathbf H$ is $M\times N$. The last $g$ rows hold $\mathbf C,\mathbf D,\mathbf E$. $\mathbf B$ and $\mathbf D$ have $g$ columns. $\mathbf T$ is square, lower triangular with 1s on the diagonal. The six blocks are very sparse. The source has $K=N-M$ bits, and $\mathbf t=[\mathbf s,\mathbf p_1,\mathbf p_2]$ with $\mathbf p_1$ of length $g$.

1. Upper syndrome $\mathbf z_A=\mathbf A\mathbf s$ (47.19), linear time.
2. Tentative second parity bits making the upper syndrome zero: $\mathbf p_2^A=-\mathbf T^{-1}\mathbf z_A$ (47.20), by back-substitution in linear time.
3. Lower syndrome of $[\mathbf s,\mathbf 0,\mathbf p_2^A]$: $\mathbf z_B=\mathbf C\mathbf s-\mathbf E\mathbf p_2^A$ (47.21), linear time.
4. Define $\mathbf F\equiv-\mathbf E\mathbf T^{-1}\mathbf B+\mathbf D$ (47.22) and invert it once, at cost of order $g^3$. $\mathbf F^{-1}$ is a dense $g\times g$ matrix. If $\mathbf F$ is not invertible, either $\mathbf H$ is not of full rank or further column permutations can give an invertible $\mathbf F$. Set $\mathbf p_1=-\mathbf F^{-1}\mathbf z_B$ (47.23), cost of order $g^2$. The text claims this is the correct setting of the first parity bits, and gives no proof. *(added step, mod 2 where $-1=+1$):* $\mathbf H[\mathbf s;\mathbf p_1;\mathbf p_2]=\mathbf 0$ needs $\mathbf p_2=\mathbf T^{-1}(\mathbf A\mathbf s+\mathbf B\mathbf p_1)$. Substituting into the lower rows gives $\mathbf F\mathbf p_1=\mathbf C\mathbf s+\mathbf E\mathbf T^{-1}\mathbf A\mathbf s=\mathbf z_B$.
5. Discard $\mathbf p_2^A$. New upper syndrome $\mathbf z_C=\mathbf z_A+\mathbf B\mathbf p_1$ (47.24), linear time.
6. $\mathbf p_2=-\mathbf T^{-1}\mathbf z_C$ (47.25), by back-substitution in linear time.

*Intuition note.* Most of the encoding is cheap triangular solving. Only a $g\times g$ dense system, with $g$ hopefully small, (the "gap") needs real work, so the cost is about $N$ plus a term in $g^2$.

### 47.8 Further reading (pp. 571–572)
Gallager studied LDPC codes in 1962, and the coding community then largely forgot them. Tanner (1981) generalized them with more general constraint nodes, and MacKay argues that "turbo product codes" should be called Tanner product codes. MacKay and Davey (2000) showed LDPC codes can outperform Reed–Solomon codes at high rate and short blocklength. LDPC codes are now being adopted for applications from hard drives to satellite communications. The section also lists many further references.

### 47.9–47.10 Exercises and solution
Exercise 47.1 asks for the log-ratio form of the algorithm, with $l_{mn}\equiv\ln(q^0_{mn}/q^1_{mn})$ (47.26) and $\delta q_{mn}=\tanh(l_{mn}/2)$ (47.27) (p. 572). The printed solution to Exercise 47.2 concludes that not every random linear code can be expressed as a low-density parity-check code. The argument counts distinct codes and uses the pigeon-hole principle (p. 573).

## Toy example (ours, not from the text)
Syndrome view, one check on 3 bits, with the observed syndrome $z=1$ and $P(x_n=1)=f=0.1$, so $p^0=0.9$, $p^1=0.1$ for each bit. This graph has no cycles, so the algorithm is exact.

- Initialization: $q^0_{mn}=0.9$, $q^1_{mn}=0.1$, so $\delta q=0.8$ for each bit.
- Horizontal step for bit 1: $\delta r=(-1)^1\cdot(0.8)(0.8)=-0.64$. By (47.10), $r^0=\tfrac12(1-0.64)=0.18$ and $r^1=\tfrac12(1+0.64)=0.82$.
- Direct check: $r^0=P(x_2+x_3=1)=2(0.9)(0.1)=0.18$ and $r^1=P(x_2+x_3=0)=0.81+0.01=0.82$. ✓.
- Pseudoposterior (bit 1 has one check): $q^0\propto0.9\times0.18=0.162$ and $q^1\propto0.1\times0.82=0.082$. The sum is $0.244$, so $q^1=0.082/0.244\approx0.336$.
- Direct check: $P(z=1)=3(0.1)(0.81)+0.001=0.244$, so $P(x_1=1\mid z=1)=0.082/0.244$. ✓.

By symmetry all three bits get $q^1\approx0.336<0.5$, so $\hat{\mathbf x}=000$ and $\mathbf H\hat{\mathbf x}=0\ne z=1$. The decoder cannot halt, and the block is flagged as a *detected* failure. One check cannot say which bit flipped. The many overlapping checks of a real LDPC code are what resolve this.

## Concepts
- [[ldpc-code]] (new) — block code with sparse parity-check matrix $\mathbf H$; regular if every column has weight $j$ and every row weight $k$ (p. 557)
- [[error-correcting-code]] — structured redundancy letting errors be corrected; here, a linear block code given by parity checks (p. 557)
- [[noisy-channel]] — memoryless channel $P(r_n\mid t_n)$ assumed for decoding (p. 557)
- [[channel-capacity]] — "Shannon limit" used as the benchmark for noise level and signal-to-noise ratio (pp. 565, 567)
- [[factor-graph]] (new) — graph of variable and check/factor nodes for $P(\mathbf t)$, $P(\mathbf t\mid\mathbf r)$ or $P(\mathbf n,\mathbf z)$ (p. 558)
- [[syndrome-decoding]] (new) — decode by inferring the noise $\mathbf n$ from the syndrome $\mathbf z=\mathbf H\mathbf r$ (p. 558)
- [[sum-product-algorithm]] (new) — message passing of $q$ and $r$ on the bipartite graph, equal to belief propagation; exact if the graph has no cycles (p. 560)
- [[posterior-distribution]] — marginals $P(x_n=1\mid\mathbf z,\mathbf H)$, approximated by the pseudoposterior $q_n$ (pp. 559, 561)
- [[density-evolution]] (new) — track average bit entropy on an infinite tree by Monte Carlo, to find the threshold (p. 566)
- [[decoding-threshold]] (new) — boundary between noise levels where the decoding algorithm succeeds and where it fails, for the binary symmetric channel (p. 567)
- [[irregular-ldpc-code]] (new) — LDPC code whose nodes have unequal degrees (p. 568)
- [[gf-q-ldpc-code]] (new) — LDPC code over a finite field GF($q$), decoded with a Fourier transform at cost $q\log q$ (pp. 567–568)
- [[fast-ldpc-encoding]] (new) — staircase and Richardson–Urbanke encoding with cost about $N+g^2$ (pp. 569–571)

## Canonical instances
- [[ldpc-rate-half-image-demo]] (new) — 10 000×20 000 code decoding a noisy image at $f=7.5\%$ in 13 iterations (p. 564)
- [[ldpc-threshold-table]] (new) — thresholds $f_{\max}$ 0.084, 0.076, 0.068 for $(3,6),(4,8),(5,10)$ (p. 567)
- [[difference-set-cyclic-273]] (new) — $N=273$, $K=191$ code with 273 sparse constraints, about 0.7 dB better than a random Gallager code (p. 569)
- [[ldpc-vs-turbo-rate-quarter]] (new) — comparison of rate-1/4 codes, Shannon limit about −0.79 dB (p. 568)

## Bridges (candidates)
- [same-math] Sum–product decoding ↔ bayesian: belief propagation on a factor graph, computing marginal posteriors exactly on trees — the text itself gives the name belief propagation (p. 557).
- [same-math] Check update (47.15) as a convolution computed by Fourier transform ↔ signal processing: convolution theorem; the GF(2) transform is $f^0\pm f^1$.
- [structural-analogy] Density evolution with resampled message populations ↔ bayesian: Monte Carlo integration, approximating a distribution by a sample.
- [metaphor] Decoding threshold ↔ physics: a sharp change of behaviour at a critical noise level (not stated in the unit).

## Questions this raises
- Why does ignoring cycles work for good codes, even though it gives inaccurate marginals?
- How do the code profile (degree distribution) and the threshold relate, and how is the profile optimized?
- Can codes with the properties of difference-set cyclic codes be found at other lengths and rates (the Tanner challenge)?
- Why does the best $j$ for sum–product decoding differ from the best $j$ under optimal decoding?

## Exercises worth doing
- Ex. 47.1 (p. 572) — derive the tanh form of sum–product and the $\{r\}$, $\{l\}$ update rules — difficulty: medium
- Ex. 47.2 (p. 572) — why a random linear code has no sparse $\mathbf H$ (solution printed on p. 573) — difficulty: medium
- Ex. 47.3 (p. 572) — more than $M$ weight-2 columns force low-weight codewords of order $\log M$ — difficulty: hard
- Ex. 47.4 (p. 572) — typical, not mean, weight enumerator of LDPC ensembles — difficulty: hard

## Reading notes
- Printed page = pdf − 12 (pdf 569 = printed 557).
- Page 562 prints the decoding cost as "120t/R". $t$ is not defined in this unit, and from $6Nj\times20$ iterations $/K$ it is probably $j$ (added inference).
- The text calls the $(4,8)$ threshold "about 0.075" (simulation, p. 567) and Table 47.13 gives 0.076 from analysis. The two values differ slightly.
- Figure 47.17's caption cites Luby et al. (1998) for a code, while the text on p. 568 credits Luby et al. (2001b) for irregular graphs.
- The label for $\mathbf T$ and $M$ in figure 47.19 is ambiguous, so the block shapes in 47.7 are inferred.
- p. 571 has a typo, "codes codes". The claim after step 4 of the encoder is not proved in the source.
- The figures (matrices, images, curves) are only described here. Of the exercises, only the solution to 47.2 (p. 573) appears in these pages; it is summarised, not reproduced.
