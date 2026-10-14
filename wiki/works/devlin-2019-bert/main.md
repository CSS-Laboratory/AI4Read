---
id: devlin-2019-bert/main
work: devlin-2019-bert
unit: paper
pages: 4171–4186 (journal pagination as printed on the page images; page labels show 1–11 and appendix 1–5)
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
# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

## L0 — One line
A Transformer encoder pre-trained to predict randomly masked tokens from both left and right context (plus next-sentence prediction) can be fine-tuned with one extra output layer to set new state-of-the-art results on eleven NLP tasks.

## L1 — The gist (≤ 120 words)
Standard language models are unidirectional (they condition on context from one side only), which the authors argue limits pre-trained representations, especially when fine-tuning for token-level tasks like question answering. This paper proposes BERT, a Transformer encoder pre-trained on unlabeled text with a masked-word objective (predict hidden tokens from both sides) plus next-sentence prediction. The same pre-trained model is then fine-tuned on each task with one extra output layer. The authors report new best results on eleven tasks (benchmarks and datasets such as GLUE, SQuAD and SWAG). Their ablations indicate that bidirectionality and the two pre-training tasks matter, and that bigger models help even on small tasks. The central claim is that one pre-trained model can serve many tasks with minimal architecture change.

**Prerequisites:** Transformer self-attention and encoder layers; softmax and cross-entropy; the idea of pre-training then fine-tuning; vectors and dot products; basic NLP metrics (accuracy, F1).

## L2 — Key ideas (5–10 bullets)
- **Unidirectionality is the targeted limitation.** Left-to-right models (GPT, a Transformer language model) and shallow concatenations of two directions (ELMo, which joins separately trained left-to-right and right-to-left LSTMs) cannot condition every layer on both sides; BERT is designed to (p. 4171–4172).
- **Masked LM makes deep bidirectional training possible.** Mask 15% of WordPiece (sub-word) tokens and predict them; ordinary conditional LMs cannot condition on both sides because a word could "see itself" (p. 4174).
- **The 80/10/10 replacement rule reduces the pre-train/fine-tune mismatch.** [MASK] never appears at fine-tuning, so chosen tokens are sometimes replaced by a random token or left unchanged (p. 4174, 4182).
- **Next sentence prediction (NSP)** is a binary IsNext/NotNext task meant to teach sentence relationships; its removal hurts QNLI, MNLI and SQuAD in the ablation (p. 4174, 4178).
- **One architecture, many tasks.** Input packs one or two segments into one sequence, using a special first token [CLS], a separator token [SEP], and segment embeddings. Each task adds only a small output layer, and all parameters are fine-tuned (p. 4173–4175).
- **Results.** New state of the art on GLUE, SQuAD v1.1, SQuAD v2.0 and SWAG (p. 4176–4177).
- **Ablations support the bidirectionality claim.** A left-to-right model with the same data and settings is worse on all tasks tested, and adding a randomly initialised BiLSTM (a bidirectional recurrent network) on top does not close the gap (p. 4178).
- **Scale helps even small tasks.** The authors report that larger models improve accuracy across all four datasets, even MRPC with 3,600 labeled examples (Table 6 shows three GLUE tasks plus LM perplexity). The authors hypothesise that fine-tuning is why this differs from earlier feature-based work (p. 4178–4179).
- **BERT also works feature-based.** On CoNLL-2003 named entity recognition (NER), concatenating the top four layers is 0.3 F1 behind full fine-tuning (p. 4179).

## L3 — Walkthrough

### Abstract and 1 Introduction (p. 4171–4172)
- **Claim of the paper.** BERT stands for Bidirectional Encoder Representations from Transformers. It pre-trains deep bidirectional representations from unlabeled text by jointly conditioning on left and right context in all layers. It is fine-tuned "with just one additional output layer" for many tasks (p. 4171).
- **Headline numbers (abstract).** GLUE score 80.5% (7.7-point absolute improvement); MultiNLI accuracy 86.7% (+4.6); SQuAD v1.1 Test F1 93.2 (+1.5); SQuAD v2.0 Test F1 83.1 (+5.1) (p. 4171).
- **Two strategies for using pre-trained representations.**
  - *Feature-based*, e.g. ELMo: task-specific architectures take the pre-trained representations as extra features.
  - *Fine-tuning*, e.g. OpenAI GPT: minimal task-specific parameters, and all pre-trained parameters are fine-tuned on the downstream task.
  - Both share the same pre-training objective, a unidirectional language model (p. 4171).
- **Stated limitation.** The authors argue current techniques restrict the power of pre-trained representations, especially for fine-tuning. Standard LMs are unidirectional, which limits the choice of architectures. In GPT every token attends only to earlier tokens. This is sub-optimal for sentence-level tasks and could be very harmful for token-level tasks such as QA, where both directions matter (p. 4171).
- **Proposal.** BERT uses a "masked language model" (MLM) objective, inspired by the Cloze task. Random input tokens are masked, and the model predicts the original vocabulary id of each masked token from context only. This lets the representation fuse left and right context, so a deep bidirectional Transformer can be pre-trained. A "next sentence prediction" task additionally pre-trains text-pair representations (p. 4171–4172).
- **Contributions as listed (p. 4172).**
  - Shows the importance of bidirectional pre-training. This contrasts with Radford et al. (2018), who use unidirectional LMs. It also contrasts with Peters et al. (2018a), who use a shallow concatenation of independently trained left-to-right and right-to-left LMs.
  - Pre-trained representations reduce the need for heavily engineered task-specific architectures. The authors claim BERT is the first fine-tuning-based model with state-of-the-art results on a large suite of sentence-level and token-level tasks.
  - New state of the art on eleven NLP tasks; code and models are released.

### 2 Related Work (p. 4172–4173)
- **2.1 Unsupervised feature-based approaches.**
  - Pre-trained word embeddings (non-neural and neural) improve over embeddings learned from scratch. They were trained with left-to-right LM objectives or objectives that discriminate correct from incorrect words in left and right context.
  - Sentence and paragraph embeddings use other objectives: ranking candidate next sentences, generating the next sentence's words, or denoising-autoencoder objectives.
  - ELMo extracts context-sensitive features from a left-to-right and a right-to-left LM. Each token's representation is the concatenation of the two. It advanced the state of the art for several benchmarks when plugged into task-specific architectures.
  - Melamud et al. (2016) predict a word from both sides with LSTMs; the authors call this feature-based and not deeply bidirectional (p. 4172).
- **2.2 Unsupervised fine-tuning approaches.**
  - Early work pre-trained only word embeddings. More recent work pre-trains sentence or document encoders that give contextual token representations and fine-tunes them. The advantage is that few parameters must be learned from scratch.
  - At least partly for this reason, OpenAI GPT reached previous state-of-the-art results on many GLUE sentence-level tasks, using left-to-right LM and auto-encoder objectives (p. 4172–4173).
- **2.3 Transfer from supervised data.** Effective transfer has been shown from large supervised tasks (natural language inference, machine translation). In computer vision, fine-tuning ImageNet-pre-trained models is an effective recipe (p. 4173).

### 3 BERT (p. 4173–4175)
**Two steps.** Pre-training: train on unlabeled data with different pre-training tasks. Fine-tuning: initialise with the pre-trained parameters, then fine-tune all parameters on labeled downstream data. Each task gets its own fine-tuned model, even though all start from the same pre-trained parameters. There is minimal difference between pre-trained and final downstream architecture (p. 4173, Figure 1).

**Model architecture.**
- A multi-layer bidirectional Transformer encoder, almost identical to the original implementation of Vaswani et al. (2017) (p. 4173).
- Notation: $L$ = number of layers (Transformer blocks), $H$ = hidden size, $A$ = number of self-attention heads. The feed-forward/filter size is always $4H$ (3072 for $H=768$, 4096 for $H=1024$) (p. 4173, footnote 3).
- Two sizes (p. 4173):

| Model | L | H | A | Parameters |
|---|---|---|---|---|
| BERT_BASE | 12 | 768 | 12 | 110M |
| BERT_LARGE | 24 | 1024 | 16 | 340M |

- BERT_BASE has the same size as OpenAI GPT for comparison. The critical difference is that BERT uses bidirectional self-attention, while GPT uses constrained self-attention where each token attends only to its left (p. 4173).
- Footnote 4: the literature often calls the bidirectional Transformer a "Transformer encoder" and the left-context-only version a "Transformer decoder", since it can generate text (p. 4173–4174).

**Input/output representations (p. 4174).**
- A "sentence" is any contiguous span of text. A "sequence" is the token sequence input to BERT, one sentence or two packed together.
- WordPiece embeddings with a 30,000-token vocabulary.
- The first token of every sequence is always [CLS]. Its final hidden state is the aggregate sequence representation for classification.
- Sentence pairs are packed into one sequence and distinguished in two ways: a [SEP] token between them, and a learned embedding added to every token marking sentence A or B.
- Notation: input embedding $E$; final hidden vector of [CLS] is $C\in\mathbb{R}^H$; final hidden vector of the $i$-th input token is $T_i\in\mathbb{R}^H$.
- A token's input representation is the **sum** of its token, segment and position embeddings (Figure 2, p. 4175). Figure 2 example: [CLS] my dog is cute [SEP] he likes play ##ing [SEP], with segment embeddings $E_A$ for the first six tokens and $E_B$ for the rest, and position embeddings $E_0,\dots,E_{10}$.

#### 3.1 Pre-training BERT (p. 4174–4175)
Pre-training does not use left-to-right or right-to-left LMs. It uses two unsupervised tasks.

**Task #1: Masked LM.**
- Authors' intuition: it is reasonable to believe that a deep bidirectional model is strictly more powerful than a left-to-right model or a shallow concatenation of the two. But standard conditional LMs can only be trained in one direction, because bidirectional conditioning would let each word indirectly "see itself" and trivially predict the target in a multi-layer model (p. 4174).
- Fix: mask some percentage of input tokens at random and predict them. The final hidden vectors at the masked positions are fed to an output softmax over the vocabulary, as in a standard LM.
- In all experiments, 15% of all WordPiece tokens in each sequence are masked at random. Unlike denoising auto-encoders, only the masked words are predicted, not the whole input (p. 4174).
- **Mismatch problem.** [MASK] does not appear during fine-tuning. Mitigation: the data generator chooses 15% of token positions. If the $i$-th token is chosen, it is replaced by (1) [MASK] 80% of the time, (2) a random token 10% of the time, (3) the unchanged token 10% of the time. Then $T_i$ predicts the original token with cross-entropy loss (p. 4174).
- Appendix A.1 example, sentence `my dog is hairy` with 4th token chosen: 80% → `my dog is [MASK]`; 10% → `my dog is apple`; 10% → `my dog is hairy`. Keeping the word unchanged is meant to bias the representation toward the actually observed word (p. 4182).
- Appendix rationale: the encoder does not know which words it must predict or which were replaced by random words, so it must keep a distributional contextual representation of every input token. Random replacement affects only 1.5% of tokens (10% of 15%), which, the authors say, does not seem to harm language understanding (p. 4182).
- Appendix cost: MLM predicts only 15% of tokens per batch, which suggests more pre-training steps may be needed (p. 4182–4183).

*Intuition note.* Hiding a word and asking for it from both sides gives bidirectional context without letting the model copy the answer. The random and unchanged cases force the model to keep good representations of tokens that look normal, because it cannot tell which ones it will be graded on.

**Task #2: Next Sentence Prediction (NSP).**
- Many tasks (QA, NLI) rest on the relationship between two sentences, which language modeling does not directly capture. So BERT is pre-trained on a binarised next-sentence task generated from any monolingual corpus (p. 4174).
- For each example with sentences A and B: 50% of the time B is the actual next sentence (label IsNext); 50% of the time B is a random sentence from the corpus (NotNext). $C$ is used for this prediction (p. 4174).
- The final model reaches 97%–98% accuracy on NSP (footnote 5). $C$ is not a meaningful sentence representation without fine-tuning, since it was trained with NSP (footnote 6) (p. 4174).
- Appendix A.1 examples: `[CLS] the man went to [MASK] store [SEP] he bought a gallon [MASK] milk [SEP]` is IsNext. `[CLS] the man [MASK] to the store [SEP] penguin [MASK] are flight ##less birds [SEP]` is NotNext (p. 4183).
- Related to objectives of Jernite et al. (2017) and Logeswaran and Lee (2018). In that prior work only sentence embeddings are transferred downstream; BERT transfers all parameters to initialise the end-task model (p. 4175).

**Pre-training data.** BooksCorpus (800M words) and English Wikipedia (2,500M words; text passages only, ignoring lists, tables, headers). The authors say it is critical to use a document-level corpus rather than a shuffled sentence-level corpus such as the Billion Word Benchmark, in order to extract long contiguous sequences (p. 4175).

#### 3.2 Fine-tuning BERT (p. 4175)
- Self-attention lets BERT model many tasks, single text or text pairs, by swapping inputs and outputs. Earlier text-pair models often encode the two texts independently and then apply bidirectional cross attention. BERT instead encodes the concatenated pair with self-attention, which effectively includes bidirectional cross attention between the two sentences (p. 4175).
- For each task, plug in the task inputs and outputs and fine-tune all parameters end-to-end. Sentence A/B from pre-training correspond to: (1) sentence pairs in paraphrasing, (2) hypothesis–premise pairs in entailment, (3) question–passage pairs in QA, (4) a degenerate text–∅ pair in classification or tagging (p. 4175).
- Outputs: token representations go to an output layer for token-level tasks (tagging, QA). The [CLS] representation goes to an output layer for classification (p. 4175).
- Fine-tuning is relatively inexpensive: all paper results replicate in at most 1 hour on a single Cloud TPU, or a few hours on a GPU, from the same pre-trained model. Example: the SQuAD model trains in about 30 minutes on one Cloud TPU, Dev F1 91.0% (p. 4175, footnote 7).

*Intuition note.* Because pre-training already used the same input format (one or two segments with [CLS]/[SEP]), a downstream task only needs a way to read an answer off $C$ or the $T_i$. This is consistent with the authors' statement that each task needs only one additional output layer (p. 4175, 4185).

### 4 Experiments (p. 4175–4177)

#### 4.1 GLUE (p. 4175–4176)
- GLUE is a collection of diverse natural-language-understanding tasks (descriptions in Appendix B.1).
- Input is represented as in Section 3, with $C\in\mathbb{R}^H$ as aggregate representation. The only new parameters are classification weights $W\in\mathbb{R}^{K\times H}$, with $K$ the number of labels. The loss is the standard classification loss: $\log(\mathrm{softmax}(CW^T))$ (p. 4175). (added step) Shapes: $C$ is $1\times H$, $W^T$ is $H\times K$, so $CW^T$ is $1\times K$, one score per label.
- Settings: batch size 32, 3 epochs for all GLUE tasks. The learning rate was chosen per task on the Dev set from 5e-5, 4e-5, 3e-5, 2e-5. For BERT_LARGE, fine-tuning was sometimes unstable on small datasets, so several random restarts were run and the best Dev model chosen. Restarts share the pre-trained checkpoint but differ in fine-tuning data shuffling and classifier-layer initialisation (p. 4176).
- Only a single GLUE test submission was made for each of BERT_BASE and BERT_LARGE (footnote 9) (p. 4176).

Table 1 (GLUE Test; $F_1$ for QQP and MRPC, Spearman for STS-B, accuracy otherwise; "Average" excludes WNLI) (p. 4176):

| System | MNLI-m/mm | QQP | QNLI | SST-2 | CoLA | STS-B | MRPC | RTE | Avg |
|---|---|---|---|---|---|---|---|---|---|
| Pre-OpenAI SOTA | 80.6/80.1 | 66.1 | 82.3 | 93.2 | 35.0 | 81.0 | 86.0 | 61.7 | 74.0 |
| BiLSTM+ELMo+Attn | 76.4/76.1 | 64.8 | 79.8 | 90.4 | 36.0 | 73.3 | 84.9 | 56.8 | 71.0 |
| OpenAI GPT | 82.1/81.4 | 70.3 | 87.4 | 91.3 | 45.4 | 80.0 | 82.3 | 56.0 | 75.1 |
| BERT_BASE | 84.6/83.4 | 71.2 | 90.5 | 93.5 | 52.1 | 85.8 | 88.9 | 66.4 | 79.6 |
| BERT_LARGE | 86.7/85.9 | 72.1 | 92.7 | 94.9 | 60.5 | 86.5 | 89.3 | 70.1 | 82.1 |

- Training set sizes: MNLI 392k, QQP 363k, QNLI 108k, SST-2 67k, CoLA 8.5k, STS-B 5.7k, MRPC 3.5k, RTE 2.5k (p. 4176).
- Authors' reading: both sizes outperform all systems on all tasks by a substantial margin, with 4.5% and 7.0% average improvement over the prior state of the art. BERT_BASE and GPT are nearly identical in architecture apart from attention masking. On MNLI the gain is 4.6% absolute. On the official leaderboard BERT_LARGE scores 80.5 versus 72.8 for GPT as of the date of writing (p. 4176).
- BERT_LARGE significantly outperforms BERT_BASE across all tasks, especially those with very little training data. Model size is explored in Section 5.2 (p. 4176).

#### 4.2 SQuAD v1.1 (p. 4176–4177)
- Task: 100k crowd-sourced question/answer pairs. Given a question and a Wikipedia passage containing the answer, predict the answer span.
- Question uses the A embedding, passage the B embedding, packed into one sequence. New parameters: a start vector $S\in\mathbb{R}^H$ and an end vector $E\in\mathbb{R}^H$ (p. 4176).
- Probability that word $i$ starts the answer span:
$$P_i=\frac{e^{S\cdot T_i}}{\sum_j e^{S\cdot T_j}}$$
The end probability uses the analogous formula with $E$. The sum runs over all words in the paragraph (p. 4176).
- Span score for positions $i$ to $j$: $S\cdot T_i+E\cdot T_j$. The prediction is the maximum-scoring span with $j\ge i$. The training objective is the sum of the log-likelihoods of the correct start and end positions. Fine-tuned 3 epochs, learning rate 5e-5, batch size 32 (p. 4176).
- The top SQuAD leaderboard entries have no up-to-date public descriptions and may use any public data. So the authors use modest data augmentation: first fine-tune on TriviaQA, then on SQuAD (p. 4176; footnote 12 describes the TriviaQA data, p. 4177).

Table 2 highlights (p. 4177):

| System | Dev EM/F1 | Test EM/F1 |
|---|---|---|
| Human | – | 82.3 / 91.2 |
| #1 Ensemble – nlnet (Dec 10th, 2018) | – | 86.0 / 91.7 |
| #2 Ensemble – QANet | – | 84.5 / 90.5 |
| BERT_LARGE (Single) | 84.1 / 90.9 | – |
| BERT_LARGE (Sgl.+TriviaQA) | 84.2 / 91.1 | 85.1 / 91.8 |
| BERT_LARGE (Ens.+TriviaQA) | 86.2 / 92.2 | 87.4 / 93.2 |

- BERT_BASE (Single) Dev: 80.8 EM / 88.5 F1. The BERT ensemble is 7 systems with different pre-training checkpoints and fine-tuning seeds (p. 4177).
- The best system beats the top leaderboard system by +1.5 F1 as an ensemble and +1.3 F1 as a single system. The single BERT model outperforms the top ensemble system in F1. Without TriviaQA data, the system loses only 0.1–0.4 F1 and still outperforms all existing systems by a wide margin (p. 4176–4177).

#### 4.3 SQuAD v2.0 (p. 4177)
- SQuAD 2.0 allows that no short answer exists in the paragraph.
- Method: questions without an answer are treated as having an answer span that starts and ends at [CLS]. The start/end probability space is extended to include the [CLS] position (p. 4177).
- No-answer score: $s_{\text{null}}=S\cdot C+E\cdot C$. Best non-null span score: $\hat{s}_{i,j}=\max_{j\ge i} S\cdot T_i+E\cdot T_j$. Predict a non-null answer when $\hat{s}_{i,j}>s_{\text{null}}+\tau$. The threshold $\tau$ is selected on the dev set to maximise F1 (p. 4177).
- No TriviaQA data. Fine-tuned 2 epochs, learning rate 5e-5, batch size 48 (p. 4177).
- Table 3, excluding systems that use BERT: BERT_LARGE (Single) Test 80.0 EM / 83.1 F1 (Dev 78.7/81.9). The #1 single system MIR-MRC (F-Net) has 74.8/78.0 and #2 nlnet 74.2/77.1. Human: 86.9/89.5. The authors report a +5.1 F1 improvement over the previous best system (p. 4177).

#### 4.4 SWAG (p. 4177)
- 113k sentence-pair completion examples evaluating grounded commonsense inference. Given a sentence, choose the most plausible continuation among four.
- Four input sequences are built, each the given sentence (A) plus one candidate continuation (B). The only new parameter is a vector whose dot product with $C$ gives a score for each choice. The four scores go through a softmax. Fine-tuned 3 epochs, learning rate 2e-5, batch 16 (p. 4177).
- Table 4: BERT_LARGE Dev 86.6, Test 86.3. BERT_BASE Dev 81.6. OpenAI GPT Test 78.0. ESIM+ELMo Dev 59.1, Test 59.2. ESIM+GloVe 51.9/52.7. Human (expert) 85.0; human (5 annotations) 88.0, measured on 100 samples (p. 4177).
- BERT_LARGE outperforms the authors' baseline ESIM+ELMo by +27.1% and OpenAI GPT by 8.3% (p. 4177).

*Intuition note.* Across sentence-pair classification, span extraction, and multiple choice, only a tiny head differs: a matrix $W$, two vectors $S,E$, or one scoring vector. The authors attribute the majority of BERT's improvement over GPT to the two pre-training tasks and the bidirectionality they enable (p. 4184), not to the task-specific heads.

### 5 Ablation Studies (p. 4177–4179)

#### 5.1 Effect of pre-training tasks (p. 4178)
Two variants, all using exactly the same pre-training data, fine-tuning scheme and hyperparameters as BERT_BASE:
- **No NSP:** bidirectional, trained with MLM but without NSP.
- **LTR & No NSP:** a standard left-to-right LM instead of MLM, also without NSP. The left-only constraint was also applied at fine-tuning, because removing it produced a pre-train/fine-tune mismatch that degraded downstream performance. This is directly comparable to OpenAI GPT but with BERT's larger dataset, input representation and fine-tuning scheme.

Table 5 (Dev set; MNLI-m/QNLI/MRPC/SST-2 accuracy, SQuAD F1) (p. 4178):

| | MNLI-m | QNLI | MRPC | SST-2 | SQuAD |
|---|---|---|---|---|---|
| BERT_BASE | 84.4 | 88.4 | 86.7 | 92.7 | 88.5 |
| No NSP | 83.9 | 84.9 | 86.5 | 92.6 | 87.9 |
| LTR & No NSP | 82.1 | 84.3 | 77.5 | 92.1 | 77.8 |
| + BiLSTM | 82.1 | 84.1 | 75.7 | 91.6 | 84.9 |

- Removing NSP hurts performance significantly on QNLI, MNLI and SQuAD 1.1. The LTR model is worse than the MLM model ("No NSP") on all tasks, with large drops on MRPC and SQuAD (p. 4178).
- For SQuAD, the authors say it is intuitively clear that an LTR model does poorly at token predictions because token-level hidden states have no right-side context. To strengthen the LTR system they added a randomly initialised BiLSTM on top. This improves SQuAD significantly, but results are still far worse than the pre-trained bidirectional models. The BiLSTM hurts performance on GLUE tasks (p. 4178).
- **Authors' comparison with ELMo-style concatenation.** Separate LTR and RTL models could be concatenated as ELMo does. But: (a) twice as expensive as one bidirectional model; (b) non-intuitive for QA, since the RTL model could not condition the answer on the question; (c) strictly less powerful than a deep bidirectional model, which uses both contexts at every layer (p. 4178).

*Intuition note.* The comparison "No NSP" vs "LTR & No NSP" compares bidirectional MLM training with left-to-right training, with NSP absent in both. The drop on SQuAD (87.9 for No NSP → 77.8 for the fully LTR model) fits the authors' view that token-level tasks need right context. A BiLSTM on top recovers part of it (84.9) but not all.

#### 5.2 Effect of model size (p. 4178–4179)
- Several BERT models with different layers, hidden units and heads were trained with otherwise the same hyperparameters. Dev accuracies are averages from 5 random restarts of fine-tuning (p. 4178).

Table 6 (p. 4179):

| #L | #H | #A | LM ppl | MNLI-m | MRPC | SST-2 |
|---|---|---|---|---|---|---|
| 3 | 768 | 12 | 5.84 | 77.9 | 79.8 | 88.4 |
| 6 | 768 | 3 | 5.24 | 80.6 | 82.2 | 90.7 |
| 6 | 768 | 12 | 4.68 | 81.9 | 84.8 | 91.3 |
| 12 | 768 | 12 | 3.99 | 84.4 | 86.7 | 92.9 |
| 12 | 1024 | 16 | 3.54 | 85.7 | 86.9 | 93.3 |
| 24 | 1024 | 16 | 3.23 | 86.6 | 87.8 | 93.7 |

- "LM (ppl)" is the masked-LM perplexity on held-out training data. The authors say larger models give a strict accuracy improvement across all four datasets, even MRPC (3,600 labeled examples, a task the authors describe as substantially different from the pre-training tasks) (p. 4178).
- Context for scale: the largest Transformer in Vaswani et al. is (L=6, H=1024, A=16) with 100M encoder parameters. The largest the authors found in the literature is (L=64, H=512, A=2) with 235M (Al-Rfou et al.). BERT_BASE has 110M and BERT_LARGE 340M parameters (p. 4178).
- Improvements on large-scale tasks like machine translation and language modeling from more parameters were already known. The authors "believe" this is the first work to show convincingly that extreme scaling also gives large improvements on very small tasks, provided the model is sufficiently pre-trained (p. 4178).
- Prior mixed results: Peters et al. (2018b) on going from two to four bi-LM layers; Melamud et al. mentioned in passing that hidden size 200→600 helped but 1,000 did not. Both used a feature-based approach. **The authors hypothesise** that when the model is fine-tuned directly and uses only a very small number of randomly initialised extra parameters, task models can benefit from larger, more expressive representations even when downstream data is very small (p. 4178–4179).

#### 5.3 Feature-based approach with BERT (p. 4179)
- Advantages of feature-based use: (1) not all tasks can easily be represented by a Transformer encoder, so some need a task-specific architecture; (2) there are computational benefits to pre-computing an expensive representation once and running many cheaper experiments on top (p. 4179).
- Test case: CoNLL-2003 NER. Case-preserving WordPiece model; maximal document context from the data; formulated as tagging with no CRF layer. The first sub-token's representation feeds the token-level classifier over the NER labels (p. 4179).
- Feature-based version: extract activations from one or more layers without fine-tuning any BERT parameters. These feed a randomly initialised two-layer 768-dimensional BiLSTM before the classification layer (p. 4179).

Table 7 (Dev F1 / Test F1; scores averaged over 5 random restarts) (p. 4179):

| System | Dev | Test |
|---|---|---|
| ELMo | 95.7 | 92.2 |
| CVT | – | 92.6 |
| CSE | – | 93.1 |
| BERT_LARGE (fine-tuning) | 96.6 | 92.8 |
| BERT_BASE (fine-tuning) | 96.4 | 92.4 |
| Feature-based (BERT_BASE): Embeddings | 91.0 | – |
| Second-to-last hidden | 95.6 | – |
| Last hidden | 94.9 | – |
| Weighted sum last four hidden | 95.9 | – |
| Concat last four hidden | 96.1 | – |
| Weighted sum all 12 layers | 95.5 | – |

- The best feature-based method (concatenating the top four hidden layers) is 0.3 F1 behind fine-tuning the entire model (96.4 vs 96.1 Dev for BERT_BASE). The authors conclude BERT is effective for both approaches (p. 4179).

### 6 Conclusion (p. 4179)
Rich unsupervised pre-training is an integral part of many language understanding systems and lets even low-resource tasks benefit from deep unidirectional architectures. The authors' major contribution is generalising this to deep bidirectional architectures, so one pre-trained model can tackle a broad set of NLP tasks (p. 4179).

### Appendix A: Additional details for BERT (p. 4182–4185)
- **A.1** gives the masking and NSP examples summarised above (p. 4182–4183).
- **A.2 Pre-training procedure (p. 4183).**
  - Two text spans ("sentences", typically much longer than a sentence) are sampled with combined length ≤ 512 tokens. The first gets embedding A and the second B; 50% of the time B is the true next span.
  - Masking is applied after WordPiece tokenisation with a uniform 15% rate and no special treatment of partial word pieces.
  - Batch of 256 sequences (256 × 512 = 128,000 tokens/batch) for 1,000,000 steps, about 40 epochs over the 3.3-billion-word corpus.
  - Adam, learning rate 1e-4, $\beta_1=0.9$, $\beta_2=0.999$, L2 weight decay 0.01, warmup over the first 10,000 steps, then linear decay. Dropout 0.1 on all layers. GELU activation instead of ReLU, following GPT.
  - Training loss = sum of the mean masked-LM likelihood and the mean NSP likelihood.
  - BERT_BASE trained on 4 Cloud TPUs (16 chips); BERT_LARGE on 16 Cloud TPUs (64 chips); each took 4 days.
  - Attention cost is quadratic in sequence length, so the model is pre-trained with length 128 for 90% of the steps, then length 512 for the remaining 10% to learn the positional embeddings.
- **A.3 Fine-tuning (p. 4183–4184).** Most hyperparameters match pre-training except batch size, learning rate, epochs. Dropout always 0.1. Values that worked across tasks: batch size 16 or 32; Adam learning rate 5e-5, 3e-5, 2e-5; epochs 2, 3, 4. Large datasets (100k+ labeled examples) were far less sensitive to hyperparameters. Since fine-tuning is fast, the authors suggest an exhaustive search over these values, picking the best Dev model (p. 4184).
- **A.4 BERT vs ELMo vs GPT (p. 4184, Figure 3 p. 4183).** BERT uses a bidirectional Transformer, GPT a left-to-right Transformer, ELMo concatenated independently trained left-to-right and right-to-left LSTMs. Only BERT is jointly conditioned on both sides in all layers. BERT and GPT are fine-tuning approaches, ELMo is feature-based. BERT was intentionally made close to GPT for comparison. The core argument is that bidirectionality and the two pre-training tasks account for the majority of the improvements. The authors also list other differences:
  - GPT: BooksCorpus only (800M words); BERT adds Wikipedia (2,500M).
  - GPT introduces [SEP] and [CLS] only at fine-tuning; BERT learns [SEP], [CLS] and A/B embeddings during pre-training.
  - GPT: 1M steps, batch of 32,000 words; BERT: 1M steps, batch of 128,000 words.
  - GPT uses learning rate 5e-5 for all fine-tuning; BERT chooses the best learning rate per task on the Dev set.
  - The Section 5.1 ablations are said to show that the majority of the improvements come from the two pre-training tasks and the bidirectionality they enable (p. 4184).
- **A.5 Fine-tuning illustrations (Figure 4, p. 4185).** (a) sentence-pair classification: MNLI, QQP, QNLI, STS-B, MRPC, RTE, SWAG; (b) single-sentence classification: SST-2, CoLA; (c) QA: SQuAD v1.1; (d) single-sentence tagging: CoNLL-2003 NER. (a),(b) are sequence-level tasks; (c),(d) token-level. Each adds one output layer (p. 4184–4185).

### Appendix B: GLUE datasets (B.1, p. 4184–4185)
- MNLI: crowdsourced entailment; predict entailment, contradiction or neutral.
- QQP: binary; are two Quora questions semantically equivalent.
- QNLI: SQuAD converted to binary: does the sentence contain the answer.
- SST-2: binary sentiment of movie-review sentences.
- CoLA: is an English sentence linguistically "acceptable".
- STS-B: similarity score 1 to 5.
- MRPC: paraphrase detection from online news.
- RTE: binary entailment, much less training data than MNLI.
- WNLI: small NLI set. The GLUE page notes problems with its construction, and every submitted trained system performed worse than the 65.1 majority-class baseline. The authors therefore exclude it, saying this is to be fair to OpenAI GPT, and for their GLUE submission always predicted the majority class.
- Footnote 14: only single-task fine-tuning is reported. Multitask fine-tuning could potentially push performance further; they saw substantial RTE improvements from multitask training with MNLI (p. 4185).

### Appendix C: Additional ablations (p. 4186)
- **C.1 Number of training steps (Figure 5).**
  - Question 1: Does BERT need so much pre-training (128,000 words/batch × 1,000,000 steps)? Answer: yes; BERT_BASE gets almost 1.0% additional MNLI accuracy at 1M steps compared with 500k steps.
  - Question 2: Does MLM converge slower than LTR since only 15% of tokens are predicted? Answer: slightly slower, but in absolute accuracy MLM begins to outperform LTR almost immediately (p. 4186).
- **C.2 Masking procedures (Table 8).** [MASK] = replace with the [MASK] symbol; SAME = keep the token; RND = replace with a random token. Reported to reduce the mismatch between pre-training and fine-tuning. NER is reported in both fine-tuning and feature-based modes, because the authors expect the mismatch to be amplified for the feature-based approach, which cannot adjust representations. The feature-based mode concatenates the last 4 layers (p. 4186).

| MASK / SAME / RND | MNLI fine-tune | NER fine-tune | NER feature-based |
|---|---|---|---|
| 80 / 10 / 10 | 84.2 | 95.4 | 94.9 |
| 100 / 0 / 0 | 84.3 | 94.9 | 94.0 |
| 80 / 0 / 20 | 84.1 | 95.2 | 94.6 |
| 80 / 20 / 0 | 84.4 | 95.2 | 94.7 |
| 0 / 20 / 80 | 83.7 | 94.8 | 94.6 |
| 0 / 0 / 100 | 83.6 | 94.9 | 94.6 |

  Authors' reading: fine-tuning is "surprisingly robust" to masking strategy. As expected, using only MASK was problematic for the feature-based NER approach. Using only RND performs much worse than their strategy (p. 4186).

## Toy example (ours, not from the text)
**Masking arithmetic for the 80/10/10 rule.** Take a batch with 1,000 WordPiece tokens.
1. Chosen for prediction: $0.15\times1000=150$ tokens. The other 850 are fed in unchanged and contribute no MLM loss.
2. Of the 150 chosen: $0.8\times150=120$ become [MASK]; $0.1\times150=15$ become a random token; $0.1\times150=15$ stay as they are.
3. The loss is computed at all 150 positions, including the 15 whose input token is already correct and the 15 whose input token is wrong. The model cannot tell which positions are scored.
4. The fraction of all tokens corrupted by a random replacement is $15/1000=1.5\%$, which matches the author's "10% of 15%" statement (p. 4182).
5. Fraction of all tokens that show [MASK]: $120/1000=12\%$. So at fine-tuning, where no token is [MASK], the input looks different from what the model usually saw at pre-training.
6. An LM that predicts every token would score 1,000 positions; MLM scores 150. This is why the authors expect slower convergence (p. 4182–4183).

## Concepts
- [[masked language modeling]] — randomly mask 15% of WordPiece tokens and predict them from both sides; only masked positions are predicted (p. 4174)
- [[pretraining / fine-tuning]] — unsupervised pre-training, then all parameters are fine-tuned per task with a small output layer (p. 4173)
- [[encoder-only / decoder-only]] — BERT is a bidirectional Transformer "encoder"; the left-context-only version is called a "decoder" (p. 4173–4174, footnote 4)
- [[causal masking]] — GPT's constrained self-attention, where each token attends only to its left; BERT lacks it (p. 4173)
- [[self-attention]] — used to encode a concatenated text pair, effectively including bidirectional cross attention between the sentences (p. 4175)
- [[positional encoding]] — here, learned position embeddings summed into the input; longer 512-length training teaches them (p. 4174, 4183)
- [[softmax]] — used over the vocabulary at masked positions, over labels from $C$, over start/end positions, and over SWAG choices (p. 4174–4177)
- [[cross-entropy / log-loss]] — loss at the masked positions and for classification (p. 4174–4175)
- [[perplexity]] — masked-LM perplexity on held-out training data is reported for each model size (p. 4179)
- [[tokenization (BPE)]] — related only: BERT uses WordPiece with a 30,000-token vocabulary; the paper does not describe its algorithm (p. 4174)
- [[next-sentence-prediction]] (new) — binary IsNext/NotNext pre-training task, 50% random B, predicted from $C$ (p. 4174)
- [[cls-token-and-segment-embeddings]] (new) — [CLS] first token whose final state $C$ is the sequence representation; [SEP] and A/B embeddings mark sentence pairs (p. 4174)
- [[feature-based vs fine-tuning]] (new) — feature-based: fixed pre-trained features in task architectures; fine-tuning: all parameters updated (p. 4171, 4179)
- [[deep bidirectionality]] (new) — conditioning on both left and right context in all layers, versus shallow concatenation of two unidirectional models (p. 4172, 4178)
- [[ablation study]] (new) — removing or varying one component under otherwise identical conditions to measure its effect (p. 4178)

## Canonical instances
- [[bert-base-and-large]] — the two main model sizes (110M and 340M parameters) on which results are primarily reported; Table 6 also varies size (p. 4173, 4179)
- [[openai-gpt-comparison]] — BERT_BASE built to match GPT size; the LTR ablation approximates GPT under BERT's data and settings (p. 4173, 4178)
- [[elmo-comparison]] — feature-based, concatenation of independent LTR and RTL LSTMs (p. 4172, 4184)
- [[glue-benchmark]] — collection of nine datasets in B.1; Table 1 reports eight, with WNLI excluded from the average; BERT_LARGE average 82.1 (p. 4176, 4184–4185)
- [[squad-v1-v2]] — span-extraction QA, with a [CLS]-span null answer for v2.0 (p. 4176–4177)
- [[swag]] — four-way commonsense continuation task; BERT_LARGE 86.3 Test (p. 4177)
- [[conll-2003-ner]] — token-level tagging used for the feature-based comparison (p. 4179)

## Bridges (candidates)
- [structural-analogy] Masked LM ↔ education/psychology: the Cloze procedure (the paper cites Taylor, 1953, for the Cloze task, p. 4171) — fill in a blank from surrounding words.
- [structural-analogy] Fine-tuning a pre-trained BERT ↔ computer vision: fine-tuning ImageNet-pre-trained models (cited p. 4173) — reuse general pre-trained features, adapt with labeled data.
- [structural-analogy] Feature-based use of BERT layers (Section 5.3) ↔ text-as-data in social science: fixed text embeddings as inputs to a smaller downstream model — pre-compute representations once, then fit cheaper models.
- [metaphor] "Seeing itself" in bidirectional conditioning ↔ target leakage in supervised learning — the model gets the answer through its input.
- [structural-analogy] MLM vs denoising autoencoder ↔ the paper contrasts them (p. 4174): both corrupt input, but MLM predicts only the corrupted tokens.

## Questions this raises
- The authors say bidirectionality and the two pre-training tasks account for "the majority" of the gain, but BERT also uses more data and bigger batches than GPT (p. 4184). How could one separate these factors more cleanly?
- NSP helps in Table 5, but the paper only compares "with" and "without" it. Would other sentence-level objectives do as well or better?
- The authors hypothesise that fine-tuning, not feature extraction, is why larger models help small tasks (p. 4178–4179). What experiment would test this directly?
- Given that MLM scores only 15% of tokens per pass, can a pre-training objective use the data more efficiently without the [MASK] mismatch?

## Reading notes
- **Page numbers.** Page labels give "printed" numbers 1–11 for the paper body and references, and 1–5 for the appendix pages; these collide. The page images show journal numbers 4171–4186. The reference list is on pp. 4180–4182.
- The unit metadata said "printed pages 1–5"; the actual unit contains the body (4171–4179), the references, and the appendix (4182–4186).
- **Misprints visible in the images.** "befor fine-tuning" (p. 4176); "pretraing" (A.2); "langauge" (A.1); "this it is strictly less powerful" (p. 4178); "The right part of the paper represents the Dev set results" (p. 4186, "table" intended); a space in "ELMo ,and" (A.4 heading).
- **Small inconsistencies.** Section 5.2 says MRPC has "3,600" labeled examples, Table 1 says 3.5k. The abstract's GLUE score of 80.5 is the official leaderboard score (p. 4176). Table 1's "Average" of 82.1 for BERT_LARGE excludes WNLI and differs from the official score. BERT_BASE Dev values in Table 5 (SST-2 92.7) differ slightly from the 12/768/12 row of Table 6 (SST-2 92.9); Table 6 states its numbers are averages over 5 restarts, and Table 5's caption does not say.
- Tables and figures were checked against the page images. Figure 5 is a plot; only the C.1 text answers were used. Section 5.2 says 'all four datasets', but Table 6 shows only three GLUE tasks (MNLI-m, MRPC, SST-2) plus LM perplexity.
- Footnote 3 and the relation "feed-forward size = 4H" are stated for all cases. The source does not give shapes for $T$ beyond $T_i\in\mathbb{R}^H$; the shape remarks marked "(added step)" are ours.
- Claims of "first" (first fine-tuning-based model with SOTA on a large suite; first to show scaling helps very small tasks) are the authors' own statements, kept as theirs.
