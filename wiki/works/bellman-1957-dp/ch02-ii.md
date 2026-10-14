---
id: bellman-1957-dp/ch02-ii
work: bellman-1957-dp
unit: "Chapter II. A Stochastic Multi-Stage Decision Process"
pages: 61-80
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# A Stochastic Multi-Stage Decision Process (the two-mine gold-mining problem)

## L0 — One line
In the two-mine gold-mining problem, the functional equation shows the optimal first choice is the mine with the larger ratio of immediate expected gain to immediate expected loss, which splits the $(x,y)$-quadrant into two "decision regions" bounded by one straight line.

## L1 — The gist (≤ 120 words)
A delicate machine mines one of two mines, Anaconda or Bonanza. Each use either yields a fixed fraction of that mine's gold or destroys the machine. Which sequence of choices maximizes expected gold? Bellman writes a functional equation for the optimal expected return. He proves existence by successive approximations; the uniqueness proof is left to the reader. He then finds the policy: use A when $p_1r_1x/(1-p_1)$ exceeds $p_2r_2y/(1-p_2)$, otherwise B. Two regions persist for finite horizons, and a similar ratio rule is stated for several generalizations. With a third, compromise choice the simple structure fails, as a counter-example shows. A stability theorem ends the main text (exercises follow).

**Prerequisites:** expected value; geometric series; maxima of functions; uniform convergence and successive approximations; homogeneous functions; lines through the origin.

## L2 — Key ideas (5–10 bullets)
- The expected return $f(x,y)$ of the unbounded process satisfies a one-function equation. It is the limit of the finite-horizon returns $f_N$ (pp. 63, 65).
- If $|p_i|<1$ and $0\le r_i<1$, the equation has a unique bounded solution, continuous in any finite part of $x,y\ge0$. The proof shows successive differences shrink geometrically (pp. 64–65).
- Because $f(kx,ky)=kf(x,y)$, the choice depends only on $x/y$. If the sets are well-behaved, decision regions are therefore sectors bounded by lines through the origin (p. 66).
- The boundary $L$ is found without knowing $f$: on $L$, the order AB versus BA is immaterial. This gives $p_1r_1x/(1-p_1)=p_2r_2y/(1-p_2)$ (pp. 67–69).
- Interpretation: at each step choose the action with the larger ratio of immediate expected gain to immediate expected loss. Theorems 3–4 extend this to many outcomes and many mines (pp. 69–70).
- For finite $N$ there are still two decision regions. They coincide with those of $f$ once $N\ge N_0$ (pp. 72–74).
- A third "compromise" choice can produce a pattern like B, A, C, A, so the simple solution does not extend. Much about it is unknown (pp. 74–76).
- Stability: a perturbation $h$ of the equation changes the solution by at most $\max_R|h|/q$ on a rectangle $R$ (p. 76).

## L3 — Walkthrough

### §1–§3. Problem and enumeration (pp. 61–62)
Bellman uses this process to introduce "decision regions". The plan follows Chapter I: statement, functional equation, existence and uniqueness, then properties (p. 61). The simple solution found here does not extend to more general processes of this class. A counter-example exists, and Lemma 8 of Chapter 8 also shows it (p. 61).

**Process (§2).** Anaconda holds gold $x$ and Bonanza holds $y$. There is a single machine, and a choice of mine is made before each operation (p. 62).
- Using it in Anaconda: with probability $p_1$ it mines a fraction $r_1$ of the gold there and stays in order. With probability $1-p_1$ it mines nothing and is destroyed.
- Bonanza has $p_2,r_2$ in the same way.
- Operation ends when the machine is damaged. The question is which sequence of choices maximizes the gold mined (p. 62).

**Enumeration (§3).** A stochastic policy has no single return, so it is valued by an average, here the expected value (p. 62). A policy is a sequence such as $S=AABBBABB\ldots$, read as "A, then A if undamaged, then B if still undamaged…" (p. 62). For an $N$-step process one can list all policies. This is a brute-force method that does not reveal the optimal structure; a 10-stage binary process needs $2^{10}=1024$ policies (p. 62).

### §4. Functional equation for $N$ stages (p. 63)
$f_N(x,y)$ = expected gold mined when the optimal policy of at most $N$ stages is used (p. 63).

$$f_1(x,y)=\max[p_1r_1x,\;p_2r_2y]\tag{4.2}$$

Whatever the first choice, the continuation over $N$ stages must be optimal (p. 63):
$$f_A(x,y)=p_1\bigl(r_1x+f_N((1-r_1)x,y)\bigr),\qquad f_B(x,y)=p_2\bigl(r_2y+f_N(x,(1-r_2)y)\bigr)\tag{4.3, 4.4}$$
$$f_{N+1}(x,y)=\max[f_A,f_B]\tag{4.5}$$

### §5. Infinite-stage approximation (p. 63)
The unbounded process is an approximation to a finite one with large $N$. Its return, if it exists, satisfies
$$f(x,y)=\max\bigl[p_1(r_1x+f((1-r_1)x,y)),\;p_2(r_2y+f(x,(1-r_2)y))\bigr]\tag{5.1}$$
Existence and uniqueness must now be proved (p. 63).

### §6. Existence and uniqueness (pp. 64–65)
**Theorem 1.** Assume (a) $|p_1|,|p_2|<1$ and (b) $0\le r_1,r_2<1$. Then (5.1) has a unique solution bounded in any rectangle $0\le x\le\bar X$, $0\le y\le\bar Y$. It is continuous in any finite part of $x,y\ge0$ (p. 64). Footnote 2: in this process the $p_i$ are nonnegative, but the proof covers the more general equation (p. 64).

**Proof.** Set $T_1(f)=p_1[r_1x+f((1-r_1)x,y)]$ and $T_2(f)=p_2[r_2y+f(x,(1-r_2)y)]$. Then $f=\max[T_1(f),T_2(f)]$ (p. 64). Define $f_1$ as in (4.2) and $f_{N+1}=\max_{i=1,2}T_i(f_N)$, as in (4.5). Let $i(N)$ be an index attaining the maximum for $f_N$. Then (p. 64):
$$f_{N+1}=T_{i(N)}(f_N)\ge T_{i(N+1)}(f_N),\qquad f_{N+2}=T_{i(N+1)}(f_{N+1})\ge T_{i(N)}(f_{N+1})$$
Hence (p. 65)
$$|f_{N+1}-f_{N+2}|\le\max\bigl[|T_{i(N)}(f_N)-T_{i(N)}(f_{N+1})|,\;|T_{i(N+1)}(f_N)-T_{i(N+1)}(f_{N+1})|\bigr]\le\max_{i}|T_i(f_N)-T_i(f_{N+1})|$$
$$\le\max\bigl[|p_1||f_N((1-r_1)x,y)-f_{N+1}((1-r_1)x,y)|,\;|p_2||f_N(x,(1-r_2)y)-f_{N+1}(x,(1-r_2)y)|\bigr]\tag{6}$$
Define
$$u_N(x,y)=\max_{0\le s\le x,\;0\le t\le y}|f_N(s,t)-f_{N+1}(s,t)|\tag{7}$$
The points $((1-r_1)x,y)$ and $(x,(1-r_2)y)$ lie in the rectangle $[0,x]\times[0,y]$ (added step). So (6) gives
$$u_{N+1}(x,y)\le q\,u_N(x,y),\qquad q=\max(|p_1|,|p_2|)<1\tag{8}$$
Thus $\sum_N u_N$ converges uniformly in any bounded rectangle. So $f_N\to f$ uniformly, $f$ satisfies (5.1), and $f$ is continuous in any bounded rectangle (p. 65). Uniqueness follows the proof of Theorem 1 of Chapter 1 and is left as an exercise (p. 65). The starting function $f_1$ can be any function bounded in finite rectangles. By uniqueness, the limit is continuous even if the initial function is not (p. 65).

*Intuition note.* Each step of the recursion shrinks the gap between successive approximations by at least the factor $q$, because survival probability is below 1. So the approximations settle down to a limit function; the theorem asserts that the solution is unique, with that proof left to the reader.

### §7. Approximation in policy space (pp. 65–66)
If $p_1,p_2\ge0$, monotone convergence can be ensured by approximation in policy space. The two simplest starting policies are $A^\infty$ and $B^\infty$ (p. 65):
$$f_A(x,y)=\frac{p_1r_1x}{1-p_1(1-r_1)},\qquad f_B(x,y)=\frac{p_2r_2y}{1-p_2(1-r_2)}\tag{7.1, 7.2}$$
Footnote 3: $A^\infty$ is conditional as far as the process is concerned, but deterministic as far as the equation is concerned (p. 65). Bellman says §8–§9 give a more sophisticated way to get a first approximation for more complicated processes (p. 66).

### §8. The solution (pp. 66–69)
Take $0\le p_1,p_2<1$. Bellman says it is intuitively clear that A is chosen when $x/y\gg1$ and B when $y/x\gg1$ (p. 66). Since $f(kx,ky)=kf(x,y)$ for $k>0$, the choice depends only on $x/y$. The quickest proof invokes uniqueness (p. 66). So if $(x,y)$ is in the A-set, so is $(kx,ky)$ for all $k>0$, and likewise for the B-set. If these sets are well-behaved, their boundaries are straight lines through the origin (Figure 1: several alternating sectors) (p. 66). He conjectures two regions, A below a line $L$ and B above it (Figure 2) (p. 67).

*Finding $L$.* $L$ is the line on which A and B are equally optimal. Writing $f_A$ and $f_B$ for A or B first with optimal continuation (p. 67):
$$f_A=p_1r_1x+p_1f((1-r_1)x,y),\qquad f_B=p_2r_2y+p_2f(x,(1-r_2)y)\tag{8.1, 8.2}$$
Equating these is of little use, since $f$ is unknown. Instead, on $L$ the machine's first use of A decreases $x$ and so leads into the B-region, and a first use of B leads into the A-region. So on $L$, first-A is equivalent to AB, and first-B is equivalent to BA (p. 67):
$$f_{AB}=p_1r_1x+p_1p_2r_2y+p_1p_2f((1-r_1)x,(1-r_2)y)\tag{8.3}$$
$$f_{BA}=p_2r_2y+p_1p_2r_1x+p_1p_2f((1-r_1)x,(1-r_2)y)\tag{8.4}$$
Footnote 5: after surviving both choices, the original order no longer matters for the continuation (p. 67). Equating, $f$ cancels:
$$\frac{p_1r_1x}{1-p_1}=\frac{p_2r_2y}{1-p_2}\tag{8.5}$$

*Rigorous proof (pp. 68–69).* For $y=0$, (5.1) gives $f(x,0)=\max[p_1r_1x+p_1f((1-r_1)x,0),\,p_2f(x,0)]=p_1r_1x+p_1f((1-r_1)x,0)$ (8.6). The $B$-term is smaller strictly. By continuity in $y$, $f(x,y)>p_2(r_2y+f(x,(1-r_2)y))$ for $0\le y\le kx$, some small $k>0$ (8.7). So A is optimal first in a region near the x-axis (Figure 3). Take $P$ between $L$ and $y=kx$ such that $(x,(1-r_2)y)$ lies in that A-region. If B were optimal at $P$, then $f=f_{BA}$ by (8.8). But below $L$, $f_{BA}<f_{AB}$, so B is not optimal. Proceeding inductively, the A-region extends up to $L$. The same argument gives the B-region between $L$ and the y-axis (p. 69).

**Theorem 2.** Let $f(x,y)=\max\{p_1[r_1x+f((1-r_1)x,y)],\,p_2[r_2y+f(x,(1-r_2)y)]\}$ with $x,y\ge0$, $0\le p_1,p_2<1$ and $0\le r_1,r_2\le1$. Then $f$ equals the A-expression when $p_1r_1x/(1-p_1)>p_2r_2y/(1-p_2)$. It equals the B-expression when the inequality is reversed. When the two sides are equal, either choice is optimal (p. 69).

*Intuition note.* The orders AB and BA cannot be told apart by the unknown future, because after both A and B have been survived the future is the same. Only the first two moves matter, and their comparison gives a formula free of $f$.

### §9. Discussion (p. 69)
Bellman calls $p_1r_1x$ the immediate expected gain and $(1-p_1)$ the immediate expected loss. The theorem says to make, at each instant, the decision that maximizes the ratio of immediate expected gain to immediate expected loss. He says this criterion occurs from time to time in dynamic programming (p. 69).

### §10. Generalizations (pp. 69–70)
Bellman says the same methods prove two more results.
- **Theorem 3.** Equation with A: $\sum_{k=1}^N p_k[c_kx+f(c'_kx,y)]$ and B: $\sum_{k=1}^N q_k[d_ky+f(x,d'_ky)]$. Conditions: $p_k,q_k\ge0$, $\sum p_k<1$, $\sum q_k<1$; $1\ge c_k,d_k\ge0$; $c'_k+c_k=d'_k+d_k=1$. The rule: choose A if
$$\frac{\sum_k p_kc_k}{1-\sum_k p_k}\,x>\frac{\sum_k q_kd_k}{1-\sum_k q_k}\,y\tag{10.3}$$
Choose B if reversed; either at equality (p. 70).
- **Theorem 4.** For $n$ mines, with $f(x_1,\dots,x_n)=\max_i\sum_{k=1}^K p_{ik}[c_{ik}x_i+f(x_1,\dots,c'_{ik}x_i,\dots,x_n)]$, $p_{ik}\ge0$, $\sum_kp_{ik}<1$, $1\ge c_{ik}\ge0$, $c_{ik}+c'_{ik}=1$. The decision functions are
$$D_i(x)=\frac{\sum_{k}p_{ik}c_{ik}}{1-\sum_{k}p_{ik}}\,x_i$$
The optimal index is the $i$ maximizing $D_i$. Equality means indifference (p. 70).

Theorems 3 and 4 can be combined and generalized with Stieltjes integrals, e.g. $f(x,y)=\max\bigl[\int_0^1(zx+f((1-z)x,y))dG(z),\;\int_0^1(wy+f(x,(1-w)y))dH(w)\bigr]$. Derivations and the existence and uniqueness proofs are left as exercises (p. 70).

### §11. The form of $f(x,y)$ (pp. 71–72)
In general $f$ has no simple analytic form. Take
$$f(x,y)=\max\begin{bmatrix}a_1x+a_2y+p_2f(c_2x,y)\\ b_1x+b_2y+q_2f(x,d_2y)\end{bmatrix}\tag{11.1}$$
If $c_2^m=d_2^n$ with $m,n$ positive integers, a piecewise-linear $f$ can be obtained (p. 71). He treats the simplest case $c_2=d_2$ (p. 71). Let $L_1$ be the line that A maps onto $L$, $L_2$ the line mapped onto $L_1$, and so on. Let $M_1$ be the line that B maps onto $L$ (Figure 4). In the sector $LOL_1$, A is used first and then B (p. 71). Then (11.2):
$$f=a_1x+a_2y+p_2f(c_2x,y)=a_1x+a_2y+p_2(b_1c_2x+b_2y)+p_2q_2f(c_2x,c_2y)$$
$$=(a_1+p_2b_1c_2)x+(a_2+p_2b_2)y+p_2q_2c_2f(x,y)$$
The last step uses $f(c_2x,c_2y)=c_2f(x,y)$ (homogeneity, added step). Solving (p. 72):
$$f(x,y)=\frac{(a_1+p_2b_1c_2)x+(a_2+p_2b_2)y}{1-p_2q_2c_2}\quad\text{in }LOL_1\tag{11.3}$$
Footnote 6 gives the boundary line for this equation as $[a_1(1-q_2)+b_1(p_2c_2-1)]x=[b_2(1-p_2)+a_2(q_2d_2-1)]y$ (p. 71). A linear expression is obtained likewise in $LOM_1$, $L_1OL_2$ and so on (p. 72).

### §12. Finite number of stages (pp. 72–74)
**Theorem 5.** For the recurrence $f_1=\max\{p_1r_1x,p_2r_2y\}$, $f_{N+1}=\max\{A:p_1[r_1x+f_N((1-r_1)x,y)],\,B:p_2[r_2y+f_N(x,(1-r_2)y)]\}$, there are two decision regions for each $N$ (p. 72).

*Proof outline.* For $N\ge2$, points where AB plus optimal $(N-2)$-move continuation equals BA plus the same lie on $L:\ p_1r_1x/(1-p_1)=p_2r_2y/(1-p_2)$ (p. 72). Any optimal $N$-stage policy has the form $S_N:A^{a_1}B^{b_1}\dots A^{a_N}B^{b_N}$ with $a_i,b_i\ge0$ integers and $\sum(a_i+b_i)=N$ (p. 72).

Take $P$ above $L$. If A is used there, either $S_N=A^kB\dots$ with $1\le k\le N-1$, or $S_N=A^N$. In the first case, after $k-1$ A's we reach $P'$ further above $L$. There AB cannot be the first two moves of an optimal $(N-k+1)$-stage policy, since BA plus an optimal continuation is better. So above $L$, either B is first or the optimal policy is $A^N$ (p. 73).

If $A^N$ is optimal at $P$, it is optimal between $OP$ and the x-axis. By homogeneity we may take $x+y=1$. Each of the $2^N$ policies gives a return linear in $x,y$, so a set of $2^N$ straight lines is plotted (Figures 5, 6) (p. 73). $A^N$ is optimal at $y=0,x=1$. So if it is optimal at $(\bar x,\bar y)$ with $0<\bar y<1$, its line dominates all others for $\bar x\le x\le1$ (p. 74). Thus for any $N$ the A/B boundary is either $AB=BA$, or $A^N=M_1$ with $M_1$ a complicated policy, or $B^N=M_2$, also complicated (p. 74).

**Theorem 6.** The decision regions for $f_N$ converge to those of $f$ monotonically as $N\to\infty$. There is an integer $N_0$ with the regions for $f_N$ identical to those of $f$ for $N\ge N_0$ (p. 74).

*Proof for $N=3$ (p. 74).* Let $L_2$ be the two-stage boundary, assumed to lie above $L$ (Figure 7). Let $L_2(A^{-1})$ be the line sent into $L_2$ when A is used (the text writes $(x,y)\to(cx,y)$). Take $Q$ between $L_2$ and $L_2(A^{-1})$. If A is used first at $Q$, B comes next, since the transformed point is in the two-stage B-region. But above $L$, AB cannot be the first two moves of an optimal policy. So B is used at $Q$. Hence the three-stage B-region contains at least the region above $L_2(A^{-1})$. This continues until, for some finite $k$, $L_k(A^{-1})$ lies below $L$. Then the boundary is $AB=BA$ and stays so for larger $N$ (p. 74).

*Intuition note.* Short horizons can distort the boundary. Each extra stage moves it toward $L$, and after finitely many stages it equals $L$.

### §13. A three-choice problem (pp. 74–76)
Add choice C, a compromise between A and B (p. 75):
$$C:\ p_3[r_3x+r_4y+f((1-r_3)x,(1-r_4)y)]$$
with $0\le r_3,r_4\le1$, $0\le p_3<1$. One might suspect three regions with C in the middle (Figure 8). A counter-example shows this is not true in general: for suitable parameter values the regions can be B, A, C, A from the y-axis to the x-axis (Figure 9). The calculation is described as complicated but straightforward and is not given (p. 75). The solution seems a difficult problem. It is not even known whether the number of regions is always finite, or uniformly bounded if finite (p. 76). For a continuous version, treated in Chapter 8 with variational techniques, the regions do take the simple form of Figure 8 (p. 76).

### §14. Stability (pp. 76–77)
"Solution" means the unique solution in the appropriate function class (footnote 7, p. 76).

**Theorem 7.** Let $g$ solve (14.1) with an added term: $g=\max[A:p_1(r_1x+g((1-r_1)x,y)),\,B:p_2(r_2y+g(x,(1-r_2)y))]+h(x,y)$. Then in any rectangle $R$: $0\le x\le\bar X$, $0\le y\le\bar Y$:
$$|f(x,y)-g(x,y)|\le\max_R|h(x,y)|/q,\qquad q=\min\{(1-p_1),(1-p_2)\}\tag{14.3}$$
The text does not restate conditions on $p_i$ here (p. 76).

*Proof sketch.* Successive approximations: $f_1=\max[p_1r_1x,p_2r_2y]$, $g_1=f_1+h$, and $f_{n+1},g_{n+1}$ by the same recursion, with $g_{n+1}$ also having $+h$ (p. 76). Clearly $|f_1-g_1|\le\max_R|h|$ (14.6). With $p_3=\max(p_1,p_2)$ (p. 77):
$$\max_R|f_{n+1}-g_{n+1}|\le p_3\max_R|f_n-g_n|+\max_R|h|\tag{14.7}$$
Iterating:
$$\max_R|f_n-g_n|\le\max_R|h|\,(1+p_3+\dots+p_3^{n-1}),\quad n=2,\dots\tag{14.8}$$
Letting $n\to\infty$ gives the bound. (Added step: $1/(1-p_3)=1/q$.) (p. 77)

*Intuition note.* A bounded error $h$ added at every stage accumulates only like a geometric series. Because the process is discounted by survival probability, small errors cannot grow without bound.

## Toy example (ours, not from the text)
Take $p_1=0.5,\ r_1=0.5$ (Anaconda) and $p_2=0.75,\ r_2=0.5$ (Bonanza), with $x=4,\ y=2$.

- **Immediate expected gain:** $p_1r_1x=0.5\cdot0.5\cdot4=1$ for A; $p_2r_2y=0.75\cdot0.5\cdot2=0.75$ for B. A looks better at first sight.
- **Ratio index (Theorem 2):** A: $1/(1-0.5)=2$. B: $0.75/(1-0.75)=3$. The rule says choose B.
- **Check with the AB vs BA argument.** The continuation after surviving both is identical, so compare only the first two moves.
  - AB gives $p_1r_1x+p_1p_2r_2y=1+0.5\cdot0.75\cdot0.5\cdot2=1+0.375=1.375$.
  - BA gives $p_2r_2y+p_1p_2r_1x=0.75+0.5\cdot0.75\cdot0.5\cdot4=0.75+0.75=1.5$.
  - BA is better by $0.125$, as the rule predicts.
- **Identity (added step):** $f_{AB}-f_{BA}=p_1r_1x(1-p_2)-p_2r_2y(1-p_1)=(1-p_1)(1-p_2)\bigl[\tfrac{p_1r_1x}{1-p_1}-\tfrac{p_2r_2y}{1-p_2}\bigr]$. Numerically: $0.25-0.375=-0.125$ and $0.5\cdot0.25\cdot(2-3)=-0.125$. The sign of the ratio difference decides the order.

## Concepts
- [[bellman-equation-value-function]] — $f(x,y)$ is the optimal expected return, satisfying a one-function max equation (p. 63).
- [[principle-of-optimality]] — after any first choice, the continuation over the remaining stages must be optimal (p. 63).
- [[policy]] — a sequence of A/B choices, each read conditionally on survival of the machine (p. 62).
- [[decision-region]] (new) — the set of states $(x,y)$ in which a given choice is the optimal first move (p. 66).
- [[gain-to-loss-ratio-rule]] (new) — choose the action maximizing immediate expected gain over immediate expected loss, e.g. $p_1r_1x/(1-p_1)$ (p. 69).
- [[homogeneity-of-value-function]] (new) — $f(kx,ky)=kf(x,y)$; the choice depends only on $x/y$ (p. 66).
- [[successive-approximations]] (new) — $f_N\to f$ by geometric shrinkage of differences, factor $q=\max|p_i|<1$ (p. 65).
- [[approximation-in-policy-space]] — start from a fixed policy such as $A^\infty$ to get monotone convergence when $p_i\ge0$ (p. 65).
- [[stability-of-solution]] (new) — a bounded perturbation $h$ changes $f$ by at most $\max|h|/q$ (p. 76).

## Canonical instances
- [[gold-mining-two-mines]] (new) — the Anaconda/Bonanza process: fraction mined with probability $p_i$, else machine destroyed (p. 62).
- [[three-choice-counterexample]] (new) — adding a compromise choice C can give regions B, A, C, A instead of B, C, A (p. 75).
- [[gross-shapiro-problem]] (new) — Exercise 10, a two-mine problem in which A leads to $(ax,by)$ and B to $(cy,dx)$ (p. 78).

## Bridges (candidates)
- [structural-analogy] gain/loss ratio rule ↔ control-theory: an index policy that ranks actions by a single number computed per option — the text proves it for this two-mine process and only states it for the extensions (Theorems 3–4).
- [same-math] Theorem 1's contraction argument, $u_{N+1}\le q\,u_N$ ↔ control-theory: value iteration for discounted Bellman equations — the survival probability $p_i<1$ plays the role of a discount factor.
- [structural-analogy] Decision regions bounded by lines through the origin ↔ control-theory: switching surfaces in optimal control (canon link; not stated in this unit).
- [metaphor] Counter-example with a third option ↔ control-theory: why simple threshold policies need not be optimal beyond two actions.

## Questions this raises
- Why does a compromise choice C break the two-region pattern, and for which parameter values does Figure 9 occur?
- Is the number of decision regions finite for every choice set, and uniformly bounded?
- What changes if the objective is a utility $\varphi(R)$ of total return, or the probability of exceeding $R_0$ (Exercises 1, 8, 12)?
- How do the variational methods of Chapter 8 recover the simple three-region form in the continuous version?

## Exercises worth doing
- Ex. 1 (p. 77) — formulate the functional equation for maximizing $E\varphi(R)$ with state $(x,y,a)$ — difficulty: medium.
- Ex. 6 (p. 78) — show that Theorem 2 is the limit of the exponential-utility result as $b\to0$ — difficulty: medium.
- Ex. 10 (p. 78) — Gross–Shapiro problem: solve $f=\max[x+f(ax,by),\,y+f(cy,dx)]$ — difficulty: hard.
- Ex. 11 (p. 78) — a "continue with no gain" outcome reduces to the original form by rescaling $p_1\to p_1/(1-p_2)$ — difficulty: easy.
- Ex. 15–16 (p. 79) — a solution with no optimal policy, only $\delta$-optimal ones — difficulty: medium.
- Ex. 17 (p. 79) — non-uniqueness in bounded functions, uniqueness under $f(0,0)=0$ and continuity at the origin — difficulty: hard.

## Reading notes
- Printed page = pdf − 23 (pdf 84 = printed 61). Page numbers cited are printed.
- The text layer is garbled in several equations. These were checked against the images: Theorem 1's $r_i$ range, the ≥ signs in (6.5), Theorem 3–4 notation, and (11.2)–(11.3).
- Theorem 4 is printed with $f(x_1,x_2,\dots,x_N)$ in (4) although the indices run over $n$ in (5) and in $D_i$. This is a notational inconsistency in the source.
- In §12, $L_2(A^{-1})$ is described by the map $(x,y)\to(cx,y)$ where $c$ is not defined on that page.
- The §1 Introduction of this chapter says that the simple solution does not extend; Lemma 8 of Chapter 8 is cited for this (p. 61).
- Theorem 7 does not restate conditions on $p_i$.
- Bibliography (pp. 79–80): decision regions are mentioned again in Chapters VIII and IX. §8's result was obtained with M. Shiffman in summer 1950. Karlin and Shapiro gave an alternative geometric proof of Theorem 2 and the first counter-example (RAND RM-933, 1952).
