---
id: shapira-2024-clever-hans/main
work: shapira-2024-clever-hans
unit: paper
pages: 2257–2273
fields: [theory-of-mind]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Clever Hans or Neural Theory of Mind? Stress Testing Social Reasoning in Large Language Models

## L0 — One line
Across six ToM datasets, 15 LLMs show some ToM-like success but no robust ability: performance varies by dataset, probing method and small adversarial changes, which suggests shallow heuristics rather than general reasoning.

## L1 — The gist (≤ 120 words)
Do large language models (LLMs) have a robust neural theory of mind (N-ToM)? Earlier papers disagreed, and some rested on a few anecdotes. The authors test 15 LLMs on six ToM datasets and compare probing methods. They also build two expert-made sets, ToMi′ and Adv-CSFB, that focus on adversarial examples. Some datasets are nearly solved, but no model does well on all. Results change with the probing method, and small variations of the original tasks (a transparent container, "in" changed to "on") sharply lower the performance of the best models. The authors conclude the abilities are limited and not robust, and they warn against anecdotes, small benchmarks and human-designed psychological tests applied to models.

**Prerequisites:** false-belief tasks (Sally–Anne); accuracy and majority-class baselines; prompting LLMs (zero-shot, multiple-choice, chain-of-thought); the idea of spurious correlation.

## L2 — Key ideas (5–10 bullets)
- **Meta-evaluation:** the best model per dataset ranges from near-perfect (TriangleCOPA 96%) to below the majority baseline (FauxPas-EAI, 27% story-level vs 30%). Some models do well on some datasets, but no model is robust on all (p. 2260–2261).
- **Probing method matters:** LM-, MC- and CoT-probing influence accuracy (sometimes little, sometimes several points). The authors argue a model with N-ToM should do well across probing techniques (p. 2261).
- **Spurious correlations:** accuracy is much lower on ToMi′ (built with alterations) than on ToM-k, although both use the unexpected-transfer task. The authors say this suggests the models' abilities are not based on generalization, and that models might be recognizing patterns from the Sally–Anne story (p. 2262).
- **Adversarial test (Adv-CSFB):** in the unexpected-transfer part, GPT-4 gets 97.5% on the original false-belief items but 0% on in→on and transparent access (p. 2262–2263).
- **Splits expose heuristics:** within ToMi and SocialIQa, some question types are much harder than the total score suggests (p. 2263).
- **Authors' hedged explanations:** reporting bias and instruction-tuned models assuming every detail is relevant are offered for failures on adversarial categories. Recency bias is offered for good true-belief results. All are stated with "might" or "partly", and the authors do not test them on these pages (p. 2264).
- **Methodological cautions:** anecdotes invite the ELIZA effect, and success on human tests does not transfer to models. "Solving" a benchmark is necessary but not sufficient, and a joint score is suggested (p. 2264–2265).
- **Emergence claims** are called unfounded and unfalsifiable without training data. The authors' contamination check on SocialIQa is inconclusive (p. 2265, 2273).

## L3 — Walkthrough

### Abstract and 1 Introduction (p. 2257–2258)
- The paper asks whether LLMs show N-ToM. It cites a conflict: Sap et al. (2022) say LLMs lack ToM; Kosinski (2023) says it emerged spontaneously, a claim criticized as methodologically flawed (Marcus & Davis). Ullman (2023) showed that simple changes to ToM questions break LLMs. Bubeck et al. (2023) claim GPT-4 has a very advanced level of theory of mind, based on a few anecdotal examples (p. 2257).
- Earlier work tested 2 tasks each. This paper uses 6 tasks and different probing methods (p. 2257).
- Claimed contributions: the largest quantitative ToM analysis so far, reproductions plus new results, and two new expert-made test sets with adversarial examples. The authors caution against anecdotes, limited benchmarks and human-designed psychological tests. They say success on a human test does not straightforwardly transfer from humans to models (p. 2258).
- The ELIZA effect is the incorrect ascription of human-like intelligence, or even sentience, to a machine (p. 2257).

### 2 Background: ToM and clinical tests (p. 2258)
- **False belief test:** a character has partial information and holds a false belief, while the listener knows the full story. In Sally–Anne (unexpected transfer), Sally puts a marble in her basket and leaves, and Anne moves it to her box. Questions: first-order belief (where will Sally look?), reality, and memory. Correct: Sally looks in the basket. A second-order question asks where Anne thinks Sally will look (p. 2258).
- **Smarties test (unexpected contents):** the protagonist does not know a container's real contents because of a false label (p. 2258).
- **Faux pas test:** a speaker says something the listener may not want to hear, without realizing it. Example: a guest says they like cakes except apple pie, when the host baked an apple pie. The original test has 10 stories with 4 questions each: detection, identification, a comprehension question, and a false-belief question (did they know or remember that?) (p. 2258).
- **2.3:** NLP work has modelled mental states and emotions. The authors say half of their tests are not meant for humans, and that when LLMs do well on benchmarks designed for humans we should be careful about reading this as having the human capability (p. 2258–2259).

### 3 Data (p. 2259–2260)
Table 1 lists the datasets (p. 2259):

| Dataset | Based on | Size | Built by |
|---|---|---|---|
| TriangleCOPA | social behaviour of fictional characters | 100 | experts |
| SocialIQa | motivations, next events, emotional reactions | 400 random out of 37,588 | crowdsourcing |
| ToMi | unexpected transfer; first- and second-order false belief | 400 random out of 1000+ | synthetic |
| ToMi′ (this paper) | adjusted ToMi | 180 questions, 30 stories | experts |
| epistemic_reasoning | factive and non-factive verbs; entailment | 2000 | experts, 10 templates |
| Adv-CSFB (this paper) | unexpected content or transfer + commonsense | 183 questions, 40 stories | experts |
| FauxPas-EAI | faux pas test | 176 questions, 44 stories | experts and AI + experts |

Appendix 7.3 describes each set. ToMi′ is 30 ToMi stories with 6 questions each. They were rewritten as sentence completion, e.g. "Oliver thinks that Emma searches for the grapes in the" (p. 2270–2271).

**3.1 Adv-CSFB.** It has 110 unexpected-contents and 73 unexpected-transfer examples. Each is a short paragraph about two objects $O_1, O_2$, followed by questions on reality and on the protagonist's belief (p. 2259). Three categories (p. 2260):
- **False belief:** Kosinski's original examples. He created only false-belief scenarios.
- **True belief** (for the unexpected contents task): each false-belief example is modified, for each applicable example, so the label shows the true content $O_1$, with $O_2$ mentioned in a way that does not change the answer. One author wrote them and another verified.
- **Adversarial:** up to 4 extra examples per false-belief example, following Ullman's alterations. Ullman's examples, per the authors, are sufficient to show LLMs did not robustly acquire ToM. Unexpected contents: transparent access, uninformative label, trustworthy testimony, late labels. Unexpected transfer: transparent access, in→on, trustworthy testimony, other person.
- Ullman's example: a bag of popcorn labelled "chocolate". LLMs still predict a false belief even if the bag is transparent or the protagonist cannot read (p. 2260, Fig. 6–7, p. 2270).

> **Intuition note.** Adversarial variants add one detail that should remove the false belief. A model that really tracks what the protagonist can know should change its answer; the authors use such variants because they could reveal reliance on heuristics (p. 2262).

### 4 Experiments & results (p. 2260–2261)
**4.1 Meta-evaluation.** Fifteen LLMs were run zero-shot on all datasets and compared with a most-frequent-class (MFC) baseline. The temperature was fixed at 0 after tests across temperatures (App. 7.5) (p. 2260).
- Key results (Table 2, p. 2261), accuracy in %:
  - TriangleCOPA: flan-t5-xxl 96 (MFC 52).
  - SocialIQa: flan-t5-xxl 86 (MFC 36).
  - ToMi: flan-t5-xl 81 (also flan-ul2 and flan-t5-base 81) (MFC 56).
  - Epistemic reasoning: MFC 63, which three j2 models equal; the best other model scores 61.
  - Adv-CSFB (question, story level): text-davinci-003 79, 61 (MFC 32, 25).
  - FauxPas-EAI (question, story level): gpt4-0314 74, 27 (MFC 55, 30).
- The text says the best LLM on FauxPas-EAI (27%) is below a simple most-frequent-class baseline (p. 2260).
- Best performance seems correlated with dataset age. Two possible explanations: newer datasets are harder by design, or models had more chance to train on older ones (p. 2260–2261).
- Conclusion: some models show strong ToM-like performance on some datasets, but "no model robustly exhibits ToM on all datasets". This is consistent with Sap et al. (2022) and Ullman (2023) (p. 2261).

**4.2 Probing technique.** The authors argue that a model claimed to have N-ToM should do well across probing techniques. Efficient methods may reveal latent abilities, but robustness should not depend on the probe (p. 2261).
- **LM-probing:** choose the answer option with the highest probability.
- **MC-probing:** the context, question and options are given, and the model generates the answer as a letter list (a, b, c). This works for models without probabilities (GPT-3.5, GPT-4).
- **CoT-probing:** the model reasons step by step, then answers. It was run zero-shot, without reasoning examples.
- Table 3 (400-item samples; accuracy in %): SocialIQa davinci-003 LM 55, MC 60, CoT 68; GPT-3.5 MC 67, CoT 69; GPT-4 MC 79, CoT 72. ToMi davinci-003 67/67/71; GPT-3.5 70 (MC), 73 (CoT); GPT-4 70 (MC), 73 (CoT).
- CoT generally helps, but not always, since reasoning can lead to wrong conclusions (p. 2261).

> **Intuition note.** The same model scores differently depending on how it is asked (GPT-4 loses 7 points with CoT on SocialIQa). The authors argue that a claim of N-ToM needs good performance across probing techniques, not just under the best one (p. 2261).

### 5 Clever Hans vs. generalized reasoning (p. 2261–2263)
Guiding question: do the models that solve the tasks have a general ability, or do they rely on memorization and shallow heuristics (Clever Hans)? The authors use adversarial examples in the way earlier work used them to show reliance on spurious correlations (p. 2261–2262).

**5.1 Spurious correlations: ToMi′ vs ToM-k.** Both test unexpected transfer. ToM-k has variants of Sally–Anne and only first-order questions. ToMi also has alterations that create negative examples (omission or duplication of information) and second-order questions. For fairness, ToMi was converted to sentence-completion format, and a "no second order" subset was made (p. 2262).

| Accuracy (%) | ToMi′ all questions | ToMi′ no second order | ToM-k |
|---|---|---|---|
| text-davinci-003 | 10 | 21 | 87 |
| GPT-3.5 | 27 | 48 | 65 |
| GPT-4 | 20 | 52 | 87 |

(Table 4, p. 2262.) The authors say the discrepancy suggests the models' abilities are not based on generalization. They suggest models might recognize patterns from the Sally–Anne story in ToM-k and answer from those patterns, and that ToMi′ gives lower scores because it is more robust to spurious correlations (p. 2262).

> **Intuition note.** The same task type gives 87% (text-davinci-003) on the familiar form and as low as 10% on the altered form. The authors suggest this may reflect pattern recognition rather than understanding of what a character thinks (p. 2262).

**5.2 Robustness on Adv-CSFB.** GPT models were tested with MC-probing. One out-of-domain ToMi example was prepended to fix the format. Accuracy is the average of questions 2 and 3, both about the agent's belief, at temperature 0 (p. 2262).
- Main finding: LLMs do not show robust performance across categories. Later LLMs excel in some categories while completely failing on others (p. 2262).
- **Unexpected transfer (Fig. 2):** GPT-4 reaches 97.5% (false belief) and 83.3% (trusted testimony). Other categories decline across models: other person 93.8% (davinci-002) → 68.8% (GPT-4); in→on 71.4% → 0%; transparent access 66.7% → 0% (p. 2262–2263).
- **Unexpected contents (Fig. 3):** the text says newer models do better on false belief and transparent access; nearly all models since text-davinci-002 do well on true belief. The same paragraph then says GPT-3.5-Turbo and GPT-4 decline against earlier models on transparent access, late label and uninformative label, so the text contradicts itself on transparent access. In the Figure 3 image, GPT-4 scores 100 on false belief, 18.8 on transparent access, 33.4 on late label and 34.3 on uninformative label (p. 2262–2263).
- Responses regenerated several times gave similar results. The authors conclude the models are confident even when wrong (p. 2262).
- Caveat: LM-probing results may differ slightly. In MC-probing, verbose models such as GPT-3.5-Turbo and GPT-4 may answer "none of the above" or "both". Still, a robust model should answer correctly regardless of probe (p. 2263).

**5.3 Is this a trend? (inspired by Sap et al., 2022).**
- ToMi (Fig. 4, p. 2263): by question type, GPT-3.5 gets 46% on false belief, close to random. The text gives GPT-3.5 81% accuracy (apparently overall), but the caption says 0.7 total (see Reading notes). In the figure, GPT-3.5 scores fact 100, true belief 81, mind 61. GPT-4 scores 15 on false belief.
- SocialIQa (Fig. 5, p. 2263): GPT-4 has 79% total. On questions about others, the Effect panel shows 61.1 against 81.8 for the main character. The Want panel shows 74.5 against 78.8.

### 6 Summary of findings and insights (p. 2264–2265)
- **Answer to "do LLMs have ToM?":** some datasets are nearly solved (TriangleCOPA 96%), others are hard (FauxPas-EAI 27%, below the majority baseline). The authors conclude that models do not have robust N-ToM abilities (p. 2264).
- They argue that Kosinski's and Bubeck's conclusions were over-generalized from a small number of examples (40 and 10 respectively). They write that their results show, in their own word "proving", that GPT-4 does not display robust N-ToM (p. 2264).
- **Clever Hans, heuristics, shortcuts.** The authors give hedged explanations ("might", "partly") (p. 2264):
  - *Reporting bias:* the bad performance on some adversarial categories might be partly due to it. People do not share obvious facts, so it is likely that LLMs are biased towards surprising continuations. In most of these categories belief equals truth, which makes a boring story.
  - *Instruction tuning:* GPT-3.5 and GPT-4 are trained to follow instructions. This might make them assume every detail matters, e.g. the false label, even when it cannot be read.
  - *Recency bias:* the good true-belief results might be attributed to it, since the correct content is typically mentioned last.
  - *Main character vs. others:* the authors reassess Sap et al.'s finding; Sap et al. suggested centering theory (texts focus on one protagonist) as a reason.
- **ELIZA effect and anecdotes.** LLMs are designed to produce text that looks high-quality to human observers. The illusion of human-like N-ToM, the authors say, often says more about the human reader than about the model. Later models hedge ("epistemic humility"), giving rationales for several answers. Humans may show confirmation bias and credit the model with the right one. The authors argue for quantifying performance across multiple large-scale datasets, preferably with automatic evaluation (p. 2264).
- **Human psychological tests.** These tests are carefully constructed and vetted for validity in humans. There is evidence that a person's success in one ToM task can indicate their ToM, but this does not transfer to models. If a system succeeds on a human instrument, we should consider other explanations (e.g. heuristics). The same holds in the other direction when models are used to learn about the human brain (p. 2264–2265).
- **Anthropomorphism.** The authors do not aim to make claims about "AI cognition", and their measures are not an endorsement of pursuing human-like social intelligence for AI. Whether LLMs could develop human-like ToM is left to philosophers (p. 2265).
- **"Solving" is necessary but not sufficient:** if a model fails at least one ToM task, it does not have ToM in general. Success on one example or task is not sound proof. Benchmarks will need to assess LLMs directly rather than through clinical tests. Aggregated scores hide differences across question types. One approach is to pair a hard question with an easy one and require both (a "joint score", used in FauxPas-EAI, Adv-CSFB, ToMi). Where pairing is hard, the authors recommend evaluating dataset difficulty by the lowest score across splits (p. 2265).
- **Emergence vs. training on the test set.** The authors argue that claims of emergence are (i) unfounded and (ii) unfalsifiable without the training data. Alternative factors include related datasets, online descriptions of clinical tests and user interactions. OpenAI acknowledged GPT-4 was trained on BIGBench test data (footnote 7). Since the GPT training data is not public, the degree of data leakage cannot be quantified. The authors echo calls for open training data (p. 2265).
- **Conclusion:** LLMs show an enhanced yet limited N-ToM that is not robust, with some evidence of over-reliance on simple heuristics (p. 2265).

> **Intuition note.** The authors' methodological rule is asymmetric: failing at least one ToM task means a model lacks ToM in general, while success on one example or task is not sound proof of ToM (p. 2265).

### Limitations and ethical statement (p. 2265–2266)
- Only 6 test sets, and many other ToM tests exist. Some questions may be ambiguous, but the authors keep human-style phrasing. Sharma et al. suggest human feedback may encourage sycophancy. Some LLMs refused to answer or gave the wrong format, which affected only MC-probing (p. 2265–2266).
- Zero-shot was kept deliberately, to test the claims of Kosinski and Bubeck, which rely on zero-shot setups. CoT might help GPT-4, but the authors warn that such methods may reveal task structure, like Clever Hans reacting to his owner's hints. The models are text-only (p. 2266).
- Some failures may reflect lower-level skills (e.g. transparent containers need physics knowledge). The authors say models also failed pure ToM tasks (Table 4) (p. 2266).
- Datasets are public and were checked by the authors for offensive content. The authors did not record the LLMs' responses (p. 2266).

### 7 Appendices (p. 2270–2273)
- **7.1:** In a ChatGPT example inspired by ToMi (Table 5), it answers the false-belief version correctly. In the trivial true-belief version (Natalie does not leave the room), it still says she will look in box A. The authors say this is likely due to exposure to Sally–Anne (p. 2270–2271).
- **7.2:** Ullman's variations are illustrated in Fig. 6–7 (p. 2270).
- **7.4:** Unless written otherwise, prompts use the MC-probing setup. Table 7 gives example prompts (for TriangleCOPA, epistemic reasoning and FauxPas-EAI). The decoding settings minimize randomness (Flan-T5 and Flan-UL2 use temperature 0.0001; OpenAI and AI21 models use 0) (p. 2271–2272).
- **Table 6** shows two stories with matching lexical, semantic, grammatical and pragmatic patterns, illustrating pattern similarity (p. 2272).
- **7.5:**
  - On TriangleCOPA, Flan-T5 accuracy mostly decreases as temperature rises (Table 8, 100 runs each; e.g. xxl 96.00 → 94.05). The authors fix temperature 0 as constant and reproducible (p. 2272–2273).
  - Running Kosinski's code, the authors found task 2 (unexpected transfer) scored 85% or 90% for GPT-3.5, and the two-task average 85% or 87.5%, against a reported 93%. They cite two clear mispredictions and one borderline format issue (p. 2272–2273).
- **7.6 Emergence or contamination?** Comparing 11 random subsets of 100 questions from the standard and the hidden SocialIQa test sets, gpt-3.5-turbo-0301 and gpt-4-0314 showed no significant difference (t-test). This is inconclusive about training on the test set, and it does not mean ToM has emerged (p. 2273).
- **7.7 ToMi′ subsets (Table 9, % correct):** the joint score counts a story as correct only if all its questions are right (30 stories); the average score is a simple average.

| Model | Reality | Memory | First order | Second order | Joint w/o second order | Joint all |
|---|---|---|---|---|---|---|
| Devinci003 | 100 | 96.6 | 61.6 | 25.0 | 20.6 | 10.3 |
| Turbo-0301 | 100 | 90.0 | 73.3 | 40.0 | 41.3 | 17.2 |

The authors conclude that the models answer simple reading-comprehension questions well, but not ToM questions (first and second order) with similar accuracy. Even when the story questions are answered correctly, they may fail more complex ones (p. 2273).

## Toy example (ours, not from the text)
**A heuristic that looks like ToM.** A "model" always answers "where the object started" in transfer stories.
- Test set A (false-belief only): 4 stories, in each the character misses the move, so the correct answer is "the original place". The heuristic gets 4/4 = 100%.
- Test set B (adds 4 true-belief stories where the character sees the move): the heuristic is wrong on all 4. Total = 4/8 = 50%.
- This mirrors the paper's logic: success on false-belief-only items is compatible with a shortcut, and adversarial or true-belief variants reveal it.

**Average vs. joint score.** 3 stories, each with an easy and a hard question.
- Easy: 3/3 correct. Hard: correct on story 1 only → 1/3.
- Average score = (3 + 1) / 6 = 66.7%.
- Joint score = stories with both correct = 1/3 = 33.3%.
- The joint score is the lower number, so it exposes the hard-question failures.

## Concepts
- [[theory of mind / mentalizing / mindreading]] — the ability to understand that others have thoughts, beliefs and emotions that differ from one's own; here asked of LLMs as N-ToM (p. 2257)
- [[machine theory of mind]] — Neural ToM (N-ToM): ToM-like abilities in neural language models, measured on benchmarks; the authors make no claim about AI cognition (p. 2257, 2265)
- [[first-order false belief]] — where will Sally look? A belief that differs from reality (p. 2258)
- [[second-order false belief]] — what one character thinks another character thinks or searches for (p. 2258, 2259)
- [[unexpected transfer task]] — an object is moved while the protagonist is absent; Sally–Anne (p. 2258)
- [[unexpected contents task]] — a container's contents differ from its label; Smarties test (p. 2258)
- [[Clever Hans effect]] — apparent competence from memorization and shallow heuristics rather than general ability (p. 2261)
- [[construct validity in LLM evaluation]] — human tests are vetted for validity in humans; success by a model does not allow the same conclusions (p. 2264–2265)
- [[data contamination]] — possible training on test data or related material; cannot be quantified without open training data (p. 2265, 2273)
- faux-pas-test (new) — a speaker says something unwelcome without realizing it; four questions per story (p. 2258)
- probing-method (new) — how a model is queried: LM-, MC- or CoT-probing (p. 2261)
- most-frequent-class baseline (new) — always predict the commonest answer in a dataset (p. 2260)
- joint-score (new) — a story counts as correct only if all its questions are right (p. 2265, 2273)
- reporting-bias (new) — people do not share obvious facts, so models may favour surprising continuations (p. 2264)
- ELIZA-effect (new) — humans assuming that computer behaviour is analogous to human behaviour (p. 2264)
- adversarial-test-set (new) — variants that add new information (e.g. the protagonist should know the truth), used to reveal heuristics (p. 2260, 2262)

## Canonical instances
- [[sally-anne-test]] — unexpected transfer false-belief test, basis for ToMi and ToM-k (p. 2258)
- [[smarties-test]] — unexpected contents task with false labelling (p. 2258)
- [[faux-pas-test]] — the apple-pie example and the FauxPas-EAI stories (p. 2258, 2259)
- [[ullman-variations]] — popcorn bag and cat-in-basket variants: transparent access, uninformative label, trusted testimony, late label, in→on, other person (p. 2260, 2270)
- [[adv-csfb]] — new dataset with false-belief, true-belief and adversarial categories (p. 2259–2260)
- [[tomi-prime]] — ToMi adjusted to sentence completion, 30 stories (p. 2270–2271)
- [[kosinski-2023-replication]] — rerun gave lower GPT-3.5 scores on task 2 (p. 2272–2273)

## Bridges (candidates)
- [structural-analogy] shortcut reliance revealed by adversarial variants ↔ machine-learning evaluation: spurious correlations and shortcut learning — same logic of changing what should not matter.
- [structural-analogy] joint score over paired easy and hard questions ↔ psychometrics/test design: requiring consistency across items before crediting an ability.
- [metaphor] Clever Hans horse responding to owner's cues ↔ LLMs responding to surface cues in prompts.
- [structural-analogy] ELIZA effect and confirmation bias ↔ human judgment: observers read competence into fluent output.

## Questions this raises
- If a model passes both original and adversarial variants plus several probing methods, would that be sufficient evidence of ToM, or only enough to rule out these heuristics?
- How much of the failure on "transparent access" reflects missing physical knowledge rather than missing mindreading (the authors raise this in their limitations)?
- Do CoT or belief-tracking methods fix the adversarial failures, or only expose the task structure to the model?
- Can a contamination test other than a SocialIQa hidden-set comparison tell memorization from generalization?

## Reading notes
- Printed page numbers 2257–2273 are visible on all pages (pdf 1–17, an offset of 2256); all citations use the printed numbers.
- Caption/text mismatches. In 5.3 the text says GPT-3.5 "achieves 81% accuracy" (apparently overall), while Figure 4's caption says 0.7 total (and 81.0 is the true-belief bar). In 5.3 the text says GPT-4 gets 74.5% on others, whereas the Figure 5 caption says 61% for "others effect". The 74.5 value is in the Want panel and 61.1 in the Effect panel. Figure 2's caption says 97%, while the bar and text say 97.5%.
- In 5.2 the text says newer models improved on transparent access in the unexpected-contents segment, and then says GPT-3.5-Turbo and GPT-4 declined on it; Figure 3 shows GPT-4 at 18.8.
- §6 says Sap et al.'s finding is "(§5.1)" but it is discussed in §5.3. Section 4.1 has the typo "suggest are that".
- The 7.7 text says Table 9 gives results for GPT-3.5, but the rows are Devinci003 and Turbo-0301 (the Table 9 caption does not name a model). Table 9 joint scores "all" (10.3, 17.2) and "w/o second order" (20.6, 41.3) can be compared with Table 4's ToMi′ columns only if those columns measure the same thing; the pages do not say so. If they do, davinci-003 matches (10, 21) while Turbo-0301 differs from GPT-3.5 (27, 48), and the source does not explain it.
- Table 8 shows Flan-t5-xl rising slightly from 92.00 at temperature 0 to 92.43 at 0.3, so the statement that zero temperature is "always" the lowest (most accurate) does not hold for that row. Temperature near zero is given as 0.00001 in footnote 13 and 0.0001 in 7.4.2.
- Table 2 bolds the best value per column (e.g. MFC 63 for epistemic reasoning).
- Appendices 7.1–7.7 are covered in L3. Table 6 is not referred to in the main text on these pages.
