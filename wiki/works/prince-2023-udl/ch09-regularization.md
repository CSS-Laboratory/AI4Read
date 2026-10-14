---
id: prince-2023-udl/ch09-regularization
work: prince-2023-udl
unit: "Chapter 9 — Regularization"
pages: 138-160
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
# Regularization

## L0 — One line
Generalization can be improved by adding a penalty to the loss, by the implicit biases of SGD, and by many heuristics (early stopping, ensembling, dropout, noise, transfer learning, augmentation) that smooth the function, add data, combine models or find wide minima.

## L1 — The gist (≤ 120 words)
Chapter 8 showed that a model can fit training data much better than test data. This chapter asks how to shrink that generalization gap. Explicit regularization adds a penalty term to the loss; in the MAP view this term corresponds to a prior over the parameters (its negative log). Gradient descent and SGD also act as implicit regularizers: they are repelled from steep regions, and SGD also favors places where batch gradients agree. Many heuristics also help: early stopping, ensembling, dropout, adding noise, label smoothing, Bayesian inference, transfer, multi-task and self-supervised learning, and data augmentation. The author groups them under four principles: smoother functions, more data, combined models, wider minima.

**Prerequisites:** loss functions and maximum likelihood (ch. 5); gradient descent/SGD; Bayes' rule; Taylor expansion and partial derivatives; the bias/variance trade-off (ch. 8).

## L2 — Key ideas
- Explicit regularization adds $\lambda\, g[\phi]$ to the loss; the minima move, so training ends at different parameters (p. 139).
- The penalty equals a negative log prior: $\lambda g[\phi] = -\log Pr(\phi)$, so regularized fitting is MAP estimation (p. 140).
- L2 (weight decay) penalizes squared weights and smooths the function. One way to think about it, when the network is overfitting: lower variance at the cost of higher bias (p. 140).
- Finite-step gradient descent behaves like continuous descent on a loss with an added squared-gradient-norm term, $\frac{\alpha}{4}\|\partial L/\partial\phi\|^2$ (p. 142).
- SGD adds a further penalty on the variance of batch gradients. This may partly explain why smaller batches generalize better (p. 143).
- Early stopping, ensembling, dropout, input/weight/label noise and Bayesian averaging reduce overfitting in different ways (pp. 145–151).
- Transfer, multi-task and self-supervised learning and augmentation exploit other data or labels, or create more (pp. 151–154).
- Four principles unify the methods: smoother function, more data, combine models, wider minima (p. 154).
- Notes: weight decay ≠ L2 for Adam. L2 gives little benefit in some studies, and L1/L0 encourage sparsity (pp. 155–156).

## L3 — Walkthrough

**Opening (p. 138).** Chapter 8 gave two reasons for a train–test gap: (i) overfitting, where the model describes quirks of the training data; (ii) the model is unconstrained where there are no training examples (p. 138). *Regularization* strictly means adding explicit loss terms that favor some parameters. In machine learning it is also used for any strategy that improves generalization (p. 138).

### 9.1 Explicit regularization
Standard fitting:
$$\hat\phi=\operatorname*{argmin}_\phi\Big[\sum_{i=1}^I \ell_i[x_i,y_i]\Big]\tag{9.1}$$
Regularized fitting:
$$\hat\phi=\operatorname*{argmin}_\phi\Big[\sum_{i=1}^I \ell_i[x_i,y_i]+\lambda\cdot g[\phi]\Big]\tag{9.2}$$
$g[\phi]$ is a scalar that is larger for less-preferred parameters. $\lambda>0$ sets the relative weight of loss and penalty. The minima usually differ from the original ones, so training converges to different values (p. 139). Figure 9.1 shows this for the Gabor model: adding a penalty that grows with distance from the centre gives fewer local minima, and the global minimum moves (p. 139).

**9.1.1 Probabilistic interpretation.** Maximum likelihood (section 5.1):
$$\hat\phi=\operatorname*{argmax}_\phi\Big[\prod_{i=1}^I Pr(y_i|x_i,\phi)\Big]\tag{9.3}$$
The penalty can be seen as a *prior* $Pr(\phi)$, knowledge about parameters before seeing data. This gives the maximum a posteriori (MAP) criterion:
$$\hat\phi=\operatorname*{argmax}_\phi\Big[Pr(\phi)\prod_{i=1}^I Pr(y_i|x_i,\phi)\Big]\tag{9.4}$$
Taking the log and multiplying by $-1$ returns the loss form, with $\lambda\cdot g[\phi]=-\log[Pr(\phi)]$ (p. 140).

*Intuition note:* Penalizing "unlikely" parameters can be read as believing, before seeing data, that some parameters are more plausible. The loss adds a "cost of surprise" for the parameters themselves.

**9.1.2 L2 regularization.** Since networks serve very diverse tasks, the preferences can only be generic. The most common penalty is the L2 norm:
$$\hat\phi=\operatorname*{argmin}_\phi\Big[\sum_{i=1}^I \ell_i[x_i,y_i]+\lambda\sum_j\phi_j^2\Big]\tag{9.5}$$
Other names are Tikhonov regularization, ridge regression and (for matrices) Frobenius norm regularization (p. 140). In networks it is usually applied to weights but not biases and is called *weight decay* here. Smaller weights make the output vary less, so the function is smoother. This holds layer by layer going backward. If all weights were zero, the output would be constant, set by the final bias (p. 140).

Figure 9.2 (14 hidden units): small $\lambda$ has little effect. Intermediate $\lambda$ gives a smoother function closer to the truth. Large $\lambda$ overpowers the likelihood term and the fit worsens (p. 141). Two reasons it may help test performance (p. 140):
- If overfitting, the network must trade fidelity to the data against smoothness. Variance falls at the cost of increased bias.
- If over-parameterized, spare capacity describes regions with no data. The penalty favors smooth interpolation there, which is reasonable without knowledge of the true function.

### 9.2 Implicit regularization
Neither gradient descent nor SGD moves neutrally to a minimum; each prefers some solutions. This is *implicit regularization* (p. 141).

**9.2.1 Gradient descent.** Continuous version (infinitesimal step) and discrete version with step $\alpha$:
$$\frac{d\phi}{dt}=-\frac{\partial L}{\partial\phi}\tag{9.6}$$
$$\phi_{t+1}=\phi_t-\alpha\frac{\partial L[\phi_t]}{\partial\phi}\tag{9.7}$$
Discretization deviates from the continuous path (fig. 9.3). A modified loss for the continuous case that reaches the same place as the discrete version on $L$ is (derivation in Notes, below):
$$\tilde L_{GD}[\phi]=L[\phi]+\frac{\alpha}{4}\left\|\frac{\partial L}{\partial\phi}\right\|^2\tag{9.8}$$
The discrete trajectory is repelled from steep places. Minima (gradient zero) do not move, but the effective loss elsewhere changes, so the path may reach a different minimum. This may be responsible for full-batch gradient descent generalizing better with larger step sizes (fig. 9.5a) (p. 142).

**9.2.2 SGD.** Seek a loss whose continuous version reaches the same place as the *average* of the random SGD updates:
$$\tilde L_{SGD}[\phi]=\tilde L_{GD}[\phi]+\frac{\alpha}{4B}\sum_{b=1}^B\left\|\frac{\partial L_b}{\partial\phi}-\frac{\partial L}{\partial\phi}\right\|^2 = L[\phi]+\frac{\alpha}{4}\left\|\frac{\partial L}{\partial\phi}\right\|^2+\frac{\alpha}{4B}\sum_{b=1}^B\left\|\frac{\partial L_b}{\partial\phi}-\frac{\partial L}{\partial\phi}\right\|^2\tag{9.9}$$
$L_b$ is the loss for the $b$th of $B$ batches in an epoch. Both are means of per-example losses:
$$L=\frac1I\sum_{i=1}^I\ell_i[x_i,y_i],\qquad L_b=\frac1{|\mathcal B|}\sum_{i\in\mathcal B_b}\ell_i[x_i,y_i]\tag{9.10}$$
The extra term is the variance of the batch gradients, so SGD implicitly favors places where batches agree on the slope (fig. 9.4). The global minimum is not necessarily moved: if the model is over-parameterized and fits all training data exactly, these gradient terms are zero there (p. 143).

SGD generalizes better than gradient descent, and smaller batches generally do better (fig. 9.5b). One possible explanation is that randomness reaches different parts of the loss surface. It is also possible that some or all of the gain is implicit regularization, which favors solutions where all data fit well over ones with the same overall loss but some data fitted extremely well and some poorly (p. 143).

*Intuition note:* Taking big discrete steps is not the same as sliding smoothly downhill. The difference can be interpreted as a small penalty against steep ground, and with random batches also against ground where batches disagree.

### 9.3 Heuristics to improve performance (p. 143)

**9.3.1 Early stopping.** Stop before full convergence. This can reduce overfitting if the model has captured the coarse shape but not yet fit the noise (fig. 9.6: training loss keeps falling, yet intermediate models are closest to the truth). Two views: weights start small (section 7.5) and have no time to grow, similar to L2; or effective model complexity is reduced, moving back down the bias/variance curve from the critical region (p. 145). The one hyperparameter (number of steps) is chosen with a validation set without training several models: train once, evaluate every $T$ iterations, store parameters, keep the best (p. 145).

**9.3.2 Ensembling.** Average predictions of several models. It reliably improves test performance at the cost of training, storing and running several models (p. 146). Combine by mean of outputs (regression) or mean of pre-softmax activations (classification), assuming errors are independent and cancel; or use the median / most frequent class for robustness (p. 146). Ways to get different models: different random initializations (may help far from the training data, where the function is unconstrained); *bagging* (bootstrap aggregating: resample the data with replacement, train one model per resample, fig. 9.7), which smooths the data because a missing outlier is interpolated from neighbours; different hyperparameters or model families (pp. 146–147).

**9.3.3 Dropout.** At each SGD iteration, clamp a random subset (typically 50%) of hidden units to zero (fig. 9.8). The network depends less on any one unit, and weights tend to be smaller (p. 147). Dropout can remove "kinks" far from the data that do not affect the loss: three units become active in turn (slope up, down, up again) and "conspire" to make a local bump (fig. 9.9a). Removing one changes the function in the half-space where it was active. The next gradient step compensates, and such dependencies are removed over time, even though they contribute nothing to the loss (pp. 147–148).

At test time, run the network with all units but multiply weights by one minus the dropout probability (*weight scaling inference rule*). Alternatively use *Monte Carlo dropout*: run several times with random units clamped and combine the results. This is closely related to ensembling but needs no multiple trained networks (p. 148).

**9.3.4 Applying noise.** Dropout is multiplicative Bernoulli noise on activations, which suggests noise elsewhere (p. 149):
- *Inputs:* smooths the function (fig. 9.10). For regression it can be shown to equal a penalty on derivatives of output with respect to input (Problem 9.3). *Adversarial training* searches for small input perturbations causing large output changes, i.e. worst-case additive noise.
- *Weights:* encourages sensible predictions under small weight perturbations; training converges to minima in wide, flat regions.
- *Labels:* maximum likelihood for classification pushes pre-softmax activations toward very large values for the correct class (eq. 5.24). To discourage overconfidence, assume a proportion $\rho$ of labels are wrong, belonging equally to the other classes. Equivalently, minimize cross-entropy to a target with probability $1-\rho$ on the true label and equal probability on the others. This is *label smoothing* and improves generalization in diverse scenarios (p. 150).

**9.3.5 Bayesian inference.** Maximum likelihood is generally overconfident: it picks the most likely parameters, though many may be only slightly less likely. The Bayesian approach computes a distribution over parameters:
$$Pr(\phi|\{x_i,y_i\})=\frac{\prod_{i=1}^I Pr(y_i|x_i,\phi)Pr(\phi)}{\int\prod_{i=1}^I Pr(y_i|x_i,\phi)Pr(\phi)\,d\phi}\tag{9.11}$$
The prediction is a posterior-weighted integral, an "infinite weighted ensemble" whose weights depend on the prior and the agreement with the data:
$$Pr(y|x,\{x_i,y_i\})=\int Pr(y|x,\phi)\,Pr(\phi|\{x_i,y_i\})\,d\phi\tag{9.12}$$
Fig. 9.11: with a zero-mean normal prior, when the prior variance $\sigma_\phi^2$ is small, the parameters also tend to be small and the functions smoother. Predictions come with an uncertainty band. For networks there is no practical way to represent or integrate the full distribution, so all current methods approximate and typically add considerable complexity (pp. 150–151).

**9.3.6 Transfer and multi-task learning.** With limited data, pre-train on a related secondary task with more data, then adapt: remove the last layer, add new layers, and either train only those or fine-tune everything (fig. 9.12a). The network builds a good internal representation, or equivalently the parameters are initialized in a sensible region (p. 152). *Multi-task learning* trains on several problems at once (e.g. segmentation, depth, captioning of one image), and performance on each may improve (fig. 9.12b) (p. 152).

**9.3.7 Self-supervised learning.** Creates "free" labeled data for transfer learning. *Generative:* mask part of each example and predict it, e.g. inpainting images, or masking words in text and then fine-tuning (see ch. 12). *Contrastive:* compare related pairs with unrelated ones, e.g. transformed versions of one image, or whether two sentences followed each other. Sometimes the exact relation must be identified, such as the relative position of two patches (p. 152).

**9.3.8 Augmentation.** Transform each example so the label stays valid: rotate, flip, blur or recolour images of a bird (fig. 9.13); substitute synonyms or round-trip translate text; amplify or attenuate audio frequency bands. The aim is to make the model indifferent to irrelevant transformations (pp. 152, 154).

### 9.4 Summary (p. 154)
Explicit regularization changes the minimum's position; the term can be read as a prior. SGD with finite step size has implicit bias, interpretable as extra loss terms. The heuristics follow four principles (fig. 9.14): (i) smoother function (e.g. L2); (ii) more data (augmentation); (iii) combine models (ensembling); (iv) wider minima (weight noise). Choosing an architecture to suit the task (e.g. sharing parameters in segmentation) also helps; chapters 10–13 cover this (p. 155).

### Notes (pp. 155–159)
**L2 vs weight decay.** The Notes say L2 is "often also mistakenly referred to as 'weight decay'", a separate technique (Hanson & Pratt) with update
$$\phi\leftarrow(1-\lambda')\phi-\alpha\frac{\partial L}{\partial\phi}\tag{9.13}$$
For standard SGD it equals L2 regularization with $\lambda=\lambda'/2\alpha$. For Adam the learning rate differs per parameter, so they differ; AdamW implements weight decay properly and improves performance (p. 156).

**Other norms.** L0 charges a fixed penalty per non-zero weight (prunes the network; group versions can remove whole units) but is hard to optimize because the penalty is not smooth. L1 (LASSO) penalizes absolute values; its constant derivative can give sparser solutions than L2 and is easier to optimize than L0. L1 + L2 is the elastic net (p. 156).

**Evidence on explicit regularization is mixed.** Zhang et al. found L2 contributes little. Generalization error is bounded by the network's Lipschitz constant, which depends on the product of spectral norms of weight matrices, only indirectly on individual weight magnitudes (p. 156).

**Derivation of eq. 9.8 (pp. 156–157).** Write the gradient step as
$$\phi_1=\phi_0+\alpha\,g[\phi_0]\tag{9.14}$$
with $g$ the negative gradient. As $\alpha\to0$:
$$\frac{d\phi}{dt}=g[\phi]\tag{9.15}$$
Backward error analysis seeks a correction $g_1$ so the continuous path matches the discrete step:
$$\frac{d\phi}{dt}\approx g[\phi]+\alpha g_1[\phi]+\dots\tag{9.16}$$
Taylor-expand the modified solution to second order, insert 9.16, replace $d\phi/dt$ by $g$, and drop terms above order $\alpha^2$:
$$\begin{aligned}\phi[\alpha]&\approx\phi+\alpha\frac{d\phi}{dt}+\frac{\alpha^2}{2}\frac{d^2\phi}{dt^2}\Big|_{\phi=\phi_0}\\&\approx\phi+\alpha(g+\alpha g_1)+\frac{\alpha^2}{2}\Big(\frac{\partial g}{\partial\phi}\frac{d\phi}{dt}+\alpha\frac{\partial g_1}{\partial\phi}\frac{d\phi}{dt}\Big)\Big|_{\phi_0}\\&=\phi+\alpha(g+\alpha g_1)+\frac{\alpha^2}{2}\Big(\frac{\partial g}{\partial\phi}g+\alpha\frac{\partial g_1}{\partial\phi}g\Big)\Big|_{\phi_0}\\&\approx\phi+\alpha g+\alpha^2\Big(g_1+\frac12\frac{\partial g}{\partial\phi}g\Big)\Big|_{\phi_0}\end{aligned}\tag{9.17}$$
The first two terms match the discrete update, so the $\alpha^2$ term must vanish:
$$g_1[\phi]=-\frac12\frac{\partial g[\phi]}{\partial\phi}g[\phi]\tag{9.18}$$
With $g=-\partial L/\partial\phi$:
$$\frac{d\phi}{dt}\approx g+\alpha g_1=-\frac{\partial L}{\partial\phi}-\frac\alpha2\Big(\frac{\partial^2L}{\partial\phi^2}\Big)\frac{\partial L}{\partial\phi}\tag{9.19}$$
This is continuous gradient descent on
$$L_{GD}[\phi]=L[\phi]+\frac\alpha4\left\|\frac{\partial L}{\partial\phi}\right\|^2\tag{9.20}$$
because the right side of 9.19 is the negative derivative of 9.20 (p. 157). (added step, one parameter: $\partial/\partial\phi\,[\tfrac\alpha4(L')^2]=\tfrac\alpha2L''L'$.) The notes attribute this to Barrett & Dherin and the SGD extension to Smith et al. They report that large learning rates reduce movement toward "sharper" regions, which can be approximated by penalizing the trace of the Fisher Information Matrix (p. 157).

*Intuition note:* The derivation asks: what extra push on a smooth path would reproduce one finite step? The answer is a push away from steep, high-curvature places, which is the same as descending a loss with a gradient-norm penalty.

**Early stopping.** Under a quadratic loss approximation with parameters initialized to zero, early stopping is equivalent to L2 regularization in gradient descent, with $\lambda\approx1/(\tau\alpha)$ ($\tau$ = stopping time) (p. 157).

**Ensembling.** Averaging independently trained outputs can improve accuracy, calibration and robustness; averaging the *weights* of separately trained networks into one model fails (Frankle et al.). Different random starts give bigger gains than exploring around one solution. Cheaper variants: stochastic weight averaging, snapshot ensembles, fast geometric ensembling (p. 158).

**Dropout, noise, label smoothing.** Dropping a unit equals zeroing its incoming and outgoing weights and bias. Monte Carlo dropout is argued to approximate Bayesian inference. Input noise (Bishop) is shown equivalent to weight decay. Label smoothing helps in several domains, but its mechanism is not well understood; one finding is that it improves calibration (p. 158).

**Wider minima.** It is thought that wider minima generalize better. Entropy SGD biases toward flat minima. SGD finds wider minima as batch size falls, possibly due to the batch-variance term. Flooding prevents training loss reaching zero (pp. 158–159).

**Bayesian, transfer, self-supervised, augmentation.** Neural-network posteriors cannot be represented in closed form and must be approximated; the two main approaches are variational Bayes and MCMC. Transfer learning has worked "extremely well" for vision and NLP (BERT features). NLP self-supervision includes masked words, next-word and next-sentence prediction. Augmentation extends to audio, speech and text (pp. 159–160).

### Problems (p. 160)
Problems 9.1–9.6 ask for derivations (see Exercises).

## Toy example (ours, not from the text)
**Explicit L2 moves the minimum.** One parameter, loss $L(\phi)=(\phi-3)^2$, so the unregularized minimum is $\phi=3$. Add $\lambda\phi^2$ with $\lambda=1$: $L_\text{reg}=(\phi-3)^2+\phi^2$. Derivative: $2(\phi-3)+2\phi=4\phi-6=0$, so $\phi=1.5$. In general $2(\phi-3)+2\lambda\phi=0\Rightarrow\phi=3/(1+\lambda)$. For $\lambda=0$ this gives 3, for $\lambda=1$ it gives 1.5, for $\lambda=9$ it gives 0.3. Larger $\lambda$ shrinks the parameter more, as in fig. 9.2.

**Checking eq. 9.8.** Take $L=\phi^2$, so $\partial L/\partial\phi=2\phi$ and $\tilde L=\phi^2+\frac\alpha4(2\phi)^2=(1+\alpha)\phi^2$. Discrete GD: $\phi_1=\phi_0-\alpha\cdot2\phi_0=(1-2\alpha)\phi_0$; with $\alpha=0.1$ the factor is 0.8. Continuous descent on $L$ for time $\alpha$ gives $e^{-2\alpha}=e^{-0.2}\approx0.8187$. Continuous descent on $\tilde L$ gives $e^{-2(1+\alpha)\alpha}=e^{-0.22}\approx0.8025$. The corrected continuous path is closer to the discrete result 0.8. (Time $\alpha$ corresponds to one discrete step.)

## Concepts
- [[explicit-regularization]] (new) — adding a penalty $\lambda g[\phi]$ to the loss to favor certain parameters (p. 139)
- [[map-estimation]] (new) — maximizing prior × likelihood; the penalty is $-\log Pr(\phi)$ (p. 140)
- [[l2-regularization]] (new) — penalty $\lambda\sum_j\phi_j^2$ ("weight decay" in the main text); smooths the function (p. 140)
- [[implicit-regularization]] (new) — bias of GD/SGD toward certain solutions (p. 141), which can be interpreted as extra loss terms (p. 154)
- [[early-stopping]] (new) — stop training before convergence, using validation performance (p. 145)
- [[ensembling]] (new) — averaging several models' predictions; bagging is one way (p. 145)
- [[dropout]] (new) — randomly clamp hidden units to zero during training (p. 147)
- [[label-smoothing]] (new) — train on targets with $1-\rho$ on the true class and the rest spread equally (p. 150)
- [[bayesian-inference]] (new) — treat parameters as a distribution and average predictions over it (p. 150)
- [[transfer-learning]] (new) — pre-train on a secondary task, then adapt to the target task (p. 151)
- [[pretraining-fine-tuning]] — here: pre-train on a related task, then train new final layers or the whole model (p. 152)
- [[self-supervised-learning]] (new) — make labels from the data itself (masking or contrastive pairs) (p. 152)
- [[masked-language-modeling]] — here: masking words and predicting them as a generative self-supervised task (p. 152)
- [[data-augmentation]] (new) — label-preserving transformations that expand the training set (p. 154)

## Canonical instances
- [[gabor-model-loss-surface]] (new) — loss with many local minima, shown with a penalty added (p. 139)
- [[14-hidden-unit-regression-fit]] (new) — toy network fitted with different $\lambda$, training stages, ensembles and priors (pp. 141, 146, 151)
- [[mnist1d-lr-batch-experiment]] (new) — larger learning rates and smaller batches give lower test error (p. 145)
- [[dropout-kink-removal]] (new) — three conspiring units cause a kink dropout removes (p. 149)
- [[bird-image-augmentation]] (new) — flips, blurs etc. keep the label "bird" (p. 154)

## Bridges (candidates)
- [same-math] Gaussian prior on weights ↔ L2 penalty: both follow from $\lambda g=-\log Pr(\phi)$; Problem 9.1 asks for the derivation (p. 160).
- [structural-analogy] Masked-word prediction (9.3.7) ↔ llm: masked language modeling as pretraining before fine-tuning.
- [structural-analogy] Dropout / Monte Carlo dropout ↔ ensembling: many sub-networks as an implicit ensemble.
- [metaphor] Label smoothing ↔ scoring rules that discourage extreme confidence in forecasting.

## Questions this raises
- When does L2 help noticeably, given that the Notes cite evidence that it contributes little in some studies (p. 156)?
- Why does SGD with smaller batches find wider minima, and is the batch-variance term the cause (p. 159)?
- How could Bayesian predictions be approximated cheaply enough for large networks (p. 151)?
- Does self-supervised pre-training (masked or next-word prediction) behave as a regularizer or as extra data (pp. 152, 159)?

## Exercises worth doing
- Ex. 9.1 (p. 160) — Gaussian prior ⇒ L2 loss; links MAP to weight decay — difficulty: easy
- Ex. 9.2 (p. 160) — effect of L2 on gradients — difficulty: easy
- Ex. 9.5 (p. 160) — weight decay update equals L2 with $\lambda/2\alpha$ — difficulty: medium
- Ex. 9.4 (p. 160) — loss under label smoothing (0.9 / 0.1) — difficulty: hard
- Ex. 9.3 (p. 160) — input noise ⇒ expected loss in linear regression — difficulty: hard
- Ex. 9.6 (p. 160) — sketch L0, L½, L1 penalties — difficulty: medium

## Reading notes
- Printed page = pdf − 14. The text layer for several equations (e.g. 9.8–9.9, 9.17) has scrambled layout, so I checked the equations against the page images (9.8–9.9 and 9.14–9.20).
- Terminology tension in the source: section 9.1.2 calls L2 on weights "weight decay", but the Notes (p. 155) say that name is mistaken for L2 and give eq. 9.13 as the real weight decay. I followed each passage as written.
- Eq. 9.8 is written $\tilde L_{GD}$ in the main text and $L_{GD}$ (no tilde) in eq. 9.20. The source says the right side of 9.19 'is the derivative of' 9.20; the digest writes 'negative derivative', which is what the signs give.
- In fig. 9.5 the image's x-axis is labelled "Hidden layer size" (0–400), though the captions discuss learning rate and batch size.
- The unit includes the figures, Notes and Problems (pp. 155–160). Problem solutions are not printed in these pages.
