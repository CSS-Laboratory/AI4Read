---
id: polyanskiy-2025-information/ch05-variational
work: polyanskiy-2025-information
unit: "Chapter 4 (printed numbering; unit id ch05) — Variational characterizations and continuity of information measures"
pages: 66-90
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Variational characterizations and continuity of information measures

## L0 — One line
Writing divergence and mutual information as a sup or inf over simple objects (partitions, functions, reference measures) gives convexity, lower semicontinuity and easy bounds, and these give the "Gibbs principle", continuity theorems and PAC-Bayes generalization bounds.

## L1 — The gist (≤ 120 words)
How can KL divergence D(P‖Q) and mutual information I(X;Y) be computed, bounded and shown continuous when alphabets are infinite or the distributions are intractable? The chapter writes them as suprema or infima: over partitions (Gelfand–Yaglom–Perez), over functions (Donsker–Varadhan, Gibbs), and for I over a reference output measure Q_Y (the "golden formula"). These forms give upper and lower bounds by choosing a candidate. They also give lower semicontinuity, limits along growing σ-algebras, and applications: mean-field inference, the evidence lower bound (ELBO), variational autoencoders, and PAC-Bayes bounds on norms and on generalization error.

**Prerequisites:** KL divergence and its chain rule and data-processing inequality; mutual information; Radon–Nikodym density; Jensen and Markov inequalities; basic convexity and measure-theoretic convergence.

## L2 — Key ideas
- **Golden formula** $D(P_{Y|X}\|Q_Y|P_X)=I(X;Y)+D(P_Y\|Q_Y)$. So $I$ is the minimum over $Q_Y$, attained at $Q_Y=P_Y$, which lets us upper-bound $I$ by choosing any $Q_Y$ (p. 67–68).
- $I(X;Y)$ is also the minimum distance to product measures, and $I(X;Z|Y)$ is the minimum distance to Markov chains $X\to Y\to Z$. A sup form over kernels $Q_{X|Y}$ gives lower bounds (p. 69–70).
- **Gelfand–Yaglom–Perez:** D is the supremum of finite-partition divergences. General identities can be proved for discrete variables and then passed to the limit (p. 70–71).
- **Donsker–Varadhan:** $D(P\|Q)=\sup_f E_P[f]-\log E_Q e^f$. It gives change-of-measure bounds and lower semicontinuity (p. 72–73, 78).
- **Gibbs variational principle** is the dual: $\log E_Q e^f=\sup_P E_P f-D(P\|Q)$, with the tilted $Q^f$ as maximizer. It underlies mean-field inference, the ELBO, EM and VAEs (p. 74–77).
- Divergence is not continuous in general, but it is lower semicontinuous (if $P_n\to P$ and $Q_n\to Q$ weakly, then $D(P\|Q)\le\liminf D(P_n\|Q_n)$). It is continuous along increasing σ-algebras, and along decreasing ones if D is finite at the start (p. 78–80).
- Mutual information is continuous on finite alphabets and under the convex-hull condition of Prop. 4.13(c), only lower semicontinuous in general, and passes to limits in processes. The tail-σ-algebra limit needs finiteness (p. 81–83).
- **PAC-Bayes:** one inequality, with probability ≥ 1−δ, controls $E_\rho[f_\theta-\psi(\theta)]$ for all ρ simultaneously. It gives Gaussian-norm bounds and McAllester's generalization bound, and links overfitting to $I(\hat\theta;X^n)$ and to compressibility (p. 84–90).

## L3 — Walkthrough

### Introduction (p. 66–67)
A variational form $F=\sup_\lambda f_\lambda$ or $\inf_\mu g_\mu$ gives: convexity (sup of convex is convex), lower semicontinuity (sup of lsc is lsc), and bounds (evaluate any one $f_\lambda$) (p. 66). D has two sup forms (partitions, functions). I has two more: an inf over "centroid" measures $Q_Y$ and a sup over Markov kernels (p. 66). Three kinds of continuity are announced: in discretization (Thm 4.5), under change of distribution (§4.5; "delicate"), and in the σ-algebra (§4.6) (p. 66).

Motivating example: $\theta\sim\mathrm{Unif}(0,1)$, $X_i\overset{iid}{\sim}\mathrm{Ber}(\theta)$, observed until τ = first occurrence of 0101. Set $Z_j=X_j$ for $j\le\tau$ and $Z_j=?$ otherwise. The chapter will show
$$I(\theta;Z^\infty)=\lim_{n\to\infty} I(\theta;Z^n)=\sum_{n=1}^\infty I(\theta;Z_n|Z^{n-1})\tag{4.1}$$
(p. 67). So even this simple question needs safe handling of infinite-dimensional vectors.

### 4.1 Geometric interpretation of mutual information (p. 67–70)
For discrete X, $I(X;Y)=D(P_{Y|X}\|P_Y|P_X)=\sum_x D(P_{Y|X=x}\|P_Y)P_X(x)$: a weighted "distance" from conditionals to the marginal, with $P_Y$ acting as a centre of gravity (p. 67).

**Theorem 4.1 (Golden formula).** For any $Q_Y$,
$$D(P_{Y|X}\|Q_Y|P_X)=I(X;Y)+D(P_Y\|Q_Y).\tag{4.2}$$
If $D(P_Y\|Q_Y)<\infty$ then
$$I(X;Y)=D(P_{Y|X}\|Q_Y|P_X)-D(P_Y\|Q_Y).\tag{4.3}$$
It presents $I$ as a difference of relative entropies, Shannon-style, while keeping Fano-style applicability to continuous spaces (p. 67).

*Proof idea (discrete, ignoring division by zero):* $I=E\log\frac{P_{Y|X}Q_Y}{P_YQ_Y}$ and $\log\frac{P_{Y|X}Q_Y}{P_YQ_Y}=\log\frac{P_{Y|X}}{Q_Y}-\log\frac{P_Y}{Q_Y}$ (p. 67–68). *Rigorous steps (p. 68):*
1. By Thm 2.16(e), $D(P_{Y|X}\|Q_Y|P_X)\ge D(P_Y\|Q_Y)$. So if $D(P_Y\|Q_Y)=\infty$, both sides of (4.2) are infinite. Assume it is finite, hence $P_Y\ll Q_Y$.
2. By the chain rule (2.24), the claim becomes $D(P_{X,Y}\|P_XQ_Y)=D(P_{X,Y}\|P_XP_Y)+D(P_Y\|Q_Y)$. If both left terms are infinite this is clear. Otherwise $P_{X,Y}\ll P_XQ_Y$.
3. Let $\lambda=dP_Y/dQ_Y$. Then $E_{P_Y}[\log\lambda(Y)]=E_{P_{X,Y}}\big[\mathrm{Log}\frac{\lambda(Y)}{1}\big]$ (4.4). The same λ is the density $d(P_XP_Y)/d(P_XQ_Y)$. By (2.11) with $\mu=P_XQ_Y$ the right side of (4.4) equals $D(P_{X,Y}\|P_XQ_Y)-D(P_{X,Y}\|P_XP_Y)$, and by (2.13) the left side equals $D(P_Y\|Q_Y)$. $\square$

*Intuition note.* Measuring each conditional against a wrong centre $Q_Y$ costs exactly the true information plus the "price of the wrong centre" $D(P_Y\|Q_Y)$. The price is non-negative, so the true centre is cheapest.

**Corollary 4.2 (centre of gravity).** For any $Q_Y$, $I(X;Y)\le D(P_{Y|X}\|Q_Y|P_X)$, so
$$I(X;Y)=\min_{Q_Y}D(P_{Y|X}\|Q_Y|P_X).\tag{4.5}$$
If $I(X;Y)<\infty$ the unique minimizer is $Q_Y=P_Y$ (p. 68).

**Remark 4.1.** (4.5) upper-bounds $I$ when each $P_{Y|X=x}$ is simple but the mixture $P_Y$ is hard. Example: AWGN channel $Y=X+Z$, $\mathrm{Var}(X)=\sigma^2$, $Z\sim N(0,1)$. With the best Gaussian Q, $I(X;Y)\le\inf_{\mu\in\mathbb R,s\ge0}E[D(N(X,1)\|N(\mu,s))]=\tfrac12\log(1+\sigma^2)$, tight when X is Gaussian (p. 68).

**Theorem 4.3.** $I(X;Y)=\min_{Q_X,Q_Y}D(P_{X,Y}\|Q_XQ_Y)$, with unique minimizer $(P_X,P_Y)$. *Proof:* by (2.24), $D(P_{X,Y}\|Q_XQ_Y)=D(P_{Y|X}\|Q_Y|P_X)+D(P_X\|Q_X)\ge I(X;Y)$ (p. 69).

**Conditional MI (4.6).** $I(X;Z|Y)=\min_{Q_{X,Y,Z}:X\to Y\to Z}D(P_{X,Y,Z}\|Q_{X,Y,Z})$, over $Q=Q_XQ_{Y|X}Q_{Z|Y}$. Repeating the argument of (4.2):
$$D(P_{XYZ}\|Q_XQ_{Y|X}Q_{Z|Y}) = D(P_{XYZ}\|P_XP_{Y|X}P_{Z|Y})+D(P_X\|Q_X)+D(P_{Y|X}\|Q_{Y|X}|P_X)+D(P_{Z|Y}\|Q_{Z|Y}|P_Y)$$
$$= D(P_{XYZ}\|P_YP_{X|Y}P_{Z|Y})+\dots = \underbrace{D(P_{XZ|Y}\|P_{X|Y}P_{Z|Y}|P_Y)}_{I(X;Z|Y)}+\dots\ \ge I(X;Z|Y).$$
The optimal Q is $P_YP_{X|Y}P_{Z|Y}$. Reading: removing the edge X→Z from the triangle graph forces a Markov chain, so $I(X;Z|Y)$ is the information flowing through that edge (p. 69).

**Theorem 4.4 (sup over kernels).** For any Markov kernel $Q_{X|Y}$ with $Q_{X|Y=y}\ll P_X$ for $P_Y$-a.e. y, $I(X;Y)\ge E_{P_{X,Y}}\big[\log\frac{dQ_{X|Y}}{dP_X}\big]$. If $I(X;Y)<\infty$,
$$I(X;Y)=\sup_{Q_{X|Y}}E_{P_{X,Y}}\Big[\log\frac{dQ_{X|Y}}{dP_X}\Big].\tag{4.7}$$
*Proof (p. 70):* if $I=\infty$ there is nothing to prove. Otherwise $P_{X,Y}\ll P_XP_Y$, and by Lemma 3.3 $P_{X|Y=y}\ll P_X$ for a.e. y. For such y, (2.11) with $\mu=P_X$ gives $E_{P_{X|Y=y}}[\log\frac{dQ_{X|Y=y}}{dP_X}]=D(P_{X|Y=y}\|P_X)-D(P_{X|Y=y}\|Q_{X|Y=y})$. Averaging over y:
$$E_{P_{X,Y}}\Big[\log\tfrac{dQ_{X|Y}}{dP_X}\Big]=I(X;Y)-D(P_{X|Y}\|Q_{X|Y}|P_Y)\le I(X;Y).\tag{4.8}$$
Equality holds at $Q_{X|Y}=P_{X|Y}$.

Remark 4.2: (4.7) lower-bounds $I$ by choosing a computable approximation to a complicated posterior $P_{X|Y}$ (p. 70).

*Intuition note.* Two one-sided tools: guess a centre $Q_Y$ and you get an upper bound on I; guess a posterior $Q_{X|Y}$ and you get a lower bound. The gap in each case is a divergence from the truth.

### 4.2 Gelfand–Yaglom–Perez (p. 70–71)
**Theorem 4.5.** For probability measures P, Q on $(\mathcal X,\mathcal F)$,
$$D(P\|Q)=\sup_{\{E_1,\dots,E_n\}}\sum_{i=1}^nP[E_i]\log\frac{P[E_i]}{Q[E_i]},\tag{4.9}$$
over finite $\mathcal F$-measurable partitions, with $0\log\frac10=0$ and $\log\frac10=\infty$ (p. 70). So divergence on general alphabets is defined through finite alphabets, and finer quantization approaches it. Remark 4.3: general identities can be proved for discrete variables and then passed to the limit. For $I(X;Y)=D(P_{X,Y}\|P_XP_Y)$, partitions of $\mathcal X$ and $\mathcal Y$ can be chosen separately, see (4.29) (p. 71).

*Proof (p. 71).* "≥": for a partition, let $f(x)$ be the index of the cell containing x and $Y=f(X)$. The data-processing inequality gives $D(P\|Q)\ge D(P_Y\|Q_Y)=\sum_iP(E_i)\log\frac{P(E_i)}{Q(E_i)}$ (4.10).
"≤": if $P\not\ll Q$, pick B with $Q(B)=0<P(B)$ and partition $\{B,B^c\}$; both sides are ∞. Otherwise let $X=dP/dQ$, $\varphi(x)=x\log x$, so $D=E_Q[\varphi(X)]$ by (2.4). Since $\varphi(x)\ge0$ iff $x\ge1$, monotone convergence gives $E_Q[\varphi(X)1\{X<c\}]\to D(P\|Q)$ as $c\to\infty$, even if D is infinite. Take $n=c/\epsilon$ an integer, cells $E_j=\{j\epsilon\le X<(j+1)\epsilon\}$ for $j<n$ (the text writes ≤ on both ends) and $E_n=\{X\ge c\}$, and $Y=\epsilon\lfloor X/\epsilon\rfloor$. By uniform continuity of φ on $[0,c]$, $|\varphi(x)-\varphi(y)|\le\epsilon'$ when $|x-y|\le\epsilon$, with $\epsilon'\to0$ as $\epsilon\to0$. Hence $E_Q[\varphi(Y)1\{X<c\}]\ge E_Q[\varphi(X)1\{X<c\}]-\epsilon'$, and
$$E_Q[\varphi(Y)1\{X<c\}]=\sum_{j<n}\varphi(j\epsilon)Q(E_j)\le\epsilon'+\sum_{j<n}\varphi\Big(\tfrac{P(E_j)}{Q(E_j)}\Big)Q(E_j)\le\epsilon'+Q(X\ge c)\log e+\sum_{j\le n}P(E_j)\log\tfrac{P(E_j)}{Q(E_j)}.$$
The second inequality uses $\varphi\ge-\log e$. Send $\epsilon\to0$ and then $c\to\infty$ (using $Q(X\ge c)\to0$). $\square$

### 4.3 Donsker–Varadhan (p. 71–73)
**Theorem 4.6.** Let $\mathcal C_Q=\{f:\mathcal X\to\mathbb R\cup\{-\infty\}:0<E_Q[e^{f(X)}]<\infty\}$. Then
$$D(P\|Q)=\sup_{f\in\mathcal C_Q}E_P[f(X)]-\log E_Q[\exp\{f(X)\}].\tag{4.11}$$
If $D(P\|Q)<\infty$, then $E_P[f]$ is well defined and $<\infty$ for every $f\in\mathcal C_Q$. (4.11) also holds with $\mathcal C_Q$ replaced by all real-valued simple functions. If $\mathcal X$ is a normal topological space with the Borel σ-algebra, then
$$D(P\|Q)=\sup_{f\in C_b}E_P[f(X)]-\log E_Q[\exp\{f(X)\}],\tag{4.12}$$
with $C_b$ the bounded continuous functions (p. 72).

*Proof.* "≥" (assume $D<\infty$): for $f\in\mathcal C_Q$ define the tilted measure $Q^f(dx)=\exp\{f(x)-\psi_f\}Q(dx)$, $\psi_f\triangleq\log E_Q[e^{f(X)}]$ (4.13). Using (2.11) with $\mu=Q$:
$$E_P[f(X)]-\psi_f=E_P\Big[\mathrm{Log}\tfrac{dQ^f/dQ}{1}\Big]=D(P\|Q)-D(P\|Q^f)\le D(P\|Q).$$
"≤" over simple functions: the idea is $f=\log\frac{dP}{dQ}$, handled carefully. If $P\not\ll Q$, take E with $Q[E]=0<P[E]$ and $f=c1_E$, $c\to\infty$: both sides are infinite. If $P\ll Q$, for a partition set $f=\sum_j1_{E_j}\log\frac{P[E_j]}{Q[E_j]}$. Then the DV objective equals the partition sum in (4.9), so Thm 4.5 gives sup ≥ D (p. 72).
For (4.12), approximate a simple function by continuous bounded ones so that $E_P$ and $E_Q[e^\cdot]$ both converge. First, for $a>0$ and measurable A, choose compact $F\subset A\subset U$ open with $\max(P[U]-P[F],Q[U]-Q[F])\le\epsilon$ (possible for regular measures; finite measures on Polish spaces are regular). Urysohn's lemma gives continuous $f_\epsilon:\mathcal X\to[0,a]$ equal to a on F and 0 off U. Then $aP[F]\le E_P f_\epsilon\le aP[U]$ and $e^aQ[F]\le E_Q e^{f_\epsilon}\le e^aQ[U]$, so (4.14) holds: $E_P f_n\to aP[A]$ and $E_Qe^{f_n}\to e^aQ[A]$ (p. 72–73). For $g=\sum_{i=1}^na_i1_{A_i}$ with disjoint $A_i$ and $|a_i|\le a_{\max}$, approximate each piece with $F_i\subset A_i\subset U_i$ and $S=\cup_i(U_i\setminus F_i)$, $\max(P[S],Q[S])\le n\epsilon$. Then $|E_P[\sum f_{i,\epsilon}]-E_P[g]|\le a_{\max}n^2\epsilon$ and $E_Q[e^{\sum f_{i,\epsilon}}]\le E_Q[e^g]+e^{na_{\max}}n\epsilon$ (p. 73). $\square$

*Intuition note.* Each test function f gives a lower bound on D; the best f is $\log dP/dQ$. The term $\log E_Qe^f$ is a penalty that stops f from just being huge.

**Remark 4.4 (uses, p. 73).**
1. With $f=\epsilon g$, $\epsilon\ll1$, linearizing exp and log shows that when $D(P\|Q)$ is small, $E_P[g]\approx E_Q[g]$, for g with finite exponential moment under Q. Total variation gives $|E_Pg-E_Qg|\le\|g\|_\infty\mathrm{TV}(P,Q)$ but only for bounded g.
2. $E_P[f]\le\log E_Q e^{f}+D(P\|Q)$ estimates $E_P[f]$ for complicated P by a smart Q (e.g. with iid components).
3. D(·‖Q) is convex in P (shown in Ch. 5, said to hold in the pair). (4.11) is the Young–Fenchel duality, since the conjugate of $D(\cdot\|Q)$ is the convex map $f\mapsto\psi_f$.
4. DV is an "improved version" of the DPI. The estimate $P[A]\log\frac1{Q[A]}\le D(P\|Q)+\log2$ (4.15), used in large deviations and Fano's inequality, also follows from (4.11) with $f=1\{x\in A\}\log\frac1{Q[A]}$.

### 4.4 Gibbs variational principle (p. 74–77)
DV writes the convex $P\mapsto D(P\|Q)$ as a sup of linear functions $P\mapsto E_P[f]-\psi_f$. By convex duality one expects $f\mapsto\psi_f$ to have a similar sup form (p. 74).

**Proposition 4.7.** For measurable $f:\mathcal X\to\mathbb R\cup\{-\infty\}$ and probability Q,
$$\log E_Q[\exp\{f(X)\}]=\sup_P E_P[f(X)]-D(P\|Q),$$
over P with $D(P\|Q)<\infty$. If the left side is finite, the unique maximizer is $P=Q^f$ (p. 74).

*Proof (p. 74).* Let $\psi_f=\log E_Qe^f$.
- If $\psi_f=-\infty$, then f = −∞ Q-a.s., hence P-a.s., and both sides are −∞.
- If $-\infty<\psi_f<\infty$: DV gives $\psi_f\ge E_Pf-D(P\|Q)$, with equality at $P=Q^f$. For uniqueness, (2.11) gives $E_P[f-\psi_f]=D(P\|Q)-D(P\|Q^f)$ whenever $D(P\|Q)<\infty$. So $E_Pf<\infty$ and $E_P[f]-D(P\|Q)=\psi_f-D(P\|Q^f)$. Equality with $\psi_f$ forces $P=Q^f$.
- If $\psi_f=\infty$: set $f_n=f\wedge n$. Then $\psi_{f_n}<\infty$ and there are $P_n$ with $E_{P_n}[f\wedge n]-D(P_n\|Q)=\psi_{f_n}\nearrow\infty$. Since $E_{P_n}[f\wedge n]\le E_{P_n}[f]$, also $E_{P_n}f-D(P_n\|Q)\ge\psi_{f_n}\to\infty$. $\square$

The key idea in applications is to replace the sup over all P by a subset that is easier to handle; this underlies variational inference (p. 74).

**Example 4.1 (mean-field for the Ising model, p. 75–76).** $\tilde X\in\{0,1\}^{n+m}$, $P_{\tilde X}(\tilde x)=\frac1{\tilde Z}\exp\{\tilde x^\top\tilde A\tilde x+\tilde b^\top\tilde x\}$, with $\tilde A$ symmetric with zero diagonal, often sparse. Split $\tilde X=(X,Y)$: first n coordinates hidden, last m observed. Then $P_{X|Y}(x|y)=\frac1Z\exp\{x^\top Ax+b^\top x\}$ on $\{0,1\}^n$, where A is the leading $n\times n$ minor of $\tilde A$ (b and Z depend on y). Computing even $P[X_1=1]$ is generally infeasible, since Z needs $2^n$ terms. With $f(x)=x^\top Ax+b^\top x$ and Q uniform on $\{0,1\}^n$, Prop. 4.7 gives
$$\log Z-n\log2=\log E_Q[e^f]=\sup_{P_{X^n}}E_P[f(X^n)]-D(P\|Q),$$
and by Thm 2.2, $\log Z=\sup_{P_{X^n}}E_P[f(X^n)]+H(P_{X^n})$. Restricting to product laws $\prod_i\mathrm{Ber}(p_i)$ turns the sup into $\sup_pp^\top Ap+b^\top p+\sum_ih(p_i)$ ($h$ = binary entropy; the first two terms use zero diagonal, *added step*). The objective is strongly concave (Ex. I.37), so first-order conditions (mean-field equations) suffice:
$$p_i=\sigma\Big(b_i+2\sum_{j=1}^na_{i,j}p_j\Big),\qquad\sigma(x)=\frac1{1+e^{-x}},$$
solved by iterative message passing. The approximation is $P_{X|Y=y}\approx\prod_i\mathrm{Ber}(p_i)$. The point is to use the maximizer, not only the value of Z, as an approximate posterior (p. 75–76).

**ELBO (p. 76).** Take a family $P^{(\theta)}_{X,Y}$ with X latent and Y observed, where $P_X$ and $P_{Y|X}$ are simple but $P_Y$ and $P_{X|Y}$ are not. The evidence is $P_Y(y)=E_{x\sim P_X}[P_{Y|X}(y|x)]$. Apply Prop. 4.7 with $f(x)=\log P_{Y|X}(y|x)$ and $Q=P_X$:
$$\log P_Y(y)=\sup_RE_R[f(X)]-D(R\|P_X)=\sup_RE_{X\sim R}\Big[\log\frac{P_{X,Y}(X,y)}{R(X)}\Big].\tag{4.16}$$
For any fixed R this is a provable lower bound on $\log P_Y(y)$ (the evidence lower bound). All complexity moves to optimizing over R, typically within a convenient class. One application is the EM algorithm, see (5.33) (p. 76).

**Example 4.2 (variational autoencoders, p. 76–77).** Density estimation from $y_1,\dots,y_n\overset{iid}\sim P_Y$ on $\mathbb R^d$. Generative model: $X\sim N(0,I_{d'})$, $Y=\mu(X;\theta)+D(X;\theta)Z$, $X\perp Z\sim N(0,I_d)$, with μ and diagonal D given by neural networks with weights θ. Maximum likelihood $\max_\theta\sum_i\log P^{(\theta)}_Y(y_i)$ is intractable, so replace it via ELBO by
$$\max_\theta\sup_{R_{X|Y}}\sum_iE_{X\sim R_{X|Y=y_i}}\Big[\log\frac{p^{(\theta)}_{X,Y}(X,y_i)}{r_{X|Y}(X|y_i)}\Big].\tag{4.17}$$
In this form it is the EM algorithm (Sec. 5.6). The 21st-century step is to restrict R to a Gaussian "recognition model" $X=\tilde\mu(Y;\phi)+\tilde D(Y;\phi)\tilde Z$, $\tilde Z\sim N(0,I_{d'})$, with networks of parameter φ. The ELBO is attained at the true posterior, so this approximates the true posterior by a Gaussian. Replacing the expectation by samples $\tilde Z_{ij}$:
$$\max_\theta\max_\phi\sum_i\sum_j\log\frac{p^{(\theta)}_{X,Y}(x_{i,j},y_i)}{r^{(\phi)}_{X|Y}(x_{i,j}|y_i)},\quad x_{i,j}=\tilde\mu(y_i;\phi)+\tilde D(y_i;\phi)\tilde Z_{ij}.\tag{4.18}$$
Gradients in θ, φ come from automatic differentiation. Since R and $P_{Y|X}$ are Gaussian, less Monte Carlo is needed: the objective in (4.17) equals $-D(R_{X|Y=y_i}\|P_X)+E_{R}[\log p^{(\theta)}_{Y|X}(y_i|X)]$, where the Gaussian KL is closed-form (Example 2.2) and only the second term needs sampling. After training, $P_Y^{(\theta^*)}$ generates samples, $R^{(\phi^*)}_{X|Y}$ "encodes", $P^{(\theta^*)}_{Y|X}$ "decodes" (p. 77). Footnote: the "reparametrization trick" writes $E_{Q^{(\phi)}}[f]=E_{Z\sim N}[f(g(Z;\phi))]$ and moves the gradient inside, which is better than the score-function estimator $E[f\nabla_\phi\ln q^{(\phi)}]$ here (p. 77).

### 4.5 Continuity of divergence (p. 78)
**Prop. 4.8.** For finite $\mathcal X$ and Q with $Q(x)>0$ for all x, $P\mapsto D(P\|Q)$ is continuous (each term of $\sum_xP(x)\log\frac{P(x)}{Q(x)}$ is continuous in $P(x)$); in particular $P\mapsto H(P)$ is continuous. Warning: divergence is never continuous in the pair, even for finite alphabets, e.g. $d(\frac1n\|2^{-n})\not\to0$ (p. 78).

**Remark 4.5.** In general D is not continuous in P or in Q. Example: $S_n=\frac1{\sqrt n}\sum_{i\le n}X_i$ with $X_i$ iid uniform on $\{\pm1\}$. By the CLT $S_n\to N(0,1)$ in distribution, yet $D(P_{S_n}\|N(0,1))=\infty$ for all n because $S_n$ is discrete. It is also an example of strict inequality in (4.19) (p. 78).

**Theorem 4.9 (lower semicontinuity).** Let $\mathcal X$ be a metric space with Borel σ-algebra. If $P_n\to P$ and $Q_n\to Q$ weakly, then
$$D(P\|Q)\le\liminf_{n\to\infty}D(P_n\|Q_n).\tag{4.19}$$
On a general space, pointwise convergence ($P_n[E]\to P[E]$, $Q_n[E]\to Q[E]$ for every measurable E) also suffices. Proof: from (4.12), since $E_{P_n}f\to E_Pf$ and $E_{Q_n}e^f\to E_Qe^f$ for $f\in C_b$ (a sup of continuous functionals is lsc) (p. 78).

### 4.6* Continuity under monotone limits of σ-algebras (p. 79–81)
Write $D(P_{\mathcal F}\|Q_{\mathcal F})$ to make the σ-algebra explicit. $\mathcal F_n\nearrow\mathcal F$ means $\mathcal F=\sigma(\cup_n\mathcal F_n)$. $\mathcal F_n\searrow\mathcal F$ means $\mathcal F=\cap_n\mathcal F_n$. The claims are
$$\mathcal F_n\nearrow\mathcal F\Rightarrow D(P_{\mathcal F_n}\|Q_{\mathcal F_n})\nearrow D(P_{\mathcal F}\|Q_{\mathcal F}),\qquad\mathcal F_n\searrow\mathcal F\Rightarrow D(P_{\mathcal F_n}\|Q_{\mathcal F_n})\searrow D(P_{\mathcal F}\|Q_{\mathcal F}).\tag{4.20, 4.21}$$
The text says "we always have" these in the introduction, but Prop. 4.12 below adds a finiteness condition for (4.21) (p. 79–80).

**Definition 4.10.** For positive additive (not necessarily σ-additive) set functions P, Q on an algebra $\mathcal F$, define $D(P_{\mathcal F}\|Q_{\mathcal F})$ as the supremum of the partition sums in (4.9) over finite $\mathcal F$-measurable partitions. Radon–Nikodym is unavailable here, so the original definition does not apply (p. 79).

**Theorem 4.11.** For probability measures on $(\mathcal X,\mathcal H)$ and sub-algebras of $\mathcal H$ (p. 79–80):
- (Monotonicity) $\mathcal F\subseteq\mathcal G\Rightarrow D(P_{\mathcal F}\|Q_{\mathcal F})\le D(P_{\mathcal G}\|Q_{\mathcal G})$ (4.22).
- For increasing algebras $\mathcal F_1\subseteq\mathcal F_2\subseteq\dots$ with limit $\mathcal F=\cup_n\mathcal F_n$: $D(P_{\mathcal F_n}\|Q_{\mathcal F_n})\nearrow D(P_{\mathcal F}\|Q_{\mathcal F})$.
- If $\mathcal F$ is $(P+Q)$-dense in $\mathcal G$ (every $E\in\mathcal G$ is approximated by $E'\in\mathcal F$ with $(P+Q)[E\triangle E']\le\epsilon$), then $D(P_{\mathcal F}\|Q_{\mathcal F})=D(P_{\mathcal G}\|Q_{\mathcal G})$ (4.23).
- (Monotone convergence) For increasing algebras with $\mathcal F=\bigvee_n\mathcal F_n$ the σ-algebra they generate, $D(P_{\mathcal F_n}\|Q_{\mathcal F_n})\nearrow D(P_{\mathcal F}\|Q_{\mathcal F})$; in particular $D(P_{X^\infty}\|Q_{X^\infty})=\lim_nD(P_{X^n}\|Q_{X^n})$.

*Proof sketch.* The first two items follow directly from the definition. The third: a $\mathcal G$-partition $\{E_i\}$ is approximated by an $\mathcal F$-partition $\{E_i'\}$ with $(P+Q)[E_i\triangle E_i']\le\epsilon$ (choose $E_1'$ within $\epsilon/2n$, then $E_2'$ approximating $E_2\setminus E_1'$, etc., and $E_n'=(\cup_{j<n}E_j')^c$, the text writes $j\le1$). Sending $\epsilon\to0$ makes the partition sums converge. The last statement uses that any algebra is μ-dense in the σ-algebra it generates, for bounded μ (cf. [142, Lemma III.7.1]) (p. 80).

**Proposition 4.12.** If $\mathcal F_n\searrow\mathcal F$ and $D(P_{\mathcal F_0}\|Q_{\mathcal F_0})<\infty$, then $D(P_{\mathcal F_n}\|Q_{\mathcal F_n})\searrow D(P_{\mathcal F}\|Q_{\mathcal F})$ (4.24). The finiteness condition cannot be dropped (see the example after (4.32)) (p. 80).

*Proof (p. 80–81).* Let $X_{-n}=\frac{dP}{dQ}\big|_{\mathcal F_n}=E_Q[\frac{dP}{dQ}|\mathcal F_n]$. Then $(\dots,X_{-1},X_0)$ is a uniformly integrable martingale, and by reversed-time martingale convergence $X_{-n}\to X_{-\infty}=\frac{dP}{dQ}\big|_{\mathcal F}$ a.s. (4.25). It suffices to show $E_Q[X_{-n}\log X_{-n}]\to E_Q[X_{-\infty}\log X_{-\infty}]$. Split $x\log x=x\log^+x+x\log^-x$ ($\log^+=\max(\log,0)$, $\log^-=\min(\log,0)$). Since $x\log^-x$ is bounded, bounded convergence handles that part. For the $\log^+$ part: $x\mapsto x\log^+x$ is convex, and for any non-negative convex φ with $E\varphi(X_0)<\infty$ the family $Z_n=\varphi(E[X_0|\mathcal F_n])$ is uniformly integrable. Indeed, by Jensen, $P[Z_n>c]\le E[\varphi(X_0)]/c$, and $E[Z_n1\{Z_n>c\}]\le E[\varphi(X_0)1\{Z_n>c\}]\to0$. So $X_{-n}\log^+X_{-n}$ is uniformly integrable and converges by (4.25). $\square$

*Intuition note.* More information (a finer σ-algebra) can only increase divergence, and in the limit nothing is lost. For shrinking σ-algebras the limit works if the starting divergence is finite, because then the densities are controlled.

### 4.7 Mutual information: variational forms and continuity (p. 81–83)
**Prop. 4.13.** (a) For finite $\mathcal X,\mathcal Y$, $P_{X,Y}\mapsto I(X;Y)$ is continuous. (b) For finite $\mathcal X$, $P_X\mapsto I(X;Y)$ is continuous. (c) For arbitrary $\mathcal X,\mathcal Y$, let $P_X$ range over $\Pi=\mathrm{co}(P_1,\dots,P_n)$. If $I(P_j,P_{Y|X})<\infty$ for all $j\in[n]$, then $P_X\mapsto I(X;Y)$ is continuous (p. 81).
*Proof (p. 81–82).* (a) Use $I=H(X)+H(Y)-H(X,Y)$ and Prop. 4.8. (b) Take $Q_Y=\frac1{|\mathcal X|}\sum_xP_{Y|X=x}$. Then $D(P_Y\|Q_Y)=E_{Q_Y}[f(\sum_xP_X(x)h_x(Y))]$ with $f(t)=t\log t$ and $h_x=\frac{dP_{Y|X=x}}{dQ_Y}$, which are bounded by $|\mathcal X|$ and non-negative. So bounded convergence gives continuity of $P_X\mapsto D(P_Y\|Q_Y)$. By the golden formula $I=D(P_{Y|X}\|Q_Y|P_X)-D(P_Y\|Q_Y)$, and the first term is linear in $P_X$. (c) Form a chain $Z\to X\to Y$ with $Z\in[n]$, $P_{X|Z=j}=P_j$. Assume w.l.o.g. the $P_j$ are distinct extreme points, so $P_Z\leftrightarrow P_X\in\Pi$ is a linear bijection. Then $I(X;Y)=I(Z;Y)+I(X;Y|Z)$: the first term is continuous in $P_Z$ by (b), the second is linear in $P_Z$.

Further properties (from $I=D(P_{X,Y}\|P_XP_Y)$), p. 82–83:
1. **DV for MI:** $I(X;Y)=\sup_fE[f(X,Y)]-\log E[\exp f(X,\bar Y)]$ (4.26), with $\bar Y$ an independent copy of Y. A stronger form: $I(X;Y)\ge E[f(X,Y)]-E[\log E[\exp f(X,\bar Y)|X]]$ (4.27), from which (4.26) follows by moving the outer expectation inside the log. Both show $E f(X,Y)\approx Ef(X,\bar Y)$ when $I(X;Y)$ is small (cf. Ex. I.55).
2. **Lower semicontinuity:** if $(X_n,Y_n)\to(X,Y)$ in distribution, $I(X;Y)\le\liminf I(X_n;Y_n)$ (4.28). Strict inequality: $X_n=Y_n=\frac1nZ$ gives $(X_n,Y_n)\to(0,0)$ but $I(X_n;Y_n)=H(Z)>0=I(0;0)$. A sharper one: $(X_p,Y_p)$ uniform on the unit $\ell_p$-ball in the plane converges to $(0,0)$ as $p\to0$, while $I(X_p;Y_p)\to\infty$ (Ex. I.16).
3. **Partitions:** $I(X;Y)=\sup_{\{E_i\}\times\{F_j\}}\sum_{i,j}P_{X,Y}[E_i\times F_j]\log\frac{P_{X,Y}[E_i\times F_j]}{P_X[E_i]P_Y[F_j]}$ (4.29), using that measurable rectangles are dense in the product σ-algebra.
4. **Monotone convergence I:** $I(X^\infty;Y)=\lim_nI(X^n;Y)$ (4.30), $I(X^\infty;Y^\infty)=\lim_nI(X^n;Y^n)$ (4.31). All information between the processes sits in finite-dimensional projections, none in the tail σ-algebra. Applying the finite-n chain rule to (4.30) recovers (4.1).
5. **Monotone convergence II:** with $\mathcal F_{tail}=\cap_{n\ge1}\sigma(X_n^\infty)$ and $X_{tail}$ such that $\sigma(X_{tail})=\cap_n\sigma(X_n^\infty)$,
$$I(X_{tail};Y)=\lim_{n\to\infty}I(X_n^\infty;Y)\tag{4.32}$$
whenever the right side is finite (consequence of Prop. 4.12). Without finiteness it fails: for $X_j\overset{iid}\sim\mathrm{Ber}(1/2)$ and $Y=X_0^\infty$, each $I(X_n^\infty;Y)=\infty$, but $X_{tail}$ is a.e. constant (Kolmogorov 0–1 law), so the left side is 0.

### 4.8* PAC-Bayes (p. 83–90)
Here ρ, π are distributions on Θ, and $E_\rho[f_\theta(x)]=\int f_\theta(x)\rho(d\theta)$ integrates only θ. $E_{P_X}$ integrates only X (p. 83).

**Prop. 4.14 (PAC-Bayes inequality).** For measurable $(\theta,x)\mapsto f_\theta(x)$, a random variable X and prior π, with probability ≥ 1−δ, for all ρ simultaneously:
$$E_\rho[f_\theta(X)-\psi(\theta)]\le D(\rho\|\pi)+\log\frac1\delta,\qquad\psi(\theta)\triangleq\log E_{P_X}[\exp\{f_\theta(X)\}].\tag{4.33}$$
Moreover, for any joint $P_{\theta,X}$,
$$E[f_\theta(X)-\psi(\theta)]\le I(\theta;X)\le D(P_{\theta|X}\|\pi|P_X).\tag{4.34}$$
*Proof (p. 84).* Prove the exponential inequality
$$E_{P_X}\Big[\sup_\rho\exp\{E_\rho[f_\theta(X)-\psi(\theta)]-D(\rho\|\pi)\}\Big]\le1\tag{4.35}$$
(sup over ρ with $D(\rho\|\pi)<\infty$); (4.33) follows by Markov. Measurability of the sup over uncountably many ρ is shown along the way. Apply the Gibbs principle to $\theta\mapsto f_\theta(X)-\psi(\theta)$ with base π (it may be −∞): $\sup_\rho E_\rho[f_\theta(X)-\psi(\theta)]-D(\rho\|\pi)=\log E_\pi[\exp\{f_\theta(X)-\psi(\theta)\}]$, a measurable function of X. Exponentiate and take $E_{P_X}$: the left side of (4.35) equals $E_{P_X}[E_\pi[\exp\{f_\theta(X)-\psi(\theta)\}]]$. Let $E=\{\theta:\psi(\theta)<\infty\}$. For $\theta\in E$, $E_{P_X}[\exp\{f_\theta-\psi\}]=1$. Applying $E_\pi$ and Fubini gives $\pi[E]$, and the indicator can be dropped because for $\theta\notin E$ the integrand is $\exp\{f_\theta-\infty\}=0$. So the value is $\pi[E]\le1$. For (4.34), put $\rho=P_{\theta|X=x}$ in (4.35), move the outer expectation into the exponent by Jensen, and for the $I$-bound take $\pi=P_\theta$ and use (4.5). $\square$

*Intuition note.* With one probability budget δ, a bound on an average over any ρ holds simultaneously for all ρ. Choosing ρ far from the prior π is penalised in the bound by the term $D(\rho\|\pi)$.

**4.8.1 Uniform convergence.**

*Example 4.3 (norm of a Gaussian vector, p. 85).* $X\sim N(0,\Sigma)$ in $\mathbb R^d$. By Jensen $E\|X\|\le\sqrt{E\|X\|^2}=\sqrt{\mathrm{tr}\,\Sigma}$. For a high-probability bound, write $\|X\|=\sup_{\|v\|=1}v^\top X$. Take $\rho_v=N(v,\beta^2I_d)$ (so $v^\top X=E_{\rho_v}[\theta^\top X]$), $\pi=N(0,\beta^2I_d)$, $f_\theta(x)=\lambda\theta^\top x$. With natural logs: $\psi(\theta)=\frac12\lambda^2\theta^\top\Sigma\theta$, $E_{\rho_v}\psi=\frac{\lambda^2}2(v^\top\Sigma v+\beta^2\mathrm{tr}\Sigma)$, $D(\rho_v\|\pi)=\frac{\|v\|^2}{2\beta^2}$ via (2.8). By (4.33), with probability ≥ 1−δ, for all unit v:
$$\lambda v^\top X\le\frac{\lambda^2}2(v^\top\Sigma v+\beta^2\mathrm{tr}\Sigma)+\frac1{2\beta^2}+\ln\frac1\delta.$$
Choosing $\beta^2=1/\sqrt{\lambda^2\mathrm{tr}\Sigma}$ gives $\lambda v^\top X\le\frac{\lambda^2}2v^\top\Sigma v+\lambda\sqrt{\mathrm{tr}\Sigma}+\ln\frac1\delta$. Using $v^\top\Sigma v\le\|\Sigma\|_{op}$ and optimizing λ:
$$\|X\|\le\sqrt{\mathrm{tr}\,\Sigma}+\sqrt{2\|\Sigma\|_{op}\ln\tfrac1\delta}.$$
Chernoff-type methods give such results too, but the PAC-Bayes proof (a) holds for any X with $\psi(\theta)\le\frac{\lambda^2}2\theta^\top\Sigma\theta$ and (b) extends to sample covariance matrices (cf. [475]) (p. 85).

**Definition 4.15.** X is $\sigma^2$-subgaussian if $E[e^{\lambda(X-E[X])}]\le e^{\sigma^2\lambda^2/2}$ for all $\lambda\in\mathbb R$ (p. 85). Observations (p. 86): $N(0,\sigma^2)$ is $\sigma^2$-subgaussian (with equality); $X\in[a,b]$ is $\frac{(b-a)^2}4$-subgaussian (Hoeffding's lemma); the average of n iid $\sigma^2$-subgaussian variables is $(\sigma^2/n)$-subgaussian. So averages of independent bounded variables are $O(1/n)$-subgaussian.

*Uniform convergence (p. 86).* For F a class of functions and iid sample $X^n$, one wants high-probability bounds on $\sup_{f\in F}E[f(X)]-\hat E_n[f(X)]$, $\hat E_n f=\frac1n\sum f(X_i)$. If each f takes values in [0,1], $(E-\hat E_n)f$ is $\frac1{4n}$-subgaussian, and PAC-Bayes applied to $\lambda(E-\hat E_n)f(X)$ gives, with probability ≥ 1−δ, for all ρ on F and a fixed prior π:
$$E_{f\sim\rho}[(E-\hat E_n)f(X)]\le\frac\lambda{8n}+\frac1\lambda D(\rho\|\pi)+\ln\frac1\delta.$$
As printed on p. 86, $\ln\frac1\delta$ is not divided by λ; compare (4.39), where $\ln\frac1\delta$ is inside the factor $\frac1\lambda$ (see Reading notes). It is useful for countable F (Ex. I.55, I.56), and most powerful for uncountable F. The usual alternative is discretization and chaining; PAC-Bayes often gives sharper results and shorter proofs (p. 86).

**Remark 4.6 (vs Rademacher complexity).** Each ρ defines a linear function $F(\rho)=E_{\theta\sim\rho}[f_\theta(Y)]$. If $|f_\theta|\le M$, the set $\{F(\rho):D(\rho\|\pi)\le C<\infty\}$ has Rademacher complexity $O(M\sqrt{C/n})$ [239]. The same holds for $\{F(\rho):G(\rho)\le C\}$ whenever G is strongly convex, and $\rho\mapsto D(\rho\|\pi)$ is strongly convex (Ex. I.37) (p. 86–87).

**4.8.2 Generalization bounds (p. 87–90).** Setup: sample $X^n\overset{iid}\sim P$, parameter space Θ, loss $\ell_\theta(X_i)$, test loss $L(\theta)=E[\ell_\theta(X_{new})]$ (not computable since P is unknown), training error $\hat L_n(\theta)=\frac1n\sum\ell_\theta(X_i)$. Two selection rules: ERM, $\hat\theta=\arg\min\hat L_n$; and the Gibbs sampler, $\rho(d\theta)\propto\pi(d\theta)e^{-\lambda\hat L_n(\theta)}$ (4.36), which reduces to ERM as $\lambda\to\infty$ (p. 87). Overfitting means $\hat L_n(\hat\theta)$ may not represent $L(\hat\theta)$. Treat the estimator as a data-dependent ρ (a channel from $X^n$ to θ), and aim for bounds uniform over ρ, with "∀ρ" inside the probability:
$P[\forall\rho:E_\rho L\le E_\rho\hat L_n+\text{excess risk}(\rho)]\ge1-\delta$. Minimizing the right side over ρ makes the second term a regularizer (p. 88).

**Theorem 4.16 (McAllester-type).** Fix π; suppose $\ell_\theta(x)\in[0,1]$. Then for any $\delta\le e^{-1}$,
$$P\Big[\forall\rho:E_{\theta\sim\rho}L(\theta)\le E_{\theta\sim\rho}\hat L_n(\theta)+\frac54\sqrt{\frac{D(\rho\|\pi)+\ln\frac1\delta}{2n}}+\frac1{\sqrt{10n}}\Big]\ge1-\delta.\tag{4.37}$$
The same holds if $\ell_\theta(X)$ is $\frac14$-subgaussian for each θ (p. 88).

*Finite Θ (p. 88).* For $|\Theta|=M$, $P[\forall\rho:E_\rho L\le E_\rho\hat L_n+\sqrt{\frac1{2n}\ln\frac M\delta}]\ge1-\delta$ (4.38). By linearity it suffices to use point masses. $\hat L_n(\theta)-L(\theta)$ is zero-mean and $\frac1{4n}$-subgaussian, so by Markov, $P[L-\hat L_n\ge t]\le e^{\lambda^2/8n-\lambda t}$. Setting the right side to $\delta/M$ and using a union bound gives $L-\hat L_n\le\frac\lambda{8n}+\frac1\lambda\ln\frac M\delta$ for all θ, and $\lambda=\sqrt{8n\ln\frac M\delta}$ yields (4.38). Applying (4.37) with $\pi=\mathrm{Unif}(\Theta)$ and $D(\rho\|\pi)\le\log M$ recovers (4.38) with a slightly worse excess risk. The core difficulty is that the union bound needs finite Θ (p. 88–89).

*Proof of Theorem 4.16 (p. 89).*
1. Fix λ and apply PAC-Bayes to $f_\theta(X^n)=\lambda(L(\theta)-\hat L_n(\theta))$ with $\psi(\theta)\le\lambda^2/8n$. With probability ≥ 1−δ, for all ρ: $E_\rho[L-\hat L_n]\le\frac\lambda{8n}+\frac{D(\rho\|\pi)+\ln\frac1\delta}\lambda$ (4.39).
2. Let $b(\rho)=D(\rho\|\pi)+\ln\frac1\delta$. Since $\delta<e^{-1}$, $b\ge1$. The ideal $\lambda^*=\sqrt{8nb(\rho)}$ cannot depend on ρ.
3. Use the grid $\lambda_i=\sqrt{2n}\,2^i$, $i\ge1$, with $\delta_i=\delta2^{-i}$ and a union bound: for all ρ and i, $E_\rho[L-\hat L_n]\le\frac{\lambda_i}{8n}+\frac{b(\rho)+i\ln2}{\lambda_i}$.
4. Pick $i^*$ with $\lambda^*\le\lambda_{i^*}<2\lambda^*$. Then $i^*\ln2<\ln4+\frac12\ln b(\rho)\le\ln4-\frac12+\frac12b(\rho)$.
5. Using $\lambda_{i^*}\le2\lambda^*$ and $1/\lambda_{i^*}\le1/\lambda^*$ the text gets $E_\rho[L-\hat L_n]\le\sqrt{\frac{b(\rho)}{8n}}(2+\frac32)+\frac{\ln4-1/2}{\sqrt{8nb(\rho)}}$. Bound the last term by $\frac1{\sqrt{10n}}$ (since $b\ge1$). $\square$

*Comments (p. 89–90).* (4.39) suggests choosing ρ to minimize $E_\rho\hat L_n+\frac1\lambda D(\rho\|\pi)$; by Prop. 4.7 the minimizer is the Gibbs sampler (4.36). **Criticism of PAC-Bayes (critics' view as reported by the author):** a trained network has non-random weights, so $\rho=\delta_{\hat\theta}$ and $D(\rho\|\pi)=\infty$ for any continuous prior, making the bound vacuous. The author reports [476]'s reply: weights are stored as finite-bit numbers, so one can take $\pi(\theta)=2^{-\mathrm{length}(\theta)}$, where length is the size of a compressed representation of θ. As the author says will be shown in Part II, this is a valid distribution for any lossless compressor. So a highly compressible network (e.g. many zero weights) has smaller excess risk and is less prone to overfitting (p. 89–90).

*In-expectation version.* With $\ell\in[0,1]$ and $\hat\theta\sim\rho$ given $X^n$ (joint $P_{\hat\theta,X^n}$), (4.34) gives for every $\lambda>0$: $E[L(\hat\theta)-\hat L_n(\hat\theta)]\le\frac\lambda{8n}+\lambda I(\hat\theta;X^n)$. Optimizing λ:
$$E[L(\hat\theta)-\hat L_n(\hat\theta)]\le\sqrt{\tfrac1{2n}I(\hat\theta;X^n)}.$$
Intuition: the propensity to overfit can be gauged by the information leaking from $X^n$ into $\hat\theta$. For applications, the flexible-prior form of Thm 4.16 is more convenient (p. 90).

## Toy example (ours)
Check the golden formula (4.2) and the centre-of-gravity property. Let X be uniform on {0,1}, and $P_{Y|X=0}=(\frac34,\frac14)$, $P_{Y|X=1}=(\frac14,\frac34)$ on y∈{0,1}. Logs are base 2; $\log_23=1.58496$, $\log_2\frac32=0.58496$.
- $P_Y=(\frac12,\frac12)$. $D(P_{Y|X=0}\|P_Y)=\frac34(0.58496)+\frac14(-1)=0.43872-0.25=0.18872$. The same holds for x=1, so $I(X;Y)=0.18872$ bits (check: $1-h(\frac14)=1-0.81128$).
- Wrong centre $Q_Y=(\frac34,\frac14)$. $D(P_{Y|X=0}\|Q_Y)=0$. $D(P_{Y|X=1}\|Q_Y)=\frac14\log_2\frac13+\frac34\log_23=-0.39624+1.18872=0.79248$. Average over $P_X$: $D(P_{Y|X}\|Q_Y|P_X)=\frac12(0)+\frac12(0.79248)=0.39624$.
- $D(P_Y\|Q_Y)=\frac12\log_2\frac23+\frac12\log_22=-0.29248+0.5=0.20752$.
- Golden formula: $I+D(P_Y\|Q_Y)=0.18872+0.20752=0.39624$ ✓. The wrong centre costs 0.39624 > 0.18872 = I, as (4.5) says; $Q_Y=P_Y$ costs exactly I.

## Concepts
- [[mutual-information]] — here $I(X;Y)=D(P_{X,Y}\|P_XP_Y)$, with inf forms over $Q_Y$, $Q_XQ_Y$ and sup forms over kernels and partitions (p. 67–70, 83).
- [[relative-entropy-kl-divergence]] — defined via densities, and equivalently as a sup over partitions or functions; convex, lower semicontinuous, not continuous in general (p. 70–72, 78).
- [[golden-formula]] (new) — $D(P_{Y|X}\|Q_Y|P_X)=I(X;Y)+D(P_Y\|Q_Y)$ (p. 67).
- [[gelfand-yaglom-perez-theorem]] (new) — D equals the sup of finite-partition divergences (p. 70).
- [[donsker-varadhan-formula]] (new) — $D=\sup_fE_Pf-\log E_Qe^f$ (p. 72).
- [[gibbs-variational-principle]] (new) — $\log E_Qe^f=\sup_PE_Pf-D(P\|Q)$, maximizer the tilted $Q^f$ (p. 74).
- [[data-processing-inequality]] — used to show partition divergences lower-bound D (p. 71).
- [[chain-rule]] — used in proofs of Thm 4.1 and 4.3 (p. 68–69).
- [[lower-semicontinuity-of-divergence]] (new) — $D(P\|Q)\le\liminf D(P_n\|Q_n)$ under weak convergence (p. 78).
- [[sigma-algebra-continuity]] (new) — D and I converge along increasing σ-algebras; along decreasing ones if finite at the start (p. 79–80).
- [[evidence-lower-bound]] (new) — the Gibbs principle applied to $P_Y(y)=E_{P_X}P_{Y|X}$ gives a provable lower bound (p. 76).
- [[mean-field-approximation]] (new) — restricting the Gibbs sup to product distributions (p. 75).
- [[pac-bayes-inequality]] (new) — with probability ≥ 1−δ, for all ρ, $E_\rho[f_\theta-\psi]\le D(\rho\|\pi)+\log\frac1\delta$ (p. 84).
- [[subgaussian-random-variable]] (new) — $E e^{\lambda(X-EX)}\le e^{\sigma^2\lambda^2/2}$ (p. 85).
- [[exponential-family-gibbs-distribution]] — the tilted measure $Q^f\propto e^fQ$ is of this exponential-tilting form (canon link; the unit does not call it that) (p. 74).

## Canonical instances
- [[awgn-channel]] — Gaussian Q upper-bounds $I(X;Y)$ by $\frac12\log(1+\sigma^2)$ (p. 68).
- [[ising-model-mean-field]] — Gibbs principle plus product distributions gives mean-field equations (p. 75).
- [[variational-autoencoder]] — ELBO with a Gaussian recognition model (p. 76–77).
- [[gaussian-norm-concentration]] — PAC-Bayes proof of $\|X\|\le\sqrt{\mathrm{tr}\Sigma}+\sqrt{2\|\Sigma\|_{op}\ln\frac1\delta}$ (p. 85).
- [[mcallester-generalization-bound]] — Theorem 4.16 (p. 88).
- [[clt-discrete-vs-gaussian]] — $D(P_{S_n}\|N(0,1))=\infty$ although $S_n\to N(0,1)$ (p. 78).

## Bridges (candidates)
- [same-math] Gibbs principle $\log E_Qe^f=\sup_PE_Pf-D(P\|Q)$ ↔ statistical physics: free energy as sup of "energy + entropy" for $\log Z=\sup_PE_Pf+H(P)$ (p. 75).
- [same-math] Donsker–Varadhan duality ↔ convex analysis: Fenchel–Legendre conjugacy of $D(\cdot\|Q)$ and $f\mapsto\psi_f$ (p. 73).
- [structural-analogy] $I(X;Z|Y)$ as distance to Markov chains ↔ graphical models: information flow through a deleted edge (p. 69).
- [structural-analogy] PAC-Bayes with prior $2^{-\mathrm{length}(\theta)}$ ↔ MDL: compressibility of parameters limits overfitting (p. 89–90).
- [structural-analogy] $E[L-\hat L_n]\le\sqrt{I(\hat\theta;X^n)/2n}$ ↔ privacy/leakage: information leaking from data into the output controls overfitting (p. 90).

## Questions this raises
- When does the bound of Thm 4.16 become non-vacuous for real networks, i.e. how small can $D(\rho\|\pi)$ be made with a compression prior?
- Since D is only lower semicontinuous, under what extra conditions (e.g. uniform integrability of densities) does $D(P_n\|Q)\to D(P\|Q)$ hold, as needed to estimate D from samples?
- How loose is the mean-field bound $\sup_{\text{product }P}$ versus the true $\log Z$, and when are the maximizers good posteriors?
- Can the sup over kernels in (4.7) be restricted to a tractable family while keeping the lower bound on $I(X;Y)$ useful (the text points to Sec. 5.6)?

## Exercises worth doing
The chapter cites exercises but does not print them in these pages; the cited ones are:
- Ex. I.37 (p. 75, 87) — strong concavity of the mean-field objective and strong convexity of $\rho\mapsto D(\rho\|\pi)$ — difficulty: medium.
- Ex. I.55 (p. 82, 86) — change of measure when $I(X;Y)$ is small; PAC-Bayes for countable classes — difficulty: medium.
- Ex. I.56 (p. 86) — PAC-Bayes bounds for countably infinite F — difficulty: medium.
- Ex. I.16 (p. 82) — $I(X_p;Y_p)\to\infty$ for uniform on $\ell_p$-balls as $p\to0$ — difficulty: hard.
- Ex. I.54 (p. 88) — alternative generalization bounds — difficulty: medium.

## Reading notes
- The unit is labelled chapter 5 in the metadata, but the printed chapter number is **4** (pages 66–90). Section numbers are 4.1–4.8, and cross-references say "Chapter 4". Printed = pdf − 25.
- Running header: "itbook-export CUP/HE2-design August 16, 2024" (production proof header).
- Misprint: at the end of the proof of Prop. 4.12 (p. 81) the final displayed line reads $E_Q[X_{-n}\log^-X_{-n}]\to E_Q[X_{-\infty}\log^-X_{-\infty}]$. Context (uniform integrability of $X\log^+X$) indicates it should be $\log^+$.
- The uniform-convergence display on p. 86 has $\ln\frac1\delta$ without the factor $\frac1\lambda$ that (4.39) has. Equation (4.39) on p. 89 has the form $\frac1\lambda(D(\rho\|\pi)+\ln\frac1\delta)$; I could not tell from these pages which form is intended on p. 86.
- In the proof of Thm 4.16 (p. 89) the text says $\hat L_n(\theta)$ is "$\frac1{8n}$-subgaussian" with $\psi\le\lambda^2/8n$. Earlier (p. 88) it is $\frac1{4n}$-subgaussian, which gives $\psi\le\lambda^2/8n$; the "$\frac1{8n}$" looks like a slip.
- My own check of the last proof step: tracking the printed constants gives $\frac72\sqrt{b/8n}=\frac74\sqrt{b/2n}$, whereas (4.37) states $\frac54$. I did not resolve this; treat the constant in (4.37) with care.
- Remark 4.5 says the CLT example is also a strict inequality example "for (4.19)", which is printed after the remark; in Thm 4.5's proof the cells are written with ≤ on both ends although they should be disjoint.
- Skipped: Prop. 4.13(c) and the regular-measure approximations are compressed. On p. 90 the in-expectation bound is printed with second term $\lambda I(\hat\theta;X^n)$; the optimised bound $\sqrt{I/2n}$ shown below it corresponds to $I/\lambda$, so this looks like a misprint (not resolved here). Text-layer equations were garbled in places but were checked against the page images.
