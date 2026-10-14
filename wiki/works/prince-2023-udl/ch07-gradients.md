---
id: prince-2023-udl/ch07-gradients
work: prince-2023-udl
unit: "Chapter 7 — Gradients and initialization"
pages: 96-117
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
# Gradients and initialization

## L0 — One line
Backpropagation computes every parameter gradient efficiently by running the network forward once, storing the activations, and then sweeping backward while reusing earlier results. He initialization sets the weight variance (2 divided by the layer's input width, for ReLU networks) so that the forward-pass variance of the signals stays stable from layer to layer; for equal-width layers the gradient variance is stable too.

## L1 — The gist (≤ 120 words)
Training a deep network with SGD needs the gradient of the loss for every parameter, at every iteration. The chapter asks how to compute these gradients cheaply and how to choose starting weights so training is stable. Answer 1: backpropagation. A forward pass stores the activations. A backward pass applies the chain rule from the output toward the input and reuses each partial result. Answer 2: a badly chosen initial weight variance can make activations and gradients shrink or blow up exponentially with depth. Setting it to 2/D_h (He initialization, ReLU networks; D_h = layer inputs) keeps forward activation variance stable, and gradient variance too when layers have equal width. Modern frameworks automate the gradient computation.

**Prerequisites:** chain rule; partial derivatives; matrix–vector products and transposes; mean, variance and independence of random variables; ReLU; SGD update.

## L2 — Key ideas (5–10 bullets)
- SGD needs $\partial \ell_i/\partial \beta_k$ and $\partial \ell_i/\partial \Omega_k$ for every layer and every batch example, so gradient computation must be efficient (pp. 96–97).
- Observation 1: a weight's effect is scaled by its source activation, so the forward pass stores all activations (p. 97).
- Observation 2: a parameter's effect on the loss passes through all later layers. These shared factors can be computed once, working backward (pp. 98–100).
- The scalar toy model shows the full pattern: forward pass (7.9), backward pass #1 over intermediate variables (7.13), backward pass #2 over parameters (7.14–7.16) (pp. 100–103).
- For ReLU networks, the backward recursion alternately multiplies by $\boldsymbol\Omega_k^T$ and masks by $\mathbb{I}[\mathbf f_{k-1}>0]$ (eq. 7.25). It is cheap in compute but must store all forward activations (pp. 104–106).
- Frameworks such as PyTorch do this automatically (algorithmic differentiation), on GPUs, with batch tensors, and on arbitrary acyclic graphs (pp. 106–107).
- Poor initialization can make activations (forward) and gradients (backward) vanish or explode, exponentially with depth (pp. 108, 113).
- With zero biases, zero-mean independent weights, ReLU and pre-activations symmetric about zero, forward variance is preserved if $\sigma_\Omega^2 = 2/D_h$ (He initialization). Backward needs $2/D_{h'}$, and $4/(D_h+D_{h'})$ is a compromise (pp. 109–111).

## L3 — Walkthrough

### Opening and 7.1 Problem definitions (pp. 96–97)
Chapter 6 gave iterative optimizers. This chapter handles two neural-network-specific issues: computing gradients efficiently (the largest models have about $10^{12}$ parameters), and initializing parameters so that initial losses and gradients are not extremely large or small (p. 96).

The network has three hidden layers (p. 96):
$$\mathbf h_1=\mathbf a[\boldsymbol\beta_0+\boldsymbol\Omega_0\mathbf x],\ \ \mathbf h_2=\mathbf a[\boldsymbol\beta_1+\boldsymbol\Omega_1\mathbf h_1],\ \ \mathbf h_3=\mathbf a[\boldsymbol\beta_2+\boldsymbol\Omega_2\mathbf h_2],\ \ \mathbf f[\mathbf x,\boldsymbol\phi]=\boldsymbol\beta_3+\boldsymbol\Omega_3\mathbf h_3 \tag{7.1}$$
Here $\mathbf a[\bullet]$ applies the activation to each element. The parameters are $\boldsymbol\phi=\{\boldsymbol\beta_k,\boldsymbol\Omega_k\}$.

Each training example has a loss term $\ell_i$, the negative log-likelihood of the label $y_i$ (for example, least squares $(\mathrm f[\mathbf x_i,\boldsymbol\phi]-y_i)^2$). The total loss and the SGD update are (p. 97):
$$L[\boldsymbol\phi]=\sum_{i=1}^{I}\ell_i \tag{7.2}$$
$$\boldsymbol\phi_{t+1}\leftarrow\boldsymbol\phi_t-\alpha\sum_{i\in\mathcal B_t}\frac{\partial \ell_i[\boldsymbol\phi_t]}{\partial\boldsymbol\phi} \tag{7.3}$$
$\alpha$ is the learning rate and $\mathcal B_t$ the batch indices. We therefore need $\partial\ell_i/\partial\boldsymbol\beta_k$ and $\partial\ell_i/\partial\boldsymbol\Omega_k$ (7.4) for each layer $k\in\{0,\dots,K\}$ and each batch index (p. 97).

### 7.2 Computing derivatives (pp. 97–100)
- **Observation 1.** A weight multiplies a source hidden unit's activation and adds the result to a destination unit. A small change in the weight is therefore amplified or attenuated by that activation. So we run the network on each batch example and store all hidden activations. This is the **forward pass** (p. 97; Fig. 7.1, p. 98).
- **Observation 2.** A small change in a parameter ripples through all later layers to the output and the loss. The quantities that describe this ripple (how each layer affects its successor) are also needed for other parameters in the same or earlier layers. They can be computed once and reused (p. 98).
  - For a parameter feeding $\mathbf h_3$, we need how $\mathbf h_3$ changes $\mathbf f$ and how $\mathbf f$ changes $\ell$.
  - For one feeding $\mathbf h_2$, we also need how $\mathbf h_2$ affects $\mathbf h_3$.
  - For one feeding $\mathbf h_1$, we also need how $\mathbf h_1$ affects $\mathbf h_2$ (p. 98; Fig. 7.2, p. 99).

Moving backward, most needed terms were already computed in the previous step. This is the **backward pass** (p. 100). The full derivation needs matrix calculus, so the author first derives it for a scalar toy model (p. 100).

*Intuition note.* Every weight's effect on the loss is "how much its source activation is" times "how the loss reacts downstream of its destination". The first factor comes from the forward pass. The second is shared by many weights and is built up from the output backward, so nothing is recomputed.

### 7.3 Toy example (pp. 100–103)
**Model** with eight scalar parameters (p. 100):
$$\mathrm f[x,\boldsymbol\phi]=\beta_3+\omega_3\cos\Big[\beta_2+\omega_2\exp\big[\beta_1+\omega_1\sin[\beta_0+\omega_0 x]\big]\Big]\tag{7.5}$$
The loss is $\ell_i=(\mathrm f[x_i,\boldsymbol\phi]-y_i)^2$ (7.6). The goal is the eight derivatives of $\ell_i$ in (7.7). Writing them directly is awkward and redundant. For example, $\partial\ell_i/\partial\omega_0$ (7.8) is a long product in which the same exponential term appears three times (p. 100).

**Forward pass** (7.9; Fig. 7.3). Compute and store the following (p. 101):
$$f_0=\beta_0+\omega_0x_i,\ h_1=\sin[f_0],\ f_1=\beta_1+\omega_1h_1,\ h_2=\exp[f_1],\ f_2=\beta_2+\omega_2h_2,\ h_3=\cos[f_2],\ f_3=\beta_3+\omega_3h_3,\ \ell_i=(f_3-y_i)^2$$

**Backward pass #1.** Compute the derivatives of $\ell_i$ with respect to the intermediates, in reverse order: $\partial\ell_i/\partial f_3,\ \partial\ell_i/\partial h_3,\dots,\partial\ell_i/\partial f_0$ (7.10). The first is
$$\frac{\partial\ell_i}{\partial f_3}=2(f_3-y_i)\tag{7.11}$$
The next uses the chain rule (p. 101):
$$\frac{\partial\ell_i}{\partial h_3}=\frac{\partial f_3}{\partial h_3}\frac{\partial\ell_i}{\partial f_3}\tag{7.12}$$
Here $\partial f_3/\partial h_3=\omega_3$ and the second factor is already known. Continuing (Fig. 7.4, p. 102):
$$\frac{\partial\ell_i}{\partial f_2}=\frac{\partial h_3}{\partial f_2}\Big(\frac{\partial f_3}{\partial h_3}\frac{\partial\ell_i}{\partial f_3}\Big),\quad
\frac{\partial\ell_i}{\partial h_2}=\frac{\partial f_2}{\partial h_2}\Big(\frac{\partial h_3}{\partial f_2}\frac{\partial f_3}{\partial h_3}\frac{\partial\ell_i}{\partial f_3}\Big),\ \dots,$$
$$\frac{\partial\ell_i}{\partial f_0}=\frac{\partial h_1}{\partial f_0}\Big(\frac{\partial f_1}{\partial h_1}\frac{\partial h_2}{\partial f_1}\frac{\partial f_2}{\partial h_2}\frac{\partial h_3}{\partial f_2}\frac{\partial f_3}{\partial h_3}\frac{\partial\ell_i}{\partial f_3}\Big)\tag{7.13}$$
In each line the bracket was computed in the previous step and the new factor is simple. This embodies Observation 2 (p. 102). The author notes (footnote 1, p. 103) that the derivatives with respect to the activations $h_k$ are not needed explicitly in the final algorithm.

**Backward pass #2.** For the parameters (Fig. 7.5, p. 103):
$$\frac{\partial\ell_i}{\partial\beta_k}=\frac{\partial f_k}{\partial\beta_k}\frac{\partial\ell_i}{\partial f_k},\qquad \frac{\partial\ell_i}{\partial\omega_k}=\frac{\partial f_k}{\partial\omega_k}\frac{\partial\ell_i}{\partial f_k}\tag{7.14}$$
For $k>0$, $f_k=\beta_k+\omega_kh_k$, so
$$\frac{\partial f_k}{\partial\beta_k}=1,\qquad\frac{\partial f_k}{\partial\omega_k}=h_k\tag{7.15}$$
This matches Observation 1: the effect of $\omega_k$ is proportional to the stored $h_k$. For $f_0=\beta_0+\omega_0x_i$:
$$\frac{\partial f_0}{\partial\beta_0}=1,\qquad\frac{\partial f_0}{\partial\omega_0}=x_i\tag{7.16}$$
Backpropagation is simpler and more efficient than computing each derivative separately (p. 103).

*Intuition note.* Each derivative is a product of local slopes along the path from the parameter to the loss. Doing the products from the loss backward means each partial product can be reused for the parameters earlier in the network.

### 7.4 Backpropagation algorithm (pp. 103–107)
The same idea is applied to the three-layer network of Fig. 7.1. The differences are that $\mathbf f_k,\mathbf h_k,\boldsymbol\beta_k$ are vectors, $\boldsymbol\Omega_k$ are matrices, and the activation is ReLU (p. 103).

**Forward pass** (7.17): $\mathbf f_0=\boldsymbol\beta_0+\boldsymbol\Omega_0\mathbf x_i$, $\mathbf h_1=\mathbf a[\mathbf f_0]$, $\mathbf f_1=\boldsymbol\beta_1+\boldsymbol\Omega_1\mathbf h_1$, and so on, up to $\mathbf f_3=\boldsymbol\beta_3+\boldsymbol\Omega_3\mathbf h_3$ and $\ell_i=\mathrm l[\mathbf f_3,y_i]$. Here $\mathbf f_{k-1}$ are the pre-activations (before ReLU) of hidden layer $k$ and $\mathbf h_k$ the activations. All intermediates are stored (pp. 103–104). The ReLU derivative is 0 for negative input and 1 for positive input (Fig. 7.6, p. 104).

**Backward pass #1.** For $\mathbf f_2$ (p. 104):
$$\frac{\partial\ell_i}{\partial\mathbf f_2}=\frac{\partial\mathbf h_3}{\partial\mathbf f_2}\frac{\partial\mathbf f_3}{\partial\mathbf h_3}\frac{\partial\ell_i}{\partial\mathbf f_3}\tag{7.18}$$
The three terms have sizes $D_3\times D_3$, $D_3\times D_f$ and $D_f\times1$. $D_3$ is the number of units in layer 3 and $D_f$ the output dimension. Similarly:
$$\frac{\partial\ell_i}{\partial\mathbf f_1}=\frac{\partial\mathbf h_2}{\partial\mathbf f_1}\frac{\partial\mathbf f_2}{\partial\mathbf h_2}\Big(\frac{\partial\mathbf h_3}{\partial\mathbf f_2}\frac{\partial\mathbf f_3}{\partial\mathbf h_3}\frac{\partial\ell_i}{\partial\mathbf f_3}\Big)\tag{7.19}$$
$$\frac{\partial\ell_i}{\partial\mathbf f_0}=\frac{\partial\mathbf h_1}{\partial\mathbf f_0}\frac{\partial\mathbf f_1}{\partial\mathbf h_1}\Big(\frac{\partial\mathbf h_2}{\partial\mathbf f_1}\frac{\partial\mathbf f_2}{\partial\mathbf h_2}\frac{\partial\mathbf h_3}{\partial\mathbf f_2}\frac{\partial\mathbf f_3}{\partial\mathbf h_3}\frac{\partial\ell_i}{\partial\mathbf f_3}\Big)\tag{7.20}$$
The terms are simple (pp. 104–105):
- $\partial\ell_i/\partial\mathbf f_3$ depends on the loss function but usually has a simple form.
- $\partial\mathbf f_3/\partial\mathbf h_3=\boldsymbol\Omega_3^T$ (7.21). This is not obvious without matrix calculus (Problem 7.6).
- $\partial\mathbf h_3/\partial\mathbf f_2$ is a diagonal matrix, because each activation depends only on its own pre-activation. For ReLU the diagonal is 0 where $\mathbf f_2<0$ and 1 otherwise. The author extracts it as a vector $\mathbb I[\mathbf f_2>0]$ and multiplies pointwise, which is more efficient.

Moving back, we alternately multiply by $\boldsymbol\Omega_k^T$ and threshold using the stored $\mathbf f_{k-1}$ (p. 105).

**Backward pass #2** (p. 105):
$$\frac{\partial\ell_i}{\partial\boldsymbol\beta_k}=\frac{\partial\mathbf f_k}{\partial\boldsymbol\beta_k}\frac{\partial\ell_i}{\partial\mathbf f_k}=\frac{\partial\ell_i}{\partial\mathbf f_k}\tag{7.22}$$
$$\frac{\partial\ell_i}{\partial\boldsymbol\Omega_k}=\frac{\partial\mathbf f_k}{\partial\boldsymbol\Omega_k}\frac{\partial\ell_i}{\partial\mathbf f_k}=\frac{\partial\ell_i}{\partial\mathbf f_k}\mathbf h_k^T\tag{7.23}$$
The step to the last line of (7.23) is explored in Problem 7.9. The result has the same size as $\boldsymbol\Omega_k$ and is linear in $\mathbf h_k$. This agrees with Observation 1 (p. 105).

#### 7.4.1 Algorithm summary (p. 106)
For $K$ hidden ReLU layers.

*Forward* (store everything), with $k\in\{1,\dots,K\}$:
$$\mathbf f_0=\boldsymbol\beta_0+\boldsymbol\Omega_0\mathbf x_i,\qquad\mathbf h_k=\mathbf a[\mathbf f_{k-1}],\qquad\mathbf f_k=\boldsymbol\beta_k+\boldsymbol\Omega_k\mathbf h_k\tag{7.24}$$
*Backward*, starting from $\partial\ell_i/\partial\mathbf f_K$, for $k\in\{K,\dots,1\}$:
$$\frac{\partial\ell_i}{\partial\boldsymbol\beta_k}=\frac{\partial\ell_i}{\partial\mathbf f_k},\quad\frac{\partial\ell_i}{\partial\boldsymbol\Omega_k}=\frac{\partial\ell_i}{\partial\mathbf f_k}\mathbf h_k^T,\quad\frac{\partial\ell_i}{\partial\mathbf f_{k-1}}=\mathbb I[\mathbf f_{k-1}>0]\odot\Big(\boldsymbol\Omega_k^T\frac{\partial\ell_i}{\partial\mathbf f_k}\Big)\tag{7.25}$$
$\odot$ is pointwise multiplication. Finally:
$$\frac{\partial\ell_i}{\partial\boldsymbol\beta_0}=\frac{\partial\ell_i}{\partial\mathbf f_0},\qquad\frac{\partial\ell_i}{\partial\boldsymbol\Omega_0}=\frac{\partial\ell_i}{\partial\mathbf f_0}\mathbf x_i^T\tag{7.26}$$
These are computed for every example in the batch and summed to give the SGD gradient. The dominant cost is matrix multiplication (by $\boldsymbol\Omega$ forward, $\boldsymbol\Omega^T$ backward), which uses only additions and multiplications, so it is very efficient in compute. It is not memory-efficient, because all forward intermediates must be stored, which can limit model size (p. 106).

*Intuition note.* Going backward, each layer hands its "blame vector" to the layer below through the transposed weights. ReLU units that were off pass nothing back. A weight's gradient is that blame times the activation it multiplied.

#### 7.4.2 Algorithmic differentiation (p. 107)
Frameworks such as PyTorch and TensorFlow compute derivatives automatically from the model specification. Each component (linear map, ReLU, loss) knows its own derivative, and the framework knows the order of operations. They exploit GPU parallelism, and can process the whole batch in parallel if memory allows. The input then becomes a tensor, a generalization of a matrix to arbitrary dimensions. For 1D data the input is 2D (batch × data dimension). For RGB images (height × width × channel), it is a 4D tensor (p. 107).

#### 7.4.3 Arbitrary computational graphs (p. 107)
The ideas of backpropagation still hold if the computational graph is acyclic (for example, branches processed by two sub-networks and then recombined). Modern frameworks handle arbitrary acyclic graphs (p. 107).

### 7.5 Parameter initialization (pp. 107–111)
Pre-activations are $\mathbf f_k=\boldsymbol\beta_k+\boldsymbol\Omega_k\mathbf a[\mathbf f_{k-1}]$ (7.27). Take zero biases and zero-mean normal weights with variance $\sigma^2$ (p. 108).
- If $\sigma^2$ is very small (for example $10^{-5}$), each pre-activation is a weighted sum with tiny weights, so it is likely smaller than the input. ReLU also clips negatives. Magnitudes shrink layer by layer.
- If $\sigma^2$ is very large (for example $10^5$), magnitudes are likely to grow. ReLU halves the range, but if $\sigma^2$ is large enough, the magnitudes still grow.

Values may then be too small or too large for finite-precision floating point. The same logic applies backward, since each step in (7.25) multiplies by $\boldsymbol\Omega^T$. These are the **vanishing gradient** (updates vanishingly small) and **exploding gradient** (updates unstable) problems (p. 108).

#### 7.5.1 Forward pass (pp. 108–110)
Consider adjacent layers with $\mathbf h=\mathbf a[\mathbf f]$ and $\mathbf f'=\boldsymbol\beta+\boldsymbol\Omega\mathbf h$ (7.28), dimensions $D_h$ and $D_{h'}$. Assume the $f_j$ have variance $\sigma_f^2$, $\beta_i=0$, and $\Omega_{ij}$ is normal with mean 0 and variance $\sigma_\Omega^2$ (p. 108). Mean (assuming weights and hidden units are independent):
$$\mathbb E[f_i']=\mathbb E\Big[\beta_i+\sum_{j=1}^{D_h}\Omega_{ij}h_j\Big]=\mathbb E[\beta_i]+\sum_j\mathbb E[\Omega_{ij}]\mathbb E[h_j]=0+\sum_j0\cdot\mathbb E[h_j]=0\tag{7.29}$$
Variance, using $\sigma^2=\mathbb E[z^2]-\mathbb E[z]^2$ and again independence (p. 109):
$$\sigma_{f_i'}^2=\mathbb E[f_i'^2]-\mathbb E[f_i']^2=\mathbb E\Big[\Big(\sum_{j}\Omega_{ij}h_j\Big)^2\Big]=\sum_j\mathbb E[\Omega_{ij}^2]\mathbb E[h_j^2]=\sigma_\Omega^2\sum_{j=1}^{D_h}\mathbb E[h_j^2]\tag{7.30}$$
(Added step: the cross terms $j\neq j'$ in the square vanish because $\mathbb E[\Omega_{ij}]=0$ and the weights are independent of each other and of $\mathbf h$.) If the pre-activations $f_j$ are symmetric about zero, ReLU clips half of them and $\mathbb E[h_j^2]=\sigma_f^2/2$ (Problem 7.14). Then
$$\sigma_{f_i'}^2=\sigma_\Omega^2\sum_{j=1}^{D_h}\frac{\sigma_f^2}{2}=\frac12D_h\sigma_\Omega^2\sigma_f^2\tag{7.31}$$
So to keep $\sigma_{f'}^2=\sigma_f^2$ in the forward pass, set
$$\sigma_\Omega^2=\frac{2}{D_h}\tag{7.32}$$
with $D_h$ the dimension of the layer the weights are applied to. This is **He initialization** (p. 110).

*Intuition note.* Each output is a sum of $D_h$ terms, so its variance grows with $D_h$. The factor $1/2$ comes from ReLU zeroing about half the inputs. Dividing the weight variance by $D_h/2$ cancels both effects.

**Experiment (Fig. 7.7, p. 110).** The network has 50 hidden layers and $D_h=100$ units per layer. The input is 100-dimensional and standard normal, the target is $y=0$, and the loss is least squares. Biases are zero. Weight variances are $\sigma_\Omega^2\in\{0.001,0.01,0.02,0.1,1.0\}$. The value $0.02=2/D_h$ keeps the forward activation variance stable. Larger values make it grow rapidly and smaller values make it shrink rapidly (log scale). The backward gradient variance follows the same trend. Larger values explode and smaller values vanish.

#### 7.5.2 Backward pass (pp. 110–111)
A similar argument applies, now with $\boldsymbol\Omega^T$ (7.25). To keep the gradient variance stable, set
$$\sigma_\Omega^2=\frac{2}{D_{h'}}\tag{7.33}$$
where $D_{h'}$ is the dimension of the layer the weights feed into (p. 111).

#### 7.5.3 Both passes (p. 111)
If $\boldsymbol\Omega$ is not square ($D_h\ne D_{h'}$), (7.32) and (7.33) cannot both hold. One compromise uses the mean $(D_h+D_{h'})/2$:
$$\sigma_\Omega^2=\frac{4}{D_h+D_{h'}}\tag{7.34}$$
Fig. 7.7 shows empirically that forward variance and backward gradient variance stay stable with appropriate initialization (p. 111).

### 7.6 Example training code (pp. 111–112)
Fig. 7.8 gives PyTorch code. It defines a network and He initialization. It creates random data, a least squares loss, and SGD with momentum with batch size 10 over 100 epochs. The text says the learning rate starts at 0.01 and halves every 10 epochs. All backpropagation detail is hidden in the single call `loss.backward()` (p. 111).

### 7.7 Summary (pp. 111–113)
Efficient gradients (backpropagation) and careful initialization are both critical. Activation magnitudes can shrink or grow exponentially in the forward pass, and gradients behave the same way backward. Both problems impede training but can be avoided with appropriate initialization. The next chapter turns to measuring model performance (p. 113).

### Notes (pp. 113–114) — condensed
- **Backpropagation history.** The reuse of partial computations was discovered repeatedly (Werbos, Bryson et al., LeCun, Parker). Rumelhart et al. (1985, 1986) gave the best-known description and coined the term. Progress later stalled, in retrospect because of limited data, limited compute and sigmoid activations (p. 113). The frameworks implement reverse-mode algorithmic differentiation, as opposed to forward-mode, which accumulates chain-rule derivatives moving forward (p. 113).
- **Initialization.** He initialization is from He et al. (2015). Glorot/Xavier initialization is very similar but ignores ReLU, so it differs by a factor of two. Other approaches mentioned are SeLU, data-driven schemes (layer-sequential unit variance initialization, GradInit, ActNorm), BatchNorm (chapter 11) and architecture-specific schemes (p. 113–114).
- **Memory.** Gradient checkpointing stores activations only every $N$ layers and recomputes the rest, at the cost of a second forward pass. Micro-batching and reversible networks also reduce memory (p. 114).
- **Distributed training.** Data parallelism (synchronous, or asynchronous as in Hogwild!), pipeline model parallelism and tensor model parallelism are described. One cited system combines all three to train a one-trillion-parameter language model on 3072 GPUs (p. 114).

## Toy example
Our own example (not from the text). Scalar ReLU network with $K=2$: $f_0=\beta_0+\omega_0x$, $h_1=\mathrm{ReLU}[f_0]$, $f_1=\beta_1+\omega_1h_1$, $h_2=\mathrm{ReLU}[f_1]$, $f_2=\beta_2+\omega_2h_2$, $\ell=(f_2-y)^2$. Take $x=1$, $y=2$, $\beta_0=0$, $\omega_0=2$, $\beta_1=1$, $\omega_1=0.5$, $\beta_2=0$, $\omega_2=3$.

*Forward:* $f_0=2$, $h_1=2$, $f_1=1+0.5\cdot2=2$, $h_2=2$, $f_2=0+3\cdot2=6$, $\ell=(6-2)^2=16$.

*Backward* (scalar version of 7.25; the mask $\mathbb I[f>0]$ is 1 here because $f_0=f_1=2>0$):
- $\partial\ell/\partial f_2=2(6-2)=8$. Then $\partial\ell/\partial\beta_2=8$ and $\partial\ell/\partial\omega_2=8\cdot h_2=16$.
- $\partial\ell/\partial f_1=1\cdot\omega_2\cdot8=24$. Then $\partial\ell/\partial\beta_1=24$ and $\partial\ell/\partial\omega_1=24\cdot h_1=48$.
- $\partial\ell/\partial f_0=1\cdot\omega_1\cdot24=12$. Then $\partial\ell/\partial\beta_0=12$ and $\partial\ell/\partial\omega_0=12\cdot x=12$.

*Check by direct differentiation for $\omega_0$:* with the others fixed, $f_2=3(1+0.5\omega_0)=3+1.5\omega_0$. So $\ell=(1+1.5\omega_0)^2$ and $d\ell/d\omega_0=2(1+1.5\cdot2)(1.5)=2\cdot4\cdot1.5=12$ ✓.

*Initialization:* for a layer with $D_h=50$ inputs, He initialization gives $\sigma_\Omega^2=2/50=0.04$ (from 7.32).

## Concepts
- [[backpropagation]] (new) — algorithm computing all parameter gradients by a forward pass storing activations, then a backward pass reusing partial derivatives (p. 97)
- [[forward-pass]] (new) — running the network on an example and storing all intermediate activations (p. 97)
- [[backward-pass]] (new) — working from the loss toward the input applying the chain rule, reusing earlier factors (p. 100)
- [[algorithmic-differentiation]] (new) — frameworks derive gradients automatically from the model's sequence of operations (p. 107)
- [[stochastic-gradient-descent]] (new) — updates parameters by $-\alpha\times$ summed per-example gradients over a batch (p. 97)
- [[he-initialization]] (new) — weight variance $2/D_h$ for ReLU layers, keeping forward activation variance stable (p. 110)
- [[vanishing-exploding-gradients]] (new) — gradient magnitudes shrinking or growing uncontrollably, exponentially with depth, through the backward pass (pp. 108, 113)
- [[computational-graph]] (new) — acyclic graph of operations; backpropagation still applies to it (p. 107)

## Canonical instances
- [[sin-exp-cos-toy-model]] (new) — eight-parameter scalar model used to derive backpropagation (p. 100)
- [[init-variance-experiment-fig7-7]] (new) — 50-layer, 100-unit network showing stable variance at $\sigma_\Omega^2=0.02=2/D_h$, with larger values growing and smaller ones shrinking among the five tested (p. 110)
- [[pytorch-training-loop-fig7-8]] (new) — short code example in which `loss.backward()` hides backpropagation (p. 112)

## Bridges (candidates)
- [structural-analogy] Backpropagation's reuse of partial products ↔ dynamic programming: sharing sub-results across overlapping computations.
- [same-math] Variance of $\sum_j\Omega_{ij}h_j$ for independent zero-mean terms ↔ statistics: variance of a sum of independent variables adds.
- [structural-analogy] Reverse-mode differentiation on acyclic graphs ↔ LLM training (canon link; not stated in this unit): gradients for Transformer parameters are obtained by such graph sweeps.

## Questions this raises
- Why does reverse mode suit networks (many parameters, one scalar loss) better than forward mode (Problem 7.13 asks this)?
- How do normalization layers (BatchNorm, chapter 11) relate to careful initialization?
- How much memory can gradient checkpointing save, and at what extra compute?
- What does the symmetry assumption behind $\mathbb E[h_j^2]=\sigma_f^2/2$ mean once layers are no longer symmetric about zero?

## Exercises worth doing
- Ex. 7.1 (p. 114) — derive all 13 derivatives of a small two-layer ReLU net by hand, to feel the redundancy backprop removes — difficulty: medium
- Ex. 7.6* (p. 115) — show $\partial\mathbf z/\partial\mathbf h=\boldsymbol\Omega^T$ — difficulty: medium
- Ex. 7.9* (p. 116) — derive $\partial\ell/\partial\boldsymbol\Omega=(\partial\ell/\partial\mathbf f)\mathbf h^T$ — difficulty: medium
- Ex. 7.12–7.13* (pp. 116–117) — reverse-mode versus forward-mode differentiation on a small graph — difficulty: hard
- Ex. 7.14 (p. 117) — prove $\mathbb E[b^2]=\sigma^2/2$ for ReLU (used in 7.31) — difficulty: medium
- Ex. 7.15 (p. 117) — what happens if all weights and biases start at zero — difficulty: easy

## Reading notes
- Printed page = pdf − 14. Page labels give printed numbers; I used them.
- The text on p. 111 says the learning rate starts at 0.01, but the code in Fig. 7.8 (p. 112) shows `lr = 0.1`. The caption says "two-layer network" and the code comment says "two hidden layers".
- Equations were checked against the page images; none were unreadable.
- The author omits the cross-term argument in (7.30); I marked my added step. The Notes and Problems are summarised, not solved.
