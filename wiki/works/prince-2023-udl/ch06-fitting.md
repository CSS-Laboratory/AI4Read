---
id: prince-2023-udl/ch06-fitting
work: prince-2023-udl
unit: Chapter 6 — Fitting models
pages: 77-95
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Fitting models

## L0 — One line
Training a model means repeatedly moving its parameters downhill on the loss surface. Random minibatches (SGD) help against local minima and saddle points, and momentum and Adam make the progress more efficient.

## L1 — The gist (≤ 120 words)
The question: given a loss $L[\boldsymbol\phi]$, how do we find parameters that minimize it? Plain gradient descent computes the gradient and steps downhill. It works on convex losses such as linear regression. Most nonlinear models, including neural networks, have non-convex losses with local minima and saddle points. Stochastic gradient descent (SGD) computes each gradient on a random minibatch. This is cheaper and adds noise that can help escape bad regions. Momentum smooths the path. Adam normalizes each parameter's step and adds momentum. The chapter also says that learning rate, batch size and momentum coefficients are hyperparameters, which are often found by trying many settings.

**Prerequisites:** partial derivatives and gradient vectors; least-squares loss; sine and exponential functions; (for the Notes) matrix eigenvalues.

## L2 — Key ideas
- Training iterates two steps: compute the gradient of the loss, then move the parameters against it by a step set by $\alpha$ (eq. 6.3) (p. 78).
- Linear regression has a convex loss with a single global minimum, so downhill walking cannot fail from any start (p. 80).
- Losses of most nonlinear models, including neural networks, are non-convex. They have local minima, and saddle points near which the surface is flat, so a small gradient does not prove convergence (pp. 80–83).
- SGD computes the gradient on a random minibatch. It is cheaper, still moves downhill on average, and can escape the wrong valley (pp. 85–86).
- A learning rate schedule explores with a high $\alpha$ early and fine-tunes with a lower $\alpha$ later (p. 86).
- Momentum averages past gradients and gives a smoother path (eq. 6.11). Nesterov momentum evaluates the gradient at the predicted point (eq. 6.12) (pp. 86–88).
- Adam divides the momentum-smoothed gradient by the root of the smoothed squared gradient, with bias correction (eqs. 6.15–6.17). This balances progress across directions and makes training less sensitive to the learning rate (pp. 88–90).
- Algorithm choices (batch size, schedule, momentum coefficients) are hyperparameters, often chosen by hyperparameter search (p. 91).

## L3 — Walkthrough
(Printed page = pdf page − 14.)

**Chapter intro (p. 77).** Networks are families of piecewise linear functions. The loss is one number measuring mismatch with the training set. Training means: choose initial parameters, then iterate (i) compute gradients of the loss, (ii) adjust parameters to reduce the loss. This chapter covers step (ii). Chapter 7 covers initialization and gradient computation (p. 77).

### 6.1 Gradient descent
Given training pairs $\{x_i,y_i\}$ and model $f[x_i,\boldsymbol\phi]$, we want
$$\hat{\boldsymbol\phi}=\operatorname*{argmin}_{\boldsymbol\phi}\big[L[\boldsymbol\phi]\big]\tag{6.1}$$
The standard methods are iterative: initialize heuristically, then adjust repeatedly so the loss decreases (p. 77).

Gradient descent starts from $\boldsymbol\phi=[\phi_0,\dots,\phi_N]^T$ and iterates (p. 78):

- Step 1 (gradient, shape $(N{+}1)\times1$): $\dfrac{\partial L}{\partial\boldsymbol\phi}=\begin{bmatrix}\partial L/\partial\phi_0\\ \vdots\\ \partial L/\partial\phi_N\end{bmatrix}$ (6.2)
- Step 2: $\boldsymbol\phi\leftarrow\boldsymbol\phi-\alpha\cdot\dfrac{\partial L}{\partial\boldsymbol\phi}$ (6.3), with positive scalar $\alpha$.

The gradient gives the uphill direction, so the minus sign moves downhill. $\alpha$ may be fixed (a *learning rate*) or chosen by *line search*, trying several values to find the one that most decreases the loss. At a minimum the surface is flat, so the gradient is zero and the parameters stop changing. In practice we stop when the gradient magnitude becomes too small (p. 78).

*Intuition note.* Gradient descent is "feel the slope, take a step down". Each step needs a direction (the negative gradient) and a step size $\alpha$.

**6.1.1 Linear regression example.** Model: $y=f[x,\boldsymbol\phi]=\phi_0+\phi_1x$ (6.4), with intercept $\phi_0$ and slope $\phi_1$. Least squares loss over $I$ pairs (p. 78):
$$L[\boldsymbol\phi]=\sum_{i=1}^I\ell_i=\sum_{i=1}^I(f[x_i,\boldsymbol\phi]-y_i)^2=\sum_{i=1}^I(\phi_0+\phi_1x_i-y_i)^2\tag{6.5}$$
The derivative is the sum of per-example derivatives (p. 80):
$$\frac{\partial L}{\partial\boldsymbol\phi}=\frac{\partial}{\partial\boldsymbol\phi}\sum_{i=1}^I\ell_i=\sum_{i=1}^I\frac{\partial\ell_i}{\partial\boldsymbol\phi}\tag{6.6}$$
$$\frac{\partial\ell_i}{\partial\boldsymbol\phi}=\begin{bmatrix}2(\phi_0+\phi_1x_i-y_i)\\ 2x_i(\phi_0+\phi_1x_i-y_i)\end{bmatrix}\tag{6.7}$$
Figure 6.1 (12 data points) uses line search for $\alpha$. After four iterations the parameters are already close to the minimum (pp. 79–80).

**6.1.2 Gabor model example.** Linear-regression losses always have a single global minimum. More formally they are *convex*: every chord (segment between two surface points) lies above the function and does not intersect it. Convexity implies that from any initialization, walking downhill reaches the minimum (p. 80). Most nonlinear models, including shallow and deep networks, have non-convex losses. To study this with only two parameters, the author uses the Gabor model (p. 80):
$$f[x,\boldsymbol\phi]=\sin[\phi_0+0.06\,\phi_1x]\cdot\exp\!\Big(-\frac{(\phi_0+0.06\,\phi_1x)^2}{32.0}\Big)\tag{6.8}$$
A sinusoid is multiplied by a decaying exponential. $\phi_0\in\mathbb R$ sets the centre position (larger $\phi_0$ moves the function left). $\phi_1\in\mathbb R^+$ squeezes it along $x$ (larger $\phi_1$ narrows it) (pp. 80–81). Training data: 28 points, $x_i$ sampled uniformly in $[-15,15]$, passed through a Gabor model with $\boldsymbol\phi=[0.0,16.6]^T$, plus normal noise (p. 81). Loss:
$$L[\boldsymbol\phi]=\sum_{i=1}^I(f[x_i,\boldsymbol\phi]-y_i)^2\tag{6.9}$$

**6.1.3 Local minima and saddle points.** Figure 6.4 shows many *local minima*: the gradient is zero and the loss rises in every direction, but they are not the overall minimum. The *global minimum* (loss 0.64) has the lowest loss. Gradient descent from a random start has no guarantee of reaching the global minimum. The author says it is equally or even more likely to end in a local minimum, and we cannot know whether a better solution exists elsewhere (pp. 81–82). Figure 6.5a: starting in the right "valley" (points 1, 3) leads to the global minimum. Starting outside it (point 2) leads to a local minimum (p. 83).

*Saddle points* have zero gradient, with the function rising in some directions and falling in others. Gradient descent can escape if the parameters are not exactly at the saddle. But the surface is flat nearby, so stopping when the gradient is small may stop erroneously near one (p. 83).

*Intuition note.* On a bowl-shaped (convex) loss, downhill always works. On a bumpy loss, where you end depends on where you start, and a tiny gradient can mean "flat but not finished".

### 6.2 Stochastic gradient descent
With two parameters we could search exhaustively or restart from many positions. With millions of parameters neither is practical. We can find *a* minimum but cannot tell whether it is global or even good (pp. 83–85). Because the destination is entirely determined by the starting point, SGD adds noise to the gradient. It still moves downhill on average, but a single step may not be steepest and may even go uphill, so it can jump between valleys (Fig. 6.5b) (p. 85).

**6.2.1 Batches and epochs.** Each iteration draws a random subset (minibatch, "batch") $\mathcal B_t$ of indices and uses only those examples (p. 85):
$$\boldsymbol\phi_{t+1}\leftarrow\boldsymbol\phi_t-\alpha\sum_{i\in\mathcal B_t}\frac{\partial\ell_i[\boldsymbol\phi_t]}{\partial\boldsymbol\phi}\tag{6.10}$$
The learning rate $\alpha$ is chosen at the start and does not depend on local properties of the function. Batches are usually drawn without replacement. One pass through the whole training set is an *epoch*. A batch can be one example or the whole dataset; the latter is full-batch gradient descent, identical to regular gradient descent. Another view: SGD does deterministic descent on a loss that changes with every batch (Fig. 6.6). The expected loss and expected gradient at any point stay the same as for gradient descent (p. 85).

**6.2.2 Properties.** Attractive features listed by the author (pp. 85–86): (1) each update still improves the fit to a subset of data, so updates tend to be sensible; (2) without-replacement sampling lets all examples contribute equally; (3) gradients on a subset are cheaper; (4) it can in principle escape local minima; (5) it reduces the chance of getting stuck near saddle points, since likely some batches have a significant gradient there; (6) there is some evidence that SGD finds parameters that generalize well (section 9.2).

SGD does not necessarily converge in the traditional sense. The hope is that near the global minimum all data points are well described, so the gradient is small for any batch and parameters stop changing much. A *learning rate schedule* starts $\alpha$ high and decreases it by a constant factor every $N$ epochs. Early on we want to explore and jump between valleys. Later we want small fine-tuning changes (p. 86).

*Intuition note.* Each batch gives a slightly different loss surface. The "wrong" downhill direction on one batch can be the step that leaves a poor valley.

### 6.3 Momentum
Momentum mixes the current batch gradient with the previous step's direction (p. 86):
$$\mathbf m_{t+1}\leftarrow\beta\,\mathbf m_t+(1-\beta)\sum_{i\in\mathcal B_t}\frac{\partial\ell_i[\boldsymbol\phi_t]}{\partial\boldsymbol\phi},\qquad \boldsymbol\phi_{t+1}\leftarrow\boldsymbol\phi_t-\alpha\,\mathbf m_{t+1}\tag{6.11}$$
with $\beta\in[0,1)$ controlling how much the gradient is smoothed over time. Recursively, the step is an infinite weighted sum of all previous gradients, with weights shrinking going back in time. The effective learning rate increases if these gradients stay aligned and decreases if the direction keeps changing so terms cancel. The result is a smoother trajectory with less oscillation in valleys (Fig. 6.7) (p. 86).

**6.3.1 Nesterov accelerated momentum.** Momentum is a coarse prediction of where SGD will go next. Nesterov momentum evaluates the gradient at the predicted point $\boldsymbol\phi_t-\alpha\beta\,\mathbf m_t$ (p. 88):
$$\mathbf m_{t+1}\leftarrow\beta\,\mathbf m_t+(1-\beta)\sum_{i\in\mathcal B_t}\frac{\partial\ell_i[\boldsymbol\phi_t-\alpha\beta\,\mathbf m_t]}{\partial\boldsymbol\phi},\qquad\boldsymbol\phi_{t+1}\leftarrow\boldsymbol\phi_t-\alpha\,\mathbf m_{t+1}\tag{6.12}$$
The gradient term then corrects the path given by momentum alone. In Fig. 6.8, ordinary momentum measures the gradient at the current point, then adds the previous direction. Nesterov applies the momentum move first, then measures the gradient (pp. 87–88).

### 6.4 Adam
Fixed-step gradient descent makes large changes where gradients are large and small changes where they are small. When the surface is much steeper in one direction than another, no single learning rate both progresses in both directions and stays stable (Fig. 6.9a–b) (p. 88).

*Normalized gradients.* Measure the gradient and its pointwise square (shape: same as $\boldsymbol\phi$):
$$\mathbf m_{t+1}\leftarrow\frac{\partial L[\boldsymbol\phi_t]}{\partial\boldsymbol\phi},\qquad\mathbf v_{t+1}\leftarrow\Big(\frac{\partial L[\boldsymbol\phi_t]}{\partial\boldsymbol\phi}\Big)^2\tag{6.13}$$
$$\boldsymbol\phi_{t+1}\leftarrow\boldsymbol\phi_t-\alpha\frac{\mathbf m_{t+1}}{\sqrt{\mathbf v_{t+1}}+\epsilon}\tag{6.14}$$
Square root and division are pointwise. $\epsilon$ is a small constant that prevents division by zero. Only the sign of each coordinate remains, so the algorithm moves a fixed distance $\alpha$ per coordinate. This progresses in both directions but will not converge unless it lands exactly on the minimum. Instead it bounces around it (Fig. 6.9c) (p. 88).

*Adam (adaptive moment estimation)* adds momentum to both statistics, with coefficients $\beta,\gamma$ (p. 90):
$$\mathbf m_{t+1}\leftarrow\beta\,\mathbf m_t+(1-\beta)\frac{\partial L[\boldsymbol\phi_t]}{\partial\boldsymbol\phi},\qquad\mathbf v_{t+1}\leftarrow\gamma\,\mathbf v_t+(1-\gamma)\Big(\frac{\partial L[\boldsymbol\phi_t]}{\partial\boldsymbol\phi}\Big)^2\tag{6.15}$$
Momentum is a weighted average over history. At the start the earlier values are effectively zero, giving unrealistically small estimates. So:
$$\tilde{\mathbf m}_{t+1}\leftarrow\frac{\mathbf m_{t+1}}{1-\beta^{t+1}},\qquad\tilde{\mathbf v}_{t+1}\leftarrow\frac{\mathbf v_{t+1}}{1-\gamma^{t+1}}\tag{6.16}$$
Since $\beta,\gamma\in[0,1)$, the denominators approach one and the correction fades. The update is
$$\boldsymbol\phi_{t+1}\leftarrow\boldsymbol\phi_t-\alpha\frac{\tilde{\mathbf m}_{t+1}}{\sqrt{\tilde{\mathbf v}_{t+1}}+\epsilon}\tag{6.17}$$
Adam can converge to the overall minimum (the author's claim) and makes good progress in every direction. It is usually used with minibatches, replacing the gradients by batch sums (p. 90):
$$\mathbf m_{t+1}\leftarrow\beta\,\mathbf m_t+(1-\beta)\sum_{i\in\mathcal B_t}\frac{\partial\ell_i[\boldsymbol\phi_t]}{\partial\boldsymbol\phi},\qquad\mathbf v_{t+1}\leftarrow\gamma\,\mathbf v_t+(1-\gamma)\Big(\sum_{i\in\mathcal B_t}\frac{\partial\ell_i[\boldsymbol\phi_t]}{\partial\boldsymbol\phi}\Big)^2\tag{6.18}$$
So the trajectory is noisy. Gradient magnitudes of network parameters can depend on depth (chapter 7). Adam helps balance changes across layers. It is also less sensitive to the initial learning rate, so it does not need complex schedules (p. 90).

*Intuition note.* Normalizing the gradient by its root squared value makes each coordinate move a fixed distance $\alpha$, whatever its raw gradient scale (p. 88). Adam adds momentum to this, which gives a smoother path (Fig. 6.9d, p. 89).

### 6.5 Training algorithm hyperparameters
Algorithm, batch size, learning rate schedule and momentum coefficients are hyperparameters of the training algorithm. They affect final performance but are distinct from model parameters. Choosing them is "more art than science", and it is common to train many models and keep the best (*hyperparameter search*; see chapter 8) (p. 91).

### 6.6 Summary (p. 91)
Gradient descent follows the gradient until convergence. For nonlinear functions the loss may have local minima and saddle points. SGD helps mitigate these problems, and each iteration is cheaper. Momentum makes convergence more efficient, and Adam was introduced. The ideas apply to any model. Chapter 7 covers backpropagation and initialization. Without careful initialization, gradients can become extremely large or small (p. 91). A footnote says chapter 20 discusses how much saddle points and local minima are really problems in deep learning, and that deep networks are "surprisingly easy to train" (p. 91).

### Notes (pp. 91–94)
- **History.** Gradient descent: Cauchy (1847). SGD: at least Robbins & Monro (1951). In engineering "objective function" is the more usual term (p. 91).
- **Convexity and the Hessian.** The Hessian $\mathbf H[\boldsymbol\phi]$ is the matrix of second derivatives, entry $(j,k)$ being $\partial^2L/\partial\phi_j\partial\phi_k$ (6.19). If it is positive definite (positive eigenvalues) for all parameter values, the function is convex: a smooth bowl, one global minimum, no local minima or saddle points. At a zero-gradient point, all-positive eigenvalues mean a minimum, all-negative a maximum, and mixed signs a saddle point (p. 92).
- **Line search.** Fixed steps move far where the function changes fast and little where it changes slowly. One line-search method is *bracketing*: evaluate two interior points $b,c$ in $[a,d]$ and discard the end segment next to the worse point (Fig. 6.10) (pp. 92–93). Gradient descent also tends to oscillate when descending valleys (p. 92).
- **Newton method.** It uses the inverse Hessian, so it needs no line search and avoids oscillation. In its simplest form it moves toward the nearest extremum, which may be a maximum, and inverting the Hessian is intractable for many parameters (p. 92).
- **SGD properties.** Jastrzębski et al. (2018): the small-learning-rate limit is a stochastic differential equation depending on the learning-rate-to-batch-size ratio, which relates to minimum width. He et al. (2019) prove a generalization bound positively correlated with batch size over learning rate. Their experiments find better test accuracy when that ratio is low (p. 92).
- **Momentum origins.** Polyak (1964); Nesterov (1983); first applied to SGD by Sutskever et al. (2013) (pp. 92–93).
- **Adaptive methods.** AdaGrad uses cumulative squared gradients, so learning rates shrink and learning can halt. RMSProp and AdaDelta update the squared gradient recursively. Adam (Kingma & Ba, 2015) is by far the most widely used. Its convergence proof for convex losses had a counterexample (Reddi et al.), leading to AMSGrad. YOGI is proved convergent in the non-convex case. The author says Adam works well in practice regardless. Learning-rate warm-up and rectified Adam address noisy early statistics (p. 93).
- **SGD vs Adam.** Wilson et al. (2017) found SGD with momentum can find lower minima that generalize better. The author finds this strange, since SGD is a special case of Adam ($\beta=0$, $\gamma\to1$) once the correction (6.16) becomes one. He says SGD more likely wins when Adam's default hyperparameters are used. Choi et al. (2019): with tuned hyperparameters Adam performs as well as SGD and converges faster. AdamW and SWATS are mentioned (p. 94).
- **Exhaustive search.** Quantize parameters and search with SAT solvers. This could find the global minimum with a guarantee but is practical only for very small models (p. 94).

## Toy example (ours)
One parameter $\phi$, model $f=\phi$, two data points $y_1=1$, $y_2=5$. Loss $L=(\phi-1)^2+(\phi-5)^2$. Per-example gradients (as in 6.7, for this model): $\partial\ell_1/\partial\phi=2(\phi-1)$, $\partial\ell_2/\partial\phi=2(\phi-5)$.

At $\phi=0$: $-2$ and $-10$. Their sum is $-12$, the full gradient (eq. 6.6). Also $L'=4\phi-12$, so the minimum is $\phi=3$.

Gradient descent, $\alpha=0.1$ (eq. 6.3):
- $\phi=0$: gradient $-12$, so $\phi\leftarrow0-0.1(-12)=1.2$.
- $\phi=1.2$: gradient $4(1.2)-12=-7.2$, so $\phi\leftarrow1.2+0.72=1.92$.
- $\phi=1.92$: gradient $-4.32$, so $\phi\leftarrow1.92+0.432=2.352$.

The steps shrink as the slope flattens, and $\phi$ approaches 3.

SGD with batch $\{2\}$ only (eq. 6.10), from $\phi=0$: gradient $-10$, so $\phi\leftarrow0+1.0=1.0$. The step differs from the full-gradient step (1.2) but goes the same way. With batch $\{1\}$ it would be $0+0.2=0.2$. Noise comes from which example is drawn.

## Concepts
- [[gradient-descent]] (new) — iteratively subtract $\alpha$ times the loss gradient from the parameters (p. 78)
- [[learning-rate]] (new) — the scalar $\alpha$ setting step size; fixed, scheduled, or chosen by line search (p. 78)
- [[line-search]] (new) — try several $\alpha$ along the gradient direction and pick the best (p. 78)
- [[convex-loss]] (new) — every chord lies above the function; a single global minimum (p. 80)
- [[local-minimum]] (new) — zero gradient and loss rises in all directions, but not the lowest loss (p. 81)
- [[saddle-point]] (new) — zero gradient, loss rises in some directions and falls in others (p. 83)
- [[sgd]] (new) — gradient descent where each step uses a random minibatch (p. 85)
- [[minibatch-epoch]] (new) — a random subset of examples per step; an epoch is one pass through all data (p. 85)
- [[learning-rate-schedule]] (new) — start $\alpha$ high, reduce by a constant factor every $N$ epochs (p. 86)
- [[momentum]] (new) — step uses a weighted sum of past gradients, with weights shrinking back in time (p. 86)
- [[nesterov-momentum]] (new) — gradient evaluated at the predicted point $\boldsymbol\phi_t-\alpha\beta\mathbf m_t$ (p. 88)
- [[adam]] (new) — momentum on gradient and squared gradient, bias-corrected, with per-coordinate normalization (p. 90)
- [[hyperparameter]] (new) — a training choice (batch size, schedule, momentum coefficients) that is not a model parameter (p. 91)
- [[hessian]] (new) — matrix of second derivatives; positive eigenvalues everywhere implies convexity (p. 92)

## Canonical instances
- [[linear-regression-gradient-descent]] (new) — convex loss; after four iterations the parameters are already close to the minimum (p. 79)
- [[gabor-model-fitting]] (new) — two-parameter non-convex loss with local minima and a saddle point; global loss 0.64 (pp. 80–82)

## Bridges (candidates)
- [structural-analogy] SGD with minibatches ↔ llm: pretraining on huge text, where each step uses a sampled batch of tokens — same noisy-gradient idea (canon link; not stated in this unit)
- [same-math] Momentum and Adam's $\mathbf m,\mathbf v$ ↔ statistics: exponentially weighted moving averages — the recursions have the same form
- [structural-analogy] Hessian-eigenvalue classification of zero-gradient points ↔ dynamical systems: stability of fixed points
- [structural-analogy] Learning rate schedule ↔ simulated annealing: large random moves early, small later

## Questions this raises
- Are local minima and saddle points really a problem for deep networks? The footnote defers to chapter 20 (p. 91).
- Why would a lower batch-size-to-learning-rate ratio or a wider minimum generalize better (p. 92)?
- How is the gradient of a network's loss actually computed (chapter 7)?
- If SGD is a special case of Adam, why does tuning matter so much for which one wins (p. 94)?

## Exercises worth doing
- Ex. 6.1 (p. 94) — derive eq. 6.7 from eq. 6.5 — difficulty: easy
- Ex. 6.2 (p. 94) — Hessian of linear regression; prove convexity via trace and determinant — difficulty: medium
- Ex. 6.7 (p. 95) — why path 1 in Fig. 6.5a zigzags at right angles, and how to prevent it — difficulty: medium
- Ex. 6.8 (p. 95) — can non-stochastic gradient descent with a fixed learning rate escape local minima? — difficulty: medium
- Ex. 6.9 (p. 95) — relate iterations, dataset size and batch size to epochs — difficulty: easy
- Ex. 6.10 (p. 95) — show momentum is an infinite weighted sum of past gradients; find the weights — difficulty: medium

## Reading notes
- Printed page = pdf page − 14. Some pages carry a "Draft: please send errata" footer.
- Equations were checked against the page images and are readable. The text layer is garbled for some equations (e.g. 6.2, 6.7).
- Notes (p. 94) write SGD as Adam's special case "when $\beta=0,\gamma\to1$". I reproduced this as printed.
- In eq. 6.2 the vector has $N+1$ entries, because indexing starts at $\phi_0$.
- Fig. 6.9 labels the second Adam momentum coefficient $\gamma$, consistent with eq. 6.15.
