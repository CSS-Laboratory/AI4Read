---
id: prince-2023-udl/ch12-transformers
work: prince-2023-udl
unit: "Chapter 12 — Transformers"
pages: 207–239
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Transformers

## L0 — One line
A transformer lets the tokens in a sequence exchange information through dot-product self-attention (in an encoder, every token with every other token), which shares parameters across positions and makes the connection strengths depend on the content.

## L1 — The gist (≤ 120 words)
Text inputs are large, vary in length and are ambiguous, so the network must share parameters across positions and connect words in content-dependent ways; fully connected networks are impractical. The chapter builds self-attention: one shared set of weights produces values, queries and keys. Softmax-normalised query–key dot products then decide how the values are mixed. Positional encodings, scaling and multiple heads extend self-attention; residual connections and LayerNorm complete a transformer layer. Stacked layers form encoders (BERT), decoders (GPT3, trained by next-token prediction with masked attention) and encoder-decoders (translation, via cross-attention). The cost grows quadratically with sequence length, so sparse variants exist. The same machinery is applied to images (ImageGPT, ViT, SWin, DaViT).

**Prerequisites:** matrix multiplication and transposes; softmax; residual connections and normalisation layers; cross-entropy loss; basic conditional probability.

## L2 — Key ideas
- Text needs parameter sharing across positions and connections that depend on the words (e.g. "it" → "restaurant"). Self-attention gives both (pp. 207–208, 211–212).
- Each output is a weighted sum of shared linear "values". The weights come from softmax of query–key dot products, so they are positive and sum to one (pp. 208, 210).
- Matrix form: $\mathbf{Sa}[\mathbf X]=\mathbf V\cdot\mathbf{Softmax}[\mathbf K^T\mathbf Q/\sqrt{D_q}]$. Self-attention ignores order, so positional encodings are added. Several heads run in parallel (pp. 212–215).
- A transformer layer is multi-head attention plus a per-token MLP, each as a residual block, with LayerNorm (p. 216).
- Pipeline: sub-word tokenizer → learned embeddings → $K$ layers. Three model types: encoder (BERT, masked-word pre-training, then fine-tuning), decoder (GPT3, autoregressive, masked self-attention) and encoder-decoder (cross-attention) (pp. 217–227).
- Large decoders often answer new tasks correctly from a few in-prompt examples. The author says performance is erratic and the amount of true generalisation is unclear (p. 225).
- Attention cost is quadratic in sequence length. Sparsifying the interaction matrix is one remedy (pp. 227–228).
- Transformers also work for images (ImageGPT, ViT, multi-scale models). They usually need very large data, since they must learn what convolution's inductive bias provides (pp. 229–230, 238).

## L3 — Walkthrough

### Opening (p. 207)
Convolutional networks suit grid data through parameter sharing (p. 207). Language data shares some characteristics with images: the number of input variables can be very large, and the statistics are similar at every position. Text differs in that sequences vary in length and cannot easily be resized (p. 207).

### 12.1 Processing text data (pp. 207–208)
The example passage is a restaurant review in which the restaurant refuses to serve a ham sandwich because it only cooks vegetarian food. Three observations follow:
1. The encoded input is large. With 37 words and 1024-dimensional embeddings, $37\times1024=37888$ numbers, so fully connected networks are impractical (p. 207).
2. Inputs differ in length, so parameters should be shared across positions, as in convolution (p. 208).
3. Language is ambiguous. "it" should "pay attention" to "restaurant", not "ham sandwich". Connections must therefore depend on the words and span long distances. "their" in the last sentence also refers to the restaurant (p. 208).

### 12.2 Dot-product self-attention (pp. 208–212)
A standard layer is
$$\mathbf f[\mathbf x]=\mathbf{ReLU}[\boldsymbol\beta+\boldsymbol\Omega\mathbf x]\tag{12.1}$$
A self-attention block takes $N$ inputs $\mathbf x_1,\dots,\mathbf x_N$, each $D\times1$, and returns $N$ outputs of size $D\times1$. First, values:
$$\mathbf v_m=\boldsymbol\beta_v+\boldsymbol\Omega_v\mathbf x_m,\quad \boldsymbol\beta_v\in\mathbb R^{D\times1},\ \boldsymbol\Omega_v\in\mathbb R^{D\times D}\tag{12.2}$$
Then the $n$th output is a weighted sum of all values:
$$\mathbf{sa}_n[\mathbf x_1,\dots,\mathbf x_N]=\sum_{m=1}^N a[\mathbf x_m,\mathbf x_n]\,\mathbf v_m\tag{12.3}$$
The scalar $a[\mathbf x_m,\mathbf x_n]$ is the attention that output $n$ pays to input $m$. The $N$ weights $a[\bullet,\mathbf x_n]$ are non-negative and sum to one. Self-attention can therefore be thought of as routing the values in different proportions to create each output (p. 208).

Figure 12.1 ($N=3$, $D=4$): output 1 uses weights 0.1, 0.3, 0.6; output 2 uses 0.5, 0.2, 0.3. Panel c shows 0.1, 0.2, 0.7 for output 3 (pp. 208–209).

**12.2.1 Computing and weighting values.** The same $\boldsymbol\Omega_v,\boldsymbol\beta_v$ are applied to every input. The cost scales linearly with $N$, and this needs fewer parameters than a fully connected network relating all $DN$ inputs to all $DN$ values. The attention weights are also sparse: there is one per ordered pair of inputs, whatever the input size. Their number is therefore quadratic in $N$ and independent of $D$ (p. 209).

**12.2.2 Computing attention weights.** The outputs result from two chained linear steps: values computed per input, then combined linearly by the attention weights. The whole computation is nonlinear, because the weights are nonlinear functions of the input. The author calls this a *hypernetwork*, where one branch computes the weights of another (p. 209). Two more linear maps give queries and keys:
$$\mathbf q_n=\boldsymbol\beta_q+\boldsymbol\Omega_q\mathbf x_n,\qquad \mathbf k_m=\boldsymbol\beta_k+\boldsymbol\Omega_k\mathbf x_m\tag{12.4}$$
$$a[\mathbf x_m,\mathbf x_n]=\mathrm{softmax}_m[\mathbf k_\bullet^T\mathbf q_n]=\frac{\exp[\mathbf k_m^T\mathbf q_n]}{\sum_{m'=1}^N\exp[\mathbf k_{m'}^T\mathbf q_n]}\tag{12.5}$$
For each $\mathbf x_n$ the weights are positive and sum to one (p. 210). The names come from information retrieval. The dot product measures similarity, so the weights depend on the relative similarity of the $n$th query to all keys. The softmax makes the keys "compete". Queries and keys must have the same dimension, which may differ from the value dimension. The value dimension is usually the same as the input's, so the representation does not change size (pp. 210–211).

**12.2.3 Summary.** Self-attention has no activation function but is nonlinear through the dot product and softmax. It meets both requirements. First, there is one shared parameter set $\boldsymbol\phi=\{\boldsymbol\beta_v,\boldsymbol\Omega_v,\boldsymbol\beta_q,\boldsymbol\Omega_q,\boldsymbol\beta_k,\boldsymbol\Omega_k\}$, independent of $N$, so different sequence lengths are possible. Second, connections between inputs depend on the inputs (pp. 211–212).

**12.2.4 Matrix form.** Put the inputs in the columns of $\mathbf X\in\mathbb R^{D\times N}$, with $\mathbf 1$ an $N\times1$ vector of ones:
$$\mathbf V[\mathbf X]=\boldsymbol\beta_v\mathbf 1^T+\boldsymbol\Omega_v\mathbf X,\quad \mathbf Q[\mathbf X]=\boldsymbol\beta_q\mathbf 1^T+\boldsymbol\Omega_q\mathbf X,\quad \mathbf K[\mathbf X]=\boldsymbol\beta_k\mathbf 1^T+\boldsymbol\Omega_k\mathbf X\tag{12.6}$$
$$\mathbf{Sa}[\mathbf X]=\mathbf V[\mathbf X]\cdot\mathbf{Softmax}\big[\mathbf K[\mathbf X]^T\mathbf Q[\mathbf X]\big]\tag{12.7}$$
$\mathbf{Softmax}[\bullet]$ acts on each column of the matrix separately. The dependence on $\mathbf X$ is then dropped:
$$\mathbf{Sa}[\mathbf X]=\mathbf V\cdot\mathbf{Softmax}\big[\mathbf K^T\mathbf Q\big]\tag{12.8}$$
Shapes (Fig. 12.4): $\mathbf V,\mathbf Q,\mathbf K$ are each $D\times N$ here. $\mathbf K^T\mathbf Q$ is $N\times N$. The output is $D\times N$, the same as the input (pp. 212–213).

*Intuition note:* each token asks a question (query) and every token offers a label (key). The match scores decide how much of each token's content (value) is mixed into the answer. The same small set of matrices is used at every position.

### 12.3 Extensions (pp. 213–215)
The author introduces three extensions that are almost always used in practice (p. 213).

**12.3.1 Positional encoding.** Self-attention ignores input order; more precisely, it is equivariant to permutations of the inputs (p. 213). The author's example is "The woman ate the raccoon" versus "The raccoon ate the woman". Two approaches:
- *Absolute:* add a matrix $\boldsymbol\Pi$ with a unique column per position to $\mathbf X$. It may be hand-chosen (Fig. 12.5: sinusoidal) or learned. It may be added at the input or at every layer, and sometimes only in the queries and keys, not the values (p. 213).
- *Relative:* the absolute position of a word is much less important than the relative position between two words. Each attention-matrix element corresponds to an offset between key position $a$ and query position $b$. A parameter $\pi_{a,b}$ is learned per offset and used to modify the attention matrix (adding, multiplying, or otherwise) (p. 214).

**12.3.2 Scaled dot-product.** Large dot products can push the softmax into a region where the largest value dominates and gradients are very small, making training hard. The dot products are therefore divided by $\sqrt{D_q}$, where $D_q$ is the query/key dimension:
$$\mathbf{Sa}[\mathbf X]=\mathbf V\cdot\mathbf{Softmax}\!\left[\frac{\mathbf K^T\mathbf Q}{\sqrt{D_q}}\right]\tag{12.9}$$
(p. 214).

**12.3.3 Multiple heads.** Run $H$ heads in parallel:
$$\mathbf V_h=\boldsymbol\beta_{vh}\mathbf 1^T+\boldsymbol\Omega_{vh}\mathbf X,\ \ \mathbf Q_h=\boldsymbol\beta_{qh}\mathbf 1^T+\boldsymbol\Omega_{qh}\mathbf X,\ \ \mathbf K_h=\boldsymbol\beta_{kh}\mathbf 1^T+\boldsymbol\Omega_{kh}\mathbf X\tag{12.10}$$
$$\mathbf{Sa}_h[\mathbf X]=\mathbf V_h\cdot\mathbf{Softmax}\!\left[\frac{\mathbf K_h^T\mathbf Q_h}{\sqrt{D_q}}\right]\tag{12.11}$$
Typically values, queries and keys have size $D/H$, since this allows an efficient implementation. The head outputs are vertically concatenated and a linear map $\boldsymbol\Omega_c$ combines them (Fig. 12.6):
$$\mathbf{MhSa}[\mathbf X]=\boldsymbol\Omega_c\big[\mathbf{Sa}_1[\mathbf X]^T,\mathbf{Sa}_2[\mathbf X]^T,\dots,\mathbf{Sa}_H[\mathbf X]^T\big]^T\tag{12.12}$$
Multiple heads seem to be necessary for good performance. It has been speculated that they make the network more robust to bad initialisations (p. 215).

### 12.4 Transformer layers (p. 216)
A transformer layer is multi-head self-attention followed by a fully connected network $\mathbf{mlp}[\bullet]$ applied to each word separately. Both are residual blocks (output added to input). It is typical to add LayerNorm after each. LayerNorm is like BatchNorm but normalises each embedding separately, using statistics over its $D$ embedding dimensions:
$$\begin{aligned}\mathbf X&\leftarrow\mathbf X+\mathbf{MhSa}[\mathbf X]\\ \mathbf X&\leftarrow\mathbf{LayerNorm}[\mathbf X]\\ \mathbf x_n&\leftarrow\mathbf x_n+\mathbf{mlp}[\mathbf x_n]\quad\forall n\in\{1,\dots,N\}\\ \mathbf X&\leftarrow\mathbf{LayerNorm}[\mathbf X]\end{aligned}\tag{12.13}$$
A real network passes the data through a series of such layers (p. 216).

*Intuition note:* attention is the only step where tokens talk to each other. The MLP then processes each token alone. The input and output of a layer have the same $D\times N$ shape, so layers can be stacked.

### 12.5 Transformers for NLP (pp. 216–219)
A typical pipeline: tokenizer → learned embeddings → transformer layers (pp. 216–218).

**12.5.1 Tokenization.** Whole-word vocabularies have three difficulties: some words (e.g. names) are missing; punctuation (e.g. a question mark) must be encoded; and walk/walks/walked/walking would be unrelated tokens. A letters-only vocabulary forces the network to re-learn relations between tiny parts. In practice a compromise is used: common words plus word fragments. A sub-word tokenizer such as byte pair encoding greedily merges commonly occurring sub-strings by frequency (p. 218).

Figure 12.8 (nursery-rhyme example): start from characters and whitespace; repeatedly merge the most frequent adjacent pair (first "s"+"e", then "e"+whitespace). The last character of the first merged token cannot be whitespace, which prevents merging across words. After 23 iterations the tokens are a mix of letters, fragments and common words. Run indefinitely, they become full words. The token count first rises, then falls. In a real case the algorithm stops at a preset vocabulary size (p. 217).

**12.5.2 Embeddings.** Vocabulary $\mathcal V$ has embedding matrix $\boldsymbol\Omega_e\in\mathbb R^{D\times|\mathcal V|}$. The $N$ tokens form $\mathbf T\in\mathbb R^{|\mathcal V|\times N}$ with one-hot columns. Then $\mathbf X=\boldsymbol\Omega_e\mathbf T$, with $\boldsymbol\Omega_e$ learned like any other parameter (Fig. 12.9). Typical sizes are $D=1024$ and $|\mathcal V|=30{,}000$, so $\boldsymbol\Omega_e$ already has many parameters (p. 218). Identical tokens get identical embeddings; the Fig. 12.9 caption notes this for the two copies of "an" (p. 219).

**12.5.3 Transformer model.** $K$ layers form a transformer model. An *encoder* makes a representation supporting many tasks. A *decoder* predicts the next token. An *encoder-decoder* converts one text string into another (pp. 218–219).

### 12.6 Encoder example: BERT (pp. 219–222)
BERT: vocabulary 30,000; 1024-dimensional embeddings; 24 layers; 16 heads per layer; queries, keys and values of dimension 64 per head (matrices $64\times1024$); MLP hidden size 4096; about 340 million parameters (p. 219). Encoders use transfer learning: pre-training by self-supervision on a large corpus, then fine-tuning with a smaller labelled set (p. 219).

**12.6.1 Pre-training.** The task is to predict missing words. A small fraction of input tokens is replaced by `<mask>`. The outputs at those positions go through softmax with a multiclass cross-entropy loss (Fig. 12.10). Training settings: maximum input 512 tokens, batch size 256, a million steps, roughly 50 epochs of a 3.3-billion-word corpus (p. 220). Predicting missing words forces the model to learn some syntax (it might learn that "red" is often found before nouns such as "house" or "car" but never before a verb such as "shout"). It also gives superficial common sense: "train" is more probable than "peanut" in "The <mask> pulled into the station". However, the author adds that the degree of "understanding" such a model can ever have is limited (p. 220). The task uses left and right context but is data-inefficient: in Fig. 12.10, seven tokens add only two loss terms. A secondary adjacent-sentence task only marginally improves performance (footnote, p. 220).

**12.6.2 Fine-tuning.** An extra layer maps outputs to the required format (pp. 221–222):
- *Text classification:* the `<cls>` vector is mapped to a number, passed through a sigmoid, and trained with binary cross-entropy (sentiment).
- *Word classification (named entity recognition):* each embedding $\mathbf x_n$ is mapped to $E\times1$ scores, then softmax and multiclass cross-entropy.
- *Text span prediction (SQuAD 1.1):* question and passage are concatenated. Each token gets two numbers, for span start and span end, each set passed through softmax. A span's likelihood combines the start and end probabilities.

### 12.7 Decoder example: GPT3 (pp. 222–225)
The architecture is very similar to the encoder, but the goal is to generate the next token. Feeding the extended sequence back in gives longer text (p. 222).

**12.7.1 Language modelling.** An autoregressive model factorises the probability of a sentence into conditionals (Eq. 12.14 gives the example "It takes great courage to let yourself appear weak"):
$$Pr(t_1,\dots,t_N)=Pr(t_1)\prod_{n=2}^N Pr(t_n\mid t_1,\dots,t_{n-1})\tag{12.15}$$
This links maximising the joint probability to next-token prediction (pp. 222–223).

**12.7.2 Masked self-attention.** Training maximises the sum of log conditional probabilities. To do this in one forward pass, the term for "great" must not see the answer or the right context, or the system "can cheat". Tokens interact only in self-attention. The dot products to the answer and right context are therefore set to $-\infty$ before the softmax, so their weights are zero. This is masked self-attention (p. 223). The decoder then works as follows: embed tokens; apply layers with masked attention; map each output embedding with a linear layer to vocabulary size; apply softmax; train with multiclass cross-entropy on the next token at every position (Fig. 12.12). Every word contributes a loss term, which is data-efficient, but only the left context is used (pp. 223–224).

**12.7.3 Generating text.** Start from a prompt (e.g. `<start>`). Get next-token probabilities, then pick the most likely token or sample. Append it and repeat. Because of masking, earlier embeddings do not depend on later ones, so earlier computation can be recycled (p. 224). Coherence strategies: *beam search* tracks several completions, since greedy choice does not necessarily find the most likely whole sequence. *Top-k sampling* draws only from the $K$ most likely tokens, to avoid the long tail of low-probability tokens (p. 224).

**12.7.4 GPT3 and few-shot learning.** Sequences are 2048 tokens; total batch 3.2 million tokens; 96 layers (some with sparse attention); embedding size 12288; 96 heads with query/key/value dimension 128; trained on 300 billion tokens; 175 billion parameters (pp. 224–225). The author shows a plausible but "only partially accurate" continuation for a prompt about this book (p. 225). Given a few correct input/output pairs (the grammar-correction example), such models often answer the next question without fine-tuning. This extends to code, arithmetic, translation and question answering. "It is argued" that huge language models are few-shot learners. But the author says performance is erratic in practice, and it is unclear whether the model extrapolates or merely interpolates or copies verbatim (p. 225).

### 12.8 Encoder-decoder: machine translation (pp. 226–227)
For English→French, the encoder makes an output representation per source token. During training the decoder gets the ground-truth French through masked self-attention and predicts the next word at each position. A new attention layer is inserted between the masked self-attention layer and the per-token network. It is called *cross-attention*, or encoder-decoder attention: queries come from the decoder embeddings, keys and values from the encoder embeddings (Fig. 12.14). Each output word is thus conditioned on the previous output words and the source sentence (p. 227).

### 12.9 Transformers for long sequences (pp. 227–228)
In an encoder every token interacts with every other, so computation scales quadratically with length. In a decoder there are roughly half as many interactions, but still quadratic scaling (Fig. 12.15a–b). This limits sequence length. One remedy is to sparsify the interaction matrix (Fig. 12.15c–h):
- A convolutional structure, so each token interacts with a few neighbours. Tokens still interact at larger distances across layers, and kernels can vary in size and dilation rate.
- A pure convolutional approach needs many layers to cover long distances. To speed this up, some tokens (perhaps at the start of each sentence) attend to all tokens, or to all previous tokens in a decoder.
- A few *global tokens* connect to all tokens and each other. Like `<cls>`, they represent no word (p. 228).

### 12.10 Transformers for images (pp. 228–232)
Two reasons for doubt. Images have many more pixels than a sentence has words, so quadratic cost is a bottleneck. And convolutional nets have a good inductive bias (translation equivariance, 2D structure) that a transformer must learn. Even so, transformers have "eclipsed" convolutional nets in image classification and other tasks. The author attributes this partly to their scale and the large pre-training data (p. 229).

**12.10.1 ImageGPT.** A decoder modelling pixels autoregressively. The largest model (6.8 billion parameters) handles only $64\times64$ images. The 24-bit colour is quantised to 9 bits, so there are 512 tokens. It learns a separate positional encoding for each pixel. For classification, the final pixel embeddings are averaged and passed through a linear layer and softmax. It is pre-trained on web images and fine-tuned on ImageNet resized to $48\times48$, with a loss combining cross-entropy and a generative term. Result: 27.4% top-1 error, worse than the convolutional nets of the time but impressive for the small input. It fails where the target object is small or thin (p. 229).

**12.10.2 Vision Transformer (ViT).** Split the image into $16\times16$ patches. Each patch goes through a learned linear map to an input embedding, with learned 1D positional encodings. It is an encoder with a `<cls>` token, but with *supervised* pre-training on 303 million labelled images from 18,000 classes. The final layer is replaced and fine-tuned. ImageNet top-1 error is 11.45%. It did not match the best contemporary convolutional nets that lacked supervised pre-training. The author says the strong inductive bias of convolutional nets can only be superseded with extremely large amounts of training data (pp. 229–230).

**12.10.3 Multi-scale vision transformers.** ViT works at a single scale with a whole-image receptive field. Multi-scale models start with small high-resolution patches and few channels, then enlarge the receptive field, reduce resolution and increase channels (pp. 230–232).
- *SWin* (shifted window): self-attention within windows of patches, with windows shifted in alternate layers so information crosses borders (Fig. 12.18). Every so often, features from non-overlapping $2\times2$ patches are concatenated and mapped to twice the channels. There is no `<cls>`; the last-layer features are averaged. The most sophisticated version gets 9.89% top-1 error (p. 232).
- *DaViT:* alternates patch-to-patch attention using all channels with channel-to-channel attention using all patches. It reaches 9.60% top-1 error and is close to the state of the art at the time of writing (p. 232).

### 12.11 Summary (p. 232)
The transformer operates on sets of embeddings, has low per-layer computational complexity, and is highly parallel in matrix form. Long-range dependencies are possible because every embedding interacts with every other. Cost is quadratic in length. Encoders learn representations by predicting missing tokens. Decoders are autoregressive models, the book's first generative models. Training on very large unlabelled datasets is the book's first example of unsupervised learning. Chapter 13 covers graph networks, whose nodes attend to one another (p. 232).

### Notes (pp. 232–238), compressed
- **RNNs → transformers.** RNNs read tokens one at a time, passing a hidden state forward. They can forget distant tokens. LSTMs and GRUs partially addressed this. Machine translation then suggested that output words should attend to relevant input words, which led to dropping recurrence for the encoder-decoder transformer. The author warns that many transformer "enhancements" do not give meaningful gains in controlled experiments (pp. 233–234).
- **Large language models.** Decoder models are generally not fine-tuned for benchmarks but do well with few-shot prompts. Improvements are attributed mostly to larger models, sparsely activated modules and more data. The author says PaLM (540 billion parameters, 780 billion tokens) has more than enough capacity to memorise its training set, as do many language models. The author says claims of super-human performance are probably true for some tasks but need caution. Arguments exist that such models' "understanding" is limited (p. 234).
- **Tokenizers.** WordPiece and BPE both greedily merge by adjacency frequency and differ in how initial tokens are chosen. Unigram LM, BPE dropout and SentencePiece are mentioned (p. 234).
- **Decoding.** Greedy choice can be generic, and pure random sampling can degrade quality. Part of the reason: training sees only ground-truth tokens (teacher forcing), but at deployment the model sees its own output. Top-K sampling can still allow unreasonable tokens when few choices are probable. Nucleus sampling samples from a fixed proportion of the probability mass (p. 235).
- **Relations to other models.** Self-attention is a hypernetwork. It is also a routing mechanism, but unlike capsule networks (routing by agreement, where outputs compete for inputs), here inputs compete for each output. The random synthesizer removes input dependence of the attention matrix and "performed surprisingly well" (pp. 235–236). Multi-head attention is also linked to graph networks, convolution, RNNs and Hopfield networks (p. 236).
- **Positional encoding.** Position is added rather than concatenated. Since $D$ is usually greater than $N$, the encoding lies in a subspace, and learned embeddings could in theory keep the two parts in orthogonal subspaces. Sinusoidal encodings have two stated properties: relative position is easy to recover linearly, and the dot product generally decreases with distance. Many methods modify only the attention matrix, so that only queries and keys carry position (p. 236):
$$\mathbf V=\boldsymbol\beta_v\mathbf 1^T+\boldsymbol\Omega_v\mathbf X,\quad \mathbf Q=\boldsymbol\beta_q\mathbf 1^T+\boldsymbol\Omega_q(\mathbf X+\boldsymbol\Pi),\quad \mathbf K=\boldsymbol\beta_k\mathbf 1^T+\boldsymbol\Omega_k(\mathbf X+\boldsymbol\Pi)\tag{12.17}$$
 (Eq. 12.16 repeats Eq. 12.9.) In BERT experiments (Wang et al., 2020a) relative encodings did better than absolute ones, with little difference between sinusoidal and learned (p. 236).
- **Longer sequences.** Three lines of work: smaller attention matrices (strided convolution on keys/values; low-rank projection), sparse attention (local blocks, dilated patterns, global tokens; the latter only in the encoder version, otherwise they let the system "look ahead"), and efficient kernels. For the last, $\exp[\mathbf k^T\mathbf q]$ is treated as a kernel $\mathbf g[\mathbf k]^T\mathbf g[\mathbf q]$. This decouples queries and keys, but reproducing the exponential exactly needs a map into infinite-dimensional space. The linear transformer uses a different similarity measure, and the Performer uses a finite approximation (p. 237).
- **Training.** Transformers need learning-rate warm-up and Adam. The author lists interacting causes: residual connections, LayerNorm placement, varying relative weight of residual and attention paths at initialisation, and smaller gradients for query/key parameters than value parameters. Stabilisation attempts include TFixup, moving LayerNorm, and re-weighting residual paths (pp. 237–238).
- **Vision and multimodal.** Many vision applications and variants are listed. Transformers can outperform convolutional nets but usually require large quantities of data. CLIP learns a joint image–caption encoder with a contrastive task (p. 238).

## Toy example (ours, not from the text)
Take $N=2$, $D=D_q=2$, all biases zero, $\boldsymbol\Omega_q=\boldsymbol\Omega_k=\mathbf I$, $\boldsymbol\Omega_v=\mathrm{diag}(2,3)$. Inputs $\mathbf x_1=(1,0)^T$, $\mathbf x_2=(0,1)^T$, so $\mathbf X=\mathbf I$.

- Shapes: $\mathbf Q=\mathbf K=\mathbf I$ ($2\times2$). $\mathbf V=\mathrm{diag}(2,3)\mathbf I$, so $\mathbf v_1=(2,0)^T$ and $\mathbf v_2=(0,3)^T$.
- $\mathbf K^T\mathbf Q=\mathbf I$. Column 1 of scores is $(1,0)$, column 2 is $(0,1)$.
- Column softmax with $e\approx2.718$: for column 1, $e/(e+1)=2.718/3.718=0.731$ and $1/3.718=0.269$. Column 2 is $(0.269,0.731)$.
- Output 1 $=0.731(2,0)+0.269(0,3)=(1.462,\,0.807)$. Output 2 $=0.269(2,0)+0.731(0,3)=(0.538,\,2.193)$.
- Each output mostly copies the value of the input most similar to itself (large dot product), plus a share of the other.
- *Scaling:* divide scores by $\sqrt{D_q}=\sqrt2\approx1.414$. Column 1 becomes $(0.707,0)$, giving weights $2.028/3.028=0.670$ and $0.330$. The softer weights show how scaling keeps the softmax from saturating.
- *Masking (decoder):* set the score of key 2 for query 1 to $-\infty$. Column 1 becomes weights $(1,0)$, so output 1 $=\mathbf v_1=(2,0)$. Column 2 is unchanged.
- *Order-blindness:* swapping the columns of $\mathbf X$ gives the same outputs in swapped order. Output for $\mathbf x_2$ is still $(0.538,2.193)$, now in column 1.

## Concepts
- [[self-attention]] — attention where queries, keys and values all come from the same inputs; each output is an attention-weighted sum of shared linear values (p. 208) (reuse spine "self-attention")
- [[attention]] — non-negative weights summing to one that route values to outputs; here from softmax of query–key dot products (p. 208)
- [[multi-head attention]] — $H$ parallel attention heads with separate parameters, concatenated and mixed by $\boldsymbol\Omega_c$ (p. 214)
- [[positional encoding]] — matrix $\boldsymbol\Pi$ (absolute) or per-offset parameters $\pi_{a,b}$ (relative) that add order information to an order-blind mechanism (pp. 213–214)
- [[causal masking]] — "masked self-attention": dot products to answer and right context set to $-\infty$ before softmax (p. 223)
- [[softmax]] — applied per column of $\mathbf K^T\mathbf Q$ to make attention weights (p. 210)
- [[tokenization (BPE)]] — greedy merging of frequent adjacent token pairs into sub-word tokens (p. 218)
- [[word embedding]] — learned vector per token, $\mathbf X=\boldsymbol\Omega_e\mathbf T$ (p. 218)
- [[encoder-only / decoder-only]] — encoder builds representations (BERT); decoder predicts the next token (GPT3) (pp. 218–219)
- [[masked language modeling]] — BERT pre-training: predict randomly masked tokens from both sides (p. 220)
- [[pretraining / fine-tuning]] — self-supervised pre-training, then task-specific adaptation with labelled data (p. 219)
- [[zero-shot / few-shot prompting]] — here only the few-shot case: examples are given in the context, with no fine-tuning (p. 225)
- [[language model]] — autoregressive factorisation of joint token probability (Eq. 12.15) (p. 223)
- [[cross-entropy / log-loss]] — multiclass/binary cross-entropy used for masking, next-token and fine-tuning losses (pp. 220–224)
- [[layer-norm]] (new) — normalises each embedding using statistics over its $D$ dimensions (p. 216)
- [[cross-attention]] (new) — queries from decoder embeddings; keys and values from encoder embeddings (p. 227)
- [[scaled dot-product attention]] (new) — dot products divided by $\sqrt{D_q}$ to avoid softmax saturation (p. 214)
- [[quadratic attention cost]] (new) — attention cost grows with the square of sequence length; sparse interaction matrices reduce it (p. 227)
- [[decoding strategies]] (new) — greedy, sampling, beam search, top-k, nucleus (pp. 224, 235)
- [[vision transformer]] (new) — patches as tokens in an encoder with `<cls>`; uses large supervised pre-training (pp. 229–230)
- [[hypernetwork]] (new) — one network branch computes the weights of another; applies to the attention weights (p. 209)

## Canonical instances
- [[bert]] — encoder, 340M parameters, masked-word pre-training, fine-tuned for classification, NER, span prediction (pp. 219–222)
- [[gpt3]] — decoder, 175B parameters, next-token prediction, few-shot completion (pp. 224–225)
- [[encoder-decoder-translation]] — English→French with cross-attention (p. 226)
- [[imagegpt]] — pixel-level autoregressive decoder, 27.4% ImageNet top-1 error (p. 229)
- [[vit]] — 16×16 patches, 11.45% top-1 error with large supervised pre-training (pp. 229–230)
- [[swin-transformer]] — shifted windows, multi-scale, 9.89% error (p. 232)

## Bridges (candidates)
- [structural-analogy] self-attention as content-dependent routing ↔ convolution: both share parameters across positions, but attention weights depend on the inputs
- [same-math] autoregressive factorisation (Eq. 12.15) ↔ probability: chain rule, since the product of next-token conditionals p(x_t | x_<t) is the chain rule applied to the token sequence
- [structural-analogy] cross-attention in translation ↔ word-alignment attention: output words attend to relevant source words
- [metaphor] queries/keys/values ↔ information retrieval: a query matched against keys returns content

## Questions this raises
- Why would several smaller heads work better than one large head, and what do the heads learn?
- If a model can memorise its training data, how can we tell few-shot generalisation from copying?
- How much of ViT's data hunger could be removed by building in convolution-like structure?
- Which positional encoding is best, given that relative encodings did better in one BERT study?

## Exercises worth doing
- Ex. 12.1 (p. 239) — count parameters and attention weights versus a fully connected net — difficulty: easy
- Ex. 12.3 (p. 239) — prove permutation equivariance, $\mathbf{Sa}[\mathbf{XP}]=\mathbf{Sa}[\mathbf X]\mathbf P$ — difficulty: medium
- Ex. 12.4 (p. 239) — softmax derivatives for $z=(-3,1,100,5,-1)$; why scaling matters — difficulty: easy
- Ex. 12.7 (p. 239) — extra computation to add one token under masked attention — difficulty: medium
- Ex. 12.9 (p. 239) — compare patch-attention and channel-attention cost in DaViT — difficulty: medium
- Ex. 12.10 (p. 239) — kernelised attention with $\mathbf g[\mathbf k]^T\mathbf g[\mathbf q]$ and efficiency — difficulty: hard

## Reading notes
- Printed page = pdf − 14. The pages carry a draft footer asking for errata, and the licence line names CC-BY-NC-ND and MIT Press.
- Figure 12.10's caption cites "section 5.24" for multiclass cross-entropy, while p. 221 cites section 5.4 for binary cross-entropy. The pages do not let me tell which number is correct; it may be a typo.
- The p. 237 Notes attribute BigBird to "Ainslie et al., 2020", the same citation as for the extended transformer construction. This is reported as printed.
- The p. 235 Notes cite "Wu et al., 2019" for both a convolutional attention system and the gated MLP. This is also as printed.
- Text layers were mostly clean. Figure 12.1's third panel weights (0.1, 0.2, 0.7) were read from the image, since the caption does not give them.
