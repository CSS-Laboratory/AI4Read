---
id: russell-1905-denoting/main
work: russell-1905-denoting
unit: paper
pages: 479–493 (printed pages not visible in the HTML source; cited by paragraph number)
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Russell, "On Denoting" (1905)

## L0 — One line
Phrases like "the present King of France" or "every man" have no meaning on their own; any sentence containing one must be rewritten into a form without it, using "always true" and "sometimes true" of a variable.

## L1 — The gist (≤ 120 words)
Russell asks how to understand phrases such as "a man", "every man" and "the present King of France". They may denote one thing, nothing, or ambiguously. He proposes that such phrases have no meaning alone. Each sentence containing one is analysed into a form with no such phrase, built from "always true" and "sometimes true" of a variable. He argues that Meinong's and Frege's views end in contradiction or in an "inextricable tangle". He claims his view solves three puzzles: George IV and Scott, the excluded middle, and non-being. He says the subject matters for logic, mathematics and the theory of knowledge. He also concludes that the propositions we can think about contain only things we know directly.

**Prerequisites:** basic logic (if–then, "for all", "for some", identity, true/false); the idea of a variable in a sentence frame such as "x is human".

## L2 — Key ideas (5–10 bullets)
- A denoting phrase is a phrase such as *a man*, *all men*, *the King of France*. It is "denoting" by its form alone, and it may denote one object, nothing, or ambiguously (para. 1).
- Russell's principle: denoting phrases never have meaning in themselves, but every proposition containing one does (para. 5).
- "Some", "all", "no" are defined from the one primitive "C(x) is always true" (para. 5–7).
- "The F is G" is analysed as: exactly one thing is F, and it is G. If nothing is F, or several things are, every such proposition with a primary occurrence is false (para. 8–11, 30).
- Meinong's view gives non-subsisting objects that are apt to infringe the law of contradiction (para. 13). Frege's meaning/denotation view seems to make sentences with empty phrases nonsense, though they are not; Frege's fix is conventional denotations, which Russell finds artificial; and Russell finds a tangle about speaking of meanings (para. 15–25).
- Russell claims his theory solves three puzzles: substitution in George IV's wish, the bald King of France, and the "difference between A and B" (para. 17, 29–31).
- Primary versus secondary occurrence of a phrase separates the two readings of "the King of France is not bald" (para. 29–30).
- Every proposition we can apprehend has only things we are acquainted with as constituents. Things known only by denoting phrases, such as matter and other people's minds, are not constituents of any proposition we can apprehend, so we know no proposition having them as constituents (para. 3, 36).

## L3 — Walkthrough
(Paragraph numbers are our own count of prose paragraphs. The source has no headings or page numbers. Lists and displayed formulas are counted inside their introducing paragraph. Section letters are ours.)

### A. Opening (paras 1–4)
- **Denoting phrase:** a phrase like *a man, some man, any man, every man, all men, the present King of England, the center of mass of the solar system…*. It is denoting "solely in virtue of its form" (para. 1).
- Three cases: the phrase denotes nothing (*the present King of France*); it denotes one definite object (*the present King of England*); it denotes ambiguously (*a man* denotes "an ambiguous man", not many men) (para. 1).
- Russell says that all the difficulties he is acquainted with are met, so far as he can discover, by his theory (para. 2).
- Importance for the theory of knowledge: we may know a phrase denotes one definite thing, such as the center of mass, without being acquainted with it. **Acquaintance** means having a thing presented to us. **Knowledge about** means reaching it by denoting phrases. We are acquainted with objects of perception and abstract logical objects. We probably are not acquainted with other minds. "All thinking has to start from acquaintance" but reaches things we are not acquainted with (para. 3).
- Plan: state the theory, discuss Frege and Meinong, give grounds, give consequences (para. 4).

### B. The theory (paras 5–12)
Russell takes the **variable** as fundamental. $C(x)$ is a proposition (more exactly a propositional function) with $x$ wholly undetermined. "$C(x)$ is always true" is taken as ultimate and indefinable (para. 5, notes 2–3):

$$C(\text{everything}) := \text{“}C(x)\text{ is always true”}$$
$$C(\text{nothing}) := \text{“}\text{“}C(x)\text{ is false”}\text{ is always true”}$$
$$C(\text{something}) := \text{“it is false that “}C(x)\text{ is false” is always true”}$$

- *Everything, nothing, something* have no meaning in isolation. Each proposition containing them does (para. 5).
- "I met a man" does not affirm that I met some definite man. It says: "'I met $x$, and $x$ is human' is not always false". In general, $C(\text{a man}) := $ "'$C(x)$ and $x$ is human' is not always false" (para. 6).
- "All men are mortal" is hypothetical (note 5): "'If $x$ is human, $x$ is mortal' is always true". In general (para. 7):
  - $C(\text{all men}) := $ "'if $x$ is human, then $C(x)$ is true' is always true". $C(\text{every man})$ means the same.
  - $C(\text{no men}) := $ "'if $x$ is human, then $C(x)$ is false' is always true".
  - $C(\text{some men})$ means the same as $C(\text{a man})$. Russell sets aside the psychological suggestion of "only one" versus "more than one" (note 6).
- *The* is "by far the most interesting and difficult" (para. 8). Strictly used it involves uniqueness. "$x$ begat Charles II" has no uniqueness. To get "$x$ is the father of Charles II" add "if $y$ begat Charles II, $y$ is identical with $x$", always true of $y$ (para. 8). In symbols (added step: our rendering of his words), with $B(x)$ = "$x$ begat Charles II":

$$\text{“}x\text{ is the father of Charles II”}:\quad B(x)\wedge\forall y\,(B(y)\to y=x)$$

- "The father of Charles II was executed" becomes: "it is not always false of $x$ that $x$ begat Charles II, and $x$ was executed, and 'if $y$ begat Charles II, $y$ is identical with $x$' is always true of $y$" (para. 9):

$$\exists x\,[B(x)\wedge E(x)\wedge\forall y\,(B(y)\to y=x)]\quad\text{(added step: our rendering)}$$

- Russell admits this may seem "somewhat incredible"; he is here only stating the theory, not yet giving reasons (para. 10).
- For any statement $C$, $C(\text{the father of Charles II})$ implies "Charles II had one father and no more". So if this condition fails, every proposition of that form is false. Hence every proposition of the form $C(\text{the present King of France})$ is false. Russell calls this a great advantage and promises to show it does not violate the law of contradiction (para. 11).
- Result: all propositions with denoting phrases are reduced to forms with no such phrases (para. 12).

*Intuition note:* "The F is G" is not a statement about a special object called "the F". It says that exactly one thing is F and that thing is G. If there is no F, the statement is false instead of strange.

### C. Meinong and Frege (paras 13–16)
- **Meinong's view** (as Russell reports it): every grammatically correct denoting phrase stands for an object. Such objects do not "subsist", yet are objects. Russell's chief objection is that they are apt to infringe the law of contradiction: the present King of France exists and does not exist, the round square is round and not round. This is "intolerable" (para. 13).
- **Frege's view** (as reported): a denoting phrase has *meaning* and *denotation* (note 8 cites Frege's *Ueber Sinn und Bedeutung*). The center of mass phrase has a complex meaning and a simple denotation. Meaning explains why "Scott is the author of Waverley" is worth asserting: identity of denotation with difference of meaning (para. 14, note 9).
- **Objection (Russell) to Frege:** if "the King of France" has no denotation, then "the King of France is bald" ought to be nonsense. Yet it is plainly false (para. 15). Likewise "If $u$ is a unit class, the $u$ is a $u$" should always be true, but would seem to turn into nonsense when $u$ is not a unit class (para. 15).
- Such propositions do not become nonsense just because the hypothesis is false. The King in *The Tempest* could say "If Ferdinand is not drowned, Ferdinand is my only son", and it would stay true if he had drowned. So we must either supply a denotation or give up the view that denotation matters here. Russell chooses the latter (para. 16).
- Meinong supplies non-subsisting objects. Frege supplies conventional denotations, e.g. the null-class for "the King of France", or the class of all sons for "the only son of Mr. So-and-so". Russell says this "may not lead to actual logical error" but is artificial and not an exact analysis (para. 16).

### D. Three puzzles (para. 17)
Puzzles are like experiments: a theory of denoting should solve them.
1. **Substitution.** George IV wished to know whether Scott was the author of *Waverley*. Scott is that author. Substituting would give "George IV wished to know whether Scott was Scott", which can hardly be attributed to him.
2. **Excluded middle.** Either "the present King of France is bald" or "…is not bald" must be true. Yet he is on neither list of things. Russell jokes that Hegelians will probably conclude he wears a wig.
3. **Non-being.** If A differs from B, "the difference between A and B subsists". If not, it does not subsist, yet it seems to be the subject of a proposition. Hence, it would appear, denying being is always self-contradictory, while admitting being sometimes leads to contradictions (as with Meinong) (para. 17, note 11).

### E. The meaning/denotation view tangles (paras 18–25)
- Russell uses inverted commas to speak of a meaning. "The center of mass… is a point" speaks of the denotation. "'The center of mass…' is a denoting complex" speaks of the meaning. Similarly, the first line of Gray's *Elegy* states a proposition, but "'the first line of Gray's Elegy'" does not (para. 19).
- The meaning is said to denote the denotation, which is a logical relation, not merely linguistic. The difficulty: we cannot both keep this connection and keep the two apart, and the meaning can only be reached by denoting phrases (para. 20).
- "The meaning of $C$" gives the meaning of the denotation, not the one wanted. "The meaning of the first line of Gray's Elegy" equals "the meaning of 'The curfew tolls the knell of parting day'". To get the wanted meaning one must say "the meaning of '$C$'", which is just "$C$" (para. 21).
- "The denotation of $C$" fails similarly. With $C$ = "the denoting complex occurring in the second of the above instances", the denotation of $C$ is "The curfew tolls the knell of parting day", not the wanted "the first line of Gray's Elegy" (para. 21).
- So when we speak about a meaning, the subject must be something that denotes it. $C$ itself cannot occur inside that phrase, because then only its denotation occurs. There is "no backward road from denotations to meaning", since an object has infinitely many denoting phrases (para. 22–23).
- So "$C$" and $C$ would be different entities with "$C$" denoting $C$. But this relation is "wholly mysterious", and Russell asks where the denoting complex "$C$" is to be found. Also $C$ in a proposition is more than the denotation. Russell calls this "an inextricable tangle" and says it seems to prove the distinction was "wrongly conceived" (para. 24).
- Formal proof that meaning matters: "Scott was the author of *Waverley*" has a property "Scott was Scott" lacks, namely that George IV wished to know whether it was true. So meaning is relevant. But the view in question forces us to say only the denotation is relevant. So it must be abandoned (para. 25).

*Intuition note:* Russell says that if each phrase has both a meaning and a denotation, talking about the meaning slips back to the denotation. A phrase used normally is about its denotation, so you cannot get hold of its meaning without another phrase. This difficulty is, for him, a reason to drop the two-part view.

### F. How the theory solves the puzzles (paras 26–32)
- A denoting phrase is "essentially part of a sentence". "Scott was a man" has the form "$x$ was a man" with "Scott" as subject. "The author of *Waverley* was a man" does not have that form and has no such subject. It becomes "One and only one entity wrote *Waverley*, and that one was a man". Russell says this is easier to follow, not strictly what was said earlier (para. 27).
- **Denotation redefined.** "Scott was the author of *Waverley*" becomes "one and only one entity wrote *Waverley*, and Scott was identical with that one". If exactly one $x$ makes "$x$ is identical with $C$" true (so interpreted), $x$ is the denotation of "$C$". The phrase itself has no meaning, because the fully expressed proposition does not contain it (para. 28).
- **Puzzle 1.** The unabbreviated proposition has no constituent "the author of *Waverley*" to replace with "Scott". Substitution is safe when the phrase has a *primary occurrence* (para. 29).
- **Primary vs secondary occurrence.** In "George IV wished to know whether so-and-so", "so-and-so" is a proposition. A denoting phrase inside it can be eliminated either from the subordinate proposition or from the whole proposition, and different propositions result (para. 29). Illustration: the guest says "I thought your yacht was larger than it is". The owner replies "No, my yacht is not larger than it is". The guest meant "the size I thought it was is greater than its actual size" (para. 29).
  - Secondary: "George IV wished to know whether one and only one man wrote *Waverley* and Scott was that man". This is the normal reading.
  - Primary: "One and only one man wrote *Waverley*, and George IV wished to know whether Scott was that man". This is true if, for example, he saw Scott at a distance and asked "Is that Scott?".
  - A secondary occurrence is one where the phrase is in a proposition $p$ that is only a constituent of the whole, and the elimination happens in $p$. Symbolic logic avoids the ambiguity (para. 29).
- **Puzzle 2.** "$C$ has property $\varphi$" (abbreviated reading, note 12) means "one and only one term has the property $F$, and that one has $\varphi$". If $F$ belongs to no term or to several, this is false for every $\varphi$ (para. 30). Then "the present King of France is not bald" is false if it means "there is an entity which is now King of France and is not bald". It is true if it means "it is false that there is an entity which is now King of France and is bald". So it is false with a primary occurrence and true with a secondary one. All propositions with a primary occurrence are false; the denials of such propositions are true, but in them the phrase has a secondary occurrence. No wig is needed (para. 30).
- **Puzzle 3.** "The difference between A and B" has a denotation when A and B differ and none otherwise (para. 31). Generally, from "$a R b$" we can form a phrase that denotes an entity if the proposition is true and not if it is false. So "the revolution of the earth round the sun" denotes an entity (Russell: "at least we will suppose so"), while "the revolution of the sun round the earth" does not (para. 31, note 13).
- **Non-entities** (the round square, the even prime other than 2, Apollo, Hamlet) are denoting phrases that denote nothing. A proposition about Apollo is read by substituting a dictionary description such as "the sun-god". With primary occurrence it is false. With secondary occurrence it may be true (para. 32). "The round square is round" is false, not true as Meinong maintains (para. 32).
- **Ontological argument.** "The most perfect Being has all perfections; existence is a perfection; therefore it exists" becomes a proof that fails for want of a proof of "there is one and only one entity $x$ which is most perfect" (para. 32). Russell's note 14 adds further remarks on the class of most perfect Beings.

*Intuition note:* "The King of France is not bald" can mean two different things. The "not" can be applied to the whole claim "there is a bald King of France" (true), or to the part "is bald" after assuming there is a king (false). Once the two readings are separated, Russell escapes the conclusion that the King of France wears a wig.

### G. Further consequences (paras 33–37)
- **MacColl** treats individuals as real or unreal and defines the null-class as the class of all unreal individuals. Russell says this is essentially Meinong's theory and conflicts with the law of contradiction. On his own theory there are no unreal individuals, so the null-class has no members (para. 33).
- **Definitions.** "$m-n$ means the number which, added to $n$, gives $m$" should read: any proposition containing $m-n$ means the proposition got by substituting that phrase. Where exactly one such number exists it can be substituted. Otherwise propositions with a primary occurrence of "$m-n$" are false (para. 34).
- **Identity.** No one outside a logic book wants to say "$x$ is $x$". Identity is worth affirming in forms like "Scott was the author of *Waverley*". Russell says the shortest statement seems to be "Scott wrote *Waverley*; and it is always true of $y$ that if $y$ wrote *Waverley*, $y$ is identical with Scott" (para. 35). An editorial note (note 15, attributed to Moore via Marsh) says this is faulty because "wrote" is ambiguous.
- **Acquaintance.** Where we have only a denoting phrase, the proposition contains the constituents expressed by the phrase's words, not the thing. So "in every proposition that we can apprehend… all the constituents are really entities with which we have immediate acquaintance". Matter and other people's minds are known only by denoting phrases. We know "So-and-so has a mind which has such properties", not "$A$ has such properties" for the mind $A$ itself (para. 36).
- Russell asks readers not to reject the view for its complication until they have tried building their own theory. He believes that attempt will convince the reader that the true theory, whatever it is, cannot be as simple as one might have expected (para. 37).

## Toy example (ours, not from the text)
Domain: people $\{a,b,c\}$. Let $W(x)$ = "$x$ wrote the report" and $T(x)$ = "$x$ is tall". Take $T(a)$ true. The analysed form of "the writer of the report is tall" is
$\exists x\,[W(x)\wedge\forall y\,(W(y)\to y=x)\wedge T(x)]$.
- **Case 1: only $a$ wrote it.** Try $x=a$. $W(a)$ is true. For $y=a$, $a=a$ is true. For $y=b$ and $y=c$, $W(y)$ is false, so the implication is true. $T(a)$ is true. The sentence is **true**.
- **Case 2: $a$ and $b$ both wrote it.** For $x=a$, take $y=b$: $W(b)$ is true but $b=a$ is false, so the uniqueness part fails. The same happens for $x=b$. For $x=c$, $W(c)$ is false. The sentence is **false**.
- **Case 3: nobody wrote it.** No $x$ satisfies $W(x)$. The sentence is **false**.
- Now "not tall" in Case 3. Primary reading: $\exists x\,[W(x)\wedge\text{unique}\wedge\neg T(x)]$ is false, since no $x$ satisfies $W$. Secondary reading: $\neg\exists x\,[W(x)\wedge\text{unique}\wedge T(x)]$ is true, by Case 3. Both readings are consistent, which mirrors Russell's King of France.

## Concepts
- [[theory of descriptions]] — "the F is G" means exactly one thing is F and it is G; Russell's analysis of "the" (para. 8–11, 27)
- [[logical form vs. grammatical form]] — a phrase like "the author of Waverley" looks like a subject but disappears on analysis (para. 27)
- [[analysis]] — rewriting propositions containing denoting phrases into forms with none (para. 5, 12)
- [[sense (Sinn) vs. reference (Bedeutung)]] — Frege's meaning/denotation, in Russell's wording; Russell rejects it for denoting phrases (para. 14, 25)
- [[Frege's puzzle]] — the George IV puzzle: why "Scott is the author of Waverley" is informative and not like "Scott is Scott" (para. 14, 17)
- [[use vs. mention]] — Russell uses inverted commas to separate a phrase "C" from what C is about; he treats this as a way to speak of meanings (para. 19)
- [[denoting-phrase]] (new) — phrase denoting by form alone: *a man, all men, the King of France* (para. 1)
- [[acquaintance-vs-description]] (new) — direct presentation versus reaching a thing only by denoting phrases (para. 3, 36)
- [[primary-vs-secondary-occurrence]] (new) — whether the denoting phrase is eliminated from the whole proposition or from an embedded one (para. 29–30)
- [[propositional-function]] (new) — $C(x)$ with the variable undetermined; "always true" is primitive (para. 5, note 2)

## Canonical instances
- [[george-iv-waverley]] — substitution failure; solved by primary/secondary occurrence (para. 17, 29)
- [[king-of-france-bald]] — empty phrase; "not bald" false (primary) or true (secondary) (para. 11, 30)
- [[father-of-charles-ii]] — worked analysis of "the" (para. 8–9)
- [[gray-elegy-first-line]] — shows the meaning/denotation tangle (para. 19–21)
- [[yacht-size]] — shows scope ambiguity (para. 29)
- [[round-square-apollo]] — non-entities handled as empty phrases (para. 32)
- [[ontological-argument]] — fails for want of a uniqueness premise (para. 32)

## Bridges (candidates)
- [same-math] $C(\text{everything})$ as "always true", $C(\text{something})$ as "not always false" ↔ predicate logic: universal and existential quantifiers, with $\exists$ defined via $\forall$ and $\neg$ — same definability of one quantifier from the other.
- [structural-analogy] Primary vs secondary occurrence ↔ scope ambiguity of negation or modal and attitude operators in semantics — a phrase can be eliminated inside or outside the operator.
- [structural-analogy] Russell's "a theory is tested by puzzles, as by experiments" ↔ philosophy of science: puzzles as data for theory choice.
- [metaphor] Phrases with no meaning alone but meaningful in context ↔ syncategorematic terms in logic.

## Questions this raises
- Does Russell's rewrite capture what ordinary speakers say when "the King of France is bald" is uttered, or is "false" the wrong verdict?
- If proper names like "Scott" were also descriptions, would the acquaintance restriction (para. 36) shrink our thought even further?
- Is the primary/secondary distinction enough for all attitude contexts, or are there cases it does not cover?
- How serious is Moore's correction about "wrote" for the identity analysis (para. 35, note 15)?

## Reading notes
- Source is a Wikisource HTML transcription, "text from *Logic and Knowledge*", originally in *Mind*, 1905. No printed page numbers are visible, so citations use our own paragraph count (para. N), explained in L3.
- The source's word count is about 7,272 words. The pages to which it corresponds in *Mind* (479–493) come only from the unit metadata.
- The notes section contains stray markup (`<ref name=…>` fragments). All footnotes 1–15 are tagged [BR] in the source, though note 15 itself says it quotes Marsh's introduction and Moore's correction.
- Apparent typos in the source: "scott" in lowercase (para. 29), "thou are the man" (para. 35), "only and only one entity" (para. 31), "contain m-n" (para. 34), "Gegnstandstheorie" in note 7. 
- The unit's frontmatter pages are given as the metadata's printed range; the HTML has no page labels.
- Para. 5 and para. 7 give two forms of "C(a man)"; both appear in the source and are equivalent.
