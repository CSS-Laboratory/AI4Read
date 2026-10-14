# Independent audit: wave 2, argumentative prose (Kripke Lecture II, Kuhn ch. IX, Habermas ch. V, Grice 1975, Clark/Golder/Golder ch. 12 part 1)

Auditor: Claude Opus 5.5. I did not write or verify these digests. Date: 2026-10-14.
Pipeline audited: Sonnet 5.5 digest pass (prompt v2.2) plus independent verifier (v2.2). All five digests are `verified: repaired`.

**Method.** For Kripke, Kuhn, Habermas and Clark I read the whole extracted source (pdftotext, with page breaks marked) and checked digest claims one by one against the printed page. I also checked the Kripke p. 71 image (thesis numerals) and the Clark Map 12.1 / Figure 12.2 images. Grice has no text layer, so I read all 11 page images (two printed pages per sheet). Page mapping: Kripke excerpt page N = printed 70+N. Kuhn N = 91+N. Habermas N = 140+N (p. 141 has no printed number). Clark N = 456+N (pp. 463, 464 and 482 have no number). Grice sheet N has printed pages 2N+36 and 2N+37. The offsets the digests give in Reading notes refer to the parent PDFs, and I did not re-check them; the Grice offset formula is correct.

**Severity scale (from the brief).** *Critical:* wrong, reversed, strengthened or weakened claim; a claim not in the source (outside knowledge included); misattributed voice. *Major:* wrong page reference, missing key argument, dropped hedge, three or more undefined terms. *Minor:* wording or format. For hedges I separate two kinds. **Major:** losing a hedge changes a claim's modal status, scope or epistemic status (*it seems / not necessarily / to the extent that / a sense in which / if … indeed / increasingly / to speak approximately*). **Minor:** a degree word is swapped for a near-synonym in a side example (*scarcely* → *too*, *often* dropped).

---

## Summary

| Digest | Claims checked | Critical | Major | Minor | Words: digest / source / target | Verifier issues fixed |
|---|---|---|---|---|---|---|
| Kripke, Lecture II | 58 | 0 | 4 | 6 | 6,121 / 12,825 / 5,130 (1.19× target) | 20 |
| Kuhn, ch. IX | 52 | 0 | 5 | 7 | 4,322 / 6,718 / 2,687 (**1.61×**) | 15 |
| Habermas, ch. V | 85 | 1 | 2 | 12 | ~7,830 / 15,208 / 6,000 (1.30×) | 20 |
| Grice 1975 | 56 | 1 | 2 | 8 | 4,766 / 4,950 / 2,722 (**1.75×; 0.96× source**) | 21 |
| Clark et al. ch. 12 p1 | 62 | 1 | 1 | 9 | 5,473 / 9,916 / 5,454 (1.00×) | 13 |
| **Total** | **313** | **3** | **14** | **42** | | 89 |

**Estimated surviving error rate.** About 0.6 critical errors per digest. All three are low-impact: one sits in a Reading note and two are single L3 sentences. That is about 1 critical per 100 checked claims and about 18 errors of any severity per 100. In wave 1 it was 3 critical per 145 claims. The rate has not moved, but the location has. No critical error is left in L0–L2 (in wave 1, two of three were in L1). Instead, the summaries keep losing **hedges**. Eight of the 14 majors are dropped hedges (K-M1–3, U-M1–3, H-M1, G-M1). Five of these sit in L0–L2, where L3 or the source keeps the hedge. The verifier v2.2 lists hedge survival as a check, but its word list lacks scope and degree qualifiers (see P-1).

**Page references are excellent.** I checked about 200 references and found no wrong page. One range is incomplete (K-m2).

**Overall verdict: OK to continue the batch.** First, hand-fix the 3 critical lines and the 6 summary-hedge majors (list at the end). Second, apply verifier patch P-1 (scope/degree hedge words) and length gate P-3. Usefulness is good for Clark and Kripke, adequate for Kuhn and Habermas, and poor for Grice. The Grice digest is almost as long as the paper, and the paper itself is short and clear.

---

## 1. Kripke, *Naming and Necessity*, Lecture II (pp. 71–105)

File: `wiki/works/kripke-1980-naming/ch02-lecture.md`

### A. Faithfulness: 58 claims checked
(L0 2, L1 7, L2 9, L3 32, Concepts/Instances/Notes/Questions 8.) 48 correct, 0 critical, 4 major, 6 minor.

**Checked and correct:**
- The six theses and (C), against the p. 71 image.
- Kneale/Russell and the Isaiah/Greece points; Glunk (pp. 72–73).
- The converses of (5)/(6), "a sufficiently reflective speaker grasps this theory" (p. 73).
- Searle's quote; the Carlyle-style deterministic view; the Hitler "gut feeling" (pp. 74–75).
- Meter and yard (pp. 75–76); counterpart theory and Lewis (pp. 76–77); both rigidity clarifications (pp. 77–78).
- (6) crossed off; (5) survives "as far as the arguments … go"; (2)–(5) jointly true only in "a rare class of cases, usually initial baptisms" (p. 78).
- The mental-ceremony picture, Hesperus and Jack the Ripper (p. 79); n. 34 Donnellan/Phosphorus (p. 80).
- Feynman/Gell-Mann, Catiline pair, Einstein circle, encyclopedia joke (pp. 81–82).
- Gödel–Schmidt, Peano/Dedekind ("I have been told"), Einstein/bomb, Columbus (pp. 83–85).
- n. 36 attributive reply and the Smith/Jones answer; Thesis 4 random-atoms variant; Jonah; Thesis 5 (pp. 85–87); n. 37.
- The "commonly attributed" proposal: counterexample, then circularity (pp. 88–89).
- Strawson's passing the buck; the chain picture; Cicero–Jones (pp. 90–93).
- Santa Claus; "sort of too lazy"; Butler maxim; Newton and George Smith ("I am not sure"); the rough theory; the aardvark (pp. 93–97).
- n. 42 and n. 44; bifocals; the identity-thesis setting; Kripke's two theses on theoretical identities.
- Quine/Marcus, Everest/Gaurisanker, Russell (pp. 98–101).
- The Hesperus argument, the four-colour "epistemic might", qualitatively identical evidence, and the leftover contingent truth (pp. 102–105).
- The toy example: correct vote arithmetic and a good choice of main idea.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| K-M1 | L0 ("even though it is not known a priori"); L3 §10 "Kripke's diagnosis", bullet 1 ("So we do not know a priori that a name-identity is true") | Two qualifiers are dropped. Kripke says "**it seems** that we do **not necessarily** know a priori". The digest generalises to "every true name-identity is not known a priori". Only Hesperus/Phosphorus is said flatly to be not a priori (p. 104). | p. 101 | major |
| K-M2 | L1 ("Repairs … fail, mainly by circularity"); L3 §7 ("*Circularity, more significantly*") | Kripke says "second, and **perhaps** more significantly". The L1 word "mainly" also drops the first reply, the counterexample, as an equal ground. | p. 89 | major |
| K-M3 | L3 §3, n. 33 bullet ("Leverrier named the planet before anyone saw it") | The conditional "**If** Leverrier **indeed** gave the name … before it was ever seen" is turned into a historical fact. | p. 79 n. 33 | major |
| K-M4 | Whole digest (reader level) | Terms used without a definition: *idiolect* (Thesis 6), *analytic*, *ostension*, *nomological dangler*, *transworld identification*, *counterpart theory* (only half-glossed), *a posteriori* (Concepts only). | pp. 71, 72, 76, 79, 99 | major |
| K-m1 | Reading notes, "Text-layer problems" | Says the board list "has missing numerals; I assigned (1)–(4)…". The page **image** prints (1)–(6) and (C) clearly. Only the text layer drops them. This misreports the source, and "I assigned" is meta-commentary. | p. 71 image | minor |
| K-m2 | L3 §10 "Setting", bullet 3 | The "commonly held thesis" and the C-fibre identity thesis are on p. 98, but the bullet cites only (p. 99). | pp. 98–99 | minor |
| K-m3 | L3 §10 "Kripke's position", item 1 | The parenthesis merges two sentences ("does not prejudge whether physical necessity might turn out to be that, at least for this sort of example"). Kripke: physical necessity *might* be necessity in the highest degree, he does not prejudge it, and "at least for this sort of example, it might be that when something's physically necessary, it always is necessary tout court". | p. 99 | minor |
| K-m4 | Concepts | `[[rigid designator]]` correctly says "even where the thing does not exist", but does not flag that this **differs from the canon** ("in every possible world in which it exists"). `[[necessary a posteriori]]` and `[[epistemic … vs metaphysical possibility]]` use terms the lecture does not use, without "(canon link; not stated in this unit)". The ids contain spaces (same as wave-1 G2). | canon/analytic-philosophy.md l. 344; pp. 78, 103 | minor |
| K-m5 | Coverage | Omits n. 38 (Nozick: a description theory is trivially true if any non-circular theory of reference exists, but it would then be "of a completely different sort") and n. 43 (the aardvark has a causal chain to Napoleon, "but not one of the required type"). n. 43 is the cleanest statement of why mere causation is not enough. | pp. 88 n. 38, 96 n. 43 | minor |
| K-m6 | Questions, Q3 | "Kripke only says the analogy 'has to go'". He also says "it's hard to see … how to avoid concluding that the two are actually different", which L3 itself reports. | p. 100 | minor |

### B. Toy example
Correct and well chosen. Zorb/Mia reproduces the cluster vote (2 of 3 for Mia) against the chain from the baptism, and adds a rigidity check. It is the most useful toy in this wave for an argumentative text.

### C. Coverage
Complete for the main text. Only footnotes are missing (K-m5).

### D. Usefulness
Good. L0–L2 give a reliable entry, and L3 follows the lecture's own order with clear voice tags (Searle, Strawson, Quine, Marcus, the cluster theorist). For a B2 reader starting from high school it is heavy: `level: grad` is honest, but K-M4 needs a 6-line glossary. The length (0.48× source) is right for a 35-page lecture.

---

## 2. Kuhn, *Structure*, ch. IX "The Nature and Necessity of Scientific Revolutions" (pp. 92–110)

File: `wiki/works/kuhn-1962-structure/ch09-nature.md`

### A. Faithfulness: 52 claims checked
(L0 3, L1 7, L2 9, L3 27, Concepts/Questions 6.) 40 correct, 0 critical, 5 major, 7 minor.

**Checked and correct:**
- Definition of revolution (p. 92); both aspects of the political parallel; X-rays (pp. 92–93).
- Circularity is "only that of persuasion"; the "assent of the relevant community" quote (p. 94).
- Life on the moon; quantum theory "not exclusively"; energy conservation (p. 95).
- "Almost non-existent exception" (p. 96).
- The three types of phenomena, "this type alone" (p. 97).
- Caloric-theory crisis; "permissible view … historical implausibility" (p. 98).
- The positivist objection, voiced correctly (p. 99); phlogiston (pp. 99–100).
- "Logically unexceptionable" (p. 100); the rhetorical question kept as a question (p. 101).
- E/N derivation and "spurious, at least to this point" (p. 101); mass conserved vs convertible (p. 102).
- The incommensurable tradition (p. 103); Molière, collisions, gravity as reversion not retrogression, the Leyden jar (pp. 104–106).
- Chemistry principles, Maxwell's ether "lip service, which it emphatically had not been" (p. 107); reversals (pp. 108–109).
- Map and map-making (p. 109); "which problems is it more significant to have solved" (p. 110).
- Toy arithmetic.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| U-M1 | L1 ("so rival camps talk past each other"); L2 bullet 8 ("rival camps talk through each other") | Drops Kuhn's scope qualifier: "**To the extent, as significant as it is incomplete,** that two scientific schools disagree about what is a problem and what a solution, they will inevitably talk through each other". The L3 intuition note keeps it. | p. 109 | major |
| U-M2 | L0 ("are historically the rule for new theories and almost all new kinds of phenomena") | Drops the condition "**After the pre-paradigm period**". L3 keeps it. | p. 96 | major |
| U-M3 | L3 last bullet ("paradigms are constitutive of nature as well as of science"); Questions Q3 | Kuhn: "Now I wish to display **a sense in which** they are constitutive of nature as well." | p. 110 | major |
| U-M4 | L1 ("He rejects the positivist claim that Newton's laws are a special case of Einstein's"); L2 bullet 5 | Kuhn's own concession is lost: "an out-of-date theory **can always be viewed** as a special case of its up-to-date successor, [but] it must be transformed for the purpose". What he rejects is that the derived N_i *are Newton's laws*, i.e. a derivation "in any sense of 'derive' now generally recognized". L3 has this right. | pp. 101–103 | major |
| U-M5 | Whole digest (reader level) | Undefined terms: *logical positivism*, *phlogiston*, *caloric theory*, *ether*, *incommensurable* (never defined, only quoted), *charging by induction*, *Leyden jar*, *electric displacement*. | pp. 98–109 | major |
| U-m1 | L0, last clause of first half ("it is hard to see how new theories could arise without them") | True to p. 98, but the sentence is absent from L3 (rule 4: summaries only from L3). | p. 98 | minor |
| U-m2 | L2 bullet 3 ("Paradigm choice is circular") | Kuhn says the *role of paradigms in the debate* is circular, not the choice itself. | p. 94 | minor |
| U-m3 | L3 positivist objection, bullet 1 ("engineers and some physicists") | Source: "**most** engineers and, in selected applications, … **many** physicists". This is a weakening in the objector's voice, with no argumentative weight. | p. 99 | minor |
| U-m4 | L3 "logical lacuna", bullet 6 | Says the argument "justifies … the teaching of earth-centered astronomy to surveyors". Source: "An argument **of the same type** is used to justify" it. | p. 102 | minor |
| U-m5 | L3 Newton example, last bullet ("Without it, Lavoisier's and Dalton's later work would be incomprehensible") | The antecedent is changed. Source: without "the data and the chemical concepts developed in that process". | p. 106 | minor |
| U-m6 | Questions, Q1 | Quotes "persuasion only", which is not verbatim, and applies it to paradigm choice. Source: "the status of the circular argument is only that of persuasion". | p. 94 | minor |
| U-m7 | Coverage | Missing: the chapter's own pivot "Let us … now take it for granted that the differences between successive paradigms are both necessary and irreconcilable" (p. 103), the conclusion of the "necessity" half; "most of the apparent differences between a discarded … theory and its successor are real" (p. 102); "Perhaps it is another sort of enterprise" (p. 96). | pp. 96, 102, 103 | minor |

### B. Toy example
Arithmetic correct (5 vs 5 tie). It illustrates the partially circular debate of pp. 109–110, which ties to the main claim that paradigm choice is not settled by normal-science criteria. Good.

### C. Coverage
All sections of the argument are present. The key concluding sentences are listed in U-m7.

### D. Usefulness
Faithful and clear, and the voice handling of the positivist objection is exemplary. But it is **1.61× the target and 0.64× the source**, so L3 is close to a paraphrase of the chapter. For an HS-level reader, the history-of-science vocabulary (U-M5) is the real barrier, more than the argument. A 5-term glossary would help more than the extra L3 detail.

---

## 3. Habermas, *Structural Transformation*, ch. V (§§16–19, pp. 141–180)

File: `wiki/works/habermas-1989-publicsphere/ch05-social.md`

### A. Faithfulness: 85 claims checked
(L0 1, L1 7, L2 9, L3 60, Concepts/Instances/Questions/Notes 8.) 70 correct, 1 critical, 2 major, 12 minor.

**Checked and correct:**
- §16: separation of state and society and the High Middle Ages; neomercantilism without interlocking; "refeudalization"; the societalization/state-ification dialectic; the Chapter V/VI relation (pp. 141–143).
- 1873, protectionism, Aktiengesellschaft/trust; Germany unable to catch up; Say's Law; horizontal vs vertical relations; Neumann (pp. 143–144).
- 1867/1883 reforms; Bismarck; Strachey; budget plus qualitative analysis; formative functions; econometric modelling; the "democratic influence" with its mid-century caveat (pp. 145–148).
- Renner; "publification"; super-ownership; the liberal jurists' complaint, correctly voiced; wage agreements as surrogate law, correctly flagged as a quotation; do ut des; the township contracting under private law (pp. 148–151).
- §17: deprivatization vs privatization; Rathenau, Burnham and Drucker "hit the mark"; family property to incomes; prevention as intrusion; pseudo-privacy; Whyte; Bahrdt (pp. 151–159).
- §18: not mere ideology, "political" in the Greek sense; culture industry; Gartenlaube; "the conversation itself is administered"; paperbacks vs book clubs (Kayser); West German reading figures; Cobbett, penny press, Pulitzer; delayed vs immediate reward news; "Don't talk back"; status gradient of consumption, with "if a generalization be permitted" kept; Hauser; specialists vs consumers (pp. 159–175).
- §19: culture of integration; acclamation; Marx vs Habermas, correctly voiced; "Critical publicity is supplanted by manipulative publicity"; universality and truth of law; Forsthoff's three processes; the double concept of law; Kant (pp. 175–180).
- Every page reference I checked is correct.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| H-C1 | L3 §16, "Mass suffrage", last bullet ("He also cites Galbraith's analysis of countervailing powers as explaining this mechanism") | What explains what is reversed. Source: "This mechanism, which Galbraith analyzed also from the perspective of countervailing powers, **explained the connection between tendencies toward a concentration of capital and a growing state interventionism**." Galbraith *analysed* the mechanism, and the mechanism explains the concentration–interventionism link. The digest drops that claim. | p. 146 | **critical** (low impact) |
| H-M1 | L3 §17, "The family as consumer unit", bullet 6 ("The family lost upbringing, education … Even the family was deprivatized") | Two hedges are lost: "the family **increasingly** lost also the functions …" and "**in a certain fashion** even the family … was deprivatized". The same pattern appears at p. 156 ("tendency toward the leveling" becomes "Paternal authority was levelled") and p. 157 ("**has started to** dissolve into a sphere of pseudo-privacy" becomes a finished state). | pp. 155–157 | major |
| H-M2 | Whole digest (reader level) | Undefined terms: *mercantilist/neomercantilist*, *oligopolistic*, *Aktiengesellschaft*, *petty commodity exchange*, *do ut des*, *conjugal family*, *intimate sphere*, *internalization*, *acclamation*, *mediatized public*, *plebiscitary* (L2/L3; defined only in Concepts). | passim | major |
| H-m1 | L1, last sentence | "the social-structural half of the explanation" is the digest's framing. Habermas: the downfall "demonstrated by its changing political functions (Chapter VI) **had its source** in the structural transformation … (Chapter V)". | pp. 142–143 | minor |
| H-m2 | L2 bullet 8 ("the parliamentary public takes on a plebiscitary character") | This is a block quote from an unnamed author ("As has often been described in detail in the literature …"), stated in L2 as Habermas's claim. Habermas endorses it, and L3 attributes it correctly. | p. 180 | minor |
| H-m3 | §16 intuition note ("it lost its place, not merely some of its power") | The contrast with "power" is the digest's own addition. | pp. 142–143 | minor |
| H-m4 | L3 "Economic background", bullet 4 | "the liberal era was a mere episode, a 'vast secular boom'" drops "From the perspective of the overall development of capitalism the period … **appeared to be** no more than". | p. 144 | minor |
| H-m5 | L3 "Economic background", bullet 7 | A comparative is flattened. Source: "**The more** society became transparent as a mere nexus of coercive constraints, **the more** urgent became the need for a strong state." | p. 144 | minor |
| H-m6 | L3 "Mass suffrage", bullet 5 | "Examples: Bismarck's Socialist Law, and his Social Security Insurance" lists both as examples of the entrepreneurs' answer. Source: the Socialist Law was "a prime example", **but** the Insurance showed intervention "had to yield to pressure from below". The relative clause partly repairs this. | p. 146 | minor |
| H-m7 | Concepts, `[[societalization-and-state-ification]]` | Defined as "the state adopting social interests and society taking on public functions". In the source the pair is the transfer of public functions to private bodies vs the extension of public authority over the private realm. "Adopting social interests" belongs to a different sentence. L2 bullet 2 is better. | p. 142 | minor |
| H-m8 | L3 §18 bullet 7 ("This was not to be expected"); Questions Q2 | Drops "**Under the given circumstances**". Q2 then uses the phrase as a general verdict on whether a public sphere can be rebuilt. | p. 161 | minor |
| H-m9 | L3 "Who consumes?", bullet 4 | "the first consumer strata were … upwardly mobile groups" drops "**often**". The outer hedge "if a generalization be permitted" survives. | pp. 173–174 | minor |
| H-m10 | L3 §19 "Culture of integration", bullet 5 | "There is an interest in influencing them" drops the condition "**To the extent that** social reproduction still depends on consumption decisions and … voting decisions". | p. 176 | minor |
| H-m11 | L3 §19 "Culture of integration", bullet 1 ("could serve as a super-slogan") | Weakened. The culture "is flexible enough … to serve itself as a kind of super slogan that, if it did not already exist, could have been invented" for PR. | p. 175 | minor |
| H-m12 | L3 §19 "The law", bullets 4 and last | "laws take on the character of administrative dispositions" drops "**often already**". "too remote for rational justification to be demanded or achieved" replaces "can **scarcely** be demanded, let alone be accomplished". | pp. 179, 180 | minor |

### B. Toy example
The arithmetic is correct (R-share 0.60 vs 0.10). But it illustrates a single phrase on p. 171, "exchanges about tastes and preferences", not the chapter's main idea, which is the fusion of state and society and the resulting loss of the private basis of the public sphere. It also invents a coding scheme, which a reader may take for Habermas's method. The disclaimer is there, but a toy that traces one institution across the private/public line would be closer to the main idea. One example is a firm that moves from private property to a semipublic institution providing housing and care (p. 154).

### C. Coverage
Very complete. Even §17's architecture passage and §19's Forsthoff list are present. Small omissions: the young industrial nations surpassing France and Britain in antitrust law (p. 143); the "absolutely constitutive" relation of the literary to the political public sphere (p. 177).

### D. Usefulness
Adequate. L0–L2 are a trustworthy map of a very hard chapter, and the voice handling is good: socialist critique, liberal jurists, Schelsky, Bahrdt, Marx vs Habermas and unnamed quoted authors are all tagged. But L3 is 60 bullets of compressed paraphrase in Habermas's own vocabulary (H-M2). An HS-level B2 reader will not be able to use L3 without a glossary. The five intuition notes are the most useful part for that reader.

---

## 4. Grice 1975, "Logic and Conversation" (pp. 41–58; scanned)

File: `wiki/works/grice-1975-conversation/main.md`

### A. Faithfulness: 56 claims checked
(L0 2, L1 7, L2 10, L3 30, Concepts/Instances/Notes 7.) 45 correct, 1 critical, 2 major, 8 minor.

**Checked against the images and correct:**
- The formal-device list, "somewhat rashly made", the formalist outline, "I do not wish to suggest that all formalists would accept the whole" (pp. 41–42).
- The informalist reply as "might reply", correctly voiced; "(broadly speaking) a common mistake" (pp. 42–43).
- The prison example; terms of art; *say* and the vice example; Harold Wilson; *therefore* as conventional implicature (pp. 43–45).
- The CP wording; "one may **perhaps** distinguish four categories"; Kant (p. 45).
- All maxim texts; Relation's problems; the Manner list; the urgency and Quality-first remark (pp. 46–47); the four analogues (p. 47).
- The "dull" answer; rationalist; the three quasi-contract features and their failure; the alternative aim and uncertainty (pp. 48–49).
- The four ways of failing; exploitation (p. 49); the definition and the general pattern; the five data (pp. 49–50).
- Groups A/B/C with all examples and Grice's odd numbering (1a), (3b), (2a), (2b), (3), (4) (pp. 51–56).
- Particularized vs generalized; *an X*; "may be incorrect in detail" (pp. 56–57); features 1, 2, 4, 5 (pp. 57–58).
- The Reading-notes offset formula; the Searle page excluded.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| G-C1 | L3 "The Cooperative Principle and the maxims", Quantity bullet ("…but it might be answered that it may confuse or mislead about the speaker's point, and a later maxim, Relation, may secure its effect") | The argumentative role is reversed. In Grice, the Relation point is a **further reason for doubting** the second Quantity maxim: "However this may be, there is **perhaps** a different reason for doubt about the admission of this second maxim, namely, that its effect will be secured by a later maxim". The digest places it inside the reply that *defends* the maxim, and drops "perhaps". | p. 46 | **critical** (low impact) |
| G-M1 | L3 "Features", item 3; L2 last bullet | Drops "**To speak approximately**". "Though it **may not be impossible** for what starts life … as a conversational implicature to become conventionalized" becomes "It may become conventionalized", which is stronger. | p. 58 | major |
| G-M2 | Whole digest (reader level) | Undefined: *ceteris paribus*, *perspicuous* (in a maxim the reader must learn), *meiosis*, *categorial falsity*, *supermaxim*, *tautology*, *explication*. | pp. 45–53 | major |
| G-m1 | L3 "Conventional implicature" ("the utterance would not be strictly speaking false if it failed to follow") | Grice: "I do **not want to say** that my utterance … would be, STRICTLY SPEAKING, false". Declining to assert falsity becomes asserting non-falsity. | p. 45 | minor |
| G-m2 | L1, sentence 5 | Implicature is introduced only through blatant failure ("A speaker who blatantly fails to follow a maxim … can convey more"). The definition requires only presumed observance (pp. 49–50), and Group A has no violation (p. 51). Not false ("can"), but it narrows the concept in the summary. | pp. 49–51 | minor |
| G-m3 | L3 definition, clause (2) | Drops "(or doing so **in THOSE terms**)". This qualifier is what later grounds the Manner exception to nondetachability. | p. 50 | minor |
| G-m4 | L3 prison reworked; Group A | Omits "and so may be regarded as having flouted one of the maxims conjoining perspicuity" (p. 50). Also omits the Group A remark that, unlike the prison case, Manner is not infringed in (1) (p. 51). | pp. 50–51 | minor |
| G-m5 | L3 Group C, (3b) heading | Drops the conditional title "on the assumption that the existence of such a maxim should be admitted". Together with G-C1, the reader loses Grice's doubt about this maxim. | p. 52 | minor |
| G-m6 | L3 "Grice's account" ("Information, like money, is given without the giver knowing its use") | Drops "is **often** given". | p. 57 | minor |
| G-m7 | L3 "Analogues outside talk" | Lists four analogues without saying which category each illustrates (Quantity, Quality, Relation, Manner), and without Grice's framing: "one of my avowed aims is to see talking as a special case … of purposive, indeed rational, behavior". Also omits "the talker who is irrelevant or obscure has primarily let down not his audience but himself" (pp. 48–49). | pp. 47–49 | minor |
| G-m8 | Concepts; Reading notes | Ids use display names with spaces and capitals (`[[Smith in New York]]`, `[[Miss X sang]]`). The ιx reading of "ʃx" is outside inference, though flagged as such. | p. 41 | minor |

### B. Toy example
Correct and on the main idea. The popcorn reply runs through the p. 50 pattern. The cancellation test is honestly marked as an extension, because Grice states cancellability for *generalized* implicatures and the popcorn case is particularized.

### C. Coverage
Complete. Every example is present with its page.

### D. Usefulness
Faithful, but **not useful as a guide at this length**. At 4,766 words the digest is 0.96× the paper (4,950 words) and 1.75× the target. It exceeds even the 0.8×source cap in `target_words()`. L3 is a section-by-section paraphrase of an 11-page paper that is itself written in clear, example-led prose. The reader would do better with L0–L2, the toy, a 10-term glossary (G-M2) and the original. If L3 is kept, it should be cut to about 2,500 words: drop the restatement of each example's gloss and keep the maxim list, the definition, the five data and the five features.

---

## 5. Clark, Golder & Golder, *Principles of Comparative Politics*, ch. 12, part 1 (pp. 457–482)

File: `wiki/works/clark-2017-principles/ch12-parliamentary-p1.md`

### A. Faithfulness: 62 claims checked
(L0 2, L1 7, L2 9, L3 36, numbers/toy 6, Notes 2.) 51 correct, 1 critical, 1 major, 9 minor.

**Checked and correct:**
- Epigraphs and the five overview points (pp. 457–458); Figure 12.1; no-confidence, n. 3 Art. 81, constructive vote, Weimar, vote of confidence and its uses (pp. 459–460).
- "Not defined by the presence of a president" (pp. 460–461); popular election (i)/(ii); Germany; fixed term; n. 5; "neither necessary nor sufficient"; monarchs; n. 6 Kiribati (p. 461).
- The three definitions (p. 462); every 2008 and 1946 number (p. 462).
- PM titles; board of directors; ministerial and collective responsibility; Robin Cook (pp. 465–467).
- Table 12.3; Box 12.1 including Andreotti 258/630/44 (pp. 467–468); 40/47 = 85% and 219/266 = 82% (p. 469).
- All six Table 12.4 rows quoted, with the 249 threshold correctly marked "added step" (p. 470).
- Greece/Bulgaria; Czech 2006 (100–100, then 100–98); informateur "at least theoretically"; Bäck & Dumont; n. 9 Sonia Gandhi (pp. 472–473).
- Thatcher quote; Indriðason & Kam; caretaker and n. 10 (pp. 473–474).
- Seven options; the three MWCs; least MWC = Greens (16) (pp. 475–476).
- Box 12.2 80/120 example; "some evidence"; both answers and Buttard & Golder (pp. 477–478).
- Figure 12.5 order; five connected coalitions; FDP prediction; "four extra surplus seats"; "slightly more sense" (pp. 479–480).
- Table 12.6/Figure 12.6 percentages and the UK/Denmark/Italy rows (pp. 481–482); support parties, Liberals 1977 (p. 481).
- Reading-note checks: the Figure 12.2b peak is indeed about 70% (image), so the text's 74% conflict is real. The "Porportion" misprint and the stray quotation mark are real. The Czech/Italy tension is a fair observation.

### Surviving errors

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| C-C1 | Reading notes, first bullet ("The sentence about the **2010 UK** situation is cut off") | A claim not in the source. The page reads only "This also occurred more recently after the 2010 legislative" and names no country. L3 correctly says "a further example from after the 2010 legislative elections". | p. 481 | **critical** (low impact; outside knowledge in Reading notes) |
| C-M1 | Whole digest (reader level) | Undefined: *ideal point* (central to the policy-seeking model; used in L3 and the toy), *proportional representation*, *single-member district plurality*, *mixed* democracies (fn. 1 says it means semi-presidential; omitted, but the word is used for the 1946 figure), *impeachment*. | pp. 458 n. 1, 462, 469, 478 | major |
| C-m1 | L3 "Choosing ministers"; Canonical instances (`thatcher-1979-cabinet`: "a PM forced to include internal opponents") | Source: Thatcher "**felt compelled** to appoint" such a cabinet. | p. 473 | minor |
| C-m2 | L3 "Trade-off", bullet 1 ("very hard, if not impossible") | Adds "very". Source: "hard, if not impossible, to answer empirically". | p. 479 | minor |
| C-m3 | L3 "Minority government" definition | Drops "do not **explicitly** command a majority". The word matters, since the next bullet argues they implicitly do. | p. 480 | minor |
| C-m4 | L3 Czech case | Drops the authors' evaluation "In somewhat dubious circumstances" and "surprisingly decided to abstain". The intuition note's "it can matter" is weaker than "starkly partisan". | p. 472 | minor |
| C-m5 | L3 Figure 12.3 description | Omits the "freestyle bargaining between elites" branch (when the head of state is not active). That is the default path in the text's own account. | p. 471 | minor |
| C-m6 | Coverage | Omits the authors' highlighted trend: "A striking feature of Figure 12.2 is the rapid increase … of semi-presidential democracies"; and "the parliamentary form … is the most common". | p. 462 | minor |
| C-m7 | Reading notes, "Edition" | "copyright 2013" is not visible on these pages. It comes from pipeline metadata ("the source note"). Rule 14 limits Reading notes to what the pages show. The "2e" proof stamp is visible and enough. | p. 463 | minor |
| C-m8 | Toy example, step 1 | Enumeration is incomplete: A+B+D (80 seats, not minimal) and A+B+C+D are not listed. The conclusions are unaffected. | — | minor |
| C-m9 | Format | Page ranges written "(p. 458–459, 462)", "(p. 476–480)" instead of "pp.". This happens throughout L2 and in several L3 and Concepts lines. | — | minor |

### B. Toy example
Excellent and fully checkable. It reproduces the office-seeking vs policy-seeking logic with new numbers, adds Gamson's-law portfolio counts (14/7 vs 12/9), and ends with the same kind of trade-off the CDU/CSU faced. Fix the incomplete enumeration (C-m8).

### C. Coverage
Complete for the pages. The digest is honest that points 3–5 of the overview and the rest of the minority-government discussion lie outside this part.

### D. Usefulness
The best digest in this wave for the target reader. The textbook source suits the format. Numbers are exact, terms are mostly defined inline, and the L1 Prerequisites line defines no-confidence, formateur and investiture up front. The length matches the target exactly. Only C-M1 (ideal point) blocks an HS-level reader.

---

## Error patterns across the five digests

1. **Hedges lost in summaries (still).** These cases are all *scope or degree* qualifiers, not the modal verbs on the v2.2 hedge list (K-M3's *if … indeed* is a conditional, also missing from the list): K-M1 (*it seems / not necessarily*), K-M2 (*perhaps*), U-M1 (*to the extent … that*), U-M2 (*after the pre-paradigm period*), U-M3 (*a sense in which*), H-M1 (*increasingly / in a certain fashion / has started to*), G-M1 (*to speak approximately / may not be impossible*). The verifier's hedge-survival list (verify.md, H5) has none of these words. In four cases (K-M2, U-M1, U-M2, U-M4) L3 is right and only L0–L2 drift. The "every sentence of L0–L2" pass exists, but it compares against L3 loosely.
2. **Argumentative role and direction.** Both L3 criticals are not about strength. In each, the role of a clause in the argument is wrong: G-C1 has a reason for doubt placed inside the defence, and H-C1 has explanans and explanandum swapped. Neither is triggered by a strong word, so neither appears among the verifier's mandatory L3 items.
3. **Reading notes still carry unsupported claims.** K-m1 says numerals are missing that the image shows. C-C1 names a country the page does not name. C-m7 is a metadata fact. All Reading-notes sentences are mandatory verifier items, and these survived anyway.
4. **Readability is the weakest dimension.** All five digests leave three or more terms undefined, so every digest has the major (K-M4, U-M5, H-M2, G-M2, C-M1). The verifier's G rule checks only L0–L2, and most undefined terms sit in L3.
5. **Length is not enforced after generation.** Kuhn is 1.61× and Grice 1.75× the target (0.96× its source). Neither was repaired.
6. **Strengths.** No wrong page references. No invented facts in L2/L3. Voice tags are excellent in all four philosophy texts (Searle, Strawson, Quine/Marcus, the positivist objector, the informalist, Marx vs Habermas, liberal jurists, quoted authors). All numbers in Clark are exact.

## Prompt and pipeline improvements

**P-1 (verifier H5 + digest rule 2): add scope and degree qualifiers to the hedge list.** Append to both lists: *it seems, not necessarily, necessarily, to the extent that, insofar as, in a sense / a sense in which, in a certain fashion, to speak approximately, roughly, increasingly, tendency / tends, has started to, if … indeed, after/before <period>, under the given circumstances, may not be impossible, scarcely, often, most/many/some*. For each L0–L2 sentence, the verifier must quote the **source sentence**, not just the L3 line, and list its qualifiers. This would have caught all eight hedge majors (K-M1–3, U-M1–3, H-M1, G-M1).

**P-2 (verifier, mandatory L3 items): argumentative-role check.** Add as mandatory items the L3 sentences containing *but, however, answer/reply, objection, reason for doubt, explains/explained, because, so, therefore*. For each, the verifier states which side of the argument the clause is on in the source (claim / objection / reply / reason for doubt) and what explains what. This catches G-C1 and H-C1.

**P-3 (deterministic gate): length.** After verification, if `words > 1.3 × target_words`, send the digest back for a compression pass ("cut L3 restatements of examples; keep definitions, the author's examples by name, and key steps"). Hard-fail above `0.8 × source_words` (Grice).

**P-4 (verifier G): undefined terms in L3 too, and a glossary fallback.** Extend G to L3. When there are three or more undefined terms, the repair should add a `**Glossary:**` line under Prerequisites (≤15 words per term) rather than inline edits. That is cheaper and more useful for an HS-level reader.

**P-5 (checks.py): concept-id slug check.** Flag `[[...]]` ids containing spaces, capitals or parentheses. This is the wave-1 G2 issue, still present in Kripke, Kuhn and Grice.

## Hand fixes needed now (before posts reuse these)

- **G-C1 (Grice p. 46):** "Grice calls the second maxim disputable. It might be said that overinformativeness is merely a waste of time. It might be answered that it may confuse or mislead hearers about the speaker's point. There is perhaps a different reason for doubting this maxim: its effect will be secured by a later maxim, Relation (p. 46)."
- **H-C1 (Habermas p. 146):** "This mechanism, which Galbraith also analysed in terms of countervailing powers, explained the link between capital concentration and growing state interventionism (p. 146)."
- **C-C1 (Clark Reading notes):** replace "the 2010 UK situation" with "the 2010 example".
- **K-M1:** L0 "…even though it **need not be** known a priori"; L3 "So it seems we do not necessarily know a priori that a name-identity is true (p. 101)."
- **K-M2:** L1 "Repairs … meet counterexamples and, perhaps more significantly, circularity"; L3 "*Circularity, perhaps more significantly.*"
- **U-M1:** L1/L2 "to the extent that rival camps disagree on what counts as a problem and a solution, they talk through each other".
- **U-M2:** L0 "…are historically the rule, after the pre-paradigm period, for…".
- **U-M3:** "Kuhn announces that he will show a sense in which paradigms are constitutive of nature as well (p. 110)."
- **U-M4:** L1 "He rejects the positivist claim that Newton's laws can be derived from Einstein's: the derived laws are a special case only after their key terms change meaning."
- **G-M1:** feature 3: "To speak approximately, … It may not be impossible for an implicature to become conventionalized, but …"
