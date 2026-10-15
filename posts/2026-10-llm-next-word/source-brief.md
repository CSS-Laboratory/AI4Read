---
id: 2026-10-llm-next-word/source-brief
type: source-brief
post: "What does an LLM know when it predicts the next word?"
lenses: [information-theory, linear-algebra, bayesian, analytic-philosophy, theory-of-mind]
built_from: wiki/works digests only (19 works; GPT-3 part 2 used only for §5 Limitations)
created: 2026-10-15
post_fixes: 31
post_fixed: 2026-10-15  # corrections from review/verify.md; log in pipeline/reviews/audit/post01-digest-fixes.md
grounding: all digests primary-text; re-check every claim at the source page before it enters the post (Charter §9)
---

# Source brief — "What does an LLM know when it predicts the next word?"

**Citations.** "(p. N)" = printed page; "(pdf N)" for GPT-2 and Piantadosi & Hill (no printed numbers); "(§ …)" = section heading for Kosinski and Strachan (HTML sources). Hedges are copied from the digests: keep them. Logs base 2 unless a source uses nats.

**Three traps for the whole post**
1. *Relative entropy.* Shannon 1948 means $H/H_{\max}$ (p. 14); Cover means KL, $D(p\|q)$ (p. 18).
2. *Cross-entropy.* Cover shows a code built for $q$ costs $H(p)+D(p\|q)$ bits on average (p. 18), but his historical notes list "cross entropy" as another name for *relative entropy* (p. 49). If we call $H(p)+D(p\|q)$ "cross-entropy" (ML usage), say it is our label.
3. *Units.* Shannon: bits/letter. Kaplan: nats/token (p. 6). Bengio, GPT-2: perplexity. Use $1\text{ nat}=1/\ln2\approx1.443$ bits and perplexity $=2^{H_\text{bits}}=e^{H_\text{nats}}$.

---

## A. Information theory

### 1. Shannon (1948), *Mathematical Theory of Communication*, part 1 (pp. 1–28)
**Claims**
- Semantic aspects are "irrelevant to the engineering problem"; a message is a *selection from a set* (p. 1).
- Any stochastic process producing symbols from a finite set can be seen as a discrete source (p. 5).
- English can be approximated by zero- to third-order letter and first/second-order word approximations; resemblance "increases quite noticeably at each step", and samples are reasonable out to about twice the range used to build them (pp. 6–7).
- It *appears* that a sufficiently complex stochastic process will give a satisfactory representation of a discrete source (p. 7).
- Theorem 2 singles out $-K\sum p\log p$, but Shannon says it is "in no way necessary"; the "real justification" lies in the implications (p. 11).
- $F_N$ (uncertainty of the next symbol given $N-1$ previous) decreases with $N$ and tends to $H$ (Thm 6, p. 14).
- English redundancy is roughly 50% *ignoring structure beyond about eight letters* (p. 14).

**Numbers & equations.** E = .12, W = .02 (p. 7); 27 symbols (p. 7). Worked example (unnumbered; Shannon: "a simple example"): $(\tfrac12,\tfrac14,\tfrac18,\tfrac18)\Rightarrow H=\tfrac74$ bits, code 0/10/110/111 (p. 18). Example C (p. 6): rows A $(0,\tfrac45,\tfrac15)$, B $(\tfrac12,\tfrac12,0)$, C $(\tfrac12,\tfrac25,\tfrac1{10})$; frequencies $\tfrac9{27},\tfrac{16}{27},\tfrac2{27}$. About $2^{HN}$ typical sequences (Thm 4, p. 14).
$$H=-\sum_i p_i\log p_i,\qquad H_x(y)=H(x,y)-H(x),\qquad H=\sum_i P_iH_i\ \ (\text{pp. 11–13})$$

**Instance.** The series of approximations to English (p. 7). The sample texts are not in the digest; copy them from the source.

**Careful!** Shannon sets meaning aside; he does not say a good stochastic model captures meaning.

### 2. Shannon (1951), *Prediction and Entropy of Printed English* (pp. 50–64)
**Claims**
- It *appears* that long-range effects (up to 100 letters) reduce entropy to "something of the order of one bit per letter", redundancy roughly 75%; it *may be* higher with paragraph/chapter structure (pp. 50–51).
- The reduced text (guess numbers) can, at least in principle, be decoded by an identical twin, "mathematically, not just biologically" — prediction is encoding (p. 55).
- Errors cluster at the beginnings of words and syllables (p. 55).
- An ideal predictor with more context never does worse (ineq. 11, p. 59).
- Upper bound valid for any predictor; lower bound proved for the ideal predictor only; human data carry sampling error (pp. 61, 64).
- Reverse prediction scored only slightly worse (p. 58).

**Numbers & equations.** 26 letters: $F_0=4.70, F_1=4.14, F_2=3.56, F_3\approx3.3, F_{word}=2.62$; 27 letters: 4.76, 4.03, 3.32, 3.1, 2.14 (p. 54). Zipf $p_n=.1/n$ to rank 8,727: 11.82 bits/word ÷ 4.5 = 2.62 bits/letter (pp. 52–53). Exp. 1 (single guess, told the letter if wrong): 89/129 (69%) right (p. 55); Exp. 2 (guess until right): 79/102 (77%) right at the first guess (p. 56). Do not mix the two. Table I first-guess row (per 100), columns $N$ = 1…15, 100: 18.2, 29.2, 36, 47, 51, 58, 48, 66, 66, 67, 62, 58, 66, 72, 60, 80 (p. 57). Column $N$ means $N-1$ letters known (column 1 = no letters known); the last test had 100 letters known. Columns 1–2 were computed from letter and digram frequency tables, not from the subject's guesses (p. 57). At 100 letters: 0.6–1.3 bits/letter (p. 64).
$$F_N=-\sum_{i,j}p(b_i,j)\log_2 p_{b_i}(j),\quad H=\lim_{N\to\infty}F_N\ (\text{p. 51});\qquad \sum_i i(q_i-q_{i+1})\log i\le F_N\le-\sum_i q_i\log q_i\ (\text{p. 61})$$

**Instance.** The guessing game: the reduced text is mostly 1s (p. 56).

**Careful!** "About one bit per letter" is hedged, from human guessers on one book (*Jefferson the Virginian*, named on p. 57; experiment described pp. 56–57); not a measured constant.

### 3. Cover & Thomas, ch. 2 (pp. 12–49)
**Claims**
- $H(X)=E\log\frac1{p(X)}$ depends only on probabilities (p. 13); $H\le\log|\mathcal X|$, equality iff uniform (p. 27).
- $D(p\|q)$ = inefficiency of assuming $q$ when truth is $p$; the $q$-code costs $H(p)+D(p\|q)$ bits (p. 18).
- $D\ge0$, equality iff $p=q$ (p. 26); not symmetric (pp. 18–19).
- Chain rule $H(X_1..X_n)=\sum_i H(X_i\mid X_{i-1}..X_1)$ (p. 21).
- Conditioning reduces entropy *on average only* (p. 28).
- Data processing: $X\to Y\to Z\Rightarrow I(X;Y)\ge I(X;Z)$ (p. 32). Fano: leftover $H(X|Y)$ forces errors (p. 39).

**Numbers & equations.** 7/4 bits (p. 14) = 1.75 yes/no questions for this source (p. 15). In general the minimum expected number of binary questions lies between $H$ and $H+1$ (p. 15); it equals $H$ here only because the probabilities are powers of ½. $D(p\|q)=0.2075$ vs $D(q\|p)=0.1887$ bits for $r=\tfrac12,s=\tfrac14$ (p. 19).
$$D(p\|q)=\sum_x p(x)\log\frac{p(x)}{q(x)},\qquad I(X;Y)=H(X)-H(X\mid Y),\qquad D(p\|u)=\log|\mathcal X|-H(X)$$

**Instance.** "Coding with the wrong distribution costs $D$ extra bits" (p. 18).

**Careful!** Trap 2. And a specific context can *raise* uncertainty (p. 28).

---

## B. Linear algebra (embeddings, attention)

### 4. Bengio et al. (2003), *Neural Probabilistic LM* (pp. 1137–1155)
**Claims**
- Curse of dimensionality: 10 words, $|V|=100{,}000$ → potentially $10^{50}-1$ free parameters (p. 1137).
- In the authors' view n-grams ignore context beyond 1–2 words and word similarity (pp. 1138–1139).
- A learned vector $C(i)\in\mathbb R^m$ per word, trained jointly; similar words are *expected* to sit close (p. 1139). Smoothness lets one sentence raise a "combinatorial number" of neighbours (p. 1140).
- Fixed PCA features were tried "unsuccessfully", which *suggests* joint learning helps (p. 1141).
- Perplexity ≈24% (Brown) and ≈8% (AP) better than the best n-gram; mixing with a trigram always helped, *suggesting* different errors (p. 1148).
- The authors *believe* the gain comes from the distributed representation (p. 1152); polysemy is "probably not well served" (p. 1152).

**Numbers & equations.** $m=30,60,100$ vs $|V|\approx17{,}000$ (p. 1139). Brown test perplexity: MLP10 (mixed 0.5/0.5 with an interpolated trigram) 252; best n-gram = class-based back-off, 500 classes, 312 (gives the caption's 24%); best word-level Kneser–Ney 321 (Table 1, p. 1149). AP: MLP10 (mixed) 109 vs KN 117 (Table 2, p. 1150). Softmax ≈99.7% of compute (p. 1145).
$$\hat P(w_1^T)=\prod_t\hat P(w_t\mid w_1^{t-1})\ (\text{p. 1138});\qquad \hat P(w_t\mid\cdot)=\frac{e^{y_{w_t}}}{\sum_ie^{y_i}}\ (\text{p. 1142}),\ \ y=b+Wx+U\tanh(d+Hx)\ (\text{eq. 1, p. 1143})$$
$$L=\tfrac1T\textstyle\sum_t\log f(w_t,\dots,w_{t-n+1};\theta)+R(\theta)\ (\text{p. 1142});\quad \text{perplexity}=\exp(\text{mean NLL})\ (\text{p. 1141})$$

**Instance.** "The cat is walking in the bedroom" → "A dog was running in a room" (p. 1139).

**Careful!** Conclusion says "10–20%" (p. 1152); §4 says ≈24%/≈8% — use §4. Embeddings are not tested separately from the hidden layer.

### 5. Mikolov et al. (2013a), *Efficient Estimation* (pp. 1–12)
**Claims**
- CBOW and Skip-gram drop the hidden layer; they *might* represent data less precisely but can *possibly* train on much more data (p. 4).
- Analogy: nearest word (cosine) to vec(biggest) − vec(big) + vec(small), inputs discarded (p. 5).
- Exact match required; 100% "likely impossible"; authors *believe* accuracy correlates with usefulness (p. 6).
- Dimension and data must grow together (pp. 6–7). Skip-gram is much better on semantics (p. 7).
- Table 8 examples would score only ≈60% under exact match (pp. 9–10).

**Numbers & equations.** 8,869 semantic + 10,675 syntactic questions (p. 6). Table 3, sem/syn %: RNNLM 9/36, NNLM 23/53, CBOW 24/64, Skip-gram 55/59 (p. 7). Skip-gram 1000-dim, 6B words: 65.6 total (p. 9).
$$O=E\times T\times Q;\quad Q_{\text{CBOW}}=N D+D\log_2V;\quad Q_{\text{SG}}=C(D+D\log_2V)\ (\text{pp. 3–4})$$

**Instance.** big : biggest :: small : smallest; France : Paris :: Germany : Berlin (p. 5).

**Careful!** King − Man + Woman ≈ Queen is cited from earlier work [20] (p. 2). Best totals are about two thirds (65.6%); with 2013b's 39.6% the range is about 40–66%, not "one third".

### 6. Mikolov, Yih & Zweig (2013b), *Linguistic Regularities* (pp. 746–751)
**Claims**
- Word vectors = columns of $\mathbf U$ of an RNN LM trained only for likelihood, with no built-in syntax or semantics (p. 747).
- Relations show up as *roughly* constant offsets, $x_{apple}-x_{apples}\approx x_{car}-x_{cars}$ (p. 746); the method *assumes* one offset per relation (p. 748).
- RNN-1600: 39.6% of 8,000 syntactic questions vs best LSA 16.5% (test set p. 748; Table 2 p. 749).
- RNN-320+ beat the prior best on SemEval-2012 Task 2 without task training (p. 750). Both called byproducts of maximum-likelihood training (p. 750).

**Equations.**
$$\mathbf s(t)=f(\mathbf U\mathbf w(t)+\mathbf W\mathbf s(t-1)),\ \ \mathbf y(t)=g(\mathbf V\mathbf s(t))\ (\text{p. 747});\qquad y=x_b-x_a+x_c,\ \ w^*=\arg\max_w\frac{x_w\cdot y}{\|x_w\|\|y\|}\ (\text{p. 748})$$

**Instance.** man→woman, uncle→aunt, king→queen (Fig. 2, p. 749).

**Careful!** ≈40% correct, "≈" offsets. Whether $a,b,c$ are excluded from the search is not stated.

### 7. Mikolov et al. (2013c), *Words and Phrases* (pp. 1–9)
**Claims**
- Full softmax costs ∝ $W\approx10^5$–$10^7$: impractical (p. 3).
- Negative sampling: true context vs $k$ noise words; $U(w)^{3/4}/Z$ was best of those tried (p. 4).
- Madrid − Spain + France is closer to Paris than to any other word vector (p. 1).
- Reply to "linearity makes analogies easy": non-linear RNNs also improve with data, which *suggests* non-linear models also prefer linear structure (p. 5).
- Authors *explain* vector addition as a product ("AND") of context distributions (p. 7).
- Phrase analogies 72% (≈33B words) vs 66% (6B), *suggesting* large data is crucial (p. 7).

**Equations.** $k$ = 5–20 small data, 2–5 large (p. 4). NEG-15: 61% total (Table 1, p. 5).
$$\frac1T\sum_t\sum_{-c\le j\le c,j\ne0}\log p(w_{t+j}\mid w_t),\quad p(w_O\mid w_I)=\frac{\exp({v'_{w_O}}^{\top}v_{w_I})}{\sum_w\exp({v'_w}^{\top}v_{w_I})}\ (\text{pp. 2–3})$$
$$\log\sigma({v'_{w_O}}^{\top}v_{w_I})+\textstyle\sum_{i=1}^k\mathbb E_{w_i\sim P_n}[\log\sigma(-{v'_{w_i}}^{\top}v_{w_I})]\ (\text{p. 4})$$

**Instance.** Country–capital PCA (Fig. 2, p. 4).

**Careful!** "AND" is informal. Intro says "Russia" + "river" (p. 2); Table 5 uses "Russian", with "Volga River" *second* after "Moscow" (p. 7).

### 8. Vaswani et al. (2017), *Attention Is All You Need* (pp. 1–15)
**Claims**
- Output = weighted sum of values, weights from query–key compatibility (pp. 3–4).
- Authors *suspect* large $d_k$ pushes softmax into tiny-gradient regions, hence $1/\sqrt{d_k}$; under independence $\mathrm{Var}(q\cdot k)=d_k$ (p. 4, fn. 4).
- Multi-head lets the model attend to different representation subspaces (p. 5).
- Masking ($-\infty$ before softmax) in the translation *decoder* makes position $i$ depend only on positions $<i$, "to preserve the auto-regressive property" (pp. 3, 5).
- Self-attention: $O(1)$ path length, $O(n^2d)$ per layer (pp. 6–7).
- Heads "apparently involved in anaphora resolution" (p. 14).

**Numbers & equations.** $N=6$, $d_{model}=512$, $h=8$, $d_k=d_v=64$, $d_{ff}=2048$ (pp. 3, 5); BLEU 28.4 EN-DE, 41.8 EN-FR (p. 8); single head −0.9 BLEU (p. 9).
$$\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\Big(\frac{QK^T}{\sqrt{d_k}}\Big)V\ (\text{p. 4});\qquad \mathrm{head}_i=\mathrm{Attention}(QW_i^Q,KW_i^K,VW_i^V)\ (\text{p. 5})$$

**Instance.** Sharp attention from "its" to "Law" and "application" (Fig. 4, p. 14).

**Careful!** This is an encoder–decoder translation model; GPT-style LMs are decoder-only (Kaplan p. 6). Visualizations are not causal evidence. EN-FR 41.0 in §6.1 vs 41.8 in Table 2 (p. 8).

---

## C. Scale

### 9. Radford et al. (2019), *GPT-2* (pdf 1–24)
**Claims**
- A general system should model $p(\text{output}\mid\text{input},\text{task})$; language puts all three in one sequence (pdf 2).
- In a "slightly toy setting" the supervised and unsupervised objectives share a global minimum; learning is "much slower" than supervised (pdf 3).
- *Speculation:* a model with enough capacity will begin to infer and perform tasks shown in text "in order to better predict them" (pdf 3).
- Zero-shot SOTA on 7 of 8 LM datasets; still underfits WebText (pdf 5, 8).
- Summaries "just barely" beat random sentences; zero-shot is "far from use-able" (pdf 6, 9).
- Overlap gives a "small but consistent benefit" (pdf 8).

**Numbers & equations.** 117M–1542M parameters; vocab 50,257; context 1024 (pdf 4). WebText >8M docs, 40 GB (pdf 3). LAMBADA ppl 99.8 → 8.6, acc 63.24% (pdf 5); CoQA 55 F1 (pdf 6); EN→FR 5 BLEU, FR→EN 11.5 (pdf 6–7); NQ 4.1% (pdf 7). "TL;DR:" removed → −6.4 points (pdf 6).
$$p(x)=\prod_{i=1}^n p(s_n\mid s_1,\dots,s_{n-1})\quad(\text{pdf 2, printed with } s_n)$$

**Instance.** Adding "TL;DR:" after an article and generating 100 tokens with top-$k$ sampling ($k=2$) induces summary-like text; the first 3 sentences are taken as the summary (pdf 6). The model *tends to* continue with a summary; it is not "the most likely continuation".

**Careful!** "Unsupervised multitask learning" is a hypothesis; most task scores are weak.

### 10. Brown et al. (2020), *GPT-3* (pp. 1–28; §5 pp. 33–34)
**Claims**
- In-context learning = inner loop in the forward pass, no gradient updates (pp. 3–4).
- The terms are "agnostic" on learning from scratch vs recognizing trained patterns (p. 4, fn. 1); §5: it is a spectrum and *may* vary by task (p. 34).
- *Plausible* that ICL gains with scale (p. 4); growing zero/few-shot gap "perhaps suggesting" larger models are better meta-learners (p. 6).
- Arithmetic: 0.8% of problems found in training data *suggests* trivial memorization; missed carries *suggest* attempted computation (p. 23).
- Scrambling tasks *appear* learned at test time; "cannot confirm" (p. 24).
- Limits: every token weighted equally; not grounded in video or physical interaction; pure self-supervised scaling *likely* hits limits (pp. 33–34).

**Numbers & equations.** 175B, 96 layers, $d_{model}=12288$, $n_{ctx}=2048$, 300B tokens (p. 8). $L=2.57\,C^{-0.048}$ (p. 11). LAMBADA 76.2/72.5/86.4 vs SOTA 68.0 (p. 12); TriviaQA 64.3/68.0/71.2 (p. 13). Few-shot 2D+ 100.0, 3D+ 80.4, 5D+ 9.3 (p. 23); WiC 49.4 (p. 20). News detection ≈52% vs control ≈86% (pp. 25–26).

**Instance.** "Alice was friends with Bob. Alice went to visit her friend ____. → Bob" (p. 12): the fill-in-the-blank *format* shown to the model, with its answer; not a reported model output.

**Careful!** No weights change in "few-shot learning". A filtering bug left some overlap (p. 9). 3D+ is 80.2 in text, 80.4 in table.

### 11. Kaplan et al. (2020), *Scaling Laws* (pp. 1–30)
**Claims**
- Loss depends strongly on scale, very weakly on shape (pp. 3, 8). Doubling $N$ multiplies loss by 0.95 (p. 5).
- Constants $N_c,D_c,C_c$ "have no fundamental meaning" (p. 5).
- $D\gtrsim(5\times10^3)N^{0.74}$ avoids overfitting; 8× model needs ≈5× data (pp. 3, 12).
- Compute-optimal $N\propto C_{\min}^{0.73}$; stop well before convergence (pp. 3, 16).
- Trends must flatten out eventually before zero loss (p. 3), since language has non-zero entropy (p. 17). Extrapolated $L(D(C_{\min}))$ and $L(C_{\min})$ contradict each other near $N^*\sim10^{12}$, $L^*\sim1.7$ nats/token; the "most obvious interpretation" is that the laws break down *at or before* this point; numbers uncertain by an order of magnitude (p. 17). *Further conjecture:* $L^*$ *might* give a rough estimate of the entropy per token (p. 18).
- No theory (p. 22); smooth loss "may hide seemingly qualitative changes in capability" (p. 19).

**Equations.** Loss in **nats**/token over 1024 tokens; $N$ excludes embeddings (p. 6).
$$L(N)=(N_c/N)^{0.076},\ \ L(D)=(D_c/D)^{0.095},\ \ L(C_{\min})=(C_c^{\min}/C_{\min})^{0.050}\ (\text{p. 4});\quad L(N,D)=\Big[\Big(\tfrac{N_c}{N}\Big)^{\alpha_N/\alpha_D}+\tfrac{D_c}{D}\Big]^{\alpha_D}\ (\text{p. 5})$$
Code-checked: $2^{-0.076}=0.949$, $8^{0.74}=4.66$, $10^{0.73}=5.37$.

**Instance.** Billion-fold compute: >10⁶× model, ≈100× batch, <10× steps (Fig. 3, p. 4).

**Careful!** Fits of *test* loss on WebText2 (p. 6), not ability; $L(N)$ is for models trained to convergence on large data (p. 4). Not "training loss". $\alpha_D$ 0.095 vs 0.103; $C_c^{\min}$ 3.1e8 vs 2.3e8 in figures.

---

## D. Bayesian

### 12. Xie et al. (2022), *ICL as Implicit Bayesian Inference* (pp. 1–31)
**Claims**
- *Assumes* documents from a mixture of HMMs with latent concept θ, and an LM that fits pretraining exactly (pp. 2–3).
- Prompts are low-probability under pretraining (mismatch) (p. 4).
- If $p(\text{concept}\mid\text{prompt})$ concentrates, the LM "selects" the concept by marginalization (p. 3).
- Thm 1: under the assumptions *and* distinguishability, optimal 0-1 risk as $n\to\infty$ (p. 7). Longer examples help; inputs carry signal too (pp. 7–8).
- GINC: unseen concepts or one concept → ICL fails (p. 10). Same loss 1.33, ICL 81.2 vs 84.7 (12 vs 16 layers): larger models *may* gain beyond loss (p. 10). In GINC (4-layer Transformer, synthetic data) order shifts accuracy 10–40%, similar to GPT-3 per Zhao et al.; zero-shot can beat few-shot (pp. 10–11).
- "A first step" (p. 12).

**Equations.** GPT-3 LAMBADA 5-shot short 69.8, long 70.7; 10 duplicated 69.6; 10 independent 71.4 (p. 30).
$$p(\text{output}\mid\text{prompt})=\int p(\text{output}\mid\text{concept},\text{prompt})\,p(\text{concept}\mid\text{prompt})\,d(\text{concept})\ (\text{p. 2})$$
$$p(o_{1:T})=\int_\Theta p(o_{1:T}\mid\theta)p(\theta)d\theta\ (\text{p. 3});\quad \text{weight}(\theta)\propto e^{n\,r_n(\theta)}p(\theta)\ \text{(proportional to, not grows like)},\ r_n=\tfrac1n\log\tfrac{p(S_n,x\mid\theta)}{p(S_n,x\mid\theta^*)}\ (\text{p. 6})$$
$$\textstyle\sum_{j=1}^kKL_j(\theta^*\|\theta)>\epsilon_{\text{start}}^\theta+\epsilon_{\text{delim}}^\theta\quad(\text{Condition 1, p. 7})$$

**Instance.** "Albert Einstein was German \n Mahatma Gandhi was Indian \n Marie Curie was" → Polish (p. 1).

**Careful!** A theorem inside a stylized model, tested on synthetic data; it does not show real LLMs compute posteriors.

---

## E. Philosophy of meaning

### 13. Bender & Koller (2020), *Climbing towards NLU* (pp. 5185–5198)
**Claims**
- LM = any system trained only on string prediction; meaning = relation between form and communicative intent (p. 5185).
- Form-only training "cannot in principle" lead to learning meaning (p. 5185).
- $M\subseteq E\times I$; standing meanings $C\subseteq E\times S$ must have interpretations (p. 5187).
- The octopus *may* pass in social chat but fails at the bear; the listener does the sense-making (pp. 5188–5189).
- Children learn through interaction and joint attention, not passive exposure (p. 5190).
- With grounding data, meaning can "conceivably" be learned (p. 5192); quantity of form is "not relevant" (p. 5193).
- BERT has "probably learned something about meaning" (§9); LMs learn "some reflection of meaning into the linguistic form" (§10); useful but incomplete (both p. 5193). Two separate sentences: do not splice.

**Numbers.** GPT-2 on "Three plus five equals": seven, six, unrelated, ten, five (p. 5198).

**Instance.** The octopus test; Java without I/O; text plus unconnected photos (pp. 5188–5190).

**Careful!** They do not say LMs learn nothing; the claim concerns form→intent and "human-analogous NLU"; evidence is BERT/GPT-2 era.

### 14. Piantadosi & Hill (2022), *Meaning without reference* (pdf 1–8)
**Claims**
- Contests that LLMs are *necessarily* meaningless; meanings may be similar "in many (but not all) ways" (pdf 1).
- The octopus test *assumes* reference determines meaning (pdf 1–2): "justice", "king of San Francisco", morning/evening star, postage stamp (pdf 2).
- Conceptual role: meaning mainly from relations ($f=m\cdot a$) (pdf 2).
- If so, meaning cannot be read off architecture or objective; examine internal relations (pdf 3).
- Whether prediction discovers roles is "empirical"; a "promising, partial affirmative" (pdf 4). Embedding theorems and AlphaFold are *analogies* making it "plausible" (pdf 5).
- Reference is one *optional* aspect (pdf 4). "If conceptual role theories are correct, LLMs likely already share the foundation" (pdf 5).

**Instance.** The postage stamp (pdf 2).

**Careful!** Conditional claim in a short comment; no claim of human-level meaning.

### 15. Mahowald et al. (2024), *Dissociating language and thought* (pp. 1–18 of arXiv:2301.06627v3, "A PREPRINT"; not the *TiCS* typeset pages)
**Claims**
- Fallacies: good at language → good at thought; bad at thought → bad at language (p. 2).
- Formal competence = rules and statistical regularities; functional = using language in the world (short definitions p. 2; longer p. 3).
- The human language network ignores arithmetic, logic, music, mental-state reasoning; global aphasics still do arithmetic and chess (p. 5).
- English formal competence near human level; functional "patchy" (p. 2). Prediction gives formal but "not necessarily" functional competence (p. 2); not out of reach in principle (p. 14).
- Lexical/compositional semantics count as *formal* (Box 2, p. 7).
- ToM: mastery claim [185] vs controls below chance [186] (p. 14); "particularly large" overclaiming on functional skills (p. 11).

**Numbers.** BLiMP 86% (BabyLM) vs human 89% (p. 7); a construction with 58 examples in 7B sentences (p. 8).

**Instance.** "The keys to the old, wooden kitchen cabinet *are*…" (pp. 7–8).

**Careful!** Brain dissociation motivates, does not prove, modularity. Refs [185]/[186] are unnamed in the digest; check before naming Kosinski/Ullman.

---

## F. Theory of mind

### 16. Kosinski (2024), PNAS (§ headings)
**Claims**
- ToM *may* emerge as a by-product of training (§ "Abstract"; the source has no "Introduction" heading).
- 40 bespoke tasks; 8 scenarios (false belief, 3 true-belief controls, reversals) × 2 prompts, all 16 correct (§ "Abstract", § "Study 3").
- GPT-1/2 none; davinci-002 5%; davinci-003 and ChatGPT-3.5 20%; ChatGPT-4 75% [66, 84], "on par with 6-year-olds" (meta-analysis, 178 studies) (§ "Study 3").
- Earlier scores higher: davinci-003 90 → 60 → 20%; ChatGPT-4 95 → 75% (§ "Study 3").
- Failures do not *necessarily* indicate inability ("do not prove their inability"); successes do not prove ToM; failures can still give "valuable insights" (§ "Discussion").
- Leaves credit for ToM open; Turing-style "polite convention" (§ "Conclusion").

**Numbers.** $(1/2)^{16}=1/65{,}536$ (§ "Discussion"). Contents 90% vs transfer 60%; R = 0.98 across task types (§ "Study 3", § "Discussion").

**Instance.** Sam's popcorn bag labelled "chocolate", revealed sentence by sentence (§ "Study 1.1", § "Study 1.4").

**Careful!** Strict scoring; child comparison uses different procedures. Text says older models failed all, yet davinci-002 = 5%.

### 17. Ullman (2023), *Trivial Alterations* (pp. 1–11)
**Claims**
- Quotes Kosinski's preprint: GPT-3.5 comparable to 9-year-olds (p. 2).
- One failure outweighs averages: a *machine* that answers 100 easy products but fails 213×261 has probably not learned a general multiplication algorithm (p. 2).
- Has ToM emerged? "Probably not"; presume strongly it has not (p. 8).
- A later LLM *may* pass; a benchmark can be absorbed (pp. 8–9).
- One can doubt LLM ToM yet trust tests for people, judging likely algorithms (p. 9).

**Numbers (GPT-3.5).** Transparent bag P(chocolate) 95%; cannot read 98%; trusted friend 97%; Sam writes label 87% (pp. 3–5). Transparent containers P(chest) 94/90%; phone call P(basket) 97/94%; asking about Mark P(basket) 99/54% (pp. 6–8).

**Instance.** The transparent popcorn bag (p. 3).

**Careful!** One model, few variants, no repeated runs. In 1A prompt 2 there was *no* flip (58/36%; p. 3).

### 18. Strachan et al. (2024), Nat. Hum. Behav. (§ headings)
**Claims**
- Five tests, 15 sessions per model, 1,907 humans (§ "Main").
- False belief at ceiling; LLM success *may* have lower-level explanations; humans (N = 757) also failed half of Ullman-style perturbations, which change physical properties (§ "False belief").
- GPT-4 above humans on irony, hinting, strange stories; below on faux pas (§ "Irony", § "Hinting", § "Strange stories", § "Faux Pas", under "Performance across theory of mind tests").
- Faux pas errors were "not enough information"; 2/349 said "knew" (§ "Understanding faux pas"). Likelihood wording → GPT-4 perfect: supports *hyperconservatism*.
- LLaMA2-70B's faux pas success *may* be a "didn't know" bias (§ "Testing information integration").
- Mitigation measures *may*, disembodiment "could", explain it (§ "Discussion").

**Numbers.** Irony P = 0.040, r = 0.32; faux pas P = 5.42×10⁻⁵, r = 0.55 (§ "Irony", § "Faux Pas"); $r=Z/\sqrt N$ (§ Methods).

**Instance.** The curtains faux pas (§ "Understanding faux pas").

**Careful!** Test-specific; authors deny output imitation implies human cognition. Reported Z values are inconsistent; cite P and r only.

### 19. Shapira et al. (2024), *Clever Hans or Neural ToM?* (pp. 2257–2273)
**Claims**
- 15 LLMs, 6 datasets: "no model robustly exhibits ToM on all datasets" (p. 2261). Probing method changes scores (p. 2261).
- ToMi′ vs ToM-k gap *suggests* no generalization; models *might* recognize Sally–Anne patterns (p. 2262).
- GPT-4: 97.5% on original false-belief transfer items, 0% on in→on and transparent access (pp. 2262–2263).
- Hedged causes: reporting bias, instruction tuning, recency bias ("might") (p. 2264).
- Kosinski/Bubeck over-generalized from 40/10 examples; they say "proving" no robust N-ToM (p. 2264). Fail one task → no ToM in general (p. 2265).
- Emergence claims "unfounded" and "unfalsifiable" without training data (p. 2265).

**Numbers.** ToMi′/ToM-k: davinci-003 10/87, GPT-3.5 27/65, GPT-4 20/87 (p. 2262). FauxPas-EAI 27% vs baseline 30% (p. 2261). Rerun of Kosinski: 85–90% vs reported 93% (pp. 2272–2273).

**Instance.** Cat placed *on* the box: GPT-4 0% (p. 2263).

**Careful!** Their rule is a stance; they concede physics may explain some failures (p. 2266). Self-contradiction on transparent access (p. 2263).

---

## Cross-source tensions
1. **Meaning from form.** B&K: "cannot in principle" (p. 5185). P&H: B&K *assume* reference fixes meaning (pdf 1–2); relations in text may carry meaning (pdf 4). Shared ground: richer input enriches (B&K p. 5192; P&H pdf 4); "reflection of meaning" (p. 5193) vs "foundation" (pdf 5). Mahowald counts lexical semantics as formal (p. 7). GPT-3's authors list lack of grounding as a limit (p. 34).
2. **Embedding geometry.** Mikolov: offsets are likelihood byproducts, ≈40–66% exact (2013b p. 749; 2013a p. 9). B&K: "only a weak reflection" (p. 5193). P&H: evidence of conceptual role (pdf 3).
3. **ToM.** *Versions:* Ullman (p. 2) and Shapira (pp. 2272–2273) target Kosinski's preprint; PNAS has davinci-003 at 20%, ChatGPT-4 at 75% after controls. *Asymmetry:* one failure decides (Ullman p. 2; Shapira p. 2265) vs a failure does not *necessarily* show inability (Kosinski § "Discussion"). *Perturbations:* humans fail half too (Strachan § "False belief"); physics confound (Shapira p. 2266). *Behaviour vs process:* Turing (Kosinski) vs algorithms (Ullman p. 9).
4. **What ICL learns.** GPT-3: agnostic, scrambling *seems* de novo (pp. 4, 24, 34). Xie: concept *selection* from pretraining; unseen concepts fail (p. 10).
5. **Smooth loss vs jumps.** Kaplan smooth (p. 4) yet "may hide" (p. 19); GPT-3 arithmetic jump 13B→175B (p. 22); Xie: ICL varies at equal loss (p. 10).
6. **Entropy floor.** Shannon ≈1 bit/letter (p. 50) vs Kaplan $L^*\approx1.7$ nats/token, where two trends contradict (laws break down at or before it, p. 17); reading it as entropy is a further conjecture (p. 18). Our rough conversion: 2.45 bits/token ÷ 0.7 words/token (GPT-3 p. 24) ÷ 4.5 letters/word (Shannon p. 53) ≈ 0.78 bits/letter. This mixes alphabets (Shannon's ~1 bit is for 27 symbols with space; 4.5 letters/word excludes spaces). Kaplan's own fn. 7 (4.3 characters per token on WebText2) gives 2.45/4.3 ≈ 0.57 bits/character (p. 18). Different corpora and tokenizers: a talking point only.
7. **Memorization.** GPT-2 "small but consistent" (pdf 8); GPT-3 0.8% (p. 23); Ullman: benchmarks get absorbed (p. 9); Shapira: unfalsifiable without data (p. 2265).

---

## Toy-example ideas (numbers checked by code)
**T1. 4-word language.** True $p=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$ (Cover pp. 14–15). Average $-\log_2q$ under $p$ (= $H+D$, Cover p. 18): true model 1.75 bits, perplexity 3.36; uniform 2.00 bits ($D=0.25$), perplexity 4; reversed $(\tfrac18,\tfrac18,\tfrac14,\tfrac12)$ 2.625 bits ($D=0.875$), perplexity 6.17.

**T2. Shannon's Example C as a bigram table** (p. 6). Stationary (1/3, 16/27, 2/27) (checked). $F_0=1.585$, $F_1=1.254$; row entropies 0.722 / 1.000 / 1.361; $F_2=0.934$ bits. Perplexity 3 → 2.38 → 1.91. The zero cells are true zeros in this language. In real text many possible sequences are merely unseen; n-grams avoid zero by back-off/smoothing (p. 1138), and Bengio's vectors target generalization through word similarity (p. 1139).

**T3. 3-token causal attention, $d_k=2$.** $Q=K=[(1,0),(0,1),(1,1)]$, $V=[(1,0),(0,1),(2,2)]$. Row-3 scores $/\sqrt2$: 0.707, 0.707, 1.414. Weights: (1,0,0); (0.330, 0.670, 0); (0.248, 0.248, 0.504). Outputs: (1,0); (0.330, 0.670); (1.255, 1.255). Hand values $e^{0.707}=2.028$, $e^{1.414}=4.113$.

**T4. Two-concept ICL** (Xie eq. 1). Prior ½–½; per-example likelihood 0.2 vs 0.05; right answer 0.9 vs 0.1 (invented). Posterior/answer: $n=0$ 0.50/0.50; 1: 0.80/0.74; 2: 0.941/0.853; 3: 0.985/0.888; 4: 0.996/0.897. Mismatch version: join penalty ×1.5 vs per-token 0.8 → selection needs $k\ge2$ (0.446 > 0.405 nats).

**T5. 3-D analogy** (Mikolov 2013b). man (1,0,0), woman (0,1,0), king (0.6,0,0.8), queen (0,0.6,0.8). $y=(-0.4,1,0.8)$, $\|y\|=1.342$. Cosines: queen 0.924, woman 0.745, king 0.298, man −0.298.

*Optional T6.* "Copy the label" gets 4/8 belief prompts in Kosinski's design; coin flips pass with $1.5\times10^{-5}$.

**Also check at source:** Shannon 1948 sample texts (p. 7); GPT-2 eq. (1) misprint; Kosinski 1,000 vs 2,000 runs; Shapira Table 9 vs Table 4 (p. 2273).
