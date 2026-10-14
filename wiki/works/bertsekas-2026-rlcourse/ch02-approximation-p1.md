---
id: bertsekas-2026-rlcourse/ch02-approximation-p1
work: bertsekas-2026-rlcourse
unit: "2 Approximation in Value Space - Rollout Algorithms (part 1/7): Secs. 2.1–2.3.1 and the start of 2.3.2"
pages: 163–189
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Deterministic finite-horizon DP, approximation in value space, and rollout with cost improvement

## L0 — One line
In a deterministic finite-horizon problem, a rollout algorithm replaces the unknown optimal cost-to-go by the cost of a cheap base heuristic, and it is guaranteed to do no worse than that heuristic when the heuristic is sequentially consistent or sequentially improving.

## L1 — The gist (≤ 120 words)
Exact DP for deterministic problems (shortest paths on a graph) is often intractable because the state space is huge. Approximation in value space runs the forward optimal-control construction with an approximate cost-to-go (estimated remaining cost) instead. Rollout builds this approximation on-line: for each control, it runs a base heuristic from the resulting next state and picks the control with the smallest Q-factor. The unit proves that the rollout policy costs no more than the base heuristic, under sequential consistency or the weaker sequential improvement. It gives a counterexample when neither holds, and introduces the fortified rollout as a repair. The price is extra computation of roughly a low-order polynomial factor times the heuristic's cost.

**Prerequisites:** backward dynamic programming (cost-to-go); shortest paths on layered graphs; proof by induction; the idea of a heuristic as an arbitrary rule that picks controls.

## L2 — Key ideas (5–10 bullets)
- With a deterministic system, minimizing over control sequences gives the same optimal cost as minimizing over policies. This is why the chapter can use base heuristics that are more general than policies (p. 167).
- A finite-state deterministic problem is a shortest-path problem on an acyclic graph with an artificial terminal node. Some such problems (for example scheduling, routing, and $N$ queens with large $N$) are too large for exact DP in practice (p. 169, p. 171, p. 180).
- Approximation in value space is the forward construction (2.6) with $\tilde J_{k+1}$ in place of $J^*_{k+1}$. Here $J^*_{k+1}$ is the optimal cost-to-go (the optimal cost of finishing from the next state). Minimizing the one-step expression is the same as minimizing the approximate Q-factor, i.e. the stage cost plus $\tilde J_{k+1}$ at the next state (p. 173–174).
- Rollout takes $\tilde J_{k+1}=H_{k+1}$, the cost of a base heuristic run from the next state (a base heuristic is any cheap rule that finishes the problem from a state). It needs at most $Nn$ heuristic runs, where $n$ bounds the controls per state (p. 178–179).
- Sequential consistency (the heuristic "stays the course") means the heuristic is a legitimate DP policy. It implies cost improvement $J_{k,\tilde\pi}\le H_k$ (Prop. 2.3.1) (p. 183–185).
- Sequential improvement, $\min_u \tilde Q_k\le H_k$, is weaker than consistency but still gives the same guarantee. It also makes the successive trajectories $T_k$ monotonically no worse (p. 186–187).
- Without sequential improvement, rollout can be strictly worse than its heuristic (Example 2.3.3). The fortified rollout keeps the best trajectory found so far to repair this (p. 188–189).

## L3 — Walkthrough

### Chapter introduction (p. 165)
- The chapter treats algorithms that predict future costs from the current state: approximation in value space and rollout. It focuses mainly on finite state and control spaces (p. 165).
- Sections 2.1–2.6 treat finite-horizon deterministic problems. A finite horizon suits rollout, and determinism removes the need for costly on-line Monte Carlo simulation (p. 165).
- Deterministic structure allows extensions that do not extend to stochastic problems: multistep lookahead, constraints on the whole trajectory, and heuristics more general than policies (p. 165).
- Finite-state deterministic problems also frame discrete optimization (integer programming, scheduling, assignment, routing) (p. 165).
- Sections 2.7–2.11 treat stochastic uncertainty; Section 2.12 treats minimax problems (p. 165).
- The author says the methods apply to infinite-horizon problems too, because value-space approximation and rollout are essentially finite-stage algorithms. The horizon type affects only the terminal cost approximation (p. 165).
- A finite-horizon problem can be turned into an infinite-horizon one with an artificial cost-free termination state (Sections 1.6.3–1.6.4, referred to). The author uses this to carry over the Chapter 1 "Newton's method" insights (p. 165).

### 2.1 Deterministic finite horizon problems (p. 166–172)
**Setup.** The state evolves by
$$x_{k+1}=f_k(x_k,u_k),\quad k=0,\dots,N-1,\tag{2.1}$$
with $x_k\in X_k$, control $u_k\in U_k(x_k)$, stage cost $g_k(x_k,u_k)$ and terminal cost $g_N(x_N)$. The sets and functions may depend on $k$ (p. 166). The cost of a control sequence is
$$J(x_0;u_0,\dots,u_{N-1})=g_N(x_N)+\sum_{k=0}^{N-1}g_k(x_k,u_k),\tag{2.2}$$
and $J^*(x_0)=\min J(x_0;u_0,\dots,u_{N-1})$ over $u_k\in U_k(x_k)$, $k=0,\dots,N-1$ (p. 166).

**Sequences versus policies.** In the stochastic case, policies $\pi=\{\mu_0,\dots,\mu_{N-1}\}$ can beat control sequences. In the deterministic case, optimizing over sequences gives the same optimal cost. The reason is that a policy's cost from a given state fixes the controls and future states with certainty, so a sequence can reproduce it (p. 167).

**DP algorithm** (backward, p. 167):
$$J^*_N(x_N)=g_N(x_N),\tag{2.3}$$
$$J^*_k(x_k)=\min_{u_k\in U_k(x_k)}\Big[g_k(x_k,u_k)+J^*_{k+1}\big(f_k(x_k,u_k)\big)\Big].\tag{2.4}$$
The author recalls from Section 1.2 that
$$J^*_k(x_k)=\min_{u_m\in U_m(x_m),\,m=k,\dots,N-1}J(x_k;u_k,\dots,u_{N-1}),\tag{2.5}$$
where $J(x_k;u_k,\dots,u_{N-1})=g_N(x_N)+\sum_{t=k}^{N-1}g_t(x_t,u_t)$. So $J_k^*(x_k)$ is the optimal cost of the $(N-k)$-stage tail subproblem, called the optimal cost-to-go, and $J^*_0(x_0)=J^*(x_0)$ (p. 167–168).

**Forward construction of an optimal sequence** (p. 168). Given $J^*_1,\dots,J^*_N$: set $u_0^*\in\arg\min_{u_0}[g_0(x_0,u_0)+J_1^*(f_0(x_0,u_0))]$ and $x_1^*=f_0(x_0,u_0^*)$. Then for $k=1,\dots,N-1$:
$$u^*_k\in\arg\min_{u_k\in U_k(x^*_k)}\Big[g_k(x^*_k,u_k)+J^*_{k+1}\big(f_k(x^*_k,u_k)\big)\Big],\quad x^*_{k+1}=f_k(x^*_k,u^*_k).\tag{2.6}$$
This splits into off-line training (computing $J^*_k$ by precomputation) and on-line play (computing $u_k^*$), analogous to chess and backgammon in Section 1.1 (p. 168).

> *Intuition note.* The backward pass tabulates "cost of finishing from here". The forward pass then just picks, at each state, the move that is best given that table. The approximation in value space of Section 2.2 and the rollout of Section 2.3 keep the forward pass and change the table (p. 173, p. 178).

**Finite-state problems as shortest paths** (p. 168–169). States are nodes of an acyclic graph and state–control pairs are arcs. An arc $(x_k,u_k)$ has cost $g_k(x_k,u_k)$ and ends at $f_k(x_k,u_k)$. An artificial terminal node $t$ is joined to each $x_N$ by an arc of cost $g_N(x_N)$. The problem is then equivalent to finding a shortest path from the stage-0 initial nodes to $t$ (Fig. 2.1.2). Efficient polynomial shortest-path algorithms exist. Still, some practical problems have astronomically many nodes; deterministic scheduling problems, for example, have a node count that grows exponentially with the number of tasks. For these, neither exact DP nor any other shortest-path algorithm can compute an exact optimum in practice, and the author proposes suboptimal methods such as rollout (p. 169).

**Example 2.1.1 (Four queens)** (p. 169–171). Four queens must be placed on a $4\times4$ board with no mutual attack. The formulation places queens row by row. Only the first two squares of the top row are used, since the other two give symmetric positions. The root node is the empty board. Terminal positions are those where no further queen can be added. Each terminal position is connected to the artificial node $t$ by an arc. This arc costs 1 if the position has fewer than four queens (a dead end) and 0 otherwise; all other arcs cost 0 (Fig. 2.1.3). The problem is then a minimal-cost path from $s$ to $t$, and a placement that solves it has cost 0 (p. 171).
- Once the nodes are enumerated the problem is essentially solved. For $N$ queens on an $N\times N$ board, though, the state space grows fast: for $N=8$ there are $8^8=16{,}777{,}216$ placements with one queen per row (p. 171).
- Solutions exist for all $N\ge4$, and effective non-DP search algorithms exist for very large $N$ (p. 171).
- Backward DP must consider all terminal positions, which are too many for large $N$. A forward DP exists (the backward algorithm applied to the reversed graph, Section 2.4), but it cannot cure the large-state-space problem (p. 171).

**Discrete optimization problems** (p. 171–172). Minimizing $G(u)$ over a finite set $U$, with $u=(u_0,\dots,u_{N-1})$, fits the framework with state $x_{k}=(u_0,\dots,u_{k-1})$, $x_{k+1}=(x_k,u_k)$, and only a terminal cost $G(x_N)=G(u)$ (Fig. 2.1.4) (p. 172).

**Example 2.1.2 (Constraint programming)** (p. 172–173). A feasibility problem has $G(u)\equiv0$: find a $u$ satisfying the constraints. The four queens and the breakthrough problem are instances. Constraints $h_k(u_k,u_{k+1})\le0$, $u_k\in U_k$, can be turned into the penalty problem of minimizing $\sum_{k=1}^{N}\max\{0,h_k(x_k,u_k)\}$ subject to $x_{k+1}=u_k$ and $u_k\in U_k$. This gives no guarantee of finding a complete feasible solution even if one exists. It only aims, suboptimally, to minimize a measure of total violation; in the process it may find a complete feasible solution, or an infeasible solution that is adequate for practical purposes (p. 173).

### 2.2 Approximation in value space — deterministic problems (p. 173–177)
**The scheme.** The forward construction (2.6) needs $J^*_k$ for all $x_k$ and $k$, which is often prohibitively time-consuming. Replace $J^*_k$ by approximations $\tilde J_k$: set $\tilde u_0\in\arg\min_{u_0}[g_0(x_0,u_0)+\tilde J_1(f_0(x_0,u_0))]$, $\tilde x_1=f_0(x_0,\tilde u_0)$, and for $k=1,\dots,N-1$
$$\tilde u_k\in\arg\min_{u_k\in U_k(\tilde x_k)}\Big[g_k(\tilde x_k,u_k)+\tilde J_{k+1}\big(f_k(\tilde x_k,u_k)\big)\Big],\quad\tilde x_{k+1}=f_k(\tilde x_k,\tilde u_k).\tag{2.7}$$
(p. 173).

**Q-factors.** The minimized expression is the approximate Q-factor
$$\tilde Q_k(x_k,u_k)=g_k(x_k,u_k)+\tilde J_{k+1}\big(f_k(x_k,u_k)\big),$$
so $\tilde u_k\in\arg\min_{u_k}\tilde Q_k(\tilde x_k,u_k)$ (p. 174). One could use off-line trained approximate Q-factors directly. The author warns that, unlike cost approximation, performance may then be degraded by errors in training the Q-factors, depending on how the training is done (p. 174).

**Exploiting structure.** One may choose $\tilde J_{k+1}$ so that the lookahead minimization is fast. A noteworthy case is multiagent problems with decomposable structure, where separable approximations decompose the minimization (p. 174).

**Example 2.2.1 (Multidimensional assignment)** (p. 174–177).
- *Problem.* The graph has $N+1$ layers $\mathcal N_0,\dots,\mathcal N_N$ of $m$ nodes each, with $N\ge2$ and a unique arc between each node and each node of an adjacent layer. A grouping is one node per layer. Each grouping has a cost depending on its $N$-tuple of arcs. An $(N+1)$-dimensional assignment partitions the nodes into $m$ disjoint groupings, and its cost is the sum of the groupings' costs. The aim is a minimum-cost assignment (Fig. 2.2.1). If grouping costs do not decompose into sums of arc costs, exact solution is very difficult; if they did, the problem would split into $N$ easy 2-dimensional assignment problems (p. 175).
- *DP formulation.* Stage $k$ selects $u_k=\{(i_n,j_n)\mid n=1,\dots,m\}$, a one-to-one assignment between layers $\mathcal N_k$ and $\mathcal N_{k+1}$ (2.8). The cost is $G(u_0,\dots,u_{N-1})$, the state is $x_k=(u_0,\dots,u_{k-1})$, and $x_{k+1}=(x_k,u_k)$. The exact DP is $J^*_N(x_N)=G(u_0,\dots,u_{N-1})$ and $J^*_k(x_k)=\min_{u_k\in U_k}J^*_{k+1}(x_k,u_k)$ (p. 175–176).
- *Approximation.* Choose $\tilde J_{k+1}(x_k,u_k)=\sum_{(i,j)\in u_k}c^{ij}_{k+1}(x_k)$. The lookahead $\min_{u_k}\tilde J_{k+1}(x_k,u_k)$ is then a 2-dimensional assignment problem, solvable by fast algorithms such as the Hungarian method or the auction algorithm. The arc costs must be computed for every arc $(i,j)$ between layers $\mathcal N_k$ and $\mathcal N_{k+1}$ (p. 176).
- *Arc costs.* They may depend in complicated ways on past choices $x_k$ and on future choices, possibly determined by a heuristic. In Fig. 2.2.2 they are computed by extending the trajectory heuristically along "most likely" arcs over a truncated horizon of $m$ steps ($m=2$ in the figure) (p. 176–177).

**Multistep lookahead** (p. 177). $\ell$-step lookahead, $1<\ell<N-k$, solves an $\ell$-step deterministic DP problem with terminal approximation $\tilde J_{k+\ell}$. It typically performs better than one-step lookahead (AlphaZero chess uses long lookahead). It costs more, but determinism and the single initial state $x_k$ limit the tree's growth. Approximate solution of the lookahead is deferred to Section 2.4 (p. 177).

> *Intuition note.* Approximation in value space is "plan one move ahead using a guess of the future". Looking several steps ahead typically performs better than one step, at the price of more computation (p. 177). The guess can be any approximation, which is where rollout enters (p. 178).

### 2.3 Rollout algorithms for discrete optimization (p. 177–183)
**Definition.** Rollout obtains $\tilde J_{k+1}(x_{k+1})$ in (2.7) when needed by running a base heuristic from $x_{k+1}=f_k(x_k,u_k)$, for each $u_k\in U_k(x_k)$, for a suitably large number of steps (p. 178). The base heuristic can be any method that, from $x_{k+1}$, generates controls $u_{k+1},\dots,u_{N-1}$, the states $x_{k+2},\dots,x_N$, and the cost
$$H_{k+1}(x_{k+1})=g_{k+1}(x_{k+1},u_{k+1})+\cdots+g_{N-1}(x_{N-1},u_{N-1})+g_N(x_N).$$
This $H_{k+1}$ is used as $\tilde J_{k+1}$ (p. 178). The pure form discussed has one-step lookahead, no truncation and no terminal cost approximation (p. 178).

**Rollout policy.**
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}\tilde Q_k(x_k,u_k),\tag{2.9}$$
$$\tilde Q_k(x_k,u_k)=g_k(x_k,u_k)+H_{k+1}\big(f_k(x_k,u_k)\big).\tag{2.10}$$
This defines the rollout policy $\tilde\pi=\{\tilde\mu_0,\dots,\tilde\mu_{N-1}\}$ (Fig. 2.3.1) (p. 179).

**Cost of computation.** The base heuristic is run at most $Nn$ times, with $n$ an upper bound on the number of controls per state. If $n$ is small relative to $N$, the cost is a small multiple of $N$ heuristic runs. If $n$ is bounded by a polynomial in $N$, the ratio to the heuristic's time is a polynomial in $N$ (p. 179).

**Example 2.3.1 (Multi-vehicle routing)** (p. 179–181).
- *Problem.* $m$ vehicles move along graph arcs. Each task is performed once, when a vehicle first reaches its node. The cost is one unit per vehicle move, summed until all tasks are done. Exact DP is intractable: the state (vehicle positions plus pending tasks) grows exponentially with the numbers of tasks and vehicles (p. 180).
- *Base heuristic.* Each vehicle selfishly moves one step along a shortest path toward its nearest pending task (Fig. 2.3.2: two vehicles, tasks at nodes 7 and 9) (p. 180).
- *Rollout from the state (1,2).* The joint moves lead to (3,5), (4,5), (3,4), (4,4). From (3,5) the heuristic goes (6,2), then (9,4) (task at 9 done), then (12,7) (task at 7 done), "a total of 6 vehicle moves once the move to (3,5) has been made". From (3,4) it goes (6,7) (task 7 done), then (9,4) (task 9 done), for "a total of 6 vehicle moves". The author states that (3,4) gives the minimum first-stage cost plus heuristic cost, so rollout moves to (3,4) (p. 181).
- *Outcome.* Rollout started from (1,2) attains the optimal cost of 6 vehicle moves. The base heuristic alone goes (4,4), (7,7), (10,10), (12,12), (9,9), a total of 10 moves (p. 181).
- *Cost of rollout.* Its computation grows exponentially with $m$, because the number of joint moves does. Multiagent rollout (Section 2.9) addresses this (p. 181).

**Example 2.3.2 (Breakthrough problem)** (p. 181–183).
- *Problem.* A binary tree has $N$ stages, with $2^k$ nodes at stage $k$. Each arc is free or blocked, and a free path from root to a leaf is sought (Fig. 2.3.3) (p. 182).
- *Exact DP.* Working backwards, step $k$ costs $O(2^{N-k})$. The total is $O(N2^N)$, exponential in $N$ (p. 182).
- *Greedy heuristic.* Take a free arc if exactly one is free. Otherwise use a fixed rule depending only on the current node. It costs $O(N)$ but can fail even when a free path exists (p. 182–183).
- *Rollout with the greedy base heuristic.* For random trees (each arc free or blocked independently with given probability $p$), an analysis in [Ber17a] Section 6.4 shows that asymptotically rollout needs $O(N)$ times more computation but has an $O(N)$ times larger probability of finding a free path. The author calls this tradeoff qualitatively typical: a substantial improvement at the price of the heuristic's time times a low-order polynomial factor in problem size (p. 183).

### 2.3.1 Cost improvement — sequential consistency, sequential improvement (p. 183–188)
The base heuristic may be a greedy algorithm, local search, a genetic algorithm, etc. The author expects rollout to be no worse than the heuristic, but says special conditions must hold to guarantee it. Two conditions are given (from [BTW97]) (p. 183).

**Definition 2.3.1 (sequential consistency).** If the heuristic, started at $x_k$, generates $\{x_k,u_k,x_{k+1},u_{k+1},\dots,x_N\}$, then started at $x_{k+1}$ it generates $\{x_{k+1},u_{k+1},\dots,x_N\}$ (p. 183). It "stays the course" (p. 184).
- The nearest-neighbor heuristic of the TSP Example 1.2.3 and the heuristics of Example 2.3.1 are sequentially consistent. Greedy/myopic heuristics are similar examples (p. 184).
- Most practical heuristics satisfy it at "most" states, but some may violate it at some states (p. 184).
- A consistent heuristic applies the same control at a state wherever that state sits in a heuristic trajectory. Hence a base heuristic is sequentially consistent if and only if it defines a legitimate DP policy (p. 184).
- *Footnote on ties* (p. 184). For sequential consistency, ties in greedy heuristics must be broken by a fixed rule. Randomizing among equally ranked controls violates sequential consistency and can seriously degrade rollout.

**Proposition 2.3.1 (cost improvement under sequential consistency).** For the rollout policy $\tilde\pi$ from a sequentially consistent base heuristic,
$$J_{k,\tilde\pi}(x_k)\le H_k(x_k),\quad\text{for all }x_k\text{ and }k.\tag{2.11}$$
*Proof* (induction, p. 185). For $k=N$: $J_{N,\tilde\pi}=H_N=g_N$. Assume the claim for $k+1$. Let $\bar u_k$ be the control the base heuristic applies at $x_k$. Then
$$\begin{aligned}J_{k,\tilde\pi}(x_k)&=g_k\big(x_k,\tilde\mu_k(x_k)\big)+J_{k+1,\tilde\pi}\Big(f_k\big(x_k,\tilde\mu_k(x_k)\big)\Big)\\&\le g_k\big(x_k,\tilde\mu_k(x_k)\big)+H_{k+1}\Big(f_k\big(x_k,\tilde\mu_k(x_k)\big)\Big)\\&=\min_{u_k\in U_k(x_k)}\Big[g_k(x_k,u_k)+H_{k+1}\big(f_k(x_k,u_k)\big)\Big]\\&\le g_k(x_k,\bar u_k)+H_{k+1}\big(f_k(x_k,\bar u_k)\big)\\&=H_k(x_k).\end{aligned}\tag{2.12}$$
- First equality: the DP equation for the rollout policy.
- First inequality: the induction hypothesis.
- Second equality: the definition of rollout.
- Second inequality: the minimum is at most its value at $\bar u_k$ (added step).
- Last equality: the DP equation for the policy of the base heuristic; this is where sequential consistency is needed (p. 185).

The author says the improvement cannot be easily quantified but is determined by the performance of the Newton step associated with the rollout policy, so it can be very substantial (p. 184).

> *Intuition note.* Rollout is allowed to deviate from the heuristic's first move only when that looks cheaper, and the heuristic then finishes the job. Consistency makes "the heuristic's cost from here" equal to the cost of the move the heuristic actually makes, so the one-step minimum cannot be worse.

**Definition 2.3.2 (sequential improvement).** The heuristic is sequentially improving if for all $x_k$ and $k$
$$\min_{u_k\in U_k(x_k)}\tilde Q_k(x_k,u_k)\le H_k(x_k).\tag{2.13}$$
In words: minimal heuristic Q-factor at $x_k\le$ heuristic cost at $x_k$ (p. 186).
- Sequential consistency implies sequential improvement. For a consistent heuristic, $H_k(x_k)=\tilde Q_k(x_k,\bar u_k)=g_k(x_k,\bar u_k)+H_{k+1}(f_k(x_k,\bar u_k))$, which is at least the minimal Q-factor (p. 186).

**Proposition 2.3.2 (cost improvement under sequential improvement).** For the rollout policy from a sequentially improving heuristic, $J_{k,\tilde\pi}(x_k)\le H_k(x_k)$ for all $x_k$ and $k$. *Proof:* take the calculation (2.12) and replace its last two steps (which rely on consistency) by (2.13) (p. 186).

**Monotonic improvement.** Let $T_0$ be the base heuristic's trajectory from $x_0$ and $T_N$ the final rollout trajectory. Let $T_k=(x_0,\tilde u_0,\tilde x_1,\tilde u_1,\dots,\tilde x_k,u_k,\dots,x_{N-1},u_{N-1},x_N)$ for $k=1,\dots,N-1$. Here the tail $(\tilde x_k,u_k,\dots,x_N)$ is the heuristic's trajectory from $\tilde x_k$. By the sequential improvement condition (Fig. 2.3.4), it can be proved that
$$\text{Cost of }T_0\ge\cdots\ge\text{Cost of }T_k\ge\text{Cost of }T_{k+1}\ge\cdots\ge\text{Cost of }T_N.\tag{2.14}$$
The reason, as in the figure caption, is $H_k(\tilde x_k)\ge\tilde Q_k(\tilde x_k,\tilde u_k)$. If the inequality is strict, rollout switches from $T_k$ to $T_{k+1}$ (p. 187).

**Empirical and MPC remarks** (p. 188). The author reports that improvement from rollout with a sequentially improving heuristic is typically considerable and often dramatic, with case studies since the mid-1990s. The extra computation is typically the heuristic's time times a low-order polynomial factor in $N$. Results are consistent with the Newton-step interpretation of Chapter 1. According to [Ber19a], [Ber20a], sequential improvement holds in the context of MPC and is the underlying reason for MPC's stability properties, while the base heuristic of classical MPC is not sequentially consistent (p. 188).

**Example 2.3.3 (Sequential improvement violation)** (p. 188–189).
- *Setup.* A 2-stage problem (Fig. 2.3.5) has states $x_1^*,\tilde x_1$ at stage 1 and $x_2^*,\tilde x_2$ at stage 2. The unique optimal trajectory is $(x_0,u_0^*,x_1^*,u_1^*,x_2^*)$, and the base heuristic produces it from $x_0$ (p. 188).
- *Rollout rejects the optimal control.* If
$$g_0(x_0,u_0^*)+H_1(x_1^*)>g_0(x_0,\tilde u_0)+H_1(\tilde x_1),\tag{2.15}$$
rollout rejects $u_0^*$ in favor of $\tilde u_0$. This happens if the heuristic chooses $\bar u_1$ at $x_1^*$ (nothing prevents this, since the heuristic is arbitrary) and the cost $g_1(x_1^*,\bar u_1)+g_2(\tilde x_2)=H_1(x_1^*)$ is high enough (p. 188).
- *Why sequential improvement fails.* If (2.15) holds, then $H_0(x_0)<\min\{g_0(x_0,u_0^*)+H_1(x_1^*),\,g_0(x_0,\tilde u_0)+H_1(\tilde x_1)\}$. Indeed $H_0(x_0)=g_0(x_0,u_0^*)+g_1(x_1^*,u_1^*)+g_2(x_2^*)$ is the optimal cost. It must be smaller than both the cost of $(x_0,u_0^*,x_1^*,\bar u_1,\tilde x_2)$ and the cost of $(x_0,\tilde u_0,\tilde x_1,\tilde u_1,\tilde x_2)$ (p. 188–189).
- *Conclusion.* The rollout choice at $x_0$ is strictly suboptimal while the heuristic's is optimal (Fig. 2.3.5 caption) (p. 189).

This example and (2.14) suggest the fortified rollout, which detects violations of sequential improvement and corrects them by keeping the best trajectory found so far (p. 189).

### 2.3.2 The fortified rollout algorithm (starts at p. 189; the part ends here)
The variant implicitly enforces sequential improvement. At state $x_k$ it holds a permanent trajectory $\bar P_k=\{x_0,u_0,\dots,u_{k-1},x_k\}$ built by rollout. It also stores a tentative best trajectory $\bar T_k=\{x_0,u_0,\dots,u_{k-1},x_k,\bar u_k,\bar x_{k+1},\bar u_{k+1},\dots,\bar u_{N-1},\bar x_N\}$ (p. 189). The description continues beyond this part.

## Toy example (ours, not from the text)
A 2-stage problem with $g_2\equiv0$. From $x_0$: control $a$ costs 1 and leads to state $A$; control $b$ costs 2 and leads to state $B$. At stage 1, from $A$: control $p$ costs 4, control $q$ costs 1. From $B$: control $p$ costs 1, control $q$ costs 3.
- *Base heuristic:* "at $x_0$ use $a$; at stage 1 always use $p$". Then $H_1(A)=4$ and $H_1(B)=1$, so $H_0(x_0)=1+4=5$. It is sequentially consistent: from $A$ it again uses $p$, as in the trajectory it generated from $x_0$.
- *Rollout at $x_0$:* $\tilde Q_0(x_0,a)=1+H_1(A)=1+4=5$ and $\tilde Q_0(x_0,b)=2+H_1(B)=2+1=3$. The minimum is 3, attained by $b$, so $\tilde\mu_0(x_0)=b$ and $\tilde x_1=B$.
- *Rollout at $B$:* $\tilde Q_1(B,p)=1+0=1$ and $\tilde Q_1(B,q)=3+0=3$. Rollout picks $p$. Total cost $2+1=3$.
- *Consistency with the theory:* $J_{0,\tilde\pi}(x_0)=3\le H_0(x_0)=5$, as in (2.11). Also $\min\tilde Q_0=3\le5=H_0$, as in (2.13).
- *Optimal cost:* by backward DP, $J_1^*(A)=\min\{4,1\}=1$ and $J_1^*(B)=\min\{1,3\}=1$, so $J_0^*=\min\{1+1,\,2+1\}=2$, via $a$ then $q$. Rollout (3) lies between the heuristic (5) and the optimum (2): it improves on the heuristic but need not be optimal.

## Concepts
- [[approximation-in-value-space]] (new) — run the forward construction (2.6) with an approximate cost-to-go $\tilde J_{k+1}$ in place of $J^*_{k+1}$ (p. 173)
- [[bellman-equation-value-function]] — here the deterministic DP recursion (2.3)–(2.4), where $J_k^*$ is the optimal cost-to-go of the tail subproblem (p. 167–168)
- [[cost-to-go]] (new) — $J^*_k(x_k)$, the optimal cost of the $(N-k)$-stage tail subproblem starting at $x_k$ (p. 168)
- [[q-factor]] (new) — $\tilde Q_k(x_k,u_k)=g_k+\tilde J_{k+1}(f_k)$; its minimization gives the one-step lookahead control (p. 174)
- [[rollout]] (new) — approximation in value space where $\tilde J_{k+1}$ is the cost of a base heuristic run from the next state (p. 178)
- [[base-heuristic]] (new) — any method that, from a state, produces controls, states and a cost $H_k(x_k)$ to the end (p. 178)
- [[sequential-consistency]] (new) — the heuristic continues along its own trajectory; equivalent to the heuristic defining a DP policy (p. 183–184)
- [[sequential-improvement]] (new) — $\min_u\tilde Q_k(x_k,u)\le H_k(x_k)$ for all $x_k,k$; weaker than consistency, and still gives cost improvement (p. 186)
- [[policy]] — here a sequence of functions $\mu_k$ mapping states to controls; for deterministic problems control sequences do as well (p. 167)
- [[fortified-rollout]] (new) — rollout that keeps the best trajectory found so far to enforce improvement (p. 189)
- [[model-predictive-control]] — mentioned: the sequential improvement condition underlies MPC stability, but the classical MPC heuristic is not sequentially consistent (p. 188)
- [[multistep-lookahead]] (new) — $\ell$-step deterministic DP with terminal approximation $\tilde J_{k+\ell}$ (p. 177)

## Canonical instances
- [[four-queens-problem]] — a constraint (feasibility) problem as a shortest path with dead-end arcs of cost 1 (p. 169–171)
- [[multidimensional-assignment]] — value-space approximation reduced to 2-dimensional assignment via arc-cost sums (p. 174–177)
- [[multi-vehicle-routing-rollout]] — rollout improves a nearest-task heuristic from 10 to 6 moves (p. 179–181)
- [[breakthrough-problem]] — greedy versus rollout versus exact DP on a binary tree (p. 182–183)
- [[sequential-improvement-violation-example]] — rollout strictly worse than a heuristic that is optimal from $x_0$ (p. 188–189)

## Bridges (candidates)
- [structural-analogy] Rollout with a consistent base heuristic ↔ control-theory: one policy-improvement (Newton) step on the base policy — the author states this link to Chapter 1's Newton interpretation (p. 184, p. 188).
- [structural-analogy] Sequential improvement ↔ MPC: the condition behind MPC's stability properties (p. 188).
- [structural-analogy] Off-line training of $J_k^*$ plus on-line forward play ↔ chess/backgammon programs of Section 1.1 (p. 168).
- [metaphor] Fortified rollout's "keep the best trajectory so far" ↔ incumbent solution in search heuristics.

## Questions this raises
- How large is the improvement in practice, and can it be bounded? The author says it is hard to quantify (p. 188).
- How can the fortified rollout guarantee improvement without sequential improvement? (Continued in the next part.)
- When the exponential growth in the number of vehicle moves per stage is a problem (Example 2.3.1), how does multiagent rollout (Section 2.9) keep the guarantee?
- How do the deterministic ideas (general heuristics, multistep lookahead, trajectory constraints) change for stochastic problems, where the author says they do not extend (p. 165)?

## Reading notes
- This is part 1 of 7 of Chapter 2. It starts at the chapter opening (printed p. 163, with the chapter table of contents on pp. 163–164) and ends at printed p. 189, in the middle of Section 2.3.2 (the fortified rollout), right after the definition of the tentative best trajectory $\bar T_k$. The section is not completed here.
- Page-number offset: printed = pdf − 20.
- The text layer shows "→" for the minus sign in "$N-1$" and similar places.
- No exercises appear in these pages.
- A possible inconsistency in Example 2.3.1 (my observation, p. 181): for the move to (3,5), the "6 vehicle moves" counts only the heuristic's three joint steps after that move. For (3,4), the "6 vehicle moves" appears to include the first joint move. Counting the first joint move for both, (3,5) would total 8. This recount does not contradict the author's stated conclusion that rollout picks (3,4) with a total of 6, though the page does not show the heuristic costs from (4,5) and (4,4).
- The statement about the rollout versus greedy probability (p. 183) is quoted from the book's summary of an analysis in [Ber17a]. This unit does not reproduce the analysis.
