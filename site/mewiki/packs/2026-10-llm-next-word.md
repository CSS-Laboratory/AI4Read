# English pack · What does an LLM know when it predicts the next word?

C1/C2 only · 27 items · source post: https://khyang-lab.org/ai4read/2026-10-llm-next-word/

## Expressions

- **to be tantamount to** (C2): to have the same effect or meaning as something else, usually something stronger or worse. *A low loss on held-out text is not tantamount to understanding what the text means.*
- **to be predicated on** (C2): to be based on an assumption or condition, so that it fails if the assumption fails. *Xie's account of in-context learning is predicated on the model fitting its training distribution exactly.*
- **to be contingent on** (C2): depending on something else in order to be true or to happen. *Xie's result that prompting amounts to Bayesian inference is contingent on strong assumptions about the data, the model and the prompt.*
- **to stand or fall on** (C2): to succeed or fail completely depending on one particular thing. *The octopus argument stands or falls on what one takes meaning to be.*
- **to throw something into sharp relief** (C2): to make a difference or problem very easy to see by contrast. *Comparing bits per token with bits per character throws into sharp relief how misleading per-token loss can be.*
- **in and of itself** (C1): considered alone, without other evidence or factors. *An attention map is not, in and of itself, an explanation of what the model computes.*
- **to gloss over** (C2): to treat something important as if it were minor, or to avoid discussing it properly. *A single accuracy figure can gloss over how fragile a result is to small changes in the story.*
- **by the same token** (C2): for the same reason; following the same logic. *If a collapse after one small change counts against the model's theory of mind, then by the same token human failures on such changes count against people's.*
- **to be agnostic about** (C1): to take no position on a question because the evidence does not settle it. *The GPT-3 authors keep their terms agnostic about whether the model learns tasks from scratch or recognises patterns from training.*
- **to tease apart** (C1): to separate two things that are closely mixed so that each can be examined. *Mahowald and colleagues try to tease apart formal and functional competence.*
- **to stop short of** (C1): to come close to doing or saying something, but deliberately not do it. *Piantadosi and Hill stop short of saying that LLMs understand language as we do.*
- **to lend weight to** (C2): to make an idea or argument more convincing. *Strachan's human data lend weight to the idea that some perturbations are simply hard.*
- **to give someone pause** (C2): to make someone stop and think carefully, often with doubt. *A drop from 97.5% to 0% after one small change should give us pause.*
- **the burden of proof lies with** (C1): the person or side that must provide evidence for a claim is the one making it. *Ullman argues for a sceptical default: the burden of proof lies with those who claim the ability has emerged.*
- **the jury is still out (on)** (C2): people have not yet reached a decision or agreement about something. *The jury is still out on whether machines have theory of mind.*
- **to sidestep a question** (C2): to avoid dealing with a question or problem directly. *Shannon openly sidesteps the question of meaning: he calls it irrelevant to the engineering problem.*

## Sentence patterns

- **All-cleft for a limited claim** (C1): Start with 'All (that) … is/was …' to say that something tells us only this much and no more. *All that a low loss tells us is how many bits the model saves.*
- **Inversion after a restrictive adverbial** (C2): After 'only when', 'not until' or 'little' at the start of a clause, put the auxiliary before the subject ('Little did they expect …'). Formal writing and talks. *Only when the output layer is made cheap does the hidden layer become the bottleneck.*
- **Concession with 'adjective + as'** (C2): Front an adjective before 'as' (or 'though') to concede a point before the main claim: 'Smooth as it is, …' means 'Although it is smooth, …'. Formal. *Smooth as the loss curve is, it tells us little about when a particular skill appears.*
- **Nominalisation for academic register** (C2): Turn an event ('accuracy declines sharply') into a noun phrase so that it can be the subject of an evaluative verb ('casts doubt on'). *The sharp decline in accuracy under minor perturbations casts doubt on claims of robust theory of mind.*

## Fixes

- **comprise (no 'of')** (C1): ~~A transformer block comprises of an attention layer and a feed-forward layer.~~ → A transformer block comprises an attention layer and a feed-forward layer. 'Comprise' takes a direct object; use 'consist of' or 'is composed of' if you want 'of'. 'Is comprised of' is common in print but criticised by careful editors; avoid it in submissions.
- **stacked hedges** (C1): ~~These results may possibly suggest that the model might select a latent concept.~~ → These results suggest that the model, in effect, selects a latent concept. One well-chosen hedge is enough; piling up 'may', 'possibly' and 'might' sounds unsure rather than careful.
- **respectively** (C1): ~~Shannon and Kaplan respectively measured uncertainty.~~ → Shannon and Kaplan measured uncertainty in letters and in tokens, respectively. 'Respectively' pairs two lists item by item in the same order; it needs a second list to pair with.
- **dangling modifier** (C2): ~~Trained on English web text, our Japanese sentence costs far more bits per character.~~ → Trained on English web text, GPT-2 needs far more bits per character for our Japanese sentence. An opening participle phrase must describe the subject that follows. Either make the subject the thing that was trained ('…, GPT-2 needs …') or use a full clause ('Because GPT-2 was trained on English web text, …').

## Practice

- **Production drill**: Cover the expression, read the definition and the sentence with a gap, and say the expression aloud before you check. Recognising an expression is not the same as being able to use it.
- **90-second retell**: Explain one idea from the post aloud in 90 seconds, as if to a colleague, using one hedge, one concession and two expressions from this pack. Record it once a week.

## Paragraph to loop

What Shannon showed was that predicting text and compressing it are, in effect, the same problem. It is tempting to conclude that a model which predicts well must understand what it reads, but a low loss is not tantamount to understanding. Xie's account of in-context learning is predicated on the model fitting its training distribution exactly, an assumption that real models may not meet. Attention maps are suggestive, yet a map is not, in and of itself, an explanation. The theory-of-mind results should give us pause: accuracy collapses after small changes to the story. Yet people stumble on many of those changes too, and if a collapse counts against the model, then by the same token it should count against us. Even so, the burden of proof lies with those who claim the ability has emerged. Piantadosi and Hill stop short of saying that models understand as we do, and for now the jury is still out.

Targets: tantamount to, predicated on, in and of itself, give us pause, by the same token, the burden of proof lies with, stop short of, the jury is still out
