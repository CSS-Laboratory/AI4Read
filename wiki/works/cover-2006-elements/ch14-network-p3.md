---
id: cover-2006-elements/ch14-network-p3
work: cover-2006-elements
unit: "14 Network Information Theory (part 3/4): end of 14.4, 14.5 Duality, 14.6 Broadcast channel, 14.7 Relay channel, 14.8 Source coding with side information"
pages: 416-437
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Duality, broadcast, relay and side-information coding

## L0 — One line
The network problems treated in this part are handled by combining random coding, binning and typicality: Slepian–Wolf mirrors the multiple access channel, the degraded broadcast channel needs superposition coding with an auxiliary "cloud" variable $U$, and side-information source coding needs a description $U$ of $Y$ with $R_1\ge H(X|U)$, $R_2\ge I(Y;U)$.

## L1 — The gist (≤ 120 words)
This part asks how to code when a network is more than one sender and one receiver. It shows that Slepian–Wolf coding has the same error-bound structure as the multiple access channel. It then finds the capacity region of the degraded broadcast channel by superposition coding with a cloud-center variable $U$. Next it gives the capacity of the physically degraded relay channel, using block Markov coding. Finally it characterises source coding with side information. These results show how one sender can serve receivers of different quality, how a relay helps, and how a partial description of $Y$ can replace full side information about $X$.

**Prerequisites:** mutual information and chain rule; AEP and joint typicality (weak and strong); random coding and error-union bounds; data processing inequality; Fano's inequality; Markov chains; Slepian–Wolf binning (previous part).

## L2 — Key ideas
- Slepian–Wolf's error bound (14.192) has the same three-term shape as the multiple access channel bound (14.190), with rates and entropies swapped (a multiple access channel has two independent senders and one receiver). The author finds this duality surprising, because a broadcast–MAC duality was expected (p. 418).
- A broadcast channel has one sender and several receivers. Its capacity region depends only on the conditional marginals $p(y_1|x)$, $p(y_2|x)$, so stochastically degraded channels reduce to physically degraded ones (pp. 418–422).
- Degraded broadcast capacity (degraded means $X\to Y_1\to Y_2$: $Y_2$ depends on $X$ only through $Y_1$): $R_1\le I(X;Y_1|U)$, $R_2\le I(U;Y_2)$ for some $p(u)p(x|u)$ (Thm 14.6.2). It is achieved by superposition coding: clouds that both receivers see, with satellite codewords that only the better receiver resolves (pp. 422–425).
- Common information costs the better receiver nothing in the degraded case, because it decodes everything meant for the worse receiver (Thm 14.6.4, p. 425).
- Relay channel: the max-flow min-cut upper bound $C\le\sup\min\{I(X,X_1;Y),I(X;Y,Y_1|X_1)\}$ is tight for the physically degraded relay channel (where $Y$ is a random degradation of the relay's observation $Y_1$), via block Markov coding (each block also carries a hint about the previous block's message) with Slepian–Wolf-style partitioning (pp. 429–432).
- Source coding with side information: $X$ can be recovered iff $R_1\ge H(X|U)$ and $R_2\ge I(Y;U)$ for some $U$ with $X\to Y\to U$, $|\mathcal U|\le|\mathcal Y|+2$ (p. 433).
- The converse uses Fano, the chain rule, and a time-sharing variable $Q$ to get a single-letter form (pp. 433–436). Achievability uses binning of $X^n$, a codebook for $U^n$, and a strong-typicality lemma for Markov chains (pp. 436–437).

## L3 — Walkthrough

### End of 14.4 (Slepian–Wolf proof idea) (p. 416)
This part starts mid-section. If the $Y$ encoder knew $X^n$, it could send the index of $Y^n$ inside the jointly typical "fan" of $X^n$ (Fig. 14.21). It does not know $X^n$. So it colours all $Y^n$ sequences at random with $2^{nR_2}$ colours. If the number of colours is high enough, all colours inside one fan are different with high probability. The colour then identifies $Y^n$ within the $X^n$ fan. If $R_2>H(Y|X)$, the colours are exponentially more numerous than the fan's elements, and the error probability is exponentially small (p. 416).

### 14.5 Duality between Slepian–Wolf encoding and multiple access channels
Setting: in the MAC (Fig. 14.22), independent messages $W_1,W_2$ go over a two-input, one-output channel $p(y|x_1,x_2)$. In Slepian–Wolf (Fig. 14.23), correlated sources $(X,Y)$ are encoded as "independent" indices $i,j$ and decoded by a common decoder. The MAC proof uses a random map from messages to sequences; the Slepian–Wolf proof uses a random map from sequences to messages (pp. 416–417).

MAC error bound, with $\epsilon$ the probability that the sequences are not typical:
$$P_e^{(n)}\le\epsilon+\sum_{\text{codewords}}\Pr(\text{codeword jointly typical with received sequence})\tag{14.189}$$
$$=\epsilon+\sum_{2^{nR_1}\text{ terms}}2^{-nI_1}+\sum_{2^{nR_2}\text{ terms}}2^{-nI_2}+\sum_{2^{n(R_1+R_2)}\text{ terms}}2^{-nI_3}\tag{14.190}$$
Here $R_i$ counts the codewords that can cause an error and $I_i$ is the matching mutual information (p. 417).

Slepian–Wolf error bound:
$$P_e^{(n)}\le\epsilon+\sum_{\text{jointly typical sequences}}\Pr(\text{have same codeword})\tag{14.191}$$
$$=\epsilon+\sum_{2^{nH_1}\text{ terms}}2^{-nR_1}+\sum_{2^{nH_2}\text{ terms}}2^{-nR_2}+\sum_{2^{nH_3}\text{ terms}}2^{-n(R_1+R_2)}\tag{14.192}$$
The terms are the ways another jointly typical pair could land in the same bin as the true pair (p. 418). The author calls the duality "now obvious", and surprising, since a duality between broadcast channel and MAC was expected (p. 418).

*Intuition note:* In both proofs the error is a sum over wrong candidates of the chance each looks right. In the MAC the candidates are wrong codewords and the "looks right" chance is $2^{-nI}$. In Slepian–Wolf the candidates are wrong source pairs and the chance is $2^{-nR}$.

### 14.6 The broadcast channel
A broadcast channel has one sender and two or more receivers (Fig. 14.24). The problem is to find the set of simultaneously achievable rates (p. 418).

**Examples (pp. 418–420).**
- *TV station (14.6.1):* sending the same information to everyone gives capacity essentially $\max_{p(x)}\min_i I(X;Y_i)$. One may instead want better receivers to get extra information (HDTV) while bad receivers still get the basic signal (pp. 418–419).
- *Lecturer (14.6.2):* a lecture tailored so that good students get more and poor students get at least a minimum is a broadcast channel. The text adds that a poorly prepared lecture proceeds at the pace of the weakest student (p. 419).
- *Orthogonal channels (14.6.3):* with two independent channels of capacities $C_1,C_2$, rate pairs with $R_1<C_1$, $R_2<C_2$ are achievable. The region is a rectangle (Fig. 14.25) (p. 419).
- *Spanish and Dutch speaker (14.6.4):* each language has $2^{20}$ words and the speaker says one word per second. Speaking only one language gives 20 bits/s to one listener. Time-sharing gives any pair with $R_1+R_2=20$. But each listener can tell when a word is in the other language. With 50% of each in 100 words, there are about $\binom{100}{50}=2^{100H(1/2)}$ orderings, and the ordering carries information to both. This yields 10 bits/s to the Dutch receiver, 10 to the Spanish receiver and 1 bit/s common to both, so 21 bits/s in total, more than time-sharing. This is superposition of information (p. 420).

The results also apply to a single-user channel with unknown distribution: get a minimum through when the channel is bad, and extra when it is good (p. 420).

#### 14.6.1 Definitions
A broadcast channel has input alphabet $\mathcal X$, output alphabets $\mathcal Y_1,\mathcal Y_2$ and transition function $p(y_1,y_2|x)$. It is memoryless if $p(y_1^n,y_2^n|x^n)=\prod_{i=1}^n p(y_{1i},y_{2i}|x_i)$ (p. 420).

A $((2^{nR_1},2^{nR_2}),n)$ code for independent information has an encoder and two decoders:
$$X:\{1,\dots,2^{nR_1}\}\times\{1,\dots,2^{nR_2}\}\to\mathcal X^n\tag{14.193}$$
$$g_1:\mathcal Y_1^n\to\{1,\dots,2^{nR_1}\}\tag{14.194}$$
$$g_2:\mathcal Y_2^n\to\{1,\dots,2^{nR_2}\}\tag{14.195}$$
$$P_e^{(n)}=P(g_1(Y_1^n)\ne W_1\text{ or }g_2(Y_2^n)\ne W_2),\tag{14.196}$$
with $(W_1,W_2)$ uniform. A pair $(R_1,R_2)$ is achievable if some sequence of such codes has $P_e^{(n)}\to0$ (pp. 420–421).

With common information $W_0$, a $((2^{nR_0},2^{nR_1},2^{nR_2}),n)$ code has
$$X:\{1,\dots,2^{nR_0}\}\times\{1,\dots,2^{nR_1}\}\times\{1,\dots,2^{nR_2}\}\to\mathcal X^n\tag{14.197}$$
$$g_1:\mathcal Y_1^n\to\{1,\dots,2^{nR_0}\}\times\{1,\dots,2^{nR_1}\}\tag{14.198}$$
$$g_2:\mathcal Y_2^n\to\{1,\dots,2^{nR_0}\}\times\{1,\dots,2^{nR_2}\}\tag{14.199}$$
$$P_e^{(n)}=P(g_1(Y_1^n)\ne(W_0,W_1)\text{ or }g_2(Z^n)\ne(W_0,W_2)).\tag{14.200}$$
(14.200) is printed with $g_2(Z^n)$; $Y_2^n$ is meant. A triple $(R_0,R_1,R_2)$ is achievable if some code sequence has $P_e^{(n)}\to0$. The capacity region is the closure of the achievable rates (p. 421).

**Theorem 14.6.1.** The capacity region depends only on the conditional marginals $p(y_1|x)$ and $p(y_2|x)$. (Proof left to the exercises.) (p. 422)

#### 14.6.2 Degraded broadcast channels
*Physically degraded:* $p(y_1,y_2|x)=p(y_1|x)p(y_2|y_1)$. *Stochastically degraded:* the conditional marginals equal those of a physically degraded channel, i.e. there is $p'(y_2|y_1)$ with
$$p(y_2|x)=\sum_{y_1}p(y_1|x)p'(y_2|y_1).\tag{14.201}$$
Since capacity depends only on the marginals, both have the same capacity region, so the text assumes physical degradedness (p. 422).

#### 14.6.3 Capacity region for the degraded broadcast channel
**Theorem 14.6.2.** For independent information over the degraded channel $X\to Y_1\to Y_2$, the capacity region is the convex hull of the closure of all $(R_1,R_2)$ with
$$R_1\le I(X;Y_1|U),\qquad R_2\le I(U;Y_2)\tag{14.202–14.203}$$
for some $p(u)p(x|u)p(y_1,y_2|x)$, with $|\mathcal U|\le\min\{|\mathcal X|,|\mathcal Y_1|,|\mathcal Y_2|\}$. The cardinality bound comes from convex-set theory and is not proved here (p. 422). The text layer of this page is garbled; the rate constraints are read from the proof (pp. 423–425) and the cardinality bound from the garbled text.

*Achievability idea:* $U$ is a cloud center both receivers can distinguish. Each cloud holds $2^{nR_1}$ codewords $X^n$ that $Y_1$ can distinguish. The worse receiver sees only clouds; the better one also sees the codewords inside (pp. 422–423).

*Random codebook.* Fix $p(u),p(x|u)$.
- Generate $2^{nR_2}$ codewords $\mathbf U(w_2)$ i.i.d. from $\prod p(u_i)$.
- For each, generate $2^{nR_1}$ codewords $\mathbf X(w_1,w_2)$ from $\prod p(x_i|u_i(w_2))$.
- $\mathbf u(i)$ is the cloud center and $\mathbf x(i,j)$ is the $j$th satellite in cloud $i$. To send $(W_1,W_2)$, send $\mathbf X(W_1,W_2)$ (p. 423).

*Decoding.*
- Receiver 2 looks for the unique $\hat W_2$ with $(\mathbf U(\hat W_2),\mathbf Y_2)\in A_\epsilon^{(n)}$.
- Receiver 1 looks for the unique $(\hat W_1,\hat W_2)$ with $(\mathbf U(\hat W_2),\mathbf X(\hat W_1,\hat W_2),\mathbf Y_1)\in A_\epsilon^{(n)}$.
- Failure to find a unique pair counts as an error (p. 423).

*Error analysis.* By symmetry assume $(1,1)$ was sent. With $E_{Yi}=\{(\mathbf U(i),\mathbf Y_2)\in A_\epsilon^{(n)}\}$ (14.204), receiver 2 has
$$P_e^{(n)}(2)=P\Big(E_{Y1}^c\cup\bigcup_{i\ne1}E_{Yi}\Big)\le P(E_{Y1}^c)+\sum_{i\ne1}P(E_{Yi})\le\epsilon+2^{nR_2}2^{-n(I(U;Y_2)-2\epsilon)}\le2\epsilon\tag{14.205–14.208}$$
for large $n$ if $R_2<I(U;Y_2)$; (14.207) follows from the AEP (pp. 423–424).

For receiver 1 define $\tilde E_{Yi}=\{(\mathbf U(i),\mathbf Y_1)\in A_\epsilon^{(n)}\}$ and $\tilde E_{Yij}=\{(\mathbf U(i),\mathbf X(i,j),\mathbf Y_1)\in A_\epsilon^{(n)}\}$ (14.209–14.210). Then
$$P_e^{(n)}(1)\le P(\tilde E_{Y1}^c)+\sum_{i\ne1}P(\tilde E_{Yi})+\sum_{j\ne1}P(\tilde E_{Y1j}).\tag{14.211–14.212}$$
- Wrong-cloud terms: $P(\tilde E_{Yi})\le2^{-n(I(U;Y_1)-3\epsilon)}$. These vanish if $R_2<I(U;Y_1)$. By the data processing inequality and degradedness, $I(U;Y_1)\ge I(U;Y_2)$, so the theorem's condition suffices.
- Wrong-satellite terms:
$$P(\tilde E_{Y1j})=\sum_{(\mathbf u,\mathbf x,\mathbf y_1)\in A_\epsilon^{(n)}}P(\mathbf U(1))P(\mathbf X(1,j)|\mathbf U(1))P(\mathbf Y_1|\mathbf U(1))\tag{14.213–14.215}$$
$$\le\sum 2^{-n(H(U)-\epsilon)}2^{-n(H(X|U)-\epsilon)}2^{-n(H(Y_1|U)-\epsilon)}\le2^{n(H(U,X,Y_1)+\epsilon)}2^{-n(H(U)-\epsilon)}2^{-n(H(X|U)-\epsilon)}2^{-n(H(Y_1|U)-\epsilon)}=2^{-n(I(X;Y_1|U)-4\epsilon)}\tag{14.216–14.218}$$
(added step: the last equality uses $H(U,X,Y_1)=H(U)+H(X|U)+H(Y_1|U,X)$ and $H(Y_1|X,U)=H(Y_1|X)$ in the Markov structure, so the exponent sums to $-I(X;Y_1|U)$.)

Hence
$$P_e^{(n)}(1)\le\epsilon+2^{nR_2}2^{-n(I(U;Y_1)-3\epsilon)}+2^{nR_1}2^{-n(I(X;Y_1|U)-4\epsilon)}\le3\epsilon\tag{14.219–14.220}$$
for large $n$ if $R_2<I(U;Y_1)$ and $R_1<I(X;Y_1|U)$. So good codes exist (pp. 424–425). The converse is outlined in the exercises (p. 425).

*Intuition note:* The coarse message $W_2$ goes in the cloud, which a poor receiver can read. The fine message $W_1$ is the position inside the cloud, visible only through the better channel. Because $Y_1$ is better, it can also read the cloud, so nothing is lost for it.

**Common information.** *Theorem 14.6.3:* if $(R_1,R_2)$ is achievable for independent information, then $(R_0,R_1-R_0,R_2-R_0)$ is achievable, provided $R_0\le\min(R_1,R_2)$. *Theorem 14.6.4:* in the degraded case, if $(R_1,R_2)$ is achievable then $(R_0,R_1,R_2-R_0)$ is achievable, provided $R_0<R_2$ (the printed inequality is faint). The better receiver always decodes all the information sent to the worse one, so its rate need not be reduced (p. 425).

**Example 14.6.5 (binary symmetric broadcast channel)** (the text layer labels it 14.6.6). Take BSCs with parameters $p_1<p_2<\tfrac12$ (Fig. 14.26). Recast it as a degraded channel: BSC($p_2$) is BSC($p_1$) cascaded with a BSC of crossover $\alpha$, where
$$p_1(1-\alpha)+(1-p_1)\alpha=p_2\tag{14.221}$$
$$\alpha=\frac{p_2-p_1}{1-2p_1}.\tag{14.222}$$
(added step: (14.222) follows from (14.221) because the left side equals $p_1+\alpha(1-2p_1)$.) $U$ is binary. By symmetry, connect $U$ to $X$ by a BSC($\beta$) (Fig. 14.27), and take $U$ uniform on $\{0,1\}$. Then
$$I(U;Y_2)=H(Y_2)-H(Y_2|U)=1-H(\beta*p_2),\quad\beta*p_2=\beta(1-p_2)+(1-\beta)p_2\tag{14.223–14.225}$$
$$I(X;Y_1|U)=H(Y_1|U)-H(Y_1|X,U)=H(Y_1|U)-H(Y_1|X)=H(\beta*p_1)-H(p_1),\quad\beta*p_1=\beta(1-p_1)+(1-\beta)p_1\tag{14.226–14.229}$$
Plotting over $\beta$ gives the region of Fig. 14.28. At $\beta=0$: $R_2=1-H(p_2)$, $R_1=0$. At $\beta=\tfrac12$: $R_1=1-H(p_1)$, $R_2=0$. These are the corner points (pp. 425–427).

**Example 14.6.6 (Gaussian broadcast channel).** Written in degraded form (Fig. 14.29):
$$Y_1=X+Z_1,\qquad Y_2=X+Z_2=Y_1+Z_2',\tag{14.230–14.231}$$
with $Z_1\sim\mathcal N(0,N_1)$, $Z_2'\sim\mathcal N(0,N_2-N_1)$. Extending the results, the capacity region is
$$R_1<C\Big(\frac{\alpha P}{N_1}\Big),\qquad R_2<C\Big(\frac{(1-\alpha)P}{\alpha P+N_2}\Big),\tag{14.232–14.233}$$
with $0\le\alpha\le1$ chosen arbitrarily. The scheme is outlined in Section 14.1.3 (not in this part). All Gaussian broadcast channels are said to be equivalent to this degraded type, to be shown later (pp. 427–428).

### 14.7 The relay channel
One sender, one receiver, and intermediate relay nodes; the simplest case has one relay. The channel is $(\mathcal X,\mathcal X_1,\mathcal Y,\mathcal Y_1)$ with pmfs $p(\cdot,\cdot|x,x_1)$ on $\mathcal Y\times\mathcal Y_1$. Here $x$ is the sender's input, $y$ the output, $y_1$ the relay's observation and $x_1$ the relay's input (Fig. 14.30). It combines a broadcast channel ($X\to Y,Y_1$) and a MAC ($X,X_1\to Y$). The capacity is known for the physically degraded case (p. 428).

**Definition.** A $(2^{nR},n)$ code consists of
$$X:\{1,\dots,2^{nR}\}\to\mathcal X^n\tag{14.234}$$
$$x_{1i}=f_i(Y_{11},Y_{12},\dots,Y_{1,i-1}),\quad1\le i\le n\tag{14.235}$$
$$g:\mathcal Y^n\to\{1,\dots,2^{nR}\}.\tag{14.236}$$
The relay input depends only on past observations (non-anticipatory). The channel is memoryless: $(Y_i,Y_{1i})$ depends on the past only through $(X_i,X_{1i})$. The joint pmf is
$$p(w,\mathbf x,\mathbf x_1,\mathbf y,\mathbf y_1)=p(w)\prod_{i=1}^np(x_i|w)p(x_{1i}|y_{11},\dots,y_{1,i-1})p(y_i,y_{1i}|x_i,x_{1i}).\tag{14.237}$$
Error: $\lambda(w)=\Pr\{g(\mathbf Y)\ne w\mid w\text{ sent}\}$ (14.238), and $P_e^{(n)}=2^{-nR}\sum_w\lambda(w)$ (14.239). $R$ is achievable if some code sequence has $P_e^{(n)}\to0$. The capacity $C$ is the supremum of achievable rates (p. 429).

**Theorem 14.7.1 (upper bound).** For any relay channel,
$$C\le\sup_{p(x,x_1)}\min\{I(X,X_1;Y),\;I(X;Y,Y_1|X_1)\}.\tag{14.240}$$
This follows from a more general max flow min cut theorem (Section 14.10, not in this part). The first term bounds the transfer from $X,X_1$ to $Y$; the second bounds the transfer from $X$ to $Y,Y_1$ (pp. 429–430).

**Physically degraded relay channel:** $p(y,y_1|x,x_1)=p(y_1|x,x_1)p(y|y_1,x_1)$ (14.241). So $Y$ is a random degradation of $Y_1$.

**Theorem 14.7.2.** For this channel,
$$C=\sup_{p(x,x_1)}\min\{I(X,X_1;Y),\;I(X;Y_1|X_1)\}.\tag{14.242}$$
*Converse:* from 14.7.1, since degradedness gives $I(X;Y,Y_1|X_1)=I(X;Y_1|X_1)$ (p. 430).

*Achievability (outline only).* It combines random coding, list codes, Slepian–Wolf partitioning, coding for the cooperative MAC, superposition coding and block Markov encoding (p. 430).
- Use $B$ blocks of $n$ symbols and send $B-1$ indices $w_i\in\{1,\dots,2^{nR}\}$. The rate $R(B-1)/B$ is close to $R$ for large $B$ (p. 430).
- Codewords: $\{\mathbf x(w|s),\mathbf x_1(s)\}$ with $w\in\{1,\dots,2^{nR}\}$, $s\in\{1,\dots,2^{nR_0}\}$ (14.243). Partition $\mathcal S=\{S_1,\dots,S_{2^{nR_0}}\}$ of $\mathcal W=\{1,\dots,2^{nR}\}$ into disjoint cells covering $\mathcal W$ (14.244); the cell index acts as Slepian–Wolf side information (p. 431).
- Random code: fix $p(x_1)p(x|x_1)$. Draw $2^{nR_0}$ i.i.d. $\mathbf x_1(s)\sim\prod p(x_{1i})$. For each, draw $2^{nR}$ conditionally independent $\mathbf x(w|s)\sim\prod p(x_i|x_{1i}(s))$. Each $w$ goes to a cell chosen uniformly at random (p. 431).
- Encoding in block $i$: let $s_i$ be the cell containing $w_{i-1}$. The sender sends $\mathbf x(w_i|s_i)$. The relay has an estimate $\hat w_{i-1}$, finds the cell $\hat s_i$ containing it, and sends $\mathbf x_1(\hat s_i)$ (p. 431).
- Decoding at the end of block $i$, assuming the receiver knows $w_1..w_{i-2}$ and $s_1..s_{i-1}$, and the relay knows $w_1..w_{i-1}$ and so $s_1..s_i$:
 1. The relay finds the unique $w$ with $(\mathbf x(w|s_i),\mathbf x_1(s_i),\mathbf y_1(i))$ jointly $\epsilon$-typical. Success is reliable if $R<I(X;Y_1|X_1)$ (14.245).
 2. The receiver finds the unique $s$ with $(\mathbf x_1(s),\mathbf y(i))$ jointly typical. This works if $R_0<I(X_1;Y)$ (14.246).
 3. Given $s_i$ correct, the receiver forms a list $\mathcal L(\mathbf y(i-1))$ of indices jointly typical with $\mathbf y(i-1)$. It picks the unique $w\in S_{s_i}\cap\mathcal L(\mathbf y(i-1))$. This works if $R<I(X;Y|X_1)+R_0$ (14.247).
- Combining (14.246) and (14.247), $R_0$ drops out:
$$R<I(X;Y|X_1)+I(X_1;Y)=I(X,X_1;Y).\tag{14.248}$$
(added step: the equality is the chain rule for mutual information.) Details are in Cover and El Gamal [67] (pp. 431–432).

Theorem 14.7.2 is also said to give the capacity for: (i) reversely degraded relay channels, $p(y,y_1|x,x_1)=p(y|x,x_1)p(y_1|y,x_1)$ (14.249); (ii) relay channels with feedback; (iii) deterministic relay channels, $y_1=f(x,x_1)$, $y=g(x,x_1)$ (14.250) (p. 432).

*Intuition note:* The relay decodes the message block by block and tells the receiver, in the next block, which cell the old message lies in. The receiver combines this hint with its own noisy view of the old block. The rate is limited by the weaker of two cuts: sender+relay to receiver, and sender to relay-and-receiver.

### 14.8 Source coding with side information
Two variables $X,Y$ are encoded separately, but only $X$ is to be recovered. $R_1$ is the rate for $X$ and $R_2$ the rate for $Y$ (Fig. 14.31). Extremes: if $R_2>H(Y)$, $Y$ is known perfectly and $R_1=H(X|Y)$ suffices (Slepian–Wolf). If $R_2=0$, $R_1=H(X)$ is necessary. In general, $R_2=I(Y;\hat Y)$ bits describe an approximate $\hat Y$ and $X$ needs $H(X|\hat Y)$ bits (p. 433).

**Theorem 14.8.1.** Let $(X,Y)\sim p(x,y)$. $X$ can be recovered with arbitrarily small error probability **if and only if**
$$R_1\ge H(X|U),\qquad R_2\ge I(Y;U)\tag{14.251–14.252}$$
for some $p(x,y)p(u|y)$ with $|\mathcal U|\le|\mathcal Y|+2$ (p. 433). No proof of the cardinality bound appears in this part.

**Converse.** Take mappings $f_n(X^n)$, $g_n(Y^n)$ with rates below $R_1,R_2$, and $h_n$ with
$$P_e^{(n)}=\Pr\{h_n(f_n(X^n),g_n(Y^n))\ne X^n\}<\epsilon.\tag{14.253}$$
Let $S=f_n(X^n)$, $T=g_n(Y^n)$. Fano's inequality gives $H(X^n|S,T)\le n\epsilon_n$ (14.254) (p. 433).

For $R_2$:
$$nR_2\overset{(a)}\ge H(T)\overset{(b)}\ge I(Y^n;T)=\sum_{i=1}^nI(Y_i;T|Y_1,\dots,Y_{i-1})\overset{(c)}=\sum_{i=1}^nI(Y_i;T,Y_1,\dots,Y_{i-1})\overset{(d)}=\sum_{i=1}^nI(Y_i;U_i)\tag{14.255–14.259}$$
(a) range of $g_n$ has $2^{nR_2}$ values; (b) properties of mutual information; (c) chain rule, and $Y_i$ independent of $Y_1..Y_{i-1}$ so $I(Y_i;Y_1,\dots,Y_{i-1})=0$; (d) define $U_i=(T,Y_1,\dots,Y_{i-1})$ (p. 434).

For $R_1$:
$$\begin{aligned}nR_1&\overset{(a)}\ge H(S)\overset{(b)}\ge H(S|T)=H(S|T)+H(X^n|S,T)-H(X^n|S,T)\overset{(c)}\ge H(X^n,S|T)-n\epsilon_n\overset{(d)}=H(X^n|T)-n\epsilon_n\\&\overset{(e)}=\sum_iH(X_i|T,X_1,\dots,X_{i-1})-n\epsilon_n\overset{(f)}\ge\sum_iH(X_i|T,X^{i-1},Y^{i-1})-n\epsilon_n\overset{(g)}=\sum_iH(X_i|T,Y^{i-1})-n\epsilon_n\overset{(h)}=\sum_iH(X_i|U_i)-n\epsilon_n\end{aligned}\tag{14.260–14.268}$$
(a) range of $S$; (b) conditioning reduces entropy; (c) Fano; (d) chain rule, $S$ is a function of $X^n$; (e) chain rule; (f) conditioning reduces entropy; (g) the "subtle" fact that $X_i\to(T,Y^{i-1})\to X^{i-1}$ is a Markov chain; (h) definition of $U$ (pp. 434–435). Also $X_i\to Y_i\to U_i$ is a Markov chain. Hence (the printed (14.269) omits the $\epsilon_n$ term)
$$R_1\ge\frac1n\sum_iH(X_i|U_i),\qquad R_2\ge\frac1n\sum_iI(Y_i;U_i).\tag{14.269–14.270}$$
Introduce a time-sharing variable $Q$ ($Q=i$ with probability $1/n$):
$$R_1\ge H(X_Q|U_Q,Q),\qquad R_2\ge I(Y_Q;U_Q|Q).\tag{14.271–14.272}$$
Since $Q$ is independent of $Y_Q$,
$$I(Y_Q;U_Q|Q)=I(Y_Q;U_Q,Q)-I(Y_Q;Q)=I(Y_Q;U_Q,Q).\tag{14.273}$$
$X_Q,Y_Q$ have joint distribution $p(x,y)$. With $U=(U_Q,Q)$, $X=X_Q$, $Y=Y_Q$: $R_1\ge H(X|U)$ (14.274) and $R_2\ge I(Y;U)$ (14.275). This proves the converse (pp. 435–436).

*Skip path:* carry forward only the single-letter result (14.274–14.275) with $X\to Y\to U$.

*Intuition note:* The $Y$ encoder's message $T$ costs at least $I(Y;U)$ bits. $X$ then needs at least its leftover uncertainty $H(X|U)$ given what $T$ reveals. Time-sharing turns the per-symbol sums into a single "typical" symbol.

**Lemma 14.8.1 (strong typicality and Markov chains).** A triple $(x^n,y^n,z^n)$ is $\epsilon$-strongly typical if
$$\Big|\frac1nN(a,b,c|x^n,y^n,z^n)-p(a,b,c)\Big|<\frac{\epsilon}{|\mathcal X||\mathcal Y||\mathcal Z|}.\tag{14.276}$$
This implies that $(x^n,y^n)$ and $(y^n,z^n)$ are jointly strongly typical. The converse is not true in general. But if $X\to Y\to Z$ is a Markov chain, $p(x,y,z)=p(x,y)p(z|y)$, then for given $(y^n,z^n)\in A_\epsilon^{*(n)}(Y,Z)$ and $X^n\sim\prod p(x_i|y_i)$, we get $\Pr\{(X^n,y^n,z^n)\in A_\epsilon^{*(n)}(X,Y,Z)\}>1-\epsilon$ for large $n$. It is stated without proof [28, 83]. Remark: if instead $X^n\sim\prod p(x_i|y_i,z_i)$ this holds by the strong law of large numbers. Markovity shows that drawing from $p(x_i|y_i)$ is enough (p. 436).

**Achievability.** Fix $p(u|y)$; $p(u)=\sum_yp(y)p(u|y)$.
- *Codebooks:* $2^{nR_2}$ codewords $\mathbf U(w_2)\sim\prod p(u_i)$. Each $X^n$ gets an independent uniform bin index in $\{1,\dots,2^{nR_1}\}$; $B(i)$ is bin $i$ (p. 436).
- *Encoding:* the $X$ sender sends its bin index $i$. The $Y$ sender sends the least $s$ with $(Y^n,U^n(s))\in A_\epsilon^{*(n)}(Y,U)$, or $s=1$ if none exists (p. 437).
- *Decoding:* find the unique $X^n\in B(i)$ with $(X^n,U^n(s))\in A_\epsilon^{*(n)}(X,U)$. Otherwise declare an error (p. 437).
- *Error sources* (p. 437):
 1. $(X^n,Y^n)$ not typical: small for large $n$. Then condition on a typical pair.
 2. No $U^n(s)$ jointly typical with $Y^n$: small if $R_2>I(Y;U)$ (14.277), by the Section 13.6 argument.
 3. $U^n(s)$ typical with $y^n$ but not with $x^n$: small by Lemma 14.8.1, since $X\to Y\to U$.
 4. Another typical $X^n\in B(i)$ jointly typical with $U^n(s)$. Any other $X^n$ is jointly typical with probability less than $2^{-n(I(U;X)-3\epsilon)}$, so
$$|B(i)\cap A_\epsilon^{*(n)}(X)|\,2^{-n(I(X;U)-3\epsilon)}\le2^{n(H(X)+\epsilon)}2^{-nR_1}2^{-n(I(X;U)-3\epsilon)},\tag{14.278}$$
 which goes to 0 if $R_1>H(X|U)$ (added step: $H(X)-I(X;U)=H(X|U)$).

Hence the error probability can be made arbitrarily small, completing the proof (p. 437).

## Toy example (ours, not from the text)
Superposition on a degraded broadcast channel. Let $X=(a,b)$ be two fair-bit-capable inputs ($|\mathcal X|=4$). Receiver 1 sees $Y_1=(a,b)$ exactly. Receiver 2 sees $Y_2=a$ only. This is physically degraded: $X\to Y_1\to Y_2$, with $Y_2$ a function of $Y_1$.

- Choose $U=a$, uniform, and $X=(U,V)$ with $V$ an independent uniform bit, so $p(x|u)$ fixes $a=u$.
- $I(U;Y_2)=H(Y_2)-H(Y_2|U)=1-0=1$ bit.
- $I(X;Y_1|U)=H(Y_1|U)-H(Y_1|X,U)=H(V)-0=1-0=1$ bit. By Thm 14.6.2, $(R_1,R_2)=(1,1)$ is achievable.
- Corners: $U$ constant gives $I(U;Y_2)=0$ and $I(X;Y_1|U)=H(X)-0=2$, so $(2,0)$. $U=X$ gives $I(U;Y_2)=I(X;Y_2)=1$ and $I(X;Y_1|U)=0$, so $(0,1)$.
- Time-sharing between $(2,0)$ and $(0,1)$ gives $(2\lambda,1-\lambda)$. Reaching $R_2=1$ forces $\lambda=0$ and $R_1=0$. At $R_1=1$ it gives only $R_2=\tfrac12$. So $(1,1)$ beats time-sharing, as in the Spanish/Dutch example.
- Common information (Thm 14.6.4): if $(1,1)$ is achievable, then $(R_0,R_1,R_2-R_0)=(\tfrac12,1,\tfrac12)$ is achievable. Receiver 1 loses nothing.

## Concepts
- [[broadcast-channel]] (new) — one sender, several receivers, channel $p(y_1,y_2|x)$; question is the set of simultaneously achievable rates (p. 418)
- [[degraded-broadcast-channel]] (new) — $p(y_1,y_2|x)=p(y_1|x)p(y_2|y_1)$ (physically), or same marginals as such a channel (stochastically) (p. 422)
- [[superposition-coding]] (new) — a cloud-center codeword $U^n$ plus satellite codewords $X^n$; the worse receiver reads clouds, the better one also reads satellites (pp. 420, 422–423)
- [[multiple-access-channel]] (new) — independent messages over a channel with two inputs and one output (p. 416)
- [[slepian-wolf-coding]] (new) — separate encoding of correlated sources with joint decoding, by random binning ("colouring") (pp. 416–418)
- [[relay-channel]] (new) — sender, receiver and a relay that observes $Y_1$ and chooses $X_1$ causally (p. 428)
- [[block-markov-encoding]] (new) — each block sends a new index plus a cell index for the previous block's index (pp. 430–431)
- [[source-coding-with-side-information]] (new) — recover $X$ with $Y$ described at rate $R_2\ge I(Y;U)$; $R_1\ge H(X|U)$ (p. 433)
- [[strong-typicality]] (new) — typicality by symbol-count closeness; Markov-chain lemma 14.8.1 (p. 436)
- [[typical-set-aep]] — jointly typical sequences used for every error bound here (p. 417)
- [[mutual-information]] — rate constraints $I(U;Y_2)$, $I(X;Y_1|U)$, etc. (p. 422)
- [[data-processing-inequality]] — gives $I(U;Y_1)\ge I(U;Y_2)$ for degraded channels (p. 424)
- [[fanos-inequality]] — gives $H(X^n|S,T)\le n\epsilon_n$ in the converse (p. 433)

## Canonical instances
- [[spanish-dutch-speaker]] — superposition beats time-sharing: 21 vs 20 bits/s (p. 420)
- [[hdtv-layered-broadcast]] — regular TV for bad receivers, extra for good ones (p. 419)
- [[binary-symmetric-broadcast-channel]] — region from $1-H(\beta*p_2)$ and $H(\beta*p_1)-H(p_1)$ (pp. 425–427)
- [[gaussian-broadcast-channel]] — region $C(\alpha P/N_1)$, $C((1-\alpha)P/(\alpha P+N_2))$ (pp. 427–428)
- [[orthogonal-broadcast-channels]] — rectangular capacity region (p. 419)

## Bridges (candidates)
- [structural-analogy] Relay upper bound (14.240) ↔ graph theory: max-flow min-cut — the author gives the bound a max flow min cut interpretation (p. 430).
- [structural-analogy] Slepian–Wolf binning error sum (14.192) ↔ MAC error sum (14.190) — same three-term structure with rates and entropies exchanged.
- [structural-analogy] Side-information coding with $U$ ($R_2\ge I(Y;U)$, $R_1\ge H(X|U)$) ↔ information bottleneck: compress $Y$ into $U$ while keeping information relevant to $X$.
- [metaphor] Superposition clouds and satellites ↔ layered media coding such as HDTV on top of regular TV (p. 419).

## Questions this raises
- Why does the cardinality bound on $U$ hold in Theorems 14.6.2 and 14.8.1, and can it be tightened?
- Is the superposition region still the capacity region when the broadcast channel is not degraded? (The text proves it only for the degraded case; the Gaussian case is claimed equivalent to a degraded one.)
- How does the max flow min cut theorem of Section 14.10 yield the relay upper bound (14.240)?
- What happens to the side-information region if $Y$ must also be recovered (the Slepian–Wolf case)?

## Reading notes
- **Unit span:** this part starts in the section before 14.5 (taken to be 14.4; its heading is not on these pages), at the "fans/colouring" paragraph on printed p. 416. It ends on printed p. 437, at the end of the achievability proof of Theorem 14.8.1 (section 14.8). It does not cover 14.9 onwards.
- **Page offset:** printed = pdf − 22.
- **Edition:** the task notes say this PDF is the 1991 first edition, not the 2006 2nd edition named in the work citation; nothing on these pages shows the edition.
- **Text-only pages:** pdf 442 (p. 420), 444 (p. 422), 447 (p. 425) and 459 (p. 437) had no page image. Statements on those pages rely on the text layer, which is partly garbled.
- **Garbled equations:** (14.202)–(14.203) are reconstructed from the proof on pp. 423–425; the cardinality bound in Theorem 14.6.2 is read from the garbled text layer (the proof does not derive it). The inequality in Theorem 14.6.4 ("R, CR,") is read as $R_0<R_2$.
- **Misprints:** (14.200) has $g_2(Z^n)$ where $Y_2^n$ is meant. The BSC example is labelled "14.6.6" in the text layer; this is probably 14.6.5, since the Gaussian example is also 14.6.6. (14.269) omits the $\epsilon_n$ term of (14.268).
- **Undefined notation:** $C(\cdot)$ in (14.232)–(14.233) is not defined on these pages. Theorems 14.2.1 and 14.2.3 and Sections 13.6, 14.1.3 and 14.10 are cited but not in this part.
- **Converses:** the proof of Theorem 14.6.1 and the converse of Theorem 14.6.2 are left to exercises, which are not in this unit.
