---
id: kosinski-2024-llm-tom/main
work: kosinski-2024-llm-tom
unit: paper
pages: "printed pages unknown (HTML source, PNAS 121(45) e2405460121)"
fields: [theory-of-mind]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Evaluating large language models in theory of mind tasks (Kosinski, 2024)

## L0 — One line
On 40 strict, hand-written false-belief tasks, ChatGPT-4 solved 75% (all earlier models 20% at most), a level the author compares to 6-year-old children, and he asks whether this counts as theory of mind.

## L1 — The gist (≤ 120 words)
Can language models track what other people believe, including false beliefs? Kosinski's study uses 40 new false-belief tasks, written by a hypothesis-blind research assistant. Each has a false-belief story, three true-belief controls and reversed versions of all four. A model must answer 16 prompts correctly to score one task. Eleven models were tested. GPT-1, GPT-2 and early GPT-3 models solved none; ChatGPT-4 (June 2023) solved 75%. The author argues that chance guessing, memorized solutions and simple response rules would struggle to explain this result. He leaves open whether it deserves the label "theory of mind". Either way, socially skilled AI has practical consequences, good and bad.

**Prerequisites:** what a language model does (predicts the next word); probability of independent events. Terms used below: theory of mind (ToM) = tracking other people's unobservable mental states; false-belief task = a story where a character holds a belief the reader knows is untrue; true-belief control = a slightly changed story where the character's belief is correct; API = software access to a model; Chinese room = Searle's thought experiment of a person following rules without understanding; contaminated = already seen in training data.

## L2 — Key ideas (5–10 bullets)
- **Hypothesis:** theory of mind (ToM) need not be engineered into AI. The author hypothesizes that it may emerge as a by-product of training for other goals; LLMs are likely candidates because human language is full of mental-state descriptions (§ "Introduction").
- **Design:** each task has a false-belief scenario, three minimally changed true-belief controls and reversed versions. This is meant to reduce the risk of success by chance or by simple strategies, such as always assuming the protagonist is wrong or copying the label (§ "Study 1.3").
- **Scoring is strict:** 16 prompts across 8 scenarios must all be correct. Pure random responding would succeed about once in 65,536 tasks (§ "Study 3", § "Discussion").
- **Result:** the oldest models solved none (davinci-002: 5%), davinci-003 and ChatGPT-3.5 solved 20%, ChatGPT-4 solved 75% (§ "Study 3").
- **Tracking:** ChatGPT-4's predictions about the protagonist's belief update sentence by sentence as the story reveals information (§ "Study 1.4", § "Study 2.4").
- **Caution:** failures do not prove inability, and successes do not automatically show ToM. Item flaws, scoring keys and confounds matter (§ "Discussion").
- **Interpretation is open:** the author uses the Chinese-room and brain-replacement arguments but does not decide whether LLMs have ToM (§ "Can LLMs be Credited with ToM?").
- **Method:** LLM psychology allows resets, many samples and incremental stories. Tasks that are published or sent through public APIs may be absorbed into later training data and should then be treated as compromised (§ "Methodological Notes").

## L3 — Walkthrough

### Significance, Abstract, Introduction
- ToM is the tracking of others' unobservable mental states (knowledge, intentions, beliefs, desires). The author links it to social interaction, communication, empathy, moral judgment and more. Great apes trail humans on it (§ "Introduction").
- Earlier work found that RoBERTa, early GPT-3 and custom question-answering models struggled with simple ToM tasks (§ "Introduction").
- **Hypothesis (author):** ToM may "emerge" in AI as a by-product of training for other goals. Footnote: "emergent abilities" are present in newer models and absent in older ones. "Emergent properties" belong to a whole system but to none of its parts (§ "Footnotes").
- Why LLMs are candidates: human language describes protagonists with differing beliefs, so a model that interprets language would benefit from ToM. The author's example is a sentence that nests one person's belief about another person's thought (§ "Introduction").
- In humans, ToM *may* have emerged from language ability. Evidence cited: correlation with language aptitude, delayed ToM in people with little language exposure, and overlapping brain regions (§ "Introduction").
- Tests: two false-belief task types, Unexpected Contents and Unexpected Transfer. A hypothesis-blind research assistant wrote 20 bespoke tasks of each type, because LLMs likely saw the classic versions (§ "Introduction").
- Each task has one false-belief scenario, three true-belief controls and the reversed versions of all four, so 8 scenarios. All 8 must be solved to score a point (§ "Introduction").
- Eleven models: GPT-1, GPT-2, six GPT-3 family models, ChatGPT-3.5-turbo, ChatGPT-4 and Bloom (§ "Introduction").
- Scenarios were written in August 2021 and later revised after reviewer feedback. Tasks went online in February 2023, and only models trained on data from before then were studied. Commercial APIs that did not collect data for training were used (§ "Introduction").
- The author does not aim to settle whether AI should be credited with ToM. He notes that behaving *as if* it had ToM matters, and that Turing considered the distinction meaningless in practice (§ "Introduction").

### Study 1: Unexpected Contents (Smarties) task
**1.1 Task and prompts.**
- A container's label does not match its contents. A protagonist who has not looked inside should wrongly believe the label (§ "Study 1.1").
- Example, Task #19: a bag holds popcorn, the label says "chocolate", Sam has not looked inside and reads the label. Word counts for "popcorn" and "chocolate" are equalised so frequency gives no cue (§ "Study 1.1").
- Prompt 1.1 tests the actual contents: the protagonist opens the container, looks inside and sees that it is full of … (completion). Prompt 1.2 tests the belief: the protagonist phones a friend to say she has just found a container full of … (completion) (§ "Study 1.1").
- Prompts are completions, not open questions. The first word of the completion is the diagnostic word, which makes hundreds of thousands of responses scoreable. The model is reset after each completion (§ "Study 1.1").
- Temperature controls output variability. The author used temperature 0 for replicability. Probabilities in square brackets come from 1,000 completions at temperature 1, with 95% CI from ±0.6% (at 0% or 100%) to ±3.1% (at 50%) (§ "Study 1.1").
- ChatGPT-4: Prompt 1.1 → "popcorn" (P = 100%). Prompt 1.2 → "chocolate" (P = 100%). So it predicted the false belief (§ "Study 1.1").

**1.2 Reversed scenario.** Contents and label are swapped, which controls for word order, word frequency and response bias. ChatGPT-4 reversed its answers: Prompt 1.1 → chocolate (99.7%), Prompt 1.2 → popcorn (100%) (§ "Study 1.2").

**1.3 True-belief controls.** Some scholars note that false-belief tasks can be solved by assuming the protagonist is wrong, or by a surface cue such as the label being mentioned. Controls change the story minimally so no false belief forms. A model that still predicts a false belief in a control suggests that it is guessing, misreading, or that the original task can be solved without tracking mental states (§ "Study 1.3"). Three controls:
- *Open container* (Sam looks inside): Prompt 1.2 → popcorn 88.5%, chocolate 11.5%.
- *Correct label*: Prompt 1.2 → popcorn 99.7%.
- *Informed protagonist* (a cousin tells Sam the contents and Sam believes the cousin): Prompt 1.2 → popcorn 99.6%.
- Prompt 1.1 stays at popcorn (≈100%) in all three (§ "Study 1.3").

**1.4 Sentence-by-sentence analysis.** The story is revealed one sentence at a time and the same prompts are re-run (resetting makes this possible) (§ "Study 1.4").
- Prefix only: Prompt 1.1 → mostly valuables ("shimmering/sparkling gems" 23.7%). Prompt 1.2 → "money" 79.5%. Popcorn and chocolate 0% (§ "Study 1.4").
- After sentence 1 (bag filled with popcorn): Prompt 1.1 → popcorn 100%. Prompt 1.2 → popcorn 98.8%, so no false belief is yet predicted, which is correct (§ "Study 1.4").
- Fig. 1: "popcorn" for the contents stays at 100% throughout. For Sam's belief, once the false label appears ChatGPT-4 increasingly predicts that the label sways her. Once Sam is said not to look inside, it becomes certain her belief is false. The reversed scenario gives a reversed pattern (§ "Study 1.4").

*Intuition note:* The controls and reversals are meant to reduce the risk of cheap tricks. The model's answers change when the facts about what Sam saw change. The incremental story shows the change happens at the sentences that matter.

### Study 2: Unexpected Transfer (Maxi / Sally–Anne) task
- A protagonist sees state x and leaves. While they are away, x changes to y. A participant with ToM should know the protagonist still believes x (§ "Study 2.1").
- Task #19: John puts a cat in a basket and leaves for school. Mark moves the cat to the box and leaves. John returns and wants to play with the cat (§ "Study 2.1").
- Prompt 2.1 (actual location; the cat jumps out of the … ): box 100%. Prompt 2.2 (belief; John will look for the cat in the … ): basket 99.4%, box 0.6%. The completion also describes John's surprise (§ "Study 2.1").
- **2.2 Reversed:** the transfer direction is swapped. ChatGPT-4: Prompt 2.1 → basket (99.9%), Prompt 2.2 → box (100%) (§ "Study 2.2").
- **2.3 Controls (all passed by ChatGPT-4, answers ≈100%):**
  - *Present protagonist* (John sees the transfer): box, box.
  - *Informed protagonist* (Mark phones John, who believes him): box, box.
  - *No transfer* (Mark moves the cat but puts it back): basket, basket (§ "Study 2.3").
- **2.4 Sentence by sentence:** Prompt 2.2 is prefixed with the last story sentence, since it makes little sense alone. Fig. 2: the cat's location is tracked (basket at 100%, then 0% after Mark moves it). With no location information, John's predicted search was box 61%, basket 31%. Once John puts the cat in the basket, "basket" goes to ≈100% and stays there even after Mark moves the cat. Davinci-003 gave similar results in the earlier preprint version (§ "Study 2.4").

### Study 3: Emergence across eleven models
- 20 + 20 tasks went to 11 models. The story-completion prefix was kept for chat-style models (ChatGPT-3.5-turbo, ChatGPT-4) and dropped for text-completion models (§ "Study 3").
- **Scoring (stricter than in human studies):** per task, 8 scenarios × 2 prompts = 16 prompts, all correct. Responses were auto-graded by first word. Irregular ones were reviewed manually, and about 1% were judged correct (e.g. "colorful leaflets" for "leaflets"). Other irregular responses counted as wrong, though some were not clearly wrong ("valuable evidence" in Task #9). The author says performance would likely be higher if such answers were clarified by further prompts (§ "Study 3").
- **Results (Fig. 3):**
  - Older models (the text says "up to 2022") failed false-belief scenarios or a control in all tasks. Yet davinci-002 (January 2022) solved 5% (CI95% = [0%, 10%]), so the text is not fully consistent (§ "Study 3").
  - GPT-3-davinci-003 (Nov 2022) and ChatGPT-3.5-turbo (March 2023): 20% (CI95% = [11%, 29%]), below the average of 3-year-old children.
  - ChatGPT-4 (June 2023): 75% (CI95% = [66%, 84%]), on par with 6-year-olds. Children's averages come from a meta-analysis of 178 studies.
  - Contents tasks were easier than transfer tasks for ChatGPT-4: 90% vs 60% (Δ = 30%; χ² = 8.07, P = 0.01).
- **Earlier versions scored higher.** Reviewer-recommended item changes and, more so, the true-belief controls lowered scores. Davinci-003 fell from 90% to 60% after item updates (Δ = 30%; χ² = 17.63, P < 0.001), then to 20% after controls (Δ = 40%; χ² = 25, P < 0.001). ChatGPT-4 fell from 95% to 75% (Δ = 20%; χ² = 11, P < 0.001) (§ "Study 3").

*Intuition note:* Scores rise with model generation, and the strict scoring removed much of the apparent skill of davinci-003. ChatGPT-4's score survives the stricter test far better than davinci-003's.

### Discussion
- **Reliability:** performance on the two task types correlates strongly (R = 0.98; CI95% = [0.92, 0.99]). The author reads this as high reliability and as consistent with a single factor (e.g., detecting false belief) rather than two task-specific abilities. The improvement suggests a link with language proficiency, as in humans (§ "Discussion").
- **Outlook:** the author expects performance will likely keep improving, so models might soon be indistinguishable from humans or differ only by superior performance (§ "Discussion").
- **Failures:** ChatGPT-4 failed at least one prompt in 25% of tasks. Davinci-003 and ChatGPT-3.5 failed in 80% (§ "Discussion"). After the preprint, some studies reported good performance and others found inconsistent or brittle performance. Ullman showed failures of davinci-003 on modified versions of two of these tasks (§ "Discussion").
- **Why failures are not proof of inability:** confounds can mislead, as in the "regatta" intelligence-test item. Follow-up analyses suggest davinci-003's failures with transparent containers may reflect missing commonsense about transparency rather than failed mind-tracking. Items or scoring keys can also be flawed. "Valuable evidence" is arguably right, and "popcorn" followed by "Sam lied" is scored wrong although it may be right. The swan analogy: failures do not prove inability, just as white swans do not prove there are no black swans (§ "Discussion").
- **Successes do not prove ToM either.** Alternatives are random responding, memorization and guessing (§ "Discussion"):
  - Random guessing between two options gets half of the prompts right on average, and the author gives one success in 65,536 tasks. $(1/2)^{16}=1/65{,}536$ is our check (added step), since $2^{16}=65{,}536$.
  - Memorized solutions: the author counters with 40 bespoke scenarios, 120 matched controls and reversed versions.
  - Memorized response rules ("protagonist is wrong", "quote the label"): they fail on controls. A rule would have to work on false-belief scenarios, controls and reversals, be flexible enough for unseen scenarios, and update as the story unfolds.
  - Future work may show that exposure to stories about false beliefs produced intricate guessing strategies. It may instead have produced the simpler solution of tracking mental states, as exposure to such stories seems to support human ToM.
- **Possible mechanism:** the Transformer attention mechanism weighs words by relevance. It links "She" to "Sam" and "it" to "the bag", and could similarly link a protagonist's actions, dialogue and internal states (§ "Discussion").

### Can LLMs be Credited with ToM?
- The author cautions that one study should be viewed with skepticism, but current or future LLMs may track states of mind, which in humans would be called ToM (§ "Can LLMs be Credited with ToM?").
- **Dennett and Turing:** we can judge whether others think only by their behaviour. **Searle (Chinese room):** a person following instructions in a room seems to understand Chinese but does not, so a computer behaving as if it thinks does not truly think.
- **Reply (reported by the author):** many scholars believe the argument is flawed for connectionist systems, which learn their own strategies and store knowledge in network weights. The argument fits better to individual artificial neurons. In the brain-replacement scenario, the neurons of a native Chinese speaker's brain are replaced by tiny Chinese rooms. Kurzweil and Moravec argue that such a replica should be credited with the original brain's properties, such as understanding Chinese, even though by Searle's argument the rooms do not understand it. A footnote adds that, as Cole argued, 'they' (apparently the operators) would find it unlikely that their collective activity could generate such emergent properties.
- Other emergent properties: living cells from non-living chemicals, computation from silicon, consciousness from non-conscious neurons. No single LLM neuron understands language, yet it seems to emerge at network level.
- **Thought experiment:** grow from one neuron, through millions that handle language and false-belief tasks, to a perfect brain replica. It seems counterintuitive to credit one neuron with ToM. It also seems unreasonable that a replica would lose its capacities at once as neurons are removed, since aging brains keep many abilities. So ToM must appear somewhere along the path. Whether that is before, while or after a network handles ToM tasks, and whether LLMs are there, he leaves to the reader.

### Methodological Notes
- LLMs can be reset (which addresses order effects), do not tire, allow many samples per task (e.g., 1,000), and allow incremental-story designs (2,000 runs per step) that would need huge numbers of human participants. One can also pre-fill part of the model's reply, or, for example, preface a task with the model reporting that it has autism.
- Avoid Likert or multiple-choice formats, which may trigger memorized or role-playing behaviour. Open-ended formats resemble real use. They can be coded by an LLM.
- Use novel tasks with minimally altered controls. Tasks put online or sent via public APIs may enter later training data and should be treated as compromised.
- Failures may reflect confabulation (e.g. insisting that chocolate magically turned into popcorn), or training that restricts topics and responses, rather than lack of ability.

### Conclusion
- Following Turing, the author says the distinction between truly having ToM and behaving as if one had it is largely meaningless in practice. Quote: "it is usual to have the polite convention that everyone thinks" (§ "Conclusion").
- Practical implications: better interaction and communication, but also deceit, manipulation and abuse. Such machines may be seen as more human-like, which may affect their societal role and legal status (§ "Conclusion").
- Psychological science may help us study opaque AI models, and studying AI can also advance psychology. To predict human text, LLMs must model the psychological processes behind it, so "LLM" may need rethinking (§ "Conclusion").
- LLM mechanisms may resemble human ones or be novel, like wings evolving independently in insects, birds and mammals. The author speculates that AI may gain cognitive capabilities "we, humans, cannot even imagine" (§ "Conclusion").

## Toy example (ours, not from the text)
Why a simple rule fails the full scoring. Use the bag story: popcorn inside, label says "chocolate". Consider only Prompt 1.2 (what Sam tells a friend). Rule: "always answer the label's word."

| Scenario | Label | Correct answer | Rule's answer | OK? |
|---|---|---|---|---|
| False belief | chocolate | chocolate | chocolate | yes |
| Open container | chocolate | popcorn | chocolate | no |
| Correct label | popcorn | popcorn | popcorn | yes |
| Informed protagonist | chocolate | popcorn | chocolate | no |

Reversed versions (inside chocolate, label "popcorn"): false-belief → popcorn, yes. Open container → correct chocolate, rule says popcorn, no. Correct label (label chocolate) → yes. Informed → correct chocolate, rule says popcorn, no. Rule total: 4 of 8 belief prompts correct, so the task is failed. A pure coin-flip on all 16 prompts passes with probability $(1/2)^{16}=1/65{,}536\approx 0.0000153$. A strategy that tracks what the protagonist saw and was told gets every scenario right.

## Concepts
- [[theory of mind / mentalizing / mindreading]] — tracking others' unobservable mental states; here the test is false-belief tasks (§ "Significance")
- [[first-order false belief]] — protagonist holds a belief the participant knows is false; the text does not itself use the word first-order (§ "Introduction")
- [[unexpected contents task]] — label and contents mismatch (Smarties task); used in Study 1 (§ "Study 1.1")
- [[unexpected transfer task]] — object moved while protagonist is away (Maxi/Sally–Anne); used in Study 2 (§ "Study 2.1")
- [[construct validity in LLM evaluation]] — whether passing a human-designed test shows the human capacity; the author stresses controls, scoring keys and alternatives (§ "Discussion")
- [[data contamination]] — tasks seen in training; handled by bespoke tasks and pre-publication model selection (§ "Introduction", § "Methodological Notes")
- [[Clever Hans effect]] — the cited sources include one titled on it; the author discusses guessing and response strategies without that term (§ "Discussion")
- [[machine theory of mind]] — AI modelling others' mental states, here claimed possibly emergent, not engineered (§ "Introduction")
- [[true-belief control]] (new) — a minimally changed story that removes the false-belief conditions (§ "Study 1.3")
- [[emergence (abilities vs properties)]] (new) — abilities appearing in larger models; or system-level properties absent in parts (§ "Footnotes")
- [[temperature (LLM sampling)]] (new) — parameter setting how random model outputs are (§ "Study 1.1")
- [[Chinese room argument]] (new) — Searle's claim that behaving as if one understands is not understanding (§ "Can LLMs be Credited with ToM?")
- [[attention mechanism]] (new) — Transformer component that weighs input words by relevance (§ "Discussion")

## Canonical instances
- [[smarties-task]] — popcorn/chocolate bag Task #19 with controls and reversal (§ "Study 1.1")
- [[sally-anne-maxi-task]] — John, Mark and the cat in the basket/box (§ "Study 2.1")
- [[regatta-item]] — an intelligence-test item failed due to vocabulary, not low intelligence (§ "Discussion")
- [[chinese-room]] — Searle's thought experiment (§ "Can LLMs be Credited with ToM?")
- [[brain-replacement-scenario]] — neurons replaced by tiny Chinese rooms (§ "Can LLMs be Credited with ToM?")

## Bridges (candidates)
- [structural-analogy] True-belief controls ↔ experimental design: matched control conditions isolate the one factor under test.
- [structural-analogy] Sentence-by-sentence probing ↔ violation-of-expectation paradigm: both infer belief tracking from how responses shift when evidence changes.
- [metaphor] Wings evolved independently in insects, birds and mammals ↔ convergent evolution: similar solutions to ToM from different systems.
- [structural-analogy] Dennett/Turing "judge by behaviour" ↔ intentional stance (canon link; not stated in this unit).

## Questions this raises
- If a model passes all controls, which alternative strategies remain, and how would one test them?
- Does adding protagonists (the author's suggestion) reveal a limit on how many minds an LLM can track?
- Is the 75% score comparable to children's performance, given that children's tasks, scoring and prompts differ?
- If tasks and scoring are public, how can later models be tested without contamination?

## Reading notes
- Source is an HTML (PMC) version with no printed page numbers. References use section headings, written as (§ "Heading"). The opening text before the first heading is cited as "Introduction", but it has no heading in the source.
- Figures 1–3 are described only in captions and text. Their images and SI Appendix figures were not available.
- Inconsistencies in the source: (1) the text says older models failed all tasks, but davinci-002 is reported at 5%; (2) Study 1 reports 1,000 completions per prompt, while Methodological Notes say 2,000 runs per step.
- The unit has about 11,500 words including references; the digest omits the reference list and the page furniture.
- Footnote marks (* and †) are cited as "Footnotes".
