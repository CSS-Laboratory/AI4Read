---
id: bertsekas-2026-rlcourse/ch02-approximation-p7
work: bertsekas-2026-rlcourse
unit: "2 Approximation in Value Space - Rollout Algorithms (part 7/7): end of §2.12.2, §2.12.3–2.12.5, §2.13 Notes, Exercises 2.1–2.8"
pages: 322-348
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Minimax rollout, combined value/policy approximation, computer chess, and chapter notes

## L0 — One line
Rollout and one-step lookahead extend to minimax (adversarial) control by computing a maximization per Q-factor, and replacing the maximizer by a fixed nominal opponent policy gives a cheaper deterministic one-player problem that keeps the Newton-step picture.

## L1 — The gist (≤ 120 words)
This part finishes Chapter 2's treatment of minimax control, where an adversary picks disturbances. It asks how rollout and approximation in value space work against an opponent, and what changes. Under a sequential improvement condition, rollout keeps its cost-improvement guarantee, but each Q-factor needs a maximization. Exact policy iteration for minimax can fail to converge because the Bellman operator is neither convex nor concave. A simplification replaces the maximizer by a fixed nominal policy, giving a deterministic one-player problem, to which Newton-step theory applies. The author applies this to computer chess and to leader-follower games. The unit ends with chapter notes and eight exercises.

**Prerequisites:** finite-horizon dynamic programming (DP), Q-factors, rollout with a base policy/heuristic, sequential improvement, the Newton-step view of approximation in value space (Ch. 1), convex vs concave functions.

## L2 — Key ideas
- Minimax rollout may use a base *heuristic* (not a legitimate policy) that generates controls and disturbances; if it is sequentially improving, the rollout policy has cost $J_{k,\tilde\pi}\le H_k$ (p. 322).
- The main added cost of minimax rollout is that each Q-factor needs a maximization, not a simulation (p. 322). Example 2.12.1 (pursuit-evasion) shows how to get it by DP against a precomputed base policy (p. 323).
- Variants carry over: multistep lookahead (with alpha-beta pruning), trajectory-constrained rollout, fortified rollout, and multiagent rollout. Multiagent rollout makes the number of evaluations of $J_1^*$ grow linearly in $m$ (pp. 324–326).
- Minimax is harder than one-player DP: the Bellman operator is neither convex nor concave, so Newton's method and exact policy iteration can behave unreliably. No reliable theory exists for training both players' policies simultaneously (pp. 326–327).
- Replacing the inner maximization by an approximate maximizer policy $\nu(x,u)$ gives a deterministic one-player problem (2.117)–(2.118). It coincides with minimax lookahead if $\nu$ is optimal for the maximizer (pp. 327–328).
- Computer chess "meta algorithm": an engine as position evaluator plus a nominal-opponent engine. Computation is about twice (one step) or $\ell+1$ times ($\ell$ steps) one engine move, given enough parallelism. In the reported tests it improves the base engine, with diminishing gains for stronger engines (pp. 329–331).
- For leader-follower games with non-shared costs, no Bellman equation may exist. The author proposes converting to a leader-only problem with nominal follower policies (pp. 332–334).

## L3 — Walkthrough

**Start of this part.** The unit begins mid-section, with minimax rollout in §2.12.2 (p. 322).

### 2.12.2 (end) Minimax rollout with a general base heuristic (p. 322)
- For deterministic problems, the base heuristic need not be sequentially consistent. Sequential improvement is sufficient for cost improvement. A similar generalization is not easily built for stochastic problems, but it is possible for minimax control (p. 322).
- At state $x_k$, a heuristic generates feasible controls, disturbances and states $\{u_k,w_k,x_{k+1},\dots,u_{N-1},w_{N-1},x_N\}$ with cost
$$H_k(x_k)=g_k(x_k,u_k,w_k)+\cdots+g_{N-1}(x_{N-1},u_{N-1},w_{N-1})+g_N(x_N).$$
- Rollout applies
$$\tilde u_k\in\arg\min_{u_k\in U_k(x_k)}\ \max_{w_k\in W_k(x_k,u_k)}\Big[g_k(x_k,u_k,w_k)+H_{k+1}\big(f_k(x_k,u_k,w_k)\big)\Big].$$
- The disturbances $w_k,\dots,w_{N-1}$ may be chosen by an antagonistic opponent, but the heuristic may also choose them by some approximate maximization. Example: with $w_k=(w_k^1,\dots,w_k^m)$ for multiple opponent agents, an agent-by-agent maximization (p. 322).
- **Sequential improvement condition:** for all $x_k$ and $k$,
$$\min_{u_k}\max_{w_k}\Big[g_k+H_{k+1}\big(f_k(x_k,u_k,w_k)\big)\Big]\le H_k(x_k).$$
- It guarantees cost improvement: the rollout policy $\tilde\pi=\{\tilde\mu_0,\dots,\tilde\mu_{N-1}\}$ satisfies $J_{k,\tilde\pi}(x_k)\le H_k(x_k)$ for all $x_k,k$ (p. 322). The page states this guarantee without proof.
- Difference from deterministic/stochastic rollout: computing a Q-factor needs a maximization, not a deterministic or Monte Carlo simulation of the base policy (p. 322).

*Intuition note.* Rollout against an adversary is the same recipe as before: "act greedily, then trust the base heuristic's cost-to-go". The main change is that the one-step value is the worst case over the opponent's reply.

### Example 2.12.1 — Pursuit-evasion (p. 323)
- State $x_k=(x_k^1,x_k^2)$: pursuer (minimizer) and evader (maximizer) locations in a finite graph. A cost-free absorbing termination set includes all pairs with $x^1=x^2$.
- The pursuer picks $u_k\in U_k(x_k)$. The evader then picks $x_{k+1}$ from a known set $X_{k+1}(x_k,u_k)$. The pursuer minimizes a nonnegative terminal cost $g(x_N^1,x_N^2)$, or reaches termination (cost 0).
- **Base policy** (precomputed by DP): from $x_k$, move along the path from $x_k^1$ that minimizes terminal cost after $N-k$ stages, assuming the evader stays motionless at $x_k^2$. A variation assumes the evader follows a nominal move sequence.
- **Online:** let $\tilde J_{k+1}(x_{k+1})$ be the maximal terminal cost the evader can achieve from $x_{k+1}$ if the pursuer follows the base policy. It is computable by an $(N-k)$-stage DP over the evader's choices. Then
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}\max_{x_{k+1}\in X_{k+1}(x_k,u_k)}\tilde J_{k+1}(x_{k+1}).$$
- With imperfect knowledge of $x_k^2$, the algorithm can be adapted by assumed certainty equivalence: use an estimate of $x_k^2$ for the base policy and the evader's maximization (p. 323).
- The base policy was easy here because of problem structure. In general, finding a suitable, conveniently implementable base policy is an important problem-dependent issue (p. 323).

### Variants of minimax rollout (pp. 323–325)
- Truncation with terminal cost approximation, multistep and selective lookahead, and multiagent rollout all have minimax analogs (pp. 323–324).
- **$\ell$-step lookahead:** solve
$$\min_{u_k,\mu_{k+1},\dots,\mu_{k+\ell-1}}\ \max_{\substack{w_k\in W_k(x_k,u_k)\\ w_t\in W_t(x_t,\mu_t(x_t)),\ t=k+1,\dots,N-1}}\Big\{g_k(x_k,u_k,w_k)+\sum_{t=k+1}^{k+\ell-1}g_t\big(x_t,\mu_t(x_t),w_t\big)+H_{k+\ell}(x_{k+\ell})\Big\},$$
then apply only the first component $\tilde u_k$ (p. 324).
- Some chess programs solve this kind of problem at each move, with the terminal cost encoded by a position evaluator. Alpha-beta pruning can accelerate multistep lookahead by eliminating unnecessary parts of the lookahead graph (p. 324).
- **Constrained rollout** (unlike stochastic control, an online constrained form exists for minimax): add the constraint $(x_0,u_0,\dots,u_{N-1},x_N)\in C$, with $C$ an arbitrary set. At the partial trajectory $\tilde y_k=(\tilde x_0,\tilde u_0,\dots,\tilde u_{k-1},\tilde x_k)$, compute for each $u_k\in\tilde U_k(\tilde y_k)$ (the controls that guarantee feasibility)
$$\tilde Q_k(\tilde x_k,u_k)=\max_{w_k,\dots,w_{N-1}}\Big[g_k(\tilde x_k,u_k,w_k)+H_{k+1}\big(f_k(\tilde x_k,u_k,w_k),w_{k+1},\dots,w_{N-1}\big)\Big],$$
and choose $\tilde u_k\in\arg\min_{u_k\in\tilde U_k(\tilde y_k)}\tilde Q_k(\tilde x_k,u_k)$. Feasibility of $(\tilde y_k,u_k)$ is checked by an algorithm that tests whether the future disturbances can be chosen to violate the constraint under the base policy (p. 324).
- **Fortified** versions (unconstrained and constrained) guarantee a feasible, cost-improved rollout policy. This requires that the base heuristic at the initial state produce a trajectory feasible for all possible disturbance sequences (p. 325).

### Example 2.12.2 — Multiagent minimax rollout (pp. 325–326)
- Minimizer's choice $u=(u^1,\dots,u^m)\in U=U^1\times\cdots\times U^m$ (finite, exponentially large in $m$). Maximizer's $w\in W$ (finite). Two-stage problem: $x_1=f_0(x_0,u)$ with cost $g_0(x_0,u)$. Then $x_2=f_1(x_1,w)$ with cost $g_1(x_1,w)+g_2(x_2)$. Minimize $g_0(x_0,u)+\max_{w\in W}[g_1(x_1,w)+g_2(x_2)]$.
- Exact DP:
$$J_1^*(x_1)=\max_{w\in W}\Big[g_1(x_1,w)+g_2\big(f_1(x_1,w)\big)\Big],\qquad J_0^*(x_0)=\min_{u\in U}\Big[g_0(x_0,u)+J_1^*\big(f_0(x_0,u)\big)\Big].$$
- This is intractable for large $m$: $J_1^*\big(f_0(x_0,u)\big)$ must be computed for each of exponentially many $u$.
- **Multiagent rollout** with base policy $\mu=(\mu^1,\dots,\mu^m)$ proceeds one agent at a time. Agent 1 chooses
$\tilde u^1\in\arg\min_{u^1\in U^1}\big[g_0(x_0,u^1,\mu^2(x_0),\dots,\mu^m(x_0))+J_1^*\big(f_0(x_0,u^1,\mu^2(x_0),\dots,\mu^m(x_0))\big)\big]$.
Agent 2 then chooses $\tilde u^2$ with $\tilde u^1$ fixed and $\mu^3,\dots,\mu^m$ for the rest, and so on up to $\tilde u^m$, which uses $\tilde u^1,\dots,\tilde u^{m-1}$.
- The number of evaluations of $J_1^*\big(f_0(x_0,u)\big)$ grows linearly with $m$. For more stages, $J_1^*$ is replaced by the optimal cost of a multistage maximization problem in which the minimizer is constrained to use the base policy (p. 326).

*Intuition note.* Choosing the minimizer's components one at a time, with the not-yet-chosen agents following their base rules, replaces a product search by a sum of small searches. The adversary's reply is still evaluated exactly, once per candidate.

### Approximating min-max and max-min: difficulties (pp. 326–327)
- We can improve the minimizer's policy assuming a *fixed* maximizer policy (basis for §2.12.3). It is unclear how to improve both players' policies simultaneously (p. 326).
- In symmetric games such as chess, a common policy is trained for both players. This is computationally expedient and has worked well in AlphaZero and TD-Gammon. But there is no reliable theory for simultaneous training, and unusual behavior may arise in exceptional cases. Footnote: reports in late 2022 say humans beat KataGo ("an AlphaGo look-alike") using adversarial techniques (p. 326).
- Even *exact* policy iteration (Pollatschek and Avi-Itzhak, 1969) has serious convergence difficulties. Policy iteration is equivalent to Newton's method on the minimax Bellman equation, which behaves in a more complex and unreliable way than in the one-player case (pp. 326–327).
- Reason: the infinite-horizon Bellman operator
$$(TJ)(x)=\min_{u\in U(x)}\max_{w\in W(x,u)}\Big[g(x,u,w)+\alpha J\big(f(x,u,w)\big)\Big]$$
is neither convex nor concave in $J$. For fixed $(x,u)$, the inner max is convex in $J$, but when minimized over $u$ it becomes neither convex nor concave (p. 327). The author's modified policy iteration versions are in [Ber21b] and [Ber22b] (p. 327).

*Intuition note.* Concave components of the Bellman equation (the one-player case) have a beneficial effect on the convergence of Newton's method (footnote p. 328). In the minimax case the components may be neither concave nor convex, which complicates the convergence properties significantly.

### 2.12.3 Combined approximation in value and policy space (pp. 327–328)
- Standard minimax lookahead (infinite horizon):
$$\tilde u\in\arg\min_{u\in U(x)}\max_{w\in W(x,u)}\Big[g(x,u,w)+\alpha\tilde J\big(f(x,u,w)\big)\Big]\tag{2.116}$$
The maximization over $w$ must be done for each $u$, which complicates the minimization over $u$ (p. 327).
- **Alternative:** approximate the maximizer's optimal policy by $\nu(x,u)$ and use
$$\tilde u\in\arg\min_{u\in U(x)}\Big[g\big(x,u,\nu(x,u)\big)+\alpha\tilde J\Big(f\big(x,u,\nu(x,u)\big)\Big)\Big]\tag{2.117}$$
- $\nu$ may be obtained by off-line training, using samples from the maximization in (2.116) (p. 327).
- If $\nu$ is optimal for the maximizer, (2.117) coincides with (2.116) and inherits the Newton-step superlinear cost-improvement guarantees. Otherwise, cost improvement is not guaranteed, but can be expected under favorable conditions where $\nu$ is near-optimal (p. 328).
- (2.117) is a one-player approximation in value space for the problem with system equation
$$x_{k+1}=f\big(x_k,u_k,\nu(x_k,u_k)\big)\tag{2.118}$$
and cost per stage $g\big(x,u,\nu(x,u)\big)$.
- This problem is *deterministic*, so the deterministic techniques apply, including the rollout schemes of Sections 2.3–2.6, and the superlinear error bounds of Newton's method (cf. Section 1.5.3) apply (p. 328).

**Distributionally robust models** (p. 328). Here $w_k$ is a probability distribution, and $W_k(x_k,u_k)$ is a given set of distributions. Allowing $\nu(x,u)$ to take distribution values makes (2.117) applicable. But then system (2.118) is stochastic, so implementation is more complicated. The author gives the model's roots in early statistics (Blackwell–Girshick) (p. 328).

*Intuition note.* Fix a guess of how the adversary replies, and the game becomes a one-player problem. The guess is exactly right when $\nu$ is optimal for the maximizer, and otherwise there is no guarantee, though improvement can be expected when $\nu$ is near-optimal.

### 2.12.4 A meta algorithm for computer chess (pp. 329–332)
Based on Gundawar, Li and Bertsekas [GLB24] (p. 329). Chess engines supply a move policy (this plays the role of $\nu$ in (2.117)) and board evaluations (this plays the role of $\tilde J$) (p. 329).

- **(a) Position evaluator:** a chess engine such as Stockfish, which evaluates any position.
- **(b) Nominal opponent:** approximates the true opponent (engine or human); it outputs deterministically one move per position. If the opponent is unknown, a competent engine (e.g., the evaluator) is a reasonable choice. It is important not to use a relatively poor nominal opponent, which would lead us to underestimate the true opponent (p. 329).
- The two may be different engines, and the nominal opponent may change from game to game. Stored knowledge (opening book, endgame database) is indirectly incorporated (p. 329).
- **Notation:** $x_k$ = our chess position, $u_k$ = our move, $w_k$ = nominal opponent's move after $(x_k,u_k)$, and $x_{k+1}=f(x_k,u_k,w_k)$ with $f$ known (pp. 329–330).
- **One-step scheme** (Fig. 2.12.1, p. 330): (1) generate all legal moves $u_k$; (2) for each $(x_k,u_k)$ the nominal opponent produces one best move $w_k$, giving $x_{k+1}$; (3) evaluate each $x_{k+1}$. At most $m$ evaluations and $m$ opponent move generations, with $m$ an upper bound on the number of legal moves (p. 330).
- The scheme suits parallel computation. With sufficient parallel resources it needs roughly twice the computation of the underlying engines per move (p. 331).
- **Reported tests** ([GLB24]): like rollout, the scheme improves the evaluation engine it is based on, dramatically for relatively weak engines. This assumes a reasonable opponent choice. With Stockfish at various strength levels as both opponent and evaluator, the scheme beat the engine itself by a significant margin. The margin diminishes as engine strength increases, which is expected since Stockfish plays near-perfect chess at its highest levels. The author likens this to Newton-step/rollout improvement diminishing near $J^*$ (p. 331).
- **Multistep lookahead** (Fig. 2.12.2): for $\ell$ steps, per move $m+m^2+\cdots+m^\ell$ opponent move generations plus $m^\ell$ position evaluations. With sufficient parallelism, roughly $\ell+1$ times the computation of the underlying engines. Pruning the tree at the second stage can reduce the computation time (p. 331).
- **Multiple opponent moves:** replace the single nominal move by a few good moves, giving a reduced minimax tree. It is important not to prune any first-stage moves, to preserve the Newton step character. Pruned multistep search can still be costly, so pruning should be aggressive and lookahead short (pp. 331–332).

### 2.12.5 Noncooperative (nonzero-sum) sequential games (pp. 332–334)
- Noncooperative games: several agents choose distinct controls and optimize private costs. The author treats a simple class: sequential choices, with complete communication of controls to the other agents (p. 332).
- Unlike minimax problems, such problems may have no Bellman equation to support approximation in value space (p. 333).
- **Leader-follower (Stackelberg / bilevel) problem:** a leader and $m$ followers. Followers observe the leader's decision, then optimize their own private costs. Follower constraints are decoupled (p. 333).
- **Cooperative two-stage case.** The leader knows $x_0$, picks $u_0\in U_0$, and $x_1=f_0(x_0,u_0,w_0)$ with cost $g_0(x_0,u_0,w_0)$. The followers knowing $x_1$ choose $u_1^\ell\in U_1^\ell$, $\ell=1,\dots,m$. Then $x_2=f_1(x_1,u_1^1,\dots,u_1^m,w_1)$ with cost $g_{1,1}(x_1,u_1^1,w_1)+\cdots+g_{1,m}(x_1,u_1^m,w_1)+g_2(x_2)$. Minimize total expected cost over $u_0$ and follower policies $\mu_1^\ell$. This is a multiagent DP problem, solvable approximately by multiagent rollout (Section 2.9), with straightforward multistage extension (p. 333).
- If followers do **not** share the leader's cost, the multiagent formulation fails and approximation in value space seems very difficult. Approximation in policy space has been suggested, with mixed success so far (footnote, p. 333).
- **Proposed approach:** convert to a leader-only problem with nominal follower policies (from some policy training) that give follower actions depending predictably on $x_1$ and possibly the leader's $u_0$. Then the Newton step framework fully applies to the leader's problem, and online implementation is tractable. Limited preliminary results are encouraging, but more research is needed (p. 334).

### 2.13 Notes, sources (pp. 334–341)
- **Framing:** the chapter covered deterministic, stochastic and minimax problems; its emphasis is the effectiveness of approximation in value space via its Newton-step link. Finite-horizon problems can be converted to infinite-horizon ones with a termination state (§1.6.4), so the infinite-horizon insights apply (p. 334).
- **§2.2–2.3:** "rolling/receding horizon" is an often-used name for truncated $\ell$-step lookahead. Rollout appears earlier in game contexts, and the name was coined by Tesauro and Galperin for backgammon. The author adopts the original meaning: policy improvement from a base policy evaluated by Monte Carlo simulation, possibly with a terminal cost approximation (pp. 334–335).
- Sequential consistency/improvement, fortified and parallel rollout come from Bertsekas–Tsitsiklis–Wu [BTW97]. Stochastic rollout is from [Ber97b] and [BeC99]. Constrained rollout is from [Ber05a,b] (p. 335).
- A long chronological list of rollout studies reports favorable experience, with impressive cost improvement over the base policy, "evidently owing" to Newton's method. Other advantages: reliability, simplicity, online replanning, interfacing with neural-network training (pp. 335–336).
- Model-free rollout relates to Tesauro's comparison training. Most-likely-sequence generation (n-grams, HMMs, Markov chains) is from Li and Bertsekas [LiB24] (p. 336).
- **§2.4–2.5:** the incremental multistep rollout algorithms of §2.4.2 are presented here for the first time (p. 336). Constrained rollout and restricted-structure policies are discussed in [Ber05a] (p. 337).
- **§2.7:** certainty equivalence in rollout is from [BeC99]; the Newton-step view suggests that the minimization after the first step can be approximated with small degradation. Markov jump problems seem particularly well suited to these methods. Variance reduction is from [Ber97b] (p. 337).
- Adaptive sampling and early Monte Carlo tree search are from Chang–Hu–Fu–Marcus, inspired by multiarmed bandit work (UCB). MCTS now covers adaptive sampling, rollout and sequential games (p. 338).
- **Open-loop feedback controller (OLFC):** at information vector $I_k$ it solves the open-loop problem of minimizing $E\{g_N(x_N)+\sum_{i=k}^{N-1}g_i(x_i,u_i,w_i)\mid I_k\}$ subject to $x_{i+1}=f_i(x_i,u_i,w_i)$, $u_i\in U_i$, and applies the first control. The author says it is "easily seen" to be rollout with the optimal open-loop policy as base policy (pp. 338–339).
- The OLFC has a generalization, partial open-loop feedback control, which assumes some but not all future observations will be taken. A variant of the OLFC that also applies to minimax problems is in [Ber72b], with a proof of a cost improvement property over the optimal open-loop policy (p. 339).
- **§2.8–2.11:** these sections draw on [Ber20a] and [Ber22d]. For adaptive control with parameter estimation, one "may conjecture" an asymptotic cost-improvement property for the rollout policy under appropriate conditions (pp. 339–340).
- **§2.12:** minimax control assumes the maximizer chooses with perfect knowledge of the minimizer's policy. With roles reversed the minimizer gains an advantage and the optimal value may be reduced. So "min-max" and "max-min" are generally different problems. In classical zero-sum game theory the focus is on cases where they are equal; in engineering worst-case design they are typically unequal (p. 340).
- Pollatschek–Avi-Itzhak policy iteration is a Newton method that may not converge to the optimal cost, but converges much faster than competitors when it does. [Ber21b] explains the unreliability by the missing concavity, and gives a modified algorithm based on a uniform contraction mapping, convergent even under totally asynchronous implementation (pp. 340–341).
- Further notes: Yu [Yu14] analyzes stochastic shortest path games, including Q-learning for them, and [Ber19b] develops VI, PI and Dijkstra-like algorithms for robust shortest path planning, with related rollout algorithms (p. 341).
- Sections 2.12.3 and 2.12.5 are formally presented here for the first time; the author calls the idea natural and likely to have occurred to others. The chess methodology is from [GLB24], as an application of model predictive control to computer chess (p. 341).

### Exercises 2.1–2.8 (pp. 342–348)
Summarized under "Exercises worth doing" below.

## Toy example (ours, not from the text)
One state $x$, one-step lookahead, $\alpha=1$. Controls $u\in\{a,b\}$, disturbances $w\in\{1,2\}$. Suppose the values $g(x,u,w)+\tilde J(f(x,u,w))$ are:

| | $w=1$ | $w=2$ |
|---|---|---|
| $u=a$ | 3 | 7 |
| $u=b$ | 5 | 6 |

- **Minimax scheme (2.116):** $\max_w$ for $a$ is $\max(3,7)=7$; for $b$ it is $\max(5,6)=6$. $\min(7,6)=6$, so $\tilde u=b$. This needs 4 table evaluations.
- **Nominal opponent equal to the true maximizer:** $\nu(a)=2$, $\nu(b)=2$. Scheme (2.117) compares $7$ vs $6$ and picks $b$, the same as minimax. This needs only 2 evaluations plus the opponent's moves. It illustrates "coincides if $\nu$ is optimal for the maximizer" (p. 328).
- **Poor nominal opponent:** $\nu(a)=1$, $\nu(b)=1$ (the opponent is assumed to play the weak reply). Scheme (2.117) compares $3$ vs $5$ and picks $a$. Against the true worst case, $a$ costs $7>6$. The guarantee is lost, as the text warns that a poor nominal opponent leads to underestimating the true opponent (p. 329).

## Concepts
- [[minimax-control]] (new) — sequential decision where a minimizer picks controls and a maximizer picks disturbances; DP uses $\min\max$ (p. 322).
- [[rollout]] (new) — policy improvement from a base policy/heuristic evaluated by simulation or, here, by DP/maximization (pp. 322, 335).
- [[sequential-improvement]] (new) — condition that one-step lookahead on the heuristic's cost is no worse than the heuristic's cost; it implies cost improvement (p. 322).
- [[approximation-in-value-space]] (new) — apply the control from lookahead with an approximate cost-to-go $\tilde J$, as in (2.116) (p. 327).
- [[newton-step-interpretation]] (new) — approximation in value space/rollout seen as a Newton step for the Bellman equation, giving superlinear improvement (pp. 328, 331, 334).
- [[bellman-equation]] — here, the minimax Bellman operator $T$, neither convex nor concave in $J$ (p. 327).
- [[policy]] — here also the maximizer policy $\nu(x,u)$ and the nominal follower policies (pp. 327, 334).
- [[nominal-opponent]] (new) — a fixed, deterministic opponent policy approximating the true adversary; makes the problem one-player (pp. 328–329).
- [[multiagent-rollout]] (new) — choose components of a joint control one agent at a time with the others on base policy (p. 326).
- [[distributionally-robust-control]] (new) — minimax model where the "disturbance" is a distribution chosen from a given set (p. 328).
- [[stackelberg-game]] (new) — leader-follower (bilevel) game: followers react after observing the leader (p. 333).
- [[open-loop-feedback-controller]] (new) — re-solve an open-loop problem from the current information vector at every step; a rollout with an open-loop base policy (pp. 338–339).
- [[model-predictive-control]] — the chess scheme is described as an application of it; "rolling/receding horizon" is the lookahead truncation idea (pp. 334, 341).

## Canonical instances
- [[pursuit-evasion]] — pursuer/evader on a graph; base policy by DP against a motionless evader (p. 323).
- [[multiagent-minimax-two-stage]] — exponential control space cut to linear-in-$m$ evaluations (pp. 325–326).
- [[computer-chess-stockfish]] — engine as evaluator and nominal opponent; improves the base engine, with diminishing gains (pp. 329–331).
- [[alphazero-td-gammon-common-policy]] — common policy trained for both players in symmetric games; no reliable theory (p. 326).
- [[katago-adversarial-exploit]] — human adversarial play beat a Go program in 2022 reports (p. 326 footnote).
- [[tsp-rollout-exercise]] — traveling salesman with farthest/nearest neighbor heuristics (pp. 342–343).
- [[parking-problem]] — one-directional parking with empirical probabilities (pp. 343–345).
- [[breakthrough-problem]] — greedy/random/truncated rollout (pp. 345–346).
- [[treasure-hunting]] — adaptive control with parameter $\theta$ (p. 348).

## Bridges (candidates)
- [structural-analogy] Minimax rollout/worst-case lookahead ↔ robust (worst-case) control: the text contrasts engineering worst-case design with zero-sum theory (p. 340).
- [structural-analogy] Nominal-opponent reduction ↔ certainty equivalence: fix a point guess of the uncertain element, solve the resulting deterministic problem (pp. 323, 328).
- [structural-analogy] Leader with nominal follower policies ↔ economics: Stackelberg leaders optimize against a fixed reaction rule of followers (p. 333–334).
- [structural-analogy] OLFC ↔ model predictive control: re-solve an open-loop optimization each step and apply only the first control (p. 338).
- [structural-analogy] Distributionally robust model ↔ statistics: minimax decision theory (Blackwell–Girshick, p. 328).

## Questions this raises
- When is a nominal opponent good enough that (2.117) is near-optimal, and how can one detect that it is too weak (p. 329)?
- Can a theory be built for simultaneously improving the minimizer's and maximizer's policies, or for guaranteed-convergent policy iteration in practice (pp. 326, 340–341)?
- How should the stochastic system (2.118) in the distributionally robust case be handled in an implementable scheme (p. 328)?
- For leader-follower games with non-shared costs, how well do nominal follower policies work beyond "limited preliminary results" (p. 334)?

## Exercises worth doing
- Ex. 2.1 (p. 342) — sequential consistency vs sequential improvement on the traveling salesman problem. The text prints the answers (rollout tour cost 13 vs 45 for the base tour in (a), and the same cost-13 rollout tour in (b)); the text also prints a solution of (b) — difficulty: easy.
- Ex. 2.2 (p. 343) — a base heuristic that is not sequentially improving can make rollout strictly worse — difficulty: easy.
- Ex. 2.3 (pp. 343–345) — computational: parking with unknown probabilities; compare problem approximation, rollout with a greedy heuristic, DP optimum, and the greedy cost recursion — difficulty: hard.
- Ex. 2.4 (p. 345) — breakthrough with a random base heuristic; show $R_k/D_k$ grows exponentially — difficulty: medium.
- Ex. 2.6 (pp. 346–347) — incremental truncated rollout for constraint programming; $O(Nd)$ memory vs depth-first search — difficulty: medium.
- Ex. 2.8 (p. 348) — treasure hunting as adaptive control; rollout with two base policies — difficulty: hard.

## Reading notes
- **Part boundaries:** the part begins on printed p. 322, mid-§2.12.2 (the heading of §2.12.2 is not on these pages), and ends at the end of Exercise 2.8 on p. 348. The source notes say it was split at an even boundary.
- **Page offset:** printed = pdf − 20.
- **Misprints seen in the images:**
  - p. 322: the sequential improvement condition writes $W_k(x_k,w_k)$ under the max, where the earlier formula has $W_k(x_k,u_k)$. This is presumably a misprint.
  - p. 326: the second agent's line writes $g_0(x,\tilde u^1,\dots)$ with $x$, not $x_0$.
  - p. 346: Ex. 2.6(b) reads "$1\le m\le\min\{m,N-k\}$"; the repeated $m$ looks unintended.
  - p. 348: Ex. 2.8 states "$\sum_{i=1}^n p_i<0$". Positive probability of no treasure would require $<1$. I did not use this.
- **Text-layer problems:** equations, overbars on $F$ (Ex. 2.3) and the Ex. 2.8 sum were garbled. I checked them against the page images.
- **Scope of the L3 notes summary:** the bibliography-style lists on pp. 335–336 and 338 are compressed to their claims. Individual citations are not reproduced.
- **Figures:** Figs. 2.12.1–2.12.2 are chess diagrams. I used only their captions and text.
