---
id: sutton-2018-rl/ch11-off
work: sutton-2018-rl
unit: "Chapter 11 — Off-policy Methods with Approximation"
pages: 257–286
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Off-policy Methods with Approximation

## L0 — One line
Combining function approximation, bootstrapping and off-policy training (the "deadly triad") can make learning diverge, and the improved methods (Gradient-TD, Emphatic-TD) come with weaker theory and less satisfying results than on-policy learning.

## L1 — The gist (≤ 120 words)
The chapter asks why off-policy learning with function approximation is harder than on-policy learning. Tabular off-policy algorithms extend easily to semi-gradient form, but these may diverge, as Baird's counterexample shows. The danger comes from combining function approximation, bootstrapping and off-policy training. The chapter compares error objectives and argues that the Bellman error cannot be learned from observable data. It then presents two families with better guarantees: Gradient-TD (stochastic gradient descent on the projected Bellman error) and Emphatic-TD (reweighting updates toward an on-policy distribution). The authors call the area unsettled, and they expect high variance to probably remain a challenge.

**Prerequisites:** value functions and TD error; importance sampling; linear function approximation $\hat v=\mathbf w^\top\mathbf x$; stochastic gradient descent; matrix–vector products; expectations.

## L2 — Key ideas (5–10 bullets)
- Off-policy learning has two challenges: the update *target* (handled by importance sampling, at the cost of variance) and the update *distribution* (needs new methods). (pp. 257–258)
- Semi-gradient off-policy methods follow from the tabular ones by replacing array updates with weight updates. They may diverge. (pp. 258–259, 262)
- Divergence examples: a one-weight $w$/$2w$ fragment, Baird's counterexample, and the Tsitsiklis–Van Roy example. Even least-squares fitting at each DP step does not guarantee stability. (pp. 260–263)
- The danger of instability arises whenever function approximation, bootstrapping and off-policy training are all combined (the deadly triad). With only two of the three, instability can be avoided. (p. 264)
- Linear value-function geometry defines several error objectives (VE, BE, PBE, TDE) with potentially different minimizers. (pp. 266–269)
- Residual-gradient methods (SGD on the BE) converge robustly but not necessarily to desirable values, and the BE is not learnable from feature-vector data. (pp. 270–277)
- Gradient-TD (GTD2, TDC) does SGD on the PBE in $O(d)$ time with a second weight vector. Emphatic-TD reweights updates toward an on-policy distribution. (pp. 278–282)
- Off-policy learning has inherently higher variance; several partial remedies are listed and the field is called unsettled. (pp. 283–285)

## L3 — Walkthrough

### Introduction (pp. 257–258)
- Off-policy learning: learn about target policy $\pi$ from data of behavior policy $b$. In control, $\pi$ is typically greedy in $\hat q$ and $b$ more exploratory, e.g. $\varepsilon$-greedy. (p. 257)
- The challenge has two parts. (1) The *target of the update* (not the target policy). Importance sampling handles this; it may increase variance but is needed in all successful algorithms. (2) The *distribution of updates*, which arises only with function approximation. The on-policy distribution matters for semi-gradient stability. (pp. 257–258)
- Two approaches: use importance sampling to warp the update distribution back to on-policy (then semi-gradient converges in the linear case), or use true gradient methods that need no special distribution. The authors say it is unclear which is more effective in practice. (p. 258)

### 11.1 Semi-gradient Methods (pp. 258–259)
These methods address part 1 but not part 2, so they may diverge in some cases yet are often used. In the tabular case they are guaranteed stable and asymptotically unbiased. (p. 258)

Per-step importance sampling ratio:
$$\rho_t \doteq \rho_{t:t}=\frac{\pi(A_t|S_t)}{b(A_t|S_t)}\tag{11.1}$$

Semi-gradient off-policy TD(0):
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\rho_t\delta_t\nabla\hat v(S_t,\mathbf w_t)\tag{11.2}$$
$$\delta_t\doteq R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_t)\ \text{(episodic, discounted)}\tag{11.3}$$
$$\delta_t\doteq R_{t+1}-\bar R_t+\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_t)\ \text{(continuing, average reward)}\tag{11.4}$$

Semi-gradient Expected Sarsa (no importance sampling): (p. 259)
$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\delta_t\nabla\hat q(S_t,A_t,\mathbf w_t)\tag{11.5}$$
with $\delta_t\doteq R_{t+1}+\gamma\sum_a\pi(a|S_{t+1})\hat q(S_{t+1},a,\mathbf w_t)-\hat q(S_t,A_t,\mathbf w_t)$ (episodic). The continuing form uses $-\bar R_t$ and no $\gamma$. This is appropriate in the tabular case. With function approximation it is less clear, since different state–action pairs might deserve different weights. The authors say a proper resolution awaits a better theory. (p. 259)

$n$-step semi-gradient Sarsa uses importance sampling:
$$\mathbf w_{t+n}\doteq\mathbf w_{t+n-1}+\alpha\rho_{t+1}\cdots\rho_{t+n}\,[G_{t:t+n}-\hat q(S_t,A_t,\mathbf w_{t+n-1})]\nabla\hat q(S_t,A_t,\mathbf w_{t+n-1})\tag{11.6}$$
with episodic $G_{t:t+n}\doteq R_{t+1}+\dots+\gamma^{n-1}R_{t+n}+\gamma^n\hat q(S_{t+n},A_{t+n},\mathbf w_{t+n-1})$. The continuing return subtracts $\bar R$ at each reward and has no discounting. At episode ends, $\rho_k$ for $k\ge T$ is taken as 1 and $G_{t:t+n}=G_t$ if $t+n\ge T$. (p. 259)

$n$-step tree backup needs no importance sampling:
$$\mathbf w_{t+n}\doteq\mathbf w_{t+n-1}+\alpha[G_{t:t+n}-\hat q(S_t,A_t,\mathbf w_{t+n-1})]\nabla\hat q(S_t,A_t,\mathbf w_{t+n-1})\tag{11.7}$$
$$G_{t:t+n}\doteq\hat q(S_t,A_t,\mathbf w_{t+n-1})+\sum_{k=t}^{t+n-1}\delta_k\prod_{i=t+1}^{k}\gamma\pi(A_i|S_i)\tag{11.8}$$
with $\delta_t$ as for Expected Sarsa. Semi-gradient $n$-step $Q(\sigma)$ and $n$-step state-value forms are left as exercises. (p. 259)

*Intuition note:* Going from tabular to approximate needs only one change: update weights along the gradient of $\hat v$ instead of one table entry. Importance sampling still corrects *what* is learned, but nothing yet corrects *where* the updates happen.

### 11.2 Examples of Off-policy Divergence (pp. 260–264)
**The $w$-to-$2w$ fragment.** Two states have estimated values $w$ and $2w$ (features 1 and 2). The first state has one action, going to the second with reward 0. (p. 260)
- Verbal case: start at $w=10$ (values 10 → 20), $\gamma\approx1$, $\alpha=0.1$. $w$ rises to about 11, so the second state rises to about 22. The TD error is then about 11, larger than before. $w$ goes to about 12.1 and keeps growing. (p. 260)
- Exact version: $\rho_t=1$ (only one action) and
$$\delta_t=0+\gamma 2w_t-w_t=(2\gamma-1)w_t,\qquad w_{t+1}=w_t+\alpha\cdot1\cdot(2\gamma-1)w_t\cdot1=\big(1+\alpha(2\gamma-1)\big)w_t.$$
- If the constant exceeds 1, $w$ goes to $\pm\infty$. The constant exceeds 1 whenever $\gamma>0.5$, and this does not depend on the step size as long as $\alpha>0$. The step size changes the rate of divergence, not whether it happens. (p. 260)
- Key point: the one transition recurs without $w$ being updated on other transitions. Off-policy, the behavior policy may take actions the target never would; there $\rho_t=0$ and no update is made. On-policy, $\rho_t$ is always one, and each entry into the $2w$ state must be followed by a transition out. That transition would reduce $w$ unless it led to a state of even higher value, which in turn must be followed by a state of higher value, or else $w$ is reduced. In the authors' image, the piper must eventually be paid on-policy, whereas off-policy a promise can be made and then forgotten and forgiven. (pp. 260–261)

**Baird's counterexample (Fig. 11.1, p. 261).** Seven states, two actions. Dashed action: to one of the six upper states with equal probability. Solid action: to the seventh state. $b$: dashed $6/7$, solid $1/7$ (uniform next-state distribution, also the start distribution). $\pi$: always solid, so the on-policy distribution sits on state 7. Reward is 0 everywhere, $\gamma=0.99$. Linear values: upper states $2w_i+w_8$ ($i=1..6$), seventh state $w_7+2w_8$, $\mathbf w\in\mathbb R^8$. For example $\mathbf x(1)=(2,0,0,0,0,0,0,1)^\top$. (pp. 261–262)
- $v_\pi=0$ is exactly representable with $\mathbf w=0$ (and in many other ways: 8 weights, 7 states). The feature vectors are linearly independent, so this seems a favorable case. (p. 262)
- Semi-gradient TD(0) diverges for any positive step size (Fig. 11.2, left: $\alpha=0.01$, initial $\mathbf w=(1,1,1,1,1,1,10,1)^\top$). It also diverges for an expected, DP-style semi-gradient sweep (right): (p. 262)
$$\mathbf w_{k+1}\doteq\mathbf w_k+\frac{\alpha}{|\mathcal S|}\sum_s\Big(\mathbb E_\pi[R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_k)\mid S_t=s]-\hat v(s,\mathbf w_k)\Big)\nabla\hat v(s,\mathbf w_k)\tag{11.9}$$
- If just the distribution of these DP updates in Baird's counterexample is changed from uniform to on-policy (which generally requires asynchronous updating), convergence is guaranteed to a solution with error bounded by (9.14). The authors say the example shows that even the simplest combination of bootstrapping and function approximation can be unstable if updates are not done according to the on-policy distribution. (pp. 262–263)
- Similar counterexamples exist for Q-learning. It may be possible to guarantee convergence when $b$ is close to $\pi$ (e.g. $\varepsilon$-greedy). The authors know of no divergence in that case but no theoretical analysis either. (p. 263)

**Example 11.1: Tsitsiklis and Van Roy.** Add to the $w$/$2w$ fragment a terminal state. The second state loops to itself with probability $1-\varepsilon$ and terminates with probability $\varepsilon$. All rewards are 0. At each step set $w_{k+1}$ to minimize the VE against the expected one-step return, i.e. the best least-squares fit: (p. 263)
$$w_{k+1}=\arg\min_w\sum_s\big(\hat v(s,w)-\mathbb E_\pi[R_{t+1}+\gamma\hat v(S_{t+1},w_k)\mid S_t=s]\big)^2$$
$$=\arg\min_w\big(w-\gamma 2w_k\big)^2+\big(2w-(1-\varepsilon)\gamma 2w_k\big)^2=\frac{6-4\varepsilon}{5}\gamma w_k\tag{11.10}$$
The sequence diverges when $\gamma>\frac{5}{6-4\varepsilon}$ and $w_0\ne0$. If the feature vectors were linearly independent, exact fitting would reduce the method to tabular DP; the point is the case where exact fitting is not possible. There, stability is not guaranteed even when forming the best approximation at each iteration. (p. 263)

*Averagers.* Stability is guaranteed for approximators that do not extrapolate from observed targets (nearest neighbor, locally weighted regression), but not for tile coding or ANNs. (p. 264)

*Intuition note:* In the $w$/$2w$ fragment, the weight is multiplied by a constant on each pass. If that constant exceeds 1, errors feed on themselves. On-policy, each rise in $w$ must eventually be followed by transitions that tend to pull $w$ back, unless they lead to ever higher values.

### 11.3 The Deadly Triad (pp. 264–265)
The danger of instability and divergence arises whenever all three of these are combined: (p. 264)
1. **Function approximation** (generalizing over a state space much larger than memory).
2. **Bootstrapping** (targets that include existing estimates, as in DP or TD, rather than complete returns).
3. **Off-policy training** (a distribution of transitions other than the target policy's; uniform DP sweeps count).

The danger is not due to control, GPI, learning or environment uncertainty: it occurs in simple prediction and in DP with a known environment. If any *two* elements are present but not all three, instability can be avoided. (p. 264)

Can one be given up?
- *Function approximation*: no. Scalable, expressive methods are needed. State aggregation and nonparametric methods are too weak or costly, and least-squares methods such as LSTD are $O(d^2)$ and so too expensive. (p. 264)
- *Bootstrapping*: possible, at a cost in computation (Monte Carlo must store everything until the return arrives) and in data efficiency. Examples: Figs. 7.2, 9.2, 10.4, 12.14. Bootstrapping can hurt when the state representation is poor (Tetris is cited, with a reference). A poor representation can also cause bias, the reason the authors give for the poorer asymptotic bound of bootstrapping methods (9.14). The authors judge the ability to bootstrap extremely valuable. (pp. 264–265)
- *Off-policy*: on-policy methods are often adequate (use Sarsa instead of Q-learning). But off-policy learning is essential for anticipated uses where an agent learns many value functions and policies in parallel from one stream of experience. Parallel learning is conceptually possible because the one behavior policy may overlap in part with many target policies. (p. 265)

### 11.4 Linear Value-function Geometry (pp. 266–269)
Treat value functions as vectors over states. With 3 states and 2 parameters, representable functions form a plane inside 3-D space; $v_\pi$ is assumed to lie off the plane (Fig. 11.3). (p. 266)

Norm weighted by distribution $\mu$ (often the on-policy distribution):
$$\|v\|_\mu^2\doteq\sum_s\mu(s)v(s)^2\tag{11.11}$$
Then $\overline{\text{VE}}(\mathbf w)=\|v_{\mathbf w}-v_\pi\|_\mu^2$. Projection onto representable functions:
$$\Pi v\doteq v_{\mathbf w},\quad \mathbf w=\arg\min_{\mathbf w\in\mathbb R^d}\|v-v_{\mathbf w}\|_\mu^2\tag{11.12}$$
$\Pi v_\pi$ is what Monte Carlo methods find asymptotically, often slowly. (p. 267)

Box (p. 268). For linear approximation the projection is an $|\mathcal S|\times|\mathcal S|$ matrix. Here $\mathbf D$ is diagonal with $\mu(s)$ ($|\mathcal S|\times|\mathcal S|$), $\mathbf X$ is $|\mathcal S|\times d$ with rows $\mathbf x(s)^\top$; use the pseudoinverse if the inverse does not exist:
$$\Pi\doteq\mathbf X(\mathbf X^\top\mathbf D\mathbf X)^{-1}\mathbf X^\top\mathbf D\tag{11.13}$$
$$\|v\|_\mu^2=v^\top\mathbf D v\tag{11.14}$$
$$v_{\mathbf w}=\mathbf X\mathbf w\tag{11.15}$$

Bellman equation: $v_\pi(s)=\sum_a\pi(a|s)\sum_{s',r}p(s',r|s,a)[r+\gamma v_\pi(s')]$ (11.16); $v_\pi$ is its only exact solution. Plugging in $v_{\mathbf w}$ gives the **Bellman error**: (p. 268)
$$\bar\delta_{\mathbf w}(s)\doteq\Big(\sum_a\pi(a|s)\sum_{s',r}p(s',r|s,a)[r+\gamma v_{\mathbf w}(s')]\Big)-v_{\mathbf w}(s)\tag{11.17}$$
$$=\mathbb E_\pi[R_{t+1}+\gamma v_{\mathbf w}(S_{t+1})-v_{\mathbf w}(S_t)\mid S_t=s,A_t\sim\pi]\tag{11.18}$$
So the Bellman error is the expectation of the TD error. The vector $\bar\delta_{\mathbf w}\in\mathbb R^{|\mathcal S|}$ gives
$$\overline{\text{BE}}(\mathbf w)=\|\bar\delta_{\mathbf w}\|_\mu^2\tag{11.19}$$
In general it cannot be reduced to zero. With linear approximation its minimizer is unique and in general differs from the VE minimizer. (p. 268)

Bellman operator $B_\pi:\mathbb R^{|\mathcal S|}\to\mathbb R^{|\mathcal S|}$, so that $\bar\delta_{\mathbf w}=B_\pi v_{\mathbf w}-v_{\mathbf w}$: (pp. 268–269)
$$(B_\pi v)(s)\doteq\sum_a\pi(a|s)\sum_{s',r}p(s',r|s,a)[r+\gamma v(s')]\tag{11.20}$$
$$v_\pi=B_\pi v_\pi\tag{11.21}$$
Applied to a representable function, $B_\pi$ in general gives a function outside the subspace. DP (without approximation) iterates $B_\pi$ to $v_\pi$, its only fixed point. With approximation one must project back each time, giving a DP-like process within the subspace. The **projected Bellman error** and its mean square are (p. 269)
$$\overline{\text{PBE}}(\mathbf w)=\|\Pi\bar\delta_{\mathbf w}\|_\mu^2\tag{11.22}$$
With linear approximation some point has zero PBE: the TD fixed point $\mathbf w_{TD}$ (Section 9.4). It is not always stable under semi-gradient off-policy TD, and it is generally different from the VE and BE minimizers. Methods converging to it are in 11.7 and 11.8. (p. 269)

*Intuition note:* Four different ways of measuring how wrong an approximate value function is give four potentially different best answers. TD methods find the PBE-zero point, not the point closest to $v_\pi$.

### 11.5 Gradient Descent in the Bellman Error (pp. 269–274)
True SGD goes downhill in expectation, so it is typically stable. Among earlier algorithms only Monte Carlo methods are true SGD. They converge off-policy and for nonlinear differentiable approximators, but are often slower than bootstrapping. (p. 270) The authors conclude that the BE-based approach is a misstep that yields no good learning algorithms, though it fails in an informative way. (p. 270)

**Naive attempt: mean square TD error.**
$$\overline{\text{TDE}}(\mathbf w)=\sum_s\mu(s)\mathbb E[\delta_t^2|S_t{=}s,A_t{\sim}\pi]=\sum_s\mu(s)\mathbb E[\rho_t\delta_t^2|S_t{=}s,A_t{\sim}b]=\mathbb E_b[\rho_t\delta_t^2]$$
(last step if $\mu$ is the distribution under $b$). SGD gives
$$\mathbf w_{t+1}=\mathbf w_t-\tfrac12\alpha\nabla(\rho_t\delta_t^2)=\mathbf w_t-\alpha\rho_t\delta_t\nabla\delta_t=\mathbf w_t+\alpha\rho_t\delta_t\big(\nabla\hat v(S_t,\mathbf w_t)-\gamma\nabla\hat v(S_{t+1},\mathbf w_t)\big)\tag{11.23}$$
This is (11.2) plus a final term; it is the *naive residual-gradient algorithm* (after Baird, 1995). It converges robustly, but not necessarily to a desirable place. (pp. 270–271)

**Example 11.2: A-split.** Episodic MRP, $\gamma=1$, on-policy, tabular. From A (reward 0) go to B or C with probability ½ each. B then terminates with reward 1, C with reward 0. True values: A=½, B=1, C=0. (p. 271)
- Naive residual gradient converges to B=¾, C=¼, A=½, which minimize the TDE. For these values the first transition has TD error $\pm\frac14$ (squared $\frac1{16}$). The second has TD error $\pm\frac14$ (squared $\frac1{16}$). So the TDE is $\frac1{16}$ on both steps. (p. 271)
- For the true values, the first-step squared error is $\frac14$ and the second is 0, a mean of $\frac18>\frac1{16}$. So the true values do not minimize the TDE. (p. 271)
- By penalizing all TD errors, minimizing the TDE achieves something more like temporal smoothing than accurate prediction. (p. 272)

**Residual-gradient algorithm (Bellman error).** Because the BE is the expected TD error, repeat the derivation with the expectation inside the square (all expectations conditional on $S_t$): (p. 272)
$$\begin{aligned}\mathbf w_{t+1}&=\mathbf w_t-\tfrac12\alpha\nabla(\mathbb E_\pi[\delta_t]^2)=\mathbf w_t-\tfrac12\alpha\nabla(\mathbb E_b[\rho_t\delta_t]^2)\\&=\mathbf w_t-\alpha\mathbb E_b[\rho_t\delta_t]\nabla\mathbb E_b[\rho_t\delta_t]\\&=\mathbf w_t-\alpha\mathbb E_b\big[\rho_t(R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w)-\hat v(S_t,\mathbf w))\big]\mathbb E_b[\rho_t\nabla\delta_t]\\&=\mathbf w_t+\alpha\Big[\mathbb E_b[\rho_t(R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w))]-\hat v(S_t,\mathbf w)\Big]\Big[\nabla\hat v(S_t,\mathbf w)-\gamma\mathbb E_b[\rho_t\nabla\hat v(S_{t+1},\mathbf w)]\Big]\end{aligned}$$
Plugging in single samples gives almost exactly (11.23). Footnote 1: for state values a small difference in $\rho_t$ treatment remains; for action values it reduces exactly to the naive version. But this is naive: $S_{t+1}$ appears in *two* multiplied expectations, so an unbiased product needs two independent next-state samples. It works (a) in deterministic environments, or (b) with a simulator that can be rolled back to draw a second next state. Then it converges to a minimum of the BE under usual step-size conditions: robustly for linear and nonlinear approximators, and in the linear case to the unique BE minimizer. (pp. 272–273)

Three unsatisfactory aspects: (p. 273)
1. It is empirically much slower than semi-gradient methods. Baird and Moore (1999) proposed starting with semi-gradient methods and switching gradually to residual gradient.
2. It seems to converge to the wrong values when function approximation is genuine.
3. Explained in 11.6; like the second, it concerns the BE itself, not a particular algorithm. (p. 274)

**Example 11.3: A-presplit.** Start in A1 or A2 with equal probability. A1→B (reward 0)→terminate (reward 1). A2→C (reward 0)→terminate (reward 0). A1 and A2 share one weight; B and C have their own, so there are three components. Everything else is deterministic. (p. 273)
- To the learner it looks identical to A-split. Semi-gradient TD gets the ideal values (A=½, B=1, C=0), while the naive residual gradient gets B=¾, C=¼. The non-naive algorithm is the same algorithm in a deterministic problem. On deterministic problems BE = TDE, so this naive solution also minimizes the BE. (p. 273)
- Hence minimizing the BE "may not be a desirable goal". (p. 274)

*Intuition note:* Squared-TD-error objectives penalize every TD error, including the unavoidable ones when the future is random, and so can prefer smoothed values over true values. Taking the gradient of the BE correctly also needs two independent samples of the next state, which normal interaction with a real environment does not give.

### 11.6 The Bellman Error is Not Learnable (pp. 274–277)
Learnable here means learnable at all with any amount of experience, not efficiently learnable. A quantity is not learnable if it cannot be computed or estimated from the observed sequence of feature vectors, actions and rewards, even with infinite data. (p. 274)

**Two MRPs.** Left: one state, emits random 0s and 2s (probability ½ each). Right: two states, each step stays or switches with probability ½, deterministic reward 0 in one state and 2 in the other. All states have feature $x=1$ and value $w$. Both produce the same data distribution, so one cannot tell whether there are one or two states or whether the process is stochastic. (pp. 274–275)
- With $\gamma=0$ the true values are 1 (left) and 0, 2 (right). With $w=1$, $\overline{\text{VE}}=0$ for the left MRP and $1$ for the right. So the VE is not learnable. (p. 275)
- However, $w=1$ is optimal for both (if $\mu$ is the same on the two indistinguishable states): the *minimizer* of VE may still be learnable. The authors show it is, via the return error: (p. 275)
$$\overline{\text{RE}}(\mathbf w)=\mathbb E\big[(G_t-\hat v(S_t,\mathbf w))^2\big]=\overline{\text{VE}}(\mathbf w)+\mathbb E\big[(G_t-v_\pi(S_t))^2\big]\tag{11.24}$$
(on-policy case). The two objectives differ by a variance term independent of $\mathbf w$, so they share the optimal $\mathbf w^*$. RE is learnable, hence so is $\mathbf w^*$ (Fig. 11.4, left). (p. 275)

**Example 11.4: BE counterexample (p. 276).** Left MRP: A→B with reward 0; from B, either B→A with reward 1 or B→B with reward −1 (equal probability). Right MRP: three states A, B, B′. A goes to B or to B′ with reward 0 (equal probability). B goes to A with reward 1. B′ goes to B or stays in B′, each with reward −1 (equal probability). B and B′ look the same and share a weight; $\mathbf w=(w_A,w_B)$ has two components; $\mu(s)=\frac13$ for all three states. (p. 276)
- Observable data are identical: single A, then 0, then some number of apparent Bs, each followed by −1 except the last, which is followed by 1; then repeat. The probability of a string of $k$ Bs is $2^{-k}$. (p. 276)
- At $\mathbf w=0$: $\overline{\text{BE}}=0$ for the first MRP. For the second, B and B′ each have squared error 1, so $\overline{\text{BE}}=\mu(B)\cdot1+\mu(B')\cdot1=\frac23$. So the BE is not learnable. (p. 276)
- Moreover the minimizing $\mathbf w$ differs: $\mathbf w=0$ for the first MRP for any $\gamma$; for the second a complicated function of $\gamma$, tending to $(-\frac12,0)^\top$ as $\gamma\to1$. So the BE minimizer cannot be estimated from data alone. A's BE-minimizing value is negative because it compromises between errors on leaving and on entering A. (p. 276)

PBE and TDE are learnable from data, with minimizers $\mathbf w_3^*,\mathbf w_4^*$ that in general differ from each other and from the BE minimizers (Fig. 11.4, right). The BE is thus limited to model-based settings. Residual-gradient can minimize the BE only because it may double-sample "a state ... guaranteed to be the same underlying state", which feature vectors alone cannot ensure. All this directs attention to the PBE. (p. 277)

*Intuition note:* Two different worlds can look identical through the feature vectors the learner sees. The BE gives different numbers (and different best weights) in the two worlds, so no algorithm can aim at it using data alone.

### 11.7 Gradient-TD Methods (pp. 278–281)
Goal: an SGD method for the PBE (linear case), $O(d)$ rather than the $O(d^2)$ of least squares. Gradient-TD methods come close to this goal at the cost of a rough doubling of computation. Take $\mu$ as the behavior-policy state distribution. (p. 278)

Derivation (shapes: $\mathbf X$ is $|\mathcal S|\times d$, $\mathbf D$ is $|\mathcal S|\times|\mathcal S|$, $\bar\delta_{\mathbf w}$ is an $|\mathcal S|$-vector, $\mathbf X^\top\mathbf D\mathbf X$ is $d\times d$): (p. 278)
$$\begin{aligned}\overline{\text{PBE}}(\mathbf w)&=\|\Pi\bar\delta_{\mathbf w}\|_\mu^2=(\Pi\bar\delta_{\mathbf w})^\top\mathbf D\Pi\bar\delta_{\mathbf w}=\bar\delta_{\mathbf w}^\top\Pi^\top\mathbf D\Pi\bar\delta_{\mathbf w}\\&=\bar\delta_{\mathbf w}^\top\mathbf D\mathbf X(\mathbf X^\top\mathbf D\mathbf X)^{-1}\mathbf X^\top\mathbf D\bar\delta_{\mathbf w}\end{aligned}\tag{11.25}$$
(using (11.13) and the identity $\Pi^\top\mathbf D\Pi=\mathbf D\mathbf X(\mathbf X^\top\mathbf D\mathbf X)^{-1}\mathbf X^\top\mathbf D$)
$$=(\mathbf X^\top\mathbf D\bar\delta_{\mathbf w})^\top(\mathbf X^\top\mathbf D\mathbf X)^{-1}(\mathbf X^\top\mathbf D\bar\delta_{\mathbf w})\tag{11.26}$$
$$\nabla\overline{\text{PBE}}(\mathbf w)=2\nabla[\mathbf X^\top\mathbf D\bar\delta_{\mathbf w}]^\top(\mathbf X^\top\mathbf D\mathbf X)^{-1}(\mathbf X^\top\mathbf D\bar\delta_{\mathbf w})$$
Each factor is an expectation:
- $\mathbf X^\top\mathbf D\bar\delta_{\mathbf w}=\sum_s\mu(s)\mathbf x(s)\bar\delta_{\mathbf w}(s)=\mathbb E[\rho_t\delta_t\mathbf x_t]$, the expected semi-gradient TD(0) update.
- $\nabla\mathbb E[\rho_t\delta_t\mathbf x_t]^\top=\mathbb E[\rho_t\nabla\delta_t^\top\mathbf x_t^\top]=\mathbb E[\rho_t\nabla(R_{t+1}+\gamma\mathbf w^\top\mathbf x_{t+1}-\mathbf w^\top\mathbf x_t)^\top\mathbf x_t^\top]=\mathbb E[\rho_t(\gamma\mathbf x_{t+1}-\mathbf x_t)\mathbf x_t^\top]$ (episodic $\delta_t$).
- $\mathbf X^\top\mathbf D\mathbf X=\sum_s\mu(s)\mathbf x(s)\mathbf x(s)^\top=\mathbb E[\mathbf x_t\mathbf x_t^\top]$.

$$\nabla\overline{\text{PBE}}(\mathbf w)=2\,\mathbb E[\rho_t(\gamma\mathbf x_{t+1}-\mathbf x_t)\mathbf x_t^\top]\;\mathbb E[\mathbf x_t\mathbf x_t^\top]^{-1}\;\mathbb E[\rho_t\delta_t\mathbf x_t]\tag{11.27}$$
Sampling the first and last factors together would be biased (both contain $\mathbf x_{t+1}$), as with residual gradient. Estimating all three separately works but needs $d\times d$ storage; storing two and sampling the third remains $O(d^2)$. (p. 279)

Gradient-TD stores the product of the last two factors, a $d$-vector:
$$\mathbf v\approx\mathbb E[\mathbf x_t\mathbf x_t^\top]^{-1}\mathbb E[\rho_t\delta_t\mathbf x_t]\tag{11.28}$$
This is the solution of a least-squares problem approximating $\rho_t\delta_t$ from features, learned by the LMS rule with importance ratio, with a second step size $\beta>0$:
$$\mathbf v_{t+1}\doteq\mathbf v_t+\beta\rho_t(\delta_t-\mathbf v_t^\top\mathbf x_t)\mathbf x_t$$
Main update:
$$\begin{aligned}\mathbf w_{t+1}&=\mathbf w_t-\tfrac12\alpha\nabla\overline{\text{PBE}}(\mathbf w_t)\\&=\mathbf w_t+\alpha\,\mathbb E[\rho_t(\mathbf x_t-\gamma\mathbf x_{t+1})\mathbf x_t^\top]\mathbb E[\mathbf x_t\mathbf x_t^\top]^{-1}\mathbb E[\rho_t\delta_t\mathbf x_t]\end{aligned}\tag{11.29}$$
$$\approx\mathbf w_t+\alpha\,\mathbb E[\rho_t(\mathbf x_t-\gamma\mathbf x_{t+1})\mathbf x_t^\top]\mathbf v_t\approx\mathbf w_t+\alpha\rho_t(\mathbf x_t-\gamma\mathbf x_{t+1})\mathbf x_t^\top\mathbf v_t$$
This is **GTD2**; it is $O(d)$ if $\mathbf x_t^\top\mathbf v_t$ (a scalar) is computed first. (pp. 279–280)

A slightly better algorithm, continuing from (11.29): (p. 280)
$$\begin{aligned}\mathbf w_{t+1}&=\mathbf w_t+\alpha\big(\mathbb E[\rho_t\mathbf x_t\mathbf x_t^\top]-\gamma\mathbb E[\rho_t\mathbf x_{t+1}\mathbf x_t^\top]\big)\mathbb E[\mathbf x_t\mathbf x_t^\top]^{-1}\mathbb E[\rho_t\delta_t\mathbf x_t]\\&=\mathbf w_t+\alpha\big(\mathbb E[\mathbf x_t\mathbf x_t^\top]-\gamma\mathbb E[\rho_t\mathbf x_{t+1}\mathbf x_t^\top]\big)\mathbb E[\mathbf x_t\mathbf x_t^\top]^{-1}\mathbb E[\rho_t\delta_t\mathbf x_t]\\&=\mathbf w_t+\alpha\Big(\mathbb E[\rho_t\delta_t\mathbf x_t]-\gamma\mathbb E[\rho_t\mathbf x_{t+1}\mathbf x_t^\top]\mathbb E[\mathbf x_t\mathbf x_t^\top]^{-1}\mathbb E[\rho_t\delta_t\mathbf x_t]\Big)\\&\approx\mathbf w_t+\alpha\big(\mathbb E[\rho_t\delta_t\mathbf x_t]-\gamma\mathbb E[\rho_t\mathbf x_{t+1}\mathbf x_t^\top]\mathbf v_t\big)\approx\mathbf w_t+\alpha\rho_t\big(\delta_t\mathbf x_t-\gamma\mathbf x_{t+1}\mathbf x_t^\top\mathbf v_t\big)\end{aligned}$$
(The second line replaces $\mathbb E[\rho_t\mathbf x_t\mathbf x_t^\top]$ by $\mathbb E[\mathbf x_t\mathbf x_t^\top]$ (added step: valid since $\rho_t$ has expectation one given the state under $b$).) This is **TDC** (TD(0) with gradient correction), also called GTD(0), again $O(d)$ if $\mathbf x_t^\top\mathbf v_t$ is computed first. (p. 280)

*Intuition note:* The PBE gradient is a product of three expectations that cannot all be sampled at once. Gradient-TD learns a helper vector $\mathbf v$ for the awkward part, so each step needs only $O(d)$ work.

**Baird's counterexample (Fig. 11.5, $\alpha=0.005$, $\beta=0.05$).** The PBE falls to zero, but the weights do not go to zero. The VE remains almost 2 after 1000 iterations. An exact solution would need $\mathbf w\propto(1,1,1,1,1,1,4,2)^\top$. The system is converging to an optimal solution, but very slowly because the PBE is already near zero. (pp. 280–281)

**Cascade and two time scales.** The secondary process ($\mathbf v$) proceeds without being influenced by the primary one ($\mathbf w$), while $\mathbf w$'s logic relies on $\mathbf v$ having approximately finished. Convergence proofs often assume the secondary process is on the faster time scale (two-time-scale proofs). With $\alpha$ the primary and $\beta$ the secondary step size, the text states the requirement as a limit involving $\beta\to0$ and $\alpha\to0$. (p. 281)

The authors call Gradient-TD methods currently the most well understood and widely used stable off-policy methods. Extensions: GQ (action values), GTD($\lambda$)/GQ($\lambda$), nonlinear approximation, hybrid-TD (Gradient-like where policies differ, semi-gradient where they agree), proximal and control-variate versions. (p. 281)

### 11.8 Emphatic-TD Methods (pp. 281–283)
Linear semi-gradient TD is stable on-policy because of the positive definiteness of the matrix $\mathbf A$ and the match between state distribution and transition probabilities under $\pi$ (Section 9.4). Off-policy, importance sampling fixes the transitions, but the state distribution is still $b$'s. Idea: reweight *states* to restore an on-policy distribution; then existing results would give stability and convergence. (p. 281)

There are many on-policy distributions: any distribution that results from starting anywhere with all transitions due to $\pi$ is one, provided all states encountered are updated until termination. Any one of them is sufficient to guarantee stability (linear semi-gradient). Discounting is treated as *pseudo termination*: with probability $1-\gamma$ per step the process terminates and restarts in the next state, affecting learning but not the transitions. Since restarts are optional, this relieves the need to keep encountered states in the on-policy distribution. (p. 282)

One-step Emphatic-TD (episodic state values):
$$\delta_t=R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_t),$$
$$\mathbf w_{t+1}=\mathbf w_t+\alpha M_t\rho_t\delta_t\nabla\hat v(S_t,\mathbf w_t),\qquad M_t=\gamma\rho_{t-1}M_{t-1}+I_t,$$
with arbitrary *interest* $I_t$ and *emphasis* $M_t$, $M_{-1}=0$. On Baird's counterexample (expected trajectory, $I_t=1$, $\alpha=0.03$; Fig. 11.6) there are oscillations but everything converges and the VE goes to zero. The actual algorithm has such high variance on this problem that consistent experimental results are nearly impossible to get; it converges in theory but not in practice. (p. 282)

*Intuition note:* Emphatic-TD does not change *which* transitions occur. It scales each update by a running weight so the weighted mixture of updates behaves like on-policy training.

### 11.9 Reducing Variance (pp. 283–284)
Off-policy data are less closely related to the target policy, so greater variance is expected: "You can't expect to learn how to drive by cooking dinner". (p. 283) Importance sampling uses products of ratios. Ratios have expectation one; successive ratios are uncorrelated, so products also have expectation one but may have very high variance. Since ratios multiply the SGD step size, occasional huge steps are harmful. A step size small enough to prevent them makes the expected step tiny and learning slow. (p. 283)

Possible remedies (all only touched on): momentum, Polyak–Ruppert averaging, per-component adaptive step sizes and "importance weight aware" updates (p. 284); weighted importance sampling, which is challenging to adapt to function approximation and can probably only be done approximately with $O(d)$ complexity (p. 284); Tree Backup extensions without importance sampling (Munos et al. 2016; Mahmood, Yu and Sutton 2017); and letting the target policy depend on the behavior policy so ratios stay moderate, e.g. the recognizers of Precup et al. (2006). (p. 284)

### 11.10 Summary (pp. 284–285)
- Tabular Q-learning makes off-policy learning seem easy, but significant function approximation brings new challenges. Reasons for wanting it: flexibility in the exploration–exploitation tradeoff, freeing behavior from learning, and the hope of learning about many things in parallel from one stream of experience (TD learning appears to hold this out; it can be done in special cases, not in every case). (p. 284)
- Part 1 (target correction) is handled by importance sampling at the cost of variance; the authors expect high variance to probably always remain a challenge. Part 2 shows up as instability of bootstrapping semi-gradient methods. (p. 284)
- The authors say true SGD in the BE is not an appealing goal in many cases and is in any case impossible with a learning algorithm, because the BE gradient is not learnable from feature-vector experience. Gradient-TD does SGD in the PBE, whose gradient is learnable at $O(d)$ with a second parameter vector and step size. Emphatic-TD restores the properties that make on-policy learning stable by reweighting updates. (p. 285)
- The authors call the area "relatively new and unsettled" and ask whether the complexity of the new methods is really necessary. (p. 285)

### Bibliographical and Historical Remarks (pp. 285–286)
Credits: semi-gradient TD($\lambda$) (Sutton 1988); $w$-to-$2w$ and the Example 11.1 counterexample (Tsitsiklis & Van Roy); Baird's counterexample (Baird 1995, slightly modified here); deadly triad (identified by Sutton 1995b, analyzed by Tsitsiklis & Van Roy 1997, named by Sutton 2015a); BE (Schweitzer & Seidmann 1985, extended by Baird); A-split (Dayan 1992); the content of Section 11.6 is new to this text; Gradient-TD (Sutton, Szepesvári, Maei 2009b; Sutton et al. 2009a); Emphatic-TD (Sutton, Mahmood, White 2016). (pp. 285–286)

## Toy example (ours, not from the text)
Take the $w$/$2w$ fragment with $\gamma=0.9$, $\alpha=0.1$, start $w_0=10$.

*Off-policy repetition* (only the first transition ever updated): $\delta=(2\gamma-1)w=0.8w$, so $w_{t+1}=w_t+0.1\cdot0.8\,w_t=1.08\,w_t$.
$w_1=10.8$, $w_2=10.8\cdot1.08=11.664$, $w_3=11.664\cdot1.08\approx12.597$. The factor 1.08 exceeds 1, so $w$ grows without bound.

*On-policy version* (our extension: the $2w$ state must also be updated, moving to a terminal state with reward 0): there $\delta=0+0-2w=-2w$ and $\nabla\hat v=2$, so the update is $w\leftarrow w+0.1\cdot(-2w)\cdot2=0.6\,w$.
One full cycle from $w=10$: $10\to10.8\to10.8\cdot0.6=6.48$. The per-cycle factor $1.08\cdot0.6=0.648<1$, so $w\to0$, the true value. The promise made by the first transition is paid by the second.

## Concepts
- [[off-policy-learning]] (new) — learning about a target policy $\pi$ from data generated by a different behavior policy $b$ (p. 257)
- [[importance-sampling-ratio]] (new) — $\rho_t=\pi(A_t|S_t)/b(A_t|S_t)$, correcting the update target; raises variance (pp. 257, 258)
- [[semi-gradient-method]] (new) — update with the gradient of the estimate only, ignoring the bootstrapped target's dependence on $\mathbf w$; not true SGD (pp. 258, 270)
- [[deadly-triad]] (new) — function approximation + bootstrapping + off-policy training; combining all three risks divergence (p. 264)
- [[on-policy-distribution]] (new) — state distribution produced by following the target policy; many exist; any one suffices for linear semi-gradient stability (p. 282)
- [[bellman-equation-value-function]] — $v_\pi=B_\pi v_\pi$; the Bellman operator's only fixed point is $v_\pi$ (pp. 268–269)
- [[bellman-error]] (new) — expected TD error at each state under $\pi$; $\overline{\text{BE}}$ is its $\mu$-weighted squared norm (p. 268)
- [[projected-bellman-error]] (new) — norm of the projection of the Bellman error into the representable subspace; zero at the TD fixed point (p. 269)
- [[residual-gradient-algorithm]] (new) — SGD on the (squared) Bellman error; needs two independent next-state samples (pp. 271–272)
- [[learnability]] (new) — a quantity is learnable if determined by the data distribution of observable features, actions and rewards (p. 274)
- [[gradient-td]] (new) — GTD2, TDC: SGD on the PBE with a second learned vector $\mathbf v$ (pp. 278–280)
- [[emphatic-td]] (new) — updates scaled by emphasis $M_t$ to restore on-policy-like distribution (p. 282)
- [[temporal-difference-learning]] — bootstrapped value learning from the TD error (p. 258)
- [[exploration-vs-exploitation]] — off-policy learning is one way to handle this conflict (p. 257)
- [[stability]] — here: whether weights stay bounded and converge; semi-gradient off-policy may violate it (p. 260)

## Canonical instances
- [[w-to-2w-example]] (new) — one-weight fragment where repeated off-policy update diverges when $\gamma>0.5$ (p. 260)
- [[baird-counterexample]] (new) — seven-state MDP where semi-gradient TD and DP both diverge; also test bed for TDC and Emphatic-TD (pp. 261–262, 280, 283)
- [[tsitsiklis-van-roy-counterexample]] (new) — least-squares fit at each DP step still diverges if $\gamma>5/(6-4\varepsilon)$ (p. 263)
- [[a-split-example]] (new) — naive residual gradient finds B=¾, C=¼ because true values have higher TDE (p. 271)
- [[a-presplit-example]] (new) — looks like A-split to the learner; BE minimizer equals the naive solution (p. 273)
- [[bellman-error-unlearnability-example]] (new) — two MRPs with identical data but different BE and BE minimizers (p. 276)

## Bridges (candidates)
- [same-math] Off-policy semi-gradient factor $1+\alpha(2\gamma-1)$ ↔ control-theory/stability: scalar linear recursion $x_{k+1}=ax_k$ unstable iff $|a|>1$ — same recursion form (here the text's condition is "greater than 1")
- [structural-analogy] BE unlearnable from feature vectors ↔ control-theory/observability: different internal systems giving identical outputs cannot be told apart from data
- [structural-analogy] Primary/secondary cascade with two-time-scale proofs ↔ control-theory: fast inner loop assumed settled for slow outer loop
- [structural-analogy] Projected Bellman operator iteration ↔ control-theory/state-space: projection to representable subspace then dynamics step, fixed point as equilibrium
- [metaphor] "the piper must be paid" (on-policy promises must be kept) ↔ feedback: system kept in check by consequences of its own predictions

## Questions this raises
- Under what conditions on $b$ and $\pi$ (e.g. $\varepsilon$-greedy $b$) can semi-gradient Q-learning be proven stable, given that only the absence of observed divergence is reported?
- Is the extra complexity of Gradient-TD and Emphatic-TD actually necessary, as the authors ask?
- How do variance-reduction methods combine with Emphatic-TD, whose variance on Baird's example is described as so high that consistent experimental results are nearly impossible?
- How would one choose among the PBE, VE and TDE minimizers when they differ?

## Exercises worth doing
- Ex. 11.1 (p. 259) — convert $n$-step off-policy TD (7.9) to semi-gradient form, with returns for episodic and continuing cases — difficulty: medium
- Ex. 11.2 (p. 259) — convert $n$-step $Q(\sigma)$ (7.11, 7.17) to semi-gradient form — difficulty: hard
- Ex. 11.3 (p. 264) — programming: apply one-step semi-gradient Q-learning to Baird's counterexample and show divergence — difficulty: medium
- Ex. 11.4 (p. 275) — prove $\overline{\text{RE}}=\overline{\text{VE}}+\text{variance term}$ (11.24) — difficulty: medium

## Reading notes
- Printed page = pdf page − 22 (pdf 279 = printed 257).
- The text layers of pdf 289 (printed 267) and pdf 299 (printed 277) are badly garbled: figure text overlaps unrelated text. I used the page images; Figures 11.3 and 11.4 and their captions were read from the images.
- Text layers drop overlines and minus signs (e.g. $\overline{\text{VE}}$, "$(-\frac12,0)^\top$" in Example 11.4); the images show them.
- Misprints as printed: p. 263 calls the method "linear, semi-descent" (presumably semi-gradient); p. 271 says "mean reward over the two transitions of 1/8", where the context means the mean squared TD error; p. 273 "slower that"; p. 272 footnote "analagous".
- p. 281 time-scale sentence: only the text layer was available for this page. It reads as a limit with $\beta\to0$ and $\alpha\to0$; I could not check the exact form of the second limit, and the exact step-size ordering is not spelled out beyond a "fast" secondary process.
- Section 11.7's TDC derivation does not state why $\mathbb E[\rho_t\mathbf x_t\mathbf x_t^\top]=\mathbb E[\mathbf x_t\mathbf x_t^\top]$; that explanation is my added step.
