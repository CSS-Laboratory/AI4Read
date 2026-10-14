---
id: sutton-2018-rl/ch13-policy
work: sutton-2018-rl
unit: Chapter 13 — Policy Gradient Methods
pages: 321-338
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Policy Gradient Methods

## L0 — One line
Instead of learning action values and acting on them, learn a differentiable parameterized policy directly by stochastic gradient ascent on performance, using the policy gradient theorem, which gives that gradient without differentiating the state distribution.

## L1 — The gist (≤ 120 words)
Most earlier methods learned action values and derived the policy from them. This chapter learns a parameterized policy directly, by approximate gradient ascent on a performance measure J(θ). The policy gradient theorem gives the gradient of J without the derivative of the state distribution. From it follow REINFORCE (Monte Carlo), REINFORCE with a baseline (same expected update, variance often lower) and actor–critic methods (a learned critic; often lower variance, some bias). The theorem has the same form for episodic and continuing tasks (only the proportionality constant differs). Parameterized policies can approach determinism, can use chosen action probabilities, and can handle continuous actions, which ε-greedy action-value methods handle poorly or not at all.

**Prerequisites:** MDPs, value functions $v_\pi,q_\pi$, on-policy distribution μ, Monte Carlo and TD(0) returns, gradient ascent, product and chain rules, eligibility traces (Ch. 12).

## L2 — Key ideas (5–10 bullets)
- Policy-gradient methods update the policy parameter θ along an estimate of $\nabla J(\theta)$; a value function may help learning but is not needed to choose actions (p. 321).
- Soft-max over action preferences lets the policy approach determinism, or take any specific action probabilities. ε-greedy selection over action values has no natural way to do either (pp. 322–323).
- Policy gradient theorem: $\nabla J(\theta)\propto\sum_s\mu(s)\sum_a q_\pi(s,a)\nabla\pi(a|s,\theta)$, with no derivative of the state distribution (p. 326).
- REINFORCE samples this expression and updates with $G_t\nabla\pi/\pi$. It is a Monte Carlo method; its expected update is in the direction of the gradient, but it may have high variance and learn slowly (pp. 327–329).
- A baseline $b(s)$ (a term subtracted from the return) that does not depend on $a$ leaves the expected update unchanged but can have a large effect on its variance (p. 329).
- Actor–critic methods use a learned value function to form a one-step return. This often lowers variance, at the cost of some bias (p. 331).
- The continuing case uses average reward and differential return (returns measured relative to the average reward). The theorem has the same form, with proportionality constant 1 (pp. 326, 333–334).
- For continuous actions, learn the mean and standard deviation of a Gaussian policy (pp. 335–336).

## L3 — Walkthrough

### Introduction (p. 321)
In almost all earlier methods the policy came from action-value estimates (the lone exception, the gradient bandit algorithms, is named in a footnote). Here the policy has parameter $\theta\in\mathbb R^{d'}$, and $\pi(a|s,\theta)=\Pr\{A_t=a\mid S_t=s,\theta_t=\theta\}$. A learned value function, if used, has weights $w\in\mathbb R^d$ (p. 321). Updates approximate gradient ascent on a scalar performance measure $J(\theta)$:
$$\theta_{t+1}=\theta_t+\alpha\,\widehat{\nabla J(\theta_t)}\tag{13.1}$$
where $\widehat{\nabla J(\theta_t)}$ is a stochastic estimate whose expectation approximates the gradient (p. 321). Any method of this form is a *policy gradient method*. If it also learns a value function it is an *actor–critic* method: the actor is the policy, the critic the (usually state-) value function (p. 321). The episodic case is treated first, then the continuing case (pp. 321–322).

### 13.1 Policy approximation and its advantages (pp. 322–324)
- **Requirement:** $\nabla\pi(a|s,\theta)$ must exist and be finite. In practice, to ensure exploration the authors generally require that the policy never become deterministic: $\pi\in(0,1)$ for all $s,a,\theta$ (p. 322).
- **Soft-max in action preferences.** For discrete, not-too-large action sets, use numerical preferences $h(s,a,\theta)$ (p. 322):
$$\pi(a|s,\theta)\doteq\frac{e^{h(s,a,\theta)}}{\sum_b e^{h(s,b,\theta)}}\tag{13.2}$$
The preferences may come from a neural network, or be linear in features:
$$h(s,a,\theta)=\theta^\top x(s,a)\tag{13.3}$$
- **Advantage 1: can approach determinism.** ε-greedy always keeps probability ε of a random action. A soft-max over *action values* would not approach determinism either: the estimates converge to true values that differ by a finite amount, giving probabilities other than 0 and 1 (p. 322). A temperature schedule would be hard to choose without prior knowledge. Preferences do not converge to specific values. They are driven toward the optimal stochastic policy. If the optimal policy is deterministic, the optimal actions' preferences are driven infinitely above the rest, if the parameterization permits (p. 323).
- **Advantage 2: arbitrary action probabilities.** With heavy function approximation the best policy may be stochastic, as in bluffing in poker. Action-value methods have no natural way to find stochastic optimal policies (p. 323).
- **Example 13.1 (short corridor, switched actions).** Three nonterminal states, actions right/left, reward $-1$ per step. In the second state the actions' effects are reversed. All states look identical to the function approximator, with $x(s,\text{right})=[1,0]^\top$ and $x(s,\text{left})=[0,1]^\top$ (p. 323). An ε-greedy method must choose "right with probability $1-\varepsilon/2$" or "left with that probability" everywhere. For ε = 0.1 these have start-state values below −44 and −82. Choosing right with probability about 0.59 gives about −11.6 (p. 323).
- **Advantage 3:** the policy may be a simpler function than the action-value function, so a policy-based method will typically learn faster and reach a better asymptotic policy (Tetris cited); for other problems the action-value function is the simpler one (p. 324).
- **Advantage 4:** the parameterization injects prior knowledge. The authors call this often the most important reason for a policy-based method (p. 324).

> **Intuition note.** A policy can be tuned smoothly toward "almost always this action", or toward "this action about 59% of the time". An ε-greedy rule built on values has no natural way to do either: it always keeps probability ε of a random action.

### 13.2 The policy gradient theorem (pp. 324–326)
Continuous parameterization makes action probabilities change smoothly with θ. ε-greedy probabilities can jump when a different action becomes maximal. Largely for this reason, stronger convergence guarantees are available for policy-gradient methods (p. 324).

**Episodic performance.** Assume every episode starts in $s_0$ and $\gamma=1$ in the text (boxed algorithms keep γ):
$$J(\theta)\doteq v_{\pi_\theta}(s_0)\tag{13.4}$$
**Difficulty.** Performance depends on action choices and on the state distribution, and both depend on θ. The effect on the state distribution is typically unknown (pp. 324–326).

**Theorem (episodic).**
$$\nabla J(\theta)\propto\sum_s\mu(s)\sum_a q_\pi(s,a)\nabla\pi(a|s,\theta)\tag{13.5}$$
μ is the on-policy distribution under π. In the episodic case the constant of proportionality is the average episode length; in the continuing case it is 1 (p. 326).

**Proof (episodic, p. 325).** Gradients are with respect to θ.
1. $\nabla v_\pi(s)=\nabla\big[\sum_a\pi(a|s)q_\pi(s,a)\big]=\sum_a[\nabla\pi(a|s)q_\pi(s,a)+\pi(a|s)\nabla q_\pi(s,a)]$ (product rule).
2. Expand $q_\pi=\sum_{s',r}p(s',r|s,a)(r+v_\pi(s'))$. Since $p$ and $r$ do not depend on θ (added step), only $v_\pi$ does, so $\nabla v_\pi(s)=\sum_a[\nabla\pi(a|s)q_\pi(s,a)+\pi(a|s)\sum_{s'}p(s'|s,a)\nabla v_\pi(s')]$.
3. Unroll $\nabla v_\pi(s')$ the same way, repeatedly: $\nabla v_\pi(s)=\sum_{x\in\mathcal S}\sum_{k=0}^\infty\Pr(s\to x,k,\pi)\sum_a\nabla\pi(a|x)q_\pi(x,a)$, where $\Pr(s\to x,k,\pi)$ is the probability of going from $s$ to $x$ in $k$ steps under π.
4. Then $\nabla J=\nabla v_\pi(s_0)=\sum_s\big(\sum_{k}\Pr(s_0\to s,k,\pi)\big)\sum_a\nabla\pi(a|s)q_\pi(s,a)=\sum_s\eta(s)\sum_a\nabla\pi(a|s)q_\pi(s,a)$ (η from the box on p. 199 of the book, outside this unit).
5. Multiply and divide by $\sum_{s'}\eta(s')$. Since $\mu(s)=\eta(s)/\sum_{s'}\eta(s')$ (Eq. 9.3), $\nabla J=\big(\sum_{s'}\eta(s')\big)\sum_s\mu(s)\sum_a\nabla\pi(a|s)q_\pi(s,a)\propto\sum_s\mu(s)\sum_a\nabla\pi(a|s)q_\pi(s,a)$.

> **Intuition note.** The theorem's expression differentiates only the action probabilities; no derivative of the state distribution appears, even though performance depends on that distribution.

### 13.3 REINFORCE: Monte Carlo policy gradient (pp. 326–329)
Stochastic gradient ascent needs samples whose expectation is *proportional* to the gradient. The constant is absorbed into α (p. 326). Since states appear under π in proportion to μ:
$$\nabla J(\theta)\propto\mathbb E_\pi\Big[\sum_a q_\pi(S_t,a)\nabla\pi(a|S_t,\theta)\Big]\tag{13.6}$$
Stopping here gives the **all-actions** update, with $\hat q$ a learned approximation of $q_\pi$ (p. 326):
$$\theta_{t+1}\doteq\theta_t+\alpha\sum_a\hat q(S_t,a,w)\nabla\pi(a|S_t,\theta)\tag{13.7}$$
REINFORCE instead uses only the action actually taken. Multiply and divide each term by $\pi(a|S_t,\theta)$ to get an expectation under π (p. 327):
$$\nabla J\propto\mathbb E_\pi\Big[\sum_a\pi(a|S_t,\theta)q_\pi(S_t,a)\frac{\nabla\pi(a|S_t,\theta)}{\pi(a|S_t,\theta)}\Big]=\mathbb E_\pi\Big[q_\pi(S_t,A_t)\frac{\nabla\pi(A_t|S_t,\theta)}{\pi(A_t|S_t,\theta)}\Big]=\mathbb E_\pi\Big[G_t\frac{\nabla\pi(A_t|S_t,\theta)}{\pi(A_t|S_t,\theta)}\Big]$$
The second step replaces $a$ by the sample $A_t\sim\pi$. The third uses $\mathbb E_\pi[G_t|S_t,A_t]=q_\pi(S_t,A_t)$ (p. 327). The REINFORCE update is:
$$\theta_{t+1}\doteq\theta_t+\alpha G_t\frac{\nabla\pi(A_t|S_t,\theta_t)}{\pi(A_t|S_t,\theta_t)}\tag{13.8}$$
- **Reading the update.** The vector is the direction in parameter space that most increases the probability of repeating $A_t$ in $S_t$. The step is proportional to the return, so parameters move most toward high-return actions. It is inversely proportional to the action probability, so frequently chosen actions do not win merely by being chosen often (p. 327).
- **Monte Carlo.** REINFORCE uses the full return to the episode's end. It is defined only for episodic tasks, with updates made after the episode (p. 327).
- **Pseudocode** (p. 328) uses $\nabla\ln\pi=\nabla\pi/\pi$ (from $\nabla\ln x=\nabla x/x$), called the *eligibility vector*. It is the only place the policy parameterization appears in the algorithm. The box computes $G\leftarrow\sum_{k=t+1}^T\gamma^{k-t-1}R_k$ and $\theta\leftarrow\theta+\alpha\gamma^tG\nabla\ln\pi(A_t|S_t,\theta)$. The factor $\gamma^t$ appears because the boxes treat the discounted case, while the text uses γ = 1 (p. 328).
- **Figure 13.1** (short corridor, 100 runs): with step sizes $2^{-12}$, $2^{-13}$, $2^{-14}$, the $2^{-13}$ run comes closest to the optimal start-state value and $2^{-12}$ plateaus near −40 (p. 328).
- **Properties.** The expected update over an episode is in the direction of the performance gradient. This assures expected improvement for sufficiently small α, and convergence to a local optimum under standard stochastic-approximation conditions with decreasing α. As a Monte Carlo method it may have high variance and learn slowly (p. 329).
- **Exercise 13.3** asks to prove, for soft-max with linear preferences, $\nabla\ln\pi(a|s,\theta)=x(s,a)-\sum_b\pi(b|s,\theta)x(s,b)$ (13.9) (p. 329).

### 13.4 REINFORCE with baseline (pp. 329–331)
The theorem generalizes to a baseline $b(s)$ that may be any function or random variable, as long as it does not vary with $a$:
$$\nabla J(\theta)\propto\sum_s\mu(s)\sum_a\big(q_\pi(s,a)-b(s)\big)\nabla\pi(a|s,\theta)\tag{13.10}$$
It stays valid because the subtracted term is zero: $\sum_a b(s)\nabla\pi(a|s,\theta)=b(s)\nabla\sum_a\pi(a|s,\theta)=b(s)\nabla1=0$ (p. 329). The resulting update is
$$\theta_{t+1}\doteq\theta_t+\alpha\big(G_t-b(S_t)\big)\frac{\nabla\pi(A_t|S_t,\theta_t)}{\pi(A_t|S_t,\theta_t)}\tag{13.11}$$
With $b\equiv0$ this is plain REINFORCE. In general the baseline leaves the expected update unchanged but can strongly change its variance. For MDPs the baseline should depend on state: in some states all actions have high values and need a high baseline, in others a low one (p. 329).

A natural choice is $b(S_t)=\hat v(S_t,w)$; since REINFORCE is Monte Carlo, it seems natural to learn $w$ by a Monte Carlo method too (pp. 329–330). **Pseudocode** (p. 330), per step: $G\leftarrow\sum_{k=t+1}^T\gamma^{k-t-1}R_k$; $\delta\leftarrow G-\hat v(S_t,w)$; $w\leftarrow w+\alpha^w\delta\nabla\hat v(S_t,w)$; $\theta\leftarrow\theta+\alpha^\theta\gamma^t\delta\nabla\ln\pi(A_t|S_t,\theta)$. Step size for values: in the linear case a rule of thumb is $\alpha^w=0.1/\mathbb E[\|\nabla\hat v(S_t,w)\|_\mu^2]$. The policy step size $\alpha^\theta$ is much less clear, since it depends on the reward range and the parameterization (p. 330). **Figure 13.2:** on the short corridor, with $\hat v(s,w)=w$, a baseline with $\alpha^\theta=2^{-9},\alpha^w=2^{-6}$ learns much faster than plain REINFORCE at $2^{-13}$ (pp. 330–331).

> **Intuition note.** Subtracting a state-dependent number from the return does not change the average push on the parameters, because the extra term averages to zero. A well-chosen baseline can remove the "all returns are large" part of the signal, which can reduce variance.

### 13.5 Actor–critic methods (pp. 331–332)
In REINFORCE with baseline, $\hat v$ is evaluated at the *first* state of a transition, before the action. It therefore cannot assess that action. In actor–critic methods $\hat v$ is also applied to the second state, giving the one-step return $G_{t:t+1}$, which assesses the action. Like TD methods generally, the one-step return often has lower variance and is computationally convenient, but it introduces bias. Bias can be tuned with n-step returns and eligibility traces. The bias is *not* due to bootstrapping as such: the actor would be biased even with a Monte Carlo critic (p. 331). One-step actor–critic:
$$\theta_{t+1}\doteq\theta_t+\alpha\big(G_{t:t+1}-\hat v(S_t,w)\big)\frac{\nabla\pi(A_t|S_t,\theta_t)}{\pi(A_t|S_t,\theta_t)}\tag{13.12}$$
$$=\theta_t+\alpha\big(R_{t+1}+\gamma\hat v(S_{t+1},w)-\hat v(S_t,w)\big)\frac{\nabla\pi(A_t|S_t,\theta_t)}{\pi(A_t|S_t,\theta_t)}\tag{13.13}$$
$$=\theta_t+\alpha\,\delta_t\frac{\nabla\pi(A_t|S_t,\theta_t)}{\pi(A_t|S_t,\theta_t)}\tag{13.14}$$
It is fully online and incremental, paired with semi-gradient TD(0) for the critic (p. 331). **Pseudocode** (p. 332): set $I\leftarrow1$; each step sample $A\sim\pi$, observe $S',R$; $\delta\leftarrow R+\gamma\hat v(S',w)-\hat v(S,w)$ (with $\hat v=0$ at terminal $S'$); $w\leftarrow w+\alpha^w\delta\nabla\hat v(S,w)$; $\theta\leftarrow\theta+\alpha^\theta I\delta\nabla\ln\pi(A|S,\theta)$; $I\leftarrow\gamma I$; $S\leftarrow S'$.

The n-step and λ-return versions replace $G_{t:t+1}$ by $G_{t:t+n}$ or $G_t^\lambda$. The backward view uses separate traces for actor and critic (p. 332):
$z^w\leftarrow\gamma\lambda^wz^w+\nabla\hat v(S,w)$, $z^\theta\leftarrow\gamma\lambda^\theta z^\theta+I\nabla\ln\pi(A|S,\theta)$, $w\leftarrow w+\alpha^w\delta z^w$, $\theta\leftarrow\theta+\alpha^\theta\delta z^\theta$ (p. 332).

### 13.6 Policy gradient for continuing problems (pp. 333–335)
Performance is the average reward per step:
$$J(\theta)\doteq r(\pi)\doteq\lim_{h\to\infty}\frac1h\sum_{t=1}^h\mathbb E[R_t|S_0,A_{0:t-1}\sim\pi]=\lim_{t\to\infty}\mathbb E[R_t|S_0,A_{0:t-1}\sim\pi]=\sum_s\mu(s)\sum_a\pi(a|s)\sum_{s',r}p(s',r|s,a)r\tag{13.15}$$
μ is the steady-state distribution, $\mu(s)\doteq\lim_{t\to\infty}\Pr\{S_t=s|A_{0:t}\sim\pi\}$. It is assumed to exist and not depend on $S_0$ (ergodicity), and it satisfies
$$\sum_s\mu(s)\sum_a\pi(a|s,\theta)p(s'|s,a)=\mu(s')\quad\forall s'\tag{13.16}$$
Values use the differential return:
$$G_t\doteq R_{t+1}-r(\pi)+R_{t+2}-r(\pi)+R_{t+3}-r(\pi)+\cdots\tag{13.17}$$
With these definitions, (13.5) remains true in the continuing case, and the forward- and backward-view equations stay the same (p. 334). **Continuing actor–critic pseudocode** (p. 333): $\delta\leftarrow R-\bar R+\hat v(S',w)-\hat v(S,w)$; $\bar R\leftarrow\bar R+\alpha^{\bar R}\delta$; traces $z^w\leftarrow\lambda^wz^w+\nabla\hat v$, $z^\theta\leftarrow\lambda^\theta z^\theta+\nabla\ln\pi$; then $w\leftarrow w+\alpha^w\delta z^w$, $\theta\leftarrow\theta+\alpha^\theta\delta z^\theta$.

**Proof (continuing, pp. 334–335).** Here $J=r(\pi)$, and $v_\pi,q_\pi$ use the differential return.
1. As before, $\nabla v_\pi(s)=\sum_a[\nabla\pi\,q_\pi+\pi\nabla q_\pi]$, and now $q_\pi=\sum_{s',r}p(s',r|s,a)(r-r(\theta)+v_\pi(s'))$. So $\nabla v_\pi(s)=\sum_a[\nabla\pi(a|s)q_\pi(s,a)+\pi(a|s)(-\nabla r(\theta)+\sum_{s'}p(s'|s,a)\nabla v_\pi(s'))]$.
2. Rearranging: $\nabla r(\theta)=\sum_a[\nabla\pi(a|s)q_\pi(s,a)+\pi(a|s)\sum_{s'}p(s'|s,a)\nabla v_\pi(s')]-\nabla v_\pi(s)$.
3. The left side is $\nabla J(\theta)$ and does not depend on $s$. So the right side can be weighted by $\mu(s)$ and summed over $s$, since $\sum_s\mu(s)=1$.
4. This gives $\nabla J=\sum_s\mu(s)\sum_a\nabla\pi\,q_\pi+\sum_{s'}\big[\sum_s\mu(s)\sum_a\pi(a|s)p(s'|s,a)\big]\nabla v_\pi(s')-\sum_s\mu(s)\nabla v_\pi(s)$.
5. By (13.16) the bracket is $\mu(s')$. The last two terms cancel, leaving $\nabla J=\sum_s\mu(s)\sum_a\nabla\pi(a|s)q_\pi(s,a)$.

> **Intuition note.** In the continuing case, under the ergodicity assumption, the steady-state distribution does not depend on the starting state, and $\nabla J$ does not depend on $s$. This lets the state-by-state equation be averaged under the stationary distribution, where by (13.16) the value-gradient terms cancel exactly.

### 13.7 Policy parameterization for continuous actions (pp. 335–336)
Instead of probabilities for each of infinitely many actions, learn statistics of a distribution. Normal density: $p(x)\doteq\frac1{\sigma\sqrt{2\pi}}\exp\!\big(-\frac{(x-\mu)^2}{2\sigma^2}\big)$ (13.18). It is a *density*, which can exceed 1. Probabilities come from the area under it (integrating over a range) (p. 335). Gaussian policy with state-dependent mean and standard deviation:
$$\pi(a|s,\theta)\doteq\frac1{\sigma(s,\theta)\sqrt{2\pi}}\exp\!\Big(-\frac{(a-\mu(s,\theta))^2}{2\sigma(s,\theta)^2}\Big)\tag{13.19}$$
with $\mu:\mathcal S\times\mathbb R^{d'}\to\mathbb R$ and $\sigma:\mathcal S\times\mathbb R^{d'}\to\mathbb R^+$. Split $\theta=[\theta_\mu,\theta_\sigma]^\top$. The mean is linear, and σ must be positive, so it is better as an exponential of a linear function:
$$\mu(s,\theta)\doteq\theta_\mu^\top x_\mu(s),\qquad\sigma(s,\theta)\doteq\exp\big(\theta_\sigma^\top x_\sigma(s)\big)\tag{13.20}$$
All the chapter's algorithms can then be applied to real-valued actions (p. 336). Exercises 13.4 and 13.5 follow (p. 336).

### 13.8 Summary (p. 337)
Policy-parameter methods can learn specific action probabilities, learn the right amount of exploration, approach determinism and handle continuous actions. These are easy for them, but awkward or impossible for ε-greedy and action-value methods. The theorem gives an exact formula without state-distribution derivatives. A baseline reduces REINFORCE's variance without bias. A critic introduces bias into the actor's gradient estimates but is often desirable, for the same reason that bootstrapping TD methods are often superior to Monte Carlo (substantially reduced variance). The authors say policy-gradient methods are less well understood in some respects and a subject of ongoing research (p. 337).

**Bibliographical notes (p. 338).** The presentation is based mainly on Sutton, McAllester, Singh and Mansour (2000). The theorem was first obtained by Marbach and Tsitsiklis and independently by Sutton et al. REINFORCE is due to Williams. Thomas (2014) first realized the $\gamma^t$ factor was needed for discounted episodic problems (p. 338).

## Toy example (ours, not from the text)
One state, two actions, preferences $h(a)=\theta_a$, $\theta=(\theta_1,\theta_2)=(0,0)$, one-step episode, γ = 1, α = 0.1.
- $\pi(1)=e^0/(e^0+e^0)=0.5$, $\pi(2)=0.5$.
- Suppose the sampled action is $A=1$ with return $G=2$.
- Eligibility vector, by direct differentiation of $\ln\pi(1)=\theta_1-\ln(e^{\theta_1}+e^{\theta_2})$: $\partial/\partial\theta_1=1-\pi(1)=0.5$ and $\partial/\partial\theta_2=-\pi(2)=-0.5$. So $\nabla\ln\pi(1)=(0.5,-0.5)$. As a check, $\nabla\pi(1)/\pi(1)=(0.25,-0.25)/0.5=(0.5,-0.5)$.
- Update (13.8): $\theta=(0,0)+0.1\cdot2\cdot(0.5,-0.5)=(0.1,-0.1)$.
- New $\pi(1)=e^{0.1}/(e^{0.1}+e^{-0.1})=1.10517/(1.10517+0.90484)=1.10517/2.01001\approx0.550$. Action 1 became more likely.
- **Baseline.** With $b=1.5$, $G-b=0.5$, so the step is $0.1\cdot0.5\cdot(0.5,-0.5)=(0.025,-0.025)$, smaller than before.
- **Why the expected update is unchanged.** $\nabla\ln\pi(2)=(-0.5,0.5)$, so $\sum_a\pi(a)\nabla\ln\pi(a)=0.5(0.5,-0.5)+0.5(-0.5,0.5)=(0,0)$. The baseline term averages to zero, as in the proof on p. 329.

## Concepts
- [[policy]] — here a differentiable parameterized rule $\pi(a|s,\theta)$ that selects actions without value estimates (p. 321)
- [[policy-gradient-theorem]] (new) — $\nabla J\propto\sum_s\mu(s)\sum_aq_\pi(s,a)\nabla\pi(a|s,\theta)$, with no derivative of the state distribution (p. 326)
- [[reinforce]] (new) — Monte Carlo policy gradient with update $\alpha G_t\nabla\pi/\pi$ (p. 327)
- [[eligibility-vector]] (new) — $\nabla\ln\pi(A_t|S_t,\theta)$, the only place the parameterization enters the algorithm (p. 328)
- [[baseline]] (new) — an $a$-independent $b(s)$ subtracted from the return: same expected update, different variance (p. 329)
- [[actor-critic]] (new) — policy (actor) plus a value function that assesses actions via a one-step return (critic); adds bias, often cuts variance (p. 331)
- [[softmax-action-preferences]] (new) — $\pi\propto e^{h(s,a,\theta)}$; can approach determinism or any stochastic policy (p. 322)
- [[gaussian-policy]] (new) — a normal density over real actions with state-dependent mean and standard deviation (p. 335)
- [[differential-return]] (new) — returns measured relative to average reward $r(\pi)$ in the continuing case (p. 334)
- [[exploration vs exploitation]] — policies kept in (0,1) to ensure exploration; preferences can learn their own exploration level (pp. 322, 337)
- [[temporal-difference learning / reward prediction error]] — δ is the quantity $R+\gamma\hat v(S',w)-\hat v(S,w)$ from the pseudocode (p. 332), used by the critic (paired with semi-gradient TD(0)) (p. 331)

## Canonical instances
- [[short-corridor-switched-actions]] (new) — a problem where the best policy is stochastic (right with p ≈ 0.59, value ≈ −11.6) (p. 323)
- [[poker-bluffing]] (new) — optimal play may mix actions with specific probabilities (p. 323)
- [[gradient-bandit-algorithm]] (new) — the one earlier method that learned a policy parameter directly (p. 321, footnote)

## Bridges (candidates)
- [structural-analogy] parameterized policy $\pi_\theta$ updated by gradient ascent on $J$ ↔ control theory: state feedback $u=-Kx$ with gain tuned to optimize a cost — both tune a feedback law's parameters.
- [structural-analogy] actor + critic ↔ control theory: controller plus an estimator that evaluates performance — both separate acting from assessing.
- [metaphor] baseline subtraction ↔ statistics: variance reduction by subtracting something with zero mean effect.

## Questions this raises
- How does the policy gradient theorem change when future rewards are discounted (Exercise 13.2 asks for this)?
- How should the policy step size $\alpha^\theta$ be chosen when it depends on the reward scale and parameterization (p. 330)?
- Is there a baseline better than $\hat v(s,w)$, or one that depends on the action (p. 338 mentions work on both)?
- When is the critic's bias worth its variance reduction, and how does the choice of λ trade the two?

## Exercises worth doing
- Ex. 13.1 (p. 324) — derive the optimal right-probability in the switched-corridor example; makes stochastic optimality concrete — difficulty: medium
- Ex. 13.2 (p. 328, starred) — generalize the box, theorem, proof and REINFORCE derivation so the factor $\gamma^t$ appears — difficulty: hard
- Ex. 13.3 (p. 329) — prove the eligibility vector for linear soft-max preferences, (13.9) — difficulty: medium
- Ex. 13.4 (p. 336) — derive the Gaussian-policy eligibility vectors for $\theta_\mu$ and $\theta_\sigma$ — difficulty: medium
- Ex. 13.5 (p. 336) — Bernoulli-logistic unit: logistic policy, REINFORCE update, eligibility vector — difficulty: medium

## Reading notes
- Printed page = pdf page − 22 (pdf 343 = p. 321).
- The text layer drops minus signs and Greek symbols in places. I checked equations against the page images, including (13.15), (13.19) and (13.20), and the proofs on pp. 325 and 334–335.
- The text on p. 327 prints "Willams, 1992", and the image shows the same spelling.
- Example 13.1: the values are −44, −82 and −11.6 (minus signs confirmed in the image, p. 323).
- Equation (13.14) uses $\delta_t$ without defining it in the surrounding text. It is identified with the bracket in (13.13), as in the pseudocode (p. 332).
