---
id: bahdanau-2015-attention/main
work: bahdanau-2015-attention
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
verifier_issues: 9
pipeline_version: 0.1
---
# Neural Machine Translation by Jointly Learning to Align and Translate

## L0 — One line
Instead of squeezing a source sentence into one fixed vector, let the decoder compute, for every target word, a learned softmax-weighted average of per-word source annotations, so alignment and translation are trained together.

## L1 — The gist (≤ 120 words)
Most earlier neural machine translation models encoded a whole source sentence into one fixed-length vector. The authors conjecture that this is a bottleneck, especially for long sentences. Their model encodes the source into a sequence of annotations (one vector per source word). At each target word, the decoder scores all annotations against its previous state, normalises the scores with a softmax, and uses the weighted sum as a fresh context vector. Because this soft alignment is differentiable, it is trained jointly with everything else. On WMT'14 English→French the authors report that the model beats the plain encoder–decoder regardless of sentence length, and RNNsearch-50 shows no deterioration on long sentences. It comes close to a phrase-based system (Moses). Its alignments look linguistically plausible.

**Prerequisites:** RNN hidden states and gating; softmax; conditional probability and the chain rule; matrix shapes; BLEU as a translation score; SGD.

## L2 — Key ideas (5–10 bullets)
- The basic encoder–decoder compresses the sentence into one fixed-length vector. The authors conjecture this hurts long sentences (p. 1–2).
- Each target word $y_i$ gets its own context vector $c_i=\sum_j\alpha_{ij}h_j$, with $\alpha$ from a softmax over alignment scores (p. 3).
- The alignment model is a feedforward net trained jointly. Alignment is not a latent variable, so gradients flow through it (p. 3–4).
- $c_i$ is an expected annotation under the alignment probabilities $\alpha_{ij}$. The authors call this a mechanism of attention: the decoder decides which source positions to pay attention to (p. 4).
- A bidirectional RNN makes each annotation $h_j$ summarise both left and right context, focused around word $j$ (p. 4).
- RNNsearch beats RNNencdec in all reported BLEU cases. RNNsearch-50 shows no deterioration at length ≥ 50 (p. 6–7).
- Soft alignment copes with reordering (*zone économique européenne*), lets the model use the next word (*the man* → *l'homme*), and handles phrases of different lengths (p. 7). The cost is computing weights for every source word per target word (p. 8).
- Open problem: unknown or rare words (p. 9).

## L3 — Walkthrough

### Abstract and 1 Introduction (p. 1–2)
- Neural MT builds one large network that is tuned jointly. Phrase-based systems instead have many sub-components tuned separately (p. 1).
- Most proposals are encoder–decoders. An encoder reads the source into a fixed-length vector. A decoder generates the translation from it. The pair is trained to maximise the probability of a correct translation given the source (p. 1).
- **Authors' concern:** the network must compress all necessary information into a fixed-length vector. This may make long sentences hard, especially ones longer than those in training. Cho et al. (2014b) showed that the basic model's performance deteriorates rapidly as input length grows (p. 1).
- **Proposal:** the model encodes the input into a *sequence* of vectors. It chooses a subset of them adaptively while decoding. This is meant to remove the squashing problem (p. 2).
- **Claims:** large gains over the basic model, more apparent for long sentences but visible at any length. Performance with a single model is "comparable, or close" to the phrase-based system. The alignments are linguistically plausible (p. 2).

### 2 Background (p. 2–3)
- Translation is $\arg\max_y p(y\mid x)$. A parameterised model is fit on a parallel corpus. Translation is generation by searching for the maximising sentence (p. 2).
- Cited results: Sutskever et al. (2014) reached close to phrase-based performance using LSTMs. Neural components added to existing systems (scoring phrase pairs, re-ranking) surpassed the previous state of the art (p. 2).

**2.1 RNN Encoder–Decoder.** The encoder maps $x=(x_1,\dots,x_{T_x})$ to a vector $c$:
$$h_t=f(x_t,h_{t-1})\tag{1}$$
$$c=q(\{h_1,\dots,h_{T_x}\})$$
Here $h_t\in\mathbb R^n$ is the hidden state. $f,q$ are nonlinear. Sutskever et al. used an LSTM for $f$ and $q(\{h_1,\dots,h_T\})=h_T$ (p. 2). The decoder factorises the probability of the translation:
$$p(y)=\prod_{t=1}^{T}p(y_t\mid\{y_1,\dots,y_{t-1}\},c)\tag{2}$$
$$p(y_t\mid\{y_1,\dots,y_{t-1}\},c)=g(y_{t-1},s_t,c)\tag{3}$$
$g$ is nonlinear and possibly multi-layered. $s_t$ is the decoder RNN state (p. 3). Footnote 2 says that encoding into a fixed-length vector is not necessary, and that a variable-length vector "may be beneficial" (p. 2).

*Intuition note:* In this baseline every output word sees the same $c$. All source information must pass through one vector of fixed size, however long the sentence.

### 3 Learning to Align and Translate (p. 3–4)
**3.1 Decoder.** Eq. (2) is now conditioned on a distinct $c_i$ per target word:
$$p(y_i\mid y_1,\dots,y_{i-1},x)=g(y_{i-1},s_i,c_i)\tag{4}$$
$$s_i=f(s_{i-1},y_{i-1},c_i)$$
The annotations $(h_1,\dots,h_{T_x})$ come from the encoder. Each $h_j$ holds information about the whole input, with a strong focus on the parts around word $j$ (p. 3).
$$c_i=\sum_{j=1}^{T_x}\alpha_{ij}h_j\tag{5}$$
$$\alpha_{ij}=\frac{\exp(e_{ij})}{\sum_{k=1}^{T_x}\exp(e_{ik})}\tag{6}$$
$$e_{ij}=a(s_{i-1},h_j)$$
- $a$ is the *alignment model*. It scores how well the inputs around position $j$ match the output at position $i$. It uses $s_{i-1}$ (the state just before emitting $y_i$) and $h_j$ (p. 3).
- $a$ is a feedforward network trained jointly with all other components (p. 3).
- Unlike in traditional MT, alignment is not a latent variable. The model computes a soft alignment directly, so the cost gradient can be backpropagated through it. Alignment model and translation model are therefore trained together (p. 3–4).
- Reading of $c_i$: let $\alpha_{ij}$ be the probability that $y_i$ is aligned to (translated from) $x_j$. Then $c_i$ is the *expected annotation* under these probabilities (p. 4).
- $\alpha_{ij}$ (or $e_{ij}$) reflects how important $h_j$ is, given $s_{i-1}$, for deciding $s_i$ and generating $y_i$. This is a mechanism of *attention* in the decoder. It relieves the encoder of encoding everything into one fixed vector. Information can be spread over the annotations and retrieved selectively (p. 4).

*Intuition note:* At each output step the decoder asks "which source words matter now?" and takes a weighted average of their annotations. The weights are probabilities that sum to 1 over source positions. Because the alignment is soft and not a latent variable, the whole step is differentiable.

**3.2 Encoder: bidirectional RNN.** The aim is annotations that summarise both preceding and following words. A BiRNN (Schuster & Paliwal, 1997) has a forward RNN $\overrightarrow f$ (reading $x_1\to x_{T_x}$) with states $(\overrightarrow h_1,\dots,\overrightarrow h_{T_x})$. It also has a backward RNN $\overleftarrow f$ (reading $x_{T_x}\to x_1$) with states $(\overleftarrow h_1,\dots,\overleftarrow h_{T_x})$ (p. 4). The annotation concatenates them:
$$h_j=\big[\overrightarrow h_j^{\top};\overleftarrow h_j^{\top}\big]^{\top}$$
Because RNNs tend to represent recent inputs better, $h_j$ will focus on the words around $x_j$ (p. 4).

### 4 Experiment settings (p. 4–5)
- **Task and data.** English→French, WMT'14 parallel corpora: Europarl (61M words), news commentary (5.5M), UN (421M), and two crawled corpora (90M and 272.5M). Total 850M words. Data selection (Axelrod et al., 2011) reduces this to 348M words. No monolingual data is used (p. 4).
- **Splits.** Development set is news-test-2012 plus news-test-2013. Test set is news-test-2014, 3003 sentences (p. 4–5).
- **Vocabulary.** Standard tokenization, then a shortlist of the 30,000 most frequent words per language. Other words map to [UNK]. No lowercasing or stemming (p. 5).
- **Models.** RNNencdec (Cho et al., 2014a) and RNNsearch, each trained on sentences up to 30 words (-30) and up to 50 words (-50). All use 1000 hidden units, with a gated unit (Appendix A.1.1). RNNsearch's encoder has 1000 units in each direction. The output uses a maxout hidden layer (p. 5).
- **Training and decoding.** Minibatch SGD with Adadelta, 80 sentences per minibatch, about 5 days per model. Translations are found by beam search, which only approximately maximises the conditional probability (p. 5).

### 5 Results (p. 5–8)
**5.1 Quantitative (Table 1, BLEU on test set; p. 7).**

| Model | All | No UNK |
|---|---|---|
| RNNencdec-30 | 13.93 | 24.19 |
| RNNsearch-30 | 21.50 | 31.44 |
| RNNencdec-50 | 17.82 | 26.71 |
| RNNsearch-50 | 26.75 | 34.16 |
| RNNsearch-50⋆ | 28.45 | 36.15 |
| Moses | 33.30 | 35.63 |

- "No UNK" means sentences with no unknown words in themselves or in the reference. The models were not allowed to generate [UNK] there. RNNsearch-50⋆ was trained much longer, until development performance stopped improving (p. 7).
- RNNsearch beats RNNencdec in all cases (p. 5).
- On the no-UNK subset, the authors say RNNsearch is "as high as" Moses. This is notable because Moses also uses a separate 418M-word monolingual corpus (p. 5). The table shows 34.16 (RNNsearch-50) and 36.15 (⋆) against 35.63 (Moses). On all sentences Moses leads (33.30 versus 28.45 at best) (p. 7).
- Fig. 2 plots BLEU against sentence length. RNNencdec drops dramatically with length. Both RNNsearch models are more robust. RNNsearch-50 shows no deterioration even at length ≥ 50. RNNsearch-30 even outperforms RNNencdec-50 (p. 5–6).

**5.2.1 Alignment (Fig. 3, p. 6–7).** Fig. 3 plots $\alpha_{ij}$ as grayscale (0 black, 1 white). Each row shows which source positions were weighted while generating one target word (p. 6–7).
- English–French alignment is largely monotonic (strong diagonal), with some non-monotonic cases (p. 7).
- *European Economic Area* → *zone économique européenne* (Fig. 3a): the model aligned *zone* with *Area*, jumping over two words, then looked one word back at a time (p. 7).
- *the man* → *l'homme* (Fig. 3d): a hard alignment would map *the*→*l'* and *man*→*homme*. That is not helpful, because the form of *the* (*le, la, les, l'*) depends on the next word. Soft alignment lets the model look at both words (p. 7).
- Soft alignment also handles phrases of different lengths without mapping words to [NULL] (p. 7).

**5.2.2 Long sentences (p. 7–8).** The authors say the advantage is "likely due to" RNNsearch not having to encode a long sentence perfectly into one vector. It only has to encode well the parts around each word (p. 7).
- Example 1 (*admitting privilege*): RNNencdec-50 translates correctly up to *a medical center*, then drifts. For instance, it renders "based on his status as a health care worker" as *en fonction de son état de santé*. RNNsearch-50's translation preserves the whole meaning (p. 7–8).
- Example 2 (Disney): RNNencdec-50 deviates after about 30 words and loses the closing quotation mark. RNNsearch-50 translates it correctly (p. 8).
- The authors conclude that these examples confirm their hypothesis. Appendix C gives more examples (p. 8).

### 6 Related work (p. 8–9)
- **Graves (2013)**, handwriting synthesis, is a similar alignment. It uses a mixture of Gaussian kernels whose location, width and weight are predicted. The location may only increase monotonically. The authors call this a severe limit for MT because long-distance reordering is often needed (e.g. English→German) (p. 8).
- **This model's cost:** annotation weights are computed for every source word for every target word. The authors say this is not severe for sentences of 15–40 words, but it may limit other tasks (p. 8).
- **Earlier neural MT:** neural nets mostly supplied a feature to an existing system or re-ranked candidates. The authors call their approach "a radical departure": the network alone generates the translation (p. 9).

### 7 Conclusion (p. 9)
- The fixed-length vector is conjectured to be problematic for long sentences, citing Cho et al. (2014b) and Pouget-Abadie et al. (2014).
- All parts, including alignment, are jointly trained toward a better log-probability of correct translations.
- RNNsearch beats RNNencdec "regardless of the sentence length" and is much more robust to length. Its performance is comparable to phrase-based SMT.
- Left for the future: better handling of unknown or rare words.

### Appendix A: Architecture (p. 12–14)
**A.1.1 Gated hidden unit** (decoder; encoder is the same without $c_i$ terms). $\circ$ is element-wise product, $e(y_{i-1})\in\mathbb R^m$ the word embedding (p. 12):
$$s_i=(1-z_i)\circ s_{i-1}+z_i\circ\tilde s_i$$
$$\tilde s_i=\tanh\big(We(y_{i-1})+U[r_i\circ s_{i-1}]+Cc_i\big)$$
$$z_i=\sigma(W_ze(y_{i-1})+U_zs_{i-1}+C_zc_i),\qquad r_i=\sigma(W_re(y_{i-1})+U_rs_{i-1}+C_rc_i)$$
Update gates $z_i$ let a unit keep its previous activation. Reset gates $r_i$ control what to reset. The unit resembles an LSTM: some paths have derivative products close to 1, which eases backward gradient flow (p. 12).

**A.1.2 Alignment model.** It is evaluated $T_x\times T_y$ times per sentence pair, so it is kept cheap (p. 12):
$$a(s_{i-1},h_j)=v_a^\top\tanh(W_as_{i-1}+U_ah_j)$$
with $W_a\in\mathbb R^{n\times n}$, $U_a\in\mathbb R^{n\times2n}$, $v_a\in\mathbb R^{n}$. $U_ah_j$ does not depend on $i$, so it can be precomputed (p. 12).

**A.2.1 Encoder.** Inputs are 1-of-$K$ vectors, $x_i\in\mathbb R^{K_x}$. Forward states (p. 13):
$$\overrightarrow h_i=\begin{cases}(1-\overrightarrow z_i)\circ\overrightarrow h_{i-1}+\overrightarrow z_i\circ\overrightarrow{\underline h}_i & i>0\\0 & i=0\end{cases}$$
$$\overrightarrow{\underline h}_i=\tanh\big(\overrightarrow W\overline Ex_i+\overrightarrow U[\overrightarrow r_i\circ\overrightarrow h_{i-1}]\big)$$
$$\overrightarrow z_i=\sigma(\overrightarrow W_z\overline Ex_i+\overrightarrow U_z\overrightarrow h_{i-1}),\qquad\overrightarrow r_i=\sigma(\overrightarrow W_r\overline Ex_i+\overrightarrow U_r\overrightarrow h_{i-1})$$
Shapes: $\overline E\in\mathbb R^{m\times K_x}$; $\overrightarrow W,\overrightarrow W_z,\overrightarrow W_r\in\mathbb R^{n\times m}$; $\overrightarrow U,\overrightarrow U_z,\overrightarrow U_r\in\mathbb R^{n\times n}$. Backward states are computed similarly. $\overline E$ is shared between directions, the weight matrices are not (p. 13).
$$h_i=\begin{bmatrix}\overrightarrow h_i\\\overleftarrow h_i\end{bmatrix}\tag{7}$$

**A.2.2 Decoder** (p. 13–14). Same gated update as in A.1.1, with $E$ the target embedding and $W,W_z,W_r\in\mathbb R^{n\times m}$, $U,U_z,U_r\in\mathbb R^{n\times n}$, $C,C_z,C_r\in\mathbb R^{n\times2n}$. Initial state: $s_0=\tanh(W_s\overleftarrow h_1)$, $W_s\in\mathbb R^{n\times n}$. Context and alignment (same as Eqs. 5–6):
$$c_i=\sum_{j}\alpha_{ij}h_j,\quad\alpha_{ij}=\frac{\exp e_{ij}}{\sum_k\exp e_{ik}},\quad e_{ij}=v_a^\top\tanh(W_as_{i-1}+U_ah_j)$$
Here $v_a\in\mathbb R^{n'}$, $W_a\in\mathbb R^{n'\times n}$, $U_a\in\mathbb R^{n'\times2n}$. The model becomes the RNN Encoder–Decoder if $c_i$ is fixed to $\overrightarrow h_{T_x}$ (p. 14). Output probability (deep output with one maxout layer):
$$p(y_i\mid s_i,y_{i-1},c_i)\propto\exp(y_i^\top W_ot_i),\quad t_i=\big[\max\{\tilde t_{i,2j-1},\tilde t_{i,2j}\}\big]^\top_{j=1,\dots,l}$$
$$\tilde t_i=U_os_{i-1}+V_oEy_{i-1}+C_oc_i$$
Shapes: $W_o\in\mathbb R^{K_y\times l}$, $U_o\in\mathbb R^{2l\times n}$, $V_o\in\mathbb R^{2l\times m}$, $C_o\in\mathbb R^{2l\times2n}$ (p. 14).

**A.2.3 Sizes:** $n=1000$, $m=620$, $l=500$, $n'=1000$ (p. 14).

### Appendix B: Training (p. 14–15)
- Recurrent matrices are initialised as random orthogonal. $W_a,U_a$ are Gaussian with mean 0 and std 0.001. $V_a$ and biases are zero. Other weights are Gaussian with mean 0 and std 0.01 (p. 14).
- SGD with Adadelta ($\epsilon=10^{-6}$, $\rho=0.95$). The gradient's $L_2$ norm is clipped to at most 1. Minibatch of 80 sentences (p. 14–15).
- To save computation, before every 20th update the code retrieves 1600 sentence pairs, sorts them by length, and splits them into 20 minibatches. Data is shuffled once (p. 15).
- Table 2 gives training statistics. For example, RNNsearch-50 took 111 h, with train/dev NLL 40.7/38.1. RNNsearch-50⋆ took 252 h, 6.67×10⁵ updates, dev NLL 35.2 (p. 14).

### Appendix C (p. 15)
Table 3 lists three long test sentences with the reference, RNNenc-50, RNNsearch-50 and Google Translate (made 27 August 2014) (p. 15).

## Toy example
*(Ours, not from the paper.)* Three source words, 2-D annotations $h_1=(1,0)$, $h_2=(0,1)$, $h_3=(1,1)$. Suppose at output step $i$ the alignment scores are $e_{i1}=\ln6,\ e_{i2}=\ln3,\ e_{i3}=\ln1$.
- Exponentials: $6,\ 3,\ 1$. Sum $=10$.
- Softmax (Eq. 6): $\alpha_{i}=(0.6,\ 0.3,\ 0.1)$.
- Context (Eq. 5): $c_i=0.6(1,0)+0.3(0,1)+0.1(1,1)=(0.6+0.1,\ 0.3+0.1)=(0.7,\ 0.4)$.

At the next step the decoder state has changed, so the scores differ. Take $e_{i+1,\cdot}=(\ln1,\ln1,\ln8)$. Exponentials are $1,1,8$ (sum 10), so $\alpha=(0.1,0.1,0.8)$ and $c_{i+1}=0.1(1,0)+0.1(0,1)+0.8(1,1)=(0.9,\ 0.9)$. Each output word gets a different mixture of the same annotations. A fixed-vector encoder would give both words the same $c$.

## Concepts
- [[attention]] — decoder computes a weighted sum of source annotations; weights from the previous decoder state and each annotation (p. 4)
- [[softmax]] — turns alignment scores $e_{ij}$ into weights $\alpha_{ij}$ that sum to 1 over source positions (p. 3)
- [[encoder-decoder-fixed-vector]] (new) — encoder compresses the source into one fixed-length vector $c$; the paper's baseline and conjectured bottleneck (p. 2)
- [[context-vector]] (new) — per-target-word weighted sum of annotations, $c_i$; the "expected annotation" (p. 3–4)
- [[soft-alignment]] (new) — differentiable alignment probabilities $\alpha_{ij}$, not a latent variable; allows joint training (p. 3–4)
- [[bidirectional-rnn]] (new) — forward and backward RNN states concatenated into annotations $h_j$ (p. 4)
- [[gated-hidden-unit]] (new) — LSTM-like RNN unit with update and reset gates (p. 12)
- [[cross-entropy-log-loss]] — training maximises the conditional log-probability of correct translations (NLL in Table 2) (p. 9, 14)
- [[beam-search]] (new) — approximate search for the translation maximising the conditional probability (p. 5)
- [[bleu-score]] (new) — translation-quality metric used for all comparisons (p. 5, 7)

## Canonical instances
- [[bahdanau-fig2-length-robustness]] — BLEU vs sentence length: RNNencdec falls, RNNsearch-50 does not (p. 5–6)
- [[bahdanau-fig3-alignment-heatmaps]] — $\alpha_{ij}$ plotted as grayscale matrices; mostly diagonal with reorderings (p. 6–7)
- [[bahdanau-the-man-l-homme]] — soft alignment lets *the* use the next word to become *l'* (p. 7)
- [[bahdanau-wmt14-en-fr-table1]] — BLEU of RNNencdec, RNNsearch and Moses (p. 7)

## Bridges (candidates)
- [same-math] $c_i=\sum_j\alpha_{ij}h_j$ with softmax weights ↔ probability: an expectation of $h_j$ under a distribution over positions (the paper's own "expected annotation" reading)
- [structural-analogy] additive alignment score $v_a^\top\tanh(W_as+U_ah)$ ↔ LLM canon, attention: query–key similarity then a weighted average of values. Here keys and values are both $h_j$ and the score is an MLP, not a dot product.
- [structural-analogy] Soft alignment replacing hard word alignment ↔ the paper's discussion of statistical MT: a probability distribution over alignments instead of a single choice.
- [metaphor] "Attention" as the decoder choosing where to look ↔ human selective attention.

## Questions this raises
- The model scores all $T_x$ positions for every one of $T_y$ outputs. How does this cost grow for much longer inputs? (The paper only says it is not severe for 15–40 words, p. 8.)
- Are the learned alignments a faithful explanation of the model's behaviour, or only a visualisation of weights?
- How does the model handle rare words, given its [UNK] shortlist? (The authors name this as the main open problem, p. 9.)
- What happens if the source annotations are not computed by an RNN?

## Reading notes
- Printed page numbers equal pdf page numbers (offset 0). The arXiv version is v7 (19 May 2016), as stamped on page 1.
- Text on p. 7 writes "[zone économique européen]" first and then "[zone économique européenne]". Fig. 3a shows *européenne*.
- Eq. (4) on p. 3 uses $s_i$ and $c_i$. The output formula on p. 14 conditions on $s_i$ but computes $\tilde t_i$ from $s_{i-1}$. The paper does not explain this difference.
- The alignment-model matrices have dimension $n$ on p. 12 and $n'$ on p. 14. Both are 1000 (p. 14).
- The Fig. 2 curves and the grayscale heatmaps in Fig. 3 were read from the images only qualitatively. No exact numbers are given.
- Two Pascanu et al. 2013 references (a/b) are both listed, apparently duplicates (p. 11).
