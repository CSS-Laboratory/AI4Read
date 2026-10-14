---
id: grimmer-2022-textasdata/ch19-classifying
work: grimmer-2022-textasdata
unit: Chapter 19. Classifying Documents with Supervised Learning
pages: 318-336
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Classifying Documents with Supervised Learning

## L0 — One line
Supervised classifiers, from Naive Bayes to deep networks, can essentially all be seen as fitting labelled examples by minimizing a loss plus a complexity penalty, and the fitted model then labels (or measures) a much larger unlabelled corpus.

## L1 — The gist (≤ 120 words)
How can human labels on a small training set be extended to a large corpus? The chapter derives Naive Bayes: a simple classifier that models how classes generate words. Its independence assumption is almost certainly wrong, but this need not make it useless. It then frames essentially all classifiers as minimizing a loss plus a complexity penalty (regularization). Fixed basis functions use feature transformations chosen in advance; adaptive ones, such as neural networks, learn the features from the data. If only class proportions matter, Hopkins and King's ReadMe estimates them directly. Nielsen's "Jihad Score" shows a Naive Bayes log-odds used as a continuous measure. Classifier error should be accounted for in later analyses. Validation follows in Chapter 20.

**Prerequisites:** Bayes' rule; multinomial distribution; linear regression and least squares; logarithms; the idea of overfitting; document-feature matrices.

## L2 — Key ideas (5–10 bullets)
- Supervised learning approximates the human label mapping with a function of text features, chosen by optimizing a loss function. It is explained by analogy to linear regression (p. 318).
- Naive Bayes combines class prevalence with a class-specific word distribution, assuming words are independent given the class. Smoothing with a constant $c$ avoids zero probabilities (pp. 320–321).
- The independence assumption is "almost certainly wrong". The authors' point is to assess its effect, not to dismiss the method. It tends to make predicted probabilities overconfident and poorly calibrated (not matching true frequencies), so averaging them gives a poor estimate of class shares (p. 322).
- Naive Bayes is generative (it models how documents arise given a class); its discriminative analogue, multinomial logistic regression, models the label given the features directly. Naive Bayes tends to do better with small samples if its assumptions roughly hold (pp. 323–324).
- Essentially all classifiers can be seen as solving $\arg\min_\mu \sum_i L(\cdot) + R(\mu,\lambda)$ (loss plus regularizer, a penalty on model complexity). They differ in loss, regularizer and feature transformation (pp. 326–327).
- Fixed basis functions (transformed versions of the features) are fixed in advance. Adaptive ones (neural networks) learn features, which requires substantially more data (pp. 328–330).
- If the target is class proportions, ReadMe bypasses individual classification and avoids Naive Bayes independence, at the cost of losing individual document classifications (pp. 331–332).
- Nielsen's Jihad Score treats Naive Bayes log-odds (the log of the odds of one class against another) as a continuous measure ("predictability as measurement"). How to incorporate classifier uncertainty into downstream analysis is an understudied problem that needs attention (pp. 333–335).

## L3 — Walkthrough

### Chapter introduction (p. 318)
- Supervised learning fits a statistical model to the mapping between training examples and their labels. It then predicts labels for the larger unlabelled set, "amplifying" human effort (p. 318).
- Reading aid: linear regression approximates $y$ by $X\beta$ and picks $\beta$ by minimizing the loss $\sum_{i=1}^N (y_i - X_i\beta)^2$. A classifier approximates the labels $y$ by some function of the features $W$ and has its own loss (p. 318).
- Features can be transformed, multiplied or layered. The feature space then grows very large, so regularization (automatically reducing model complexity) is needed to keep fitting tractable and to prevent overfitting (p. 318).
- Performance should be evaluated on data not used for fitting, so some training data is held out. Details are in Chapter 20 (p. 318).

### 19.1 Naive Bayes (pp. 320–322)
Setup. Document $D_i$ has a label $y_i\in\{1,\dots,K\}$ (mutually exclusive, exhaustive classes). Recode it as a length-$K$ vector $\pi_i$ with $\pi_{ik}=1$ if $y_i=k$, else 0 (p. 320).

Bayes rule:
$$p(\pi_{ik}=1\mid D_i)=\frac{p(\pi_{ik}=1,D_i)}{p(D_i)}\tag{19.1.1}$$
$$=\frac{p(\pi_{ik}=1)\,p(D_i\mid\pi_{ik}=1)}{p(D_i)}.\tag{19.1.2}$$
The denominator is the same for all classes. Drop it and normalize at the end (p. 320):
$$\underbrace{p(\pi_{ik}=1\mid D_i)}_{\text{prediction}}\propto\underbrace{p(\pi_{ik}=1)}_{\text{prevalence of class }k}\;\underbrace{p(D_i\mid\pi_{ik}=1)}_{\text{category-specific language model}}.\tag{19.1.3}$$

- Prevalence $p(\pi_{ik}=1)=\alpha_k$ is estimated as the training share in class $k$, assuming a random sample of documents (p. 320):
$$\hat\alpha_k=\frac{\sum_{i}^{N}\mathbb I(y_i=k)}{N}.\tag{19.1.4}$$
- The "naive" assumption: each token is drawn independently given the class. With $W_{i,\cdot}$ the word-count row for document $i$ and $\mu_k$ the word probabilities in class $k$ (p. 320):
$$W_{i,\cdot}\mid\pi_{ik}=1\sim\text{Multinomial}\Big(\sum_j W_{ij},\ \mu_k\Big)\tag{19.1.5}$$
$$p(W_{i,\cdot}\mid\pi_{ik}=1)\propto\prod_{j=1}^{J}\mu_{kj}^{W_{ij}}.\tag{19.1.6}$$
- The idea is general. With other feature types, such as continuous ones, one would factorize differently. The assumption is almost certainly wrong, but it gives parameters that are easy to estimate (p. 321).
- Estimate: pool all class-$k$ training documents and take word frequencies (p. 321):
$$\hat\mu_{kj}=\frac{\sum_i^N\pi_{ik}W_{ij}}{\sum_i\sum_j\pi_{ik}W_{ij}}.\tag{19.1.7}$$
- Problem: a word never seen in class $k$ gets probability 0, which rules out class $k$ for any document containing it. Fix: add a small constant $c$ for each word (p. 321):
$$\hat\mu_{kj}=\frac{c+\sum_i^N\pi_{ik}W_{ij}}{Jc+\sum_i\sum_j\pi_{ik}W_{ij}}.\tag{19.1.8}$$
With $c=1$ this is like adding one new document per class containing every vocabulary word once. It is the Laplace smoothing of Chapter 6 (p. 321).
- Full algorithm and prediction (p. 321):
$$p(\pi_{ik}=1\mid W_{i,\cdot})\propto\alpha_k\prod_{j=1}^{J}\mu_{kj}^{W_{ij}}\tag{19.1.9}$$
$$\hat y_i=\arg\max_k\ \hat\alpha_k\prod_{j=1}^J\hat\mu_{kj}^{W_{ij}}\tag{19.1.10}$$
$$=\arg\max_k\ \log(\hat\alpha_k)+\sum_j^J W_{ij}\log(\hat\mu_{kj}).\tag{19.1.11}$$
Taking logs improves numerical stability and preserves the maximum (p. 321).

*Intuition note.* Naive Bayes builds a "prototype" word profile per class from the training documents. A new document goes to the class whose prototype it resembles most, after correcting for how common the class is (pp. 321–322).

**19.1.1 The assumptions are almost certainly wrong (p. 322).**
- The authors believe all such independence assumptions are wrong for real language. Being wrong does not necessarily make the method useless. A "dangerous trap" is to dismiss or rebuild a method because its assumptions are wrong without assessing their effect (p. 322).
- Benefit: the parameter count falls to $(J-1)K+(K-1)$. The model is limited (it cannot capture word interactions) but needs relatively little data (p. 322).
- Cost: it tends to be overconfident. It treats each extra word count as new information, but words are "bursty" (once used, more likely to be used again). Class choices are often right, but predicted probabilities are poorly calibrated. Hence averaging predictions gives a poor estimate of the total proportion in a class (p. 322).

**19.1.2 Naive Bayes is a generative model (pp. 323–324).**
- It maximizes a joint distribution $p(\pi_{ik}=1,D_i)=p(D_i\mid\pi_{ik}=1)p(\pi_{ik}=1)$. It can be seen as a mixture model (Part 3) with some components labelled in advance (p. 323).
- Generative models are easy to build on, adapt and interpret. Examples: the constant $c$ can be read as a Bayesian prior (the pseudo-document); burstiness can be addressed with the Dirichlet compound multinomial (Elkan, 2006) (p. 323).
- **Question the authors pose:** if the aim is $p(y_i\mid D_i)$, why learn $p(D_i\mid y_i)$? Can't we maximize $p(y_i\mid D_i)$ directly? **Their answer:** yes. This gives discriminative models, which condition only on the features, as in regression (p. 323).
- The discriminative analogue is multinomial logistic regression (also logistic regression or softmax classifier) (p. 323), as printed:
$$p(\pi_{ik}=1\mid W_{i,\cdot})\propto\exp(W_{i,\cdot}\mu).\tag{19.1.12}$$
- **Ng and Jordan (2002):** logistic regression has higher asymptotic accuracy, but Naive Bayes approaches its own asymptotic accuracy faster. So with small training samples, expect Naive Bayes to beat logistic regression if the assumptions approximately hold (pp. 323–324). The authors link this to the asymptotic-efficiency motivation of Multinomial Inverse Regression (Chapter 11) (p. 324).
- Discriminative models take extra covariates easily: add the variable (e.g. upvotes) next to word counts. A generative model needs a generative process for it, though modelling inputs does help with missing input data (p. 324).
- The two types are not a clean dichotomy. Part of Naive Bayes's small-data success is "almost certainly" due to its generative structure, which also explains why it is seldom seen in production systems with millions of training examples (p. 324).

**19.1.3 Naive Bayes is a linear classifier (pp. 324–325).**
- Linear form, with $f$ converting the linear combination to the prediction space (the $\mu$ here need not match the earlier $\mu$):
$$\hat y_i=f\Big(\mu_0+\sum_{j=1}^J\mu_jW_{ij}\Big).\tag{19.1.13}$$
- The logged Naive Bayes rule has this form, with $\tilde\mu_0=\log(\hat\alpha_k)$ and $\tilde\mu_j=\log(\hat\mu_{kj})$ (p. 324):
$$\hat y_i=\arg\max_k\Big[\underbrace{\log(\hat\alpha_k)}_{\tilde\mu_0}+\sum_j^J W_{ij}\underbrace{\log(\hat\mu_{kj})}_{\tilde\mu_j}\Big]\tag{19.1.14}$$
$$=f\Big(\tilde\mu_0+\sum_{j=1}^J\tilde\mu_jW_{ij}\Big).\tag{19.1.15}$$
- Linear classifiers are fast to train and less prone to overfitting than more sophisticated ones. They cannot capture meaningful interactions between features; this works well in settings where the supplied features are meaningful and useful on their own. The next section covers methods that build better features but need more data (pp. 324–325).

### 19.2 Machine Learning (pp. 326–332)
The general problem (inspired by Mullainathan and Spiess 2017): essentially all classifiers solve (p. 326)
$$\arg\min_\mu\sum_{i=1}^N\underbrace{L\big(f(W_{i,\cdot},\mu),y_i\big)}_{\text{training loss}}+\underbrace{R(\mu,\lambda)}_{\text{regularization}}.\tag{19.2.1}$$
Minimize training error (loss $L$) by choosing $\mu$ defining $f$, subject to a complexity penalty $R$ whose strength is $\lambda$ (p. 326).

*Ordinary least squares* (p. 326):
$$L(f(W_{i,\cdot},\mu),y_i)=(y_i-f(W_{i,\cdot},\mu))^2\tag{19.2.2}$$
$$f(W_{i,\cdot},\mu)=W_{i,\cdot}\mu\tag{19.2.3}$$
$$R(\mu,\lambda)=0\tag{19.2.4}$$
$$\arg\min_\mu\sum_{i=1}^N(y_i-W_{i,\cdot}\mu)^2.\tag{19.2.5}$$
The prediction is $\hat y_i=\sum_jW_{ij}\mu_j$, a weighted sum of features with one weight per feature.

*Softmax classifier* (baseline for multi-category outcomes). The softmax $\sigma(a)_k=\exp(a_k)/\sum_{k'=1}^K\exp(a_{k'})$ maps real values to the simplex (the set of non-negative vectors summing to 1) (p. 326). The full model (p. 327):
$$L(f(W_{i,\cdot},\mu),y_i)=-y_i\log\big(f(W_{i,\cdot},\mu)\big)\tag{19.2.6}$$
$$f(W_{i,\cdot},\mu)=\frac{\exp(W_{i,\cdot}\mu_k)}{\sum_{k'=1}^K\exp(W_{i,\cdot}\mu_{k'})}\tag{19.2.7}$$
$$R(\mu,\lambda)=0\tag{19.2.8}$$
$$\arg\min_{\mu_k}\sum_{i=1}^N-y_i\log\frac{\exp(W_{i,\cdot}\mu_k)}{\sum_{k'=1}^K\exp(W_{i,\cdot}\mu_{k'})}.\tag{19.2.9}$$
It is a linear classifier whose predictions for each category are always nonzero and sum to 1 (p. 327).

*Intuition note.* Complicated models can often be written as a linear model on transformed features. One way to see them is as a search for the transformation that makes the linear model work (p. 327).

**19.2.1 Fixed basis functions (pp. 327–329).**
- The linear predictor is linear and additive in $W_{i,\cdot}$. Including nonlinear transformations $h(W_{i,\cdot})$ gives $f=h(W_{i,\cdot})\mu$, linear in the parameters but nonlinear in the predictors (p. 327).
- Examples: polynomials $h(W_{ij})=(W_{ij},W_{ij}^2,\dots,W_{ij}^b)$ and all pairwise interactions $W_{ij}W_{ij'}$ (basis function expansion). The author says any continuous function can be represented as a linear function on some set of basis functions. The difficulty is specifying the "right" ones (p. 328).
- Fixed basis models commit to the basis functions before estimation and optimize the weights $\mu$. A *global* basis function (e.g. a polynomial) has a coefficient affected by data over the whole range of $W$. A *local* one models a local region. Splines suit smooth functions; wavelets suit sharp discontinuities (p. 328).
- Document-feature matrices are already high-dimensional. Expansion can push the number of features beyond the number of documents. Then $\mu$ cannot be estimated without a constraint, so a regularizer $R(\mu,\lambda)$ expresses a preference for simpler functions (p. 328).
- **Ridge** ($\|\mu\|_2^2$) shrinks parameters smoothly toward zero. **Lasso** ($\|\mu\|_1$) induces sparsity, setting many parameters exactly to zero. Sparsity helps when most features are believed uninformative but we do not know which. Example: in product-review sentiment, most words describe the product and carry little sentiment information (p. 328).
- Table 19.1 lists fixed-basis models, as printed (loss; regularization): regression (squared error; none), lasso (squared error; $\sum_j|\mu_j|$), ridge (squared error; $\sum_j\mu_j^2$), support vector machines ($\max(0,y_i(W_{i,\cdot}\mu))$; $\sum_j\mu_j^2$). Adaptive models: classification and regression trees (loss varies; depth, nodes, information gain at splits), boosting (linear combination of classifiers; learning rate, iterations), neural networks (cross-entropy or mean squared error; layers, neurons, iterations) (p. 327).
- If parameters are truly sparse, a sparsity-promoting penalty is uncontroversial. In social science we may believe the world is full of small but generally nonzero effects, so the parameter vector is dense. Hastie, Tibshirani and Friedman's "bet on sparsity" advice: "use a procedure that does well in sparse problems, since no procedure does well in dense problems" (p. 329).
- Fixed basis models with regularization give great control over complexity. They work best when features carry much independent information about the outcome, and they tend to beat alternatives when data is limited (p. 329).

**19.2.2 Adaptive basis functions (pp. 329–330).**
- When features are informative, supervised learning is relatively easy and the main challenge is high dimensionality, handled by regularization. For complicated categories, word-count features may be insufficient. One can do "feature engineering" by hand (p. 329).
- Recent trend: learn the most predictive features from the data. This needs substantially more data and is less efficient than a correctly specified fixed basis model, but takes less human effort (p. 329).
- Neural network idea. Perhaps new features $\tilde W_{i,\cdot}=(\tilde W_{i1},\dots,\tilde W_{iJ})$, an unknown function of $W_i$, make $\sigma(\tilde W_{i,\cdot}\mu)$ classify better than $\sigma(W_{i,\cdot}\mu)$. Learn each as $\tilde W_{ij}=f(W_{i,\cdot},\mu^W)$ with its own weight matrix (pp. 329–330).
- A popular choice is the Rectified Linear Unit: $\tilde W_{ij}=\max(0,\mu^W_{ij}W_{i,\cdot})$, i.e. the weighted linear combination of all $W_{i,\cdot}$ or 0, whichever is larger. This set of unobserved features is a "hidden layer" (p. 330).
- Like fixed basis functions, the layer allows nonlinear and interactive functions, but it is learned inductively. The analyst chooses the number of hidden features (the layer's "breadth"), which sets flexibility (p. 330).
- "Deep learning" came when computing power and data allowed stacked hidden layers, each predicting the next. Empirically, decreasing breadth while increasing depth lets hidden features learn progressively more abstract concepts that generalize well (p. 330).
- The field's focus has shifted from feature engineering to network architectures. The authors give only a brief summary and point to Goodfellow et al. (2016), Chang and Masterson (2020) and Hvitfeldt and Silge (2021) (p. 330).

*Intuition note.* In a fixed basis model you choose the new features and the data picks the weights. In a neural network the data also picks the features; the authors note this requires substantially more data (pp. 329–330).

**19.2.3 Quantification (pp. 330–332).**
- Often only the *proportion* of documents per category matters. Example: King, Pan and Roberts grouped censored and uncensored blog posts into topics to study the motivation for Chinese censorship, and cared about shares per category (p. 331).
- Hopkins and King (2010): to estimate $p(\pi)=p(\pi_1,\dots,\pi_K)$, one can gain substantially in accuracy by targeting it directly and bypassing individual classifications. Their software and strategy: ReadMe (p. 331).
- Their representation: word *indicators* (occurs or not), not counts. With no independence assumptions there are $2^J$ possible documents. Define $p(W)$ over them, $p(W\mid\pi)$ (a $2^J\times K$ matrix) and $p(\pi)$ (a length-$K$ vector). Without further assumptions (p. 331):
$$p(W)=p(W\mid\pi)\,p(\pi).\tag{19.2.10}$$
- If $p(W)$ and $p(W\mid\pi)$ were known, solving for $p(\pi)$ is simple matrix algebra. $p(W)$ can be estimated from the test set. $p(W\mid\pi)$ is too high-dimensional to estimate without assumptions, so King and Lu (2008) and Hopkins and King (2010) compute it from the training set using matrix smoothing algorithms. This keeps dependence across many features. Equation 19.2.10 resembles Naive Bayes but avoids its independence assumptions. Jerzak, King and Strezhnev (2019) consider alternate models for $p(W\mid\pi)$ (p. 331).
- Gains: weaker training-data assumptions. The training data need not be a random sample but only share $p(W\mid\pi)$, which the authors call more plausible for documents not yet written. It also helps correct a bias of individual classifiers with a large number of categories. **Authors' example:** five documents each with probability 0.2 of being in category $k$ would be placed by an individual classifier all in a different category, whereas ReadMe can add these to the category-$k$ proportion (p. 332).
- Limits: it loses individual classifications. It is less practical with few documents or when relating results to an external covariate (e.g. sentiment by individual). With many documents per covariate value, run it per stratum. With continuous or many-valued covariates, individual classification is needed (p. 332).

**19.2.4 Concluding thoughts (p. 332).** A reasonable measurement strategy: define categories, have humans annotate a random subset, train an algorithm to predict them. As long as it predicts accurately on the kind of documents to be measured, it "doesn't much matter" which algorithm is used. Further reading: Bishop (2006), Eisenstein (2019), Murphy (2021), Aggarwal (2018) (p. 332).

### 19.3 Example: Estimating Jihad Scores (pp. 333–335)
- Nielsen (2017), *Deadly Clerics*, asks why some Muslim clerics express support for violent jihad. He argues that blocked ambition (being shut out of prominent government jobs) is a major driver (p. 333).
- He collects the first census of Muslim clerics on the web with their online writings (articles, books, sermons, fatwas = legal rulings). These capture *expressed ideology*. He aggregates all texts per cleric (p. 333).
- Training set: "supervision with found data" (existing labels), namely "The Jihadist's Bookbag" (an introduction to jihadist ideology) plus a curated set of non-jihadist texts (p. 333).
- Naive Bayes estimates the probability that a cleric's writings fall in the Bookbag versus the non-jihadist set. He uses the output not directly but to build a continuous "Jihad Score". Under NB assumptions it is the log-odds of the jihad class, assuming equal prior odds (Beauchamp 2011; Perry and Benoit 2017) (p. 333):
$$\text{Jihad Score}_i=\frac{1}{\sum_jW_{ij}}\sum_jW_{ij}\underbrace{\log\frac{\mu_{j1}}{\mu_{j0}}}_{\text{word score}}\tag{19.3.1}$$
with $\mu_{j1}$ and $\mu_{j0}$ the probability of word $j$ in a jihadist or non-jihadist document.
- A word more probable in jihadist documents contributes positively. One more probable in non-jihadist documents contributes a lower score (negative, since the log-ratio is below 0; added step). The log-ratio is a word weight, summed over the cleric's words. Figure 19.1 plots the weights (e.g. "apostasy", "jihad", "religion" on the jihadi side; "prayer", "correct", "hadith" on the not-jihadi side, by position and size in the image) (pp. 333, 335).
- Probabilities are estimated from the training set. Scores are validated several ways (Chapter 20). Nielsen then supports his hypothesis that blocked ambition is a significant cause of turning to support violence (p. 334).
- The authors call this "predictability as measurement". It is common in low-dimensional embedding methods, where humans can hardly judge exact continuous values. It is related to Chapter 11's fictitious prediction problem (p. 334).
- Here the prediction is not fictitious, because classifying clerics would itself be useful. **Authors' reading:** Nielsen generally treats scores as an indicator of how likely a cleric supports violent jihad, but at times seems to suggest they also measure intensity. Others claim more directly that class prediction measures intensity of ideology (Beauchamp 2011) and polarization (Gentzkow, Shapiro, Taddy 2019). Predictability is then a surrogate for the underlying dimension (p. 334).
- **Uncertainty.** The authors call it understudied. A classifier-based measure has error, so ignoring it gives an inaccurate sense of uncertainty. If errors are systematically related to other variables, it could add omitted variable bias (Fong and Tyler 2020). Nielsen uses a block bootstrap: resample each cleric's words with replacement and recompute the score. Fong and Tyler propose a general-method-of-moments alternative (p. 335). The same problem applies to hand coding, where annotation error is often ignored (p. 336, footnote).

### 19.4 Conclusion (p. 336)
Naive Bayes was covered for intuition. Then fixed and adaptive basis function models were reviewed through linear regression, and Nielsen's cleric measure showed a Naive Bayes variant in use. Validation comes next (p. 336).

## Toy example (ours, not from the text)
Two classes, vocabulary $J=3$ words (tax, war, peace), $c=1$. Training: 10 documents, 3 in class 1, so $\hat\alpha_1=3/10=0.3$ and $\hat\alpha_2=0.7$.
- Class 1 word counts (tax, war, peace) = (6, 3, 0), total 9. Class 2 counts = (1, 2, 7), total 10.
- Unsmoothed (19.1.7): $\hat\mu_{1,\text{peace}}=0/9=0$. Any document containing "peace" would rule out class 1.
- Smoothed (19.1.8): class 1 denominator $=Jc+9=3+9=12$, so $\hat\mu_1=(7/12,\,4/12,\,1/12)$. Class 2 denominator $=3+10=13$, so $\hat\mu_2=(2/13,\,3/13,\,8/13)$.
- New document $W=(1,0,2)$. Score (19.1.9):
  - Class 1: $0.3\times\frac{7}{12}\times\left(\frac{1}{12}\right)^2=\frac{2.1}{1728}\approx0.001215$.
  - Class 2: $0.7\times\frac{2}{13}\times\left(\frac{8}{13}\right)^2=\frac{89.6}{2197}\approx0.040783$.
- Normalizing: $P(\text{class 1})=0.001215/(0.001215+0.040783)\approx0.029$. The prediction (19.1.10) is class 2. Smoothing kept class 1 possible but unlikely.

## Concepts
- [[supervised-learning]] — fit a model to labelled training texts, then predict labels for unlabelled texts (p. 318) (new)
- [[loss-function]] — the quantity minimized to fit parameters, e.g. squared error or cross-entropy (pp. 318, 326) (new)
- [[regularization]] — a penalty $R(\mu,\lambda)$ that limits complexity to make fitting tractable and prevent overfitting (pp. 318, 326) (new)
- [[lasso-ridge]] — $\ell_1$ penalty induces exact zeros; $\ell_2$ penalty shrinks smoothly (p. 328) (new)
- [[naive-bayes-classifier]] — class prevalence times a class-specific multinomial word model, with words independent given the class (pp. 320–321) (new)
- [[laplace-smoothing]] — adding constant $c$ to each word count to avoid zero probabilities (p. 321) (new)
- [[generative-vs-discriminative]] — modelling $p(D\mid y)p(y)$ versus modelling $p(y\mid D)$ directly (p. 323) (new)
- [[calibration]] — whether predicted probabilities match true frequencies. Naive Bayes tends to be overconfident (p. 322) (new)
- [[basis-function-expansion]] — adding transformed features $h(W)$ so a linear model fits nonlinear functions (p. 328) (new)
- [[neural-network-hidden-layer]] — features learned from the data by a function such as ReLU, which can be stacked (p. 330) (new)
- [[quantification-readme]] — estimating category proportions directly from $p(W)=p(W\mid\pi)p(\pi)$ (p. 331) (new)
- [[predictability-as-measurement]] — using a classifier's output as a continuous measure of an underlying dimension (p. 334) (new)
- [[validation-and-uncertainty]] — here: classifier-based measures are validated (Ch. 20; Nielsen does so, p. 334) and their uncertainty should be handled downstream (p. 335) (new)

## Canonical instances
- [[nielsen-jihad-score]] — Naive Bayes log-odds as continuous measure of clerics' expressed support for violent jihad (pp. 333–335)
- [[king-pan-roberts-censorship]] — group blog posts by topic, where category shares matter, not individual posts (p. 331)
- [[product-review-sentiment]] — example where most words are uninformative, motivating sparsity (p. 328)
- [[hopkins-king-readme]] — direct proportion estimation avoiding Naive Bayes independence (pp. 331–332)

## Bridges (candidates)
- [same-math] Naive Bayes log-score $\log\hat\alpha_k+\sum_jW_{ij}\log\hat\mu_{kj}$ ↔ Linear models: linear function of features (eq. 19.1.14–15) — the chapter shows the identity.
- [same-math] Lasso/ridge penalties ↔ Regression: regularized least squares — the same loss plus penalty form (Table 19.1).
- [structural-analogy] ReadMe's $p(W)=p(W\mid\pi)p(\pi)$ ↔ Misclassification correction in survey/measurement error: recover true shares from observed outputs — suggests a matrix-inversion logic.
- [structural-analogy] Classifier error entering downstream regressions ↔ Measurement error in regressors: uncertainty and bias if error relates to other variables.
- [metaphor] "Prototype document" per class ↔ Spatial models of voting: nearest-ideal-point choice.

## Questions this raises
- When is an overconfident, poorly calibrated Naive Bayes still good enough for a research question, and how would we check this?
- Under what conditions is a parameter vector in text problems sparse rather than dense, and how should that choose between lasso and ridge?
- Does a Naive Bayes log-odds score measure the intensity of ideology, or only the probability of class membership?
- How should classifier uncertainty be propagated, e.g. by block bootstrap or Fong and Tyler's method, when the score is a regressor?

## Reading notes
- Printed page = pdf page (offset 0). The unit covers pp. 318–336. Pages 319 and 325 are nearly empty transition pages.
- The text layer garbles all equations. They were checked against the page images.
- Eq. 19.1.12 is printed as $\propto\exp(W_{i,\cdot}\mu)$ without a class index. Table 19.1 prints the SVM loss as $\max(0,y_i(W_{i,\cdot}\mu))$. Both are reproduced as printed, not corrected.
- The sparsity discussion (p. 329) mentions "dense, not sparse" parameters. The "bet on sparsity" line is a quote from Hastie et al. as printed.
- Figure 19.1 (p. 335) is a word-cloud style plot, with word size by frequency and position by weight. The word placements named above are my reading of the image and may be imprecise for small words.
- The chapter has no exercises.
