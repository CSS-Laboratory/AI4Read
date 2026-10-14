---
id: bayes-1763-essay/main
work: bayes-1763-essay
unit: paper
pages: 8–23
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# An Essay towards Solving a Problem in the Doctrine of Chances (Price's letter, Section I, Section II up to the Scholium)

## L0 — One line
Bayes uses rules built from expectations, plus a ball-on-a-table model, to show how to find the chance that an unknown event's single-trial probability lies between two values, given only how often it happened and failed; he argues that the model fits events about which nothing is known beforehand.

## L1 — The gist (≤ 120 words)
Bayes asks the inverse of De Moivre's problem. Given that an unknown event happened p times and failed q times, what is the chance that its single-trial probability lies between two named values? He builds the sum and product rules from expectations (Section I). He then models the unknown probability by the landing point of a ball on a level table (Section II). The answer (Prop. 9) is a ratio of areas under the curve $y=E x^p r^q$. A scholium (a note added after a proposition) gives a reason why the same rule seems to fit any event about which nothing is known beforehand. The unit stops there.

**Prerequisites:** ratios and proportions; the binomial expansion; area under a curve; the idea of "expectation" as value of a bet.

## L2 — Key ideas (5–10 bullets)
- Price presents the problem as the converse of De Moivre's: from observed happenings and failures, infer the chance that the underlying probability lies in a range. He says De Moivre's rules are not pretended to be rigorously exact except for infinitely many trials (pp. 9–10).
- Bayes defines probability as the ratio of the value of an expectation to the value of the thing expected, so that no dispute about the word "probability" is needed (pp. 11–12).
- From this definition he derives additivity (Prop. 1), the product rule (Prop. 3), and the rule for the chance of a first event given that a second has happened (Prop. 5) (pp. 12–16).
- Independent trials give the binomial probability $E a^p b^q$ (Prop. 7) (p. 17).
- A ball thrown on a level table gives a physical model with uniform chances; the unknown probability becomes a point $o$ that is equally likely to lie anywhere along a line $AB$ (Postulates, Lemmas 1–2) (pp. 18–20).
- Prop. 8 shows the joint probability is an area under the curve $y=Ex^pr^q$ relative to the square $CA$ on the line $AB$. Prop. 9 divides by the total area $AiB$ (the whole figure drawn on $AB$) to get the answer (pp. 20–22).
- The scholium argues that, before $W$ is thrown, there is no reason to favour one count of happenings over another, so it seems the table rule can be used for any unknown event, i.e. one about which nothing is known beforehand (pp. 22–23).

## L3 — Walkthrough

### Price's letter (pp. 8–11)
**Voice: Price, reporting Bayes.**
- Price found the essay among Bayes's papers after his death and judged it worth preserving (p. 8).
- Bayes's first aim was to judge the probability of an event, knowing only that in the same circumstances it had happened some number of times and failed some number of times (pp. 8–9).
- Bayes soon saw this would not be very difficult if one had a rule for the chance, before any experiment, that the unknown probability lies between two named degrees. It appeared to him that the rule must be to take the chance as the same for any two equidifferent degrees, i.e. equal-width intervals get equal chance. Price says Bayes did solve the problem this way (p. 8).
- Bayes then considered that this postulate might not be looked upon by all as reasonable. So he stated a proposition in another form and put his reasons for it in a scholium, to keep disputable matter out of his mathematics (pp. 8–9).
- Price says the problem must be solved to give a sure foundation for reasoning about past facts and what is likely hereafter, and must be considered by anyone who wants a clear account of the strength of inductive reasoning (p. 9).
- Price says that De Moivre (after Bernoulli) gives rules for the **direct** problem: how far the observed proportion of happenings is likely to differ from the single-trial probability. He knows of no one who solved the converse. He adds that De Moivre's rules are not pretended to be rigorously exact except for infinitely many trials, so it is not obvious how many trials suffice in practice (pp. 9–10).
- Price says that the converse problem shows, for any observed order or recurrence, what reason there is to think it comes from stable causes rather than chance (p. 10).
- The last two rules of the essay are given without proof, and Price adds an appendix of applications. Neither is in these pages (p. 10).
- Price says Bayes apologised for his peculiar definition of probability. Bayes wanted to cut off disputes, and he used what all will allow to be the measure of probability: an expectation is worth more the likelier the event (p. 11).

### The Problem (p. 12)
Given the number of times an unknown event has happened and failed, find the chance that its probability in a single trial lies between any two named degrees of probability (p. 12).

### Section I: definitions (p. 12)
- Events are **inconsistent** if when one happens none of the others can. Two events are **contrary** if one or the other must happen and both cannot (Defs. 1–2).
- An event **fails** when it cannot happen, i.e. when its contrary has happened. It is **determined** when it has happened or failed (Defs. 3–4).
- **Def. 5:** the probability of an event is the ratio between the value at which an expectation depending on the event ought to be computed, and the value of the thing expected if the event happens. **Def. 6:** chance means the same as probability.
- **Def. 7:** events are **independent** when the happening of one neither raises nor lowers the probability of the others.

### Props. 1–2: additivity and odds (pp. 12–13)
**Prop. 1.** For inconsistent events, the probability that one or other happens is the sum of their probabilities.
- Take three events with probabilities $a/N, b/N, c/N$, with $N$ received whichever happens. By Def. 5 the expectations are worth $a, b, c$.
- Together they make an expectation of $N$ on "one or other", worth $a+b+c$. So the probability is $\frac{a+b+c}{N}=\frac aN+\frac bN+\frac cN$ (pp. 12–13).
- Corollary: if one of the events must happen, $a+b+c=N$. So an event with probability $P/N$ has failure probability $(N-P)/N$ (p. 13).

**Prop. 2.** The probability of an event is to the probability of its failure as one's loss if it fails is to one's gain if it happens.
- With probability $P/N$ the expectation is worth $P$. The loss on failure is $P$; the gain on success is $N-P$.
- $\frac PN : \frac{N-P}{N} = P : N-P$ (p. 13).

*Intuition note.* Probability is defined through the fair price of a bet. Additivity, and the rule that an event's probability is to its failure's probability as loss is to gain, then follow from simple bookkeeping about bets.

### Props. 3–5: product rule and the inverse conditional (pp. 13–16)
**Prop. 3.** The probability that two subsequent events both happen is a ratio compounded of (i.e. the product of) the probability of the 1st and the probability of the 2nd given that the 1st happens.
- Let me receive $N$ if both happen. Let $P/N$ be the probability of both, $a/N$ of the 1st, and $b/N$ of the 2nd given the 1st. The expectation is worth $P$; if the 1st happens it becomes worth $b$ (p. 13).
- If the 1st happens my gain is $b-P$. If it fails my loss is $P$ (p. 14).
- By Prop. 2: $\frac aN : \frac{N-a}{N} = P : b-P$, i.e. $a : N-a :: P : b-P$ (p. 14).
- *Componendo inversè* gives $a : N :: P : b$. (added step: from $\frac{a}{N-a}=\frac{P}{b-P}$ we get $\frac{N-a}{a}=\frac{b-P}{P}$, so $\frac Na=\frac bP$.) Hence $\frac PN=\frac Pb\cdot\frac bN=\frac aN\cdot\frac bN$ (p. 14).
- Corollary: if the 1st has probability $a/N$ and both together $P/N$, the 2nd given the 1st has probability $P/a$ (p. 14).

**Prop. 4.** Two events are determined each day. The 2nd has probability $b/N$ and both have probability $P/N$ each day. I receive $N$ if both happen on the first day on which the 2nd happens. Then the probability of obtaining $N$ is $P/b$ (p. 14).
- Suppose that probability is $x/N$, so the expectation is worth $x$. Let $y$ be to $x$ as $N-b$ to $N$ (p. 14).
- On day 1, I have an expectation of $N$ on both events, worth $P$. If the 2nd fails (probability $\frac{N-b}{N}=\frac yx$) I am reinstated, with an expectation worth $x$, which here has value $y$ (pp. 14–15).
- These two expectations together equal the original, so $P+y=x$. Since $y:x::N-b:N$, we get $x:P::N:b$, so $\frac xN=\frac Pb$ (pp. 14–15).

**Prop. 4, Cor.** Suppose that before I know whether the 1st event happened, I learn that the 2nd has happened.
- The value of my expectation ought to stay at $x$. If it fell, I would be willing to pay to be reinstated, again and again. If it rose, I would refuse offers to give it up, again repeatedly. The author calls both results absurd (p. 15).
- So the probability of obtaining $N$ is still $P/b$. But that probability is now the probability that the 1st event has happened, given that the 2nd has. The probability that an event has happened equals the probability of guessing right when guessing it has (pp. 15–16).

**Prop. 5.** For two subsequent events, with probability $b/N$ for the 2nd and $P/N$ for both, if it is first discovered that the 2nd happened and I guess the 1st also happened, the probability I am right is $P/b$ (pp. 15–16).
- Footnote (p. 15): what is lost when the 2nd event happens is only a chance of being reinstated. That chance is always as much against me as for me, so the loss is no disadvantage.
- Footnote (p. 16; it refers to Mr. Bayes in the third person, so it is not Bayes's own wording): this is the same as asking for the probability that an event, when it happens, comes with another. With $x$ the probability of the other event, $\frac pN=\frac bN x$, so $x=\frac pb$.

*Intuition note.* Props. 3 and 5 together are the rule for turning the probability of both events and the probability of the second event into the probability of the first given the second. In modern terms, this is conditional probability.

### Prop. 6 and trials (pp. 16–17)
- **Prop. 6.** For independent events, the probability that all happen is the product of their probabilities. Proof: by independence, the 2nd's probability given the 1st is its original probability, so Prop. 3 applies repeatedly, treating earlier events together as one (p. 16).
- Cor. 1: failures count as happenings of the contrary event. Cor. 2: if each event has probability $a$ and failure $b$, the sequence "happens, fails, fails, happens, …" has probability $a\,b\,b\,a\cdots$ (pp. 16–17).
- **Definition of trials:** repeated occurrences under the same data are the "1st trial", "2d trial", and so on. They are distinct independent events "exactly familiar" to each other (p. 17).

### Prop. 7: the binomial (p. 17)
If an event has probability $a$ and failure $b$ in each trial, the probability that it happens $p$ times and fails $q$ times in $p+q$ trials is $E\,a^p b^q$, where $E$ is the coefficient of $a^pb^q$ in $(a+b)^{p+q}$.
- By Prop. 6, Cor. 2, any one ordering has probability $a^pb^q$.
- The number of orderings equals the number of permutations of $p$ letters $a$ and $q$ letters $b$, which is $E$ (in modern notation, $\binom{p+q}{p}$; added step).
- The orderings are inconsistent events, so Prop. 1 gives $E a^pb^q$ (p. 17).

### Section II: the table model (pp. 18–20)
**Postulates (p. 18).**
1. A level square table $ABCD$ is made so that a thrown ball $o$ or $W$ rests on any equal part of the plane with the same probability, and rests somewhere on it.
2. Ball $W$ is thrown first, and a line $os$ parallel to $AD$ is drawn through where it rests. Ball $O$ is then thrown $p+q=n$ times. Its resting between $AD$ and $os$ is called the happening of the event $M$ in a single trial.

**Lemma 1.** The probability that the point $o$ falls between two points of line $AB$ is the ratio of the distance between them to the whole line $AB$ (p. 18).
- Commensurable case: cut the plane into equal parts. Inconsistent events (resting on different parts) sum by Prop. 1, so the probability is proportional to the number of parts, i.e. to the width (p. 18).
- Incommensurable case: the probability can be neither less nor greater than $fb/AB$. If it were less, choose points $p, t$ with commensurable segments and $pt$ larger than the supposed value. Then probability $\ge pt/AB>$ the supposed value, a contradiction. The "greater" case is the same (pp. 18–20).

**Lemma 2.** After $W$ is thrown, the probability of $M$ in a single trial is $Ao/AB$ (p. 20).

*Intuition note.* The table turns a probability about which we know nothing into a point $o$ on a line. The point is equally likely to be anywhere, and that is the model's prior assumption.

### Prop. 8: the joint probability is an area (pp. 20–22)
Erect on $BA$ a figure $BghikmA$ with this property.
- Divide the base at $b$. Let $y, x, r$ be the ratios of $bm$, $Ab$, $Bb$ to $AB$ (the text prints "A B" for the first part; context requires $Ab$).
- The curve satisfies $y=E x^p r^q$, with $E$ as in Prop. 7 (p. 20).

**Claim.** Before $W$ is thrown, the probability that $o$ falls between $f$ and $b$ and that $M$ happens $p$ times and fails $q$ times in $p+q$ trials is the ratio of the area $fghikmb$ to the square $CA$ on $AB$ (p. 20).

**Demonstration (by contradiction).**
- Suppose first that the ratio is $D/CA$, with area $D$ greater than $fghikmb$. Choose points $e,d,c$ on $fb$, with $di$ the longest ordinate. Choose them so that the rectangles on $ef$, $ed$, $dc$, $cb$ together differ from the figure by less than $D$ does. Ordinates decrease on each side of $di$ (pp. 20–21).
- If $Ao=Ae$, then by Lemma 2 the single-trial chance is $x=Ae/AB$, with failure $r=Be/AB$. By Prop. 7 the probability of the counts is $Ex^pr^q=y=eh/AB$ (p. 21).
- For $o$ anywhere between $f$ and $e$, the probability of the counts is therefore at most $eh/AB$, since $eh$ is the greatest ordinate on $ef$ (p. 21).
- By Lemma 1, $P(o\in ef)=ef/AB$. By Prop. 3, the probability of both is at most $\frac{ef}{AB}\cdot\frac{eh}{AB}$, i.e. the ratio of the rectangle $fh$ to $CA$. The same holds for each other sub-interval (p. 21).
- By Prop. 1 the sum of the four bounds bounds the probability on $fb$. So the probability is below $D/CA$, because the rectangles total less than $D$. This contradicts the supposition (pp. 21–22).
- Inscribed rectangles show likewise that the probability exceeds the ratio of any smaller figure to $CA$. So it equals $fghikmb/CA$ (p. 21).

**Corollary.** Since $o$ certainly lies on $AB$, the probability, before $W$ is thrown, that $M$ happens $p$ times and fails $q$ times in $p+q$ trials is $AiB/CA$ (pp. 21–22).

*Intuition note.* Each strip of the table is weighted by Lemma 1 (how likely $o$ is there) and by Prop. 7 (how likely the observed count is if $o$ is there). Adding the strips approximates the area; the proof squeezes the probability between inner and outer sets of rectangles.

### Prop. 9: Bayes's answer (p. 22)
**Statement.** Suppose that, before anything is known of the place of $o$, it appears that $M$ happened $p$ times and failed $q$ times in $p+q$ trials. Suppose I guess that $o$ lies between $f$ and $b$, i.e. that the single-trial probability lies between $Af/AB$ and $Ab/AB$. Then the probability that I am right is the ratio of the part of $AiB$ between the perpendiculars at $f$ and $b$ to the whole figure $AiB$ (p. 22).

**Proof.**
- Take the first event "$o$ between $f$ and $b$" and the second event "$M$ happens $p$ times, fails $q$ times".
- By the Corollary of Prop. 8, the probability of the second is $AiB/CA$. By Prop. 8, the probability of both is $fghimb/CA$ (the text omits $k$ here; see Reading notes).
- Prop. 5 applies: the second is discovered first, and I guess the first. The probability I am right is $\dfrac{fghimb/CA}{AiB/CA}=\dfrac{fghimb}{AiB}$ (p. 22).

**Corollary.** If I guess the probability lies between $0$ and $Ab/AB$, the chance I am right is the ratio of $Abm$ to $AiB$ (p. 22).

*Intuition note.* The answer is a ratio of areas under the curve $Ex^pr^q$. In modern words, the probability is spread over the possible chances with a shape given by how well each chance explains the observed counts.

### Scholium: why the table rule fits an unknown event (pp. 22–23)
**Voice: Bayes.**
- For an event like $M$, Prop. 9 lets one guess where its probability lies from its counts alone, and compute the chance the guess is right (p. 22).
- Bayes says it seems to appear that this rule is also the proper one for an event about whose probability one knows absolutely nothing before any trials (pp. 22–23).
- His reason: for such an event one has no reason to expect any one number of happenings in $n$ trials rather than another. One may then reason as if its probability were first unfixed and then fixed so as to give no such reason (p. 22).
- This is exactly the case for $M$. Before $W$ is thrown, the probability of $p$ happenings in $n$ trials is $AiB/CA$. For a given $n$, this ratio is the same whatever $p$ is, as computing $AiB$ by the method of fluxions will show, Bayes says (p. 23).
- Footnote: Bayes says it will be proved presently, in art. 4, that $AiB$ contracted in the ratio $E$ to $1$ is to $CA$ as $1$ to $(n+1)\times E$. So $AiB:CA=1:(n+1)$, constant for given $n$ (p. 23). The proof is not in these pages.
- Bayes then takes the Prop. 9 rule as the rule for any event about which nothing is known beforehand, and calls such an event an **unknown event** (p. 23).

## Toy example (ours, not from the text)
Take $n=2$ trials, unit square, so $CA=1$ and the curve is $y=E x^p(1-x)^q$.

**Step 1 (check the scholium).** Areas under the curve:
- $p=0,q=2$: $E=1$, $\int_0^1(1-x)^2dx=\tfrac13$.
- $p=1,q=1$: $E=2$, $\int_0^1 2x(1-x)dx=2(\tfrac12-\tfrac13)=\tfrac13$.
- $p=2,q=0$: $E=1$, $\int_0^1x^2dx=\tfrac13$.

Every count has probability $\tfrac13=\tfrac1{n+1}$ before $W$ is thrown. This matches the footnote's $1:(n+1)$.

**Step 2 (Prop. 9).** Suppose both trials succeeded ($p=2$). Guess that the chance lies between $\tfrac12$ and $1$.
- Joint area: $\int_{1/2}^1x^2dx=\tfrac13(1-\tfrac18)=\tfrac7{24}$.
- Whole area: $\tfrac13$.
- Probability of being right: $\tfrac{7/24}{1/3}=\tfrac78$.

## Concepts
- [[bayes-theorem]] — here shown as Prop. 5/Prop. 9: probability of the first event given the second equals probability of both divided by probability of the second (pp. 15–16, 22).
- [[prior-distribution]] — no explicit prior formula appears; the position of $o$ (uniform on $AB$) plays that role (pp. 18–20).
- [[likelihood]] — the binomial $Ex^pr^q$ as a function of the single-trial chance $x$ (pp. 17, 20).
- [[posterior-distribution]] — the area ratio of Prop. 9, giving the chance that the probability lies in a range (p. 22).
- [[marginal-likelihood]] — $AiB/CA$, the probability of the observed counts before $W$ is thrown (pp. 21–22).
- [[principle-of-indifference-maximum-entropy]] — the scholium argues from having no reason to expect one count rather than another; these pages do not call it a principle (pp. 22–23).
- [[probability-as-expectation-ratio]] (new) — Def. 5: probability is the ratio of an expectation's value to the value of the thing expected (p. 12).
- [[direct-vs-inverse-probability]] (new) — De Moivre's direct problem versus Bayes's converse problem (pp. 9–10).
- [[unknown-event]] (new) — an event about whose probability nothing is known before any trials (p. 23).

## Canonical instances
- [[bayes-billiard-table]] — the table with balls $W$ and $O$ models an unknown probability and repeated trials (p. 18).
- [[binomial-trials]] — Prop. 7: $E a^pb^q$ for $p$ happenings and $q$ failures in independent trials (p. 17).

## Bridges (candidates)
- [same-math] Prop. 3 and Cor. ↔ probability: product rule $P(A\cap B)=P(A)P(B\mid A)$ — Bayes derives the same rule from expectations.
- [same-math] Prop. 9 ↔ Bayesian inference: posterior $\propto x^p(1-x)^q$ on $[0,1]$ under a uniform prior — the curve drawn is this function.
- [structural-analogy] Prop. 4 Cor. (no repeated paying) ↔ Dutch book argument: value that allowed repeated sure losses or gains would be incoherent.
- [structural-analogy] Scholium (no reason to prefer a count) ↔ principle of indifference: a symmetry argument fixes the uniform prior.

## Questions this raises
- Does equal chance for each possible count (scholium) justify the same prior as equal chance for equidifferent degrees (Price's account of Bayes's first postulate)?
- What is the exact area $AiB$, and how does the proof in art. 4 (not in these pages) go?
- How large must $n$ be before Bayes's answer is useful, compared with De Moivre's infinite-trial rules (pp. 9–10)?
- What changes if some knowledge about the event exists before the trials?

## Reading notes
- Printed page = pdf page + 7. The inline "(page 371)" etc. mark the original journal pages; I cite printed pages only.
- This unit ends at the scholium (original p. 394). The essay is longer (metadata: pp. 370–418), but later propositions, the appendix and the "last two rules" are not in these pages.
- Page headers read "Chapter 2 / The Essay" and "Version zh25a.doc … 13 July, 2001", so this is a reprint copied from the Philosophical Transactions (p. 8).
- The text layer is garbled in places. I checked pdf pages 6, 7, 10–16.
- Prop. 8 text reads "as A B, and B b" for the two parts of the base. Context needs $Ab$ (p. 20).
- Prop. 9's proof prints the area as "f g h i m b" (no $k$), unlike Prop. 8's "fghikmb" (p. 22). The Corollary of Prop. 9 prints the lower limit of the guess as an italic $o$, read here as $0$ (p. 22).
- Prop. 7 prints the binomial as $\overline{a+b}|^{p+q}$ with a bar notation; the footnote on p. 23 prints "n + 1 x E" with an overline, read here as $(n+1)\times E$.
