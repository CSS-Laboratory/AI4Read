---
id: ziems-2024-css/main-p1
work: ziems-2024-css
unit: paper (part 1/2) — Sections 1–5 and the start of Section 6
pages: 237–264
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
# Can Large Language Models Transform Computational Social Science? (part 1)

## L0 — One line
Zero-shot prompted large language models (LLMs) usually do not beat fine-tuned classifiers on social-science text labelling, but on about half the tasks they agree with gold labels moderately well, so they may help human annotation teams.

## L1 — The gist (≤ 120 words)
The paper asks whether prompted large language models can serve as tools for computational social science (CSS: computational analysis of behavioural and linguistic data). The authors survey CSS needs and pick 20 classification tasks and 5 generation tasks in English. They write prompts, then test zero-shot models from the FLAN-T5 and OpenAI families against fine-tuned baselines. Part 1 covers the design and the classification results. LLMs rarely beat the fine-tuned classifiers. On about half of the tasks they reach moderate-to-good agreement (κ, an agreement score) with gold labels. In the OpenAI family, instruction tuning, code pretraining and RLHF help more than raw size. Performance seems tied more to input complexity than to academic field.

**Prerequisites:** zero-shot prompting (the task is given by instructions only, no training examples); fine-tuning (further training a model on labelled examples); instruction tuning (training a model to follow human-written instructions); RLHF (reinforcement learning from human feedback); precision/recall/F1; inter-annotator agreement (κ, a score for how far two sets of labels agree); FLAN-T5 and GPT-3/4 (the open and OpenAI model families tested); the idea of a scaling plot (performance versus model size).

## L2 — Key ideas (5–10 bullets)
- The authors ask four questions: viability (RQ1), model selection (RQ2), domain utility (RQ3), functionality of classification versus generation (RQ4) (p. 239).
- The benchmark has 10 utterance-level, 6 conversation-level and 4 document-level classification tasks, plus 5 generation tasks, chosen from a survey of six fields (pp. 243, 252).
- Prompts follow written guidelines: multiple-choice options, instructions after the context, an explicit constraint for uncertainty, JSON output. Results are averaged over prompt paraphrases, with temperature 0 (pp. 254–255).
- LLMs rarely exceed the fine-tuned RoBERTa baseline. In 8 of 17 tasks with a κ score they reach κ = 0.40–0.65, and in 5 of 17 agreement is poor (pp. 257–259).
- Error analysis suggests that on easy-to-define labels some "errors" are gold mislabels. On expert taxonomies models default to generic labels, such as "stereotype" (pp. 259–261).
- Few-shot prompting (3 or 5 examples) gives spotty gains on FLAN models (p. 261).
- FLAN gains roughly 5 F1 points per ten-fold size increase. OpenAI gains come more from instruction tuning, code pretraining and RLHF than from size (pp. 261–263).
- Performance overlaps across academic fields. The authors suggest it may track input and label complexity; the text says document-level tasks are hardest, though Table 3 only partly fits this (pp. 263–264).

## L3 — Walkthrough

### Abstract and 1. Introduction (pp. 238–240)
- **Claim of the paper.** Zero-shot LLMs may augment CSS in two ways: as zero-shot annotators on human teams, and for bootstrapping creative generation tasks such as explaining text attributes (p. 238).
- **Problem.** Supervised CSS methods need much human-annotated data, while unsupervised ones can be uninterpretable. Data resources therefore limit which theories CSS can address. Zero-shot viability is the primary research question (p. 238).
- **Research questions (RQ1–RQ4).**
  - RQ1: can LLMs augment annotation, matching or exceeding human reliability?
  - RQ2: how do model size and pretraining affect performance?
  - RQ3: are LLMs better in some fields than others?
  - RQ4: are they better at labelling (classification) or at explaining (generation)? (p. 239)
- **Pipeline** (Figure 1, p. 239): survey the literature (Section 2), operationalise tasks (3), test 13 models (5–6), advise researchers (7). The authors propose a blended supervised–unsupervised scheme for human–AI labelling (p. 240).
- **Summary of findings** (p. 240):
  - Except in minority cases, prompted LLMs do not match carefully fine-tuned classifiers.
  - The best LLM performance is often too low to replace human annotation entirely.
  - LLMs reach fair agreement with humans.
  - The introduction adds that these results are not limited to a subset of fields and span utterance, conversation and document levels, and that the benefits of LLMs are compounded as models scale up (p. 240).
  - Leading models match dataset reference explanations and can exceed them in relevance, coherence, faithfulness and fluency.
  - Humans prefer model outputs 50% of the time. (The generation evidence is in part 2.)

**Intuition note.** The question is not "is the LLM perfect?" but "is it good enough to be one more annotator?" The paper judges this mostly by agreement with gold labels and by comparison with a fine-tuned baseline.

### 2. An Overview of CSS (pp. 240–243)
- CSS is defined, following Lazer et al. (2020), as the development and application of computational methods to the scientific analysis of behavioural and linguistic data. It centres on the scientific method (testing broad, objective hypotheses). Digital Humanities focus more on subjectivity and particularity. The authors merge both under "CSS" (p. 240).
- Scope: classification, structured parsing, summarisation and generation. Aggregate mining and topic modelling "may be largely outside the scope" of transformer LMs, because of their fixed window and quadratic space cost (p. 240).
- The section maps each field to tasks. The tasks listed below are benchmarked later.
  - History: event detection and event argument extraction (pp. 240–241).
  - Literature: narrative analysis, roles, power, emotion, figurative language, humour (p. 241).
  - Linguistics: dialect features and language change (p. 241).
  - Political science: framing, ideology, stance, persuasion (pp. 241–242).
  - Psychology: humour, persuasion, politeness, empathy, emotion summarisation, positive reframing (p. 242).
  - Sociology: power, unhealthy conversations, emotion, hate, figurative slogans (pp. 242–243).

### 3. Representative CSS Task Selection (pp. 243–253)
The task selection is "not exhaustive." It differs from BIG-Bench, which lacks dialect, ideology, misinformation, persuasion, politeness, power, semantic change and stance. It has few document-level tasks and no conversation-level tasks (p. 243, fn. 1). Tasks are grouped by the unit of analysis.

**3.1 Utterance level** (an utterance is one speaker's unit of communication on one subject; p. 243):

| Task | Data and label space (as the text gives it) |
|---|---|
| Dialect | Indian English; 22 grammatical features (Demszky et al. 2021) (p. 244) |
| Emotion | Saravia et al. 2018 tweets, weakly labelled; text lists Plutchik's 8 categories (p. 244) |
| Figurative | FLUTE, 9k premise–hypothesis pairs; classes sarcasm, simile, metaphor, idiom (p. 244) |
| Hate | Latent Hatred; 6 classes, incl. white grievance and stereotypes (p. 245) |
| Humor | ~16K jokes, binary (p. 245) |
| Ideology | Ideological Books Corpus: 2,025 liberal, 1,701 conservative, 600 neutral sentences. Labels are perceived ideology, not the speaker's affiliation (p. 245) |
| Misinfo | Misinfo Reaction Frames, 25k headlines, binary, headline only (p. 245) |
| Persuasion | RAOP, strategies after Cialdini: Evidence, Impact, Politeness, Reciprocity, Scarcity, Emotion (p. 246) |
| Stance | SemEval-2016, favor/against/none; zero-shot uses only the Donald Trump target (p. 246) |
| Semantic change | TempoWiC: do two sentences use the same sense of a word? Binary (p. 246) |

**3.2 Conversation level** (multi-party exchanges; tasks largely from ConvoKit; p. 247):
- Discourse acts: Coarse Discourse Sequence Corpus, 9-class taxonomy. Announcements, Negative reactions and Other are dropped, leaving 7 classes (p. 247).
- Empathy: TalkLife; only the Exploration dimension of EPITOME is used (strong, weak, none) (p. 248).
- Persuasion: Winning Arguments (r/ChangeMyView), 3,051 conversations; predict whether the persuader got a "delta" (p. 248).
- Power: Wikipedia Talk Pages; is the editor an administrator? The input is the editor's whole comment history (p. 249).
- Toxicity: Conversations Gone Awry; from the first two messages, predict later toxicity (p. 249).
- Politeness: Stanford Politeness Corpus; Polite, Neutral or Impolite according to Mechanical Turk annotators (pp. 249–250).

**3.3 Document level** (a collection of utterances forming one narrative; p. 250):
- Event detection: Hippocorpus, 6,854 stories; binary sentence-level "new event" label (p. 250).
- Event argument extraction: WikiEvents with the KAIROS ontology (67 event types, versus 33 in ACE). Output is a structured template (pp. 250–251).
- Ideology: Article Bias Corpus (Left/Right/Centrist). Whole articles are the input (p. 251).
- Roles and tropes: CMU Movie Corpus; identify one of 72 tropes from a character's quotes alone (pp. 251–252).

**3.4 Generation tasks** (p. 252–253):
- Emotion-specific summarisation: COVIDET, 1,883 Reddit posts. Summarise what triggered a given emotion.
- Figurative-language explanation: explain the entailment or contradiction in FLUTE pairs.
- Implied-misinformation explanation: state the writer's intent behind a headline.
- Social Bias Inference: SBIC, 34K inferences. Write the implied statement.
- Positive reframing: rewrite a distorted negative utterance using cognitive-behavioural-therapy strategies, without contradicting the speaker.

### 4. Evaluation Methods (pp. 253–257)
**4.1 Models and baselines (pp. 253–254).**
- Open models: FLAN-T5 (instruction-tuned encoder-decoder) in "six different sizes" from small (80M parameters) to XXL (11B) and UL2 (20B) (p. 253).
- OpenAI models: GPT-3 text-001 (ada, babbage, curie, davinci), text-002, and text-003 (further trained with human preferences, RLHF). Also gpt-3.5-turbo (conversational, RLHF) and GPT-4. GPT-4 is described as 1.7 trillion parameters, about 1000× scaled up from GPT-3 (p. 253). Footnote 7 (p. 263) warns that these sizes are estimates.
- Baselines: RoBERTa-large for classification, tuned on validation F1. T5-base for generation, tuned on validation BLEU. The grid search covers learning rate {5e-6, 1e-5, 2e-5, 5e-5}, batch size {4, 8, 16, 32} and epochs {1, 2, 3, 4}. Results are averaged over 3 seeds (p. 254).
- The baselines are meant as a comparison point, "rather than" a fair methodological comparison. They match or exceed best published results on several tasks, and better architectures might do more (p. 254).

**4.2 Prompt engineering (pp. 254–255).**
- The author most familiar with a task writes the prompt. gpt-3.5-turbo then produces four paraphrases, and results are averaged over all five prompts (pp. 254–255).
- Decoding uses temperature 0. Where probabilities are available, decoding is constrained to valid classes. Otherwise logit bias favours valid outputs (p. 254).
- Models were found to hedge, refuse offensive content and go beyond the given labels. Table 1 therefore lists guidelines (p. 255):
  1. Enumerate categorical options as alphabetical multiple choice, one per line.
  2. Give instructions after the context, then state constraints.
  3. State what to do under uncertainty (e.g. "you must pick either True or False").
  4. Request JSON when several pieces of information are needed.
- The prompts are "reasonable approximations", not claimed optimal (p. 255).

**4.3 Test sets (p. 255).** At most 500 class-stratified instances per task, from the designated test set (or the whole dataset if none). Sizes are in Table 2 (p. 256).

**4.4 Metrics (pp. 255–257).**
- Classification and parsing: macro F1, averaged over the 5 prompts, because label counts differ. Outputs are scored by string matching (p. 255).
- Generation: BLEU and BERTScore showed no discernible pattern against manual inspection, and BLEURT reported zero overlap despite good outputs. Human evaluation is therefore used (p. 256).
- Scoring: a blinded domain expert, recruited on Upwork, rates 100–400 outputs on 1–5 Likert scales for faithfulness, coherence, relevance and fluency (definitions after Fabbri et al. 2021) (pp. 256–257).
- Ranking: for Social Bias Frames, annotators rank four implied statements, from OpenAI models or the gold, from best to worst with no ties. A unanimous vote is used to decide when a model outranks the human; the authors say this "reflects only significant differences" (p. 257).
- Pilot annotation showed that crowdworker evaluations can have high variance. The authors therefore served as blind annotators, two per task (p. 257).

**Intuition note.** Averaging over paraphrased prompts and fixing temperature to zero keeps one lucky prompt from deciding the result. Human judges replace overlap metrics because, on high-variation generation tasks, overlap metrics are expected to correlate poorly with human quality judgments (p. 256).

### 5. Classification Results (pp. 257–264)
Headline: the authors say the results suggest that LLMs are a viable tool for augmenting human annotation, and show that larger instruction-tuned open-source LLMs are preferable for classification (p. 257).

**5.1.1 Zero-shot viability (RQ1; pp. 257–260).**
- The test: if overall performance is high and model–human agreement is as high as human–human agreement, LLMs might viably augment annotation (p. 257).
- Two paradigms are named:
  - The LLM is one labeller among many, and gold labels come from majority vote.
  - LLM pseudo-labels plus a small gold set feed unbiased estimators, as in Design-based Semi-supervised Learning (DSL; Egami et al. 2023) (p. 257).
- Misinformation: best F1 is 77.4 (FLAN-UL2). κ with gold is 0.55, versus 0.51 inter-human in the original paper (p. 257, Tables 3–4).
- Across the 17 tasks in Table 4, 8 (47%) reach moderate-to-good κ of 0.40–0.65. The highest F1s are Stance 76.0, Emotion 70.8, Figurative 62.3 and utterance-level Ideology 60.0. For these, the authors recommend DSL and augmented-annotator paradigms (pp. 257–259).
- The authors say these strong performances are on tasks with objective ground truth or labels with explicit colloquial definitions in the pretraining data. In the authors' own manual error analysis, errors there are less often "neutral" defaults and more often gold-label mistakes (p. 259, Figure 2).
- Zero-shot results rarely exceed the tuned RoBERTa baselines, but the best match classifiers in published studies (e.g. stance, 67.8 F1). Zero-shot could then replace expensive training sets, with humans validating outputs and tuning prompts. The authors urge caution and human-in-the-loop checks in sensitive domains (p. 259).
- Poor agreement occurs in 5 of 17 tasks (text: 29.5%). Best F1 is then barely above the random baseline:

| Task | Best F1 | Random |
|---|---|---|
| Semantic Change | 56.9 | 50 |
| Empathy | 35.9 | 33.3 |
| Conversation Persuasion | 53.9 | 50 |
| Toxicity | 55.4 | 50 |

  Event Argument Extraction is structurally complex. Empathy and Tropes have subjective taxonomies that differ from definitions learned in pretraining (p. 259). GPT-3.5 often defaults to the generic label "stereotype" (64% of errors) instead of "white grievance" (pp. 259–260).

**5.1.2 Error analysis (pp. 260–261).** Figure 2 plots "gold/plausible" errors against "neutral" errors for four tasks. Gold/plausible means the gold label is wrong or the model's label is a valid secondary one. Neutral means over-predicting a generic class (p. 259). By task:
- Figurative language: 29 items where all models were wrong. In 14 all models agreed on one wrong answer (unanimous errors). Four of those were plausible or gold errors: 1 wrong gold label and 3 similes nested in sarcasm. Of the other 10, 3 were idioms called metaphors and 7 were similes called metaphors. This is surprising, since similes carry the keywords "as" and "like". Of the remaining 15, in 5 all models disagreed and missed sarcasm. In 5 the dataset was mislabelled (4 idioms marked metaphor, 1 simile marked idiom). In 5 ChatGPT predicted the generic "metaphor" (p. 260).
- Emotion: 50 items where all models differed from gold. At least 18 are judged gold mislabels. For FLAN-UL2 and ChatGPT, 17 and 15 of 50 predictions were still valid. ChatGPT over-labels *surprise* (gold joy 8, love 5). UL2 confuses love with joy (9). davinci confuses sadness with joy (9) (p. 260).
- Politeness: models differ in per-class accuracy:

| Model | Polite | Neutral | Impolite |
|---|---|---|---|
| FLAN-T5-XL | 70.4 | 62.0 | 45.2 |
| davinci-002 | 43.9 | 82.9 | 40.9 |
| ChatGPT | 66.8 | 75.9 | 9.0 |

  All three are wrong on 81 of 498 items, and in 54 the three make the same error. In 79 of the 81 the cue is first/second-person mention, and all are direct or indirect questions. In 38 a counterfactual or indicative modal appears (pp. 260–261).
- Implicit hate: davinci-003 and ChatGPT over-predict "stereotypical" (71% and 65% false-positive rates). Of the false positives, 86% contain identity terms. Models miss phrasal signals for white grievance (3/50). Other false negatives need sociopolitical knowledge (2/50) or understanding of humour (6/50). In 5/50 the model chose a valid secondary category (p. 261).

**5.1.3 Few-shot viability (p. 261).** On FLAN models, 3-shot and 5-shot prompts without extra prompt engineering give "spotty and inconsistent" gains (Table 5, p. 262). For Empathy and conversation Persuasion, few-shot helps in 2 and 5 of 6 model sizes respectively. The authors conclude that more engineering may be needed.

**5.2 Model selection (RQ2; pp. 261–263).**
- Structured parsing (event extraction) is best served by a code-instructed model like gpt-3.5-turbo. Most classification tasks are best served by open-source models like FLAN-UL2 (p. 261).
- Size, FLAN: performance scales nearly logarithmically with parameter count (Figure 3, p. 262). The median average gain is 5.0 absolute F1 points per order of magnitude. FLAN-T5 shares data, objective and architecture, which gives a controlled setting (p. 262).
- Size, OpenAI: ada to davinci-001 gives minimal gain despite three orders of magnitude. GPT-4 gives little over GPT-3.5-turbo. The authors say the greatest improvements come from pretraining, fine-tuning and RL variations (p. 263).
- Pretraining and instruction tuning: davinci-001 to davinci-002 adds about 11 absolute points, larger than any gain from scale alone. davinci-002 builds on a base-code model with more instruction data and was pretrained on text and code. On JSON-formatted Event Argument Extraction it gains +13.0 F1 while davinci-001 often fails to produce JSON (p. 263).
- RLHF: text-davinci-003 and gpt-3.5-turbo (with RLHF) improve the mean F1 of text-davinci-002 (without) by 3.5 points (p. 263).

**Intuition note.** Bigger helps open FLAN models steadily. For OpenAI models the training recipe (instructions, code, human feedback) matters more than size. The authors caution that OpenAI sizes are estimates (fn. 7, p. 263).

**5.3 Domain utility (RQ3; pp. 263–264).**
- Tasks are binned into the field they most affect (a 1:1 partition the authors flag as imperfect, so readers should "interpret with caution"). Figure 4 shows that field distributions overlap heavily. The authors see no strong bias for or against a field. Within political science, misinformation reaches 77.4 F1 and implicit hate 32.3. Within psychology, emotion reaches 70.8 and empathy 35.9 (p. 264).
- Performance "may be more closely determined by the complexity of the input." The text says document-level tasks are hardest, with character tropes and event argument extraction the two lowest (but Table 3 does not fully show this; see Reading notes). For utterance- and conversation-level tasks, the text says difficulty also reflects label-space complexity, giving implicit hate, empathy and dialect (expert-labelled on a subtle theoretical taxonomy) as examples (p. 264).

### 6. Generation Results (start, p. 264)
RQ4 asks whether prompted LLMs can generatively implement theories and explain constructs. FLAN models failed to follow instructions on these tasks and are excluded. The OpenAI suite is evaluated by the human setup of Section 4.4. According to the domain experts, leading models can match or exceed gold references. For emotion summarisation, misinformation explanation and social bias inference, gpt-3.5-turbo is on average more faithful, coherent and fluent than the gold and the fine-tuned baseline. The text breaks off at the Positive Reframing and Figurative explanation results for text-davinci-003 (p. 264).

## Toy example (ours, not from the paper)
A zero-shot LLM labels 10 headlines as misinformation (+) or not (−). Gold has 5 (+) and 5 (−). The LLM gets 4 of the 5 (+) right and 4 of the 5 (−) right.
- Counts: TP = 4, FN = 1, FP = 1, TN = 4.
- Class (+): precision 4/5 = 0.8, recall 4/5 = 0.8, F1 = 0.8. Class (−): the same, F1 = 0.8. Macro F1 = (0.8 + 0.8)/2 = 0.8.
- Agreement (standard Cohen's κ; the paper gives no formula in these pages). Observed agreement $p_o = 8/10 = 0.8$. Chance agreement $p_e = 0.5\cdot0.5 + 0.5\cdot0.5 = 0.5$ (LLM says + half the time, gold is + half the time). So $\kappa = (0.8-0.5)/(1-0.5) = 0.6$.
- Reading: κ = 0.6 lies inside the 0.40–0.65 range that the paper calls "moderate to good" agreement (p. 257). If the LLM instead labelled every item (+), accuracy would be 0.5, and macro F1 would be $(0.667+0)/2 = 0.333$ (F1 for + is $2\cdot0.5\cdot1/1.5=0.667$).

## Concepts
- [[zero-shot-few-shot-prompting]] — specifying a task with instructions only (zero-shot) or with 3 or 5 examples (few-shot); the paper tests both on FLAN (pp. 238, 261)
- [[pretraining-fine-tuning]] — here, instruction fine-tuning plus pretraining on text and code changes CSS accuracy more than size does in the OpenAI family (p. 263)
- [[rlhf]] — training with human preference feedback (text-003, gpt-3.5-turbo); +3.5 mean F1 over davinci-002 (pp. 253, 263)
- [[scaling-law]] — FLAN mean F1 grows nearly log-linearly with parameters, about 5.0 points per tenfold increase; the GPT-3 001 models do not scale monotonically and GPT-4 gives little over GPT-3.5-turbo (pp. 262–263)
- [[supervised-fine-tuning]] — used for the RoBERTa-large and T5-base baselines (p. 254)
- [[macro-f1]] (new) — F1 averaged equally over classes; the paper's main classification metric (p. 255)
- [[inter-annotator-agreement-kappa]] (new) — κ between model and gold labels, compared with human–human κ; bands poor/fair/moderate/good (pp. 257–258)
- [[prompt-perturbation-averaging]] (new) — averaging results over an author-written prompt and 4 paraphrases to reduce instruction variance (p. 254)
- [[constrained-decoding-logit-bias]] (new) — restricting or biasing output tokens to valid class labels so scoring is string matching (p. 254)
- [[css-prompt-guidelines]] (new) — the Table 1 rules for consistent, machine-readable outputs (p. 255)
- [[llm-augmented-annotation]] (new) — LLM as one annotator among many, or via DSL with a small gold set (p. 257)
- [[design-based-semi-supervised-learning]] (new) — using LLM pseudo-labels with a small gold set for unbiased downstream estimates (Egami et al. 2023) (p. 257)

## Canonical instances
- [[misinfo-reaction-frames]] — best zero-shot task: 77.4 F1, κ 0.55 versus 0.51 inter-human (p. 257)
- [[flute-figurative-language]] — classification and explanation tasks; unanimous model errors on similes called metaphors (pp. 244, 260)
- [[latent-hatred-implicit-hate]] — models over-predict "stereotypical"; identity terms trigger it (pp. 245, 261)
- [[stanford-politeness-corpus]] — all three models struggle with direct or indirect questions with first/second-person mentions (pp. 249, 261)
- [[winning-arguments-persuasion]] — conversation-level task with F1 barely above random (pp. 248, 259)
- [[wikievents-kairos]] — event argument extraction needs JSON; davinci-002 gains +13.0 F1 over davinci-001 (pp. 250, 263)
- [[social-bias-frames-sbic]] — the example for human ranking evaluation (pp. 253, 257)

## Bridges (candidates)
- [structural-analogy] LLM pseudo-labels plus a small gold set (DSL) ↔ statistics/econometrics: estimating with surrogate labels while correcting bias — the aim is unbiased downstream estimates from noisy labels.
- [structural-analogy] FLAN near-log-linear scaling (5.0 F1 points per decade) ↔ llm: power-law scaling laws — the paper says the trend roughly matches Kaplan et al.'s prediction.
- [structural-analogy] Model defaults to a generic label ("stereotype", "metaphor", "neutral") ↔ measurement validity: taxonomy mismatch between a coder's everyday concept and an expert codebook.
- [metaphor] Human-in-the-loop prompt tuning ↔ codebook development in qualitative social science: iterating instructions as one iterates a codebook.

## Questions this raises
- If gold labels have mistakes (18 of 50 emotion errors judged mislabels), how should agreement with gold be interpreted as a measure of LLM quality?
- Would better prompt engineering or fine-tuning narrow the gap on expert taxonomies (empathy, tropes, implicit hate) where few-shot gave only spotty gains?
- Is the weak κ on Persuasion and Toxicity a limit of prediction from early context, or of the models?
- Do these conclusions hold for newer models, other languages or other data that may have been seen in pretraining? (The paper itself restricts the study to English; p. 238.)

## Reading notes
- **Scope of this part.** It starts at the title page (printed p. 237) and ends mid-Section 6 on printed p. 264, at "Human Scoring Evaluation", where the sentence on text-davinci-003 is cut off. Table 6, the rest of Section 6 and Section 7 are in part 2. Printed pages are used throughout (printed = pdf + 236).
- **Counts disagree.** The abstract says 25 benchmarks and 13 models. Introduction and Figure 1 say "24 tasks". Section 3 counts 20 classification plus 5 generation tasks. Table 3 has 14 model columns (6 FLAN, 4 text-001, 2 davinci-002/003, GPT-3.5, GPT-4).
- **Label spaces.** Text on Emotion lists Plutchik's 8 categories, but Table 2 lists 6 classes, and the error analysis mentions *love*, which is not among the 8. Dialect: text says 22 features, Table 2 says 23 classes. Persuasion (RAOP): text lists 6 strategies, Table 2 says 7 classes. Section 4.1 mentions "Event Surprisal", Table 2 "Evt. Surprisal", Table 3 "Event Det.", and the text Section 3.3.1 "Event Detection".
- **Table 3 versus Table 4.** The Table 4 image shows Stance best model gpt-3.5-turbo with 72.0 F1, while the text and Table 3 give 76.0 (GPT-4). Several other Table 4 best-model entries differ from the colour-highlighted Table 3 cells. The Table 4 "Event Det." row shows 23.0, the Event Arg. value in Table 3. The caption says 3 of the 6 conversation tasks have at least fair κ, which matches the image. The printed percent 29.5% for 5/17 is rounded oddly (5/17 ≈ 29.4%).
- **Claims in Section 5.3 versus Table 3.** The text says the two lowest task performances are document-level and that all other document-level scores are at or below 50%. Table 3 shows Event Det. 52.4 (davinci-003) and Ideology 51.5 (GPT-4). Tropes at 44.9 is not among the overall lowest.
- **Section 5.1.2 text.** The figures "17/20" (UL2) and "19/20" (ChatGPT) on the emotion errors use a denominator of 20, which does not fit the 50-item sample, so I cannot tell what they count. Figure 2's caption describes the best model per class, while the text says the figure shows gpt-3.5-turbo.
- Section 4.2 says "four" perturbations plus the original and later "five"; I read these as consistent (4 paraphrases + original). A "pertubations" typo appears on p. 255.
- OCR was clean overall. Tables 3–5 and Figure 4 were read from the images.
