---
id: magnus-2025-forallx/ch07-ambiguity
work: magnus-2025-forallx
unit: "7 Ambiguity"
pages: 56–61
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Ambiguity

## L0 — One line
English sentences can have several meanings, but every sentence of TFL (the book's formal language) has exactly one reading, so TFL can be used to separate the readings of an ambiguous English sentence.

## L1 — The gist (≤ 120 words)
The chapter asks how ambiguity in English, whether in words or in structure, can be handled. Lexical ambiguity comes from words with several meanings. Structural ambiguity comes from several ways of reading a sentence. Scope ambiguity is one kind of structural ambiguity: it arises when a connective such as "not", "and" or "or" can be read as inside or outside another. Usually only one meaning is intended, and context (or sometimes the way a sentence is uttered) determines which. Ambiguity is not the same as vagueness. TFL sentences cannot be structurally ambiguous, so we can write each reading as a separate formula. The Casement treason trial shows that a legal ambiguity can decide a life.

**Prerequisites:** TFL connectives ¬, ∧, ∨; sentence letters; symbolization keys; brackets showing grouping.

## L2 — Key ideas
- A sentence is ambiguous if it has more than one meaning. Lexical ambiguity comes from a word ("bank"). Structural ambiguity comes from the sentence's construction (*Flying planes can be dangerous*) (p. 56).
- Usually only one meaning is intended; context, or sometimes how the sentence is uttered (for instance, which parts are stressed), determines which. When one reading is much more likely, the other can be hard to see, and this is often why a joke works (p. 57).
- Ambiguity differs from vagueness. A vague word has borderline cases. In TFL the authors aim to avoid ambiguity, e.g. by giving symbolization keys that avoid ambiguous words or disambiguate them. Vagueness is harder to avoid: borderline cases cannot be accommodated, because every case must make every basic sentence true or false (p. 57).
- Every TFL sentence has exactly one reading. That makes TFL a tool for showing what an ambiguous English sentence might mean (pp. 57–58).
- Clear statement matters in law. Casement's death sentence turned on how to read a comma in the Treason Act, which TFL can represent as two formulas (pp. 58–59).
- A common source of structural ambiguity in English is its lack of brackets; the examples are ambiguities in how "not", "and" and "or" combine (pp. 59–60).
- Scope ambiguities depend on whether one connective is in the scope of another, e.g. ¬(L ∧ B) versus ¬L ∧ B (pp. 60–61).

## L3 — Walkthrough

**Two kinds of ambiguity (p. 56).**
- *Lexical ambiguity*: a sentence contains a word with more than one meaning. *I went to the bank* may mean the river bank or the financial institution. The meaning depends on the context of utterance (p. 56).
- *Structural ambiguity*: the sentence can be interpreted in different ways, and each interpretation selects a different meaning (p. 56).
- Chomsky's example is "Flying planes can be dangerous." In one reading "flying" is an adjective modifying "planes": planes that are in flight are dangerous. In the other it is a gerund, so the act of flying a plane is dangerous (p. 56).
- The authors' uses: warning someone about to launch a hot air balloon, or counselling someone against becoming a pilot (p. 56).

> **Intuition note.** The same words can be read in different ways, and each reading says something different. In structural ambiguity the source is how the sentence is interpreted, not a word with several meanings.

**Context and jokes (p. 57).** Usually only one meaning is intended. Context determines which, or sometimes how the sentence is uttered, e.g. which parts are stressed (p. 57). Often one reading is so likely that the other is hard to "see". This is often why a joke works. Groucho Marx's "One morning I shot an elephant in my pajamas" is the example (p. 57).

**Ambiguity versus vagueness (p. 57).**
- An adjective such as "rich" or "tall" is vague when it is not always possible to say whether it applies (p. 57).
- A 6 ft 4 in person is pretty clearly tall, but a building of that size is tiny. Context plays a role in determining the clear cases and clear non-cases (*tall for a person*, *for a basketball player*, *for a building*). Even in a clear context, a middle range of cases remains (p. 57).

**Ambiguity and TFL (pp. 57–58).**
- We generally aim to avoid ambiguity in TFL. The authors will try to give symbolization keys that do not use ambiguous words, or that disambiguate them. For example, *Rebecca went to the (money) bank* and *Rebecca went to the (river) bank* need two different sentence letters (p. 57).
- Vagueness is harder to avoid. The authors have stipulated that every case, and later every valuation, must make each basic sentence true or false and nothing in between. So TFL cannot accommodate borderline cases (p. 57).
- Every sentence of TFL can be read in one and only one way. The authors call this a strength, because TFL can help show the different meanings of an ambiguous English sentence (p. 57).
- Avoiding ambiguity can be very important. Logic helps philosophers state thoughts clearly, mathematicians state theorems rigorously, and software engineers specify loop conditions, queries and verification criteria (p. 58).

**The law: Roger Casement (pp. 58–59).**
- Casement was a British diplomat. In 1914–16 he secretly went to Germany, with which Britain was at war, and tried to recruit Irish prisoners of war to fight against Britain. He was captured and tried for high treason (p. 58).
- The Treason Act of 1351 says someone is guilty of treason "if a man is adherent to the King's enemies in his realm, giving to them aid and comfort in the realm, or elsewhere" (p. 58).
- The last comma is absent in the original French text of 1351. It was not disputed that Casement had been *adherent to the King's enemies*. The question was whether that was treason only in the realm, or also abroad (p. 58).
- **Defense:** it argued that the law was ambiguous. The claimed ambiguity hinged on whether "or elsewhere" attaches only to "giving aid and comfort" (the natural reading without the comma), or to both "being adherent" and "giving aid and comfort" (the natural reading with the comma) (pp. 58–59).
- The authors say the first reading may seem far fetched, but the argument for it was "not unpersuasive" (p. 59). The court read the passage with the comma, so Casement was sentenced to death. He wrote that he was "hanged by a comma" (p. 59).

Symbolization key (p. 59):
- $A$: Casement was adherent to the King's enemies in the realm.
- $G$: Casement gave aid and comfort to the King's enemies in the realm.
- $B$: Casement was adherent to the King's enemies abroad.
- $H$: Casement gave aid and comfort to the King's enemies abroad.

Reading under which his behavior was not treasonous: $$A \lor (G \lor H)$$

Reading under which he was executed: $$(A \lor B) \lor (G \lor H)$$

In the actual case, $B$ is true and $A$, $G$, $H$ are false (p. 59).

> **Intuition note.** In the defense's argument, the comma matters because it affects whether "adherent" shares the words "or elsewhere". In logic that is the difference between $A$ alone and $A \lor B$ in the first group. With $B$ true and the rest false, the first formula is false and the second is true. (The values come from the author's statement of the facts, p. 59.)

**Scope ambiguity (pp. 59–61).**
- English lacks parentheses, which is a common source of structural ambiguity (p. 59).
- *I like movies that are not long and boring*: you will most likely think the speaker dislikes movies that are long and boring, i.e. likes movies that are not both long and boring. A less likely reading is movies that are both not long and boring (p. 60).
- *I like dishes that are not sweet and flavorful*: here the more likely interpretation is that I like savory, flavorful dishes. The author adds that this could have been said better, e.g. *I like dishes that are not sweet, yet flavorful* (p. 60).
- "And" and "or" also interact. In *a small and dangerous or stealthy animal*, a leopard is stealthy but not small. It does not count if I want small animals that are dangerous or stealthy. It counts if I want either a small, dangerous animal or a stealthy animal of any size (p. 60).
- These are *scope ambiguities*: they depend on whether one connective is in the scope of another (p. 60).

Example with $B$: *Avengers: Endgame* is boring, $L$: it is long (p. 60).
1. *Not: both long and boring*: $\lnot(L \land B)$. Here $\land$ is in the scope of $\lnot$.
2. *Both: not long and boring*: $\lnot L \land B$. Here $\lnot$ is in the scope of $\land$.

Sentence 2 is certainly false, since the film is over three hours long. Whether sentence 1 is true depends on whether you think it boring (p. 60).

Example with $D$: Tai Lung is dangerous, $S$: small, $T$: stealthy (p. 61).
3. *Either both small and dangerous, or stealthy*: $(S \land D) \lor T$. Here $\land$ is in the scope of $\lor$.
4. *Both small and either dangerous or stealthy*: $S \land (D \lor T)$. Here $\lor$ is in the scope of $\land$ (p. 61).

> **Intuition note.** Brackets in TFL show how the connectives are grouped. The same English words, with different grouping, give two different formulas that can have different truth values.

## Toy example (ours, not from the text)
Sentence: "The soup is not hot and salty." Key: $H$ = the soup is hot; $S$ = the soup is salty.
- Reading 1: $\lnot(H \land S)$. Reading 2: $\lnot H \land S$.
- Suppose the soup is hot ($H$ true) and not salty ($S$ false).
- Reading 1: $H \land S$ = true ∧ false = false, so $\lnot(H \land S)$ = true.
- Reading 2: $\lnot H$ = false, so $\lnot H \land S$ = false ∧ false = false.
- The readings get different truth values in the same situation. So the English sentence cannot be assessed until we choose a reading.

## Concepts
- [[ambiguity]] (new) — a sentence has more than one meaning (p. 56)
- [[lexical-ambiguity]] (new) — ambiguity from a word with several meanings (p. 56)
- [[structural-ambiguity]] (new) — ambiguity from several ways of interpreting the sentence's construction (p. 56)
- [[scope-ambiguity]] (new) — structural ambiguity depending on whether one connective is in the scope of another (p. 60)
- [[vagueness]] (new) — an adjective is vague when it is not always determinate whether it applies; related to, not the same as, ambiguity (p. 57)
- [[disambiguation]] (new) — making the meanings clear, e.g. by separate sentence letters or separate formulas (pp. 57, 59)
- [[logical form vs. grammatical form]] — here, one English sentence can correspond to several TFL formulas, each with one reading (pp. 57, 60)

## Canonical instances
- [[flying-planes-ambiguity]] — Chomsky's structural ambiguity: adjective versus gerund (p. 56)
- [[groucho-elephant-pajamas]] — a joke that exploits a likely-versus-unlikely reading (p. 57)
- [[casement-hanged-by-a-comma]] — legal ambiguity in the Treason Act of 1351 (pp. 58–59)
- [[avengers-endgame-not-long-and-boring]] — scope of ¬ and ∧ (p. 60)
- [[tai-lung-small-dangerous-or-stealthy]] — scope of ∧ and ∨ (p. 61)

## Bridges (candidates)
- [structural-analogy] Scope ambiguity ↔ analytic-philosophy: surface grammar hiding logical form — a single surface string has several underlying logical structures.
- [metaphor] Casement's comma ↔ law: interpretation of statutes — one punctuation mark changes which words a phrase modifies.
- [structural-analogy] Brackets in TFL ↔ mathematics: order of operations — grouping fixes which operation applies to which part.

## Questions this raises
- If context settles most ambiguities in conversation, why do jokes and legal disputes still arise?
- Can every ambiguity in English be removed by adding brackets or by splitting a sentence letter? What about vagueness?
- In Casement's case, should a court prefer the "natural reading" or the reading most favorable to the accused?
- Are there structural ambiguities (like "Flying planes…") that TFL cannot display, because they do not involve connectives?

## Exercises worth doing
- Ex. A.1 (p. 61) — "Haskell is a birder and enjoys watching cranes": give a key and symbolize the readings — difficulty: easy
- Ex. A.2 (p. 61) — "The zoo has lions or tigers and bears": scope of ∨ and ∧ — difficulty: medium
- Ex. A.3 (p. 61) — "The flower is not red or fragrant": scope of ¬ and ∨ — difficulty: medium

## Reading notes
- Printed page = pdf page − 10 (pdf 66–71 = printed 56–61).
- Minor misprints in the source: "baloon" (p. 56), "disambiguiation" (p. 59), "far fetched" without a hyphen (p. 59). None affects the content.
- The text layer matched the page images on pp. 59–61. The formulas on pp. 59–61 were checked against the images.
- On these pages TFL is used without being defined; the digest calls it the book's formal language only from how it is used here (symbolization keys, sentence letters, connectives).
- Practice exercise A is printed with no solutions in these pages.
