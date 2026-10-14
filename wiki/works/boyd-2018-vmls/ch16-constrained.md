---
id: boyd-2018-vmls/ch16-constrained
work: boyd-2018-vmls
unit: "Chapter 16 — Constrained least squares"
pages: 339–356
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Constrained least squares

## L0 — One line
Minimizing $\|Ax-b\|^2$ subject to linear equality constraints $Cx=d$ reduces to one square linear system (the KKT equations), whose coefficient matrix is invertible exactly when $C$ has independent rows and $\begin{bmatrix}A\\C\end{bmatrix}$ has independent columns.

## L1 — The gist (≤ 120 words)
How do we fit or choose a vector $x$ when some linear equations $Cx=d$ must hold exactly? The chapter shows that the solution comes from the $(n+p)\times(n+p)$ KKT linear system (the optimality conditions written as linear equations). That system is invertible if and only if condition (16.5) holds. The authors derive it with Lagrange multipliers, then verify it directly without calculus. They give two algorithms: one forms the KKT equations, the other uses QR and costs about $2(m+p)n^2+2np^2$ flops. The special case $A=I$, $b=0$ is the least norm problem, with solution $\hat x=C^\dagger d$. Examples: spline fitting, budget allocation, and moving a mass with minimal force.

**Prerequisites:** least squares and normal equations; QR factorization and back substitution; pseudo-inverse of a wide matrix; linear independence; partial derivatives; block matrices.

## L2 — Key ideas
- The constrained problem (16.1) combines solving the equations $Cx=d$ with least squares; each of those two problems is a special case of it. It can also be thought of, roughly speaking, as a limit of putting infinite weight on $\|Cx-d\|^2$; for very large $\lambda$, minimizing $\|Ax-b\|^2+\lambda\|Cx-d\|^2$ is expected to give a vector close to a solution (p. 339–340).
- Constraints are conditions that must hold exactly. Examples: continuity of a spline fit at a join (p. 341) and a fixed total advertising budget (p. 341).
- Lagrange multipliers give necessary optimality conditions. They form one linear system, the KKT equations (16.4), which extends the normal equations (p. 344–345).
- The KKT matrix is invertible if and only if (16.5) holds. Then $\hat x$ is unique and linear in $(b,d)$ (p. 345–346).
- When (16.5) holds, a calculus-free check shows that $\hat x$ is optimal and unique. The cross term vanishes because $C(x-\hat x)=0$ (p. 346–347).
- Algorithm 16.2 (QR) solves the problem in about $2(m+p)n^2+2np^2$ flops. It reduces to the ordinary QR least squares method when $p=0$ (p. 348–349).
- A sparse formulation (16.11) avoids forming the possibly denser $A^TA$ (p. 350).
- The least norm problem has solution $\hat x=C^\dagger d=C^T(CC^T)^{-1}d$, computable by QR of $C^T$ (p. 350–351).

## L3 — Walkthrough

### 16.1 Constrained least squares problem (p. 339–344)
**Problem.** Given $A$ ($m\times n$), $b$ ($m$-vector), $C$ ($p\times n$), $d$ ($p$-vector):
$$\text{minimize } \|Ax-b\|^2 \quad \text{subject to } Cx=d. \tag{16.1}$$
The function $\|Ax-b\|^2$ is the *objective*. The $p$ equations $c_i^Tx=d_i$ ($c_i^T$ = $i$th row of $C$) are the *constraints* (p. 339).
- $x$ is *feasible* if $Cx=d$.
- $\hat x$ is an *optimal point (solution)* if it is feasible and $\|A\hat x-b\|^2\le\|Ax-b\|^2$ for every feasible $x$ (p. 339).

**Relation to other problems.** Solving $Cx=d$ and unconstrained least squares are each special cases of (16.1) (p. 340). The problem can also be seen as a limit of a bi-objective least squares problem. The primary objective is $\|Ax-b\|^2$; the secondary is $\|Cx-d\|^2$, with "infinite weight". The authors expect, and say it can be verified, that minimizing $\|Ax-b\|^2+\lambda\|Cx-d\|^2$ for very large $\lambda$ gives a vector close to a solution of (16.1) (p. 340).

**Example: splines (p. 340–341).** Fit $\hat f(x)=p(x)$ for $x\le a$ and $q(x)$ for $x>a$ to $N=140$ points. Here $p(x)=\theta_1+\theta_2x+\theta_3x^2+\theta_4x^3$, $q(x)=\theta_5+\dots+\theta_8x^3$, and $a$ is given. Points are numbered so that $x_1,\dots,x_M\le a<x_{M+1},\dots,x_N$.
- The prediction-error sum of squares is $\sum_{i=1}^M(p(x_i)-y_i)^2+\sum_{i=M+1}^N(q(x_i)-y_i)^2$.
- Requiring $p(a)=q(a)$ and $p'(a)=q'(a)$ makes $\hat f$ continuous with a continuous first derivative. These are two linear equations:
$$\theta_1+\theta_2a+\theta_3a^2+\theta_4a^3-\theta_5-\theta_6a-\theta_7a^2-\theta_8a^3=0,$$
$$\theta_2+2\theta_3a+3\theta_4a^2-\theta_6-2\theta_7a-3\theta_8a^2=0.$$
- This is a constrained least squares problem in $\theta$ ($8$ unknowns). $A$ is $N\times 8$: rows $(1,x_i,x_i^2,x_i^3,0,0,0,0)$ for $i\le M$ and $(0,0,0,0,1,x_i,x_i^2,x_i^3)$ for $i>M$. $b=(y_1,\dots,y_N)$.
$$C=\begin{bmatrix}1&a&a^2&a^3&-1&-a&-a^2&-a^3\\0&1&2a&3a^2&0&-1&-2a&-3a^2\end{bmatrix},\quad d=\begin{bmatrix}0\\0\end{bmatrix}.$$
- With more intervals the method extends to *splines* (p. 341).

**Example: advertising budget (p. 341–342).** Choose channel spending $s$ ($n$-vector) so that the views $Rs$ are close to the target $v^{\rm des}$, with total spending fixed: minimize $\|Rs-v^{\rm des}\|^2$ subject to $\mathbf 1^Ts=B$. The solution may have negative entries. The authors ignore this here (p. 342).
- Instance: $m=10$ groups, $n=3$ channels.
- Plain least squares: RMS error 133 (about 13.3%), total budget $\mathbf 1^Ts^{\rm ls}=1605$.
- Target a budget 20% smaller, $B=1284$. The constrained solution is $s^{\rm cls}=(315,110,859)$, with RMS error 161.
- Simply scaling $s^{\rm ls}$ by 0.80 gives RMS error 239 (p. 342).

*Intuition note.* A constraint is a demand that must hold exactly, not a preference. Here, the best plan that spends exactly $B$ does better (161) than shrinking the unconstrained plan (239).

**16.1.1 Least norm problem (p. 342).** With $A=I$, $b=0$:
$$\text{minimize }\|x\|^2\quad\text{subject to }Cx=d. \tag{16.2}$$
This asks for the smallest-norm vector satisfying $Cx=d$.

**Example: force on a mass (p. 343–344).** The 10-vector $f$ gives forces applied for one second each to a unit mass without friction, starting at rest at position 0. Final velocity and position are
$$v^{\rm fin}=f_1+\dots+f_{10},\qquad p^{\rm fin}=(19/2)f_1+(17/2)f_2+\dots+(1/2)f_{10}.$$
- Goal: $v^{\rm fin}=0$, $p^{\rm fin}=1$. One solution is the "bang-bang" sequence $f^{\rm bb}=(1,-1,0,\dots,0)$. It has $\|f^{\rm bb}\|^2=2$ (p. 343).
- The smallest sequence by $\|f\|^2$ solves the least norm problem with $C=\begin{bmatrix}1&1&\cdots&1&1\\19/2&17/2&\cdots&3/2&1/2\end{bmatrix}$ and $d=(0,1)$.
- The solution $f^{\rm ln}$ has $\|f^{\rm ln}\|^2=0.0121$, a factor of 165 smaller than 2 (p. 343). Its force falls gradually from about $+0.05$ to $-0.05$ (figure 16.4, p. 344).

### 16.2 Solution (p. 344–347)
**Optimality conditions (Lagrange multipliers).** Write the constraints as $c_i^Tx=d_i$ and form the Lagrangian
$$L(x,z)=\|Ax-b\|^2+z_1(c_1^Tx-d_1)+\dots+z_p(c_p^Tx-d_p),$$
where $z$ is the $p$-vector of Lagrange multipliers. The method says: if $\hat x$ is a solution, then there exists $\hat z$ with
$$\frac{\partial L}{\partial x_i}(\hat x,\hat z)=0\ (i=1..n),\qquad \frac{\partial L}{\partial z_i}(\hat x,\hat z)=0\ (i=1..p). \tag{16.3}$$
Any solution must satisfy these (p. 344).
- The second set says $c_i^T\hat x-d_i=0$, i.e. $C\hat x=d$.
- The first set, after expanding the objective, is
$$2\sum_j (A^TA)_{ij}\hat x_j-2(A^Tb)_i+\sum_j\hat z_j(c_j)_i=0,$$
in matrix form $2A^TA\hat x-2A^Tb+C^T\hat z=0$ (p. 345).
- Together they give $n+p$ linear equations in $(\hat x,\hat z)$, the **KKT equations**:
$$\begin{bmatrix}2A^TA&C^T\\C&0\end{bmatrix}\begin{bmatrix}\hat x\\\hat z\end{bmatrix}=\begin{bmatrix}2A^Tb\\d\end{bmatrix}. \tag{16.4}$$
- (16.4) extends the normal equations (12.4) of unconstrained least squares (p. 345).

*Intuition note.* The multipliers $z$ are extra unknowns, one per constraint. Including them lets the optimality conditions be written as one ordinary square linear system.

**Invertibility.** The $(n+p)\times(n+p)$ KKT matrix is invertible if and only if
$$C \text{ has linearly independent rows, and } \begin{bmatrix}A\\C\end{bmatrix}\text{ has linearly independent columns.} \tag{16.5}$$
- The first condition requires $C$ to be wide or square: fewer constraints than variables.
- The second can hold even when the columns of $A$ are dependent. (16.5) generalizes assumption (12.2) (p. 345).

*Proof, "if".* Assume (16.5) and suppose the KKT matrix is not invertible. Then some nonzero $(\bar x,\bar z)$ has $2A^TA\bar x+C^T\bar z=0$ and $C\bar x=0$ (p. 345).
1. Multiply the first equation by $\bar x^T$: $2\|A\bar x\|^2+\bar x^TC^T\bar z=0$.
2. $C\bar x=0$ gives $\bar x^TC^T=0$, so $2\|A\bar x\|^2=0$, i.e. $A\bar x=0$.
3. So $\begin{bmatrix}A\\C\end{bmatrix}\bar x=0$. Independent columns give $\bar x=0$.
4. Then $C^T\bar z=0$. Independent columns of $C^T$ give $\bar z=0$. Contradiction (p. 346).

*Proof, "only if".*
- If the rows of $C$ are dependent, some $\bar z\ne0$ has $C^T\bar z=0$. Then the KKT matrix times $(0,\bar z)$ is $0$.
- If the stacked matrix has dependent columns, some $\bar x\neq0$ has $\begin{bmatrix}A\\C\end{bmatrix}\bar x=0$. Then the KKT matrix times $(\bar x,0)$ is $0$ (p. 346).

Under (16.5) the problem has the unique solution
$$\begin{bmatrix}\hat x\\\hat z\end{bmatrix}=\begin{bmatrix}2A^TA&C^T\\C&0\end{bmatrix}^{-1}\begin{bmatrix}2A^Tb\\d\end{bmatrix}, \tag{16.6}$$
which also gives $\hat z$. The solution $\hat x$ is a linear function of $(b,d)$ (p. 346).

**Direct verification (no calculus).** Assume (16.5). Let $(\hat x,\hat z)$ satisfy $2A^TA\hat x+C^T\hat z=2A^Tb$ and $C\hat x=d$. Take any $x\ne\hat x$ with $Cx=d$ (p. 346).
1. $\|Ax-b\|^2=\|Ax-A\hat x\|^2+\|A\hat x-b\|^2+2(Ax-A\hat x)^T(A\hat x-b)$.
2. The cross term: $2(x-\hat x)^TA^T(A\hat x-b)=-(x-\hat x)^TC^T\hat z=-(C(x-\hat x))^T\hat z=0$. This uses $2A^T(A\hat x-b)=-C^T\hat z$ and $Cx=C\hat x=d$ (p. 347).
3. Hence $\|Ax-b\|^2=\|A(x-\hat x)\|^2+\|A\hat x-b\|^2\ge\|A\hat x-b\|^2$, so $\hat x$ is a minimizer among feasible $x$.
4. Strictness: if $\|A(x-\hat x)\|^2=0$, then $A(x-\hat x)=0$ and $C(x-\hat x)=0$. So $\begin{bmatrix}A\\C\end{bmatrix}(x-\hat x)=0$, and independent columns force $x=\hat x$ (p. 347).

*Intuition note.* Moving from $\hat x$ to another feasible point changes $x$ only along directions $v$ with $Cv=0$. The multiplier term is orthogonal to those directions, so the error grows by exactly $\|Av\|^2$.

### 16.3 Solving constrained least squares problems (p. 347–351)
**Algorithm 16.1 (KKT).** Given $A,C$ satisfying (16.5), $b$, $d$: (1) compute $A^TA$; (2) solve (16.4) by QR factorization and back substitution. Step 2 cannot fail under (16.5). Cost: $mn^2+2(n+p)^3$ flops. Since (16.5) implies $p\le n$, $(n+p)^3$ may be replaced by $n^3$ in order terms (p. 347).

**QR method.** Assume (16.5) (p. 348).
1. Multiply $C\hat x=d$ by $2C^T$, add it to the first KKT equation, and set $w=\hat z-2d$:
$$2(A^TA+C^TC)\hat x+C^Tw=2A^Tb,\quad C\hat x=d. \tag{16.7}$$
2. The stacked matrix has independent columns, so
$$\begin{bmatrix}A\\C\end{bmatrix}=\begin{bmatrix}Q_1\\Q_2\end{bmatrix}R, \tag{16.8}$$
with $Q_1$ of size $m\times n$, $Q_2$ of size $p\times n$, $R$ of size $n\times n$.
3. Substitute $A=Q_1R$, $C=Q_2R$, $A^TA+C^TC=R^TR$: $2R^TR\hat x+R^TQ_2^Tw=2R^TQ_1^Tb$ and $Q_2R\hat x=d$.
4. Multiply the first by $R^{-T}$:
$$R\hat x=Q_1^Tb-(1/2)Q_2^Tw. \tag{16.9}$$
5. Put this into $Q_2R\hat x=d$:
$$Q_2Q_2^Tw=2Q_2Q_1^Tb-2d. \tag{16.10}$$
6. $Q_2^T=R^{-T}C^T$ ($n\times p$) has independent columns. If $R^{-T}C^Tz=0$, then $C^Tz=0$, so $z=0$ because $C$ has independent rows.
7. So $Q_2^T=\tilde Q\tilde R$ (QR factorization). Then $Q_2Q_2^T=\tilde R^T\tilde R$, and (16.10) becomes $\tilde R^T\tilde Rw=2\tilde R^T\tilde Q^TQ_1^Tb-2d$, i.e. $\tilde Rw=2\tilde Q^TQ_1^Tb-2\tilde R^{-T}d$ (p. 348).
8. Compute $w$ (forward substitution for $\tilde R^{-T}d$, then back substitution), then $\hat x$ from (16.9).

**Algorithm 16.2 (QR) (p. 349).**
1. Compute $\begin{bmatrix}A\\C\end{bmatrix}=\begin{bmatrix}Q_1\\Q_2\end{bmatrix}R$ and $Q_2^T=\tilde Q\tilde R$.
2. Compute $\tilde R^{-T}d$ by forward substitution.
3. Solve $\tilde Rw=2\tilde Q^TQ_1^Tb-2\tilde R^{-T}d$ by back substitution.
4. Solve $R\hat x=Q_1^Tb-(1/2)Q_2^Tw$ by back substitution.

If $p=0$: step 1 is the QR factorization of $A$, steps 2–3 are not needed, step 4 is $R\hat x=Q_1^Tb$. This is algorithm 12.1 (p. 349).

**Complexity (p. 349).**
- Step 1: QR of an $(m+p)\times n$ and an $n\times p$ matrix, $2(m+p)n^2+2np^2$ flops.
- Step 2: $p^2$.
- Step 3: $2mn+2pn+p^2$.
- Step 4: $2mn+2pn+n^2$.
- Steps 2–4 are quadratic and negligible, so the total is $2(m+p)n^2+2np^2$.
- (16.5) implies $p\le n\le m+p$, so $(m+p)n^2\ge np^2$. Hence the count is at most $4(m+p)n^2$, of order $(m+p)n^2$.

**Sparse case (p. 349–350).** One can replace QR by sparse QR. The Gram matrix $A^TA$ can be much less sparse than $A$. To avoid it, solve the $(m+n+p)$-equation system
$$\begin{bmatrix}0&A^T&C^T\\A&-(1/2)I&0\\C&0&0\end{bmatrix}\begin{bmatrix}\hat x\\\hat y\\\hat z\end{bmatrix}=\begin{bmatrix}0\\b\\d\end{bmatrix}. \tag{16.11}$$
Solutions correspond to KKT solutions: $(\hat x,\hat z)$ solves (16.4), and conversely, with $\hat y=2(A\hat x-b)$. The coefficient matrix is sparse when $A$ and $C$ are (p. 350).

**Least norm solution (p. 350–351).** For $A=I$, the stacked matrix $\begin{bmatrix}I\\C\end{bmatrix}$ always has independent columns. So (16.5) reduces to: $C$ has independent rows. The KKT equations become $\begin{bmatrix}2I&C^T\\C&0\end{bmatrix}\begin{bmatrix}\hat x\\\hat z\end{bmatrix}=\begin{bmatrix}0\\d\end{bmatrix}$.
1. Row 1: $\hat x=-(1/2)C^T\hat z$.
2. Substitute into $C\hat x=d$: $-(1/2)CC^T\hat z=d$. $CC^T$ is invertible, so $\hat z=-2(CC^T)^{-1}d$.
3. Therefore
$$\hat x=C^T(CC^T)^{-1}d=C^\dagger d. \tag{16.12}$$
- $C^\dagger$ is the pseudo-inverse of a wide matrix with independent rows, known from §11.5 to be a right inverse. Now $\hat x=C^\dagger d$ is also the least-norm vector satisfying $Cx=d$ (p. 351).
- With $C^T=QR$: $C^\dagger=QR^{-T}$, so $\hat x=QR^{-T}d$.

**Algorithm 16.3 (least norm via QR) (p. 351).** (1) Factor $C^T=QR$. (2) Solve $R^Ty=d$ by forward substitution. (3) $\hat x=Qy$. Cost is dominated by step 1: $2np^2$ flops.

*Intuition note.* When $C$ has independent rows, the shortest solution of $Cx=d$ has the form $C^T$ times something, i.e. it lies in the row space of $C$ (16.12). The pseudo-inverse picks exactly that one.

## Toy example (ours, not from the text)
Minimize $(x_1-3)^2+(x_2-1)^2$ subject to $x_1+x_2=2$.
- Data: $A=I_2$, $b=(3,1)$, $C=[1\ \ 1]$, $d=[2]$. Here $C$ has independent rows and $\begin{bmatrix}I\\C\end{bmatrix}$ has independent columns, so (16.5) holds.
- KKT system (16.4): $2A^TA=2I$, $2A^Tb=(6,2)$:
$$\begin{bmatrix}2&0&1\\0&2&1\\1&1&0\end{bmatrix}\begin{bmatrix}x_1\\x_2\\z\end{bmatrix}=\begin{bmatrix}6\\2\\2\end{bmatrix}.$$
- Rows 1 and 2 give $x_1=(6-z)/2$ and $x_2=(2-z)/2$. Row 3: $(6-z)/2+(2-z)/2=4-z=2$, so $z=2$, $x_1=2$, $x_2=0$.
- Check the constraint: $2+0=2$ ✓. Objective: $(2-3)^2+(0-1)^2=2$.
- Other feasible points do worse: $(1,1)$ gives $4+0=4$; $(1.5,0.5)$ gives $2.25+0.25=2.5$.
- The unconstrained minimizer $(3,1)$ has objective 0 but is infeasible ($3+1=4\ne2$).

## Concepts
- [[constrained-least-squares]] (new) — minimize $\|Ax-b\|^2$ subject to linear equalities $Cx=d$ (p. 339)
- [[feasible-point]] (new) — a vector satisfying all constraints $Cx=d$ (p. 339)
- [[lagrange-multipliers]] (new) — extra variables $z$ whose Lagrangian conditions give necessary optimality conditions (p. 344)
- [[kkt-equations]] (new) — the square $(n+p)$ linear system (16.4) in $(\hat x,\hat z)$; extends the normal equations (p. 345)
- [[kkt-matrix-invertibility]] (new) — invertible iff (16.5): $C$ has independent rows, $[A;C]$ independent columns (p. 345)
- [[least-norm-problem]] (new) — minimize $\|x\|^2$ subject to $Cx=d$; solution $C^\dagger d$ (p. 342, 351)
- [[least squares]] — the unconstrained special case, with normal equations (12.4) (p. 340, 345)
- [[pseudoinverse]] — $C^\dagger=C^T(CC^T)^{-1}$ gives the least-norm solution (p. 351)
- [[Gram–Schmidt and QR]] — QR of $[A;C]$ and of $Q_2^T$ yields Algorithm 16.2 (p. 348)

## Canonical instances
- [[spline-fit-continuity-constraints]] — two cubics joined with continuous value and slope (p. 340–341)
- [[advertising-budget-allocation]] — fixed total budget $\mathbf 1^Ts=B$; RMS 161 vs 239 for scaling (p. 341–342)
- [[least-norm-force-sequence]] — least norm $0.0121$ vs bang-bang $2$ (p. 343–344)

## Bridges (candidates)
- [structural-analogy] Weighted objective $\|Ax-b\|^2+\lambda\|Cx-d\|^2$, large $\lambda$ ↔ optimization: penalty methods — a hard constraint as the limit of a heavy penalty.
- [same-math] Least norm solution $C^T(CC^T)^{-1}d$ ↔ linear-algebra: pseudo-inverse of a wide full-row-rank matrix — the chapter states they are the same matrix.
- [structural-analogy] Lagrange multipliers $\hat z$ ↔ economics: shadow prices of constraints — $\hat z$ measures how the constraint "costs" the objective (our reading; not stated in the unit).
- [structural-analogy] Sparse trick (16.11) ↔ numerical linear algebra: augmented systems — avoid forming $A^TA$.

## Questions this raises
- How do the $\hat z$ values change if $d$ changes? Do they measure sensitivity of the optimum?
- What if $C$ has dependent rows, or $[A;C]$ has dependent columns? Is there still a solution, and when is it non-unique?
- How would inequality constraints (e.g. $s\ge0$ in the advertising problem) change the method?
- How accurate is the large-$\lambda$ approximation, and when would one prefer it to the exact KKT solution?

## Exercises worth doing
- Ex. 16.3 (p. 352) — closest point to $y$ among solutions of $Ax=b$; a least norm problem in disguise — difficulty: medium
- Ex. 16.5 (p. 352) — numerically check KKT solution and compare with the least norm solution — difficulty: easy
- Ex. 16.11 (p. 354) — least distance problem, $\hat x=a-C^\dagger(Ca-d)$ — difficulty: medium
- Ex. 16.9 (p. 353) — smoothest force sequence; contrast with the least norm one — difficulty: medium
- Ex. 16.2 (p. 352) — matrix least norm problem splits into column problems, $\hat X=C^\dagger D$ — difficulty: medium
- Ex. 16.15 (p. 355) — predict each column from the others at once via $(A^TA)^{-1}$ — difficulty: hard

## Reading notes
- Printed page = pdf page − 10. Pdf 366 (printed 356) carries no text in the text layer.
- Exercises 16.1–16.15 have no solutions printed here.
- Figure 16.3's caption says the mass moves "over a unit distance in 10 seconds". The text says it arrives after two seconds and then rests. The plot shows position 1 reached at about $t=2$.
- The complexity text (p. 349) says $w$ is found with "forward substitution ($p^2$ flops)" in step 3. Algorithm 16.2 itself says back substitution for that step.
- The text layer was readable. All equations were checked against the images.
