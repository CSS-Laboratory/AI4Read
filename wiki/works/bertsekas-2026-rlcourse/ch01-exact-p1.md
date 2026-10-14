---
id: bertsekas-2026-rlcourse/ch01-exact-p1
work: bertsekas-2026-rlcourse
unit: "1 Exact and Approximate Dynamic Programming (part 1/6): chapter overview, 1.1 AlphaZero, 1.2 Deterministic DP"
pages: 1-27
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
# Exact and Approximate Dynamic Programming — overview, AlphaZero, and deterministic DP

## L0 — One line
Exact dynamic programming computes optimal cost-to-go functions backwards, and when that is too expensive, approximation in value space (e.g. rollout) replaces them with cheap approximations used in a forward, one-state-at-a-time lookahead.

## L1 — The gist (≤ 120 words)
How can one optimize a long sequence of decisions when the state space is huge? For deterministic finite-horizon problems, the DP algorithm solves "tail subproblems" backwards, using the principle of optimality, and then builds the optimal controls forward. This is exact but intractable for large problems such as the traveling salesman problem. The remedy is approximation in value space: replace the exact cost-to-go by an approximation, trained off-line or obtained on-line by rollout with a base heuristic, and minimize one step (or several) ahead only at the states actually visited. The author presents AlphaZero and TD-Gammon as examples of this architecture.

**Prerequisites:** sums and minimization over finite sets; mathematical induction; shortest paths on a graph; basic idea of a discrete-time dynamical system.

## L2 — Key ideas (5–10 bullets)
- A deterministic finite-horizon problem is a system $x_{k+1}=f_k(x_k,u_k)$ with additive stage costs plus a terminal cost; with finitely many states and controls it is equivalent to a shortest-path problem on a staged graph (pp. 10–12).
- Principle of optimality: the tail of an optimal control sequence is optimal for the tail subproblem. The principle suggests constructing the optimal cost-to-go functions backwards (pp. 14–15).
- The DP algorithm (1.4)–(1.5) produces $J_k^*(x_k)$, the optimal cost of the $(N-k)$-stage tail problem. A forward pass (1.8) then recovers an optimal control sequence (pp. 18–20).
- Exact DP is intractable when the number of states explodes, as in the traveling salesman problem, where the states are partial tours (p. 20).
- Q-factors $Q_k^*(x_k,u_k)$ are the quantities minimized in the DP equation. DP can be written with Q-factors only; exact and approximate forms of such algorithms make up the class of RL methods called Q-learning (p. 22).
- Approximation in value space replaces $J^*_k$ by $\tilde J_k$ in the forward pass (1.11). It needs minimizations only at the states actually encountered; multistep lookahead typically (not always) does better (p. 23).
- Rollout obtains $\tilde J_k$ by running a base heuristic. Under conditions discussed in Chapter 2, it is at least as good as the base heuristic, and its computation is bounded by a polynomial in $N$ in the TSP example (pp. 24–27).
- AlphaZero is described as off-line training (policy iteration) plus on-line play (lookahead with a trained position evaluator); the author says this off-line/on-line division will be conceptually very important for the later discussion (pp. 5–9).

## L3 — Walkthrough

### Chapter introduction (pp. 1–4)
The chapter opens with a contents list for the whole of Chapter 1 (Sections 1.1–1.8; pp. 1–2). This part covers only Sections 1.1 and 1.2. The author lists four purposes (p. 3):
- (a) Give an overview of exact DP with a focus on suboptimal methods. Finite-horizon problems come first, deterministic (Section 1.2) and stochastic (Section 1.3) separately, because deterministic problems are simpler and allow more methods. They include discrete and combinatorial optimization problems. Infinite horizon problems are treated more briefly (Section 1.4).
- (b) Summarize the main RL methodologies, mostly *approximation in value space*. This is the architecture behind AlphaZero, AlphaGo, TD-Gammon and Model Predictive Control (MPC).
- (c) Explain approximation in value space, split into off-line training and on-line play. The two are linked through Newton's method applied to the Bellman equation, discussed for linear quadratic problems in Section 1.5.
- (d) Survey the range of problem types (partial observation, multiagent, unknown model; Section 1.6).

The author states that the book reflects a decision/control and operations research orientation. RL also grew in the AI community, so Section 1.7 gives a glossary of differences in terminology and notation (p. 4).

### 1.1 AlphaZero, Off-Line Training, and On-Line Play (pp. 4–10)
**Claims about performance** (author's description, pp. 4–5). AlphaZero and AlphaGo play better than all competitor programs available in 2022 and much better than all humans. They learned from self-play data without human instruction. The author says AlphaZero's chess play differs from human play in long-term strategic vision. He stresses that it rests on established DP methodology: DP, policy iteration, limited lookahead, rollout and approximation in value space. Similar principles appear in Tesauro's backgammon programs and in a Tetris program based on policy iteration (p. 4).

**Two parts of the design** (p. 5). *Off-line training* learns to evaluate positions and a default ("base") player. *On-line play* generates good moves in real time, using that training.

**Off-line training = policy iteration** (pp. 5–7, Fig. 1.1.1).
- The training produces a sequence of players and position evaluators, represented by a *policy network* (move probabilities) and a *value network* (position score). In DP terms, a position is a state, the evaluator is a cost function (an estimate of optimal cost-to-go), and the player is a randomized policy (p. 5).
- Training is a form of *policy iteration*, with two stages (p. 6):
  - (a) *Policy evaluation*: outcomes of games played from positions are data points used to train the value network.
  - (b) *Policy improvement*: trial move sequences are evaluated from many positions, and the move probabilities are nudged towards the better trials. AlphaZero does this with Monte Carlo Tree Search; simpler ways exist, e.g. trying all move sequences a few moves ahead with the terminal position scored by the evaluator (pp. 6–7).
- Footnote: two-player self-play training may fail against a particular opponent who exploits training vulnerabilities; the author calls this a theoretical but rare possibility (p. 6).
- TD-Gammon also uses approximate policy iteration but evaluates policies with TD($\lambda$). It has no policy network or MCTS, and generates moves by one- or two-step lookahead with its value network (p. 7).

**On-line play = approximation in value space** (pp. 7–9, Figs. 1.1.2–1.1.3).
- Playing the move of highest probability from the policy network is fast but, per the author, not strong enough against skilled opponents. AlphaZero's strength arises only when the trained player and evaluator are embedded in an on-line player that builds a lookahead tree of move/countermove sequences to some depth and evaluates the remaining moves with the value network (p. 7). The policy network is not used directly for on-line play (Fig. 1.1.2 caption, p. 8).
- *Truncated rollout*: run a player for a few moves before applying the evaluator. It is an economical way to extend lookahead. TD-Gammon's final version uses it. Backgammon is stochastic, so rollout needs Monte-Carlo simulation and is time-consuming (pp. 7, 9).
- Architectures of this kind are called *approximation in value space*, also *approximate DP* or *neuro-dynamic programming* (p. 8). Footnote: RL is generally thought to also include *approximation in policy space*, a search over parametrized policies with methods largely unrelated to DP (p. 8).
- In MPC, the number of lookahead-minimization steps is the *control interval*. The total of lookahead steps and truncated-rollout steps is the *prediction interval* (pp. 8–9).

The off-line training and on-line play parts can often be decoupled and designed independently. One may be simple (e.g. rollout with a known policy) while the other is sophisticated (pp. 9–10).

*Intuition note.* Off-line you learn a "scoring rule" for situations. On-line you look a few moves ahead and use the score to judge where the lookahead ends. Learning can often be separated from acting.

### 1.2 Deterministic Dynamic Programming (pp. 10–27)

#### 1.2.1 Finite horizon problem formulation (pp. 10–14)
A discrete-time system over $N$ stages (time steps):
$$x_{k+1}=f_k(x_k,u_k),\qquad k=0,1,\dots,N-1,\tag{1.1}$$
with state $x_k$, control $u_k\in U_k(x_k)$, system function $f_k$, horizon $N$ (pp. 10–11). State space, control space and $f_k$ can be arbitrary and may depend on $k$. The author argues this generality lets one focus on essential algorithmic aspects, and says that the transition-probability notation common in AI/OR is poorly suited to deterministic and continuous-space models (p. 11, footnote).

The cost is additive. For initial state $x_0$ and controls $u_0,\dots,u_{N-1}$ (these with $x_0$ determine the states $x_1,\dots,x_N$ through (1.1)):
$$J(x_0;u_0,\dots,u_{N-1})=g_N(x_N)+\sum_{k=0}^{N-1}g_k(x_k,u_k),\tag{1.2}$$
where $g_N$ is the terminal cost. The optimal value as a function of $x_0$ is
$$J^*(x_0)=\min_{\substack{u_k\in U_k(x_k)\\ k=0,\dots,N-1}}J(x_0;u_0,\dots,u_{N-1}).\tag{1.3}$$
Footnote: "min" is written even when attainment is not certain; likewise "max" (p. 11).

**Discrete optimal control as shortest path** (p. 12, Fig. 1.2.2). If state and control spaces are finite, use an acyclic graph. Nodes are states, arcs are state-control pairs $(x_k,u_k)$ going from $x_k$ to $f_k(x_k,u_k)$, and the arc length is $g_k(x_k,u_k)$. An artificial terminal node $t$ is joined to each $x_N$ by an arc of length $g_N(x_N)$. Control sequences correspond to paths from a stage-0 node, so the problem is equivalent to finding a shortest path from the initial node(s) to $t$. Combinatorial optimization problems can generally be formulated this way (p. 12). Footnote: any shortest path problem (even with a possibly nonacyclic graph) can be reformulated as a finite-state deterministic optimal control problem (p. 12).

**Example 1.2.1 (deterministic scheduling)** (pp. 13–14). Four operations A, B, C, D are performed on one machine. B must come after A, and D after C (so CDAB is allowed, CDBA is not). The setup cost $C_{mn}$ for passing from operation $m$ to $n$ is given, plus startup costs $S_A$ or $S_C$. The cost of ACDB is $S_A+C_{AC}+C_{CD}+C_{DB}$. This is a three-decision problem (the last operation is forced). The state is the set of operations already done, with an artificial initial state. Each decision leads to a unique next state, e.g. at state AC, choosing D gives state ACD at cost $C_{CD}$ (Fig. 1.2.3).

#### 1.2.2 The dynamic programming algorithm (pp. 14–22)
DP breaks an $N$-stage problem into simpler single-stage problems. It starts with $J_N^*=g_N$ and computes $J^*_{N-1},J^*_{N-2},\dots,J_0^*$ in turn (p. 14).

**Principle of optimality** (p. 14, Fig. 1.2.4). Let $\{u_0^*,\dots,u_{N-1}^*\}$ be optimal, with states $x_1^*,\dots,x_N^*$ generated from $x_0$. Consider the *tail subproblem* starting at $x_k^*$ at time $k$: minimize over $\{u_k,\dots,u_{N-1}\}$ with $u_m\in U_m(x_m)$ the cost-to-go
$$g_k(x_k^*,u_k)+\sum_{m=k+1}^{N-1}g_m(x_m,u_m)+g_N(x_N).$$
Then the truncated sequence $\{u_k^*,\dots,u_{N-1}^*\}$ is optimal for this subproblem. Succinctly: "the tail of an optimal sequence is optimal for the tail subproblem" (p. 14).

*Justification* (p. 14): if the tail were not optimal, we could lower the cost by switching to an optimal tail once $x_k^*$ is reached, because the earlier controls do not restrict future choices. *Analogy* (p. 14–15): if the fastest route from Phoenix to Boston passes through St Louis, its St Louis–Boston part is the fastest route for a trip from St Louis to Boston. Footnote p. 15 quotes Bellman's statement of the same idea.

The consequence: construct the optimal cost function backwards, solving all tail subproblems of a given length using the solutions for shorter tails (p. 15).

**Example 1.2.1 continued: DP on the scheduling problem** (pp. 15–17, Fig. 1.2.5). The numbers below come from the figure. Arc costs: start A 5, start C 3; A→AB 2, A→AC 3; AB→ABC 3; AC→ACB 4, AC→ACD 6; C→CA 4, C→CD 6; CA→CAB 2, CA→CAD 4; CD→CDA 3. Terminal costs: ABC 6, ACB 1, ACD 3, CAB 1, CAD 3, CDA 2.
- *Tail subproblems of length 2* (states AB, AC, CA, CD):
  - AB: only C then D is possible, cost $3+6=9$.
  - AC: B then D costs 5; D then B costs 9; optimal 5.
  - CA: B then D costs 3; D then B costs 7; optimal 3.
  - CD: only A then B, optimal 5.
- *Length 3*:
  - State A: B first costs $2+9=11$; C first costs $3+5=8$; optimal 8.
  - State C: A first costs $4+3=7$; D first costs $6+5=11$; optimal 7.
- *Length 4*: start with A costs $5+8=13$; start with C costs $3+7=10$; the optimal cost is 10.
- Going forward, choosing at each node the arc that attains the minimum gives the optimal schedule CABD (p. 17).

**The DP algorithm** (p. 18, Fig. 1.2.6). Start with
$$J_N^*(x_N)=g_N(x_N),\quad\text{for all }x_N,\tag{1.4}$$
and for $k=0,\dots,N-1$,
$$J_k^*(x_k)=\min_{u_k\in U_k(x_k)}\Big[g_k(x_k,u_k)+J^*_{k+1}\big(f_k(x_k,u_k)\big)\Big],\quad\text{for all }x_k.\tag{1.5}$$
At stage $k$ the computation must be done for all states $x_k$ before moving to stage $k-1$ (p. 18).

**Key fact** (pp. 18–19). For every $k$ and every state $x_k$,
$$J_k^*(x_k)=\min_{\substack{u_m\in U_m(x_m)\\ m=k,\dots,N-1}}J(x_k;u_k,\dots,u_{N-1}),\tag{1.6}$$
$$J(x_k;u_k,\dots,u_{N-1})=g_N(x_N)+\sum_{t=k}^{N-1}g_t(x_t,u_t).\tag{1.7}$$
So $J_k^*(x_k)$ is the optimal cost of the $(N-k)$-stage tail subproblem; in particular $J_0^*(x_0)=J^*(x_0)$. $J_k^*$ is the *optimal cost-to-go function* (in maximization problems, with max in (1.5), the *optimal value function*) (p. 19).

*Proof (footnote, p. 19), by induction.* It holds for $k=N$ since $J_N^*=g_N$. For general $k$, using (1.6)–(1.7):
$$J_k^*(x_k)=\min_{\substack{u_t\in U_t(x_t)\\ t=k,\dots,N-1}}\Big[g_N(x_N)+\sum_{t=k}^{N-1}g_t(x_t,u_t)\Big]$$
$$=\min_{u_k\in U_k(x_k)}\Big[g_k(x_k,u_k)+\min_{\substack{u_t\in U_t(x_t)\\ t=k+1,\dots,N-1}}\Big[g_N(x_N)+\sum_{t=k+1}^{N-1}g_t(x_t,u_t)\Big]\Big]$$
$$=\min_{u_k\in U_k(x_k)}\Big[g_k(x_k,u_k)+J^*_{k+1}\big(f_k(x_k,u_k)\big)\Big],$$
where the last equality uses the induction hypothesis. The author notes $J_k^*$ may equal $-\infty$ for some $x_k$, and the argument remains valid (p. 19).

**Forward construction of an optimal sequence** (p. 20). Once $J_0^*,\dots,J_N^*$ are known: set $u_0^*\in\arg\min_{u_0\in U_0(x_0)}[g_0(x_0,u_0)+J_1^*(f_0(x_0,u_0))]$ and $x_1^*=f_0(x_0,u_0^*)$. Then for $k=1,\dots,N-1$,
$$u_k^*\in\arg\min_{u_k\in U_k(x_k^*)}\Big[g_k(x_k^*,u_k)+J^*_{k+1}\big(f_k(x_k^*,u_k)\big)\Big],\quad x_{k+1}^*=f_k(x_k^*,u_k^*).\tag{1.8}$$
The same method gives an optimal sequence for any tail subproblem (p. 20).

*Intuition note.* $J_k^*(x)$ is the best possible remaining cost if you are at $x$ at time $k$. Knowing it for the next stage turns the multi-stage problem into a one-step comparison: "cost now + best cost afterwards".

**Example 1.2.2 (traveling salesman problem, TSP)** (pp. 20–21, Fig. 1.2.7). Given $N$ cities and travel times, find a minimum-time tour visiting each city once and returning to the start. As a DP problem, the stage-$k$ states are sequences of $k$ distinct cities (initial state: the start city, here A). Adding a city costs the travel time between the last two cities, and each $N$-city sequence is joined to an artificial terminal node by an arc costing the return time. In the four-city example the travel matrix (rows = from, columns = to, A–D) is A: $-,5,1,15$; B: $20,-,20,4$; C: $1,20,-,3$; D: $15,4,3,-$. DP gives $J_0^*(A)=13$, and the unique optimal tour is ABDCA (arc costs $5+4+3+1=13$, [reading from figure]). The number of nodes grows exponentially with $N$, so exact DP is intractable for large $N$; such problems are typically handled by approximation methods, some DP-based (pp. 20–21).

**Q-factors and Q-learning** (p. 22). The optimal Q-factors are
$$Q_k^*(x_k,u_k)=g_k(x_k,u_k)+J^*_{k+1}\big(f_k(x_k,u_k)\big),\tag{1.9}$$
i.e. the expressions minimized on the right side of (1.5). Then
$$J_k^*(x_k)=\min_{u_k\in U_k(x_k)}Q_k^*(x_k,u_k),\tag{1.10}$$
and the DP algorithm can be written with Q-factors only:
$$Q_k^*(x_k,u_k)=g_k(x_k,u_k)+\min_{u_{k+1}\in U_{k+1}(f_k(x_k,u_k))}Q^*_{k+1}\big(f_k(x_k,u_k),u_{k+1}\big).$$
Exact and approximate forms of this and related algorithms, including stochastic counterparts, form an important class of RL methods called *Q-learning* (p. 22). Footnote: "action value", "state-action value" and "Q-value" are other names; "Q-factor" comes from the notation of an influential thesis [Wat89] (p. 22).

*Intuition note.* A Q-factor scores a *state-action pair* by the cost of acting now and then behaving optimally. Minimizing the Q-factor over actions gives $J_k^*$ (1.10).

#### 1.2.3 Approximation in value space and rollout (pp. 22–27)
The forward construction (1.8) needs $J_k^*$ for all $x_k$ and $k$, often prohibitively expensive. Replacing $J^*_k$ by approximations $\tilde J_k$ gives a suboptimal sequence $\{\tilde u_0,\dots,\tilde u_{N-1}\}$ (p. 22):
$$\tilde u_k\in\arg\min_{u_k\in U_k(\tilde x_k)}\Big[g_k(\tilde x_k,u_k)+\tilde J_{k+1}\big(f_k(\tilde x_k,u_k)\big)\Big],\quad \tilde x_{k+1}=f_k(\tilde x_k,\tilde u_k),\tag{1.11}$$
starting from $\tilde x_0=x_0$ (for $k=0$ the same formula with $x_0$; p. 23). Footnote: the idea is called "search" or "tree search" in AI, and underlies the A* method for large shortest path problems (p. 22).

- The computation goes forward only, and is independent of how $\tilde J_k$ was computed (p. 23).
- The minimization (1.11) is needed only at the $N$ states $x_0,\tilde x_1,\dots,\tilde x_{N-1}$ met during on-line control, not at every state of a possibly huge state space (p. 23). The text states this motivation for "stochastic DP problems".
- (1.11) is *one-step lookahead*. *Multistep lookahead* solves an $\ell$-step DP problem with terminal cost approximation $\tilde J_{k+\ell}$ ($1<\ell<N-k$). It typically (but not always) performs better, e.g. long multistep lookahead is critical for AlphaZero chess. Intuitively, with $\ell$ stages treated exactly, the effect of the error $\tilde J_{k+\ell}-J^*_{k+\ell}$ tends to become less significant as $\ell$ grows, but the optimization costs more time (p. 23).

**Rollout with a base heuristic** (p. 24). $\tilde J_k$ may come from off-line training (Section 1.1) or on-line rollout. In *rollout*, $\tilde J_k(x_k)$ is obtained when needed by running a *base heuristic* (base policy) from $x_k$ for many stages and accumulating the costs.
- *Cost improvement*: the cost of rollout with a base heuristic is less than or equal to the cost of the base heuristic, for any starting state, provided the heuristic satisfies simple conditions discussed in Chapter 2 (p. 24). Footnote: the intuition is that rollout adds a first-stage optimization on top of the heuristic, which also suggests why multistep lookahead tends to do better in rollout schemes (p. 24).
- Deterministic algorithm with finitely many controls: at $x_k$, for every $u_k\in U_k(x_k)$ generate the next state $x_{k+1}$. Run the base heuristic from it to get states $\{x_{k+1},\dots,x_N\}$ and controls $\{u_{k+1},\dots,u_{N-1}\}$ with $x_{t+1}=f_t(x_t,u_t)$, and the cost
$$H_{k+1}(x_{k+1})=g_{k+1}(x_{k+1},u_{k+1})+\cdots+g_{N-1}(x_{N-1},u_{N-1})+g_N(x_N).$$
- Apply the control minimizing $g_k(x_k,u_k)+H_{k+1}(x_{k+1})$ (p. 24). Equivalently, with approximate Q-factors,
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}\tilde Q_k(x_k,u_k),\tag{1.12}$$
$$\tilde Q_k(x_k,u_k)=g_k(x_k,u_k)+H_{k+1}\big(f_k(x_k,u_k)\big)\tag{1.13}$$
(Fig. 1.2.8, p. 25).
- *Cost of rollout* (p. 25): the base heuristic is run a number of times bounded by $Nn$, where $n$ bounds the number of controls per state. If $n$ is small relative to $N$, this is a small multiple of $N$ times one heuristic run; if $n$ is bounded by a polynomial in $N$, the time ratio is polynomial in $N$.

*Intuition note.* Rollout asks, for each possible next move, "how would my simple rule do from there?" and picks the move whose total (move cost + simple rule's cost afterwards) is lowest. Because it adds a real optimization step on top of the simple rule, it should not do worse (under the stated conditions).

**Example 1.2.3 (TSP continued)** (pp. 25–27, Figs. 1.2.9–1.2.10). Cities $c=0,\dots,N-1$ with traversal costs $g(c,c')$; direct travel between any pair is assumed, and precluded pairs get a very high cost. The *nearest neighbor heuristic* extends a partial tour $\{c_0,\dots,c_k\}$ by the city $c_{k+1}\neq c_0,\dots,c_k$ minimizing $g(c_k,c_{k+1})$. It yields a complete tour with cost
$$g(c_0,c_1)+\cdots+g(c_{N-2},c_{N-1})+g(c_{N-1},c_0).\tag{1.14}$$
In the DP formulation, states are partial tours, feasible controls are the unvisited cities, and the number of states grows exponentially with $k$. Rollout with this base heuristic: at partial tour $\{c_0,\dots,c_k\}$, run nearest neighbor from each $\{c_0,\dots,c_k,c\}$ with $c$ unvisited, then add the city $c$ that gave the cheapest completed tour. The computation is bounded by a polynomial in $N$ and is much smaller than exact DP (p. 27).

Fig. 1.2.10 (as captioned, p. 27): at city A the base heuristic gives tour ACDBA ($T_0$). Rollout compares ABCDA, ACDBA, ADCBA, finds ABCDA ($T_1$) cheapest and moves to B. At AB it compares ABCDA and ABDCA, finds ABDCA ($T_2$) cheapest, and moves to D, then C and A. $T_2$ is optimal here and $T_0$ is suboptimal. The author calls this "suggestive of a general result": under some conditions on the base heuristic (Chapter 2; satisfied by nearest neighbor), rollout generates solutions of decreasing cost (p. 27). See also Exercise 1.1.

## Toy example (ours, not from the text)
Two stages ($N=2$), initial state $S$, controls $L$ or $R$.

| | $f$ | $g$ |
|---|---|---|
| Stage 0 | $S\xrightarrow{L}P$, $S\xrightarrow{R}Q$ | $g_0(S,L)=1$, $g_0(S,R)=2$ |
| Stage 1 | $P\xrightarrow{L}X$, $P\xrightarrow{R}Y$, $Q\xrightarrow{L}X$, $Q\xrightarrow{R}Y$ | $g_1(P,L)=4$, $g_1(P,R)=5$, $g_1(Q,L)=1$, $g_1(Q,R)=2$ |
| Terminal | | $g_2(X)=2$, $g_2(Y)=0$ |

**Exact DP.** Use (1.4)–(1.5).
- $J_2^*(X)=2$, $J_2^*(Y)=0$.
- $J_1^*(P)=\min(4+2,\,5+0)=\min(6,5)=5$ (control $R$).
- $J_1^*(Q)=\min(1+2,\,2+0)=\min(3,2)=2$ (control $R$).
- $J_0^*(S)=\min(1+J_1^*(P),\,2+J_1^*(Q))=\min(6,4)=4$ (control $R$).
- Forward pass (1.8): $u_0^*=R$ gives $Q$, then $u_1^*=R$ gives $Y$. Total $2+2+0=4$.

**Greedy** (minimize only the stage cost): $L$ at $S$ (1), then at $P$ the cheaper stage cost is $L$ (4), ending in $X$ (2): total $1+4+2=7$. So optimality needs the cost-to-go, not just the stage cost.

**Rollout** with base heuristic "always $L$". The base heuristic alone from $S$ costs $1+4+2=7$.
- At $S$: the base heuristic from $P$ costs $H_1(P)=4+2=6$ and from $Q$ costs $H_1(Q)=1+2=3$. Q-factors (1.13): $\tilde Q_0(S,L)=1+6=7$, $\tilde Q_0(S,R)=2+3=5$. Choose $R$, reaching $Q$.
- At $Q$ (last stage): $\tilde Q_1(Q,L)=1+2=3$, $\tilde Q_1(Q,R)=2+0=2$. Choose $R$.
- Rollout cost: $2+2+0=4\le 7$, so it improves on the base heuristic; here it equals the optimum.

## Concepts
- [[dynamic-programming-algorithm]] (new) — backward recursion (1.4)–(1.5) building optimal tail costs $J_k^*$ for all states (p. 18)
- [[principle-of-optimality]] — the tail of an optimal control sequence is optimal for the tail subproblem (p. 14)
- [[bellman-equation-value-function]] — here the deterministic finite-horizon DP equation (1.5); $J_k^*$ is the optimal cost-to-go (called value function in maximization problems) (pp. 18–19)
- [[cost-to-go]] (new) — cost of the remaining stages from $x_k$; its optimum is $J_k^*(x_k)$ (pp. 14, 19)
- [[state]] — the quantity $x_k$ that, with controls, determines future states via $f_k$; in the scheduling example, the set of operations already done (pp. 10, 13)
- [[q-factor]] (new) — $g_k(x_k,u_k)+J^*_{k+1}(f_k(x_k,u_k))$; also "action value" or "Q-value" (p. 22)
- [[approximation-in-value-space]] (new) — using $\tilde J_k$ for $J_k^*$ in a forward lookahead minimization (pp. 22–23)
- [[lookahead-minimization]] (new) — one-step or $\ell$-step optimization ending with a terminal cost approximation (p. 23)
- [[rollout]] (new) — getting $\tilde J_k$ on-line by running a base heuristic from each candidate next state (p. 24)
- [[base-heuristic]] (new) — a suboptimal control scheme whose cost approximates cost-to-go in rollout (p. 24)
- [[cost-improvement-property]] (new) — rollout cost $\le$ base heuristic cost, under conditions deferred to Chapter 2 (p. 24)
- [[policy-iteration]] (new) — alternating policy evaluation and policy improvement; the AlphaZero training structure (p. 6)
- [[policy]] — a rule choosing actions from states; for a chess player, a randomized rule giving move probabilities (p. 5)
- [[model-predictive-control]] — approximation in value space used in control design; control interval and prediction interval defined here (pp. 8–9)

## Canonical instances
- [[alphazero]] — off-line policy-iteration training plus on-line lookahead with a trained evaluator (pp. 4–8)
- [[td-gammon]] — approximate policy iteration trained with TD($\lambda$); on-line lookahead with truncated rollout (pp. 7, 9)
- [[deterministic-scheduling-example]] — four-operation scheduling solved by backward DP; optimal cost 10, schedule CABD (pp. 13–17)
- [[traveling-salesman-dp]] — exponential state growth makes exact DP intractable; rollout with nearest neighbor is polynomial (pp. 20, 25–27)

## Bridges (candidates)
- [same-math] DP backward recursion (1.5) ↔ shortest-path algorithms on staged acyclic graphs: the book states the equivalence of finite-state deterministic problems and shortest paths (p. 12)
- [same-math] Principle of optimality / $J_k^*$ recursion ↔ control-theory Bellman equation / value function: this unit gives the finite-horizon deterministic case
- [structural-analogy] Approximation in value space with a control interval and prediction interval ↔ model predictive control: the book relates the two (pp. 8–9)
- [structural-analogy] Off-line training vs on-line play ↔ design-time vs run-time split in controllers: only the book's own framing; fuller treatment later
- [metaphor] Phoenix–Boston route via St Louis ↔ tail optimality: the author's own travel analogy (p. 14–15)

## Questions this raises
- Under what exact conditions on the base heuristic does rollout guarantee cost improvement (promised for Chapter 2)?
- How good must $\tilde J_k$ be for one-step lookahead to be near optimal, and how does the error shrink with lookahead length $\ell$?
- What changes in (1.5) and in the forward pass when transitions are random (Section 1.3)?
- How does the claimed link between off-line training and on-line play through Newton's method on the Bellman equation work (Section 1.5)?

## Exercises worth doing
Only Exercise 1.1 is mentioned in this part (p. 27); it relates to Example 1.2.3, comparing the nearest neighbor heuristic with its rollout algorithm. Its statement lies outside the pages given, so no difficulty rating is possible here.

## Reading notes
- This unit covers printed pp. 1–27 (pdf 21–47): the chapter title page and contents (pp. 1–2), the chapter introduction (pp. 3–4), Section 1.1 (pp. 4–10) and Section 1.2 through the end of Example 1.2.3 (p. 27). Section 1.2.3 ends after Fig. 1.2.10, with Section 1.3 following in the next part. Printed = pdf − 20.
- The text layer is garbled in figures (Figs. 1.1.1–1.1.3, 1.2.3, 1.2.5–1.2.10). Numbers for Figs. 1.2.3, 1.2.5, 1.2.7 and 1.2.10 were read from the page images. Math symbols in the text layer show arrows for "∈" (e.g. "u_k → U_k"); the images show ∈.
- Apparent inconsistency in Fig. 1.2.10 (p. 27), as the image shows it: the matrix gives C→D = 1 and B→C = 1, but arc AC→ACD is labelled 3 and arc ADB→ADBC is labelled 20. The caption's comparison (T1 cheaper than T0) matches the arc labels, not the matrix. I did not resolve this and used only the caption's statements. The matrix also differs from the one in Fig. 1.2.7.
- Fig. 1.2.7 is the TSP with matrix A–D; the caption states the optimal sequence ABDCA is unique.
- On p. 23, the motivation sentence refers to "stochastic DP problems" though the discussion is deterministic. I reported it as printed.
- Summary of the AlphaZero/AlphaGo performance claims (p. 4) is the author's own description, not independently stated evidence.
