---
id: sutton-2018-rl/ch08-planning
work: sutton-2018-rl
unit: "Chapter 8 — Planning and Learning with Tabular Methods"
pages: 159–194
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
# Planning and Learning with Tabular Methods

## L0 — One line
Planning (using a model) and learning (using real experience) are both done by small backing-up updates to value functions, so they can share one algorithm and differ mainly in the source of experience; the key design question is which updates to do and where to focus them.

## L1 — The gist (≤ 120 words)
How can learning from real experience and planning with a model be treated as one thing? The chapter shows that both estimate value functions by small backing-up updates; they differ mainly in whether experience is real or simulated by a model. Dyna combines acting, model learning, direct RL and planning. The chapter then studies which updates to do: prioritized sweeping, expected versus sample updates, on-policy trajectory sampling, real-time DP, and planning at decision time (heuristic search, rollouts, Monte Carlo Tree Search). It matters because computation, not only data, limits large problems, and focusing updates saves computation.

**Prerequisites:** MDPs and value functions; Q-learning and one-step TD; DP (value iteration, policy improvement); Monte Carlo returns; ε-greedy and UCB; asynchronous DP.

## L2 — Key ideas (5–10 bullets)
- A model predicts next state and reward. A distribution model gives all outcomes with probabilities; a sample model gives one sampled outcome. Sample models are often much easier to obtain (pp. 159–160).
- Planning = any computation that takes a model and produces or improves a policy. State-space planning computes value functions by backups on simulated experience, the same structure as the learning methods (pp. 160–161).
- Dyna-Q (a simple agent architecture) runs direct RL (learning values straight from real experience), model learning and planning together, using the same Q-learning update on real and simulated experience. In the maze, more planning steps gave much faster learning (pp. 162–165).
- A wrong model can mislead planning. Optimistic model errors tend to be found and corrected quickly; if the world becomes better than the model says, the error may go unnoticed for a long time, if ever. Exploration bonuses (Dyna-Q+) help (pp. 166–168).
- Planning can be focused: prioritized sweeping (a queue that orders updates by urgency) works backward from states whose values changed. Sample updates (one sampled successor) can beat expected updates (all successors) when the branching factor (number of possible next states) is large (pp. 168–174).
- Trajectory sampling (updating along simulated runs of the current policy) and RTDP (real-time dynamic programming, a value-iteration version of it) focus updates on states reached under the current policy. This helps early and for large problems, and can lose in the long run on small ones (pp. 174–180).
- Decision-time planning (heuristic search = a lookahead tree with backed-up values; rollouts = Monte Carlo trials from the current state; MCTS = Monte Carlo Tree Search, rollouts plus a growing tree) computes values for the current state, uses them to pick an action, then mostly discards them. The gain of deeper search comes from focus, not multistep updates as such (pp. 180–188).
- Part I methods vary along dimensions: update width, depth, on/off-policy, and others. Function approximation is left to Part II (pp. 189–191).

## L3 — Walkthrough

### 8.1 Models and Planning (pp. 159–161)
- **Model**: anything an agent can use to predict how the environment responds to its actions: given state and action, it predicts next state and reward (p. 159).
- **Distribution model**: lists all possibilities with probabilities. **Sample model**: returns one possibility drawn by those probabilities. Example: sum of a dozen dice. A distribution model lists all sums and their probabilities; a sample model returns one sum (pp. 159–160).
- DP's $p(s',r\mid s,a)$ is a distribution model; the blackjack simulator of Chapter 5 is a sample model (p. 160).
- A distribution model can always produce samples, so it is stronger. But sample models are often much easier to build (dice: easy to simulate, harder to enumerate) (p. 160).
- Models simulate experience: a sample model gives a transition (or, with a policy, an episode); a distribution model gives all transitions or episodes with probabilities (p. 160).
- **Planning** (this book's meaning): any computation that takes a model as input and produces or improves a policy (p. 160).
- **State-space planning** searches the state space; value functions are over states. **Plan-space planning** searches the space of plans (includes evolutionary methods and partial-order planning). The authors say plan-space methods are hard to apply efficiently to stochastic sequential decision problems and do not consider them (p. 160).
- Unified view: (1) state-space planning computes value functions as a step toward a better policy; (2) it does so by backup updates on simulated experience. Diagram: model → simulated experience → (updates/backups) → values → policy (p. 160).
- DP fits: sweeps over states, using each state's distribution of transitions as the backed-up value. The authors argue that various other state-space planning methods also fit this structure, differing only in the kind of update, the order, and how long backed-up information is retained (pp. 160–161).
- Planning and learning share value estimation by backups. The difference: planning uses simulated experience, learning uses real experience. Hence a learning algorithm can often replace the update step of a planning method (p. 161).

**Random-sample one-step tabular Q-planning** (p. 161), loop forever:
1. select $S\in\mathcal S$, $A\in\mathcal A(S)$ at random;
2. send $S,A$ to a sample model, get $R,S'$;
3. $Q(S,A)\leftarrow Q(S,A)+\alpha\,[R+\gamma\max_a Q(S',a)-Q(S,A)]$.

It converges to the optimal policy *for the model* under the conditions of one-step tabular Q-learning: every pair selected infinitely often in Step 1, and $\alpha$ decreasing appropriately (p. 161).

*Intuition note.* Planning is, in effect, learning from imagined (model-generated) experience. The Q-learning update does not care whether the transition really happened or was drawn from a model.

A second theme: planning in small incremental steps lets planning be interrupted or redirected with little waste, which matters when mixing planning with acting and model learning (p. 161).

### 8.2 Dyna: Integrated Planning, Acting, and Learning (pp. 161–166)
- Real experience has two roles: **model-learning** (improve the model) and **direct RL** (improve values/policy directly). Using experience via the model to improve values/policy is **indirect RL**; planning is part of it (p. 162).
- Indirect methods often use limited experience more fully and need fewer environment interactions. Direct methods are simpler and not affected by model-design biases (p. 162).
- **Authors' view:** the contrast between direct/indirect (and cognition/trial-and-error, deliberation/reaction) has been exaggerated; the similarities are more instructive (p. 162). Some others (voice: unnamed "some") argue indirect methods are always superior, and others that direct methods explain most human and animal learning (p. 162).
- **Dyna-Q** includes planning, acting, model-learning and direct RL, all continually. Planning is random-sample one-step tabular Q-planning; direct RL is one-step tabular Q-learning. The model is a table assuming a deterministic environment: after $S_t,A_t\to R_{t+1},S_{t+1}$ it stores that outcome. Planning samples only previously experienced pairs, so the model is never queried about an unseen pair (pp. 162–163).
- **Search control**: the process that picks starting states and actions for simulated experience. The RL method is the "final common path" for learning and planning (p. 163; Figure 8.1).
- In each time step the acting, model-learning and direct RL steps are cheap; the remaining time is used for $n$ planning iterations (pp. 163–164).

**Tabular Dyna-Q** (p. 164): initialise $Q(s,a)$, $Model(s,a)$. Loop forever:
- (a) $S\leftarrow$ current state; (b) $A\leftarrow\varepsilon$-greedy$(S,Q)$; (c) take $A$, observe $R,S'$;
- (d) $Q(S,A)\leftarrow Q(S,A)+\alpha[R+\gamma\max_a Q(S',a)-Q(S,A)]$;
- (e) $Model(S,A)\leftarrow R,S'$ (deterministic environment);
- (f) repeat $n$ times: $S\leftarrow$ random previously observed state; $A\leftarrow$ random action previously taken in $S$; $R,S'\leftarrow Model(S,A)$; same Q update.

Without (e),(f) it is one-step tabular Q-learning (p. 164).

**Example 8.1, Dyna Maze** (pp. 164–165): 47 states, four deterministic actions (blocked moves leave the agent in place). Reward 0 except +1 on entering the goal; episodic, $\gamma=0.95$. Settings: initial $Q=0$, $\alpha=0.1$, $\varepsilon=0.1$, random tie-breaking, average over 30 repetitions with the same seed, so the first episode (about 1700 steps) was identical for all $n$. Results: the $n=0$ agent was by far the slowest even with parameters optimised for it, taking about 25 episodes to reach ($\varepsilon$-)optimal performance; $n=5$ took about 5; $n=50$ took about 3 (p. 164). Why (Figure 8.3, halfway through episode 2): without planning each episode adds one step to the policy. With $n=50$, a long policy has been built by planning while the agent is still near the start, reaching almost back to the start state by the end of episode 2 (p. 165).

*Intuition note.* Without planning, the news "the goal is here" crawls backward one step per episode. With planning, the model lets the agent replay that news many times between real steps.

- Because planning is incremental, it is trivial to intermix with acting. The agent is "always reactive and always deliberative." As the model changes, planning gradually computes behaviour matching the new model (p. 166).

### 8.3 When the Model Is Wrong (pp. 166–168)
- Models may be wrong because of limited samples in a stochastic environment, imperfect generalisation by function approximation, or because the environment changed unobserved. Then planning is likely to compute a suboptimal policy (p. 166).
- If the model is **optimistic** (predicts more reward or better transitions than possible), the planned policy tries to exploit them and discovers they do not exist (p. 166). In some cases this quickly leads to discovery and correction of the modelling error; the authors say this tends to happen when the model is optimistic (p. 166).
- **Example 8.2, Blocking Maze**: a short path exists for 1000 steps, then it is blocked and a longer path opens. Both Dyna-Q and Dyna-Q+ found the new path after a flat period of no reward (pp. 166–167; Figure 8.4).
- Harder: the environment becomes *better* but the old policy does not reveal it. The error may go undetected for a long time, if ever (p. 166).
- **Example 8.3, Shortcut Maze**: after 3000 steps a shorter path opens on the right, leaving the long path intact. Dyna-Q never switched; its model said no shortcut existed, so more planning made it less likely to explore there. Even ε-greedy is very unlikely to find it. Dyna-Q+ did (p. 167).
- In planning, **exploration** = trying actions that improve the model; **exploitation** = acting optimally for the current model. The authors say there probably is no perfect and practical solution, but simple heuristics are often effective (pp. 167–168).
- **Dyna-Q+** keeps, for each pair, the time $\tau$ since it was last tried in real interaction. In planning updates, a transition with modelled reward $r$ is treated as giving reward
$$r+\kappa\sqrt{\tau}$$
for a small $\kappa$. This encourages testing long-untried transitions, even through long action sequences (p. 168).
- Footnote 1: Dyna-Q+ also (i) lets never-tried actions be considered in planning step (f), and (ii) initialises their model as leading back to the same state with reward zero (p. 168).

*Intuition note.* The longer a pair has been untried, the more likely (we might presume) the model of it is wrong, so planning treats it as if it paid extra. This is "computational curiosity" with a cost.

Exercises 8.2–8.5 are on p. 168.

### 8.4 Prioritized Sweeping (pp. 168–171)
- Uniformly random choice of simulated transitions is usually not best. Early in episode 2 of the maze, only the pair leading into the goal has positive value, so most updates move between zero-valued states and have no effect (pp. 168–169).
- **Backward focusing**: work back from any state whose value has changed (not only goal states). Useful one-step updates are those of actions leading into the changed state; their predecessors may then change, and so on, until the propagation stops (p. 169).
- Not all changes are equally urgent. **Prioritized sweeping** keeps a queue of state–action pairs whose estimated value would change nontrivially, ordered by the size of change. After updating the top pair, the effect on each predecessor is computed; if above a small threshold, the predecessor is inserted with its priority (keeping only the higher priority if already queued) (p. 169).

**Prioritized sweeping, deterministic environment** (p. 170):
- Initialise $Q$, $Model$, empty PQueue. Loop forever: (a) $S\leftarrow$ current state; (b) $A\leftarrow policy(S,Q)$; (c) take $A$, observe $R,S'$; (d) $Model(S,A)\leftarrow R,S'$;
- (e) $P\leftarrow|R+\gamma\max_a Q(S',a)-Q(S,A)|$; (f) if $P>\theta$, insert $S,A$ with priority $P$;
- (g) repeat $n$ times while PQueue is not empty: $S,A\leftarrow first(PQueue)$; $R,S'\leftarrow Model(S,A)$; Q-update as in Dyna-Q; for all $\bar S,\bar A$ predicted to lead to $S$: $\bar R\leftarrow$ predicted reward; $P\leftarrow|\bar R+\gamma\max_a Q(S,a)-Q(\bar S,\bar A)|$; if $P>\theta$, insert with priority $P$.

- **Example 8.4**: on mazes like Figure 8.2 but with varying grid resolution, prioritized sweeping often speeds finding optimal solutions by a factor of 5 to 10, with both methods making at most $n=5$ updates per interaction (p. 170).
- **Example 8.5, Rod maneuvering**: a rod moves around obstacles; four actions, 20×20 positions, 10-degree rotation steps, 14,400 potential states. The problem is probably too large for unprioritized methods (p. 171).
- Stochastic case: keep counts of experienced pairs and next states, and use expected updates (p. 170).
- Authors' caveat: prioritized sweeping is "probably not the best way"; expected updates may waste computation on low-probability transitions. Sample updates can break backup computation into smaller pieces, which can be focused on those with the most impact. "Small backups" (van Seijen and Sutton, 2013) go to the limit: single-transition updates using the transition's probability without sampling (pp. 170–171).
- The authors suggest that all kinds of state-space planning can be viewed as sequences of value updates, varying only in type (expected/sample, large/small) and order. Backward focusing is one strategy; **forward focusing** (by reachability from frequently visited states) is another (p. 171).

### 8.5 Expected vs. Sample Updates (pp. 172–174)
- One-step updates vary on three binary dimensions: state vs action values; optimal vs given policy ($v_*,q_*,v_\pi,q_\pi$); expected vs sample. That gives eight cases, seven of which are specific algorithms (Figure 8.6): e.g. policy evaluation / TD(0) for $v_\pi$, value iteration for $v_*$ (expected), Sarsa for $q_\pi$ (sample), Q-learning for $q_*$ (sample). The eighth case does not seem to correspond to any useful update (p. 172).
- Dyna-Q uses $q_*$ sample updates. For stochastic problems, prioritized sweeping is always done using one of the expected updates (p. 172).
- Expected updates are exact up to errors in successor values but cost more; computation is often the limiting resource in planning. For $q_*$ with tabular $Q$ and model $\hat p$ (p. 173):
$$Q(s,a)\leftarrow\sum_{s',r}\hat p(s',r\mid s,a)\Big[r+\gamma\max_{a'}Q(s',a')\Big]\tag{8.1}$$
$$Q(s,a)\leftarrow Q(s,a)+\alpha\Big[R+\gamma\max_{a'}Q(S',a')-Q(s,a)\Big]\tag{8.2}$$
- If only one next state is possible, the two are identical (with $\alpha=1$). They differ to the extent that the environment is stochastic (p. 173).
- Let $b$ be the **branching factor**: number of $s'$ with $\hat p(s'\mid s,a)>0$. An expected update costs roughly $b$ times a sample update, since cost is dominated by the number of pairs where $Q$ is evaluated (p. 173).
- If time suffices for an expected update, it is generally better than $b$ sample updates. If time does not suffice, sample updates are always preferable, since they improve the estimate with fewer than $b$ updates (p. 173).
- **Analysis (Figure 8.7)**: all $b$ successors equally likely, initial error 1, successor values correct. The expected update reduces the error to zero on completion. After $t$ sample updates with $\alpha=1/t$, the error is
$$\sqrt{\frac{b-1}{bt}}.$$
For moderately large $b$, error falls dramatically within a tiny fraction of $b$ updates (p. 174).
- This advantage is "probably an underestimate": in real problems successor values are themselves being updated, so more accurate estimates sooner help backed-up values too. Conclusion: sample updates are likely superior on problems with large stochastic branching factors and too many states to solve exactly (p. 174).

*Intuition note.* For large $b$ the error falls dramatically within a tiny fraction of $b$ updates. (added step) With $b=10{,}000$ and $t=100$ sample updates, $\sqrt{(b-1)/(bt)}\approx0.1$, i.e. a tenth of the initial error, at 1% of the cost of one expected update. Spread that saving over many pairs, not one.

Exercise 8.6 is on p. 174.

### 8.6 Trajectory Sampling (pp. 174–177)
- Classical DP does exhaustive sweeps, which may not finish on large tasks and give equal time to irrelevant states. Sweeps are not essential to DP: updates can be distributed any way, though for convergence all pairs must be visited infinitely often in the limit (with an exception in 8.7) (p. 175).
- Sampling uniformly (as in Dyna-Q) has some of the same problems. More appealing: the **on-policy distribution**, generated by **trajectory sampling**: simulate trajectories with the model and current policy, updating the pairs encountered. It is easy to generate; an explicit representation would cost about as much as a complete policy evaluation and changes whenever the policy changes (p. 175).
- Plausibility (author's): like studying chess positions that arise in real games. Part II will show on-policy advantages with function approximation (p. 175).
- **Experiment** (pp. 175–176): one-step expected tabular updates (8.1) only. *Uniform*: cycle through all pairs. *On-policy*: simulate episodes from one start state, ε-greedy ($\varepsilon=0.1$). Random undiscounted episodic tasks: $|\mathcal S|$ states, 2 actions each, each to $b$ equally likely next states (random per pair), 0.1 probability of termination on every transition, expected reward from Gaussian mean 0, variance 1. Performance = $v_{\tilde\pi}(s_0)$ of the greedy policy $\tilde\pi$ under the model. Averages over 200 tasks, 1000 states, $b=1,3,10$; plus 10,000 states with $b=1$.
- **Result**: on-policy sampling gave faster planning initially and retarded planning in the long run. The effect was stronger, and the initial advantage longer, at smaller $b$ and with more states (large and long-lasting for 10,000 states, $b=1$) (p. 176).
- Explanation (author's): early on, on-policy focuses on near descendants of the start state. Later, commonly visited states already have correct values, so sampling them is useless. Results are not conclusive (random tasks) but suggest on-policy sampling can be a great advantage for large problems where a small part of the space is visited (pp. 176–177).

*Intuition note.* Focusing helps while there is unexplored value near where you actually go; once that is learned, revisiting it wastes effort.

Exercises 8.7–8.8 are on p. 177.

### 8.7 Real-time Dynamic Programming (pp. 177–180)
- **RTDP**: on-policy trajectory-sampling version of value iteration. It applies expected tabular value-iteration updates (4.10) to states visited in real or simulated trajectories. It is an asynchronous DP algorithm, so DP theory can be adapted (p. 177).
- For prediction with designated start states, states unreachable under the given policy are irrelevant and skipped. For control, states not reachable from any start state by any optimal policy are irrelevant; what is needed is an **optimal partial policy**, optimal on relevant states, arbitrary or undefined elsewhere (pp. 177–178).
- Finding it with an ordinary on-policy control method (e.g. Sarsa) generally needs all pairs visited infinitely often, which can be arranged, e.g., by exploring starts. For episodic tasks with exploring starts, RTDP converges to optimal policies for discounted finite MDPs (and for the undiscounted case under certain conditions) (p. 178).
- **Key result**: for certain problems, RTDP finds a policy optimal on the relevant states without visiting every state infinitely often, or without visiting some at all. Setting: undiscounted episodic tasks with absorbing goal states with zero reward. At each step it takes a greedy action (random ties) and does the expected value-iteration update on the current state; it may also update other states (p. 178).
- **Theorem (stated; proved by Barto, Bradtke, Singh, 1995)**: with each episode starting from a randomly chosen start state and ending at a goal, RTDP converges with probability one to a policy optimal on all relevant states, provided (1) initial value of every goal state is zero, (2) at least one policy reaches a goal with probability one from any start state, (3) all rewards from non-goal states are strictly negative, (4) all initial values are equal to or greater than the optimal values (satisfied by setting all initial values to zero) (p. 178).
- These are **stochastic optimal path problems**, usually stated as cost minimisation. Examples: minimum-time control (reward −1 per step; the page text drops the minus sign) and the Golf example (p. 178).

**Example 8.6, RTDP on the Racetrack** (pp. 179–180)
- Rewards −1 per step until the finish line is crossed (sign inferred; see Reading notes); hitting the boundary moves the car to a random start state. No speed limit, but the set of states reachable from start states under any policy is finite. The small track has 9,115 reachable states, of which only 599 are relevant (estimated by counting states visited under optimal actions over $10^7$ episodes) (p. 179).
- Conventional DP: in-place (Gauss–Seidel) value iteration with exhaustive sweeps, about twice as fast as the Jacobi version here. Initial values 0. DP stopped when max change in a sweep $<10^{-4}$. RTDP updated only the current state each step and was judged converged when average crossing time over 20 episodes stabilised. Averages over 25 runs (p. 179).

| | DP | RTDP |
|---|---|---|
| Computation to convergence | 28 sweeps | 4000 episodes |
| Updates to convergence | 252,784 | 127,600 |
| Updates per episode | — | 31.9 |
| States updated ≤100 times | — | 98.45% |
| States updated ≤10 times | — | 80.51% |
| States updated 0 times | — | 3.18% |

- Both policies averaged 14–15 steps. RTDP used roughly half the updates. About 290 states were never updated in an average run (p. 180).
- Another RTDP advantage: its behaviour policy is always greedy for the current values, so it approaches optimal as values approach $v_*$. Value iteration might have a nearly optimal greedy policy long before it terminates; checking this is not part of conventional DP. In the racetrack, a close-to-optimal policy emerged after 15 sweeps (136,725 updates), still more than RTDP's 127,600 (p. 180).
- Authors: not a definitive comparison; RTDP focus became increasingly narrow, and by the convergence theorem it would eventually focus only on relevant states (p. 180).

*Intuition note.* RTDP concentrates its updates on states visited along (real or simulated) trajectories that follow the greedy policy, so much of the irrelevant part of the state space is updated rarely or never (in the racetrack, about 290 of 9,115 states were never updated).

### 8.8 Planning at Decision Time (pp. 180–181)
- **Background planning** (so far): simulated experience gradually improves a policy or value function. It is not focused on the current state; planning happened well before the action is chosen (pp. 180–181).
- **Decision-time planning**: planning begun and completed after each new state $S_t$, whose output is one action $A_t$. Simplest case: compare model-predicted next-state values; more generally look much deeper. It focuses on a particular state (p. 181).
- Values and policy made this way are typically discarded after the action is chosen. This is often little loss since states rarely recur; one may mix both uses (p. 181).
- Decision-time planning is most useful when fast responses are not required (chess: seconds or minutes per move). If low latency matters, background planning to compute a policy that is applied quickly is generally better (p. 181).

### 8.9 Heuristic Search (pp. 181–183)
- **Heuristic search**: for each state, consider a large tree of continuations, apply the approximate value function at the leaves, back values up to the root (same as expected max-updates for $v_*$, $q_*$), choose the best action, discard the backed-up values (p. 181).
- Conventionally the value function is hand-designed and not changed by search. It is natural to let it improve using backed-up values or other methods. Greedy, ε-greedy and UCB selection are like heuristic search on a smaller scale; heuristic search extends greedy beyond one step (p. 182).
- With a perfect model and an imperfect action-value function, deeper search will *usually* yield better policies (footnote 2: interesting exceptions exist). Search to the end of the episode removes the value function's effect and gives an optimal action. Deeper search costs more time (p. 182).
- **TD-Gammon**: TD learning of an afterstate value function through self-play, with heuristic search to pick moves; model = known dice probabilities plus an opponent assumed to choose what TD-Gammon rates best for it. Tesauro found that deeper search gave better moves but slower play. Only selective search a few steps ahead was feasible, yet it significantly improved moves (p. 182).
- Much of the effectiveness is due to the tree being focused on states and actions that may immediately follow the current state, and the limited memory devoted to them (chess programs store estimates for millions of positions seen from one position) (pp. 182–183).
- A search tree can be viewed as a sequence of one-step updates done bottom-up (Figure 8.9). With tabular values this gives exactly the same overall update as depth-first heuristic search. So the gain from deeper search is "not due to the use of multistep updates as such" but to the focus of updates on states and actions just downstream of the current state (p. 183).

### 8.10 Rollout Algorithms (pp. 183–185)
- **Rollout algorithms**: decision-time Monte Carlo control on simulated trajectories all starting at the current state. For each action, average the returns of many simulations that start with it and then follow a given **rollout policy**. Execute the best action, then repeat from the next state. The name comes from backgammon "rolling out" a position with random dice (pp. 183–184).
- Unlike Chapter 5, they do not estimate a full $q_*$ or $q_\pi$; they estimate values only for the current state, use them, and discard them. So no per-pair sampling or function approximation is needed (p. 184).
- Why they work: by the policy improvement theorem, if $\pi'$ equals $\pi$ except $\pi'(s)=a\neq\pi(s)$ and $q_\pi(s,a)\ge v_\pi(s)$, then $\pi'$ is as good as or better than $\pi$; strict inequality gives strictly better. Averaging simulated returns estimates $q_\pi(s,a')$; acting greedily on these and then following $\pi$ is a good candidate for improving on $\pi$. It is like one step of policy iteration, or more like one step of asynchronous value iteration since only the current state's action changes (p. 184).
- **Aim**: to improve the rollout policy, not to find an optimal policy. Tesauro and Galperin were surprised by dramatic backgammon improvements; in some applications even a completely random rollout policy can work. Intuition suggests that better rollout policies and more accurate estimates give better results ("but see Gelly and Silver, 2007") (p. 184).
- Trade-off: better rollout policies cost more time. Computation depends on number of actions, trajectory length, rollout-policy decision time and number of trajectories. Ways to ease it: run independent trials in parallel; truncate trajectories and correct with a stored evaluation function; prune unlikely actions (which complicates parallelism) (pp. 184–185).
- Not ordinarily seen as learning (no long-term memory), but they use sample-based Monte Carlo estimation on a sample model, avoid sweeps by trajectory sampling, and exploit policy improvement by acting greedily (p. 185).

### 8.11 Monte Carlo Tree Search (pp. 185–188)
- **MCTS**: at its base a rollout algorithm, plus accumulation of value estimates to direct later simulations toward more rewarding trajectories. Run after each new state. Reported impact: computer Go from weak amateur (2005) to grandmaster level (6 dan or more) in 2015; a variant (Section 16.6) was critical to AlphaGo's 2016 wins. It also works on single-agent problems if the model is simple enough for fast multistep simulation (p. 185).
- Simulated trajectories use a simple **rollout policy** beyond the tree. Value estimates (average simulated returns) are kept only for pairs in a tree rooted at the current state, which is extended incrementally. Inside the tree an informed **tree policy** (e.g. ε-greedy or UCB) balances exploration and exploitation (pp. 186–187).
- **Four steps per iteration** (Figure 8.10, p. 187):
 1. *Selection*: from the root, the tree policy traverses the tree to a leaf node.
 2. *Expansion*: on some iterations, add one or more child nodes via unexplored actions.
 3. *Simulation*: from the selected node (or a new child), simulate a complete episode with the rollout policy.
 4. *Backup*: the return updates or initialises action values on edges traversed by the tree policy. No values are saved for rollout-policy states beyond the tree.
- Repeat until time or another resource runs out. Then pick a root action from the accumulated statistics: e.g. largest action value, or largest visit count to avoid outliers (p. 187).
- After the environment moves on, MCTS restarts from a single root or from the retained subtree of descendants; other nodes and their values are discarded (p. 187).
- For two-person games, each simulated episode is one full game. AlphaGo extends MCTS with action values learned by a deep network via self-play RL (Section 16.6) (p. 187).
- Why it works (authors): it benefits from online, sample-based value estimation and policy improvement; the tree stores action values updated by sample updates, concentrating trials on trajectories whose initial segments are common to earlier high-return ones. The growing tree is a lookup table for a partial action-value function, avoiding global approximation while still using experience to guide exploration (p. 188).

*Intuition note.* MCTS is a rollout algorithm that remembers, within the current decision, which opening moves looked good, so later simulations are spent on those (many implementations also keep part of the tree for the next decision).

### 8.12 Summary of the Chapter (pp. 188–189)
- DP needs a distribution model (expected updates); sample updates need only a sample model, which is generally much easier to obtain (p. 188).
- Planning and learning estimate the same value functions by small backups. Any learning method can become a planning method by running it on simulated experience; the two can be possibly identical algorithms on different experience sources (p. 188).
- Planning, acting and model-learning interact circularly; asynchronous parallel operation is most natural; if resources are shared, division can be nearly arbitrary (p. 188).
- Dimensions of variation: size of updates (smaller = more incremental) and distribution of updates (backward focus: prioritized sweeping; on-policy focus: trajectory sampling, RTDP; forward focus: decision-time planning, heuristic search, rollouts, MCTS) (p. 189).

### 8.13 Summary of Part I: Dimensions (pp. 189–191)
- All Part I methods share three ideas: estimate value functions; back up values along actual or possible trajectories; follow generalized policy iteration (GPI), i.e. maintain approximate value function and policy and improve each from the other. The authors suggest these are powerful organizing principles potentially relevant to any model of intelligence (p. 189).
- Figure 8.11: horizontal = width (sample vs expected updates); vertical = depth (degree of bootstrapping). Corners: TD (shallow, sample), DP (shallow, expected), Monte Carlo (deep, sample), exhaustive search (deep, expected). Between: n-step methods, heuristic search, mixed methods (pp. 189–190).
- A third dimension is on-policy vs off-policy. Other dimensions listed (p. 191): definition of return; action vs state vs afterstate values; action selection/exploration; synchronous vs asynchronous; real vs simulated; location of updates; timing of updates; memory for updates. They are neither exhaustive nor mutually exclusive.
- The most important dimension not covered in Part I is function approximation, an orthogonal spectrum from tabular to nonlinear; Part II covers it (p. 191).

*Bibliographical remarks (pp. 192–193)* attribute Dyna to Sutton (1990); "direct/indirect" and "system identification" to the adaptive control literature; prioritized sweeping to Moore and Atkeson (1993) and Peng and Williams (1993); the RTDP convergence result to Barto, Bradtke and Singh (1995); and MCTS to Coulom (2006) and Kocsis and Szepesvári (2006).

## Toy example (ours, not from the text)
Chain: states A, B, goal G. Action "right" moves A→B and B→G deterministically. Reward 0 on A→B and +1 on B→G. Use $\gamma=0.9$, $\alpha=1$, all $Q=0$ initially. Compare $n=0$ with $n=1$ planning step per real step.

- Real step 1: A, right → $R=0$, $S'=$B. Update: $Q(A,r)=0+0.9\cdot\max_a Q(B,a)-0=0$. Model stores (A,r)→(0,B). Planning ($n=1$): the only stored pair is (A,r); it gives $Q(A,r)=0+0.9\cdot0=0$.
- Real step 2: B, right → $R=1$, goal (terminal, value 0). Update: $Q(B,r)=0+1\,[1+0-0]=1$. Model stores (B,r)→(1,G).
- Planning, $n=1$. The pair is chosen at random from {(A,r),(B,r)}.
 - If (A,r) is chosen: $Q(A,r)=0+1\,[0+0.9\cdot\max_a Q(B,a)-0]=0.9\cdot1=0.9$.
 - If (B,r) is chosen: $Q(B,r)$ is recomputed as 1 and nothing changes (probability ½ this step).
- With $n=0$: after episode 1, $Q(A,r)=0$. The agent needs episode 2 to reach A→B again and pick up value 0.9.
- With $n=1$: with probability ½, $Q(A,r)=0.9$ already after episode 1. With larger $n$ it becomes more likely. This is the Dyna-Maze effect (value spreads backward during episode 1) in miniature.

## Concepts
- [[model-based vs model-free RL]] — model-based methods plan with a model; model-free learn directly; this chapter treats them as intermixable (p. 159)
- [[planning]] (new) — any computation taking a model and producing or improving a policy (p. 160)
- [[distribution-vs-sample-model]] (new) — full outcome probabilities vs one sampled outcome; sample models are easier to get (p. 159)
- [[dyna-architecture]] (new) — acting, model-learning, direct RL and planning all running, sharing one RL update (p. 162)
- [[direct-vs-indirect-rl]] (new) — direct: learn values from real experience; indirect: learn via the model (p. 162)
- [[exploration vs exploitation]] — here, exploration means testing actions to improve the model; exploitation means acting optimally for the current model (p. 167)
- [[exploration-bonus]] (new) — Dyna-Q+ gives planning updates extra reward $\kappa\sqrt\tau$ for long-untried pairs (p. 168)
- [[prioritized-sweeping]] (new) — queue of pairs ordered by size of expected value change; updates propagate backward (p. 169)
- [[expected-vs-sample-update]] (new) — exact average over successors (costs ≈ $b$×) vs one sampled successor (p. 173)
- [[trajectory-sampling]] (new) — distribute updates along simulated on-policy trajectories (p. 175)
- [[real-time-dynamic-programming]] (new) — on-policy trajectory-sampling value iteration; converges on relevant states under stated conditions (p. 177)
- [[decision-time-planning]] (new) — planning begun and finished at each state to pick one action; results mostly discarded (p. 181)
- [[heuristic-search]] (new) — tree of continuations with backed-up leaf values; extends greedy beyond one step (p. 181)
- [[rollout-algorithm]] (new) — Monte Carlo action-value estimates for the current state under a rollout policy (p. 183)
- [[monte-carlo-tree-search]] (new) — rollouts plus a growing tree of stored action values: selection, expansion, simulation, backup (pp. 185, 187)
- [[temporal-difference learning / reward prediction error]] — the Q-learning step used for both learning and planning (p. 161)
- [[policy]] — the policy improvement theorem supports the view that acting greedily on rollout estimates is a good candidate for improving the rollout policy (p. 184)

## Canonical instances
- [[dyna-maze]] — more planning steps give much faster learning (Example 8.1, p. 164)
- [[blocking-maze]] — optimistic-model error corrected after a path is blocked (Example 8.2, p. 166)
- [[shortcut-maze]] — Dyna-Q misses an improvement; Dyna-Q+ finds it (Example 8.3, p. 167)
- [[rod-maneuvering]] — prioritized sweeping on 14,400 states (Example 8.5, p. 171)
- [[expected-vs-sample-error-curve]] — error $\sqrt{(b-1)/(bt)}$ vs computation (Figure 8.7, p. 174)
- [[random-task-trajectory-experiment]] — uniform vs on-policy update distribution (Figure 8.8, p. 176)
- [[racetrack-rtdp]] — RTDP uses ≈ half the updates of DP (Example 8.6, p. 179)
- [[td-gammon]] — deeper search gives better but slower moves (p. 182)
- [[computer-go-mcts]] — MCTS and Go progress 2005–2016 (p. 185)

## Bridges (candidates)
- [structural-analogy] Decision-time planning (replan after every state, execute one action) ↔ control theory: model predictive control — repeated finite-horizon planning with only the first action applied.
- [structural-analogy] Direct vs indirect RL; model-learning = "system identification" (p. 192) ↔ adaptive control: direct vs indirect adaptive control.
- [structural-analogy] Dyna-Q's model-learning running beside acting ↔ observer/estimator: a model corrected by data and used for decisions.
- [structural-analogy] Expected vs sample updates ↔ statistics: exact expectation vs Monte Carlo average, with error shrinking as $t$ grows.
- [same-math] RTDP and other asynchronous updates (4.10) ↔ dynamic programming: Gauss–Seidel / asynchronous value iteration.
- [metaphor] "Always reactive and always deliberative" Dyna agent ↔ psychology: habit vs goal-directed behaviour (the book relates this in Section 14.6).

## Questions this raises
- How do planning and model learning behave when the model is learned by function approximation instead of a table (Part II)?
- Can exploration bonuses be added without distorting the value estimates, e.g. used only in action selection (Exercise 8.4)?
- When is on-policy focusing harmful in the long run, and can one switch from on-policy to uniform updates to get both advantages?
- How much should a decision-time planner store between decisions, and how should that be balanced against fast response?

## Exercises worth doing
- Ex. 8.1 (p. 166) — compare multi-step bootstrapping with Dyna's planning on the maze — difficulty: medium
- Ex. 8.2 (p. 168) — why Dyna-Q+ also wins in the first phase — difficulty: medium
- Ex. 8.4 (p. 168) — programming: use the bonus only in action selection, not in updates — difficulty: hard
- Ex. 8.5 (p. 168) — extend Dyna-Q to stochastic and changing environments — difficulty: medium
- Ex. 8.6 (p. 174) — does a skewed successor distribution strengthen the case for sample updates? — difficulty: medium
- Ex. 8.8 (p. 177) — programming: replicate Figure 8.8 lower part and try $b=3$ — difficulty: hard

## Reading notes
- Printed = pdf − 22 (e.g. pdf 181 = p. 159). The last page (pdf 216, printed 194) is blank.
- The text layer garbles symbols (⇥, ⇤, "2" for ∈, "←" lost, etc.). Where an image was provided (pp. 163–165, 167, 173–174, 176, 183, 186, 189–190) I checked equations (8.1), (8.2) and the algorithm boxes against it.
- No image was given for pp. 161, 168, 170, 178–179 (among others). On those pages the text layer drops $\gamma$, $\kappa$ and minus signs: I wrote $\gamma$ in the Q-planning and prioritized-sweeping boxes by analogy with the Dyna-Q box (p. 164, image checked), and $\kappa$ in the Dyna-Q+ bonus by context ("for some small ..."). The racetrack reward and $10^{-4}$ threshold appear as "1" and "10 4"; I read them as −1 and $10^{-4}$ by context. "107" episodes is read as $10^7$ (superscript flattened).
- Figure 8.7's x-axis values and Figure 8.8's curves were read from the images only as labels, not as numbers.
- Chapter-ending bibliographical remarks are summarised in one line only; the running header on p. 193 reads "8.13 Summary of Part I: Dimensions" (p. 192 has the chapter header).
