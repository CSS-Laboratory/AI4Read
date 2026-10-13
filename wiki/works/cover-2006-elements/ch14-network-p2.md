---
id: cover-2006-elements/ch14-network-p2
work: cover-2006-elements
unit: "14 Network Information Theory (part 2/4): §14.3 The multiple access channel; §14.4 Encoding of correlated sources (up to §14.4.3)"
pages: 388-415
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
# The multiple access channel and Slepian–Wolf coding

## L0 — One line
Two independent senders sharing one receiver can reach every rate pair inside a region bounded by conditional mutual informations, and two separately encoded correlated sources need a total rate of only H(X,Y), the same as joint encoding.

## L1 — The gist (≤ 120 words)
How fast can several senders talk to one receiver at once? And how can two separated, correlated sources be compressed? For the multiple access channel, the capacity region is the closure of the convex hull of pairs with R₁ < I(X₁;Y|X₂), R₂ < I(X₂;Y|X₁) and R₁+R₂ < I(X₁,X₂;Y). The input distribution is a product, and time sharing mixes points. In the Gaussian case, the sum rate can equal that of one transmitter with the summed power. For separately encoded correlated sources, Slepian–Wolf shows the region is R₁ ≥ H(X|Y), R₂ ≥ H(Y|X), R₁+R₂ ≥ H(X,Y). Proofs use random codes, joint typicality, random binning and Fano's inequality.

**Prerequisites:** mutual information and chain rule; typical sets/AEP and union bound; Fano's inequality; data processing inequality; Gaussian channel capacity and differential entropy; random coding proof of the channel coding theorem.

## L2 — Key ideas
- A multiple access channel (MAC) has several senders and one receiver. Its capacity is a region of rate pairs, not one number (p. 388–389).
- Region for a fixed product input $p_1p_2$: $R_1<I(X_1;Y|X_2)$, $R_2<I(X_2;Y|X_1)$, $R_1+R_2<I(X_1,X_2;Y)$. The full region is the closure of the convex hull (all mixtures of such pairs, plus their limit points) over all product inputs (Thm 14.3.1, p. 389–390).
- Achievability uses independent random codebooks and joint-typicality decoding (the decoder accepts a codeword pair only if it is statistically typical together with the received sequence). The error events for "wrong i", "wrong j" and "both wrong" give the three inequalities (p. 393–394).
- Corner points are interpreted as decoding one sender while treating the other as noise, then subtracting it. Time sharing (using one code for part of the block and another for the rest) gives the points in between (p. 395–396).
- A time-sharing variable $Q$ with $|\mathcal Q|\le 4$ folds the convex hull into one formula. The converse uses Fano, the data processing inequality and a uniformly random time index (p. 397–402).
- Gaussian MAC: the region is bounded by $C(P_1/N)$, $C(P_2/N)$ and $C((P_1+P_2)/N)$. Frequency division (each sender gets its own frequency band) touches the capacity boundary at one point (p. 406–407).
- Slepian–Wolf: separate encoders of correlated $(X,Y)$ lose nothing in total rate, since $R_1+R_2\ge H(X,Y)$ is enough (Thm 14.4.1, p. 407–409).
- Achievability uses random binning (each source sequence gets a random bin index, like a hash). The encoders need no typical set (the set of likely sequences), only the decoder does (p. 410–413).

## L3 — Walkthrough

### End of §14.2 (p. 388)
The chain ends with $\doteq 2^{-n(I(S_1;S_2|S_3)\pm 6\epsilon)}$ (14.51). The author says this theorem will be specialised to particular choices of $S_1,S_2,S_3$ in the achievability proofs of the chapter (p. 388).

### 14.3 The multiple access channel (p. 388–392)
Two (or more) senders send to a common receiver. Example: a satellite receiver with many ground stations. Senders face receiver noise and each other's interference (p. 388).

**Definitions (p. 388–389).**
- A discrete memoryless MAC is $(\mathcal X_1,\mathcal X_2,\mathcal Y,p(y|x_1,x_2))$.
- A $((2^{nR_1},2^{nR_2}),n)$ code has message sets $\mathcal W_1=\{1,\dots,2^{nR_1}\}$, $\mathcal W_2=\{1,\dots,2^{nR_2}\}$, encoders
$$X_1:\mathcal W_1\to\mathcal X_1^n,\tag{14.52}$$
$$X_2:\mathcal W_2\to\mathcal X_2^n,\tag{14.53}$$
and a decoder
$$g:\mathcal Y^n\to\mathcal W_1\times\mathcal W_2.\tag{14.54}$$
- Messages are independent and uniform. The average error is
$$P_e^{(n)}=\frac{1}{2^{n(R_1+R_2)}}\sum_{(w_1,w_2)\in\mathcal W_1\times\mathcal W_2}\Pr\{g(Y^n)\neq(w_1,w_2)\mid(w_1,w_2)\text{ sent}\}.\tag{14.55}$$
- A rate pair is *achievable* if some sequence of codes has $P_e^{(n)}\to0$. The *capacity region* is the closure of the achievable pairs (p. 389).

**Theorem 14.3.1 (p. 389–390).** The capacity region is the closure of the convex hull of all $(R_1,R_2)$ satisfying
$$R_1<I(X_1;Y|X_2),\tag{14.56}$$
$$R_2<I(X_2;Y|X_1),\tag{14.57}$$
$$R_1+R_2<I(X_1,X_2;Y)\tag{14.58}$$
for some product distribution $p_1(x_1)p_2(x_2)$ on $\mathcal X_1\times\mathcal X_2$.

**Examples (p. 390–392).**
- *Independent BSCs (14.3.1).* Rates $1-H(p_1)$ and $1-H(p_2)$ are achievable with no interference. The region is a rectangle (Fig. 14.10) (p. 390).
- *Binary multiplier channel (14.3.2)*, $Y=X_1X_2$ (14.59). Setting $X_2=1$ gives $R_1=1$, and setting $X_1=1$ gives $R_2=1$. The output is binary, so $R_1+R_2\le1$. Time sharing gives every pair with $R_1+R_2=1$, a triangle (Fig. 14.11) (p. 390–391).
- *Binary erasure MAC (14.3.3)*, $Y=X_1+X_2\in\{0,1,2\}$. $Y=0$ or $2$ is unambiguous. $Y=1$ comes from $(0,1)$ or $(1,0)$. The axis points $(1,0)$ and $(0,1)$ are achievable. If $R_1=1$, $X_1$ must contain all binary sequences and looks like a Bernoulli(½) process. For sender 2 the channel is then a binary erasure channel with erasure probability ½ (Fig. 14.12), of capacity ½ bit. So $(1,\tfrac12)$ is achieved. The author says the region (Fig. 14.13) can be verified to be best possible after the capacity theorem is derived (p. 391–392).

*Intuition note:* Each sender's rate is limited by what it could send if the other's codeword were known. The sum rate is limited by what the output can tell about both inputs together.

### 14.3.1 Achievability (p. 393–395)
The proof is "very similar" to the single-user proof. Fix $p(x_1,x_2)=p_1(x_1)p_2(x_2)$ (p. 393).
- *Codebooks.* Generate $2^{nR_1}$ codewords $\mathbf X_1(i)$ i.i.d. $\prod p_1(x_{1k})$, and $2^{nR_2}$ codewords $\mathbf X_2(j)$ i.i.d. $\prod p_2(x_{2k})$. The codebook is revealed to senders and receiver.
- *Decoding.* With $A_\epsilon^{(n)}$ the set of jointly typical $(\mathbf x_1,\mathbf x_2,\mathbf y)$, choose $(i,j)$ with
$$(\mathbf x_1(i),\mathbf x_2(j),\mathbf y)\in A_\epsilon^{(n)}\tag{14.60}$$
if such a pair exists and is unique. Otherwise declare an error.
- *Error analysis.* By symmetry assume $(1,1)$ was sent. Define $E_{ij}=\{(\mathbf X_1(i),\mathbf X_2(j),\mathbf Y)\in A_\epsilon^{(n)}\}$ (14.61). With $P$ the probability given $(1,1)$ sent,
$$P_e^{(n)}=P\Big(E_{11}^c\cup\bigcup_{(i,j)\ne(1,1)}E_{ij}\Big)\tag{14.62}$$
$$\le P(E_{11}^c)+\sum_{i\ne1,j=1}P(E_{i1})+\sum_{i=1,j\ne1}P(E_{1j})+\sum_{i\ne1,j\ne1}P(E_{ij}).\tag{14.63}$$
- $P(E_{11}^c)\to0$ by the AEP. For $i\neq1$, using Theorems 14.2.1 and 14.2.3 (earlier in the chapter):
$$P(E_{i1})=P((\mathbf X_1(i),\mathbf X_2(1),\mathbf Y)\in A_\epsilon^{(n)})\tag{14.64}$$
$$=\sum_{A_\epsilon^{(n)}}p(\mathbf x_1)p(\mathbf x_2,\mathbf y)\tag{14.65}$$
$$\le|A_\epsilon^{(n)}|\,2^{-n(H(X_1)-\epsilon)}2^{-n(H(X_2,Y)-\epsilon)}\tag{14.66}$$
$$\le2^{-n(H(X_1)+H(X_2,Y)-H(X_1,X_2,Y)-3\epsilon)}\tag{14.67}$$
$$=2^{-n(I(X_1;X_2,Y)-3\epsilon)}\tag{14.68}$$
$$=2^{-n(I(X_1;Y|X_2)-3\epsilon)}.\tag{14.69}$$
The last step holds because $X_1,X_2$ are independent, so $I(X_1;X_2,Y)=I(X_1;X_2)+I(X_1;Y|X_2)=I(X_1;Y|X_2)$.
- Similarly, $P(E_{1j})\le2^{-n(I(X_2;Y|X_1)-3\epsilon)}$ (14.70) and, for $i\ne1,j\ne1$, $P(E_{ij})\le2^{-n(I(X_1,X_2;Y)-4\epsilon)}$ (14.71).
- Counting the number of wrong indices of each kind:
$$P_e^{(n)}\le P(E_{11}^c)+2^{nR_1}2^{-n(I(X_1;Y|X_2)-3\epsilon)}+2^{nR_2}2^{-n(I(X_2;Y|X_1)-3\epsilon)}+2^{n(R_1+R_2)}2^{-n(I(X_1,X_2;Y)-4\epsilon)}.\tag{14.72}$$
- Since $\epsilon>0$ is arbitrary, the conditions of the theorem make each term tend to 0. The codebook-averaged error is small, so at least one code $\mathcal C^*$ has small error. Timesharing then covers the convex hull (p. 394–395).

*Intuition note:* Each way the decoder can be wrong (wrong sender 1 only, wrong sender 2 only, both wrong) gives one inequality. The "both wrong" event involves the most codeword pairs, so it gives the sum-rate bound.

### 14.3.2 Comments on the region (p. 395–396)
The region is the closure of the convex hull of (14.73)–(14.75), which repeat (14.56)–(14.58), for some $p_1p_2$ (p. 395). For a fixed $p_1p_2$ the region is a pentagon with corners A, B, C, D (Fig. 14.14) (p. 395).
- *Point A* is the maximum $R_1$ when sender 2 sends nothing:
$$\max R_1=\max_{p_1(x_1)p_2(x_2)}I(X_1;Y|X_2).\tag{14.76}$$
Since
$$I(X_1;Y|X_2)=\sum_{x_2}p_2(x_2)I(X_1;Y|X_2=x_2)\le\max_{x_2}I(X_1;Y|X_2=x_2),\tag{14.77–14.78}$$
the maximum is attained by fixing $X_2$ at the best value $x_2$. So $X_2$ must help sender 1 by setting $X_2=x_2$ (p. 395–396).
- *Point B* is the maximum $R_2$ while sender 1 sends at its maximum rate. Treat $X_1$ as noise. Sender 2 gets $I(X_2;Y)$. The receiver then knows the $X_2$ codeword (the subscript is garbled in the text layer; this reading follows from the context) and subtracts it. This leaves an indexed set of single-user channels for $X_1$. The $X_1$ rate is the average mutual information over these, which would be $I(X_1;Y|X_2)$ (equation 14.79 is blank in the image; this is my inference from the surrounding text) (p. 396).
- C and D are B and A with the roles of the senders reversed. Non-corner points come from timesharing (p. 396).
- The idea of treating the other signal as noise, decoding, and subtracting returns for the degraded broadcast channel (p. 396).

### 14.3.3 Convexity; the time-sharing variable (p. 396–399)
**Theorem 14.3.2.** The capacity region $\mathcal C$ is convex (p. 396). *Proof (timesharing):* use the first code for the first $\lambda n$ symbols and the second code for the last $(1-\lambda)n$ symbols. The number of $\mathbf X_1$ codewords is
$$2^{n\lambda R_1}2^{n(1-\lambda)R_1'}=2^{n(\lambda R_1+(1-\lambda)R_1')}\tag{14.80}$$
(and similarly for $X_2$). So the rate is $\lambda\mathbf R+(1-\lambda)\mathbf R'$. The error is below the sum of the segment errors, so it goes to 0 (p. 396–397).

**Theorem 14.3.3 (p. 397).** The achievable set is the closure of all $(R_1,R_2)$ with
$$R_1<I(X_1;Y|X_2,Q),\quad R_2<I(X_2;Y|X_1,Q),\quad R_1+R_2<I(X_1,X_2;Y|Q)\tag{14.81}$$
for some $p(q)p(x_1|q)p(x_2|q)p(y|x_1,x_2)$ with $|\mathcal Q|\le4$.

*Proof sketch (p. 397–398).* One direction: write
$$I(X_1;Y|X_2,Q)=\sum_{k=1}^m p(q)I(X_1;Y|X_2,Q=q)=\sum_k p(q)I(X_1;Y|X_2)_{p_{1q},p_{2q}}\tag{14.82–14.83}$$
and do the same for the other terms. Let $\mathbf R_q=(R_{1q},R_{2q})$ satisfy
$$R_{1q}<I(X_1;Y|X_2)_{p_{1q}p_{2q}},\tag{14.84}$$
$$R_{2q}<I(X_2;Y|X_1)_{p_{1q}p_{2q}},\tag{14.85}$$
and the sum-rate inequality (14.86; not visible in the image). Each $\mathbf R_q$ is achievable by Thm 14.3.1. Any $\mathbf R$ satisfying (14.81) can be written $\mathbf R=\sum_q p(q)\mathbf R_q$ (14.87). A convex combination of achievable rates is achievable, so $\mathbf R$ is achievable. The same argument reverses: any point of the convex closure of the region of (14.58) is a mixture of such points and so has the form (14.81) (p. 398).

**Theorem 14.3.4 (Carathéodory).** Any point in the convex closure of a connected compact set $A$ in $d$-dimensional Euclidean space is a convex combination of $d+1$ or fewer points of $A$. The proof is cited (Eggleston, Grünbaum) and omitted (p. 398). The MAC bounds define a connected compact set in three dimensions, so four points suffice and $|\mathcal Q|\le4$ (p. 398–399). Without such a bound the region could not be computed, since we would never know whether a larger alphabet would enlarge it (p. 398).

*Intuition note:* $Q$ is a "which code segment" label. Averaging over $Q$ replaces taking a convex hull, and Carathéodory says four segments are always enough here.

### 14.3.4 Converse (p. 399–402)
Claim: any sequence of codes with $P_e^{(n)}\to0$ has rates satisfying
$$R_1\le I(X_1;Y|X_2,Q),\quad R_2\le I(X_2;Y|X_1,Q),\quad R_1+R_2\le I(X_1,X_2;Y|Q)\tag{14.88}$$
for some $Q$ on $\{1,2,3,4\}$ and $p(q)p(x_1|q)p(x_2|q)p(y|x_1,x_2)$ (p. 399).

The joint distribution of the fixed block-length-$n$ code is
$$p(w_1,w_2,x_1^n,x_2^n,y^n)=\frac1{2^{nR_1}}\frac1{2^{nR_2}}p(x_1^n|w_1)p(x_2^n|w_2)\prod_{i=1}^np(y_i|x_{1i},x_{2i}),\tag{14.89}$$
where $p(x_1^n|w_1)\in\{0,1\}$ says whether $x_1^n=\mathbf x_1(w_1)$ (p. 399). Fano's inequality gives
$$H(W_1,W_2|Y^n)\le n(R_1+R_2)P_e^{(n)}+H(P_e^{(n)})\triangleq n\epsilon_n,\tag{14.90}$$
with $\epsilon_n\to0$ as $P_e^{(n)}\to0$. Hence $H(W_1|Y^n)\le H(W_1,W_2|Y^n)\le n\epsilon_n$ (14.91) and $H(W_2|Y^n)\le n\epsilon_n$ (14.92) (p. 399–400).

Bound on $R_1$ (p. 400):
$$nR_1=H(W_1)\tag{14.93}$$
$$=I(W_1;Y^n)+H(W_1|Y^n)\tag{14.94}$$
$$\overset{(a)}\le I(W_1;Y^n)+n\epsilon_n\tag{14.95}$$
$$\overset{(b)}\le I(X_1^n(W_1);Y^n)+n\epsilon_n\tag{14.96}$$
$$=H(X_1^n(W_1))-H(X_1^n(W_1)|Y^n)+n\epsilon_n\tag{14.97}$$
$$\overset{(c)}\le H(X_1^n(W_1)|X_2^n(W_2))-H(X_1^n(W_1)|Y^n,X_2^n(W_2))+n\epsilon_n\tag{14.98}$$
$$=I(X_1^n(W_1);Y^n|X_2^n(W_2))+n\epsilon_n\tag{14.99}$$
$$=H(Y^n|X_2^n(W_2))-H(Y^n|X_1^n(W_1),X_2^n(W_2))+n\epsilon_n\tag{14.100}$$
$$\overset{(d)}=H(Y^n|X_2^n(W_2))-\sum_{i=1}^nH(Y_i|Y^{i-1},X_1^n(W_1),X_2^n(W_2))+n\epsilon_n\tag{14.101}$$
$$\overset{(e)}=H(Y^n|X_2^n(W_2))-\sum_iH(Y_i|X_{1i},X_{2i})+n\epsilon_n\tag{14.102}$$
$$\overset{(f)}\le\sum_iH(Y_i|X_2^n(W_2))-\sum_iH(Y_i|X_{1i},X_{2i})+n\epsilon_n\tag{14.103}$$
$$\overset{(g)}\le\sum_iH(Y_i|X_{2i})-\sum_iH(Y_i|X_{1i},X_{2i})+n\epsilon_n\tag{14.104}$$
$$=\sum_iI(X_{1i};Y_i|X_{2i})+n\epsilon_n.\tag{14.105}$$
Reasons: (a) Fano; (b) data processing; (c) $W_1,W_2$ independent, so $X_1^n(W_1),X_2^n(W_2)$ are independent and $H(X_1^n|X_2^n)=H(X_1^n)$, and conditioning reduces entropy; (d) chain rule; (e) memoryless channel; (f) chain rule and removing conditioning; (g) removing conditioning (p. 400).

Hence $R_1\le\frac1n\sum_iI(X_{1i};Y_i|X_{2i})+\epsilon_n$ (14.106), and likewise $R_2\le\frac1n\sum_iI(X_{2i};Y_i|X_{1i})+\epsilon_n$ (14.107) (p. 401).

Sum rate (p. 401):
$$n(R_1+R_2)=H(W_1,W_2)=I(W_1,W_2;Y^n)+H(W_1,W_2|Y^n)\tag{14.108–14.109}$$
$$\overset{(a)}\le I(W_1,W_2;Y^n)+n\epsilon_n\overset{(b)}\le I(X_1^n(W_1),X_2^n(W_2);Y^n)+n\epsilon_n\tag{14.110–14.111}$$
$$=H(Y^n)-H(Y^n|X_1^n(W_1),X_2^n(W_2))+n\epsilon_n\tag{14.112}$$
$$\overset{(c)}=H(Y^n)-\sum_iH(Y_i|Y^{i-1},X_1^n(W_1),X_2^n(W_2))+n\epsilon_n\tag{14.113}$$
$$\overset{(d)}=H(Y^n)-\sum_iH(Y_i|X_{1i},X_{2i})+n\epsilon_n\tag{14.114}$$
$$\overset{(e)}\le\sum_iH(Y_i)-\sum_iH(Y_i|X_{1i},X_{2i})+n\epsilon_n=\sum_iI(X_{1i},X_{2i};Y_i)+n\epsilon_n.\tag{14.115–14.116}$$
Reasons: (a) Fano; (b) data processing; (c) chain rule; (d) $Y_i$ depends only on $X_{1i},X_{2i}$; (e) chain rule and removing conditioning. So $R_1+R_2\le\frac1n\sum_iI(X_{1i},X_{2i};Y_i)+\epsilon_n$ (14.117) (p. 401).

*Time variable (p. 402).* The sums are averages of mutual informations at the empirical distributions in column $i$ of the codebook. Let $Q=i$ with probability $1/n$, and let $X_1\triangleq X_{1Q}$, $X_2\triangleq X_{2Q}$, $Y\triangleq Y_Q$. Then
$$R_1\le\frac1n\sum_iI(X_{1q};Y_q|X_{2q},Q=i)+\epsilon_n=I(X_{1Q};Y_Q|X_{2Q},Q)+\epsilon_n=I(X_1;Y|X_2,Q)+\epsilon_n\tag{14.118–14.121}$$
Independence of $W_1,W_2$ gives conditional independence of the inputs given $Q$:
$$\Pr(X_{1i}(W_1)=x_1,X_{2i}(W_2)=x_2)\triangleq\Pr\{X_{1Q}=x_1|Q=i\}\Pr\{X_{2Q}=x_2|Q=i\}.\tag{14.122}$$
Letting $n\to\infty$ and $P_e^{(n)}\to0$ gives (14.123), the same three inequalities as (14.88). The cardinality bound of 4 holds as before. The converse is complete, and (14.58) cannot be larger than (14.88) (p. 402–403).

*Intuition note:* Each of the $n$ channel uses is treated as a draw from some input distribution. Averaging over a random "time index" $Q$ turns the code into a single-letter bound.

### 14.3.5 m-user MAC (p. 403)
With $S\subseteq\{1,\dots,m\}$, $R(S)=\sum_{i\in S}R_i$ and $X(S)=\{X_i:i\in S\}$:

**Theorem 14.3.5.** The capacity region is the closure of the convex hull of the rate vectors with
$$R(S)\le I(X(S);Y|X(S^c))\ \text{ for all }S\subseteq\{1,\dots,m\}\tag{14.124}$$
for some product distribution $p_1(x_1)\cdots p_m(x_m)$.
The proof "contains no new ideas": there are $2^m-1$ error terms and as many converse inequalities, and the details are left to the reader. In general the region is a beveled box (p. 403).

### 14.3.6 Gaussian MAC (p. 403–407)
Model: $Y_i=X_{1i}+X_{2i}+Z_i$ (14.125), with $Z_i$ i.i.d. zero-mean Gaussian of variance $N$. Power constraints:
$$\frac1n\sum_{i=1}^nx_{ji}^2(w_j)\le P_j,\quad w_j\in\{1,\dots,2^{nR_j}\},\ j=1,2.\tag{14.126}$$
The author says the discrete proof extends, as in Chapter 10, and that "we expect" the region to be the convex hull of pairs with
$$R_1\le I(X_1;Y|X_2),\ R_2\le I(X_2;Y|X_1),\ R_1+R_2\le I(X_1,X_2;Y)\tag{14.127–14.129}$$
for some $f_1(x_1)f_2(x_2)$ with $EX_1^2\le P_1$, $EX_2^2\le P_2$ (p. 404).

Expanding in differential entropy (p. 404–405):
$$I(X_1;Y|X_2)=h(Y|X_2)-h(Y|X_1,X_2)=h(X_1+X_2+Z|X_2)-h(X_1+X_2+Z|X_1,X_2)\tag{14.130–14.131}$$
$$=h(X_1+Z|X_2)-h(Z|X_1,X_2)=h(X_1+Z|X_2)-h(Z)=h(X_1+Z)-h(Z)\tag{14.132–14.134}$$
$$=h(X_1+Z)-\tfrac12\log(2\pi e)N\le\tfrac12\log(2\pi e)(P_1+N)-\tfrac12\log(2\pi e)N=\tfrac12\log\Big(1+\frac{P_1}N\Big).\tag{14.135–14.137}$$
Reasons: (14.133) $Z$ is independent of $X_1,X_2$; (14.134) $X_1,X_2$ are independent; (14.136) the normal maximizes entropy for a given second moment. The maximiser is $X_1\sim\mathcal N(0,P_1)$, $X_2\sim\mathcal N(0,P_2)$, independent, and it maximises all three bounds simultaneously (p. 405).

Define $C(x)\triangleq\frac12\log(1+x)$ (14.138), the capacity of a Gaussian white-noise channel with signal-to-noise ratio $x$. Then
$$R_1\le C\Big(\frac{P_1}N\Big),\quad R_2\le C\Big(\frac{P_2}N\Big),\quad R_1+R_2\le C\Big(\frac{P_1+P_2}N\Big).\tag{14.139–14.141}$$
These are achieved by the Gaussian inputs and define the capacity region. The "surprising" fact: the sum rate can be as large as $C((P_1+P_2)/N)$, the rate of one transmitter with power $P_1+P_2$ (p. 405).

*Corner points (p. 406).* Decode in two stages. First decode sender 2, treating sender 1 as noise. This works with low error if $R_2<C(P_2/(P_1+N))$. Then subtract sender 2 and decode sender 1, which works if $R_1<C(P_1/N)$. This achieves the corner points.

*Many senders (p. 406).* With $m$ equal-power senders the total rate is $C(mP/N)$, which goes to $\infty$ as $m\to\infty$. The rate per sender, $\frac1mC(mP/N)$, goes to 0.

*Multiplexing (p. 406–407).* The region above corresponds to Code Division Multiple Access (CDMA), with orthogonal codes and one-by-one decoding. In practice simpler schemes are used. With frequency division on disjoint bands $W_1+W_2=W$,
$$R_1=\frac{W_1}2\log\Big(1+\frac{P_1}{NW_1}\Big),\tag{14.142}$$
$$R_2=\frac{W_2}2\log\Big(1+\frac{P_2}{NW_2}\Big).\tag{14.143}$$
Varying $W_1,W_2$ traces a curve (Fig. 14.17) that touches the capacity boundary at one point. That point is bandwidth proportional to power. So no allocation of bands can be optimal unless the powers are proportional to the bandwidths. In general the capacity region is larger than the time/frequency-division region. The capacity region needs a common decoder, and the author notes that design simplicity may outweigh the gain (p. 407).

*Gauss's-law analogue.* For $m$ sources with powers $P_i$ and noise $N$ (p. 407):
$$\sum_{i\in S}R_i=\text{total rate of information flow across boundary of }S\le C\Big(\frac{\sum_{i\in S}P_i}N\Big).\tag{14.144–14.145}$$

*Intuition note:* Once a user is decoded it can be subtracted out. The sum rate can then be as large as that of one big transmitter with the summed power, though each sender gets only a share.

### 14.4 Encoding of correlated sources (p. 407–409)
This is distributed data compression, in many ways the data-compression dual of the MAC problem. A rate $R>H(X)$ suffices for one source, and $H(X,Y)$ for joint encoding of $(X,Y)\sim p(x,y)$. Separate encoding with $R_x+R_y>H(X)+H(Y)$ is clearly enough. Slepian and Wolf [255] show that total rate $H(X,Y)$ suffices even for separate encoding (p. 407). $X^n$ is at location A, $Y^n$ at B, and one decoder reconstructs both (Fig. 14.18) (p. 408).

**Definitions (p. 408).** A $((2^{nR_1},2^{nR_2}),n)$ distributed source code has encoders
$$f_1:\mathcal X^n\to\{1,\dots,2^{nR_1}\},\ f_2:\mathcal Y^n\to\{1,\dots,2^{nR_2}\}\tag{14.146–14.147}$$
and decoder $g:\{1,\dots,2^{nR_1}\}\times\{1,\dots,2^{nR_2}\}\to\mathcal X^n\times\mathcal Y^n$ (14.148). The error is
$$P_e^{(n)}=P\big(g(f_1(X^n),f_2(Y^n))\ne(X^n,Y^n)\big).\tag{14.149}$$
A rate pair is achievable if codes exist with $P_e^{(n)}\to0$. The achievable region is the closure of the achievable pairs.

**Theorem 14.4.1 (Slepian–Wolf) (p. 409).** For $(X,Y)$ i.i.d. $\sim p(x,y)$, the achievable region is
$$R_1\ge H(X|Y),\quad R_2\ge H(Y|X),\quad R_1+R_2\ge H(X,Y).\tag{14.150–14.152}$$

**Example 14.4.1 (p. 409).** Gotham's weather is sunny with probability 0.5, and Metropolis has the same weather with probability 0.89. Joint distribution: rain/rain 0.445, rain/shine 0.055, shine/rain 0.055, shine/shine 0.445. For 100 days, sending raw bits costs 200 bits. Independent compression costs $100H(0.5)=100$ bits from each place, 200 in all. Slepian–Wolf needs only $100H(0.5)+100H(0.89)=100+50=150$ bits (as printed).

**Example 14.4.2 (p. 409–410).** For a joint distribution of $(U,V)$ (table not visible in the image), the total rate is $H(U)+H(V|U)=\log3=1.58$ bits, rather than 2 bits for independent transmission.

*Intuition note:* The total rate $H(X,Y)=H(X)+H(Y|X)$ is enough even though the encoders work separately. At the corner point the second encoder's share can be as small as $H(Y|X)$, although it never sees $X$ (pp. 407, 409, 415).

### 14.4.1 Achievability (p. 410–413)
**Random bins (p. 410).** The idea is like a hash function. Give each $X^n$ a random index in $\{1,\dots,2^{nR}\}$; sequences sharing an index form a *bin*. To decode, look in the bin for a typical sequence. If exactly one exists, output it. Otherwise declare an error. A typical source sequence is always in its own bin, so an error occurs only if the bin holds another typical sequence. A non-typical source always errs.

**Single source (p. 410–411).** With $f$ the random binning and $g$ the decoder, averaging over $f$:
$$P(g(f(X))\ne X)\le P(X\notin A_\epsilon^{(n)})+\sum_{\mathbf x}P\big(\exists\mathbf x'\ne\mathbf x:\mathbf x'\in A_\epsilon^{(n)},f(\mathbf x')=f(\mathbf x)\big)p(\mathbf x)\tag{14.153}$$
$$\le\epsilon+\sum_{\mathbf x}\sum_{\mathbf x'\in A_\epsilon^{(n)}}2^{-nR}p(\mathbf x)\tag{14.154}$$
$$=\epsilon+\sum_{\mathbf x'\in A_\epsilon^{(n)}}2^{-nR}\sum_{\mathbf x}p(\mathbf x)\le\epsilon+\sum_{\mathbf x'\in A_\epsilon^{(n)}}2^{-nR}\tag{14.155–14.156}$$
$$\le\epsilon+2^{n(H(X)+\epsilon)}2^{-nR}\le2\epsilon\tag{14.157–14.158}$$
if $R>H(X)+\epsilon$ and $n$ is large. So a rate above entropy gives arbitrarily small error. The binning encoder does not need the typical set; only the decoder does. This is what lets the scheme work for distributed sources (p. 411).

**Slepian–Wolf proof (p. 411–413).**
- *Code.* Assign every $\mathbf x\in\mathcal X^n$ uniformly at random to one of $2^{nR_1}$ bins, and every $\mathbf y\in\mathcal Y^n$ to one of $2^{nR_2}$ bins. Reveal $f_1,f_2$ to encoders and decoder. Sender 1 sends the bin index of $X$, and sender 2 the bin index of $Y$.
- *Decoding.* Given $(i_0,j_0)$, declare $(\hat{\mathbf x},\hat{\mathbf y})=(\mathbf x,\mathbf y)$ if exactly one pair has $f_1(\mathbf x)=i_0$, $f_2(\mathbf y)=j_0$ and $(\mathbf x,\mathbf y)\in A_\epsilon^{(n)}$. Otherwise declare an error. Fig. 14.19 shows the product bins isolating the $2^{nH(X,Y)}$ jointly typical pairs (p. 411–412).
- *Error events (p. 412):*
$$E_0=\{(\mathbf X,\mathbf Y)\notin A_\epsilon^{(n)}\},\tag{14.159}$$
$$E_1=\{\exists\mathbf x'\ne\mathbf X:f_1(\mathbf x')=f_1(\mathbf X),(\mathbf x',\mathbf Y)\in A_\epsilon^{(n)}\},\tag{14.160}$$
$$E_2=\{\exists\mathbf y'\ne\mathbf Y:f_2(\mathbf y')=f_2(\mathbf Y),(\mathbf X,\mathbf y')\in A_\epsilon^{(n)}\},\tag{14.161}$$
$$E_{12}=\{\exists(\mathbf x',\mathbf y'):\mathbf x'\ne\mathbf X,\mathbf y'\ne\mathbf Y,f_1(\mathbf x')=f_1(\mathbf X),f_2(\mathbf y')=f_2(\mathbf Y),(\mathbf x',\mathbf y')\in A_\epsilon^{(n)}\}.\tag{14.162}$$
Union bound: $P_e^{(n)}\le P(E_0)+P(E_1)+P(E_2)+P(E_{12})$ (14.163–14.164). By the AEP, $P(E_0)<\epsilon$ for large $n$ (p. 412).
- *Bound on $E_1$ (p. 412–413):*
$$P(E_1)=\sum_{(\mathbf x,\mathbf y)}p(\mathbf x,\mathbf y)P\{\exists\mathbf x'\ne\mathbf x:f_1(\mathbf x')=f_1(\mathbf x),(\mathbf x',\mathbf y)\in A_\epsilon^{(n)}\}\tag{14.165–14.166}$$
$$\le\sum_{(\mathbf x,\mathbf y)}p(\mathbf x,\mathbf y)\sum_{\mathbf x'\ne\mathbf x,(\mathbf x',\mathbf y)\in A_\epsilon^{(n)}}P(f_1(\mathbf x')=f_1(\mathbf x))\tag{14.167}$$
$$=\sum p(\mathbf x,\mathbf y)2^{-nR_1}|A_\epsilon(X|\mathbf y)|\le2^{-nR_1}2^{n(H(X|Y)+\epsilon)}\ \ (\text{Thm 14.2.2}),\tag{14.168–14.169}$$
which goes to 0 if $R_1>H(X|Y)$. Similarly $P(E_2)<\epsilon$ if $R_2>H(Y|X)$, and $P(E_{12})<\epsilon$ if $R_1+R_2>H(X,Y)$, for large $n$.
- The average error is $<4\epsilon$, so a code $(f_1^*,f_2^*,g^*)$ with error $<4\epsilon$ exists. Hence there are codes with $P_e^{(n)}\to0$ (p. 413).

*Intuition note:* Random bins act as hash codes. The decoder's own side knowledge (the other source and joint typicality) picks the right sequence out of the bin. This works as long as bins are numerous enough to separate the typical candidates.

### 14.4.2 Converse (p. 413–415)
The author says this follows from single-source results but gives it for completeness. Let $I_0=f_1(X^n)$ and $J_0=f_2(Y^n)$. By Fano (p. 413):
$$H(X^n,Y^n|I_0,J_0)\le P_e^{(n)}n(\log|\mathcal X|+\log|\mathcal Y|)+1=n\epsilon_n\tag{14.170}$$
with $\epsilon_n\to0$, and with more conditioning,
$$H(X^n|Y^n,I_0,J_0)\le P_e^{(n)}n\epsilon_n,\quad H(Y^n|X^n,I_0,J_0)\le P_e^{(n)}n\epsilon_n.\tag{14.171–14.172}$$
(These are as printed; since $P_e^{(n)}\le1$ they imply the bound $n\epsilon_n$ used below.) Sum rate (p. 413–414):
$$n(R_1+R_2)\overset{(a)}\ge H(I_0,J_0)=I(X^n,Y^n;I_0,J_0)+H(I_0,J_0|X^n,Y^n)\tag{14.173–14.174}$$
$$\overset{(b)}=I(X^n,Y^n;I_0,J_0)=H(X^n,Y^n)-H(X^n,Y^n|I_0,J_0)\tag{14.175–14.176}$$
$$\overset{(c)}\ge H(X^n,Y^n)-n\epsilon_n\overset{(d)}=nH(X,Y)-n\epsilon_n.\tag{14.177–14.178}$$
Reasons: (a) $I_0,J_0$ take at most $2^{nR_1},2^{nR_2}$ values; (b) $I_0$ is a function of $X^n$ and $J_0$ of $Y^n$; (c) Fano; (d) chain rule and i.i.d. For $R_1$ (p. 414):
$$nR_1\overset{(a)}\ge H(I_0)\ge H(I_0|Y^n)=I(X^n;I_0|Y^n)+H(I_0|X^n,Y^n)\overset{(b)}=I(X^n;I_0|Y^n)\tag{14.179–14.182}$$
$$=H(X^n|Y^n)-H(X^n|I_0,J_0,Y^n)\overset{(c)}\ge H(X^n|Y^n)-n\epsilon_n\overset{(d)}=nH(X|Y)-n\epsilon_n.\tag{14.183–14.185}$$
Similarly $nR_2\ge nH(Y|X)-n\epsilon_n$ (14.186). Divide by $n$ and let $n\to\infty$. The region is drawn in Fig. 14.20, a corner-cut region with corner values $H(X|Y)$, $H(X)$, $H(Y|X)$, $H(Y)$ (p. 415).

### 14.4.3 Many sources (p. 415)
**Theorem 14.4.2.** For $(X_{1i},\dots,X_{mi})$ i.i.d. $\sim p(x_1,\dots,x_m)$, the rate vectors achievable with separate encoders and a common decoder are given by
$$R(S)>H(X(S)|X(S^c))\ \text{ for all }S\subseteq\{1,\dots,m\},\ R(S)=\sum_{i\in S}R_i\tag{14.187–14.188}$$
(inequality as printed). The proof is "identical" and omitted. The achievability extends to any joint source satisfying the AEP, in particular any jointly ergodic source [63]. In those cases entropies are replaced by entropy rates (p. 415).

### Start of 14.4.4 (p. 415)
The unit ends as the author begins a graph-colouring reading of the corner point $R_1=H(X)$, $R_2=H(Y|X)$, with a "fan" of $Y^n$ sequences jointly typical with each $X^n$ (Fig. 14.21 begins on the next page, outside this unit).

## Toy example (ours, not from the text)
Slepian–Wolf corner point with $n=1$. Let $X$ be uniform on $\{0,1,2,3\}$, and let $Y=X$ or $Y=X+1\pmod4$, each with probability $\tfrac12$.
- $H(X)=\log_24=2$ bits.
- $H(Y|X)=1$ bit, since two equally likely values.
- $H(X,Y)=2+1=3$ bits.
- Independent compression needs $H(X)+H(Y)$. $Y$ is uniform because $P(Y=y)=\tfrac14\cdot\tfrac12+\tfrac14\cdot\tfrac12=\tfrac14$. So $H(Y)=2$, and the total is $2+2=4$ bits.
- Slepian–Wolf corner $(R_1,R_2)=(H(X),H(Y|X))=(2,1)$ gives total 3 bits.
- Binning scheme: encoder 1 sends $x$ in 2 bits. Encoder 2 sees only $y$ and sends its parity, 1 bit. The bins are $\{0,2\}$ and $\{1,3\}$.
- Decoding: the decoder knows $x$, and the candidates are $x$ and $x+1\bmod4$, which have different parity. The parity picks $y$ exactly. Example: $x=3$, candidates $3$ and $0$. Parity 0 means $y=0$.
- This is zero-error with 3 bits instead of 4, matching $H(X,Y)=3$. Here the "typical set" is just the set of two candidates, and the bins separate them.

## Concepts
- [[multiple-access-channel]] (new) — several independent senders, one receiver, channel $p(y|x_1,x_2)$ (p. 388).
- [[capacity-region]] (new) — closure of the set of achievable rate pairs (p. 389).
- [[time-sharing]] (new) — using different codes on different fractions of the block; yields the convex hull; formalised by $Q$ (p. 396–397).
- [[noisy-channel-coding-theorem]] — its random-coding proof is extended here to two senders (p. 393).
- [[typical-set-aep]] — joint typicality decoding and the AEP bound on $P(E_{11}^c)$ (p. 393–394).
- [[mutual-information]] — conditional mutual informations bound the rates (p. 389–390).
- [[fanos-inequality]] — used in all converses (p. 399, 413).
- [[data-processing-inequality]] — step (b) of the converse (p. 400).
- [[differential-entropy]] — used to evaluate Gaussian MAC bounds (p. 404–405).
- [[gaussian-mac-capacity]] (new) — $R_1\le C(P_1/N)$, $R_2\le C(P_2/N)$, $R_1+R_2\le C((P_1+P_2)/N)$ with $C(x)=\frac12\log(1+x)$ (p. 405).
- [[successive-decoding]] (new) — decode one sender treating the other as noise, then subtract; reaches the corner points (p. 396, 406).
- [[slepian-wolf-coding]] (new) — distributed lossless compression with region $R_1\ge H(X|Y)$, $R_2\ge H(Y|X)$, $R_1+R_2\ge H(X,Y)$ (p. 409).
- [[random-binning]] (new) — hash-like random assignment of sequences to bins; only the decoder uses typicality (p. 410).
- [[caratheodory-theorem]] (new) — a point in the convex closure in $d$ dimensions needs at most $d+1$ points (p. 398).
- [[entropy-rate]] — replaces entropies when the source is jointly ergodic (p. 415).

## Canonical instances
- [[independent-bsc-mac]] — two non-interfering channels give a rectangular region (p. 390).
- [[binary-multiplier-channel]] — $Y=X_1X_2$; the region is the triangle $R_1+R_2\le1$ (p. 390–391).
- [[binary-erasure-mac]] — $Y=X_1+X_2$; the point $(1,\tfrac12)$ comes from a binary erasure channel for the second sender (p. 391–392).
- [[gaussian-mac-fdm]] — frequency division touches the capacity boundary only at the point where bandwidths are proportional to powers (p. 406–407).
- [[gotham-metropolis-weather]] — 150 bits instead of 200 with Slepian–Wolf (p. 409).

## Bridges (candidates)
- [structural-analogy] MAC capacity region ↔ Slepian–Wolf region — the same $H(X|Y)$-style conditional bounds with a sum constraint; the author calls the problems duals (p. 407).
- [structural-analogy] Random binning ↔ hashing in computer science — the author says the idea is "very similar to hash functions" (p. 410).
- [structural-analogy] Successive decoding and subtraction ↔ chain rule decomposition $I(X_1,X_2;Y)=I(X_2;Y)+I(X_1;Y|X_2)$ — each corner is a chain-rule ordering (p. 396).
- [metaphor] "Gauss's law for information flow" (14.144) ↔ physics: flux across a boundary — author's own analogy (p. 407).

## Questions this raises
- Is the MAC region still given by (14.58) when the senders' messages are correlated or when feedback is available?
- Why is a common decoder essential, and how much capacity is lost with the simple time/frequency-division schemes the author mentions?
- For Slepian–Wolf, how can the corner point $R_2=H(Y|X)$ be implemented concretely? (The unit ends as the graph-colouring interpretation begins.)
- Does Slepian–Wolf coding extend to lossy reconstruction, and does the converse still hold for non-i.i.d. sources?

## Reading notes
- **Part boundaries.** The unit starts at the last lines of a proof from §14.2 (eqs. 14.50–14.51, p. 388) and §14.3 begins on the same page. It ends at the start of §14.4.4 (p. 415), before Figure 14.21.
- **Edition.** The PDF is the 1991 first edition (Wiley), not the 2006 second edition. Page headers read "NETWORK INFORMATION THEORY". Printed = pdf − 22.
- **Equations not readable in the images.** Eqs. (14.79) (p. 396) and (14.86) (p. 398) are blank or garbled; the table for Example 14.4.2 on p. 409 is missing in the image. The text layer reads "Example 14.43" on p. 409; I call it 14.4.2, following Example 14.4.1 just before it.
- **Garbled symbols and text-layer divergences.**
  - Subscripts of $X_1$/$X_2$ on p. 396: I read the receiver as knowing the $X_2$ codeword.
  - (14.171–14.172): the right-hand side prints $P_e^{(n)}n\epsilon_n$, which I give as printed; it is at most $n\epsilon_n$ because $P_e^{(n)}\le1$.
  - Thm 14.4.1 on p. 409: the text layer is ambiguous between $>$ and $\ge$; I read $\ge$ from the image. The achievability proof uses strict $>$, and the region is a closure.
  - Thm 14.4.2 (14.187) prints $>$.
  - Here $n\epsilon_n$ is defined by Fano's inequality in (14.90) and (14.170). (14.162) on p. 412: the second bin condition on $f_2$ appears printed as $\ne$ in the page image; I write $=$, which the proof requires.
- **Cited but not in this unit.** Theorems 14.2.1, 14.2.2, 14.2.3, Chapter 3, Chapter 8, Chapter 10 and the degraded broadcast channel are referred to but are not in these pages. I use them only as the author does.
