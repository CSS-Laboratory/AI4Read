---
id: cover-2006-elements/ch14-network-p4
work: cover-2006-elements
unit: "14 Network Information Theory (part 4/4): §14.9 Rate distortion with side information, §14.10 General multiterminal networks, chapter summary, problems, historical notes"
pages: 438–458
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
# Rate distortion with side information; the cut-set bound for general networks

## L0 — One line
When the decoder also sees correlated side information Y, describing X within distortion D costs $R_Y(D)=\min\,[I(X;W)-I(Y;W)]$ bits (Wyner–Ziv), and in any multiterminal network the information flow across every cut is bounded by a conditional mutual information, though this bound is not always achievable.

## L1 — The gist (≤ 120 words)
How many bits are needed to describe X within distortion D if the decoder has side information Y? Theorem 14.9.1 answers with a single-letter formula that equals H(X|Y) at D = 0. The proof combines rate-distortion coding with random binning. The chapter then gives a cut-set upper bound (one bound for each split of the nodes into two groups) on achievable rates in a general network. The bound is tight for some channels, such as the multiple access channel (several senders, one receiver) with product inputs and a convex hull. It is not achievable in general. Source–channel separation fails for multi-user channels, and feedback can enlarge multi-user capacity regions. Rate distortion for two correlated sources is still open.

**Prerequisites:** mutual information and chain rule; Fano's inequality; strong typicality; Jensen's inequality and convexity; Slepian–Wolf and multiple access channel results from earlier in Chapter 14.

## L2 — Key ideas
- $R_Y(D)$ is the least rate for distortion D when only the decoder sees side information Y. It is at most R(D), and $R_Y(0)=H(X|Y)$, the Slepian–Wolf rate (the lossless rate when only the decoder sees Y) (p. 438).
- Theorem 14.9.1 gives $R_Y(D)=\min_{p(w|x)}\min_f\,[I(X;W)-I(Y;W)]$ under a distortion constraint. $R_Y(D)$ is non-increasing and convex in D (pp. 438–439).
- The converse uses $W_i=(T,Y^{i-1},Y_{i+1}^n)$, the Markov chain $W_i\to X_i\to Y_i$, and Jensen's inequality via convexity (pp. 440–441).
- Achievability sends only a bin index of a rate-distortion codebook. The side information at the decoder picks the right codeword in the bin (p. 442).
- Rate distortion for two correlated sources (distortion on both) contains the earlier distributed-coding problems as special cases. Its region is unknown (p. 444).
- Theorem 14.10.1 (cut-set bound): for any cut (a split of the nodes into S and its complement $S^c$), achievable rates across it obey $\sum R^{(ij)}\le I(X^{(S)};Y^{(S^c)}|X^{(S^c)})$ for some joint input distribution (p. 445).
- The bound is not achievable in general. For the multiple access channel (several senders, one receiver) it matches the capacity region when the inputs are restricted to product distributions and the convex hull is taken. For the relay channel (a sender, a receiver and a helper node) it gives an upper bound that is the capacity of the physically degraded relay channel and of the relay channel with feedback (pp. 447–448).
- In the multi-user case, the condition that the Slepian–Wolf region meets the multiple access capacity region is sufficient for sending a distributed source but, as an example shows, not necessary. The author's reason is that capacity grows with input correlation while Slepian–Wolf encoding removes it (p. 449). Feedback can enlarge multi-user capacity regions even for memoryless channels (p. 450).

## L3 — Walkthrough

### 14.9 Rate distortion with side information (pp. 438–444)
**Setup.** $(X_i,Y_i)$ are i.i.d. $\sim p(x,y)$. The encoder sees $X^n$ only. The decoder sees $Y^n$ and the index (Figure 14.32) (p. 438).

**Definition.** $R_Y(D)$ is the infimum of rates R such that there exist maps $i_n:\mathcal X^n\to\{1,\dots,2^{nR}\}$ and $g_n:\mathcal Y^n\times\{1,\dots,2^{nR}\}\to\hat{\mathcal X}^n$ with
$$\limsup_{n\to\infty} E\,d\big(X^n,g_n(Y^n,i_n(X^n))\big)\le D. \tag{14.279}$$
The author notes that side information can only help, so $R_Y(D)\le R(D)$. At zero distortion this is the Slepian–Wolf problem, so $R_Y(0)=H(X|Y)$ (p. 438).

**Theorem 14.9.1.** Let $(X,Y)\sim p(x,y)$ i.i.d. and $d(x^n,\hat x^n)=\frac1n\sum d(x_i,\hat x_i)$. Then
$$R_Y(D)=\min_{p(w|x)}\ \min_f\ \big(I(X;W)-I(Y;W)\big) \tag{14.280}$$
The minimum is over functions $f:\mathcal Y\times\mathcal W\to\hat{\mathcal X}$ and pmfs $p(w|x)$ with $|\mathcal W|\le|\mathcal X|+1$, such that
$$\sum_x\sum_w\sum_y p(x,y)\,p(w|x)\,d\big(x,f(y,w)\big)\le D. \tag{14.281}$$
Here f is the decoding map. It combines the encoded X-description with Y to give the output symbol (pp. 438–439).

*Intuition note.* W is a description of X. Describing it costs $I(X;W)$, but the decoder already knows part of it through Y, worth $I(Y;W)$. The net cost is the difference.

**Lemma 14.9.1.** $R_Y(D)$ is a non-increasing convex function of D (p. 439).
- *Monotone:* the domain of minimization grows with D (p. 439).
- *Convex:* the double minimization makes this more involved than without side information, so the author only outlines it (p. 439). Let $(W_1,f_1)$, $(W_2,f_2)$ achieve the minima for $D_1$, $D_2$. Let Q be independent of $X,Y,W_1,W_2$, with $\Pr(Q=1)=\lambda$, $\Pr(Q=2)=1-\lambda$. Define $W=(Q,W_Q)$ and $f(W,Y)=f_Q(W_Q,Y)$. Then
$$D=Ed(X,\hat X)=\lambda E d(X,f_1(W_1,Y))+(1-\lambda)Ed(X,f_2(W_2,Y))=\lambda D_1+(1-\lambda)D_2 \tag{14.282–14.284}$$
$$\begin{aligned}I(W;X)-I(W;Y)&=H(X)-H(X|W)-H(Y)+H(Y|W)\\&=H(X)-H(X|W_Q,Q)-H(Y)+H(Y|W_Q,Q)\\&=H(X)-\lambda H(X|W_1)-(1-\lambda)H(X|W_2)-H(Y)+\lambda H(Y|W_1)+(1-\lambda)H(Y|W_2)\\&=\lambda\big(I(W_1;X)-I(W_1;Y)\big)+(1-\lambda)\big(I(W_2;X)-I(W_2;Y)\big)\end{aligned}\tag{14.285–14.288}$$
Since this W is feasible for $D=\lambda D_1+(1-\lambda)D_2$:
$$R_Y(D)=\min_{U:\,Ed\le D}\big(I(U;X)-I(U;Y)\big)\le I(W;X)-I(W;Y)=\lambda R_Y(D_1)+(1-\lambda)R_Y(D_2) \tag{14.289–14.291}$$
(pp. 439–440).

**Converse.** Take any code with side information: $T=f_n(X^n)$, with range $\{1,\dots,2^{nR}\}$. Let $g_{ni}$ be the i-th output symbol. We must show $Ed(X^n,g_n(Y^n,f_n(X^n)))\le D\Rightarrow R\ge R_Y(D)$ (p. 440). Define $W_i=(T,Y^{i-1},Y_{i+1}^n)$. Then:
$$\begin{aligned}
nR&\overset{(a)}{\ge}H(T)\overset{(b)}{\ge}H(T|Y^n)\ge I(X^n;T|Y^n)\overset{(c)}{=}\sum_{i=1}^n I(X_i;T|Y^n,X^{i-1})\\
&=\sum_i H(X_i|Y^n,X^{i-1})-H(X_i|T,Y^n,X^{i-1})\\
&\overset{(d)}{=}\sum_i H(X_i|Y_i)-H(X_i|T,Y^{i-1},Y_i,Y_{i+1}^n,X^{i-1})\\
&\overset{(e)}{\ge}\sum_i H(X_i|Y_i)-H(X_i|T,Y^{i-1},Y_i,Y_{i+1}^n)\overset{(f)}{=}\sum_i H(X_i|Y_i)-H(X_i|W_i,Y_i)\\
&\overset{(g)}{=}\sum_i I(X_i;W_i|Y_i)=\sum_i H(W_i|Y_i)-H(W_i|X_i,Y_i)\overset{(h)}{=}\sum_i H(W_i|Y_i)-H(W_i|X_i)\\
&=\sum_i I(W_i;X_i)-I(W_i;Y_i)\overset{(i)}{\ge}\sum_i R_Y\big(Ed(X_i,g'_{ni}(W_i,Y_i))\big)\\
&=n\frac1n\sum_i R_Y(\cdot)\overset{(j)}{\ge}nR_Y\Big(E\tfrac1n\sum_i d(X_i,g'_{ni}(W_i,Y_i))\Big)\overset{(k)}{\ge}nR_Y(D)
\end{aligned}\tag{14.292–14.308}$$
Reasons (p. 441): (a) range of T; (b), (e) conditioning reduces entropy; (c) chain rule; (d) $X_i$ is independent of the other Y's and X's given $Y_i$; (g) definition of mutual information; (h) $W_i\to X_i\to Y_i$ is a Markov chain; (i) definition of $R_Y$, since $\hat X_i=g_{ni}(T,Y^n)=g'_{ni}(W_i,Y_i)$; (j) Jensen and Lemma 14.9.1; (k) definition of D. *(Added step: (k) also uses that $R_Y$ is non-increasing and that the average distortion is at most D.)*

*Intuition note.* The total rate $nR$ is at least the sum over symbols of $I(W_i;X_i)-I(W_i;Y_i)$, and each such term is at least $R_Y$ at the distortion actually achieved at that symbol. Convexity (Jensen) lets us average these terms.

**Achievability** (outline; details are left to Wyner and Ziv [284]) (pp. 442–443). The proof parallels the strong-typicality proof of the rate distortion theorem. Instead of sending the index of the jointly typical codeword, the encoder sends the bin index of that codeword. If a bin holds few enough codewords, the side information isolates the right one (p. 442).
- *Codebook.* Fix $p(w|x)$ and $f(w,y)$; compute $p(w)=\sum_x p(x)p(w|x)$. Let $R_1=I(X;W)+\epsilon$. Generate $2^{nR_1}$ i.i.d. codewords $W^n(s)\sim\prod p(w_i)$, $s\in\{1,\dots,2^{nR_1}\}$. Let $R_2=I(X;W)-I(Y;W)+5\epsilon$. Assign each index s uniformly at random to one of $2^{nR_2}$ bins. Let $B(i)$ be bin i. There are about $2^{n(R_1-R_2)}$ indices per bin (p. 442).
- *Encoding.* Find s with $(X^n,W^n(s))\in A_\epsilon^{*(n)}$. If none, set $s=1$. If several, take the lowest. Send the bin index of s (p. 442).
- *Decoding.* Find s in the received bin with $(W^n(s),Y^n)\in A_\epsilon^{*(n)}$. If it is unique, output $\hat X_i=f(W_i,Y_i)$. Otherwise output an arbitrary default sequence (p. 442).
- *Error events* (pp. 442–443):
  1. $(X^n,Y^n)$ not typical: small for large n by the weak law of large numbers.
  2. No s with $(X^n,W^n(s))$ typical: small if $R_1>I(W;X)$ \tag{14.309}.
  3. $(X^n,W^n(s))$ typical but $(W^n(s),Y^n)$ not: small for large n by the Markov lemma (Lemma 14.8.1).
  4. Another $s'$ in the same bin with $(W^n(s'),Y^n)$ typical. A random $W^n$ is jointly typical with $Y^n$ with probability $\approx 2^{-nI(Y;W)}$, so
  $$\Pr(\exists s'\in B(i):(W^n(s'),Y^n)\in A_\epsilon^{*(n)})\le 2^{n(R_1-R_2)}2^{-n(I(W;Y)-3\epsilon)}\tag{14.310}$$
  This goes to zero because $R_1-R_2<I(Y;W)-3\epsilon$.
  5. If s is decoded correctly, the Markov lemma gives $(X^n,Y^n,W^n)$ typical. The empirical joint distribution of $(X^n,\hat X^n)$ is then close to the one that achieves distortion D.

Hence, with high probability, the distortion between $X^n$ and $\hat X^n$ is close to $nD$ (as printed) (p. 443).

*Intuition note.* Binning is the same trick as in Slepian–Wolf. The encoder withholds information the decoder can recover from Y, so the rate falls from $I(X;W)$ to $I(X;W)-I(Y;W)$.

**Open problem.** Rate distortion for correlated sources (Figure 14.33) has two encoders and one decoder. It is Slepian–Wolf with distortion in both X and Y. The three distributed source-coding problems above are special cases. The general rate-distortion region is unknown (p. 444).

### 14.10 General multiterminal networks (pp. 444–450)
**Model.** There are m nodes. Node i has transmitted variable $X^{(i)}$ and received variable $Y^{(i)}$. Superscripts are nodes and subscripts are times. Node i sends to node j at rate $R^{(ij)}$ with message $W^{(ij)}\in\{1,\dots,2^{nR^{(ij)}}\}$. All messages are independent and uniform. The channel is memoryless, given by $p(y^{(1)},\dots,y^{(m)}|x^{(1)},\dots,x^{(m)})$, which captures noise and interference (pp. 444–445).
- *Encoders:* $X_k^{(i)}(W^{(i1)},\dots,W^{(im)},Y_1^{(i)},\dots,Y_{k-1}^{(i)})$, $k=1,\dots,n$.
- *Decoders:* $\hat W^{(ji)}(Y_1^{(i)},\dots,Y_n^{(i)},W^{(i1)},\dots,W^{(im)})$, $j=1,\dots,m$. Node i uses all its received symbols and its own messages to estimate messages meant for it.
- Error probability: $P_e^{(n)(ij)}=\Pr\big(\hat W^{(ij)}(Y^{(j)},W^{(j1)},\dots,W^{(jm)})\ne W^{(ij)}\big)$ \tag{14.311}.
- $\{R^{(ij)}\}$ is *achievable* if encoders and decoders exist with $P_e^{(n)(ij)}\to0$ for all i, j (p. 445).

**Theorem 14.10.1 (cut-set bound).** If $\{R^{(ij)}\}$ is achievable, there is some joint $p(x^{(1)},\dots,x^{(m)})$ such that
$$\sum_{i\in S,\,j\in S^c}R^{(ij)}\le I\big(X^{(S)};Y^{(S^c)}\,\big|\,X^{(S^c)}\big)\quad\text{for all }S\subset\{1,\dots,m\}\tag{14.312}$$
(p. 445).

**Proof** (same lines as the multiple access converse). Let $T=\{(i,j):i\in S,j\in S^c\}$ and $T^c$ the other links. Then
$$\begin{aligned}
n\!\!\sum_{i\in S,j\in S^c}\!\!R^{(ij)}&\overset{(a)}{=}\sum H(W^{(ij)})\overset{(b)}{=}H(W^{(T)})\overset{(c)}{=}H(W^{(T)}|W^{(T^c)})\\
&=I(W^{(T)};Y_1^{(S^c)},\dots,Y_n^{(S^c)}|W^{(T^c)})+H(W^{(T)}|Y_1^{(S^c)},\dots,Y_n^{(S^c)},W^{(T^c)})\\
&\overset{(d)}{\le}I(W^{(T)};Y_1^{(S^c)},\dots,Y_n^{(S^c)}|W^{(T^c)})+n\epsilon_n\\
&\overset{(e)}{=}\sum_{k=1}^n I(W^{(T)};Y_k^{(S^c)}|Y_1^{(S^c)},\dots,Y_{k-1}^{(S^c)},W^{(T^c)})+n\epsilon_n\\
&\overset{(f)}{=}\sum_k H(Y_k^{(S^c)}|Y_1^{(S^c)},\dots,Y_{k-1}^{(S^c)},W^{(T^c)})-H(Y_k^{(S^c)}|Y_1^{(S^c)},\dots,Y_{k-1}^{(S^c)},W^{(T^c)},W^{(T)})+n\epsilon_n\\
&\overset{(g)}{\le}\sum_k H(Y_k^{(S^c)}|Y_1^{(S^c)},\dots,Y_{k-1}^{(S^c)},W^{(T^c)},X_k^{(S^c)})-H(Y_k^{(S^c)}|Y_1^{(S^c)},\dots,Y_{k-1}^{(S^c)},W^{(T^c)},W^{(T)},X_k^{(S)},X_k^{(S^c)})+n\epsilon_n\\
&\overset{(h)}{\le}\sum_k H(Y_k^{(S^c)}|X_k^{(S^c)})-H(Y_k^{(S^c)}|X_k^{(S)},X_k^{(S^c)})+n\epsilon_n=\sum_k I(X_k^{(S)};Y_k^{(S^c)}|X_k^{(S^c)})+n\epsilon_n\\
&\overset{(i)}{=}n\frac1n\sum_k I(X_Q^{(S)};Y_Q^{(S^c)}|X_Q^{(S^c)},Q=k)+n\epsilon_n\overset{(j)}{=}nI(X_Q^{(S)};Y_Q^{(S^c)}|X_Q^{(S^c)},Q)+n\epsilon_n\\
&=n\big(H(Y_Q^{(S^c)}|X_Q^{(S^c)},Q)-H(Y_Q^{(S^c)}|X_Q^{(S)},X_Q^{(S^c)},Q)\big)+n\epsilon_n\\
&\overset{(k)}{\le}n\big(H(Y_Q^{(S^c)}|X_Q^{(S^c)})-H(Y_Q^{(S^c)}|X_Q^{(S)},X_Q^{(S^c)},Q)\big)+n\epsilon_n\\
&\overset{(l)}{\le}n\big(H(Y_Q^{(S^c)}|X_Q^{(S^c)})-H(Y_Q^{(S^c)}|X_Q^{(S)},X_Q^{(S^c)})\big)+n\epsilon_n=nI(X_Q^{(S)};Y_Q^{(S^c)}|X_Q^{(S^c)})+n\epsilon_n
\end{aligned}\tag{14.313–14.330}$$
Reasons (p. 447): (a) uniform messages; (b) definition of $W^{(T)}$ and independence; (c) independence of $W^{(T)}$ and $W^{(T^c)}$; (d) Fano, since $W^{(T)}$ can be decoded from $Y^{(S^c)}$ and $W^{(T^c)}$; (e) chain rule; (f) definition of mutual information; (g) $X_k^{(S^c)}$ is a function of past $Y^{(S^c)}$ and $W^{(T^c)}$, and extra conditioning reduces the second term; (h) $Y_k^{(S^c)}$ depends only on the current inputs; (i) time-sharing variable Q uniform on $\{1,\dots,n\}$; (j) definition of mutual information; (k) conditioning reduces entropy; (l) $Y_Q$ depends only on the current inputs and is conditionally independent of Q. So random variables $X^{(S)},X^{(S^c)}$ with some joint distribution satisfy the theorem (p. 447).

*Intuition note.* The author says the theorem has a simple max-flow–min-cut interpretation: the flow across any boundary is at most what the inputs on one side can convey to the outputs on the other, given the inputs on that other side (p. 447). The author states that these bounds are not achievable even for some simple channels, so the cut bound need not be reached.

**Limits of the bound** (p. 447). If the bounds were achievable, information flow in networks would be solved. They are not achievable even for some simple channels (p. 447).
- *Multiple access channel.* For two users the bounds become
$$R_1\le I(X_1;Y|X_2),\quad R_2\le I(X_2;Y|X_1),\quad R_1+R_2\le I(X_1,X_2;Y)\tag{14.331–14.333}$$
for some joint $p(x_1,x_2)p(y|x_1,x_2)$. They coincide with the capacity region if the input distribution is restricted to a product distribution and the convex hull is taken (Theorem 14.3.1) (pp. 447–448).
- *Relay channel.* The bounds give the upper bound of Theorem 14.7.1 with different choices of subsets (Figure 14.35):
$$C\le\sup_{p(x,x_1)}\min\{I(X,X_1;Y),\,I(X;Y,Y_1|X_1)\}\tag{14.334}$$
This is the capacity of a physically degraded relay channel and of the relay channel with feedback [67] (p. 448).

**Two single-user features that fail in networks** (pp. 448–450).
- *Source–channel separation.* For a single user (Section 8.13), the source can be sent noiselessly iff the entropy rate is below capacity. The author expects the multi-user analogue: a distributed source can be sent iff its noiseless-coding rate region lies within the channel's capacity region (p. 448). For a distributed source (U,V) over a multiple access channel (Figure 14.36), combining Slepian–Wolf with MAC capacity shows transmission is possible with low error probability if
$$H(U|V)\le I(X_1;Y|X_2,Q),\quad H(V|U)\le I(X_2;Y|X_1,Q),\quad H(U,V)\le I(X_1,X_2;Y,Q)\tag{14.335–14.337}$$
for some $p(q)p(x_1|q)p(x_2|q)p(y|x_1,x_2)$. This holds exactly when the Slepian–Wolf region meets the MAC capacity region (pp. 448–449). It is not necessary. Take the source of Example 14.4 over the binary erasure MAC (Example 14.3). The Slepian–Wolf region does not meet the capacity region, yet setting $X_1=U$, $X_2=V$ lets Y reveal (U,V) without error (p. 449). The reason: MAC capacity grows with correlation between inputs, while Slepian–Wolf encoding removes correlation. Cover, El Gamal and Salehi [69] gave an achievable region that preserves correlation. Han and Costa [131] gave a similar one for broadcast channels (p. 449).
- *Feedback.* Theorem 8.12.1: feedback does not increase the capacity of a single-user discrete memoryless channel. For channels with memory, feedback helps because the sender can predict the noise. For multi-user channels, feedback increases the capacity region even when memoryless (Gaarder and Wolf [117], binary erasure MAC) (pp. 449–450). Feedback acts as a channel between the senders. They can decode each other before the receiver does, then cooperate at the higher cooperative rate. Cover and Leung [73] gave an achievable region. Willems [273] showed it is the capacity for a class including the binary erasure MAC. Ozarow [204] found the capacity region of the two-user Gaussian MAC with feedback. The problem is closely related to the capacity of a two-way channel with common output (p. 450).

The chapter closes: there is no unified theory of network information flow yet, but a complete one would have wide implications for communication and computation (p. 450).

### Chapter 14 summary (pp. 450–452)
Collected results, as printed:
- **MAC:** the capacity region is the closure of the convex hull of $R_1<I(X_1;Y|X_2)$, $R_2<I(X_2;Y|X_1)$, $R_1+R_2<I(X_1,X_2;Y)$ over $p_1(x_1)p_2(x_2)$ (14.338–14.340). The m-user version is $R(S)\le I(X(S);Y|X(S^c))$ over product distributions (14.341) (p. 450).
- **Gaussian MAC:** $R_1\le C(P_1/N)$, $R_2\le C(P_2/N)$, $R_1+R_2\le C((P_1+P_2)/N)$, with $C(x)=\frac12\log(1+x)$ (14.342–14.345) (p. 451).
- **Slepian–Wolf:** separate descriptions with a common decoder succeed iff $R_1>H(X|Y)$, $R_2>H(Y|X)$, $R_1+R_2>H(X,Y)$ (14.346–14.348) (p. 451).
- **Degraded broadcast channel** $X\to Y_1\to Y_2$: convex hull of the closure of $R_2\le I(U;Y_2)$, $R_1\le I(X;Y_1|U)$ over $p(u)p(x|u)p(y_1,y_2|x)$ (14.349–14.350) (p. 451).
- **Physically degraded relay channel:** $C=\sup_{p(x,x_1)}\min\{I(X,X_1;Y),I(X;Y_1|X_1)\}$ (14.351) (p. 451).
- **Source coding with side information:** with Y encoded at $R_2$ and X at $R_1$, X is recovered iff $R_1\ge H(X|U)$, $R_2\ge I(Y;U)$ for some $p(y,u)$ with $X\to Y\to U$ (14.352–14.353) (pp. 451–452).
- **Rate distortion with side information:** formula (14.354–14.355), the same as Theorem 14.9.1 (p. 452).

### Problems and historical notes (pp. 452–458)
The 15 problems cover cooperative MAC capacity, MAC examples, cut-set reading of the MAC region, Gaussian MAC achievability and converse, an "unusual" MAC needing timesharing, broadcast-channel convexity and converses, Slepian–Wolf examples, channels with unknown parameters, and the two-way channel (pp. 452–457). The historical notes credit the chapter to El Gamal and Cover [98] and attribute rate distortion with side information to Wyner and Ziv [284] (pp. 457–458).

## Toy example (ours, not from the text)
Let X be a uniform bit. Let Y be X passed through a binary symmetric channel with flip probability 0.1. Use Hamming distortion.

1. *D = 0.* Choose $W=X$ and $f(y,w)=w$. The distortion is 0. The objective is $I(X;W)-I(Y;W)=H(X)-I(X;Y)=H(X|Y)$. With $H(0.1)=0.1(3.3219)+0.9(0.1520)=0.3322+0.1368=0.469$, we get $R_Y(0)\le 0.469$ bits. This matches the Slepian–Wolf value $H(X|Y)$ (p. 438).
2. *D = 0.1.* Choose W constant and $f(y,w)=y$. The decoder just outputs Y, so $E\,d=\Pr(Y\ne X)=0.1$. The objective is $0-0=0$. So $R_Y(0.1)\le 0$ and, since rates are not negative, $R_Y(0.1)=0$.
3. *D = 0.05.* The convexity lemma with $\lambda=0.5$ gives $D=0.5\cdot0+0.5\cdot0.1=0.05$ and $R_Y(0.05)\le0.5(0.469)+0.5(0)=0.2345$ bits. This is the time-sharing mixture Q of the two schemes, as in the proof (p. 439).

## Concepts
- [[rate-distortion-function]] — minimum bits to describe a source within average distortion D. Here it gets a side-information version (p. 438).
- [[wyner-ziv-rate-distortion]] (new) — $R_Y(D)=\min[I(X;W)-I(Y;W)]$ with decoder side information Y (p. 438).
- [[random-binning]] (new) — hashing codeword indices into bins and sending only the bin index. The decoder's side information resolves the bin (p. 442).
- [[markov-lemma]] (new) — a lemma from an earlier part (Lemma 14.8.1, not visible here), cited in events 3 and 5 of the achievability proof to conclude joint typicality of the codeword with $Y^n$ and of $(X^n,Y^n,W^n)$ (p. 443).
- [[cut-set-bound]] (new) — $\sum R^{(ij)}\le I(X^{(S)};Y^{(S^c)}|X^{(S^c)})$ across a cut S (p. 445).
- [[multiterminal-network]] (new) — m nodes, each with an input and an output, and a memoryless channel $p(y^{(1..m)}|x^{(1..m)})$ (p. 444).
- [[time-sharing-variable]] (new) — random Q uniform on $\{1,\dots,n\}$ used to turn a per-letter sum into a single-letter mutual information (p. 447).
- [[source-channel-separation]] — holds for one user. For a MAC it is sufficient to combine Slepian–Wolf and MAC capacity, but not necessary (pp. 448–449).
- [[fanos-inequality]] — used in step (d) of the cut-set proof (p. 447).
- [[channel-capacity]] — here, capacity regions of multi-user channels. Feedback can enlarge them, unlike the single-user memoryless case (p. 450).
- [[slepian-wolf-coding]] (new) — separate encoding of correlated sources at rates $R_1>H(X|Y)$, $R_2>H(Y|X)$, $R_1+R_2>H(X,Y)$ (p. 451).

## Canonical instances
- [[binary-erasure-mac]] — Y reveals $(X_1,X_2)$ when sources are sent uncoded. This shows separation is not necessary (p. 449).
- [[relay-channel]] — cut-set bound with $C\le\sup\min\{I(X,X_1;Y),I(X;Y,Y_1|X_1)\}$ (p. 448).
- [[gaussian-mac]] — rate region with $C(x)=\frac12\log(1+x)$ (p. 451).
- [[unusual-mac]] — a MAC with $Y=1$ w.p. ½ when $(X_1,X_2)=(1,1)$, where timesharing strictly enlarges the region (Problem 6, p. 453).
- [[binary-multiplying-channel]] — two-way channel $Y_1=Y_2=X_1X_2$ with unequal inner and outer bounds (p. 457).

## Bridges (candidates)
- [structural-analogy] cut-set bound ↔ graph theory: max-flow–min-cut — the text itself offers this reading, with mutual information in place of edge capacity.
- [metaphor] random binning ↔ computer science: hashing — only a bin label is sent, and extra knowledge at the receiver disambiguates it.
- [same-math] $I(X;W)-I(Y;W)$ under the Markov chain $W\to X\to Y$ ↔ information-theory: the Slepian–Wolf rate (the case $W=X$) — at D = 0 it equals H(X|Y).
- [metaphor] feedback as an inter-sender channel ↔ economics/game theory: cooperation raising joint payoff — senders gain by pooling what each learns.

## Questions this raises
- Why is the Wyner–Ziv problem solved while the general two-source rate-distortion problem is not?
- When is the cut-set bound tight? Which network structures close the gap?
- Can correlation-preserving joint source–channel schemes be characterized exactly?
- How does feedback-induced sender cooperation scale beyond two users?

## Exercises worth doing
- Ex. 1 (p. 452) — cooperative MAC capacity and comparison with the non-cooperative region for the binary erasure MAC — difficulty: easy
- Ex. 3 (p. 452) — cut-set reading of the MAC region; shows the bound in a concrete graph — difficulty: easy
- Ex. 6 (p. 453) — an "unusual" MAC where timesharing is strictly needed — difficulty: medium
- Ex. 9 (p. 454) — Slepian–Wolf region for $Y=X\oplus Z$ — difficulty: medium
- Ex. 14 (p. 456) — BSC with unknown parameter, revealing p to the receiver — difficulty: medium
- Ex. 15 (p. 456) — inner and outer bounds on the two-way channel — difficulty: hard

## Reading notes
- This part starts at §14.9 (printed p. 438) and ends with the chapter's Historical Notes (printed p. 458). Pages: pdf 460–480 = printed 438–458 (printed = pdf − 22). Chapter summary (pp. 450–452), problems (pp. 452–457) and historical notes (pp. 457–458) are included.
- The PDF is the 1991 first edition (running header "NETWORK INFORMATION THEORY"), not the 2006 second edition, so numbering may differ from the 2nd edition.
- The OCR text is badly garbled in equations. I used the page images to correct them. In (14.285)–(14.290) the source mixes commas and semicolons in $I(W,X)$; I wrote $I(W;X)$.
- (14.337) is printed as $I(X_1,X_2;Y,Q)$; presumably $Y|Q$ is intended, but I kept it as printed. The text after the achievability proof says the distortion is "close to nD", presumably total distortion over n symbols. The proof of (14.312) stops at $n\epsilon_n$ without writing the final division by n, which is implicit.
- Example 14.3, Example 14.4, Theorems 14.3.1 and 14.7.1, Lemma 14.8.1 and Section 8.13 are referenced from earlier parts and not visible here, so I do not describe them beyond what these pages say.
