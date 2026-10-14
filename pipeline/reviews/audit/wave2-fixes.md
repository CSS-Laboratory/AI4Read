# Wave-2 audit fixes

Date: 2026-10-14. Fixer: Claude Opus 5.5. Inputs: `wave2-regression.md`, `wave2-argumentative.md`, `wave2-math.md`.

Scope: every critical and major error, plus every minor error that a one-line wording fix can repair. Each item was first checked against the source page image. Edits were kept minimal and followed DIGEST_SPEC v1.2 and prompt v2.2: only the source, the same strength and hedges, the correct voice, printed pages, and L1 ≤ 120 words (re-counted after each edit). Glosses for undefined-term majors are ≤ 15 words and placed at first use.

Rules for leaving items unfixed:
- Pure coverage omissions (adding content that is missing) were not fixed. They are not wording fixes.
- Concept-id renames were not made. Changing an id can break links in other files.

Each fixed digest has `audited: 2026-10-14` and `audit_fixes: <n>` in its frontmatter. `cover-2006-elements/ch02-entropy.md` was not touched.

## Cover ch. 2 (`ch02-entropy.pipeline.md`, 5 fixes)

| ID | Status | Note |
|---|---|---|
| N-C1 (major) | fixed | L2: "equivalently" → "a weaker form is" (p. 39: "can be weakened to"). |
| N-C2 | fixed | L0: mutual information "extends" entropy and is a special case of relative entropy (p. 12). |
| N-C3 | fixed | Reading note now says only what is printed: copyright 1991 and the ISBN, with no edition number. |
| N-C4 | fixed | The sufficient-statistic and Fano ideas are now two separate bullets (L2 has 9 bullets). |
| C5 | fixed | $0\le p(x)\le1$ (p. 14 image). |
| C10 (minor, partly) | not fixed | Adding glosses to L0–L2 is not a one-line wording fix, and the audit rates it minor. |

## Wittgenstein §§243–312 (`ch04-private.md`, 8 fixes)

| ID | Status | Note |
|---|---|---|
| S-W1 / W2 (major) | fixed | §263: both quoted lines are tagged as voices, and "An odd question" is given to Wittgenstein (unquoted) (100e image). |
| N-W1 (major) | fixed | §312: "an objector" → "voice unclear, since nothing is in quotation marks" (110e). |
| N-W2 | fixed | L1 now reports §307's "grammatical fiction" answer and §308's "we don't want to deny them", not a flat denial. The L1 count is 119 words. |
| N-W3 | fixed | L2 separates §305 (the remembering challenge) from §307 (the behaviourism charge). |
| N-W4 | fixed | §262 now opens with "One might say:" (99e). |
| N-W5 | fixed | §277 restores "(as I should like to say)" (103e). |
| N-W6 | fixed | Three canon concept lines are tagged "(canon link; not stated in this unit)". |
| N-W7 | fixed | Edition line is limited to the printed header and the printer's slug. |
| Length / argument map (verdict note) | not fixed | Shortening to about 3,000 words is a rewrite, outside the scope of minimal fixes. |

## Jaynes ch. 2 (`ch02-quantitative.md`, 4 fixes)

| ID | Status | Note |
|---|---|---|
| N-J1 (major) | fixed | "hold only" → "have been established only", in both L2 and Questions (p. 43). |
| N-J2 | fixed | L0: "a monotonic function of them must obey" the rules. |
| N-J3 | fixed | "appears to Jaynes, at the moment, to be an open question" (p. 47). |
| N-J4 | fixed | "partly as a result" (p. 50). |

## Dennett ch. 2 (`ch02-true.md`, 4 fixes)

| ID | Status | Note |
|---|---|---|
| N-D1 (major) | fixed | "The Earthling's performance would look like magic to the Martian…" (p. 27). |
| N-D2 | fixed | Adds Dennett's hedge: there *are* reasons for (2), but they are not overwhelming (p. 34). |
| D4 | fixed | Restores "do not fairly represent any serious theorist's position" (p. 15). |
| D5 | fixed | Oxford colleges: the recursive reasons chain is restored (pp. 21–22). |
| N-D3 (quote budget) | not fixed | Choosing which of 12 quotes to paraphrase is not a one-line fix. |

## Kripke Lecture II (`ch02-lecture.md`, 9 fixes)

| ID | Status | Note |
|---|---|---|
| K-M1 | fixed | L0: "need not be known a priori". L3: "it seems we do not necessarily know a priori" (p. 101). |
| K-M2 | fixed | L1: "meet counterexamples and, perhaps more significantly, circularity". L3: "perhaps more significantly" (p. 89). |
| K-M3 | fixed | n. 33: "If Leverrier indeed gave the name before the planet was ever seen…" (p. 79). |
| K-M4 | fixed | Glosses added for idiolect, analytic, ostension, nomological dangler, transworld identification, counterpart theory and a posteriori (in Prerequisites). |
| K-m1 | fixed | Reading note: the image prints (1)–(6) and (C); only the text layer drops them. The "I assigned" sentence was removed. |
| K-m2 | fixed | Citation is now pp. 98–99. |
| K-m3 | fixed | The physical-necessity parenthesis now follows p. 99. |
| K-m4 | fixed (partly) | Rigid designator now flags the difference from the canon. Necessary a posteriori has the canon tag. The epistemic-possibility line notes the lecture's own wording. Ids with spaces were not renamed. |
| K-m6 | fixed | Q3 adds "hard to avoid concluding that the two are different". |
| K-m5 | not fixed | Coverage (nn. 38, 43). |

## Kuhn ch. IX (`ch09-nature.md`, 11 fixes)

| ID | Status | Note |
|---|---|---|
| U-M1 | fixed | L1 and L2 now include "to the extent that … disagree about what is a problem and what a solution" (p. 109). |
| U-M2 | fixed | L0: "after the pre-paradigm period" (p. 96). |
| U-M3 | fixed | L3 and Q3: "a sense in which they are constitutive of nature as well" (p. 110). |
| U-M4 | fixed | L1 and L2: what Kuhn rejects is the *derivation* of Newton's laws. An old theory can be viewed as a special case only after transformation (pp. 101–103). |
| U-M5 | fixed | Glosses added for logical positivism, caloric theory, phlogiston, ether, incommensurable, charging by induction, Leyden jar and electric displacement. |
| U-m1 | fixed | The "hard to see how new theories could arise…" sentence was added to L3 (p. 98), and L0 was aligned with it. |
| U-m2 | fixed | "When paradigms enter a debate about paradigm choice, their role is circular". |
| U-m3 | fixed | "most engineers and, in selected applications, many physicists". |
| U-m4 | fixed | "an argument of the same type is used to justify…". |
| U-m5 | fixed | "Without the data and chemical concepts developed in that work…". |
| U-m6 | fixed | Q1 no longer uses a non-verbatim quote. |
| U-m7 | not fixed | Coverage. |

L1 was re-trimmed to 120 words.

## Habermas ch. V (`ch05-social.md`, 15 fixes)

| ID | Status | Note |
|---|---|---|
| H-C1 (critical) | fixed | The mechanism, which Galbraith also analysed, explained the link between capital concentration and interventionism (p. 146). |
| H-M1 | fixed | Restored "increasingly", "in a certain fashion", "tendency toward levelling" and "has started to dissolve" (pp. 155–157). The citation is now pp. 155–156. L1 was softened to match. |
| H-M2 | fixed | Glosses added for mercantilist/neomercantilist, oligopolistic, Aktiengesellschaft, petty commodity exchange, do ut des, conjugal family, intimate sphere, internalization, acclamation, mediatized public and plebiscitary. |
| H-m1 | fixed | L1 last sentence follows pp. 142–143 ("had its source in"). |
| H-m2 | fixed | L2 marks the plebiscitary claim as a passage Habermas quotes. |
| H-m3 | fixed | The intuition note drops the invented "not merely power" contrast. |
| H-m4 | fixed | "appeared to be no more than a 'vast secular boom'". |
| H-m5 | fixed | The "the more … the more" comparative is restored. |
| H-m6 | fixed | Socialist Law is "a prime example"; *but* the Insurance yielded to pressure from below. |
| H-m7 | fixed | The concept line now follows p. 142 (public functions go to private bodies, and public authority extends over the private realm). |
| H-m8 | fixed | "Under the given circumstances", in both L3 and Q2. |
| H-m9 | fixed | "often". |
| H-m10 | fixed | The "To the extent that…" condition is restored. |
| H-m11 | fixed | The "flexible enough … could have been invented" wording is restored. |
| H-m12 | fixed | "often already … detailed administrative dispositions"; "can scarcely be demanded, let alone accomplished". |

## Grice 1975 (`main.md`, 9 fixes)

| ID | Status | Note |
|---|---|---|
| G-C1 (critical) | fixed | Relation is now "perhaps a different reason for doubt" about the second Quantity maxim, separate from the reply (p. 46). |
| G-M1 | fixed | "To speak approximately" and "may not be impossible" are restored in feature 3. L2 adds "to speak approximately" (p. 58). |
| G-M2 | fixed | Glosses added for ceteris paribus, supermaxim, perspicuous, meiosis, tautology and categorially false. "explication" does not occur in the digest. |
| G-m1 | fixed | "does not want to say … would be, strictly speaking, false" (p. 45). |
| G-m2 | fixed | L1 now rests implicature on the presumption of cooperation; blatant failure is given as an example (pp. 49–51). |
| G-m3 | fixed | "(or doing so in THOSE terms)" (p. 50). |
| G-m5 | fixed | The (3b) conditional title is restored, and the Relation remark now reads "it is arguable … without invoking an alleged second maxim" (pp. 52–53). |
| G-m6 | fixed | "is often given without the giver knowing just what use…" (p. 57). |
| G-m7 | fixed (partly) | Category labels were added to the four analogues. The omitted framing sentences are coverage and were not added. |
| G-m4 | not fixed | Coverage. |
| G-m8 | not fixed | Concept-id rename. |

## Clark et al. ch. 12 p1 (`ch12-parliamentary-p1.md`, 10 fixes)

| ID | Status | Note |
|---|---|---|
| C-C1 (critical) | fixed | The Reading note no longer names the UK. It now reads "a further example, after the 2010 legislative elections" (p. 481). |
| C-M1 | fixed | Glosses added for ideal point (p. 478), proportional representation, single-member district plurality, mixed (= semi-presidential, fn. 1, p. 458) and impeachment. |
| C-m1 | fixed | "felt compelled", in both L3 and Canonical instances. |
| C-m2 | fixed | "hard, if not impossible". |
| C-m3 | fixed | "do not explicitly command". |
| C-m4 | fixed | Restored "somewhat dubious circumstances", "surprisingly" and "starkly partisan". The intuition note was aligned with L3. |
| C-m5 | fixed | The Figure 12.3 description now includes the freestyle-bargaining branch (the old sentence misdescribed the chart, p. 471). |
| C-m7 | fixed | The Edition note cites only the proof stamp in the p. 463 text layer. The image itself shows only the map. |
| C-m8 | fixed | Toy step 1 now also lists A+B+D and A+B+C+D as non-minimal. |
| C-m9 | fixed | 13 page ranges changed from "(p. …–…)" or "(p. …, …)" to "pp.". |
| C-m6 | not fixed | Coverage. |

## Gelman BDA3 ch. 5 (`ch05-hierarchical.md`, 6 fixes)

| ID | Status | Note |
|---|---|---|
| G1 | fixed | "perhaps, given the expected outliers, the prior should have wide tails" (p. 106). |
| G2 | fixed | Glosses added for half-Cauchy, inverse-gamma, logit, Jacobian, random-effects model, scaled inverse-χ², order statistics, HPD interval and half-$t$. Prerequisites now include change of variables. |
| G3 | fixed | "One reasonable choice" (p. 110). |
| G4 | fixed | "$\tau$ might be close to zero"; "relatively informative" (pp. 126–127). |
| G5 | fixed | The "Unless you are familiar with divorce statistics" condition and the beta/logit-normal suggestion are restored (p. 105). |
| G6 | fixed | The "largely overlap / median-centred" half is now cited to p. 122. |
| G7, G8 | not fixed | Coverage. |

## Åström & Murray ch. 7 (`ch07-state.md`, 5 fixes)

| ID | Status | Note |
|---|---|---|
| A1 | fixed | L1: "will in general require large control signals" (p. 7-22). |
| A2 | fixed | Glosses added for impulse, Cayley–Hamilton, positive definite, frequency response, resonant peak, bandwidth and Jordan form. |
| A3 | fixed | p. 7-15 added for Theorem 7.3. |
| A4 | fixed | The unsupported "later design chapters build on it" was removed from L1. |
| A5 | fixed | L0 is now one sentence. |

## Bellman ch. III (`ch03-iii.md`, 6 fixes)

| ID | Status | Note |
|---|---|---|
| B1 (critical) | fixed | L2 bullet 8 and the §10 intuition note: Procedure B starts from $f_0$, the return of an initial policy $q_0$. That start is why $f_1\ge f_0$ (p. 89). |
| B2 | fixed | (5.1) and (5.2) now show $\int_{z\in D}$, as printed on the p. 85 image. The parenthetical note was corrected. |
| B3 | fixed | "difficulty of establishing the existence of an actual maximum" (p. 86). |
| B4 | fixed | Glosses added for Stieltjes integral (Prerequisites), finite closed region, jointly continuous, calculus of variations, Banach space, branching processes and Huygens' principle. |
| B5 | fixed | HJB concept line has the canon tag and says the name does not appear. |
| B6 | fixed (partly) | "easy" → "not too difficult" (p. 82). The two omitted sentences (p. 82, fn. 4) are coverage. |

## Kalman 1960 (`main.md`, 7 fixes)

| ID | Status | Note |
|---|---|---|
| K1 (critical) | fixed | "$x_2(1)$" (p. 43). |
| K2 (critical) | fixed | The false "grows with $P^*M'$" sentence was replaced with the audit's degree-0 wording based on (28). |
| K3 (critical) | fixed | L2: "For zero-mean processes…" (Theorem 2, p. 38). |
| K4 | fixed | (37) restored as printed ($\hat\Phi'$), with an equivalence note (p. 42). |
| K5 | fixed | Glosses added for impulse response, spectral factorization, Wiener–Hopf equation, rational spectra, Schmidt orthogonalization, Hilbert space and realizable. "linear manifold" does not occur in the digest. L1 was re-trimmed to 120 words. |
| K6 | fixed | Reading note now flags the printed $C_3$ and $\phi_{3s}$ (p. 44) and $\hat M(t)$ in Remark (o) (p. 43) as misprints. |
| K8 | fixed | "this is true also in Example 1" was added to the existing sentence. |
| K7 | not fixed | Coverage (first half of Remark (b)). |

## Disagreements with the audits

None on substance. Every critical and major error was confirmed on the page images. One small difference from the audit's suggested text: for N-J3 I paraphrased instead of quoting, to stay within the quote budget.
