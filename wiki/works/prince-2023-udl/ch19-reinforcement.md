---
id: prince-2023-udl/ch19-reinforcement
work: prince-2023-udl
unit: "Chapter 19 — Reinforcement learning"
pages: 374–401
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Reinforcement learning (Prince, *Understanding Deep Learning*, ch. 19)

## L0 — One line
Reinforcement learning chooses actions in a Markov decision process so as to maximize expected discounted return, either by learning values (Bellman consistency, Q-learning, deep Q-networks) or by directly following gradients of a stochastic policy (policy gradients, actor-critic); offline RL can instead be treated as supervised sequence prediction (decision transformer).

## L1 — The gist (≤ 120 words)
How can an agent learn to act when rewards are sparse, delayed and stochastic, and it must balance exploring against exploiting? The chapter defines Markov decision processes, returns, policies, and state and action values. It shows that values obey self-consistency (Bellman) equations. These support tabular methods (dynamic programming, Monte Carlo, temporal-difference (TD) methods such as SARSA and Q-learning) and neural versions (fitted Q-learning, DQN, double DQN). Policy-gradient methods (REINFORCE, baselines, actor-critic) instead optimize a stochastic policy directly. Offline RL, for example the decision transformer, learns from logged data as sequence prediction. The Notes link RL to RLHF (learning from human feedback) for chatbots, trained with PPO (a policy-gradient method).

**Prerequisites:** expectation and conditional probability; gradient descent; softmax; a basic neural network (convolutions); transformer decoders only for section 19.7.

## L2 — Key ideas
- RL is hard because rewards are sparse, delayed (temporal credit assignment), stochastic, and need exploration versus exploitation (p. 374).
- An MDP adds actions to a Markov reward process; the agent follows a policy to maximize expected discounted return $G_t$ (pp. 375, 378–379).
- State value $v$ and action value $q$ are linked by Bellman equations, which say the values must be self-consistent (pp. 380–382).
- Tabular methods differ in what they know and when they update. Dynamic programming uses the known model, Monte Carlo averages whole episodes, and temporal difference (TD) methods (SARSA, Q-learning) bootstrap (update from other value estimates) while acting (pp. 382–385).
- Fitted Q-learning replaces the table with a network, but convergence is no longer guaranteed. DQN adds reward clipping, experience replay and a frozen target network, and double Q-learning reduces overestimation (pp. 386–389).
- Policy gradients ascend $\mathbb{E}[r[\tau]]$. The likelihood-ratio identity and the log of the trajectory probability remove the dynamics from the update. Baselines that do not depend on the actions leave the expected update unchanged and can reduce variance (pp. 389–394).
- Actor-critic is TD policy gradient. A critic network $v[s,\phi]$ replaces the Monte Carlo return (p. 394).
- Offline RL can be cast as supervised sequence prediction using returns-to-go (the remaining rewards in the episode) (decision transformer) (pp. 395–396).

## L3 — Walkthrough

### Introduction (p. 374)
RL is a sequential decision framework where agents act in an environment to maximize received reward. Examples are a game character, a robot and a trader. Chess shows four difficulties (p. 374).
- Sparse reward: only a +1/−1/0 at game end.
- Temporal credit assignment: the reward comes long after the causal action.
- Stochastic environment: a good action may only look lucky.
- Exploration–exploitation trade-off.

RL does not necessarily require deep learning, but state-of-the-art systems often use deep networks to encode the environment (p. 374).

### 19.1 Markov decision processes, returns, policies (pp. 374–378)
**19.1.1 Markov process.** The world is always in one of a set of states. "Markov" means the next state depends only on the current one, via transition probabilities $Pr(s_{t+1}|s_t)$ (p. 375). Figure 19.1: a penguin on a 16-cell icy grid has equal probability of moving to each adjacent cell (25% to each of four neighbours from cell 6) (p. 375).

**19.1.2 Markov reward process.** This adds rewards $Pr(r_{t+1}|s_t)$ and a discount factor $\gamma\in(0,1]$. The return is (p. 375):
$$G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}.\tag{19.1}$$
With $\gamma<1$, nearer rewards count more (p. 375). Figure 19.2 uses $\gamma=0.9$. The returns along the trajectory rise as the penguin nears the fish: $G_1=1.19$, $G_2=1.31$, $G_3=1.47$ (p. 376).

**19.1.3 MDP.** Actions $a_t$ are added. Transitions and rewards become $Pr(s_{t+1}|s_t,a_t)$ and $Pr(r_{t+1}|s_t,a_t)$. The entity that performs the actions is the agent (p. 378). In Figure 19.3 the penguin moves as intended with 50% probability and otherwise slides to another adjacent cell (p. 376).

**19.1.4 POMDP.** The state is hidden. The agent gets an observation $o_t\sim Pr(o_t|s_t)$ that fits some states better than others but does not identify the state uniquely (p. 378). In Figure 19.4, states three and nine look identical to the penguin, but moving right leads to −2 in one and +3 in the other (p. 377).

**19.1.5 Policy.** A policy $\pi[a|s]$ is stochastic (a distribution over actions) or deterministic (probability one for a single action). A stationary policy depends only on the state; a non-stationary one also depends on time (p. 378). The agent–environment loop (Figure 19.6): the agent picks $a_t$ from $s_t$; the environment returns $s_{t+1}$ and $r_{t+1}$ (p. 378).

### 19.2 Expected return (pp. 378–382)
**19.2.1 Values.** In general, sequences differ on every run because policy, transitions and rewards are all stochastic (pp. 378–379).
$$v[s_t|\pi]=\mathbb{E}\big[G_t\,|\,s_t,\pi\big]\tag{19.2}$$
$$q[s_t,a_t|\pi]=\mathbb{E}\big[G_t\,|\,s_t,a_t,\pi\big]\tag{19.3}$$
The action value $q$ links future rewards to current actions, which resolves temporal credit assignment (p. 379).

**19.2.2 Optimal policy.** For MDPs (but not POMDPs) there is always a deterministic, stationary policy that maximizes the value of every state (p. 380).
$$v^*[s_t]=\max_\pi\mathbb{E}[G_t|s_t,\pi]\tag{19.4}$$
$$q^*[s_t,a_t]=\max_\pi\mathbb{E}[G_t|s_t,a_t,\pi]\tag{19.5}$$
$$\pi[a_t|s_t]\leftarrow\operatorname*{argmax}_{a_t}\,q^*[s_t,a_t]\tag{19.6}$$
(The arrow means set the chosen action's probability to one, others to zero; footnote 1, p. 380.)

**19.2.3 Bellman equations.** From now on the author writes $v[s_t]$, $q[s_t,a_t]$ for the values under $\pi$, and assumes deterministic rewards $r[s_t,a_t]$ (p. 380, footnotes 2–3).
$$v[s_t]=\sum_{a_t}\pi[a_t|s_t]\,q[s_t,a_t]\tag{19.7}$$
$$q[s_t,a_t]=r[s_t,a_t]+\gamma\sum_{s_{t+1}}Pr(s_{t+1}|s_t,a_t)\,v[s_{t+1}]\tag{19.8}$$
Substituting 19.8 into 19.7 and 19.7 into 19.8 gives (pp. 380–382):
$$v[s_t]=\sum_{a_t}\pi[a_t|s_t]\Big(r[s_t,a_t]+\gamma\sum_{s_{t+1}}Pr(s_{t+1}|s_t,a_t)v[s_{t+1}]\Big)\tag{19.9}$$
$$q[s_t,a_t]=r[s_t,a_t]+\gamma\sum_{s_{t+1}}Pr(s_{t+1}|s_t,a_t)\Big(\sum_{a_{t+1}}\pi[a_{t+1}|s_{t+1}]\,q[s_{t+1},a_{t+1}]\Big)\tag{19.10}$$
These are the Bellman equations. Values must be self-consistent, so updating one value ripples to the others (p. 382).

*Intuition note:* A state's value is the policy-weighted average of its actions' values. An action's value is its reward plus the discounted value of where it leads. Each value is defined by its neighbours, so updating one value ripples to the others.

### 19.3 Tabular reinforcement learning (pp. 382–385)
Tabular methods avoid function approximation. **Model-based** methods use the transition matrix and rewards (known, or estimated from trajectories). If known, dynamic programming solves it (p. 382). **Model-free** methods assume these are unknown. They are either *value estimation* (estimate $q$, then take the greedy action) or *policy estimation* (gradient descent on the policy directly). Within each family, Monte Carlo methods simulate many trajectories, while TD methods update during the episode (p. 382). Terms (footnote 5): a trajectory is an observed sequence, a rollout a simulated one, and an episode runs from an initial to a terminal state (p. 382).

**19.3.1 Dynamic programming** (perfect knowledge of the MDP; p. 383). Initialize $v[s]$ (usually zero) and a deterministic policy, then alternate:
$$v[s_t]\leftarrow\sum_{a_t}\pi[a_t|s_t]\Big(r[s_t,a_t]+\gamma\sum_{s_{t+1}}Pr(s_{t+1}|s_t,a_t)v[s_{t+1}]\Big)\tag{19.11}$$
$$\pi[a_t|s_t]\leftarrow\operatorname*{argmax}_{a_t}\Big[r[s_t,a_t]+\gamma\sum_{s_{t+1}}Pr(s_{t+1}|s_t,a_t)v[s_{t+1}]\Big]\tag{19.12}$$
Eq. 19.11 (policy evaluation) uses the successor values; this is bootstrapping. Eq. 19.12 (policy improvement) is greedy and is guaranteed to improve the policy by the policy improvement theorem. Iterate until the policy converges (p. 383; Figure 19.10 shows the penguin learning to avoid holes). Variants (p. 384):
- Policy iteration: evaluate to convergence before improving.
- Value iteration: one sweep, then improve.
- Asynchronous DP: update an arbitrary subset of states in place.

**19.3.2 Monte Carlo** (no model needed; p. 384). Run episodes from a state-action pair, then follow the current policy. Estimate $q[s,a]$ as the average empirical return after each occurrence of the pair. Then update:
$$\pi[a|s]\leftarrow\operatorname*{argmax}_a\,q[s,a].\tag{19.13}$$
This is *on-policy*; the value of untried actions cannot be estimated, and nothing encourages exploring them (pp. 384–385). Fixes:
- Exploring starts: start episodes from all state-action pairs. This is impractical for large state spaces or uncontrollable starts.
- $\epsilon$-greedy: a random action with probability $\epsilon$, the best action with $1-\epsilon$. An on-policy method then finds the best policy *within* the $\epsilon$-greedy family, which will not generally be the best overall.

*Off-policy* methods learn a target policy $\pi$ from episodes of a different behavior policy $\pi'$. Typically the target is deterministic and the behavior policy stochastic. Some use importance sampling; others, like Q-learning, use the greedy action's value even if it was not chosen (p. 385).

**19.3.3 Temporal difference.** TD combines bootstrapping and sampling and updates while the agent traverses the MDP (p. 385). With learning rate $\alpha\in\mathbb{R}^+$:
$$q[s_t,a_t]\leftarrow q[s_t,a_t]+\alpha\big(r[s_t,a_t]+\gamma\,q[s_{t+1},a_{t+1}]-q[s_t,a_t]\big)\quad\text{(SARSA, on-policy)}\tag{19.14}$$
$$q[s_t,a_t]\leftarrow q[s_t,a_t]+\alpha\big(r[s_t,a_t]+\gamma\max_a q[s_{t+1},a]-q[s_t,a_t]\big)\quad\text{(Q-learning, off-policy)}\tag{19.15}$$
The bracket is the TD error. In Q-learning the action taken comes from a behavior policy $\pi'$. The policy is updated by taking the max (19.13). The updates can be shown to be contraction mappings, so the values converge assuming every state-action pair is visited infinitely often (p. 385). Worked numbers (Figure 19.12, $\gamma=0.9$, $\alpha=0.1$, reward 0): $1.12\leftarrow1.20+0.1(0.0+0.9\cdot\max[-0.23,0.43,-1.97,-1.25]-1.20)$ (p. 386).

*Intuition note:* TD methods nudge each estimate toward "reward now plus discounted estimate next" without waiting for the episode to end. SARSA uses the next action actually taken; Q-learning uses the best next action.

### 19.4 Fitted Q-learning (pp. 386–389)
Tables are impractical because the state space is huge (chess: more than $10^{40}$ legal states; p. 386). Replace $q[s_t,a_t]$ by a model $q[\mathbf{s}_t,a_t,\boldsymbol\phi]$ on a state vector:
$$L[\boldsymbol\phi]=\Big(r[\mathbf s_t,a_t]+\gamma\max_a q[\mathbf s_{t+1},a,\boldsymbol\phi]-q[\mathbf s_t,a_t,\boldsymbol\phi]\Big)^2\tag{19.16}$$
$$\boldsymbol\phi\leftarrow\boldsymbol\phi+\alpha\Big(r[\mathbf s_t,a_t]+\gamma\max_a q[\mathbf s_{t+1},a,\boldsymbol\phi]-q[\mathbf s_t,a_t,\boldsymbol\phi]\Big)\frac{\partial q[\mathbf s_t,a_t,\boldsymbol\phi]}{\partial\boldsymbol\phi}\tag{19.17}$$
Convergence is no longer guaranteed. A parameter change can alter both the target and the prediction (p. 386).

**19.4.1 DQN for Atari** (pp. 387–388). In practice the network takes the state and outputs a value for each action. Input frames are reshaped from 220×160 to 84×84 grayscale. Four frames are stacked, because velocity is not visible in one frame. Shapes in Figure 19.14: $84{\times}84{\times}4\to$ conv 8×8 stride 4 $\to20{\times}20{\times}16\to$ conv 4×4 stride 2 $\to9{\times}9{\times}32\to$ FC 256 $\to$ FC 18 (one value per action). Modifications:
- Reward clipping to −1/+1, which allows the same learning rate across games.
- Experience replay: store recent tuples in a buffer and sample batches randomly. This reuses data and reduces correlation between adjacent frames.
- A fixed target network $\boldsymbol\phi^-$, updated only periodically:
$$\boldsymbol\phi\leftarrow\boldsymbol\phi+\alpha\Big(r[\mathbf s_t,a_t]+\gamma\max_a q[\mathbf s_{t+1},a,\boldsymbol\phi^-]-q[\mathbf s_t,a_t,\boldsymbol\phi]\Big)\frac{\partial q[\mathbf s_t,a_t,\boldsymbol\phi]}{\partial\boldsymbol\phi}\tag{19.18}$$
The network no longer chases a moving target. With these tricks and $\epsilon$-greedy, DQN performed comparably to a professional game tester across 49 games with one architecture, each trained separately. Learning took about 38 full days of experience per game. It exceeded humans in some games and barely progressed on "Montezuma's Revenge" (sparse rewards, multiple screens) (p. 388).

**19.4.2 Double Q-learning.** The max in
$$q[s_t,a_t]\leftarrow q[s_t,a_t]+\alpha\big(r[s_t,a_t]+\gamma\max_a q[s_{t+1},a]-q[s_t,a_t]\big)\tag{19.19}$$
biases estimates upward. Example: of two actions with equal average reward, one stochastic and one deterministic, the stochastic one exceeds its average about half the time and gets selected by the max. Random network errors act similarly (p. 388). The cause is that one network both selects and evaluates. The fix trains two models, each choosing the action and the other evaluating it (p. 389):
$$\begin{aligned}q_1[s_t,a_t]&\leftarrow q_1[s_t,a_t]+\alpha\Big(r[s_t,a_t]+\gamma\,q_2\big[s_{t+1},\operatorname*{argmax}_a q_1[s_{t+1},a]\big]-q_1[s_t,a_t]\Big)\\ q_2[s_t,a_t]&\leftarrow q_2[s_t,a_t]+\alpha\Big(r[s_t,a_t]+\gamma\,q_1\big[s_{t+1},\operatorname*{argmax}_a q_2[s_{t+1},a]\big]-q_2[s_t,a_t]\Big)\end{aligned}\tag{19.20}$$
New tuples are randomly assigned to update one model or the other. Double DQN uses networks $q[\cdot,\boldsymbol\phi_1]$, $q[\cdot,\boldsymbol\phi_2]$ with the same cross-structure (eq. 19.21, p. 389).

*Intuition note:* Taking a max over noisy estimates picks the lucky ones. Letting a second model score the chosen action helps prevent that bias.

### 19.5 Policy gradient methods (pp. 389–394)
Policy-based methods learn a stochastic policy $\pi[a_t|\mathbf s_t,\boldsymbol\theta]$ directly. MDPs always have an optimal deterministic policy, but the author gives three reasons for a stochastic one (p. 389):
- It helps exploration.
- The loss changes smoothly with the parameters, so gradient descent works even though rewards are discrete (like maximum likelihood in classification).
- The MDP assumption is often wrong. With two identical-looking locations, a stochastic policy can try different actions until the ambiguity resolves.

**19.5.1 Derivation** (pp. 390–392). Trajectory probability:
$$Pr(\boldsymbol\tau|\boldsymbol\theta)=Pr(\mathbf s_1)\prod_{t=1}^{T}\pi[a_t|\mathbf s_t,\boldsymbol\theta]\,Pr(\mathbf s_{t+1}|\mathbf s_t,a_t).\tag{19.22}$$
Objective, with $r[\boldsymbol\tau]$ the sum of all rewards along $\boldsymbol\tau$:
$$\boldsymbol\theta=\operatorname*{argmax}_{\boldsymbol\theta}\Big[\mathbb{E}_{\boldsymbol\tau}\big[r[\boldsymbol\tau]\big]\Big]=\operatorname*{argmax}_{\boldsymbol\theta}\Big[\int Pr(\boldsymbol\tau|\boldsymbol\theta)\,r[\boldsymbol\tau]\,d\boldsymbol\tau\Big]\tag{19.23}$$
Gradient ascent:
$$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\frac{\partial}{\partial\boldsymbol\theta}\int Pr(\boldsymbol\tau|\boldsymbol\theta)r[\boldsymbol\tau]d\boldsymbol\tau=\boldsymbol\theta+\alpha\int\frac{\partial Pr(\boldsymbol\tau|\boldsymbol\theta)}{\partial\boldsymbol\theta}r[\boldsymbol\tau]d\boldsymbol\tau\tag{19.24}$$
Multiply and divide by $Pr(\boldsymbol\tau|\boldsymbol\theta)$, then replace the integral by a sample average over $I$ observed trajectories:
$$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\int Pr(\boldsymbol\tau|\boldsymbol\theta)\frac{1}{Pr(\boldsymbol\tau|\boldsymbol\theta)}\frac{\partial Pr(\boldsymbol\tau|\boldsymbol\theta)}{\partial\boldsymbol\theta}r[\boldsymbol\tau]d\boldsymbol\tau\approx\boldsymbol\theta+\alpha\frac1I\sum_{i=1}^I\frac{1}{Pr(\boldsymbol\tau_i|\boldsymbol\theta)}\frac{\partial Pr(\boldsymbol\tau_i|\boldsymbol\theta)}{\partial\boldsymbol\theta}r[\boldsymbol\tau_i]\tag{19.25}$$
Reading: raise the likelihood of each observed trajectory in proportion to its return, normalized by how often it is observed. The largest updates come from uncommon trajectories with large returns (p. 390; Figure 19.15). Using the likelihood ratio identity
$$\frac{\partial\log f[z]}{\partial z}=\frac{1}{f[z]}\frac{\partial f[z]}{\partial z}\tag{19.26}$$
$$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\frac1I\sum_{i=1}^I\frac{\partial\log Pr(\boldsymbol\tau_i|\boldsymbol\theta)}{\partial\boldsymbol\theta}r[\boldsymbol\tau_i]\tag{19.27}$$
$$\log Pr(\boldsymbol\tau|\boldsymbol\theta)=\log Pr(\mathbf s_1)+\sum_{t=1}^T\log\pi[a_t|\mathbf s_t,\boldsymbol\theta]+\sum_{t=1}^T\log Pr(\mathbf s_{t+1}|\mathbf s_t,a_t)\tag{19.28}$$
Only the middle term depends on $\boldsymbol\theta$:
$$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\frac1I\sum_{i=1}^I\sum_{t=1}^T\frac{\partial\log\pi[a_{it}|\mathbf s_{it},\boldsymbol\theta]}{\partial\boldsymbol\theta}r[\boldsymbol\tau_i]\tag{19.29}$$
The transition terms vanish, so this update does not assume a Markov time evolution (p. 391). Split the return:
$$r[\boldsymbol\tau_i]=\sum_{t=1}^Tr_{i,t+1}=\sum_{k=1}^{t}r_{i,k+1}+\sum_{k=t}^{T}r_{i,k+1}\tag{19.30}$$
The author states it can (non-obviously) be proved that the rewards before $t$ do not affect the update at $t$ (p. 392), giving
$$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\frac1I\sum_{i=1}^I\sum_{t=1}^T\frac{\partial\log\pi[a_{it}|\mathbf s_{it},\boldsymbol\theta]}{\partial\boldsymbol\theta}\sum_{k=t}^{T}r_{i,k+1}.\tag{19.31}$$
*Intuition note:* Make actions that were followed by high reward more probable, and weight each step only by rewards that came after it. The unknown dynamics drop out because only the policy's log-probability depends on $\boldsymbol\theta$.

**19.5.2 REINFORCE** (p. 392). This is a Monte Carlo method with discounting. A network with a softmax output gives the action distribution, which is sampled. For each episode $i$ and step $t$:
$$r[\boldsymbol\tau_{it}]=\sum_{k=t+1}^{T}\gamma^{k-t-1}r_{i,k}\tag{19.32}$$
$$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\frac{\partial\log\pi_{a_{it}}[\mathbf s_{it},\boldsymbol\theta]}{\partial\boldsymbol\theta}r[\boldsymbol\tau_{it}]\qquad\forall\,i,t\tag{19.33}$$

**19.5.3 Baselines** (pp. 392–393). Policy gradients have high variance. Subtract a baseline $b$:
$$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\frac1I\sum_{i=1}^I\sum_{t=1}^T\frac{\partial\log\pi_{a_{it}}[\mathbf s_{it},\boldsymbol\theta]}{\partial\boldsymbol\theta}\big(r[\boldsymbol\tau_{it}]-b\big)\tag{19.34}$$
As long as $b$ does not depend on the actions,
$$\mathbb{E}_{\boldsymbol\tau}\Big[\sum_{t=1}^{T-1}\frac{\partial\log\pi_{a_{it}}[\mathbf s_{it},\boldsymbol\theta]}{\partial\boldsymbol\theta}\cdot b\Big]=0,\tag{19.35}$$
so the expected update is unchanged. If $b$ co-varies with irrelevant factors that add uncertainty, subtracting it reduces variance (Figure 19.16). This is a special case of control variates (p. 393). The variance-minimizing $b$ (write the variance, differentiate in $b$, set to zero) and the usual approximation are:
$$b=\sum_i\frac{\sum_{t=1}^T\big(\partial\log\pi_{a_{it}}[\mathbf s_{it},\boldsymbol\theta]/\partial\boldsymbol\theta\big)^2r[\boldsymbol\tau_{it}]}{\sum_{t=1}^T\big(\partial\log\pi_{a_{it}}[\mathbf s_{it},\boldsymbol\theta]/\partial\boldsymbol\theta\big)^2}\tag{19.36}$$
$$b=\frac1I\sum_ir[\boldsymbol\tau_i]\tag{19.37}$$
The baseline removes variance that arises when all returns are high only because the trajectories pass through high-return states whatever the actions (p. 393).

**19.5.4 State-dependent baselines** (p. 394). Use $b[\mathbf s_{it}]$:
$$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\frac1I\sum_{i}\sum_{t}\frac{\partial\log\pi_{a_{it}}[\mathbf s_{it},\boldsymbol\theta]}{\partial\boldsymbol\theta}\big(r[\boldsymbol\tau_{it}]-b[\mathbf s_{it}]\big)\tag{19.38}$$
A sensible choice is the state value $v[\mathbf s]$. The difference is then the advantage estimate. A network $b[\mathbf s]=v[\mathbf s,\boldsymbol\phi]$ is fitted by least squares:
$$L[\boldsymbol\phi]=\sum_{i=1}^I\sum_{t=1}^T\Big(v[\mathbf s_{it},\boldsymbol\phi]-\sum_{j=t}^Tr_{i,j+1}\Big)^2\tag{19.39}$$

### 19.6 Actor-critic methods (pp. 394–395)
These are TD policy-gradient methods. They can update the policy at each step, whereas REINFORCE must wait for episodes to finish (p. 394). The future return is approximated by the current reward plus the discounted next-state value from a second network:
$$r[\boldsymbol\tau_{it}]\approx r_{i,t+1}+\gamma\,v[\mathbf s_{i,t+1},\boldsymbol\phi]\tag{19.40}$$
$$\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\frac1I\sum_i\sum_t\frac{\partial\log Pr(a_{it}|\mathbf s_{it},\boldsymbol\theta)}{\partial\boldsymbol\theta}\big(r_{i,t+1}+\gamma v[\mathbf s_{i,t+1},\boldsymbol\phi]-v[\mathbf s_{i,t},\boldsymbol\phi]\big)\tag{19.41}$$
$$L[\boldsymbol\phi]=\sum_{i=1}^I\sum_{t=1}^T\big(r_{i,t+1}+\gamma v[\mathbf s_{i,t+1},\boldsymbol\phi]-v[\mathbf s_{i,t},\boldsymbol\phi]\big)^2\tag{19.42}$$
The policy network is the *actor*; the value network is the *critic*. One network often serves both, with two sets of outputs. Per-step updates are rarely done in practice; the agent usually collects a batch over many steps first (pp. 394–395).

### 19.7 Offline reinforcement learning (pp. 395–396)
Offline (batch) RL is used when exploring is dangerous (autonomous vehicles) or costly (trading). It learns from logged sequences $s_1,a_1,r_2,\dots$ without interacting. It differs from imitation learning, which (i) has no rewards and (ii) tries to copy the historical agent rather than improve on it (p. 395). The **decision transformer** treats this as sequence prediction with a transformer decoder (p. 396).
- The reward $r_t$ is replaced by the return-to-go $R_{t:T}=\sum_{t'=t}^Tr_{t'}$.
- States, actions and returns-to-go get learned fixed-size embeddings. For Atari the state encoder may be a CNN like Figure 19.14.
- Training uses masked self-attention and position embeddings; the network predicts the next action.
- At inference, start with the desired total return and decrement it as rewards arrive.
- It can be fine-tuned online. It replaces most RL machinery and its instability with supervised learning. Large contexts may make temporal credit assignment more tractable.

### 19.8 Summary (p. 396)
Restates the chapter: tabular methods (DP, MC, TD), deep Q-learning (human-level Atari), policy gradients (stochastic policies, noisy updates), and offline RL with the decision transformer (p. 396).

### Notes (pp. 397–399) — brief
- Landmarks: DQN on Atari, AlphaGo, a Dota 2 system, Cicero (Diplomacy), AlphaTensor (faster matrix multiplication) (p. 397).
- History: Q-learning convergence rests on the Bellman operator being a contraction (Banach); REINFORCE and actor-critic are credited to named authors (pp. 397–398).
- The "deadly triad" (bootstrapping, off-policy, function approximation) can destabilize deep Q-learning. Refinements listed: prioritized replay, dueling, noisy and distributional DQN, Rainbow. Double DQN's efficacy "has since been questioned" (pp. 397–398).
- One cited claim: the value baseline may mainly reduce update aggressiveness rather than variance (Mei et al., 2022) (p. 398).
- Trust-region methods (natural gradient, TRPO, PPO) moderate large policy updates (p. 398). Actor-critic extensions: k-step estimators (as $k$ grows, variance rises and bias falls), GAE, A3C, soft actor-critic (pp. 398–399).
- Offline RL: distributional shift causes over-optimistic values. Conservative Q-learning is a remedy (p. 399).
- **RLHF** (p. 399): fine-tune a transformer decoder on human-written responses; train a reward model on human preference rankings; then train the chatbot to produce high reward using PPO. Plain gradient descent cannot be used because derivatives cannot pass through sampling of the output.

## Toy example (ours, not from the text)
Deterministic MDP, $\gamma=0.9$. States $s_1,s_2$, plus an end state with value 0 (our convention). From $s_2$ the only action "exit" gives reward 10 and ends. From $s_1$: action $a$ goes to $s_2$ with reward 0; action $b$ exits with reward 5.
- Bellman (19.8): $v[s_2]=10+0.9\cdot0=10$. $q[s_1,a]=0+0.9\cdot10=9$. $q[s_1,b]=5+0=5$.
- Policy $\pi[a|s_1]=\pi[b|s_1]=0.5$ in (19.7): $v[s_1]=0.5\cdot9+0.5\cdot5=7$.
- Improvement (19.6/19.12): $9>5$, so choose $a$. Then $v[s_1]=9$. Check by return: rewards 0 then 10 give $G=0+0.9\cdot10=9$.
- Q-learning (19.15), all $q=0$, $\alpha=0.5$. Observe $(s_2,\text{exit},10)$: $q[s_2,\text{exit}]\leftarrow0+0.5(10+0-0)=5$. Observe $(s_1,a,0,s_2)$: $q[s_1,a]\leftarrow0+0.5(0+0.9\cdot5-0)=2.25$. Repeated visits move both toward 10 and 9.

## Concepts
- [[markov-decision-process]] (new) — states, actions, transition and reward distributions; Markov means the next state depends on the current state and action only (pp. 375, 378)
- [[return-discounted]] (new) — $G_t=\sum_k\gamma^kr_{t+k+1}$; near rewards weigh more when $\gamma<1$ (p. 375)
- [[policy-rl]] (new) — rule giving action probabilities per state; stochastic or deterministic (p. 378)
- [[state-action-value]] (new) — $v$ and $q$: expected return from a state or state-action pair under a policy (p. 379)
- [[bellman-equations]] (new) — self-consistency relations linking values at $t$ and $t+1$ (pp. 380–382)
- [[bootstrapping]] (new) — updating a value from other current value estimates (p. 383)
- [[q-learning]] (new) — off-policy TD update using the max next action value (p. 385)
- [[experience-replay]] (new) — sampling stored past tuples at random to form batches (pp. 387–388)
- [[policy-gradient]] (new) — gradient ascent on expected return via $\nabla\log\pi$ (pp. 389–391)
- [[baseline-variance-reduction]] (new) — subtracting an action-independent term to cut variance, leaving the expected update unchanged (p. 393)
- [[actor-critic]] (new) — policy network (actor) plus value network (critic), updated by TD (p. 394)
- [[offline-rl]] (new) — learning from logged data without interaction; the decision transformer is one method (pp. 395–396)
- [[softmax]] — turns network outputs into action probabilities in REINFORCE (p. 392)
- [[RLHF]] — reward model plus PPO training of chatbots, as described in the Notes (p. 399)
- [[reward model]] — transformer scoring a prompt-response pair from human preferences (p. 399)

## Canonical instances
- [[penguin-ice-grid]] — running example for Markov processes, MDPs, values, DP, MC and Q-learning (pp. 375–386)
- [[dqn-atari]] — a CNN on four stacked frames predicts 18 action values; replay and a target network stabilize it (pp. 387–388)
- [[decision-transformer]] — offline RL as next-action prediction from states, actions and returns-to-go (pp. 395–396)
- [[instructgpt-rlhf-pipeline]] — fine-tune, reward model, PPO (p. 399)

## Bridges (candidates)
- [structural-analogy] REINFORCE with $\partial\log\pi$ weighted by return ↔ llm: maximum-likelihood next-token training, but weighted by reward and using sampled sequences (the text compares policy-gradient smoothness to maximum likelihood in classification, p. 389).
- [same-math] Softmax policy for discrete actions (p. 392) ↔ llm: softmax over vocabulary logits.
- [structural-analogy] Decision transformer (return-conditioned action prediction) ↔ llm: decoder-only autoregressive models with conditioning tokens.
- [structural-analogy] RLHF's reward model + PPO (p. 399) ↔ llm: Bradley–Terry reward model and KL-penalised policy optimization (canon link; not stated in this unit).

## Questions this raises
- Why can the value baseline be non-constant ($b[\mathbf s]$) without biasing the update, and when does it not help?
- How does deep Q-learning's instability (the three ingredients named in the Notes) show up in practice, and which fix matters most?
- For chatbots, what is lost by using PPO on a learned reward model instead of direct supervised learning?
- How reliable is "desired total return" conditioning in the decision transformer at test time?

## Exercises worth doing
- Ex. 19.1 (p. 400) — compute discounted returns along a trajectory — difficulty: easy
- Ex. 19.3 (p. 400) — verify two iterations of policy evaluation and improvement in Figure 19.10 — difficulty: medium
- Ex. 19.4 (p. 400) — Boltzmann policy and temperature as exploration–exploitation control — difficulty: easy
- Ex. 19.5 (p. 400) — Q-learning update as a contraction mapping — difficulty: hard
- Ex. 19.6 (p. 401) — baselines leave the expected policy gradient unchanged — difficulty: medium
- Ex. 19.8 (p. 401) — derive the variance-minimizing baseline — difficulty: hard

## Reading notes
- Printed page = pdf − 14. Source is a draft (footer "Draft: please send errata").
- Section 19.4.1 text says the network has "three convolutional layers followed by a fully connected layer", but Figure 19.14 and its caption show two convolutions and two fully connected layers; I followed the figure.
- Eq. 19.20 labels the models $q_1[s_t,a_t,\pi_1]$, $q_2[s_t,a_t,\pi_2]$; the later DQN version uses $\boldsymbol\phi_1,\boldsymbol\phi_2$, so $\pi$ appears to be a misprint.
- Eq. 19.35 sums to $T-1$, while related equations sum to $T$.
- Problem 19.8 (eq. 19.52) defines $r[\boldsymbol\tau]=\sum_{k=t}^Tr_k$, which depends on $t$ although written without it.

- The Notes (pp. 397–399) are summarized only briefly. Solutions are not printed in the unit; none are given here.
