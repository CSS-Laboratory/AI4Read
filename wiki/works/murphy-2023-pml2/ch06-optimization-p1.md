---
id: murphy-2023-pml2/ch06-optimization-p1
work: murphy-2023-pml2
unit: "6 Optimization (part 1/3): 6.1 Introduction to 6.4 Natural gradient descent"
pages: 261-286
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Optimization (part 1/3): automatic differentiation, stochastic gradients, natural gradient

## L0 — One line
Gradients of complicated, possibly random objectives can be computed automatically (forward/reverse-mode AD, score-function and reparameterization estimators), and can be rescaled by the Fisher information matrix (natural gradient) so that steps are measured in distribution space rather than parameter space.

## L1 — The gist (≤ 120 words)
The chapter asks how to minimise a loss $\mathcal L(\theta)$ when the loss is a long composition of operations, or an expectation over random variables, or when parameters define a probability distribution. Section 6.2 shows how automatic differentiation computes Jacobian-vector and vector-Jacobian products, first on chains, then circuits, then programs. Section 6.3 covers stochastic gradient descent, estimators for gradients of expectations (score function, reparameterization, Gumbel-softmax, straight-through), and variance reduction. Section 6.4 introduces natural gradient descent, which preconditions with the Fisher matrix and is invariant to parameterization. These tools are used in deep learning and variational inference.

**Prerequisites:** multivariable calculus (Jacobian, chain rule, Hessian); matrix transpose; expectations and Monte Carlo averaging; KL divergence; exponential-family basics (natural vs moment parameters).

## L2 — Key ideas
- Automatic differentiation (AD) computes derivatives of compositions of basic operations. Its two essential tasks are the Jacobian-vector product (JVP) $\partial f(x)[v]$ and the vector-Jacobian product (VJP) $\partial f(x)^\top[u]$ (p. 266). The chain rule plus fan-out rules (several sub-expressions sharing one input) let AD break derivatives of chains and circuits into simpler ones (pp. 265–266, 268–269).
- Forward mode evaluates the chain rule right to left on inputs; reverse mode evaluates it on transposed Jacobians. Reverse mode is faster than forward mode when the output is scalar but stores all chain prefixes; on circuits it is precisely the backpropagation algorithm (pp. 267, 270).
- Fan-out in a circuit becomes a duplication in forward mode and a sum of VJPs in reverse mode (p. 269).
- SGD uses an unbiased gradient estimate. A sufficient convergence condition on the step sizes is given (Robbins–Monro), with common decay schedules (pp. 271–272).
- When the sampling distribution depends on $\theta$, the gradient has an extra term. The score function estimator (REINFORCE; it uses the gradient of the log sampling density) needs only a differentiable sampling distribution, not a differentiable objective, but can have high variance. The reparameterization trick (write the sample as a deterministic function of the parameters and parameter-free noise) gives a lower-variance estimator but needs an objective differentiable w.r.t. $z$ and a sampler of that form (pp. 273–275).
- Variance can be reduced by control variates (subtracting a correlated baseline), Rao-Blackwellization (enumerating a high-probability part of a discrete sum) and, for the ELBO, the "sticking the landing" estimator. For discrete variables one can often use a continuous relaxation (Gumbel-softmax), and for thresholds a surrogate backward pass (straight-through) (pp. 277–279).
- Natural gradient descent preconditions SGD by the inverse Fisher matrix. It can be viewed as a trust-region method with a Fisher (KL-based) distance, uses an always positive-definite $\mathbf F$ (the Fisher information matrix, the local quadratic form of KL), and is invariant to how the distribution is parameterized (pp. 280–282).
- For exponential-family $q$, the natural gradient w.r.t. natural parameters equals the ordinary gradient w.r.t. moment parameters. For Gaussians it needs the gradient and Hessian of the loss (pp. 284–285).

## L3 — Walkthrough

### 6.1 Introduction (p. 261)
The generic problem is $\theta^*\in\arg\min_{\theta\in\Theta}\mathcal L(\theta)$ \tag{6.1}. This hides whether the problem is constrained or not, discrete or continuous, convex or not. This chapter treats more advanced methods than the prequel (p. 261).

### 6.2 Automatic differentiation (written by Roy Frostig; p. 261)
AD computes (partial) derivatives of functions built from a composition of arbitrarily many basic operations (p. 261).

#### 6.2.1 Differentiation in functional form (pp. 261–265)
*Why the notation.* Named-variable notation ($\partial f/\partial x_1|_{x=a}$, 6.2, or $\partial f(a_1,a_2)/\partial a_1$, 6.3) depends on names that get hard to track under composition. Functional notation treats derivatives as operators on functions, with arguments identified by position (p. 262).

*Linear maps.* $F:\mathbb R^n\multimap\mathbb R^m$ denotes a linear map, applied as $F[x]$. It corresponds to a matrix in $\mathbb R^{m\times n}$ whose columns are $F[e_i]$. Composition $F\circ G$ is the matrix product $FG$. A $k$-linear map $T:\mathbb R^n\times\dots\times\mathbb R^n\to\mathbb R^m$ corresponds to an array in $\mathbb R^{m\times n\times\cdots\times n}$ (p. 262, eqs. 6.4–6.5).

*Derivative operator.* For open $U\subset\mathbb R^n$ and differentiable $f:U\to\mathbb R^m$, the derivative function is
$$\partial f:U\to(\mathbb R^n\multimap\mathbb R^m)\ \ (\equiv U\to\mathbb R^{m\times n}),\tag{6.6}$$
mapping $x$ to the Jacobian at $x$. For $m=1$ this recovers the gradient $\nabla f(x)$. For $n=m=1$ it is $f'$ (p. 263). In $\partial f(x)[v]$, $x$ is the *linearization point* and $v$ the *perturbation*. Two maps are named:
- **JVP** (Jacobian-vector product): $(x,v)\mapsto\partial f(x)[v]$ \tag{6.7}, with $v\in\mathbb R^n$ an input perturbation.
- **VJP** (vector-Jacobian product): $(x,u)\mapsto\partial f(x)^\top[u]$ \tag{6.8}, with $u\in\mathbb R^m$ an output perturbation (p. 263).

In code one often implements the whole JVP at once rather than a stored matrix. Toy case: $(x,v)\mapsto\partial\cos(x)v=-v\sin(x)$ \tag{6.9}. Written this way, $\sin(x)$ need not be computed when $v=0$ (p. 263).

*Higher order.* $\partial^2f:U\to(\mathbb R^n\multimap\mathbb R^n\multimap\mathbb R^m)$ \tag{6.10}; $\partial^2f(x)$ is a bilinear map of all second partials. It holds that $\partial^2=\partial\circ\partial$, and $\partial^kf(x)$ is $k$-linear \tag{6.11}. For $m=1$, $\partial^2 f(x)$ is the Hessian. Taylor series:
$$f(x+v)\approx f(x)+\partial f(x)[v]+\tfrac1{2!}\partial^2f(x)[v,v]+\dots+\tfrac1{k!}\partial^kf(x)[v,\dots,v]\tag{6.12}$$
(pp. 263–264).

*Multiple inputs.* For $g:U\times V\to\mathbb R^m$ with $U\subset\mathbb R^{n_1},V\subset\mathbb R^{n_2}$ \tag{6.13}, $\partial_ig$ is the derivative w.r.t. argument $i$ (6.14–6.15). The full derivative is their concatenation:
$$\partial g(x,y)[\dot x,\dot y]=\partial_1g(x,y)[\dot x]+\partial_2g(x,y)[\dot y],\tag{6.17}$$
$$\partial g(x,y)=\big(\partial_1g(x,y)\ \ \partial_2g(x,y)\big).\tag{6.18}$$
When $n_1=n_2=m=1$, $\partial_1 g$ recovers $\frac{\partial}{\partial x}g(x,y)$ (6.19). The expression $\partial_1 g$ has a meaning as a function on its own, whereas $\partial g/\partial x$ may be ambiguous. Operators compose: $\partial_2\partial_1g(x,y)\in\mathbb R^{m\times n_1\times n_2}$, and for $m=1$ the Hessian is the block matrix with entries $\partial_i\partial_jg(x,y)$ \tag{6.20} (p. 265).

*Composition and fan-out.* For $f=g\circ h$, $h:\mathbb R^n\to\mathbb R^p$, $g:\mathbb R^p\to\mathbb R^m$:
$$\partial f(x)=\partial g(h(x))\circ\partial h(x).\tag{6.21}$$
Fan-out means several sub-expressions share the same input. For $f(x)=g(a(x),b(x))$ \tag{6.22}, with $h(x)=(a(x),b(x))$:
$$\partial f(x)=\partial g(h(x))\circ\partial h(x)\tag{6.23}$$
$$=\partial_1g(a(x),b(x))\circ\partial a(x)+\partial_2g(a(x),b(x))\circ\partial b(x),\tag{6.24}$$
with $+$ meant pointwise. Without fan-out, $f(x,y)=g(a(x),b(y))$ \tag{6.25} gives
$$\partial_1f(x,y)=\partial_1g(a(x),b(y))\circ\partial a(x),\quad \partial_2f(x,y)=\partial_2g(a(x),b(y))\circ\partial b(y).\tag{6.26–6.27}$$
These rules let AD break a complex derivative into simpler ones (p. 265).

> **Intuition note.** Every derivative here is a linear map that you can apply to a vector. Chain and fan-out rules say how these maps compose. That is all AD needs.

#### 6.2.2 Differentiating chains, circuits, and programs (pp. 266–271)
AD takes $f:U\subset\mathbb R^n\to\mathbb R^m$ and a point $x$, and returns either a JVP or a VJP. Materialising a full Jacobian is a special case, using standard basis vectors (footnote 2). The set of functions allowed (the "language" of composed primitives) is perhaps the most load-bearing aspect of the setup. The author introduces AD in stages as expressiveness grows (p. 266).

**6.2.2.1 Chains.** For $f=c\circ b\circ a$ \tag{6.28}:
$$\partial f(x)=\partial c(b(a(x)))\circ\partial b(a(x))\circ\partial a(x)\tag{6.29}$$
$$\partial f(x)[v]=\partial c(b(a(x)))\big[\partial b(a(x))[\partial a(x)[v]]\big]\tag{6.30}$$
The bracketing means right-to-left evaluation, which is **forward-mode AD**. Compute the prefixes $x,\ a(x),\ b(a(x))$ (6.31) alongside the partial JVPs, because each prefix is the next linearization point (6.32) (p. 266).

*Algorithm 6.1 (forward mode on $f=f_T\circ\dots\circ f_1$).* Set $x_0,v_0:=x,v$. For $t=1..T$: $x_t:=f_t(x_{t-1})$ and $v_t:=\partial f_t(x_{t-1})[v_{t-1}]$. Output $x_T=f(x)$ and $v_T=\partial f(x)[v]$ (p. 267).

Transposing (6.29) gives
$$\partial f(x)^\top[u]=\partial a(x)^\top\big[\partial b(a(x))^\top\big[\partial c(b(a(x)))^\top[u]\big]\big].\tag{6.33}$$
Transposition reverses the order of the Jacobians. This is **reverse-mode AD**. The prefixes are computed first and then read in reverse as linearization points (6.34) (p. 267).

*Algorithm 6.2 (reverse mode).* Forward pass: $x_0:=x$, $x_t:=f_t(x_{t-1})$ for $t=1..T$. Set $u_T:=u$. Backward pass: for $t=T..1$, $u_{t-1}:=\partial f_t(x_{t-1})^\top[u_t]$. Output $x_T=f(x)$ and $u_0=\partial f(x)^\top[u]$ (p. 267).

Chains already cover multi-layer perceptrons, if matrix multiplication is a primitive. Reverse mode is faster than forward mode when the output is scalar (e.g. a loss), but it stores all chain prefixes, so it uses more memory. Memory can be reduced in special cases, e.g. when each operation is reversible, or traded for computation by recomputing discarded prefixes (pp. 267–268).

> **Intuition note.** Forward mode pushes one input direction through the network. Reverse mode pulls one output direction back through it. With a scalar output, reverse mode is faster (p. 267). (added step) One VJP with $u=1$ then gives the whole gradient.

**6.2.2.2 Circuits.** A circuit (computation graph) is a directed acyclic graph over primitive operations. Input nodes have no incoming edges and, without loss of generality, one outgoing edge. The text assumes there is exactly one sink node. New features are fan-in (a primitive with several arguments, already handled by 6.17–6.18) and fan-out (several outgoing edges), which needs care in reverse mode (p. 268).

For Figure 6.1a ($a$ feeds both $b$ and $c$, and $b$ feeds $c$), cut $a$ away to get $a$ and
$$f_{\{b,c\}}(x_1,x_2)=c(x_1,b(x_2)).\tag{6.35}$$
With $\mathrm{dup}(x)=(x,x)\equiv\binom{I}{I}x$ \tag{6.36}, we get $f=f_{\{b,c\}}\circ\mathrm{dup}\circ a$ \tag{6.37}. Then
$$\partial f(x)=\partial f_{\{b,c\}}(\mathrm{dup}(a(x)))\circ\partial\,\mathrm{dup}(a(x))\circ\partial a(x)\tag{6.38}$$
$$=\partial f_{\{b,c\}}(a(x),a(x))\circ\tbinom{I}{I}\circ\partial a(x),\tag{6.39}$$
$$\partial f(x)^\top=\partial a(x)^\top\circ\big(I\ \ I\big)\circ\partial f_{\{b,c\}}(a(x),a(x))^\top.\tag{6.40}$$
In forward mode there is a duplication; in reverse mode, a summation. Lesson: for fan-out in reverse mode, process operations in topological order forward and then backward, and **sum** partial VJPs along multiple outgoing edges (p. 269).

*Algorithm 6.3 (forward, circuits).* Nodes are $1..T$, $f_1$ is the identity. $x_1,v_1:=x,v$. For $t=2..T$, with parents $[q_1..q_r]=\mathrm{Pa}(t)$: $x_t:=f_t(x_{q_1},..,x_{q_r})$ and $v_t:=\sum_{i=1}^r\partial_if_t(x_{q_1},..,x_{q_r})[v_{q_i}]$ (p. 269).

*Algorithm 6.4 (reverse, circuits).* Same forward pass for $x_t$. Set $u_{(T-1)\to T}:=u$. For $t=T-1..2$: $u'_t:=\sum_{c\in\mathrm{Ch}(t)}u_{t\to c}$, then $u_{q_i\to t}:=\partial_if_t(x_{q_1},..,x_{q_r})^\top u'_t$ for $i=1..r$. Output $u_{1\to2}=\partial f(x)^\top u$. Conventions: $f_T$ is the identity, node $T$'s only parent is $T-1$, and node 1's child is node 2 (p. 270).

Fan-out is a feature of graphs but arguably not an essential feature of functions, since duplicating nodes removes it. The point of handling it is efficient representation and memory use. Reverse-mode AD on circuits is exactly backpropagation, and also arose in control theory and sensitivity analysis (p. 270).

**6.2.2.3 Programs.** Can AD handle functions written in Python, Haskell or lambda calculus? Loops, conditionals, recursion and parallel constructs have only partial answers so far, and this is an ongoing research topic. The author restricts "function" to pure functions (footnote 3). A `let` binding whose variable appears twice is analogous to fan-out: $f(x)=\texttt{let ax = a(x) in c(ax, b(ax))}$ is Figure 6.1a. Systems such as JAX and Dex use pure functional models (pp. 270–271).

### 6.3 Stochastic optimization (pp. 271–279)
Objectives have the form
$$\mathcal L(\theta)=\mathbb E_{q_\theta(z)}\big[\tilde{\mathcal L}(\theta,z)\big]\tag{6.41}$$
with $z$ random, e.g. external noise (p. 271).

#### 6.3.1 Stochastic gradient descent (pp. 271–273)
If $g_t$ is an unbiased estimate, $\mathbb E[g_t]=\nabla_\theta\mathcal L(\theta)|_{\theta_t}$ \tag{6.42}, then
$$\theta_{t+1}=\theta_t-\eta_tg_t\tag{6.43}$$
is SGD, with learning rate (step size) $\eta_t$ (p. 271).

*6.3.1.1 Step size.* Use a learning-rate schedule. Theoretically, a *sufficient* condition for convergence is the Robbins–Monro conditions, printed as
$$\eta_t\to0,\qquad \frac{\sum_{t=1}^\infty\eta_t^2}{\sum_{t=1}^\infty\eta_t}\to0.\tag{6.44}$$
Common schedules:
- piecewise constant: $\eta_t=\eta_i$ if $t_i\le t\le t_{i+1}$ \tag{6.45}
- exponential decay: $\eta_t=\eta_0e^{-\lambda t}$ \tag{6.46}
- polynomial decay: $\eta_t=\eta_0(\beta t+1)^{-\alpha}$ \tag{6.47}

For piecewise constant, one may set $\eta_i=\eta_0\gamma^i$ ("step decay"); Figure 6.2a uses $\eta_0=1,\gamma=0.9$. If thresholds are chosen by detecting a plateau of train/validation loss, it is "reduce-on-plateau". Exponential decay is typically too fast (Fig. 6.2b). A common choice is $\alpha=0.5,\beta=1$, the square-root schedule $\eta_t=\eta_0/\sqrt{t+1}$ (p. 272).

*6.3.1.2 Variance reduction.* SGD can be slow because the gradient is noisy; variance-reduction methods can speed convergence (details deferred to the prequel) (p. 272).

*6.3.1.3 Preconditioned SGD.* If gradient magnitudes differ greatly across dimensions (a valley with a steep and a shallow direction), scale by a conditioning matrix $C_t$:
$$\theta_{t+1}=\theta_t-\eta_tC_tg_t.\tag{6.48}$$
(pp. 272–273)

#### 6.3.2 Finite-sum objectives (p. 273)
If $q(z)$ does not depend on $\theta$, push the gradient inside the expectation and use Monte Carlo:
$$\nabla_\theta\mathcal L(\theta)=\mathbb E_{q(z)}[\nabla_\theta\tilde{\mathcal L}(\theta,z)]\approx\frac1S\sum_{s=1}^S\nabla_\theta\tilde{\mathcal L}(\theta,z_s).\tag{6.49}$$
Empirical risk minimisation (ERM) is the finite sum
$$\mathcal L(\theta)=\frac1N\sum_{n=1}^N\tilde{\mathcal L}(\theta,z_n)=\frac1N\sum_{n=1}^N\ell(y_n,f(x_n;\theta)),\tag{6.50}$$
which equals $\mathbb E_{p_{\mathcal D}(z)}[\tilde{\mathcal L}(\theta,z)]$ under the empirical distribution \tag{6.51}. A minibatch $\mathcal B$ of size $B$ gives the gradient estimate $g_t=\frac1B\sum_{n\in\mathcal B}\nabla\ell(y_n,f(x_n;\theta))$ \tag{6.52}. For large datasets this is much faster than full-batch descent (p. 273).

#### 6.3.3 Optimizing the parameters of a distribution (pp. 273–274)
If $z$ depends on $\theta$ (e.g. an action from a stochastic policy, or a latent variable from an inference network):
$$\nabla_\theta\mathbb E_{q_\theta}[\tilde{\mathcal L}]=\nabla_\theta\!\int\tilde{\mathcal L}\,q_\theta\,dz=\int\nabla_\theta[\tilde{\mathcal L}\,q_\theta]\,dz\tag{6.53}$$
$$=\int[\nabla_\theta\tilde{\mathcal L}(\theta,z)]q_\theta(z)dz+\int\tilde{\mathcal L}(\theta,z)[\nabla_\theta q_\theta(z)]dz.\tag{6.54}$$
The first line assumes swapping integration and differentiation; the second uses the product rule. The first term is $\approx\frac1S\sum_s\nabla_\theta\tilde{\mathcal L}(\theta,z_s)$ with $z_s\sim q_\theta$ \tag{6.55}. It vanishes if $\tilde{\mathcal L}$ does not depend on $\theta$. The second term
$$I\triangleq\int\tilde{\mathcal L}(\theta,z)[\nabla_\theta q_\theta(z)]dz\tag{6.56}$$
cannot be handled by vanilla Monte Carlo (p. 274).

#### 6.3.4 Score function estimator (REINFORCE) (pp. 274–275)
Log-derivative trick: $\nabla_\theta q_\theta(z)=q_\theta(z)\nabla_\theta\log q_\theta(z)$ \tag{6.57}. Hence
$$I=\int\tilde{\mathcal L}\,[q_\theta\nabla_\theta\log q_\theta]dz=\mathbb E_{q_\theta(z)}\big[\tilde{\mathcal L}(\theta,z)\nabla_\theta\log q_\theta(z)\big]\tag{6.58}$$
$$\approx\frac1S\sum_{s=1}^S\tilde{\mathcal L}(\theta,z_s)\nabla_\theta\log q_\theta(z_s),\quad z_s\sim q_\theta.\tag{6.59}$$
This is the score function estimator (SFE), also called likelihood-ratio or REINFORCE. Only the sampling distribution must be differentiable, not $\tilde{\mathcal L}$, so it suits black-box problems (variational optimization, black-box VI, RL) (p. 274).

> **Intuition note.** The estimator weights each sample's score $\nabla_\theta\log q_\theta$ by that sample's loss (our reading: a descent step then lowers the probability of high-loss samples). For the term $I$ only the sampling distribution must be differentiable, not the loss, which is why it suits black-box problems (p. 274).

*6.3.4.1 Control variates.* The SFE can have high variance. Replace $\tilde{\mathcal L}$ by
$$\hat{\tilde{\mathcal L}}(\theta,z)=\tilde{\mathcal L}(\theta,z)-c\,(b(\theta,z)-\mathbb E[b(\theta,z)])\tag{6.60}$$
where $b$ is a baseline function correlated with $\tilde{\mathcal L}$ and $c>0$. Since the expectations of $\hat{\tilde{\mathcal L}}$ and $\tilde{\mathcal L}$ are equal, the gradient estimates stay unbiased and can have lower variance (shown in Sec. 11.6.3, not in this unit) (p. 275).

*6.3.4.2 Rao-Blackwellization.* For discrete $q_\theta$, $\nabla_\theta\mathcal L=\sum_z\tilde{\mathcal L}\nabla_\theta q_\theta$, which is intractable if $z$ has exponentially many values. Partition values into a small high-probability set $S_1$ and the rest $S_2$; enumerate $S_1$ and use SFE for $S_2$:
$$\nabla_\theta\mathcal L=\sum_{z\in S_1}\tilde{\mathcal L}\nabla_\theta q_\theta(z)+\mathbb E_{q_\theta(z|z\in S_2)}\big[\tilde{\mathcal L}\nabla_\theta\log q_\theta(z)\big].\tag{6.61}$$
The second expectation can use rejection sampling from $q_\theta$. This is a form of Rao-Blackwellization (per [Liu+19b]) and reduces variance compared with standard SFE (p. 275).

#### 6.3.5 Reparameterization trick (p. 275)
Requirements: $\tilde{\mathcal L}$ differentiable w.r.t. $z$, and a sample from $q_\theta$ obtainable as $z=g(\theta,\epsilon)$ with $\epsilon\sim q_0$ independent of $\theta$ and $g$ deterministic and differentiable. Example: $z=\mu+\sigma\epsilon$, $\epsilon\sim\mathcal N(0,1)$, $\theta=(\mu,\sigma)$ \tag{6.62}. Then
$$\mathcal L(\theta)=\mathbb E_{q_\theta(z)}[\tilde{\mathcal L}(\theta,z)]=\mathbb E_{q_0(\epsilon)}[\tilde{\mathcal L}(\theta,g(\theta,\epsilon))]\tag{6.63}$$
$$\nabla_\theta\mathcal L=\mathbb E_{q_0(\epsilon)}[\nabla_\theta\tilde{\mathcal L}(\theta,g(\theta,\epsilon))]\approx\frac1S\sum_{s=1}^S\nabla_\theta\tilde{\mathcal L}(\theta,g(\theta,\epsilon_s)).\tag{6.64}$$
Names: reparameterization gradient, pathwise derivative. It is widely used in variational inference. TensorFlow Probability supports reparameterizable distributions, so one can average a loss over samples and call `jax.grad` (Listing 6.1) (p. 275–276).

*6.3.5.1 Example (p. 276).* Take $\tilde{\mathcal L}(z)=z^2-3z$, $\mathcal L(\theta)=\mathbb E_{\mathcal N(z|\mu,v)}[\tilde{\mathcal L}(z)]$, $\theta=(\mu,v)$, $v=\sigma^2$. Want $\nabla_\theta\mathcal L=[\partial_\mu\mathbb E[\tilde{\mathcal L}],\partial_v\mathbb E[\tilde{\mathcal L}]]$ \tag{6.65}. Either sample and use AD, or, for Gaussians, use Bonnet's theorem and Price's theorem (presented in Sec. 6.4.5.1):
$$\frac{\partial}{\partial\mu}\mathbb E[\tilde{\mathcal L}(z)]=\mathbb E\Big[\frac{\partial}{\partial z}\tilde{\mathcal L}(z)\Big],\qquad \frac{\partial}{\partial v}\mathbb E[\tilde{\mathcal L}(z)]=0.5\,\mathbb E\Big[\frac{\partial^2}{\partial z^2}\tilde{\mathcal L}(z)\Big].\tag{6.66–6.67}$$
A notebook shows the two methods are numerically equivalent (p. 276).

*6.3.5.2 Total derivative (p. 276–277).* In (6.64), $\tilde{\mathcal L}$ depends on $\theta$ directly and via $z(\theta)$. The total derivative is
$$\frac{\partial\tilde{\mathcal L}}{\partial\theta_i}^{\!\!\mathrm{TD}}=\frac{\partial\tilde{\mathcal L}}{\partial\theta_i}+\sum_j\frac{\partial\tilde{\mathcal L}}{\partial z_j}\frac{\partial z_j}{\partial\theta_i}\tag{6.68}$$
$$\nabla_\theta\tilde{\mathcal L}(\theta,z)^{\mathrm{TD}}=\nabla_z\tilde{\mathcal L}(\theta,z)\mathbf J+\nabla_\theta\tilde{\mathcal L}(\theta,z)\tag{6.69}$$
where $\mathbf J=\partial z^\top/\partial\theta$ is the $d_z\times d_\psi$ Jacobian of the noise transformation \tag{6.70}.

*6.3.5.3 "Sticking the landing" (STL) (p. 277).* For the ELBO with one latent sample,
$$\tilde{\mathcal L}(\theta,z)=\log p(z,x)-\log q(z|\theta)\tag{6.71}$$
and, using (6.69),
$$\nabla_\theta\tilde{\mathcal L}=\nabla_\theta[\log p(z,x)-\log q(z|\theta)]\tag{6.72}$$
$$=\underbrace{\nabla_z[\log p(z,x)-\log q(z|\theta)]\mathbf J}_{\text{path derivative}}-\underbrace{\nabla_\theta\log q(z|\theta)}_{\text{score function}}.\tag{6.73}$$
The first term is the indirect effect of $\theta$ via the samples; the second is the direct effect. The second has zero expectation (it is a score function), but with finitely many samples it may be nonzero even when $q(z|\theta)=p(z|x)$. [RWD17] propose to drop it by using $\log q(z|\theta')$ with $\theta'$ a disconnected copy:
$\epsilon\sim q_0(\epsilon)$ (6.74); $z=g(\epsilon,\theta)$ (6.75); $\theta'=\text{stop-gradient}(\theta)$ (6.76); $g=\nabla_\theta[\log p(z,x)-\log q(z|\theta')]$ (6.77).
STL is not always better than the standard estimator. [GD20] propose a weighted combination with weights optimised to reduce variance for fixed compute (p. 277).

> **Intuition note.** The score term has zero expectation, but with finitely many samples it can be non-zero even when $q$ equals the true posterior (p. 277). The aim of dropping it is that the objective should not "wobble" with Monte Carlo noise when the posterior is optimal (footnote 4).

#### 6.3.6 Gumbel-softmax trick (pp. 277–278)
For discrete variables we cannot use the reparameterization trick directly, but we can often relax them to continuous ones. A $K$-ary categorical is a one-hot $d$ ($d_k\in\{0,1\}$, $\sum_kd_k=1$) with $\pi_k=P(d_k=1)$, or $d\sim\mathrm{Cat}(d|\alpha)$ with $\pi_k=\alpha_k/\sum_{k'}\alpha_{k'}$. Sampling:
$$d=\mathrm{onehot}\big(\arg\max_k[\epsilon_k+\log\alpha_k]\big)\tag{6.78}$$
with $\epsilon_k\sim\mathrm{Gumbel}(0,1)$, drawn as $\epsilon_k=-\log(-\log u_k)$, $u_k\sim\mathrm{Unif}(0,1)$. This is the Gumbel-max trick, a reparameterizable form of the categorical. Its argmax has zero derivative except at transitions, where it is undefined. Replace argmax by softmax and $d$ by a point $x$ in the simplex $\Delta^{K-1}$:
$$x_k=\frac{\exp((\log\alpha_k+\epsilon_k)/\tau)}{\sum_{k'=1}^K\exp((\log\alpha_{k'}+\epsilon_{k'})/\tau)}\tag{6.79}$$
with temperature $\tau>0$. This is the Gumbel-softmax (concrete) distribution. It approaches the discrete distribution smoothly as $\tau\to0$ (Fig. 6.3). One can then replace $f(d)$ by $f(x)$ and take reparameterized gradients (p. 278).

#### 6.3.7 Stochastic computation graphs (p. 278)
Functions mixing deterministic and stochastic parts can be represented as stochastic computation graphs. AD can be generalised to use score-function estimation and reparameterization to get Monte Carlo gradients (details in cited works) (p. 278).

#### 6.3.8 Straight-through estimator (p. 279)
For the threshold $f(x)=1$ if $x>0$, $0$ if $x\le0$ \tag{6.80}, the gradient is not well defined. The straight-through estimator [Ben13] replaces $g(x)=f'(x)$ by $g(x)=x$ in the backward pass (Fig. 6.4). In practice $g$ is sometimes the hard tanh, $x$ on $[-1,1]$ and $\pm1$ outside \tag{6.81}, which keeps backpropagated gradients from getting too large (p. 279).

### 6.4 Natural gradient descent (pp. 279–286)
NGD is a second-order method for parameters of (conditional) distributions $p_\theta(y|x)$. Key idea: measure update size by distance between induced distributions, not between parameter values (p. 279).

*Motivation.* For Gaussians, $\|\theta-\theta'\|^2=(\mu-\mu')^2+(\sigma-\sigma')^2$ treats $\mu$ and $\sigma$ separately. But a shift $\delta$ in $\mu$ matters much more for the distribution when $\sigma$ is small (Fig. 6.5). The parameters interact, which Euclidean distance cannot capture. By modelling such correlations, NGD can converge much faster than other gradient methods (p. 280).

#### 6.4.1 Defining the natural gradient (pp. 280–281)
Use KL divergence, approximated by the Fisher information matrix (FIM) (Sec. 5.1.9):
$$D_{\mathrm{KL}}(p_\theta(y|x)\,\|\,p_{\theta+\delta}(y|x))\approx\tfrac12\delta^\top F_x\delta\tag{6.82}$$
$$F_x(\theta)=-\mathbb E_{p_\theta(y|x)}[\nabla^2\log p_\theta(y|x)]=\mathbb E_{p_\theta(y|x)}\big[(\nabla\log p_\theta)(\nabla\log p_\theta)^\top\big].\tag{6.83}$$
The average KL is $\frac12\delta^\top F\delta$ with $F(\theta)=\mathbb E_{p_{\mathcal D}(x)}[F_x(\theta)]$ \tag{6.84}. NGD preconditions with the inverse FIM:
$$\theta_{t+1}=\theta_t-\eta_tF(\theta_t)^{-1}g_t\tag{6.85}$$
and $F^{-1}g_t=F^{-1}\nabla\mathcal L(\theta_t)\triangleq\tilde\nabla\mathcal L(\theta_t)$ is the **natural gradient** \tag{6.86} (p. 281).

#### 6.4.2 Interpretations (p. 281)
*Trust region.* Gradient descent minimises the model $M_t(\delta)=\mathcal L(\theta_t)+g_t^\top\delta+\eta\|\delta\|_2^2$ \tag{6.87}, with $\theta_{t+1}=\theta_t+\delta$. Replace the squared distance by $\|\delta\|_F^2=\delta^\top F\delta$. This is Euclidean distance in the whitened coordinates $\phi=F^{1/2}\theta$:
$$\|\phi_{t+1}-\phi_t\|_2^2=\|F^{1/2}(\theta_t+\delta)-F^{1/2}\theta_t\|_2^2=\|F^{1/2}\delta\|_2^2=\|\delta\|_F^2.\tag{6.88}$$
The objective becomes $M_t(\delta)=\mathcal L(\theta_t)+g_t^\top\delta+\eta\,\delta^\top F\delta$ \tag{6.89}. Setting $\nabla_\delta M_t=0$ gives $\delta_t=-\eta F^{-1}g_t$ \tag{6.90}, the natural gradient direction (see Reading notes on the factor of $\eta$). So NGD can be viewed as a trust-region method with a first-order objective and FIM-distance. This assumed constant $F$. In general $F$ changes with position, since the space is a curved Riemannian manifold. For certain models $F$ can be computed efficiently, capturing curvature information despite the first-order objective (p. 281).

*Gauss-Newton.* If $p(y|x,\theta)$ is exponential-family with natural parameters $\eta=f(x,\theta)$, one can show [Hes00; PB14] that NGD is identical to the generalized Gauss-Newton method. In the online setting these are equivalent to sequential Bayesian inference with the extended Kalman filter [Oll18] (p. 281).

#### 6.4.3 Benefits (p. 282)
- $F$ is always positive definite; the Hessian $H$ can have negative eigenvalues at saddle points, which are prevalent in high dimensions.
- $F$ is easy to estimate online from minibatches (an expectation of outer products of gradients); Hessian methods are much more sensitive to minibatch noise.
- The trust-region view means updates change parameters in the way that matters most for prediction, allowing larger steps in uninformative regions, which can help avoid plateaus and with correlated parameters.

*Example (from [SD12]).* A 2-d Gaussian with unit covariance and coupled mean $\big(3\theta_1+\tfrac13\theta_2,\ \tfrac13\theta_1\big)$:
$$p(x;\theta)=\frac1{2\pi}\exp\Big[-\tfrac12\big(x_1-[3\theta_1+\tfrac13\theta_2]\big)^2-\tfrac12\big(x_2-[\tfrac13\theta_1]\big)^2\Big]\tag{6.91}$$
with cross-entropy loss $\mathcal L(\theta)=-\mathbb E_{p^*(x)}[\log p(x;\theta)]$ \tag{6.92} and gradient (6.93) as printed on p. 282. If $p^*(x)=p(x;[0,0])$ the Fisher matrix is constant:
$$F=\begin{pmatrix}3^2+\frac1{3^2}&1\\1&\frac1{3^2}\end{pmatrix}.\tag{6.94}$$
Both methods start at $\theta=(1,-1)$; the optimum is $(0,0)$. NG (steepest descent in $\phi$ space) converges much faster and takes the shortest path; steepest descent takes a circuitous route (Fig. 6.6). The gradient field is more "spherical" in whitened space. NGD is invariant to how the distribution is parameterised, so a standard Gaussian parameterisation would give the same results (p. 282).

#### 6.4.4 Approximating the natural gradient (pp. 282–284)
The main drawback is the cost of computing or inverting $F$. Approaches (p. 282–283):
- diagonal approximation [LeC+98]
- low-rank plus block-diagonal [RMB08]
- a low-treewidth directed Gaussian graphical model for gradient covariance, i.e. sparse Cholesky factor of $F$ [GS15]
- **KFAC** [MG15]: block-diagonal FIM of a DNN, each block a Kronecker product of two small matrices. It has shown good results in supervised learning and RL. [ZMG19] prove KFAC converges to the global optimum of an overparameterized DNN (one that acts like an interpolator).

*Empirical Fisher.* Replace the model's distribution of $(x,y)$ by the data's:
$$F=\mathbb E_{p_\theta(x,y)}[\nabla\log p\,\nabla\log p^\top]\approx\mathbb E_{p_{\mathcal D}(x,y)}[\cdots]=\frac1{|\mathcal D|}\sum_{(x,y)\in\mathcal D}\nabla\log p(y|x,\theta)\nabla\log p(y|x,\theta)^\top.\tag{6.95–6.97}$$
It is simple, and a diagonal version uses squared gradients (similar to AdaGrad, but with only the current gradient, not a moving average). It does not work as well as the true Fisher [KBH19; Tho+19]. Author's explanation: where the gradient goes to zero, the empirical Fisher becomes singular and the algorithm gets stuck. The true Fisher marginalizes out $y$, so it can detect small changes in output, which is why natural gradient can escape plateaus better (p. 284).

*Hessian-free optimization.* Compute $F$ exactly but solve for $F^{-1}g$ approximately by truncated conjugate gradient, with efficient Hessian-vector products. It can be slow, since a single update may take many CG iterations (p. 284).

#### 6.4.5 Natural gradients for the exponential family (pp. 284–286)
Assume $\mathcal L(\mu)=\mathbb E_{q_\mu(z)}[\tilde{\mathcal L}(z)]$ \tag{6.98}, with $q_\mu$ exponential-family in moment parameters $\mu$ (the basis of variational optimization and natural evolution strategies). The gradient w.r.t. $\mu$ equals the natural gradient w.r.t. natural parameters $\lambda$, by the chain rule:
$$\frac{d}{d\lambda}\mathcal L(\lambda)=\frac{d\mu}{d\lambda}\frac{d}{d\mu}\mathcal L(\mu)=F(\lambda)\nabla_\mu\mathcal L(\mu)\tag{6.99}$$
using $F(\lambda)=\nabla_\lambda\mu(\lambda)=\nabla^2_\lambda A(\lambda)$ \tag{6.100} (via Eq. 2.232, outside this unit). Hence
$$\tilde\nabla_\lambda\mathcal L(\lambda)=F(\lambda)^{-1}\nabla_\lambda\mathcal L(\lambda)=\nabla_\mu\mathcal L(\mu).\tag{6.101}$$

> **Intuition note.** In moment coordinates the Fisher "curvature" is already absorbed. So an ordinary gradient there is the natural gradient in natural-parameter coordinates. No matrix inversion is needed.

**6.4.5.1 Gaussian case, analytic (p. 285).** $q(z)=\mathcal N(z|m,V)$. Natural parameters: $\lambda^{(1)}=V^{-1}m$, $\lambda^{(2)}=-\frac12V^{-1}$ \tag{6.102}. Moment parameters: $\mu^{(1)}=m$, $\mu^{(2)}=V+mm^\top$ \tag{6.103}. Scalar case: $m=\mu^{(1)}$, $v=\mu^{(2)}-(\mu^{(1)})^2$, so by the chain rule
$$\frac{\partial\mathcal L}{\partial\mu^{(1)}}=\frac{\partial\mathcal L}{\partial m}\frac{\partial m}{\partial\mu^{(1)}}+\frac{\partial\mathcal L}{\partial v}\frac{\partial v}{\partial\mu^{(1)}}=\frac{\partial\mathcal L}{\partial m}-2\frac{\partial\mathcal L}{\partial v}m\tag{6.104}$$
$$\frac{\partial\mathcal L}{\partial\mu^{(2)}}=\frac{\partial\mathcal L}{\partial v}.\tag{6.105}$$
For $z\sim\mathcal N(m,V)$, Bonnet's theorem and Price's theorem give (as printed)
$$\frac{\partial}{\partial m_i}\mathbb E[\tilde{\mathcal L}(z)]=\mathbb E\Big[\frac{\partial}{\partial\theta_i}\tilde{\mathcal L}(z)\Big]\tag{6.106}$$
$$\frac{\partial}{\partial V_{ij}}\mathbb E[\tilde{\mathcal L}(z)]=c_{ij}\mathbb E\Big[\frac{\partial^2}{\partial\theta_i\theta_j}\tilde{\mathcal L}(z)\Big]\tag{6.107}$$
with $c_{ij}=\frac12$ if $i=j$, else $1$. Multivariate result [OA09; KR21a]:
$$\nabla_{\mu^{(1)}}\mathbb E[\tilde{\mathcal L}]=\nabla_m\mathbb E[\tilde{\mathcal L}]-2\nabla_V\mathbb E[\tilde{\mathcal L}]\,m\tag{6.108}$$
$$=\mathbb E[\nabla_z\tilde{\mathcal L}(z)]-\mathbb E[\nabla^2_z\tilde{\mathcal L}(z)]\,m\tag{6.109}$$
$$\nabla_{\mu^{(2)}}\mathbb E[\tilde{\mathcal L}]=\nabla_V\mathbb E[\tilde{\mathcal L}]=\tfrac12\mathbb E[\nabla^2_z\tilde{\mathcal L}(z)].\tag{6.110–6.111}$$
So natural gradients here need both the gradient and the Hessian of $\tilde{\mathcal L}$ (p. 285).

**6.4.5.2 General case, stochastic (p. 286).** For $\mathcal L(\mu)=\mathbb E_{q_\mu}[\tilde{\mathcal L}(z)]$ \tag{6.112}, the natural gradient is $F(\lambda)^{-1}\nabla_\lambda\mathcal L(\lambda)$ \tag{6.113}. For exponential families both factors are expectations: $F(\lambda)=\nabla_\lambda\mu(\lambda)=\nabla_\lambda\mathbb E_{q_\lambda}[\mathcal T(z)]$ \tag{6.114} and $\nabla_\lambda\mathcal L(\lambda)=\nabla_\lambda\mathbb E_{q_\lambda}[\tilde{\mathcal L}(z)]$ \tag{6.115}. Both can be approximated by Monte Carlo [KL17a]. If $q$ is reparameterizable, push the gradient inside, sample, average, and pass the stochastic gradients to SGD (p. 286).

**6.4.5.3 Natural gradient of the entropy (p. 286).** Want $\tilde\nabla_\lambda\mathbb H(\lambda)=-\nabla_\mu\mathbb E_{q_\mu}[\log q(z)]$ \tag{6.116}, with $\log q(z)=\log h(z)+\mathcal T(z)^\top\lambda-A(\lambda)$ \tag{6.117}. Using $\mathbb E[\mathcal T(z)]=\mu$:
$$\nabla_\mu\mathbb E[\log q]=\nabla_\mu\mathbb E[\log h(z)]+\nabla_\mu\mu^\top\lambda(\mu)-\nabla_\mu A(\lambda)\tag{6.118}$$
$$\nabla_\mu\mu^\top\lambda=\lambda+(\nabla_\mu\lambda)^\top\mu=\lambda+(F_\lambda^{-1}\nabla_\lambda\lambda)^\top\mu=\lambda+F_\lambda^{-1}\mu\tag{6.119}$$
$$\nabla_\mu A(\lambda)=F_\lambda^{-1}\nabla_\lambda A(\lambda)=F_\lambda^{-1}\mu\tag{6.120}$$
(the last uses $\mu=\nabla_\lambda A(\lambda)$). Hence $-\nabla_\mu\mathbb E[\log q]=-\nabla_\mu\mathbb E[\log h(z)]-\lambda$ \tag{6.121}, and if $h(z)=$ const (as is often the case), $\tilde\nabla_\lambda\mathbb H(\lambda)=-\lambda$ \tag{6.122} (p. 286).

## Toy example (ours, not from the text)
Take the book's loss $\tilde{\mathcal L}(z)=z^2-3z$ with $z\sim\mathcal N(\mu,\sigma^2)$ at $\mu=1,\sigma=1$. Exact: $\mathcal L=\mu^2+\sigma^2-3\mu$, so $\partial_\mu\mathcal L=2\mu-3=-1$ and $\partial_\sigma\mathcal L=2\sigma=2$.

Use three noise draws $\epsilon=-1,0,1$, so $z=\mu+\sigma\epsilon=0,1,2$.

*Reparameterization (6.64).* $\tilde{\mathcal L}'(z)=2z-3=-3,-1,1$.
- $\partial_\mu$: $\tilde{\mathcal L}'(z)\cdot1$, mean $(-3-1+1)/3=-1$ ✓.
- $\partial_\sigma$: $\tilde{\mathcal L}'(z)\cdot\epsilon=(-3)(-1),(-1)(0),(1)(1)=3,0,1$, mean $4/3$. Only 3 samples, so it differs from the exact $2$.

*Score function (6.59) for $\mu$.* $\nabla_\mu\log q=(z-\mu)/\sigma^2=\epsilon$. $\tilde{\mathcal L}(z)=0,-2,-2$. Products: $0\cdot(-1)=0$, $(-2)(0)=0$, $(-2)(1)=-2$; mean $-2/3$.

Both target $\partial_\mu\mathcal L=-1$. With these three draws the pathwise estimate happens to be exact and the score-function estimate is $-2/3$; this is a single illustration, not a proof of higher variance. The pathwise values $-3,-1,1$ also use $\tilde{\mathcal L}'$, which the score function never needs.

## Concepts
- [[automatic-differentiation]] (new) — computing exact derivatives of compositions of primitive operations via the chain rule (p. 261)
- [[jvp-vjp]] (new) — JVP $\partial f(x)[v]$ and VJP $\partial f(x)^\top[u]$, the two tasks of AD (p. 263)
- [[forward-reverse-mode-ad]] (new) — right-to-left JVP evaluation vs transposed, reverse VJP evaluation; reverse = backpropagation (pp. 266–270)
- [[stochastic-gradient-descent]] (new) — $\theta_{t+1}=\theta_t-\eta_tg_t$ with unbiased gradient estimate $g_t$ (p. 271)
- [[learning-rate-schedule]] (new) — step size changed over time; Robbins–Monro conditions are sufficient for convergence (p. 272)
- [[score-function-estimator]] (new) — $\mathbb E[\tilde{\mathcal L}\nabla_\theta\log q_\theta]$, via the log-derivative trick; also REINFORCE (p. 274)
- [[control-variates]] (new) — subtract a correlated baseline with known mean to lower variance (p. 274)
- [[reparameterization-trick]] (new) — write $z=g(\theta,\epsilon)$ with $\epsilon$ independent of $\theta$; pathwise gradient (p. 275)
- [[gumbel-softmax]] (new) — softmax relaxation of Gumbel-max categorical sampling, temperature $\tau$ (p. 278)
- [[straight-through-estimator]] (new) — use $g(x)=x$ (or hard tanh) as backward pass for a threshold (p. 279)
- [[natural-gradient-descent]] (new) — preconditioning by the inverse Fisher matrix; steps measured by KL (p. 281)
- [[fisher-information-matrix]] (new) — $F=\mathbb E[\nabla\log p\,\nabla\log p^\top]$, local quadratic form of KL (p. 280)
- [[empirical-fisher]] (new) — FIM with data replacing model outputs; singular where gradients vanish (p. 284)
- [[kl-divergence]] — the distance used by NGD, approximated by $\frac12\delta^\top F\delta$ (p. 280)
- [[monte-carlo-integration]] — averaging samples to approximate gradient expectations (p. 273)
- [[variational-inference-elbo]] — the ELBO as the stochastic objective in STL (p. 277)

## Canonical instances
- [[cos-jvp-example]] — $\partial\cos(x)v=-v\sin(x)$ as a whole-JVP implementation (p. 263)
- [[circuit-fan-out-dup]] — Fig. 6.1 circuit and the dup/sum trick for fan-out (pp. 268–269)
- [[gaussian-reparam-example]] — $\tilde{\mathcal L}(z)=z^2-3z$, reparameterization vs Bonnet/Price (p. 276)
- [[coupled-gaussian-ngd-example]] — 2-d Gaussian with coupled parameters, NGD vs steepest descent (pp. 282–283)
- [[gumbel-softmax-temperature-figure]] — $K=7$ states at several $\tau$ (p. 278)

## Bridges (candidates)
- [same-math] Reverse-mode AD on circuits ↔ neural networks: backpropagation — the text states they are the same algorithm (p. 270)
- [same-math] Reparameterization gradient ↔ variational inference: the pathwise ELBO gradient used in stochastic VI (p. 275)
- [structural-analogy] NGD with Fisher preconditioner ↔ Bayesian inference: the text says it is equivalent to EKF sequential inference in the online exponential-family case (p. 281)
- [structural-analogy] Control variate/baseline ↔ Monte Carlo variance reduction in estimating expectations (p. 275)
- [structural-analogy] Natural parameters vs moment parameters ↔ exponential-family duality: ordinary gradient in $\mu$ equals natural gradient in $\lambda$ (p. 284)

## Questions this raises
- When is reverse mode's memory cost the bottleneck, and how much computation does recomputing discarded prefixes cost?
- How does the variance of SFE compare with the reparameterization estimator on a concrete problem, and what does a control variate buy?
- How good are KFAC-type approximations to the Fisher matrix compared with the true Fisher, and when does the empirical Fisher fail?
- For non-Gaussian exponential families, how can natural gradients be computed when Bonnet/Price-type identities are unavailable?

## Reading notes
- This is part 1 of 3 of Chapter 6. It starts at the chapter opening (6.1, p. 261) and ends at the end of Section 6.4.5.3 (p. 286), split at a section boundary. Printed pages 261–286 correspond to pdf 295–320 (printed = pdf − 34).
- Running footer on pages: "Probabilistic Machine Learning: Advanced Topics. Online version. December 10, 2025"; Section 6.2 is written by Roy Frostig.
- Misprint/looseness (6.90): minimising (6.89) literally gives $\delta=-\frac1{2\eta}F^{-1}g$; the text writes $-\eta F^{-1}g$ (the same direction, with $\eta$ used loosely as a step size). The same applies to (6.87).
- Eq. (6.93) as printed has no leading minus sign. Differentiating the cross-entropy of (6.91) gives a minus sign in front of the bracketed expectations. I did not use the printed expression in any later step.
- Eq. (6.52) writes $g_t=\nabla\mathcal L(\theta_t)=\dots$ with an equals sign, although it is a minibatch estimate.
- In (6.106)–(6.107) the image shows $\partial/\partial\theta_i$ and $\partial^2/\partial\theta_i\theta_j$ inside the expectation, though the variable is $z$ (compare 6.66–6.67). I copied them as printed.
- (6.44) is printed as $\eta_t\to0$ and $\sum\eta_t^2/\sum\eta_t\to0$; I reproduced it as printed.
- Cross-references to Sections 3.3.4.1, 5.1.9, 10.2, 11.6, 17.3.2, 21.6, 35.3.2 and Supplementary 7.x are outside these pages.
