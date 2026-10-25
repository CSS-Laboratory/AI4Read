# English pack · What Is a Hidden State? The Residual Stream, Read and Written

C1/C2 only · 28 items · source post: https://khyang-lab.org/ai4read/2026-10-residual-stream/

## Expressions

- **to bear out** (C2): to show that something said or believed is true. *The notebook bears out the claim that the writes add up to the stream, up to rounding, for entries 0 to 11 of GPT-2 small.*
- **to square with** (C2): to be consistent with something; to fit with it. *The idea that a reader sees only the sum squares with the toy, where the four shares of a read add up to the direct read, 5.*
- **to a first approximation** (C1): as a rough first description that ignores smaller details. *To a first approximation, a read is a dot product with the stream, once the norm in front of it is set aside; the norm adds a division, which is not linear.*
- **by construction** (C1): because of the way something was built or chosen, not because of a discovery. *In the toy, the two groups separate along the 135° direction by construction, because we chose the numbers.*
- **to carry over (to)** (C1): to continue to apply in a new situation. *Whether a result on GPT-2 small carries over to a trained Qwen3 model is untested here.*
- **to pin down** (C1): to identify or define something exactly. *It is hard to pin down what a library's hidden state is until you say which entry you mean: entries 0 to 11 are stream vectors in GPT-2 small, up to rounding, and the last is not.*
- **to take something at face value** (C1): to accept something as it appears, without asking whether it is more complicated. *We should not take a high probe score at face value: it shows information along a direction, not that the model uses it.*
- **a case in point** (C1): a good example of what has just been said. *Library names can mislead, and the last entry of a library's list is a case in point: it has been through the final norm, so it is not a stream vector.*
- **to hold up** (C1): to remain true or valid when tested. *The additivity check holds up for GPT-2 small, entries 0 to 11, but we did not run it on a trained Qwen3, Llama, Gemma or Mistral model.*
- **to be premised on** (C2): to be based on something taken as true at the start. *Comparing two models through each one's own dot products is premised on the stream having no privileged basis, which Elhage and colleagues assert for an idealised stream.*
- **to be at pains to** (C2): to make a special effort to do something, often to be clear or careful. *Olah and colleagues are at pains to say that their evidence for universality is, so far, anecdotal.*
- **to fall out of** (C2): to follow naturally as a result of something. *Steering as a translation falls out of the algebra: every score shifts by the same amount, u dot v.*
- **a matter of convention** (C1): something decided by agreement, not by necessity. *Giving a direction length one is a matter of convention in this post, chosen so that scores from different arrows can be compared.*
- **to be on firm ground** (C1): in a safe position, with good evidence to support what you say. *With the arithmetic of a sum we are on firm ground; with the claim that concepts are directions in a language model’s stream, we are not.*
- **in lockstep** (C1): moving or changing together, at exactly the same time and in the same way. *A steering push shifts every score in lockstep: each one moves by the same amount, u dot v.*
- **to hinge on** (C1): to depend completely on one particular thing. *Whether a steering push changes behaviour as intended hinges on how a real model responds, which the algebra does not say.*
- **to be tantamount to** (C2): to have the same effect or meaning as something else, usually something stronger or worse. *To say that a high probe score proves the model uses a direction would be tantamount to confusing seeing with doing.*

## Sentence patterns

- **Fronted wh-clause object (contrast)** (C2): Put a 'what' clause first, as the object of a verb that comes later, to make it the topic: 'What a score means, the algebra does not say.' The rest keeps normal subject-verb order, and no pronoun is added. It sets what is settled against what is not. *What a score means, or whether a push changes behaviour, the algebra does not say.*
- **Perfect participle clause** (C1): 'Having + past participle' shows that one action was finished before the next. The subject of the main clause must be the one who did the first action. *Having added the four writes to the embedding, we get the stream after two blocks, (4, 2).*
- **Mandative subjunctive** (C2): After words like essential, important, insist or recommend, formal English uses the bare base form: 'that the check be run'. British English also allows 'should be run'; 'is run' is the informal option. *The post recommends that the additivity check be run on any model before its additivity is trusted.*
- **Inversion with 'Should' (formal conditional)** (C2): 'Should + subject + verb' replaces 'If the check should fail' in a formal, slightly unlikely condition. Do not add 'if'. *Should the additivity check fail with the hooks placed correctly, the identity does not hold for that model.*

## Fixes

- **whether (not 'if')** (C1): ~~The toy shows that cancellation is possible; it leaves open the question of if real models cancel writes.~~ → The toy shows that cancellation is possible; it leaves open the question of whether real models cancel writes. After a noun ('the question of') or a preposition ('depends on'), and when the clause is the subject, use 'whether', not 'if'. 'If' belongs to conditions and to casual speech after verbs such as ask or wonder.
- **however (not a conjunction)** (C1): ~~The sum is exact in the account Elhage and colleagues give, which ignores layer normalisation, however a real model adds a norm.~~ → The sum is exact in the account Elhage and colleagues give, which ignores layer normalisation; however, a real model adds a norm. 'However', 'therefore' and 'moreover' are adverbs. A comma alone cannot join two main clauses with them (a comma splice). Use a full stop or a semicolon before the adverb and a comma after it, or use a real conjunction such as 'but' or 'although'.
- **compare like with like ('those in')** (C1): ~~Every coordinate differs, but the dot products in model B are the same as model A.~~ → Every coordinate differs, but the dot products in model B are the same as those in model A. Both sides of a comparison must be the same kind of thing. Dot products are compared with dot products, not with a model. 'Those in', 'those of', 'that of' and 'the one in' stand in for the repeated noun.
- **imply vs infer** (C1): ~~A high probe score infers nothing about use; from it we can only imply that information is present along a direction.~~ → A high probe score implies nothing about use; from it we can only infer that information is present along a direction. Evidence or a statement implies something (it suggests it); a person infers it (draws the conclusion). Data cannot infer, and a reader does not imply a conclusion by reading.

## Practice

- **Three-step retell**: Without looking, explain in two minutes how a hidden state is built, using three expressions from this pack: start from the embedding, add each write, then say what a reader can and cannot hear.
- **Shadow, then test yourself**: Shadow the loop paragraph twice, then close it and say in three sentences what the notebook bears out and what it leaves untested.

## Paragraph to loop

Every attention and MLP part adds its write to one shared list, so the stream is a running sum. In the toy this is true by construction, and the notebook bears it out on GPT-2 small, up to rounding. To a first approximation, a read is a dot product with that sum, setting aside the norm in front of it, whose division is not linear. Names can mislead: the last entry of a library's list is a case in point, because it has been through the final norm, so it should not be taken at face value. The claim that concepts are directions in a model's stream hinges on tests that none of the three sources runs, so we are on firmer ground with the arithmetic than with the interpretation. A push moves every score in lockstep, but to say that a high score shows the model uses the direction would be tantamount to confusing seeing with doing.

Targets: To a first approximation, by construction, bears it out, a case in point, at face value, hinges on, on firmer ground, in lockstep, tantamount to
