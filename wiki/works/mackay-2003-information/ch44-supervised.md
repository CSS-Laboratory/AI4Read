---
id: mackay-2003-information/ch44-supervised
work: mackay-2003-information
unit: "44 Supervised Learning in Multilayer Networks"
pages: 527-533
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Supervised Learning in Multilayer Networks

## L0 — One line
Training a neural network by minimizing error plus weight decay (a penalty on large weights) can be given a Bayesian interpretation: the objective is a negative log posterior up to a constant, and the evidence (the probability of the data given the model settings) can then be used to tune model complexity without a test set.

## L1 — The gist (≤ 120 words)
How should we train and control the complexity of multilayer perceptrons (flexible nonlinear curve-fitters)? MacKay first explores random networks: the characteristic size of the weights determines how complex a typical function is. He then reads the usual objective, error plus weight decay (a penalty on large weights), as a likelihood times a prior, for regression and classification. The evidence (probability of the data given the control settings) can then be maximized to choose regularization constants, with no validation set. Marginalization (averaging over uncertain parameters) gives error bars. An exercise suggests mutual information, as an alternative to error rate, for comparing classifiers.

**Prerequisites:** Gaussian distributions; Bayes' theorem; negative log likelihood; gradient descent; the idea of overfitting; mutual information.

## L2 — Key ideas (5–10 bullets)
- A multilayer perceptron is a feedforward map $\mathbf y(\mathbf x;\mathbf w,\mathcal A)$ with hidden units; it can make functions with more complexity than a linear model (p. 527, p. 528).
- In random networks, the vertical scale, horizontal range and shortest length scale of functions are of orders set by the weight magnitudes. Neal showed that in the $H\to\infty$ limit the statistics do not depend on $H$ (p. 528).
- Sum-squared error corresponds to Gaussian noise with $\sigma_\nu^2=1/\beta$; weight decay with a quadratic $E_W$ corresponds to a Gaussian prior with $\sigma_W^2=1/\alpha$ (p. 529).
- $M(\mathbf w)=\beta E_D+\alpha E_W$ is a negative log posterior up to a constant, and minimizing it gives $\mathbf w_{\rm MP}$, a (local) most probable parameter vector (p. 529).
- Binary and softmax classifiers fit the same scheme: the negative log likelihood $G(\mathbf w)$ replaces $\beta E_D$ (p. 530).
- Over-complex models overfit. The evidence $P(\text{Data}\mid\text{control parameters})$ can be maximized instead of using a test set (p. 530, p. 531).
- Marginalizing over parameter uncertainty gives better predictions and error bars that grow where data are sparse (p. 531).
- Exercise: error rate does not necessarily measure how informative a classifier is, and can rank classifiers poorly in the examples; mutual information $I(T;Y)$ is suggested as an alternative to investigate (p. 532, p. 533).

## L3 — Walkthrough

### 44.1 Multilayer perceptrons
- A multilayer perceptron is a feedforward network with input, hidden and output neurons. One hidden layer is called a "two-layer" network; the count excludes the inputs (p. 527).
- It defines a nonlinear parameterized mapping $\mathbf y=\mathbf y(\mathbf x;\mathbf w,\mathcal A)$. The output is continuous in $\mathbf x$ and $\mathbf w$. $\mathcal A$ is the architecture, i.e. the functional form (p. 527).
- Regression network with one hidden layer (indices: $l$ over inputs, $j$ hidden, $i$ outputs) (p. 527):

$$a^{(1)}_j=\sum_l w^{(1)}_{jl}x_l+\theta^{(1)}_j;\qquad h_j=f^{(1)}\!\big(a^{(1)}_j\big)\tag{44.1}$$

$$a^{(2)}_i=\sum_j w^{(2)}_{ij}h_j+\theta^{(2)}_i;\qquad y_i=f^{(2)}\!\big(a^{(2)}_i\big)\tag{44.2}$$

  For example $f^{(1)}(a)=\tanh(a)$ and $f^{(2)}(a)=a$. Weights $w$ and biases $\theta$ together form the parameter vector $\mathbf w$. The nonlinear hidden function gives more flexibility than linear regression (p. 527).
- **Random-network experiment** (one input, one output, large $H$). Hidden biases $\theta^{(1)}_j$ are drawn Gaussian with zero mean and s.d. $\sigma_{\rm bias}$. Input-to-hidden weights have s.d. $\sigma_{\rm in}$. Output weights and output biases have s.d. $\sigma_{\rm out}$ (p. 528).
- Bigger weights and biases give more complex functions, with more features and more sensitivity to the input (p. 528). Typical scales (p. 528):
  - vertical scale of order $\sqrt H\,\sigma_{\rm out}$;
  - horizontal range of significant variation of order $\sigma_{\rm bias}/\sigma_{\rm in}$;
  - shortest horizontal length scale of order $1/\sigma_{\rm in}$.
- Fig. 44.3 example: $H=400$, $\sigma_{\rm bias}=4$, $\sigma_{\rm in}=8$, $\sigma_{\rm out}=0.5$ (p. 528).
- Neal (1996): as $H\to\infty$, the statistical properties of the random functions do not depend on the number of hidden units. So function complexity becomes independent of the number of parameters (p. 528).
- The author concludes that the characteristic magnitude of the weights determines typical complexity. He anticipates that controlling it will be an important way to control complexity when fitting real data (p. 528).
- A two-input network gives a non-flat surface (Fig. 44.4), unlike the flat plane of linear regression (p. 528).

*Intuition note.* Think of the weights' typical size as a "volume knob" for wiggliness. Large input weights make quick changes, and large output weights make tall ones. Adding more hidden units does not by itself make the random functions more complicated (in the limit).

### 44.2 How a regression network is traditionally trained
- Given data $D=\{\mathbf x^{(n)},\mathbf t^{(n)}\}$, adjust $\mathbf w$ to minimize (p. 528)

$$E_D(\mathbf w)=\frac12\sum_n\sum_i\Big(t^{(n)}_i-y_i(\mathbf x^{(n)};\mathbf w)\Big)^2.\tag{44.3}$$

- Minimization uses repeated gradient evaluation. Backpropagation computes the gradient efficiently using the chain rule (p. 528).
- Regularization (weight decay) modifies the objective (p. 529):

$$M(\mathbf w)=\beta E_D+\alpha E_W,\tag{44.4}$$

  for example $E_W=\tfrac12\sum_i w_i^2$. It favours small $\mathbf w$ and reduces the tendency to overfit noise (p. 529).
- Rumelhart et al. (1986) trained such networks by gradient descent on $M(\mathbf w)$ on non-trivial problems (e.g. symmetry of images). Applications cited: pronouncing English text, focussing telescopes (p. 529).

### 44.3 Neural network learning as inference
- The error function is interpreted as defining a noise model; $\beta E_D$ is the negative log likelihood (p. 529):

$$P(D\mid\mathbf w,\beta,\mathcal H)=\frac{1}{Z_D(\beta)}\exp(-\beta E_D).\tag{44.5}$$

  Sum-squared error corresponds to Gaussian noise on the targets, with noise level $\sigma_\nu^2=1/\beta$ (p. 529).
- The regularizer is interpreted in terms of a log prior (p. 529):

$$P(\mathbf w\mid\alpha,\mathcal H)=\frac{1}{Z_W(\alpha)}\exp(-\alpha E_W).\tag{44.6}$$

  If $E_W$ is quadratic, the prior is Gaussian with variance $\sigma_W^2=1/\alpha$. The model $\mathcal H$ fixes the architecture $\mathcal A$, the likelihood and the prior (p. 529).
- Minimizing $M$ corresponds to inferring $\mathbf w$ (p. 529):

$$P(\mathbf w\mid D,\alpha,\beta,\mathcal H)=\frac{P(D\mid\mathbf w,\beta,\mathcal H)\,P(\mathbf w\mid\alpha,\mathcal H)}{P(D\mid\alpha,\beta,\mathcal H)}\tag{44.7}$$

$$=\frac{1}{Z_M}\exp(-M(\mathbf w)).\tag{44.8}$$

  The $\mathbf w$ found by (locally) minimizing $M$ is the (locally) most probable vector, $\mathbf w_{\rm MP}$. The author says this reading "adds little new at this stage"; new tools come with further inferences (p. 529).
- **Binary classification.** Targets $t\in\{0,1\}$. Output $y\in(0,1)$ is read as $P(t{=}1\mid\mathbf x,\mathbf w,\mathcal A)$, with $f^{(2)}(a)=1/(1+e^{-a})$. $\beta E_D$ is replaced by (p. 530)

$$G(\mathbf w)=-\Big[\sum_n t^{(n)}\ln y(\mathbf x^{(n)};\mathbf w)+(1-t^{(n)})\ln\big(1-y(\mathbf x^{(n)};\mathbf w)\big)\Big].\tag{44.9}$$

  Total objective $M=G+\alpha E_W$. There is no $\beta$, since there is no Gaussian noise (p. 530).
- **Multi-class.** Targets are one-hot vectors. A softmax network has coupled outputs that sum to one and are class probabilities $y_i=P(t_i{=}1\mid\mathbf x,\mathbf w,\mathcal A)$ (p. 530):

$$y_i=\frac{e^{a_i}}{\sum_{i'}e^{a_{i'}}}\tag{44.10}$$

$$G(\mathbf w)=-\sum_n\sum_i t^{(n)}_i\ln y_i(\mathbf x^{(n)};\mathbf w).\tag{44.11}$$

  Minimizing $M=G+\alpha E_W$ again corresponds to inference of the form (44.8) (p. 530).

*Intuition note.* "Squared error + weight penalty" and "Gaussian noise + Gaussian prior" are the same function (up to a constant, for quadratic $E_W$) seen in two ways. The best-fit weights are the (locally) most probable weights. Once training is a posterior, we can ask other probabilistic questions about it.

### 44.4 Benefits of the Bayesian approach
- Statistically, supervised networks are "nothing more than nonlinear curve-fitting devices", and the effective complexity of the fit matters greatly (p. 530).
- As the control parameter (e.g. the regularization constant $\alpha$) is varied to raise complexity, the best fit to the training data keeps improving. Test error first falls, then rises: an over-complex model overfits and generalizes poorly (Fig. 44.5) (p. 530). The same problem may also complicate the choice of architecture, basis-function radius and input variables (p. 530).
- Bayesian remedy: with a probabilistic model we can evaluate the evidence for alternative control parameters. By Chapter 28, over-complex models are less probable, so $P(\text{Data}\mid\text{control parameters})$ can be the objective (Fig. 44.5e). The evidence-maximizing $\alpha$ is shown in Fig. 44.5b (p. 531).
- Four advantages (p. 531):
  1. No test or validation set, so all data serve fitting and model comparison.
  2. Regularization constants can be optimized on-line, along with ordinary parameters.
  3. The objective is not noisy, unlike a cross-validation measure.
  4. The gradient of the evidence with respect to control parameters can be evaluated, so many can be optimized at once.
- Marginalization is the "unique prescription" for including parameter uncertainty in predictions. It gives better predictions (Chapter 41) and error bars that grow where data are sparse (Fig. 44.6) (p. 531).
- Implementation: Monte Carlo sampling, or deterministic Gaussian approximations (Neal 1996; MacKay 1992c) (p. 531).
- Models are easy to extend. With multiple hyperparameters, a model can infer from the data which inputs are relevant (p. 532).

*Intuition note.* The evidence can be used in place of a test set. Over-complex models turn out to be less probable (as explained in Chapter 28), so too-flexible models score lower on the evidence even though they fit the training data best.

### 44.5 Exercise 44.1: measuring a classifier's quality (p. 532–533)
- Error rate $e=e_++e_-$ ignores firmness of predictions and need not measure informativeness. Three frequency tables (percentages, rows $t$, columns $y$) (p. 532):
  - A: $t{=}0$: (90, 0); $t{=}1$: (10, 0).
  - B: (80, 10); (0, 10).
  - C: (78, 12); (0, 10).
- A and B have error 10%, C has 12%. A always outputs 0 and conveys no information about $t$. Common sense ranks B > C > A. Error rate ranks A = B > C (p. 532).
- The pair $(e_+,e_-)$ is $(0,0.1)$ for A and $(0.1,0)$ for B. Problems: it does not show that A is worthless, and with 10 classes there are $10\times9=90$ error types (p. 532, p. 533).
- With a rejection output "?", D and E both have $(e_+,e_-,r)=(6\%,0\%,11\%)$ (p. 533):
  - D: $t{=}0$: (74, 10, 6); $t{=}1$: (0, 1, 9).
  - E: (78, 6, 6); (0, 5, 5).
- E is C in disguise (coin toss when C says '1'), so E equals C and is inferior to B. The author asks whether D can be justified as more informative than B, and so better than E (p. 533).
- Error-reject (ROC) curves plot $e$ against $r$; some use the area under them. The task: build an example showing the curve and area are not necessarily good comparisons, or prove they are (p. 533).
- Suggested alternative (p. 533):

$$I(T;Y)\equiv H(T)-H(T\mid Y)=\sum_{y,t}P(y)P(t\mid y)\log\frac{P(t)}{P(t\mid y)}.\tag{44.12}$$

  Task: evaluate it for A–E and discuss its usefulness and practical drawbacks (p. 533).

## Toy example (ours, not from the text)
One weight, linear model $y=wx$, one data point $x=1,\ t=2$, so $E_D=\tfrac12(2-w)^2$ and $E_W=\tfrac12w^2$. Take $\beta=1$, $\alpha=3$. Then $M(w)=\tfrac12(2-w)^2+\tfrac32w^2$.
- $dM/dw=-(2-w)+3w=4w-2=0\Rightarrow w_{\rm MP}=0.5$.
- $M(0.5)=\tfrac12(1.5)^2+\tfrac32(0.25)=1.125+0.375=1.5$. Compare $M(0)=2$ and $M(1)=0.5+1.5=2$, so 0.5 is lower.
- Probabilistic reading: noise variance $1/\beta=1$, prior variance $1/\alpha=1/3$. With $\alpha=1$ the minimum is $w=1$; the larger $\alpha$ (tighter prior) shrinks $w_{\rm MP}$ to 0.5.

## Concepts
- [[multilayer-perceptron]] (new) — feedforward net with input, hidden, output neurons; a nonlinear parameterized map $\mathbf y(\mathbf x;\mathbf w,\mathcal A)$ (p. 527)
- [[backpropagation]] (new) — chain-rule algorithm that computes the gradient of $E_D$ efficiently (p. 528)
- [[weight-decay]] (new) — regularizer $\alpha E_W$ favouring small weights; interpreted as a negative log prior, Gaussian when $E_W$ is quadratic (p. 529)
- [[softmax]] (new) — output layer $y_i=e^{a_i}/\sum e^{a_{i'}}$, coupled outputs summing to one (p. 530)
- [[overfitting]] (new) — a too-complex model fits training noise and generalizes poorly (p. 530)
- [[maximum-a-posteriori]] (new) — $\mathbf w_{\rm MP}$, the (locally) most probable parameter vector found by minimizing $M$ (p. 529)
- [[Likelihood]] — $\beta E_D$ or $G$ is the negative log likelihood (p. 529, p. 530)
- [[Prior distribution]] — $\exp(-\alpha E_W)/Z_W$ (p. 529)
- [[Posterior distribution]] — $\exp(-M)/Z_M$ (p. 529)
- [[Marginal likelihood (evidence)]] — $P(\text{Data}\mid\text{control parameters})$, used to set $\alpha$ (p. 531)
- [[Bayesian Occam's razor]] — over-complex models are less probable (via Chapter 28) (p. 531)
- [[Cross-validation / LOO / WAIC]] — contrasted: a cross-validation measure is noisy, unlike the Bayesian objective (p. 531)
- [[Posterior predictive distribution]] — marginalization over parameters gives predictions and error bars (p. 531)
- [[Markov chain Monte Carlo (MCMC)]] — Monte Carlo sampling named as one implementation (p. 531)
- [[mutual information I(X;Y)]] — proposed classifier score $I(T;Y)$ (p. 533)

## Canonical instances
- [[random-network-prior-functions]] (new) — functions from random weights; scales $\sqrt H\sigma_{\rm out}$, $\sigma_{\rm bias}/\sigma_{\rm in}$, $1/\sigma_{\rm in}$ (p. 528)
- [[classifier-ABCDE-comparison]] (new) — tables where error rate misranks informative classifiers (p. 532, p. 533)
- [[overfitting-curve-fig-44-5]] (new) — training error keeps falling while test error first falls then rises; the evidence has a peak (p. 531)

## Bridges (candidates)
- [same-math] weight decay $\alpha E_W$ ↔ bayesian: Gaussian prior with variance $1/\alpha$ — the penalty is the negative log prior (p. 529).
- [same-math] cross-entropy-type loss $G$ (44.9, 44.11) ↔ information-theory: negative log likelihood of the labels (p. 530).
- [structural-analogy] evidence maximization ↔ cross-validation: both choose complexity, one without held-out data.
- [structural-analogy] $I(T;Y)$ for classifiers ↔ information-theory: channel from target to output, measured in bits.

## Questions this raises
- How do Monte Carlo and Gaussian-approximation methods actually compute evidence and error bars for a network?
- Does Neal's $H\to\infty$ result mean very wide networks need no complexity control beyond weight size?
- Is mutual information a useful classifier score when costs of errors differ, and does it have practical drawbacks?
- Can the evidence-based approach handle many control parameters, such as per-input relevance?

## Exercises worth doing
- Ex. 44.1 (p. 532–533) — build an example or proof about error-reject curves and the area under them — difficulty: hard
- Ex. 44.1 (p. 533) — compute $I(T;Y)$ for classifiers A–E and compare with the common-sense ranking B > C > A — difficulty: medium
- Ex. 44.1 (p. 533) — justify (or refute) that D is more informative than B, though D and E share $(e_+,e_-,r)$ — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 539–545 ↔ printed 527–533).
- Figure 44.2's caption in the text layer has displaced superscripts. The image shows $\sigma_{\rm in}=5\sigma^{\rm w}_{\rm bias}$, $H=400$, $\sigma^{\rm w}_{\rm out}=0.05$.
- The pages carry a Cambridge University Press 2003 on-screen-viewing header. Exercise 44.1 carries the printed difficulty rating [4].
- These pages give no solution to Exercise 44.1, and this digest does not solve it.
- Eq. (44.12) is copied as printed ($\log P(t)/P(t\mid y)$). Since $H(T)-H(T\mid Y)=\sum P(y,t)\log[P(t\mid y)/P(t)]$, the printed log argument appears inverted.
