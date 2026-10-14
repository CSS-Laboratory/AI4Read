# Wave 5 audit fixes (2026-10-15)

Sources: `wiki/works/<work>/<unit>.md`, checked against `/home/claude/audit/w5/<work>__<unit>.pdf`. Every fix was verified against the page images before editing:
- Spielman: pp. 189–195 (all pages).
- Särkkä & Svensson: pp. 204, 207, 208, 211, 216, 227.
- Kelly: pp. 917, 918, 920, 924.
- Arrow: pp. 34–45 (all pages).
- Tractatus: pp. 42–48, 50–53.
- Hall: title page, pp. 1, 7, 19. The p. 19 date was checked in a 300 dpi crop next to the title-page date. Hedge wording on pp. 4, 9, 12, 13, 15, 17, 18–19 was checked in the text layer.

Edits are minimal and nothing was cut. All six digests got longer (Spielman 1,806 → 2,005 words; Arrow 3,222 → 3,520; Hall 4,397 → 4,569; the others +75 to +85). Every edited digest now has `audited: 2026-10-15` and `audit_fixes: <n>` in its frontmatter. Undefined-term majors were fixed with inline definitions of 15 words or fewer at first use. For a term that first appears in L0/L1, the definition went in the Prerequisites line or in L1 if the word budget allowed.

## Math audit (wave5-math.md)

### Spielman ch. 23: 7 fixes
| ID | Status | Note |
|---|---|---|
| P1 | fixed | L0: "with at most $288p(1-p)/(p-q)^2$ errors: a constant number for fixed p and q, a constant fraction for p = 1/2, q = p − 17/√n" (p. 194). This follows the source's own case and does not use the audit's "$p-q\sim1/\sqrt n$". |
| P2 | fixed | Definitions added for spectral norm and Courant–Fischer (Prerequisites), multiplicity and eigenspace (§23.2), and information-theoretically unsolvable (intro). `[[norm]]` now says spectral norm. |
| P3 | not fixed | Length (1.74×). The brief says not to shorten digests. |
| P4 | fixed | "Why the gap matters (pp. 192–193)". `[[norm]]` now cites p. 191. |
| P5 | fixed | Added "no reason to believe … useful in practice. Nevertheless, some of them are" in L2 and L3 (p. 190). |
| P6 | fixed | Restored the premise that the X/Y partition "will not be the smallest" (p. 189). Added a one-line §23.5 ([Ver10], [Tro12], p. 195). |
| P7 | fixed | Toy: added one line saying it shows only the step to $\|\delta\|$, sits at the boundary $q=p/3$, and gives a vacuous $k$ bound of 432 for n = 4. |
| P8 | fixed | Bridge 2 relabelled `same-math`. |

### Särkkä & Svensson ch. 10: 6 fixes
| ID | Status | Note |
|---|---|---|
| S1 | fixed | "can be seen as a type of PL" (p. 227) |
| S2 | fixed | Definitions added for sigma points and cubature/Gauss–Hermite (Prerequisites), Gauss–Newton, CKF/GHKF/UKF, RMSE, EKF and MAP |
| S3 | fixed | "may strongly affect filter performance" (p. 204) |
| S4 | fixed | L2: "aims to be accurate" (p. 207, "seeks") |
| S5 | fixed | "this is added bookkeeping" replaced by "(added step)" |
| S6 | fixed | "Some non-additive noise models also have closed-form conditional moments; important examples are the Chapter 4 dynamic models with state-dependent covariance" (p. 216) |

### Kelly 1956: 4 fixes
| ID | Status | Note |
|---|---|---|
| K1 | fixed | "Generally, that cost would depend…" (p. 918) |
| K2 | fixed | Definitions added for coding theorem (L1; now 114 words), conditional entropy $H(X/Y)$ (Prerequisites), equivocation, von Neumann utility theory and parimutuel betting |
| K3 | fixed | "(including that one dollar)" (p. 920) |
| K4 | fixed | L2: "equal to a constant $k$ for outcomes bet on, and at most $k$ for the rest" (p. 924) |

## Argumentative audit (wave5-argumentative.md)

### Arrow ch. IV: 11 fixes
| ID | Status | Note |
|---|---|---|
| A-M1 | fixed | L2 b5: Condition 3 is satisfied "if one waives, as Arrow does for argument's sake (fn. 14), its application to nonadmissible alternatives". L3: the fn. 14 reservation is added with the "simply waiving the issue" quote (p. 42). |
| A-M2 | fixed | "In a one-commodity world, of course, the ambiguity disappears (p. 40)." |
| A-M3 | fixed | `[[compensation-principle]]` now gives both senses: paid, which reduces to unanimity (p. 34), and Kaldor's possible-but-unpaid version (p. 38) |
| A-M4 | fixed | Definitions added for Bergson's Fundamental Value Propositions, marginal rate of substitution, production-side optimum conditions, summation-of-utilities criterion, marginal utility of real income and utility indicators |
| A-m1 | fixed | L2 b3 and L3: "doubts that any study of maximal alternatives will be useful for those aspects of social choice tied to consumer's (and worker's) choice" (p. 37) |
| A-m2 | fixed | L2: "The x–y comparison also strongly suggests…" (p. 45) |
| A-m3 | fixed | L1: "(under the usual assumption (6))" and "may leave". L1 is 118 words. |
| A-m4 | fixed | Objection (1) now includes the rich/poor point. The reply to (2) now has "especially so if … as Baumol himself observes in a footnote" (p. 38). |
| A-m5 | fixed | "arbitrary in the sense that another rule … could have been chosen", in L2 and L3 (p. 39) |
| A-m6 | fixed | Buridan instance now refers to the nonmaximal case (p. 37) |
| A-m7 | not fixed | Coverage: five omitted points. Not a one-line fix. |
| A-m8 | not fixed | Adding two intuition notes is new content, not a wording fix. |
| A-m9 | fixed | Toy: added a caveat that x and y have the same totals, so $xCy$ and only one would be admissible under Arrow's restatement. The toy shows the Kaldor paradox, not the three-state intransitivity. |

### Wittgenstein, Tractatus 3.344–4.5: 12 fixes
| ID | Status | Note |
|---|---|---|
| T-C1 | fixed | §4.442: "(TT–T)(p, q)", or more plainly "(TTFT)(p, q)"; the dash fills the TF place (p. 52 image). The Reading note is replaced to match. |
| T-m1 | fixed | L1: the "Because … So" chain is removed; the two claims are now stated side by side |
| T-m2 | fixed | §4.1121: "(the 'Only …' that follows implies yes: it does correspond)" |
| T-m3 | fixed | §4.112: "the making clear of propositions", plus the "make clear and sharply bound … murky and blurred" sentence (p. 44) |
| T-m4 | fixed | L2 b4 is now conditional: "If one does not see … one can easily believe…" (§4.061) |
| T-m5 | fixed | "$K_n$ rows (added step: the row count follows from §4.28)" |
| T-m6 | fixed | §4.241: "Wittgenstein stipulates: if I use two signs … I express this…". §4.1272: "presented in logical symbolism by variables, not by functions or classes" |
| T-m7 | fixed | Map/mapping-rule intuition note replaced by one based on §§4.12–4.121 (form shared, not depicted; it shows itself) |
| T-m8 | fixed | "4.05–4.0641 (pp. 42–44)"; "§4.45, pp. 52–53" (images checked) |
| T-m9 | not fixed | Coverage: about ten omitted propositions. Not a one-line fix. |
| T-m10 | fixed | §4.1252 note now reports the edition misprint (p. 47 image: "aRx . aRy . yRb"; p. 48: "aRx . xRy . yRb"). First-person wording is removed from the Reading notes. |
| T-m11 | fixed | "colour exclusion" removed; the question now cites §4.211 |
| T-m12 | fixed | "(canon link; not stated in this unit)" added to `[[picture theory of meaning]]` |
| T-m13 | not fixed | Verbatim spans and the 2.53× length both need a rewrite or compression of L3, which the brief rules out. Regeneration (as the audit recommends) is still needed. |
| T-m14 | not fixed | A borderline minor, and not a wording fix. These are mostly Wittgenstein's own undefined terms (logical syntax, logical co-ordinates), and glossing them risks adding outside doctrine. |

### Hall 1973: 8 fixes
| ID | Status | Note |
|---|---|---|
| H-M1 | fixed | L0 now separates the two sentences: "improving communications" is "extremely difficult to call a neutral goal" (p. 18); making the elites' hegemonic codes more effective is "a political, not a technical, choice" (p. 19) |
| H-M2 | fixed | Definitions added for sign-vehicle, deep structure / surface transformations, marked / unmarked, reference-code, condensation / displacement, corporate, ideological apparatus, totalisations and detotalize / retotalize |
| H-m1 | fixed | "has a great deal to do with … also has something to do with" (p. 4) |
| H-m2 | fixed | L2 b8: the object is now "a political choice (whether to make the dominant codes more effective)" (p. 19) |
| H-m3 | fixed | All six hedges restored: "may be bounded", "we might say", "tempted", "(if the analytic distinction can be made for the moment)", "more intimately", "it is now perfectly clear … only" |
| H-m4 | fixed | Instance: "violence speculatively read as messages about conduct" |
| H-m5 | fixed | (a) "*Left Handed Gun*?" and "*Butch Cassidy*?" restored, with "garbled in the source" removed (p. 7 image). (b) The 1975 note is replaced: both dates read 1973 in the images (300 dpi crop), and "1975" is an OCR error. (c) p. 1 (pdf 2) is now noted as unnumbered. (d) The process note is removed. |
| H-m6 | not fixed | Coverage: eight omitted caveats. Not a one-line fix. |
| H-m7 | not fixed | Verbatim spans: rewording them means rewriting several passages. |
| H-m8 | fixed | "by not overtly biasing its operations" (p. 17) |

## Disagreements with the audit
None on substance. Two fixes differ in wording from the audit's suggestion:
- **P1.** The audit's "a constant fraction when $p-q\sim1/\sqrt n$" is replaced by the source's own case ($p=1/2$, $q=p-17/\sqrt n$). For small constants the bound can exceed $n$, so the general phrasing would be stronger than p. 194.
- **P8.** The bridge is relabelled `same-math`, not dropped.

Every item listed as not fixed was skipped for scope (length, coverage, verbatim spans, new content), not because the finding is wrong.
