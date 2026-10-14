---
id: brown-2020-gpt3/main-p1
work: brown-2020-gpt3
unit: paper (part 1/3) — Abstract, §1 Introduction, §2 Approach, §3 Results through the start of §3.9.5
pages: 1–28
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
# Language Models are Few-Shot Learners — Part 1: Motivation, Method, Benchmark Results

## L0 — One line
Scaling an autoregressive language model to 175B parameters makes it much better at learning a task from instructions or a few examples in its prompt, with no weight updates, though results vary strongly by task.

## L1 — The gist (≤ 120 words)
The paper asks whether a very large language model can perform new tasks from an instruction or a few examples placed in its prompt, with no gradient updates. It trains eight models, up to GPT-3 (175B parameters). It tests them zero-, one- and few-shot on dozens of benchmarks and new synthetic tasks. Few-shot performance tends to rise with model size and is sometimes competitive with fine-tuned state of the art. It is weak on some tasks, such as NLI and WiC. Humans barely beat chance at spotting its generated news articles. This matters because it turns task specification into text conditioning. This part covers the abstract, introduction, approach and results up to the start of §3.9.5.

**Prerequisites:** language modeling as next-token prediction; the idea of fine-tuning versus pre-training; perplexity and cross-entropy loss; accuracy, F1 and BLEU as benchmark scores; a two-sample t-test (for §3.9.4).

## L2 — Key ideas (5–10 bullets)
- **Problem.** Pre-train-then-fine-tune needs thousands of labeled examples per task. It may also exploit spurious correlations and overstate real performance. Humans learn from an instruction or a few demonstrations (pp. 3–4).
- **Idea.** "In-context learning": the model is conditioned on an instruction and/or K demonstrations and predicts the completion. It is evaluated zero-shot, one-shot and few-shot, with no gradient updates (pp. 4–7).
- **Scale hypothesis.** Prior work suggests log loss improves smoothly with scale, so the authors say it is plausible that in-context abilities also gain strongly with scale. The authors train eight sizes (125M–175B) to test this (pp. 4, 8).
- **Recipe.** GPT-2 architecture with alternating dense and sparse attention, n_ctx = 2048, 300B training tokens, and a filtered, quality-weighted data mix. A filtering bug left some benchmark overlap in the training data, and retraining was too costly (pp. 8–9).
- **Loss scaling.** Validation loss keeps following a power law in compute over two more orders of magnitude (p. 11).
- **Results.** Many benchmarks improve with K and with model size. GPT-3 sets or matches the state of the art on LAMBADA and TriviaQA (few-shot) and on PTB (zero-shot only). It is weak on ANLI, WiC, RACE and QuAC (pp. 5, 12–21).
- **Synthetic tasks.** Arithmetic accuracy jumps between 13B and 175B; word-manipulation accuracy mostly grows smoothly, with a steep rise on random insertion. A memorization spot-check finds few matches (pp. 22–24).
- **Human detection.** Humans scored ~52% on 175B-generated news, against ~86% on a deliberately bad control model, with 50% as chance (pp. 25–27).

## L3 — Walkthrough

### Abstract (p. 1)
- Authors' claim: pre-training followed by fine-tuning still needs task-specific datasets of thousands or tens of thousands of examples. Humans can usually do a new language task from a few examples or simple instructions (p. 1).
- GPT-3 is an autoregressive LM with 175B parameters, 10x more than any previous non-sparse language model. It is tested few-shot with no gradient updates or fine-tuning. Tasks and demonstrations are given purely as text (p. 1).
- It does well on translation, QA, cloze, unscrambling words, using a novel word and 3-digit arithmetic. It struggles on some datasets and faces methodological issues from training on large web corpora (p. 1).
- Human evaluators have difficulty distinguishing its news articles from human-written ones (p. 1).

### 1 Introduction (pp. 3–6)
**Background (p. 3).** The authors describe a trend in how pre-trained representations are used:
- single-layer word vectors fed to task-specific architectures;
- multi-layer RNN representations, still with task-specific architectures;
- pre-trained recurrent or transformer LMs fine-tuned directly, removing task-specific architectures (p. 3).

The remaining limitation is that strong performance still typically needs fine-tuning on thousands to hundreds of thousands of task-specific examples (p. 3).

**Three reasons to remove the limitation (pp. 3–4).**
1. *Practical.* Collecting a large labeled set for every new task limits applicability. Tasks range from grammar correction to critiquing a story (p. 3).
2. *Spurious correlations.* The potential to exploit them grows with model expressiveness and the narrowness of the training distribution. Large models fine-tuned on narrow distributions may generalize poorly out-of-distribution. Benchmark performance, even if nominally human-level, may therefore exaggerate real task performance (p. 3).
3. *Human analogy.* Humans learn most language tasks from a brief directive or a tiny number of demonstrations. This also lets them switch between tasks, e.g. doing addition mid-dialogue (pp. 3–4).

**Meta-learning and in-context learning (p. 4).**
- Meta-learning, for LMs, means developing a broad set of skills at training time, then using them at inference time to adapt to or recognize the task (Fig. 1.1).
- "In-context learning" is the inner loop. It occurs within the forward pass on each sequence. The outer loop is learning by SGD during unsupervised pre-training (p. 3, Fig. 1.1; p. 4, fn. 1).
- Footnote 1: "zero-shot transfer" is ambiguous, because demonstrations are often supplied at inference time. The authors therefore say zero-, one- or few-shot by number of demonstrations. These terms stay agnostic on whether the model learns tasks from scratch at inference time or only recognizes patterns seen in training (p. 4).
- The prior in-context approach [RWC+19] gave far inferior results. It scored 4% on Natural Questions, and its 55 F1 on CoQA was more than 35 points behind the state of the art (p. 4).

**Scale motivation (p. 4).** Transformer LM sizes grew from 100M to 17B parameters, and each increase brought improvements. There is evidence that log loss, which correlates well with many downstream tasks, improves smoothly with scale. Since in-context learning absorbs many skills within the parameters, the authors say it is plausible that it also gains strongly with scale (p. 4).

**What the paper does (pp. 5–6).**
- Evaluate GPT-3 on over two dozen NLP datasets and several novel tasks, in three conditions:
  - few-shot: as many demonstrations as fit in the context window, typically 10–100;
  - one-shot: one demonstration;
  - zero-shot: only a natural-language instruction (p. 5).
- Fine-tuning GPT-3 is left to future work (p. 5).
- Fig. 1.2 (symbol-removal task): performance rises with a task description, with the number of in-context examples K, and dramatically with model size. These curves involve no gradient updates (pp. 4–5).
- Headline numbers (p. 5):
  - CoQA F1: 81.5 / 84.0 / 85.0 (zero / one / few).
  - TriviaQA accuracy: 64.3 / 68.0 / 71.2. The few-shot figure is state of the art relative to fine-tuned models in the same closed-book setting.
- Struggles: ANLI, and reading comprehension sets RACE and QuAC (p. 5).
- Fig. 1.3 aggregates 42 accuracy benchmarks. Zero-shot improves steadily with size and few-shot more rapidly. The authors say it should not be seen as a rigorous benchmark (p. 5).
- *Data contamination* (benchmark test content present in training data) is studied systematically. It has a minimal effect on most datasets. A few datasets could be inflated, and these are omitted or marked with an asterisk (p. 6).
- Smaller models (125M–13B) show relatively smooth scaling. The gap between zero-, one- and few-shot often grows with capacity, "perhaps suggesting" larger models are more proficient meta-learners (p. 6).
- Outline of the rest of the paper (§§2–8) (p. 6).

*Intuition note.* The paper's picture (Fig. 1.1) is that a model trained only to predict text can meet repeated small sub-tasks inside its training sequences. A prompt with an instruction or examples can then act like a task specification. The authors say it is plausible that a bigger model gets better at this.

### 2 Approach (pp. 6–10)
The pre-training approach is similar to GPT-2 [RWC+19], scaled up in model size, data size and diversity, and training length. The in-context use is also similar, but explored systematically (p. 6).

**Four settings on a spectrum of task-specific data (pp. 6–7, Fig. 2.1).**
- **Fine-tuning (FT).** Updates weights on a supervised task dataset, typically thousands to hundreds of thousands of labeled examples.
  - Advantage: strong benchmark performance.
  - Disadvantages: a new large dataset per task, potentially poor out-of-distribution generalization, and potential exploitation of spurious features, which may make comparison with humans unfair.
  - GPT-3 is not fine-tuned here, because the focus is task-agnostic performance (p. 6).
- **Few-shot (FS).** K examples of context and completion are given at inference time as conditioning, then one final context. No weight updates.
  - K is typically 10–100, since that fits in $n_{\text{ctx}} = 2048$.
  - Advantages: much less task-specific data, and less risk of learning an overly narrow distribution.
  - Disadvantage: results so far much worse than state-of-the-art fine-tuned models; some task data is still needed (p. 6).
- **One-shot (1S).** Like few-shot but with one demonstration plus a natural-language description. It most closely matches how some tasks are communicated to humans, e.g. on Mechanical Turk (p. 6).
- **Zero-shot (0S).** Only a natural-language instruction.
  - Advantages: maximum convenience, potential robustness, and avoidance of spurious correlations (unless they are very broad in the pre-training data).
  - It is the most challenging setting, and in some cases "unfairly hard", e.g. a request to make a table of 200m-dash world records is ambiguous (pp. 6–7).

The authors present the three as different problem settings, trading benchmark performance against sample efficiency, not as competing alternatives. They say one-shot, or sometimes zero-shot, seem the fairest comparisons to human performance (p. 7).

#### 2.1 Model and Architectures (p. 8)
- Same model and architecture as GPT-2 (modified initialization, pre-normalization, reversible tokenization). The exception is alternating dense and locally banded sparse attention patterns in the layers, similar to the Sparse Transformer (p. 8).
- Eight sizes, from 125M to 175B, spanning three orders of magnitude. Previous work [KMH+20] suggests validation loss should be approximately a smooth power law in size. Training many sizes tests this for loss and for downstream tasks (p. 8).
- Definitions: $n_{\text{params}}$ is the trainable parameter count and $n_{\text{layers}}$ the number of layers. $d_{\text{model}}$ is the units per bottleneck layer, with feed-forward width $d_{\text{ff}} = 4\,d_{\text{model}}$. $d_{\text{head}}$ is the dimension of each attention head. All models use $n_{\text{ctx}} = 2048$ (p. 8).
- The models are partitioned across GPUs along depth and width. Architecture parameters were chosen for computational efficiency and load balancing. Validation loss is reported not to be strongly sensitive to them within a broad range (p. 8).

**Table 2.1 (p. 8).** Batch size is in tokens. All models were trained for 300B tokens.

| Model | $n_{\text{params}}$ | $n_{\text{layers}}$ | $d_{\text{model}}$ | $n_{\text{heads}}$ | $d_{\text{head}}$ | Batch | LR |
|---|---|---|---|---|---|---|---|
| Small | 125M | 12 | 768 | 12 | 64 | 0.5M | 6.0e−4 |
| Medium | 350M | 24 | 1024 | 16 | 64 | 0.5M | 3.0e−4 |
| Large | 760M | 24 | 1536 | 16 | 96 | 0.5M | 2.5e−4 |
| XL | 1.3B | 24 | 2048 | 24 | 128 | 1M | 2.0e−4 |
| 2.7B | 2.7B | 32 | 2560 | 32 | 80 | 1M | 1.6e−4 |
| 6.7B | 6.7B | 32 | 4096 | 32 | 128 | 2M | 1.2e−4 |
| 13B | 13.0B | 40 | 5140 | 40 | 128 | 2M | 1.0e−4 |
| 175B ("GPT-3") | 175.0B | 96 | 12288 | 96 | 128 | 3.2M | 0.6e−4 |

#### 2.2 Training Dataset (pp. 8–9)
- The Common Crawl dataset constitutes nearly a trillion words, enough to train the largest models without updating on the same sequence twice. Unfiltered or lightly filtered versions tend to be lower quality than curated data (p. 8).
- Three quality steps:
  1. Filter Common Crawl by similarity to high-quality reference corpora.
  2. Fuzzy document-level deduplication within and across datasets. This also keeps the held-out validation set a valid measure of overfitting.
  3. Add curated corpora: an expanded WebText, Books1, Books2 and English Wikipedia (p. 8).
- Common Crawl: 41 monthly shards, 2016–2019, 45TB compressed before filtering and 570GB after, roughly 400B byte-pair-encoded tokens (p. 8).
- Datasets are not sampled in proportion to size. Higher-quality ones are sampled more often. This accepts a small amount of overfitting for higher-quality data (p. 8).

**Table 2.2 (p. 9).**

| Dataset | Tokens | Weight in mix | Epochs in 300B tokens |
|---|---|---|---|
| Common Crawl (filtered) | 410B | 60% | 0.44 |
| WebText2 | 19B | 22% | 2.9 |
| Books1 | 12B | 8% | 1.9 |
| Books2 | 55B | 8% | 0.43 |
| Wikipedia | 3B | 3% | 3.4 |

- **Compute (Fig. 2.2).** Following [KMH+20], the authors train much larger models on many fewer tokens than is typical. GPT-3 3B is almost 10x larger than RoBERTa-Large (355M), yet both took roughly 50 petaflop/s-days in pre-training (p. 9).
- **Contamination bug.** The authors tried to remove overlaps with the dev and test sets of all benchmarks. A bug in the filtering let some overlaps through, and retraining was infeasible. §4 characterizes the impact (p. 9).

#### 2.3 Training Process (p. 9)
- Larger models can typically use a larger batch size but need a smaller learning rate. The gradient noise scale was measured to guide batch size (p. 9).
- Training uses model parallelism within each matrix multiply and across layers, on V100 GPUs on a Microsoft cluster. Details are in Appendix B (p. 9).

#### 2.4 Evaluation (p. 10)
- **Few-shot conditioning.** K examples are drawn at random from the task's training set for each evaluation example, separated by 1 or 2 newlines.
  - LAMBADA and StoryCloze have no training set, so conditioning examples come from the dev set.
  - Original Winograd has one dataset, so examples come from it directly (p. 10).
- K ranges from 0 to what fits in $n_{\text{ctx}} = 2048$ (typically 10–100). Larger K is usually but not always better. When a dev set exists, a few values of K are tried on dev and the best is run on test. A natural-language prompt is sometimes added (p. 10).
- **Multiple choice.** Show K examples of context plus correct completion, then a context only, and compare LM likelihood of each completion. Usually the per-token likelihood is compared, to normalize for length. For ARC, OpenBookQA and RACE, normalizing by the unconditional probability helped on dev:

$$\frac{P(\text{completion}\mid\text{context})}{P(\text{completion}\mid\text{answer context})},$$

where the answer context is the string "Answer: " or "A: " (p. 10).
- **Binary classification.** Options get meaningful names ("True"/"False") and the task is treated as multiple choice (p. 10).
- **Free-form completion.** Beam search, beam width 4, length penalty α = 0.6, as in [RSR+19]. Scoring uses F1, BLEU or exact match, whichever is standard (p. 10).
- **Reporting.** Test-set results where public. Where the test set is private and the model is too large for the test server, dev-set results are reported. Test-server submissions were made only for SuperGLUE, TriviaQA and PiQa; the text says only 200B few-shot results were submitted, as printed (see Reading notes) (p. 10).

*Intuition note.* In every setting the weights stay fixed. The only thing that changes between zero-, one- and few-shot is the text in the prompt. Multiple-choice tasks are answered by asking which candidate answer the model finds most probable after the prompt.

### 3 Results (pp. 10–28)
**Scaling of loss (p. 10–11, Fig. 3.1).**
- Training curves are shown for the 8 models plus 6 extra-small models (as few as 100,000 parameters) (p. 10).
- Language-modeling performance follows a power law when compute is used efficiently [KMH+20]. After extending the trend by two more orders of magnitude, there is only a slight (if any) departure. Fig. 3.1's fitted line is $L = 2.57\cdot C^{-0.048}$ (C in PetaFLOP/s-days; embedding parameters excluded) (pp. 10–11).
- The authors say one might worry that cross-entropy improvements come from modeling spurious details of the corpus. They say later sections show they lead to consistent gains across a broad range of tasks (p. 10).
- The 9 task groups are §§3.1–3.9 (p. 10).

*Intuition note.* Doubling compute lowers validation loss by a small, predictable factor. The curve looked straight on a log–log plot over many orders of magnitude. The open question for the rest of §3 is whether lower loss translates into better task performance.

#### 3.1 Language Modeling, Cloze, and Completion (pp. 11–13)
**3.1.1 PTB (p. 11).**
- Zero-shot perplexity is 20.5 for GPT-3 versus 35.8 for the previous zero-shot SOTA (Table 3.1). The authors report a new SOTA margin of 15 points.
- The four Wikipedia-related tasks and the One Billion Word benchmark were omitted because they are largely in the training data. PTB avoids these issues because it predates the modern internet.
- Only zero-shot is measured, since PTB has no clear example separation (p. 11).

**3.1.2 LAMBADA (pp. 11–13).**
- Task: predict the last word of a sentence that needs a paragraph of context.
- Others' view: [BHT+20] note a 1.5% gain from doubling model size between two SOTAs and argue "continuing to expand hardware and data sizes by orders of magnitude is not the path forward". Authors' reply: they find that path "still promising". Zero-shot GPT-3 reaches 76%, +8% over the previous SOTA (pp. 11–12).
- Problem: a standard LM has no way of knowing that the completion is always the last word of a sentence. It puts probability on other valid continuations, which stop-word filters only partly addressed. The few-shot setting lets the authors frame the task as a cloze test, so the model can infer a one-word completion is wanted. The format is "Alice was friends with Bob. Alice went to visit her friend ____. → Bob" (p. 12).
- Few-shot gives 86.4% (K = 15 in Fig. 3.2), over 18% above the previous SOTA. The format lowers the smallest model's performance by almost 20% but raises GPT-3's by 10%. It is not effective one-shot, where it always performs worse than zero-shot. The authors suggest, as a "perhaps", that all models need several examples to recognize the pattern (p. 12).
- Zero-shot uses a different format from one- and few-shot (Fig. 3.2 caption) (p. 12).
- Caution: a significant minority of LAMBADA appears in the training data. The §4 analysis suggests negligible impact (p. 13).

**Table 3.2 (p. 12).**

| Setting | LAMBADA acc | LAMBADA ppl | StoryCloze acc | HellaSwag acc |
|---|---|---|---|---|
| SOTA | 68.0 | 8.63 | 91.8 | 85.6 |
| GPT-3 zero-shot | 76.2 | 3.00 | 83.2 | 78.9 |
| GPT-3 one-shot | 72.5 | 3.35 | 84.7 | 78.1 |
| GPT-3 few-shot | 86.4 | 1.92 | 87.7 | 79.3 |

**3.1.3 HellaSwag (p. 13).** Pick the best story ending. Examples were adversarially mined against LMs and are easy for humans (95.6%). GPT-3 gets 78.1% one-shot and 79.3% few-shot. This beats a fine-tuned 1.5B LM (75.4%) but is a fair amount lower than the fine-tuned multi-task SOTA, ALUM (85.6%) (p. 13).

**3.1.4 StoryCloze (p. 13).** Choose the ending of a five-sentence story. GPT-3 gets 83.2% zero-shot and 87.7% few-shot (K = 70). That is 4.1% below the fine-tuned BERT-based SOTA but about 10% above previous zero-shot results (p. 13).

#### 3.2 Closed Book Question Answering (pp. 13–14)
- Open-book QA retrieves relevant text and conditions on it. Closed-book answers directly from the model [RRS20]. GPT-3 is tested on Natural Questions, WebQuestions and TriviaQA with the same splits. The authors say this is stricter than prior closed-book work, because fine-tuning on the QA dataset is also not permitted (p. 13).

**Table 3.3 (p. 13).**

| Setting | NQ | WebQS | TriviaQA |
|---|---|---|---|
| RAG (fine-tuned, open-domain) | 44.5 | 45.5 | 68.0 |
| T5-11B+SSM (fine-tuned, closed-book) | 36.6 | 44.7 | 60.5 |
| T5-11B (fine-tuned, closed-book) | 34.5 | 37.4 | 50.1 |
| GPT-3 zero-shot | 14.6 | 14.4 | 64.3 |
| GPT-3 one-shot | 23.0 | 25.3 | 68.0 |
| GPT-3 few-shot | 29.9 | 41.5 | 71.2 |

- **TriviaQA.** Zero-shot beats fine-tuned T5-11B by 14.2% and T5-11B+SSM by 3.8%. One-shot (68.0) matches the open-domain SOTA (RAG), which fine-tunes and uses a retrieval index of 21M documents. Few-shot adds another 3.2% (p. 13).
- **WebQS.** Zero-/one-shot are poor and the zero-to-few gain is much larger than on TriviaQA. The authors suggest, as a "perhaps", that the questions and/or answer style are out-of-distribution for GPT-3. It appears able to adapt in the few-shot setting (pp. 13–14).
- **NQ.** The large zero-to-few gain may again suggest distribution shift. The authors note NQ questions tend toward very fine-grained Wikipedia knowledge, which could be testing the limits of GPT-3's capacity (p. 14).
- Overall, on one of three datasets one-shot matches the open-domain fine-tuning SOTA. On the other two it approaches the closed-book SOTA without fine-tuning. Performance scales very smoothly with model size, "possibly reflecting" that capacity translates to knowledge absorbed in the parameters (p. 14, Fig. 3.3).

*Intuition note.* The large few-shot gains on WebQS and NQ might mean that the examples mainly help the model adapt to the question and answer style. The authors only suggest this ("perhaps", "may"); they do not show it.

#### 3.3 Translation (pp. 14–16)
- GPT-3's training data is 93% English by word count and 7% other languages, from raw Common Crawl with only quality filtering. German and Romanian are added to the analysis (p. 14).
- Prior unsupervised NMT usually pretrains on monolingual data and uses back-translation. GPT-3 has a single, task-agnostic objective and a naturally mixed multilingual blend. The authors say its one-/few-shot settings are not strictly comparable to unsupervised work, because they use 1 or 64 paired examples (up to a page or two of context) (p. 14).

**Table 3.4 (BLEU) (p. 15).**

| Setting | En→Fr | Fr→En | En→De | De→En | En→Ro | Ro→En |
|---|---|---|---|---|---|---|
| SOTA (supervised) | 45.6 | 35.0 | 41.2 | 40.2 | 38.5 | 39.9 |
| XLM | 33.4 | 33.3 | 26.4 | 34.3 | 33.3 | 31.8 |
| MASS | 37.5 | 34.9 | 28.3 | 35.2 | 35.2 | 33.1 |
| mBART | – | – | 29.8 | 34.0 | 35.0 | 30.5 |
| GPT-3 zero-shot | 25.2 | 21.2 | 24.6 | 27.2 | 14.1 | 19.9 |
| GPT-3 one-shot | 28.3 | 33.7 | 26.2 | 30.4 | 20.6 | 38.6 |
| GPT-3 few-shot | 32.6 | 39.2 | 29.7 | 40.6 | 21.0 | 39.5 |

- Zero-shot underperforms recent unsupervised NMT. A single demonstration adds over 7 BLEU. Full few-shot adds about 4 more, giving average performance similar to prior unsupervised NMT (pp. 15–16).
- **Direction skew.** Translating into English, GPT-3 significantly outperforms prior unsupervised NMT. Translating from English, it underperforms. The caption says few-shot is 5 BLEU better into English, which it attributes to its strength as an English LM (pp. 15–16).
- En→Ro is a notable outlier, over 10 BLEU worse than prior unsupervised work. The authors say this "could be" a weakness of reusing GPT-2's byte-level BPE tokenizer, built for almost entirely English data (p. 16).
- Few-shot GPT-3 beats the best supervised result they found for Fr→En and De→En. Because of their unfamiliarity with the literature, and because those look like uncompetitive benchmarks, they do not suspect these are true SOTA. For Ro→En it is within 0.5 BLEU of the overall SOTA, which uses unsupervised pretraining, supervised fine-tuning on 608K examples and back-translation (p. 16).
- Improvement with capacity is smooth for all pairs and all three settings (Fig. 3.4) (p. 16).

#### 3.4 Winograd-Style Tasks (pp. 16–17)
- The task is to resolve a pronoun that is grammatically ambiguous but semantically clear to humans. Fine-tuned models are near-human on original Winograd, but the adversarial Winogrande still lags humans (pp. 16–17).
- **Winograd (273 schemas, "partial evaluation" as in GPT-2).** 88.3% / 89.7% / 88.6% (zero/one/few), so there is no clear in-context learning. Results are a few points below SOTA (90.1) and estimated human performance. Some schemas were found in training data, with a small apparent effect (§4) (p. 17, Table 3.5).
- **Winogrande.** 70.2% / 73.2% / 77.7%, so there are gains from in-context learning. For comparison, fine-tuned RoBERTa gets 79%, the SOTA is 84.6% (fine-tuned T5), and human performance is 94.0% (p. 17).

#### 3.5 Common Sense Reasoning (pp. 17–18)
**Table 3.6 (p. 17).**

| Setting | PIQA | ARC (Easy) | ARC (Chall.) | OpenBookQA |
|---|---|---|---|---|
| Fine-tuned SOTA | 79.4 | 92.0 | 78.5 | 87.2 |
| GPT-3 zero-shot | 80.5* | 68.8 | 51.4 | 57.6 |
| GPT-3 one-shot | 80.5* | 71.2 | 53.2 | 58.8 |
| GPT-3 few-shot | 82.8* | 70.1 | 51.5 | 65.4 |

- **PIQA** (physical commonsense, a probe of grounded understanding of the physical world). Few-shot is measured on the test server. GPT-3 beats the prior SOTA of 79.4%, with shallow scaling, and is still over 10% below human performance. It is asterisked for potential contamination (pp. 17–18).
- **ARC.** On the Challenge set, GPT-3 approaches a fine-tuned RoBERTa baseline (55.9%). On the Easy set it slightly exceeds that baseline. UnifiedQA exceeds GPT-3 few-shot by 27% (Challenge) and 22% (Easy) (p. 18).
- **OpenBookQA.** A big zero- to few-shot improvement, but still over 20 points short of SOTA. Few-shot is similar to a fine-tuned BERT Large baseline (p. 18).
- Authors' summary: mixed results. There are small and inconsistent in-context gains on PIQA and ARC and a significant one on OpenBookQA. GPT-3 sets SOTA on PIQA in all settings (p. 18).

#### 3.6 Reading Comprehension (p. 18)
**Table 3.7 (F1; RACE = accuracy).**

| Setting | CoQA | DROP | QuAC | SQuADv2 | RACE-h | RACE-m |
|---|---|---|---|---|---|---|
| Fine-tuned SOTA | 90.7 | 89.1 | 74.4 | 93.0 | 90.0 | 93.1 |
| Zero-shot | 81.5 | 23.6 | 41.5 | 59.5 | 45.5 | 58.4 |
| One-shot | 84.0 | 34.3 | 43.3 | 65.4 | 45.9 | 57.4 |
| Few-shot | 85.0 | 36.5 | 44.3 | 69.8 | 46.8 | 58.1 |

- A wide spread across the five datasets suggests varying capability with different answer formats. In general GPT-3 is on par with initial baselines and early contextual-representation results (p. 18).
- Best: CoQA, within 3 points of the human baseline. Worst: QuAC, 13 F1 below an ELMo baseline (p. 18).
- DROP: few-shot beats the original fine-tuned BERT baseline but is well below humans and SOTA systems that add symbolic components (p. 18).
- SQuAD 2.0: few-shot gains almost 10 F1 over zero-shot and slightly outperforms the original paper's best fine-tuned result (p. 18).
- RACE: relatively weak, competitive only with the earliest contextual-representation work, and "45% behind SOTA" as stated (p. 18).

#### 3.7 SuperGLUE (pp. 18–20)
- Few-shot used 32 examples per task, sampled randomly from the training set. For all tasks except WSC and MultiRC a new set of examples was sampled per problem. For WSC and MultiRC the same randomly drawn set was used for all problems (pp. 18, 20).

**Table 3.8 (test set) (p. 19).**

| | SG avg | BoolQ | CB acc | CB F1 | COPA | RTE |
|---|---|---|---|---|---|---|
| Fine-tuned SOTA | 89.0 | 91.0 | 96.9 | 93.9 | 94.8 | 92.5 |
| Fine-tuned BERT-Large | 69.0 | 77.4 | 83.6 | 75.7 | 70.6 | 71.7 |
| GPT-3 few-shot | 71.8 | 76.4 | 75.6 | 52.0 | 92.0 | 69.0 |

| | WiC | WSC | MultiRC acc | MultiRC F1a | ReCoRD acc | ReCoRD F1 |
|---|---|---|---|---|---|---|
| Fine-tuned SOTA | 76.1 | 93.8 | 62.3 | 88.2 | 92.5 | 93.3 |
| Fine-tuned BERT-Large | 69.6 | 64.6 | 24.1 | 70.0 | 71.3 | 72.0 |
| GPT-3 few-shot | 49.4 | 80.1 | 30.5 | 75.4 | 90.2 | 91.1 |

- COPA and ReCoRD are near-SOTA in one- and few-shot. COPA falls only a couple of points short and is second on the leaderboard, behind a fine-tuned 11B model (T5). WSC is relatively strong (80.1%; 88.6% on original Winograd). BoolQ, MultiRC and RTE roughly match fine-tuned BERT-Large. CB shows "signs of life" at 75.6% (p. 20).
- WiC is a notable weak spot at 49.4%, "at random chance", despite several phrasings. The authors suggest GPT-3 appears to be weak in few-/one-shot at some tasks comparing two sentences or snippets: word sense in WiC, paraphrase, entailment. This "could also explain" the low RTE and CB scores (p. 20).
- GPT-3 beats fine-tuned BERT-Large on four of eight tasks, and on two tasks is close to the fine-tuned 11B SOTA (p. 20).
- Fig. 3.8 (dev-set numbers, so not directly comparable to the test-set reference lines): the score improves with model size and with K, up to K = 32, after which more examples will not reliably fit in context. GPT-3 needs fewer than eight total examples per task to beat fine-tuned BERT-Large on the overall score (p. 20).
- Caption comparison: the BERT-Large vs BERT++ gap (125K vs about 630K fine-tuning examples) is roughly equivalent to GPT-3 with one versus eight examples per context (p. 20).

#### 3.8 NLI (p. 21)
- NLI asks whether a second sentence follows from, contradicts, or is neutral to the first. RTE is the binary version (p. 21).
- On RTE, only the largest GPT-3 performs convincingly better than random (56%) in any setting. In the few-shot setting it performs similarly to a single-task fine-tuned BERT Large (p. 21).
- ANLI (adversarially mined, three rounds): all models smaller than GPT-3 are at almost exactly random chance (about 33%), even few-shot. GPT-3 shows "signs of life" on Round 3. The dev set has 1500 examples, with an estimated standard deviation of 1.2%. Few-shot 175B closes almost half the gap from random to SOTA (Fig. 3.9) (p. 21).
- Authors' conclusion: NLI is still very difficult for LMs, which are only just beginning to show progress (p. 21).

#### 3.9 Synthetic and Qualitative Tasks (pp. 21–28)
The goal is to probe on-the-fly reasoning, novel patterns, and quick adaptation. The authors will release the synthetic datasets (p. 21).

**3.9.1 Arithmetic (pp. 21–23).**
- Ten tests, asked in natural language, e.g. a question asking for the sum of 48 and 76 (answer 124).
  - 2D+/2D−: integers uniform on [0,100); the answer may be negative.
  - 3D±, 4D±, 5D±: uniform on [0,1000), [0,10000), [0,100000).
  - 2Dx: two integers from [0,100) multiplied.
  - 1DC: three one-digit numbers with parentheses around the last two, e.g. 6+(4*8); operations drawn from {+,−,*}.
- The answer must be exactly correct. Each task has 2,000 random instances (pp. 21–22).

**Table 3.9 (GPT-3 175B) (p. 23).**

| Setting | 2D+ | 2D− | 3D+ | 3D− | 4D+ | 4D− | 5D+ | 5D− | 2Dx | 1DC |
|---|---|---|---|---|---|---|---|---|---|---|
| Zero-shot | 76.9 | 58.0 | 34.2 | 48.3 | 4.0 | 7.5 | 0.7 | 0.8 | 19.8 | 9.8 |
| One-shot | 99.6 | 86.4 | 65.5 | 78.7 | 14.0 | 14.0 | 3.5 | 3.8 | 27.4 | 14.3 |
| Few-shot | 100.0 | 98.9 | 80.4 | 94.2 | 25.5 | 26.8 | 9.3 | 9.9 | 29.2 | 21.3 |

- Few-shot: accuracy falls as digits increase. The authors say 25–26% on four-digit and 9–10% on five-digit operations suggests at least some capacity to generalize to more digits (p. 22).
- Small models do poorly. Even 13B solves 2-digit addition/subtraction only about half the time, and everything else less than 10% of the time (Fig. 3.10: big jump from 13B to 175B) (p. 22).
- One- and zero-shot are degraded relative to few-shot, which the authors take to suggest that adapting to the task, or at least recognizing it, is important. Even zero-shot full GPT-3 significantly outperforms few-shot learning for all smaller models (pp. 22–23).
- **Memorization spot-check.** 3-digit problems were searched in the training data as "<NUM1> + <NUM2> =" and "<NUM1> plus <NUM2>". There were 17 matches among 2,000 addition problems (0.8%) and 2 among 2,000 subtraction problems (0.1%). The authors say this suggests only a trivial fraction of answers could be memorized. Incorrect answers often show errors like not carrying a "1", suggesting the model attempts the computation (p. 23).

*Intuition note.* The model gets 2-digit addition nearly perfect but only about 10% right on 5-digit. Wrong answers like a missing carry look like attempted calculation, not table lookup. The authors treat this as suggestive evidence, not proof.

**3.9.2 Word Scrambling and Manipulation (pp. 23–24).**
- Five character-manipulation tasks: recover the original word from
  - CL: letters cycled ("lyinevitab" → "inevitably");
  - A1: all letters but first and last scrambled ("criroptuon" = "corruption");
  - A2: all letters but first two and last two scrambled ("opoepnnt" → "opponent");
  - RI: random punctuation or space inserted between letters;
  - RW: word spelled backwards ("stcejbo" → "objects") (p. 23).
- Each task has 10,000 examples: the top 10,000 most frequent words (per [Nor09]) with length more than 4 and less than 15 characters. Few-shot uses K = 100 (pp. 23–24).

**Table 3.10 (GPT-3 175B) (p. 23).**

| Setting | CL | A1 | A2 | RI | RW |
|---|---|---|---|---|---|
| Zero-shot | 3.66 | 2.28 | 8.91 | 8.26 | 0.09 |
| One-shot | 21.7 | 8.62 | 25.9 | 45.4 | 0.48 |
| Few-shot | 37.9 | 15.1 | 39.7 | 67.2 | 0.44 |

- Performance tends to grow smoothly with size. No model can reverse letters in a word. One-shot performance is dropping "by half or more" and zero-shot is rarely able to perform the tasks. The authors say this suggests the model appears to learn these tasks at test time, since it cannot do them zero-shot and the tasks are artificial and unlikely to be in the pre-training data. They add that they cannot confirm this with certainty (p. 24).
- In-context learning curves (performance versus number of examples) for symbol insertion are in Fig. 1.2. Larger models use in-context information, both examples and task descriptions, more effectively (p. 24).
- BPE tokens average about 0.7 words per token, so success needs "pulling apart" token substructure. CL, A1 and A2 are not bijective (the answer is not a deterministic function of the scrambled word), so some search is required (p. 24).

**3.9.3 SAT Analogies (p. 24).**
- 374 SAT analogy problems (a section of the SAT before 2005), five choices each, e.g. the pair audacious:boldness, whose correct choice is sanctimonious:hypocrisy.
- GPT-3 gets 65.2% few-shot, 59.1% one-shot and 53.7% zero-shot. The average college applicant scored 57% and random guessing gives 20% (p. 24).
- The 175B model improves by over 10% over 13B (p. 24, Fig. 3.12 shows K = 20) (p. 25).

**3.9.4 News Article Generation (pp. 25–28).**
- Raw samples are less effective because GPT-3's training data is much less weighted towards news. It often treats a news first sentence as a tweet. So three previous news articles were put in the context. With a title and subtitle, the model can reliably generate short articles in the news genre (p. 25).
- *Rationale:* LMs are trained to match the human distribution, so humans' (in)ability to tell model text from human text is a potentially important quality measure (p. 25).
- **Design.** 25 titles/subtitles from newser.com (mean 215 words). Completions came from "four language models" ranging from 125M to 175B parameters (mean 200 words). About 80 US-based participants per model judged real versus model articles on a five-point scale (very likely human … very likely machine) (p. 25).
- **Controls.**
  - Articles were not in training data.
  - Outputs were selected programmatically, with no human cherry-picking.
  - All models used the same context.
  - A control model (160M parameters, no context, increased output randomness) with intentionally bad articles checked participant effort (p. 25).
- Accuracy = correct assignments / non-neutral assignments. A two-sample Student's t-test compares each model with the control (p. 26, fn. 5).

**Table 3.11 (short articles) (p. 26).**

| Model | Mean acc. | 95% CI | t vs control (p) | "I don't know" |
|---|---|---|---|---|
| Control | 86% | 83–90% | – | 3.6% |
| GPT-3 Small | 76% | 72–80% | 3.9 (2e−4) | 4.9% |
| Medium | 61% | 58–65% | 10.3 (7e−21) | 6.0% |
| Large | 68% | 64–72% | 7.3 (3e−11) | 8.7% |
| XL | 62% | 59–65% | 10.7 (1e−19) | 7.5% |
| 2.7B | 62% | 58–65% | 10.4 (5e−19) | 7.1% |
| 6.7B | 60% | 56–63% | 11.2 (3e−21) | 6.2% |
| 13B | 55% | 52–58% | 15.3 (1e−32) | 7.1% |
| 175B | 52% | 49–54% | 16.9 (1e−34) | 7.8% |

- Accuracy on the control was about 86% (chance 50%). On 175B output it was about 52%, "barely above chance". Detection ability "appears to decrease" with model size, with a trend towards chance, even though participants spend more time per output as models grow (Appendix E). Fig. 3.13 shows a power-law line of best fit (pp. 26–27).
- Footnote 6: if a model consistently produced text more impressive than human articles, accuracy could fall below 50%. Many individual participants did score below 50% (p. 26).
- Examples in Figs. 3.14–3.15. The article humans found hardest to identify had 12% accuracy, and the easiest had 61% (p. 28).
- Possible giveaways: factual inaccuracies (the model lacks access to the specific facts), repetition, non sequiturs and unusual phrasings, often too subtle to notice. Ippolito et al. indicate automatic discriminators (GROVER, GLTR) may do better than humans (p. 26).
- **Longer articles.** Ippolito et al. also note accuracy rises as humans see more tokens. The authors ran 12 Reuters articles (average 569 words; completions averaging 498 words) with about 80 participants each. Accuracy was about 88% on the control and about 52% on GPT-3 175B (Table 3.12: t = 12.7, p = 3.2e−23; "I don't know" 2.7% vs 10.6%) (pp. 26–27).

*Intuition note.* Participants spot a deliberately bad model about 86–88% of the time and 175B output about 52% of the time. They are barely above a coin flip even for ~500-word articles. That is a statement about average US internet users in this design, not about detection tools.

**3.9.5 Learning and Using Novel Words (p. 26; continues beyond this part).** This part ends mid-section. It sets up a developmental-linguistics-style qualitative test: GPT-3 gets the definition of a nonexistent word such as "Gigamuru" and must use it in a sentence. The text on p. 26 breaks off after saying that one to five previous examples of a (separate) item are provided; the rest is on the next page.

## Toy example (ours, not from the text)
**Goal:** show how a prompt alone specifies a task and how multiple-choice scoring in §2.4 works, with no weight updates.

*Prompt (K = 2):*
"Alice visited her friend ___ . → Bob / The cat sat on the ___ . → mat / The doctor treated her ___ . →"

Two candidate completions have these made-up log-probabilities per token under the frozen model:
- A = " patient", 1 token: log p = −2.0.
- B = " old family friend today", 4 tokens: log p = −1.0, −1.5, −1.2, −1.5.

1. Total log-likelihood: A = −2.0. B = −1.0 − 1.5 − 1.2 − 1.5 = −5.2. By total, A wins (−2.0 > −5.2), which just rewards short answers.
2. Per-token (the paper's default, p. 10): A = −2.0 / 1 = −2.0. B = −5.2 / 4 = −1.3. B now wins (−1.3 > −2.0).
3. Unconditional normalization (used for ARC, OpenBookQA, RACE, p. 10), with made-up unconditional scores after "A:": log P(A | "A:") = −2.5 and log P(B | "A:") = −6.0.
   - Score for A: −2.0 − (−2.5) = +0.5, a probability ratio of exp(0.5) ≈ 1.65.
   - Score for B: −5.2 − (−6.0) = +0.8, a ratio of exp(0.8) ≈ 2.23.
   - B wins again. This rewards answers made more likely by the context than by the generic "answer" prompt.

Different scoring rules can choose different answers, and none of them changes any weight. The toy is only meant to show the mechanics.

## Concepts
- [[in-context-learning]] — inner loop of meta-learning: the task is conditioned on in the forward pass, via an instruction and/or demonstrations, with no weight updates (p. 3–4)
- [[zero-shot-few-shot-prompting]] — zero-/one-/few-shot = 0 / 1 / K (typically 10–100) demonstrations in context, plus an optional natural-language description (pp. 5–7)
- [[pretraining-fine-tuning]] — the paradigm the paper contrasts with: weights updated on thousands to hundreds of thousands of task examples (pp. 3, 6)
- [[meta-learning]] (new) — here: the model acquires broad skills in the outer loop (SGD pre-training) and uses them to adapt or recognize a task in the inner loop (p. 3–4, fn. 1)
- [[scaling-law]] — validation loss follows an approximate power law in compute; the paper's Fig. 3.1 fit is $L = 2.57\,C^{-0.048}$ (pp. 8, 10–11)
- [[language-model]] — here an autoregressive transformer (GPT-2 architecture, alternating dense and sparse attention) with $n_{\text{ctx}} = 2048$ (pp. 1, 8)
- [[perplexity]] — used for zero-shot PTB (20.5) and LAMBADA ppl (3.00 / 3.35 / 1.92) (pp. 11–12)
- [[cross-entropy-log-loss]] — validation loss tracked across sizes; the paper says it correlates well with many downstream tasks (pp. 4, 10)
- [[tokenization-bpe]] — byte-level BPE inherited from GPT-2, about 0.7 words per token; the authors suggest it may hurt En→Ro and complicates character-level tasks (pp. 16, 24)
- [[data-contamination]] (new) — test or dev content inadvertently present in the pre-training corpus; assessed in §4, with asterisks on some results (pp. 6, 9)
- [[closed-book-qa]] (new) — answering factual questions from model parameters only, without retrieval or fine-tuning on the QA set (p. 13)
- [[human-detection-of-generated-text]] (new) — mean accuracy = correct / non-neutral assignments, compared to a control with a two-sample t-test (pp. 25–26)

## Canonical instances
- [[gpt-3-175b]] — the 175B autoregressive model; 96 layers, $d_{\text{model}} = 12288$, trained on 300B tokens (p. 8)
- [[lambada-cloze-framing]] — few-shot framing as a fill-in-the-blank cloze addresses the one-word-completion problem and reaches 86.4% accuracy (p. 12)
- [[triviaqa-closed-book]] — few-shot 71.2%; one-shot (68.0) matches the fine-tuned open-domain RAG (pp. 13–14)
- [[translation-direction-asymmetry]] — GPT-3 is much stronger translating into English than out of it (pp. 15–16)
- [[superglue-wic-weakness]] — few-shot WiC 49.4%, at random chance; suggested weakness on sentence-comparison tasks (p. 20)
- [[arithmetic-battery]] — ten tests; 100% on 2-digit addition few-shot; memorization check finds 0.8% / 0.1% matches (pp. 22–23)
- [[word-scrambling-tasks]] — five character-manipulation tasks that the authors think are unlikely to appear in pre-training (they cannot confirm this); zero-shot performance is near zero and no model reverses words (pp. 23–24)
- [[news-article-detection-experiment]] — humans at about 52% on 175B articles versus about 86% on the control (pp. 25–27)

## Bridges (candidates)
- [structural-analogy] Inner loop (in-context learning) / outer loop (SGD) ↔ ML: meta-learning, learning to learn across a distribution of tasks — the authors say the structure is the same, while staying agnostic on mechanism (p. 4, fn. 1)
- [same-math] Two-sample t-test on participant accuracies, GPT-3 vs control (Table 3.11) ↔ statistics: the standard Student's two-sample test (p. 26, fn. 5)
- [structural-analogy] The news-detection quiz ↔ computational social science: survey-experiment design with an attention-check control arm (pp. 25–26)
- [structural-analogy] Data contamination of benchmarks ↔ train–test leakage / measurement validity in empirical social science (pp. 6, 9)
- [metaphor] Smooth power-law loss in compute ↔ empirical regularities in physics-style scaling relations; here the claim is only an empirical fit (p. 11)

## Questions this raises
- When the model "learns" a task from a prompt (e.g. word scrambling), is it learning something new or recognizing a pattern seen in training? The authors flag this as important and agnostic here (p. 4, fn. 1; p. 24).
- How much of the benchmark performance is inflated by contamination from the undetected overlaps? §4 is promised to quantify it (pp. 6, 9).
- Why are tasks that compare two sentences (WiC, RTE, CB, ANLI) especially hard few-shot (p. 20)?
- Will the human-detection result hold for non-US, expert, or longer-reading evaluators, or against automatic detectors (p. 26)?

## Reading notes
- **Scope.** This part runs from printed p. 1 (title and abstract) to p. 28, ending mid-§3.9.5 (Learning and Using Novel Words, which starts on p. 26). The rest of §3.9.5 and the later sections and appendices (§§4–8 and Appendices A–H, listed on p. 2) are not in these pages. Printed page number = pdf page number.
- **Page 2** is the table of contents, covering sections and appendices not in this part.
- **Citation keys** (e.g. [KMH+20]) appear as keys only; the reference list is not in these pages. The SuperGLUE citation block in §3.7 (p. 18) repeats [WPN+19] in the text layer.
- **Misprints and inconsistencies:**
  - §2.4 says "the 200B few-shot results" are submitted to test servers. Elsewhere the largest model is 175B (p. 10).
  - Text on PIQA says 81.0% zero-shot (p. 17), but Table 3.6 gives 80.5* (p. 17).
  - In §3.9.1 the text gives 80.2% for 3-digit addition (p. 22), while Table 3.9 gives 80.4 (p. 23).
  - In §3.9.2 the text gives 66.9 / 38.6 / 40.2 / 15.1 for RI / CL / A2 / A1 (p. 24), but Table 3.10 gives 67.2 / 37.9 / 39.7 / 15.1 (p. 23).
  - §3.9.4 text says "four language models" (p. 25), but Table 3.11 lists eight GPT-3 sizes plus a control, and its caption says "five different models" (p. 26).
  - Control model: the text describes a 160M-parameter model with no context and higher randomness (p. 25); the table caption calls it an unconditional GPT-3 Small with increased output randomness (p. 26).
  - Fig. 3.13 shows the control line at 86%. Table 3.11 gives 86% and Table 3.12 gives 88% for the longer articles.
  - Table 2.1 prints $d_{\text{model}} = 5140$ for 13B. Our check: $40\times128 = 5120$. For XL, $24\times128 = 3072 \ne 2048$ (our observation).
  - Table 2.2 weights sum to 101% (rounding).
- Figure values (e.g. Fig. 3.4) are read from plots only where stated in the text.
