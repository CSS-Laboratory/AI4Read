---
id: lycan-2019-language/ch02-definite
work: lycan-2019-language
unit: "2 Definite Descriptions"
pages: 9–30
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 25
pipeline_version: 0.1
---
# Definite Descriptions

## L0 — One line
Russell analysed "the F is G" as three general statements (at least one F, at most one F, every F is G), which, Russell argued, solves four puzzles about singular terms for the case of descriptions, though Strawson and Donnellan object and anaphoric uses may resist the analysis.

## L1 — The gist (≤ 120 words)
Do singular terms mean what they mean simply by naming something? Lycan presents four puzzles that, for descriptions at least, say no: apparent reference to nonexistents, negative existentials ("Pegasus never existed"), Frege's puzzle about identity, and substitutivity. Russell's Theory of Descriptions treats "the F is G" as a hidden triple of quantified generalizations, with no singular term at the level of logical form. Russell argues that this solves the puzzles for descriptions. Strawson objects that Russell ignores presupposition, context and use. Donnellan adds the referential use of descriptions. Anaphoric uses may also resist the theory. Lycan calls the theory impressive but open to objection. On Russell's view, surface grammar can hide logical form.

**Prerequisites:** basic quantifiers (∃, ∀) and identity in predicate logic; the idea of truth-value; the Referential Theory of Meaning from Chapter 1 (meaning = what a word refers to).

## L2 — Key ideas (5–10 bullets)
- Singular terms (names, descriptions, pronouns, demonstratives) are the paradigm referring expressions. Four puzzles arise if reference is all there is to their meaning: apparent reference to nonexistents; negative existentials (denials of existence); Frege's puzzle about identity; and substitutivity (swapping terms for the same thing). Lycan reports that Frege and Russell showed this view false for descriptions and raised doubts about other singular terms (pp. 10–12).
- Russell's contextual definition treats "The F is G" as an existence clause, a uniqueness clause and a predication clause. The description "disappears on analysis" (pp. 13–14).
- On Russell's analysis the puzzles are solved for descriptions: the King-of-France sentence is false, negative existentials depend on whether "not" falls inside or outside the description's quantifiers (scope), identity statements become predications, and swapping descriptions changes the belief attributed, while at the level of logical form no term is substituted (pp. 14–18).
- Strawson (Objection 1) holds that "The present King of France is bald" lacks truth-value because its presupposition (that there is a King of France) fails. He also holds that people refer, not expressions (pp. 19–20).
- Context-bound descriptions ("The table…") may be handled by restricted quantification (quantifier domains limited by context), though some cases like the bishop sentence (11) are harder (pp. 20–22).
- Donnellan distinguishes attributive use (whoever fits the description) from referential use (picking out a particular thing, whatever its properties). Kripke replies with speaker-reference versus semantic reference, but the distinction still seems to matter (pp. 22–26).
- Anaphoric uses (pronouns and repeated descriptions that take their meaning from an earlier phrase) may defy Russell's treatment (pp. 27–28).

## L3 — Walkthrough

### Overview and "Singular Terms" (pp. 9–10)
- **Singular terms** are expressions that purport to denote one particular individual. Examples are proper names, definite descriptions, "you", "she", "this" and "that". They differ from general terms like "dog", which can apply to several things (p. 10).
- Frege and, following him, Russell showed that the Referential Theory of Meaning fails for definite descriptions. They also raised doubts about other singular terms (p. 10).
- Four puzzles follow. The first three go back to Chapter 1's objections to the Referential Theory (p. 10).

### The four puzzles (pp. 10–12)
**1. Apparent Reference to Nonexistents.** Take (1) "James Moriarty is bald." The following six statements seem each true but cannot all be true (p. 10):
- J1: (1) is meaningful.
- J2: (1) is a subject–predicate sentence.
- J3: A meaningful subject–predicate sentence is meaningful (only) in virtue of picking out some individual and ascribing a property to it.
- J4: (1)'s subject term fails to denote anything existing.
- J5: Given J1–J3 and J4, either (1) is not meaningful or (1) picks out a nonexistent thing.
- J6: There are no nonexistent things.

**2. Negative Existentials.** Take (2) "Pegasus never existed." It seems true and about Pegasus. But if it is true, there is nothing for it to be about. If it is about Pegasus, Pegasus must in some sense exist, so it is false (p. 11).
- **Meinong's solution (to 1 and 2):** deny J6. Every possible object of thought has being, though few exist. Negative existentials then say that an entity with being lacks existence. Frege and Russell rejected this (p. 11).
- **Frege's solution (to 1):** deny J3. A singular term is meaningful through its *sense*, an abstract entity, whether or not it has a referent. Frege's other solutions are deferred to Chapter 3 (p. 11).

**3. Frege's Puzzle.** Take (3) "Mark Twain is Samuel Langhorne Clemens." If both names denote one person, (3) seems to say only that he is identical with himself. Yet (3) seems informative (one might learn something) and contingent (it need not have held). So it seems that at least one term must contribute meaning beyond its referent (pp. 11–12).

**4. Substitutivity.** One would expect co-denoting terms to be intersubstitutable without changing truth-value. But take (4) "Albert believes that Samuel Langhorne Clemens was less than 5 feet tall." Suppose it is true and Albert does not know that Clemens wrote as "Twain". Swapping in "Mark Twain" gives a false sentence (p. 12).
- Quine's term: the name's position in (4) is **referentially opaque**. Substituting a co-denoting term there may change the truth-value. The opacity is caused by "believes that". Standing alone, the sentence "Samuel Langhorne Clemens was less than 5 feet tall" is transparent (p. 12).

*Intuition note:* In each puzzle, treating a singular term as a mere label for its bearer leads to trouble: the sentence seems to have no object to be about, or it seems to say something trivial, or swapping labels for the same bearer can change the truth-value.

### Russell's Theory of Descriptions (pp. 12–14)
- Russell posed the puzzles for definite descriptions because he was interested in "the". He concluded that descriptions have and contribute meaning beyond their referents (p. 12).
- The theory is a **contextual definition**: a recipe for paraphrasing whole sentences containing "the", not a definition of "the" itself. It reveals "logical form". It does not cover plural or generic uses (pp. 12–13).
- Example (5) "The author of *Waverley* was Scotch." Russell says it abbreviates a conjunction of three quantified generalizations, none about Scott in particular (p. 13):
  - (5a) At least one person authored *Waverley*.
  - (5b) At most one person authored *Waverley*.
  - (5c) Whoever authored *Waverley* was Scotch.
- Each of (5a)–(5c) is intuitively necessary for (5), and together they seem sufficient. Lycan calls this, in itself, a powerful argument for Russell's analysis (p. 13).
- With $W$ = "authored *Waverley*" and $S$ = "was Scotch" (p. 13):

$$(\exists x)Wx \tag{a}$$
$$(x)\big(Wx \rightarrow (y)(Wy \rightarrow y = x)\big) \tag{b}$$
$$(x)(Wx \rightarrow Sx) \tag{c}$$

(a)–(c) together are equivalent to (p. 14):

$$(\exists x)\big(Wx \;\&\; (y)(Wy \rightarrow y = x) \;\&\; Sx\big) \tag{d}$$

- Russell holds that (d) gives the *logical form* of (5), as distinct from its superficial grammatical form (p. 14).
- **Parallel:** "I saw nobody" looks like "I saw Martha". The two have the same surface form but differ sharply in logical properties: "I saw Martha" entails that I saw someone, while "I saw nobody" entails the opposite. "Nobody" is a quantifier, and the sentence is $\sim(\exists x)Aix$, equivalently $(x)\sim Aix$ (p. 14).
- So too, Russell maintained, "The author of *Waverley*" is not really (at the level of logical form) a singular term at all. It "disappears on analysis" (p. 14).
- On Russell's analysis, the puzzles arise from applying singular-reference principles to expressions that only masquerade as singular terms (p. 14).

*Intuition note:* "The author of *Waverley*" works like "nobody": grammar suggests a name, but on Russell's view the logical form is a pattern of counting and generalizing. Once rewritten, there is no name left to cause trouble.

### Russell's solutions (pp. 14–18)
**Apparent reference to nonexistents.** Take (6) "The present King of France is bald," with the K1–K6 set as in J1–J6 (p. 14).
- Paraphrase: at least one person is presently King of France, and at most one is, and whoever is, is bald. The first conjunct is false, so (6) comes out *false* (pp. 14–15).
- Russell denies K2 (that (6) is subject–predicate): only superficially is it so. Lycan's alternative is to keep K2 as a claim about surface form and deny K3. Either way, no individual "King" appears in the logical form (p. 15).

**Negative existentials.** Take (7) "The present King of France does not exist." (p. 15)
- Paraphrase A treats "exist" as an ordinary predicate with "not" attached to it. The third conjunct then denies that whoever is King of France exists, which contradicts the first conjunct. That explains why (7) sounds peculiar (p. 15).
- Paraphrase B (the intended meaning) applies "not" to the whole description-sentence (pp. 15–16):

$$\sim(\exists x)\big(Kx \;\&\; (y)(Ky \rightarrow y = x) \;\&\; Ex\big)$$

  Here $E$ is "exists". Lycan notes that "exists" is itself a quantifier in logic, so $Ex$ should be $(\exists z)(z = x)$, which is redundant (p. 16).
- B says that no one uniquely kings France. Nothing is said of a particular individual that he does not exist, so the puzzle vanishes, at least for definite descriptions (p. 16).
- **Scope:** In B the description has **secondary** position, with its quantifiers *inside* "not" (narrow scope). In A it has **primary** position, with the quantifiers outside "not" and "not" inside their scope (wide scope) (p. 16).

**Frege's Puzzle.** Take (8) "The present Queen of England is Elizabeth Windsor." Paraphrase: at least one person is presently Queen, at most one is, and whoever is Queen is identical with Elizabeth Windsor (pp. 16–17):

$$(\exists x)\big(Qx \;\&\; (y)(Qy \rightarrow y = x) \;\&\; x = e\big)$$

- This is informative, because one learns something substantive. It is contingent, because someone else might have been Queen (p. 17).
- On Russell's view (8) is only superficially an identity statement. It is a predication attributing a complex relational property to Elizabeth. How a *real* identity statement can be true and informative is left to Chapter 3 (p. 17).

**Substitutivity.** Take (9) "Albert believes that the author of *Nothing and Beingness* is a profound thinker." Albert does not know that this author also wrote *Sizzling Veterinarians*, whose author he thinks a drooling moron. Substituting that description makes (9) false, so the position is opaque (p. 17).
- Russellian paraphrase, with narrow scope: Albert believes the following: (at least one person authored *N&B*, and at most one did, and whoever did is a profound thinker). The substituted sentence attributes an *entirely different* belief. At the level of logical form no substitution was made, because the descriptions have disappeared (pp. 17–18).
- Note 5 (p. 29) gives a second, wide-scope reading, on which (9) relates Albert to the author himself. Lycan says it is exceptionally hard to hear, and on it co-referring descriptions do substitute.

**Taking stock (p. 18).** The four puzzles made it clear that descriptions do not hook onto the world by directly naming and nothing else. When a unique satisfier exists, Lycan calls it the description's **semantic denotatum or semantic referent**. The hook is more indirect than for names. A description is compound, and one understands it through its words and their arrangement. This illustrates **compositionality** ("Frege's Principle"): roughly, the meaning of a complex expression is determined, and solely determined, by the meanings of its smallest meaningful parts and how they are combined (p. 18).

### Objections to Russell's Theory (pp. 18–19)
- **Generality objection:** the four puzzles arise for names and pronouns too, so a theory of descriptions alone seems to miss the point (pp. 18–19).
- **Russell's answer:** ordinary proper names are not really proper names but abbreviate definite descriptions. Lycan postpones discussing this to Chapter 3 (p. 19).
- **Strawson's framing:** Russell takes sentences in the abstract. His article "On Denoting" treats denoting as a relation between an expression and a thing. Strawson's "On Referring" treats referring as an *act* done by a person on an occasion. **Strawson's view:** expressions do not refer, people do (p. 19).
- **Lycan's partial rebuttal (made later in the chapter, after Objection 3):** there is a secondary sense in which expressions do refer, e.g. "The table" in context. A Russellian may grant that descriptions refer, so long as they do not refer directly like names (p. 22).

**Objection 1 (Strawson): presupposition failure.** Hearers of (6) would not say "That's false". **Strawson's claim:** the speaker has failed to refer and so made no complete statement. The utterance is "abortive", not false, and has no truth-value (pp. 19–20).
- Strawson then denies K3. (6) is meaningful in that it has a legitimate use in the language, not because it picks out something (p. 20).
- Russell takes a meaningful sentence to express a proposition, which is true or false. Strawson denies that sentences bear truth-values. *Statements* do, and not every utterance makes one (p. 20).
- Lycan says the standard Russellian reply depends on Chapter 13 and defers it. Note 9 (p. 30) says Strawson admits some exceptions in which a sentence with a non-referring description is plainly false.

**Objection 2 (Strawson): what is asserted.** Strawson attributes to Russell the claim that part of what the speaker would be asserting is that there is exactly one king (1950: 330), and finds this implausible, since the speaker presupposes it but does not assert it. Lycan: this is a misunderstanding, since Russell said nothing about acts of asserting. Perhaps Strawson assumes that whatever a sentence logically implies is necessarily asserted by a speaker who utters it, but Lycan says that principle is false. "Fat Tommy can't run or climb a tree" does not assert that Tommy is fat (p. 20).

**Objection 3 (Strawson): context-bound descriptions.** Take (10) "The table is covered with books." Russell's analysis entails that there is at most one table in the universe (p. 21).
- *Ellipsis option:* "the table" abbreviates a fuller description, e.g. "the table in this room". This has a cost: logical form is objectively real for Russell, so if "the table" is elliptical there must be a determinate answer about what is ellipsized, and the different candidates make (10) say different things (p. 21).
- *Restricted quantification option* (Lycan 1984, Neale 1990): the quantifier's domain is restricted by context. Lycan says practically all English quantification is restricted (a remark about nobody going to a certain restaurant would usually mean no one of our sort). The uniqueness clause then yields only that there is at most one table of the contextually indicated sort. This acts like a silent demonstrative, not hidden words (p. 21).
- A harder case is (11) "If a bishop meets another bishop, the bishop blesses the other bishop" (Heim 1990). Lycan only cites it and further literature (p. 22). How hearers fix the domains is a general problem, not special to Russell (p. 22).

*Intuition note:* Lycan says most descriptions are context-bound, so "the" often does not mean "the only one in the whole world". On the restricted-quantification option, context shrinks the pool of things being counted, and Russell's uniqueness clause holds only within that pool.

### Objection 4 (Donnellan): referential use (pp. 22–26)
- Some descriptions are fused titles ("The Holy Roman Empire", "The Grateful Dead"). Russell can say these are not used as descriptions at all (pp. 22–23).
- Donnellan finds less formal cases. In (12) "Smith's murderer is insane," the **attributive** use means whoever committed the crime, e.g. on seeing the body. The **referential** use arises when we watch Jones on trial, presume him guilty, and I use the phrase to pick him out. On Donnellan's account, what I said is then true iff the defendant is insane, regardless of whether he did the murder (p. 23).
- Donnellan's charges: Russell writes as if all uses were attributive, and Strawson writes as if all were referential. Donnellan does not decide what kind of ambiguity it is (p. 23).
- His informal characterizations (quoted by Lycan from Donnellan 1966: 285–6): the referential speaker uses the description to help the audience pick out what he is talking about. The description is "merely one tool", replaceable by another description or a name (p. 23). Note 11 (p. 30) says these characterizations do not perfectly line up.
- **Near-miss cases** (from Linsky): "Her husband is kind to her" said of a woman and her unmarried male companion. Another is the "man drinking a martini" whose glass holds water. **Donnellan and Linsky's view:** the companion is referred to and what is said holds of him, even though no semantic referent exists (p. 24). The *Pink Panther* joke ("That is not my dog") illustrates the contrast (p. 24).

**Kripke's reply (p. 24–25).** Kripke, following Grice, distinguishes expression meaning from speaker meaning. In near-miss cases the speaker means the companion and says something literally false, as with sarcastic "Albert's an elegant fellow".
- The **speaker-referent** of a description is the object the speaker intended to call to the audience's attention (p. 25).
- Communication goes by speaker-meaning, so it succeeds even if the sentence is literally false. Kripke concludes that Donnellan has not shown that a sentence with a description can be true when its semantic referent is absent or something else (p. 25).

**Why the distinction still matters (p. 25–26).**
- Lycan says Donnellan has shown that succeeding in referring by a description does not always go by the semantic referent (p. 25).
- It affects truth-values in embedded clauses. In (13) "I know that's right because I heard it from the town doctor," the truth-value may depend on attributive versus referential reading. In (14) "I wish that her husband weren't her husband," the most natural reading is referential then attributive (p. 25).
- Lycan says the ambiguity of (13) and (14) still seems to elude Russell's analysis. A determined Russellian might treat them as scope ambiguities, as with (7) and (9) (p. 26; note 12, p. 30).

**"Actual referent" (p. 26).** What is meant by the actual referent seems to be the object about which the speaker actually succeeded in making a statement. Lycan says the notion is distinct from the other two, and that it remains controversial whether, in the referential case, the actual referent is always the speaker-referent.
- MacKay argues that the actual referent may sometimes be the semantic referent rather than the speaker-referent. His cases: asking for "the rock on the table" while meaning the book. I have asked for the rock. In the Schumacher bet, "the glorious winner" is Fat Freddy Phreak, and I owe $5 (p. 26).
- A speaker's intentions can be arbitrarily crazy: "Mrs Thatcher's Christmas bastard" would not be correctly reported as saying that Donnellan wrote the article (p. 26).
- Lycan asks whether "actual referent" is just a confusion of semantic referent and speaker-referent. Kripke roughly takes that line, using an idea of Grice's from Chapter 13 (p. 26).

### Anaphora (pp. 27–28)
- Russell exempts plural and generic uses and does not mention anaphoric uses. These are ostensibly singular referring expressions (p. 27).
- An **anaphoric** expression inherits its meaning from an antecedent. In (15) "The man who lived around the corner was eccentric. He used to snack on turtle heads," Geach's "pronoun of laziness" idea (one theory among several) makes "he" abbreviate the antecedent phrase. If Geach is right, (15) poses no problem for Russell (p. 27).
- **Evans's objection:** this fails when the antecedent is a quantifier phrase or indefinite description. Substituting the antecedent into (16) "Just one turtle came down the street. It was running…" can make it false when (16) is true. In (17) "A rabbit appeared… It seemed unconcerned," the paraphrase loses the particular rabbit (p. 27).
- **Russell's possible rejoinder:** (16) and (17) contain no definite descriptions. Lycan replies: if the "It"s in (16) and (17) are not pronouns of laziness, why think "He" in (15) is one? (p. 27).
- Descriptions can also be anaphors. In (18) "The turtle" can abbreviate "The turtle that came down the street". In (19) "A rabbit appeared… The rabbit seemed unconcerned," the same move would entail that at most one rabbit appeared. (19) does not entail that, since it is consistent with several rabbits. A speaker of (19) does suggest there was just one, but adding that there were several would not be contradictory (p. 28).
- Neale tries a conservative Russellian treatment. Heim, Kamp and Reyle argue that a broader format is needed. Further open issues include whether "the" even entails contextual uniqueness, the relation to indefinite descriptions, and plurals (p. 28).

### Summary (p. 28)
Lycan's summary: Russell defended the theory directly and by its solutions to the four puzzles. Strawson argues that Russell treats sentences too abstractly and ignores presupposition failure and context-bound descriptions. Donnellan calls attention to the referential use, also ignored by Russell, and tries, not altogether successfully, to distinguish it from the attributive use. It is not obvious that the theory covers all anaphoric uses (p. 28).

## Toy example (ours, not from the text)
Domain: Ann, Bo, Cy. $M$ = "is mayor", $T$ = "is tall". Sentence: "The mayor is tall", i.e. $(\exists x)(Mx \,\&\, (y)(My \rightarrow y=x) \,\&\, Tx)$.
- **Case 1:** only Ann is mayor, and Ann is tall. Existence: $MAnn$ is true. Uniqueness: for $y$ = Ann, $y=x$; for Bo and Cy, $My$ is false, so the conditional is true. Tall: true. The sentence is **true**.
- **Case 2:** nobody is mayor. $(\exists x)Mx$ is false, so the whole conjunction is **false** (Russell). Strawson would say no statement is made, with no truth-value.
- **Case 3:** Ann and Bo are both mayor. Take $x$ = Ann, $y$ = Bo. $MBo$ is true but $Bo \neq Ann$, so the uniqueness clause fails for Ann, and symmetrically for Bo. The sentence is **false**.
- **Scope, in Case 2:** "The mayor is not tall" with "not" attached to the predicate (description in primary position), $(\exists x)(Mx \,\&\, \ldots \,\&\, \sim Tx)$, is false because there is no mayor. The reading with "not" applied to the whole sentence (description in secondary position) $\sim(\exists x)(Mx \,\&\, \ldots \,\&\, Tx)$ is true. This is the scope contrast of (7) (pp. 15–16).

## Concepts
- [[theory of descriptions]] — "The F is G" abbreviates: at least one F, at most one F, whoever is F is G (p. 13)
- [[logical form vs. grammatical form]] — surface subject–predicate form can hide quantificational structure, as with "nobody" (p. 14)
- [[singular-term]] (new) — an expression purporting to denote one individual: name, description, pronoun, demonstrative (p. 10)
- [[quantifier]] (new) — a word like "some", "all", "no" that quantifies general terms (p. 13)
- [[scope-distinction]] (new) — whether a description's quantifiers fall inside or outside "not" or "believes" (primary/wide vs. secondary/narrow) (p. 16)
- [[referential-opacity]] (new) — a position where substituting co-denoting terms may change truth-value (Quine) (p. 12)
- [[Frege's puzzle]] — a true identity can be informative and contingent though both terms co-denote (p. 11)
- [[sense (Sinn) vs. reference (Bedeutung)]] — Frege posits senses so a term can be meaningful without a referent (p. 11)
- [[presupposition-failure]] (new) — Strawson: using a non-denoting description usually yields no statement and no truth-value (p. 20; exceptions in note 9, p. 30)
- [[restricted-quantification]] (new) — quantifier domains are set by context, not universal (p. 21)
- [[attributive-vs-referential-use]] (new) — Donnellan: "whoever fits" versus "picks out this one" use of a description (p. 23)
- [[speaker (non-natural) meaning]] — here, speaker-reference: the object the speaker intends to call attention to (Kripke, citing Grice) (p. 25)
- [[semantic-referent]] (new) — what in fact uniquely satisfies a description in context (p. 18)
- [[compositionality]] (new) — meaning of a complex expression is fixed by its parts and their combination (p. 18)
- [[anaphora]] (new) — an expression inheriting meaning from an antecedent (p. 27)

## Canonical instances
- [[moriarty-bald]] — apparent reference to a nonexistent (p. 10)
- [[pegasus-never-existed]] — negative existential puzzle (p. 11)
- [[twain-clemens]] — Frege's puzzle and substitutivity (pp. 11–12)
- [[author-of-waverley]] — the paradigm Russellian analysis (p. 13)
- [[present-king-of-france]] — falsity (Russell) versus no truth-value (Strawson) (pp. 14, 19–20)
- [[smiths-murderer]] — attributive/referential contrast (p. 23)
- [[the-table-covered-with-books]] — context-bound description (p. 20)
- [[turtle-and-rabbit-anaphora]] — anaphora cases (16)–(19) (pp. 27–28)

## Bridges (candidates)
- [structural-analogy] Russell's "nobody"/"the F" as quantifiers, not names ↔ logic: variable binding in predicate logic — grammar hides binding structure.
- [structural-analogy] Quantifier-domain restriction ↔ statistics: conditioning on a reference population — a statement's truth depends on the contextual pool.
- [metaphor] Strawson's "people refer, not expressions" ↔ computational social science: measuring what a coded variable means requires knowing how coders actually use it.

## Questions this raises
- If ordinary proper names abbreviate descriptions (Russell's reply, p. 19), do the four puzzles really go away for names?
- Is "no truth-value" (Strawson) or "false" (Russell) the better verdict for the King of France sentence? What is the Russellian reply deferred to Chapter 13 (p. 20)?
- Is Donnellan's distinction an ambiguity in the sentence or only a difference in speaker-meaning (pp. 23, 25)?
- Does the notion of an "actual referent" add anything to semantic referent and speaker-referent (p. 26)?

## Exercises worth doing
- Question 1 (p. 29) — assess Russell's solutions to the four puzzles — difficulty: medium
- Question 4 (p. 29) — refine Donnellan's intuitive contrast — difficulty: hard
- Question 7 (p. 29) — extend Russell's theory to the anaphora examples — difficulty: hard
- Note 6 (p. 30) — solve the Problem of the Excluded Middle using Russell's tools — difficulty: medium
- Note 12 (p. 30) — treat (13) and (14) as scope ambiguities — difficulty: medium

## Reading notes
- Printed page = pdf − 15 (pdf 24 = printed 9).
- In the page text, the logical symbols appear as odd glyphs (for example "ð9xÞ" for (∃x)). The formulas (a)–(d) and those for (7) and (8) are transcribed from that text and agree with Lycan's verbal paraphrases.
- Lycan's own notation uses "(x)" for the universal quantifier, "∽" or "~" for negation, and "&" for conjunction. I kept this notation.
- "Scotch" in (5) is Russell's usage, as Lycan notes (note 4, p. 29).
- Further Reading prints "vol. 144, October 2005" for the *Mind* special issue (p. 30). I have not checked this against any other source.
- Donnellan is quoted via Lycan with page references to Donnellan 1966 (pp. 285–7). Those are not printed pages of this book.
