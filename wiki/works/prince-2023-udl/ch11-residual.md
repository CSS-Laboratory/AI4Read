---
id: prince-2023-udl/ch11-residual
work: prince-2023-udl
unit: Chapter 11 — Residual networks
pages: 186-206
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Residual networks

## L0 — One line
Letting each layer add a change to its input (a residual connection), plus batch normalization to tame the growing variance, makes much deeper networks trainable.

## L1 — The gist (≤ 120 words)
Very deep plain convolutional networks train worse than shallower ones, on training data as well as test data. A conjecture is that gradients "shatter" in deep sequential networks. The chapter introduces residual blocks, y = x + f[x], which give every layer a short path to the output and so reduce shattered gradients. With He initialization (a standard weight-variance rule for ReLU nets) they make activation variance double per block at initialization. Batch normalization compensates for this; in a residual net with batch normalization the variance grows only linearly. The chapter then reviews ResNet, DenseNet, U-Net and hourglass networks. It also reports that residual connections seem to help for reasons beyond depth. Residual connections are now a standard part of deep learning pipelines.

**Prerequisites:** layers, ReLU, backpropagation and the chain rule; He initialization (section 7.5); variance of sums; convolutions and channels.

## L2 — Key ideas (5–10 bullets)
- A plain 56-layer convolutional network does worse than a 20-layer one, on both training and test sets. This implies the problem is training deep networks, not generalizing (pp. 187–188).
- One conjecture is shattered gradients: in deep networks the gradient changes unpredictably for finite step sizes (pp. 187–189).
- A residual block computes $\mathbf{h}_k=\mathbf{h}_{k-1}+\mathbf{f}_k[\mathbf{h}_{k-1}]$. Unraveling (expanding the equations into a sum) shows the net as an ensemble of smaller networks, or, for four blocks, sixteen paths. In general, gradients through shorter paths are better behaved (pp. 189–191).
- With He initialization (a weight-variance rule for ReLU nets), residual forward-pass variance doubles per block, so it grows exponentially. A similar argument applies to the gradients (p. 192).
- Batch normalization standardizes each unit over the batch, then rescales with learned $\gamma,\delta$. In residual nets, when it starts each branch with $\gamma=1,\delta=0$ at initialization, it makes variance grow only linearly and later layers start near the identity (pp. 193–194).
- Batch normalization also permits higher learning rates and adds regularizing noise. Its costs are redundant weight scalings and extra parameters (p. 194).
- Residual designs include ResNet (bottleneck blocks of 1×1, 3×3, 1×1 convolutions), DenseNet (concatenating earlier outputs instead of adding), U-Net and hourglass nets (encoder–decoder networks with skips from encoder to decoder) (pp. 195–198).
- Evidence suggests depth alone does not explain the gains. Wider shallower nets sometimes win, and residual loss surfaces tend to be smoother (p. 199).

## L3 — Walkthrough

### 11.1 Sequential processing (pp. 186–189)
A sequential network feeds each layer's output to the next:
$$\mathbf{h}_1=\mathbf{f}_1[\mathbf{x},\phi_1],\ \mathbf{h}_2=\mathbf{f}_2[\mathbf{h}_1,\phi_2],\ \mathbf{h}_3=\mathbf{f}_3[\mathbf{h}_2,\phi_3],\ \mathbf{y}=\mathbf{f}_4[\mathbf{h}_3,\phi_4]\tag{11.1}$$
Equivalently it is nested functions: $\mathbf{y}=\mathbf{f}_4[\mathbf{f}_3[\mathbf{f}_2[\mathbf{f}_1[\mathbf{x},\phi_1],\phi_2],\phi_3],\phi_4]$ (11.2) (pp. 186–187).

**11.1.1 Limitations.** VGG (19 layers) beats AlexNet (8 layers). Adding still more layers lowers accuracy again (fig. 11.2: 20-layer beats 56-layer on CIFAR-10). The drop appears on the training set too, so the author concludes the problem is training deep nets, not generalizing (p. 187).

The author says the phenomenon "is not completely understood". One conjecture (offered without proof; the author says the phenomenon is not completely understood):
- Gradients are computed for an infinitesimal change, but optimizers take finite steps.
- In deep nets a step may reach a place with a completely different, unrelated gradient. The loss surface looks like "an enormous range of tiny mountains" (p. 187).
- Support: for a network with one input and one output, $\partial y/\partial x$ varies slowly in a shallow net. In a deep net (24 layers) it changes rapidly, and its autocorrelation drops to near zero. This is called *shattered gradients* (pp. 187–188, fig. 11.3).

Presumed reason: the derivative of $\mathbf{y}$ with respect to the first layer is
$$\frac{\partial \mathbf{y}}{\partial \mathbf{f}_1}=\frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_1}\frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_2}\frac{\partial \mathbf{f}_4}{\partial \mathbf{f}_3}\tag{11.3}$$
Changing $\mathbf{f}_1$'s parameters moves the point where all these factors are evaluated, because later layers are computed from $\mathbf{f}_1$. So the gradient may change completely (p. 189).

*Intuition note:* A long chain of factors depends on where every factor is evaluated. A small step early on can therefore change the gradient a lot, so the gradient just computed may be a poor guide for the next step.

### 11.2 Residual connections and residual blocks (pp. 189–192)
A residual (skip) connection adds a layer's input back to its output:
$$\mathbf{h}_1=\mathbf{x}+\mathbf{f}_1[\mathbf{x},\phi_1],\ \mathbf{h}_2=\mathbf{h}_1+\mathbf{f}_2[\mathbf{h}_1,\phi_2],\ \mathbf{h}_3=\mathbf{h}_2+\mathbf{f}_3[\mathbf{h}_2,\phi_3],\ \mathbf{y}=\mathbf{h}_3+\mathbf{f}_4[\mathbf{h}_3,\phi_4]\tag{11.4}$$
Each $\mathbf{f}_k$ learns an additive change, so its output must have the same size as its input. Input plus processed output is a *residual block* (p. 189).

Substituting gives the "unraveled" network (11.5): $\mathbf{y}$ is $\mathbf{x}$ plus four terms, $\mathbf{f}_1[\mathbf{x}]$, $\mathbf{f}_2[\mathbf{x}+\mathbf{f}_1[\mathbf{x}]]$, and so on, with $\mathbf{f}_3$ and $\mathbf{f}_4$ applied to ever longer sums (p. 189, fig. 11.4b). Written out: $$\mathbf y=\mathbf x+\mathbf f_1[\mathbf x]+\mathbf f_2\big[\mathbf x+\mathbf f_1[\mathbf x]\big]+\mathbf f_3\big[\mathbf x+\mathbf f_1[\mathbf x]+\mathbf f_2[\mathbf x+\mathbf f_1[\mathbf x]]\big]+\mathbf f_4\Big[\mathbf x+\mathbf f_1[\mathbf x]+\mathbf f_2[\mathbf x+\mathbf f_1[\mathbf x]]+\mathbf f_3\big[\mathbf x+\mathbf f_1[\mathbf x]+\mathbf f_2[\mathbf x+\mathbf f_1[\mathbf x]]\big]\Big]\tag{11.5}$$ Two readings:
- an *ensemble* of smaller networks whose outputs are summed;
- sixteen paths of differing length from input to output (p. 191).

$\mathbf{f}_1$ appears in eight of the sixteen paths, so the derivative has eight terms:
$$\frac{\partial\mathbf y}{\partial\mathbf f_1}=\mathbf I+\frac{\partial\mathbf f_2}{\partial\mathbf f_1}+\Big(\frac{\partial\mathbf f_3}{\partial\mathbf f_1}+\frac{\partial\mathbf f_2}{\partial\mathbf f_1}\frac{\partial\mathbf f_3}{\partial\mathbf f_2}\Big)+\Big(\frac{\partial\mathbf f_4}{\partial\mathbf f_1}+\frac{\partial\mathbf f_2}{\partial\mathbf f_1}\frac{\partial\mathbf f_4}{\partial\mathbf f_2}+\frac{\partial\mathbf f_3}{\partial\mathbf f_1}\frac{\partial\mathbf f_4}{\partial\mathbf f_3}+\frac{\partial\mathbf f_2}{\partial\mathbf f_1}\frac{\partial\mathbf f_3}{\partial\mathbf f_2}\frac{\partial\mathbf f_4}{\partial\mathbf f_3}\Big)\tag{11.6}$$
The identity term means layer-1 parameters affect $\mathbf{y}$ directly. They also act through chains of various lengths. The author's claim is that gradients through shorter paths will in general be better behaved. So networks with residual links suffer less from shattered gradients (p. 191).

*Intuition note:* Every layer now has a short route to the output. The gradient is therefore not only a long product that may change wildly. It also contains short-path terms, and gradients through shorter paths will in general be better behaved.

**11.2.1 Order of operations.** Blocks must contain a nonlinearity such as ReLU, or the whole network is linear. If the block ends with ReLU (linear → ReLU), each block can only add non-negative values. So it is typical to apply ReLU first, then the linear transformation; blocks with several layers usually end in a linear transformation (fig. 11.5b,c). A block that starts with ReLU does nothing for an all-negative input. So it is typical to start the network with a linear transformation rather than a residual block (p. 191).

**11.2.2.** Residual connections roughly double the depth that can be trained before performance degrades. They do not permit arbitrary depth, for the reasons in 11.3 (p. 192).

### 11.3 Exploding gradients in residual networks (p. 192)
He initialization sets biases $\beta=0$ and draws weights $\Omega$ normal with mean 0 and variance $2/D_h$, where $D_h$ is the number of hidden units in the previous layer. For ReLU it keeps the variance of activations and gradients the same across layers (p. 192).

In a residual net, values and gradients do not vanish, since each layer has a direct path to the output. But with He initialization the forward-pass values still grow exponentially:
- The branch output has (uncorrelated) variability.
- Under ReLU and He initialization, a block's processing leaves the expected variance unchanged.
- Adding it to the input therefore doubles the variance (fig. 11.6a), which is exponential growth in the number of blocks.

A similar argument applies to backward-pass gradients (p. 192). One fix is to multiply each block's combined output by $1/\sqrt2$ (fig. 11.6b). The usual fix is batch normalization (p. 192).

### 11.4 Batch normalization (pp. 193–194)
For each hidden unit $h$, over batch $\mathcal B$:
$$m_h=\frac1{|\mathcal B|}\sum_{i\in\mathcal B}h_i,\qquad s_h=\sqrt{\frac1{|\mathcal B|}\sum_{i\in\mathcal B}(h_i-m_h)^2}\tag{11.7}$$
$$h_i\leftarrow\frac{h_i-m_h}{s_h+\epsilon}\quad\forall i\in\mathcal B\tag{11.8}$$
$$h_i\leftarrow\gamma h_i+\delta\quad\forall i\in\mathcal B\tag{11.9}$$
Here $\epsilon$ is a small number that avoids division by zero when $s_h=0$ (p. 193). Afterwards the activations have mean $\delta$ and standard deviation $\gamma$ over the batch, and both are learned (p. 194).

Counting parameters:
- It is applied independently per hidden unit. A net with $K$ layers of $D$ units has $KD$ offsets and $KD$ scales.
- In a convolutional net, statistics are taken over batch and spatial positions. With $K$ layers of $C$ channels there are $KC$ offsets and $KC$ scales.
- At test time, $m_h$ and $s_h$ are computed over the whole training set and frozen (p. 194).

**11.4.1 Costs and benefits.**
- *Cost:* the network becomes invariant to rescaling the weights and biases feeding a unit, so many weight settings give the same function. $\gamma,\delta$ add parameters. This is inefficient. Footnote 2 says the invariance is strictly true only when BatchNorm directly follows the layer (p. 194).
- *Stable forward propagation:* with $\delta=0,\gamma=1$, each unit's output has unit variance. In a residual net the variance still grows, but linearly. The $k$th block adds one unit of variance to the existing $k$ (fig. 11.6c). Later layers therefore change the signal less than earlier ones at the start. The network is "effectively less deep" initially and can raise $\gamma$ in later layers to control its own effective depth (p. 194).
- *Higher learning rates:* empirical studies and theory both show that BatchNorm makes the loss surface and its gradient change more smoothly, which allows higher learning rates (p. 194).
- *Regularization:* the normalization depends on the other members of the batch. This injects noise, and noise can improve generalization (p. 194).

*Intuition note:* With He initialization and ReLU, and without BatchNorm, each block adds a branch with the same variance as its input, so the variance doubles. With BatchNorm at the start of each branch (and $\gamma=1,\delta=0$), each branch contributes variance one at initialization. Variance then grows by a fixed amount per block instead of being multiplied.

### 11.5 Common residual architectures (pp. 195–198)
**11.5.1 ResNet.** Each block holds BN → ReLU → 3×3 convolution, repeated twice, then added to the input (fig. 11.7a). The order was found by trial and error to work well. *Bottleneck blocks* save parameters with three convolutions: 1×1 to reduce channels, 3×3, and 1×1 to restore channels (fig. 11.7b) (p. 195).

ResNet-200 (ImageNet, fig. 11.8):
- A 7×7 convolution with stride 2 and a downsample step come first.
- Bottleneck blocks follow, with periodic stride-2 downsampling. Channels increase by appending zeros or by an extra 1×1 convolution.
- A fully connected layer maps to 1000 classes, followed by softmax (p. 195).

| Model | Top-5 error | Top-1 error |
|---|---|---|
| ResNet-200 | 4.8% | 20.1% |
| AlexNet | 16.4% | 38.1% |
| VGG | 6.8% | 23.7% |

Human top-five error is given as 5.1%. The model dates from 2016 and is far from state of the art. At the time of writing the best model has 9.0% top-one error, and the top models are now transformer-based (p. 195).

**11.5.2 DenseNet.** Instead of adding, it concatenates the processed and original signals, which grows the channel count. An optional 1×1 convolution can map back to the original size, letting the model sum, take a weighted sum, or combine the signals in a more complex way (p. 197). Each layer's input is the concatenation of *all* earlier outputs (fig. 11.9: 3 → 32+3=35 → 32+35=67 → 32+67=99 channels). The direct contribution of early layers means the loss surface behaves reasonably (p. 197).
- In practice it can only be sustained for a few layers because channels and parameters grow. A 1×1 convolution reduces channels first.
- Concatenation across downsampling makes no sense because spatial sizes differ, so the chain restarts there.
- It performs competitively with ResNet, and can do better at comparable parameter count. The author says this is presumably because it can reuse earlier processing more flexibly (p. 197).

**11.5.3 U-Nets and hourglass networks.** In an encoder–decoder (hourglass) segmentation net, the low-resolution middle must "remember" high-resolution detail. Passing encoder representations to their partner in the decoder removes this need (p. 198).
- *U-Net* (fig. 11.10) concatenates earlier representations to later ones. The original used "valid" convolutions, so representations shrink by two pixels per 3×3 layer and encoder maps must be cropped. Later versions use zero-padding. It is fully convolutional, so it can run on any image size after training (p. 198).
- It was designed for medical segmentation (fig. 11.11, 3D mouse cortex, ensemble of five U-Nets) but has many other uses (p. 198).
- *Hourglass networks* put further convolutions in the skip paths and add rather than concatenate. A stack of them alternates local and global views and is used for pose estimation (fig. 11.12). One heatmap per joint is predicted, and each estimate is the heatmap maximum (p. 198).

### 11.6 Why do nets with residual connections perform so well? (p. 199)
ResNets can be extended to 1000 layers and still train. The gain was initially attributed to depth, but two observations contradict this:
1. Shallower, wider residual networks sometimes beat deeper, narrower ones with similar parameter count.
2. There is evidence that gradients do not propagate effectively through very long paths of the unraveled network. A very deep network may act like a combination of shallower ones.

The current view is that residual connections add some value of their own. Support: loss surfaces near a minimum tend to be smoother than for the same net without skips (fig. 11.13). This may make it easier to find a solution that generalizes (p. 199).

### 11.7 Summary (pp. 199–201)
Excess depth hurts training and test performance, possibly because early-layer gradients change quickly relative to the step size. Residual nets do not suffer vanishing gradients but have exponential variance growth, usually handled by BatchNorm. There is evidence that both residual links and BatchNorm make the loss surface smoother, which permits larger learning rates (pp. 200–201).

### Notes (pp. 201–205, compressed)
- **History:** He et al. introduced residual connections with a 152-layer net. ResNet v1 had a ReLU after the addition. The 2016b study found extra processing along the skip path or after recombination unnecessary, giving the pre-activation block (v2, 200 layers) (pp. 201–202).
- **Why they help:** Residual links alone raise trainable depth about two-fold. With BatchNorm, it is unclear that depth is critical. A 16-layer wide residual net outperformed all residual nets of the time on image classification (Zagoruyko & Komodakis). Another proposal is eliminating loss-surface singularities (p. 202).
- **Ensemble view (Veit et al.):** deleting a layer from a trained residual net has a modest effect, but in VGG it is catastrophic. In a 54-block net, almost all gradient came from paths of 5–17 blocks, which are 0.45% of all paths (p. 202).
- **Related:** highway networks use data-dependent gating. ResNeXt puts a residual connection around parallel convolutional branches (p. 202).
- **Regularization:** methods such as stochastic depth drop whole residual blocks, which removes paths. Shake-shake re-weights branches randomly (pp. 202–203).
- **BatchNorm limits:** Yang et al. showed BatchNorm causes gradient explosion by a factor $\sqrt{\pi/(\pi-1)}\approx1.21$ per layer in ReLU nets without skips. The author presumes that removing the $2^K$ forward growth outweighs a $1.21^K$ backward growth (p. 203).
- **Variants** (fig. 11.14): GhostNorm uses part of the batch. LayerNorm normalizes each example over channels and positions. GroupNorm uses channel groups. InstanceNorm normalizes each channel separately. LayerNorm and GroupNorm still keep a separate learned scale and offset per channel (pp. 203–204).
- **Why BatchNorm helps:** the original "internal covariate shift" explanation was questioned. Evidence instead points to a smoother loss and gradient, which permits larger learning rates. The mechanism is "not well understood" (p. 204).
- **Alternatives:** Balduzzi et al. argued that the $1/\sqrt2$ rescaling prevents gradient explosion but does not resolve shattered gradients. SkipInit, Stable ResNet and FixUp rescale or zero-initialize branches. These usually do not match BatchNorm's test performance, probably because they lack its regularization (p. 205).
- **U-Net variants:** 3D U-Net, V-Net, and uses in medical segmentation and diffusion models (p. 205).

## Toy example (ours)
Setting: a residual stack where each branch preserves variance (He-initialized, ReLU) and is uncorrelated with its input. Start with input variance 1.
- **No BatchNorm:** the output variance is input variance + branch variance, and the branch variance equals the input variance.
  - Block 1: 1+1=2.
  - Block 2: 2+2=4.
  - Block 3: 4+4=8, so $2^k$ (fig. 11.6a).
- **BatchNorm first in each branch:** the branch always sees variance 1, so it adds 1.
  - Block 1: 1+1=2.
  - Block 2: 2+1=3.
  - Block 3: 3+1=4, so $k+1$ (fig. 11.6c).
- After 20 blocks: $2^{20}=1{,}048{,}576$ versus $21$.

BatchNorm arithmetic for a batch $\{1,3,5,7\}$ (ignoring $\epsilon$): $m_h=16/4=4$. Squared deviations are $9,1,1,9$, so the mean is $5$ and $s_h=\sqrt5\approx2.236$. Standardized values are $-3/2.236,\,-1/2.236,\,1/2.236,\,3/2.236\approx-1.342,\,-0.447,\,0.447,\,1.342$. With $\gamma=2,\delta=1$ the outputs are $\approx-1.683,\,0.106,\,1.894,\,3.683$. Their mean is 1 and their standard deviation is 2.

## Concepts
- [[residual-connection]] (new) — add a layer's input back to its output, $\mathbf h+\mathbf f[\mathbf h]$; the layer learns an additive change (p. 189)
- [[shattered-gradients]] (new) — in deep sequential nets, nearby inputs or parameters give unrelated gradients; a conjectured cause of poor training (p. 187)
- [[unraveled-network]] (new) — expanding a residual net into a sum of smaller networks, read as an ensemble; four blocks give sixteen paths (pp. 189–190)
- [[batch-normalization]] (new) — standardize each unit over the batch, then rescale with learned $\gamma,\delta$ (p. 193)
- [[he-initialization]] (new) — zero biases, weight variance $2/D_h$; keeps variance steady for ReLU (p. 192)
- [[bottleneck-block]] (new) — 1×1, 3×3, 1×1 convolutions to save parameters (p. 195)
- [[skip-concatenation]] (new) — DenseNet and U-Net variant: concatenate earlier representations instead of adding (p. 197)
- [[layer-normalization]] (new) — normalize per example over channels and positions (p. 203)

## Canonical instances
- [[resnet-200]] (new) — 200-layer bottleneck ResNet with 4.8% top-five error on ImageNet (p. 195)
- [[densenet]] (new) — concatenates all earlier layers' outputs (p. 197)
- [[u-net]] (new) — encoder–decoder with concatenating skips for segmentation (p. 198)
- [[stacked-hourglass]] (new) — additive-skip hourglass blocks for pose heatmaps (p. 198)
- [[variance-doubling]] (new) — residual-block variance doubling versus linear growth with BatchNorm (p. 193)

## Bridges (candidates)
- [structural-analogy] additive layer update $\mathbf h+\mathbf f[\mathbf h]$ ↔ llm: the residual stream that every Transformer layer reads from and writes to — the same additive pattern, but the unit never mentions Transformers' internals.
- [structural-analogy] LayerNorm (per-example statistics) ↔ llm: normalization inside Transformer layers — avoids batch statistics.
- [structural-analogy] unraveled residual net as many paths ↔ llm: circuit/path analysis in interpretability — both decompose output into paths through the graph.

## Questions this raises
- Why would residual networks have smoother loss surfaces, beyond the short-path argument?
- The unit says BatchNorm's mechanism is poorly understood. What is the best-supported explanation?
- If very deep nets behave like shallower ensembles, what do extra blocks actually buy?
- How does the additive pattern change when the layer is attention rather than convolution (chapter 12)?

## Exercises worth doing
- Ex. 11.1 (p. 205) — derive the unraveled form (11.5) from (11.4) — easy
- Ex. 11.2 (p. 205) — count paths of each length for $K$ blocks and deduce the rule — easy
- Ex. 11.4 (p. 206) — why branch values are uncorrelated; variance of a sum — medium
- Ex. 11.5 (p. 206) — implement BatchNorm forward and backward by hand — hard
- Ex. 11.6 (p. 206) — parameter count with and without BatchNorm — easy
- Ex. 11.8 (p. 206) — parameter count: plain versus bottleneck block — medium

## Reading notes
- Printed page = pdf − 14. The pages are a draft ("please send errata"), CC-BY-NC-ND.
- The prose of the text layer is mostly clean, but equation symbols are garbled in places (e.g. square roots in eq. 11.7 and in $1/\sqrt2$), so math was read from the images. Equations 11.3–11.9 and 11.10 were checked against the images. Square-root signs in the Notes (pp. 203, 205) are garbled in the text layer, so I used the image.
- The Fig. 11.2 caption says "56-layer neural network", while the text says convolutional networks.
- Fig. 11.9's caption stops at 67 channels; the figure continues to 99.
- Unit includes the end-of-chapter Notes and Problems, which were compressed. No solutions are printed on these pages.
