---
id: liberzon-2012-calculus/ch06-linear
work: liberzon-2012-calculus
unit: "Chapter 6 — The Linear Quadratic Regulator"
pages: 145–160
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# The Linear Quadratic Regulator

## L0 — One line
For linear dynamics and quadratic cost, the optimal control is a linear state feedback $u^*=-R^{-1}B^TPx$, where $P$ solves a Riccati equation and $x^TPx$ is the optimal cost.

## L1 — The gist (≤ 120 words)
How should one steer a linear system $\dot x=Ax+Bu$ to make a quadratic cost on state and control as small as possible? The maximum principle gives a unique candidate: linear state feedback with a matrix $P(t)$ that solves a Riccati differential equation run backward from the final time. The HJB sufficient condition then shows optimality and that $x^TPx$ is the optimal cost. On an infinite horizon, $P$ becomes constant and solves an algebraic Riccati equation. With controllability and observability, the optimal closed loop is exponentially stable. LQR is much more tractable than the general problem, because an ordinary differential equation replaces the HJB partial differential equation.

**Prerequisites:** maximum principle and costate; HJB equation and value function; matrix calculus; positive (semi)definite matrices; transition matrix; controllability and observability of linear systems.

## L2 — Key ideas
- The finite-horizon LQR problem has linear dynamics, a quadratic running and terminal cost, free final state, and $R>0$ so that $R^{-1}$ exists (p. 145).
- The maximum principle yields a unique candidate control, a linear feedback $u^*=-R^{-1}B^TPx^*$, with $P(t_1)=M$. The gain is time-varying even for time-invariant systems (p. 146–147).
- $P$ satisfies the quadratic matrix Riccati differential equation (RDE), integrated backward. This is an $n\times n$ quadratic equation instead of a $2n\times 2n$ linear one (p. 148).
- The guess $V=x^TPx$ solves the HJB equation. So the candidate control is globally optimal and $x^TPx$ is the cost-to-go (p. 150).
- $P(t)$ cannot blow up: $x^TPx$ is bounded by the cost of zero control, which rules out finite escape (p. 151–152).
- Infinite horizon: under controllability, $P(t_0,t_1)$ is monotone and bounded in $t_1$. So it converges to a constant $P$ solving the algebraic Riccati equation (ARE) (p. 153–154).
- A Lyapunov-type computation shows $u^*=-R^{-1}B^TPx$ is optimal, with cost $x_0^TPx_0$ (p. 155–156).
- Observability of $(A,C)$ with $Q=C^TC$ makes the optimal closed loop exponentially stable and makes $P$ unique and positive definite (p. 156–158).

## L3 — Walkthrough

### 6.1 Finite-horizon LQR problem (p. 145)
Setting: $\dot x=A(t)x+B(t)u$, $x(t_0)=x_0$ (6.1), with $x\in\mathbb R^n$, $u\in\mathbb R^m$ unconstrained. The target set is $\{t_1\}\times\mathbb R^n$ (fixed time, free endpoint). The cost is
$$J(u)=\int_{t_0}^{t_1}\big(x^TQ(t)x+u^TR(t)u\big)dt+x^T(t_1)Mx(t_1)\tag{6.2}$$
with $M=M^T\ge0$, $Q=Q^T\ge0$, $R=R^T>0$. Shapes: $A,Q,M$ are $n\times n$; $B$ is $n\times m$; $R$ is $m\times m$. Q and R weight state size against control effort. $R>0$ is required because its inverse is needed.

#### 6.1.1 Candidate optimal feedback law (p. 146–148)
Hamiltonian: $H=p^TA x+p^TBu-x^TQx-u^TRu$, with abnormal multiplier $p_0=-1$. This loses no generality: the transversality condition $0=p^*(t_1)-2p_0^*Mx^*(t_1)$ plus nontriviality forces $p_0^*\ne0$ (p. 146). The variational approach of Section 3.4 would also work, since $u$ is unconstrained, the endpoint is free and $H$ is quadratic in $u$ (p. 146).

Steps:
1. $H_u=B^Tp-2Ru=0$ gives, since $R$ is invertible,
$$u^*(t)=\tfrac12R^{-1}(t)B^T(t)p^*(t)\tag{6.3}$$
$H_{uu}=-2R<0$, so (6.3) maximizes $H$ globally. It is the unique control meeting the necessary conditions, but optimality is not yet verified (p. 146).
2. Adjoint equation and boundary condition:
$$\dot p^*=-H_x|_*=2Qx^*-A^Tp^*\tag{6.4}$$
$$p^*(t_1)=-K_x(x^*(t_1))=-2Mx^*(t_1)\tag{6.5}$$
3. Goal: a linear relation $p^*(t)=-2P(t)x^*(t)$ (6.6) for all $t$. The canonical equations are
$$\begin{pmatrix}\dot x^*\\ \dot p^*\end{pmatrix}=\begin{pmatrix}A&\tfrac12BR^{-1}B^T\\2Q&-A^T\end{pmatrix}\begin{pmatrix}x^*\\p^*\end{pmatrix}=:\mathcal H(t)\begin{pmatrix}x^*\\p^*\end{pmatrix}\tag{6.7}$$
$\mathcal H$ is the Hamiltonian matrix, $2n\times2n$ (p. 146–147).
4. Let $\Phi(\cdot,\cdot)$ be the transition matrix of (6.7), partitioned into $n\times n$ blocks $\Phi_{ij}$. Then $(x^*(t),p^*(t))=\Phi(t,t_1)(x^*(t_1),p^*(t_1))$. With (6.5):
$$x^*(t)=(\Phi_{11}(t,t_1)-2\Phi_{12}(t,t_1)M)x^*(t_1)\tag{6.8}$$
$$p^*(t)=(\Phi_{21}(t,t_1)-2\Phi_{22}(t,t_1)M)x^*(t_1)\tag{6.9}$$
5. Solve (6.8) for $x^*(t_1)$ and insert into (6.9). This gives (6.6) with
$$P(t):=-\tfrac12\big(\Phi_{21}-2\Phi_{22}M\big)\big(\Phi_{11}-2\Phi_{12}M\big)^{-1}\tag{6.10}$$
(all blocks evaluated at $(t,t_1)$) (p. 147).
6. Remarks (p. 147). Invertibility is not yet justified. But $\Phi(t_1,t_1)=I$, so $\Phi_{11}-2\Phi_{12}M=I$ at $t_1$, and by continuity it stays invertible near $t_1$. So $P$ is well defined at least near $t_1$. From (6.5) and (6.6), $P(t_1)=M$ (6.11). The factor $-\tfrac12$ is explained later: $P$ is symmetric positive semidefinite and tied to the optimal cost.
7. Combining (6.3) and (6.6):
$$\boxed{u^*(t)=-R^{-1}(t)B^T(t)P(t)x^*(t)}\tag{6.12}$$
This is a linear state feedback law, so the optimal closed loop must be linear. The gain is time-varying even if (6.1) is time-invariant (p. 147). An open-loop formula via $x_0$ is also possible, but the feedback form is more revealing (p. 148).

*Intuition note.* Because the dynamics are linear and the cost is quadratic, the costate turns out to be a linear function of the state (6.6). So the optimal action is a linear rule applied to whatever state the system is in; its gain may vary with time (p. 147). Formula (6.10) is clumsy, since $\Phi$ is rarely computable analytically (p. 148).

*Skip path:* carry forward (6.11) and (6.12).

#### 6.1.2 Riccati differential equation (p. 148–149)
1. Differentiate (6.6): $\dot p^*=-2\dot Px^*-2P\dot x^*$.
2. Substitute (6.7): $2Qx^*-A^Tp^*=-2\dot Px^*-2PAx^*-PBR^{-1}B^Tp^*$.
3. Replace $p^*$ by $-2Px^*$ and divide by 2:
$$Qx^*+A^TPx^*=-\dot Px^*-PAx^*+PBR^{-1}B^TPx^*\tag{6.13}$$
4. $x_0$ is arbitrary and the closed-loop transition matrix is nonsingular, so $x^*(t)$ can be arbitrary. Hence
$$\boxed{\dot P=-PA-A^TP-Q+PBR^{-1}B^TP}\tag{6.14}$$
the Riccati differential equation (RDE), with $P(t_1)=M$, propagated backward in time.

Comparison (p. 148): (6.14) is quadratic and $n\times n$. (6.10) uses $\Phi$, which solves a linear equation $\tfrac{d}{dt}\Phi=\mathcal H\Phi$ of size $2n\times2n$. Going from (6.10) to (6.14) halves the matrix size but trades a linear equation for a quadratic one. Exercise 6.1 gives a linear route of size $2n\times n$: solve $(\dot X,\dot Y)=\mathcal H(X,Y)$ with $X(t_1)=I$, $Y(t_1)=-2M$, and set $P=-\tfrac12YX^{-1}$ (6.15) (p. 149). This matches the substitution in Section 2.6.2, with $W$ playing the role of $P$ (p. 149).

Summary so far: the maximum principle gives a unique candidate (6.12), with $P$ from (6.14) and (6.11). It cannot settle global existence of $P$ or optimality (p. 149).

#### 6.1.3 Value function and optimality (p. 149–151)
The HJB equation and its boundary condition become
$$-V_t=\inf_{u}\{x^TQx+u^TRu+\langle V_x,Ax+Bu\rangle\},\qquad V(t_1,x)=x^TMx\tag{6.16, 6.17}$$
Since $R>0$ the infimum is a minimum, attained at $u=-\tfrac12R^{-1}B^TV_x$ (6.18). Substituting:
$$-V_t=x^TQx-\tfrac14V_x^TBR^{-1}B^TV_x+V_x^TAx\tag{6.19}$$
For (6.12) to match (6.18) we need $\tfrac12V_x(t,x)=P(t)x$ (6.20). By (6.11), the boundary condition reads $V(t_1,x)=x^TP(t_1)x$ (6.21). "Wishful thinking": assume $P$ is symmetric (Exercise 6.2a), and guess
$$V(t,x)=x^TP(t)x\tag{6.22}$$
Then (6.21) holds, $V_x=2Px$ so (6.20) holds, and $V_t=x^T\dot Px$. Substituting into (6.19):
$$-x^T\dot Px=x^T\big(Q-PBR^{-1}B^TP+PA+A^TP\big)x\tag{6.23}$$
This is an identity by the RDE. So (6.22) is the value function and (6.12) is the globally optimal control. Uniqueness follows from Section 6.1.1 (p. 150).

*Intuition note.* The path was: maximum principle gives a candidate control, then a guessed value function verifies it through HJB. The optimal cost-to-go from $(t,x)$ is the quadratic form $x^TP(t)x$ (p. 150).

Exercise 6.2 asks to prove symmetry, $P\ge0$, and whether $P>0$ (p. 151). Exercise 6.3 asks to confirm optimality by square completion alone (p. 151).

#### 6.1.4 Global existence of the RDE solution (p. 151–152)
Local existence near $t_1$ is standard. The danger is finite escape time: some $P_{ij}(t)\to\pm\infty$ as $t\searrow\bar t$. In terms of (6.10) this would mean that $\Phi_{11}-2\Phi_{12}M$ becomes singular at $\bar t$; in terms of (6.15), that $X(t)$ does (p. 151). Argument by contradiction:
1. Suppose $P$ exists on $(\bar t,t_1]$ but an entry is unbounded as $t\searrow\bar t$. By Exercise 6.2, $P$ is symmetric $\ge0$, so all principal minors are $\ge0$.
2. If an off-diagonal entry $P_{ij}$ is unbounded while the diagonals stay bounded, the $2\times2$ principal minor on rows and columns $i,j$ becomes negative near $\bar t$. This is excluded (p. 151–152).
3. So some $P_{ii}=e_i^TPe_i\to\infty$. This is the optimal cost-to-go from $e_i$ at time $t$. It cannot exceed the cost of zero control, with trajectory $x(s)=\Phi_A(s,t)e_i$:
$$\int_t^{t_1}e_i^T\Phi_A^T(s,t)Q(s)\Phi_A(s,t)e_i\,ds+e_i^T\Phi_A^T(t_1,t)M\Phi_A(t_1,t)e_i$$
This is bounded as $t\to\bar t$. Contradiction (p. 152).

So $P(\cdot)$ exists on $[t_0,t_1]$ and the finite-horizon problem is solved (p. 152).

**Example 6.1** (p. 152): $\dot x=u$, $J=\int_{t_0}^{t_1}(x^2+u^2)dt$. So $A=0$, $B=Q=R=1$, $M=0$, and the RDE is $\dot P=P^2-1$, $P(t_1)=0$. Separating variables: $\int_{P(t)}^{0}\frac{dP}{P^2-1}=\int_t^{t_1}ds$. The left side is $\tanh^{-1}P(t)$, so $P(t)=\tanh(t_1-t)$ and $u=-\tanh(t_1-t)x$. Footnote 2: with $R=-1$ the RDE would be $\dot P=-P^2-1$, whose solutions do not exist globally backward (p. 152).

Closed forms are expected only in special cases. Still, the RDE is an ODE, solvable by standard numerical methods, whereas HJB is a PDE (p. 152).

### 6.2 Infinite-horizon LQR problem (p. 153–159)
Assume $A,B,Q,R$ constant and $M=0$, then let $t_1\to\infty$. Well-posedness (finite optimal cost) must be proved. Notation: $V^{t_1}$ is the value function; $P(t,t_1)$ solves the RDE with $P(t_1)=0$; $u^*_{t_1},x^*_{t_1}$ are the finite-horizon optimal pair. Then
$$u^*_{t_1}=-R^{-1}B^TP(t,t_1)x^*_{t_1},\quad V^{t_1}(t,x)=x^TP(t,t_1)x,\quad V^{t_1}(t_0,x_0)=x_0^TP(t_0,t_1)x_0\tag{6.24–6.26}$$

#### 6.2.1 Existence and properties of the limit (p. 153–155)
- **Monotonicity.** For $t_2>t_1$, since $Q\ge0$, $R>0$: $x_0^TP(t_0,t_2)x_0=V^{t_2}(t_0,x_0)\ge\int_{t_0}^{t_1}(\dots)dt\ge V^{t_1}(t_0,x_0)$, using the $t_2$-optimal pair truncated at $t_1$. So the cost is nondecreasing in $t_1$ (p. 153).
- **Boundedness.** Not true in general: for $\dot x=x$ the cost is unbounded. If $(A,B)$ is controllable, some control $\bar u$ steers $x_0$ to $0$ at time $\bar t$; set $\bar u=0$ afterwards. Then $x_0^TP(t_0,t_1)x_0\le J(\bar u)=\int_{t_0}^{\bar t}(\dots)dt$ for all $t_1\ge\bar t$, a bound independent of $t_1$ (p. 154). Controllability is assumed from here on.
- **Existence of the matrix limit.** Monotone and bounded gives a limit of $x_0^TPx_0$. With $x_0=e_i$, the diagonal entries $P_{ii}$ converge. With $x_0=e_i+e_j$ and symmetry, $P_{ii}+2P_{ij}+P_{jj}$ converges, so off-diagonal entries converge (p. 154).
- **Properties.** The RDE is now time-invariant, so $P(t_0,t_1)$ depends only on $t_1-t_0$. Hence $P:=\lim_{t_1\to\infty}P(t,t_1)$ (6.27) is a constant matrix, independent of $t$. Then $\dot P(t,t_1)$ has a limit that must be the zero matrix, so $P$ solves the algebraic Riccati equation (ARE)
$$PA+A^TP+Q-PBR^{-1}B^TP=0\tag{6.28}$$
(p. 154). The ARE may have spurious extra solutions. $P$ is symmetric positive semidefinite, and the author hopes that this property pins $P$ down, and says that 6.2.4 will show this holds under appropriate assumptions (p. 155). Exercise 6.4: double integrator, find $P$ from the ARE (p. 155).

*Intuition note.* Under controllability, running the RDE backward from zero for a long time lets it settle to a steady state (p. 154). The steady state of a differential equation satisfies a purely algebraic equation.

#### 6.2.2 Infinite-horizon problem and its solution (p. 155–156)
Cost $J(u)=\int_{t_0}^\infty(x^TQx+u^TRu)dt$ (6.29). Guess: $V(x_0)=x_0^TPx_0$ (6.30) and $u^*=-R^{-1}B^TPx^*$ (6.31), where $x^*$ is the closed-loop trajectory from $x_0$. Optimality is not yet obvious. Proof:
1. Let $\hat V(x)=x^TPx$. Along $x^*$ (with $\dot x^*=(A-BR^{-1}B^TP)x^*$):
$$\tfrac{d}{dt}\hat V=x^{*T}P(A-BR^{-1}B^TP)x^*+x^{*T}(A^T-PBR^{-1}B^T)Px^*=x^{*T}(PA+A^TP-2PBR^{-1}B^TP)x^*=-x^{*T}(Q+PBR^{-1}B^TP)x^*$$
The last step uses the ARE (6.28).
2. Since $(u^*)^TRu^*=x^{*T}PBR^{-1}B^TPx^*$ *(added step)*, the cost on $[t_0,T]$ is
$$\int_{t_0}^T(x^{*T}Qx^*+u^{*T}Ru^*)dt=-\int_{t_0}^T\tfrac{d}{dt}\hat V\,dt=x_0^TPx_0-x^{*T}(T)Px^*(T)\le x_0^TPx_0$$
because $P\ge0$. Letting $T\to\infty$: $J(u^*)\le x_0^TPx_0$ (6.32). So the problem is well posed.
3. For any control $u$ from $x_0$ and any finite $t_1$: $x_0^TP(t_0,t_1)x_0\le\int_{t_0}^{t_1}(\dots)\le J(u)$, using $Q\ge0$, $R>0$. Letting $t_1\to\infty$: $x_0^TPx_0\le J(u)$.
4. Hence $J(u^*)=x_0^TPx_0\le J(u)$ for all $u$ (p. 156).

#### 6.2.3 Closed-loop stability (p. 156–157)
**Example 6.2:** $\dot x=x+u$, $J=\int u^2dt$. Then $u^*\equiv0$ (zero cost), $P=0$ (the ARE also has the solution $P=2$, to be discarded), and the closed loop $\dot x^*=x^*$ is unstable. The cost does not penalize the state (p. 156).

Remedy: $Q=C^TC$ with $C$ of size $p\times n$, $p\le n$. Set $y=Cx$, so $J=\int(y^Ty+u^TRu)dt$. Assume $(A,C)$ is observable. If $Q>0$ then $C=Q^{1/2}$ is nonsingular and observability holds automatically. In Example 6.2, $C=0$ and it fails (p. 157). Argument for stability:
1. By (6.32), $J(u^*)$ is finite (6.33).
2. The closed loop is linear time-invariant, so $x^*,y^*,u^*$ are combinations of exponentials. Since $R>0$, a finite integral forces $y^*\to0$ and $u^*\to0$.
3. For an observable LTI system, $y,u\to0$ implies $x\to0$. (Sketch: choose $L$ so that $A-LC$ is stable and write $\dot x=(A-LC)x+Ly+Bu$.)
4. So the closed loop is asymptotically, in fact exponentially, stable (p. 157).

#### 6.2.4 Complete result (p. 157–159)
**Theorem 6.1.** Let $\dot x=Ax+Bu$, $J=\int_{t_0}^\infty(x^TC^TCx+u^TRu)dt$, with $(A,B)$ controllable, $(A,C)$ observable, $R=R^T>0$. Then:
1. $P=\lim_{t_1\to\infty}P(t_0,t_1)$ exists, is constant, and is the unique symmetric positive definite solution of the ARE (6.28).
2. The optimal cost is $V(x_0)=x_0^TPx_0$.
3. The unique optimal control is $u^*=-R^{-1}B^TPx^*$.
4. The closed loop $\dot x^*=(A-BR^{-1}B^TP)x^*$ is exponentially stable. (p. 157–158)

Remaining claims (p. 158–159):
- **$P>0$.** If $x_0^TPx_0=0$, the optimal cost is $0$, so $Cx^*\equiv0$ and $u^*\equiv0$ (as $R>0$). By observability, $x^*\equiv0$, so $x_0=0$.
- **Uniqueness of $P$** (even among positive semidefinite solutions). Let $\bar P\ge0$ solve the ARE. Define $\bar J^{t_1}(u)=\int_{t_0}^{t_1}(x^TQx+u^TRu)dt+x^T(t_1)\bar Px(t_1)$ and its limit $\bar J^\infty$. By statements 4 and 2, $u^*$ gives $\bar J^\infty(u^*)=x_0^TPx_0$, and every $u$ has $\bar J^\infty(u)\ge x_0^TPx_0$. By Section 6.1, the optimal cost of $\bar J^{t_1}$ is $x_0^TP(t_0;\bar P,t_1)x_0$. But $\bar P$ is an equilibrium of the RDE, so this solution equals $\bar P$ for every $t_1$. Hence $\bar P=P$.
- **Uniqueness of the control.** From (5.13)–(5.14), with $V=x^TPx$, $u^*(t)=\arg\min_u\{x^{*T}Qx^*+u^TRu+2x^{*T}PAx^*+2x^{*T}PBu\}$, which uniquely gives statement 3 (p. 159).

Role of assumptions (p. 159): observability is used only for stability (statement 4) and for positive definiteness and uniqueness of $P$ in statement 1. Controllability is used for existence of $P$, on which the other claims rest. Some claims might still hold without these assumptions. Exercise 6.5: replace them by stabilizability and detectability.

Examples (p. 159): the infinite-horizon version of Example 6.1 has ARE $P^2-1=0$, solutions $P=\pm1$. The wanted one is $P=1$, giving $V(x_0)=x_0^2$ and $u^*=-x^*$. The text calls linearity, time-invariance and exponential stability very desirable. The choice of $Q$ and $R$ is often part of the design. Exercise 6.6: for $\dot x=ax+bu$, $a,q,r>0$, as $r\to0$ the closed-loop eigenvalue goes to $-\infty$, and as $r\to\infty$ it tends to $-a$.

### 6.3 Notes and references (p. 160)
Kalman's original LQR paper is recommended; it contains the first treatment of controllability for linear systems. Not covered: cross-terms in the cost, tracking, output-feedback LQR and its relation to optimal state estimation (Kalman filter). Section 7.3 treats robust control problems as extensions of LQR (p. 160).

## Toy example (ours)
System $\dot x=x+u$, so $A=1$, $B=1$. Cost $\int_0^\infty(x^2+u^2)dt$, so $Q=1$, $R=1$ ($C=1$). $(A,B)$ is controllable and $(A,C)$ observable.
1. ARE (6.28): $2P+1-P^2=0$, so $P=1\pm\sqrt2$.
2. Keep the positive root $P=1+\sqrt2\approx2.414$. Check: $P^2=3+2\sqrt2$ and $2P+1=3+2\sqrt2$, so the difference is $0$. The other root $1-\sqrt2\approx-0.414$ is not $\ge0$.
3. Control: $u^*=-R^{-1}B^TPx=-(1+\sqrt2)x$.
4. Closed loop: $\dot x=(1-(1+\sqrt2))x=-\sqrt2\,x$, exponentially stable, even though the open loop $\dot x=x$ is unstable.
5. Cost from $x_0=1$: $x_0^TPx_0\approx2.414$. Check: $x(t)=e^{-\sqrt2t}$ and $u=-(1+\sqrt2)x$, so the integrand is $(1+(1+\sqrt2)^2)e^{-2\sqrt2t}=(4+2\sqrt2)e^{-2\sqrt2t}$. The integral is $(4+2\sqrt2)/(2\sqrt2)=\sqrt2+1$. ✓
Contrast: with $Q=0$ (Example 6.2) the ARE gives $P=0$, $u=0$, and the closed loop stays unstable.

## Concepts
- [[lqr]] — linear dynamics, quadratic cost on state and control; optimal control is linear state feedback (p. 145)
- [[state-feedback-pole-placement]] — here the linear feedback $u=-R^{-1}B^TPx$ is derived from the necessary conditions, with $P$ given by (6.10) or the RDE (6.14) (p. 147)
- [[riccati-differential-equation]] (new) — quadratic matrix ODE (6.14) for $P(t)$, solved backward from $P(t_1)=M$ (p. 148)
- [[algebraic-riccati-equation]] (new) — static equation (6.28) for the steady-state $P$; may have spurious solutions (p. 154)
- [[hamiltonian-matrix]] (new) — $2n\times2n$ matrix $\mathcal H(t)$ of the canonical state–costate equations (6.7) (p. 147)
- [[finite-escape-time]] (new) — an entry of $P$ blows up in finite backward time; excluded here by the cost bound (p. 151)
- [[bellman-equation-value-function]] — $V=x^TP(t)x$ is the optimal cost-to-go and solves HJB (p. 150)
- [[hamilton-jacobi-bellman-equation]] — specialised to (6.16), used as sufficient condition (p. 149)
- [[pontryagin-maximum-principle]] — gives the unique candidate control with $p^*=-2Px^*$ (p. 146)
- [[controllability-reachability]] — used to bound the infinite-horizon cost, so $P$ exists (p. 154)
- [[observability]] — of $(A,C)$ with $Q=C^TC$; gives stability and $P>0$ (p. 157)
- [[stability]] — closed loop exponentially stable under Theorem 6.1 (p. 158)

## Canonical instances
- [[scalar-integrator-lqr]] — $\dot x=u$; $P=\tanh(t_1-t)$ finite horizon, $P=1$ infinite horizon (p. 152, 159)
- [[unstable-scalar-zero-state-cost]] — $\dot x=x+u$, $J=\int u^2$; optimal control leaves the system unstable (p. 156)
- [[double-integrator-lqr]] — Exercise 6.4 (p. 155)
- [[cheap-vs-expensive-control]] — Exercise 6.6 (p. 159)

## Bridges (candidates)
- [same-math] Substitution $P=-\tfrac12YX^{-1}$ ↔ calculus of variations: second-order sufficient conditions and conjugate points (Section 2.6.2) — author states the correspondence (p. 149, 151).
- [same-math] $\hat V=x^TPx$ decreasing along trajectories ↔ stability theory: Lyapunov function; the author calls this the "Lyapunov argument" (p. 156, 160).
- [structural-analogy] Quadratic cost gives linear law ↔ statistics: Gauss's least squares (footnote 1, p. 147).
- [structural-analogy] Output-feedback LQR and optimal state estimation (Kalman filter) ↔ estimation theory; the text only mentions this relation as not discussed (p. 160).

## Questions this raises
- How do the conditions on $(A,B)$ and $(A,C)$ weaken to stabilizability and detectability, and which claims of Theorem 6.1 survive (Exercise 6.5)?
- How does the closed-loop eigenvalue move as the ratio of $R$ to $Q$ changes (Exercise 6.6)?
- How would $P$ change if the cost had cross terms $x^TNu$, or for a tracking problem (listed in the notes as not discussed)?
- Where exactly does $R>0$ enter the global-existence argument (footnote 2 invites the reader to find out)?

## Exercises worth doing
- Ex. 6.1 (p. 149) — linear $2n\times n$ system reproduces the RDE solution — difficulty: medium
- Ex. 6.2 (p. 151) — symmetry and positive semidefiniteness of $P$; used in 6.1.3 and 6.1.4 — difficulty: medium
- Ex. 6.3 (p. 151) — optimality by square completion only — difficulty: medium
- Ex. 6.4 (p. 155) — double integrator: solve ARE, check it is the steady state of the RDE — difficulty: medium
- Ex. 6.5 (p. 159) — Theorem 6.1 under stabilizability and detectability — difficulty: hard
- Ex. 6.6 (p. 159) — cheap and expensive control limits for a scalar system — difficulty: easy

## Reading notes
- Printed page = pdf − 10 (pdf 155 is printed 145). Pages 145–160 are covered.
- The text layer was readable; equations were checked against the page images.
- Footnote 2 (p. 152) says the standing assumption is that $R$ is "nonnegative", while Section 6.1 assumes $R>0$ (positive definite). The source does not comment on the difference.
- In 6.2.4 the cost uses $R(t)$ in the proof (p. 158) although $R$ is constant in this section. The source does not comment on this.
- Exercises 6.1–6.6 have no printed solutions here.
