---
id: astrom-2021-feedbacksystems/ch05-dynamic
work: astrom-2021-feedbacksystems
unit: "5 Dynamic Behavior"
pages: 5-1 to 5-38
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Dynamic Behavior (Åström & Murray, Ch. 5)

## L0 — One line
Stability of equilibria and other solutions of nonlinear systems can be judged by phase portraits, by linearization (eigenvalues of the Jacobian), or by an energy-like Lyapunov function, and linearization and Lyapunov functions can also be used to design feedback.

## L1 — The gist (≤ 120 words)
How do nonlinear systems behave over time, and how can we prove that an equilibrium is stable? The chapter defines equilibria, limit cycles and stability (Lyapunov and asymptotic). For linear systems, stability follows from the eigenvalues of A. For nonlinear systems, the linearization often decides local stability, and Lyapunov functions (energy-like) give proofs and help design controllers. Examples include pendulums, congestion control, a genetic switch and noise cancellation. Regions of attraction and bifurcations describe behavior far from equilibrium and under parameter changes. This matters because the book mostly designs feedback with linear approximations, and feedback can keep a system near its equilibrium, where the approximation is valid.

**Prerequisites:** ordinary differential equations; vectors and matrices (eigenvalues, symmetric matrices, matrix products); partial derivatives and Taylor series; polar coordinates.

## L2 — Key ideas (5–10 bullets)
- A system under state feedback, $\dot x = F(x)$, has a unique solution for given initial data if $F$ is Lipschitz, i.e. $\|F(x)-F(y)\|<c\|x-y\|$ for some fixed $c$ (the author says this guarantees existence and uniqueness). Without such a condition, a solution may fail to exist for all time (finite escape time) or may be non-unique (pp. 5-3, 5-4).
- A vector field gives the velocity $F(x)$ at every point of the plane. A phase portrait draws trajectories from several initial conditions, which lets us infer the behavior for all of them. They reveal equilibria (where $F=0$) and limit cycles (nonconstant periodic solutions; for a stable one, nearby trajectories converge to it) (pp. 5-5, 5-7).
- Stability (Lyapunov): nearby solutions stay near. Asymptotic stability: they also converge. Unstable: not stable. These are local or global depending on the region of initial conditions (pp. 5-8, 5-10).
- For $\dot x = Ax$, the system is asymptotically stable iff all eigenvalues of $A$ have strictly negative real part. $\mathrm{Re}\,\lambda \le 0$ is not enough (Theorem 5.1, p. 5-13).
- Linearizing at an equilibrium $x_e$ gives $A=\partial F/\partial x|_{x_e}$. If all eigenvalues of $A$ have strictly negative real part (and the remaining nonlinear terms $\tilde F$ are small compared with $\|x\|$ near $x_e$), the nonlinear equilibrium is locally asymptotically stable (Theorem 5.3, p. 5-26). The author adds that it can also be shown that one or more eigenvalues with strictly positive real part make the equilibrium unstable (p. 5-26).
- A Lyapunov function $V$ (an energy-like function, positive definite near the equilibrium, with $\dot V\le 0$ or $\dot V<0$ there) proves local stability (or local asymptotic stability). For a stable linear system, the author says one can always find a quadratic $V=x^TPx$ by choosing $Q\succ0$ (positive definite) and solving the linear equation $A^TP+PA=-Q$; the proof is deferred to Chapter 6 (pp. 5-19, 5-22).
- The Krasovski–Lasalle principle gives asymptotic stability when $\dot V\le0$ (negative semidefinite: it may be zero away from the origin) and the only invariant set (a set that trajectories cannot leave once inside) contained in $\{\dot V=0\}$ is the origin (Theorem 5.4, p. 5-27).
- Beyond local analysis: regions of attraction (the set of initial conditions that converge to an asymptotically stable equilibrium; estimated with level sets $\{V\le r\}$ of $V$) and bifurcations (qualitative change of behavior as parameters change, shown by bifurcation diagrams and root loci, which are plots of the eigenvalues as a parameter varies) (pp. 5-29–5-31).
- Lyapunov functions can also design nonlinear controllers: the pendulum stabilizer and the adaptive noise-cancellation law (pp. 5-27, 5-33).

## L3 — Walkthrough

### 5.1 Solving differential equations
**Setup.** A state-space input/output system is
$$\frac{dx}{dt}=f(x,u),\qquad y=h(x,u),\tag{5.1}$$
with $x\in\mathbb R^n$, $u\in\mathbb R^p$, $y\in\mathbb R^q$, and smooth maps $f,h$ (p. 5-1). MIMO means many inputs and outputs; SISO means $p=q=1$ (p. 5-1). Setting $u=\alpha(x)$ (a simple feedback) gives
$$\frac{dx}{dt}=f(x,\alpha(x))=:F(x).\tag{5.2}$$

**Solutions.** $x(t)$ is a solution on $t_0<t<t_f$ if $\dot x=F(x(t))$ there. In the initial value problem, $x(t_0)=x_0$ is also prescribed. For most equations met here the solution is unique. If $F$ does not depend on time, we may take $t_0=0$ with no loss of generality by using $\tau=t-t_0$ (Exercise 5.1) (p. 5-2).

**Example 5.1 (damped oscillator).** $\ddot q+2\zeta\omega_0\dot q+\omega_0^2 q=0$ with $\zeta<1$. Set $x_1=q$, $x_2=\dot q/\omega_0$:
$$\dot x_1=\omega_0x_2,\qquad \dot x_2=-\omega_0x_1-2\zeta\omega_0x_2 .$$
The book asserts the solution (p. 5-2, 5-3), with $\omega_d=\omega_0\sqrt{1-\zeta^2}$:
$$x_1(t)=e^{-\zeta\omega_0t}\Big(x_{10}\cos\omega_dt+\tfrac1{\omega_d}(\omega_0\zeta x_{10}+x_{20})\sin\omega_dt\Big),$$
$$x_2(t)=e^{-\zeta\omega_0t}\Big(x_{20}\cos\omega_dt-\tfrac1{\omega_d}(\omega_0^2x_{10}+\omega_0\zeta x_{20})\sin\omega_dt\Big).$$
This holds only for $0<\zeta<1$ (underdamped). Figure 5.1 shows the response from $x_0=(1,0)$: an oscillation with exponentially decaying size (p. 5-3). (See Reading notes on these formulas.)

**Existence and uniqueness can fail** (p. 5-3, 5-4):
- *Example 5.2, finite escape time.* $\dot x=x^2$, $x(0)=1$ has solution $x(t)=1/(1-t)$, which goes to infinity as $t\to1$. The solution exists only on $0\le t<1$ (p. 5-3).
- *Example 5.3, non-unique solution.* $\dot x=2\sqrt x$, $x(0)=0$. For every $a\ge0$, $x(t)=0$ for $0\le t\le a$ and $(t-a)^2$ for $t>a$ is a solution; its derivative is $0$ or $2(t-a)$, which equals $2\sqrt{x}$ (p. 5-4).

**Lipschitz condition.** Existence and uniqueness can be guaranteed by requiring, for some fixed $c$,
$$\|F(x)-F(y)\|<c\|x-y\|\quad\text{for all }x,y.$$
This is Lipschitz continuity. A sufficient condition is that the Jacobian $\partial F/\partial x$ is uniformly bounded. In Example 5.2 the derivative becomes large for large $x$. In Example 5.3 it is infinite at the origin (p. 5-4).

*Intuition note.* A differential equation can fail to have a solution for all time, or to have only one, if its right-hand side changes too fast. Bounding how fast $F$ can change (Lipschitz) removes both problems.

### 5.2 Qualitative analysis
**Phase portraits.** For planar systems ($x\in\mathbb R^2$), $F(x)$ is a velocity vector at each point: a *vector field* (Fig. 5.3a). A *phase portrait* plots solutions from several initial conditions, following the arrows (Fig. 5.3b). Points where $F=0$ are stationary: starting there, you stay (p. 5-5). A portrait lets us infer the behavior for all initial conditions rather than a single one. It does not readily show the rate of change, though arrow lengths hint at it (p. 5-5).

**Equilibrium points.** $x_e$ is an equilibrium of $\dot x=F(x)$ if $F(x_e)=0$; then $x(t)=x_e$ for all $t\ge0$. A system can have zero, one or more (p. 5-6).

**Example 5.4 (inverted pendulum).** States $x_1=\theta$, $x_2=\dot\theta$; input $u$ is the pivot acceleration. With $mgl/J_t=1$, $l/J_t=1$, $c=\gamma/J_t$:
$$\frac{dx}{dt}=\begin{pmatrix}x_2\\ \sin x_1-cx_2+u\cos x_1\end{pmatrix}.\tag{5.5}$$
With $u=0$ the equilibria are $x_e=(\pm n\pi,0)$, $n=0,1,2,\dots$. Even $n$ is pendulum up; odd $n$ is hanging down. Figure 5.4c covers $-2\pi\le x_1\le2\pi$, so five of the equilibrium points are shown (p. 5-6, 5-7).

**Limit cycles.** The normalized oscillator
$$\dot x_1=x_2+x_1(1-x_1^2-x_2^2),\qquad \dot x_2=-x_1+x_2(1-x_1^2-x_2^2)\tag{5.6}$$
has solutions converging to a circle (Fig. 5.5). Formally, a nonconstant solution $x_p(t)$ is a limit cycle of period $T>0$ if $x_p(t+T)=x_p(t)$ for all $t$ and nearby trajectories converge to $x_p$ as $t\to\infty$ (stable) or $t\to-\infty$ (unstable) (p. 5-7). Methods exist for second-order systems, but for general higher-order systems one has to resort to computation. Stable limit cycles can often be found by simulating from different initial conditions (p. 5-7).

### 5.3 Stability
**Definitions.** Let $x(t;a)$ be the solution with initial condition $a$. It is *stable* (in the sense of Lyapunov) if for every $\epsilon>0$ there is $\delta>0$ with
$$\|b-a\|<\delta\implies\|x(t;b)-x(t;a)\|<\epsilon\ \text{ for all }t>0.$$
This does not say the solutions approach each other. $\delta$ may depend on $\epsilon$. If a solution is stable and nearby trajectories do not converge, it is *neutrally stable* (p. 5-8). For an equilibrium:
$$\|x(0)-x_e\|<\delta\implies\|x(t)-x_e\|<\epsilon\ \text{ for all }t>0.\tag{5.7}$$
Figure 5.7 ($\dot x_1=x_2,\ \dot x_2=-x_1$) is neutrally stable. Trajectories may leave the $\delta$-circle, so $\delta<\epsilon$ is needed (p. 5-8).

*Asymptotically stable* means stable and also $\lim_{t\to\infty}\|x(t;b)-x(t;a)\|=0$ for $b$ close to $a$. For an equilibrium:
$$\|x(0)-x_e\|<\delta\implies\|x(t)-x_e\|<\epsilon\ \text{ and }\ \lim_{t\to\infty}x(t)=x_e.\tag{5.8}$$
Figure 5.8 ($\dot x_1=x_2,\ \dot x_2=-x_1-x_2$) is an example (p. 5-9). A solution is *unstable* if it is not stable: for some $\epsilon$, no $\delta$ works. Figure 5.9 ($\dot x_1=2x_1-x_2,\ \dot x_2=-x_1+2x_2$) is unstable (p. 5-10).

*Local vs global.* A solution is locally stable (or locally asymptotically stable) if stable for initial conditions in $B_r(a)=\{x:\|x-a\|<r\}$, $r>0$. It is globally asymptotically stable if asymptotically stable for all $r>0$ (p. 5-10).

*Names for planar equilibria* (p. 5-10): asymptotically stable = *sink* (attractor). Unstable = *source* (all trajectories leave) or *saddle* (some approach, others leave). Stable but not asymptotically stable = *center*.

**Example 5.5 (congestion control).** With $N$ identical sources and one router, window size $w$, buffer $b$ (model from Sec. 4.4):
$$\frac{dw}{dt}=\frac cb-\rho c\Big(1+\frac{w^2}{2}\Big),\qquad \frac{db}{dt}=N\frac{wc}{b}-c .$$
Equilibria: $b_e=Nw_e$ with $w_e(1+w_e^2/2)=1/(N\rho)$. Since $w(1+w^2/2)$ is monotone, there is only one equilibrium. In Figure 5.10 ($N=60$) the author reads from the phase portraits that all initial conditions converge to it, so it is asymptotically stable. The equilibrium buffer is below the 500-packet capacity (p. 5-11).

**Stability of linear systems.** $\dot x=Ax$, $x(0)=x_0$, $A\in\mathbb R^{n\times n}$ (5.9). Define $\lambda(A)=\{s\in\mathbb C:\det(sI-A)=0\}$; $\det(sI-A)$ is the characteristic polynomial. The origin is always an equilibrium. Stability depends only on $A$, so it is a property of the system (pp. 5-11, 5-12).
- *Diagonal $A$* (5.10): the states decouple, $x_j(t)=e^{\lambda_jt}x_j(0)$. The origin is stable if $\lambda_j\le0$ and asymptotically stable if $\lambda_j<0$ (p. 5-12).
- *Block diagonal* with $2\times2$ blocks $\begin{pmatrix}\sigma_j&\omega_j\\-\omega_j&\sigma_j\end{pmatrix}$: eigenvalues $\sigma_j\pm i\omega_j$ and
$$x_{2j-1}(t)=e^{\sigma_jt}\big(x_{2j-1}(0)\cos\omega_jt+x_{2j}(0)\sin\omega_jt\big),\quad x_{2j}(t)=e^{\sigma_jt}\big(-x_{2j-1}(0)\sin\omega_jt+x_{2j}(0)\cos\omega_jt\big).$$
Asymptotically stable iff $\sigma_j=\mathrm{Re}\,\lambda_j<0$ for all $j$ (p. 5-12).
- *General case with distinct eigenvalues:* there is $T\in\mathbb R^{n\times n}$ with $TAT^{-1}$ (block) diagonal (Exercise 5.14). With $z=Tx$: $\dot z=T\dot x=TAx=TAT^{-1}z$. Eigenvalues are unchanged, and $x=T^{-1}z$, so stability type carries back. Hence for distinct eigenvalues, stability is determined by the real parts of the eigenvalues (pp. 5-12, 5-13).

**Theorem 5.1 (stability of a linear system).** $\dot x=Ax$ is asymptotically stable if and only if all eigenvalues of $A$ have strictly negative real part. It is unstable if any eigenvalue has strictly positive real part (proved in the next chapter) (p. 5-13).

It is not enough that $\mathrm{Re}\,\lambda\le0$: $\ddot q=0$, i.e. $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, has $\lambda=0$ but $x_1(t)=x_{1,0}+x_{2,0}t$, $x_2=x_{2,0}$ is unbounded (p. 5-13).

*Intuition note.* Each eigenvalue is a mode $e^{\lambda t}$. It shrinks if its real part is negative and grows if positive. A zero real part is the borderline case and needs separate treatment.

**Example 5.6 (compartment model; Sec. 4.6).**
$$\dot x=\begin{pmatrix}-k_0-k_1&k_1\\k_2&-k_2\end{pmatrix}x+\begin{pmatrix}b_0\\0\end{pmatrix}u,\qquad y=\begin{pmatrix}0&1\end{pmatrix}x.$$
Output feedback $u=-k(y-y_d)+u_d$ gives
$$\dot x=\begin{pmatrix}-k_0-k_1&k_1-b_0k\\k_2&-k_2\end{pmatrix}x+\begin{pmatrix}b_0\\0\end{pmatrix}(u_d+ky_d)=:Ax+Bu_e .$$
Solving $Ax_e+Bu_e=0$ gives $x_{1,e}=x_{2,e}=y_d$ and $u_e=u_d=\frac{k_0}{b_0}y_d$ (as printed). With $z=x-x_e$, the characteristic polynomial is
$$\lambda(s)=s^2+(k_0+k_1+k_2)s+(k_0k_2+b_0k_2k).$$
By the Routh–Hurwitz criterion the roots have negative real part as long as the linear and constant terms are both positive. Hence the system is stable for any $k>0$ (p. 5-14).

**Stability via linear approximation.**
*Example 5.7 (inverted pendulum, $u=0$).* Near $x=(0,0)$ (up), replace $\sin x_1\approx x_1$:
$$\dot x=\begin{pmatrix}0&1\\1&-c\end{pmatrix}x.\tag{5.11}$$
Its equilibrium is unstable (phase portrait or eigenvalues). Near $x=(\pi,0)$ (down), use $\sin(\pi+\theta)\approx-\theta$ and set $z_1=x_1-\pi$, $z_2=x_2$:
$$\dot z=\begin{pmatrix}0&1\\-1&-c\end{pmatrix}z.\tag{5.12}$$
Its eigenvalues have negative real parts, so the downward equilibrium is asymptotically stable. Figure 5.11 shows the nonlinear and linear portraits nearly identical near the equilibrium. The author states that if the linear approximation has asymptotically stable or unstable equilibria, the local stability of the original system must be the same (pp. 5-14, 5-15).

*General linearization.* Taylor-expand around $x_e$ with $F(x_e)=0$ and set $z=x-x_e$:
$$\frac{dz}{dt}=Az,\qquad A=\frac{\partial F}{\partial x}\Big|_{x_e}.\tag{5.13}$$
This is the linear approximation (linearization) at $x_e$ (pp. 5-15, 5-16).

**Example 5.8 (tanker).** Normalized steering: $\dot v=a_1v+a_2r+\alpha v|v|+b_1\delta$, $\dot r=a_3v+a_4r+b_2\delta$. Here $v$ is the sideways velocity, $r$ the turning rate and $\delta$ the rudder angle. Parameters: $a_1=-0.6$, $a_2=-0.3$, $a_3=-5$, $a_4=-2$, $\alpha=-2$, $b_1=0.1$, $b_2=-0.8$. With $\delta=0$, equilibria solve $a_1v+a_2r+\alpha v|v|=0$ and $a_3v+a_4r=0$. Eliminating $r$:
$$(a_1a_4-a_2a_3)v+\alpha a_4v|v|=0,$$
which has solutions $v_e=0$ and $v_e=\pm0.075$. Linearizations:
$$A_0=\begin{pmatrix}-0.6&-0.3\\-5&-2\end{pmatrix},\qquad A_1=\begin{pmatrix}-0.9&-0.3\\-5&-2\end{pmatrix}.$$
$A_0$ has characteristic polynomial $s^2+2.6s-0.3$, with one right-half-plane root: unstable. $A_1$ has $s^2+2.9s+0.3$, with all roots in the left half-plane: stable. So going straight ($v_e=r_e=0$) is unstable. The stable equilibria $(v_e,r_e)=(\mp0.075,\pm0.1875)$ are circular motions to the left or right. With the rudder at zero, the ship turns one way or the other depending on the initial condition (p. 5-16).

The author notes that a local linear approximation can be used to design feedback that keeps the system near its equilibrium. This in turn keeps the approximation valid (p. 5-16).

**Stability of limit cycles, Example 5.9.** For (5.6), a periodic solution is
$$x_p=\begin{pmatrix}x_1(0)\cos t+x_2(0)\sin t\\x_2(0)\cos t-x_1(0)\sin t\end{pmatrix},\quad x_1^2(0)+x_2^2(0)=1,\tag{5.14}$$
on which the nonlinear terms vanish. Use polar coordinates $x_1=r\cos\varphi$, $x_2=r\sin\varphi$. Differentiating gives $\dot x_1=\dot r\cos\varphi-r\dot\varphi\sin\varphi$ and $\dot x_2=\dot r\sin\varphi+r\dot\varphi\cos\varphi$. Solving for $\dot r,\dot\varphi$ gives, "after some calculation",
$$\frac{dr}{dt}=r(1-r^2),\qquad\frac{d\varphi}{dt}=-1.\tag{5.15}$$
These are decoupled. For $r\ge0$ the equilibria are $r=0$ (unstable) and $r=1$ (stable): $\dot r>0$ for $0<r<1$ and $\dot r<0$ for $r>1$. All solutions with $r(0)>0$ converge to $r=1$. Also $\varphi(t)=-t+\varphi(0)$, so solutions with different $\varphi(0)$ keep a constant angle separation. Thus $r=1,\varphi=-t$ is stable but not asymptotically stable. The unit circle is attracting, with a constant phase shift between solutions (Fig. 5.13) (pp. 5-17, 5-18).

### 5.4 Lyapunov stability analysis
We study $\dot x=F(x)$ (5.16) with $x_e=0$ (otherwise use $z=x-x_e$). For physical systems, stability can often be argued from dissipation of energy. Lyapunov functions generalize energy (p. 5-18, 5-19).

**Definitions.** $V:\mathbb R^n\to\mathbb R$ continuous. On the ball $B_r=B_r(0)$ it is *positive definite* if $V(x)>0$ for $x\ne0$ and $V(0)=0$; *negative definite* if $V<0$ for $x\neq 0$, $V(0)=0$; *positive semidefinite* if $V\ge0$ (it may vanish elsewhere). Example: $V_1=x_1^2$ is semidefinite (zero at $(0,c)$); $V_2=x_1^2+x_2^2$ is positive definite (p. 5-19).

**Theorem 5.2 (Lyapunov stability theorem).** Let $\dot V=\frac{\partial V}{\partial x}\frac{dx}{dt}=\frac{\partial V}{\partial x}F(x)$. If there is $r>0$ such that $V$ is positive definite and $\dot V$ is negative semidefinite on $B_r$, then $x=0$ is (locally) stable in the sense of Lyapunov. If $V$ is positive definite and $\dot V$ is negative definite on $B_r$, then $x=0$ is (locally) asymptotically stable (p. 5-19).

A function $V$ meeting one of these conditions is a (local) *Lyapunov function*. Geometrically, level sets $V(x)=c$ are closed contours. $\dot V<0$ means the vector field points toward lower contours (Fig. 5.14), so trajectories move to smaller $V$, and if $\dot V$ is negative definite, $x$ must approach 0 (p. 5-19).

*Intuition note.* $V$ is like stored energy that can never increase along a trajectory. If it strictly decreases, the state has to slide down to the bottom, the equilibrium.

Finding $V$ is not always easy. For $\dot x_1=x_2$, $\dot x_2=-x_1-\alpha x_2$, $\alpha>0$, the eigenvalues $\lambda=(-\alpha\pm\sqrt{\alpha^2-4})/2$ have negative real part, so the system is asymptotically stable. The candidate $V=\frac12x_1^2+\frac12x_2^2$ gives $\dot V=-\alpha x_2^2$, which is zero at $x=(1,0)$. So it does not prove asymptotic stability by Theorem 5.2 (p. 5-20).

**Example 5.10 (scalar).** $\dot x=\frac{2}{1+x}-x$ has equilibria $x=1$, $x=-2$. With $z=x-1$: $\dot z=\frac2{2+z}-z-1$. Take $V=\frac12z^2$ (globally positive definite). Then $\dot V=z\dot z=\frac{2z}{2+z}-z^2-z$. On $B_r$ with $r<2$ we have $2+z>0$, so multiply by $2+z$:
$$2z-(z^2+z)(2+z)=-z^3-3z^2=-z^2(z+3)<0\quad(z\in B_r,\ r<2,\ z\ne0).$$
So $x=1$ is locally asymptotically stable (pp. 5-20, 5-21).

**Example 5.11 (hanging pendulum).** $\dot x_1=x_2$, $\dot x_2=-\sin x_1$. Use total energy $V=1-\cos x_1+\frac12x_2^2\approx\frac12x_1^2+\frac12x_2^2$ (positive definite near 0). Then $\dot V=\dot x_1\sin x_1+\dot x_2x_2=x_2\sin x_1-x_2\sin x_1=0$. This is negative semidefinite, so the equilibrium is stable, not necessarily asymptotically stable. A perturbed pendulum moves along a constant-energy trajectory (p. 5-21).

Lyapunov functions are not unique. The author states that they can always be found for any stable system under certain conditions, and conversely. Sum-of-squares methods give systematic search for polynomial and hybrid systems (p. 5-21).

**Linear systems: Lyapunov equation.** Take $V=x^TPx$ with $P=P^T\in\mathbb R^{n\times n}$. $V$ positive definite $\iff$ $P\succ0$ ($x^TPx>0$ for all $x\ne0$). For symmetric $P$ this holds iff all its eigenvalues are real and positive (p. 5-22). Then
$$\dot V=\frac{\partial V}{\partial x}\frac{dx}{dt}=x^T(A^TP+PA)x=:-x^TQx .$$
Asymptotic stability needs $Q\succ0$. So it is sufficient to choose $Q\succ0$ and solve the Lyapunov equation
$$A^TP+PA=-Q.\tag{5.17}$$
This is linear in the entries of $P$. A solution always exists if all eigenvalues of $A$ are in the left half-plane, and $P\succ0$ if $Q\succ0$. So a stable linear system always has a quadratic Lyapunov function (proof deferred to Chapter 6; Exercise 5.6) (p. 5-22).

*Intuition note.* Choosing $Q$ and solving a linear equation for $P$ turns "find an energy function" into plain linear algebra for stable linear systems.

**Example 5.12 (spring–mass).** $\dot x_1=x_2$, $\dot x_2=-\frac kmx_1-\frac bmx_2$ ($m,b,k>0$). With $Q=I$, (5.17) reads
$$\begin{pmatrix}0&-k/m\\1&-b/m\end{pmatrix}\begin{pmatrix}p_{11}&p_{12}\\p_{12}&p_{22}\end{pmatrix}+\begin{pmatrix}p_{11}&p_{12}\\p_{12}&p_{22}\end{pmatrix}\begin{pmatrix}0&1\\-k/m&-b/m\end{pmatrix}=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}.$$
Elementwise:
$$-\frac{2k}{m}p_{12}=-1,\qquad p_{11}-\frac bmp_{12}-\frac kmp_{22}=0,\qquad 2p_{12}-\frac{2b}{m}p_{22}=-1.$$
Solution:
$$P=\begin{pmatrix}\frac{b^2+k(k+m)}{2bk}&\frac m{2k}\\ \frac m{2k}&\frac{m(k+m)}{2bk}\end{pmatrix},\qquad V(x)=\frac{b^2+k(k+m)}{2bk}x_1^2+\frac mkx_1x_2+\frac{m(k+m)}{2bk}x_2^2 .$$
$V$ is positive definite, with rotated-ellipse level sets (p. 5-22, 5-23).

**Nonlinear systems with linear part.** Write $\dot x=F(x)=:Ax+\tilde F(x)$ with $F(0)=0$ and $\tilde F$ containing second- and higher-order terms (5.18). Find $V$ for the linear part, then check whether it works for the full system (p. 5-23).

**Example 5.13 (genetic switch).** Two mutually repressing proteins (Fig. 5.15a), with inputs set to zero:
$$\frac{dz_1}{d\tau}=\frac\mu{1+z_2^n}-z_1,\qquad\frac{dz_2}{d\tau}=\frac\mu{1+z_1^n}-z_2,\tag{5.19}$$
$n,\mu>0$. Let $f(u)=\frac\mu{1+u^n}$, $f'(u)=\frac{-\mu nu^{n-1}}{(1+u^n)^2}$. Dynamics: $\dot z_1=f(z_2)-z_1$, $\dot z_2=f(z_1)-z_2$. Equilibria satisfy $z_1=f(z_2)$, $z_2=f(z_1)$: intersections of two curves (Fig. 5.15b). The author says it can be shown there are always three: one with $z_{1e}=z_{2e}$, one with $z_{1e}<z_{2e}$, one with $z_{1e}>z_{2e}$. For $\mu\gg1$:
$$z_{1e}\approx\mu,\ z_{2e}\approx\tfrac1{\mu^{n-1}};\qquad z_{1e}=z_{2e};\qquad z_{1e}\approx\tfrac1{\mu^{n-1}},\ z_{2e}\approx\mu.\tag{5.20}$$
*Linearize* via the Taylor series of $f$ about $u_e$. With $w=z-z_e$:
$$\frac{dw}{dt}=\begin{pmatrix}-1&f'(z_{2e})\\f'(z_{1e})&-1\end{pmatrix}w+\tilde F(w).$$
Write $f_1'=f'(z_{1e})$, $f_2'=f'(z_{2e})$. Solve (5.17) with $Q=I$ and symmetric $P$ ($p_{21}=p_{12}$):
$$\begin{pmatrix}-2p_{11}+2f_1'p_{12}&p_{11}f_2'-2p_{12}+p_{22}f_1'\\ p_{11}f_2'-2p_{12}+p_{22}f_1'&-2p_{22}+2f_2'p_{12}\end{pmatrix}=\begin{pmatrix}-1&0\\0&-1\end{pmatrix},$$
giving
$$p_{11}=-\frac{f_1'^2-f_2'f_1'+2}{4(f_1'f_2'-1)},\quad p_{12}=-\frac{f_1'+f_2'}{4(f_1'f_2'-1)},\quad p_{22}=-\frac{f_2'^2-f_1'f_2'+2}{4(f_1'f_2'-1)} .$$
*Positive definiteness.* A symmetric $2\times2$ $P$ has real eigenvalues with $\lambda_1+\lambda_2=\mathrm{trace}(P)$, $\lambda_1\lambda_2=\det(P)$. Both positive requires $\mathrm{trace}(P)>0$ and $\det(P)>0$, with
$$\mathrm{trace}(P)=\frac{f_1'^2-2f_2'f_1'+f_2'^2+4}{4-4f_1'f_2'},\qquad\det(P)=\frac{f_1'^2-2f_2'f_1'+f_2'^2+4}{16-16f_1'f_2'} .$$
Here $\mathrm{trace}(P)=4\det(P)$ and the numerator is $(f_1'-f_2')^2+4>0$, so it suffices to check the sign of $1-f_1'f_2'$. Thus $P\succ0$ requires $f'(z_{1e})f'(z_{2e})<1$.
*Check at the unequal equilibria,* using (5.20):
$$f'(z_{1e})f'(z_{2e})\approx f'(\mu)f'\!\Big(\tfrac1{\mu^{n-1}}\Big)=\frac{-\mu n\mu^{n-1}}{(1+\mu^n)^2}\cdot\frac{-\mu n\mu^{-(n-1)^2}}{(1+\mu^{-n(n-1)})^2}\approx n^2\mu^{-n^2+n}.$$
With $n=2$, $\mu\approx200$ (from Exercise 3.10) this is $\ll1$, so $P\succ0$ and $V=w^TPw$ is a candidate Lyapunov function.
*Derivative.* $\dot V=w^T(PA+A^TP)w+\tilde F^T(w)Pw+w^TP\tilde F(w)=-w^Tw+\tilde F^T(w)Pw+w^TP\tilde F(w)$. The last two terms are at least third order in $w$. So sufficiently close to $w=0$, $\dot V$ is negative definite, and both unequal equilibria are stable (p. 5-25).
*Skip path:* carry forward the condition $f'(z_{1e})f'(z_{2e})<1$ (needed for $P\succ0$; the author finds $f'f'\ll1$ at the two unequal equilibria for $n=2$, $\mu\approx200$) and the conclusion that those two equilibria are stable (sufficiently close to them).
*Bistability.* Figure 5.16 ($\mu=4$): if protein B starts above A, the solution goes to about $(1/\mu^{n-1},\mu)$; if A is above B, to about $(\mu,1/\mu^{n-1})$. The author states that the equilibrium with $z_{1e}=z_{2e}$ is unstable (p. 5-25; Fig. 5.16, p. 5-26).

**Theorem 5.3.** Consider (5.18) with $F(0)=0$ and $\tilde F$ such that $\|\tilde F(x)\|/\|x\|\to0$ as $\|x\|\to0$. If the real parts of all eigenvalues of $A$ are strictly less than zero, then $x_e=0$ is a locally asymptotically stable equilibrium of (5.18) (p. 5-26).
So stabilizing the linear approximation gives a stable equilibrium of the nonlinear system. The proof follows Example 5.13 (formal proof in [Kha01]). It can also be shown that an eigenvalue with strictly positive real part makes $x_e=0$ unstable (p. 5-26).

*Intuition note.* Close to the equilibrium the nonlinear terms are much smaller than the linear one. So the linear model's verdict carries over locally, if the linear verdict is clear (strictly negative or strictly positive real parts).

**Krasovski–Lasalle invariance principle.** It applies to time-invariant (or periodic) systems and allows $\dot V\le0$ instead of $\dot V<0$; asymptotic stability then needs the extra condition on invariant sets in Theorem 5.4. The $\omega$ *limit set* of $x(t;a)$ is the set of $z$ such that $x(t_n;a)\to z$ for some strictly increasing times $t_n$. A set $M$ is *invariant* if $b\in M\Rightarrow x(t;b)\in M$ for all $t\ge0$. The $\omega$ limit set of every trajectory is closed and invariant (p. 5-26, 5-27).

**Theorem 5.4.** Let $V$ be locally positive definite such that on the compact set $\Omega_r=\{x:V(x)\le r\}$ we have $\dot V(x)\le0$. Define $S=\{x\in\Omega_r:\dot V(x)=0\}$. As $t\to\infty$ the trajectory tends to the largest invariant set inside $S$ (its $\omega$ limit set is contained in it). In particular, if $S$ contains no invariant set other than $x=0$, then 0 is asymptotically stable (p. 5-27).

*Intuition note.* If energy stops falling only where $\dot V=0$, the state can stay there forever only if it can actually stay in that set. If the only set where it can stay is the origin, the state tends to the origin.

**Example 5.14 (stabilized inverted pendulum).**
$$\dot x_1=x_2,\qquad\dot x_2=\sin x_1+u\cos x_1.\tag{5.22}$$
Take $V=(\cos x_1-1)+a(1-\cos^2x_1)+\frac12x_2^2\approx(a-\frac12)x_1^2+\frac12x_2^2$, positive definite near the origin if $a>0.5$. Then
$$\dot V=-\dot x_1\sin x_1+2a\dot x_1\sin x_1\cos x_1+\dot x_2x_2=x_2(u+2a\sin x_1)\cos x_1 .$$
Choosing $u=-2a\sin x_1-x_2\cos x_1$ gives $\dot V=-x_2^2\cos^2x_1$. So the equilibrium is locally stable, but Theorem 5.2 does not give asymptotic stability. $\dot V=0$ means $x_2=0$ or $x_1=\pi/2\pm n\pi$. In a small neighborhood $\Omega_r$, $r\ll\pi/2$, $S=\{x_2=0\}$. To stay in $S$ we need $x_2\equiv0$, so $\dot x_2\equiv0$, which by (5.22) forces $x_1\equiv0$. So the largest invariant set in $S$ is the origin, and by Theorem 5.4 the origin is locally asymptotically stable (Fig. 5.17b). The angle really lives on a manifold ($\theta=2\pi\equiv\theta=0$, Fig. 5.17c); the analysis is more complicated but uses the same ideas (p. 5-28).

### 5.5 Parametric and nonlocal behavior
**Regions of attraction.** Local behavior is behavior near an equilibrium. Far away, solutions can differ: in the stabilized pendulum, some trajectories go to other equilibria or swing over the top several times (p. 5-29). The *region of attraction* of an asymptotically stable equilibrium is the set of all initial conditions converging to it (shaded in Fig. 5.17b). It is hard to compute in general, but patches that are attracting can often be found. If $V$ is a local Lyapunov function about $x_0$, $\Omega_r=\{V(x)\le r\}$, and $\dot V\le0$ on $\Omega_r$ with equality only at $x_0$, then $\Omega_r$ lies inside the region of attraction. This estimate depends on the choice of $V$ and can be very conservative. If $V$ is positive definite and $\dot V$ negative (semi-)definite for all $x$, then in many instances the region of attraction is the whole space (global asymptotic stability); see [Kha01] (p. 5-29).

*Example 5.15.* For the pendulum $V$ above with $a>0.5$, $\dot V$ is negative semidefinite for all $x$. Any $x$ with $|x_1|<\pi/2$ and $V(x)>0$ lies inside the invariant set defined by the level curves of $V$ (one is shown in Fig. 5.17b) (p. 5-30).

**Bifurcations.** Consider $\dot x=F(x,\mu)$, $x\in\mathbb R^n$, $\mu\in\mathbb R^k$ (5.23). Equilibria satisfy $F(x,\mu)=0$. The system has a *bifurcation* at $\mu=\mu^*$ if its behavior changes qualitatively there, through a change in stability type or in the number of solutions (p. 5-30).

**Example 5.16 (predator–prey).**
$$\frac{dH}{dt}=rH\Big(1-\frac Hk\Big)-\frac{aHL}{c+H},\qquad\frac{dL}{dt}=b\frac{aHL}{c+H}-dL,\tag{5.24}$$
$H$ hares (prey), $L$ lynxes (predators). There is an equilibrium $H_e,L_e>0$, found numerically. Nominal values: $a=3.2$, $b=0.6$, $c=50$, $d=0.56$, $k=125$, $r=1.6$. Figure 5.18a, a numerically computed parametric stability diagram in $(a,c)$, shows stable and unstable regions. Figure 5.18b, a bifurcation diagram, plots $H_e$ against $a$ (other parameters nominal). A solid line is a stable and a dashed line an unstable equilibrium. It matches the stability diagram for $c=50$ and $a$ from 1.35 to 4. When the equilibrium is unstable, the solution converges to a stable limit cycle, whose amplitude is the dash-dotted line (pp. 5-30, 5-31).

**Root locus.** A common bifurcation for linear systems: the equilibrium stays fixed but its stability changes with parameters. A plot of eigenvalues versus parameters is a *root locus diagram*. Bifurcations occur at parameter values where an eigenvalue has zero real part (p. 5-31; more in Sec. 12.5).

**Example 5.17 (bicycle).** The linear bicycle model (4.8) with states $x=(\varphi,\delta,\dot\varphi,\dot\delta)$, steering torque $T=0$:
$$\dot x=\begin{pmatrix}0&I\\-M^{-1}(K_0+K_2v_0^2)&-M^{-1}Cv_0\end{pmatrix}x=:Ax,$$
$I$ is $2\times2$, so $A$ is $4\times4$; $v_0$ is velocity. The bicycle is unstable at low velocity (two eigenvalues in the right half-plane), becomes self-stabilizing as these cross to the left, and for higher velocity a small eigenvalue near the origin returns to the right half-plane. Because it is small, a rider can easily stabilize it. Fig. 5.19a shows self-stabilization for velocities between 6 and 10 m/s (pp. 5-31, 5-32). Parameter choice matters; software such as AUTO, LOCBIF, XPPAUT produces such diagrams (p. 5-32).

**Design of nonlinear dynamics using feedback.** Most of the book uses linear approximations, but some problems need nonlinear controllers (p. 5-32). For $\dot x=f(x,u)$, $V$ is a *control Lyapunov function* if for every $x$ there is $u$ with $\dot V=\frac{\partial V}{\partial x}f(x,u)<0$. Then it may be possible to find $\alpha(x)$ so that $u=\alpha(x)$ stabilizes the system (p. 5-33).

**Example 5.18 (noise cancellation).** Headphones have an outside microphone (noise $n$) and an inside one (signal $e$ = desired signal $S$ plus penetrating noise). The outside signal is filtered and subtracted; a feedback mechanism adjusts the filter parameters to minimize the inside noise. This feedback is nonlinear because it changes filter parameters (Fig. 5.20) (p. 5-33). Model noise propagation as
$$\dot z=a_0z+b_0n,\tag{5.25}$$
with unknown $a_0<0$, $b_0$. The filter is $\dot w=aw+bn$ with adjustable $a,b$. If $a=a_0$, $b=b_0$ then $e=S$. Take $S=0$ and $x_1=e=z-w$, $x_2=a-a_0$, $x_3=b-b_0$. The book gives
$$\frac{dx_1}{dt}=a_0(z-w)+(a-a_0)w+(b-b_0)n=a_0x_1+x_2w+x_3n\tag{5.26}$$
(as printed; see Reading notes). Choose $V=\frac12(\alpha x_1^2+x_2^2+x_3^2)$. Then
$$\dot V=\alpha x_1\dot x_1+x_2\dot x_2+x_3\dot x_3=\alpha a_0x_1^2+x_2(\dot x_2+\alpha wx_1)+x_3(\dot x_3+\alpha nx_1).$$
Choosing
$$\dot a=\dot x_2=-\alpha we,\qquad\dot b=\dot x_3=-\alpha ne\tag{5.27}$$
gives $\dot V=\alpha a_0x_1^2<0$ (given $a_0<0$ and $\alpha>0$, the sign being implied by the author's claim that $V$ decreases). So $V$ decreases while $e\ne0$. The law (5.27) does not use the model (5.25) explicitly. In simulation (Fig. 5.21), a sinusoidal signal buried in broadband noise becomes visible with cancellation; the parameters move quickly from $a=b=0$. Practical filters are of higher order (pp. 5-33, 5-34).

*Intuition note.* The adaptive law changes the filter's parameters in the direction that makes a Lyapunov function fall. So the law tries to push the error down without using the noise model (5.25) explicitly.

### 5.6 Further reading
The author recommends Strogatz and Abraham–Shaw for readable introductions to dynamical systems, several technical texts, and Khalil as the comprehensive treatment of Lyapunov stability (p. 5-34).

## Toy example
*(Our own, not from the text.)* Scalar system $\dot x=F(x)=-x+x^3$.

1. Equilibria: $F=0\Rightarrow x(-1+x^2)=0\Rightarrow x=0,\pm1$.
2. Linearization (5.13): $F'(x)=-1+3x^2$. At $0$: $A=-1<0$. Here $\tilde F=x^3$ and $|x^3|/|x|=x^2\to0$, so Theorem 5.3 gives local asymptotic stability. At $x=1$: $A=-1+3=2>0$, so unstable.
3. Lyapunov equation (5.17): $A^TP+PA=-Q$ with $A=-1$, $Q=1$: $-2P=-1$, so $P=\tfrac12$ and $V=\tfrac12x^2$.
4. Check $\dot V=xF(x)=-x^2(1-x^2)$. It is $<0$ for $0<|x|<1$, so by Theorem 5.2 the origin is locally asymptotically stable. For $|x|>1$, $\dot V>0$.
5. Region of attraction estimate: $\Omega_r=\{x^2/2\le r\}$ has $|x|\le\sqrt{2r}$. For $r<\tfrac12$ this lies inside $|x|<1$, where $\dot V<0$ except at 0, so $\Omega_r$ is inside the region of attraction (the actual region is $|x|<1$).
6. Numbers (Euler step $h=0.1$): from $x=0.5$: $F=-0.5+0.125=-0.375$, $x\to0.5+0.1(-0.375)=0.4625$; $V$ goes from $0.125$ to $0.4625^2/2=0.21390625/2\approx0.1070$ (decrease). Also $\dot V=-0.25(1-0.25)=-0.1875=0.5\cdot(-0.375)$. From $x=1.5$: $F=-1.5+3.375=1.875$, $x\to1.6875$ (moves away).

## Concepts
- [[stability]] — Lyapunov: for each $\epsilon$ there is $\delta$ so solutions starting $\delta$-close stay $\epsilon$-close for all $t>0$; weaker than convergence (p. 5-8)
- [[asymptotic-stability]] (new) — stable and nearby solutions converge to the solution, eq. (5.8) (p. 5-9)
- [[equilibrium-point]] (new) — a state $x_e$ with $F(x_e)=0$; constant operating condition (p. 5-6)
- [[phase-portrait]] (new) — plot of trajectories in the plane over the vector field $F(x)$ (p. 5-5)
- [[limit-cycle]] (new) — nonconstant periodic solution that nearby trajectories approach (stable) or leave (unstable) (p. 5-7)
- [[lipschitz-continuity]] (new) — $\|F(x)-F(y)\|<c\|x-y\|$; guarantees existence and uniqueness (p. 5-4)
- [[finite-escape-time]] (new) — solution goes to infinity at a finite time, e.g. $\dot x=x^2$ (p. 5-3)
- [[state-space-model]] — $\dot x=f(x,u)$, $y=h(x,u)$, possibly nonlinear (p. 5-1)
- [[linearization]] — $\dot z=Az$, $A=\partial F/\partial x|_{x_e}$; local asymptotic stability follows if all eigenvalues have strictly negative real part; the author also says one or more strictly positive real parts give instability (pp. 5-15, 5-26)
- [[eigenvalues and modes]] — linear $\dot x=Ax$ is asymptotically stable iff all $\mathrm{Re}\,\lambda<0$ (Thm 5.1) (p. 5-13)
- [[lyapunov-function]] (new) — energy-like $V$ with $V>0$, $\dot V\le0$ (or $<0$) near equilibrium (p. 5-19)
- [[lyapunov-equation]] (new) — $A^TP+PA=-Q$; gives quadratic $V=x^TPx$ for stable linear systems (p. 5-22)
- [[invariance-principle]] (new) — Krasovski–Lasalle: with $\dot V\le0$ on $\Omega_r$, trajectories tend to the largest invariant set inside $S=\{x\in\Omega_r:\dot V=0\}$ (p. 5-27)
- [[region-of-attraction]] (new) — set of initial conditions converging to an asymptotically stable equilibrium (p. 5-29)
- [[bifurcation]] (new) — qualitative change in behavior at a parameter value (p. 5-30)
- [[root-locus]] (new) — plot of eigenvalues as a parameter varies (here only introduced) (p. 5-31)
- [[control-lyapunov-function]] (new) — $V$ such that for every $x$ some $u$ gives $\dot V<0$ (p. 5-33)
- [[feedback]] — here $u=\alpha(x)$, the system regulating itself (p. 5-1)

## Canonical instances
- [[inverted-pendulum]] — open-loop unstable upright equilibrium; stabilized by a Lyapunov-based law plus Krasovski–Lasalle (pp. 5-6, 5-14, 5-27)
- [[damped-oscillator]] — explicit solution, phase portrait with solutions approaching the origin (pp. 5-2, 5-3, 5-5)
- [[tcp-congestion-control]] — unique, asymptotically stable equilibrium (p. 5-10)
- [[compartment-model]] — feedback gain $k>0$ stabilizes drug concentration (p. 5-13)
- [[tanker-steering]] — three equilibria; straight motion unstable (p. 5-16)
- [[genetic-switch]] — bistable repressor pair, Lyapunov check (p. 5-23)
- [[predator-prey]] — stability diagram, bifurcation, limit cycle (p. 5-30)
- [[bicycle-model]] — self-stabilizing for velocities between 6 and 10 m/s (Fig. 5.19a) (p. 5-32)
- [[noise-cancelling-headphones]] — adaptive nonlinear feedback from a Lyapunov function (p. 5-33)

## Bridges (candidates)
- [structural-analogy] Lyapunov function $V$ ↔ physics: total energy with dissipation — $\dot V\le0$ plays the role of energy loss (p. 5-18).
- [same-math] Linearization and Jacobian eigenvalues ↔ dynamical-systems analysis of any fixed point: same criterion on $\partial F/\partial x$.
- [metaphor] Bistable genetic switch (two stable states, an unstable middle) ↔ social/economic models with two stable regimes and tipping.
- [structural-analogy] Adaptive law $\dot a=-\alpha we$, $\dot b=-\alpha ne$ ↔ machine learning: stochastic-gradient / LMS-style parameter updates driven by an error signal.
- [structural-analogy] Predator–prey cycle (a stable limit cycle when the equilibrium is unstable) ↔ cyclical dynamics in economics or epidemics.

## Questions this raises
- When $A$ has an eigenvalue with zero real part, what decides the stability of the nonlinear system? (Theorem 5.3 and the remark on p. 5-26 do not cover this.)
- Is there a constructive way to find Lyapunov functions for general nonlinear systems, beyond energy and sum-of-squares (p. 5-21)?
- How can region-of-attraction estimates be made less conservative than one level set of one $V$ (p. 5-29)?
- How do the pendulum and noise-cancellation designs behave when states or parameters are only measured with noise?

## Exercises worth doing
- Ex. 5.3 (p. 5-35) — test two candidate Lyapunov functions on a second-order system and find conditions — difficulty: medium
- Ex. 5.4 (p. 5-36) — use Krasovski–Lasalle to prove asymptotic stability of a damped spring–mass system from the energy $V$ — difficulty: medium
- Ex. 5.6 (p. 5-36) — show the Lyapunov equation (5.17) has a solution when $A$ is stable — difficulty: hard
- Ex. 5.9 (p. 5-37) — plot eigenvalues versus feedback gain $k$ (root locus) — difficulty: easy
- Ex. 5.10 (p. 5-37) — discrete-time Lyapunov argument for asymptotic stability — difficulty: medium
- Ex. 5.13 (p. 5-38) — equilibria and Lyapunov stability of a self-activating genetic circuit — difficulty: hard

## Reading notes
- Page labels give no printed number, but each page image shows a printed header such as "5-1", "5-2", …, "5-38". References here use these, written (p. 5-N). Offset: printed 5-N = pdf − 152.
- Example 5.1: I checked the printed solution against the initial derivatives at $t=0$. $\dot x_1(0)$ should equal $\omega_0x_{20}$ and $\dot x_2(0)$ should equal $-\omega_0x_{10}-2\zeta\omega_0x_{20}$. The printed $x_1$ gives $x_{20}$ and the printed $x_2$ gives $-\omega_0^2x_{10}-2\zeta\omega_0x_{20}$. So the printed formulas may be missing or misplaced factors of $\omega_0$. I report them as printed.
- p. 5-20: the text says $\dot V=-\alpha x_2^2$ "is not positive definite". The intended meaning is that $\dot V$ is not negative definite (it is $0$ at $(1,0)$).
- p. 5-25: the numerator "$(f_1-f_2)^2+4$" is printed without primes; it should be $(f_1'-f_2')^2+4$, consistent with the trace and det formulas above it.
- Example 5.18, eq. (5.26): with $x_1=e=z-w$, my own algebra gives $\dot x_1=a_0x_1-x_2w-x_3n$ (minus signs), while the page prints plus signs. The text after (5.27) also writes $e=x_1=w-z$, opposite to the definition $x_1=z-w$. The Lyapunov argument is otherwise as printed; I did not re-derive the update law with the corrected signs.
- Example 5.15 as printed says $\dot V$ is "nonzero when $x_1\ne\pm\pi/2$"; from $\dot V=-x_2^2\cos^2x_1$ it is nonzero only if also $x_2\ne0$. I reported the passage loosely.
- Theorem 5.2's "negative semidefinite" and the Lyapunov-based claims are as printed. The proofs of Theorems 5.1–5.4 are not given in this chapter (deferred to Chapter 6 or to references).
