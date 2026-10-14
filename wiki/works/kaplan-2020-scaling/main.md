---
id: kaplan-2020-scaling/main
work: kaplan-2020-scaling
unit: paper
pages: 1-30
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Scaling Laws for Neural Language Models

## L0 — One line
Transformer language-model loss falls as a smooth power law in model size, data and compute, so a fixed compute budget is best spent on a very large model trained on modest data and stopped well before convergence.

## L1 — The gist (≤ 120 words)
The paper asks how the cross-entropy test loss of Transformer language models depends on model size N (non-embedding parameters), dataset size D, and training compute C. It finds that, when not bottlenecked by the other two factors, loss follows a power law in each, over many orders of magnitude, while depth versus width matters little. Simple fitted equations describe overfitting and training curves, and from them the authors derive how to split a fixed compute budget: mostly into a larger model, with modest data growth, stopping well before convergence. This matters because it makes performance at larger scale predictable, though the authors stress the laws lack a theoretical explanation and must break down eventually.

**Prerequisites:** cross-entropy loss; power laws and log-log plots; partial derivatives (for Appendix B); what a batch, a training step and early stopping are.

## L2 — Key ideas (5–10 bullets)
- Loss depends strongly on scale (N, D, C) and only weakly on shape (depth, width, heads) at fixed N (p. 3, p. 8).
- With the other factors not limiting, $L(N)=(N_c/N)^{\alpha_N}$, $L(D)=(D_c/D)^{\alpha_D}$, $L(C_{\min})=(C_c^{\min}/C_{\min})^{\alpha_C^{\min}}$ with small exponents (≈0.076, 0.095, 0.050); $C_{\min}$ is the minimum compute needed to reach a given loss (p. 4, p. 6).
- One four-parameter equation, $L(N,D)$, covers both limits and governs overfitting. The penalty depends on $N^{\alpha_N/\alpha_D}/D$, so data need grow only about $N^{0.74}$ (p. 5, p. 11–12).
- Learning curves fit $L(N,S_{\min})$, where $S_{\min}$ corrects the step count for batch size using the critical batch size $B_{\rm crit}(L)$ (the batch size giving a roughly optimal time/compute trade-off), which depends on the loss, not directly on model size (p. 12–14).
- Compute-optimal training: $N\propto C_{\min}^{0.73}$, $B\propto C_{\min}^{0.24}$, $S\propto C_{\min}^{0.03}$. Large models are more sample-efficient (they reach a given loss with fewer examples), so training stops far short of convergence (p. 5, p. 15–16).
- Extrapolating the laws far enough yields a contradiction between $L(C_{\min})$ and $L(D)$ at roughly $10^{12}$ parameters (numbers uncertain by an order of magnitude either way). The authors conjecture, with explicit uncertainty, that it marks where Transformer LMs reach maximal performance (p. 17–18).
- Generalization to other text distributions tracks in-distribution loss with a roughly constant offset (p. 3, p. 9).
- The authors list caveats: no theory, uncertain extrapolation of $B_{\rm crit}$, small-data regime and regularization unexplored. They also note that smooth loss may hide qualitative capability changes (p. 19, p. 22–23).

## L3 — Walkthrough

### 1 Introduction (p. 2–6)
**Motivation.** Language is a natural domain for studying AI because most reasoning tasks can be expressed in language and text is plentiful (p. 2). The authors study how loss depends on architecture, model size, compute and data, using Transformers, over more than seven orders of magnitude in scale (p. 2).

**1.1 Summary of findings (p. 3).**
- *Scale, not shape.* Performance depends most strongly on N (non-embedding parameters), D, and C. Within reasonable limits it depends very weakly on depth vs. width (p. 3).
- *Smooth power laws* in each of N, D, C when not bottlenecked by the other two. No deviation seen at the upper end, though loss must flatten before zero (p. 3).
- *Overfitting.* Performance improves predictably if N and D are scaled together, with diminishing returns if one is fixed. The penalty depends on $N^{0.74}/D$. An 8x larger model needs only about 5x more data to avoid a penalty (p. 3).
- *Training curves* follow power laws with parameters roughly independent of model size. Early parts can be extrapolated roughly (p. 3).
- *Transfer:* on other distributions, loss correlates strongly with training-validation loss with a roughly constant offset (p. 3).
- *Sample efficiency:* large models reach the same loss with fewer steps and fewer data points (p. 3).
- *Convergence is inefficient:* under a fixed C with no other limits, best performance comes from very large models stopped significantly short of convergence. Data needs grow as $D\sim C^{0.27}$ (p. 3).
- *Batch size:* the ideal batch size is roughly a power of the loss only, measurable by the gradient noise scale [MKAT18]. It is about 1–2 million tokens at convergence for the largest models (p. 3).

**Figure 3 (p. 4).** For a billion-fold compute increase, the figure shows these multiplicative contributions: more than 1,000,000x model size, about 100x batch size, and fewer than 10x serial steps. The authors read this as: most extra compute goes to model size, data grows slowly, and serial training time barely grows (p. 4).

**1.2 Summary of scaling laws (p. 4–5).** Loss can be predicted by a power law when limited by only one of three things (p. 4):

$$L(N)=(N_c/N)^{\alpha_N};\ \alpha_N\sim0.076,\ N_c\sim8.8\times10^{13}\ \text{(non-embedding params; trained to convergence, large data)}\tag{1.1}$$
$$L(D)=(D_c/D)^{\alpha_D};\ \alpha_D\sim0.095,\ D_c\sim5.4\times10^{13}\ \text{tokens (large model, early stopping)}\tag{1.2}$$
$$L(C_{\min})=\left(C_c^{\min}/C_{\min}\right)^{\alpha_C^{\min}};\ \alpha_C^{\min}\sim0.050,\ C_c^{\min}\sim3.1\times10^{8}\ \text{PF-days}\tag{1.3}$$

(1.3) assumes enough data, an optimally sized model and a sufficiently small batch. A footnote says the trend in plain C at fixed batch size also exists, but $C_{\min}$ should be used for predictions; they are related by (5.5) (p. 4).

The relations span eight orders of magnitude in $C_{\min}$, six in N, and over two in D. They depend very weakly on depth, width and number of heads, and the numbers are specific to WebText2 (p. 5). Doubling parameters multiplies loss by $2^{-\alpha_N}=0.95$. The constants $N_c, C_c^{\min}, D_c$ depend on vocabulary and tokenization, so have no fundamental meaning (p. 5).

Critical batch size obeys roughly (p. 5):
$$B_{\rm crit}(L)=\frac{B_*}{L^{1/\alpha_B}},\quad B_*\sim2\times10^8\text{ tokens},\ \alpha_B\sim0.21\tag{1.4}$$

(1.1) and (1.2) together suggest $D\propto N^{\alpha_N/\alpha_D}\sim N^{0.74}$. A single equation governs joint dependence and overfitting (p. 5):
$$L(N,D)=\left[\left(\frac{N_c}{N}\right)^{\frac{\alpha_N}{\alpha_D}}+\frac{D_c}{D}\right]^{\alpha_D}\tag{1.5}$$
The authors conjecture this form may also describe other generative modeling tasks (p. 5).

For finite steps S in the infinite-data limit, after an initial transient (p. 5):
$$L(N,S)=\left(\frac{N_c}{N}\right)^{\alpha_N}+\left(\frac{S_c}{S_{\min}(S)}\right)^{\alpha_S},\quad S_c\approx2.1\times10^3,\ \alpha_S\approx0.76\tag{1.6}$$
$S_{\min}(S)$ is the minimum possible number of updates, from (5.4) (p. 5).

Under a fixed budget C, (1.6) predicts (p. 5):
$$N\propto C^{\alpha_C^{\min}/\alpha_N},\quad B\propto C^{\alpha_C^{\min}/\alpha_B},\quad S\propto C^{\alpha_C^{\min}/\alpha_S},\quad D=B\cdot S\tag{1.7}$$
$$\alpha_C^{\min}=1/(1/\alpha_S+1/\alpha_B+1/\alpha_N)\tag{1.8}$$
This closely matches empirical $N\propto C_{\min}^{0.73}$, $B\propto C_{\min}^{0.24}$, $S\propto C_{\min}^{0.03}$ (p. 5). Budget should go mostly to larger models; the authors say this also implies that larger models become increasingly sample efficient. In practice researchers train smaller models longer than is compute-efficient, because of hardware constraints (p. 5–6).

*Intuition note.* Each factor alone gives a straight line on a log-log plot, and the slopes are small. So a big loss reduction needs a huge increase in scale. But the line keeps going over many orders of magnitude, which is what makes extrapolation possible.

**1.3 Notation (p. 6).**
- L: cross-entropy in nats, averaged over tokens in a context.
- N: parameters *excluding* vocabulary and positional embeddings.
- $C\approx 6NBS$: estimated non-embedding training compute. B is batch size, S is number of updates. One PF-day $=10^{15}\times24\times3600=8.64\times10^{19}$ FLOPs.
- D: dataset tokens. $B_{\rm crit}$: critical batch size, a roughly optimal time/compute compromise.
- $C_{\min}$: estimated minimum compute to reach a loss (training far below $B_{\rm crit}$).
- $S_{\min}$: estimated minimum steps (training far above $B_{\rm crit}$).
- $\alpha_X$: exponents with $L(X)\propto 1/X^{\alpha_X}$ (p. 6).

### 2 Background and Methods (p. 6–7)
Models are trained on WebText2, byte-pair-encoded with $n_{\rm vocab}=50257$. The loss is the autoregressive log-likelihood averaged over a 1024-token context. The main models are decoder-only Transformers. LSTMs and Universal Transformers are trained for comparison (p. 6).

**2.1 Parameter and compute scaling.** Hyperparameters: $n_{\rm layer}$, $d_{\rm model}$ (residual stream dimension), $d_{\rm ff}$, $d_{\rm attn}$, $n_{\rm heads}$, $n_{\rm ctx}=1024$ (p. 6). Model size, excluding biases and sub-leading terms:
$$N\approx 2d_{\rm model}n_{\rm layer}(2d_{\rm attn}+d_{\rm ff})=12n_{\rm layer}d_{\rm model}^2\ \text{ for } d_{\rm attn}=d_{\rm ff}/4=d_{\rm model}\tag{2.1}$$
(added step: with those substitutions, $2d_{\rm model}n_{\rm layer}(2d_{\rm model}+4d_{\rm model})=12n_{\rm layer}d_{\rm model}^2$.) Embedding parameters ($n_{\rm vocab}d_{\rm model}$) and positional ones ($n_{\rm ctx}d_{\rm model}$) are excluded because this yields significantly cleaner scaling laws (p. 6). A forward pass costs about
$$C_{\rm forward}\approx 2N+2n_{\rm layer}n_{\rm ctx}d_{\rm model}\tag{2.2}$$
add-multiply operations (p. 6). Table 1 (p. 7) gives per-operation counts. Examples: QKV has $n_{\rm layer}d_{\rm model}3d_{\rm attn}$ parameters, and feed-forward has $n_{\rm layer}2d_{\rm model}d_{\rm ff}$. For $d_{\rm model}>n_{\rm ctx}/12$ the context-dependent cost is a small fraction. The backward pass costs about twice the forward pass, so $C\approx 6N$ FLOPs per training token (p. 7).

**2.2 Training.** Adam, 250,000 steps, batch of 512 sequences × 1024 tokens (so $B=2^{19}$ tokens). The largest models (>1B parameters) use Adafactor. The schedule is 3000-step linear warmup then cosine decay to zero. Results at convergence were largely independent of schedule (p. 7).

**2.3 Data.** WebText2 extends WebText with Reddit outbound links through October 2018 (≥3 karma). It has 20.3M documents, 96 GB, $1.62\times10^{10}$ words, and $2.29\times10^{10}$ tokens, of which $6.6\times10^{8}$ are held out as a test set. Other test sets: Books Corpus, Common Crawl, English Wikipedia, Internet Books (p. 7).

### 3 Empirical Results and Basic Power Laws (p. 7–10)
Runs vary: model size (768 to 1.5B non-embedding parameters), dataset size (22M to 23B tokens), shape, context length, batch size ($2^{19}$ for most runs) (p. 7).

**3.1 Shape independence.** At fixed N, loss varies only a few percent over a wide range of $n_{\rm layer}$, $d_{\rm ff}$, $n_{\rm heads}$ (varied one at a time; $d_{\rm model}$ was adjusted to hold N fixed when varying $n_{\rm layer}$ or $d_{\rm ff}$) (p. 8). Aspect ratio can vary by a factor of 40 with little effect. A $(n_{\rm layer},d_{\rm model})=(6,4288)$ model is within 3% of the $(48,1600)$ model of [RWC+19] (Fig. 5, p. 8). Independence of depth would follow if deep Transformers behave as ensembles of shallower models, as suggested for ResNets (p. 8).

**3.2 Loss vs. N.** Models range from $(2,128)$ to billions of parameters. Trained to near convergence on full WebText2, they show no overfitting, except possibly for the largest models (p. 8). The trend fits
$$L(N)\approx(N_c/N)^{\alpha_N}\tag{3.1}$$
Including embedding parameters somewhat obscures the trend, and performance then appears to depend strongly on depth (Fig. 6). Excluding them, models of different depths converge to a single trend; only models with fewer than 2 layers or extreme depth-to-width ratios deviate significantly. This suggests embedding matrices can be made smaller without hurting performance (p. 8–9). Loss on other datasets is also a power law in N with nearly identical exponent (p. 9).

*3.2.1 LSTMs and Universal Transformers (p. 9).* LSTMs match Transformers on early-context tokens but not later ones (Fig. 7). Larger models show larger power-law exponents in context position (Appendix D.5), which the authors take to suggest better quick pattern recognition. Recurrent Transformers, which re-use parameters, do slightly better per N at the cost of more compute per parameter (p. 9).

*3.2.2 Generalization across distributions (p. 9).* Models trained only on WebText2 improve smoothly on other distributions, in parallel. Generalization depends almost exclusively on in-distribution validation loss. It does not depend on training duration, proximity to convergence, or depth (Fig. 8; Appendix D.8) (p. 9–10).

**3.3 Loss vs. D and C (p. 9–10).** For D, a $(36,1280)$ model was trained on fixed subsets and stopped when test loss stopped decreasing:
$$L(D)\approx(D_c/D)^{\alpha_D}\tag{3.2}$$
For C, with $C=6NBS$, for each C they take the best model at step $S=C/(6BS)$ [as printed; $S=C/(6NB)$ is meant]. The batch size is fixed, so this is not truly optimal (p. 9–10):
$$L(C)\approx(C_c/C)^{\alpha_C}\tag{3.3}$$
Data strongly suggest sample efficiency improves with model size (p. 10).

### 4 The infinite-data limit and overfitting (p. 10–12)
**4.1 Why this form of $L(N,D)$.** Three principles (p. 10):
1. Vocabulary or tokenization changes are expected to rescale the loss by an overall factor, so the form must allow rescaling. This holds because $N_c, D_c$ can absorb the change.
2. With D fixed and $N\to\infty$ the loss must approach $L(D)$. With N fixed and $D\to\infty$ it must approach $L(N)$.
3. $L$ should be analytic at $D=\infty$, with a series in $1/D$ with integer powers. The authors call theoretical support "significantly weaker" than for 1–2.

Principle 2 motivates the form because any finite D prevents reaching the entropy of text, and a fixed-size model is capacity-limited. $L(N)$ at infinite D and $L(D)$ at infinite N fully determine the parameters (p. 11). Principle 3: overfitting should relate to dataset variance or signal-to-noise, which scales as $1/D$. This assumes $1/D$ corrections dominate other variance sources (e.g. finite batch size). Without empirical confirmation they would not be confident (p. 11). Principle 3 explains the N–D asymmetry. A symmetric alternative $[(N_c/N)^{\alpha_N}+(D_c/D)^{\alpha_D}]^\beta$ has no integer $1/D$ expansion (footnote 4). The best justification is the good fit (p. 11).

**4.2 Results.** Models use 10% dropout and early stopping. Fit (Table 2, p. 11):

| $\alpha_N$ | $\alpha_D$ | $N_c$ | $D_c$ |
|---|---|---|---|
| 0.076 | 0.103 | $6.4\times10^{13}$ | $1.8\times10^{13}$ |

The fit is excellent except where D is reduced by 1024x to about $2\times10^7$ tokens (an epoch is only 40 updates). The authors suggest that may be a different regime (p. 11). For all but the largest models, 22B-token WebText2 shows no overfitting, so it stands in for $D=\infty$ (p. 11). Define the overfitting measure
$$\delta L(N,D)\equiv\frac{L(N,D)}{L(N,\infty)}-1\tag{4.2}$$
Empirically it depends only on a combination of N and D (Fig. 9, right; the text cites Fig. 16 here). This follows from (1.5), since $L(N,\infty)=(N_c/N)^{\alpha_N}$ (added step):
$$\delta L\approx\left(1+\left(\frac{N}{N_c}\right)^{\frac{\alpha_N}{\alpha_D}}\frac{D_c}{D}\right)^{\alpha_D}-1\tag{4.3}$$
With seed-to-seed loss variation of roughly 0.02, avoiding overfitting to within that threshold requires
$$D\gtrsim(5\times10^3)\,N^{0.74}\tag{4.4}$$
Models under $10^9$ parameters then train with minimal overfitting on the 22B-token set. Our largest models meet some mild overfitting (p. 12). (Added check: $5\times10^3\times(10^9)^{0.74}\approx2.3\times10^{10}$.) Dataset size may thus grow sub-linearly in model size. This is not typically maximally compute-efficient, and regularization was not optimized (p. 12).

*Intuition note.* Overfitting is not controlled by N or D separately but by the ratio $N^{0.74}/D$. Make the model 8x bigger and you need only about 5x more data, since $8^{0.74}\approx4.7$ (added check).

### 5 Scaling with model size and training time (p. 12–14)
**5.1 Adjusting for $B_{\rm crit}$.** [MKAT18] (prior work) argued there is a critical batch size: up to $B_{\rm crit}$, batch size can grow with minimal compute-efficiency loss, and beyond it returns diminish. The gradient noise scale predicts $B_{\rm crit}$, and neither depends directly on model size except via the loss reached (p. 12–13). Training at $B\gg B_{\rm crit}$ minimizes steps and $B\ll B_{\rm crit}$ minimizes compute. Per [MKAT18], at any fixed loss, with steps S and examples $E=BS$ (p. 13):
$$\left(\frac{S}{S_{\min}}-1\right)\left(\frac{E}{E_{\min}}-1\right)=1\tag{5.1}$$
$$B_{\rm crit}(L)\equiv E_{\min}/S_{\min}\tag{5.2}$$
Training at $B_{\rm crit}$ needs $2S_{\min}$ steps and $2E_{\min}$ examples (p. 13). Figure 10 shows $B_{\rm crit}$ follows a power law in the loss and does not depend directly on model size; it approximately doubles for every 13% decrease in loss. The fit is
$$B_{\rm crit}(L)\approx B_*/L^{1/\alpha_B},\quad B_*\approx2\times10^8,\ \alpha_B\approx0.21\tag{5.3}$$
The form lets $B_{\rm crit}$ diverge as $L\to0$, because $L_{\min}>0$ is unknown but apparently far below achieved losses (p. 13). Conversions for runs at batch $B=2^{19}$ tokens (p. 13):
$$S_{\min}(S)\equiv\frac{S}{1+B_{\rm crit}(L)/B}\ \ (\text{min. steps, at }B\gg B_{\rm crit})\tag{5.4}$$
$$C_{\min}(C)\equiv\frac{C}{1+B/B_{\rm crit}(L)}\ \ (\text{min. compute, at }B\ll B_{\rm crit})\tag{5.5}$$

**5.2 $L(N,S_{\min})$.** Stable Adam runs, after warmup, are fit with
$$L(N,S_{\min})=\left(\frac{N_c}{N}\right)^{\alpha_N}+\left(\frac{S_c}{S_{\min}}\right)^{\alpha_S}\tag{5.6}$$
Table 3 (p. 14): $\alpha_N=0.077$, $\alpha_S=0.76$, $N_c=6.5\times10^{13}$, $S_c=2.1\times10^3$. Fits are imperfect but the authors find them compelling given the simplicity (Fig. 4, p. 14). Fits are poor at small S, since the law breaks down early in training (Fig. 11). The authors suggest that, because fits are best late in training when the loss may be roughly quadratic, the power law should provide information about the Hessian spectrum, and its universality suggests the Hessian eigenvalue density is roughly independent of model size (p. 14).

**5.3 Early-stopping lower bound.** Finite-D and infinite-D curves should be similar until $S_{\min}\approx S_{\rm stop}$. This gives a lower bound (and rough estimate), because finite-D loss decreases more slowly (p. 14):
$$S_{\rm stop}(N,D)\gtrsim\frac{S_c}{[L(N,D)-L(N,\infty)]^{1/\alpha_S}}\tag{5.7}$$
Compared with data in Fig. 16 (p. 14, 23).

### 6 Optimal allocation of the compute budget (p. 14–18)
The fixed-batch result of Fig. 1 is not optimal, so the authors standardize to $C_{\min}$ (p. 14–15). Footnote 6: they did not train at $B_{\rm crit}$ from the start because it depends on the target loss (p. 15).

**6.1 Empirical allocations.** Loss vs. $C_{\min}$ is a somewhat altered power law (Fig. 13: $L=(C_{\min}/2.3\cdot10^8)^{-0.050}$ vs. $(C/2.0\cdot10^7)^{-0.057}$ for plain C). The 1-layer to 2-layer transition causes a lump, and 1-layer nets are excluded from fits (p. 15). The optimal model size is
$$N(C_{\min})\propto C_{\min}^{0.73}\tag{6.1}$$
Optimal size grows 5x for each 10x compute. Examples processed supply the rest, about 2x (Fig. 14 caption, p. 16). Since $C_{\min}\equiv6NB_{\rm crit}S$, $B\propto L^{-4.8}$ and $L\propto C_{\min}^{-0.05}$, we get $B_{\rm crit}\propto C_{\min}^{0.24}$ and
$$S_{\min}\propto C_{\min}^{0.03}\tag{6.2}$$
The exponent is small enough that results may be consistent with zero (p. 16). Conclusion: scale mainly N, and raise batch size with $B_{\rm crit}$, with negligible increase in serial steps. Work on speeding early training may be warranted (p. 16). Figure 12 (p. 15): models 0.6x–2.2x the optimal size can be trained with a 20% larger compute budget. Larger-than-optimal models need fewer steps (details in B.4).

**6.2 Predictions from $L(N,S_{\min})$.** Substituting $S_{\min}=C_{\min}/(6NB)$ and minimizing over N at fixed compute (details in Appendix B) gives (p. 16):
$$L(C_{\min})=\left(C_c^{\min}/C_{\min}\right)^{\alpha_C^{\min}},\quad\alpha_C^{\min}\equiv\frac{1}{1/\alpha_S+1/\alpha_B+1/\alpha_N}\approx0.054\tag{6.3, 6.4}$$
$$N(C_{\min})\propto C_{\min}^{\alpha_C^{\min}/\alpha_N}\approx C_{\min}^{0.71}\tag{6.5}$$
These agree with Fig. 13 and match Fig. 14 to within a few percent (p. 16).

*Intuition note.* Most of a bigger budget should go into parameters. The paper notes this also implies bigger models are more sample efficient (they need fewer examples and steps for a given loss) (p. 5). Compute-efficient training therefore stops significantly short of convergence (p. 3).

**6.3 Contradictions and a conjecture (p. 17–18).** Trends must eventually level off because natural language has non-zero entropy (p. 17). Controlling overfitting requires
$$D\propto N^{0.74}\propto C_{\min}^{0.54}\tag{6.6}$$
But compute-efficient single-epoch training at $B_{\rm crit}$ (i.e. $C=2C_{\min}$) uses only
$$D(C_{\min})=\frac{2C_{\min}}{6N(C_{\min})}\approx(4\times10^{10}\text{ tokens})(C_{\min}/\text{PF-Day})^{0.26}\tag{6.7}$$
which grows much more slowly than (6.6) (p. 17). When data-limited, $L(D)\propto D^{-0.095}$ implies $L(D(C_{\min}))\propto C_{\min}^{-0.03}$, which would intersect $L(C_{\min})\propto C_{\min}^{-0.050}$. The intersection is at
$$C^*\sim10^4\text{ PF-days},\ N^*\sim10^{12}\text{ params},\ D^*\sim10^{12}\text{ tokens},\ L^*\sim1.7\text{ nats/token}\tag{6.8}$$
Numbers are uncertain by an order of magnitude either way (Fig. 15). The most obvious reading is that the laws break down at or before this point (p. 17).

**Conjecture (authors', speculative):** the intersection may mean that all reliable information in natural language data has been extracted, so $L^*$ would roughly estimate the entropy per token, and the loss trend would level off at or before $L^*$ (p. 18). Adding noise to the data would shift all trends by a constant, so the critical point would not change except for $L^*$'s absolute value. Distance from the noise floor, $L-L_{\rm noise}$, could be the more meaningful metric (p. 18).

### 7 Related work (p. 18)
Power laws arise from many sources. Power-law scalings in density estimation and random forests may connect, which suggest that exponents may have a very rough interpretation as the inverse of the number of relevant features. Earlier work found power laws with dataset size. [HNA+17] found super-linear data scaling with model size, whereas this paper finds sub-linear. [RRBS19b] fit a similar ansatz. EfficientNet scales depth and width exponentially, whereas here width/depth should stay roughly fixed and architecture matters less than scale. No "jamming transition" when model size reaches dataset size is observed (p. 18).

### 8 Discussion (p. 18–19)
Scalings with N, D, $C_{\min}$ are power laws, so returns diminish. The relations go beyond observation to a predictive framework, which, the authors say, one might interpret as analogues of the ideal gas law. They conjecture that the relations apply to other generative maximum-likelihood tasks, and say they do not know which results are specific to language (p. 19). They hope for a "statistical mechanics" underlying the observed "thermodynamics." Smooth loss improvement "may hide seemingly qualitative changes in capability" ("more is different"), so whether lower loss yields better task performance needs investigation (p. 19). "Big models may be more important than big data" (p. 19); they suggest model parallelism (wide networks, sparsity, growing networks) is worth studying.

### Appendix A: Summary of power laws (p. 20)
Table 4 restates the equations. Table 5 gives fits: $\alpha_N=0.076$, $N_c=8.8\times10^{13}$; $\alpha_D=0.095$, $D_c=5.4\times10^{13}$; $\alpha_C=0.057$, $C_c=1.6\times10^7$ PF-days; $\alpha_C^{\min}=0.050$, $C_c^{\min}=3.1\times10^8$; $\alpha_B=0.21$, $B_*=2.1\times10^8$; $\alpha_S=0.76$, $S_c=2.1\times10^3$. Table 6, compute-efficient values: $N_{\rm opt}=N_eC_{\min}^{0.73}$ ($N_e=1.3\cdot10^9$); $B\ll B_{\rm crit}=B_*/L^{1/\alpha_B}=B_eC_{\min}^{0.24}$ ($B_e=2.0\cdot10^6$ tokens); $S_{\min}=S_eC_{\min}^{0.03}$ (lower bound, $S_e=5.4\cdot10^3$); $D_{\rm opt}=D_eC_{\min}^{0.27}$ (1 epoch, $D_e=2\cdot10^{10}$) (p. 20).

### Appendix B: Compute-efficient frontier (p. 20–22)
All C, S are adjusted to training at $B_{\rm crit}$ (p. 20).

**B.1 Defining equations.** Start from
$$L(N,S)=(N_c/N)^{\alpha_N}+(S_c/S)^{\alpha_S}\tag{B.1}$$
with S at the critical batch size, $B(L)=B_*/L^{1/\alpha_B}$ (B.2). Replace $S=C/(6NB(L))$ (p. 21):
$$L(N,C)=\left(\frac{N_c}{N}\right)^{\alpha_N}+\left(6B_*S_c\frac{N}{L^{1/\alpha_B}C}\right)^{\alpha_S}\tag{B.3}$$
Set $\partial_NL|_C=0$. The author's step is
$$0=-\frac{\alpha_N}{N}\left(\frac{N_c}{N}\right)^{\alpha_N}+\frac{\alpha_S}{N}\left(6B_*S_c\frac{N}{L^{1/\alpha_B}C}\right)^{\alpha_S}\left(1-5\frac{N}{L}\frac{\partial L}{\partial N}\Big|_C\right)$$
where the term containing $\partial L/\partial N|_C$ is crossed out in the source because it vanishes at the optimum. (Added step: the "5" is about $1/\alpha_B\approx4.8$, from differentiating $L^{-1/\alpha_B}$.) Hence
$$\frac{\alpha_N}{\alpha_S}\left(\frac{N_c}{N}\right)^{\alpha_N}=\left(6B_*S_c\frac{N}{L^{1/\alpha_B}C}\right)^{\alpha_S}\tag{B.4}$$
(B.3) and (B.4) determine the frontier (p. 21).

**B.2 Efficient training.** Inserting (B.4) into (B.3) (added step: the second term equals $\frac{\alpha_N}{\alpha_S}(N_c/N)^{\alpha_N}$):
$$L(N_{\rm eff}(C),C)=\left(1+\frac{\alpha_N}{\alpha_S}\right)L(N_{\rm eff},\infty)\tag{B.5}$$
So compute-efficient training stops at a fixed fraction $\alpha_N/\alpha_S\approx10\%$ above the converged loss (p. 21). Eliminating N gives (p. 21):
$$L(C)=(C_c/C)^{\alpha_C},\quad\alpha_C=1/(1/\alpha_S+1/\alpha_B+1/\alpha_N)\approx0.052\tag{B.6, B.7}$$
$$C_c=6N_cB_*S_c\left(1+\frac{\alpha_N}{\alpha_S}\right)^{1/\alpha_S+1/\alpha_N}\left(\frac{\alpha_S}{\alpha_N}\right)^{1/\alpha_S}\tag{B.8}$$
$$\frac{N(C)}{N_c}=\left(\frac{C}{C_c}\right)^{\alpha_C/\alpha_N}\left(1+\frac{\alpha_N}{\alpha_S}\right)^{1/\alpha_N}\tag{B.9}$$
$$S(C)=\frac{C_c}{6N_cB_*}\left(1+\frac{\alpha_N}{\alpha_S}\right)^{-1/\alpha_N}\left(\frac{C}{C_c}\right)^{\alpha_C/\alpha_S}\tag{B.10}$$

**B.3 Comparison to inefficient training.** Define the convergence factor f by
$$L(N,C)=(1+f)L(N,\infty)\tag{B.11}$$
Efficient training has $f=\alpha_N/\alpha_S\approx10\%$. The authors take typical practice as $f'=2\%$. At a fixed loss (p. 22):
$$\frac{N_f}{N_{f'}}=\left(\frac{1+f}{1+f'}\right)^{1/\alpha_N}\approx2.7,\quad\frac{S_f}{S_{f'}}=\left(\frac{1+1/f}{1+1/f'}\right)^{1/\alpha_S}\approx0.13,\quad\frac{C_f}{C_{f'}}=\frac{N_f}{N_{f'}}\frac{S_f}{S_{f'}}\approx0.35\tag{B.12–B.14}$$
So efficient training uses 7.7x fewer updates, 2.7x more parameters and 65% less compute for the same loss (p. 22).

**B.4 Suboptimal model sizes.** Compute to reach loss L with a model of size N (p. 22):
$$C(N,L)=\left(6B_*S_c\frac{N}{L^{1/\alpha_B}}\right)\left(L-\left(\frac{N_c}{N}\right)^{\alpha_N}\right)^{-1/\alpha_S}\tag{B.15}$$
Relative to the efficient size $N_{\rm eff}(L)$:
$$\frac{C(N,N_{\rm eff})}{C(N_{\rm eff},N_{\rm eff})}=\frac{N}{N_{\rm eff}}\left[1+\frac{\alpha_S}{\alpha_N}\left(1-\left(\frac{N_{\rm eff}}{N}\right)^{\alpha_N}\right)\right]^{-1/\alpha_S}\tag{B.16}$$
$$\frac{S(N,N_{\rm eff})}{S(N_{\rm eff},N_{\rm eff})}=\left[1+\frac{\alpha_S}{\alpha_N}\left(1-\left(\frac{N_{\rm eff}}{N}\right)^{\alpha_N}\right)\right]^{-1/\alpha_S}\tag{B.17}$$
Models 0.6x–2.2x the optimal size cost at most about 20% more compute. A smaller model is useful when inference cost matters. A 2.2x larger model needs 45% fewer steps at 20% more compute. The equation should not be trusted for very large models (power-law region only) (p. 22).

*Skip path (Appendix B):* carry forward (B.5) (train to about 10% above converged loss) and (B.6)–(B.10).

### Appendix C: Caveats (p. 22–23)
The authors list: no solid theoretical understanding of any law, "especially mysterious" for model size and compute; low confidence in $B_{\rm crit}(L)$ far outside the explored range; small-data regime, regularization and data augmentation not thoroughly explored; $C\approx6NBS$ omits $n_{\rm ctx}$-dependent terms, so compute scaling may be confounded for $n_{\rm ctx}\gtrsim12d_{\rm model}$; some hyperparameters (initialization scale, momentum) may be untuned; the optimal learning rate depends on target loss and higher rates for unconverged runs were not tried (p. 22–23).

### Appendix D: Supplemental figures (p. 23–27)
- **D.1 Early stopping (Fig. 16, p. 23):** the bound (5.7) holds against empirical $S_{\rm stop}$. $L_{\rm test}-L_{\rm train}$ significantly overestimates overfitting relative to the infinite-data limit.
- **D.2 Universal Transformers (Fig. 17, p. 23–24):** better per N, slightly worse per FLOP.
- **D.3 Batch size (Fig. 18, p. 24):** fits to (5.1) give $B_{\rm crit}(L)$.
- **D.4 Sample efficiency (Fig. 19, p. 24):** steps to reach a given loss fall precipitously with model size. Examples needed improve by almost 100x from smallest to very large.
- **D.5 Context dependence (Fig. 20–21, p. 25):** at fixed model size, per-token loss is a power law in position T. Larger models improve faster on early tokens. During training the model learns short-range information first. Tiny-context ($n_{\rm ctx}=8$) models beat the largest 1024-context models on very early tokens.
- **D.6 Learning rates (Fig. 22, p. 25–26):** schedule is mostly irrelevant if total summed LR is large enough and the schedule has warmup and decays to near zero. Run-to-run variation is about 0.05 in loss for the small (3M) model in Fig. 22. Rule of thumb $\mathrm{LR}(N)\approx0.003239-0.0001395\log(N)$ (D.1), which breaks down for $N>10^{10}$.
- **D.7 Fit quality (Fig. 23, p. 26):** a power law fits L(N) better than a logarithm. 1-layer models and unconverged largest models are excluded from some fits.
- **D.8 Generalization vs. depth (Fig. 24, p. 26–27):** at ~1.5B parameters, no depth effect. The 12-layer model overfit Internet Books (surprising, not seen elsewhere).

## Toy example (ours, not from the text)
*Aim: show why the optimum balances model size against training steps, and how it scales with compute.*

Simplified loss with no batch-size term: $L(N,S)=A/N+B/S$, with $A=B=1$ (an "exponent 1" version of (5.6)). Compute $C=NS$ is fixed (a stand-in for $6NBS$ at fixed B). Take $C=100$.

- $N=5,S=20$: $L=1/5+1/20=0.20+0.05=0.25$.
- $N=10,S=10$: $L=0.10+0.10=0.20$.
- $N=20,S=5$: $L=0.05+0.20=0.25$.

So the middle choice is best. Calculus (added step): $S=C/N$, so $L=1/N+N/C$, and $dL/dN=-1/N^2+1/C=0$ gives $N=\sqrt C$. For $C=10{,}000$: $N=100$, $S=100$, $L=0.01+0.01=0.02$. Compute rose 100x and the optimal N rose 10x, i.e. $N\propto C^{0.5}$. The paper's formula (1.7)–(1.8) with $\alpha_N=\alpha_S=1$ and no batch term gives $\alpha_C=1/(1+1)=0.5$ and $N\propto C^{0.5/1}$, the same. In the paper, $\alpha_N\ll\alpha_S$ and the $B_{\rm crit}$ term shift the exponent to $N\propto C_{\min}^{0.73}$.

Two number checks from the text: doubling N multiplies loss by $2^{-0.076}=e^{-0.076\times0.693}=e^{-0.0527}\approx0.949$. A 10x compute increase gives $10^{0.73}=5.37$x model size, matching "5x" in Fig. 14.

## Concepts
- [[scaling-law]] — loss falls as a power law in parameters, data or compute; here $L(X)\propto1/X^{\alpha_X}$ (p. 4, p. 6)
- [[power-law]] (new) — relation $y\propto x^{-\alpha}$, a straight line on log-log axes; fitted separately for N, D, C (p. 3–4)
- [[compute-optimal-training]] — allocating a fixed compute budget among model size, batch size and steps; here the answer is mostly model size, $N\propto C_{\min}^{0.73}$ (p. 5, p. 16)
- [[cross-entropy-log-loss]] — loss in nats averaged over a 1024-token context; the paper's main metric (p. 6)
- [[non-embedding-parameters]] (new) — parameter count excluding vocabulary and positional embeddings; used because it gives cleaner scaling laws (p. 6, p. 8)
- [[critical-batch-size]] (new) — batch size giving a roughly optimal time/compute trade-off. It depends on loss: $B_{\rm crit}(L)=B_*/L^{1/\alpha_B}$ (p. 12–13)
- [[s-min-c-min-adjustment]] (new) — conversions (5.4)–(5.5) mapping a run at batch B to the minimum steps and compute at $B_{\rm crit}$ (p. 13)
- [[early-stopping-overfitting-law]] (new) — $L(N,D)$ of (1.5); overfitting set by $N^{\alpha_N/\alpha_D}/D$ (p. 5, p. 11)
- [[sample-efficiency]] (new) — larger models reach a given loss with fewer examples and steps (p. 3, p. 24)
- [[tokenization-bpe]] — byte-pair encoding, vocabulary 50257; changing it rescales the loss and the constants (p. 6, p. 5)
- [[residual-stream]] — $d_{\rm model}$ is the dimension of the residual stream (p. 6)
- [[feed-forward-block]] — $d_{\rm ff}$ intermediate layer, counted in N (p. 6)
- [[encoder-only-decoder-only]] — models here are mainly decoder-only Transformers (p. 6)

## Canonical instances
- [[webtext2-scaling-runs]] — Transformers from 768 to 1.5B non-embedding parameters on WebText2 (p. 7)
- [[lstm-vs-transformer]] — LSTMs match early-context tokens but plateau; Transformers keep improving along the context (p. 9)
- [[compute-data-contradiction]] — extrapolated crossing of $L(C_{\min})$ and $L(D(C_{\min}))$ near $N^*\sim10^{12}$, $L^*\sim1.7$ nats/token (p. 17)
- [[ideal-gas-analogy]] — authors say one might interpret the scaling relations as analogues of the ideal gas law (p. 19)

## Bridges (candidates)
- [structural-analogy] $\delta L$ depends on $N^{\alpha_N/\alpha_D}/D$, with overfitting tied to variance ∝ 1/D ↔ statistics: bias–variance and signal-to-noise in finite samples — the authors cite [AS17] for the 1/D argument (p. 11).
- [structural-analogy] Critical batch size from gradient noise scale ↔ optimization: noise-limited vs. curvature-limited regimes of SGD — authors rely on [MKAT18] (p. 12–13).
- [metaphor] "thermodynamics" vs. hoped-for "statistical mechanics" of scaling ↔ physics: macroscopic laws independent of microscopic detail — the authors' own analogy, no derivation (p. 19).
- [structural-analogy] The 1/D expansion principle for $L(N,D)$ ↔ analytic expansions around an infinite-data limit in statistical estimation — authors say its support is weaker than for the other principles (p. 10–11).
- [metaphor] Smooth aggregate loss hiding qualitative change ↔ economics: smooth GDP hiding specific technologies — the authors' own comparison (p. 19).

## Questions this raises
- Does lower loss translate into better performance on downstream language tasks, or do capabilities change in jumps? The authors call this important and open (p. 19).
- Which results depend on natural-language structure and which are universal across modalities? The authors say they do not know (p. 19).
- How reliable is the conjectured meaning of $(N^*,L^*)$, given it moves by an order of magnitude with the exponents (p. 17)?
- What theory could explain the exponents and the compute scaling, which the authors call "especially mysterious" (p. 22)?

## Reading notes
- Printed page = pdf page (offset 0); all page references are printed pages. There are no exercises in this unit.
- The text layer garbled several equations (e.g. 4.3, B.3–B.4, exponents in 1.3). I checked all of them against the page images.
- **Source inconsistencies (as printed):**
  - The abstract says "more than seven orders of magnitude"; §1.1 says "more than six" for N, D, C; p. 5 says eight for $C_{\min}$, six for N, two for D.
  - $C_c^{\min}$ is $3.1\times10^8$ in (1.3) and Table 5, but the Fig. 1 and Fig. 13 legends read $2.3\cdot10^8$.
  - Fig. 13's legend gives $C_c=2.0\cdot10^7$ for plain C, but Table 5 says $1.6\times10^7$.
  - $\alpha_D$ is 0.095 in (1.2) but 0.103 in Table 2. The "0.74" equals $0.076/0.103$ (my arithmetic); $0.076/0.095\approx0.8$.
  - $\alpha_C^{\min}\approx0.054$ in (6.4) but $\approx0.052$ in (B.7). My arithmetic with $\alpha_S=0.76,\alpha_B=0.21,\alpha_N=0.076$ gives about 0.052.
  - Predicted $N\propto C^{0.71}$ (6.5) vs. empirical 0.73.
  - Data growth is $C^{0.27}$ with $2\times10^{10}$ tokens (Table 6, §1.1) but $C^{0.26}$ with $4\times10^{10}$ tokens in (6.7).
  - $B_*$ is about $2\times10^8$ in the text and $2.1\times10^8$ in Fig. 10 and Table 5.
  - Seed variation is "roughly 0.02" (§4.2) vs. "0.05" run-to-run for the 3M model (Fig. 22).
- The text just before Eq. (3.3) (p. 10) gives the best step as $S=C/(6BS)$, which should read $C/(6NB)$.
- Table 1's "Attention: Project" FLOPs entry uses $d_{\rm embd}$ (presumably $d_{\rm model}$). §3.3 writes $n_{\rm embd}$ where $d_{\rm model}$ is meant.
- Appendix B.4 cites "A.1", "A.6", "A.9", "Figure X", "Figure Y". These appear to mean (B.1), (B.6), (B.9), and Fig. 12 (inference from context).
- Fig. 1's footnote 2 text appears at the bottom of p. 2 in the text layer. The first line of §1.1 reads "are are". The references list has OCR damage ("GÃŠrard Biau") and lists [RRBS19a] and [RRBS19b] as the same paper.
