---
id: geva-2021-ffn/main
work: geva-2021-ffn
unit: paper
pages: 5484–5495
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Transformer Feed-Forward Layers Are Key-Value Memories

## L0 — One line
The feed-forward layers of a transformer language model behave like key-value memories: keys detect input patterns, values (mostly in the upper layers) push probability toward likely next tokens, and layer outputs are mixtures of many memories refined through the residual connections.

## L1 — The gist (≤ 120 words)
Feed-forward layers hold about two-thirds of a transformer's parameters, but their role was little studied. The authors note that such a layer has the same form as a key-value neural memory, except for the non-linearity. They test this in a 16-layer language model trained on WikiText-103. Keys fire on human-recognisable patterns: lower layers tend to show shallow ones (such as a shared last word), upper layers more semantic ones. In upper layers, values tend to assign higher probability to the token that follows the key's patterns. Each layer's output is usually a composition of many memories, not one dominant memory. The residual connections then refine the prediction layer by layer.

**Prerequisites:** matrix–vector products; softmax; ReLU; residual connections and layer normalisation in transformers; the idea of an output embedding matrix.

## L2 — Key ideas (5–10 bullets)
- A feed-forward layer $f(xK^\top)V$ has the same form as a key-value neural memory $\mathrm{softmax}(xK^\top)V$; only the non-linearity differs. Rows of $K$ are keys, rows of $V$ are values, $x$ is the input vector, and $d_m$ is the number of memories (p. 5485).
- Keys act as pattern detectors. Experts found at least one human-recognisable pattern for every sampled key (p. 5486).
- Lower layers (1–9) are dominated by shallow patterns, upper layers (10–16) by more semantic ones. Removing the last input token hurts a memory coefficient (how strongly a key's memory fires on an input) far more than removing the first (pp. 5486–5487).
- Projecting a value through the output embeddings gives a vocabulary distribution. Its top token agrees with the next token of the key's top trigger example (the training prefix that fires the key most) almost never in layers 1–10, but up to 3.5% by layer 16 (p. 5487).
- A typical example activates hundreds of memories per layer. In at least ~68% of cases the layer's top prediction differs from every memory's top prediction, so layer outputs are compositional (p. 5489).
- The residual stream (the vector carried from layer to layer, to which each layer adds its output) is refined sequentially: about a third of final predictions are already fixed in the bottom few layers, and the share grows rapidly from layer 10 (p. 5490).
- When a feed-forward layer changes the residual's top prediction, the result is usually a "compromise" equal to neither. The authors conjecture the layer may "veto" the residual's top candidate (p. 5491).

## L3 — Walkthrough

### 1 Introduction (pp. 5484–5485)
- Self-attention is well studied but has only $4d^2$ parameters per layer ($d$ = hidden dimension). Position-wise feed-forward layers have $8d^2$, about two-thirds of the parameters, and their role is under-explored (p. 5484).
- Claim: feed-forward layers emulate neural memories (Sukhbaatar et al., 2015). The first parameter matrix holds keys and the second holds values (p. 5484). Sukhbaatar et al. (2019) suggested the similarity before; this paper analyses what the memories store (p. 5484).
- Three findings are previewed (pp. 5484–5485):
  - Keys correlate with human-interpretable input patterns (n-grams or topics).
  - Values induce output-vocabulary distributions that correlate with the next-token distribution of the keys' patterns in upper layers.
  - Each layer combines hundreds of active memories into a distribution qualitatively different from its component values. The residual connection acts as a refinement mechanism.

### 2 Feed-forward layers as unnormalized key-value memories (p. 5485)
- A feed-forward layer processes each position independently. Input $x\in\mathbb R^d$ (a prefix representation, row vector). Bias terms are omitted. $K,V\in\mathbb R^{d_m\times d}$, and $f$ is a non-linearity such as ReLU:
$$\mathrm{FF}(x)=f(x\cdot K^\top)\cdot V \tag{1}$$
- (added step) Shapes: $xK^\top$ is $1\times d_m$, $V$ is $d_m\times d$, and the output is $1\times d$ (p. 5485).
- A neural memory has $d_m$ key-value pairs ("memories"), with keys $k_i\in\mathbb R^d$ stacked into $K$ and values into $V$. It computes a distribution over keys and an expected value (p. 5485):
$$p(k_i\mid x)\propto \exp(x\cdot k_i),\qquad \mathrm{MN}(x)=\sum_{i=1}^{d_m}p(k_i\mid x)\,v_i$$
$$\mathrm{MN}(x)=\mathrm{softmax}(x\cdot K^\top)\cdot V \tag{2}$$
- Comparing (1) and (2): the only difference is that neural memory uses softmax as $f$, while the canonical transformer uses no normalising function (p. 5485).
- $d_m$ is essentially the number of memories. The hidden layer $m=f(xK^\top)$ holds an unnormalised non-negative coefficient for each memory; $m_i$ is the *memory coefficient* of cell $i$ (p. 5485).
- Sukhbaatar et al. (2019) moved feed-forward parameters into attention as persistent memory. The authors say this does not tell us much about the canonical transformer (p. 5485).
- Conjecture (author): key $k_i$ captures a pattern or set of patterns in the input (Section 3), and value $v_i$ represents the distribution of tokens that follows the pattern (Section 4) (p. 5485).

*Intuition note:* Each hidden unit is one memory slot. Its key row decides how strongly the slot fires, and its value row is what the slot writes to the output. The layer output is the sum of the written values, weighted by the firing strengths.

### 3 Keys capture input patterns (pp. 5485–5487)
**3.1 Experiment.**
- Model: Baevski and Auli's 16-layer transformer LM on WikiText-103, with $d=1024$, $d_m=4096$, and $d_m\cdot16=65{,}536$ potential keys. The authors randomly sample 10 keys per layer, 160 in total (p. 5486).
- Trigger examples: for key $k_i^\ell$, compute the memory coefficient $\mathrm{ReLU}(x_j^\ell\cdot k_i^\ell)$ for every prefix $x_1,\dots,x_j$ of every training sentence. For "I love dogs" the prefixes are "I", "I love", "I love dogs". The top-$t$ prefixes by inner product are the *trigger examples* (p. 5486).
- Annotation: NLP graduate students annotated the top-25 prefixes of each key (one expert per key). They (a) identified patterns occurring in at least 3 prefixes, (b) described them, and (c) classified each as "shallow" (e.g. recurring n-grams) or "semantic" (recurring topic). A prefix may carry several patterns (p. 5486).
- Table 1 examples (p. 5486): $k^1_{449}$ ends with "substitutes" (shallow); $k^6_{2546}$ military, ends with "base"/"bases" (shallow + semantic); $k^{10}_{2997}$ a "part of" relation (semantic); $k^{13}_{2989}$ ends with a time range (semantic); $k^{16}_{1935}$ TV shows (semantic).

**3.2 Results.**
- Experts found at least one pattern for every key, 3.6 patterns per key on average. 65%–80% of retrieved prefixes were associated with at least one pattern (Figure 2) (pp. 5486–5487).
- Layers 1–9 are dominated by shallow patterns, often prefixes sharing the last word. Layers 10–16 show more semantic patterns without clear surface similarity. This matches earlier findings on contextual models (p. 5487).
- Perturbation test: 1600 random keys (100 per layer); for each key's top-50 trigger examples, remove the first, last or a random token and measure the change in memory coefficient (p. 5487).
- Figure 3: removing the last token reduces the coefficient much more than removing the first or a random token. From the plot, the last-token drop is roughly 50–70% (my reading of the figure). The authors read this as the model treating the end of the input as more salient for next-token prediction. In upper layers removing the last token has less impact, supporting the claim that upper-layer keys correlate less with shallow patterns (p. 5487).

*Intuition note:* Keys are not random directions. The text that most excites a key shares a visible pattern, such as the same last word or the same topic. That pattern becomes more abstract with depth.

### 4 Values represent distributions (pp. 5487–5488)
- Conversion: multiply each value by the output embedding matrix $E$ and apply softmax (the actual model uses adaptive softmax):
$$\mathbf p_i^\ell=\mathrm{softmax}(v_i^\ell\cdot E)$$
- $\mathbf p_i^\ell$ is uncalibrated, because in the real model $v_i^\ell$ is scaled by the input-dependent coefficient. Its ranking is invariant to that coefficient. The conversion naïvely assumes all layers share one embedding space (p. 5487).
- Agreement rate: the fraction of cells where $\mathrm{argmax}(\mathbf p_i^\ell)=w_i^\ell$, the next token after the key's top-1 trigger example (p. 5487).
- Figure 4: the rate is close to zero in layers 1–10 and rises quickly from layer 11 to 3.5%. This is orders of magnitude above the 0.0004% expected from a random token, so upper-layer memories show non-trivial predictive power (pp. 5487–5488).
- Figure 5: the rank of $w_i^\ell$ in the value's distribution improves toward upper layers (vocabulary ~270K tokens). The authors say $w_i^\ell$ tends to get higher probability there (p. 5488).
- Figure 6: values with higher maximal probability are more likely to agree. Among the 100 values with the highest top probability, 97 are in layers 11–16. For 46 of them, at least one of the key's top-50 trigger examples agrees with the value's top prediction (p. 5488).
- Table 2 (p. 5489), precision@50 = share of the key's top-50 trigger examples whose next token matches the value's top prediction:

| Value | Top prediction | Precision@50 |
|---|---|---|
| $v^{15}_{222}$ | each | 68% |
| $v^{15}_{881}$ | part | 92% |
| $v^{16}_{2070}$ | line | 84% |
| $v^{16}_{752}$ | played | 16% |
| $v^{13}_{2601}$ | extratropical | 4% |
| $v^{12}_{3186}$ | jail | 4% |

- Discussion: upper-layer values tend to give higher probability to the next token of the examples that trigger their keys. This suggests memory cells often store how to predict the next word from a prefix pattern. Lower layers show no clear correlation (p. 5488).
- Authors' *possible explanation* of the lower-layer result: lower layers may not operate in the same embedding space as the output embeddings. Some intermediate layers show some agreement, so they appear to operate in a similar space. Further exploration is left to future work (p. 5488).

*Intuition note:* A key says "this pattern is present". In upper layers, the paired value tends to put more probability on the token that follows the pattern. The agreement is small in absolute terms (3.5% at most) but far above chance.

### 5 Aggregating memories (pp. 5488–5491)
**5.1 Intra-layer composition.**
- Layer output (bias $b^\ell$ included here):
$$y^\ell=\sum_i \mathrm{ReLU}(x^\ell\cdot k_i^\ell)\cdot v_i^\ell+b^\ell$$
- Data: 4,000 random validation prefixes. The validation set is used because the aim is to characterise inference-time behaviour, not find memorised training examples (p. 5489).
- Figure 7: a typical example activates (positive coefficient) hundreds of the 4096 memories per layer (10%–50%), and most cells stay inactive. The share drops toward layer 10, the layer where semantic patterns become more prevalent than shallow ones (p. 5489).
- Notation: $\mathrm{top}(h)=\mathrm{argmax}(h\cdot E)$. Count the examples where $\forall i:\ \mathrm{top}(v_i^\ell)\neq\mathrm{top}(y^\ell)$ (p. 5489).
- Figure 8: in every layer, at least ~68% of examples satisfy this condition. Even in upper layers the layer prediction is typically a composition of multiple memories, not one dominant cell (p. 5489).
- Where some memory does agree with the layer: in 60% of cases the target is a common stop word ("the", "of"), and in 43% the prefix has fewer than 5 tokens. The authors suggest very common patterns might be "cached" in single cells without compositionality (pp. 5489–5490).

**5.2 Inter-layer refinement.**
- Residual composition (the residual also carries information from earlier layers, including self-attention) (p. 5490):
$$x^\ell=\mathrm{LayerNorm}(r^\ell),\quad y^\ell=\mathrm{FF}(x^\ell),\quad o^\ell=y^\ell+r^\ell$$
- Hypothesis (author): the model refines its prediction layer by layer, often deciding the prediction at a lower layer (p. 5490).
- Figure 9: the fraction of examples with $\mathrm{top}(r^\ell)=\mathrm{top}(o^L)$ is roughly a third in the bottom few layers and grows rapidly from layer 10. So most "hard" decisions occur before the final layer (p. 5490).
- Figure 10: with $w=\mathrm{top}(o^L)$, $\mathbf p=\mathrm{softmax}(r^\ell\cdot E)$ and $p=\mathbf p_w$, the probability of $w$ also rises with depth. Confidence is refined as well as the identity of the top token (p. 5490).
- Figure 11 splits the cases where the residual's top prediction changes by whether the feed-forward layer overrides it ($\mathrm{top}(o^\ell)=\mathrm{top}(y^\ell)$) or the result is a true composition ($\mathrm{top}(r^\ell)\neq\mathrm{top}(o^\ell)\neq\mathrm{top}(y^\ell)$) (pp. 5490–5491).
  - In most examples the residual's top prediction survives, usually while the feed-forward layer predicts something else (p. 5491).
  - When the residual's prediction does change, it rarely changes to the layer's own prediction. Instead a "compromise" equal to neither appears (p. 5491).
  - Possible conjecture (author): the feed-forward layer acts as an elimination mechanism that vetoes the residual's top prediction and shifts mass to other top candidates (p. 5491).
- Manual check of 100 random last-layer composition cases: in 66 the output changes to a semantically distant word (e.g. "people"→"same"), and in 34 to a related word (e.g. "later"→"earlier", "gastric"→"stomach"). The authors suggest that feed-forward layers tune predictions at varying granularity, even in the last layer (p. 5491).

*Intuition note:* A layer usually does not pick one memory and copy its token. It adds up many small memory contributions. Across layers the residual's guess is nudged, mostly kept and occasionally replaced by a compromise token.

### 6 Related work (p. 5491)
- Prior work analysed neurons in general, CNNs for text (key n-grams), self-attention and inter-layer differences. Earlier work highlighted the importance of feed-forward layers, but their role stayed under-explored. Maximal-activation examples were used before in NLP and vision. The authors' aim is the mechanism of transformers, not explanation of single predictions (p. 5491).

### 7 Discussion and conclusion (pp. 5491–5492)
- Summary: (a) keys correlate with interpretable patterns; (b) values, mostly in upper layers, induce distributions correlating with the next-token distribution of the key's patterns; (c) output is formed by composition within layers and refinement across layers (p. 5491).
- Open directions listed:
  - *Layer embedding space.* The key–value correlation grows with depth. The authors ask whether the layers' output space transforms across layers, and note that this possible transformation cannot be explained solely by feed-forward look-ups plus weighted addition, since one unifying space would then seem more natural. It might involve the interplay with self-attention (p. 5492).
  - *Beyond language modelling.* The formulation should generalise to any transformer (e.g. BERT encoders, translation models). The authors expect similar qualitative results but leave verification to future work (p. 5492).
  - *Practical implications* (the authors say future work may or might explore): interpretability methods that automate pattern identification; effects on training-data privacy (white-box membership inference); and cases where a correct pattern is found but suppressed during aggregation, which may guide architectural novelties (p. 5492).

### Appendices (p. 5494–5495)
- A: Table 3 annotates the top-25 prefixes of $k^5_{895}$. Pattern 1 is "ends with 'press'" (shallow), and pattern 2 is "press/news related" (semantic). Some prefixes carry both patterns, and a few carry none (p. 5495).
- B: the model is Baevski and Auli's 247M-parameter `transformer_lm.wiki103.adaptive` from fairseq. WikiText-103 has over 100M tokens from Wikipedia. spaCy split examples into sentences (p. 5494).

## Toy example (ours, not from the text)
Setup: $d=2$, $d_m=3$, vocabulary $\{a,b,c\}$.
- Keys: $k_1=(1,0)$, $k_2=(0,1)$, $k_3=(-1,-1)$. Values: $v_1=(1,0)$, $v_2=(0,1)$, $v_3=(0,-1)$.
- Output embedding $E$ ($2\times3$), columns $a=(3,0)$, $b=(0,3)$, $c=(2,2)$.
- Input $x=(1,1)$.

1. Pre-activations $xK^\top=(1,\,1,\,-2)$. ReLU gives memory coefficients $m=(1,1,0)$. Memory 3 is inactive.
2. Output $y=1\cdot v_1+1\cdot v_2+0\cdot v_3=(1,1)$.
3. Each value read through $E$ (scores $v\cdot E$ over $a,b,c$):
   - $v_1$: $(3,0,2)$, so top $=a$. Softmax: $e^3=20.09$, $e^0=1$, $e^2=7.39$, sum $28.48$, giving $(0.705,\,0.035,\,0.259)$.
   - $v_2$: $(0,3,2)$, so top $=b$.
   - $v_3$: $(0,-3,-2)$, so top $=a$ (score 0).
4. Layer output: $y\cdot E=(3,3,4)$, so top $=c$. Softmax: $e^3=20.09$ twice, $e^4=54.60$, sum $94.77$, giving $p_c=0.576$ and $p_a=p_b=0.212$.

The layer's top prediction $c$ differs from every memory's top ($a$, $b$, $a$). This is the compositional case counted in Section 5.1: two partial memories together favour a token neither favours alone.

## Concepts
- [[feed-forward-block]] — per-token two-layer network $f(xK^\top)V$; here read as a key-value memory (p. 5485)
- [[key-value-memory]] (new) — $d_m$ key-value pairs; the input is matched to keys and the values are summed with weights (p. 5485)
- [[memory-coefficient]] (new) — the hidden activation $m_i=f(x\cdot k_i)$, an unnormalised non-negative weight for memory $i$ (p. 5485)
- [[trigger-example]] (new) — one of the training prefixes with the highest memory coefficients for a given key (p. 5486)
- [[shallow-vs-semantic-patterns]] (new) — shallow = recurring n-grams; semantic = recurring topic; labelled by human experts (p. 5486)
- [[agreement-rate]] (new) — share of cells where the value's top token equals the next token of the key's top trigger example (p. 5487)
- [[intra-layer-composition]] (new) — a layer output formed from many active memories, differing from each memory's top prediction (p. 5489)
- [[inter-layer-refinement]] (new) — the residual's prediction is sequentially updated by each layer (p. 5490)
- [[residual-stream]] — the vector $r^\ell$ carried between layers, with $o^\ell=y^\ell+r^\ell$ (p. 5490)
- [[softmax]] — used to turn $v\cdot E$ into a vocabulary distribution, and in neural memory (pp. 5485, 5487)

## Canonical instances
- [[baevski-auli-wikitext103-lm]] — the 16-layer LM ($d=1024$, $d_m=4096$) used for all experiments (p. 5486)
- [[table1-key-patterns]] — keys for "substitutes", "base(s)", "part of", time ranges, TV shows (p. 5486)
- [[key-k5-895-press]] — fully annotated "press" key, shallow plus semantic patterns (p. 5495)
- [[value-v15-881-part]] — value predicting "part", 92% of its key's top-50 trigger examples agree (p. 5489)

## Bridges (candidates)
- [structural-analogy] $\mathrm{softmax}(xK^\top)V$ (Eq. 2) ↔ attention: weighted average of value vectors with query–key weights. Here keys and values are fixed parameters and no scaling is shown.
- [structural-analogy] Keys that fire on several patterns (avg 3.6 per key) ↔ polysemantic units (canon link; not stated in this unit).
- [structural-analogy] Residual $r^\ell$ read out through $E$ and refined layer by layer ↔ residual stream as shared bus (canon link; not stated in this unit).
- [metaphor] Memory cells "cache" frequent patterns ↔ key-value lookup tables in data systems.

## Questions this raises
- Why do value projections through $E$ agree with keys only from layer 11 on? Is the layer embedding space really changing, as the authors suggest, or is something else going on?
- Are the 3.5% agreement and ~68% non-agreement figures stable for other models, datasets and tokenisers?
- If a correct pattern is detected but suppressed in aggregation, which memories do the suppressing, and could they be located automatically?
- How would the picture change if the memory coefficients were not sparse ReLU activations?

## Reading notes
- Page offset: printed = pdf + 5483 (printed pages 5484–5495 are the paper's own numbers, pdf 1–12).
- The unit contains no exercises. The experiments are for one model and one dataset (WikiText-103); the authors leave other settings to future work (p. 5492).
- Section 4 says the rank of $w_i^\ell$ "increases" through layers. Figure 5 shows the rank number getting smaller (better rank) in upper layers. I paraphrased by meaning.
- The Figure 3 drop sizes (about 50–70% for the last token) were read from the plot, not given in the text. The Figure 6 tick labels are garbled in the text layer; in the image they are legible (8.9e-5 … 4.e-4).
- Key subscripts such as $k^6_{2546}$ and $k^5_{895}$ are garbled in the text layer. I checked them against the images.
- Appendix B states the model has 247M parameters.
