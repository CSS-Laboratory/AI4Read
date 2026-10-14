---
id: polyanskiy-2025-information/ch36-strong-p2
work: polyanskiy-2025-information
unit: "Chapter 33 (printed numbering), part 2/2: §33.8 Undirected information percolation to §33.11 Distributed mean estimation, plus Exercises for Part VI (tail of §33.7 on p. 648 included)"
pages: 648-671
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Strong data processing inequality (part 2/2): undirected percolation, post-SDPI, distributed estimation

## L0 — One line
Contraction coefficients of channels let you bound information flow in graphs (via percolation) and through one-way processing (post-SDPI), which gives converses that are sharp for spiked Wigner recovery and order-optimal in bits for distributed mean estimation.

## L1 — The gist (≤ 120 words)
When noisy edge observations on a graph hide vertex labels, how much can still be learned? Each edge is "open" with probability equal to its KL contraction coefficient. Then the conditional mutual information between vertex sets is at most the percolation function $\mathrm{perc}_u$ (a union bound on connection probabilities) times $\log|\mathcal X|$. For the spiked Wigner model this gives a converse for $\lambda\le1$, matching a spectral algorithm for $\lambda>1$. A second tool, the post-SDPI, bounds $I(U;X)/I(U;Y)$ for $X\to Y\to U$. It is 1 for erasure channels and $(1-2\delta)^2$ for the BSC. It implies that distributed Gaussian mean estimation with risk $\lesssim d/m$ needs about $dm$ bits. The unit ends with 26 exercises.

**Prerequisites:** mutual information and chain rule; spiked Wigner model (a rank-one signal plus symmetric Gaussian noise matrix) and stochastic block model (SBM, a random graph with communities), both introduced in §33.8; weak recovery (doing better than a random guess); KL/χ² divergence; contraction coefficient $\eta_{\rm KL}$ and the less-noisy order (earlier pages, not in this unit); erasure/BSC/AWGN channels; Erdős–Rényi graphs; rate–distortion; minimax risk.

## L2 — Key ideas
- **Undirected information percolation (Thm 33.18).** For an inference problem on an undirected graph, $I(X_{S_1};X_{S_2}\mid Y)\le \mathrm{perc}_u(S_1,S_2)\log|\mathcal X|$. Edges open independently with probability $\eta_{\rm KL}$. This is the analogue of the DAG theorem (pp. 649–650).
- **Proof idea (given only under Assumption 33.1 and for $S_1=\{i\}$).** Replace each edge channel by an erasure channel with the same $\eta_{\rm KL}$, using less-noisy comparison and tensorization. Then only open paths carry information (pp. 650–651).
- **Spiked Wigner converse (Thm 33.20).** For $\lambda\le1$ no estimator achieves weak recovery. For $\lambda<1$ the proof reduces to connectivity in $\mathrm{ER}(n,\lambda'/n)$ with $\lambda'<1$; $\lambda=1$ needs a finer analysis. With the spectral algorithm for $\lambda>1$, $\lambda^*=1$ is the threshold (pp. 651–653).
- **Dense–sparse caveat.** Percolation replaces a dense weak-signal problem by a sparse random-graph one, but the reduction is not generally tight. The SBM bound it gives is weaker than the best known (p. 653).
- **Post-SDPI.** $\eta^{(p)}_{\rm KL}$ controls $I(U;X)/I(U;Y)$ for $X\to Y\to U$. It equals 1 for the erasure channel $\mathrm{BEC}_\tau$ even though that channel is noisy, and $(1-2\delta)^2$ for BSC$_\delta$ (pp. 653–655).
- **BI-AWGN post-SDPI (Thm 33.24).** $\eta^{(p)}_{\rm KL}\le K\epsilon^2/(\pi(1-\pi))$, proved via Marton's $T_1$ transportation inequality and Lipschitzness of the posterior (pp. 655–656).
- **Distributed mean estimation (Thm 33.25).** Risk $\le d\epsilon^2/9$ forces $B\ge c_1d/\epsilon^2$ bits. The coordinate-sign quantizer is therefore order-optimal in bits (pp. 657–658).
- **Interactive protocols.** Published lower bounds for fully interactive protocols contain subtle errors; weaker bounds with log factors are known (pp. 658–659).

## L3 — Walkthrough

### End of §33.7 (p. 648) — tail of a tensorization proof
Statements are on earlier pages. This is the end of a proof that the order relations tensorize (the first chain is the less-noisy form, the second the most-capable form). It uses channels $Y_1,Y_2$ vs $Z_1,Z_2$ with $Y_i$ "worse" than $Z_i$.

First claim, for any $P_{X_1,X_2,U}$ (p. 648):
$$I(U;Y_1,Y_2)=I(U;Y_1)+I(U;Y_2|Y_1)\le I(U;Y_1)+I(U;Z_2|Y_1)=I(U;Y_1,Z_2).$$
The same argument replaces $Y_1$ by $Z_1$, giving $I(U;Y_1,Z_2)\le I(U;Z_1,Z_2)$.

Second claim (p. 648), with $X^2=(X_1,X_2)$:
$$\begin{aligned}I(X^2;Y^2)&=I(X_2;Y^2)+I(X_1;Y^2|X_2)\\&=I(X_2;Y_1)+I(X_2;Y_2|Y_1)+I(X_1;Y_1|X_2)\quad\text{(a)}\\&\le I(X_2;Y_1)+I(X_2;Z_2|Y_1)+I(X_1;Z_1|X_2)\\&=I(X_2;Y_1,Z_2)+I(X_1;Z^2|X_2)\\&=I(X_2;Z_2)+I(X_2;Y_1|Z_2)+I(X_1;Z^2|X_2)\\&\le I(X_2;Z_2)+I(X_2;Z_1|Z_2)+I(X_1;Z^2|X_2)=I(X^2;Z^2).\end{aligned}$$
The equalities are chain rules. Given $X_2$, $Y_2$ (or $Z_2$) is non-informative. Both inequalities apply the most-capable relation to conditional distributions, e.g. $I(X_2;Y_2|Y_1=y)\le I(X_2;Z_2|Y_1=y)$ for every $y$, then average over $y\sim P_{Y_1}$ (p. 648).

*Intuition note.* If each $Z_i$ is better than $Y_i$ in the given order, swapping one noisy observation for its better version does not decrease the relevant information. Do this coordinate by coordinate, and the product of the worse channels stays worse than the product of the better ones.

### §33.8 Undirected information percolation (pp. 648–651)
**Setup.** Undirected graph $G=(\mathcal V,\mathcal E)$. Each vertex has $X_v\in\mathcal X$. Each edge $e=(u,v)$ gives $Y_e\sim P_{Y_e|X_e}$ with $X_e=(X_u,X_v)$. The goal is to infer the $X_v$ from the $Y_e$ (p. 648).

**Examples (pp. 648–649).**
- *33.11 Community detection:* $K_n$, $X_v$ uniform on $[m]$, independent. $Y_{uv}\sim\mathrm{Ber}(a/n)$ if $X_u=X_v$, $\mathrm{Ber}(b/n)$ otherwise.
- *33.12 $\mathbb Z_2$ synchronization:* any graph, $X_v$ uniform on $\{\pm1\}$, $Y_e=\mathrm{BSC}_\delta(X_uX_v)$.
- *33.13 Spiked Wigner:* $Y_{ij}=\sqrt{\lambda/n}\,X_iX_j+W_{ij}$ for $i\le j$. Here $X$ is uniform on $\{\pm1\}^n$ and $W_{ij}=W_{ji}\stackrel{iid}{\sim}\mathcal N(0,1)$. In matrix form $\mathbf Y=\sqrt{\lambda/n}\,\mathbf X\mathbf X^\top+\mathbf W$, a rank-one perturbation of a Wigner matrix, used as a probabilistic model for PCA. It is inference on the complete graph with edge observation $Y_{ij}=\mathrm{BIAWGN}_{\lambda/n}(X_iX_j)$.

**Assumption 33.1 (p. 649).** (i) Each $X_v$ is uniform. (ii) With $B=\mathbf 1\{X_u\ne X_v\}$, the Markov chain $(X_u,X_v)\to B\to Y_e$ holds: each edge observation depends only on whether the endpoints agree.

Consequence: reconstruction is symmetric under relabelling. For $\mathcal X=\{\pm1\}$, $P_{X|Y}(\sigma|b)=P_{X|Y}(-\sigma|b)$. The metric is therefore $\frac1n\big|\sum_iX_i\hat X_i\big|$ (p. 649).

**Percolation model (p. 650).**
- Each edge $e$ is open with probability $\eta_{\rm KL}(P_{Y_e|X_e})$, independently.
- $v\leftrightarrow S$ is the event that an open path joins $v$ to some vertex of $S$.
- $\mathrm{perc}_u(S_1,S_2)\triangleq\sum_{v\in S_1}\mathbb P(v\leftrightarrow S_2)$.

This is not the exact percolation probability. It is a union bound over $S_1$, and hence not symmetric: $\mathrm{perc}_u(S_1,S_2)\ne\mathrm{perc}_u(S_2,S_1)$ in general (p. 650).

**Theorem 33.18 (undirected information percolation, [347]).** For any $S_1,S_2\subset\mathcal V$:
$$I(X_{S_1};X_{S_2}\mid \mathbf Y)\le \mathrm{perc}_u(S_1,S_2)\log|\mathcal X|.$$
This is the analogue of the DAG information percolation theorem (Thm 33.8, p. 649); here the percolation function controls conditional mutual information directly, not a contraction coefficient (pp. 649–650).

**Theorem 33.19 (p. 650).** Let $X_1,\dots,X_n$ be not necessarily independent. If $P_{Y_e|X_e}\le_{LN}P_{Z_e|X_e}$ then for all $S_1,S_2\subset\mathcal V$ and $E\subset\mathcal E$: $I(X_{S_1};Y_E|X_{S_2})\le I(X_{S_1};Z_E|X_{S_2})$.
*Proof.* Tensorization (Prop. 33.17) gives $P_{Y_E|X_{S_1},X_{S_2}}\le_{ln}P_{Z_E|X_{S_1},X_{S_2}}$. For each realization $\sigma$ of $X_{S_2}$:
$$I(X_{S_1};Y_E|X_{S_2}=\sigma)=I(X_{S_1},X_{S_2};Y_E|X_{S_2}=\sigma)\le I(X_{S_1},X_{S_2};Z_E|X_{S_2}=\sigma)=I(X_{S_1};Z_E|X_{S_2}=\sigma).$$
Average over $\sigma$ (p. 650).

**Proof of Thm 33.18 (p. 651),** only under Assumption 33.1 and for $S_1=\{i\}$. The full proof is by induction and does not use the less-noisy idea; see [347].
1. Equation (33.22):
$$I(X_i;X_{S_2}|\mathbf Y_E)=I(X_i;X_{S_2},\mathbf Y_E)=I(X_i;\mathbf Y_E|X_{S_2}).$$
The first equality is justified in the text by $B_E\perp\!\!\!\perp X_i$ (the label it cites is unclear). The second uses $X_i\perp\!\!\!\perp X_{S_2}$ under Assumption 33.1. (Added step: $X_i\to B_E\to\mathbf Y_E$ is a Markov chain and $B_E\perp\!\!\!\perp X_i$ (as the text states), so $I(X_i;\mathbf Y_E)=0$; this gives the first equality via $I(X_i;X_{S_2},\mathbf Y_E)=I(X_i;\mathbf Y_E)+I(X_i;X_{S_2}|\mathbf Y_E)$. By chain rule $I(X_i;X_{S_2},\mathbf Y_E)=I(X_i;X_{S_2})+I(X_i;\mathbf Y_E|X_{S_2})$, and $I(X_i;X_{S_2})=0$.)
2. If $\eta_{\rm KL}(P_{Y_e|X_e})=1-\tau$, then $P_{Y_e|X_e}\le_{LN}P_{Z_e|X_e}=\mathrm{EC}_\tau$ (erasure channel, "previous result"). By tensorization this holds for the product channel, so $I(X_i;\mathbf Y_E|X_{S_2})\le I(X_i;\mathbf Z_E|X_{S_2})$. (The page prints $X_j$ on the right; see Reading notes.)
3. Let $D=\mathbf 1\{i\leftrightarrow S_2\}$, which is determined by $\mathbf Z_E$. By the argument of (33.22):
$$\begin{aligned}I(X_i;\mathbf Z_E|X_{S_2})&=I(X_i;X_{S_2}|\mathbf Z_E)=I(X_i;X_{S_2}|\mathbf Z_E,D)\\&=(1-\mathbb P[i\leftrightarrow S_2])\underbrace{I(X_i;X_{S_2}|\mathbf Z_E,D=0)}_{0}+\mathbb P[i\leftrightarrow S_2]\underbrace{I(X_i;X_{S_2}|\mathbf Z_E,D=1)}_{\le\log|\mathcal X|}\\&\le\mathbb P[i\leftrightarrow S_2]\log|\mathcal X|=\mathrm{perc}_u(i,S_2).\end{aligned}$$

*Intuition note.* Replace every noisy edge by an erasure channel that is at least as informative. Through erased edges nothing passes. So $X_i$ can be correlated with $X_{S_2}$ given the data only if an unerased path connects them.

### §33.9 Application: spiked Wigner model (pp. 651–653)
**Goal.** Weak recovery: an estimator with
$$\tfrac1n\mathbb E\Big[\Big|\sum_{i=1}^nX_i\hat X_i\Big|\Big]\ge\epsilon_0>0\tag{33.23}$$
as $n\to\infty$ (p. 651).

**Known BBP phase transition [29, 326] (p. 652).**
- The eigenvalues of $W/\sqrt n$ follow Wigner's semicircle law on $(-2,2)$.
- The rank-one part $\frac{\sqrt\lambda}{n}XX^T$ has one nonzero eigenvalue $\sqrt\lambda$.
- For $\lambda<1$ the spike is undetectable in the spectrum.
- For $\lambda>1$ the top eigenvalue of $\mathbf Y/\sqrt n$ leaves the semicircle edge, moving to $\lambda+\frac1\lambda>2$ (as printed). The signs of the top eigenvector's coordinates then achieve (33.23).
- Inability to move the spectrum does not by itself exclude other reconstruction methods. This section shows that for $\lambda\le1$ no method works. Together with the spectral algorithm, $\lambda^*=1$ is the critical threshold.

**Theorem 33.20.** If $\lambda\le1$, then for any estimators $\hat X^n(\mathbf Y)$, $\frac1n\mathbb E\big[\big|\sum_{i}X_i\hat X_i\big|\big]\to0$ (33.24).

*Proof (p. 652).*
1. By Cauchy–Schwarz it suffices to show $\sum_{i\ne j}\mathbb E[X_iX_j\hat X_i\hat X_j]=o(n^2)$. (Added step, taking $\hat X_i\in\{\pm1\}$: $(\mathbb E|\sum_iX_i\hat X_i|)^2\le\mathbb E(\sum_iX_i\hat X_i)^2=n+\sum_{i\ne j}\mathbb E[X_iX_j\hat X_i\hat X_j]$.)
2. Relax: estimate each product $X_iX_j$ separately by $\hat T_{i,j}$:
$$\max_{\hat X^n}\sum_{i\ne j}\mathbb E[X_iX_j\hat X_i\hat X_j]\le\sum_{i\ne j}\max_{\hat T_{i,j}}\mathbb E[X_iX_j\hat T_{i,j}].$$
The maximizer is the MAP decoder $\hat T_{i,j}(\mathbf Y)=\arg\max_{\sigma\in\{\pm1\}}\mathbb P[X_iX_j=\sigma|\mathbf Y]$.
3. Since $X_i\sim\mathrm{Ber}(1/2)$, $I(X_i;X_j|\mathbf Y)\to0\iff\max_{\hat T_{i,j}}\mathbb E[X_iX_j\hat T_{i,j}]\to0$. (For example, $I(X_i;X_j|\mathbf Y)=I(X_i,X_j;\mathbf Y)\ge I(X_iX_j;\mathbf Y)$ and apply Fano.) By symmetry it suffices to show $I(X_1;X_2|\mathbf Y)\to0$.
4. By Thm 33.18, $I(X_2;X_1|\mathbf Y)\le\mathrm{perc}_u(\{1\},\{2\})$.
5. The open-edge probability is $\eta_{\rm KL}(\mathrm{BIAWGN}_{\lambda/n})=I_{\chi^2}(X;Y)$ with $X\sim\mathrm{Ber}(1/2)$ (Thm 33.6). A short computation gives $\eta_{\rm KL}(\mathrm{BIAWGN}_{\lambda/n})=\frac\lambda n(1+o(1))$ (p. 653).
6. For $\lambda<1$ overbound $\frac{\lambda+o(1)}n$ by $\frac{\lambda'}n$ with $\lambda'<1$. The percolation graph is then the Erdős–Rényi graph $\mathrm{ER}(n,\lambda'/n)$, and $I(X_2;X_1|\mathbf Y)\le\mathbb P(\text{1 and 2 connected in }\mathrm{ER}(n,\lambda'/n))$.
7. Classical fact [154]: for $\lambda'<1$ the largest component has $O(\log n)$ vertices. So the probability that two specific vertices are connected is $o(1)$, and $I(X_2;X_1|\mathbf Y)\to0$.
8. The case $\lambda=1$ needs finer information on $\eta_{\rm KL}$ and on the giant component of $\mathrm{ER}(n,\frac{1+o(1)}n)$; see [347] (p. 653).

*Intuition note.* With weak signal the open-edge probability is about $\lambda/n$ per pair. Below the critical average degree 1, any two vertices are almost never joined by an open path, so no pairwise correlation can be learned.

**Remark 33.2 (dense–sparse correspondence), p. 653.** The proof replaces the complete graph by a sparse Erdős–Rényi graph. If $\eta_{\rm KL}$ is small, the percolation graph is very sparse and locally tree-like. The author says dense inference with very weak signals resembles sparse inference (broadcasting on trees) with moderate signals, and that the method perhaps partially explains why results in the two worlds parallel each other (e.g. belief propagation vs approximate message passing). Caution: the reduction is not generally tight (spiked Wigner is a lucky exception). For correlated recovery in the SBM with $k$ communities and edge probabilities $a/n$, $b/n$ it gives only the impossibility $(\sqrt a-\sqrt b)^2\le k/2$, weaker than the best known bounds of [203].

### §33.10 Strong data post-processing inequality (pp. 653–656)
**Definition 33.21 (post-SDPI constants).**
$$\eta^{(p)}_{\rm KL}(P_X,P_{Y|X})=\sup_{P_{U|Y}}\Big\{\tfrac{I(U;X)}{I(U;Y)}:X\to Y\to U\Big\},\qquad \eta^{(p)}_{\rm KL}(P_{Y|X})=\sup_{P_X,P_{U|Y}}\Big\{\tfrac{I(U;X)}{I(U;Y)}\Big\}.$$
Equivalent forms, with $P_Y=P_{Y|X}\circ P_X$ and $P_{X|Y}$ the backward kernel of $P_XP_{Y|X}$ (p. 654):
$$\eta^{(p)}_{\rm KL}(P_X,P_{Y|X})=\eta_{\rm KL}(P_Y,P_{X|Y})\tag{33.25}$$
$$\eta^{(p)}_{\rm KL}(P_{Y|X})=\sup_{P_X}\eta_{\rm KL}(P_Y,P_{X|Y})\tag{33.26}$$
From (33.25) and Prop. 33.11, the input-dependent version tensorizes:
$$\eta^{(p)}_{\rm KL}(P_X^{\otimes n},(P_{Y|X})^{\otimes n})=\eta^{(p)}_{\rm KL}(P_X,P_{Y|X}).\tag{33.27}$$
By the DPI, $\eta^{(p)}_{\rm KL}(P_{Y|X})\le1$. Unlike $\eta_{\rm KL}$, it can equal 1 for a noisy channel (p. 654).

**Example 33.14 (erasure channels).** $P_{Y|X}=\mathrm{BEC}_\tau$ (erasure probability $\tau$), $X\sim(\bar\varepsilon,\varepsilon)$ on $\{0,1\}$. Let $U$ be $Y$ with the erasure mapped to 0 (Fig. 33.6). Then $I(Y;U)=H(U)=h(\varepsilon\bar\tau)$ and $I(X;U)=H(U)-H(U|X)=h(\varepsilon\bar\tau)-\varepsilon h(\tau)$. Hence
$$\eta^{(p)}_{\rm KL}(P_{Y|X})\ge\frac{I(X;U)}{I(Y;U)}=1-h(\tau)\frac{\varepsilon}{h(\varepsilon\bar\tau)}.$$
This tends to 1 as $\varepsilon\to0$, so $\eta^{(p)}_{\rm KL}(\mathrm{BEC}_\tau)=1$, even though $Y$ is not a one-to-one function of $X$. The example also refutes the natural conjecture $\eta^{(p)}_{\rm KL}(\mathrm{Unif},\mathrm{BMS})=\eta_{\rm KL}(\mathrm{BMS})$. Taking $\varepsilon=\tfrac12$ gives $\eta^{(p)}_{\rm KL}(\mathrm{Unif},\mathrm{BEC}_\tau)>1-\tau$ for $\tau\to1$ (p. 654).

**Theorem 33.22.** $\eta^{(p)}_{\rm KL}(\mathrm{BSC}_\delta)=(1-2\delta)^2$ (p. 655).

**Lemma 33.23.** If for $X,Y\in\{0,1\}$ the joint law has the form $p_{X,Y}(x,y)=f(x)\big(\tfrac\delta{1-\delta}\big)^{\mathbf 1(x\ne y)}g(y)$ for some $f,g$, then $\eta_{\rm KL}(P_{Y|X})\le(1-2\delta)^2$.
*Proof.* From (33.6), for binary-input channels, $\eta_{\rm KL}(P_{Y|X})\le H^2(P_{Y|X=0},P_{Y|X=1})-\tfrac14H^4(P_{Y|X=0},P_{Y|X=1})$. Let $\phi=g(0)/g(1)$. Then $p_{Y|X=0}=B\big(\tfrac\lambda{\phi+\lambda}\big)$ and $p_{Y|X=1}=B\big(\tfrac1{1+\phi\lambda}\big)$. (The page does not define $\lambda$; it appears to be $\delta/(1-\delta)$.) A simple check shows the maximum over $\phi$ of the bound is attained at $\phi=1$ and equals $(1-2\delta)^2$ (p. 655).

*Proof of Thm 33.22.* The joint law $P_{X,Y}$ of the BSC with input $X$ has the lemma's form with $X,Y$ exchanged. So $\eta_{\rm KL}(P_Y,P_{X|Y})\le(1-2\delta)^2$, hence $\eta^{(p)}_{\rm KL}(P_{Y|X})=\sup_{P_X}\eta_{\rm KL}(P_Y,P_{X|Y})\le(1-2\delta)^2$, with equality if $P_X$ is uniform (p. 655).

**Theorem 33.24 (post-SDPI for BI-AWGN).** Let $0\le\epsilon\le1$, $X\in\{\pm1\}$, $Y=\epsilon X+Z$, $Z\sim\mathcal N(0,1)$. For any $\pi\in(0,1)$ and $P_X=\mathrm{Ber}(\pi)$, for some absolute constant $K$:
$$\eta^{(p)}_{\rm KL}(P_X,P_{Y|X})\le K\frac{\epsilon^2}{\pi(1-\pi)}.$$
*Proof (pp. 655–656), information measures in base $e$.*
1. The posterior is $v(y)\triangleq\mathbb P[X=1|Y=y]=\big(1+\tfrac{1-\pi}\pi e^{-2y\epsilon}\big)^{-1}$.
2. The defining optimization becomes
$$\eta^{(p)}_{\rm KL}(P_X,P_{Y|X})\le\sup_{Q_Y}\frac{d(\mathbb E_{Q_Y}[v(Y)]\,\|\,\pi)}{D(Q_Y\|P_Y)}\tag{33.28}$$
and by (7.34), where $d$ is binary KL divergence (here bounded by the $\chi^2$ form),
$$\eta^{(p)}_{\rm KL}(P_X,P_{Y|X})\le\frac1{\pi(1-\pi)}\sup_{Q_Y}\frac{(\mathbb E_{Q_Y}[v(Y)]-\pi)^2}{D(Q_Y\|P_Y)}.\tag{33.29}$$
3. *$T_1$-transportation inequality (Marton) for $P_Y$:* for every $Q_Y$, for some $c=c(P_Y)$,
$$W_1(Q_Y,P_Y)\le\sqrt{2c\,D(Q_Y\|P_Y)},\tag{33.30}$$
$$W_1(Q_Y,P_Y)=\sup\{\mathbb E_{Q_Y}[f]-\mathbb E_{P_Y}[f]:f\ 1\text{-Lipschitz}\}=\inf\{\mathbb E|A-B|:A\sim Q_Y,B\sim P_Y\}.\tag{33.31}$$
4. One estimate of $c$ ([64, 125]): $c(P_Y)\le\frac2\delta\sup_{k\ge1}\big(G(\delta)/\binom{2k}k\big)^{1/k}$ with $G(\delta)=\mathbb E[e^{\delta(Y-Y')^2}]$, $Y,Y'\stackrel{iid}{\sim}P_Y$. Using $\binom{2k}k\ge\frac{4^k}{\sqrt{\pi(k+1/2)}}$ and $\frac1k\ln(k+\frac12)\le\frac12$:
$$c(P_Y)\le\frac2\delta G(\delta)\frac{\pi\sqrt e}4\le\frac{6G(\delta)}\delta.$$
5. $Y-Y'\stackrel d=B_\epsilon+\sqrt2Z$, with $B_\epsilon\perp\!\!\!\perp Z\sim\mathcal N(0,1)$, $B_\epsilon$ symmetric, $|B_\epsilon|\le2\epsilon$. So for any $\delta<1/4$, $\bar c\triangleq\frac6\delta\sup_{\epsilon\le1}G(\delta)<\infty$, and (33.30) holds with $c=\bar c$ uniformly in $0\le\epsilon\le1$.
6. $|\frac d{dy}v(y)|\le\frac\epsilon2$, so $v$ is $\frac\epsilon2$-Lipschitz, and
$$|\mathbb E_{Q_Y}[v(Y)]-\mathbb E_{P_Y}[v(Y)]|\le\frac\epsilon2\sqrt{2\bar c\,D(Q_Y\|P_Y)}.$$
Square this and plug into (33.29). (Added step: $\mathbb E_{P_Y}[v(Y)]=\pi$, so the bound is $\eta^{(p)}_{\rm KL}\le\frac{\bar c\,\epsilon^2}{2\pi(1-\pi)}$, i.e. $K=\bar c/2$.)

**Remark 33.3 (exact value).** From (33.28), among $Q_Y$ with given $\mathbb E_{Q_Y}[v(Y)]$ one wants the minimizer of $D(Q_Y\|P_Y)$. By Thm 15.11 it is $dQ_Y=e^{bv(y)-\psi_V(b)}dP_Y$ with $\psi_V(b)\triangleq\ln\mathbb E_{P_Y}[e^{bv(Y)}]$. With the convex dual $\psi_V^*$,
$$\eta^{(p)}_{\rm KL}(P_X,P_{Y|X})=\sup_{\lambda\in[0,1]}\frac{d(\lambda\|\pi)}{\psi_V^*(\lambda)}.$$
Numerically, for $\pi=1/2$ the optimum is at $\lambda\to\frac12$. This justifies overbounding $d$ by $\chi^2$, and gives, "surprisingly",
$$\eta^{(p)}_{\rm KL}(\mathrm{Ber}(1/2),P_{Y|X})=4\,\mathbb E_{P_Y}[\tanh^2(\epsilon Y)]=\eta_{\rm KL}(P_{Y|X}),$$
the last equality by Thm 33.6(f) (p. 656).

*Intuition note (post-SDPI).* Post-SDPI asks how much of what $U$ knows about $Y$ is also about $X$. An erasure channel can hide a rare but informative event: $U$ says "Y equals 1" only when $Y$ certifies $X=1$, so the ratio is near 1. (Our gloss.) For BSC$_\delta$ the ratio is at most $(1-2\delta)^2<1$ (for $\delta\in(0,1)$), and for BI-AWGN the bound is of order $\epsilon^2$ for fixed $\pi$.

### §33.11 Application: distributed mean estimation (pp. 657–659)
**Setup (p. 657).** Unknown $\theta\in[-1,1]^d$. Machine $i=1,\dots,m$ sees $Y_i=\theta+\sigma Z_i$, $Z_i\sim\mathcal N(0,I_d)$ independent. It sends message $U_i\in\mathcal U_i$. The total budget is $\sum_i\log_2|\mathcal U_i|\le B$. The remote estimator $\hat\theta$ minimizes $\sup_\theta\mathbb E\|\theta-\hat\theta\|^2$. The minimax risk is
$$R^*(m,d,\sigma^2,B)=\inf_{U_1..U_m,\hat\theta}\sup_\theta\mathbb E\|\theta-\hat\theta\|^2.$$

**Observations (p. 657).**
- Without $\theta\in[-1,1]^d$: take $\theta\sim\mathcal N(0,bI_d)$. By rate–distortion, risk $R$ needs at least $\frac d2\log\frac{bd}R$ bits, which diverges as $b\to\infty$. So restricting the magnitude of $\theta$ is necessary for it to be estimable with finitely many bits communicated.
- No communication constraint: $R^*(m,d,\sigma^2,\infty)=\mathbb E\|\frac\sigma m\sum Z_i\|^2=\frac{d\sigma^2}m$ with $U_i=Y_i$, $\hat\theta=\frac1m\sum U_i$. This matches the non-distributed minimax risk (28.17).
- Crude quantizer: $U_i=\mathrm{sign}(Y_i)$ coordinatewise, so $B=md$. With $V=\frac1m\sum U_i$, each $V_j$ estimates (within $O_p(1/\sqrt m)$) $\Phi(\theta_j/\sigma)$. Since $\Phi'$ is bounded away from 0 on $[-1/\sigma,1/\sigma]$, $\hat\theta_j=\sigma\Phi^{-1}(V_j)$ has MSE $O(1/m)$ (with poor dependence on $\sigma$). Total risk is $O(d/m)$.
- The main result shows this strategy is order-optimal in bits. This simplifies the proofs of [137, 73]. The Gaussian CEO literature implies the same $B\gtrsim dm$ ([156], Thm 3), but uses heavier tools (entropy power inequality).

**Goal and motivation.** Show $R^*\lesssim d/m\Rightarrow B\gtrsim md$. For $d=1$ it is obvious: if $B\le\tau m$, fewer than $\tau m$ machines send anything, so $R^*\ge K/(\tau m)$. For $d\gg1$ it is unclear that each machine must send $\Omega(d)$ bits. Perhaps $\ll d$ one-bit measurements in different orthogonal bases could work; this guess is incorrect, which is why the result is non-trivial (p. 658).

**Theorem 33.25.** There is $c_1>0$ such that if $R^*(m,d,\sigma^2,B)\le\frac{d\epsilon^2}9$, then $B\ge\frac{c_1d}{\epsilon^2}$.
*Proof (p. 658).*
1. Let $X\sim\mathrm{Unif}(\{\pm1\}^d)$, $\theta=\epsilon X$, $\hat X=\mathrm{sign}(\hat\theta)$ coordinatewise. Then
$$\mathbb E[d_H(X,\hat X)]\frac{\epsilon^2}4\le\mathbb E\|\hat\theta-\theta\|^2\le\frac{d\epsilon^2}9,$$
so $\hat X$ is within Hamming distance $\frac49d$ (in expectation).
2. Rate–distortion (Thm 26.1): $I(X;\hat X)\ge cd$ for some $c>0$. By DPI and Thm 6.1,
$$cd\le I(X;\hat X)\le I(X;U_1,\dots,U_m)\le\sum_{j=1}^mI(X;U_j).\tag{33.32}$$
3. $X\to Y_j$ is a memoryless extension of BI-AWGN with SNR $\epsilon$, and each coordinate of $X$ is uniform. Apply Thm 33.24 with $\pi=1/2$ and tensorization (33.27):
$$I(X;U_j)\le4K\epsilon^2I(Y_j;U_j)\le4K\epsilon^2\log|\mathcal U_j|.$$
4. Summing with (33.32):
$$cd\le I(X;\hat X)\le4K\epsilon^2B\log2.\tag{33.33}$$
(Added step: this gives $B\ge\frac{c}{4K\log2}\cdot\frac d{\epsilon^2}$, so $c_1=\frac c{4K\log2}$.)

*Intuition note.* Each machine's message can carry only a fraction about $\epsilon^2$ of what it knows about its own noisy copy $Y_j$. So to gather $\Omega(d)$ bits about $X$ in total, many bits must be sent. Taking $\epsilon^2\sim1/m$ recovers $B\gtrsim dm$.

**Interactivity (pp. 658–659).** The section treats the non-interactive setting: $U_i$ depends only on $Y_i$. Allowing machines to broadcast bits to all others gives interactive protocols. Lower bounds claimed in [137, 73] for that setting contain subtle errors (see [5, 4]). Weaker bounds with logarithmic factors exist. For example [5, Thm 4]: to get risk $\lesssim d\epsilon^2$ one needs $B\gtrsim\frac d{\epsilon^2\log(dm)}$ when $U_i$ may depend on $U_1^{i-1}$ but there are no other interactions.

### Exercises for Part VI (pp. 660–671)
Twenty-six exercises, with no solutions printed.
- **VI.1–VI.17** (pp. 660–668) cover estimation theory: Bayes and Cramér–Rao-type bounds; system identification; linear regression; Hellinger lower bound; Bayesian distribution estimation, add-$\beta$ estimators and coin-flip minimax risk $\frac1{4(1+\sqrt n)^2}$; TV/KL/$\chi^2$ rates; sparse denoising; MLE suboptimality; covariance estimation; $\chi^2$-modulus of continuity.
- **VI.18–VI.26** (pp. 669–671) are linked to Chapter 33: comparison of contraction coefficients, spectral gap and $\chi^2$-contraction of Markov chains, achievability by binary inputs, BMS channel comparison, broadcasting on trees and grids, coloring and Potts channels, spectral independence.

## Toy example (ours, not from the text)
**A. Percolation bound on a path.** Path 1–2–3 with edges $e_{12}$, $e_{23}$. Suppose each edge channel has $\eta_{\rm KL}=0.25$ (assumed), and $|\mathcal X|=2$, logs in base 2 ($\log|\mathcal X|=1$ bit).
- $\mathrm{perc}_u(\{1\},\{3\})=\mathbb P(\text{both edges open})=0.25\cdot0.25=0.0625$. Thm 33.18 gives $I(X_1;X_3|\mathbf Y)\le0.0625$ bit. The trivial bound is 1 bit.
- Asymmetry: $\mathrm{perc}_u(\{1,2\},\{3\})=\mathbb P(1\leftrightarrow3)+\mathbb P(2\leftrightarrow3)=0.0625+0.25=0.3125$. But $\mathrm{perc}_u(\{3\},\{1,2\})=\mathbb P(3\leftrightarrow\{1,2\})=\mathbb P(e_{23}\text{ open})=0.25$. These differ.

**B. Post-SDPI of the erasure channel.** $\tau=0.5$, $\varepsilon=0.1$ in Example 33.14. Then $\varepsilon\bar\tau=0.05$ and $h(0.05)=0.05\log_2\frac1{0.05}+0.95\log_2\frac1{0.95}=0.05(4.3219)+0.95(0.0740)=0.2161+0.0703=0.2864$ bits. With $h(\tau)=h(0.5)=1$:
$$\frac{I(X;U)}{I(Y;U)}=1-1\cdot\frac{0.1}{0.2864}=1-0.3492=0.651.$$
This exceeds $\eta_{\rm KL}(\mathrm{BEC}_{0.5})=1-\tau=0.5$ (the erasure-channel value $1-\tau$, implied by p. 654). Shrinking $\varepsilon$ pushes the ratio toward 1.

## Concepts
- [[strong-data-processing-inequality]] (new) — $I(U;Y)\le\eta\,I(U;X)$ with $\eta<1$ for noisy channels; defined on earlier pages; here used for graphs and post-processing (pp. 650, 653)
- [[contraction-coefficient-eta-kl]] (new) — $\eta_{\rm KL}(P_{Y|X})$, the SDPI constant; the erasure channel $\mathrm{EC}_\tau$ has value $1-\tau$ (implied on pp. 651, 654; $\eta_{\rm KL}$ is used on p. 650)
- [[information-percolation]] (new) — random subgraph with edges open w.p. $\eta_{\rm KL}$; connectivity bounds information (p. 650)
- [[less-noisy-order]] (new) — $P_{Y|X}\le_{LN}P_{Z|X}$; implies $I(U;Y)\le I(U;Z)$ for all $U$, and tensorizes (pp. 648, 650)
- [[post-sdpi]] (new) — $\eta^{(p)}_{\rm KL}$, the SDPI constant for post-processing $X\to Y\to U$; the input-dependent version equals $\eta_{\rm KL}(P_Y,P_{X|Y})$ (pp. 653–654)
- [[t1-transportation-inequality]] (new) — $W_1(Q,P)\le\sqrt{2cD(Q\|P)}$ (Marton), used to bound the post-SDPI (p. 656)
- [[spiked-wigner-model]] (new) — rank-one signal $\sqrt{\lambda/n}XX^\top$ plus Gaussian symmetric noise; weak recovery threshold $\lambda^*=1$ (p. 649, 652)
- [[distributed-estimation-communication-lower-bound]] (new) — minimax risk under a total bit budget $B$ (p. 657)
- [[relative-entropy-kl-divergence]] — the divergence whose contraction defines $\eta_{\rm KL}$ (p. 650)
- [[mutual-information]] — conditional MI bounded by percolation, $I(X_{S_1};X_{S_2}|Y)$ (p. 650)
- [[data-processing-inequality]] — used for $\eta^{(p)}\le1$ and (33.32) (pp. 654, 658)
- [[rate-distortion-function]] — used to force $I(X;\hat X)\ge cd$ (p. 658)
- [[noisy-channel]] — BSC, BEC, BI-AWGN as edge/observation channels (pp. 649, 654)

## Canonical instances
- [[community-detection-sbm]] — complete graph, edge probabilities $a/n$ vs $b/n$ (p. 648–649)
- [[z2-synchronization]] — BSC edge observations of $X_uX_v$ (p. 649)
- [[spiked-wigner-weak-recovery]] — converse for $\lambda\le1$ via $\mathrm{ER}(n,\lambda'/n)$ (pp. 651–653)
- [[bec-post-sdpi-equals-one]] — post-SDPI 1 despite noise (p. 654)
- [[distributed-gaussian-mean-estimation]] — $B\ge c_1d/\epsilon^2$ (pp. 657–658)

## Bridges (candidates)
- [structural-analogy] information percolation on graphs ↔ probability: bond percolation / Erdős–Rényi connectivity — information flow is bounded by connectivity of a random open-edge graph.
- [same-math] post-SDPI $\eta^{(p)}_{\rm KL}(P_X,P_{Y|X})=\eta_{\rm KL}(P_Y,P_{X|Y})$ ↔ information-theory: input-dependent SDPI of the backward channel — identity (33.25).
- [structural-analogy] $T_1$ transportation inequality + Lipschitz posterior ↔ concentration of measure: bounding mean shift under change of measure by $\sqrt{D}$.
- [structural-analogy] spiked-Wigner threshold $\lambda=1$ ↔ random-graph theory: critical average degree 1 for the giant component.
- [metaphor] distributed bit budget ↔ rational inattention: limited channel capacity per agent restricts aggregate inference.

## Questions this raises
- When is the percolation bound tight? The text says it is not in general (SBM) and is tight for spiked Wigner. What distinguishes these cases?
- Can the post-SDPI constant for BI-AWGN be computed exactly for $\pi\ne1/2$? Remark 33.3 reduces it to a one-variable optimization.
- Can $B\gtrsim dm$ be proved without log losses for fully interactive protocols?
- How does the dependence on $\sigma$ enter the constants in Thm 33.25?

## Exercises worth doing
- Ex. VI.19 (p. 669) — spectral gap controls $\chi^2$-contraction of reversible Markov chains; compare $\gamma_*$ for BSC$_\delta$ with $\eta_{\chi^2}$ — difficulty: medium
- Ex. VI.21 (p. 669) — BSC and BEC are extremal for degradation, more-capable and less-noisy orders among BMS channels — difficulty: hard
- Ex. VI.22 (p. 670) — Kesten–Stigum reconstruction for broadcasting on trees via less-noisy comparison and tensorization — difficulty: hard
- Ex. VI.23 (p. 670) — apply the DAG information-percolation theorem to a 2D grid with bond percolation threshold $p_c$ — difficulty: medium
- Ex. VI.25 (p. 671) — compute $\eta_{\rm KL}$ of the Potts channel, $\frac{q\lambda^2}{(q-2)\lambda+2}$ — difficulty: medium
- Ex. VI.7 (p. 662–663) — coin-flip minimax risk via Bayesian Cramér–Rao and a least favorable Beta prior — difficulty: medium

## Reading notes
- This is part 2/2 of the chapter, which is printed as Chapter 33 (the unit id says ch36). It starts at p. 648, in the middle of a proof whose statement is on earlier pages; it is presumably the tensorization of the less-noisy/most-capable orders (Prop. 33.17 is cited on p. 650), at the end of §33.7. It runs through §§33.8–33.11 and the "Exercises for Part VI" (pp. 660–671). The split is at a section boundary of the source. Printed = pdf − 25.
- Text-layer problems on p. 648: superscripts are dropped (e.g. $I(X_2;Y^2)$ vs $I(X^2;Y^2)$) and the text refers to labels (a) and (b) although only (a) is printed in the chain; the chain was copied from the image. The text also writes "I(X_2|Y_1|Z_2)", which should read $I(X_2;Y_1|Z_2)$.
- Probable misprints (p. 651): after (33.22) the text says "first inequality… second inequality" for equalities, and refers to "S.C" without definition. The line "$I(X_i;Y_E|X_{S_2})\le I(X_j;Z_E|X_{S_2})$" has $X_j$, evidently meaning $X_i$.
- p. 652: the top eigenvalue for $\lambda>1$ is printed as moving to $\lambda+1/\lambda>2$ in the page image.
- p. 655: $\lambda$ in the proof of Lemma 33.23 is not defined on the page.
- p. 657: the page says $V_j$ estimates $\Phi(\theta_j/\sigma)$ although $U_i$ takes sign values; I followed the printed text.
- p. 658: the proof applies Thm 33.24 with parameter $\epsilon$; how $\sigma$ enters is not displayed. The closing paragraph speaks of "lower bounds applicable to non-interactive settings" being weaker, which presumably means the interactive setting.
- Exercises are listed, not solved; no solutions are printed.
