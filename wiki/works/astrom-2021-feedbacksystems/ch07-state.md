---
id: astrom-2021-feedbacksystems/ch07-state
work: astrom-2021-feedbacksystems
unit: "7 State Feedback"
pages: 7-1 to 7-36
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 5
---
# State Feedback

## L0 — One line
If a single-input linear system is reachable, feeding back its full state can place the closed-loop eigenvalues anywhere, so the designer can shape the dynamics directly; practical limits are actuator size, the choice of eigenvalues, and the need for exact calibration (integral action removes the calibration need; an optimal cost is another way to choose the gains).

## L1 — The gist (≤ 120 words)
The chapter asks what feedback of the full state can do to a linear system's dynamics. Answer: if the single-input system is reachable (its reachability matrix has full rank), the law u = −Kx + k_f r can give the closed loop any chosen characteristic polynomial. The feedforward gain k_f then fixes the steady state. Limits: eigenvalue choice is hard, and fast eigenvalues will in general require large control signals. Integral action removes the need for exact calibration. The linear quadratic regulator (LQR) instead picks K by minimising a cost that trades state error against control effort. This matters because the eigenvalue locations shape the behavior of the closed loop.

**Prerequisites:** matrix–vector algebra (rank, determinant, inverse); eigenvalues and characteristic polynomial; linear ODE x' = Ax + Bu and its convolution solution; change of coordinates z = Tx; step response (rise time, overshoot, settling time).

## L2 — Key ideas (5–10 bullets)
- **Reachability** means any state can be reached from any other in finite time by some input. For $\dot x = Ax+Bu$ it holds iff $W_r=(B\ AB\ \cdots\ A^{n-1}B)$ has full rank (Theorem 7.1). It does not depend on the time allowed (p. 7-4).
- **Unreachability** can arise, for example, when a linear combination $Hx$ of the states stays constant, or when identical subsystems share one input. In the constant-combination case $HW_r=0$ (p. 7-6).
- **Reachable canonical form** exists for every reachable system. The coefficients of the characteristic polynomial appear directly in $\tilde A$, so state feedback can rewrite them one by one (Theorems 7.2, 7.3; pp. 7-9, 7-13, 7-14, 7-15).
- **Eigenvalue assignment** (Theorem 7.3): for a reachable single-input system, $u=-Kx+k_fr$ gives any desired closed-loop polynomial. $k_f=-1/(C(A-BK)^{-1}B)$ makes the zero-frequency gain (the steady-state gain from $r$ to $y$) equal to 1, but this needs exact knowledge of the model (pp. 7-11, 7-14, 7-15).
- **Where to put eigenvalues** is the hard design question. Second-order formulas (damping ratio $\zeta$ and natural frequency $\omega_0$) and the dominant pair (the complex pair closest to the imaginary axis) give guidance. Large eigenvalues will in general need large and fast control signals (pp. 7-19 to 7-24).
- **Integral action** augments the state with $z=\int(y-r)\,dt$. If the closed loop is stable, $y=r$ in steady state without calibration, and constant disturbances are rejected (pp. 7-25, 7-26).
- **LQR** picks $K=Q_u^{-1}B^TS$, where $S$ solves a Riccati equation (a matrix equation), to minimise a quadratic cost. The weights $Q_x,Q_u$ trade performance against effort. For constant matrices over an infinite horizon, a reachable system gives a unique stabilising positive definite $S$ (positive definite: $x^TSx>0$ for every nonzero $x$) (pp. 7-28, 7-29).
- Worked examples (steering, predator–prey, drug dosing, balance system, cruise control, thrust aircraft, web server) show the same recipe on different systems (pp. 7-11 to 7-32).

## L3 — Walkthrough

### Opening (p. 7-1)
The chapter shows how feedback of the state can shape local behavior of a system. It introduces reachability and uses it to design dynamics through eigenvalue assignment. Under certain conditions the eigenvalues can be assigned arbitrarily (p. 7-1). The epigraph (Kalman, Falb, Arbib) says the state may intuitively be regarded as a kind of memory or accumulation of past causes, and that the set of states must be rich enough to carry all information needed to predict the effect of the past on the future (p. 7-1).

### 7.1 Reachability

**Setting.** The output is ignored; study $\dot x=Ax+Bu$ with $x\in\mathbb R^n$, $u\in\mathbb R$, $A$ an $n\times n$ matrix, $B$ a column vector (7.1, p. 7-1).

**Definitions.** The reachable set $\mathcal R(x_0,\le T)$ is the set of all $x_f$ for which some input $u(t)$, $0\le t\le T$, steers $x(0)=x_0$ to $x(T)=x_f$ (p. 7-2).

*Definition 7.1.* A linear system is reachable if for any $x_0,x_f\in\mathbb R^n$ there exist $T>0$ and $u:[0,T]\to\mathbb R$ such that $x(0)=x_0$ implies $x(T)=x_f$ (p. 7-2).

Reachability concerns reaching points transiently. Equilibria are special because constant input lets us stay there. The set of equilibria for constant controls is
$$\mathcal R_{eq}=\{x_e: Ax_e+Bu_e=0\ \text{for some } u_e\in\mathbb R\}.$$
This lies in a one-dimensional (or possibly higher) subspace. If $A$ is invertible it is one-dimensional, spanned by $A^{-1}B$ (p. 7-2).

**Example 7.1 (double integrator).** $\dot x_1=x_2,\ \dot x_2=u$. The equilibria are the $x_1$ axis with $u_e=0$. To go from $(a,0)$ with $a>0$ to the origin, first set $u<0$ so $x_2<0$ and $x_1$ decreases. Later set $u>0$ to bring $x_2$ back toward zero. A positive $x_2$ moves the state the other way (p. 7-3). Points with $x_2\ne0$ can only be passed through transiently (p. 7-3).

**Testing for reachability (heuristic argument with impulses, i.e. idealised infinitely short inputs of unit area, $\delta(t)$; p. 7-3).** With $x(0)=0$,
$$x(t)=\int_0^t e^{A(t-\tau)}Bu(\tau)\,d\tau.\tag{7.2}$$
An impulse input $\delta(t)$ gives $x_\delta(t)=e^{At}B$. Differentiating the impulse response gives the response to $\dot\delta$: $x_{\dot\delta}(t)=Ae^{At}B$. By linearity, the input
$$u=\alpha_1\delta+\alpha_2\dot\delta+\cdots+\alpha_n\delta^{(n-1)}$$
gives $x(t)=\alpha_1e^{At}B+\alpha_2Ae^{At}B+\cdots+\alpha_nA^{n-1}e^{At}B$. Letting $t\to0^+$,
$$\lim_{t\to0^+}x(t)=\alpha_1B+\alpha_2AB+\cdots+\alpha_nA^{n-1}B.$$
This is a linear combination of the columns of the **reachability matrix**
$$W_r=\begin{pmatrix}B&AB&\cdots&A^{n-1}B\end{pmatrix}.\tag{7.3}$$
To reach an arbitrary point we need $n$ independent columns (full rank). For one input this is the same as a nonzero determinant (p. 7-4). The same test works for several inputs (then $W_r$ must have full column rank). Only terms up to $A^{n-1}B$ are needed (Exercise 7.3) (p. 7-4).

Impulses are violent signals. For smooth inputs, write $x(t)=\int_0^te^{A\tau}Bu(t-\tau)d\tau$. By the Cayley–Hamilton theorem (every square matrix satisfies its own characteristic polynomial), $e^{A\tau}=I\alpha_0(\tau)+A\alpha_1(\tau)+\cdots+A^{n-1}\alpha_{n-1}(\tau)$ with scalar functions $\alpha_i$. Therefore
$$x(t)=B\!\int_0^t\!\alpha_0(\tau)u(t-\tau)d\tau+AB\!\int_0^t\!\alpha_1(\tau)u(t-\tau)d\tau+\cdots+A^{n-1}B\!\int_0^t\!\alpha_{n-1}(\tau)u(t-\tau)d\tau.$$
This is again a combination of the columns of $W_r$ (p. 7-4).

*Theorem 7.1 (Reachability rank condition).* A linear system (7.1) is reachable if and only if $W_r$ is invertible (full column rank) (p. 7-4). The formal proof is beyond the scope of the text; it follows the sketch above and is found in books on linear control theory. The theorem does not mention the time $T$. For a linear system an input exists for any $T>0$, but it may need to be very large when $T$ is very small (p. 7-4).

> **Intuition note.** The columns $B, AB, A^2B,\dots$ are the directions the input can push the state directly or through the dynamics. If they span the whole space, nothing is out of reach. Short time only costs larger inputs.

**Example 7.2 (balance system; pp. 7-4 to 7-6).** The nonlinear equations (7.4) are
$$(M+m)\ddot q-ml\cos\theta\,\ddot\theta=-c\dot q-ml\sin\theta\,\dot\theta^2+F,\qquad (J+ml^2)\ddot\theta-ml\cos\theta\,\ddot q=-\gamma\dot\theta+mgl\sin\theta.$$
Take $c=\gamma=0$ and linearise at $x_e=(0,0,0,0)$:
$$A=\begin{pmatrix}0&0&1&0\\0&0&0&1\\0&m^2l^2g/\mu&0&0\\0&M_tmgl/\mu&0&0\end{pmatrix},\quad B=\begin{pmatrix}0\\0\\J_t/\mu\\lm/\mu\end{pmatrix},$$
with $\mu=M_tJ_t-m^2l^2$, $M_t=M+m$, $J_t=J+ml^2$. The reachability matrix is
$$W_r=\begin{pmatrix}0&J_t/\mu&0&gl^3m^3/\mu^2\\0&lm/\mu&0&gl^2m^2M_t/\mu^2\\J_t/\mu&0&gl^3m^3/\mu^2&0\\lm/\mu&0&gl^2m^2M_t/\mu^2&0\end{pmatrix}.\tag{7.5}$$
Permuting the first and last columns changes the determinant by a factor $-1$ and gives a block diagonal matrix with two identical blocks. Then
$$\det W_r=-\Big(\frac{gl^4m^4}{\mu^3}-\frac{gl^2m^2J_tM_t}{\mu^3}\Big)^2=-\frac{g^2l^4m^4}{\mu^6}(MJ+mJ+Mml^2)^2 .$$
The text concludes the system is reachable. So we can move from any state to any state, and in particular to an equilibrium (p. 7-6).

**Mechanisms of non-reachability (p. 7-6).**
- Two identical systems driven by the same input (Figure 7.3, two identical pendula on one cart): they cannot be made to do different things, so arbitrary states are not reachable (Exercise 7.4).
- A constant linear combination of states: suppose a row vector $H$ has $0=\frac d{dt}Hx=H(Ax+Bu)$ for all $x,u$. Then $H$ is in the left null space of $A$ and $B$, so $HW_r=H(B\ AB\ \cdots\ A^{n-1}B)=0$ and $W_r$ is not full rank. If $Hx_0\ne Hx_f$, no input moves $x_0$ to $x_f$.

**Reachable canonical form (pp. 7-7, 7-8).** A change of coordinates $z=Tx$ can bring a system into a form that is easy to analyse. The system is in reachable canonical form if
$$\frac{dz}{dt}=\begin{pmatrix}-a_1&-a_2&-a_3&\cdots&-a_n\\1&0&&&\\&1&0&&0\\&&\ddots&\ddots&\\&0&&1&0\end{pmatrix}z+\begin{pmatrix}1\\0\\0\\\vdots\\0\end{pmatrix}u,\qquad y=\begin{pmatrix}b_1&b_2&\cdots&b_n\end{pmatrix}z+du.\tag{7.6}$$
This is a chain of integrators (Figure 7.4). The characteristic polynomial is
$$\lambda(s)=s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n.\tag{7.7}$$
Its reachability matrix $\tilde W_r$ is upper triangular with ones on the diagonal; the first row is $1,-a_1,a_1^2-a_2,\dots$ and the last two entries of the final column are $-a_1$ and $1$. Because of this triangular structure it is full rank (p. 7-8).

**Transforming to canonical form (p. 7-8).** With $z=Tx$: $\tilde A=TAT^{-1}$, $\tilde B=TB$. Then $\tilde A\tilde B=TAT^{-1}TB=TAB$, $\tilde A^2\tilde B=TA^2B$, …, $\tilde A^n\tilde B=TA^nB$. Hence
$$\tilde W_r=T\begin{pmatrix}B&AB&\cdots&A^{n-1}B\end{pmatrix}=TW_r.\tag{7.8}$$
If $W_r$ is invertible, $T=\tilde W_rW_r^{-1}$.

**Example 7.3 (p. 7-8, 7-9).** $\dot x=\begin{pmatrix}\alpha&\omega\\-\omega&\alpha\end{pmatrix}x+\begin{pmatrix}0\\1\end{pmatrix}u$. The characteristic polynomial is $s^2-2\alpha s+(\alpha^2+\omega^2)$, so $a_1=-2\alpha$, $a_2=\alpha^2+\omega^2$. We have $W_r=\begin{pmatrix}0&\omega\\1&\alpha\end{pmatrix}$ and $\tilde W_r=\begin{pmatrix}1&-a_1\\0&1\end{pmatrix}$. Then
$$T=\tilde W_rW_r^{-1}=\begin{pmatrix}-(a_1+\alpha)/\omega&1\\1/\omega&0\end{pmatrix}=\begin{pmatrix}\alpha/\omega&1\\1/\omega&0\end{pmatrix},\qquad z=Tx=\begin{pmatrix}\alpha x_1/\omega+x_2\\x_1/\omega\end{pmatrix}.$$

*Theorem 7.2 (Reachable canonical form).* Let $A,B$ be dynamics and control matrices of a reachable system with $\det(sI-A)=s^n+a_1s^{n-1}+\cdots+a_n$. Then there is a transformation $z=Tx$ giving the form (7.6) (p. 7-9). So for a reachable system we may assume canonical coordinates without loss of generality, which is useful in proofs. For high-order systems, small changes in the $a_i$ can give large changes in the eigenvalues, so the form is not always well conditioned (p. 7-9).

### 7.2 Stabilization by State Feedback

The state permits prediction of future evolution given future inputs. The design is limited to a linear state model with a single input, and uses one idea: position the closed-loop eigenvalues (p. 7-9).

**Controller structure (p. 7-10).** Figure 7.5 shows the process, controller elements $K$ and $k_f$, reference $r$ and process disturbance $v$ (entering additively at the input). The goal is that $y$ tracks $r$ despite disturbances and uncertainty. Performance specifications include stability (an asymptotically stable equilibrium for constant $r$ with no disturbance), step-response properties (rise time, overshoot, settling time), and disturbance attenuation (p. 7-10).

For $\dot x=Ax+Bu,\ y=Cx+Du$ (7.9), assume all states are measured. Since the state holds all information needed to predict the future, the most general time-invariant control law is $u=\alpha(x,r)$. A linear one is
$$u=-Kx+k_fr,\tag{7.10}$$
with $r$ a constant. The minus sign is a convention for negative feedback; $k_fr$ is a feedforward term. The closed loop is
$$\dot x=(A-BK)x+Bk_fr.\tag{7.11}$$
We seek $K$ so that the closed loop has characteristic polynomial $p(s)=s^n+p_1s^{n-1}+\cdots+p_n$ (7.12). This is the **eigenvalue assignment (pole placement) problem** (p. 7-11).

$k_f$ does not affect stability (determined by the eigenvalues of $A-BK$) but does affect the steady state. At equilibrium $x_e=-(A-BK)^{-1}Bk_fr$ and $y_e=Cx_e+Du_e$. Choose $k_f$ so that $y_e=r$. If $D=0$,
$$k_f=-1/\big(C(A-BK)^{-1}B\big),\tag{7.13}$$
which is exactly the inverse of the closed-loop zero-frequency gain (p. 7-11).

**Example 7.4 (vehicle steering; pp. 7-11 to 7-13).** From the normalised model, $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $B=\begin{pmatrix}\gamma\\1\end{pmatrix}$, $C=(1\ 0)$, $D=0$, where $\gamma=a/b$ is the ratio of the centre-of-mass-to-rear-wheel distance $a$ to the wheelbase $b$. With $u=-k_1x_1-k_2x_2+k_fr$:
$$\dot x=\begin{pmatrix}-\gamma k_1&1-\gamma k_2\\-k_1&-k_2\end{pmatrix}x+\begin{pmatrix}\gamma k_f\\k_f\end{pmatrix}r,\quad y=(1\ 0)x\tag{7.14}$$
and $\det(sI-A+BK)=s^2+(\gamma k_1+k_2)s+k_1$. Matching to $p(s)=s^2+2\zeta_c\omega_cs+\omega_c^2$ gives $k_1=\omega_c^2$, $k_2=2\zeta_c\omega_c-\gamma\omega_c^2$. Equation (7.13) gives $k_f=k_1=\omega_c^2$. The law is
$$u=\omega_c^2(r-x_1)-(2\zeta_c\omega_c-\gamma\omega_c^2)x_2.$$
Figure 7.6: response speed rises with $\omega_c$, but larger $\omega_c$ also gives larger initial control action. With $\zeta_c=0.7$ and $\omega_c=0.5,0.7,1$, overshoot is below 5% (15 cm for $b=3$ m). Settling times are 3–6 normalised units, about 2–4 s at $v_0=15$ m/s. Smaller $\zeta_c$ gives faster response but more overshoot. For $\omega_c=0.7$ and a step of 0.2, the initial steering angle is 0.1 rad, "aggressive but not unreasonable" at moderate speed; $\zeta_c=0.7$ gives about 5% overshoot (pp. 7-12, 7-13).

**State feedback in reachable canonical form (pp. 7-13, 7-14).** For (7.15), the coefficient $a_k$ can be changed by feedback from $z_k$ to $u$ (Figure 7.4). With $u=-\tilde Kz+k_fr=-\tilde k_1z_1-\cdots-\tilde k_nz_n+k_fr$ (7.16), the closed loop (7.17) has the first row of $\tilde A$ changed to $-a_i-\tilde k_i$ and $B=(k_f,0,\dots,0)^T$ for input $r$. Its characteristic polynomial is $s^n+(a_1+\tilde k_1)s^{n-1}+\cdots+(a_n+\tilde k_n)$. Setting this equal to $p(s)$ gives $\tilde k_i=p_i-a_i$:
$$\tilde K=\begin{pmatrix}p_1-a_1&p_2-a_2&\cdots&p_n-a_n\end{pmatrix}.\tag{7.18}$$
For unit zero-frequency gain, set the right side of (7.17) to zero. Then $z_{e,1},\dots,z_{e,n-1}$ are zero, $(-a_n-\tilde k_n)z_{e,n}+k_fr=0$ and $y_e=b_nz_{e,n}$. So
$$k_f=\frac{a_n+\tilde k_n}{b_n}=\frac{p_n}{b_n}.\tag{7.19}$$
The precise values of $a_n,b_n$ must be known, so the gain is obtained by precise calibration. This differs from integral action, discussed later (p. 7-14).

**General case (p. 7-14).** Change coordinates $z=Tx$ into canonical form, apply (7.16) with (7.18), and transform back: $u=-\tilde KTx+k_fr$, so $K=\tilde KT$.

*Theorem 7.3 (Eigenvalue assignment by state feedback).* Consider the single-input single-output system (7.20) with $\lambda(s)=s^n+a_1s^{n-1}+\cdots+a_n$ the characteristic polynomial of $A$. If the system is reachable, there is a control law $u=-Kx+k_fr$ that gives closed-loop polynomial $p(s)$ and unity zero-frequency gain between $r$ and $y$. The gain is
$$K=\tilde KT=\begin{pmatrix}p_1-a_1&\cdots&p_n-a_n\end{pmatrix}\tilde W_rW_r^{-1},\tag{7.21}$$
with $W_r=(B\ AB\ \cdots\ A^{n-1}B)$ and $\tilde W_r=\begin{pmatrix}1&a_1&a_2&\cdots&a_{n-1}\\&1&a_1&\cdots&a_{n-2}\\&&\ddots&\ddots&\vdots\\0&&&1&a_1\\&&&&1\end{pmatrix}^{-1}$. Also $k_f=-1/(C(A-BK)^{-1}B)$ (p. 7-15).

For simple problems, treat the $k_i$ as unknowns, compute $\det(sI-A+BK)$, and equate coefficients with $p(s)$. This gives linear equations, which can always be solved if the system is reachable, as in Example 7.4. Equation (7.21) is **Ackermann's formula** (MATLAB `acker`). `place` is preferable for high-order systems because it is better conditioned numerically (p. 7-15).

> **Intuition note.** In canonical form each gain moves exactly one polynomial coefficient, so you can set all coefficients independently. Reachability guarantees you can reach this form. The formula $K=\tilde KT$ just translates the gains back.

**Example 7.5 (predator–prey; pp. 7-15 to 7-17).** Model:
$$\dot H=(r+u)H\Big(1-\frac Hk\Big)-\frac{aHL}{c+H},\qquad \dot L=b\frac{aHL}{c+H}-dL.$$
Parameters: $a=3.2,\ b=0.6,\ c=50,\ d=0.56,\ k=125,\ r=1.6$. The hare growth rate is modulated by $u$ (for example through a food source), and the output is the lynx count $L$. Equilibrium $x_e\approx(20.6,29.5)$. Linearisation:
$$\frac d{dt}\begin{pmatrix}z_1\\z_2\end{pmatrix}=\begin{pmatrix}0.13&-0.93\\0.57&0\end{pmatrix}\begin{pmatrix}z_1\\z_2\end{pmatrix}+\begin{pmatrix}17.2\\0\end{pmatrix}v,\quad w=(0\ 1)z.$$
The system is reachable (p. 7-16). Chosen eigenvalues are $\{-0.1,-0.2\}$, giving $K=(0.025\ \ -0.052)$ and $k_f=0.002$ from (7.13). The law in original coordinates is
$$u=-(0.025\ \ -0.052)\begin{pmatrix}H-20.6\\L-29.5\end{pmatrix}+0.002(L_d-29.5).$$
Figure 7.7: starting from 15 hares and 20 lynxes, the lynx population settles at the reference $L_d=30$, and the dynamics differ greatly from the natural ones (p. 7-16).

**Caveats (p. 7-17).** State feedback assumes all states are measured (output feedback and estimation come in the next chapter). Theorem 7.3 is idealised and assumes high-precision process knowledge. Robustness is treated in Chapter 13 (p. 7-17).

### 7.3 Design Considerations

Eigenvalue location is the main decision, and there are trade-offs among input magnitude, robustness and performance (p. 7-17).

**Second-order systems (pp. 7-17 to 7-20).** Canonical form:
$$\ddot q+2\zeta\omega_0\dot q+\omega_0^2q=k\omega_0^2u,\quad y=q.\tag{7.22}$$
In state space with $x=(q,\dot q/\omega_0)$:
$$\dot x=\begin{pmatrix}0&\omega_0\\-\omega_0&-2\zeta\omega_0\end{pmatrix}x+\begin{pmatrix}0\\k\omega_0\end{pmatrix}u,\quad y=(1\ 0)x.\tag{7.23}$$
Eigenvalues: $\lambda=-\zeta\omega_0\pm\omega_0\sqrt{\zeta^2-1}$. The system is stable if $\omega_0>0$ and $\zeta>0$. They are complex if $\zeta<1$ and real otherwise (p. 7-18). Here $\zeta$ is the **damping ratio** and $\omega_0$ the **natural frequency**.

*Natural response ($u=0$; p. 7-18).*
- $\zeta>1$ (overdamped): $y(t)=\frac{\beta x_{10}+x_{20}}{\beta-\alpha}e^{-\alpha t}-\frac{\alpha x_{10}+x_{20}}{\beta-\alpha}e^{-\beta t}$ with $\alpha=\omega_0(\zeta+\sqrt{\zeta^2-1})$, $\beta=\omega_0(\zeta-\sqrt{\zeta^2-1})$.
- $\zeta=1$ (critically damped): $y(t)=e^{-\zeta\omega_0t}\big(x_{10}+(x_{20}+\zeta\omega_0x_{10})t\big)$. This is still asymptotically stable if $\omega_0>0$.
- $0<\zeta<1$ (underdamped): $y(t)=e^{-\zeta\omega_0t}\big(x_{10}\cos\omega_dt+(\tfrac{\zeta\omega_0}{\omega_d}x_{10}+\tfrac1{\omega_d}x_{20})\sin\omega_dt\big)$, with damped frequency $\omega_d=\omega_0\sqrt{1-\zeta^2}$. For $\zeta\ll1$, $\omega_d\approx\omega_0$. For $\zeta=0$ the oscillation frequency is $\omega_0$.

*Step response with $x(0)=0$ (7.24, p. 7-18):*
$$y(t)=\begin{cases}k\Big(1-e^{-\zeta\omega_0t}\cos\omega_dt-\frac{\zeta}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_0t}\sin\omega_dt\Big),&\zeta<1\\[2pt]k\big(1-e^{-\omega_0t}(1+\omega_0t)\big),&\zeta=1\\[2pt]k\Big(1-\tfrac12\big(\tfrac{\zeta}{\sqrt{\zeta^2-1}}+1\big)e^{-\omega_0t(\zeta-\sqrt{\zeta^2-1})}+\tfrac12\big(\tfrac{\zeta}{\sqrt{\zeta^2-1}}-1\big)e^{-\omega_0t(\zeta+\sqrt{\zeta^2-1})}\Big),&\zeta>1.\end{cases}$$
Figure 7.8: with $k=1$, a larger $\zeta$ lengthens the rise time but reduces overshoot. The shape is set by $\zeta$ and the speed by $\omega_0$ (p. 7-19).

*Step-response properties (p. 7-19).* For $\zeta<1$ rewrite
$$y(t)=k\Big(1-\frac1{\sqrt{1-\zeta^2}}e^{-\zeta\omega_0t}\sin(\omega_dt+\varphi)\Big),\quad\varphi=\arccos\zeta.\tag{7.25}$$
Maximum overshoot occurs at the first zero of $\dot y$ and equals $M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}$. Rise time is normally the time to go from $p\%$ to $(100-p)\%$ of the final value (typically $p=5$ or $10$). The alternative, the inverse of the steepest slope, is $T_r=\frac1{\omega_0}e^{\varphi/\tan\varphi}$.

**Table 7.1** (0 < ζ ≤ 1; p. 7-20):

| Property | Value | ζ=0.5 | ζ=1/√2 | ζ=1 |
|---|---|---|---|---|
| Steady-state | $k$ | $k$ | $k$ | $k$ |
| Rise time | $T_r=e^{\varphi/\tan\varphi}/\omega_0$ | 1.8/ω₀ | 2.2/ω₀ | 2.7/ω₀ |
| Overshoot | $M_p$ | 16% | 4% | 0% |
| Settling (2%) | $T_s\approx4/\zeta\omega_0$ | 8.0/ω₀ | 5.6/ω₀ | 4.0/ω₀ |

*Frequency response (pp. 7-19, 7-20)* (the steady output's gain $M$ and phase $\theta$ for a sinusoidal input of frequency $\omega$): $Me^{i\theta}=\frac{k\omega_0^2}{(i\omega)^2+2\zeta\omega_0(i\omega)+\omega_0^2}=\frac{k\omega_0^2}{\omega_0^2-\omega^2+2i\zeta\omega_0\omega}$. The resonant peak (the maximum gain over frequency) grows as $\zeta$ falls, and is described by $Q=1/2\zeta$ (Figure 7.9).

**Table 7.2** (0 < ζ ≤ 1; p. 7-20; bandwidth = the frequency where the gain falls to $1/\sqrt2$ of its zero-frequency value):

| Property | Value | ζ=0.1 | ζ=0.5 | ζ=1/√2 |
|---|---|---|---|---|
| Zero-frequency gain | $M_0=k$ | $k$ | $k$ | $k$ |
| Bandwidth | $\omega_b=\omega_0\sqrt{1-2\zeta^2+\sqrt{(1-2\zeta^2)^2+1}}$ | 1.54ω₀ | 1.27ω₀ | ω₀ |
| Resonant peak gain | $M_r=k/(2\zeta\sqrt{1-\zeta^2})$ if $\zeta\le\sqrt2/2$; N/A otherwise | 5k | 1.15k | k |
| Resonant frequency | $\omega_{mr}=\omega_0\sqrt{1-2\zeta^2}$ if $\zeta\le\sqrt2/2$; 0 otherwise | ω₀ | 0.707ω₀ | 0 |

> **Intuition note.** $\zeta$ decides the shape (ringing or not) and $\omega_0$ sets the speed. Choosing both for a second-order closed loop gives you overshoot and rise time from simple formulas.

**Example 7.6 (drug administration; pp. 7-20 to 7-22).** Two-compartment model $\dot c=\begin{pmatrix}-k_0-k_1&k_1\\k_2&-k_2\end{pmatrix}c+\begin{pmatrix}b_0\\0\end{pmatrix}u$, $y=(0\ 1)c$. Both concentrations are assumed measurable; the aim is to hold $y$ at $r$. Choose $\zeta=1/\sqrt2$ and $T_r=10$ min. Table 7.1 then gives $\omega_0=0.22$. The text states the closed-loop eigenvalues satisfy $\lambda(s)=-0.2\pm0.096i$, uses $\tilde k_1=-0.2$, $\tilde k_2=0.2$ (with $K=(\tilde k_1,\tilde k_2)$ to avoid clashing with the rates $k_i$), and gets $k_f=0.065$ from (7.13). Figure 7.10: compared with periodic pulsed doses (open loop), the state-feedback dose keeps the concentration with substantially less variability (p. 7-22).

**Higher-order systems (pp. 7-21, 7-22).** Eigenvalue assignment is harder. A complex pair $\lambda,\lambda^*$ of a stable system is **dominant** if it is closest to the imaginary axis; ties are broken by the lowest damping ratio $\zeta=-\operatorname{Re}\lambda/|\lambda|$. Argument: in Jordan form (a block-diagonal form splitting the system into simple subsystems) the response is a sum of subsystem responses. For $\zeta<1$ the slowest is the subsystem nearest the imaginary axis (Figure 7.8). So after other transients die out, the dominant pair is the main factor. This does not always hold (for example if non-dominant terms have larger coefficients), but often the dominant eigenvalues determine the step response (p. 7-22).

The only formal requirement for assignment is reachability. In practice, large eigenvalues need large and fast control signals, and actuators limit the choice (Chapters 12–14) (p. 7-22).

**Example 7.7 (balance system; pp. 7-23, 7-24).** With $c,\gamma\neq 0$,
$$A=\begin{pmatrix}0&0&1&0\\0&0&0&1\\0&m^2l^2g/\mu&-cJ_t/\mu&-\gamma lm/\mu\\0&M_tmgl/\mu&-clm/\mu&-\gamma M_t/\mu\end{pmatrix},\quad B=\begin{pmatrix}0\\0\\J_t/\mu\\lm/\mu\end{pmatrix}.$$
Parameters: $M=10$ kg, $m=80$ kg, $c=0.1$, $J=100$, $l=1$ m, $\gamma=0.01$, $g=9.8$. Open-loop eigenvalues $\approx0,\,-0.0011,\,\pm2.68$.
- Fast dynamics (pendulum): $\omega_0=\sqrt{mgl/(J+ml^2)}\approx2.1$ rad/s. Choose $\zeta=0.5$ and eigenvalues $\approx-1\pm2i$ (using $\sqrt{1-\zeta^2}\approx1$).
- Slow dynamics (cart position): damping 0.7 and natural frequency 0.5 (rise time about 5 s), giving $-0.35\pm0.35i$.
- Result: $K=(-15.6\ \ 1730\ \ -50.1\ \ 443)$, $k_f=-15.6$. The step response is good, but the input force is almost three times gravity at its peak (Figure 7.11a).
- Redesign: slow the fast pair by about a factor 3 (same damping). Slow the second pair too (damping 0.7, "frequency to 1", rise time about 10 s). The eigenvalues become $\{-0.33\pm0.66i,\ -0.18\pm0.18i\}$, with a much more reasonable input (Figure 7.11b).

The text concludes that choosing eigenvalues is hard, a principal limitation of the approach for higher dimensions. Optimal control (Section 7.5) and frequency-domain design (Chapters 9–13) are alternatives (p. 7-24).

### 7.4 Integral Action

State feedback achieves the correct steady state by careful calibration of $k_f$; requiring an exact model of the process is undesirable. Integral feedback uses an integrator to give zero steady-state error (p. 7-24).

**System augmentation (p. 7-25).** Add the state $z$ = integral of $y-r$:
$$\frac d{dt}\begin{pmatrix}x\\z\end{pmatrix}=\begin{pmatrix}Ax+Bu\\y-r\end{pmatrix}=\begin{pmatrix}Ax+Bu\\Cx-r\end{pmatrix}.\tag{7.26}$$
If a controller stabilises this system, then $\dot z=0$ in steady state, hence $y=r$. Use $u=-Kx-k_iz+k_fr$ (7.27). The equilibrium satisfies $x_e=-(A-BK)^{-1}B(k_fr-k_iz_e)$ and $Cx_e=r$. The value $z_e$ settles by itself to make $\dot z=y-r=0$. This holds independently of the specific $A,B,K$ as long as the system is stable. The controller $u=-Kx-k_iz+k_fr,\ \dot z=y-r$ is a **dynamic compensator**, because it has internal dynamics (p. 7-25).

**Example 7.8 (cruise control; pp. 7-25, 7-26).** Linearised: $\dot x=-ax-b_g\theta+bw$, $y=v=x+v_e$, with $x=v-v_e$, $w=u-u_e$, $\theta$ the road angle. Augmented ($\dot z=v_e+x-v_r$):
$$\frac d{dt}\begin{pmatrix}x\\z\end{pmatrix}=\begin{pmatrix}-a&0\\1&0\end{pmatrix}\begin{pmatrix}x\\z\end{pmatrix}+\begin{pmatrix}b\\0\end{pmatrix}w+\begin{pmatrix}-b_g\\0\end{pmatrix}\theta+\begin{pmatrix}0\\v_e-v_r\end{pmatrix}.$$
Controller $w=-k_px-k_iz+k_fv_r$. With $\theta=0$, $\det(sI-(A-BK))=s^2+(bk_p+a)s+bk_i$. To get $s^2+a_1s+a_2$:
$$k_p=\frac{a_1-a}b,\quad k_i=\frac{a_2}b,\quad k_f=-1/\big(C(A-BK)^{-1}B\big)=\frac{a_1}b.$$
Perfect tracking holds even with small parameter errors, as long as the closed loop stays stable. One can even take $k_f=0$, but $k_f$ shapes the transient response. Hill simulation (Figure 7.12): $\theta=4^\circ$ at $t=5$ s, $k_p=0.5$, $k_i=0.1$, $v_r=20$ m/s. With integral action the speed returns to $v_r$. With plain state feedback the throttle is nearly the same but the speed is quite different, because the zero-frequency gain from throttle to velocity is high (printed as $-b/a=130$). The stability of the system is unaffected by the disturbance. Rejecting constant disturbances is a general property of integral feedback (Exercise 7.15) (p. 7-26).

> **Intuition note.** The integrator keeps changing the input as long as any error remains. If the closed loop is stable, it can only settle when $y=r$. That is why no precise calibration is needed.

**Reachability of the augmented system (p. 7-27).** Eigenvalue assignment needs (7.26) to be reachable:
$$W_r=\begin{pmatrix}B&AB&\cdots&A^nB\\0&CB&\cdots&CA^{n-1}B\end{pmatrix}.$$
Let $\lambda_A(s)=s^n+a_1s^{n-1}+\cdots+a_n$. Multiply the first column by $a_n$, the second by $a_{n-1}$, and so on, and add these to the last column. By Cayley–Hamilton the matrix becomes
$$\begin{pmatrix}B&AB&\cdots&A^{n-1}B&0\\0&CB&\cdots&CA^{n-2}B&b_n\end{pmatrix},\quad b_n=C(A^{n-1}B+a_1A^{n-2}B+\cdots+a_{n-1}B).\tag{7.28}$$
If $A$ is invertible (no eigenvalue at the origin), $b_n=CA^{-1}(A^n+a_1A^{n-1}+\cdots+a_{n-1}A)B=-a_nCA^{-1}B$ (second use of Cayley–Hamilton). As long as $b_n\neq0$ the system is reachable and the augmented eigenvalues can be assigned arbitrarily. $b_n$ is a coefficient of $G(s)=\frac{b_1s^{n-1}+\cdots+b_n}{s^n+a_1s^{n-1}+\cdots+a_n}$ (Chapter 9). So the condition is that the original system has no pure derivative in its input/output response (p. 7-27).

### 7.5 Linear Quadratic Regulators

Instead of choosing eigenvalues, choose the gains by optimising a cost, which helps balance performance against input size (p. 7-28).

**Problem (p. 7-28).** For $\dot x=Ax+Bu$, $x\in\mathbb R^n$, $u\in\mathbb R^p$, $x(0)=x_0$, minimise
$$J(x_0)=\int_0^{t_f}\big(x^TQ_xx+u^TQ_uu\big)dt+x^T(t_f)Q_fx(t_f),\tag{7.29}$$
with symmetric $Q_x\succeq0$, $Q_u\succ0$, $Q_f\succeq0$. The cost trades deviation of the state from the origin against control cost.

**Solution (p. 7-28).**
$$u=-Kx,\quad K=Q_u^{-1}B^TS,\tag{7.30}$$
$$-\frac{dS}{dt}=A^TS+SA-SBQ_u^{-1}B^TS+Q_x,\quad S(t_f)=Q_f,\tag{7.31}$$
where $S\in\mathbb R^{n\times n}$ is positive definite and symmetric. (7.31) is the **Riccati differential equation**, integrated backwards from $S(t_f)=Q_f$. The optimal cost is
$$\min_u\int_0^{t_f}(\cdots)dt+x^T(t_f)Q_fx(t_f)=x^T(0)S(0)x(0).\tag{7.32}$$
The matrices may depend on time. A solution exists if the Riccati equation has a unique positive solution. LQR is well suited to linearisation around a trajectory (Section 8.5). Exercise 7.17 asks the reader to prove optimality using (7.31).

**Infinite horizon, constant matrices (pp. 7-28, 7-29).** $S$ is the steady-state solution of the **algebraic Riccati equation**
$$A^TS+SA-SBQ_u^{-1}B^TS+Q_x=0.\tag{7.33}$$
If the system is reachable, it can be shown there is a unique positive definite $S$ satisfying (7.33) that makes the closed loop stable. MATLAB `lqr` returns $K$, $S$ and $E=A-BK$.

**Choosing weights (p. 7-29).** A solution needs $Q_x\succeq0$ and $Q_u\succ0$. There are also "observability" conditions on $Q_x$. Here $Q_x\succ0$ is assumed to ensure the algebraic Riccati equation always has solutions. A simple choice is diagonal weights $Q_x=\operatorname{diag}(q_1,\dots,q_n)$, $Q_u=\operatorname{diag}(\rho_1,\dots,\rho_n)$; each entry says how much that squared state or input adds to the cost. Put high weights on states that must stay small.

> **Intuition note.** LQR does not assign eigenvalues directly. A higher input weight $\rho$ penalises the control input more; in Example 7.9 this gave a more sluggish response (Figure 7.13b). Higher weights on states that must stay small penalise deviations of those states more.

**Example 7.9 (vectored thrust aircraft; pp. 7-29, 7-30).** Parameters $m=4$ kg, $J=0.0475$ kg m², $r=0.25$ m, $g=9.8$, $c=0.05$. Equilibrium $F_e=(0,mg)$, $z_e=(x_e,y_e,0,0,0,0)$. Linearised:
$$A=\begin{pmatrix}0&0&0&1&0&0\\0&0&0&0&1&0\\0&0&0&0&0&1\\0&0&-g&-c/m&0&0\\0&0&0&0&-c/m&0\\0&0&0&0&0&0\end{pmatrix},\ B=\begin{pmatrix}0&0\\0&0\\0&0\\1/m&0\\0&1/m\\r/J&0\end{pmatrix},\ C=\begin{pmatrix}1&0&0&0&0&0\\0&1&0&0&0&0\end{pmatrix}.$$
Shapes: $A$ is $6\times6$, $B$ is $6\times2$, $C$ is $2\times6$, $D=0$. The text states the system is reachable. Cost $J=\int_0^\infty(\xi^TQ_\xi\xi+v^TQ_vv)dt$ with $Q_\xi=I_6$, $Q_v=\rho I_2$, and $F=-K(z-z_e)+F_e$. Figure 7.13: for $\rho=1,10^2,10^4$, a higher input weight gives a more sluggish response (p. 7-30).

**Example 7.10 (web server, discrete time; pp. 7-30 to 7-32).** Dynamics $x[k+1]=Ax[k]+Bu[k]$, $y_{cpu}[k]=x_{cpu}[k]+d_{cpu}[k]$, with $x=(x_{cpu},x_{mem})$, $u=(u_{ka},u_{mc})$ (KeepAlive and MaxClients), $A,B\in\mathbb R^{2\times2}$ from Section 4.4. The disturbance enters after the process (Figure 7.14), so the controller is
$$u=-K\begin{pmatrix}y_{cpu}\\x_{mem}\end{pmatrix}+k_fr_{cpu}.$$
It uses the measured $y_{cpu}$ rather than $x_{cpu}$. LQR weights: $Q_x=\operatorname{diag}(5,1)$ (more weight on processor load than memory), $Q_u=\operatorname{diag}(1/50^2,1/1000^2)$ (a KeepAlive of 50 s weighs the same as a MaxClients of 1000). With `dlqr`:
$$K=\begin{pmatrix}-22.3&10.1\\382.7&77.7\end{pmatrix}.$$
For $k_f$, set $x[k+1]=x[k]=x_e$: $x_e=(A-BK)x_e+Bk_fr$. Take $x_e=(r,0)$ (zero memory use). Then $\binom r0=(A-BK-I)^{-1}Bk_fr$, so
$$k_f=\Big(\big((A-BK-I)^{-1}B\big)\Big)^{-1}\binom10=\binom{49.3}{539.5}.$$
A load change $d_{cpu}=0.3$ is applied; the desired load is 0.57. Both parameters adjust. The load decreases but stays about 0.2 above the desired value. The Figure 7.15 caption says the effect of the disturbance is reduced by about 40% (p. 7-32).

### 7.6 Further Reading (p. 7-33)
Kalman's seminal paper discussed state models and state feedback, with the gain from minimising a quadratic loss. Reachability and observability (Chapter 8) are also due to Kalman. Kalman defines controllability and reachability as the ability to reach the origin and an arbitrary state, respectively. The authors prefer "reachability" as more descriptive. Reachability is also used in graph theory as the ability to get from one vertex to another. That arbitrary eigenvalue placement is possible for reachable linear systems was first realised by J. Bertram in 1959 (root-locus based). An analytical proof was given in 1960 (p. 7-33).

### Exercises (pp. 7-33 to 7-36)
Exercises 7.1–7.17 are listed (no solutions printed). See "Exercises worth doing" below.

## Toy example (ours, not from the text)
**Goal:** assign eigenvalues $-1$ and $-2$ to a reachable system, then show a non-reachable system where this fails.

*Reachable case.* $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $B=\begin{pmatrix}0\\1\end{pmatrix}$, $C=(1\ 0)$.
- $AB=\begin{pmatrix}1\\0\end{pmatrix}$, so $W_r=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\det W_r=-1\neq0$. The system is reachable (Theorem 7.1).
- With $K=(k_1\ k_2)$: $A-BK=\begin{pmatrix}0&1\\-k_1&-k_2\end{pmatrix}$ and $\det(sI-A+BK)=s(s+k_2)+k_1=s^2+k_2s+k_1$.
- Desired $p(s)=(s+1)(s+2)=s^2+3s+2$, so $k_2=3$, $k_1=2$, $K=(2\ \ 3)$. (Here $a_1=a_2=0$, so $k_i=p_i-a_i$ as in (7.18).)
- $A-BK=\begin{pmatrix}0&1\\-2&-3\end{pmatrix}$, $\det=2$, inverse $=\tfrac12\begin{pmatrix}-3&-1\\2&0\end{pmatrix}$. Times $B$: $\tfrac12\begin{pmatrix}-1\\0\end{pmatrix}=\begin{pmatrix}-0.5\\0\end{pmatrix}$. Then $C(\cdot)=-0.5$, so $k_f=-1/(-0.5)=2$ from (7.13).
- Check: $x_e=-(A-BK)^{-1}Bk_fr=-(-0.5,0)^T\cdot2r=(r,0)^T$, so $y_e=r$.
- Control law: $u=-2x_1-3x_2+2r$.

*Unreachable case.* $A=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}$, $B=\begin{pmatrix}1\\1\end{pmatrix}$ (two identical subsystems, one input, as in Figure 7.3).
- $AB=\begin{pmatrix}-1\\-1\end{pmatrix}$, so $W_r=\begin{pmatrix}1&-1\\1&-1\end{pmatrix}$, $\det=-1+1=0$. Not reachable.
- $A-BK=\begin{pmatrix}-1-k_1&-k_2\\-k_1&-1-k_2\end{pmatrix}$, trace $=-2-\sigma$ with $\sigma=k_1+k_2$, determinant $=(1+k_1)(1+k_2)-k_1k_2=1+\sigma$.
- So $\det(sI-A+BK)=s^2+(2+\sigma)s+(1+\sigma)=(s+1)(s+1+\sigma)$. One eigenvalue stays at $-1$ for every $K$.
- This is the shared-input mechanism (p. 7-6) in a slightly different form: with $H=(1\ \ -1)$, $\frac d{dt}Hx=-(x_1-x_2)$, so $H(x_1,x_2)$ is not constant, but $HB=0$ and $HA=-H$, so $H$ decays on its own whatever $u$ does, and $HW_r=0$ (this is not the exact constant-combination case, which needs $HA=0$).

## Concepts
- [[state-feedback-pole-placement]] — law $u=-Kx+k_fr$ chosen to give the closed loop a desired characteristic polynomial (pp. 7-10, 7-11, 7-15)
- [[controllability-reachability]] — any state reachable from any state in finite time; tested by rank of $W_r$ (Def. 7.1, Thm 7.1; pp. 7-2, 7-4). Author prefers "reachability" to "controllability" (p. 7-33)
- [[reachability-matrix]] (new) — $W_r=(B\ AB\ \cdots\ A^{n-1}B)$ (p. 7-4)
- [[reachable-canonical-form]] (new) — coordinates in which the polynomial coefficients sit in the first row of $\tilde A$ (7.6) (p. 7-7)
- [[eigenvalues-and-modes]] — closed-loop eigenvalue locations determine the closed-loop behavior; the dominant pair often determines the step response (pp. 7-17, 7-22)
- [[state]] — variables that permit prediction of future evolution given future inputs (p. 7-9)
- [[feedforward]] — the term $k_fr$ from reference to input; fixes steady state but needs exact calibration (pp. 7-10, 7-14)
- [[reference-set-point]] — constant target value $r$ for $y$ (p. 7-10)
- [[integral-action]] — augment state with $\int(y-r)dt$; forces $y=r$ in steady state if the closed loop is stable (p. 7-25)
- [[dynamic-compensator]] (new) — controller with its own internal state, e.g. an integrator (p. 7-25)
- [[damping-ratio-natural-frequency]] (new) — $\zeta,\omega_0$ of the second-order system; $\zeta=-\operatorname{Re}\lambda/|\lambda|$ for a complex eigenvalue (pp. 7-18, 7-21)
- [[dominant-eigenvalues]] (new) — complex pair nearest the imaginary axis (ties: lowest damping ratio) (p. 7-21)
- [[lqr]] — optimal linear state feedback for a quadratic cost (7.29)–(7.33) (p. 7-28)
- [[riccati-equation]] (new) — differential (7.31) and algebraic (7.33) equations that give $S$ and $K=Q_u^{-1}B^TS$ (p. 7-28)
- [[ackermann-formula]] (new) — (7.21), the numeric formula for $K$ (p. 7-15)
- [[disturbance-and-noise]] — constant disturbances are rejected by integral action (p. 7-26)
- [[robustness]] — only touched on: Theorem 7.3 assumes precise knowledge of the process; robustness is deferred to Chapter 13 (p. 7-17)

## Canonical instances
- [[double-integrator]] — phase-portrait example of steering to the origin; equilibria on the $x_1$ axis (pp. 7-2, 7-3)
- [[balance-system-cart-pendulum]] — reachable (7.5); eigenvalue placement trades speed against input size (pp. 7-4, 7-23)
- [[vehicle-steering]] — $k_1=\omega_c^2$, $k_2=2\zeta_c\omega_c-\gamma\omega_c^2$ (p. 7-11)
- [[predator-prey]] — linearised state feedback regulates lynx population (p. 7-15)
- [[drug-administration-two-compartment]] — state-feedback dosing vs pulsed doses (p. 7-20)
- [[cruise-control]] — integral action rejects hill disturbance (p. 7-25)
- [[vectored-thrust-aircraft]] — LQR with weight $\rho$ on inputs (p. 7-29)
- [[web-server-control]] — discrete-time LQR for load control (p. 7-30)
- [[two-identical-pendula-one-input]] — standard unreachable system (p. 7-6)

## Bridges (candidates)
- [structural-analogy] Reachable canonical form (polynomial coefficients as feedback paths) ↔ signal processing / transfer functions: direct-form realisation of a denominator polynomial — coefficients appear one-to-one in a chain of integrators.
- [same-math] Cayley–Hamilton rewriting of $e^{A\tau}$ in powers $I,\dots,A^{n-1}$ ↔ linear algebra: any matrix polynomial reduces to degree $\le n-1$ — same theorem used here.
- [structural-analogy] Integral action ($\dot z=y-r$ forces $y=r$) ↔ perceptual control: behavior keeps a perceived variable at a reference by acting on the error.
- [structural-analogy] LQR cost weights $Q_x,Q_u$ ↔ economics/decision theory: a loss that trades off outcome error against effort or cost of action.
- [metaphor] Dominant eigenvalue pair ↔ dynamical systems generally: the slowest mode dominates long-run behavior.

## Questions this raises
- How can we get $x$ when only $y$ is measured? (The text points to output feedback and state estimation in the next chapter, p. 7-17.)
- How do model errors affect Theorem 7.3 and the exact calibration of $k_f$ (robustness, Chapter 13)?
- Is there a principled way to choose eigenvalues or LQR weights, beyond trial and error and Bryson's rule (Exercise 7.16)?
- How do actuator limits constrain how fast the closed-loop eigenvalues can be placed (Chapters 12–14)?

## Exercises worth doing
- Ex. 7.4 (p. 7-33) — show unreachability of two identical systems with one input, and that $W_r$ is not full rank — difficulty: easy
- Ex. 7.10 (p. 7-34) — rank of $W_r$ for a system where eigenvalues cannot be assigned arbitrarily — difficulty: easy
- Ex. 7.9 (p. 7-34) — design $K$ for a specified $\zeta_c,\omega_c$ in a 2-state system — difficulty: medium
- Ex. 7.13 (p. 7-35) — two systems with the same eigenvalues but different dominant eigenvalues in the step response — difficulty: medium
- Ex. 7.15 (p. 7-35) — integral feedback rejects constant disturbances — difficulty: medium
- Ex. 7.17 (p. 7-36) — prove LQR optimality via the Riccati equation, and ask whether it holds for time-varying matrices — difficulty: hard

## Reading notes
- **Page numbers.** Text-layer labels show no printed number, but the page images show "7-1 … 7-36" in headers/footers. I cite these as (p. 7-N). Offset: pdf = (7-N) + 228 (pdf 229 = p. 7-1).
- **Example 7.6:** with printed $\zeta=1/\sqrt2$ and $\omega_0=0.22$, $-\zeta\omega_0\pm i\omega_0\sqrt{1-\zeta^2}\approx-0.156\pm0.156i$, but the text prints $-0.2\pm0.096i$. The values $\tilde k_1=-0.2$, $\tilde k_2=0.2$ and $k_f=0.065$ are as printed and I did not check them. It also says $\zeta=1/\sqrt2$ is chosen "to minimize the overshoot", although Table 7.1 gives 0% overshoot for $\zeta=1$.
- **Example 7.7:** the slow pair is first set with natural frequency 0.5 (giving $-0.35\pm0.35i$); the redesign says "changing the frequency to 1" but the printed eigenvalues $-0.18\pm0.18i$ have modulus $\approx0.25$. Treat the stated frequency with caution.
- **Example 7.8:** the zero-frequency gain from throttle to velocity is printed as "$-b/a=130$". The model $\dot x=-ax+bw$ gives $b/a$ for the throttle gain; the sign is as printed.
- **Example 7.10:** the caption says the load change is applied at "k = 10 ms", the text says "t = 10 s". The caption says disturbance reduced by about 40%. The text says the load stays about 0.2 above desired for a 0.3 change.
- **Example 7.5:** text gives $L_d=30$ and $L_e=29.5$/ $y_e=29.5$ in the formula, while the Figure 7.7 caption says $L_e=30$.
- **Section 7.4, augmented reachability:** the argument gives the block form with $b_n$ in the corner; it does not say explicitly that the original system must also be reachable for the upper-left block to be full rank. This reading is mine, not stated in the text. The column-operation description says "(n−1)th column by $a_1$"; the page prints it so.
- **Exercise 7.15** defines the disturbance as $Fd$ but the text says "$v$ is a disturbance" (printed inconsistency). **Exercise 7.9** says $\det(sI-BK)$, probably meant $\det(sI-A+BK)$ (my reading).
- The Theorem 7.3 statement is for single-input single-output systems. Within the pole-placement discussion, the multi-input case is mentioned only for the reachability test (p. 7-4); the LQR problem is stated for multi-input systems (p. 7-28).
- The section 7.5 title has a marker icon in the image (meaning not stated on the page).
