---
id: mackay-2003-information/ch25-exact
work: mackay-2003-information
unit: "25 Exact Marginalization in Trellises"
pages: 324-333
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
# Exact Marginalization in Trellises

## L0 — One line
For a linear code drawn as a trellis, message passing (local computations passed along the graph) can find the most probable codeword (min–sum, with work equal to the number of edges) and each bit's exact posterior (sum–product) without listing all codewords; how much is saved depends on the code.

## L1 — The gist (≤ 120 words)
Given a received signal from a noisy memoryless channel, how do we decode a linear (N, K) code exactly? Brute force sums over all 2^K codewords. MacKay redraws the code as a trellis, a layered graph in which each left-to-right path is a codeword. Then two message-passing algorithms do the work. Min–sum (Viterbi) finds the MAP codeword, the most probable one given the received signal. Sum–product (forward–backward, BCJR) gives each bit's exact posterior marginal. For min–sum the cost equals the number of trellis edges. How much this saves depends on the code; bit order can matter. MAP decoding of a general linear code is known to be NP-complete (in layman's terms, cost growing exponentially with blocklength).

**Prerequisites:** Bayes' theorem; marginalization (summing out variables); linear codes, generator and parity-check matrices, syndromes (Chapters 1, 11); the min–sum idea (Chapter 16).

## L2 — Key ideas
- There are two decoding problems. Codeword decoding infers which codeword was sent. Bitwise decoding infers, for each bit, the probability that it was 1 (p. 324).
- For a memoryless channel the likelihood factorises, $P(\mathbf y\mid\mathbf t)=\prod_n P(y_n\mid t_n)$. For decoding only the likelihood ratio $P(y_n\mid t_n{=}1)/P(y_n\mid t_n{=}0)$ matters (pp. 324–325).
- Bitwise decoding is a marginalization over codewords. Done naively it takes exponential time (p. 326).
- A trellis is a layered graph whose left-to-right paths are the codewords. A minimal trellis has the fewest nodes, and its width is a power of two, at most $2^K$ (p. 327).
- Min–sum on the trellis, with edge costs $-\log P(y_n\mid t_n)$, finds the MAP codeword in a number of operations equal to the number of edges. It is the Viterbi algorithm (p. 329).
- Sum–product replaces (min, +) by (+, ×). Forward messages $\alpha$ and backward messages $\beta$ give the bit posteriors (pp. 329–330).
- MAP decoding and bitwise decoding can disagree. Thresholding then decoding is not optimal (pp. 328, 333).
- Trellises are built from a generator matrix in trellis-oriented form (row spans start in different columns and end in different columns), or from a parity-check matrix via partial syndromes (the parity-check matrix times the bits generated so far). Reordering bits can shrink the trellis (pp. 331–333).

## L3 — Walkthrough

### 25.1 Decoding problems (pp. 324–326)
A codeword $\mathbf t$ from a linear (N, K) code is sent over a memoryless channel (for example Gaussian). The received signal is $\mathbf y$ (p. 324).
- **Codeword decoding:** infer which $\mathbf t$ was sent.
- **Bitwise decoding:** for each $t_n$, infer how likely it was a 1 rather than a 0 (p. 324).

**Codeword posterior.** By Bayes' theorem (p. 324):
$$P(\mathbf t\mid \mathbf y)=\frac{P(\mathbf y\mid\mathbf t)P(\mathbf t)}{P(\mathbf y)}\tag{25.1}$$
The likelihood is separable for any memoryless channel:
$$P(\mathbf y\mid\mathbf t)=\prod_{n=1}^N P(y_n\mid t_n)\tag{25.2}$$
For a Gaussian channel with transmissions $\pm x$ and noise standard deviation $\sigma$ (p. 325):
$$P(y_n\mid t_n{=}1)=\tfrac{1}{\sqrt{2\pi\sigma^2}}\exp\!\Big(-\tfrac{(y_n-x)^2}{2\sigma^2}\Big)\tag{25.3}$$
$$P(y_n\mid t_n{=}0)=\tfrac{1}{\sqrt{2\pi\sigma^2}}\exp\!\Big(-\tfrac{(y_n+x)^2}{2\sigma^2}\Big)\tag{25.4}$$
For decoding, only the likelihood ratio matters:
$$\frac{P(y_n\mid t_n{=}1)}{P(y_n\mid t_n{=}0)}=\exp\!\Big(\frac{2xy_n}{\sigma^2}\Big)\tag{25.5}$$
Exercise 25.1 asks the reader to show that this makes the Gaussian channel equivalent to a time-varying binary symmetric channel with known noise level $f_n$ (p. 325).

The prior $P(\mathbf t)$ is usually uniform over valid codewords. The normaliser is $P(\mathbf y)=\sum_{\mathbf t}P(\mathbf y\mid\mathbf t)P(\mathbf t)$ (25.6) (p. 325).

**MAP codeword decoding.** The full answer lists all $2^K$ codewords and their probabilities. Since $2^K$ is often very large, we often restrict attention to the most probable codeword. With a uniform prior this equals maximum-likelihood decoding (p. 325). Searching all codewords takes time of order $2^K$. The min–sum algorithm (section 25.3) may do better, depending on the code (p. 325). MacKay states that MAP decoding for a *general* linear code is NP-complete, so restricting to MAP "hasn't necessarily made the task much less challenging" (p. 325).

**Bitwise decoding.** The exact solution marginalizes over the other bits:
$$P(t_n\mid\mathbf y)=\sum_{\{t_{n'}:n'\neq n\}}P(\mathbf t\mid\mathbf y)\tag{25.7}$$
Equivalently, with the truth function $\mathbb 1[S]$ (1 if $S$ is true, else 0) (p. 326):
$$P(t_n{=}1\mid\mathbf y)=\sum_{\mathbf t}P(\mathbf t\mid\mathbf y)\,\mathbb 1[t_n{=}1]\tag{25.8}$$
$$P(t_n{=}0\mid\mathbf y)=\sum_{\mathbf t}P(\mathbf t\mid\mathbf y)\,\mathbb 1[t_n{=}0]\tag{25.9}$$
An explicit sum over codewords takes exponential time. For certain codes, the forward–backward algorithm (an instance of sum–product) is much faster (p. 326).

*Intuition note:* Decoding is Bayesian inference over a list of $2^K$ hypotheses. The trellis is a way to avoid writing that list out.

### 25.2 Codes and trellises (pp. 326–327)
For a systematic block code, the first K bits are source bits and the other $M=N-K$ are parity bits. The matrices are
$$\mathbf G^{\mathsf T}=\begin{bmatrix}\mathbf I_K\\ \mathbf P\end{bmatrix}\tag{25.10}$$
$$\mathbf H=\begin{bmatrix}\mathbf P&\mathbf I_M\end{bmatrix}\tag{25.11}$$
where $\mathbf P$ is $M\times K$ (p. 326). Trellises in general give non-systematic codes. These can be made systematic by reordering bits (p. 326).

**Definition (narrow, p. 326).** A trellis is a graph of nodes (states, vertices) and edges. Nodes are grouped into vertical slices called times. Each edge joins neighbouring times and carries a symbol. The leftmost and rightmost times each hold one node. Every other node has at least one edge leftwards and one rightwards.

A trellis with $N+1$ times defines a code of blocklength $N$. A left-to-right path read off through its edge symbols is a codeword. Times are numbered $0,\dots,N$. States are numbered from 0 (start) to $I$ (end). Bit $n$ is emitted between time $n-1$ and time $n$ (p. 327).

Width is the number of nodes at a time. A linear trellis defines a linear code. Only linear, binary trellises are discussed (p. 327). Figure 25.1 shows trellises for the repetition code $R_3$ with (N, K) = (3, 1), the parity code $P_3$ with (3, 2), and the (7, 4) Hamming code (p. 327).

**Observations about minimal trellises** (the one with fewest nodes) (p. 327):
- Each node has at most two edges in and at most two out.
- All nodes at one time share the same left degree, and the same right degree.
- Width is always a power of two.
- Width cannot exceed $2^K$, because every node lies on at least one of the $2^K$ codewords.
- MacKay also says the width is "everywhere less than $2^M$", to be proved in 25.4.
- In figure 25.1, $K$ is the number of binary branch points met going across.

### 25.3 Solving the decoding problems on a trellis (pp. 327–330)
The trellis is a causal story of how a codeword arises, with time running left to right. At each divergence a random source picks the branch. The receiver sees noisy edge labels. It wants (a) the most probable path (codeword decoding) and (b) the probability that bit $n$ was 0 or 1 (bitwise decoding) (p. 327).

**Example 25.3 (Hamming (7,4)).** The normalized likelihoods are $(0.1,0.4,0.9,0.1,0.1,0.1,0.3)$. Each is a ratio such as $P(y_1\mid x_1{=}1)/P(y_1\mid x_1{=}0)=0.1/0.9$ (25.12) (p. 328).
1. Thresholding at 0.5 gives $\mathbf r=(0,0,1,0,0,0,0)$. The binary-symmetric-channel decoder then outputs $\hat{\mathbf t}=0000000$. MacKay calls this not optimal; optimal inference always uses Bayes' theorem (p. 328).
2. Enumerating all 16 codewords (figure 25.2) shows that the most probable codeword is $0110001$ with posterior 0.63. This is more than twice that of $0000000$, which has 0.25 (p. 328).
3. The bit marginals (figure 25.3) are $P(t_n{=}1\mid\mathbf y)=0.061,\,0.674,\,0.746,\,0.061,\,0.061,\,0.061,\,0.659$ for $n=1..7$. Bits 1, 4, 5, 6 are confidently 0. Bits 2, 3, 7 are less certain (pp. 328–329).

Here the MAP codeword agrees with bit-by-bit decoding, but not always (p. 328). In Exercise 25.4's solution the likelihoods are $(0.2,0.2,0.9,0.2,0.2,0.2,0.2)$. The MAP codeword is $0000000$ (posterior 0.3006). The bitwise decoding is $0010000$, which is not a codeword (p. 333).

**Min–sum algorithm.** A codeword's log likelihood is the sum of bitwise log likelihoods, like the cost of a journey. Flip the sign to get a cost to minimize. Put cost $-\log P(y_n\mid t_n)$ on each edge. The min–sum algorithm of section 16.3 then finds the most probable codeword in a number of operations equal to the number of edges. It is also known as the Viterbi algorithm (p. 329).

**Sum–product algorithm.** This is a small modification of min–sum. Edge costs become likelihoods $P(y_n\mid t_n)$, and (min, sum) becomes (sum, product). Messages then mean "probability of the data up to here" instead of "cost of the best route" (p. 329). Notation: $i$ runs over nodes, 0 is the start, $\mathcal P(i)$ is the set of parents of $i$, and $w_{ij}$ is the likelihood on the edge from $j$ to $i$.

Forward pass (left to right):
$$\alpha_0=1,\qquad \alpha_i=\sum_{j\in\mathcal P(i)}w_{ij}\alpha_j\tag{25.13}$$
- Exercise 25.5: $\alpha_i$ is proportional to the joint probability that the path passes through $i$ and the first $n$ received symbols were $y_1..y_n$.
- $\alpha_I$ at the end node is proportional to the marginal probability of the data. Exercise 25.6 gives the constant as $2^K$ (p. 330).

Backward pass (right to left), with $I$ the end node:
$$\beta_I=1,\qquad \beta_j=\sum_{i:\,j\in\mathcal P(i)}w_{ij}\beta_i\tag{25.14}$$
Exercise 25.7: $\beta_i$ is proportional to the conditional probability of the later symbols $y_{n+1}..y_N$, given that the path passed through $i$ (p. 330).

Bit posteriors. Let $i$ run over nodes at time $n$, $j$ over nodes at time $n-1$, and $t_{ij}$ be the bit on edge $j\to i$. For $t=0,1$:
$$r_n^{(t)}=\sum_{i,j:\,j\in\mathcal P(i),\,t_{ij}=t}\alpha_j w_{ij}\beta_i\tag{25.15}$$
$$P(t_n=t\mid\mathbf y)=\frac1Z\,r_n^{(t)},\quad Z=r_n^{(0)}+r_n^{(1)}\tag{25.16}$$
$Z$ should equal the final forward message $\alpha_I$ (p. 330). Exercise 25.8 asks for confirmation that this computes $P(t_n=t\mid\mathbf y)$. The algorithm is also called forward–backward, BCJR, or belief propagation (p. 330).

*Intuition note:* $\alpha$ summarises everything to the left of a node, and $\beta$ everything to the right. Multiplying them with the edge likelihood between gives, up to normalisation, the total probability of all codewords using that edge, without listing the codewords.

**Exercise 25.9 solution ($P_3$, likelihoods in table 25.4).** The MAP codeword is 101 with likelihood 1/8. $Z=\alpha_I=3/16$. The intermediate $\alpha_i$ (left to right) are $1/2,1/4,5/16,4/16$ and the intermediate $\beta_i$ (right to left) are $1/2,1/8,9/32,3/16$. The codeword probabilities are $1/12,\,2/12,\,1/12,\,8/12$ for 000, 011, 110, 101. The bitwise results are $3/4$, $1/4$, $5/6$ for $P(t_n{=}1\mid\mathbf y)$, $n=1,2,3$ (p. 333).

### 25.4 More on trellises (pp. 331–333)
MacKay says this section may be skipped (p. 331).

**Span and trellis-oriented form.** The span of a codeword runs from its first non-zero bit to its last non-zero bit, inclusive. For example, $0001011$ has span $0001111$ (table 25.5). A generator matrix is in trellis-oriented form if the row spans all start in different columns and all end in different columns (p. 331).

**Trellis from a generator matrix.** First put $\mathbf G$ in trellis-oriented form by row operations like Gaussian elimination. The Hamming generator matrix (rows are codewords, shape $K\times N=4\times7$)
$$\mathbf G=\begin{bmatrix}1&0&0&0&1&0&1\\0&1&0&0&1&1&0\\0&0&1&0&1&1&1\\0&0&0&1&0&1&1\end{bmatrix}\tag{25.17}$$
is not in this form, since rows 1, 3, 4 have spans ending in the same column. Subtracting lower rows from upper rows gives an equivalent matrix, one that generates the same codewords:
$$\mathbf G=\begin{bmatrix}1&1&0&1&0&0&0\\0&1&0&0&1&1&0\\0&0&1&1&1&0&0\\0&0&0&1&0&1&1\end{bmatrix}\tag{25.18}$$
Each row defines an (N, 1) subcode with two codewords. Row 1 gives $1101000$ and $0000000$. The minimal trellis of each subcode is easy to draw (figure 25.6, left). Build the full trellis by adding subcodes one at a time. Vertices within the new subcode's span are duplicated. Edge symbols in the original copy stay unchanged. In the second copy, symbols are flipped wherever the new subcode has a 1 (p. 331).

Another (7, 4) Hamming code, a bit permutation of the first, is generated by
$$\mathbf G=\begin{bmatrix}1&1&1&0&0&0&0\\0&1&1&1&1&0&0\\0&0&1&0&1&1&0\\0&0&0&1&1&1&1\end{bmatrix}\tag{25.19}$$
with parity-check matrix
$$\mathbf H=\begin{bmatrix}1&0&1&0&1&0&1\\0&1&1&0&0&1&1\\0&0&0&1&1&1&1\end{bmatrix}\tag{25.20}$$
Its trellis (figure 25.7a) has fewer nodes than that of figure 25.1c. So reordering bits can sometimes give smaller, simpler trellises (p. 332).

**Trellis from a parity-check matrix.** The syndrome of $\mathbf r$ is $\mathbf H\mathbf r$. A vector is a codeword only if its syndrome is zero. While generating a codeword, the state is the partial syndrome, which is $\mathbf H$ times the bits generated so far. Start and end states are the zero syndrome. $\mathbf H$ is $M\times N$, so the syndrome has at most $M$ bits and each time has at most $2^M$ nodes. The trellis is the intersection of two trees of syndrome sequences, one grown from each end. If the vertical coordinate shows the syndrome, horizontal edges are 0-bits and non-horizontal edges are 1-bits, so labels are not needed (pp. 332–333). Figure 25.7b shows the trellis for (25.20).

## Toy example (ours, not from the text)
Repetition code $R_3$ (codewords 000 and 111). Its trellis has start node 0, an upper path $A_1\to A_2$ (bits 0), a lower path $B_1\to B_2$ (bits 1), and end node $I$. Take the edge likelihoods $P(y_n\mid t_n=0)$ and $P(y_n\mid t_n=1)$:
- $n=1$: 0.8 and 0.2
- $n=2$: 0.6 and 0.4
- $n=3$: 0.3 and 0.7

**Forward.** $\alpha_0=1$. $\alpha_{A_1}=0.8$ and $\alpha_{B_1}=0.2$. $\alpha_{A_2}=0.8\times0.6=0.48$ and $\alpha_{B_2}=0.2\times0.4=0.08$. $\alpha_I=0.48\times0.3+0.08\times0.7=0.144+0.056=0.2$.

**Backward.** $\beta_I=1$. $\beta_{A_2}=0.3$ and $\beta_{B_2}=0.7$. $\beta_{A_1}=0.6\times0.3=0.18$ and $\beta_{B_1}=0.4\times0.7=0.28$.

**Bit 2.** $r_2^{(0)}=\alpha_{A_1}\cdot0.6\cdot\beta_{A_2}=0.8\times0.6\times0.3=0.144$. $r_2^{(1)}=0.2\times0.4\times0.7=0.056$. Their sum is $0.2=\alpha_I=Z$, as (25.16) requires. So $P(t_2=1\mid\mathbf y)=0.056/0.2=0.28$.

**Check by enumeration.** $P(000\mid\mathbf y)\propto0.8\times0.6\times0.3=0.144$ and $P(111\mid\mathbf y)\propto0.056$. The posteriors are 0.72 and 0.28. Min–sum (maximum product) picks 000. For this two-codeword code, bitwise and MAP decoding agree.

## Concepts
- [[bayes-theorem]] — gives the codeword posterior $P(\mathbf t\mid\mathbf y)\propto P(\mathbf y\mid\mathbf t)P(\mathbf t)$ (p. 324)
- [[likelihood]] — for a memoryless channel, a product of per-bit terms; only the ratio matters for decoding (pp. 324–325)
- [[prior-distribution]] — usually uniform over valid codewords (p. 325)
- [[posterior-distribution]] — probabilities over codewords given $\mathbf y$ (p. 324)
- [[noisy-channel]] — here memoryless, e.g. Gaussian, described by $P(y\mid t)$ (p. 324)
- [[error-correcting-code]] — a linear (N, K) code with $2^K$ codewords (pp. 324–325)
- [[map-codeword-decoding]] (new) — find the most probable codeword; equals maximum-likelihood decoding under a uniform prior (p. 325)
- [[bitwise-decoding]] (new) — compute each bit's posterior marginal by summing over the other bits (p. 326)
- [[trellis]] (new) — layered graph whose left-to-right paths are the codewords (p. 326)
- [[min-sum-algorithm]] (new) — message passing that finds the minimum-cost path (Viterbi); work equals the number of edges (p. 329)
- [[sum-product-algorithm]] (new) — min–sum with (sum, product): forward–backward, BCJR, belief propagation (pp. 329–330)
- [[syndrome]] (new) — $\mathbf H\mathbf r$; partial syndromes are the trellis states (p. 332)
- [[trellis-oriented-form]] (new) — generator matrix whose row spans start in different columns and end in different columns (p. 331)

## Canonical instances
- [[hamming-7-4-trellis]] — worked decoding with likelihoods $(0.1,0.4,0.9,0.1,0.1,0.1,0.3)$ (pp. 327–329)
- [[gaussian-channel-likelihood-ratio]] — $\exp(2xy_n/\sigma^2)$ (p. 325)
- [[repetition-code-r3-and-parity-code-p3]] — the small trellises of figure 25.1 and the $P_3$ exercise (pp. 327, 330)

## Bridges (candidates)
- [same-math] sum–product on a trellis ↔ bayesian: exact marginal posteriors by summing out variables on a chain (forward–backward as in hidden-Markov-style inference). The trellis states play the role of a hidden state sequence.
- [same-math] min–sum on a trellis ↔ information-theory: Viterbi MAP path search. The same mathematics as in Chapter 16 (p. 329).
- [structural-analogy] choosing a bit order to shrink the trellis ↔ bayesian: choosing a variable elimination order to reduce the cost of exact inference.
- [structural-analogy] syndrome-as-state ↔ information-theory: a parity-check constraint turned into a finite-state machine.

## Questions this raises
- How does the maximal trellis width depend on the code and bit order, and how hard is it to find the best order?
- For codes whose minimal trellises are too wide, what approximate message-passing methods replace the exact ones?
- When do MAP codeword decoding and bit-by-bit decoding differ, and which should we prefer?
- Is the bound "less than $2^M$" (p. 327) strict, or "at most $2^M$" (p. 332)?

## Exercises worth doing
- Ex. 25.1 (p. 325) — a Gaussian channel acts like a binary symmetric channel with varying noise — difficulty: medium
- Ex. 25.2 (p. 327) — confirm the 16 Hamming codewords come from the trellis of figure 25.1c — difficulty: medium
- Ex. 25.4 (p. 329) — MAP decoding versus bitwise decoding on a new likelihood vector (solution printed on p. 333) — difficulty: medium
- Ex. 25.5 and 25.7 (p. 330) — meaning of the forward and backward messages — difficulty: medium
- Ex. 25.8 (p. 330) — verify that (25.15)–(25.16) give the bit posteriors — difficulty: medium
- Ex. 25.9 (p. 330) — run both algorithms on the $P_3$ trellis and check by enumeration (solution printed on p. 333) — difficulty: medium

## Reading notes
- Printed page = pdf page − 12.
- Misprint in the solution to Ex. 25.9 (p. 333): the image shows "$P(t_1{=}1\mid\mathbf y)$" three times, with values 3/4, 1/4, 5/6. Enumerating the codeword probabilities given on that page shows these are for $t_1,t_2,t_3$.
- The text words the trellis width bound differently in two places: "everywhere less than $2^M$" (p. 327) versus "at most $2^M$ nodes in each state" (p. 332). I report both.
- In Ex. 25.6 the stated constant $2^K$ is given as an answer in the exercise line (p. 330). The text does not derive it.
- The page-331 text says "subtracting lower rows from upper rows". (Our remark, not the text's: over binary arithmetic this is addition mod 2.) The text says only "subtracting".
- The trellis figures (25.1, 25.6, 25.7) are only partly legible in the images. I rely on the text for their content.
