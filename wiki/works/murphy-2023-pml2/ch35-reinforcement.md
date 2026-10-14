---
id: murphy-2023-pml2/ch35-reinforcement
work: murphy-2023-pml2
unit: "35 Reinforcement learning"
pages: 1145–1184
fields: [bayesian]
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
# Reinforcement learning (Murphy & Li, Ch. 35)

## L0 — One line
An agent that does not know its environment can learn a reward-maximizing policy by bootstrapped value updates, policy gradients, or a learned model. Learning from another policy's data needs correction for distribution mismatch, and control can also be recast as probabilistic inference.

## L1 — The gist (≤ 120 words)
How can an agent that interacts with an unknown environment learn a policy that maximizes expected discounted reward? The chapter covers three families. Value-based methods are Monte Carlo, temporal-difference (TD) learning, SARSA, Q-learning and deep Q-networks (DQN). Policy-based methods are REINFORCE, actor-critic, trust-region and proximal policy optimization (TRPO/PPO) and deterministic gradients. Model-based methods plan with a learned model. It then treats learning from data collected by a different policy: importance sampling, doubly robust estimators, the curse of horizon and the deadly triad. Finally it recasts control as inference (maximum-entropy RL, imitation learning). It matters because exploration, bias–variance trade-offs and distribution mismatch recur across the methods of this chapter.

**Prerequisites:** MDPs, value functions $V,Q$ and Bellman equations (Ch. 34); gradients and the score-function (log-derivative) estimator; KL divergence; importance sampling; basic ideas of VAEs and Gaussian processes for §35.4.

## L2 — Key ideas (5–10 bullets)
- **Bootstrapping.** TD learning updates a value estimate toward a target built from the estimate itself. This makes it efficient and online, but it may diverge with function approximation (pp. 1147, 1151, 1159).
- **SARSA vs Q-learning.** SARSA is on-policy. Q-learning replaces the sampled next action by a greedy one and learns $Q_*$ off-policy (pp. 1153–1154).
- **Policy gradient theorem.** $\nabla_\theta J$ is an expectation of $\nabla\log\pi_\theta\cdot Q$ under the discounted state distribution. A baseline or critic reduces variance (pp. 1157–1160).
- **Safe policy steps.** Lower bounds on $J(\pi')-J(\pi)$ lead to conservative policy iteration (CPI), TRPO (trust-region policy optimization, KL constraint) and PPO (proximal policy optimization, clipping) (pp. 1160–1162).
- **Model-based RL.** A learned model can improve sample efficiency. It is used for planning (model predictive control, MPC; Monte Carlo tree search, MCTS), for synthetic data, or inside latent models (PILCO, world models, PlaNet, Dreamer). Model error under distribution shift is the main challenge (pp. 1164–1171).
- **Off-policy estimation.** Direct, IS, doubly robust and behavior-regularized methods exist. Trajectory-level IS has variance growing exponentially in horizon, so one approach corrects state-action distributions instead (DualDICE) (pp. 1172–1176).
- **Deadly triad.** Off-policy data, bootstrapping and function approximation together can make value learning diverge (pp. 1176–1177).
- **Control as inference.** Optimality variables turn policy search into KL minimization to a trajectory posterior. This gives maximum-entropy RL, soft actor-critic (SAC) and soft Q-learning (pp. 1177–1180).
- **Imitation learning.** It uses behavior cloning, inverse RL with an energy-based model, or divergence matching of state-action distributions (pp. 1182–1183).

## L3 — Walkthrough

### 35.1 Introduction (pp. 1145–1149)
**Setup.** A trajectory is $\tau=(s_0,a_0,r_0,s_1,\dots,s_T)$. The agent maximizes the expected discounted return $G_0\triangleq\sum_{t=0}^{T-1}\gamma^t r_t$ with $\gamma\in[0,1]$ (p. 1145). The authors maximize the expectation and mention conditional value at risk (CVaR, expected reward in the worst, say, 5% of samples) as an alternative for risk-sensitive uses (p. 1145). Known model parameters give *planning*. Unknown ones give *learning*. Model-free RL learns the policy directly from trajectories. Model-based RL first learns a model, then plans (p. 1145).

**Table 35.1** (p. 1146) lists what each method learns and whether it is on- or off-policy:
- SARSA: $Q(s,a)$, on-policy.
- Q-learning: $Q(s,a)$, off-policy.
- REINFORCE: $\pi(a|s)$, on-policy.
- A2C: $\pi(a|s),V(s)$, on-policy.
- TRPO/PPO: $\pi(a|s),A(s,a)$, on-policy.
- DDPG: $a=\pi(s),Q(s,a)$, off-policy.
- Soft actor-critic: $\pi(a|s),Q(s,a)$, off-policy.
- Model-based RL: $p(s'|s,a)$, off-policy.

**35.1.2 Value-based.** For a transition $(s,a,r,s')$ the TD error is $r+\gamma\max_{a'}Q_w(s',a')-Q_w(s,a)$. Its expectation is the Bellman error at $(s,a)$, so it is 0 on average if $Q_w=Q_*$. Otherwise it signals how to change $w$. Using a target computed from $Q_w$ itself is *bootstrapping*, not the statistical bootstrap (p. 1147).

**35.1.3 Policy search.** The objective $J(\pi_\theta)$ is an expectation whose distribution depends on $\theta$, so $\nabla$ and $\mathbb E$ cannot be swapped. The score-function estimator is used on Monte Carlo rollouts. Advantages of policy gradient:
- It provably converges to a local optimum for many common policy classes, whereas Q-learning may diverge under approximation.
- It handles continuous actions, since no $\arg\max_a Q$ is needed.

Its drawback is high variance. A learned baseline $V_w(s)$ or advantage $A_w(s,a)$ helps; these variants are *actor-critic* methods (actor $=\pi_\theta$, critic $=V_w$ or $A_w$) (p. 1147).

**35.1.4 Model-based.** Value-based and policy-search methods can be sample inefficient. In model-based RL one learns $p(s'|s,a)$ and $R(s,a)$ by supervised learning. Then one runs RL on synthetic experience or plans directly. Learning and planning are often interleaved (pp. 1147–1148).

**35.1.5 Exploration–exploitation** (pp. 1148–1150).
- *ε-greedy:* the greedy action with probability $1-\epsilon$, a random action with probability $\epsilon$. It is suboptimal because every action is explored with probability at least $\epsilon/|\mathcal A|$.
- *Boltzmann:* $\pi_\tau(a|s)=\dfrac{\exp(\hat R_t(s_t,a)/\tau)}{\sum_{a'}\exp(\hat R_t(s_t,a')/\tau)}$ (35.1). As $\tau\to0$ it becomes greedy. Larger $\tau$ is more uniform. Table 35.2 (p. 1149): with $\epsilon=0.1$, $\tau=1$ and two actions, ε-greedy jumps from (0.05, 0.95) to (0.95, 0.05) when the estimates cross. For $\hat R=(4.90,5.10)$ Boltzmann gives (0.45, 0.55), and for $(5.05,4.95)$ it gives (0.53, 0.48) (rounded in the table).
- *UCB / count-based:* add a bonus $\tilde r=r+\alpha/\sqrt{N_{s,a}}$ (35.2), $\alpha\ge0$ (MBIE-EB). Unlike bandits, transition uncertainty must also be handled (p. 1148).
- *Thompson sampling:* keep a posterior over reward and transition parameters. For finite MDPs a Dirichlet (conjugate) prior on the categorical transition model gives a posterior that is easy to compute and sample. UCB and Thompson methods have provable regret or PAC bounds, often under assumptions such as finite MDPs (p. 1149).
- *Bayes-adaptive MDP (BAMDP):* a POMDP whose belief state $b_t$ covers the reward and transition models.
  $$T^+(s_{t+1},b_{t+1}|s_t,b_t,a_t,r_t)=T^+(s_{t+1}|s_t,a_t,b_t)\,T^+(b_{t+1}|s_t,a_t,r_t,s_{t+1})\tag{35.3}$$
  $$=\mathbb E_{b_t}[T(s_{t+1}|s_t,a_t)]\times\mathbb I\big(b_{t+1}=p(R,T|h_{t+1})\big)\tag{35.4}$$
  $$R^+(r|s_t,b_t,a_t,s_{t+1},b_{t+1})=\mathbb E_{b_{t+1}}[R(s_t,a_t,s_{t+1})]\tag{35.5}$$
  Here $\mathbb E_{b_t}[T]$ is the posterior predictive over next states, and the new belief comes from Bayes' rule. This gives the Bayes-optimal trade-off. It can be solved for small problems but is intractable in general. Approximations include [KN09], Monte Carlo rollouts [GSD13], and a meta-learning method [Zin+20] that uses a VAE posterior over a task embedding as belief proxy (pp. 1149–1150).

*Intuition note.* Exploration costs reward now to gain information. The Bayes-adaptive view makes this exact by treating "what I believe" as part of the state, but the resulting problem is usually too big to solve.

### 35.2 Value-based RL (pp. 1150–1156)
**35.2.1 Monte Carlo.** $Q_\pi(s,a)=\mathbb E[G_t|s_t=s,a_t=a]$ is estimated by averaging discounted returns of rollouts. With policy iteration, $\pi_{k+1}(s)=\arg\max_aQ_k(s,a)$ is *Monte Carlo control*. In the tabular case every $(s,a)$ must be visited. With ε-greedy (on-policy) it converges to the optimal ε-soft policy, not the optimal policy. Importance sampling could fix this, but gradually reducing $\epsilon$ is simpler (p. 1150).

**35.2.2 TD learning.** MC has very high variance and needs episodes to finish. TD updates from single transitions toward a bootstrapped target (pp. 1150–1151):
$$V(s_t)\leftarrow V(s_t)+\eta\,[r_t+\gamma V(s_{t+1})-V(s_t)]\tag{35.6}$$
$$w\leftarrow w+\eta\,[r_t+\gamma V_w(s_{t+1})-V_w(s_t)]\nabla_wV_w(s_t)\tag{35.7}$$
The bracket is the TD error. Tabular TD (35.6) converges under proper conditions, but it may diverge under approximation (35.7). Equation (35.7) is not SGD on any objective, despite its form. DP also bootstraps but uses the full model. MC does not bootstrap (Fig. 35.2 contrasts MC, TD and DP backups).

*Intuition note.* TD nudges today's guess toward "reward now plus tomorrow's guess". It learns from every step, at the price of chasing a target that moves with the estimate.

**35.2.3 Eligibility traces / TD(λ)** (p. 1152).
$$G_{t:t+n}=r_t+\gamma r_{t+1}+\dots+\gamma^{n-1}r_{t+n-1}+\gamma^nV(s_{t+n})\tag{35.8}$$
$$V(s_t)\leftarrow V(s_t)+\eta[G_{t:t+n}-V(s_t)]\tag{35.9}$$
$$G^\lambda_t\triangleq(1-\lambda)\sum_{n=1}^\infty\lambda^{n-1}G_{t:t+n}\tag{35.10}$$
The factor $1-\lambda=(1+\lambda+\lambda^2+\cdots)^{-1}$ makes this a convex combination. $\lambda=0$ is standard TD and $\lambda=1$ is MC (Fig. 35.3). The geometric weights allow an efficient implementation with eligibility traces, though $G^\lambda_t$ has infinitely many terms.

**35.2.4 SARSA (on-policy).** With $a'\sim\pi(s')$ and $\pi$ greedy w.r.t. $Q$ (p. 1153):
$$Q(s,a)\leftarrow Q(s,a)+\eta[r+\gamma Q(s',a')-Q(s,a)]\tag{35.11}$$
For convergence to $Q_*$, every state-action pair must be visited infinitely often (tabular). A "greedy in the limit with infinite exploration" (GLIE) policy, e.g. ε-greedy with $\epsilon\to0$, suffices.

**35.2.5 Q-learning (off-policy).** Replace $a'$ by $\arg\max_bQ(s',b)$ (p. 1153):
$$Q(s,a)\leftarrow Q(s,a)+\eta\Big[r+\gamma\max_bQ(s',b)-Q(s,a)\Big]\tag{35.12}$$
Data can come from any source. With every pair visited infinitely often and properly decayed learning rates, it provably converges to $Q_*$ in the tabular case. Algorithm 35.1 (p. 1154): sample ε-greedy $a$, observe $s',r$, $\delta=r+\gamma\max_{a'}Q_w(s',a')-Q_w(s,a)$, $w\leftarrow w+\eta\delta\nabla_wQ_w(s,a)$.

*Example (Fig. 35.4, p. 1155).* 1d grid world, $\gamma=0.9$, $Q=0$ initially, $\eta=1$. The update becomes $Q_*(s,a)=r+\gamma Q_*(s',a_*)$ with $a_*={\downarrow}$. Episode 1 ends with reward 1 from $S_3$, so $Q(S_3,\downarrow)=1$. Episode 2 gives $Q(S_2,\downarrow)=0.9\times1=0.9$. Later entries are $0.81$ and $0.73$.

**Double Q-learning (p. 1154).** Maximization bias (optimizer's curse) comes from $\mathbb E[\max_aX_a]\ge\max_a\mathbb E[X_a]$. Noise can make a wrong action look best. In Fig. 35.5, state A has a "right" action (reward 0, terminate) and a "left" action (reward 0, then state B with many actions with rewards $\mathcal N(-0.1,1.0)$). The true return of left is $-0.1$, yet Q-learning may prefer it. Remedy: two Q-functions, one selects and one evaluates:
$$Q_1(s,a)\leftarrow Q_1(s,a)+\eta\Big[r+\gamma Q_2\big(s',\arg\max_{a'}Q_1(s',a')\big)-Q_1(s,a)\Big]\tag{35.13}$$
and the roles are swapped on other updates.

**35.2.6 DQN (pp. 1154–1156).** Two stabilizers:
- An *experience replay buffer* $\mathcal D$ of recent transitions. It gives data reuse and less correlated samples.
- A frozen *target network* $Q_{w^-}$:
$$\mathcal L^{\rm DQN}(w)=\mathbb E_{(s,a,r,s')\sim U(\mathcal D)}\Big[\big(r+\gamma\max_{a'}Q_{w^-}(s',a')-Q_w(s,a)\big)^2\Big]\tag{35.14}$$
with $w^-\leftarrow w$ set periodically. This is an instance of fitted value iteration.

Extensions:
- *Double DQN* uses double learning.
- *Prioritized replay* samples with probability $\propto(|\delta|+\varepsilon)^\eta$, where $\eta=0$ is uniform.
- *Dueling DQN* learns $V_w$ and $A_w$ with shared parameters.
- *Rainbow* combines these with multi-step returns, distributional RL and noisy nets.

### 35.3 Policy-based RL (pp. 1156–1163)
Value-based methods have three disadvantages: they are hard to use with continuous actions, they may diverge under approximation, and $Q$-training is not directly tied to the policy's expected return (p. 1156).

**35.3.1 Policy gradient theorem** (episodic case; p. 1157).
$$J(\pi)\triangleq\mathbb E_{p_0,\pi}[G_0]=\mathbb E_{p_0(s_0)}[V_\pi(s_0)]=\mathbb E_{p_0(s_0)\pi(a_0|s_0)}[Q_\pi(s_0,a_0)]\tag{35.15}$$
$$\nabla_\theta J(\pi_\theta)=\mathbb E_{p_0(s_0)}\Big[\nabla_\theta\sum_{a_0}\pi_\theta(a_0|s_0)Q_{\pi_\theta}(s_0,a_0)\Big]\tag{35.16}$$
$$=\mathbb E_{p_0(s_0)}\Big[\sum_{a_0}\nabla\pi_\theta(a_0|s_0)Q_{\pi_\theta}(s_0,a_0)\Big]+\mathbb E_{p_0(s_0)\pi_\theta(a_0|s_0)}[\nabla_\theta Q_{\pi_\theta}(s_0,a_0)]\tag{35.17}$$
(35.17 follows from 35.16 by the product rule; added step.) For the last term:
$$\nabla_\theta Q_{\pi_\theta}(s_0,a_0)=\nabla_\theta\big[R(s_0,a_0)+\gamma\mathbb E_{p(s_1|s_0,a_0)}[V_{\pi_\theta}(s_1)]\big]=\gamma\nabla_\theta\mathbb E_{p(s_1|s_0,a_0)}[V_{\pi_\theta}(s_1)]\tag{35.18}$$
This has the form of $\nabla_\theta J$, so repeating the steps gives
$$\nabla_\theta J(\pi_\theta)=\sum_{t=0}^\infty\gamma^t\mathbb E_{p_t(s)}\Big[\sum_a\nabla_\theta\pi_\theta(a|s)Q_{\pi_\theta}(s,a)\Big]\tag{35.19}$$
$$=\frac1{1-\gamma}\mathbb E_{p^\infty_{\pi_\theta}(s)}\Big[\sum_a\nabla_\theta\pi_\theta(a|s)Q_{\pi_\theta}(s,a)\Big]\tag{35.20}$$
$$=\frac1{1-\gamma}\mathbb E_{p^\infty_{\pi_\theta}(s)\pi_\theta(a|s)}\big[\nabla_\theta\log\pi_\theta(a|s)\,Q_{\pi_\theta}(s,a)\big]\tag{35.21}$$
Here $p_t(s)$ is the probability of being in $s$ at time $t$ (start $s_0\sim p_0$, follow $\pi_\theta$). Also $p^\infty_{\pi_\theta}(s)=(1-\gamma)\sum_t\gamma^tp_t(s)$ is the normalized discounted visitation distribution. Equation (35.21) is the *policy gradient theorem*. (35.20→35.21 uses $\nabla\pi=\pi\nabla\log\pi$; added step.) A baseline $b(s)$ reduces variance:
$$\nabla_\theta J(\pi_\theta)=\frac1{1-\gamma}\mathbb E_{p^\infty_{\pi_\theta}(s)\pi_\theta(a|s)}\big[\nabla_\theta\log\pi_\theta(a|s)(Q_{\pi_\theta}(s,a)-b(s))\big]\tag{35.22}$$
A common choice is $b(s)=V_{\pi_\theta}(s)$.

*Intuition note.* Raise the log-probability of actions in proportion to how good they are. States are weighted by how often, and how early, the policy visits them.

**35.3.2 REINFORCE** (p. 1158). From a sampled trajectory:
$$\nabla_\theta J\approx\sum_{t=0}^{T-1}\gamma^tG_t\nabla_\theta\log\pi_\theta(a_t|s_t)\tag{35.24}$$
$$\theta\leftarrow\theta+\eta\sum_{t=0}^{T-1}\gamma^t(G_t-b(s_t))\nabla_\theta\log\pi_\theta(a_t|s_t)\tag{35.25}$$
If the return beats the baseline, make the trajectory more likely, otherwise less. Algorithm 35.2 uses $b=V_w$ learned by MC. For each $t$: $\delta=G_t-V_w(s_t)$, $w\leftarrow w+\eta_w\delta\nabla_wV_w(s_t)$, $\theta\leftarrow\theta+\eta_\theta\gamma^t\delta\nabla_\theta\log\pi_\theta(a_t|s_t)$.

**35.3.3 Actor-critic** (pp. 1158–1160). The return is estimated by TD instead of MC. This allows efficient, fully online updates. With the one-step return $G_{t:t+1}=r_t+\gamma V_w(s_{t+1})$ and baseline $V_w(s_t)$:
$$\theta\leftarrow\theta+\eta\sum_{t}\gamma^t\big(r_t+\gamma V_w(s_{t+1})-V_w(s_t)\big)\nabla_\theta\log\pi_\theta(a_t|s_t)\tag{35.26–35.27}$$
The bracket is a single-sample estimate of $A(s_t,a_t)=Q-V$. This is *A2C* (Alg. 35.3). Running actors in parallel with asynchronous shared updates gives *A3C*.

With $n$ steps (35.28–35.29), $A^{(n)}=G_{t:t+n}-V_w(s_t)$. Real rewards are unbiased but high variance. $V_w$ has lower variance but is biased, so $n$ controls bias–variance. A $\lambda$-weighted average is equivalent to
$$A^{(\lambda)}_{\pi_\theta}(s_t,a_t)\triangleq\sum_{\ell=0}^\infty(\gamma\lambda)^\ell\delta_{t+\ell},\quad\delta_t=r_t+\gamma V_w(s_{t+1})-V_w(s_t)\tag{35.30}$$
Larger $\lambda$ lowers bias and raises variance. Algorithm 35.4 implements it with eligibility traces ($z_w\leftarrow\gamma\lambda_wz_w+\nabla_wV_w$, $z_\theta\leftarrow\gamma\lambda_\theta z_\theta+\gamma^t\nabla_\theta\log\pi_\theta$, then $w\leftarrow w+\eta_w\delta z_w$, $\theta\leftarrow\theta+\eta_\theta\delta z_\theta$). This is generalized advantage estimation (GAE).

**35.3.4 Bound optimization** (pp. 1160–1162). Plain policy gradient need not improve $J$ monotonically; it can collapse if the learning rate is too large. A fact relating two policies [KL02]:
$$J(\pi')-J(\pi)=\frac1{1-\gamma}\mathbb E_{p^\infty_{\pi'}(s)}\big[\mathbb E_{\pi'(a|s)}[A_\pi(s,a)]\big]\tag{35.31}$$
If $\mathbb E_{\pi'(a|s)}[A_\pi(s,a)]\ge0$ for all $s$, then $J(\pi')\ge J(\pi)$. This is hard to ensure with function approximation, and there is no direct way to sample states from $p^\infty_{\pi'}$.

*Conservative step.* Let $\pi_\theta=\theta\pi'+(1-\theta)\pi$, $\theta\in[0,1]$. Then $J(\pi_\theta)-J(\pi)=\theta L(\pi')+O(\theta^2)$ with
$$L(\pi')\triangleq\frac1{1-\gamma}\mathbb E_{p^\infty_\pi(s)}\big[\mathbb E_{\pi'(a|s)}[A_\pi(s,a)]\big]=\frac1{1-\gamma}\mathbb E_{p^\infty_\pi(s)\pi(a|s)}\Big[\frac{\pi'(a|s)}{\pi(a|s)}A_\pi(s,a)\Big]\tag{35.32}$$
This switches the state distribution to $p^\infty_\pi$ and creates an $O(\theta^2)$ residual. Bounding the residual gives lower bounds:
$$J^{\rm CPI}(\pi_\theta)\triangleq J(\pi)+\theta L(\pi')-\frac{2\varepsilon\gamma}{(1-\gamma)^2}\theta^2,\ \ \varepsilon=\max_s|\mathbb E_{\pi'(a|s)}[A_\pi(s,a)]|\tag{35.33}$$
$$J^{\rm TRPO}(\pi')\triangleq J(\pi)+L(\pi')-\frac{\varepsilon\gamma}{(1-\gamma)^2}\max_sD_{\mathbb{KL}}(\pi(s)\|\pi'(s)),\ \ \varepsilon=\max_{s,a}|A_\pi(s,a)|\tag{35.34}$$
Safe policy iteration uses maximum total variation instead of KL. In practice TRPO's update is overly conservative, so [Sch+15b] use an average KL and a trust region:
$$\arg\max_{\pi'}L(\pi')\ \text{ s.t. }\ \mathbb E_{p^\infty_\pi(s)}[D_{\mathbb{KL}}(\pi(s)\|\pi'(s))]\le\delta\tag{35.35}$$
Trust regions with a KL penalty are equivalent to natural gradient descent (Sec. 6.4.2.1). This matters because equal parameter distances need not mean equal policy (KL) distances (35.36). The natural gradient can be approximated with KFAC.

PPO uses a clipped objective, with $\kappa_\epsilon(x)=\mathrm{clip}(x,1-\epsilon,1+\epsilon)$:
$$J^{\rm PPO}(\pi')\triangleq\frac1{1-\gamma}\mathbb E_{p^\infty_\pi(s)\pi(a|s)}\Big[\kappa_\epsilon\Big(\frac{\pi'(a|s)}{\pi(a|s)}\Big)A_\pi(s,a)\Big]\tag{35.37}$$
The authors say this "often works better, and is simpler" than a KL penalty (p. 1162). It can be modified to ensure monotonic improvement [WHT19].

*Intuition note.* Take a policy step only as large as the advantage estimate can be trusted. Penalizing or capping how far the new policy moves from the old one does this.

**35.3.5 Deterministic policy gradient** (pp. 1162–1163). For $a_t=\mu_\theta(s_t)$ with continuous states and actions:
$$J(\mu_\theta)\triangleq\frac1{1-\gamma}\mathbb E_{p^\infty_{\mu_\theta}(s)}[R(s,\mu_\theta(s))]\tag{35.38}$$
$$\nabla_\theta J(\mu_\theta)=\frac1{1-\gamma}\mathbb E_{p^\infty_{\mu_\theta}(s)}[\nabla_\theta Q_{\mu_\theta}(s,\mu_\theta(s))]=\frac1{1-\gamma}\mathbb E_{p^\infty_{\mu_\theta}(s)}\big[\nabla_\theta\mu_\theta(s)\nabla_aQ_{\mu_\theta}(s,a)|_{a=\mu_\theta(s)}\big]\tag{35.39–35.40}$$
The stochastic policy gradient theorem reduces to this as noise $\to0$. The estimate integrates over states, not actions, which lowers variance. A deterministic policy does not explore, so data come from a stochastic behavior policy $\beta$:
$$J_b(\mu_\theta)\triangleq\mathbb E_{p^\infty_\beta(s)}[Q_{\mu_\theta}(s,\mu_\theta(s))],\quad\nabla_\theta J_b\approx\mathbb E_{p^\infty_\beta(s)}\big[\nabla_\theta\mu_\theta(s)\nabla_aQ_{\mu_\theta}(s,a)|_{a=\mu_\theta(s)}\big]\tag{35.41–35.42}$$
where a term depending on $\nabla_\theta Q_{\mu_\theta}(s,a)$ is dropped. With a TD critic:
$$\delta=r_t+\gamma Q_w(s_{t+1},\mu_\theta(s_{t+1}))-Q_w(s_t,a_t)\tag{35.43}$$
$$w_{t+1}\leftarrow w_t+\eta_w\delta\nabla_wQ_w(s_t,a_t)\tag{35.44}$$
$$\theta_{t+1}\leftarrow\theta_t+\eta_\theta\nabla_\theta\mu_\theta(s_t)\nabla_aQ_w(s_t,a)|_{a=\mu_\theta(s_t)}\tag{35.45}$$
No importance sampling is needed: the actor uses the deterministic gradient and the critic uses Q-learning. A linear critic with features $\phi(s,a)=a^\top\nabla_\theta\mu_\theta(s)$ is *compatible*, and then the approximation does not bias the gradient.

Extensions:
- *DDPG* uses DQN-style target networks and replay. The actor minimizes $-Q(\mathrm{sg}(s),\pi(s))$ and the critic a 1-step TD loss.
- *TD3* uses double learning and other heuristics.
- *REDQ* uses an ensemble of more than 2 Q-networks.
- *D4PG* adds distributed training and distributional RL.
- *Amago* uses a shared transformer for actor and critic, with a Pop-Art-normalized loss $\mathcal L=\mathbb E[\lambda_0\mathcal L_{TD}+\lambda_1\mathcal L_{PG}]$.

**35.3.6 Gradient-free** (p. 1163). Policy gradient is a "zeroth-order" estimator. Derivative-free optimizers can be more efficient, e.g. random search on linear policies [MGR18] and evolutionary strategies [Sal+17b].

### 35.4 Model-based RL (pp. 1164–1171)
Model-free methods need very many interactions: millions of Atari frames for rainbow, and 100 years of simulated data for OpenAI's robot hand (p. 1164). MBRL learns $p(s'|s,a)$ and $R(s,a)$, then "tries things out" in imagination.

**35.4.1 Model predictive control (MPC)** (p. 1164). Wait until state $s_t$ is known, plan with the model, act, and repeat:
$$a^*_{t:t+H-1}=\arg\max_{a_{t:t+H-1}}\mathbb E\Big[\sum_{h=0}^{H-1}R(s_{t+h},a_{t+h})+\hat V(s_{t+H})\Big]\tag{35.46}$$
$H$ is the planning horizon and $\hat V(s_{t+H})$ estimates the reward-to-go.
- *Heuristic search* (p. 1165). With finite spaces, exact solution is typically exponential in $H$. Pruning via best-first search helps. A heuristic is *admissible* if it is optimistic: a lower bound on distance, or an upper bound on value for reward maximization. Admissibility ensures no incorrect pruning, and the resulting $A^*$ search is optimal.
- *MCTS* learns a value for each encountered state instead of a hand-made heuristic. It is inspired by UCB. It underlies AlphaGo/AlphaZero (known model). MuZero and Stochastic MuZero learn the model.
- *Continuous actions* (pp. 1165–1166). Equation (35.46) is a nonlinear program. With linear dynamics and negative-quadratic reward, LQG gives a mathematical solution. Otherwise shooting, collocation or DDP are used. DDP linearizes dynamics around a reference trajectory, solves the local problem with LQG, and iterates. Gradient-free options include the cross-entropy method.

**35.4.2 Combining model-based and model-free** (p. 1166). Train a policy or Q-function on "hallucinated" model rollouts (Dyna). [Jan+19] start short rollouts from real visited states so the model only extrapolates locally. Imagination-augmented agents [Web+17] use hidden states of a predictive model as extra policy context. [Jad+17] add auxiliary prediction targets, which helps with sparse rewards.

**35.4.3 Gaussian processes** (pp. 1166–1168).
- *PILCO:* $s_{t+1}=f(s_t,a_t)+\epsilon_t$, $\epsilon_t\sim\mathcal N(0,\Sigma)$, with $f$ modeled by a GP. Fantasy rollouts evaluate $J(\pi_\theta)=\sum_{t=1}^T\mathbb E[c(s_t)]$. Under a Gaussian assumption the belief state is propagated deterministically, so $J$ and its gradient are deterministic. Deterministic batch optimizers (Levenberg–Marquardt) can then be used instead of SGD.
  - Cart-pole swing-up: $s\in\mathbb R^4$, $a\in\mathbb R$, an RBF controller with 50 basis functions and 305 parameters, trained in 7 real trials (17.5 s).
  - Block stacking: $s\in\mathbb R^3$, $a\in\mathbb R^4$, a linear policy trained with as few as 10 real trials.
- *GP-MPC* proposes open-loop action sequences and gets a Gaussian approximation of future states by moment matching. It computes the expected reward and its gradient w.r.t. $a_{t:t+H-1}$, executes the first action and repeats. Claimed advantages over PILCO: easier constraints, and possibly more data efficiency from per-step model updates.

**35.4.4 DNNs** (p. 1168). DNNs scale better but do not naturally model uncertainty. Examples: deep PILCO (MC dropout) and PETS (ensembles). Stochastic models give high-variance returns. The *common random number* trick (shared seed across rollouts, as in PEGASUS) reduces this.

**35.4.5 Latent-variable models** (pp. 1168–1170).
- *World models [HS18]:* a VAE compresses images $x_t\in\mathbb R^{64\times64\times3}$ to $z_t\in\mathbb R^{64}$ (as printed). An RNN with mixture-density output predicts $p(z_{t+1}|z_t,a_t,h_t)$. A linear controller on $(z_t,h_t)$ is trained with CMA-ES (867 parameters; the VAE has 4.3M and the MDN-RNN 422k). The model can be trained unsupervised from random rollouts. Training the controller wholly in "dream mode" does not always work, because the controller can exploit model flaws (like an adversarial attack). A temperature $\tau$ that raises MDN variance forces robustness, similar to domain randomization.
- *PlaNet:* a POMDP with a recurrent state-space model $p(z_t|z_{t-1},a_{t-1})p(s_t|z_t)p(r_t|z_t)$ fitted by variational inference with $q(z_t|s_{1:t},a_{1:t-1})$. It plans with the cross-entropy method in latent space and uses latent overshooting. It outperforms A3C and D4PG on image-based control, but is expensive: CEM with 1000 samples × 10 iterations × horizon 12 = 120,000 dynamics evaluations per action. [AY20] use differentiable CEM, which is faster but a bit worse, then fine-tune with PPO.
- *Dreamer:* replaces MPC with a policy network $\pi(a_t|z_t)$ trained by actor-critic in latent space. Models are trained by the ELBO and the value by MSE to the TD-λ estimate. It does better than PlaNet, "presumably" because it optimizes long-term value rather than short rollouts.

**35.4.6 Robustness to model errors** (p. 1171). Model error causes distribution shift. The model is trained on states from the behavior policy, but the policy optimized under it visits different states. Models must generalize robustly or at least quantify uncertainty.

### 35.5 Off-policy learning (pp. 1171–1177)
Off-policy methods tend to be more data efficient and easier to use when trying a new policy is costly or risky. Plain averaging of data from $\pi'$ estimates $J(\pi')$, not $J(\pi)$. Distribution mismatch also arises in covariate shift and causal effect estimation. Off-policy RL stresses the data–policy mismatch. Offline RL stresses that the data are static and no further interaction is allowed (p. 1171). Data: trajectories from a behavior policy $\pi_b$, to evaluate a target policy $\pi_e$. If $\pi_b$ is unknown, the setting is behavior-agnostic (p. 1172).

**35.5.1.1 Direct method** (p. 1172). Estimate $\hat R,\hat P$ by regression and density estimation, then simulate. Small model errors compound over long horizons (γ near 1), so an agent may overfit the errors. Learning the transition model is generally hard.

**35.5.1.2 Importance sampling** (pp. 1172–1173), horizon $T$:
$$\hat J_{\rm IS}(\pi_e)\triangleq\frac1n\sum_{i=1}^n\frac{p(\tau^{(i)}|\pi_e)}{p(\tau^{(i)}|\pi_b)}\sum_{t=0}^{T-1}\gamma^tr^{(i)}_t\tag{35.47}$$
It is unbiased, $\mathbb E_{\pi_b}[\hat J_{\rm IS}]=J(\pi_e)$, provided $p(\tau|\pi_b)>0$ whenever $p(\tau|\pi_e)>0$. The ratio does not depend on the MDP models:
$$\frac{p(\tau|\pi_e)}{p(\tau|\pi_b)}=\frac{p(s_0)\prod_tπ_e(a_t|s_t)p(s_{t+1}|s_t,a_t)p_R(r_t|s_t,a_t,s_{t+1})}{p(s_0)\prod_t\pi_b(a_t|s_t)p(s_{t+1}|s_t,a_t)p_R(r_t|s_t,a_t,s_{t+1})}=\prod_{t=0}^{T-1}\frac{\pi_e(a_t|s_t)}{\pi_b(a_t|s_t)}\tag{35.48}$$
If $\pi_b$ is unknown it can be estimated ($\hat\pi_b$, e.g. logistic regression or a DNN). The per-step ratio is $\rho_t=\pi_e(a_t|s_t)/\pi_b(a_t|s_t)$, and $\hat\rho_t$ uses $\hat\pi_b$. The ratio can be arbitrarily large, so variance can be high. *Per-decision IS* uses that $r_t$ is independent of the later trajectory:
$$\hat J_{\rm PDIS}(\pi_e)\triangleq\frac1n\sum_{i=1}^n\sum_{t=0}^{T-1}\prod_{t'\le t}\rho_{t'}(\tau^{(i)})\gamma^tr^{(i)}_t\tag{35.49}$$
Self-normalized and truncated IS trade a small bias for lower variance. For policy improvement, one approximation averages over the behavior state distribution:
$$J_b(\pi_\theta)\triangleq\mathbb E_{p^\infty_\beta(s)}\Big[\sum_a\pi_\theta(a|s)Q_\pi(s,a)\Big]\tag{35.50}$$
Dropping $\nabla_\theta Q_\pi$ [DWS12] gives $\nabla_\theta J_b\approx\mathbb E_{p^\infty_\beta(s)\beta(a|s)}\big[\tfrac{\pi_\theta(a|s)}{\beta(a|s)}\nabla_\theta\log\pi_\theta(a|s)Q_\pi(s,a)\big]$. In the tabular case an optimal policy exists for all states. So $J_b$ can be a good proxy for $J$ as long as $\pi_b$ "covers" all states. In general with parametric families this uniform optimality is lost.

**35.5.1.3 Doubly robust** (pp. 1173–1174). For a contextual bandit ($T=1$):
$$\hat J_{\rm DR}(\pi_e)\triangleq\frac1n\sum_i\Big(\frac{\pi_e(a_0^{(i)}|s_0^{(i)})}{\hat\pi_b(a_0^{(i)}|s_0^{(i)})}\big(r_0^{(i)}-\hat Q(s_0^{(i)},a_0^{(i)})\big)+\hat V(s_0^{(i)})\Big),\ \ \hat V(s)=\mathbb E_{\pi_e(a|s)}[\hat Q(s,a)]\tag{35.51}$$
If $\hat\pi_b=\pi_b$, $\hat Q$ cancels against $\hat V$ on average, leaving the unbiased IS estimate. If $\hat Q=Q_{\pi_e}$, $\hat Q$ cancels against the reward on average, leaving the unbiased direct method. So the estimator is unbiased as long as one of $\hat\pi_b$, $\hat Q$ is right. For MDPs: $\hat J_{\rm DR}[T]\triangleq0$ and
$$\hat J_{\rm DR}[t]\triangleq\hat V(s_t)+\hat\rho_t(\tau)\big(r_t+\gamma\hat J_{\rm DR}[t+1]-\hat Q(s_t,a_t)\big)\tag{35.52}$$
which equals (exercise)
$$\hat J_{\rm DR}[0]=\hat V(s_0)+\sum_{t=0}^{T-1}\Big(\prod_{t'=0}^t\hat\rho_{t'}(\tau)\Big)\gamma^t\big(r_t+\gamma\hat V(s_{t+1})-\hat Q(s_t,a_t)\big)\tag{35.53}$$
The estimator is shown to have minimum variance under certain conditions [JL16].

**35.5.1.4 Behavior-regularized** (pp. 1174–1175). Keep $\pi_e$ close to $\pi_b$. Hard constraint:
$$\mathcal L^{\rm DQN}_1(w)\triangleq\mathbb E_{\mathcal D}\Big[\big(r+\gamma\max_{\pi:D(\pi,\pi_b)\le\varepsilon}\mathbb E_{\pi(a'|s')}[Q_{w^-}(s',a')]-Q_w(s,a)\big)^2\Big]\tag{35.54}$$
Soft penalty:
$$\mathcal L^{\rm DQN}_2(w)\triangleq\mathbb E_{\mathcal D}\Big[\big(r+\gamma\max_\pi\mathbb E_{\pi(a'|s')}[Q_{w^-}(s',a')]-\alpha\gamma D(\pi(s'),\pi_b(s'))-Q_w(s,a)\big)^2\Big]\tag{35.55}$$
$D$ may be a KL divergence. This can be combined with IS.

**35.5.2 Curse of horizon** (pp. 1175–1176). The trajectory ratio has variance growing exponentially in $T$ [Liu+18b]. An example is cited where behavior and target state-action distributions are identical, yet the trajectory ratio grows exponentially. So correct the state-action distribution instead. Data: $\mathcal D=\{(s_i,a_i,r_i,s_i')\}$ with $(s_i,a_i)\sim p_{\mathcal D}$. Define $\zeta_*(s,a)=p^\infty_\pi(s,a)/p_{\mathcal D}(s,a)$:
$$J(\pi)=\frac1{1-\gamma}\mathbb E_{p^\infty_\pi(s,a)}[R(s,a)]=\frac1{1-\gamma}\mathbb E_{p^\infty_\beta(s,a)}[\zeta_*(s,a)R(s,a)]\tag{35.56}$$
Start from a linear program with $f$-divergence $D_f$ and flow constraints (a variant of Eq. 34.93):
$$\max_{d\ge0}-D_f(d\|p_{\mathcal D})\ \text{ s.t. }\ d(s,a)=(1-\gamma)\mu_0(s)\pi(a|s)+\gamma\sum_{\bar s,\bar a}p(s|\bar s,\bar a)d(\bar s,\bar a)\pi(a|s)\ \ \forall(s,a)\tag{35.57}$$
Under mild conditions $p^\infty_\pi$ is the only solution of the constraints, so the objective does not change the solution. With multipliers $\nu(s,a)$ and $\zeta=d/p_{\mathcal D}$ the Lagrangian is:
$$\max_{\zeta\ge0}\min_\nu\mathcal L(\zeta,\nu)=\mathbb E_{p_{\mathcal D}}[-f(\zeta)]+(1-\gamma)\mathbb E_{p_0(s)\pi(a|s)}[\nu(s,a)]+\mathbb E_{\pi(a'|s')p(s'|s,a)p_{\mathcal D}(s,a)}\big[\zeta(s,a)(\gamma\nu(s',a')-\nu(s,a))\big]\tag{35.58}$$
The saddle point coincides with $\zeta_*$. Two-timescale SGD on $\zeta,\nu$ gives *DualDICE* (extended to GenDICE). This has generally lower variance than IS or DR. It is behavior-agnostic, needs no trajectories, and can be extended to be doubly robust and to optimize a policy.

*Intuition note.* Reweighting whole trajectories multiplies many per-step ratios, so the weights explode. Reweighting individual state-action pairs avoids the product.

**35.5.3 Deadly triad** (pp. 1176–1177). *Baird's example* (Fig. 35.10a): 7 states, 2 actions, all rewards 0, $\gamma=0.99$. The dashed action goes to one of the 6 upper states uniformly. The solid action goes to the bottom state. $V_w$ is linear in $w\in\mathbb R^8$, and the target policy always chooses solid. So $V_\pi=0$ is exactly representable with $w=0$. With behavior policy $b$ (dashed 6/7, solid 1/7), TD(0) diverges to $\infty$. With on-policy data, TD(0) with linear approximation is guaranteed to converge to a good approximation [TR97].

Divergence appears in many bootstrapping methods, linear or nonlinear. The root cause is that they do not minimize a fixed objective. They build targets from their own estimates, which can create a self-reinforcing loop. The tabular contraction property (Eq. 34.87) may fail under approximation. Off-policy learning, bootstrapping and function approximation together can destabilize an algorithm: the *deadly triad*.

Fixed objectives that aim to ensure convergence:
$$\min_{V,\pi}\mathcal L^{\rm PCL}(V,\pi)\triangleq\mathbb E\Big[\tfrac12\big(r+\gamma V(s')-\lambda\log\pi(a|s)-V(s)\big)^2\Big]\tag{35.59}$$
This is path consistency learning, an entropy-smoothed Bellman residual. Minimizing it does not give the optimal $V,\pi$ in general, because of "double sampling". The fix is a dual function:
$$\min_{V,\pi}\max_\nu\mathcal L^{\rm SBEED}\triangleq\mathbb E\Big[\nu(s,a)\big(r+\gamma V(s')-\lambda\log\pi(a|s)-V(s)\big)-\nu(s,a)^2/2\Big]\tag{35.60}$$
Optimizing it forces $\nu$ to model the Bellman error (SBEED).

**35.5.4.** Common off-policy methods: Q-learning, SAC, DDPG/TD3, and MPO (a bound-optimization method based on EM) (p. 1177).

*Intuition note.* TD chases its own predictions. Off-policy data adds a further source of instability, and the self-reinforcing loop of estimates built from estimates can push them to infinity.

### 35.6 Control as inference (pp. 1177–1183)
**35.6.1 Maximum entropy RL** (pp. 1178–1180). Add a binary optimality variable $o_t$ (Fig. 35.11):
$$p(o_t=1|s_t,a_t)=\exp(\lambda^{-1}R(s_t,a_t))\tag{35.61}$$
with $\lambda>0$ and, w.l.o.g., $R<0$ so this is a valid probability. With a uniform action prior:
$$p(\tau|o_{0:T-1}=1)\propto p(s_0)\prod_{t=0}^{T-1}p(s_{t+1}|s_t,a_t)\exp\Big(\frac1\lambda\sum_{t=0}^{T-1}R(s_t,a_t)\Big)\tag{35.62}$$
With deterministic transitions, feasible trajectories have probability $\propto\exp(\lambda^{-1}\sum R)$ and infeasible ones 0. So maximizing reward means inferring the most probable trajectory. The optimal policy is
$$p(a_t|s_t,o_{t:T-1}=1)\propto\frac{p(o_{t:T-1}=1|s_t,a_t)}{p(o_{t:T-1}=1|s_t)}\tag{35.63}$$
with
$$p(o_{t:T-1}=1|s_t,a_t)=\int_{\mathcal S}p(o_{t+1:T-1}=1|s_{t+1})p(s_{t+1}|s_t,a_t)\exp(\lambda^{-1}R(s_t,a_t))ds_{t+1}\tag{35.64}$$
$$p(o_{t:T-1}=1|s_t)=\int_{\mathcal A}p(o_{t:T-1}=1|s_t,a_t)p(a_t|s_t)da_t\tag{35.65}$$
starting from $p(o_{T-1}=1|s_{T-1},a_{T-1})=\exp(\lambda^{-1}R)$. This is expensive, so a parametric $\pi_\theta$ is used, with $p_\theta(\tau)=p(s_1)\prod_tp(s_{t+1}|s_t,a_t)\pi_\theta(a_t|s_t)$ (35.66, as printed). Minimizing $D_{\mathbb{KL}}(p_\theta(\tau)\|p(\tau|o_{0:T-1}=1))$ gives
$$D_{\mathbb{KL}}=-\mathbb E_{p_\theta}\Big[\sum_{t=0}^{T-1}\lambda^{-1}R(s_t,a_t)+\mathbb H(\pi_\theta(s_t))\Big]+\text{const}\tag{35.67}$$
where the constant depends only on the uniform action prior. The objective is total reward plus entropy regularization (MERL). If $\pi_\theta$ is unrestricted, a softmax Bellman equation holds:
$$Q_*(s_t,a_t)=\lambda^{-1}R(s_t,a_t)+\mathbb E_{p(s_{t+1}|s_t,a_t)}\Big[\log\int_{\mathcal A}\exp(Q_*(s_{t+1},a_{t+1}))da\Big]\tag{35.68}$$
with $Q_*(s_T,a)=0$ and $\pi_*(a_t|s_t)\propto\exp(Q_*(s_t,a_t))$. This $Q_*$ differs from the usual one because of the entropy term. As $\lambda\to0$ the difference vanishes and the policy becomes greedy.

*Soft actor-critic (SAC)* is off-policy with objective ($T\to\infty$)
$$J^{\rm SAC}(\theta)\triangleq\mathbb E_{p^\infty_{\pi_\theta}(s)\pi_\theta(a|s)}[R(s,a)+\lambda\mathbb H(\pi_\theta(s))]\tag{35.69}$$
The entropy also encourages exploration. Soft value updates use (as printed):
$$Q_w(s,a)=R(s,a)+\gamma\mathbb E_{p(s'|s,a)}[V_u(s',a')-\lambda\log\pi_\theta(a'|s')],\quad V_u(s,a)=\lambda\log\sum_a\exp(\lambda^{-1}Q_w(s,a))\tag{35.70–35.71}$$
This induces $\pi_w(a|s)=\exp(\lambda^{-1}Q_w)/Z_w(s)$. Then $\theta$ is updated by minimizing $\mathbb E[D_{\mathbb{KL}}(\pi_\theta(s)\|\pi_w(s))]$ over states from a replay buffer. SAC is reported to beat DDPG and PPO "by a wide margin" on continuous control [Haa+18]. *Soft Q-learning* learns only $Q_w$, since
$$V_w(s)=\lambda\log\sum_a\exp(\lambda^{-1}Q_w(s,a)),\quad\pi_w(a|s)=\exp\big(\lambda^{-1}(Q_w(s,a)-V_w(s))\big)\tag{35.72–35.73}$$
It is convenient for few discrete actions or an easy integral. MERL algorithms resemble PCL and SBEED.

*Intuition note.* Treat "being optimal" as evidence and ask what trajectory distribution best explains it. Minimizing KL to that posterior amounts to maximizing reward plus an entropy bonus that favors more uniform policies.

**35.6.2 Other approaches** (pp. 1180–1181).
- *VIREL:* $p(o_t=1|s_t,a_t)=\exp\big(\tfrac{Q_w(s_t,a_t)-\max_aQ_w(s_t,a)}{\lambda_w}\big)$ (35.74), with learned temperature. EM maximizes $\mathcal L(w,\theta)=\mathbb E_{p(s)}\big[\mathbb E_{\pi_\theta(a|s)}[Q_w/\lambda_w]+\mathbb H(\pi_\theta(s))\big]$ (35.75). E-step: $\theta\leftarrow\theta+\eta_\theta\nabla_\theta\mathcal L$ (35.76). M-step: $w\leftarrow w+\eta_w\nabla_w\mathcal L$ (35.77).
- *Pseudo-likelihood:* maximize $J(\pi_\theta)=\int G(\tau)p(\tau|\theta)d\tau$ (35.78). Some such methods resemble MERL but have $\theta$ in the second argument of the KL (forward KL). Forward KL is mode-covering, and in RL this is argued to be less preferred than MERL's mode-seeking reverse KL (see [Lev18]).
- *Active inference* rests on the free energy principle (FEP). The FEP is equivalent to variational inference for state estimation and parameter estimation, with $\mathcal F[p,q](y)=D_{\mathbb{KL}}(q(s,\theta|y)\|p(s,\theta|y))-\log p(y)$. A nonlinear hierarchical Gaussian model with a Laplace/Gaussian mean-field $q$ recovers *predictive coding*. This is a non-amortized VAE, with E and M steps both by gradient descent. For decisions, expected free energy is $\overline{\mathcal F}(a)=\mathbb E_{q(y|a)}[\mathcal F(y)]$ and the policy is $\pi(a)=\mathrm{softmax}(\overline{\mathcal F}(a))$ (as printed). Preferences enter as a prior $p(s)\propto e^{R(s)}$ or $p(y)\propto e^{R(y)}$. The generative model then encodes what the agent wants, which induces goal-directed information seeking. This contrasts with the goal-independent uncertainty of maxent RL. The authors say active inference is very similar to control as inference.

**35.6.3 Imitation learning** (pp. 1182–1183). The agent sees expert trajectories $\mathcal D_{\exp}$ (no rewards), with $a_t\sim\pi_{\exp}(s_t)$.
- *Behavior cloning* treats policy learning as classification:
$$\min_\pi\mathbb E_{p^\infty_{\pi_{\exp}}(s)}[D_{\mathbb{KL}}(\pi_{\exp}(s)\|\pi(s))]\tag{35.79}$$
A policy with low error under $p^\infty_{\pi_{\exp}}$ may have large error under $p^\infty_{\hat\pi}$ when run, because the state distribution depends on earlier actions.
- *Inverse RL (IRL)* infers a reward that explains the expert, then runs standard RL. Many rewards make the expert optimal, so a maximum-entropy energy model is used:
$$p(\tau)\propto\exp\Big(\sum_{t=0}^{T-1}R_\theta(s_t,a_t)\Big)\tag{35.80}$$
with partition function $Z_\theta=\int_\tau\exp(R_\theta(\tau))$. Using trajectories $\mathcal D$ from a known $q$:
$$\mathcal L(\theta)=-\frac1{|\mathcal D_{\exp}|}\sum_{\tau\in\mathcal D_{\exp}}R_\theta(\tau)+\log\frac1{|\mathcal D|}\sum_{\tau\in\mathcal D}\frac{\exp(R_\theta(\tau))}{q(\tau)}\tag{35.81}$$
The term inside the log is an importance sampling estimate of $Z$ that is unbiased as long as $q(\tau)>0$ for all $\tau$. The ideal $q_*\propto\exp(R_\theta(\tau))$ is approximated by a max-ent RL policy $\hat\pi$. This yields both $R_\theta$ and $\hat\pi$ (guided cost learning).
- *Divergence minimization:* if $p^\infty_\pi(s,a)$ and $p^\infty_{\pi_{\exp}}(s,a)$ are close, $\pi$ receives similar long-term reward. With convex $f$, a variational form of $D_f(p^\infty_{\pi_{\exp}}\|p^\infty_\pi)$ gives
$$\min_\pi\max_w\mathbb E_{p^\infty_{\pi_{\exp}}(s,a)}[T_w(s,a)]-\mathbb E_{p^\infty_\pi(s,a)}[f^*(T_w(s,a))]\tag{35.82}$$
with $T_w:\mathcal S\times\mathcal A\to\mathbb R$. The symbol $f^*$ is not defined on these pages. Different $f$ give GAIL, AIRL, $f$-MAX and FAIRL. Off-policy IL needs a distribution correction, e.g. ValueDICE (based on DualDICE).

## Toy example (ours, not from the text)
**Part A — TD/Q-learning on a 2-step chain.** States $s_1\to s_2\to$ terminal, one action "go". Reward 0 for $s_1\to s_2$, reward 1 for $s_2\to$terminal. $\gamma=0.9$, $\eta=0.5$, $Q=0$ initially, terminal value 0. True values: $Q(s_2)=1$, $Q(s_1)=0.9\times1=0.9$.
1. Update $(s_2,r=1,\text{term})$: target $=1+0.9\cdot0=1$. $Q(s_2)=0+0.5(1-0)=0.5$.
2. Update $(s_1,r=0,s_2)$: target $=0+0.9\times0.5=0.45$. $Q(s_1)=0+0.5(0.45-0)=0.225$.
3. Repeat $s_2$: target 1. $Q(s_2)=0.5+0.5(1-0.5)=0.75$.
4. Repeat $s_1$: target $=0.9\times0.75=0.675$. $Q(s_1)=0.225+0.5(0.675-0.225)=0.45$.

Both values move toward 1 and 0.9, and information flows backwards through bootstrapping. Each update uses one transition, not a full episode.

**Part B — baseline in the score-function estimator.** One-step bandit, $\pi_\theta(a{=}1)=\sigma(\theta)$, reward $=1$ if $a=1$, else 0, $\theta=0$ so $\sigma=0.5$. $\nabla_\theta\log\pi(1)=1-\sigma=0.5$ and $\nabla_\theta\log\pi(0)=-\sigma=-0.5$.
- No baseline: sample $a=1$ gives $(1)(0.5)=0.5$. Sample $a=0$ gives $(0)(-0.5)=0$. Expected value $0.5(0.5)+0.5(0)=0.25$, with values varying between 0.5 and 0.
- Baseline $b=0.5$: $a=1$ gives $(1-0.5)(0.5)=0.25$. $a=0$ gives $(0-0.5)(-0.5)=0.25$. Expected value $0.25$ with zero variance.

The expectation is unchanged and the variance drops, matching (35.22).

## Concepts
- [[markov-decision-process]] (new) — trajectory model factored into one-step transition and reward models; planning if known, RL if not (p. 1145)
- [[discounted-return]] (new) — $G_0=\sum_t\gamma^tr_t$, the quantity whose expectation is maximized (p. 1145)
- [[bootstrapping-td-learning]] (new) — update an estimate toward a target built from the estimate itself; TD error $r+\gamma V(s')-V(s)$ (pp. 1147, 1151)
- [[q-learning]] (new) — off-policy TD control with greedy next-action target, learning $Q_*$ (p. 1153)
- [[sarsa]] (new) — on-policy TD control using the sampled next action (p. 1153)
- [[on-off-policy]] (new) — on-policy: actions chosen by the current policy; off-policy: data from other policies allowed (p. 1146)
- [[maximization-bias]] (new) — $\mathbb E[\max X_a]\ge\max\mathbb E[X_a]$ makes Q-learning overestimate; double Q-learning fixes it (p. 1153)
- [[policy-gradient-theorem]] (new) — $\nabla J\propto\mathbb E[\nabla\log\pi\cdot Q]$ under discounted visitation (p. 1157)
- [[actor-critic-advantage]] (new) — policy (actor) trained with a learned value or advantage (critic) baseline (pp. 1147, 1159)
- [[trust-region-policy-optimization]] (new) — monotone-improvement bounds, KL constraint (TRPO), clipping (PPO) (pp. 1160–1162)
- [[model-predictive-control]] (new) — plan $H$ steps with a model, act once, replan (p. 1164)
- [[importance-sampling-off-policy]] (new) — reweight trajectories by $\prod\pi_e/\pi_b$ to correct behavior-data mismatch (p. 1172)
- [[doubly-robust-estimator]] (new) — unbiased if either the behavior model or the Q-model is correct (p. 1174)
- [[curse-of-horizon]] (new) — trajectory-ratio variance grows exponentially in $T$; fix by state-action correction (p. 1175)
- [[deadly-triad]] (new) — off-policy + bootstrapping + function approximation can diverge (p. 1177)
- [[bayes-adaptive-mdp]] (new) — belief over reward/transition models as part of the state; the Bayes-optimal exploration solution (p. 1149)
- [[control-as-inference]] (new) — optimality variables turn policy optimization into inference; max-ent RL (p. 1177)
- [[imitation-learning]] (new) — learn from expert trajectories without rewards (p. 1182)
- Reused: [[kl-divergence]] — policy proximity and the MERL objective (pp. 1161, 1179); [[variational-inference-elbo]] — PlaNet/Dreamer and the free energy principle (pp. 1170, 1181); [[conjugate-prior]] — Dirichlet for Thompson sampling (p. 1149); [[posterior-predictive-distribution]] — $\mathbb E_{b_t}[T]$ in the BAMDP (p. 1149); [[principle-of-indifference-maximum-entropy]] — the max-ent IRL model (p. 1182).

## Canonical instances
- [[baird-counterexample]] — 7-state MDP where off-policy linear TD(0) diverges (p. 1176)
- [[maximization-bias-mdp]] — states A and B with $\mathcal N(-0.1,1)$ rewards; Q-learning vs double Q-learning (pp. 1154, 1156)
- [[gridworld-q-learning]] — 1d grid, $\gamma=0.9$, values 1, 0.9, 0.81, 0.73 (p. 1155)
- [[pilco-cartpole]] — cart-pole swing-up learned in 7 real trials (p. 1167)
- [[world-models-vizdoom]] — VAE + MDN-RNN + linear controller, dream-mode training (p. 1168)

## Bridges (candidates)
- [same-math] control as inference: $\min_\theta D_{\mathbb{KL}}(p_\theta(\tau)\|p(\tau|o=1))$ ↔ bayesian: reverse-KL variational inference to a posterior over trajectories (p. 1179).
- [same-math] Thompson sampling with a Dirichlet transition posterior ↔ bayesian: conjugate Dirichlet–categorical updating and posterior sampling (p. 1149).
- [structural-analogy] Bayes-adaptive MDP belief state ↔ bayesian: sequential updating, with the posterior predictive as transition model (p. 1149).
- [structural-analogy] doubly robust off-policy estimator ↔ causal inference: DR estimators for treatment effects (p. 1174).
- [structural-analogy] importance-sampling off-policy correction ↔ causal inference / covariate shift: reweighting to remove data–target mismatch (p. 1171).
- [structural-analogy] predictive coding / active inference ↔ bayesian: variational free energy as the objective for perception and action (p. 1181).
- [metaphor] ε-greedy vs Boltzmann exploration ↔ bayesian: hard vs soft (temperature) decision rules.

## Questions this raises
- When does the soft (entropy-regularized) optimum differ materially from the standard optimum, and how should $\lambda$ be chosen?
- Can the doubly robust idea be pushed to the state-action ratio of DualDICE, and what would it cost in assumptions?
- How can a learned model's uncertainty be made reliable enough for MPC under distribution shift?
- Which practical conditions break the deadly triad, and do target networks and replay (DQN) only reduce it?

## Exercises worth doing
- Exercise at p. 1174 — verify that the recursive DR definition (35.52) equals the closed form (35.53) — difficulty: medium. (The text states this as "an exercise"; no numbered exercises are printed in this unit.)

## Reading notes
- Page offset: printed = pdf − 34 (pdf 1179 = p. 1145). pdf 1218 (printed 1184) has no text on it, so the content ends at p. 1183. Running footers: "Online version. December 10, 2025"; "Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license". The chapter is marked as co-authored with Lihong Li.
- Misprints and inconsistencies in the pages:
  - p. 1145: a sentence fragment ("...[SB18]. in textbooks such as...").
  - p. 1159: "csae"; "$r_{t+1}+\gamma V_w(s_{t+1})-V_w(s_t)$" where Eq. 35.27 has $r_t$.
  - p. 1160: "$V_w(s_{t+n+1})$" where $s_{t+n}$ seems meant; "$\delta_{t+l}$" in 35.30 vs $\ell$.
  - p. 1162: $\nabla_\theta\mu_\theta(s)$ is described as an $M\times N$ Jacobian ($M=\dim\mathcal A$, $N=\dim\theta$). For the product with the $M$-vector $\nabla_aQ$ to give an $N$-vector, the shape would appear to need to be $N\times M$.
  - p. 1163: samples "(s,a,r,a')" where $s'$ seems meant.
  - p. 1168: $z_t\in\mathbb R^{64}$ in the text, but footnote 8 uses a 32-dimensional $z_t$ for the 867-parameter count.
  - p. 1175: stray parenthesis in 35.57 ("$D_f(d\|p_{\mathcal D}))$") and a missing bracket in 35.58; I typeset them without the stray symbols. Eq. 35.57 uses $\mu_0$ and 35.58 uses $p_0$ for the initial distribution.
  - p. 1176: the Fig. 35.10 caption says "parameters of the policy diverge", while the text says value-function parameters $w$ diverge, and the plot shows $w_1,\dots,w_8$.
  - p. 1179: Eq. 35.66 starts with $p(s_1)$ though the product starts at $t=0$.
  - p. 1180: Eq. 35.71 writes $V_u(s,a)$ with a sum over $a$; $V$ seems intended as a function of $s$ only. The soft $Q$ in 35.68 is scaled by $\lambda^{-1}$ while 35.70 is not.
  - Fig. 35.4 (p. 1155): some episode-4 rows show next states that look inconsistent with a 1d chain (e.g. $(S_2,U,0,S_3)$, $(S_1,D,0,S_3)$). I could not check them against Figure 34.13, which is not in this unit.
- Symbol reuse: $\eta$ is the learning rate in most places but the "inverse temperature" in prioritized replay (p. 1156); $\epsilon$ and $\varepsilon$ are used for different things.
- The symbol $f^*$ in (35.82) and the "UTD ratio" (p. 1163) are not defined on these pages. References in brackets are not expanded here.
- Equations were checked against the page images; the text layer was readable throughout.
