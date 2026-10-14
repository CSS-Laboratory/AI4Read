# Wave-2 regression audit: v2.2 re-digests of Cover ch. 2, Wittgenstein PI §§243–315, Jaynes ch. 2, Dennett ch. 2

Auditor: Claude Opus 5.5 (independent; wrote none of these files). Date: 2026-10-14.
Pipeline audited: Claude Sonnet 5.5, digest prompt v2.2 + verifier v2.2 (all four `verified: repaired`).
Ground truth: page images of `/home/claude/audit/{cover-ch02,wittgenstein-ch04,jaynes-ch02,dennett-ch02}.pdf`, all pages read as images (38 + 16 + 27 + 15 spreads).
Earlier reports: `akerlof-cover.md` (C*), `philosophy-prose.md` (D*, W*), `math.md` (J*).
Severity rubric (same as earlier audits): **critical** = wrong statement / wrong equation / claim not in source; **major** = wrong page ref, missing key content, misattributed voice, dropped hedge or condition that changes the claim, L0–L2 stronger than L3; **minor** = wording, format, small imprecision.
Arithmetic re-checked by hand and in Python: Cover toy (1.81128 / 0.18872 three ways), Jaynes added steps for (2.17), (2.46), (2.57), (2.58) and the toy (both scales), Dennett blinker counts.

---

## Summary

| Digest | Known crit/major errors | Fixed | Partly | Still present | New checks | Correct | Minor | Major | Critical |
|---|---|---|---|---|---|---|---|---|---|
| Cover ch. 2 | 3 (C1, C2, C3) | 3 | 0 | 0 | 35 | 31 | 3 | 1 | 0 |
| Wittgenstein §§243–312 | 7 (W1–W7) | 6 | 0 | 1 (W2) | 42 | 35 | 6 | 1 | 0 |
| Jaynes ch. 2 | 3 (J1–J3) | 3 | 0 | 0 | 34 | 30 | 3 | 1 | 0 |
| Dennett ch. 2 | 2 (D1, D2) | 2 | 0 | 0 | 39 | 36 | 2 | 1 | 0 |
| **Total** | **15** (4 critical, 11 major) | **14** | 0 | **1** | **150** | **132** | **14** | **4** | **0** |

All 4 known critical errors are gone. 14 of 15 known critical/major errors are fixed. The one that survives is W2 (§263 voice), and it is now arguably worse. Of 25 known minors, 19 are fixed, 3 are partly fixed and 3 are still present (§A tables).

The four new majors follow the earlier pattern: **voice** (Wittgenstein §312, Dennett's Mrs Gardner contest) and **logical strength in L2** (Cover "equivalently", Jaynes "hold only for"). Equations, numbers and page references were error-free in all four digests. I found no wrong equation and no wrong page reference in about 60 equation checks and about 70 page-reference checks.

---

## A. Known errors: status

### A1. Cover & Thomas ch. 2 (`wiki/works/cover-2006-elements/ch02-entropy.pipeline.md`)

| ID | Old severity | Status | Evidence in v2.2 digest |
|---|---|---|---|
| C1 | critical | **fixed** | L2: "entropy itself need not increase unless the stationary distribution is uniform" (sufficient condition kept; p. 35). L3 item 3 says "Entropy increases **if**…". The Concepts line says "rises **if**". |
| C2 | critical | **fixed** | The claim about missing 2nd-edition chapters is gone. Reading notes now say only "may differ". A small residual remains: "first edition" is an inference, not printed (counted as new minor N-C3). |
| C3 | major | **fixed** | §2.9 intuition note: "guaranteed to rise if … uniform, but with a non-uniform stationary state it can fall". |
| C4 | minor | fixed | The bridge with "only for uniform" was removed. |
| C5 | minor | **still present** | Lemma 2.1.1 still reads "$0<p(x)\le1$". The image (p. 14) shows $0\le p(x)\le1$. |
| C6 | minor | fixed | "up to at most one question … between $H$ and $H+1$". |
| C7 | minor | fixed | `[[self-information-surprisal]]` now states Cover's usage ($I(X;X)=H(X)$, p. 20). |
| C8 | minor | fixed | Ex. 15 with its added hint was dropped. |
| C9 | minor | fixed | That question was removed. |
| C10 | minor | partly | A Prerequisites line was added. L0–L2 still use undefined terms: "Markov chain", "stationary distribution", "convex/concave", "sufficient statistic". |

### A2. Wittgenstein PI §§243–312 (`wiki/works/wittgenstein-1953-investigations/ch04-private.md`)

| ID | Old severity | Status | Evidence |
|---|---|---|---|
| W1 | critical | **fixed** | §249 is kept as a question: "The text asks whether we are over-hasty…". The parenthesis on lying follows it (96e). |
| W2 | major | **still present (worse)** | See S-W1 below. The challenge is attributed "presumably" to Wittgenstein, and W's verdict "An odd question" is given to "the first speaker". |
| W3 | major | fixed | §264: "gives the view … (voice unclear)". It is no longer presented as W's thesis. |
| W4 | major | fixed | §272 is tagged "(voice unclear)". The canonical instance and the inverted-spectrum bridge were removed. |
| W5 | major | fixed | L0 no longer turns §244's "one possibility" into the thesis. L2 bullet 2 keeps "one possible way". |
| W6 | major | fixed | The "Meaning is use" slogan is gone. The concept line is hedged ("perhaps", §270). A residual tag issue is counted as new minor N-W5. |
| W7 | major | fixed | Citations are now `(§N, p. M)`. Frontmatter reads `95e–110e`. Dropping the "e" is declared in Reading notes. |
| W8 | minor | fixed | §243: translation "and so predict their actions". |
| W9 | minor | fixed | §252: "could answer 'Nonsense!' but are inclined to say 'Of course!'". |
| W10 | minor | fixed | §265: **Interlocutor:** tag; "one memory to another". |
| W11 | minor | fixed | §281 wording matches. |
| W12 | minor | fixed (by omission) | The §289 counterfactual sentence is no longer paraphrased. |
| W13 | minor | fixed | §300: "Imagined pain certainly enters the game in a sense, only not as a picture". |
| W14 | minor | fixed | §292: "without guidance". |
| W15 | minor | fixed | The "Part II renamed" note was removed. |

### A3. Jaynes ch. 2 (`wiki/works/jaynes-2003-probability/ch02-quantitative.md`)

| ID | Old severity | Status | Evidence |
|---|---|---|---|
| J1 | critical | **fixed** | L2 no longer claims $A\bar B$ and $B\bar A$ get equal values. It now reads "Consistency of the product rule applied to $AB$ and $A\bar B$ forces $w^m(A|B)+w^m(\bar A|B)=1$" (pp. 30–33). |
| J2 | major | **fixed** | L2: "whether consistency can be proved from outside probability theory is left open" (p. 47). |
| J3 | major | **fixed** | The false "sign absorbed" gloss is gone. L3 uses only the source's $S'[S(x)]S'(x)=1$ (p. 32). |
| J4 | minor | fixed | The false "C implies A" misprint note is gone. The remaining misprint notes ((2.25) on p. 31, the capital $P$ in (2.84), the Ex. 2.2 parenthesis) are all confirmed on the images. |
| J5 | minor | fixed | Fisher is attached to the deducibility argument, and "does not suppose a logician would accept it" is kept (p. 46). |
| J6 | minor | fixed | Ex. 2.1 is worded "whether a formula … can be derived". |
| J7 | minor | fixed | No verifier residue. |
| J8 | minor | fixed | The formula without $|C$ was removed from L2. |
| J9 | minor | fixed | "illustrates … only in one special case"; Kolmogorov's axioms are "derived". |
| (meta) | — | fixed | `fields: [information-theory, bayesian]`. Bayes and Cox are linked to spine ids with "not named" tags. |

### A4. Dennett ch. 2 (`wiki/works/dennett-1987-intentional-stance/ch02-true.md`)

| ID | Old severity | Status | Evidence |
|---|---|---|---|
| D1 | major | **fixed** | Every citation now uses printed pages (13–41). Spot-checked 20; all land on the correct half-spread. |
| D2 | major | **fixed** | Fn. 2 now has "a mechanism disguised as a Martian yields a *true* sentence … so isolated from the events the Martian needed to know about" (p. 28). The source of the bafflement is now correct. A residual imprecision remains: "the Martian's prediction would still appear as a written Martian sentence" should be "his prediction *of the Earthling's prediction*". It is not counted. |
| D3 | minor | fixed | L2: "will prove correct". |
| D4 | minor | partly | "baldly stated" and "apparently" are now kept. "do not fairly represent any serious theorists' positions" is still dropped (p. 15). |
| D5 | minor | still present | Oxford colleges: "reasoning about what people would then do". The recursive "reasons … to give others reasons for…" chain is still lost (pp. 21–22). |
| D6 | minor | fixed | L1 no longer misplaces "a little". |
| coverage | — | mostly fixed | Now included: the Martian conclusion ("Where there are intelligent beings…", p. 28), the lectern contrast ("often the only practical way", p. 23), and Hayes 1979 (p. 31). Still missing: the Earthling-disguised-as-Martian twist (p. 27). |

---

## B. New audit

### B1. What was checked (150 items)

- **Cover (35):** L0, L1; all 8 L2 bullets; all 8 intuition notes; equations (2.74)–(2.75) with the added step, (2.84)–(2.90), (2.102) with the added step, (2.107), (2.130)–(2.135), (2.144)–(2.151); Ex. 2.6.1 numbers; Concepts (self-information, relative entropy/"cross entropy", max-ent, doubly stochastic); all instances' pages; all 6 exercise page refs; historical notes; Reading notes; toy (recomputed); 15 page refs.
- **Wittgenstein (42):** L0, L1; 8 L2 bullets; 5 intuition notes; voice and wording for §§243, 244, 246, 249, 251, 253, 257, 258, 260, 262, 265, 270–271, 277, 281–282, 288, 293, 295, 300, 304, 305–308, 311, 312; Concepts; Instances; Reading notes; 16 page refs; toy.
- **Jaynes (34):** L0, L1; 7 L2 bullets (3 sub-bullets); 4 intuition notes; equations and added steps (2.16)–(2.17), (2.25), (2.46), (2.52)–(2.53), (2.56)→(2.57), (2.58), (2.65)–(2.66), (2.73)–(2.77), (2.82)–(2.86), (2.87)–(2.95), (2.96)–(2.99); §2.6.1 voices; Gödel/Fisher; Kolmogorov; Concepts; Instances; Exercises; Reading notes; toy (recomputed); 20 page refs.
- **Dennett (39):** L0, L1; 8 L2 bullets; 6 intuition notes; three stances; belief attribution ("less than ten percent", "which I doubt very much"); fn. 1 objection voice; desires and baked beans; lectern; "it will be urged"; free choice vs objective; chess and KGB; Nozick voice; Mrs Gardner contest; fn. 2; milder realism; thermostat and Hayes; LOT hedge; the two empirical claims; Life rule (word by word); Quine/Davidson/Parfit voices; Concepts; Instances; Reading notes; toy; quote budget; 20 page refs.

### B2. Surviving errors (all digests)

| # | Digest / location | Problem | Evidence (printed page) | Severity |
|---|---|---|---|---|
| S-W1 (= W2) | Wittgenstein L3 §263 | §263 has three parts: "'Surely I can (inwardly) resolve…' — 'But is it certain that you have resolved this? …' — An odd question." Both quoted lines are voices; the unquoted "An odd question" is Wittgenstein's comment. The digest has "**Reply (speaker not marked, presumably Wittgenstein):** Is it certain…" and then "**The first speaker** calls this an odd question." The challenge goes to W (the opposite of the textual convention), and W's verdict goes to the interlocutor. A reader learns that W doubts the resolution, when in fact W dismisses that doubt as odd (cf. §246, §288). | 100e | **major** |
| N-W1 | Wittgenstein L3 §312 | "an objector asks whether the tooth and pain cases are not similar … and says that I can exhibit the visual impression to myself as little or as well as the pain." Nothing in §312 is in quotation marks or tagged. By the digest's own rule it should be "(voice unclear)". On the PI convention the unquoted text is W's, and the last sentence is W's own point (the visual impression is no more privately exhibitable than the pain). | 110e | **major** |
| N-C1 | Cover L2, last bullet | "Fano's inequality bounds $H(X|Y)$ … ; **equivalently** $P_e\ge\frac{H(X|Y)-1}{\log|\mathcal X|}$". The source calls (2.146) a **weakened** form ("This inequality can be weakened to"). It follows from (2.144) but does not imply it. L3 correctly says "Weakened forms". L2 is stronger than L3. | p. 39 | **major** |
| N-J1 | Jaynes L2 bullet 6 (and Questions, 3rd item) | "The consistency theorems **hold only** for finite sets". The source says they "have been **established only** for probabilities assigned on finite sets", and infinite sets are allowed via a well-behaved limit. "Hold only" asserts failure elsewhere. L3 has it right ("established only"). | p. 43 | **major** |
| N-D1 | Dennett L3, prediction contest | "The Martian can make the same prediction only with vast knowledge of physical interactions. **His** performance would look like magic to anyone without the intentional strategy." The antecedent of "His" is the Martian. The source says "**The Earthling's** performance would look like magic!" (to the Martian, who lacks the intentional strategy). This reverses the point of the thought experiment. | p. 27 | **major** |
| N-C2 | Cover L0 | "relative entropy and mutual information are built from [entropy]". Relative entropy is defined independently (p. 18). Mutual information is a special case of relative entropy (p. 12). | pp. 12, 18 | minor |
| N-C3 | Cover Reading notes | "1991 **first edition**": the page shows only "Copyright © 1991" and the ISBN. "First edition" is an inference, not printed (rule 14). | p. 12 | minor |
| N-C4 | Cover L2, last bullet | It packs two unrelated ideas (sufficient statistics and Fano) into one bullet (spec: one idea per bullet). | — | minor |
| N-W2 | Wittgenstein L1 | "He **denies being a behaviourist**". §307's answer to "Aren't you … a behaviourist in disguise?" is "If I speak of a fiction, then it is of a *grammatical* fiction". This is a qualification, not a flat denial. | 109e | minor |
| N-W3 | Wittgenstein L2, last bullet | "**Charged with behaviourism**, he says that he denies not the inner process but that its picture gives the correct idea of … 'remember'". This merges §305 (the remembering challenge, not a charge of behaviourism) with §307 (the charge). | 109e | minor |
| N-W4 | Wittgenstein L3 §262 | "Someone who has given himself a private explanation … must inwardly resolve…" is stated flatly. The source opens with "**One might say:**", which marks it as a tempting view. | 99e | minor |
| N-W5 | Wittgenstein L3 §277 | "When I mean the impression that belongs to me alone…". The source has "(**as I should like to say**) belongs to me alone". The hedge marking the private-linguist inclination is dropped. | 103e | minor |
| N-W6 | Wittgenstein Concepts | Canon ids `[[meaning as use]]`, `[[rule-following problem]]` and `[[logical form vs. grammatical form]]` are linked without the required "(canon link; not stated in this unit)" tag (prompt rule 8/10). The canon definitions (`canon/analytic-philosophy.md` ll. 320, 331) are not what these remarks state. The logical-form id in particular (Russell's analysis) is a stretch for §§246/290. | 95e–106e | minor |
| N-W7 | Wittgenstein Reading notes | "Edition: 4th ed., Wiley-Blackwell 2009". The pages show only the running head, the file slug "9781405159289 … 23/6/09" and "95e"–"110e". "4th ed." and "Wiley-Blackwell" are not printed (rule 14). The claim is true, but it comes from memory. | 95e header | minor |
| N-J2 | Jaynes L0 | "degrees of plausibility … **must obey** the product rule and the sum rule, and they can be rescaled". In the source, a monotonic function $w$ (then $w^m$) obeys the rules, not the plausibilities $x$ themselves (pp. 29, 33, 41). L1 and L2 get this right. | pp. 29, 33 | minor |
| N-J3 | Jaynes L3 §2.6.2, last bullet | "Whether consistency can be proved by going outside probability theory **is an open question**". The source says "At the moment, this **appears to us** to be an open question". | p. 47 | minor |
| N-J4 | Jaynes L3 §2.6.4 | "He claims this gives analytical resources absent from Kolmogorov's system". The source says "**Partly** as a result, our system has analytical resources…". | p. 50 | minor |
| N-D2 | Dennett L3, "Two empirical claims" | It omits Dennett's own hedge on claim (2): "There *are* reasons for believing in the second pattern, but they are not overwhelming." L2 and the intuition note keep a weaker form of the hedge ("not necessarily true", "far from assured"), so no summary is stronger than the source. | p. 34 | minor |
| N-D3 | Dennett (whole digest) | Quote budget: 12 quoted spans of ≥ 4 words that are Dennett's own words. The limit is 10 (prompt rule 13). | — | minor |

Persisting known minors (not counted again in B): C5, C10 (partly), D4 (partly), D5.

### B3. Things checked and found correct (highlights)

- **Cover:** every equation sampled matches the image symbol by symbol. The added steps for (2.72) (derivative terms cancel) and (2.100) (multiply by $\sum b_j$) are correct. Reading notes are accurate: the (2.121) misprint, "four" vs five interpretations, "positive numbers" in the summary box, and the Thm 2.6.4 equality case. The concept line flags Cover's "cross entropy" = $D$ against the canon. Toy: $H(X,Y)=1.81128$; $I=0.18872$ by three routes; the DPI step is valid.
- **Wittgenstein:** voice tags are now correct in §§243, 244, 246, 258, 260, 265, 281, 282, 288, 296, 303, 304, 305, 307. "(voice unclear)" is used in §§264 and 272. Every § and page reference checked is correct. The hedges "perhaps" (§270), "One possibility" (§244 in L2) and "if we construe … object and name" (§293 in L1/L2) are kept.
- **Jaynes:** all five marked added steps are literally true. I verified (2.17), (2.46), (2.57) and (2.58) symbolically. Hedges kept: "We do not suppose that any logician would accept…", "evidently also sufficient", "as far as one can see, arbitrary axiom", "very innocuous", "Canon link: Bayes' theorem; not named". The toy example is correct under both $p$ and $w=\sqrt p$.
- **Dennett:** the Nozick objection, "it will be urged" and "it may be urged" are all tagged. The LOT modal ("provided one allows great latitude for attenuation … will prove correct", "not obvious") is exact in L3 and L2. The Life rule matches word for word. The Parfit and Quine quotations are correctly attributed. In the toy, the blinker counts are right, and Part B (two rival interpretations tying at 8/10) now illustrates the *intentional*-level point (p. 29), fixing the earlier "off-target toy" criticism.

---

## C. Length vs source and usefulness (B2 reader, high-school start)

Word counts are body words. Source words come from the text layer, except Dennett (scan), which is estimated at about 430 words per printed page. Targets come from `build.target_words` (f = 0.40; 0.55 for scans; cap 6000).

| Digest | Source words | Target | Digest | Ratio to target | L3 words | L1 words | L2 bullets |
|---|---|---|---|---|---|---|---|
| Cover ch. 2 | ≈ 11,000 | ≈ 4,400 | 5,036 | 1.14 | 3,585 | 103 | 8 |
| Wittgenstein | ≈ 7,000 | ≈ 2,800 | **5,917** | **2.1** | 4,400 | 115 | 8 |
| Jaynes ch. 2 | ≈ 12,100 | ≈ 4,850 | 5,584 | 1.15 | 4,043 | 98 | 7 |
| Dennett ch. 2 | ≈ 11,000 | 6,000 (cap) | 6,487 | 1.08 | 4,650 | 99 | 8 |

- **Cover:** within the tolerance for dense math. It is excellent as a reference sheet: every tag is present, misprints are flagged, 8 intuition notes, and a correct toy. For an HS-start reader L0–L2 are still opaque (C10 partly). A Prerequisites line now exists, but "Markov chain", "stationary distribution", "convex" and "sufficient statistic" are used in L2 without a ≤ 15-word gloss. Level `grad` is honest.
- **Wittgenstein:** **far over target**. At 85% of the source's own length, it is close to a remark-by-remark retelling. It still has no argument map (the earlier audit's P-5a was not adopted), so a reader cannot tell which remarks carry the argument (§§243 → 258 → 265–271 → 293 → 304–308). Voice handling is much better than v1 and is now the digest's main strength. The intuition notes are short and faithful. The toy (two diarists, manometer, swap X/Y) is better than v1's "15 − 15" but still builds in its conclusion (both diarists are stipulated to write "S" on the same days). For a B2 reader the volume is the main barrier.
- **Jaynes:** within tolerance. Skip paths, the Prerequisites line, and the spine-linked concepts all help. The Cox derivation is still a grad-level ladder; an HS-start reader would need the skip path plus the intuition notes only. The intuition note after (2.73) ("evidence moves a hypothesis a lot only if it would be surprising otherwise") is the best single teaching line across the four digests.
- **Dennett:** at the cap and appropriate for a 27-page chapter. Several terms are now glossed inline (LOT, combinatorial explosion, Game of Life, de-interpret, Twin Earth). Still undefined: *Laplacean*, *instrumentalistic*, *de re*. It is useful for the target reader, and the bridges to ToM, IRL identifiability and ABMs are well chosen.

---

## Notes and verdict

1. **Regression target met.** All 4 known critical errors and 10 of 11 known majors are fixed. Logical-strength errors in the *flagged* places (C1/C3, J2, D3, W5) were all repaired. The v2.2 rules on voice tags, "(voice unclear)", canon-link tags and printed pages are visibly followed.
2. **Residual pattern.** All 5 surviving majors (W2 and 4 new) are of the two types the v2.2 rules target: voice (3) and L2 strength (2). That is about 1 major per unit and 0 critical, against about 1 critical and 2–6 majors per unit in v1. Three of them sit in places the verifier probably did not treat as "strength" sentences: a pronoun antecedent (N-D1), a last fragmentary remark (N-W1), and "equivalently" / "hold only" (N-C1, N-J1). The deterministic STRONG regex in `build.py` lacks *equivalently*, *hold(s) only*, *established only* and *denies*. Adding them, plus a voice check on every unquoted/quoted switch in dialogic texts, would catch N-C1, N-J1 and N-W2.
3. **W2 is the one regression.** The verifier "repaired" §263 into a different wrong attribution. Voice repairs should be checked against quotation marks in the image, not inferred.
4. **Length control fails for the short dialogic unit** (Wittgenstein, 2.1× target). The cap logic works for the others.

**Verdict:** all four digests are **acceptable as knowledge-base sources after five hand fixes**:
- (S-W1) §263: tag both quoted lines as voices and give "An odd question" to Wittgenstein.
- (N-W1) §312: replace "an objector" with "(voice unclear)".
- (N-C1) Cover L2: replace "equivalently" with "a weaker form is".
- (N-J1) Jaynes L2 and Questions: replace "hold only" with "have been established only".
- (N-D1) Dennett: replace "His performance" with "The Earthling's performance would look like magic to the Martian".

Wittgenstein should additionally be shortened toward about 3,000 words, with an argument map, before posts build on it.
