---
id: hoffmann-2022-chinchilla/main
work: hoffmann-2022-chinchilla
unit: paper
pages: 1-36
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Training Compute-Optimal Large Language Models (Hoffmann et al., 2022)

## L0 — One line
For a fixed compute budget, the authors estimate that model size and number of training tokens should grow in roughly equal proportion, which implies that the large models of the time were over-sized and under-trained, and they test this with Chinchilla (70B parameters, 1.4T tokens).

## L1 — The gist (≤ 120 words)
Given a fixed training-compute budget, how large should a language model be, and on how many tokens should it train? The authors estimate the best split with three methods, all based on training many models (over 400 runs in total). All three suggest that model size and training tokens should grow in roughly equal proportion with compute, unlike the earlier Kaplan et al. recommendation. They test this by training Chinchilla (70B parameters, 1.4T tokens) with Gopher's compute budget. Chinchilla outperforms the 280B Gopher and other larger models on most evaluations. The authors conclude that the large models of the time were over-sized and under-trained, and that larger, high-quality datasets will play a key role in further scaling.

**Prerequisites:** power laws and log-log plots; minimizing a function under a constraint (derivative = 0); the idea of training loss, learning-rate schedules, and 0/5-shot evaluation. Terms: FLOPs = floating-point operations (a measure of compute); token = a unit of text; Gopher = an earlier 280B-parameter model trained on 300B tokens; IsoFLOP = compared at equal FLOPs; epoch = one pass over the training data; MMLU and Winogender = benchmarks (a multi-subject exam test and a pronoun-resolution test).

## L2 — Key ideas (5–10 bullets)
- **The question.** Choose $N_{opt}(C), D_{opt}(C)$ to minimize final loss subject to FLOPs$(N,D)=C$ (Eq. 1). The authors say compute budgets are often known in advance and that it is typically feasible to train such large models only once (pp. 1–2).
- **Disagreement with Kaplan et al.** For 10× more compute, Kaplan et al. suggest 5.5× larger models but only 1.8× more tokens. This paper finds equal scaling. The authors say the earlier work's fixed token count and learning-rate schedule prevented it from modelling their effect, which contributes to the gap (p. 3).
- **Three estimators give similar exponents.** Training-curve envelope, IsoFLOP profiles and a parametric loss fit give exponents $a$ (model size) of 0.50, 0.49 and 0.46, and $b$ (tokens) of 0.50, 0.51 and 0.54, versus 0.73/0.27 for Kaplan et al. (pp. 5–8).
- **Parametric form.** $\hat L = E + A/N^\alpha + B/D^\beta$ has a closed-form frontier with $a=\beta/(\alpha+\beta)$ and $b=\alpha/(\alpha+\beta)$ (pp. 6–7).
- **Implication for existing models.** The authors find the current generation of large models (Figure 1 shows Gopher, GPT-3 and MT-NLG) considerably over-sized for their compute budgets. Optimal training token counts are far beyond current data use (p. 8).
- **Direct test.** Chinchilla (70B, 1.4T tokens) uses Gopher's compute and beats Gopher, GPT-3, Jurassic-1 and MT-NLG on most tasks. It reaches 67.6% on MMLU, 7.6 points above Gopher (pp. 9–13).
- **Side effects.** A smaller model costs less for inference and fine-tuning. Bias and toxicity are not eliminated: gains on Winogender are uneven, and unprompted toxicity is about the same as Gopher's (pp. 14–15).
- **Stated limitations.** There are only two large-scale comparable runs. A power law is assumed, though the frontier shows some concavity, which may mean the optimal model is smaller still. All runs use less than one epoch (p. 15).

## L3 — Walkthrough

### Abstract and 1. Introduction (pp. 1–2)
- **Setting.** The largest dense language models now have over 500B parameters. Training cost rises with size, the compute budget is often known in advance, and it is typically feasible to train such models only once. Estimating the best hyperparameters for a given budget is therefore critical (p. 1).
- **Kaplan et al. (2020).** They showed a power-law relation between parameters and performance, and concluded that large models should not be trained to their lowest possible loss to be compute optimal. The authors agree with this conclusion, but estimate that large models should be trained on many more tokens. For a 10× larger budget, Kaplan et al. suggest 5.5× larger models and only 1.8× more tokens. This paper finds that size and tokens should scale in equal proportions (p. 1).
- **Practice.** Following Kaplan et al. and GPT-3, many recent large models were trained on about 300B tokens (Table 1) (p. 1).
- **Formal question.** Model the final pre-training loss $L(N,D)$, where $N$ is parameters and $D$ is training tokens. Compute $C$ is a deterministic function FLOPs$(N,D)$. Then:

$$N_{opt}(C),\,D_{opt}(C)=\operatorname*{argmin}_{N,D\ \text{s.t.}\ \mathrm{FLOPs}(N,D)=C} L(N,D) \tag{1}$$

- **Evidence.** They estimate these functions from over 400 models (under 70M to over 16B parameters, 5B to over 400B tokens), each configuration trained for several training horizons (p. 2).
- **Footnote 2.** Smoothed training loss is used. It is described as an unbiased estimate of test loss, because the number of training tokens is smaller than the corpus ("infinite data regime") (p. 2).
- **Prediction and test.** For Gopher's budget, an optimal model should be 4× smaller and trained on 4× more tokens. They train Chinchilla (70B, 1.4T tokens) to check this. A smaller model also reduces inference cost, and energy cost is amortized over inference and fine-tuning (p. 2).
- **Table 1** (size / tokens): LaMDA 137B/168B; GPT-3 175B/300B; Jurassic 178B/300B; Gopher 280B/300B; MT-NLG 530B/270B; Chinchilla 70B/1.4T (p. 3).

**Intuition note.** With a fixed budget, every extra parameter costs training tokens. If compute is split badly, a huge model sees too little data and a small model sees too much for its capacity. The paper asks where the best split lies.

### 2. Related Work (pp. 3–4)
- **Large models.** Dense and mixture-of-experts (MoE) models are listed. The authors say that in this work they find that larger, high-quality datasets will play a key role in any further scaling (p. 3).
- **How this work differs from Kaplan et al.** (p. 3)
  1. Kaplan et al. use a fixed number of training tokens and a fixed learning-rate schedule for all models, so they cannot model the effect of these choices.
  2. The authors find that setting the learning-rate schedule to roughly match the number of training tokens gives the best final loss regardless of model size (Figure A1).
  3. With a cosine schedule fixed to 130B tokens, intermediate losses at $D' \ll 130$B overestimate the loss of a model trained with a schedule matching $D'$. This underestimates the effectiveness of training on less data. The authors say it eventually contributes to the conclusion that model size should grow faster than data.
  4. They include models up to 16B because they observe slight curvature in the FLOP–loss frontier (Appendix E). Most of their models have over 500M parameters, whereas most runs of Kaplan et al. are much smaller, many under 100M.
- **Clark et al. (2022)** studied MoE scaling at a fixed token count, as in Kaplan et al. The authors say this potentially underestimates the improvements of branching (pp. 3–4).
- **Other hyperparameters.** This work focuses on model size and training steps and relies on existing heuristics for the rest (learning rate, batch size, optimiser, depth/width). It uses slightly less deep models than Levine et al. propose, because they run faster on the authors' hardware (p. 4).
- **Architectures.** Retrieval augmentation (Borgeaud et al.) effectively increases the data tokens seen by a factor of about 10. The authors say this suggests performance may depend more on training-data size than previously thought. Routed models seem to lose their computational benefit at very large size (Clark et al.) (p. 4).

### 3. Estimating the optimal parameter/token allocation (pp. 4–8)
All three approaches train many models of varying size and token count, then fit an empirical estimator. All assume a power law between compute and model size, though future work may include curvature. The predictions are similar and suggest that parameters and tokens should increase equally with compute (Table 2). The authors say this is in clear contrast to previous work on the topic and warrants further investigation (p. 4). FLOPs are computed as in Appendix F.

**3.1 Approach 1: fix model sizes, vary training tokens (p. 5).**
- Models from 70M to over 10B parameters. For each size, 4 runs decay the learning rate by 10× over horizons that span a factor of 16× in tokens.
- Each run's loss curve is smoothed and interpolated, giving a continuous map from FLOPs to loss. At 1500 log-spaced FLOP values, the lowest-loss run gives the efficient $(N,D)$ with FLOPs$(N,D)=C$.
- Power laws $N_{opt}\propto C^a$, $D_{opt}\propto C^b$ are fitted to these points. Result: $a=0.50$, $b=0.50$.
- Footnote 4: all selected points lie within the last 15% of training. This suggests that, when training over $D$ tokens, one should pick a cosine cycle that decays 10× over about $D$ tokens (Appendix B).
- Section D.4 reports a head-to-head at $10^{21}$ FLOPs, favouring the size this approach recommends (details in D.4 below).

**3.2 Approach 2: IsoFLOP profiles (pp. 5–6).**
- Vary model size (up to 16B) at 9 fixed FLOP budgets from $6\times10^{18}$ to $3\times10^{21}$, and use the final loss for each point. The number of tokens follows from size and FLOPs, and the cosine length is matched to the token count.
- The authors say they trained enough sizes to see a clear loss minimum per budget. A parabola is fitted to each IsoFLOP curve to locate the loss-minimizing size. Power laws are then fitted: $a=0.49$, $b=0.51$ (Figure 3).

**3.3 Approach 3: parametric loss (pp. 6–7).** All final losses from Approaches 1 and 2 are modelled as

$$\hat L(N,D) \triangleq E+\frac{A}{N^{\alpha}}+\frac{B}{D^{\beta}}. \tag{2}$$

- Term roles, following a "classical risk decomposition" (Section D.2): $E$ is the loss of an ideal generative process, which, the authors say, should correspond to the entropy of natural text. $A/N^\alpha$ is the underperformance of a perfectly trained $N$-parameter transformer. $B/D^\beta$ is the cost of finite optimisation steps on a sample of the data (p. 6).
- **Fitting.** Minimize the Huber loss between predicted and observed log loss, using L-BFGS:

$$\min_{A,B,E,\alpha,\beta}\ \sum_{\text{Runs } i}\mathrm{Huber}_\delta\!\big(\log\hat L(N_i,D_i)-\log L_i\big) \tag{3}$$

- The best fit comes from a grid of initialisations, to account for local minima. $\delta=10^{-3}$. The Huber loss is robust to outliers, which the authors find important for predicting held-out points (p. 6).
- **Efficient frontier.** Minimize $\hat L$ under FLOPs$(N,D)\approx 6ND$ (Kaplan et al.). The result has power-law form:

$$N_{opt}(C)=G\Big(\tfrac{C}{6}\Big)^{a},\quad D_{opt}(C)=G^{-1}\Big(\tfrac{C}{6}\Big)^{b},\quad G=\Big(\tfrac{\alpha A}{\beta B}\Big)^{\frac1{\alpha+\beta}},\ a=\tfrac{\beta}{\alpha+\beta},\ b=\tfrac{\alpha}{\alpha+\beta}. \tag{4}$$

- Section 3 states the power-law form "by construction" and gives no derivation there. *(Added step)* Substitute $D=C/(6N)$. Then $\hat L = E + AN^{-\alpha} + B(C/6)^{-\beta}N^{\beta}$. Setting $d\hat L/dN=0$ gives $\alpha A N^{-\alpha}=\beta B (C/6)^{-\beta}N^{\beta}$, so $N^{\alpha+\beta}=\frac{\alpha A}{\beta B}(C/6)^{\beta}$. This yields $N_{opt}$ as in Eq. (4), and $D_{opt}=(C/6)/N_{opt}$ follows.
- Result for this approach: $a=0.46$, $b=0.54$ (Figure 4). For Gopher's FLOP budget it projects an optimal size of 40B parameters (Figure 4 caption).

**Intuition note.** The text says the optimum balances the two terms of the loss that depend on model size and on data (p. 7). If the data exponent $\beta$ is larger than the size exponent $\alpha$, then $a>b$. If $\alpha\approx\beta$, the two grow together.

**3.4 Optimal model scaling (pp. 7–8).**

| Approach | $a$ ($N_{opt}\propto C^a$) | $b$ ($D_{opt}\propto C^b$) |
|---|---|---|
| 1. Min. over training curves | 0.50 (0.488, 0.502) | 0.50 (0.501, 0.512) |
| 2. IsoFLOP profiles | 0.49 (0.462, 0.534) | 0.51 (0.483, 0.529) |
| 3. Parametric loss | 0.46 (0.454, 0.455) | 0.54 (0.542, 0.543) |
| Kaplan et al. (2020) | 0.73 | 0.27 |

(Table 2, p. 8. Parentheses are the 10th and 90th percentiles from bootstrapping: 80% of the data sampled 100 times.)

- Approaches 1 and 2 give very similar model sizes. Approach 3 predicts even smaller models at larger budgets (p. 7).
- **Explanation of the Approach 3 difference.** Points with $C\le 1e21$ have larger residuals. The Huber loss effectively treats them as outliers, so the fit gives more weight to high-FLOP points. Because the observed frontier $C\to N_{opt}$ has negative curvature (Appendix E), this lowers the predicted $N_{opt}$ (p. 7).
- **Table 3** (Approach 1; FLOPs / tokens): 400M: 1.92e19 / 8.0B; 1B: 1.21e20 / 20.2B; 10B: 1.23e22 / 205.1B; 67B: 5.76e23 (=1 Gopher unit) / 1.5T; 175B: 3.85e24 / 3.7T; 280B: 9.90e24 / 5.9T; 520B: 3.43e25 / 11.0T; 1T: 1.27e26 / 21.2T; 10T: 1.30e28 / 216.2T (p. 8).
- **Text conclusions.** Current LLMs are "considerably over-sized" for their budgets. The text gives 4.41e24 FLOPs and over 4.2T tokens for 175B, and about 1e25 FLOPs and 6.8T tokens for a 280B Gopher-like model. A 1T-parameter model is unlikely to be optimal unless the budget is 1e26 FLOPs (the text says over 250× Gopher's compute). Needed data is far beyond current use, which underlines the importance of dataset collection. The authors acknowledge significant uncertainty in extrapolating many orders of magnitude (p. 8).
- **Other datasets (Appendix C).** On C4 and GitHub code, IsoFLOP analysis gives a similar conclusion (p. 8).

### 4. Chinchilla (pp. 9–15)
- **Choice.** Approaches suggest the optimum for Gopher's budget is between 40B and 70B parameters. They train 70B for 1.4T tokens (the larger end), for dataset and computational efficiency reasons. Both models use the same FLOPs. Chinchilla is 4× smaller, so its memory footprint and inference cost are lower (p. 9).

**4.1 Model and training details (p. 9).** Same architecture and setup as Gopher except:
- slightly different MassiveText subset distribution (Table A1);
- AdamW instead of Adam, which improves language-modelling loss and downstream performance after fine-tuning. Footnote 8: the AdamW model passes the Adam model's training performance only about 80% of the way through the cosine cycle, but ends notably better;
- a SentencePiece tokenizer without NFKC normalisation (94.15% of tokens shared with Gopher's), which helps with mathematics and chemistry;
- a float32 weight copy in the distributed optimiser state, with bfloat16 forward/backward passes.

Table 4: Gopher 280B has 80 layers, 128 heads, $d_{model}=16{,}384$, max LR $4\times10^{-5}$, batch 3M→6M. Chinchilla 70B has 80 layers, 64 heads, $d_{model}=8{,}192$, max LR $1\times10^{-4}$, batch 1.5M→3M. Key/value size is 128 and feed-forward size is $4\times d_{model}$. Batch size doubles midway for both.

**4.2 Results (pp. 10–15).** Tasks follow Rae et al. (2021) for direct comparison (Table 5: 20 language-modelling tasks, 3 reading comprehension, 3 QA, 5 common sense, 57 MMLU, 62 BIG-bench).

- **4.2.1 Language modelling (p. 10).** Chinchilla beats Gopher on all Pile subsets, and beats Jurassic-1 on all but two (dm_mathematics, ubuntu_irc). Wikitext103 perplexity is 7.16 versus 7.75 for Gopher. The authors caution that train/test leakage may artificially help Chinchilla, since it saw 4× more data. They therefore put more emphasis on MMLU, BIG-bench, closed-book QA and common sense (pp. 10–11).
- **4.2.2 MMLU (p. 11).** Average 5-shot accuracy is 67.6% (+7.6 over Gopher's 60.0%). Other Table 6 rows: random 25.0, average human rater 34.5, GPT-3 43.9, average human expert 89.8. Chinchilla exceeds the June 2023 forecast of 63.4% (73 forecasters, Steinhardt). It scores above 90% on four tasks (high_school_gov_and_politics, international_law, sociology, us_foreign_policy). The authors say, "to our knowledge", no other model has done this on a subset. Chinchilla is better on 51/57 tasks, the same on 2, and worse on 4 (college_mathematics, econometrics, moral_scenarios, formal_logic) (Figure 6, pp. 11–12).
- **4.2.3 Reading comprehension (pp. 11–12).** LAMBADA 77.4% (Gopher 74.5, MT-NLG 76.6). RACE-m 86.8 vs 75.1 and RACE-h 82.3 vs 71.6, both improvements above 10 points. GPT-3 and MT-NLG use a different prompt format on RACE, so those numbers are not comparable (Table 7).
- **4.2.4 BIG-bench (pp. 11–13).** Average accuracy 65.1% vs 54.4% for Gopher (+10.7). Chinchilla is worse on only four of 62 tasks (crash_blossom, dark_humor_detection, mathematical_induction, logical_args).
- **4.2.5 Common sense (p. 12).** On PIQA, SIQA, Winogrande, HellaSwag and BoolQ (Table 8, zero-shot), the authors say Chinchilla outperforms Gopher and GPT-3 on all tasks and MT-NLG on all but one (PIQA: 81.8 vs 82.0). TruthfulQA: 43.6 / 58.5 / 66.7% at 0 / 5 / 10 shots; Gopher 29.5 (0-shot) and 43.7 (10-shot). **Authors' reading:** the 14.1-point 0-shot gain contrasts with Lin et al. and suggests that better modelling of the pre-training data alone can give substantial improvements here.
- **4.2.6 Closed-book QA (pp. 13–14).** Natural Questions: 31.5% (5-shot) and 35.5% (64-shot), described as new closed-book SOTA (text gives Gopher 21% and 28%; Table 9 gives 24.5% and 28.2%). TriviaQA filtered: Chinchilla lags the open-book SOTA by 7.9 points. Unfiltered: it beats GPT-3.
- **4.2.7 Gender bias and toxicity (pp. 14–15).** The authors expect risks similar to Gopher's (same data, similar architecture) and stress that their evaluations are not comprehensive.
  - *Winogender (Table 10).* Chinchilla resolves pronouns better in every group: all 78.3 vs 71.4; male 71.2 vs 68.0 (+3.2); female 79.6 vs 71.3 (+8.3); neutral 84.2 vs 75.0 (+9.2). On "gotcha" examples (correct answer contradicts a stereotype), the largest gain is female gotcha, 76.7 vs 66.7 (+10). **Authors' conclusion:** gains from a more compute-optimal model "can be uneven"; differences across groups suggest Chinchilla still exhibits bias.
  - *Toxicity.* 25,000 unprompted samples, scored with PerspectiveAPI. Mean (median): Gopher 0.081 (0.064), Chinchilla 0.087 (0.066). 95th percentile: 0.230 vs 0.238. The authors read this as negligible difference. Following Rae et al., it suggests that unprompted toxicity is largely independent of model quality (language-modelling loss), so better models of the data are not necessarily more toxic.

**Intuition note.** Chinchilla is the real-world test of the prediction. Same compute, 4× fewer parameters, 4× more data, better results on nearly all tasks. This supports the claim that the larger models were under-trained. It is one comparison, not a proof (see limitations).

### 5. Discussion & Conclusion (pp. 15–16)
- **Hypothesis.** The authors hypothesize that the race to larger and larger models, often without more training tokens (most existing large models use around 300B), is resulting in models that substantially underperform what the same compute could achieve (p. 15).
- **Limitations (authors').** (i) Only two comparable large-scale runs (Chinchilla, Gopher), no intermediate-scale tests. (ii) A power law is assumed, but there is some concavity in $\log N_{opt}$ at high budgets, which, the authors say, suggests they may still be overestimating the optimal size of large models. (iii) All runs use less than one epoch (p. 15).
- **Data.** The analysis suggests more focus on dataset scaling. **Speculatively**, the authors expect larger datasets to help only if data is high-quality. Larger data needs care about train–test overlap and raises ethical and privacy concerns, since web data contains toxic language, biases and private information. The authors say Chinchilla does suffer from bias and toxicity, but it seems less affected than Gopher (p. 16).
- **Generalisation.** The authors expect a similar size–data trade-off in other modalities and say their methods are easy to reproduce (p. 16).

### Appendix (pp. 22–36)
- **A. Data (p. 22).** Table A1, MassiveText sampling proportions (Chinchilla vs Rae et al. in parentheses) and epochs within 1.4T tokens: MassiveWeb 45% (48%), 1.24 epochs; Books 30% (27%), 0.75; C4 10% (10%), 0.77; News 10% (10%), 0.21; GitHub 4% (3%), 0.13; Wikipedia 1% (2%), 3.40. MassiveWeb and Wikipedia are used for more than one epoch.
- **B. Cosine cycle length (p. 22).** A cycle much longer than the target number of steps gives sub-optimally trained models (Figure A1). The main analysis assumes the cycle is calibrated to the maximum number of steps. Footnote 9: decaying 10× versus decaying to 0 differs little (10× slightly better); decaying only 5× is clearly worse.
- **C. Other datasets (pp. 22–24).** Table A2 (IsoFLOP, $a$/$b$): C4 0.50/0.50; GitHub 0.53/0.47; Kaplan et al. 0.73/0.27. The authors say this suggests the results are independent of the dataset, as long as training stays within one epoch.
- **D.1 Approach 1 details (p. 24).** Max LR $2\times10^{-4}$ (smallest) to $1.25\times10^{-4}$ (largest), 10× cosine decay. An overshoot of the cosine cycle by more than 25% noticeably degrades performance. Gaussian smoothing, window 10 steps.
- **D.2 Approach 3: loss decomposition (pp. 24–25).**
  - Setup: predict next token $y\in\mathcal Y$ from past $x\in\mathcal Y^s$. The expected risk (as printed) and the Bayes predictor are
$$L(f)\triangleq \mathbb E[\log f(x)_y],\qquad f^\star\triangleq\operatorname*{argmin}_{f\in\mathcal F(\mathcal X,\mathcal D(\mathcal Y))}L(f) \tag{6}$$
  - The best transformer of size $N$: $f_N\triangleq\operatorname*{argmin}_{f\in\mathcal H_N}L(f)$ (7).
  - The empirical risk is $\hat L_D(f)\triangleq\hat{\mathbb E}_D[\log f(x)_y]$, with $\hat f_{N,D}\triangleq\operatorname*{argmin}_{f\in\mathcal H_N}\hat L_D(f)$ (8). The authors say they are never able to obtain this minimizer, since they typically perform a single epoch. Instead one gets $\bar f_{N,D}$, the result of gradient steps on $D$ datapoints.
  - Decomposition:
$$L(N,D)\triangleq L(\bar f_{N,D})=L(f^\star)+\big(L(f_N)-L(f^\star)\big)+\big(L(\bar f_{N,D})-L(f_N)\big) \tag{9}$$
  - The three terms are the Bayes risk ("entropy of natural text"), a functional approximation term (depends on the size of the hypothesis space), and a stochastic approximation term (minimizing $\hat L_D$ rather than $L$, with a single epoch).
  - Expected forms: for two-layer neural networks, the second term is expected to be proportional to $1/N^{1/2}$ (Siegel and Xu). The third corresponds to early stopping of stochastic first-order methods, so it should scale like their convergence rate, lower-bounded by $1/D^{1/2}$ (Robbins–Monro) and possibly attaining it. This rate is expected to be dimension-free.
  - Fitted values:
$$L(N,D)=E+\frac{A}{N^{0.34}}+\frac{B}{D^{0.28}},\quad E=1.69,\ A=406.4,\ B=410.7 \tag{10}$$
  - Both coefficients are below $\tfrac12$. The authors say this is expected for the data coefficient, though far from the known lower bound. They say future models and training approaches should try to increase these coefficients.
  - Fitting objective, with $\mathrm{LSE}$ the log-sum-exp operator and $A,B,E=\exp(a),\exp(b),\exp(e)$:
$$\min_{a,b,e,\alpha,\beta}\sum_{\text{Run }i}\mathrm{Huber}_\delta\Big(\mathrm{LSE}\big(a-\alpha\log N_i,\ b-\beta\log D_i,\ e\big)-\log L_i\Big) \tag{11}$$
  - *(Added step)* The LSE equals $\log\big(AN_i^{-\alpha}+BD_i^{-\beta}+E\big)=\log\hat L(N_i,D_i)$, so (11) is Eq. (3).
  - L-BFGS started from a grid: $\alpha,\beta\in\{0,0.5,\dots,2\}$, $e\in\{-1,-0.5,\dots,1\}$, $a,b\in\{0,5,\dots,25\}$. The best initialisation is not on the grid boundary. Larger $\delta$ overfits the small-compute regime and predicts held-out larger runs poorly. $\delta$ below $10^{-3}$ makes no difference.
- **D.3 Other approaches' frontiers (p. 26).** Table A3 (Approach 2 / 3 tokens): 1B: 20.0B / 27.1B; 67B: 1.7T / 4.1T; 280B: 7.1T / 20.1T; 1T: 26.5T / 94.1T. Approach 3 requires more tokens per model size.
- **D.4 Kaplan comparison at $10^{21}$ FLOPs (pp. 26–27).** Batch 0.5M tokens, max LR $1.5\times10^{-4}$ with 10× decay. Kaplan et al. imply a 4.68B model; Approach 1 implies 2.86B. They trained 4.74B and 2.80B models with the same depth-to-width ratio. The Approach 1 model ends with lower loss (Figure A4).
- **E. Curvature (p. 27).** The FLOP–minimal-loss frontier is curved. Linear fits on the first, middle and final thirds of frontier points differ (Figure A5). The authors do not account for this. They say it suggests even smaller models may be optimal at large budgets.
- **F. FLOPs computation (pp. 27–28).** All training FLOPs are counted, including embeddings, which are also in parameter counts. A multiply-accumulate counts as 2. Forward-pass terms: embeddings $2\cdot s\cdot V\cdot d_{model}$; attention per layer: QKV projections $2\cdot3\cdot s\cdot d_{model}\cdot(k\cdot h)$, key–query logits $2s^2(k h)$, softmax $3hs^2$, softmax-weighted values $2s^2(k h)$, final linear $2s(k h)d_{model}$; dense block per layer $2s(d_{model}f+d_{model}f)$ with $f$ = ffw_size; final logits $2s\,d_{model}V$. Here $s$ is seq_len, $V$ vocab_size, $k$ key_size, $h$ num_heads. Total forward = embeddings + layers × (attention + dense) + logits. Backward is assumed to be 2× forward. Compared with $C=6DN$, the ratio is 0.99–1.10 for the models in Table A4. The authors say the differences are very small and do not affect the analysis. Their Gopher budget is $6.3\times10^{23}$ with this count versus $5.76\times10^{23}$ in Rae et al.
- **G. Other Chinchilla–Gopher differences (p. 29).** Independent of learning-rate schedule, AdamW-trained models outperform Adam-trained ones (Figures A6, A7). The Chinchilla setup (AdamW and high-precision weights) clearly outperforms the Gopher setup on a 680M model.
- **H. Results (pp. 29–31, 35).** Table A5 gives bits-per-byte on The Pile; Jurassic-1 is better on dm_mathematics (1.037 vs 1.111) and ubuntu_irc (0.857 vs 1.026). Tables A6 and A7 give per-task MMLU and BIG-bench scores. Winogender setup: a sentence with a pronoun, then the probability of completing "'{Pronoun}' refers to the" with each candidate occupation, tested with female, male and neutral pronouns.
- **I. Model card (pp. 31–34).** Primary use is research for DeepMind researchers; the model will not be made public. Tokenizer vocabulary is 32,000. The model is trained on English. The card says it can output toxic language (especially when prompted with toxic text) and that it reproduces occupation–gender stereotypes. The authors considered filtering toxic content but decided against it because filtering can introduce new biases (Welbl et al.). Intersectional biases were not investigated.
- **J. All models (p. 36).** Table A9 lists the hyperparameters of all trained models, from 44M to 16,183M parameters; many were trained with multiple schedules or token counts.

## Toy example (ours, not from the paper)
Use Eq. (2) with $E=0$, $\alpha=\beta=0.5$, $A=B=1$, and $C=6ND$.
- **Formula.** $G=(\alpha A/\beta B)^{1/(\alpha+\beta)}=1^{1}=1$, $a=b=0.5$. For $C=600$: $N_{opt}=G(C/6)^{0.5}=100^{0.5}=10$ and $D_{opt}=100^{0.5}=10$. Check: $6\cdot10\cdot10=600$ ✓.
- **Loss at the optimum.** $\hat L=10^{-0.5}+10^{-0.5}=0.3162+0.3162=0.6325$.
- **Loss at other splits with $C=600$.**
  - $N=5$, $D=20$ ($6\cdot5\cdot20=600$): $0.4472+0.2236=0.6708$.
  - $N=20$, $D=5$: $0.2236+0.4472=0.6708$.
  - $N=2$, $D=50$: $0.7071+0.1414=0.8485$.
  - All are worse than 0.6325. So a model twice too small or too large for its budget loses.
- **Scaling.** $C=2400$ gives $C/6=400$, so $N_{opt}=D_{opt}=20$. Compute ×4 gives size ×2 and tokens ×2, i.e. 2× size for 2× data. Equal exponents mean doubling size means doubling tokens.
- **Unequal exponents.** If $\alpha=0.4$, $\beta=0.2$, then $a=0.2/0.6=1/3$, $b=2/3$. Compute ×8 gives size ×$8^{1/3}=2$ and tokens ×$8^{2/3}=4$.

## Concepts
- [[compute-optimal-training]] — choosing parameters $N$ and tokens $D$ to minimize final loss for a fixed FLOP budget (Eq. 1) (p. 2)
- [[scaling-law]] — here, a power law of the optimal $N$ and $D$ in compute $C$ (and, for the loss in $N$, $D$, a power-law-plus-constant form, Eq. 2) (pp. 3–4, 6)
- [[isoflop-profile]] (new) — final loss versus model size at fixed FLOPs. Its minimum gives the loss-optimal size (p. 5)
- [[parametric-loss-fit]] (new) — fitting $\hat L = E + A/N^\alpha + B/D^\beta$ with Huber loss, then minimizing under $C\approx6ND$ (pp. 6–7)
- [[flops-6nd-approximation]] (new) — training FLOPs $C\approx 6ND$; the exact count in Appendix F differs by 0.99–1.10× for the models in Table A4 (pp. 7, 28)
- [[huber-loss]] (new) — a loss robust to outliers, used with $\delta=10^{-3}$ in the fit (p. 6)
- [[cosine-lr-schedule]] (new) — learning rate decays along a cosine curve. Here, cycle length should match the training tokens and decay 10× (pp. 3, 22)
- [[cross-entropy-log-loss]] — the expected log-loss risk $L(f)$ (Eq. 6); its minimum (the Bayes risk) is also called the entropy of natural text (pp. 24–25)
- [[train-test-leakage]] (new) — overlap of evaluation text with training data. The authors say it may inflate language-modelling results for a model trained on more data (p. 10)
- [[zero-shot-few-shot-prompting]] — evaluation protocol used throughout, e.g. 5-shot MMLU (p. 11)
- [[perplexity]] — reported for Wikitext103, 7.16 vs 7.75 (p. 10)
- [[pretraining-fine-tuning]] — pre-training compute is traded against fine-tuning and inference costs (p. 9)

## Canonical instances
- [[chinchilla-vs-gopher]] — 70B/1.4T vs 280B/300B at equal FLOPs; the main test of the predictions (pp. 9–13)
- [[kaplan-vs-hoffmann-exponents]] — 0.73/0.27 versus about 0.5/0.5, plus the head-to-head at $10^{21}$ FLOPs (pp. 1, 8, 26–27)
- [[mmlu-benchmark]] — Chinchilla 67.6% 5-shot versus Gopher 60.0% (p. 11)
- [[winogender-bias-eval]] — uneven gains across pronoun groups (p. 14)
- [[gopher-flop-budget]] — $5.76\times10^{23}$ FLOPs, the reference budget with projected optimal sizes of 40–70B (pp. 5–7, 9)

## Bridges (candidates)
- [structural-analogy] $\hat L = E + A/N^\alpha + B/D^\beta$ (irreducible term plus function-approximation and optimisation/finite-data terms) ↔ statistics: bias/variance or approximation/estimation decomposition of risk — the paper describes its form as following a classical risk decomposition (pp. 6, 25).
- [structural-analogy] Splitting a fixed budget between model size and data ↔ economics/optimization: allocating a budget between two inputs with diminishing returns. Eq. (4) is the first-order-condition solution of such a problem.
- [metaphor] "Over-sized, under-trained" models ↔ survey methodology: a very elaborate model trained on a small sample. This is only a loose analogy.

## Questions this raises
- If the frontier is concave (Appendix E), how small is the truly optimal model at 1e25–1e26 FLOPs, and does the power-law assumption fail?
- What happens beyond one epoch, when data is scarce and repeated? The authors flag this as future work (p. 15).
- How does data quality, which the authors only speculate about, enter the $A/N^\alpha + B/D^\beta$ picture?
- Why did the three approaches' bootstrap intervals differ so much in width, and how reliable are their uncertainty estimates?

## Reading notes
- Page offset: printed = pdf for pages 1–36. The text layer garbled the math symbols (Greek letters and calligraphic letters); equations were checked against the page images.
- Abstract says MMLU 67.5% and "greater than a 7% improvement". Section 4.2.2 and Table 6 say 67.6% and +7.6%. The abstract also contains "4× more more data" (typo). The abstract says 5 to 500B tokens, while the text says 5B to over 400B.
- Number mismatches between text and tables:
  - Text p. 8: 175B model → 4.41e24 FLOPs and 4.2T tokens. Table 3 (Approach 1) gives 3.85e24 and 3.7T.
  - Text p. 8: 280B model → about 1e25 FLOPs and 6.8T tokens. Table 3 gives 9.90e24 and 5.9T.
  - Text p. 8: "over 250×" Gopher compute for a 1T model at about 1e26. Table 3 gives 221.3 Gopher units for 1T.
  - Section 4.2.6: Gopher on Natural Questions is "21% and 28%" for 5/64-shot, but Table 9 gives 24.5% and 28.2%.
  - Table A3 (p. 26), Approach 3, 175B row: FLOPs 1.26e+24 is lower than the 67B row (1.71e24). Using $6ND$ with the listed 12.0T tokens gives 1.26e25, so this looks like a misprint (my arithmetic).
  - Section 4.2.5 says Chinchilla outperforms Gopher on all common sense tasks, while Table 8 shows PIQA tied at 81.8 (the Table 8 caption says "matches or outperforms").
- Equation-related issues:
  - Page 7 says the frontier "balance[s] the two terms in Equation (3)". The two terms appear in Eq. (2).
  - Table 2 gives $a=0.46$ for Approach 3, but its listed interval (0.454, 0.455) does not contain 0.46. Using the fitted $\alpha=0.34$, $\beta=0.28$ from Eq. (10), $\beta/(\alpha+\beta)=0.28/0.62\approx0.45$ (my arithmetic).
  - Eq. (6) is printed without a minus sign, $\mathbb E[\log f(x)_y]$, yet is described as cross-entropy; a minus sign would be needed for it to be cross-entropy minimization.
  - In D.2 the sentence about the dimension-free convergence rate says "the second term only depends on $D$"; it presumably means the third.
- Table 3 labels the 67B row as Gopher's budget (5.76e23), while the trained Chinchilla has 70B parameters and 1.4T tokens.
- Model sizes are inconsistent in places: Jurassic-1 is 178B in the text (pp. 2, 3, 10) but 170B in Table A5 (p. 30), and p. 15 calls GPT-3 '170 billion' parameters while elsewhere it is 175B.
- Reference list (pp. 16–21) was not digested. Table A6 and Table A7 were not summarised beyond the cited averages.
