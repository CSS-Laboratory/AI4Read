---
id: shannon-1948-mathematical/main-p1
work: shannon-1948-mathematical
unit: "paper (part 1/2): Introduction, Part I (discrete noiseless systems), Part II §§11–17, Appendix 1, start of Appendix 2"
pages: 1–28
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 9
---
# A Mathematical Theory of Communication — Part 1 (pp. 1–28)

## L0 — One line
Information produced by a source is measured by entropy $H=-\sum p_i\log p_i$; $H$ determines the channel capacity needed on a noiseless channel, and on a noisy channel the best reliable rate is the capacity $C=\max[H(x)-H_y(x)]$, a property of the channel.

## L1 — The gist (≤ 120 words)
Shannon asks how to measure the information a source produces and how fast it can be sent over a channel. He defines entropy $H=-\sum p_i\log p_i$ and shows that long messages carry about $H$ bits per symbol. On a noiseless channel of capacity $C$, proper coding sends about $C/H$ symbols per second, and no more. For a noisy channel he defines the equivocation $H_y(x)$ and the capacity $C=\max[H(x)-H_y(x)]$. Information at rates below $C$ can be sent with errors as rare as desired; at rates above $C$ an equivocation of at least the excess is unavoidable. Meaning is ignored: a message is only a selection from a set.

**Prerequisites:** logarithms base 2; basic probability (joint, conditional, independence); sums and maxima; Lagrange multipliers (only in §§15–16); matrices and determinants (only in Theorem 1).

## L2 — Key ideas (5–10 bullets)
- **Meaning is out of scope.** Only the fact that one message is chosen from a set of possible messages matters, and the system must work for every possible choice (p. 1).
- **Logarithmic measure.** Engineering quantities tend to vary linearly with the log of the number of possibilities; base 2 gives bits (pp. 1–2).
- **Channel capacity (noiseless).** $C=\lim_{T\to\infty}\log N(T)/T$; for finite-state constraints it is $\log W$, with $W$ the largest root of a determinant equation (Theorem 1) (pp. 3–4).
- **Sources as Markoff processes; entropy.** A discrete source can be represented by a stochastic process; its entropy $H=\sum_i P_iH_i$ is the information per symbol. Three requirements that Shannon calls reasonable single out the form $-K\sum p_i\log p_i$ (Theorem 2); he says they are not necessary to the theory (pp. 10–13).
- **Typical sequences.** For large $N$, almost all sequences have $\log(1/p)/N$ close to $H$, so for most purposes the long sequences can be treated as about $2^{HN}$ of them (Theorems 3–4); $F_N$ and $G_N$ approach $H$ from above (Theorems 5–6) (pp. 13–14).
- **Noiseless coding theorem.** One can transmit at $C/H-\epsilon$ symbols per second, never above $C/H$ (Theorem 9) (p. 16).
- **Equivocation and noisy capacity.** The rate is $R=H(x)-H_y(x)$ and $C=\max R$ over input sources (pp. 20–22).
- **Fundamental theorem for noisy channels.** Below $C$ error can be made arbitrarily small, shown by averaging over random codes (Theorem 11); above $C$ equivocation is at least $H-C$ (pp. 22–24).
- **Worked cases and a code.** Capacity is computed for several channels, and a 7-symbol Hamming code reaches the capacity of a block-noise channel (pp. 25–28).

## L3 — Walkthrough

### Introduction (pp. 1–2)
- **Goal.** Shannon extends the work of Nyquist and Hartley to include noise and the savings due to the statistical structure of the source and the nature of the destination (p. 1).
- **Problem.** Communication means reproducing at one point, exactly or approximately, a message selected at another point (p. 1). Messages often have meaning, but "These semantic aspects of communication are irrelevant to the engineering problem" (p. 1). What matters is that the message is one selected from a set of possible messages. The system must work for each possible selection, since the actual one is unknown at design time (p. 1).
- **Measure.** If the set is finite and all choices are equally likely, the number of messages, or any monotonic function of it, can measure the information. Hartley's choice, the logarithm, is the most natural (p. 1). Shannon says three reasons make it convenient (p. 1):
  1. Time, bandwidth, number of relays and similar parameters tend to vary linearly with the log of the number of possibilities. Adding one relay doubles the states, so it adds 1 to the base-2 log.
  2. It matches intuition: two punched cards should hold twice as much as one.
  3. Limiting operations are simpler in logarithms.
- **Units.** Base 2 gives *binary digits* or *bits* (Tukey's word). $N$ two-state devices store $N$ bits, since $\log_2 2^N=N$ (p. 1). Base 10 gives decimal digits, with $\log_2 M=\log_{10}M/\log_{10}2=3.32\log_{10}M$, so one decimal digit is about $3\tfrac13$ bits. Base $e$ gives natural units. Changing from base $a$ to base $b$ multiplies by $\log_b a$ (pp. 1–2).
- **System (Fig. 1).** Five parts (p. 2): information source (message may be letters, a function of time, of $(x,y,t)$, several functions, etc.); transmitter (turns message into signal); channel (the medium); receiver (usually the inverse operation); destination. A noise source acts on the signal in the channel.
- **Three categories.** *Discrete* (message and signal are sequences of discrete symbols), *continuous*, and *mixed* (p. 3). This unit covers the discrete case, which "forms a foundation" for the continuous and mixed cases treated in the second half of the paper (p. 3).

### Part I — 1. The discrete noiseless channel (pp. 3–4)
- A discrete channel transmits sequences of choices from finite symbols $S_1,\dots,S_n$. Symbol $S_i$ lasts $t_i$ seconds. Not all sequences need be allowed (p. 3). Telegraph example: dot (1 unit closed, 1 open), dash (3 closed, 1 open), letter space (3 open), word space (6 open); no two spaces may be adjacent (p. 3).
- Teletype case: any sequence of 32 symbols of equal duration is allowed, so 5 bits per symbol. At $n$ symbols per second the capacity is $5n$ bits/s. This is the maximum possible rate; the actual rate depends on the source (p. 3).
- **Definition (capacity).**
$$C=\lim_{T\to\infty}\frac{\log N(T)}{T}$$
where $N(T)$ is the number of allowed signals of duration $T$. It can be shown that the limit exists as a finite number in most cases of interest (p. 3).
- If all sequences are allowed, $N(t)=N(t-t_1)+\dots+N(t-t_n)$, because sequences are counted by their last symbol. By a well-known result on finite differences (the maths of equations linking a quantity to its earlier values), $N(t)$ is asymptotic to $X_0^t$, with $X_0$ the largest real solution of
$$X^{-t_1}+X^{-t_2}+\dots+X^{-t_n}=1,$$
and so $C=\log X_0$ (pp. 3–4).
- Telegraph with the stated restriction: $N(t)=N(t-2)+N(t-4)+N(t-5)+N(t-7)+N(t-8)+N(t-10)$. So $C=-\log\mu_0$, where $\mu_0$ is the positive root of $1=\mu^2+\mu^4+\mu^5+\mu^7+\mu^8+\mu^{10}$. Solving gives $C=0.539$ (p. 4).
- **State constraints (Fig. 2).** There are states $a_1,\dots,a_m$. Each state allows certain symbols, and sending one moves to a new state. In the telegraph case there are two states: whether or not a space was last sent (p. 4).
- **Theorem 1.** Let $b_{ij}^{(s)}$ be the duration of the $s$-th symbol allowed in state $i$ that leads to state $j$. Then $C=\log W$, where $W$ is the largest real root of
$$\Big|\sum_s W^{-b_{ij}^{(s)}}-\delta_{ij}\Big|=0,$$
with $\delta_{ij}=1$ if $i=j$ and 0 otherwise (p. 4). This is an $m\times m$ determinant. For telegraph it is
$$\begin{vmatrix}-1 & W^{-2}+W^{-4}\\ W^{-3}+W^{-6} & W^{-2}+W^{-4}-1\end{vmatrix}=0,$$
which expands to the equation above (p. 4). The proof is in Appendix 1 (below).

> **Intuition note.** The number of distinguishable signals grows like $W^T$, so the information that can be carried grows linearly in $T$ with slope $\log W$. Capacity is just this slope, in bits per second.

### 2. The discrete source of information (pp. 4–7)
- Statistical structure lets a good code save time or capacity. Telegraphy already gives the short dot to the common letter E; commercial codes give short groups to common phrases (p. 5).
- A discrete source chooses symbols one by one with probabilities that may depend on earlier choices. A physical or mathematical system producing symbols this way is a *stochastic process* (a process governed by probabilities). Conversely, any stochastic process producing symbols from a finite set can be seen as a discrete source. Examples are written languages, quantized continuous sources, and abstract processes (p. 5).
- Abstract examples (pp. 5–6):
  - **(A)** Letters A–E, each with probability .2, independent.
  - **(B)** Same letters with probabilities .4, .1, .2, .2, .1, independent.
  - **(C)** The next letter depends on the preceding letter only. This is described by transition probabilities $p_i(j)$ (probability that $i$ is followed by $j$) or digram probabilities $p(i,j)$ (frequency of the pair $ij$). The relations are
$$p(i)=\sum_j p(i,j)=\sum_j p(j,i)=\sum_j p(j)p_j(i),\qquad p(i,j)=p(i)p_i(j),\qquad \sum_j p_i(j)=\sum_i p(i)=\sum_{i,j}p(i,j)=1.$$
   Three-letter example: rows of $p_i(j)$ (columns A, B, C) are A: $0,\tfrac45,\tfrac15$; B: $\tfrac12,\tfrac12,0$; C: $\tfrac12,\tfrac25,\tfrac1{10}$. Letter frequencies are $p(A),p(B),p(C)=\tfrac9{27},\tfrac{16}{27},\tfrac2{27}$. The digram table $p(i,j)$ has rows A: $0,\tfrac4{15},\tfrac1{15}$; B: $\tfrac8{27},\tfrac8{27},0$; C: $\tfrac1{27},\tfrac4{135},\tfrac1{135}$ (p. 6). Longer memory needs trigram probabilities $p_{ij}(k)$ and, in general, $n$-gram probabilities (p. 6).
  - **(D)** A source emitting independent "words" (16 words with given probabilities, separated by spaces). If all words are finite this is equivalent to an earlier type, but the description may be simpler (p. 6).
- A natural language can be approximated by a series of artificial languages: zero-order (all letters equiprobable and independent), first-order (independent with real letter frequencies; E has probability .12, W .02), second-order (digram structure), third-order (trigram structure) (pp. 6–7).

### 3. The series of approximations to English (pp. 7–8)
- With a 27-symbol alphabet (26 letters and space), Shannon shows sample texts for: zero-order, first-order, second-order (digram), third-order (trigram), first-order word approximation, and second-order word approximation (p. 7). The resemblance to English increases quite noticeably at each step. The samples are reasonable out to about twice the range used in constructing them (p. 7).
- He remarks that it appears a sufficiently complex stochastic process will give a satisfactory representation of a discrete source (p. 7). The samples were made with random-number tables, or by opening a book at random and reading on from the previous letter (p. 8).

### 4. Graphical representation of a Markoff process (p. 8)
- A discrete Markoff process has finitely many states $S_1,\dots,S_n$ and transition probabilities $p_i(j)$ from $S_i$ to $S_j$. It becomes a source if a letter is produced at each transition. States stand for the "residue of influence" of preceding letters (p. 8).
- Figs. 3–5 draw this as a graph. Example B has one state (independent letters). Example C has as many states as letters. A trigram source would have at most $n^2$ states (p. 8).

### 5. Ergodic and mixed sources (pp. 8–10)
- An *ergodic* process is one in which every sequence has the same statistical properties. Letter and digram frequencies measured on a sequence approach limits independent of the sequence. The exceptions have probability zero. Roughly, ergodic means statistical homogeneity (pp. 8–9).
- A graph gives an ergodic process if (p. 9): (1) it does not split into two parts with no path from one to the other in either direction; (2) the greatest common divisor of the lengths of all circuits (closed, consistently directed loops) is 1.
- If (1) holds but the gcd is $d>1$, sequences fall into $d$ classes that differ only by a shift of origin. Example with $d=2$: $a$ is followed by $b$ or $c$ with probability $\tfrac13,\tfrac23$, and $b$ or $c$ is always followed by $a$. Shannon says this case is of little importance for his work (p. 9).
- If (1) fails but (2) holds for each subgraph (Shannon assumes this), the source is *mixed*: $L=p_1L_1+p_2L_2+\dots$. It is made of ergodic components, one is chosen at the start with probability $p_i$, and the sequence stays in it forever. Example: $L=.2L_1+.8L_2$ (pp. 9–10).
- Sources are assumed ergodic unless stated. This lets one identify averages along a sequence with ensemble averages (averages over all sequences the source could produce), with probability one (p. 10). For stationarity (statistics that do not change over time) the state probabilities must satisfy these equilibrium conditions (balance: probability flowing into each state equals its own probability)
$$P_j=\sum_i P_ip_i(j).$$
In the ergodic case, from any start the probabilities $P_j(N)$ approach these values as $N\to\infty$ (p. 10).

### 6. Choice, uncertainty and entropy (pp. 10–12)
- **Requirements** for a measure $H(p_1,\dots,p_n)$ of "choice" or uncertainty (p. 10):
  1. $H$ is continuous in the $p_i$.
  2. If all $p_i=1/n$, $H$ increases monotonically with $n$.
  3. If a choice is broken into successive choices, $H$ is the weighted sum of the parts. Fig. 6 example: $H(\tfrac12,\tfrac13,\tfrac16)=H(\tfrac12,\tfrac12)+\tfrac12H(\tfrac23,\tfrac13)$. The factor $\tfrac12$ appears because the second choice occurs half the time.
- **Theorem 2.** The only $H$ satisfying the three assumptions has the form
$$H=-K\sum_{i=1}^n p_i\log p_i,\qquad K>0,$$
proved in Appendix 2 (p. 11). Shannon says the theorem and its assumptions are "in no way necessary" to the theory. It lends plausibility, and "the real justification" of the definitions lies in their implications (p. 11).
- $K$ only fixes the unit. The form is that of entropy in statistical mechanics (Boltzmann's $H$ theorem, a result in the statistical physics of gases). Shannon calls $H=-\sum p_i\log p_i$ the **entropy**. $H(x)$ labels the entropy of chance variable (random variable) $x$. For two outcomes $p,q=1-p$, $H=-(p\log p+q\log q)$ is plotted in Fig. 7 (p. 11).
- **Properties** (pp. 11–12):
  1. $H=0$ iff all $p_i$ but one are zero (that one equals 1). Otherwise $H>0$.
  2. For given $n$, $H\le\log n$, with maximum $\log n$ when all $p_i=1/n$.
  3. With joint probabilities $p(i,j)$: $H(x,y)=-\sum p(i,j)\log p(i,j)$, $H(x)=-\sum_{i,j}p(i,j)\log\sum_jp(i,j)$, $H(y)=-\sum_{i,j}p(i,j)\log\sum_ip(i,j)$. It is easily shown (Shannon's words) that $H(x,y)\le H(x)+H(y)$, with equality only if $p(i,j)=p(i)p(j)$.
  4. Any equalizing change in the $p_i$ increases $H$. For averaging $p_i'=\sum_ja_{ij}p_j$ with $\sum_ia_{ij}=\sum_ja_{ij}=1$ and all $a_{ij}\ge0$, $H$ increases, except when the transformation is only a permutation.
  5. *Conditional entropy.* With $p_i(j)=p(i,j)/\sum_jp(i,j)$,
$$H_x(y)=-\sum_{i,j}p(i,j)\log p_i(j)=H(x,y)-H(x),$$
   (substituting $p_i(j)$ and splitting the logarithm), i.e. $H(x,y)=H(x)+H_x(y)$. It is the uncertainty of $y$ on average when $x$ is known.
  6. From 3 and 5: $H(x)+H(y)\ge H(x,y)=H(x)+H_x(y)$, hence $H(y)\ge H_x(y)$. Knowing $x$ never increases the uncertainty of $y$; it decreases it unless $x,y$ are independent.

> **Intuition note.** Entropy measures how much choice or uncertainty there is in picking an outcome. For a given number of outcomes it is largest when all are equally likely, and it is zero when the outcome is certain. Knowing $x$ never increases the average uncertainty about $y$.

### 7. The entropy of an information source (pp. 13–15)
- For a finite-state source, each state $i$ has entropy $H_i$ from its $p_i(j)$. The source entropy per symbol is
$$H=\sum_iP_iH_i=-\sum_{i,j}P_ip_i(j)\log p_i(j).$$
If the process runs in time, the entropy per second is $H'=\sum_if_iH_i=mH$, where $f_i$ is the frequency of state $i$ and $m$ is the average number of symbols per second. In base 2 these are bits per symbol and bits per second (p. 13).
- For independent symbols, a long message of $N$ symbols contains about $p_iN$ copies of symbol $i$ with high probability. So $p\approx p_1^{p_1N}\cdots p_n^{p_nN}$, giving $\log p\doteq N\sum p_i\log p_i=-NH$, i.e. $H\doteq\frac{\log 1/p}{N}$ (p. 13).
- **Theorem 3.** Given $\epsilon>0$, $\delta>0$ there is $N_0$ such that all sequences of length $N\ge N_0$ fall into two classes: a set of total probability less than $\epsilon$, and the rest, all with
$$\Big|\frac{\log p^{-1}}{N}-H\Big|<\delta.$$
So $\log p^{-1}/N$ is almost certainly very close to $H$ for large $N$ (p. 13). This holds "for any source" (stated for general sources, proof in Appendix 3) (p. 13).
- **Theorem 4.** Order the length-$N$ sequences by decreasing probability and let $n(q)$ be the number needed to accumulate total probability $q$. Then
$$\lim_{N\to\infty}\frac{\log n(q)}{N}=H\quad\text{when }q\neq0,1.$$
The growth rate of the number of reasonably probable sequences is $H$, regardless of the meaning of "reasonably". For most purposes the long sequences can be treated as though there were just $2^{HN}$ of them, each of probability $2^{-HN}$ (p. 14).

> **Intuition note.** Out of all possible long messages, almost all the probability sits on a set that, for most purposes, can be treated as about $2^{HN}$ "typical" messages, each of probability about $2^{-HN}$. So about $H$ bits per symbol suffice to specify them.

- **Theorem 5.** $G_N=-\frac1N\sum_ip(B_i)\log p(B_i)$, summed over all $N$-symbol blocks $B_i$, is monotonic decreasing in $N$ and $\lim G_N=H$ (p. 14).
- **Theorem 6.** With $p_{B_i}(S_j)=p(B_i,S_j)/p(B_i)$ and $F_N=-\sum_{i,j}p(B_i,S_j)\log p_{B_i}(S_j)$ (blocks of $N-1$ symbols):
$$F_N\ \text{decreases in }N,\quad F_N=NG_N-(N-1)G_{N-1},\quad G_N=\frac1N\sum_{n=1}^NF_n,\quad F_N\le G_N,\quad \lim F_N=H.$$
- $F_N$ is the conditional entropy of the next symbol given the $N-1$ preceding ones. It is the entropy of the $N$-th order approximation, and it is the better approximation to $H$. $G_N$ is the entropy per symbol of $N$-blocks. If no influence reaches back beyond $N$ symbols, $F_N=H$ (p. 14).
- **Relative entropy** (Shannon's meaning): the ratio of a source's entropy to the maximum it could have with the same symbols. It is the maximum possible compression when encoding into the same alphabet. $1-$relative entropy is the **redundancy**. For ordinary English, ignoring structure beyond about eight letters, redundancy is roughly 50%: half of what is written is fixed by the language and half chosen freely (p. 14).
- The 50% comes from several methods (p. 15): entropy of approximations; deleting a fraction of letters and asking someone to restore them (if 50% can be restored, redundancy exceeds 50%); and known cryptographic results.
- Extremes: Basic English (850 words) has very high redundancy; Joyce's *Finnegans Wake* is "alleged" to compress semantic content (p. 15). Crossword puzzles: with zero redundancy any letter array is a puzzle; with too much redundancy large puzzles are impossible. If constraints are "chaotic and random", large puzzles are just possible at 50% redundancy; at 33%, three-dimensional puzzles should be possible (p. 15).

> **Intuition note.** Redundancy is the part of a text that is fixed by the structure of the language rather than chosen freely. $F_N$ gets lower as the predictor looks at more context, which is why longer-range structure keeps shrinking the estimate of $H$.

### 8. Representation of encoding and decoding (pp. 15–16)
- A *discrete transducer* has finitely many internal states $\alpha_n$. Its output and next state are functions of the current input symbol $x_n$ and state:
$$y_n=f(x_n,\alpha_n),\qquad \alpha_{n+1}=g(x_n,\alpha_n).$$
Transducers can be chained. If a second transducer recovers the input of the first, the first is *non-singular* and the second is its inverse (p. 15).
- **Theorem 7.** The output of a finite-state transducer driven by a finite-state statistical source is a finite-state source with entropy per unit time $\le$ that of the input, and equal if the transducer is non-singular (p. 15).
- Proof idea: use the product state space of (source state, transducer state) pairs, sum the entropy over states, and note that summing first on the transducer state gives each term $\le$ the corresponding source term. For non-singular transducers, with $H_1',H_2',H_3'$ the entropies of the source, the first transducer's output and the inverse's output: $H_1'\ge H_2'\ge H_3'=H_1'$, so $H_1'=H_2'$ (p. 15).
- **Theorem 8.** Let the constraints (as in Fig. 2, with $\ell_{ij}^{(s)}$ the durations) have capacity $C=\log W$. If transition probabilities are assigned as
$$p_{ij}^{(s)}=\frac{B_j}{B_i}W^{-\ell_{ij}^{(s)}},\qquad B_i=\sum_{s,j}B_jW^{-\ell_{ij}^{(s)}},$$
then $H$ is maximized and equals $C$ (p. 16). Proof is in Appendix 4, not in this part.

### 9. The fundamental theorem for a noiseless channel (pp. 16–17)
- **Theorem 9.** A source has entropy $H$ (bits per symbol), a channel has capacity $C$ (bits per second). The source output can be encoded so as to transmit at average rate $\frac CH-\epsilon$ symbols per second, with $\epsilon$ arbitrarily small. It is not possible to transmit at an average rate greater than $\frac CH$ (p. 16).
- **Converse.** The transmitter must be non-singular, so the channel-input entropy per second equals the source's, $H'$. It cannot exceed $C$. So $H'\le C$ and the symbol rate is $H'/H\le C/H$ (p. 16).
- **First proof of the direct part** (p. 16):
  - For large $N$ the $N$-symbol sequences split into a group with fewer than $2^{(H+\eta)N}$ members and a group with fewer than $2^{RN}$ members ($R$ = log of the number of symbols) and total probability less than $\mu$. As $N$ grows, $\eta$ and $\mu$ go to 0.
  - The channel has more than $2^{(C-\theta)T}$ signals of duration $T$. Take $T=(\frac HC+\lambda)N$. Then there are enough channel sequences for the high-probability group, which is coded one-to-one into them.
  - The remaining sequences get longer codes that start and end with an unused sequence, which acts as a start/stop signal. They need $T_1=(\frac RC+\varphi)N$.
  - The mean rate in message symbols per second then exceeds
$$\Big[(1-\delta)\tfrac TN+\delta\tfrac{T_1}N\Big]^{-1}=\Big[(1-\delta)\big(\tfrac HC+\lambda\big)+\delta\big(\tfrac RC+\varphi\big)\Big]^{-1}.$$
  As $N$ grows, $\delta,\lambda,\varphi\to0$ and the rate approaches $C/H$ (pp. 16–17).
- **Second proof (binary code).**
  - Order the length-$N$ messages by decreasing probability $p_1\ge p_2\ge\dots\ge p_n$. Let $P_s=\sum_{i=1}^{s-1}p_i$ (cumulative probability not including $p_s$). The code of message $s$ is the binary expansion (the number written in base 2, e.g. $\tfrac34=0.11$) of $P_s$ carried to $m_s$ places, where $m_s$ is the integer with
$$\log_2\frac1{p_s}\le m_s<1+\log_2\frac1{p_s}.$$
  - Hence $\frac1{2^{m_s}}\le p_s<\frac1{2^{m_s-1}}$. All later $P_i$ exceed $P_s$ by at least $2^{-m_s}$, so their expansions differ within the first $m_s$ places. So all codes are different and decodable (p. 17). If channel symbols are not binary, binary numbers are assigned to them arbitrarily.
  - Average binary digits per original symbol: $H'=\frac1N\sum m_sp_s$. From the inequalities on $m_s$,
$$G_N\le H'<G_N+\frac1N.$$
  - So the inefficiency with delay $N$ need not exceed $\frac1N$ plus the gap between $H$ and $G_N$. The percent excess time over the ideal is less than $\frac{G_N}{H}+\frac1{HN}-1$ (p. 17).
  - This is substantially the same as the method independently found by R. M. Fano: split the probability-ordered list into two groups of nearly equal probability, give the first digit 0 or 1 accordingly, and repeat inside each group. It differs from the above only in minor ways, generally in the last digit (p. 17).

> **Intuition note.** Give likely messages short codewords and unlikely ones long ones, with length about $\log 1/p$. Then the average length per symbol is about $H$, so a channel of capacity $C$ carries about $C/H$ symbols per second. Longer blocks make the match tighter but add delay.

### 10. Discussion and examples (pp. 17–19)
- Analogy (author's): as a transformer matches generator and load for maximum power transfer, the encoder should match source to channel statistically. The source seen through the transducer should look like the entropy-maximizing source for the channel. Theorem 9 says this match can be approximated as closely as desired. Coding *efficiency* is the actual rate over $C$, equal to the ratio of the actual to the maximum entropy of channel symbols (pp. 17–18).
- In general, ideal or nearly ideal encoding needs a long delay. The quantity $\big|\frac{\log p^{-1}}{T}-C\big|$ must be small for all but a small fraction of long messages (p. 18).
- A source that can produce only one message has zero entropy and needs no channel (e.g. the digits of $\pi$, which a machine at the receiver could compute). If that is impractical, one may ignore some statistical knowledge and use the maximum-entropy source subject to the conditions retained. Its entropy fixes the capacity that is "necessary and sufficient". For $\pi$, retaining only that digits come from $\{0,\dots,9\}$; for English, retaining only letter frequencies gives the first-order approximation (p. 18).
- **Example 1.** Letters A, B, C, D with probabilities $\tfrac12,\tfrac14,\tfrac18,\tfrac18$, independent:
$$H=-\big(\tfrac12\log\tfrac12+\tfrac14\log\tfrac14+\tfrac28\log\tfrac18\big)=\tfrac74\text{ bits per symbol}.$$
The code A→0, B→10, C→110, D→111 achieves it: average length $N(\tfrac12\cdot1+\tfrac14\cdot2+\tfrac28\cdot3)=\tfrac74N$. The 0 and 1 have probabilities $\tfrac12,\tfrac12$, so the coded sequence has 1 bit per symbol. The maximum for the original set is $\log4=2$, so the relative entropy is $\tfrac78$. Translating binary pairs 00, 01, 10, 11 into A′, B′, C′, D′ re-encodes into the same symbols with compression ratio $\tfrac78$ (p. 18, 19).
- **Example 2.** A's with probability $p$, B's with $q$, $p\ll q$:
$$H=-\log p^p(1-p)^{1-p}=-p\log p(1-p)^{(1-p)/p}\doteq p\log\frac ep.$$
A fairly good code sends a special sequence (say 0000) for the rare A, followed by the binary count of B's after it, with numbers containing the special sequence deleted. Numbers up to 16 are normal; 16 is represented by 17 = 10001. Shannon says it can be shown that as $p\to0$ the coding approaches the ideal if the special sequence length is adjusted (p. 19).

### Part II — The discrete channel with noise

### 11. Representation of a noisy discrete channel (p. 19)
- If a transmitted signal always gives the same received signal, the effect is *distortion*. If this function has an inverse, distortion can be undone in principle. The case of interest is where the change varies: the received signal $E$ is a function of the signal $S$ and a chance variable noise $N$, $E=f(S,N)$ (p. 19).
- General noisy channel: finitely many states and probabilities $p_{\alpha,i}(\beta,j)$, the probability that, in state $\alpha$ with symbol $i$ sent, symbol $j$ is received and the channel goes to state $\beta$. With independent perturbations there is one state and transition probabilities $p_i(j)$ (p. 19).
- Entropies: $H(x)$ (input), $H(y)$ (output), $H(x,y)$ (joint), $H_x(y)$ (output given input), $H_y(x)$ (input given output), with
$$H(x,y)=H(x)+H_x(y)=H(y)+H_y(x).$$
In the noiseless case $H(y)=H(x)$ (p. 19).

### 12. Equivocation and channel capacity (pp. 20–22)
- **Setup.** Two equiprobable symbols at 1000 per second give a source of 1000 bits/s. Noise makes 1 in 100 wrong (p. 20).
  - **Rejected first impulse:** subtract expected errors to get 990 bits/s. This fails, since the recipient does not know where errors are. If noise were total (output independent of input), half the symbols would be right by chance, giving "credit" for 500 bits/s though no information is sent; a coin flipped at the receiver would do equally well (p. 20).
- **Equivocation.** The correction is the information missing in the received signal, measured by $H_y(x)$ and called the *equivocation* (average ambiguity of the received signal). The rate of transmission is
$$R=H(x)-H_y(x).$$
- Example: given 0 received, the posterior probabilities are .99 (0 sent) and .01 (1 sent). So $H_y(x)=-[.99\log.99+.01\log.01]=.081$ bits/symbol, i.e. 81 bits/s. The rate is $1000-81=919$ bits/s. In the total-noise case $H_y(x)=1$ bit/symbol, so $R=0$ (p. 20).
- **Theorem 10.** An observer sees both sent and recovered messages and sends correction data over a "correction channel" (Fig. 8). If that channel has capacity $H_y(x)$, the data can be encoded so that all but an arbitrarily small fraction $\epsilon$ of errors are corrected. This is not possible if the capacity is less than $H_y(x)$ (p. 20).
- *Proof, first part:* for long received sequences $M'$, about $2^{TH_y(x)}$ original messages $M$ could have produced each, so $TH_y(x)$ binary digits per $T$ seconds must be sent. A channel of capacity $H_y(x)$ can do this with frequency $\epsilon$ of errors (p. 21).
- *Proof, second part:* for any discrete chance variables, $H_y(x,z)\ge H_y(x)$. Expanding the left side,
$$H_y(z)+H_{yz}(x)\ge H_y(x)\ \Rightarrow\ H_{yz}(x)\ge H_y(x)-H_y(z)\ge H_y(x)-H(z).$$
Take $x$ = source output, $y$ = received signal, $z$ = the signal on the correction channel. The right side is the equivocation less the rate on the correction channel. If the capacity is below the equivocation it is positive, so $H_{yz}(x)>0$ and the error frequency cannot be arbitrarily small (p. 21).
- Example: random errors with probability $p$ per binary digit, with their positions known. The correction channel needs capacity $-[p\log p+q\log q]$, which is the equivocation (p. 21).
- **Equivalent forms of the rate:**
$$R=H(x)-H_y(x)=H(y)-H_x(y)=H(x)+H(y)-H(x,y).$$
They mean: information sent minus uncertainty of what was sent; amount received minus the part due to noise; in a sense the number of bits per second the two have in common (p. 22).
- **Capacity of a noisy channel:**
$$C=\max\big(H(x)-H_y(x)\big),$$
the maximum over all input sources. For a noiseless channel $H_y(x)=0$, and this reduces to the earlier definition (p. 22).

> **Intuition note.** Counting only the matches between sent and received symbols over-credits a noisy channel. The right deduction is the leftover uncertainty about what was sent. Capacity is the best rate after this deduction, over all ways of feeding the channel.

### 13. The fundamental theorem for a discrete channel with noise (pp. 22–24)
- **Expectation rejected:** Shannon notes one would expect that driving the error probability to zero requires the redundancy to grow indefinitely and the rate to fall to zero; he says this is by no means true (p. 22). Instead it is possible to send at rate $C$ with as small a frequency of errors or equivocation as desired. This is not true for any greater rate: at $C+R_1$ there is necessarily an equivocation at least $R_1$. "Nature takes payment by requiring just that much uncertainty" (p. 22).
- Fig. 9 plots input entropy (horizontal) against equivocation (vertical). Points in the shaded region above the heavy line (slope 1.0, starting at $C$) can be attained, those below cannot. Points on the line cannot in general be attained, but "there will usually be two points on the line that can" (p. 22).
- **Theorem 11.** Let the channel have capacity $C$ and the source entropy per second $H$.
  - If $H\le C$, there is a coding system giving arbitrarily small error frequency (or equivocation).
  - If $H>C$, one can encode so that the equivocation is less than $H-C+\epsilon$, $\epsilon$ arbitrarily small.
  - No method gives an equivocation less than $H-C$ (p. 22).
- **Proof of the first part** (pp. 23–24). It is by averaging over codes, not by exhibiting a code: if the average error frequency over a group is $<\epsilon$, at least one member is $<\epsilon$.
  - Let $S_0$ be a source achieving (or approaching) the maximum $C$. For long duration $T$ (Fig. 10): the transmitted sequences have a high-probability group of about $2^{TH(x)}$ members; the received sequences have about $2^{TH(y)}$; each high-probability output could come from about $2^{TH_y(x)}$ inputs (and each input has about $2^{TH_x(y)}$ reasonable effects). The $\epsilon,\delta$ errors vanish as $T$ grows and $S_0$ nears the maximizer (p. 23).
  - Take another source with rate $R<C$, so $2^{TR}$ high-probability messages. Assign them at random to the $2^{TH(x)}$ high-probability inputs. A given point is a message with probability $2^{T(R-H(x))}$. The probability that no other point in the fan of $2^{TH_y(x)}$ possible causes of a received signal is a message is
$$P=\big[1-2^{T(R-H(x))}\big]^{2^{TH_y(x)}}.$$
  - Since $R<H(x)-H_y(x)$, write $R-H(x)=-H_y(x)-\eta$ with $\eta>0$:
$$P=\big[1-2^{-TH_y(x)-T\eta}\big]^{2^{TH_y(x)}}\ \to\ 1-2^{-T\eta}\quad(T\to\infty).$$
  - So the error probability tends to zero (p. 24).
- *Second part:* send only $C$ bits per second of the source and ignore the rest. The neglected part gives equivocation $H(x)-C$, and the transmitted part adds only $\epsilon$ (p. 24).
- *Third part:* suppose $H(x)=C+a$ were encoded with equivocation $H_y(x)=a-\epsilon$, $\epsilon>0$. Then $H(x)-H_y(x)=C+\epsilon$, contradicting the definition of $C$ as the maximum (p. 24).
- Author's remark: more is proved. If the average of a set of numbers is within $\epsilon$ of their maximum, at most a fraction $\sqrt\epsilon$ can lie more than $\sqrt\epsilon$ below it, so almost all codes are close to ideal (p. 24).

> **Intuition note.** Each received signal could have come from about $2^{TH_y(x)}$ inputs. If the messages are scattered at random thinly enough (rate below $C$), it is very unlikely that two of them land in the same fan. A random code is therefore good on average, so a good code must exist.

### 14. Discussion (pp. 24–25)
- The proof is not a pure existence proof but has some of the deficiencies of such proofs: following it is generally impractical. Apart from rather trivial cases and certain limiting situations, no explicit series of approximations to the ideal is known. Shannon thinks this is probably related to the difficulty of constructing a good approximation to a random sequence (p. 24).
- A near-ideal code adds redundancy suited to the noise structure, so that noise does not bring a signal closer to another reasonable signal. Any redundancy in the source will usually help combat noise if it is utilized at the receiving point. E.g. a noiseless telegraph channel could save about 50% of the time by proper coding of English, but English redundancy is kept, so many letters can be wrong and still recovered from context (p. 24).
- Delay now also lets a large sample of noise affect the signal before a decision is made (p. 25).
- **Theorem 12.** Let $N(T,q)$ be the maximum number of length-$T$ signals, each used with equal probability, that can be chosen so that a most-probable-cause receiver errs with probability $\le q$. Then
$$\lim_{T\to\infty}\frac{\log N(T,q)}{T}=C\qquad(q\ne0,1).$$
So reliably distinguishable messages correspond to about $CT$ bits. Compare the noiseless capacity definition of §1 (p. 25).

### 15. Example of a discrete channel and its capacity (pp. 25–26)
- Fig. 11: three symbols. The first is never disturbed. The second and third each arrive correctly with probability $p$ and are swapped with probability $q$. Let $\alpha=-[p\log p+q\log q]$, and $P,Q$ be the probabilities of using the first symbol and each of the other two. Then
$$H(x)=-P\log P-2Q\log Q,\qquad H_y(x)=2Q\alpha.$$
- Maximize $H(x)-H_y(x)$ subject to $P+2Q=1$ using
$$U=-P\log P-2Q\log Q-2Q\alpha+\lambda(P+2Q).$$
The conditions are
$$\frac{\partial U}{\partial P}=-1-\log P+\lambda=0,\qquad \frac{\partial U}{\partial Q}=-2-2\log Q-2\alpha+2\lambda=0.$$
- Eliminating $\lambda$ gives $\log P=\log Q+\alpha$, so $P=Qe^\alpha=Q\beta$. With the constraint,
$$P=\frac\beta{\beta+2},\qquad Q=\frac1{\beta+2},\qquad C=\log\frac{\beta+2}\beta.$$
- (added step) With base-2 logs the factor $e^\alpha$ becomes $2^\alpha$; the author's check $\beta=2$ at $p=\tfrac12$ matches $\alpha=1$ bit. (added step) At the optimum, $H-H_y=-(P+2Q)\log Q-(P+2Q)\alpha=-\log Q-\alpha=\log\frac{\beta+2}\beta$ with $\alpha=\log\beta$, which agrees with $C$.
- Checks: $p=1$: $\beta=1$, $C=\log3$ (noiseless, three symbols). $p=\tfrac12$: $\beta=2$, $C=\log2$ (symbols 2 and 3 are indistinguishable and act as one; $P=\tfrac12$, and the other half may be split between them in any way). For intermediate $p$, $C$ lies between $\log2$ and $\log3$, and the noise-free first symbol is used somewhat more often (p. 26).

### 16. The channel capacity in certain special cases (pp. 26–27)
- With independent noise on successive symbols, transition probabilities $p_{ij}$, the rate to maximize is
$$-\sum_{i,j}P_ip_{ij}\log\sum_iP_ip_{ij}+\sum_{i,j}P_ip_{ij}\log p_{ij},\quad\sum P_i=1.$$
- The Lagrange method gives
$$\sum_jp_{sj}\log\frac{p_{sj}}{\sum_iP_ip_{ij}}=\mu,\qquad s=1,2,\dots$$
Multiplying by $P_s$ and summing shows $\mu=C$.
- If the (square) matrix $[p_{sj}]$ has an inverse $[h_{st}]$ with $\sum_sh_{st}p_{sj}=\delta_{tj}$, then
$$\sum_{s,j}h_{st}p_{sj}\log p_{sj}-\log\sum_iP_ip_{it}=C\sum_sh_{st},$$
so
$$\sum_iP_ip_{it}=\exp\Big[-C\sum_sh_{st}+\sum_{s,j}h_{st}p_{sj}\log p_{sj}\Big],\qquad P_i=\sum_th_{it}\exp\Big[-C\sum_sh_{st}+\sum_{s,j}h_{st}p_{sj}\log p_{sj}\Big].$$
$C$ is fixed by $\sum P_i=1$; then $C$ is the capacity and the $P_i$ are the capacity-achieving probabilities (p. 26).
- If every input symbol has the same set of outgoing probabilities and every output symbol the same set of incoming ones (Fig. 12), $H_x(y)=-\sum p_i\log p_i$ does not depend on the input distribution. The maximum of $H(y)$ is $\log m$ ($m$ output symbols; equiprobable inputs make outputs equiprobable). So
$$C=\log m+\sum p_i\log p_i.$$
- Fig. 12 values: (a) $C=\log4-\log2=\log2$, achieved by using only the 1st and 3rd symbols; (b) $C=\log4-\tfrac23\log3-\tfrac13\log6=\log4-\log3-\tfrac13\log2=\log\tfrac13 2^{5/3}$; (c) $C=\log3-\tfrac12\log2-\tfrac13\log3-\tfrac16\log6=\log\dfrac3{2^{1/2}3^{1/3}6^{1/6}}$ (p. 27).
- If symbols form groups never confused with each other, with group capacities $C_n$ (alone), Shannon says it is easily shown that the best group probabilities and capacity are
$$P_n=\frac{2^{C_n}}{\sum2^{C_n}},\qquad C=\log\sum2^{C_n}.$$
Within a group the probabilities are as if the group were used alone (p. 27).

### 17. An example of efficient coding (pp. 27–28)
- Two symbols, noise acting on blocks of seven: a block is sent correctly or has exactly one wrong symbol; the eight possibilities are equally likely. Then
$$C=\max[H(y)-H_x(y)]=\tfrac17\big[7+\tfrac88\log\tfrac18\big]=\tfrac47\text{ bits/symbol}.$$
- Code (Hamming's method): in a block $X_1,\dots,X_7$, $X_3,X_5,X_6,X_7$ are message symbols chosen freely. $X_4,X_2,X_1$ are redundant, set to make the following sums even (p. 28):
$$\alpha=X_4+X_5+X_6+X_7,\qquad \beta=X_2+X_3+X_6+X_7,\qquad \gamma=X_1+X_3+X_5+X_7.$$
- At the receiver, compute $\alpha,\beta,\gamma$ (even = 0, odd = 1). The binary number $\alpha\beta\gamma$ is the subscript of the wrong $X_i$ (0 = no error) (p. 28). Shannon says this code, in an example he calls "somewhat unrealistic", allows complete correction of errors and transmits at rate $C$ (p. 27).

### Appendix 1 — Growth of the number of blocks with a finite state condition (p. 28)
- Let $N_i(L)$ be the number of blocks of length $L$ ending in state $i$, with
$$N_j(L)=\sum_{i,s}N_i\big(L-b_{ij}^{(s)}\big).$$
These are linear difference equations (each value is a fixed linear combination of earlier values); the asymptotic behavior is $N_j=A_jW^L$.
- Substituting: $A_jW^L=\sum_{i,s}A_iW^{L-b_{ij}^{(s)}}$, i.e. $A_j=\sum_{i,s}A_iW^{-b_{ij}^{(s)}}$, i.e.
$$\sum_i\Big(\sum_sW^{-b_{ij}^{(s)}}-\delta_{ij}\Big)A_i=0.$$
- For a nonzero solution the determinant $D(W)=\big|\sum_sW^{-b_{ij}^{(s)}}-\delta_{ij}\big|$ must vanish. This fixes $W$ as the largest real root of $D=0$. Then
$$C=\lim_{L\to\infty}\frac{\log\sum A_jW^L}{L}=\log W.$$
The same growth results if all blocks start in the same, arbitrarily chosen, state (p. 28).

### Appendix 2 — start (p. 28)
- Only the opening is in this part: let $H(\tfrac1n,\dots,\tfrac1n)=A(n)$. Condition (3) lets a choice among $s^m$ equally likely possibilities be split into $m$ choices from $s$, so $A(s^m)=mA(s)$ (p. 28). The rest of the derivation lies beyond this unit.

## Toy example (ours, not from the text)
**Source.** Letters X, Y, Z with probabilities $\tfrac12,\tfrac14,\tfrac14$, independent.

**Entropy.** $H=-(\tfrac12\log_2\tfrac12+\tfrac14\log_2\tfrac14+\tfrac14\log_2\tfrac14)=0.5+0.5+0.5=1.5$ bits/symbol.

**Code by the second proof of Theorem 9** (single symbols, $N=1$). Order: X, Y, Z with $p=\tfrac12,\tfrac14,\tfrac14$. Cumulative $P_s$: $0,\ \tfrac12,\ \tfrac34$. The integer $m_s$ satisfies $\log_2(1/p_s)\le m_s<1+\log_2(1/p_s)$:
- X: $1\le m<2$, so $m=1$.
- Y: $2\le m<3$, so $m=2$.
- Z: $2\le m<3$, so $m=2$.

Binary expansions: $0=0.0\to$ "0"; $\tfrac12=0.10\to$ "10"; $\tfrac34=0.11\to$ "11". Average length $=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac14\cdot2=1.5=H$. So $G_1\le H'<G_1+1$ holds with $H'=H$.

**Typical sequences.** For $N=10$ there are $3^{10}=59049\approx2^{15.85}$ sequences, but about $2^{HN}=2^{15}=32768$ typical ones, each with probability about $2^{-15}$.

**Noisy channel.** Binary input, equiprobable, each symbol flipped with probability .1. Given a received symbol, the posteriors are .9 and .1, so
$$H_y(x)=-[.9\log_2.9+.1\log_2.1]=.9(0.1520)+.1(3.3219)=0.1368+0.3322\approx0.469.$$
$R=H(x)-H_y(x)=1-0.469=0.531$ bits/symbol. Every input has the same outgoing probabilities and every output the same incoming ones, so §16 gives $C=\log_2 2+(.9\log_2.9+.1\log_2.1)=1-0.469=0.531$. By Theorem 11, rates below 0.531 bits/symbol can be sent with arbitrarily small error, but a source of 1 bit/symbol must suffer equivocation of at least $1-0.531=0.469$.

## Concepts
- [[bit]] — unit from base-2 logarithm; $N$ two-state devices store $N$ bits (p. 1)
- [[entropy]] — $H=-\sum p_i\log p_i$ (Shannon: choice/uncertainty); $K$ only sets the unit (p. 11)
- [[self-information]] — used implicitly as $\log 1/p$ of a long message, with $\frac{\log1/p}N\doteq H$ (p. 13)
- [[joint-and-conditional-entropy]] — $H(x,y)$, $H_x(y)$ (conditional entropy of $y$ given $x$) (p. 12)
- [[chain-rule]] — $H(x,y)=H(x)+H_x(y)$ (p. 12)
- [[mutual-information]] — not named here; the rate $R=H(x)-H_y(x)=H(y)-H_x(y)=H(x)+H(y)-H(x,y)$ is, in a sense, the bits per second common to input and output (p. 22)
- [[redundancy]] — $1-$relative entropy; for English about 50% (considering structure up to about eight letters) (p. 14)
- [[entropy-rate]] — $H$ per symbol and $H'=mH$ per second; $F_N,G_N\to H$ (pp. 13–14)
- [[typical-set-aep]] — Theorems 3–4: about $2^{HN}$ sequences of probability about $2^{-HN}$ (pp. 13–14) (canon link; not stated in this unit)
- [[source-coding-theorem]] — Theorem 9 gives rate $C/H-\epsilon$, never above $C/H$ (p. 16)
- [[huffman-arithmetic-coding]] — (canon link; not stated in this unit: Huffman coding is not named; this is a Shannon–Fano-type code) here the cumulative-probability binary code and Fano's method, substantially the same apart from minor differences (p. 17); the 0/10/110/111 code (p. 18)
- [[noisy-channel]] — $E=f(S,N)$ with probabilities $p_{\alpha,i}(\beta,j)$ (p. 19)
- [[channel-capacity]] — noiseless: $\lim\log N(T)/T$ (p. 3); noisy: $\max[H(x)-H_y(x)]$ (p. 22)
- [[noisy-channel-coding-theorem]] — Theorem 11 (and Theorem 12) (pp. 22, 25)
- [[error-correcting-code]] — the 7-symbol Hamming example (p. 28)
- [[maximum-entropy-principle]] — (canon link; the principle is not stated in this unit) in §10, use the maximum-entropy source subject to the statistical conditions one chooses to retain (p. 18)
- [[equivocation]] (new) — $H_y(x)$: average ambiguity of the received signal about what was sent (p. 20)
- [[relative-entropy-shannon]] (new) — author's meaning: $H/H_{\max}$ for the same symbols. **Not** the KL divergence of the canon list (p. 14)
- [[markoff-source]] (new) — finite-state source with transition probabilities $p_i(j)$, one symbol per transition (p. 8)
- [[ergodic-source]] (new) — statistically homogeneous source; sequence averages equal ensemble averages with probability one (pp. 8–10)
- [[discrete-transducer]] (new) — finite-state encoder/decoder $y_n=f(x_n,\alpha_n)$, $\alpha_{n+1}=g(x_n,\alpha_n)$ (p. 15)

## Canonical instances
- [[telegraph-channel]] — dot/dash/space channel with $C=0.539$ (p. 4)
- [[english-approximations]] — zero- to third-order letter and first/second-order word approximations (p. 7)
- [[three-letter-markov-source]] — example C with its $p_i(j)$, $p(i)$, $p(i,j)$ tables (p. 6)
- [[abcd-source-7-4]] — $H=\tfrac74$, code 0/10/110/111 (p. 18)
- [[binary-error-1-percent]] — 1000 sym/s, 1% errors, 919 bits/s (p. 20)
- [[three-symbol-channel-fig11]] — $C=\log\frac{\beta+2}\beta$ (pp. 25–26)
- [[hamming-7-4-block-channel]] — $C=\frac47$, parity checks $\alpha,\beta,\gamma$ (pp. 27–28)
- [[crossword-redundancy]] — if constraints are chaotic and random, large 2D puzzles are just possible at 50% redundancy and 3D puzzles should be possible at 33% (p. 15)

## Bridges (candidates)
- [same-math] $H=-\sum p_i\log p_i$ ↔ statistical mechanics: entropy over cells of phase space, Boltzmann's $H$ — the author notes the same form (p. 11)
- [structural-analogy] $F_N$ (conditional entropy of next symbol given $N-1$ previous) ↔ language modelling: $n$-gram context models — same idea of predicting the next token from limited history
- [structural-analogy] Ergodicity (one long sequence represents the ensemble) ↔ social-science time-series estimation: inferring population properties from a single long record
- [structural-analogy] Random-coding proof (average over codes, so one good code exists) ↔ probabilistic existence arguments
- [metaphor] Matching encoder to channel like transformer matching generator to load (author's own analogy, p. 17)
- [structural-analogy] Channel capacity as a limit on reliable information rate ↔ rational inattention: agents with a bound on absorbed information

## Questions this raises
- Why does the equivocation $H_y(x)$ of the channel, not the raw error rate, set the cost of correcting errors (Theorem 10)?
- Shannon says the random-coding proof gives no practical code. What would an explicit code approaching $C$ require?
- How should $H$ be extended to continuous messages, where the number of possibilities is infinite (promised in the second half, p. 3)?
- How good is the estimate "redundancy of English about 50%" when only structure up to about eight letters is counted (p. 14)?

## Reading notes
- **Scope:** printed pages 1–28 (printed = pdf). The unit starts at the title and Introduction (p. 1). It contains Part I (§§1–10, pp. 3–19), Part II §§11–17 (pp. 19–28), Appendix 1 (p. 28), and ends on p. 28 inside Appendix 2 after the line $A(s^m)=mA(s)$. The rest of Appendix 2 (Theorem 2), Appendix 3 (Theorems 3–6), Appendix 4 (Theorem 8) and the continuous-case sections are in the other part. The proof of Theorem 7 is in the text (p. 15).
- Page header: "Reprinted with corrections from The Bell System Technical Journal, Vol. 27, pp. 379–423, 623–656, July, October, 1948." Footnote 9 on p. 17 cites an M.I.T. report dated 17 March 1949, later than the 1948 date in the header.
- The text layer drops or garbles many symbols (inequality signs, $\Sigma$, Greek letters, minus signs). All formulas here were checked against the page images.
- Notation: on p. 16 the low-probability group has "total probability less than $\mu$", but the rate expression uses $\delta$. I read $\delta$ as that probability. On p. 25, "$P=Qe^\alpha=Q\beta$" implies $\beta=e^\alpha$ (natural logs); with base-2 logs the author's check $\beta=2$ at $p=\tfrac12$ corresponds to $2^\alpha$.
- Shannon's "relative entropy" (p. 14) is $H/H_{\max}$, not the KL divergence.
- In §12 the equivocation notation is $H_y(x)$ (input given output) as in the paper; "$M'$" in Fig. 8 is the received message.
- The converse of Theorem 11 is stated for rates above $C$; the direct-part proof treats $R<C$ strictly (p. 23).
- Theorem 12 is stated without proof in this part.
