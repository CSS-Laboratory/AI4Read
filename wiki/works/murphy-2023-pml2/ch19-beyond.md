---
id: murphy-2023-pml2/ch19-beyond
work: murphy-2023-pml2
unit: "19 Beyond the iid assumption"
pages: 735–770
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Beyond the iid assumption (distribution shift, multiple distributions, continual learning, adversarial examples)

## L0 — One line
When test data differ from training data, the right remedy depends on which factor of the joint distribution changed, and worst-case (adversarial) errors exist whenever errors exist.

## L1 — The gist (≤ 120 words)
The chapter asks what to do when training and test data are not iid draws from one distribution. It sorts shifts into covariate, concept, label and manifestation shift. It then covers detecting shift and out-of-distribution inputs, robustness, and adaptation (transfer learning, importance weighting, domain-adversarial learning, blackbox shift estimation, test-time adaptation). Next come learning from several distributions (multitask, domain generalization, invariant risk minimization, meta-learning), continual and online learning, and adversarial examples. Which factor of the joint distribution changes guides which fix is appropriate. Accurate models can fail under mild shift, so these tools matter in practice.

**Prerequisites:** joint, conditional and marginal probability; Bayes' rule; empirical risk minimization; KL divergence; Gaussian distribution; matrix inverse; gradients; basic hierarchical Bayesian models and causal DAGs.

## L2 — Key ideas (5–10 bullets)
- Models often rely on spurious (shortcut) features that predict labels in training but are unstable across distributions; the author names this a root cause of many of the failures shown, and high-performing models can be very sensitive to small input shifts (p. 736).
- Writing the joint as $p(x)p(y|x)$ (causal/discriminative) or $p(y)p(x|y)$ (anticausal/generative) gives four shifts: covariate, concept, label, manifestation. Standard remedies differ by shift type, and concept shift cannot be fixed without labeled target data (pp. 738–739).
- Shift can be detected by two-sample tests, by single-input out-of-distribution (OOD) scores, or by conformal methods. Raw likelihoods from deep generative models can fail as OOD scores, while log-likelihood ratios are invariant to invertible transforms (pp. 741–743).
- Under covariate shift, weighted empirical risk minimization (ERM) with $w=q(x)/p(x)$ gives a risk estimate. The weights can be estimated with a source-vs-target classifier, $w=\exp(h(x))$ (pp. 748–749).
- Under label shift, blackbox shift estimation solves $\mu=Cq$ for the new label prior. It is valid if $C$ is invertible, no new labels appear, and only the label prior changes (p. 750).
- With several distributions, multitask, domain generalization, IRM and meta-learning differ in what is available and what is predicted. Meta-learning is cast as hierarchical Bayesian prediction with log-of-average objective (pp. 751–758).
- Continual learning risks catastrophic forgetting. Remedies are regularization, memory, or architecture. Online learning scores each step's prediction made from past data (prequential loss) and compares total loss to the best predictor in hindsight (regret) (pp. 762–764).
- Adversarial examples are worst-case shifts, found by gradients (fast gradient sign, projected gradient descent) or gradient-free search. If the decision boundary is locally linear and the input is high-dimensional, even a small error rate in noise implies very close errors (pp. 765–770).

## L3 — Walkthrough

### 19.1 Introduction (p. 735)
Standard supervised ML assumes train and test sets are iid from the same distribution. The chapter relaxes this in four ways: distribution shift (19.2), data from multiple related distributions (19.6), streaming data whose distribution changes continuously or piecewise (19.7), and test data chosen by an adversary (19.8).

### 19.2 Distribution shift (pp. 735–740)
Fit $p(y|x)$ on a labeled **source** distribution $p(x,y)$; at test time data come from the **target** $q(x,y)$. If $p\neq q$ there is a **distribution shift** (dataset shift) (p. 735). The chapter then treats detecting shift (19.3), robustness (19.4) and adaptation (19.5) (p. 735).

**19.2.1 Motivating examples (pp. 735–737).**
- Adding a little Gaussian noise can hurt an accurate ResNet-50 on ImageNet. In Fig. 19.1 a coffee pot is labelled "Toaster" at $\sigma=.2$ and "Television" at $\sigma=.6$ (p. 736).
- In Fig. 19.2 a cow on a beach ("out of context") is not detected, or is called a generic "mammal". In training data cows mostly stand on grass (p. 736).
- Root cause: discriminative models often use features predictive *in the training set* but unreliable in general, such as grass for "cow". These are **spurious correlations** or **shortcut features**, and such features are often easier to learn (p. 736).
- Real consequence: [Zec+18a] found a pneumonia CNN relied on hospital-specific metal tokens in X-rays, so it did not generalize to new hospitals (p. 737).
- Analogous failures occur in text ("he"→"she" can flip sentiment), audio (background noise) and medical records. Changes needed to flip outputs can be imperceptible (p. 737).

**19.2.2 A causal view (pp. 737–738).** Covariates are $X$, labels $Y$. If $X\to Y$ the task is **causal (discriminative) prediction**. If $Y\to X$ it is **anticausal (generative) prediction** (p. 737). Examples (p. 738):
- $X$ medical image, $Y$ a segmentation made by an expert: $X\to Y$.
- $X$ medical image, $Y$ true disease state: $Y\to X$.
- $X$ review text, $Y$ informativeness: $X\to Y$. $Y$ star rating: $Y\to X$.

Footnote 1: whether a model generalizes to a new distribution is *external validity*. An externally valid model is *transportable* (p. 737). Two factorizations:

$$p_\theta(x,y)=p_\psi(x)\,p_w(y|x)\quad\text{(discriminative)}\tag{19.1}$$
$$p_\theta(x,y)=p_\pi(y)\,p_\phi(x|y)\quad\text{(generative)}\tag{19.2}$$

Fig. 19.3 shows the graphical models, with a labeled source set, optional labeled/unlabeled target sets and a labeled target test set. Loss is evaluated only on the target (p. 737). In each model, different parts can change, giving four canonical shifts (p. 738).

**19.2.3 The four main types (pp. 738–739; Table 19.1).**

| Name | Source | Target | Joint |
|---|---|---|---|
| Covariate/domain shift | $p(X)p(Y|X)$ | $q(X)p(Y|X)$ | Discriminative |
| Concept shift | $p(X)p(Y|X)$ | $p(X)q(Y|X)$ | Discriminative |
| Label (prior) shift | $p(Y)p(X|Y)$ | $q(Y)p(X|Y)$ | Generative |
| Manifestation shift | $p(Y)p(X|Y)$ | $p(Y)q(X|Y)$ | Generative |

- *Covariate shift* ($\psi^s\neq\psi^t$): clean vs noisy coffee-pot images; catalog photos vs photos "in the wild"; synthetic vs real images; English reviews vs Spanish translations. Standard remedies: importance weighting (19.5.2) and domain adaptation (19.5.3) (pp. 738–739).
- *Concept shift* ($w^s\neq w^t$), also *annotation shift*: annotation conventions differ, or a new label appears in the target (related to open-world recognition, 19.3.4). Since it changes what a label "means", it is impossible to fix without labeled target examples (p. 739).
- *Label/prior/prevalence shift* ($\pi^s\ne\pi^t$): e.g. disease prevalence differs between an urban and a rural hospital. A standard strategy: reweight a discriminative classifier's output using an estimate of the new label distribution (19.5.4) (p. 739).
- *Manifestation (conditional) shift* ($\phi^s\neq\phi^t$): the same disease looks different, e.g. tumor shape. It is in some sense the inverse of concept shift. It is usually due to a hidden confounder that changed, such as patient age (p. 739).

*Intuition note.* Each shift is "one factor of the joint changed, the other did not". That suggests what may be reused from the source and what may need re-learning.

**19.2.4 Selection bias (p. 740).** Let $S=1$ if a population sample enters the training set. Source: $p(X,Y)=p(X,Y|S=1)$. Target: $q(X,Y)=p(X,Y|S\in\{0,1\})=p(X,Y)$, i.e. no selection (p. 740). Fig. 19.5 shows four selection types: (a) no selection, (b) on $X$, (c) on $Y$, (d) on $X$ and $Y$. Their effects:
- Selection on $X$ can induce domain/covariate shift.
- Selection on $Y$ (e.g. oversampling rare $Y=1$ to balance the dataset) can induce label shift.
- Selection on both can induce non-causal dependencies between $X$ and $Y$, known as selection bias (see Sec. 4.2.4.2, not in this unit).

### 19.3 Detecting distribution shifts (pp. 740–745)
It will not generally be possible to make a model robust to all shifts, so it may suffice to *detect* a shift and respond. Methods differ by whether we have a set of target samples or one sample, and whether they are labeled (pp. 740–741).

**19.3.1 Two-sample testing (p. 741).** With samples from source and target, test the null $p(x,y)=q(x,y)$ (or $p(x)=q(x)$ if unlabeled). Options: MMD on inputs, or Euclidean distances in the embedding space of a source-trained classifier. In some cases it may be possible to test only $p(y)$, which is easier than testing $p(x)$. If the label-shift assumption $q(x|y)=p(x|y)$ holds, plus some other assumptions, one can estimate $q(y)$ by blackbox shift estimation (19.5.4). If $q(y)=p(y)$ is found, then $q(x,y)=p(x,y)$ can be concluded. [RGL19] showed experimentally that this works well even when the label-shift assumption does not hold. Conformal prediction gives "distribution free" covariate-shift detection from a calibration set and a conformity score [HL20].

**19.3.2 Detecting single OOD inputs (p. 741).** Given one unlabeled $x\sim q$, decide in-distribution (ID) or out-of-distribution (OOD). This is also called anomaly or novelty detection. If ID, one may also return a class label (Fig. 19.6). Footnote 2: *outlier detection* is different: one unlabeled dataset, find untypical points (transductive), whereas the chapter focuses on inductive tasks.

- **19.3.2.1 Outlier exposure (p. 741).** With labeled ID and OOD training samples, fit a binary classifier ("known unknowns" vs "known knowns"). It can work well, but usually there are too few OOD examples, since OOD is "all possible inputs" except those of interest.
- **19.3.2.2 Classification confidence (p. 742).** With $p_c=p(y=c|x)$ and logits $\ell_c=\log p_c$, scores include: max probability $s=\max_c p_c$; margin $s=\max_c\ell_c-\max^2_c\ell_c$ (second largest); entropy $s=\mathbb H(p_{1:C})$; "energy score" $s=\sum_c\ell_c$ as printed [Liu+21b]. [Mil+21; Vaz+22] show that the simple max-probability baseline performs very well. Footnote 3: [Kir+21] argue against entropy, since it confuses uncertainty about which label with uncertainty about whether any label fits ("none-of-the-above").
- **19.3.2.3 Conformal prediction (pp. 742–743).** Following [Ang+21], define the two-stage prediction set
$$\mathcal T_\lambda(x)=\begin{cases}\emptyset & \text{if } \mathrm{OOD}(x)>\lambda_1\\ \mathrm{APS}(x)&\text{otherwise}\end{cases}\tag{19.3}$$
where $\mathrm{OOD}(x)$ is a heuristic score (e.g. max class probability) and APS is the adaptive prediction set: the top-$K$ labels whose probabilities sum above $\lambda_2$. Formally $\mathrm{APS}(x)=\{\pi_1,\dots,\pi_K\}$, $\pi$ sorts $f(x)_{1:C}$ descending, $K=\min\{K':\sum_{c=1}^{K'}f(x)_c>\lambda_2\}$ (p. 742). Thresholds are chosen on a calibration set with a frequentist hypothesis-testing method. They jointly control
$$R_1(\lambda)=p(\mathcal T_\lambda(x)=\emptyset)\tag{19.4}$$
$$R_2(\lambda)=p(y\notin\mathcal T_\lambda(x)\mid\mathcal T_\lambda(x)\neq\emptyset)\tag{19.5}$$
under the true unknown source distribution (ID samples only; no OOD samples needed). $R_1$ is the type-I error (ID rejected as OOD). $R_2$ is the chance, given a decision to classify, that the true label is not in the set. The goal is to set $\lambda_1$ as large as possible while controlling type-I error (e.g. falsely flag at most 10% of ID samples), then set $\lambda_2$ as usual for APS (p. 743).
- **19.3.2.4 Unsupervised (pp. 743–744).** Fit a density model (e.g. VAE) to ID data and threshold $p(x)$. But for many deep models, $p(x)$ is sometimes *lower* on source samples than on a novel target. Pixel-CNN or flow models trained on Fashion-MNIST give higher likelihood to MNIST. Fig. 19.7: a Glow model trained on CIFAR10 gives higher likelihood to SVHN, which has lower visual complexity. Explanation given: natural data lies on a low-dimensional manifold, and simpler distributions get higher density from many models defined over the whole ambient space [Kam+24] (p. 743).
  - Fix: use the log-likelihood ratio against a baseline density $q$, $R(x)=\log p(x)/q(x)$, instead of $L(x)=\log p(x)$ [Ren+19]. $R$ is invariant to invertible transforms $x'=\phi(x)$. By change of variables $p(x')=p(x)|\det\mathrm{Jac}(\phi^{-1})(x)|$, so $L(x')$ differs from $L(x)$ by a transformation-dependent term. For $R$:
$$R(x')=\log p(x')-\log q(x')=\log p(x)+\log|\det\mathrm{Jac}(\phi^{-1})(x)|-\log q(x)-\log|\det\mathrm{Jac}(\phi^{-1})(x)|\tag{19.6}$$
  The two log-determinant terms cancel, so $R(x')=\log p(x)-\log q(x)=R(x)$ (added step; the printed equation ends at the cancellation) (pp. 743–744).
  - Other strategies: likelihood adjusted by complexity (compression coding length) [Ser+20]; likelihood of model features [Mor+21a]; autoencoder/VAE reconstruction error [Pol+19] (suffers the same problems as density methods); GAN discriminators, extended to open-set recognition by OpenGAN [KR21b] (p. 744).

**19.3.3 Selective prediction (p. 744).** If the system's confidence is below a threshold it may abstain. Varying the threshold trades accuracy against abstention rate. This is useful where errors cost more than asking an expert.

*19.3.3.1 Example: SGLD vs SGD for MLPs (pp. 744–745).* "Being Bayesian" about parameters puts parameter uncertainty into the posterior predictive and can help selective prediction. Setup: shallow MLP on MNIST, either RMSprop (SGD) or stochastic gradient Langevin dynamics (SGLD, an MCMC method, Sec. 12.7.1), 6,000 steps, minibatch 1,000. Confidence = probability of the MAP class. Fig. 19.8 uses 10 SGLD samples.
- On MNIST test data both behave similarly, with SGD slightly more accurate.
- On Fashion-MNIST (shift), both have accuracy below the 10% chance level. But SGD stays confident on many more predictions. At threshold 0.5, SGD predicts on about 97% of examples, SGLD on about 70%.

*Intuition note.* In this experiment the Bayesian (SGLD) model is more conservative under shift: it predicts on fewer inputs, i.e. abstains more, which is what selective prediction wants.

**19.3.4 Open set and open world recognition (p. 745).** If lack of confidence is due to a novel *class* (not a novel instance), the problem is **open set recognition**. Instead of flagging novel classes as OOD, the class set can grow over time: **open world classification**, most naturally handled by a continual learner (19.7.3).

### 19.4 Robustness to distribution shifts (pp. 745–746)
Goal: from labeled $p(x,y)$, build a model approximating $q(y|x)$.

**19.4.1 Data augmentation (p. 746).** Simulate target samples by modifying source data: small image perturbations (shifts, rotations) keeping the label, on the assumption that the label is invariant. In NLP: replace words that should not affect the label, or back-translation for paraphrases.

**19.4.2 Distributionally robust optimization (p. 746).** To be robust to (some forms of) covariate shift:
$$\min_{f\in\mathcal F}\max_{w\in\mathcal W}\frac1N\sum_{n=1}^N w_n\,\ell(f(x_n),y_n),\quad (x_n,y_n)\sim p\tag{19.7}$$
This is a min-max problem that minimizes the worst-case risk. The robustness set $\mathcal W$ is key to quality and difficulty. It is typically an $\ell_2$ ball around the inputs (as printed), but could be in feature space or defined by local changes to a structural causal model [Mei18a].

### 19.5 Adapting to distribution shifts (pp. 746–751)
With some labeled target data use transfer learning (19.5.1). Otherwise use unlabeled target data (19.5.2–19.5.5).

**19.5.1 Supervised adaptation (pp. 746–747).** Source set $\mathcal D^s$ ($N_s$ pairs from $p$) and a labeled target set $\mathcal D^t$ ($N_t$ pairs from $q$). Target risk and its empirical estimate:
$$R(f,q)=\mathbb E_{q(x,y)}[\ell(y,f(x))]\tag{19.8}$$
$$\hat R(f,\mathcal D^t)=\frac1{|\mathcal D^t|}\sum_{(x_n,y_n)\in\mathcal D^t}\ell(y_n,f(x_n))\tag{19.9}$$
If $\mathcal D^t$ is large, use ERM. If small, use $\mathcal D^s$ as a regularizer: **transfer learning**.
- *Pre-train and fine-tune.* Fit $f^s=\arg\min_f\hat R(f,\mathcal D^s)$ (source may be unlabeled, using self-supervised learning). Then
$$f^t=\arg\min_f \hat R(f,\mathcal D^t)+\lambda\|f-f^s\|\tag{19.10}$$
with $\lambda\ge0$ and $\|f-f^s\|$ some distance between functions. With few target samples one "freezes" most parameters (an implicit assumption that source features work for the target), "chops off the head" and fits a new linear layer by MAP. A pre-trained large model (e.g. a transformer) is often used as a feature extractor (p. 747).
- *Prompt tuning / in-context learning.* Keep the model frozen and condition on a prompt $z$:
$$f^t(x)=f^s(x\cup z)\tag{19.11}$$
Optimize $z$ manually or automatically. $z$ acts like a small training set, and attention lets $f^s$ compare $x$ with the examples in $z$. It works because text training data often has similar hierarchical structure ([Xie+22] give a Bayesian interpretation) (p. 747).

**19.5.2 Weighted ERM for covariate shift (pp. 748–749).** Assume covariate shift, $q(x,y)=q(x)p(y|x)$. Then
$$R(f,q)=\int q(x)q(y|x)\ell(y,f(x))\,dx\,dy\tag{19.12}$$
$$=\int q(x)p(y|x)\ell(y,f(x))\,dx\,dy\tag{19.13}$$
$$=\int \frac{q(x)}{p(x)}p(x)p(y|x)\ell(y,f(x))\,dx\,dy\tag{19.14}$$
$$\approx\frac1N\sum_{(x_n,y_n)\in\mathcal D^s_L}w_n\,\ell(y_n,f(x_n))\tag{19.15}$$
$$w_n=w(x_n)=\frac{q(x_n)}{p(x_n)}\tag{19.16}$$
This is **weighted ERM** [Shi00a; SKM07] (p. 748).

*Why is covariate shift a problem for a discriminative model?* If $p(y|x)$ is correct for all of input space, a change in $p(x)$ would not matter. But most models are accurate only in parts of input space. Fig. 19.10b: a linear model fit across the full support of $X$ may perform much worse on the target than a model that weights target points more heavily in training (p. 748).

*Estimating the weights.* Density estimation is hard in high dimension. Instead fit a binary classifier to distinguish the distributions (Sec. 2.7.5). With equal numbers from $p(x)$ (label $c=-1$) and $q(x)$ (label $c=1$):
$$p(c=1|x)=\frac{q(x)}{q(x)+p(x)},\quad\text{so}\quad\frac{p(c=1|x)}{p(c=-1|x)}=\frac{q(x)}{p(x)}\tag{19.17}$$
If $p(c=1|x)=\sigma(h(x))=1/(1+\exp(-h(x)))$ with $h$ the logits, then
$$w_n=\frac{1/(1+\exp(-h(x_n)))}{\exp(-h(x_n))/(1+\exp(-h(x_n)))}=\exp(h(x_n))\tag{19.18}$$
This requires $q(x)>0\Rightarrow p(x)>0$. So there are no guarantees about interpolating beyond the training distribution (p. 749).

*Intuition note.* Reweighting makes source points that look like target points count more. It cannot help where the target has inputs the source never produces.

**19.5.3 Unsupervised domain adaptation (UDA) (pp. 749–750).** Uses labeled source $\mathcal D_1\sim p(x,y)$ and unlabeled target $\mathcal D_2\sim q(x)$ to make the predictor more robust or invariant, rather than reweighting. One method is **domain adversarial learning** [Gan+16a]. Let $f_\alpha:\mathcal X_1\cup\mathcal X_2\to\mathcal H$ be a feature extractor, $c_\beta:\mathcal H\to\{1,2\}$ a domain classifier, $g_\gamma:\mathcal H\to\mathcal Y$ a label classifier. Train so the features cannot reveal the domain:
$$\min_\gamma\max_{\alpha,\beta}\ \frac1{N_1+N_2}\sum_{x_n\in\mathcal D_1,\mathcal D_2}\ell(d_n,c_\beta(f_\alpha(x_n)))+\frac1{N_1}\sum_{(x_n,y_n)\in\mathcal D_1}\ell(y_n,g_\gamma(f_\alpha(x_n)))\tag{19.19}$$
It minimizes the label-task loss but *maximizes* the domain-classification loss. This is implemented by the gradient sign reversal trick and is related to GANs (p. 750).

**19.5.4 Blackbox shift estimation for label shift (p. 750).** Method of [LWS18]. Assume only the label prior changes: $q(x,y)=p(x|y)q(y)$. For any deterministic $f:\mathcal X\to\mathcal Y$ with $\hat y=f(x)$:
$$p(x|y)=q(x|y)\Rightarrow p(f(x)|y)=q(f(x)|y)\Rightarrow p(\hat y|y)=q(\hat y|y)\tag{19.20}$$
Let $\mu_i=q(\hat y=i)$ be the fraction of test predictions in class $i$, $q(y=i)$ the unknown true test label distribution, and $C_{ij}=p(\hat y=i|y=j)$ the confusion matrix estimated on training data. Then
$$\mu_{\hat y}=\sum_y q(\hat y|y)q(y)=\sum_y p(\hat y|y)q(y)=\sum_y p(\hat y,y)\frac{q(y)}{p(y)}\tag{19.21}$$
$$\mu_i=\sum_i C_{ij}q_j\ \Rightarrow\ \boldsymbol\mu=\mathbf C\boldsymbol q\tag{19.22}$$
(the printed sum index is $i$; it should run over $j$ — see Reading notes). So $\boldsymbol q=\mathbf C^{-1}\boldsymbol\mu$, provided $\mathbf C$ is not singular. This holds if $\mathbf C$ is strongly diagonal, i.e. the model predicts class $y_i$ correctly more often than any other class $y_j$. Also $q(y)>0\Rightarrow p(y)>0$ is required (every label seen in training). Then correct the classifier:
$$q(y|x)=\frac{q(x|y)q(y)}{q(x)}=\frac{p(x|y)q(y)}{q(x)}=\frac{p(y|x)p(x)}{p(y)}\frac{q(y)}{q(x)}=p(y|x)\frac{q(y)}{p(y)}\frac{p(x)}{q(x)}\tag{19.23}$$
The factor $p(x)/q(x)$ is constant in $y$ and can be ignored. Requirements: (1) invertible confusion matrix, (2) no new labels at test time, (3) only the label prior changes. If all hold, the estimator is valid. [Gar+20] give a maximum-likelihood alternative (p. 750).

*Intuition note.* The model's predicted-class frequencies on the target are a mixture of its per-class behaviours, with mixing weights equal to the true target label frequencies. Inverting the confusion matrix un-mixes them.

**19.5.5 Test-time adaptation (TTA) (pp. 750–751).** The model is updated continuously, with only the source-trained model available (not the source data), unlike UDA.
- *TTT* [Sun+20]: a Y-shaped network, $x\to h$, then $h\to y$ and $h\to r$ for a proxy output $r$ such as image rotation angle (known under augmentation). At test time, update the $x\to h\to r$ branch, which influences $y$ via the shared bottleneck $h$ (p. 751).
- *TENT* [Wan+20a]: when no proxy is available, update parameters to minimize predictive entropy over a batch of test examples. [Goy+22] justify it from meta-learning. *BACS* [ZL21] is a Bayesian version.
- *MEMO* [ZLF21]: augment one test input into $\tilde x_1,\dots,\tilde x_B$ and minimize the entropy of the averaged prediction
$$\bar p(y|x,w)=\frac1B\sum_{b=1}^B p(y|\tilde x_b,w)\tag{19.24}$$
so predictions are consistent across perturbations and confident (low entropy).
- Alternative: pseudolabels (source-model predictions on unlabeled target data) plus self-training, often with regularizers against over-fitting.

### 19.6 Learning from multiple distributions (pp. 751–758)
Train on $J\ge2$ source distributions; Fig. 19.11 maps set-ups to method families (p. 751–752).

**19.6.1 Multitask learning (pp. 751–752).** Labeled data from $J$ distributions $\mathcal D^j=\{(x^j_n,y^j_n)\}_{n=1}^{N_j}$. Learn $f(x,j):\mathcal X\to\mathcal Y_j$ predicting well on all. Example: per-pixel semantic labels $\mathcal Y^1=\{1..C\}^{HW}$ and depth $\mathcal Y^2=\mathbb R^{HW}$. ERM:
$$f^*=\arg\min_f\sum_{j=1}^J\sum_{n=1}^{N_j}\ell_j(y^j_n,f(x^j_n,j))\tag{19.25}$$
with $\ell_j$ suitably scaled. The simplest approach is a shared trunk with multiple output heads (Fig. 19.12). It often does worse than $J$ single-task networks. Cross-stitch networks [Mis+16] combine activations of single-task networks. Multitask learning does not always help because of "task interference" or "negative transfer". Then use separate networks (p. 752).

**19.6.2 Domain generalization (DG) (pp. 752–754).** Train on $J$ labeled source "environments" and test on a new target $t=J+1$. Environments may be bare integer ids or carry meta-data/context variables (time, location, device). Unlike multitask learning, only target accuracy matters and no labeled target data exist. So assumptions are needed on how $p^t(x,y)$ relates to $p^j(x,y)$ (p. 754). One formalization is a hierarchical Bayesian model [Bax00] (Fig. 19.13): $p^t(x,y)=p(x|\phi^t)p(y|x,w^t)$, where $w^t$ derives from a shared population-level $w^0$ (and likewise $\phi^t$). A discriminative model need not model $p(x|\phi^t)$. [GLP21] found that none of many other DG methods worked consistently better than ERM across all provided datasets (p. 754).

**19.6.3 Invariant risk minimization (IRM) (pp. 754–755).** Aims to predict well in all environments while being less prone to spurious features. It extends *invariant causal prediction* (ICP) [PBM16b], which uses hypothesis tests to find the features that *directly cause* the outcome in every environment. Fig. 19.14: with $Y$'s parents $X_2,X_4$ ($X_5\to X_4$, $Y\to X_3$), an invariant predictor must use $\{X_2,X_4\}$. Indirect causes ($\{X_2,X_5\}$) or an incomplete set of direct causes ($\{X_4\}$) may not suffice (p. 754). [Arj+19] extend ICP to high-dimensional inputs (e.g. pixels): find a predictor that works well on average and is optimal in each environment:
$$f^*=\arg\min_{f\in\mathcal F}\sum_{j=1}^J\frac1{N_j}\sum_{n=1}^{N_j}\ell(y^j_n,f(x^j_n))\tag{19.26}$$
$$\text{such that } f\in\arg\min_{g\in\mathcal F}\frac1{N_j}\sum_{n=1}^{N_j}\ell(y^j_n,g(x^j_n))\ \text{ for all } j\in\mathcal E\tag{19.27}$$
Intuition (author): many functions may fit one environment because the problem is underspecified, but the one that works in all environments is more likely to use causal rather than spurious features. Later work shows IRM often does not work well for covariate shift, in theory [RRR21] and practice [GLP21], although it can work well in some anticausal (generative) models [Ahu+21] (p. 755).

**19.6.4 Meta learning (pp. 755–758).** Goal: "learn the learning algorithm". Like DG, but each training distribution is split into train and test parts, so the learner can "practice" generalizing. Summary follows [Gor+19].

*19.6.4.1 Meta-learning as probabilistic inference.* $J$ tasks, each with $\mathcal D^j_{\rm train}=\{(x^j_n,y^j_n)\}_{n=1}^{N^j}$ and $\mathcal D^j_{\rm test}=\{(\tilde x^j_m,\tilde y^j_m)\}_{m=1}^{M^j}$. Task parameters $w^j$, shared parameters $w^0$ (Fig. 19.15). Differences from Fig. 19.13: plate notation, and train/test partitions exist for all distributions (p. 755). A *point estimate* is learned for $w^0$ (shared, little uncertainty). An *approximate posterior* is computed for $w^j$ (little data per task). The posterior predictive for each task:
$$p(\tilde y^j|\tilde x^j,\mathcal D^j_{\rm train},w^0)=\int p(\tilde y^j|\tilde x^j,w^j)\,p(w^j|\mathcal D^j_{\rm train},w^0)\,dw^j\tag{19.28}$$
This is intractable, so learn an amortized approximation $q_\phi(\tilde y|\tilde x,\mathcal D_{\rm train},w^0)$. Choose $w^0$ and the inference network $\phi$ to make the predictive posterior accurate:
$$\phi^*=\arg\min_\phi\mathbb E_{p(\mathcal D_{\rm train},\tilde x)}\big[D_{\mathbb{KL}}(p(\tilde y|\tilde x,\mathcal D_{\rm train},w^0)\,\|\,q_\phi(\tilde y|\tilde x,\mathcal D_{\rm train},w^0))\big]\tag{19.29}$$
$$=\arg\min_\phi\mathbb E_{p(\mathcal D_{\rm train},\tilde x)}\big[\mathbb E_{p(\tilde y|\tilde x,\mathcal D_{\rm train},w^0)}[\log q_\phi(\tilde y|\tilde x,\mathcal D_{\rm train},w^0)]\big]\tag{19.30}$$
$$=\arg\min_\phi\mathbb E_{p(\mathcal D_{\rm train},\tilde x,\tilde y)}\Big[\log\int p(\tilde y|\tilde x,w)\,q_\phi(w|\mathcal D_{\rm train},w^0)\,dw\Big]\tag{19.31}$$
(signs as printed; see Reading notes), using the approximation $p(\tilde y|\tilde x,\mathcal D_{\rm train},w^0)\approx p(\tilde y|\tilde x,\mathcal D_{\rm train})$. Monte Carlo: sample $J$ tasks, each partitioned into train/test, and draw $S$ samples $w^j_s\sim q_\phi(w^j|\mathcal D^j,w^0)$ for the integral. With $M$ test points per task:
$$\mathcal L_{\rm meta}(w^0,\phi)=\frac1{MJ}\sum_{m=1}^M\sum_{j=1}^J\log\Big(\frac1S\sum_{s=1}^S p(\tilde y^j_m|\tilde x^j_m,w^j_s)\Big)\tag{19.32}$$
(p. 756). Standard amortized VI instead approximates the *parameter posterior* given all task data $\mathcal D^j_{\rm all}=\mathcal D^j_{\rm train}\cup\mathcal D^j_{\rm test}$:
$$\mathcal L_{\rm VI}(w^0,\phi)=\frac1J\sum_{j=1}^J\Big(\sum_{(x,y)\in\mathcal D^j_{\rm all}}\Big[\frac1S\sum_{s=1}^S\log p(\tilde y^j|\tilde x^j,w^j_s)\Big]-D_{\mathbb{KL}}\big(q_\phi(w^j|\mathcal D^j_{\rm all},w^0)\,\|\,p(w^j|w^0)\big)\Big)\tag{19.33}$$
Differences: VI takes the *average of a log*, meta-learning the *log of an average* (the latter can give provably better predictive accuracy [MAD20]). Meta-learning optimizes the forward KL, not reverse KL. It has no KL penalty on the parameter posterior (p. 757).

*Intuition note.* Meta-learning scores the model on how well the *training-set-conditioned prediction* matches held-out test points. VI scores how well the parameter posterior fits all data.

*19.6.4.2 Neural processes (p. 757).* If the task inference network gives a point estimate, $q(w^j|\mathcal D^j,w^0)=\delta(w^j-\mathcal A_\phi(\mathcal D^j,w^0))$, then
$$q(\tilde y^j|\tilde x^j,\mathcal D^j,w^0)=\int p(\tilde y^j|\tilde x^j,w^j)q(w^j|\mathcal D^j,w^0)dw^j=p(\tilde y^j|\tilde x^j,\mathcal A_\phi(\mathcal D^j,w^0),w^0)\tag{19.34}$$
where $\mathcal A_\phi$ maps a set to parameters. It can be optimized by standard supervised maximum likelihood. This is a **neural process**.

*19.6.4.3 MAML (p. 757).* $\hat w^j=\mathcal A(\mathcal D^j,w^0)=w^0+\eta\nabla_w\log\sum_{n=1}^{N^j}p(y^j_n|x^j_n,w)\big|_{w^0}$ (19.35, as printed). Task parameters are the shared parameters moved one gradient step along the log conditional likelihood. Multiple steps are possible by feeding the gradient into an RNN [RL17].

*19.6.4.4 Prototypical networks (pp. 757–758).* Let $w^0$ be a shared feature extractor $h_{w^0}(x)$, and $w^j=\{w^j_c,b^j_c\}_{c=1}^C$ the last linear layer. Class means in each task's training set:
$$\mu^j_c=\frac1{|\mathcal D^j_c|}\sum_{x^c_n\in\mathcal D^j_c}h_{w^0}(x^c_n)\tag{19.36}$$
$$\hat w^j=\mathcal A(\mathcal D^j,w^0)=\Big[\mu^j_c,\,-\tfrac12\|\mu^j_c\|^2\Big]_{c=1}^C\tag{19.37}$$
$$q(\tilde y^j=c|\tilde x^j,\mathcal D^j,w^0)\propto\exp(-d(h_{w^0}(\tilde x),\mu^j_c))=\exp\Big(h_{w^0}(\tilde x)^\top\mu^j_c-\tfrac12\|\mu^j_c\|^2\Big)\tag{19.38}$$
with $d$ the Euclidean distance. This is equivalent to prototypical networks [SSZ17]. (Added step: the equality in 19.38 holds, up to a factor constant in $c$, if $d(u,v)=\tfrac12\|u-v\|^2$, since $-\tfrac12\|h-\mu\|^2=h^\top\mu-\tfrac12\|\mu\|^2-\tfrac12\|h\|^2$.)

### 19.7 Continual learning (pp. 758–765)
Continual (life-long) learning: a sequence of distributions $p_1,p_2,\dots$; at step $t$ the model receives
$$\mathcal D_t=\{(x_n,y_n)\sim p_t(x,y)\}_{n=1}^{N_t}\tag{19.39}$$
with $p_t(x,y)=p_t(x)p(y|f_t(x))$, $f_t:\mathcal X_t\to\mathcal Y_t$ unknown. Each distribution is a different **task**. The learner is tested on
$$\mathcal D_t^{\rm test}=\{(x_n,y_n)\sim p_t^{\rm test}(x,y)\}_{n=1}^{N_t^{\rm test}}\tag{19.40}$$
If the test distribution at $t$ includes all tasks up to $t$, the model must not "forget". If it equals the current distribution (online learning, 19.7.5), the learner need only adapt, not remember. Non-stationarity also arises in RL (policy and value function change) (p. 758).

**19.7.1 Domain drift (pp. 758–759).** $p_t(x)$ changes (covariate shift), $f_t$ is constant (e.g. a self-driving car's vision under shifting lighting). Evaluate with $f^{\rm test}_t=f_t$ and $p^{\rm test}_t(x)=p_t$ (current input distribution), or with the union of all seen so far, $p_t^{\rm test}=\cup_{s=1}^Tp_s$ (Fig. 19.16).

**19.7.2 Concept drift (pp. 759–760).** $f_t$ changes, $p_t(x)$ is constant [WK96]. Example: what is classified illegal changes at $t'>t$, so the decision boundary moves (Fig. 19.17). Another: sort by color, then by shape. Here $p(y|x,\text{task})$ is stationary but the task is unobserved, so $p(y|x)$ changes. Since predictions for the same $x$ depend on when they are made, the test distribution must also change over time, or inputs can be tagged with a time stamp or task id (p. 760).

**19.7.3 Class incremental learning (pp. 760–761).** A true static $f:\mathcal X\to\mathcal Y$, but at step $t$ the learner sees only $(\mathcal X,\mathcal Y_t)$ with $\mathcal Y_t\subset\mathcal Y$ (e.g. digits $\{0,1\}$, then $\{2,\dots,9\}$; Fig. 19.18). Scenarios (Fig. 19.19):
- No well-defined task boundaries: *continuous task-agnostic* learning.
- Boundaries exist but are unknown in training: *discrete task-agnostic* learning.
- Boundaries given: *task-aware* learning. If the task label is also known at test time, this is essentially multitask learning. If not, the model must predict task and class (hierarchical label space), commonly with a multi-headed DNN with $CT$ outputs ($C$ classes, $T$ tasks).
- Common setups: *permuted MNIST* (10 classes, pixels permuted) and *split MNIST* (2 classes per step). Footnote 5: in split MNIST, task 1 digits (0,1) are labeled (0,1), and task 2 digits (2,3) are also labeled (0,1) (p. 760).

Head count is usually an input because softmax's sum-to-one constraint prevents incremental estimation of output weights in the open-class setting. Alternatives: enlarge the head when a new class appears (requires storing past data); generative classifiers (no heads); deep nearest-neighbour classifiers (challenge: updating stored prototypes as the feature extractor changes); per-class generative models, e.g. VAEs (easier online learning, possibly less sample efficient) (p. 761). Author's view: most CL work is task-aware, but assuming given task boundaries is "very unrealistic" (e.g. a robot learning from a data stream), so future work should target the task-agnostic setting (p. 761).

**19.7.4 Catastrophic forgetting (pp. 762–763).** Train on a task sequence, test on all tasks at each step. Failure modes: *catastrophic forgetting* (performance on old tasks drops after training on a new one; Fig. 19.20a) and too little plasticity (only the first task is learned, e.g. from too much regularization; Fig. 19.20b). Success looks like no forgetting (Fig. 19.21a) and ideally *forwards transfer* (past tasks help future tasks beyond training from scratch) and *backwards transfer* (future tasks help past tasks). Following [LPR17], with $R_{ij}$ the performance on task $j$ after training on task $i$, $R_j^{\rm ind}$ the performance on $j$ trained only on $j$, and $T$ tasks:
$$\mathrm{FWT}=\frac1T\sum_{j=1}^T R_{j,j}-R_j^{\rm ind}\tag{19.41}$$
$$\mathrm{BWT}=\frac1T\sum_{j=1}^T R_{T,j}-R_{j,j}\tag{19.42}$$
Three method families (p. 763):
- *Regularization*: add a loss preserving old-task information. Online Bayesian inference is of this type, since the posterior comes from the new data and the past prior. Examples: elastic weight consolidation (Sec. 17.5.1), variational continual learning (Supp. Sec. 10.2).
- *Memory*: experience replay or rehearsal, or a generative model of past data.
- *Architectural*: add capacity at task boundaries.

They can be combined, e.g. a semi-parametric model with stored exemplars plus Bayesian online parameter learning [Kur+20]. The right method depends on the desired inductive bias and the time/memory budget.

**19.7.5 Online learning (pp. 763–765).** Similar to CL, but the loss differs and learning and evaluation usually occur at each step. The data distribution $p_t^*(x,y)=p(x|\phi_t)p(y|x,w_t)$ evolves (Fig. 19.22). At step $t$ nature draws $(x_t,y_t)\sim p_t^*$; the agent sees $x_t$ and predicts $y_t$ through the posterior predictive
$$\hat p_{t|t-1}=p(y|x_t,\mathcal D_{1:t-1}),\quad \mathcal D_{1:t-1}=\{(x_s,y_s)\}_{s=1}^{t-1}\tag{19.43}$$
$$\mathcal L_t=\ell(\hat p_{t|t-1},y_t)\tag{19.44}$$
This is **prequential prediction** [DV99; GSR13] (also the basis of online conformal prediction). The aim is to minimize $\mathcal L=\sum_{t=1}^T\mathcal L_t$, the loss at each step, not on a fixed test set. For log-loss this equals the (conditional) log marginal likelihood, $\log p(\mathcal D_{1:T})=\log p(y_{1:T}|x_{1:T})$. This gives the prequential MDL of a model, useful for model selection (p. 764). Another metric, especially with adversarial data, is **regret** against the best in hindsight:
$$\mathrm{regret}=\sum_{t=1}^T\big[\ell(\hat p_{t|t-1},y_t)-\ell(\hat p_{t|T},y_t)\big],\quad \hat p_{t|T}=p(y|x_t,\mathcal D_{1:T})\tag{19.45}$$
Regret bounds can be derived when the loss is convex. Backward-looking regret bounds can be converted into forward-looking risk bounds [HT15] (p. 764). Online learning suits bandits and RL, where there is no fixed train/test phase. CL scenarios are special cases of online learning: one task per step, odd steps train (loss 0), even steps evaluate on the test distribution (possibly the union of past tasks). In CL there is typically a lot of data per task, whereas online learning stresses fast adaptation from small data per step (pp. 764–765).

### 19.8 Adversarial examples (pp. 765–770)
Here an adversary picks inputs to minimize performance. Given $x$ classified as $c$, find $x_{\rm adv}$ perceptually similar to $x$:
$$x_{\rm adv}=\arg\min_{x'\in\Delta(x)}\log p(y=c|x')\tag{19.46}$$
with $\Delta(x)$ the set of "similar" images. Fig. 19.23: a panda (57% confidence) plus tiny structured noise ($\epsilon=0.007$) becomes a "gibbon" at 99%. First noted in [Sze+14]. They are surprisingly easy to create, which seems paradoxical (explained in 19.8.5). Security concerns: sunglasses with a pattern fool face recognition [Sha+16]; stickers make stop signs read as speed-limit signs [Eyk+18]. Models other than deep nets for images, and other domains (audio, text), are also vulnerable (pp. 765–766).

**19.8.1 Whitebox attacks (pp. 766–767).** The attacker knows $\theta$. Perturb $x_{\rm adv}=x+\delta$. *Targeted* attack: force $f(x_{\rm adv})=y'$. *Untargeted*: $f(x+\delta)\neq f(x)$. General objective:
$$x_{\rm adv}=\arg\max_{x'\in\Delta(x)}\mathcal L(x',y;\theta)\tag{19.47}$$
Untargeted: $\mathcal L=-\log p(y|x')$. Targeted: $\mathcal L=\log p(y'|x')$ with $y'\neq y$. Typical constraint is a bounded $\ell_p$ ball:
$$\Delta(x)=\{x':\|x'-x\|_p<\epsilon\}\tag{19.48}$$
(The text says "typically people assume $p=1$ or $p=0$" as printed.) Solvers: bound-constrained BFGS [Sze+14]; the **fast gradient sign** (FGS) method [GSS15]:
$$x_{t+1}=x_t+\delta_t\tag{19.49}$$
$$\delta_t=\epsilon\,\mathrm{sign}(\nabla_x\log p(y'|x,\theta)|_{x_t})\tag{19.50}$$
with $\epsilon>0$ a small learning rate; the gradient is with respect to the input pixels, not the parameters. **PGD** [Mad+18] is an iterated, more powerful version. There is no "best" PGD variant. What matters is step count, step size and the exact loss. Use random restarts, tune carefully and monitor the loss [Car+19] (pp. 766–767).

**19.8.2 Blackbox attacks (pp. 767–768).** Parameters unknown, so use derivative-free optimization. [NYC15] used evolutionary algorithms to create *fooling images* (not visually realistic): noise images (Fig. 19.24) and CPPN-generated patterns (Fig. 19.25; footnote 6 defines a CPPN as composed elementary functions mapping coordinates to colors). [SVK19] attacked via differential evolution by changing a single pixel ($\|x_{\rm adv}-x\|_0=1$). [Pap+17] learned a differentiable surrogate of the blackbox by querying it, attacked the surrogate with gradients, and showed the attacks transferred to cloud classification APIs (Google, Amazon, MetaMind) (p. 768).

**19.8.3 Real-world attacks (p. 768).** The space $\Delta$ is large and hard to define mathematically, since it depends on semantics and attacker goals. The set of variations we want invariance to is the **threat model**. Example: the content-constrained threat model of [Gil+18a], image spam. Here $\Delta$ is all images containing the advertisement concept. Spammers use fonts, orientations and background clutter (Fig. 19.26, built from scratch rather than perturbed). Hand-designed inputs can be easier with limited-query blackbox access.

**19.8.4 Defenses based on robust optimization (p. 769).** For general threat models, securing a system "seems extraordinarily difficult". Research instead targets $\ell_p$-robustness. Solving this toy threat model has little security application, but smoothness priors have in some cases improved robustness to random corruptions, improved transfer, and biased models toward different features. *Adversarial training* (robust optimization) optimizes the adversarial risk:
$$\min_\theta\ \mathbb E_{(x,y)\sim p(x,y)}\Big[\max_{x'\in\Delta(x)}\mathcal L(x',y;\theta)\Big]\tag{19.51}$$
This needs a non-concave inner maximization and a non-convex outer minimization, and the inner max is NP-hard in general [Kat+17]. In practice it may suffice to take $\nabla_\theta\mathcal L(x_{\rm adv},y;\theta)$ at an approximate inner maximizer. Best practice uses a few PGD steps. *Certification*: randomized smoothing [CRK19] turns a noise-robust model into one provably robust to bounded worst-case $\ell_2$ perturbations. For ReLU networks, local linearity reduces certification to linear programs [WK18].

**19.8.5 Why models have adversarial examples (pp. 769–770).** Author's argument: if accuracy drops on some shifted $p_{\rm te}(x)\ne p_{\rm tr}(x)$, the model is necessarily vulnerable to attack. If errors exist there is a nearest one. In high dimension the nearest error should be much closer than errors sampled from $p_{\rm te}$ (p. 769). Fig. 19.27a: $x_0$ clean, $B$ a Gaussian-noise corruption, $A$ adversarial. With a *linear* decision boundary the error set $E$ is a half-space. With $\mu=\mathbb P_{\delta\sim N(0,\sigma I)}[x_0+\delta\in E]$:
$$d(x_0,E)=-\sigma\Phi^{-1}(\mu)\tag{19.52}$$
($\Phi^{-1}$ the inverse Gaussian cdf). A random noisy image has $\|\delta\|_2\approx\sigma\sqrt d$ with high probability. Example: ImageNet $d=224\times224\times3$, $\sigma=.2$, $\mu=.01$: (19.52) gives $d(x_0,E)=.5$, versus $\sigma\sqrt d\approx77.6$, so the adversarial example is more than 100 times closer (p. 770). This is **concentration of measure**: small-volume error sets close to most points of a high-dimensional distribution. Conclusion: worst-case errors "will always exist as long as errors exist" (p. 770).

*Intuition note.* In high dimensions random noise travels far from $x_0$ (about $\sigma\sqrt d$), but a single well-chosen direction crosses a flat boundary after a tiny step. So, if the boundary is locally linear, a small error rate in noise already means adversarial errors are very near.

## Toy example (ours, not from the text): label shift with blackbox shift estimation
Two classes. Source prior $p(y)=(0.5,0.5)$. Confusion matrix of a fixed classifier on source data, $C_{ij}=p(\hat y=i|y=j)$:
$$C=\begin{pmatrix}0.9&0.2\\0.1&0.8\end{pmatrix}$$
(columns sum to 1). Suppose the unknown true target prior is $q=(0.8,0.2)$. We only observe prediction frequencies:
$$\mu=Cq=(0.9\cdot0.8+0.2\cdot0.2,\ 0.1\cdot0.8+0.8\cdot0.2)=(0.72+0.04,\ 0.08+0.16)=(0.76,\ 0.24).$$
Recover $q$: $\det C=0.9\cdot0.8-0.2\cdot0.1=0.72-0.02=0.70$, and
$$C^{-1}=\tfrac1{0.7}\begin{pmatrix}0.8&-0.2\\-0.1&0.9\end{pmatrix}.$$
Then $q=C^{-1}\mu=\tfrac1{0.7}(0.8\cdot0.76-0.2\cdot0.24,\ -0.1\cdot0.76+0.9\cdot0.24)=\tfrac1{0.7}(0.608-0.048,\ -0.076+0.216)=\tfrac1{0.7}(0.56,0.14)=(0.8,0.2)$. ✓.

Correct a prediction (eq. 19.23). Take an input $x$ with $p(y|x)=(0.6,0.4)$. Weights $q(y)/p(y)=(1.6,0.4)$. Unnormalized: $(0.6\cdot1.6,\ 0.4\cdot0.4)=(0.96,0.16)$, sum $1.12$. So $q(y|x)=(0.96/1.12,\ 0.16/1.12)\approx(0.857,0.143)$. The $p(x)/q(x)$ factor is absorbed by this normalization. The classifier's 60% for class 1 becomes about 86% because class 1 is now more prevalent.

## Concepts
- [[distribution-shift]] (new) — test/target $q(x,y)$ differs from training/source $p(x,y)$ (p. 735)
- [[spurious-correlation-shortcut-features]] (new) — features predictive in training but not stable across distributions (p. 736)
- [[covariate-shift]] (new) — $p(x)$ changes, $p(y|x)$ fixed; also domain shift (p. 738)
- [[concept-shift]] (new) — $p(y|x)$ changes (annotation shift); not fixable without labeled target data (p. 739)
- [[label-shift]] (new) — $p(y)$ changes, $p(x|y)$ fixed; prior/prevalence shift (p. 739)
- [[manifestation-shift]] (new) — $p(x|y)$ changes (conditional shift), often via a hidden confounder (p. 739)
- [[confounding-vs-selection-bias]] — selection on both $X$ and $Y$ can induce non-causal dependence, called selection bias (p. 740)
- [[causal-dag]] — causal (X→Y) vs anticausal (Y→X) prediction and selection diagrams (pp. 737, 740)
- [[ood-detection]] (new) — decide whether a single input is in- or out-of-distribution (p. 741)
- [[importance-weighting]] (new) — weight source losses by $q(x)/p(x)$ to estimate target risk under covariate shift (p. 748)
- [[blackbox-shift-estimation]] (new) — solve $\mu=Cq$ for the new label prior using a confusion matrix (p. 750)
- [[domain-adaptation]] (new) — use unlabeled target data to make predictors invariant/robust, e.g. domain adversarial learning (p. 749)
- [[domain-generalization]] (new) — train on several labeled environments, test on a new unseen one (p. 752)
- [[invariant-risk-minimization]] (new) — predictor that works well on average and is optimal in every environment, aiming to be less prone to spurious features (p. 754)
- [[hierarchical-model]] — population-level $w^0$ generating task/environment parameters $w^j$ (pp. 754–755)
- [[learning-to-learn]] — meta-learning as hierarchical Bayesian prediction from train to test split per task (p. 755)
- [[kl-divergence]] — forward KL on the predictive posterior is the meta-learning objective (p. 756)
- [[variational-inference-elbo]] — standard objective (19.33) contrasted with meta-learning (19.32) (p. 757)
- [[posterior-predictive-distribution]] — per-task predictive integrates over task-parameter posterior (p. 755)
- [[continual-learning]] (new) — learn from a sequence of distributions; catastrophic forgetting is one of two main failure modes (pp. 758, 762)
- [[catastrophic-forgetting]] (new) — performance on a past task drops after training on a new task (p. 762)
- [[online-learning-regret]] (new) — prequential loss per step; regret vs hindsight-optimal predictor (p. 763)
- [[marginal-likelihood]] — for log-loss, cumulative online loss equals conditional log marginal likelihood (p. 763)
- [[adversarial-example]] (new) — worst-case input in a similarity set that minimizes the model's performance (p. 765)
- [[concentration-of-measure]] (new) — small-volume error sets lie close to most points in high dimension (p. 770)

## Canonical instances
- [[cow-on-beach]] — grassy training backgrounds make a classifier fail on cows on beaches (p. 736)
- [[pneumonia-metal-tokens]] — CNN uses hospital tokens, not lungs, so fails at new hospitals (p. 737)
- [[fashion-mnist-vs-mnist-ood-likelihood]] — pixel-CNN and flow models trained on Fashion-MNIST give higher likelihood to MNIST (p. 743)
- [[sgld-vs-sgd-selective-prediction]] — on Fashion-MNIST the SGLD MLP predicts on fewer inputs than the SGD MLP (about 70% vs 97% at threshold 0.5) (p. 744)
- [[panda-gibbon-fgs]] — tiny perturbation ($\epsilon=0.007$) flips a 57% panda to a 99% gibbon (p. 765)
- [[imagenet-adversarial-distance]] — $d=150{,}528$ dims, $\sigma=.2$, $\mu=.01$ gives $d(x_0,E)=.5$ vs $77.6$ (p. 770)
- [[permuted-split-mnist]] — common task-aware continual-learning experimental setups (p. 760)

## Bridges (candidates)
- [same-math] Importance weighting $w=q(x)/p(x)$ for target risk (19.12–19.16) ↔ Monte Carlo integration: importance sampling re-expresses an expectation under $q$ as one under $p$ times a density ratio.
- [same-math] Blackbox shift estimation $\mu=Cq$ ↔ linear inverse problems / moment matching: observed prediction rates are a known linear mixture of the unknown label prior. The author calls it moment matching (p. 750).
- [same-math] Prequential log-loss $\sum_t\log \hat p_{t|t-1}$ ↔ Marginal likelihood (evidence): chain-rule decomposition into one-step-ahead predictive terms (p. 763).
- [structural-analogy] Selection variable $S$ in Fig. 19.5 ↔ Confounding vs selection bias: conditioning on a common effect of $X$ and $Y$ creates non-causal dependence.
- [structural-analogy] Hierarchical Bayesian DG and meta-learning models (Figs. 19.13, 19.15) ↔ Hierarchical models / partial pooling: task parameters drawn from a shared population level.
- [structural-analogy] Adversarial examples via $\|\delta\|\approx\sigma\sqrt d$ ↔ Typical set: in high dimensions mass sits in a thin shell far from the center, so ordinary and worst-case distances differ greatly.
- [metaphor] Catastrophic forgetting vs regularization to past posterior ↔ Sequential updating: yesterday's posterior as today's prior (the author says online Bayesian inference is of this type, p. 763).

## Questions this raises
- How can one tell from data alone which of the four shift types (covariate, concept, label, manifestation) has occurred, given that the remedies' assumptions are untestable without target labels?
- When $q(x)>0$ but $p(x)\approx0$, importance weights explode. What is the practical variance–bias trade-off, and what do weight-clipping or regularization options look like?
- Why does the log-of-average meta-learning objective (19.32) give better predictive accuracy than the average-of-log VI objective (19.33), and when does the difference matter?
- If IRM often fails under covariate shift and ERM matches most DG methods [GLP21], what assumptions about environments would make invariance learnable?

## Reading notes
- Page offset: printed = pdf − 34 (pdf 769 = printed 735). All page refs are printed pages.
- Eq. (19.6) breaks across pages: the equation line at the foot of p. 743 ends with the log-determinant terms, and p. 744 shows only the tag "(19.6)". The final equality $=R(x)$ is not printed; I supplied the cancellation as an added step.
- Eq. (19.22): the printed sum is $\sum_i C_{ij}q_j$; the index should run over $j$.
- Eq. (19.30)–(19.31) are printed with "argmin" and no minus sign on $\log q_\phi$. Since $D_{\rm KL}(p\|q)=\mathbb E_p[\log p]-\mathbb E_p[\log q]$, minimizing KL maximizes $\mathbb E_p[\log q_\phi]$. Eq. (19.32) is written as a log-likelihood to be maximized. The sign convention is inconsistent as printed. Also the Fig. 19.15 caption says "$\theta$ are the shared parameters" while the text and figure use $w^0$.
- Eq. (19.35): the sum over $n$ appears *inside* the log ($\log\sum_n p(\cdot)$), whereas the prose says "log conditional likelihood" (which would normally be a sum of logs). I copied it as printed.
- Eq. (19.38): "$d$ is the Euclidean distance". The stated equality with $h^\top\mu-\frac12\|\mu\|^2$ holds only for a half squared distance, up to a $c$-independent term. See the added step.
- Eq. (19.19): as printed, $\beta$ (the domain classifier) is in the max with $\alpha$, and the prose says the objective maximizes the domain loss. Check against [Gan+16a] before teaching the exact roles.
- 19.3.2.3: the text says to set $\lambda_1$ "as large as possible" to detect OOD. Given $\mathcal T=\emptyset$ when $\mathrm{OOD}(x)>\lambda_1$, the direction depends on the sign convention of the OOD score, which the text does not state. 19.3.3 says abstain "if $p$ is below some threshold" where $p$ is described as confidence that input is OOD. This reads reversed. In 19.3.3.1 confidence is the probability of the MAP class.
- 19.8.1: "typically people assume $p=1$ or $p=0$" as printed.
- The FWT formula (19.41) is printed as $\frac1T\sum_j R_{j,j}-R_j^{\rm ind}$; the sum's scope is not bracketed.
- Figure 19.27 caption uses $n$ for input dimension, text uses $d$.
- The online version footer says "December 10, 2025". Cross-referenced sections (e.g. 2.7.3, 14.3, 17.5, 34.2) are outside this unit.
