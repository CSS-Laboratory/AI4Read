# English pack · What does an LLM know when it predicts the next word?

Schema /2 (passage-centred) · C1/C2 only · source post: https://khyang-lab.org/ai4read/2026-10-llm-next-word/

## Passage

0. A language model is trained to do one job: guess the next piece of text.
1. It is scored by its loss, which measures how closely those guesses match real text.
2. What it knows comes in four layers, from the most certain to the most contested.
3. First come bits about text, which are measurable.
4. That is knowledge in Shannon's sense, and his theory sidesteps the question of meaning.
5. Next is structure, such as grammar, and that is well supported.
6. Whether the model grasps meaning stands or falls on what you take meaning to be.
7. **As for minds, the jury is still out.**
8. **Many tests are passed, but small changes often break the result, which should give us pause.**
9. **Yet people fail some of those changes too, so if a failure counts against the model, then by the same token it counts against us.**
10. **A low loss is not tantamount to understanding, and in and of itself it cannot tell you what kind of knowledge the model has.**
11. To tease apart the kinds, you have to change the test in small ways and see what breaks.

184 words · core (bold) 73 words · audio 80.0 s, Kokoro bm_george (en-GB), 155 wpm

### Gist

- What four layers of knowledge does the speaker describe, and which is the most contested? → Bits about text, structure such as grammar, meaning, and minds. The question of minds is the most contested.
- What does a low loss not tell you, and how can you find out more? → It does not tell you what kind of knowledge the model has. To find out, you change the test in small ways and see what breaks.

### Retell

In 2-3 sentences, explain to a colleague why a low loss does not settle what an LLM knows.

Must use: to tease apart, in and of itself, the jury is still out (on)

Model answer: A low loss, in and of itself, only tells you how much a model knows about text, not what kind of knowledge it is. To tease apart the kinds, you change the test in small ways and see what breaks. On whether models have anything like a mind, the jury is still out.

## Expressions

- **to stand or fall on** (C2): to succeed or fail completely depending on one particular thing. In the passage: “stands or falls on”. Second context: *The validity of a surrogate-labelling study stands or falls on the quality of the human-coded sample it is checked against.*
- **the jury is still out (on)** (C2): people have not yet reached a decision or agreement about something. In the passage: “the jury is still out”. Second context: *On whether these labels transfer to other platforms, the jury is still out.*
- **to give someone pause** (C2): to make someone stop and think carefully, often with doubt. In the passage: “give us pause”. Second context: *An agreement score that drops sharply on a second platform should give us pause.*
- **by the same token** (C2): for the same reason; following the same logic. In the passage: “by the same token”. Second context: *If we discount a classifier because it was tuned on its test set, then by the same token we should discount a hand-tuned dictionary.*
- **to be tantamount to** (C2): to have the same effect or meaning as something else, usually something stronger or worse. In the passage: “tantamount to”. Second context: *Publishing only the runs that worked would be tantamount to hiding the ones that failed.*
- **in and of itself** (C1): considered alone, without other evidence or factors. In the passage: “in and of itself”. Second context: *A high agreement score is not, in and of itself, evidence that the codebook is valid.*
- **to tease apart** (C1): to separate two things that are closely mixed so that each can be examined. In the passage: “tease apart”. Second context: *It is hard to tease apart the effect of the platform from the effect of the topic.*
- **to sidestep a question** (C2): to avoid dealing with a question or problem directly. In the passage: “sidesteps the question”. Second context: *The report sidesteps the question of causation by describing associations only.*

## Patterns

- **Double superlative range (from the most X to the most Y)** (C1): Mark the two ends of a scale with parallel superlatives: 'from the most certain to the most contested'. It lets you list items in order in a single phrase. In the passage: “from the most certain to the most contested”. Second context: *The studies range from the most carefully controlled to the most loosely designed.*
- **As for + topic** (C1): 'As for X, ...' moves to a new topic in the middle of a talk and signals that what follows is about X alone. Spoken and written, neutral. In the passage: “As for minds”. Second context: *As for the second dataset, we have not yet checked its labels.*
- **Sentential relative clause (, which ...)** (C1): After a comma, 'which' can refer to a whole preceding clause, not just one noun: 'small changes often break the result, which should give us pause'. 'That' cannot be used this way. In the passage: “which should give us pause”. Second context: *Agreement dropped on the new sample, which suggests that the codebook is too loose.*

## Fixes

- **no article with uncountable abstract noun** (C1), sentence 4: ~~That is a knowledge in Shannon's sense, and his theory sidesteps the question of meaning.~~ → That is knowledge in Shannon's sense, and his theory sidesteps the question of meaning. 'Knowledge' is uncountable: no 'a' and no plural. Say 'knowledge' or 'a piece of knowledge'.
- **whether, not if, in a subject clause** (C1), sentence 6: ~~If the model grasps meaning stands or falls on what you take meaning to be.~~ → Whether the model grasps meaning stands or falls on what you take meaning to be. A clause that is the subject of a sentence and expresses a yes/no question starts with 'whether', not 'if'.
- **which, not that, after a comma** (C1), sentence 8: ~~Many tests are passed, but small changes often break the result, that should give us pause.~~ → Many tests are passed, but small changes often break the result, which should give us pause. A comment on a whole clause needs ', which'. 'That' only starts a defining relative clause, with no comma.
- **no inversion in an embedded question** (C1), sentence 10: ~~A low loss is not tantamount to understanding, and in and of itself it cannot tell you what kind of knowledge has the model.~~ → A low loss is not tantamount to understanding, and in and of itself it cannot tell you what kind of knowledge the model has. After 'what kind of ...' inside a statement, keep statement order (subject then verb): 'what kind of knowledge the model has'.

## Practice

- **Shadow the core first**: Loop the four core sentences until you can say them without the text; the expressions will come with them, already in a natural rhythm.
