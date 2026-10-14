---
id: deisenroth-2020-mml/ch08-when
work: deisenroth-2020-mml
unit: "8 When Models Meet Data"
pages: 251-288
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# When Models Meet Data

## L0 — One line
A machine learning model is fitted to data by empirical risk minimization, maximum likelihood or MAP point estimates, or by full Bayesian inference, and its quality is judged on unseen data, using cross-validation or model evidence.

## L1 — The gist (≤ 120 words)
The chapter asks what it means for a model to be "good". The answer given is that it should perform well on unseen data. Data become vectors, and a predictor is either a function or a probability model. Training can be empirical risk minimization (loss plus regularizer), maximum likelihood or MAP (negative log-likelihood or negative log-posterior), or Bayesian inference (a full posterior, which needs integration). Overfitting is checked with cross-validation. Directed graphical models give a compact picture of a joint distribution. Model selection uses nested cross-validation, marginal likelihood and Bayes factors, or information criteria. The chapter prepares the regression, PCA, density-estimation and classification chapters.

**Prerequisites:** vectors and matrices (X ∈ ℝ^{N×D}), norms, gradients and optimization, Bayes' theorem, Gaussian distributions, independence and conditional independence, conjugate priors.

## L2 — Key ideas (5–10 bullets)
- Data are N examples, each a D-dimensional vector of features. The table X ∈ ℝ^{N×D} has examples as rows, and labels y_n form a vector. This lets linear algebra, geometry and optimization be applied. (pp. 252–254)
- A predictor is a function f: ℝ^D → ℝ (here affine: θᵀx + θ₀) or a probabilistic model. Learning means finding parameters so that the predictor does well on unseen data. (pp. 255–258)
- Empirical risk minimization (choosing parameters that minimize the average loss on the training data) has four design choices: hypothesis class, loss function, regularization and a search procedure. Regularization (a penalty on the parameters) discourages overfitting, and cross-validation (repeatedly holding out part of the data for testing) estimates how well a predictor generalizes. (pp. 259–264)
- Maximum likelihood picks the parameters that most likely generated the data, i.e., it minimizes the negative log-likelihood. With Gaussian noise of known σ this is the least-squares problem. MAP adds a prior, which is analogous to a regularizer (a penalty on large parameters). (pp. 265–269)
- Overfitting, underfitting and fitting well describe how the richness of the model class matches the data-generating model. (pp. 270–272)
- Bayesian inference keeps the whole posterior over parameters, so its key computation is integration, not optimization. Latent-variable models (with extra unobserved variables z) need extra marginalization. (pp. 273–277)
- Directed graphical models (graphs whose nodes are random variables) write the joint as ∏ₖ p(xₖ | Paₖ), where Paₖ are the parent nodes of xₖ. d-separation, a rule about blocked paths, reads conditional independence off the graph. (pp. 278–282)
- Model selection uses nested cross-validation (cross-validation repeated inside each split), or the evidence p(D | M) (the probability of the data with the parameters integrated out), which embodies an "automatic Occam's razor". Bayes factors compare two models. AIC and BIC are heuristics that penalize model complexity when working with the maximum likelihood estimate. (pp. 283–288)

## L3 — Walkthrough

### Opening (p. 251)
Part II uses the mathematics of Part I to describe four pillars: regression (Ch. 9), dimensionality reduction (Ch. 10), density estimation (Ch. 11) and classification (Ch. 12). The aim is practical methods, not advanced machine learning (p. 251).

### 8.1 Data, Models, and Learning
The three components are data, models and learning. The main question is "What do we mean by good models?". A guiding principle is that good models should perform well on unseen data. That requires performance metrics and ways to do well under them (p. 251). "Algorithm" has two senses, training and prediction (p. 252).

**8.1.1 Data as vectors.**
- Data are assumed tabular and numeric. Rows are instances (examples, data points). Columns are features (attributes, covariates) (p. 252).
- Choices remain even for tabular data. In Table 8.2, gender becomes −1/+1 (0/1 would also do). Degrees are ordered numbers, using domain knowledge about how degrees progress. The postcode becomes latitude and longitude. The Name column is dropped, because an identifier should not be informative and anonymizing protects privacy (pp. 252–253).
- Without additional information, one should shift and scale every column to empirical mean 0 and empirical variance 1 (p. 253).
- Notation: N examples indexed n = 1..N, features d = 1..D, each x_n ∈ ℝ^D. X ∈ ℝ^{N×D} stacks the examples. Examples are rows here, but some algorithms (Ch. 10) prefer column vectors (p. 253).
- Supervised learning: each x_n has a label y_n (target, response variable, annotation). The dataset is {(x₁,y₁),…,(x_N,y_N)}. Running example: x = age, y = salary, and we want the salary at x = 60 (Fig. 8.1) (pp. 253–254).
- Vectors allow similarity or distance between examples (geometry, Ch. 3) and optimization (Ch. 7) (p. 254).
- Two ways to get better representations: lower-dimensional approximations (principal components, Ch. 10, related to eigenvalues and SVD of Ch. 4) and nonlinear higher-dimensional combinations through a feature map φ(·), giving φ(x_n). The feature map is treated in Sec. 9.2 and leads to a kernel in Sec. 12.4. Deep learning learns features from data. It is not covered here (backpropagation is in Sec. 5.6) (p. 254).

**8.1.2 Models as functions.**
A predictor maps an input vector to a real number:
$$f:\mathbb{R}^D\to\mathbb{R}\tag{8.1}$$
The book restricts itself to linear (affine) functions, avoiding functional analysis:
$$f(\boldsymbol x)=\boldsymbol\theta^\top\boldsymbol x+\theta_0\tag{8.2}$$
with unknown θ, θ₀. Chapters 2 and 3 then suffice to state the non-probabilistic predictor precisely. Linear functions balance generality against the background mathematics needed (pp. 255–256). Fig. 8.2 shows a line with f(60) = 100 (p. 255).

**8.1.3 Models as probability distributions.**
- Data are treated as noisy observations of a true effect. Probability theory (Ch. 6) quantifies the uncertainty, for example a Gaussian predictive distribution at x = 60 (Fig. 8.3) (p. 256).
- A predictor can be seen as a distribution over possible functions. The book limits itself to distributions with finite-dimensional parameters, so models are multivariate distributions and no stochastic processes are needed (p. 256).

**8.1.4 Learning is finding parameters.**
Three algorithmic phases (p. 257):
1. Prediction or inference: a trained predictor with fixed parameters and model is applied to new inputs. For probabilistic models this phase is called inference.
2. Training or parameter estimation: adjust the model using training data.
3. Hyperparameter tuning or model selection.

A remark says naming is not agreed. "Inference" is sometimes used for parameter estimation, and less often for prediction in non-probabilistic models (p. 257).

Training uses either a best predictor under some quality measure (a point estimate) or Bayesian inference. Bayesian inference requires probabilistic models. Non-probabilistic models use empirical risk minimization (Sec. 8.2). Statistical models use maximum likelihood (Sec. 8.3). Parameter uncertainty is modeled in Sec. 8.4 (p. 257). Most training is hill climbing on an objective, using gradients (Ch. 5) and optimization (Ch. 7). Since optimization conventions minimize, an extra minus sign often appears in objectives (p. 257).

Fitting the training data is not enough. Cross-validation (Sec. 8.2.4) simulates unseen data. Performing well requires balancing fit against "simple" explanations, through regularization (Sec. 8.2.3) or a prior (Sec. 8.3.2). The book calls this abduction, "inference to the best explanation" (p. 258). Hyperparameters (for example the number of components) can affect performance a lot. Choosing among models is model selection (Sec. 8.6), for non-probabilistic models often by nested cross-validation (p. 258).

A remark says the parameter/hyperparameter distinction is somewhat arbitrary. It is driven by what can be numerically optimized versus what needs search. Another view is that hyperparameters control the distribution of the explicit parameters (p. 258).

> **Intuition note.** The book separates three jobs: using a fixed model (prediction), fitting its parameters (training), and choosing the model itself (selection). Several later sections are different ways to do the second or third job, so that the first works on new data.

### 8.2 Empirical Risk Minimization
ERM was originally popularized by the support vector machine (Ch. 12). It asks what learning is without explicitly building probabilistic models. Four design questions (pp. 258–259): which set of functions, how to measure fit on training data, how to generalize to unseen test data, and how to search the model space.

**8.2.1 Hypothesis class of functions.**
Given examples x_n ∈ ℝ^D and labels y_n ∈ ℝ, we estimate f(·, θ): ℝ^D → ℝ so that
$$f(\boldsymbol x_n,\boldsymbol\theta^*)\approx y_n\quad\text{for all } n=1,\dots,N\tag{8.3}$$
and write ŷ_n = f(x_n, θ*) (p. 259).

*Example 8.1 (ordinary least-squares regression).* The class is the affine functions. Add a unit feature x^{(0)} = 1, so x_n = [1, x_n^{(1)}, …, x_n^{(D)}]ᵀ and θ = [θ₀, θ₁, …, θ_D]ᵀ. Then
$$f(\boldsymbol x_n,\boldsymbol\theta)=\boldsymbol\theta^\top\boldsymbol x_n\tag{8.4}$$
$$f(\boldsymbol x_n,\boldsymbol\theta)=\theta_0+\sum_{d=1}^{D}\theta_d x_n^{(d)}\tag{8.5}$$
Now f: ℝ^{D+1} → ℝ. Affine functions are often called linear in machine learning (p. 259). Non-linear classes, such as neural networks, are possible (p. 260).

**8.2.2 Loss function for training.**
- A loss function ℓ(y_n, ŷ_n) takes the true label and the prediction and returns a non-negative number measuring the error. We minimize the average loss on the N training examples (p. 260).
- Assumption: the examples are independent and identically distributed (i.i.d.). Independence means (x_i,y_i) and (x_j,y_j) do not statistically depend on each other, so the empirical mean is a good estimate of the population mean. The empirical mean of the loss on training data can then be used (p. 260).
- With X := [x₁,…,x_N]ᵀ ∈ ℝ^{N×D} and y := [y₁,…,y_N]ᵀ ∈ ℝ^N, the empirical risk is
$$\mathbf R_{\rm emp}(f,\boldsymbol X,\boldsymbol y)=\frac1N\sum_{n=1}^N \ell(y_n,\hat y_n)\tag{8.6}$$
with ŷ_n = f(x_n, θ). Learning by minimizing it is empirical risk minimization (p. 260).

*Example 8.2 (least-squares loss).* With squared loss ℓ(y_n, ŷ_n) = (y_n − ŷ_n)²:
$$\min_{\boldsymbol\theta\in\mathbb R^D}\frac1N\sum_{n=1}^N (y_n-f(\boldsymbol x_n,\boldsymbol\theta))^2\tag{8.7}$$
With the linear predictor:
$$\min_{\boldsymbol\theta\in\mathbb R^D}\frac1N\sum_{n=1}^N (y_n-\boldsymbol\theta^\top\boldsymbol x_n)^2\tag{8.8}$$
In matrix form:
$$\min_{\boldsymbol\theta\in\mathbb R^D}\frac1N\|\boldsymbol y-\boldsymbol X\boldsymbol\theta\|^2\tag{8.9}$$
This is the least-squares problem. It has a closed-form solution via the normal equations (Sec. 9.2) (p. 261).

We actually want low risk on unseen data, that is, the expected risk (also called population risk), the expectation over the infinite set of all possible data and labels:
$$\mathbf R_{\rm true}(f)=\mathbb E_{\boldsymbol x,y}[\ell(y,f(\boldsymbol x))]\tag{8.10}$$
Two practical questions follow: how to change training so it generalizes, and how to estimate the expected risk from finite data (p. 261). A remark says the loss should in principle match the task's performance measure. In practice they often mismatch, for example for ease of implementation or efficiency of optimization (p. 261).

> **Intuition note.** The empirical risk is the average error on the data we have. The expected risk is the average error on all data we might ever see. ERM minimizes the first and hopes the second is small as well.

**8.2.3 Regularization to reduce overfitting.**
- Part of the data is held out as a test set. The training set fits the model and the test set evaluates generalization. One must not cycle back to a new round of training after seeing the test set (p. 262).
- With a rich enough function class, the training data can essentially be memorized, giving zero empirical risk but poor generalization (p. 262).
- Overfitting: very small average training loss but large test loss. It tends to occur with little data and a complex hypothesis class. For a fixed predictor, it occurs when R_emp on training data underestimates R_true. A test risk much larger than the training risk indicates it (p. 262).
- Regularization is a penalty term that biases the minimizer away from overly flexible predictors. It compromises between accurate ERM and the size or complexity of the solution (p. 262).

*Example 8.3 (regularized least squares).* Replace
$$\min_{\boldsymbol\theta}\frac1N\|\boldsymbol y-\boldsymbol X\boldsymbol\theta\|^2\tag{8.11}$$
by
$$\min_{\boldsymbol\theta}\frac1N\|\boldsymbol y-\boldsymbol X\boldsymbol\theta\|^2+\lambda\|\boldsymbol\theta\|^2\tag{8.12}$$
The term ‖θ‖² is the regularizer and λ the regularization parameter. It trades off training loss against the magnitude of θ. The book notes that parameter magnitudes often become relatively large under overfitting (p. 263).

The penalty biases θ toward the origin. In probabilistic models the same idea appears as a prior on the parameters (Sec. 8.3.2). In Chapter 12 the regularizer is said to be equivalent to a large margin (p. 263).

**8.2.4 Cross-validation.**
- A validation set is a subset of the available training data that is kept aside. A small one gives a noisy, high-variance performance estimate, but a large one leaves less data for training (p. 263).
- *K-fold cross-validation*: split the data into K chunks. K−1 form the training set R and one is the validation set V. Repeat for all K choices of V and average the performance (Fig. 8.4 shows K = 5). The data are D = R ∪ V with R ∩ V = ∅ (p. 263).
- Each partition k trains f^{(k)} on R^{(k)} and evaluates the risk on V^{(k)} (for example RMSE). The expected generalization error is approximated by
$$\mathbb E_{\mathcal V}[R(f,\mathcal V)]\approx\frac1K\sum_{k=1}^K R(f^{(k)},\mathcal V^{(k)})\tag{8.13}$$
- The approximation has two error sources: a finite training set, so f^{(k)} is not the best possible, and a finite validation set, so the risk is estimated inaccurately (p. 264).
- Disadvantage: K training runs. Exploring several hyperparameters may need a number of training runs exponential in the number of parameters. Nested cross-validation (Sec. 8.6.1) can search hyperparameters. Cross-validation is embarrassingly parallel: with enough computing resources it takes no longer than one assessment (p. 264).

**8.2.5 Further reading (summary).** ERM comes from Vapnik and has led to statistical learning theory. The regularization here is Tikhonov regularization, with a closely related constrained version called Ivanov regularization. Bootstrap and jackknife are alternatives to cross-validation. The book says that calling ERM "probability free" is incorrect. An unknown distribution p(x,y) governs the data, but ERM is agnostic to it, and unlike standard statistics it needs no noise model for y (p. 265).

### 8.3 Parameter Estimation
Probability distributions now model uncertainty from the observation process and about the parameters. The likelihood is analogous to the loss, and the prior is analogous to regularization (p. 265).

**8.3.1 Maximum likelihood estimation (MLE).**
For data x and a density family p(x | θ), the negative log-likelihood is
$$\mathcal L_{\boldsymbol x}(\boldsymbol\theta)=-\log p(\boldsymbol x\mid\boldsymbol\theta)\tag{8.14}$$
θ varies and x is fixed. For fixed θ, p(x | θ) models the uncertainty of the data. For fixed data, L(θ) says how likely a setting of θ is. The MLE gives the most likely θ (pp. 265–266).

In the supervised setting we specify the conditional distribution of labels given examples (p. 266).

*Example 8.4.* Assume independent Gaussian noise ε_n ∼ N(0, σ²) and the linear model x_nᵀθ. Then
$$p(y_n\mid\boldsymbol x_n,\boldsymbol\theta)=\mathcal N(y_n\mid\boldsymbol x_n^\top\boldsymbol\theta,\sigma^2)\tag{8.15}$$
(p. 266).

With i.i.d. data (Y = {y₁..y_N}, 𝒳 = {x₁..x_N}), independence gives a product, and "identically distributed" means every factor has the same form and parameters:
$$p(\mathcal Y\mid\mathcal X,\boldsymbol\theta)=\prod_{n=1}^N p(y_n\mid\boldsymbol x_n,\boldsymbol\theta)\tag{8.16}$$
Sums are easier to optimize than products (log(ab) = log a + log b), so we use
$$\mathcal L(\boldsymbol\theta)=-\log p(\mathcal Y\mid\mathcal X,\boldsymbol\theta)=-\sum_{n=1}^N\log p(y_n\mid\boldsymbol x_n,\boldsymbol\theta)\tag{8.17}$$
Although θ stands right of the conditioning bar, it should not be treated as fixed. L(θ) is a function of θ, and we minimize it over θ. A remark: the minus sign is a historical artifact, because we want to maximize likelihood but optimization literature minimizes (p. 267).

*Example 8.5 (Gaussian case).*
$$\mathcal L(\boldsymbol\theta)=-\sum_{n=1}^N\log p(y_n\mid\boldsymbol x_n,\boldsymbol\theta)=-\sum_{n=1}^N\log\mathcal N(y_n\mid\boldsymbol x_n^\top\boldsymbol\theta,\sigma^2)\tag{8.18a}$$
$$=-\sum_{n=1}^N\log\frac1{\sqrt{2\pi\sigma^2}}\exp\!\Big(-\frac{(y_n-\boldsymbol x_n^\top\boldsymbol\theta)^2}{2\sigma^2}\Big)\tag{8.18b}$$
$$=-\sum_{n=1}^N\log\exp\!\Big(-\frac{(y_n-\boldsymbol x_n^\top\boldsymbol\theta)^2}{2\sigma^2}\Big)-\sum_{n=1}^N\log\frac1{\sqrt{2\pi\sigma^2}}\tag{8.18c}$$
$$=\frac1{2\sigma^2}\sum_{n=1}^N(y_n-\boldsymbol x_n^\top\boldsymbol\theta)^2-\sum_{n=1}^N\log\frac1{\sqrt{2\pi\sigma^2}}\tag{8.18d}$$
Since σ is given, the second term is constant. Minimizing L(θ) therefore solves the least-squares problem (8.8) (p. 267).

For Gaussian likelihoods this has a closed-form solution (Ch. 9). Fig. 8.5 shows the fitted line and the prediction at x = 60. MLE may overfit, like unregularized ERM. For non-Gaussian likelihoods a closed form may not exist, and numerical optimization (Ch. 7) is used (p. 268).

> **Intuition note.** With Gaussian noise of known σ, "make the data most probable" and "make the squared errors smallest" give the same minimizer. The likelihood view just adds a reason (the noise model) for choosing the squared loss.

**8.3.2 Maximum a posteriori (MAP) estimation.**
A prior p(θ) encodes prior knowledge. Bayes' theorem (Sec. 6.3) gives the posterior from the prior and the likelihood:
$$p(\boldsymbol\theta\mid\boldsymbol x)=\frac{p(\boldsymbol x\mid\boldsymbol\theta)p(\boldsymbol\theta)}{p(\boldsymbol x)}\tag{8.19}$$
Since p(x) does not depend on θ, it can be ignored for optimization:
$$p(\boldsymbol\theta\mid\boldsymbol x)\propto p(\boldsymbol x\mid\boldsymbol\theta)p(\boldsymbol\theta)\tag{8.20}$$
MAP estimation minimizes the negative log-posterior (p. 269). Fig. 8.6 compares MLE and MAP at x = 60 with a zero-mean Gaussian prior. The prior biases the slope to be less steep and the intercept closer to zero. In this example, moving the intercept toward zero actually increases the slope (p. 268).

*Example 8.6.* With a Gaussian likelihood and a prior p(θ) = N(0, Σ), the conjugate prior of a Gaussian is Gaussian, so the posterior is expected to be Gaussian too. Details are in Ch. 9 (p. 269).

Regularization (Sec. 8.2.3) is an alternative view of including prior knowledge. MAP can be considered to bridge the non-probabilistic and probabilistic worlds: it explicitly acknowledges the need for a prior but still only produces a point estimate (p. 269).

*Remark (properties of the MLE θ_ML)* (pp. 269–270):
- Asymptotic consistency: it converges to the true value in the limit of infinitely many observations, plus an approximately normal random error.
- The sample size needed for this can be quite large.
- The error's variance decays like 1/N.
- In the "small" data regime, MLE can lead to overfitting.

Both MLE and MAP still return one set of parameter values. Sec. 8.4 treats parameters as random variables and uses the full distribution for prediction (p. 270).

**8.3.3 Model fitting.**
The parametrization defines a model class M_θ. Example: y = ax + b with θ := {a, b}. Assume the data come from an unknown model M*. We optimize θ so that M_θ is as close as possible to M*, where closeness is set by the objective (Fig. 8.7: a small class with M* outside it) (pp. 270–271). Three cases (p. 271):
- *Overfitting:* the class is too rich for the data-generating model, so M_θ could model much more complicated datasets (for example seventh-order polynomials for linear data). Such models typically have many parameters. They use their flexibility to reduce training error and find "signal" in noise. This causes problems away from the training data (Fig. 8.8a). One practical sign is low training risk but high test risk in cross-validation.
- *Underfitting:* the class is not rich enough (for example straight lines for sinusoidal data). The best line is still found, but is far from the true model. Such models typically have few parameters (Fig. 8.8b).
- *Fitting well:* the class is about right and has good generalization properties (Fig. 8.8c).

Rich classes such as deep neural networks are common. To mitigate overfitting, use regularization or priors. Choosing the class is the topic of Sec. 8.6 (p. 272).

**8.3.4 Further reading (summary).** MLE generalizes least-squares regression for linear models. Putting a nonlinear function φ on the linear output, p(y_n | x_n, θ) = φ(θᵀx_n) (8.21), gives generalized linear models, with φ called the link function. This allows binary classification or count data, and is related to exponential-family likelihoods. MLE is described as frequentist in nature. Some probabilistic models do not allow MLE (p. 272).

### 8.4 Probabilistic Modeling and Inference
We build models of the generative process that produces the data. Coin-flip example: a parameter μ gives the probability of heads as the parameter of a Bernoulli distribution, and an outcome x ∈ {head, tail} is sampled from p(x | μ) = Ber(μ). μ is unknown and cannot be observed directly (p. 273).

**8.4.1 Probabilistic models.** They represent uncertain aspects as distributions and give a unified set of tools for modeling, inference, prediction and model selection. The joint p(x, θ) of observed variables and hidden parameters is central. It encapsulates the prior and likelihood (product rule). The marginal likelihood p(x) is obtained by integrating out the parameters (sum rule). The posterior is the joint divided by the marginal likelihood. Only the joint has this property, so a probabilistic model is specified by the joint distribution of all its random variables (p. 273).

**8.4.2 Bayesian inference.**
- MLE and MAP give a single θ*, and prediction uses p(x | θ*). Keeping only a statistic of the posterior loses information, which can be critical when decisions use other objectives (squared error, misclassification). Having the full posterior can lead to more robust decisions (pp. 273–274).
- The posterior for a dataset 𝒳, prior p(θ) and likelihood:
$$p(\boldsymbol\theta\mid\mathcal X)=\frac{p(\mathcal X\mid\boldsymbol\theta)p(\boldsymbol\theta)}{p(\mathcal X)},\qquad p(\mathcal X)=\int p(\mathcal X\mid\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta\tag{8.22}$$
- Predictions propagate parameter uncertainty:
$$p(\boldsymbol x)=\int p(\boldsymbol x\mid\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta=\mathbb E_{\boldsymbol\theta}[p(\boldsymbol x\mid\boldsymbol\theta)]\tag{8.23}$$
The prediction is an average over all plausible θ, with plausibility given by p(θ) (p. 274).
- Comparison (p. 274). MLE/MAP yields a point estimate, and the key computation is optimization. Bayesian inference yields a posterior distribution, and the key computation is integration. Predictions with point estimates are straightforward. Bayesian predictions need another integral (8.23). Bayesian inference gives a principled way to include prior, side and structural knowledge, and uncertainty propagation helps risk assessment and data-efficient learning.
- If the prior is not conjugate (Sec. 6.6.1), the integrals in (8.22) and (8.23) are not analytically tractable. Approximations: MCMC (stochastic) or Laplace approximation, variational inference, expectation propagation (deterministic) (pp. 274–275). Applications listed include topic modeling, click-through-rate prediction, data-efficient reinforcement learning, online ranking and recommender systems. Bayesian optimization helps search model or algorithm meta-parameters (p. 275).
- A remark: the split between "variables" (marginalized out) and "parameters" (estimated) is somewhat arbitrary. A prior on any parameter turns it into a random variable (p. 275).

**8.4.3 Latent-variable models.**
- Latent variables z are extra variables that do not explicitly parametrize the model. They can aid interpretability, simplify structure and often reduce the number of parameters. Maximum-likelihood learning can use the EM algorithm. Examples: PCA (Ch. 10) and Gaussian mixture models (Ch. 11). Learning is generally hard (pp. 275–276).
- The generative process is given by
$$p(\boldsymbol x\mid\boldsymbol z,\boldsymbol\theta)\tag{8.24}$$
with a prior p(z) on z.
- Two-step learning procedure (p. 276). First compute the likelihood by marginalizing out z:
$$p(\boldsymbol x\mid\boldsymbol\theta)=\int p(\boldsymbol x\mid\boldsymbol z,\boldsymbol\theta)p(\boldsymbol z)\,d\boldsymbol z\tag{8.25}$$
The likelihood depends only on x and θ, not on z. Second, use it exactly as in Secs. 8.3 and 8.4.2 (MLE, MAP, or Bayes with prior p(θ)):
$$p(\boldsymbol\theta\mid\mathcal X)=\frac{p(\mathcal X\mid\boldsymbol\theta)p(\boldsymbol\theta)}{p(\mathcal X)}\tag{8.26}$$
- Except for a conjugate prior p(z) for p(x | z, θ), the marginalization (8.25) is not analytically tractable, and approximations are needed (p. 276).
- The posterior on the latent variables is
$$p(\boldsymbol z\mid\mathcal X)=\frac{p(\mathcal X\mid\boldsymbol z)p(\boldsymbol z)}{p(\mathcal X)},\qquad p(\mathcal X\mid\boldsymbol z)=\int p(\mathcal X\mid\boldsymbol z,\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta\tag{8.27}$$
Marginalizing out both z and θ at the same time is not possible in general. A more tractable quantity is the posterior on z conditioned on θ:
$$p(\boldsymbol z\mid\mathcal X,\boldsymbol\theta)=\frac{p(\mathcal X\mid\boldsymbol z,\boldsymbol\theta)p(\boldsymbol z)}{p(\mathcal X\mid\boldsymbol\theta)}\tag{8.28}$$
Chapters 10 and 11 derive the likelihoods and these posteriors for PCA and Gaussian mixtures (p. 277).
- Later chapters may loosely call θ "latent" or "hidden". Where both types appear (Ch. 10, 11), the difference is kept (p. 277).

**8.4.4 Further reading (summary).** Analytic solutions are rare in general, so sampling and variational inference are used. Probabilistic programming languages treat program variables as random variables and apply Bayesian inference automatically (pp. 277–278).

> **Intuition note.** MLE/MAP ask for the single best parameter, which is an optimization. Bayesian inference keeps all plausible parameters weighted by the posterior, which is an integration. The price of keeping everything is that those integrals usually have no closed form.

### 8.5 Directed Graphical Models
A directed graphical model (Bayesian network) is a compact way to specify a probabilistic model. It shows how the joint factorizes into factors depending on subsets of the variables, and shows independence structure that the joint alone does not show. Nodes are random variables, and edges are probabilistic relations such as conditional probabilities. Not every distribution can be represented by a given choice of graphical model. The graph is a simple visualization, can motivate new models, shows conditional independence by inspection, and lets inference be expressed as graph manipulations (p. 278).

**8.5.1 Graph semantics.**
An arrow from a to b gives the conditional p(b | a). With additional assumptions, arrows can indicate causal relationships (a margin note citing Pearl, 2009) (p. 279).

*Example 8.7.* The joint
$$p(a,b,c)=p(c\mid a,b)p(b\mid a)p(a)\tag{8.29}$$
says c depends directly on a and b, b depends directly on a, and a depends on neither b nor c. This gives Fig. 8.9(a) (fully connected) (p. 279).

Construction from a factorized joint: (1) create a node per random variable; (2) for each conditional distribution, add arrows from the nodes it is conditioned on. The layout depends on the chosen factorization (p. 279).

*Example 8.8 (the reverse direction).* The joint is a product of one conditional per node, each depending only on the node's parents. For Fig. 8.9(b):
$$p(x_1,x_2,x_3,x_4,x_5)=p(x_1)p(x_5)p(x_2\mid x_5)p(x_3\mid x_1,x_2)p(x_4\mid x_2)\tag{8.30}$$
In general:
$$p(\boldsymbol x)=\prod_{k=1}^K p(x_k\mid \mathrm{Pa}_k)\tag{8.31}$$
where Pa_k are the parent nodes of x_k, the nodes with arrows pointing to x_k (p. 280).

*Coin-flip example (pp. 280–281).* One flip has p(x | μ) = Ber(μ) (8.32). N independent flips give
$$p(x_1,\dots,x_N\mid\mu)=\prod_{n=1}^N p(x_n\mid\mu)\tag{8.33}$$
Independence means the distribution factorizes. Observed variables are drawn as shaded nodes (Fig. 8.10a), and the single μ is shared because the outcomes are identically distributed. Plate notation (Fig. 8.10b) repeats the enclosed node N times and is equivalent but more compact. A hyperprior is a second layer of priors on the parameters of the first layer. Fig. 8.10(c) puts a Beta(α, β) prior on the latent μ. Deterministic (non-random) α and β are drawn without a circle (p. 281).

**8.5.2 Conditional independence and d-separation.**
We want to decide from the graph whether
$$\mathcal A\perp\!\!\!\perp\mathcal B\mid\mathcal C\tag{8.34}$$
(A conditionally independent of B given C, for non-intersecting node sets A, B, C) is implied by a directed acyclic graph. Consider all trails (paths ignoring arrow direction) from any node in A to any node in B. A trail is blocked if it contains a node such that either (p. 281):
- the arrows meet head-to-tail or tail-to-tail at the node, and the node is in C; or
- the arrows meet head-to-head at the node, and neither the node nor any of its descendants is in C.

If all trails are blocked, A is d-separated from B by C, and the joint distribution will satisfy A ⊥⊥ B | C (p. 281).

*Example 8.9 (Fig. 8.11).* By visual inspection (p. 282):
$$b\perp\!\!\!\perp d\mid a,c\tag{8.35}$$
$$a\perp\!\!\!\perp c\mid b\tag{8.36}$$
$$b\not\!\perp\!\!\!\perp d\mid c\tag{8.37}$$
$$a\not\!\perp\!\!\!\perp c\mid b,e\tag{8.38}$$
The text gives these results without justification.

Graphical models let a probabilistic model be factorized into expressions that are easier to optimize and show the effect of structural design choices. Such structural assumptions (hyperparameters) cannot be selected directly by the methods so far, and Sec. 8.6 addresses this (p. 282).

**8.5.3 Further reading (summary).** Three main types of graphical models: directed (Bayesian networks), undirected (Markov random fields) and factor graphs (Fig. 8.12). They allow graph-based inference such as local message passing. Structured prediction is not covered in the book. Graphical models have renewed interest through causal inference (p. 283).

### 8.6 Model Selection
High-level choices (for example the functional form of the likelihood) set the number and type of free parameters, and so the model's flexibility. A polynomial of degree 2 can describe everything a degree-1 polynomial can (set a₂ = 0), and more (p. 283).

**Naive expectation (framed by the author):** very flexible models seem preferable because they are more expressive. The reply: at training time only the training set is available, performance on it is not what we want, and MLE can overfit, especially for small data. Model selection addresses assessing generalization (p. 284).

**8.6.1 Nested cross-validation.**
Apply cross-validation again inside each split (Fig. 8.13). The inner level estimates the performance of a model or hyperparameter choice on an internal validation set. The outer level estimates generalization performance for the best choice selected by the inner loop. To distinguish the levels, the outer set is often called the test set and the inner set the validation set. The inner loop approximates the expected generalization error of model M:
$$\mathbb E_{\mathcal V}[\mathbf R(\mathcal V\mid M)]\approx\frac1K\sum_{k=1}^K\mathbf R(\mathcal V^{(k)}\mid M)\tag{8.39}$$
Repeat for all models and pick the best. Cross-validation also gives higher-order statistics, such as the standard error σ/√K (K experiments, σ the standard deviation of the per-experiment risk). The final performance of the chosen model is evaluated on the test set (pp. 284–285).

**8.6.2 Bayesian model selection.**
- Approaches trade off model complexity and data fit. The assumption is that simpler models are less prone to overfitting, so the aim is the simplest model that explains the data reasonably well (Occam's razor) (p. 285). A remark adds that, viewed as hypothesis testing, one looks for the simplest hypothesis consistent with the data (p. 285).
- A prior favoring simple models is not necessary. An "automatic Occam's Razor" is embodied in Bayesian probability (p. 285).
- Fig. 8.14 (from MacKay): with a uniform prior over models, Bayes' theorem rewards models in proportion to how well they predicted the data that occurred. That prediction, p(D | M_i), is the evidence. A simple model M₁ predicts few datasets, so its evidence is high on them. A more powerful M₂ predicts more datasets but spreads probability thinner. Evidence integrates to 1 over datasets. For a dataset in region C, with equal priors, M₁ is the more probable model (pp. 285–286).
- Setup. Take models M = {M₁..M_K}, each with parameters θ_k, and a prior p(M). The generative process:
$$M_k\sim p(M)\tag{8.40}$$
$$\boldsymbol\theta_k\sim p(\boldsymbol\theta\mid M_k)\tag{8.41}$$
$$\mathcal D\sim p(\mathcal D\mid\boldsymbol\theta_k)\tag{8.42}$$
- The posterior over models:
$$p(M_k\mid\mathcal D)\propto p(M_k)p(\mathcal D\mid M_k)\tag{8.43}$$
with the model evidence (marginal likelihood)
$$p(\mathcal D\mid M_k)=\int p(\mathcal D\mid\boldsymbol\theta_k)p(\boldsymbol\theta_k\mid M_k)\,d\boldsymbol\theta_k\tag{8.44}$$
and the MAP model
$$M^*=\arg\max_{M_k}p(M_k\mid\mathcal D)\tag{8.45}$$
With a uniform prior p(M_k) = 1/K, this means picking the model that maximizes the evidence (p. 286).
- Remark: the likelihood is prone to overfitting. The marginal likelihood typically is not, since parameters are marginalized out, and it automatically embodies a trade-off between complexity and data fit (p. 286).

**8.6.3 Bayes factors.**
$$\underbrace{\frac{p(M_1\mid\mathcal D)}{p(M_2\mid\mathcal D)}}_{\text{posterior odds}}=\underbrace{\frac{p(M_1)}{p(M_2)}}_{\text{prior odds}}\underbrace{\frac{p(\mathcal D\mid M_1)}{p(\mathcal D\mid M_2)}}_{\text{Bayes factor}}\tag{8.46}$$
(the intermediate form divides both posteriors by p(D), which cancels). The prior odds measure how prior beliefs favor M₁ over M₂. The Bayes factor measures how well D is predicted by M₁ compared with M₂ (p. 287).

A remark quotes Murphy (2012) for the Jeffreys–Lindley paradox: the Bayes factor "always favors the simpler model", because data probability under a complex model with a diffuse prior is very small (p. 287).

With a uniform prior over models the prior odds are 1, and the posterior odds equal the Bayes factor
$$\frac{p(\mathcal D\mid M_1)}{p(\mathcal D\mid M_2)}\tag{8.47}$$
If it exceeds 1, choose M₁, otherwise M₂. There are guidelines on how large the ratio should be before "significance" (p. 287).

Remark on computing the marginal likelihood: it needs the integral (8.44), generally intractable. Approximations include numerical integration, Monte Carlo and Bayesian Monte Carlo. With a conjugate prior it is available in closed form, which Ch. 9 does for linear regression (p. 287).

> **Intuition note.** The evidence asks how probable the observed data are if we average over all the parameter values a model allows. A very flexible model spreads its probability over many datasets, so it assigns less to any single one. This is why complexity is penalized without an explicit penalty.

**8.6.4 Further reading.**
- Examples of high-level choices: polynomial degree, number of mixture components, neural-network architecture, kernel type, dimension of the PCA latent space, learning-rate schedule (p. 288).
- Rasmussen and Ghahramani (2001) showed that the automatic Occam's razor does not necessarily penalize the number of parameters but is active in terms of function complexity. It also holds for Bayesian nonparametric models with many parameters, for example Gaussian processes (p. 288).
- Information criteria (choose the model with the largest value) work with the maximum likelihood estimate. With M the number of model parameters:
$$\text{AIC: } \log p(\boldsymbol x\mid\boldsymbol\theta)-M\tag{8.48}$$
With N the number of data points (for exponential-family distributions):
$$\text{BIC: } \log p(\boldsymbol x)=\log\int p(\boldsymbol x\mid\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta\approx\log p(\boldsymbol x\mid\boldsymbol\theta)-\tfrac12M\log N\tag{8.49}$$
BIC penalizes model complexity more heavily than AIC (p. 288).

## Toy example
*(Our own, not from the text.)* One feature, no intercept: f(x) = θx. Data: (x₁,y₁) = (1,1) and (x₂,y₂) = (2,3). N = 2.

**ERM, squared loss.** R(θ) = ½[(1−θ)² + (3−2θ)²]. Derivative: ½[−2(1−θ) − 4(3−2θ)] = −(1−θ) − 2(3−2θ) = −1 + θ − 6 + 4θ = 5θ − 7. Setting it to 0 gives θ* = 7/5 = 1.4. Training predictions: 1.4 and 2.8, with squared errors 0.16 and 0.04.

**MLE, Gaussian noise with σ = 1.** By (8.18d), L(θ) = ½Σ(y_n − θx_n)² + constant. Its derivative is 5θ − 7, so θ_ML = 1.4, the same as ERM.

**Regularized ERM (8.12).** Minimize ½[(1−θ)² + (3−2θ)²] + λθ². The derivative is 5θ − 7 + 2λθ, so θ = 7/(5 + 2λ). For λ = 0.5, θ = 7/6 ≈ 1.167, closer to 0 than 1.4.

**MAP (added step).** For a prior θ ∼ N(0, τ²), −log p(θ) = θ²/(2τ²) + const. The derivative of the negative log-posterior is 5θ − 7 + θ/τ², so θ_MAP = 7/(5 + 1/τ²). For τ² = 1 this gives 7/6, the same as λ = 0.5 above, because 2λ = 1/τ². This matches the book's statement that a prior plays the role of a regularizer (p. 269). The explicit correspondence is our computation.

## Concepts
- [[model]] (new) — a predictor as a function or as a probability model (pp. 251, 255–256)
- [[feature-map]] (new) — φ(·): lifts x_n to a higher-dimensional nonlinear representation (p. 254)
- [[empirical-risk-minimization]] (new) — choose parameters minimizing the average training loss (8.6) (pp. 258, 260)
- [[loss-function]] (new) — ℓ(y, ŷ), a non-negative error for one prediction (p. 260)
- [[expected-risk]] (new) — R_true(f) = E[ℓ(y, f(x))], risk under the full data distribution (p. 261)
- [[least-squares]] — minimize (1/N)‖y − Xθ‖² (8.9); closed form via normal equations in Ch. 9 (p. 261)
- [[overfitting]] (new) — low training risk but much higher test risk (pp. 262, 271)
- [[underfitting]] (new) — the model class is too poor to approach the true model (p. 271)
- [[regularization]] (new) — penalty (here λ‖θ‖²) trading data fit against parameter size (p. 263)
- [[cross-validation]] (new) — K-fold estimate of generalization error, (8.13) (p. 263)
- [[nested-cross-validation]] (new) — an inner loop selects a model, an outer loop assesses it (p. 284)
- [[maximum-likelihood-estimation]] (new) — minimize the negative log-likelihood (8.17) over θ (pp. 265–267)
- [[maximum-a-posteriori-estimation]] (new) — minimize the negative log-posterior; the prior acts like a regularizer (p. 269)
- [[bayesian-inference]] (new) — compute the full posterior p(θ | X) (8.22) and predict by (8.23) (p. 274)
- [[latent-variable-model]] (new) — extra unobserved z; the likelihood marginalizes it out (8.25) (pp. 275–276)
- [[directed-graphical-model]] (new) — a joint factorized as ∏ p(x_k | Pa_k) (8.31) (pp. 278–280)
- [[d-separation]] (new) — graph criterion implying conditional independence (8.34) (p. 281)
- [[model-evidence]] (new) — p(D | M) = ∫ p(D | θ)p(θ | M) dθ, the marginal likelihood (8.44) (p. 286)
- [[bayes-factor]] (new) — ratio of evidences p(D | M₁)/p(D | M₂) (8.46) (p. 287)
- [[information-criteria]] (new) — AIC (8.48) and BIC (8.49), penalized log-likelihoods (p. 288)

## Canonical instances
- [[salary-from-age-regression]] — toy dataset of Tables 8.1/8.2 and Fig. 8.1, with the prediction at x = 60 (pp. 252–254)
- [[gaussian-likelihood-linear-regression]] — Gaussian noise gives least squares (Ex. 8.4–8.5) (pp. 266–267)
- [[coin-flip-bernoulli]] — Bernoulli with parameter μ, repeated flips, plate notation, Beta hyperprior (pp. 273, 280–281)
- [[polynomial-overfitting-demo]] — Fig. 8.8: overfitting, underfitting and a good fit (p. 271)
- [[d-separation-example-8-9]] — Fig. 8.11 with four independence statements (p. 282)
- [[evidence-occam-figure]] — Fig. 8.14: why a simple model can have higher evidence (pp. 285–286)

## Bridges (candidates)
- [same-math] Least-squares ERM (8.9) ↔ linear-algebra: least squares by projecting y onto the column space of X (the book defers the closed form to Sec. 9.2 (p. 261); the projection reading is from the field list, not this unit).
- [same-math] Squared-loss ERM ↔ Gaussian MLE: with σ fixed, (8.18d) equals (8.8) up to a constant and a positive factor, so the minimizers coincide.
- [structural-analogy] Regularizer λ‖θ‖² ↔ probability: zero-mean Gaussian prior on θ — both bias θ toward the origin (p. 263, 269).
- [structural-analogy] Graphical model factorization ∏ p(x_k | Pa_k) ↔ graph theory: acyclic directed graph where each node's factor depends only on its parents.
- [metaphor] Evidence and Occam's razor ↔ philosophy of science: prefer the simplest hypothesis consistent with the data (p. 285).

## Questions this raises
- Why does the Gaussian prior give exactly the squared-norm penalty, and how is λ linked to σ² and the prior covariance (Ch. 9)?
- When are posterior integrals available in closed form (conjugacy), and what approximations replace them otherwise?
- How reliable is K-fold cross-validation when the number of folds or the data size is small, given the two error sources the book names (p. 264)?
- What do the Jeffreys–Lindley remark and the diffuse prior imply for using Bayes factors in practice (p. 287)?

## Reading notes
- Printed page = pdf page − 6 (pdf 257 = printed 251). Page images were used; the text layer garbles some stacked layouts, notably equation (8.46), which was read from the image.
- Running footers show "Draft (2024-01-15) of 'Mathematics for Machine Learning'" and "©2024 … Published by Cambridge University Press (2020)". Running header: "When Models Meet Data".
- Sec. 8.2.4 calls test data "also sometimes referred to as the validation set". Sec. 8.6.1 then distinguishes validation set (inner loop) from test set (outer loop). The usage is not consistent between the two sections.
- On p. 282, Fig. 8.12 appears before Fig. 8.11 in layout. Fig. 8.12 is cited in Sec. 8.5.3 and Fig. 8.11 in Example 8.9.
- The results (8.35)–(8.38) are stated "by visual inspection" without derivation. I checked them against the d-separation rules and Fig. 8.11 (arrows a→b, b→c, a→d, c→d, d→e) and they agree.
- This unit contains no exercises, so the exercises section is omitted. The "Further Reading" subsections mainly list references, so I only summarized the substantive statements.
