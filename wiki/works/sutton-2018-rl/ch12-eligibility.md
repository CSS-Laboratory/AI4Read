---
id: sutton-2018-rl/ch12-eligibility
work: sutton-2018-rl
unit: Chapter 12 — Eligibility Traces
pages: 287-320
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Eligibility Traces

## L0 — One line
An eligibility trace is a fading short-term memory vector that lets a TD learner spread each one-step TD error backward over recently visited states, giving an efficient, incremental, backward-view way to obtain, exactly or approximately, the effect of "forward-view" updates that average n-step returns, with Monte Carlo at one end and one-step TD at the other.

## L1 — The gist (≤ 120 words)
How can a learner use returns of every length n without storing n feature vectors or waiting for the episode to end? The chapter first defines the λ-return, a geometric average of n-step returns (a forward view). It then shows that TD(λ), with a trace, approximates this view. Next it presents true online TD(λ) (the derivation is left to the literature), which reproduces the ideal online λ-return algorithm exactly in the linear case. The same trace idea extends to action values (Sarsa(λ)), to variable λ and γ, and to off-policy learning, including stable off-policy variants. Empirically, an intermediate λ appears to be best. Traces cost more computation than one-step methods but offer significantly faster learning, particularly when rewards are delayed.

**Prerequisites:** TD(0) and the TD error; n-step returns and bootstrapping (Ch. 7); semi-gradient updates and linear function approximation (Ch. 9); importance sampling ratios; geometric series; matrix–vector products.

## L2 — Key ideas (5–10 bullets)
- **Forward and backward views.** A forward view updates a state from the future events that follow it. A backward view uses the current TD error and a trace over recently visited states. Backward views are cheaper to implement and can give the same or nearly the same updates (pp. 287–288).
- **λ-return.** It averages all n-step returns with weights $(1-\lambda)\lambda^{n-1}$. λ=0 gives one-step TD; λ=1 gives Monte Carlo (pp. 289–290).
- **TD(λ).** A trace $\mathbf z_t=\gamma\lambda\mathbf z_{t-1}+\nabla\hat v$ and the update $\mathbf w\leftarrow\mathbf w+\alpha\delta_t\mathbf z_t$ approximate the offline λ-return algorithm. They also work online and on continuing tasks. On the random walk, TD(λ) is much worse than the offline λ-return algorithm at large step sizes (pp. 292–295).
- **True online TD(λ).** For linear approximation, the "dutch trace" (the special trace of Eq. 12.11) gives an exact, O(d)-per-step implementation of the ideal online λ-return algorithm (p. 300).
- **Traces seem not to be specific to TD.** Linear Monte Carlo can be rewritten with a dutch trace and an auxiliary vector, giving the same final update with O(d) work per step (pp. 301–303).
- **Generalizations.** Sarsa(λ) extends traces to action values, state-dependent λ and γ generalize the returns, and the off-policy versions (per-decision importance sampling with control variates) are derived by one pattern: forward view, sum of TD errors, rearranged summation (pp. 303–313).
- **Stability.** Off-policy semi-gradient trace methods are not guaranteed stable. Gradient-TD and Emphatic-TD versions with traces (two families of methods built for off-policy stability) have stability guarantees (pp. 312, 314–316).
- **Practice.** An intermediate λ appears best; λ at or near 1 (nearly pure Monte Carlo) degrades sharply. Traces suit scarce data and delayed rewards (pp. 316–318).

## L3 — Walkthrough

### Introduction (pp. 287–288)
- Eligibility traces unify and generalize TD and Monte Carlo (MC) methods. Almost any TD method (Q-learning, Sarsa) can be combined with them (p. 287).
- The mechanism is a short-term memory vector $\mathbf z_t\in\mathbb R^d$ parallel to the long-term weight vector $\mathbf w_t\in\mathbb R^d$. When a weight component helps produce a value estimate, its trace component is bumped up and then fades. Learning occurs in that component if a nonzero TD error occurs before the trace falls back to zero. The trace-decay parameter is $\lambda\in[0,1]$ (p. 287).
- Advantages over n-step methods: one trace vector instead of the last n feature vectors; learning is continual and uniform in time; learning can affect behavior immediately (p. 287).
- **Forward view:** an update based on events after the state (MC, n-step TD). It is always somewhat complex to implement because it needs later data. **Backward view:** an algorithm that uses the current TD error and a trace over recently visited states. Sometimes the two give exactly the same updates, often nearly the same (p. 288).
- Order of the chapter: state values and prediction, then action values and control; on-policy, then off-policy. Linear approximation gets special attention, and tabular and state aggregation are special cases (p. 288).

### 12.1 The λ-return (pp. 288–291)
- General n-step return for a function approximator (12.1):
$$G_{t:t+n}\doteq R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^n\hat v(S_{t+n},\mathbf w_{t+n-1}),\quad 0\le t\le T-n.\tag{12.1}$$
- A valid update target can be any average of n-step returns, if the weights are positive and sum to 1. Example: $\tfrac12G_{t:t+2}+\tfrac12G_{t:t+4}$. The author says such a composite return has an error-reduction property similar to that of single n-step returns (p. 288).
- An update that averages simpler updates is a **compound update**. It can only be done when its longest component is complete, so one wants to limit that length (pp. 288–289).
- TD(λ) is one particular average. It contains all n-step returns, weighted $\propto\lambda^{n-1}$ and normalized by $1-\lambda$ (Fig. 12.1). The result is the **λ-return** (p. 289):
$$G^\lambda_t\doteq(1-\lambda)\sum_{n=1}^{\infty}\lambda^{n-1}G_{t:t+n}.\tag{12.2}$$
- The one-step return gets weight $1-\lambda$, the two-step $(1-\lambda)\lambda$, the three-step $(1-\lambda)\lambda^2$, and so on. After termination all n-step returns equal the conventional return $G_t$. Separating those terms (p. 290):
$$G^\lambda_t=(1-\lambda)\sum_{n=1}^{T-t-1}\lambda^{n-1}G_{t:t+n}+\lambda^{T-t-1}G_t.\tag{12.3}$$
- If λ=1 the main sum vanishes and the λ-return is $G_t$, a Monte Carlo update. If λ=0 it is $G_{t:t+1}$, one-step TD (p. 290).
- **Offline λ-return algorithm:** no weight change during the episode. At the end, for $t=0,\dots,T-1$ (p. 290):
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\big[G^\lambda_t-\hat v(S_t,\mathbf w_t)\big]\nabla\hat v(S_t,\mathbf w_t).\tag{12.4}$$
- On the 19-state random walk (Example 7.1), its performance is comparable to n-step TD. Both do best at an intermediate bootstrapping parameter. The λ-return algorithm is slightly better at the best α and λ and at high α (Fig. 12.3, p. 291). Error is RMS, averaged over the first 10 episodes and 19 states.
- This is the "theoretical" or forward view. We look forward from each state and, once it is updated, never have to work with it again (p. 291).

> **Intuition note.** Instead of picking one n, the λ-return mixes all n with geometrically shrinking weights. Small λ trusts the nearest bootstrap; large λ trusts actual rewards further out.

### 12.2 TD(λ) (pp. 292–295)
- TD(λ) was the first algorithm with a formal link between a forward view and a backward view with eligibility traces. Here the link is shown empirically (p. 292).
- TD(λ) improves on the offline λ-return algorithm in three ways: it updates every step, spreads computation evenly in time, and applies to continuing problems (p. 292).
- The trace is a short-term memory of the same size $d$ as $\mathbf w$. It is zeroed at episode start, incremented by the value gradient, and decays by $\gamma\lambda$ (p. 292):
$$\mathbf z_{-1}\doteq\mathbf 0,\qquad \mathbf z_t\doteq\gamma\lambda\mathbf z_{t-1}+\nabla\hat v(S_t,\mathbf w_t),\quad 0\le t\le T.\tag{12.5}$$
- In the linear case $\nabla\hat v=\mathbf x_t$, so the trace is a sum of past, fading feature vectors (p. 292).
- With the TD error and the update (p. 293):
$$\delta_t\doteq R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_t),\tag{12.6}$$
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\,\delta_t\,\mathbf z_t.\tag{12.7}$$
- Shapes: $\mathbf w,\mathbf z,\mathbf x\in\mathbb R^d$; $\delta_t$ is a scalar. Pseudocode: per step, $\mathbf z\leftarrow\gamma\lambda\mathbf z+\nabla\hat v(S,\mathbf w)$, $\delta\leftarrow R+\gamma\hat v(S',\mathbf w)-\hat v(S,\mathbf w)$, $\mathbf w\leftarrow\mathbf w+\alpha\delta\mathbf z$ (p. 293).
- Backward view: the current TD error is "shouted back" to earlier states in proportion to their traces (Fig. 12.5, p. 294).
- λ=0: the trace equals the current gradient, so TD(λ) reduces to one-step semi-gradient TD (the reason it is called TD(0)). For $0<\lambda<1$, more earlier states are updated, each less than the later one, because they get less "credit" (p. 294).
- λ=1: credit falls only by γ per step. This is right for MC behavior, because $\delta_t$ contains an undiscounted $R_{t+1}$, which passed back $k$ steps needs a factor $\gamma^k$. With λ=1 and γ=1 the traces do not decay and the method behaves like MC for an undiscounted episodic task (p. 294).
- TD(1) implements MC more generally than earlier MC. It applies to discounted continuing tasks and runs incrementally and online. It can learn mid-episode, so behavior can change in the same episode (p. 294).
- Fig. 12.6 (19-state walk): for each λ, if α is optimal or smaller, TD(λ) and the offline λ-return algorithm perform virtually identically. At larger α, the λ-return algorithm is only a little worse while TD(λ) is much worse and may be unstable (p. 294).
- Convergence: linear TD(λ) has been proved to converge on-policy if the step size is reduced over time under the usual conditions (2.7). It converges to a nearby weight vector that depends on λ, not to the minimum-error one (p. 295). For the continuing discounted case:
$$\overline{\mathrm{VE}}(\mathbf w_\infty)\le\frac{1-\gamma\lambda}{1-\gamma}\min_{\mathbf w}\overline{\mathrm{VE}}(\mathbf w).\tag{12.8}$$
  The bound approaches the minimum error as λ→1 and is loosest at λ=0. In practice λ=1 is often the poorest choice (Fig. 12.14) (p. 295).

> **Intuition note.** TD(λ) does cheaply what the λ-return does expensively: each reward's information reaches earlier states through traces instead of through stored future data. The price is that, with large α, the one-pass trace version is less robust than the ideal.

### 12.3 n-step truncated λ-return methods (pp. 295–297)
- The λ-return is unknown until the episode ends, and in continuing tasks it is technically never known. But the dependence on distant rewards falls by $\gamma\lambda$ per step, so one can truncate at a horizon $h$ (p. 296):
$$G^\lambda_{t:h}\doteq(1-\lambda)\sum_{n=1}^{h-t-1}\lambda^{n-1}G_{t:t+n}+\lambda^{h-t-1}G_{t:h},\quad 0\le t<h\le T.\tag{12.9}$$
- The horizon $h$ plays the role of $T$. The residual weight goes to the longest available return $G_{t:h}$ (p. 296).
- Truncated TD(λ), TTD(λ): updates are delayed n steps and use all k-step returns for $1\le k\le n$. Its update is $\mathbf w_{t+n}\doteq\mathbf w_{t+n-1}+\alpha[G^\lambda_{t:t+n}-\hat v(S_t,\mathbf w_{t+n-1})]\nabla\hat v(S_t,\mathbf w_{t+n-1})$, $0\le t<T$ (p. 297).
- Per-step computation need not scale with n, though memory does. No updates occur on the first $n-1$ steps, and $n-1$ extra updates occur at termination (p. 297).
- Efficient implementation uses an exact identity (12.10), with $\delta'_t\doteq R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_{t-1})$:
$$G^\lambda_{t:t+k}=\hat v(S_t,\mathbf w_{t-1})+\sum_{i=t}^{t+k-1}(\gamma\lambda)^{i-t}\delta'_i.\tag{12.10}$$

### 12.4 Redoing updates: online λ-return algorithm (pp. 297–299)
- Trade-off: n should be large (to approximate the offline λ-return) and small (so updates come sooner). The idea: as each new data step arrives, redo all updates since the episode start, with the latest horizon (p. 297).
- Procedure: weights start at $\mathbf w_0$ (from the previous episode). At horizon 1, use $G_{0:1}$ to get $\mathbf w_1$. At horizon 2, redo the updates for $S_0$ and $S_1$ from $\mathbf w_0$, using better targets $G^\lambda_{0:2}$ and $G^\lambda_{1:2}$, to get $\mathbf w_2$. And so on (p. 298).
- Notation: $\mathbf w^h_t$ is the weight used at time $t$ in the sequence for horizon $h$. $\mathbf w^h_0$ is the inherited weight, the same for all $h$. The final weights $\mathbf w^T_T$ start the next episode (p. 298).
- First sequences: $h=1$: $\mathbf w^1_1\doteq\mathbf w^1_0+\alpha[G^\lambda_{0:1}-\hat v(S_0,\mathbf w^1_0)]\nabla\hat v(S_0,\mathbf w^1_0)$. For $h=2$ and $h=3$ the same form is applied successively to $S_0,S_1,(S_2)$ (p. 298).
- General form, with $\mathbf w_t\doteq\mathbf w^t_t$ (p. 298):
$$\mathbf w^h_{t+1}\doteq\mathbf w^h_t+\alpha\big[G^\lambda_{t:h}-\hat v(S_t,\mathbf w^h_t)\big]\nabla\hat v(S_t,\mathbf w^h_t),\quad 0\le t<h\le T.$$
- It is fully online but computationally complex (strictly more than the offline version). It can be expected to perform better, during the episode and at its end, because bootstrapping uses weights with more informative updates. Fig. 12.8 shows it is "subtly better" in VE at episode end (pp. 298–299).

### 12.5 True online TD(λ) (pp. 299–301)
- The online λ-return algorithm is described as the best-performing TD algorithm at present, an ideal that TD(λ) only approximates (p. 299).
- For linear $\hat v=\mathbf w^\top\mathbf x$, an exact, efficient backward implementation exists. The derivation is not given (it is in van Seijen et al., 2016). The strategy: arrange the weights in a triangle ($\mathbf w^0_0$; $\mathbf w^1_0,\mathbf w^1_1$; …; $\mathbf w^T_0,\dots,\mathbf w^T_T$). Only the diagonal $\mathbf w^t_t$ is needed, and one computes each from the previous diagonal entry (pp. 299–300).
- Result, with $\mathbf x_t\doteq\mathbf x(S_t)$, $\delta_t$ from (12.6) (p. 300):
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\delta_t\mathbf z_t+\alpha(\mathbf w_t^\top\mathbf x_t-\mathbf w_{t-1}^\top\mathbf x_t)(\mathbf z_t-\mathbf x_t),$$
$$\mathbf z_t\doteq\gamma\lambda\mathbf z_{t-1}+\big(1-\alpha\gamma\lambda\mathbf z_{t-1}^\top\mathbf x_t\big)\mathbf x_t.\tag{12.11}$$
- It is proven to give exactly the same weight sequence as the online λ-return algorithm. Memory equals that of TD(λ). Per-step computation rises about 50% (one more inner product), still $O(d)$ (p. 300).
- Pseudocode keeps a scalar $V_{old}$: $V\leftarrow\mathbf w^\top\mathbf x$, $V'\leftarrow\mathbf w^\top\mathbf x'$, $\delta\leftarrow R+\gamma V'-V$, update $\mathbf z$ by (12.11), $\mathbf w\leftarrow\mathbf w+\alpha(\delta+V-V_{old})\mathbf z-\alpha(V-V_{old})\mathbf x$, $V_{old}\leftarrow V'$ (p. 300).
- (12.11) is a **dutch trace**; (12.5) is an **accumulating trace**. A third kind, the **replacing trace**, is defined only for the tabular or binary-feature case, component by component (p. 301):
$$z_{i,t}\doteq\begin{cases}1&\text{if }x_{i,t}=1\\ \gamma\lambda z_{i,t-1}&\text{otherwise.}\end{cases}\tag{12.12}$$
- Replacing traces are now seen as crude approximations to dutch traces. Dutch usually perform better and have a clearer theory. Accumulating traces remain of interest for nonlinear approximation, where dutch traces are not available (p. 301).

> **Intuition note.** Redoing all past updates at every step is the ideal but impractical. The dutch trace is a compact summary that makes one cheap update per step land on exactly the same weights in the linear case.

### 12.6 *Dutch traces in Monte Carlo learning (pp. 301–303)
- The author states that eligibility traces "have nothing to do" with TD ("in fact"): they arise even in MC learning. This is the only forward/backward equivalence derived explicitly in the book (p. 301).
- Setup: linear gradient MC with $G$ a single reward at episode end and no discounting (the LMS rule). The offline updates (p. 301):
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\big[G-\mathbf w_t^\top\mathbf x_t\big]\mathbf x_t,\quad 0\le t<T.\tag{12.13}$$
- Aim: weights still change only at episode end, but with O(d) computation per step, and without storing the feature vectors. Derivation (p. 302), with the forgetting matrix $\mathbf F_t\doteq\mathbf I-\alpha\mathbf x_t\mathbf x_t^\top\in\mathbb R^{d\times d}$:
  - $\mathbf w_T=\mathbf w_{T-1}+\alpha(G-\mathbf w_{T-1}^\top\mathbf x_{T-1})\mathbf x_{T-1}=(\mathbf I-\alpha\mathbf x_{T-1}\mathbf x_{T-1}^\top)\mathbf w_{T-1}+\alpha G\mathbf x_{T-1}=\mathbf F_{T-1}\mathbf w_{T-1}+\alpha G\mathbf x_{T-1}$.
  - Recursing: $=\mathbf F_{T-1}\mathbf F_{T-2}\mathbf w_{T-2}+\alpha G(\mathbf F_{T-1}\mathbf x_{T-2}+\mathbf x_{T-1})$, and so on, down to
$$\mathbf w_T=\underbrace{\mathbf F_{T-1}\cdots\mathbf F_0\mathbf w_0}_{\mathbf a_{T-1}}+\alpha G\underbrace{\sum_{k=0}^{T-1}\mathbf F_{T-1}\mathbf F_{T-2}\cdots\mathbf F_{k+1}\mathbf x_k}_{\mathbf z_{T-1}}=\mathbf a_{T-1}+\alpha G\mathbf z_{T-1}.\tag{12.14}$$
- $\mathbf a_t$ and $\mathbf z_t$ can be updated incrementally without knowing $G$. The trace is $\mathbf z_0=\mathbf x_0$ and, for $1\le t<T$:
  $\mathbf z_t\doteq\sum_{k=0}^t\mathbf F_t\cdots\mathbf F_{k+1}\mathbf x_k=\mathbf F_t\sum_{k=0}^{t-1}\mathbf F_{t-1}\cdots\mathbf F_{k+1}\mathbf x_k+\mathbf x_t=\mathbf F_t\mathbf z_{t-1}+\mathbf x_t=\mathbf z_{t-1}-\alpha\mathbf x_t\mathbf x_t^\top\mathbf z_{t-1}+\mathbf x_t=\mathbf z_{t-1}+(1-\alpha\mathbf z_{t-1}^\top\mathbf x_t)\mathbf x_t$
  (p. 302). This is the dutch trace of (12.11) with $\gamma\lambda=1$.
- $\mathbf a_t\doteq\mathbf F_t\cdots\mathbf F_0\mathbf w_0=\mathbf F_t\mathbf a_{t-1}=\mathbf a_{t-1}-\alpha\mathbf x_t\mathbf x_t^\top\mathbf a_{t-1}$, $1\le t<T$ (p. 302).
- At time $T$, when $G$ is known, (12.14) gives exactly the MC/LMS result with O(d) time and memory per step. The author says it seems traces are not specific to TD and that the need for them seems to arise "whenever one tries to learn long-term predictions in an efficient manner" (p. 303).

> **Intuition note.** The final MC weight is "old weights shrunk by the forgetting matrices" plus "$G$ times a summary of all inputs, each shrunk by later forgetting". Only the summary $\mathbf z$ must be kept, so no feature vectors are stored.

### 12.7 Sarsa(λ) (pp. 303–307)
- Action-value n-step return: $G_{t:t+n}\doteq R_{t+1}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^n\hat q(S_{t+n},A_{t+n},\mathbf w_{t+n-1})$ for $t+n<T$, and $G_t$ if $t+n\ge T$. The offline λ-return update is (12.4) with $\hat q$ (p. 303):
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\big[G^\lambda_t-\hat q(S_t,A_t,\mathbf w_t)\big]\nabla\hat q(S_t,A_t,\mathbf w_t).\tag{12.15}$$
- Sarsa(λ) approximates it with $\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\delta_t\mathbf z_t$, where
$$\delta_t\doteq R_{t+1}+\gamma\hat q(S_{t+1},A_{t+1},\mathbf w_t)-\hat q(S_t,A_t,\mathbf w_t),\tag{12.16}$$
  and $\mathbf z_{-1}\doteq\mathbf 0$, $\mathbf z_t\doteq\gamma\lambda\mathbf z_{t-1}+\nabla\hat q(S_t,A_t,\mathbf w_t)$ (p. 303).
- Pseudocode (binary features, linear): for each active feature $i$, $\delta\leftarrow\delta-w_i$ and $z_i\leftarrow z_i+1$ (accumulating) or $z_i\leftarrow1$ (replacing). After choosing $A'$, $\delta\leftarrow\delta+\gamma w_i$ for active features of $(S',A')$. Then $\mathbf w\leftarrow\mathbf w+\alpha\delta\mathbf z$, $\mathbf z\leftarrow\gamma\lambda\mathbf z$ (p. 305).
- **Example 12.1 (gridworld).** One episode, all rewards zero except at goal G, values initially zero. On reaching G, one-step Sarsa increments only the last action value. An n-step method (here 10-step; γ=1) increments the last n actions equally. Sarsa(λ) with λ=0.9 updates all action values back to the episode start, fading with recency. "The fading strategy is often the best" (p. 304).
- **Example 12.2 (Mountain Car).** Sarsa(λ) with replacing traces, compared with n-step Sarsa from Chapter 10 (same setup). Fading-trace bootstrapping "appears to result in more efficient learning" (Fig. 12.10, p. 305).
- The online λ-return algorithm and true online TD(λ) carry over to action values with $\mathbf x_t=\mathbf x(S_t,A_t)$. This gives true online Sarsa(λ) (pseudocode, p. 307). Fig. 12.11 (Mountain Car, first 20 episodes): true online Sarsa(λ) did better than Sarsa(λ) with accumulating or replacing traces (p. 306).
- Forward Sarsa(λ) (van Seijen, 2016) is a truncated version that appears particularly effective with multi-layer neural networks (p. 307).

### 12.8 Variable λ and γ (pp. 307–308)
- Make λ and γ functions: $\lambda:\mathcal S\times\mathcal A\to[0,1]$, $\lambda_t\doteq\lambda(S_t,A_t)$; $\gamma:\mathcal S\to[0,1]$, $\gamma_t\doteq\gamma(S_t)$. γ is now the **termination function** (p. 307).
- General return, requiring $\prod_{k=t}^\infty\gamma_k=0$ with probability one for all $t$ (p. 308):
$$G_t\doteq R_{t+1}+\gamma_{t+1}G_{t+1}=\sum_{k=t}^{\infty}\Big(\prod_{i=t+1}^{k}\gamma_i\Big)R_{k+1}.\tag{12.17}$$
- An old terminal state becomes a state with $\gamma(s)=0$ that transitions to the start distribution. This recovers the episodic setting from one stream of experience. State-dependent termination also covers "pseudo termination" (predicting a quantity without changing the process), and unifies episodic and discounted-continuing cases. Undiscounted-continuing still needs special treatment (p. 308).
- Variable λ is a change in solution strategy, not in the problem. State-based λ-return (12.18) and action-based forms (Sarsa form 12.19, Expected Sarsa form 12.20) (p. 308):
$$G^{\lambda s}_t\doteq R_{t+1}+\gamma_{t+1}\big((1-\lambda_{t+1})\hat v(S_{t+1},\mathbf w_t)+\lambda_{t+1}G^{\lambda s}_{t+1}\big),\tag{12.18}$$
$$G^{\lambda a}_t\doteq R_{t+1}+\gamma_{t+1}\big((1-\lambda_{t+1})\hat q(S_{t+1},A_{t+1},\mathbf w_t)+\lambda_{t+1}G^{\lambda a}_{t+1}\big),\tag{12.19}$$
$$G^{\lambda a}_t\doteq R_{t+1}+\gamma_{t+1}\big((1-\lambda_{t+1})\bar V_t(S_{t+1})+\lambda_{t+1}G^{\lambda a}_{t+1}\big),\tag{12.20}$$
  with $\bar V_t(s)\doteq\sum_a\pi(a|s)\hat q(s,a,\mathbf w_t)$ (12.21).
- Reading of (12.18): the first reward is unaffected. The rest counts only to the extent we are not terminating (via $\gamma_{t+1}$). Within that, the term is the estimated value to the extent we bootstrap, and the next λ-return otherwise (p. 308).

### 12.9 Off-policy traces with control variates (pp. 309–312)
- For non-truncated λ-returns there is no practical option of weighting the whole target by importance sampling (as in n-step methods, Section 7.3). Instead the text uses per-decision importance sampling with control variates (Section 7.4). With $\rho_t=\pi(A_t|S_t)/b(A_t|S_t)$ (p. 309):
$$G^{\lambda s}_t\doteq\rho_t\Big(R_{t+1}+\gamma_{t+1}\big((1-\lambda_{t+1})\hat v(S_{t+1},\mathbf w_t)+\lambda_{t+1}G^{\lambda s}_{t+1}\big)\Big)+(1-\rho_t)\hat v(S_t,\mathbf w_t).\tag{12.22}$$
- With $\delta^s_t\doteq R_{t+1}+\gamma_{t+1}\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_t)$ (12.23):
$$G^{\lambda s}_t\approx\hat v(S_t,\mathbf w_t)+\rho_t\sum_{k=t}^\infty\delta^s_k\prod_{i=t+1}^{k}\gamma_i\lambda_i\rho_i,\tag{12.24}$$
  and the approximation becomes exact if the value function does not change (p. 309).
- Forward-view update: $\mathbf w_{t+1}=\mathbf w_t+\alpha(G^{\lambda s}_t-\hat v(S_t,\mathbf w_t))\nabla\hat v(S_t,\mathbf w_t)\approx\mathbf w_t+\alpha\rho_t\big(\sum_{k\ge t}\delta^s_k\prod_{i=t+1}^k\gamma_i\lambda_i\rho_i\big)\nabla\hat v(S_t,\mathbf w_t)$ (p. 309).
- Summed over time (approximate because value changes are ignored), using the summation swap $\sum_{t=x}^y\sum_{k=t}^y=\sum_{k=x}^y\sum_{t=x}^k$ (p. 310):
$$\sum_{t=0}^\infty(\mathbf w_{t+1}-\mathbf w_t)\approx\sum_{k=0}^\infty\alpha\delta^s_k\sum_{t=0}^k\rho_t\nabla\hat v(S_t,\mathbf w_t)\prod_{i=t+1}^k\gamma_i\lambda_i\rho_i.$$
- If $\mathbf z_k\doteq\sum_{t=0}^k\rho_t\nabla\hat v(S_t,\mathbf w_t)\prod_{i=t+1}^k\gamma_i\lambda_i\rho_i$, split off the $t=k$ term and factor out $\gamma_k\lambda_k\rho_k$ from the rest:
  $\mathbf z_k=\gamma_k\lambda_k\rho_k\,\mathbf z_{k-1}+\rho_k\nabla\hat v(S_k,\mathbf w_k)=\rho_k(\gamma_k\lambda_k\mathbf z_{k-1}+\nabla\hat v(S_k,\mathbf w_k))$. Renaming the index (p. 310):
$$\mathbf z_t\doteq\rho_t\big(\gamma_t\lambda_t\mathbf z_{t-1}+\nabla\hat v(S_t,\mathbf w_t)\big).\tag{12.25}$$
- With (12.7) this is a general TD(λ) for on- or off-policy data. On-policy $\rho_t=1$, so it is exactly TD(λ). Off-policy it often works well but, as a semi-gradient method, is not guaranteed stable (p. 310).
- Action values, Expected Sarsa form (after Eq. 7.14), where the second line combines the two terms (p. 311):
$$G^{\lambda a}_t\doteq R_{t+1}+\gamma_{t+1}\Big(\bar V_t(S_{t+1})+\lambda_{t+1}\rho_{t+1}\big[G^{\lambda a}_{t+1}-\hat q(S_{t+1},A_{t+1},\mathbf w_t)\big]\Big),\tag{12.26}$$
$$G^{\lambda a}_t\approx\hat q(S_t,A_t,\mathbf w_t)+\sum_{k=t}^\infty\delta^a_k\prod_{i=t+1}^k\gamma_i\lambda_i\rho_i,\tag{12.27}$$
  with $\delta^a_t\doteq R_{t+1}+\gamma_{t+1}\bar V_t(S_{t+1})-\hat q(S_t,A_t,\mathbf w_t)$ (12.28). Exact if the value function does not change.
- Analogous steps give the trace (12.29) and the Expected Sarsa(λ) algorithm:
$$\mathbf z_t\doteq\gamma_t\lambda_t\rho_t\mathbf z_{t-1}+\nabla\hat q(S_t,A_t,\mathbf w_t).\tag{12.29}$$
  It is "probably the best algorithm of this type at the current time", though not stable until combined with a method of 12.11. In the on-policy case with constant λ and γ, and with the usual state–action TD error (12.16) in place of the expectation form, it would be identical to Sarsa(λ) of Section 12.7 (p. 311).
- At λ=1 these algorithms are closely related to MC. One might expect exact equivalence for episodic problems with off-line updating, but even under these most favorable conditions it holds only in expectation, not episode by episode. They make irrevocable updates as a trajectory unfolds, while true MC would make no update if an action has zero target-policy probability. They still bootstrap, though the dependence cancels in expected value (pp. 311–312).
- PTD(λ) and PQ(λ) (Sutton, Mahmood, Precup, van Hasselt, 2014) achieve exact equivalence using "provisional weights" that may be retracted or emphasized later. Practical consequences are not yet established. High variance is expected, as with all importance-sampling methods (p. 312).
- For λ<1 these off-policy algorithms bootstrap, so the deadly triad applies. They can be guaranteed stable only for tabular, state aggregation and limited approximators. Off-policy traces fix the first part of the off-policy challenge (the expected value of targets), not the second (the distribution of updates) (p. 312).

> **Intuition note.** The importance ratio $\rho$ simply enters the trace: if the behavior policy takes an action the target policy would never take ($\rho=0$), the trace is cut and past credit stops flowing.

### 12.10 Watkins's Q(λ) to Tree-Backup(λ) (pp. 312–314)
- Watkins's Q(λ) decays traces as usual while greedy actions are taken, then cuts them to zero after the first non-greedy action (Fig. 12.12, p. 312).
- Tree-Backup(λ), TB(λ), weights tree-backup updates (Section 7.5) by λ as usual. It is arguably the true successor to Q-learning because it keeps the absence of importance sampling (p. 312). Starting from (12.20) and expanding after (7.16) (p. 313):
$$G^{\lambda a}_t=R_{t+1}+\gamma_{t+1}\Big(\bar V_t(S_{t+1})+\lambda_{t+1}\pi(A_{t+1}|S_{t+1})\big(G^{\lambda a}_{t+1}-\hat q(S_{t+1},A_{t+1},\mathbf w_t)\big)\Big).$$
- Approximately $G^{\lambda a}_t\approx\hat q(S_t,A_t,\mathbf w_t)+\sum_{k\ge t}\delta^a_k\prod_{i=t+1}^k\gamma_i\lambda_i\pi(A_i|S_i)$, giving the trace
  $\mathbf z_t\doteq\gamma_t\lambda_t\pi(A_t|S_t)\mathbf z_{t-1}+\nabla\hat q(S_t,A_t,\mathbf w_t)$ (p. 313). With (12.7) this defines TB(λ). Like all semi-gradient methods it is not guaranteed stable off-policy with powerful approximators (p. 314).

### 12.11 Stable off-policy methods with traces (pp. 314–316)
All four assume linear approximation and build on Gradient-TD or Emphatic-TD (p. 314). Each has a second step size β>0 where noted.
- **GTD(λ)** (analogue of TDC; learns $\mathbf w^\top\mathbf x(s)\approx v_\pi$ from data of policy $b$):
  $\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\delta^s_t\mathbf z_t-\alpha\gamma_{t+1}(1-\lambda_{t+1})(\mathbf z_t^\top\mathbf v_t)\mathbf x_{t+1}$, and (12.30) $\mathbf v_{t+1}\doteq\mathbf v_t+\beta\delta^s_t\mathbf z_t-\beta(\mathbf v_t^\top\mathbf x_t)\mathbf x_t$, $\mathbf v_0=\mathbf 0$ (pp. 314–315).
- **GQ(λ)** (action values; can be a control algorithm if the target policy is ε-greedy or similarly biased toward greedy): $\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\delta^a_t\mathbf z_t-\alpha\gamma_{t+1}(1-\lambda_{t+1})(\mathbf z_t^\top\mathbf v_t)\bar{\mathbf x}_{t+1}$, with $\bar{\mathbf x}_t\doteq\sum_a\pi(a|S_t)\mathbf x(S_t,a)$ and $\delta^a_t\doteq R_{t+1}+\gamma_{t+1}\mathbf w_t^\top\bar{\mathbf x}_{t+1}-\mathbf w_t^\top\mathbf x_t$. $\mathbf z_t$ is from (12.29) and $\mathbf v_t$ as in (12.30) (p. 315).
- **HTD(λ)**: a hybrid state-value method that strictly generalizes TD(λ) off-policy. If behavior = target policy it becomes TD(λ), which is not true of GTD(λ) (p. 315):
  $\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\delta^s_t\mathbf z_t+\alpha((\mathbf z_t-\mathbf z^b_t)^\top\mathbf v_t)(\mathbf x_t-\gamma_{t+1}\mathbf x_{t+1})$;
  $\mathbf v_{t+1}\doteq\mathbf v_t+\beta\delta^s_t\mathbf z_t-\beta(\mathbf z^{b\top}_t\mathbf v_t)(\mathbf x_t-\gamma_{t+1}\mathbf x_{t+1})$;
  $\mathbf z_t\doteq\rho_t(\gamma_t\lambda_t\mathbf z_{t-1}+\mathbf x_t)$; $\mathbf z^b_t\doteq\gamma_t\lambda_t\mathbf z^b_{t-1}+\mathbf x_t$. The traces and $\mathbf v$ start at zero ($\mathbf v_0=\mathbf z_{-1}=\mathbf z^b_{-1}=\mathbf 0$). If all $\rho_t=1$, then $\mathbf z^b_t=\mathbf z_t$ and the extra term vanishes (p. 315).
- **Emphatic TD(λ)**: keeps strong off-policy convergence guarantees with any degree of bootstrapping, at the cost of high variance and potentially slow convergence (pp. 315–316):
  $\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\delta_t\mathbf z_t$; $\delta_t\doteq R_{t+1}+\gamma_{t+1}\mathbf w_t^\top\mathbf x_{t+1}-\mathbf w_t^\top\mathbf x_t$; $\mathbf z_t\doteq\rho_t(\gamma_t\lambda_t\mathbf z_{t-1}+M_t\mathbf x_t)$; $M_t\doteq\lambda_tI_t+(1-\lambda_t)F_t$; $F_t\doteq\rho_{t-1}\gamma_tF_{t-1}+I_t$, with $\mathbf z_{-1}=\mathbf 0$ and $F_0\doteq i(S_0)$.
  Here $M_t\ge0$ is the emphasis, $F_t\ge0$ the followon trace, $I_t\ge0$ the interest. On-policy, Emphatic-TD(λ) is guaranteed to converge for all state-dependent λ functions, whereas TD(λ) is guaranteed convergent only for all constant λ (Yu's counterexample) (p. 316).

### 12.12 Implementation issues (p. 316)
- A naive tabular implementation updates every state's value and trace each step. This is fine on parallel hardware or neural networks, but a problem on serial computers. For typical λ and γ, almost all traces are nearly zero, so only the few recently visited states need updating. The cost is then typically just a few times that of a one-step method (p. 316).
- The tabular case is in a sense the worst case. With neural networks and backpropagation, traces generally only double memory and computation per step. Truncated λ-return methods can be efficient but always need extra memory (p. 316).

### 12.13 Conclusions (p. 317–318)
- Traces plus TD errors give an efficient, incremental way to move between MC and TD. They are more general than n-step methods, often faster, with different complexity trade-offs. True online methods reproduce expensive ideal methods exactly (p. 317).
- Because they make TD more like MC, traces can also have advantages in partially non-Markov tasks: "Eligibility traces are the first line of defense against both long-delayed rewards and non-Markov tasks." (p. 317).
- Where to put λ: no good theory yet, but a clear empirical answer "appears to be emerging": on tasks with many steps per episode (or many steps within the discount half-life), it appears significantly better to use traces than not. Pure or near-MC traces degrade sharply, and an intermediate mixture appears to be the best choice: "Eligibility traces should be used to bring us toward Monte Carlo methods, but not all the way there." (p. 317). Fig. 12.14 (Mountain Car, random walk, Puddle World, cart-pole) shows performance generally best at an intermediate λ (p. 318).
- Traces cost more computation but offer significantly faster learning, particularly when rewards are delayed, so it often makes sense to use them when data are scarce and cannot be repeatedly processed (typical online). For cheap simulated data, one-step methods are usually favored (p. 317).
- Bibliographical remarks (pp. 319–320) give credit: traces entered RL through Klopf (1972); the λ-return to Watkins (1989); TD(λ) to Sutton (1988, 1984); true online TD(λ) and dutch traces to van Seijen and van Hasselt; the Expected Sarsa(λ) of 12.9 is stated by the authors not to have been previously described or tested, to their knowledge (p. 320).

## Toy example (ours, not from the text)
Tabular chain: states A→B→C→terminal. γ=1, λ=0.5, α=0.1. All values start at 0. Reward is 0, 0, then 1 on the last step. With tabular one-hot features, $\nabla\hat v$ is a unit vector. Trace entries are listed in the order (A,B,C).

- Step 1 (at A→B, R=0): $\mathbf z=0.5\cdot(0,0,0)+(1,0,0)=(1,0,0)$. $\delta=0+0-0=0$, so $\mathbf w$ is unchanged.
- Step 2 (B→C, R=0): $\mathbf z=0.5\cdot(1,0,0)+(0,1,0)=(0.5,1,0)$. $\delta=0$, so $\mathbf w$ is unchanged.
- Step 3 (C→terminal, R=1, $\hat v(\text{terminal})=0$): $\mathbf z=0.5\cdot(0.5,1,0)+(0,0,1)=(0.25,0.5,1)$. $\delta=1+0-0=1$. $\mathbf w=\mathbf 0+0.1\cdot1\cdot(0.25,0.5,1)=(0.025,0.05,0.1)$.

Check against the forward view (12.3). Here $T=3$ and $\mathbf w$ stays $\mathbf 0$ until step 3, so the offline λ-return updates use the same weights. All n-step returns before termination are 0, so $G^\lambda_t=\lambda^{T-t-1}G_t$ with $G_t=1$:
- A ($t=0$): $\lambda^2=0.25$, update $0.1\cdot0.25=0.025$ ✓.
- B ($t=1$): $\lambda^1=0.5$, update $0.05$ ✓.
- C ($t=2$): $\lambda^0=1$, update $0.1$ ✓.

For comparison, TD(0) would update only C (by 0.1). λ=1 would give each state 0.1. The trace spreads the final surprise backward with fading credit. In this case the weights are constant until the reward arrives, so the backward and forward totals match exactly.

## Concepts
- [[eligibility-trace]] (new) — a fading short-term memory vector $\mathbf z_t$ (same size as $\mathbf w$) marking which weights recently contributed to value estimates (p. 287, 292)
- [[temporal-difference-learning]] — learning values from the one-step TD error $\delta_t$; traces spread this error over recent states (p. 293)
- [[lambda-return]] (new) — geometric average $(1-\lambda)\sum\lambda^{n-1}G_{t:t+n}$ of n-step returns; interpolates TD and Monte Carlo (p. 289)
- [[forward-and-backward-views]] (new) — forward: update from later events; backward: update from current TD error and traces; sometimes equivalent (p. 288)
- [[n-step-return]] (new) — sum of n discounted rewards plus a bootstrapped value at step n (p. 288)
- [[bootstrapping]] (new) — using current value estimates in the target; λ sets the degree (pp. 308, 317)
- [[trace-decay-parameter]] (new) — λ∈[0,1], the rate at which traces fall (p. 287)
- [[dutch-trace]] (new) — trace (12.11) used in true online TD(λ); in contrast to the accumulating and replacing traces (pp. 300–301)
- [[true-online-td-lambda]] (new) — exact O(d) implementation of the online λ-return algorithm for linear approximation (pp. 299–300)
- [[termination-function]] (new) — state-dependent γ(s) that ends or discounts the return and unifies episodic and continuing cases (p. 307–308)
- [[off-policy-learning]] — learning about a target policy π from data of a behavior policy b; here via control-variate importance sampling and traces (p. 309)
- [[importance-sampling-ratio]] (new) — $\rho_t=\pi(A_t|S_t)/b(A_t|S_t)$, entering traces and returns (p. 309)
- [[policy]] — rule mapping states to actions; π is the target policy, b the behavior policy (pp. 309, 312, 314)
- [[stability]] — here: off-policy semi-gradient trace methods are not guaranteed stable; Gradient-TD and Emphatic-TD ones are (pp. 312, 314)
- [[deadly-triad]] (new) — off-policy + bootstrapping + function approximation can diverge (p. 312)
- [[delay-dead-time]] — delayed rewards are one case where traces help (p. 317)

## Canonical instances
- [[random-walk-19-state]] — Example 7.1 task used to compare λ-return, TD(λ), online λ-return and n-step methods (pp. 291, 294, 299)
- [[gridworld-trace-credit]] — Example 12.1: one-step, n-step and trace updates after reaching a goal (p. 304)
- [[mountain-car]] — Example 12.2 and Fig. 12.11: Sarsa(λ) versus n-step Sarsa and true online Sarsa(λ) (pp. 305–306)
- [[lambda-sweep-four-tasks]] — Fig. 12.14: intermediate λ best on Mountain Car, random walk, Puddle World and cart-pole (p. 318)
- [[linear-mc-lms]] — Section 12.6: LMS/MC rewritten with a dutch trace (pp. 301–303)

## Bridges (candidates)
- [structural-analogy] eligibility trace ↔ control-theory: fading-memory (exponentially weighted) filter of past inputs — both keep a decaying sum of past signals, with decay set by one parameter.
- [structural-analogy] backward-view credit assignment (TD error shouted back to prior states) ↔ control-theory: delay (dead time) — spreading a late signal back over earlier causes compensates for lag between action and effect.
- [same-math] dutch-trace derivation with forgetting matrices $\mathbf F_t=\mathbf I-\alpha\mathbf x_t\mathbf x_t^\top$ ↔ LMS adaptive filtering: the LMS update itself (stated in the text as the same rule), unrolled as a matrix product.
- [metaphor] choosing λ between MC and TD ↔ control-theory: trade-off between trusting a model prediction (bootstrap) and measured outcomes (Kalman-gain-like weighting).

## Questions this raises
- Is there a principled way to choose λ (or to vary $\lambda_t$ automatically), given that the author says no good theory exists yet (p. 317)?
- Which other forward-view algorithms can be turned into cheap backward-view ones by the same derivation pattern (forward update, sum of TD errors, rearranged summation)?
- Off-policy traces fix the expected-target problem but not the distribution-of-updates problem (p. 312). How do the Gradient-TD and Emphatic-TD methods address the second part, and at what cost in variance?
- How well do traces work with nonlinear function approximation, where dutch traces are not available (p. 301)?

## Exercises worth doing
- Ex. 12.1 (p. 290) — derive a recursive relation for the λ-return from (12.2) and (12.1); basis for later recursive forms — difficulty: medium
- Ex. 12.3 (p. 295) — write the λ-return error as a sum of TD errors; explains why TD(λ) approximates the offline λ-return — difficulty: medium
- Ex. 12.5 (p. 297) — prove (12.10): k-step λ-return as a sum of TD-like errors — difficulty: medium
- Ex. 12.6 (p. 305) — change the Sarsa(λ) pseudocode to dutch traces (linear, binary features) — difficulty: medium
- Ex. 12.8 (p. 309) — prove (12.24) is exact when the value function is fixed — difficulty: medium
- Ex. 12.12 (p. 311) — derive the action-value trace (12.29) in detail — difficulty: hard

## Reading notes
- Printed page = pdf page − 22 (pdf 309 = printed 287). Page labels give printed numbers directly.
- The text layer drops most Greek letters and symbols (γ, λ, δ, α, ρ, ∇, superscripts). I rebuilt every equation from the page images where available. No image was provided for printed p. 301, so Eq. (12.12) was reconstructed from the surviving text ("otherwise $z_{i,t-1}$"): I read the missing factor as $\gamma\lambda$, matching the decay in (12.5).
- The text layer of printed p. 306 is badly mixed with fragments of another paper's figure. The page image is clean and was used instead.
- Possible misprint, p. 302: the text says $\mathbf a_0=\mathbf w_0$ but also defines $\mathbf a_t\doteq\mathbf F_t\cdots\mathbf F_0\mathbf w_0$ and uses $\mathbf a_{T-1}=\mathbf F_{T-1}\cdots\mathbf F_0\mathbf w_0$ in (12.14). Taken literally, $\mathbf a_0=\mathbf w_0$ with $\mathbf a_t=\mathbf F_t\mathbf a_{t-1}$ would omit $\mathbf F_0$. I report both as printed.
- Typo, p. 310: "alway 1" for "always 1".
- Section 12.6 is starred in the source (optional). Derivation of true online TD(λ) is not given; the text refers to van Seijen et al. (2016).
- The unit contains exercises 12.1–12.14; only a selection is listed above and none are solved. Edition and copyright details are not visible on these pages beyond the running headers "Chapter 12: Eligibility Traces".
