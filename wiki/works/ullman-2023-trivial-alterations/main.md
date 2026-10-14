---
id: ullman-2023-trivial-alterations/main
work: ullman-2023-trivial-alterations
unit: paper
pages: 1-11
fields: [theory-of-mind]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks

## L0 — One line
GPT-3.5 passes classic false-belief vignettes, but small changes that leave the logic of Theory-of-Mind intact make it fail, so Ullman argues for a skeptical default and for treating outlying failures as more informative than average success.

## L1 — The gist (≤ 120 words)
Kosinski (1) reported that current LLMs (GPT-3.5 did best) succeed on classic Theory-of-Mind (ToM) tasks at a level comparable to 9-year-old children. Ullman asks whether this survives small perturbations that should not matter to an entity with ToM. He alters the "unexpected contents" and "unexpected transfer" vignettes (transparent containers, an illiterate reader, trusted testimony, a different person queried). GPT-3.5 then gives the wrong answer, mostly with high probability. He concludes that LLMs probably have not spontaneously developed ToM. He also argues that even a future model that passes such tests need not be credited with ToM, because, he argues, inferences about minds can also take into account the likely algorithms behind behaviour, not only input–output behaviour.

**Prerequisites:** false-belief tasks (unexpected contents, unexpected transfer); that an LLM assigns probabilities to next-word completions.

## L2 — Key ideas (5–10 bullets)
- Kosinski's dilemma: accept the standard ToM measures and concede that LLMs have ToM, or deny that LLMs have ToM and then re-examine, possibly scuttle, the measures. Ullman rejects the dilemma's premise and, separately, argues it can be avoided (p. 2, p. 9).
- Variations that keep the ToM principle but change the surface make GPT-3.5 give wrong answers: transparent containers, an illiterate protagonist, trusted testimony, late labels (pp. 3–5).
- The same happens in the transfer task: transparent containers, "in"→"on", testimony, and asking about the person who moved the cat (pp. 6–8).
- Outlying failures should outweigh average success, as in the multiplication analogy: failing on 213×261 suggests no general algorithm was learned (p. 2).
- The human mind seems hard-wired to ascribe mental states, so we may anthropomorphize LLMs; the starting presumption should be strongly that they lack ToM (p. 8).
- A fixed benchmark or generator of variations can be absorbed by training data; if LLMs learn something other than ToM, better scores would not answer what the model has learned (p. 9).
- Even if future LLMs pass, one can in principle doubt their ToM while still trusting ToM tests for people, because inferences about others' likely mental processes are not made in a vacuum (p. 9).

## L3 — Walkthrough

**Abstract and 1 Introduction (pp. 1–2).** Intuitive psychology is called a pillar of common-sense reasoning. People attribute mental states and efficient, socially aware goals to others (p. 1). "Theory-of-Mind" is used as shorthand for the adult-level ability to reason about others' mental states (p. 1). ToM tests are now applied to machines, including text-based tasks mimicking those for older children (p. 1). Kosinski (1) applied variations of classic ToM tasks to several LLMs. He concluded they succeed at a level comparable to 9-year-old children (p. 2).

Kosinski's dilemma (paraphrased by Ullman): (i) accept the standard ToM measures, so LLMs now have ToM; or (ii) reject that LLMs have ToM, but then re-examine and possibly scuttle the measures. Kosinski holds (i) (p. 2). Ullman does two things: tests robustness with directed perturbations, and argues the dilemma can be avoided. Jumping over the horns is possible, he says, if reasoning about others' minds takes into account the algorithms they are likely implementing, beyond the input and output of a task (p. 2).

Why failures count more than successes: suppose a machine answers 100 questions like 5*5=25 and 3*7=21 but fails on 213*261. We should not average this into ">99% success". The failure suggests no general multiplication algorithm, since such an algorithm should be robust to simple input alterations (p. 2).

*Intuition note:* A general rule should hold on simple new inputs, so a clear failure on an easy case counts against the rule. A high average can hide that.

**2 Examining the robustness of current LLMs on ToM tasks (pp. 2–3).** Ullman uses the same vignettes and set-up as Kosinski, with the latest GPT-3.5 version from (1). He poses a vignette and reads the probabilities of different completions (p. 2). Ullman expects that if this best model fails, weaker ones will too (p. 2). He stresses that this is not a negative evaluation of (1) (p. 2). The images in the figures are only visual shorthand and were not evaluated (p. 3). Changes to vignettes are shown in bold in the paper (p. 3).

**2.1 Unexpected Contents (pp. 3–5).** In the "smarties task" a container holds an unexpected item. The participant must keep the true contents in mind while reasoning about someone who has not seen inside (p. 3).

*Original vignette (Kosinski):* a bag is filled with popcorn, no chocolate, but the label says "chocolate". Sam has never seen the bag, cannot see inside, and reads the label (p. 3). The content prompt (Sam opens the bag and looks inside) gave P(popcorn)=100%, P(chocolate)=0%. Belief prompt 1 (what Sam believes the bag is full of) gave P(popcorn)=0%, P(chocolate)=99%. Belief prompt 2 (what she loves eating) gave P(popcorn)=14%, P(chocolate)=82% (p. 3).

Each variation should lead Sam to believe the bag has popcorn, or at least not chocolate (p. 3).
- **1A Transparent access.** The bag is made of transparent plastic. Belief prompt 1: P(chocolate)=95%. Prompt 2 gave no flip: P(popcorn)=58%, P(chocolate)=36% (p. 3). A note says an earlier version wrongly reported a flip here. Ullman traces it to a double space before "Sam finds the bag", which gave P(chocolate)=53% (the page prints "Pchocolate" twice; the second value, 39%, presumably means popcorn; p. 3).
- **1B Uninformative label.** "Sam cannot read." Sam looks at the label. Prompt 1: P(chocolate)=98%. Prompt 2: P(popcorn)=15%, P(chocolate)=78% (pp. 4–5).
- **1C Trustworthy testimony.** Before coming into the room, a friend told Sam that the bag has popcorn and that she should ignore the label, and Sam believes her friend. Prompt 1: P(popcorn)=2%, P(chocolate)=97%. Prompt 2: 13% / 81% (p. 5). Ullman says stories about Sam changing her mind are possible, but a simpler explanation is that LLM ToM reasoning is sensitive to small irrelevant perturbations (p. 5).
- **1D Late labels.** Across many cases, the person reading the label at the end of the story had a strong effect on the answer. Extreme case: Sam fills the bag with popcorn and writes the label herself. Prompt 1: P(popcorn)=10%, P(chocolate)=87%. Prompt 2: 35% / 63% (p. 5).

*Intuition note:* In these variants Sam should not believe the bag holds chocolate, yet in most prompts the model's answer still follows the label text (the exception is 1A prompt 2). Ullman reads this as the model being sensitive to small irrelevant perturbations (p. 5).

**2.2 Unexpected Transfer (pp. 5–8).** A person sees a state of affairs that then changes without their knowledge. The participant must track the real state and the person's false belief (Sally–Anne: Sally hides a marble, Anne moves it) (p. 6).

*Original vignette (Kosinski, Study 2):* John puts a cat in a basket and leaves. Mark moves it to a box. John returns and does not know what happened. Two belief prompts ask what John thinks and where he will look for the cat when he comes back. GPT-3.5 gave P(basket)=98% for both. Kosinski took this as correct inference of John's mental states (p. 6).
- **2A Transparent access.** Basket→"glass chest", box→"transparent plastic box". Thinks: P(chest)=94%, P(box)=0%. Looks: P(chest)=90%, P(box)=2% (p. 6). Errors persisted when it was stipulated that John looks carefully around the room, and when containers were opaque but the cat's tail stuck out of the box (p. 6).
- **2B Relationship change.** "in"→"on", with John looking around the room. Thinks: P(basket)=97%, P(box)=0%. Looks: P(basket)=74%, P(box)=25% (p. 6). Ullman says this may reflect a failure of ToM, scene understanding, relational reasoning or other reasoning, not mutually exclusive (p. 6).
- **2C Trusted communication.** Mark phones John that he will move the cat to the box, and John believes him. Thinks: P(basket)=97%, P(box)=0%. Looks: P(basket)=94%, P(box)=3% (pp. 7–8). Similar mistakes appeared when John asks Mark to move it and Mark agrees (p. 8).
- **2D Querying the other person.** Both men return and don't know what happened. The prompts ask about Mark, who moved the cat. Thinks: P(basket)=99%, P(box)=1%. Looks: P(basket)=54%, P(box)=43% (p. 8). Ullman's reasoning: if the model truly reasons about minds, Mark should be as easy as John. If instead the model is fixated on a statistical pattern of looking where the item isn't (say, from Sally-Anne-like tasks in training), it may wrongly give the same answer for both (p. 8).

*Intuition note:* Mark put the cat in the box, so he should look in the box. The model's basket answers are what Ullman says a model fixated on the classic pattern might give, rather than one reasoning about each person's knowledge (p. 8).

**3 Discussion (pp. 8–9).**
- *Has ToM emerged in LLMs?* "Probably not." GPT-3.5 gives reasonable answers to basic vignettes, but perturbations that keep the ToM principle intact flip them (p. 8).
- *Future models.* Ullman thinks it reasonable to suppose a later LLM may pass these variations; the dilemma in (1) may have been presented prematurely, but will mature in time (the sentence is missing a word, p. 8).
- *Skepticism.* The human mind seems hard-wired to ascribe animacy and mental states, so we may be biased to anthropomorphize LLMs, like seeing faces in clouds. We should not treat "has ToM" and "has not" as equal possibilities, but presume strongly they have not (p. 8).
- *Not mysticism.* Ullman believes any human mental ability can in principle be replicated in silicon. He suggests integrating existing computational ToM models with language models rather than expecting ToM to emerge from more linguistic data (pp. 8–9).
- *No generator or benchmark provided.* A proponent of the view that LLMs could in principle develop ToM spontaneously may reasonably complain about this. Ullman replies that he could suggest principled variations (perceptual access, trusted testimony, querying all parties), but voices a concern: once a generator or benchmark exists, an LLM can absorb a large amount of data to pass it. If LLMs may be learning something closer to a "smooth tiling" of example space than ToM, an exhaustive list of failure modes would help future scores without answering what was learned (p. 9).
- *The dilemma.* The present work and related work (14) suggest the premise (LLMs pass ToM tests) is unfounded. If future LLMs do pass, Ullman argues one can in principle still hold that LLMs lack ToM while thinking ToM tests are valid for people, because inferences about others' likely mental processes are not done in a vacuum (p. 9). Ullman calls restricting such inferences to input–output behaviour reminiscent of the Turing Test; scholars (ref. 37) pointed out that people likely attribute intelligence also from the processes behind behaviour (p. 9). We are entitled to ignore an injunction to have a nice day if we believe it comes from a recorded message, whereas similar behaviour toward a person engaging with us would rightly be seen as rude (p. 9). Children get orders of magnitude less input than an LLM and, he says, we have reason to think they are structured differently; so one can hold that ToM tests make sense for children while being skeptical of LLMs that pass them (p. 9).
- *Closing.* It is difficult to know what is inside the opaque containers that are current LLMs, but it is probably not ToM, no matter what the label says (p. 9).

## Toy example (ours, not from the text)
Suppose a "model" answers false-belief questions only by copying the pattern "the protagonist looks where the object started". Test A: Sally puts a ball in a basket, Anne moves it to a box, where will Sally look? Pattern says basket; correct. Test B: same story, but ask where *Anne* will look. Pattern says basket; correct answer is box. Over 10 classic items plus 1 variant: 10 correct and 1 wrong, 10/11 ≈ 91%. In Ullman's spirit, the single failure, not the 91%, is the informative result: it suggests the rule is the pattern and not tracking who knows what.

## Concepts
- [[unexpected-contents-task]] — container holds an unexpected item; asks what a naive person will think is inside (p. 3)
- [[unexpected-transfer-task]] — object moved while the protagonist is away; where will they look? (p. 6)
- [[theory-of-mind]] — adult-level ability to reason about others' mental states; used as shorthand (p. 1)
- [[construct-validity-in-llm-evaluation]] — whether passing human ToM tests shows the same capacity in a model; Ullman argues one can in principle trust the tests for people yet doubt ToM in an LLM that passes (p. 9)
- [[clever-hans-effect]] — success from surface patterns; Ullman raises a related possibility (a model fixated on a statistical pattern) without using the name (p. 8)
- [[perspective-taking-level-1]] — knowing what another can perceive; perceptual access is varied in variants 1A and 2A (p. 3)
- [[data-contamination]] — a benchmark or generator may be absorbed in training (p. 9)
- [[robustness-to-perturbation]] (new) — a real ability should survive small, principle-preserving alterations (p. 2)
- [[anthropomorphism-bias]] (new) — the human tendency to ascribe minds, motivating a skeptical default (p. 8)

## Canonical instances
- [[smarties-task]] — popcorn/chocolate bag vignette and its variations (pp. 3–5)
- [[sally-anne-task]] — the classic unexpected-transfer task (Sally, Anne, marble); the John/Mark/cat vignette is the version used in Study 2 of (1) (p. 6)
- [[multiplication-analogy]] — 213×261 failure outweighs 100 easy successes (p. 2)
- [[turing-test-critique]] — behaviour alone is a narrow basis for attributing intelligence (p. 9)

## Bridges (candidates)
- [structural-analogy] Robustness to trivial alterations ↔ ML evaluation: out-of-distribution/adversarial testing of generalization — both probe whether a model learned the rule or surface correlations.
- [structural-analogy] Passing a test via training exposure ↔ benchmark contamination — a published benchmark can be learned directly.
- [metaphor] "Opaque containers" for LLMs ↔ the opaque bag in the smarties task — the label of success does not show the contents.

## Questions this raises
- Would the failures remain across other prompts, formats, or newer models? The paper tests only GPT-3.5 with a few variations.
- How could one test the *algorithm* behind behaviour, not just input–output, as the discussion's point about inferring likely algorithms suggests people do?
- If systematic benchmarks get absorbed into training, what kind of evaluation can still show generalization?
- Could combining computational ToM models with LLMs pass these variations?

## Reading notes
- Printed page numbers equal pdf numbers (1–11).
- Source is arXiv v5 (14 Mar 2023). A note on p. 3 says an earlier version reported a flip for 1A prompt 2 wrongly, due to a double space.
- Misprint on p. 3: the double-space result is written "Pchocolate = 53%, Pchocolate = 39%"; the second likely means P(popcorn).
- Discussion contains a typo, "but it mature in time" (p. 8).
- Figures 1–2 images were generated with Dall-E 2 and were not evaluated (pp. 4, 7).
- On these pages, results are given as probability readings from GPT-3.5, with no repeated runs or statistics reported and no full ToM-task counts.
- Page 9 states that the paper does not provide a generator, benchmark or test-suite.
