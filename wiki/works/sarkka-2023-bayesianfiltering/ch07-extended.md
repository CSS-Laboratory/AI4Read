---
id: sarkka-2023-bayesianfiltering/ch07-extended
work: sarkka-2023-bayesianfiltering
unit: "7 Extended Kalman Filtering"
pages: 108-130
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Extended Kalman Filtering

## L0 — One line
The extended Kalman filter (EKF) handles non-linear models by replacing the model functions with Taylor-series approximations around the current mean, so that the Kalman filter equations can be reused with Gaussian approximations.

## L1 — The gist (≤ 120 words)
Passing a Gaussian through a non-linear function gives a non-Gaussian result, but filtering distributions can often be approximated by Gaussians. This chapter does so using Taylor expansions of the dynamic and measurement functions. The first-order EKF linearises both functions with Jacobians and reuses the Kalman equations. A second-order EKF adds Hessian terms. The iterated EKF (IEKF) re-linearises at the updated mean and can be interpreted as a Gauss–Newton search (an iterative least-squares method) for the MAP (most probable state) estimate. The authors credit the EKF with relative simplicity compared with its performance, but say it will not work with considerable non-linearities and needs differentiable models and Gaussian noise. Automatic differentiation can sometimes avoid hand-derived Jacobians. Pendulum and coordinated-turn examples illustrate the methods.

**Prerequisites:** Jacobian and Hessian matrices; Gaussian joint/conditional formulas; the linear Kalman filter (prediction, update, gain); Bayes' rule and MAP estimation; basic least-squares.

## L2 — Key ideas (5–10 bullets)
- A Gaussian input pushed through a non-linear function is non-Gaussian, so a Gaussian is fitted using only the mean and covariance from a Taylor expansion (p. 108–110).
- Linearising $g$ at the mean gives mean $g(\mathbf m)$ and covariance $\mathbf G_x\mathbf P\mathbf G_x^\top$ (+ noise); this is the basis of the first-order additive-noise EKF equations (Alg. 7.1, p. 110–111).
- The EKF is the Kalman filter with $\mathbf f,\mathbf h$ in the mean and Jacobians in the covariance and gain computations (Alg. 7.4, p. 113–114).
- It is derived by repeating the Kalman derivation, replacing each exact Gaussian step by the linearised joint distribution (p. 114–115).
- Strength: relative simplicity compared with its performance. Limits: weak for strong non-linearity, Gaussian noise only, differentiability required, error-prone Jacobians (p. 116–117).
- The second-order EKF keeps Hessian terms; still higher orders cost much more and may be numerically unstable, so iteration is preferred (p. 119–120).
- The IEKF re-linearises inside the update step. It can be interpreted as a Gauss–Newton method for the MAP estimate, and the iterations can help in situations where the measurement likelihood is informative compared with the predicted density (p. 121–124).
- Levenberg–Marquardt, line search and quasi-Newton variants are extensions of Gauss–Newton, and other optimisation methods often perform better than plain Gauss–Newton; automatic differentiation can sometimes avoid manual derivative work (p. 126–127).

## L3 — Walkthrough

### Chapter intro (p. 108)
When dynamic or measurement models are non-linear, the Kalman filter does not apply, but the filtering distributions can often be approximated by Gaussians (p. 108). The chapter covers the first-order EKF ("the classical and probably the most widely used non-linear filter"), higher-order EKFs, and the iterated EKF (p. 108).

### 7.1 Taylor series approximation of a non-linear transform (p. 108–113)
**Set-up.** $\mathbf x\sim\mathrm N(\mathbf m,\mathbf P)$, $\mathbf y=\mathbf g(\mathbf x)$, $\mathbf x\in\mathbb R^n$, $\mathbf y\in\mathbb R^m$, $\mathbf g$ general non-linear (7.1). The exact density, for invertible $\mathbf g$, is
$$p(\mathbf y)=|\mathbf J(\mathbf y)|\,\mathrm N(\mathbf g^{-1}(\mathbf y)\mid \mathbf m,\mathbf P)\tag{7.2}$$
with $|\mathbf J(\mathbf y)|$ the Jacobian determinant of $\mathbf g^{-1}$. It is non-Gaussian for all but linear $\mathbf g$, so it cannot generally be handled directly (p. 108).

**Expansion.** Write $\mathbf x=\mathbf m+\delta\mathbf x$, $\delta\mathbf x\sim\mathrm N(\mathbf 0,\mathbf P)$. If $\mathbf g$ is sufficiently differentiable (p. 109):
$$\mathbf g(\mathbf m+\delta\mathbf x)\approx \mathbf g(\mathbf m)+\mathbf G_x(\mathbf m)\delta\mathbf x+\sum_i\tfrac12\,\delta\mathbf x^\top\mathbf G_{xx}^{(i)}(\mathbf m)\,\delta\mathbf x\,\mathbf e_i+\cdots\tag{7.3}$$
$$[\mathbf G_x(\mathbf m)]_{j,j'}=\frac{\partial g_j(\mathbf x)}{\partial x_{j'}}\Big|_{\mathbf x=\mathbf m},\qquad [\mathbf G^{(i)}_{xx}(\mathbf m)]_{j,j'}=\frac{\partial^2 g_i(\mathbf x)}{\partial x_j\,\partial x_{j'}}\Big|_{\mathbf x=\mathbf m}\tag{7.4, 7.5}$$
$\mathbf G_x$ is the $m\times n$ Jacobian. $\mathbf G_{xx}^{(i)}$ is the $n\times n$ Hessian of component $g_i$. $\mathbf e_i$ is the unit vector along axis $i$ (p. 109).

**Linear approximation.** Keep two terms: $\mathbf g(\mathbf x)\simeq\mathbf g(\mathbf m)+\mathbf G_x(\mathbf m)\delta\mathbf x$ (7.6). Then
$$\mathrm E[\mathbf g(\mathbf x)]\simeq \mathrm E[\mathbf g(\mathbf m)+\mathbf G_x\delta\mathbf x]=\mathbf g(\mathbf m)+\mathbf G_x\mathrm E[\delta\mathbf x]=\mathbf g(\mathbf m)\tag{7.7}$$
(p. 109). The covariance:
$$\begin{aligned}\mathrm{E}\big[(\mathbf g-\mathrm E[\mathbf g])(\mathbf g-\mathrm E[\mathbf g])^\top\big]&\simeq \mathrm E\big[(\mathbf g(\mathbf x)-\mathbf g(\mathbf m))(\mathbf g(\mathbf x)-\mathbf g(\mathbf m))^\top\big]\\&\simeq \mathrm E\big[(\mathbf G_x\delta\mathbf x)(\mathbf G_x\delta\mathbf x)^\top\big]=\mathbf G_x\,\mathrm E[\delta\mathbf x\delta\mathbf x^\top]\,\mathbf G_x^\top=\mathbf G_x\mathbf P\mathbf G_x^\top\end{aligned}\tag{7.8}$$
(p. 110).

**Joint with $\mathbf x$.** Use the augmented map $\tilde{\mathbf g}(\mathbf x)=(\mathbf x;\ \mathbf g(\mathbf x))$ (7.9). Then
$$\mathrm E[\tilde{\mathbf g}]\simeq\begin{pmatrix}\mathbf m\\ \mathbf g(\mathbf m)\end{pmatrix},\quad \mathrm{Cov}[\tilde{\mathbf g}]\simeq\begin{pmatrix}\mathbf I\\ \mathbf G_x\end{pmatrix}\mathbf P\begin{pmatrix}\mathbf I\\ \mathbf G_x\end{pmatrix}^{\!\top}=\begin{pmatrix}\mathbf P&\mathbf P\mathbf G_x^\top\\ \mathbf G_x\mathbf P&\mathbf G_x\mathbf P\mathbf G_x^\top\end{pmatrix}\tag{7.10}$$
(p. 110).

**Additive noise (7.11):** $\mathbf y=\mathbf g(\mathbf x)+\mathbf q$, $\mathbf q\sim\mathrm N(\mathbf 0,\mathbf Q)$ independent of $\mathbf x$. Then $\mathbf Q$ is added to the lower-right block (p. 110).

**Algorithm 7.1 (linear approximation, additive).** (p. 110–111)
$$\begin{pmatrix}\mathbf x\\ \mathbf y\end{pmatrix}\sim\mathrm N\!\left(\begin{pmatrix}\mathbf m\\ \boldsymbol\mu_L\end{pmatrix},\begin{pmatrix}\mathbf P&\mathbf C_L\\ \mathbf C_L^\top&\mathbf S_L\end{pmatrix}\right)\tag{7.12}$$
$$\boldsymbol\mu_L=\mathbf g(\mathbf m),\quad \mathbf S_L=\mathbf G_x(\mathbf m)\mathbf P\mathbf G_x^\top(\mathbf m)+\mathbf Q,\quad \mathbf C_L=\mathbf P\mathbf G_x^\top(\mathbf m)\tag{7.13}$$
with $\mathbf G_x$ as in (7.14), the same Jacobian as (7.4).

**Non-additive noise (7.15):** $\mathbf y=\mathbf g(\mathbf x,\mathbf q)$, $\mathbf x,\mathbf q$ independent. Substitute $(\mathbf x,\mathbf q)$ for $\mathbf x$ in (7.10), with joint Jacobian $\mathbf G_{x,q}=(\mathbf G_x\ \ \mathbf G_q)$ evaluated at $\mathbf x=\mathbf m,\mathbf q=\mathbf 0$. This gives mean $\mathbf g(\mathbf m,\mathbf 0)$ and the lower-right covariance block $\mathbf G_x\mathbf P\mathbf G_x^\top+\mathbf G_q\mathbf Q\mathbf G_q^\top$ (7.16) (p. 111).

**Algorithm 7.2 (linear, non-additive).** Same form as (7.17), with (p. 112)
$$\boldsymbol\mu_L=\mathbf g(\mathbf m,\mathbf 0),\quad \mathbf S_L=\mathbf G_x\mathbf P\mathbf G_x^\top+\mathbf G_q\mathbf Q\mathbf G_q^\top,\quad \mathbf C_L=\mathbf P\mathbf G_x^\top\tag{7.18}$$
Jacobians $[\mathbf G_x]_{j,j'}=\partial g_j/\partial x_{j'}$ (7.19) and $[\mathbf G_q]_{j,j'}=\partial g_j/\partial q_{j'}$ (7.20), both at $\mathbf x=\mathbf m,\mathbf q=\mathbf 0$.

**Algorithm 7.3 (quadratic, additive).** The second-order terms are kept. The joint is Gaussian as in (7.21) with (p. 112–113)
$$\begin{aligned}\boldsymbol\mu_Q&=\mathbf g(\mathbf m)+\tfrac12\sum_i\mathbf e_i\,\mathrm{tr}\{\mathbf G^{(i)}_{xx}(\mathbf m)\mathbf P\},\\ \mathbf S_Q&=\mathbf G_x\mathbf P\mathbf G_x^\top+\tfrac12\sum_{i,i'}\mathbf e_i\mathbf e_{i'}^\top\mathrm{tr}\{\mathbf G^{(i)}_{xx}\mathbf P\,\mathbf G^{(i')}_{xx}\mathbf P\}+\mathbf Q,\\ \mathbf C_Q&=\mathbf P\mathbf G_x^\top\end{aligned}\tag{7.22}$$

*Intuition note.* Replacing a curved function by its tangent at the mean gives a mean and covariance that are easy to compute. Because this is a local linear approximation, the authors warn it will not work with considerable non-linearities (p. 116). The second-order version adds a curvature correction to the mean and spread.

### 7.2 Extended Kalman filter (p. 113–119)
**Model (additive noise):** $\mathbf x_k=\mathbf f(\mathbf x_{k-1})+\mathbf q_{k-1}$, $\mathbf y_k=\mathbf h(\mathbf x_k)+\mathbf r_k$ (7.24), with $\mathbf q_{k-1}\sim\mathrm N(\mathbf 0,\mathbf Q_{k-1})$, $\mathbf r_k\sim\mathrm N(\mathbf 0,\mathbf R_k)$. The EKF uses (or assumes) $p(\mathbf x_k\mid\mathbf y_{1:k})\simeq\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k)$ (7.25) (p. 113).

**Algorithm 7.4 (EKF I).** (p. 113–114)
Prediction:
$$\mathbf m_k^-=\mathbf f(\mathbf m_{k-1}),\qquad \mathbf P_k^-=\mathbf F_x(\mathbf m_{k-1})\mathbf P_{k-1}\mathbf F_x^\top(\mathbf m_{k-1})+\mathbf Q_{k-1}\tag{7.26}$$
Update:
$$\begin{aligned}\mathbf v_k&=\mathbf y_k-\mathbf h(\mathbf m_k^-),\\ \mathbf S_k&=\mathbf H_x(\mathbf m_k^-)\mathbf P_k^-\mathbf H_x^\top(\mathbf m_k^-)+\mathbf R_k,\\ \mathbf K_k&=\mathbf P_k^-\mathbf H_x^\top(\mathbf m_k^-)\mathbf S_k^{-1},\\ \mathbf m_k&=\mathbf m_k^-+\mathbf K_k\mathbf v_k,\\ \mathbf P_k&=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^\top\end{aligned}\tag{7.27}$$
Jacobians: $[\mathbf F_x(\mathbf m)]_{j,j'}=\partial f_j/\partial x_{j'}|_{\mathbf x=\mathbf m}$ (7.28), $[\mathbf H_x(\mathbf m)]_{j,j'}=\partial h_j/\partial x_{j'}|_{\mathbf x=\mathbf m}$ (7.29). Shapes: $\mathbf F_x$ is $n\times n$, $\mathbf H_x$ is $m\times n$, $\mathbf S_k$ is $m\times m$, $\mathbf K_k$ is $n\times m$.

**Derivation** (repeat the Kalman derivation of Section 6.3 with Taylor steps) (p. 114–115):
1. Apply Alg. 7.1 to $\mathbf f(\mathbf x_{k-1})+\mathbf q_{k-1}$ (7.30). This gives $p(\mathbf x_{k-1},\mathbf x_k\mid\mathbf y_{1:k-1})\simeq\mathrm N(\mathbf m',\mathbf P')$ (7.31) with
$\mathbf m'=\begin{pmatrix}\mathbf m_{k-1}\\ \mathbf f(\mathbf m_{k-1})\end{pmatrix}$, $\mathbf P'=\begin{pmatrix}\mathbf P_{k-1}&\mathbf P_{k-1}\mathbf F_x^\top\\ \mathbf F_x\mathbf P_{k-1}&\mathbf F_x\mathbf P_{k-1}\mathbf F_x^\top+\mathbf Q_{k-1}\end{pmatrix}$ (7.32), $\mathbf F_x$ at $\mathbf m_{k-1}$. The marginal of $\mathbf x_k$ then has mean and covariance (7.33), identical to (7.26).
2. Apply Alg. 7.1 to $\mathbf h(\mathbf x_k)+\mathbf r_k$ (7.34). Then $p(\mathbf x_k,\mathbf y_k\mid\mathbf y_{1:k-1})\simeq\mathrm N(\mathbf m'',\mathbf P'')$ (7.35) with $\mathbf m''=(\mathbf m_k^-;\ \mathbf h(\mathbf m_k^-))$, $\mathbf P''=\begin{pmatrix}\mathbf P_k^-&\mathbf P_k^-\mathbf H_x^\top\\ \mathbf H_x\mathbf P_k^-&\mathbf H_x\mathbf P_k^-\mathbf H_x^\top+\mathbf R_k\end{pmatrix}$ (7.36), $\mathbf H_x$ at $\mathbf m_k^-$.
3. By Lemma A.3, $p(\mathbf x_k\mid\mathbf y_k,\mathbf y_{1:k-1})\simeq\mathrm N(\mathbf m_k,\mathbf P_k)$ (7.37) with
$\mathbf m_k=\mathbf m_k^-+\mathbf P_k^-\mathbf H_x^\top(\mathbf H_x\mathbf P_k^-\mathbf H_x^\top+\mathbf R_k)^{-1}[\mathbf y_k-\mathbf h(\mathbf m_k^-)]$, $\mathbf P_k=\mathbf P_k^--\mathbf P_k^-\mathbf H_x^\top(\mathbf H_x\mathbf P_k^-\mathbf H_x^\top+\mathbf R_k)^{-1}\mathbf H_x\mathbf P_k^-$ (7.38).

**Non-additive model (7.39):** $\mathbf x_k=\mathbf f(\mathbf x_{k-1},\mathbf q_{k-1})$, $\mathbf y_k=\mathbf h(\mathbf x_k,\mathbf r_k)$. **Algorithm 7.5 (EKF II)** (p. 115–116), obtained by using Alg. 7.2 instead of 7.1:
Prediction: $\mathbf m_k^-=\mathbf f(\mathbf m_{k-1},\mathbf 0)$; $\mathbf P_k^-=\mathbf F_x\mathbf P_{k-1}\mathbf F_x^\top+\mathbf F_q\mathbf Q_{k-1}\mathbf F_q^\top$ (7.40).
Update: $\mathbf v_k=\mathbf y_k-\mathbf h(\mathbf m_k^-,\mathbf 0)$; $\mathbf S_k=\mathbf H_x\mathbf P_k^-\mathbf H_x^\top+\mathbf H_r\mathbf R_k\mathbf H_r^\top$; $\mathbf K_k=\mathbf P_k^-\mathbf H_x^\top\mathbf S_k^{-1}$; $\mathbf m_k=\mathbf m_k^-+\mathbf K_k\mathbf v_k$; $\mathbf P_k=\mathbf P_k^--\mathbf K_k\mathbf S_k\mathbf K_k^\top$ (7.41). The Jacobians $\mathbf F_x,\mathbf F_q,\mathbf H_x,\mathbf H_r$ (7.42–7.45) are taken w.r.t. state and noise at the state mean and noise $\mathbf 0$.

**Pros and cons** (authors' assessment, p. 116–117). The advantage is relative simplicity compared with performance; linearisation is a familiar engineering tool. Disadvantages: (i) as a local linear approximation it will not work with considerable non-linearities; (ii) only Gaussian noise is allowed, so no discrete-valued variables, hierarchical models or significantly non-Gaussian models; (iii) $\mathbf f,\mathbf h$ must be differentiable, and sometimes the Jacobians cannot be computed; (iv) coding Jacobians is error-prone and hard to debug. Automatic differentiation (Section 7.6) can sometimes avoid manual Jacobians.

**Example 7.6 (pendulum, p. 117–118).** Euler–Maruyama discretisation with $\Delta t$:
$$\mathbf f(\mathbf x_{k-1})=\begin{pmatrix}x_{1,k-1}+x_{2,k-1}\Delta t\\ x_{2,k-1}-g\sin(x_{1,k-1})\Delta t\end{pmatrix},\quad h(\mathbf x_k)=\sin(x_{1,k})\tag{7.46}$$
with $r_k\sim\mathrm N(0,R)$. To avoid a singular noise covariance, the additive-noise approximation of Example 4.21 is used:
$$\mathbf Q=\begin{pmatrix}q^c\Delta t^3/3&q^c\Delta t^2/2\\ q^c\Delta t^2/2&q^c\Delta t\end{pmatrix}\tag{7.47}$$
with $q^c$ the spectral density of the continuous-time noise. Jacobians:
$$\mathbf F_x=\begin{pmatrix}1&\Delta t\\ -g\cos(x_1)\Delta t&1\end{pmatrix},\quad \mathbf H_x=(\cos(x_1)\ \ 0)\tag{7.48}$$
Prior $\mathbf m_0=(0,0)$, $\mathbf P_0=\mathbf I$. After an initial transient the EKF tracks the angle well. Angle RMSE is 0.17, much lower than the measurement-noise standard deviation 0.32 (Fig. 7.1, p. 117–118).

**Example 7.7 (coordinated turn, p. 118–119).** State $\mathbf x_k=(x_{1,k},x_{2,k},s_k,\varphi_k,\omega_k)$: 2D position, speed, direction, angular velocity. Dynamics use the analytical mean discretisation of Example 4.15 (7.50) and the noise covariance of Example 4.22. Measurements are ranges $\sqrt{(x_{1,k}-s_{i,x})^2+(x_{2,k}-s_{i,y})^2}+r_{i,k}$ from four radars (7.51). The Jacobians are more complicated than in the pendulum case but easy to derive. The trajectory was simulated with 100 Euler–Maruyama steps between measurements, not with the additive-noise model. The EKF recovers it well, with position RMSE 0.031 (Fig. 7.2).

### 7.3 Higher-order extended Kalman filters (p. 119–120)
The second-order EKF (Alg. 7.8) retains second-order terms as in Alg. 7.3 (additive noise):
Prediction (7.52):
$$\mathbf m_k^-=\mathbf f(\mathbf m_{k-1})+\tfrac12\sum_i\mathbf e_i\mathrm{tr}\{\mathbf F^{(i)}_{xx}(\mathbf m_{k-1})\mathbf P_{k-1}\},$$
$$\mathbf P_k^-=\mathbf F_x\mathbf P_{k-1}\mathbf F_x^\top+\tfrac12\sum_{i,i'}\mathbf e_i\mathbf e_{i'}^\top\mathrm{tr}\{\mathbf F^{(i)}_{xx}\mathbf P_{k-1}\mathbf F^{(i')}_{xx}\mathbf P_{k-1}\}+\mathbf Q_{k-1}.$$
Update (7.53):
$$\mathbf v_k=\mathbf y_k-\mathbf h(\mathbf m_k^-)-\tfrac12\sum_i\mathbf e_i\mathrm{tr}\{\mathbf H^{(i)}_{xx}(\mathbf m_k^-)\mathbf P_k^-\},$$
$$\mathbf S_k=\mathbf H_x\mathbf P_k^-\mathbf H_x^\top+\tfrac12\sum_{i,i'}\mathbf e_i\mathbf e_{i'}^\top\mathrm{tr}\{\mathbf H^{(i)}_{xx}\mathbf P_k^-\mathbf H^{(i')}_{xx}\mathbf P_k^-\}+\mathbf R_k,$$
and $\mathbf K_k,\mathbf m_k,\mathbf P_k$ as in (7.27). The Hessians $\mathbf F^{(i)}_{xx},\mathbf H^{(i)}_{xx}$ are of $f_i,h_i$ (7.54, 7.55). The non-additive version is not presented (p. 120).
Higher-order EKFs are possible, but cost grows rapidly with order and the extra terms can make filters numerically unstable. The authors therefore prefer iteration (p. 120).

### 7.4 Iterated extended Kalman filter (p. 121–125)
**Idea.** After the EKF update, linearise again at the updated mean, update again, and repeat. This loop is the update step of the IEKF (p. 121). It can be interpreted as a Gauss–Newton method for the MAP estimate at each update (Bell and Cathey, 1993), which per the authors guarantees convergence "in well-defined conditions" (p. 121).

**MAP derivation (additive noise).** The prediction is as in the EKF, $p(\mathbf x_k\mid\mathbf y_{1:k-1})\simeq\mathrm N(\mathbf m_k^-,\mathbf P_k^-)$ (7.56). Likelihood: $p(\mathbf y_k\mid\mathbf x_k)=\mathrm N(\mathbf y_k\mid\mathbf h(\mathbf x_k),\mathbf R_k)$ (7.57). Bayes: $p(\mathbf x_k\mid\mathbf y_{1:k})\propto p(\mathbf y_k\mid\mathbf x_k)p(\mathbf x_k\mid\mathbf y_{1:k-1})$ (7.58). Then $\mathbf x_k^{\rm MAP}=\arg\max_{\mathbf x_k}p(\mathbf y_k\mid\mathbf x_k)p(\mathbf x_k\mid\mathbf y_{1:k-1})$ (7.59). With $L(\mathbf x_k)=-\log[p(\mathbf y_k\mid\mathbf x_k)p(\mathbf x_k\mid\mathbf y_{1:k-1})]$ (7.60),
$$L(\mathbf x_k)\simeq C+\tfrac12(\mathbf y_k-\mathbf h(\mathbf x_k))^\top\mathbf R_k^{-1}(\mathbf y_k-\mathbf h(\mathbf x_k))+\tfrac12(\mathbf x_k-\mathbf m_k^-)^\top[\mathbf P_k^-]^{-1}(\mathbf x_k-\mathbf m_k^-)\tag{7.61}$$
with $C$ independent of $\mathbf x_k$, and $\mathbf x_k^{\rm MAP}=\arg\min L$ (7.62) (p. 121–122).

**Gauss–Newton** assumes $L_{\rm GN}(\mathbf x_k)=\tfrac12\sum_{j=1}^N\mathbf r_j^\top(\mathbf x_k)\mathbf r_j(\mathbf x_k)$ (7.63). It iterates: (1) first-order Taylor expand $\mathbf r_1,\dots,\mathbf r_N$ about the current estimate; (2) find analytically the optimum of the resulting approximate model (p. 122). Here $N=3$:
$$\mathbf r_1=\sqrt{2C},\quad \mathbf r_2=\mathbf R_k^{-1/2}(\mathbf y_k-\mathbf h(\mathbf x_k)),\quad \mathbf r_3=[\mathbf P_k^-]^{-1/2}(\mathbf x_k-\mathbf m_k^-)\tag{7.64}$$
Linearising represents $\mathbf r_1,\mathbf r_3$ exactly and approximates only $\mathbf r_2$, through $\mathbf h$ (p. 122).

**Iteration.** From a guess $\mathbf x_k^{(0)}$, with current estimate $\mathbf x_k^{(i-1)}$: $\mathbf h(\mathbf x_k)\simeq\mathbf h(\mathbf x_k^{(i-1)})+\mathbf H_x(\mathbf x_k^{(i-1)})(\mathbf x_k-\mathbf x_k^{(i-1)})$ (7.65). Substituting in $L$ gives the quadratic (7.66):
$$L_{\rm GN}\simeq C+\tfrac12(\mathbf y_k-\mathbf h(\mathbf x_k^{(i-1)})-\mathbf H_x(\mathbf x_k-\mathbf x_k^{(i-1)}))^\top\mathbf R_k^{-1}(\cdots)+\tfrac12(\mathbf x_k-\mathbf m_k^-)^\top[\mathbf P_k^-]^{-1}(\mathbf x_k-\mathbf m_k^-)$$
Instead of setting the gradient to zero, the authors note that (7.66) is the negative log-posterior of the affine model $\tilde p(\mathbf y_k\mid\mathbf x_k)=\mathrm N(\mathbf y_k\mid\mathbf h(\mathbf x_k^{(i-1)})+\mathbf H_x(\mathbf x_k^{(i-1)})(\mathbf x_k-\mathbf x_k^{(i-1)}),\mathbf R_k)$ (7.67). Prior and likelihood are linear-Gaussian, so the minimiser equals the posterior mean. The affine Kalman update (Theorem 6.9) with $\mathbf H_k=\mathbf H_x(\mathbf x_k^{(i-1)})$ and offset $\mathbf b_k=\mathbf h(\mathbf x_k^{(i-1)})-\mathbf H_x\mathbf x_k^{(i-1)}$ gives
$$\mathbf K_k^{(i)}=\mathbf P_k^-\mathbf H_x^\top[\mathbf H_x\mathbf P_k^-\mathbf H_x^\top+\mathbf R_k]^{-1},\quad \mathbf x_k^{(i)}=\mathbf m_k^-+\mathbf K_k^{(i)}[\mathbf y_k-\mathbf h(\mathbf x_k^{(i-1)})-\mathbf H_x(\mathbf x_k^{(i-1)})(\mathbf m_k^--\mathbf x_k^{(i-1)})]\tag{7.68}$$
(all $\mathbf H_x$ at $\mathbf x_k^{(i-1)}$) (p. 123). Repeating until a stationary point $\mathbf x_k^{(*)}\simeq\mathbf x_k^{\rm MAP}$ gives the updated mean. The covariance is that of the linearised model (7.67) at that mean (p. 123–124).

**Algorithm 7.9 (IEKF)** (p. 124). Prediction as (7.26), written (7.69). Update: start with $\mathbf x_k^{(0)}=\mathbf m_k^-$ (for example); for $i=1,\dots,I_{\max}$:
$$\begin{aligned}\mathbf v_k^{(i)}&=\mathbf y_k-\mathbf h(\mathbf x_k^{(i-1)})-\mathbf H_x(\mathbf x_k^{(i-1)})(\mathbf m_k^--\mathbf x_k^{(i-1)}),\\ \mathbf S_k^{(i)}&=\mathbf H_x(\mathbf x_k^{(i-1)})\mathbf P_k^-\mathbf H_x^\top(\mathbf x_k^{(i-1)})+\mathbf R_k,\\ \mathbf K_k^{(i)}&=\mathbf P_k^-\mathbf H_x^\top(\mathbf x_k^{(i-1)})[\mathbf S_k^{(i)}]^{-1},\\ \mathbf x_k^{(i)}&=\mathbf m_k^-+\mathbf K_k^{(i)}\mathbf v_k^{(i)}\end{aligned}\tag{7.70}$$
Set $\mathbf m_k=\mathbf x_k^{(I_{\max})}$ and
$$\mathbf P_k=\mathbf P_k^--\mathbf K_k^{(I_{\max})}\mathbf S_k^{(I_{\max})}[\mathbf K_k^{(I_{\max})}]^\top\tag{7.71}$$

The iteration only improves the update step and ignores other time steps. It can help when the measurement likelihood is informative compared with the predicted density (Morelande and García-Fernández, 2013). Chapters 13–14 treat global iteration over whole trajectories (p. 124).

*Intuition note.* The EKF linearises $\mathbf h$ at the predicted mean. The IEKF linearises again at the updated mean, step by step, in a search for the MAP estimate. The source asks the reader to show that the IEKF with a single iteration is equivalent to the first-order EKF (Exercise 7.4).

**Example 7.10 (p. 124–125).** On the pendulum, IEKF gives RMSE 0.17, the same as EKF (Fig. 7.3).
**Example 7.11 (p. 125–126).** On the coordinated turn with the accurate initial guess of Example 7.7, IEKF and EKF are basically the same. With an initial guess further from the true position (and larger prior covariance), EKF takes much longer to converge. RMSE: EKF 0.038, IEKF 0.031. After the initial transient the results are practically identical (Fig. 7.4).

### 7.5 Levenberg–Marquardt, line-search and related IEKFs (p. 125–127)
The IEKF can be seen as a Gauss–Newton method for the cost (7.72) (same as (7.61)). Other optimisation methods often perform better (Fatemi et al., 2012; Skoglund et al., 2015):
- **Levenberg–Marquardt:** add a regularisation term $\tfrac12\lambda(\mathbf x_k-\mathbf x_k^{(i-1)})^\top(\mathbf x_k-\mathbf x_k^{(i-1)})$ to (7.66), giving (7.73). It can be implemented as an extra measurement at $\mathbf x_k^{(i-1)}$ with noise covariance $\mathbf I/\lambda$.
- **Line search:** replace the step by $\mathbf x_k^{(i)}=\mathbf x_k^{(i-1)}+\gamma(\tilde{\mathbf x}_k^{(i)}-\mathbf x_k^{(i-1)})$ (7.74), where $\tilde{\mathbf x}_k^{(i)}=\mathbf m_k^-+\mathbf K_k^{(i)}\mathbf v_k^{(i)}$ and $\gamma$ approximately minimises $L$ along that line.
- **Quasi-Newton:** include an additional correction matrix in the minimisation, which gives an extension similar to Levenberg–Marquardt.

### 7.6 Automatic differentiation and EKFs (p. 127–128)
EKFs need $\mathbf F_x,\mathbf H_x$ (and, for second order, the Hessians). Manual derivation can be tedious, for example when models come from numerical PDE solutions. Automatic differentiation (AD) turns the function into a sequence of operations that computes the value and its exact derivative; this differs from finite-difference approximation. AD avoids derivation errors and can validate manual derivatives. A disadvantage is that it can be slower than hand-coded derivatives. In parameter estimation (Chapter 16) it can give derivatives of the marginal log-likelihood (p. 127–128).

### 7.7 Exercises (p. 128–130)
Listed under "Exercises worth doing".

## Toy example (ours, not from the text)
Scalar case: $g(x)=x^2$, $x\sim\mathrm N(1,0.04)$, so $m=1$, $P=0.04$.

*Transform.* $G_x=2$, $G_{xx}=2$.
- Linear (Alg. 7.1, $Q=0$): $\mu_L=1$, $S_L=2\cdot0.04\cdot2=0.16$, $C_L=0.04\cdot2=0.08$.
- Quadratic (Alg. 7.3): $\mu_Q=1+\tfrac12\cdot2\cdot0.04=1.04$. $S_Q=0.16+\tfrac12(2\cdot0.04)^2=0.16+0.0032=0.1632$.
- (Added check, not in the text) For Gaussian $x$, the exact values are $\mathrm E[x^2]=m^2+P=1.04$ and $\mathrm{Var}[x^2]=4m^2P+2P^2=0.16+0.0032=0.1632$, so the second-order result is exact here because $g$ is quadratic.

*EKF update.* Prior $m^-=1$, $P^-=0.04$; $h(x)=x^2$, $R=0.01$, $y=1.2$.
- $H=2$, $v=1.2-1=0.2$, $S=4\cdot0.04+0.01=0.17$.
- $K=0.04\cdot2/0.17=0.4706$, $m=1+0.4706\cdot0.2=1.0941$, $P=0.04-0.08^2/0.17=0.04-0.03765=0.00235$.

*IEKF second iteration* (7.70), $x^{(1)}=1.0941$:
- $H=2.1882$, $h(x^{(1)})=1.1971$.
- $v^{(2)}=1.2-1.1971-2.1882\,(1-1.0941)=0.0029+0.2060=0.2089$.
- $S^{(2)}=2.1882^2\cdot0.04+0.01=0.2015$, $K^{(2)}=0.04\cdot2.1882/0.2015=0.4343$.
- $x^{(2)}=1+0.4343\cdot0.2089=1.0907$.

The estimate moves from 1.0941 to 1.0907, showing the re-linearisation effect. At 1.0907 the gradient of $L$, $-200x(1.2-x^2)+25(x-1)$, is about 0.005, so this is nearly the MAP stationary point.

## Concepts
- [[linearization]] — first-order Taylor approximation of a non-linear map at the current mean, used as the basis for EKF equations (p. 109)
- [[extended-kalman-filter]] (new) — Kalman filter with $\mathbf f,\mathbf h$ in the means and Jacobians in the covariances; assumes Gaussian filtering densities (p. 113)
- [[taylor-gaussian-approximation]] (new) — Gaussian approximation of $(\mathbf x,\mathbf g(\mathbf x))$ by a Taylor expansion; linear or quadratic (Algs. 7.1–7.3) (p. 110–112)
- [[second-order-ekf]] (new) — EKF keeping Hessian terms in the Taylor series (p. 119)
- [[iterated-ekf]] (new) — EKF whose update is repeated, re-linearising at the latest mean (p. 121)
- [[gauss-newton-method]] (new) — optimisation of a sum of squared residuals by repeated linearisation of the residuals (p. 122)
- [[map-estimate]] (new) — state maximising the posterior; here the minimiser of $L$ (p. 121)
- [[levenberg-marquardt]] (new) — Gauss–Newton with an added regularisation term (p. 126)
- [[automatic-differentiation]] (new) — exact derivatives from program operations, not finite differences (p. 127)
- [[kalman-filter]] — recursive predict–update estimator that the EKF reuses with linearisation (p. 113)
- [[kalman-gain]] — $\mathbf K_k=\mathbf P_k^-\mathbf H_x^\top\mathbf S_k^{-1}$, the weight on the innovation $\mathbf v_k$ (p. 114)
- [[state-space-model]] — $\mathbf x_k=\mathbf f(\mathbf x_{k-1})+\mathbf q_{k-1}$, $\mathbf y_k=\mathbf h(\mathbf x_k)+\mathbf r_k$ (p. 113)
- [[disturbance and noise]] — Gaussian process and measurement noise, additive or non-additive (p. 113, 115)

## Canonical instances
- [[pendulum-tracking]] — EKF/IEKF track pendulum angle from $\sin(x_1)$ measurements; RMSE 0.17 (p. 117, 124)
- [[coordinated-turn-radar-tracking]] — five-state turn model with four range radars; with a poor initial guess the EKF takes much longer to converge than the IEKF; RMSE 0.038 vs 0.031 (p. 118–119, 125–126)
- [[bearings-only-tracking]] — two angle sensors, Exercise 7.2 (p. 128–129)

## Bridges (candidates)
- [structural-analogy] EKF linearisation at the current estimate ↔ control-theory linearisation: Jacobian approximation of a non-linear system near an operating point — here taken at the moving estimate, not a fixed equilibrium.
- [same-math] IEKF update ↔ optimisation: Gauss–Newton for a nonlinear least-squares/MAP cost (the text states this equivalence, p. 121–122).
- [structural-analogy] EKF ↔ observer (state estimator): a model run in parallel, corrected by gain times innovation, with the gain from the covariance.
- [structural-analogy] Levenberg–Marquardt regularisation ↔ trust-region step control in numerical optimisation.

## Questions this raises
- How large can the non-linearity be, relative to the covariance, before linearisation at the mean fails? Which methods avoid derivatives (the chapter notes Jacobians may be impossible to compute)?
- When does the IEKF iteration converge, and what are the "well-defined conditions" of the convergence guarantee?
- How does a global (whole-trajectory) iteration, promised for Chapters 13–14, differ from the local update iteration?
- Is the EKF covariance consistent (not over-confident) when the model is strongly non-linear?

## Exercises worth doing
- Ex. 7.1 (p. 128) — derive derivatives and implement an EKF on a scalar non-linear model; the basic workflow — difficulty: easy
- Ex. 7.2 (p. 128–129) — bearings-only tracking with two angle sensors; $\mathrm{atan2}$, scalar updates, Jacobian check — difficulty: medium
- Ex. 7.3 (p. 129) — second-order EKF on the model of 7.1 — difficulty: medium
- Ex. 7.4 (p. 129) — show that the IEKF with one iteration equals the first-order EKF — difficulty: easy
- Ex. 7.5–7.6 (p. 129) — derive the IEKF update via the affine Kalman update, and via gradient zero plus matrix inversion formulas — difficulty: medium
- Ex. 7.8 (p. 130) — EKF for the Cartesian coordinated turn with linear position measurements; why would the IEKF make no sense? — difficulty: medium

## Reading notes
- Printed page = pdf page − 30 (labels give printed numbers directly).
- The text layer loses many symbols (hats, minus superscripts, Greek letters). Equations here were checked against the page images; the "−" on prior quantities $\mathbf m_k^-,\mathbf P_k^-$ appears in the images.
- Page 127 has no figure; Fig. 7.5 (p. 128, in Exercise 7.2) is an illustration of two sensor dishes and a car (no data).
- The 7.3 non-additive second-order EKF is explicitly omitted by the authors. Exercises 7.7 and 7.9 (implement IEKF) are listed on p. 130.
- Source mentions Example numbers (4.9, 4.15, 4.21, 4.22, 5.2, 5.4), Lemma A.3, Theorem 6.9 and Corollary A.5 from outside this unit; their content is not in these pages beyond the uses shown.
