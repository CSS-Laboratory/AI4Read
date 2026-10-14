# Wave 1 audit fixes (2026-10-14)

Source reports: `wave1-argumentative.md`, `wave1-math.md`, `wave1-social.md`.
Every fix was checked against the page images in `/home/claude/audit/w1/` (text layer used only to locate passages).
Several reports reuse IDs (A1, C1), so each ID below is prefixed with its digest.
Each fixed digest now carries `audited: 2026-10-14` and `audit_fixes: N` in its frontmatter.

**Totals:** 93 fixes applied across 12 digests. Not fixed: 3 items, plus 1 item fixed only in part. All 25 critical/major items were fixed.

| Digest | ID | Severity | Status | Note |
|---|---|---|---|---|
| Gettier | G1 | minor | fixed | L1 last sentence now gives the reason: the analyses were offered as necessary and sufficient conditions (p. 121) |
| Gettier | G2 | minor | not fixed | Disagree: the canon spine (`canon/analytic-philosophy.md`) uses display names with spaces as ids, e.g. `justified true belief (JTB)`; renaming would break the canon match |
| Gettier | G3 | minor | fixed | Removed the pipeline meta-sentence from Reading notes |
| Godfrey-Smith | K1 | critical | fixed | L1: he agrees with Kuhn on history; one must ask which claims are descriptive and which normative (pp. 78–79) |
| Godfrey-Smith | K2 | major | fixed | Replaced the toy: the counting threshold misrepresented the main mechanism. New toy has two labs, a "poor workman" failure vs. a deep anomaly, and no count (pp. 82–83) |
| Godfrey-Smith | K3 | major | fixed | Prerequisites now name logical empiricism; glosses added for Trojan horse, epistemological, cellular automata (source's own definition, p. 85) and simpler empiricism |
| Godfrey-Smith | K4 | minor | fixed | "much of his writing, and most later work by others" (p. 77) |
| Godfrey-Smith | K5 | minor | fixed | Restored "Amusingly… Kuhn even suggests" and "quite useless for normal science" (p. 82) |
| Godfrey-Smith | K6 | minor | fixed | L2 now says the broad/narrow labels are Godfrey-Smith's |
| Godfrey-Smith | K7 | minor | fixed | `[[falsifiability]]` marked "differs from canon" |
| Godfrey-Smith | K8 | minor | fixed | Added Popper's concession (p. 81) |
| Godfrey-Smith | K9 | minor | fixed | Corrected the sentence about willingness to revise going too far (p. 83) |
| Carey | C1 | major | fixed | `[[entropy]]` marked "differs from canon: … not Shannon entropy"; L3 note says the same |
| Carey | C2 | major | fixed | Restored "though still inadequate" (p. 19) |
| Carey | C3 | major | fixed | Quoted spans cut from 153 to 12 source quotations. Word mentions now in italics; the rest paraphrased |
| Carey | C4 | major | fixed | Prerequisites rewritten; glosses for phatic communion, terministic systems, metaphysical, operant conditioning, deep structures, functionalism, uses and gratifications, dissonance/balance theory and fiduciary. Galilean paradigm, scientific realism and the Chicago School are explained in context |
| Carey | C5 | minor | fixed | First Dynasty → telegraph is now the span of linked transport and communication (p. 12) |
| Carey | C6 | minor | fixed | Spring: harvest *because* thought travels by steam and wire (p. 13) |
| Carey | C7 | minor | fixed | One points to the **blueprint** (p. 23) |
| Carey | C8 | minor | fixed | "worry" → "social interest" (p. 26) |
| Carey | C9 | minor | fixed | "Carey suggests, in contrast" (p. 22) |
| Carey | C10 | minor | fixed | Fish/water image credited to McLuhan (p. 19) |
| Carey | C11 | minor | fixed | The models create motives "through policy and program" (p. 25) |
| Carey | C12 | minor | fixed | Added L3 line "less an analysis than a contribution to the chaos of modern culture" (p. 27) to support L1 |
| Carey | C13 | minor | fixed | Removed the metadata date from Reading notes |
| Carey | C14 | minor | fixed | Dropped the percentages from the toy |
| Apperly | A1 | critical | fixed | "do not take close proximity to be **necessary** for having a belief" (p. 17) |
| Apperly | A2 | critical | fixed | L1: "The authors think both camps … are mistaken" (p. 7) |
| Apperly | A3 | major | fixed | Prerequisites gloss executive function and working memory; inline glosses for parsimony, conservation, habituation, preferential looking, analogue system, parallel individuation/object files, central process, quantifier, modes of presentation, level-1/level-2 perspective-taking |
| Apperly | A4 | minor | fixed | "Four puzzles" → "Contrasting findings" |
| Apperly | A5 | minor | fixed | L0 keeps "may be best explained" (p. 2) |
| Apperly | A6 | minor | fixed | L1/L2: "one or more systems … analogues in some animals" (pp. 11–12) |
| Apperly | A7 | minor | fixed | L2: "see and believe" for both species (p. 19) |
| Apperly | A8 | minor | fixed | 5–8 months applies to all four abilities (p. 8) |
| Apperly | A9 | minor | fixed | Added 15 months and "may correlate" (p. 6) |
| Apperly | A10 | minor | fixed | Toy limit now names a quantifier ("no") |
| Axler | A1 | minor | fixed | "Suppose $V$ is finite-dimensional" added to 5.31 and 5.32 |
| Axler | A2 | minor | fixed | "roots of rational numbers" (p. 147) |
| Axler | A3 | minor | fixed | 5A.13 and 5B.8 descriptions no longer give away the answers |
| Axler | A4 | minor | fixed | Q1 reworded to the p. 132 promise; Q3 now has "dimension at least two" |
| Axler | A5 | minor | not fixed | Coverage pointers (Ex. 16 comment, Ex. 8B.23/9C.10) would be additions, not one-line wording changes |
| Cover | C1 | major | fixed | (8.66)–(8.68) transcribed from the p. 200 image; false "partly legible" Reading note corrected |
| Cover | C2 | minor | fixed | L2: concavity gives local = global; finiteness comes from the bounds (p. 191) |
| Cover | C3 | minor | fixed | Identity marked "(added step)" |
| Cover | C4 | minor | fixed | Concepts line has the row-permutation condition |
| Cover | C5 | minor | partly fixed | Garbled L2 residue fixed. The omitted p. 186 and p. 198 sentences were not added (coverage additions, not wording) |
| Blei | B1 | major | fixed | Glosses: ergodic Markov chain, stationary distribution, HMC/NUTS, Markov blanket, held-out log predictive, symmetrized KL; Prerequisites add Markov chains |
| Blei | B2 | minor | fixed | Added the authors' general caveat (pp. 1–2) |
| Blei | B3 | minor | fixed | 20/28/35/50 are now called Fig. 3 snapshot panels; the image shows the ELBO flat by about iteration 45 |
| Blei | B4 | minor | fixed | Eq. (15) cited p. 7 |
| Ashby | S1 | critical | fixed | Photographer condition restored ("if all the negatives are to be brought to a uniform density and sharpness", pp. 212–213), in L3 and the instance line |
| Ashby | S2 | critical | fixed | "±10°" (image p. 217) |
| Ashby | S3 | major | fixed | Biology/two-forms passage and L2 bullet now cite p. 212 (left half of the spread) |
| Ashby | S4 | major | fixed | "essentially independent" (p. 210) |
| Ashby | S5 | minor | fixed | "17" for η noted as a misprint visible in the image (p. 209) |
| Ashby | S6 | minor | not fixed | Disagree: `law of requisite variety` and `disturbance and noise` are the canon spine's own ids (`canon/control-theory.md`) |
| Ashby | (pdf N) | — | n/a | The Ashby digest already cited printed pages, so no `(pdf N)` was present |
| Achen | A1 | critical | fixed | "seem to be more strongly related to … than to" (p. 107), in L3 and the instance line |
| Achen | A2 | major | fixed | L2 voice-tagged: "seems to save voters"; authors find it less positive. Supporting L3 line added (p. 91) |
| Achen | A3 | major | fixed | "as they probably were in 1992" in L3; instance says "probably" |
| Achen | A4 | major | fixed | "we shall show" in ch. 6, plus "even when perceptions do track real changes" (p. 108) |
| Achen | A5 | minor | fixed | "poses a significant challenge to" (p. 114) |
| Achen | A6 | minor | fixed | "great, and perhaps principal, role" (p. 91) |
| Achen | A7 | minor | fixed | Running-tally condition added to L2 |
| Achen | A8 | minor | fixed | "more or less durable partisan preferences" (p. 99) |
| Achen | A9 | minor | fixed | Half-variance figure attributed to economic fluctuations (p. 97) |
| Achen | A10 | minor | fixed | Mediated evaluations "grounded in" simple ones (p. 95) |
| Achen | A11 | minor | fixed | "much less well" plus the "more serious than previous scholars thought" thesis (p. 93) |
| Achen | A12 | minor | fixed | "simplest explanation" (p. 114) |
| Achen | A13 | minor | fixed | L1 gloss of shirk now follows n. 11, not the "inapt" image |
| Achen | A14 | minor | fixed | Kicking the dog is the authors' metaphor; Key's own term was "displacement of economic resentment" |
| Achen | A15 | minor | fixed | Lenz instance: "surprisingly little evidence" (p. 96) |
| Axelrod | X1 | major | fixed | Added Axelrod's explanation of why nice rules did well (p. 35) |
| Axelrod | X2 | minor | fixed | Retaliation lasted to the end of the illustrative game, not "endless" |
| Axelrod | X3 | minor | fixed | Two REVISED DOWNING submissions plus one modified version (p. 45) |
| Axelrod | X4 | minor | fixed | $w$ glossed and flagged as a ch. 1 parameter not defined in this unit |
| Axelrod | X5 | minor | fixed | "often eventually" (p. 47) |
| Axelrod | X6 | minor | fixed | "tended to be relatively small variations" (pp. 47–48) |
| Axelrod | X7 | minor | fixed | "occasionally fruitful" concession (p. 54) |
| Axelrod | X8 | minor | fixed | Round robin defined as in the source; twin and RANDOM listed as this tournament's extras |
| Axelrod | X9 | minor | fixed | "being American" in place of "nationality" (p. 43) |
| Argyle | R1 | major | fixed | "find evidence that GPT-3 is capable of replicating", voice-tagged (p. 15) |
| Argyle | R2 | minor | fixed | No respondent saw the same texts in both parts; each text rated about 3 times per part (p. 19) |
| Argyle | R3 | minor | fixed | Authors' words "shows" and "both strong" reported, plus the p. 10 "some initial evidence" contrast |
| Argyle | R4 | minor | fixed | Intuition-note sentence flagged as our reading |
| Argyle | R5 | minor | fixed | L1: "the authors report that…" |
| Argyle | R6 | minor | fixed | Gloss now follows the source ("zero-shot learning property") |
| Anderson | N1 | major | fixed | All `(pdf N)` converted to printed pp. 393–396 (numbers visible on the page images); frontmatter and Reading note updated |
| Anderson | N2 | major | fixed | One-way street hedged in L1 and L2 ("may well be no useful parallel … except perhaps … in general", p. 396) |
| Anderson | N3 | major | fixed | Glosses: optical rotating power, homogeneous and isotropic, superconductivity, superfluidity, phase transition, ethology, QED, superposition; Prerequisites mention the bra-ket toy |
| Anderson | N4 | minor | fixed | "which I think is as fundamental" kept in L0 and L3 |
| Anderson | N5 | minor | fixed | "It seems to me", "seems to be identifiable", "In some sense" restored |
| Anderson | N6 | minor | fixed | "in a very deep analogy" for rigidity (L2, L3) |
| Anderson | N7 | minor | fixed | Logic corrected: regular so it can be read out, *but* elements vary |
| Anderson | N8 | minor | fixed | Third inference moved after the N → ∞ nucleus paragraph, as in the source |
| Anderson | N9 | minor | fixed | Sugar instance limited to free molecules |
| Anderson | N10 | minor | fixed | `[[emergence]]` and `[[criticality-phase-transition]]` flagged "(canon link; not stated in this unit)" |

## Notes
- `checks.check()` passes on all 12 digests (format, L1 ≤ 120 words, L2 bullet count, page ranges, no `(pdf N)`). The KaTeX check could not run because `pipeline/katex` has no `node_modules`.
- I did not change suggestions that the reports left unrated, so they are still open: the Cover skip paths, the Anderson toy, Gettier's length, and the Argyle appendix tables.
