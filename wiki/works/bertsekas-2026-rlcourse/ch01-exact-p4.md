---
id: bertsekas-2026-rlcourse/ch01-exact-p4
work: bertsekas-2026-rlcourse
unit: "1 Exact and Approximate Dynamic Programming (part 4/6): end of the preceding section, and Sec. 1.6 (Examples, Reformulations, and Simplifications) through the opening of 1.6.8"
pages: 79-108
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Examples, Reformulations, and Simplifications (Sec. 1.6)

## L0 — One line
There is no unique way to choose state and control variables, and many practical problems (delays, forecasts, partial information, many agents) can be recast into the standard DP form, and the recast form can often be simplified or approximated.

## L1 — The gist (≤ 120 words)
How can real problems be fitted to the DP framework, and how can the resulting algorithms be made cheaper? Bertsekas says a good state separates past from future. He then shows reformulations: termination states, discrete optimization as sequential decisions, finite-to-infinite horizon, state augmentation (delays, forecasts), removal of uncontrollable state components, belief states for partial information, and one-agent-at-a-time control for multiagent rollout. Each keeps the DP algorithm valid or reduces its cost, often at the price of a larger or more awkward state. The unit ends by raising unknown or changing models.

**Prerequisites:** finite-horizon stochastic DP and the Bellman equation; policy, cost-to-go and Q-factor; rollout and approximation in value space; conditional expectation and Bayes' rule.

## L2 — Key ideas (5–10 bullets)
- The state $x_k$ should hold all information relevant to future decisions, i.e. separate past from future. Several valid state choices may exist, and it may be worth trying states of small dimension (p. 81).
- Any finite-horizon problem equals an infinite-horizon problem with a cost-free absorbing termination state. This gives a route to Newton-step insight (lookahead seen as one Newton step for the Bellman equation) for finite-horizon rollout (pp. 83, 89–91).
- Discrete optimization becomes a DP problem by choosing solution components one at a time. Exact DP often becomes intractable because the number of states grows exponentially, which motivates rollout (pp. 85–87).
- State augmentation handles delays, correlated disturbances and forecasts, but may give a very complex state space (pp. 91–94).
- An uncontrollable state component can be "averaged out", so DP runs on the controllable part only (parking, tetris) (pp. 85, 94–97).
- Partial state information reduces to perfect information with a sufficient statistic, i.e. a summary of the available information. Two choices are the belief state (the probability distribution of the state given all past observations and controls) or the information vector (the list of all past observations and controls) (pp. 98–101).
- Multiagent rollout replaces $O(n^m)$ Q-factor computations by $O(nm)$ by unfolding the joint control, and, the author states, it keeps cost improvement (proved elsewhere) (pp. 102–105).
- RL methods have limited guarantees. The right method depends on whether the problem is single and stable or variable (pp. 82–83).

## L3 — Walkthrough

### Top of p. 79 (end of the preceding section)
The text continues a list of error sources in approximation in value space. Items (a) and (b) are presumably on the previous page, which is not in this part. Item (c) is the extra error from imperfect training. If the architecture cannot bring $\tilde J-J^*$ inside the region of convergence of Newton's method, one-step lookahead will likely fail, however much data and however good the training (p. 79).

Two remedies (p. 79):
1. A more powerful architecture (typically a deep network or transformer, with more weights and costlier training).
2. A longer combined lookahead minimization and truncated rollout. This needs longer on-line computation, which may violate real-time limits.

Parallel computation and multistep lookahead methods (Chapter 2) may help (p. 79).

> **Intuition note.** Lookahead acts like a Newton step. A Newton step is reliable only when the starting guess lies within its region of convergence. If $\tilde J-J^*$ is outside it, one-step lookahead will likely fail. The text suggests two remedies: a more powerful architecture for $\tilde J$, or a longer lookahead/truncated rollout.

### 1.6.1 A few words about modeling (pp. 79–83)
**When DP fits.** A problem is a prime candidate if it has multiple sequential decisions separated by feedback (observations that improve later decisions) (p. 80). Deterministic problems also fit, though many non-DP methods exist for them. The book still treats rollout for deterministic optimization, and the DP sequential structure is often introduced artificially to enable approximate DP/RL (p. 80). Policy gradient and policy search fit the sequential structure but use non-DP methods. The policy is parametrized and its cost optimized by gradient or random search (p. 80).

**Practical guide, two stages** (pp. 80–81):
- (a) Identify the controls $u_k$ and the times they are applied. In deterministic problems controls may be lumped, e.g. $(u_0,u_1)$ as one choice. This is usually not possible in stochastic problems, because decisions differ by the information available (p. 80).
- (b) Select states $x_k$. The state should hold all information known at $k$ that can be used with advantage in choosing $u_k$. It should separate past from future: past states, controls and disturbances are irrelevant once $x_k$ is known. This is called a "Markov property", by analogy with Markov chains (p. 81).

State choice is not unique. If $x_k$ qualifies as state, so does $(x_{k-1},x_k)$, but it gains nothing in optimal cost and enlarges the space DP must work over. So try to minimize the dimension of the state (p. 81).

**Sufficient statistic.** A quantity summarizing all essential content of the information available to the controller (p. 81). With partial state information (e.g. measuring only position, not velocity), let $I_k$ be all measurements and controls up to $k$ (the information vector). Using $I_k$ as state gives a perfect-information problem. A better alternative may be the belief state $P_k(x_k\mid I_k)$, which subsumes all useful information. But it is infinite-dimensional while $I_k$ may be finite-dimensional, so the best choice depends on the problem. In either case the stochastic DP algorithm applies with the sufficient statistic as state (pp. 81–82).

**Choice of RL method.** RL can address a very broad range of problems, but theoretical guarantees are limited. Several successful methods have less than solid performance properties. No method is guaranteed for all or even most DP problems, yet enough methods exist to give a reasonable chance after tuning, so insight into inner workings matters (p. 82). Context matters: a single problem (like chess) or a family of problems, and fixed or changing data. Convenient but less reliable, tunable methods (including policy-space approximation and neural networks) may suit a single problem in a stable environment. They are not well suited to variable environments or real-time parameter changes. There, approximation in value space with on-line play, possibly with on-line replanning, is much better suited (pp. 82–83).

On-line play may improve off-line trained policies even without replanning, because of the implicit Newton step in lookahead. Deterministic problems are better suited than stochastic ones for on-line play. Methods that parallelize well, and/or use certainty equivalence approximations, are generally better suited for a stochastic environment (p. 83).

### 1.6.2 Problems with a termination state (pp. 83–85)
A termination state $t$ is cost-free and absorbing: for all $k$,
$$g_k(t,u_k,w_k)=0,\qquad f_k(t,u_k,w_k)=t,\qquad \text{for all } w_k \text{ and } u_k\in U_k(t).$$
Games (chess, Go, backgammon) have one: the end of the game (p. 83). If an optimal policy is known to reach $t$ within at most $N$ stages, formulate an $N$-stage problem with a very large termination cost at non-termination states. Reaching $t$ early, one stays there at no cost, so the optimal policy never pays the large cost (p. 83). If no such bound is known, the footnote says the problem may be formulated as an infinite-horizon stochastic shortest path problem (p. 83).

**Example 1.6.1 (Parking)** (p. 84). A driver passes spaces $0,\dots,N-1$, then a garage costing $C$. Space $k$ costs $c(k)$ and is free with probability $p(k)$, independently across spaces. Free status is seen only on arrival, and then he parks or continues. States at each stage: $F$ (free), $\overline F$ (taken), $t$ (parked). The only decision is at $F$.

DP algorithm for $k=0,\dots,N-1$ (pp. 84–85):
$$J_k^*(F)=\begin{cases}\min\big[c(k),\;p(k+1)J^*_{k+1}(F)+(1-p(k+1))J^*_{k+1}(\overline F)\big] & k<N-1\\ \min[c(N-1),C] & k=N-1\end{cases}$$
$$J_k^*(\overline F)=\begin{cases}p(k+1)J^*_{k+1}(F)+(1-p(k+1))J^*_{k+1}(\overline F) & k<N-1\\ C & k=N-1\end{cases}$$
and $J_k^*(t)=0$ for $k=1,\dots,N$. The min is the choice park / not park at free spaces (p. 85).

Simplification. Define the cost-to-go on arrival at $k$ before seeing its status:
$$\hat J_k=p(k)J_k^*(F)+(1-p(k))J_k^*(\overline F),\qquad k=0,\dots,N-1.$$
Then
$$\hat J_{N-1}=p(N-1)\min[c(N-1),C]+(1-p(N-1))C,$$
$$\hat J_k=p(k)\min[c(k),\hat J_{k+1}]+(1-p(k))\hat J_{k+1},\quad k=0,\dots,N-2.$$
Optimal policy: park at space $k$ if it is free and $c(k)\le\hat J_{k+1}$ (p. 85). This is an instance of simplification when the state has components not affected by the control (p. 85).

> **Intuition note.** Whether a space is free is not chosen by the driver. So average over it first, and the recursion needs one number per space instead of two.

### 1.6.3 General discrete optimization problems (pp. 85–87)
Problem (1.61): $\min G(u)$ subject to $u\in U$, with $U$ finite and $u=(u_0,\dots,u_{N-1})$ (pp. 85–86). Exact DP often explodes exponentially in the number of states, but the reformulation allows rollout and other approximate DP (p. 85).

Formulation (Fig. 1.6.2, p. 86):
- A $k$-solution is a $k$-tuple $(u_0,\dots,u_{k-1})$. At stage $k=1,\dots,N$ the states are the $k$-solutions.
- The initial state is an artificial state $s$.
- Control sets:
$$U_0=\{\tilde u_0\mid \text{there exists a solution } (\tilde u_0,\tilde u_1,\dots,\tilde u_{N-1})\in U\},\tag{1.62}$$
$$U_k(u_0,\dots,u_{k-1})=\{u_k\mid \text{for some }\bar u_{k+1},\dots,\bar u_{N-1}:(u_0,\dots,u_{k-1},u_k,\bar u_{k+1},\dots,\bar u_{N-1})\in U\}.\tag{1.63}$$
These are the feasible-consistent choices. The set (1.63) may be empty (p. 87).
- Only cost: $G(u)$ at the last transition. All other transitions cost 0 (p. 87).

DP algorithm (p. 87), with $J_k^*(u_0,\dots,u_{k-1})$ the optimal cost over solutions whose first $k$ components are fixed:
$$J_k^*(u_0,\dots,u_{k-1})=\min_{u_k\in U_k(u_0,\dots,u_{k-1})}J^*_{k+1}(u_0,\dots,u_{k-1},u_k),\qquad J_N^*(u_0,\dots,u_{N-1})=G(u_0,\dots,u_{N-1}).$$
It runs backwards from $J_N^*=G$ to $J_0^*$. An optimal solution is built forward:
$$u_k^*\in\arg\min_{u_k\in U_k(u_0^*,\dots,u^*_{k-1})}J^*_{k+1}(u_0^*,\dots,u^*_{k-1},u_k),\quad k=0,\dots,N-1.\tag{1.64}$$

Approximation: the number of states typically grows exponentially in $N$. Replace $J^*_{k+1}$ in (1.64) by a suboptimal $\tilde J_{k+1}$. One choice is the cost of a heuristic that solves the problem suboptimally with the first $k+1$ components fixed at $u_0^*,\dots,u^*_{k-1},u_k$. This is the rollout algorithm (p. 87). If $G$ and/or $U$ have additive structure (as in the traveling salesman, Example 1.2.2) it may be exploited (p. 87).

**Example 1.6.2 (LLM based on $N$-grams)** (pp. 88–89). State $x_k$ is a string of $N$ words. Control $u_k\in U(x_k)$ is the word added at the front, while the word at the back is deleted:
$$x_{k+1}=f(x_k,u_k).$$
The initial string $x_0$ is given and may contain a "prompt", which may itself be optimized ("prompt engineering"). With a cost $G$ on text strings:
- Finite horizon: after exactly $N$ steps, minimize $G(x_N)$.
- Termination action: stop optionally and pay $G(x)$, possibly plus an additive stage cost depending on $u$. This is an infinite-horizon formulation with a termination state, as in 1.6.2.

A GPT is viewed as a policy generating next words, either deterministic $u_k=\mu(x_k)$ or randomized. Rollout could improve the GPT's output. A more ambitious option is a policy-iteration/self-training scheme in the spirit of AlphaZero/TD-Gammon: a sequence of GPTs, each trained on data from the previous one (pp. 88–89).

**Infinite-horizon form of (1.65)**, which is (1.61) again: introduce a termination state $t$ entered after $N$ steps, with $u_k\in U_k(u_0,\dots,u_{k-1})$ from (1.63). It is a special case of the reformulation in 1.6.4 (p. 89).

### 1.6.4 General finite to infinite horizon reformulation (pp. 89–91)
A finite-horizon problem, possibly nonstationary, can be turned into an equivalent infinite-horizon problem. For the $N$-stage problem of Sec. 1.3.1 with
$$x_{k+1}=f_k(x_k,u_k,w_k),\quad k=0,\dots,N-1,\tag{1.66}$$
define the expanded spaces (Fig. 1.6.4)
$$X=\Big(\cup_{k=0}^N X_k\Big)\cup\{t\},\qquad U=\cup_{k=0}^{N-1}U_k.\tag{1.67}$$
States in $X_k$ ($k<N$) move to $X_{k+1}$ per (1.66). States $x_N\in X_N$ move to $t$ at cost $g_N(x_N)$, and $t$ is absorbing and cost-free (p. 90).

Consequences (pp. 90–91):
- Policies of the new problem are the finite-horizon policies $\mu_k(x_k)$.
- The Bellman equation of the infinite-horizon problem is identical to the finite-horizon DP algorithm.
- $J^*(x_k)$ and $\mu^*(x_k)$ for $x_k\in X_k$ equal $J_k^*(x_k)$ and $\mu_k^*(x_k)$.
- Approximation in value space and rollout have infinite-horizon counterparts and can be understood as Newton steps for the Bellman equation (equivalently, the finite-horizon DP algorithm).
- PI for the infinite-horizon problem translates to a PI algorithm for the finite-horizon problem. The Newton-step explanation of rollout's cost improvement carries over (p. 91).

> **Intuition note.** The finite horizon is hidden inside the state, because the stage index is part of which set $X_k$ you are in. So infinite-horizon tools (Newton step, PI) apply to finite-horizon problems too.

### 1.6.5 State augmentation, time delays, forecasts, uncontrollable components (pp. 91–97)
When assumptions are violated (correlated disturbances, delayed control effects), enlarge the state with all information known at $k$ that can help choose $u_k$. The price may be a very complex state space (p. 91).

**Time delays.** With at most one stage of delay (p. 92):
$$x_{k+1}=f_k(x_k,x_{k-1},u_k,u_{k-1},w_k),\ k=1,\dots,N-1,\qquad x_1=f_0(x_0,u_0,w_0).\tag{1.68}$$
Let $y_k=x_{k-1}$, $z_k=u_{k-1}$ (the text says "$y_k$ and $s_k$", a typo for $z_k$; see Reading notes):
$$\begin{pmatrix}x_{k+1}\\y_{k+1}\\z_{k+1}\end{pmatrix}=\begin{pmatrix}f_k(x_k,y_k,u_k,z_k,w_k)\\x_k\\u_k\end{pmatrix}.\tag{1.69}$$
With $\tilde x_k=(x_k,y_k,z_k)$ this is $\tilde x_{k+1}=\tilde f_k(\tilde x_k,u_k,w_k)$. Policies then depend on $x_k$, $x_{k-1}$ and $u_{k-1}$ (p. 92). The DP algorithm in original variables (p. 92):
$$J_N^*(x_N)=g_N(x_N),$$
$$J^*_{N-1}(x_{N-1},x_{N-2},u_{N-2})=\min_{u_{N-1}\in U_{N-1}(x_{N-1})}E_{w_{N-1}}\Big\{g_{N-1}(x_{N-1},u_{N-1},w_{N-1})+J_N^*\big(f_{N-1}(x_{N-1},x_{N-2},u_{N-1},u_{N-2},w_{N-1})\big)\Big\},$$
$$J_k^*(x_k,x_{k-1},u_{k-1})=\min_{u_k\in U_k(x_k)}E_{w_k}\Big\{g_k(x_k,u_k,w_k)+J^*_{k+1}\big(f_k(x_k,x_{k-1},u_k,u_{k-1},w_k),x_k,u_k\big)\Big\},\ k=1,\dots,N-2,$$
$$J_0^*(x_0)=\min_{u_0\in U_0(x_0)}E_{w_0}\Big\{g_0(x_0,u_0,w_0)+J_1^*\big(f_0(x_0,u_0,w_0),x_0,u_0\big)\Big\}.$$
Delays in the cost or constraints work similarly, e.g. cost $E\{g_N(x_N,x_{N-1})+g_0(x_0,u_0,w_0)+\sum_{k=1}^{N-1}g_k(x_k,x_{k-1},u_k,w_k)\}$ (p. 92). The extreme nonadditive case is $E\{g_N(x_N,x_{N-1},\dots,x_0,u_{N-1},\dots,u_0,w_{N-1},\dots,w_0)\}$. Use the augmented state $\tilde x_k=(x_k,\dots,x_0,u_{k-1},\dots,u_0,w_{k-1},\dots,w_0)$ and cost $E\{g_N(\tilde x_N)\}$. This requires past disturbances to be known to the controller. Otherwise the state is imprecisely known (next section) (p. 93).

**Forecasts.** At each stage the controller receives an accurate forecast $y_k\in\{1,\dots,m\}$: if $y_k=i$, then $w_k\sim P_i$. The prior probability of forecast $i$ is $p_i$. Model: $y_{k+1}=\xi_k$, where $\xi_k$ takes value $i$ with probability $p_i$. The augmented system is $(x_{k+1},y_{k+1})=(f_k(x_k,u_k,w_k),\xi_k)$, with $\tilde x_k=(x_k,y_k)$ and $\tilde w_k=(w_k,\xi_k)$. The distribution of $\tilde w_k$ depends on $\tilde x_k$ (via $y_k$) but not on prior disturbances (pp. 93–94). DP algorithm (p. 94):
$$J_N^*(x_N,y_N)=g_N(x_N),$$
$$J_k^*(x_k,y_k)=\min_{u_k\in U_k(x_k)}E_{w_k}\Big\{g_k(x_k,u_k,w_k)+\sum_{i=1}^m p_iJ^*_{k+1}\big(f_k(x_k,u_k,w_k),i\big)\,\Big|\,y_k\Big\},\tag{1.70}$$
where the expectation over $w_k$ uses $P_{y_k}$. The control depends on both current state and current forecast. Extensions (forecasts influenced by the control, e.g. paying for a more accurate one; several future disturbances) raise the complexity of the DP algorithm (p. 94).

**Uncontrollable state components.** Let the state be $(x_k,y_k)$ with $x_{k+1}=f_k(x_k,y_k,u_k,w_k)$ and $w_k\sim P_k(\cdot\mid x_k,y_k,u_k)$. The component $y_k$ follows $P_k(y_k\mid x_k)$ and is not affected by the control, except through $x_k$. It differs from a disturbance because $y_k$ is observed before $u_k$ is applied, while $w_k$ occurs after $u_k$ and may depend on it (p. 94). Define the average cost-to-go
$$\hat J_k(x_k)=E_{y_k}\{J_k^*(x_k,y_k)\mid x_k\}.$$
Then
$$\hat J_k(x_k)=E_{y_k}\Big\{\min_{u_k\in U_k(x_k,y_k)}E_{w_k}\Big\{g_k(x_k,y_k,u_k,w_k)+\hat J_{k+1}\big(f_k(x_k,y_k,u_k,w_k)\big)\,\Big|\,x_k,y_k,u_k\Big\}\,\Big|\,x_k\Big\}.\tag{1.71}$$
Derivation (p. 95):
$$\hat J_k(x_k)=E_{y_k}\{J_k^*(x_k,y_k)\mid x_k\}$$
$$=E_{y_k}\Big\{\min_{u_k}E_{w_k,x_{k+1},y_{k+1}}\{g_k(x_k,y_k,u_k,w_k)+J^*_{k+1}(x_{k+1},y_{k+1})\mid x_k,y_k,u_k\}\mid x_k\Big\}$$
$$=E_{y_k}\Big\{\min_{u_k}E_{w_k,x_{k+1}}\big\{g_k+E_{y_{k+1}}\{J^*_{k+1}(x_{k+1},y_{k+1})\mid x_{k+1}\}\mid x_k,y_k,u_k\big\}\mid x_k\Big\}.$$
(added step) The inner expectation equals $\hat J_{k+1}(x_{k+1})$ by definition, which gives (1.71).

The minimization must still be done for every full state $(x_k,y_k)$ to get a control law in $(x_k,y_k)$, but DP runs over a much smaller space. For approximation in value space it is often more convenient to approximate $\hat J_k(x_k)$ than $J_k^*(x_k,y_k)$ (p. 95).

Forecast case: $\hat J_k(x_k)=\sum_{i=1}^m p_iJ_k^*(x_k,i)$, $\hat J_N=g_N$, and using (1.70) (p. 96)
$$\hat J_k(x_k)=\sum_{i=1}^m p_i\min_{u_k\in U_k(x_k)}E_{w_k}\Big\{g_k(x_k,u_k,w_k)+\hat J_{k+1}\big(f_k(x_k,u_k,w_k)\big)\,\Big|\,y_k=i\Big\}.$$
Uncontrollable components often occur in arrival systems such as queueing, where the state is augmented with the random event (p. 96).

> **Intuition note.** An uncontrolled variable that you see before you act still must be part of the state for choosing the action. But when you evaluate "how good is $x$", you may average it away. This makes the function you must approximate a function of fewer variables.

**Example 1.6.3 (Tetris)** (pp. 96–97). Finite horizon, very long. State $(x,y)$: $x$ is the binary full/empty board, $y$ is the current falling block shape. Control $u$ is horizontal position and rotation. There is a cost-free termination state. A very large amount is added to the score if the horizon ends without game termination. Shape $y$ is generated by $p(y)$ independently of the control, so it is an uncontrollable component. With $g(x,y,u)$ the points scored (rows removed) and $f(x,y,u)$ the next board (or termination state), the algorithm over boards is
$$\hat J_k(x)=\sum_y p(y)\max_u\Big[g(x,y,u)+\hat J_{k+1}\big(f(x,y,u)\big)\Big]\quad\text{for all }x.\tag{1.72}$$
The undiscounted infinite-horizon (stochastic shortest path) reduced Bellman equation is $\hat J(x)=\sum_yp(y)\max_u[g(x,y,u)+\hat J(f(x,y,u))]$, where $\hat J(x)$ is the "average score" at $x$. The number of boards is still enormous, so only suboptimal methods apply (p. 97). The footnote reports that works over 1995–2015 used approximation in value space and approximate PI (p. 97).

### 1.6.6 Partial state information and belief states (pp. 98–101)
The controller may see only some components of the state, or noisy ones (e.g. noisy radar on the position part of a position/velocity state). These are partial information problems, called POMDP (p. 98). Exact solution is typically intractable, so in practice POMDPs are solved approximately except in very special cases (p. 98). Conceptually they are not different. They reduce to perfect-information problems whose state is a sufficient statistic, roughly a summary of the information available up to $k$ for optimal control (p. 98).

**Belief state.** $b_k$ is the distribution of $x_k$ given all observations and controls up to $k$. It can in principle be updated by Bayes-rule-based methods such as Kalman filtering and particle filtering (p. 98).

**Example 1.6.4 (Bidirectional parking)** (p. 99). As in Example 1.6.1, but at space $i$ the driver may park (cost $c(i)$, if free), move to $i-1$ at cost $t_i^-$, or move to $i+1$ at cost $t_i^+$. He remembers statuses seen and may return. Each probability $p(i)$ of being free changes over time by a mechanism known to the driver, e.g. $p(i)$ rises by a known factor with probability $\xi$ and falls by another known factor with probability $1-\xi$. The belief state is the vector $(p(0),\dots,p(N-1))$, updated by a simple algorithm from the newly observed free/taken status.

**DP on belief states** (pp. 99–101):
$$J_k^*(b_k)=\min_{u_k\in U_k}\Big[\hat g_k(b_k,u_k)+E_{z_{k+1}}\big\{J^*_{k+1}\big(F_k(b_k,u_k,z_{k+1})\big)\mid b_k,u_k\big\}\Big].\tag{1.73}$$
- $U_k$ must not depend on $x_k$, since $x_k$ is unknown.
- $\hat g_k(b_k,u_k)$ is the expected stage cost of $g_k(x_k,u_k,w_k)$, with $(x_k,w_k)$ jointly distributed according to $b_k$ and the law of $w_k$.
- The belief system equation, with $z_{k+1}$ the observation acting as the "disturbance":
$$b_{k+1}=F_k(b_k,u_k,z_{k+1}).\tag{1.74}$$
$F_k$ is a sequential belief estimator, given by a formula or an algorithm (Kalman or particle filtering) based on Bayes' rule (p. 100).
- The distribution of $z_{k+1}$ depends on $x_k$ and $u_k$, and the expectation in (1.73) is a function of $b_k,u_k$ (p. 100).

(1.73) is the ordinary DP algorithm for the perfect-information problem of Fig. 1.6.7. Since $b_k$ lives in a continuous space, it typically needs approximation in value space (p. 101).

**Alternative: information vectors.** $I_k=\{z_0,u_0,\dots,z_{k-1},u_{k-1},z_k\}$ is also a sufficient statistic, evolving as $I_{k+1}=(I_k,z_{k+1},u_k)$ (p. 101). The DP algorithm is
$$J_k^*(I_k)=\min_{u_k\in U_k(x_k)}E_{w_k,z_{k+1}}\Big\{g_k(x_k,u_k,w_k)+J^*_{k+1}(I_k,z_{k+1},u_k)\mid I_k,u_k\Big\},\tag{1.75}$$
for $k=0,\dots,N-1$, with $J_N^*(I_N)=E\{g_N(x_N)\mid I_N\}$ (p. 101). Drawback: $I_k$ grows with time, so the system is nonstationary even for a stationary infinite-horizon problem. Remedy: use a finite history (a fixed number of most recent observations) as state, giving a stationary finite-state system. The author states this approach is used in large language models such as ChatGPT and DeepSeek (p. 101). It can be seen as feature-based approximation (Chapter 3, Example 3.1.6) and generalized to finite-state controllers; a cited paper (Yu and Bertsekas) also addresses convergence of the approximation error to zero as the memory size increases (pp. 101–102).

> **Intuition note.** If you cannot see the state, replace it by what you know about it: either everything you saw (grows forever) or a probability distribution (continuous). Both turn the problem into one with perfect information, but on a harder space.

### 1.6.7 Multiagent problems and multiagent rollout (pp. 102–107)
Agents are decision makers pursuing a common goal by exchanging information (p. 102). Challenges include limited communication and no full information sharing. Another is that the set of joint decisions grows exponentially with the number of agents. This section addresses the latter for fully shared information; Sec. 2.9 treats more autonomous agents (p. 102).

Setup: discounted infinite horizon, control $u=(u^1,\dots,u^m)$, with $u^\ell\in U^\ell(x)$, so
$$U(x)=U^1(x)\times\cdots\times U^m(x),\tag{1.76}$$
each $U^\ell(x)$ finite (p. 102). Standard rollout with base policy $\mu$:
$$\tilde u\in\arg\min_{u\in U(x)}E_w\{g(x,u,w)+\alpha J_\mu(f(x,u,w))\}.\tag{1.77}$$
It needs up to $n^m$ Q-factors, where $n$ is the maximum size of the sets $U^\ell(x)$. So the cost is $O(n^m)$ per stage, overwhelming even for moderate $m$ (p. 103).

**Multiagent rollout.** Given $\mu=(\mu^1,\dots,\mu^m)$, perform $m$ successive one-agent-at-a-time minimizations at $x$ (p. 103):
$$\tilde\mu^1(x)\in\arg\min_{u^1\in U^1(x)}E_w\{g(x,u^1,\mu^2(x),\dots,\mu^m(x),w)+\alpha J_\mu(f(x,u^1,\mu^2(x),\dots,\mu^m(x),w))\},$$
$$\tilde\mu^2(x)\in\arg\min_{u^2\in U^2(x)}E_w\{g(x,\tilde\mu^1(x),u^2,\mu^3(x),\dots,\mu^m(x),w)+\alpha J_\mu(f(x,\tilde\mu^1(x),u^2,\mu^3(x),\dots,w))\},$$
and so on, up to
$$\tilde\mu^m(x)\in\arg\min_{u^m\in U^m(x)}E_w\{g(x,\tilde\mu^1(x),\dots,\tilde\mu^{m-1}(x),u^m,w)+\alpha J_\mu(f(x,\tilde\mu^1(x),\dots,\tilde\mu^{m-1}(x),u^m,w))\}.$$
Each $u^\ell$ is chosen with earlier components fixed at the rollout values and later components fixed at the base-policy values. This needs $O(nm)$ Q-factors per stage instead of $O(n^m)$ (p. 104).

**Unfolding the control.** The cost of the minimization (1.77) is proportional to the number of controls and independent of the size of the state space. So control-space complexity can be traded for state-space complexity (idea attributed to the neuro-dynamic programming book [BeT96]) (p. 104). Reformulation (Fig. 1.6.9, p. 105): between $x$ and $\bar x=f(x,u,w)$ insert artificial intermediate "states" $(x,u^1),(x,u^1,u^2),\dots,(x,u^1,\dots,u^{m-1})$. Choosing $u^m$ at the last one causes the transition to $\bar x$ and the cost $g(x,u,w)$ (p. 104). The two problems are equivalent. Every policy of the original problem, including a base policy, is admissible in the reformulated problem with the same cost (p. 104). There are $m-1$ extra layers with cost-to-go functions $J^1(x,u^1),\dots,J^{m-1}(x,u^1,\dots,u^{m-1})$. The larger state space does not hurt rollout because the Q-factor minimization is done at one state per stage (p. 104).

**Cost improvement.** The author states that it can be proved (Sec. 2.9 and references; not proved here) that multiagent rollout satisfies
$$J_{\tilde\mu}(x)\le J_\mu(x)\quad\text{for all }x,$$
and that this extends to multiagent PI schemes with one-agent-at-a-time policy improvement, with sound convergence properties. It also leads to PI schemes suited to distributed operation by autonomous decision makers (p. 105).

**Example 1.6.5 (Spiders and flies)** (pp. 105–107). $m$ spiders and several flies on a 2-D grid. Flies move randomly with a state-dependent distribution. Each spider sees the state, then moves to a neighbour or stays (up to 5 choices), so there are about $5^m$ joint controls. Fig. 1.6.10 has 20 spiders and 5 flies, with a little less than $5^{20}$ joint moves. Base policy: each spider moves along a minimum-distance path to the closest fly. In multiagent rollout, spider 1 picks its best of at most 5 moves. This assumes the others follow the base policy now and all spiders follow it afterwards, until no flies remain. It broadcasts its move, then spider 2 chooses given spider 1's move, and so on (p. 106). Standard rollout compares $5^m$ Q-factors (slightly fewer at edges). Multiagent rollout compares at most 5 per spider, fewer than $5m$ in total. Experiments reportedly show comparable performance to standard rollout (pp. 106–107).

### 1.6.8 Problems with unknown or changing model — adaptive control (start; pp. 107–108)
This part of the unit covers only the opening. Earlier discussion assumed a known model, given by formulas or by software (a simulator, a trained neural network). It makes no difference for the methods whether the model is closed-form or computer-based; only suitability may differ (p. 107).

Parameters may be unknown or change, causing large complications. Example, the oversimplified cruise control (Example 1.3.1):
$$x_{k+1}=x_k+bu_k+w_k,\tag{1.78}$$
with $x_k=v_k-\bar v$ the deviation from nominal velocity, $u_k$ the propelling force, $w_k$ the disturbance. The coefficient $b$ and the law of $w_k$ change frequently (road slope, car weight), and $\bar v$ is set by the driver and may affect $b$ (pp. 107–108). Footnote: changing parameters may be far more challenging than chess, whose rules do not change mid-game (p. 107).

Points made (p. 108):
- RL is viewed in AI as learning from interaction with the environment (Sutton–Barto), connected to exploring the environment. In control this is system identification. Combined with control it is sometimes called dual control, studied intensively since the early 1960s.
- Neural network/AI advances expand system identification. Sec. 2.3.8 discusses world models, which predict trajectories beyond the first lookahead step.
- Robust controller design: ignore parameter changes and check performance over a range of parameter values. For (1.78) with linear controller $\mu(x)=Lx$ ($L$ scalar), the controller is stable for $b$ with $|1+bL|<1$, and one ensures $b$ stays in that range.
- The broader class where the controller is modified in response to parameter changes starts at the end of this part (the text breaks off here).

## Toy example (ours, not from the text)
Parking with $N=2$ spaces (0 and 1), garage cost $C=10$, $c(0)=2$, $c(1)=4$, $p(0)=p(1)=0.5$.

Reduced recursion (p. 85):
- $\hat J_1=p(1)\min[c(1),C]+(1-p(1))C=0.5\cdot\min(4,10)+0.5\cdot10=2+5=7$.
- $\hat J_0=p(0)\min[c(0),\hat J_1]+(1-p(0))\hat J_1=0.5\cdot\min(2,7)+0.5\cdot7=1+3.5=4.5$.

Policy: at space 0, park if free because $c(0)=2\le\hat J_1=7$. At space 1, park if free because $c(1)=4\le C=10$.

Check with the full two-state algorithm:
- $J_1^*(F)=\min(4,10)=4$ and $J_1^*(\overline F)=10$, so $\hat J_1=0.5\cdot4+0.5\cdot10=7$ ✓.
- $J_0^*(F)=\min[2,\;0.5\cdot4+0.5\cdot10]=\min[2,7]=2$ and $J_0^*(\overline F)=7$, so $\hat J_0=0.5\cdot2+0.5\cdot7=4.5$ ✓.

If instead $c(0)=8>\hat J_1=7$, the driver would skip a free space 0. The reduced recursion tracks one number per space, yet gives the same threshold rule as the two-state version.

Counting for multiagent rollout: $m=3$ agents with $n=5$ choices each gives $5^3=125$ Q-factors for standard rollout, versus at most $3\cdot5=15$ for one-agent-at-a-time (counts per pp. 103–104).

## Concepts
- [[state]] — here: information known to the controller at $k$ that can help choose $u_k$; it separates past from future ("Markov property") (p. 81)
- [[sufficient-statistic]] (new) — quantity summarizing all essential content of the available information for control; $I_k$ or $b_k$ (p. 81)
- [[belief-state]] (new) — $b_k$, the distribution of $x_k$ given all observations and controls up to $k$; serves as state in an exact DP (pp. 81, 98)
- [[pomdp]] (new) — partially observed Markovian decision problem; solving exactly is typically intractable (p. 98)
- [[state-augmentation]] (new) — enlarging the state to include past states and controls, forecasts and the like, to fit the standard format (p. 91)
- [[termination-state]] (new) — cost-free absorbing state $t$ (p. 83)
- [[uncontrollable-state-component]] (new) — a state part not affected by control (except via $x_k$) and observed before $u_k$. DP can be run on its average (p. 94)
- [[bellman-equation]] — here: for the infinite-horizon form of a finite-horizon problem it coincides with the finite-horizon DP algorithm (p. 90)
- [[policy]] — here also a GPT viewed as a policy generating next words (p. 88)
- [[rollout]] (new) — one-step lookahead using a base policy's cost as $\tilde J$ (pp. 87, 102)
- [[multiagent-rollout]] (new) — one-agent-at-a-time lookahead giving $O(nm)$ instead of $O(n^m)$ Q-factors (pp. 103–104)
- [[approximation-in-value-space]] (new) — replacing $J^*_{k+1}$ by some $\tilde J_{k+1}$ in the minimization (p. 87)
- [[newton-step-view]] (new) — lookahead as a Newton step for the Bellman equation; it may fail if $\tilde J$ is outside the region of convergence (pp. 79, 91)
- [[kalman-filter]] — named as one belief-estimator algorithm based on Bayes' rule (p. 98)
- [[robustness]] — here: robust controller design checks one fixed controller over a parameter range (e.g. $|1+bL|<1$) (p. 108)
- [[system-identification-dual-control]] (new) — building models of unknown systems, combined with control (p. 108)

## Canonical instances
- [[parking-problem]] — optional stopping with an uncontrollable component, reduced to $\hat J_k$ (p. 84)
- [[bidirectional-parking]] — belief-state DP with time-varying free probabilities (p. 99)
- [[tetris]] — stochastic DP over boards, with the block shape averaged out (pp. 96–97)
- [[llm-ngram-dp]] — text strings as states, words as controls, a GPT as a policy (p. 88)
- [[spiders-and-flies]] — multiagent rollout with $5^m$ joint moves (p. 105)
- [[cruise-control-1.78]] — scalar system with unknown/changing $b$ (p. 107)
- [[discrete-optimization-as-dp]] — $k$-solutions as states (p. 86)

## Bridges (candidates)
- [structural-analogy] Belief state $b_k$ with update $F_k$ ↔ control-theory state estimation: Kalman filter output used as the state of a perfect-information problem (the text names Kalman filtering as one choice of $F_k$).
- [structural-analogy] State augmentation with $x_{k-1},u_{k-1}$ ↔ state-space modeling: higher-order recursions rewritten as first-order systems.
- [same-math] Stability range $|1+bL|<1$ for $x_{k+1}=x_k+bu_k+w_k$, $u=Lx$ ↔ discrete-time linear stability: eigenvalue $1+bL$ inside the unit circle.
- [structural-analogy] Finite-history state for POMDP ↔ sequence models: the author states that this is how LLMs such as ChatGPT work.
- [metaphor] Averaging out uncontrollable components ↔ certainty-equivalence or expected-value reductions.

## Questions this raises
- How large an error in $\tilde J$ can Newton's method tolerate, and how does lookahead length enlarge that region (p. 79)?
- When is the belief state a better choice than the information vector, given that the belief is infinite-dimensional and $I_k$ grows with time (pp. 81, 101)?
- Why does the order of agents not destroy cost improvement in multiagent rollout, and what changes without full information sharing (Sec. 2.9, p. 105)?
- How should a controller balance robust design, adaptation and on-line replanning when $b$ and the disturbance law keep changing (p. 108)?

## Reading notes
- This is part 4 of 6 of Chapter 1. It starts at printed p. 79 (it opens with item (c) of a list whose items (a) and (b) presumably sit on p. 78, which is not given; the number of the preceding section is not visible on these pages) and ends at printed p. 108, mid-Sec. 1.6.8 ("Robust and adaptive control" is cut off). Printed = pdf − 20.
- Page 82 repeats nearly the same paragraph twice ("A related consideration is the context…"), with slightly different wording. This looks like an editing leftover. I merged both.
- In Sec. 1.6.5, the text introduces "additional state variables $y_k$ and $s_k$" but then uses $z_k=u_{k-1}$ (p. 92). $s_k$ appears to be a misprint for $z_k$.
- The parking policy "park at $k=0,\dots,N-1$ if $c(k)\le\hat J_{k+1}$" (p. 85) uses $\hat J_N$, which is not defined on these pages. At $k=N-1$ the recursion for $J^*_{N-1}(F)$ compares $c(N-1)$ with $C$.
- In (1.75) the minimization is over $U_k(x_k)$, while after (1.73) the text says $U_k$ must be independent of $x_k$ when the state is unobserved.
- The text layer shows $\to$ for $-$ in subscripts ($x_{k\to1}$) and $\downarrow$ for $\in$. The page images were used for all equations.
- The unit contains no exercises.
