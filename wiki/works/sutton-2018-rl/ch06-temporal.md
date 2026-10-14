---
id: sutton-2018-rl/ch06-temporal
work: sutton-2018-rl
unit: "Chapter 6 — Temporal-Difference Learning"
pages: 119–140
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Temporal-Difference Learning

## L0 — One line
Temporal-difference (TD) learning updates a value estimate toward "observed reward + current estimate of the next state's value", so an agent can learn online, from raw experience, without a model and without waiting for the final outcome.

## L1 — The gist (≤ 120 words)
The chapter asks how an agent can predict long-run reward, and then control its behavior, from raw experience. It should need no model and no wait for the episode to end. The answer is TD learning. Each estimate is moved toward the next reward plus the current estimate of the next state's value (bootstrapping). Tabular TD(0) is proved to converge for a fixed policy. In batch training it generally converges to the certainty-equivalence estimate. The chapter derives the control methods Sarsa (on-policy), Q-learning and Expected Sarsa (off-policy), and Double Q-learning to counter maximization bias. The authors call these one-step methods today's most widely used RL methods (p. 138).

**Prerequisites:** Markov decision process, return and value function; Bellman equation for $v_\pi$; Monte Carlo prediction; ε-greedy policies; step-size averaging; expectation.

## L2 — Key ideas
- **TD = Monte Carlo sampling + DP bootstrapping.** TD learns from sampled experience like Monte Carlo (MC, which waits for the sampled return), but updates from other estimates like dynamic programming (DP) (p. 119, p. 121).
- **The TD(0) update uses the target $R_{t+1}+\gamma V(S_{t+1})$ and the TD error $\delta_t$.** It can update at the next step, not at episode end (p. 120–121).
- **With fixed $V$, the Monte Carlo error equals a discounted sum of TD errors** (6.6) (p. 121).
- **TD is online, needs no model, and converges.** Its convergence is proved for a fixed policy. Which method learns faster is open in theory, but TD has usually been found faster than constant-α MC on stochastic tasks in practice (p. 124).
- **Batch TD(0) gives the certainty-equivalence estimate; batch MC minimizes error on the training data.** (The certainty-equivalence estimate is the value function exactly correct for the model fitted to the data; batch means the data are reused repeatedly with one update per pass.) This helps explain TD's speed. Forming that model may need memory of order $n^2$, while TD can approximate the same solution with memory of order $n$ (p. 128).
- **Sarsa learns the value of the policy it follows.** Q-learning's $Q$ approximates $q_*$ whatever policy is followed, provided all state–action pairs keep being updated. On cliff walking Sarsa did better online (p. 129–132).
- **Expected Sarsa replaces the sampled next action by an expectation.** This removes the variance due to the random choice of $A_{t+1}$, and it is exactly Q-learning if the target policy is greedy and behavior is more exploratory (p. 133–134).
- **A maximum over noisy estimates can give a significant positive bias (maximization bias); double learning gives an estimate that is unbiased in that sense.** One estimate picks the action, the other evaluates it; in the example it seems to remove the harm (p. 134–136).
- **Afterstate values exploit known immediate effects of actions** (an afterstate is the position right after the agent's move) (p. 136–137).

## L3 — Walkthrough

### Chapter introduction (p. 119)
- The authors say that if one had to name one idea "central and novel" to RL, it would undoubtedly be TD learning (p. 119). It combines Monte Carlo ideas (learn from experience, no model) with DP ideas (bootstrap: update from other estimates, no final outcome).
- Chapter 7 (n-step methods) is a bridge from TD to Monte Carlo. Chapter 12 (TD(λ)) unifies them (p. 119).
- The chapter starts with **prediction** (estimate $v_\pi$ for a given $\pi$). For **control**, DP, TD and Monte Carlo all use some form of generalized policy iteration (GPI). The methods differ mainly in how they do prediction (p. 119).

### 6.1 TD Prediction
**Constant-α MC** (every-visit, suits nonstationary problems), with $G_t$ the actual return after $t$ (p. 119–120):
$$V(S_t)\leftarrow V(S_t)+\alpha\big[G_t-V(S_t)\big]\tag{6.1}$$
It must wait until the episode ends, because only then is $G_t$ known (p. 120).

**TD(0)** (one-step TD) forms a target at $t+1$ from the observed $R_{t+1}$ and the estimate $V(S_{t+1})$ (p. 120):
$$V(S_t)\leftarrow V(S_t)+\alpha\big[R_{t+1}+\gamma V(S_{t+1})-V(S_t)\big]\tag{6.2}$$
- MC target: $G_t$. TD target: $R_{t+1}+\gamma V(S_{t+1})$ (p. 120).
- Tabular TD(0) procedure (p. 120): input policy $\pi$; step size $\alpha\in(0,1]$; initialize $V(s)$ arbitrarily except $V(\text{terminal})=0$. For each step: $A\leftarrow$ action from $\pi$ for $S$; take $A$, observe $R,S'$; $V(S)\leftarrow V(S)+\alpha[R+\gamma V(S')-V(S)]$; $S\leftarrow S'$; until $S$ is terminal.

**Why it is bootstrapping and how the targets differ** (p. 120):
$$v_\pi(s)\doteq\mathbb E_\pi[G_t\mid S_t=s]\tag{6.3}$$
$$=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s]\quad(\text{from }(3.9))$$
$$=\mathbb E_\pi[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t=s]\tag{6.4}$$
- MC uses a sample return in place of the unknown expectation in (6.3). That makes its target an estimate (p. 120).
- DP targets are estimates only because $v_\pi(S_{t+1})$ is replaced by $V(S_{t+1})$. The expectations come from a model (p. 120).
- The TD target is an estimate for both reasons. It samples the expectation in (6.4) and uses $V$ instead of $v_\pi$ (p. 120).

TD and MC updates are **sample updates**: they use one sampled successor. DP uses **expected updates** over all successors (p. 121). The TD(0) backup diagram is one transition from a state to the next state (p. 121).

**TD error** (p. 121):
$$\delta_t\doteq R_{t+1}+\gamma V(S_{t+1})-V(S_t)\tag{6.5}$$
- It is the error in the estimate made at time $t$, but it is available only at $t+1$ (p. 121).
- **If $V$ does not change during the episode**, the MC error is a sum of TD errors (p. 121):
$$\begin{aligned}G_t-V(S_t)&=R_{t+1}+\gamma G_{t+1}-V(S_t)+\gamma V(S_{t+1})-\gamma V(S_{t+1})\\&=\delta_t+\gamma\big(G_{t+1}-V(S_{t+1})\big)\\&=\delta_t+\gamma\delta_{t+1}+\gamma^2\big(G_{t+2}-V(S_{t+2})\big)\\&=\delta_t+\gamma\delta_{t+1}+\dots+\gamma^{T-t-1}\delta_{T-1}+\gamma^{T-t}\big(G_T-V(S_T)\big)\\&=\delta_t+\gamma\delta_{t+1}+\dots+\gamma^{T-t-1}\delta_{T-1}+\gamma^{T-t}(0-0)\\&=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k\end{aligned}\tag{6.6}$$
- The identity is not exact if $V$ changes during the episode, as in TD(0). With a small step size it may still hold approximately (p. 121).

*Intuition note.* Each TD error measures how much the estimate at one step is off. If $V$ does not change during the episode, the discounted sum of these errors from $t$ to the end equals the MC error of the early prediction. TD can apply the correction step by step, MC only at the end.

**Example 6.1 (Driving Home)** (p. 122–123). The reward is the elapsed time on each leg, $\gamma=1$, and the value of a state is the expected time to go. Table (minutes):

| State | Elapsed | Predicted time to go | Predicted total |
|---|---|---|---|
| leaving office | 0 | 30 | 30 |
| reach car, raining | 5 | 35 | 40 |
| exiting highway | 20 | 15 | 35 |
| secondary road, behind truck | 30 | 10 | 40 |
| entering home street | 40 | 3 | 43 |
| arrive home | 43 | 0 | 43 |

- MC with $\alpha=1$ moves every prediction to the actual outcome. At the highway exit, $G_t-V(S_t)=23-15=8$ minutes. With $\alpha=1/2$ the estimate would rise by 4 minutes. The authors think this is probably too large, since the truck was probably just bad luck. The change can only be made after arriving home (p. 122).
- TD moves each estimate toward the estimate that follows it. Each error is proportional to the temporal difference of predictions (Fig. 6.1 right, $\alpha=1$) (p. 123).
- Second day: stuck in a traffic jam, after 25 minutes you estimate 25 more (total 50). TD shifts the initial estimate from 30 toward 50 immediately. MC must wait for the true return (p. 123).

### 6.2 Advantages of TD Prediction Methods (p. 124–125)
- **Versus DP:** TD needs no model of rewards or next-state probabilities (p. 124).
- **Versus MC:** TD is naturally online and fully incremental. It waits one step, not an episode. This matters for very long episodes and continuing tasks. Some MC methods must ignore or discount episodes with exploratory actions. TD learns from every transition whatever actions follow, so it is much less susceptible (p. 124).
- **Soundness:** for any fixed $\pi$, TD(0) has been proved to converge to $v_\pi$. Convergence is in the mean for a constant step size if it is sufficiently small, and with probability 1 if the step size decreases according to the usual conditions (2.7). Most proofs are for the tabular case, some for linear function approximation (Sec. 9.4) (p. 124).
- **Speed:** no one has proved that either method converges faster, and it is unclear how to phrase the question formally. In practice TD usually converges faster than constant-α MC on stochastic tasks (p. 124).

**Example 6.2 (Random Walk)** (p. 125). A Markov reward process (MRP: an MDP without actions) with states A–E in a row. Episodes start at C and move left or right with equal probability. They end beyond A (reward 0) or beyond E (reward $+1$). All other rewards are 0. The task is undiscounted, so the true values are the probabilities of ending on the right: $\tfrac16,\tfrac26,\tfrac36,\tfrac46,\tfrac56$ for A–E, with $v_\pi(C)=0.5$.
- A single TD(0) run with $\alpha=0.1$: after 100 episodes the values are about as close as they get. With a constant step size they keep fluctuating (p. 125).
- Learning curves: RMS error averaged over the five states and over 100 runs, initial $V(s)=0.5$. TD was consistently better than MC (p. 125).

### 6.3 Optimality of TD(0) (p. 126–128)
**Batch updating** (p. 126). With finite experience, present it repeatedly. Compute the increments of (6.1) or (6.2) for every time step, change $V$ once by their sum, and repeat until convergence.
- For $\alpha$ sufficiently small, batch TD(0) converges deterministically to one answer independent of $\alpha$. Constant-α MC also converges, but to a different answer (p. 126).
- **Example 6.3:** on the random walk, all episodes seen so far were treated as a batch after each new episode. Batch TD was consistently better than batch MC (Fig. 6.2) (p. 126–127).

**What each batch method finds** (p. 127–128):
- Batch MC gives sample averages of the observed returns. These minimize mean squared error on the training set (p. 127).
- Batch TD(0) gives estimates that are exactly correct for the **maximum-likelihood model** of the Markov process. This model uses the fraction of observed transitions $i\to j$ as the transition probability and the average observed reward as the expected reward (p. 128).
- The value function that would be exactly correct if that model were exactly correct is the **certainty-equivalence estimate**. In general, batch TD(0) converges to it (p. 128).

**Example 6.4 (You are the Predictor)** (p. 127–128). Eight episodes: A,0,B,0 once; B,1 six times; B,0 once.
- $V(B)=\tfrac34$ (six of eight returns are 1).
- Batch TD(0) gives $V(A)=\tfrac34$, since A always goes to B with reward 0. This is the value under the fitted model.
- Batch MC gives $V(A)=0$, since A was seen once with return 0. This has zero error on the data.
- The authors expect the first answer to give lower error on future data if the process is Markov (p. 128).

*Intuition note.* Batch MC finds the estimates with the least error on the past returns. Batch TD gives the same answer as first fitting a model of "what follows what" and then asking what that model implies. The authors expect the second to give lower error on future data if the process is Markov.

**Consequences** (p. 128):
- This helps explain TD's speed. Nonbatch TD(0) may be faster because it moves toward a better estimate, though nothing more definite can be said.
- Computing the certainty-equivalence estimate directly is almost never feasible. With $n=|\mathcal S|$ states it may need order $n^2$ memory and order $n^3$ computation. TD approximates it with memory of order $n$.

### 6.4 Sarsa: On-policy TD Control (p. 129–131)
- GPI is used with TD for evaluation. First learn action values $q_\pi(s,a)$ for the current behavior policy $\pi$. Transitions from state–action pair to state–action pair form a Markov chain with rewards, so the TD(0) convergence theorems carry over (p. 129):
$$Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\big[R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t)\big]\tag{6.7}$$
- $Q(S_{t+1},A_{t+1})=0$ if $S_{t+1}$ is terminal. The rule uses the quintuple $(S_t,A_t,R_{t+1},S_{t+1},A_{t+1})$, which gives the name **Sarsa** (p. 129).
- **Sarsa control** (box, p. 130): choose $A$ from $S$ by a policy derived from $Q$ (e.g. ε-greedy); take $A$, observe $R,S'$; choose $A'$ from $S'$ the same way; apply (6.7); $S\leftarrow S'$, $A\leftarrow A'$.
- **Convergence** (p. 129): Sarsa converges with probability 1 to an optimal policy and action-value function, under the usual step-size conditions (2.7). It also needs all state–action pairs visited infinitely often and the policy converging in the limit to the greedy policy (e.g. ε-greedy with $\varepsilon=1/t$).

**Example 6.5 (Windy Gridworld)** (p. 130). The standard four moves, with an upward crosswind in the middle. Wind strength by column: 0 0 0 1 1 1 2 2 1 0 cells. The task is undiscounted, episodic, reward $-1$ until the goal.
- ε-greedy Sarsa with $\varepsilon=0.1$, $\alpha=0.5$, initial $Q=0$: goal reached faster over time. By 8000 steps the greedy policy was long since optimal. Exploration kept the average episode length near 17 steps, versus a minimum of 15 (p. 130).
- MC cannot easily be used here. A policy that never reaches the goal would make an episode never end. Sarsa learns during the episode that such a policy is poor (p. 130).

### 6.5 Q-learning: Off-policy TD Control (p. 131–132)
$$Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\Big[R_{t+1}+\gamma\max_a Q(S_{t+1},a)-Q(S_t,A_t)\Big]\tag{6.8}$$
- $Q$ directly approximates $q_*$, independent of the policy followed. The policy still has an effect: it determines which pairs are visited and updated. Correct convergence needs only that all pairs keep being updated (p. 131).
- Under that condition and a variant of the usual step-size conditions, $Q\to q_*$ with probability 1 (p. 131).
- Algorithm (box, p. 131): as Sarsa, but the target uses $\max_a Q(S',a)$ and no $A'$ is chosen before the update.
- Backup diagram: filled action node at the root, all next-state action nodes below with a max arc (p. 132; Fig. 6.4 is on p. 134).

**Example 6.6 (Cliff Walking)** (p. 132). An undiscounted gridworld with reward $-1$ per step. Stepping into "The Cliff" gives $-100$ and an instant return to the start. With ε-greedy, $\varepsilon=0.1$:
- Q-learning learns the optimal path along the cliff edge, but occasionally falls off because of ε-greedy exploration.
- Sarsa takes action selection into account and learns the longer, safer path.
- Online, Sarsa did better. If $\varepsilon$ were gradually reduced, both would asymptotically converge to the optimal policy (p. 132).

*Intuition note.* Sarsa evaluates the behavior it actually runs, mistakes included. Q-learning evaluates the best possible behavior, so it ignores that exploration sometimes pushes it off the cliff.

### 6.6 Expected Sarsa (p. 133–134)
$$Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\Big[R_{t+1}+\gamma\,\mathbb E_\pi[Q(S_{t+1},A_{t+1})\mid S_{t+1}]-Q(S_t,A_t)\Big]$$
$$=Q(S_t,A_t)+\alpha\Big[R_{t+1}+\gamma\sum_a\pi(a|S_{t+1})Q(S_{t+1},a)-Q(S_t,A_t)\Big]\tag{6.9}$$
- Given $S_{t+1}$, it moves deterministically in the direction Sarsa moves in expectation (p. 133).
- It costs more computation than Sarsa but removes the variance from the random choice of $A_{t+1}$. It generally does slightly better with the same experience (p. 133).
- Cliff walking (Fig. 6.3): Expected Sarsa keeps Sarsa's advantage over Q-learning and improves on Sarsa over a wide range of $\alpha$ (p. 133–134).
- Transitions there are deterministic and all randomness comes from the policy. In such cases Expected Sarsa can set $\alpha=1$ without losing asymptotic performance. Sarsa does well in the long run only at small $\alpha$, where short-term performance is poor (p. 134).
- **Off-policy use:** if behavior differs from the target policy $\pi$, it is off-policy. If $\pi$ is greedy and behavior more exploratory, Expected Sarsa is exactly Q-learning. It subsumes Q-learning and "may completely dominate" Sarsa and Q-learning, apart from a small extra cost (p. 134).

### 6.7 Maximization Bias and Double Learning (p. 134–136)
**Maximization bias.** Q-learning's target policy uses a max, and Sarsa's ε-greedy policy also involves maximization. A maximum over noisy estimates is used as an estimate of the maximum true value, which can give significant positive bias. Example: if all true $q(s,a)=0$ but the estimates scatter above and below zero, the maximum estimate is positive (p. 134).

**Example 6.7** (p. 134–135). Episodes start in A. *Right* ends with reward 0. *Left* goes to B with reward 0. From B, many actions end the episode with a reward from $\mathcal N(-0.1,1)$. So *left* has expected return $-0.1$ and is always a mistake.
- Q-learning with ε-greedy first strongly favors *left*; the authors say control methods may favor *left* because maximization bias makes B appear to have a positive value. Even at asymptote it takes *left* about 5% more often than optimal ($\varepsilon=0.1,\alpha=0.1,\gamma=1$) (p. 135, Fig. 6.5).
- Double Q-learning is essentially unaffected (p. 135).

**Double learning** (p. 135). The bias comes from using the same samples both to pick the maximizing action and to evaluate it.
- Learn two independent estimates $Q_1,Q_2$ of $q(a)$. Use $A^*=\arg\max_aQ_1(a)$ to select and $Q_2(A^*)=Q_2(\arg\max_aQ_1(a))$ to evaluate.
- Then $\mathbb E[Q_2(A^*)]=q(A^*)$ (unbiased in this sense). Reverse the roles for a second estimate.
- Only one estimate is updated per play. Memory doubles, computation per step does not (p. 135).

**Double Q-learning** (p. 135–136). Flip a coin each step. If heads:
$$Q_1(S_t,A_t)\leftarrow Q_1(S_t,A_t)+\alpha\Big[R_{t+1}+\gamma Q_2\big(S_{t+1},\arg\max_aQ_1(S_{t+1},a)\big)-Q_1(S_t,A_t)\Big]\tag{6.10}$$
If tails, swap $Q_1$ and $Q_2$. Behavior can be ε-greedy on $Q_1+Q_2$ (the average or sum). Double versions of Sarsa and Expected Sarsa also exist (p. 136).

*Intuition note.* A noisy estimate that looks best is often best partly by luck. If you rate it with the same data you praise your own luck. Rating it with independent data gives an estimate that is unbiased in that sense.

### 6.8 Games, Afterstates, and Other Special Cases (p. 136–137)
- The tic-tac-toe method of Chapter 1 learned values of board positions after the agent's move. These are **afterstates**. This is neither a usual state-value nor an action-value function (p. 136–137).
- Afterstates help when the immediate effects of actions are known but not the full dynamics (e.g. chess moves, but not the opponent's reply). Many position–move pairs can give the same afterposition. An afterstate value function gives them the same value, so learning about one pair transfers at once to the others, whereas a conventional action-value function would assess each pair separately (p. 137).
- Afterstates also arise in queuing tasks. The methods still fit GPI, with the same on-/off-policy choice (p. 137).

### 6.9 Summary (p. 138)
- TD is an alternative to MC for prediction. Extension to control is via GPI. Sarsa is on-policy. Q-learning, and Expected Sarsa as presented here, are off-policy. Actor–critic methods are the third route, covered in Chapter 13 (p. 138).
- The authors say these methods are today the most widely used RL methods; this is probably due to their simplicity: online, little computation, nearly one equation each. They are called one-step, tabular, model-free TD methods (p. 138).
- TD methods are more general: they learn long-term predictions about dynamical systems. Their theory was first well understood when analyzed as pure prediction methods (p. 138).

**Historical remarks** (p. 139–140), brief: TD(0), the random walk and the name "temporal-difference learning" are mostly from Sutton (1988). Sarsa: Rummery and Niranjan (1994), named by Sutton (1996). Q-learning: Watkins (1989). Expected Sarsa: John (1994), with convergence by van Seijen et al. (2009). Maximization bias and double learning: van Hasselt (2010, 2011). An afterstate is the same notion as a "post-decision state". The term certainty equivalence is from the adaptive control literature (p. 139–140).

## Toy example (ours, not from the text)
Chain A → B → terminal. $\gamma=1$, $\alpha=0.5$.

**Part 1: identity (6.6) with fixed $V$.** Let $V(A)=0.4$, $V(B)=0.7$. Episode: A, reward 0, B, reward 1, end. Then $G_0=0+1=1$.
- $\delta_0=0+0.7-0.4=0.3$; $\delta_1=1+0-0.7=0.3$.
- Sum: $0.3+1\cdot0.3=0.6$. MC error: $G_0-V(A)=1-0.4=0.6$. ✓.

**Part 2: TD versus MC targets.** Let $V(A)=0.4$, $V(B)=0.9$. Suppose B is well known. Episode: A, 0, B, 0 (an unlucky end).
- MC: $V(A)\leftarrow0.4+0.5(0-0.4)=0.2$.
- TD(0): at the A→B step, $V(A)\leftarrow0.4+0.5(0+0.9-0.4)=0.65$. B has not yet been updated at that moment.
- At the B step, both methods give $V(B)\leftarrow0.9+0.5(0-0.9)=0.45$.

TD's update for A reuses what is already believed about B, as in Example 6.4. MC trusts the single noisy return.

## Concepts
- [[temporal-difference-learning]] — update a value estimate toward $R_{t+1}+\gamma V(S_{t+1})$; the bracket is the TD error $\delta_t$ (p. 120–121)
- [[bootstrapping]] (new) — updating an estimate partly from another estimate, a "guess from a guess" (p. 120, p. 124)
- [[sample-vs-expected-update]] (new) — TD/MC use one sampled successor; DP uses all successors with their probabilities (p. 121)
- [[model-based-vs-model-free-rl]] — TD(0) needs no model of reward or transition probabilities (p. 124)
- [[batch-updating]] (new) — sum the increments over all stored experience, then change $V$ once; repeat to convergence (p. 126)
- [[certainty-equivalence]] (new) — value function exactly correct for the maximum-likelihood model; batch TD(0) converges to it (p. 128)
- [[generalized-policy-iteration]] (new) — policy and value function interact so both move toward optimal (p. 129, p. 138)
- [[sarsa]] (new) — on-policy TD control using $(S,A,R,S',A')$ (p. 129)
- [[q-learning]] (new) — off-policy TD control with a max target; $Q$ approximates $q_*$ (p. 131)
- [[expected-sarsa]] (new) — uses $\sum_a\pi(a|S')Q(S',a)$ as target; Q-learning if $\pi$ is greedy (p. 133–134)
- [[exploration-vs-exploitation]] — on-policy and off-policy TD control are two ways to keep exploring (p. 129, p. 138)
- [[maximization-bias]] (new) — positive bias when a max over noisy estimates estimates a max true value (p. 134)
- [[double-learning]] (new) — two independent estimates; one selects, the other evaluates (p. 135)
- [[afterstate]] (new) — position after the agent's move, before the environment's response (p. 137)
- [[policy]] — rule mapping states to actions; ε-greedy policies derived from $Q$ (p. 129)

## Canonical instances
- [[driving-home]] — TD updates predictions step by step, MC only after arrival (p. 122–123)
- [[random-walk-mrp]] — five-state chain; TD(0) beats constant-α MC (p. 125)
- [[you-are-the-predictor]] — eight episodes; batch TD gives $V(A)=\tfrac34$, batch MC gives $0$ (p. 127–128)
- [[windy-gridworld]] — Sarsa where MC is awkward (p. 130)
- [[cliff-walking]] — Sarsa safer online than Q-learning (p. 132)
- [[maximization-bias-mdp]] — Q-learning favors *left* wrongly; Double Q-learning does not (p. 134–135)
- [[tic-tac-toe-afterstates]] — different position–move pairs, same afterposition (p. 137)

## Bridges (candidates)
- [structural-analogy] TD error $\delta_t$ ↔ control theory: error signal — both are a difference between a current value and a better reference, used to correct the estimate.
- [structural-analogy] TD(0) predict-then-correct from one-step data ↔ Kalman filter: predict, then correct — an estimate is corrected by a new observation.
- [structural-analogy] Q-learning's max backup ↔ Bellman equation / value iteration — a sampled version of the optimality backup.
- [metaphor] Certainty equivalence in batch TD ↔ adaptive control: certainty-equivalence design — the text says the term comes from there (p. 139).

## Questions this raises
- When is learning toward a bootstrapped estimate worse than waiting for the real return, for example if $V$ is badly wrong at the start?
- Why is TD usually faster than MC in practice, yet no one has proved it? What formal question would capture "faster" (p. 124)?
- How do the n-step methods of Chapter 7 interpolate between the one-step TD target and the MC target?
- How should the $\varepsilon$ schedule or $\alpha$ be chosen so that Sarsa both stays safe online and converges to the optimal policy?

## Exercises worth doing
- Ex. 6.1 (p. 121) — redo (6.6) when $V$ changes during the episode, to see the extra term — difficulty: medium
- Ex. 6.3 (p. 126) — read the random-walk results to infer what the first episode did and by how much $V(A)$ changed — difficulty: easy
- Ex. 6.8 (p. 129) — action-value version of the TD-error identity (6.6) — difficulty: easy
- Ex. 6.12 (p. 132) — is Q-learning with greedy actions exactly Sarsa? — difficulty: medium
- Ex. 6.9 / 6.10 (p. 131) — programming: windy gridworld with king's moves, then stochastic wind — difficulty: medium

## Reading notes
- Printed page = pdf − 22 (pdf 141 = printed 119).
- The text layer of pdf 155 (printed 133) is jumbled with fragments of another paper (van Seijen et al. figure and text). The page image shows only §6.6 and Figure 6.3. I used the image.
- Page images were provided only for pdf 142, 143, 145, 149, 152, 154, 155, 156, 157. For the other pages I used the text layer, where γ and other symbols are dropped. I reconstructed equations (6.1), (6.7), (6.8) and (6.10) and the Q-learning box title ("π ≈ π∗") from structure and the algorithm boxes.
- In the Double Q-learning box, the text layer reads "probabilility", a misprint for "probability" (pdf 158 text only).
- The α values of the curves in Example 6.2 are not legible in the text layer, so I do not report them.
