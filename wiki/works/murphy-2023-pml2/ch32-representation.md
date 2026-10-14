---
id: murphy-2023-pml2/ch32-representation
work: murphy-2023-pml2
unit: "31 Nonparametric Bayesian models (introduction only) and 32 Representation learning"
pages: 1047–1072
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Representation learning (with the one-page introduction to Ch. 31)

## L0 — One line
Representation learning trains a network on a cleverly designed task (supervised, generative or self-supervised) so that its features help with later, unknown tasks. Such features are judged by downstream performance or by similarity measures, and the theory of when they are recoverable is still thin.

## L1 — The gist (≤ 120 words)
Ch. 32 asks how to learn input transformations that make unseen future tasks easier, and how to tell whether they succeeded. It covers evaluation (linear evaluation, fine-tuning, similarity measures such as centered kernel alignment (CKA) and canonical correlation analysis (CCA)). It then covers learning approaches: supervised pretraining, generative models, denoising/masked prediction, transformation prediction, and multiview (contrastive and negative-free) learning. It ends with theory: identifiability (recovering the true latent factors), where several existing methods cannot work without extra assumptions, and information maximization, which has trivial solutions and estimation problems. The key difficulty is choosing a task that forces a useful representation. Ch. 31 appears only as a one-page introduction to nonparametric Bayes.

**Prerequisites:** SVD/QR, Frobenius norm, correlation; softmax cross-entropy; autoencoders/VAEs and mutual information (earlier chapters); basic Bayesian modelling.

## L2 — Key ideas (5–10 bullets)
- Representation learning designs a task whose solution forces a good input transformation, because we cannot directly specify what the representation should do (p. 1049).
- Evaluation is by downstream performance (linear evaluation, fine-tuning, disentanglement) or by task-free similarity of two representations (RSA/CKA, CCA variants). Linear evaluation accuracy on a finite dataset is only a lower bound on the accuracy of the Bayes-optimal linear classifier (pp. 1050–1052).
- Squared-CCA, regression-based and linear-CKA similarities all involve similarities between all pairs of principal components. They place different weightings on these pairs according to the variance explained (p. 1055).
- Choices of invariance matter. Permutation invariance is the minimum, and invariance to all invertible maps is undesirable. CKA passed a sanity check on CNN layers that other measures failed (p. 1056).
- The three families (supervised, generative, self-supervised) differ in what supervision they need and in how well their training task matches downstream tasks (pp. 1056–1057). Supervised pretraining remains dominant, and generative methods have empirically fallen behind (pp. 1057–1061).
- Self-supervised pretext tasks (denoising, masking, transformation prediction) turn unlabeled data into supervised problems. Masked-prediction models currently hold the top ImageNet positions among models trained without additional data, and transformation prediction underperforms masked prediction (pp. 1062–1064).
- Multiview learning uses positive pairs plus a way to prevent collapse: contrastive losses (contrastive, triplet, InfoNCE) or negative-free losses (Barlow Twins, BYOL, SimSiam, DINO) (pp. 1064–1068).
- Entangled and disentangled latent models can give the same marginal likelihood, so marginal likelihood alone cannot identify the disentangled model, and several existing methods cannot work without extra assumptions (p. 1069).
- Information maximization has trivial solutions (identity map). The information bottleneck adds compression guided by labels. Mutual-information estimators are also weak for deterministic continuous encoders (pp. 1070–1071).

## L3 — Walkthrough

### 31.1 Introduction to nonparametric Bayes (Rao) (p. 1047)
- **Parametric model:** the modelled objects (functions, densities, graphs, shapes) are indexed by a finite-dimensional parameter vector. In a parametric Bayesian model a prior on the parameters induces a prior on the objects (p. 1047).
- **Bayesian nonparametric (BNP) model:** the prior is placed directly on the objects, usually via a *stochastic process*, i.e. a distribution over a potentially infinite set of random variables (p. 1047).
- Example, the Gaussian process: for any finite $\mathbf X=\{x_n\}_{n=1}^N$, $p(f(\mathbf X))=\mathcal N(f(\mathbf X)\mid \boldsymbol\mu(\mathbf X),\mathbf K(\mathbf X))$. Here $\mathbf K(\mathbf X)$ is the $N\times N$ Gram matrix of a positive definite kernel (p. 1047).
- Posterior complexity can grow with the data, which avoids underfitting. The Bayesian treatment avoids overfitting this flexible model. Practitioners are often interested only in finite training and test sets, which often makes these models surprisingly tractable (p. 1047). Details are in Supplementary Chapter 31, not in this unit.

### 32.1 Introduction (Poole, Kornblith) (p. 1049)
- Representation learning transforms raw inputs into a form that makes *new* tasks easier. Unlike supervised learning, the task is often unknown at training time (p. 1049).
- Humans are cited as evidence that this is possible: they form rich class representations quickly (p. 1049).
- Desired properties are hard to specify directly (few-shot ease, similarity queries, keeping some information while discarding other). So the aim is to design a task whose solution requires a better representation (p. 1049).
- Plan: evaluation, then supervised, generative and self-supervised learning, then theory (p. 1049).

### 32.2 Evaluating and comparing representations (pp. 1049–1056)
Representations are high-dimensional, so they must be summarised by a few scalars. This requires assumptions about which structure matters (pp. 1049–1050). Fig. 32.1 shows a network mapping mixed-class input data to a representation where class is more easily distinguished (p. 1050).

#### 32.2.1 Downstream performance (pp. 1050–1052)
- Downstream performance can differ from pretraining performance only if the downstream task differs in input distribution, target distribution, or both. Self-supervised evaluation often keeps the inputs but uses labels not seen in pretraining. In *transfer learning* the input distribution changes, e.g. pretrain on varied natural images and test on unseen bird species (p. 1050).
- **32.2.1.1 Linear evaluation.** The network is a frozen feature extractor, and a linear classifier is trained on features from a chosen layer. This is equivalent to training only a new layer with the rest frozen and normalization layers in inference mode. Earlier work used SVMs; recent work typically uses $L^2$-regularized multinomial logistic regression (pp. 1050–1051).
  - The objectives are convex, so global minima exist, but SGD can need many more epochs than the original network. It needs tuned learning-rate schedule and weight decay (p. 1051).
  - If all features fit in memory, full-batch methods with line search (L-BFGS) need no learning-rate tuning. Regularization is swept using warm starts. Precomputing features saves compute but limits augmentations (p. 1051).
  - The accuracy of a trained linear classifier on a finite dataset is only a lower bound on the Bayes-optimal linear classifier's accuracy. It depends on linear separability and on how much data is needed to find a good boundary. Even an invertible linear transformation of a representation can change it (p. 1051).
- **32.2.1.2 Fine-tuning.** Attach a new layer and update *all* parameters on the downstream task, typically at a lower learning rate than in pretraining (p. 1051). It is more expensive, but fine-tuned networks typically outperform linear classifiers, especially when the tasks differ a lot. Linear classifiers perform better only when training examples are very few (about 5 per class) (p. 1051). Variants: feature pyramid networks for detection/segmentation, Net2Net (new layers initialised to preserve output), adapter modules (new parameter-efficient modules, old ones frozen) (p. 1052).
- **32.2.1.3 Disentanglement.** If the data-generating factors are known (position, shape, colour), one asks how well they are recovered. Most metrics measure the degree of one-to-one correspondence between latent factors and representation dimensions (p. 1052).

> **Intuition note.** Evaluating a representation requires assumptions about which structure matters, e.g. a stand-in downstream task. Linear evaluation tests how easily the classes can be read out, not only whether they are separable, because regularization and data size also matter.

#### 32.2.2 Representational similarity (pp. 1052–1056)
Setting: two fixed representations of the same $n$ examples, stacked row-wise as $\boldsymbol X\in\mathbb R^{n\times p_1}$, $\boldsymbol Y\in\mathbb R^{n\times p_2}$ (p. 1052).

**32.2.2.1 RSA and CKA.**
- RSA (dominant in neuroscience) forms representational similarity matrices $K_{ij}=k(X_{i,:},X_{j,:})$ and $K'_{ij}=k'(Y_{i,:},Y_{j,:})$, both $n\times n$. A matrix similarity $s(K,K')$ gives a scalar. Common choices are Pearson correlation for $k,k'$ and Spearman rank correlation of the reshaped matrices for $s$. How to choose these is contentious (pp. 1052–1053).
- CKA (first proposed in the ML literature, interpretable as RSA) takes $k,k'$ to be positive semi-definite kernels and $s$ the cosine similarity of centered kernel matrices ($H=I-\frac1n\mathbf 1\mathbf 1^\top$ is the centering matrix, $n\times n$):
$$s(K,K')=\frac{\langle HKH,HK'H\rangle_F}{\|HKH\|_F\|HK'H\|_F},\tag{32.1}$$
with $\langle A,B\rangle_F=\mathrm{vec}(A)^\top\mathrm{vec}(B)=\mathrm{tr}(A^\top B)$ (p. 1053).
- Linear kernel case: $K=XX^\top$, $K'=YY^\top$. With column-centered $\tilde X=HX$, $\tilde Y=HY$:
$$s(K,K')=\frac{\langle\tilde X\tilde X^\top,\tilde Y\tilde Y^\top\rangle_F}{\|\tilde X\tilde X^\top\|_F\|\tilde Y\tilde Y^\top\|_F}=\frac{\|\tilde X^\top\tilde Y\|_F^2}{\|\tilde X^\top\tilde X\|_F\|\tilde Y^\top\tilde Y\|_F}.\tag{32.2}$$
Linear CKA equals the RV coefficient between centered features, as shown in [Kor+19] (p. 1053).

**32.2.2.2 CCA and relatives.**
- CCA finds, for $i=1,2,\dots$, weights $(w_i,w_i')$ maximizing correlation of canonical vectors, with orthogonality to earlier ones:
$$\begin{aligned}&\text{maximize }\operatorname{corr}[Xw_i,Yw_i']\\&\text{subject to }\forall_{j<i}\ Xw_i\perp Xw_j,\ \ \forall_{j<i}\ Yw_i'\perp Yw_j',\ \ \|Xw_i\|=\|Yw_i'\|=1.\end{aligned}\tag{32.3}$$
The number of non-zero canonical correlations is at most $p=\min(\mathrm{rk}(X),\mathrm{rk}(Y))$ (p. 1053).
- Algorithm [BG73]: decompose $\tilde X=QR$ and $\tilde Y=Q'R'$ with $Q^\top Q=I$, $Q'^\top Q'=I$ (QR or SVD). Take an SVD $Q^\top Q'=U\Sigma V^\top$. Then the canonical correlations are $\rho=\mathrm{diag}(\Sigma)$, the canonical vectors are $XW=QU$ and $YW'=Q'V$, and the weights are $W=R^{-1}U$ and $W'=R'^{-1}V$ (pp. 1053–1054).
- Scalar summaries: mean squared canonical correlation and mean canonical correlation ($\|\cdot\|_*$ = nuclear norm):
$$R^2_{\rm CCA}(X,Y)=\|\rho\|_2^2/p=\|Q^\top Q'\|_F^2/p,\tag{32.4}$$
$$\bar\rho=\sum_{i=1}^p\rho_i/p=\|Q^\top Q'\|_*/p.\tag{32.5}$$
$R^2_{\rm CCA}$ is also called Yanai's GCD, Pillai's trace, or the eigenspace overlap score (p. 1054).
- **Weakness of CCA:** if at least one representation has more neurons than examples and each neuron is linearly independent of the others, all canonical correlations are 1. Estimation also needs enough data, and one may want less weight on low-variance directions (p. 1054).
- **SVCCA** keeps only the top $k$ (resp. $k'$) principal components of $\tilde X=U\Sigma V^\top$ (resp. $\tilde Y=U'\Sigma'V'^\top$) before CCA:
$$Q=U_{:,1:k},\quad R=\Sigma_{1:k,1:k}V_{:,1:k}^\top,\quad Q'=U'_{:,1:k'},\quad R'=\Sigma'_{1:k',1:k'}V'^\top_{:,1:k'}.\tag{32.6}$$
Raghu et al. suggest the smallest $k$ with $\|\sigma_{1:k}\|^2/\|\sigma\|^2=0.99$ (same for $k'$). But for fixed $\min(k,k')$, CCA-based similarity increases with $\max(k,k')$. So representations needing more components may look "more similar" to everything, and it is often better to set $k=k'$ to a fixed value (p. 1054).
- **PWCCA** weights correlations by the variability they explain:
$$\mathrm{PWCCA}(X,Y)=\frac{\sum_{i=1}^p\alpha_i\rho_i}{\sum_{i=1}^p\alpha_i},\qquad \alpha_i=\|(Yw_i')^\top Y\|_1.\tag{32.7}$$
Potential problems: it is asymmetric, and the $L^1$ norm is not rotation invariant with no clear justification (p. 1055).
- Replacing the $L^1$ norm by the squared $L^2$ norm weights by explained variance:
$$R^2_{\rm LR}(X,Y)=\frac{\sum_{i=1}^p\alpha_i'\rho_i^2}{\sum_{i=1}^p\alpha_i'},\qquad \alpha_i'=\sum_{j=1}^{p_2}\|(Yw_i')^\top Y\|_2^2.\tag{32.8}$$
(The index $j$ is printed as shown; see Reading notes.) When $p_2\ge p_1$ [Kor+19], this equals the variance explained by linear regression of every neuron of $\tilde Y$ on $\tilde X$:
$$R^2_{\rm LR}(X,Y)=1-\sum_{i=1}^{p_2}\min_{\beta}\|\tilde Y_{:,i}-\tilde X\beta\|^2/\|\tilde Y\|_F^2.\tag{32.9}$$
- **Unified view.** With $\tilde X=U\Sigma V^\top$, $\tilde Y=U'\Sigma'V'^\top$, $u_i=U_{:,i}$ (unit-length principal components) and $\lambda_i=\Sigma_{ii}^2$ (explained variance, up to a factor $1/n$), as printed:
$$R^2_{\rm CCA}=\sum_{i=1}^{p_1}\sum_{j=1}^{p_2}(u_i^\top u_j')^2/p_1\tag{32.10}$$
$$R^2_{\rm LR}=\sum_{i=1}^{p_2}\sum_{j=1}^{p_2}\lambda_j'(u_i^\top u_j')^2\Big/\sum_{j=1}^{p_2}\lambda_j'\tag{32.11}$$
$$\mathrm{CKA}_{\rm linear}=\frac{\sum_{i=1}^{p_1}\sum_{j=1}^{p_2}\lambda_i\lambda_j'(u_i^\top u_j')^2}{\sqrt{\sum_{i=1}^{p_1}\lambda_i^2}\sqrt{\sum_{j=1}^{p_2}\lambda_j'^2}}\tag{32.12}$$
All three involve similarities between all pairs of principal components, with different weights by explained variance (p. 1055).

> **Intuition note.** Each index asks how well the principal directions of $X$ line up with those of $Y$. CCA treats all directions equally, regression weights by $Y$'s variance, and CKA weights by the variance of both. The text notes that CCA gives all correlations equal to 1 when a representation has more linearly independent neurons than examples, and that one may want less weight on low-variance directions.

**32.2.2.3 Comparing similarity measures (pp. 1055–1056).**
- What properties are desirable is an open question that may have no unique answer. The goal differs from downstream accuracy: it is to understand how representations evolve or differ across architectures and training settings (p. 1055).
- *Invariances.* The minimum is invariance to neuron permutation, since neurons have no canonical order. Invariance to arbitrary invertible maps (as with mutual information) is clearly undesirable, because many realistic networks are injective, so an invertible map between any two representations always exists. Most common measures are invariant to rotations, which implies permutation invariance. Measures based solely on CCA correlations ($R^2_{\rm CCA}$, $\bar\rho$) are invariant to all invertible linear maps; SVCCA and PWCCA are not (p. 1056).
- *Sanity check* [Kor+19]: for two identical architectures from different random initialisations, a layer of A should be more similar to the corresponding layer of B than to any other layer. For flattened CNN representations, CKA-based measures pass and other measures do not. For tokens in Transformers, all measures do reasonably well (p. 1056).
- Maheswaranathan et al. report that CCA and linear CKA are highly sensitive to seemingly innocuous RNN design choices (e.g. activation function), even though fixed-point analysis suggests the networks work similarly (p. 1056).

### 32.3 Approaches for learning representations (pp. 1056–1069)
- The goal is a transformation $z=f_\theta(x)$ useful for future, unknown tasks. This needs large unlabeled or weakly labeled data and tasks or priors solvable without the downstream tasks (p. 1056).
- Main difficulty: if the pretext task is too easy, it may be solved by a shortcut. If it is too different from the downstream task, the representation may not help. For detection the representation needs object identity and location, while classification alone can discard position. So methods are often not generic (p. 1056).
- Fig. 32.2 outlines three families: supervised (standard losses on large labeled or weakly labeled data), generative (model the data or parts of it), self-supervised (transformation prediction or multi-view learning with cheaply synthesised labels). Extra heads used for training are often thrown away for downstream use (p. 1057).

#### 32.3.1 Supervised representation learning and transfer (pp. 1057–1059)
- Networks trained on large labeled datasets gave the first major deep-learning successes in visual representation learning. Their features outperformed handcrafted ones, and supervised pretraining remains dominant (p. 1057).
- Larger networks and datasets generally give better pretraining and downstream accuracy. With other choices fixed, higher pretraining accuracy gives better downstream natural-image representations. The correlation can be much lower under larger domain shift (e.g. ImageNet to medical imaging) (pp. 1057–1058).
- Small models aimed at one task are sometimes better pretrained on a smaller, more related dataset. Larger models seem to gain more from larger, more diverse datasets (p. 1058).
- Some choices trade pretraining accuracy against transfer. Penultimate-layer dropout and label smoothing improve pretraining accuracy but give worse representations. Group normalization plus weight standardization gives similar pretraining and substantially better transfer. Adversarial training lowers pretraining accuracy but transfers better. For some dataset pairs, more weight decay on the final layer improves transfer at the cost of pretraining accuracy (p. 1058).
- *Weak supervision* uses cheap Internet signals (hashtags, automatic labels, captions/alt text). In practice the benefits of more data often outweigh the harm from noise. Image–text supervision allows many designs: predicting words or n-grams, image-conditional language models, masked language models, and contrastive models (CLIP, ALIGN) with two separate "towers" that place matching image and text embeddings close together. CLIP-style pretraining learns high-quality representations faster than alternatives [Rad+21] (p. 1058).
- *Zero-shot transfer:* build an image classifier from class text descriptions only. It typically performs worse than linear classifiers on image embeddings but is far more robust to distribution shift (pp. 1058–1059).

#### 32.3.2 Generative representation learning (pp. 1059–1061)
- Motivation: supervised representations often fail for tasks very different from the pretraining task. Generative learning models $q(x)$ with $p_\theta(x)$, in the hope that a model able to produce all the data implicitly learns a representation for any question. Example: digit style is hard to label, but a generator must model it, whereas supervised digit classification aims at style invariance (p. 1059).
- Two routes: latent-variable models (latents $z$ are the representation) and fully observed models (autoregressive, flow) from which a representation is extracted (p. 1059).

**32.3.2.1 Latent-variable models (pp. 1059–1060).**
- *Analysis-by-synthesis:* learn $p_\theta(x,z)$. The "analysis" step extracts a representation by sampling or computing the posterior mean of $p_\theta(z\mid x)$. Different models and inference procedures give different representation learners (p. 1059).
- Early stacked energy-based or sparse-coding models learned increasingly abstract features, but such greedy approaches failed to scale to larger natural datasets (pp. 1059–1060).
- Known generative structure helps: hierarchical stroke-based character models excel at several downstream tasks. When the structure is unknown it must be learned, and there is often a tradeoff between imposing structure (e.g. sparsity) and learning it (p. 1060).
- VAEs learn a prior $p_\theta(z)$, a decoder $p_\theta(x\mid z)$ and an amortised inference network $q_\phi(z\mid x)$. $\beta$-VAEs learn latents matching factors of variation on simple synthetic data, and VAEs help semi-supervised learning. None of the scaled-up VAEs has yet given representations competitive for classification or segmentation (p. 1060).
- GANs trained with encoders (BiGAN, ALI) gave good object-classification representations on small datasets, and BigBiGAN scaled to ImageNet with strong classification and segmentation results (p. 1060).

**32.3.2.2 Fully observed models (p. 1060).** ImageGPT, an autoregressive transformer on pixels, gives internal representations (from deterministic layers, not latents) that excel at image classification. In language, masked-training objectives (BERT) often do better than autoregressive ones (p. 1060).

**32.3.2.3 Autoencoders (pp. 1060–1061).** An encoder $z=f_\theta(x)$ and decoder $g_\phi(z)$ minimise reconstruction error, e.g. for images
$$\mathcal L(\theta,\phi)=\frac1{|\mathcal D|}\sum_{x\in\mathcal D}\|x-g_\phi(f_\theta(x))\|_2^2.\tag{32.13}$$
Unlike generative models, they typically cannot synthesise from scratch or assign likelihoods (p. 1060).
- If $z$ has the input's dimensionality and nothing is constrained, identity maps for $f_\theta$ and $g_\phi$ are a trivial solution. So a regularizer is usually added (p. 1061).
- Reducing the dimension of $z$ is one effective way to avoid this. With linear encoder and decoder and MSE loss, the autoencoder can learn the principal components (p. 1061).
- Higher-dimensional alternatives: sparsity ($\ell_1$ on $z$), smoothness, or noise added to inputs or intermediate layers. Stacked regularised autoencoders trained greedily were found to degrade performance versus end-to-end training. Denoising autoencoders have shown promise in discrete domains and with richer noise/masking patterns (§32.3.3.1) (p. 1061).

**32.3.2.4 Challenges (p. 1061).** Generative methods have empirically fallen behind. They must model all axes of variation whether or not semantically relevant (e.g. exact blades of grass). Biasing them toward semantic features is an open research area (p. 1061).

> **Intuition note.** A generative objective rewards matching every detail of the data, relevant or not. That is why it can be a weaker route to *useful* features than a task that targets semantics.

#### 32.3.3 Self-supervised representation learning (pp. 1061–1064)
Self-supervised learning designs *pretext tasks* with cheaply generated labels, so that supervised tools apply to unlabeled data. The learned representation is then transferred via a linear classifier or fine-tuning (pp. 1061–1062).

**32.3.3.1 Denoising and masked prediction (pp. 1062–1063).**
- Denoising adds noise to the input and trains the model to reconstruct the clean input. Masked prediction replaces patches or tokens with uninformative masks and predicts only the missing ones (p. 1062).
- The denoising autoencoder was the first deep model to use denoising. Vincent et al. argue that the network must learn the structure of the data manifold to solve the task (p. 1062).
- **BERT masked language modeling:** 15% of tokens are selected. Of these, 80% are replaced by [MASK], 10% by random tokens, 10% left intact. The mixture reduces the domain shift caused by [MASK] being absent at fine-tuning (p. 1062).
- Vision: greedy stacks of up to three denoising autoencoders were abandoned once end-to-end CNNs worked well. Context encoders (inpainting) were competitive at the time. Colorization is related to denoising (colour is dropped deterministically) (p. 1062).
- Image GPT trains a transformer on pixels for BERT-style masked modeling. Self-attention cost is quadratic in the number of pixels, which limits image size (pp. 1062–1063). **BEiT** splits images into $16\times16$ patches, discretises them with a discrete VAE, masks 40% of tokens, and predicts the discrete tokens with a softmax (p. 1063). The **masked autoencoder (MAE)** (Fig. 32.3) predicts the pixels of masked patches directly with a shallow decoder and $L_2$ loss. The encoder sees only unmasked tokens, so training is efficient even with 75% masked (p. 1063).
- Models pretrained by masked prediction and then fine-tuned hold the top ImageNet leaderboard positions among models trained without additional data (p. 1063).

**32.3.3.2 Transformation prediction (pp. 1063–1064).**
- Apply a transformation and classify which one was applied (Fig. 32.4). It reuses supervised classification pipelines, but may allow "shortcut" solutions (trivial features that solve the task). Methods of this kind were once top-performing but have been displaced by contrastive and masked prediction (p. 1063).
- Context prediction: two adjacent patches, eight-way classification of their relative position. A small variable gap and colour distortion or dropping prevent shortcuts via border pixels and chromatic aberration (p. 1064).
- Jigsaw: a $3\times3$ grid of shuffled patches, predicting the permutation. Restricting to a subset of permutations makes it a standard classification task (p. 1064).
- Rotation prediction: rotate by 0/90/180/270 degrees and classify. It is extremely simple, and its representations often beat patch-based ones. All transformation-prediction methods currently underperform masked prediction and multiview approaches on CIFAR-10 and ImageNet (p. 1064).

#### 32.3.4 Multiview representation learning (pp. 1064–1069)
- Goal: "similar" inputs or views map near each other and "dissimilar" ones further apart. All methods need positive pairs and a mechanism to prevent collapse of all representations to one point. The section covers contrastive learning (positive and negative pairs), metric learning, and "non-contrastive" learning (no negatives) (p. 1064). It makes it easy to incorporate prior knowledge about which inputs should be close, and views may come from different modalities (p. 1064).

**32.3.4.1 View selection (pp. 1065–1066).**
- Setup: anchor $x$, positive $x^+$, zero or more negatives $x^-$. Positives come from a process $p^+(x,x^+)$ and negatives from $p^-(x^-\mid x)$. Typically $x,x^+$ are two augmentations of one image, and $x^-$ is an augmented view of a different random image, so $p^-(x^-\mid x)=p^-(x^-)$ (p. 1065).
- **SimCLR:** $x=t(x_0)$, $x^+=t'(x_0)$ with random crops (flips, resize), colour distortion and Gaussian blur. Augmentation strengths are hyperparameters (p. 1065).
- **SupCon:** with categorical labels, positives share a label and negatives differ. With a contrastive loss this resembles neighbourhood component analysis and improved robustness over standard supervised learning (p. 1065).
- **CMC:** views are orthogonal image dimensions (e.g. luma and chroma). Each view has its own encoder, but all outputs live in one embedding space. At test time, embeddings can be averaged or concatenated (pp. 1065–1066).
- **CLIP:** $x$ is an image and $x^+$, $x^-$ are texts. On massive web image–text data it needs none of the augmentation used by image-only methods (p. 1066).
- Negatives are usually other minibatch elements. With small batches none may be close to the anchor, and learning may be slow. Hard negative mining picks close negatives but needs a negative database, so it is rarely used. Reweighting within the minibatch can also help (p. 1066).
- View choice determines which features and invariances are learned. Tian et al. show that choosing positives by shared attributes can lead to learning or ignoring those attributes. They also learn views by targeting a "sweet spot" of mutual information between views, neither too high nor too low. Which views suit which tasks remains open (p. 1066).

**32.3.4.2 Contrastive losses (pp. 1066–1067).** Learning $f_\theta$ with $x,x^+$ close and $x,x^-$ far apart is *metric learning* (p. 1066).
- Contrastive loss (negatives pushed to be at least $\epsilon$ apart; $\epsilon$ is hard to tune):
$$\mathcal L_{\rm contrastive}=\mathbb E_{x,x^+,x^-}\big[\|f_\theta(x)-f_\theta(x^+)\|^2+\max(0,\epsilon-\|f_\theta(x)-f_\theta(x^-)\|^2)\big].\tag{32.14}$$
- Triplet loss (positive pair at least $\epsilon$ closer than negative pair). It gives zero loss, hence no learning, once the negative is far enough:
$$\mathcal L_{\rm triplet}=\mathbb E_{x,x^+,x^-}\big[\max(0,\|f_\theta(x)-f_\theta(x^+)\|^2-\|f_\theta(x)-f_\theta(x^-)\|^2+\epsilon)\big].\tag{32.15}$$
- InfoNCE (multiclass N-pair loss), popular for its lack of hyperparameters and empirical effectiveness; $M$ is the number of negatives:
$$\mathcal L_{\rm InfoNCE}=-\mathbb E_{x,x^+,x^-_{1:M}}\left[\log\frac{\exp f_\theta(x)^Tg_\phi(x^+)}{\exp f_\theta(x)^Tg_\phi(x^+)+\sum_{i=1}^M\exp f_\theta(x)^Tg_\phi(x_i^-)}\right].\tag{32.16}$$
Embeddings are typically $\ell_2$-normalised and a temperature $\tau$ may rescale inner products. Unlike the triplet loss, it can always be improved by pushing negatives further away. It relates to a mutual-information lower bound and to the InfoMax principle:
$$I(X;Z)\ge\log M-\mathcal L_{\rm InfoNCE}.\tag{32.17}$$
For parallel views of the same modality and dimension, $f_\theta$ and $g_\phi$ can be shared (p. 1067).

> **Intuition note.** InfoNCE is a softmax over "which candidate is the true partner of the anchor?". It never reaches exactly zero, so it keeps pushing negatives away. Triplet and contrastive losses stop caring once a margin is met.

**32.3.4.3 Negative-free losses (pp. 1067–1068).** Only positive pairs are used. Collapse is prevented either by extra terms in the loss or by learning dynamics alone (p. 1067).
- **Barlow Twins**, with $C$ the cross-correlation matrix of the two views' features ($p\times p$):
$$\mathcal L_{\rm BT}=\sum_{i=1}^p(1-C_{ii})^2+\lambda\sum_{i=1}^p\sum_{j\ne i}C_{ij}^2.\tag{32.18}$$
The first term is attractive, and the second prevents collapse to a low-rank representation. The loss is minimised when $C=I$. VICreg uses a non-zero feature-variance requirement against collapse. Barlow Twins relates to kernel independence criteria such as HSIC (p. 1067).
- **BYOL / SimSiam** minimise a mean squared error between two representations:
$$\mathcal L_{\rm BYOL}=\mathbb E_{x,x^+}\big[\|g_\phi(f_\theta(x))-f_{\theta'}(x^+)\|^2\big].\tag{32.19}$$
Here $g_\phi$ is the predictor, $f_\theta$ the online network and $f_{\theta'}$ the target network. Optimising $\theta'$ directly leads to collapse. BYOL sets $\theta'$ to an exponential moving average of $\theta$, and SimSiam sets $\theta'\leftarrow\theta$ each iteration. Why collapse is avoided is not entirely clear, but a gradient-flow analysis of a simplified linear BYOL shows collapse can be avoided with properly set hyperparameters (pp. 1067–1068).
- **DINO:** attractive term only, with an EMA target network, cross-entropy $H$ (target produces the targets) and no predictor:
$$\mathcal L_{\rm DINO}=\mathbb E_{x,x^+}\big[H\big(f_{\theta'}(x)/\tau,\ \mathrm{center}(f_\theta(x^+))/\tau'\big)\big].\tag{32.20}$$
Centering (mean over the minibatch) is said to be necessary to prevent collapse to a single "class", and a lower temperature $\tau'<\tau$ is necessary to prevent collapse to a uniform distribution. It gives marginal gains over BYOL with vision transformers on ImageNet (p. 1068).
- **JEPA** (LeCun's roadmap): learn $z=f(x)$, $z'=f(x')$ and a predictor $\hat z'=g(z)$ with $\hat z'$ close to $z'$. It is similar to BYOL, but "close" can be more general than small squared distance (p. 1068).

**32.3.4.4 Tricks of the trade (pp. 1068–1069).**
- Normalising encoder outputs and using cosine similarity improves performance. Similarity is then bounded in $[-1,1]$, so a temperature $\tau$ (fixed or annealed) is used (p. 1068).
- Invariance can become too strong for some tasks. Remedies: take an earlier encoder layer as the representation, or add a *projection head* before the loss and discard it at evaluation (p. 1068).
- InfoNCE is sensitive to batch size, with batches of 4096 or more needed for good performance. MoCo adds a memory queue of negatives from earlier minibatches and a momentum (EMA) encoder. An extra predictor network improves MoCo and removes the need for the queue (pp. 1068–1069).
- Vision transformer backbones recently replaced ConvNets, giving larger models with improved performance (p. 1069).

### 32.4 Theory of representation learning (pp. 1069–1071)
The theory of what is learned, and what guarantees hold, is limited. The intro lists three directions: identifiability, information maximization and transfer bounds (p. 1069). Only the first two appear in these pages.

#### 32.4.1 Identifiability (pp. 1069–1070)
- Assume $z\sim p(z)$ and a deterministic generator $x=g(z)$. We want $h=f_\theta(x)$ with $h=z$, in which case the model is *identifiable* (p. 1069).
- Exact recovery is often impossible (permuted or elementwise-transformed latents $h_i=f_i(z_i)$). So theory focuses on representations equal to the true latents up to permutation and elementwise transformation, called *disentangled* (p. 1069).
- Locatello et al.'s large-scale study found that several existing methods cannot work without additional assumptions on data or model. Their argument: for a factorial prior $p(z)=\prod_ip_i(z_i)$ one can build a bijection $f$ mapping $z$ to $z'=f(z)$ that (1) preserves the marginal distribution and (2) entangles every latent (each $z_i$ affects every dimension of $z'$). The marginal likelihood of the data is unchanged, so marginal likelihood alone cannot distinguish entangled from disentangled models. Past successes largely came from tuning hyperparameters on disentanglement metrics that require supervised labels. Unsupervised hyperparameter selection has addressed some issues, but no known robust method exists without further assumptions (p. 1069).
- Routes to guarantees: (a) weakly labelled data in nonlinear ICA, i.e. additional observations related to the latents through an exponential family, and causal representation learning (p. 1070); (b) pairs of observations where only one latent changes (Shu et al., provably). Such pairs are hard to get in real data. Locatello et al. use a heuristic to detect the changed latent, which works empirically and may work under restricted settings (p. 1070); (c) [Kiv+21; Kiv+22]: deep latent variable models such as VAEs are identifiable without side information provided the latent prior is a mixture. Some latent causal structure is provably identifiable given data from multiple related environments (p. 1070).

> **Intuition note.** If many different latent codings assign the same probability to the data, fitting the data cannot tell you which coding is the "true" one. Extra information (weak labels, paired observations, a mixture prior) is what the routes listed below use to break the tie.

#### 32.4.2 Information maximization (pp. 1070–1071)
- One desideratum is to preserve information about $x$, since discarded information cannot be recovered. Linsker and Bell & Sejnowski argued that information maximization (InfoMax) is a good learning principle for biological systems. The text adds that such systems face strong constraints that evolution can likely tune, whereas networks can realise the trivial solution of copying the input losslessly (p. 1070).
- Information theory "does not 'color' the bits" (p. 1070): it does not say which bits matter. Architectural and optimisation constraints can guide which bits are kept, and extra information such as labels can also identify which bits to extract (p. 1070).
- **Information bottleneck:** representations $Z$ of $X$ that are predictive of $Y$ yet as compressed as possible [TPB00]:
$$\text{maximize}_\theta\ I(Z;Y)-\beta I(X;Z).\tag{32.21}$$
Variational bounds make this trainable (VIB). VIB-based approaches showed improved robustness to adversarial examples and natural variations (pp. 1070–1071).
- Many recent InfoMax-motivated methods have no explicit compression term (p. 1071).
- **Challenges:** most encoders are deterministic and continuous, so they can preserve infinite information. MI estimators scale poorly with the true MI, giving weak lower bounds. Without constraints, $z=x$ maximises information trivially. Tschannen et al. show that for invertible networks, where true MI is infinite, maximising MI estimators can still give meaningful representations. This suggests that the geometry and bias of the estimators may matter more than the information itself (p. 1071).
- Stochastic representations that constrain information have not yet improved most downstream tasks. Constraining information improved robustness on some benchmarks, but scaling up models and datasets with deterministic representations currently gives the best results. Whether constraining information helps remains to be shown (p. 1071).

## Toy example (ours, not from the text)
Anchor $x$ with $M=2$ negatives. Take $\ell_2$-normalised-free scores $s=f_\theta(x)^Tg_\phi(\cdot)$ for illustration.

**InfoNCE (32.16), single sample.** Positive score $s^+=2$, negative scores $0$ and $1$.
- $e^2=7.389$, $e^0=1$, $e^1=2.718$. Denominator $=7.389+1+2.718=11.107$.
- Ratio $=7.389/11.107=0.6652$, so loss $=-\ln 0.6652=0.4076$.
- If instead $s^+=0$ (positive no better than a negative): denominator $=1+1+2.718=4.718$, loss $=\ln4.718=1.551$. A better-aligned positive gives lower loss.
- Push negatives to $-5$ and $-4$: $e^{-5}=0.00674$, $e^{-4}=0.01832$. Denominator $=7.389+0.00674+0.01832=7.4140$, loss $=\ln(7.4140/7.389)=0.0034$. It is smaller but not zero, so InfoNCE keeps rewarding pushing negatives away.

**Triplet loss (32.15)** for comparison, with $\epsilon=2$ and squared distances $\|f(x)-f(x^+)\|^2=1$:
- Negative at squared distance $9$: $\max(0,1-9+2)=\max(0,-6)=0$. No gradient, no learning.
- Negative at squared distance $1.5$: $\max(0,1-1.5+2)=1.5$. A close (hard) negative is penalised.

This shows why the triplet loss depends on choosing hard negatives while InfoNCE does not need a threshold.

## Concepts
- [[bnp-model]] (new) — Bayesian nonparametric model: prior placed directly on functions, distributions or graphs, usually via a stochastic process (p. 1047)
- [[stochastic-process]] (new) — probability distribution over a potentially infinite set of random variables (p. 1047)
- [[representation-learning]] (new) — training a model to transform inputs so that new, possibly unknown tasks become easier (p. 1049)
- [[linear-evaluation]] (new) — freeze the network and train only a linear classifier on a chosen layer's features (p. 1050)
- [[fine-tuning]] (new) — adapt all network parameters (plus a new layer) on the downstream task (p. 1051)
- [[representational-similarity-analysis]] (new) — compare two representations via $n\times n$ similarity matrices of the same examples plus a matrix similarity $s(K,K')$ (p. 1052)
- [[centered-kernel-alignment]] (new) — cosine similarity between centered kernel matrices; linear version equals the RV coefficient of centered features (p. 1053)
- [[canonical-correlation-analysis]] (new) — maps two representations to a shared space of maximally correlated orthogonal directions; variants SVCCA, PWCCA (p. 1053)
- [[pretext-task]] (new) — self-supervised task with cheaply generated labels, used only to train the representation (p. 1062)
- [[masked-prediction]] (new) — replace tokens or patches with masks and predict only the missing parts (p. 1062)
- [[analysis-by-synthesis]] (new) — perception as inferring latent factors that could synthesise the observations (p. 1059)
- [[multiview-representation-learning]] (new) — pull positive pairs together in embedding space, with a mechanism against collapse (p. 1064)
- [[infonce-loss]] (new) — softmax-over-candidates contrastive loss; $I(X;Z)\ge\log M-\mathcal L_{\rm InfoNCE}$ (p. 1067)
- [[representation-collapse]] (new) — all inputs mapped to the same point (or low-rank solution), prevented by negatives, extra loss terms, or dynamics (p. 1064)
- [[identifiability-disentanglement]] (new) — recovering latents up to permutation and elementwise transform; not possible from marginal likelihood alone (p. 1069)
- [[information-bottleneck]] (new) — maximise $I(Z;Y)-\beta I(X;Z)$: predictive yet compressed representations (p. 1070)
- [[marginal-likelihood-evidence]] — here: a quantity that stays unchanged under the entangling bijection, so it cannot identify the disentangled model (p. 1069)
- [[variational-inference-elbo]] — only mentioned: VAEs train latent-variable models with variational inference, and VIB uses variational MI bounds (pp. 1060, 1071)

## Canonical instances
- [[gaussian-process]] — BNP prior over functions with jointly Gaussian finite marginals (p. 1047)
- [[simclr]] — positives from two augmentations of one image (p. 1065)
- [[clip]] — image/text contrastive pretraining enabling zero-shot transfer (pp. 1058, 1066)
- [[bert-masking]] — 15% selected, 80/10/10 mask/random/keep (p. 1062)
- [[masked-autoencoder-mae]] — 75% masking, shallow pixel decoder with $L_2$ loss (p. 1063)
- [[byol-simsiam]] — MSE between predictor of online net and target net, no negatives (pp. 1067–1068)
- [[locatello-nonidentifiability]] — an entangling bijection keeps the marginal likelihood, so disentanglement is not identifiable from it alone (p. 1069)
- [[linear-autoencoder-pca]] — linear autoencoder with MSE can learn principal components (p. 1061)

## Bridges (candidates)
- [structural-analogy] InfoNCE (32.16) ↔ softmax cross-entropy: positive is the correct "class" among $M+1$ candidates.
- [same-math] Linear CKA ↔ RV coefficient: stated equivalence on centered features (p. 1053).
- [same-math] $R^2_{\rm LR}$ (32.8) ↔ regression: stated equivalence to the variance explained by regressing $\tilde Y$ on $\tilde X$ (32.9) when $p_2\ge p_1$.
- [structural-analogy] Analysis-by-synthesis (posterior $p_\theta(z\mid x)$ as representation) ↔ Bayesian inference: the representation is a posterior summary of latent variables.
- [structural-analogy] Non-identifiability of disentanglement ↔ Bayesian non-identifiability: different parameterisations give the same likelihood, so the data cannot choose between them.
- [structural-analogy] Linear autoencoder ↔ PCA: both recover the top principal subspace under MSE.

## Questions this raises
- Under what weak assumptions (mixture priors, paired observations, multiple environments) can contrastive or generative methods be shown to identify the latents?
- Can a probabilistic treatment of representations (a posterior over $z$ rather than a point) improve robustness more reliably than deterministic encoders?
- Which similarity measure should be used when networks differ in width, and how can the sensitivity reported for RNNs be reduced?
- Why do BYOL, SimSiam and DINO avoid collapse? Only a simplified linear analysis is cited here.

## Reading notes
- Printed = pdf − 34 (pdf 1081 = p. 1047). The unit contains the one-page intro of Ch. 31 (Rao) and Ch. 32 (Poole & Kornblith). Footer reads "Online version. December 10, 2025". Pdf 1082 (p. 1048) and pdf 1106 (p. 1072) are blank.
- §32.4's opening sentence lists "transfer bounds" as a direction, but no such subsection appears in these pages. The chapter text ends after 32.4.2.
- Apparent misprints in the source: "Figue 32.2"; p. 1065 says all methods have "a repulsion component that pulls positive pairs closer" (presumably *attraction*); p. 1066 says negatives are chosen "by randomly choosing $x^+$" from the minibatch (presumably $x^-$); "a task that where labels" (p. 1057). Fig. 32.3 caption cites He+21 while the text cites He+22. In (32.6) the image prints the primed matrices with index range $1{:}k$; the digest writes $1{:}k'$, following the text's definition of $k'$.
- Eq. (32.8): $\alpha_i'$ has a sum over $j$ in the image but $j$ does not appear in the summand (read as printed). Eq. (32.11) has both sums running to $p_2$ in the image, while (32.10) uses $p_1$ and $p_2$; copied as printed.
- Eq. (32.20) as printed applies centering and $\tau'$ to $f_\theta(x^+)$ (the online network, per the BYOL notation), whereas the text says the *target* network is centered and has the lower temperature. I report both and do not resolve this.
- Several claims are reported as the author's summaries of cited work (e.g. results of Kornblith, Locatello, Tschannen); the digest reports them with the author's wording of strength.
