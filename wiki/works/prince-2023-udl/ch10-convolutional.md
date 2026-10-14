---
id: prince-2023-udl/ch10-convolutional
work: prince-2023-udl
unit: "Chapter 10 — Convolutional networks"
pages: 161-185
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Convolutional networks

## L0 — One line
A convolutional layer computes each hidden unit as the same weighted sum of nearby inputs at every position, which gives far fewer parameters and a useful translation-based inductive bias for images.

## L1 — The gist (≤ 120 words)
Fully connected networks are a poor fit for images. Images are high-dimensional, nearby pixels are related, and an image's meaning is stable under shifts. The chapter introduces convolutional layers: each unit is a weighted sum of nearby inputs, with the same weights at every position. This gives far fewer parameters, translation equivariance (a shifted input gives a shifted output) and a useful inductive bias (built-in prior knowledge). Downsampling (strides, pooling) shrinks the representation, upsampling restores resolution, and 1×1 convolutions change channel counts. The chapter then shows how these parts build networks for image classification, object detection and semantic segmentation. Depth helped classification, but very deep networks become hard to train, which motivates residual connections, the next chapter's topic.

**Prerequisites:** fully connected layers and activation functions (ReLU); weights and biases; SGD; softmax; matrix and tensor shapes; the idea of overfitting and of inductive bias.

## L2 — Key ideas
- Images are high-dimensional, have statistically related nearby pixels, and keep their meaning under shifts; fully connected networks have no notion of "nearby" and must relearn patterns at every position (p. 161).
- For a transformation $t$ (such as a shift), invariance means $f[t[x]] = f[x]$ (wanted for classification). Equivariance means $f[t[x]] = t[f[x]]$ (wanted for segmentation) (p. 162).
- A 1D convolution shares one small kernel across positions, so it is equivariant to translation. It is a special case of a fully connected layer with many zero and tied weights (pp. 163, 165).
- Stride (the step between kernel positions) sets how many outputs there are; kernel size and dilation (zeros spaced inside the kernel) set how wide a region each output covers (pp. 164–165). With many channels, a layer needs $C_i \times C_o \times K$ weights (1D) or $C_i \times C_o \times K \times K$ (2D) (pp. 165, 167, 170).
- Stacked layers enlarge the receptive field (the part of the input that feeds a unit). In MNIST-1D, the convolutional net (2,050 parameters) generalises better than a fully connected net (59,065 parameters). The author attributes this probably to inductive bias (pp. 167–170).
- Downsampling (sub-sampling, max pooling, mean pooling), upsampling (duplication, max unpooling, bilinear interpolation, transposed convolution) and 1×1 convolutions are the tools for resizing representations (pp. 171–174).
- AlexNet, VGG, YOLO and the Noh et al. segmentation network show the pieces combined. Classification error fell as depth grew, but indefinite depth stops helping, which motivates residual connections (pp. 174–180).

## L3 — Walkthrough

**Opening: why not fully connected? (p. 161)**
Three properties of images call for specialised architecture.
1. *High dimension.* A typical $224\times224$ RGB image has 150,528 input dimensions. Hidden layers in fully connected networks are generally larger than the input, so even a shallow network would have more than $150{,}528^2$ weights, about 22 billion.
2. *Nearby pixels are related.* A fully connected net has no notion of "nearby". If train and test pixels were permuted the same way, training would work equally well.
3. *Interpretation is stable under geometric transformations.* A shifted tree is still a tree, but the shift changes every input. A fully connected model must relearn "tree" at every position.

Convolutional layers process each local region independently with shared parameters. A network mostly made of them is a CNN.

**10.1 Invariance and equivariance (p. 162)**
$$f[t[x]] = f[x] \tag{10.1}$$
$f$ is *invariant* to $t$: the output ignores the transformation. Image classification should be invariant to translation, rotation, flipping and warping.
$$f[t[x]] = t[f[x]] \tag{10.2}$$
$f$ is *equivariant* (or covariant) to $t$: the output changes in the same way as the input. Per-pixel segmentation should be equivariant, so a translated image gives a translated segmentation (Fig. 10.1).

*Intuition note:* Invariant means "the answer does not move when the picture moves". Equivariant means "the answer moves with the picture". Labels for the whole image want the first; labels for each pixel want the second.

**10.2 Convolutional networks for 1D inputs (pp. 163–170)**
Convolutional layers are each equivariant to translation. Networks usually add pooling, which induces *partial* invariance (p. 163).

*10.2.1 The operation.* Each output is a weighted sum of nearby inputs, using the same weights (the *kernel* or *filter*) at every position. For kernel size three, with kernel $\boldsymbol\omega = [\omega_1,\omega_2,\omega_3]^T$:
$$z_i = \omega_1 x_{i-1} + \omega_2 x_i + \omega_3 x_{i+1} \tag{10.3}$$
Translating $x$ translates $z$ in the same way, so the operation is equivariant (p. 163). Footnote: strictly this is a cross-correlation, not a convolution (which would flip the weights). The author calls the machine-learning convention "incorrect" but usual (p. 163).

*10.2.2 Padding.* The first and last outputs lack a neighbour. Two options (p. 164):
- *Pad the edges.* Zero-padding assumes zeros outside the input. Other options are circular or reflected padding.
- *Valid convolution.* Discard output positions where the kernel leaves the input. This adds no edge information, but the representation shrinks.

*10.2.3 Stride, kernel size, dilation (pp. 164–165).*
- *Stride* is the shift between kernel evaluations. Stride one gives an output at every position. Stride two gives roughly half as many outputs.
- *Kernel size* is typically odd so the kernel can be centred. A larger kernel needs more weights.
- *Dilated (atrous) convolution* intersperses zeros among the kernel values. A size-five kernel becomes a dilated size-three kernel by zeroing its second and fourth elements, so three weights cover a wider region. Dilation rate = number of zeros interspersed plus one.

*10.2.4 Convolutional layer.* The layer convolves, adds a bias $\beta$, and applies activation $a[\cdot]$. For kernel size three, stride one, dilation one (zero-padding, $x$ is zero out of range):
$$h_i = a[\beta + \omega_1 x_{i-1} + \omega_2 x_i + \omega_3 x_{i+1}] = a\Big[\beta + \sum_{j=1}^{3}\omega_j x_{i+j-2}\Big] \tag{10.4}$$
A fully connected layer computes
$$h_i = a\Big[\beta_i + \sum_{j=1}^{D}\omega_{ij}x_j\Big] \tag{10.5}$$
With $D$ inputs and $D$ hidden units it has $D^2$ weights and $D$ biases. The convolutional layer uses three weights and one bias. A fully connected layer reproduces it exactly if most weights are zero and the others are constrained to be identical (Fig. 10.4) (p. 165).

*Intuition note:* A convolutional layer is a fully connected layer with a very restricted weight matrix: mostly zeros, and the same few numbers repeated along diagonals. Training searches only among those restricted layers.

*10.2.5 Channels.* One convolution alone will likely lose information (it averages neighbours and ReLU clips negatives). So several convolutions run in parallel; each produces a *feature map* or *channel* with its own kernel and bias (Fig. 10.5) (pp. 165–167). With $C_i$ input channels and kernel size $K$, each output channel is a weighted sum over all $C_i$ channels and $K$ positions, using $\boldsymbol\Omega \in \mathbb{R}^{C_i\times K}$ and one bias. For $C_o$ output channels the layer needs $\boldsymbol\Omega \in \mathbb{R}^{C_i\times C_o\times K}$ weights and $\boldsymbol\beta \in \mathbb{R}^{C_o}$ biases (p. 167).

*10.2.6 Receptive fields.* The receptive field of a hidden unit is the region of the original input that feeds into it (p. 167).
- With kernel size three in every layer, first-layer units have receptive field three and second-layer units have five.
- Fig. 10.6: a third layer with kernel three and stride two gives seven. By the fourth layer, units at position three cover the whole input (p. 168).

*10.2.7 Example: MNIST-1D (pp. 167–170).*
- *Network (Fig. 10.7, p. 169).* Input $x\in\mathbb{R}^{40}$. Three conv layers, each with kernel 3, stride 2, "valid" padding, 15 channels. Shapes: $H_1 \in \mathbb{R}^{19\times15}$, $H_2\in\mathbb{R}^{9\times15}$, $H_3\in\mathbb{R}^{4\times15}$, then reshaped to 60 values and passed through a fully connected layer $\Omega_3\in\mathbb{R}^{10\times60}$. Output $f\in\mathbb{R}^{10}$, followed by softmax. The conv weights are $\Omega_0\in\mathbb{R}^{1\times15\times3}$, $\Omega_1,\Omega_2\in\mathbb{R}^{15\times15\times3}$, with $\beta\in\mathbb{R}^{15}$ for each of the three conv layers (p. 169).
- *Training (p. 167).* 100,000 SGD steps without momentum, learning rate 0.01, batch size 100, 4,000 examples.
- *Comparison (pp. 167, 170).* The fully connected net has hidden layers of 285, 135 and 60 units. It has 59,065 parameters; the CNN has 2,050. The CNN is a special case of the fully connected net, which could replicate it exactly.
- *Result (Fig. 10.8, p. 169).* Both fit the training data perfectly. Test error is about 17% for the CNN and about 40% for the fully connected net.
- *Explanation (author's hedged view, p. 170).* This is probably not due to parameter count, since overparameterisation usually helps (section 8.4.1). The likely explanation is a superior inductive bias: the architecture forces each position to be processed the same way, which the author calls sensible because the data were made from a template that is (among other operations) randomly translated. The fully connected net must learn each digit template at every position. Another way to see it: the CNN searches a smaller family of plausible mappings. Alternatively, it can be seen as a regulariser with an infinite penalty on most mappings a fully connected net can express.

*Intuition note:* Both models can fit the training set, but they differ in which functions they prefer. The author's likely explanation is that the CNN's built-in "same everywhere" rule matches how the data were made, so it probably guesses better on new examples.

**10.3 Convolutional networks for 2D inputs (p. 170)**
A $3\times3$ kernel $\boldsymbol\Omega\in\mathbb{R}^{3\times3}$ on 2D input $x_{ij}$:
$$h_{ij} = a\Big[\beta + \sum_{m=1}^{3}\sum_{n=1}^{3}\omega_{mn}\,x_{i+m-2,\,j+n-2}\Big] \tag{10.6}$$
The kernel slides horizontally and vertically (Fig. 10.9, p. 171). An RGB image is a 2D signal with three channels. A $3\times3$ kernel has $3\times3\times3$ weights and, with zero-padding, gives an output of the image's height and width (Fig. 10.10, p. 172). Several kernels give several output channels, stacked into a 3D tensor. For a $K\times K$ kernel with $C_i$ input channels, each output channel sums $C_i\times K\times K$ quantities plus one bias. So $C_o$ output channels need $C_i\times C_o\times K\times K$ weights and $C_o$ biases (p. 170).

**10.4 Downsampling and upsampling (pp. 171–174)**
Fig. 10.7 grew receptive fields by stride-two convolutions. This section covers shrinking representations, restoring size (useful when the output is an image) and changing channel counts (useful when recombining branches, chapter 11) (p. 171).

*10.4.1 Downsampling* (both dimensions by a factor of two; Fig. 10.11) (pp. 171–173):
- *Sub-sampling:* keep every other position. A stride of two does this together with the convolution.
- *Max pooling:* keep the maximum of each $2\times2$ block. This induces some invariance to translation, since after a one-pixel shift many maxima stay the same.
- *Mean (average) pooling:* average each block.

Each channel is downsampled separately, so the channel count is unchanged (p. 172).

*10.4.2 Upsampling* (Figs. 10.12–10.13) (pp. 172–174):
- *Duplicate* each value four times.
- *Max unpooling:* put values back at the positions of the earlier maxima.
- *Bilinear interpolation* between sampled values.
- *Transposed convolution:* the reverse of strided downsampling. There are twice as many outputs as inputs, and each input contributes to three outputs. Its weight matrix is the transpose of the downsampling matrix (Fig. 10.13b, d).

*10.4.3 Changing channels (p. 174).* A convolution with kernel size one takes a weighted sum of all channels at the same position. Weights have size $1\times1\times C_i\times C_o$, hence "1×1 convolution". With bias and activation, it equals running the same fully connected network on the channels at every position.

**10.5 Applications (pp. 174–180)**

*10.5.1 Image classification (pp. 174–176).*
- *ImageNet.* 1,281,167 training, 50,000 validation and 100,000 test images, each in one of 1000 classes (p. 174). A typical input is $224\times224$ RGB; the output is a distribution over 1000 classes.
- *Error history.* In 2011, before deep networks, the best method had about 25% top-five error. Five years later, the best deep models eclipsed human performance (p. 174).
- *AlexNet (2012; Fig. 10.16, p. 176).* Eight hidden layers with ReLU: five convolutional, three fully connected. Pipeline:
  - $11\times11$ kernels, stride 4 → 96 channels
  - max pool
  - $5\times5$ conv → 256 channels
  - max pool
  - three $3\times3$ convs → $13\times13\times256$
  - max pool → $6\times6\times256$, flattened to 9,216
  - FC 4096, 4096, 1000 → softmax

  It has about 60 million parameters, most in the fully connected layers.
- *AlexNet training.* Data augmented by a factor of 2048 (spatial transformations and intensity changes). Test time: predictions averaged over five cropped and mirrored versions. SGD with momentum 0.9, batch 128, dropout in the fully connected layers, L2 regularisation. Result: 16.4% top-5 and 38.1% top-1 error. The author says this revealed the potential of deep learning and "kick-started the modern era of AI research" (p. 176).
- *VGG (Fig. 10.17, p. 177).* Interspersed conv and max-pool layers; spatial size falls and channels rise; then three fully connected layers. It reached 6.8% top-5 and 23.7% top-1 error, using 19 hidden layers and 144 million parameters. The author calls depth the most important change from AlexNet, and the multi-year trend of better performance with depth "evidence that depth is important" (p. 176).

*10.5.2 Object detection (pp. 177–178).* YOLO ("You Only Look Once") takes a $448\times448$ RGB image through 24 conv layers, shrunk by max pooling with channels increasing as in VGG. The final conv layer is $7\times7$ with 1024 channels. A fully connected layer maps it to 4096 values, and one more fully connected layer gives the output.
- *Output.* Class information for each location of a $7\times7$ grid, plus a fixed number of bounding boxes per location (two per cell in Fig. 10.18, p. 178). Each box has five parameters: centre x and y, height, width and confidence. Confidence estimates the overlap with the ground-truth box.
- *Training.* Momentum, weight decay, dropout, augmentation, and transfer learning (first trained on ImageNet classification, then fine-tuned).
- *Inference.* A heuristic removes low-confidence boxes and suppresses boxes for the same object, keeping the most confident (p. 177).

*10.5.3 Semantic segmentation (pp. 178–180).* The network of Noh et al. maps a $224\times224$ RGB image to a $224\times224\times21$ array of probabilities for 21 classes (Fig. 10.19).
- *Encoder.* A smaller VGG with 13 rather than 16 conv layers, down to $14\times14$. Then one more max pool and two fully connected layers to 4096-vectors. These layers combine information across the whole image.
- *Decoder.* A fully connected layer reshapes to $7\times7\times512$. Then max unpooling and deconvolution layers (2D transposed convolutions without the upsampling), then a $1\times1$ convolution to 21 channels, and softmax at each position.
- *Names.* Downsampling side = encoder, upsampling side = decoder; such nets are "encoder-decoder" or "hourglass" networks.
- *Final labelling.* A greedy heuristic picks the most represented class and infers its region, using probabilities and encouraging connectedness. It then adds the next class where it dominates the remaining pixels, until evidence runs out (p. 179; Fig. 10.20, p. 180).

**10.6 Summary (pp. 179–180)**
- Weights and bias are shared across positions, so there are far fewer parameters than in a fully connected net. The parameter count does not grow with image size.
- Many channels keep information.
- Typical networks interleave convolutions with factor-two downsampling. Spatial size usually halves while channels double. Fully connected layers at the end integrate the whole input. If the output is an image, a mirrored decoder upsamples.
- Translation equivariance is a useful inductive bias that improves image tasks relative to fully connected nets.
- Classification improved with depth, but subsequent experiments showed that increasing depth indefinitely stops helping and the system becomes difficult to train. This motivates residual connections (chapter 11).

**Notes (pp. 180–184), reported as the author's survey**
- *History.* Early CNNs: Fukushima & Miyake (1982), LeCun et al. (1989a, b). LeNet (LeCun et al., 1998) classified $28\times28$ grayscale digits using conv then fully connected layers, sigmoids and average pooling. AlexNet is "widely considered" the start of modern deep CNNs (p. 181).
- *ImageNet winners.* Network-in-network alternated convolutions with 1×1 layers. GoogLeNet introduced inception blocks, with parallel paths of different filter sizes that effectively let the system learn the filter size. Deeper nets became hard to train without residual connections and normalisation (p. 181).
- *Layer variants.*
  - Dilated convolutions: Chen et al. (2018c), Yu & Koltun (2015).
  - Transposed convolutions: Long et al. (2015). Odena et al. (2016) noted they can cause checkerboard artifacts and need caution.
  - Depthwise convolution uses $K\times K\times C$ parameters instead of $K\times K\times C\times C$.
  - Grouped convolutions apply each kernel to a subset of channels; AlexNet used them to split work over two GPUs.
  - Separable convolutions treat each kernel as an outer product of 1D vectors (printed: $C+K+K$ parameters for each of the $C$ channels).
  - Partial and gated convolutions handle masked inputs; squeeze-and-excitation re-weights channels (p. 181).
- *Pooling.* Scherer et al. (2010) compared average and max pooling and concluded max was superior. Max pooling can be seen as an $L_\infty$ norm; other $L_k$ norms cost more and are not widely used. Zhang (2019) introduced max-blur-pooling (low-pass filter before downsampling to prevent aliasing), which improves generalisation over translation and protects against adversarial attacks. PixelShuffle (Shi et al., 2016) scales up with fractional stride (pp. 181–182).
- *Other data.* CNNs are also used on 1D data (speech, sentence classification, electrocardiograms, fault diagnosis) and 3D data (video, volumes) (p. 182).
- *Equivariance.* Part of the motivation for convolutional layers is that they are *approximately* equivariant to translation, and part of the motivation for max pooling is to induce invariance to small translations (p. 182); the chapter body (p. 163) calls the operation equivariant. Zhang (2019) examines how far this holds. Other work targets rotation, scale and reflection (group CNNs, polar transformer networks, harmonic networks) (pp. 182–183).
- *Initialisation and regularisation.* Xavier or He initialisation is typical. The ConvolutionOrthogonal initialiser lets networks of up to 10,000 layers train without residual connections. Dropout is less effective for conv layers, possibly because neighbouring pixels carry the same information. Alternatives are spatial dropout and cutout (p. 183).
- *Adaptive kernels.* Inception blocks, learned scales, kernel size changed adaptively based on the data, guided convolution, and learned offsets (p. 183).
- *Detection and segmentation.* Proposal-based detectors (R-CNN and successors) use two stages. Proposal-free ones, with YOLO the most celebrated, use a single pass. Many later segmentation methods vary U-Net (section 11.5.3) (pp. 183–184).
- *Visualisation.* Methods: gradient ascent on the input, reconstruction through hidden units, network inversion, network dissection. Bau et al. (2017) showed that earlier layers correlate more with texture and color and later layers with object type. The author says fully understanding networks with millions of parameters is currently not possible (p. 184).

## Toy example (ours, not from the text)
Take a 1D input of length 6, kernel $\boldsymbol\omega=[1,2,3]$, zero-padding, using $z_i=\omega_1x_{i-1}+\omega_2x_i+\omega_3x_{i+1}$. We omit bias and activation.

*Input* $x=[0,2,1,0,0,0]$ (taking $x_0=x_7=0$):
- $z_1 = 1\cdot0+2\cdot0+3\cdot2=6$
- $z_2 = 1\cdot0+2\cdot2+3\cdot1=7$
- $z_3 = 1\cdot2+2\cdot1+3\cdot0=4$
- $z_4 = 1\cdot1+2\cdot0+3\cdot0=1$
- $z_5=0$, $z_6=0$

So $z=[6,7,4,1,0,0]$.

*Shifted input* $x'=[0,0,2,1,0,0]$ (shifted right by one):
- $z'_1=0$
- $z'_2=1\cdot0+2\cdot0+3\cdot2=6$
- $z'_3=1\cdot0+2\cdot2+3\cdot1=7$
- $z'_4=1\cdot2+2\cdot1+3\cdot0=4$
- $z'_5=1\cdot1=1$
- $z'_6=0$

So $z'=[0,6,7,4,1,0]$, which is $z$ shifted right by one. This is equivariance.

*Max pooling over pairs:*
- $z\to[\max(6,7),\max(4,1),\max(0,0)]=[7,4,0]$
- $z'\to[\max(0,6),\max(7,4),\max(1,0)]=[6,7,1]$

The pooled outputs differ, so pooling gives only *partial* invariance.

*Parameters:* a fully connected layer on 6 inputs and 6 outputs has $6\times6=36$ weights; this convolutional layer has 3 weights (plus one bias).

*(added step)* MNIST-1D parameter count from Fig. 10.7 shapes: $45+15+675+15+675+15+600+10=2050$, matching the stated 2,050.

## Concepts
- [[convolutional-layer]] (new) — hidden unit = shared-weight sum of nearby inputs + bias, then activation (p. 165)
- [[kernel-stride-dilation]] (new) — kernel size, step between evaluations, and zero-spaced kernel entries (pp. 163–165)
- [[invariance-equivariance]] (new) — $f[t[x]]=f[x]$ versus $f[t[x]]=t[f[x]]$ (p. 162)
- [[channel-feature-map]] (new) — one set of hidden units from one kernel; layers hold many (p. 165)
- [[receptive-field]] (new) — the region of the original input feeding a hidden unit (p. 167)
- [[inductive-bias]] (new) — prior knowledge built into architecture; here, same processing at every position (p. 170)
- [[pooling-downsampling]] (new) — sub-sampling, max pooling or mean pooling to halve spatial size per channel (p. 172)
- [[transposed-convolution]] (new) — upsampling whose weight matrix is the transpose of strided downsampling (p. 174)
- [[1x1-convolution]] (new) — kernel size one; the same fully connected map on channels at each position (p. 174)
- [[encoder-decoder-network]] (new) — downsampling side then mirrored upsampling side, "hourglass" (p. 179)
- softmax — final map from activations to class probabilities (pp. 167, 176)
- pretraining / fine-tuning — YOLO is trained on ImageNet, then fine-tuned for detection (p. 177)

## Canonical instances
- [[mnist-1d-cnn-vs-fc]] — CNN (2,050 parameters, ~17% test error) beats a fully connected net (59,065, ~40%) (pp. 167–170)
- [[alexnet]] — 8 layers, ~60M parameters, 16.4% top-5 error (p. 176)
- [[vgg-network]] — 19 layers, 144M parameters, 6.8% top-5 error (p. 176)
- [[yolo-detector]] — $7\times7$ grid with boxes and confidences (p. 177)
- [[noh-segmentation-net]] — smaller-VGG encoder plus unpooling/deconvolution decoder, 21 classes (pp. 178–179)

## Bridges (candidates)
- [same-math] 1×1 convolution with activation (same fully connected map at every position) ↔ llm: the per-token feed-forward (MLP) block of a Transformer — both apply one shared network independently at each position.
- [structural-analogy] Weight sharing across positions (translation equivariance) ↔ llm: sharing Transformer layer weights across token positions, with order information supplied separately (positional encoding) — different symmetry, similar economy.
- [structural-analogy] Fully connected net "has no notion of nearby" (p. 161) ↔ llm: attention without positional encoding is order-blind.
- [metaphor] Encoder–decoder "hourglass" segmentation net ↔ llm: encoder-only versus decoder-only model families.

## Questions this raises
- The Notes call convolutional layers *approximately* equivariant (p. 182), while the chapter text calls them equivariant (p. 163); what breaks exact equivariance, and how do pooling choices affect it?
- Why does depth help up to a point and then make training hard (p. 180)? What do residual connections change?
- The author says the CNN's advantage is "probably" inductive bias (p. 170). How could one test this against other explanations?
- Can the same weight-sharing idea work for text (1D data, p. 182), and what inductive bias would it encode?

## Exercises worth doing
- Ex. 10.1 (p. 184) — prove eq. 10.3 is translation-equivariant — difficulty: easy
- Ex. 10.5 (p. 184) — draw weight matrices for strided, larger-kernel and dilated convolutions — difficulty: medium
- Ex. 10.9–10.11 (p. 185) — receptive field sizes with stride and dilation — difficulty: medium
- Ex. 10.12 (p. 185) — convert training steps to epochs for the MNIST-1D run — difficulty: easy
- Ex. 10.14 (p. 185) — count weights and biases of a $5\times5$ 2D conv layer — difficulty: easy
- Ex. 10.16 (p. 185) — parameter count of AlexNet layer by layer — difficulty: hard

## Reading notes
- Printed page = pdf − 14. Pages 175–199 cover printed 161–185; the unit includes the chapter notes and problems.
- No solutions to problems are printed in these pages.
- Text layer was clean; equations were checked against the page images (e.g., 10.4, 10.5, 10.6).
- The Notes give separable convolutions as "$C+K+K$ parameters for each of the $C$ channels" (p. 181); I report it as printed without checking it.
- Footnote p. 163: the author flags "convolution" as technically cross-correlation.
- Fig. 10.18 caption says two bounding boxes per cell; the main text says only "a fixed number" (pp. 177–178).
- Running footers show "Draft: please send errata…" and a CC-BY-NC-ND license line; it is a draft edition.
