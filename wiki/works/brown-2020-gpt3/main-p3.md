---
id: brown-2020-gpt3/main-p3
work: brown-2020-gpt3
unit: paper (part 3/3) — Appendix G (task phrasing), Appendix H (results for all tasks and model sizes), References
pages: 50–75
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# GPT-3 paper, part 3: task formats (App. G), full results table (App. H), references

## L0 — One line
This part of the paper shows how each task was formatted as a text prompt with answer options or a target completion (App. G) and lists the zero-, one- and few-shot score of every task for all eight model sizes (App. H).

## L1 — The gist (≤ 120 words)
This part contains no new argument. It documents the experiments. Appendix G prints one real dataset example for each of the paper's tasks. Each example shows the context text and either the candidate answers or the target completion. The captions state special scoring rules: normalizing by the unconditional probability of each answer, partial evaluation for Winograd-style tasks (comparing the probability of the same ending after a correct and an incorrect context), and all-answers-correct scoring for MultiRC. Appendix H gives Table H.1, with scores for every task, setting (zero/one/few-shot) and model size, plus captions of figures that group results by task category. The reference list follows. These pages help a reader check how tasks were posed and look up exact numbers.

**Prerequisites:** the idea of zero-/one-/few-shot prompting, multiple-choice versus free-form completion tasks, and the metrics acc, F1, EM, BLEU and perplexity.

## L2 — Key ideas (5–10 bullets)
- Every task is cast as text: a context string plus either candidate completions to rank or a target completion to generate. Appendix G prints one ground-truth example per task and says no GPT-3 samples appear there (p. 50).
- Prompt wording varies by task: "Article: … Q: … A:" (RACE), "Question: … Answer:" (ARC), "question: … answer:" (BoolQ, CB, RTE, WiC), "=" for translation and scrambling, "->" for LAMBADA (pp. 50–61).
- In these pages, several scoring rules are stated only in captions: normalization by unconditional answer probability (RACE, OpenBookQA, ARC), "partial" evaluation (Winograd, Winogrande), and per-question all-correct scoring (MultiRC) (pp. 50–54).
- TriviaQA allows many valid completions (15 acceptable strings are shown for one question), and ReCoRD counts a whole passage as one "problem" with two correct variants (pp. 52, 59).
- Zero-shot translation uses a "Q: What is the {language} translation of {sentence} A:" template. One- and few-shot use "source =" (p. 60).
- Table H.1 gives scores for 8 model sizes × 3 settings × all tasks. For arithmetic and word-scrambling tasks there is no fine-tuned SOTA entry (p. 63).
- In Table H.1, SOTA means the listed fine-tuned state-of-the-art score, and 175B is the largest of the eight model sizes. At 175B few-shot, the table lists scores above the listed SOTA for LAMBADA, TriviaQA, PIQA, Fr→En and De→En, and below it for most other tasks (p. 63).
- Arithmetic accuracy at 175B falls with digit count in every setting, from 100.0 (2D+, few-shot) to 9.30 (5D+, few-shot) (p. 63).

## L3 — Walkthrough

### G. Details of task phrasing and specifications (pp. 50–62)
The appendix says its figures show the formatting and phrasing of all tasks in the paper. All data comes from the ground-truth datasets, with no GPT-3 samples (p. 50). Each figure shows a **Context**. It then shows either answer options (each marked correct or incorrect) or a **Target Completion** for free-form generation.

**Tasks with answer options (pp. 50–55)**
- **RACE-h (G.1, p. 50)** and **RACE-m (G.3, p. 51)**:
  - The context starts with "Article:" followed by the passage.
  - Three earlier question/answer pairs follow, each in the form "Q: … A: …".
  - The final question has a blank (e.g. "The author considers politics and religion __") and ends with "A:".
  - There is one correct and three incorrect options (RACE-h: "taboo" correct; RACE-m: "names" correct).
  - The caption says that when predicting, the paper normalizes by the unconditional probability of each answer "as described in 2". That description is in the paper's section 2, not in these pages.
  - The same normalization sentence appears for OpenBookQA (G.8), ARC Challenge (G.11) and ARC Easy (G.16) (pp. 53–54).
- **ANLI R1/R2/R3 (G.7, G.2, G.10, pp. 51–53)**:
  - The context begins "anli N: anli N: " followed by a premise.
  - A hypothesis follows: "Question: … True, False, or Neither?".
  - Options are True / False / Neither.
  - The printed examples have the correct answers Neither (R1), Neither (R2) and False (R3).
- **PIQA (G.4)**: a goal sentence ("How to apply sealant to wood.") and two candidate solutions (p. 52).
- **COPA (G.5)**: a premise fragment ("My body cast a shadow over the grass because") and two candidate completions (p. 52).
- **ReCoRD (G.6, p. 52)**:
  - The context is a news passage plus bullet highlights.
  - Candidates are completions that fill in an entity.
  - Two candidates (Trump variants) are correct; three (Hillary Clinton, U.S., Yitzhak Rabin) are incorrect.
  - The caption says the whole context is treated as a single "problem". It says this is how the dataset presents the task and how the ReCoRD evaluation script scores it.
- **OpenBookQA (G.8)**, **HellaSwag (G.9)** and **SAT Analogies (G.12)**: a question or sentence stem plus 4–5 candidate endings. SAT has five options, e.g. "lull is to trust as" → "cajole is to compliance" (pp. 53).
- **ARC (Challenge/Easy)** (G.11, G.16): "Question: … Answer:" followed by four options (pp. 53–54).
- **StoryCloze (G.17)**: a four-sentence story and two candidate endings (p. 55).

**Winograd-style tasks with "partial" evaluation (G.13, G.14, pp. 53–54)**
- Each example gives a correct context and an incorrect context. They differ only in the resolved referent (e.g. "She thinks the sweater" versus "She thinks the jacket"). A shared target completion follows ("looks dowdy on her").
- Winogrande has the same structure ("…because the fruits" / "…because the vegetables" → "are saccharine.").
- The captions say the 'partial' evaluation method compares the probability of the completion given the correct context with the probability given the incorrect context.

**SuperGLUE tasks (pp. 54, 58–59)**
- **MultiRC (G.15, p. 54)**:
  - MultiRC has three levels: passage, questions, answers.
  - The context is a passage headed "READING COMPREHENSION ANSWER KEY" followed by a question. Each candidate is written as "- [False] Bin Laden" or "- [True] Bin Laden".
  - Accuracy is computed per question. A question is correct if and only if all its answers are labelled correctly.
  - For this reason K refers to the number of **questions** shown in the context.
- **BoolQ (G.29)**: passage, then "question: … answer:", target "yes" (p. 58).
- **CB (G.30)**: passage, then "question: Manhattan comes cheap. true, false, or neither? answer:", target "false" (p. 58).
- **RTE (G.31)**: context, then "question: … True or False? answer:", target "False" (p. 59).
- **WiC (G.32)**: two sentences, then "question: Is the word 'outfitter' used in the same way in the two sentences above? answer:", target "no" (p. 59).
- **WSC (G.33)**: a "Final Exam with Answer Key" header and instructions, then a passage with the pronoun marked in *bold*. The question is "what does the pronoun 'his' refer to?". The target is "mr. moncrieff" (p. 59).
- COPA and ReCoRD are also SuperGLUE tasks and were shown above.

**Tasks with a target completion**
- **CoQA (G.18, p. 55)**: a passage, then earlier Q/A turns about it, then a final "Q: … A:". The target is a span ("Helsinki, Espoo, Vantaa, Kauniainen, and surrounding commuter towns").
- **DROP (G.20, p. 56)**: "Passage: … Question: … Answer:". The target is a number ("4").
- **LAMBADA (G.21, p. 56)**: "Fill in blank:" followed by the story with a "___." gap and ending in "->". The target is a single word ("step").
- **Natural Questions (G.24, p. 56)** and **WebQs (G.35, p. 60)**: "Q: … A:" with no passage. The NQ target is a long name string ("Delloreese Patricia Early … known professionally as Della Reese").
- **QuAC (G.25, p. 57)**: "TITLE: … PARAGRAPH: …" then "Q: what team did he play for? A:". The target is "the Chicago Bears".
- **SQuADv2 (G.28, p. 58)**: "Title: … Background: …", one worked Q/A, then a second "Q: … A:". The target is "only on moonlit nights".
- **TriviaQA (G.34, p. 59)**: "Q: … A:". The caption says TriviaQA allows multiple valid completions. The printed list has 15 target completions for one question (spelling and case variants of Marcel Duchamp, plus "r mutt", "R.Mutt", "Duchampian").

**Word-manipulation tasks (pp. 55–57)**
- All five use the same instruction: "Please unscramble the letters into a word, and write that word:", followed by the scrambled string and " =" (e.g. "asinoc =").
- Examples: Cycled Letters "asinoc =" → casino (G.19); Anagrams 1 "skicts =" → sticks (G.22); Anagrams 2 "volwskagen =" → volkswagen (G.23); Symbol Insertion "r e!c.i p r o.c a/l =" → reciprocal (G.26); Reversed Words "taefed =" → defeat (G.27).

**Translation (G.36–G.41, pp. 60–61)**
- Six directions are shown: De→En, En→De, En→Fr, Fr→En, En→Ro, Ro→En.
- Format: source sentence followed by " =", target is the translation.
- The G.36 caption says this is the format for one- and few-shot learning (for this and the other language tasks). The zero-shot format is "Q: What is the {language} translation of {sentence} A: {translation}."

**Arithmetic (G.42–G.51, pp. 61–62)**
- Format: "Q: What is … ? A:", with the target a number.

| Task | Example prompt | Target |
|---|---|---|
| 1DC | (2 * 4) * 6 | 48 |
| 2D− | 17 minus 14 | 3 |
| 2D+ | 98 plus 45 | 143 |
| 2Dx | 95 times 45 | 4275 |
| 3D− | 509 minus 488 | 21 |
| 3D+ | 556 plus 497 | 1053 |
| 4D− | 6209 minus 3365 | 2844 |
| 4D+ | 9923 plus 617 | 10540 |
| 5D− | 40649 minus 78746 | −38097 |
| 5D+ | 65360 plus 16204 | 81564 |

*Intuition note.* In these figures, each benchmark appears as a text context plus either candidate answers or a target completion. The figures differ mainly in prompt wording and in a few scoring rules stated in captions (normalizing by unconditional probability, comparing two contexts, per-question scoring). So the prompt format and scoring rule shown here look like part of what defines each reported task, alongside the dataset.

### H. Results on all tasks for all model sizes (pp. 63–67)

**Table H.1 (p. 63)** gives "scores for every task, setting and model that we investigate in this paper".
- Columns: Name, Metric, Split, Fine-tune SOTA, K. Then, for each of Zero-Shot, One-Shot and Few-Shot, eight model sizes: Small, Med, Large, XL, 2.7B, 6.7B, 13B, 175B. A last column gives the 175B few-shot score from the test server, filled for only some tasks.
- K is not defined in these pages except in the MultiRC caption (number of questions in the context).
- For arithmetic, word-manipulation and SAT Analogies rows, Split is "n/a" and the Fine-tune SOTA cell is empty. The SOTA cell is empty for the "-sb" BLEU rows other than En→Fr and En→De.
- The ANLI rows list "test" under Split, and the SuperGLUE average row is listed on "dev".

**Selected 175B entries (p. 63)** (SOTA = listed fine-tuned value; ppl is lower-is-better):

| Task (metric, K) | SOTA | Zero | One | Few |
|---|---|---|---|---|
| HellaSwag acc (20) | 85.6 | 78.9 | 78.1 | 79.3 |
| LAMBADA acc (15) | 68.0 | 76.2 | 72.5 | 86.4 |
| LAMBADA ppl (15) | 8.63 | 3.00 | 3.35 | 1.92 |
| StoryCloze acc (70) | 91.8 | 83.2 | 84.7 | 87.7 |
| NQs acc (64) | 44.5 | 14.6 | 23.0 | 29.9 |
| TriviaQA acc (64) | 68.0 | 64.3 | 68.0 | 71.2 (test server 71.2) |
| WebQs acc (64) | 45.5 | 14.4 | 25.3 | 41.5 |
| Fr→En 14 BLEU-mb | 35.0 | 21.2 | 33.7 | 39.2 |
| De→En 16 BLEU-mb | 40.2 | 27.2 | 30.4 | 40.6 |
| Ro→En 16 BLEU-mb | 39.9 | 19.9 | 38.6 | 39.5 |
| En→Fr 14 BLEU-mb | 45.6 | 25.2 | 28.3 | 32.6 |
| Winograd acc (7) | 93.8 | 88.3 | 89.7 | 88.6 |
| Winogrande acc (50) | 84.6 | 70.2 | 73.2 | 77.7 |
| PIQA acc (50) | 77.1 | 81.0 | 80.5 | 82.3 (test server 82.8) |
| ARC Challenge acc | 78.5 | 51.4 | 53.2 | 51.5 |
| OpenBookQA acc (100) | 87.2 | 57.6 | 58.8 | 65.4 |
| CoQA f1 (5) | 90.7 | 81.5 | 84.0 | 85.0 |
| DROP f1 (20) | 89.1 | 23.6 | 34.3 | 36.5 |
| SQuADv2 em (16) | 90.7 | 52.6 | 60.1 | 64.9 |
| SuperGLUE average | 89.0 | 58.2 | 68.9 | 73.2 (test server 71.8) |
| ANLI R3 acc (50) | 48.3 | 34.5 | 35.1 | 40.2 |

- Reading the table: few-shot 175B is above the listed SOTA for LAMBADA (acc and ppl), TriviaQA, PIQA, Fr→En and De→En. It is below the SOTA for most other listed rows (e.g. StoryCloze, WebQs, DROP, SuperGLUE average).
- Some single cells do not follow the size trend. For De→En BLEU-mb, one-shot is 33.0 at 13B and 30.4 at 175B. For 2D+, one-shot is 73.0 at 13B versus few-shot 55.5 at 13B.
- Other SuperGLUE 175B entries (zero / one / few; test-server value where printed):
  - BoolQ 60.5 / 76.7 / 77.5 (76.4)
  - CB acc 46.4 / 64.3 / 82.1 (75.6)
  - COPA 91.0 / 87.0 / 92.0 (92.0)
  - RTE 63.5 / 70.4 / 72.9 (69.0)
  - WiC 0.00 / 48.6 / 55.3 (49.4)
  - WSC 65.4 / 69.2 / 75.0 (80.1)
  - MultiRC acc 27.6 / 27.6 / 32.5 (30.5)
  - ReCoRD acc 90.2 / 90.2 / 89.0 (90.2)
- WiC zero-shot is 0.00 at all eight sizes (p. 63).
- ANLI R1 and R2 at 175B are 34.6/32.0/36.8 and 35.4/33.9/34.0 (zero/one/few) (p. 63).

**Arithmetic and string tasks, 175B (zero / one / few) (p. 63)**

| Task | Zero | One | Few |
|---|---|---|---|
| 2D+ | 76.9 | 99.6 | 100.0 |
| 2D− | 58.0 | 86.4 | 98.9 |
| 3D+ | 34.2 | 65.5 | 80.4 |
| 3D− | 48.3 | 78.7 | 94.2 |
| 4D+ | 4.00 | 14.0 | 25.5 |
| 4D− | 7.50 | 14.0 | 26.8 |
| 5D+ | 0.65 | 3.45 | 9.30 |
| 5D− | 0.80 | 3.75 | 9.90 |
| 2Dx | 19.8 | 27.4 | 29.2 |
| 1DC | 9.75 | 14.3 | 21.3 |
| Cycled Letters | 3.66 | 21.7 | 37.9 |
| Anagrams 1 | 2.28 | 8.62 | 15.1 |
| Anagrams 2 | 8.91 | 25.9 | 39.7 |
| Symbol Insertion | 8.26 | 45.4 | 67.2 |
| Reversed Words | 0.09 | 0.48 | 0.44 |
| SAT Analogies (K=20) | 53.7 | 59.1 | 65.2 |

- Arithmetic rows use K = 50 and the scramble rows K = 100 (p. 63).
- In the arithmetic rows, models up to 6.7B score below 15 in all three settings, with one exception (2D+ one-shot at 6.7B: 19.6); at 13B the 2-digit rows jump (e.g. 2D+ at 13B: 15.4 / 73.0 / 55.5) (p. 63).

*Intuition note.* For the arithmetic rows, the table shows a similar pattern in all three settings. Scores are near zero for small models, then rise sharply only at 13B or 175B, and at 175B scores fall as the number of digits grows. At 175B few-shot is the highest of the three settings in every arithmetic row; it is not the highest in every row of the table (e.g. Reversed Words, Winograd).

**Figures H.1–H.11 (pp. 64–67)** are figures whose captions name result categories. Only the captions are available in these pages: all SuperGLUE tasks (H.1), SAT (H.2), all Winograd tasks (H.3), all Arithmetic tasks (H.4), all Cloze and Completion tasks (H.5), all Common Sense Reasoning tasks (H.6), all QA tasks (H.7), all Reading Comprehension tasks (H.8), all ANLI rounds (H.9), all Scramble tasks (H.10), all Translation tasks (H.11).

### References (pp. 68–75)
- An alphabetical list of cited works, with author-year keys such as [DCLT18], [KMH+20], [RWC+19], [VSP+17].
- These pages give no commentary on the references.
- Both [ZSW+19a] and [ZSW+19b] are given as "Fine-tuning language models from human preferences" with identical authors (pp. 74–75).

## Toy example (ours, not from the text)
This illustrates two scoring rules that Appendix G states only in captions.

**1. "Partial" evaluation (G.13).** Take a made-up model. Context A is "…She thinks the sweater", context B is "…She thinks the jacket", and the completion is "looks dowdy on her." Suppose the model assigns the completion probability 0.020 after A and 0.005 after B.
- Compare: 0.020 > 0.005, so the model picks A. A is the correct context, so this example is scored correct.
- The ratio is 0.020 / 0.005 = 4.

**2. MultiRC per-question accuracy (G.15).** Suppose 3 questions have 3, 2 and 3 answer options (8 answers in total). The model labels all 3 answers right for Q1, 1 of 2 right for Q2, and all 3 right for Q3.
- Answer-level accuracy would be (3 + 1 + 3) / 8 = 7/8 = 87.5%.
- Under the paper's rule a question counts only if all its answers are right, so Q1 and Q3 count and Q2 does not.
- Question-level accuracy is 2/3 ≈ 66.7%.

## Concepts
- [[zero-shot-few-shot-prompting]] — the three settings (zero, one, few examples in the context) under which every task is scored in Table H.1; the zero-shot translation template differs from the one/few-shot one (pp. 60, 63)
- [[task-prompt-format]] (new) — the fixed text template (prefix words, "Q:/A:", "=", "->") that turns a dataset item into a string for the model (pp. 50–62)
- [[unconditional-probability-normalization]] (new) — scoring multiple-choice options after normalizing by each answer's unconditional probability; used for RACE, OpenBookQA, ARC. Only named in captions here; defined in section 2 (p. 50)
- [[partial-evaluation]] (new) — compare the probability of a fixed completion under a correct context versus an incorrect one (Winograd, Winogrande) (p. 53)
- [[per-question-all-correct-accuracy]] (new) — MultiRC counts a question correct only if all its answers are labelled correctly (p. 54)
- [[perplexity]] — LAMBADA is reported both as accuracy and as ppl in Table H.1 (p. 63)
- [[scaling-law]] — Table H.1 provides raw per-size scores across eight sizes; these pages state no law (p. 63)

## Canonical instances
- [[racing-passage-mc]] — RACE-h/m format with prior Q/A pairs and four options (pp. 50–51)
- [[winograd-partial-eval]] — sweater/jacket and fruits/vegetables examples (pp. 53–54)
- [[multirc-scoring]] — three-level passage/question/answer structure, scored per question (p. 54)
- [[triviaqa-multi-answer]] — 15 acceptable strings for one answer (p. 59)
- [[arithmetic-n-digit]] — 1DC to 5D± prompts and 175B accuracies (pp. 61–63)
- [[unscramble-tasks]] — five string tasks sharing one instruction (pp. 55–57)

## Bridges (candidates)
- [structural-analogy] Prompt templates for each task ↔ survey methodology: question wording and response format — both show that fixed phrasing affects what is measured, so the format must be reported.
- [structural-analogy] "Partial" evaluation of Winograd completions ↔ likelihood-ratio comparison between two hypotheses — the choice is made by comparing probabilities of the same data under two conditions.
- [metaphor] Table H.1 as a results grid ↔ a replication package in social-science research — it lets others check each number.

## Questions this raises
- How exactly does the unconditional-probability normalization in section 2 work, and how much does it change accuracy compared with plain likelihood ranking?
- Why does One-Shot sometimes exceed Few-Shot for the same model (e.g. 2D+ at 13B: 73.0 vs 55.5)? Is it noise, or an effect of prompt content?
- Why are some zero-shot cells exactly 0.00 (WiC at every size, CB at Small)? Is this a formatting failure rather than a lack of ability?
- Why are the MultiRC zero-shot and one-shot rows identical in the table?

## Reading notes
- **Where this part starts and ends:** it begins at Appendix G (printed p. 50) and ends with the last reference on p. 75. The split is at a section boundary. Printed page = pdf page throughout.
- **Page images:** images were provided only for pdf 50–63. For pdf 64–67 (Figures H.1–H.11) and the references I had only the text layer. The text layer contains just the captions, so I did not describe the figure contents.
- **Table H.1 (p. 63)** is dense. I checked cited values against the page image. The "K" column header is not explained on these pages beyond the MultiRC caption.
- **Rows with identical values:** the MultiRC acc and f1a rows have identical zero-shot and one-shot values at all sizes in the table. The source does not comment on this.
- **Printing artifacts:** Figure G.24 shows "{" where a dash is presumably meant ("July 6, 1931 { November 19, 2017)"). In Figures G.2, G.7 and G.10 the context begins with the label repeated ("anli 2: anli 2:"). In G.40/G.41, Romanian diacritics are garbled in the text layer; the images show correct characters.
- **Duplicate reference:** [ZSW+19a] and [ZSW+19b] have the same title and authors, so they appear to be one paper listed twice (pp. 74–75).
