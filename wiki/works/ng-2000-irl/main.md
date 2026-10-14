---
id: ng-2000-irl/main
work: ng-2000-irl
unit: paper
pages: 1–7 (plus the unnumbered title page, cited here as p. 0)
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Algorithms for Inverse Reinforcement Learning (Ng & Russell)

## L0 — One line
Observed optimal behaviour in a Markov decision process (a model of states, actions, random transitions and rewards) fits a whole set of reward functions, which in the finite case is described by linear inequalities; the paper suggests heuristics, solved by linear programming, to help choose among them.

## L1 — The gist (≤ 120 words)
Inverse reinforcement learning (IRL) asks: if an agent is seen acting optimally in a Markov decision process (a model with states, actions, random transitions and rewards), which reward function is it optimizing? For finite state spaces, the paper describes all reward functions that make a given policy optimal, as linear inequalities. That set contains degenerate members such as R = 0, so the authors suggest heuristics: prefer rewards that make the observed policy better than single-step deviations, optionally penalizing large rewards. These can be written as linear programs (optimization with linear objective and linear constraints). Extensions cover large state spaces with linear basis functions and policies seen only through sampled trajectories. Simple experiments recover rewards that explain behaviour fairly well.

**Prerequisites:** Markov decision processes (states, actions, transition matrices, discount factor); value function and Bellman equation; vector/matrix notation; linear programming basics; Monte Carlo averaging.

## L2 — Key ideas (5–10 bullets)
- **Problem and motivation.** Given an agent's behaviour (plus, if needed, its sensory inputs and, if available, an environment model), find the reward being optimized. Two motivations: modelling animals and humans whose reward is unknown, and apprenticeship learning, where the authors propose recovering the reward rather than copying the policy (p. 0–1).
- **Characterization (Theorem 3).** In a finite MDP with $\gamma\in(0,1)$, the policy $\pi\equiv a_1$ is optimal if and only if $(P_{a_1}-P_a)(I-\gamma P_{a_1})^{-1}R\succeq 0$ for all other actions $a$ (p. 2).
- **Degeneracy.** $R=0$ (indeed any constant vector) always satisfies the condition. For most MDPs it also "seems likely" that many other solutions exist, so extra criteria are needed (p. 2–3).
- **Suggested selection heuristics.** Maximize the summed gap between the best action's Q-value and the next best (6). Optionally subtract an $\ell_1$ penalty $\lambda\|R\|_1$; to set $\lambda$ automatically, a value just below a phase transition "would be an appealing choice". The result is a linear program (p. 3).
- **Large state spaces.** Writing $R=\sum_i\alpha_i\phi_i$ makes the constraints linear in $\alpha$. Constraints are imposed on sampled states and relaxed with a penalty, which keeps the problem linear (p. 3–4).
- **Sampled trajectories.** An iterative LP uses Monte Carlo value estimates and a growing set of competing policies; no explicit model is needed, but an optimal-policy solver is assumed (p. 4–5).
- **Experiments.** In all experiments the authors recover a reward that "explains" the observed behaviour fairly well; the penalized 5×5 fit is very close to the true reward, and the mountain-car fits are judged to capture the main structure. On the continuous grid the authors compare policies and values: disagreement is typically 3–10%, and usually by about 15 iterations no significant value difference was detected (p. 5–6).
- **Open problems.** Rewards that are "easy" to learn from, noisy or suboptimal observations, locally consistent rewards, experiment design, and partial observability (p. 7).

## L3 — Walkthrough

### 1. Introduction (p. 0–1)
**Abstract/aims (p. 0).** The paper treats IRL in Markov decision processes: extracting a reward function from observed, optimal behaviour. Possible uses: apprenticeship learning, and ascertaining the reward being optimized by a natural system. It characterizes all rewards for which a given policy is optimal, then gives three algorithms. The first two assume the entire policy is known: tabulated rewards on a finite state space, and linear function approximation of the reward over a possibly infinite state space. The third assumes the policy is known only through a finite set of observed trajectories. A key issue throughout is *degeneracy*: many reward functions make the observed policy optimal (p. 0).

**Informal problem (Russell, 1998; p. 0).** *Given* (1) measurements of an agent's behaviour over time in a variety of circumstances, (2) if needed, measurements of the agent's sensory inputs, (3) if available, a model of the environment. *Determine* the reward function being optimized (p. 0).

**Two motivations (p. 0–1).**
1. Reinforcement learning is used as a computational model of animal and human learning, with support from behavioural and neurophysiological evidence. That literature assumes a fixed, known reward, for example a saturating function of nectar content in bee-foraging models. The authors say it "seems clear" that the reward must be treated as unknown, to be found empirically, especially for multiattribute rewards (e.g. a bee weighing nectar against flight distance, time and risk). In their words: "we must consider the reward function as an unknown to be ascertained through empirical investigation" (p. 0).
2. An agent designer may have only a rough idea of the reward that gives "desirable" behaviour. Imitation or apprenticeship learning usually assumes the aim is to learn a *policy*. The authors propose instead to recover the expert's reward and use it to generate behaviour. They suggest the reward often gives a much more parsimonious (compact) description of behaviour, and note that reinforcement learning rests on the presupposition that the reward is the most succinct, robust and transferable definition of a task (p. 0–1).

**Related work (p. 1).** To the authors' knowledge the task has not been well studied in computer science, control theory, psychology or biology. The closest work is in economics: multiattribute utility assessment (one-shot decisions), Sargent (1978) for the sequential case, and structural estimation of MDPs in econometrics. In control theory, Kalman posed in the early 1960s the recovery of the objective function of a deterministic linear system with quadratic costs; it was recently solved as a semidefinite program (Boyd et al., 1994) (p. 1).

**Outline (p. 1).** Section 2: definitions. Section 3: the set of rewards making a policy optimal, its degenerate members (e.g. the reward that is zero everywhere), and heuristics giving an LP. Section 4: large or infinite state spaces. Section 5: trajectories. Section 6: experiments. Section 7: conclusions. The authors say that in all experiments they can recover a reward that "explains" the observed behaviour fairly well (p. 1).

### 2. Notation and problem formulation (p. 1–2)
**2.1 MDPs (p. 1).** A finite MDP is a tuple $(S,A,\{P_{sa}\},\gamma,R)$: $S$ is a set of $N$ states; $A=\{a_1,\dots,a_k\}$ the actions; $P_{sa}(\cdot)$ the transition probabilities after taking $a$ in $s$; $\gamma\in[0,1)$ the discount factor; $R:S\to\mathbb R$ the reward function, bounded by $R_{\max}$ (written $R(s)$, not $R(s,a)$, for simplicity) (p. 1). A policy is any map $\pi:S\to A$. Value function and Q-function:
$$V^\pi(s_1)=\mathrm E\left[R(s_1)+\gamma R(s_2)+\gamma^2R(s_3)+\cdots\mid\pi\right],\qquad Q^\pi(s,a)=R(s)+\gamma\,\mathrm E_{s'\sim P_{sa}(\cdot)}[V^\pi(s')].$$
Optimal versions: $V^*(s)=\sup_\pi V^\pi(s)$, $Q^*(s,a)=\sup_\pi Q^\pi(s,a)$ (p. 1). For finite spaces, $\boldsymbol R$ and $\boldsymbol V^\pi$ are $N$-vectors, and $\boldsymbol P_a$ is the $N\times N$ matrix whose $(i,j)$ entry is the probability of moving from $i$ to $j$ under $a$. Also $\boldsymbol x\prec\boldsymbol y$ means $x_i<y_i$ for all $i$, and $\preceq$ is the non-strict version (p. 1–2). An optimal policy $\pi^*$ exists that maximizes $V^\pi(s)$ for all $s$ simultaneously (p. 2).

**2.2 Classical results (p. 2).**
- *Theorem 1 (Bellman equations).* For all $s\in S,a\in A$:
$$V^\pi(s)=R(s)+\gamma\sum_{s'}P_{s\pi(s)}(s')V^\pi(s')\tag{1}$$
$$Q^\pi(s,a)=R(s)+\gamma\sum_{s'}P_{sa}(s')V^\pi(s')\tag{2}$$
- *Theorem 2 (Bellman optimality).* $\pi$ is optimal if and only if, for all $s\in S$,
$$\pi(s)\in\arg\max_{a\in A}Q^\pi(s,a)\tag{3}$$

**2.3 The IRL problem (p. 2).** Given a finite $S$, actions $A$, transitions $\{P_{sa}\}$, $\gamma$ and a policy $\pi$ that is fully observed, find the set of rewards $R$ for which $\pi$ is optimal in $(S,A,\{P_{sa}\},\gamma,R)$. One may then pick among them using extra criteria. Without loss of generality (by renaming actions) $\pi(s)\equiv a_1$ (p. 2).

### 3. IRL in finite state spaces (p. 2–3)
**3.1 Characterization of the solution set (p. 2).**

*Theorem 3.* Let finite $S$, actions $A=\{a_1,\dots,a_k\}$, matrices $\{\boldsymbol P_a\}$ and $\gamma\in(0,1)$ be given. Then $\pi(s)\equiv a_1$ is optimal if and only if, for all $a=a_2,\dots,a_k$, the reward satisfies
$$(\boldsymbol P_{a_1}-\boldsymbol P_a)(\boldsymbol I-\gamma\boldsymbol P_{a_1})^{-1}\boldsymbol R\succeq 0.\tag{4}$$
Shapes: $\boldsymbol P_a$ is $N\times N$, $\boldsymbol R$ is $N\times1$, so (4) is $N$ inequalities per other action (p. 2).

*Proof (p. 2).* With $\pi\equiv a_1$, (1) reads $\boldsymbol V^\pi=\boldsymbol R+\gamma\boldsymbol P_{a_1}\boldsymbol V^\pi$, so
$$\boldsymbol V^\pi=(\boldsymbol I-\gamma\boldsymbol P_{a_1})^{-1}\boldsymbol R.\tag{5}$$
Footnote 1: $\boldsymbol I-\gamma\boldsymbol P_{a_1}$ is always invertible. A transition matrix has all eigenvalues in the unit circle. Since $\gamma<1$, $\gamma\boldsymbol P_{a_1}$ has all eigenvalues in the interior of the circle, so 1 is not one of its eigenvalues. Hence $\boldsymbol I-\gamma\boldsymbol P_{a_1}$ has no zero eigenvalue (p. 2). Substituting (2) into (3), $\pi\equiv a_1$ is optimal if and only if, for all $s\in S$, $a_1\equiv\pi(s)\in\arg\max_a\sum_{s'}P_{sa}(s')V^\pi(s')$. (added step: this uses that $R(s)$ does not depend on $a$ and $\gamma>0$.) This is equivalent to the following chain:
$$\sum_{s'}P_{sa_1}(s')V^\pi(s')\ge\sum_{s'}P_{sa}(s')V^\pi(s')\ \ \forall s,a$$
$$\Leftrightarrow\ \boldsymbol P_{a_1}\boldsymbol V^\pi\succeq\boldsymbol P_a\boldsymbol V^\pi\ \ \forall a\in A\setminus a_1$$
$$\Leftrightarrow\ \boldsymbol P_{a_1}(\boldsymbol I-\gamma\boldsymbol P_{a_1})^{-1}\boldsymbol R\succeq\boldsymbol P_a(\boldsymbol I-\gamma\boldsymbol P_{a_1})^{-1}\boldsymbol R\ \ \forall a\in A\setminus a_1,$$
where the last step uses (5) (p. 2). $\square$

*Remark (p. 2).* The author says it is easy to show, by essentially replacing all inequalities in the proof with strict ones, that $(\boldsymbol P_{a_1}-\boldsymbol P_a)(\boldsymbol I-\gamma\boldsymbol P_{a_1})^{-1}\boldsymbol R\succ0$ is necessary and sufficient for $\pi\equiv a_1$ to be the *unique* optimal policy (p. 2).

*Intuition note.* Condition (4) just says that, under the reward $R$, taking the observed action is at least as good as any alternative at every state. Because $\boldsymbol V^\pi$ is a fixed linear function of $\boldsymbol R$, this becomes a set of linear inequalities in $\boldsymbol R$.

**Two problems (p. 2–3).** (i) $\boldsymbol R=0$ (indeed any constant vector) is always a solution: the reward is the same whatever action is taken, so every policy, including $\pi\equiv a_1$, is optimal. Demanding that $\pi$ be the unique optimal policy would alleviate this but is "not entirely satisfying", since usually some reward vectors arbitrarily close to 0 would still be solutions (p. 2–3). (ii) For most MDPs, the author says it "seems likely" that there are many choices of $\boldsymbol R$ meeting (4). The original IRL statement does not say which to choose; the next section proposes natural criteria (p. 3).

**3.2 LP formulation and penalty terms (p. 3).** Linear programming can find a feasible point of (4), but some solutions may be less meaningful than others. The proposals below were chosen largely because they fit into an LP, but the author considers them fairly natural (p. 3).

*Criterion 1.* Among rewards satisfying (4) and $|R(s)|\le R_{\max}$, choose one that makes single-step deviations from $\pi$ as costly as possible, i.e. maximize
$$\sum_{s\in S}\Big(Q^\pi(s,a_1)-\max_{a\in A\setminus a_1}Q^\pi(s,a)\Big)\tag{6}$$
This is the summed gap between the best action and the next-best action. The author notes other criteria are possible, such as $\sum_s\sum_{a\in A\setminus a_1}\big(Q^\pi(s,a_1)-Q^\pi(s,a)\big)$ (p. 3).

*Criterion 2 (optional).* If we believe that, other things equal, solutions with mainly small rewards are "simpler", we may optionally subtract a weight-decay-like term $\lambda\|R\|_1$, where $\|R\|_1=\sum_i|R_i|$ (the $\ell_1$ norm) and $\lambda$ is an adjustable penalty coefficient. A side effect is that for sufficiently large $\lambda$, $R$ will often be nonzero in only a few states. The author also says it can be shown (assuming the solution is not already degenerate at $\lambda=0$) that as $\lambda$ increases there is a phase transition at some $\lambda_0$: the optimal $R$ is bounded away from 0 for $\lambda<\lambda_0$ and $R=0$ for $\lambda>\lambda_0$. To choose $\lambda$ automatically, $\lambda=\lambda_0^-$ (just before the transition, perhaps found by binary search) "would be an appealing choice". It gives the "simplest" $R$ (largest penalty) that is not zero everywhere, so that $R$ at least partially "explains" why $\pi$ is optimal (p. 3).

*Combined problem (p. 3).* With $\boldsymbol P_a(i)$ the $i$th row of $\boldsymbol P_a$:
$$\begin{aligned}\text{maximize}\quad&\sum_{i=1}^N\min_{a\in\{a_2,\dots,a_k\}}\big\{(\boldsymbol P_{a_1}(i)-\boldsymbol P_a(i))(\boldsymbol I-\gamma\boldsymbol P_{a_1})^{-1}\boldsymbol R\big\}-\lambda\|\boldsymbol R\|_1\\\text{s.t.}\quad&(\boldsymbol P_{a_1}-\boldsymbol P_a)(\boldsymbol I-\gamma\boldsymbol P_{a_1})^{-1}\boldsymbol R\succeq0\quad\forall a\in A\setminus a_1\\&|\boldsymbol R_i|\le R_{\max},\ i=1,\dots,N\end{aligned}$$
The author says this is easily written as a linear program and solved efficiently (p. 3).

*Intuition note.* Constraint (4) leaves a large set of possible rewards, so the authors add a preference. They favour rewards under which the observed action wins by a wide margin, and optionally rewards that are small and sparse. These preferences are heuristics, not consequences of the theorem.

### 4. Linear function approximation in large state spaces (p. 3–4)
**Setup (p. 3).** Take $S=\mathbb R^n$, and assume a subroutine that approximates $V^\pi$ for any particular MDP. $R$ is now a function $\mathbb R^n\to\mathbb R$; working over all such functions is hard algorithmically, so the authors use a linear approximation:
$$R(s)=\alpha_1\phi_1(s)+\alpha_2\phi_2(s)+\cdots+\alpha_d\phi_d(s)\tag{8}$$
with fixed, known, bounded basis functions $\phi_i:S\to\mathbb R$ and unknown parameters $\alpha_i$ (p. 3).

**Linearity of value (p. 3–4).** Let $V_i^\pi$ be the value function of $\pi$ when the reward is $R=\phi_i$. By linearity of expectations,
$$V^\pi=\alpha_1V_1^\pi+\cdots+\alpha_dV_d^\pi.\tag{9}$$
The author says the reader may easily verify, using essentially the argument of Theorem 3's proof, that the appropriate generalization of (4) for $R$ to make $\pi\equiv a_1$ optimal is
$$\mathrm E_{s'\sim P_{sa_1}}[V^\pi(s')]\ge\mathrm E_{s'\sim P_{sa}}[V^\pi(s')]\tag{10}$$
for all states $s$ and all $a\in A\setminus a_1$. By (9) these are linear constraints on the $\alpha_i$ (p. 4).

**Two problems and the fix (p. 4).** (i) With infinitely many states there are infinitely many constraints (10). The authors sample a large but finite subset $S_0$ of states and impose the constraints only there. (ii) The linear class (8) may not express any reward (other than $R=0$) for which $\pi$ is optimal. As a compromise, constraints may be relaxed at a penalty when violated. The final LP is:
$$\text{maximize }\sum_{s\in S_0}\min_{a\in\{a_2,\dots,a_k\}}\Big\{p\Big(\mathrm E_{s'\sim P_{sa_1}}[V^\pi(s')]-\mathrm E_{s'\sim P_{sa}}[V^\pi(s')]\Big)\Big\}\quad\text{s.t. }|\alpha_i|\le1,\ i=1,\dots,d$$
where $p(x)=x$ if $x\ge0$ and $p(x)=2x$ otherwise. The factor 2 is a heuristically chosen penalty weight for violating (10). The author reports the results did not seem very sensitive to it, with moderately larger values usually giving quite similar results. $V^\pi$ is an implicit linear function of the $\alpha_i$ via (9) (p. 4).

*Intuition note.* Writing the reward as a short weighted sum of fixed shapes turns the search over functions into a search over $d$ numbers. The policy-optimality conditions stay linear in those numbers. Where the shapes cannot satisfy every condition, violations are allowed but cost twice as much as satisfied margins gain.

### 5. IRL from sampled trajectories (p. 4–5)
**Setting (p. 4).** The policy $\pi$ is known only through actual trajectories. No explicit MDP model is required, but the authors assume they can find an optimal policy under any reward they choose, and can simulate trajectories (from the initial state $s_0$) under the optimal policy or any other policy of their choice. They fix an initial state distribution $D$ and look for $R$ such that the unknown policy maximizes $\mathrm E_{s_0\sim D}[V^\pi(s_0)]$. For simplicity they assume one start state $s_0$, which they say is without loss of generality because $s_0$ can be a "dummy" state whose next-state distribution is $D$. $R$ is expressed with (8) (p. 4).

**Estimating values (p. 4).** For a policy $\pi$, execute $m$ Monte Carlo trajectories. For each $i$, $\hat V_i^\pi(s_0)$ is the average empirical return over these trajectories if the reward had been $\phi_i$. For $m=1$ and a trajectory $(s_0,s_1,\dots)$: $\hat V_i^\pi(s_0)=\phi_i(s_0)+\gamma\phi_i(s_1)+\gamma^2\phi_i(s_2)+\cdots$. In general it is the average over the $m$ returns. Footnote 2: trajectories are truncated after a large finite $H$ steps. By discounting this adds only a small error; for $H=H_\epsilon=\log_\gamma(\epsilon(1-\gamma)/R_{\max})$, truncation adds at most $\epsilon$ error. Alternatively, a random-length trajectory of expected length $O(H_\epsilon)$ gives an unbiased estimate (Kearns et al., 1999) (p. 4). The estimate for any $\alpha$ is
$$\hat V^\pi(s_0)=\alpha_1\hat V_1^\pi(s_0)+\cdots+\alpha_d\hat V_d^\pi(s_0),\tag{11}$$
justified by $V^\pi(s_0)=\alpha_1V_1^\pi(s_0)+\cdots+\alpha_dV_d^\pi(s_0)$ (p. 4).

**Algorithm (p. 4–5).**
1. Compute value estimates for the given (assumed optimal) policy $\pi^*$ and for a "base case" policy $\pi_1$, which is a randomly chosen policy (p. 4).
2. *Inductive step.* With policies $\{\pi_1,\dots,\pi_k\}$, find $\alpha$ so that the resulting reward (hopefully) satisfies
$$V^{\pi^*}(s_0)\ge V^{\pi_i}(s_0),\quad i=1,\dots,k.\tag{12}$$
As before, the objective is modified slightly:
$$\text{maximize }\sum_{i=1}^kp\big(\hat V^{\pi^*}(s_0)-\hat V^{\pi_i}(s_0)\big)\quad\text{s.t. }|\alpha_i|\le1,\ i=1,\dots,d$$
with the same $p$ ($x$ if $x\ge0$, $2x$ otherwise; the 2 is again heuristic and results again did not seem extremely sensitive to it). Both $\hat V$ terms are implicit linear functions of $\alpha$ by (11), so this is an LP (p. 4–5).
3. This gives a new $R=\alpha_1\phi_1+\cdots+\alpha_d\phi_d$. Find a policy $\pi_{k+1}$ maximizing $V^\pi(s_0)$ under $R$, add it to the set, and repeat for some large number of iterations until an $R$ with which one is "satisfied" is found (p. 5).

*Intuition note.* The fitted reward must make the expert's policy look at least as good as every rival policy found so far. Each new reward produces a new best-response policy, which becomes a new rival, so the set of constraints grows.

### 6. Experiments (p. 5–6)
**5×5 grid (p. 5).** The agent starts at the lower-left square and must reach the absorbing upper-right square, where it receives reward 1. Actions try to move in the four compass directions, but have a 30% chance of moving in a random direction. Figure 1 shows an optimal policy and the true reward. The Section 3.2 algorithm *without* a penalty term recovers most of the reward structure (Fig. 2, top), but the result is slightly "bumpy". The author says some of this comes from arbitrary symmetry-breaking in the chosen policy. With $\lambda=1.05$, just below the phase transition, the recovered reward (Fig. 2, bottom) is very close to the true reward. Footnote 3: intermediate values such as $\lambda=0.5$ did not give smooth-looking functions; the author says this is not surprising, since small $\lambda$ gives many values near $\pm1$, large $\lambda$ many near 0, and intermediate $\lambda$ a mix (p. 5).

**Mountain-car (p. 5–6).** The state is the car's x-position and velocity. The true undiscounted reward is $-1$ per step until the goal at the top of the hill. Using the Section 4 algorithm, the reward is restricted to functions of x-position only, with all linear combinations of 26 evenly spaced Gaussian basis functions. The optimal policy given to the algorithm came from a fine 120×120 discretization (footnote 4); a sample of $|S_0|=5000$ states was used, not counting states that gave no nontrivial constraints (p. 6). A typical fitted reward (Fig. 4, top, note the y-axis scale) has "nearly perfectly captured" the $R=-c$ structure, per the author (p. 6). A harder variant has true reward 1 on $[-0.72,-0.32]$ around the hill's bottom and 0 elsewhere, with $\gamma=0.99$. The optimal policy is to go to the bottom as fast as possible and park, which is not always possible, e.g. when the car is near the right top and moving too fast. A typical solution (Fig. 4, bottom) has by and large recovered the structure, large and positive around the specified interval. It also has an artifact on the right side, which the authors believe comes from unavoidably "shooting off" the right end sometimes; they consider it a fairly good solution (p. 6).

**Continuous 5×5 grid (p. 6).** The state is $[0,1]\times[0,1]$. Each compass action moves the agent 0.2 in the intended direction; uniform noise in $[-0.1,0.1]$ is then added to each coordinate, and the state is truncated to stay in the unit square. The true reward is 1 in the (non-absorbing) square $[0.8,1]\times[0.8,1]$ and 0 elsewhere, with $\gamma=0.9$. The basis is a 15×15 array of two-dimensional Gaussians. $D$ is uniform over the state space; each policy is evaluated with $m=5000$ trajectories of 30 steps. The comparison "optimal" policy came from a 50×50 discretization. The fitted solution was usually already reasonable after 1 iteration, and by about 15 iterations the algorithm had usually settled on fairly good solutions. The fitted reward's optimal policy and the true optimal policy disagreed on typically 3–10% of the state space (Fig. 5, top). The author says that with many distinct near-optimal policies such variation is to be expected. A perhaps more appropriate measure compares the *quality* of the fitted reward's optimal policy with that of the true optimal policy, both measured with the true reward. Usually by about 15 iterations, evaluations with 50000 Monte Carlo trials of 50 steps each were unable to detect a statistically significant difference between the true optimal policy's value (about 6.65) and the fitted reward's optimal policy's value (Fig. 5, bottom; 5 runs) (p. 6–7).

*Intuition note.* Many distinct policies can be near-optimal, so some action disagreement is expected even from a good fit. The authors suggest that comparing the values of the two policies under the true reward is perhaps a more appropriate measure; by that measure, usually by about 15 iterations, they could not detect a significant difference.

### 7. Conclusions and future work (p. 7)
The results show that IRL is soluble, at least for moderate-sized discrete and continuous domains. Open questions listed by the authors:
- Potential-based shaping rewards (Ng et al., 1999) can make an MDP dramatically easier to learn without affecting optimality. Can IRL algorithms be designed that recover "easy" reward functions?
- Real applications may involve substantial noise in the observer's measurements of the agent's sensor inputs and actions. The agent's own action selection may be noisy and/or suboptimal, and there may be many optimal policies of which only a few are observed. What are appropriate metrics for fitting such data?
- If behaviour is strongly inconsistent with optimality, can "locally consistent" reward functions be identified for specific regions of the state space?
- How can experiments be designed to maximize identifiability of the reward function?
- How well does the approach carry over to partially observable environments? (p. 7)

## Toy example (ours, not from the paper)
Two states, two actions, $\gamma=0.5$. Action $a_1$ moves to state 1; $a_2$ moves to state 2, both with probability 1. So $\boldsymbol P_{a_1}=\begin{pmatrix}1&0\\1&0\end{pmatrix}$, $\boldsymbol P_{a_2}=\begin{pmatrix}0&1\\0&1\end{pmatrix}$. Observed policy: $\pi\equiv a_1$.

1. $\boldsymbol I-\gamma\boldsymbol P_{a_1}=\begin{pmatrix}0.5&0\\-0.5&1\end{pmatrix}$. Its inverse is $\begin{pmatrix}2&0\\1&1\end{pmatrix}$. Check: row 2 times column 1 is $-0.5\cdot2+1\cdot1=0$.
2. By (5): $\boldsymbol V^\pi=(2R_1,\ R_1+R_2)^\top$.
3. $\boldsymbol P_{a_1}-\boldsymbol P_{a_2}=\begin{pmatrix}1&-1\\1&-1\end{pmatrix}$, so (4) gives $\big(2R_1-(R_1+R_2),\ 2R_1-(R_1+R_2)\big)^\top=(R_1-R_2)(1,1)^\top\succeq0$. Solution set: $R_1\ge R_2$. This includes $R=(0,0)$ and $R=(1,1)$, which are degenerate.
4. Take $R_{\max}=1$. Each row of the Section 3.2 objective equals $R_1-R_2$ (only one rival action, so the min is trivial). The objective is $2(R_1-R_2)-\lambda(|R_1|+|R_2|)$ with $R_1\ge R_2$, $|R_i|\le1$.
5. Since $|R_1|+|R_2|\ge|R_1-R_2|=R_1-R_2$, the objective is at most $(2-\lambda)(R_1-R_2)$. For $\lambda<2$ this is at most $2(2-\lambda)$, because $R_1-R_2\le2$. This is attained at $R=(1,-1)$: $4-2\lambda$. For $\lambda>2$ the bound is $\le0$, and the only maximizer is $R=0$, with value 0. So the phase transition is at $\lambda_0=2$, and $\lambda_0^-$ gives the nonzero reward $(1,-1)$.

## Concepts
- [[inverse-reinforcement-learning]] — find the reward function that an observed (optimal) behaviour is optimizing (p. 0)
- [[markov-decision-process]] — tuple $(S,A,\{P_{sa}\},\gamma,R)$ as defined here (p. 1)
- [[policy]] — a map $\pi:S\to A$ (p. 1)
- [[bellman-equation]] — Theorems 1–2: value equations (1)–(2) and the optimality test (3) (p. 2)
- [[reward-degeneracy]] (new) — many rewards, including $R=0$, make the observed policy optimal (p. 0, p. 2)
- [[apprenticeship-learning]] (new) — learning skilled behaviour from an expert's behaviour; here via recovering the reward instead of the policy (p. 0)
- [[linear-reward-basis]] (new) — $R=\sum\alpha_i\phi_i$ with fixed known basis functions, so constraints are linear in $\alpha$ (p. 3)
- [[l1-penalty-phase-transition]] (new) — optional $\lambda\|R\|_1$ penalty; the optimal $R$ becomes 0 beyond some $\lambda_0$ (p. 3)

## Canonical instances
- [[bee-foraging-reward]] — example of a model with a fixed, known reward that the authors argue should be treated as unknown (p. 0)
- [[kalman-inverse-optimal-control]] — Kalman's early-1960s problem of recovering the objective of a deterministic linear system with quadratic costs, later solved as a semidefinite program (p. 1)
- [[gridworld-5x5]] — discrete test; unpenalized fit is slightly bumpy, $\lambda=1.05$ fit is very close to the truth (p. 5)
- [[mountain-car]] — continuous test with two true rewards, with fitted rewards judged by the authors to capture the main structure (p. 6)
- [[continuous-gridworld]] — sampled-trajectory test, judged by policy disagreement and policy value (p. 6–7)

## Bridges (candidates)
- [structural-analogy] IRL's reward recovery ↔ econometrics: structural estimation of MDPs (Rust, Sargent), cited on p. 1 as the closest prior work.
- [structural-analogy] Optional $\ell_1$ penalty $\lambda\|R\|_1$ with a sparsity-driven phase transition ↔ statistics: sparsity-promoting regularization; the penalty is used here to pick a simple solution from a set of equally consistent ones.
- [structural-analogy] The asymmetric penalty $p(x)$ on violated constraints ↔ optimization: piecewise-linear loss (hinge-like) that keeps the problem an LP.

## Questions this raises
- If potential-based shaping can change a reward without changing optimal behaviour (p. 7), which part of the solution set of (4) is genuinely identifiable from behaviour alone?
- How should the penalty weight $\lambda$ and the factor 2 in $p(x)$ be chosen when no true reward is available to check against?
- When the observer's measurements are noisy or the agent is suboptimal (p. 7), what replaces the exact inequalities (4) and (10)?
- Is comparing policy quality under the true reward, as in Fig. 5, available in real applications where the true reward is unknown?

## Reading notes
- The first page (title, authors, abstract, start of Section 1) shows no printed page number. The numbered pages that follow show printed page 1 on the second PDF page, so printed = pdf − 1. The unnumbered first page is cited here as "p. 0".
- The first page shows the title, authors Andrew Y. Ng and Stuart Russell, and the affiliation "Computer Science Division, U.C. Berkeley". No running headers, venue or copyright line are visible on these pages.
- The extracted text layer is heavily garbled (symbol-font equations); everything was read from the page images.
- Equation numbers printed in the text are (1)–(6) and (8)–(12). The LP given after (6) on p. 3 and the LPs in Sections 4 and 5 carry no number, and no (7) is visible.
- The Section 3.2 objective has no $\gamma$ factor, as printed; the Q-gaps in (6) differ from it by a constant factor $\gamma$ (added observation, from (2) and (5)).
- Figures 1–5 were read as images; only values stated in the text (e.g. 6.65, 3–10%, $\lambda=1.05$) are used here.
