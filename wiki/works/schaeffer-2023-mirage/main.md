---
id: schaeffer-2023-mirage/main
work: schaeffer-2023-mirage
unit: paper
pages: 1-17
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Are Emergent Abilities of Large Language Models a Mirage?

## L0 — One line
Some claimed "emergent abilities" of LLMs may come from the researcher's choice of a nonlinear or discontinuous metric (and from too little test data), not from sudden changes in the models themselves.

## L1 — The gist (≤ 120 words)
Earlier work claimed that some abilities appear sharply and unpredictably as language models get larger. The authors ask whether this is caused by how performance is scored. Their simple model assumes per-token loss falls smoothly with scale. Metrics such as exact-match accuracy or multiple-choice grade then produce sharp curves. Linear or continuous metrics on the same outputs give smooth curves. They test this on GPT-3/InstructGPT outputs, on a meta-analysis of BIG-Bench, and by inducing "emergence" in vision networks. They do not claim that LLMs cannot have emergent abilities. The work matters because emergence claims feed AI-safety worries about sudden new capabilities.

**Prerequisites:** powers and exponentials; probability of independent events (multiply); cross-entropy as −log p of the correct token; linear-log plots; the idea of a scaling law.

## L2 — Key ideas (5–10 bullets)
- Emergent abilities, as defined by prior work, have two properties: sharpness and unpredictability (p. 1–2). The authors target exactly these two.
- More than 92% of the hand-annotated BIG-Bench emergent abilities appear under only two metrics, Multiple Choice Grade and Exact String Match (p. 2, 7).
- Simple model: if per-token loss is a smooth power law in parameters, then accuracy on an L-token answer is the single-token success probability raised to the power L. This yields a sharp curve. A linear metric yields a smooth one (p. 4).
- A second cause is low resolution: with a small test set, small models seem to score exactly zero (p. 2, 4, 5).
- On GPT-3/InstructGPT outputs, switching to Token Edit Distance, or enlarging the test set, removes the apparent emergence. Both results fit the model's predictions (p. 5–6).
- In BIG-Bench, emergence is tied to particular metrics, not to task–model pairs. Replacing Multiple Choice Grade with Brier Score removes LaMDA's emergence (p. 6–7).
- The authors induce "emergent" abilities in autoencoders, Transformers and (App. B) CNNs by choosing sharp metrics (p. 8–9, 16–17).
- Limits: this does not show that LLMs cannot have emergent abilities. Several models were not queryable. Other explanations (broken power laws, "quanta") may also hold (p. 9–10).

## L3 — Walkthrough

### Abstract and 1 Introduction (p. 1–3)
- **Prior claim (Wei et al. [38], quoted):** emergent abilities are "not present in smaller-scale models but … present in large-scale models", thus they cannot be predicted by simply extrapolating the performance improvements on smaller-scale models. Later work [9] said performance on a specific task can "emerge quite unpredictably and abruptly at scale" (p. 1).
- Two defining properties: **sharpness** (instant switch from absent to present) and **unpredictability** (appearing at unforeseeable scales) (p. 1–2).
- Why it matters: such abilities raise safety worries that larger models might gain dangerous abilities without warning (p. 2).
- **The authors' target:** sharp and unpredictable changes in model outputs versus scale on specific tasks (p. 2).
- **Observation:** emergent abilities seem to appear only under metrics that nonlinearly or discontinuously scale per-token error. More than 92% of BIG-Bench emergent abilities (hand-annotated by [37]) appear under one of two metrics (p. 2):
  - Multiple Choice Grade = 1 if the highest probability mass is on the correct option, else 0.
  - Exact String Match = 1 if the output string exactly equals the target, else 0.
- **Alternative hypothesis:** emergence is a mirage caused *primarily* by a metric that deforms per-token error nonlinearly or discontinuously. *Secondarily* it is caused by too few test data to estimate small models' performance (p. 2).
- Three tests: (1) GPT-3/InstructGPT, (2) BIG-Bench meta-analysis, (3) vision models (p. 3).

### 2 Alternative explanation (p. 3–4)
- **Assumption:** within a model family, test loss falls smoothly with parameters, as in neural scaling laws (power laws in dataset size, parameters or compute). For parameters $N>0$ and constants $c>0$, $\alpha<0$ (p. 3–4):
$$\mathcal{L}_{CE}(N)=\left(\frac{N}{c}\right)^{\alpha}$$
  The authors do not require this exact form; it is illustrative (p. 4).
- Cross-entropy, with $V$ the token set, $p$ the true distribution and $\hat p_N$ the model's:
$$\mathcal{L}_{CE}(N)\overset{def}{=}-\sum_{v\in V}p(v)\log\hat p_N(v)$$
- Since $p$ is unknown, a one-hot distribution on the observed token $v^*$ is used: $\mathcal{L}_{CE}(N)=-\log\hat p_N(v^*)$ (p. 4).
- Per-token success probability (Fig. 2B), which tends to 1 as $N$ grows:
$$p(\text{single token correct})=\exp(-\mathcal{L}_{CE}(N))=\exp\!\big(-(N/c)^{\alpha}\big)$$
- **Nonlinear metric.** The task needs all $L$ tokens right, e.g. $L$-digit addition. If token correctness is independent (footnote 1: not true, but it gives results that match the emergence claims qualitatively):
$$\text{Accuracy}(N)\approx p_N(\text{single token correct})^{L}=\exp\!\big(-(N/c)^{\alpha}\big)^{L}$$
  On a linear-log plot this looks like a sharp, unpredictable emergent ability at longer $L$ (Fig. 2C) (p. 4).
- **Linear metric.** Token Edit Distance is roughly linear in the per-token error rate (App. A.2):
$$\text{Token Edit Distance}(N)\approx L\big(1-p_N(\text{single token correct})\big)=L\big(1-\exp(-(N/c)^{\alpha})\big)$$
  This gives smooth, predictable change (Fig. 2E) (p. 4).
- **Discontinuous metric.** Multiple Choice Grade (step-like) can show emergence (Fig. 2D). The continuous Brier Score removes it (Fig. 2F) (p. 3–4).
- **Conclusion of the section:** sharp, unpredictable changes can be fully explained by three factors (p. 4):
  1. a nonlinear or discontinuous metric;
  2. insufficient resolution for small models, where resolution is set by $1/\text{test set size}$;
  3. insufficient sampling of the large-parameter regime.

*Intuition note:* If a model gets each digit right with probability 0.9, it gets a 10-digit answer fully right only about 35% of the time. Because per-token success changes smoothly, the "all-correct" score sits near zero for a long stretch and then climbs quickly. The ability looks like it switches on, but the underlying quantity moved smoothly.

### 3 InstructGPT/GPT-3 arithmetic (p. 4–6)
- **Setup:** GPT family outputs on 2-shot multiplication of two 2-digit integers and 2-shot addition of two 4-digit integers. Four models were available: 350M, 1.3B, 6.7B and 175B parameters (footnote 3, p. 4–6). Prior work claimed emergence on these arithmetic tasks (p. 4).
- **Three predictions (p. 5):**
  1. A linear or continuous metric should show smooth, predictable improvement.
  2. For nonlinear metrics, a larger test set (higher resolution) should reveal smooth improvement "commensurate with the predictable nonlinear effect".
  3. Longer targets should lower performance predictably: roughly geometrically for accuracy, roughly quasilinearly for token edit distance.
- **Result 1 (Fig. 3):** under Accuracy, targets of 4–5 digits show emergence. With the *same fixed outputs* scored by Token Edit Distance, performance improves smoothly with scale. This confirms prediction 1. Longer targets lower performance roughly quasilinearly, which confirms the first half of prediction 3 (p. 6).
- **Result 2 (Fig. 4):** with more generated test data, every model in the family is above chance even under Accuracy. This confirms prediction 2. Accuracy falls roughly geometrically with target length, which confirms the second half of prediction 3 (p. 6).

*Intuition note:* The small models were not unable. Their accuracy was small but nonzero, and a small test set rounded it to zero. Re-scoring the same answers, or testing on more examples, shows steady progress.

### 4 Meta-analysis of claimed emergent abilities (p. 6–7)
- At the time of the analysis, other model families claimed to show emergent abilities were not publicly queryable and had no public outputs, so only published results could be analysed (p. 6).
- **Predictions (p. 6):**
  1. Across Task–Metric–Model-family triplets, emergence should appear mainly with specific metrics, namely nonlinear or discontinuous ones. It should not depend on the task–model pair.
  2. For a triplet showing emergence, switching to a linear or continuous metric should remove it.
- **Emergence score** (from [33]), for performance $y_i$ at scales $x_i$ sorted so that $x_i<x_{i+1}$ (p. 6):
$$\text{Emergence Score}\big(\{x_n,y_n\}_{n=1}^{N}\big)\overset{def}{=}\frac{\operatorname{sign}(\arg\max_i y_i-\arg\min_i y_i)\,(\max_i y_i-\min_i y_i)}{\sqrt{\operatorname{Median}\big(\{(y_i-y_{i-1})^2\}_i\big)}}$$
- **Result 1:** of 39 preferred BIG-Bench metrics, at most 5 show emergence (Fig. 5A). Many of those are nonlinear or discontinuous (Exact String Match, Multiple Choice Grade, ROUGE-L-Sum). Because BIG-Bench often scores one task with several metrics, the absence of emergence under the other metrics suggests that emergence does not appear when outputs are scored with them (p. 6).
- **Hand-annotated data [37]:** emergence appears under 4 of 39 metrics (Fig. 5B). Two metrics account for more than 92% of claimed abilities (Fig. 5C): Multiple Choice Grade (discontinuous) and Exact String Match (nonlinear). The pie chart counts are 51 and 11 of 67 abilities (76.12% and 16.42%), plus BLEU (2) and normalized aggregate score (3) (p. 7).
- **Result 2 (LaMDA):** on tasks where LaMDA shows emergence under Multiple Choice Grade, the continuous Brier Score removes it (Fig. 6). For a binary outcome, Brier Score reduces to the squared error between 1 and the probability mass on the outcome (p. 7).

### 5 Inducing emergent abilities in vision networks (p. 8–9)
- Aim: show that a sharp metric can create emergence where none has been seen. Abrupt transitions in vision models have not been observed, to the authors' knowledge (p. 8).
- **Autoencoders on CIFAR100:** shallow nonlinear autoencoders have smoothly falling squared reconstruction error as bottleneck units grow (Fig. 7B). The authors define a discontinuous metric with indicator $\mathbb{I}$ and cutoff $c$ (p. 8):
$$\text{Reconstruction}_c\big(\{x_n\}_{n=1}^{N}\big)\overset{def}{=}\frac1N\sum_n\mathbb{I}\big[\|x_n-\hat x_n\|^2<c\big]\tag{1}$$
  For particular $c$, this shows a sharp, seemingly unpredictable jump (Fig. 7C).
- **Omniglot with autoregressive (decoder-only) Transformers:** the setup is inspired by [6]. Subset accuracy is 1 only if all $L\in[1,5]$ images in a sequence are classified correctly. It shows a seemingly emergent ability (Fig. 8C) (p. 8).
- App. B.1 (p. 16–17): LeNet on MNIST has smoothly rising accuracy (Fig. 11B). Subset accuracy over $K$ independent test items gives a seemingly emergent jump (Fig. 11C).

*Intuition note:* The vision models improve smoothly under ordinary metrics. Changing only the scoring rule produces a curve like the published LLM ones. So a sharp curve does not by itself show a sharp change in the model.

### 6 Limitations (p. 9)
- The paper does not claim that LLMs cannot display emergent abilities. Its message is that some claimed ones appear to be mirages created by researcher analysis.
- Some models (e.g. PaLM 1, Gopher, Chinchilla) were private.
- The best metric arguably depends on human preferences. The authors know of no study of whether human judgment is thresholded in an "emergent" way.

### 7 Related work (p. 9–10)
- Srivastava et al. [33] saw that accuracy looks sharp but cross-entropy does not, and discussed whether the metric may explain part of emergence. This paper turns that discussion into testable predictions (p. 9).
- **Caballero et al. [5]:** emergence is real, caused by a "break" in a piece-wise power law. The authors suggest emergence can be induced under a single power law. Both explanations could be true (p. 9–10).
- **Michaud et al. [28]:** language data may consist of discrete "quanta". Larger networks learn more of them, so they can perform tasks needing a combination. The authors find this interesting and worth study (p. 10).

### 8 Discussion (p. 10)
- For a fixed task and model family, the researcher can choose a metric that creates or ablates an emergent ability. Hence emergent abilities "may be creations of the researcher's choices" rather than a fundamental property of the family on the task.
- Implications:
  1. Task and metric are distinct choices when building a benchmark.
  2. To forecast scaling accurately, consider cross-entropy, transformations and resolution-limited evaluation. Continuous or linear metrics are "probably better" for forecasts. Discontinuous or nonlinear ones may need much more data.
  3. Claims need proper controls. Emergence claims are possibly affected by uncontrolled multiple comparisons. BIG-Bench has at least 220 tasks, about 40 metrics per task and about 10 model families, so about $10^6$ triplets. The chance that none shows emergence by chance "might be small".
  4. Progress is hampered when models and outputs are not available for independent study.

### Appendix A: Approximate behaviour of metrics (p. 14–16)
Setup: $N$ test items of length $L$ tokens, targets $t_n=(t_{n1},\dots,t_{nL})$, predictions $\hat t_n$, constant per-token error probability $\epsilon\in[0,1]$. The authors say constant $\epsilon$ is empirically false but modelling error dependence is out of scope (p. 14).

**A.1 Resolution.** Resolution for viewing $\epsilon$ is limited by $1/NL$. Coin analogy: after $F$ flips, the probability of heads is resolved only to $1/F$. Notation (p. 14):
$$a_b\overset{def}{=}a\text{ rounded to the nearest integer multiple of }1/b\tag{2}$$

**A.2 Token Edit Distance** (p. 14–15). Adaptation of Levenshtein distance to tokens:
$$\text{TED}(t_n,\hat t_n)\overset{def}{=}\text{Num. Substitutions}+\text{Num. Additions}+\text{Num. Deletions}\tag{3}$$
$$=\sum_{\ell=1}^{L}\mathbb{I}[t_{n\ell}\ne\hat t_{n\ell}]+\text{Num. Additions}+\text{Num. Deletions}\tag{4}$$
$$\ge\sum_{\ell=1}^{L}\mathbb{I}[t_{n\ell}\ne\hat t_{n\ell}]\tag{5}$$
$$\mathbb{E}[\text{TED}]\ge\mathbb{E}\Big[\sum_{\ell}\mathbb{I}[t_{n\ell}\ne\hat t_{n\ell}]\Big]\tag{6}$$
$$=\sum_{\ell=1}^{L}p(t_{n\ell}\ne\hat t_{n\ell})\tag{7}$$
$$\approx L(1-\epsilon)\tag{8}$$
$$\mathbb{E}[\text{TED}]_{NL}\ge L\big(1-\epsilon_{NL}\big)\tag{9}$$
Conclusion: expected TED scales approximately linearly with the resolution-limited per-token probability. The true rate is slightly higher than linear because additions and deletions add non-negative cost. The authors have no model of over- or under-production of tokens (p. 14–15). (See Reading notes on Eq. 8.)

**A.3 Accuracy** (p. 15):
$$\text{Accuracy}(t_n,\hat t_n)\overset{def}{=}\mathbb{I}[\text{No additions}]\,\mathbb{I}[\text{No deletions}]\prod_{l=1}^{L}\mathbb{I}[t_{nl}=\hat t_{nl}]\tag{10}$$
$$\approx\prod_{l=1}^{L}\mathbb{I}[t_{nl}=\hat t_{nl}]\tag{11}$$
$$\mathbb{E}[\log\text{Accuracy}]=\sum_l\mathbb{E}\big[\log\mathbb{I}[t_{nl}=\hat t_{nl}]\big]\tag{12}$$
$$\le\sum_l\log\mathbb{E}\big[\mathbb{I}[t_{nl}=\hat t_{nl}]\big]\tag{13}$$
$$\approx L\log(1-\epsilon)\tag{14}$$
$$\mathbb{E}[\text{Accuracy}]\approx\exp(\mathbb{E}[\log\text{Accuracy}])\tag{15}$$
$$=(1-\epsilon)^{L}\tag{16}$$
The authors call (15) an approximation "that would make most mathematicians cry" (p. 15). Result: accuracy approximately falls geometrically with target length. Resolution-limited:
$$\mathbb{E}[\text{Accuracy}]_{NL}=\big((1-\epsilon)^{L}\big)_{NL}\tag{18}$$
Accuracy is affected significantly more than a linear metric by limited resolution, because it forces one to distinguish quantities that decay rapidly (p. 15).

**A.4 ROUGE-L-Sum** (p. 15). Based on longest common subsequence (LCS), using the "union" LCS across several references. Example from [25]: candidate $c=w_1w_2w_3w_4w_5$, $r_1=w_1w_2w_6w_7w_8$, $r_2=w_1w_3w_8w_9w_5$. Then $LCS(r_1,c)=w_1w_2$, $LCS(r_2,c)=w_1w_3w_5$, and the union LCS is $w_1w_2w_3w_5$, of length 4. Intuitively, this disproportionately benefits models with smaller error rates. Monte Carlo simulation (Fig. 9) shows the metric falls sharply as per-token error rises slightly, e.g. from 0.05 to 0.1 (p. 15–16).

**A.5 BLEU** (p. 15–16). Based on shared n-grams. It uses the geometric mean of n-gram precisions, so any zero precision makes the score 0. Example: prediction "hello there general" against an identical reference has no 4-grams, so the 4-gram precision is 0 and BLEU is 0.0. Simulations (Fig. 10) show a sharp fall as error rises slightly.

### Appendix B (p. 16–17) and C (p. 17)
- B.1: see Sec. 5 above.
- **C, Grokking** (a single model gets high training accuracy and only much later high test accuracy). Differences from emergent abilities (p. 17):
  1. grokking is primarily studied within a single model, emergence within a model family;
  2. grokking runs over gradient steps, emergence over model scale;
  3. grokking studies a train/test discrepancy, while emergence work, to the authors' knowledge, shows no separate train and test curves;
  4. grokking is primarily studied on toy algorithmic tasks in small networks, emergence often on benchmark NLP tasks in large LLMs.

## Toy example (ours, not from the paper)
Take a model family where the per-token success probability $p$ rises smoothly: 0.2, 0.4, 0.6, 0.8, 0.95 for five sizes. Let the answer have $L=10$ tokens.
- Accuracy $=p^{10}$:
  - $0.2^{10}=0.0000001024$
  - $0.4^{10}=0.0001048576$
  - $0.6^{10}\approx0.00605$
  - $0.8^{10}\approx0.1074$
  - $0.95^{10}\approx0.5987$
- Expected token errors (the edit-distance idea, $L(1-p)$): 8, 6, 4, 2, 0.5. This is a straight line in $p$.
- With a 100-item test set (resolution 0.01), the first two accuracies (about 0 and 0.0001) round to 0. The third (0.006) is under one item in expectation, so it reads 0 or 0.01. The curve then reads about 0, 0, 0 (or 0.01), 0.11, 0.60 and looks like a sudden onset.
- With $10^6$ items, the expected correct counts are about 0.1, 105 and 6,047. The small models are now visibly above zero (the 0.2 model is still near 0 correct), and the rise is smooth on a log axis.
- The model improved smoothly the whole time. Only the metric and the test-set size created the jump.

## Concepts
- [[emergent-ability]] — ability absent in small models, present in large ones; defined by sharpness and unpredictability (p. 1–2)
- [[scaling-law]] — power-law decline of test loss with parameters, data or compute; here assumed, not required in exact form (p. 3–4)
- [[cross-entropy-log-loss]] — per-token loss $-\log\hat p_N(v^*)$ with a one-hot target; assumed to fall smoothly (p. 4)
- [[nonlinear-or-discontinuous-metric]] (new) — a metric that warps per-token error nonlinearly (Accuracy, Exact String Match) or like a step (Multiple Choice Grade) (p. 2–4)
- [[resolution-limited-evaluation]] (new) — finest measurable performance difference is about $1/(\text{test size})$; small test sets round small scores to zero (p. 4, 14)
- [[token-edit-distance]] (new) — number of substitutions, additions and deletions needed to turn the output into the target; roughly linear in error (p. 14)
- [[brier-score]] (new) — continuous proper scoring rule; for binary outcomes, squared error between 1 and the probability on the outcome (p. 7)
- [[emergence-score]] (new) — a statistic from [33] that flags possible emergence; it only suggests emergence (p. 6–7)
- [[multiple-comparisons]] (new) — many triplets tested, so some emergence may appear by chance; the authors say this is possible (p. 10)
- [[grokking]] (new) — a single model reaches high training accuracy and only much later high test accuracy; the paper lists several differences from emergent abilities (p. 17)

## Canonical instances
- [[gpt3-instructgpt-arithmetic]] — 2-digit multiplication and 4-digit addition: emergence under Accuracy, smooth under Token Edit Distance (p. 5–6)
- [[big-bench-metric-meta-analysis]] — more than 92% of claimed emergent abilities under Multiple Choice Grade or Exact String Match (p. 7)
- [[lamda-brier-score]] — emergence under Multiple Choice Grade disappears under Brier Score (p. 7–8)
- [[induced-emergence-vision]] — autoencoder reconstruction, Omniglot Transformers, MNIST LeNet (p. 8–9, 16–17)

## Bridges (candidates)
- [same-math] Accuracy $=p^L$ for independent tokens ↔ probability: probability of independent events all occurring is a product, giving geometric decay in $L$.
- [structural-analogy] Resolution $1/NL$ and zero-rounding ↔ statistics: a small sample cannot detect a small rate (coin-flip example, p. 14).
- [structural-analogy] Thresholded metric creates a jump ↔ measurement theory: applying a step function to a continuous latent variable gives an apparent discontinuity.
- [metaphor] Emergence as a mirage ↔ Anderson's "More Is Different" (p. 1): the paper questions the claim of emergence for LLMs.

## Questions this raises
- If per-token loss is smooth, which metric best matches what users care about (e.g. an exactly correct answer)? The authors note human judgment may itself be thresholded (p. 9).
- How much of the claimed emergence remains after multiple-comparison controls and larger test sets, in model families that were not queryable?
- How much does the independence and constant-error assumption (p. 4, 14) matter for real, correlated token errors?
- Could real changes (broken power laws [5], quanta [28]) coexist with metric artifacts in the same data?

## Reading notes
- Printed page = pdf page (offset 0). The text layer of Figs. 2, 3 and 5 is garbled, so figure content was taken from the images.
- **Eq. 8 (p. 14) as printed:** $p(t\ne\hat t)\approx L(1-\epsilon)$ with $\epsilon$ defined as the per-token *error* probability. The mismatch probability would be $\epsilon$, giving $L\epsilon$. The main-text formula $L(1-p(\text{correct}))$ (p. 4) is consistent with $L\epsilon$. This looks like a notation slip. The same issue carries into Eq. 9. The qualitative conclusion (linear in per-token rate) is unaffected.
- In A.3 the label (17) is printed with no equation next to it, and (18) follows.
- Fig. 10 caption (p. 16) says "ROUGE-L-Sum metric falls sharply" although the figure is about BLEU.
- Appendix B.1 text (p. 16) says $K$ increases from 1 to 5, but the Fig. 11C legend (p. 17) shows $K$ = 6, 8, 10.
- Fig. 11A (p. 17) is cited as "Grounded Mappings" [38], while Fig. 1F also uses Grounded mappings.
- Figure 5A's exact "at most 5" metric list is not named beyond the three examples in the text.
