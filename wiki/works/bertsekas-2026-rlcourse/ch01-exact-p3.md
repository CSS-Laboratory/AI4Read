---
id: bertsekas-2026-rlcourse/ch01-exact-p3
work: bertsekas-2026-rlcourse
unit: "1 Exact and Approximate Dynamic Programming (part 3/6), Sections 1.5–1.5.4 (start)"
pages: 56-78
fields: [control-theory]
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
# Newton's method and linear quadratic problems: approximation in value space as a Newton step

## L0 — One line
In the one-dimensional linear quadratic problem, one-step lookahead with a quadratic terminal cost approximation is one Newton step for the Riccati equation, and further lookahead steps are value iterations that only improve the Newton starting point.

## L1 — The gist (≤ 120 words)
The unit asks how good and how stable a lookahead policy is when it uses an approximate terminal cost. Using the one-dimensional linear quadratic problem, where on quadratic functions the Bellman equation is equivalent to a scalar Riccati equation, the author shows that one-step lookahead acts as a Newton step started at the terminal cost approximation. Extra lookahead steps are value iterations that improve the Newton starting point, and in general they enlarge the region of stability. Rollout is also a Newton step, and policy iteration repeats it. Classical global linear error bounds are very conservative, because they hold for every approximation, even the worst. Near the optimum the local error is superlinear in the approximation error.

**Prerequisites:** Bellman equation and value iteration; policy iteration; scalar calculus (tangent line, concavity); Newton's method for a fixed point $y=T(y)$. Terms used above: a *Newton step* solves the linearization of a fixed-point equation at the current point; *rollout* is one-step lookahead whose terminal cost is the cost of a base policy; the *region of stability* is the set of $K\ge0$ for which the one-step lookahead policy is stable; *superlinear* means the error is $o(\cdot)$ of the approximation error, i.e. their ratio tends to 0 as the approximation error tends to 0.

## L2 — Key ideas
- For the 1-D linear quadratic problem, the Bellman equation restricted to $J=Kx^2$, $K\ge0$, is the scalar Riccati equation $K=F(K)$. Its nonnegative solution $K^*$ gives $J^*=K^*x^2$ and a linear optimal policy (pp. 57–59).
- The Riccati operator $F$ is the lower envelope of linear operators $F_L$, one per linear policy $Lx$. The line $F_{\tilde L}$ for the lookahead gain $\tilde L$ is tangent to $F$ at $\tilde K$ (pp. 64–65).
- Therefore one-step lookahead from $\tilde J=\tilde Kx^2$ is a Newton step for $K=F(K)$, started at $\tilde K$. Its output $K_{\tilde L}$ is the cost coefficient of the lookahead policy if that policy is stable (pp. 65–67).
- With $\ell$-step lookahead, the effective Newton starting point is $F^{\ell-1}(\tilde K)$. Only the first step needs precision; this suggests that later steps can be simplified (within reason) with small (if any) loss (pp. 68, 70).
- The region of stability can also be viewed as the region of convergence of Newton's method; in 1-D it is $(K_S,\infty)$. It is generally true that it enlarges with lookahead length (p. 69).
- Rollout is a Newton step started at the base policy's cost. Policy iteration repeats it and converges quadratically from a stable linear start. A rollout on top of approximation in value space is a "double Newton step" (pp. 71–73).
- Global linear error bounds (1.57)–(1.58) are very conservative. The local estimate (1.59) is superlinear, and example 1.5.1 contrasts the two (pp. 75–78).

## L3 — Walkthrough

### Opening questions of the part (p. 56)
This part begins with items (b)–(d) of a list of questions about multistep lookahead. Item (a) is not in these pages.
- **(b)** How do simplifications of multistep lookahead affect $J_{\tilde\mu}$? Only the first step acts as the Newton step and needs precision. Later steps are value iterations that improve the Newton starting point, so their exact implementation is not critical. Simplifications such as certainty equivalence or tree pruning may therefore cause relatively small (if any) loss. They save on-line computation that can be spent on longer lookahead (p. 56).
- **(c)** When is $\tilde\mu$ stable? In many control applications stability is the dominant concern and optimality is secondary. The author wants to characterize the terminal cost approximations $\tilde J$ that give a stable $\tilde\mu$ (p. 56).
- **(d)** The author says it is generally true that longer lookahead (or longer truncated rollout) helps quality, and that it turns out to help stability too. The question is the mechanism (p. 56).
- These are studied first in the linear quadratic problem. The author says the conclusions hold much more generally via abstract DP (p. 56).

### 1.5 Newton's method – linear quadratic problems (pp. 56–59)
**Setup.** General form: $x_{k+1}=Ax_k+Bu_k$, with $x_k\in\Re^n$, $u_k\in\Re^m$, $A$ of shape $n\times n$, $B$ of shape $n\times m$, no control constraints. The stage cost is $g(x,u)=x'Qx+u'Ru$, with $Q$ ($n\times n$) and $R$ ($m\times m$) positive definite symmetric (p. 57). The author then restricts to one dimension, with $b\ne0$ and $q,r>0$ (p. 57):
$$x_{k+1}=ax_k+bu_k \tag{1.38}$$
$$\sum_{k=0}^\infty (qx_k^2+ru_k^2) \tag{1.39}$$

**Riccati equation.** Taking the limit of the finite-horizon Example 1.3.1, the optimal cost is expected to be quadratic (p. 57):
$$J^*(x)=K^*x^2 \tag{1.40}$$
where $K^*$ solves
$$K=F(K) \tag{1.41}$$
$$F(K)=\frac{a^2rK}{r+b^2K}+q \tag{1.42}$$
The optimal policy is linear (p. 58):
$$\mu^*(x)=L^*x \tag{1.43}$$
$$L^*=-\frac{abK^*}{r+b^2K^*} \tag{1.44}$$

**Justification** (p. 58). Show that $J^*$ satisfies the Bellman equation
$$J(x)=\min_{u\in\Re}\{qx^2+ru^2+J(ax+bu)\} \tag{1.45}$$
and that $\mu^*$ attains the minimum. For $J(x)=Kx^2$, $K\ge0$, the minimization is
$$\min_{u\in\Re}\{qx^2+ru^2+K(ax+bu)^2\} \tag{1.46}$$
which is a positive definite quadratic in $u$. Setting the derivative to zero gives $0=2ru+2bK(ax+bu)$. So the minimizer is
$$\mu_K(x)=L_Kx \tag{1.47}$$
$$L_K=-\frac{abK}{r+b^2K} \tag{1.48}$$
Substituting gives $\big(q+rL_K^2+K(a+bL_K)^2\big)x^2$. After "straightforward algebra" (not shown by the author) this equals $F(K)x^2$ (p. 58). So for $J=Kx^2$ the Bellman equation reads $Kx^2=F(K)x^2$, i.e. $K=F(K)$ (pp. 58–59). Restricted to quadratics with $K\ge0$, it is equivalent to
$$K=F(K)=\frac{a^2rK}{r+b^2K}+q \tag{1.49}$$
called the **Riccati equation**; $F$ is the **Riccati operator** (p. 59). The Riccati operator is the restriction of the Bellman operator $T$ to quadratic functions of $x$ (footnote, p. 59). $T$ maps a function $J$ to the right side of Bellman's equation.

Graphically (Fig. 1.5.1), $F$ is concave and monotonically increasing on $(-r/b^2,\infty)$ and flattens as $K\to\infty$. $K^*$ is the unique solution on the nonnegative line. A second solution $\bar K$ is negative and of no interest (pp. 59–60).

*Intuition note.* On quadratic functions with $K\ge0$, finding a function that solves the Bellman equation reduces to finding one number $K$ with $K=F(K)$. The graph of $F$ against the 45° line shows the answer.

**Stable linear policy.** Take $\mu(x)=Lx$ with $|a+bL|<1$, so $x_{k+1}=(a+bL)x_k$ converges to 0 (p. 59). Then $J_\mu(x)=K_Lx^2$ with $K_L$ solving
$$K=F_L(K) \tag{1.50}$$
$$F_L(K)=(a+bL)^2K+q+rL^2 \tag{1.51}$$
This is linear in $K$ with slope $(a+bL)^2<1$, so its graph meets the 45° line at a unique point (p. 60). It is the Bellman equation for $\mu$, $J(x)=(q+rL^2)x^2+J((a+bL)x)$, restricted to quadratics (p. 60). Solving it gives (box, p. 68)
$$K_L=\frac{q+rL^2}{1-(a+bL)^2}.$$
If $\mu$ is not stable, $|a+bL|\ge1$, then $J_\mu(x)=\infty$ for all $x\ne0$ (since $q,r>0$). The equation still has a solution, but it is negative and of no interest (p. 61).

**Value iteration (VI).** $J_{k+1}(x)=\min_u\{qx^2+ru^2+J_k(ax+bu)\}$. If $J_k=K_kx^2$ with $K_k\ge0$, then $J_{k+1}=K_{k+1}x^2$ with $K_{k+1}=F(K_k)$. From any $K_0\ge0$ the sequence $\{K_k\}$ converges to $K^*$ (Fig. 1.5.3, p. 62).

### 1.5.1 Visualizing approximation in value space; region of stability (pp. 62–70)
The author aims to show two claims (pp. 62–63):
- (a) One-step lookahead is a Newton step for the Bellman equation. It maps $\tilde J$ to the cost $J_{\tilde\mu}$ of the lookahead policy (Fig. 1.5.4).
- (b) Multistep lookahead with truncated rollout is a Newton step that maps the result of several VI iterations started at $\tilde J$ to $J_{\tilde\mu}$ (Fig. 1.5.5).

The derivation is for 1-D. The author says it applies far more generally, because the Bellman equation holds universally and the Bellman operator has a concavity property suited to Newton's method (p. 63).

**$F$ as a lower envelope.** The minimization splits into two stages (p. 64):
$$F(K)x^2=\min_{L\in\Re}\min_{u=Lx}\{qx^2+ru^2+K(ax+bu)^2\}=\min_{L\in\Re}\{q+rL^2+K(a+bL)^2\}x^2$$
hence
$$F(K)=\min_{L\in\Re}F_L(K) \tag{1.52}$$
$$F_L(K)=(a+bL)^2K+q+rL^2 \tag{1.53}$$
The graph of $F$ is the lower envelope of the lines $F_L$ (Fig. 1.5.6, p. 64). For fixed $\tilde K$, the minimizing $\tilde L=-\dfrac{ab\tilde K}{r+b^2\tilde K}$ [Eq. (1.48)] gives a line $F_{\tilde L}$ tangent to $F$ at $\tilde K$ (p. 65).

**One-step lookahead = Newton step** (pp. 65–67). Fix $\tilde J=\tilde Kx^2$, $\tilde K\ge0$. Let $\tilde\mu$ be the one-step lookahead policy. $F_{\tilde L}$ linearizes $F$ at $\tilde K$. The linearized problem is $K=F_{\tilde L}(K)=q+r\tilde L^2+K(a+b\tilde L)^2$. Its solution $K_{\tilde L}$ equals one Newton iteration for $K=F(K)$ from $\tilde K$ (Fig. 1.5.7; analytic justification in Exercise 1.7) (p. 65).
- Classical Newton for $y=T(y)$ solves the linearization $y_{k+1}=T(y_k)+\frac{\partial T(y_k)}{\partial y}(y_{k+1}-y_k)$, with $\partial T/\partial y$ the $n\times n$ Jacobian (p. 66).
- Quadratic convergence: near $y^*$, $\|y_{k+1}-y^*\|=O(\|y_k-y^*\|^2)$, assuming the Jacobian exists and is Lipschitz continuous (p. 66).
- Extensions to piecewise differentiable or component-concave $T$ keep quadratic or similarly fast superlinear convergence (p. 67).
- If $|a+b\tilde L|<1$, then $J_{\tilde\mu}(x)=K_{\tilde L}x^2$. If $\tilde\mu$ is unstable, $J_{\tilde\mu}(x)=\infty$ for all $x\ne0$ (p. 67).

*Intuition note.* The lookahead gain $\tilde L$ is the best response to the guess $\tilde K$. If the lookahead policy is stable, the cost that this gain actually achieves is found by solving the line tangent to $F$ at $\tilde K$ instead of the curve itself.

**Multistep lookahead** (pp. 67–68). For $\ell$-step lookahead, linearize $F$ at $K_{\ell-1}=F^{\ell-1}(\tilde K)$, the result of $\ell-1$ value iterations from $\tilde K$. The effective Newton starting point is $F^{\ell-1}(\tilde K)$ (Fig. 1.5.8 shows $\ell=2$).

**Formula box (p. 68), 1-D problems:**
- Riccati equation: $K=F(K)$.
- Linear policy: $K=F_L(K)$.
- Cost of a stable $Lx$: $K_L=\dfrac{q+rL^2}{1-(a+bL)^2}$.
- One-step lookahead gain for $K$ in the region of stability: $L_K=\arg\min_LF_L(K)=-\dfrac{abK}{r+b^2K}$.
- Its cost coefficient $\tilde K$ solves $\tilde K=F_{L_K}(\tilde K)$, or equivalently comes from a Newton iteration started at $K$.

**Region of stability** (p. 69). It is the set of $K\ge0$ with $|a+bL_K|<1$. It can also be viewed as the region of convergence of Newton's method. This is the set of starting points $K$ from which Newton's method for $K=F(K)$ converges to $K^*$ asymptotically, with quadratic rate near $K^*$. In 1-D it is the interval $(K_S,\infty)$, where $K_S$ is the point at which $F$ has derivative 1 (Fig. 1.5.9). For multidimensional problems it may not be characterized as easily. It is generally true that the region of stability enlarges as lookahead grows. With longer lookahead the effective starting point $F^{\ell-1}(\tilde K)$ is pushed more and more into the region. For any given $K\ge0$, the $\ell$-step lookahead policy is stable for all $\ell$ larger than some threshold. The author refers to [Ber22a], Section 3.3, and Exercises 1.8 and 1.9 (p. 69).

*Intuition note.* The author says that with longer lookahead the effective starting point is pushed more and more within the region of stability. For 1-D the region is $(K_S,\infty)$, and a starting point inside it gives a stable policy.

**General infinite-horizon problems** (p. 70). Because arbitrary state and control spaces are allowed, the Riccati operator is replaced by an abstract Bellman operator, and the graphical interpretations carry over, but only as one-dimensional pictures that motivate conjectures and analysis (p. 70).

**Importance of the first step** (p. 70). Only the first step is the Newton step; the other $\ell-1$ steps are value iterations from $\tilde J$. This suggests simplifying them, e.g. by certainty equivalence (Sections 1.6.9, 2.7.2, 2.8.3) or pruning the tree after the first step (Section 2.4). Experimentation, starting with Bertsekas–Castañon [BeC99], supports this for certainty equivalence after the first step (p. 70).

### 1.5.2 Rollout and policy iteration (pp. 70–74)
**Rollout.** Start from a stable linear base policy $\mu^0(x)=L_0x$, $|a+bL_0|<1$. Policy improvement gives the one-step lookahead policy for $\tilde J=J_\mu$ (p. 71). The rollout policy satisfies $J_{\tilde\mu}(x)\le J_\mu(x)$ for all $x$ (read from Fig. 1.5.10), so it is stable, since $\mu$ is assumed stable and hence $J_\mu(x)<\infty$ for all $x$ (p. 71):
$$J_{\mu^0}(x)=K_0x^2 \tag{1.54}$$
$$K_0=\frac{q+rL_0^2}{1-(a+bL_0)^2} \tag{1.55}$$
$$L_1=-\frac{abK_0}{r+b^2K_0} \tag{1.56}$$
with $\mu^1(x)=L_1x$ (p. 71). The quadratic coefficient of the rollout policy comes from that of the base policy by a Newton step (Fig. 1.5.10).

**Policy iteration (PI)** is repeated nontruncated rollout: $L_{k+1}=-\frac{abK_k}{r+b^2K_k}$, $K_k=\frac{q+rL_k^2}{1-(a+bL_k)^2}$, and $J_{\mu^k}=K_kx^2$ (p. 72). From a linear stable initial policy, classical LQ theory gives $J_{\mu^k}\to J^*$ and $\mu^k\to$ optimal, with quadratic convergence of $\{K_k\}$. Kleinman [Kle68] proved this for the continuous-time multidimensional version, crediting Bellman and Kalaba [BeK65] for 1-D (p. 72).

**Truncated rollout** (p. 72). With a stable linear base policy $\mu$, $m$ rollout steps, one-step lookahead and $\tilde J=\tilde Kx^2$: start at $\tilde K$, execute $m$ VI steps using $\mu$, then take a Newton step (Fig. 1.5.11, $m=4$). The author recalls from Section 1.1 that (a) lookahead by rollout may economically substitute for lookahead by minimization, and (b) rollout with a stable policy helps the lookahead policy's stability. These are difficult to establish analytically in generality. They can be understood intuitively in the 1-D problem and are consistent with experiments (p. 73).

**Double Newton step** (pp. 73–74). Take $\tilde\mu(x)=L_{\tilde K}x$ and use it as the base policy for rollout. This is a Newton step started from the result of the Newton step started at $\tilde K$ (Fig. 1.5.12). The author says it is much more powerful than two-step lookahead from $\tilde K$, which is a VI followed by a Newton step, and that it extends to general infinite-horizon problems. A truncated variant is the 1996 TD-Gammon architecture [TeG96], whose base policy uses a terminal cost approximation trained off-line with a neural network (p. 74).

### 1.5.3 Local and global error bounds (pp. 74–78)
**Global (linear) bounds.** For an $\alpha$-discounted problem with finite state space $X$ and maximum norm, one-step lookahead satisfies (p. 74)
$$\|J_{\tilde\mu}-J^*\|\le\frac{2\alpha}{1-\alpha}\|\tilde J-J^*\| \tag{1.57}$$
Viewing $\ell$-step lookahead as one-step lookahead with terminal cost $T^{\ell-1}\tilde J$ ($\tilde J$ after $\ell-1$ value iterations) gives (p. 75)
$$\|J_{\tilde\mu}-J^*\|\le\frac{2\alpha^\ell}{1-\alpha}\|\tilde J-J^*\| \tag{1.58}$$
These apply beyond the discounted case, to problems where the Bellman equation involves a contraction over a subset of functions (Fig. 1.5.13, p. 75).

**Local (superlinear) estimate.** The author says the linear bounds are very conservative and do not reflect practice, "even qualitatively". The main reason is that they are global: they hold for all $\tilde J$, even the worst possible (p. 75). In practice $\tilde J$ is often close to $J^*$, and then the error behaves like the Newton step (p. 75):
$$\|J_{\tilde\mu}-J^*\|=o\big(\|\tilde J-J^*\|\big) \tag{1.59}$$
The performance error rises rapidly outside the region of superlinear convergence. Small improvements in $\tilde J$ (better sampling, improved confidence intervals, same architecture) have little effect both inside and outside it (p. 75).

Fig. 1.5.14 caption (p. 76):
- Its drawing is not realistic: the real region of convergence is unbounded and contains lines $\gamma e$ ($e$ the vector of ones).
- The region expands as $\ell$ grows.
- With long enough $\ell$, the lookahead policy can be shown to be exactly optimal for many problems of interest. This is known since the 60s–70s for $\alpha$-discounted finite-state problems (p. 76).

The author says the linear bounds often misdirect academic research and confuse practitioners (p. 76). Footnote: a study by Laidlaw, Russell and Dragan on 155 problems found that "prior bounds do not correlate well with when deep RL succeeds vs. fails". It also supports the value of long lookahead, the required $\ell$ depending on $\tilde J-J^*$ (p. 76).

**Example 1.5.1** (pp. 77–78). 1-D LQ problem, one-step lookahead, $\tilde J=\tilde Kx^2$ with $\tilde K$ in the region of stability $(S,\infty)$. $K_{\tilde\mu}$ is the result of one Newton step from $\tilde K$.
- $S$ solves $\frac{\partial F}{\partial K}\big|_{K=S}=1$.
- For $\bar S>S$, $F$ is a contraction on $[\bar S,\infty)$ with modulus $\alpha=\frac{\partial F}{\partial K}\big|_{K=\bar S}\in(0,1)$. The derivative is positive and decreases to 0 as $K\to\infty$ (p. 78).
- Bound (1.57), rewritten for quadratic coefficients (p. 78):
$$K_{\tilde\mu}-K^*\le\frac{2\alpha}{1-\alpha}|\tilde K-K^*| \tag{1.60}$$
- Data: $a=2,b=2,q=1,r=5$, so $K^*=5$ and $S=1.25$. In the figure $\bar S=S+0.5$. The actual error $K_{\tilde\mu}-K^*$ follows Newton behavior and is much smaller when $\tilde K>K^*$ than when $\tilde K<K^*$, because the slope of $F$ decreases as $K$ grows. The bound does not show this (Fig. 1.5.15, p. 77).
- The bound depends on $\alpha$, hence on how close $\tilde K$ is to $S$. The local Newton behavior does not depend on $S$ (p. 78).

### 1.5.4 How approximation in value space can fail (start, p. 78)
When $\tilde J$ is trained from data with an architecture such as a neural network (as in AlphaZero and TD-Gammon), the approximation error $\tilde J-J^*$ has three components. Two are in this part: (a) the power of the architecture, i.e. the representation error that would remain even with infinite data used optimally; (b) the error degradation due to limited training data (p. 78). The list continues in the next part.

## Toy example (ours; data borrowed from the author's Fig. 1.5.15, all computations ours)
Take $a=2,b=2,q=1,r=5$, so $F(K)=\dfrac{20K}{5+4K}+1$ and $F'(K)=\dfrac{100}{(5+4K)^2}$.
- Check $K^*=5$: $F(5)=100/25+1=5$. Boundary $S$: $F'(S)=1\Rightarrow 5+4S=10\Rightarrow S=1.25$.
- **One-step lookahead from $\tilde K=2.5$.** $F(2.5)=50/15+1=13/3$. $\tilde L=-\dfrac{4\cdot2.5}{5+4\cdot2.5}=-\dfrac{10}{15}=-\dfrac23$, and $a+b\tilde L=2-\dfrac43=\dfrac23$, which is stable. Check of $F(\tilde K)$ by the minimization form: $q+r\tilde L^2+\tilde K(a+b\tilde L)^2=1+\dfrac{20}9+2.5\cdot\dfrac49=1+\dfrac{20}9+\dfrac{10}9=\dfrac{39}9=\dfrac{13}3$ ✓.
- Cost coefficient: $K_{\tilde L}=\dfrac{1+5\cdot4/9}{1-4/9}=\dfrac{29/9}{5/9}=5.8$.
- Newton check (added step): $F'(2.5)=100/225=4/9=(a+b\tilde L)^2$, the tangent slope. The tangent line is $K=\frac{13}3+\frac49(K-2.5)$, so $\frac59K=\frac{13}3-\frac{10}9=\frac{29}9$ and $K=5.8$ ✓.
- Errors: starting error $|2.5-5|=2.5$; after the Newton step $5.8-5=0.8$.
- **Two-step lookahead** (one VI first): $K_1=F(2.5)=13/3$. Then $L=-\dfrac{4\cdot13/3}{5+52/3}=-\dfrac{52}{67}$, $a+bL=\dfrac{30}{67}$, $(a+bL)^2=\dfrac{900}{4489}$. So $K_L=\dfrac{1+5\cdot2704/4489}{1-900/4489}=\dfrac{18009}{3589}\approx5.018$. The error falls to about $0.018$, so the improved starting point helps.
- **Stability.** From $\tilde K=1<S$: $L=-\frac49$, $a+bL=\frac{10}9>1$, unstable. With $\ell=2$: $K_1=F(1)=\frac{20}9+1=\frac{29}9\approx3.22>S$, and $F'(29/9)=\frac{8100}{25921}\approx0.31<1$ (the slope of the tangent line, i.e. $(a+bL)^2$ for $L=L_{K_1}$), so the policy is stable.

## Concepts
- [[bellman-equation-value-function]] — fixed-point equation for the cost; here restricted to $J=Kx^2$ it becomes $K=F(K)$ (pp. 58–59).
- [[riccati-equation]] (new) — scalar equation $K=F(K)$, $F(K)=\frac{a^2rK}{r+b^2K}+q$; $F$ is the Riccati operator (p. 59).
- [[bellman-operator]] (new) — maps $J$ to the right side of Bellman's equation; Riccati operator is its restriction to quadratics (footnote, p. 59).
- [[newton-step-approximation-in-value-space]] (new) — one-step lookahead from $\tilde J$ equals one Newton iteration for the Bellman or Riccati equation (pp. 62–65).
- [[approximation-in-value-space]] (new) — choose actions by minimizing stage cost plus an approximate terminal cost $\tilde J$ (p. 62).
- [[multistep-lookahead]] (new) — $\ell$-step lookahead: $\ell-1$ VI steps improve the Newton starting point $F^{\ell-1}(\tilde K)$ (p. 68).
- [[value-iteration]] (new) — repeatedly minimizing stage cost plus $J_k$; for LQ, $K_{k+1}=F(K_k)$ (p. 61).
- [[policy-iteration]] (new) — repeated nontruncated rollout; converges quadratically from a stable linear policy (p. 72).
- [[rollout]] (new) — one-step lookahead with $\tilde J=J_\mu$ of a base policy; improves on it, so is stable if $\mu$ is (p. 71).
- [[double-newton-step]] (new) — rollout using as base the lookahead policy of $\tilde K$ (p. 73).
- [[region-of-stability]] (new) — set of $K\ge0$ with $|a+bL_K|<1$; also Newton's region of convergence (p. 69).
- [[stability]] — here: $|a+bL|<1$, so $x_{k+1}=(a+bL)x_k$ tends to 0 (p. 59).
- [[global-vs-local-error-bound]] (new) — linear bound (1.57)–(1.58) for all $\tilde J$ versus local $o(\cdot)$ estimate (1.59) (pp. 75–76).
- [[certainty-equivalence]] (new) — a simplification of later lookahead steps; discussed later in the book (p. 70).
- [[policy]] — here a linear feedback $\mu(x)=Lx$ (p. 58).

## Canonical instances
- [[lq-1d-problem]] — scalar system $x_{k+1}=ax_k+bu_k$ with cost $qx^2+ru^2$ (pp. 57–58).
- [[example-1-5-1]] — $a=b=2,q=1,r=5$: global bound versus actual one-step error (pp. 77–78).
- [[td-gammon]] — truncated rollout with a base policy from a neural-network terminal cost (p. 74).
- [[kleinman-pi-convergence]] — PI converges to the optimum from a stable linear start (p. 72).

## Bridges (candidates)
- [same-math] Riccati operator fixed point $K=F(K)$ and its optimal gain $L^*$ ↔ control-theory LQR: the scalar LQR solution (the unit does not use the word LQR).
- [same-math] one-step lookahead as a Newton step ↔ numerical analysis: Newton's method on a fixed point with a concave map (pp. 65–66).
- [structural-analogy] region of stability = region of convergence of Newton's method ↔ dynamical systems: basin of attraction of a fixed point.
- [structural-analogy] first step precise, later steps only enhance the starting point ↔ model predictive control: apply only the first step of a finite-horizon solution (canon link; not stated in this unit).
- [metaphor] linear global bounds versus local superlinear error ↔ worst-case versus typical-case analysis in learning theory.

## Questions this raises
- In several dimensions, when does $\tilde J$ lie in the region of stability, and how does it enlarge with $\ell$?
- How much accuracy is lost when certainty equivalence replaces exact minimization after the first step?
- How large must $\ell$ be for exact optimality, given the approximation error $\tilde J-J^*$ (p. 76)?
- Which of the three error components in 1.5.4 matters most in practice?

## Exercises worth doing
(These are referenced but not printed in these pages; contents are inferred from the text.)
- Ex. 1.7 (p. 65) — analytic proof that $K_{\tilde L}$ is one Newton iteration from $\tilde K$ — difficulty: medium.
- Ex. 1.8 and 1.9 (p. 69) — region of stability and role of multistep lookahead — difficulty: medium.

## Reading notes
- This part starts at item (b) of the list of questions on p. 56, which continues from the previous part. It ends in Section 1.5.4 on p. 78, after item (b) of the list of error components; item (c) and the rest are in the next part.
- Printed = pdf − 20.
- Text layer: $\Re$ appears as "+" or "'", "≠" as "%=", "∞" as "↑", the fraction minus signs and $\ell-1$ superscripts are garbled. All equations were checked against the images.
- Misprints: on pp. 69 and 78 the images show "Riccati equation $F=F(K)$", which should be $K=F(K)$. The Fig. 1.5.2 caption (p. 61) has a garbled phrase, "but the equation has $K=F_L(K)$ still has…".
- The author omits the algebra in the justification of (1.42) ("straightforward algebra", p. 58) and defers the Newton-step proof to Exercise 1.7.
