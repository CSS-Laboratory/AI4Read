---
id: polyanskiy-2025-information/ch28-rate
work: polyanskiy-2025-information
unit: "Chapter 25 (printed): Rate distortion: achievability bounds"
pages: 490-506
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Rate distortion: achievability bounds

## L0 — One line
Random codebooks drawn from the output marginal compress a memoryless source at rate $\phi_S(D)=\min I(S;\hat S)$, so $R(D)=R^{(I)}(D)$; the same random-coding idea gives the covering lemma ($R>I(A;B)$) and the soft-covering lemma (about $2^{I(X;Y)}$ i.i.d. inputs), which is used to show that fooling every tester in total variation is possible at rate $R>C(A;B)$.

## L1 — The gist (≤ 120 words)
The previous chapter proved the converse $R(D)\ge\phi_S(D)$. This chapter asks whether $\phi_S(D)$ bits per symbol suffice. Answer: yes, for memoryless sources under mild conditions, by random coding. Codewords are drawn i.i.d. from the output marginal, and a general bound on average distortion is applied to $n$-letter blocks. A large-deviations heuristic explains why mutual information appears. The same machinery gives the covering lemma, which fools a fixed test set at rate $I(A;B)$. A stronger requirement, fooling every tester in total variation, needs the larger rate $C(A;B)$ (Wyner's common information). This is proved via the soft-covering lemma.

**Prerequisites:** mutual information and information density; KL and Rényi divergence; large deviations (Chapter 15); typical sequences and types; total variation and coupling; law of large numbers; uniform integrability.

## L2 — Key ideas (5–10 bullets)
- Under three conditions (non-negative separable $d$, $D>D_0$, $D_{\max}<\infty$), $R(D)=R^{(I)}(D)=\phi_S(D)$ for memoryless sources (p. 491).
- Heuristic: with $M$ codewords drawn i.i.d. from $Q_{\hat S}^n$, failure probability is about $(1-2^{-nE(Q_{\hat S})})^M$. Minimising over $Q_{\hat S}$ turns the exponent into $\phi_S(D)$ (p. 493).
- Theorem 25.2: a one-shot random-coding bound on average distortion, with a fail-safe codeword $y_0$ and a threshold $\gamma$ on the information density (pp. 493–495).
- Applying Theorem 25.2 to $S^n$, with the law of large numbers and uniform integrability, proves achievability (p. 496–497).
- Covering lemma: $R>I(A;B)$ suffices to make one fixed test set $F$ accept $(A^n,\text{codeword})$ with at least the probability it accepts the true i.i.d. pair, up to $o(1)$. For finite alphabets this gives joint typicality, and $R\ge I(A;B)$ is also necessary (pp. 498–500).
- Markov lemma (Prop. 25.7): an extra variable $X^n$ generated after $(A^n,\hat B^n)$ stays jointly typical, and $I(X^n;\hat B^n)\ge nI(X;B)+o(n)$ (p. 501).
- To fool all testers in total variation, the rate must reach Wyner's common information $C(A;B)=\min_{A\to U\to B}I(A,B;U)\ge I(A;B)$ (p. 503).
- Soft-covering: $n\approx 2^{I(X;Y)}$ i.i.d. inputs (assuming $I(X;Y)\gg1$ and concentration of $i(X;Y)$ around $I(X;Y)$) make the mixed channel output close to $P_Y$ in KL; the proof uses a Rényi-mutual-information bound (pp. 504–506).

## L3 — Walkthrough

### Chapter opening: recap (p. 490)
Definitions from the previous chapter:
$$R(D)=\limsup_{n\to\infty}\tfrac1n\log M^*(n,D),\qquad R^{(I)}(D)=\limsup_{n\to\infty}\tfrac1n\phi_{S^n}(D),$$
$$\phi_S(D)\triangleq\inf_{P_{\hat S|S}:\,\mathbb E[d(S,\hat S)]\le D} I(S;\hat S)\tag{25.1}$$
$$\phi_{S^n}(D)=\inf_{P_{\hat S^n|S^n}:\,\mathbb E[d(S^n,\hat S^n)]\le D} I(S^n;\hat S^n)\tag{25.2}$$
with $d(S^n,\hat S^n)=\frac1n\sum_i d(S_i,\hat S_i)$ (separable). Converse (Theorem 24.3): any scheme with $\mathbb E[d(X,\hat X)]\le D$ has $\log M\ge\phi_X(D)$, so $R(D)\ge R^{(I)}(D)$. For i.i.d. sources $\phi_{S^n}(D)=n\phi_S(D)$ (Theorem 24.8), so $R(D)\ge R^{(I)}(D)=\phi_S(D)$. Goal: equality.

### 25.1 Shannon's rate-distortion theorem (pp. 490–497)

**Theorem 25.1.** Let $S^n$ be i.i.d. $P_S$. Assume (1) $d(s^n,\hat s^n)$ is non-negative and separable; (2) $D>D_0$, where $D_0=\inf\{D:\phi_S(D)<\infty\}$; (3) $D_{\max}\triangleq\inf_{\hat s}\mathbb E[d(S,\hat s)]<\infty$ (25.3). Then
$$R(D)=R^{(I)}(D)=\phi_S(D)=\inf_{P_{\hat S|S}:\,\mathbb E[d(S,\hat S)]\le D}I(S;\hat S).\tag{25.4}$$
(p. 491)

**Remark 25.1** (p. 491–492).
- $D_{\max}<\infty$ allows $d(s,\hat s)=\infty$ for some pairs.
- When $D_{\max}=\infty$, typically $R(D)=\infty$ for all $D$. If $d$ is a metric, a finite codebook has $\max_j d(x_0,c_j)<\infty$, so $\mathbb E[d(X,\hat X)]\ge\mathbb E[d(X,x_0)]-\max_j d(x_0,c_j)=\infty$. This only rules out fixed-length codes.
- Example: quadratic distortion and Cauchy $S$ give $D_{\max}=\infty$, yet $R^{(I)}(D)<\infty$ for every $D\in(0,\infty)$ (footnote 1: quantize $S$ finely; its differential entropy is finite). Open question: is $H(W)=nR^{(I)}(D)+o(n)$ attainable with variable-length codes?
- $D>D_0$ is needed because possibly $R(D_0)\ne R^{(I)}(D_0)$. Example: a non-uniform i.i.d. source on a finite metric space has $D_0=0$ and $R(D_0+)<R(D_0)$ (Exercise V.5), while $R^{(I)}$ is continuous at $D_0$ (Theorem 24.4(d)).
- The techniques extend to stationary ergodic sources, as in Chapter 12.

#### 25.1.1 Intuition (pp. 492–493)
Throw $M$ random points $\mathcal C=\{c_1,\dots,c_M\}$ into $\hat{\mathcal A}^n$, i.i.d. from $Q_{\hat S}^n$. Encoder and decoder:
$$f(s^n)=\arg\min_{j\in[M]}d(s^n,c_j)\tag{25.5}$$
$$g(j)=c_j\tag{25.6}$$
Each codeword is close to $s^n$ with small probability $\epsilon$. With many codewords, the chance that none is good is about $(1-\epsilon)^M$, small if $M\gg1/\epsilon$. Precisely,
$$P_{\text{failure}}\triangleq\mathbb P[\forall c\in\mathcal C,\ d(S^n,c)>D]=\mathbb E_{S^n}\big[\mathbb P[d(S^n,c_1)>D\mid S^n]^M\big],$$
and with $\hat S^n\sim Q^n_{\hat S}$ independent of $S^n$,
$$\mathbb P[d(S^n,c_1)>D\mid S^n]=\mathbb P[d(S^n,\hat S^n)>D\mid S^n].\tag{25.7}$$
*Bernoulli case.* Take $P_S=Q_{\hat S}=\mathrm{Ber}(1/2)$ and Hamming distortion with $D<1/2$. For any $s^n$, $nd(S^n,\hat S^n)\sim\mathrm{Bin}(n,1/2)$, so
$$\mathbb P[d(S^n,\hat S^n)>D\mid S^n]=\mathbb P[\mathrm{Bin}(n,\tfrac12)\ge nD]\approx 1-2^{-n(1-h(D))+o(n)}\tag{25.8}$$
(large deviations, Theorem 15.9 and Example 15.1; lower estimates on exponentially small probabilities are needed). Hence $P_{\text{failure}}=(1-2^{-n(1-h(D))+o(n)})^M\to0$ if $M=2^{n(1-h(D)+\delta)}$, $\delta>0$. Since $\phi_S(D)=1-h(D)$ here (Theorem 26.1), this proves optimality in this case (p. 493).

*General $P_S$.* Now (25.7) depends on $S^n$ through its type. Let $T_n$ be the typical realizations. Then
$$P_{\text{failure}}\approx(1-\mathbb P[d(S^n,\hat S^n)\le D\mid S^n\in T_n])^M\approx(1-2^{-nE(Q_{\hat S})})^M,\tag{25.9}$$
$$E(Q_{\hat S})=\min_{P_{\hat S|S}:\,\mathbb E[d(S,\hat S)]\le D}D(P_{\hat S|S}\|Q_{\hat S}|P_S)\tag{25.10}$$
(the text says this can be shown by large deviations analysis like information projection, Chapter 15). So $M=2^{n(E(Q_{\hat S})+\delta)}$ gives vanishing excess distortion. Optimising over $Q_{\hat S}$:
$$\min_{Q}E(Q)=\min_{P_{\hat S|S}:\,\mathbb E d\le D}\ \min_{Q}D(P_{\hat S|S}\|Q|P_S)=\min_{P_{\hat S|S}:\,\mathbb E d\le D}I(S;\hat S)=\phi_S(D),$$
where the third equality is the variational representation of mutual information (Corollary 4.2). (p. 493)

*Intuition note.* The best "random dictionary" is drawn from the output distribution of the optimal test channel. Mutual information is exactly the exponent of the chance that one random word lands near the source word.

#### 25.1.2 Proof of Theorem 25.1 (pp. 493–497)

**Theorem 25.2 (random coding bound, average distortion).** Fix $P_X$ and let $d(x,\hat x)\ge0$. For any $P_{Y|X}$ and any $y_0\in\hat{\mathcal A}$ there is a code $X\to W\to\hat X$ with $W\in[M+1]$ such that $d(X,\hat X)\le d(X,y_0)$ a.s. and, for any $\gamma>0$,
$$\mathbb E[d(X,\hat X)]\le\mathbb E[d(X,Y)]+\mathbb E[d(X,y_0)]e^{-M/\gamma}+\mathbb E[d(X,y_0)\mathbf 1\{i(X;Y)>\log\gamma\}].$$
Expectations of the first and third terms are over $P_{X,Y}=P_XP_{Y|X}$, and $i$ is the information density of this joint law. (pp. 493–494)

Remarks: $P_{Y|X}$ is used only in the analysis (it couples $P_X$ with $P_Y$), not in building the code. The codewords are drawn i.i.d. from $P_Y$. The deterministic $y_0$ (default reconstruction, with $D_{\max}=\mathbb E[d(X,y_0)]$) is a "fail-safe" codeword guarding against a terrible codebook (p. 494).

*Proof.* Draw $c_1,\dots,c_M\sim P_Y$ i.i.d., independent of $X$; set $c_{M+1}=y_0$; use (25.5)–(25.6). Then $d(X,\hat X)=\min_{j\in[M+1]}d(X,c_j)\le d(X,y_0)$. Let $\overline Y$ be an independent copy of $Y$, $P_{X,Y,\overline Y}=P_{X,Y}P_{\overline Y}$ with $P_{\overline Y}=P_Y$. For $U\in[0,a]$, $\mathbb E[U]=\int_0^a\mathbb P[U\ge u]du$, so (pp. 494–495):
$$\mathbb E\,d(X,\hat X)=\mathbb E_X\!\int_0^{d(X,y_0)}\mathbb P\Big[\min_{j\in[M+1]}d(X,c_j)>u\,\Big|\,X\Big]du\le\mathbb E_X\!\int_0^{d(X,y_0)}\mathbb P\Big[\min_{j\in[M]}d(X,c_j)>u\,\Big|\,X\Big]du$$
$$=\mathbb E_X\!\int_0^{d(X,y_0)}\mathbb P[d(X,\overline Y)>u|X]^Mdu=\mathbb E_X\!\int_0^{d(X,y_0)}(1-\mathbb P[d(X,\overline Y)\le u|X])^Mdu$$
$$\le\mathbb E_X\!\int_0^{d(X,y_0)}\big(1-\underbrace{\mathbb P[d(X,\overline Y)\le u,\ i(X,\overline Y)>-\infty|X]}_{\triangleq\delta(X,u)}\big)^Mdu.\tag{25.11}$$
Bound the integrand, for any $\gamma>0$:
$$(1-\delta(X,u))^M\le e^{-M/\gamma}+|1-\gamma\delta(X,u)|^+\tag{25.12}$$
$$=e^{-M/\gamma}+\big|1-\gamma\,\mathbb E[\exp\{-i(X;Y)\}\mathbf 1\{d(X,Y)\le u\}|X]\big|^+\tag{25.13}$$
$$\le e^{-M/\gamma}+\mathbb P[i(X;Y)>\log\gamma|X]+\mathbb P[d(X,Y)>u|X].\tag{25.14}$$
- (25.12): rule of thumb $(1-\delta)^M\approx0$ if $\delta M\gg1$ and $\approx1$ if $\delta M\ll1$. Firm version: $(1-\delta)^M\le e^{-\delta M}\le e^{-M/\gamma}+(1-\gamma\delta)_+$.
- (25.13): change of measure, (18.4) of Proposition 18.3 with $f(x,y)=\mathbf 1\{d(x,y)\le u\}$.
- (25.14): $1-\gamma\mathbb E[e^{-i}\mathbf 1\{d\le u\}|X]\le1-\gamma\mathbb E[e^{-i}\mathbf 1\{d\le u,\,i\le\log\gamma\}|X]\le1-\mathbb E[\mathbf 1\{d\le u,\,i\le\log\gamma\}|X]=\mathbb P[d>u\text{ or }i>\log\gamma|X]\le\mathbb P[d>u|X]+\mathbb P[i>\log\gamma|X]$. (The second step uses $\gamma e^{-i}\ge1$ when $i\le\log\gamma$ — added step.)

Insert into (25.11), bound $\int_0^{d(X,y_0)}\le d(X,y_0)\times$ constant terms, and extend the last integral to $\infty$:
$$\mathbb E[d(X,\hat X)]\le\mathbb E[d(X,y_0)]e^{-M/\gamma}+\mathbb E[d(X,y_0)\mathbb P[i>\log\gamma|X]]+\mathbb E_X\!\int_0^\infty\mathbb P[d(X,Y)>u|X]du,$$
and the last term equals $\mathbb E[d(X,Y)]$. $\square$

**Theorem 25.3 (excess distortion).** For any $P_{Y|X}$ there is a code with $W\in[M]$ such that for any $\gamma>0$,
$$\mathbb P[d(X,\hat X)>D]\le e^{-M/\gamma}+\mathbb P[\{d(X,Y)>D\}\cup\{i(X;Y)>\log\gamma\}].$$
Proof: as above without $y_0$, starting from $\mathbb P[d(X,\hat X)>D]=\mathbb E_X[(1-\mathbb P[d(X,\overline Y)\le D|X])^M]$. (p. 496)

*Proof of Theorem 25.1* (p. 496–497). Only achievability $R(D)\le\phi_S(D)$ is needed. WLOG $D_{\max}=\mathbb E[d(S,\hat s_0)]$ for some fixed $\hat s_0$ (otherwise take any symbol with finite expectation). Use $\hat s_0^n$ as $y_0$; by separability $\mathbb E[d(S^n,\hat s_0^n)]=D_{\max}$. Fix $\delta>0$ and $P_{\hat S|S}$ with $\mathbb E[d(S,\hat S)]\le D-\delta$ (exists since $D>D_0$). Apply Theorem 25.2 with
$P_X=P_{S^n}$, $P_{Y|X}=(P_{\hat S|S})^n$, $\log M=n(I(S;\hat S)+2\delta)$, $\log\gamma=n(I(S;\hat S)+\delta)$, $d(X,Y)=\frac1n\sum_jd(S_j,\hat S_j)$, $y_0=\hat s_0^n$. There exist $f:\mathcal A^n\to[M+1]$, $g$ with
$$\mathbb E[d(S^n,g(f(S^n)))]\le D-\delta+\underbrace{D_{\max}e^{-\exp(n\delta)}}_{\to0}+\underbrace{\mathbb E[d(S^n,\hat s_0^n)\mathbf 1_{E_n}]}_{\to0\ \text{(later)}},\tag{25.15}$$
where $E_n=\{i(S^n;\hat S^n)>\log\gamma\}=\{\frac1n\sum_ji(S_j;\hat S_j)>I(S;\hat S)+\delta\}$ and $\mathbb P[E_n]\to0$ by the weak law of large numbers. So there is an $(n,M,\bar D)$-code with $M=2^{n(I(S;\hat S)+2\delta)}$, $\bar D=D-\delta+o(1)\le D$.

*Vanishing of the last term.* **Lemma 25.4:** for positive $U$, let $g(\delta)=\sup_{H:\mathbb P[H]\le\delta}\mathbb E[U\mathbf 1_H]$. Then $\mathbb EU<\infty\Rightarrow g(\delta)\to0$ as $\delta\to0$ (footnote: the converse also holds). Proof: $\mathbb E[U\mathbf 1_H]\le\mathbb E[U\mathbf 1\{U>b\}]+b\delta$; the first term $\to0$ as $b\to\infty$ (dominated convergence); take $b=1/\sqrt\delta$. Now $d(S^n,\hat s_0^n)=\frac1n\sum U_j$, $U_j$ i.i.d. copies of $d(S,\hat s_0)$ with mean $D_{\max}<\infty$, so $\mathbb E[d(S^n,\hat s_0^n)\mathbf 1_{E_n}]\le g(\mathbb P[E_n])\to0$.

Conclusion: for every $P_{\hat S|S}$ with $\mathbb E d\le D-\delta$, $R(D)\le I(S;\hat S)$. Letting $\delta\downarrow0$ and using continuity of $\phi_S$ on $(D_0,\infty)$ (Theorem 24.4), $R(D)\le\phi_S(D-)=\phi_S(D)$. $\square$

**Remark 25.2** (p. 497). The theorem also holds for excess distortion under mild extra conditions: achievability is already in probability. For the converse, assume $D_p=\mathbb E[d(S,\hat s)^p]^{1/p}<\infty$ for some $\hat s$ and $p>1$. Rosenthal's inequality gives $\mathbb E[d(S,\hat s^n)^p]\le CD_p^p$, so Theorem 24.9 converts an excess-distortion code into an average-distortion one.

The two proofs (25.1.1 and Theorem 25.1) are two ways to estimate the large-deviations exponent of the underlined probabilities in (25.9) and (25.11). With $P_Y=P_{\hat S}^n$, the output marginal of the optimal test channel, the exponent is exactly $2^{-i(X;Y)}$ (p. 497).

*Intuition note.* The one-shot bound pays three prices: the average distortion of the test channel, a tiny penalty if $M$ is much larger than $\gamma$, and the cost of the rare event that the information density is atypically high. For i.i.d. blocks the last two vanish.

### 25.2* Covering lemma and joint typicality (pp. 497–502)
**Channel simulation game** (Figure 25.1). $A^n\sim P_A^n$ is seen at one terminal, which sends a message $W\in[2^{nR}]$ noiselessly. The decoder outputs $B^n$. A tester inspects $(A^n,B^n)$ and tries to check that it is i.i.d. $P_{A,B}$. The required $R$ depends on how the tester works. If the tester is a fixed set $F$ known in advance, this is the covering-lemma setting. If $F$ is unknown, a higher rate $C(A;B)$ is needed (next section). The text mentions, without proof, the Bennett–Shor theorem: $R=I(A;B)$ is attainable even for unknown $F$ if encoder and decoder share common random bits (p. 498).

Corner cases (p. 498): $R=H(A)$ suffices (send $A^n$, generate $B^n$ through $P_{B^n|A^n}$); $R=H(B)$ suffices (generate and send $B^n$); if $A\perp B$, $R=0$.

**Theorem 25.5 (covering lemma).** Fix $P_{A,B}$, $(A_j,B_j)$ i.i.d., $R>I(A;B)$. Draw a codebook $\mathcal C=\{c_1,\dots,c_M\}$, $\log M=nR$, each $c_j\sim P_B^n$ i.i.d. Then for all sets $F$
$$\mathbb P[\exists c:(A^n,c)\in F]\ge\mathbb P[(A^n,B^n)\in F]+o_R(1),\tag{25.16}$$
the $o_R(1)$ term being uniform in $F$. (p. 498)

Remark 25.3: with $A=S$, $B=\hat S$ (optimal reconstruction) and $F=\{d(a^n,b^n)\le D+\delta\}$, the text says both terms on the right-hand side are $o(1)$, so $2^{nR}$ points cover the space of source realizations (p. 498–499).

*Proof.* Take $\gamma$ large (printed "$\gamma>M$"; see Reading notes) and proceed as in Theorem 25.2:
$\mathbb P[\forall c:(A^n,c)\notin F]\le e^{-M/\gamma}+\mathbb P[\{(A^n,B^n)\notin F\}\cup\{i(A^n;B^n)>\log\gamma\}]=\mathbb P[(A^n,B^n)\notin F]+o(1)$. (p. 499)

**Finite alphabets.** Joint empirical distribution $\hat P_{a^n,b^n}(\alpha,\beta)=\frac1n\sum_i\mathbf 1\{a_i=\alpha,b_i=\beta\}$. Call $(a^n,b^n)$ *jointly typical* w.r.t. $P_{A,B}$ if $\mathrm{TV}(\hat P_{a^n,b^n},P_{A,B})=o(1)$. For a codebook $\mathcal C\subset\mathcal B^n$ define
$$W=\arg\min_{j\in[M]}\mathrm{TV}(\hat P_{a^n,c_j},P_{A,B}),\qquad\hat B^n=c_W.\tag{25.17}$$
**Corollary 25.6.** For finite $\mathcal A,\mathcal B$, $R>I(A;B)$, and a random codebook as in Theorem 25.5,
$$\mathbb E[\mathrm{TV}(\hat P_{A^n,\hat B^n},P_{A,B})]=o_R(1).\tag{25.18}$$
No codebook with rate $R<I(A;B)$ can achieve (25.18). (p. 499)

*Proof, achievability.* $i(A^n;B^n)$ is a sum of bounded i.i.d. terms, so the $o_R(1)$ in (25.16) is $e^{-\Omega(n)}$. For $\epsilon>0$ apply the covering lemma to $F=\{(a^n,b^n):|\hat P_{a^n,b^n}(\alpha,\beta)-P_{A,B}(\alpha,\beta)|\le\epsilon\ \forall\alpha,\beta\}$: $\mathbb P[\mathrm{TV}(\hat P_{A^n,\hat B^n},P_{A,B})\le\epsilon]\ge1-|\mathcal A||\mathcal B|e^{-\Omega(n)}$. Since $\epsilon$ is arbitrary, (25.18) follows. (pp. 499–500)

*Combinatorial view* (p. 500). An i.i.d. $B^n$ ranges over about $2^{nH(B)}$ likely sequences (Prop. 1.5). Given a typical $A^n$, about $2^{nH(B|A)}$ sequences $B^n$ are jointly typical with it. So there are about $2^{nH(B)}/2^{nH(B|A)}=2^{nI(A;B)}$ "classes", and, to make this rigorous, one would need to show that a random subset of $2^{nI(A;B)}$ right vertices of the typical-pair bipartite graph covers all left vertices (the text's own phrasing: "we need to show").

*Proof, necessity.* Suppose (25.18) holds for a codebook. Then
$$nR=\log M\ge I(A^n;\hat B^n)=nH(A)-H(A^n|\hat B^n),$$
so it suffices to show $H(A^n|\hat B^n)\le nH(A|B)+o(n)$. Define the random conditional type $\hat Q(\alpha|\beta)=\#\{i:A_i=\alpha,\hat B_i=\beta\}/\#\{i:\hat B_i=\beta\}$ (the text writes $\hat A_i$; see Reading notes). Let $T=1$ iff for some $\alpha,\beta$ either $|\frac1n\#\{i:\hat B_i=\beta\}-P_B(\beta)|>\epsilon$ or $|\hat Q(\alpha|\beta)-P_{A|B}(\alpha|\beta)|>\epsilon$. By Markov's inequality (WLOG $P_B(\beta)>0$), $\mathbb P[T=1]=o(1)$. Then
$$H(A^n|\hat B^n)\le H(A^n,T|\hat B^n)\le\log2+n\log|\mathcal A|\,\mathbb P[T=1]+H(A^n|\hat B^n,T=0).$$
The first two terms are $o(n)$. Since $\hat Q$ takes polynomially many values (Exercise I.2), $H(A^n|\hat B^n,T=0)\le H(A^n|\hat Q,\hat B^n,T=0)+O(\log n)$. Given $\hat Q$ and $n_\beta$ positions with $\hat B_i=\beta$, $A^n$ ranges over a product of multinomial coefficients. With Prop. 1.5 and continuity of entropy (Prop. 4.8), $H(A^n|\hat Q,\hat B^n,T=0)\le n(H(A|B)+\delta)$, with $\delta=\delta(\epsilon)\to0$ as $\epsilon\to0$. (pp. 500–501)

*Intuition note.* Rate $I(A;B)$ is the cost of naming one "class" of $B^n$ that is compatible with the observed $A^n$. Fewer bits cannot make the pair typical, because then $\hat B^n$ would carry too little information about $A^n$.

**Proposition 25.7.** Fix $P_{X,A,B}$ on finite alphabets. Let $(A^n,\hat B^n)$ satisfy (25.18), and generate $X^n\sim P_{X|A,B}^{\otimes n}$ given $(A^n,\hat B^n)$. Then $\mathbb E[\mathrm{TV}(\hat P_{X^n,A^n,\hat B^n},P_{X,A,B})]=o(1)$ and
$$I(X^n;\hat B^n)\ge nI(X;B)+o(n).\tag{25.19}$$
*Proof.* By (25.18) and Markov, $(A^n,\hat B^n)$ is jointly typical with probability $1-o(1)$. For fixed $(a,b,x)$ consider the $m=n\hat P_{A^n,\hat B^n}(a,b)$ positions with $A_i=a,\hat B_i=b$; among them $m'$ have $X_i=x$, and concentration gives $|m'-mP_{X|A,B}(x|a,b)|=o(m)$ with probability $1-o(1)$. A union bound gives $|\hat P_{X^n,A^n,\hat B^n}(x,a,b)-P_{X,A,B}(x,a,b)|=o(1)$ w.h.p. Summing out $a$ gives typicality of $(X^n,\hat B^n)$; the second part repeats the steps of Corollary 25.6. (pp. 501–502)

**Remark 25.4 (Markov lemma).** Typical use: $P_{X,A,B}=P_{X,A}P_{B|A}$ ($X\to A\to B$), with $(X^n,A^n)$ i.i.d. from nature and only $A^n$ observed. Joint typicality is generally not transitive (footnote 4 gives a binary counterexample with $P_X=P_A=P_B=\mathrm{Ber}(1/2)$). It works here because $X^n$ is generated *after* $(A^n,\hat B^n)$ are fixed, so it may even depend on $\hat B^n$ (p. 501). **Remark 25.5:** under $X\to A\to B$, (25.19) is known to hold with equality, citing [111, Ch. 15] (p. 502).

**Permutation-invariant testers** (p. 502). Corollary 25.6 fools testers that compute empirical averages $\frac1n\sum f(A_j,\hat B_j)\approx\mathbb E f(A,B)$ for bounded $f$. It does *not* guarantee fooling every permutation-invariant tester, i.e. $\sup_F|P_{A^n,\hat B^n}(F)-P^n_{A,B}(F)|\to0$. Example: if all codewords have a fixed composition $P_0$, the $P_B^n$-measure of that composition is $O(1/\sqrt n)$ and the tester detects it. The authors *conjecture* that $R=I(A;B)$ still suffices for this requirement.

### 25.3* Wyner's common information (pp. 502–504)
Goal: small total variation, $\mathrm{TV}(P_{A^n,\hat B^n},P^n_{A,B})\le\epsilon$ (25.20).

**Theorem 25.8 (Cuff).** Let $P_{A,B}$ be on a finite space. Alice sees $A^n\sim P_A^n$, sends $W\in[2^{nR}]$, and Bob generates (possibly random) $\hat B^n$. If (25.20) holds for all $\epsilon>0$ and large $n$, then
$$R\ge C(A;B)\triangleq\min_{A\to U\to B}I(A,B;U)\tag{25.21}$$
(Wyner's common information). Conversely, for every $R>C(A;B)$ and $\epsilon>0$ there is $n_0(\epsilon)$ such that for all $n\ge n_0$ a scheme satisfying (25.20) exists. Since $C(A;B)\ge I(A;B)$, this needs more rate than Theorem 25.5, but fools every tester, permutation invariant or not. (p. 503)

*Proof of the lower bound.* Because $P_{A^n,\hat B^n}\approx P^n_{A,B}$ in TV, $I(A_t,\hat B_t;A^{t-1},\hat B^{t-1})\approx I(A_t,B_t;A^{t-1},B^{t-1})=0$ (finite alphabets and bounds relating $H(P)-H(Q)$ to $\mathrm{TV}$, (7.20), Cor. 6.7). Then
$$nR=H(W)\ge I(A^n,\hat B^n;W)\tag{25.22}$$
$$\ge\sum_{t=1}^nI(A_t,\hat B_t;W)-I(A_t,\hat B_t;A^{t-1},\hat B^{t-1})\tag{25.23}$$
$$\approx\sum_{t=1}^nI(A_t,\hat B_t;W)\tag{25.24}$$
$$\gtrsim nC(A;B)\tag{25.25}$$
using $A_t\to W\to\hat B_t$ and continuity of $C(A;B)$ in total variation. (p. 503)

*Proof of achievability.* The problem is equivalent to building $(\hat A^n,W,\hat B^n)$ with (a) $W\in[2^{nR}]$, (b) Markov chain $\hat A^n\leftarrow W\to\hat B^n$ (25.26), (c) $\mathrm{TV}(P_{\hat A^n,\hat B^n},P^n_{A,B})\le\epsilon/2$. Given such a triple, the coupling characterisation of TV (7.20) and $\mathrm{TV}(P_{\hat A^n},P_A^n)\le\epsilon/2$ extend the space to $A^n\to\hat A^n\to W\to\hat B^n$ with $\mathbb P[A^n=\hat A^n]\ge1-\epsilon/2$. Then $\mathrm{TV}(P_{A^n,\hat B^n},P_{\hat A^n,\hat B^n})\le\epsilon/2$ and the triangle inequality gives (25.20). The triple comes from the soft-covering lemma (Corollary 25.10) with $V=(A,B)$ and $W$ uniform on the $x_i$'s there. (pp. 503–504)

*Intuition note.* Fooling every tester in total variation (25.20) is reduced to building $\hat A^n\leftarrow W\to\hat B^n$, so the message $W$ links the two sides (the lower-bound proof also uses $A_t\to W\to\hat B_t$). The rate needed is $C(A;B)=\min_{A\to U\to B}I(A,B;U)$, which the text notes is clearly at least $I(A;B)$ (p. 503).

### 25.4* Approximation of output statistics and soft covering (pp. 504–506)
Recall (Section 7.9): for i.i.d. $X_i\sim P_X$ with empirical distribution $\hat P_n$, $D(P_{Y|X}\circ\hat P_n\|P_Y)\to0$. How large must $n$ be? The section shows $n\approx2^{I(X;Y)}$, assuming $I(X;Y)\gg1$ and concentration of $i(X;Y)$ around $I(X;Y)$ (origin: Wyner [458], strengthened in [212]). It strengthens the $\chi^2$-information bound of Prop. 7.17 ($\lambda=2$). (p. 504)

**Theorem 25.9.** With Rényi mutual information $I_\lambda(X;Y)\triangleq D_\lambda(P_{X,Y}\|P_XP_Y)$, for every $1<\lambda\le2$,
$$\mathbb E[D(P_{Y|X}\circ\hat P_n\|P_Y)]\le\frac1{\lambda-1}\log\big(1+\exp\{(\lambda-1)(I_\lambda(X;Y)-\log n)\}\big).\tag{25.27}$$
*Proof.* $\lambda\mapsto D_\lambda$ is non-decreasing, so it suffices to bound $\mathbb E[D_\lambda]$. By Jensen,
$$\mathbb E[D_\lambda(P_{Y|X}\circ\hat P_n\|P_Y)]=\frac1{\lambda-1}\mathbb E_{X^n}\log\mathbb E_{Y\sim P_Y}\Big[\Big(\tfrac{P_{Y|X}\circ\hat P_n}{P_Y}\Big)^\lambda\Big]\le\frac1{\lambda-1}\log\mathbb E_{X^n}\mathbb E_{Y\sim P_Y}[\cdots]=I_\lambda(X^n;\bar Y),\tag{25.28}$$
with $P_{\bar Y|X^n}=\frac1n\sum_iP_{Y|X=X_i}$. This requires bounding
$$\mathbb E_{(X^n,\bar Y)\sim P_X^n\times P_Y}\Big[\Big(\frac1n\sum_i\frac{P_{Y|X}(Y|X_i)}{P_Y(Y)}\Big)^\lambda\Big].\tag{25.29}$$
Given $Y$ this is a $\lambda$-th moment of a sum of i.i.d. terms. A Rosenthal-type inequality (footnote 5 sketches the proof; the text says it is essentially tight) says that for i.i.d. $B_j\ge0$ and $1\le\lambda\le2$,
$$\mathbb E\Big[\Big(\sum_{i=1}^nB_i\Big)^\lambda\Big]\le n\mathbb E[B^\lambda]+(n\mathbb E[B])^\lambda.\tag{25.30}$$
Here $B_i=P_{Y|X}(Y|X_i)/P_Y(Y)$ has conditional mean 1 given $Y$ (added step), so (25.29) is at most $1+n^{1-\lambda}\mathbb E[(P_{Y|X}/P_Y)^\lambda]$. By the definition of $D_\lambda$ this expectation is $\exp\{(\lambda-1)I_\lambda(X;Y)\}$ (added step). Hence $I_\lambda(X^n;\bar Y)\le\frac1{\lambda-1}\log(1+n^{1-\lambda}\exp\{(\lambda-1)I_\lambda(X;Y)\})$, which with (25.28) gives (25.27). $\square$ (pp. 504–505)

**Remark 25.6.** Hayashi [217] has a bound with $\frac\lambda{\lambda-1}\log(1+\exp\{\frac{\lambda-1}\lambda(K_\lambda(X;Y)-\log n)\})$, $K_\lambda=\inf_{Q_Y}D_\lambda(P_{X,Y}\|P_XQ_Y)$ (Sibson–Csiszár information). It does not have the right convergence rate as $n\to\infty$, at least for $\lambda=1$, compared with Prop. 7.17. Direct TV bounds in [217, 212] rely on the distribution of $i(X;Y)$ and are not discussed (p. 505).

**Corollary 25.10 (soft-covering lemma).** Let $X=(U_1,\dots,U_d)$, $Y=(V_1,\dots,V_d)$ with $(U_i,V_i)$ i.i.d. $P_{U,V}$ and $I_{\lambda_0}(U;V)<\infty$ for some $\lambda_0>1$ (e.g. if $U$ or $V$ has a finite alphabet). Then for any $R>I(U;V)$ there is $\epsilon>0$ such that for all $d\ge1$ there exist $x_1,\dots,x_n$, $n=\lceil\exp\{dR\}\rceil$, with
$$D\Big(\frac1n\sum_{i=1}^nP_{Y|X=x_i}\Big\|P_Y\Big)\le\frac1\epsilon\exp\{-d\epsilon\}.$$
*Proof.* Tensorization gives $I_\lambda(X;Y)=dI_\lambda(U;V)$. For $1<\lambda<\lambda_0$, $\lambda\mapsto I_\lambda(U;V)$ is continuous with limit $I(U;V)$ as $\lambda\to1$, so pick $\lambda$ with $R>I_\lambda(U;V)$ and apply Theorem 25.9. (pp. 505–506)

**Remark 25.7.** "Soft" covering: unlike the covering lemma, which picks one $x_i$, here we mix uniformly over $n$ choices (p. 506).

*Intuition note.* Mixing about $2^{dI}$ randomly chosen inputs already reproduces the output distribution almost exactly. This is the "no-tester-can-tell" version of covering, and it costs $C(A;B)$ rather than $I(A;B)$ once used for simulation.

## Toy example (ours, not from the text)
Binary uniform source, Hamming distortion, $n=4$, target $D=1/4$ (at most one flipped bit). Codewords are i.i.d. uniform in $\{0,1\}^4$, as in Section 25.1.1.
- For any fixed $s^4$, the codewords within distance 1 are $s^4$ itself and its 4 one-bit flips: $1+4=5$ of 16. So $p=\mathbb P[d(s^4,c_1)\le D]=5/16$, independent of $s^4$.
- $P_{\text{failure}}=(1-p)^M=(11/16)^M$.
- $M=2$: $(11/16)^2=121/256\approx0.473$. $M=8$: $11^8/16^8=214358881/4294967296\approx0.0499$. $M=16$: $\approx0.0025$.
- Check against $(1-p)^M\le e^{-pM}$: for $M=8$, $pM=2.5$, $e^{-2.5}\approx0.082\ge0.0499$. ✓.
- Rate: $M=8$ means $\frac1n\log_2M=3/4$ bit/symbol, while $1-h(1/4)\approx1-0.811=0.189$. At $n=4$ the $o(n)$ terms dominate. The asymptotic claim is that $M=2^{n(1-h(D)+\delta)}$ gives $P_{\text{failure}}\to0$ as $n\to\infty$, not that small $n$ is efficient.

## Concepts
- [[rate-distortion-function]] — $R(D)$: operational minimal rate; equals $\phi_S(D)$ under Theorem 25.1's conditions (p. 491)
- [[mutual-information]] — $I(S;\hat S)$ minimised over test channels with $\mathbb E d\le D$ gives $\phi_S(D)$ (p. 490)
- [[kl-divergence]] — used as $D(P_{\hat S|S}\|Q_{\hat S}|P_S)$, the random-coding exponent (p. 493)
- [[typical-set-aep]] — types and joint typicality used for covering; "jointly typical" means $\mathrm{TV}(\hat P,P)=o(1)$ (p. 499)
- [[information-density]] (new) — information density of the joint law $P_{X,Y}$ (Definition 18.1, not restated on these pages); its upper tail ($i>\log\gamma$) enters the random-coding bounds (p. 494)
- [[random-coding-quantizer]] (new) — codewords drawn i.i.d. from $P_Y$, min-distortion encoder (25.5)–(25.6) (pp. 492, 494)
- [[fail-safe-codeword]] (new) — extra fixed codeword $y_0$ capping distortion at $d(X,y_0)$ (p. 494)
- [[excess-distortion-vs-average-distortion]] (new) — $\mathbb P[d>D]$ vs $\mathbb E[d]\le D$ criteria (p. 496–497)
- [[covering-lemma]] (new) — rate $I(A;B)$ suffices to fool one fixed test set $F$ (p. 498)
- [[soft-covering-lemma]] (new) — about $2^{I(X;Y)}$ i.i.d. inputs make the mixed output close to $P_Y$ in KL (p. 505)
- [[wyner-common-information]] (new) — $C(A;B)=\min_{A\to U\to B}I(A,B;U)$; simulation rate for total-variation fooling (p. 503)
- [[renyi-mutual-information]] (new) — $I_\lambda=D_\lambda(P_{XY}\|P_XP_Y)$ (p. 504)
- [[markov-lemma]] (new) — joint typicality of $(X^n,\hat B^n)$ when $X^n$ is generated after $(A^n,\hat B^n)$ (p. 501)
- [[channel-simulation]] (new) — reproducing $P_{A,B}$ from $A^n$ via a rate-limited message (p. 497)

## Canonical instances
- [[bernoulli-half-hamming-rd]] — $P_S=Q_{\hat S}=\mathrm{Ber}(1/2)$: random coding with $M=2^{n(1-h(D)+\delta)}$ achieves $\phi_S(D)=1-h(D)$ (p. 492–493)
- [[cauchy-quadratic-distortion]] — $D_{\max}=\infty$ so fixed-length $R(D)=\infty$, but $R^{(I)}(D)<\infty$ (p. 491)
- [[nonuniform-source-finite-metric-at-D0]] — shows $R(D_0+)<R(D_0)$ while $R^{(I)}$ is continuous (p. 491)
- [[joint-typicality-nontransitive-example]] — binary counterexample (footnote 4) (p. 501)
- [[fixed-composition-codebook-detectable]] — a permutation-invariant tester detects it (p. 502)

## Bridges (candidates)
- [structural-analogy] Random-coding exponent $\min_{Q}\min_P D(P_{\hat S|S}\|Q|P_S)=\phi_S(D)$ ↔ information-theory (channel coding): random-coding argument with information density and unsent codeword — same change-of-measure bound (pp. 494, 498; text cites Chapter 18).
- [structural-analogy] Covering lemma ($R>I(A;B)$) ↔ channel coding: packing needs $R<I$ while covering needs $R>I$ — mirror roles, same quantity.
- [same-math] Soft-covering bound via Rényi mutual information ↔ information-theory: Rényi divergence bounds of Chapter 7 (Prop. 7.17 is the $\lambda=2$ case, p. 504).
- [structural-analogy] Wyner's common information as a minimal "common cause" $U$ ↔ causal modelling: shared latent variable that makes $A$ and $B$ conditionally independent.

## Questions this raises
- Is $H(W)=nR^{(I)}(D)+o(n)$ attainable with variable-length codes when $D_{\max}=\infty$ (e.g. Cauchy source)? The text poses it as open (p. 491).
- Is $R=I(A;B)$ enough to fool every permutation-invariant tester? The authors conjecture yes (p. 502).
- How does the soft-covering threshold $n\approx2^{I(X;Y)}$ change if $i(X;Y)$ does not concentrate around $I(X;Y)$?
- Under what conditions does the Markov-lemma bound (25.19) hold with equality beyond $X\to A\to B$?

## Reading notes
- Page offset: printed = pdf − 25. The unit metadata calls this "ch28"; the printed chapter number is 25 and the sections are 25.1–25.4*.
- Misprints seen in the images: (i) p. 500, the combinatorial paragraph gives both bipartite-graph degrees as $2^{nH(A|B)}$; the two degrees should differ ($2^{nH(B|A)}$ and $2^{nH(A|B)}$). (ii) p. 500, "$=1+o(1)$" should read $1-o(1)$. (iii) p. 500, "apply Theorem to $F$" omits the number (Theorem 25.5 presumably). (iv) p. 500, $\hat Q$ is defined with $\hat A_i$ where $A_i$ appears intended. (v) p. 499, the proof of Theorem 25.5 says "Set $\gamma>M$"; for $e^{-M/\gamma}\to0$, $\gamma$ must be $o(M)$, as in the choice $\log M-\log\gamma=n\delta$ for Theorem 25.1. (vi) p. 502, "$\mathbb E[|\mathrm{TV}(\dots)=o(1)$" has a stray bar. (vii) p. 502, "In the next section we show that if one removes the permutation-invariance constraint…": the text's wording is kept; it refers to Section 25.3.
- The $o_R(1)$ in (25.16) is printed with "+"; it is a signed error term, so the inequality reads "at least, up to $o(1)$".
- The unit has no exercises. Results from other chapters (Theorems 24.3–24.9, 26.1, Prop. 7.17, Cor. 4.2) are cited but not proved here.
