---
id: sutton-2018-rl/ch09-policy-p1
work: sutton-2018-rl
unit: "Chapter 9, part 1/2 — On-policy Prediction with Approximation (intro, 9.1–9.4, 9.5 through 9.5.4 and the start of 9.5.5)"
pages: 197–221
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# On-policy Prediction with Approximation (part 1/2)

## L0 — One line
Replace the value table by a parameterized function $\hat v(s,\mathbf w)$ and learn $\mathbf w$ by (semi-)gradient descent on a state-weighted squared error. Linear features make this analyzable, and the choice of features sets how learning generalizes.

## L1 — The gist (≤ 120 words)
The chapter asks how to estimate $v_\pi$ when there are far more states than weights. Updates then generalize across states, so we must say which states matter: the mean square value error $\overline{\text{VE}}$ weighted by the on-policy distribution. Stochastic gradient descent with an unbiased target (Monte Carlo) converges to a local optimum under decreasing step sizes. Bootstrapping targets (built from current estimates) give only semi-gradient methods. For linear approximators, semi-gradient TD(0) converges to the TD fixed point, whose asymptotic error, in the continuing case, is bounded by $1/(1-\gamma)$ times the best possible. The rest of this part covers feature constructions: polynomials, Fourier cosines, coarse coding, tile coding, and the start of radial basis functions.

**Prerequisites:** gradients and partial derivatives; matrix–vector products; positive definite matrices; stationary distributions of Markov chains; tabular MC and TD(0) updates.

## L2 — Key ideas
- Each RL update $s\mapsto u$ can be treated as one supervised-learning training example. RL also needs methods that learn online and can cope with nonstationary targets (p. 198).
- With approximation, not all states can be fit exactly. We choose a state weighting $\mu$ and minimize $\overline{\text{VE}}(\mathbf w)=\sum_s\mu(s)[v_\pi(s)-\hat v(s,\mathbf w)]^2$. $\mu$ is the on-policy distribution here, usually the fraction of time spent in each state under $\pi$ (p. 199).
- SGD on an unbiased target (gradient Monte Carlo) converges to a local optimum if the step size decreases under the usual conditions. Bootstrapping targets (built from the current value estimate) depend on $\mathbf w$, so those methods are only semi-gradient: they ignore the weights' effect on the target (pp. 201–202).
- In the linear case $\nabla\hat v=\mathbf x(s)$. There is a single optimum, and semi-gradient TD(0) converges to the TD fixed point $\mathbf w_{TD}=\mathbf A^{-1}\mathbf b$, a point near, not at, the optimum (pp. 205–206).
- Stability of on-policy linear TD(0) follows from $\mathbf A$ being positive definite ($\mathbf y^\top\mathbf A\mathbf y>0$ for every real $\mathbf y\ne\mathbf 0$). This relies on the states being updated by the stationary distribution (p. 207).
- $\overline{\text{VE}}(\mathbf w_{TD})\le\frac1{1-\gamma}\min_{\mathbf w}\overline{\text{VE}}(\mathbf w)$ in the continuing case. TD may lose asymptotic accuracy (error up to $1/(1-\gamma)$ times the best), but often has much lower variance and so is often faster (p. 207).
- Choosing features is an important way of adding prior domain knowledge. Linear form cannot capture feature interactions unless interaction features are added (p. 210).
- In coarse coding (overlapping receptive fields, the regions where features are on) and tile coding, the size and shape of the receptive fields control initial generalization, while acuity (the finest discrimination possible) is controlled more by the number of features (p. 216). Tile coding gives a constant number of active features, so $\alpha$ is easy to set (pp. 217–218).

## L3 — Walkthrough

### Chapter introduction (p. 197)
The approximate value is $\hat v(s,\mathbf w)\approx v_\pi(s)$ with weight vector $\mathbf w\in\mathbb R^d$. $\hat v$ may be linear in features, a neural network, or a decision tree. Typically $d\ll|\mathcal S|$, so changing one weight changes the values of many states (p. 197). The author calls this generalization potentially more powerful but harder to manage and understand.

Function approximation also covers partially observable problems. If $\hat v$ cannot depend on some aspect of the state, that aspect is as if unobservable. It cannot add memories of past observations (p. 197).

### 9.1 Value-function approximation
An update is written $s\mapsto u$: $s$ is the state updated, $u$ the update target (p. 198). The targets are:
- Monte Carlo: $S_t\mapsto G_t$.
- TD(0): $S_t\mapsto R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)$.
- $n$-step TD: $S_t\mapsto G_{t:t+n}$.
- DP: $s\mapsto\mathbb E_\pi[R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)\mid S_t=s]$, for an arbitrary $s$.

Each update is read as an example of desired input–output behavior (p. 198). In the tabular case an update shifted one entry toward $u$ and left all others unchanged. Now any supervised-learning ("function approximation") method may be used, passing $s\mapsto u$ as a training example. Not all such methods suit RL. Learning must be online, from incrementally acquired data. The method must also handle nonstationary targets, for example under GPI or when the targets are bootstrapped (p. 198).

> **Intuition note.** Learning a value function becomes ordinary curve fitting, but the data arrive one point at a time and the "correct answers" keep moving. So methods that need several passes over a fixed data set are less suitable.

### 9.2 The prediction objective ($\overline{\text{VE}}$)
In the tabular case no objective was needed, since values could be exactly right and were decoupled. With approximation, improving one state generally worsens others, because there are far more states than weights. So we must specify a distribution $\mu(s)\ge0$, $\sum_s\mu(s)=1$, saying how much we care about each state (p. 199). The mean square value error is

$$\overline{\text{VE}}(\mathbf w)\doteq\sum_{s\in\mathcal S}\mu(s)\big[v_\pi(s)-\hat v(s,\mathbf w)\big]^2.\tag{9.1}$$

The root $\overline{\text{VE}}$ is often plotted. Usually $\mu(s)$ is the fraction of time spent in $s$, called the on-policy distribution. In continuing tasks it is the stationary distribution under $\pi$ (p. 199).

**Episodic tasks (box, p. 199).** Let $h(s)$ be the probability that an episode starts in $s$. Let $\eta(s)$ be the average number of time steps spent in $s$ per episode. Then

$$\eta(s)=h(s)+\sum_{\bar s}\eta(\bar s)\sum_a\pi(a|\bar s)p(s|\bar s,a),\quad\text{for all }s\in\mathcal S,\tag{9.2}$$

$$\mu(s)=\frac{\eta(s)}{\sum_{s'}\eta(s')},\quad\text{for all }s\in\mathcal S.\tag{9.3}$$

This is the natural choice without discounting. With $\gamma<1$, treat discounting as a form of termination by including a factor $\gamma$ in the second term of (9.2) (p. 199).

The continuing and episodic cases must be treated separately in formal analyses (p. 200). The author says it is not completely clear that $\overline{\text{VE}}$ is the right objective. The best value function for finding a better policy is not necessarily the one minimizing $\overline{\text{VE}}$, but no better goal is yet clear (p. 200).

A global optimum $\mathbf w^*$ has $\overline{\text{VE}}(\mathbf w^*)\le\overline{\text{VE}}(\mathbf w)$ for all $\mathbf w$. This is sometimes possible for simple approximators such as linear ones, but rarely for neural networks or decision trees. Complex approximators may only reach a local optimum, meaning optimal within a neighborhood. Some methods may diverge, with $\overline{\text{VE}}\to\infty$ (p. 200). The chapter focuses on gradient methods, linear ones in particular (p. 200).

### 9.3 Stochastic-gradient and semi-gradient methods
$\mathbf w=(w_1,\dots,w_d)^\top$, and $\hat v(s,\mathbf w)$ is differentiable in $\mathbf w$ (p. 200). First assume examples $S_t\mapsto v_\pi(S_t)$ with $S_t$ drawn from $\mu$. Even with exact targets the problem is hard, since generally no $\mathbf w$ gets all states right (p. 201). SGD moves the weights a small amount in the direction that most reduces the error on the current example:

$$\mathbf w_{t+1}\doteq\mathbf w_t-\tfrac12\alpha\nabla\big[v_\pi(S_t)-\hat v(S_t,\mathbf w_t)\big]^2\tag{9.4}$$
$$=\mathbf w_t+\alpha\big[v_\pi(S_t)-\hat v(S_t,\mathbf w_t)\big]\nabla\hat v(S_t,\mathbf w_t),\tag{9.5}$$

with $\alpha>0$ and the gradient defined by

$$\nabla f(\mathbf w)\doteq\Big(\frac{\partial f(\mathbf w)}{\partial w_1},\dots,\frac{\partial f(\mathbf w)}{\partial w_d}\Big)^\top.\tag{9.6}$$

(added step) (9.4)→(9.5) uses $\nabla\tfrac12[v-\hat v]^2=-[v-\hat v]\nabla\hat v$, valid when $v_\pi(S_t)$ does not depend on $\mathbf w$ (p. 201; the independence requirement is stated on p. 202).

Why only a small step? We do not want zero error on each example. We want a balance across states. The convergence results assume $\alpha$ decreases over time. If it satisfies the standard stochastic approximation conditions (2.7), (9.5) is guaranteed to converge to a local optimum (p. 201).

**General SGD with approximate targets.** If the target $U_t$ is only an approximation to $v_\pi(S_t)$, substitute it (p. 202):

$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\big[U_t-\hat v(S_t,\mathbf w_t)\big]\nabla\hat v(S_t,\mathbf w_t).\tag{9.7}$$

If $U_t$ is unbiased, $\mathbb E[U_t|S_t=s]=v_\pi(s)$ for each $t$, then $\mathbf w_t$ is guaranteed to converge to a local optimum under (2.7). The Monte Carlo target $U_t\doteq G_t$ is unbiased, so gradient Monte Carlo is guaranteed to find a locally optimal solution (p. 202).

*Gradient Monte Carlo algorithm* (p. 202). Input: $\pi$, a differentiable $\hat v$, step size $\alpha$. Initialize $\mathbf w$ arbitrarily. For each episode, generate $S_0,A_0,R_1,\dots,S_T$ with $\pi$. For $t=0,\dots,T-1$ do $\mathbf w\leftarrow\mathbf w+\alpha[G_t-\hat v(S_t,\mathbf w)]\nabla\hat v(S_t,\mathbf w)$.

**Semi-gradient methods.** Bootstrapping targets ($G_{t:t+n}$, the DP target) depend on the current $\mathbf w_t$. They are therefore biased and do not give true gradient descent. The step (9.4)→(9.5) relies on the target being independent of $\mathbf w_t$. Bootstrapping methods account for the effect of $\mathbf w_t$ on the estimate but ignore its effect on the target. They include only part of the gradient, hence "semi-gradient" (p. 202). They converge less robustly, but reliably in important cases such as the linear case. They are often preferred because they usually learn faster, and because they learn online and continually without waiting for episode end, so they apply to continuing problems (pp. 202–203).

*Semi-gradient TD(0)* uses $U_t\doteq R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w)$, with $\hat v(\text{terminal},\cdot)=0$ (p. 203). Per step: choose $A\sim\pi(\cdot|S)$, observe $R,S'$, then
$$\mathbf w\leftarrow\mathbf w+\alpha\big[R+\gamma\hat v(S',\mathbf w)-\hat v(S,\mathbf w)\big]\nabla\hat v(S,\mathbf w),\quad S\leftarrow S'.$$

> **Intuition note.** In TD the target moves when the weights move, but the update treats the target as fixed. That is why it is not true gradient descent. Such methods still converge reliably in important cases such as the linear one, and often learn faster.

**State aggregation** groups states, with one weight per group. A state's value is its group's weight, and an update changes only that weight. It is a special case of (9.7) where $\nabla\hat v$ is 1 for the group's component and 0 elsewhere (p. 203).

**Example 9.1: 1000-state random walk** (pp. 203–204). States are $1,\dots,1000$ and episodes start at 500. Each step goes to one of the 100 neighbors on the left or one of the 100 on the right, all equally likely. Missing neighbors near an edge give termination on that side: state 1 has a 0.5 chance of terminating left, and state 950 has 0.25 of terminating right. Termination left gives reward $-1$, right gives $+1$, and all other rewards are 0. $v_\pi$ is nearly a straight line. Gradient MC used 10 groups of 100 states, 100,000 episodes and $\alpha=2\times10^{-5}$. The result is a staircase, close to the global minimum of $\overline{\text{VE}}$. About 1.37% of time steps are in the start state. The one-step neighbors get about 0.17% each, and $\mu$ falls off almost linearly to about 0.0147% at states 1 and 1000 (as printed). The leftmost groups' values are shifted above the unweighted average of true values in the group, and the rightmost groups' values are shifted below. The reason is asymmetric weighting by $\mu$. In the leftmost group, state 100 is weighted more than 3 times as strongly as state 1 (p. 204).

### 9.4 Linear methods
Each state has a feature vector $\mathbf x(s)=(x_1(s),\dots,x_d(s))^\top$, with $d$ equal to the number of weights (p. 204).

$$\hat v(s,\mathbf w)\doteq\mathbf w^\top\mathbf x(s)\doteq\sum_{i=1}^dw_ix_i(s).\tag{9.8}$$

Each $x_i:\mathcal S\to\mathbb R$ is a feature, or basis function. Choosing $d$ features means choosing $d$ basis functions (p. 205). Here $\nabla\hat v(s,\mathbf w)=\mathbf x(s)$, so (9.7) becomes $\mathbf w_{t+1}\doteq\mathbf w_t+\alpha[U_t-\hat v(S_t,\mathbf w_t)]\mathbf x(S_t)$ (p. 205).

In the linear case there is only one optimum (in degenerate cases, one set of equally good optima). So any method guaranteed to converge to or near a local optimum converges to or near the global one. Gradient MC converges to the global optimum of $\overline{\text{VE}}$ if $\alpha$ is reduced by the usual conditions. Semi-gradient TD(0) also converges in the linear case, but a separate theorem is needed. The point reached is near the local optimum, not the global optimum (p. 205).

**TD fixed point (continuing case).** With $\mathbf x_t=\mathbf x(S_t)$:

$$\mathbf w_{t+1}\doteq\mathbf w_t+\alpha\big(R_{t+1}+\gamma\mathbf w_t^\top\mathbf x_{t+1}-\mathbf w_t^\top\mathbf x_t\big)\mathbf x_t=\mathbf w_t+\alpha\big(R_{t+1}\mathbf x_t-\mathbf x_t(\mathbf x_t-\gamma\mathbf x_{t+1})^\top\mathbf w_t\big).\tag{9.9}$$

Once the system has reached steady state, for any given $\mathbf w_t$,

$$\mathbb E[\mathbf w_{t+1}|\mathbf w_t]=\mathbf w_t+\alpha(\mathbf b-\mathbf A\mathbf w_t),\tag{9.10}$$

$$\mathbf b\doteq\mathbb E[R_{t+1}\mathbf x_t]\in\mathbb R^d,\qquad\mathbf A\doteq\mathbb E\big[\mathbf x_t(\mathbf x_t-\gamma\mathbf x_{t+1})^\top\big]\in\mathbb R^{d\times d}.\tag{9.11}$$

If the system converges, it must converge to $\mathbf w_{TD}$ with $\mathbf b-\mathbf A\mathbf w_{TD}=\mathbf 0$, so $\mathbf b=\mathbf A\mathbf w_{TD}$ and

$$\mathbf w_{TD}\doteq\mathbf A^{-1}\mathbf b.\tag{9.12}$$

This is the TD fixed point, and linear semi-gradient TD(0) converges to it (p. 206).

**Proof of convergence (box, pp. 206–207).** Rewrite (9.10) as
$$\mathbb E[\mathbf w_{t+1}|\mathbf w_t]=(\mathbf I-\alpha\mathbf A)\mathbf w_t+\alpha\mathbf b.\tag{9.13}$$
Only $\mathbf A$ matters for convergence, since it multiplies $\mathbf w_t$.
- *Diagonal case.* If a diagonal element of $\mathbf A$ is negative, the matching element of $\mathbf I-\alpha\mathbf A$ exceeds one, that component is amplified, and divergence follows if this continues. If all are positive, choose $\alpha$ below one over the largest, so the diagonal of $\mathbf I-\alpha\mathbf A$ lies between 0 and 1 and $\mathbf w_t$ shrinks.
- *General case.* $\mathbf w_t$ is reduced toward zero whenever $\mathbf A$ is positive definite ($\mathbf y^\top\mathbf A\mathbf y>0$ for real $\mathbf y\ne\mathbf 0$). This also ensures $\mathbf A^{-1}$ exists.
- *Matrix form.* For linear TD(0), continuing case, $\gamma<1$:
$$\mathbf A=\sum_s\mu(s)\sum_a\pi(a|s)\sum_{r,s'}p(r,s'|s,a)\mathbf x(s)\big(\mathbf x(s)-\gamma\mathbf x(s')\big)^\top=\sum_s\mu(s)\mathbf x(s)\Big(\mathbf x(s)-\gamma\sum_{s'}p(s'|s)\mathbf x(s')\Big)^\top=\mathbf X^\top\mathbf D(\mathbf I-\gamma\mathbf P)\mathbf X.$$
Here $\mu$ is the stationary distribution under $\pi$, $\mathbf P$ is the $|\mathcal S|\times|\mathcal S|$ matrix of $p(s'|s)$ under $\pi$, $\mathbf D$ is $|\mathcal S|\times|\mathcal S|$ diagonal with $\mu(s)$, and $\mathbf X$ is $|\mathcal S|\times d$ with rows $\mathbf x(s)$. The inner matrix $\mathbf D(\mathbf I-\gamma\mathbf P)$ is key (p. 207).
- *Positive definiteness.* It is assured for this key matrix if all its columns sum to a nonnegative number (Sutton 1988). The proof uses two cited theorems. (i) A matrix $\mathbf M$ is positive definite iff $\mathbf M+\mathbf M^\top$ is. (ii) A symmetric real matrix is positive definite if its diagonal entries are positive and exceed the sum of absolute values of the off-diagonal entries in the row. Here the diagonal is positive and the off-diagonal is negative, so it only has to be shown that each row sum plus the matching column sum is positive. Row sums are positive because $\mathbf P$ is stochastic and $\gamma<1$. Column sums: with $\boldsymbol\mu=\mathbf P^\top\boldsymbol\mu$ (stationarity),
$$\mathbf 1^\top\mathbf D(\mathbf I-\gamma\mathbf P)=\boldsymbol\mu^\top(\mathbf I-\gamma\mathbf P)=\boldsymbol\mu^\top-\gamma\boldsymbol\mu^\top\mathbf P=\boldsymbol\mu^\top-\gamma\boldsymbol\mu^\top=(1-\gamma)\boldsymbol\mu^\top,$$
all components positive. So $\mathbf A$ is positive definite and on-policy TD(0) is stable. Convergence with probability one needs additional conditions and a schedule for reducing $\alpha$ (p. 207).

> **Intuition note.** The expected update is a linear iteration $\mathbf w\mapsto(\mathbf I-\alpha\mathbf A)\mathbf w+\alpha\mathbf b$. It shrinks toward a fixed point when $\mathbf A$ is positive definite. In the proof box, positive definiteness is shown using the stationary distribution of the states, which gives column sums $(1-\gamma)\boldsymbol\mu^\top$, together with positive row sums.

**Error bound.** At the TD fixed point, in the continuing case,
$$\overline{\text{VE}}(\mathbf w_{TD})\le\frac1{1-\gamma}\min_{\mathbf w}\overline{\text{VE}}(\mathbf w).\tag{9.14}$$
The asymptotic TD error is at most $1/(1-\gamma)$ times the smallest possible error, the one attained in the limit by Monte Carlo. Since $\gamma$ is often near 1, the factor can be large. But TD often has much lower variance, and so is often faster, so which is better depends on the approximation, the problem, and how long learning lasts (p. 207).

**Extensions (p. 208).** An analogous bound holds for other on-policy bootstrapping methods. Linear semi-gradient DP with on-policy updates converges to the TD fixed point. One-step semi-gradient action-value methods such as Sarsa(0) converge to an analogous fixed point and bound. Episodic tasks have a related bound (Bertsekas and Tsitsiklis, 1996). The full details, with conditions omitted here, are in Tsitsiklis and Van Roy (1997). Critical to these results is the on-policy distribution. For other update distributions, bootstrapping with function approximation may diverge to infinity (discussed in Chapter 11) (p. 208).

**Example 9.2: bootstrapping on the 1000-state walk** (pp. 208–209). With the same 10-group aggregation, semi-gradient TD(0) ends farther from the true values than Monte Carlo did (Fig. 9.2 left). For $n$-step semi-gradient TD (Fig. 9.2 right), the author switched to 20 groups of 50 states. This makes a typical transition (about 50 states) analogous to one-state transitions in the 19-state tabular walk, and the results are strikingly similar to the tabular ones (Fig. 7.2). The performance measure is the unweighted average RMS error over all states and the first 10 episodes, not $\overline{\text{VE}}$, to complete the match (p. 209). Data are averages over 100 runs (p. 208).

*$n$-step semi-gradient TD* (p. 209). The key equation, analogous to (7.2), is
$$\mathbf w_{t+n}\doteq\mathbf w_{t+n-1}+\alpha\big[G_{t:t+n}-\hat v(S_t,\mathbf w_{t+n-1})\big]\nabla\hat v(S_t,\mathbf w_{t+n-1}),\quad0\le t<T,\tag{9.15}$$
with the $n$-step return
$$G_{t:t+n}\doteq R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^n\hat v(S_{t+n},\mathbf w_{t+n-1}),\quad0\le t\le T-n.\tag{9.16}$$
The pseudocode keeps $S_t,R_t$ with indices mod $n+1$. It sets $\tau=t-n+1$, the time whose state is updated, and updates when $\tau\ge0$ using $G=\sum_{i=\tau+1}^{\min(\tau+n,T)}\gamma^{i-\tau-1}R_i$, plus $\gamma^n\hat v(S_{\tau+n},\mathbf w)$ if $\tau+n<T$.

### 9.5 Feature construction for linear methods
Linear methods can be very efficient in data and computation, depending critically on the features. Features are a way to add prior domain knowledge. They should match the aspects of the state along which generalization is appropriate (p. 210). A limitation is that linear form cannot represent interactions, such as feature $i$ being good only when $j$ is absent. In pole-balancing, high angular velocity is bad at a high angle and good at a low angle. Features coding angle and velocity separately cannot represent this, so features for combinations are needed (p. 210).

#### 9.5.1 Polynomials
For two numbers $s_1,s_2$, $\mathbf x(s)=(s_1,s_2)^\top$ allows no interactions and forces value 0 when both are zero. Using $\mathbf x(s)=(1,s_1,s_2,s_1s_2)^\top$ fixes both: the 1 allows affine functions and the product captures interaction. Higher-dimensional vectors such as $(1,s_1,s_2,s_1s_2,s_1^2,s_2^2,s_1s_2^2,s_1^2s_2,s_1^2s_2^2)^\top$ allow arbitrary quadratic functions of the state numbers, still linear in the weights (pp. 210–211). In general, for $k$ numbers, each order-$n$ polynomial-basis feature is

$$x_i(s)=\Pi_{j=1}^ks_j^{c_{i,j}},\tag{9.17}$$

with each $c_{i,j}\in\{0,1,\dots,n\}$. This gives $(n+1)^k$ features (p. 211). The count grows exponentially with $k$ (if $n>0$), so a subset must generally be selected, using prior beliefs or adapted automated selection methods (p. 211).

#### 9.5.2 Fourier basis
A Fourier series writes periodic functions as sums of sines and cosines. For an aperiodic function on a bounded interval, set $\tau$ to the interval length. If $\tau$ is twice the interval of interest, approximating on $[0,\tau/2]$ needs only cosines, because any (well-behaved) even function can be represented by cosines. Sines alone give odd functions, which are often discontinuous at the origin and harder to approximate. So cosines are generally preferred (p. 212). With $\tau=2$ the one-dimensional order-$n$ basis has $n+1$ features

$$x_i(s)=\cos(i\pi s),\quad s\in[0,1],\quad i=0,\dots,n,$$

with $x_0$ constant (Fig. 9.3, p. 212). In $k$ dimensions, $\mathbf s=(s_1,\dots,s_k)^\top$ with $s_i\in[0,1]$:

$$x_i(\mathbf s)=\cos\big(\pi\,\mathbf s^\top\mathbf c^i\big),\tag{9.18}$$

where $\mathbf c^i=(c^i_1,\dots,c^i_k)^\top$, $c^i_j\in\{0,\dots,n\}$, giving $(n+1)^k$ features. The inner product assigns an integer frequency to each dimension (pp. 212–213). A zero in $\mathbf c$ means the feature is constant along that dimension. If neither entry is zero, the feature represents an interaction. The values set the frequencies and their ratio gives the direction of the interaction (Fig. 9.4, p. 213).

A separate step size per feature may help. Konidaris et al. (2011) suggest $\alpha_i=\alpha/\sqrt{(c^i_1)^2+\cdots+(c^i_k)^2}$, except $\alpha_i=\alpha$ when all $c^i_j=0$ (p. 213).

Fourier features with Sarsa can perform well against polynomial and radial basis functions. They have trouble with discontinuities ("ringing") unless very high frequencies are included (p. 214). If $k$ is small (e.g. $k\le5$), all order-$n$ features can be used, which makes selection more or less automatic. Otherwise subsets are chosen by setting the $\mathbf c^i$ for suspected interactions and limiting entries of $\mathbf c$ to filter high-frequency noise. Fourier features are nonzero over nearly the whole space, so they represent global properties and local properties are hard to represent (p. 214). Fig. 9.5 compares the bases on the 1000-state walk using gradient MC (orders 5, 10, 20; $\alpha=0.0001$ polynomial, $0.00005$ Fourier). The Fourier curves reach lower root $\overline{\text{VE}}$, and the author does not recommend polynomials for online learning in general (p. 214).

#### 9.5.3 Coarse coding
Features are circles in a continuous 2-D space. A feature is 1 (present) if the state is inside its circle and 0 (absent) otherwise: a binary feature. Features that overlap like this give coarse coding (p. 215). Training at one state changes the weights of all circles containing it, so states sharing more circles with it are affected more (Fig. 9.6). Small circles give short-distance generalization, large circles give broad generalization, and elongated shapes give generalization elongated the same way (Fig. 9.7) (pp. 215–216). Broad features might seem to limit resolution, but they do not. Initial generalization is controlled by size and shape of the receptive fields, while acuity (the finest discrimination possible) is controlled more by the total number of features (p. 216).

**Example 9.3** (p. 216). A one-dimensional square wave was learned with (9.7), using interval-shaped features of narrow, medium and broad width. Density was about 50 features over the extent, training examples were uniform at random, and $\alpha=\frac{0.2}{n}$ with $n$ the number of features present at once. Width strongly affected early learning: broad gave broad generalization, narrow gave a bumpy function. The final function was affected only slightly (Fig. 9.8). Shape tends to affect generalization strongly but asymptotic quality little.

> **Intuition note.** Receptive field size decides how far one update spreads at first. How many features you have decides how finely you can eventually draw the function.

#### 9.5.4 Tile coding
Tile coding is coarse coding for multi-dimensional continuous spaces. The author calls it flexible and computationally efficient, and possibly the most practical representation for modern sequential digital computers (p. 217). Receptive fields form partitions called tilings, whose elements are tiles. One grid tiling is just state aggregation. For true coarse coding, use multiple tilings, each offset by a fraction of a tile width. Every state falls in exactly one tile per tiling. In the four-tiling example of Fig. 9.9, $\mathbf x(s)$ has $4\times4\times4=64$ components, of which exactly four are 1 (p. 217). Fig. 9.10 shows multiple offset tilings beating one tiling on the 1000-state walk: tiles 200 states wide, 50 tilings offset by 4 states, with initial rate $\alpha=0.0001$ for one tiling and $0.0001/50$ for 50 (p. 218).

*Practical advantages (p. 218).* The number of active features always equals the number of tilings $n$, so $\alpha$ is easy to set.
- $\alpha=1/n$ gives exact one-trial learning: after training on $s\mapsto v$, $\hat v(s,\mathbf w_{t+1})=v$.
- $\alpha=\frac1{10n}$ moves the estimate one-tenth of the way. Neighbors move less, in proportion to shared tiles.
- With binary features, (9.8) is computed by summing the $n\ll d$ weights of the active features instead of $d$ multiplications.

*Offsets (pp. 218–220).* Uniformly offset tilings give patterns with diagonal artifacts and large variation across states. Asymmetric offsets give more homogeneous, well-centered generalization (Fig. 9.11). With tile width $w$ and $n$ tilings, $w/n$ is the fundamental unit. All states within a $w/n$ square have the same features, and a move of $w/n$ changes one tile. A displacement vector $(1,1)$ means each tiling is offset from the previous by $\frac wn(1,1)$. The asymmetric tilings in Fig. 9.11 use $(1,3)$. Miller and Glanz (1996) recommend displacement vectors of the first odd integers $(1,3,5,\dots,2k-1)$, with $n$ an integer power of 2 at least $4k$. For $k=2$: $n=2^3\ge4k=8$, vector $(1,3)$. In 3-D the first four tilings are offset from a base by $(0,0,0)$, $(1,3,5)$, $(2,6,10)$, $(3,9,15)$ (p. 220).

*Tile shapes (p. 220).* The number of tilings and tile size set the resolution of the asymptotic approximation. Tile shape sets generalization. Square tiles generalize about equally in each dimension. Stripe tilings promote generalization along their long direction. Log stripes give finer discrimination where the stripes are denser. Diagonal stripes generalize along a diagonal. Irregular tilings are possible but rare (Fig. 9.12). Stripe tilings alone cannot learn a distinctive value for a conjunction of coordinates, because it bleeds into states sharing either coordinate. Mixing horizontal, vertical and conjunctive tilings gives both preferences for generalizing along each dimension and specific values for conjunctions (pp. 220–221).

*Hashing (p. 221).* Hashing is a consistent pseudo-random collapse of a large tiling into a much smaller set of tiles. Each hashed tile is a set of noncontiguous disjoint regions, and together the tiles still partition the space. Memory is often reduced by large factors with little loss, because high resolution is needed in only a small part of the space. Memory then need not grow exponentially with dimension, which frees us from the curse of dimensionality in that sense.

#### 9.5.5 Radial basis functions (start; p. 221)
RBFs generalize coarse coding to features with values anywhere in $[0,1]$, reflecting degrees of presence. A typical feature has a Gaussian response depending on the distance between state $s$ and the feature's center $c_i$, relative to its width $\sigma_i$:

$$x_i(s)\doteq\exp\!\Big(-\frac{\|s-c_i\|^2}{2\sigma_i^2}\Big).$$

The distance metric may be chosen to suit the task. Fig. 9.13 shows a one-dimensional example with a Euclidean metric. The part given here ends at this point.

## Toy example (ours, not from the text)
Two states $s_1,s_2$, one shared feature $x(s)=1$ (one weight $w$, so the two states are fully aggregated). Under $\pi$, every step goes to $s_1$ or $s_2$ with probability 0.5, so $\mu=(0.5,0.5)$. The reward on leaving $s_1$ is 0 and on leaving $s_2$ is 1. Take $\gamma=0.5$, $\alpha=0.1$.

- *Fixed point.* $A=\mathbb E[x(x-\gamma x')]=1\cdot(1-0.5\cdot1)=0.5$. $b=\mathbb E[Rx]=0.5\cdot0+0.5\cdot1=0.5$. So $w_{TD}=A^{-1}b=0.5/0.5=1$.
- *Check with the matrix form.* $\mathbf P=\begin{pmatrix}.5&.5\\.5&.5\end{pmatrix}$, so $\mathbf I-\gamma\mathbf P=\begin{pmatrix}.75&-.25\\-.25&.75\end{pmatrix}$, and $\mathbf D(\mathbf I-\gamma\mathbf P)=\begin{pmatrix}.375&-.125\\-.125&.375\end{pmatrix}$. Column sums are $0.25=(1-\gamma)\mu(s)=0.5\cdot0.5$. With $\mathbf X=(1,1)^\top$, $A=\mathbf X^\top\mathbf D(\mathbf I-\gamma\mathbf P)\mathbf X=0.375+0.375-0.125-0.125=0.5$ ✓.
- *True values.* $v_1=0.5\gamma(v_1+v_2)$, $v_2=1+0.5\gamma(v_1+v_2)$. Adding: $S=v_1+v_2=1+0.5S$, so $S=2$. Then $v_1=0.25\cdot2=0.5$ and $v_2=1.5$. The best single value under $\mu$ is $0.5(0.5)+0.5(1.5)=1$, equal to $w_{TD}$ here. At $w=1$, $\overline{\text{VE}}=0.5(0.5-1)^2+0.5(1.5-1)^2=0.25$. This special case does not show a TD/MC gap, but it satisfies (9.14).
- *Stability.* $I-\alpha A=1-0.05=0.95<1$, so the expected iteration (9.13) shrinks toward the fixed point.
- *Two updates from $w=0$.* At $s_2$ (reward 1, next $s_1$): $\delta=1+0.5\cdot0-0=1$, so $w=0+0.1\cdot1\cdot1=0.1$. At $s_1$ (reward 0, next $s_2$): $\delta=0+0.5\cdot0.1-0.1=-0.05$, so $w=0.1+0.1\cdot(-0.05)=0.095$. The expected drift from $w=0$ is $\alpha(b-Aw)=0.1\cdot0.5=0.05$, pointing toward $w=1$.

## Concepts
- [[function-approximation]] (new) — representing $v_\pi$ by $\hat v(s,\mathbf w)$ with $d\ll|\mathcal S|$ weights, so updates generalize across states (p. 197)
- [[mean-square-value-error]] (new) — $\overline{\text{VE}}(\mathbf w)=\sum_s\mu(s)[v_\pi(s)-\hat v(s,\mathbf w)]^2$ (p. 199)
- [[on-policy-distribution]] (new) — fraction of time spent in each state under $\pi$; stationary distribution in continuing tasks (p. 199)
- [[stochastic-gradient-descent]] (new) — move $\mathbf w$ a small step along the negative gradient of one example's squared error (p. 201)
- [[semi-gradient-methods]] (new) — bootstrapping updates that ignore the weights' effect on the target, so are not true gradient descent (p. 202)
- [[state-aggregation]] (new) — states grouped, one weight per group; a special case of SGD (p. 203) and of linear approximation (p. 208)
- [[linear-function-approximation]] (new) — $\hat v(s,\mathbf w)=\mathbf w^\top\mathbf x(s)$; single optimum, so local convergence implies global (p. 205)
- [[td-fixed-point]] (new) — $\mathbf w_{TD}=\mathbf A^{-1}\mathbf b$, the point linear semi-gradient TD(0) converges to (p. 206)
- [[stability]] — in the proof box, the iteration $(\mathbf I-\alpha\mathbf A)\mathbf w+\alpha\mathbf b$ is stable when $\mathbf A$ is positive definite (pp. 206–207)
- [[bootstrapping-bias-bound]] (new) — $\overline{\text{VE}}(\mathbf w_{TD})\le\frac1{1-\gamma}\min\overline{\text{VE}}$ in the continuing case (p. 207)
- [[feature-construction]] (new) — choosing basis functions for linear methods; an important way of adding prior knowledge (p. 210)
- [[coarse-coding]] (new) — overlapping receptive fields; size and shape control generalization, number of features controls acuity (pp. 215–216)
- [[tile-coding]] (new) — coarse coding by multiple offset partitions; constant number of active binary features (p. 217)
- [[temporal-difference-learning / reward prediction error]] — here used as the semi-gradient TD(0) update with target $R+\gamma\hat v(S',\mathbf w)$ (p. 203)

## Canonical instances
- [[random-walk-1000-states]] — running example for state aggregation, bootstrapping and feature comparisons (p. 203)
- [[pole-balancing-feature-interaction]] — why angle and angular velocity need interaction features in a linear value function (p. 210)

## Bridges (candidates)
- [same-math] Expected linear TD iteration $\mathbf w\mapsto(\mathbf I-\alpha\mathbf A)\mathbf w+\alpha\mathbf b$ ↔ control-theory: discrete-time linear system stability — the text shows only the diagonal case via $\mathbf I-\alpha\mathbf A$, so the eigenvalue condition is our extension.
- [structural-analogy] State aggregation ↔ control-theory: discretizing a continuous state space into cells — both treat nearby states as one.
- [structural-analogy] Fourier cosine features with per-feature step sizes ↔ control-theory: frequency-domain view (Bode plots) — both organize behavior by frequency.
- [metaphor] Receptive-field overlap and acuity ↔ sensor resolution versus the number of sensors.

## Questions this raises
- If $\overline{\text{VE}}$ is not the best objective for finding good policies, what should replace it (p. 200)?
- Why can off-policy updates make bootstrapping methods diverge, when on-policy ones are stable (p. 208, Chapter 11)?
- Can feature selection, such as the choice of tilings, be automated (p. 221)?
- How large is the practical gap between TD and Monte Carlo when $\gamma$ is near 1 and learning is long (p. 207)?

## Exercises worth doing
- Ex. 9.1 (p. 209) — show tabular methods are a special case of linear approximation, and find the features — difficulty: easy
- Ex. 9.2 (p. 211) — why (9.17) gives $(n+1)^k$ distinct features — difficulty: easy
- Ex. 9.3 (p. 211) — find $n$ and $c_{i,j}$ giving the nine-feature quadratic vector — difficulty: easy
- Ex. 9.4 (p. 221) — which tilings use prior knowledge that one dimension matters more — difficulty: medium

## Reading notes
- Printed page = pdf page − 22 (pdf 219 = printed 197). Page labels give printed numbers directly.
- This unit is part 1 of Chapter 9. It starts at the chapter opening (p. 197) and ends at the end of printed p. 221, after the opening of 9.5.5 (RBF formula and Fig. 9.13). The source notes say the split is at a section boundary; here the pages stop right after the opening of 9.5.5, and these pages do not show whether that section continues.
- The text layer garbles Greek letters and symbols. Equations were checked against the page images.
- On p. 204 the text gives about 1.37% for the start state, 0.17% for its neighbors and about 0.0147% at the extreme states. The right axis of Fig. 9.1 is labeled 0.0137 and 0.0017, which match the first two values as fractions. The extreme-state value is not marked on the axis.
- Fig. 9.3 on p. 212 shows features for $i=1,\dots,4$. In the image each panel shows only tick values ($-1$ and $1$ on the vertical axis, 0 and 1 on the horizontal axis) and no axis titles.
