---
id: prince-2023-udl/ch14-unsupervised
work: prince-2023-udl
unit: Chapter 14 — Unsupervised learning
pages: 269–275
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Unsupervised learning

## L0 — One line
Unsupervised models learn from unlabelled data; generative models, especially probabilistic ones, are judged by desirable properties and by imperfect metrics such as test likelihood, inception score, Fréchet inception distance and manifold precision/recall.

## L1 — The gist (≤ 120 words)
How should we classify models trained without labels, and how do we tell whether a generative model is good? Prince nests the classes: unsupervised ⊃ generative ⊃ probabilistic generative models. Latent variables, usually low-dimensional, often link the data to a compressed description. Generative models based on latent variables should have six properties (fast, high-quality, covering the data, with a well-behaved and disentangled latent space, and cheap likelihood if probabilistic). The author calls the ratings subjective and disputable, but says most practitioners would agree that none of GANs, VAEs, flows or diffusion models has all six. Metrics each cover only part of this: test likelihood does not apply to GANs, and the image metrics depend on a pretrained classifier. The chapter prepares chapters 15–18.

**Prerequisites:** probability distributions; log-likelihood; KL divergence (Appendix C); what a classifier's class probabilities are.

## L2 — Key ideas
- Unsupervised learning means learning from $\{\mathbf{x}_i\}$ without labels. Goals include generating, denoising, compressing, clustering and outlier detection (p. 269).
- Latent variables $\mathbf{z}$ are unseen, usually lower-dimensional summaries of data. The mapping can go $\mathbf{x}\to\mathbf{z}$ (k-means) or $\mathbf{z}\to\mathbf{x}$ (generative models) (pp. 269–270).
- Probabilistic generative models assign $Pr(\mathbf{x}|\boldsymbol\phi)$. They are trained by minimising the summed negative log-likelihood (eq. 14.1). The probabilities also allow model comparison and outlier detection (p. 270).
- Generative models based on latent variables should have six properties; the author calls the ratings subjective and disputable, but says most practitioners would agree that no single model has them all (pp. 270–272).
- Test likelihood is sensible but not defined for GANs and is costly for VAEs and diffusion models. Flows are the only model type where it is exact and efficient (p. 272).
- The inception score (eq. 14.2) rewards confident classification and class balance. It does not reward within-class diversity and is sensitive to the classifier (p. 273).
- Fréchet inception distance compares real and generated data in a classifier's feature space, and manifold precision/recall is also typically computed there. Precision measures realism; recall measures the proportion of real data the model can generate (p. 274).

## L3 — Walkthrough

**Chapter introduction.** Chapters 2–9 covered supervised learning, and chapters 10–13 covered architectures (p. 269). Unsupervised models learn from $\{\mathbf{x}_i\}$ with no labels. Their goals include generating new samples; manipulating, denoising, interpolating or compressing examples; revealing structure such as clusters; and separating outliers from the dataset (p. 269). The next four chapters cover GANs, normalizing flows, VAEs and diffusion models, and need probability from Appendix C (p. 269).

**14.1 Taxonomy.**
- A common strategy defines a mapping between data $\mathbf{x}$ and unseen latent variables $\mathbf{z}$. Latent variables capture underlying structure and usually have lower dimension than the data, so $\mathbf{z}$ can be considered a compressed version of $\mathbf{x}$ (p. 269).
- The mapping may run either way. k-means maps $\mathbf{x}$ to a cluster assignment $z\in\{1,\dots,K\}$ (p. 270).
- If a model defines a distribution $Pr(\mathbf{z})$ and maps $\mathbf{z}$ to $\mathbf{x}$, new examples come from (i) drawing from $Pr(\mathbf{z})$ and (ii) mapping the sample to data space. These are *generative models* (p. 270).
- Figure 14.1 nests the classes: probabilistic generative models sit inside generative models, which sit inside unsupervised learning. Latent variable models can fall into any of these categories (p. 270).
- GANs generate $\mathbf{x}^*$ from $\mathbf{z}$ using a loss that pushes samples to be indistinguishable from real ones (fig. 14.2a) (p. 270).
- Flows, VAEs and diffusion models are probabilistic. They generate and also assign $Pr(\mathbf{x}|\boldsymbol\phi)$. Training maximises the probability of the data, so the loss is the sum of negative log-likelihoods (p. 270):

$$L[\boldsymbol\phi]=-\sum_{i=1}^{I}\log\big[Pr(\mathbf{x}_i|\boldsymbol\phi)\big].\tag{14.1}$$

- Because probabilities must sum to one, this implicitly lowers the probability of examples far from the data. Test-set probability can be used to compare models, and the probability of an example can be thresholded to decide whether it is an outlier (p. 270).
- Footnote: not all probabilistic generative models use latent variables. The transformer decoder is trained without labels, generates, and assigns probabilities, but is autoregressive (eq. 12.15) (p. 270).

*Intuition note:* Probability mass is limited, so giving more to the real data takes it from everything else. So raising the likelihood of the data implicitly lowers the probability of examples far from it.

**14.2 What makes a good generative model?** The author says generative models based on latent variables should have these properties (pp. 270–271):
1. Efficient sampling: cheap, and using hardware parallelism.
2. High-quality sampling: samples indistinguishable from real data.
3. Coverage: samples represent the whole training distribution, not a subset.
4. Well-behaved latent space: every $\mathbf{z}$ gives a plausible $\mathbf{x}$, and smooth changes in $\mathbf{z}$ give smooth changes in $\mathbf{x}$.
5. Disentangled latent space: each dimension of $\mathbf{z}$ changes an interpretable property (for language, it might change topic, tense or verbosity).
6. Efficient likelihood computation, for probabilistic models.

Figure 14.3 gives guidance; the author calls the answer subjective (symbols ✓, ✗, ?, n/a as printed). The author says the assignments are disputable (p. 271).

| Model | Efficient | Quality | Coverage | Well-behaved | Disentangled | Likelihood |
|---|---|---|---|---|---|---|
| GANs | ✓ | ✓ | ✗ | ✓ | ? | n/a |
| VAEs | ✓ | ✗ | ? | ✓ | ? | ✗ |
| Flows | ✓ | ✗ | ? | ✓ | ? | ✓ |
| Diffusion | ✗ | ✓ | ? | ✗ | ✗ | ✗ |

Most practitioners would agree no single model has all properties (pp. 271–272).

**14.3 Quantifying performance.** Many experiments use images, so some metrics apply only to images (p. 272).

*Test likelihood.*
- Training likelihood is ineffective. A model could give each training point very high probability and everything between them very low, so it could only reproduce the training data (p. 272).
- Test likelihood captures generalisation and coverage. If probability concentrates on a subset, other test points get low probability (p. 272).
- The author calls it a sensible way to quantify probabilistic models, but it is not relevant to GANs, which assign no probability. It is expensive for VAEs and diffusion models, though a lower bound on the log-likelihood is computable. Only flows allow exact, efficient computation (p. 272).

*Inception score (IS).*
- It is specialised for images and ideally for models trained on ImageNet. A pretrained classifier (usually "Inception") is used (p. 272).
- Criterion 1: each generated image should look like exactly one of the 1000 classes, so $Pr(y|\mathbf{x}^*_i)$ should be peaked.
- Criterion 2: classes should be equally frequent over the generated set, so $Pr(y)$ should be flat (p. 272).
- The score is large when the first is peaked and the second flat. It is the exponential of the expected KL divergence (p. 273):

$$IS=\exp\left[\frac1I\sum_{i=1}^{I}D_{KL}\big[Pr(y|\mathbf{x}^*_i)\,\|\,Pr(y)\big]\right],\tag{14.2}$$

$$Pr(y)=\frac1I\sum_{i=1}^{I}Pr(y|\mathbf{x}^*_i).\tag{14.3}$$

Here $I$ is the number of generated examples.
- Weaknesses: it is sensible only for ImageNet models, and retraining the classifier can give quite different numbers. It does not reward diversity within a class, and it is high if the model produces one realistic example per class (p. 273).

*Intuition note:* IS asks whether each image is classified confidently and whether the classes come out balanced. It does not reward diversity within a class: one realistic image per class already scores high.

*Fréchet inception distance (FID).*
- It is a symmetric distance between generated and real distributions, and it is approximate. Both distributions are approximated by multivariate Gaussians, and the Fréchet distance (Appendix C.5.4) is estimated (pp. 273–274).
- The Gaussians are fitted to activations in the deepest layer of the Inception network. The comparison is therefore semantic and ignores fine detail (p. 274).
- It accounts for within-class diversity but relies heavily on what the network retains. Discarded information, which may matter for realism, does not contribute (p. 274).

*Manifold precision/recall.*
- FID reflects realism and diversity but does not separate them. Here, the data manifold is where real examples lie and the model manifold is where generated samples lie (p. 274).
- Precision is the fraction of model samples inside the data manifold (realism). Recall is the fraction of data examples inside the model manifold (how much of the real data the model can generate) (p. 274, fig. 14.5).
- Estimation: put a hypersphere around each example, with radius equal to the distance to its $k$th nearest neighbour. The union approximates the manifold. This is also typically done in a classifier's feature space (p. 274).

**14.4 Summary.** Unsupervised ⊃ generative ⊃ probabilistic. The next four models start from a latent $\mathbf{z}$ with a known distribution, and a deep network maps $\mathbf{z}$ to data space (p. 274).

**Notes (p. 275).** The inception score is credited to Salimans et al. (2016) and FID to Heusel et al. (2017). Both are based on the Pool-3 layer of Inception V3. Nash et al. (2021) used earlier layers that retain spatial information. Kynkäänniemi et al. (2019) introduced manifold precision/recall. Barratt & Sharma (2018) discuss IS weaknesses (p. 275).

## Toy example (ours)
Two classes, two generated images, $I=2$.
- Image 1: $Pr(y|\mathbf{x}_1^*)=(0.9,0.1)$. Image 2: $(0.1,0.9)$.
- Eq. 14.3: $Pr(y)=\tfrac12[(0.9,0.1)+(0.1,0.9)]=(0.5,0.5)$.
- $D_{KL}$ for image 1: $0.9\ln(0.9/0.5)+0.1\ln(0.1/0.5)=0.9(0.5878)+0.1(-1.6094)=0.5290-0.1609=0.3681$. Image 2 is symmetric, also 0.3681.
- Eq. 14.2: $IS=\exp(0.3681)\approx1.445$.
- If both images were $(0.5,0.5)$, every KL is 0 and $IS=e^0=1$, the lowest value. Confident, balanced classification therefore scores higher.

## Concepts
- [[unsupervised-learning]] (new) — learning from $\{\mathbf{x}_i\}$ with no labels (p. 269)
- [[latent-variable]] (new) — unseen, usually lower-dimensional variable capturing a dataset's structure (p. 269)
- [[generative-model]] (new) — model that can synthesise new examples, e.g. by sampling $\mathbf{z}$ and mapping to $\mathbf{x}$ (p. 270)
- [[probabilistic-generative-model]] (new) — generative model that also assigns $Pr(\mathbf{x}|\boldsymbol\phi)$; trained with eq. 14.1 (p. 270)
- [[cross-entropy / log-loss]] — here the summed negative log-likelihood of the data, eq. 14.1 (p. 270)
- [[disentangled-latent-space]] (new) — manipulating each latent dimension should change an interpretable property (p. 271)
- [[test-likelihood]] (new) — probability of held-out data, measuring generalisation and coverage (p. 272)
- [[inception-score]] (new) — exp of mean KL between per-image and marginal class distributions (p. 273)
- [[frechet-inception-distance]] (new) — Fréchet distance between Gaussians fitted to classifier features (p. 274)
- [[manifold-precision-recall]] (new) — realism (precision) and share of real data the model can generate (recall), via $k$-NN hypersphere manifolds (p. 274)

## Canonical instances
- [[k-means]] — maps $\mathbf{x}$ to a cluster index $z$ (p. 270)
- [[gan-vae-flow-diffusion-comparison]] — fig. 14.3 property table (p. 272)
- [[transformer-decoder-as-autoregressive-generator]] — probabilistic generative model without latent variables (p. 270)
- [[imagenet-inception-evaluation]] — Inception classifier over the 1000 ImageNet classes used for IS; FID uses activations of the inception network (pp. 272–274)

## Bridges (candidates)
- [same-math] Eq. 14.1, summed negative log-likelihood ↔ llm: cross-entropy / log-loss — the same quantity up to dividing by the number of examples.
- [same-math] Test likelihood ↔ llm: held-out log-loss / perplexity — perplexity is the exponential of held-out cross-entropy.
- [structural-analogy] IS exponentiates an average KL divergence ↔ llm: perplexity exponentiates an average log-loss — both turn an information measure into an "effective number".
- [metaphor] Disentangled latent dimensions (topic, tense) ↔ llm: feature steering — directions in a representation that change one property.

## Questions this raises
- If a model can be sampled but gives no likelihood (GANs), how can coverage be measured directly?
- How much do IS, FID and precision/recall depend on the choice of classifier?
- Do language models with autoregressive probabilities meet the six properties?
- Can a disentangled latent space be measured, since the table gives "?" for most models?

## Reading notes
- Printed page = pdf − 14. Pages are labelled with printed numbers.
- The text layer shows "7" where the figure 14.3 image shows ✗; the table above follows the image.
- No exercises in this unit. The source is a draft ("please send errata").
- Ratings in fig. 14.3 are called subjective by the author (p. 271).
