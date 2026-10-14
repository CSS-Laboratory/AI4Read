---
id: mackay-2003-information/ch17-communication
work: mackay-2003-information
unit: "17 Communication over Constrained Noiseless Channels"
pages: 248-259
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Communication over Constrained Noiseless Channels

## L0 — One line
If some strings are forbidden, the capacity of the channel is $\log_2\lambda_1$, where $\lambda_1$ is the principal eigenvalue of the matrix that records which state-to-state moves are allowed.

## L1 — The gist (≤ 120 words)
How many bits per use can we send over a channel where some strings are forbidden, such as "no 11"? The chapter defines capacity as $C=\lim \frac1N\log M_N$, where $M_N$ is the number of valid strings of length $N$. Counting paths in a trellis (a diagram of the channel's states over time, in which valid strings are paths) gives $M_N\sim\lambda_1^N$, so $C=\log_2\lambda_1$. Channel A (no 11) has $C=\log_2 1.618=0.694$. Channels B and C are related to A by invertible maps. Optimal codes use transition probabilities built from the eigenvectors of the matrix; the sequences they produce have entropy $\log_2\lambda$ per symbol. The same ideas extend to symbols with different durations.

**Prerequisites:** entropy and binary entropy $H_2$; matrix–vector products; eigenvalues and eigenvectors; mod-2 arithmetic; geometric series; Taylor expansion.

## L2 — Key ideas
- A constrained noiseless channel allows only some input strings. Runlength-limited channels (which limit how short or long a run of equal symbols may be) A, B and C are the running examples (pp. 248–249).
- A simple code (C₂) gives rate 2/3. Feeding it a sparse source (a stream with fewer 1s than 0s, a fraction $f$ of 1s) gives $R(f)=H_2(f)/(1+f)$, which peaks near 0.69 at $f\simeq0.38$ (p. 250).
- Capacity is $\lim\frac1N\log M_N$, which is the same identity as for noisy channels, but with $M_N$ counting valid strings (pp. 250–251).
- Valid strings are paths through a trellis (states drawn over time). Counting them is message passing with the connection matrix (entry 1 where a move between two states is allowed, else 0), $\mathbf c^{(N)}=\mathbf A^N\mathbf c^{(0)}$, so $C=\log_2\lambda_1$ (pp. 251–254).
- For channel A the counts form the Fibonacci series and $C=\log_2\gamma=0.694$. Channels A and B are linked by an accumulator (running sum mod 2) and its inverse, the differentiator, and channel C is related to both (pp. 253–254).
- Optimal variable-length coding uses $Q_{s'|s}=e^{(L)}_{s'}A_{s's}/(\lambda e^{(L)}_s)$, whose output entropy is $\log_2\lambda$ per symbol (pp. 255, 258).
- When symbols have durations $l_i$, the optimal symbol probabilities are $p_i^*=2^{-\beta l_i}$, with $\beta$ the capacity in bits per unit time. This is analogous to $p_i=2^{-l_i^*}$ in symbol codes (p. 256).
- For a channel that allows any run of 0s and a large maximum run $L$ of 1s, capacity is very close to 1 bit (p. 258), and the capacity is approximated by $\beta\simeq1-2^{-(L+2)}/\ln2$ (p. 259).

## L3 — Walkthrough

### 17.1 Three examples of constrained binary channels (pp. 248–250)
A constrained channel is defined by rules saying which strings are permitted (p. 248).
- **Channel A:** every 1 must be followed by at least one 0 (substring 11 forbidden). Motivation: a pulse device that needs one clock cycle to recover (p. 248).
- **Channel B:** all runs of 1s and of 0s have length ≥ 2 (101 and 010 forbidden). Motivation: an isolated magnetic domain on a disk is unstable (p. 248).
- **Channel C:** runs have length at most 2 (111 and 000 forbidden). Motivation: the disk speed is poorly known, so runs of two and three equal symbols are hard to tell apart (p. 249).

All three are *runlength-limited* channels (p. 249). Min/max runlengths:

| Channel | 1s min–max | 0s min–max |
|---|---|---|
| unconstrained | 1–∞ | 1–∞ |
| A | 1–1 | 1–∞ |
| B | 2–∞ | 2–∞ |
| C | 1–2 | 1–2 |

The unconstrained binary channel has capacity 1 bit per use. Until capacity is defined for these channels, "capacity" means bits conveyed reliably per channel use (p. 249).

**Codes for channel A.** Code C₁ maps $0\to00$, $1\to10$. It has rate 1/2, so capacity of A is at least 0.5 (p. 249). Code C₂ drops the redundant 0: $0\to0$, $1\to10$. With equally frequent source bits the mean length is
$$L=\tfrac12\cdot1+\tfrac12\cdot2=\tfrac32,\tag{17.4}$$
so $R=2/3$ (17.5), and capacity of A is at least 2/3 (p. 249).

**First argument for doing better.** Feed C₂ a source with a fraction $f$ of 1s. Such a stream could come from passing a file through the decoder of an arithmetic code that is optimal for density $f$ (p. 250). The rate is the source entropy divided by the mean transmitted length:
$$L(f)=(1-f)+2f=1+f,\tag{17.6}$$
$$R(f)=\frac{H_2(f)}{L(f)}=\frac{H_2(f)}{1+f}.\tag{17.7}$$
Set $f=\tfrac12+\delta$ (17.8) with small negative $\delta$. Near $f=1/2$, $L(f)$ is linear in $\delta$, but $H_2(f)$ depends on $\delta$ only at second order (Exercise 17.4). So to first order $R$ increases linearly with decreasing $\delta$. Figure 17.1 shows $R(f)$ has a maximum of about 0.69 bits per channel use at $f\simeq0.38$. Hence capacity of A is at least $\max_f R(f)=0.69$ (p. 250).

*Intuition note:* Sending fewer 1s shortens the transmitted stream at once, but it hardly lowers the information per source bit near $f=1/2$. So the rate improves.

Exercise 17.5 solution (p. 257): C₂ at $f=0.5$ sends on average one-third 1s. At $f=0.38$ the fraction of 1s is $f/(1+f)=(\gamma-1)/(2\gamma-1)=0.2764$.

**Second, more fundamental argument:** count the valid sequences $S_N$ of length $N$. Giving each a name conveys $\log S_N$ bits in $N$ cycles (p. 250).

### 17.2 The capacity of a constrained noiseless channel (pp. 250–251)
For noisy channels, capacity was related to the number of distinguishable messages $S(N)$ in $N$ uses by
$$C=\lim_{N\to\infty}\frac1N\log S(N).\tag{17.9}$$
For the constrained noiseless channel this identity is adopted as the *definition*. The letter $s$ is now used for channel states, so the number of distinguishable messages of length $N$ is written $M_N$ (p. 250–251):
$$C=\lim_{N\to\infty}\frac1N\log M_N.\tag{17.10}$$

### 17.3 Counting the number of possible messages (pp. 251–254)
**Representations.** A *state diagram* has circles for transmitter states. Directed edges are permitted transitions, labelled with the emitted symbol. For channel A there are two states, 0 and 1. A transition into state $s$ emits $s$, and 1→1 is absent (Fig. 17.2a, p. 251). A *trellis section* shows states $s_n$ and $s_{n+1}$ at two successive times. A *trellis* strings sections together, and a valid sequence is a path through it (p. 251). For counting, edge labels are ignored. The *connection matrix* $\mathbf A$ has $A_{ss'}=1$ if there is an edge from $s$ to $s'$, and 0 otherwise (p. 253). Figure 17.3 gives $\mathbf A$ for channels B and C, each with four states labelled 11, 1, 0, 00 (p. 251).

**Counting by message passing.** Counts are accumulated left to right across the trellis (Fig. 17.4). Figure 17.5a gives total path counts for channel A: $M_n=2,3,5,8,13,21,34,55$ for $n=1,\dots,8$ (pp. 252–253). This is the Fibonacci series. Channel B gives the same $M_n$ for $n=1,\dots,8$, and channel C gives $1,2,3,5,8,13,21,34$ (Fig. 17.5, p. 252). Figure 17.5 assumes the first bit is preceded by 00. So channels A and B accept any first symbol, but channel C's first symbol must be a 1 (p. 252).

Figure 17.6 (p. 253) shows channel A: $M_8=55$ with ratio $M_n/M_{n-1}=1.618$ and $\frac1n\log_2M_n=0.72$. By $n=400$, $M_n=5\times10^{83}$ and $\frac1n\log_2M_n=0.69$.

Exercise 17.6 asks to show the ratio tends to the golden ratio
$$\gamma\equiv\frac{1+\sqrt5}{2}=1.618.\tag{17.11}$$
So $M_N\sim\gamma^N$ to within a constant factor, and
$$C=\lim\frac1N\log_2\!\big[\text{constant}\cdot\gamma^N\big]=\log_2\gamma=\log_2 1.618=0.694.\tag{17.12}$$

**Matrix form.** The count vector $\mathbf c^{(n)}$ (one entry per state) obeys
$$\mathbf c^{(n+1)}=\mathbf A\mathbf c^{(n)},\tag{17.13}$$
$$\mathbf c^{(N)}=\mathbf A^N\mathbf c^{(0)},\tag{17.14}$$
where $\mathbf c^{(0)}$ is the state count before any symbol is sent. Figure 17.5 uses $\mathbf c^{(0)}=[0,1]^{\mathsf T}$, so either symbol is allowed first. The total is $M_n=\sum_s c^{(n)}_s=\mathbf c^{(n)}\cdot\mathbf n$ (with $\mathbf n$ the all-ones vector). In the limit, $\mathbf c^{(N)}$ is dominated by the principal right-eigenvector of $\mathbf A$:
$$\mathbf c^{(N)}\to\text{constant}\cdot\lambda_1^N\,\mathbf e_{\mathrm R}^{(0)}.\tag{17.15}$$
Here $\lambda_1$ is the principal eigenvalue of $\mathbf A$. So the capacity of any constrained channel is
$$C=\log_2\lambda_1.\tag{17.16}$$
(Shapes: for channel A, $\mathbf A$ is $2\times2$ and $\mathbf c^{(n)}$ has length 2. For B and C, $\mathbf A$ is $4\times4$ and $\mathbf c^{(n)}$ has length 4.) (p. 253–254)

*Intuition note:* Every extra symbol multiplies the number of valid strings by roughly $\lambda_1$. So each symbol carries about $\log_2\lambda_1$ bits.

### 17.4 Back to our model channels (p. 254)
Figures 17.5a–c suggest that B and C have the same capacity as A. The principal eigenvalues of the three trellises are the same. The eigenvectors for A and B are given in table C.4 on p. 608 (outside this unit) (p. 254).

**A ↔ B.** An *accumulator* maps a valid A-string $\mathbf s$ to
$$t_1=s_1,\qquad t_n=t_{n-1}+s_n \bmod 2\ (n\ge2).\tag{17.17}$$
The result is valid for B, because $\mathbf s$ has no 11 and so $\mathbf t$ has no isolated digits. The accumulator is invertible. The inverse, the *binary differentiator*, maps any valid B-string to a valid A-string:
$$s_1=t_1,\qquad s_n=t_n-t_{n-1}\bmod2\ (n\ge2).\tag{17.18}$$
Since $+$ and $-$ agree mod 2, the differentiator is also a "blurrer": it convolves the source stream with the filter $(1,1)$ (p. 254).

**C.** Exercise 17.7 solution (p. 257): a valid C-string comes from a valid A-string by first inverting it ($1\to0$, $0\to1$) and then passing it through an accumulator. Both steps are invertible. With the assumption that C starts after a run of zeros (so its first character is 1), the equivalence is exact only if A's first character must be 0.

### 17.5 Practical communication over constrained channels (pp. 254–256)
Since the three channels are equivalent, the text concentrates on channel A (p. 254).

**Fixed-length solutions.** Table 17.8 maps 8 source strings to 5-bit strings valid for A, for example $1\to00000$, $2\to10000$, $8\to10010$. Its rate is $3/5=0.6$ (p. 254). Exercise 17.8 asks for all length-8 strings ending in the zero state (34 of them), giving 5 bits → 8 bits at rate $5/8=0.625$. For $N=16$, at most 10 source bits fit, so the rate is again 0.625 (solution, p. 257).

**Optimal variable-length solution.** The optimal way is to find the optimal transition probabilities $Q_{s'|s}$ at all trellis points and make transitions with them (p. 255). For channel A, a sparse source of density $f=0.38$ driving C₂ achieves capacity. Sparse sources can be made with an arithmetic code optimal for sparse strings: its decoder maps dense (random binary) strings to sparse ones (p. 255).

Exercise 17.9 (statement only, no printed solution). Take the principal right and left eigenvectors, $\mathbf A\mathbf e^{(R)}=\lambda\mathbf e^{(R)}$ and $\mathbf e^{(L)\mathsf T}\mathbf A=\lambda\mathbf e^{(L)\mathsf T}$, with the largest eigenvalue $\lambda$. The optimal $\mathbf Q$ has invariant distribution proportional to $e^{(R)}_ie^{(L)}_i$ and is
$$Q_{s'|s}=\frac{e^{(L)}_{s'}A_{s's}}{\lambda\,e^{(L)}_s}.\tag{17.19}$$

Exercise 17.10 (solution, p. 258) shows the entropy rate of sequences from (17.19) is $\log_2\lambda$ per symbol. Let the invariant distribution be
$$P(s)=\alpha\,e^{(L)}_se^{(R)}_s,\tag{17.22}$$
with $\alpha$ a normalization constant. Then, with $S_{t-1}$ drawn from this distribution,
$$H(S_t|S_{t-1})=-\sum_{s,s'}P(s)P(s'|s)\log P(s'|s)\tag{17.23}$$
$$=-\sum_{s,s'}\alpha e^{(L)}_se^{(R)}_s\frac{e^{(L)}_{s'}A_{s's}}{\lambda e^{(L)}_s}\log\frac{e^{(L)}_{s'}A_{s's}}{\lambda e^{(L)}_s}\tag{17.24}$$
$$=-\sum_{s,s'}\alpha e^{(R)}_s\frac{e^{(L)}_{s'}A_{s's}}{\lambda}\Big[\log e^{(L)}_{s'}+\log A_{s's}-\log\lambda-\log e^{(L)}_s\Big].\tag{17.25}$$
Since $A_{s's}\in\{0,1\}$, the terms proportional to $A_{s's}\log A_{s's}$ vanish. The $-\log\lambda$ term gives $\log\lambda$ (added step: the weights $P(s)Q_{s'|s}$ sum to 1). So
$$H(S_t|S_{t-1})=\log\lambda-\frac\alpha\lambda\sum_{s'}\Big(\sum_sA_{s's}e^{(R)}_s\Big)e^{(L)}_{s'}\log e^{(L)}_{s'}+\frac\alpha\lambda\sum_s\Big(\sum_{s'}e^{(L)}_{s'}A_{s's}\Big)e^{(R)}_s\log e^{(L)}_s\tag{17.26}$$
$$=\log\lambda-\frac\alpha\lambda\sum_{s'}\lambda e^{(R)}_{s'}e^{(L)}_{s'}\log e^{(L)}_{s'}+\frac\alpha\lambda\sum_s\lambda e^{(L)}_se^{(R)}_s\log e^{(L)}_s\tag{17.27}$$
$$=\log\lambda.\tag{17.28}$$
(Step 17.26→17.27 uses the eigenvector equations. The last two sums are identical after renaming $s'\to s$, so they cancel.)

*Intuition note:* Choosing moves with probabilities built from $\mathbf e^{(L)}$ gives a sequence whose entropy rate is $\log_2\lambda$, which is the capacity (17.16). So these probabilities use the channel at full capacity.

**Practical caveats.** The author says one would probably use finite-precision approximations. Variable-length codes make the encoded length unpredictable, which one might dislike; for example, a disk drive is easier to control if all 512-byte blocks are known to take exactly the same disk space (p. 255). For some channels a simple modification gives a guarantee on the encoded length: use two variable-length codes such that any string has an above-average length under one if it is below-average under the other. Encode with both, send the shorter, and prepend a bit saying which code was used (p. 255).

Exercise 17.11 asks for $M_8$ (strings starting with 0), the capacities of the channels with maximum 1-runs of 2 and 3 (Fig. 17.9), and (using a computer) the matrices $\mathbf Q$ for channel A and those two channels. Solution: principal eigenvalues 1.839 and 1.928, capacities 0.879 and 0.947 bits (p. 258).

Exercise 17.12 considers any run of 0s and 1-runs of at most $L$ (large). The printed solution (p. 258–259) gives these steps.
- The capacity is very close to 1 bit. A lower bound comes from a code that replaces the maximal run $11\ldots1$ by $11\ldots10$ and otherwise leaves the file unchanged. Its rate is $1/(1+2^{-L})$.
- Using exercise 6.18, capacity is the $\beta$ such that
$$Z(\beta)=\sum_{l=1}^{L+1}2^{-\beta l}=1,\tag{17.29}$$
the $L+1$ terms matching the strings $0,10,110,\dots,11\ldots10$. By the geometric sum,
$$Z(\beta)=2^{-\beta}\frac{\big(2^{-\beta}\big)^{L+1}-1}{2^{-\beta}-1}.\tag{17.30}$$
- Setting $Z(\beta)=1$ (17.31) and using $\ln(1+x)\simeq x$ gives
$$\beta\simeq1-2^{-(L+2)}/\ln2.\tag{17.32}$$
Examples from the table: $L=2$: $\beta=0.910$, true 0.879. $L=3$: 0.955 vs 0.947. $L=9$: 0.9993 vs 0.9993.
- $Q_{1|0}$ is close to $1/2$, just slightly larger. After a run of $L-1$ ones, let $f$ be the probability of choosing "10" over "0". With $C\approx1$ the entropy of the next $N$ characters is
$$H\simeq H_2(f)+[(N-1)(1-f)+(N-2)f]C=H_2(f)+NC-fC\simeq H_2(f)+N-f.\tag{17.33}$$
Setting the derivative to zero gives
$$\log_2\frac{1-f}{f}\simeq1\ \Rightarrow\ \frac{1-f}{f}\simeq2\ \Rightarrow\ f\simeq\tfrac13.\tag{17.34}$$
So the probability of emitting a 1 falls from about 0.5 to about 1/3 as the run of 1s grows. For the $L=9$ channel the explicit matrix (17.35) has entries .3334, .4287, .4669, .4841, .4923, .4963, .4983, .4993, .4998 on its upper diagonal. The complementary entries in the last row are .6666, .5713, .5331, .5159, .5077, .5037, .5017, .5007, .5002. The text concludes "Our rough theory works" (p. 259).

### 17.6 Variable symbol durations (p. 256)
The aim is the maximum rate per unit time when symbols have different durations.

**Unconstrained channel.** This is exercise 6.18. The task is to find the optimal usage frequencies of the symbols. The author notes an analogy with symbol codes. For a source with probabilities $p_i$, the optimal lengths are $l_i^*=\log_2 1/p_i$, so
$$p_i=2^{-l_i^*}.\tag{17.20}$$
For symbols with durations $l_i$, the optimal probabilities are
$$p_i^*=2^{-\beta l_i},\tag{17.21}$$
where $\beta$ is the capacity in bits per unit time (p. 256).

**Constrained channel.** The author says that once the earlier topics are grasped, one can figure out how to define and find capacity here (p. 256). Exercise 17.13 (Morse channel) has symbols dot, dash, short space and long space. Spaces may be followed only by dots and dashes. The exercise asks for the capacity in bits per unit time if (a) all four symbols have equal durations, or (b) the durations are 2, 4, 3 and 6 time units respectively (p. 256).

### Applications posed as exercises (p. 257)
Exercise 17.14 asks how well Morse code suits English. Exercise 17.15 models DNA squeezed into a tube of width $L$. In the open, a polymer of length $N$ doing a 3-direction random walk has entropy $N\log3$. In the tube the connection matrix is tridiagonal with 1s (for $L=10$, first row $1\,1\,0\ldots$, last row $\ldots0\,1\,1$). The entropy of the walk, and the change on entering the tube, are to be found. The text states that the capacity difference between constrained and unconstrained channels is directly proportional to the force needed to pull the DNA into the tube (p. 257).

## Toy example (ours)
Channel A with states $(0,1)$ = last symbol sent. From 0 we may go to 0 or 1. From 1 only to 0. Put rows = "to", columns = "from":
$$\mathbf A=\begin{bmatrix}1&1\\1&0\end{bmatrix},\qquad \mathbf c^{(0)}=\begin{bmatrix}1\\0\end{bmatrix}\ \text{(start as if after a 0)}.$$
- $\mathbf c^{(1)}=\mathbf A\mathbf c^{(0)}=[1\cdot1+1\cdot0,\ 1\cdot1+0\cdot0]=[1,1]$, so $M_1=2$ (strings 0, 1).
- $\mathbf c^{(2)}=[1+1,\ 1]=[2,1]$, so $M_2=3$ (00, 01, 10).
- $\mathbf c^{(3)}=[2+1,\ 2]=[3,2]$, so $M_3=5$. Direct list: 000, 001, 010, 100, 101 = 5. ✓.
- Eigenvalues: $\det(\mathbf A-\lambda\mathbf I)=(1-\lambda)(-\lambda)-1=\lambda^2-\lambda-1=0$, so $\lambda_1=(1+\sqrt5)/2=1.618$.
- $C=\log_2 1.618=0.694$ bits per symbol, since $2^{0.694}\approx1.618$. For $n=3$, $\frac1n\log_2M_n=\frac13\log_2 5=0.77$, and this value falls towards 0.694 as $N$ grows (compare Fig. 17.6).

## Concepts
- [[constrained-noiseless-channel]] (new) — noiseless channel where only some input strings may be sent (p. 248)
- [[runlength-limited-channel]] (new) — constrained channel limiting the minimum and maximum runs of 1s and 0s (p. 249)
- [[channel-capacity]] — here $\lim\frac1N\log M_N$, with $M_N$ the number of valid length-$N$ strings (p. 251)
- [[trellis-and-connection-matrix]] (new) — trellis of states over time; matrix $\mathbf A$ marks permitted transitions (p. 251, 253)
- [[capacity-as-log-principal-eigenvalue]] (new) — $C=\log_2\lambda_1$ for connection matrix $\mathbf A$ (p. 254)
- [[optimal-transition-probabilities]] (new) — $Q_{s'|s}$ from eigenvectors; entropy rate $\log_2\lambda$ (p. 255, 258)
- [[entropy]] — used as information per source symbol, $H_2(f)$ (p. 250)
- [[huffman-arithmetic-coding]] — arithmetic-code decoders serve as "sparsifiers" (p. 255)
- [[redundancy]] — C₁'s forced 0 is redundant and can be removed (p. 249)
- [[variable-symbol-durations]] (new) — channels with symbols of different durations; capacity per unit time $\beta$, $p_i^*=2^{-\beta l_i}$ (p. 256)

## Canonical instances
- [[channel-A-no-11]] — no 11; Fibonacci counts; $C=0.694$ (p. 248, 253)
- [[channel-B-C-equivalence]] — B and C equivalent to A by accumulator and inversion (p. 254, 257)
- [[morse-channel]] — constrained channel with variable symbol durations (p. 256)
- [[dna-in-tube]] — polymer in a tube as a constrained random walk (p. 257)

## Bridges (candidates)
- [structural-analogy] $p_i^*=2^{-\beta l_i}$ for channel symbols ↔ information-theory: optimal code lengths $l_i=\log_2 1/p_i$ — the text itself draws this analogy (p. 256).
- [same-math] Trellis path counting with $\mathbf A^N$ ↔ statistical physics: polymer entropy in a tube — the text says the same calculations are done to predict polymer thermodynamics (p. 257).
- [structural-analogy] $\mathbf Q$ built from $\mathbf e^{(L)}$ so all long valid strings are equally likely ↔ maximum entropy principle: least-committal distribution under constraints.
- [structural-analogy] Message passing on a trellis ↔ Bayesian inference: sum-product on a chain (the chapter reuses Chapter 16's local message passing, p. 248).

## Questions this raises
- Does the rate approach $\log_2\lambda_1$ for any starting state $\mathbf c^{(0)}$, and when is $\lambda_1$ guaranteed to dominate?
- How close to capacity can a finite-precision, guaranteed-length code get?
- How is capacity defined and computed when a constrained channel also has variable symbol durations (the Morse case)?
- What happens to these capacities when the channel is also noisy?

## Exercises worth doing
- Ex. 17.4 (p. 250) — Taylor expansion of $H_2$ near $1/2$; why $R(f)$ rises when $f$ falls — difficulty: easy
- Ex. 17.6 (p. 253) — Fibonacci ratios tend to the golden ratio, giving $C=0.694$ — difficulty: easy
- Ex. 17.8 (p. 254) — fixed-length code from the 34 length-8 strings; rate 0.625 — difficulty: easy
- Ex. 17.9 (p. 255) — derive the optimal $\mathbf Q$ from eigenvectors — difficulty: hard
- Ex. 17.13 (p. 256) — capacity of the Morse channel with equal and unequal durations — difficulty: hard
- Ex. 17.15 (p. 257) — entropy of a polymer in a tube; link to force — difficulty: hard

## Reading notes
- Printed page = pdf page − 12. Figures 17.2–17.5 had garbled text layers. I checked them against the images. Path counts in Section 17.3 are read from Figure 17.5 and Figure 17.6.
- Index convention: p. 253 says $A_{ss'}=1$ for an edge from $s$ to $s'$. Figure 17.2d labels columns "(from)" and rows "(to)", and (17.19) uses $A_{s's}$ with $s'$ the new state; (17.13), $\mathbf c^{(n+1)}=\mathbf A\mathbf c^{(n)}$, is consistent with rows = to. The figure and equations agree with each other (rows = to). The prose definition has its subscripts the other way round.
- In (17.15) the vector is printed $\mathbf e_{\mathrm R}^{(0)}$, the principal right-eigenvector.
- Matrix (17.35): I did not interpret the state ordering. Each column sums to 1 (for example .3334 + .6666).
- Ex. 17.9, 17.13, 17.14, 17.15 and 17.11 (computer part) have no printed solution on these pages. In (17.33) the printed result $NC-fC$ omits a constant: the bracket $(N-1)(1-f)+(N-2)f$ equals $N-1-f$. The constant does not affect the optimal $f$. Figure 17.9 matrices are not reproduced here.
- Eigenvectors for A and B are in table C.4 (p. 608), not in these pages.
