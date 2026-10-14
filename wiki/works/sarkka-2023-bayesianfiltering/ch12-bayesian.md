---
id: sarkka-2023-bayesianfiltering/ch12-bayesian
work: sarkka-2023-bayesianfiltering
unit: "12 Bayesian Smoothing Equations and Exact Solutions"
pages: 253–266
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
# Bayesian Smoothing Equations and Exact Solutions

## L0 — One line
A smoother runs backward from a filter's output and conditions each state on all measurements; for linear Gaussian models it has a closed form (the RTS smoother), and for discrete states it becomes sums over states; the Viterbi algorithm is a separate method that finds the most probable whole state path (the MAP trajectory).

## L1 — The gist (≤ 120 words)
A filter estimates $\mathbf x_k$ from measurements up to step $k$ only. The chapter asks how to also use later measurements up to $T$. The answer is a backward recursion that starts from the filtering distributions (Theorem 12.1). For linear Gaussian models it becomes the Rauch–Tung–Striebel (RTS) smoother, with an affine extension. For discrete states it becomes sums over states. The Viterbi algorithm is a different task: it finds the single most probable whole trajectory. In the book's examples, smoothing gives smaller variances (equal at the last step) and lower errors than filtering. The book says the affine RTS form is useful later for building non-linear smoothers.

**Prerequisites:** Bayes' rule; Markov property; Kalman filter prediction/update; joint, conditional and marginal Gaussians; hidden Markov models; dynamic programming (max over sequences).

## L2 — Key ideas (5–10 bullets)
- Smoothing computes $p(\mathbf x_k\mid\mathbf y_{1:T})$ for $T>k$, using future data that a filter ignores (p. 253).
- The forward-backward smoother needs the filter output and then recurses backward, from $p(\mathbf x_{k+1}\mid\mathbf y_{1:T})$ to $p(\mathbf x_k\mid\mathbf y_{1:T})$ (Theorem 12.1, pp. 254–255).
- The two-filter smoother uses $p(\mathbf x_k\mid\mathbf y_{1:k-1})\,p(\mathbf y_{k:T}\mid\mathbf x_k)$. The book prefers forward-backward because it carries over better to approximate non-linear smoothers (p. 255).
- RTS smoother: for linear Gaussian models the backward recursion is closed-form in means and covariances (Theorem 12.2, pp. 255–257).
- In the random-walk example the smoother variance is below the filter variance everywhere except the last step (Fig. 12.2, p. 258). In car tracking, position RMSE falls from 0.43 (filter) to 0.27 (smoother) (Fig. 12.3, p. 260).
- The affine RTS smoother differs only in $\mathbf m^-_{k+1}=\mathbf A_k\mathbf m_k+\mathbf a_k$ (Theorem 12.5, p. 260).
- For discrete states the integrals become sums (Corollaries 12.6–12.7, p. 261).
- Viterbi gives the MAP trajectory by a forward recursion for $V_k$ and a backward argmax pass (Theorem 12.9, pp. 263–264). Maxima of smoothing marginals are not necessarily on the MAP path; for linear Gaussian models the book states that the two solutions always coincide (p. 263).

## L3 — Walkthrough

### 12.1 Bayesian smoothing equations (pp. 253–255)
Goal (fixed-interval smoothing, footnote p. 253): compute $p(\mathbf x_k\mid\mathbf y_{1:T})$ for $T>k$ \tag{12.1}. A filter uses $\mathbf y_{1:k}$ only; a smoother also uses future measurements (p. 253).

**Theorem 12.1.** For $k<T$, given the filtering distribution $p(\mathbf x_k\mid\mathbf y_{1:k})$ (p. 254):
$$p(\mathbf x_{k+1}\mid\mathbf y_{1:k})=\int p(\mathbf x_{k+1}\mid\mathbf x_k)\,p(\mathbf x_k\mid\mathbf y_{1:k})\,d\mathbf x_k,$$
$$p(\mathbf x_k\mid\mathbf y_{1:T})=p(\mathbf x_k\mid\mathbf y_{1:k})\int\left[\frac{p(\mathbf x_{k+1}\mid\mathbf x_k)\,p(\mathbf x_{k+1}\mid\mathbf y_{1:T})}{p(\mathbf x_{k+1}\mid\mathbf y_{1:k})}\right]d\mathbf x_{k+1}\tag{12.2}$$
The first line is the predicted distribution. Integrals become sums for discrete components (p. 254).

*Proof (p. 254).* By the Markov property, $\mathbf x_k$ is independent of $\mathbf y_{k+1:T}$ given $\mathbf x_{k+1}$. Hence $p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:T})=p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:k})$. Then
$$p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:T})=\frac{p(\mathbf x_k,\mathbf x_{k+1}\mid\mathbf y_{1:k})}{p(\mathbf x_{k+1}\mid\mathbf y_{1:k})}=\frac{p(\mathbf x_{k+1}\mid\mathbf x_k,\mathbf y_{1:k})\,p(\mathbf x_k\mid\mathbf y_{1:k})}{p(\mathbf x_{k+1}\mid\mathbf y_{1:k})}=\frac{p(\mathbf x_{k+1}\mid\mathbf x_k)\,p(\mathbf x_k\mid\mathbf y_{1:k})}{p(\mathbf x_{k+1}\mid\mathbf y_{1:k})}\tag{12.3}$$
$$p(\mathbf x_k,\mathbf x_{k+1}\mid\mathbf y_{1:T})=p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:T})\,p(\mathbf x_{k+1}\mid\mathbf y_{1:T})=\frac{p(\mathbf x_{k+1}\mid\mathbf x_k)\,p(\mathbf x_k\mid\mathbf y_{1:k})\,p(\mathbf x_{k+1}\mid\mathbf y_{1:T})}{p(\mathbf x_{k+1}\mid\mathbf y_{1:k})}\tag{12.4}$$
Integrating (or summing) over $\mathbf x_{k+1}$ gives (12.2) (p. 254).

*Intuition note.* Run the filter forward and store its results. Then go backward: the smoothed law at $k+1$ is pushed back through the transition, weighted by the ratio of the smoothed to the predicted density of $\mathbf x_{k+1}$, as in (12.2) (p. 254).

The method is forward-backward: filter forward, smooth backward (p. 255). The alternative **two-filter smoother** uses $p(\mathbf x_k\mid\mathbf y_{1:T})\propto p(\mathbf x_k\mid\mathbf y_{1:k-1})\,p(\mathbf y_{k:T}\mid\mathbf x_k)$. The second factor comes from a backward recursion. It is useful in linear Gaussian and discrete-state models, and belief propagation can be seen as an instance. It is less useful for approximate non-linear smoothers, so the book focuses on forward-backward (p. 255).

### 12.2 Rauch–Tung–Striebel smoother (pp. 255–260)
The RTSS (Kalman smoother) gives $p(\mathbf x_k\mid\mathbf y_{1:T})=\mathrm N(\mathbf x_k\mid\mathbf m^s_k,\mathbf P^s_k)$ \tag{12.5} for the linear model (6.17) (p. 255).

**Theorem 12.2.** With $\mathbf m_k,\mathbf P_k$ from the Kalman filter (state dimension $n$ assumed: $\mathbf A_k$, $\mathbf P_k$, $\mathbf G_k$ are $n\times n$; $\mathbf m_k$ is $n\times1$):
$$\begin{aligned}\mathbf m^-_{k+1}&=\mathbf A_k\mathbf m_k,\\ \mathbf P^-_{k+1}&=\mathbf A_k\mathbf P_k\mathbf A_k^{\mathsf T}+\mathbf Q_k,\\ \mathbf G_k&=\mathbf P_k\mathbf A_k^{\mathsf T}[\mathbf P^-_{k+1}]^{-1},\\ \mathbf m^s_k&=\mathbf m_k+\mathbf G_k[\mathbf m^s_{k+1}-\mathbf m^-_{k+1}],\\ \mathbf P^s_k&=\mathbf P_k+\mathbf G_k[\mathbf P^s_{k+1}-\mathbf P^-_{k+1}]\mathbf G_k^{\mathsf T}\end{aligned}\tag{12.6}$$
The first two lines are the Kalman prediction equations (p. 256). At $k=T$ smoothing and filtering coincide: $\mathbf m^s_T=\mathbf m_T$, $\mathbf P^s_T=\mathbf P_T$. The recursion runs from $k=T$ back to $k=0$ (p. 256). One may store $\mathbf m^-_k,\mathbf P^-_k$ from the filter and compute only $\mathbf G_k,\mathbf m^s_k,\mathbf P^s_k$ during smoothing (p. 257).

*Proof (pp. 256–257).* Lemma A.2 (used as cited; its text is not in this unit) gives the joint law:
$$p(\mathbf x_k,\mathbf x_{k+1}\mid\mathbf y_{1:k})=\mathrm N(\mathbf x_{k+1}\mid\mathbf A_k\mathbf x_k,\mathbf Q_k)\,\mathrm N(\mathbf x_k\mid\mathbf m_k,\mathbf P_k)=\mathrm N\!\left(\begin{pmatrix}\mathbf x_k\\\mathbf x_{k+1}\end{pmatrix}\Big|\,\tilde{\mathbf m}_1,\tilde{\mathbf P}_1\right)\tag{12.7}$$
$$\tilde{\mathbf m}_1=\begin{pmatrix}\mathbf m_k\\\mathbf A_k\mathbf m_k\end{pmatrix},\quad\tilde{\mathbf P}_1=\begin{pmatrix}\mathbf P_k&\mathbf P_k\mathbf A_k^{\mathsf T}\\\mathbf A_k\mathbf P_k&\mathbf A_k\mathbf P_k\mathbf A_k^{\mathsf T}+\mathbf Q_k\end{pmatrix}\tag{12.8}$$
The Markov property gives $p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:T})=p(\mathbf x_k\mid\mathbf x_{k+1},\mathbf y_{1:k})$ \tag{12.9}. Lemma A.3 then gives $\mathrm N(\mathbf x_k\mid\tilde{\mathbf m}_2,\tilde{\mathbf P}_2)$ \tag{12.10} with
$$\mathbf G_k=\mathbf P_k\mathbf A_k^{\mathsf T}(\mathbf A_k\mathbf P_k\mathbf A_k^{\mathsf T}+\mathbf Q_k)^{-1},\ \ \tilde{\mathbf m}_2=\mathbf m_k+\mathbf G_k(\mathbf x_{k+1}-\mathbf A_k\mathbf m_k),\ \ \tilde{\mathbf P}_2=\mathbf P_k-\mathbf G_k(\mathbf A_k\mathbf P_k\mathbf A_k^{\mathsf T}+\mathbf Q_k)\mathbf G_k^{\mathsf T}\tag{12.11}$$
Multiplying by the smoothed law of $\mathbf x_{k+1}$:
$$p(\mathbf x_{k+1},\mathbf x_k\mid\mathbf y_{1:T})=\mathrm N(\mathbf x_k\mid\tilde{\mathbf m}_2,\tilde{\mathbf P}_2)\,\mathrm N(\mathbf x_{k+1}\mid\mathbf m^s_{k+1},\mathbf P^s_{k+1})=\mathrm N\!\left(\begin{pmatrix}\mathbf x_{k+1}\\\mathbf x_k\end{pmatrix}\Big|\,\tilde{\mathbf m}_3,\tilde{\mathbf P}_3\right)\tag{12.12}$$
$$\tilde{\mathbf m}_3=\begin{pmatrix}\mathbf m^s_{k+1}\\\mathbf m_k+\mathbf G_k(\mathbf m^s_{k+1}-\mathbf A_k\mathbf m_k)\end{pmatrix},\quad\tilde{\mathbf P}_3=\begin{pmatrix}\mathbf P^s_{k+1}&\mathbf P^s_{k+1}\mathbf G_k^{\mathsf T}\\\mathbf G_k\mathbf P^s_{k+1}&\mathbf G_k\mathbf P^s_{k+1}\mathbf G_k^{\mathsf T}+\tilde{\mathbf P}_2\end{pmatrix}\tag{12.13}$$
The marginal of $\mathbf x_k$ (Lemma A.3) is $\mathrm N(\mathbf x_k\mid\mathbf m^s_k,\mathbf P^s_k)$ \tag{12.14} with
$$\mathbf m^s_k=\mathbf m_k+\mathbf G_k(\mathbf m^s_{k+1}-\mathbf A_k\mathbf m_k),\qquad\mathbf P^s_k=\mathbf P_k+\mathbf G_k(\mathbf P^s_{k+1}-\mathbf A_k\mathbf P_k\mathbf A_k^{\mathsf T}-\mathbf Q_k)\mathbf G_k^{\mathsf T}\tag{12.15}$$
(Added step: $\mathbf P^s_k$ is the lower-right block of $\tilde{\mathbf P}_3$, namely $\mathbf G_k\mathbf P^s_{k+1}\mathbf G_k^{\mathsf T}+\mathbf P_k-\mathbf G_k(\mathbf A_k\mathbf P_k\mathbf A_k^{\mathsf T}+\mathbf Q_k)\mathbf G_k^{\mathsf T}$. This equals (12.15).)

*Intuition note.* The smoothed mean is the filtered mean plus a correction. The correction is the gain $\mathbf G_k$ times the amount by which the smoothed next state differs from the prediction. If the smoothed next mean equals the prediction, the mean is not corrected.

**Example 12.3 (random walk, p. 258).** With the filter of Example 6.7:
$$m^-_{k+1}=m_k,\quad P^-_{k+1}=P_k+Q,\quad m^s_k=m_k+\frac{P_k}{P^-_{k+1}}(m^s_{k+1}-m^-_{k+1}),\quad P^s_k=P_k+\left(\frac{P_k}{P^-_{k+1}}\right)^2[P^s_{k+1}-P^-_{k+1}]\tag{12.16}$$
Fig. 12.2: smoother variance is always smaller than filter variance, except at the final step where they are equal (p. 258).

**Example 12.4 (car tracking, pp. 258–260).** The same equations apply to the model of Example 6.8. There $\mathbf A$ is the $4\times4$ matrix with $\Delta t$ in entries (1,3) and (2,4), and $\mathbf Q$ is built from $q^c_1,q^c_2$ and powers of $\Delta t$ (p. 259). Fig. 12.3 gives position RMSE of 0.77 from measurements alone, 0.43 for the filter and 0.27 for the smoother (p. 260).

### 12.3 Affine RTS smoother (pp. 259–260)
For affine models (6.34) the measurement model does not influence the smoother. The only change is the constant $\mathbf a_k$ in the prediction mean.

**Theorem 12.5.** Same as (12.6) except $\mathbf m^-_{k+1}=\mathbf A_k\mathbf m_k+\mathbf a_k$ \tag{12.17}. Here $\mathbf m_k,\mathbf P_k$ come from the affine Kalman filter and the start is $\mathbf m^s_T=\mathbf m_T$, $\mathbf P^s_T=\mathbf P_T$ (p. 260). The authors say it is included because it is useful later for non-linear smoothers (p. 259).

### 12.4 Smoother for discrete state spaces (p. 261)
**Corollary 12.6.** For $\mathbf x_k\in\mathbb X$ discrete, (12.2) holds with integrals replaced by sums over $\mathbb X$ \tag{12.18}.

With transition matrix $\boldsymbol\Pi$, emission matrix $\mathbf O$ (Eqs. 6.41) and $p^s_{j,k}=p(x_k=j\mid y_{1:T})$ \tag{12.19}:

**Corollary 12.7 (HMM smoother).**
$$p^-_{j,k+1}=\sum_i\Pi_{i,j}\,p_{i,k},\qquad p^s_{i,k}=p_{i,k}\sum_j\Pi_{i,j}\frac{p^s_{j,k+1}}{p^-_{j,k+1}}\tag{12.20}$$
(The printed left side of the second equation is $p^s_{j,k}$; see Reading notes.)

**Example 12.8** (Gilbert–Elliot channel): picking the most probable smoothed state gives an 8% error rate, against 11% for the filter (Example 6.12) (p. 262).

### 12.5 Viterbi algorithm (pp. 262–265)
The algorithm can be applied to discrete or continuous state or measurement spaces, but the most common practical use is when both are discrete (p. 262). Aim: the MAP trajectory
$$p(\mathbf x_{0:T}\mid\mathbf y_{1:T})\propto\ p(\mathbf y_{1:T},\mathbf x_{0:T})=p(\mathbf x_0)\prod_{i=1}^T[p(\mathbf y_i\mid\mathbf x_i)\,p(\mathbf x_i\mid\mathbf x_{i-1})],\qquad\mathbf x^*_{0:T}=\arg\max_{\mathbf x_{0:T}}p(\mathbf y_{1:T},\mathbf x_{0:T})\tag{12.21–12.23}$$
This differs from smoothing marginals. The maxima of the marginals are not necessarily the states on the MAP path. For discrete spaces both algorithms are therefore relevant. For linear Gaussian models the two solutions always coincide, so one algorithm suffices (p. 263).

**Theorem 12.9.** Forward pass: $V_0(\mathbf x_0)=p(\mathbf x_0)$ and, for $k=1,\dots,T$,
$$V_k(\mathbf x_k)=\max_{\mathbf x_{k-1}}[p(\mathbf y_k\mid\mathbf x_k)\,p(\mathbf x_k\mid\mathbf x_{k-1})\,V_{k-1}(\mathbf x_{k-1})]\tag{12.24}$$
Backward pass: $\mathbf x^*_T=\arg\max_{\mathbf x_T}V_T(\mathbf x_T)$ \tag{12.25}, then for $k=T-1,\dots,0$
$$\mathbf x^*_k=\arg\max_{\mathbf x_k}[p(\mathbf x^*_{k+1}\mid\mathbf x_k)\,V_k(\mathbf x_k)]\tag{12.26}$$
Any maximiser may be returned on ties (p. 263).

*Proof (pp. 263–264).* Claim: $V_k(\mathbf x_k)=\max_{\mathbf x_{0:k-1}}p(\mathbf x_0)\prod_{i=1}^k[p(\mathbf y_i\mid\mathbf x_i)p(\mathbf x_i\mid\mathbf x_{i-1})]$ \tag{12.27}. It holds trivially for $k=0$. Assume it for $k-1$; then (12.28) writes $V_k$ as a max over $\mathbf x_{k-1}$ of the new factors times the max over $\mathbf x_{0:k-2}$ of the old product. That inner max is $V_{k-1}(\mathbf x_{k-1})$, which gives (12.24). The case $k=T$ gives (12.25) from (12.27). For the backward pass, assume the MAP tail $\mathbf x^*_{k+1:T}$ is known. Then the problem is $\arg\max_{\mathbf x_{0:k}}p(\mathbf x^*_{k+1}\mid\mathbf x_k)\,p(\mathbf x_0)\prod_{i=1}^k[\cdots]$ \tag{12.29}. Maximising first over $\mathbf x_{0:k-1}$ gives $\mathbf x^*_k=\arg\max_{\mathbf x_k}p(\mathbf x^*_{k+1}\mid\mathbf x_k)V_k(\mathbf x_k)$ \tag{12.30}, which is (12.26).

*Intuition note.* $V_k(\mathbf x_k)$ is the largest value of the unnormalised joint $p(\mathbf y_{1:k},\mathbf x_{0:k})$ over paths that end in $\mathbf x_k$ (12.27). The backward pass picks $\mathbf x^*_k$ by maximising $p(\mathbf x^*_{k+1}\mid\mathbf x_k)\,V_k(\mathbf x_k)$, given the already chosen $\mathbf x^*_{k+1}$ (p. 263).

Links (p. 264): the forward pass resembles joint prediction and update, but $V_k$ is unnormalised and $\mathbf x_{k-1}$ is maximised out rather than summed out. The max-product algorithm can roughly be seen as a two-filter formulation of Viterbi.

**Corollary 12.10 (HMMs).** $V_{i,k}=V_k(x_k=i)$ \tag{12.31}; $V_{i,0}=p_{i,0}$;
$$V_{i,k}=\max_j[O_{i,y_k}\Pi_{j,i}V_{j,k-1}]\tag{12.32}$$
$$x^*_T=\arg\max_iV_{i,T},\qquad x^*_k=\arg\max_j[\Pi_{j,x^*_{k+1}}V_{j,k}]\tag{12.33}$$
**Example 12.11** (Gilbert–Elliot): Viterbi error rate is 8%, against 11% for the filter (p. 265).

## Toy example (ours)
Scalar random walk: $A=1$, $Q=1$, measurement noise $R=1$, $y=x+$ noise. Take the filter at $k=0$ as $m_0=0$, $P_0=1$, and observe $y_1=3$.
- Prediction: $m^-_1=0$, $P^-_1=1+1=2$.
- Filter update: $S=2+1=3$, $K=2/3$, $m_1=0+\tfrac23\cdot3=2$, $P_1=2-\tfrac23\cdot2=\tfrac23$.
- Here $T=1$, so $m^s_1=2$ and $P^s_1=\tfrac23$.
- Smoother gain: $G_0=P_0A/P^-_1=1/2$.
- $m^s_0=0+\tfrac12(2-0)=1$.
- $P^s_0=1+\tfrac14(\tfrac23-2)=1-\tfrac13=\tfrac23<1$.

Check by direct Gaussian conditioning: $y_1=x_0+w+v$ has variance $3$ and covariance $1$ with $x_0$. So the posterior mean is $\tfrac13\cdot3=1$ and the variance is $1-\tfrac13=\tfrac23$. The two results agree.

## Concepts
- [[bayesian-smoothing]] (new) — computing $p(\mathbf x_k\mid\mathbf y_{1:T})$ with $T>k$; here the fixed-interval type (p. 253)
- [[forward-backward-smoother]] (new) — run a filter forward, then recurse backward on smoothed distributions (p. 255)
- [[two-filter-smoother]] (new) — combines the prediction with $p(\mathbf y_{k:T}\mid\mathbf x_k)$ from a backward recursion (p. 255)
- [[rts-smoother]] (new) — closed-form Kalman smoother for linear Gaussian models (p. 255)
- [[kalman-filter]] — supplies $\mathbf m_k,\mathbf P_k$ and the prediction equations used by the smoother (p. 256)
- [[state-space-model]] — the linear (6.17) and affine (6.34) models the smoothers assume (pp. 255, 259)
- [[map-trajectory]] (new) — the single most probable whole state path, different from the marginal maxima (p. 263)
- [[viterbi-algorithm]] (new) — recursion for the MAP path: forward pass for $V_k$, backward argmax pass (p. 263)
- [[hidden-markov-model]] (new) — finite states and measurements with matrices $\boldsymbol\Pi$ and $\mathbf O$ (p. 261)

## Canonical instances
- [[gaussian-random-walk-smoothing]] — smoother variance below filter variance except at step $T$ (p. 258)
- [[car-tracking-rts]] — position RMSE 0.77 / 0.43 / 0.27 for measurements / filter / smoother (p. 260)
- [[gilbert-elliot-channel]] — smoother error 8%, Viterbi 8%, filter 11% (pp. 262, 265)

## Bridges (candidates)
- [same-math] RTS smoother ↔ control-theory: fixed-interval Kalman smoothing of a whole record offline. The book itself calls the RTS smoother the Kalman smoother (p. 255).
- [structural-analogy] Viterbi forward value $V_k$ ↔ control-theory: dynamic-programming value function and the principle of optimality. The backward argmax resembles reading off an optimal policy.
- [metaphor] Two-filter smoothing ↔ control-theory: duality of filtering and control. This is only a loose picture of a backward recursion complementing a forward one; the book makes no such link.

## Questions this raises
- When both are available, why use a smoother rather than a filter, and what does the extra delay cost in applications?
- Exercise 12.9 asks how Viterbi reduces to RTS in the linear Gaussian case. Why do marginal maxima and the MAP path then coincide?
- How are the same equations approximated when dynamics or measurements are non-linear (the book's later chapters)?
- How does smoothing relate to the joint Gaussian posterior over the whole trajectory?

## Exercises worth doing
- Ex. 12.2 (p. 266) — implement the random-walk smoother and compare with the Kalman filter — easy
- Ex. 12.3 (p. 266) — build the joint Gaussian posterior over $\mathbf x_{0:T}$ and check it matches the smoother means and variances — medium
- Ex. 12.5–12.6 (p. 266) — HMM smoother vs filter vs Viterbi error rates — medium
- Ex. 12.1 (p. 266) — derive the RTS smoother for non-zero-mean noise — medium
- Ex. 12.9 (p. 266) — show Viterbi reduces to RTS in the linear Gaussian case — hard

## Reading notes
- Printed page = pdf − 30.
- The text layer drops many symbols (e.g. "−", hats, Greek letters). I checked the equations against the page images.
- Eq. (12.21) is printed with "∝ p(y_{0:T}, x_{1:T})" on the right. The next line (12.22) suggests this should read $p(\mathbf y_{1:T},\mathbf x_{0:T})$. I wrote the latter.
- Eq. (12.20), second line: the image shows $p^s_{j,k}$ on the left but $j$ as the summation index. (12.18) indicates that the left side should be $p^s_{i,k}$. I wrote it that way.
- The text calls the Fig. 12.5 rate "filter rate"; I read it as filter error rate.
- Lemmas A.2 and A.3 are cited but not included in this unit.
