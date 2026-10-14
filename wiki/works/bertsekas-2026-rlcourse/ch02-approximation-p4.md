---
id: bertsekas-2026-rlcourse/ch02-approximation-p4
work: bertsekas-2026-rlcourse
unit: "Chapter 2, part 4/7: end of 2.5 Constrained Forms of Rollout; 2.6 Small Stage Costs and Long Horizon – Continuous-Time Rollout; 2.7 Approximation in Value Space – Stochastic Problems (to the start of 2.7.4)"
pages: 243-268
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Rollout with constraints, small stage costs, continuous time and randomness

## L0 — One line
Rollout (one-step lookahead that scores each control by the cost of a base heuristic or policy) can be extended to constraints, tiny stage costs, continuous time and stochastic problems, keeping the "no worse than the base" guarantee under stated conditions.

## L1 — The gist (≤ 120 words)
How can rollout (one-step lookahead that uses a base heuristic's cost) handle constraints, tiny stage costs, continuous time and randomness? With constraints, rollout stays feasible and no worse than the heuristic if the heuristic is sequentially improving (defined earlier); a fortified version needs only a feasible initial heuristic trajectory. With tiny stage costs, consider approximating cost differences; in continuous time, the lookahead uses the gradient of the base cost. For stochastic problems, rollout with an exactly evaluated base policy is no worse than that policy. Certainty equivalence (replacing random disturbances by nominal values) thins the lookahead tree; simulation estimates Q-factors (expected costs under the base policy); common random numbers cut the variance of their differences.

**Prerequisites:** finite-horizon dynamic programming (DP) and cost-to-go; the basic rollout idea and sequential improvement from earlier in the chapter; expectation; ordinary differential equations and gradients.

## L2 — Key ideas
- **Fortified constrained rollout** keeps a feasible "tentative best" complete trajectory. The result is always feasible and no worse than the base heuristic, even without sequential improvement, if the base heuristic is feasible from the start (pp. 243–244).
- **Tree-based rollout** keeps several partial trajectories. It can revisit abandoned ones, but it is off-line only (p. 245).
- **Discrete optimization examples.** In facility location, rollout fixes 0-1 variables one at a time and solves transportation problems. In constrained spanning trees, it swaps one arc per stage and can be iterated, which the author views as a form of policy iteration (repeated policy improvement, discussed earlier in the book) (pp. 245–249).
- **Small stage costs.** Approximation errors in $\tilde J_{k+1}$ can swamp a small $g_k$. In the continuous-time limit the lookahead becomes a gradient term $\nabla_x \tilde J_t' h$, which suggests approximating cost differences (pp. 250–256).
- **Continuous-time rollout** uses $\nabla_x J_{\pi,t}$. If the continuous-time sequential improvement condition (2.63) holds, the rollout cost is no worse than the base heuristic cost. The condition holds when $H_t=J_{\pi,t}$, via the Hamilton–Jacobi–Bellman equation (a partial differential equation, the continuous-time analog of the DP equation for one policy; under the requisite mathematical conditions) (pp. 252–256).
- **Stochastic rollout** is no worse than the base policy, shown by induction on $k$ (2.68–2.69). It can even be optimal with a poor base policy, as in optimal stopping (pp. 258–261).
- **Certainty equivalence (CE)** applied only after the first lookahead stage shrinks the lookahead tree. The author says it keeps the Newton-step character (the view of the lookahead policy's cost as the result of a Newton-method step, explained earlier in the book) (pp. 262–263).
- **Simulation and variance reduction.** Q-factors are estimated by Monte Carlo (backgammon is the showcase). Using the same disturbances for both controls reduces the variance of Q-factor differences (pp. 265–268).

## L3 — Walkthrough

### 2.5 Constrained forms of rollout (continued)

**Sequential improvement, remarks.** The definition and Prop. 2.5.1 come earlier. For the traveling-salesman Example 2.5.1, the base heuristic of Fig. 2.5.3 is sequentially improving. If the travel cost D→A were 25, the definition would be violated at A. Constrained rollout would then give a tour more costly than the base heuristic's tour from A (p. 243).

**Fortified constrained rollout.** Without sequential improvement, the set $U_k(\tilde y_k)$ of controls leading to feasible trajectories $T_k(\tilde y_k,u_k)$ may be empty, in which case the rollout algorithm cannot extend the partial trajectory (p. 243). The fix needs one requirement: the base heuristic produces a feasible complete trajectory $R(\tilde y_0)$ from the initial state (p. 243).

The algorithm keeps the current partial trajectory $\tilde y_k=(\tilde x_0,\tilde u_0,\dots,\tilde u_{k-1},\tilde x_k)$. It also keeps a feasible complete **tentative best trajectory** $\hat T_k\in C$ ($C$ = feasible set) that agrees with $\tilde y_k$ up to $\tilde x_k$:
$$\hat T_k=(\tilde x_0,\tilde u_0,\dots,\tilde u_{k-1},\tilde x_k,\overline u_k,\overline x_{k+1},\dots,\overline u_{N-1},\overline x_N)\tag{2.49}$$
with $\overline x_{k+1}=f_k(\tilde x_k,\overline u_k)$ and $\overline x_{t+1}=f_t(\overline x_t,\overline u_t)$ for $t=k+1,\dots,N-1$. Initially $\hat T_0=R(\tilde y_0)$ (p. 243). At stage $k$ it forms
$$\hat U_k(\tilde y_k)=\{u_k\in U_k(\tilde y_k)\mid G(T_k(\tilde y_k,u_k))\le G(\hat T_k)\}.$$
(p. 243). Two cases:
1. $\hat U_k$ nonempty: pick $\tilde u_k\in\arg\min_{u_k\in\hat U_k}G(T_k(\tilde y_k,u_k))$, set $\tilde x_{k+1}=f_k(\tilde x_k,\tilde u_k)$ and $\hat T_{k+1}=T_k(\tilde y_k,\tilde u_k)$ (p. 244).
2. $\hat U_k$ empty: follow the tentative best trajectory, $\tilde u_k=\overline u_k$, $\tilde x_{k+1}=\overline x_{k+1}$, and keep $\hat T_{k+1}=\hat T_k$ (p. 244).

The algorithm follows $\hat T_0$ until it finds a feasible complete trajectory of smaller cost, which replaces it. Later replacements are possible (p. 244). If the base heuristic is sequentially improving, case (1) holds by Prop. 2.5.1 (the controls $\tilde u_k$ of the non-fortified algorithm then lie in $\hat U_k$). The fortified algorithm then gives the same trajectory as the non-fortified one, with $\hat T_{k+1}=T_k(\tilde y_k,\tilde u_k)$ (p. 244). Without sequential improvement the result is still feasible and costs no more than the base heuristic from $\tilde y_0$. Each tentative best trajectory costs no more than its predecessor, and $\hat T_0$ is the base heuristic's trajectory (p. 244).

*Intuition note.* The fortified version keeps a safe, already-feasible full plan in the drawer. It switches to a new plan only when that plan is feasible and not more costly, so it can never end up worse than the base heuristic.

**Tree-based constrained rollout.** Instead of one partial trajectory, keep a tree of partial trajectories rooted at $\tilde y_0$, possibly of different lengths. At each step select one, and extend it as in ordinary constrained rollout. A fortified version keeps the minimum-cost complete trajectory found so far (p. 245). The gain is the ability to return to partial trajectories abandoned earlier. The author notes freedom in choosing how many to keep. The drawback is that it suits off-line computation, not on-line use, where the control is chosen after the state is revealed in real time (p. 245).

### 2.5.1 Constrained rollout for discrete optimization and integer programming

**Example 2.5.2 (Facility location).** There are $N$ candidate locations $k=0,\dots,N-1$ and $M$ clients. Client $i$ has demand $d_i$, served at location $k$ at cost $a_{ik}$ per unit. A facility at $k$ costs $b_k$ and can serve up to $c_k$. The variable $u_k\in\{0,1\}$ says whether a facility is placed at $k$; $y_{ik}$ is the demand of client $i$ served at $k$ (p. 245). Constraints:
$$\sum_{k=0}^{N-1}y_{ik}=d_i\ (i=1,\dots,M)\tag{2.50}$$
$$\sum_{i=1}^{M}y_{ik}\le c_ku_k\ (k=0,\dots,N-1)\tag{2.51}$$
$$y_{ik}\ge0,\quad u_k\in\{0,1\}\tag{2.52}$$
Minimize
$$\sum_{i=1}^M\sum_{k=0}^{N-1}a_{ik}y_{ik}+\sum_{k=0}^{N-1}b_ku_k\tag{2.53}$$
(p. 246). This can be a very difficult mixed integer programming problem. But once all $u_k$ are fixed, it is a *linear transportation problem*, solvable by fast polynomial algorithms. So the difficulty lies in choosing $u_0,\dots,u_{N-1}$, a discrete optimization problem of the Section 1.6.3 type (p. 246).

*Base heuristic* at "state" $(u_0,\dots,u_k)$: place a facility at all remaining locations ($u_j=1$ for $j>k$), and compute its cost by solving the transportation problem with the earlier $u_j$ fixed (p. 246).

*Rollout:* try $u_0=1$ and $u_0=0$, solve the two transportation problems, and fix $u_0$ by the smaller cost. Repeat for $u_1$, and so on (p. 247).

Results (p. 247):
- If placing a facility everywhere is feasible, i.e. $\sum_i d_i\le\sum_k c_k$, rollout gives a feasible solution costing no more than the base heuristic.
- The author states the base heuristic is sequentially consistent, so fortification is not needed.
- Counting transportation problems gives $2N$, reducible to $N+1$, because one of the two problems at each later stage was already solved earlier.
- The graph of Fig. 2.1.4 is the branch-and-bound tree, so rollout is a quick, imperfect traversal of it.
- The many similar transportation problems favour a warm-started method such as the auction algorithm (Bertsekas–Castañon [BeC89]).

**Example 2.5.3 (Constrained shortest paths, directed spanning trees).** The graph has nodes $0,\dots,N$, with root $N$ (no outgoing arc). Each node $k<N$ chooses one outgoing arc $u_k\in U_k$. The collection $u=(u_0,\dots,u_{N-1})$ must form no cycle, so it is a directed spanning tree rooted at $N$. We minimize $G(u)$ subject to $u\in U$, where $U$ includes the tree requirement and other unspecified constraints (p. 248). The classical shortest-path problem is a special case. There $G(u)$ is the sum of the path lengths from all nodes to $N$. A constraint such as a bound on the number of arcs per path is also allowed (p. 248).

Start from a feasible tree $\bar u$ (finding it may be hard). The base heuristic, given $y_k=(u_0,\dots,u_{k-1})$, completes it as $(u_0,\dots,u_{k-1},\bar u_k,\dots,\bar u_{N-1})$ (pp. 248–249). Rollout, given $\tilde y_k$, considers all arcs $u_k$ out of node $k$ for which $(\tilde y_k,u_k,\bar u_{k+1},\dots,\bar u_{N-1})$ is feasible, and picks the one of least cost (Fig. 2.5.5) (p. 249). By induction from $\bar u$:
- $\hat U_k(\tilde y_k)$ is nonempty.
- Each solution is feasible and no worse than the previous one.
- Successive trees differ by at most one arc.

Rollout can be applied repeatedly, with the previous result as the new base heuristic and possibly a different node order. This is a form of policy iteration. It stops when no progress is possible, with no guarantee of optimality (p. 249).

### 2.6 Small stage costs and long horizon — continuous-time rollout

**The difficulty.** In the deterministic one-step scheme
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}\big[g_k(x_k,u_k)+\tilde J_{k+1}(f_k(x_k,u_k))\big]\tag{2.54}$$
the stage cost $g_k$ may be 0 or small relative to $\tilde J_{k+1}$. Then approximation errors in $\tilde J_{k+1}$ may overwhelm $g_k$, with unpredictable consequences for the policy (p. 250). The straightforward remedy is longer lookahead, as in MPC (model predictive control, Section 1.6.9). This costs on-line computation, so tree pruning and incremental rollout (Section 2.4.2) may help (p. 250).

**Continuous-time problem.** The dynamics are $\dot x(t)=h(x(t),u(t),t)$, $0\le t\le T$ (2.55), with $x(t)\in\Re^n$, $u(t)\in U\subset\Re^m$. The cost is
$$G(x(T))+\int_0^Tg(x(t),u(t),t)\,dt\tag{2.56}$$
(p. 250). Discretize with $\delta>0$, $T=\delta N$: $x_{k+1}=x_k+\delta\,h_k(x_k,u_k)$, with $x_k\approx x(k\delta)$, $u_k\approx u(k\delta)$. The cost becomes $g_N(x_N)+\sum_{k=0}^{N-1}\delta\,g_k(x_k,u_k)$, where $g_N(x_N)=G(x(N\delta))$ (pp. 250–251). Approximation in value space becomes
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U}\big[\delta g_k(x_k,u_k)+\tilde J_{k+1}(x_k+\delta h_k(x_k,u_k))\big]\tag{2.57}$$
(p. 251). The ratio of $\delta g_k$ to $\tilde J_{k+1}(\cdot)$ is likely to tend to 0 as $\delta\to0$, since $\tilde J_{k+1}(\cdot)$ ordinarily stays roughly constant at a nonzero level. So the lookahead may be degraded substantially. The author notes similar sensitivity in other discrete-time models with frequent decisions and tiny stage costs (p. 251).

*Fix.* Subtract the constant $\tilde J_k(x_k)$, which does not depend on $u_k$ and so leaves the minimizer unchanged:
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U}\Big[\delta g_k(x_k,u_k)+\big(\tilde J_{k+1}(x_k+\delta h_k(x_k,u_k))-\tilde J_k(x_k)\big)\Big]\tag{2.58}$$
If $\tilde J_k$ is differentiable, $\tilde J_{k+1}(x_k+\delta h_k)-\tilde J_k(x_k)\approx\delta\,\nabla_x\tilde J_k(x_k)'h_k(x_k,u_k)$. Dividing by $\delta$ and letting $\delta\to0$ informally gives
$$\tilde\mu(t)\in\arg\min_{u(t)\in U}\big[g(x(t),u(t),t)+\nabla_x\tilde J_t(x(t))'h(x(t),u(t),t)\big]\tag{2.59}$$
This is "the correct analog" of (2.54) for continuous time (p. 251).

*Intuition note.* The values $\tilde J$ at neighbouring states are nearly equal, and only their small difference matters for choosing $u$. Subtracting the common level leaves the part that is comparable in size to $\delta g_k$.

**Rollout in continuous time.** For a base policy $\pi=\{\mu_t(x(t))\mid0\le t\le T\}$ (2.60), the author speculates that the analog of rollout is
$$\tilde\mu_t(x(t))\in\arg\min_{u(t)\in U}\big[g(x(t),u(t),t)+\nabla_xJ_{\pi,t}(x(t))'h(x(t),u(t),t)\big]\tag{2.61}$$
with $J_{\pi,T}(x(T))=G(x(T))$ (p. 252). The inner product can be approximated by a finite difference, which needs two runs of the base policy:
$$\nabla_xJ_{\pi,t}(x(t))'h(x(t),u(t),t)\approx\frac{J_{\pi,t}\big(x(t)+\delta h(x(t),u(t),t)\big)-J_{\pi,t}(x(t))}{\delta}$$
(p. 252). An often sensible and convenient base policy is "short-sighted": it takes into account the short-term cost over a very small horizon and ignores the remaining cost. The extreme is the *myopic* policy $\mu_t(x(t))\in\arg\min_{u\in U}g(x(t),u(t),t)$, the analog of the greedy policy (p. 252).

**Example 2.6.1 (Minimum-length curve from a point to a line).** Start at $(0,0)$ and end on the vertical line through $(T,0)$. A small piece of the curve has length $\sqrt{(dt)^2+(\dot x\,dt)^2}=\sqrt{1+\dot x(t)^2}\,dt$. So we minimize $\int_0^T\sqrt{1+\dot x(t)^2}\,dt$ with $x(0)=0$ (p. 253). As a control problem: $\dot x=u$, $x(0)=0$, minimize $\int_0^T\sqrt{1+u(t)^2}\,dt$. Thus $h=u$, $g=\sqrt{1+u^2}$, $G=0$ (pp. 253–254).

Take a base policy that depends only on $t$: $\mu_t(x(t))=\beta(t)$. For constant $\beta(t)\equiv\bar\beta$ it is a straight line at angle $\phi$ with $\tan\phi=\bar\beta$. Its cost is
$$J_{\pi,t}(x(t))=\int_t^T\sqrt{1+\beta(\tau)^2}\,d\tau,$$
independent of $x(t)$, so $\nabla_xJ_{\pi,t}\equiv0$. Then (2.61) reduces to $\arg\min_{u\in\Re}\sqrt{1+u^2}$, so the rollout policy is $\tilde\mu_t\equiv0$. This is the optimal policy, the horizontal line from $(0,0)$ to $(T,0)$, although the base policy may be poor (p. 254).

**General base heuristics and sequential improvement.** Replace $J_{\pi,t}$ by a differentiable function $H_t$ obtainable from a base heuristic, which may lack the sequential consistency that policies have (p. 254):
$$\tilde\mu(t)\in\arg\min_{u(t)\in U}\big[g(x(t),u(t),t)+\nabla_xH_t(x(t))'h(x(t),u(t),t)\big].$$
Assume
$$H_T(\tilde x(T))=G(\tilde x(T))\tag{2.62}$$
$$\min_{u(t)\in U}\big[g(x(t),u(t),t)+\nabla_tH_t(x(t))+\nabla_xH_t(x(t))'h(x(t),u(t),t)\big]\le0\ \text{ for all }(x(t),t)\tag{2.63}$$
(2.63) is the continuous-time analog of sequential improvement (2.13). The claim is
$$J_{\tilde\pi,0}(x(0))\le H_0(x(0))\tag{2.64}$$
(pp. 254–255). *Proof.* Let $\tilde x(t),\tilde u(t)$ be the rollout trajectories. By (2.63), $g(\tilde x,\tilde u,t)+\nabla_tH_t(\tilde x)+\nabla_xH_t(\tilde x)'h(\tilde x,\tilde u,t)\le0$ for all $t$. Integrating over $[0,T]$:
$$\int_0^Tg\,dt+\int_0^T\big(\nabla_tH_t(\tilde x(t))+\nabla_xH_t(\tilde x(t))'h(\tilde x(t),\tilde u(t),t)\big)dt\le0\tag{2.65}$$
Since $h=d\tilde x/dt$, the second integrand is the total time derivative $\frac{d}{dt}H_t(\tilde x(t))$. Hence
$$\int_0^Tg(\tilde x(t),\tilde u(t),t)\,dt+\int_0^T\frac{d}{dt}H_t(\tilde x(t))\,dt=\int_0^Tg\,dt+H_T(\tilde x(T))-H_0(\tilde x(0))\le0\tag{2.66}$$
Using (2.62) and $\tilde x(0)=x(0)$:
$$J_{\tilde\pi,0}(x(0))=\int_0^Tg\,dt+G(\tilde x(T))\le H_0(x(0)).\ \blacksquare$$
(p. 255).

*Intuition note.* Condition (2.63) says that following the rollout control, the heuristic's "remaining cost" falls at least as fast as the running cost accrues. Summing along the path then gives total cost at most the heuristic's starting cost.

**Link to HJB.** For any policy $\pi$, the analog of the DP algorithm (under the requisite mathematical conditions) is
$$0=g(x(t),\mu_t(x(t)),t)+\nabla_tJ_{\pi,t}(x(t))+\nabla_xJ_{\pi,t}(x(t))'h(x(t),\mu_t(x(t)),t)\tag{2.67}$$
This is the Hamilton–Jacobi–Bellman equation, a partial differential equation. So when $H_t=J_{\pi,t}$, (2.63) and (2.64) hold. The author invites the reader to verify that the base-policy cost in Example 2.6.1 satisfies (2.67) (p. 256).

**Approximating cost differences.** For a discrete-time long-horizon problem with small stage costs, the author suggests considering approximating
$$D_k^*(x_k,u_k)=J^*_{k+1}(f_k(x_k,u_k))-J_k^*(x_k)$$
and using $\tilde\mu_k(x_k)\in\arg\min_{u_k}[g_k(x_k,u_k)+\tilde D_k(x_k,u_k)]$. For continuous time the gradient idea is essential. For discrete time it is optional and problem-dependent, possibly together with longer lookahead. Methods mentioned: advantage updating, cost shaping, biased aggregation, baselines, and differential training (author's [Ber97b]) (p. 256).

**Zero cost per stage.** The extreme case has zero stage cost and only a terminal cost (or only constraints to satisfy). Examples: chess, backgammon, Rubik's cube, constraint programming. Cost-difference approximation may not help here. Advised remedies are long lookahead (multistep, pruning, incremental rollout) or truncated rollout. A terminal cost approximation from problem simplification or neural network training may also matter. In chess, Go and backgammon, neural-network terminal cost approximation has been critical (p. 257).

### 2.7 Approximation in value space — stochastic problems

Base heuristic: a policy $\pi=\{\mu_0,\dots,\mu_{N-1}\}$; finite state, control and disturbance spaces (p. 257). The rollout control is
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}E\{g_k(x_k,u_k,w_k)+J_{k+1,\pi}(f_k(x_k,u_k,w_k))\}=\arg\min_{u_k}Q_{k,\pi}(x_k,u_k),$$
where $Q_{k,\pi}$ is the **Q-factor** (expected cost of using $u_k$ now, then following $\pi$) (p. 257).

**Cost improvement.** Claim:
$$J_{k,\tilde\pi}(x_k)\le J_{k,\pi}(x_k)\ \text{ for all }x_k,k\tag{2.68}$$
*Proof* by induction. At $k=N$: $J_{N,\tilde\pi}=J_{N,\pi}=g_N$. Assume the claim for $k+1$. Then (p. 258)
$$\begin{aligned}J_{k,\tilde\pi}(x_k)&=E\{g_k(x_k,\tilde\mu_k(x_k),w_k)+J_{k+1,\tilde\pi}(f_k(x_k,\tilde\mu_k(x_k),w_k))\}\\&\le E\{g_k(x_k,\tilde\mu_k(x_k),w_k)+J_{k+1,\pi}(f_k(x_k,\tilde\mu_k(x_k),w_k))\}\\&=\min_{u_k\in U_k(x_k)}E\{g_k(x_k,u_k,w_k)+J_{k+1,\pi}(f_k(x_k,u_k,w_k))\}\\&\le E\{g_k(x_k,\mu_k(x_k),w_k)+J_{k+1,\pi}(f_k(x_k,\mu_k(x_k),w_k))\}=J_{k,\pi}(x_k)\end{aligned}\tag{2.69}$$
The steps are: DP equation for $\tilde\pi$; induction hypothesis; definition of rollout; DP equation for $\pi$ (p. 258).

This assumes $J_{k+1,\pi}$ is exact. With truncated rollout, terminal cost approximation and limited simulation, the rollout cost is still viewed as a Newton step. The improvement can still be proved under conditions not discussed here (p. 258). Empirically, rollout typically gives substantial improvement (pp. 258–259).

*Intuition note.* The rollout control is the best first move *given* that the base policy plays afterwards, so it is at least as good as the base policy's own first move. The induction says the same holds at every later stage. The book calls this a Newton step (explained earlier in the book, not on these pages).

**Example 2.7.1 (Optimal stopping and rollout optimality).** At each stage, stop or continue; stopping is mandatory at stage $N$. The problem is stationary. Stopping at $x_k$ costs $C(x_k)$, after which the system sits at a termination state at no cost. Continuing moves to $x_{k+1}=f(x_k,w_k)$ at cost $g(x_k,w_k)$. The terminal cost is $C(x_N)$ (p. 259). Example: option exercise with $C(x)=x$, $g\equiv0$. DP:
$$J_N^*(x_N)=C(x_N)\tag{2.70}$$
$$J_k^*(x_k)=\min\big[C(x_k),\,E\{g(x_k,w_k)+J^*_{k+1}(f(x_k,w_k))\}\big]\tag{2.71}$$
Stopping is optimal at time $k$ on $S_k=\{x\mid C(x)\le E\{g(x,w)+J^*_{k+1}(f(x,w))\}\}$ (p. 259).

Base policy $\pi$: stop at every state, so $J_{k,\pi}(x_k)=C(x_k)$. The rollout policy stops at $x_k$ iff $C(x_k)\le E\{g(x_k,w_k)+C(f(x_k,w_k))\}$, i.e. iff $x_k\in S_{N-1}$. In words, it stops where stopping beats continuing one more stage and then stopping (p. 259). From (2.70)–(2.71), $J^*_{N-1}\le J^*_N$, and inductively $J^*_k\le J^*_{k+1}$. Hence
$$S_0\subset\cdots\subset S_k\subset S_{k+1}\subset\cdots\subset S_{N-1}\tag{2.72}$$
(p. 260). Suppose $S_{N-1}$ is **absorbing**:
$$f(x,w)\in S_{N-1}\ \text{ for all }x\in S_{N-1},\ w\tag{2.73}$$
Then for $x\in S_{N-1}$, $J^*_{N-1}(x)=C(x)$, and by (2.73)
$$E\{g+J^*_{N-1}(f(x,w))\}=E\{g+C(f(x,w))\}\ge C(x).$$
So stopping is optimal at stage $N-2$ on $S_{N-1}$, i.e. $S_{N-1}\subset S_{N-2}$. With (2.72), $S_{N-2}=S_{N-1}$. Proceeding similarly, $S_k=S_{N-1}$ for all $k$. The optimal policy stops iff the state is in $S_{N-1}$, which is exactly where the rollout policy stops. So if (2.73) holds, the rollout policy is optimal (p. 260). Without (2.73), the rollout policy stops and is optimal on $\cap_kS_k$ and correctly continues outside $S_{N-1}$. Unlike the optimal policy, it also stops on states of $S_{N-1}$ not in $\cap_kS_k$ (p. 260).

**Example 2.7.2 (The rational burglar).** Each night $k$ the burglar retires with earnings $x_k$, or enters a house and gets an amount $w_k$ (i.i.d., mean $\bar w$). With probability $p$ he is caught and forfeits everything. The goal is to maximize expected earnings over $N$ nights (p. 261). DP: $J^*_N(x_N)=x_N$, and $J_k^*(x_k)=\max[x_k,(1-p)E\{J^*_{k+1}(x_k+w_k)\}]$. One-step stopping set:
$$S_{N-1}=\{x\mid x\ge(1-p)(x+\bar w)\}=\{x\mid x\ge(1-p)\bar w/p\}$$
(together with the "caught" state). It is absorbing in the sense of (2.73). So the rollout rule "retire when earnings reach or exceed $(1-p)\bar w/p$" is optimal. The base policy is the timid "always retire", far from optimal (p. 261).

### 2.7.1 Simplified rollout and policy iteration
The improvement property (2.68) also holds for simplified rollout:
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in\overline U_k(x_k)}Q_{k,\pi}(x_k,u_k)\tag{2.74}$$
for a subset $\overline U_k(x_k)\subset U_k(x_k)$ that contains $\mu_k(x_k)$. In the proof, the last inequality of (2.69) is replaced by $\min_{u_k\in\overline U_k(x_k)}Q_{k,\pi}(x_k,u_k)\le Q_{k,\pi}(x_k,\mu_k(x_k))$ (p. 261). Implementations include control discretization, random search, or one-agent-at-a-time minimization (p. 262).

In infinite-horizon policy iteration, instead of the full minimization
$$\tilde\mu(x)\in\arg\min_{u\in U(x)}E_w\{g(x,u,w)+\alpha J_\mu(f(x,u,w))\}\tag{2.75}$$
it suffices for cost improvement to find $\tilde\mu$ with, for all $x$,
$$E_w\{g(x,\tilde\mu(x),w)+\alpha J_\mu(f(x,\tilde\mu(x),w))\}\le E_w\{g(x,u,w)+\alpha J_\mu(f(x,u,w))\}.$$
As printed, the right side has a free $u$ with no further specification; the intended reading is presumably $u=\mu(x)$, but that is our reading, not stated on the page. This improvement property is the key argument for proving convergence of PI (p. 262).

### 2.7.2 Certainty equivalence approximations
$\ell$-step lookahead is expensive here, because the lookahead graph grows fast with the stochastic branching. **Certainty equivalence (CE)** replaces random quantities by nominal values. It shrinks the graph and reduces the variance of the Q-factors (p. 262).

*Pure CE* replaces all of $w_k,\dots,w_{N-1}$ by a nominal $\bar w$. This largely loses the Newton-step interpretation (p. 262). *Better* (the author says this largely corrects the difficulty while retaining substantial simplification): keep $w_k$ stochastic and replace only $w_{k+1},\dots,w_{N-1}$ by $\bar w$ (p. 262). This keeps the Newton-step character: $J_{\tilde\mu}$ is generated by a Newton step applied to the function produced by the last $\ell-1$ minimization steps (modified by CE and applied to the terminal cost approximation). The author says the performance penalty for CE "appears" typically small (p. 263).

The lookahead then has one stochastic step, and a much "thinner" graph. Fig. 2.7.1 (p. 264): an $\ell$-step tree without CE has the same height as an $\ell'$-step tree with CE, $\ell'=2\ell-1$. With $m$ controls per state and $n$ disturbances per state–control pair, the number of leaves is estimated as $O(mn^{\ell})$ without CE and $O(m(n+\ell))$ with CE. Tree pruning and iterative deepening from Section 2.4 also apply (p. 263).

**CE in rollout.** In (2.76), the base cost $J_\mu(f(x,u,w))$ is replaced by $\bar J_\mu(f(x,u,w))$, the cost of $\mu$ in a deterministic problem with $w$ replaced by a typical $\bar w$. For continuous $w$ use $\bar w=E\{w\}$. For discrete $w$ one option is the most probable value under $(x,\mu(x))$. Minimization at the first step stays exact, so the scheme still implements a Newton step and inherits the improvement properties (p. 263). For finite horizon, one can alternatively use the most likely future disturbance trajectory $(w_{k+1},\dots,w_{N-1})$ under the base policy (Section 2.3.7) (p. 263).

**Example 2.7.3 (Markov jump parameter problems).** The uncertainty is a perfectly observed parameter $\theta_k\in\{1,\dots,r\}$ following a Markov chain with $p^k_{ij}(x_k,u_k)=P(\theta_{k+1}=j\mid\theta_k=i,x_k,u_k)$. Use the augmented state $(x_k,\theta_k)$:
$$x_{k+1}=f_k(x_k,u_k,\theta_k),\quad\theta_{k+1}=w_k,$$
where $w_k=i$ with probability $p^k_{i\theta_k}(x_k,u_k)$ (p. 265, as printed). For CE rollout with base policy $\mu_k(x_k,\theta_k)$, compute future base controls assuming a deterministic parameter trajectory after $\theta_{k+1}$. One option is the most likely trajectory $(w_{k+1},\dots,w_{N-1})$ under the base policy, computed for each possible $(x_{k+1},\theta_{k+1})$ (p. 265).

### 2.7.3 Simulation-based implementation
For each $u_k\in U_k(x_k)$, simulate many trajectories $x_{i+1}=f_i(x_i,\mu_i(x_i),w_i)$, $i=k+1,\dots,N-1$, using the tail of the base policy. They start from $x_{k+1}=f_k(x_k,u_k,w_k)$, with disturbances obtained by random sampling. Their costs are samples of $Q_{k,\pi}(x_k,u_k)$ (p. 265). For long horizons, truncate and add a terminal cost approximation (pp. 265–266). Monte Carlo averaging gives $\tilde Q_{k,\pi}$, and
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}\tilde Q_{k,\pi}(x_k,u_k)\tag{2.77}$$
(p. 266).

**Example 2.7.4 (Backgammon).** Tesauro and Galperin [TeG96] gave the first impressive rollout application. It attained a level of play better than all computer backgammon programs, and eventually better than the best humans. The base player was TD-Gammon, trained with approximate policy iteration. The rollouts were truncated, with a terminal cost from TD-Gammon's position evaluation. Dice make trajectories random, so many are averaged (Fig. 2.7.2) (pp. 266–267).

*Two-player issue.* The theory here is one-player. The game is treated as a control problem where one player passively uses the base policy and the other optimizes by rollout. "Improvement" then means a better average score *against a TD-Gammon opponent*. The theory does not guarantee that the rollout player does better against a non-TD-Gammon opponent. That is a plausible hypothesis, testable only empirically. Counterexamples were built for Go with adversarial optimization (Wang et al. [WGB22]; see Section 2.12) (p. 267). Rollout programs are the strongest but too slow for real-time play without parallel hardware, partly because of the high branching factor (footnote) (p. 267).

### 2.7.4 Variance reduction in rollout — comparing advantages
Controls are chosen by Q-factor differences $\tilde Q_{k,\pi}(x_k,u_k)-\tilde Q_{k,\pi}(x_k,\hat u_k)$. Errors in the individual Q-factors may be magnified by the differencing (p. 268). Instead, sample the difference
$$C_k(x_k,u_k,\mathbf w_k)-C_k(x_k,\hat u_k,\mathbf w_k)\tag{2.78}$$
with the *same* disturbance sequence $\mathbf w_k=(w_k,\dots,w_{N-1})$ for both controls, where
$$C_k(x_k,u_k,\mathbf w_k)=g_N(x_N)+g_k(x_k,u_k,w_k)+\sum_{i=k+1}^{N-1}g_i(x_i,\mu_i(x_i),w_i).$$
This needs each $w_i$'s distribution not to depend on $x_i,u_i$ (footnote) (p. 268).

*Why it works.* Let $s_1=q_1+w_1$, $s_2=q_2+w_2$ with zero-mean $w_1,w_2$. Then $s_1-s_2$ is unbiased for $q_1-q_2$. Its variance decreases as the correlation of $w_1,w_2$ increases, and is 0 when $w_1=w_2$. The author says it is maximized when they are uncorrelated (see Reading notes). Hence a common disturbance may be far more accurate than differencing samples that use different disturbances $\mathbf w_k$ and $\hat{\mathbf w}_k$ (p. 268). The author then begins to introduce the zero-mean sample errors $D_k(x_k,u_k,\mathbf w_k)=C_k(x_k,u_k,\mathbf w_k)-\tilde Q_{k,\pi}(x_k,u_k)$. The unit ends here (p. 268).

*Intuition note.* If two noisy estimates share the same noise, the noise cancels in their difference. Rollout needs only the difference, because it just ranks the controls.

## Toy example (ours, not from the text)
Minimization, $N=2$, stopping optional at stage 0 and 1, mandatory at stage 2. Stopping at $x$ costs $C(x)=x$; continuing costs $g=0$ and moves to $x+w$ with $w=-2$ or $w=+1$, each with probability $1/2$. Start at $x_0=4$. Base policy $\pi$: always stop, so $J_{k,\pi}(x)=x$.

- **Stage 1 rollout cost.** At any $x_1$: stop costs $x_1$. Continue costs $E\{C(x_1+w)\}=x_1+E\,w=x_1-0.5$. So rollout continues at stage 1, and $J_{1,\tilde\pi}(x_1)=x_1-0.5\le x_1=J_{1,\pi}(x_1)$.
- **Stage 0 Q-factors.** $Q_{0,\pi}(4,\text{stop})=4$. $Q_{0,\pi}(4,\text{continue})=\tfrac12(2)+\tfrac12(5)=3.5$. Rollout continues.
- **Check (2.69).** $J_{0,\tilde\pi}(4)=E\{J_{1,\tilde\pi}(x_1)\}=E\{x_1-0.5\}=3.5-0.5=3$. The chain is $3\le3.5=\min Q\le4=J_{0,\pi}(4)$.
- **Optimality.** DP gives $J_1^*(x)=\min(x,x-0.5)=x-0.5$ and $J_0^*(4)=\min(4,3.5-0.5)=3$, so rollout is optimal, as in Example 2.7.1. Indeed $S_1=\{x\mid x\le x-0.5\}$ is empty, hence absorbing (2.73).

## Concepts
- [[rollout]] (new) — one-step lookahead that scores controls by the cost of a base heuristic or policy; in this unit also constrained, continuous-time and stochastic (p. 243)
- [[sequential-improvement]] (new) — condition ensuring rollout is feasible and no worse than the base heuristic; continuous-time form (2.63) (pp. 243, 255)
- [[fortified-rollout]] (new) — rollout that keeps a tentative best feasible complete trajectory (p. 243)
- [[tree-based-rollout]] (new) — maintaining a tree of partial trajectories; off-line only (p. 245)
- [[q-factor]] (new) — expected stage cost plus base-policy cost-to-go for a state–control pair (p. 257)
- [[approximation-in-value-space]] (new) — choose controls by minimizing stage cost plus approximate cost-to-go (p. 250)
- [[cost-difference-approximation]] (new) — approximate $J^*_{k+1}(f_k)-J^*_k$ when stage costs are small (p. 256)
- [[hamilton-jacobi-bellman-equation]] — PDE (2.67) satisfied by a policy's cost; implies (2.63) when $H_t=J_{\pi,t}$ (p. 256)
- [[bellman-equation-value-function]] — DP equations (2.70)–(2.71) for the stopping problem (p. 259)
- [[model-predictive-control]] — mentioned as the setting where longer lookahead is typical (p. 250)
- [[policy]] — rule $\mu_k(x_k)$, used as base policy and rollout policy (p. 257)
- [[certainty-equivalence]] (new) — replacing random disturbances by nominal values, here only after the first lookahead stage (p. 262)
- [[optimal-stopping]] (new) — problems with a stop control; stopping sets $S_k$ and the absorbing condition (p. 259)
- [[common-random-numbers]] (new) — same disturbances for both controls to reduce variance of Q-factor differences (p. 268)

## Canonical instances
- [[facility-location]] — 0-1 decisions fixed by rollout with transportation problems (p. 245)
- [[constrained-spanning-tree-rollout]] — one-arc-at-a-time rollout; iteration as policy iteration (p. 247)
- [[min-length-curve-calculus-of-variations]] — poor base policy, optimal rollout in continuous time (p. 253)
- [[optimal-stopping-always-stop-base]] — rollout optimal under absorbing stopping set (p. 259)
- [[rational-burglar]] — retire at threshold $(1-p)\bar w/p$ (p. 261)
- [[markov-jump-parameter-problem]] — augmented state, CE with most likely parameter path (p. 264)
- [[backgammon-rollout-tesauro-galperin]] — Monte Carlo rollout on top of TD-Gammon (p. 266)
- [[traveling-salesman-constrained-rollout]] — sequential improvement and its violation when D→A costs 25 (p. 243)

## Bridges (candidates)
- [structural-analogy] Rollout improvement via the continuous-time inequality (2.63) ↔ control theory: Lyapunov-style decreasing functions — the heuristic's cost-to-go must not rise along the controlled path.
- [same-math] Equation (2.67) for a fixed policy ↔ Hamilton–Jacobi–Bellman for policy evaluation — it is the HJB equation with the policy's control inserted (the author's own statement).
- [structural-analogy] Fortified rollout's tentative best trajectory ↔ anytime/incumbent solutions in branch-and-bound — the author notes rollout traverses the branch-and-bound tree.
- [structural-analogy] Common-random-number differencing (2.78) ↔ paired comparison in statistics — shared noise cancels in the difference.
- [metaphor] CE only after the first stage ↔ certainty-equivalent control in LQG-style design — nominal future, honest present.

## Questions this raises
- When is the sequential improvement condition checkable in practice, and how often does the fortified version actually replace $\hat T_0$?
- In continuous time, how reliable is the finite-difference estimate of $\nabla_x J_{\pi,t}'h$ when $\delta$ is small and base-policy costs come from simulation?
- Under what conditions is the performance penalty of CE small, since the author only says it "appears" small?
- Can rollout improvement be guaranteed against opponents other than the base policy in two-player games?

## Reading notes
- **Part boundaries.** This part starts mid-Section 2.5 (p. 243), in the discussion of sequential improvement. It ends mid-Section 2.7.4 (p. 268), at the introduction of $D_k$. The definitions of sequential improvement, Prop. 2.5.1, Eqs. (2.43), (2.46) and the earlier sections are not in these pages.
- **Page offset:** printed = pdf − 20.
- **OCR.** The text layer renders minus signs as "→" and sometimes garbles symbols. All equations were checked against the page images.
- **Misprints and oddities seen:**
  - The running head on p. 249 reads "Sec. 2.6 Constrained Forms of Rollout Algorithms"; it should be 2.5.
  - p. 246: the base heuristic fixes "$u_j$, $j=k+1,\dots,N$" at 1, while the index range is $0,\dots,N-1$.
  - p. 265: the Markov-jump dynamics are stated for $k=1,\dots,N-1$.
  - Fig. 2.7.1 caption (p. 264): "with CE, the lookahead tree grows much faster" appears reversed relative to the rest of the caption. I reported the leaf counts as printed. In the leaf count without CE, I cannot tell at this size whether $\ell$ is an exponent or a factor; the text layer gives $O(mn\ell)$, and L3 writes $O(mn^{\ell})$ as my reading.
  - p. 268: the author says the variance of $s_1-s_2$ is "maximized when $w_1$ and $w_2$ are uncorrelated". Strictly, with a fixed variance of each $w_i$, negative correlation would give a larger variance. "Uncorrelated" is the case of independent samples.
- **Prop. 2.5.1 and the claim that the facility-location base heuristic is sequentially consistent.** Both are cited, not proved, in these pages.
