---
id: recht-2019-tour/main
work: recht-2019-tour
unit: paper
pages: 1-28
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# A Tour of Reinforcement Learning: The View from Continuous Control

## L0 — One line
The survey's main view is reinforcement learning as optimal control with unknown dynamics, and on the linear quadratic regulator (LQR, a control problem with linear dynamics and quadratic cost) the author reports that simple model-based design with explicit uncertainty beats model-free methods in samples, reliability and safety.

## L1 — The gist (≤ 120 words)
Reinforcement learning (RL) is framed as optimal control when the dynamics are unknown. The survey sorts RL methods into model-based, approximate dynamic programming and direct policy search. It compares them on LQR with unknown dynamics. There, a model-based design that also estimates its own model uncertainty (Coarse-ID control) needs far fewer samples than model-free methods and gives stability guarantees. Model-free methods show high variance in the experiments. The author reports that similar patterns appear on harder simulated robot benchmarks. He closes with open problems: merging perception and control, adaptive control, and humans in the loop. The point is that safe, reliable learning systems need tools from both control and learning.

**Prerequisites:** state-space models $x_{t+1}=Ax_t+Bu_t$; expectation and gradients; least squares; the Bellman/dynamic-programming idea; eigenvalues and stability of a linear system; basic stochastic gradient descent.

## L2 — Key ideas (5–10 bullets)
- RL is posed as optimal control with unknown dynamics, solved by querying a simulator or system in episodes and judged by reward against the number of samples used; what counts as "best" is left open (pp. 2–4).
- Three solution families: model-based (fit dynamics, then plan), approximate dynamic programming (fit a Q-function, the best achievable future reward for each state-action pair), and direct policy search (optimise the policy with only reward evaluations). All reduce to function fitting from noisy data (pp. 4–11).
- Direct search via the log-likelihood trick (a sampling-based gradient estimate; REINFORCE) is easy to code, but it is derivative-free and the choice of distribution can lead to very high gradient variance. Pure random search is the same algorithm with a finite-difference reading (pp. 8–10, 14–15).
- LQR is the baseline problem. With known $A,B$, the optimal policy is linear state feedback computed through a Riccati equation (a matrix equation) (pp. 11–13).
- Coarse-ID control (learn a model, bound its error, solve a robust control problem) gives a non-asymptotic bound whose relative cost gap is $\tilde O(\sqrt{(d+p)/T})$ (here $\tilde O$ hides logarithmic factors and constants; $d$ is the state dimension, $p$ the control dimension, $T$ the trajectory length). The model-free estimate cited (for estimating a value function) is $\tilde O(\sqrt{d^2/T})$; the author says comparing worst-case upper bounds is not valid but is suggestive (pp. 13–14).
- Experiments on a double integrator and on unstable "data-center cooling" dynamics: model-based methods use far fewer samples, and robust LQR gives stabilising controllers more reliably. Model-free methods are sample-hungry and unsafe (pp. 15–18).
- On MuJoCo benchmarks (simulated robot-walking tasks), random search with linear policies and state whitening (rescaling states using their observed statistics) matches the state of the art. On these benchmarks model-free methods show alarming variance. Receding-horizon control with a learned terminal cost (a cost assigned to the last planned state) offers a middle path (pp. 18–21).
- Open challenges: end-to-end perception and control, online adaptive control (one trajectory only), and modelling humans in the loop (pp. 21–23).

## L3 — Walkthrough

### 1 Introduction (pp. 1–2)
- **Definition offered:** RL is the subfield of machine learning that studies how to use past data to enhance future manipulation of a dynamical system (p. 1). The author notes a control engineer may object that this is the scope of control theory, and that the two communities have stayed practically disjoint (p. 1).
- Opportunity: data-driven systems in self-driving vehicles, sensor networks and agile robots. Requirement: they must be safe and reliable, which is a core concern of control engineering (p. 1).
- Contrast: control designs complex actions from well-specified models; RL often makes model-free predictions from data alone (p. 2).
- Plan of the paper: RL as optimisation; solution techniques and the model-free/model-based split; the LQR case study with unknown dynamics; extension to nonlinear tasks; unification; open challenges (p. 2).
- Author's claim: on LQR, "model-free" methods popular in deep RL are considerably less effective in theory and practice than simple model-based schemes. He also says he shows cases where this continues on nonlinear problems (p. 2).

### 2 What is reinforcement learning? (pp. 2–4)
**Optimal control problem.** State $x_t$, control $u_t$, random disturbance $e_t$, reward $R_t$ (p. 2):
$$\text{maximize } \mathbb E_{e_t}\Big[\sum_{t=0}^N R_t[x_t,u_t]\Big]\quad\text{s.t. } x_{t+1}=f_t(x_t,u_t,e_t),\ x_0 \text{ given.}\tag{2.1}$$
- The expectation is over the disturbance. The control $u_t$ may use only states $x_0..x_t$ and earlier inputs $u_0..u_{t-1}$. $x_t$ is not a decision variable (pp. 2–3).
- A **trajectory** is the sequence of states and actions generated by the system:
$$\tau_t=(u_1,\dots,u_{t-1},x_0,\dots,x_t).\tag{2.2}$$
- Because the dynamics are stochastic, the controller observes the state before acting, which gives feedback. So one optimises over **policies**: a policy $\pi$ maps a trajectory to a control action (p. 3).
- Time-invariant version, with the policies $\pi_t$ as decision variables (p. 3):
$$\text{maximize } \mathbb E_{e_t}\Big[\sum_{t=0}^N R(x_t,u_t)\Big]\ \text{s.t. } x_{t+1}=f(x_t,u_t,e_t),\ u_t=\pi_t(\tau_t),\ x_0\text{ given.}\tag{2.3}$$

**Unknown dynamics.** If $f$ is unknown, standard optimisation cannot solve (2.3). One must learn about the system and then choose a policy (p. 3). Whether $R$ is known makes no difference for this survey (p. 3).

**Oracle model (episodic RL).** Choose a policy $\pi$ and horizon $L$. A simulator or real system returns a trajectory $\tau_L$ and rewards $\{R(x_t,u_t)\}$. The aim is high expected reward with few queries. $m$ queries of horizon $L$ cost $mL$, and the horizon may vary per experiment (p. 3). The author notes this oracle is more complicated than usual oracle models in optimisation, and "best" is not clearly defined: fewest samples to a reward threshold, or highest reward for a fixed budget (pp. 3–4).

**2.1 Connections to supervised learning (p. 4).** In prediction one predicts $y$ from features $x$. In RL there are two special variables, $u$ and $r$: analyse features $x$, then choose a policy that emits $u$ so $r$ is large. The key difference is that the practitioner can vary $u$, which matters for learning (designing experiments) and for control. The author says RL is clearly harder but potentially more valuable. It could help with changing distributions, gaming, adversarial behaviour and unexpected amplification, but the feedback loops are hard to study and failures can be catastrophic (p. 4). Notation: $(x,u)$ is used instead of RL's usual $(s,a)$ (p. 4, footnote).

> **Intuition note.** RL differs from ordinary prediction because the learner's own actions change what data it sees and what reward it gets. That is why the problem looks like control with an unknown plant.

### 3 Strategies for solving RL problems (pp. 4–11)
Taxonomy (pp. 4–5): **model-based** RL fits a model to data and uses it to approximate the solution of (2.3). **Model-free** RL skips the model and seeks a map from observations to actions. The latter has two branches: **policy search** and **approximate dynamic programming (ADP)**. The author states that all surveyed approaches reduce to function fitting from noisy observations (p. 5). Proponents of model-free methods argue it is often easier to find a policy than to fit a general-purpose dynamics model (p. 5).

#### 3.1 Model-based RL (pp. 5–6)
- Estimate a model (the **nominal model**), then design as if it were true ("nominal control", i.e. certainty equivalence). This is a baseline (p. 5).
- Estimation of dynamical systems is **system identification**. It differs from ordinary estimation because inputs must be chosen to excite the system's degrees of freedom, and outputs are correlated over time with parameters, inputs and noise (p. 5).
- Fit $x_{t+1}\approx\phi(x_t,u_t)$ (3.1) by least squares: $\min_\phi\sum_{t=0}^{N-1}\|x_{t+1}-\phi(x_t,u_t)\|^2$. $\phi$ may come from physics or be a neural network (p. 5).
- With the fitted $\hat\phi$ and a noise model $\omega_t$, solve: maximise $\mathbb E_{\omega}[\sum R(x_t,u_t)]$ s.t. $x_{t+1}=\hat\phi(x_t,u_t)+\omega_t$. The author says this solves the wrong problem (wrong model, assumed noise), but may work well in practice if $\hat\phi$ and $f$ are close (p. 6).

#### 3.2 Approximate dynamic programming (pp. 6–8)
- **Principle of optimality:** if $\pi_1..\pi_N$ is optimal for horizon $N$, then the optimal strategy from state $x$ at time $t$ is the tail $\pi_t..\pi_N$. Dynamic programming recurses backward from the final time (p. 6).
- **Q-function** (3.2): $\mathcal Q(x,u)=\max\{\mathbb E_{e_t}[\sum_{t=0}^N R(x_t,u_t)]: x_{t+1}=f(x_t,u_t,e_t),(x_0,u_0)=(x,u)\}$. Then the optimal value is $\max_u\mathcal Q(x_0,u)$ and the optimal policy is $\pi(x_0)=\arg\max_u\mathcal Q(x_0,u)$ (p. 6).
- Terminal $\mathcal Q_N(x,u)=R(x,u)$ and, backward in time (Bellman's equation) (p. 6):
$$\mathcal Q_k(x,u)=R(x,u)+\mathbb E_e\Big[\max_{u'}\mathcal Q_{k+1}(f(x,u,e),u')\Big].\tag{3.3}$$
The optimal $u_k=\arg\max_u\mathcal Q_k(x_k,u)$ depends only on the current state (p. 6).
- ADP estimates Q from data by assuming it is stationary, $\mathcal Q_k=\mathcal Q$, which arises for an infinite horizon. The average-reward problem (3.4) is not directly amenable to dynamic programming without technicalities, so the **discounted** problem is used (p. 7):
$$\max\ (1-\gamma)\,\mathbb E_{e_t}\Big[\sum_{t=0}^\infty\gamma^tR(x_t,u_t)\Big]\ \text{s.t. } x_{t+1}=f(x_t,u_t,e_t),\ u_t=\pi_t(\tau_t),\ \gamma\in(0,1).\tag{3.5}$$
For $\gamma$ close to 1, the discounted reward is approximately the average reward (p. 7).
- The discounted Bellman equation has the same Q on both sides: $\mathcal Q_\gamma(x,u)=R(x,u)+\gamma\mathbb E_e[\max_{u'}\mathcal Q_\gamma(f(x,u,e),u')]$. The optimal policy for all times is
$$u_t=\arg\max_u\mathcal Q_\gamma(x_t,u).\tag{3.6}$$
- **Q-learning** by stochastic approximation: along a sample trajectory, $\mathcal Q_\gamma(x_k,u_k)\approx R(x_k,u_k)+\gamma\max_{u'}\mathcal Q_\gamma(x_{k+1},u')$ (approximately, in expectation). With step size $\eta$ (p. 7):
$$\mathcal Q_\gamma^{(\text{new})}(x_k,u_k)=(1-\eta)\mathcal Q_\gamma^{(\text{old})}(x_k,u_k)+\eta\Big(R(x_k,u_k)+\gamma\max_{u'}\mathcal Q_\gamma^{(\text{old})}(x_{k+1},u')\Big).\tag{3.7}$$
- Value function $V(x)=\max_u\mathcal Q(x,u)$; temporal-difference algorithms come from the value-function view (p. 7).
- **Caveats** (pp. 7–8): "no free lunch". Choosing a parameterisation of Q is a modelling assumption. "Model-free" almost always means no model of the state-transition function when casually claimed in RL research. For continuous control these methods appear to use samples inefficiently. With state dimension $d$, model fitting (3.1) gives $d$ equations per time step, while ADP uses 1. The discount factor was introduced to get a simple Bellman equation. Large discount factors do in practice lead to brittle methods, so the discount becomes a hyperparameter to tune.

> **Intuition note.** A model fit sees the whole next state as a $d$-dimensional target, while Q-learning only sees a single scalar "target" per step. So the model uses each step's data more richly (the author's explanation of the observed sample inefficiency).

#### 3.3 Direct policy search (pp. 8–11)
Policy search turns RL into derivative-free optimisation (p. 8).

**3.3.1 Generic sampling-based optimisation (pp. 8–9).**
- $\max_{z\in\mathbb R^d}R(z)$ (3.8) is equivalent to $\max_{p(z)}\mathbb E_p[R(z)]$: a delta function at the optimum $z^\star$ gives the same value, and no distribution can beat the best fixed $z$ in expectation (p. 8).
- Restrict to a parametric family $p(z;\vartheta)$: $\max_\vartheta\mathbb E_{p(z;\vartheta)}[R(z)]$ (3.9). If the family contains all delta functions the optimum coincides; otherwise it only gives a lower bound on the optimal value (p. 8).
- **Log-likelihood trick** with $J(\vartheta)=\mathbb E_{p(z;\vartheta)}[R(z)]$ (p. 9):
$$\nabla_\vartheta J=\int R(z)\nabla_\vartheta p(z;\vartheta)dz=\int R(z)\frac{\nabla_\vartheta p}{p}\,p\,dz=\int\big(R(z)\nabla_\vartheta\log p(z;\vartheta)\big)p\,dz=\mathbb E_{p}[R(z)\nabla_\vartheta\log p(z;\vartheta)].$$
So $G(z,\vartheta)=R(z)\nabla_\vartheta\log p(z;\vartheta)$ (3.10) is an unbiased gradient estimate for samples $z\sim p(z;\vartheta)$.
- **Algorithm 1 (REINFORCE):** sample $z_k\sim p(z;\vartheta_k)$; set $\vartheta_{k+1}=\vartheta_k+\alpha_kR(z_k)\nabla_\vartheta\log p(z_k;\vartheta_k)$ (p. 9).
- Pros and cons: trivial to implement for anything you can sample. But $R$ is only accessed through function evaluations. The author states such methods are necessarily derivative-free and necessarily less effective than methods using actual gradients, especially with noisy evaluations. The distribution choice can give very high gradient variance, so many samples are needed (p. 9). Ease of implementation should not be discounted (p. 9).

**3.3.2 Policy gradient (p. 10).** Bellman's equation shows that the optimal policy for (2.3) is always deterministic, yet policy gradient uses probabilistic policies $p(u|\tau_t;\vartheta)$. Probabilistic policies are optimal for other problems (partially observed MDPs, zero-sum games). A policy induces a trajectory distribution
$$p(\tau;\vartheta)=\prod_{t=0}^{L-1}p(x_{t+1}|x_t,u_t)\,p(u_t|\tau_t;\vartheta),\tag{3.11}$$
and with $R(\tau)=\sum_{t=0}^NR_t(x_t,u_t)$ the problem takes the form (3.9). Using the log-likelihood trick and (3.11), the author says it is straightforward to verify that the gradient of $J$ is not an explicit function of the underlying dynamics (p. 10).

**3.3.3 Pure random search (pp. 10–11).** Apply Algorithm 1 with $p(z;\vartheta)=p_0(z-\vartheta)$ (e.g. uniform on a sphere or normal). Then REINFORCE is equivalent to approximate gradient ascent $\vartheta_{k+1}=\vartheta_k+\alpha g_\sigma(\vartheta_k)$ with the finite-difference estimate
$$g_\sigma(\vartheta)=\frac{R(\vartheta+\sigma\epsilon)-R(\vartheta-\sigma\epsilon)}{2\sigma}\,\epsilon,\qquad g^{(m)}_\sigma(\vartheta)=\frac1m\sum_{i=1}^m\frac{R(\vartheta+\sigma\epsilon_i)-R(\vartheta-\sigma\epsilon_i)}{2\sigma}\epsilon_i .$$
Averaging over $m$ directions reduces variance; the estimate is akin to a gradient in the random subspace spanned by the $\epsilon_i$ (pp. 10–11). History: probably first proposed by Rastrigin (the author says "probably the earliest proposal"), who developed it to solve RL problems; his motivating example was an inverted pendulum. Later analysed by Nesterov and Spokoiny, found by the evolution-strategies community, and studied in stochastic approximation and bandits (p. 11). It is simpler than policy gradient but uses less problem structure. RL problems tend to be nonconvex, so it is unclear which is better without focusing on instances (p. 11).

#### 3.4 Deep RL (p. 11)
Nothing conceptually different except neural networks for function approximation (of $\phi$, of Q/value functions, or of policies). Convergence analysis changes, and Q-learning might not even converge. The LQR case removes the complication of function approximation (p. 11).

> **Intuition note.** Whatever the method, RL is fitting an unknown function from noisy data: the dynamics, the cost-to-go, or the policy. The methods differ in which function they fit and how much problem structure they use.

### 4 The Linear Quadratic Regulator (pp. 11–15)
**Why LQR.** If a complicated method fails on a simple problem, the author says this indicates a flaw in the method. He argues LQR is the simplest non-trivial class in optimal control (p. 11):
$$\min\ \mathbb E_{e_t}\Big[\tfrac12\sum_{t=0}^N\big(x_t^TQx_t+u_t^TRu_t\big)+\tfrac12x_{N+1}^TSx_{N+1}\Big]\ \text{s.t. } x_{t+1}=Ax_t+Bu_t+e_t,\ u_t=\pi_t(\tau_t),\ x_0\text{ given.}\tag{4.1}$$
$Q,R,S$ are positive semidefinite; this is minimisation, as is conventional (p. 12). Defence of LQR (p. 12): many systems are nearly linear in their operating range, and linear dynamics are the only class guaranteeing a convex constraint set. Cost functions are at the engineer's discretion. Quadratic cost is convex, and with noise the cost equals that of the noiseless problem plus a constant independent of $u_t$. Noise degrades achievable cost but does not affect how actions are chosen.

**Solution with known $A,B$ (p. 12).** The optimal action is linear in the state, $u_t=-K_tx_t$, with $K_t$ from a linear-algebra recursion using only $(A,B,Q,R)$. As the horizon tends to infinity, the optimal policy is static linear state feedback $u_t=-Kx_t$ with
$$K=(R+B^TMB)^{-1}B^TMA,$$
$$M=Q+A^TMA-(A^TMB)(R+B^TMB)^{-1}(B^TMA)\tag{4.2}$$
(discrete algebraic Riccati equation). $M$ is the unique solution for which all eigenvalues of $A-BK$ have magnitude less than 1. Via dynamic programming the finite-horizon Q-function satisfies $\mathcal Q_k(x,u)=x^TQx+u^TRu+(Ax+Bu)^TM_{k+1}(Ax+Bu)+c_k$ for some positive definite $M_{k+1}$. The limit of these matrices solves (4.2) (pp. 12–13).

The author says LQR lacks some generality but has salient features of the generic problem: efficient dynamic programming, and a nearly optimal static policy for long horizons (p. 13).

**4.1 Sample complexity of model-based RL for LQR (pp. 13–14).**
- Maximum-likelihood nominal model: $\min_{A,B}\sum_{t=0}^{N-1}\|x_{t+1}-Ax_t-Bu_t\|^2$ (p. 13).
- Danger: if the true $A$ has an eigenvalue of magnitude above 1, the least-squares estimate of that mode may be below 1, and the optimal control for the estimate will not account for the unstable mode (p. 13).
- **Coarse-ID control** (three steps, p. 13): (1) learn a coarse model (the nominal system) by supervised learning; (2) with prior knowledge or tools such as the bootstrap, build probabilistic guarantees on the distance between nominal and true dynamics; (3) solve a robust optimisation problem that optimises the nominal system while penalising signals according to the estimated uncertainty. As long as the true system lies in the uncertainty set, a performant controller is guaranteed. Machine learning identifies the plant and its uncertainty (p. 13).
- For LQR: the accuracy of least-squares estimates of $A,B$ is guaranteed by recent probabilistic analysis. The robust LQR minimises worst-case performance given high-probability norm bounds on the model errors. It is solved with System Level Synthesis (SLS), which lifts the system description to a higher-dimensional space for efficient controller search (p. 14).
- **Result** (state dimension $d$, control dimension $p$, optimal cost $J_\star$, trajectory length $T$): the designed controller has infinite-horizon cost $\hat J$ with
$$\frac{\hat J-J_\star}{J_\star}=\tilde O\Big(\sqrt{\tfrac{d+p}{T}}\Big),$$
where $\tilde O$ hides logarithmic factors and instance-dependent constants. In particular the system is stabilised after a finite amount of data (p. 14). The approach avoids studying perturbations of Riccati equations and, being optimisation-based, can be applied beyond LQR (p. 14).

> **Intuition note.** Coarse-ID control treats the fitted model as "roughly right within a known error". It then designs for the worst case inside that error. The guarantee is only as good as the claim that the true system lies inside the estimated set.

**4.2 Sample complexity of model-free RL for LQR (pp. 14–15).**
- Q for LQR is quadratic, so it can be estimated by dynamic programming, first proposed (probably) by Bradtke, Barto and Ydstie. Tu showed that Least-Squares Temporal Differencing estimates the LQR value function to low error with $\tilde O\big(\sqrt{d^2/T}\big)$ samples; the estimator can then be combined with policy improvement (p. 14).
- The author says this bound is worse than the error obtained for estimating the dynamical-system model (he gives no explicit rate for that error here). The author says comparing worst-case upper bounds is certainly not valid but is suggestive, in line with one equation per step (TD) versus $d$ per step (model estimation). Conventional wisdom says estimating Q-functions for specific tasks should be simpler than estimating models, but current methods appear less efficient with aggregated data than system identification (p. 14).
- **Direct search variance, trivial LQR** $R(u)=\|u\|^2$ with $p(u;\vartheta)=\mathcal N(\vartheta,\sigma^2I)$. Then $\mathbb E[R(u)]=\|\vartheta\|^2+\sigma^2d$. Best is $\vartheta=0$ (off by $\sigma^2d$); the cost is strongly convex in $\vartheta$ (pp. 14–15). By (3.10) the first gradient is, as printed,
$$g=-\frac{\|\omega-\vartheta_0\|^2\,\omega}{\sigma^2},\quad \omega\sim\mathcal N(0,\sigma^2I),$$
with expected norm of order $O\big(\sigma d^{1.5}+\sigma^{-1}d^{0.5}\|\vartheta_0\|\big)$, a significant scaling with dimension (p. 15).
- Known complexity results for this method depend strongly on dimension and on the largest reward magnitude $B$ (p. 15). As printed: with noisy function values and convex objective, rate $O((d^2B^2/T)^{-1/3})$, assuming parameters exactly right. For strongly convex functions, $O((d^2B^2/T)^{-1/2})$ function evaluations, also fragile to parameters. Shifting all rewards from $[0,1]$ by subtracting one million slows the algorithm by a factor of a million, though the reward ordering is unchanged (p. 15).

### 5 Numerical comparisons (pp. 15–18)
Author's summary of the theory: model-based (learning plus robust control) achieves nearly optimal performance for its budget. ADP seems worse in worst case. Direct policy search seems too high-variance to work in practice (p. 15).

**5.1 Double integrator (pp. 15–16).** Position and velocity of a unit mass under force $u$:
$$x_{t+1}=\begin{bmatrix}1&1\\0&1\end{bmatrix}x_t+\begin{bmatrix}0\\1\end{bmatrix}u_t\tag{5.1}$$
$$Q=\begin{bmatrix}1&0\\0&0\end{bmatrix},\ R=r_0,\ x_0=[-1,0].\tag{5.2}$$
- Setup: noise $e_t$ zero mean with covariance $10^{-4}I$; training episode length $L=10$; goal is a controller for an arbitrarily long horizon with the fewest simulations of length $L$ (p. 16).
- Nominal control: with one simulation (10 samples) using unit-variance white-noise input, the nominal estimate is correct to 3 digits and gives a nearly optimal policy. The least-squares estimator discards sparsity information; realistically only the (2,1) entry of $B$ (force/mass) would need estimating (p. 16).
- Policy search restricted to static linear gains (two decision variables). Policy gradient used Adam and mean-reward baseline subtraction; the author could not make it converge without these. LSPI (Least Squares Policy Iteration) was the ADP method. 10 random seeds (p. 16).
- Result: nominal control and LSPI find high-quality controllers with only ten observations. Direct policy methods need many times as many samples. Policy gradient needs thousands of times as many as nominal control (p. 16). Figure 1 (read from image): random search reaches near-optimal median cost at roughly 5,000 samples; policy gradient median is near optimal only by about 20,000–30,000, with a wide min–max band (p. 16).

**5.2 Unstable Laplacian dynamics (pp. 17–18).** Idealised data-centre cooling: three heat sources, each coupled to its own cooling device. The state is the temperatures; they heat under a constant load and shed heat to neighbours (p. 17):
$$A=\begin{bmatrix}1.01&0.01&0\\0.01&1.01&0.01\\0&0.01&1.01\end{bmatrix},\quad B=I,\quad Q=I,\ R=1000I.$$
- The open-loop system is unstable. If a method estimates a diagonal entry of $A$ below 1, it may put less effort into cooling that source. Large $R$ models a high cost of power. Whether a policy is safe must be ascertainable (p. 17).
- Robust LQR is a small semidefinite program (Dean et al.), solved on a laptop in under a second. Two versions: given the true model-error distance (blue), and estimating it by bootstrap (green). The bootstrap version has only slightly worse LQR performance than knowing the error exactly (p. 17).
- Stability: the author says a necessary and sufficient condition for stabilisation is that $A+BK$ has all eigenvalues of magnitude below 1. Nominal control often finds controllers that fail to stabilise the true system. Robust optimisation provides controllers guaranteed to stabilise. Yet in industrial practice nominal control seems to work well, and finding reasonable assumptions under which nominal control stabilises is a great open problem (p. 18). Figure 2 (right) shows the robust methods reaching a stable fraction near 1 by roughly 100 samples, while nominal reaches about 0.9 at 600 (p. 17).
- Model-free comparison (Figure 3, x-axis ×10, to 5,000 samples): model-free methods are far from model-based. LSPI, good on the double integrator, now does worse than random search, likely because its subroutine needs a stabilising controller at all iterations and careful discount tuning (p. 18). Author's conclusion: model-free methods are sample hungry and fail to be safe, and "safety is much more critical than sample complexity" (p. 18).

> **Intuition note.** Sample counts are only half the story: a controller that is cheap to learn but sometimes destabilises the plant is unusable. The robust design pays a little cost to turn "probably fine" into a guarantee.

### 6 Beyond LQR (pp. 18–21)
**6.1 Derivative-free methods for optimal control (pp. 18–19).**
- Benchmark: OpenAI-maintained MuJoCo tasks, where a simulated legged robot should walk far and fast; the hardest humanoid has 22 degrees of freedom. The dynamics follow Lagrange's equations, but planning is hard: the objective is hard to design and the model is piecewise linear (contacts add normal forces) (pp. 18–19).
- History: Levine and Koltun among first to use MuJoCo as a learning testbed. Salimans et al. showed random search fitting neural network controllers worked well. Rajeswaran et al. showed Natural Policy Gradient learns linear policies that complete the benchmarks (p. 19).
- The author, Guy and Mania tested simple random search on linear controllers. With the same **state whitening** many RL papers used, it got state-of-the-art results on all MuJoCo tasks (p. 19).
- Takeaways (p. 19): (i) these demos are easy, or easier than believed. A few benchmarks encourage overfitting, and they seem to exploit MuJoCo's approximations more than learn reasonable walking. LQR is attractive because new instances are easy to specify and the limits of performance are relatively easy to understand. (ii) Since random search is fast, many seeds can be run. On these benchmarks, all model-free methods show alarmingly high variance. On the humanoid, training is slow almost a quarter of the time (Figure 4, middle: 100 runs, high rewards achieved but poor performance more common from random initialisation), with peculiar gaits. The author says results on linear controllers suggest such variability will be a symptom of all model-free methods.

**6.2 Receding horizon control (pp. 20–21).**
- **RHC/MPC:** plan by simulation over a short horizon, execute one step, observe, replan. The feedback loop corrects model mismatch, noise and unexpected errors (p. 20).
- Link to ADP: unrolling the discounted problem (3.5) for $N$ steps gives an equivalent problem with terminal term $\gamma^N\mathcal Q_\gamma$ (as printed on p. 20): maximise $(1-\gamma)\mathbb E[\sum_{t=0}^{N-1}\gamma^tR(x_t,u_t)+\gamma^N\mathcal Q_\gamma(x_{N+1},u_{T+1})]$ s.t. $x_{t+1}=f(x_t,u_t,e_t)$. The longer the horizon, the less accurate the Q-function needs to be, but the more the accuracy of $f$ matters. The author says it is not obvious which accuracy matters more, and the trade-off between learning models and value functions needs better understanding (p. 20).
- MuJoCo tasks were designed to test a nonlinear RHC algorithm (Tassa, Erez, Todorov), which keeps the robot upright even with a poorly specified model. Humanoid control ran at 7× real time in 2012, and a cruder 2013 version was used in the DARPA Robotics Challenge. Gaits look better than typical RL gaits (pp. 20–21).
- A middle ground: a better Q-model allows a shorter horizon, nearer real time. With a perfect Q-model one could just solve the Bellman equation (p. 21).
- **Learning MPC** (Rosolia, Carvalho, Borrelli): terminal cost of a state = value obtained the last time that state was visited; infinite if unvisited. The terminal state must be one already seen, so new ways to lower cost can be explored while staying able to reach a demonstrated-safe state. In RC car demos the learned controller beat a human operator after a few laps (p. 21).
- Constraints on controls and states, and disturbance models, can be hard coded. The author suggests merging Coarse-ID robust learning with RHC as future work (p. 21).

### 7 Challenges at the control–learning interface (pp. 21–23)
Summary of findings (p. 21): for continuous control, machine learning seems best suited to model fitting rather than direct control. Learned models and control can be merged by accounting for model uncertainty. Value functions and models can be learned together.

**7.1 Merging perception and control (pp. 21–22).** End-to-end control from pixels meets old intractability issues of nonlinear output feedback and partially observed MDPs. Early RL results from pixels exist, with worse sample complexity than from states (pp. 21–22). The author thinks the most promising approaches follow Guided Policy Search, which bootstraps state feedback to produce training data for a sensor-to-action map, reducing reliance on a precise state estimator over time. He says partial observation makes control exponentially harder, and safe use of diverse sensors is an active challenge (p. 22).

**7.2 Rethinking adaptive control (p. 22).** The survey was about episodic RL (endless simulator access). In adaptive control you get one trajectory and must learn the policy online. For LQR the best approach is not settled. Eighties work had only asymptotic guarantees. Abbasi-Yadkori and Szepesvari (bandit techniques) achieve an optimal reward (per the author) but need a hard nonconvex subproblem. Follow-ups use Thompson sampling, ADP, and coarse-ID control, but none is both efficiently implementable and optimal in cost (p. 22).

**7.3 Humans in the loop (pp. 22–23).** One popular approach is game-theoretic: humans are modelled as solving their own optimal control problem, and their actions enter as a disturbance. If the cost is known this gives a game-theoretic receding horizon control. Since humans are bad at specifying objectives, their objectives must be learned: inverse optimal control / inverse RL (pp. 22–23).

**7.4 Towards actionable intelligence (p. 23).** Author's opinion: all the daunting problems in machine learning are now RL problems. As soon as a learning system is in feedback with humans, it is an RL system. He proposes the name "actionable intelligence" for the intersection and urges the engineering community to take responsibility (p. 23).

## Toy example (ours, not from the text)
Scalar deterministic system $x_{t+1}=a x_t+u_t$ (so $b=1$), start $x_0=1$. True $a=1.01$ (unstable, like the Laplacian example's diagonal 1.01).

1. Suppose data give the estimate $\hat a=0.99$ with a known error bound $|a-\hat a|\le 0.04$, so $a\in[0.95,1.03]$.
2. **Nominal control:** treat $\hat a=0.99$ as true. It looks stable, so choose $K=0$ ($u_t=0$). On the true system $x_{10}=1.01^{10}$. Compute: $1.01^2=1.0201$, $1.01^4=1.0406$, $1.01^8=1.0829$, $1.01^{10}=1.0829\times1.0201=1.1046$. The state grows without bound as $t\to\infty$ because $1.01>1$.
3. **Robust design:** choose $K=0.05$ ($u_t=-0.05x_t$), so the closed loop is $a-0.05$. Over the whole interval, $a-0.05\in[0.90,0.98]$, all below 1 in magnitude. So it is stable for every system in the uncertainty set.
4. On the true $a=1.01$: closed loop $0.96$. $0.96^2=0.9216$, $0.96^4=0.8493$, $0.96^8=0.7214$, $0.96^{10}=0.7214\times0.9216=0.6648$. So $x_{10}\approx0.665$, versus $1.105$ for nominal control. The worst case $a=1.03$ gives $0.98^{10}\approx0.817$ (since $0.98^2=0.9604$, $0.98^4=0.9224$, $0.98^8=0.8508$, $0.98^{10}=0.8508\times0.9604=0.8171$).
5. The price is some extra control effort. This is the Coarse-ID idea of (model + error bound + robust design), p. 13.

Extra mini-check of update (3.7): take $\eta=0.5$, $\gamma=0.9$, $\mathcal Q^{\text{old}}(x_k,u_k)=0$, $R=1$, $\max_{u'}\mathcal Q^{\text{old}}(x_{k+1},u')=2$. Then $\mathcal Q^{\text{new}}=(1-0.5)\cdot0+0.5\,(1+0.9\cdot2)=0.5\cdot2.8=1.4$. This uses one scalar equation per step, versus $d$ in model fitting.

## Concepts
- [[reinforcement-learning-as-optimal-control]] (new) — RL read as optimal control with unknown dynamics, judged by samples used (p. 2).
- [[episodic-rl-oracle]] (new) — query a simulator with policy and horizon $L$ to get a trajectory and rewards; cost $mL$ (p. 3).
- [[policy]] — a function from the observed trajectory to a control action; time-invariant problem optimises over policies (p. 3).
- [[model-based-vs-model-free-rl]] — fit dynamics then plan, versus map observations to actions without a dynamics model; the author says model-free still assumes structure (pp. 4–7).
- [[system-identification]] (new) — the control community's name for estimating dynamical systems; inputs must excite the system (p. 5).
- [[nominal-control]] (new) — design as if the estimated model were true (certainty equivalence) (p. 5).
- [[principle-of-optimality]] — the tail of an optimal policy is optimal from its starting state (p. 6).
- [[bellman-equation-value-function]] — recursion (3.3) for the Q-function; $V(x)=\max_u\mathcal Q(x,u)$ (pp. 6–7).
- [[q-learning]] (new) — stochastic-approximation update (3.7) of the discounted Q-function (p. 7).
- [[discount-factor]] (new) — $\gamma\in(0,1)$ in (3.5), used to get a simple Bellman equation; large $\gamma$ can make methods brittle (pp. 7–8).
- [[temporal-difference-learning-reward-prediction-error]] — value-function methods derived from the value-centred view; named but not derived here (p. 7).
- [[reinforce-log-likelihood-trick]] (new) — unbiased gradient estimate $R(z)\nabla_\vartheta\log p(z;\vartheta)$ (p. 9).
- [[policy-gradient]] (new) — REINFORCE on a probabilistic policy; the gradient is not an explicit function of the dynamics (p. 10).
- [[random-search]] (new) — REINFORCE with $p_0(z-\vartheta)$, read as finite-difference gradient ascent (p. 10).
- [[lqr]] — linear dynamics with quadratic cost; optimal policy is linear state feedback via the Riccati equation (pp. 11–12).
- [[riccati-equation]] (new) — equation (4.2) whose stabilising solution $M$ gives $K$ (p. 12).
- [[coarse-id-control]] (new) — learn a nominal model, bound its error, solve a robust control problem (p. 13).
- [[robustness]] — here, guaranteed stabilisation for every system in an estimated uncertainty set (pp. 13–14).
- [[system-level-synthesis]] (new) — framework lifting the system to a higher-dimensional space for robust controller search (p. 14).
- [[model-predictive-control]] — receding horizon control: plan short-term, execute one step, replan (p. 20).
- [[inverse-reinforcement-learning]] — estimate a human's reward function from behaviour (p. 23).
- [[markov-decision-process]] — mentioned here only via partially observed MDPs (pp. 10, 22).

## Canonical instances
- [[double-integrator-lqr]] — position/velocity of a unit mass; nominal control works from 10 samples (pp. 15–16).
- [[unstable-laplacian-data-center-lqr]] — three coupled heat sources with $A$ having 1.01 on its diagonal; shows the safety gap (pp. 17–18).
- [[trivial-lqr-random-search-variance]] — $R(u)=\|u\|^2$ with Gaussian sampling shows dimension scaling of the gradient norm (pp. 14–15).
- [[mujoco-humanoid-random-search]] — linear policies with whitening match the state of the art; high variance across seeds (pp. 19–20).
- [[learning-mpc-rc-car]] — terminal cost from previously visited states; beats a human after a few laps (p. 21).
- [[rastrigin-inverted-pendulum]] — probably the earliest random-search proposal, motivated by an RL problem (p. 11).

## Bridges (candidates)
- [same-math] Q-learning update (3.7) ↔ stochastic approximation: a step-size-weighted average of the old value and a noisy Bellman target.
- [structural-analogy] Coarse-ID control (estimate + uncertainty set + robust design) ↔ robust control: designing for the worst case within a bounded model error.
- [structural-analogy] Receding-horizon control with a terminal Q-function ↔ ADP: unrolled Bellman recursion with a learned tail value.
- [same-math] REINFORCE with $p_0(z-\vartheta)$ ↔ evolution strategies / finite-difference zeroth-order optimisation: the same perturb-and-compare update, as the text states (p. 11).
- [metaphor] Learning MPC's "only go to states already seen" ↔ safe exploration: staying within the demonstrated region.

## Questions this raises
- Under what assumptions is nominal (certainty-equivalent) control guaranteed to stabilise? The author calls it a great open problem (p. 18).
- Can an efficiently implementable adaptive controller achieve optimal cost for LQR from a single trajectory? (p. 22)
- Which accuracy matters more for RHC: model accuracy (long horizon) or Q-function accuracy (short horizon)? (p. 20)
- Do the sample-efficiency and variance gaps between model-based and model-free methods persist when function approximators are deep and the task is partially observed? (pp. 11, 21–22)

## Reading notes
- Source is arXiv:1806.09460v2 (math.OC), "June 25, 2018. Last updated: November 9, 2018," printed pages 1–28; printed = pdf page numbers. The title page gives no journal pagination. The metadata gives the journal citation, but the pages show only the arXiv version.
- No page image was supplied for printed p. 11, so eq. (4.1) is read from the text layer. There it is ambiguous whether the $\tfrac12$ covers both $x^TQx$ and $u^TRu$; I wrote it as covering both.
- Likely misprints in the source (as shown on the page images, except the p. 21 item, which is read from the text layer; I reported them as printed): (2.2) starts the inputs at $u_1$ though the text uses $u_0..u_{t-1}$; the update after the $g_\sigma$ formula (p. 10) mixes indices $t$ and $k$; the sign in $g=-\|\omega-\vartheta_0\|^2\omega/\sigma^2$ (p. 15) is not derived; the rate $O((d^2B^2/T)^{-1/3})$ (p. 15) has a negative exponent, which would grow with $T$; the stability text (p. 18) refers to "Figure 1 (right)" though the stable-fraction plots are in Figures 2 and 3, uses $A+BK$ whereas earlier $u=-Kx$ gives $A-BK$, and says "less than 1" for eigenvalues (magnitude is meant); the unrolled equation on p. 20 uses $x_{N+1},u_{T+1}$ with mixed $N$/$T$; Section 7 summary says "three" challenges but four subsections are numbered 7.1–7.4.
- The Figure 3 caption says "5000 iterations" while the axis is labelled samples. Figure readings in my notes are approximate, taken from the plots.
- The proofs of the Coarse-ID bound, SLS, and the Tu bound are cited, not given, in this paper.
