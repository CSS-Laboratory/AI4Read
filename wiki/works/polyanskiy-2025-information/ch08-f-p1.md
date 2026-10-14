---
id: polyanskiy-2025-information/ch08-f-p1
work: polyanskiy-2025-information
unit: "Chapter 7 (printed numbering; unit id ch08), part 1/2: f-divergences, §§7.1–7.8"
pages: 115–135
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# f-divergences (part 1/2)

## L0 — One line
KL divergence is one member of the convex-function family of f-divergences. All members obey data processing and joint convexity. Different members suit different tasks (TV and Hellinger for testing), and the joint range of any two members can be found from binary or quaternary distributions.

## L1 — The gist (≤ 120 words)
The chapter generalises KL divergence to $D_f(P\|Q)=\mathbb E_Q[f(dP/dQ)]$ with $f$ convex and $f(1)=0$. It asks which properties hold for every $f$ and how different f-divergences compare. Answer: non-negativity, joint convexity and the data-processing inequality hold for all of them. Total variation (TV) gives the optimal testing error, and squared Hellinger distance $H^2$ tensorizes (it factorises over product distributions); through its sandwich bound with TV it tells when TV of products tends to 0 or 1. The Harremoës–Vajda theorem gives the exact joint range of two f-divergences, which yields sharp comparison inequalities (a sharpened Pinsker, Hellinger vs TV, $\chi^2$ vs TV). This part ends with Gaussian formulas and f-information.

**Prerequisites:** KL divergence and mutual information; Radon–Nikodym derivative (density ratio); convexity and Jensen's inequality; convex hull; basic hypothesis testing.

## L2 — Key ideas
- Every convex $f$ with $f(1)=0$ defines an f-divergence. The definition does not depend on the dominating measure, and adding $c(x-1)$ to $f$ does not change $D_f$ (pp. 115–118).
- Monotonicity, hence data processing, hold for every f-divergence. They give non-negativity, joint convexity and "conditioning increases divergence" (pp. 118–120).
- Finite partitions suffice: $D_f(P\|Q)=\sup_{\mathcal E}D_f(P_{\mathcal E}\|Q_{\mathcal E})$ (p. 121).
- The smallest total error of a binary test is $1-\mathrm{TV}$. TV has a sup form and an inf form over couplings (a coupling is a joint law with the two given marginals) (p. 122).
- $H^2$ tensorizes (for product laws it is a simple function of the one-coordinate values, $2-2\prod(1-\tfrac12H^2)$) and is sandwiched with TV. So $H^2=o(1/n)$ decides whether TV of products vanishes (pp. 123–125).
- Pinsker's inequality ($D\ge(2\log e)\mathrm{TV}^2$) is proved by reduction to Bernoulli distributions, and it is sharp in its constant. The joint range of two f-divergences (the set of all pairs $(D_f,D_g)$ attained by some $P,Q$) gives the best possible inequalities between them (pp. 126–128).
- Harremoës–Vajda: $\mathcal R=\mathrm{co}(\mathcal R_2)=\mathcal R_4$, where $\mathcal R_k$ is the joint range over $k$-point spaces and co is the convex hull. This yields the exact TV–$H^2$ and $\chi^2$–TV ranges (pp. 128–132).
- f-information $I_f$ extends mutual information. TV-information "gets stuck" and fails subadditivity, while symmetric-KL information is additive (pp. 134–135).

## L3 — Walkthrough

### 7.0 Chapter intro (p. 115)
f-divergences (Csiszár) share KL's properties: operational meaning, invariance to bijections, data processing, variational representations, and local behaviour given by $\chi^2$ (nonparametric) or Fisher information (parametric). $\chi^2$, $H^2$, TV matter for estimation, high-dimensional statistics and hypothesis testing respectively. The highlight is the Harremoës–Vajda joint range theorem (p. 115).

### 7.1 Definition and basic properties
**Definition 7.1.** $f:(0,\infty)\to\mathbb R$ convex, $f(1)=0$. If $P\ll Q$,
$$D_f(P\|Q)\triangleq\mathbb E_Q\!\left[f\!\left(\tfrac{dP}{dQ}\right)\right],\tag{7.1}$$
with $f(0)\triangleq f(0+)$. Set $f'(\infty)\triangleq\lim_{x\downarrow0}xf(1/x)$. If $P=p\,d\mu$, $Q=q\,d\mu$:
$$D_f(P\|Q)=\int_{q>0}q f\!\left(\tfrac{p}{q}\right)d\mu+f'(\infty)P[q=0],\tag{7.2}$$
and the last term is $0$ when $P[q=0]=0$, even if $f'(\infty)=\infty$ (pp. 115–116).

**Remark 7.1 (discrete case).** $D_f=\sum_xQ(x)f(P(x)/Q(x))$ with $f(0)=f(0+)$, $0f(0/0)=0$, and $0f(a/0)=af'(\infty)$ for $a>0$ (p. 116).
**Remark 7.2.** $D_f$ does not depend on the choice of $\mu$. The squared $L_2$ distance $\|p-q\|^2_{L^2(d\mu)}$ does (p. 116).

**Examples** (pp. 116–117):
- KL: $f=x\log x$.
- TV: $f=\tfrac12|x-1|$, $\mathrm{TV}=\tfrac12\int|dP-dQ|=1-\int d(P\wedge Q)$ (7.3); a metric.
- $\chi^2$: $f=(x-1)^2$ (or $x^2-1$), $\chi^2=\int dP^2/dQ-1$ (7.4).
- Squared Hellinger: $f=(1-\sqrt x)^2$, $H^2=\int(\sqrt{dP}-\sqrt{dQ})^2=2-2\int\sqrt{dPdQ}$ (7.5). $B=\int\sqrt{dPdQ}$ is the Bhattacharyya coefficient (Hellinger affinity). $H=\sqrt{H^2}$ is a metric, but $P\mapsto H(P,Q)$ is not convex (7.6); example $p\mapsto H(\mathrm{Ber}(p),\mathrm{Ber}(0.1))$.
- Le Cam: $f=\frac{1-x}{2x+2}$, $\mathrm{LC}=\tfrac12\int\frac{(dP-dQ)^2}{dP+dQ}$ (7.7); $\sqrt{\mathrm{LC}}$ is a metric.
- Jensen–Shannon: $f=x\log\frac{2x}{x+1}+\log\frac2{x+1}$, $\mathrm{JS}=D(P\|\tfrac{P+Q}2)+D(Q\|\tfrac{P+Q}2)$ (7.8); $\sqrt{\mathrm{JS}}$ is a metric.

**Remark 7.3.** $D_f(\lambda P+\bar\lambda Q\|Q)$ and $D_f(P\|\lambda P+\bar\lambda Q)$ are f-divergences. Also $D_f(Q\|P)=D_{\tilde f}(P\|Q)$ with $\tilde f(x)=xf(1/x)$ (p. 117).

**Proposition 7.2 (basic properties)** (pp. 117–118):
1. $D_{f_1+f_2}=D_{f_1}+D_{f_2}$.
2. $D_f(P\|P)=0$.
3. $D_f(P\|Q)=0$ for all $P\ne Q$ iff $f(x)=c(x-1)$. For any other $f$, $D_f(P\|Q)=f(0)+f'(\infty)>0$ for $P\perp Q$.
4. For $P_{X,Y}=P_XP_{Y|X}$, $Q_{X,Y}=P_XQ_{Y|X}$: $D_f(P_{X,Y}\|Q_{X,Y})=\int dP_X(x)D_f(P_{Y|X=x}\|Q_{Y|X=x})\triangleq D_f(P_{Y|X}\|Q_{Y|X}|P_X)$ (7.9), the conditional f-divergence.
5. For $P_{X,Y}=P_XP_{Y|X}$, $Q_{X,Y}=Q_XP_{Y|X}$: $D_f(P_{X,Y}\|Q_{X,Y})=D_f(P_X\|Q_X)$ (7.10); in particular $D_f(P_XP_Y\|Q_XP_Y)=D_f(P_X\|Q_X)$ (7.11).
6. $f_1=f+c(x-1)$ gives $D_{f_1}=D_f$. So one may assume $f\ge0$ and, if $f$ is differentiable at 1, $f'(1)=0$.

*Proof ideas.* For $P\perp Q$, $D_f=f(0)+f'(\infty)$ (7.12), which is well defined since $f(0)>-\infty$, $f'(\infty)>-\infty$ by convexity. Since $f(1)=0$, convexity makes $g(x)=f(x)/(x-1)$ non-decreasing. If $f(0)+f'(\infty)=0$ then $g(0+)=g(\infty)$, so $g$ is constant and $f=c(x-1)$. Property 4: take $R_{Y|X}=\frac12P_{Y|X}+\frac12Q_{Y|X}$ and $\mu=P_XR_{Y|X}$ in (7.2). Property 5: take $\mu=P_{X,Y}+Q_{X,Y}$, $\mu_1=P_X+Q_X$, so the density ratios agree. Property 6 follows from 1 and 3, with $c=f'(1)$ (or a subgradient) (p. 118).

### 7.2 Data processing; finite partitions
**Theorem 7.3 (monotonicity).** $D_f(P_{X,Y}\|Q_{X,Y})\ge D_f(P_X\|Q_X)$ (7.13).
*Proof.* If $P_{X,Y}\ll Q_{X,Y}$, Jensen on (7.1) gives $\mathbb E_{Q_X}\mathbb E_{Q_{Y|X}}f(\cdot)\ge\mathbb E_{Q_X}f(\mathbb E_{Q_{Y|X}}[\cdot])=\mathbb E_{Q_X}f(dP_X/dQ_X)$. General case: take $R_X=\frac12(P_X+Q_X)$ and $R_{Y|X}$ as above, with densities $p_1p_2$, $q_1q_2$ w.r.t. $R_X R_{Y|X}$. A supporting line $f(u)\ge f(t)+\mu(u-t)$ gives $f'(\infty)\ge\mu$. (Added step: with $u=\lambda t$, $f(\lambda t)\ge f(t)-\mu\bar\lambda t\ge f(t)-\bar\lambda tf'(\infty)$.) Hence
$$f(\lambda t)+\bar\lambda tf'(\infty)\ge f(t)\quad\forall t\ge0,\ \lambda\in[0,1].\tag{7.14}$$
For fixed $x$ with $q_1(x)>0$: (a) Jensen, (b) (7.14) with $t=p_1/q_1$, $\lambda=P_{Y|X=x}[q_2(Y|x)>0]$ give
$\int_{q_2>0}dR_{Y|X=x}\,q_2f\!\big(\tfrac{p_1p_2}{q_1q_2}\big)+\tfrac{p_1}{q_1}P_{Y|X=x}[q_2=0]f'(\infty)\ge f(p_1/q_1)$. Multiply by $q_1$, integrate over $\{q_1>0\}$, add $f'(\infty)P_X[q_1=0]$; both sides become (7.2) (p. 119).

**Theorem 7.4 (data processing).** If $P_Y,Q_Y$ are the outputs of one channel $P_{Y|X}$ fed by $P_X,Q_X$, then $D_f(P_Y\|Q_Y)\le D_f(P_X\|Q_X)$ (7.15). It follows from (7.13) and (7.10) (p. 120).

**Theorem 7.5.** (a) $D_f\ge0$; if $f$ is strictly convex at 1, then $D_f(P\|Q)=0$ iff $P=Q$. (b) $(P,Q)\mapsto D_f$ is jointly convex. (c) Conditioning increases f-divergence: $D_f(P_Y\|Q_Y)\le D_f(P_{Y|X}\|Q_{Y|X}|P_X)$ when $P_Y=P_{Y|X}\circ P_X$, $Q_Y=Q_{Y|X}\circ P_X$ (p. 120).
*Proof.* (a) Take $X$ unary. For strictness, suppose $D_f=0$ with $P\ne Q$. Data processing with $Y=\mathbf 1\{X\in A\}$ gives $D_f(\mathrm{Ber}(p)\|\mathrm{Ber}(q))=0$ for some event with $p\ne q$. If $0<q<1$ the value would be $qf(p/q)+\bar qf(\bar p/\bar q)$, contradicting strict convexity at 1. If $q=1$, $f'(\infty)=f(p)/(p-1)$, and monotonicity of $g$ makes $f$ affine on $[p,\infty)$, again a contradiction (pp. 120–121). (b) from data processing as in Theorem 5.1. (c) from monotonicity, or Jensen on the jointly convex $D_f$ (p. 121).

**Remark 7.4.** $D_f$ is never strictly convex in the pair. It is linear between pairs with disjoint supports, and also for some common-support pairs: $\mathrm{TV}(\mathrm{Ber}(p),\mathrm{Ber}(q))=|p-q|$ is piecewise linear (p. 121).
**Remark 7.5 (g-divergences).** A "g-divergence" is a functional satisfying positivity, monotonicity, DPI and $D(P\|P)=0$. Any monotone function of an f-divergence is one, and such functions need not be convex (7.6). There exist g-divergences that are not monotone transformations of any f-divergence (the example cited uses $\beta_\alpha$ from (14.3)). On finite alphabets, a sum $\sum_i\varphi(P_i,Q_i)$ is a g-divergence iff it is an f-divergence [325] (p. 121).

**Theorem 7.6.** $D_f(P\|Q)=\sup_{\mathcal E}D_f(P_{\mathcal E}\|Q_{\mathcal E})$ over finite measurable partitions (7.16). The proof is in §7.14*, not in these pages (p. 121).

*Intuition note.* Any processing, even deterministic coarse-graining, can only make two distributions look more alike. This holds for every convex $f$; the proof rests on Jensen's inequality and convexity (a supporting line). By Theorem 7.6, finite alphabets suffice for general questions about f-divergences (the proof is in §7.14*, not in these pages).

### 7.3 TV and Hellinger in hypothesis testing
Setting: one observation $X\sim P$ ($H_0$) or $Q$ ($H_1$). Choose a (possibly randomized) $\phi:\mathcal X\to\{0,1\}$ to minimise the total error $P[\phi(X)=1]+Q[\phi(X)=0]$ (7.17) (p. 122).

**Theorem 7.7.** (a) $\mathrm{TV}(P,Q)=\sup_EP(E)-Q(E)=\tfrac12\sup_{\|f\|_\infty\le1}\mathbb E_P f-\mathbb E_Qf$ (7.18). Hence $\min_\phi\{P[\phi=1]+Q[\phi=0]\}=1-\mathrm{TV}(P,Q)$ (7.19). (b) If the diagonal is measurable, $\mathrm{TV}(P,Q)=\min_{P_{X,Y}}\{P_{X,Y}[X\ne Y]:P_X=P,P_Y=Q\}$ over couplings (7.20) (p. 122).
*Proof.* For $\|f\|_\infty\le1$, $\int f(p-q)d\mu\le\int|p-q|d\mu=2\mathrm{TV}$. With $f=2\cdot\mathbf 1_E-1$ the first sup is also $\le\mathrm{TV}$. Equality: $E=\{p>q\}$. Since $\int(p-q)=0$, $\int_{E^c}(q-p)=\int_E(p-q)$, and the two sum to $2\mathrm{TV}$. For (b), any coupling gives $\mathbb E_Pf-\mathbb E_Qf=\mathbb E[f(X)-f(Y)]\le2P_{X,Y}[X\ne Y]$, so the coupling value is an upper bound. Tightness: with probability $\pi=\int\min(p,q)d\mu$ set $X=Y\sim r=\frac1\pi\min(p,q)$. Otherwise draw $X\sim p_1=\frac{p-\min(p,q)}{1-\pi}$ and $Y\sim q_1=\frac{q-\min(p,q)}{1-\pi}$ independently. Then use the last identity of (7.3) (pp. 122–123).

**Remark 7.6.** Only TV has the form $\sup_{f\in\mathcal F}|\mathbb E_Pf-\mathbb E_Qf|$ ("integral probability metric", here over all bounded functions). The coupling form has no analogue for other f-divergences, except Marton's $d_2$ (Remark 7.15, later). Couplings give the Wasserstein viewpoint: TV is Wasserstein distance for Hamming distance. A chosen coupling gives an upper bound on TV, and a chosen $f$ gives a lower bound (p. 123).

**Many observations.** For i.i.d. data, $H_0:P^{\otimes n}$ vs $H_1:Q^{\otimes n}$, the optimal error is $1-\mathrm{TV}(P^{\otimes n},Q^{\otimes n})$. By data processing, TV is non-decreasing in $n$. For fixed $P\ne Q$, large deviations (Ch. 16) gives $\mathrm{TV}(P^{\otimes n},Q^{\otimes n})=1-\exp(-nC(P,Q)+o(n))$ (7.21), with $C>0$ the Chernoff information. If $P_n,Q_n$ depend on $n$, this cannot be applied directly. TV of products is hard to compute, so Hellinger is used (pp. 123–124).

**Sandwich (7.22).** $\tfrac12H^2\le\mathrm{TV}\le H\sqrt{1-H^2/4}\le1$ (stated here as "we will show shortly"; §7.5.1 says the joint range is exactly described by it). Consequences: $H^2=2\iff\mathrm{TV}=1$; $H^2=0\iff\mathrm{TV}=0$ (best test is random guessing). Hence $H^2(P_n,Q_n)\to0\iff\mathrm{TV}\to0$ (7.23) and $H^2\to2\iff\mathrm{TV}\to1$ (7.24), though speeds may differ (p. 124).

**Theorem 7.8.** $\mathrm{TV}(P_n^{\otimes n},Q_n^{\otimes n})\to0\iff H^2(P_n,Q_n)=o(1/n)$, and $\to1\iff H^2(P_n,Q_n)=\omega(1/n)$.
*Proof.* With $X_i\sim Q_n$ i.i.d.:
$$H^2(P_n^{\otimes n},Q_n^{\otimes n})=2-2\,\mathbb E\sqrt{\prod_i\tfrac{P_n}{Q_n}(X_i)}=2-2\Big(\mathbb E\sqrt{\tfrac{P_n}{Q_n}}\Big)^n=2-2\Big(1-\tfrac12H^2(P_n,Q_n)\Big)^n.\tag{7.25}$$
Combine with (7.23)–(7.24). (Added step: by (7.25), the left side tends to 0 iff $nH^2(P_n,Q_n)\to0$, and to 2 iff $nH^2(P_n,Q_n)\to\infty$.) (p. 124)

*Intuition note.* Hellinger distance turns products into powers of $1-\tfrac12H^2$. So its value for one coordinate tells you whether $n$ coordinates can be told apart. TV of products is typically hard to compute, but the sandwich (7.22) links it to $H^2$.

**Remark 7.7 (tensorization).** $H^2(\prod P_i,\prod Q_i)=2-2\prod_i(1-\tfrac12H^2(P_i,Q_i))$ (7.26). Some other f-divergences tensorize too (§7.12), but $H^2$ has the sandwich bound, so it is the most convenient for asymptotic testability (p. 125).

**Remark 7.8 (Kakutani).** For $P=\prod_{i\ge1}P_i$, $Q=\prod_{i\ge1}Q_i$ with $P_i\ll Q_i$: if $\sum H^2(P_i,Q_i)=\infty$ then $P\perp Q$; if $\sum<\infty$ then $P\ll Q$ and $Q\ll P$. For $P_i=\mathcal N(\mu_i,1)$, $Q_i=\mathcal N(0,1)$, equivalence means $\sum\mu_i^2<\infty$. Argument: by (7.26), $H^2(P,Q)=2-2\prod(1-H^2(P_i,Q_i)/2)$; the product is 0 iff $\sum H^2=\infty$, so $H^2=2$, and by (7.22) $P\perp Q$. If $\sum<\infty$ then $H^2<2$, and Kolmogorov's 0-1 law gives $Q(dP/dQ=0)\in\{0,1\}$ (p. 125; see Reading notes on a misprint).

**Definition 7.9.** $P_n\lhd Q_n$ (contiguous) if $Q_n(A_n)\to0\Rightarrow P_n(A_n)\to0$ for all sequences $A_n$. $P_n\lhd\rhd Q_n$ if both directions hold. $P_n\triangle Q_n$ (asymptotically separated) if $\limsup\mathrm{TV}(P_n,Q_n)=1$ (p. 125). For $P_n=P$, $Q_n=Q$ these reduce to $P\ll Q$ and $P\perp Q$. Mutual contiguity is much weaker than $\mathrm{TV}\to0$. If $P_n\lhd Q_n$ then $\mathrm{TV}=1-\Omega(1)$, so contiguity and separatedness exclude each other (pp. 125–126). Criteria:
- $P_n\triangle Q_n\iff\limsup H^2(P_n,Q_n)=2$ (from (7.24)).
- $P_n\lhd Q_n\iff\lim_{\alpha\to0+}\limsup_nD_\alpha(P_n\|Q_n)=0$ (Rényi divergence; cited from [385]).
- Weaker, common sufficient condition: $\chi^2(P_n\|Q_n)=O(1)$. Indeed $P_n(A_n)=\mathbb E_{Q_n}[\tfrac{dP_n}{dQ_n}\mathbf 1_{A_n}]\le\sqrt{1+\chi^2(P_n\|Q_n)}\sqrt{Q_n(A_n)}$ by Cauchy–Schwarz.
- A sufficient condition for mutual contiguity is $c\le P_n/Q_n\le C$ for constants $c,C$ (p. 126).

### 7.4 Inequalities and joint range
**Theorem 7.10 (Pinsker).** $D(P\|Q)\ge(2\log e)\mathrm{TV}^2(P,Q)$ (7.27).
*Proof.* Use natural logs. For any event $E$, $Y=\mathbf 1\{X\in E\}$ is Bernoulli, and by DPI $D(P\|Q)\ge d(P(E)\|Q(E))$. If Pinsker holds for Bernoulli, then $\sqrt{\tfrac12D(P\|Q)}\ge|P(E)-Q(E)|$; take $\sup_E$ and use Theorem 7.7. Binary case, for $p\ge q$:
$$d(p\|q)=\int_q^p\frac{p-t}{t(1-t)}dt\ge4\int_q^p(p-t)dt=2(p-q)^2,$$
and $\mathrm{TV}(\mathrm{Ber}(p),\mathrm{Ber}(q))=|p-q|$ (pp. 126–127).

**Corollary 7.11 (Tao).** For a Markov chain $Y\to X\to X'$ with $Y\in[-1,1]$: $\mathbb E[|\mathbb E[Y|X]-\mathbb E[Y|X']|^2]\le\frac2{\log e}I(Y;X|X')$ (7.28). The same holds for $Y$ in the unit ball of any normed space. *Proof:* by (7.20) there is a coupling with $P[Y_1\ne Y_2]\le\mathrm{TV}$, so $|\mathbb E Y_1-\mathbb E Y_2|\le2\mathrm{TV}$. Then $|\mathbb E[Y|X=a]-\mathbb E[Y|X'=b]|^2\le4\mathrm{TV}^2\le\frac2{\log e}D(P_{Y|X=a}\|P_{Y|X'=b})$ by Pinsker. Average over $(a,b)\sim P_{X,X'}$, using $D(P_{Y|X}\|P_{Y|X'}|P_{X,X'})=I(Y;X|X')$ (p. 127).

**Sharpness.** The constants in (7.27) and (7.28) cannot be improved. For $P_n=\mathrm{Ber}(\frac12+\frac1n)$, $Q_n=\mathrm{Ber}(\frac12)$, $D/\mathrm{TV}^2\to2\log e$. The right side of (7.27) could still be replaced by a better function of TV. The author then asks what the best such inequality is, and whether $D$ can be bounded above in terms of TV (p. 127); joint ranges are the route to the answers.

**Definition 7.12 (joint range).** $\mathcal R\triangleq\{(D_f(P\|Q),D_g(P\|Q))\}\subset[0,\infty]^2$ over all pairs on all measurable spaces. $\mathcal R_k$ is the same over distributions on $[k]$ (pp. 127–128). The lower boundary of the (TV, KL) range is the optimal Pinsker refinement $D\ge F(\mathrm{TV})$, $F(\epsilon)=\inf_{\mathrm{TV}(P,Q)=\epsilon}D(P\|Q)$. There is no upper boundary, so $D$ cannot be bounded above by TV (Figure 7.1, p. 128).

**Theorem 7.13 (Harremoës–Vajda).** $\mathcal R=\mathrm{co}(\mathcal R_2)=\mathcal R_4$ (co = convex hull) (p. 128).
**Lemma 7.14 (Fenchel–Eggleston–Carathéodory).** If $S\subseteq\mathbb R^d$ and $x\in\mathrm{co}(S)$, then $x\in\mathrm{co}(S')$ for some $S'\subseteq S$ with $d+1$ points. If $S$ has at most $d$ connected components, $d$ points suffice (p. 129).

*Proof of 7.13* (three claims; Claim 3, $\mathcal R=\mathcal R_4$, is only cited from [214]). Claims 1–2 give $\bigcup_k\mathcal R_k=\mathrm{co}(\mathcal R_2)$. By Theorem 7.6, $\mathcal R$ is the closure of $\bigcup_k\mathcal R_k$, which suffices for inequalities (p. 129).
*Skip path: carry forward $\mathcal R=\mathrm{co}(\mathcal R_2)$ (up to closure), so extremal inequalities can be found with binary pairs.*
- *Claim 1, $\mathrm{co}(\mathcal R_2)\subset\mathcal R_4$.* Given pairs $(P_0,Q_0),(P_1,Q_1)$ and $\alpha\in[0,1]$, let $P_B=Q_B=\mathrm{Ber}(\alpha)$, $P_{X|B=i}=P_i$, $Q_{X|B=i}=Q_i$. By (7.9), $D_f(P_{X,B}\|Q_{X,B})=\bar\alpha D_f(P_0\|Q_0)+\alpha D_f(P_1\|Q_1)$, and similarly for $D_g$. So $\mathcal R$ is convex. Next, $\mathcal R_2=\tilde{\mathcal R}_2\cup\{(pf'(\infty),pg'(\infty)):p\in(0,1]\}\cup\{(qf(0),qg(0)):q\in(0,1]\}$, where $\tilde{\mathcal R}_2$ is the image of $(0,1)^2$ under the continuous map $(p,q)\mapsto(D_f,D_g)(\mathrm{Ber}(p)\|\mathrm{Ber}(q))$. Since $(0,0)\in\tilde{\mathcal R}_2$, the set $\mathcal R_2\cap\mathbb R^2$ is connected. By Lemma 7.14 ($d=2$), any point of $\mathrm{co}(\mathcal R_2\cap\mathbb R^2)$ is a combination of two points of it, which is in $\mathcal R_4$ by the mixing construction. Also $\mathrm{co}(\mathcal R_2)\setminus\mathbb R^2\subset\mathcal R_4$ (p. 129).
- *Claim 2, $\mathcal R_k\subset\mathrm{co}(\mathcal R_2)$.* Fix $P,Q$ on $[k]$. Without changing either divergence (perhaps raising $k$ by 1) assume $q_1=0$ and $q_j>0$ for $j>1$. Let $\phi_j=p_j/q_j$ and $\mathcal S=\{\tilde Q:\tilde q_j\ge0,\sum\tilde q_j=1,\tilde q_1=0,\sum_{j\ge2}\tilde q_j\phi_j\le1\}$. Its extreme points $\mathcal S_e$ are of two types: (1) $\tilde q_j=1$ for some $j\ge2$ with $\phi_j\le1$; (2) $\tilde q_{j_1}+\tilde q_{j_2}=1$ with $\tilde q_{j_1}\phi_{j_1}+\tilde q_{j_2}\phi_{j_2}=1$. (A point with $\sum\tilde q_j\phi_j<1$ and more than one atom is not extremal, since only one linear constraint is active; with $=1$, extremality needs one or two atoms.) $\mathcal S$ is closed and convex. By Krein–Milman, and since $\mathcal S_e$ is compact so $\mathrm{co}(\mathcal S_e)$ is closed, $\mathcal S=\mathrm{co}(\mathcal S_e)$. So $Q=\sum_{i=1}^m\alpha_i\tilde Q_i$ with $\tilde Q_i\in\mathcal S_e$ (7.29). Associate $\tilde P$ with $\tilde p_j=\phi_j\tilde q_j$ ($j\ge2$) and $\tilde p_1=1-\sum_{j\ge2}\phi_j\tilde q_j$. The map $\tilde Q\mapsto D_f(\tilde P\|\tilde Q)=\sum_{j\ge2}\tilde q_jf(\phi_j)+f'(\infty)\tilde p_1$ is affine, so $D_f(P\|Q)=\sum_i\alpha_iD_f(\tilde P_i\|\tilde Q_i)$, likewise for $D_g$. For $\tilde Q\in\mathcal S_e$, $\{j:\tilde q_j>0\text{ or }\tilde p_j>0\}$ has at most two elements (for type 2, $\tilde p_{j_1}+\tilde p_{j_2}=1$ forces $\tilde p_1=0$). So each $(\tilde P_i,\tilde Q_i)$ is a binary pair (pp. 129–130).

*Intuition note.* To find the extreme values of one divergence for a given value of another, it is enough to look at pairs on two points, then mix. Mixtures are available because every f-divergence is linear in the mixing weights (7.9).

### 7.5 Computing joint ranges
**7.5.1 $H^2$ vs TV.** $\mathcal R_2=\{(2(1-\sqrt{pq}-\sqrt{\bar p\bar q}),|p-q|)\}$ (non-convex grey region, Fig. 7.2). By Theorem 7.13 the full range is its convex hull, and this is exactly the sandwich (7.22), so (7.22) is not improvable. For $t\in[0,1]$: the upper boundary is attained at $P=\mathrm{Ber}(\frac{1+t}2)$, $Q=\mathrm{Ber}(\frac{1-t}2)$; the lower boundary at $P=(1-t,t,0)$, $Q=(1-t,0,t)$ (p. 131).

**7.5.2 KL vs TV.** No closed form, but the lower boundary is parametric [163], natural log:
$$\mathrm{TV}_t=\tfrac12t\Big(1-\big(\coth t-\tfrac1t\big)^2\Big),\quad D_t=-t^2\mathrm{csch}^2t+t\coth t+\log(t\,\mathrm{csch}\,t),\ t\ge0.\tag{7.30}$$
A weaker bound [427]: $D(P\|Q)\ge\log\frac{1+\mathrm{TV}}{1-\mathrm{TV}}-\frac{2\mathrm{TV}}{1+\mathrm{TV}}\log e$ (7.31). Both are stronger than Pinsker. Consequences: $D\to0\Rightarrow\mathrm{TV}\to0$ (also from Pinsker); $\mathrm{TV}\to1\Rightarrow D\to\infty$, so $D=O(1)$ keeps TV bounded away from one (this needs (7.30) or (7.31), not Pinsker) (pp. 131–132).

**7.5.3 $\chi^2$ vs TV. Proposition 7.15.** $\chi^2(P\|Q)\ge f(\mathrm{TV})\ge4\mathrm{TV}^2$, where $f(t)=4t^2$ for $t\le\frac12$ and $f(t)=\frac t{1-t}$ for $t\ge\frac12$ (7.32). $f$ is a convex increasing bijection $[0,1)\to[0,\infty)$, and for every $s\ge f(t)$ some pair has $\chi^2=s$, $\mathrm{TV}=t$.
*Proof.* For binary pairs, $\mathrm{TV}=|p-q|=t$ and $\chi^2=\frac{t^2}{q(1-q)}$. Given $|p-q|=t$, $q(1-q)$ can be $0$ ($p=t,q=0$), and at most $\frac14$ if $t\le\frac12$ ($p=\frac12-t,q=\frac12$), or at most $t(1-t)$ if $t>\frac12$ ($p=0,q=t$). So $\chi^2\ge f(|p-q|)$. $f$ is convex because its derivative increases, and $f(t)\ge4t^2$ since $t(1-t)\le\frac14$ (p. 132).

### 7.6 Selected inequalities (stated without proof; most are joint ranges, hence tight) (pp. 132–133)
- KL vs TV, "reverse Pinsker" for discrete $Q$ with $Q_{\min}=\min_xQ(x)$: $D\le\log\big(1+\frac2{Q_{\min}}\mathrm{TV}^2\big)\le\frac{2\log e}{Q_{\min}}\mathrm{TV}^2$.
- KL vs $H^2$: $D\ge2\log\frac2{2-H^2}\ge\log e\cdot H^2$ (7.33). The first inequality is the joint range, attained at $P=\mathrm{Ber}(0)$, $Q=\mathrm{Ber}(q)$. For fixed $H^2$ there is no finite upper bound on $D$ (take $P=\mathrm{Ber}(p)$, $Q=\mathrm{Ber}(0)$). A partial reverse (log-Sobolev): $D\le\frac{\log(1/Q_{\min}-1)}{1-2Q_{\min}}\big(1-(1-H^2)^2\big)$.
- KL vs $\chi^2$: $0\le D\le\log(1+\chi^2)\le\log e\cdot\chi^2$ (7.34). No lower bound on KL in terms of $\chi^2$ is possible.
- TV vs $H$: $\mathrm{TV}\le\sqrt{-2\ln(1-H^2/2)}$ [186], besides (7.22).
- Le Cam vs $H^2$: $\frac12H^2\le\mathrm{LC}\le H^2$ (7.35). Le Cam vs JS: $\mathrm{LC}\log e\le\mathrm{JS}\le\mathrm{LC}\cdot2\log2$ (7.36).
- $\chi^2$ vs TV: $\mathrm{TV}\le\frac12\sqrt{\chi^2}$ (7.37); $\mathrm{TV}\le\max\{\frac12,\frac{\chi^2}{1+\chi^2}\}$ (7.38), useful for bounding TV away from one.
- JS vs TV: $2d\big(\frac{1-\mathrm{TV}}2\|\frac12\big)\le\mathrm{JS}\le\mathrm{TV}\cdot2\log2$ (7.39). The lower bound follows from Fano's inequality. For the upper bound, with $|p-q|=\tau$ the maximum of $d(p\|\frac{p+q}2)$ is at $p=0,q=\tau$. The binary range is $\tau\mapsto d(\tau\|\tau/2)+d(1-\tau\|1-\tau/2)$, which is convex, so its concave envelope is the chord from $\tau=0$ to $\tau=1$.

### 7.7 Divergences between Gaussians (p. 134)
- TV: $\mathrm{TV}(\mathcal N(0,\sigma^2),\mathcal N(\mu,\sigma^2))=2\Phi(\frac{|\mu|}{2\sigma})-1=\int_{-|\mu|/2\sigma}^{|\mu|/2\sigma}\varphi=\frac{|\mu|}{\sqrt{2\pi}\sigma}+O(\mu^2)$, $\mu\to0$ (7.40).
- $H^2=2-2e^{-\mu^2/8\sigma^2}=\frac{\mu^2}{4\sigma^2}+O(\mu^3)$ (7.41). General: $H^2(\mathcal N(\mu_1,\Sigma_1)\|\mathcal N(\mu_2,\Sigma_2))=2-2\frac{|\Sigma_1|^{1/4}|\Sigma_2|^{1/4}}{|\bar\Sigma|^{1/2}}\exp\{-\frac18(\mu_1-\mu_2)'\bar\Sigma^{-1}(\mu_1-\mu_2)\}$, $\bar\Sigma=\frac{\Sigma_1+\Sigma_2}2$.
- KL: $D=\frac12\log\frac{\sigma_2^2}{\sigma_1^2}+\frac12\big(\frac{(\mu_1-\mu_2)^2}{\sigma_2^2}+\frac{\sigma_1^2}{\sigma_2^2}-1\big)\log e$ (7.42).
- $\chi^2(\mathcal N(\mu,\sigma^2)\|\mathcal N(0,\sigma^2))=e^{\mu^2/\sigma^2}-1=\frac{\mu^2}{\sigma^2}+O(\mu^3)$ (7.43). $\chi^2(\mathcal N(\mu,\sigma^2)\|\mathcal N(0,1))=\frac{e^{\mu^2/(2-\sigma^2)}}{\sigma\sqrt{2-\sigma^2}}-1$ for $\sigma^2<2$, and $\infty$ for $\sigma^2\ge2$ (7.44).
- Gaussian mixtures [225]: $\chi^2(P*\mathcal N(0,\Sigma)\|\mathcal N(0,\Sigma))=\mathbb E[e^{\langle\Sigma^{-1}X,X'\rangle}]-1$, $X\perp X'\sim P$ (7.45).

### 7.8 f-information (pp. 134–135, part)
$I_f(X;Y)\triangleq D_f(P_{X,Y}\|P_XP_Y)$ (7.46).
**Theorem 7.16.** For $U\to X\to Y$, $I_f(U;Y)\le I_f(U;X)$. *Proof:* $I_f(U;X)=D_f(P_{U,X}\|P_UP_X)\ge D_f(P_{U,Y}\|P_UP_Y)$ by Theorem 7.4 applied to $(U,X)\mapsto(U,Y)$ (p. 134).
For ordinary MI, $X\perp\!\!\!\perp Y\iff I=0$, and for $X\to Y\to Z$, $I(X;Y)=I(X;Z)\iff X\to Z\to Y$. For $I_f$ these may or may not hold, depending on strict convexity of $f$ (Ex. I.40) (p. 135).
**Subadditivity** (7.47): if $A,B$ are conditionally independent given $X$, $I(X;A,B)\le I(X;A)+I(X;B)$. For other f-informations:
1. $I_{\chi^2}(X;Y)=\chi^2(P_{X,Y}\|P_XP_Y)$ (7.48) is not generally subadditive. Special cases where it is: one of $I_{\chi^2}(X;A)$, $I_{\chi^2}(X;B)$ is small, or $X\sim\mathrm{Ber}(1/2)$ and both channels are BMS.
2. $I_{\mathrm{TV}}$ is not subadditive and "gets stuck": for $X\sim\mathrm{Ber}(1/2)$ and $A,B$ two independent $\mathrm{BSC}_\delta$ observations of $X$, $I_{\mathrm{TV}}(X;A,B)=I_{\mathrm{TV}}(X;A)=I_{\mathrm{TV}}(X;B)$ (Ex. I.35). A second observation adds nothing. The author calls this the main reason for the herding effect in economics.
3. Symmetric KL information $I_{\mathrm{SKL}}(X;Y)=D(P_{X,Y}\|P_XP_Y)+D(P_XP_Y\|P_{X,Y})$ (7.49), from $D_{\mathrm{SKL}}(P,Q)=D(P\|Q)+D(Q\|P)$ (Jeffreys) (7.50), is additive: $I_{\mathrm{SKL}}(X;A,B)=I_{\mathrm{SKL}}(X;A)+I_{\mathrm{SKL}}(X;B)$ (7.51). Discrete proof: first, $I_{\mathrm{SKL}}(X;Y)=\sum_{x,x'}P_X(x)P_X(x')D(P_{Y|X=x}\|P_{Y|X=x'})$ (7.52). Then (7.51) follows from additivity of KL for conditionally independent $A,B$. The proof of (7.52) starts from the identity $\sum_{x,x'}P_X(x)P_X(x')[D(P_Y\|P_{Y|X=x'})-D(P_Y\|P_{Y|X=x})]=0$ and continues past p. 135 (outside this unit).

*Intuition note.* Whether "more independent looks give more information" depends on which divergence measures information. For TV, a second look can be worth nothing. For symmetric KL, the gains add exactly.

## Toy example (ours)
Let $P=(0.5,0.3,0.2)$, $Q=(0.25,0.25,0.5)$ on $\{a,b,c\}$.
- $\mathrm{TV}=\tfrac12(0.25+0.05+0.30)=0.30$.
- $\chi^2=\frac{0.25^2}{0.25}+\frac{0.05^2}{0.25}+\frac{0.30^2}{0.5}=0.25+0.01+0.18=0.44$.
- $\sum\sqrt{PQ}=\sqrt{.125}+\sqrt{.075}+\sqrt{.1}=0.35355+0.27386+0.31623=0.94364$, so $H^2=2-1.88728=0.11272$.
- Checks: $\frac12H^2=0.0564\le0.30$; $H\sqrt{1-H^2/4}=0.33573\times0.98581=0.3310\ge0.30$, so (7.22) holds. $f(0.3)=4(0.09)=0.36\le0.44$, so (7.32) holds.
- Data processing: merge $b,c$ (a deterministic channel). $P'=(0.5,0.5)$, $Q'=(0.25,0.75)$. Then $\mathrm{TV}'=0.25\le0.30$; $\chi'^2=0.25+\frac{0.25^2}{0.75}=0.3333\le0.44$; $\sum\sqrt{P'Q'}=0.35355+0.61237=0.96593$, $H'^2=0.0682\le0.1127$. All three shrink, as (7.15) says.
- Tensorization (7.25): for $n=2$, $H^2(P^{\otimes2},Q^{\otimes2})=2-2(1-0.05636)^2=2-2(0.89046)\approx0.2191$.

## Concepts
- [[f-divergence]] — $D_f(P\|Q)=\mathbb E_Q f(dP/dQ)$, $f$ convex, $f(1)=0$; independent of dominating measure (p. 115)
- [[relative-entropy-kl-divergence]] — the f-divergence with $f=x\log x$ (p. 116)
- [[data-processing-inequality]] — passing both laws through one channel cannot increase any $D_f$ (p. 120)
- [[total-variation]] (new) — $f=\frac12|x-1|$; equals $\sup_EP(E)-Q(E)$ and the minimal coupling mismatch probability (p. 122)
- [[hellinger-distance]] (new) — $H^2=2-2\int\sqrt{dPdQ}$; tensorizes via the affinity product (pp. 117, 124)
- [[chi-square-divergence]] (new) — $\chi^2=\int dP^2/dQ-1$; $O(1)$ implies contiguity (pp. 116, 126)
- [[coupling]] (new) — joint law with given marginals; TV is the minimal $P[X\ne Y]$ (p. 122)
- [[contiguity]] (new) — $Q_n(A_n)\to0\Rightarrow P_n(A_n)\to0$; asymptotic version of $P\ll Q$ (p. 125)
- [[joint-range]] (new) — set of attainable $(D_f,D_g)$ pairs; $\mathcal R=\mathrm{co}(\mathcal R_2)=\mathcal R_4$ (pp. 127–128)
- [[pinsker-inequality]] (new) — $D\ge(2\log e)\mathrm{TV}^2$ (p. 126)
- [[f-information]] (new) — $I_f(X;Y)=D_f(P_{X,Y}\|P_XP_Y)$ (p. 134)
- [[mutual-information]] — ordinary case $f=x\log x$ of $I_f$; has subadditivity (7.47) (p. 135)

## Canonical instances
- [[pinsker-sharpness-example]] — $\mathrm{Ber}(\frac12+\frac1n)$ vs $\mathrm{Ber}(\frac12)$ gives ratio $\to2\log e$ (p. 127)
- [[kakutani-gaussian-product]] — infinite Gaussian products equivalent iff $\sum\mu_i^2<\infty$ (p. 125)
- [[gaussian-shift-divergences]] — closed forms (7.40)–(7.45) for Gaussian pairs and Gaussian mixtures (p. 134)
- [[bsc-tv-information-stuck]] — two BSC looks give no extra TV-information (p. 135)
- [[hellinger-tv-extremal-pairs]] — pairs attaining both sides of (7.22) (p. 131)

## Bridges (candidates)
- [same-math] TV coupling form (7.20) ↔ optimal transport: Wasserstein distance with Hamming cost.
- [same-math] $1-\mathrm{TV}$ as minimal total testing error (7.19) ↔ statistics: Bayes-optimal binary decision with equal priors, up to the sum-of-errors convention.
- [structural-analogy] Joint range via extreme points and Carathéodory ↔ convex geometry/linear programming: extremal values of linear functionals occur at atoms.
- [metaphor] TV-information "getting stuck" ↔ economics: herding, where a new signal does not change the decision.

## Questions this raises
- What are the variational (sup) representations of general $D_f$ promised in §7.13, and how do they extend the TV form?
- Which f-divergences tensorize (§7.12), and is the $H^2$ sandwich unique in giving sharp asymptotic testability?
- How do $\chi^2$ and Fisher information describe the local behaviour of $D_f$ (announced in the intro)?
- Does additivity of $I_{\mathrm{SKL}}$ have an interpretation beyond the algebraic identity (7.52)?

## Reading notes
- Printed pages 115–135 = pdf 140–160 (printed = pdf − 25). The printed chapter number is 7, although the unit id says ch08.
- Part 1 starts at the chapter opening (p. 115) and ends on p. 135, in the middle of the proof of (7.52). Later sections are not in this unit; the text refers to §7.12, §7.13 and §7.14* (the proof of Theorem 7.6 is in §7.14*).
- Misprint, p. 125 (image): in Remark 7.8 the text says that $H^2(P,Q)=2$ is equivalent, by (7.22), to "$\mathrm{TV}(P,Q)=0$". It should read $\mathrm{TV}(P,Q)=1$, which is what gives $P\perp Q$ and agrees with p. 124.
- Proof of Theorem 7.5(a), case a (p. 121): the value is written "$=f(1)$". The reasoning is that strict convexity at 1 would make it strictly larger than $f(1)=0$. I summarised this in L3 without a quote.
- Remark 7.5 (p. 121): the page says such functions 'do not need to be monotone'; L3 writes 'need not be convex' (my reading, since they are monotone by construction).
- Text-layer equations on pp. 117, 121, 134 were garbled; I checked them against the page images. Cross-references to Exercises I.35, I.40 and to the book's later chapters are as printed; I did not follow them.
