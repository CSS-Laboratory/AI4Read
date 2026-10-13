---
id: vaswani-2017-transformer/main
work: vaswani-2017-transformer
unit: paper
pages: 1-15
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-13
---

# Attention Is All You Need (Vaswani et al., 2017)

## L0 — One line
A sequence model built only from attention and position-wise feed-forward layers (the Transformer), with no recurrence and no convolution, translates better than recurrent and convolutional models and trains much faster because it parallelizes across positions.

## L1 — The gist (≤ 120 words)
Before this paper, the best sequence-to-sequence models used recurrent or convolutional networks, often with attention added on top. Recurrence must process positions one after another, which limits parallelism (p. 2). The authors ask whether attention alone is enough. Their Transformer stacks multi-head self-attention and feed-forward layers in an encoder-decoder design. Sinusoidal positional encodings supply word order (p. 3, 6). It reaches 28.4 BLEU on WMT14 English–German and 41.8 on English–French. It trains in 12 hours (base) to 3.5 days (big) on 8 GPUs and also works for constituency parsing (p. 1, 8, 10). This design became the base architecture for later language models.

## L2 — Key ideas (5–10 bullets)
- **Recurrence is the bottleneck.** Recurrent models compute $h_t$ from $h_{t-1}$, so they cannot be parallelized within a training example. This hurts most for long sequences (p. 2).
- **Scaled dot-product attention** is $\mathrm{softmax}(QK^T/\sqrt{d_k})V$ (Eq. 1). The scaling keeps dot products from growing with $d_k$ and pushing softmax into regions with tiny gradients (p. 4).
- **Multi-head attention** runs $h=8$ attention operations in parallel in learned subspaces ($d_k=d_v=64$). This restores the resolution lost by averaging, at about the same cost as one full-width head (p. 4–5).
- **Three uses of attention:** encoder-decoder attention, encoder self-attention, and masked decoder self-attention. The mask sets illegal softmax inputs to $-\infty$ to keep the model autoregressive (p. 5).
- **Order must be injected.** Attention is blind to position, so sinusoidal positional encodings are added to the embeddings. Learned positional embeddings gave nearly identical results (p. 6, 9).
- **Why self-attention (Table 1):** any two positions are linked in $O(1)$ sequential operations and path length. The price is $O(n^2 d)$ cost per layer, which is cheaper than recurrence when $n<d$ (p. 6–7).
- **Results:** a new state of the art on WMT14 En–De (28.4 BLEU) and a single-model best on En–Fr (41.8). Training cost is a fraction of earlier systems (p. 8).
- **Ablations (Table 3):** one head is 0.9 BLEU worse than the best setting, and too many heads also hurt. Smaller $d_k$ hurts, bigger models help, and dropout is very helpful (p. 9).
- **Generalization:** a 4-layer Transformer gets 91.3 F1 (WSJ only) and 92.7 F1 (semi-supervised) on parsing with almost no task-specific tuning (p. 9–10).

## L3 — Walkthrough

### Abstract and 1 Introduction (p. 1–2)
- The dominant transduction models (models that map one sequence to another) use recurrent or convolutional networks with an encoder and a decoder. The best also connect encoder and decoder through attention (p. 1).
- Recurrent models factor computation along symbol positions. They produce hidden states $h_t$ as a function of $h_{t-1}$ and the input at position $t$. This "inherently sequential nature precludes parallelization within training examples" (p. 2).
  - Memory limits batching across examples, so this matters most for long sequences (p. 2).
  - Factorization tricks and conditional computation help, but "the fundamental constraint of sequential computation" remains (p. 2).
- Attention lets a model relate positions regardless of distance. Before this work it was almost always combined with an RNN (p. 2).
- Claim: the Transformer relies entirely on attention to draw global dependencies between input and output. It reaches a new state of the art after as little as twelve hours on eight P100 GPUs (p. 2).

**Intuition note.** The paper is mainly an engineering argument. Remove the step-by-step dependence, and every position can be computed at once on parallel hardware.

### 2 Background (p. 2)
- Extended Neural GPU, ByteNet and ConvS2S also try to reduce sequential computation using convolutions over all positions in parallel (p. 2).
- In those models, the operations needed to relate two positions grow with their distance: linearly for ConvS2S and logarithmically for ByteNet. This makes distant dependencies harder to learn (p. 2).
- In the Transformer this is a constant number of operations. The cost is lower effective resolution, because attention-weighted positions are averaged. Multi-head attention counteracts this (p. 2).
- Self-attention (intra-attention) relates different positions of a single sequence to compute a representation of it. It had already been used in reading comprehension, summarization, entailment and sentence representations (p. 2).
- End-to-end memory networks use a recurrent attention mechanism (p. 2).
- Claimed novelty: the first transduction model relying entirely on self-attention, with no sequence-aligned RNNs or convolution (p. 2).

### 3 Model Architecture (p. 2–3)
- Most competitive models are encoder-decoder. The encoder maps input symbols $(x_1,\dots,x_n)$ to continuous representations $z=(z_1,\dots,z_n)$. The decoder generates $(y_1,\dots,y_m)$ one element at a time (p. 2).
- At each step the model is auto-regressive: it consumes previously generated symbols as extra input (p. 2).
- The Transformer uses stacked self-attention and point-wise fully connected layers in both halves (Figure 1, p. 3). In Figure 1, the output embedding is "shifted right". The top of the decoder has a Linear layer and a Softmax producing output probabilities (p. 3).

#### 3.1 Encoder and Decoder Stacks (p. 3)
- **Encoder:** $N=6$ identical layers. Each has two sub-layers: multi-head self-attention, then a position-wise feed-forward network (p. 3).
- Each sub-layer has a residual connection followed by layer normalization:
$$\text{output} = \mathrm{LayerNorm}\big(x + \mathrm{Sublayer}(x)\big)$$
(p. 3).
- To make the residual sums possible, all sub-layers and the embedding layers output dimension $d_{\text{model}}=512$ (p. 3).
- **Decoder:** also $N=6$ identical layers. It adds a third sub-layer: multi-head attention over the encoder output. Residuals and layer norm are used as in the encoder (p. 3).
- The decoder self-attention is modified so positions cannot attend to later positions. Together with output embeddings offset by one position, the prediction for position $i$ depends only on known outputs at positions $<i$ (p. 3).

**Intuition note.** Each sub-layer reads $x$ and adds a correction to it. The 512-dimensional vector per position is passed upward and refined layer by layer.

#### 3.2 Attention (p. 3–5)
- An attention function maps a query and a set of key-value pairs to an output; all are vectors. The output is a weighted sum of the values. Each weight comes from a compatibility function of the query with the matching key (p. 3–4).

**3.2.1 Scaled Dot-Product Attention (p. 4).**
- Inputs: queries and keys of dimension $d_k$, values of dimension $d_v$. Take dot products of the query with all keys, divide by $\sqrt{d_k}$, apply softmax to get weights on the values (p. 4).
- For many queries at once, pack them into matrices $Q$, $K$, $V$:
$$\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{T}}{\sqrt{d_k}}\right)V \tag{1}$$
- The two common attention functions are additive attention (a one-hidden-layer feed-forward network as the compatibility function) and dot-product attention. Dot-product attention is identical to Eq. 1 except for the factor $1/\sqrt{d_k}$ (p. 4).
- Both have similar theoretical complexity. Dot-product attention is faster and more space-efficient in practice because it uses optimized matrix multiplication (p. 4).
- For small $d_k$ the two perform similarly. For larger $d_k$, additive attention beats unscaled dot-product attention. The authors suspect large dot products push softmax into regions with extremely small gradients, so they scale by $1/\sqrt{d_k}$ (p. 4).
- Footnote 4: if components of $q$ and $k$ are independent with mean 0 and variance 1, then $q\cdot k=\sum_{i=1}^{d_k} q_i k_i$ has mean 0 and variance $d_k$ (p. 4).
  - (added step) Dividing by $\sqrt{d_k}$ therefore gives the scaled score variance $d_k/d_k = 1$.

**Intuition note.** Attention is a soft lookup. The query is compared to every key, the similarities become probabilities, and the output blends the values using those probabilities. The $\sqrt{d_k}$ keeps the similarities in a range where softmax can still learn.

**3.2.2 Multi-Head Attention (p. 4–5).**
- Instead of one attention with $d_{\text{model}}$-dimensional keys, values and queries, project them $h$ times with different learned linear maps to $d_k$, $d_k$, $d_v$ dimensions. Run attention on each projection in parallel, concatenate the $d_v$-dimensional outputs, and project again (p. 4–5).
- Purpose: to attend jointly to information from different representation subspaces at different positions. "With a single attention head, averaging inhibits this" (p. 5).
$$\mathrm{MultiHead}(Q,K,V)=\mathrm{Concat}(\mathrm{head}_1,\dots,\mathrm{head}_h)W^{O}$$
$$\text{where } \mathrm{head}_i=\mathrm{Attention}(QW_i^{Q},KW_i^{K},VW_i^{V})$$
- Projections: $W_i^{Q}\in\mathbb{R}^{d_{\text{model}}\times d_k}$, $W_i^{K}\in\mathbb{R}^{d_{\text{model}}\times d_k}$, $W_i^{V}\in\mathbb{R}^{d_{\text{model}}\times d_v}$, $W^{O}\in\mathbb{R}^{hd_v\times d_{\text{model}}}$ (p. 5).
- The paper uses $h=8$ and $d_k=d_v=d_{\text{model}}/h=64$. Because each head is smaller, total cost is similar to single-head attention at full dimension (p. 5).

**3.2.3 Applications of Attention in our Model (p. 5).**
- *Encoder-decoder attention:* queries come from the previous decoder layer. Keys and values come from the encoder output. Every decoder position can attend over all input positions (p. 5).
- *Encoder self-attention:* queries, keys and values all come from the previous encoder layer. Every position attends to all positions (p. 5).
- *Decoder self-attention:* each position attends to all decoder positions up to and including itself. Leftward information flow is blocked to keep the auto-regressive property. This is done inside scaled dot-product attention by setting illegal softmax inputs to $-\infty$ (p. 5).

**Intuition note.** Several small heads can each look for a different relation, such as the previous word, a related noun, or a bracket. One big head would have to average all of these into one pattern.

#### 3.3 Position-wise Feed-Forward Networks (p. 5)
- Each layer has a fully connected network applied to each position separately and identically: two linear maps with a ReLU between them.
$$\mathrm{FFN}(x)=\max(0,\,xW_1+b_1)W_2+b_2 \tag{2}$$
- The same parameters are used across positions but differ from layer to layer. It can also be seen as two convolutions with kernel size 1. Input and output dimension is $d_{\text{model}}=512$ and the inner layer has $d_{ff}=2048$ (p. 5).

#### 3.4 Embeddings and Softmax (p. 5)
- Learned embeddings map input and output tokens to $d_{\text{model}}$-dimensional vectors. A learned linear map plus softmax converts decoder output to next-token probabilities (p. 5).
- The same weight matrix is shared between the two embedding layers and the pre-softmax linear map. In the embedding layers, the weights are multiplied by $\sqrt{d_{\text{model}}}$ (p. 5).

#### 3.5 Positional Encoding (p. 6)
- Without recurrence or convolution, the model needs information about the relative or absolute position of tokens. Positional encodings of dimension $d_{\text{model}}$ are added to the input embeddings at the bottom of the encoder and decoder stacks (p. 6).
$$PE_{(pos,2i)}=\sin\!\big(pos/10000^{2i/d_{\text{model}}}\big),\qquad PE_{(pos,2i+1)}=\cos\!\big(pos/10000^{2i/d_{\text{model}}}\big)$$
- Each dimension is a sinusoid. Wavelengths form a geometric progression from $2\pi$ to $10000\cdot 2\pi$ (p. 6).
- Motivation: for any fixed offset $k$, $PE_{pos+k}$ is a linear function of $PE_{pos}$, so attending by relative position should be easy to learn (p. 6).
  - (added step) This follows from $\sin(a+b)=\sin a\cos b+\cos a\sin b$ and the matching cosine identity. For each frequency $\omega_i$, the pair $(\sin,\cos)$ at $pos+k$ is a fixed $2\times2$ rotation (depending only on $k$) of the pair at $pos$.
- Learned positional embeddings gave nearly identical results (Table 3 row (E)). Sinusoids were chosen because they may extrapolate to longer sequences than seen in training (p. 6).

### 4 Why Self-Attention (p. 6–7)
- The comparison covers layers that map $(x_1,\dots,x_n)$ to $(z_1,\dots,z_n)$ with $x_i,z_i\in\mathbb{R}^d$. There are three desiderata: (1) computational complexity per layer, (2) parallelizable computation, measured as the minimum number of sequential operations, and (3) path length between long-range dependencies (p. 6).
- Shorter paths for forward and backward signals make long-range dependencies easier to learn (p. 6).

**Table 1** ($n$ = sequence length, $d$ = representation dimension, $k$ = kernel size, $r$ = neighbourhood size in restricted self-attention) (p. 6):

| Layer type | Complexity per layer | Sequential ops | Max path length |
|---|---|---|---|
| Self-attention | $O(n^2 d)$ | $O(1)$ | $O(1)$ |
| Recurrent | $O(n d^2)$ | $O(n)$ | $O(n)$ |
| Convolutional | $O(k n d^2)$ | $O(1)$ | $O(\log_k n)$ |
| Self-attention (restricted) | $O(r n d)$ | $O(1)$ | $O(n/r)$ |

- Self-attention is faster than recurrent layers when $n<d$. This is most often true for word-piece and byte-pair representations (p. 6–7).
- For very long sequences, self-attention could be restricted to a neighbourhood of size $r$. This raises the maximum path length to $O(n/r)$. It is left for future work (p. 7).
- A single convolution with $k<n$ does not connect all pairs. Connecting all needs $O(n/k)$ layers (contiguous kernels) or $O(\log_k n)$ (dilated convolutions) (p. 7).
- Convolutions are more expensive than recurrent layers by a factor of $k$. Separable convolutions cut the cost to $O(k\cdot n\cdot d+n\cdot d^2)$. Even at $k=n$ this equals self-attention plus a point-wise feed-forward layer, which is the Transformer's choice (p. 7).
- Side benefit: possibly more interpretable models. Individual heads learn different tasks and many seem related to syntactic and semantic structure (p. 7; see the attention visualizations below).

**Intuition note.** Self-attention pays a quadratic price in length $n$ (every pair is compared). In return, any two words are one step apart and all steps run in parallel.

### 5 Training (p. 7–8)

#### 5.1 Training Data and Batching (p. 7)
- WMT 2014 English–German: about 4.5M sentence pairs, byte-pair encoding, shared source–target vocabulary of about 37,000 tokens (p. 7).
- WMT 2014 English–French: 36M sentences, 32,000 word-piece vocabulary (p. 7).
- Batches grouped by approximate length: about 25,000 source tokens and 25,000 target tokens each (p. 7).

#### 5.2 Hardware and Schedule (p. 7)
- One machine with 8 NVIDIA P100 GPUs. Base model: about 0.4 s per step, 100,000 steps, 12 hours. Big model: 1.0 s per step, 300,000 steps, 3.5 days (p. 7).

#### 5.3 Optimizer (p. 7)
- Adam with $\beta_1=0.9$, $\beta_2=0.98$, $\epsilon=10^{-9}$. The learning rate varies as
$$lrate = d_{\text{model}}^{-0.5}\cdot\min\!\big(step\_num^{-0.5},\; step\_num\cdot warmup\_steps^{-1.5}\big) \tag{3}$$
- It rises linearly for the first $warmup\_steps$ steps and then falls with the inverse square root of the step number. $warmup\_steps=4000$ (p. 7).

#### 5.4 Regularization (p. 7–8)
- Three types are announced (p. 7). Two are described on p. 8. A third item is not separately labelled in the text (see Reading notes).
- *Residual dropout:* dropout is applied to each sub-layer output before it is added to the sub-layer input and normalized. It is also applied to the sums of embeddings and positional encodings. Base rate $P_{drop}=0.1$ (p. 8).
- *Label smoothing:* $\epsilon_{ls}=0.1$. This hurts perplexity because the model learns to be more unsure, but improves accuracy and BLEU (p. 8).

### 6 Results (p. 8–10)

#### 6.1 Machine Translation (p. 8)
- **En→De:** Transformer (big) gets 28.4 BLEU, more than 2.0 above the best earlier models including ensembles. It trained 3.5 days on 8 P100s. Even the base model beats all earlier models and ensembles, at a fraction of the cost (p. 8).
- **En→Fr:** the big model gets a BLEU score stated as 41.0 in the text (Table 2 and the abstract say 41.8). It outperforms all earlier single models at less than 1/4 the training cost of the previous best. It used dropout 0.1 instead of 0.3 (p. 8).
- Inference setup:
  - Base models average the last 5 checkpoints, written at 10-minute intervals. Big models average the last 20 (p. 8).
  - Beam search with beam size 4 and length penalty $\alpha=0.6$. Maximum output length is input length + 50, with early termination when possible (p. 8).
- Training FLOPs are estimated as training time × number of GPUs × sustained single-precision capacity per GPU. The values used are 2.8, 3.7, 6.0 and 9.5 TFLOPS for K80, K40, M40, P100 (p. 8).

**Table 2** (selected rows; BLEU EN-DE / EN-FR; FLOPs EN-DE / EN-FR) (p. 8):

| Model | BLEU EN-DE | BLEU EN-FR | FLOPs EN-DE | FLOPs EN-FR |
|---|---|---|---|---|
| ByteNet | 23.75 | – | – | – |
| GNMT + RL | 24.6 | 39.92 | $2.3\cdot10^{19}$ | $1.4\cdot10^{20}$ |
| ConvS2S | 25.16 | 40.46 | $9.6\cdot10^{18}$ | $1.5\cdot10^{20}$ |
| MoE | 26.03 | 40.56 | $2.0\cdot10^{19}$ | $1.2\cdot10^{20}$ |
| GNMT + RL Ensemble | 26.30 | 41.16 | $1.8\cdot10^{20}$ | $1.1\cdot10^{21}$ |
| ConvS2S Ensemble | 26.36 | 41.29 | $7.7\cdot10^{19}$ | $1.2\cdot10^{21}$ |
| Transformer (base) | 27.3 | 38.1 | $3.3\cdot10^{18}$ (both) | |
| Transformer (big) | 28.4 | 41.8 | $2.3\cdot10^{19}$ (both) | |

**Intuition note.** The big model matches or beats ensembles of the best systems in BLEU. Its compute is $2.3\cdot10^{19}$ FLOPs, versus $7.7\cdot10^{19}$ to $1.8\cdot10^{20}$ for the En–De ensembles in the table (p. 8).

#### 6.2 Model Variations (p. 8–9)
- The base model is varied on English–German, newstest2013 development set, with beam search but no checkpoint averaging. Perplexities are per word-piece and "should not be compared to per-word perplexities" (p. 9).

**Table 3** (columns: N, $d_{\text{model}}$, $d_{ff}$, h, $d_k$, $d_v$, $P_{drop}$, $\epsilon_{ls}$, steps, PPL, BLEU, params ×10⁶; only changed values shown) (p. 9):

| Row | Change | PPL | BLEU | Params |
|---|---|---|---|---|
| base | N=6, 512, 2048, h=8, 64, 64, 0.1, 0.1, 100K | 4.92 | 25.8 | 65 |
| (A) | h=1, $d_k$=$d_v$=512 | 5.29 | 24.9 | |
| (A) | h=4, 128 | 5.00 | 25.5 | |
| (A) | h=16, 32 | 4.91 | 25.8 | |
| (A) | h=32, 16 | 5.01 | 25.4 | |
| (B) | $d_k$=16 | 5.16 | 25.1 | 58 |
| (B) | $d_k$=32 | 5.01 | 25.4 | 60 |
| (C) | N=2 | 6.11 | 23.7 | 36 |
| (C) | N=4 | 5.19 | 25.3 | 50 |
| (C) | N=8 | 4.88 | 25.5 | 80 |
| (C) | $d_{\text{model}}$=256, $d_k$=$d_v$=32 | 5.75 | 24.5 | 28 |
| (C) | $d_{\text{model}}$=1024, $d_k$=$d_v$=128 | 4.66 | 26.0 | 168 |
| (C) | $d_{ff}$=1024 | 5.12 | 25.4 | 53 |
| (C) | $d_{ff}$=4096 | 4.75 | 26.2 | 90 |
| (D) | $P_{drop}$=0.0 | 5.77 | 24.6 | |
| (D) | $P_{drop}$=0.2 | 4.95 | 25.5 | |
| (D) | $\epsilon_{ls}$=0.0 | 4.67 | 25.3 | |
| (D) | $\epsilon_{ls}$=0.2 | 5.47 | 25.7 | |
| (E) | positional embedding instead of sinusoids | 4.92 | 25.7 | |
| big | N=6, 1024, 4096, h=16, $P_{drop}$=0.3, 300K | 4.33 | 26.4 | 213 |

- Rows (A): head count and $d_k$, $d_v$ are varied at constant computation. Single-head attention is 0.9 BLEU worse than the best setting. Quality also drops with too many heads (p. 9).
- Rows (B): reducing $d_k$ hurts quality. This suggests that judging compatibility is not easy and a more sophisticated function than the dot product may help (p. 9).
- Rows (C), (D): bigger models are better, and dropout is very helpful against over-fitting (p. 9).
- Row (E): learned positional embeddings give nearly identical results (p. 9).

**Intuition note.** Heads, key size, depth and width all matter, and the base setting sits near the sweet spot. Dropout is the one regularizer whose removal clearly hurts (24.6 vs 25.8 BLEU).

#### 6.3 English Constituency Parsing (p. 9–10)
- Purpose: test generalization. Parsing has strong structural output constraints and output much longer than input. RNN seq2seq models had not reached state of the art in small-data regimes (p. 9).
- Setup:
  - A 4-layer Transformer with $d_{\text{model}}=1024$, trained on the WSJ part of the Penn Treebank (about 40K sentences) (p. 9).
  - A semi-supervised setting uses high-confidence and BerkeleyParser corpora of about 17M sentences. Vocabulary is 16K tokens (WSJ only) or 32K (semi-supervised) (p. 9).
  - Only a small number of experiments tuned dropout, learning rates and beam size on the Section 22 development set. Other parameters stayed as in the En–De base model (p. 9).
  - At inference, maximum output length is input length + 300, beam size 21, $\alpha=0.3$ (p. 10).

**Table 4** (WSJ 23 F1) (p. 10):

| Parser | Training | F1 |
|---|---|---|
| Vinyals & Kaiser et al. (2014) | WSJ only, discriminative | 88.3 |
| Petrov et al. (2006) | WSJ only, discriminative | 90.4 |
| Zhu et al. (2013) | WSJ only, discriminative | 90.4 |
| Dyer et al. (2016) | WSJ only, discriminative | 91.7 |
| **Transformer (4 layers)** | WSJ only, discriminative | 91.3 |
| Zhu et al. (2013) | semi-supervised | 91.3 |
| Huang & Harper (2009) | semi-supervised | 91.3 |
| McClosky et al. (2006) | semi-supervised | 92.1 |
| Vinyals & Kaiser et al. (2014) | semi-supervised | 92.1 |
| **Transformer (4 layers)** | semi-supervised | 92.7 |
| Luong et al. (2015) | multi-task | 93.0 |
| Dyer et al. (2016) | generative | 93.3 |

- The authors say the Transformer is better than all earlier models except the Recurrent Neural Network Grammar (p. 10).
- Unlike RNN seq2seq models, it beats the BerkeleyParser even when trained only on the 40K-sentence WSJ set (p. 10).

### 7 Conclusion (p. 10)
- The Transformer is presented as the first sequence transduction model based entirely on attention. It replaces the recurrent layers of encoder-decoders with multi-headed self-attention (p. 10).
- It trains significantly faster than recurrent or convolutional architectures and sets a new state of the art on both WMT14 tasks (p. 10).
- Future plans: other modalities (images, audio, video), local restricted attention for large inputs, and "making generation less sequential" (p. 10). Code is at tensor2tensor (p. 10).

### Attention Visualizations (appendix, p. 13–15)
- **Figure 3 (p. 13):** in encoder self-attention at layer 5 of 6, many heads attend from the verb "making" to the distant word "difficult", completing the phrase "making...more difficult". Only attention from "making" is shown. Colours represent heads.
- **Figure 4 (p. 14):** two heads in layer 5 appear to be involved in anaphora resolution (linking a pronoun to what it refers to). Top: full attentions for head 5. Bottom: attentions from just the word "its" for heads 5 and 6. The attentions are very sharp for this word. In the image, "its" attends to "Law" and "application".
- **Figure 5 (p. 15):** two different heads at layer 5 show behaviour that seems related to sentence structure. "The heads clearly learned to perform different tasks."

**Intuition note.** These pictures are qualitative evidence only. The paper offers them as examples that heads specialize. It does not measure how often this happens.

## Toy example
*(Ours, not from the paper.)* One query, three positions, $d_k=4$, 2-dimensional values.

Setup: $q=(1,1,1,1)$; keys $k_1=(2,2,0,0)$, $k_2=(0,0,1,1)$, $k_3=(-1,0,0,0)$; values $v_1=(1,0)$, $v_2=(0,1)$, $v_3=(1,1)$.

1. Dot products: $q\cdot k_1=2+2=4$; $q\cdot k_2=1+1=2$; $q\cdot k_3=-1$.
2. Scale by $\sqrt{d_k}=2$: $2,\;1,\;-0.5$.
3. Softmax: $e^{2}=7.389$, $e^{1}=2.718$, $e^{-0.5}=0.6065$. Sum $=10.714$. Weights: $7.389/10.714=0.6897$; $2.718/10.714=0.2537$; $0.6065/10.714=0.0566$. They sum to 1.0000.
4. Output $=0.6897\,v_1+0.2537\,v_2+0.0566\,v_3=(0.6897+0.0566,\;0.2537+0.0566)=(0.7463,\;0.3103)$.

Without scaling: scores $4,2,-1$ give $e^4=54.598$, $e^2=7.389$, $e^{-1}=0.3679$. Sum $=62.355$. Weights: $0.8756$, $0.1185$, $0.0059$. The weights are much sharper. With larger $d_k$ the effect grows, which is the saturation problem of p. 4.

Causal mask: if position 3 is "in the future", set its score to $-\infty$. Then $e^{-\infty}=0$ and the weights are $7.389/(7.389+2.718)=7.389/10.107=0.7311$ and $0.2689$ for positions 1 and 2. The weights still sum to 1 (p. 5 describes the masking).

Learning-rate schedule (Eq. 3), $d_{\text{model}}=512$, $warmup\_steps=4000$:
- $512^{-0.5}=0.04419$.
- At step 4000, both terms of the min are equal: $4000^{-0.5}=0.015811$. So $lrate=0.04419\times0.015811=6.99\times10^{-4}$.
- At step 1000, the warm-up term is $1000\times4000^{-1.5}=1000\times3.9528\times10^{-6}=3.9528\times10^{-3}$. So $lrate=0.04419\times3.9528\times10^{-3}=1.75\times10^{-4}$, which is a quarter of the peak, as expected for a linear ramp.

## Concepts
- [[attention]] — a weighted sum of values, with weights from a compatibility function of a query with each key (p. 3–4)
- [[self-attention]] — attention where queries, keys and values all come from the same sequence (p. 2, 5)
- [[multi-head-attention]] — $h$ attention operations in learned subspaces, concatenated and projected (p. 4–5)
- [[softmax]] — turns scaled dot-product scores into weights on values, and decoder output into next-token probabilities (p. 4, 5)
- [[positional-encoding]] — sinusoids added to embeddings to inject order into an order-blind model (p. 6)
- [[causal-masking]] — setting illegal softmax inputs to $-\infty$ so position $i$ sees only earlier positions (p. 3, 5)
- [[residual-stream]] — the residual connection $\mathrm{LayerNorm}(x+\mathrm{Sublayer}(x))$ around every sub-layer, with all dimensions equal to $d_{\text{model}}$ (p. 3). The paper does not use the term "residual stream".
- [[feed-forward-mlp-block]] — the position-wise two-layer ReLU network, Eq. 2 (p. 5)
- [[tokenization-bpe]] — byte-pair (≈37K shared) and word-piece (32K) vocabularies for translation (p. 7)
- [[perplexity]] — reported per word-piece in Table 3; label smoothing worsens it (p. 8, 9)
- [[cross-entropy-log-loss]] — only implicit: the model outputs next-token probabilities via softmax (p. 5). Not named in the paper.
- [[encoder-only-decoder-only]] — the paper uses the full encoder-decoder, with a masked decoder (p. 2–3)
- [[language-model]] — the decoder predicts next-token probabilities autoregressively (p. 2, 5)
- [[label-smoothing]] (new) — $\epsilon_{ls}=0.1$; trades perplexity for accuracy and BLEU (p. 8)
- [[layer-normalization]] (new) — normalization applied after each residual sum (p. 3)
- [[learning-rate-warmup]] (new) — linear increase then inverse-square-root decay, Eq. 3 (p. 7)
- [[beam-search]] (new) — decoding with beam size 4 (translation) or 21 (parsing) and a length penalty (p. 8, 10)
- [[path-length-and-parallelism-tradeoff]] (new) — Table 1 comparison of layer types by complexity, sequential operations and path length (p. 6)

## Canonical instances
- [[wmt14-en-de-translation]] (new) — 28.4 BLEU for the big model, 27.3 for the base (p. 8)
- [[wmt14-en-fr-translation]] (new) — 41.8 BLEU (Table 2; text says 41.0) for the big model (p. 8)
- [[wsj-constituency-parsing]] (new) — 91.3 F1 (WSJ only), 92.7 F1 (semi-supervised) (p. 10)
- [[long-distance-dependency-head]] (new) — layer-5 heads linking "making" to "more difficult" (p. 13)
- [[anaphora-resolution-head]] (new) — heads linking "its" to "Law" and "application" (p. 14)

## Bridges (candidates)
- [structural-analogy] Attention as soft key-value lookup ↔ nonparametric regression: output is a similarity-weighted average of stored values — the weights come from a learned similarity function.
- [same-math] Dividing scores by $\sqrt{d_k}$ before softmax ↔ temperature scaling of a softmax / Boltzmann distribution — the same operation $\mathrm{softmax}(x/T)$ with a fixed $T=\sqrt{d_k}$.
- [structural-analogy] Sinusoidal positional encoding ↔ Fourier features: a bank of sines and cosines at geometrically spaced frequencies, where shifts act as rotations.
- [structural-analogy] Full self-attention over $n$ tokens ↔ message passing on a complete graph with learned, input-dependent edge weights (network science).
- [metaphor] Heads specializing in different relations (Fig. 3–5) ↔ linguistics: separate grammatical "modules" for agreement, coreference, and phrase structure.
- [structural-analogy] Path length $O(1)$ vs $O(n)$ (Table 1) ↔ small-world networks: shortcuts reduce the distance between any two nodes.

## Questions this raises
- The paper hopes a more sophisticated compatibility function than the dot product may help (p. 9). Does that hold, and how do the cost and quality trade off?
- Self-attention costs $O(n^2 d)$. How do the restricted $O(r\,n\,d)$ variants (p. 6–7) behave on very long inputs?
- Do attention maps like Figures 3–5 actually explain what the model computes, or are they only correlated with it? The paper shows examples only.
- The paper ends with a full encoder-decoder. What changes if one uses only the masked decoder, or only the encoder, for language modelling?

## Reading notes
- The text layer is clean for prose and equations. I checked Eq. 1, Eq. 2, Eq. 3, the multi-head formulas, the positional-encoding formulas and the tables against the page images. The images match the text.
- The text layer of the appendix figures (pp. 13–15) is scrambled word lists. Only the images and captions are usable. Figure 3 is described from the image and caption.
- **Inconsistency:** Section 6.1 says the big En–Fr model gets "41.0" BLEU (p. 8). The abstract (p. 1) and Table 2 (p. 8) say 41.8. I reported 41.8 as the headline number.
- **Inconsistency:** the text on p. 10 says the Transformer beats all earlier parsers except the Recurrent Neural Network Grammar. Table 4 also lists Luong et al. multi-task (93.0), above the Transformer's 92.7. The WSJ-only discriminative Dyer et al. (91.7) is also above the Transformer's 91.3.
- Section 5.4 (p. 7) says "three types of regularization". Only residual dropout and label smoothing appear under headings on p. 8. The attention-dropout use mentioned in 6.3 (p. 9) may be the third. This is my guess, not stated in the text.
- Section 5.1 cites [3] for byte-pair encoding. Section 4 cites [31] for byte-pair. I did not verify the reference.
- Table 2's FLOPs cell for the Transformer rows is merged across the EN-DE and EN-FR columns, as in the image. The base cost is $3.3\cdot10^{18}$ and the big cost is $2.3\cdot10^{19}$.
- Table 4 has the misspelling "Vinyals & Kaiser el al." in the source; "BerkleyParser" on p. 9 is also misspelled.
- Section 3.2.1's footnote 4 is a heuristic argument assuming independent, zero-mean, unit-variance components. The authors say "we suspect" and give no experiment of their own on this (p. 4).
- The arXiv v7 version (2 Aug 2023) is used here. Page numbering is the arXiv one (p. 1–15), where pages 11–12 are references and pages 13–15 are the attention visualizations.