---
id: mackay-2003-information/ch41-learning
work: mackay-2003-information
unit: "41 Learning as Inference"
pages: 492-504
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Learning as Inference

## L0 — One line
Minimizing a neural network's regularized error is finding the (locally) most probable weights under a Bayesian posterior, and predictions are better when averaged over the whole posterior than made with those weights alone.

## L1 — The gist (≤ 120 words)
The chapter asks what the objective $M(\mathbf w)=G+\alpha E_W$ means probabilistically. Answer: $G$ is minus a log likelihood and $\alpha E_W$ is minus a log (Gaussian) prior, so $\exp(-M)$ is a posterior over weights. Optimization returns only the peak $\mathbf w_{\rm MP}$. That peak tends to give over-confident predictions, especially far from the training data. The Bayesian prediction averages the network's output over the posterior. The chapter computes this average by Monte Carlo (Langevin, Hamiltonian) and by a Gaussian approximation. It also warns that optimized parameters can be unrepresentative of typical plausible parameters.

**Prerequisites:** Bayes' theorem; logistic sigmoid; marginalization (sum rule) as an integral; gradient and Hessian (matrix of second derivatives); Gaussian distribution; basic Metropolis sampling.

## L2 — Key ideas
- The error $G$ is minus the log likelihood. The regularizer is minus the log of a Gaussian prior with variance $1/\alpha$. Minimizing $M$ finds the (locally) most probable weights $\mathbf w_{\rm MP}$ (pp. 492–493).
- The Bayesian product of learning is an ensemble of plausible weights, not one point. It concentrates as data arrive (p. 493).
- Using $\mathbf w_{\rm MP}$ alone often gives over-confident predictions, since it ignores uncertainty in $\mathbf w$. The fix is to marginalize over the posterior (p. 495).
- Marginalizing means averaging the neuron's output over the posterior; with samples this becomes a sample mean (pp. 495–496). Samples can come from Langevin Monte Carlo, i.e. gradient descent with added noise and an accept/reject step (pp. 496–498).
- During sampling, $M(\mathbf w)$ does not fluctuate around its minimum. The typical set differs from the most probable point, so optimized parameters can be unrepresentative (p. 500).
- Hamiltonian Monte Carlo, which uses many gradient steps per proposal, reduces random-walk behaviour. On this toy problem it is at least ten times more efficient (p. 501).
- Alternative: a Gaussian approximation at $\mathbf w_{\rm MP}$ with the Hessian $\mathbf A$. It gives an approximate closed-form moderated output $f(\kappa(s)a_{\rm MP})$ (pp. 501–502).
- Under the Gaussian approximation, marginalizing makes no difference to an immediate 0/1 decision with symmetric error costs. It does matter if there is a "don't know" option or if error costs are unequal (p. 503).

## L3 — Walkthrough

### 41.1 Neural network learning as inference (pp. 492–493)
Chapter 39's neuron was trained by minimizing
$$M(\mathbf w)=G(\mathbf w)+\alpha E_W(\mathbf w)\tag{41.1}$$
$$G(\mathbf w)=-\sum_n\Big[t^{(n)}\ln y(\mathbf x^{(n)};\mathbf w)+(1-t^{(n)})\ln(1-y(\mathbf x^{(n)};\mathbf w))\Big]\tag{41.2}$$
$$E_W(\mathbf w)=\tfrac12\sum_i w_i^2.\tag{41.3}$$

- The output is read literally as a probability: $y(\mathbf x;\mathbf w)\equiv P(t=1\mid\mathbf x,\mathbf w)$. Each $\mathbf w$ is then a hypothesis about class probability as a function of $\mathbf x$ (p. 492).
- The data $D$ are the targets $\{t\}$. The inputs are given and not modelled (p. 492).
- The two cases $P(t=1\mid\mathbf w,\mathbf x)=y$ and $P(t=0\mid\mathbf w,\mathbf x)=1-y$ (41.4) combine into one equation:
$$P(t\mid\mathbf w,\mathbf x)=y^t(1-y)^{1-t}=\exp[t\ln y+(1-t)\ln(1-y)].\tag{41.5}$$
- Hence $G$ is minus the log likelihood: $P(D\mid\mathbf w)=\exp[-G(\mathbf w)]$ (41.6) (p. 492).
- The regularizer is minus a log prior: $P(\mathbf w\mid\alpha)=\frac1{Z_W(\alpha)}\exp(-\alpha E_W)$ (41.7). For quadratic $E_W$ this is a Gaussian with variance $\sigma_W^2=1/\alpha$ and $1/Z_W(\alpha)=(\alpha/2\pi)^{K/2}$, where $K$ is the number of parameters (p. 493).
- Bayes' theorem then gives
$$P(\mathbf w\mid D,\alpha)=\frac{P(D\mid\mathbf w)P(\mathbf w\mid\alpha)}{P(D\mid\alpha)}=\frac{e^{-G}e^{-\alpha E_W}/Z_W(\alpha)}{P(D\mid\alpha)}=\frac1{Z_M}\exp(-M(\mathbf w)).\tag{41.8–41.10}$$
- So the $\mathbf w$ found by (locally) minimizing $M$ is the (locally) most probable vector, $\mathbf w^*=\mathbf w_{\rm MP}$ (p. 493).
- Why use logs: error functions are additive ($G$ is a sum of information contents, $E_W$ a sum of squares). Probabilities of independent events multiply. The log maps one to the other (p. 493).

*Intuition note:* Adding errors and multiplying probabilities are the same thing seen through a logarithm. So "lowest total error plus penalty" means "highest posterior probability" (locally, at a minimum of $M$).

### 41.2 Illustration for a neuron with two weights (p. 493)
- Model: $y=1/(1+e^{-(w_1x_1+w_2x_2)})$ (41.11), with no bias. The posterior $\propto\exp(-M)$ can be plotted in $(w_1,w_2)$ space (p. 493).
- Fig. 41.1 shows $N=0,2,4,6$ data points. The likelihood $\exp(-G)$ is a product of functions of the form (41.11). The posterior is likelihood times a broad Gaussian prior (p. 493).
- Traditional learning outputs one point $\mathbf w^*$. In the Bayesian view the output is an ensemble of plausible values, each with a posterior probability. As data increase, the posterior concentrates around $\mathbf w^*$ (p. 493).

### 41.3 Beyond optimization: making predictions (pp. 494–496)
- Setting: the neuron with two inputs and a bias, $y=1/(1+e^{-(w_0+w_1x_1+w_2x_2)})$ (41.12), trained with $\alpha=0.01$ (p. 495).
- Common practice fixes the weights at $\mathbf w_{\rm MP}$. The author says this is not optimal (p. 495).
- Example (fig. 41.2): new points A and B have the same $\mathbf w_{\rm MP}\cdot\mathbf x$, so the best-fit model gives both probability 0.2 of class 1. B is far from the training data. Intuitively one might be inclined to be less confident at B, with probability closer to 0.5 (p. 495).
- A non-Bayesian remedy is to downweight all predictions uniformly by an empirical factor (Copas, 1983). The author calls this not ideal, because intuition suggests B should be downweighted more than A (p. 495).
- Bayesian prediction marginalizes over the uncertain quantities. Here only $\mathbf w$ is taken as uncertain, with $\alpha$ and the model $\mathcal H$ fixed. By the sum rule:
$$P(t^{(N+1)}\mid\mathbf x^{(N+1)},D,\alpha)=\int d^K\mathbf w\,P(t^{(N+1)}\mid\mathbf x^{(N+1)},\mathbf w,\alpha)\,P(\mathbf w\mid D,\alpha)\tag{41.14}$$
where $K=3$ in the toy problem, and
$$P(t^{(N+1)}=1\mid\mathbf x^{(N+1)},\mathbf w,\alpha)=y(\mathbf x^{(N+1)};\mathbf w)\tag{41.15}$$
with $1-y$ for $t=0$ (p. 495).
- The weight is $P(\mathbf w\mid D,\alpha)=\frac1{Z_M}\exp(-M(\mathbf w))$ (41.16), with $Z_M=\int d^K\mathbf w\,\exp(-M(\mathbf w))$ (41.17).
- The task is the integral
$$P(t^{(N+1)}=1\mid\mathbf x^{(N+1)},D,\alpha)=\int d^K\mathbf w\;y(\mathbf x^{(N+1)};\mathbf w)\frac1{Z_M}\exp(-M(\mathbf w)),\tag{41.18}$$
the posterior average of the neuron's output (p. 495).
- Implementation (p. 496): realistic networks may have $K$ in the thousands. General options are exact methods (Ch. 25), Monte Carlo (Ch. 29), and Gaussian approximations by Laplace's method (Ch. 27) or variational methods (Ch. 33). For neural networks there are few exact methods. The two main approaches are Neal's (1996) Monte Carlo methods and MacKay's (1991) Gaussian approximations (p. 496).

*Intuition note:* Each possible weight vector "votes" with its own prediction, weighted by its posterior probability. Where plausible weight vectors disagree (far from the data), the average tends to move toward 0.5.

### 41.4 Monte Carlo implementation of a single neuron (pp. 496–501)
- Treat $y(\mathbf x^{(N+1)};\mathbf w)$ as a function $f(\mathbf w)$ and estimate
$$\langle f(\mathbf w)\rangle\simeq\frac1R\sum_r f(\mathbf w^{(r)})\tag{41.19}$$
with $\{\mathbf w^{(r)}\}$ sampled from $\frac1{Z_M}\exp(-M(\mathbf w))$ by a Metropolis method (p. 496).
- Possible disadvantage: this is a poor way to estimate a very small probability if the improbable event is most likely to occur together with improbable parameter values (p. 496).
- **Langevin Monte Carlo** (algorithm 41.4) is a simple version of Hamiltonian Monte Carlo, summarized as "gradient descent with added noise". Draw $\mathbf p$ from a unit-variance Gaussian. Compute the gradient $\mathbf g$ of $M$. Take the step
$$\Delta\mathbf w=-\tfrac12\epsilon^2\mathbf g+\epsilon\mathbf p.\tag{41.20}$$
Without the $\epsilon\mathbf p$ term this is gradient descent with $\eta=\tfrac12\epsilon^2$ (pp. 496, 498).
- The code (p. 497): $H=\mathbf p^{\mathsf T}\mathbf p/2+M$. A half-step in $\mathbf p$ is followed by a step in $\mathbf w$, a new gradient, and another half-step in $\mathbf p$. The move is accepted if $dH<0$, else with probability $\exp(-dH)$. Acceptance is set so that detailed balance holds (p. 498).
- The single parameter $\epsilon$ sets the step size. Too large and moves are rejected. Too small and progress is slow (p. 498).
- Demonstration ($\alpha=0.01$, $\eta=0.01$, $\epsilon=\sqrt{2\eta}$; figs 41.5–41.7):
  - The mean evolution of $\mathbf w$ resembles gradient descent. The sampler seems to have converged to the posterior after about 10 000 iterations (p. 498).
  - The acceptance rate was 93%. A larger $\epsilon$ would probably have been faster, but $\epsilon$ was chosen to match the earlier descent rate (p. 498).
  - Weights were sampled every 1000 iterations from 10 000 to 40 000, giving thirty plausible functions (fig. 41.6). Averaging them gives the Bayesian prediction (fig. 41.7) (p. 498).
  - The Bayesian predictions become moderate away from the densest data. The classifier better identifies uncertain points. This follows from a mechanical application of the rules of probability (pp. 498, 500).
- **Optimization and typicality** (p. 500):
  - $G(\mathbf w)$ fluctuates around $G(\mathbf w_{\rm MP})$, but not symmetrically.
  - $M(\mathbf w)$ does not fluctuate around $M(\mathbf w_{\rm MP})$, since $M$ cannot go lower than its minimum. It also only rarely drops close to it.
  - In information-theory language, the typical set of $\mathbf w$ has different properties from the most probable state.
  - Message, for all data models: be cautious with optimized parameters. They may be unrepresentative of typical plausible parameters, and predictions from them alone will often be unreasonably over-confident.
- **Hamiltonian Monte Carlo** (algorithm 41.8) replaces the four starred lines with a loop of steps (half-step in $\mathbf p$, step in $\mathbf w$, new gradient, half-step in $\mathbf p$) repeated Tau times (pp. 500–501).
  - Tau was random between 100 and 200 per trajectory. The step size was fixed for comparability, though randomizing it is recommended in practice (p. 501).
  - The autocorrelation falls much faster than for Langevin. The rejection rate was 8%. For this toy problem HMC is at least ten times more efficient (fig. 41.9) (pp. 500–501).

*Intuition note:* Plain Langevin moves wander like a random walk. Following the gradient for many steps before the accept test is how HMC reduces random-walk behaviour (p. 500).

### 41.5 Implementing inference with Gaussian approximations (pp. 501–503)
- Go to the minimum of $M$ and Taylor-expand:
$$M(\mathbf w)\simeq M(\mathbf w_{\rm MP})+\tfrac12(\mathbf w-\mathbf w_{\rm MP})^{\mathsf T}\mathbf A(\mathbf w-\mathbf w_{\rm MP})+\cdots\tag{41.22}$$
with the Hessian
$$A_{ij}\equiv\frac{\partial^2}{\partial w_i\partial w_j}M(\mathbf w)\Big|_{\mathbf w=\mathbf w_{\rm MP}}.\tag{41.23}$$
- The Gaussian approximation is
$$Q(\mathbf w;\mathbf w_{\rm MP},\mathbf A)=[\det(\mathbf A/2\pi)]^{1/2}\exp\!\Big[-\tfrac12(\mathbf w-\mathbf w_{\rm MP})^{\mathsf T}\mathbf A(\mathbf w-\mathbf w_{\rm MP})\Big].\tag{41.24}$$
Its variance–covariance matrix is $\mathbf A^{-1}$, so $\mathbf A$ defines error bars on $\mathbf w$ ($\mathbf A$ is $K\times K$) (p. 501).
- Exercise 41.1 asks for the Hessian: $\partial^2M/\partial w_i\partial w_j=\sum_{n=1}^Nf'(a^{(n)})x_i^{(n)}x_j^{(n)}+\alpha\delta_{ij}$ (41.25), with $f'(a)=f(a)(1-f(a))$ (41.26) and $a^{(n)}=\sum_jw_jx_j^{(n)}$ (41.27) (p. 501).
- **Marginalized probability** (p. 502):
  - The output depends on $\mathbf w$ only through the scalar activation $a(\mathbf x;\mathbf w)$. Under the locally Gaussian posterior, $a$ is linear in $\mathbf w$ with $\partial a/\partial\mathbf w=\mathbf x$, so $a$ is Gaussian.
  - Exercise 41.2 asks to show $P(a\mid\mathbf x,D,\alpha)=\mathrm{Normal}(a_{\rm MP},s^2)$ (41.28), with $a_{\rm MP}=a(\mathbf x;\mathbf w_{\rm MP})$ and $s^2=\mathbf x^{\mathsf T}\mathbf A^{-1}\mathbf x$.
  - The marginalized output is
$$P(t=1\mid\mathbf x,D,\alpha)=\psi(a_{\rm MP},s^2)\equiv\int da\,f(a)\,\mathrm{Normal}(a_{\rm MP},s^2),\tag{41.29}$$
in contrast to $y(\mathbf x;\mathbf w_{\rm MP})=f(a_{\rm MP})$.
  - A sigmoid-times-Gaussian integral is approximated by
$$\psi(a_{\rm MP},s^2)\simeq\phi(a_{\rm MP},s^2)\equiv f(\kappa(s)a_{\rm MP}),\qquad\kappa=1/\sqrt{1+\pi s^2/8}.\tag{41.30}$$
- Demonstration: the predictions (fig. 41.11) are qualitatively the same as the Langevin ones but clearly numerically different. So at least one method is not completely accurate (p. 503).
- Exercise 41.3 asks whether the Gaussian approximation is too heavy- or light-tailed, and when it is most accurate (p. 503).
- **Why marginalize?** (p. 503)
  - For an immediate 0/1 decision with symmetric error costs, marginalized outputs under this Gaussian approximation make no difference. Both functions pass through 0.5 at $a_{\rm MP}=0$.
  - It does matter if there is an "I don't know" option.
  - It also matters if error costs are unequal, because the decision boundary is then a contour other than 0.5 and marginalization shifts it.

*Intuition note:* Bigger $s^2$ (more weight uncertainty at $\mathbf x$) shrinks $\kappa$, pulling the output toward 0.5. When $a_{\rm MP}=0$ the shrinking changes nothing, which is why the 0.5 boundary stays put.

### Postscript on Supervised Neural Networks (p. 504)
- **Student Robert asks:** supervised networks seem equivalent to fitting a pre-defined function to data, then extrapolating. **Author:** agrees. Supervised networks so far are parameterized nonlinear functions fitted to data (p. 504).
- Robert also finds unsupervised networks more interesting; the author hopes the reader agrees (p. 504).

## Toy example (ours)
One-weight model $y=f(wx)$, $f(a)=1/(1+e^{-a})$. Suppose the posterior has only two hypotheses: $w=+2$ with probability 0.7, and $w=-1$ with probability 0.3. The most probable weight is $w_{\rm MP}=2$.

Predict $P(t=1)$ at $x=3$:
- MAP: $f(6)=1/(1+0.002479)=0.9975$.
- Under $w=-1$: $f(-3)=1/(1+20.0855)=0.0474$.
- Bayesian (eq. 41.14 with a sum): $0.7\times0.9975+0.3\times0.0474=0.6983+0.0142=0.7125$.

The MAP is very confident; the average is moderate because 30% of the posterior disagrees.

Equation 41.30 check: take $a_{\rm MP}=2$, $s^2=4$. Then $\kappa=1/\sqrt{1+4\pi/8}=1/\sqrt{2.5708}=1/1.6034=0.6237$ and $\kappa a_{\rm MP}=1.2474$. So $\phi=f(1.2474)=1/(1+0.2872)=0.777$, versus $f(2)=0.881$ without marginalization.

## Concepts
- [[likelihood]] — $P(D\mid\mathbf w)=\exp(-G)$; the error is minus its log (p. 492)
- [[prior-distribution]] — weight decay $\alpha E_W$ as a Gaussian prior, variance $1/\alpha$ (p. 493)
- [[posterior-distribution]] — $P(\mathbf w\mid D,\alpha)=\exp(-M)/Z_M$ (p. 493)
- [[map-estimate]] (new) — $\mathbf w_{\rm MP}$, the (locally) most probable weights found by minimizing $M$ (p. 493)
- [[posterior-predictive-distribution]] — average of predictions over the posterior, eq. 41.14 (p. 495)
- [[monte-carlo-integration]] — posterior averages by sample means, eq. 41.19 (p. 496)
- [[metropolis-hastings]] — accept/reject sampler used for the weights (p. 496)
- [[langevin-monte-carlo]] (new) — gradient descent with noise plus accept/reject, with detailed balance (pp. 496, 498)
- [[hamiltonian-monte-carlo]] — many gradient steps per proposal; less random-walk behaviour (p. 500)
- [[typical-set]] — here: the typical set of $\mathbf w$ has different properties from the most probable state $\mathbf w_{\rm MP}$ (p. 500)
- [[laplace-approximation]] (new) — Gaussian fit at $\mathbf w_{\rm MP}$ with covariance $\mathbf A^{-1}$ (p. 501)

## Canonical instances
- [[single-neuron-classifier-posterior]] — two-weight neuron whose posterior sharpens as data arrive (p. 493)
- [[overconfident-map-predictions]] — points A and B: same MAP output 0.2, but intuitively B warrants less confidence (p. 495)
- [[langevin-vs-hmc-neuron]] — HMC at least ten times more efficient on the toy neuron (p. 501)

## Bridges (candidates)
- [same-math] Weight decay ↔ bayesian: Gaussian prior with variance $1/\alpha$; the penalty is minus the log prior.
- [same-math] Logistic regression loss $G$ ↔ information-theory: cross-entropy; $G$ is a sum of information contents, as the text says.
- [structural-analogy] Optimized $\mathbf w_{\rm MP}$ unrepresentative of samples ↔ information-theory: typical set versus the single most probable sequence.
- [structural-analogy] Moderated output $f(\kappa a_{\rm MP})$ ↔ bayesian: posterior predictive shrinking toward 0.5 with uncertainty.

## Questions this raises
- How do $\alpha$ and the model $\mathcal H$ get inferred rather than fixed, as the text assumes here?
- When is the Gaussian approximation accurate, given it disagreed numerically with the Monte Carlo result?
- How does one judge convergence of the sampler? The text only says it "appears" converged after about 10 000 iterations.
- How would the benefit of marginalizing grow with network size, when the posterior is far from Gaussian?

## Exercises worth doing
- Ex. 41.1 (p. 501) — derive the Hessian of $M$; needed for the Gaussian approximation — difficulty: medium
- Ex. 41.2 (p. 502) — show the activation is Normal$(a_{\rm MP},s^2)$ with $s^2=\mathbf x^{\mathsf T}\mathbf A^{-1}\mathbf x$ — difficulty: medium
- Ex. 41.3 (p. 503) — tail behaviour of the Gaussian approximation and when it is accurate — difficulty: medium

## Reading notes
- Printed = pdf − 12 (pdf 504–516 ↔ printed 492–504).
- Fig. 41.5 caption writes "$M(\mathbf x)$" in (d); the axis is evidently $M(\mathbf w)$. Likely a misprint.
- In algorithm 41.4, `findM` uses `y` without computing it inside the function. As printed, the function is therefore incomplete.
- Eq. 41.13 writes $\alpha E(\mathbf w)$, where 41.1 has $\alpha E_W$. Same quantity.
- Figures (surfaces, sample plots) were read from images only roughly; no numeric values beyond those stated in the text were used.
