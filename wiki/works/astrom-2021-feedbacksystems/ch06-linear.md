---
id: astrom-2021-feedbacksystems/ch06-linear
work: astrom-2021-feedbacksystems
unit: "6 Linear Systems"
pages: 6-1 to 6-38 (printed as chapter-page; pdf 191–228)
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Linear Systems (Åström & Murray, ch. 6)

## L0 — One line
A linear time-invariant system is completely described by the matrix exponential $e^{At}$ and the convolution equation, and a nonlinear system near an equilibrium can be approximated by a linear one (Jacobian linearization).

## L1 — The gist (≤ 120 words)
The chapter asks how to compute and describe the behavior of linear systems $\dot x = Ax+Bu$, $y=Cx+Du$, and when a linear model can stand in for a nonlinear one. The answer is the matrix exponential for the initial-condition response and the convolution equation for the response to inputs. This gives step response, frequency response, modes, Jordan form (the stability proof) and sampling that is exact at the sampling instants. Near an equilibrium, the Jacobian matrices of a nonlinear model give a linear approximation. Feedback can also cancel nonlinearities. This matters because designing controllers on an approximate linear model and checking them on the nonlinear one is common practice.

**Prerequisites:** matrices and eigenvalues; Taylor series; ODE $\dot x=ax$; complex exponentials $e^{i\omega t}$; partial derivatives and the Jacobian; basic integrals.

## L2 — Key ideas (5–10 bullets)
- A system is linear if its output is jointly linear in initial state and input. Superposition then lets us add the initial-condition response and the forced response. (p. 6-3)
- $x(t)=e^{At}x(0)$ solves $\dot x=Ax$, where $e^{At}$ is the matrix version of the Taylor series for $e^{at}$. Diagonal form, or Jordan form (a block form with the eigenvalues on the diagonal), makes it computable and is used to prove the eigenvalue stability test. (pp. 6-6 to 6-11)
- Each (real) eigenvalue/eigenvector pair gives a "mode" with a fixed mode shape. For distinct eigenvalues the free response is a combination of modes. (pp. 6-13, 6-14)
- The convolution equation $y=Ce^{At}x(0)+\int_0^t h(t-\tau)u(\tau)d\tau$ gives the full response. The impulse response is $h(t)=Ce^{At}B+D\delta(t)$. (pp. 6-15, 6-17)
- The input response splits into a transient part (short-term, reflecting the initial mismatch) and a steady-state part (long-term behavior). The step response gives rise time, overshoot, settling time. The frequency response $G(i\omega)=C(i\omega I-A)^{-1}B+D$ gives gain and phase. (pp. 6-19 to 6-25)
- Sampling a linear system whose input is held constant over each sampling interval gives a discrete model that is exact at the sampling instants: $\Phi=e^{Ah}$, $\Gamma=(\int_0^h e^{As}ds)B$. (pp. 6-27, 6-28)
- Jacobian linearization (replacing $f,h$ by their matrices of partial derivatives) approximates a nonlinear system near an equilibrium or solution. If the linearization is asymptotically stable, the equilibrium is locally asymptotically stable. (p. 6-30)
- Feedback linearization uses a nonlinear feedback law to make the input–output map linear. It requires an accurate model and can cancel useful dynamics. (pp. 6-33, 6-34)

## L3 — Walkthrough

### Chapter introduction (p. 6-1)
The chapter specializes Chapters 3–5 to linear, time-invariant input/output systems. Two central tools are the matrix exponential and the convolution equation. It also shows how to approximate a nonlinear system by a linear one (p. 6-1).

### 6.1 Basic definitions

**Why linear models (pp. 6-1, 6-2).** Linear models fit electrical circuits, small deviations in solid and fluid mechanics, and signal processing (p. 6-1). We often *create* linear input/output behavior by feedback: Black's negative feedback amplifier was motivated by the wish for linear behavior (p. 6-2). For some systems nonlinearities cannot be ignored, especially for global behavior (to capture the predator–prey oscillations the nonlinear coupling terms must be included). Near an equilibrium, local linearization often suffices (p. 6-2).

**Setup (p. 6-2).** Consider
$$\frac{dx}{dt}=f(x,u),\qquad y=h(x,u),\tag{6.1}$$
with $x\in\mathbb R^n,u\in\mathbb R^p,y\in\mathbb R^q$. Usually $p=q=1$. Smoothness is assumed, and for a reasonable class of inputs (e.g. piecewise continuous) solutions are assumed to exist for all time (p. 6-2).

*Shift to the origin, without loss of generality (p. 6-2).* If $(x_e,u_e)\ne(0,0)$ is an equilibrium with $y_e=h(x_e,u_e)$, define $\tilde x=x-x_e,\ \tilde u=u-u_e,\ \tilde y=y-y_e$. Then
$$\tfrac{d}{dt}\tilde x=f(\tilde x+x_e,\tilde u+u_e)=:\tilde f(\tilde x,\tilde u),\qquad \tilde y=h(\tilde x+x_e,\tilde u+u_e)-y_e=:\tilde h(\tilde x,\tilde u).$$
The origin is now an equilibrium with output 0. Answers are translated back by $x=\tilde x+x_e$ and so on (p. 6-2).

**Linearity (p. 6-3).** Write $y(t;x_0,u)$ for the output from $x(0)=x_0$ with input $u$. The system is *linear input/output* if
$$\begin{aligned}&\text{(i) } y(t;\alpha x_1+\beta x_2,0)=\alpha y(t;x_1,0)+\beta y(t;x_2,0),\\&\text{(ii) } y(t;\alpha x_0,\delta u)=\alpha y(t;x_0,0)+\delta y(t;0,u),\\&\text{(iii) } y(t;0,\delta u_1+\gamma u_2)=\delta y(t;0,u_1)+\gamma y(t;0,u_2).\end{aligned}\tag{6.2}$$
So outputs are jointly linear in the initial-condition response ($u=0$) and the forced response ($x(0)=0$). Property (iii) is the *principle of superposition* (p. 6-3).

The general linear state space system is
$$\frac{dx}{dt}=Ax+Bu,\qquad y=Cx+Du,\tag{6.3}$$
with $A\in\mathbb R^{n\times n}$, $B\in\mathbb R^{n\times p}$, $C\in\mathbb R^{q\times n}$, $D\in\mathbb R^{q\times p}$. For single-input single-output: $B$ is a column, $C$ a row, $D$ a scalar (p. 6-3). Solutions of (6.3) satisfy (6.2). Conversely, a finite-state system that is input/output linear can always be written as (6.3) for a suitable choice of states (p. 6-3).

The *homogeneous solution* $x_h$ solves $\dot x_h=Ax_h,\ x_h(0)=x_0$. The *particular (forced) solution* $x_p$ solves $\dot x_p=Ax_p+Bu,\ x_p(0)=0$. Fig. 6.1 shows them adding to the complete solution (p. 6-3, 6-4).

**Example 6.1 (scalar system, p. 6-3, 6-4).** $\dot x=ax+u,\ y=x$, $x(0)=x_0$, $u_1=A\sin\omega_1t$, $u_2=B\cos\omega_2t$. Then $x_h=e^{at}x_0$ and the particular solutions are
$$x_{p1}(t)=-A\,\frac{-\omega_1e^{at}+\omega_1\cos\omega_1t+a\sin\omega_1t}{a^2+\omega_1^2},\qquad x_{p2}(t)=B\,\frac{ae^{at}-a\cos\omega_2t+\omega_2\sin\omega_2t}{a^2+\omega_2^2}.$$
With $x(0)=\alpha x_0$ and $u=u_1+u_2$ the solution is the weighted sum
$$x(t)=e^{at}\Big(\alpha x_0+\frac{A\omega_1}{a^2+\omega_1^2}+\frac{Ba}{a^2+\omega_2^2}\Big)-A\frac{\omega_1\cos\omega_1t+a\sin\omega_1t}{a^2+\omega_1^2}+B\frac{-a\cos\omega_2t+\omega_2\sin\omega_2t}{a^2+\omega_2^2}\tag{6.4}$$
The author says to check this by substituting into the ODE (p. 6-4).

**Time invariance (p. 6-4).** For a time-invariant system, if input $u(t)$ gives output $y(t)$, shifting the input by a constant $a$ ($u(t+a)$) gives $y(t+a)$. Linear time-invariant (LTI) systems have responses to any input that are completely characterized by the step response or the impulse response (p. 6-4).

**Response to piecewise constant inputs (p. 6-5).** Take zero initial condition. A piecewise constant input with jumps at $t_k$ is a sum of steps: amplitude $u(t_0)$ at $t_0$, then $u(t_1)-u(t_0)$ at $t_1$, etc. (Fig. 6.2). Let $H(t)$ be the unit step response with $H(0)=0$. By superposition and time invariance,
$$\begin{aligned}y(t)&=H(t-t_0)u(t_0)+H(t-t_1)\big(u(t_1)-u(t_0)\big)+\cdots\\&=\big(H(t-t_0)-H(t-t_1)\big)u(t_0)+\big(H(t-t_1)-H(t-t_2)\big)u(t_1)+\cdots\\&=\sum_{k=1}^n\big(H(t-t_{k-1})-H(t-t_k)\big)u(t_{k-1})+H(t-t_n)u(t_n)\\&=\sum_{k=1}^n\frac{H(t-t_{k-1})-H(t-t_k)}{t_k-t_{k-1}}\,u(t_{k-1})\,(t_k-t_{k-1})+H(t-t_n)u(t_n),\end{aligned}$$
where $t_n\le t$. Letting $n\to\infty$ with $t_k-t_{k-1}\to0$ and $t_n\to t$ gives
$$y(t)=\int_0^tH'(t-\tau)u(\tau)\,d\tau,\tag{6.5}$$
where $H'$, the derivative of the step response, is the *impulse response* (p. 6-5). The response of an LTI system to any input can thus be computed from its step response. With zero initial state, the output depends only on the input (p. 6-6).

*Intuition note.* Any input is a pile of small steps. Each step produces a delayed copy of the step response, and linearity lets us add them. Letting the steps shrink gives an integral.

### 6.2 The matrix exponential

**Initial condition response (p. 6-6).** For $\dot x=Ax$ (6.6) the scalar case $\dot x=ax$ has solution $e^{at}x(0)$. The *matrix exponential* is defined by the series
$$e^X=I+X+\tfrac12X^2+\tfrac1{3!}X^3+\cdots=\sum_{k=0}^\infty\frac1{k!}X^k,\tag{6.7}$$
with $X^0=I$, $X^2=XX$, $X^n=X^{n-1}X$. It is the Taylor series of the scalar exponential. The author states it converges for any $X\in\mathbb R^{n\times n}$ (p. 6-6). Replacing $X$ by $At$:
$$e^{At}=I+At+\tfrac12A^2t^2+\cdots=\sum_k\frac1{k!}A^kt^k,\qquad \frac{d}{dt}e^{At}=A+A^2t+\tfrac12A^3t^2+\cdots=Ae^{At}.\tag{6.8}$$
Hence (p. 6-7):

**Proposition 6.1.** The solution of (6.6) is $x(t)=e^{At}x(0)$. The vector $x(0)$ must stand on the right of $e^{At}$ (p. 6-7).

The solution is linear in the initial condition: $e^{At}(\alpha x_{01}+\beta x_{02})=\alpha x_{h1}(t)+\beta x_{h2}(t)$, and the output $y=Cx$ is linear likewise (p. 6-7).

*Intuition note.* The matrix exponential does for a vector system what $e^{at}$ does for a scalar one. Multiplying by $e^{At}$ moves the state forward by time $t$.

**Example 6.2 (double integrator, pp. 6-7, 6-8).** $\ddot q=u,\ y=q$; state $x=(q,\dot q)$; $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $B=\begin{pmatrix}0\\1\end{pmatrix}$. Direct calculation gives $A^2=0$, so $e^{At}=I+At=\begin{pmatrix}1&t\\0&1\end{pmatrix}$. With $u=0$: $x(t)=\begin{pmatrix}x_1(0)+tx_2(0)\\x_2(0)\end{pmatrix}$, $y(t)=x_1(0)+tx_2(0)$ (p. 6-8).

**Example 6.3 (undamped oscillator, p. 6-8).** $\ddot q+\omega_0^2q=u$, with $x_1=q$, $x_2=\dot q/\omega_0$:
$$A=\begin{pmatrix}0&\omega_0\\-\omega_0&0\end{pmatrix},\qquad e^{At}=\begin{pmatrix}\cos\omega_0t&\sin\omega_0t\\-\sin\omega_0t&\cos\omega_0t\end{pmatrix}.$$
This is verified by differentiation: $\frac{d}{dt}e^{At}=Ae^{At}$ (p. 6-8). With damping, $\ddot q+2\zeta\omega_0\dot q+\omega_0^2q=u$ and $\zeta<1$,
$$\exp\Big(\begin{pmatrix}-\zeta\omega_0&\omega_d\\-\omega_d&-\zeta\omega_0\end{pmatrix}t\Big)=e^{-\zeta\omega_0t}\begin{pmatrix}\cos\omega_dt&\sin\omega_dt\\-\sin\omega_dt&\cos\omega_dt\end{pmatrix},\quad\omega_d=\omega_0\sqrt{1-\zeta^2}.$$
The case $\zeta\ge1$ is in Exercise 6.4 (p. 6-8).

**Diagonalization (pp. 6-8, 6-9).** If all eigenvalues of $A$ are distinct, an invertible $T$ exists (Exercise 5.14) with $TAT^{-1}$ diagonal. With $z=Tx$: $\dot z=T\dot x=TAx=TAT^{-1}z$. For diagonal $A=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$, $(At)^k=\mathrm{diag}(\lambda_i^kt^k)$, so from the series
$$e^{At}=\mathrm{diag}(e^{\lambda_1t},\dots,e^{\lambda_nt}).$$
Complex eigenvalues are handled by block-diagonal matrices. The original solution is $x=T^{-1}z$ (p. 6-9).

**Jordan form (p. 6-9).** Some matrices with repeated eigenvalues cannot be diagonalized. They can be put in *Jordan form*: block diagonal $J=\mathrm{diag}(J_1,\dots,J_k)$, where each *Jordan block* $J_i$ has $\lambda_i$ on the diagonal and 1's on the superdiagonal:
$$J_i=\begin{pmatrix}\lambda_i&1&&0\\&\ddots&\ddots&\\&&\ddots&1\\0&&&\lambda_i\end{pmatrix}.\tag{6.9}$$
A $1\times1$ block is an integrator with feedback $\lambda$. Larger blocks are cascades of such systems (Fig. 6.3, p. 6-9, 6-10).

**Theorem 6.2 (Jordan decomposition).** Any $A\in\mathbb R^{n\times n}$ can be transformed into Jordan form, with the eigenvalues of $A$ giving the $\lambda_i$. The proof is referred to linear-algebra texts (p. 6-9).

Eigenvalues need not be distinct, so one eigenvalue can have several blocks of different sizes (p. 6-10). Then
$$e^{Jt}=\mathrm{diag}\big(e^{J_1t},\dots,e^{J_kt}\big),\tag{6.10}$$
$$e^{J_it}=\begin{pmatrix}1&t&\frac{t^2}{2!}&\cdots&\frac{t^{n-1}}{(n-1)!}\\&1&t&\cdots&\frac{t^{n-2}}{(n-2)!}\\&&\ddots&\ddots&\vdots\\&&&\ddots&t\\0&&&&1\end{pmatrix}e^{\lambda_it}\tag{6.11}$$
(block of size $n$; p. 6-10). If $\lambda=\sigma+i\omega$ the solutions oscillate, since $e^{(\sigma+i\omega)t}=e^{\sigma t}(\cos\omega t+i\sin\omega t)$ (p. 6-10).

**Proof of Theorem 5.1 (p. 6-11).** Theorem 5.1: $x_e=0$ of a linear system is asymptotically stable iff $\mathrm{Re}\,\lambda_i<0$ for all $i$. Let $T$ give $J=TAT^{-1}$ and $z=Tx$. Then $z(t)=e^{Jt}z(0)$ and $x(t)=T^{-1}e^{Jt}z(0)$. By (6.11) all elements of $e^{Jt}$ decay to zero for arbitrary $z(0)$ iff $\mathrm{Re}\,\lambda_i<0$ for all $i$. If some $\lambda_i$ has positive real part, some initial condition gives unbounded growth. That initial condition can be scaled arbitrarily small, so the equilibrium is unstable (p. 6-11).

**Proposition 6.3 (p. 6-11).** Suppose $\dot x=Ax$ has no eigenvalue with strictly positive real part and one or more with zero real part. Then the system is stable (in the sense of Lyapunov) iff the Jordan blocks of each eigenvalue with zero real part are scalar ($1\times1$). Proof: Exercise 6.6b.

**Example 6.4 (vectored thrust aircraft, pp. 6-11, 6-12).** With $u_1=u_2=0$ and $z=(x,y,\theta,\dot x,\dot y,\dot\theta)$:
$$\dot z=\big(z_4,\ z_5,\ z_6,\ -g\sin z_3-\tfrac cmz_4,\ g(\cos z_3-1)-\tfrac cmz_5,\ 0\big)^T.\tag{6.12}$$
Equilibria need zero velocities and $-g\sin z_{3,e}=0$, $g(\cos z_{3,e}-1)=0$, so $\theta_e=0$ (upright). $x_e,y_e$ are free because the system can be translated (p. 6-11). The linearization (eq. 5.13) is
$$A=\begin{pmatrix}0&0&0&1&0&0\\0&0&0&0&1&0\\0&0&0&0&0&1\\0&0&-g&-c/m&0&0\\0&0&0&0&-c/m&0\\0&0&0&0&0&0\end{pmatrix},\qquad\lambda(A)=\{0,0,0,0,-c/m,-c/m\}.$$
So it is not asymptotically stable. The Jordan form has a $1\times1$ block (eigenvalue 0), a $3\times3$ block (eigenvalue 0) and two $1\times1$ blocks ($-c/m$). Because the eigenvalue 0 has a non-scalar block, the linearization is unstable (Exercise 6.6) (p. 6-12).

**Eigenvalues and modes (pp. 6-12 to 6-14).** For oscillatory systems a *mode* is a vibration pattern (Fig. 6.4: both masses move together, or toward/away from each other) (p. 6-12). For a real eigenpair $Av=\lambda v$ and $x(0)=v$:
$$e^{At}v=\big(I+At+\tfrac12A^2t^2+\cdots\big)v=v+\lambda tv+\tfrac{\lambda^2t^2}2v+\cdots=e^{\lambda t}v.$$
The solution stays in the span of $v$. This solution is called a mode ("mode" is also often used for the eigenvalue itself). Component ratios $x_i/x_j=v_i/v_j$ are constant, so $v$ is the *mode shape*. Fig. 6.5 shows a fast and a slow mode: the states have the same sign for the slow mode and different signs for the fast mode (p. 6-13).

For complex pairs $\lambda=\sigma\pm i\omega$, $v=u\pm iw$ (with $u=\frac{v+v^*}2$, $w=\frac{v-v^*}{2i}$):
$$e^{At}u=ue^{\sigma t}\cos\omega t-we^{\sigma t}\sin\omega t,\qquad e^{At}w=ue^{\sigma t}\sin\omega t+we^{\sigma t}\cos\omega t.$$
A solution starting in span$\{u,w\}$ stays there, as a logarithmic spiral set by $\sigma,\omega$ (pp. 6-13, 6-14).

If $A$ has $n$ distinct eigenvalues, write $x(0)=\alpha_1v_1+\cdots+\alpha_nv_n$ (shown for real eigenvalues with unit eigenvectors). Then
$$x(t)=\alpha_1e^{\lambda_1t}v_1+\cdots+\alpha_ne^{\lambda_nt}v_n.$$
Complex distinct eigenvalues are similar. Non-distinct ones are subtler and need Jordan form (p. 6-14).

*Intuition note.* For a real eigenvalue, the eigenvector is a direction in state space along which the dynamics is just scalar exponential growth or decay. If the $n$ eigenvalues are distinct, the eigenvectors are linearly independent, so any start is a mix of them.

**Example 6.5 (coupled spring–mass with dampers, pp. 6-14, 6-15).** $m\ddot q_1=-2kq_1-c\dot q_1+kq_2$, $m\ddot q_2=kq_1-2kq_2-c\dot q_2$; $x=(q_1,q_2,\dot q_1,\dot q_2)$,
$$A=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-2k/m&k/m&-c/m&0\\k/m&-2k/m&0&-c/m\end{pmatrix}.$$
Define $z_1=\tfrac12(q_1+q_2)$, $z_2=\dot z_1$, $z_3=\tfrac12(q_1-q_2)$, $z_4=\dot z_3$, i.e. $z=Tx$ with $T=\tfrac12\begin{pmatrix}1&1&0&0\\0&0&1&1\\1&-1&0&0\\0&0&1&-1\end{pmatrix}$. Then
$$\dot z=\begin{pmatrix}0&1&0&0\\-k/m&-c/m&0&0\\0&0&0&1\\0&0&-3k/m&-c/m\end{pmatrix}z,$$
block diagonal. The $(z_1,z_2)$ mode has $\lambda\approx-c/(2m)\pm i\sqrt{k/m}$, and the $(z_3,z_4)$ mode has $\lambda\approx-c/(2m)\pm i\sqrt{3k/m}$. These match the two modes of Fig. 6.4. Real and imaginary parts give decay rate $\sigma$ and frequency $\omega$ (p. 6-15).

### 6.3 Input/output response

**Convolution equation (pp. 6-15, 6-16).** For $\dot x=Ax+Bu,\ y=Cx+Du$ (6.13):

**Theorem 6.4.**
$$x(t)=e^{At}x(0)+\int_0^te^{A(t-\tau)}Bu(\tau)\,d\tau.\tag{6.14}$$
*Proof.* Differentiate and use (6.8): $\dot x=Ae^{At}x(0)+\int_0^tAe^{A(t-\tau)}Bu(\tau)d\tau+Bu(t)=Ax+Bu$. The initial condition also holds (p. 6-15, 6-16).

Hence
$$y(t)=Ce^{At}x(0)+\int_0^tCe^{A(t-\tau)}Bu(\tau)\,d\tau+Du(t).\tag{6.15}$$
This is the *convolution equation*. The output is jointly linear in initial condition and input. $A$ governs both stability and performance, and $e^{At}$ describes both the response to perturbed initial conditions and the response to inputs (p. 6-16).

**Impulse response (pp. 6-16, 6-17).** Define the pulse
$$p_\epsilon(t)=\begin{cases}0&t<0\\1/\epsilon&0\le t<\epsilon\\0&t\ge\epsilon\end{cases}\tag{6.16}$$
and the *impulse* $\delta(t)=\lim_{\epsilon\to0}p_\epsilon(t)$ (6.17). It is not physically achievable but is a convenient abstraction. Its integral is 1: $\int_0^t\delta(\tau)d\tau=\lim_{\epsilon\to0}\int_0^\epsilon\frac1\epsilon d\tau=1$ for $t>0$ (p. 6-17). The impulse response $h(t)$ is the output with zero initial condition and an impulse input:
$$h(t)=\int_0^tCe^{A(t-\tau)}B\delta(\tau)d\tau+D\delta(t)=Ce^{At}B+D\delta(t).\tag{6.18}$$
The second equality holds because $\delta$ is zero except at the origin and has integral 1. Then
$$y(t)=Ce^{At}x(0)+\int_0^th(t-\tau)u(\tau)\,d\tau.\tag{6.19}$$
The second term equals (6.5). The author notes the impulse response is the derivative of the step response (p. 6-17). The response is a superposition of responses to shifted impulses weighted by $u$ (Exercise 6.2) (p. 6-17).

Pulses approximate impulses in experiments (Fig. 6.6). As a rule, if the fastest eigenvalue of a stable system has real part $-\sigma_{\max}$, a pulse of length $\epsilon$ estimates the impulse response well if $\epsilon\sigma_{\max}\ll1$. For Fig. 6.6, $\epsilon=1$ s gives $\epsilon\sigma_{\max}=0.62$ and the pulse response is already close (p. 6-17).

*Intuition note.* The impulse response $h$ is the system's "fingerprint". Once you know it, the part of the output caused by the input (with zero initial state) is the input blended with $h$.

**Coordinate invariance (p. 6-18).** Input and output components are fixed by the model, but state coordinates are a choice. With $z=Tx$:
$$\tilde A=TAT^{-1},\quad\tilde B=TB,\quad\tilde C=CT^{-1},\quad D\text{ unchanged}.\tag{6.20}$$
The eigenvalues of $\tilde A$ equal those of $A$, so stability is unaffected. Using $e^{TST^{-1}}=Te^ST^{-1}$ (checked by substitution in the series),
$$x(t)=T^{-1}z(t)=T^{-1}e^{\tilde At}Tx(0)+T^{-1}\int_0^te^{\tilde A(t-\tau)}\tilde Bu(\tau)d\tau.$$
So if $\tilde A$ has an easy exponential, the solution for $x$ follows by matrix multiplication (p. 6-18).

**Example 6.6 (coupled spring–mass, driven, pp. 6-18, 6-19).** Same masses as Example 6.5, but the right spring is driven: $m\ddot q_2=kq_1-2kq_2-c\dot q_2+ku$. Then $B=(0,0,0,k/m)^T$ in $x$ coordinates, and with the $T$ of Example 6.5
$$\dot z=\begin{pmatrix}0&1&0&0\\-k/m&-c/m&0&0\\0&0&0&1\\0&0&-3k/m&-c/m\end{pmatrix}z+\begin{pmatrix}0\\k/2m\\0\\-k/2m\end{pmatrix}u.$$
The system decouples into two second-order systems. Solve each, then $x=T^{-1}z$. Stability is judged from the two second-order systems. The explicit solution is in Section 7.3 (p. 6-19).

**Steady-state response (pp. 6-19, 6-20).** The solution of (6.21) has an initial-condition response and an input response. The input response (last two terms of (6.15)) splits into a *transient response*, which reflects the mismatch between initial condition and steady-state solution, and a *steady-state response* (long-term behavior). For periodic inputs the steady state is often periodic, and for constant inputs often constant (Fig. 6.8) (pp. 6-19, 6-20).

*Step response.* Unit step: $S(t)=0$ at $t=0$, $=1$ for $t>0$ (Heaviside). The step response is the output from zero initial condition with a step input. It is not practically implementable but widely used (p. 6-20). With $x(0)=0$:
$$\begin{aligned}y(t)&=C\int_0^te^{A(t-\tau)}B\,d\tau+D=C\int_0^te^{A\sigma}B\,d\sigma+D=C\big(A^{-1}e^{A\sigma}B\big)\Big|_{\sigma=0}^{\sigma=t}+D\\&=CA^{-1}e^{At}B-CA^{-1}B+D.\end{aligned}$$
$$y(t)=\underbrace{CA^{-1}e^{At}B}_{\text{transient}}+\underbrace{D-CA^{-1}B}_{\text{steady-state}},\quad t>0.\tag{6.22}$$
The transient decays to zero if all eigenvalues of $A$ have negative real part. The steady-state term assumes $A$ is invertible (pp. 6-20, 6-21).

*Step response measures (Fig. 6.9, p. 6-21).*
- Steady-state value $y_{ss}$: final level, if the output converges.
- Rise time $T_r$: time to first go from 10% to 90% of the final value (the book's convention).
- Overshoot $M_p$: percentage by which the signal initially rises above the final value. This assumes later overshoots are not larger, otherwise the term is ambiguous.
- Settling time $T_s$: time after which the signal stays within 2% of the final value. 1% or 5% are sometimes used (Exercise 6.7).

For linear systems $T_r$, $M_p$, $T_s$ are independent of the step size (p. 6-21).

**Example 6.7 (compartment model, p. 6-21).** A drug is infused at constant rate into $V_1$, and the effect is in $V_2$. The step response (Fig. 6.10b) is slow, with settling time 39 min. A larger initial injection rate reaches steady state faster (Fig. 6.10c). That response combines two step responses (Exercise 6.3).

**Frequency response (pp. 6-21 to 6-25).** The response of a linear system to a sinusoid is a sinusoid at the same frequency; compare magnitude and phase (p. 6-22). By Euler, $\cos\omega t=\tfrac12(e^{i\omega t}+e^{-i\omega t})$. By linearity it suffices to find the response to $u=e^{st}$ and average over $s=\pm i\omega$ (p. 6-22). From (6.15):
$$y(t)=Ce^{At}x(0)+Ce^{At}\int_0^te^{(sI-A)\tau}B\,d\tau+De^{st}.$$
If no eigenvalue of $A$ equals $\pm i\omega$, $sI-A$ is invertible, so the integral is $(sI-A)^{-1}\big(e^{(sI-A)t}-I\big)B$. With $e^{At}e^{(sI-A)t}=e^{st}I$ (added step),
$$y(t)=Ce^{At}\big(x(0)-(sI-A)^{-1}B\big)+\big(C(sI-A)^{-1}B+D\big)e^{st}.\tag{6.23}$$
The first term is transient (decays if the system is asymptotically stable) and the second is steady state, proportional to $e^{st}$ (p. 6-23). Write $y_{ss}=Me^{i\theta}e^{st}$ with
$$Me^{i\theta}=G(s)=C(sI-A)^{-1}B+D.\tag{6.24}$$
For $s=i\omega$, gain is $M=|G(i\omega)|$ and phase is $\theta=\arg G(i\omega)$. If $u=A_u\sin(\omega t+\psi)$ and $y=A_y\sin(\omega t+\varphi)$, then gain$(\omega)=A_y/A_u=M$ and phase$(\omega)=\varphi-\psi=\theta$. Also
$$y_{ss}(t)=\mathrm{Re}\big(G(i\omega)e^{i\omega t}\big)=M\cos(\omega t+\theta)\tag{6.25}$$
for $u=\cos\omega t$. Positive $\theta$: output *leads*; otherwise *lags*. From a plot, $\theta=-2\pi\,\Delta T/T$ (Fig. 6.11a). Plotting gain and phase against $\omega$ gives a Bode plot (Fig. 6.11b; Section 9.6) (p. 6-23).

*Intuition note.* In steady state, a stable linear system acts on a sine only by scaling it and shifting its phase. $G(i\omega)$ is the single complex number that records both effects at frequency $\omega$.

**Example 6.8 (active band-pass filter, pp. 6-23 to 6-25).** With $v_-=v_+=0$ and states $v_2,v_3$:
$$\dot v_2=\frac{v_1-v_2}{R_1C_1},\qquad\dot v_3=-\frac{v_3}{R_2C_2}-\frac{v_1-v_2}{R_1C_2}.$$
$$\frac{dx}{dt}=\begin{pmatrix}-\frac1{R_1C_1}&0\\\frac1{R_1C_2}&-\frac1{R_2C_2}\end{pmatrix}x+\begin{pmatrix}\frac1{R_1C_1}\\-\frac1{R_1C_2}\end{pmatrix}u,\quad y=(0\ \ 1)x,\tag{6.26}$$
with $x=(v_2,v_3)$, $u=v_1$, $y=v_3$. Then
$$Me^{i\theta}=-\frac{R_2}{R_1}\,\frac{R_1C_1s}{(1+R_1C_1s)(1+R_2C_2s)},\quad s=i\omega.$$
For $R_1=100\,\Omega$, $R_2=5\,\mathrm{k}\Omega$, $C_1=C_2=100\,\mu$F: signals near 15 rad/s pass with small attenuation. Signals below 2 or above 100 rad/s are attenuated. At 0.1 rad/s the attenuation factor is 20. The author calls it a band-pass filter passing roughly 5 to 50 rad/s (p. 6-24). Phase starts at $-90^\circ$ due to the op amp's negative gain (Fig. 6.12) (p. 6-25).

**Standard frequency-response properties (p. 6-25).**
- *Zero frequency gain* $M_0=G(0)=-CA^{-1}B+D$. It is well defined only if $A$ is invertible. It is relevant only if the equilibrium $x_e=-A^{-1}Br$ for constant input $u=r$ is stable. In electrical engineering it is called the DC gain.
- *Bandwidth* $\omega_b$: frequency range over which gain has decreased by no more than a factor $1/\sqrt2$ from its reference value. The reference is the zero frequency gain if that is nonzero and finite, or the high-frequency gain for systems that attenuate low frequencies and pass high ones. For a band-pass system like Example 6.8, it is the range where gain exceeds $1/\sqrt2$ of the gain at band centre (about 2 to 100 rad/s for Example 6.8).
- *Resonant peak* $M_r$: the largest value of the frequency response. *Peak frequency* $\omega_{mr}$: where it occurs.

**Example 6.9 (atomic force microscope, contact mode, p. 6-26).** The piezo stack is a second-order system (natural frequency $\omega_3$, damping $\zeta_3$) coupled to the AFM dynamics:
$$\dot x=\begin{pmatrix}0&1&0&0\\-\frac{k_2}{m_1+m_2}&-\frac{c_2}{m_1+m_2}&\frac1{m_2}&0\\0&0&0&\omega_3\\0&0&-\omega_3&-2\zeta_3\omega_3\end{pmatrix}x+\begin{pmatrix}0\\0\\0\\\omega_3\end{pmatrix}u,\quad y=\frac{m_2}{m_1+m_2}\Big(\frac{m_1k_2}{m_1+m_2}\ \ \frac{m_1c_2}{m_1+m_2}\ \ 1\ \ 0\Big)x.$$
Frequency response (Fig. 6.13): $M_0=1$; peaks $M_{r1}=2.12$ at 238 krad/s and $M_{r2}=4.29$ at 746 krad/s; a dip $M_d=0.556$ at 268 krad/s (an *antiresonance*, associated with a phase dip, which limits performance under simple controllers, Chapter 11). Neglecting the dip, $\omega_b=1.12$ Mrad/s (p. 6-26).

**Periodic and transient inputs (p. 6-27).** Decompose a periodic input $u(t)=\sum_k a_k\sin(k\omega_ft)+b_k\cos(k\omega_ft)$. By (6.25) and superposition,
$$y(t)=\sum_k|G(ik\omega_f)|\Big(a_k\sin\big(k\omega_ft+\arg G(ik\omega_f)\big)+b_k\cos\big(k\omega_ft+\arg G(ik\omega_f)\big)\Big).$$
For a transient input, approximate its initial part by the periodic $u_p$ equal to $u(t)$ on $[0,T/2)$ and 0 on $[T/2,T)$. The Fourier transforms satisfy $y_F(i\omega)=G(i\omega)u_F(i\omega)$. The inverse transform gives $y_p(t)$, efficiently via fast Fourier transforms (Exercise 6.12) (p. 6-27).

**Sampling (pp. 6-27, 6-28).** Let the control signal be constant over a sampling interval of length $h$ (continuous from the right). From (6.14),
$$x(t+h)=e^{Ah}x(t)+\int_t^{t+h}e^{A(t+h-\tau)}Bu(\tau)d\tau=:\Phi x(t)+\Gamma u(t).\tag{6.27}$$
At times $t=kh$:
$$x[k+1]=\Phi x[k]+\Gamma u[k],\quad y[k]=Cx[k]+Du[k],\qquad\Phi=e^{Ah},\ \Gamma=\Big(\int_0^he^{As}ds\Big)B.\tag{6.28}$$
(The form of $\Gamma$ follows by substituting $s=t+h-\tau$ and using constant $u$: added step.) This is an exact representation at the sampling instants (p. 6-28). The passage from (6.27) to (6.28) is called *sampling*. Going back from the sampled to the continuous matrices:
$$A=\tfrac1h\log\Phi,\qquad B=\Big(\int_0^he^{As}ds\Big)^{-1}\Gamma,\tag{6.29}$$
and if $A$ is invertible, $\Gamma=A^{-1}(e^{Ah}-I)B$. Every continuous-time system can be sampled, but some discrete-time systems have no continuous-time equivalent, because matrix logarithms are subtle (there may be many). $\Phi$ nonsingular is necessary but not sufficient. A real matrix has a real logarithm iff it is invertible and each Jordan block for a negative eigenvalue occurs an even number of times (the author cites [Cul66]). So $\Phi$ cannot have isolated eigenvalues on the negative real axis (p. 6-28).

**Example 6.10 (IBM Lotus server, p. 6-28).** The discrete model is $x[k+1]=ax[k]+bu[k]$, $a=0.43$, $b=0.47$, $h=60$ s. By (6.29): $A=\log a/h=-0.0141$, $B=(\int_0^he^{At}dt)^{-1}b=0.0116$. So it is a sampled version of $\dot x=-0.0141x+0.0116u$.

*Intuition note.* Holding the input constant between samples makes the exact one-step update $x[k+1]=e^{Ah}x[k]+\dots$. So "continuous" and "discrete" linear models translate into each other exactly at the sampling instants, as long as a real matrix logarithm exists (the book notes this can fail, p. 6-28).

### 6.4 Linearization

Controllers are often designed on a linear model and checked on the nonlinear one (pp. 6-28, 6-29).

**Example 6.11 (cruise control, pp. 6-29, 6-30).** The model is
$$m\dot v=\alpha_nuT(\alpha_nv)-mgC_r\,\mathrm{sgn}(v)-\tfrac12\rho C_dAv|v|-mg\sin\theta.\tag{6.30}$$
The terms are engine force, rolling friction, aerodynamic drag and gravitational disturbance. An equilibrium $(v_e,u_e)$ exists when engine force balances the disturbance forces. Taylor expansion gives
$$\frac{d(v-v_e)}{dt}=-a(v-v_e)-b_g(\theta-\theta_e)+b(u-u_e)+\text{higher-order terms},\tag{6.31}$$
$$a=\frac{\rho C_dA|v_e|-u_e\alpha_n^2T'(\alpha_nv_e)}{m},\quad b_g=g\cos\theta_e,\quad b=\frac{\alpha_nT(\alpha_nv_e)}{m}.\tag{6.32}$$
The rolling-friction term disappears for $v>0$. For fourth gear, $v_e=20$ m/s, $\theta_e=0$: $u_e=0.1687$, $a=0.01$, $b=1.32$, $b_g=9.8$ (p. 6-29). A PI controller ($k_p=0.5$, $k_i=0.1$, with anti-windup) was simulated on a nonlinear and a linear model as the car meets a 4° or 6° hill at $t=5$ s (Fig. 6.14). The curves differ very little (especially for 4°), so design on the linearization is validated (pp. 6-29, 6-30).

**Jacobian linearization (p. 6-30).** For $\dot x=f(x,u)$, $y=h(x,u)$ (6.33), $x\in\mathbb R^n$, $u,y\in\mathbb R$, with equilibrium $(x_e,u_e)$: set $z=x-x_e$, $v=u-u_e$, $w=y-h(x_e,u_e)$. Near the equilibrium the nonlinear terms are higher-order terms of a Taylor expansion (the argument is like $\sin\theta\approx\theta$). The Jacobian linearization is
$$\dot z=Az+Bv,\quad w=Cz+Dv,\tag{6.34}$$
$$A=\frac{\partial f}{\partial x}\Big|_{(x_e,u_e)},\ B=\frac{\partial f}{\partial u}\Big|_{(x_e,u_e)},\ C=\frac{\partial h}{\partial x}\Big|_{(x_e,u_e)},\ D=\frac{\partial h}{\partial u}\Big|_{(x_e,u_e)}.\tag{6.35}$$
By Theorem 5.3, if the linearization is asymptotically stable, then $x_e$ is locally asymptotically stable for the full nonlinear system (p. 6-30).

**Example 6.12 (p. 6-31).** For cruise control with constant $\theta_e$, $x=v$, $f=\frac{\alpha_n}muT(\alpha_nx)-gC_r\mathrm{sgn}(x)-\frac12\frac{\rho C_dA}mx|x|-g\sin\theta_e$, $h=x$. At $x_e=v_e>0$: $A=\frac{u_e\alpha_n^2T'(\alpha_nx_e)-\rho C_dA|x_e|}m$, $B=\frac{\alpha_nT(\alpha_nx_e)}m$, $C=1$, $D=0$. This matches Example 6.11 (here $A=-a$) (p. 6-31).

**Linearize only near a solution (p. 6-31).** Take $\dot x=a_0+a_1x+a_2x^2+a_3x^3+u$ with $a_0\ne0$. Equilibria are $(x_e,\,-a_0-a_1x_e-a_2x_e^2-a_3x_e^3)$. Dropping higher-order terms at the origin gives $\dot x=a_0+a_1x+u$, which is not the Jacobian linearization when $a_0\ne0$, since $(0,0)$ is not a solution. Even with the constant kept, the system would quickly move away because $a_0$ drives it. Linearizing about a trajectory gives a time-varying linear system (p. 6-31).

**Example 6.13 (vehicle steering, pp. 6-32, 6-33).** The equations are $\frac d{dt}(x,y,\theta)=(v\cos(\alpha(\delta)+\theta),\ v\sin(\alpha(\delta)+\theta),\ \frac{v\sin\alpha(\delta)}a)$, $\alpha(\delta)=\arctan\big(\frac{a\tan\delta}b\big)$. The full model cannot formally be linearized about straight motion because $\dot x^2+\dot y^2=v^2\ne0$ means the $xy$ motion is not at equilibrium. Focus on lateral deviation: $\theta_e=0$, state $x=(y,\theta)$, $u=\delta$:
$$f=\begin{pmatrix}v_0\sin(\alpha(u)+x_2)\\\frac{v_0\sin\alpha(u)}a\end{pmatrix},\ h=x_1.$$
At $x=(0,0)$, $u=0$:
$$A=\begin{pmatrix}0&v_0\\0&0\end{pmatrix},\ B=\begin{pmatrix}av_0/b\\v_0/b\end{pmatrix},\ C=(1\ \ 0),\ D=0.\tag{6.36}$$
Normalizing length by wheelbase $b$ and time by $\tau=v_0t/b$ with $z=(x_1/b,x_2)$:
$$\frac{dz}{d\tau}=\begin{pmatrix}0&1\\0&0\end{pmatrix}z+\begin{pmatrix}\gamma\\1\end{pmatrix}u,\quad y=(1\ \ 0)z,\quad\gamma=a/b.\tag{6.37}$$
It has a single parameter $\gamma$ (p. 6-33).

**Feedback linearization (pp. 6-33, 6-34).**

*Example 6.14 (cruise control).* Choose
$$u=\frac1{\alpha_nT(\alpha_nv)}\Big(\tilde u+mgC_r\,\mathrm{sgn}(v)+\tfrac12\rho C_dAv|v|\Big).\tag{6.38}$$
Then (6.30) becomes
$$m\dot v=\tilde u+d,\qquad d(t)=-mg\sin\theta(t).\tag{6.39}$$
This is linear. A controller (e.g. PID) is designed for $\tilde u$, and (6.38) gives the real input. It needs an accurate measurement of $v$ and an accurate model (engine torque, gears, drag, friction, mass). Such a model is generally not available, but a good feedback law for $\tilde u$ can give robustness to the uncertainties (p. 6-33).

*Definition.* $\dot x=f(x,u)$, $y=h(x)$ is *feedback linearizable* if some control law $u=\alpha(x,v)$ makes the closed loop input/output linear with input $v$ and output $y$ (Fig. 6.15). The general theory also allows nonlinear changes of state coordinates, keeping input and output fixed. Full characterization is beyond the text (see Isidori, Khalil) (p. 6-33).

*Mechanical systems.* For $M(q)\ddot q+C(q,\dot q)=B(q)u$ ($q\in\mathbb R^n$, $M$ inertia matrix, $C$ Coriolis and other nonlinear forces, $B\in\mathbb R^{n\times p}$), if $p=n$ and $B(q)$ is invertible for all $q$, choose
$$u=B^{-1}(q)\big(M(q)v+C(q,\dot q)\big).\tag{6.40}$$
Then $M(q)\ddot q=M(q)v$, i.e. $\ddot q=v$, which is linear. This is called *computed torque* in robotics and *dynamic inversion* in aircraft flight control. Caution: feedback linearization can cancel beneficial terms of the natural dynamics, so use it with care (p. 6-34).

*Intuition note.* If you know the nonlinear terms, the controller can subtract them exactly so that what remains is a simple linear system. The price is that you need a good model, and you may cancel useful dynamics.

### 6.5 Further reading (pp. 6-34, 6-35)
The author says most material is classical and cites standard texts. Brockett [Bro70] presents linear systems via the matrix exponential. Step-response characterization is credited to Heaviside, whose methods were criticized for rigor until Schwartz's distribution theory. Matrix-exponential use began with 1960s control theory, helped by numerical linear-algebra software (p. 6-35).

## Toy example (ours, not from the text)
**Part 1: double integrator, convolution equation.** $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $B=\begin{pmatrix}0\\1\end{pmatrix}$, $C=(1\ 0)$, $D=0$, $x(0)=(1,0)^T$, $u=1$ for $t>0$. We have $e^{At}=\begin{pmatrix}1&t\\0&1\end{pmatrix}$ (from $A^2=0$). Then
- $Ce^{At}x(0)=1$ and $Ce^{At}B=t$, so $h(t)=t$.
- $y(t)=1+\int_0^t(t-\tau)\cdot1\,d\tau=1+t^2/2$.
- At $t=2$: $y=1+2=3$.
- Direct check: $\ddot q=1$, $q(0)=1$, $\dot q(0)=0$ gives $q=1+t^2/2$. ✓.

**Part 2: stable scalar system, step and frequency response.** $\dot x=-2x+2u$, $y=x$ ($A=-2,B=2,C=1,D=0$).
- Step response by (6.22): $CA^{-1}e^{At}B=\tfrac1{-2}e^{-2t}\cdot2=-e^{-2t}$, and $D-CA^{-1}B=0+1=1$. So $y=1-e^{-2t}$. Steady state is 1. Zero frequency gain $M_0=-CA^{-1}B+D=1$.
- $G(s)=C(sI-A)^{-1}B+D=2/(s+2)$. At $\omega=2$: $G(2i)=2/(2+2i)$, so $M=2/\sqrt8=0.7071=1/\sqrt2$ and $\theta=-\arctan(2/2)=-45^\circ$. So the bandwidth is 2 rad/s, and the output lags.

**Part 3: sampling.** With $h=0.5$: $\Phi=e^{-1}=0.3679$, $\Gamma=A^{-1}(e^{Ah}-1)B=(-\tfrac12)(0.3679-1)(2)=0.6321$. Then $x[k+1]=0.3679x[k]+0.6321u[k]$, and for $u=1$ the fixed point is $0.6321/(1-0.3679)=1$, matching $M_0=1$.

## Concepts
- [[state-space-model]] — $\dot x=Ax+Bu,\ y=Cx+Du$ as the general linear system form (p. 6-3)
- [[linear-system-superposition]] (new) — outputs jointly linear in initial state and input; response to a sum of inputs is the sum of responses (p. 6-3)
- [[time-invariance]] (new) — shifting the input in time shifts the output by the same amount (p. 6-4)
- [[matrix-exponential]] (new) — $e^{X}=\sum X^k/k!$; $x(t)=e^{At}x(0)$ solves $\dot x=Ax$ (pp. 6-6, 6-7)
- [[jordan-form]] (new) — block form with eigenvalues on the diagonal; 1's may appear on the superdiagonal, coupling states, when there are equal eigenvalues (p. 6-9)
- [[eigenvalues-and-modes]] — an eigenpair gives a mode $e^{\lambda t}v$; the eigenvector is the mode shape (p. 6-13)
- [[stability]] — here: asymptotic stability iff all $\mathrm{Re}\lambda_i<0$; if no eigenvalue has positive real part and some have zero real part, Lyapunov stability holds iff the Jordan blocks of the zero-real-part eigenvalues are scalar (p. 6-11)
- [[convolution-equation]] (new) — $y=Ce^{At}x(0)+\int Ce^{A(t-\tau)}Bu\,d\tau+Du$ (p. 6-16)
- [[impulse-response]] (new) — output for a delta input, $h=Ce^{At}B+D\delta(t)$; derivative of the step response (p. 6-17)
- [[step-response]] (new) — output for a unit step; characterized by rise time, overshoot, settling time, steady-state value (pp. 6-20, 6-21)
- [[transient-vs-steady-state]] (new) — short-term part reflecting initial mismatch vs long-term part driven by the input (p. 6-19)
- [[frequency-response]] (new) — $G(i\omega)=C(i\omega I-A)^{-1}B+D$; gain $|G|$ and phase $\arg G$ for sinusoidal input (p. 6-23)
- [[transfer-function]] — here $G(s)=C(sI-A)^{-1}B+D$, appearing as the steady-state factor for input $e^{st}$ (p. 6-23)
- [[bode-plot]] — gain and phase of $G(i\omega)$ plotted against $\omega$ (p. 6-23)
- [[bandwidth-and-dc-gain]] (new) — zero frequency gain $G(0)$; bandwidth = range where gain stays within $1/\sqrt2$ of the reference (p. 6-25)
- [[coordinate-transformation]] (new) — $z=Tx$ gives $\tilde A=TAT^{-1}$, $\tilde B=TB$, $\tilde C=CT^{-1}$; eigenvalues unchanged (p. 6-18)
- [[sampling]] (new) — exact discrete-time model for piecewise-constant input: $\Phi=e^{Ah}$, $\Gamma=(\int_0^he^{As}ds)B$ (p. 6-27)
- [[linearization]] — Jacobian matrices at an equilibrium give a local linear model; valid only near a solution (pp. 6-30, 6-31)
- [[feedback-linearization]] (new) — nonlinear feedback $u=\alpha(x,v)$ making the input–output map linear (p. 6-33)
- [[robustness]] — here: a good feedback law for $\tilde u$ can tolerate model uncertainty in the cancellation (p. 6-33)

## Canonical instances
- [[double-integrator]] — $\ddot q=u$; $A^2=0$ so $e^{At}=I+At$ (p. 6-7)
- [[undamped-oscillator]] — $e^{At}=\begin{pmatrix}\cos\omega_0t&\sin\omega_0t\\-\sin\omega_0t&\cos\omega_0t\end{pmatrix}$ (p. 6-8)
- [[vectored-thrust-aircraft]] — eigenvalue 0 with a non-scalar Jordan block makes the linearization unstable (p. 6-12)
- [[coupled-spring-mass]] — decouples into two modes by a change of coordinates (pp. 6-14, 6-18)
- [[compartment-model]] — drug step response, settling time 39 min (p. 6-21)
- [[active-band-pass-filter]] — op amp circuit with a band-pass frequency response (p. 6-23)
- [[atomic-force-microscope]] — two resonant peaks and an antiresonance (p. 6-26)
- [[ibm-lotus-server]] — discrete model converted to a continuous one (p. 6-28)
- [[cruise-control]] — linearization validated on hills; feedback linearization example (pp. 6-29, 6-33)
- [[vehicle-steering]] — linearized lateral dynamics with single parameter $\gamma=a/b$ (p. 6-32)

## Bridges (candidates)
- [same-math] Linearization of a nonlinear ODE ↔ multivariable calculus: first-order Taylor expansion with the Jacobian — the matrices (6.35) are partial derivatives.
- [same-math] Sampling a continuous linear system (6.28) ↔ discrete-time linear systems/difference equations: $x[k+1]=\Phi x[k]+\Gamma u[k]$ is the one-step solution of (6.14). Exercise 6.9 gives a Keynesian economic model of the same form.
- [structural-analogy] Modes and eigenvectors ↔ principal components / spectral decomposition in data analysis: a state vector decomposed along eigen-directions that evolve independently.
- [structural-analogy] Impulse-response convolution ↔ signal filtering in time-series analysis: output is the input weighted by a kernel.
- [structural-analogy] Feedback linearization (cancel the nonlinearity) ↔ inverse-model/computed-torque control in robotics (named in the text).

## Questions this raises
- When the linearization has an eigenvalue with zero real part, what does the Jordan structure say about the nonlinear system? (Example 6.4 and Prop. 6.3 treat only the linear case.)
- How accurate is a linearized model, and how far from the equilibrium can the state wander before design based on it fails?
- When does a discrete-time model have a real continuous-time counterpart, given the matrix-logarithm condition on $\Phi$?
- How much model error can feedback linearization tolerate before the cancellation fails? (The text says only that a good feedback law for $\tilde u$ can give robustness.)

## Exercises worth doing
- Ex. 6.2 (p. 6-35) — derive the convolution equation from the impulse decomposition and superposition — difficulty: medium
- Ex. 6.5 (p. 6-36) — show $P=\int_0^\infty e^{A^T\tau}Qe^{A\tau}d\tau$ gives a Lyapunov function when all $\mathrm{Re}\lambda_j<0$ — difficulty: medium
- Ex. 6.6 (p. 6-36) — prove Proposition 6.3 via non-scalar Jordan blocks — difficulty: hard
- Ex. 6.7 (p. 6-36) — rise and settling times of a first-order system in terms of the time constant $\tau$ — difficulty: easy
- Ex. 6.8 (pp. 6-36, 6-37) — discrete-time convolution and stability conditions on eigenvalue magnitudes — difficulty: medium
- Ex. 6.13 (p. 6-38) — linearize $\dot x=1-x^3+u$ about its equilibrium, check against (6.34) — difficulty: easy

## Reading notes
- Page labels carry no printed number ("?"), but every page image shows a running header "6-N" (e.g. "6-2"). I cite as (p. 6-N). Offset: printed 6-N = pdf (N + 190), so pdf 191 is 6-1 and pdf 228 is 6-38.
- Fig. 6.6 caption shows pulses of width 5, 2.5 and 0.8, but the text (p. 6-17) discusses $\epsilon=1$ s with $\epsilon\sigma_{\max}=0.62$. I report both as printed.
- Example 6.8 gives both "passes roughly 5 to 50 rad/s" (p. 6-24) and "bandwidth approximately 2 to 100 rad/s" (p. 6-25). These are different descriptions in the source and I kept both.
- In Exercise 6.10 the image shows the right-hand side as $b\,dc/dt$ with lowercase $c$, presumably meant as $C$. I did not resolve it.
- Section 6.5 contains historical remarks (Heaviside, Schwartz, etc.). I only paraphrased them lightly.
- The text layer was garbled on equations. All equations were checked against the images.
