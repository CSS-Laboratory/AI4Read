---
id: prince-2023-udl/ch20-does
work: prince-2023-udl
unit: "Chapter 20 — Why does deep learning work?"
pages: 402-420
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Why does deep learning work?

## L0 — One line
Deep networks are surprisingly easy to fit and surprisingly good at generalizing, and the evidence points to overparameterization, architecture and training details, but there is still no predictive theory.

## L1 — The gist (≤ 120 words)
The chapter asks why deep networks train and generalize when, on paper, they should not. It reviews empirical evidence rather than settled results. For training, overparameterization (more parameters than training data) and the activation function matter most. Dataset structure, batch randomness and explicit regularization seem less important. Loss surfaces appear to have many connected global minima and no obvious bad local minima. For generalization, factors include the training algorithm, flat minima (insensitive to small parameter errors), weight norm, architecture and overparameterization. Pruning and distillation have not shown that models with fewer parameters than data can match large ones. Depth seems to matter, but there is no definitive explanation. The author's conclusion: we lack a theory that predicts when training and generalization succeed.

**Prerequisites:** SGD and loss surfaces; local minima and saddle points; overfitting and regularization; the Hessian and its eigenvalues; convolutional networks; ReLU; pruning (removing weights from a trained network); distillation (training a small model to copy a large one); weight norm (size of the weight vector).

## L2 — Key ideas (5–10 bullets)
- Both fitting and generalization are surprising: finding the global minimum of an arbitrary non-convex function is NP-hard (also true for certain network losses), and the number of possible inputs dwarfs the training set (pp. 402–403).
- Networks can fit random pixels and random labels (Zhang et al.), neither L2 regularization nor Dropout was required, and full-batch training also fits random labels. This suggests that dataset structure, explicit regularization and SGD noise are not what makes fitting easy (pp. 404–405).
- Overparameterization (more parameters than training data) almost certainly is an important factor in easy training, but convergence theorems usually rest on unrealistic assumptions (pp. 405–406).
- Loss surfaces appear to have large families of connected global minima, low-dimensional training paths, and few or no bad local minima (pp. 408–411).
- Generalization is linked to SGD's implicit regularization (extra loss terms from finite-step-size SGD), flat minima (where small parameter errors matter little), weight norm in a "Goldilocks zone" (a weight-norm range with positive curvature and good generalization), architecture and overparameterization. Weight norm is used to explain grokking (generalization improving long after training error is zero) and double descent (generalization improving with overparameterization) (pp. 411–414).
- Adversarial examples (inputs close to the data that are misclassified after a tiny change) seem to exploit small-norm information present in the training distribution (p. 415).
- Pruning (removing weights from a trained network) and distillation (training a small student to copy a large teacher) have not produced convincing underparameterized models (fewer parameters than data). Bubeck & Sellke prove that in $D$ dimensions smooth interpolation needs $D$ times more parameters than mere interpolation (pp. 415–418).
- Depth seems needed, but there is no definitive explanation. Three candidate explanations: complexity of the functions, ease of training, and inductive bias (built-in architectural assumptions) (pp. 418–419).

## L3 — Walkthrough

### Opening (p. 402)
The chapter poses questions rather than presenting established results. Understanding of deep learning "is still limited" (p. 402).

### 20.1 The case against deep learning
**20.1.1 Training (pp. 402–403).**
- On MNIST-1D (40 inputs, 10 outputs), a two-layer fully connected network fits 10,000 training points perfectly at 43 hidden units per layer, about 4000 parameters (p. 402).
- Finding the global minimum of an arbitrary non-convex function is NP-hard. This is also true for certain neural-network losses (p. 402).
- So it is remarkable that fitting does not get trapped in local minima or near saddle points (p. 402).
- Overparameterization (more parameters than data) might explain this, but it is debatable whether it holds generally. AlexNet had ~60M parameters and ~1M data points, each augmented with 2048 transformations. GPT-3 had 175B parameters and 300B tokens. There is no clear-cut case that either was overparameterized (p. 403).
- The author's conclusion: data, models, training algorithms, or some combination must have special properties (p. 403).

**20.1.2 Generalization (p. 403).**
- *Curse of dimensionality* (inputs vastly outnumber data): quantizing each of 40 MNIST-1D inputs to 10 values gives $10^{40}$ inputs, $10^{36}$ times the number of training examples.
- A two-hidden-layer, width-400 network can make up to $10^{42}$ linear regions, about $10^{38}$ per training example. Very few regions contain data, yet those that do constrain the rest to behave reasonably.
- Generalization improves with more parameters. The 177,201-parameter model has 167,201 spare degrees of freedom (assuming one example fitted per parameter), yet behaves sensibly.

**20.1.3 (p. 403).** A priori, deep learning "shouldn't work. And yet it does." Sections 20.2–20.3 cover fitting and loss functions. Sections 20.4–20.6 cover generalization.

*Intuition note:* There are far more possible inputs than training examples. Models can also do almost anything between training points. Success is therefore not guaranteed by counting arguments.

### 20.2 Factors that influence fitting performance (pp. 403–407)
Loss functions can have local minima and saddle points (figure 6.4), yet fitting reliably reaches zero error (p. 403). Footnote 1: "global minimum" here loosely means any solution classifying all data correctly (p. 404).

**20.2.1 Dataset (p. 404).** A completely random mapping from 28×28 binary images to ten classes could only be memorized ($2^{784}$ assignments). Hypothesis: real-world functions are simple. Zhang et al. (2017a) trained AlexNet on CIFAR-10 (50,000 images, 10 classes) with (i) Gaussian-noise images, and (ii) randomly permuted labels. Learning was slower, slowest for random labels, but the data were still fit (figure 20.1). The author says this suggests dataset properties aren't critical.

**20.2.2 Regularization (p. 404).** Neither L2 regularization nor Dropout was required to fit random data (Zhang et al.). Implicit regularization from finite step size grows with learning rate (eq. 9.9), but fitting does not get easier with larger learning rates.

**20.2.3 Stochastic algorithms (pp. 404–405).**
- Keskar et al. (2017): various models fit many datasets almost perfectly with very large batches (5000–6000 images), removing most randomness.
- Figure 20.2: four fully connected nets with 1–4 layers (298, 100, 75, 63 hidden units; about 15,200 parameters each) were fit to 4000 MNIST-1D examples with random labels. Setup: full-batch gradient descent, He initialization, no momentum or regularization, learning rate 0.0025. All trained to zero error. Deeper models needed fewer epochs.
- Here the labels are unstructured, training is deterministic and there is no regularization, yet error still reaches zero. The author concludes this suggests these losses "may genuinely have no local minima."

**20.2.4 Overparameterization (pp. 405–406).**
- It "almost certainly is" important. It implies many degenerate solutions, so there may always be a direction that decreases loss. Sejnowski (2020): a "haystack of needles" rather than a needle in a haystack (p. 405).
- Networks are often overparameterized by one or two orders of magnitude (figure 20.3). Augmentation makes this imprecise, since augmented data are not independent. Figure 8.10 shows that networks can sometimes fit the training data with equal or fewer parameters than data, presumably due to redundancy in the examples (p. 405).
- Convergence results hold under certain circumstances. Du et al. (2019b): randomly initialized SGD reaches a global minimum for shallow fully connected ReLU nets with least-squares loss and enough hidden units. Du et al. (2019a) cover deep, residual and convolutional nets with smooth, Lipschitz activations. Zou et al. (2020) treat deep fully connected nets with hinge loss. Allen-Zhu et al. (2019) treat deep ReLU nets (p. 405).
- If a network can memorize any dataset of a fixed size, all stationary points become global minima (Livni; Nguyen & Hein). If the network is wide enough, bad local minima are rare. Kawaguchi et al. prove that for squared loss, loss at local minima approaches the global minimum as the network gets deeper, wider or both (p. 406).
- Caveat: these results usually make unrealistic assumptions about the network. Du et al. (2019a) need width $D = \Omega[I^4K^2]$ ($I$ data points, $K$ depth). Nguyen & Hein assume width exceeds dataset size. "Theory cannot yet explain empirical fitting performance" (p. 406).

**20.2.5 Activation functions (p. 406).** Activations that change over only a small input range are harder to fit than ReLU or Leaky ReLU. Sigmoid and tanh have near-zero gradients in their tails, so learning is very weak there.

**20.2.6 Initialization (pp. 406–407).** Xavier/He initialization is necessary in deep nets to avoid exploding and vanishing gradients. For shallower nets, initial weight variance matters less. Liu et al. (2023c): a 3-layer, 200-unit net on 1000 MNIST points needed more iterations as the variance rose above He's, but still fit (figure 20.4). So initialization says little about why fitting is easy.

**20.2.7 Network depth (p. 407).** Very deep nets are harder to fit because of exploding, vanishing and shattered gradients, which are arguably practical numerical issues. There is no definitive evidence that the loss is fundamentally more or less convex with depth. In figure 20.2 deeper nets train faster, which might be (i) steeper gradients or (ii) He initialization starting wider, shallower nets further from the optimum. Frankle & Carbin (2019), for small networks like VGG:
1. train the network;
2. prune the smallest-magnitude weights;
3. retrain from the same initial weights.

This gives the same or better performance, but not if the weights are re-initialized randomly. They conclude the original network contains small trainable sub-networks (*winning tickets*), the *lottery ticket hypothesis*. The effective number of sub-networks may matter; a precise characterization is lacking.

*Intuition note:* Dataset structure, SGD noise and explicit regularization do not seem to be needed to fit data. More parameters give more ways to reduce the loss, and good activations keep gradients alive. Theory does not yet cover realistic settings.

### 20.3 Properties of loss functions (pp. 407–411)
The section opens by restating that the number of parameters and the activation function are both important, while dataset, fitting-algorithm randomness and regularization don't seem important, and there is no definitive evidence that depth matters beyond numerical gradient problems (p. 408). Most evidence comes from fully connected nets and CNNs; transformer loss functions are less well understood (p. 408).

**20.3.1 Multiple global minima (p. 408).** Equivalent minima come from:
- permuting hidden units, or channels with their kernels;
- scaling weights around a ReLU (multiply before, divide after, by a positive number);
- BatchNorm redundancies.

Overparameterized nets also have solutions that agree at the data points but differ between them. All are global minima.

**20.3.2 Route to the minimum (p. 408).**
- Goodfellow et al. (2015b): along a straight line from initial to final parameters, the loss usually decreases monotonically, with sometimes a small bump near the start (figure 20.5a).
- Li et al. (2018b): real trajectories lie in low-dimensional subspaces. They attribute this to large, nearly convex regions that funnel the trajectory.
- Li et al. (2018a): training still works when constrained to a random low-dimensional subspace. In figure 20.6, 90% of unconstrained performance is reached at 750 dimensions (the *intrinsic dimension*, 0.4% of parameters) (p. 409).
- Li & Liang (2018): with greater width, parameters change by a smaller proportion and converge in fewer steps.

**20.3.3 Connections between minima (pp. 409–410).**
- Goodfellow et al. (2015b): a straight line between two independently found minima shows a pronounced loss increase (figure 20.5b). Good minima are not generally linearly connected.
- Frankle et al. (2020): the increase vanishes if networks are trained identically at first and later diverge via different SGD noise and augmentation. The author says this suggests the solution is constrained early and that *some* families of minima are linearly connected.
- Draxler et al. (2018): curved low-loss paths join different CIFAR-10 minima. They conclude there is a single connected manifold of low loss (figure 20.7); this seems to be increasingly true as width and depth grow.

**20.3.4 Curvature (p. 411).**
- In random Gaussian functions, at zero-gradient points the fraction of downward-curving directions is smaller at lower loss values (Bahri et al., 2020).
- Dauphin et al. (2014) found a similar correlation between loss and number of negative Hessian eigenvalues at neural-net critical points (figure 20.8).
- Baldi & Hornik (1989): a shallow network has no local minima, only saddle points. The author: these results suggest few or no bad local minima.
- Fort & Scherlis (2019): curvature is unusually positive when the $\ell_2$ weight norm is in a certain range, the *Goldilocks zone*. He and Xavier initialization fall within it (figure 20.9).

*Intuition note:* Many different weight settings give the same fit, and they appear to be connected. Where the gradient is zero, being a *bad* minimum requires no downhill direction at high loss, which looks rare.

### 20.4 Factors that determine generalization (pp. 411–415)
**20.4.1 Training algorithms (pp. 411–412).** In overparameterized nets, training details determine which minimum is reached. LeCun et al. (2012): SGD generalizes better than full-batch gradient descent. SGD vs. Adam: argued before, but little difference with careful hyperparameter search (Choi et al.). Keskar et al.: smaller batches generalize better when no other regularization is used. Larger learning rates tend to generalize better. He et al. (2019) show a significant correlation with the batch size/learning rate ratio and prove a bound positively correlated with it (figure 20.10). This fits SGD's implicit regularization (section 9.2), whose size depends on learning rate.

**20.4.2 Flatness (pp. 412–413).**
- Speculation since Hochreiter & Schmidhuber (1997a): flat minima generalize better than sharp ones (figure 20.11), because small parameter errors matter less. Minimum description length theory also motivates this: wide minima need less weight precision.
- Flatness measures: (i) size of the region of similar training loss, (ii) second-order curvature, (iii) maximum loss in a neighborhood. Caution: ReLU's non-negative homogeneity means trivial reparameterizations can change estimated flatness (Dinh et al.).
- Keskar et al.: varying batch size and learning rate shows flatness correlates with generalization. Izmailov et al.: averaging weights along the trajectory flattens surfaces and improves generalization. Ensembling may also flatten the test loss. Kleinberg et al.: large gradient variance helps avoid sharp regions.
- Limit: sharpness alone is not a good criterion for predicting generalization between datasets. With randomized CIFAR labels there is no commensurate sharpening (Neyshabur et al.).

**20.4.3 Architecture (p. 413).** Architecture sets the inductive bias (built-in assumptions). CNNs share parameters across position, transformers suit permutation-invariant data, and GNNs suit irregular graphs. Matching architecture to data improves generalization over fully connected nets.

**20.4.4 Norm of weights (p. 413).** Fort & Scherlis: generalization is also good when the $\ell_2$ weight norm is in the Goldilocks zone (figure 20.12). The author's reading: the norm is indirectly related to the Lipschitz constant (a bound on how fast the function can change). Too small, and the model cannot capture the function's variation. Too large, and it is unnecessarily variable between training points. Liu et al. (2023c) use this to explain *grokking* (Power et al., 2022), where generalization improves suddenly many epochs after training error is zero (figure 20.13). Proposal: the initial norm is too large; regularization lowers it until it reaches the zone.

**20.4.5 Overparameterization (pp. 413–414).** Generalization tends to improve with overparameterization; combined with the bias/variance curve this gives *double descent*. Putative explanation: more latitude to be smooth between data points. The author adds that weight norm can explain it too. Norm rises when parameters ≈ data points (the model contorts to fit exactly), lowering generalization. With more width the norm falls, because initial variance is inversely proportional to width and weights need change less.

**20.4.6 Leaving the data manifold (pp. 414–415).**
- Deployed models may meet noise, drift or attacks. D'Amour et al. (2020): identical models with different seeds on corrupted data can vary enormously and unpredictably.
- Goodfellow et al. (2015a): perturb a correctly classified "dog" image so the correct-class probability falls as fast as possible until the class flips. The result looks almost identical to the original, not like a dog–airplane cross (figure 20.14).
- So positions near but off the data manifold are misclassified: *adversarial examples*. Best current explanation (Ilyas et al., 2019): they exploit information that is in the training distribution but has small norm and is imperceptible to humans.

*Intuition note:* Among many equally good fits, training details determine which one is found, and some details reliably improve generalization. Flatness, weight norm and smoothness between data points are the properties proposed to explain which fits generalize well.

### 20.5 Do we need so many parameters? (pp. 415–418)
Almost no state-of-the-art results come from models with significantly fewer parameters than data points. But training is also easier with more parameters. So it is unclear whether small models are inherently limited or just hard to train (p. 415).

**20.5.1 Pruning (p. 416).** Remove weights by second derivatives or by absolute value, or remove units, channels or layers; often fine-tune after (figure 20.15). Han et al. (2016) kept good VGG ImageNet performance with 8% of weights, but VGG has ~100× more parameters than training examples. Frankle & Carbin (iterated procedure above): VGG-19 (138M parameters) cut by 98.5% on CIFAR-10 (60,000 examples). ResNet-50 (25.6M) cut by 80% on ImageNet (1.28M examples). Still overparameterized after pruning, disregarding augmentation.

**20.5.2 Knowledge distillation (pp. 416–417).** A smaller *student* is trained to mimic a larger *teacher*. Hinton et al. (2015) trained the student to approximate the teacher's pre-softmax logits (figure 20.16). Zagoruyko & Komodakis (2017), *attention transfer*: an 18-layer ResNet (~11M) approximates a 34-layer one (~63M) on ImageNet, still above ~1M images. Distillation has "not yet provided convincing evidence" that underparameterized models work well.

**20.5.3 Discussion (pp. 417–418).** Current evidence suggests overparameterization is needed for generalization, at least for current dataset sizes and complexity. Bubeck & Sellke (2021) proved that in $D$ dimensions, smooth interpolation requires $D$ times more parameters than mere interpolation. They argue that current models on large datasets (e.g., ImageNet) aren't overparameterized enough.

### 20.6 Do networks have to be deep? (pp. 418–419)
Shallow nets can approximate any function in principle (universal approximation, chapter 3). Evidence for depth: performance improved with depth until training became hard. Residual connections and batch normalization then allowed deeper nets with commensurate gains. State-of-the-art systems use tens or hundreds of layers (p. 418). Counter-efforts: wider, shallower ResNets (Zagoruyko & Komodakis, 2016) perform similarly. Goyal et al. (2021) used parallel convolutional channels for similar performance with 12 layers. Veit et al.: shorter paths of 5–17 layers drive performance in residual nets. Still, the shallowest good image classifiers need >10 layers, with no definitive explanation. Candidates (p. 418):

- **20.6.1 Complexity.** Deep nets make more linear regions per parameter, and "pathological" functions need exponentially more shallow units (Eldan & Shamir; Telgarsky). Liang & Srikant found general families that deep nets model more efficiently. But Nye & Saxe found some of these cannot easily be fit by deep nets in practice. There is little evidence that real-world functions are pathological (p. 418).
- **20.6.2 Trainability.** Urban et al. (2017) distilled an ensemble of 16 CIFAR-10 CNNs into students of varying depth. Shallow students could not replicate the teacher. Performance rose with depth at constant parameter budget (p. 419).
- **20.6.3 Inductive bias.** Conv blocks and transformers share parameters locally and integrate gradually. Such constraints may be a good bias that shallow nets struggle to obey (p. 419). Evidence: an untrained CNN's structure works as a prior for denoising and super-resolution (Ulyanov et al.). Fixed random kernels with only BatchNorm offsets and scales trained give good classification (Frankle et al., 2021). Random conv features plus a kernel model support classification (Zhang et al., 2017a). Distilling into convolutional students beat fully connected ones (Urban et al.). The author concludes this argues depth is important (p. 419).

### 20.7 Summary (pp. 419–420)
Overparameterization and activation choice are the author's two most important factors for tractable optimization. Parameters move through a low-dimensional subspace to one of a connected family of global minima, and local minima are not apparent. Generalization improves with overparameterization; flatness and inductive bias also matter. Both many parameters and multiple layers appear required, "although we do not yet know why" (p. 420). There is no prescriptive theory predicting success or failure, and the field is still driven by empirical demonstrations (p. 420).

## Toy example (ours, not from the text)
One training point $x=(1,2)$, label $y=3$, linear model $f(x)=w_1x_1+w_2x_2$, loss $L=(w\cdot x-y)^2$, two parameters vs one datum. Global minima: all $w$ with $w_1+2w_2=3$ (a line, a "degenerate family").
- Start $w=(0,0)$: $w\cdot x=0$, residual $-3$, gradient $=2(-3)(1,2)=(-6,-12)$. Step 0.1: $w=(0.6,1.2)$; $w\cdot x=0.6+2.4=3$, loss 0.
- Start $w=(1,0)$: $w\cdot x=1$, residual $-2$, gradient $=(-4,-8)$, step 0.1: $w=(1.4,0.8)$; $w\cdot x=1.4+1.6=3$, loss 0.
- Both reach zero loss: one step of size 0.1 works from either start, and the update moves along the data direction.
- On a new input $(2,-1)$: first solution gives $1.2-1.2=0$; second gives $2.8-0.8=2$.

Both fit the training data and disagree elsewhere. Which one is found depends on initialization and training details, echoing sections 20.2.4 and 20.4.1.

## Concepts
- [[overparameterization]] (new) — more parameters than training data; gives a family of degenerate solutions and contributes to ease of training (p. 405)
- [[implicit-regularization]] (new) — finite-step-size SGD adds loss terms whose size depends on learning rate (pp. 404, 412)
- [[lottery-ticket-hypothesis]] (new) — the original overparameterized network contains small trainable sub-networks ("winning tickets") sufficient for its performance (p. 407)
- [[mode-connectivity]] (new) — minima joined by low-loss paths, possibly one connected low-loss manifold (p. 409)
- [[intrinsic-dimension]] (new) — random-subspace dimension at which performance reaches 90% of the unconstrained level (p. 409)
- [[goldilocks-zone]] (new) — weight-norm range with positive curvature and good generalization (pp. 411, 413)
- [[flat-minima]] (new) — minima where small parameter errors matter little; speculated to generalize better (p. 412)
- [[grokking]] (new) — generalization improving long after training error is zero (p. 413)
- [[double-descent]] (new) — generalization improving with overparameterization on top of the bias/variance curve (p. 413)
- [[adversarial-example]] (new) — imperceptibly perturbed input that is misclassified (p. 415)
- [[pruning]] (new) — removing weights, units, channels or layers from a trained network (p. 415)
- [[knowledge-distillation]] (new) — training a student to mimic a teacher's outputs (p. 416)
- [[inductive-bias]] (new) — constraints from architecture that favor some functions (p. 413)

## Canonical instances
- [[zhang-random-labels]] (new) — AlexNet fits random pixels and random labels on CIFAR-10 (p. 404)
- [[mnist-1d-full-batch]] (new) — full-batch fits of random labels; deeper nets need fewer epochs (p. 405)
- [[adversarial-ostrich]] (new) — near-identical images misclassified as an ostrich (fig. 20.14, p. 415)
- [[vgg-19-pruning]] (new) — 98.5% of parameters removed on CIFAR-10 (p. 416)
- [[urban-distillation]] (new) — shallow students fail to match a deep ensemble (p. 419)

## Bridges (candidates)
- [structural-analogy] Bubeck & Sellke: smooth interpolation needs ~D× more parameters ↔ llm: scaling laws, where loss falls as parameters grow — both tie capacity to quality
- [metaphor] Grokking as weight norm falling into the Goldilocks zone ↔ llm: delayed generalization during long pretraining
- [structural-analogy] Distillation of a teacher's logits ↔ llm: training small models on large-model outputs
- [structural-analogy] Double descent via weight norm ↔ classical bias/variance trade-off

## Questions this raises
- Can a theory predict when training and generalization succeed, rather than describe results afterward (p. 420)?
- Do the loss-surface findings, from fully connected nets and CNNs, hold for transformers (p. 408)?
- Is there an architecture or training method that matches large models with fewer parameters than data (pp. 417–418)?
- Why does depth help beyond complexity, trainability and inductive bias (p. 418)?

## Exercises worth doing
- Ex. 20.1 (p. 420) — counting possible inputs per training point on ImageNet-sized images; the curse of dimensionality — difficulty: easy
- Ex. 20.2 (p. 420) — why random pixels fit faster than random labels in figure 20.1 — difficulty: medium
- Ex. 20.3 (p. 420) — whether fitting random data deterministically implies no local minima or convexity — difficulty: medium

## Reading notes
- Printed page = pdf page − 14 (pdf 416 = printed 402).
- Figures were checked against the page images. The text layer is garbled in a few places (e.g., "1040" = $10^{40}$, "2784" = $2^{784}$, "1042" = $10^{42}$). The images confirm the superscripts.
- Odd printed pages carry the footer "Draft: please send errata…" (even pages carry the license line), so this appears to be a draft printing.
- Margin notes point to Notebooks 20.1–20.4 (random data, full-batch gradient descent, lottery tickets, adversarial attacks). Their content is not in these pages.
- In 20.1.2, "167,201 spare degrees of freedom" equals 177,201 − 10,000. The 10,000 training examples come from 20.1.1, not restated there.
- Figure 20.1 shows random-pixel inputs fit faster than random labels. Problem 20.2 asks the reader to explain why.
