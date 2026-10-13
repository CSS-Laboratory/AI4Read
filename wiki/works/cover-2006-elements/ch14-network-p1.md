---
id: cover-2006-elements/ch14-network-p1
work: cover-2006-elements
unit: "14 Network Information Theory (part 1/4): introduction, §14.1 Gaussian multiple user channels, §14.2 jointly typical sequences (start)"
pages: 374-387
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Network Information Theory: Gaussian multi-user channels and jointly typical sequences

## L0 — One line
When many senders and receivers share a noisy channel, interference, cooperation and feedback arise; Gaussian examples give concrete capacity answers, and an extended joint AEP (a result on which long sequences of several variables are typical together) is the tool for the later proofs.

## L1 — The gist (≤ 120 words)
The chapter asks which rates many senders and receivers can achieve at once over a shared noisy network. No complete theory exists, so the author studies special cases. This part gives an overview of the cases (multiple access, broadcast, relay, interference, two-way), then states Gaussian results without proof. Examples: in the multiple access channel the sum rate $C(mP/N)$ grows without bound in the number of users $m$; in the broadcast channel the better receiver decodes the weaker receiver's message first. The part then extends the joint AEP to any subsets of $k$ random variables. It gives bounds on the size and probability of typical sets and on the probability that conditionally independent sequences are jointly typical.

**Prerequisites:** Gaussian channel capacity $\tfrac12\log(1+P/N)$; typical sets and the AEP; entropy, conditional entropy and mutual information; the law of large numbers.

## L2 — Key ideas (5–10 bullets)
- A network is $m$ nodes; node $i$ sends a symbol depending on its messages and its past received symbols, and the outputs are drawn from $p(y^{(1)},\dots,y^{(m)}\mid x^{(1)},\dots,x^{(m)})$. The general problem is unsolved, so special cases are studied (p. 375).
- Water-pipe flow has a clean answer (Ford–Fulkerson: max flow = min cut). For information, the cut-set bound (a limit set by the total capacity of the edges cut by a cut-set) is an upper bound that is generally not achievable. The relay and cascade channels do admit a max-flow min-cut reading, and no source–channel separation theorem is available (pp. 376–377).
- Gaussian MAC with $m$ users of power $P$: the optimal scheme uses no time division; each transmitter uses all of the bandwidth all of the time. The sum-rate bound is $C(mP/N)$, which goes to infinity with $m$ (p. 379).
- Gaussian broadcast channel: superposition of two codebooks with power split $\alpha$ and $\bar\alpha=1-\alpha$. The weaker receiver treats the other message as noise; the better receiver decodes the weaker one's codeword, subtracts it, then decodes its own (p. 380).
- Gaussian relay channel: cooperation over successive blocks, with the sender and relay sending the same codeword coherently (the signals add as amplitudes, giving received power $(\sqrt{\bar\alpha P}+\sqrt{P_1})^2$). The capacity is the max–min formula (14.16) (pp. 380–382).
- Interference channel: the capacity region (the set of simultaneously achievable rates) is unknown in general, but with high interference it equals the no-interference region. The Gaussian two-way channel splits into two independent channels (pp. 383–384).
- Extended joint AEP: for every subset $S$ of the $k$ variables, $|A_\epsilon^{(n)}(S)|\doteq 2^{n(H(S)\pm2\epsilon)}$; for a typical $\mathbf s_2$, the set of $\mathbf s_1$ jointly typical with it has size at most about $2^{nH(S_1|S_2)}$, and a matching lower bound holds on average over $\mathbf s_2$ (pp. 385–386).
- Conditionally independent sequences with the right pairwise marginals are jointly typical with probability about $2^{-nI(S_1;S_2|S_3)}$ (up to $\pm\epsilon$ terms); this drives error analysis (p. 387).

## L3 — Walkthrough

### Introduction (pp. 374–377)
- **Setting.** Many senders and receivers add interference, cooperation and feedback. Given a channel transition matrix, decide whether sources can be sent over the network. This covers distributed source coding and the capacity region (the set of simultaneously achievable rates). The general problem is unsolved (p. 374).
- **Channel types.**
  - Multiple access channel (MAC): $m$ stations send to one satellite. It is the best understood multi-user channel (pp. 374–375).
  - Broadcast channel: one sender to $m$ receivers. Answers are known only in special cases (p. 375).
  - Relay channel: one source, one destination, intermediate relays.
  - Interference channel: two senders, two receivers, crosstalk.
  - Two-way channel: two sender–receiver pairs sending to each other. Only partial answers are known for these (p. 375).
- **General network model.** Node $i$ sends $x_i$, which depends on its messages and past received symbols. The joint transmission $(x_1,\dots,x_m)$ gives received $(Y_1,\dots,Y_m)\sim p(y^{(1)},\dots,y^{(m)}|x^{(1)},\dots,x^{(m)})$. If $p$ takes only values 0 and 1, the network is deterministic. Sources may be independent, but full generality needs dependent sources (pp. 375–376).
- **Source coding case.** For noiseless, interference-free channels the problem reduces to finding rate sets per source. Simplest case: Slepian–Wolf, where two sources are encoded separately and decoded together; extensions are promised (p. 376).
- **Flow analogy.** For the pipe network of Fig. 14.4, the max flow cannot exceed the total capacity of the edges cut by any cut-set. The figure gives
$$C=\min\{C_1+C_2,\; C_2+C_3+C_4,\; C_4+C_5,\; C_1+C_3+C_5\}.$$
 Ford–Fulkerson shows this is achievable (pp. 376–377).
- **For information flow,** the author proves an upper bound across any cut-set, but it is not achievable in general. Relay and cascade channels do admit a max-flow min-cut interpretation. There is no source–channel separation theorem, touched on in the last section. A complete theory is "a distant goal" (p. 377).
- *Intuition note:* Water obeys max-flow = min-cut, but for information the author says the cut-set bounds are not achievable in general. They remain upper bounds.

### 14.1 Gaussian multiple user channels (pp. 377–384)
Key ideas are given without proof; proofs for the discrete memoryless counterparts come in later sections (p. 377).

**Basic channel.** $Y_i=X_i+Z_i$, $Z_i$ i.i.d. $\mathcal N(0,N)$ \tag{14.1}, with power constraint
$$\frac1n\sum_{i=1}^n X_i^2\le P \tag{14.2}$$
and capacity
$$C=\tfrac12\log\!\left(1+\tfrac PN\right)\ \text{bits per transmission}. \tag{14.3}$$
Only discrete-time memoryless channels are treated (p. 378).

**14.1.1 Single user.** For $R<\tfrac12\log(1+P/N)$, fix a good $(2^{nR},n)$ codebook of power $P$, send $\mathbf X(i)$, and decode to the closest codeword. For large $n$ the error probability is arbitrarily small. Minimum-distance decoding is essentially equivalent to finding the jointly typical codeword (p. 378).

**14.1.2 Gaussian MAC with $m$ users.** Each user has power $P$:
$$Y=\sum_{i=1}^m X_i+Z \tag{14.4}$$
$$C\!\left(\tfrac PN\right)=\tfrac12\log\!\left(1+\tfrac PN\right) \tag{14.5}$$
The rate region begins $R_i<C(P/N)$ \tag{14.6}. Inequalities (14.7)–(14.9) are unreadable in the text layer [unreadable p. 379]. (14.10) is also blank in the text layer; the remarks on p. 379 give the sum of the rates as $C(mP/N)$ (the digest infers that the last inequality bounds this sum). When all rates are equal, the last inequality dominates the others (p. 379).
- Scheme: $m$ codebooks, the $i$th with $2^{nR_i}$ codewords of power $P$. Each user sends an arbitrary codeword from its own book. The receiver finds the $m$ codewords, one per book, whose vector sum is closest to $Y$ in Euclidean distance. If the rates lie in the region, the error probability tends to 0 as $n\to\infty$ (p. 379).
- Remarks: the sum rate $C(mP/N)$ goes to infinity with $m$. The author's cocktail-party picture is that the listener receives unbounded information as the crowd grows. The optimal scheme does not use time-division multiplexing: every transmitter uses all the bandwidth all the time (p. 379).
- *Intuition note:* The sum rate $C(mP/N)$ is the single-user capacity formula with signal power $mP$ in place of $P$, so it grows with $m$. (See the Toy example: with equal rates, each user's share of the sum bound shrinks as $m$ grows.)

**14.1.3 Gaussian broadcast channel.** Sender power $P$; receivers $Y_1=X+Z_1$, $Y_2=X+Z_2$, with noise variances $N_1<N_2$ (w.l.o.g.) and $Z_1,Z_2$ arbitrarily correlated. Independent messages at rates $R_1,R_2$ (p. 379). All Gaussian broadcast channels are degraded broadcast channels (Section 14.6.2), so the capacity region follows from that result. It is (14.11)–(14.12) [unreadable p. 380], with $\alpha\in[0,1]$ trading $R_1$ against $R_2$ (p. 380).
- Encoding: one codebook of power $\alpha P$ at rate $R_1$, another of power $\bar\alpha P$ at rate $R_2$. The transmitter sends the sum of the chosen codewords (p. 380).
- Decoding: the bad receiver $Y_2$ finds the closest codeword in the second book. The first message acts as noise, so its effective SNR is $\bar\alpha P/(\alpha P+N_2)$ (the author says this "can be proved"; the bar is garbled in the text layer). The good receiver $Y_1$ first decodes $Y_2$'s codeword (possible because $N_1$ is lower), subtracts it, then decodes its own (p. 380).
- Consequence: in optimal encoding for degraded broadcast channels the better receiver knows the weaker receiver's message too (p. 380).

**14.1.4 Gaussian relay channel.** $Y_1=X+Z_1$ \tag{14.13}, $Y=X+Z_1+X_1+Z_2$ \tag{14.14}, with $Z_1,Z_2$ independent, zero mean, variances $N_1,N_2$. The relay's encoding is a causal sequence (14.15) [unreadable p. 380]. Powers are $P$ and $P_1$. The capacity is
$$C=\max_{0\le\alpha\le1}\min\left\{C\!\left(\frac{P+P_1+2\sqrt{\bar\alpha PP_1}}{N_1+N_2}\right),\,C\!\left(\frac{\alpha P}{N_1}\right)\right\},\quad \bar\alpha=1-\alpha. \tag{14.16}$$
If $\dfrac{P_1}{N_2}\ge\dfrac{P}{N_1}$ \tag{14.17}, then $C=C(P/N_1)$, achieved at $\alpha=1$. The channel looks noise-free after the relay. For large $N_2$ and $P_1/N_2\ge P/N_1$ the rate rises from $C(P/(N_1+N_2))\approx 0$ to $C(P/N_1)$ (p. 381).

Scheme (successive blocks; each block resolves the receiver's uncertainty from the previous one), for $R_1<C(\alpha P/N_1)$ (pp. 381–382):
1. Two codebooks: first has $2^{nR_1}$ words of power $\alpha P$; second has $2^{nR_0}$ words of power $\bar\alpha P$.
2. Block 1: send a first-codebook word. The relay learns its index (since $R_1<C(\alpha P/N_1)$). The receiver only has a list of size $2^{n(R_1-C(\alpha P/(N_1+N_2)))}$, from a result on list codes (p. 381).
3. The first codebook is randomly partitioned into $2^{nR_0}$ cells, known to all. In block 2, the sender and relay both send the second-codebook word indexed by the cell of the block-1 word. The relay scales it to power $P_1$. The signals add coherently, so the received power is $(\sqrt{\bar\alpha P}+\sqrt{P_1})^2$ (p. 381).
4. The sender also adds, "on paper", a fresh first-codebook word (p. 381).
5. Receiver in block 2: find the cooperative index (closest second-codebook word), subtract it, and form a list of $2^{nR_0}$ candidate indices for the new first-codebook word. He intersects his block-1 list with the learned cell. By the choice of rates and powers, the intersection is highly probably a single word (pp. 381–382).
6. Steady state: the receiver is one block behind; with many blocks this does not affect the rate (p. 382).
- *Intuition note:* The relay turns the receiver's list of candidates into one answer by sending a short hint (the cell index). Coherent addition of the sender's and relay's signals is what gives the extra power term.

**14.1.5 Gaussian interference channel.** Two senders, each wanting only its own receiver. With symmetric interference:
$$Y_1=X_1+aX_2+Z_1 \tag{14.18}$$
$$Y_2=X_2+aX_1+Z_2 \tag{14.19}$$
$Z_1,Z_2$ independent $\mathcal N(0,N)$ (p. 382). The channel is unsolved in general, even in the Gaussian case. For high interference the capacity region equals that with no interference (p. 383).
- Scheme: two codebooks, each of power $P$ and rate $C(P/N)$. If $C(a^2P/(P+N))>C(P/N)$, the first receiver decodes the second sender's index correctly, subtracts that codeword, and then has a clean channel to its own sender (p. 383).

**14.1.6 Gaussian two-way channel.** Like the interference channel, but sender 1 is attached to receiver 2 and sender 2 to receiver 1 (Fig. 14.6). Senders can use past received symbols, so this introduces feedback (p. 383). The region is not known in general; Shannon [246] gave upper and lower bounds (see Problem 15). For Gaussian channels the bounds coincide. With powers $P_1,P_2$ and noises $N_1,N_2$, rates $R_1<C(P_1/N_1)$, $R_2<C(P_2/N_2)$ are achievable. Each receiver subtracts the codeword of its own sender and has a clean channel from the other. So the Gaussian two-way channel decomposes into two independent channels. This is not true for the general two-way channel, where there is generally a trade-off between the senders (pp. 383–384).

### 14.2 Jointly typical sequences (pp. 384–387)
**Setup.** $(X_1,\dots,X_k)$ are discrete random variables with joint $p(x_1,\dots,x_k)$. $S$ is an ordered subset, and $n$ i.i.d. copies are taken:
$$\Pr\{S=s\}=\prod_{i=1}^n\Pr\{S_i=s_i\}. \tag{14.20}$$
For $S=(X_j,X_l)$: $\Pr\{S=s\}=\prod_{i=1}^n p(x_{ji},x_{li})$ (14.21–14.22). By the law of large numbers, for each subset $S$,
$$-\frac1n\log p(S_1,\dots,S_n)=-\frac1n\sum_{i=1}^n\log p(S_i)\to H(S), \tag{14.23}$$
simultaneously with probability 1 for all $2^k$ subsets (p. 384).

**Definition (typical set).** $A_\epsilon^{(n)}(X_1,\dots,X_k)$ is the set of $(\mathbf x_1,\dots,\mathbf x_k)$ with
$$\left|-\tfrac1n\log p(\mathbf s)-H(S)\right|<\epsilon\quad\forall S\subseteq\{X_1,\dots,X_k\}. \tag{14.24}$$
$A_\epsilon^{(n)}(S)$ is its restriction to the coordinates of $S$. For $S=(X_1,X_2)$ this requires the three conditions (joint, $X_1$, $X_2$) in (14.25) (p. 385).

**Notation.** $a_n\doteq2^{n(b\pm\epsilon)}$ means $\left|\tfrac1n\log a_n-b\right|<\epsilon$ for large $n$ \tag{14.26} (p. 385).

**Theorem 14.2.1.** For any $\epsilon>0$ and large $n$ (p. 385):
1. $P(A_\epsilon^{(n)}(S))\ge1-\epsilon$ for all $S$ \tag{14.27}
2. $\mathbf s\in A_\epsilon^{(n)}(S)\Rightarrow p(\mathbf s)\doteq2^{-n(H(S)\pm\epsilon)}$ \tag{14.28}
3. $|A_\epsilon^{(n)}(S)|\doteq2^{n(H(S)\pm2\epsilon)}$ \tag{14.29}
4. If $(\mathbf s_1,\mathbf s_2)\in A_\epsilon^{(n)}(S_1,S_2)$, then $p(\mathbf s_2|\mathbf s_1)\doteq2^{-n(H(S_2|S_1)\pm2\epsilon)}$ \tag{14.30}

*Proof* (p. 386). Part 1 follows from the law of large numbers; part 2 from the definition. Part 3:
$$1\ge\sum_{\mathbf s\in A_\epsilon^{(n)}(S)}p(\mathbf s)\ge\sum 2^{-n(H(S)+\epsilon)}=|A_\epsilon^{(n)}(S)|\,2^{-n(H(S)+\epsilon)} \tag{14.31–14.33}$$
For large $n$ and with (14.27):
$$1-\epsilon\le\sum_{\mathbf s\in A_\epsilon^{(n)}(S)}p(\mathbf s)\le\sum 2^{-n(H(S)-\epsilon)}=|A_\epsilon^{(n)}(S)|\,2^{-n(H(S)-\epsilon)} \tag{14.34–14.36}$$
Combining (14.33) and (14.36) gives (14.29). Part 4: $p(\mathbf s_1)\doteq2^{-n(H(S_1)\pm\epsilon)}$ and $p(\mathbf s_1,\mathbf s_2)\doteq2^{-n(H(S_1,S_2)\pm\epsilon)}$, so
$$p(\mathbf s_2|\mathbf s_1)=\frac{p(\mathbf s_1,\mathbf s_2)}{p(\mathbf s_1)}\doteq2^{-n(H(S_2|S_1)\pm2\epsilon)} \tag{14.37}$$
- *Intuition note:* With high probability, a long sequence of any group of variables is one of about $2^{nH}$ typical sequences, each with probability close to $2^{-nH}$. This holds for all $2^k$ subsets at once, which is the form the author uses to prove the network theorems (p. 384).

**Theorem 14.2.2.** Let $A_\epsilon^{(n)}(S_1|\mathbf s_2)$ be the set of $\mathbf s_1$ jointly $\epsilon$-typical with a particular $\mathbf s_2$. If $\mathbf s_2\in A_\epsilon^{(n)}(S_2)$, then for large $n$ (p. 386):
$$|A_\epsilon^{(n)}(S_1|\mathbf s_2)|\le2^{n(H(S_1|S_2)+2\epsilon)} \tag{14.38}$$
$$(1-\epsilon)\,2^{n(H(S_1|S_2)-2\epsilon)}\le\sum_{\mathbf s_2}p(\mathbf s_2)\,|A_\epsilon^{(n)}(S_1|\mathbf s_2)| \tag{14.39}$$
*Proof* (p. 387). As in part 3 above, using $p(\mathbf s_1|\mathbf s_2)\ge 2^{-n(H(S_1|S_2)+2\epsilon)}$ on the conditionally typical set:
$$1\ge\sum_{\mathbf s_1\in A_\epsilon^{(n)}(S_1|\mathbf s_2)}p(\mathbf s_1|\mathbf s_2)\ge|A_\epsilon^{(n)}(S_1|\mathbf s_2)|\,2^{-n(H(S_1|S_2)+2\epsilon)} \tag{14.40–14.42}$$
This gives (14.38). For large $n$, using (14.27):
$$1-\epsilon\le\sum_{\mathbf s_2}p(\mathbf s_2)\sum_{\mathbf s_1\in A_\epsilon^{(n)}(S_1|\mathbf s_2)}p(\mathbf s_1|\mathbf s_2)\le\sum_{\mathbf s_2}p(\mathbf s_2)\,|A_\epsilon^{(n)}(S_1|\mathbf s_2)|\,2^{-n(H(S_1|S_2)-2\epsilon)} \tag{14.43–14.45}$$
Rearranging gives (14.39) (the last step is implicit in the source).

**Theorem 14.2.3.** To bound decoding error one needs the probability that conditionally independent sequences are jointly typical. Let $S_1,S_2,S_3$ be subsets of $\{X_1,\dots,X_k\}$, and let $S_1',S_2'$ be conditionally independent given $S_3'$, with the same pairwise marginals as $(S_1,S_2,S_3)$:
$$P(\mathbf S_1'=\mathbf s_1,\mathbf S_2'=\mathbf s_2,\mathbf S_3'=\mathbf s_3)=\prod_{i=1}^np(s_{1i}|s_{3i})\,p(s_{2i}|s_{3i})\,p(s_{3i}) \tag{14.46}$$
Then $P\{(\mathbf S_1',\mathbf S_2',\mathbf S_3')\in A_\epsilon^{(n)}\}\doteq2^{-n(I(S_1;S_2|S_3)\pm6\epsilon)}$ \tag{14.47}; the minus sign is not visible in the printed exponent (see Reading notes) (p. 387).

*Proof, as far as this part goes* (p. 387). Using $\doteq$, sum $p(\mathbf s_3)p(\mathbf s_1|\mathbf s_3)p(\mathbf s_2|\mathbf s_3)$ over typical triples:
$$=\sum_{(\mathbf s_1,\mathbf s_2,\mathbf s_3)\in A_\epsilon^{(n)}}p(\mathbf s_3)p(\mathbf s_1|\mathbf s_3)p(\mathbf s_2|\mathbf s_3) \tag{14.48}$$
$$\doteq|A_\epsilon^{(n)}(S_1,S_2,S_3)|\,2^{-n(H(S_3)\pm\epsilon)}2^{-n(H(S_1|S_3)\pm2\epsilon)}2^{-n(H(S_2|S_3)\pm2\epsilon)} \tag{14.49}$$
The proof continues on the next page, outside this part.
(added step) Inserting $|A_\epsilon^{(n)}|\doteq2^{nH(S_1,S_2,S_3)}$ gives the exponent $H(S_1,S_2,S_3)-H(S_3)-H(S_1|S_3)-H(S_2|S_3)=-I(S_1;S_2|S_3)$, matching (14.47) up to the $\epsilon$ terms.
- *Intuition note:* If two sequences are drawn independently given a shared third one, they are jointly typical only by luck. This probability is of order $2^{-nI(S_1;S_2|S_3)}$ (up to the $\pm6\epsilon$ term in the exponent), i.e. exponentially small in the conditional mutual information.

## Toy example (ours)
Gaussian MAC with $P=3$, $N=1$ and logs in base 2. One user: $C(3)=\tfrac12\log_2(1+3)=\tfrac12\cdot2=1$ bit. With $m=5$: $C(15)=\tfrac12\log_2(16)=2$ bits; with $m=85$: $C(255)=\tfrac12\log_2(256)=4$ bits. The sum rate grows with $m$ (without bound as $m\to\infty$, p. 379). For equal rates, the per-user bound is $<C(P/N)=1$ bit, but the sum bound allows only $R<2/5=0.4$ bit each (for $m=5$) and $R<4/85\approx0.047$ bit each (for $m=85$). So the last (sum-rate) inequality dominates for equal rates, as the author notes.

## Concepts
- [[multiple-access-channel]] (new) — many senders, one receiver; capacity region is a set of simultaneously achievable rates (p. 374)
- [[broadcast-channel]] (new) — one sender, several receivers, with different messages (p. 375)
- [[relay-channel]] (new) — source and destination aided by intermediate nodes that listen and send (p. 375)
- [[interference-channel]] (new) — two senders, two receivers, each receiver wants only its own sender (p. 382)
- [[two-way-channel]] (new) — two terminals each send and receive; feedback is possible (p. 383)
- [[capacity-region]] (new) — set of rate tuples achievable with vanishing error (p. 374)
- [[cut-set-bound]] (new) — information flow across any cut is bounded; generally not achievable (p. 377)
- [[superposition-coding]] (new) — sum of codewords from several codebooks sent at once (p. 380)
- [[channel-capacity]] — here $C=\tfrac12\log(1+P/N)$ for the Gaussian channel (p. 378)
- [[noisy-channel]] — here $p(y^{(1)},\dots,y^{(m)}|x^{(1)},\dots,x^{(m)})$ for the network (p. 375)
- [[typical-set-aep]] — here extended to joint typicality over all subsets of $k$ variables (p. 384)
- [[joint-and-conditional-entropy]] — used for conditional typical sets (p. 386)
- [[mutual-information]] — conditional mutual information sets the joint-typicality probability (p. 387)

## Canonical instances
- [[cocktail-party]] — Gaussian MAC with many speakers and one listener (p. 379)
- [[ford-fulkerson-pipes]] — water-pipe network as a contrast: max flow equals min cut (p. 376)
- [[gaussian-two-way-decomposition]] — the Gaussian two-way channel splits into two independent channels (p. 384)

## Bridges (candidates)
- [structural-analogy] Cut-set bound on information flow ↔ graph theory: max-flow min-cut — the same cut idea, but equality fails for information in general.
- [same-math] Joint AEP set sizes $2^{nH(S)}$ ↔ the joint AEP of Chapter 8 (p. 384) — the same counting argument, now over all subsets.
- [structural-analogy] Gaussian broadcast successive decoding ↔ interference cancellation in the Gaussian interference channel — both decode a codeword, subtract it, then decode the rest.

## Questions this raises
- When does the cut-set bound become achievable beyond the relay and cascade channels?
- Why do Shannon's upper and lower bounds coincide for the Gaussian two-way channel but not in general?
- What exact rate region replaces (14.7)–(14.9), and how is it proved for the discrete memoryless MAC?
- How is the list-code argument for the relay channel made precise?

## Reading notes
- This part starts at the beginning of Chapter 14 (p. 374) and ends in the middle of the proof of Theorem 14.2.3, at (14.49) on p. 387.
- Edition: the copyright line says 1991 John Wiley & Sons, so this is the first edition, not the 2006 second edition cited in the metadata. Printed = pdf − 22.
- No page images were given for printed pp. 374, 377, 379 and 380; there the text layer was used. Equations (14.7)–(14.9), (14.11)–(14.12) and (14.15) are blank in it and are marked unreadable. (14.10) is only described through the remarks on p. 379.
- The broadcast SNR $\bar\alpha P/(\alpha P+N_2)$ is read from a garbled text line ("CUP/(CUP+N2)"); the bar and formula reflect the sentence "$Y_1$'s message acts as noise".
- The relay equations (14.13)–(14.14) were read from the text layer only (no image of p. 380). The text cites "Figure 14.30", which is not on these pages.
- In (14.47) the exponent appears printed without a minus sign. The derivation from (14.49) gives $-nI(S_1;S_2|S_3)$, so I treated the missing sign as a misprint.
- The text layer is heavily garbled in places; equations were checked against the page images where available.
