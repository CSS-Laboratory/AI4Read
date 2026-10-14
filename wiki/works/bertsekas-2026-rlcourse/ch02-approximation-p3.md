---
id: bertsekas-2026-rlcourse/ch02-approximation-p3
work: bertsekas-2026-rlcourse
unit: "2 Approximation in Value Space - Rollout Algorithms (part 3/7): end of Sec. 2.3, Sec. 2.4, start of Sec. 2.5"
pages: 216–242
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
# Rollout: sequence selection results, multistep lookahead, constrained rollout

## L0 — One line
Rollout (one-step lookahead using a base policy or heuristic to evaluate the leaves) is guaranteed to do at least as well as its base policy under a sequential-improvement condition, and it can be extended cheaply to long lookahead and to trajectory constraints.

## L1 — The gist (≤ 120 words)
This part finishes rollout for most-likely-sequence selection, then extends rollout to multistep lookahead and to constrained problems. One-step rollout never yields a less likely sequence than its greedy base policy; experiments recover roughly 60–90% of greedy's loss against optimal. In deterministic problems, one-step minimization plus truncated rollout needs computation linear in the lookahead length ℓ, while pure ℓ-step minimization grows exponentially. Iterative deepening, pruning and incremental multistep rollout reduce lookahead cost further. With trajectory constraints, rollout discards infeasible candidates; if the base heuristic is sequentially improving and feasible from the start, the result is feasible and no costlier.

**Prerequisites:** finite-horizon deterministic DP; shortest paths on layered graphs; Markov chain transition probabilities; Q-factors; big-O counting.

## L2 — Key ideas
- Rollout with one-step lookahead gives sequences at least as likely as the greedy base policy, for every start state and time (proved by induction, Eq. 2.32) (pp. 217–218).
- Truncated rollout saves computation. Double rollout is two policy iterations, i.e. two Newton steps; each extra iteration multiplies the cost by an amplification factor, so it is viable on-line mainly together with truncation and simplification (pp. 216–217, 221).
- Experiments (|X|=100, q=5, N=100): rollout recovers ≈58–93% of greedy's optimality loss; double rollout does better; truncation to m=10 costs little (pp. 219–221).
- Deterministic multistep lookahead is a layered shortest-path problem plus a terminal cost J̃. Scheme (b), one-step minimization with (ℓ−1)-step truncated rollout, needs at most about m²ℓ evaluations of J̃, against up to m^ℓ for pure ℓ-step minimization (pp. 224–226).
- Forward DP gives iterative deepening ("anytime"), optionally with pruning. Incremental multistep rollout grows a subgraph guided by D(x)+H(x); the parameter δ matters: δ=0 (with S={x₀} and a sequentially improving heuristic) gives exactly rollout, and large δ acts like forward DP (pp. 227–231).
- IMR can be cheapened, because its termination does not depend on which leaf is expanded (p. 231).
- Constrained rollout runs the base heuristic from every one-step extension, discards infeasible complete trajectories, and keeps the cheapest feasible one (pp. 236–238).
- Sequential improvement (implied by sequential consistency) plus a feasible R(ỹ₀) guarantees feasibility and cost no worse than the base heuristic (Prop. 2.5.1) (pp. 240–242).

## L3 — Walkthrough

### End of Sec. 2.3 — rollout for most-likely-sequence selection
Notation here: π̄ is the greedy policy, π̃ the rollout policy, P_k(x,·) the probability of the sequence the policy generates from x at time k. Rollout maximizes over next states y the Q-factor p(y|x_k)P_{k+1}(y,π̄).

**Cheaper variants (p. 216).**
- *Simplified rollout:* consider only some next states y. Often many p(y|x) are very close to 0 and can be safely ignored. The page opens mid-sentence on this point.
- *m-step truncated rollout* (needs k+m<N): maximize over y
$$p(y\mid x_k)\,P_{k+1,m}(y,\bar\pi)\tag{2.31}$$
$$P_{k+1,m}(y,\bar\pi)=p\big(y_{k+2,k+1}(y,\bar\pi)\mid y\big)\prod_{i=k+2}^{k+m}p\big(y_{i+1,k+1}(y,\bar\pi)\mid y_{i,k+1}(y,\bar\pi)\big)$$
Here $y_{i,k+1}(y,\bar\pi)$ is the state at time $i$ on the greedy path started at $y$ at time $k+1$. Without truncation, the product runs to $N-1$ and has $N-k-1$ steps (p. 216).

**Double rollout (pp. 216–217).**
- Applying rollout repeatedly, each rollout policy being the next base policy, is policy iteration.
- Two on-line iterations ("double rollout") equal two successive Newton steps for Bellman's equation.
- One-step rollout needs $O(qN)$ base-policy applications, with $q$ the number of Q-factors per stage. Each extra policy iteration multiplies the cost by $O(qN)$.
- It may still be viable on-line with truncation and simplification to reduce $q$, because the calculations are simple and parallelizable.
- Footnote (p. 217): $m$ greedy steps cost $q\cdot m$ comparisons. Truncated rollout needs $q^2m+q$ comparisons per stage, so $(q^2m+q)N$ in total, against $qN$ for greedy. The amplification factor is $qm+1$. Double rollout adds an extra factor of no more than $qm+1$.

**Performance improvement (pp. 217–218).** Claim: for all states $x\in X$ and all $k$,
$$P_k(x,\bar\pi)\le P_k(x,\tilde\pi).\tag{2.32}$$
- *Base case:* $P_N(x,\bar\pi)=P_N(x,\tilde\pi)\equiv1$.
- *Induction step:* assume $P_{k+1}(x,\bar\pi)\le P_{k+1}(x,\tilde\pi)$ for all $x$. Then
$$P_k(x,\tilde\pi)=p(\tilde\mu_k(x)\mid x)P_{k+1}(\tilde\mu_k(x),\tilde\pi)\ \ge\ p(\tilde\mu_k(x)\mid x)P_{k+1}(\tilde\mu_k(x),\bar\pi)\ \ge\ p(\bar\mu_k(x)\mid x)P_{k+1}(\bar\mu_k(x),\bar\pi)=P_k(x,\bar\pi).$$
- Justifications: the first equality is the definition of the rollout policy's probabilities. The first inequality is the induction hypothesis. The second inequality holds because the rollout choice $\tilde\mu_k(x)$ maximizes the Q-factor $p(y\mid x)P_{k+1}(y,\bar\pi)$ over $y$. The last equality is the definition for the greedy policy.
- The printed third line has $p(\tilde\mu_k(x)\mid x)$ in front of $P_{k+1}(\bar\mu_k(x),\bar\pi)$. I wrote $p(\bar\mu_k(x)\mid x)$, which the stated justification requires (p. 218).

*Intuition note.* At each step the rollout choice scores at least as well as the greedy choice under the greedy continuation. By induction from the end of the horizon, the whole sequence is at least as likely.

**Further remarks (p. 218).**
- Improvement continues over successive rollout iterations. After enough iterations it yields the most likely selection policy, by finite convergence of policy iteration for finite-state Markovian decision problems.
- A similar proof works for ℓ-step lookahead. Other books give conditions for simplified rollout.
- It is *not* necessarily true that performance improves as ℓ increases, nor that m-step truncated rollout beats the greedy policy. Footnote: truncated rollout does beat an m-step version of greedy.
- Such deterioration examples are artificial and apparently rare in practice.

**Computational comparison (pp. 219–221).**
- Setup: random Markov chains where each state has exactly $q$ successors with $p(y|x)>0$. Successors and probabilities are drawn from uniform distributions. The branching factor is $q/|X|$ in percent.
- Sequence probabilities are averaged as geometric means over a sample $C$ of chains and all start states $x$. For greedy:
$$(\bar P_0)^{1/N}=\frac{\sum_{c\in C}\sum_{x\in X}\big(P_{0,c}(x,\bar\pi)\big)^{1/N}}{|C|\cdot|X|}\tag{2.33}$$
- The optimal value $(P_0^*)^{1/N}$ and the rollout value $(\tilde P_0)^{1/N}$ are defined the same way, with $P^*_{0,c}(x)$ and $\tilde\pi$ respectively.
- Percentage recovery of greedy's optimality loss:
$$\frac{(\tilde P_0)^{1/N}-(\bar P_0)^{1/N}}{(P_0^*)^{1/N}-(\bar P_0)^{1/N}}\times100\ (\%)\tag{2.34}$$
- Experiment: 50 chains, $|X|=100$, branching 5%, $N=100$, truncation $m=10$.
- Fig. 2.3.15 (single rollout), read from the bars: ℓ=1–5 without truncation: 64.3, 79.64, 82.89, 87.62, 91.51; with truncation: 58.36, 73.02, 84.18, 84.37, 92.79.
- Fig. 2.3.16 (double rollout): without truncation 87.97, 89.84, 90.72, 91.47, 92.73; with truncation 80.75, 85.31, 89.27, 89.75, 91.34.
- Author's conclusions: improvement grows with lookahead length. Truncation to 10 of 100 steps barely hurts, and the same insensitivity has been seen elsewhere. Double rollout clearly beats single rollout. Truncation also makes double rollout possible (pp. 220–221).

### 2.4 Approximation in value space with multistep lookahead
**Multistep rollout, deterministic case (pp. 221–222, Fig. 2.4.1).** From $x_k$, take every ℓ-step-ahead state (ℓ=2 in the figure). Run the base heuristic from each. Compute the lookahead cost plus the heuristic cost. Pick the best leaf, apply the first control $\tilde u_k$ and discard the rest. If the ℓ-step minimization is too slow, use approximations.

**Truncated rollout with terminal cost approximation (pp. 222–223).**
- The heuristic runs only a limited number of steps from the leaves, and a terminal cost approximation $\tilde J$ is added. $\tilde J$ may simply be zero, which often works well when the combined lookahead is long.
- $\tilde J$ may also come from problem approximation or off-line training (e.g. a neural network). It matters most when much of the cost is incurred at termination, e.g. in games.
- This scheme is a Newton step with a starting point set by the truncated rollout and $\tilde J$. The interpretation requires reformulating the problem as an equivalent infinite-horizon SSP problem. The scheme then inherits the Newton step's fast convergence (p. 223).

**General ℓ-step scheme without rollout (pp. 223–225, Fig. 2.4.3).**
- The graph is acyclic, with root $x_0$ (the current state) and layers $n=1,\dots,\ell$. Layer $n$ holds the states reachable with $n$ feasible controls.
- Arc cost, minimized over controls giving the same transition:
$$\hat g_n(x_n,x_{n+1})=\min_{\{u_n\in U_n(x_n)\,\mid\,x_{n+1}=f_n(x_n,u_n)\}}g_n(x_n,u_n)\tag{2.35}$$
- Let $D(x_\ell)$ be the shortest distance from $x_0$ to $x_\ell$. Choose $x_\ell^*$ minimizing $D(x_\ell)+\tilde J(x_\ell)$ and apply the control of the first move $x_0\to x_1^*$.
- All shortest-path problems can be solved at once by backward DP (p. 225).

**Long lookahead (p. 225).**
- Deterministic problems are simpler than AlphaZero-type schemes: no Monte Carlo simulation, and a deterministic shortest-path problem instead of a stochastic one.
- Working hypothesis: longer lookahead is better. This is typically true in practice but not provable without extra assumptions; footnote: isolated artificial counterexamples exist.
- On-line cost often grows exponentially with lookahead length, so use the longest lookahead the time budget allows.

**Rollout versus lookahead minimization (pp. 225–226).**
- Base policy: $\tilde\mu(x)\in\arg\min_{u\in U(x)}\big[g(x,u)+\tilde J(f(x,u))\big]$ (2.36). Assume the main cost is evaluating $\tilde J$, and $|U(x)|=m$ for all $x$.
- (a) ℓ-step lookahead minimization with $\tilde J$, no rollout: up to $m^\ell$ evaluations (leaf count; the page writes "m-step", a slip for ℓ-step).
- (b) One-step lookahead with $(\ell-1)$-step truncated rollout. This is the TD-Gammon scheme, used out of necessity (p. 226).
  - Stage $k$: $m$ evaluations, giving $m$ states $x_{k+1}$.
  - Each $x_{k+1}$ needs $\ell-1$ base-policy controls, each costing $m$ evaluations, so $m(\ell-1)$ per state and $m^2(\ell-1)$ in total.
  - Total: at most $m^2\ell$ evaluations.
- Both look ℓ stages ahead, but cost grows exponentially (a) versus linearly (b) in ℓ.
- Hence short minimization with long truncated rollout can raise total lookahead within a budget. By the Newton-step view, truncated rollout with a reasonably good (e.g. stable) base policy often works about as well as long lookahead minimization (p. 226).

*Intuition note.* Rollout follows one path per leaf instead of branching at every step. The work therefore grows like a multiple of ℓ rather than $m^\ell$.

### 2.4.1 Iterative deepening using forward DP (pp. 227–228)
- Forward DP is backward DP with arcs reversed:
$$D_{n+1}(x_{n+1})=\min_{x_n}\big[\hat g_n(x_n,x_{n+1})+D_n(x_n)\big]$$
- The ℓ-step solution minimizes $D_\ell(x_\ell)+\tilde J(x_\ell)$.
- *Iterative deepening:* solve the $n$-step lookahead problem for $n=1,2,\dots$ until the budget is exhausted. This is an "anytime" algorithm: it returns a usable $n$-step solution for some $n\le\ell$ (with a suitable terminal cost). The author notes this is well known from chess programming.
- *With pruning (Fig. 2.4.5):* delete layer-$n$ states $\hat x_n$ whose $D_n(\hat x_n)+\tilde J(\hat x_n)$ is "far from the minimum" over $x_n$. This automatically removes some states of layer $n+1$. The rationale is that such states are "unlikely" to lie on the shortest path. Pruning is progressive, layer by layer (p. 228).

### 2.4.2 Incremental multistep rollout (IMR) (pp. 229–232)
- IMR applies a base heuristic and forward DP to expanding subgraphs of the lookahead graph $G$. It extends a connected subgraph of many paths, not a single path as in rollout. It is similar to MCTS but, in the author's view, more appropriate for deterministic problems, where Monte Carlo simulation makes no sense (p. 229).
- It maintains a connected acyclic subgraph $S\ni x_0$. Each iteration expands the leaf $x^*$ of $S$ minimizing $D(x)+H(x)$ and adds its neighbors to $S$ (p. 229).
  - $D(x)$ is the shortest distance from $x_0$ to $x$ using only arcs of $S$, computed by forward DP. It may be replaced by an approximation.
  - $H(x)$ is the sum of three terms: the base-heuristic cost from $x$ to a last-layer state $x_\ell$; $\tilde J(x_\ell)$; and a loss $L(x)=\delta\cdot(\text{layer index of }x)$ with $\delta>0$. $L$ penalizes distant layers and encourages backtracking (p. 230).
- Start: $S$ and a path $P$ from $x_0$ (possibly just $x_0$). Stop when the end of $P$ is in layer ℓ, or earlier if the budget runs out (p. 230).
- Role of δ (p. 230):
  - If $\delta=0$, the initial $S$ is $\{x_0\}$ and the base heuristic is sequentially improving, IMR performs exactly like rollout for the ℓ-step problem.
  - If δ is large enough, it acts like forward DP, because every node of a layer is expanded before the next layer.
  - Larger δ means more backtracking, more paths and more base-heuristic calls, so δ is an "exploration parameter". Good values are found by experiment (p. 231); adaptive δ is possible.
- If the base heuristic is sequentially consistent, a local optimality property of the IMR trajectory can be shown (cf. Sec. 2.3.1) (p. 231).

**Cheaper IMR variants (pp. 231–232).**
- Keep a list $L$ of leaves. Each step expands one leaf of $L$, adds its new neighbors to $S$ and $L$ (computing $D,H$ on entry), then removes the expanded leaf. A node enters $L$ at most once, so the algorithm terminates at layer ℓ *whichever* leaf is expanded. Minimizing $D+H$ is therefore not essential (p. 231).
- Variant (1): replace $D(x)$ by an upper bound, the shortest distance through $S$ at the time $x$ enters $L$. It may be larger than the current $D(x)$ but is computed once (pp. 231–232).
- Variant (2): keep $L$ as a priority queue and take the top node. Heap or bucket structures speed this up. Simpler label-correcting schemes (SLF, LLL, threshold algorithms in [Ber98]) are said to work very well in practice, typically better than heap or bucket schemes (p. 232).
- For δ small or 0, the variants can be made to coincide with rollout and inherit its cost improvement. Fortified rollout (Sec. 2.3) can restore the property (p. 232).

### 2.5 Constrained forms of rollout (pp. 232–242)
**Setting and the unconstrained outline (pp. 232–233).** The claim is: if the base heuristic gives a feasible solution, rollout gives a feasible solution that costs no more, under suitable assumptions. The unconstrained deterministic rollout:
- (a) builds complete trajectories $T_0,\dots,T_N$ of nonincreasing cost, assuming sequential improvement;
- (b) takes $T_0$ from the base heuristic and $T_N$ from rollout;
- (c) lets $T_k,\dots,T_N$ share their initial portion up to $\tilde x_k$;
- (d) generates candidates at each $k$, one per control $u_k\in U_k(x_k)$ (including the tentative best for fortified rollout);
- (e) takes the best candidate as $T_{k+1}$.

With a constraint $T\in C$, infeasible candidates are discarded and the best feasible one is chosen. To make sure one exists, sequential improvement is used. The fortified version (promised later) needs only a feasible $T_0$ (p. 233).

**Formulation (pp. 233–234).**
- States lie in a possibly infinite set. Controls lie in a finite set, needed only for implementation.
- A complete trajectory is $T=(x_0,u_0,\dots,u_{N-1},x_N)$ (2.37) with $x_{k+1}=f_k(x_k,u_k)$ (2.38).
- Problem: $\min_{T\in C}G(T)$ (2.39). $G$ need not be additive, i.e. of the form $g_N(x_N)+\sum_{k=0}^{N-1}g_k(x_k,u_k)$ (2.40).
- Examples of constraints: time-uncoupled $u_k\in U_k(x_k)$; coupled constraints $g^m_N(x_N)+\sum_{k=0}^{N-1}g^m_k(x_k,u_k)\le b^m$, $m=1,\dots,M$ (2.41), as in multiobjective/Pareto problems; discrete control components that stay fixed over several periods.
- Footnote (p. 234): explicit $G$ and $C$ are not needed. An oracle that tests feasibility and compares two feasible trajectories is enough.

**Example 2.5.1 (constrained TSP, p. 235, Fig. 2.5.1).** Find a minimum-cost tour whose safety cost is at most 10. The safety costs of the six tours are given in the figure's table, and the constraint need not be additive. The unconstrained minimum-cost tour ABDCA violates the constraint (safety cost 20 in the table); the optimal constrained tour is ABCDA.

**Mechanism (pp. 235–238, Fig. 2.5.2).**
- The base heuristic completes any partial trajectory $y_k=(x_0,u_0,\dots,u_{k-1},x_k)$ with $R(y_k)=(x_k,u_k,\dots,u_{N-1},x_N)$ (p. 235).
- For a control $u_k$, set $y_{k+1}=(y_k,u_k,f_k(x_k,u_k))$ and run the heuristic:
$$T_k(y_k,u_k)=\big(y_k,u_k,R(y_{k+1})\big)\tag{2.42}$$
$R(y_{k+1})$ depends on the whole $y_{k+1}$, not only on $x_{k+1}$ (p. 236).
- Controls keeping feasibility: $\hat U_k(y_k)=\{u_k\mid T_k(y_k,u_k)\in C\}$ (2.43). The page text and the algorithm box write this set as $U_k(\tilde y_k)$ (p. 237).
- Algorithm: $\tilde y_0=\tilde x_0$, $\tilde y_{k+1}=(\tilde y_k,\tilde u_k,f_k(\tilde x_k,\tilde u_k))$ (2.44), with
$$\tilde u_k\in\arg\min_{u_k\in\hat U_k(\tilde y_k)}G\big(T_k(\tilde y_k,u_k)\big)\tag{2.45, 2.47}$$
- The aim is a feasible final trajectory with $G(\tilde y_N)\le G(R(\tilde y_0))$. For now it is assumed that $\hat U_k(\tilde y_k)$ is nonempty; the weaker assumption $R(\tilde y_0)\in C$ comes later (pp. 237–238).
- The cost is not much above unconstrained rollout if feasibility checks are cheap. The method uses determinism and has no straightforward stochastic extension, since feasibility of a complete trajectory is typically hard to check there (p. 238).

**TSP illustration (p. 239, Fig. 2.5.3).** The base heuristic completes partial tours as follows. At A it gives ACDBA; at AB, ABCDA; at AC, ACBDA; at AD, ADCBA.
- At A, rollout considers AB, AC, AD, and obtains ABCDA, ACBDA, ADCBA.
- It discards ADCBA as infeasible and compares the other two. ABCDA is cheaper, so it selects AB.
- At AB it considers ABC and ABD, obtaining ABCDA and ABDCA. It discards ABDCA and selects ABCDA.

The result ABCDA is only barely cheaper than the heuristic's tour ACDBA from A. If the cost D→A were 25, the rollout tour would cost more than the base tour (p. 238). This motivates a constrained sequential-improvement notion and a fortified variant (p. 240).

**Sequential consistency and improvement (pp. 240–241).** The goal is conditions that make $\hat U_k$ nonempty and give
$$G(T_{k+1}(\tilde y_{k+1},\tilde u_{k+1}))\le G(T_k(\tilde y_k,\tilde u_k)),\qquad G(T_0(\tilde y_0,\tilde u_0))\le G(R(\tilde y_0)),$$
hence $G(\tilde y_N)\le G(R(\tilde y_0))$ (p. 240).

- **Definition 2.5.1.** The base heuristic is *sequentially consistent* if, whenever it generates $(x_k,u_k,x_{k+1},\dots,u_{N-1},x_N)$ from $y_k$, it generates $(x_{k+1},u_{k+1},\dots,u_{N-1},x_N)$ from $y_{k+1}=(y_k,u_k,x_{k+1})$ (p. 240).
  - Greedy heuristics tend to be sequentially consistent. So is any policy for the DP problem of minimizing $G(y_N)$ subject to $y_{k+1}=(y_k,u_k,f_k(x_k,u_k))$ and $y_N\in C$.
  - The TSP heuristic violates it: from A it generates ACDBA, but from AC it generates ACBDA (p. 241).
- **Definition 2.5.2.** The heuristic is *sequentially improving* if, for every $k$ and every $y_k$ with $y_k\cup R(y_k)\in C$, the set $\hat U_k(y_k)$ is nonempty and
$$G\big(y_k\cup R(y_k)\big)\ \ge\ \min_{u_k\in\hat U_k(y_k)}G\big(T_k(y_k,u_k)\big).\tag{2.48}$$
Here $y_k\cup R(y_k)$ is $y_k$ joined with the heuristic's completion (p. 241).
- Nonemptiness must be required explicitly. Without sequential consistency, $y_k\cup R(y_k)\in C$ does not imply it, because the heuristic from $y_{k+1}$ may differ from its path from $y_k$. The fortified version will drop this requirement (p. 241).
- Sequentially consistent implies sequentially improving: $y_k\cup R(y_k)$ is then one of the trajectories $T_k(y_k,u_k)$, $u_k\in\hat U_k(y_k)$ (p. 241).

**Proposition 2.5.1 (cost improvement for constrained rollout, p. 242).** Assume the base heuristic is sequentially improving and $R(\tilde y_0)\in C$. Then each $\hat U_k(\tilde y_k)$ is nonempty and
$$G(R(\tilde y_0))\ge G(T_0(\tilde y_0,\tilde u_0))\ge G(T_1(\tilde y_1,\tilde u_1))\ge\cdots\ge G(T_{N-1}(\tilde y_{N-1},\tilde u_{N-1}))=G(\tilde y_N),$$
with $T_k(\tilde y_k,\tilde u_k)=(\tilde y_k,\tilde u_k,R(\tilde y_{k+1}))$. So $\tilde y_N$ is feasible and costs no more than $R(\tilde y_0)$.

*Proof (as given).*
- $\tilde y_0\cup R(\tilde y_0)=R(\tilde y_0)\in C$. By (2.48), $\hat U_0(\tilde y_0)$ is nonempty and $G(R(\tilde y_0))\ge G(T_0(\tilde y_0,\tilde u_0))$, with $T_0(\tilde y_0,\tilde u_0)\in C$.
- Next stage: $\tilde y_1\cup R(\tilde y_1)=T_0(\tilde y_0,\tilde u_0)\in C$. So (2.48) gives $\hat U_1(\tilde y_1)\neq\emptyset$ and $G(T_0)\ge G(T_1(\tilde y_1,\tilde u_1))$, with $T_1\in C$.
- Repeat for every $k$.

*Intuition note.* Each stage starts from a feasible complete trajectory, the previous best. Sequential improvement then guarantees a feasible candidate at least as cheap. So feasibility is kept and cost never rises.

The unit ends mid-sentence, noting that examples exist where (2.48) fails and rollout costs more than the base heuristic (p. 242).

## Toy example (ours, not from the text)
Constrained rollout with $N=2$ and controls $u_0,u_1\in\{0,1\}$. The state plays no role; a trajectory is $(u_0,u_1)$.
- Costs: $G(0,0)=5$, $G(0,1)=3$, $G(1,0)=2$, $G(1,1)=4$. Constraint: $C=\{(0,0),(0,1),(1,1)\}$, so $(1,0)$ is infeasible.
- Base heuristic: from the empty $y_0$ it picks $u_0=0$ then $u_1=0$, giving $R(\tilde y_0)=(0,0)$, feasible, cost 5. After $u_0=0$ it continues with $u_1=0$. After $u_0=1$ it continues with $u_1=1$.
- *Sequential improvement check:*
  - at $y_0$: $5\ge\min(5,4)=4$;
  - at $y_1=(0)$: $\hat U=\{0,1\}$, costs 5 and 3, and $5\ge3$;
  - at $y_1=(1)$: the heuristic gives $(1,1)$ with cost 4, $\hat U=\{1\}$, and $4\ge4$.
- *Stage 0:* candidates are $T_0=(0,0)$ with cost 5 and $T_0=(1,1)$ with cost 4. Both are feasible. Pick $\tilde u_0=1$.
- *Stage 1:* from $\tilde y_1=(1)$, candidate $(1,0)$ is infeasible and is discarded. Candidate $(1,1)$ costs 4. Pick $\tilde u_1=1$.
- Chain: $G(R(\tilde y_0))=5\ge G(T_0)=4\ge G(T_1)=4=G(\tilde y_2)$. This matches Prop. 2.5.1.
- Rollout is not optimal here: the best feasible trajectory $(0,1)$ costs 3.

*Counting check for scheme (a) versus (b).* Take $m=3$ controls and $\ell=4$. Scheme (a) needs up to $3^4=81$ evaluations of $\tilde J$. Scheme (b) needs $m+m^2(\ell-1)=3+9\cdot3=30\le m^2\ell=36$.

## Concepts
- [[policy]] — here the greedy, rollout, and base policies over state sequences or controls (p. 216)
- [[rollout-algorithm]] (new) — one-step or multistep lookahead whose leaves are evaluated by running a base policy or heuristic (pp. 216, 221)
- [[truncated-rollout]] (new) — the base heuristic is run only m steps; a terminal cost approximation $\tilde J$ may be added (pp. 216, 222)
- [[double-rollout]] (new) — rollout with a rollout policy as base; two on-line policy iterations (p. 216)
- [[terminal-cost-approximation]] (new) — $\tilde J$ at the lookahead leaves; may be zero, from off-line training, or from a heuristic's cost (pp. 222–224)
- [[newton-step-interpretation]] (new) — lookahead with truncated rollout and $\tilde J$ as one Newton step for Bellman's equation, with fast convergence (pp. 216, 223)
- [[iterative-deepening]] (new) — solve the n-step lookahead for n=1,2,… via forward DP until the budget ends; an anytime method (pp. 227–228)
- [[incremental-multistep-rollout]] (new) — expand a subgraph guided by D(x)+H(x); δ is the exploration parameter (pp. 229–231)
- [[exploration-vs-exploitation]] — in IMR, larger δ tends to give more paths explored, at greater computational effort (p. 230)
- [[constrained-rollout]] (new) — rollout that discards candidate trajectories violating $T\in C$ (pp. 233, 237–238)
- [[sequential-consistency]] (new) — heuristic's continuation from $y_{k+1}$ equals the tail of its path from $y_k$ (p. 240)
- [[sequential-improvement]] (new) — Eq. (2.48); with $R(\tilde y_0)\in C$ it gives feasibility and cost improvement (pp. 241–242)

## Canonical instances
- [[sequence-selection-experiment]] — random Markov chains, percentage recovery of greedy's loss (pp. 219–221)
- [[constrained-tsp]] — TSP with a safety constraint; rollout with a non-consistent heuristic (pp. 235, 239)
- [[td-gammon]] — uses scheme (b), one-step minimization plus truncated rollout, out of necessity (p. 226)
- [[chess-iterative-deepening]] — anytime property known from chess programming (p. 228)

## Bridges (candidates)
- [structural-analogy] Rollout applies the first control and discards the rest of the ℓ-step plan ↔ control-theory: model predictive control (receding horizon) — both re-solve a finite lookahead each step.
- [structural-analogy] Rollout or lookahead with $\tilde J$ as one Newton step ↔ Newton's method for fixed-point equations — the page states the Newton-step view for Bellman's equation.
- [metaphor] Anytime iterative deepening ↔ control-theory: trading computation time against solution quality in on-line control.

## Questions this raises
- Why is performance so insensitive to cutting the rollout horizon to 10% of N? The text only reports this (p. 220).
- What exactly is the fortified version that works with only $R(\tilde y_0)\in C$, and what does it guarantee?
- How should δ be adapted in IMR, and when does an intermediate δ beat both pure rollout and forward DP?
- What replaces trajectory-feasibility checking for stochastic problems, given the author's remark that it is hard there?

## Reading notes
- Unit coverage: printed pp. 216–242 (pdf 236–262; printed = pdf − 20). It starts mid-sentence on p. 216, in the discussion of most-likely-sequence rollout of Sec. 2.3, and ends on p. 242 in the middle of the sentence after the proof of Prop. 2.5.1.
- Misprint, p. 218: the third line of the induction chain shows $p(\tilde\mu_k(x)\mid x)$ with $P_{k+1}(\bar\mu_k(x),\bar\pi)$. I corrected it to $p(\bar\mu_k(x)\mid x)$.
- Text-layer symbol problems: the text layer often loses overlines (so the greedy π̄ looks like π) and sometimes tildes, so π̄ and π̃ can be confused there. I followed the images. The ℓ in the text layer appears as "!" or a quotation mark, and the minus sign appears as "→".
- p. 226: "m-step lookahead graph" in the leaf-count sentence should be ℓ-step; the count $m^\ell$ is right. Also, $m$ means the truncation length earlier and the number of controls here.
- Set notation: Eq. (2.43) uses $\hat U_k$, while the text after it and the algorithm box write $U_k(\tilde y_k)$.
- p. 235 (Fig. 2.5.1): the figure caption says the constraint is "less or equal to 10", while the figure label shows "< 10". The text says ≤ 10. I did not compute tour costs, because the arc costs in the figure tree and in the matrix were hard to reconcile in the image.
- Experimental bar values (Figs. 2.3.15, 2.3.16) are read from the images. In Fig. 2.3.16 the first, blue bar (64.3) is single one-step rollout; the green bars are double rollout.
