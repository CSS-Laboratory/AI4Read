---
id: prince-2023-udl/ch08-measuring
work: prince-2023-udl
unit: "Chapter 8 — Measuring performance"
pages: 118-137
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Measuring performance

## L0 — One line
Training error says little about generalization: test error is made of noise, bias and variance, it can behave unexpectedly as capacity grows (double descent), and hyperparameters should be chosen on a separate validation set rather than the test set.

## L1 — The gist (≤ 120 words)
How can we tell whether a trained network will work on new data? Measure it on a held-out test set. For least-squares regression, the expected test error splits into noise, bias and variance, which add up. More training data reduces variance. More capacity (number of hidden units) reduces bias but, for a fixed dataset, usually raises variance. In over-parameterized models (more parameters than training examples), however, test error can fall again (double descent), possibly because training favours smooth interpolation. Hyperparameters, such as capacity or learning rate, should not be chosen on the test set, so a separate validation set is used. This matters because a model can fit its training data perfectly and still generalize badly.

**Prerequisites:** expectation of a random variable; squared error; softmax and cross-entropy loss (chapter 5); the idea of a shallow network as a piecewise linear function.

## L2 — Key ideas
- A model can reach zero training error yet generalize poorly. On MNIST-1D, training error reached zero but test error stayed near 40% (p. 119–120).
- Test loss can rise while test error stays flat. The model keeps its mistakes but becomes more confident, a side-effect of softmax, the function that turns scores into class probabilities (p. 120).
- For least squares, expected test error = variance + bias² + noise, all additive (eq. 8.7, p. 124). Here noise is the random variation in the outputs, bias is the model being too inflexible, and variance is how much the fitted model changes with the training sample. Noise cannot be removed.
- More training data reduces variance (p. 125). More capacity reduces bias but, for a fixed dataset, typically increases variance. This is the bias-variance trade-off (p. 125).
- Double descent: test error rises near the point where the model can just memorize the data, then falls again as capacity keeps growing (p. 129).
- The proposed explanation is smooth interpolation between sparse training points. Two possible reasons are that the initialization encourages smoothness, or that the training algorithm acts as an implicit regularizer (any factor that biases a solution toward a subset of similar-loss solutions). The author calls what drives it uncertain (p. 129–132).
- Hyperparameters are chosen on a validation set. The test set is kept for the final estimate of performance (p. 133).
- The Notes add k-fold cross-validation (rotating which part of the data is used for validation), capacity measures, curse-of-dimensionality facts, data drift and hyperparameter-search algorithms (pp. 133–137).

## L3 — Walkthrough

### 8.1 Training a simple model (pp. 118–120)
- **Data:** MNIST-1D has 10 classes (digits 0–9). Each example is a randomly transformed 1D template plus noise, sampled at 40 positions. There are I = 4000 training examples, $D_i = 40$, about 400 per class (p. 118).
- **Model:** 40 inputs, 10 outputs through a softmax, two hidden layers of 100 units. It is trained by SGD with batch size 100 and learning rate 0.1 for 6000 steps (150 epochs) on multiclass cross-entropy (p. 118).
- **Result:** the training data are classified perfectly after about 4000 steps, and the training loss approaches zero (p. 118).
- This does not make the classifier perfect, because the model might have memorized the training set (p. 118–120). A test set of 1000 new examples from the same process is used.
- Test error falls only to about 40%. This is better than the chance error of 90% but far worse than training error (p. 120, fig. 8.2a).
- Test loss falls for the first 1500 steps and then rises. Test error is then roughly constant, so the model makes the same mistakes with more confidence. That lowers the probability of the correct answers and raises the negative log-likelihood (p. 120).
- This confidence is a side-effect of softmax. The pre-softmax activations are driven to extreme values so that the training-data probabilities approach one (p. 120).

*Intuition note:* Error counts only whether the top answer is right. Loss also punishes confident wrong answers. So the loss can get worse while the error stays the same.

### 8.2 Sources of error (pp. 120–124)
- **Setup:** a 1D least-squares regression task with known ground truth. A quasi-sinusoidal function on [0, 1] gets Gaussian noise of fixed variance. Training and test data are generated the same way (p. 120, fig. 8.3).
- **Toy model:** a shallow net whose first-layer weights are fixed so that the $D$ joints are evenly spaced at $0, 1/D, \dots, (D-1)/D$. It can represent any piecewise linear function with $D$ equal regions. It can be fit in closed form, so the global minimum of the loss is guaranteed (p. 120–121, fig. 8.4).

**8.2.1 Noise, bias, variance (pp. 122–123)**
- **Noise:** several valid outputs $y$ exist for one $x$. This cannot be removed from test error. It need not limit training performance, because we will likely never see the same $x$ twice (p. 122).
  - Its causes include a stochastic process, mislabeled data, or unobserved explanatory variables.
  - In rare cases noise is absent, e.g. a deterministic but expensive function. Usually it is a fundamental limit (p. 122).
- **Bias:** the model is not flexible enough to fit the true function even with optimal parameters. The three-region model cannot exactly fit the quasi-sinusoid (p. 122).
- **Variance:** training data are limited, and we cannot tell real changes in the function from noise. Different training sets give different fitted functions. There may also be extra variance from the stochastic learning algorithm (p. 123).

**8.2.2 Mathematical formulation (pp. 123–124)**

Let the noise have variance $\sigma^2$. For each $x$ there is a distribution $Pr(y|x)$ with mean $\mu[x]$:

$$\mu[x]=\mathbb{E}_y[y[x]]=\int y[x]\,Pr(y|x)\,dy, \tag{8.1}$$

and the noise is $\sigma^2=\mathbb{E}_y\big[(\mu[x]-y[x])^2\big]$ (p. 123).

Least-squares loss at position $x$. The author adds and subtracts $\mu[x]$ and expands (p. 123):

$$
\begin{aligned}
L[x]&=\big(f[x,\phi]-y[x]\big)^2\\
&=\big((f[x,\phi]-\mu[x])+(\mu[x]-y[x])\big)^2\\
&=(f[x,\phi]-\mu[x])^2+2(f[x,\phi]-\mu[x])(\mu[x]-y[x])+(\mu[x]-y[x])^2.
\end{aligned}\tag{8.2}
$$

Take the expectation over $y$. Terms without $y$ leave the expectation, and the cross term vanishes because $\mathbb{E}_y[y[x]]=\mu[x]$ (p. 123):

$$
\begin{aligned}
\mathbb{E}_y[L[x]]&=(f[x,\phi]-\mu[x])^2+2(f[x,\phi]-\mu[x])\big(\mu[x]-\mathbb{E}_y[y[x]]\big)+\mathbb{E}_y\big[(\mu[x]-y[x])^2\big]\\
&=(f[x,\phi]-\mu[x])^2+2(f[x,\phi]-\mu[x])\cdot 0+\mathbb{E}_y\big[(\mu[x]-y[x])^2\big]\\
&=(f[x,\phi]-\mu[x])^2+\sigma^2.
\end{aligned}\tag{8.3}
$$

So the expected loss is the squared gap between model and true mean, plus noise (p. 124).

The parameters depend on the training set $\mathcal D=\{x_i,y_i\}$, so write $f[x,\phi[\mathcal D]]$. The expected model output over all datasets is (p. 124):

$$f_\mu[x]=\mathbb{E}_{\mathcal D}\big[f[x,\phi[\mathcal D]]\big]. \tag{8.4}$$

Add and subtract $f_\mu[x]$ in the first term of 8.3:

$$
\begin{aligned}
(f[x,\phi[\mathcal D]]-\mu[x])^2&=\big((f[x,\phi[\mathcal D]]-f_\mu[x])+(f_\mu[x]-\mu[x])\big)^2\\
&=(f[x,\phi[\mathcal D]]-f_\mu[x])^2+2(f[x,\phi[\mathcal D]]-f_\mu[x])(f_\mu[x]-\mu[x])+(f_\mu[x]-\mu[x])^2.
\end{aligned}\tag{8.5}
$$

Taking $\mathbb{E}_{\mathcal D}$ (the author: "similar steps as for equation 8.3"):

$$\mathbb{E}_{\mathcal D}\big[(f[x,\phi[\mathcal D]]-\mu[x])^2\big]=\mathbb{E}_{\mathcal D}\big[(f[x,\phi[\mathcal D]]-f_\mu[x])^2\big]+(f_\mu[x]-\mu[x])^2. \tag{8.6}$$

(added step) The cross term vanishes because $\mathbb{E}_{\mathcal D}[f[x,\phi[\mathcal D]]-f_\mu[x]]=0$ by 8.4.

Substituting into 8.3 gives (p. 124):

$$\mathbb{E}_{\mathcal D}\big[\mathbb{E}_y[L[x]]\big]=\underbrace{\mathbb{E}_{\mathcal D}\big[(f[x,\phi[\mathcal D]]-f_\mu[x])^2\big]}_{\text{variance}}+\underbrace{(f_\mu[x]-\mu[x])^2}_{\text{bias}}+\underbrace{\sigma^2}_{\text{noise}}. \tag{8.7}$$

- Variance is the uncertainty in the fitted model due to the sampled training set. Bias is the systematic deviation of the model from the mean of the function. Noise is the inherent uncertainty of the mapping (p. 124).
- The three sources are present for any task and combine additively for regression with least squares. For other problem types their interaction can be more complex (p. 124).

*Intuition note:* Test error has a floor (noise). Above it, a model can be wrong in two ways. It can be wrong on average (bias), or it can change a lot when the training set changes (variance).

### 8.3 Reducing error (pp. 124–125)
- **8.3.1 Variance:** adding training data averages out noise and samples the input space well. With 6, 10 and 100 samples, the fitted functions become more similar each time (fig. 8.6). "In general, adding training data almost always improves test performance" (p. 125).
- **8.3.2 Bias:** bias falls if the model is made more flexible, usually by adding capacity (more hidden units and/or layers). In the toy model this means more linear regions. With ten regions the model fits the true function closely (p. 125, fig. 8.7a–c).
- **8.3.3 Trade-off:** for a fixed-size training set, variance typically increases with capacity. So more capacity does not necessarily reduce test error (p. 125, fig. 8.7d–f).
  - With 15 points, the three-region model gives similar fits on three datasets. The ten-region model fits each dataset better but devotes much of the extra descriptive power to modeling noise. This is overfitting (p. 125, fig. 8.8).
  - Bias falls and variance rises with capacity for a fixed-size training set, which suggests that there is an optimal capacity. In fig. 8.9 the sum of bias and variance is minimized at capacity four (four hidden units, four regions) (p. 125).

*Intuition note:* A flexible model can follow the truth, but it can also follow the noise in one particular sample. The best model is neither too rigid nor too flexible.

### 8.4 Double descent (pp. 127–132)
- **Experiment:** MNIST-1D with 10,000 training and 5,000 test examples. Training uses Adam, step size 0.005, full batch, 4000 steps. Capacity is increased through the number of hidden units in a two-layer net (p. 127).
- **Fig. 8.10a, original labels:** training error quickly reaches near zero. Memorization already happens before parameters equal training examples (the dashed line). Test error keeps decreasing instead of rising as the trade-off predicts (p. 127).
- **Fig. 8.10b, 15% of labels randomized:** training error again reaches zero, now needing almost as many parameters as data points. Test error shows the classical trade-off up to the exact-fit point, then decreases again. With enough capacity it falls below the minimum of the first part of the curve (p. 129).
- This is **double descent**. For some datasets, e.g. MNIST, it appears with the original data (fig. 8.10c). For others, e.g. MNIST-1D and CIFAR-100 (fig. 8.10d), it emerges or grows when label noise is added (p. 129).
- **Regimes:** the first part is the classical or under-parameterized regime. The second is the modern or over-parameterized regime. The rising middle is the critical regime (p. 129).

**8.4.1 Explanation (pp. 129–132)**
- The author calls the discovery of double descent "recent, unexpected, and somewhat puzzling". It results from two phenomena (p. 129):
  - Test performance temporarily worsens when the model has just enough capacity to memorize the data. This is as the bias-variance trade-off predicts.
  - Test performance keeps improving past the point where all training data are classified correctly. This is the confusing part, since there are not even enough data points to constrain the parameters uniquely.
- Once training loss is near zero, extra capacity cannot fit the training points better. Any change occurs between the training points. A model's tendency to prefer one solution over another there is its **inductive bias** (p. 129).
- **Curse of dimensionality:** training data are very sparse in high dimensions. MNIST-1D has 40 dimensions. With each dimension quantized into 10 bins there would be $10^{40}$ bins and only $10^4$ examples, so only one data point per $10^{36}$ bins (p. 129).
- **Putative explanation:** more capacity lets the model interpolate between nearest points more smoothly. Assuming smoothness is sensible and will probably generalize reasonably (p. 129).
- Figs. 8.11b–f show the smoothest curve through the points for 6, 7, 8, 10 and 50 hidden units. With parameters close to the number of data points, the model must contort itself. This explains why the peak is so pronounced (p. 131).
- The author notes that this does not explain why over-parameterized models should produce smooth functions. Fig. 8.12 shows three zero-loss fits from the 50-unit model, one smooth and two erratic (p. 131).
- The answer is described as uncertain, with two likely possibilities (p. 132):
  - The initialization may encourage smoothness, and the model would then never depart from the smooth functions during training.
  - The training algorithm may "prefer" smooth solutions.
- Any factor that biases a solution toward a subset of equivalent solutions is a **regularizer**. The training algorithm might act as an implicit regularizer (see section 9.2) (p. 132).

*Intuition note:* Past the memorization point, many functions fit the training points exactly, and they differ only between the points. If training tends to find smooth ones, more capacity can help.

### 8.5 Choosing hyperparameters (pp. 132–133)
- In the classical regime we cannot measure bias (it needs the true function) or variance (it needs many independent datasets). In the modern regime we cannot tell how much capacity is enough. So how to choose capacity in practice is a question (p. 132).
- **Hyperparameters** are the elements that affect test performance, namely the model-capacity and learning-algorithm choices:
  - capacity-related choices (layers, units, other architecture aspects);
  - learning-algorithm choices (learning rate, etc.) (p. 132).
  - Finding the best is **hyperparameter search**, or **neural architecture search** when focused on structure (p. 132).
- **Procedure:** train many models on the training set and keep the best. Do not judge them on the test set, because the choice might just happen to suit that set. A third **validation set** is used. For each hyperparameter choice, train on the training set and evaluate on the validation set. Finally, measure the chosen model on the test set. In principle this gives a reasonable estimate of true performance (p. 133).
- **Difficulties:** the hyperparameter space is generally smaller than the parameter space but still too big to try every combination. Many hyperparameters are discrete, and others may be conditional on one another, so we cannot rely on gradient descent. Optimization algorithms sample intelligently, using previous results. This is expensive, since each trial needs a full training run (p. 133).

### 8.6 Summary (p. 133)
- Generalization is how well performance holds on a test set. Test errors are explained by noise, bias and variance (additive for regression with least squares).
- More data lowers variance. When capacity is below the number of training examples, more capacity lowers bias and raises variance.
- This is balanced by the tendency of performance to improve even beyond the number of examples. Together they give double descent. The modern-regime smoothness is thought to explain this, but what drives it is unclear. Capacity and other hyperparameters are chosen on a validation set (p. 133).

### Notes (pp. 133–137)
- **Bias-variance for other losses:** the three factors are present but interact in a more complicated way. For classification, if a model is biased toward the wrong class in a region, increasing variance can improve the classification rate (pp. 133–134).
- **k-fold cross-validation:** used when data are limited, because with few training examples the variance is large. Split the training and validation data into $K$ disjoint parts (e.g. 5). Train on four and validate on the fifth, for each of five permutations. Pick hyperparameters by average validation performance. Assess the final models, averaging their predictions, on a separate test set. The aim is to use more data for training and so reduce variance (p. 134).
- **Capacity:** "capacity" was used informally for number of parameters or hidden units. *Representational capacity* is the space of functions the model can construct over all parameter values. *Effective capacity* accounts for what the optimizer can reach. The VC dimension is the largest number of training examples a binary classifier can label arbitrarily. Rademacher complexity is the expected empirical performance on random labels (p. 134).
- **Double descent literature (as reported by the author):**
  - Belkin et al. coined the term and also claimed it in decision trees, but Buschjäger & Morik gave contrary evidence.
  - Nakkiran et al. found it across datasets, architectures and optimizers. It is more pronounced with label noise and, per Ishida et al., with some regularization.
  - Nakkiran et al. also give evidence that test performance depends on effective model capacity, and they observe epoch-wise double descent.
  - Prediction: adding training data can sometimes worsen test performance, if it moves the model into the critical region (p. 134).
  - Bubeck & Sellke prove that overparameterization is necessary to interpolate data smoothly in high dimensions (p. 135).
- **Curse of dimensionality:** the data needed to sample space densely grows exponentially with dimension. Properties listed (p. 135):
  - random standard-normal points are very close to orthogonal with high likelihood;
  - their distance from the origin is roughly constant;
  - most of a hypersphere's volume is near its surface;
  - a hypersphere inscribed in a unit hypercube takes a decreasing share of the volume as dimension grows;
  - for random points in a hypercube, the nearest/furthest distance ratio approaches one.
  
  Fig. 8.13 shows typical samples lying in a narrow shell (p. 137). Low-dimensional visualizations should be treated with "healthy skepticism" (p. 135).
- **Real-world performance:** test results do not reflect real use if the test set's statistics differ from real data. This is data drift. There are three causes of worse real-world performance (p. 135):
  - covariate shift (input statistics change);
  - prior shift (output statistics change);
  - concept shift (the input–output relationship changes).
- **Hyperparameter search methods (p. 135–136):**
  - random sampling;
  - Bayesian optimization (Gaussian processes), exploring where uncertainty is high and exploiting promising regions;
  - SMAC (random forest as surrogate);
  - Tree-Parzen Estimators, which model the probability of hyperparameters given performance;
  - Hyperband: run random configurations on a budget, keep the best fraction $\eta$, multiply the budget by $1/\eta$, repeat;
  - BOHB, combining Hyperband's efficiency with Tree-Parzen sampling.

## Toy example (ours, not from the text)
Fix one input $x$. Suppose the true mean is $\mu[x]=1$ and the noise variance is $\sigma^2=0.25$. Suppose training on a random dataset gives prediction 0.6 or 1.0, each with probability ½.

- $f_\mu[x]=\tfrac12(0.6)+\tfrac12(1.0)=0.8$.
- Variance $=\tfrac12(0.6-0.8)^2+\tfrac12(1.0-0.8)^2=\tfrac12(0.04)+\tfrac12(0.04)=0.04$.
- Bias $=(0.8-1)^2=0.04$.
- Noise $=0.25$.
- Eq. 8.7 total: $0.04+0.04+0.25=0.33$.
- Check against eq. 8.6: $\mathbb{E}_{\mathcal D}[(f-\mu)^2]=\tfrac12(0.6-1)^2+\tfrac12(1-1)^2=0.08=0.04+0.04$ ✓. Adding noise gives $0.08+0.25=0.33$ ✓.

## Concepts
- [[generalization]] (new) — how well performance is maintained on new test data (p. 133)
- [[test-set]] (new) — held-out input/output pairs from the same process, used to estimate true performance (p. 120)
- [[validation-set]] (new) — third dataset used to choose hyperparameters; test set is used only for the final estimate (p. 133)
- [[bias-variance-decomposition]] (new) — expected least-squares test error = variance + bias² + noise (p. 124)
- [[noise-bias-variance]] (new) — three error sources: inherent output uncertainty, model inflexibility, dependence on the training sample (p. 122)
- [[overfitting]] (new) — extra model flexibility devoted to modeling noise in the training data (p. 125)
- [[double-descent]] (new) — test error falls, rises near the exact-fit point, then falls again with capacity (p. 129)
- [[inductive-bias]] (new) — a model's tendency to prefer one solution over another between data points (p. 129)
- [[regularization]] (new) — any factor biasing a solution toward a subset of solutions with similar training loss; possibly implicit (p. 132)
- [[curse-of-dimensionality]] (new) — volume of high-dimensional space overwhelms the number of training points (p. 129)
- [[hyperparameter]] (new) — a choice of architecture (e.g. layers, units) or learning algorithm (e.g. learning rate) that affects test performance (p. 132)
- [[k-fold-cross-validation]] (new) — rotate which of $K$ disjoint parts is used for validation (p. 134)
- [[cross-entropy / log-loss]] — multiclass loss; test loss rises when wrong predictions grow more confident (p. 120)
- [[softmax]] — turns scores into probabilities; pre-softmax activations driven to extreme values explain the increasing confidence (p. 120)

## Canonical instances
- [[mnist-1d]] — 1D digit-like dataset where train error reaches zero but test error stays near 40% (p. 118–120)
- [[piecewise-linear-toy-regression]] — closed-form shallow net with D equal regions, used to show noise, bias, variance (p. 120–125)
- [[double-descent-curves]] — MNIST-1D with 15% label noise, MNIST, CIFAR-100 (pp. 129–130)
- [[grid-sparsity-example]] — $10^{40}$ bins versus $10^4$ examples (p. 129)

## Bridges (candidates)
- [same-math] bias–variance decomposition (eq. 8.7) ↔ estimation theory: mean squared error of an estimator = variance + bias² (here with extra irreducible noise) — same squared-error algebra.
- [structural-analogy] validation set for hyperparameters ↔ model selection in statistics: choosing among models on data not used for the final evaluation.
- [structural-analogy] curse of dimensionality (sparse data in 40-D) ↔ nearest-neighbour and density estimation: distances lose contrast in high dimensions (note 5, p. 135).
- [metaphor] over-parameterized network "choosing the smoothest fit" ↔ Occam's razor: prefer simpler explanations when data do not decide.

## Questions this raises
- If the training algorithm is the implicit regularizer, how does test performance depend on training length and optimizer, not only on architecture (cf. effective capacity, p. 134)?
- How should we choose the capacity in the modern regime, where no point of "enough" capacity can be read from training error?
- Do bias and variance decompose in a useful way for cross-entropy or other losses (p. 124, 133)?
- How can we detect covariate, prior or concept shift once a model is deployed (p. 135)?

## Exercises worth doing
- Ex. 8.1 (p. 136) — can multiclass cross-entropy training loss reach exactly zero? Links to softmax saturation — difficulty: easy
- Ex. 8.3 (p. 136) — closed-form least-squares fit for the 3-hidden-unit model — difficulty: medium
- Ex. 8.4 (p. 136) — predict training and test performance at the 200-unit point of fig. 8.10b if training examples rise from 10,000 to 50,410 — difficulty: medium
- Ex. 8.5 (p. 136) — heteroscedastic model when training loss can be driven to zero — difficulty: hard
- Ex. 8.6 (p. 136) — random Gaussian points in 1000-D are nearly orthogonal — difficulty: medium
- Ex. 8.9 (p. 137) — empirical check of the typical-shell distances in 25, 100 and 500 dimensions — difficulty: easy

## Reading notes
- Printed page = pdf − 14 (pdf 132 = printed 118). Page labels give printed numbers.
- The text layer is garbled for equations 8.2–8.7 (pdf 137–138). The page images were used to check the LaTeX above.
- This is a draft edition ("Draft: please send errata…" in the footer), under a CC-BY-NC-ND licence, MIT Press.
- Fig. 8.13 is on p. 137 under the running header "Notes"; Problems start on p. 136 and Problems 8.7–8.9 continue onto p. 137. Eq. 8.8 (hypersphere volume) is printed on p. 137 as part of Problem 8.7.
- The author gives no cross term derivation for eq. 8.6; the vanishing step is marked as added above.
- No misprints noticed. Problems have no printed solutions in these pages.
