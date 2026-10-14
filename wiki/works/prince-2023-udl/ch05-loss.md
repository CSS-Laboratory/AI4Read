---
id: prince-2023-udl/ch05-loss
work: prince-2023-udl
unit: "Chapter 5 — Loss functions"
pages: 56-76
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
# Loss functions (maximum likelihood, negative log-likelihood, cross-entropy)

## L0 — One line
Treat the network as outputting the parameters of a probability distribution over the label, then train by minimizing the negative log-likelihood of the training data. This yields least squares, binary cross-entropy and multiclass cross-entropy as special cases.

## L1 — The gist (≤ 120 words)
The chapter asks what "best possible mapping" means when training a model. Answer: the model predicts a distribution Pr(y|θ) over outputs. We choose parameters that make the observed training outputs most probable. In practice we minimize the negative log-likelihood. Choosing a normal distribution gives least squares. Choosing a Bernoulli distribution with a sigmoid gives binary cross-entropy. Choosing a categorical distribution with a softmax gives multiclass cross-entropy. Independent outputs add their losses. Minimizing the distance (KL divergence) between the empirical data distribution and the model gives the same criterion, which is why the loss is also called "cross-entropy". Next-word prediction is a K-class case.

**Prerequisites:** conditional probability; independence (product rule); logarithms and exponentials; what a neural network f[x, ϕ] is; argmin/argmax.

## L2 — Key ideas
- The model f[x, ϕ] computes parameters θ of a distribution Pr(y|θ), not a bare prediction. The loss rewards high probability for each true training output (p. 56, p. 58).
- Maximum likelihood implicitly assumes the same distribution form for every data point and independent conditional distributions; independence makes the total likelihood a product (p. 58).
- Maximizing the likelihood and maximizing the log-likelihood give the same best parameters, because log is monotonically increasing. A sum is numerically safer than a product. Multiplying by −1 gives the loss to minimize (p. 59–60).
- A four-step recipe builds a maximum-likelihood loss for a given prediction type: choose a distribution, let the network predict its parameters, minimize the negative log-likelihood, infer with the full distribution or its maximum (p. 60).
- A normal distribution with a predicted mean, together with independent examples, gives least squares. Learning σ² (the variance) gives an estimate of the uncertainty of the prediction. Making σ² depend on x gives heteroscedastic regression, where the uncertainty varies with the input (p. 62–64).
- Bernoulli (a distribution on {0,1}) plus sigmoid (a function that maps any real number into [0,1]) gives binary cross-entropy. Categorical (a distribution over K classes) plus softmax (a function that maps K scores to K probabilities that sum to one) gives multiclass cross-entropy. Other data types call for other distributions (p. 66–70).
- For vector outputs, usually assume independence, so negative log-likelihoods sum over outputs (p. 69–70).
- Minimizing KL divergence between the empirical distribution and the model gives the same criterion as negative log-likelihood (p. 71–72).

## L3 — Walkthrough

### Opening (p. 56)
- A loss (cost) function L[ϕ] returns one number measuring the mismatch between predictions f[xᵢ, ϕ] and ground truth yᵢ. Training seeks ϕ that minimizes it. Chapter 2's least squares loss suits real-valued y (p. 56).
- The chapter gives a framework that justifies least squares and builds losses for other prediction types: binary classification y ∈ {0,1}, multiclass y ∈ {1,…,K}, and more (p. 56).

### 5.1 Maximum likelihood
**Shift of view.** The model computes a conditional distribution Pr(y|x) over outputs. The loss encourages each training yᵢ to have high probability under Pr(yᵢ|xᵢ) (p. 56). Figure 5.1 shows the model predicting a different distribution for each x for four output types: real values, discrete classes, counts, and directions (circular domain) (p. 57).

**5.1.1 Computing a distribution.** Choose a parametric distribution Pr(y|θ) on the output domain. The network computes one or more of its parameters θ (p. 58).
- Example: for y ∈ ℝ choose the univariate normal, θ = {μ, σ²}. The model may predict μ and treat σ² as an unknown constant (p. 58).

**5.1.2 Maximum likelihood criterion.** Each input gives θᵢ = f[xᵢ, ϕ]. Choose ϕ to maximize the combined probability over all I examples:
$$\hat{\phi}=\operatorname*{argmax}_{\phi}\Big[\prod_{i=1}^{I}Pr(y_i|x_i)\Big]=\operatorname*{argmax}_{\phi}\Big[\prod_{i=1}^{I}Pr(y_i|\theta_i)\Big]=\operatorname*{argmax}_{\phi}\Big[\prod_{i=1}^{I}Pr(y_i|f[x_i,\phi])\Big]\tag{5.1}$$
(p. 58). The product is the *likelihood* of the parameters, so this is the *maximum likelihood criterion*. Footnote: as a function of z, Pr(z|ψ) is a distribution that sums to one; as a function of ψ it is a likelihood and does not generally sum to one (p. 58).

Two implicit assumptions (p. 58):
1. The form of the distribution over yᵢ is the same for every data point.
2. The conditionals Pr(yᵢ|xᵢ) are independent, so
$$Pr(y_1,\dots,y_I|x_1,\dots,x_I)=\prod_{i=1}^{I}Pr(y_i|x_i)\tag{5.2}$$

**5.1.3 Log-likelihood.** The product of many small terms can be tiny and hard to represent in finite-precision arithmetic (p. 59). Since log is monotonically increasing (z > z′ if and only if log z > log z′), the maximizer is unchanged (figure 5.2):
$$\hat{\phi}=\operatorname*{argmax}_{\phi}\Big[\prod_{i}Pr(y_i|f[x_i,\phi])\Big]=\operatorname*{argmax}_{\phi}\Big[\log\prod_{i}Pr(y_i|f[x_i,\phi])\Big]=\operatorname*{argmax}_{\phi}\Big[\sum_{i=1}^{I}\log Pr(y_i|f[x_i,\phi])\Big]\tag{5.3}$$
Improving one criterion improves the other, and the best ϕ̂ is the same. The sum form avoids the precision problem (p. 59).

*Intuition note:* Taking logs turns a product of tiny numbers into a sum of terms that is easy to represent in finite-precision arithmetic. Because log never reverses order, the best parameters stay the same.

**5.1.4 Negative log-likelihood.** By convention we minimize, so multiply by −1:
$$\hat{\phi}=\operatorname*{argmin}_{\phi}\Big[-\sum_{i=1}^{I}\log Pr(y_i|f[x_i,\phi])\Big]=\operatorname*{argmin}_{\phi}\big[L[\phi]\big]\tag{5.4}$$
This forms the final loss L[ϕ] (p. 60).

**5.1.5 Inference.** The network gives a distribution, so for a point estimate we return its maximum:
$$\hat{y}=\operatorname*{argmax}_{y}\big[Pr(y|f[x,\hat\phi])\big]\tag{5.5}$$
This can usually be written in terms of the predicted θ. For the normal distribution the maximum is at μ (p. 60).

### 5.2 Recipe (p. 60)
1. Choose a distribution Pr(y|θ) over the domain of y.
2. Let the model predict one or more parameters: θ = f[x, ϕ].
3. Train by minimizing
$$\hat\phi=\operatorname*{argmin}_{\phi}[L[\phi]]=\operatorname*{argmin}_{\phi}\Big[-\sum_{i=1}^{I}\log Pr(y_i|f[x_i,\phi])\Big]\tag{5.6}$$
4. For a new x, return the full distribution Pr(y|f[x, ϕ̂]) or the value where it is maximized.

*Intuition note:* Between tasks, what mainly changes is the choice of distribution, which parameters the network predicts, and how those parameters are kept valid (for example by a sigmoid or softmax). The steps of the recipe stay the same.

### 5.3 Example 1: univariate regression (p. 61–64)
Choose the univariate normal (figure 5.3: μ sets the peak position, the standard deviation sets the width, and a narrower curve has a higher peak):
$$Pr(y|\mu,\sigma^2)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Big[-\frac{(y-\mu)^2}{2\sigma^2}\Big]\tag{5.7}$$
Set μ = f[x, ϕ]:
$$Pr(y|f[x,\phi],\sigma^2)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Big[-\frac{(y-f[x,\phi])^2}{2\sigma^2}\Big]\tag{5.8}$$
$$L[\phi]=-\sum_{i=1}^{I}\log\Big[\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Big[-\frac{(y_i-f[x_i,\phi])^2}{2\sigma^2}\Big]\Big]\tag{5.9}$$
(p. 61).

**5.3.1 Least squares.** Algebra (p. 62):
$$\hat\phi=\operatorname*{argmin}_\phi\Big[-\sum_i\Big(\log\frac{1}{\sqrt{2\pi\sigma^2}}-\frac{(y_i-f[x_i,\phi])^2}{2\sigma^2}\Big)\Big]=\operatorname*{argmin}_\phi\Big[-\sum_i-\frac{(y_i-f[x_i,\phi])^2}{2\sigma^2}\Big]=\operatorname*{argmin}_\phi\Big[\sum_i(y_i-f[x_i,\phi])^2\Big]\tag{5.10}$$
The first term is dropped because it does not depend on ϕ. The denominator 2σ² is dropped because it is a positive constant scale factor that does not move the minimum. The result is
$$L[\phi]=\sum_{i=1}^{I}\big(y_i-f[x_i,\phi]\big)^2\tag{5.11}$$
So least squares follows from assuming the predictions are (i) independent and (ii) drawn from a normal distribution with mean μ = f[xᵢ, ϕ] (p. 62).

Figure 5.4 compares a good and a bad linear fit (p. 63):
- Good fit: Σ(yᵢ−f)² = 0.19 and −Σ log Pr = −6.57.
- Bad fit: Σ(yᵢ−f)² = 10.22 and −Σ log Pr = 497.37.

**5.3.2 Inference.** ŷ = argmax_y Pr(y|f[x, ϕ̂], σ²) (5.12). For the normal this is the mean, which the model computed, so ŷ = f[x, ϕ̂] (p. 62).

**5.3.3 Estimating variance.** Eq. 5.11 does not depend on σ², but σ² can be treated as a learned parameter, minimizing 5.9 over both ϕ and σ²:
$$\hat\phi,\hat\sigma^2=\operatorname*{argmin}_{\phi,\sigma^2}\Big[-\sum_i\log\Big[\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Big[-\frac{(y_i-f[x_i,\phi])^2}{2\sigma^2}\Big]\Big]\Big]\tag{5.13}$$
At inference the mean f[x, ϕ̂] is the best prediction, and σ̂² tells us about the uncertainty of the prediction (p. 64).

**5.3.4 Heteroscedastic regression.** *Heteroscedastic* means the uncertainty varies with the input; *homoscedastic* means it is constant. A network with two outputs predicts the mean (f₁) and the variance (f₂). Variance must be positive, so pass f₂ through a function mapping any value to a positive one. The author suggests squaring (p. 64):
$$\mu=f_1[x,\phi],\qquad \sigma^2=f_2[x,\phi]^2\tag{5.14}$$
$$\hat\phi=\operatorname*{argmin}_\phi\Big[-\sum_{i=1}^{I}\Big(\log\Big[\frac{1}{\sqrt{2\pi f_2[x_i,\phi]^2}}\Big]-\frac{(y_i-f_1[x_i,\phi])^2}{2f_2[x_i,\phi]^2}\Big)\Big]\tag{5.15}$$
Figure 5.5: in the homoscedastic network the mean is piecewise linear in x but the ±2σ band has constant width. In the heteroscedastic network the standard deviation is also piecewise linear in x (p. 65).

*Intuition note:* Least squares is not a separate idea. It is maximum likelihood when the labels are independent and normal around the model output with a fixed spread. Letting the spread be learned (or depend on x) gives an estimate of the prediction's uncertainty.

### 5.4 Example 2: binary classification (p. 64–67)
Labels y ∈ {0,1}, for example review sentiment or tumor present/absent (p. 64). Use the Bernoulli distribution with parameter λ ∈ [0,1] = Pr(y=1) (figure 5.6):
$$Pr(y|\lambda)=\begin{cases}1-\lambda&y=0\\ \lambda&y=1\end{cases}\tag{5.16}$$
$$Pr(y|\lambda)=(1-\lambda)^{1-y}\cdot\lambda^{y}\tag{5.17}$$
The network output cannot be guaranteed to lie in [0,1], so pass it through the logistic sigmoid (figure 5.7; 0 maps to 0.5):
$$\mathrm{sig}[z]=\frac{1}{1+\exp[-z]}\tag{5.18}$$
Set λ = sig[f[x, ϕ]]:
$$Pr(y|x)=(1-\mathrm{sig}[f[x,\phi]])^{1-y}\cdot \mathrm{sig}[f[x,\phi]]^{y}\tag{5.19}$$
$$L[\phi]=\sum_{i=1}^{I}-(1-y_i)\log\big[1-\mathrm{sig}[f[x_i,\phi]]\big]-y_i\log\big[\mathrm{sig}[f[x_i,\phi]]\big]\tag{5.20}$$
This is the *binary cross-entropy loss* (name explained in 5.7) (p. 66). For a point estimate, set y = 1 if λ > 0.5, otherwise y = 0 (p. 66). Figure 5.8: the loss favors large λ at xᵢ with yᵢ = 1 and small λ at xᵢ with yᵢ = 0 (p. 67).

### 5.5 Example 3: multiclass classification (p. 67–69)
y ∈ {1,…,K}, K > 2. Examples: which of K = 10 digits is in an image; which of K possible words follows an incomplete sentence (p. 67). Use the categorical distribution (figure 5.9) with parameters λ₁…λ_K:
$$Pr(y=k)=\lambda_k\tag{5.21}$$
Each λ_k must lie in [0,1] and they must sum to one (p. 68). The network has K outputs, passed through the softmax:
$$\mathrm{softmax}_k[z]=\frac{\exp[z_k]}{\sum_{k'=1}^{K}\exp[z_{k'}]}\tag{5.22}$$
The exponentials ensure positivity; the denominator ensures the sum is one (p. 68).
$$Pr(y=k|x)=\mathrm{softmax}_k\big[f[x,\phi]\big]\tag{5.23}$$
$$L[\phi]=-\sum_{i=1}^{I}\log\big[\mathrm{softmax}_{y_i}[f[x_i,\phi]]\big]=-\sum_{i=1}^{I}\Big(f_{y_i}[x_i,\phi]-\log\Big[\sum_{k'=1}^{K}\exp[f_{k'}[x_i,\phi]]\Big]\Big)\tag{5.24}$$
where f_{yᵢ} and f_{k′} are the yᵢ-th and k′-th network outputs. This is the *multiclass cross-entropy loss*. The point estimate is the most probable category ŷ = argmax_k Pr(y=k|f[x, ϕ̂]) (p. 69). (The second line of 5.24 is the author's own rewriting. No intermediate step is shown.)

*Intuition note:* The network outputs raw scores. The softmax turns them into probabilities. The loss is the negative log of the probability given to the true class.

**5.5.1 Other data types.** Choose a distribution suited to the domain and apply the recipe. Figure 5.11 pairs data types, distributions and uses (p. 69–70):

| Domain | Distribution | Use |
|---|---|---|
| ℝ | univariate normal | regression |
| ℝ | Laplace or t | robust regression |
| ℝ | mixture of Gaussians | multimodal regression |
| ℝ⁺ | exponential or gamma | predicting magnitude |
| [0,1] | beta | predicting proportions |
| ℝᴷ | multivariate normal | multivariate regression |
| (−π, π] | von Mises | predicting direction |
| {0,1} | Bernoulli | binary classification |
| {1,…,K} | categorical | multiclass classification |
| {0,1,2,…} | Poisson | predicting event counts |
| permutations of {1,…,K} | Plackett-Luce | ranking |

### 5.6 Multiple outputs (p. 69–70)
For vector targets y (for example a molecule's melting and boiling points; the object class at every pixel), it is more usual to treat predictions as independent than to use a multivariate distribution (p. 69):
$$Pr(y|f[x,\phi])=\prod_d Pr(y_d|f_d[x,\phi])\tag{5.25}$$
Here f_d are the network outputs that set the parameters of the distribution over y_d. Continuous y_d: a normal for each, with f_d predicting the means. Discrete y_d: a categorical for each, with f_d predicting its K values. The product becomes a sum under the negative log:
$$L[\phi]=-\sum_{i=1}^{I}\log Pr(y_i|f[x_i,\phi])=-\sum_{i=1}^{I}\sum_d\log Pr(y_{id}|f_d[x_i,\phi])\tag{5.26}$$
(p. 70). Different prediction types can be combined under the same independence assumption. Example: wind direction (von Mises) plus strength (exponential). The joint likelihood is the product of the two, and the negative log-likelihoods add (p. 70).

### 5.7 Cross-entropy loss (p. 71–72)
Claim: the cross-entropy loss is equivalent to negative log-likelihood (p. 71).
- Idea: find θ minimizing the distance between the empirical data distribution q(y) and the model Pr(y|θ) (figure 5.12). Distance is measured by the KL divergence:
$$D_{KL}[q\|p]=\int_{-\infty}^{\infty}q(z)\log[q(z)]dz-\int_{-\infty}^{\infty}q(z)\log[p(z)]dz\tag{5.27}$$
- Empirical distribution as point masses (Dirac delta δ[•]):
$$q(y)=\frac1I\sum_{i=1}^{I}\delta[y-y_i]\tag{5.28}$$
- Minimize the KL divergence to the model (p. 71):
$$\hat\theta=\operatorname*{argmin}_\theta\Big[\int q(y)\log[q(y)]dy-\int q(y)\log[Pr(y|\theta)]dy\Big]=\operatorname*{argmin}_\theta\Big[-\int_{-\infty}^{\infty}q(y)\log[Pr(y|\theta)]dy\Big]\tag{5.29}$$
- The first term has no dependence on θ and is dropped. The remaining term is the *cross-entropy*, which the author describes as the uncertainty remaining in one distribution after accounting for what we know from the other (p. 72).
- Substituting 5.28 (the delta functions leave weighted masses at the data points; 1/I is dropped as a constant that does not move the minimum) (p. 72):
$$\hat\theta=\operatorname*{argmin}_\theta\Big[-\int\Big(\frac1I\sum_i\delta[y-y_i]\Big)\log[Pr(y|\theta)]dy\Big]=\operatorname*{argmin}_\theta\Big[-\frac1I\sum_i\log[Pr(y_i|\theta)]\Big]=\operatorname*{argmin}_\theta\Big[-\sum_i\log[Pr(y_i|\theta)]\Big]\tag{5.30}$$
- With θ = f[xᵢ, ϕ]:
$$\hat\phi=\operatorname*{argmin}_\phi\Big[-\sum_{i=1}^{I}\log[Pr(y_i|f[x_i,\phi])]\Big]\tag{5.31}$$
This is precisely the negative log-likelihood of the recipe. So the two criteria are equivalent (p. 72).

*Intuition note:* "Make the data likely" and "make the model distribution close to the data distribution" lead to the same minimization problem. That is why classification losses are called cross-entropy.

### 5.8 Summary (p. 72–73)
The chapter moved from networks that predict y directly to networks that compute θ of Pr(y|θ). Least squares is a natural consequence of the normal assumption with predicted mean. Regression can be extended with learned or input-dependent uncertainty. The same approach gives binary and multiclass classification losses. The next chapter addresses finding parameters that minimize these losses (p. 73).

### Notes (p. 73–74)
Pointers to the literature, as summarized by the author:
- **Robust regression:** minimizing mean absolute error follows from assuming a Laplace distribution and estimates the median rather than the mean (p. 73).
- **Quantile regression:** quantile (pinball) loss minimizes absolute deviations but weights one direction more than the other (p. 73).
- **Class imbalance:** focal loss adds one parameter that down-weights well-classified examples (p. 73).
- **Learning to rank:** the Plackett-Luce model is used in listwise approaches (p. 73).
- **Mixture density networks:** model multimodal output as a mixture of Gaussians conditional on the input (figure 5.14) (p. 73–74).
- **Non-probabilistic losses:** the probabilistic approach is "not strictly necessary". Any loss that reduces a sensible distance suffices. Examples are hinge loss (support vector machines) and exponential loss (AdaBoost) (p. 74).

## Toy example (ours, not from the text)
Three classes (K = 3). Suppose the network outputs the same scores for two training examples: f = (2, 0, −1). Their labels are y₁ = 1 and y₂ = 3.

1. Exponentials: e² ≈ 7.389, e⁰ = 1, e⁻¹ ≈ 0.368. Sum ≈ 8.757.
2. Softmax (eq. 5.22): λ ≈ (7.389/8.757, 1/8.757, 0.368/8.757) ≈ (0.844, 0.114, 0.042). These sum to 1.000.
3. Loss per example via eq. 5.24: log 8.757 ≈ 2.170.
   - y = 1: −(2 − 2.170) = 0.170.
   - y = 3: −(−1 − 2.170) = 3.170.
   - Total L ≈ 3.340.
4. Cross-entropy check (5.30): the empirical q puts mass ½ on class 1 and ½ on class 3. Then −Σ q log p = ½(0.170) + ½(3.170) = 1.670. Multiplying by I = 2 gives 3.340, the same as the total loss. So minimizing the negative log-likelihood and minimizing the cross-entropy rank parameters the same way.
5. Inference: the highest probability is class 1 (0.844), so ŷ = 1. The confident wrong guess on example 2 costs far more than the confident right guess on example 1.

## Concepts
- [[loss-function]] (new) — one number measuring mismatch between model outputs and training targets; training minimizes it (p. 56)
- [[maximum-likelihood]] (new) — choose parameters that maximize the product of probabilities of the training outputs; assumes same form and independence (p. 58)
- [[negative-log-likelihood]] (new) — minus the sum of log-probabilities of the true outputs; the loss the recipe produces (p. 60)
- [[cross-entropy-log-loss]] — in this chapter, the negative log-likelihood, shown equivalent to minimizing KL divergence to the empirical distribution (p. 72)
- [[kl-divergence]] (new) — measure of distance between two distributions, eq. 5.27 (p. 71)
- [[softmax]] — maps K arbitrary scores to K non-negative numbers summing to one (p. 68)
- [[sigmoid-function]] (new) — maps ℝ to [0,1]; used to make the Bernoulli parameter λ (p. 66)
- [[heteroscedastic-regression]] (new) — regression where the predicted variance depends on the input (p. 64)
- [[bernoulli-distribution]] (new) — distribution on {0,1} with parameter λ = Pr(y=1) (p. 66)
- [[categorical-distribution]] (new) — distribution over K classes with parameters λₖ in [0,1] summing to one (p. 67)
- [[language-model]] — not defined here; the chapter's K-class example of predicting the next word is one case (p. 67)

## Canonical instances
- [[least-squares-regression-as-gaussian-mle]] (new) — least squares follows from normal distribution with predicted mean and independence (p. 62)
- [[binary-cross-entropy]] (new) — Bernoulli with sigmoid, eq. 5.20 (p. 66)
- [[multiclass-cross-entropy]] (new) — categorical with softmax, eq. 5.24; includes predicting which word follows a sentence (p. 67–69)
- [[wind-direction-prediction]] (new) — von Mises for direction plus exponential for strength, independent (p. 70)

## Bridges (candidates)
- [same-math] Multiclass cross-entropy, eq. 5.24 ↔ llm: next-token loss, a softmax over the vocabulary and the negative log-probability of the true token — the chapter names next-word prediction as a K-class case (p. 67).
- [structural-analogy] Negative log-likelihood / cross-entropy ↔ llm: canon's "cross-entropy / log-loss" and "perplexity (exp of cross-entropy)" — perplexity is the exponential of this loss (canon link; not stated in this unit).
- [structural-analogy] Pairwise preference modeling with sigmoid ↔ llm: Bradley–Terry reward models also use σ(·) to turn a score difference into a probability; the chapter shows only sigmoid-to-Bernoulli (canon link; not stated in this unit).

## Questions this raises
- When the independence assumption (eq. 5.2, 5.25) fails, as for neighbouring pixels, how bad is the resulting loss?
- Does taking the argmax of the predicted distribution always give the best point estimate, for example for multimodal outputs (problem 5.4 asks about inference problems)?
- How are the minimizers of these losses found in practice? (The next chapter addresses training.)
- What does the learned σ̂² really measure if the chosen distribution is a poor model of the data?

## Exercises worth doing
- Ex. 5.1 (p. 74) — show the sigmoid limits and value at 0; checks that sig maps ℝ into [0,1] — difficulty: easy
- Ex. 5.2 (p. 74) — plot the binary loss for y = 0 and y = 1; shows how the loss behaves as confidence changes — difficulty: easy
- Ex. 5.3 (p. 74) — apply the recipe to the von Mises distribution for wind direction; practice with a new distribution and inference — difficulty: medium
- Ex. 5.6 (p. 76) — design a Poisson loss for counts; also needs a positivity constraint on the network output — difficulty: medium
- Ex. 5.7 (p. 76) — independent normal outputs; shows least squares survives for vector outputs with constant σ² — difficulty: easy
- Ex. 5.9 (p. 76) — height in metres and weight in kilos on different scales; asks for two fixes — difficulty: medium

## Reading notes
- Printed page = pdf page − 14 (pdf 70 = printed 56). All page references are printed numbers.
- The unit ends with Problem 5.10 on p. 76.
- The text layer garbles many equations, so equations were checked against the page images. In eq. 5.22 the image shows the summation index as z_{k′}, not z_k.
- Problem 5.6 calls the Poisson formula (eq. 5.36) a "probability density function", although the distribution is discrete. This is reported as printed.
- The unit pages show "Draft: please send errata to udlbookmail@gmail.com" in the footer, so this is a draft printing; the title page is not included.
- Several notes cite appendices (A, B.1.3, C.1.3, C.1.5, C.5.1) and Notebooks 5.1–5.3. These are not in the supplied pages.
