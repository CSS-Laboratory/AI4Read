---
id: mcgrayne-2011-theory/ch01-causes
work: mcgrayne-2011-theory
unit: "1. Causes in the Air"
pages: 3-12
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Causes in the Air

## L0 — One line
Thomas Bayes devised, and left unpublished, a way to move from observed effects back to their probable cause by revising a starting guess with new data. Richard Price published it.

## L1 — The gist (≤ 120 words)
The chapter asks how an eighteenth-century Presbyterian minister, Thomas Bayes, came to treat the "inverse" problem of probability: from effects back to causes. His thought experiment with a ball on a level table shows how a guessed starting belief, revised by new data, narrows toward a range of likely values. McGrayne also lists what Bayes did not do. He gave no modern formula and did not name the method, and, as she tells it earlier, he never published the essay. Richard Price published the essay after Bayes' death. This beginning matters because it set up the later quarrels over priors and subjective belief.

**Prerequisites:** basic probability (equally likely outcomes, gambling odds); the idea of "cause and effect".

## L2 — Key ideas (5–10 bullets)
- Bayes lived as a Dissenter, barred from English universities. He moved in a network of amateur mathematicians linked to the Earl of Stanhope and the Royal Society (pp. 4–5).
- Hume's doubts about cause and effect, and de Moivre's cause-to-effect gambling work, formed the background. No one had solved the reverse question, from effect to cause (pp. 5–6).
- Bayes' goal was the probability of a future event known only through its past record. He began with an invented number, a "guess", and refined it with new information (p. 6).
- In his table thought experiment each new left/right report narrows where the hidden ball probably lies. The conclusion is a range with growing confidence, never an exact answer (p. 7).
- The scheme is: initial belief + new objective data = improved belief. Later names are prior, likelihood and posterior. "Prior times likelihood is proportional to the posterior", and each posterior becomes the next prior (p. 8).
- McGrayne says Bayes' wish to cover every uncertain case triggered 150 years of misunderstanding and attacks, with his guess and his equal-probabilities shortcut as especially popular targets. Critics disliked putting a hunch into rigorous mathematics and saw "quantifying ignorance" (pp. 8–9).
- Bayes buried the essay for about a decade. Price edited it, added a religious motive, and sent it to the Royal Society (pp. 9–11).
- Bayes turned probability from a measure of frequency into a measure of informed belief. He had no algebraic equation, no stated uses, and no name for the method (pp. 11–12).

## L3 — Walkthrough
(The chapter has no numbered sections. Headings below are my own, in the author's order.)

### Opening claims (p. 3)
McGrayne says Bayes discovered the rule in the 1740s and then abandoned it. Laplace rediscovered it independently and gave it its modern form. It drew the attention of leading twentieth-century statisticians, some of whom vilified it and declared it dead, yet it solved practical problems that nothing else could (examples listed: Dreyfus, insurance, Enigma, H-bomb search, Federalist Papers). Many supporters used it while hiding that fact (p. 3).

### Bayes' world (pp. 3–5)
- Bayes died in 1761, aged 59, per his gravestone. As a Presbyterian he was a Dissenter. Dissenters were persecuted, and many mathematicians were amateurs because they were barred from English universities (pp. 3–4).
- He studied at Edinburgh, went to London in 1711, and was ordained by his father (p. 4).
- He wrote a 1731 pamphlet on evil and God's beneficence. He also defended Newton's calculus against Bishop Berkeley's attack. That was his only mathematical publication in his lifetime (p. 4).
- He was nominated to the Royal Society in 1742. At Tunbridge Wells he joined a peer-review network run by the Earl of Stanhope and John Canton (pp. 4–5).

### The problem in the air (pp. 5–6)
- **Hume's view:** we cannot be absolutely certain about anything based only on traditional beliefs, testimony, habitual relationships or cause and effect. Umbrellas accompany rain without causing it. The sun's past risings do not guarantee tomorrow's. Because we can seldom be certain that a cause will have a given effect, we must be content with finding only probable causes and probable effects (pp. 5–6).
- De Moivre's book expected calculation to reveal "Wisdom and Design" (p. 6).
- Early-1700s probability was applied mainly to gambling. De Moivre had solved the cause-to-effect question (odds of four aces). The inverse question remained open. Example: a player deals himself four aces in three consecutive hands, so how likely is it that his deck is loaded? (p. 6)
- McGrayne says we do not know what prompted Bayes. De Moivre, Stanhope, Newton's gravitation and Hume are named as possibilities (p. 6).

### The billiard-table thought experiment (pp. 6–8)
- Bayes wanted the approximate probability of a future event, known only from how often it had and had not occurred. Between 1746 and 1749 he chose to invent a starting number, his "guess", and refine it (p. 6).
- Setup: a level square table, where a ball is equally likely to stop anywhere. Bayes sits with his back turned. A first ball lands at an unknown place. An associate throws further balls and reports only left or right of the first (p. 7).
- A "left" report makes the first ball more likely to sit toward the right. A "right" report rules out the far right edge (p. 7).
- With more throws the cue ball is confined to a smaller area. If all later throws fall right, it probably sits at the far left, and vice versa (p. 7).
- The method cannot give the exact position. It gives a range, with increasing confidence, and it says how confident one can be (pp. 7–8).

*Intuition note:* each report narrows the plausible region a little. Many reports together narrow it further. The answer is a range with a confidence level, not a single point.

### The scheme and its names (p. 8)
- Initial Beliefs + Recent Objective Data = A New and Improved Belief (p. 8).
- Later names: prior (initial belief), likelihood (probability of competing hypotheses for the fixed observed data), posterior (revised belief). Each posterior becomes the next prior (p. 8).
- $$\text{prior} \times \text{likelihood} \propto \text{posterior}$$
- **Andrew Dale (quoted):** "Put somewhat rudely, the likelihood is what remains of Bayes's Theorem once the prior is removed from the discussion." (p. 8)

*Intuition note:* the rule is a recipe for updating. Multiply what you believed by how well each possibility explains the data. The result is your new belief.

### Why it was attacked (pp. 8–9)
- For the table, the rule is uncontroversial (p. 8). Bayes wanted it to cover any uncertain case, even where we "absolutely know nothing antecedently to any trials". McGrayne says this triggered 150 years of attacks (p. 8).
- Target 1, the guess: critics would be horrified at a subjective hunch in objective mathematics (p. 8).
- Target 2, equal probabilities when nothing distinguishes the cases. McGrayne traces the practice to Christian ideas about usury, to annuities and to marine insurance, where parties took equal shares. It later had many names, including the law of insufficient reason. It became a lightning rod for the complaint that Bayes quantified ignorance (pp. 8–9).
- Some historians say Bayes may have applied equal probabilities to the later throws instead of the first toss. McGrayne calls this also guesswork. She adds that for many working statisticians the question is irrelevant, because in the tightly circumscribed case of a carefully leveled table both give the same mathematical results (p. 9).

### Silence and Price (pp. 9–11)
- In 1749 David Hartley wrote of a friend's "Solution of the inverse problem". Suggested friends were Bayes, Stanhope, and (Stigler, 1999) Nicholas Saunderson. McGrayne judges it highly unlikely anyone but Bayes made the breakthrough (p. 9).
- Bayes did not send the essay to the Royal Society. It sat among his papers for roughly a decade. McGrayne says fear of controversy can hardly be the reason, since he had joined the pamphlet wars twice. She raises the idea that he thought it useless but doubts it: a pious clergyman who thought the work proved God's existence would surely have published it. She reports that some thought he was too modest and others wondered whether he was unsure of his mathematics. She concludes that, whatever the reason, he suppressed it (pp. 9–10).
- After Bayes died in 1761, Richard Price examined his papers. Price found "an imperfect solution" of a hard problem and at first saw little reason to spend time on it (p. 10).
- Once Price saw it as an answer to Hume on causation, he worked on it for almost two years. He added references, cut background, and discarded Bayes' introduction (pp. 10–11).
- **Price's cover letter:** the theorem aimed to show the world "must be the effect of the wisdom and power of an intelligent cause". Bayes' own part does not mention God (p. 11).
- The essay appeared in *Philosophical Transactions* the next year. Its title stressed gambling. As far as we know, no one else mentioned it for 17 years, until Price did (p. 11). McGrayne says "Bayes-Price rule" would be fairer, but the single name is entrenched (p. 11).

### What Bayes did and did not do (pp. 11–12)
- He turned probability from a gambler's measure of frequency into a measure of informed belief. He combined hunches with repeatable-experiment probabilities (p. 11).
- He used no algebraic equation, only Newton's geometric notation to add areas. He did not develop a powerful method, did not mention Hume, religion or God, and did not discuss hypothesizing, predicting, deciding or acting (pp. 11–12).
- The method was called probability of causes or inverse probability for 200 years, and "Bayesian" only from the 1950s (p. 12).
- For two centuries few read the Bayes-Price article and it had almost no impact, except on Laplace (p. 12).

## Toy example (ours, not from the text)
A discrete version of the table. The hidden ball sits at position $x \in \{0.25, 0.5, 0.75\}$, measured from the left edge. A later ball lands left of it with probability $x$. Prior: equal, $1/3$ each.

Report 1 is "left". Likelihoods are $0.25, 0.5, 0.75$.
- Prior × likelihood: $0.0833,\ 0.1667,\ 0.25$. Sum $=0.5$.
- Posterior: $1/6,\ 1/3,\ 1/2$.

Report 2 is "left". The old posterior is the new prior.
- Products: $\tfrac16(0.25)=0.04167$, $\tfrac13(0.5)=0.16667$, $\tfrac12(0.75)=0.375$. Sum $=0.58333$.
- Posterior: $0.0714,\ 0.2857,\ 0.6429$.

Belief moves toward the right side, as Bayes' reasoning says, and each posterior is the next prior.

## Concepts
- [[inverse-probability]] (new) — reasoning from observed effects to their probable cause; the old name for Bayes' rule (p. 6, p. 12)
- [[prior-distribution]] — the probability of the initial belief, Bayes' "guess" before new data (p. 8)
- [[likelihood]] — as McGrayne puts it, the probability of competing hypotheses for the fixed observed data (p. 8)
- [[posterior-distribution]] — the probability of the newly revised belief (p. 8)
- [[bayes-theorem]] — prior times likelihood is proportional to the posterior (p. 8)
- [[sequential-updating]] — each posterior becomes the prior of the next round (p. 8)
- [[principle-of-indifference]] — equal probabilities when nothing distinguishes cases; "law of insufficient reason" (p. 9)
- [[subjective-probability]] — here, a belief or hunch entering the mathematics, which critics rejected (pp. 8, 11)

## Canonical instances
- [[bayes-billiard-table]] (new) — a hidden ball located from left/right reports of later throws (p. 7)
- [[loaded-deck-inverse-question]] (new) — four aces in three hands: what is the chance the deck is loaded? (p. 6)

## Bridges (candidates)
- [structural-analogy] Table narrowing ↔ Bayesian statistics: repeated data shrink the plausible range of an unknown parameter.
- [structural-analogy] Hume's "probable causes" ↔ causal inference: causes can only be inferred with uncertainty from observed association.
- [metaphor] Posterior becomes the next prior ↔ everyday learning from experience.

## Questions this raises
- Does it matter whether equal probabilities are assigned to the first toss or to the later throws, outside the leveled-table case?
- How can a subjective starting guess be defended in "objective" science?
- What would Bayes' lost introduction have told us about his own aims?
- What did Laplace add to turn Bayes' table result into a general method?

## Reading notes
- Printed = pdf − 15. The running header on even pages is "Enlightenment and the Anti-Bayesian Reaction".
- The text layer is clean. Bayes' quote contains "[sic]" as printed.
- The source states the Hartley quotation and Stigler's 1999 suggestion only briefly. Nothing here goes beyond that.
