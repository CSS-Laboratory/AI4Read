---
id: sutton-2018-rl/ch10-policy
work: sutton-2018-rl
unit: Chapter 10 — On-policy Control with Approximation
pages: 243-256
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
# On-policy Control with Approximation

## L0 — One line
Episodic control with a parametric action-value function is a direct extension of semi-gradient TD (Sarsa), but for continuing tasks discounting stops defining the problem, and average reward with "differential" values takes its place.

## L1 — The gist (≤ 120 words)
How do we extend semi-gradient prediction to on-policy control? In episodic tasks the step is direct: learn action values with a parametric function, act ε-greedily (semi-gradient Sarsa and its n-step version), tested on Mountain Car. In continuing tasks, the average of discounted returns equals r(π)/(1−γ), so γ does not change how policies are ranked. The chapter therefore replaces discounting with average reward, differential value functions, differential TD errors and a differential Sarsa. This matters because function approximation removes the policy improvement theorem, and action-value methods seem to lack a local improvement guarantee.

**Prerequisites:** TD(0) and Sarsa in the tabular case; gradient descent; the discounted return and Bellman equations; MDPs and stationary distributions; the linear form $\hat q=\mathbf w^\top\mathbf x$.

## L2 — Key ideas
- Episodic semi-gradient Sarsa uses the TD(0) form with $\hat q(S,A,\mathbf w)$ in place of $\hat v$ (semi-gradient: the gradient in (10.2) is taken of $\hat q(S_t,A_t,\mathbf w_t)$ only). Control is added by ε-greedy action selection, for discrete and not-too-large action sets (p. 244).
- On Mountain Car (an underpowered car that must first move away from the goal), linear Sarsa with tile coding (grid tilings that turn the continuous state into binary features) solves the task. Zero initial values are optimistic and drive exploration even with ε = 0 (p. 246).
- n-step semi-gradient Sarsa learns best at an intermediate n (n = 4 in Fig. 10.4); n = 8 beat n = 1 in Fig. 10.3 (pp. 247–248).
- For continuing tasks the new objective is the average reward r(π), with differential returns (rewards minus $r(\pi)$), value functions and TD errors that mirror the old ones (pp. 249–250).
- Differential Sarsa converges to the differential values plus an arbitrary offset. The author says the offset may not matter in practice (p. 250).
- Discounting is futile for the problem definition: both the symmetry argument and the boxed derivation give average discounted return $=r(\pi)/(1-\gamma)$ (pp. 253–254).
- Root cause of the difficulties with the discounted setting: with function approximation the policy improvement theorem (improving one state's value guarantees a better policy) is lost; the author adds that improvement can no longer be guaranteed in any setting. For action-value methods we seem to be without a local improvement guarantee (pp. 253–254).

## L3 — Walkthrough

### Introduction (p. 243)
The chapter uses $\hat q(s,a,\mathbf w)\approx q_*(s,a)$ with $\mathbf w\in\mathbb R^d$. It stays on-policy; off-policy is Chapter 11. Episodic case: a straightforward extension. Continuing case: the authors say that once we have genuine function approximation, discounting has to be given up for a new average-reward formulation (p. 243).

### 10.1 Episodic Semi-gradient Control (pp. 243–246)
Training examples now have the form $S_t,A_t\mapsto U_t$. The target $U_t$ can be any approximation of $q_\pi(S_t,A_t)$: the Monte Carlo return $G_t$ or an n-step Sarsa return (p. 243). The general update:
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\big[U_t-\hat q(S_t,A_t,\mathbf w_t)\big]\nabla\hat q(S_t,A_t,\mathbf w_t)\tag{10.1}$$
One-step Sarsa uses $U_t=R_{t+1}+\gamma\hat q(S_{t+1},A_{t+1},\mathbf w_t)$:
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\big[R_{t+1}+\gamma\hat q(S_{t+1},A_{t+1},\mathbf w_t)-\hat q(S_t,A_t,\mathbf w_t)\big]\nabla\hat q(S_t,A_t,\mathbf w_t)\tag{10.2}$$
This is *episodic semi-gradient one-step Sarsa*. For a constant policy it converges like TD(0), with the same kind of error bound (9.14) (p. 244).

For control, the author says techniques for continuous or large discrete action sets are an open research topic with no clear resolution. For discrete, not-too-large action sets, compute $\hat q(S_{t+1},a,\mathbf w_t)$ for each $a$ and take the greedy action $A^*_{t+1}=\arg\max_a\hat q(S_{t+1},a,\mathbf w_t)$. Policy improvement then makes the policy a soft approximation of greedy (e.g. ε-greedy), and the same policy selects actions (p. 244). The boxed algorithm applies (10.2) each step, with target $R$ alone if $S'$ is terminal. $A'$ is chosen as a function of $\hat q(S',\cdot,\mathbf w)$, e.g. ε-greedily (p. 244).

**Example 10.1, Mountain Car.** An underpowered car must first move up the opposite slope to build inertia. Things must get "worse" (farther from the goal) before they get better (pp. 244–245). The reward is −1 on every step until the car passes the goal, which ends the episode. Actions: throttle +1, −1, 0. Dynamics (p. 245):
$$x_{t+1}\doteq \mathrm{bound}[x_t+\dot x_{t+1}],\qquad \dot x_{t+1}\doteq \mathrm{bound}[\dot x_t+0.001A_t-0.0025\cos(3x_t)]$$
The bounds are $-1.2\le x_{t+1}\le0.5$ and $-0.07\le\dot x_{t+1}\le0.07$. At the left bound the velocity is reset to zero; at the right bound the episode ends. Each episode starts at a random $x_t\in[-0.6,-0.4)$ with zero velocity (p. 245).

Features: 8 grid tilings. Each tile covers 1/8 of the bounded range in each dimension, with asymmetrical offsets (pp. 245–246). The feature vector is $\mathbf x(s,a)\in\mathbb R^d$, and the approximation is linear:
$$\hat q(s,a,\mathbf w)\doteq\mathbf w^\top\mathbf x(s,a)=\sum_{i=1}^d w_i\,x_i(s,a)\tag{10.3}$$
(added step) Here $\nabla\hat q=\mathbf x(s,a)$.

Initial values of zero are optimistic, because all true values are negative. This causes extensive exploration even though ε = 0. By "Step 428" no episode has finished, yet the car has oscillated through the valley. Frequently visited states look worse than unexplored ones, which pushes the agent to new states until a solution is found (p. 246). Fig. 10.2 shows learning curves for α = 0.1/8, 0.2/8, 0.5/8, averaged over 100 runs. Footnote 2 (attached to the Fig. 10.1 discussion): that data come from semi-gradient Sarsa(λ), which the book meets only in Chapter 12; the authors say semi-gradient Sarsa would behave similarly (p. 246).

*Intuition note.* Sarsa with approximation is TD(0) applied to $(S,A)$ pairs, plus ε-greedy action choice. Optimism makes the agent explore on its own, because whatever it has already tried gets valued down.

### 10.2 Semi-gradient n-step Sarsa (pp. 247–248)
Use an n-step return as the target in (10.1):
$$G_{t:t+n}\doteq R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^n\hat q(S_{t+n},A_{t+n},\mathbf w_{t+n-1}),\quad t+n<T\tag{10.4}$$
with $G_{t:t+n}\doteq G_t$ if $t+n\ge T$. The update:
$$\mathbf w_{t+n}\doteq\mathbf w_{t+n-1}+\alpha\,[G_{t:t+n}-\hat q(S_t,A_t,\mathbf w_{t+n-1})]\nabla\hat q(S_t,A_t,\mathbf w_{t+n-1}),\quad 0\le t<T\tag{10.5}$$
The boxed pseudocode stores the last $n+1$ states, actions and rewards. It updates the estimate for time $\tau=t-n+1$ once $\tau\ge0$ (p. 247). Results on Mountain Car: $n=8$ tends to learn faster and reach better asymptotic performance than $n=1$ (Fig. 10.3, α = 0.5/8 for n = 1 and 0.3/8 for n = 8). Over the first 50 episodes and 100 runs, an intermediate level of bootstrapping (n = 4) performed best (Fig. 10.4, p. 248). Standard errors ranged from 0.5 (n = 1) to about 4 (n = 16), so the main effects are statistically significant (p. 248).

*Intuition note.* Looking n steps ahead before bootstrapping mixes real rewards and the current estimate. In these experiments a middle value of n worked better than either extreme tested.

### 10.3 Average Reward: A New Problem Setting for Continuing Tasks (pp. 249–251)
Third classical setting beside episodic and discounted. It applies to continuing tasks, but with no discounting: delayed reward counts as much as immediate reward (p. 249). The quality of a policy is its average reward rate:
$$r(\pi)\doteq\lim_{h\to\infty}\frac1h\sum_{t=1}^h\mathbb E[R_t\mid S_0,A_{0:t-1}\sim\pi]\tag{10.6}$$
$$=\lim_{t\to\infty}\mathbb E[R_t\mid S_0,A_{0:t-1}\sim\pi]\tag{10.7}$$
$$=\sum_s\mu_\pi(s)\sum_a\pi(a|s)\sum_{s',r}p(s',r|s,a)\,r$$
The last two lines hold if the steady-state distribution $\mu_\pi(s)\doteq\lim_{t\to\infty}\Pr\{S_t=s\mid A_{0:t-1}\sim\pi\}$ exists and does not depend on $S_0$, i.e. if the MDP is *ergodic*. Ergodicity is sufficient but not necessary for the limit in (10.6) to exist (p. 249). The author says subtle distinctions of optimality exist, but for most practical purposes it may be adequate to rank policies by $r(\pi)$. All policies attaining the maximal $r(\pi)$ are called optimal (p. 249). The stationary distribution satisfies
$$\sum_s\mu_\pi(s)\sum_a\pi(a|s)p(s'|s,a)=\mu_\pi(s')\tag{10.8}$$
The *differential return* subtracts the average reward:
$$G_t\doteq R_{t+1}-r(\pi)+R_{t+2}-r(\pi)+R_{t+3}-r(\pi)+\cdots\tag{10.9}$$
Differential value functions use the usual notation $v_\pi(s)=\mathbb E_\pi[G_t|S_t=s]$ and $q_\pi(s,a)=\mathbb E_\pi[G_t|S_t=s,A_t=a]$. Their Bellman equations drop all $\gamma$s and replace each reward by $r-r(\pi)$ (p. 250):
$$v_\pi(s)=\sum_a\pi(a|s)\sum_{r,s'}p(s',r|s,a)\big[r-r(\pi)+v_\pi(s')\big]$$
$$q_\pi(s,a)=\sum_{r,s'}p(s',r|s,a)\Big[r-r(\pi)+\sum_{a'}\pi(a'|s')q_\pi(s',a')\Big]$$
$$v_*(s)=\max_a\sum_{r,s'}p(s',r|s,a)\big[r-\max_\pi r(\pi)+v_*(s')\big]$$
$$q_*(s,a)=\sum_{r,s'}p(s',r|s,a)\big[r-\max_\pi r(\pi)+\max_{a'}q_*(s',a')\big]$$
Differential TD errors, where $\bar R_t$ estimates $r(\pi)$:
$$\delta_t\doteq R_{t+1}-\bar R_t+\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_t)\tag{10.10}$$
$$\delta_t\doteq R_{t+1}-\bar R_t+\hat q(S_{t+1},A_{t+1},\mathbf w_t)-\hat q(S_t,A_t,\mathbf w_t)\tag{10.11}$$
With these definitions most algorithms and many theoretical results carry over unchanged (p. 250). Differential semi-gradient Sarsa:
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\,\delta_t\nabla\hat q(S_t,A_t,\mathbf w_t)\tag{10.12}$$
with $\delta_t$ from (10.11). Boxed algorithm (p. 251): $\delta\leftarrow R-\bar R+\hat q(S',A',\mathbf w)-\hat q(S,A,\mathbf w)$; $\bar R\leftarrow\bar R+\beta\delta$; $\mathbf w\leftarrow\mathbf w+\alpha\delta\nabla\hat q(S,A,\mathbf w)$.

Limitation: it converges to the differential values plus an arbitrary offset. The Bellman equations and TD errors are unaffected by shifting all values equally, so the offset may not matter in practice. Removing it is left as a research question (p. 250).

**Example 10.2, access-control queuing** (p. 252). There are 10 servers. Customers of four priorities pay 1, 2, 4 or 8 if served, and are accepted or rejected at the head of the queue. A rejected customer pays 0. A customer is always rejected if no server is free. Each busy server frees with probability 0.06 per step. The statistics are assumed unknown. The solution is tabular (state = number of free servers and head priority; action = accept or reject). Parameters: α = 0.01, β = 0.01, ε = 0.1, with initial values and $\bar R$ zero. After 2 million steps the learned $\bar R$ was about 2.31. In the plotted policy, low-priority customers are rejected when few servers are free. The author says the value drop on the right of the plot is probably due to insufficient data, since many of those states were never experienced (p. 252).

*Intuition note.* Instead of discounting, we subtract the long-run reward rate. A value then measures the total excess of future rewards over the average rate, not the total reward itself.

### 10.4 Deprecating the Discounted Setting (pp. 253–254)
Discounting is useful in the tabular case, but with approximation it is questionable whether to use it at all. Suppose states are only feature vectors that may hardly distinguish states. Then only the reward sequence (and the actions) can be assessed, so returns must be averaged over a long interval. The author states that the average of discounted returns is always $r(\pi)/(1-\gamma)$, so the ordering of policies equals that of average reward. Even $\gamma=0$ would leave the ranking unchanged (p. 253).

*Symmetry argument.* Every time step is like every other. The $t$-th reward appears undiscounted in the $(t-1)$st return, discounted once in the $(t-2)$nd, and 999 times in the $(t-1000)$th. Its total weight is $1+\gamma+\gamma^2+\cdots=1/(1-\gamma)$ (p. 253).

*Box, "The Futility of Discounting".* Take the objective $J(\pi)=\sum_s\mu_\pi(s)v^\gamma_\pi(s)$ (p. 254):
$$J(\pi)=\sum_s\mu_\pi(s)\sum_a\pi(a|s)\sum_{s'}\sum_r p(s',r|s,a)[r+\gamma v^\gamma_\pi(s')]\quad\text{(Bellman)}$$
$$=r(\pi)+\sum_s\mu_\pi(s)\sum_a\pi(a|s)\sum_{s'}\sum_r p(s',r|s,a)\gamma v^\gamma_\pi(s')\quad\text{(from 10.7)}$$
$$=r(\pi)+\gamma\sum_{s'}v^\gamma_\pi(s')\sum_s\mu_\pi(s)\sum_a\pi(a|s)p(s'|s,a)\quad\text{(from 3.4)}$$
$$=r(\pi)+\gamma\sum_{s'}v^\gamma_\pi(s')\mu_\pi(s')\quad\text{(from 10.8)}$$
$$=r(\pi)+\gamma J(\pi)=r(\pi)+\gamma r(\pi)+\gamma^2J(\pi)=r(\pi)+\gamma r(\pi)+\gamma^2r(\pi)+\gamma^3r(\pi)+\cdots=\frac1{1-\gamma}r(\pi).$$
So this discounted objective orders policies exactly like average reward, and $\gamma$ does not influence the ordering (p. 254).

Consequences: optimizing discounted value over the on-policy distribution is identical to optimizing average reward. The author says this strongly suggests that discounting has no role in defining the control problem with approximation, though it can still be used in solution methods, where $\gamma$ becomes a solution-method parameter. But discounting algorithms with approximation do not optimize discounted value over the on-policy distribution, so they are not guaranteed to optimize average reward (p. 253). The author names the root cause of the difficulties with the discounted control setting as the loss of the policy improvement theorem. Improving the discounted value of one state no longer guarantees an improved policy "in any useful sense" (p. 253). The author adds that this is also a lacuna for the total-episodic and average-reward settings. Chapter 13's policy-gradient theorem plays a similar role for parameterized policies. For action-value methods we seem currently to be without a local improvement guarantee (the Perkins and Precup (2003) approach may offer part of an answer). ε-greedification may sometimes give an inferior policy, since policies may chatter among good policies (Gordon, 1996a) (p. 254).

*Intuition note.* Averaged over a never-ending, uniform stream of rewards, discounting only multiplies every policy's score by the same $1/(1-\gamma)$. So it cannot change which policy is best under this on-policy averaging.

### 10.5 Differential Semi-gradient n-step Sarsa (p. 255)
Differential n-step return, with $\bar R$ an estimate of $r(\pi)$, $n\ge1$, $t+n<T$:
$$G_{t:t+n}\doteq R_{t+1}-\bar R_{t+n-1}+\cdots+R_{t+n}-\bar R_{t+n-1}+\hat q(S_{t+n},A_{t+n},\mathbf w_{t+n-1})\tag{10.14}$$
$G_{t:t+n}\doteq G_t$ if $t+n\ge T$. The n-step TD error is
$$\delta_t\doteq G_{t:t+n}-\hat q(S_t,A_t,\mathbf w)\tag{10.15}$$
and the update (10.12) is applied. Boxed algorithm, for $\tau=t-n+1\ge0$: $\delta\leftarrow\sum_{i=\tau+1}^{\tau+n}(R_i-\bar R)+\hat q(S_{\tau+n},A_{\tau+n},\mathbf w)-\hat q(S_\tau,A_\tau,\mathbf w)$; $\bar R\leftarrow\bar R+\beta\delta$; $\mathbf w\leftarrow\mathbf w+\alpha\delta\nabla\hat q(S_\tau,A_\tau,\mathbf w)$ (p. 255).

### 10.6 Summary and remarks (p. 256)
The extension to control is immediate for episodic tasks. For continuing tasks a new formulation maximizing average reward per step is needed. The author states the discounted formulation cannot be carried over to control with approximation. In the approximate case most policies cannot be represented by a value function. The remaining arbitrary policies need ranking, and the scalar $r(\pi)$ does this effectively (p. 256). Remarks: linear semi-gradient Sarsa with ε-greedy selection does not converge in the usual sense, but enters a bounded region near the best solution (Gordon). The algorithm of §10.3 is the on-policy analog of Schwartz's R-learning (p. 256).

## Toy example (ours, not from the text)
Two deterministic reward streams, with policy A giving $1,0,1,0,\dots$ and policy B giving $0.4,0.4,\dots$. Take $\gamma=0.5$. The streams are non-ergodic, so we average the return over the two start phases, each equally often.
- Average rewards: $r(A)=(1+0)/2=0.5$; $r(B)=0.4$.
- Policy A: return starting with a 1 is $1+\gamma^2+\gamma^4+\dots=1/(1-0.25)=4/3$. Starting with a 0 it is $\gamma+\gamma^3+\dots=0.5/0.75=2/3$. The average is $(4/3+2/3)/2=1$.
- Check: $r(A)/(1-\gamma)=0.5/0.5=1$ ✓.
- Policy B: return $=0.4/(1-0.5)=0.8$; check $0.4/0.5=0.8$ ✓.
- Ranking: $1>0.8$ and $0.5>0.4$, so A is better under both. Both scores are scaled by the same $1/(1-\gamma)=2$.

## Concepts
- [[semi-gradient-sarsa]] (new) — Sarsa update (10.2) with $\hat q(s,a,\mathbf w)$; the gradient is of $\hat q(S_t,A_t,\mathbf w_t)$ only (p. 244)
- [[n-step-return]] (new) — return with $n$ real rewards, then a bootstrapped $\hat q$ term (10.4) (p. 247)
- [[tile-coding]] (new) — overlapping offset grid tilings turn continuous states into binary features (p. 245)
- [[average-reward]] (new) — $r(\pi)$, long-run reward rate, used to rank policies without discounting (p. 249)
- [[ergodicity]] (new) — steady-state distribution exists and is independent of $S_0$; sufficient, not necessary, for the limit (10.6) (p. 249)
- [[differential-value-function]] (new) — value defined from returns of $R-r(\pi)$ (10.9) (p. 250)
- [[policy-improvement-theorem]] (new) — guarantee that improving one state's value improves the policy; lost with function approximation (p. 253)
- [[temporal-difference learning / reward prediction error]] — here the differential TD error (10.11) (p. 250)
- [[policy]] — here ranked by the scalar $r(\pi)$ (p. 249)
- [[exploration vs exploitation]] — optimistic initial values drive exploration (p. 246)
- [[Bellman equation / value function]] — differential Bellman equations without $\gamma$ (p. 250)
- [[Markov decision process]] — continuing MDP with stationary distribution $\mu_\pi$ (p. 249)

## Canonical instances
- [[mountain-car]] (new) — continuous control where progress requires first moving away from the goal; linear tile-coded Sarsa (p. 244)
- [[access-control-queuing]] (new) — tabular differential Sarsa; $\bar R\approx2.31$ (p. 252)

## Bridges (candidates)
- [same-math] stationary distribution $\mu_\pi$ in (10.8) ↔ Markov chains: a fixed point of the transition operator.
- [structural-analogy] Average reward $r(\pi)$ ↔ control theory: long-run average cost per time step as an objective.
- [structural-analogy] Arbitrary offset in differential values ↔ potentials defined only up to an additive constant.
- [metaphor] Mountain Car ("worse before better") ↔ control theory: systems whose response first moves the wrong way.

## Questions this raises
- If discounting cannot define the approximate control problem, what role does it play when used as a solution-method parameter?
- Can the arbitrary offset of differential Sarsa be removed (the author calls this open)?
- What replaces the policy improvement theorem for action-value methods with approximation?
- How should one choose β for $\bar R$, given the bias-versus-slowness trade-off in Exercise 10.9?

## Exercises worth doing
- Ex. 10.2 (p. 248) — one-step Expected Sarsa for control — difficulty: easy
- Ex. 10.6 (p. 251) — average reward and (10.13) differential values for an alternating reward stream — difficulty: medium
- Ex. 10.7 (p. 251) — differential values on a three-state ring — difficulty: medium
- Ex. 10.8 (p. 251) — why updating $\bar R$ with $\delta_t$ is better than with $R_{t+1}-\bar R_t$ — difficulty: medium
- Ex. 10.9 (p. 255) — unbiased constant-step-size trick for $\bar R$ — difficulty: hard

## Reading notes
- Printed page = pdf − 22. The page labels give both numbers.
- The text layer garbles symbols (γ, ε, δ, ∇). I checked equations against the page images.
- Fig. 10.5 text is jumbled in the text layer. I read the policy plot from the image: it shows a reject region for low priorities at few free servers.
- Footnote 2 (p. 246): the Mountain Car plots in Fig. 10.1 come from Sarsa(λ), not plain Sarsa.
- Exercises 10.1, 10.3, 10.4 and 10.5 are not in the list above. I did not solve any exercise.
