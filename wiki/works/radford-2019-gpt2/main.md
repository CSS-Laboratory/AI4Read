---
id: radford-2019-gpt2/main
work: radford-2019-gpt2
unit: paper
pages: pdf 1–24 (page labels give no printed numbers; see Reading notes)
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Language Models are Unsupervised Multitask Learners (GPT-2)

## L0 — One line
A large Transformer language model trained only to predict the next token on a big, varied web corpus (WebText) can begin to do many NLP tasks zero-shot, and it improves with model size.

## L1 — The gist (≤ 120 words)
The paper asks whether a language model trained only to predict the next token can perform NLP tasks without any task-specific training (zero-shot). The authors build WebText (about 8 million web pages, 40 GB). They train Transformer language models of four sizes, up to 1.5B parameters (GPT-2), and specify tasks as plain text in the prompt. Results are strong on language-modeling and commonsense benchmarks and competitive with some supervised baselines on reading comprehension. They are weak on summarization, translation and question answering. Performance generally rises with model size. The authors suggest that tasks demonstrated naturally in text can be learned as a by-product of next-token prediction, but they call the practical performance "far from use-able".

**Prerequisites:** conditional probability and the product rule; logarithms and exponentials (perplexity); what a Transformer language model does at a high level; train/test splits.

## L2 — Key ideas (5–10 bullets)
- **Task as text.** A task can be written as a token sequence, so a language model that models $p(\text{output}\mid\text{input},\text{task})$ needs no separate architecture per task (pdf 2).
- **Core hypothesis (the authors' speculation).** A language model with enough capacity will learn to infer and perform tasks shown in natural text, because that helps it predict the text (pdf 3).
- **Data.** WebText is built from outbound Reddit links with at least 3 karma (Reddit's vote score), with Wikipedia removed. It is about 8M documents and 40 GB (pdf 3).
- **Input representation.** Byte-level BPE (byte pair encoding, which merges frequent byte pairs into tokens) can assign a probability to any string. It blocks merges across character categories, with an exception for spaces (pdf 4).
- **Results.** Zero-shot state of the art on 7 of 8 language-modeling datasets. 55 F1 (an answer-overlap score) on CoQA (a conversational reading-comprehension test). Weak on summarization, translation and Natural Questions (pdf 5–7).
- **Scale matters.** The authors report that performance improves with model size across tasks (pdf 1–2). The curves are not uniformly monotone (e.g. summarization is flat at the top sizes in Figure 1). On question answering and translation, models beat trivial baselines only with sufficient capacity (pdf 9).
- **Memorization check.** The authors' analysis of test–train overlap of 8-grams (runs of 8 consecutive words) suggests a small but consistent benefit. Train and held-out perplexity are similar, which suggests the model still underfits WebText (it has not fit its training data as well as it could) (pdf 8).
- **Limits stated by the authors.** Zero-shot performance is a baseline; the ceiling with fine-tuning (extra supervised training) is unclear (pdf 9).

## L3 — Walkthrough

### Abstract and 1. Introduction (pdf 1)
- Typical NLP tasks are approached with supervised learning on task-specific datasets. The authors report that language models begin to learn these tasks without explicit supervision when trained on WebText (pdf 1).
- Reported headline numbers: 55 F1 on CoQA, which matches or exceeds 3 of 4 baseline systems without using their 127,000+ training examples. GPT-2 is a 1.5B-parameter Transformer with state of the art on 7 of 8 tested language-modeling datasets in a zero-shot setting, but it still underfits WebText (pdf 1).
- The abstract also says that the capacity of the language model is essential to zero-shot task transfer and that increasing it improves performance in a log-linear fashion across tasks, and that samples from the model contain coherent paragraphs (pdf 1).
- **Problem diagnosed.** The dominant recipe is to collect examples of correct behavior, train a system to imitate them, and test on IID held-out examples (IID = drawn from the same distribution as the training data). The authors say current systems are better described as narrow experts than as competent generalists (pdf 1). The authors cite brittleness of captioning, reading-comprehension and image-classification systems (pdf 1).
- **Author's suspicion.** Single-task training on single-domain datasets is a major contributor to the lack of generalization. Robust systems are likely to need training and measurement across many domains and tasks. GLUE and decaNLP are cited as benchmarks that begin to study this (pdf 1).
- **Multitask learning is nascent in NLP.** The two most ambitious efforts trained on 10 and 17 (dataset, objective) pairs. From a meta-learning view each pair is one training example. Current ML needs hundreds to thousands of examples to generalize, so multitask training may need as many pairs. The authors say it will be very difficult to keep scaling dataset and objective creation to the degree that may be required. This motivates other setups (pdf 1).
- **Transfer history** (pdf 2): word vectors fed into task-specific architectures, then contextual representations from recurrent networks, then transferring many self-attention blocks. All of these still need supervised training to do a task. A separate line of work shows language models doing specific tasks (commonsense reasoning, sentiment analysis) with little or no supervised data. This paper joins the two lines: zero-shot transfer to down-stream tasks, with no change to parameters or architecture (pdf 2).

**Intuition note.** The paper's bet is that more and more varied text, plus a bigger model, can replace collecting a labelled dataset for each task. It does not claim this already works well.

### 2. Approach (pdf 2–3)
- Language modeling is framed as unsupervised distribution estimation over sequences of symbols $(s_1,\dots,s_n)$. Because language is ordered, the joint probability is factorized into conditionals (pdf 2). Eq. (1), copied as printed:
$$p(x)=\prod_{i=1}^{n} p(s_n\mid s_1,\dots,s_{n-1}) \tag{1}$$
- The authors say this allows tractable sampling from and estimation of $p(x)$, and of conditionals such as $p(s_{n-k},\dots,s_n\mid s_1,\dots,s_{n-k-1})$. Better models of these conditionals, such as the Transformer, have recently appeared (pdf 2).
- **Task conditioning.** One task is estimating $p(output\mid input)$. A general system should model $p(output\mid input, task)$. Task conditioning is often done architecturally (task-specific encoders and decoders) or algorithmically (MAML's inner and outer loops). Language offers a third way: specify task, input and output as one symbol sequence, following McCann et al. (pdf 2).
  - Translation example: `(translate to french, english text, french text)`.
  - Reading-comprehension example: `(answer the question, document, question, answer)`.
  - McCann et al. (2018) trained a single model, the MQAN, to infer and perform many tasks in this format (pdf 2–3).
- **Why language modeling could learn such tasks.** The supervised objective is the same as the unsupervised objective evaluated on a subset of the sequence. So the global minimum of the unsupervised objective is also the global minimum of the supervised objective. This holds in a "slightly toy setting". There the concerns about density estimation as a training objective are side-stepped. The remaining question is whether the unsupervised objective can be optimized to convergence in practice. Preliminary experiments confirmed that sufficiently large LMs can do multitask learning in this toy-ish setup, but learning is much slower than in explicitly supervised approaches (pdf 3).
- **Weston (2016)** argued for learning from natural language directly, in dialog, and gave a proof of concept. The authors worry dialog is "overly restrictive", because the internet holds much passively available information (pdf 3).
- **Author's speculation:** a language model with sufficient capacity will begin to infer and perform the tasks demonstrated in natural-language sequences in order to better predict them, however the data were procured. Doing so would be "unsupervised multitask learning". They test this by evaluating zero-shot performance on many tasks (pdf 3).

**Intuition note.** If a text contains "English … = French …" pairs, predicting the French part well is easier with some ability to translate. So training on prediction alone might push task skills to appear. The paper treats this as a hypothesis to test, not as a proven fact.

#### 2.1 Training dataset (pdf 3–4)
- Most prior LMs used one domain (news, Wikipedia, fiction). The authors want a large, diverse dataset so that natural demonstrations of tasks appear in many contexts (pdf 3).
- Common Crawl is huge but has data-quality problems. Trinh & Le (2018) noted a large amount of documents whose content was mostly unintelligible. Their best results used a subsample similar to their target task. The authors want to avoid assuming the tasks in advance (pdf 3).
- **WebText.** Scrape only pages curated by humans. As a starting point, take all outbound Reddit links with at least 3 karma, a heuristic for whether users found a link interesting, educational or funny. This gave 45 million links. Text was extracted with Dragnet and Newspaper (pdf 3).
- The version used has no links created after Dec 2017. After de-duplication and heuristic cleaning it has slightly over 8 million documents and 40 GB of text. All Wikipedia documents were removed, because Wikipedia is a common source for other datasets and could cause overlap between training data and evaluation tasks (pdf 3–4).
- Table 1 (pdf 3) shows naturally occurring English–French and French–English translation demonstrations found in WebText, for example quotes with a French phrase and its translation.

#### 2.2 Input representation (pdf 4)
- A general LM should compute the probability of, and generate, any string. Lower-casing, tokenization and out-of-vocabulary tokens restrict the strings a model can handle. Pure byte-level LMs satisfy this but are not competitive with word-level LMs on large datasets. The authors saw the same gap on WebText (pdf 4).
- **BPE** (byte pair encoding) is a middle ground between character and word level. It acts like word-level input for frequent sequences and character-level input for rare ones. Reference implementations work on Unicode code points. That needs a base vocabulary of over 130,000, against the 32,000–64,000 token vocabularies often used. Byte-level BPE needs a base of 256 (pdf 4).
- Applying BPE directly to bytes gives sub-optimal merges, because the greedy frequency heuristic creates many variants of common words such as `dog.` `dog!` `dog?`. This wastes vocabulary slots and capacity. Fix: **prevent merges across character categories** for any byte sequence, with an exception for spaces. The exception significantly improves compression efficiency and adds only minimal fragmentation of words (pdf 4).
- Result: the model can assign a probability to any Unicode string, so it can be evaluated on any dataset regardless of pre-processing, tokenization or vocabulary (pdf 4).

#### 2.3 Model (pdf 4)
Transformer, largely following OpenAI GPT, with these changes (pdf 4):
- Layer normalization moved to the input of each sub-block, plus one more layer norm after the final self-attention block.
- Modified initialization: residual-layer weights are scaled at initialization by $1/\sqrt{N}$, where $N$ is the number of residual layers.
- Vocabulary 50,257. Context size 512 → 1024 tokens. Batch size 512.

Table 2 (pdf 4):

| Parameters | Layers | $d_{model}$ |
|---|---|---|
| 117M | 12 | 768 |
| 345M | 24 | 1024 |
| 762M | 36 | 1280 |
| 1542M | 48 | 1600 |

### 3. Experiments (pdf 4)
- Four LMs with approximately log-uniformly spaced sizes. The smallest equals the original GPT. The second equals the largest BERT model. The largest is called GPT-2 and has over an order of magnitude more parameters than GPT (pdf 4).
- Learning rate was tuned manually for best perplexity on a 5% held-out sample of WebText. All models still underfit WebText, and held-out perplexity has so far kept improving with more training time (pdf 4).

#### 3.1 Language modeling (pdf 4–5)
- The zero-shot test here is domain transfer on the model's own task. Because the model is byte-level, it can be evaluated on any LM benchmark. The authors compute the log-probability of a dataset under the WebText LM and divide by the number of canonical units (character, byte or word). This gives the usual scaled or exponentiated average negative log-probability (pdf 4).
- Many benchmarks are far out-of-distribution for WebText: aggressively standardized text, tokenization artifacts, shuffled sentences, and `<UNK>`, which occurs only 26 times in 40 billion bytes of WebText (pdf 4–5).
- Main results use invertible de-tokenizers that remove such artifacts. They keep log-probabilities computable and can be thought of as a simple form of domain adaptation. They give gains of 2.5 to 5 perplexity for GPT-2 (pdf 5).

Table 3 (pdf 5), zero-shot. PPL = perplexity, ACC = accuracy, BPB/BPC = bits per byte/character. No training or fine-tuning was done.

| | LAMBADA PPL | LAMBADA ACC | CBT-CN | CBT-NE | WikiText2 | PTB | enwik8 | text8 | WikiText103 | 1BW |
|---|---|---|---|---|---|---|---|---|---|---|
| SOTA | 99.8 | 59.23 | 85.7 | 82.3 | 39.14 | 46.54 | 0.99 | 1.08 | 18.3 | 21.8 |
| 117M | 35.13 | 45.99 | 87.65 | 83.4 | 29.41 | 65.85 | 1.16 | 1.17 | 37.50 | 75.20 |
| 345M | 15.60 | 55.48 | 92.35 | 87.1 | 22.76 | 47.33 | 1.01 | 1.06 | 26.37 | 55.72 |
| 762M | 10.87 | 60.12 | 93.45 | 88.0 | 19.93 | 40.31 | 0.97 | 1.02 | 22.05 | 44.575 |
| 1542M | 8.63 | 63.24 | 93.30 | 89.05 | 18.34 | 35.76 | 0.93 | 0.98 | 17.48 | 42.16 |

- The authors say WebText LMs improve the state of the art on 7 of 8 datasets zero-shot. Large improvements appear on small datasets (PTB, WikiText-2; 1–2 million training tokens) and on long-dependency datasets (LAMBADA, CBT) (pdf 5).
- The model is "still significantly worse" than prior work on One Billion Word (1BW). The authors say this is likely due to a combination of 1BW being the largest dataset and having some of the most destructive pre-processing: sentence-level shuffling removes all long-range structure (pdf 5).

**Intuition note.** Without any training on these datasets, the larger model beats earlier specialized models on most of them. The authors say the one clear loss (1BW) is likely due to its size and its destructive pre-processing: sentence-level shuffling removes long-range structure.

#### 3.2 Children's Book Test (pdf 5)
- CBT tests word categories (named entities, nouns, verbs, prepositions) as a 10-choice cloze test (fill-in-the-blank). Following the original LM approach, the model scores each choice plus the rest of the sentence and picks the highest probability (pdf 5).
- Accuracy rises steadily with size and closes the majority of the gap to human performance (Figure 2). One test-set book, *The Jungle Book*, is in WebText, so results are reported on the validation set. GPT-2 reaches 93.3% on common nouns and 89.1% on named entities (Table 3 shows 93.30 and 89.05) (pdf 5).

#### 3.3 LAMBADA (pdf 5–6)
- Task: predict the final word of sentences that need at least 50 tokens of context for a human to predict (pdf 5).
- GPT-2 improves perplexity from 99.8 to 8.6 and LM accuracy from 19% to 52.66% (pdf 5).
- Error analysis: most wrong predictions are valid continuations but not valid final words. The authors say this suggests the LM is not using the constraint that the word must end the sentence. A stop-word filter approximates this and raises accuracy to 63.24%, improving the state of the art by 4% (pdf 5).
- The previous state of the art restricted outputs to words that appeared in the context. For GPT-2 this restriction is harmful, since 19% of answers are not in the context. An unpreprocessed version of the dataset is used (pdf 5–6).

#### 3.4 Winograd Schema Challenge (pdf 6)
- This commonsense task resolves ambiguities in text. Following Trinh & Le (2018), the LM picks the resolution with higher probability, with full and partial scoring (Figure 3). GPT-2 improves state-of-the-art accuracy by 7%, reaching 70.70%. The dataset has only 273 examples, so the authors point readers to Trichelair et al. (2018) for context (pdf 6).

#### 3.5 Reading comprehension (CoQA) (pdf 6)
- CoQA: documents from 7 domains with question–answer dialogues, so answers can depend on conversation history (pdf 6).
- Greedy decoding conditioned on document, conversation history and a final token `A:` gives 55 F1 on the development set. This matches or exceeds 3 of 4 baselines, without their 127,000+ training pairs. The supervised SOTA (BERT-based) is nearing the 89 F1 of humans (pdf 6).
- Inspection suggests GPT-2 often uses simple retrieval-based heuristics, for example answering a *who* question with a name from the document (pdf 6).

#### 3.6 Summarization (pdf 6)
- On CNN/Daily Mail, the prompt adds `TL;DR:` after the article. The model generates 100 tokens with top-$k$ random sampling, $k=2$ (choose among the 2 most likely next tokens). The authors say this reduces repetition and encourages more abstractive summaries than greedy decoding. The first 3 generated sentences are the summary (pdf 6).
- Qualitatively the outputs resemble summaries but often focus on recent content or confuse details (e.g. number of cars in a crash) (pdf 6).

Table 4 (ROUGE F1; R-AVG is the average of R-1, R-2 and R-L), pdf 6:

| | R-1 | R-2 | R-L | R-AVG |
|---|---|---|---|---|
| Bottom-Up Sum (SOTA) | 41.22 | 18.68 | 38.34 | 32.75 |
| Lede-3 | 40.38 | 17.66 | 36.62 | 31.55 |
| Seq2Seq + Attn | 31.33 | 11.81 | 28.83 | 23.99 |
| GPT-2 TL;DR: | 29.34 | 8.27 | 26.58 | 21.40 |
| Random-3 | 28.78 | 8.63 | 25.52 | 20.98 |
| GPT-2 no hint | 21.58 | 4.03 | 19.47 | 15.03 |

- The authors say GPT-2 only begins to approach classic neural baselines and "just barely" outperforms selecting 3 random sentences. Removing the hint costs 6.4 points on the aggregate metric, which they say shows that task-specific behavior can be invoked in an LM with natural language (pdf 6).

#### 3.7 Translation (pdf 6–7)
- The context is example pairs in the format `english sentence = french sentence`. The final prompt is `english sentence =`. GPT-2 samples greedily and the first generated sentence is the translation (pdf 6).
- WMT-14 English→French: 5 BLEU, slightly worse than word-by-word substitution with a bilingual lexicon inferred in earlier unsupervised work. French→English: 11.5 BLEU. This beats several unsupervised MT baselines but is much worse than the 33.5 BLEU of the best unsupervised MT approach (pdf 6–7).
- This was surprising, because non-English pages were deliberately removed from WebText. A byte-level language detector found only 10 MB of French in WebText, about 500× smaller than the monolingual French corpora common in prior unsupervised MT work (pdf 7).

#### 3.8 Question answering (pdf 7)
- Natural Questions is used to test how often the LM generates correct factoid answers. The context is seeded with example question–answer pairs so the model infers the short-answer style (pdf 7).
- GPT-2 answers 4.1% correctly by exact match. The smallest model does not exceed the 1.0% of a baseline that returns the most common answer for each question type. GPT-2 answers 5.3 times more questions correctly. The authors suggest model capacity has been a major factor in the poor performance of neural systems on this task so far (pdf 7).
- The probability GPT-2 assigns to answers is "well calibrated". Accuracy is 63.1% on the 1% of questions it is most confident in. Table 5 lists the 30 most confident answers. By my count 22 of them are marked correct, and none of the questions appear in WebText according to Section 4's procedure (pdf 7).
- GPT-2 is still much worse than the 30–50% of open-domain QA systems that combine retrieval and extractive reading (pdf 7).
- Footnote 3: the first author answered 17 of 100 sampled examples under the same setting. The note then corrects this to 14 right (pdf 7).

**Intuition note (3.5–3.8).** Across these tasks results are mostly below specialized systems and rise with model size. On some tasks GPT-2 is only just above (summarization) or even slightly below (En→Fr translation) simple baselines. Reading comprehension is the closest to supervised results; translation, summarization and QA are far behind.

### 4. Generalization vs memorization (pdf 8)
- Motivation: image datasets such as CIFAR-10 contain near-duplicates between train and test (3.3% overlap), which over-reports generalization. A similar problem could affect WebText (pdf 8).
- **Method.** Bloom filters (compact set-membership structures that may give false positives but no false negatives) hold the 8-grams of the WebText training set. Strings are normalized to lower-cased alphanumeric words. The false-positive rate is upper-bounded by $\frac{1}{10^{8}}$ (the text layer shows "1018" but the image shows $1/10^8$). A check with 1M generated strings found none (pdf 8).
- The approach optimizes for recall. Manual inspection shows many common phrases but also many longer matches from duplicated data (pdf 8).

Table 6 (pdf 8): percentage of test-set 8-grams that overlap with training sets.

| | PTB | WikiText-2 | enwik8 | text8 | WikiText-103 | 1BW |
|---|---|---|---|---|---|---|
| Dataset train | 2.67% | 0.66% | 7.50% | 2.34% | 9.09% | 13.19% |
| WebText train | 0.88% | 1.63% | 6.31% | 3.94% | 2.42% | 3.75% |

- Test sets overlap 1–6% with WebText train (average 3.2%). Many datasets overlap more with their own train splits (average 5.9%). The WikiText-103 test set has an article also in its training set; with only 60 test articles this is at least 1.6%. 1BW overlaps nearly 13.2% with its own training set (pdf 8).
- **Per-task checks** (pdf 8):
  - Winograd: only 10 schemata had any 8-gram overlap; 2 were spurious. Of the other 8, only 1 appeared in contexts that gave away the answer.
  - CoQA: about 15% of news-domain documents are already in WebText, and the model does about 3 F1 better on these. Overall gain from overlap is about 0.5–1.0 F1. No CoQA training questions or answers are in WebText, because CoQA was released after the link cutoff.
  - LAMBADA: average overlap 1.2%. Examples with more than 15% overlap get about 2 perplexity better. Excluding all examples with any overlap shifts 8.6 → 8.7 perplexity and 63.2% → 62.9% accuracy. Likely cause of the small change: only 1 in 200 examples has significant overlap.
- **Conclusion (author).** Their analysis suggests that overlap gives a "small but consistent benefit". For most datasets the overlaps are not significantly larger than those already between standard train and test sets. They recommend n-gram-overlap de-duplication as a sanity check when building new train/test splits, and they note that scalable fuzzy matching could help (pdf 8).
- **Second check.** Train and held-out performance on WebText are similar and improve together with size (Figure 4). This suggests that even GPT-2 is still underfitting WebText in many ways (pdf 8).

**Intuition note.** If the model had mostly memorized, its training perplexity would pull far below test perplexity. They stay close, and removing overlapping examples barely changes LAMBADA scores. This fits the authors' conclusion that overlap gives only a small but consistent benefit.

### 5. Related work (pdf 8–9)
- Closest work: Jozefowicz et al. (scaled RNN LMs on 1BW), Bajgar et al. (larger CBT training set from Project Gutenberg), and Hestness et al. (performance versus model and data size). The authors say their noisier results suggest similar trends hold for sub-tasks and continue into the 1B+ parameter regime (pdf 9).
- Learned functionality in generative models has been documented (RNN cells tracking line width and quotes). Liu et al.'s observation that a Wikipedia-generating model also learned to translate names was "more inspirational" (pdf 9).
- The section also lists web-corpus alternatives (iWeb) and pre-training work (GloVe, Skip-thought, Howard & Ruder (2018), and others) (pdf 9).

### 6. Discussion (pdf 9–10)
- Results suggest that unsupervised task learning is an additional promising research area. They "potentially help explain" the success of pre-training, which "in the limit" begins to learn tasks directly (pdf 9).
- Reading comprehension is competitive with supervised baselines zero-shot. On summarization the performance is "rudimentary" by quantitative metrics. In practical terms the zero-shot performance is "far from use-able" (pdf 9).
- There are undoubtedly practical tasks where GPT-2 is no better than random. On QA and translation, LMs begin to outperform trivial baselines only with sufficient capacity (pdf 9).
- The ceiling with fine-tuning is unclear. On some tasks GPT-2's fully abstractive output departs significantly from the extractive pointer-network outputs that are state of the art on many QA and reading-comprehension datasets (pdf 9). The authors plan to fine-tune on decaNLP and GLUE, noting it is unclear whether more data and capacity can overcome the inefficiencies of uni-directional representations shown by BERT (pdf 9–10).

### 7. Conclusion (pdf 10)
- A large LM trained on a sufficiently large and diverse dataset performs well across many domains. GPT-2 zero-shots to state of the art on 7 of 8 tested LM datasets. The diversity of zero-shot tasks suggests that high-capacity models trained to maximize likelihood on a sufficiently varied corpus "begin to learn" many tasks without explicit supervision (pdf 10).

### Appendix A: Samples (pdf 13–24)
- **8.1 Model capacity (Tables 7–11, pdf 14–18).** Side-by-side completions of the smallest model and GPT-2 on random unseen WebText test articles. Contexts are 768 tokens, completions 256 tokens, top-$k$ sampling with $k=40$. They are "non-cherry-picked" (pdf 13–18).
- **8.2 Text memorization (pdf 13).** Some memorizing appears on long strings repeated many times. Conditioned on the first sentence and a half of the Gettysburg Address (about 40 occurrences in WebText), an argmax decode recovers the speech. Under sampling without truncation the model copies it for a while, then typically drifts within about 100–200 tokens. Figure 5 compares 8-gram overlap with the WebText training set for samples versus real held-out text. Most samples have under 1% overlap, over 30% have none, and the median for the real test set is 2.6%. The authors say the results suggest GPT-2 repeats training text less often than the baseline rate of held-out articles (pdf 13).
- **8.3 Diversity (Table 12, pdf 19).** Six completions of one context (384 tokens, completions 128 tokens, $k=40$) differ in content and style (pdf 19).
- **8.4 Robustness (Table 13, pdf 20).** The "talking unicorns" news article is a conditional generation on an out-of-distribution, human-written context. It is a cherry pick of 10 samples with $k=40$. The authors say the model can handle out-of-distribution contexts but sample quality is generally lower (pdf 13, 20).
- **Table 14 (pdf 21).** GPT-2 summaries next to reference summaries on CNN/Daily Mail. In the third example the GPT-2 summary is about Yemen's civil war and the Saudi-led campaign. It does not mention the family in the article (pdf 21).
- **Table 15 (pdf 22).** English↔French outputs. In the printed table, the second box's "French reference" text matches the third box's GPT-2 French translation. This may be a misprint (pdf 22).
- **Tables 16–17 (pdf 23–24).** Selected CoQA completions. For "did they climb any mountains?" the model answers "Everest" (turkers: unknown, yes, Yes, yes). For "where does she live?" it answers "Stockholm" (turkers: Sweden, Sweden, in Sweden, Sweden) (pdf 23–24).

## Toy example (ours, not from the paper)
**Idea.** The supervised loss is a subset of the unsupervised loss terms (pdf 3). Take a 4-token sequence $s_1\,s_2\,s_3\,s_4 = $ `cat`, `=`, `chat`, `.`. The token $s_3$ is the "output" and the rest is input and format. Suppose a model assigns:
- $p(s_1)=0.1$
- $p(s_2\mid s_1)=0.8$
- $p(s_3\mid s_1,s_2)=0.5$
- $p(s_4\mid s_1,s_2,s_3)=0.9$

By Eq. (1) the joint is $0.1\times0.8\times0.5\times0.9=0.036$.

**Full (unsupervised) loss**, the sum of negative natural logs:
$2.3026+0.2231+0.6931+0.1054=3.3242$.

**Supervised loss**, which uses only the output token $s_3$: $-\ln 0.5=0.6931$.

**Improving the output conditional.** Change only $p(s_3\mid s_1,s_2)$ from 0.5 to 0.9. The full loss becomes $2.3026+0.2231+0.1054+0.1054=2.7365$. The supervised term falls from 0.6931 to 0.1054. Reducing the full loss by getting the output token right also reduces the supervised loss.

**Limit of the analogy.** In this toy, the other terms are fixed. The paper's claim is about the global minimum, and it assumes a model that can reach it. The paper notes that reaching it in practice is the real question, and that learning is much slower than with explicit supervision (pdf 3).

## Concepts
- [[language model]] — a model of $p(x)=\prod p(s_n\mid s_1..s_{n-1})$ over symbol sequences, Eq. (1) (pdf 2)
- [[perplexity]] — scaled or exponentiated average negative log-probability per canonical unit; used to compare LMs on datasets (pdf 4)
- [[cross-entropy / log-loss]] — the average negative log probability per canonical prediction unit, before scaling or exponentiation; LM results are commonly reported as a scaled or exponentiated version of it (pdf 4)
- [[tokenization (BPE)]] — subword merging between word and character level; here applied to bytes with category restrictions (pdf 4)
- [[zero-shot / few-shot prompting]] — performing a task with no parameter change, using only the context; here sometimes with example pairs in the context (pdf 2, 6)
- [[pretraining / fine-tuning]] — prior paradigm: transfer then supervised adaptation; the paper aims to skip the supervised step (pdf 2)
- [[scaling law]] — here only an empirical trend: performance improves with model size (the abstract says "log-linear"), with no formula fitted in the text (pdf 1)
- [[unsupervised multitask learning]] (new) — the hypothesis that a high-capacity LM learns tasks shown in natural text as a by-product of next-token prediction (pdf 3)
- [[WebText]] (new) — 8M documents, 40 GB, from Reddit outbound links with ≥3 karma, Wikipedia removed (pdf 3)
- [[byte-level BPE]] (new) — BPE over UTF-8 bytes (base vocabulary 256) with no merges across character categories except spaces (pdf 4)
- [[top-k sampling]] (new) — sampling the next token from the k most probable ones; k=2 for summaries, k=40 for samples (pdf 6, 14)
- [[train-test overlap (8-gram)]] (new) — share of a test set's 8-grams found in training data, measured with Bloom filters (pdf 8)
- [[task as text conditioning]] (new) — specifying task, input and output as one symbol sequence, giving $p(output\mid input, task)$ (pdf 2)

## Canonical instances
- [[lambada]] — long-context last-word prediction; 8.63 perplexity, 63.24% accuracy with a stop-word filter (pdf 5)
- [[children's-book-test]] — 10-choice cloze; 93.3% common nouns, 89.1% named entities (pdf 5)
- [[winograd-schema-challenge]] — commonsense ambiguity resolution; 70.70% on 273 examples (pdf 6)
- [[coqa]] — conversational reading comprehension; 55 F1 zero-shot (pdf 6)
- [[cnn-dailymail-tldr]] — summarization induced by `TL;DR:`; R-AVG 21.40 versus 15.03 without the hint (pdf 6)
- [[wmt14-translation]] — 5 BLEU (En→Fr) and 11.5 BLEU (Fr→En) zero-shot (pdf 6–7)
- [[natural-questions]] — 4.1% exact match; 63.1% on the 1% most confident answers (pdf 7)
- [[gettysburg-address-memorization]] — verbatim recovery of a text repeated about 40 times in WebText (pdf 13)
- [[talking-unicorns-sample]] — out-of-distribution generated news article (pdf 20)

## Bridges (candidates)
- [same-math] Eq. (1) factorization ↔ probability theory: chain rule of probability — the product of conditionals is exactly the chain rule applied in sequence order.
- [structural-analogy] Train/test 8-gram overlap analysis ↔ computational social science: data leakage and contamination checks in measurement validation — both ask whether a benchmark result reflects the claimed ability or overlap with prior data.
- [structural-analogy] WebText built from Reddit links with ≥3 karma ↔ survey and sampling methodology: a convenience sample filtered by a user-behavior proxy — it shapes who and what the corpus represents.
- [metaphor] "Unsupervised multitask learner" ↔ cognitive science: learning skills incidentally from exposure rather than instruction.

## Questions this raises
- The paper reports a gain from overlap of about 0.5–1.0 F1 on CoQA and 2 perplexity on high-overlap LAMBADA examples. How would a better fuzzy-matching de-duplication change these numbers?
- Is the log-linear improvement with model size stable beyond 1.5B parameters, and does it hold for tasks such as summarization, where the curve looks flat in Figure 1?
- How would a corpus filtered by Reddit karma differ in topics and viewpoints from a random web sample, and what could that change in what the model learns?
- If GPT-2 uses heuristics such as "answer a *who* question with a name from the text" (pdf 6), how can one tell a heuristic from understanding in the other benchmarks?

## Reading notes
- **Page numbers.** Pdf 1–5 and 23–24 carry no printed page label. Pdf 6–22 have labels "printed 1–17" in the metadata, but no page numbers are visible in the page images. I therefore cite `(pdf N)` throughout; the metadata offset for pdf 6–22 is printed = pdf − 5.
- **Edition.** Title page header reads "Language Models are Unsupervised Multitask Learners", authors Radford, Wu, Child, Luan, Amodei, Sutskever, OpenAI, San Francisco. No date is printed. The references run through pdf 12 and Appendix A through pdf 24.
- **Eq. (1) as printed.** The product index is $i=1$ to $n$ but the term uses $s_n$ rather than $s_i$. I copied it as printed. The intended meaning is the usual chain-rule factorization.
- **Garbled text layer.** The Bloom-filter bound appears as "1018" in the text layer. The image shows $1/10^8$.
- **Counts of datasets.** The "7 of 8" language-modeling claim is the authors'. Table 3 has 10 columns, because LAMBADA and CBT each have two metrics. In Table 3 the 1542M model is better than the listed SOTA in 9 of 10 columns; the exception is 1BW, which the text also names as clearly worse (pdf 5).
- **Table 15.** The "French reference" in the second pair appears to repeat the GPT-2 output printed in the third box (see L3, Appendix). This may be a misprint.
- **Not covered.** The reference list (pdf 10–12) was not summarized. Figures 1–5 were read from the images; I use only values stated in the text or table, and describe the figures qualitatively.
