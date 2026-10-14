---
id: sutton-2018-rl/ch07-n
work: sutton-2018-rl
unit: Chapter 7 — n-step Bootstrapping
pages: 141-158
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# n-step Bootstrapping

## L0 — One line
Updating a value estimate from n real rewards plus a bootstrapped estimate n steps later gives a family of methods between one-step TD (n = 1) and Monte Carlo (n = ∞), and intermediate n often works best.

## L1 — The gist (≤ 120 words)
Monte Carlo (MC) methods wait for the whole episode. One-step TD methods bootstrap (update an estimate from another estimate) after one reward. Neither is always best. The chapter defines the n-step return, which uses n real rewards and then an estimate. From it the chapter builds n-step TD prediction, n-step Sarsa and n-step Expected Sarsa. It then covers two off-policy routes: importance sampling (with control variates) and the tree-backup algorithm. Finally it gives a unifying algorithm, n-step Q(σ). A random-walk test shows intermediate n performing best. The costs are an n-step delay before each update, more computation and more memory.

**Prerequisites:** one-step TD and Sarsa; Monte Carlo returns; discounting; expectation; ε-greedy policies; basic importance sampling.

## L2 — Key ideas
- The n-step return truncates the return after n rewards and corrects with a discounted value estimate; n = 1 gives TD(0), and n reaching the episode end gives MC (p. 143).
- n-step TD updates $V(S_t)$ toward this return, but only at time $t+n$, since only then are the needed rewards and state known (p. 143).
- The error reduction property: the worst-state error of the expected n-step return is at most $\gamma^n$ times the worst error of the current estimate. It underlies convergence of n-step TD (p. 144).
- On a 19-state random walk, intermediate n gave the lowest error. In a gridworld, n-step Sarsa strengthens the last n actions of a path instead of only the last one (pp. 145, 147).
- Off-policy learning multiplies the update by an importance sampling ratio over the n actions. For action values the ratio starts one step later, because the first action is already taken (pp. 148–149).
- Per-decision control variates make the target equal the current estimate when $\rho_t = 0$, instead of zero, which reduces variance without changing the expected update (p. 150).
- The tree-backup algorithm learns off-policy without importance sampling by branching over unselected actions and weighting them by $\pi$ (pp. 152–153).
- n-step Q(σ) slides each step between sampling (σ = 1) and expectation (σ = 0), covering Sarsa, Expected Sarsa and tree backup (pp. 154–156).

## L3 — Walkthrough

### Introduction (p. 141)
- n-step TD methods generalize both MC and one-step TD. They span a spectrum between the two, and the best methods are often intermediate (p. 141).
- Another benefit is freedom from "the tyranny of the time step". In one-step TD, one step sets both how often the action can change and the interval over which bootstrapping happens. Bootstrapping works best over a longer interval in which a recognizable state change has occurred (p. 141).
- Eligibility traces (Chapter 12) are postponed. Prediction ($v_\pi$) comes first, then control (p. 141).

### 7.1 n-step TD prediction
- Between MC (all rewards until the end) and one-step TD (one reward, then the value of the next state) lie updates based on an intermediate number of rewards, for example two rewards plus the estimated value two steps later (Fig. 7.1). These are still TD methods because they change an earlier estimate based on how it differs from a later estimate, now n steps later (p. 142).
- **Target.** The MC target is the full return $G_t \doteq R_{t+1}+\gamma R_{t+2}+\dots+\gamma^{T-t-1}R_T$. The one-step return is $G_{t:t+1}\doteq R_{t+1}+\gamma V_t(S_{t+1})$, with $V_t$ the estimate at time $t$ (p. 143).
- The two-step return is $G_{t:t+2}\doteq R_{t+1}+\gamma R_{t+2}+\gamma^2 V_{t+1}(S_{t+2})$. The last term replaces the missing $\gamma^2R_{t+3}+\dots+\gamma^{T-t-1}R_T$ (p. 143).
- In general (p. 143), for $n\ge1$ and $0\le t<T-n$:
$$G_{t:t+n}\doteq R_{t+1}+\gamma R_{t+2}+\dots+\gamma^{n-1}R_{t+n}+\gamma^n V_{t+n-1}(S_{t+n}) \tag{7.1}$$
- If $t+n\ge T$, the missing terms are zero and $G_{t:t+n}\doteq G_t$ (p. 143).
- **Timing.** No real algorithm can use the n-step return before time $t+n$, when $R_{t+n}$ is seen and $V_{t+n-1}$ computed (p. 143).
- **Update (n-step TD).** All other states stay unchanged (p. 143):
$$V_{t+n}(S_t)\doteq V_{t+n-1}(S_t)+\alpha\big[G_{t:t+n}-V_{t+n-1}(S_t)\big],\quad 0\le t<T \tag{7.2}$$
- No changes are made during the first $n-1$ steps of an episode. An equal number of extra updates are made after termination (p. 143).
- **Pseudocode (p. 144).** It keeps $\tau=t-n+1$, the time whose state is updated. It computes $G\leftarrow\sum_{i=\tau+1}^{\min(\tau+n,T)}\gamma^{i-\tau-1}R_i$. If $\tau+n<T$, it adds $\gamma^nV(S_{\tau+n})$. It then updates $V(S_\tau)$.
- **Error reduction property.** For all $n\ge1$ (p. 144):
$$\max_s\big|\mathbb E_\pi[G_{t:t+n}\mid S_t=s]-v_\pi(s)\big|\le\gamma^n\max_s\big|V_{t+n-1}(s)-v_\pi(s)\big| \tag{7.3}$$
- The author says that, because of this, one can show formally that all n-step TD methods converge under appropriate technical conditions (p. 144).
- **Intuition note:** An n-step return replaces the tail of the return by an estimate that is discounted $n$ times. In the worst-state sense, the error of the expected n-step return is at most $\gamma^n$ times the error of that estimate (7.3). The author uses this property to argue that n-step TD methods converge.
- **Example 7.1 (5-state random walk, p. 144–145).** All values start at 0.5. The episode goes C → D → E → right, with return 1. A one-step method changes only $V(E)$. A two-step method changes $V(D)$ and $V(E)$. Any $n>2$ method changes all three visited states toward 1, by the same amount (p. 145).
- **Figure 7.2 (p. 145).** A 19-state walk has outcome −1 on the left and all values initialized to 0. The measure is the RMS error over the 19 states, averaged over the first 10 episodes and 100 repetitions. Methods with intermediate n worked best, so, the author says, generalizing to n-step methods can potentially perform better than either extreme (p. 145).

### 7.2 n-step Sarsa
- Switch from states to state–action pairs and use an ε-greedy policy. This gives on-policy control; the original method is called Sarsa(0). Backup diagrams start and end with an action (p. 146).
- Returns (p. 146), with $G_{t:t+n}\doteq G_t$ if $t+n\ge T$:
$$G_{t:t+n}\doteq R_{t+1}+\dots+\gamma^{n-1}R_{t+n}+\gamma^nQ_{t+n-1}(S_{t+n},A_{t+n}),\quad n\ge1,\ 0\le t<T-n \tag{7.4}$$
$$Q_{t+n}(S_t,A_t)\doteq Q_{t+n-1}(S_t,A_t)+\alpha\big[G_{t:t+n}-Q_{t+n-1}(S_t,A_t)\big],\quad 0\le t<T \tag{7.5}$$
- Other pairs $(s,a)$ stay unchanged (p. 146).
- **Figure 7.4 (p. 147).** In a gridworld all rewards are zero except at G, and values start at 0. After one path to G, one-step Sarsa strengthens only the last action. 10-step Sarsa strengthens the last 10 actions, so more is learned from one episode (p. 147).
- **Intuition note:** Reward information travels back n steps per episode instead of one. That is why learning can be faster.
- **n-step Expected Sarsa (p. 148).** It has the same update, but the last element is a branch over all actions weighted by $\pi$:
$$G_{t:t+n}\doteq R_{t+1}+\dots+\gamma^{n-1}R_{t+n}+\gamma^n\bar V_{t+n-1}(S_{t+n}),\quad t+n<T \tag{7.7}$$
$$\bar V_t(s)\doteq\sum_a\pi(a|s)Q_t(s,a)\quad\text{for all }s\in\mathcal S \tag{7.8}$$
- $G_{t:t+n}\doteq G_t$ for $t+n\ge T$. $\bar V$ is the "expected approximate value". It is 0 if $s$ is terminal (p. 148).

### 7.3 n-step off-policy learning
- Off-policy learning learns about target policy $\pi$ while following behavior policy $b$. The data from $b$ must be reweighted by the relative probability of the n actions taken (p. 148).
- Importance sampling ratio and off-policy n-step TD (p. 148):
$$\rho_{t:h}\doteq\prod_{k=t}^{\min(h,T-1)}\frac{\pi(A_k|S_k)}{b(A_k|S_k)} \tag{7.10}$$
$$V_{t+n}(S_t)\doteq V_{t+n-1}(S_t)+\alpha\,\rho_{t:t+n-1}\big[G_{t:t+n}-V_{t+n-1}(S_t)\big],\quad 0\le t<T \tag{7.9}$$
- If any action has $\pi(A_k|S_k)=0$, the return gets zero weight. If an action is taken that $\pi$ favours much more than $b$ does, the weight rises, because such actions are rare in the data (p. 149).
- On-policy, $\rho=1$ always, so (7.9) replaces the earlier n-step TD update (p. 149).
- Off-policy n-step Sarsa (p. 149):
$$Q_{t+n}(S_t,A_t)\doteq Q_{t+n-1}(S_t,A_t)+\alpha\,\rho_{t+1:t+n}\big[G_{t:t+n}-Q_{t+n-1}(S_t,A_t)\big],\quad 0\le t<T \tag{7.11}$$
- The ratio starts and ends one step later than in (7.9). The first action is already selected, so we want to learn fully from what follows, and importance sampling applies only to later actions (p. 149).
- Off-policy n-step Expected Sarsa uses $\rho_{t+1:t+n-1}$ (one factor fewer) and return (7.7). In the last state all actions are taken into account, so the action actually taken needs no correction (p. 150).

### 7.4 *Per-decision methods with control variates
- The n-step return can be written recursively (p. 150), with $G_{h:h}\doteq V_{h-1}(S_h)$:
$$G_{t:h}=R_{t+1}+\gamma G_{t+1:h},\quad t<h<T \tag{7.12}$$
- Simply weighting the right side by $\rho_t=\pi(A_t|S_t)/b(A_t|S_t)$ gives a zero return if $\rho_t=0$. This could cause high variance in the target (p. 150).
- **Off-policy state return (p. 150):**
$$G_{t:h}\doteq\rho_t(R_{t+1}+\gamma G_{t+1:h})+(1-\rho_t)V_{h-1}(S_t),\quad t<h<T \tag{7.13}$$
- If $\rho_t=0$, the target equals the estimate and the estimate is left unchanged (p. 150).
- The term $(1-\rho_t)V_{h-1}(S_t)$ is the control variate. The author says it does not change the expected update, because $\rho$ has expected value one and is uncorrelated with the estimate, so the term has expectation zero. When $\rho_t=1$ always (on-policy), (7.13) equals (7.1). It is used with the n-step TD update (7.2) (p. 150).
- **Action values (p. 151).** The first action gets no importance sampling. The recursion ends with $G_{h:h}\doteq\bar V_{h-1}(S_h)$ for the on-policy expectation form. The off-policy form is:
$$G_{t:h}\doteq R_{t+1}+\gamma\big(\rho_{t+1}G_{t+1:h}+\bar V_{h-1}(S_{t+1})-\rho_{t+1}Q_{h-1}(S_{t+1},A_{t+1})\big)$$
$$=R_{t+1}+\gamma\rho_{t+1}\big(G_{t+1:h}-Q_{h-1}(S_{t+1},A_{t+1})\big)+\gamma\bar V_{h-1}(S_{t+1}),\quad t<h\le T \tag{7.14}$$
- If $h<T$ the recursion ends with $G_{h:h}\doteq Q_{h-1}(S_h,A_h)$. If $h\ge T$ it ends with $G_{T-1:h}\doteq R_T$. Combined with (7.5), the algorithm is analogous to Expected Sarsa (p. 151).
- Importance sampling gives sound off-policy learning but high-variance updates. These force a small step size, so learning is slow. The authors say it is probably inevitable that off-policy training is slower than on-policy training, but probably also true that these methods can be improved. They name control variates, Autostep and invariant updates as ways to improve, and say Mahmood's usage technique "may also be part of the solution" (pp. 151–152).
- **Intuition note:** A zero ratio means the sample should be ignored, and the authors say leaving the estimate unchanged seems appropriate, rather than shrinking it toward zero. The control variate gives that result and, the authors say, does not change the expected update.

### 7.5 Off-policy learning without importance sampling: n-step tree backup
- Q-learning and Expected Sarsa do this for one step. The tree-backup algorithm does it for n steps (p. 152).
- In the 3-step diagram, the central spine has sampled states, rewards and actions. Unselected actions hang off each state. There is no sample for them, so their estimated values are used. The target comes from the leaf action nodes. Interior nodes of actions actually taken do not take part (p. 152).
- **Weights (p. 152).** A first-level action $a\neq A_{t+1}$ has weight $\pi(a|S_{t+1})$. A second-level action $a'$ has weight $\pi(A_{t+1}|S_{t+1})\pi(a'|S_{t+2})$. The pattern continues down the spine.
- **Returns (p. 153).** The one-step return equals Expected Sarsa's, for $t<T-1$:
$$G_{t:t+1}\doteq R_{t+1}+\gamma\sum_a\pi(a|S_{t+1})Q_t(S_{t+1},a) \tag{7.15}$$
- The two-step return is, for $t<T-2$:
$$G_{t:t+2}\doteq R_{t+1}+\gamma\!\!\sum_{a\ne A_{t+1}}\!\!\pi(a|S_{t+1})Q_{t+1}(S_{t+1},a)+\gamma\pi(A_{t+1}|S_{t+1})\Big(R_{t+2}+\gamma\sum_a\pi(a|S_{t+2})Q_{t+1}(S_{t+2},a)\Big)$$
$$=R_{t+1}+\gamma\!\!\sum_{a\ne A_{t+1}}\!\!\pi(a|S_{t+1})Q_{t+1}(S_{t+1},a)+\gamma\pi(A_{t+1}|S_{t+1})G_{t+1:t+2}$$
- General recursive definition, for $t<T-1$, $n\ge2$ (with $n=1$ handled by (7.15) and $G_{T-1:t+n}\doteq R_T$):
$$G_{t:t+n}\doteq R_{t+1}+\gamma\!\!\sum_{a\ne A_{t+1}}\!\!\pi(a|S_{t+1})Q_{t+n-1}(S_{t+1},a)+\gamma\pi(A_{t+1}|S_{t+1})G_{t+1:t+n} \tag{7.16}$$
- It is used with the n-step Sarsa update rule (7.5). Pseudocode is on p. 154.
- **Intuition note:** Where there is no sample, use your own estimates. Weight them by how likely the target policy is to choose each action, so no correction for the behavior policy is needed.

### 7.6 *A unifying algorithm: n-step Q(σ)
- Figure 7.5 shows four 4-step action-value diagrams. Sarsa samples every step. Tree backup branches every step. Expected Sarsa samples every step except the last, which it branches. The fourth diagram decides step by step whether to sample or take the expectation (p. 154–155).
- Let $\sigma_t\in[0,1]$ be the degree of sampling on step $t$: 1 is full sampling, 0 is pure expectation. $\sigma_t$ may be a function of the state, action or state–action pair (p. 155).
- Rewriting tree backup with horizon $h=t+n$ and $\bar V$ (p. 155):
$$G_{t:h}=R_{t+1}+\gamma\bar V_{h-1}(S_{t+1})-\gamma\pi(A_{t+1}|S_{t+1})Q_{h-1}(S_{t+1},A_{t+1})+\gamma\pi(A_{t+1}|S_{t+1})G_{t+1:h}$$
$$=R_{t+1}+\gamma\pi(A_{t+1}|S_{t+1})\big(G_{t+1:h}-Q_{h-1}(S_{t+1},A_{t+1})\big)+\gamma\bar V_{h-1}(S_{t+1})$$
- This equals Sarsa with control variates (7.14), with $\pi(A_{t+1}|S_{t+1})$ in place of $\rho_{t+1}$. Q(σ) interpolates linearly between the two (p. 155):
$$G_{t:h}\doteq R_{t+1}+\gamma\big(\sigma_{t+1}\rho_{t+1}+(1-\sigma_{t+1})\pi(A_{t+1}|S_{t+1})\big)\big(G_{t+1:h}-Q_{h-1}(S_{t+1},A_{t+1})\big)+\gamma\bar V_{h-1}(S_{t+1}) \tag{7.17}$$
- For $t<h\le T$. The recursion ends with $G_{h:h}\doteq Q_{h-1}(S_h,A_h)$ if $h<T$, or $G_{T-1:T}\doteq R_T$ if $h=T$. The update is (7.5), without ratios, since they are inside the return (p. 156).

### 7.7 Summary
- Intermediate amounts of bootstrapping will typically perform better than either extreme (p. 157).
- All n-step methods delay updates by $n$ steps. They need more computation per step and more memory to store the last $n$ steps. Chapter 12 will show how multi-step TD methods can be implemented with minimal memory and computational complexity using eligibility traces, but there will always be some additional computation beyond one-step methods (p. 157).
- Two off-policy approaches were developed. Importance sampling is conceptually simple but can have high variance. If the policies differ greatly, it probably needs new ideas to be efficient. Tree backup extends Q-learning to multi-step with stochastic target policies. If the policies differ substantially, its bootstrapping may span only a few steps even for large $n$ (p. 157).

### Bibliographical remarks (p. 158)
- n-step returns and their error reduction property are credited to Watkins (1989). Cichosz (1995) and van Seijen (2016) showed that they are practical. The tree-backup algorithm is credited to Precup, Sutton and Singh (2000). The Q(σ) algorithm is called new to this text (p. 158).

## Toy example (ours)
Let $\gamma=0.9$. A trajectory from $S_0$ has $R_1=1$, $R_2=0$, $R_3=2$. Current estimates are $V(S_1)=4$, $V(S_2)=3$, $V(S_3)=5$ (treated as unchanged, as in (7.1)). Take $V(S_0)=2$ and $\alpha=0.5$.

- 1-step: $G_{0:1}=1+0.9\cdot4=4.6$.
- 2-step: $G_{0:2}=1+0.9\cdot0+0.81\cdot3=3.43$.
- 3-step: $G_{0:3}=1+0+0.81\cdot2+0.729\cdot5=1+1.62+3.645=6.265$.

The targets differ because each trusts a different estimate. Update with n = 3: $V(S_0)\leftarrow2+0.5\,(6.265-2)=4.1325$. With n = 1, $V(S_0)\leftarrow2+0.5\,(4.6-2)=3.3$.

Control variate check from (7.13): if $\rho_0=0$ and $V(S_0)=2$, then $G=0\cdot(\dots)+(1-0)\cdot2=2$. The target equals the estimate, so the update is $0.5\,(2-2)=0$, a no-change update.

## Concepts
- [[bootstrapping]] (new) — updating an estimate from another estimate; here over n steps instead of one (p. 141)
- [[n-step-return]] (new) — n discounted real rewards plus $\gamma^n$ times a value estimate at step n (p. 143)
- [[temporal-difference-learning]] — update an earlier estimate toward a later one; here the gap spans n steps (p. 142)
- [[n-step-td]] (new) — TD update toward the n-step return, made at time $t+n$ (p. 143)
- [[error-reduction-property]] (new) — the worst-state error of the expected n-step return is at most $\gamma^n$ times the worst-state error of the current estimate (p. 144)
- [[n-step-sarsa]] (new) — on-policy control with n-step returns on action values (p. 146)
- [[expected-approximate-value]] (new) — $\bar V_t(s)=\sum_a\pi(a|s)Q_t(s,a)$, 0 at terminal states (p. 148)
- [[policy]] — here a target policy $\pi$ and a behavior policy $b$ (p. 148)
- [[importance-sampling-ratio]] (new) — product of $\pi/b$ over the actions taken; reweights off-policy data (p. 148)
- [[control-variate]] (new) — extra term $(1-\rho_t)V$ that leaves the expected update unchanged and cuts variance (p. 150)
- [[tree-backup]] (new) — off-policy n-step method that bootstraps on unselected actions weighted by $\pi$ (p. 152)
- [[q-sigma]] (new) — n-step method with per-step degree of sampling $\sigma_t\in[0,1]$ (p. 155)
- [[exploration-vs-exploitation]] — ε-greedy behavior is used in n-step Sarsa (p. 146)

## Canonical instances
- [[random-walk-19-state]] — n-step TD test showing intermediate n is best (p. 145)
- [[random-walk-5-state]] — which states a 1-step, 2-step and larger-n method update after one episode (p. 144)
- [[gridworld-nstep-sarsa]] — one-step vs 10-step Sarsa strengthening of action values after one path (p. 147)

## Bridges (candidates)
- [structural-analogy] n-step return with bootstrapped tail ↔ model predictive control: a finite lookahead horizon plus an estimate of the remaining cost — both truncate the future and replace the tail by a value estimate.
- [structural-analogy] Control variate in (7.13) ↔ statistics: variance reduction by adding a zero-mean term — the same trick of subtracting a correlated term with known expectation.
- [metaphor] "Tyranny of the time step" ↔ control engineering: decoupling the sampling rate of actions from the horizon of prediction.

## Questions this raises
- Why does intermediate n beat both extremes, and how would the best n depend on the noise in rewards and on the accuracy of $V$?
- How much does the best n depend on the task, such as the walk's length or the initial values and outcomes (Exercise 7.3)?
- When the target and behavior policies differ strongly, can any n-step method make good use of long n?
- How can σ be chosen well in Q(σ), and does a state-dependent σ help?

## Exercises worth doing
- Ex. 7.1 (p. 143) — write the n-step error as a sum of TD errors when values are fixed — difficulty: medium
- Ex. 7.2 (p. 143) — programming: compare the sum-of-TD-errors algorithm with n-step TD — difficulty: medium
- Ex. 7.4 (p. 148) — prove the n-step Sarsa return is a discounted sum of new TD errors — difficulty: medium
- Ex. 7.6 (p. 151) — prove the control variate leaves the expected return unchanged — difficulty: medium
- Ex. 7.10 (p. 151) — programming: show that (7.13)+(7.2) is more data efficient than (7.1)+(7.9) — difficulty: hard
- Ex. 7.11 (p. 153) — write the tree-backup return as a sum of expectation-based TD errors — difficulty: hard

## Reading notes
- Printed page = pdf page − 22 (pdf 163 = printed 141).
- The text layer garbles Greek letters and math symbols (γ, π, ρ, σ, ≤, subscripts). All equations here were checked against the page images.
- Page 151 has a small typo in the image: "the recursion ends with and $G_{T-1:h}\doteq R_T$" (stray "and").
- Figures 7.1–7.5 are backup diagrams and were described only from the images and captions.
- Sections 7.4 and 7.6 carry an asterisk (*) in their titles; these pages do not say what it means. Exercise 7.7 is also starred.
