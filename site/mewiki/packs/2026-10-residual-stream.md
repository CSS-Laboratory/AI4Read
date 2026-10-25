# English pack · What Is a Hidden State? The Residual Stream, Read and Written

Schema /2 (passage-centred) · C1/C2 only · source post: https://khyang-lab.org/ai4read/2026-10-residual-stream/

## Passage

0. **On our reading, every attention and MLP part adds its write to one shared list, so a language model's hidden state is a running sum.**
1. In our toy that is true by construction, and a notebook on GPT-2 small bears it out, up to rounding.
2. Names can mislead: the library's last entry, having been through the final norm, is a case in point, and is not to be taken at face value.
3. **To a first approximation, norm aside, a read is a dot product with that sum, so it splits into one share per writer, and a writer at right angles goes unheard.**
4. A linear probe is such a read, and a high score shows only that information is present.
5. **To say the model therefore uses it would be tantamount to confusing seeing with doing.**
6. A steering push shifts every score in lockstep.
7. **What a score means, or whether a push changes behaviour, the algebra does not say.**
8. Whether concepts are directions in a trained language model's stream hinges on tests that our three sources do not give, so we are on firm ground with the arithmetic, not the interpretation.

190 words · core (bold) 86 words · audio 80.2 s, Kokoro bm_george (en-GB), 155 wpm

### Gist

- Why is a model's hidden state described as a running sum? → Because every attention and MLP part adds its write to one shared list, so the state at any point is the starting list plus every write made so far.
- What does a high probe score show, and what does it not show? → It shows only that the information is present; it does not show that the model uses it.

### Retell

In 2-3 sentences, explain to a colleague what a hidden state is, what a probe score does and does not show, and what the open question about concepts depends on.

Must use: by construction, to be tantamount to, to hinge on

Model answer: On our reading, a hidden state is a running sum: every attention and MLP part adds its write, which is true by construction in our toy and holds up to rounding in GPT-2 small, apart from the last library entry. A probe score shows only that information is present, and to say the model uses it would be tantamount to confusing seeing with doing. Whether concepts are directions in a trained language model's stream hinges on tests that our three sources do not give.

## Expressions

- **by construction** (C1): because of the way something was built or chosen, not because of a discovery. In the passage: “by construction”. Second context: *In a simulated network, ties are denser within the two communities than between them by construction, because we wrote the generating rule that way.*
- **to bear out** (C2): to show that something said or believed is true. In the passage: “bears it out”. Second context: *If the replication bears out the original finding, we can report the effect with more confidence.*
- **to go unheard** (C2): to exist or be said without being noticed, taken into account or dealt with. In the passage: “goes unheard”. Second context: *If we only report the majority label, the minority view among the coders goes unheard.*
- **a case in point** (C1): a good example of what has just been said. In the passage: “a case in point”. Second context: *Proxies can mislead, and follower counts are a case in point.*
- **to take something at face value** (C1): to accept something as it appears, without asking whether it is more complicated. In the passage: “taken at face value”. Second context: *Self-reported media use should not be taken at face value in a survey like this.*
- **to a first approximation** (C1): as a rough first description that ignores smaller details. In the passage: “To a first approximation”. Second context: *To a first approximation, we can treat each user as an independent observation, then relax that assumption later.*
- **in lockstep** (C1): moving or changing together, at exactly the same time and in the same way. In the passage: “in lockstep”. Second context: *If the two series move in lockstep, a single underlying factor may explain both.*
- **to be tantamount to** (C2): to be virtually the same as something else, in effect; the second thing is usually more serious or negative. In the passage: “tantamount to”. Second context: *Treating a correlation as a mechanism would be tantamount to reporting an experiment we never ran.*
- **to hinge on** (C1): to depend completely on one particular thing. In the passage: “hinges on”. Second context: *The whole argument hinges on whether the sample resembles the population.*
- **to be on firm ground** (C1): in a safe position, with good evidence to support what you say. In the passage: “on firm ground”. Second context: *With the descriptive statistics we are on firm ground; with the causal story, much less so.*

## Patterns

- **Fronted wh-clause object (contrast)** (C2): Put a 'what' clause first, as the object of a verb that comes later, to make it the topic: 'What a score means, the algebra does not say.' The rest keeps normal subject-verb order, and no pronoun is added. It sets what is settled against what is not. In the passage: “What a score means, or whether a push changes behaviour, the algebra does not say”. Second context: *What a rise in retweets means, the counts alone do not say.*
- **Whether-clause as subject** (C1): A 'whether' clause can be the subject of a sentence and takes a singular verb: 'Whether it works hinges on ...'. Use 'whether', not 'if', here, and keep normal word order inside the clause. In the passage: “Whether concepts are directions in a trained language model's stream”. Second context: *Whether the effect survives a change of sample is a question for the replication.*
- **Perfect participle clause** (C1): 'Having + past participle' (or 'having been + past participle' in the passive) shows that something was finished, or is the case, before the main clause. The subject of the main clause must be the one the participle clause is about. In the passage: “having been through the final norm”. Second context: *Having coded every post twice, the team compared the two sets of labels.*
- **Noun + aside (absolute phrase)** (C1): A noun followed by 'aside' (or 'apart') makes a short verbless phrase, usually at the front of a clause, meaning 'if we set that to one side': 'Norm aside, a read is a dot product'. It is formal, and the noun names the thing being set aside. In the passage: “norm aside”. Second context: *Sampling error aside, the two surveys tell much the same story.*

## Fixes

- **tantamount to + -ing (not 'to' + infinitive)** (C1), sentence 5: ~~To say the model therefore uses it would be tantamount to confuse seeing with doing.~~ → To say the model therefore uses it would be tantamount to confusing seeing with doing. Here 'to' is a preposition, not part of an infinitive, so a verb after it takes -ing: tantamount to confusing, not tantamount to confuse. The same holds for amount to, committed to, object to and in addition to.
- **whether (not 'if') for a subject clause** (C1), sentence 8: ~~If concepts are directions in a trained language model's stream hinges on tests that our three sources do not give, so we are on firm ground with the arithmetic, not the interpretation.~~ → Whether concepts are directions in a trained language model's stream hinges on tests that our three sources do not give, so we are on firm ground with the arithmetic, not the interpretation. A clause that is the subject of a sentence begins with 'whether', not 'if': 'Whether it works hinges on ...'. 'If' opens a condition ('if it works, ...'), never a subject clause.
- **firm ground (no article)** (C1), sentence 8: ~~Whether concepts are directions in a trained language model's stream hinges on tests that our three sources do not give, so we are on a firm ground with the arithmetic, not the interpretation.~~ → Whether concepts are directions in a trained language model's stream hinges on tests that our three sources do not give, so we are on firm ground with the arithmetic, not the interpretation. In the idiom 'on firm ground' (also 'on solid ground') there is no article: 'on firm ground', not 'on a firm ground'. Adding 'a' is a common slip.
