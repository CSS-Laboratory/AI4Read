---
id: mackay-2003-information/ch10-noisy
work: mackay-2003-information
unit: "10 The Noisy-Channel Coding Theorem"
pages: 161-175
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
# The Noisy-Channel Coding Theorem

## L0 — One line
Over any discrete memoryless channel (each output depends only on the current input), reliable communication is possible at every rate below the capacity $C=\max_{P_X} I(X;Y)$, and Shannon proves this by showing that a randomly chosen code is good on average, so a good code must exist.

## L1 — The gist (≤ 120 words)
Question: how fast can data be sent through a noisy channel with arbitrarily small error? Answer: at any rate below the capacity $C$. MacKay proves it by random coding, jointly-typical decoding, a union bound, and expurgation (throwing away bad codewords). If a small bit-error probability $p_b$ is accepted, rates up to $C/(1-H_2(p_b))$ are achievable, and higher rates are not (data processing inequality). The chapter also covers computing capacity, symmetric channels, error exponents that relate the error probability to the blocklength, and why random codes are impractical. It matters because it fixes the ultimate limit of reliable communication and shows that a noisy channel can be turned into an essentially noiseless binary channel of rate up to $C$.

**Prerequisites:** entropy, mutual information, typical sets and the source coding theorem (Ch. 4); binary symmetric channel (Ch. 9); data processing inequality; Lagrange multipliers; convex and concave functions.

## L2 — Key ideas
- The theorem has three parts: (1) rates $R<C$ are achievable with maximal block error (error probability of the worst message) $<\epsilon$; (2) with bit error $p_b$ allowed, rates up to $C/(1-H_2(p_b))$ are achievable; (3) higher rates are not (p. 162).
- A pair $(\mathbf x,\mathbf y)$ is jointly typical if $\mathbf x$, $\mathbf y$ and the pair are all typical. Two independent typical sequences are jointly typical with probability about $2^{-NI(X;Y)}$ (pp. 162–163).
- Shannon's method: average the error over all random codes. If the average is small, a good code exists, as when an average baby weight below 10 kg implies one light baby (p. 164).
- A union bound over the $2^{NR'}-1$ wrong codewords gives $\langle p_B\rangle\le\delta+2^{-N(I(X;Y)-R'-3\beta)}$, which can be made small by increasing $N$ if $R'<I(X;Y)-3\beta$ (p. 166).
- Expurgation (dropping the worst half of the codewords) turns a small average error into a small maximal error, at a negligible rate loss of $1/N$ (p. 167).
- Above capacity, a code used backwards gives a lossy compressor, which proves achievability up to $R=C/(1-H_2(p_b))$ (p. 168). The data processing inequality shows nothing beyond it is achievable (p. 168).
- Capacity needs the optimal input distribution. $I(X;Y)$ is concave in the input distribution, so a stationary point is a global maximum, but the constraint $p_i\ge0$ can be active (pp. 169–170).
- The theorem says nothing about how large $N$ must be. The exponents $E_r(R)$ and $E_{sp}(R)$ bound the error from above and below. Random codes cost exponentially much to encode and decode (pp. 171–172).

## L3 — Walkthrough

### About Chapter 10: notation (p. 161)
$Q$ is the channel. $\mathcal C$ is a random code of codeword length $N$ with $S=2^K$ codewords $\mathbf x^{(s)}$. $K=\log_2 S$ is the number of bits conveyed by choosing one codeword. $R=K/N$ is the rate in bits per channel use. $\hat s$ is the decoder's guess of $s$ (p. 161).

### 10.1 The theorem (p. 162)
1. For every discrete memoryless channel (output at each step depends only on the current input), the capacity
$$C=\max_{P_X} I(X;Y)\tag{10.1}$$
has this property: for any $\epsilon>0$ and $R<C$, and large enough $N$, there is a code of length $N$ and rate $\ge R$ with a decoding algorithm whose **maximal** probability of block error is $<\epsilon$ (p. 162).
2. If bit error probability $p_b$ is acceptable, rates up to $R(p_b)$ are achievable, where
$$R(p_b)=\frac{C}{1-H_2(p_b)}.\tag{10.2}$$
3. For any $p_b$, rates greater than $R(p_b)$ are not achievable (p. 162). Figure 10.1 marks regions 1 and 2 as achievable and region 3 as not (p. 162).

### 10.2 Jointly-typical sequences (pp. 162–164)
Codewords come from an ensemble $X^N$. Choosing one codeword and passing it through the channel gives a joint ensemble $(XY)^N$. The decoder is a typical-set decoder. The proof bounds (a) the probability that the true codeword is not jointly typical with $\mathbf y$ and (b) the probability that a false codeword is. Both go to zero for large $N$ if there are fewer than $2^{NC}$ codewords and $X$ has the optimal input distribution (p. 162).

**Joint typicality.** $\mathbf x,\mathbf y$ of length $N$ are jointly typical to tolerance $\beta$ for $P(x,y)$ if all three hold (p. 162):
$$\left|\tfrac1N\log\tfrac1{P(\mathbf x)}-H(X)\right|<\beta,\quad \left|\tfrac1N\log\tfrac1{P(\mathbf y)}-H(Y)\right|<\beta,\quad \left|\tfrac1N\log\tfrac1{P(\mathbf x,\mathbf y)}-H(X,Y)\right|<\beta .$$
The jointly-typical set $J_{N\beta}$ is the set of all such pairs (p. 163).

**Example (p. 163).** $N=100$, $P(x)$ has $(p_0,p_1)=(0.9,0.1)$, and the channel is a binary symmetric channel (BSC) with noise level 0.2. The pair shown has 10 ones in $\mathbf x$ (typical), 26 ones in $\mathbf y$ (typical, since $P(y{=}1)=0.26$), and $\mathbf x,\mathbf y$ differ in 20 bits (the typical number of flips) (p. 163).

**Joint typicality theorem (p. 163).** Let $\mathbf x,\mathbf y$ be drawn from $P(\mathbf x,\mathbf y)=\prod_{n=1}^N P(x_n,y_n)$. Then:
1. The probability that $\mathbf x,\mathbf y$ are jointly typical tends to 1 as $N\to\infty$.
2. $|J_{N\beta}|\le 2^{N(H(X,Y)+\beta)}$ (10.3).
3. If $\mathbf x'\sim X^N$ and $\mathbf y'\sim Y^N$ are *independent* samples with the same marginals, then
$$P((\mathbf x',\mathbf y')\in J_{N\beta})\le 2^{-N(I(X;Y)-3\beta)}.\tag{10.4}$$

*Proof.* Parts 1–2 follow from the law of large numbers as in the source coding theorem (Ch. 4), with the pair $(x,y)$ playing the role of $x$. For part 3 (p. 163):
$$P((\mathbf x',\mathbf y')\in J_{N\beta})=\sum_{(\mathbf x,\mathbf y)\in J_{N\beta}}P(\mathbf x)P(\mathbf y)\tag{10.5}$$
$$\le |J_{N\beta}|\,2^{-N(H(X)-\beta)}2^{-N(H(Y)-\beta)}\tag{10.6}$$
$$\le 2^{N(H(X,Y)+\beta)-N(H(X)+H(Y)-2\beta)}\tag{10.7}$$
$$=2^{-N(I(X;Y)-3\beta)}.\tag{10.8}$$

Cartoon (figure 10.2): independent typical pairs fill a rectangle of about $2^{NH(X)}2^{NH(Y)}$ pairs. About $2^{NH(X,Y)}$ of them are jointly typical. So the hit probability is about
$$2^{NH(X,Y)}/2^{NH(X)+NH(Y)}=2^{-NI(X;Y)}\tag{10.9–10.10}$$
(p. 163). In the figure, each typical $\mathbf x$ goes with about $2^{NH(Y|X)}$ typical $\mathbf y$'s, and vice versa with $2^{NH(X|Y)}$ (p. 164).

*Intuition note.* Most (input, output) pairs that look typical separately do not fit together. A random wrong codeword matches the received word with probability about $2^{-NI}$. That is why up to about $2^{NI}$ codewords can be told apart.

### 10.3 Proof of the noisy-channel coding theorem (pp. 164–167)
**Analogy (p. 164).** To show that one of 100 babies weighs under 10 kg, weigh them all together. If the average is under 10 kg, at least one baby is lighter, with the caveat that a few elephants could spoil the argument. Likewise, Shannon computes the average error probability over *all* codes. If it is small, individual good codes must exist (p. 164).

**Random coding and typical-set decoding (pp. 164–165).** Rate $R'$ system:
1. Fix $P(x)$. Generate $S=2^{NR'}$ codewords of an $(N,NR')$ code at random with $P(\mathbf x)=\prod_n P(x_n)$ (10.11).
2. The code is known to sender and receiver.
3. Choose $s\in\{1,\dots,2^{NR'}\}$ and send $\mathbf x^{(s)}$. The output has $P(\mathbf y|\mathbf x^{(s)})=\prod_n P(y_n|x_n^{(s)})$ (10.12).
4. *Typical-set decoding:* decode $\mathbf y$ as $\hat s$ if $(\mathbf x^{(\hat s)},\mathbf y)$ are jointly typical and no other $s'$ gives a jointly-typical pair. Otherwise declare failure ($\hat s=0$). This is not the optimal decoder, but it is easier to analyse.
5. An error occurs if $\hat s\neq s$ (p. 165).

Three error probabilities (pp. 165–166):
- For a particular code: $p_B(\mathcal C)\equiv P(\hat s\ne s|\mathcal C)$ (10.13). It is hard to evaluate.
- The average over codes: $\langle p_B\rangle\equiv\sum_{\mathcal C}P(\hat s\neq s|\mathcal C)P(\mathcal C)$ (10.14). It is much easier to evaluate.
- The maximal one: $p_{BM}(\mathcal C)\equiv\max_s P(\hat s\ne s|s,\mathcal C)$ (10.15). It is the one we want small.

Plan: bound $\langle p_B\rangle$; deduce that some code has small $p_B(\mathcal C)$; then throw away the worst 50% of its codewords to control $p_{BM}$ (p. 166).

**Error of the typical-set decoder (p. 166).** Errors come from (a) $\mathbf y$ not jointly typical with the sent codeword, or (b) another codeword jointly typical with $\mathbf y$. By symmetry, the code-averaged error does not depend on $s$, so take $s=1$.
(a) By part 1 of the theorem, $P((\mathbf x^{(1)},\mathbf y)\notin J_{N\beta})\le\delta$, with $\delta\to0$ as $N\to\infty$.
(b) For a given $s'\neq1$, part 3 gives probability $\le2^{-N(I(X;Y)-3\beta)}$, and there are $2^{NR'}-1$ rivals. So
$$\langle p_B\rangle\le\delta+\sum_{s'=2}^{2^{NR'}}2^{-N(I(X;Y)-3\beta)}\tag{10.16}$$
$$\le\delta+2^{-N(I(X;Y)-R'-3\beta)}.\tag{10.17}$$
Step (10.16) is a **union bound**: the probability of a union of error events is at most the sum of their probabilities, with equality only if the events never co-occur (p. 166). The average error can be made $<2\delta$ by increasing $N$ if
$$R'<I(X;Y)-3\beta.\tag{10.18}$$

**Three modifications (pp. 166–167).**
1. Choose $P(x)$ to be the optimal input distribution. Then the condition is $R'<C-3\beta$.
2. The average over codes is $<2\delta$, so some code has $p_B(\mathcal C)<2\delta$.
3. **Expurgation:** discard the worst half of the codewords. The rest all have conditional error probability $<4\delta$. (added step: if any survivor had error $\ge4\delta$, so would all the discarded half, giving mean error $\ge2\delta$, contradicting $p_B(\mathcal C)<2\delta$.) The new code has $2^{NR'-1}$ codewords, so its rate is $R'-1/N$, and $p_{BM}<4\delta$ (p. 167). Figure 10.5 shows the idea: delete the "colliding" codewords that are close enough to be confused.

Conclusion: a code of rate $R'-1/N$ exists, with $R'<C-3\beta$ and $p_{BM}<4\delta$. To get the theorem as stated, set $R'=(R+C)/2$, $\delta=\epsilon/4$, $\beta<(C-R')/3$, and take $N$ large (p. 167). Since $p_b\le p_{BM}$, the region of figure 10.6 (rates below $C$, any $p_b$) is achievable (p. 167).

*Intuition note.* Random codes are good on average because a wrong codeword rarely looks jointly typical. The union bound adds up many tiny chances, which stays small while $R'<C$. Dropping the worst half then fixes the worst case at almost no cost.

### 10.4 Communication (with errors) above capacity (pp. 167–168)
This extends the achievable region to non-zero $p_b$ (called rate–distortion theory by the author) (p. 167). Trick: a noisy channel can be turned into a noiseless channel of rate up to $C$, so it suffices to study error-allowed communication over a noiseless channel (p. 167).

**Simple strategy.** On a noiseless binary channel (capacity 1 bit) with a demanded rate $R>1$, send a fraction $1/R$ of the source bits and let the receiver guess the rest at random:
$$p_b=\tfrac12(1-1/R).\tag{10.19}$$
This is the dashed curve of figure 10.7. Spreading the risk evenly over all bits does better: $p_b=H_2^{-1}(1-1/R)$, the solid curve (p. 168).

**How the optimum is reached (p. 168).** Take an excellent $(N,K)$ code for the BSC with transition probability $q$. Its rate is $R'=K/N\simeq1-H_2(q)$. With such a capacity-achieving code on a BSC:
- (a) the output distribution is close to uniform;
- (b) the optimal decoder typically maps a received vector to a codeword differing in $qN$ bits.

Now use the decoder as a compressor:
- Chop the signal into blocks of length $N$ and pass each through the decoder to get $K$ bits. Send these over the noiseless channel.
- At the far end, pass the $K$ bits through the code's encoder. The result differs from the original in about $qN$ bits, so $p_b=q$.
- The compressor's rate is $R=N/K=1/R'=1/(1-H_2(p_b))$.
- Attaching this to the error-free capacity-$C$ communicator gives achievability up to
$$R=\frac{C}{1-H_2(p_b)}.\tag{10.20}$$

*Intuition note.* A code that corrects $qN$ errors, run backwards, maps long blocks to short ones that typically land within about $qN$ flips of the original. The bits we may get wrong are the price of squeezing more than $C$ bits per use through the channel.

### 10.5 The non-achievable region (pp. 168–169)
Source, encoder, channel and decoder form a Markov chain $s\to\mathbf x\to\mathbf y\to\hat s$:
$$P(s,\mathbf x,\mathbf y,\hat s)=P(s)P(\mathbf x|s)P(\mathbf y|\mathbf x)P(\hat s|\mathbf y).\tag{10.21}$$
The data processing inequality gives $I(s;\hat s)\le I(\mathbf x;\mathbf y)$. By the definition of capacity, $I(\mathbf x;\mathbf y)\le NC$, so $I(s;\hat s)\le NC$. If a system achieves rate $R$ with bit error $p_b$, then $I(s;\hat s)\ge NR(1-H_2(p_b))$. Since $I(s;\hat s)>NC$ is impossible, $R>C/(1-H_2(p_b))$ is not achievable (p. 168). Exercise 10.1 asks for the details, including why the inequality holds when bit errors are correlated (pp. 168–169).

### 10.6 Computing capacity (pp. 169–171)
(Marked advanced; first-time readers may skip to 10.9.) Capacity requires the optimal input distribution, found in general by computer search using the derivative of $I$ with respect to the input probabilities (Ex. 10.2) (p. 169). $I(X;Y)$ is concave in the input probability vector $\mathbf p$ (Ex. 10.3), so any stationary point is a global maximum. Hence one might seek
$$\partial I(X;Y)/\partial p_i=\lambda\ \text{ for all } i,\tag{10.22}$$
with $\lambda$ a Lagrange multiplier for $\sum_ip_i=1$. This may fail because the maximum can have $p_i=0$ for some inputs (p. 169).

**Ternary confusion channel.** $\mathcal A_X=\{0,?,1\}$, $\mathcal A_Y=\{0,1\}$. Inputs 0 and 1 are reliable. Input $?$ gives output 0 or 1 with probability 1/2 each. The maximum rate of 1 bit is achieved by never using $?$ (p. 169).

**Results that may help (p. 170).** (1) All outputs must be used (unless unreachable, Ex. 10.6). (2) $I(X;Y)$ is convex in the channel parameters $Q(y|x)$. (3) Several optimal input distributions may exist, but all give the same output distribution.

**Symmetry argument (p. 170).** If a channel is invariant under a group of symmetry operations, take an optimal non-symmetric input distribution and average it with its permuted copies. The copies have equal $I$ by symmetry, and the average has $I$ at least as large by concavity.

**Symmetric channel (Gallager's definition, p. 170).** A discrete memoryless channel is symmetric if its outputs can be partitioned into subsets so that, within each subset, the transition matrix has each row (if more than 1) a permutation of every other row and each column a permutation of every other column. Example 10.9 (10.23–10.24):

| | $x=0$ | $x=1$ |
|---|---|---|
| $y=0$ | 0.7 | 0.1 |
| $y=1$ | 0.1 | 0.7 |
| $y=?$ | 0.2 | 0.2 |

Its outputs split into $\{0,1\}$ and $\{?\}$ (p. 170). Symmetry matters because, as the author says will be seen later, linear codes can achieve capacity over symmetric channels (p. 171). Ex. 10.10 asks the reader to prove that the uniform input is optimal for a symmetric channel with any number of inputs. Ex. 10.11 asks whether non-symmetric channels can also have uniform optimal inputs (p. 171).

### 10.7 Other coding theorems (pp. 171–172)
The theorem is general but not specific: it does not say how large $N$ must be for given $R$ and $\epsilon$. Presumably $N$ must grow as $\epsilon$ shrinks and $R\to C$ (p. 171).

**Version with explicit $N$ (p. 171).** For a discrete memoryless channel there exist block codes of length $N$ and rate $R$ with average error
$$p_B\le\exp[-NE_r(R)],\tag{10.25}$$
where the random-coding exponent (reliability function) $E_r(R)$ is convex, decreasing and positive for $0\le R<C$, and tends to 0 as $R\to C$. By expurgation, $p_{BM}$ is also exponentially small in $N$. Even for the BSC there is no simple expression for $E_r(R)$ (p. 171).

**Lower bound (pp. 171–172).** For any code of blocklength $N$ with equally likely messages, $p_B$ is bounded below by $\exp[-NE_{sp}(R)]$ (10.26; the relation is lower-bound type, see Reading notes). Here the sphere-packing exponent $E_{sp}(R)$ is also convex, decreasing and positive for $0\le R<C$ (p. 172).

### 10.8 Theorems and coding practice (p. 172)
Given a channel, $R$ and $p_B$, one could compute $C$, $E_r$, $E_{sp}$ and say that a blocklength $N$ exists, and that almost any random code of that length should work. But implementing a random code with large $N$ costs exponentially in $N$. Customers rarely know their channel exactly. Berlekamp (1980) suggests designing systems and plotting performance on several idealized channels against noise level, which reduces the importance of $E_r$ and $E_{sp}$ (p. 172).

### 10.9 Further exercises (pp. 172–173)
Ex. 10.12 asks for the capacity of the binary erasure channel (stated as $C=1-q$) and, via a $(2,1)$ code emulating an erasure channel with two Z-channel uses, the bound $C_Z\ge\tfrac12(1-q)$. Ex. 10.13 is the transatlantic-cable labelling problem with $N=20$ wires, which can be solved by persistent search but also by a greedy information-maximizing approach (p. 173).

### 10.10 Solutions (pp. 173–175)
**Ex. 10.4 (pp. 173–174).** For $\mathbf p=(p_0,p_?,p_1)$:
$$I(X;Y)=H(Y)-H(Y|X)=H_2(p_0+p_?/2)-p_?.\tag{10.27}$$
Special cases give the sketch skeleton (fig. 10.9): $p_?=0$ gives $H_2(p_0)$; $p_0=p_1$ gives $1-p_?$; $p_0=0$ gives a Z channel with error probability 0.5.

**Ex. 10.5 (p. 174).** Necessary and sufficient conditions for $\mathbf p$ to maximize $I$:
$$\begin{cases}\partial I/\partial p_i=\lambda & \text{and } p_i>0\\ \partial I/\partial p_i\le\lambda & \text{and } p_i=0\end{cases}\ \text{for all } i,\tag{10.28}$$
where $\lambda$ is related to capacity by $C=\lambda+\log_2e$. A program can raise and lower the $p_i$ in proportion to the derivative differences. One can also guess an optimal distribution and verify (10.28).

**Ex. 10.11 (p. 174).** Non-symmetric channels with uniform optimal input are expected to exist by counting. A channel has $I(J-1)$ degrees of freedom, the optimal input only $I-1$; so in the space of perturbations around a symmetric channel one expects a subspace of dimension $I(J-2)+1$ of perturbations that leave the optimal input unchanged. The explicit example, "a bit like a Z channel", is
$$Q=\begin{bmatrix}0.9585&0.0415&0.35&0.0\\0.0415&0.9585&0.0&0.35\\0&0&0.65&0\\0&0&0&0.65\end{bmatrix}.\tag{10.29}$$

**Ex. 10.13 (pp. 174–175).** The problem can be solved for any $N>2$ with two trips, one each way. The information content of one partition (connecting wires into groups, $g_r$ groups of size $r$) is the log of the number of partitions:
$$\Omega=\frac{N!}{\prod_r (r!)^{g_r}g_r!}.\tag{10.30}$$
Maximizing $\log\Omega$ over real-valued $g_r$ subject to $\sum_rg_rr=N$, with Lagrange multiplier $\lambda$:
$$\frac{\partial}{\partial g_r}\Big(\log\Omega+\lambda\sum_rg_rr\Big)=-\log r!-\log g_r+\lambda r.\tag{10.31}$$
Setting this to zero gives
$$g_r=\frac{e^{\lambda r}}{r!},\tag{10.32}$$
proportional to a Poisson distribution. With $\mu\equiv e^\lambda$, the constraint gives
$$N=\mu e^{\mu}.\tag{10.33}$$
(added step: $\sum_r\mu^r r/r!=\mu\sum_{r\ge1}\mu^{r-1}/(r-1)!=\mu e^\mu$.) For $N=20$, $\mu=2.2$ and the integer choice $g_r=\{1,2,2,1,1\}$ gives (a)(bc)(de)(fgh)(ijk)(lmno)(pqrst). It carries $\log\Omega=40.4$ bits, against $\log20!\simeq61$ bits needed. Joining all wires in pairs gives only about 29 bits. The second partition is left to the reader. For $N\ne2,5,9$ there are simple Knowlton–Graham partitions: two partitions $A$, $B$ of $\{1,\dots,N\}$ such that, for each $j,k$, at most one element lies in both an $A$-set of size $j$ and a $B$-set of size $k$ (p. 175).

## Toy example (ours, not from the text)
BSC with flip probability $q=0.1$, uniform input. Then $H(Y)=1$ and $H(Y|X)=H_2(0.1)=-0.1\log_20.1-0.9\log_20.9=0.3322+0.1368=0.4690$. So $I=C=1-0.4690=0.5310$ bits.

Take $N=100$, $\beta=0.01$, $R'=0.4$, so $S=2^{NR'}=2^{40}$ codewords.
- False-codeword term of (10.17): $2^{-N(I-R'-3\beta)}=2^{-100(0.5310-0.4-0.03)}=2^{-100(0.1010)}=2^{-10.10}\approx1/1097\approx9.1\times10^{-4}$.
- Heuristic count (10.9–10.10, $\beta=0$): about $2^{NH(Y)}=2^{100}$ typical outputs, of which about $2^{NH(Y|X)}=2^{46.9}$ go with a given codeword. A wrong codeword matches with chance about $2^{46.9-100}=2^{-53.1}$. Over $2^{40}$ codewords: $2^{40-53.1}=2^{-13.1}$.
- Above capacity, take $R'=0.6$: the exponent is $60-100(0.5010)=+9.9$, so the bound $2^{9.9}\approx955$ exceeds 1 and says nothing.

The bound is small only when $R'<I-3\beta$, as in (10.18). The numbers at $N=100$ only illustrate the exponent. Other terms, such as $\delta$, are not computed.

## Concepts
- [[noisy-channel-coding-theorem]] — for rates $R<C$, codes with arbitrarily small (maximal) block error exist; above $R(p_b)$ they do not (pp. 162, 167–168)
- [[channel-capacity]] — $C=\max_{P_X}I(X;Y)$ for a discrete memoryless channel (p. 162)
- [[mutual-information]] — $I(X;Y)$; sets the chance $2^{-NI}$ that independent sequences look jointly typical (p. 163)
- [[typical-set-aep]] — here extended to jointly-typical pairs, with $|J_{N\beta}|\le2^{N(H(X,Y)+\beta)}$ (pp. 162–163)
- [[jointly-typical-set]] (new) — pairs $(\mathbf x,\mathbf y)$ where $\mathbf x$, $\mathbf y$ and the pair are each typical to tolerance $\beta$ (p. 162)
- [[typical-set-decoder]] (new) — decode as $s$ if $\mathbf x^{(s)}$ alone is jointly typical with $\mathbf y$; otherwise declare failure (p. 165)
- [[random-coding]] (new) — Shannon's method: average error over randomly drawn codes, so a good code must exist (pp. 164–165)
- [[union-bound]] (new) — total error probability $\le$ the sum of the probabilities of events that each suffice for error (p. 166)
- [[expurgation]] (new) — delete the worst half of the codewords to turn small average error into small maximal error (p. 167)
- [[rate-distortion-function]] — rate achievable at bit-error $p_b$ is $C/(1-H_2(p_b))$ (pp. 167–168)
- [[data-processing-inequality]] — $I(s;\hat s)\le I(\mathbf x;\mathbf y)\le NC$ along $s\to\mathbf x\to\mathbf y\to\hat s$ (p. 168)
- [[symmetric-channel]] (new) — Gallager's partition-into-permutation-matrices definition; Ex. 10.10 asks to prove that the uniform input is optimal (p. 171) (p. 170)
- [[random-coding-exponent]] (new) — $E_r(R)$ with $p_B\le e^{-NE_r(R)}$ (p. 171)
- [[sphere-packing-exponent]] (new) — $E_{sp}(R)$ in the lower bound on $p_B$ (pp. 171–172)

## Canonical instances
- [[binary-symmetric-channel]] — jointly-typical example ($N=100$, noise 0.2); code reversed as lossy compressor (pp. 163, 168)
- [[ternary-confusion-channel]] — the optimal input leaves one input unused, so the constraint $p_i\ge0$ matters (pp. 169, 173–174)
- [[binary-erasure-channel]] — capacity $1-q$ (Ex. 10.12, p. 172)
- [[z-channel]] — capacity bounded via erasure emulation (Ex. 10.12, p. 172)
- [[cable-labelling-problem]] — greedy information maximization giving Poisson-shaped group sizes (pp. 173–175)

## Bridges (candidates)
- [structural-analogy] Random-coding existence proof ↔ probabilistic method: if the average has a property, some member does (pp. 164, 166).
- [same-math] Optimality condition (10.28) ↔ Lagrange/KKT conditions for constrained maximization with $p_i\ge0$ (pp. 169, 174).
- [structural-analogy] Averaging over symmetry copies (concavity of $I$) ↔ Jensen's inequality argument (p. 170).
- [structural-analogy] Typical-set decoding ↔ Bayesian hypothesis choice among codewords (decoder weighs "which $s$ explains $\mathbf y$"); the chapter itself uses typicality, not posteriors.
- [same-math] Rate–distortion via reversed code (10.20) ↔ lossy compression theory (information-theory canon).

## Questions this raises
- The decoder in the proof is not optimal. How much better does an optimal (maximum-posterior) decoder do, and how do $E_r(R)$ and $E_{sp}(R)$ compare?
- Linear codes are said to reach capacity on symmetric channels. How do they avoid the exponential cost of random codes?
- For the cable problem, how should the second partition be chosen so the two partitions are as unlike as possible?
- What if the channel is not exactly known (Berlekamp's concern)? How should a code be chosen then?

## Exercises worth doing
- Ex. 10.1 (p. 168) — fill in the converse: when $I(s;\hat s)=NR(1-H_2(p_b))$, and why $\ge$ holds with correlated errors — difficulty: medium
- Ex. 10.3 (p. 169) — prove $I(X;Y)$ is concave in $\mathbf p$; the key to the optimization story — difficulty: medium
- Ex. 10.6 (p. 170) — no output is unused by an optimal input unless unreachable — difficulty: medium
- Ex. 10.10 (p. 171) — uniform input is optimal for symmetric channels — difficulty: medium
- Ex. 10.12 (p. 172) — erasure channel capacity and the Z-channel bound — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 173 = p. 161). Pages carry printed numbers, and the labels match.
- The relation sign in (10.26) is missing from the text layer of p. 171. Given the heading "Lower bounds on the error probability", I read it as "$\gtrsim$". This is my reading, not a verified sign.
- The text layer of the p. 162 figure 10.1 and the p. 164 figures is garbled. The image of figure 10.1 shows the axes, the curve $R(p_b)$ and the region labels 1, 2, 3.
- The cast-of-characters table (p. 161) says $R=K/N$ is "sometimes called $R'$ instead". In the proof, $R'$ is the rate of the random code and $R<R'<C$.
- Exercise 10.5's solution states $C=\lambda+\log_2 e$ as printed; I did not re-derive it.
- Sections 10.6–10.8 are marked by the author as advanced material.
- Solutions are printed only for Ex. 10.4, 10.5, 10.11, 10.13. I summarised their main steps and results.
