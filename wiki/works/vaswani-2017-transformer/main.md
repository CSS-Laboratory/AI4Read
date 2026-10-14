---
id: vaswani-2017-transformer/main
work: vaswani-2017-transformer
unit: paper
pages: 1-15
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Attention Is All You Need

## L0 — One line
A sequence-to-sequence model built only from attention and position-wise feed-forward layers (the Transformer), with no recurrence or convolution, matched or beat the best translation systems at a fraction of the training cost.

## L1 — The gist (≤ 120 words)
Question: can sequence transduction (mapping an input sequence to an output sequence, e.g. translation) work without recurrent or convolutional layers? Answer: yes. The Transformer is an encoder–decoder built only from attention and position-wise feed-forward layers. Positional encodings add word order, and multi-head attention offsets the resolution lost by averaging. It reached 28.4 BLEU (a translation score) on WMT 2014 (a benchmark) English-to-German and 41.8 on English-to-French (Table 2), trained significantly faster than recurrent or convolutional models, and also did well on English constituency parsing (predicting phrase-structure trees). It matters because attention links any two positions in a constant number of operations, and computation parallelizes across positions.

**Prerequisites:** matrix multiplication and shapes; softmax; dot product; mean and variance of sums of independent variables; basic idea of a neural network layer, dropout, and the Adam optimizer; big-O notation.

## L2 — Key ideas (5–10 bullets)
- Recurrent models compute hidden states step by step, which blocks parallelism within a training example. The paper proposes dropping recurrence and using attention alone. (p. 2)
- Core operation: $\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^T/\sqrt{d_k})V$. The authors suspect that for large $d_k$ the dot products grow large and push the softmax into regions with extremely small gradients; the $1/\sqrt{d_k}$ factor is meant to counteract this. (p. 4)
- Multi-head attention runs $h=8$ attention operations in parallel on learned projections ($d_k=d_v=64$). The authors say this counteracts the loss of resolution from averaging. (pp. 2, 5)
- Each layer pairs attention with a position-wise feed-forward network. Residual connections (adding a sub-layer's input to its output) and layer normalization wrap each sub-layer. The decoder masks future positions to stay autoregressive (each output depends only on earlier ones). (pp. 3, 5)
- The model has no recurrence or convolution, so order information must be injected: sinusoidal positional encodings are added to the embeddings. Learned positional embeddings gave nearly identical results. (p. 6)
- Self-attention has $O(1)$ sequential operations and $O(1)$ maximum path length. Its per-layer cost is $O(n^2 d)$, cheaper than recurrence when $n<d$. (pp. 6–7)
- Results: the big model reaches 28.4 BLEU (EN-DE) and 41.8 (EN-FR). The authors report a fraction of the training cost of the best earlier models for EN-FR, and for EN-DE the base model (27.3) at a fraction of the cost of any competitive model. Ablations show single-head attention 0.9 BLEU worse than the best setting. (pp. 8–9)
- The model also reached 91.3 F1 (a parsing accuracy score; WSJ only) and 92.7 (semi-supervised) on constituency parsing with little tuning. (pp. 9–10)

## L3 — Walkthrough

### Abstract and 1 Introduction
- **Problem.** Dominant sequence transduction models are recurrent or convolutional encoder–decoders. The best also link encoder and decoder through attention. (p. 1)
- **Bottleneck.** Recurrent models make the hidden state $h_t$ a function of $h_{t-1}$ and the input at position $t$. This sequential nature precludes parallelization within training examples. This matters at long sequence lengths, where memory limits batching across examples. (p. 2)
- Factorization tricks and conditional computation brought significant efficiency improvements, but the authors say the fundamental constraint of sequential computation remains. (p. 2)
- Attention models dependencies regardless of distance, but in all but a few cases it was used together with a recurrent network. (p. 2)
- **Proposal.** The Transformer relies entirely on attention for global dependencies. It can reach a new state of the art after as little as twelve hours on eight P100 GPUs. (p. 2)

### 2 Background
- Extended Neural GPU, ByteNet and ConvS2S also reduce sequential computation using convolutions. The operations needed to relate two positions grow with distance: linearly for ConvS2S, logarithmically for ByteNet. (p. 2)
- In the Transformer this is a constant number of operations. The cost is reduced effective resolution from averaging attention-weighted positions, which the authors say Multi-Head Attention counteracts. (p. 2)
- **Self-attention** (intra-attention) relates different positions of one sequence to compute a representation of it. It had been used in reading comprehension, summarization, entailment and sentence representations. (p. 2)
- End-to-end memory networks use recurrent attention instead of sequence-aligned recurrence. (p. 2)
- Claim: to the authors' knowledge, the Transformer is the first transduction model relying entirely on self-attention, with no sequence-aligned RNNs or convolution. (p. 2)

### 3 Model Architecture
- The encoder maps input symbols $(x_1,\dots,x_n)$ to continuous representations $z=(z_1,\dots,z_n)$. The decoder generates $(y_1,\dots,y_m)$ one element at a time, auto-regressively: it consumes previously generated symbols as extra input. (p. 2)
- The Transformer uses stacked self-attention and point-wise fully connected layers in both halves (Figure 1). (p. 3)

**3.1 Encoder and decoder stacks (p. 3)**
- Encoder: $N=6$ identical layers, each with two sub-layers: multi-head self-attention, then a position-wise feed-forward network.
- Each sub-layer's output is $\mathrm{LayerNorm}(x+\mathrm{Sublayer}(x))$. All sub-layers and embedding layers output dimension $d_{\text{model}}=512$, to facilitate the residual connections.
- Decoder: $N=6$ identical layers with a third sub-layer doing multi-head attention over the encoder output. Residual connections and layer normalization are used as in the encoder.
- The decoder self-attention is masked to stop positions attending to later positions. Together with output embeddings offset by one position, this ensures predictions for position $i$ can depend only on known outputs at positions less than $i$.

**3.2 Attention (pp. 3–5)**
- An attention function maps a query and a set of key-value pairs to an output. Query, keys, values and output are vectors. The output is a weighted sum of the values. Each weight comes from a compatibility function of the query with the corresponding key. (pp. 3–4)

*3.2.1 Scaled dot-product attention (p. 4).* Queries and keys have dimension $d_k$, values $d_v$. Compute dot products of the query with all keys, divide by $\sqrt{d_k}$, apply softmax to get weights on the values. With queries, keys, values packed into matrices $Q,K,V$:
$$\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V \tag{1}$$
- Shapes (added step; follows from the definitions): $Q\in\mathbb R^{n_q\times d_k}$, $K\in\mathbb R^{n_k\times d_k}$, $V\in\mathbb R^{n_k\times d_v}$, so $QK^T\in\mathbb R^{n_q\times n_k}$ and the output is $n_q\times d_v$.
- Comparison with additive attention, which uses a feed-forward network with one hidden layer. The two are similar in theoretical complexity. Dot-product attention is much faster and more space-efficient in practice, since it uses optimized matrix multiplication.
- Dot-product attention is identical to the authors' algorithm except for the $1/\sqrt{d_k}$ factor. For small $d_k$ the two perform similarly. For larger $d_k$, additive attention beats unscaled dot-product attention (citing [3]).
- **Author's suspicion:** for large $d_k$ the dot products grow large in magnitude, pushing the softmax into regions with extremely small gradients. So they scale by $1/\sqrt{d_k}$.
- Footnote 4: assume components of $q$ and $k$ are independent random variables with mean 0 and variance 1. Then $q\cdot k=\sum_{i=1}^{d_k}q_ik_i$ has mean 0 and variance $d_k$.
- (added step) Dividing a variable by $\sqrt{d_k}$ divides its variance by $d_k$, so $\mathrm{Var}(q\cdot k/\sqrt{d_k})=d_k/d_k=1$.

*Intuition note.* Each output row is a blend of value vectors. Keys that match the query get larger weights. The authors suspect that without scaling, large $d_k$ makes the dot products large (their variance is $d_k$ under the footnote-4 assumptions), which pushes the softmax into regions with extremely small gradients.

*3.2.2 Multi-head attention (pp. 4–5).* Instead of one attention with $d_{\text{model}}$-dimensional keys, values and queries, the authors found it beneficial to project them $h$ times with different learned linear maps to $d_k,d_k,d_v$ dimensions. Attention runs in parallel on each. The $d_v$-dimensional outputs are concatenated and projected again.
$$\mathrm{MultiHead}(Q,K,V)=\mathrm{Concat}(\mathrm{head}_1,\dots,\mathrm{head}_h)W^O$$
$$\mathrm{head}_i=\mathrm{Attention}(QW_i^Q,KW_i^K,VW_i^V)$$
with $W_i^Q\in\mathbb R^{d_{\text{model}}\times d_k}$, $W_i^K\in\mathbb R^{d_{\text{model}}\times d_k}$, $W_i^V\in\mathbb R^{d_{\text{model}}\times d_v}$, $W^O\in\mathbb R^{hd_v\times d_{\text{model}}}$.
- Claim: multi-head attention lets the model jointly attend to information from different representation subspaces at different positions. With a single head, averaging inhibits this. (p. 5)
- Settings: $h=8$, $d_k=d_v=d_{\text{model}}/h=64$. Because each head is smaller, total cost is similar to single-head attention at full dimensionality. (p. 5)

*3.2.3 Three uses of attention (p. 5).*
1. Encoder-decoder attention: queries come from the previous decoder layer, keys and values from the encoder output. Every decoder position attends over all input positions.
2. Encoder self-attention: queries, keys, values all come from the previous encoder layer. Each position attends to all positions.
3. Decoder self-attention: each position attends to all decoder positions up to and including itself. Leftward information flow is blocked to keep the auto-regressive property. Inside scaled dot-product attention, illegal connections are masked by setting their softmax inputs to $-\infty$.

**3.3 Position-wise feed-forward networks (p. 5).** Applied to each position separately and identically: two linear transformations with a ReLU between them.
$$\mathrm{FFN}(x)=\max(0,xW_1+b_1)W_2+b_2 \tag{2}$$
Parameters are shared across positions but differ from layer to layer. Equivalent to two convolutions with kernel size 1. Input and output dimension is 512, inner dimension $d_{ff}=2048$.

**3.4 Embeddings and softmax (p. 5).** Learned embeddings map tokens to $d_{\text{model}}$-dimensional vectors. The usual learned linear map plus softmax turns decoder output into next-token probabilities. The same weight matrix is shared between the two embedding layers and the pre-softmax linear map. In the embedding layers those weights are multiplied by $\sqrt{d_{\text{model}}}$.

**3.5 Positional encoding (p. 6).** With no recurrence or convolution, order information must be injected. Positional encodings of dimension $d_{\text{model}}$ are added to the input embeddings at the bottoms of both stacks.
$$PE_{(pos,2i)}=\sin\!\big(pos/10000^{2i/d_{\text{model}}}\big),\qquad PE_{(pos,2i+1)}=\cos\!\big(pos/10000^{2i/d_{\text{model}}}\big)$$
- Each dimension is a sinusoid. Wavelengths form a geometric progression from $2\pi$ to $10000\cdot 2\pi$.
- **Hypothesis:** this lets the model easily learn to attend by relative position, because for any fixed offset $k$, $PE_{pos+k}$ is a linear function of $PE_{pos}$.
- Learned positional embeddings gave nearly identical results (Table 3, row E). Sinusoids were chosen because they may allow extrapolation to longer sequences than seen in training.

### 4 Why self-attention (pp. 6–7)
Three desiderata: computation per layer, parallelizable computation (minimum sequential operations), and path length between long-range dependencies. Shorter paths make long-range dependencies easier to learn (citing [12]).

**Table 1** ($n$ = sequence length, $d$ = representation dimension, $k$ = kernel size, $r$ = neighbourhood size) (p. 6):

| Layer type | Complexity per layer | Sequential ops | Max path length |
|---|---|---|---|
| Self-attention | $O(n^2 d)$ | $O(1)$ | $O(1)$ |
| Recurrent | $O(n d^2)$ | $O(n)$ | $O(n)$ |
| Convolutional | $O(k n d^2)$ | $O(1)$ | $O(\log_k n)$ |
| Self-attention (restricted) | $O(r n d)$ | $O(1)$ | $O(n/r)$ |

- Self-attention is faster than recurrent layers when $n<d$. The authors say this is most often the case for word-piece and byte-pair representations. (p. 7)
- Restricting attention to a neighbourhood of size $r$ may help very long sequences, at the cost of path length $O(n/r)$. This is left for future work. (p. 7)
- A single convolutional layer with $k<n$ does not connect all pairs. Covering all pairs needs $O(n/k)$ layers (contiguous kernels) or $O(\log_k n)$ (dilated). Convolutions cost more than recurrent layers by a factor of $k$. Separable convolutions cost $O(k\cdot n\cdot d+n\cdot d^2)$. Even with $k=n$ this equals self-attention plus a point-wise feed-forward layer, the authors' approach. (p. 7)
- Side benefit: self-attention could yield more interpretable models. Individual heads clearly learn different tasks, and many appear related to syntactic and semantic structure (appendix figures). (p. 7)

*Intuition note.* Self-attention pays $n^2$ pairwise scores per layer. In return, any two tokens are a constant number of steps apart and all positions can be computed at once. A recurrent net must pass information through up to $n$ steps in order.

### 5 Training (pp. 7–8)
- **5.1 Data.** WMT 2014 English-German: about 4.5M sentence pairs, byte-pair encoding, shared vocabulary of about 37,000 tokens. English-French: 36M sentences, 32,000 word-piece vocabulary. Batches grouped by approximate length, about 25,000 source and 25,000 target tokens each. (p. 7)
- **5.2 Hardware.** One machine, 8 NVIDIA P100 GPUs. Base model: about 0.4 s per step, 100,000 steps, 12 hours. Big model: 1.0 s per step, 300,000 steps, 3.5 days. (p. 7)
- **5.3 Optimizer.** Adam with $\beta_1=0.9$, $\beta_2=0.98$, $\epsilon=10^{-9}$. (p. 7)
$$lrate=d_{\text{model}}^{-0.5}\cdot\min\!\big(step\_num^{-0.5},\; step\_num\cdot warmup\_steps^{-1.5}\big) \tag{3}$$
The rate rises linearly for the first $warmup\_steps=4000$ steps, then falls proportionally to the inverse square root of the step number.
- **5.4 Regularization (p. 8).** Residual dropout is applied to each sub-layer output before it is added and normalized, and to the sums of embeddings and positional encodings. Base model $P_{drop}=0.1$. Label smoothing $\epsilon_{ls}=0.1$ hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU.

### 6 Results
**6.1 Machine translation (p. 8).**
- EN-DE: Transformer (big) scores 28.4 BLEU, more than 2.0 above the best previously reported models including ensembles, after 3.5 days on 8 P100s. The base model (27.3) also surpasses all previously published models and ensembles.
- EN-FR: the text of this section reports a BLEU of 41.0 (the abstract and Table 2 give 41.8); the big model beats all previously published single models at less than 1/4 the training cost of the previous state of the art. It used $P_{drop}=0.1$ instead of 0.3.
- Decoding: base models average the last 5 checkpoints (10 minutes apart), big models the last 20. Beam search with beam size 4 and length penalty $\alpha=0.6$. Maximum output length is input length + 50, ending early when possible.
- FLOPs estimate: training time × number of GPUs × estimated sustained single-precision capacity (2.8, 3.7, 6.0, 9.5 TFLOPS for K80, K40, M40, P100).

**Table 2** (selected) (p. 8): BLEU EN-DE / EN-FR and training cost in FLOPs.

| Model | EN-DE | EN-FR | Cost EN-DE | Cost EN-FR |
|---|---|---|---|---|
| ConvS2S ensemble | 26.36 | 41.29 | $7.7\cdot10^{19}$ | $1.2\cdot10^{21}$ |
| GNMT + RL ensemble | 26.30 | 41.16 | $1.8\cdot10^{20}$ | $1.1\cdot10^{21}$ |
| Transformer (base) | 27.3 | 38.1 | $3.3\cdot10^{18}$ | (same) |
| Transformer (big) | 28.4 | 41.8 | $2.3\cdot10^{19}$ | (same) |

**6.2 Model variations (p. 9, Table 3).** Evaluated on the newstest2013 development set with beam search and no checkpoint averaging. Perplexities are per word-piece and not comparable to per-word perplexities. Base: PPL 4.92, BLEU 25.8, 65M parameters.
- (A) Varying heads at constant computation: $h=1$ gives 24.9 BLEU, $h=4$ 25.5, $h=16$ 25.8, $h=32$ 25.4. Single-head is 0.9 BLEU worse than the best setting. Quality also drops with too many heads.
- (B) Reducing $d_k$ hurts: $d_k=16$ gives 25.1, $d_k=32$ gives 25.4. The authors read this as suggesting that compatibility is not easy to determine, so a more sophisticated function than the dot product may help.
- (C, D) Bigger models are better, as expected (e.g. $d_{\text{model}}=1024$: 26.0; $d_{ff}=4096$: 26.2). Dropout helps against over-fitting ($P_{drop}=0.0$: 24.6). Label smoothing $\epsilon_{ls}=0.0$ gives better PPL (4.67) but BLEU 25.3, while 0.2 gives BLEU 25.7.
- (E) Learned positional embeddings: 25.7 BLEU, nearly identical to base.
- Big model: $d_{\text{model}}=1024$, $d_{ff}=4096$, $h=16$, $P_{drop}=0.3$, 300K steps, 26.4 BLEU, 213M parameters.

**6.3 English constituency parsing (pp. 9–10).**
- Task challenges: output has strong structural constraints and is significantly longer than the input. RNN seq2seq models had not reached state of the art in small-data regimes.
- Setup: 4-layer Transformer, $d_{\text{model}}=1024$, trained on WSJ (about 40K sentences) and semi-supervised (about 17M sentences). Vocabularies 16K and 32K. Only a small number of experiments to choose dropout, learning rates and beam size (Section 22 dev set); other parameters as the EN-DE base model. Inference: maximum output length input + 300, beam size 21, $\alpha=0.3$.
- **Table 4 (WSJ 23 F1):** Transformer 91.3 (WSJ only) and 92.7 (semi-supervised). Dyer et al. (generative) 93.3, Luong et al. (multi-task) 93.0, Dyer et al. (WSJ only, discriminative) 91.7.
- The authors say the model beats all previously reported models except the Recurrent Neural Network Grammar. It also outperforms the BerkeleyParser when trained only on the 40K WSJ sentences, unlike RNN seq2seq models. (p. 10)

### 7 Conclusion (p. 10)
The Transformer is, per the authors, the first sequence transduction model based entirely on attention. It trains significantly faster than recurrent or convolutional architectures for translation and sets new state of the art on both WMT 2014 tasks. Plans: other modalities (images, audio, video), local restricted attention, and less sequential generation. Code is released in tensor2tensor.

### Attention visualizations (pp. 13–15)
- Fig. 3: in encoder self-attention layer 5 of 6, many heads attend from "making" to the distant "more difficult", completing "making...more difficult". (p. 13)
- Fig. 4: two heads in layer 5 are "apparently involved in anaphora resolution". Attention from "its" is very sharp, pointing to "Law" and "application". (p. 14)
- Fig. 5: two heads show behaviour that "seems related" to sentence structure; the heads clearly learned different tasks. (p. 15)

## Toy example (ours, not from the text)
Take one query, two keys, $d_k=2$. $Q=[1,\;0]$, $K=\begin{bmatrix}1&0\\0&1\end{bmatrix}$, $V=\begin{bmatrix}2&0\\0&4\end{bmatrix}$.
1. $QK^T=[1\cdot1+0\cdot0,\;1\cdot0+0\cdot1]=[1,\;0]$.
2. Divide by $\sqrt2\approx1.4142$: $[0.7071,\;0]$.
3. Softmax: $e^{0.7071}\approx2.028$, $e^{0}=1$, sum $\approx3.028$. Weights $\approx[0.670,\;0.330]$.
4. Output $=0.670\cdot[2,0]+0.330\cdot[0,4]=[1.340,\;1.321]$.

Causal mask: if the second key were an illegal (future) position, its score is set to $-\infty$. Then $e^{-\infty}=0$, so the weights are $[1,0]$ and the output is $[2,0]$. The masked position contributes nothing.

## Concepts
- [[attention]] — weighted sum of values, weights from query–key compatibility (p. 3)
- [[self-attention]] — queries, keys and values all come from the same sequence (pp. 2, 5)
- [[scaled-dot-product-attention]] (new) — $\mathrm{softmax}(QK^T/\sqrt{d_k})V$ (p. 4)
- [[multi-head-attention]] — $h$ parallel attentions on learned projections, concatenated and projected (p. 4)
- [[softmax]] — turns compatibility scores into attention weights and output probabilities (pp. 4–5)
- [[causal-masking]] — setting illegal softmax inputs to $-\infty$ so position $i$ sees only earlier outputs (p. 5)
- [[positional-encoding]] — sinusoidal vectors added to embeddings to inject order (p. 6)
- [[feed-forward-mlp-block]] — per-position two-layer ReLU network, $d_{ff}=2048$ (p. 5)
- [[encoder-decoder-architecture]] (new) — encoder maps input to $z$; decoder generates outputs auto-regressively (p. 2)
- [[residual-connection-layer-norm]] (new) — each sub-layer outputs $\mathrm{LayerNorm}(x+\mathrm{Sublayer}(x))$ (p. 3)
- [[label-smoothing]] (new) — $\epsilon_{ls}=0.1$; hurts perplexity, improves accuracy and BLEU (p. 8)
- [[learning-rate-warmup]] (new) — linear increase for 4000 steps, then inverse-square-root decay (p. 7)
- [[tokenization-bpe]] — byte-pair and word-piece vocabularies used for translation (p. 7)
- [[perplexity]] — reported per word-piece in Table 3 (p. 9)

## Canonical instances
- [[wmt14-translation]] — EN-DE 28.4 BLEU, EN-FR 41.8 BLEU (p. 8)
- [[constituency-parsing-transformer]] — 91.3 F1 WSJ only, 92.7 semi-supervised (p. 10)
- [[making-more-difficult-attention]] — heads link "making" to "more difficult" (p. 13)
- [[anaphora-heads-its-law]] — sharp attention from "its" (p. 14)

## Bridges (candidates)
- [structural-analogy] Attention as soft key-value lookup ↔ databases: a query retrieves a weighted mix of stored values.
- [same-math] Variance of a sum of independent terms ↔ statistics: $\mathrm{Var}(\sum q_ik_i)=d_k$ under the footnote-4 assumptions (p. 4).
- [structural-analogy] Sinusoids of geometric wavelengths for position ↔ Fourier features: each dimension is a sinusoid of a different frequency.
- [metaphor] Attention heads as specialists ↔ cognitive science: "different tasks" per head (p. 15), loosely like specialized modules.

## Questions this raises
- Does the $O(n^2 d)$ cost of full self-attention become the limit for very long inputs, and how well does restricted attention ($O(n/r)$ path length) work?
- The authors observe that reducing $d_k$ hurts quality, which they say suggests a more sophisticated compatibility function than the dot product may help (p. 9). What would that function be?
- Do the visualized heads (Figs. 3–5) causally implement syntax and anaphora, or do they only correlate with them?
- Could the same architecture work for modalities other than text, as the authors plan (p. 10)?

## Reading notes
- Printed page = pdf page (offset 0). Footnotes on p. 1 give author contribution notes (listing order random).
- Version printed: arXiv:1706.03762v7, 2 Aug 2023; the page-1 footer says NIPS 2017.
- Inconsistency in the source: the abstract and Table 2 give 41.8 BLEU for EN-FR. Section 6.1 (p. 8) says 41.0. Table 2 bolds 41.8.
- Section 5.1 cites [3] for byte-pair encoding, whereas Section 4 cites [31]. Reference [3] in the list is Britz et al.
- Figures 4 and 5 are rotated in the pages. Their text layers were garbled, so only captions and images were used.
- Table 3 omits unchanged values. In row (D), 0.0 and 0.2 appear under $P_{drop}$ first, then under $\epsilon_{ls}$.
- The paper contains no exercises.
