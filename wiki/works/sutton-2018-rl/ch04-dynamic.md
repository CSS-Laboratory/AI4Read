---
id: sutton-2018-rl/ch04-dynamic
work: sutton-2018-rl
unit: Chapter 4 — Dynamic Programming
pages: 73-90
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Dynamic Programming

## L0 — One line
Given a complete model of a finite MDP, you can compute optimal policies by turning the Bellman equations into repeated update rules, and all later methods in the book can be viewed as attempts to achieve much the same effect with less computation and without assuming a perfect model.

## L1 — The gist (≤ 120 words)
The chapter asks how to compute optimal behaviour when the MDP's dynamics $p(s',r|s,a)$ are fully known. The answer is dynamic programming (DP). Policy evaluation finds $v_\pi$ by iterating the Bellman equation. Policy improvement makes a policy greedy with respect to $v_\pi$, which gives a policy at least as good. Alternating them gives policy iteration. Truncating evaluation to one sweep gives value iteration. Both converge to optimal policies for finite MDPs. Asynchronous variants update states in any order, as long as every state keeps being updated. The unifying view is generalized policy iteration (GPI). DP needs a perfect model and heavy computation, but it is the theoretical base of the rest of the book.

**Prerequisites:** finite MDPs; return and discounting; $v_\pi$, $q_\pi$, $v_*$ and the Bellman equations from Chapter 3; expectation; argmax.

## L2 — Key ideas
- DP means algorithms that compute optimal policies from a perfect MDP model. Classical DP is of limited utility in RL, but it is an essential foundation for understanding the later methods, which can be viewed as attempts to achieve much the same effect (p. 73).
- DP turns Bellman equations into assignments (update rules). Iterative policy evaluation does this for $v_\pi$ (4.5). It converges to $v_\pi$ under the conditions that guarantee $v_\pi$ exists (p. 74).
- Policy improvement theorem: if $q_\pi(s,\pi'(s)) \ge v_\pi(s)$ for all $s$, then $v_{\pi'} \ge v_\pi$. The greedy policy satisfies this, and improvement stalls only at an optimal policy (pp. 78–79).
- Policy iteration alternates evaluation and improvement. A finite MDP has finitely many deterministic policies, so it reaches an optimal policy in finitely many iterations (p. 80).
- Value iteration is the Bellman optimality equation as an update, or policy iteration with evaluation cut to one sweep. All these truncated variants converge for discounted finite MDPs (pp. 83–84).
- Asynchronous DP updates states in any order, as long as every state keeps being updated. This avoids full sweeps and lets DP run alongside an agent's experience (p. 85).
- GPI: evaluation and improvement interact, competing and cooperating. If both stabilize, the policy is greedy for its own value function, so Bellman optimality holds (p. 86).
- In the worst case, and ignoring a few technical details, DP time is polynomial in the number of states and actions, so DP is exponentially faster than direct search in policy space. It also bootstraps, meaning it updates estimates from other estimates (pp. 87, 89).

## L3 — Walkthrough

### Introduction (pp. 73–74)
- DP = a collection of algorithms that compute optimal policies given a perfect model of the environment as an MDP. Two drawbacks: the model assumption and the computational cost. It is still important theoretically: all the methods in the rest of the book can be viewed as attempts to achieve much the same effect as DP, only with less computation and without assuming a perfect model (p. 73).
- From here on we usually assume the MDP is finite: sets $\mathcal S,\mathcal A,\mathcal R$ are finite, and dynamics are $p(s',r|s,a)$ with $s'\in\mathcal S^+$ ($\mathcal S$ plus a terminal state if episodic) (p. 73).
- For continuous states and actions, exact solutions exist only in special cases. A common approximation is to quantize the spaces and then apply finite-state DP (p. 73).
- Key idea: use value functions to organize the search for good policies. Optimal policies are easy once $v_*$ or $q_*$ is known. They satisfy (p. 73):
$$v_*(s)=\max_a \mathbb E[R_{t+1}+\gamma v_*(S_{t+1})\mid S_t=s,A_t=a]=\max_a\sum_{s',r}p(s',r|s,a)\big[r+\gamma v_*(s')\big]\tag{4.1}$$
$$q_*(s,a)=\mathbb E\big[R_{t+1}+\gamma\max_{a'}q_*(S_{t+1},a')\mid S_t=s,A_t=a\big]=\sum_{s',r}p(s',r|s,a)\big[r+\gamma\max_{a'}q_*(s',a')\big]\tag{4.2}$$
- DP algorithms come from turning such Bellman equations into update rules for improving approximations (p. 74).

### 4.1 Policy Evaluation (Prediction) (pp. 74–76)
- Policy evaluation (also the *prediction problem*) = computing $v_\pi$ for an arbitrary policy $\pi$ (p. 74):
$$v_\pi(s)\doteq\mathbb E_\pi[G_t\mid S_t=s]=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s]=\mathbb E_\pi[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t=s]\tag{4.3}$$
$$=\sum_a\pi(a|s)\sum_{s',r}p(s',r|s,a)\big[r+\gamma v_\pi(s')\big]\tag{4.4}$$
- $v_\pi$ exists and is unique if either $\gamma<1$ or eventual termination is guaranteed from all states under $\pi$ (p. 74).
- With known dynamics, (4.4) is $|\mathcal S|$ linear equations in $|\mathcal S|$ unknowns. In principle it is a straightforward but tedious solve. Iterative methods are preferred here (p. 74).
- Iterative policy evaluation: choose $v_0$ arbitrarily (terminal state must get 0). Then use (4.4) as an update (p. 74):
$$v_{k+1}(s)\doteq\mathbb E_\pi[R_{t+1}+\gamma v_k(S_{t+1})\mid S_t=s]=\sum_a\pi(a|s)\sum_{s',r}p(s',r|s,a)\big[r+\gamma v_k(s')\big]\tag{4.5}$$
- $v_k=v_\pi$ is a fixed point of (4.5), because the Bellman equation gives equality there. In general $\{v_k\}\to v_\pi$ as $k\to\infty$ under the same conditions that guarantee $v_\pi$ exists (p. 74).
- An **expected update** replaces a state's value using the old values of its successors and the expected rewards over all one-step transitions. "Expected" because it uses an expectation over all next states, not a sampled one. All DP updates are of this kind (pp. 74–75).
- Two-array version: keeps old $v_k$ and new $v_{k+1}$ separately. In-place version: each new value overwrites the old one at once. The in-place version also converges to $v_\pi$ and usually converges faster. The order of states in the sweep strongly affects its speed (p. 75).
- The pseudocode (p. 75) loops over states: $v\leftarrow V(s)$; $V(s)\leftarrow\sum_a\pi(a|s)\sum_{s',r}p(s',r|s,a)[r+\gamma V(s')]$; $\Delta\leftarrow\max(\Delta,|v-V(s)|)$. It stops when $\Delta<\theta$ after a sweep. Exact convergence is only in the limit (p. 75).
- **Example 4.1 (gridworld)** (p. 76): 14 nonterminal states, 4 actions (up, down, right, left). They move deterministically, but an action that would leave the grid leaves the state unchanged. Reward is $-1$ on all transitions until termination. The task is undiscounted and episodic. Policy: equiprobable random. Figure 4.1 (p. 77) shows $v_k$: all 0.0 at $k=0$; $-1.0$ in every nonterminal state at $k=1$; $-1.7$ and $-2.0$ at $k=2$. The limit $v_\pi$ ranges from $-14$ next to the terminal squares to $-22$ in the far corners (the squares adjacent to the corner terminal states are $-14$, the middle are $-18$ and $-20$). Here $v_\pi$ is the negative of the expected number of steps to termination (p. 76).

> **Intuition note.** Evaluating a fixed policy is like repeatedly asking "what is my value if I use my neighbours' current estimates?". Each sweep pushes correct information one step further from the terminal state until the changes become negligible (exact convergence comes only in the limit).

### 4.2 Policy Improvement (pp. 76–80)
- Goal: use $v_\pi$ to find a better policy. For a deterministic $\pi$ and one state $s$, ask whether choosing $a\ne\pi(s)$ there, then following $\pi$, is better. Its value is (p. 78):
$$q_\pi(s,a)\doteq\mathbb E[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t=s,A_t=a]=\sum_{s',r}p(s',r|s,a)\big[r+\gamma v_\pi(s')\big]\tag{4.6}$$
- **Policy improvement theorem.** Let $\pi,\pi'$ be deterministic policies such that for all $s\in\mathcal S$
$$q_\pi(s,\pi'(s))\ge v_\pi(s).\tag{4.7}$$
Then $\pi'$ is as good as or better than $\pi$:
$$v_{\pi'}(s)\ge v_\pi(s)\quad\text{for all }s.\tag{4.8}$$
If (4.7) is strict at some state, then (4.8) is strict at that state (p. 78).
- Special case: $\pi'$ equals $\pi$ except $\pi'(s)=a\ne\pi(s)$. Then (4.7) holds trivially at other states. So $q_\pi(s,a)>v_\pi(s)$ implies $\pi'$ is better (p. 78).
- Proof idea (p. 78): expand the $q_\pi$ side with (4.6) and reapply (4.7) repeatedly:
$$\begin{aligned}v_\pi(s)&\le q_\pi(s,\pi'(s))=\mathbb E[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t=s,A_t=\pi'(s)]\\&=\mathbb E_{\pi'}[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t=s]\\&\le\mathbb E_{\pi'}[R_{t+1}+\gamma q_\pi(S_{t+1},\pi'(S_{t+1}))\mid S_t=s]\quad\text{(by 4.7)}\\&=\mathbb E_{\pi'}[R_{t+1}+\gamma\,\mathbb E[R_{t+2}+\gamma v_\pi(S_{t+2})\mid S_{t+1},A_{t+1}=\pi'(S_{t+1})]\mid S_t=s]\\&=\mathbb E_{\pi'}[R_{t+1}+\gamma R_{t+2}+\gamma^2v_\pi(S_{t+2})\mid S_t=s]\\&\le\mathbb E_{\pi'}[R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\gamma^3v_\pi(S_{t+3})\mid S_t=s]\\&\;\vdots\\&\le\mathbb E_{\pi'}[R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\gamma^3R_{t+4}+\cdots\mid S_t=s]=v_{\pi'}(s).\end{aligned}$$
- Greedy policy: change all states at once, picking the action that looks best by $q_\pi$ (ties broken arbitrarily) (p. 79):
$$\pi'(s)\doteq\arg\max_a q_\pi(s,a)=\arg\max_a\mathbb E[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t=s,A_t=a]=\arg\max_a\sum_{s',r}p(s',r|s,a)\big[r+\gamma v_\pi(s')\big]\tag{4.9}$$
  It looks one step ahead using $v_\pi$. By construction it satisfies (4.7), so it is as good as or better than $\pi$. Making a policy greedy with respect to its own value function is **policy improvement** (p. 79).
- If $\pi'$ is as good as but not better than $\pi$, then $v_\pi=v_{\pi'}$, and (4.9) gives $v_{\pi'}(s)=\max_a\sum_{s',r}p(s',r|s,a)[r+\gamma v_{\pi'}(s')]$. This is (4.1), so $v_{\pi'}=v_*$ and both policies are optimal. Hence improvement gives a strictly better policy unless the original is already optimal (p. 79).
- Stochastic policies: the authors say all ideas extend, and the theorem carries through as stated. Ties need not be broken: any split of probability among maximizing actions is allowed, if submaximal actions get zero (p. 79).
- Gridworld again: the greedy policy for $v_\pi$ (random policy) has values $-1,-2$ or $-3$ everywhere, versus $v_\pi$ at most $-14$, so it is an improvement. Here it happens to be optimal. In general only improvement is guaranteed (pp. 79–80). Figure 4.1 caption: all policies after the third iteration are optimal (p. 77).

> **Intuition note.** If deviating once to a better action and then going back to old behaviour already helps, then one would expect deviating every time that state appears to help even more; the theorem makes this precise. The proof formalizes this by unrolling one deviation at a time.

### 4.3 Policy Iteration (pp. 80–82)
- Chain: $\pi_0\xrightarrow{E}v_{\pi_0}\xrightarrow{I}\pi_1\xrightarrow{E}v_{\pi_1}\xrightarrow{I}\pi_2\cdots\to\pi_*\xrightarrow{E}v_*$ (E = evaluation, I = improvement). Each policy is a strict improvement unless already optimal. A finite MDP has finitely many deterministic policies, so this converges to an optimal policy in finitely many iterations (p. 80).
- Algorithm box (p. 80): (1) initialize $V,\pi$ arbitrarily, $V(\text{terminal})=0$; (2) evaluate $\pi$ until $\Delta<\theta$ with $V(s)\leftarrow\sum_{s',r}p(s',r|s,\pi(s))[r+\gamma V(s')]$; (3) for each $s$, set $\pi(s)\leftarrow\arg\max_a\sum_{s',r}p(s',r|s,a)[r+\gamma V(s')]$. If no action changed, stop; else go to 2. Each evaluation starts from the previous $V$, which typically speeds convergence (presumably because $V$ changes little between policies) (p. 80).
- **Example 4.2 (Jack's car rental)** (p. 81): two locations. Renting a car earns \$10; moving a car overnight costs \$2. Requests and returns are Poisson, $P(n)=\frac{\lambda^n}{n!}e^{-\lambda}$. Requests: $\lambda=3$ and $4$; returns: $\lambda=3$ and $2$. At most 20 cars per location, at most 5 moved per night, $\gamma=0.9$. The task is a continuing finite MDP: time step = day, state = cars at each location at day's end, action = net cars moved. Policy iteration from "never move cars" ($\pi_0$) gives $\pi_1,\dots,\pi_4$ (Figure 4.2); each is a strict improvement and the last is optimal (p. 81).
- Policy iteration often converges in surprisingly few iterations. In the gridworld it would find the optimal policy after one iteration (p. 82).

> **Intuition note.** Evaluate, then act greedily, and repeat. Each round can only help, and there are only finitely many deterministic policies, so the process must end at an optimal policy.

### 4.4 Value Iteration (pp. 82–84)
- Drawback of policy iteration: each iteration contains a full policy evaluation, which converges exactly only in the limit. Figure 4.1 suggests truncation is possible: after three iterations, further evaluation does not change the greedy policy. Evaluation can be truncated in several ways without losing convergence guarantees (p. 82).
- **Value iteration** = evaluation stopped after one sweep, merged with improvement (p. 83):
$$v_{k+1}(s)\doteq\max_a\mathbb E[R_{t+1}+\gamma v_k(S_{t+1})\mid S_t=s,A_t=a]=\max_a\sum_{s',r}p(s',r|s,a)\big[r+\gamma v_k(s')\big]\tag{4.10}$$
  For arbitrary $v_0$, $\{v_k\}$ converges to $v_*$ under the same conditions that guarantee $v_*$ exists (p. 83).
- Equivalent view: it is the Bellman optimality equation (4.1) turned into an update. It differs from the evaluation update (4.5) only by taking the max over actions instead of averaging by $\pi$ (p. 83).
- Pseudocode (p. 83): same loop as policy evaluation, with $V(s)\leftarrow\max_a\sum_{s',r}p(s',r|s,a)[r+\gamma V(s')]$, stopping at $\Delta<\theta$. Then output a deterministic $\pi(s)=\arg\max_a\sum_{s',r}p(s',r|s,a)[r+\gamma V(s')]$.
- Faster convergence is often achieved by inserting several evaluation sweeps between improvement sweeps. *Truncated policy iteration* = any mix of evaluation sweeps and value-iteration sweeps. All converge to an optimal policy for discounted finite MDPs (pp. 83–84).
- **Example 4.3 (gambler's problem)** (p. 84): bet on coin flips with heads probability $p_h$. Goal \$100, lose at \$0. State = capital $s\in\{1,\dots,99\}$; actions = stakes $a\in\{0,1,\dots,\min(s,100-s)\}$. Reward is 0 except $+1$ on reaching the goal. The task is undiscounted and episodic; since reward is $+1$ only on reaching the goal, $v$ = probability of winning. For $p_h=0.4$, value iteration gives the policy in Figure 4.3, which is optimal but not unique (ties in the argmax give a whole family) (p. 84).

> **Intuition note.** Value iteration skips the "who is the policy?" question. It directly asks "what is the best value one step ahead?" at every state, and the best policy appears at the end.

### 4.5 Asynchronous Dynamic Programming (pp. 85–86)
- Problem with sweeps: if the state set is huge, one sweep is too costly. Backgammon has over $10^{20}$ states. At a million updates per second, one sweep would take over a thousand years (p. 85).
- Asynchronous DP: in-place algorithms with no systematic sweeps. They update states in any order, using whatever values are available. They must keep updating all states: none may be ignored after some point (p. 85).
- Example: update one state $s_k$ per step with (4.10). If $0\le\gamma<1$, asymptotic convergence to $v_*$ is guaranteed given only that every state occurs infinitely often in $\{s_k\}$ (the sequence may be random). Footnote: in the undiscounted episodic case some orderings may fail to converge, but they are relatively easy to avoid (p. 85).
- Avoiding sweeps does not necessarily mean less total computation. It means progress is not locked behind a long sweep. One can order updates to propagate information efficiently, or skip irrelevant states (p. 85).
- DP can run while an agent experiences the MDP. Experience selects which states to update, and the latest values and policy guide the agent. For example, update states as the agent visits them. The authors call this focusing "a repeated theme in reinforcement learning" (pp. 85–86).

### 4.6 Generalized Policy Iteration (pp. 86–87)
- Policy iteration has two interacting processes: evaluation (make $V$ consistent with $\pi$) and improvement (make $\pi$ greedy for $V$). They need not alternate to completion. Value iteration does one evaluation step between improvements, and asynchronous methods interleave them even more finely. As long as both keep updating all states, the result is typically convergence to $v_*$ and an optimal policy (p. 86).
- **GPI** = letting evaluation and improvement interact, whatever their granularity. Almost all RL methods are well described as GPI: they have identifiable policies and value functions, with the policy improved with respect to the value function and the value function driven toward the policy's value (p. 86).
- If both processes stabilize, then the value function is consistent with the policy and the policy is greedy for the value function. The policy is then greedy for its own evaluation function, so (4.1) holds and both are optimal (p. 86).
- The processes compete (greedy improvement typically makes $V$ wrong for the new policy; evaluation typically makes the policy non-greedy) and cooperate (they find one joint solution) (p. 86).
- Geometric picture (p. 87): two goals as two non-orthogonal lines in a plane ($v=v_\pi$ and $\pi=\text{greedy}(v)$). Driving toward one goal moves away somewhat from the other, but the joint process gets closer to optimality. The authors note the real geometry is much more complicated. Steps may be complete (policy iteration) or incomplete (p. 87).

> **Intuition note.** Think of two people correcting each other's work: each fix partly spoils the other's, yet they only stop when each is satisfied with the other. That fixed point is the optimal policy together with its value function.

### 4.7 Efficiency of Dynamic Programming (pp. 87–88)
- Ignoring technical details, worst-case DP time is polynomial in the number of states $n$ and actions $k$. The number of deterministic policies is $k^n$, so DP is exponentially faster than direct policy search (p. 87).
- Linear programming can solve MDPs and sometimes has better worst-case guarantees. But it becomes impractical at a much smaller number of states than DP, by a factor of about 100. For the largest problems only DP is feasible (p. 87).
- Curse of dimensionality: the number of states often grows exponentially with the number of state variables. The authors say this is inherent in the problem, not in DP, and DP copes comparatively better than the alternatives (p. 87).
- In practice DP solves MDPs with millions of states. Policy and value iteration are both widely used, and it is not clear which is better in general. They usually converge much faster than worst-case bounds, especially from good initial values or policies (p. 87).
- With large state spaces asynchronous methods are often preferred: even one full sweep may be impractical, while relatively few states occur along optimal trajectories (p. 88).

### 4.8 Summary (pp. 88–89)
- Policy evaluation, policy improvement, policy iteration and value iteration are summarized. Both of the last two reliably compute optimal policies and value functions for finite MDPs given complete knowledge of the MDP (p. 88).
- Expected updates are "little more than" Bellman equations turned into assignments. Four value functions ($v_\pi,v_*,q_\pi,q_*$) give four Bellman equations and four expected updates (p. 88).
- GPI: two processes around an approximate policy and an approximate value function, working to a joint solution unchanged by either. Convergence is proven in some cases, notably classical DP, and not in others (p. 88).
- **Bootstrapping** = updating estimates from other estimates. All DP methods do this. The next chapter covers methods with no model and no bootstrapping. The chapter after covers methods with no model that do bootstrap (p. 89).

### Bibliographical and Historical Remarks (pp. 89–90)
- "Dynamic programming" is due to Bellman (1957a). Policy improvement theorem and policy iteration are due to Bellman (1957a) and Howard (1960). Value iteration as truncated policy iteration follows Puterman and Shin (1978) (p. 89).
- Two-array (Jacobi-style, synchronous) versus in-place (Gauss–Seidel-style) versions of iterative policy evaluation. Asynchronous DP is due to Bertsekas, motivated by multiprocessor implementation with communication delays (p. 90).

## Toy example
Our own, not from the text. One nonterminal state $A$, terminal $T$ (value 0), $\gamma=0.9$. Actions: *stay* (reward $-1$, back to $A$) and *go* (reward $-2$, to $T$). Dynamics are deterministic.

**Value iteration (4.10), $v_0(A)=0$:**
- $v_1=\max(-1+0.9\cdot0,\,-2+0.9\cdot 0)=\max(-1,-2)=-1$.
- $v_2=\max(-1+0.9(-1),\,-2)=\max(-1.9,-2)=-1.9$.
- $v_3=\max(-1+0.9(-1.9),\,-2)=\max(-2.71,-2)=-2$.
- $v_4=\max(-1+0.9(-2),\,-2)=\max(-2.8,-2)=-2$. The value is unchanged, so $v_*(A)=-2$, and the greedy action is *go*.

**Policy iteration:**
- Start with $\pi_0=$ stay. Evaluation: $v=-1+0.9v$, so $v=-1/0.1=-10$.
- Improvement (4.9): $q(A,\text{stay})=-1+0.9(-10)=-10$; $q(A,\text{go})=-2+0=-2$. Since $-2>-10$, $\pi_1=$ go.
- Evaluate $\pi_1$: $v=-2$. Improvement: $q(A,\text{stay})=-1+0.9(-2)=-2.8<-2=q(A,\text{go})$. The policy is stable, so $\pi_1$ is optimal. Both methods give $v_*(A)=-2$.

## Concepts
- [[markov-decision-process]] — finite MDP with known $p(s',r|s,a)$; the setting of all DP here (p. 73)
- [[bellman-equation-value-function]] — equations (4.1)–(4.4) relating a state's value to its successors; DP turns them into updates (pp. 73–74)
- [[policy]] — rule $\pi(a|s)$ for choosing actions; deterministic or stochastic (pp. 74, 79)
- [[policy-evaluation]] (new) — iteratively computing $v_\pi$ for a given $\pi$ via (4.5) (p. 74)
- [[policy-improvement]] (new) — making a policy greedy w.r.t. $v_\pi$, giving a policy at least as good (p. 79)
- [[policy-iteration]] (new) — alternating evaluation and improvement until the policy is stable (p. 80)
- [[value-iteration]] (new) — update (4.10): Bellman optimality as an assignment; evaluation cut to one sweep (p. 83)
- [[asynchronous-dp]] (new) — in-place DP updating states in any order, if all are updated forever (p. 85)
- [[generalized-policy-iteration]] (new) — interacting evaluation and improvement processes at any granularity (p. 86)
- [[expected-update]] (new) — update based on an expectation over all next states, not a sample (p. 74)
- [[bootstrapping]] (new) — updating estimates from other estimates (p. 89)
- [[curse-of-dimensionality]] (new) — the number of states often grows exponentially with state variables (p. 87)
- [[model-based-vs-model-free-rl]] — DP needs a perfect model; later methods drop that requirement (pp. 73, 89)

## Canonical instances
- [[gridworld-4x4]] — random policy's $v_\pi$ equals negative expected steps to termination; greedy policy is optimal after one improvement (pp. 76, 79–80, 82)
- [[jacks-car-rental]] — policy iteration on a continuing MDP with Poisson demand; five successive policies (p. 81)
- [[gamblers-problem]] — value iteration on an episodic MDP; $v$ is the probability of winning; optimal policy not unique (p. 84)
- [[backgammon-state-count]] — over $10^{20}$ states, so a single sweep is infeasible (p. 85)

## Bridges (candidates)
- [structural-analogy] Policy iteration/GPI ↔ control theory: controller design alternating "estimate performance of the current law" and "improve the law" — two processes with a joint fixed point.
- [same-math] Iterative policy evaluation ↔ numerical linear algebra: Jacobi (two-array) and Gauss–Seidel (in-place) solution of a linear system, as the text states (p. 90).
- [structural-analogy] Value iteration's Bellman backup ↔ optimal control: backward recursion on the value function, where the max over actions is the optimizing step.
- [metaphor] GPI's two non-orthogonal goals ↔ negotiation or mutual adjustment, where each side's improvement partly undoes the other's.

## Questions this raises
- How does the update change if the model $p(s',r|s,a)$ is unknown and must be learned from sampled experience (the topic the text promises for the next chapters)?
- Why exactly does value iteration converge for arbitrary $v_0$, and how fast, as a function of $\gamma$?
- How much does the order of in-place updates matter, and how should one choose states to update (the text defers this to Chapter 8)?
- When GPI has no convergence proof, what can go wrong?

## Exercises worth doing
- Ex. 4.1 (p. 76) — compute $q_\pi$ in the gridworld from the given $v_\pi$ — difficulty: easy
- Ex. 4.3 (p. 76) — write the action-value analogues of (4.3)–(4.5) — difficulty: easy
- Ex. 4.4 (p. 82) — fix the policy iteration pseudocode so it must terminate when policies tie — difficulty: medium
- Ex. 4.5 (p. 82) — policy iteration for $q_*$; the text says its ideas are used throughout the book — difficulty: medium
- Ex. 4.8 (p. 84) — why the gambler's optimal policy bets everything at capital 50 but not at 51 — difficulty: medium
- Ex. 4.9 (p. 84) — implement value iteration for the gambler's problem at $p_h=0.25$ and $0.55$ — difficulty: medium

## Reading notes
- Printed page = pdf − 22 (e.g. pdf 95 = printed 73). Labels give the printed numbers, so these are cited.
- The text layer drops or garbles $\gamma$, $\ge$, $\le$, $\leftarrow$ and the Example 4.1 reward line ("$R_t=-1$"). All equations here were checked against the page images, which show $\gamma$ throughout (4.1)–(4.10).
- Figure 4.1 values are rounded to two significant digits (caption, p. 77). The $k=\infty$ values ($-14,-18,-20,-22$) are read from the image.
- Cross-references to pages 59 and Figure 3.4 (backup diagrams) point outside this unit and were not checked.
- The word "Interlocutor" does not apply: the whole unit is in the authors' voice.
