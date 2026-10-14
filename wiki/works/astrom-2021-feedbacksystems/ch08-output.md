---
id: astrom-2021-feedbacksystems/ch08-output
work: astrom-2021-feedbacksystems
unit: "8 Output Feedback"
pages: 8-1 to 8-34
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
# Output Feedback (Åström & Murray, ch. 8)

## L0 — One line
If a linear system is reachable and observable, an observer (a model corrected by the measured output) can rebuild the hidden state, and feeding back that estimate gives a closed loop whose eigenvalues are those of the state-feedback design together with those of the observer, so the two designs can be done separately.

## L1 — The gist (≤ 120 words)
Chapter 7 assumed every state is measured. This chapter asks what to do when only a few outputs are measured. A system is observable when the state can be recovered from inputs and outputs. Then an observer, $\dot{\hat x}=A\hat x+Bu+L(y-C\hat x)$, can have its error dynamics placed by choosing $L$. State feedback on $\hat x$ gives closed-loop eigenvalues equal to those of $A-BK$ plus those of $A-LC$ (separation). With known noise statistics, the Kalman filter chooses $L$ to minimise the mean square estimation error. Feedforward from a trajectory generator, gain scheduling, state augmentation for disturbances and computer implementation complete a practical controller.

**Prerequisites:** state-space models $\dot x = Ax+Bu$; eigenvalues and characteristic polynomial; matrix rank and transpose; state feedback by eigenvalue assignment and reachability (ch. 7); LQR and the Riccati equation (ch. 7); basic probability (mean, covariance, white noise) for §8.4.

## L2 — Key ideas
- A linear system is observable if and only if $W_o=(C;CA;\dots;CA^{n-1})$ has full row rank; observability tells you whether a sensor set is enough for control (p. 8-3, 8-2).
- Differentiating the output to get the state is not particularly practical when there is measurement noise. An observer instead runs a model copy driven by the output error $L(y-C\hat x)$ (p. 8-3, 8-7).
- The estimation error obeys $\dot{\tilde x}=(A-LC)\tilde x$. Observer design is the dual of state-feedback design, so eigenvalues of $A-LC$ can be placed as desired if the system is observable (shown for one input and one output) (p. 8-7, 8-8).
- With $u=-K\hat x+k_f r$, the closed-loop characteristic polynomial factors into $\det(sI-A+BK)\det(sI-A+LC)$. This is the separation principle, and the controller contains a model of the plant (p. 8-12, 8-13).
- Kalman's decomposition splits a linear system into four parts, according to whether states are reachable (the input can drive them) and observable (they show in the output). With zero initial state in the other parts, input–output behaviour depends only on the reachable and observable part (p. 8-15, 8-16).
- The Kalman filter gives the mean-square-optimal observer gain. The discrete case uses a covariance recursion; the continuous case uses a Riccati equation (a matrix equation for the error covariance $P$) that mirrors the one for LQR (the optimal state feedback for a quadratic cost, chapter 7). Combining the filter with LQR gives LQG control, which splits into the two separate designs (p. 8-18, 8-20, 8-22).
- A two-degree-of-freedom controller adds a trajectory generator (it computes the desired state and a feedforward input) to observer plus state feedback. For differentially flat systems (state and input are functions of a flat output and its derivatives), feasible trajectories can be computed efficiently without integrating differential equations (p. 8-23, 8-26).
- Practical extensions: estimating a constant disturbance as an extra state gives integral action (control that integrates the output error), gain scheduling (feedback gains that change with the operating point) handles varying operating points, the extended Kalman filter (nonlinear prediction plus a linearized correction gain) handles nonlinear plants, and a difference equation implements the observer on a computer (p. 8-27 to 8-31).

## L3 — Walkthrough

### Introduction (p. 8-1)
Chapter 7 gave state feedback assuming all states are measured by sensors. This chapter treats the realistic case of few measurements. The epigraph (Kalman, 1960) splits the problem in two: compute the "best approximation" $\hat x(t_1)$ of the state from $y(t)$, $t\le t_1$, then compute $u(t_1)$ from $\hat x(t_1)$ (p. 8-1).

### 8.1 Observability

**System.** $\dfrac{dx}{dt}=Ax+Bu,\; y=Cx+Du$ with $x\in\mathbb R^n$, $u\in\mathbb R^p$, $y\in\mathbb R^q$ (8.1) (p. 8-1). An observer takes $u$ and the (possibly noisy) measurement $y$ and outputs $\hat x$ (Fig. 8.1, p. 8-2).

**Definition 8.1 (Observability).** A linear system is observable if for every $T>0$ the state $x(T)$ can be determined from $y(t)$ and $u(t)$ on $[0,T]$ (p. 8-2). The definition also holds for nonlinear systems (p. 8-2).

- If observable, there are no "hidden" dynamics; observability decides whether a set of sensors suffices for control (p. 8-2).
- A model plus sensors acts as a "virtual sensor" for unmeasured variables. Reconciling many sensors through models is called sensor fusion (p. 8-2).

**Testing for observability.** Drop the input: $\dot x=Ax,\ y=Cx$ (8.2). Then $y=Cx$ gives the projection of $x$ onto the rows of $C$. If $n=q$ and $C$ is invertible, the problem is solved directly (p. 8-2). Otherwise differentiate: $\dot y = C\dot x = CAx$ (p. 8-2). Repeating gives

$$\begin{pmatrix} y\\ \dot y\\ \ddot y\\ \vdots\\ y^{(n-1)}\end{pmatrix}=\begin{pmatrix} C\\ CA\\ CA^2\\ \vdots\\ CA^{n-1}\end{pmatrix}x(t)\tag{8.3}$$

The state at time $t$ can be determined if the **observability matrix**

$$W_o=\begin{pmatrix} C\\ CA\\ CA^2\\ \vdots\\ CA^{n-1}\end{pmatrix}\tag{8.4}$$

has full row rank ($n$ independent rows), shape $(nq)\times n$. Derivatives beyond order $n-1$ are not needed (Cayley–Hamilton, Exercise 7.3) (p. 8-3). With inputs and several outputs the state is a linear combination of inputs, outputs and their derivatives, with the same criterion (left as an exercise) (p. 8-3). In practice, differentiating a noisy output gives large errors, so the method is "not particularly practical" (p. 8-3).

**Theorem 8.1 (Observability rank condition).** A linear system of form (8.1) is observable if and only if $W_o$ has full row rank (p. 8-3).

*Proof.* Sufficiency follows from the analysis above. For necessity, suppose the system is observable but $W_o$ is not full row rank. Pick $v\ne0$ with $W_ov=0$ (it exists because row and column rank are equal). Take $x(0)=v$, $u=0$, so $y(t)=Ce^{At}v$. Since $e^{At}$ is a power series in $A$ and $A^n$ and higher powers reduce to lower powers (Cayley–Hamilton), $y(t)\equiv 0$ (the author leaves the steps to the reader). Then input and output are both zero, so $\hat x=0$ would be a valid estimate for all time, but $x(0)=v\neq 0$. This contradiction shows $W_o$ must be full row rank (p. 8-3).

*Intuition note.* If some starting state produces an output that is zero forever, the output cannot tell that state apart from zero. The proof shows that a nonzero vector in the null space of $W_o$ would be such an invisible state, so full row rank rules it out.

**Example 8.1 (Compartment model, p. 8-3/8-4).** Two-compartment model with only the first compartment (blood plasma) measured:
$$\dot c=\begin{pmatrix}-k_0-k_1 & k_1\\ k_2 & -k_2\end{pmatrix}c+\begin{pmatrix}b_0\\0\end{pmatrix}u,\quad y=(1\ \ 0)\,c.$$
Then $W_o=\begin{pmatrix}1&0\\-k_0-k_1&k_1\end{pmatrix}$. The rows are linearly independent if $k_1\neq0$. Under that condition the tissue concentration can be determined from blood measurements (p. 8-4).

**A mechanism for unobservability (Fig. 8.2, p. 8-4).** Two identical subsystems have outputs that are combined (a $-1$ block feeds the summing node). The author says it seems intuitively clear that the states cannot be deduced, since the individual output contributions cannot be recovered from their difference; a formal argument is the subject of Exercise 8.2 (p. 8-4).

**Observable canonical form.** For a single-input single-output system:
$$\frac{dz}{dt}=\begin{pmatrix}-a_1&1&&0\\-a_2&0&\ddots&\\ \vdots&&\ddots&1\\-a_n&0&&0\end{pmatrix}z+\begin{pmatrix}b_1\\b_2\\ \vdots\\b_n\end{pmatrix}u,\qquad y=(1\ 0\ \cdots\ 0)z+d_0u.$$
The characteristic polynomial is $\lambda(s)=s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n$ (8.5) (p. 8-5). From the block diagram (Fig. 8.3): with $u,y$ known, $z_1$ is available. Differentiating $z_1$ gives $z_2=\dot z_1+a_1z_1-b_1u$, and so on for all states, but this needs differentiation (p. 8-5).

Formally, $\tilde W_o$ (observability matrix in this form) is lower triangular with 1 on the diagonal: first rows $(1,0,\dots)$, $(-a_1,1,0,\dots)$, $(-a_1^2-a_2,-a_1,1,\dots)$, and $*$ for unimportant entries. Its columns are independent, so it is invertible. Its inverse is (the author calls the calculation straightforward but tedious) the lower triangular matrix with rows $(1)$, $(a_1,1)$, $(a_2,a_1,1)$, …, $(a_{n-1},a_{n-2},\dots,a_1,1)$ (p. 8-6). A system is observable if and only if a transformation $T$ puts it in observable canonical form, so proofs can assume this form. The form may be poorly conditioned numerically (p. 8-6).

### 8.2 State estimation

**Goal.** Find a linear system $\dot{\hat x}=F\hat x+Gu+Hy$ with $\hat x(t)\to x(t)$ as $t\to\infty$ (p. 8-6). Take $D=0$:
$$\dot x=Ax+Bu,\quad y=Cx\tag{8.6}$$

**A first attempt: simulate the model.** $\dot{\hat x}=A\hat x+Bu$ (8.7). With $\tilde x=x-\hat x$ we get $\dot{\tilde x}=A\tilde x$. If $A$ has all eigenvalues in the left half-plane the error goes to zero, but possibly slower than desired (p. 8-7). The measurement $y$ does not appear in (8.7) and the system must be stable, so the estimate converges only because transients die out. The author calls this not very useful for control design, since we want the estimate to converge quickly to a nonzero state; a version that uses $y$ should converge fast and also work for unstable systems (p. 8-7).

**The observer.**
$$\dot{\hat x}=A\hat x+Bu+L(y-C\hat x)\tag{8.8}$$
$L(y-C\hat x)$ is proportional to the difference between measured and predicted output. Subtracting gives
$$\dot{\tilde x}=(A-LC)\tilde x.$$
If $L$ makes $A-LC$ have eigenvalues with negative real parts, $\tilde x\to0$, and the convergence rate is set by the eigenvalue choice (p. 8-7).

**Duality.** State feedback needs $K$ with $A-BK$ having given eigenvalues. Observer design needs $L$ with $A-LC$ having given eigenvalues. Since a matrix and its transpose have the same eigenvalues:
$$A\leftrightarrow A^T,\quad B\leftrightarrow C^T,\quad K\leftrightarrow L^T,\quad W_r\leftrightarrow W_o^T\tag{8.9}$$
Observer design is the *dual* of state feedback design (p. 8-7).

**Theorem 8.2 (Observer design by eigenvalue assignment).** Consider $\dot x=Ax+Bu,\ y=Cx$ (8.10), one input, one output, with $\lambda(s)=s^n+a_1s^{n-1}+\cdots+a_n$ the characteristic polynomial of $A$. If the system is observable, then
$$\dot{\hat x}=A\hat x+Bu+L(y-C\hat x)\tag{8.11}$$
is an observer, with
$$L=W_o^{-1}\widetilde W_o\begin{pmatrix}p_1-a_1\\p_2-a_2\\ \vdots\\p_n-a_n\end{pmatrix}\tag{8.12}$$
where $W_o$ is as in (8.4) and $\widetilde W_o$ is the *inverse* of the lower triangular matrix with rows $(1),(a_1,1),(a_2,a_1,1),\dots,(a_{n-1},\dots,a_1,1)$. The error $\tilde x$ then obeys a differential equation with characteristic polynomial $p(s)=s^n+p_1s^{n-1}+\cdots+p_n$ (p. 8-8). This form is much more useful than pure differentiation (8.3) (p. 8-8).

*Intuition note.* Because observer design is the transpose of state-feedback design, the "eigenvalue placement" tools from chapter 7 carry over. Observability plays the role that reachability played there.

**Example 8.2 (Compartment model).** From Example 8.1: $\lambda(s)=s^2+(k_0+k_1+k_2)s+k_0k_2$. With desired $s^2+p_1s+p_2$, (8.12) gives
$$L=\begin{pmatrix}1&0\\-k_0-k_1&k_1\end{pmatrix}^{-1}\begin{pmatrix}1&0\\k_0+k_1+k_2&1\end{pmatrix}^{-1}\begin{pmatrix}p_1-k_0-k_1-k_2\\p_2-k_0k_2\end{pmatrix}=\begin{pmatrix}p_1-k_0-k_1-k_2\\(p_2-p_1k_2+k_1k_2+k_2^2)/k_1\end{pmatrix}.$$
The condition $k_1\neq0$ is essential. Fig. 8.4b shows the estimated concentrations approaching the true ones (p. 8-8, 8-9).

**Structure of the observer.** The rate of change of $\hat x$ has two terms: $A\hat x+Bu$ (the model driven with $\hat x$) and $L(y-\hat y)$, with $\hat y=C\hat x$. $L$ ($n\times q$) weights and distributes the output error among the state estimates. The observer contains a copy of the process model driven by $y-\hat y$ through $L$ (Fig. 8.5, p. 8-9).

**Computing the observer gain.** For low order, treat the entries of $L$ as unknowns and match the characteristic polynomial (p. 8-10).

**Example 8.3 (Vehicle steering).** Normalized model (8.13): $\dot x=\begin{pmatrix}0&1\\0&0\end{pmatrix}x+\begin{pmatrix}\gamma\\1\end{pmatrix}u,\ y=(1\ 0)x$. $x_1$ is lateral path deviation and $x_2$ is turning rate. $W_o$ is the identity, so the system is observable. Then
$$A-LC=\begin{pmatrix}-l_1&1\\-l_2&0\end{pmatrix},\qquad \det(sI-A+LC)=\det\begin{pmatrix}s+l_1&-1\\l_2&s\end{pmatrix}=s^2+l_1s+l_2.$$
Matching $s^2+p_1s+p_2=s^2+2\zeta_o\omega_os+\omega_o^2$ gives $l_1=p_1=2\zeta_o\omega_o$, $l_2=p_2=\omega_o^2$. The observer is $\dot{\hat x}=A\hat x+Bu+L(y-\hat x_1)$. In the simulation (Fig. 8.6, $\omega_o=1$, $\zeta_o=0.7$, time normalized by vehicle length) the observer error settles in about 4 vehicle lengths (p. 8-10, 8-11).

**Numerics and noise (p. 8-11).** For high order, use numerical tools. Duality means state-feedback algorithms work for observers using the transposed $A$ and $C$. MATLAB `acker` implements Theorem 8.2 (one output). `place` handles many outputs and is better conditioned. A fast observer converges fast, but its gains are high and the estimate is more sensitive to measurement noise. If noise characteristics are known the best compromise can be found; the observer is then a Kalman filter (§8.4) (p. 8-11).

### 8.3 Control using estimated state

**Setup.** $\dot x=Ax+Bu,\ y=Cx$ (8.14), $D=0$ (a direct term with proportional action creates an algebraic loop, Section 9.4). $u,y$ scalar; system reachable and observable (p. 8-11, 8-12). Try
$$u=-K\hat x+k_fr\tag{8.15}$$
with $\hat x$ from the observer
$$\dot{\hat x}=A\hat x+Bu+L(y-C\hat x)\tag{8.16}$$
It is "not clear" that this works. The closed loop has state $(x,\hat x)$ of dimension $2n$ (p. 8-12).

**Derivation.** Use $\tilde x=x-\hat x$ (8.17). Subtracting (8.16) from (8.14):
$$\dot{\tilde x}=Ax-A\hat x-L(Cx-C\hat x)=A\tilde x-LC\tilde x=(A-LC)\tilde x.$$
For the process:
$$\dot x=Ax+Bu=Ax-BK\hat x+Bk_fr=Ax-BK(x-\tilde x)+Bk_fr=(A-BK)x+BK\tilde x+Bk_fr.$$
Hence, with $K\in\mathbb R^{1\times n}$, $L\in\mathbb R^{n\times1}$, the $2n\times2n$ system
$$\frac{d}{dt}\begin{pmatrix}x\\\tilde x\end{pmatrix}=\begin{pmatrix}A-BK&BK\\0&A-LC\end{pmatrix}\begin{pmatrix}x\\\tilde x\end{pmatrix}+\begin{pmatrix}Bk_f\\0\end{pmatrix}r\tag{8.18}$$
The observer error $\tilde x$ is not affected by $r$, which is desirable. The dynamics matrix is block triangular (the text says "block diagonal"), so
$$\lambda(s)=\det(sI-A+BK)\,\det(sI-A+LC)\quad (p.\ 8\text{-}12).$$

**Theorem 8.3 (Eigenvalue assignment by output feedback).** For $\dot x=Ax+Bu,\ y=Cx$, the controller
$$\dot{\hat x}=A\hat x+Bu+L(y-C\hat x)=(A-BK-LC)\hat x+Bk_fr+Ly,\qquad u=-K\hat x+k_fr$$
gives closed-loop characteristic polynomial $\det(sI-A+BK)\det(sI-A+LC)$. This polynomial can be assigned arbitrary roots if the system is reachable and observable (p. 8-13).

- $K$ depends only on $A,B$; $L$ depends only on $A,C$. Splitting the design this way is the **separation principle** (p. 8-13).
- The controller is a dynamic compensator and contains a model of the plant: the **internal model principle** (Fig. 8.7, p. 8-13/8-14).
- It is not obvious how performance and robustness are reflected in the closed-loop eigenvalues, so the author recommends evaluating a design, for example by plotting time responses. Robustness of pole placement is deferred to Section 14.5 (p. 8-13).

*Intuition note.* The state-feedback part and the observer part do not disturb each other's eigenvalues. You can compute the state-feedback gain assuming all states are measured, and then design the estimator separately.

**Example 8.4 (Vehicle steering).** Combine the state feedback of Example 7.4 with the observer of Example 8.3. The controller is $\dot{\hat x}=A\hat x+Bu+L(y-C\hat x)$, $u=-K\hat x+k_fr=k_1(r-\hat x_1)-k_2\hat x_2$, with $k_f=k_1$. Eliminating $u$:
$$\dot{\hat x}=(A-BK-LC)\hat x+Ly+Bk_fr=\begin{pmatrix}-l_1-\gamma k_1&1-\gamma k_2\\-k_1-l_2&-k_2\end{pmatrix}\hat x+\begin{pmatrix}l_1\\l_2\end{pmatrix}y+\begin{pmatrix}\gamma\\1\end{pmatrix}k_1r.$$
It is a second-order controller with inputs $y,r$ and output $u$. In simulation the estimator starts at zero while the true lateral position is 0.8; estimates converge quickly. Tracking has errors because the road curves; feedforward (§8.5) can improve this (p. 8-14).

**Kalman's decomposition (subsection marked with a margin symbol, p. 8-15).** Reachability and observability classify the dynamics. **Kalman's decomposition theorem**: a linear system divides into four subsystems: $\Sigma_{ro}$ (reachable and observable), $\Sigma_{r\bar o}$ (reachable, not observable), $\Sigma_{\bar ro}$ (not reachable, observable), $\Sigma_{\bar r\bar o}$ (neither) (p. 8-15).

*Special case*: one input, one output, distinct eigenvalues of $A$. In suitable coordinates, with reordering:
$$\frac{dx}{dt}=\begin{pmatrix}A_{ro}&0&0&0\\0&A_{r\bar o}&0&0\\0&0&A_{\bar ro}&0\\0&0&0&A_{\bar r\bar o}\end{pmatrix}x+\begin{pmatrix}B_{ro}\\B_{r\bar o}\\0\\0\end{pmatrix}u,\quad y=(C_{ro}\ \ 0\ \ C_{\bar ro}\ \ 0)\,x+Du\tag{8.19}$$
States $x_k$ with $B_k\neq0$ are reachable; states with $C_k\neq0$ are observable. With zero initial state (or steady state if $A$ is stable), the non-reachable states stay zero and the unobservable state does not affect the output. So $y$ follows from
$$\dot x_{ro}=A_{ro}x_{ro}+B_{ro}u,\quad y=C_{ro}x_{ro}+Du.$$
From the input/output viewpoint only the reachable and observable dynamics matter (Fig. 8.9a, p. 8-15).

*General case* (needs more linear algebra; Kalman, Ho, Narendra). The state space still splits into four parts, with extra coupling ($*$ = blocks of suitable size):
$$\frac{dx}{dt}=\begin{pmatrix}A_{ro}&0&*&0\\ *&A_{r\bar o}&*&*\\0&0&A_{\bar ro}&0\\0&0&*&A_{\bar r\bar o}\end{pmatrix}x+\begin{pmatrix}B_{ro}\\B_{r\bar o}\\0\\0\end{pmatrix}u,\quad y=(C_{ro}\ \ 0\ \ C_{\bar ro}\ \ 0)\,x\tag{8.20}$$
If $x_{\bar ro}(0)=0$, the input/output response is that of $\Sigma_{ro}$:
$$\dot x_{ro}=A_{ro}x_{ro}+B_{ro}u,\quad y=C_{ro}x_{ro}+Du\tag{8.21}$$
(Fig. 8.9b, p. 8-16).

**Example 8.5 (System and controller with observer feedback).** In coordinates $(x,\tilde x)$ the closed loop of Theorem 8.3 is (8.18) with $y=(C\ \ 0)\binom{x}{\tilde x}$. This is a Kalman decomposition with two subsystems: $\Sigma_{ro}$ (state $x$) and $\Sigma_{\bar ro}$ (state $\tilde x$, not reachable but observable). It is natural that $\tilde x$ is not reachable from $r$: reference changes should not create observer errors. The map $r\to y$ is $\dot x=(A-BK)x+Bk_fr,\ y=Cx$, the same as with full state feedback (p. 8-16, 8-17).

### 8.4 Kalman filtering (section marked with margin symbols, p. 8-17)
Observers are mainly used to estimate state from noisy measurements. A full treatment of stochastic systems is beyond the text. The section works mostly in discrete time and assumes basic knowledge of random variables and stochastic processes (p. 8-17).

**Discrete-time systems.**
$$x[k+1]=Ax[k]+Bu[k]+v[k],\qquad y[k]=Cx[k]+w[k]\tag{8.22}$$
$v,w$ are Gaussian white noise:
$$\mathbb E(v[k])=0,\ \mathbb E(w[k])=0,\ \mathbb E(v[k]v^T[j])=\begin{cases}0&k\ne j\\R_v&k=j\end{cases},\ \mathbb E(w[k]w^T[j])=\begin{cases}0&k\ne j\\R_w&k=j\end{cases},\ \mathbb E(v[k]w^T[j])=0\tag{8.23}$$
$R_v,R_w$ are covariance matrices of process disturbance and measurement noise ($R_v$ may be singular if disturbances do not affect all states). The initial state is Gaussian:
$$\mathbb E(x[0])=x_0,\quad \mathbb E\big((x[0]-x_0)(x[0]-x_0)^T\big)=P_0\tag{8.24}$$
Goal: an estimate $\hat x[k]$, given $\{y(\kappa):0\le\kappa\le k\}$, minimizing
$$P[k]=\mathbb E\big((x[k]-\hat x[k])(x[k]-\hat x[k])^T\big)\tag{8.25}$$
using an observer of the earlier form with time-varying gain:
$$\hat x[k+1]=A\hat x[k]+Bu[k]+L[k](y[k]-C\hat x[k])\tag{8.26}$$

**Theorem 8.4 (Kalman, 1961).** For the process (8.22) with (8.23), (8.24), the gain minimizing the mean square error is
$$L[k]=AP[k]C^T(R_w+CP[k]C^T)^{-1},$$
where
$$P[k+1]=(A-LC)P[k](A-LC)^T+R_v+LR_wL^T,\quad P[0]=\mathbb E\big((x[0]-x_0)(x[0]-x_0)^T\big)\tag{8.27}$$
(p. 8-18).

*Remarks (p. 8-18).*
- The filter is recursive: given $P[k]$ one computes how estimate and error change; old outputs need not be stored. It also supplies $P[k]$, showing how reliable the estimate is.
- The author states (without proof here) that the filter extracts the maximum information from the output data: the residual $e[k]=y[k]-C\hat x[k]$ has covariance $R_e(j,k)=W[k]\delta_{jk}$, with $\delta_{jk}=1$ if $j=k$ and $0$ otherwise. So the residual is white noise with no remaining dynamic information.
- It is versatile and works also when process, noise or disturbances are time-varying.
- For a time-invariant system, if $P[k]$ converges, the gain is constant: $L=APC^T(R_w+CPC^T)^{-1}$ with $P=APA^T+R_v-APC^T(R_w+CPC^T)^{-1}CPA^T$. The optimal gain depends on both noises, but not in a simple way. Like LQR for state feedback, it gives a systematic derivation of $L$ from the noise description. MATLAB `dlqe` solves the constant-gain case.

*Proof of Theorem 8.4 (p. 8-19).* By definition,
$$P[k+1]=\mathbb E\big((x[k+1]-\hat x[k+1])(\cdot)^T\big)=(A-LC)P[k](A-LC)^T+R_v+LR_wL^T$$
$$=AP[k]A^T+R_v-AP[k]C^TL^T-LCP[k]A^T+L(R_w+CP[k]C^T)L^T.$$
Let $R_\epsilon=R_w+CP[k]C^T$. Then
$$P[k+1]=AP[k]A^T+R_v-AP[k]C^TL^T-LCP[k]A^T+LR_\epsilon L^T$$
$$=AP[k]A^T+R_v+\big(L-AP[k]C^TR_\epsilon^{-1}\big)R_\epsilon\big(L-AP[k]C^TR_\epsilon^{-1}\big)^T-AP[k]C^TR_\epsilon^{-1}CP^T[k]A^T.$$
Only the middle term depends on $L$, so choose $L=AP[k]C^TR_\epsilon^{-1}$; this proves the theorem. (The source states the step to the minimum without comment; that the middle term is positive semidefinite and zero at this $L$ is the implicit reason. Added step.)

*Intuition note.* The gain weighs how uncertain the model prediction is ($P$) against how noisy the sensor is ($R_w$). Noisy sensors give small gains; an uncertain model gives large ones.

**Continuous-time systems.** Model:
$$\dot x=Ax+Bu+v,\ \mathbb E(v(s)v^T(t))=R_v\delta(t-s);\quad y=Cx+w,\ \mathbb E(w(s)w^T(t))=R_w\delta(t-s)\tag{8.28}$$
$\delta$ is the unit impulse function. The initial value is Gaussian with mean $x_0$ and covariance $P_0$. $v,w$ are zero-mean Gaussian (not necessarily time-invariant) with densities
$$\mathrm{pdf}(v)=\frac{1}{\sqrt[n]{2\pi}\sqrt{\det R_v}}e^{-\frac12v^TR_v^{-1}v},\quad \mathrm{pdf}(w)=\frac{1}{\sqrt[q]{2\pi}\sqrt{\det R_w}}e^{-\frac12w^TR_w^{-1}w}\tag{8.29}$$
(p. 8-19).

**Example 8.6 (Noisy sinusoidal disturbance).** Process $\dot x=x+u+v,\ y=x+w$. Model $v=z_1$ with
$$\frac{d}{dt}\binom{z_1}{z_2}=\begin{pmatrix}-0.01\omega_0&\omega_0\\-\omega_0&-0.01\omega_0\end{pmatrix}\binom{z_1}{z_2}+\binom{0}{\omega_0}e,$$
$e$ zero-mean white noise with covariance $r\delta(t)$. With $\xi=(x,z_1,z_2)$:
$$\dot\xi=\begin{pmatrix}1&1&0\\0&-0.01\omega_0&\omega_0\\0&-\omega_0&-0.01\omega_0\end{pmatrix}\xi+\begin{pmatrix}1\\0\\0\end{pmatrix}u+v,\quad y=(1\ 0\ 0)\xi+w,$$
with $v$ white Gaussian with covariance $R_v\delta(t)$, $R_v=\mathrm{diag}(0,0,\omega_0^2r)$. This is the standard form (8.28)–(8.29) (p. 8-19, 8-20).

**Theorem 8.5 (Kalman–Bucy, 1961).** The optimal estimator is the linear observer
$$\dot{\hat x}=A\hat x+Bu+L(y-C\hat x),\quad\hat x(0)=\mathbb E(x(0)),$$
with $L=PC^TR_w^{-1}$, $P=\mathbb E((x-\hat x)(x-\hat x)^T)$ satisfying
$$\frac{dP}{dt}=AP+PA^T-PC^TR_w^{-1}CP+R_v,\quad P(0)=\mathbb E\big((x(0)-x_0)(x(0)-x_0)^T\big)\tag{8.30}$$
All matrices may be time-varying. The author names the essential condition: the Riccati equation (8.30) must have a unique positive solution. For a time-invariant system, if $P(t)$ converges, $L=PC^TR_w^{-1}$ is constant and $P$ solves the algebraic Riccati equation
$$AP+PA^T-PC^TR_w^{-1}CP+R_v=0\tag{8.31}$$
(p. 8-20). These equations mirror the LQR Riccati equations (7.31), (7.33):
$$A\leftrightarrow A^T,\ B\leftrightarrow C^T,\ K\leftrightarrow L^T,\ P\leftrightarrow S,\ Q_x\leftrightarrow R_v,\ Q_u\leftrightarrow R_w\tag{8.32}$$
(compare (8.9)). MATLAB `kalman` computes the gains (p. 8-20).

**Example 8.7 (Vectored thrust aircraft).** Lateral dynamics with $z=(x,\theta,\dot x,\dot\theta)$:
$$A=\begin{pmatrix}0&0&1&0\\0&0&0&1\\0&-g&-c/m&0\\0&0&0&0\end{pmatrix},\ B=\begin{pmatrix}0\\0\\0\\r/J\end{pmatrix}.$$
(The source prints $C=(0\ 0\ 0\ 1)$ here; see Reading notes.) The system is augmented: $\dot\xi=A\xi+Bu+Fv,\ y=C\xi+w$, with $F$ the disturbance structure (including ignored nonlinearities). Choose $F=I$, independent disturbances with $R_{ii}=0.1$, $R_{ij}=0$ ($i\ne j$), and sensor noise $R_w=10^{-4}$. The resulting gain is $L=PC^TR_w^{-1}=(37.0,\,-46.9,\,185,\,-31.6)^T$, with $P$ from the algebraic Riccati equation. The estimator roughly tracks the state but has significant overshoot and substantial error in $\theta$ even after 2 s, which can hurt closed-loop performance (Fig. 8.10a). Adding a second measurement of $\theta$ (output $y=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix}\xi+\binom{w_1}{w_2}$, each $R_{w_i}=10^{-4}$) gives
$$L=\begin{pmatrix}32.6&-0.150\\-0.150&32.6\\32.7&-9.79\\-0.0033&31.6\end{pmatrix},$$
which the author says give good noise immunity and high performance (Fig. 8.10b) (p. 8-20, 8-21, 8-22).

**Linear quadratic Gaussian control (LQG).** Consider the stochastic system (8.28), Gaussian initial state, disturbances as in (8.29), and the cost
$$J=\min_u\mathbb E\Big(\int_0^{t_f}(x^TQ_xx+u^TQ_uu)\,dt+x^T(t_f)Q_fx(t_f)\Big)\tag{8.33}$$
where $u(t)$ may depend on all measurements $y(\tau)$, $0\le\tau\le t$. The optimal law is $u(t)=-K\hat x(t)$ with $K=SBQ_u^{-1}$ (as printed), $S$ the solution of the LQR Riccati equation (7.31), and $\hat x$ from the Kalman filter (Theorem 8.5). The problem separates into a deterministic control problem (LQR) and an optimal filtering problem; this is also called the separation principle (p. 8-22). The minimum cost is
$$\min J=x_0^TS(0)x_0+\mathrm{Tr}(S(0)P_0)+\int_0^{t_f}\mathrm{Tr}(R_vS)\,dt+\int_0^{t_f}\mathrm{Tr}(L^TQ_uLP)\,dt.$$
The first two terms are the cost of the initial mean and covariance, the third the cost of load disturbance, and the last the "cost of prediction" (p. 8-22). The models used have no direct term in the output; the author says the separation theorem does not hold in this case, because the nature of the disturbances is then influenced by the feedback (p. 8-23; the text does not say explicitly which case, presumably a direct term in the output).

### 8.5 State space controller design

**Two degree-of-freedom architecture (Fig. 8.11).** So far references entered through $k_f$. A more sophisticated controller has three parts: an observer, a state feedback, and a **trajectory generator** computing the desired state $x_d$ and a feedforward signal $u_{ff}$ from a task description $\mathcal T_d$. Ideally (no disturbances, no model error) $u_{ff}$ alone produces $x_d$. $\mathcal T_d$ may be a reference $r$ passed through linear systems, a list of waypoints (vehicle steering, robotics), or a transition between states optimizing a criterion (p. 8-23).

If there are no disturbances and the system rests at equilibrium with $\hat x=x$, a change in the reference changes $u_{ff}$ and $x_d$. The observer tracks perfectly, so $\hat x=x_d$ and $u_{fb}=K(x_d-\hat x)=0$. All action comes from the trajectory generator. Disturbances or modelling errors trigger the feedback correction (p. 8-24). Responses to references and disturbances are decoupled, hence "two degrees of freedom": disturbances are handled by observer and state feedback; commands by the trajectory generator (p. 8-24).

*Intuition note.* Feedforward does the planned work; feedback only fixes what the plan did not predict.

**Feedforward design and trajectory generation.** Nonlinear process: $\dot x=f(x,u),\ y=h(x,u)$ (8.34). A **feasible trajectory** is a pair $(x_d(t),u_{ff}(t))$ with $\dot x_d=f(x_d,u_{ff})$ and $r=h(x_d,u_{ff})$. Finding one is the trajectory generation problem. Given one, controllers $u=\alpha(x,x_d,u_{ff})$ can track it (p. 8-24). One may also minimize $\int_0^TL(x,u)\,dt+V(x(T))$ subject to $\dot x=f(x,u)$; this can be complex, but good numerical packages exist, including input and state constraints (p. 8-24).

**Example 8.8 (Vehicle steering, lane change).** Non-normalized model with rear-wheel reference point:
$$\dot x=v\cos\theta,\ \dot y=v\sin\theta,\ \dot\theta=\frac vb\tan\delta.$$
Given a path $x(t),y(t)$, solve
$$\dot x=v\cos\theta,\ \ \ddot x=\dot v\cos\theta-v\dot\theta\sin\theta,\ \ \dot y=v\sin\theta,\ \ \ddot y=\dot v\sin\theta+v\dot\theta\cos\theta,\ \ \dot\theta=(v/b)\tan\delta\tag{8.35}$$
Five equations in five unknowns ($\theta,\dot\theta,v,\dot v,\delta$) can be solved by trigonometry and linear algebra, so any path gives a feasible state trajectory (differential flatness) (p. 8-25). To go from $(x_0,y_0,\theta_0)$ to $(x_f,y_f,\theta_f)$ in time $T$, the path must satisfy
$$x(0)=x_0,\ y(0)=y_0,\ \dot x(0)\sin\theta_0-\dot y(0)\cos\theta_0=0,\ \dot y(0)\sin\theta_0+\dot x(0)\cos\theta_0=v_0,$$
and the same at $T$ with $x_f,y_f,\theta_f,v_f$ (8.36) (p. 8-26). Choose cubics $x_d=\alpha_0+\alpha_1t+\alpha_2t^2+\alpha_3t^3$, $y_d=\beta_0+\cdots+\beta_3t^3$. Substitution gives linear equations for $\alpha_i,\beta_i$; (8.35) then yields $\theta_d,v_d,\delta_d$. Fig. 8.12 (change lanes over 90 m in 6 s) uses a set of higher-order equations that also set initial and final steering angle to zero. The feedforward steering input is nonzero, so the turn can be executed when there are no errors (p. 8-25, 8-26).

**Differential flatness.** System (8.34) is differentially flat if there is a flat output $z$ with
$$x=\beta(z,\dot z,\dots,z^{(m)}),\quad u=\gamma(z,\dot z,\dots,z^{(m)})\tag{8.37}$$
The number of flat outputs always equals the number of inputs. The steering model is flat with the rear-wheel position as flat output (p. 8-26). For a reachable linear system in reachable canonical form (7.6): $z_1=z_n^{(n-1)},\ z_2=z_n^{(n-2)},\dots,z_{n-1}=\dot z_n,\ u=z_n^{(n)}+a_1z_n^{(n-1)}+\cdots+a_nz_n$, so $z_n$ is a flat output. Since any reachable system can be put in this form, every reachable linear system is differentially flat. Feasible trajectories need no integration of differential equations, so they can be computed efficiently (p. 8-26).

**Disturbance modeling and state augmentation.** Load disturbances may be unknown constants, drifts, sinusoids, or stochastic signals. Model them by differential equations and augment the state (p. 8-27).

**Example 8.9 (Integral action by state augmentation).** A constant unknown disturbance $z$ acts at the input; model $\dot z=0$:
$$\frac d{dt}\binom xz=\begin{pmatrix}A&B\\0&0\end{pmatrix}\binom xz+\binom B0u,\quad y=(C\ \ 0)\binom xz.$$
$z$ is not reachable from $u$, but since it enters at the input it can be attenuated by $u=-K\hat x-\hat z$ (8.38). The observer is $\dot{\hat x}=A\hat x+B\hat z+Bu+L_x(y-C\hat x)$, $\dot{\hat z}=L_z(y-C\hat x)$. Integrating the last equation (and inserting in 8.38):
$$u=-K\hat x-L_z\int_0^t(y(\tau)-C\hat x(\tau))\,d\tau,$$
a state feedback with integral action; the integral action arises from estimating a disturbance state (p. 8-27).

**Feedback design and gain scheduling.** Assume $(x_d,u_{ff})$ is feasible. Let $\xi=x-x_d$, $u_{fb}=u-u_{ff}$. Then
$$\dot\xi=f(x,u)-f(x_d,u_{ff})=f(\xi+x_d,v+u_{ff})-f(x_d,u_{ff})=:F(\xi,v,x_d(t),u_{ff}(t))$$
Linearize for small $\xi$: $\dot\xi\approx A(t)\xi+B(t)v$, $h\approx C(t)x$, with $A=\partial F/\partial\xi$, $B=\partial F/\partial v$, $C=\partial h/\partial\xi$ evaluated at $(x_d(t),u_{ff}(t))$ (p. 8-28). This is time-varying. $\xi$ corresponds to $-e$ in Fig. 8.11. LQR gives $K(t)=Q_u^{-1}(t)B^T(t)S(t)$ from the Riccati differential equation (7.31), and the Kalman gain is $L(t)=P(t)C^T(t)R_w^{-1}(t)$, with $P$ from (8.30) (p. 8-28).

If $x_d,u_{ff}$ are constant or slowly varying and $A,B,C$ depend only on $x_d$, design $K(x_d)$ for each $x_d$ and use $u_{fb}=-K(x_d)\xi$. The controller is $u=-K(x_d)(x-x_d)+u_{ff}$: a **gain scheduled** linear controller with feedforward $u_{ff}$ (p. 8-28).

**Example 8.10 (Steering control with velocity scheduling).** Track a straight line at lateral position $y_r$ with speed $v_r$: $x_d=(v_rt,y_r,0)$, $u_{ff}=(v_r,0)$, which is not an equilibrium but satisfies the equations of motion. Linearizing:
$$A_d=\begin{pmatrix}0&0&-\sin\theta\\0&0&\cos\theta\\0&0&0\end{pmatrix}_{(x_d,u_{ff})}=\begin{pmatrix}0&0&0\\0&0&1\\0&0&0\end{pmatrix},\quad B_d=\begin{pmatrix}1&0\\0&0\\0&v_r/l\end{pmatrix}.$$
Error dynamics with $e=x-x_d$, $w=u-u_{ff}$: $\dot e_x=w_1,\ \dot e_y=e_\theta,\ \dot e_\theta=\frac{v_r}{l}w_2$. The longitudinal state $e_x$ decouples from $(e_y,e_\theta)$. To place the longitudinal eigenvalue at $\lambda_1$ and the lateral eigenvalues at the roots of $s^2+a_1s+a_2$, the text sets $w_1=-\lambda_1e_x$, $w_2=\frac{l}{v_r}(a_1e_y+a_2e_\theta)$ (see Reading notes on signs). The gain $l/v_r$ depends on $v_r$, which makes the controller gain scheduled. In original coordinates:
$$\binom v\delta=-\underbrace{\begin{pmatrix}\lambda_1&0&0\\0&\frac{a_1l}{v_r}&\frac{a_2l}{v_r}\end{pmatrix}}_{K_d}\underbrace{\begin{pmatrix}x-v_rt\\y-y_r\\\theta\end{pmatrix}}_{e}+\underbrace{\begin{pmatrix}v_r\\0\end{pmatrix}}_{u_{ff}}.$$
At low speed the steering gains are high; at high speed they shrink. The gains go to infinity as $v_r\to0$, reflecting that the system is not reachable at standstill. Fig. 8.13b: step responses at three speeds have the same rate, because every scheduled controller sets the same closed-loop eigenvalues (p. 8-28, 8-29).

**Nonlinear estimation.** For nonlinear processes use the full nonlinear dynamics for prediction plus a linear correction:
$$\dot{\hat x}=f(\hat x,u)+L(\hat x)(y-h(\hat x)).$$
$L(\hat x)$ is the observer gain from linearizing about the current estimate. This is the **extended Kalman filter**, which has proved very effective for estimating nonlinear states. Trajectory generation, tracking and nonlinear estimation together give state space control of nonlinear systems. The internal model principle still applies (the observer holds a model of plant and environment) (p. 8-30).

**Computer implementation.** Controllers can be built from analog parts, but most are computers: sample sensors via an A/D converter, compute, output via a D/A converter, periodically (Fig. 8.14). For $\dot{\hat x}=A\hat x+Bu+L(y-C\hat x)$, $u=-K\hat x+k_fr$: $u$ needs only additions and multiplications. Approximate the derivative by a difference over sampling period $h=t_{k+1}-t_k$:
$$\hat x(t_{k+1})=\hat x(t_k)+h\big(A\hat x(t_k)+Bu(t_k)+L(y(t_k)-C\hat x(t_k))\big)\tag{8.39}$$
The pseudocode loop: read $r$ and $y$; get $(x_d,u_{ff})$ from the trajectory generator; $u=K(x_d-\hat x)+u_{ff}$; write $u$; then update $\hat x$. The state update comes after the output is set to minimize delay between input and output. Choosing $h$ "requires some care". Exact equations exist if $u$ is constant between samples (ref. ÅW97). Practical issues: filter measured signals so little content lies above $f_s/2$ (the Nyquist frequency, $f_s=1/h$) to avoid aliasing; protect against integrator windup when the actuator saturates (Chapter 11); avoid disturbances when parameters change (p. 8-30, 8-31).

### 8.6 Further reading (p. 8-32)
Observability is due to Kalman [Kal61b]. The Kalman filter appeared in Kalman [Kal61a] (discrete time) and Kalman–Bucy [KB61] (continuous time). Kalman conjectured that output feedback can be obtained by combining state feedback with a Kalman filter (the epigraph); this "separation theorem" is "mathematically subtle". Earlier proof attempts (Josep and Tou; Gunckel and Franklin) are named, and a rigorous proof was given by Georgiou and Lindquist in 2013. The combination is LQG theory. Robust control solutions have a similar structure with different gain computation. Two-degree-of-freedom systems were emphasized by Horowitz. Ito proposed in 1970 that human motion control combines feedback and feedforward. Differentially flat systems were first studied by Fliess et al.

## Toy example (ours, not from the text)
Take $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $B=\begin{pmatrix}0\\1\end{pmatrix}$, $C=(1\ \ 0)$, $n=2$.

1. Observability: $CA=(1\ 0)\begin{pmatrix}0&1\\0&0\end{pmatrix}=(0\ \ 1)$. So $W_o=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, rank 2, observable.
2. Observer gain: $A-LC=\begin{pmatrix}-l_1&1\\-l_2&0\end{pmatrix}$, so $\det(sI-A+LC)=s^2+l_1s+l_2$. Choose target $s^2+2s+1$ ($\omega_o=1,\zeta_o=1$): $L=(2,1)^T$. Eigenvalues: $-1$ (double).
3. Error step (with $u=0$): true $x(0)=(1,0)^T$, estimate $\hat x(0)=(0,0)^T$, so $\tilde x(0)=(1,0)^T$. Then $\dot{\tilde x}(0)=(A-LC)\tilde x(0)=\begin{pmatrix}-2&1\\-1&0\end{pmatrix}\binom10=\binom{-2}{-1}$. Euler step $h=0.1$: $\tilde x(0.1)\approx(1,0)+0.1(-2,-1)=(0.8,-0.1)$. The first error component shrinks, as the eigenvalues predict.
4. Separation: choose $K=(1\ \ 1)$. Then $A-BK=\begin{pmatrix}0&1\\-1&-1\end{pmatrix}$, $\det(sI-A+BK)=s(s+1)+1=s^2+s+1$. By (8.18) the closed-loop polynomial is $(s^2+s+1)(s^2+2s+1)$, with four eigenvalues: $-0.5\pm0.866i$ and $-1,-1$. Changing $L$ alters only the second factor.

## Concepts
- [[observability]] — the state can be determined from $y,u$ on $[0,T]$ for every $T>0$; for linear systems, $W_o$ has full row rank (p. 8-2, 8-3) (new)
- [[observability-matrix]] — $W_o=(C;CA;\dots;CA^{n-1})$ (p. 8-3) (new)
- [[observer (state estimator)]] — model copy plus output-error correction $L(y-C\hat x)$ so that $\hat x\to x$ (p. 8-7)
- [[duality]] — $A\leftrightarrow A^T,B\leftrightarrow C^T,K\leftrightarrow L^T,W_r\leftrightarrow W_o^T$; observer design mirrors state feedback (p. 8-7)
- [[state feedback / pole placement]] — here applied to $\hat x$: $u=-K\hat x+k_fr$ (p. 8-12)
- [[separation principle (LQG)]] — in this unit: eigenvalue assignment for output feedback splits into separate designs of $K$ and $L$; also LQG splits into LQR plus Kalman filter (p. 8-13, 8-22)
- [[internal model principle]] — the controller contains a model of the process (and its environment) (p. 8-13) (new)
- [[Kalman filter]] — mean-square-optimal observer under Gaussian white noise (p. 8-18, 8-20)
- [[Kalman gain]] — $L[k]=AP[k]C^T(R_w+CP[k]C^T)^{-1}$ (discrete); $L=PC^TR_w^{-1}$ (continuous) (p. 8-18, 8-20)
- [[Riccati equation]] — equation (8.30)/(8.31) for the error covariance; dual to the LQR one (p. 8-20) (new)
- [[LQR]] — optimal state feedback for quadratic cost, used with the filter in LQG (p. 8-22)
- [[Kalman decomposition]] — splitting a linear system into reachable/observable parts $\Sigma_{ro},\Sigma_{r\bar o},\Sigma_{\bar ro},\Sigma_{\bar r\bar o}$ (p. 8-15) (new)
- [[two-degree-of-freedom controller]] — observer + state feedback + trajectory generator (feedforward); reference and disturbance responses decoupled (p. 8-23, 8-24) (new)
- [[feedforward]] — here $u_{ff}$ from a trajectory generator (p. 8-23)
- [[differential flatness]] — state and input are functions of a flat output and finitely many derivatives; trajectories need no integration (p. 8-26) (new)
- [[gain scheduling]] — feedback gains $K(x_d)$ varying with the operating point (p. 8-28) (new)
- [[extended Kalman filter]] — nonlinear prediction plus linearized gain $L(\hat x)$ (p. 8-30) (new)
- [[integral action]] — obtained here by estimating a constant disturbance state (p. 8-27)
- [[linearization]] — error dynamics linearized about the desired trajectory (p. 8-28)

## Canonical instances
- [[compartment-model]] — two-compartment drug model; observable if $k_1\neq0$ from plasma measurement (the condition is called essential); observer gain computed (p. 8-3, 8-8)
- [[vehicle-steering]] — observer (Ex. 8.3), output feedback (Ex. 8.4), lane-change trajectory (Ex. 8.8), velocity-scheduled steering (Ex. 8.10) (p. 8-10, 8-14, 8-25, 8-28)
- [[unobservable-subtraction-system]] — two identical subsystems with combined outputs (Fig. 8.2) (p. 8-4)
- [[vectored-thrust-aircraft]] — Kalman filter design, improved by adding a measurement (p. 8-20, 8-21)
- [[noisy-sinusoidal-disturbance]] — disturbance modeled by a noise-driven oscillator and state augmentation (p. 8-19)
- [[integral-action-by-augmentation]] — constant disturbance estimated as a state (p. 8-27)

## Bridges (candidates)
- [same-math] Observer design by eigenvalue assignment ↔ state feedback pole placement (ch. 7): the same problem with $A,B,K$ replaced by $A^T,C^T,L^T$ (p. 8-7).
- [same-math] Kalman–Bucy Riccati equation ↔ LQR Riccati equation: equivalences (8.32) map one into the other (p. 8-20).
- [structural-analogy] Observer's "prediction + correction by error" ↔ model-based learning: a model prediction is corrected by prediction error, as in reward prediction error updates.
- [structural-analogy] Internal model principle ↔ good regulator theorem: the controller contains a model of what it controls.
- [structural-analogy] Feedforward + feedback split (two degrees of freedom) ↔ motor control: Ito's hypothesis that human motion control combines feedforward and feedback (p. 8-32).

## Questions this raises
- What happens to separation when the model used by the observer is wrong or the plant is nonlinear? (The chapter defers robustness to §14.5.)
- How should $R_v$ and $R_w$ be chosen in practice when the noise statistics are not known?
- Why does the separation principle lose validity with a direct term in the output (p. 8-23), and what does the more complicated solution look like?
- How does the choice of observer speed trade off against noise sensitivity in a given application (p. 8-11)?

## Exercises worth doing
- Ex. 8.1 (p. 8-32) — observability matrix transforms as $\widetilde W_o=W_oT^{-1}$, so observability does not depend on coordinates — easy
- Ex. 8.2 (p. 8-32) — prove that the system of Fig. 8.2 is unobservable — easy
- Ex. 8.6 (p. 8-33) — observer design by eigenvalue assignment with $\omega_o=10,\zeta_o=0.6$ — easy
- Ex. 8.8 (p. 8-33) — observability and observer for Teorell's five-compartment model — medium
- Ex. 8.10 (p. 8-33) — build a Kalman decomposition by diagonalizing — medium
- Ex. 8.11 (p. 8-34) — Kalman filter for a scalar first-order system and its large-$t$ behaviour — medium
- Ex. 8.12 (p. 8-34) — time-varying versus constant gain for vertical alignment — hard

## Reading notes
- Page labels give no printed number, but the page images show printed numbers "8-1" … "8-34". Offset: printed 8-N = pdf − 264. Citations use (p. 8-N).
- Fig. 8.2 caption says the subsystem outputs "add together", while the text and block diagram have the outputs subtracted (a $-1$ block). I followed the diagram and text.
- Theorem 8.4: the printed initial condition $P[0]=\mathbb E((x[0]=x_0)(x[0]-x_0)^T)$ has "=" where the image should read "−" (compare 8.24). The text after the theorem prints the constant gain as $L=APC^T(R_w+CPC^T)$ without the inverse exponent; the theorem itself has $^{-1}$.
- Example 8.7: the text says position $x$ is measured, but the image prints $C=(0\ 0\ 0\ 1)$ (selects $\dot\theta$). $(1\ 0\ 0\ 0)$ would match the description; I could not confirm which was intended.
- Example 8.10 (my own check, not from the source): as printed, $w_2=\frac l{v_r}(a_1e_y+a_2e_\theta)$ lacks the minus sign shown in $K_d$. With the minus sign, $\dot e_y=e_\theta$, $\dot e_\theta=-a_1e_y-a_2e_\theta$ has polynomial $s^2+a_2s+a_1$, so $a_1,a_2$ appear swapped relative to the stated $s^2+a_1s+a_2$.
- The LQG gain is printed as $K=SBQ_u^{-1}$ (p. 8-22), while p. 8-28 prints $K(t)=Q_u^{-1}(t)B^T(t)S(t)$; the two orderings are not the same expression as typed.
- Pseudocode (p. 8-31) updates `xhat` using `x` (not `xhat`) inside the update; likely a typo, since $x$ is unmeasured.
- Text-layer extraction garbles overbars in subscripts ($r\bar o$ etc.) and matrices; I checked them against the images. A road-sign-like symbol appears in the margin beside the proof of Theorem 8.1 (p. 8-3), the Kalman's Decomposition heading (p. 8-15), the §8.4 heading (two symbols, p. 8-17) and Exercise 8.7 (p. 8-33); these pages do not say what it means.
