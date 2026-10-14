---
id: magnus-2025-forallx/ch08-use
work: magnus-2025-forallx
unit: "8 Use and mention"
pages: 62-67
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Use and mention

## L0 — One line
To talk about a word or symbol rather than with it, you usually have to mark it as mentioned, and this matters for how we talk about the formal language TFL.

## L1 — The gist (≤ 120 words)
When we talk about the world we use words. When we talk about words we mention them, usually with quotation marks. The chapter applies this to logic. TFL is, for the most part, the object language (the language being studied). English, with extra vocabulary, is the metalanguage (the language we use to talk about it). To talk about any arbitrary TFL sentence we need script letters, called metavariables, which belong to the metalanguage, not to TFL. The chapter stipulates two shortcuts: '¬𝒜' abbreviates a phrase about concatenation (joining symbols in order), and the argument symbol '∴' needs no quotation marks. The shortcuts avoid a long-winded phrase and hard-to-read quotation marks.

**Prerequisites:** the idea of a sentence and of TFL sentence letters; the recursive (inductive) definition of a TFL sentence from chapter 6 (§6.2).

## L2 — Key ideas
- Using a word talks about the thing; mentioning it talks about the word. Mentioning is marked by quotation marks or by centred display (pp. 62–63).
- Confusing use and mention gives false sentences (for example, saying that the name of a man was a philosopher) or gibberish (pp. 63–64).
- The object language is the language under study (for the most part, TFL). The metalanguage is the language used to describe it (augmented English) (pp. 63–65).
- A TFL expression cannot simply be dropped into an English sentence. It must be mentioned, for example with quotation marks around the sentence letter D (p. 64).
- Script letters 𝒜, ℬ, 𝒞, … are metavariables. They are metalanguage symbols used to talk about arbitrary TFL expressions (p. 65).
- Putting quotation marks around '¬𝒜' fails, because it mixes a TFL symbol with a metalanguage symbol. A correct but long-winded alternative speaks of concatenating the symbol '¬' with the sentence 𝒜 (p. 65).
- By stipulation, '¬𝒜' and similar expressions abbreviate the concatenation phrase (p. 66).
- '𝒜₁, …, 𝒜ₙ ∴ 𝒞' is metalanguage notation marking premises and conclusion. Quotation marks around the flanking sentences are stipulated away (pp. 66–67).

## L3 — Walkthrough

### 8.1 Quotation conventions
- Two sentences contrast. "Aristotle is the founding father of logic" uses the name. "The expression 'Aristotle' is composed of one uppercase letter and eight lowercase letters" mentions it (p. 62).
- General point: to talk about things in the world we just use words. To talk about words we typically have to mention them, and some convention is needed to show this (p. 62).
- Conventions: quotation marks, or displaying the expression centrally on the page (pp. 62–63).
- Examples (p. 63):
  - "'Aristotle' was an ancient Greek philosopher" says that some expression was a philosopher, which is false. The man was one, his name was not.
  - The same claim about letters, made about the man himself (no quotation marks around the name), is also false. The man is made of flesh, not letters.
  - "'"Aristotle"' is the name of 'Aristotle'" is true. The left side is the name of a name, the right side is a name.
- The quotation marks here do not mark reported speech. They mark a move from talking about an object to talking about a name of it (p. 63).

*Intuition note:* Quotation marks work like a switch. Without them a word points at its object. With them we talk about the word itself.

### 8.2 Object language and metalanguage
- The language we talk about is the **object language**. The language we use to talk about it is the **metalanguage** (p. 63).
- For the most part, the object language here has been TFL and the metalanguage is English. It is not exactly conversational English, but English with additional vocabulary (pp. 63–64).
- Sentence letters (A, B, C, Z, A₁, B₄, A₂₅, J₃₇₅, …) are TFL expressions, not English ones. So "D is a sentence letter of TFL" is gibberish, like a German sentence dropped into English with no quotation marks around it. What we mean is 'Schnee ist weiß' is a German sentence, and likewise "'D' is a sentence letter of TFL" (p. 64).
- Whenever we want to talk in English about some specific TFL expression, we need to indicate that we are mentioning it, with quotation marks or a similar convention such as central display (p. 64).

### 8.3 Metavariables
- We also need to talk about any arbitrary TFL sentence, as in the inductive definition of §6.2. For that we use script letters 𝒜, ℬ, 𝒞, 𝒟, …. They belong to the augmented metalanguage, not to TFL (p. 65).
- Clause 2 of the definition: "If 𝒜 is a sentence, then ¬𝒜 is a sentence" (p. 65).
- Alternative 2′ uses the sentence letter 'A' and the expression '¬A' in quotation marks. It fails because it would not let us decide whether '¬B' is a sentence (p. 65).
- A **metavariable** is a symbol of augmented English used to talk about expressions of TFL. By contrast, 'A' is a particular TFL sentence letter (p. 65).
- Should clause 2 have quotation marks? The right-hand expression '¬𝒜' is not a sentence of English, since it contains '¬'. Alternative 2″ puts quotation marks around '¬𝒜' in the clause. That is no good: '¬𝒜' is not a TFL sentence, since 𝒜 is a symbol of augmented English, not of TFL (p. 65).
- What we really want to say is something like 2‴, which the author calls impeccable but long-winded: "If 𝒜 is a sentence, then the result of concatenating the symbol '¬' with the sentence 𝒜 is a sentence" (pp. 65–66).
- Shortcut: we can stipulate that '¬𝒜' is read directly in terms of rules for concatenation. Officially, the metalanguage expression '¬𝒜' abbreviates that concatenation phrase. Likewise for '(𝒜 ∧ ℬ)', '(𝒜 ∨ ℬ)', etc. (p. 66).

*Intuition note:* A metavariable is a blank in a recipe. It stands for whichever TFL sentence you pick. The recipe '¬𝒜' says to put a negation sign in front of it.

### 8.4 Quotation conventions for arguments
- We can symbolize each sentence of an English argument in TFL. But TFL itself has no way to flag which sentences are premises and which is the conclusion, whereas English uses words like 'so' and 'therefore' (p. 66).
- New notation: with premises 𝒜₁, …, 𝒜ₙ and conclusion 𝒞, we write $\mathcal{A}_1,\ldots,\mathcal{A}_n \therefore \mathcal{C}$. The role of '∴' is simply to indicate which sentences are the premises and which is the conclusion (p. 66).
- Strictly, '∴' is part of the metalanguage, not the object language, so one might think we need quotation marks around the flanking TFL sentences. That is a sensible thought, but the marks would make things harder to read, and since we are stipulating conventions anyway, we stipulate that they are unnecessary (pp. 66–67).
- Example: $A, A \to B \therefore B$ indicates an argument whose premises are (symbolized by) 'A' and 'A → B' and whose conclusion is (symbolized by) 'B' (p. 67).

*Intuition note:* '∴' is a label in our commentary, not a symbol of TFL. Writing the argument without quotes is a convenient agreement, not a claim that '∴' is a TFL symbol.

## Toy example
(Ours.) Use vs. mention: *Paris is in France* uses the name, and is true. *'Paris' has five letters* mentions the name. P-a-r-i-s gives 5 letters, so it is true. *Paris has five letters* is false, since a city is not made of letters.

Metavariable: let 𝒜 be the TFL sentence 'P'. Then '¬𝒜' abbreviates the result of concatenating '¬' with 'P', which is '¬P'. Let ℬ be '(P ∧ Q)'. Then '¬ℬ' gives '¬(P ∧ Q)'. One clause with a metavariable covers both cases. Clause 2′ mentioned only 'A', so it did not let us decide about '¬B'.

## Concepts
- [[use vs. mention]] — talking with a word versus talking about the word, marked by quotes (p. 62)
- [[object language]] (new) — the language being talked about, here (for the most part) TFL (p. 63)
- [[metalanguage]] (new) — the language used to talk about the object language, here augmented English (p. 63)
- [[metavariable]] (new) — a script letter in the metalanguage used to talk about arbitrary TFL expressions (p. 65)
- [[concatenation]] (new) — joining symbols in order, e.g. '¬' placed before a sentence (p. 65)
- [[argument notation (∴)]] (new) — metalanguage symbol marking premises and conclusion (p. 66)

## Canonical instances
- [[aristotle-name-vs-man]] — the man vs. his name 'Aristotle', with true and false sentences (pp. 62–63)
- [[schnee-ist-weiss]] — foreign-language sentence needs quotation marks (p. 64)
- [[negation-clause-2-variants]] — clauses 2, 2′, 2″, 2‴ for '¬𝒜' (p. 65)
- [[A-A-to-B-therefore-B]] — argument written without quotation marks (p. 67)

## Bridges (candidates)
- [structural-analogy] metavariable ↔ algebra: a letter standing for any value in a general formula — 𝒜 stands for any sentence as x stands for any number.
- [structural-analogy] object language/metalanguage ↔ linguistics: a language textbook written in another language, such as German examples explained in English.
- [metaphor] quotation marks ↔ a picture frame: they mark an expression as displayed rather than used.

## Questions this raises
- Does stipulating '¬𝒜' as an abbreviation hide any ambiguity when the metavariable is replaced by a long sentence?
- If metalanguage is English plus extra vocabulary, can we also study the metalanguage itself, and in what further language?
- Why is it useful to keep '∴' out of TFL rather than adding it as a connective?
- Are there everyday cases where confusing use and mention causes real misunderstandings?

## Reading notes
- Printed page = pdf − 10 (pdf 72 = printed 62). Source pages: printed 62–67.
- The text layer shows script letters 𝒜, ℬ as plain A, B in places. The images of pp. 65–66 show the script forms. On p. 67 no image was supplied, so whether the premises in 'A, A → B ∴ B' are italic sentence letters (TFL) cannot be checked. The text says the premises are "(symbolized by)" 'A' and 'A → B', and the conclusion is "(symbolized by)" 'B'.
- On p. 64 the author calls 'D' a sentence of TFL while introducing it as a sentence letter. I report this as printed.
- No exercises appear in this unit.
