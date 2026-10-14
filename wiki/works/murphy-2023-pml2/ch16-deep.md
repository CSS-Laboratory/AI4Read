---
id: murphy-2023-pml2/ch16-deep
work: murphy-2023-pml2
unit: "16 Deep neural networks"
pages: 631-646
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Deep neural networks (Murphy, PML2, Ch. 16)

## L0 — One line
A deep neural network is any differentiable function written as a computation graph of simple blocks (linear, convolutional, attention, recurrent and others), and it can be used either inside probabilistic models or to approximate their posteriors.

## L1 — The gist (≤ 120 words)
The chapter asks what a "deep neural network" is made of and which standard architectures exist. Murphy describes a DNN as any differentiable function that can be expressed as a computation graph. He lists the building blocks: linear layers, nonlinearities, convolution, residual connections, normalization, dropout, attention, recurrent, multiplicative and implicit layers. He then assembles them into MLPs, CNNs, autoencoders, RNNs and transformers. This matters for Bayesian work because DNNs enter probabilistic models in two ways: as nonlinear functions inside conditional distributions, or as inference networks that approximate a posterior. The chapter mainly describes components and architectures; for theory it points to other references.

**Prerequisites:** matrix–vector products and tensor shapes; softmax; Bernoulli variables and expectation; basic idea of gradients and loss minimisation.

## L2 — Key ideas (5–10 bullets)
- A DNN is any differentiable function expressible as a computation graph. Fitting it by gradient-based optimisation of a scalar loss is "deep learning" (p. 631).
- DNNs combine with probabilistic models in two ways: as nonlinear functions inside conditional distributions (e.g. $p(y|x,\theta)=\mathrm{Cat}(y|\mathrm{softmax}(f(x;\theta)))$), or as inference networks (DNNs that map observed data to an approximate posterior over hidden variables) (p. 631).
- A stack of linear layers equals one linear layer, so each layer is passed pointwise through a nonlinear *activation function* to get more expressive power (pp. 632–633).
- Convolution shares kernel weights across positions, giving shift equivariance (a shifted input pattern gives a shifted output). Pooling (max or average over each patch) can add shift invariance (the same output wherever the pattern occurs) (p. 634).
- Residual (skip) connections let the signal bypass layers, normalization layers standardise activations, and dropout randomly drops units; these address signal/gradient scaling and overfitting. Dropout can be read as training an ensemble (pp. 635–636).
- Attention makes the weights depend on the input: $\mathbf Z=\mathrm{softmax}(\mathbf{QK}^\top/\sqrt{d_k})\mathbf V$. Multi-head attention and self-attention lead to the transformer (pp. 637–639).
- Multiplicative layers (bilinear forms; hypernetworks, i.e. networks that generate another network's parameters; gating; FiLM, i.e. a per-channel scale and bias computed from a second input) are useful for combining different information sources. Implicit layers define the output indirectly, as the solution of a constrained optimisation problem (pp. 640–641).
- Canonical architectures: MLP, CNN, autoencoder, RNN, transformer, GNN. Why large transformers work so well is "still not very clear" (pp. 641–646).

## L3 — Walkthrough

### 16.1 Introduction (p. 631)
- A **DNN** is any differentiable function expressible as a **computation graph**: nodes are primitive operations (e.g. matrix multiplication), edges carry vectors, matrices or tensors. The simplest graph is a linear chain of "layers"; "deep" means many layers (p. 631).
- Sections 16.2 (blocks) and 16.3 (architectures) follow. Gradients of such graphs come from Section 6.2 and feed an optimiser from Chapter 6 (p. 631).
- **Way 1:** use DNNs inside conditional distributions, e.g. $p(y|\boldsymbol x,\boldsymbol\theta)=\mathrm{Cat}(y|\mathrm{softmax}(f(\boldsymbol x;\boldsymbol\theta)))$ with logits $f$. Or use a directed graphical model in which each CPD $p(x_i|\mathrm{pa}(x_i))$ is a DNN (p. 631).
- **Way 2:** use a DNN to approximate the posterior, learning $f$ so that $q(\boldsymbol z|f(\mathcal D;\boldsymbol\phi))$ approximates it. Here $\boldsymbol z$ are latents and/or parameters, $\mathcal D$ is the data, and $f$ is an *inference network*. The joint $p(\boldsymbol z,\mathcal D)$ may be traditional, e.g. a simulator. In this setting the DNN serves computational, not statistical/modelling, purposes. This is sometimes called *deep Bayesian learning*, as opposed to *Bayesian deep learning* (Chapter 17) (p. 631).

### 16.2 Building blocks (inputs $\boldsymbol x$, outputs $\boldsymbol y$)

**16.2.1 Linear layers (p. 632).** A neuron computes
$$y=f(\boldsymbol x;\boldsymbol\theta)=\boldsymbol w^\top\boldsymbol x+b\tag{16.1}$$
with $\boldsymbol\theta=(\boldsymbol w,b)$. A layer of $D$ units is
$$\boldsymbol y=f(\boldsymbol x;\boldsymbol\theta)=\mathbf W\boldsymbol x+\boldsymbol b\tag{16.2}$$
It is called a linear or fully connected layer. The bias can be absorbed: $\tilde{\mathbf W}=[\mathbf W,\boldsymbol b]$, $\tilde{\boldsymbol x}=[\boldsymbol x,1]$ (p. 632).

**16.2.2 Nonlinearities (pp. 632–633).** A stack of linear layers equals one linear layer (the product of the weight matrices). So each layer is passed pointwise through an *activation function*:
$$\boldsymbol y=\varphi(\boldsymbol x)=[\varphi(x_1),\dots,\varphi(x_D)]\tag{16.3}$$
Table 16.1 (p. 633) lists:

| Name | Definition | Range |
|---|---|---|
| sigmoid | $\sigma(a)=1/(1+e^{-a})$ | [0,1] |
| tanh | $2\sigma(2a)-1$ | [−1,1] |
| softplus | $\log(1+e^a)$ | [0,∞] |
| ReLU | $\max(a,0)$ | [0,∞] |
| leaky ReLU | $\max(a,0)+\alpha\min(a,0)$ | [−∞,∞] |
| ELU | $\max(a,0)+\min(\alpha(e^a-1),0)$ | [−∞,∞] |
| Swish | $a\sigma(a)$ | [−∞,∞] |
| GELU | $a\Phi(a)$ | [−∞,∞] |
| sine | $\sin(a)$ | [−1,1] |

**16.2.3 Convolutional layers (pp. 633–635).**
- Idea: apply the same small weight matrix (kernel/filter) to each local patch of an image, which reduces parameters. For $\mathbf X\in\mathbb R^{H\times W}$ and kernel $\mathbf W\in\mathbb R^{h\times w}$ (ignoring boundaries):
$$Z_{i,j}=\sum_{u=0}^{h-1}\sum_{v=0}^{w-1}x_{i+u,j+v}\,w_{u,v}\tag{16.4}$$
- Strictly this is cross-correlation, but deep learning uses the terms interchangeably (footnote, p. 634). The output measures how similar the local patch is to the filter. Outputs may shrink at the boundaries, which *padding* avoids (p. 634).
- With $C$ input channels and $D$ output channels there are $D$ kernels of size $h\times w\times C$:
$$z_{i,j,d}=\sum_{u=0}^{h-1}\sum_{v=0}^{w-1}\sum_{c=0}^{C-1}x_{i+u,j+v,c}\,w_{u,v,c,d}\tag{16.5}$$
- Figure 16.3 shows 3 input and 2 output channels, $3\times3$ kernels, stride 1 and no padding. The $6\times6\times3$ input becomes $4\times4\times2$ (p. 634).
- Because kernel weights are shared across locations, a shifted input pattern gives a shifted output: *shift equivariance*. *Shift invariance* (same output wherever the pattern occurs) can be obtained with a *pooling layer*, which takes the max or average in each patch and has no learnable parameters (pp. 634–635).

*Intuition note:* A convolution is one small pattern detector slid over every position. Sharing the detector saves parameters, and a moved pattern moves the response.

**16.2.4 Residual connections (p. 635).** Stacking many nonlinear layers can squash the signal to zero or blow it up, and gradients can suffer similarly. A skip connection lets the signal bypass layers, e.g.
$$\boldsymbol y=f(\boldsymbol x;\mathbf W)=\varphi(\mathrm{conv}(\boldsymbol x;\mathbf W))+\boldsymbol x\tag{16.6}$$
The layer then only needs to learn a residual (offset) to add to or subtract from the input. Residuals are often small, hence easier to learn with bounded weights (e.g. close to 1) (p. 635).

**16.2.5 Normalization layers (pp. 635–636).**
- It is often best for inputs to be standardised (zero mean, unit standard deviation), which keeps weight magnitudes small and comparable. Normalization layers aim to give internal activations this property (p. 635).
- Batch normalization needs a batch $B>1$. Alternatives are layer, instance, group and filter-response normalization (p. 635).
- Layer norm (common in transformers) is $\boldsymbol y=(\boldsymbol x-\mathbb E[\boldsymbol x])/\sqrt{\mathbb V[\boldsymbol x]}$, followed by a scale and a bias. The author interprets it as projection onto a sphere, with $\mathbf 1=(1,\dots,1)$, $d$ the dimension, and $\Pi_{\mathbf 1}$ the projection that subtracts the mean (pp. 635–636):
$$\Pi_{\mathbf 1}(\boldsymbol x)=\boldsymbol x-\langle\boldsymbol x,\mathbf 1\rangle\mathbf 1/\|\mathbf 1\|^2=\boldsymbol x-\tfrac1d\textstyle\sum_i x_i\,\mathbf 1=\big[(x_j-\tfrac1d\sum_i x_i)\big]_{j=1}^d$$
$$\sqrt{\mathbb V[\boldsymbol x]}=\sqrt{\mathbb E[(\boldsymbol x-\mathbb E[\boldsymbol x])^2]}=\sqrt{\tfrac1d\textstyle\sum_i\Pi_{\mathbf 1}(\boldsymbol x)_i^2}=\sqrt{\tfrac1d}\,\|\Pi_{\mathbf 1}(\boldsymbol x)\|$$
$$\mathrm{LayerNorm}(\boldsymbol x)=\sqrt d\,\frac{\Pi_{\mathbf 1}(\boldsymbol x)}{\|\Pi_{\mathbf 1}(\boldsymbol x)\|}=\sqrt d\,\Pi_S(\Pi_{\mathbf 1}(\boldsymbol x))$$
where $\Pi_S$ is projection onto the unit sphere (p. 636).
- The author's stated consequences: activations don't saturate, and inner products become proportional to Euclidean distances, useful for attention (p. 636).

*Intuition note:* Layer norm subtracts the mean of the vector's entries and rescales the result to a fixed length. All vectors then differ only in direction, so comparing them by dot product is like comparing distances.

**16.2.6 Dropout (pp. 636–637).**
- Networks with millions of parameters can overfit, especially on small data. Remedies include weight regularizers and a fully Bayesian approach (Chapter 17). Dropout is "another common heuristic" (p. 636).
- Each weight is replaced by $\theta_{lij}=w_{lij}\epsilon_{li}$ with $\epsilon_{li}\sim\mathrm{Ber}(1-p)$. Here $p$ is the drop probability and $1-p$ the keep probability. If $\epsilon_{li}=0$, all weights leaving unit $i$ are zeroed (p. 636).
- Gradients are zero for weights of switched-off neurons. Since $\epsilon$ is resampled at each use, different weights are updated each step, giving an *ensemble* of sparse networks (p. 636).
- At test time dropout is usually turned off. To keep the expected input activation the same, use $\mathbb E[\theta_{lij}]=w_{lij}\mathbb E[\epsilon_{li}]$. For Bernoulli noise $\mathbb E[\epsilon]=1-p$, so multiply the weights by $1-p$ (pp. 636–637).
- Dropout can be kept on at test time ("Monte Carlo dropout", Section 17.3.1) (p. 637).

**16.2.7 Attention layers (pp. 637–639).**
- Earlier layers compute $\mathbf Z=\varphi(\mathbf{XW})$ with fixed learned weights, $\mathbf X\in\mathbb R^{n\times d}$, $\mathbf W\in\mathbb R^{d\times d_v}$. Attention makes the weights input-dependent, $\mathbf Z=\varphi(\mathbf X\mathbf W(\mathbf X))$: a *multiplicative interaction* (p. 637).
- Analogy with kernel methods (e.g. GPs): compare a query $\boldsymbol x$ to training inputs by a kernel, $\boldsymbol\alpha=[\mathcal K(\boldsymbol x,\boldsymbol x_i)]_{i=1}^n$, then
$$\hat{\boldsymbol y}=\sum_{i=1}^n\alpha_i\boldsymbol y_i\tag{16.7}$$
(pp. 637–638).
- Differentiable parametric version (p. 638): keys $\mathbf K=\mathbf X\mathbf W_k\in\mathbb R^{n\times d_k}$, values $\mathbf V=\mathbf Y\mathbf W_v\in\mathbb R^{n\times d_v}$, query $\boldsymbol q=\mathbf W_q\boldsymbol x\in\mathbb R^{d_k}$. The three embedding matrices are learned.
$$\mathrm{Attn}(\boldsymbol q,(\boldsymbol k_{1:n},\boldsymbol v_{1:n}))=\sum_{i=1}^n\alpha_i(\boldsymbol q,\boldsymbol k_{1:n})\boldsymbol v_i\tag{16.8}$$
with $0\le\alpha_i\le1$ and $\sum_i\alpha_i=1$.
- Scaled dot-product score, and softmax weights:
$$a(\boldsymbol q,\boldsymbol k)=\boldsymbol q^\top\boldsymbol k/\sqrt{d_k}\tag{16.9}$$
$$\alpha_i(\boldsymbol q,\boldsymbol k_{1:n})=\frac{\exp(a(\boldsymbol q,\boldsymbol k_i))}{\sum_{j=1}^n\exp(a(\boldsymbol q,\boldsymbol k_j))}\tag{16.10}$$
The $\sqrt{d_k}$ scaling reduces the dependence of the output on dimensionality (p. 638).
- *Masked attention:* to ignore some entries (e.g. padding), set their scores to a large negative number such as $-10^6$, so their softmax weights are 0 (p. 638).
- Parallel form, with $\mathbf Q,\mathbf K\in\mathbb R^{n\times d_k}$, $\mathbf V\in\mathbb R^{n\times d_v}$, and $\boldsymbol z_j=\sum_i\alpha_i(\boldsymbol q_j,\mathbf K)\boldsymbol v_i$ (16.11):
$$\mathbf Z=\mathrm{Attn}(\mathbf Q,\mathbf K,\mathbf V)=\mathrm{softmax}\!\Big(\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_k}}\Big)\mathbf V\in\mathbb R^{n\times d_v}\tag{16.12}$$
with softmax applied row-wise (pp. 638–639).
- Multi-head attention (Fig. 16.7): head $i$ is $\boldsymbol h_i=\mathrm{Attn}(\mathbf Q\mathbf W_i^Q,\mathbf K\mathbf W_i^K,\mathbf V\mathbf W_i^V)$ (16.13), with $\mathbf W_i^Q,\mathbf W_i^K\in\mathbb R^{d\times d_k}$, $\mathbf W_i^V\in\mathbb R^{d\times d_v}$. The output is
$$\mathbf Z=\mathrm{MHA}(\mathbf Q,\mathbf K,\mathbf V)=\mathrm{Concat}(\boldsymbol h_1,\dots,\boldsymbol h_h)\mathbf W^O,\quad\mathbf W^O\in\mathbb R^{hd_v\times d}\tag{16.14}$$
Multiple heads can increase performance if some weight matrices are poorly initialised. After training one can often remove all but one head (p. 639).
- When one attention layer's output feeds another, this is *self-attention*, the basis of the transformer (p. 639).

*Intuition note:* Attention is a soft lookup. The query is compared with every key, the scores become weights that sum to 1, and the output is the weighted average of the values. It generalises kernel prediction, but the "kernel" is learned.

**16.2.8 Recurrent layers (p. 639).** A stateful layer augments the input with state $\boldsymbol s_t$:
$$(\boldsymbol y,\boldsymbol s_{t+1})=f(\boldsymbol x,\boldsymbol s_t)\tag{16.15}$$
In a vanilla RNN, $f$ is a simple MLP, but it may use attention (p. 639).

**16.2.9 Multiplicative layers (p. 640).** For $\boldsymbol x\in\mathbb R^n$, $\boldsymbol z\in\mathbb R^m$, the usual layer concatenates: $f=\mathbf W[\boldsymbol x;\boldsymbol z]+\boldsymbol b$. A bilinear form is more expressive:
$$f(\boldsymbol x,\boldsymbol z)=\boldsymbol z^\top\mathbb W\boldsymbol x+\mathbf U\boldsymbol z+\mathbf V\boldsymbol x+\boldsymbol b\tag{16.16}$$
$$(\boldsymbol z^\top\mathbb W\boldsymbol x)_k=\sum_{ij}z_i\mathbb W_{ijk}x_j\tag{16.17}$$
Shapes: $\mathbb W\in\mathbb R^{m\times n\times k}$, $\mathbf U\in\mathbb R^{k\times m}$, $\mathbf V\in\mathbb R^{k\times n}$, $\boldsymbol b\in\mathbb R^k$ (p. 640).
- *Hypernetwork:* a network generating the parameters of another, $f(\boldsymbol x;g(\boldsymbol z;\boldsymbol\phi))$. If $f,g$ are affine, set $\mathbf W'=\boldsymbol z^\top\mathbb W+\mathbf V$ and $\boldsymbol b'=\mathbf U\boldsymbol z+\boldsymbol b$. Then $f=\mathbf W'\boldsymbol x+\boldsymbol b'$ recovers (16.16) (p. 640).
- *Gating* (RNNs): if $\mathbf W'=\sigma(\boldsymbol z^\top\mathbb W+\mathbf V)=\mathrm{diag}(a_1,\dots,a_n)$, then $f=\boldsymbol a(\boldsymbol z)\odot\boldsymbol x$. Attention is also multiplicative, but three-way (query, key, value) (p. 640).
- *FiLM* (feature-wise linear modulation), a per-channel scale plus bias from $\boldsymbol z$:
$$f(\boldsymbol x,\boldsymbol z)=\boldsymbol a(\boldsymbol z)\odot\boldsymbol x+\boldsymbol b(\boldsymbol z)\tag{16.18}$$
(p. 640).

**16.2.10 Implicit layers (pp. 640–641).** Explicit layers set $\boldsymbol y=f(\boldsymbol x)$. Implicit layers define the output through a constraint:
$$\boldsymbol y\in\arg\min_{\boldsymbol y}f(\boldsymbol x,\boldsymbol y)\ \text{ such that }\ g(\boldsymbol x,\boldsymbol y)=0\tag{16.19}$$
The solution may need an inner optimiser or a differential-equation solver. The author names two advantages: inner computations need not be stored (saves memory), and gradients can be propagated through the whole layer via the implicit function theorem (p. 641).

### 16.3 Canonical architectures

**16.3.1 MLPs / feedforward networks (pp. 641–642).**
$$f(\boldsymbol x;\boldsymbol\theta)=\mathbf W_L\varphi_L(\mathbf W_{L-1}\varphi_{L-1}(\cdots\varphi_1(\mathbf W_1\boldsymbol x)\cdots))\tag{16.20}$$
$$h^{(l)}_k=\varphi_l\Big(b^{(l)}_k+\sum_{j=1}^{K_{l-1}}w^{(l)}_{jk}h^{(l-1)}_j\Big)\tag{16.21}$$
- For classification the final nonlinearity is usually softmax. Often the last layer is linear, its outputs are read as logits, and the loss converts them to log-probabilities (p. 642).
- *Heteroskedastic regression* (input-dependent variance): two outputs $f_\mu(\boldsymbol x)=\mathbb E[y|\boldsymbol x,\boldsymbol\theta]$ and $f_\sigma(\boldsymbol x)=\sqrt{\mathbb V[y|\boldsymbol x,\boldsymbol\theta]}$ share a "backbone" with two "heads". The $\mu$ head is linear and the $\sigma$ head uses softplus. With linear heads and a nonlinear backbone:
$$p(y|\boldsymbol x,\boldsymbol\theta)=\mathcal N\big(y\,|\,\boldsymbol w_\mu^\top f(\boldsymbol x;\boldsymbol w_{\text{shared}}),\ \sigma_+(\boldsymbol w_\sigma^\top f(\boldsymbol x;\boldsymbol w_{\text{shared}}))\big)\tag{16.22}$$
(p. 642).

*Intuition note:* Softplus keeps the standard deviation positive, while the mean may take any value. Sharing the backbone means both outputs reuse the same learned features.

**16.3.2 CNNs (p. 642).** A vanilla CNN has convolutional, pooling and linear layers and nonlinearities (Fig. 16.12 shows an early MNIST CNN, p. 643). ResNet adds skip connections, normalization, etc. ConvNeXt is called the state-of-the-art CNN for vision "as of February 2022" (p. 642).

**16.3.3 Autoencoders (pp. 642–644).** An encoder $\boldsymbol z=f_e(\boldsymbol x)$ maps to a low-dimensional latent space, and a decoder $\hat{\boldsymbol x}=f_d(\boldsymbol z)$ reconstructs. Training minimises
$$\mathcal L(\boldsymbol\theta)=\|r(\boldsymbol x)-\boldsymbol x\|_2^2,\quad r=f_d\circ f_e\tag{16.23}$$
Squared error can be replaced by conditional log-likelihoods. For images, use a convolutional encoder and a transpose-convolutional decoder. On MNIST, a 20-d embedding shown by t-SNE (2-d) separates classes fairly well, though labels were not used in training (Fig. 16.14, p. 644).

**16.3.4 RNNs (p. 645).** An RNN has a recurrent layer (Fig. 16.15). It defines a distribution over sequences with deterministic hidden states:
$$p(\boldsymbol y_{1:T})=\sum_{\boldsymbol h_{1:T}}p(\boldsymbol y_{1:T},\boldsymbol h_{1:T})=\sum_{\boldsymbol h_{1:T}}\mathbb I(\boldsymbol h_1=\boldsymbol h_1^*)\,p(\boldsymbol y_1|\boldsymbol h_1)\prod_{t=2}^T p(\boldsymbol y_t|\boldsymbol h_t)\,\mathbb I(\boldsymbol h_t=f(\boldsymbol h_{t-1},\boldsymbol y_{t-1}))\tag{16.24}$$
At training time $\boldsymbol y_{t-1}$ is observed. At prediction time it is generated. The author notes that attention can be used to selectively update parts of the state vector, as in the GRU and LSTM models. Extra inputs to $f$ give a conditional sequence model (p. 645).

**16.3.5 Transformers (pp. 645–646).**
- Task example: tag each word of a sentence, $f:\mathcal X\to\mathcal Y$ with $\mathcal X=\mathcal V^T$, $\mathcal Y=\mathcal T^T$. An RNN's embedding $\boldsymbol z_t$ depends on a hidden state that may be a lossy summary of past words. Bidirectional RNNs let future words in, but still via the hidden state (p. 645).
- An *encoder-only transformer* (e.g. BERT) computes $\boldsymbol z_t$ as a direct function of all other words using attention (Fig. 16.16) (p. 645).
- A *decoder-only transformer* lets each $\boldsymbol y_t$ attend only to $\boldsymbol y_{1:t-1}$, via masked attention. It is used for generative language models such as GPT. Combining both gives a sequence-to-sequence model $p(\boldsymbol y_{1:T_y}|\boldsymbol x_{1:T_x})$ (p. 646).
- The author says it has been found that large transformers are very flexible sequence-to-sequence approximators if trained on enough data. The reasons are "still not very clear", though some insights exist in the cited works (p. 646).

**16.3.6 GNNs (p. 646).** Networks for graph-structured data; details are in a supplementary section, not in this unit (p. 646).

## Toy example (ours, not from the text)
Scaled dot-product attention (16.9, 16.10, 16.8) with $d_k=2$, one query, two keys, two values.
- $\boldsymbol q=(1,0)$, $\boldsymbol k_1=(2,0)$, $\boldsymbol k_2=(0,2)$, $\boldsymbol v_1=(1,0)$, $\boldsymbol v_2=(0,1)$.
- Scores: $a_1=\boldsymbol q^\top\boldsymbol k_1/\sqrt2=2/1.4142=1.4142$. $a_2=0/1.4142=0$.
- Softmax: $e^{1.4142}\approx4.113$, $e^0=1$, sum $=5.113$. So $\alpha_1\approx0.8044$, $\alpha_2\approx0.1956$ (these sum to 1).
- Output: $0.8044(1,0)+0.1956(0,1)=(0.804,0.196)$. The query is more similar to key 1, so the output is mostly value 1.
- Masked version: set $a_2=-10^6$. Then $e^{a_2}\approx0$, so $\alpha=(1,0)$ and the output is $(1,0)$.

## Concepts
- [[deep-neural-network]] (new) — differentiable function expressed as a computation graph of primitive operations; "deep" = many layers (p. 631)
- [[inference-network]] (new) — DNN $f$ that maps data to the parameters of $q(\boldsymbol z|f(\mathcal D;\boldsymbol\phi))$; relates to [[Variational inference & ELBO]] only loosely, since the chapter does not discuss the ELBO (p. 631)
- [[activation-function]] (new) — pointwise nonlinearity applied to a layer; needed because stacked linear layers collapse to one (pp. 632–633)
- [[convolutional-layer]] (new) — shared-kernel layer, eqs. 16.4–16.5; gives shift equivariance (pp. 633–634)
- [[residual-connection]] (new) — skip connection $\boldsymbol y=\varphi(\mathrm{conv}(\boldsymbol x))+\boldsymbol x$; layer learns an offset (p. 635)
- [[layer-normalization]] (new) — mean-subtraction and rescaling per vector, read as projection to a sphere (pp. 635–636)
- [[dropout]] (new) — random omission of units while training; ensemble view; weights scaled by $1-p$ at test (pp. 636–637)
- [[attention-layer]] (new) — input-dependent weights: softmax of scaled query–key scores applied to values (pp. 637–639)
- [[recurrent-layer]] (new) — stateful layer $(\boldsymbol y,\boldsymbol s_{t+1})=f(\boldsymbol x,\boldsymbol s_t)$ (p. 639)
- [[multiplicative-interaction]] (new) — bilinear layer; hypernetworks and gating can be viewed as special cases, FiLM as a variant (p. 640)
- [[implicit-layer]] (new) — layer whose output is defined by a constrained optimisation, eq. 16.19 (pp. 640–641)
- [[transformer]] (new) — sequence model built on (masked) attention rather than recurrent state (pp. 645–646)
- [[heteroskedastic-regression]] (new) — regression where the predicted variance depends on the input (p. 642)

## Canonical instances
- [[heteroskedastic-mlp]] — backbone with $\mu$ and $\sigma$ heads, eq. 16.22 (p. 642)
- [[mnist-autoencoder]] — conv autoencoder with 20-d embedding visualised by t-SNE (p. 644)
- [[early-mnist-cnn]] — 1989 CNN example (Fig. 16.12) (p. 643)
- [[bert-gpt]] — encoder-only and decoder-only transformers (pp. 645–646)

## Bridges (candidates)
- [structural-analogy] attention $\sum_i\alpha_i\boldsymbol v_i$ ↔ kernel/GP prediction: weighted average of training targets with similarity weights — the text itself draws this analogy (pp. 637–638)
- [structural-analogy] dropout ensemble ↔ Bayesian model averaging (Monte Carlo dropout, Ch. 17): both average over many networks; the chapter only points forward
- [metaphor] inference network $q(\boldsymbol z|f(\mathcal D;\boldsymbol\phi))$ ↔ Variational inference: a learned function outputs approximate-posterior parameters
- [structural-analogy] RNN eq. 16.24 ↔ graphical models: a sequence model with a deterministic hidden-state chain

## Questions this raises
- Why do large transformers work so well? The author says the reasons are still not very clear (p. 646).
- When is a DNN better used as the model (way 1) versus as an inference network (way 2), and how does Chapter 17 (Bayesian deep learning) change this?
- Does Monte Carlo dropout give honest posterior uncertainty, or only a heuristic ensemble?
- How does the implicit function theorem give gradients through an implicit layer?

## Reading notes
- Printed page = pdf − 34 (pdf 665 = printed 631). Page labels give printed numbers directly.
- Footer: "Online version. December 10, 2025"; copyright line: Author Kevin P. Murphy, MIT Press, CC-BY-NC-ND.
- Typos in the source: "x = W̃ᵀx̃" (p. 632) should read $\boldsymbol y$. In 16.2.6 the weight goes from layer $l-1$ to "layer $l+1$" and then "layer $l$" (p. 636). Eq. 16.7 says "$m$ target values" while the sum runs over $n$ (p. 638). Fig. 16.2's caption calls ReLU "restricted linear unit", while Table 16.1 says "rectified" (p. 633).
- Layer-norm details (p. 636): the text says all vectors get "unit norm", but the formula $\sqrt d\,\Pi_S(\cdot)$ has norm $\sqrt d$ (added check). The printed identity $\|\boldsymbol x-\boldsymbol y\|^2=-2\boldsymbol x^\top\boldsymbol y-2$ seems to have a sign slip. For unit vectors, $\|\boldsymbol x-\boldsymbol y\|^2=2-2\boldsymbol x^\top\boldsymbol y$ (added step).
- In 16.3.5, plain $T$ is the sentence length and the similar-looking calligraphic $\mathcal T$ is the tag vocabulary, as printed.
- Equations 16.20–16.24 were transcribed from the page images. No exercises appear in this unit. Supplementary Sections 16.1.1–16.1.2 (transformer details, GNNs) are not part of these pages.
