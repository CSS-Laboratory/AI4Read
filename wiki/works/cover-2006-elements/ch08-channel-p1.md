---
id: cover-2006-elements/ch08-channel-p1
work: cover-2006-elements
unit: "8 Channel Capacity (part 1/2): §§8.1–8.7 up to the end of the achievability argument"
pages: 183–202
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
audited: 2026-10-14
audit_fixes: 5
---
# Channel Capacity (part 1/2): examples, joint AEP, and the achievability half of Shannon's second theorem

## L0 — One line
The capacity $C=\max_{p(x)} I(X;Y)$ of a discrete memoryless channel is the highest rate at which messages can be sent with error probability going to zero, and the proof of achievability uses random codes with joint-typicality decoding.

## L1 — The gist (≤ 120 words)
How many bits per channel use can be sent reliably through a noisy channel? The chapter defines "information" capacity as the maximum of mutual information over input distributions. It computes it for simple channels: noiseless, noisy typewriter, binary symmetric, binary erasure, and symmetric channels. It then defines codes, rates and error probabilities, and proves the joint AEP. Using random codebooks and decoding by joint typicality, it shows that every rate $R<C$ is achievable with maximal error probability tending to 0. The converse (no rate above $C$) is postponed to §8.9. This matters because it is the central success of information theory.

**Prerequisites:** entropy, conditional entropy, mutual information and its concavity in $p(x)$; the weak law of large numbers; the AEP / typical sets; union bound.

## L2 — Key ideas
- Information capacity is $C=\max_{p(x)}I(X;Y)$ (8.1). The author says Shannon's second theorem makes it equal to the operational capacity, the best rate with vanishing error (p. 184).
- Closed forms for simple channels: BSC $1-H(p)$, binary erasure channel $1-\alpha$, noisy typewriter $\log 13$ (pp. 185–188). Weakly symmetric channels (every row is a permutation of every other row, and all column sums are equal) have $C=\log|\mathcal Y|-H(\text{row})$ (Thm 8.2.1, p. 190).
- $I(X;Y)$ is concave in $p(x)$, so a local maximum is global; the bounds $C\le\log|\mathcal X|$ and $C\le\log|\mathcal Y|$ make the maximum finite (p. 191).
- Heuristic: of about $2^{nH(Y)}$ typical outputs, each input sequence takes up about $2^{nH(Y|X)}$, so about $2^{nI(X;Y)}$ inputs are distinguishable (p. 191).
- The joint AEP: the jointly typical set (pairs $(x^n,y^n)$ whose empirical entropies are all within $\epsilon$ of the true entropies) has about $2^{nH(X,Y)}$ elements, and an independent pair falls in it with probability about $2^{-nI(X;Y)}$ (Thm 8.6.1, p. 195).
- Achievability (Thm 8.7.1): draw a random codebook, decode by joint typicality, and bound the average error by $2\epsilon$ when $R<I(X;Y)-3\epsilon$ (pp. 198–202).
- Throwing away the worst half of the codewords of a codebook (the set of all codewords) with small average error gives a code with small maximal error, at a negligible rate loss (p. 202).

## L3 — Walkthrough

### Chapter introduction (pp. 183–184)
- A communicates with B if A's physical acts induce a desired physical state in B. Noise and imperfections affect this (p. 183).
- The chapter finds the maximum number of distinguishable signals in $n$ channel uses. It grows exponentially in $n$, and the exponent is the capacity (p. 183).
- The setting is Fig. 8.1: message $W$ → encoder → $X^n$ → channel $p(y|x)$ → $Y^n$ → decoder → estimate $\hat W$ (p. 184).
- Different inputs may give the same output, so inputs are "confusable". The idea is to choose a "non-confusable", widely spaced subset of input sequences, so that each output very probably comes from one input (p. 183).
- **Definition.** A *discrete channel* has an input alphabet $\mathcal X$, an output alphabet $\mathcal Y$, and a transition matrix $p(y|x)$. It is *memoryless* if the output depends only on the current input, conditionally independent of earlier inputs and outputs (p. 184).
- **Definition (8.1).** $C=\max_{p(x)} I(X;Y)$, the "information" capacity (p. 184).
- Duality: compression removes redundancy; transmission adds controlled redundancy against errors. The last section of the chapter shows the two problems can be treated separately (p. 184; not in this part).

### 8.1 Examples of channel capacity (pp. 184–189)
- **8.1.1 Noiseless binary channel.** The input is reproduced exactly, so $C=1$ bit, achieved by $p(x)=(\tfrac12,\tfrac12)$ (p. 185).
- **8.1.2 Noisy channel with nonoverlapping outputs.** From the figure: input 0 goes to outputs 1 or 2 (probabilities $\tfrac12,\tfrac12$); input 1 goes to outputs 3 or 4 ($\tfrac13,\tfrac23$). The input can be read off the output, so $C=1$ bit, with $p(x)=(\tfrac12,\tfrac12)$ (p. 185).
- **8.1.3 Noisy typewriter.** Each of 26 inputs arrives unchanged with probability $\tfrac12$ or as the next letter with probability $\tfrac12$. Using every alternate letter gives 13 error-free symbols per use, so $C=\log 13$ (p. 185). The calculation:
$$C=\max I(X;Y)=\max[H(Y)-H(Y|X)]=\max H(Y)-1=\log 26-1=\log 13,$$
achieved by $p(x)$ uniform over all inputs (p. 186).
- **8.1.4 Binary symmetric channel (BSC).** Each input bit is complemented with probability $p$. The author calls it the simplest model of a channel with errors, yet it "captures most of the complexity" of the general problem (p. 186).
$$I(X;Y)=H(Y)-H(Y|X)\tag{8.2}$$
$$=H(Y)-\sum_x p(x)H(Y|X=x)\tag{8.3}$$
$$=H(Y)-\sum_x p(x)H(p)\tag{8.4}$$
$$=H(Y)-H(p)\tag{8.5}$$
$$\le 1-H(p),\tag{8.6}$$
 The last inequality holds because $Y$ is binary. Equality holds for uniform input (p. 187). Hence
$$C=1-H(p)\text{ bits}.\tag{8.7}$$
- **8.1.5 Binary erasure channel.** A fraction $\alpha$ of bits is erased and the receiver knows which. There are 2 inputs and 3 outputs ($0,1,e$) (p. 187).
$$C=\max_{p(x)}I(X;Y)\tag{8.8}$$
$$=\max_{p(x)}\big(H(Y)-H(Y|X)\big)\tag{8.9}$$
$$=\max_{p(x)}H(Y)-H(\alpha).\tag{8.10}$$
  ($H(Y|X)=H(\alpha)$ because erasure happens with probability $\alpha$ whatever the input; added step.) The first guess for $\max H(Y)$ would be $\log 3$, but no input distribution reaches it (p. 188). Let $E=\{Y=e\}$ and $\Pr(X=1)=\pi$:
$$H(Y)=H(Y,E)=H(E)+H(Y|E),\tag{8.11}$$
$$H(Y)=H\big((1-\pi)(1-\alpha),\alpha,\pi(1-\alpha)\big)=H(\alpha)+(1-\alpha)H(\pi).\tag{8.12}$$
$$C=\max_{p(x)}H(Y)-H(\alpha)\tag{8.13}$$
$$=\max_\pi(1-\alpha)H(\pi)+H(\alpha)-H(\alpha)\tag{8.14}$$
$$=\max_\pi(1-\alpha)H(\pi)\tag{8.15}$$
$$=1-\alpha,\tag{8.16}$$
 achieved at $\pi=\tfrac12$ (p. 188).
- A proportion $\alpha$ of bits is lost, so at most $1-\alpha$ can be recovered. That $1-\alpha$ is achievable "will follow from Shannon's second theorem" (p. 188).
- With feedback, retransmit each lost bit until it arrives. The effective rate is $1-\alpha$ (p. 189).
- The author says that he will later prove $1-\alpha$ is the best rate with and without feedback. This is one consequence of the fact that feedback does not increase the capacity of discrete memoryless channels (p. 189).

*Intuition note.* In the erasure channel a fraction $\alpha$ of the bits is lost, so at most a fraction $1-\alpha$ can be recovered (p. 188). The author notes that it is not immediately obvious that this rate can be reached; he says it will follow from Shannon's second theorem, and with feedback simple retransmission reaches it (pp. 188–189).

### 8.2 Symmetric channels (pp. 189–190)
- Example transition matrix (8.17), rows indexed by $x$:
$$p(y|x)=\begin{bmatrix}0.3&0.2&0.5\\0.5&0.3&0.2\\0.2&0.5&0.3\end{bmatrix}.$$
 Rows are permutations of each other, and so are columns. Such a channel is called symmetric. Another example is $Y=X+Z \pmod c$, with $Z$ independent of $X$ and on the same alphabet (8.18) (p. 189).
- With $\mathbf r$ a row of the matrix:
$$I(X;Y)=H(Y)-H(Y|X)\tag{8.19}$$
$$=H(Y)-H(\mathbf r)\tag{8.20}$$
$$\le\log|\mathcal Y|-H(\mathbf r),\tag{8.21}$$
 with equality if the output is uniform. The input $p(x)=1/|\mathcal X|$ gives uniform output (p. 189):
$$p(y)=\sum_{x}p(y|x)p(x)=\frac1{|\mathcal X|}\sum_x p(y|x)=c\,\frac1{|\mathcal X|}=\frac1{|\mathcal Y|},\tag{8.22}$$
 where $c$ is a column sum (p. 190).
- So the channel (8.17) has
$$C=\max_{p(x)}I(X;Y)=\log 3-H(0.5,0.3,0.2),\tag{8.23}$$
 achieved by uniform input (p. 190).
- **Definition.** A channel is *symmetric* if rows are permutations of each other and columns are too. It is *weakly symmetric* if every row is a permutation of every other row and all column sums $\sum_x p(y|x)$ are equal. Example (8.24), weakly symmetric but not symmetric (p. 190):
$$p(y|x)=\begin{pmatrix}\tfrac13&\tfrac16&\tfrac12\\ \tfrac13&\tfrac12&\tfrac16\end{pmatrix}.$$
- **Theorem 8.2.1.** For a weakly symmetric channel, $C=\log|\mathcal Y|-H(\text{row of transition matrix})$ (8.25), achieved by the uniform input distribution (p. 190).

### 8.3 Properties of channel capacity (pp. 190–191)
1. $C\ge0$, since $I(X;Y)\ge0$.
2. $C\le\log|\mathcal X|$, since $C\le\max H(X)=\log|\mathcal X|$.
3. $C\le\log|\mathcal Y|$, for the same reason.
4. $I(X;Y)$ is continuous in $p(x)$.
5. $I(X;Y)$ is concave in $p(x)$ (Theorem 2.7.4).
- Concave over a closed convex set means a local maximum is global. With (2) and (3), the maximum is finite, so "maximum" rather than "supremum" is justified (p. 191).
- The maximum can be found by standard nonlinear optimization: Kuhn–Tucker conditions, Frank–Wolfe gradient search, or the Arimoto–Blahut iteration (described in §13.8). In general there is no closed form, but symmetry helps for simple channels (p. 191).

### 8.4 Preview of the channel coding theorem (pp. 191–192)
- Heuristic (not a proof): for large block length, every channel looks like the noisy typewriter, with a subset of inputs giving essentially disjoint outputs (p. 191).
- Each typical input $n$-sequence gives about $2^{nH(Y|X)}$ equally likely outputs. There are about $2^{nH(Y)}$ typical outputs in total. Hence at most about $2^{n(H(Y)-H(Y|X))}=2^{nI(X;Y)}$ non-overlapping output sets, i.e. distinguishable input sequences (p. 191, Fig. 8.7).
- The author says a stronger version of this argument will show that this rate is achievable (p. 192).

*Intuition note.* Think of packing: the output space has room for $2^{nH(Y)}$ outcomes and each input needs a "cloud" of $2^{nH(Y|X)}$ outcomes. The number of non-overlapping clouds is at most the ratio of the two (the author's bound, p. 191).

### 8.5 Definitions (pp. 192–194)
- A message $W\in\{1,\dots,M\}$ gives signal $X^n(W)$. The receiver sees $Y^n\sim p(y^n|x^n)$ and guesses $\hat W=g(Y^n)$. An error occurs if $\hat W\neq W$ (p. 192).
- A *discrete channel* $(\mathcal X,p(y|x),\mathcal Y)$ has finite $\mathcal X,\mathcal Y$, with $p(y|x)\ge0$ and $\sum_y p(y|x)=1$ for each $x$ (p. 192).
- **$n$th extension of the DMC:** $(\mathcal X^n,p(y^n|x^n),\mathcal Y^n)$ with
$$p(y_k|x^k,y^{k-1})=p(y_k|x_k),\quad k=1,\dots,n.\tag{8.26}$$
- **Remark.** Without feedback, i.e. $p(x_k|x^{k-1},y^{k-1})=p(x_k|x^{k-1})$,
$$p(y^n|x^n)=\prod_{i=1}^n p(y_i|x_i).\tag{8.27}$$
 "DMC" below means no feedback unless stated (p. 193).
- **$(M,n)$ code:** an index set $\{1,\dots,M\}$; an encoder $X^n:\{1,\dots,M\}\to\mathcal X^n$ giving codewords $X^n(1),\dots,X^n(M)$ (the *codebook*); and a deterministic decoder
$$g:\mathcal Y^n\to\{1,2,\dots,M\}.\tag{8.28}$$
- **Error probabilities.** Conditional probability of error given index $i$, with $I(\cdot)$ the indicator function:
$$\lambda_i=\Pr(g(Y^n)\ne i\mid X^n=X^n(i))=\sum_{y^n}p(y^n|x^n(i))\,I(g(y^n)\neq i).\tag{8.29}$$
 Maximal: $\lambda^{(n)}=\max_{i}\lambda_i$ (8.30). Average: $P_e^{(n)}=\frac1M\sum_{i=1}^M\lambda_i$ (8.31). If $I$ is uniform on $\{1,\dots,M\}$, $P_e^{(n)}=\Pr(I\ne g(Y^n))$ (8.32). Also $P_e^{(n)}\le\lambda^{(n)}$ (8.33) (pp. 193–194).
- The author says the maximal and average errors might be expected to behave quite differently. He promises to prove that a small average error implies a small maximal error at essentially the same rate (p. 194; done by step 3 on p. 202 below).
- **Rate:** $R=\frac{\log M}{n}$ bits per transmission (8.34). **Achievable:** there is a sequence of $(\lceil 2^{nR}\rceil,n)$ codes with $\lambda^{(n)}\to0$. Later $(2^{nR},n)$ abbreviates $(\lceil 2^{nR}\rceil,n)$ (p. 194).
- **Capacity of a DMC** (operational): the supremum of all achievable rates. So rates below capacity give arbitrarily small error for large enough block length (p. 194).

### 8.6 Jointly typical sequences (pp. 194–197)
Decoding idea: choose index $i$ if $X^n(i)$ is "jointly typical" with $Y^n$ (p. 194).

**Definition.** $A_\epsilon^{(n)}$ is the set of $(x^n,y^n)\in\mathcal X^n\times\mathcal Y^n$ whose empirical entropies are $\epsilon$-close to the true entropies:
$$\Big|-\tfrac1n\log p(x^n)-H(X)\Big|<\epsilon,\tag{8.36}$$
$$\Big|-\tfrac1n\log p(y^n)-H(Y)\Big|<\epsilon,\tag{8.37}$$
$$\Big|-\tfrac1n\log p(x^n,y^n)-H(X,Y)\Big|<\epsilon,\tag{8.38}$$
where
$$p(x^n,y^n)=\prod_{i=1}^n p(x_i,y_i).\tag{8.39}$$
(Set defined in (8.35).) (p. 195)

**Theorem 8.6.1 (Joint AEP).** Let $(X^n,Y^n)$ be i.i.d. according to $\prod_i p(x_i,y_i)$. Then:
1. $\Pr((X^n,Y^n)\in A_\epsilon^{(n)})\to1$ as $n\to\infty$.
2. $|A_\epsilon^{(n)}|\le2^{n(H(X,Y)+\epsilon)}$.
3. If $(\tilde X^n,\tilde Y^n)\sim p(x^n)p(y^n)$ (independent, same marginals), then
$$\Pr((\tilde X^n,\tilde Y^n)\in A_\epsilon^{(n)})\le2^{-n(I(X;Y)-3\epsilon)}\tag{8.40}$$
 and, for $n$ sufficiently large,
$$\Pr((\tilde X^n,\tilde Y^n)\in A_\epsilon^{(n)})\ge(1-\epsilon)2^{-n(I(X;Y)+3\epsilon)}.\tag{8.41}$$
(p. 195)

**Proof.**
- Part 1. By the weak law, in probability,
$$-\tfrac1n\log p(X^n)\to-E[\log p(X)]=H(X),\tag{8.42}$$
 so for $n>n_1$: $\Pr(|-\tfrac1n\log p(X^n)-H(X)|>\epsilon)<\tfrac\epsilon3$ (8.43). Likewise $-\tfrac1n\log p(Y^n)\to H(Y)$ (8.44) and $-\tfrac1n\log p(X^n,Y^n)\to H(X,Y)$ (8.45). There are $n_2,n_3$ with failure probability $<\tfrac\epsilon3$ for $n\ge n_2$ (8.46) and $n\ge n_3$ (8.47). For $n>\max\{n_1,n_2,n_3\}$ the union of the three bad events has probability $<\epsilon$. So $\Pr(A_\epsilon^{(n)})>1-\epsilon$ (pp. 195–196).
- Part 2.
$$1=\sum p(x^n,y^n)\tag{8.48}$$
$$\ge\sum_{A_\epsilon^{(n)}}p(x^n,y^n)\tag{8.49}$$
$$\ge|A_\epsilon^{(n)}|\,2^{-n(H(X,Y)+\epsilon)},\tag{8.50}$$
 so $|A_\epsilon^{(n)}|\le2^{n(H(X,Y)+\epsilon)}$ (8.51). For large $n$, $\Pr(A_\epsilon^{(n)})\ge1-\epsilon$, so
$$1-\epsilon\le\sum_{(x^n,y^n)\in A_\epsilon^{(n)}}p(x^n,y^n)\tag{8.52}$$
$$\le|A_\epsilon^{(n)}|\,2^{-n(H(X,Y)-\epsilon)},\tag{8.53}$$
 giving $|A_\epsilon^{(n)}|\ge(1-\epsilon)2^{n(H(X,Y)-\epsilon)}$ (8.54) (p. 196).
- Part 3, upper bound:
$$\Pr((\tilde X^n,\tilde Y^n)\in A_\epsilon^{(n)})=\sum_{A_\epsilon^{(n)}}p(x^n)p(y^n)\tag{8.55}$$
$$\le2^{n(H(X,Y)+\epsilon)}2^{-n(H(X)-\epsilon)}2^{-n(H(Y)-\epsilon)}\tag{8.56}$$
$$=2^{-n(I(X;Y)-3\epsilon)}.\tag{8.57}$$
 Lower bound ("by similar arguments"):
$$\Pr=\sum_{A_\epsilon^{(n)}}p(x^n)p(y^n)\tag{8.58}$$
$$\ge(1-\epsilon)2^{n(H(X,Y)-\epsilon)}2^{-n(H(X)+\epsilon)}2^{-n(H(Y)+\epsilon)}\tag{8.59}$$
$$=(1-\epsilon)2^{-n(I(X;Y)+3\epsilon)}.\tag{8.60}$$
(p. 197) (Added step: (8.57) and (8.60) use $I(X;Y)=H(X)+H(Y)-H(X,Y)$.)

*Intuition note.* There are about $2^{nH(X)}$ typical $x^n$ and $2^{nH(Y)}$ typical $y^n$, but only $2^{nH(X,Y)}$ jointly typical pairs. A random pair is jointly typical with probability about $2^{-nI(X;Y)}$ (p. 197). So for fixed $y^n$ one can try about $2^{nI(X;Y)}$ candidates $x^n$ before one is likely to be jointly typical, "suggesting" about $2^{nI(X;Y)}$ distinguishable signals (p. 197, Fig. 8.9).

### 8.7 The channel coding theorem (pp. 198–202)
- Intro (author's voice). Result is "rather counterintuitive". The author asks: if the channel makes errors, how can all be corrected, since any correction process is itself subject to error? (p. 198)
- Shannon's new ideas: allow arbitrarily small but non-zero error; use the channel many times so the law of large numbers applies; average the error over a random choice of codebooks, which symmetrizes the probability and shows the existence of at least one good code (p. 198).
- The proof here decodes by joint typicality. It is suboptimal but simple to analyze, and still achieves all rates below capacity (p. 198). The author says it is probably the simplest proof developed so far (p. 198).

**Theorem 8.7.1 (Channel coding theorem).** All rates below capacity $C$ are achievable: for every $R<C$ there is a sequence of $(2^{nR},n)$ codes with $\lambda^{(n)}\to0$. Conversely, any sequence of $(2^{nR},n)$ codes with $\lambda^{(n)}\to0$ must have $R\le C$ (p. 198). Only achievability is proved in this part; the converse is postponed to §8.9 (p. 199).

**Achievability proof, construction (p. 199).**
- Fix $p(x)$. Generate $2^{nR}$ codewords independently, each i.i.d. $p(x^n)=\prod_{i=1}^n p(x_i)$ (8.61). They form the rows of the $2^{nR}\times n$ matrix $\mathscr C$ (8.62), with entries $x_i(w)$ i.i.d. $p(x)$:
$$\Pr(\mathscr C)=\prod_{w=1}^{2^{nR}}\prod_{i=1}^n p(x_i(w)).\tag{8.63}$$
- Protocol:
  1. A random code $\mathscr C$ is drawn.
  2. $\mathscr C$ and $p(y|x)$ are revealed to sender and receiver.
  3. $W$ is uniform: $\Pr(W=w)=2^{-nR}$ (8.64).
  4. The $w$th row $X^n(w)$ is sent.
  5. The receiver gets $Y^n$ with $p(y^n|x^n(w))=\prod_{i=1}^n p(y_i|x_i(w))$ (8.65).
  6. The receiver uses typical set decoding. Maximum likelihood decoding minimizes error but is hard to analyze; typical set decoding is easier and "asymptotically optimal" (pp. 199–200). It declares $\hat W$ sent if $(X^n(\hat W),Y^n)\in A_\epsilon^{(n)}$ and no other index $k$ has $(X^n(k),Y^n)\in A_\epsilon^{(n)}$. If none or several qualify, an error is declared (p. 200).
  7. A decoding error is the event $\mathscr E=\{\hat W\ne W\}$ (p. 200).

**Analysis, outline (p. 200).** Average over random codes. By symmetry the average error does not depend on which index was sent. Two error sources exist: $Y^n$ is not jointly typical with the sent codeword, or some other codeword is jointly typical with $Y^n$. The first has probability $\to0$ by the joint AEP. Each rival is jointly typical with probability about $2^{-nI}$, so about $2^{nI}$ codewords can be used.

**Detailed calculation (pp. 200–202).** Average the error over all codewords in the codebook and over all codebooks (p. 200):
$$\Pr(\mathscr E)=\sum_{\mathscr C}P(\mathscr C)P_e^{(n)}(\mathscr C)\tag{8.66}$$
$$=\sum_{\mathscr C}P(\mathscr C)\frac{1}{2^{nR}}\sum_{w=1}^{2^{nR}}\lambda_w(\mathscr C)\tag{8.67}$$
$$=\frac{1}{2^{nR}}\sum_{w=1}^{2^{nR}}\sum_{\mathscr C}P(\mathscr C)\lambda_w(\mathscr C),\tag{8.68}$$
where $P_e^{(n)}(\mathscr C)$ is defined for typical set decoding (p. 200). So (8.67) writes out the average error of one codebook, and (8.68) swaps the two sums. By the symmetry of the code construction (p. 201), $\sum_{\mathscr C}P(\mathscr C)\lambda_w(\mathscr C)$ does not depend on $w$, so assume $W=1$:
$$\Pr(\mathscr E)=\frac1{2^{nR}}\sum_{w=1}^{2^{nR}}\sum_{\mathscr C}P(\mathscr C)\lambda_w(\mathscr C)\tag{8.69}$$
$$=\sum_{\mathscr C}P(\mathscr C)\lambda_1(\mathscr C)\tag{8.70}$$
$$=\Pr(\mathscr E|W=1).\tag{8.71}$$
- Define $E_i=\{(X^n(i),Y^n)\in A_\epsilon^{(n)}\}$, $i\in\{1,\dots,2^{nR}\}$ (8.72), where $Y^n$ results from sending $X^n(1)$. An error occurs if $E_1^c$ occurs or $E_2\cup\cdots\cup E_{2^{nR}}$ occurs. By the union bound:
$$\Pr(\mathscr E|W=1)=P(E_1^c\cup E_2\cup\cdots\cup E_{2^{nR}})\tag{8.73}$$
$$\le P(E_1^c)+\sum_{i=2}^{2^{nR}}P(E_i).\tag{8.74}$$
- Joint AEP gives $P(E_1^c)\to0$, so $P(E_1^c)\le\epsilon$ for large $n$ (8.75).
- For $i\ne1$, $X^n(1)$ and $X^n(i)$ are independent, so $Y^n$ and $X^n(i)$ are too. Thus $P(E_i)\le2^{-n(I(X;Y)-3\epsilon)}$ by the joint AEP. Then:
$$P(\mathscr E)=P(\mathscr E|W=1)\le P(E_1^c)+\sum_{i=2}^{2^{nR}}P(E_i)\tag{8.76}$$
$$\le\epsilon+\sum_{i=2}^{2^{nR}}2^{-n(I(X;Y)-3\epsilon)}\tag{8.77}$$
$$=\epsilon+(2^{nR}-1)2^{-n(I(X;Y)-3\epsilon)}\tag{8.78}$$
$$\le\epsilon+2^{3n\epsilon}2^{-n(I(X;Y)-R)}\tag{8.79}$$
$$\le2\epsilon\tag{8.80}$$
 if $n$ is sufficiently large and $R<I(X;Y)-3\epsilon$ (p. 202). (Step 8.78→8.79: $2^{nR}-1\le2^{nR}$; added step.)
- So if $R<I(X;Y)$, one can choose $\epsilon$ and $n$ so that the error averaged over codebooks and codewords is $<2\epsilon$ (p. 202).

**Code selection (p. 202).**
1. Take $p(x)=p^*(x)$, the capacity-achieving distribution. Then $R<I(X;Y)$ becomes $R<C$.
2. Since the average over codebooks is $\le2\epsilon$, at least one codebook $\mathscr C^*$ has $P_e^{(n)}(\mathscr C^*)\le2\epsilon$. It could be found by exhaustive search.
3. Discard the worst half of the codewords of $\mathscr C^*$. From
$$2\epsilon\ge\frac1{2^{nR}}\sum_i\lambda_i(\mathscr C^*),\tag{8.81}$$
 at least half the indices have $\lambda_i<4\epsilon$ (otherwise they alone would contribute more than $2\epsilon$ to the sum). So the best half has maximal error $<4\epsilon$. Reindexed, this gives $2^{nR-1}$ codewords, and the rate changes from $R$ to $R-\tfrac1n$, negligible for large $n$.
- Result: a code of rate $R'=R-\tfrac1n$ with $\lambda^{(n)}\le4\epsilon$, which proves achievability of any rate below capacity (p. 202).

*Intuition note.* Averaging over random codes shows that the average code is good, hence at least one code is good. Discarding the worst half converts "good on average" to "good for every message". Random coding is a proof method, not a signalling method (p. 202, final paragraph, which is cut off at the end of this part).

## Toy example (ours, not from the text)
BSC with $p=0.1$, block length $n=100$.
- $H(0.1)=-0.1\log_2 0.1-0.9\log_2 0.9=0.1(3.3219)+0.9(0.1520)=0.3322+0.1368=0.4690$ bits.
- With uniform input, $H(Y)=1$, so $I=1-0.4690=0.5310$. This equals $C=1-H(p)$ (8.7).
- Counting (8.4 heuristic): typical outputs $\approx2^{100\cdot1}=2^{100}$. Each input's cloud has $\approx2^{100\cdot0.469}=2^{46.9}$ outputs. Number of non-overlapping clouds $\approx2^{100}/2^{46.9}=2^{53.1}=2^{100\cdot0.531}$.
- So about $2^{53}$ messages, i.e. rate $\approx0.53$ bit per use, can be told apart. Rate $R=0.4$ would use $2^{40}$ codewords. A random rival is jointly typical with probability about $2^{-100(0.531-3\epsilon)}$, so the union bound over $2^{40}$ rivals is about $2^{40-53.1+300\epsilon}$, which is small if $\epsilon$ is small (the (8.79) argument).

## Concepts
- [[channel-capacity]] — $\max_{p(x)}I(X;Y)$ ("information" capacity); the operational version is the supremum of achievable rates, and they are equal (pp. 184, 194)
- [[noisy-channel]] — discrete channel $(\mathcal X,p(y|x),\mathcal Y)$, memoryless if output depends only on current input (p. 184)
- [[mutual-information]] — $I(X;Y)=H(Y)-H(Y|X)$, concave in $p(x)$, the quantity maximized (pp. 184, 191)
- [[typical-set-aep]] — here the joint AEP: jointly typical set $A_\epsilon^{(n)}$ with about $2^{nH(X,Y)}$ members (p. 195)
- [[noisy-channel-coding-theorem]] — Thm 8.7.1: rates below $C$ achievable; converse proved later (p. 198)
- [[redundancy]] — added in a controlled way during transmission to fight errors (p. 184)
- [[joint-typicality]] (new) — pair $(x^n,y^n)$ whose three empirical entropies are within $\epsilon$ of $H(X),H(Y),H(X,Y)$ (p. 195)
- [[symmetric-channel]] (new) — rows are permutations of each other and columns too; weakly symmetric: every row a permutation of every other row, and equal column sums; capacity $\log|\mathcal Y|-H(\text{row})$ (p. 190)
- [[random-coding]] (new) — proof technique: draw the codebook i.i.d. and average the error, to show a good code exists (pp. 198, 202)
- [[code-rate]] (new) — $R=\frac{\log M}{n}$ bits per transmission for an $(M,n)$ code (p. 194)
- [[maximal-vs-average-error]] (new) — $\lambda^{(n)}=\max_i\lambda_i$ versus $P_e^{(n)}=\frac1M\sum\lambda_i$; $P_e^{(n)}\le\lambda^{(n)}$ (p. 194)

## Canonical instances
- [[noiseless-binary-channel]] — $C=1$ bit (p. 185)
- [[noisy-typewriter]] — $C=\log13$ (pp. 185–186)
- [[binary-symmetric-channel]] — $C=1-H(p)$ (p. 187)
- [[binary-erasure-channel]] — $C=1-\alpha$; feedback by retransmission achieves it (pp. 187–189)
- [[weakly-symmetric-channel-example]] — matrix (8.24) (p. 190)

## Bridges (candidates)
- [structural-analogy] Random-coding existence argument ↔ probabilistic method in combinatorics: average over random objects to prove one good object exists.
- [structural-analogy] Joint-typicality counting ($2^{nH(Y)}/2^{nH(Y|X)}=2^{nI}$) ↔ sphere-packing counts in coding theory: both count disjoint decoding regions in output space (the author's own text only gives the heuristic).
- [metaphor] Capacity as a rate limit ↔ rational inattention: agents limited by an information-processing rate.

## Questions this raises
- Why is the converse ($R\le C$ for any code with vanishing error) true? The text defers it to §8.9.
- How can feedback help in practice if it does not raise the capacity of a DMC, as claimed on p. 189?
- How close does joint-typicality decoding get to maximum-likelihood decoding at finite $n$?
- What does the Arimoto–Blahut iteration look like for channels with no closed form?

## Reading notes
- This part starts at the chapter opening (printed p. 183) and ends mid-sentence on printed p. 202, in the closing remark on random coding. Later material is not in this part. The text points ahead to the converse in §8.9 (p. 199), to a later proof about feedback (p. 189), and to the last section of the chapter on treating compression and transmission separately (p. 184).
- Offset: printed = pdf − 22. Page labels already give printed numbers.
- The PDF is the 1991 first edition, as printed on p. 183 (copyright 1991, ISBN 0-471-06259-6), not the 2006 second edition. The metadata cites the 2006 edition.
- The OCR text layer is garbled in many equations. I used the images; all equations, including (8.66)–(8.68), are legible there.
- Fig. 8.3 labels (probabilities $\tfrac12,\tfrac12,\tfrac13,\tfrac23$) are read from the image.
- p. 194 states that "in the next section" a small average error implies a small maximal error. In the pages given, this is done in step 3 on p. 202 (§8.7).
- The converse's statement uses $\lambda^{(n)}$ for the maximal error, but the text layer reads it as $\mathrm{A}^{(n)}$; I treated this as an OCR artefact.
