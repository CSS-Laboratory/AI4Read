---
id: bertsekas-2026-rlcourse/ch03-learning-p2
work: bertsekas-2026-rlcourse
unit: "3 Learning Values and Policies (part 2/5): end of 3.1.3, 3.2 Neural Networks, 3.3 Learning Cost Functions in Approximate DP (to the middle of 3.3.7)"
pages: 372–398
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Neural networks as value approximators, and fitted value iteration, Q-factor methods, approximate policy iteration and advantage updating

## L0 — One line
Cost-to-go functions, Q-factors and cost differences can be approximated by least-squares fits of a (neural network) architecture to Bellman-equation targets, solved stage by stage or policy by policy.

## L1 — The gist (≤ 120 words)
How can we approximate the optimal cost-to-go or Q-factors when the state space is too large for exact DP? The unit first describes multilayer perceptrons and their training by incremental gradient methods. It then uses them in fitted value iteration, in Q-factor fitting that can be model-free, in approximate policy iteration, in optimistic variants (SARSA, DQN), and in a POMDP rollout scheme. Finally it argues that approximating differences (advantages, cost differences) can be better than approximating values, because large state-dependent terms may swamp the small terms that matter for choosing a control. The text warns repeatedly about exploration, oscillation, and on-line use.

**Prerequisites:** finite-horizon DP and the Bellman equation; Q-factors; least squares and the normal equations; gradient descent; policy iteration; basic probability. Terms glossed here: POMDP = decision problem where the state is only partly observed; rollout = improving a base policy by simulating it; SARSA and DQN = optimistic Q-factor methods (see L3); advantage = a Q-factor minus its minimum over controls.

## L2 — Key ideas (5–10 bullets)
- A single-layer perceptron is a linear layer, a scalar nonlinear unit applied to each output, and a linear weighting; its output is $\tilde J=\sum_\ell r_\ell\,\sigma((Ay(x)+b)_\ell)$ (p. 375).
- Universal approximation says one nonlinear layer is enough in principle. It does not say how many units are needed, so $m$ is found by trial and error (pp. 376–377).
- Training is a nonconvex least-squares problem with a very large number of terms, so incremental gradient methods are used. In network training, regularization is described as primarily important for avoiding overfitting (p. 377).
- Fitted value iteration fits $\tilde J_k$ backward in $k$ to targets $\beta_k^s$ computed from $\tilde J_{k+1}$. Fitting Q-factors reverses the order of min and expectation and allows model-free sampling (pp. 380–384).
- Approximate PI replaces exact evaluation by a least-squares fit. Its stated difficulties are poor exploration, oscillation (policies repeating in cycles; the text calls a related phenomenon chattering) and architecture choice (pp. 385–388).
- The extreme optimistic scheme that uses a single sample between policy updates is often called SARSA. DQN is based on experience replay (storing samples in a buffer for reuse). Both are fundamentally off-line, and on-line use has further difficulties (pp. 388–390).
- Approximating advantages (Q-factor minus its minimum over controls) can remove large state-dependent terms that may otherwise dominate the fit (pp. 395–396). Approximating cost differences is motivated by the error magnification inherent in Q-factor differencing (p. 398).

## L3 — Walkthrough

### End of 3.1.3: scaling incremental methods (p. 372)
- Incremental versions of diagonal scaling were suggested in the neural network literature, with Duchi–Hazan–Singer [DHS11] and Kingma–Ba [KiB14] named as influential (p. 372).
- ADAM adapts the stepsize of each component of $r$ using estimates of the first and second moments of the gradient (p. 372).
- Another way to move toward the Newton direction writes Newton's method in a form suited to additive costs, with low-order matrix inversion. Zeroing the off-diagonal terms of the inverted matrices gives diagonal scaling with no inversion. A Gauss–Newton/extended Kalman filter method is also cited (p. 372).

### 3.2 Neural networks (pp. 372–379)
**Setting.** Networks are used to approximate the optimal cost-to-go $J_k^*$. One builds an approximation of $J^*_{N-1}$, then uses it for $J^*_{N-2}$, and so on backward (p. 372). The focus is the multilayer perceptron (p. 372). The stage index $k$ is dropped.

**Architecture (3.11).** The class has two parameter vectors:
$$\tilde J(x,v,r)=r'\phi(x,v). \tag{3.11}$$
Given pairs $(x^s,\beta^s)$, $s=1,\dots,q$, choose $(v,r)$ to minimize $\sum_{s=1}^q(\tilde J(x^s,v,r)-\beta^s)^2$ (p. 373). $v$ parametrizes $\phi(x,v)$, which can be read as a feature vector. $r$ weights the components of $\phi$ linearly (p. 373).

**Single layer perceptron (pp. 373–375).**
- The state is encoded as $y(x)\in\Re^n$. The linear layer computes $Ay(x)+b$, with $A$ of shape $m\times n$ and $b\in\Re^m$. Set $v=(A,b)$ (p. 373).
- Each component $(Ay(x)+b)_\ell$ goes through a differentiable, monotonically increasing scalar function $\sigma$ (p. 374).
- ReLU is $\max\{0,\xi\}$, smoothed, e.g. $\sigma(\xi)=\ln(1+e^\xi)$, with $\sigma'(\xi)=e^\xi/(1+e^\xi)$, tending to 0 and 1 as $\xi\to-\infty,\infty$ (pp. 374–375).
- Sigmoids satisfy $-\infty<\lim_{\xi\to-\infty}\sigma<\lim_{\xi\to\infty}\sigma<\infty$. Examples: $\tanh(\xi)=\frac{e^\xi-e^{-\xi}}{e^\xi+e^{-\xi}}$ and the logistic $\frac1{1+e^{-\xi}}$ (p. 374).
- Features and output ($\phi\in\Re^m$, $r\in\Re^m$):
$$\phi_\ell(x,v)=\sigma\big((Ay(x)+b)_\ell\big),\qquad \tilde J(x,v,r)=\sum_{\ell=1}^m r_\ell\,\sigma\big((Ay(x)+b)_\ell\big).$$
- Each $\phi_\ell$ depends only on row $\ell$ of $A$ and component $\ell$ of $b$. This can motivate constraints on individual entries for "handcrafted" effects (p. 375).

**Intuition note.** The network first builds $m$ features by bending $m$ linear combinations of the encoded state. Then it adds the features up with weights $r$. Only $r$ enters linearly; $v=(A,b)$ enters through $\sigma$, so the fit is a nonlinear regression problem (p. 373, footnote).

**State encoding (p. 376).** Encodings may be state components, numerical versions of qualitative traits, or features meant to capture "important nonlinearities" of the cost-to-go. Feature extraction followed by a network is shown in Fig. 3.2.4. With good features the network need not be complicated and may train more easily. The author says this is supported by examples and experience but is hard to support quantitatively (p. 376).

**Universal approximation (pp. 376–377).** Roughly: if $x$ lies in a Euclidean space $X$ and $y(x)\equiv x$, a network of this form can approximate arbitrarily closely, over a compact $S\subset X$, any piecewise continuous $J:S\to\Re$, provided $m$ is large enough (p. 376). The theorem does not say how many units give "good" performance. In practice one tries larger $m$ until satisfied. Bayesian optimization has been used to tune AlphaZero's deep network (p. 377). The needed $m$ and the parameter dimension can be very large. This motivates concatenating perceptrons into deep networks (p. 377).

**Intuition note.** "Enough units exist" is a statement about existence. It gives no estimate of how many units are needed (p. 377).

#### 3.2.1 Training (pp. 377–378)
$$\min_{A,b,r}\ \sum_{s=1}^q\Big(\sum_{\ell=1}^m r_\ell\,\sigma\big((Ay(x^s)+b)_\ell\big)-\beta^s\Big)^2. \tag{3.12}$$
- The cost is generally nonconvex, so there may be several local minima (p. 377).
- A regularization term (e.g. quadratic in $A,b,r$) is customary. In network training it is primarily important to avoid overfitting, meaning a good fit to training data but worse on new data. This arises when the number of parameters is comparable to the training-set size (p. 377).
- The cost is a sum of a potentially very large number $q$ of terms. Hence incremental methods of Sec. 3.1.3 are "universally used", and can be vastly superior to non-incremental ones (p. 378). The order of component selection is arbitrary but is usually randomized each cycle. A minibatch (several components per iteration) averages and permits a larger stepsize (footnote, p. 378).
- Training is ordinarily done off-line, possibly in parallel. It need not be very accurate. This is supported by the Newton-step view of approximation in value space: great accuracy of the off-line terminal-cost approximation is not critical for the on-line play algorithm (p. 378).

#### 3.2.2 Multilayer and deep networks (pp. 378–379)
- Outputs of each nonlinear layer feed the next linear layer (Fig. 3.2.5). Early practice used one to three nonlinear layers. Tesauro's backgammon program and its descendants did well with one or two. Recent successes (images, speech, language models, approximate DP) use many layers (p. 378).
- Why more layers, if one suffices for universal approximation? The author gives "qualitative (and somewhat speculative)" reasons (p. 379):
  - (a) Linear layers with sparsity or convolution structure may match the problem and cut the parameter count.
  - (b) The outputs of each nonlinear layer form a hierarchy of features.
  - (c) Overparametrization (more weights than data) helps mitigate overfitting and the need for regularization. The explanation is the subject of much recent research.
- Deep networks were an important factor in AlphaGo, AlphaZero and large language models (p. 379).

### 3.3 Learning cost functions in approximate DP (pp. 380–398)
Architectures approximate cost functions (value network) or policies (policy network) (p. 380).

#### 3.3.1 Fitted value iteration (pp. 380–382)
Parameters $r_k$ are found backward in $k$: first $r_{N-1}$, then $r_{N-2}$, and so on. At each stage, $q$ states $x_k^s$ are sampled (p. 380). With $r_{k+1}$ known, the targets are
$$\beta_k^s=\min_{u\in U_k(x_k^s)}E\Big\{g_k(x_k^s,u,w_k)+\tilde J_{k+1}\big(f_k(x_k^s,u,w_k),r_{k+1}\big)\Big\}, \tag{3.13}$$
$$r_k\in\arg\min_r\sum_{s=1}^q\big(\tilde J_k(x_k^s,r)-\beta_k^s\big)^2. \tag{3.14}$$
At stage $N-1$ the target is $\min_u E\{g_{N-1}(x^s_{N-1},u,w_{N-1})+g_N(f_{N-1}(x^s_{N-1},u,w_{N-1}))\}$. The algorithm ends with $r_0$ (p. 381).
- For a linear architecture $\tilde J_k=r_k'\phi_k(x_k)$, the fit has the closed form (cf. Eq. (3.7))
$$r_k=\Big(\sum_{s=1}^q\phi_k(x_k^s)\phi_k(x_k^s)'\Big)^{-1}\sum_{s=1}^q\beta_k^s\phi_k(x_k^s).$$
For a nonlinear architecture, incremental gradient algorithms may be used (p. 381).
- Sample states usually come from Monte Carlo simulation. They should be "representative", with frequencies roughly proportional to their probabilities under an optimal policy (p. 381).
- With a very long horizon the total number of parameters may be excessive. If the problem is stationary it may be treated as infinite-horizon (p. 382).
- Difficulty: each $\beta_k^s$ needs a minimization of an expected value, which can be very time consuming. Q-factors reverse the order of min and expectation (p. 382).

**Intuition note.** Each stage is a regression problem whose "labels" are one Bellman backup of the already-fitted next stage. Errors in $\tilde J_{k+1}$ pass into the labels for stage $k$.

#### 3.3.2 Q-factor approximation, model-free (pp. 382–384)
Optimal Q-factors, using $J^*_k(x_k)=\min_u Q^*_k(x_k,u)$ (p. 382):
$$Q_k^*(x_k,u_k)=E\{g_k(x_k,u_k,w_k)+J^*_{k+1}(f_k(x_k,u_k,w_k))\}, \tag{3.15}$$
$$Q_k^*(x_k,u_k)=E\Big\{g_k(x_k,u_k,w_k)+\min_{u\in U_{k+1}(f_k(x_k,u_k,w_k))}Q^*_{k+1}\big(f_k(x_k,u_k,w_k),u\big)\Big\}. \tag{3.16}$$
Architectures (p. 383):
- (3.17): $\tilde Q_k=r_k(u_k)'\phi_k(x_k)$, a separate weight vector per control. It is suitable when there are few controls.
- (3.18): $\tilde Q_k=r_k'\phi_k(x_k,u_k)$. The author focuses on this one.

For (3.18), with sample pairs $(x_k^s,u_k^s)$:
$$r_k\in\arg\min_r\sum_{s=1}^q\big(r'\phi_k(x_k^s,u_k^s)-\beta_k^s\big)^2, \tag{3.19}$$
$$\beta_k^s=E\Big\{g_k(x_k^s,u_k^s,w_k)+\min_{u\in U_{k+1}(f_k(x_k^s,u_k^s,w_k))}r_{k+1}'\phi_{k+1}\big(f_k(x_k^s,u_k^s,w_k),u\big)\Big\}. \tag{3.20}$$
The closed form is $r_k=\big(\sum_s\phi_k(x_k^s,u_k^s)\phi_k(x_k^s,u_k^s)'\big)^{-1}\sum_s\beta^s_k\phi_k(x_k^s,u_k^s)$ (p. 383). On-line control is then
$$\tilde\mu_k(x_k)\in\arg\min_{u\in U_k(x_k)}\tilde Q_k(x_k,u,r_k), \tag{3.21}$$
which needs no expected value. This is a primary incentive for Q-factors when on-line computation is tight (pp. 383–384).
- $\beta_k^s$ may be replaced by an average of a few samples, even one, of the random variable
$$g_k(x_k^s,u_k^s,w_k)+\min_{u}r_{k+1}'\phi_{k+1}\big(f_k(x_k^s,u_k^s,w_k),u\big). \tag{3.22}$$
Only a simulator is needed that, for any $(x_k,u_k)$, produces the next-stage cost and state according to the distribution of $w_k$. This gives the model-free implementation (p. 384).
- Samples of (3.22) need no expectation and involve a simpler minimization than (3.13) (p. 384).
- The resulting policy may itself be approximated by a parametric architecture: approximation in policy space on top of approximation in value space (p. 384).

#### 3.3.3 Approximate policy iteration, infinite horizon (pp. 384–388)
Setting: finite-state $\alpha$-discounted problem with states $i,j$, transition probabilities $p_{ij}(u)$ and cost $g(i,u,j)$ (p. 384). Exact PI converges in finitely many iterations because of cost improvement and finite state and control spaces (p. 385).
- **(a) Policy evaluation:** $Q_\mu(i,u)=\sum_{j=1}^n p_{ij}(u)\big(g(i,u,j)+\alpha J_\mu(j)\big)$.
- **(b) Policy improvement:** $\tilde\mu(i)\in\arg\min_{u\in U(i)}Q_\mu(i,u)$ (p. 385).

*Approximate version.* Simulate training triplets $(i^s,u^s,\beta^s)$ and fit (p. 385):
$$\bar r\in\arg\min_r\sum_{s=1}^q\big(\tilde Q_\mu(i^s,u^s,r)-\beta^s\big)^2, \tag{3.23}$$
$$\tilde\mu(i)\in\arg\min_{u\in U(i)}\tilde Q_\mu(i,u,\bar r). \tag{3.24}$$
- $\beta^s$ is a sample of $Q^k_\mu(i^s,u^s)$, the $k$-stage Q-factor: start at $i^s$, apply $u^s$, then follow $\mu$ for $k$ stages. As $k\to\infty$ it gives the infinite-horizon Q-factor. If $k$ is small, add a terminal cost approximation to compensate for the gap $|Q_\mu-Q_\mu^k|$, which decreases in proportion to $\alpha^k$ (p. 385).
- Alternative improvement: compute pairs $(i^s,\tilde\mu(i^s))$ by (3.24) and fit them with a policy architecture. This gives PI with approximation in both value and policy space (p. 386).

*On-line play (p. 386).* One may apply $\tilde\mu(i)\in\arg\min_u\tilde Q(i,u,\tilde r)$, the would-be next iterate. Or one may apply the one-step lookahead
$$\tilde\mu(i)\in\arg\min_{u\in U(i)}\Big[\sum_{j=1}^np_{ij}(u)\Big(g(i,u,j)+\alpha\min_{u'\in U(j)}\tilde Q(j,u',\tilde r)\Big)\Big], \tag{3.25}$$
or a multistep version. The latter "implements a Newton step" and will likely perform substantially better, but costs more, especially with model-free simulation. Replacing $\min_{u'}\tilde Q(j,u',\tilde r)$ by an off-line trained approximation also implements a Newton step (p. 386).

*Challenges (pp. 386–388).*
- (a) Architecture: a linear feature-based architecture makes (3.23) a linear least-squares problem with a closed form. It also admits methods with solid guarantees (TD($\lambda$), LSTD($\lambda$), LSPE($\lambda$), not described here). Finding and training a good architecture can be hard (p. 387).
- (b) Exploration: inadequate exploration is called the "Achilles' heel" of approximate PI. Samples starting from states frequently visited by $\mu$ underrepresent states unlikely under $\mu$. Their Q estimates may be very inaccurate, which can give serious errors in (3.24). Remedies: many initial states, short trajectories with a terminal cost approximation, and an off-policy $\mu'$ that visits states unlikely under $\mu$ (p. 387).
- (c) Oscillation: approximate PI guarantees only that policies end up asymptotically within a certain error bound of optimal. Policies may repeat in cycles. Parameters may oscillate too, or converge in parameter space while the policy oscillates; this is called chattering. There is no guarantee the cycling policies are good. Oscillation can be avoided, and convergence shown, under special conditions, in particular with aggregation (pp. 387–388).

#### 3.3.4 Optimistic PI: SARSA and DQN (pp. 388–390)
"Optimistic" methods use few samples between policy updates. The extreme case uses one sample. At iteration $k$ we have $r^k$, state $i^k$ and control $u^k$ (p. 388):
1. Simulate the transition $(i^k,i^{k+1})$ with probabilities $p_{i^kj}(u^k)$.
2. Choose
$$u^{k+1}\in\arg\min_{u\in U(i^{k+1})}\tilde Q(i^{k+1},u,r^k). \tag{3.26}$$
For exploration, $u^{k+1}$ may with small probability be random, or $\epsilon$-greedy (within $\epsilon$ of the minimum). This is commonly called an off-policy.
3. Update
$$r^{k+1}=r^k-\gamma^k\nabla\tilde Q(i^k,u^k,r^k)\Big(\tilde Q(i^k,u^k,r^k)-g(i^k,u^k,i^{k+1})-\alpha\tilde Q(i^{k+1},u^{k+1},r^k)\Big). \tag{3.27}$$
For $\tilde Q=\phi(i,u)'r$ this becomes
$r^{k+1}=r^k-\gamma^k\phi(i^k,u^k)\big(\phi(i^k,u^k)'r^k-g(i^k,u^k,i^{k+1})-\alpha\phi(i^{k+1},u^{k+1})'r^k\big)$.

So $r^k$ moves in an incremental gradient direction, opposite to the gradient of $(\phi(i^k,u^k)'r-g-\alpha\phi(i^{k+1},u^{k+1})'r^k)^2$, evaluated at $r^k$ with the last term held fixed (p. 389).

- These schemes are often referred to as SARSA. They admit model-free implementation. With Q-factor approximation their behavior is very complex, convergence is unclear, and no performance bounds exist in the literature. Often several samples are batched and averaged before an update (p. 389).
- Storing samples in a buffer for randomized reuse is experience replay. DQN (Mnih et al.) is based on it. Experience replay does not depend on a deep network. A DeepMind idea adds asynchronous parallel computation (p. 389).
- These are fundamentally off-line algorithms. The interim Q-factors can be unreliable for on-line decisions, especially when system parameters change. Still, SARSA and DQN are far better suited to on-line use than approximate PI of 3.3.3, because (3.26) also selects controls on-line. It is important that the parameters $r^k$ stay at "safe" levels during on-line control, which can be a challenge (p. 390).
- On-line difficulties (p. 390):
  - (a) occasional off-policy controls are needed for exploration and may be poor or induce instability;
  - (b) in adaptive settings the algorithm may adapt too slowly;
  - (c) minimization (3.26) is not a Newton step, so performance is lost. The alternative $u^{k+1}\in\arg\min_u\sum_jp_{i^{k+1}j}(u)\big(g(i^{k+1},u,j)+\alpha\min_{u'}\tilde Q(j,u',r^k)\big)$ is better but costlier.
- Encouraging results exist in specific contexts, often with "manual tuning" (p. 390).

#### 3.3.5 Approximate PI for infinite-horizon POMDP (pp. 390–395)
- Setting: $n$ states, finite control set $U$, discount $\alpha\in(0,1)$. After reaching state $j$, an observation $z\in Z$ is drawn with known probability $p(z\mid j,u)$ (p. 391). The classical approach uses the belief $b=(b_1,\dots,b_n)$, a sufficient statistic (p. 391).
- **Feature state** $y$: it must subsume $b$ (so $b_y$ is computable from $y$). It is generated by a known feature estimator $F(y,u,z)$, the exact next feature after $u$ and $z$. Since $b$ is sufficient, so is $y$, so optimal costs are the same. Specific suboptimal schemes may work better with $y$ (p. 391).
- Bellman equation (the text gives it as having a unique solution):
$$J^*(y)=\min_{u\in U}\Big[\hat g(y,u)+\alpha\sum_{z\in Z}\hat p(z\mid b_y,u)J^*\big(F(y,u,z)\big)\Big],\quad \hat g(y,u)=\sum_{i=1}^nb_{y,i}\sum_{j=1}^np_{ij}(u)g(i,u,j)$$
with $\hat p(z\mid b_y,u)$ the probability of the next observation $z$ given $b_y$ and $u$ (pp. 391–392). A one-step lookahead replaces $J^*$ by $\tilde J$ in this equation (p. 392).
- **Truncated rollout** (p. 392): $\tilde J(y)$ is obtained by simulating the base policy $\mu$ for $m$ steps, starting from $b_y$ (Fig. 3.3.1), and adding a terminal approximation $\hat J(\bar y)$ at the end. The rollout policy depends on $\mu$, $\hat J$, $m$, and the lookahead size $\ell$. Choices of $m$ and $\ell$ are typically made by trial and error. Using $m$-step rollout between the $\ell$-step lookahead and the terminal cost gives the method the character of a single PI (p. 393).
- **Learning the rollout policy** (p. 393): fit $\hat\mu(y,r)$ by classification to pairs $(y^s,u^s)$, where $u^s$ is the rollout control at $y^s$. Applying this repeatedly (each approximated rollout policy becomes the next base policy) gives PI as "perpetual rollout" (pp. 393–394).
- Two versions (p. 394). (a) With truncation: a policy network plus a value network per iteration. (b) Without truncation: rollout continues until the remaining stages are insignificant due to discounting, or to a termination state. Then only a policy network is needed. Zero terminal cost may work well if $\ell$ or $m$ is relatively large (p. 394).
- Exploration still matters: the sample set should include feature states favored by the rollout trajectories (pp. 394–395). Case study: Bhattacharya et al. [BBW20], pipeline repair (p. 395).

#### 3.3.6 Advantage updating (pp. 395–397)
Define $A_k(x_k,u_k)=Q_k^*(x_k,u_k)-\min_{u\in U_k(x_k)}Q_k^*(x_k,u)$ and select $\tilde\mu_k(x_k)\in\arg\min_uA_k(x_k,u)$ (p. 395).
- Without approximation this selects the same controls as comparing Q-factors. With approximation it can matter, because $A_k$ may have a much smaller range. $Q^*_k$ may contain sizable terms that depend on $x_k$ but not on $u_k$. A training algorithm may capture this large-scale behavior and miss the finer variation that matters (p. 395).

**Example 3.3.1 (from [BeT96]) (p. 396).** System $x_{k+1}=x_k+\delta u_k$, stage cost $g=\delta(x_k^2+u_k^2)$, $\delta$ very small. Base policy $\mu(x)=-2x$. The infinite-horizon Q-factor is
$$Q_\pi(x,u)=\frac{5x^2}{4}+\delta\Big(\frac{9x^2}{4}+u^2+\frac52xu\Big)+O(\delta^2).$$
The calculation is omitted in the source. The part relevant for rollout is $\delta(u^2+\tfrac52xu)$ (3.28). A value network trained on $Q_\pi$ will be dominated by $5x^2/4$, and (3.28) is "lost" for small $\delta$. The advantage is
$$A_\mu(x,u)=\delta\Big(u^2+\tfrac52xu-\min_v\big(v^2+\tfrac52xv\big)\Big)+O(\delta^2)=\delta\Big(u^2+\tfrac52xu+\tfrac{5^2}{4}x^2\Big)+O(\delta^2),$$
essentially unaffected by $\delta$ when approximated (p. 396). (See Reading notes on the last coefficient.)

**Baseline (pp. 396–397).** Advantage updating is related to subtracting a (state-dependent) baseline from a quantity being estimated. The same remedy appears for rollout with small stage costs relative to the cost approximation (Sec. 2.6). Fig. 3.3.2: fit $h(u)$ by $ru$ after subtracting $b$ from the samples, $\bar r\in\arg\min_r\sum_s\big((h(u^s)-b)-ru^s\big)^2$. Adjusting $b$ improves the approximation, which becomes $\tilde h(u,b,r)=b+ru$. Here $b$ acts as an extra weight on the basis function 1 (p. 397).

**Intuition note.** If every Q-value contains the same large number, a regression wastes its effort on that number. Subtracting something that does not depend on the control keeps the control-dependent differences, which are all that the minimization uses.

#### 3.3.7 Differential training of cost differences for rollout (pp. 397–398; the section continues beyond this unit)
- Standard off-line rollout: (1) approximate $\tilde J_k\approx J_{k,\pi}$ of the base policy $\pi$; (2) compute $\tilde Q_k(x_k,u)=E\{g_k(x_k,u,w_k)+\tilde J_{k+1}(f_k(x_k,u,w_k))\}$ and pick $\tilde\mu_k\in\arg\min_u\tilde Q_k$ (pp. 397–398). This suffers from error magnification inherent in Q-factor differencing (p. 398).
- To compute the rollout control it is sufficient to have the cost-to-go differences:
$$\tilde J_{k+1}\big(f_k(x_k,u,w_k)\big)-\tilde J_{k+1}\big(f_k(x_k,\mu_k(x_k),w_k)\big), \tag{3.29}$$
where $\mu_k$ is the base policy. Approximate $G_{k+1}(x_{k+1},\hat x_{k+1})$, the difference between costs at two states, by $\tilde G_{k+1}$. Then
$$\tilde\mu_k(x_k)\in\arg\min_{u}E\Big\{g_k(x_k,u,w_k)-g_k(x_k,\mu_k(x_k),w_k)+\tilde G_{k+1}\big(f_k(x_k,u,w_k),f_k(x_k,\mu_k(x_k),w_k)\big)\Big\}. \tag{3.30}$$
The minimization (3.30) aims to simply subtract the approximate Q-factor of the base control from that of every other control (p. 398).
- Training $\tilde G_{k+1}$ uses a "differential" system whose states are pairs $(x_k,\hat x_k)$. With $G_k(x_k,\hat x_k)=J_{k,\pi}(x_k)-J_{k,\pi}(\hat x_k)$, subtract the DP equations of $\pi$ at $x_k$ and $\hat x_k$:
$$G_k(x_k,\hat x_k)=E\Big\{g_k\big(x_k,\mu_k(x_k),w_k\big)-g_k\big(\hat x_k,\mu_k(\hat x_k),w_k\big)+G_{k+1}\big(f_k(x_k,\mu_k(x_k),w_k),f_k(\hat x_k,\mu_k(\hat x_k),w_k)\big)\Big\}.$$
The page ends here; the continuation is outside this unit (p. 398).

## Toy example (ours, not from the text)
Fitted value iteration with a linear architecture. Two stages, $N=2$. Dynamics $x_{k+1}=x_k+u_k$, $u\in\{-1,0,1\}$, stage cost $g_k=u^2$, terminal cost $g_2(x)=x^2$. Deterministic, so $E$ is trivial. Features: $\phi(x)=x$ (one weight). Sample states: $x^s\in\{1,2,3\}$.

**Stage 1** (targets (3.13)): $\beta^s=\min_u[u^2+(x+u)^2]$.
- $x=1$: $u=-1$ gives $1+0=1$; $u=0$ gives $1$. So $\beta=1$.
- $x=2$: $u=-1$ gives $1+1=2$; $u=0$ gives 4. So $\beta=2$.
- $x=3$: $u=-1$ gives $1+4=5$; $u=0$ gives 9. So $\beta=5$.

Closed form: $r_1=\dfrac{\sum\beta^s x^s}{\sum (x^s)^2}=\dfrac{1\cdot1+2\cdot2+5\cdot3}{1+4+9}=\dfrac{20}{14}=\dfrac{10}{7}$. So $\tilde J_1(x)=\tfrac{10}{7}x$, an imperfect fit.

**Stage 0:** $\beta^s=\min_u\big[u^2+\tfrac{10}{7}(x+u)\big]$. The three options are $u=-1$: $\tfrac{10}{7}x-\tfrac37$; $u=0$: $\tfrac{10}{7}x$; $u=1$: $\tfrac{10}{7}x+\tfrac{17}{7}$. So $u=-1$ wins, for every $x$.
- $x=1$: $\tfrac{10-3}{7}=1$.
- $x=2$: $\tfrac{20-3}{7}=\tfrac{17}{7}$.
- $x=3$: $\tfrac{30-3}{7}=\tfrac{27}{7}$.

$r_0=\dfrac{1\cdot1+2\cdot\tfrac{17}{7}+3\cdot\tfrac{27}{7}}{14}=\dfrac{\tfrac{7+34+81}{7}}{14}=\dfrac{122}{98}=\dfrac{61}{49}\approx1.245$. The error of the stage-1 fit enters the stage-0 targets. Stage 0 only sees $\tilde J_1$, not the true $J_1$.

## Concepts
- [[multilayer-perceptron]] (new) — linear layers alternating with scalar nonlinear units, ending in a linear weighting; used to represent costs or policies (p. 372, p. 378)
- [[universal-approximation-theorem]] (new) — roughly, with enough nonlinear units a network can approximate arbitrarily closely any piecewise continuous function on a compact set; gives no unit count (pp. 376–377)
- [[overfitting-regularization]] (new) — a model with a relatively large number of parameters (comparable to the training-set size) matches training data very well but may not do as well on new data. A regularization term helps to avoid this (p. 377)
- [[incremental-gradient]] (new) — gradient steps on one cost component (or minibatch) at a time; standard for network training (p. 378)
- [[fitted-value-iteration]] (new) — fit $\tilde J_k$ by least squares to one-step Bellman targets, backward in $k$ (p. 380)
- [[q-factor]] (new) — expected stage cost plus optimal (or base-policy) cost-to-go after a given first control (p. 382)
- [[model-based vs model-free RL]] — here "model-free" means a simulator replaces a mathematical model (p. 382)
- [[approximate-policy-iteration]] (new) — policy iteration with least-squares evaluation of $Q_\mu$ and approximate improvement (p. 385)
- [[exploration vs exploitation]] — here, training samples must visit states a policy rarely visits; off-policies help (p. 387)
- [[sarsa-dqn]] (new) — optimistic PI with Q-factor approximation and a single-sample update; DQN adds experience replay (p. 388, p. 389)
- [[rollout]] (new) — improve a base policy by lookahead plus simulation of that policy, possibly truncated with a terminal cost (p. 392)
- [[feature-state-pomdp]] (new) — a generalized sufficient statistic $y$ that determines the belief and updates via $F(y,u,z)$ (p. 391)
- [[advantage-updating]] (new) — approximate $Q^*-\min_uQ^*$ instead of $Q^*$ (p. 395)
- [[baseline]] (new) — a subtracted constant or state-dependent term that reduces the range of the target (p. 396)
- [[differential-training]] (new) — approximate cost differences between state pairs, trained via a differential DP equation (p. 398)
- [[policy]] — here parametrized by a policy network, trained by classification (p. 393)

## Canonical instances
- [[alphazero-networks]] — specialized board-structured network (p. 372); Bayesian optimization used to tune its deep network (p. 377); deep networks an important factor in its success (p. 379)
- [[tesauro-backgammon]] — success with one or two nonlinear layers (p. 378)
- [[example-3-3-1-small-delta]] — scalar linear-quadratic system where $Q_\pi$ is dominated by a state-only term (p. 396)
- [[dqn-experience-replay]] — buffer of past samples reused for training (p. 389)
- [[pipeline-repair-pomdp]] — case study of approximate rollout and PI [BBW20] (p. 395)

## Bridges (candidates)
- [structural-analogy] feature state $y$ with estimator $F(y,u,z)$ ↔ control-theory: observer or Kalman filter state that is exactly updated from control and measurement (p. 391)
- [structural-analogy] SARSA update (3.27) ↔ temporal-difference learning: parameter moves along a gradient times the Q prediction error
- [structural-analogy] policy chattering in approximate PI ↔ control theory: limit cycles in a loop with nonlinearity (p. 387)
- [metaphor] advantage updating, baselines ↔ control theory: removing the operating-point offset to work with deviations
- [structural-analogy] rollout or one-step lookahead as a Newton step ↔ optimization: Newton iteration on the Bellman equation (pp. 378, 386)

## Questions this raises
- When does a fit of the Bellman target in least squares keep the final policy good? Does it help to fit the targets more accurately?
- How should the sampling distribution be chosen when the optimal policy is unknown, since "representative" is defined by it?
- Why does overparametrization help mitigate overfitting, when the text says regularization is normally needed to fight it?
- Under what conditions does SARSA with function approximation converge? The text says it is unclear.

## Reading notes
- This unit starts at the end of Sec. 3.1.3 (p. 372) and ends mid-Sec. 3.3.7, at the end of p. 398. The derivation of the differential equation for $G_k$ is cut off at the end of p. 398 (the displayed equation ends with a comma).
- Offset: printed = pdf − 20.
- Misprint in Example 3.3.1 (p. 396): the printed last coefficient of $A_\mu$ is "$\frac{5^2}{4}x^2$". Direct computation gives $\min_v(v^2+\tfrac52xv)=-\tfrac{25}{16}x^2$ at $v=-\tfrac54x$, so the term should be $+\tfrac{25}{16}x^2=(\tfrac54)^2x^2$. The conclusion is not affected. I copied the printed form above.
- Slips on p. 398: the first DP equation shows $\mu_k(x)$ for $\mu_k(x_k)$, and the term $g(\hat x_k,\dots)$ lacks the subscript $k$. In the derivation I wrote $\mu_k(x_k)$ and $g_k$.
- In the text layer, "→" sometimes appears where a minus sign belongs (e.g. "$r_k\to\gamma^k$"). I checked the equations against the page images.
- Closed forms use a matrix inverse. The pages do not state when the inverse exists.
- p. 384 describes $g(i,u,j)$ as an "average cost per stage"; p. 391 calls it the transition cost. I used the latter.
- The unit lists no exercises.
