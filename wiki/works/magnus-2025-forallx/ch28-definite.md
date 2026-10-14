---
id: magnus-2025-forallx/ch28-definite
work: magnus-2025-forallx
unit: 28 Definite descriptions
pages: 243–252
fields: [analytic-philosophy]
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
# Definite descriptions

## L0 — One line
Russell's analysis lets FOL symbolize *the F is G* with quantifiers and identity alone: there is exactly one F, and it is G.

## L1 — The gist (≤ 120 words)
How should FOL handle phrases like *the traitor*, which are meant to pick out one unique object? The chapter calls inventing names probably a bad idea, and it would prefer not to add a new operator. It adopts Russell's analysis: *the F is G* says there is at least one F, at most one F, and every F is G. This handles empty descriptions such as *the present King of France*, and it separates outer from inner negation. It extends to possessives, *both* and *neither*. The authors then discuss two objections (Strawson's and Donnellan's), reply briefly to each, and for now stick with Russell's analysis, as the best they can offer without significantly revising logic.

**Prerequisites:** FOL quantifiers and identity; numerical quantification (exactly one, exactly two); names must denote, predicates may be empty (chs. 23, 24, 26).

## L2 — Key ideas
- Definite descriptions (*the traitor*) aim at a unique object. Introducing a new name for each one is probably a bad idea, since we want to keep the information that the traitor is a traitor. A new operator ι would make descriptions behave like names, but it adds a symbol to FOL, which the authors would prefer to avoid (pp. 243–244).
- Russell: *the F is G* iff there is at least one F, at most one F, and every F is G. The word *the* does not appear on the right-hand side (p. 244).
- In FOL this becomes $\exists x[(F(x)\land\forall y(F(y)\to x=y))\land G(x)]$. No new symbol is needed (p. 245).
- Empty descriptions cause no trouble, because predicates may be empty and names may not (p. 246).
- Outer negation (negation over the whole sentence) differs from inner negation (negation inside the description's scope). Inner entails outer, not conversely (p. 247).
- The analysis extends to possessives (*Smith's murderer*), *both* and *neither* (pp. 247–249).
- Strawson (truth-value gaps) and Donnellan (mistaken identity) object. The authors reply that the intuitions are unclear, then for now keep Russell's analysis for FOL (pp. 249–250).

## L3 — Walkthrough

### Introduction (p. 243)
The sentences are: 1. *Nick is the traitor.* 2. *The traitor went to Cambridge.* 3. *The traitor is the deputy.* These are definite descriptions, meant to pick out a unique object. They differ from indefinite descriptions (*Nick is a traitor*) and from generics (*The whale is a mammal*, when it is inappropriate to ask which whale). The question: how should FOL deal with definite descriptions? (p. 243)

### 28.1 Treating descriptions as terms (pp. 243–244)
- Option 1: introduce a new name for each description. The authors say this is probably not a great idea, since we know the traitor is a traitor and want to keep that information. (p. 243)
- Option 2: add an operator ι, so *the F* becomes $\iota x\,F(x)$ (think: the $x$ such that $F(x)$). Such expressions would behave like names. (p. 244)
- Key: domain people; $T$: traitor; $D$: deputy; $C$: went to Cambridge; $n$: Nick. Sentences 1–3 become $n=\iota x\,T(x)$, $C(\iota x\,T(x))$ and $\iota x\,T(x)=\iota x\,D(x)$. (p. 244)
- The authors say it would be nice not to add a new symbol to FOL, and that we might make do without one. (p. 244)

### 28.2 Russell's analysis (pp. 244–246)
- Russell's analysis: the F is G iff there is at least one F, *and* at most one F, *and* every F is G. The word *the* does not occur on the right. Russell is aiming to explain descriptions in terms that do not presuppose them. (pp. 244–245)
- Worry: *the table is brown* can be said without implying there is one table in the universe. The authors say this is not (yet) a fantastic counterexample, since the domain is likely to be restricted by context. (p. 245)
- Using numerical quantification, the three conjuncts are
$$\exists x F(x)\land\forall x\forall y((F(x)\land F(y))\to x=y)\land\forall x(F(x)\to G(x))$$
- The first two conjuncts amount to the claim that there is exactly one F, and the last says that object is G. So an equivalent, crisper form is
$$\exists x\big[(F(x)\land\forall y(F(y)\to x=y))\land G(x)\big]$$
- Sentence 1: $\exists x[T(x)\land\forall y(T(y)\to x=y)\land x=n]$. Sentence 2: $\exists x[T(x)\land\forall y(T(y)\to x=y)\land C(x)]$. (p. 245)
- Sentence 3 links two descriptions. It is paraphrased as: there is exactly one traitor $x$, exactly one deputy $y$, and $x=y$:
$$\exists x\exists y\big([T(x)\land\forall z(T(z)\to x=z)]\land[D(y)\land\forall z(D(z)\to y=z)]\land x=y\big)$$
The formula $x=y$ must fall within the scope of both quantifiers. (pp. 245–246)

*Intuition note:* *The traitor* is not treated as a name. It becomes a claim that exactly one thing is a traitor, plus whatever we say about that thing.

### 28.3 Empty definite descriptions (pp. 246–247)
- A name $k$ for the present King of France would go wrong. A name must pick out an object in the domain, and whatever domain we choose will contain no present king of France. (p. 246)
- Russell uses predicates and quantifiers instead of names. Predicates can be empty, so no difficulty arises when the description is empty. (p. 246)
- Example adapted from Neale: Alex claims 4. *I am dating the present king of France.* Key: $a$ Alex; $K(x)$: $x$ is a present king of France (an indefinite, not a definite, description); $D(x,y)$: $x$ is dating $y$. Symbolization: $\exists x[(K(x)\land\forall y(K(y)\to x=y))\land D(a,x)]$. (pp. 246–247)
- This can be false in at least two ways:
  - Sentence 5 says that there is no one who is both the present King of France and such that he and Alex are dating. Symbolization: $\neg\exists x[(K(x)\land\forall y(K(y)\to x=y))\land D(a,x)]$. This is *outer negation*, since the negation governs the whole sentence. It is true if there is no present King of France.
  - Sentence 6 says that there is a unique present King of France, but Alex is not dating him. Symbolization: $\exists x[(K(x)\land\forall y(K(y)\to x=y))\land\neg D(a,x)]$. This is *inner negation*, since the negation is within the scope of the description. Its truth requires a present King of France who is not dating Alex.
  - Sentence 6 entails 5 (as do their symbolizations), but not vice versa. (p. 247)

*Intuition note:* Negation can attach to the whole claim or only to what is said about the king. Only the second version commits you to there being a king.

### 28.4 Possessives, *both*, *neither* (pp. 247–249)
- *Smith's murderer* means something like *the person who murdered Smith*, so it is a disguised definite description. On Russell's analysis, sentence 7, *Smith's murderer is insane*, can be false in three ways: the one murderer is not insane; no one murdered Smith; or more than one person did. (pp. 247–248)
- Key: $I(x)$: insane; $M(x,y)$: $x$ murdered $y$; $m$: Smith. Symbolization: $\exists x[M(x,m)\land\forall y(M(y,m)\to x=y)\land I(x)]$. (p. 248)
- *Both Fs are G* says there are exactly two Fs, and each is G. *Neither F is G* says there are exactly two Fs, and neither is G.
$$\exists x\exists y\big[F(x)\land F(y)\land\neg x=y\land\forall z(F(z)\to(x=z\lor y=z))\land G(x)\land G(y)\big]$$
$$\exists x\exists y\big[F(x)\land F(y)\land\neg x=y\land\forall z(F(z)\to(x=z\lor y=z))\land\neg G(x)\land\neg G(y)\big]$$
(p. 248)
- Compare *exactly two Fs are Gs* (§26.5, i.e. exactly two things are both F and G):
$$\exists x\exists y\big[(F(x)\land G(x))\land(F(y)\land G(y))\land\neg x=y\land\forall z((F(z)\land G(z))\to(x=z\lor y=z))\big]$$
The difference is in the antecedent of the conditional. For *both*, there cannot be any Fs other than $x,y$, whether they are Gs or not. For *exactly two*, we only require that there are no other Fs that are also Gs. (pp. 248–249)
- So *both Fs are Gs* implies *exactly two Fs are Gs*. The converse does not hold, since there might be a third F that is not a G. (p. 249)

### 28.5 The adequacy of Russell's analysis (pp. 249–250)
The authors say they will restrict themselves to two observations. (p. 249)
- **Strawson's worry:** If there are no Fs, then on Russell's analysis both *the F is G* and *the F is non-G* are false. Strawson suggested that such sentences involve presupposition failure and are neither true nor false. If we agree with Strawson, we will need to revise our logic, which has two truth values and assigns every sentence exactly one. The authors reply that there is room to disagree: it is not clear that Strawson's intuitions are very robust, and they ask whether it is not just false, not "gappy", that Tim is dating the present King of France. (p. 249)
- **Donnellan's worry (mistaken identity):**
  - Malika sees a very tall man drinking what looks like a gin martini and a very short man drinking what looks like a pint of water. She says 8. *The gin-drinker is very tall!* (p. 249)
  - Russell's analysis renders this as 8′: there is exactly one gin-drinker [in the corner], and whoever is a gin-drinker [in the corner] is very tall. (p. 250)
  - Suppose the tall man is actually drinking water from a martini glass and the short man is drinking neat gin. By Russell's analysis, Malika has said something false, but, the worry asks, don't we want to say she said something true? (p. 250)
  - The authors' reply: one might wonder how clear our intuitions are here. Malika intended to pick out a particular man and say something true of him. On Russell's analysis she picked out the short man and said something false of him. The authors say that maybe advocates of Russell's analysis only need to explain why her intentions were frustrated, and this is easy: she said something false because she had false beliefs about the drinks. (p. 250)
- Conclusion: more discussion would lead into deep philosophical waters and distract from learning formal logic. So for now the authors stick with Russell's analysis for putting things into FOL. They call it certainly the best they can offer "without significantly revising our logic", and quite defensible. (p. 250)

## Toy example (ours)
Domain $\{1,2,3\}$. Let $G$ hold of 2 and 3. Test $\exists x[(F(x)\land\forall y(F(y)\to x=y))\land G(x)]$.
- Case $F=\{2\}$. Take $x=2$: $F(2)$ is true. For $y=1$ and $y=3$, $F(y)$ is false, so the conditional is true. For $y=2$, $2=2$. $G(2)$ is true. So *the F is G* is **true**.
- Case $F=\{2,3\}$. Take $x=2$: with $y=3$, $F(3)$ is true but $2=3$ is false, so the $\forall y$ clause fails. Likewise $x=3$ fails with $y=2$. For $x=1$, $F(1)$ is false. So the sentence is **false** (two Fs).
- Case $F=\emptyset$. No $x$ satisfies $F(x)$, so the sentence is **false**. Its outer negation is true, and its inner-negation version $\exists x[(F(x)\land\forall y(F(y)\to x=y))\land\neg G(x)]$ is also false.

## Concepts
- [[theory of descriptions]] — *the F is G* means at least one F, at most one F, and every F is G (p. 244)
- [[logical form vs. grammatical form]] — *the traitor* is analysed with predicates and quantifiers rather than as a name (pp. 245–246)
- [[analysis]] — Russell's analysis restates descriptions without using *the* (p. 244)
- [[definite-description]] (new) — phrase meant to pick out a unique object, contrasted with indefinite descriptions and generics (p. 243)
- [[empty-description]] (new) — description satisfied by nothing (or, as in the murderer example, by more than one thing); with no Fs, both *the F is G* and *the F is non-G* come out false on Russell's analysis, while an outer-negated sentence is true (pp. 247–249)
- [[outer-vs-inner-negation]] (new) — negation over the whole description sentence vs. inside its scope (p. 247)
- [[presupposition-failure]] (new) — Strawson's suggested view: with no F, *the F is G* is neither true nor false (p. 249)

## Canonical instances
- [[present-king-of-france]] — empty description; shows outer vs. inner negation (pp. 246–247)
- [[smiths-murderer]] — possessive as disguised description; three ways to be false (pp. 247–248)
- [[malika-gin-drinker]] — Donnellan's mistaken-identity case against Russell (pp. 249–250)

## Bridges (candidates)
- [structural-analogy] Russell's *the F is G* ↔ database/programming: a lookup that must return exactly one record, failing on zero or many — mirrors the "at least one / at most one" conditions.
- [same-math] *Both Fs are G* ↔ same book's numerical quantification (§26.5): same quantifier-plus-identity machinery.

## Questions this raises
- If Strawson is right, what would a three-valued logic for FOL look like?
- Can Donnellan's worry be explained by what speakers intend, rather than by what the sentence says?
- How does context restrict the domain so that *the table* works?
- Does *the* always carry uniqueness, as in *the whale is a mammal*?

## Exercises worth doing
- Ex. A.4, A.6, A.7 (p. 251) — *only* and *the person who…* in FOL — difficulty: medium
- Ex. B.8, B.10 (p. 252) — descriptions inside conditionals (the deuce of clubs) — difficulty: medium
- Ex. C.6–C.8 (p. 252) — descriptions that may be empty (the Pegasus) — difficulty: medium
- Ex. D (p. 252) — why simpler forms are equivalent for a name — difficulty: hard

## Reading notes
- Printed = pdf − 10.
- The text layer garbles the ι operator and the brackets in formulas; the page images show them clearly and were used.
- The phrase "Sentences 1–3" refers to the chapter's opening sentences, not to the exercise numbers.
