---
id: bertsekas-2026-rlcourse/ch02-approximation-p6
work: bertsekas-2026-rlcourse
unit: "Chapter 2 (part 6/7): end of 2.9, 2.10 Bayesian optimization and sequential estimation, 2.11 adaptive control with a POMDP formulation, 2.12 minimax control (through the start of 2.12.2)"
pages: 296–321
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
# Rollout beyond the standard case: signaling policies, Bayesian optimization, adaptive control by belief averaging, minimax control

## L0 — One line
Rollout (replace the unknown optimal tail cost by the simulated cost of a base policy) carries over to belief-state problems and to worst-case (minimax) problems once the state, the expectation or the cost operator is redefined accordingly.

## L1 — The gist (≤ 120 words)
This part asks how rollout and approximation in value space extend beyond fully observed stochastic control. It treats four settings. First, autonomous multiagent rollout, which needs a signaling policy. Second, sequential estimation and Bayesian optimization, where the state is a posterior distribution (a belief). Third, adaptive control with an unknown parameter, posed as a POMDP (partially observed Markovian decision problem) and handled by Q-factors averaged over the belief. Fourth, minimax control, where an adversary replaces the expectation by a maximization. The common device is to replace the optimal tail cost, which is unavailable, by the cost of a base policy. Exact DP is typically impractical in the Bayesian and POMDP settings, which is why approximation matters.

**Prerequisites:** finite-horizon DP and Bellman equation; Q-factors and one-step lookahead; conditional probability and Bayes' rule; law of iterated expectations; the base-policy rollout idea from earlier in Chapter 2.

## L2 — Key ideas
- **Signaling policy.** In autonomous multiagent rollout each agent assumes preceding agents follow a precomputed signaling policy $\hat\mu$, so computation is parallel and needs no communication. Using the base policy as $\hat\mu$ gives no policy-improvement guarantee and can fail with identical agents ("groupthink"). An alternative is to approximate the sequential multiagent rollout policy, which may give approximate policy improvement (p. 296–297).
- **BO as DP over beliefs.** In Bayesian optimization the state is the posterior $b_k$ of the function-value vector $\theta$, and the action is the next point to observe. Exact DP over posteriors is practically infeasible even in the Gaussian case, except in simple cases (p. 303–304).
- **Myopic acquisition vs rollout.** The popular myopic method maximizes an acquisition function. Rollout instead computes Q-factors with a base policy, which may itself be a greedy acquisition policy, so it looks ahead several steps (p. 304–307).
- **Multiagent rollout for simultaneous observations.** Policy improvement is done one agent at a time, so computation grows linearly rather than exponentially with the number of observations. The cost improvement property can be shown to be preserved (p. 308).
- **Adaptive control as a POMDP.** With perfectly observed $x_k$ and an unknown parameter $\theta$ taking $m$ known values, the belief state is $(x_k,b_k)$. Approximation in value space averages per-parameter costs with weights $b_{k,i}$ (p. 309–313).
- **Strictly a rollout only if one base policy is used.** If the base policies $\pi^i$ differ across $i$, the scheme is "rollout-like". If all $\pi^i=\pi$, it is a legitimate rollout, and a cost improvement property can be shown (p. 313).
- **Deterministic systems and Wordle.** In the deterministic case no expectation over $w_k$ is needed. Wordle fits this case (mystery list as state), and rollout is reported to perform remarkably close to optimal (p. 314–316).
- **Minimax DP.** The expectation in Bellman's equation is replaced by maximization over disturbances. One-step lookahead and rollout carry over, and, for finite state, control and disturbance spaces, the rollout tail cost is a longest-path problem (p. 318–321).

## L3 — Walkthrough

### End of 2.9: autonomous multiagent rollout and the signaling policy
The scheme itself is defined on the preceding page, which is outside this unit. Eq. (2.92) shows it. At stage $k$ and state $x_k$, agent $\ell$ minimizes over its own control $u_k^\ell$ the expected stage cost plus the base-policy tail cost $J_{k+1,\pi}$. In that expression agents $1,\dots,\ell-1$ use the signaling-policy values $\hat\mu_k^1(x_k),\dots,\hat\mu_k^{\ell-1}(x_k)$, and agents $\ell+1,\dots,m$ use the base-policy components $\mu_k^{\ell+1}(x_k),\dots,\mu_k^m(x_k)$ (p. 296). The signaling values are precomputed and known to all agents. So the $m$ computations can run asynchronously, in parallel and without direct coordination (p. 296).

The simplest choice is $\hat\mu=\mu$, the base policy. It does not guarantee policy improvement (Example 2.9.3, cited, not in this unit), and deterioration is "not uncommon" (p. 296).

**Example 2.9.4 (spiders and flies, base policy as signaling).** Two spiders and two flies lie on a line (the setting of Example 2.9.1). The base policy moves a spider toward the closest surviving fly, and to the right from the midpoint. If the spiders start at different positions, the rollout policy is optimal (they move in opposite directions). If they start at the same position, the situation is fully symmetric. The rollout controls then move both spiders toward the fly furthest away (to the left from the midpoint). The spiders oscillate around the middle and never catch the flies (p. 296). The page prints "flies" where "spiders" is meant for the moved objects (see Reading notes).

The author calls this representative of counterexamples with multiple identical agents. If the agents start from the same state, the base policy has identical components and is used for signaling, then the agents choose identical controls. This can cause serious cost deterioration (p. 297).

Sequential choice of $u_k^1,\dots,u_k^m$ in the reformulated problem tends to break symmetries and "groupthink". Any sensible multiagent policy must handle this somehow. One simple possibility is for each agent to randomize somehow the other agents' controls when choosing its own, particularly when the problem is tightly coupled (p. 297). Alternatives for $\hat\mu_k$:
- Approximate the sequential multiagent rollout policy, or another policy known to embody coordination.
- Take the rollout policy of a simpler related problem, such as a certainty-equivalent (deterministic) version.
- Train a neural network (or $m$ networks) off-line on samples generated by the sequential multiagent rollout policy. The author "intuitively expect[s]" this to beat the base policy. A multi-robot repair case study confirmed it (p. 297).

The advantage: it may give approximate policy improvement while allowing asynchronous operation without communication of rollout control values. All agents are still assumed to know the exact state (p. 297).

*Intuition note.* Each agent must guess what the earlier agents will do. If the guess is "the base policy", and the agents are identical and start in the same state, they all guess the same thing and then all act the same way, which can be bad. A guess that already reflects coordination avoids this.

### 2.10 Rollout for Bayesian optimization and sequential estimation
**Setting.** Observations are used for inference, but their number and type are not fixed in advance. Outcomes are evaluated on-line, with a view to stopping or modifying observation. This is sequential decision making. The goal is to estimate an $m$-dimensional random vector $\theta$ by sequentially choosing observations based on feedback from earlier ones (Fig. 2.10.1) (p. 297–298).

**Example 2.10.1 (sequential probability ratio test).** Two hypotheses. Each observation costs $C$. After each observation we either accept a hypothesis or pay $C$ for another observation. The trade-off is observation cost against a higher probability of accepting the wrong hypothesis. Intuitively, stop once the conditional probability of one hypothesis given the data is close enough to 1. The author says classical DP analyses bear this out. The simple version has an elegant optimal solution, the sequential probability ratio test. Versions with multiple hypotheses and/or observation types are computationally intractable, so suboptimal methods are needed (p. 298).

**Dividing line.** If the choice of observation affects the cost and availability of future observations, the problem can often be viewed most fruitfully as combined estimation and control (adaptive control, next section; Wordle and Mastermind-type sequential decoding are examples). If observation choices are "independent" and do not affect cost or availability of future observations, the problem is substantially simpler. This section treats the second case, starting with surrogate and Bayesian optimization (p. 299).

**Surrogate optimization.** The aim is to minimize approximately a "black box" function. Its analytical form is unknown, and its values at a point may be hard to compute (costly simulation or experiments). A parametrized model with parameter $\theta$ (the surrogate) is built from observations at a few points, then minimized. The question is how to choose observation points sequentially, often with an exploration–exploitation tradeoff: observe where values look near-optimal, or in unexplored areas (Fig. 2.10.2) (p. 299–300).

**Bayesian optimization (BO).** It is used for functions whose values need time-consuming calculation or experiments. Applications named: kriging, for locating gold from a few boreholes; and selecting hyperparameters of machine-learning models, including AlphaZero's network architecture (p. 299–300).

*Formulation (p. 300–302).* Here the surrogate is parametrized by the function's values at its points.
- Minimize a real-valued $f$ over the finite set $\{1,\dots,m\}$. The finite domain is chosen to ease rollout, and infinite domains are possible in general (footnote, p. 300).
- Write $\theta_u=f(u)$, so $\theta=(\theta_1,\dots,\theta_m)\in\Re^m$ represents $f$ (Fig. 2.10.3).
- The key BO idea: function values change relatively slowly, so one observation informs neighbouring points. A limited number of well-chosen observations can then approximate the function over a large part of the search space (p. 301).
- At each of $N$ times we choose $u_k\in\{1,\dots,m\}$ and observe
$$z_{u_k}=\theta_{u_k}+w_{u_k}.\tag{2.93}$$
- The observation points are the controls. Policies choose $u_k$ knowing the earlier $z_{u_1},\dots,z_{u_{k-1}}$.
- The noises $w_u$ are independent with given distributions. $\theta$ has a given prior $b_0$. The posterior given observations $\{z_{u_1},\dots,z_{u_k}\}$ is $b_k$ (p. 301–302).
- *Gaussian special case.* $b_0$ and the noises are Gaussian. $b_0$ is defined by a mean and a covariance matrix. Correlation between $u$ and $u'$ is greater for "close" points, e.g. decreasing exponentially with Euclidean distance. Then $b_k$ is multidimensional Gaussian and is computable in closed form (p. 302).
- In general
$$b_{k+1}=B_k(b_k,u_{k+1},z_{u_{k+1}}),\quad k=0,\dots,N-1,\tag{2.94}$$
where $B_k$ is a recursive estimator. It is closed-form in the Gaussian case. Otherwise it may be implemented by simulation, sampling from the current posterior (p. 302).
- At the end, from $b_N$ one may use the posterior mean $\hat\theta$ as surrogate and declare $u^*\in\arg\min\{\hat\theta_u\mid u=1,\dots,m\}$ (Fig. 2.10.4, noise-free example with 10 observations, where the posterior mean is exact at the observed points) (p. 302–303).

*Intuition note.* BO treats the unknown function as a random vector and updates beliefs after each costly evaluation. The real decision is where to evaluate next.

**DP formulation (p. 303–304).** The state is the posterior $b_k$ (belief state). The action is the next point index $u_{k+1}$. Observing $\theta_u$ costs $c(u)$. There is a terminal cost $G(b_N)$, e.g. involving the mean and covariance of $b_N$. The DP algorithm is
$$J_k^*(b_k)=\min_{u_{k+1}\in\{1,\dots,m\}}\Big[c(u_{k+1})+E_{z_{u_{k+1}}}\big\{J^*_{k+1}\big(B_k(b_k,u_{k+1},z_{u_{k+1}})\big)\,\big|\,b_k,u_{k+1}\big\}\Big],\tag{2.95}$$
$$J_N^*(b_N)=G(b_N).\tag{2.96}$$
The expectation is over the conditional distribution of $z_{u_{k+1}}$ given $b_k,u_{k+1}$. $c(u)$ may be 0, constant or more complex. $G$ may measure surrogate "fidelity" (p. 304). Exact DP is generally practically infeasible because the space of posteriors is infinite-dimensional. In the Gaussian case, $b_k$ is fixed by a mean and covariance (finitely many numbers). Even so, (2.95) is prohibitively time-consuming except in simple special cases. Hence approximation in value space: replace $J^*_{k+1}$ by $\tilde J_{k+1}$ (p. 304).

**Approximation in value space (p. 304–305).**
- *Myopic/greedy BO.* The most popular method picks
$$\hat u_{k+1}\in\arg\max_{u_{k+1}\in\{1,\dots,m\}}A_k(b_k,u_{k+1}),\tag{2.97}$$
where the acquisition function $A_k$ quantifies some "expected benefit" of observing at $u_{k+1}$.
- *Upper confidence bound (footnote).* $A_k(b_k,u)=T_k(b_k,u)+\beta R_k(b_k,u)$. Here $T_k$ is the negative of the posterior mean of $f(u)$ (exploitation index), $R_k$ is the posterior standard deviation (exploration index), and $\beta>0$ is tunable. Another popular choice is expected improvement: the expected reduction of $f(u)$ relative to the minimal value of $f$ found up to time $k$ (p. 304–305, footnote).
- *Value-space approach.* Choose
$$\tilde u_{k+1}\in\arg\min_{u_{k+1}\in\{1,\dots,m\}}Q_k(b_k,u_{k+1}),\tag{2.98}$$
$$Q_k(b_k,u_{k+1})=c(u_{k+1})+E_{z_{u_{k+1}}}\Big\{\tilde J_{k+1}\big(B_k(b_k,u_{k+1},z_{u_{k+1}})\big)\,\Big|\,b_k,u_{k+1}\Big\}.\tag{2.99}$$
The expectation uses the distribution of $z$ given $(b_k,u_{k+1})$, computable from $b_k$ and the noise distribution. If $b_k$ and $\tilde J_{k+1}$ are available, Monte Carlo simulation can give all $m$ Q-factors (p. 305).

**Rollout for BO (p. 305–307).**
- Rollout takes $\tilde J_{k+1}$ to be the cost function of a base policy $\mu_{k+1}(b_k)$. Its values can be computed or approximated by simulation.
- Greedy acquisition-function policies have been suggested as base policies in various rollout proposals. The footnote names Lam, Wilcox, Wolpert [LWW16] as first proposing BO rollout under Gaussian assumptions, and says the papers cited generally report "encouraging computational results" (p. 306).
- For each $u_{k+1}$, the Q-factor is computed by simulating the base policy for several steps from all posteriors $b_{k+1}$ reachable from $(b_k,u_{k+1})$, accumulating cost including a terminal cost such as $G(b_N)$ (Fig. 2.10.5). The horizon may be truncated after a few steps (p. 306–307).
- The belief update is stochastic because $z$ involves noise, so some Monte Carlo is unavoidable. The burden can be reduced by *certainty equivalence*: at stage $k$ only $w_{u_{k+1}}$ is treated as stochastic, and later noises $w_{u_{k+2}},\dots$ are replaced by deterministic values such as their means (p. 307).
- If $m$ is very large, compute Q-factors only for a subset $U_{k+1}$ of the most promising observations, ranked by an acquisition function. This was used for Wordle in [BBB22], [BBB23] (p. 307).

*Intuition note.* Myopic BO asks which single next point looks best now. Rollout asks which point leads, after a sensible follow-up heuristic, to the best final outcome, and so looks further ahead.

**Multiagent rollout for BO (p. 307–308).** Sometimes several observations are made simultaneously before any feedback. Two contexts are given: (a) parallel computation, with several processors evaluating $f$ at several points, each with simulation noise; (b) distributed sensor systems. Treating the set of simultaneous observations as one observation in a Cartesian product space makes the number of Q-factors grow exponentially with the number of simultaneous observations. Multiagent rollout instead improves one agent at a time, in a given order, with possibly partial knowledge of the preceding agents' choices. Computation per policy improvement then grows linearly in the number of agents. The cost improvement property of rollout "can be shown to be preserved". Empirical evidence suggests great computational savings with hardly any performance degradation (p. 308).

**Generalization (p. 308–309).** A class containing BO as a special case estimates an $m$-dimensional $\theta$ with $N$ linear observations
$$z_u=a_u'\theta+w_u,\qquad u\in\{1,\dots,n\},$$
with known vectors $a_u$ and independent noises $w_u$. If the prior of $\theta$ and the noises are Gaussian, the posterior is Gaussian by linearity and computable in closed form. At time $k$ we choose $u_k\in\{1,\dots,n\}$ at cost $c(u_k)$. The objective is, roughly, to minimize a cost penalizing some estimation error plus observation cost. This can be formulated as $N$-stage DP, and rollout algorithms can be developed (p. 308–309).

### 2.11 Adaptive control by rollout with a POMDP formulation
**Setting (p. 309–310).** POMDP (partially observed Markovian decision problems) are among the most challenging DP problems and nearly always need approximation. The special class considered has two state components:
- a perfectly observed $x_k$;
- an unobserved constant $\theta$, estimated through the observed $x_k$.

The dynamics are
$$x_{k+1}=f_k(x_k,\theta,u_k,w_k),\tag{2.100}$$
with $u_k\in U_k(x_k)$ and $w_k$ a disturbance whose distribution depends on $(x_k,\theta,u_k)$. We assume $\theta\in\{\theta^1,\dots,\theta^m\}$ (Fig. 2.11.1). With information vector $I_k=\{x_0,\dots,x_k,u_0,\dots,u_{k-1}\}$ define
$$b_{k,i}=P\{\theta=\theta^i\mid I_k\},\quad i=1,\dots,m,\qquad b_k=(b_{k,1},\dots,b_{k,m}).$$
The pair $(x_k,b_k)$ is the *belief state*. The update is $b_{k+1}=B_k(x_k,b_k,u_k,x_{k+1})$, a recursive estimator of $\theta$, implementable by Bayes' rule or particle filtering (possibly approximately). With each $\theta^i$ a set of system parameters, $b_{k,i}$ is the outcome of a system identification algorithm and the problem becomes *dual control*, whose optimal solution is "notoriously difficult". Search problems (e.g. Wordle), where $\theta$ gives the location of hidden objects, also fit (p. 310). The footnote says this approach does not assume the a-priori split between identification and policy reoptimization of indirect adaptive control (p. 309).

**Exact DP and approximation in value space (p. 311–312).** Take $I_k$ as state, with $I_{k+1}=(I_k,x_{k+1},u_k)=\big(I_k,f_k(x_k,\theta,u_k,w_k),u_k\big)$. Then
$$J_k^*(I_k)=\min_{u_k\in U_k(x_k)}E_{\theta,w_k}\Big\{g_k(x_k,\theta,u_k,w_k)+J^*_{k+1}\big(I_k,f_k(x_k,\theta,u_k,w_k),u_k\big)\,\Big|\,I_k,u_k\Big\},\tag{2.101}$$
for $k=0,\dots,N-1$, with $J_N(I_N)=g_N(x_N)$. It is typically very hard to implement, in part because $J^*_{k+1}$ depends on the growing vector $I_{k+1}$ (p. 311).

Replace $J^*_{k+1}$ by $\tilde J_{k+1}(I_{k+1})$ such that
$$E_{\theta,w_k}\{\tilde J_{k+1}(I_{k+1})\mid I_k,u_k\}\tag{2.102}$$
is tractably computable. Useful case: $E_{w_k}\{\tilde J_{k+1}(I_{k+1})\mid I_k,\theta^i,u_k\}$ is tractable for each fixed $\theta^i$. Then, by the law of iterated expectations $E_{\theta,w_k}\{\cdot\mid I_k,u_k\}=E_\theta\{E_{w_k}\{\cdot\mid I_k,\theta,u_k\}\mid I_k,u_k\}$,
$$E_{\theta,w_k}\{\tilde J_{k+1}(I_{k+1})\mid I_k,u_k\}=\sum_{i=1}^m b_{k,i}\,E_{w_k}\{\tilde J_{k+1}(I_{k+1})\mid I_k,\theta^i,u_k\}\quad(p.\ 311\text{–}312).$$

*Choice 1: per-parameter optimal costs.* Let $\hat J^i_{k+1}(x_{k+1})$ (2.103) be the optimal cost from $x_{k+1}$ if $\theta=\theta^i$ (a perfect state information problem). Then
$$\tilde u_k\in\arg\min_{u_k\in U_k(x_k)}\sum_{i=1}^m b_{k,i}E_{w_k}\Big\{g_k(x_k,\theta^i,u_k,w_k)+\hat J^i_{k+1}\big(f_k(x_k,\theta^i,u_k,w_k)\big)\,\Big|\,x_k,\theta^i,u_k\Big\}.\tag{2.104}$$
That is, instead of minimizing the optimal Q-factor of $(I_k,u_k)$, we minimize the expected value over $\theta$ of the optimal Q-factors for fixed $\theta$ (p. 312).

For an infinite horizon, it is "reasonable to expect" that a suitable estimator converges, $\lim_k b_{k,i}=1$ if $\theta^i=\theta^*$ and $0$ otherwise. Then the controls $\tilde u_k$ are asymptotically obtained from the Bellman equation for the correct $\theta^*$, and are "typically optimal in some asymptotic sense". Such schemes have been discussed in the adaptive control literature since the 1970s (p. 312).

The costs $\hat J^i$ may be hard to compute. In favourable cases (e.g. linear quadratic) they are closed-form, but the beliefs $b_{k,i}$ may still need system identification (footnote, p. 312). Alternatives: off-line trained approximations (neural networks), or rollout (p. 312).

*Choice 2: rollout and cost improvement (p. 313).* Use the cost $\hat J^i_{k+1,\pi^i}$ of a given policy $\pi^i=\{\mu^i_0,\dots,\mu^i_{N-1}\}$ in place of $\hat J^i_{k+1}$:
$$\tilde u_k\in\arg\min_{u_k\in U_k(x_k)}\sum_{i=1}^m b_{k,i}E_{w_k}\Big\{g_k(x_k,\theta^i,u_k,w_k)+\hat J^i_{k+1,\pi^i}\big(f_k(x_k,\theta^i,u_k,w_k)\big)\,\Big|\,x_k,\theta^i,u_k\Big\}.\tag{2.105}$$
The components $\mu_k^i$ depend only on $x_k$. $\hat J^i_{k+1,\pi^i}$ is the cost of $\pi^i$ from $x_{k+1}=f_k(x_k,\theta^i,u_k,w_k)$, assuming $\theta$ stays fixed at $\theta^i$ to the end. It can be computed by Monte Carlo simulation because $\mu^i_k$ depends only on $x_k$, not on $I_k$ or the belief state (p. 313).

Strictly it is not rollout, because $\mu^i_k$ depends on $i$ as well as $x_k$. If all $\pi^i=\pi$, then $\mu_k$ depends only on $x_k$ and is a legitimate base policy. The scheme then replaces $E_{w_k}\{J^*_{k+1}(I_{k+1})\mid I_k,u_k\}$ in (2.101) by $E_{w_k}\{J_{k+1,\pi}(I_{k+1})\mid I_k,u_k\}$. As in Section 2.7, a cost improvement property can then be shown. Such a $\pi$ should be a *robust* policy, one that works adequately for all $\theta^i$. How to get one is likely problem-dependent (p. 313).

*Intuition note.* We pretend, one candidate parameter at a time, that the parameter is known and fixed. We simulate a fixed base policy to the end, and average the resulting Q-factors with the current belief as weights. The first control comes from this average.

**Deterministic system (p. 314–315).** Let $x_{k+1}=f_k(x_k,\theta,u_k)$ (2.106). There is no expectation over $w_k$, and (2.105) becomes
$$\tilde u_k\in\arg\min_{u_k\in U_k(x_k)}\sum_{i=1}^m b_{k,i}\Big(g_k(x_k,\theta^i,u_k)+\hat J^i_{k+1,\pi^i}\big(f_k(x_k,\theta^i,u_k)\big)\Big).\tag{2.107}$$
Define the Q-factor and its belief average:
$$Q_k(x_k,u_k,\theta^i)=g_k(x_k,\theta^i,u_k)+\hat J^i_{k+1,\pi^i}\big(f_k(x_k,\theta^i,u_k)\big),\tag{2.108}$$
$$\hat Q_k(x_k,u_k)=\sum_{i=1}^m b_{k,i}Q_k(x_k,u_k,\theta^i),\qquad \tilde u_k\in\arg\min_{u_k\in U_k(x_k)}\hat Q_k(x_k,u_k).\tag{2.109}$$
$Q_k$ must be computed for every pair $(u_k,\theta^i)$ using $\pi^i$ (Fig. 2.11.2). Because each state $x_k$ is a noiseless measurement relating to $\theta$, one can "typically expect" $\theta^*$ to be identified in finitely many stages. The problem then becomes one of perfect state information (p. 314). For stochastic systems the same picture applies, with Q-factors $Q_k(x_k,u_k,\theta^i,w_k)$ for every triplet $(u_k,\theta^i,w_k)$, averaged over $(\theta,w_k)$ (p. 314–315).

**Example 2.11.1 (Wordle).** The aim is to guess a mystery word $\theta^*$ from a known finite collection of 5-letter words, using sequential guesses. Each guess shrinks the *mystery list* (the smallest list known to contain $\theta^*$). The objective is to minimize the number of guesses; more than 6 counts as a loss. The shrinking rules are not described (p. 315). If $\theta^*$ is uniform over the initial collection, the belief $b_k$ stays uniform over the current mystery list. The state $x_k$ can then be the mystery list, evolving deterministically as in (2.106) with $u_k$ the guess word. Several base policies for algorithm (2.107) are in [BBB22], [BBB23]. The author reports that the rollout algorithm "performs remarkably close to the optimal policy". That optimal policy was first obtained by a very computationally intensive exact DP calculation by Selby in 2022. Variants (longer words, nonuniform known distribution) are also covered by rollout (p. 316).

**Sequential estimation as a special case (p. 316–317).** Sequential estimation is the special case $x_{k+1}=f_k(\theta,u_k,w_k)$. The new observation $x_{k+1}$ does not depend explicitly on $x_k$, but depends on the decision $u_k$ and the disturbance $w_k$ (Fig. 2.11.3). Other rollout algorithms can be used. The BO rollouts of Section 2.10 use base policies that depend on the belief state $b_k$ rather than $x_k$. Section 6.7 of [Ber22a] gives another adaptive-control example with a belief-dependent base policy (p. 317).

### 2.12 Minimax control and reinforcement learning
**Motivation (p. 317–318).** Often only a set containing the disturbances is known, not their distribution. The *minimax* approach minimizes the cost assuming the worst disturbances occur. An antagonistic opponent, the *maximizer*, chooses $w_k$ to maximize the cost, and the controller is the *minimizer*. The footnote lists other names: robust control, robust optimization, set-membership uncertainty, games against nature. The main difference from stochastic control is that disturbances are chosen by maximization rather than randomization, so the expectation is replaced by a maximization (p. 317–318).

*Roadmap (p. 318).*
- Section 2.12.2: approximate $J^*$ by $\tilde J$. The minimizer uses lookahead minimization and the maximizer maximizes exactly. Rollout is the case where $\tilde J$ is the cost of a minimizer policy.
- Section 2.12.3: approximation in policy space as well. A policy $\nu(x,u)$ for the maximizer is chosen to emulate maximization, which leaves a one-player problem for the minimizer. It is extended briefly to distributionally robust control.
- Section 2.12.4: computer chess and two-person games.

Only the start of 2.12.2 lies within this unit.

**2.12.1 Exact DP for minimax problems (p. 318–321).** Finite horizon: $w_k\in W_k(x_k,u_k)$. Find $\pi=\{\mu_0,\dots,\mu_{N-1}\}$, $\mu_k(x_k)\in U_k(x_k)$, minimizing
$$J_\pi(x_0)=\max_{\substack{w_k\in W_k(x_k,\mu_k(x_k))\\k=0,\dots,N-1}}\Big[g_N(x_N)+\sum_{k=0}^{N-1}g_k\big(x_k,\mu_k(x_k),w_k\big)\Big].$$
The DP algorithm, like the stochastic one with maximization in place of expectation, is
$$J_N^*(x_N)=g_N(x_N),\tag{2.110}$$
$$J_k^*(x_k)=\min_{u_k\in U(x_k)}\ \max_{w_k\in W_k(x_k,u_k)}\Big[g_k(x_k,u_k,w_k)+J^*_{k+1}\big(f_k(x_k,u_k,w_k)\big)\Big].\tag{2.111}$$
*Justification (principle of optimality).* Consider the tail subproblem from $x_k$, minimizing $\max_{w_t\in W_t(x_t,\mu_t(x_t)),\,t=k,\dots,N-1}\big[g_N(x_N)+\sum_{t=k}^{N-1}g_t(x_t,\mu_t(x_t),w_t)\big]$. If $\pi^*$ is optimal for the minimax problem, its tail $\{\mu^*_k,\dots,\mu^*_{N-1}\}$ is optimal for the tail subproblem, with optimal cost $J_k^*(x_k)$. At $x_k$, regardless of the past, choose $u_k$ to minimize the worst value over $w_k$ of stage cost plus optimal tail cost from the next state. The argument requires a mathematical proof with "a few fine points" (see [Ber17a], Sec. 1.6). The algorithm is correct assuming finite state and control spaces, among other cases (p. 319).

*Zero-sum games (p. 319–320).* Two related problems:
- (a) *min-max*: the minimizer picks its policy first and the maximizer picks second knowing it. The DP is (2.110)–(2.111) form.
- (b) *max-min*: the maximizer picks first. The DP is $\hat J_N=g_N$, $\hat J_k(x_k)=\max_{w_k}\min_{u_k}\big[g_k+\hat J_{k+1}(f_k)\big]$.

A basic and easily seen fact: Max-Min optimal value $\le$ Min-Max optimal value. Conditions guaranteeing equality (2.112) are the focus of the game-theory literature, but are of limited interest for worst-case engineering design. The author does not discuss them because approximations disrupt the delicate assumptions that guarantee equality (p. 320).

*Infinite horizon (p. 320–321).* $f,g,U,W$ do not depend on $k$. The discounted cost is
$$J_\pi(x_0)=\lim_{N\to\infty}\ \max_{\substack{w_k\in W(x_k,u_k)\\k=0,1,\dots}}\Big\{\sum_{k=0}^{N-1}\alpha^k g\big(x_k,\mu_k(x_k),w_k\big)\Big\},\tag{2.113}$$
with $\alpha<1$. If $g$ is bounded, the limit exists and is finite. Then $J^*$ is finite-valued and is the unique solution of
$$J^*(x)=\min_{u\in U(x)}\max_{w\in W(x,u)}\Big[g(x,u,w)+\alpha J^*\big(f(x,u,w)\big)\Big],\quad\text{for all }x.\tag{2.114}$$
A stationary policy $\mu^*$ is optimal if and only if $\mu^*(x)$ attains the minimum in Bellman's equation for all $x$. Analogs of value and policy iteration are valid under the same circumstances. Policy iteration "involves some subtleties and requires modifications" (footnote). The results follow from analyses of abstract DP in which the Bellman operator is a contraction mapping (p. 320). For undiscounted problems ($\alpha=1$), which usually have a cost-free termination state, the results hold if the number of stages to reach termination is bounded regardless of both players' choices. This holds in many computer games, such as chess (p. 321).

**2.12.2 Minimax approximation in value space and rollout (start; p. 321).** One-step lookahead for finite horizon is
$$\tilde u_k\in\arg\min_{u_k\in U_k(x_k)}\ \max_{w_k\in W_k(x_k,u_k)}\Big[g_k(x_k,u_k,w_k)+\tilde J_{k+1}\big(f_k(x_k,u_k,w_k)\big)\Big],\tag{2.115}$$
with $\tilde J_{k+1}$ approximating $J^*_{k+1}$. *Rollout* sets $\tilde J_{k+1}=J_{k+1,\pi}$, the tail cost of a base policy $\pi$. Given $\pi$, $J_{k+1,\pi}(x_{k+1})$ is computed by a deterministic maximization DP problem with $w_{k+1},\dots,w_{N-1}$ as the "controls". For finite state, control and disturbance spaces this is a longest-path problem on an acyclic graph, since the base policy fixes $u_{k+1},\dots,u_{N-1}$. Implementation: from $x_k$ generate all next states $f_k(x_k,u_k,w_k)$ over all $u_k\in U_k(x_k)$, $w_k\in W_k(x_k,u_k)$. Run the longest-path computation from each one. Then solve the minimax problem (2.115). Truncated rollout can approximate the tail cost. Like all rollout, it suits on-line replanning when data change or are revealed during control selection (p. 321).

*Intuition note.* Minimax rollout assumes nature plays the worst disturbance against our fixed follow-up policy. We then pick the first control whose worst case is smallest.

## Toy example (ours; not from the text)
Illustrates the belief-averaged deterministic rollout (2.107)–(2.109) with $m=2$.

Setup: scalar state, $x_{k+1}=x_k+\theta u_k$, $\theta\in\{\theta^1,\theta^2\}=\{1,2\}$. We are at $x_k=3$. Stage cost is $x^2+u^2$ at the second stage, and just $u^2$ at stage $k$. After stage $k$ there are two more steps simulated with base policy $\pi^i=\pi$, the same for both $i$ ($u'=-1$ if $x>0$, else $0$). Tail cost from $x_{k+1}$: $x_{k+1}^2+u'^2+x_{k+2}^2$, with $\theta$ held fixed. Controls: $u\in\{0,-1,-2\}$.

- $u=0$: $x_{k+1}=3$, $u'=-1$. $\theta^1$: $x_{k+2}=2$, tail $9+1+4=14$, $Q=0+14=14$. $\theta^2$: $x_{k+2}=1$, tail $9+1+1=11$, $Q=11$.
- $u=-1$ (stage cost 1): $\theta^1$: $x_{k+1}=2$, $u'=-1$, $x_{k+2}=1$, tail $4+1+1=6$, $Q=7$. $\theta^2$: $x_{k+1}=1$, $u'=-1$, $x_{k+2}=-1$, tail $1+1+1=3$, $Q=4$.
- $u=-2$ (stage cost 4): $\theta^1$: $x_{k+1}=1$, $u'=-1$, $x_{k+2}=0$, tail $1+1+0=2$, $Q=6$. $\theta^2$: $x_{k+1}=-1$, $u'=0$, $x_{k+2}=-1$, tail $1+0+1=2$, $Q=6$.

Belief $b=(0.75,0.25)$: $\hat Q(0)=0.75\cdot14+0.25\cdot11=13.25$. $\hat Q(-1)=0.75\cdot7+0.25\cdot4=6.25$. $\hat Q(-2)=6$. The rollout control is $u=-2$.

Belief $b=(0.1,0.9)$: $\hat Q(0)=1.4+9.9=11.3$. $\hat Q(-1)=0.7+3.6=4.3$. $\hat Q(-2)=6$. The rollout control is $u=-1$.

So the same base policy gives different controls under different beliefs. In general $\hat Q(-1)=4+3b_1<6$ exactly when $b_1<2/3$.

## Concepts
- [[rollout]] (new) — one-step lookahead whose tail cost is the simulated cost of a base policy; here applied to belief-state and minimax problems (p. 305, 321)
- [[multiagent-rollout]] (new) — policy improvement one agent at a time, giving linear instead of exponential computation (p. 308)
- [[signaling-policy]] (new) — precomputed policy $\hat\mu$ giving the preceding agents' assumed controls in autonomous multiagent rollout (p. 296)
- [[surrogate-optimization]] (new) — minimize a black-box function by estimating a parametric surrogate from sequentially chosen observations (p. 299)
- [[bayesian-optimization]] (new) — surrogate optimization with a posterior over function values $\theta$, updated after each noisy observation (p. 299, 301–302)
- [[acquisition-function]] (new) — index $A_k(b_k,u)$ scoring the expected benefit of observing at $u$; maximized by myopic BO (p. 304–305)
- [[belief-state]] (new) — the posterior over the hidden quantity, alone in BO and paired with $x_k$ in adaptive control (p. 303, 310)
- [[pomdp]] (new) — partially observed MDP; here the special case of a perfectly observed $x_k$ plus a constant hidden $\theta$ (p. 309)
- [[dual-control]] (new) — combined identification and control problem; optimal solution "notoriously difficult" (p. 310)
- [[exploration vs exploitation]] — observing near-optimal points versus unexplored areas (p. 299, 301)
- [[model-based vs model-free RL]] — system identification with policy reoptimization is contrasted here with the POMDP approach (p. 309, footnote)
- [[Bellman equation / value function]] — minimax form (2.114) with max over $w$ (p. 320)
- [[principle of optimality]] — used to justify the minimax DP algorithm (p. 319)
- [[minimax-control]] (new) — control against worst-case disturbances from a known set, with no probability distribution (p. 317)
- [[robustness]] — here, a base policy $\pi$ that works adequately for all $\theta^i$ (p. 313)
- [[Markov decision process]] — the term underlying POMDP (partially observed Markovian decision problem); not discussed on its own in this unit (p. 309)

## Canonical instances
- [[spiders-and-flies]] — shows that using the base policy as signaling policy can fail through symmetry (p. 296)
- [[sequential-probability-ratio-test]] — optimal stopping rule for binary hypothesis testing (p. 298)
- [[kriging-gold-boreholes]] — classical geostatistical BO application (p. 299)
- [[wordle]] — deterministic adaptive control / search problem; rollout near optimal (p. 315–316)

## Bridges (candidates)
- [structural-analogy] Posterior update $b_{k+1}=B_k(\cdot)$ ↔ control-theory: observer/state estimator — a recursive estimator of a hidden quantity, though here it is Bayesian and the state is a distribution (p. 302, 310).
- [structural-analogy] Gaussian posterior update with linear observations $z_u=a_u'\theta+w_u$ ↔ control-theory: Kalman-type estimation — the text says closed-form Gaussian estimation applies (p. 308); whether the formulas coincide with the Kalman filter is not stated here, so confirm.
- [structural-analogy] Belief-averaged Q-factors, with a fixed policy for each fixed $\theta^i$ ↔ certainty equivalence / indirect adaptive control — the unknown parameter is treated as known and the results are averaged (p. 312–314).
- [structural-analogy] Minimax DP with an adversarial maximizer ↔ robust control and zero-sum games — footnote lists these names (p. 317).

## Questions this raises
- When the base policy is the signaling policy and the agents are non-identical, can the improvement failure of Example 2.9.4 still occur?
- In (2.105), what price is paid in performance when the $\pi^i$ differ across $i$, given that the cost improvement property is claimed only for a common $\pi$?
- How good is a certainty-equivalence approximation of the noise in BO rollout compared with full Monte Carlo?
- Once approximation is introduced, what does the minimax equality (2.112) failing mean for the choice between min-max and max-min designs?

## Reading notes
- This is part 6 of 7 of Chapter 2. It starts mid-Section 2.9 (printed p. 296, in the sentence introducing Eq. (2.92)) and ends at printed p. 321 in the middle of 2.12.2, after the paragraph on on-line replanning. Sections 2.12.2 (remainder), 2.12.3 and 2.12.4 are outside this unit.
- Page offset: printed = pdf − 20.
- Example 2.9.4 on p. 296: the page says the rollout controls "move both flies" toward the fly furthest away. By the context, "spiders" is meant (spiders are the moving agents). It is reported here as spiders.
- Eq. (2.92) is garbled in the text layer. I read it from the image, which shows hats on the signaling values $\hat\mu$ and tildes on $\tilde\mu$.
- The zero-sum DP in (a) and (b) on p. 319 writes $W_k(x_k)$, while (2.111) writes $W_k(x_k,u_k)$. This is as printed.
- Small typos in the source: "requite" for "require" (p. 299); "a stationary policy $\mu^*$ policy" (p. 320); "depends of" (p. 303).
- The statement of the signaling policy scheme begins before p. 296, so (2.92) is described here from its display only.
