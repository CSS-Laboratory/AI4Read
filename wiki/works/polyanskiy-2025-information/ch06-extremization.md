---
id: polyanskiy-2025-information/ch06-extremization
work: polyanskiy-2025-information
unit: "Chapter 5 (printed numbering; supplied as unit ch06) — Extremization of mutual information: capacity saddle point"
pages: 91-105
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
# Extremization of mutual information: capacity saddle point

## L0 — One line
Capacity (max over inputs of I(X;Y)) is also a min over output distributions of the worst-case divergence, so the problem has a saddle point (when an optimal input exists) and, for finite capacity, capacity equals an "information radius" in KL divergence.

## L1 — The gist (≤ 120 words)
The chapter asks how to optimize mutual information over a convex set of input distributions. It shows that D(P‖Q) is jointly convex and that I(X;Y) is concave in the input and convex in the channel. Hence the sup over inputs equals an inf over outputs of the worst-case divergence. When $C<\infty$, the optimal output distribution is unique, and capacity is the KL "radius" of the set of channel rows. This holds even when no optimal input exists (Kemperman). Gaussian input and Gaussian noise form a saddle point. Finally, alternating-minimization algorithms (Blahut–Arimoto, EM, Sinkhorn) compute such optima with large jumps.

**Prerequisites:** KL divergence and conditional divergence; mutual information; the data-processing inequality; the "golden formula" $I(X;Y)=\min_Q D(P_{Y|X}\|Q|P_X)$; lower semicontinuity of D; basic convexity.

## L2 — Key ideas (5–10 bullets)
- Four basic optimization problems (I-projection, maximum likelihood, rate-distortion, capacity) all have convex or concave objectives (p. 91).
- $(P,Q)\mapsto D(P\|Q)$ is jointly convex, proved via the data-processing inequality (DPI). It is not strictly convex (pp. 91–92).
- $I(P_X,P_{Y|X})$ is concave in $P_X$ and convex in $P_{Y|X}$ (pp. 92–93).
- Saddle-point theorem: if an optimal input $P^*_X$ exists, $(P^*_X,P^*_Y)$ is a saddle point for $D(P_{Y|X}\|Q_Y|P_X)$. This yields minimax equality; if also $C<\infty$, it gives a unique $P^*_Y$ with $D(P_Y\|P_Y^*)\le C$ (pp. 94–95).
- Capacity is the KL radius of $\{P_{Y|X=x}\}$ and is at most the KL diameter (pp. 96–97).
- Kemperman: when $C<\infty$, $P^*_Y$ exists, is unique, and the minimax equality holds without assuming a capacity-achieving input exists (pp. 97–99).
- Gaussian saddle point: Gaussian input is best against Gaussian noise; Gaussian noise is worst for Gaussian input under a second-moment constraint (p. 100).
- Alternating minimization (Blahut–Arimoto, EM, Sinkhorn) solves these problems with large "global" jumps; for Blahut–Arimoto, rate-distortion and the convex case of EM it gives computable upper and lower bounds (pp. 102–104).

## L3 — Walkthrough

### Intro (p. 91)
Four problems: I-projection (min over convex class of $P$ of $D(P\|Q)$); maximum likelihood (min over a class of $Q$); rate-distortion (min $I(X;Y)$ over convex class of $P_{Y|X}$); capacity (max $I(X;Y)$ over convex class of $P_X$). The chapter's main finding is that sup over $P_X$ equals inf over $P_Y$, with a saddle point (p. 91).

### 5.1 Convexity of information measures
**Theorem 5.1.** $(P,Q)\mapsto D(P\|Q)$ is convex (p. 91).
Proof. Take $P_X=Q_X=\mathrm{Ber}(\lambda)$, kernels $P_{Y|X=0}=P_0$, $P_{Y|X=1}=P_1$, $Q_{Y|X=0}=Q_0$, $Q_{Y|X=1}=Q_1$. Then $D(P_{X,Y}\|Q_{X,Y})=\bar\lambda D(P_0\|Q_0)+\lambda D(P_1\|Q_1)$. By the DPI,
$$\bar\lambda D(P_0\|Q_0)+\lambda D(P_1\|Q_1)=D(P_{X,Y}\|Q_{X,Y})\ge D(P_Y\|Q_Y)=D(\bar\lambda P_0+\lambda P_1\,\|\,\bar\lambda Q_0+\lambda Q_1).$$
Remark 5.1: for any similarity measure, convexity in the pair is equivalent to "conditioning increases divergence" (p. 91).

Remark 5.2: other proofs use convexity of $(p,q)\mapsto p\log\frac pq$ (perspective function) or the Donsker–Varadhan representation. The proof above shows the map is not strictly convex, since the DPI gap $D(P_{X|Y}\|Q_{X|Y}|P_Y)$ can be zero (e.g. $P_0,Q_0$ share a support disjoint from the common support of $P_1,Q_1$). By contrast $P\mapsto D(P\|Q)$ is strongly convex w.r.t. total variation (Exercise I.37, not reproduced here), which matters for mirror descent (p. 92).

**Theorem 5.2.** $P_X\mapsto H(X)$ is concave; for any channel $P_{Y|X}$, $P_X\mapsto H(X|Y)$ is concave; if $\mathcal X$ is finite, $P_X\mapsto H(X|Y)$ is continuous (p. 92).
Proof. Finite case: $H(X)=\log|\mathcal X|-D(P_X\|U_X)$. General: let $f(P_X)=H(X|Y)$, $U\sim\mathrm{Ber}(\lambda)$, $P_{X|U=0}=P_0$, $P_{X|U=1}=P_1$, chain $U\to X\to Y$. Then $f(\lambda P_1+(1-\lambda)P_0)=H(X|Y)$ and $\lambda f(P_1)+(1-\lambda)f(P_0)=H(X|Y,U)\le H(X|Y)$. Continuity: Proposition 4.13 (p. 92).

**Theorem 5.3.** For fixed $P_{Y|X}$, $P_X\mapsto I(P_X,P_{Y|X})$ is concave. For fixed $P_X$, $P_{Y|X}\mapsto I$ is convex (p. 92).
Three proofs of concavity (pp. 92–93):
1. With $\theta\sim\mathrm{Ber}(\lambda)$, $P_{X|\theta}$ equal to $P^0_X$ or $P^1_X$, and $\theta\to X\to Y$: $I(X;Y)=I(X,\theta;Y)=I(\theta;Y)+I(X;Y|\theta)\ge I(X;Y|\theta)$.
2. $I(X;Y)=\min_Q D(P_{Y|X}\|Q|P_X)$ is a pointwise minimum of affine functions of $P_X$.
3. Golden formula for fixed $Q$: $I(X;Y)=D(P_{Y|X}\|Q|P_X)-D(P_Y\|Q)$; the first term is affine in $P_X$ and $P_X\mapsto D(P_Y\|Q)$ is convex (affine map composed with convex $D$).

Convexity in the channel: $I(X;Y)=D(P_{Y|X}\|P_Y|P_X)$ and $P_Y$ is linear in $P_{Y|X}$, so Theorem 5.1 applies (p. 93).

*Intuition note.* Mixing two input laws can only add the information "which component was used" and so loses nothing against the average of the two. This is why capacity is a concave maximization over inputs.

**Review box: minimax.** Always $\inf_y\sup_x f\ge\sup_x\inf_y f$. Equality holds if a saddle point $(x^*,y^*)$ exists, i.e. $f(x,y^*)\le f(x^*,y^*)\le f(x^*,y)$ for all $x,y$. Conversely, equality implies a saddle point if inf and sup are achieved. Criteria such as Sion's theorem usually require some continuity of $f$, compactness of domains, concavity in $x$ and convexity in $y$. A more general version: for compact convex $\mathcal X,\mathcal Y\subset\mathbb R^n$ and $f$ continuous, concave in $x$ and convex in $y$, $\max_x\min_y f=\min_y\max_x f$. Von Neumann: for finite alphabets and any $g$, $\min_{P_A}\max_{P_B}\mathbb E[g(A,B)]=\max_{P_B}\min_{P_A}\mathbb E[g(A,B)]$ (p. 93).

### 5.2 Saddle point of mutual information
**Theorem 5.4 (Saddle point).** Let $\mathcal P$ be a convex set of distributions on $\mathcal X$. Suppose $P^*_X\in\mathcal P$ satisfies $\sup_{P_X\in\mathcal P}I(P_X,P_{Y|X})=I(P^*_X,P_{Y|X})\triangleq C$. Let $P^*_Y=P_{Y|X}\circ P^*_X$. Then for all $P_X\in\mathcal P$ and all $Q_Y$,
$$D(P_{Y|X}\|P^*_Y|P_X)\le D(P_{Y|X}\|P^*_Y|P^*_X)\le D(P_{Y|X}\|Q_Y|P^*_X).\tag{5.1}$$
Proof (p. 94). Right inequality: $C=I(P^*_X,P_{Y|X})=\min_{Q_Y}D(P_{Y|X}\|Q_Y|P^*_X)$, which is (4.5). Left inequality: trivial if $C=\infty$; else $I<\infty$ on $\mathcal P$. Put $P_X^\lambda=\lambda P_X+\bar\lambda P^*_X\in\mathcal P$, so $P_Y^\lambda=\lambda P_Y+\bar\lambda P^*_Y$. Then
$$C\ge I(X_\lambda;Y_\lambda)=D(P_{Y|X}\|P_Y^\lambda|P_X^\lambda)=\lambda D(P_{Y|X}\|P_Y^\lambda|P_X)+\bar\lambda D(P_{Y|X}\|P_Y^\lambda|P^*_X)\ge\lambda D(P_{Y|X}\|P_Y^\lambda|P_X)+\bar\lambda C,$$
the last step by the right part of (5.1). Since $D(P_{Y|X}\|P_Y^\lambda|P_X)=D(P_{X,Y}\|P_XP_Y^\lambda)$, subtracting $\bar\lambda C$ and dividing by $\lambda$ gives $D(P_{X,Y}\|P_XP^\lambda_Y)\le C$. Take $\liminf_{\lambda\to0}$ and use lower semicontinuity of $D$ (Theorem 4.9).

**Corollary 5.5.** If also $C<\infty$, $P^*_Y$ is unique, and for any $P_Y$ induced by some $P_X\in\mathcal P$,
$$D(P_Y\|P^*_Y)\le C<\infty,\tag{5.2}$$
so $P_Y\ll P^*_Y$ (p. 94).
Proof. Suppose $I(P_X,P_{Y|X})=C$. Then $C=D(P_{Y|X}\|P_Y|P_X)=D(P_{Y|X}\|P^*_Y|P_X)-D(P_Y\|P^*_Y)\le C-D(P_Y\|P^*_Y)$, so $P_Y=P^*_Y$. Statement (5.2) follows from the left inequality of (5.1) and "conditioning increases divergence" (Theorem 2.16) (p. 95).

Remark 5.3 (p. 95): (i) finiteness of $C$ is necessary for Corollary 5.5. Counterexample: the identity channel $Y=X$ on the integers, where any distribution with infinite entropy is capacity-achieving. (ii) The capacity-achieving input need not be unique. Take $Y_1=X_1\oplus Z_1$, $Y_2=X_2$, $Z_1\sim\mathrm{Ber}(1/2)$ independent of $X_1$. Then $\max I(X_1,X_2;Y_1,Y_2)=\log2$, achieved by $\mathrm{Ber}(p)\times\mathrm{Ber}(1/2)$ for every $p$. The output $\mathrm{Ber}(1/2)\times\mathrm{Ber}(1/2)$ is unique.

**Corollary 5.6 (Minimax).** Under the assumptions of Theorem 5.4,
$$\max_{P_X\in\mathcal P}I(X;Y)=\max_{P_X\in\mathcal P}\min_{Q_Y}D(P_{Y|X}\|Q_Y|P_X)=\min_{Q_Y}\sup_{P_X\in\mathcal P}D(P_{Y|X}\|Q_Y|P_X).$$
Proof: maximize/minimize the outer sides of (5.1). This gives $\min_{Q}\sup_{P_X}\le\max_{P_X}D(\cdot\|P^*_Y|P_X)=D(\cdot\|P^*_Y|P^*_X)\le\min_Q D(\cdot\|Q|P^*_X)\le\max_{P_X}\min_Q$. Min-max $\ge$ max-min always, so all are equal (p. 95).

*Intuition note.* The input player maximizes information; the "guesser" picks the output distribution $Q_Y$ and pays divergence. At the capacity-achieving input, the best guess is $P^*_Y$ and neither side gains by deviating.

**Review box: radius and diameter** (p. 96). $\mathrm{rad}(A)=\inf_{y}\sup_{x\in A}d(x,y)$ (5.3); $\mathrm{diam}(A)=\sup_{x,y\in A}d(x,y)$ (5.4); and $\tfrac12\mathrm{diam}(A)\le\mathrm{rad}(A)\le\mathrm{diam}(A)$ (5.5). Sharper bounds: Bohnenblust $\frac n{n+1}\mathrm{diam}$ in any norm on $\mathbb R^n$; Jung $\sqrt{\frac n{2(n+1)}}\,\mathrm{diam}$ for Euclidean distance; $\mathrm{rad}=\frac12\mathrm{diam}$ for $\ell_\infty$.

### 5.3 Capacity as information radius
**Corollary 5.7.** For finite $\mathcal X$ and any kernel $P_{Y|X}$: $\max_{P_X}I(X;Y)=\max_x D(P_{Y|X=x}\|P^*_Y)=D(P_{Y|X=x}\|P^*_Y)$ for all $x$ with $P^*_X(x)>0$ (p. 96). No proof is printed. *(added step)* Take $\mathcal P$ = all distributions in (5.1) with $P_X=\delta_x$: this gives $D(P_{Y|X=x}\|P^*_Y)\le C$. Also $C=\sum_xP^*_X(x)D(P_{Y|X=x}\|P^*_Y)$. A weighted average of numbers $\le C$ equals $C$ only if each number with positive weight equals $C$.

Reading: capacity is the radius of the smallest divergence-"ball" covering all $P_{Y|X=x}$, although divergence is not a metric. The centre $P^*_Y$ is a convex combination of some $P_{Y|X=x}$ and is equidistant from them (p. 97).

**Corollary 5.8.** For any set $\{P_{Y|X=x}\}$:
$$C=\sup_{P_X}I(X;Y)\le\underbrace{\inf_Q\sup_xD(P_{Y|X=x}\|Q)}_{\text{radius}}\le\underbrace{\sup_{x,x'}D(P_{Y|X=x}\|P_{Y|X=x'})}_{\text{diameter}}.$$
Proof: golden formula, then $\sup_x\le$ worst case, then restrict $Q$ to $P_{Y|X=x'}$ (p. 97).

### 5.4* Existence of the capacity-achieving output distribution
**Theorem 5.9 (Kemperman).** For any $P_{Y|X}$ and convex $\mathcal P$ with $C=\sup_{P_X\in\mathcal P}I(P_X,P_{Y|X})<\infty$ (5.6), there is a unique $P^*_Y$ with $C=\sup_{P_X\in\mathcal P}D(P_{Y|X}\|P^*_Y|P_X)$ (5.7). Moreover
$$C=\sup_{P_X}\min_{Q_Y}D(P_{Y|X}\|Q_Y|P_X)=\min_{Q_Y}\sup_{P_X}D(P_{Y|X}\|Q_Y|P_X)\ \ (=\min_{Q_Y}\sup_xD(P_{Y|X=x}\|Q_Y)\text{ if }\mathcal P=\{\text{all }P_X\}),$$
numbered (5.8)–(5.10) (p. 97). Condition (5.6) holds automatically if some $Q_Y$ has $\sup_{P_X}D(P_{Y|X}\|Q_Y|P_X)<\infty$ (5.11) (p. 98).

**Example 5.1** (p. 98). $Z\sim\mathcal N(0,1)$, $C=\sup I(X;X+Z)$ over $P_X$ with $\mathbb E X=0$, $\mathbb EX^2=P$, $\mathbb EX^4=s$. Without the fourth-moment constraint the optimum is $\mathcal N(0,P)$. For $s>3P^2$, $C=\frac12\log(1+P)$ is still the value, approached by $P_X=(1-p)\mathcal N(0,P)+p\delta_x$ with $p\to0$, $x\to\infty$, $px^2\to0$, $px^4\to s-3P^2>0$. No input achieves it, but $P^*_Y=\mathcal N(0,1+P)$ exists and is unique.

Proof of 5.9 (pp. 98–99):
1. Take inputs $P'_{X_n}$ with $I\to C$. Let $\mathcal P_n=\mathrm{conv}\{P'_{X_1},\dots,P'_{X_n}\}$ (a finite-dimensional simplex). By continuity, $I$ attains its max $I_n$ at some $P_{X_n}\in\mathcal P_n$; let $P_{Y_n}$ be its output.
2. $D(P_{Y_n}\|P_{Y_{n+k}})=D(P_{Y|X}\|P_{Y_{n+k}}|P_{X_n})-D(P_{Y|X}\|P_{Y_n}|P_{X_n})\le I(P_{X_{n+k}},P_{Y|X})-I(P_{X_n},P_{Y|X})\le C-I_n$ (5.13–5.15), where (5.14) uses Theorem 5.4 on $(\mathcal P_{n+k},P_{Y_{n+k}})$.
3. Pinsker's inequality (assumed from Theorem 7.10) with $I_n\nearrow C$ shows $(P_{Y_n})$ is Cauchy in total variation. Completeness gives a limit $P^*_Y$.
4. Lower semicontinuity gives $D(P_{Y_n}\|P^*_Y)\le C-I_n\to0$. Hence $D(P_{Y|X}\|P^*_Y|P_{X_n})=I_n+D(P_{Y_n}\|P^*_Y)\to C$ (5.16).
5. For $P_X\in\bigcup_k\mathcal P_k$: $D(P_{Y|X}\|P_{Y_n}|P_X)\le I_n\le C$ (5.17); lower semicontinuity and Fatou's lemma give $D(P_{Y|X}\|P^*_Y|P_X)\le C$ (5.18).
6. For arbitrary $P_X\in\mathcal P$, repeat with $\tilde{\mathcal P}_n=\mathrm{conv}(\{P_X\}\cup\mathcal P_n)$; (5.19–5.20) show the limit is the same $P^*_Y$, so (5.18) holds.
7. Uniqueness: if $Q^*_Y$ also satisfies (5.7), then $C\ge D(P_{Y|X}\|Q^*_Y|P_{X_n})=I_n+D(P_{Y_n}\|Q^*_Y)$, so $D(P_{Y_n}\|Q^*_Y)\to0$. Pinsker and the triangle inequality give $Q^*_Y=P^*_Y$.
8. (5.9): max-min $\le$ min-max $\le\sup D(\cdot\|P^*_Y|P_X)=C$, using (5.16) and (5.17).

**Corollary 5.10.** For countable $\mathcal X$ and convex $\mathcal P$ with $\sup H(X)<\infty$: $\sup_{P_X}H(X)=\min_{Q_X}\sup_{P_X}\sum_xP_X(x)\log\frac1{Q_X(x)}<\infty$. The optimizer $Q^*_X$ exists and is unique; if $Q^*_X\in\mathcal P$ it is the unique maximizer of $H$. Proof: apply Theorem 5.9 to $Y=X$ (pp. 99–100).

**Example 5.2 (max entropy)** (p. 100). If $Z(\lambda)=\sum_{n\in\mathbb Z}e^{-\lambda f(n)}<\infty$ for all $\lambda>0$, then $\max_{\mathbb E f(X)\le a}H(X)\le\inf_{\lambda>0}\{\lambda a+\log Z(\lambda)\}$, taking $Q_X(n)=Z(\lambda)^{-1}e^{-\lambda f(n)}$ (5.21) in Corollary 5.10. Such $Q_X$ are Gibbs distributions. The bound is often tight (Exercise III.27, not reproduced here).

*Intuition note.* The supremum need not be attained: a maximizing sequence of inputs produces outputs that settle down, because the information gap $C-I_n$ controls how far apart they can be.

### 5.5 Gaussian saddle point
**Theorem 5.11.** Let $X_g\sim\mathcal N(0,\sigma_X^2)$, $N_g\sim\mathcal N(0,\sigma_N^2)$, independent (p. 100).
1. $C=I(X_g;X_g+N_g)=\frac12\log(1+\sigma_X^2/\sigma_N^2)$.
2. For all $X\perp N_g$ with $\mathrm{Var}X\le\sigma_X^2$: $I(X;X+N_g)\le I(X_g;X_g+N_g)$ (5.22), with equality iff $X\overset d=X_g$.
3. For all $N$ with $\mathbb E[X_gN]=0$ and $\mathbb EN^2\le\sigma_N^2$: $I(X_g;X_g+N)\ge I(X_g;X_g+N_g)$, with equality iff $N\overset d=N_g$ and $N$ is independent of $X_g$.

Proof (pp. 101–102). WLOG zero means, $Y_g=X_g+N_g$. Define
$$f(x)\triangleq D(P_{Y_g|X_g=x}\|P_{Y_g})=D(\mathcal N(x,\sigma_N^2)\|\mathcal N(0,\sigma_X^2+\sigma_N^2))=\underbrace{\tfrac12\log\!\Big(1+\tfrac{\sigma_X^2}{\sigma_N^2}\Big)}_{=C}+\tfrac{\log e}{2}\,\tfrac{x^2-\sigma_X^2}{\sigma_X^2+\sigma_N^2}.$$
1. $I(X_g;X_g+N_g)=\mathbb E f(X_g)=C$.
2. By the inf-representation, $I(X;X+N_g)\le D(P_{Y_g|X_g}\|P_{Y_g}|P_X)=\mathbb Ef(X)\le C$. *(added step)* The last inequality holds because $\mathbb EX^2\le\sigma_X^2$. If equality holds, uniqueness of the output distribution (Cor. 5.5) gives $P_Y=P_{Y_g}$. Since $P_Y=P_X*\mathcal N(0,\sigma_N^2)$, characteristic functions give $\Psi_X(t)e^{-\sigma_N^2t^2/2}=e^{-(\sigma_X^2+\sigma_N^2)t^2/2}$, hence $X\sim\mathcal N(0,\sigma_X^2)$.
3. Here $N$ is only uncorrelated with $X_g$. With $Y=X_g+N$:
$$I(X_g;X_g+N)\ge\mathbb E\log\frac{dP_{X_g|Y_g}(X_g|Y)}{dP_{X_g}(X_g)}=\mathbb E\log\frac{dP_{Y_g|X_g}(Y|X_g)}{dP_{Y_g}(Y)}\tag{5.23–5.24}$$
$$=C+\tfrac{\log e}2\,\mathbb E\Big[\tfrac{Y^2}{\sigma_X^2+\sigma_N^2}-\tfrac{N^2}{\sigma_N^2}\Big]=C+\tfrac{\log e}2\,\tfrac{\sigma_X^2}{\sigma_X^2+\sigma_N^2}\Big(1-\tfrac{\mathbb EN^2}{\sigma_N^2}\Big)\ge C.\tag{5.25–5.27}$$
(5.23) is from (4.7). (5.26) uses $\mathbb E[X_gN]=0$ and so $\mathbb EY^2=\mathbb EN^2+\sigma_X^2$. (5.27) uses $\mathbb EN^2\le\sigma_N^2$. Equality in (5.23) requires $P_{X_g|Y}=P_{X_g|Y_g}$, so $X_g=bY+cZ$ with $Z$ Gaussian independent of $Y$. Then $Y$ is Gaussian (Cramér's theorem, or characteristic functions), so $(X_g,Y)$ is jointly Gaussian and $N=Y-X_g$ is Gaussian. Equality is therefore possible only if $N$ is Gaussian of variance $\sigma_N^2$ and independent of $X_g$.

*Intuition note.* Under a power limit, Gaussian input is the best signal against Gaussian noise. Among noises of at most that power that are uncorrelated with the input, Gaussian noise gives the smallest mutual information for a Gaussian input.

### 5.6 Iterative algorithms: Blahut–Arimoto, EM, Sinkhorn
**Alternating minimization** (p. 102). To solve $\min_tf(t)$ where $f(t)=\min_sF(t,s)$ and both solvers $t^*(s)=\arg\min_tF(t,s)$, $s^*(t)=\arg\min_sF(t,s)$ exist: start from $s_0,t_0$, then $s_k=s^*(t_{k-1})$, $t_k=t^*(s_k)$. $F(s_k,t_k)$ decreases at each step. The author states that convergence to a local minimum (global under suitable conditions, e.g. convex $f$) can often be proven, referring to [113]. These large "global" jumps converge faster than gradient steps. The tool is the Gibbs variational principle (Proposition 4.7): $\min_{P_Y}D(P_Y\|Q_Y)+\mathbb E_{P_Y}[c(Y)]$ (5.28) is attained at $P^*_Y(dy)=\frac1ZQ_Y(dy)e^{-c(y)}$.

**Capacity** (p. 103). $C=\max_{P_X}\max_{Q_{X|Y}}\mathbb E\log\frac{Q_{X|Y}}{P_X}$ by (4.7). Iterations:
$$Q_{X|Y}(x|y)\leftarrow\tfrac1{Z(y)}P_X(x)P_{Y|X}(y|x),\qquad P_X(x)\leftarrow Q'(x)\triangleq\tfrac1Z\exp\Big\{\sum_yP_{Y|X}(y|x)\log Q_{X|Y}(x|y)\Big\}.$$
For fixed $P_X$ the best $Q_{X|Y}$ is $P_{X|Y}$. For fixed $Q_{X|Y}$, $\mathbb E\log\frac{Q_{X|Y}}{P_X}=\log Z-D(P_X\|Q')$, so the best $P_X$ is $Q'$. With $P_n$ the $n$-th iterate,
$$I(P_n,P_{Y|X})\le C\le\sup_xD(P_{Y|X=x}\|P_{Y|X}\circ P_n).\tag{5.29}$$
Both sides converge monotonically to $C$ (see [113]); the right side gives a computable optimality gap.

**Rate-distortion** (p. 103). $R=\min_{P_{Y|X}}I(X;Y)+\mathbb E[d(X,Y)]=\min_{P_{Y|X},Q_Y}D(P_{Y|X}\|Q_Y|P_X)+\mathbb E[d(X,Y)]$ (5.30). By (5.28): $P_{Y|X}(y|x)\leftarrow\frac1{Z(x)}Q_Y(y)e^{-d(x,y)}$, $Q_Y\leftarrow P_{Y|X}\circ P_X$. A sandwich bound like (5.29) holds (see (5.32)).

**EM, convex case** (pp. 103–104). Given $P_X$ and fixed $Q_{X|Y}$, solve $L=\min_{Q_Y}D(P_X\|Q_{X|Y}\circ Q_Y)$ (5.31); e.g. maximum likelihood for mixing weights with $P_X$ the empirical distribution. Write $\min_{Q_Y}D(P_X\|Q_X)=\min_{Q_Y}\min_{P_{Y|X}}D(P_{X,Y}\|Q_{X,Y})$, so $P_{Y|X}\leftarrow\frac1{Z(x)}Q_Y(y)Q_{X|Y}(x|y)$ and $Q_Y\leftarrow P_{Y|X}\circ P_X$. By Jensen, $D(P_X\|Q_X^{(n)})-D(P_X\|Q_X)\le\mathrm{gap}(Q_X^{(n)})$, where $\mathrm{gap}(Q_X)\triangleq\log\operatorname{esssup}_y\mathbb E_{X\sim P_X}\big[\frac{dQ_{X|Y=y}}{dQ_X}\big]$. This gives
$$D(P_X\|Q_X^{(n)})-\mathrm{gap}(Q_X^{(n)})\le L\le D(P_X\|Q_X^{(n)}).\tag{5.32}$$
Both sides converge to $L$ ([112, Thm 5.3]).

**EM, general case** (pp. 104–105). Now $Q_Y^{(\theta)}$ and $Q_{X|Y}^{(\theta)}$ depend on $\theta$, and we maximize $\sum_i\log Q_X^{(\theta)}(x_i)$. Example: $k$-component Gaussian mixture with $\theta=(w_1..w_k,\mu_1..\mu_k)$. If only the weights are unknown, this is the convex case; if the centres are also unknown it is non-convex. Using the ELBO (4.16), $\log Q^{(\theta)}_X(x_i)=\sup_P\mathbb E_{Y\sim P}\log\frac{Q^{(\theta)}_{X,Y}(x_i,Y)}{P(Y)}$, so the likelihood is $\sup_\theta\sup_{P_{Y|X}}F(\theta,P_{Y|X})$ with $F=\sum_i\mathbb E_{Y\sim P_{Y|X=x_i}}\log\frac{Q^{(\theta)}_{X,Y}(x_i,Y)}{P_{Y|X}(Y|x_i)}$. The iteration is: E-step $P_{Y|X}\leftarrow Q^{(\theta)}_{Y|X}$; M-step $\theta\leftarrow\arg\max_\theta F(\theta,P_{Y|X})$ (5.33). For non-convex log-likelihood, EM may fail to reach the global optimum even with infinite samples (example for 3-component Gaussian mixtures, [234]). If the E-step is intractable, one maximizes over a restricted class (approximate EM).

**Sinkhorn** (p. 105). Fix $Q_{X,Y}$ and marginals $V_X,V_Y$; $S=\min\{D(P_{X,Y}\|Q_{X,Y}):P_X=V_X,P_Y=V_Y\}$. By Chapter 15 results, $P^*_{X,Y}=A(x)Q_{X,Y}(x,y)B(y)$ for some $A,B\ge0$. Alternate
$$A(x)\leftarrow\frac{V_X(x)}{\sum_yQ_{X,Y}(x,y)B(y)},\qquad B(y)\leftarrow\frac{V_Y(y)}{\sum_xA(x)Q_{X,Y}(x,y)}.$$
This is the page's formulas $A(x)\leftarrow\frac{V_X(x)Q_{X,Y}(x,y)B(y)}{\sum_yQ_{X,Y}(x,y)B(y)}$ with the factor $Q_{X,Y}(x,y)B(y)$ removed from the numerator (the page keeps it, though the left side depends only on $x$); the $B$ update is likewise written on the page with $A(x)Q_{X,Y}(x,y)$ in the numerator and is shown here without it *(added step)*. The original use ($V_X=V_Y=\mathrm{Unif}[n]$) rescales rows and columns of a non-negative matrix to a doubly-stochastic one. With $Q_{X,Y}=c\exp\{-\|x-y\|^2/\epsilon\}$ the coupling approximates, as $\epsilon\to0$, the optimal-transport coupling for $W_2(V_X,V_Y)$ ([117]).

## Toy example (ours)
Binary symmetric channel, crossover $0.1$, logs base 2. Rows: $P_{Y|X=0}=\mathrm{Ber}(0.1)$ and $P_{Y|X=1}=\mathrm{Ber}(0.9)$ (probability of $Y=1$).
- Candidate centre $Q=\mathrm{Ber}(0.5)$: $D(\mathrm{Ber}(0.1)\|\mathrm{Ber}(0.5))=1-h(0.1)$, with $h(0.1)=0.1\cdot3.3219+0.9\cdot0.1520=0.4690$, so $0.531$. By symmetry the other row is also $0.531$. The rows are equidistant, so $\max_xD=0.531$.
- Uniform input gives $I=H(Y)-H(Y|X)=1-0.469=0.531$, equal to that radius, as Corollary 5.7 says.
- Other centre $Q=\mathrm{Ber}(0.4)$: $D(\mathrm{Ber}(0.9)\|\mathrm{Ber}(0.4))=0.9\log_2 2.25+0.1\log_2\frac16=0.9(1.1699)+0.1(-2.585)=1.0529-0.2585=0.794>0.531$. The other row gives $D(\mathrm{Ber}(0.1)\|\mathrm{Ber}(0.4))=0.1(-2)+0.9(0.585)=0.3265$. The worst case is $0.794$, which exceeds $C$. So $\mathrm{Ber}(0.5)$ gives the smaller worst-case divergence in this check, consistent with $\min_Q\max_x D=C$.

## Concepts
- [[saddle-point]] (new) — pair $(x^*,y^*)$ with $f(x,y^*)\le f(x^*,y^*)\le f(x^*,y)$; it implies minimax equality (p. 93)
- [[channel-capacity]] — here $\sup_{P_X\in\mathcal P}I(X;Y)$ over a convex input set; may be written as a min over outputs (p. 94)
- [[capacity-achieving-output-distribution]] (new) — unique $P^*_Y$ with $D(P_Y\|P^*_Y)\le C$ for all feasible outputs (p. 94)
- [[information-radius]] (new) — $\inf_Q\sup_xD(P_{Y|X=x}\|Q)$, equal to capacity (pp. 96–97)
- [[mutual-information]] — concave in $P_X$, convex in $P_{Y|X}$ (p. 92)
- [[relative-entropy-kl-divergence]] — jointly convex, not strictly; not a metric (pp. 91–92, 96)
- [[data-processing-inequality]] — used to prove convexity of $D$ (p. 91)
- [[exponential-family-gibbs-distribution]] — $Q_X(n)=Z(\lambda)^{-1}e^{-\lambda f(n)}$; solves max-entropy bounds (p. 100)
- [[maximum-entropy-principle]] — Example 5.2 bounds $\max H(X)$ under $\mathbb Ef(X)\le a$ (p. 100)
- [[alternating-minimization-blahut-arimoto]] (new) — alternate two exact solvers of $F(t,s)$; Blahut–Arimoto is the MI case (p. 102)
- [[expectation-maximization]] (new) — E-step sets $P_{Y|X}=Q^{(\theta)}_{Y|X}$; M-step maximizes over $\theta$ (p. 105)
- [[sinkhorn-algorithm]] (new) — alternate row and column scalings to match two marginals (p. 105)

## Canonical instances
- [[bit-flip-plus-identity-channel]] (new) — $Y_1=X_1\oplus Z_1$, $Y_2=X_2$: non-unique optimal input, unique output (p. 95)
- [[awgn-channel]] (new) — $I(X;X+Z)$ with $Z$ Gaussian; $C=\frac12\log(1+\sigma_X^2/\sigma_N^2)$ (pp. 98, 100)
- [[gaussian-mixture-model]] (new) — $k$-component mixture, the example for EM (p. 104)
- [[identity-channel-infinite-entropy]] (new) — shows finiteness of $C$ is needed in Cor. 5.5 (p. 95)

## Bridges (candidates)
- [structural-analogy] Saddle-point capacity ↔ information-theory (universal coding): a min-max over a divergence — the text only says the saddle-point result is applied later in universal data compression (p. 94).
- [structural-analogy] Capacity as KL radius ↔ metric geometry: Chebyshev radius of a set — same min-max shape, but KL is not a metric.
- [same-math] Gibbs distribution bound on max entropy ↔ maximum entropy principle in statistical physics: both give $p\propto e^{-\lambda f}$.
- [structural-analogy] EM / Blahut–Arimoto alternating steps ↔ coordinate descent: each step exactly minimizes in one block.
- [same-math] Sinkhorn scaling ↔ entropic optimal transport: $Q=c\,e^{-\|x-y\|^2/\epsilon}$ (p. 105).

## Questions this raises
- When exactly can the minimax equality fail for non-convex or non-compact input sets?
- How tight is "radius ≤ diameter" in KL (Cor. 5.8) for natural channels?
- How fast do Blahut–Arimoto iterations converge, and how large is the gap in (5.29) at finite $n$?
- Which non-Gaussian noises give the same least-favourable property under other constraints?

## Reading notes
- Printed page numbers are visible; printed = pdf − 25. The unit metadata calls this "ch06", but the pages print "Chapter 5", with sections 5.1–5.6, theorem numbers 5.1–5.11, and a starred §5.4.
- Misprint in Theorem 5.3, first proof: the last term reads $I(P^0_X,P_{Y|X})$ twice. The image shows $P^0_X$ in both places; the second should be $P^1_X$.
- Page 103 uses $c(x,y)$ for the cost in the text but $d(x,y)$ in the formulas.
- On p. 105 the printed update $A(x)\leftarrow\frac{V_X(x)Q_{X,Y}(x,y)B(y)}{\sum_yQ_{X,Y}(x,y)B(y)}$ is as shown on the page image. The left side does not depend on $y$, so the digest gives the form with that factor removed (and likewise for the $B$ update, whose printed numerator also keeps $A(x)Q_{X,Y}(x,y)$) and marks it as an added step.
- Exercises (I.37, III.27, I.9) are only cited, not printed in these pages, so no exercise list is given. Pinsker's inequality and total variation are used here without proof (promised for Chapter 7).
