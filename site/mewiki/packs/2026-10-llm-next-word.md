# English pack · What does an LLM know when it predicts the next word?

C1/C2 only · 27 items · source post: https://khyang-lab.org/ai4read/2026-10-llm-next-word/

## Expressions

- **to be tantamount to** (C2): to have the same effect or meaning as something else, usually something stronger or worse. *A low loss on held-out text is not tantamount to understanding what the text means.*
- **to be predicated on** (C2): to be based on an assumption or condition, so that it fails if the assumption fails. *Xie's account of in-context learning is predicated on the model fitting its training distribution exactly.*
- **to be contingent on** (C2): depending on something else in order to be true or to happen. *Whether prompting resembles Bayesian inference is contingent on strong assumptions about the training data.*
- **to stand or fall on** (C2): to succeed or fail completely depending on one particular thing. *The octopus argument stands or falls on what one takes meaning to be.*
- **to throw something into sharp relief** (C2): to make a difference or problem very easy to see by contrast. *Comparing bits per token with bits per character throws the tokenizer's bias into sharp relief.*
- **in and of itself** (C1): considered alone, without other evidence or factors. *An attention map is not, in and of itself, an explanation of what the model computes.*
- **to gloss over** (C1): to treat something important as if it were minor, or to avoid discussing it properly. *A single accuracy figure can gloss over how fragile a result is to small changes in the story.*
- **by the same token** (C1): for the same reason; following the same logic. *If a collapse after one small change counts against the model, then by the same token human failures on such changes count against people.*
- **to be agnostic about** (C1): to take no position on a question because the evidence does not settle it. *The GPT-3 authors are agnostic about whether the model learns tasks from scratch.*
- **to tease apart** (C1): to separate two things that are closely mixed so that each can be examined. *Mahowald and colleagues try to tease apart formal and functional competence.*
- **to stop short of** (C1): to come close to doing or saying something, but deliberately not do it. *Piantadosi and Hill stop short of saying that LLMs understand language as we do.*
- **to lend weight to** (C1): to make an idea or argument more convincing. *Strachan's human data lend weight to the idea that some perturbations are simply hard.*
- **to give someone pause** (C1): to make someone stop and think carefully, often with doubt. *A drop from 97.5% to 0% after one small change should give us pause.*
- **the burden of proof lies with** (C1): the person or side that must provide evidence for a claim is the one making it. *Ullman thinks the burden of proof lies with those who claim the ability has emerged.*
- **the jury is still out (on)** (C1): people have not yet reached a decision or agreement about something. *The jury is still out on whether machines have theory of mind.*
- **to sidestep a question** (C1): to avoid dealing with a question or problem directly. *Shannon deliberately sidesteps the question of meaning.*

## Sentence patterns

- **Cleft sentence for focus** (C1): Put the new or important information after 'What … was' or 'It is … that' to control where the listener's attention falls.. *What Shannon showed was that prediction and compression are the same problem.*
- **Inversion after a restrictive adverbial** (C2): After 'only when', 'not until', 'rarely' or 'not only' at the start of a clause, put the auxiliary before the subject. Formal writing and talks.. *Only when the output layer is made cheap does the hidden layer become the bottleneck.*
- **Concessive clause before the claim** (C1): Grant the opposing point first in a subordinate clause, then make your point in the main clause.. *While it is true that the loss falls smoothly with scale, it tells us little about when a particular skill appears.*
- **Nominalisation for academic register** (C2): Turn an event ('accuracy declines sharply') into a noun phrase so that it can be the subject of an evaluative verb ('casts doubt on').. *The sharp decline in accuracy under minor perturbations casts doubt on claims of robust theory of mind.*

## Fixes

- **comprise (no 'of')** (C1): ~~A transformer block comprises of an attention layer and a feed-forward layer.~~ → A transformer block comprises an attention layer and a feed-forward layer. 'Comprise' takes a direct object; use 'consist of' or 'is composed of' if you want 'of'.
- **stacked hedges** (C1): ~~These results may possibly suggest that the model might select a latent concept.~~ → These results suggest that the model selects a latent concept. One well-chosen hedge is enough; piling up 'may', 'possibly' and 'might' sounds unsure rather than careful.
- **respectively** (C2): ~~GPT-2 cost respectively 5.6 and 4.8 bits per token on the English and Japanese sentences.~~ → GPT-2 cost 5.6 and 4.8 bits per token on the English and Japanese sentences, respectively. Put 'respectively' at the end, after two parallel lists in the same order.
- **dangling modifier** (C2): ~~Trained on English web text, Japanese costs GPT-2 far more bits per character.~~ → Because GPT-2 was trained on English web text, Japanese costs it far more bits per character. An opening participle phrase must describe the subject that follows; here it was Japanese, not GPT-2, that seemed to be 'trained'.

## Practice

- **Production drill**: Cover the expression, read the definition and the sentence with a gap, and say the expression aloud before you check. Recognising an expression is not the same as being able to use it.
- **90-second retell**: Explain one idea from the post aloud in 90 seconds, as if to a colleague, using one hedge, one concession and two expressions from this pack. Record it once a week.

## Paragraph to loop

What Shannon showed was that predicting text and compressing it are, in effect, the same problem. It is tempting to conclude that a model which predicts well must understand what it reads, but a low loss is not tantamount to understanding. Xie's account of in-context learning is predicated on the model fitting its training data exactly, so whether prompting resembles Bayesian inference is contingent on assumptions that real models may not meet. Attention maps are suggestive, yet a map is not, in and of itself, an explanation. The theory-of-mind results should give us pause: accuracy collapses after small changes to the story. By the same token, people stumble on some of those changes too, so the burden of proof lies with whoever claims more. Piantadosi and Hill stop short of saying that models understand as we do, and for now the jury is still out.

Targets: What Shannon showed was, tantamount to, predicated on, contingent on, in and of itself, give us pause, By the same token, the burden of proof lies with, stop short of, the jury is still out
