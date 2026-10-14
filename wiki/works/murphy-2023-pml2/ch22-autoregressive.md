---
id: murphy-2023-pml2/ch22-autoregressive
work: murphy-2023-pml2
unit: "22 Autoregressive models"
pages: 821–828
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Autoregressive models

## L0 — One line
The chain rule writes any joint distribution as a product of "next item given the past" conditionals; autoregressive models give each conditional a restricted neural form (masked networks, causal convolutions, transformers), which gives exact likelihoods but slow sequential sampling.

## L1 — The gist (≤ 120 words)
The chapter asks how to model a joint distribution over a sequence without the cost of fully general conditionals. The answer is to keep the exact chain-rule factorization and give each conditional $p(x_t|x_{1:t-1})$ a restricted functional form, such as a neural network. Different networks give different models: NADE/MADE, causal CNNs (WaveNet, PixelCNN) and transformers (GPT, DALL-E). Exact likelihoods are easy to compute and optimize. Sampling is sequential and therefore slow, and no compact latent representation is learned. Transformer language models trained by maximum likelihood are the main modern example, and scaling them up seems to bring new capabilities such as in-context learning.

**Prerequisites:** chain rule of probability; maximum likelihood; neural networks, convolution and softmax; the idea of attention.

## L2 — Key ideas
- Any joint distribution factorizes by the chain rule into $\prod_t p(x_t|x_{1:t-1})$, a fully connected directed acyclic graph (DAG) (p. 821).
- Later conditionals depend on more arguments, so they are slow and data hungry. Markov models, RNNs (recurrent neural networks) and HMMs (hidden Markov models) avoid this by assumption or by a hidden state; ARMs instead restrict the functional form (p. 821–822).
- Advantage: exact likelihood is easy to compute and optimize. Disadvantages: sampling is sequential, and there is no compact latent code (p. 822).
- NADE, RNADE and MADE use neural conditionals. MADE shares one masked network. NADE-type models assume a natural linear ordering (p. 822).
- Causal (masked) convolutions give WaveNet (1d) and PixelCNN (2d). Dilation captures long-range dependencies (p. 823–824).
- Transformer decoders use causal self-attention. Training is parallel across positions, generation is sequential, and cost is $O(T^2)$ (p. 824).
- GPT-style LLMs are maximum-likelihood autoregressive transformers. Scale seems to bring new capabilities such as in-context learning (examples placed in the prompt), but hallucination, bias and cost remain open problems (p. 825).
- DALL-E models discrete image tokens plus text tokens jointly and reranks samples with a pre-trained critic, CLIP (p. 827).

## L3 — Walkthrough

### 22.1 Introduction (p. 821–822)
By the chain rule, any joint over $T$ variables is
$$p(x_{1:T}) = p(x_1)p(x_2|x_1)p(x_3|x_2,x_1)\cdots = \prod_{t=1}^{T} p(x_t|x_{1:t-1}) \tag{22.1}$$
with $p(x_1|x_{1:0})=p(x_1)$ the initial state distribution (p. 821). This is an **autoregressive model (ARM)**, a fully connected DAG (Fig. 22.1). It can be conditioned on context $c$, giving $p(x|c)$ (p. 821). The "backwards" factorization is
$$p(x_{1:T}) = \prod_{t=T}^{1} p(x_t|x_{t+1:T}) \tag{22.2}$$
Murphy says this "anti-causal" direction is often harder to learn (p. 821).

Each conditional gets more complex as it takes more arguments. This makes it slow to compute and more data hungry to estimate (p. 821). Three ways out are described (p. 821–822):
- **Markov assumption:** $p(x_t|x_{1:t-1})=p(x_t|x_{t-1})$, an ARM of order 1. It is very limiting.
- **Hidden state $z_t$** compressing the past. If $z_t$ is a deterministic function of $x_{1:t-1}$, the model is an RNN. If $z_t$ is a stochastic function of $z_{t-1}$, it is an HMM.
- **Keep the general form** but use a restricted functional form, such as a neural network, for the conditionals. The model then implicitly learns a compact mapping from past to future.

Pros and cons (p. 822): it is easy to compute and optimize the exact likelihood of each sequence. Generating samples is inherently sequential, which can be slow. The method does not learn a compact latent representation.

*Intuition note:* The chain rule is always valid. The modelling work is in choosing a cheap, expressive form for each conditional. The exact likelihood of a sequence is easy to compute and optimize (p. 822). Generating samples is inherently sequential, which can be slow, because each step needs the previous one (p. 822).

### 22.2 NADE (p. 822)
- A generalized linear model (e.g. logistic regression) can represent each conditional [Fre98]. Using a neural network gives **NADE** [LM11].
- **RNADE** uses a conditional mixture of Gaussians:
$$p(x_t|x_{1:t-1})=\sum_{k=1}^{K}\pi_{t,k}\,\mathcal N(x_t|\mu_{t,k},\sigma^2_{t,k}) \tag{22.3}$$
with $(\mu_t,\sigma_t,\pi_t)=f_t(x_{1:t-1};\theta_t)$.
- One network with $T$ inputs and $T$ outputs, built by masking, is more efficient than $T$ separate networks $f_1,\dots,f_T$. This is **MADE**.
- Disadvantage: NADE-type models assume a natural linear ordering. This suits sequences but not images or graphs. An orderless extension exists [UML14; Uri+16].

### 22.3 Causal CNNs (p. 822–824)
If predictive patterns can occur at any location in the past, a convolutional network is a natural way to detect them. The convolution must be masked ("causal") so that it sees only past inputs (p. 822).

**22.3.1 1d (p. 823).** The convolutional Markov model for discrete sequences is
$$p(x_{1:T})=\prod_{t=1}^{T}p(x_t|x_{1:t-1};\theta)=\prod_{t=1}^{T}\mathrm{Cat}\Big(x_t\,\Big|\,\mathrm{softmax}\Big(\varphi\Big(\sum_{\tau=1}^{t-k}\mathbf w^\top \mathbf x_{\tau:\tau+k}\Big)\Big)\Big) \tag{22.4}$$
Here $\mathbf w$ is a filter of size $k$, $\varphi$ a single nonlinearity, and the output is categorical. Future inputs are masked out, so $x_t$ depends only on past values. Deeper models and conditioning on features $c$ are possible. **Dilated convolution** captures long-range dependencies. It is used in **WaveNet**, a state-of-the-art text-to-speech system (Fig. 22.2, dilations 1, 2, 4, 8). WaveNet models $p(x|c)$ with $c$ linguistic features and $x$ raw audio. Tacotron is end-to-end, from words (p. 823). WaveNet is too slow for production but can be distilled into a parallel generative model (p. 823).

**22.3.2 2d, PixelCNN (p. 823–824).**
$$p(x|\theta)=\prod_{r=1}^{R}\prod_{c=1}^{C}p\big(x_{r,c}\,\big|\,f_\theta(x_{1:r-1,1:C},x_{r,1:c-1})\big) \tag{22.5}$$
This conditions on all earlier pixels in raster-scan order. Naive sampling takes $O(N)$ time with $N=RC$ pixels. A multiscale approach [Ree+17] reduces this to $O(\log N)$ (p. 823). A binary mask selects the top-left context. A vertical stack (all previous rows) plus a horizontal stack (current row) avoids blind spots (Fig. 22.3, p. 824).

Extensions (p. 824):
- PixelCNN++ uses a mixture of logistics to capture multimodality.
- PixelRNN combines masked convolution with an RNN.
- Subscale Pixel Network samples higher-order bits first, so detail is conditioned on a low-resolution version of the whole image.

*Intuition note:* Masking forces each output to look only at earlier positions, so a convolution can serve as a conditional $p(x_t|x_{1:t-1})$. Dilated convolution is used to capture long-range dependencies (p. 823).

### 22.4 Transformers (p. 824–827)
Transformers can encode, decode, or both (encoder-decoder for $p(y|c)$). Alternatively, model the joint $p(c,y)$ and give $c$ as the initial context (p. 824).

**Decoder (p. 824).** At step $t$, masked self-attention over $y_{1:t}$ gives attention weights $a_{1:t}$. Then $z_t=\sum_{\tau=1}^{t}a_\tau y_\tau$ (printed as $a_t y_t$, see Reading notes), and $h_t=\mathrm{MLP}(z_t)$. This repeats for each layer. Finally $y_{t+1}\sim\mathrm{Cat}(\mathrm{softmax}(\mathbf W h_t))$. At training time all predictions run in parallel, because the target sequence is available. At test time the model runs sequentially, feeding each output back in. Running time is $O(T^2)$ (p. 824).

*Intuition note:* Training can use the whole known sequence at once, with each position masked from its future. Generation has no future to look at, so it must go one token at a time.

**22.4.1 Text generation (p. 825).**
- GPT is a decoder-only transformer with causal attention.
- GPT-2: 1.5 billion parameters, trained on 8 million web pages (40GB) with a simplified objective, plain maximum likelihood.
- GPT-3: 175 billion parameters, 300 billion words. Training was estimated at 355 GPU years and $4.6M.
- ChatGPT: improved GPT-3, trained for dialog with RLHF (introduced in InstructGPT). RL such as PPO fine-tunes the model toward responses "aligned" with human intent, as scored by a ranking model pre-trained on supervised data.
- Such models are called large language models or foundation models.
- The basic idea is simple (maximum-likelihood training of an autoregressive transformer), about 300 lines of code. By scaling up, it "seems" that new capabilities can emerge (p. 825).
- **In-context learning:** the prompt holds $(x_i,y_i)$ for $i=1{:}N$ plus a test input $x_*$, and the model generates $y_*$ (Fig. 22.4).
- Unresolved problems: confident hallucination, biased or toxic output, and heavy resource cost (p. 825).

**22.4.2 Image generation, DALL-E (p. 825–827).**
- DALL-E was trained on 250 million scraped image-text pairs, with a 12-billion-parameter model.
- A discrete VAE turns image $x$ into tokens $z$. A transformer is fit to the concatenation of $z$ and text tokens $y$, giving $p(z,y)$.
- To sample: draw $z\sim p(z|y)$, then $x\sim p(x|z)$ with the VAE decoder.
- Several images are drawn per prompt and ranked by a pre-trained critic $s_n=\mathrm{critic}(x_n,y_n)$. The critic is CLIP, and reranking significantly improves results (p. 827).
- The hedgehog-and-dog prompt arguably tests "variable binding": the sweater belongs to the hedgehog. The model sometimes gets it right, but not always. Quality can depend on prompt wording (p. 827).
- PARTI follows similar ideas at larger scale, and larger models perform qualitatively better. DALL-E 2, Imagen and Stable Diffusion use diffusion instead (p. 827).

### 22.4.3 and 22.5 (p. 828)
Transformers also generate MIDI music and protein sequences (p. 828). An **LLM** is an autoregressive generative model of discrete tokens (words, or quantized image patches). It is almost always a transformer trained by maximum likelihood (p. 828).

## Toy example (ours)
Binary sequence $x_{1:3}$, with conditionals chosen by us:
- $p(x_1=1)=0.5$.
- $p(x_2=1|x_1=1)=0.8$; $p(x_2=1|x_1=0)=0.3$.
- $p(x_3=1|x_1,x_2)=0.9$ if $x_1=x_2=1$, otherwise $0.2$.

*Likelihood (parallel, past known).*
- $p(1,1,0)=0.5\times0.8\times(1-0.9)=0.04$.
- $p(0,1,0)=0.5\times0.3\times(1-0.2)=0.12$.

Each factor is read directly from the table, so all three could be computed at once.

*Sampling (sequential).* Use uniform draws $u=(0.3,0.6,0.95)$, and set $x_t=1$ if $u_t<p(x_t=1|\text{past})$.
- $x_1$: $0.3<0.5$, so $x_1=1$.
- $x_2$: $0.6<0.8$, so $x_2=1$.
- $x_3$: $0.95<0.9$ is false, so $x_3=0$.

The sample is $(1,1,0)$. Step 3 could not be run before step 2, because its probability depends on $x_2$.

## Concepts
- [[autoregressive-model]] (new) — model $p(x_{1:T})=\prod_t p(x_t|x_{1:t-1})$ with a restricted form for each conditional (p. 821)
- [[chain-rule-factorization]] (new) — any joint is a product of next-given-past conditionals; Eq. 22.1 (p. 821)
- [[masked-convolution]] (new) — causal convolution whose mask hides future inputs (p. 822)
- [[causal-self-attention]] (new) — attention over only the first $t$ inputs at step $t$ (p. 824)
- [[large-language-model]] (new) — autoregressive generative model of discrete tokens, usually a transformer trained by maximum likelihood (p. 828)
- [[in-context-learning]] (new) — prompt holds input-output examples plus a test input; model generates the output (p. 825)
- [[rlhf]] (new) — RL fine-tuning against a ranking model so responses fit human intent (p. 825)
- [[variable-binding-problem]] (new) — getting attributes attached to the right object in a prompt (p. 827)

## Canonical instances
- [[wavenet]] — dilated causal 1d CNN for text-to-speech (p. 823)
- [[pixelcnn]] — raster-order causal 2d CNN over pixels (p. 823)
- [[nade-rnade-made]] — neural, mixture-of-Gaussians and masked-network conditionals (p. 822)
- [[gpt-3]] — 175B-parameter decoder-only transformer, in-context learning (p. 825)
- [[dall-e]] — transformer over image and text tokens with CLIP reranking (p. 827)

## Bridges (candidates)
- [structural-analogy] fully connected ARM DAG (Fig. 22.1) ↔ causal DAG: both are DAGs, but here the ordering is a modelling choice and the text does not claim it is causal.
- [structural-analogy] hidden state $z_t$ compressing the past ↔ sufficient statistic in sequential updating: both summarize history for predicting the next item.
- [metaphor] RLHF ranking model and CLIP critic ↔ likelihood × weighting in Bayes' theorem: both use an external score to steer or rank model output.

## Questions this raises
- Why would the "anti-causal" factorization (22.2) be harder to learn, if both factorizations give the same joint?
- What do we lose, and gain, by not learning a latent representation, compared with latent-variable models?
- How can sampling be sped up (distillation, multiscale) without breaking the exact-likelihood advantage?
- Which of the abilities attributed to scale are robust, given that the text says they "seem" to emerge?

## Reading notes
- Printed = pdf − 34. Page images were supplied for pdf 855–858 and 860–861; pdf 859 and 862 were read from the text layer only.
- Running footer: "Online version. December 10, 2025"; MIT Press, CC-BY-NC-ND.
- The image shows $z_t=\sum_{\tau=1}^{t}a_t y_t$ on p. 824, with the index $\tau$ only in the sum. I wrote $a_\tau y_\tau$ as the likely intent.
- Eq. 22.4 is copied as printed. The sum runs to $t-k$ over $\mathbf x_{\tau:\tau+k}$.
- Typos in the source: "buold", "movied", "arbritrary".
- Figure 22.2 shows stacked dilated layers labelled with dilations 1, 2, 4, 8; only its caption was used. Fig. 22.3 shows a $5\times5$ binary mask.
- The source has no exercises.
