---
id: mackay-2003-information/ch26-exact
work: mackay-2003-information
unit: "26 Exact Marginalization in Graphs"
pages: 334-340
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Exact Marginalization in Graphs

## L0 — One line
When a function is a product of factors and its factor graph is tree-like, passing local messages along the edges computes every marginal, and the normalizing constant, exactly and efficiently.

## L1 — The gist (≤ 120 words)
Given a function written as a product of factors, how can we compute its normalizing constant and its marginals? In general this is believed to cost exponential time in the number of variables. The chapter's answer is the sum–product algorithm. Variable nodes and factor nodes exchange messages along the edges of a factor graph. If the graph is a tree, the marginals come out exactly. Replacing "sum" by "max" gives the max–product (min–sum, Viterbi) algorithm, from which the best joint setting can be deduced. On graphs with cycles one can merge variables into groups ("agglomerate"; junction tree, exact but exponential) or run the same messages anyway ("loopy" passing, no guarantee).

**Prerequisites:** sums and products over discrete variables; marginal and joint distributions; message passing from Chapter 16; basic graphs (trees, leaves, cycles).

## L2 — Key ideas
- A factored function $P^*(\mathbf x)=\prod_m f_m(\mathbf x_m)$ is drawn as a factor graph (variable nodes and factor nodes, with an edge when a factor depends on a variable). Three tasks follow: the normalizer $Z$, the marginals $Z_n(x_n)$, and the normalized marginals $P_n(x_n)$ (pp. 334–335).
- All three tasks are intractable in general, and the exact cost is believed in general to grow exponentially with the number of variables. For certain functions, exploiting the factorization allows the marginals to be computed efficiently (p. 335).
- The sum–product algorithm uses two message rules, (26.11) and (26.12). It is valid only if the graph is tree-like (pp. 336–337).
- Method 1 starts from the leaves (nodes with one edge). Every message exists after a number of steps equal to the graph's diameter (the longest shortest path between two nodes). Then $Z_n=\prod$ of incoming messages (p. 337).
- Method 2 ("lazy") sets all variable-to-factor messages to 1 and iterates. It also runs on graphs with cycles, where it may not converge and is not generally correct. It matters in decoding sparse-graph codes (pp. 337–338).
- On-the-fly normalization, log-domain messages and Fourier-transformed messages are computational tricks (pp. 338–339).
- The sum–product algorithm can be viewed as re-factorizing $P^*$ into $M+N$ factors. This view holds with or without cycles (p. 338).
- Replacing (add, multiply) by (max, multiply) gives max–product, which is most often run in the negative-log domain, where it becomes min–sum (the Viterbi algorithm). The maximizing $\mathbf x$ can be deduced from its output (pp. 339–340).
- For non-tree graphs: the junction tree algorithm (exact, exponential in the agglomerated variables) or loopy message passing (p. 340).

## L3 — Walkthrough

### 26.1 The general problem (pp. 334–336)
Let $\mathbf x=\{x_n\}_{n=1}^N$ and
$$P^*(\mathbf x)=\prod_{m=1}^M f_m(\mathbf x_m)\tag{26.1}$$
where each factor depends on a subset $\mathbf x_m$ of the variables. If $P^*$ is positive, define
$$P(\mathbf x)\equiv\frac1Z P^*(\mathbf x)=\frac1Z\prod_{m=1}^M f_m(\mathbf x_m),\qquad Z=\sum_{\mathbf x}\prod_{m=1}^M f_m(\mathbf x_m).\tag{26.2, 26.3}$$

**Example (26.4), p. 334.** Three binary variables, five factors:
- $f_1(x_1)=0.1$ for $x_1=0$ and $0.9$ for $x_1=1$. $f_2(x_2)$ is the same.
- $f_3(x_3)=0.9$ for $x_3=0$ and $0.1$ for $x_3=1$.
- $f_4(x_1,x_2)=1$ if $(x_1,x_2)=(0,0)$ or $(1,1)$, else $0$. $f_5(x_2,x_3)$ is the same with $(x_2,x_3)$.
- $P^*=f_1f_2f_3f_4f_5$.

This $P$ is the posterior over the three transmitted bits of a repetition code, for received $\mathbf r=(1,1,0)$ on a binary symmetric channel with flip probability 0.1. $f_4,f_5$ force equal bits. $f_1,f_2,f_3$ are the likelihoods of the received bits (p. 335).

A **factor graph** has circular variable nodes and square factor nodes. An edge joins variable $n$ and factor $m$ if $f_m$ depends on $x_n$ (p. 335).

**Three tasks (p. 335):**
1. Normalization: compute $Z$.
2. Marginal function: $Z_n(x_n)=\sum_{\{x_{n'}\},n'\ne n}P^*(\mathbf x)$ (26.5). The author notes that a special notation for this sum over "all variables except $x_n$" can be useful, called the "not-sum" or "summary" (no symbol is given on these pages).
3. Normalized marginal: $P_n(x_n)=\sum_{n'\ne n}P(\mathbf x)$ (26.7). Exercise 26.1 asks to show $P_n=Z_n/Z$ (26.8).

Marginals over subsets are also possible, e.g. $Z_{12}(x_1,x_2)=\sum_{x_3}P^*$ (26.9).

All three tasks are intractable in general. Even with factors of only three variables, exact cost is believed in general to grow exponentially with $N$. For certain $P^*$ the factorization allows efficient computation (p. 335). The sum–product algorithm generalizes Chapter 16's rule-set B and is valid only if the graph is tree-like (p. 336).

### 26.2 The sum–product algorithm (pp. 336–339)
**Notation (p. 336).** $\mathcal N(m)$ is the set of indices of variables in factor $m$. $\mathcal M(n)$ is the set of factors containing variable $n$. In (26.4): $\mathcal N(4)=\{1,2\}$, $\mathcal N(5)=\{2,3\}$. Also $\mathbf x_{m\setminus n}\equiv\{x_{n'}:n'\in\mathcal N(m)\setminus n\}$ (26.10).

Messages are $q_{n\to m}$ (variable to factor) and $r_{m\to n}$ (factor to variable). Either kind is a function of $x_n$ (p. 336). *(added step: so each message is a table with one entry per value of $x_n$.)*

$$q_{n\to m}(x_n)=\prod_{m'\in\mathcal M(n)\setminus m} r_{m'\to n}(x_n)\tag{26.11}$$
$$r_{m\to n}(x_n)=\sum_{\mathbf x_{m\setminus n}}\Big(f_m(\mathbf x_m)\prod_{n'\in\mathcal N(m)\setminus n} q_{n'\to m}(x_{n'})\Big)\tag{26.12}$$

**Leaves (p. 336).** A leaf has one edge. A factor leaf has an empty product (value 1), so it always sends $r_{m\to n}(x_n)=f_m(x_n)$. A variable leaf always sends $q_{n\to m}(x_n)=1$.

*Intuition note (our gloss, for a tree-like graph):* Each message summarizes everything on the far side of an edge, with the receiving node's own side left out. Multiplying messages combines independent pieces. Summing inside a factor removes the other variables.

**Method 1 (pp. 336–337).** Initialize leaves: $q_{n\to m}=1$ (26.13), $r_{m\to n}=f_m$ (26.14). A message is created by (26.11, 26.12) only when all messages it depends on are present. In Figure 26.4, $x_2\to f_2$ ($q_{2\to2}$) waits for $r_{4\to2}$ and $r_{5\to2}$. One message flows in each direction along every edge. After a number of steps equal to the graph's diameter, all messages exist (p. 337). Then
$$Z_n(x_n)=\prod_{m\in\mathcal M(n)} r_{m\to n}(x_n)\tag{26.15}$$
$$Z=\sum_{x_n}Z_n(x_n)\ \text{(any } n),\qquad P_n(x_n)=\frac{Z_n(x_n)}{Z}\tag{26.16}$$

*Intuition note:* The marginal of $x_n$ is the product of what each neighbouring factor "believes" about it. On a tree-like graph, summing any variable's marginal gives the same $Z$ (p. 337).

Exercises 26.2–26.4 ask to apply this to (26.4), prove correctness on trees, and extract $Z_{1,2}$ (p. 337).

**Method 2, lazy (pp. 337–338).** Set all $q_{n\to m}(x_n)=1$ (26.17). Alternate (26.12) and (26.11). This wastes computation that is gradually flushed out by correct answers. After a number of iterations equal to the diameter, the messages satisfy (26.11, 26.12). It can be used on graphs with cycles. There it does not necessarily converge and certainly does not in general give the correct marginals. Still, it is of great practical importance, especially in decoding sparse-graph codes (p. 338). Exercise 26.5 (p. 337) asks to apply method 2 to (26.4).

**On-the-fly normalization (p. 338).** Keep $r$ as in (26.12) but normalize $q$:
$$q_{n\to m}(x_n)=\alpha_{nm}\prod_{m'\in\mathcal M(n)\setminus m} r_{m'\to n}(x_n),\quad \sum_{x_n}q_{n\to m}(x_n)=1\tag{26.18, 26.19}$$
This version may be useful if only normalized marginals are wanted. Exercise 26.6 asks to apply it to (26.4).

**Factorization view (p. 338).** The algorithm re-expresses $P^*$ as $M+N$ factors:
$$P^*(\mathbf x)=\prod_{m=1}^M\phi_m(\mathbf x_m)\prod_{n=1}^N\psi_n(x_n)\tag{26.20}$$
Initially $\phi_m=f_m$ and $\psi_n=1$. Each time $r_{m\to n}$ is sent:
$$\psi_n(x_n)=\prod_{m\in\mathcal M(n)}r_{m\to n}(x_n)\tag{26.21}$$
$$\phi_m(\mathbf x_m)=\frac{f(\mathbf x_m)}{\prod_{n\in\mathcal N(m)}r_{m\to n}(x_n)}\tag{26.22}$$
$$r_{m\to n}(x_n)=\sum_{\mathbf x_{m\setminus n}}\Big(\phi_m(\mathbf x_m)\prod_{n'\in\mathcal N(m)}\psi_{n'}(x_{n'})\Big)\tag{26.23}$$
This differs from (26.12) in that the product is over all $n'\in\mathcal N(m)$. Exercise 26.7 asks to confirm equivalence to (26.11–26.12), so $\psi_n$ eventually becomes $Z_n$. This view applies whether or not the graph is tree-like.

**Computational tricks (p. 339).**
- If $P^*$ has many factors, its values are likely very large or very small. This is why normalizing on the fly helps.
- Pass $\ln q,\ln r$: products become additions. Sums need $l=\ln(e^{l_1}+e^{l_2}+e^{l_3})$ (26.24). The answer is typically a little above $\max_i l_i$. With look-up tables of $\ln(1+e^\delta)$ for negative $\delta$ (26.25), $l$ is computed exactly with look-ups and additions scaling with the number of terms. This is cheaper than direct evaluation if look-ups and sorting are cheaper than $\exp()$. Negligible terms may be omitted.
- For certain error-correcting codes, pass Fourier transforms of messages. The author's example is at (47.9) in Chapter 47.

### 26.3 The min–sum algorithm (pp. 339–340)
Sum–product solves the marginal problem (analogue of bitwise decoding, section 25.1). The **maximization problem** is: find the $\mathbf x$ maximizing $P^*(\mathbf x)$ (analogue of codeword decoding). Replace (add, multiply) by (max, multiply), which satisfy the distributive law (p. 339). Then $Z=\sum_{\mathbf x}P^*(\mathbf x)$ (26.26) becomes $\max_{\mathbf x}P^*(\mathbf x)$. Each "marginal" $Z_n(x_n)$ lists the maximum value $P^*$ can attain for each value of $x_n$ (p. 339). In practice the max–product algorithm is most often carried out in the negative log likelihood domain, where max and product become min and sum. This min–sum algorithm is also known as the Viterbi algorithm (p. 340).

*Intuition note:* The message structure is unchanged. Only the arithmetic changes, from "total over all settings" to "best over all settings".

### 26.4 The junction tree algorithm (p. 340)
For graphs with cycles, the author lists exact and approximate methods. The most widely used exact method is the junction tree algorithm. It agglomerates variables until the agglomerated graph has no cycles. Complexity grows exponentially with the number of agglomerated variables. Approximate methods include Monte Carlo and variational methods. "Loopy" message passing computes the messages as if the graph were a tree, iterates, and has no guarantee. It is important for decoding error-correcting codes (section 33.8, Part VI). Further reading is listed on p. 340.

### 26.5 Exercises (p. 340)
Exercise 26.8 asks to express the burglar-alarm and earthquake joint distribution (example 21.1) as a factor graph and use on-the-fly sum–product.

## Toy example (ours)
Two binary variables on a chain: $f_1(x_1)$, $f_2(x_1,x_2)$, $f_3(x_2)$.
- $f_1=(1,2)$ for $x_1=0,1$.
- $f_2=3$ if $x_1=x_2$, else $1$.
- $f_3=(2,1)$ for $x_2=0,1$.

Method 1, with messages written as (value at 0, value at 1):
- Leaves: $r_{1\to1}=f_1=(1,2)$ and $r_{3\to2}=f_3=(2,1)$.
- $q_{1\to2}=r_{1\to1}=(1,2)$. $q_{2\to2}=r_{3\to2}=(2,1)$.
- $r_{2\to2}(x_2)=\sum_{x_1}f_2(x_1,x_2)q_{1\to2}(x_1)$. At $x_2=0$: $3\cdot1+1\cdot2=5$. At $x_2=1$: $1\cdot1+3\cdot2=7$. So $(5,7)$.
- $r_{2\to1}(x_1)=\sum_{x_2}f_2q_{2\to2}$. At $x_1=0$: $3\cdot2+1\cdot1=7$. At $x_1=1$: $1\cdot2+3\cdot1=5$. So $(7,5)$.
- $Z_1=(1\cdot7,\,2\cdot5)=(7,10)$. $Z_2=(5\cdot2,\,7\cdot1)=(10,7)$. Both sum to $Z=17$, so $P_1=(7/17,10/17)$.

Brute-force check, with $P^*$ at $(x_1,x_2)$:
- $(0,0)$: $1\cdot3\cdot2=6$.
- $(0,1)$: $1\cdot1\cdot1=1$.
- $(1,0)$: $2\cdot1\cdot2=4$.
- $(1,1)$: $2\cdot3\cdot1=6$.

These sum to 17. $Z_1(0)=6+1=7$, $Z_1(1)=4+6=10$, $Z_2(0)=6+4=10$, $Z_2(1)=1+6=7$. This matches the messages. For max–product, replace each sum by a max. For example $r_{2\to2}(0)=\max(3\cdot1,\,1\cdot2)=3$.

## Concepts
- [[factor-graph]] (new) — bipartite graph: variable nodes, factor nodes, edge if the factor depends on the variable (p. 335)
- [[normalizing-constant-Z]] (new) — $Z=\sum_{\mathbf x}\prod_m f_m(\mathbf x_m)$, the total mass of $P^*$ (p. 334)
- [[marginal-function]] (new) — $Z_n(x_n)$, the sum of $P^*$ over all other variables; $P_n=Z_n/Z$ (p. 335)
- [[sum-product-algorithm]] (new) — message rules (26.11, 26.12); exact marginals on tree-like graphs (p. 336)
- [[min-sum-viterbi]] (new) — sum–product with max replacing sum; min and sum in the negative-log domain (p. 339–340)
- [[junction-tree-algorithm]] (new) — exact method that agglomerates variables until the graph has no cycles (p. 340)
- [[loopy-message-passing]] (new) — running sum–product on graphs with cycles; no guarantee, widely used in decoding (p. 338, 340)
- [[marginal-likelihood-evidence]] — in the book's terms, $Z$ is the normalizer of a product of likelihood and constraint factors; the chapter does not call it evidence (p. 334–335)

## Canonical instances
- [[repetition-code-R3-posterior]] — the example (26.4) as the posterior of three bits for $\mathbf r=(1,1,0)$, BSC flip probability 0.1 (p. 335)
- [[burglar-alarm-network]] — Exercise 26.8, as a factor graph (p. 340)

## Bridges (candidates)
- [structural-analogy] max–product / min–sum (Viterbi) ↔ information-theory: codeword decoding — the book calls the maximization problem "analogous to the codeword decoding problem" (p. 339).
- [structural-analogy] $Z$ ↔ bayesian: marginal likelihood — both are sums of an unnormalized product over latent states.
- [structural-analogy] sum–product on a tree ↔ bayesian: sequential updating — local evidence is combined by multiplication.
- [metaphor] log-domain softmax $\ln\sum e^{l_i}$ ↔ information-theory: log-sum-exp as a soft maximum.

## Questions this raises
- Why does the tree condition make (26.12) exact (Exercise 26.3)? What goes wrong when messages travel round a cycle?
- How large do agglomerated variable groups get in the junction tree algorithm for typical graphs?
- When does loopy message passing converge, and how good are its answers?
- How do other message-passing methods the author names (expectation propagation, survey propagation) differ?

## Exercises worth doing
- Ex. 26.2 (p. 337) — apply sum–product to (26.4) and compare with $R_3$ — difficulty: easy
- Ex. 26.3 (p. 337) — prove correctness on trees — difficulty: hard
- Ex. 26.4 (p. 337) — get $Z_{1,2}$ from messages — difficulty: medium
- Ex. 26.7 (p. 338) — equivalence of the $\phi,\psi$ updates and sum–product — difficulty: medium
- Ex. 26.8 (p. 340) — burglar-alarm factor graph — difficulty: medium

## Reading notes
- Printed pages 334–340 correspond to pdf 346–352 (printed = pdf − 12). Pages pdf 351–352 were read from the text layer only. The text layer of pdf 346–350 had jumbled equations, which were checked against the page images.
- In (26.22) the page image shows $f(\mathbf x_m)$ without the subscript $m$ on $f$. This is probably a misprint for $f_m$, since the text above has $\phi_m=f_m$ initially.
- Figures 26.1 and 26.4 are identical drawings of the factor graph for (26.4).
- The "Further reading" list (p. 340) was not digested beyond naming its existence.
