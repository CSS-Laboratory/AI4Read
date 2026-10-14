---
id: welch-2004-kalmanintro/main
work: welch-2004-kalmanintro
unit: paper
pages: 1-16
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# An Introduction to the Kalman Filter (Welch & Bishop)

## L0 — One line
The Kalman filter estimates a hidden state recursively by alternating a model-based prediction with a measurement correction weighted by the gain $K$, and the extended version handles nonlinear systems by linearizing.

## L1 — The gist (≤ 120 words)
The paper asks how to estimate the state of a noisy process from noisy measurements without reprocessing all past data. The answer is a two-step cycle. A time update predicts the state and its error covariance. A measurement update corrects the prediction with the residual (measurement minus predicted measurement), weighted by a gain that balances prediction uncertainty against sensor noise. The extended Kalman filter (EKF) applies the same cycle to nonlinear systems by linearizing with Jacobians, at the price of being only approximate. A worked example estimates a constant voltage and shows how the assumed measurement noise $R$ tunes the filter. The filter has been the subject of extensive research and application, particularly in navigation.

**Prerequisites:** matrices and transposes; expectation, variance and covariance matrices; normal distribution; partial derivatives (Jacobian); the idea of a state vector.

## L2 — Key ideas (5–10 bullets)
- The filter estimates the state $x$ of a linear process with Gaussian, white, independent process noise $w$ and measurement noise $v$ (eqs. 1.1–1.4) (p. 2).
- The posterior estimate (the one after using the measurement) is the prior estimate (the one before) plus the gain times the residual. $K$ is chosen to minimize the posterior error covariance (p. 3).
- The gain behaves sensibly in the limits. Small $R$ means the measurement is trusted more; small $P_k^-$ means the prediction is trusted more (pp. 3–4).
- The filter is a predict–correct cycle (time update, measurement update). It is recursive, which makes it more practical than a Wiener filter that works on all data directly (pp. 4–5).
- $R$ can usually be measured off-line. $Q$ is harder to set. Both can be tuned, and $Q_k$ and $R_k$ may change over time (pp. 6–7, 10).
- The EKF linearizes $f$ and $h$ about the current estimate using Jacobians. It is ad hoc: normality is lost after nonlinear transformations (pp. 7–10).
- If, over all measurements, there is not a one-to-one mapping between the measurement and the state via $h$, the authors say the filter will quickly diverge ("as you might expect"), and the process is then unobservable (p. 11).
- In the scalar example, the choice of $R$ trades responsiveness against estimate variance; the initial $P_0$ matters little unless it is 0 (pp. 12–15).

## L3 — Walkthrough

### 1 The Discrete Kalman Filter

**Process and measurement model (p. 2).** The state $x\in\Re^n$ of a discrete-time controlled process obeys
$$x_k = Ax_{k-1}+Bu_{k-1}+w_{k-1}\tag{1.1}$$
with measurement $z\in\Re^m$
$$z_k = Hx_k+v_k.\tag{1.2}$$
The process noise $w$ and measurement noise $v$ are independent of each other, white, and normal:
$$p(w)\sim N(0,Q),\qquad p(v)\sim N(0,R).\tag{1.3, 1.4}$$

Shapes (p. 2): $A$ is $n\times n$, $B$ is $n\times l$ (control $u\in\Re^l$), $H$ is $m\times n$. $Q$ and $R$ are covariance matrices (sizes $n\times n$ and $m\times m$ follow from the equations — added). In practice $Q,R,A,H$ may change per step, but here they are assumed constant (p. 2).

**Computational origins (pp. 2–3).**
- $\hat x_k^-\in\Re^n$ is the a priori estimate, using knowledge before step $k$. $\hat x_k$ is the a posteriori estimate, given measurement $z_k$ (p. 2).
- Errors: $e_k^-\equiv x_k-\hat x_k^-$ and $e_k\equiv x_k-\hat x_k$ (p. 2). Covariances: $P_k^-=E[e_k^-e_k^{-T}]$ (1.5) and $P_k=E[e_ke_k^T]$ (1.6) (p. 3).
- The goal is a posterior estimate that is a linear combination of the prior estimate and a weighted difference between the actual and predicted measurement:
$$\hat x_k=\hat x_k^-+K(z_k-H\hat x_k^-)\tag{1.7}$$
- The difference $z_k-H\hat x_k^-$ is the *innovation* or *residual*. Zero residual means prediction and measurement agree completely (p. 3).
- $K$ ($n\times m$) is the *gain* or blending factor that minimizes (1.6). The author gives the method but not the algebra. Substitute (1.7) into the definition of $e_k$, put that into (1.6), take the expectations, differentiate the trace with respect to $K$, set the result to zero, and solve for $K$ (p. 3). One resulting form is
$$K_k=P_k^-H^T(HP_k^-H^T+R)^{-1}=\frac{P_k^-H^T}{HP_k^-H^T+R}.\tag{1.8}$$
The footnote says the filter equations can be rearranged into several forms (p. 3).
- Limits (p. 3): $\lim_{R_k\to0}K_k=H^{-1}$ and $\lim_{P_k^-\to0}K_k=0$. (The $H^{-1}$ presumes $H$ is invertible — added note.) So when $R\to0$ the measurement is trusted more and more. When $P_k^-\to0$ the prediction is trusted more and more (p. 4).

*Intuition note:* $K$ is a trust dial. If the sensor is clean (small $R$), the filter moves toward the measurement. If the prediction is already very certain (small $P^-$), the filter mostly ignores the new measurement.

**Probabilistic origins (p. 4).** The justification for (1.7) comes from the probability of the prior estimate conditioned on past measurements (Bayes' rule). The filter maintains the first two moments of the state distribution: $E[x_k]=\hat x_k$ and $E[(x_k-\hat x_k)(x_k-\hat x_k)^T]=P_k$. The posterior estimate is normally distributed if (1.3) and (1.4) hold. Thus $p(x_k|z_k)\sim N(\hat x_k,P_k)$ (p. 4).

**Algorithm (pp. 4–5).** The filter uses a form of feedback control: it estimates the state, then receives feedback as noisy measurements. The *time update* (predictor) projects the state and covariance forward. The *measurement update* (corrector) folds in the new measurement (p. 4). The cycle is shown in Figure 1-1 and Figure 1-2 (p. 5, p. 6).

Time update (p. 5):
$$\hat x_k^-=A\hat x_{k-1}+Bu_{k-1}\tag{1.9}$$
$$P_k^-=AP_{k-1}A^T+Q\tag{1.10}$$

Measurement update (p. 5):
$$K_k=P_k^-H^T(HP_k^-H^T+R)^{-1}\tag{1.11}$$
$$\hat x_k=\hat x_k^-+K_k(z_k-H\hat x_k^-)\tag{1.12}$$
$$P_k=(I-K_kH)P_k^-\tag{1.13}$$

Order of steps: compute $K_k$ (same as 1.8), measure $z_k$, update the estimate with (1.12), update the covariance with (1.13). Then the posterior estimates seed the next prediction. Initial estimates $\hat x_{k-1}$, $P_{k-1}$ are needed (pp. 5–6). The recursion is a selling point. A Wiener filter is designed to operate on all the data directly for each estimate. The Kalman filter instead recursively conditions the current estimate on all past measurements (p. 5).

**Parameters and tuning (pp. 6–7).**
- $R$ is usually measured before operation, by taking off-line sample measurements. This is generally practical because we must be able to measure the process anyway (p. 6).
- $Q$ is generally harder, because we typically cannot observe the process directly. Sometimes a simple (poor) model gives acceptable results if enough uncertainty is "injected" through $Q$. In that case one hopes the measurements are reliable (p. 6).
- Often better performance results from tuning $Q$ and $R$, usually off-line, frequently with another distinct Kalman filter, a process called *system identification* (p. 6).
- If $Q$ and $R$ are in fact constant, $P_k$ and $K_k$ stabilize quickly and stay constant. They can then be pre-computed, by running the filter off-line or by finding the steady-state $P_k$ (p. 6).
- The measurement error (in particular) frequently does not remain constant. In the authors' ceiling-panel tracker, noise for nearby beacons will be smaller than for far-away ones. $Q$ is sometimes changed dynamically ($Q_k$); for example, for head tracking in a 3D virtual environment they might reduce $Q_k$ if the user seems to be moving slowly, and increase it if the dynamics start changing rapidly (p. 7).

### 2 The Extended Kalman Filter (EKF)

**Setting (p. 7).** If the process or the measurement relation is nonlinear, a Kalman filter that linearizes about the current mean and covariance is an *extended Kalman filter*. The linearization is "akin to a Taylor series", using partial derivatives (p. 7). The model becomes
$$x_k=f(x_{k-1},u_{k-1},w_{k-1}),\qquad z_k=h(x_k,v_k).\tag{2.1, 2.2}$$
The noises are as in (1.3)–(1.4). Since the noise values are unknown, one approximates without them (here $\hat x_{k-1}$ is an a posteriori estimate from the previous step):
$$\tilde x_k=f(\hat x_{k-1},u_{k-1},0),\qquad \tilde z_k=h(\tilde x_k,0).\tag{2.3, 2.4}$$

**Flaw (p. 8).** After nonlinear transformations the random variables are no longer normal. The EKF is an ad hoc estimator that only approximates the optimality of Bayes' rule by linearization. Julier et al. developed a variation that preserves normal distributions through nonlinear transformations (p. 8).

**Linearized equations (p. 8).**
$$x_k\approx\tilde x_k+A(x_{k-1}-\hat x_{k-1})+Ww_{k-1}\tag{2.5}$$
$$z_k\approx\tilde z_k+H(x_k-\tilde x_k)+Vv_k\tag{2.6}$$
The Jacobians, each entry a partial derivative:
- $A_{[i,j]}=\partial f_{[i]}/\partial x_{[j]}(\hat x_{k-1},u_{k-1},0)$
- $W_{[i,j]}=\partial f_{[i]}/\partial w_{[j]}(\hat x_{k-1},u_{k-1},0)$
- $H_{[i,j]}=\partial h_{[i]}/\partial x_{[j]}(\tilde x_k,0)$
- $V_{[i,j]}=\partial h_{[i]}/\partial v_{[j]}(\tilde x_k,0)$

They differ at each step even though the subscript $k$ is omitted (p. 8).

**Error process (p. 9).** Define the prediction error $\tilde e_{x_k}\equiv x_k-\tilde x_k$ (2.7) and the measurement residual $\tilde e_{z_k}\equiv z_k-\tilde z_k$ (2.8). In practice $x_k$ is not available, but $z_k$ is. Then
$$\tilde e_{x_k}\approx A(x_{k-1}-\hat x_{k-1})+\varepsilon_k\tag{2.9}$$
$$\tilde e_{z_k}\approx H\tilde e_{x_k}+\eta_k\tag{2.10}$$
Here $\varepsilon_k$ and $\eta_k$ are new independent zero-mean variables with covariances $WQW^T$ and $VRV^T$ (p. 9).

Equations (2.9)–(2.10) are linear and resemble (1.1)–(1.2). This motivates using $\tilde e_{z_k}$ and a second, hypothetical Kalman filter to estimate $\tilde e_{x_k}$, giving an estimate $\hat e_k$ with
$$\hat x_k=\tilde x_k+\hat e_k.\tag{2.11}$$
With approximate distributions $p(\tilde e_{x_k})\sim N(0,E[\tilde e_{x_k}\tilde e_{x_k}^T])$, $p(\varepsilon_k)\sim N(0,WQ_kW^T)$, $p(\eta_k)\sim N(0,VR_kV^T)$, and the predicted $\hat e_k$ set to zero:
$$\hat e_k=K_k\tilde e_{z_k}.\tag{2.12}$$
Substituting into (2.11) and using (2.8) shows the second filter is not needed:
$$\hat x_k=\tilde x_k+K_k\tilde e_{z_k}=\tilde x_k+K_k(z_k-\tilde z_k).\tag{2.13}$$
$K_k$ comes from (1.11) with the appropriate substitution for the measurement error covariance (p. 9).

*Intuition note:* The EKF applies a (hypothetical) Kalman filter to the *error* around a nominal prediction, using the linear error equations (2.9)–(2.10). Adding the estimated error back onto the nominal prediction gives the estimate.

**Complete EKF equations (p. 10).** Here $\hat x_k^-$ replaces $\tilde x_k$, and the Jacobians get subscript $k$ because they are recomputed each step.

Time update:
$$\hat x_k^-=f(\hat x_{k-1},u_{k-1},0)\tag{2.14}$$
$$P_k^-=A_kP_{k-1}A_k^T+W_kQ_{k-1}W_k^T\tag{2.15}$$
Measurement update:
$$K_k=P_k^-H_k^T(H_kP_k^-H_k^T+V_kR_kV_k^T)^{-1}\tag{2.16}$$
$$\hat x_k=\hat x_k^-+K_k(z_k-h(\hat x_k^-,0))\tag{2.17}$$
$$P_k=(I-K_kH_k)P_k^-\tag{2.18}$$
The basic operation is the same cycle as in Figure 1-1 (Figure 2-1, p. 11).

**Role of $H_k$ (p. 11).** $H_k$ in the gain serves to "magnify" only the relevant component of the measurement information. For example, if there is not a one-to-one mapping between $z_k$ and the state via $h$, $H_k$ affects the gain so that it only magnifies the portion of the residual that does affect the state. If over *all* measurements there is *not* a one-to-one mapping between $z_k$ and the state via $h$, then, as the authors put it, "as you might expect" the filter will quickly diverge. The process is then unobservable (p. 11).

### 3 A Kalman Filter in Action: Estimating a Random Constant

**Model (pp. 11–12).** Estimate a scalar constant, for example a voltage, measured with 0.1 V RMS white noise. The model is $x_k=x_{k-1}+w_k$ and $z_k=x_k+v_k$. So $A=1$, $u=0$, $H=1$ (p. 12).

**Filter (p. 12).** Time update: $\hat x_k^-=\hat x_{k-1}$, $P_k^-=P_{k-1}+Q$. Measurement update:
$$K_k=\frac{P_k^-}{P_k^-+R}\tag{3.1}$$
$$\hat x_k=\hat x_k^-+K_k(z_k-\hat x_k^-),\qquad P_k=(1-K_k)P_k^-$$

**Parameters (p. 12).**
- $Q=10^{-5}$. A small non-zero value gives more flexibility in tuning than $Q=0$.
- The true constant is assumed to have a standard normal distribution, so the filter is seeded with $\hat x_{k-1}=0$.
- $P_0=1$. $P_0=0$ would make the filter initially and always believe $\hat x_k=0$. Almost any $P_0\neq0$ would eventually converge.

**Simulations (pp. 13–15).**
- The true constant was $-0.37727$. Fifty measurements were generated with noise of standard deviation 0.1. They were fixed in advance so that runs with different parameters are comparable (p. 13).
- Run 1: $R=(0.1)^2=0.01$, the true measurement variance, so the authors expect the best balance of responsiveness and estimate variance (Fig. 3-1, p. 13). By iteration 50, $P_k$ has settled from 1 to about $0.0002$ V² (Fig. 3-2, p. 14).
- Run 2: $R=1$, 100 times larger. The filter is slower to believe the measurements, giving reduced estimate variance (Fig. 3-3, p. 14).
- Run 3: $R=0.0001$, 100 times smaller. The filter responds quickly, which increases the estimate variance (Fig. 3-4, p. 15).
- In Figure 3-3 in particular, the estimate appears considerably smoother than the noisy measurements (p. 15).

*Intuition note:* $R$ is the filter's belief about sensor noise. Telling it the sensor is bad gives a smooth but sluggish estimate. Telling it the sensor is good makes the filter quick to believe the noisy measurements, which increases the estimate variance.

## Toy example (ours, not from the text)
Scalar, $A=H=1$, no control. Take $Q=0$, $R=1$, $\hat x_0=0$, $P_0=1$, and measurements $z_1=2$, $z_2=3$.
- Step 1 predict: $\hat x_1^-=0$, $P_1^-=1+0=1$. Gain: $K_1=1/(1+1)=0.5$. Update: $\hat x_1=0+0.5(2-0)=1$. $P_1=(1-0.5)\cdot1=0.5$.
- Step 2 predict: $\hat x_2^-=1$, $P_2^-=0.5$. Gain: $K_2=0.5/(0.5+1)=1/3$. Update: $\hat x_2=1+\tfrac13(3-1)=5/3\approx1.667$. $P_2=(1-\tfrac13)(0.5)=1/3$.
- Check: with $Q=0$ the result equals a precision-weighted average of the prior (weight 1, value 0) and the data, $(0+2+3)/3=5/3$, and $P=1/3$ matches.
- If instead $R=100$ in step 1: $K_1=1/101\approx0.0099$, so $\hat x_1=2/101\approx0.0198$. The filter barely moves toward the data.

## Concepts
- [[kalman-filter]] — recursive estimator alternating prediction and correction; minimizes mean squared error (pp. 1–5)
- [[kalman-gain]] — $K_k=P_k^-H^T(HP_k^-H^T+R)^{-1}$, the weight on the residual (p. 3)
- [[state-space-model]] — here $x_k=Ax_{k-1}+Bu_{k-1}+w_{k-1}$, $z_k=Hx_k+v_k$ (p. 2)
- [[disturbance-and-noise]] — process noise $w\sim N(0,Q)$ and measurement noise $v\sim N(0,R)$ (p. 2)
- [[observer]] — the filter estimates the state, using measurements as feedback (p. 4)
- [[feedback]] — the author says the filter uses "a form of feedback control": measurements correct the estimate (p. 4)
- [[linearization]] — EKF linearizes $f,h$ with Jacobians about the current estimate (pp. 7–8)
- [[observability]] — if over all measurements there is not a one-to-one mapping between measurement and state via $h$, the filter will quickly diverge ("as you might expect") and the process is "unobservable" (p. 11)
- [[state]] — $x\in\Re^n$, the quantity being estimated (p. 2)
- [[innovation-residual]] (new) — $z_k-H\hat x_k^-$, the gap between actual and predicted measurement (p. 3)
- [[a-priori-a-posteriori-estimate]] (new) — estimate before ($\hat x_k^-$) and after ($\hat x_k$) using $z_k$ (p. 2)
- [[predictor-corrector]] (new) — time update predicts, measurement update corrects (p. 4)
- [[extended-kalman-filter]] (new) — Kalman filter linearized about the current estimate; ad hoc, only approximates the optimality of Bayes' rule (pp. 7–8)
- [[system-identification]] (new) — off-line tuning of $Q$ and $R$, often with another Kalman filter (p. 6)

## Canonical instances
- [[estimating-a-random-constant]] — scalar voltage example showing the effect of $R$ on smoothness and responsiveness (pp. 11–15)
- [[head-tracking-3d-environment]] — $Q_k$ might be reduced if the user seems to be moving slowly and increased if the dynamics start changing rapidly (p. 7)
- [[ceiling-beacon-tracker]] — measurement noise smaller for near beacons than far ones, so $R$ is not constant (p. 7)

## Bridges (candidates)
- [structural-analogy] Kalman gain as trust weight ↔ statistics: inverse-variance weighted averaging — in the toy case with $Q=0$ the estimate is a weighted mean of prior and data.
- [same-math] EKF Jacobians $A_k,W_k,H_k,V_k$ ↔ control-theory linearization: first-order Taylor expansion of $f,h$ about an operating point.
- [structural-analogy] Predict–correct cycle ↔ Bayesian updating: the paper links the filter's justification to conditioning on past measurements (Bayes' rule) (p. 4).
- [structural-analogy] Residual correction $\hat x^-+K(z-H\hat x^-)$ ↔ observer design: a model run in parallel and corrected by measurement error.

## Questions this raises
- How exactly is $K$ derived by minimizing the trace of $P_k$? The paper cites other references for the algebra (p. 3).
- When $Q$ and $R$ are constant, to what steady-state values do $P_k$ and $K_k$ converge? The paper only states that they stabilize (p. 6).
- How do Julier et al.'s methods keep distributions normal through nonlinear maps (p. 8)?
- What happens to the filter if the Gaussian, white, independent noise assumptions fail?

## Reading notes
- Printed page = pdf page (offset 0). This is a 16-page technical report, updated April 5, 2004. Title page, abstract, then Sections 1–3 and references.
- The abstract claims the filter supports estimating past, present and future states, and works even when the system is not precisely known. The body pages here do not develop this.
- Page 9 says "see the previous footnote" for the approximate distributions. The only footnote in the body pages is on p. 3, about equivalent algebraic forms (the title page has only author-contact footnotes); which footnote p. 9 means is unclear.
- Text after (2.15) calls $Q_k$ the covariance "at step $k$", but (2.15) uses $Q_{k-1}$. Text after (2.18) writes "$H_k$ and $V$" (no subscript on $V$). Footnote 1 on p. 3 has a typo ("into to").
- Section 2 (p. 8) says "$\hat x_k$ is an a posteriori estimate of the state at step $k$", while (2.5) uses $\hat x_{k-1}$. The p. 7 text says "from a previous time step $k$". The wording is loose.
- Fig. 3-2 (p. 14) has a y-axis that only reaches 0.01 and shows $P_k^-$ in its caption, while the text says $P_k$ settles from an initial 1 to about 0.0002. Figures 3-1 to 3-4 are plots with no numeric data.
- The limit $K\to H^{-1}$ (p. 3) is written without stating that $H$ must be invertible.
