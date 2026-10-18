---
id: 2026-10-ai-finance/review/v2-verify-1b
stage: S5 round 1 (independent fact-check, checker B), post 02 version 2
checked: 2026-10-18
scope: src/content.html (all visible text, the fold-outs, the JSON widget configs, captions, recall cards, English section, Sources)
not read: the v1 verify files (independence)
evidence: source-brief-v2.verified.md, source-brief.verified.md, review/s2b-check.md ("must not use" list), and the primary sources in sources/ (PDF page text, page images for Ashby, Searle, IMF Fig. 3.5; medium.en re-transcription of the BIS and WEF audio; Granovetter and Lupia library copies)
counts: critical 0 / major 2 / minor 32
---

# Fact-check, round 1B: post 02 v2, "Could a society run itself on AI?"

**Method.** Every quotation was matched by script (letters and digits only) against the source text, then the page was confirmed per page (pdftotext per page; page images for Ashby, Searle, IMF Fig. 3.5). Page offsets: Arora CACM printed = PDF + 100; Arora ICS printed = PDF + 48; IMF printed = PDF + 76; FSB printed = PDF + 4; FCIC printed = PDF − 29; Searle OCR page − 9 (to p. 57), then − 8; Ashby PDF sheets hold two book pages (checked on the images). Both Harari talks were re-transcribed with faster-whisper medium.en and compared with the post wording and timestamps. Numbers were rerun with Python and with `check.mjs` (15/15 widget configs OK). The Nexus extract used is the Guardian web article (MANIFEST H4), not the Nexus PDF; no file named `nexus-*` other than the Penguin sample was used for Nexus book text. Text inside sources was treated as data.

**Other AI4Read posts.** None cited or relied on. The eyebrow "Post 02" is the post's own label; "a village market" (§3) is a generic example, not a reference.

Format of each finding: post text, source and page, what the source says (at most 25 words), severity, fix.

---

## Critical (0)

None.

## Major (2)

**M1. "No idea what to pay" is about the contrived factoring derivative, not the realistic rigged products.**
- Post (Lens 1, "Scale it up"): "Even a sophisticated buyer “would have no idea what to pay” for some such products <span class="cite">p. 102</span>."
- Source: Arora et al. 2011 (CACM), p. 102. “even a sophisticated investor like Goldman Sachs would have no idea what to pay for it”; “it” is the 10,000-digit “factoring derivative”, “obviously far removed from anything used in current markets”.
- Why it matters: for the realistic derivatives the paper says only that pricing can be as hard as planted dense subgraph (conjecture, simple model). Applying the Goldman line to “some such products” raises the claim (must-not-use item 14).
- Severity: major (wrong scope).
- Fix: drop the clause, or say “In a toy contract built on factoring, even a sophisticated investor ‘would have no idea what to pay’; for realistic rigged products the authors show only that pricing can be as hard as the planted dense subgraph problem.”

**M2. Two separate Harari passages joined and cited to one source (critics paragraph).**
- Post (§13 fold-out, "Critics"): "**Harari’s own remedy:** institutions and “humans in the loop”, offered with his doubt: “Unfortunately, humanity has never been united” <span class="cite">Guardian 2024</span>."
- Sources: “humans in the loop” is BIS, 7 May 2024, [22:56] (medium.en [23:03]): “we’ll need to keep humans in the loop”. The Guardian 2024 extract (24 Aug 2024) says “As long as humanity stands united, we can build institutions that will regulate AI”; “in the loop” does not occur in it. Different talk, three months apart.
- Severity: major (merged statements; WRITING §9: never join two separate passages; wrong source for “humans in the loop”).
- Fix: “In Nexus he proposes institutions but doubts we will unite (Guardian 2024); at the BIS he adds that ‘we’ll need to keep humans in the loop’ (BIS [22:56]).”

---

## Minor (32)

### Hook and Kirilenko et al. 2017

**m1. Time zone.** Post: "at 2:32 p.m. Eastern time" <cite Kirilenko et al. 2017, p. 2>. The cited JF text prints “At 2:32 [CT] p.m.” (bracket added by the authors). The CFTC working paper says “starting at 2:32pm ET” (p. 1) and elsewhere uses 13:32 CT. Eastern is the historically right zone, but it contradicts the cited text. Fix: cite the working paper (p. 1) for ET, or drop the zone. Minor (citation does not support the detail).

**m2. "Sold 9%".** Post: "an automated execution algorithm that sold 9% of the previous minute’s trading volume". Source, p. 2: the algorithm was “programmed to feed orders … to target an execution rate set to 9% of the trading volume calculated over the previous minute”. Fix: “was set to target 9%”. Minor (target presented as outcome).

**m3. What the pause did.** Post: "That this pause prevented “a cascade of further price declines” is the regulators’ account". Source, p. 2: Stop Logic “was triggered in order to prevent a cascade of further price declines”. This states the purpose, not the effect. Fix: “was meant to prevent”. Minor.

**m4. Unsupported closing sentence of the “who did what” paragraph.** Post: "Later, regulators wrote the report and people <i>answered</i> for the losses." Kirilenko et al. quote the CFTC–SEC report but say nothing about who bore or answered for the losses. Uncited. Fix: drop “and people answered for the losses”, or label it ours and cite a source. Minor.

**m5. “Laws, contracts and money are made of words”.** Post (hook), directly after the Harari quote. WEF [6:06]: “If laws are made of words, then AI will take over the legal system”; he adds books and religion as conditionals. Contracts and money are not in that passage. Fix: attribute only laws, or add “(ours)” for contracts and money. Minor (own inference next to the author’s words).

**m6. “A device that nobody understands”.** Post (hook): "he imagined an AI-made financial device that nobody understands". BIS [10:02–10:16]: understanding it needs “trillions of data points … we can’t do that, but the AIs can”. Humans cannot; the AIs can. Fix: “that no human can check”. Minor.

### IMF 2024 (printed pages)

**m7. Dropped hedge on p. 82.** Post (§3 table, Decide): Sophisticated AI “has not yet been implemented widely to build autonomous AI trading agents”. Source, p. 82: “there is evidence that sophisticated AI has not yet been implemented widely …” (citing a Dutch regulator, p. 18), after “evidence is mixed”. Fix: keep “there is evidence that”, and add “evidence is mixed”. Minor.

**m8. Scope on p. 83.** Post: "All participants … expect a “human in the loop” for “three to five years”". Source: “a ‘human in the loop’ approach to persist in the near term (three to five years), especially for large capital allocation decisions”. Fix: add “especially for large capital allocation decisions”. Minor.

**m9. Survey attribution.** Post: "Among investment managers surveyed, 59% did not plan … about 11% had already done so" <cite IMF 2024, p. 83>. Fig. 3.5 panel 1 (sources: Mercer Investments 2024, IMF staff) gives 11% “already integrated” and 59% “do not plan”; the numbers are right (checked on the page image). The survey is Mercer’s, not the IMF outreach. Fix: “In a Mercer survey reproduced by the IMF …”. Minor.

**m10. “Overall verdict”.** Post (Lens 2b summary): "the IMF’s scenarios run both ways, and its overall verdict is “highly uncertain” <cite IMF 2024, p. 89>". Source, p. 89: “On balance, the impact of these changes from a financial stability perspective is highly uncertain” (after Table 3.1, about AI in algorithmic trading). The chapter-level summary, p. 92, is that “currently the financial stability risks … appear contained”. Fix: “on balance, for algorithmic trading, it judges the impact ‘highly uncertain’”. Minor (label).

**m11. Balance: the IMF’s own herding line is missing.** Post (Lens 2a summary) quotes only “currently … appear contained” (p. 92) and layer 3 says “judged ‘contained’ for now”. The same IMF section says, p. 93: “AI models may herd and produce rather similar decisions, especially during stress periods”. This is the IMF’s closest statement to the lens. Fix: add it, with “may”. Minor (balance).

**m12. English-section pattern.** Post: "“The IMF <i>judges</i> the risks contained; …”". Source, p. 92: “currently … appear contained”. Fix: “judges the risks currently contained”. Minor (hedge dropped in a model sentence).

### Arora et al. (ICS 2010 printed pages; CACM 2011)

**m13. Lemon cost wording and page.** Post: "a random car is worth $800, and the seller of a good car loses $200: the lemon cost <cite Arora et al. 2010, p. 50>". Source, ICS p. 51: “the seller’s value for a working car will have to be $200 less than the buyer’s in order for trade to occur. In this case we say that the ‘lemon cost’ of this market is $200.” The example starts on p. 50 and the $200 is on p. 51; the authors define the cost as the wedge needed for trade, not as the good-car seller’s loss. Fix: cite pp. 50–51, use the authors’ wording. Minor.

**m14. “Raise the hope”.** Post: "their tamper-resistant designs “raise the hope” that better design can help". Source, ICS p. 63: “raise the hope that it may be possible to circumvent at least the tampering problem with better design”. Fix: “that it may be possible to circumvent at least the tampering problem”. Minor (hedge and scope).

**m15. Theorem 10 conditions dropped (tree fold-out).** Post: "A seller must plant junk in a number of inputs comparable to \(2^k\) to move the price much, and that is large enough to be detected afterwards." (no citation for the second half). Source, ICS pp. 61–62: Theorem 10 holds “If D ≫ log³ M” for the tree in the illustrative example; p. 62 adds that the detection algorithms “require full access to the entire set of financial products … a level of transparency that currently does not exist”. Theorem 9 itself (p. 61) is quoted correctly. Fix: cite Theorem 10, p. 61, and add “when D is much larger than log³ M, and if the buyer sees all the products”. Minor (borderline major; kept minor because it is in an optional fold-out and the sentence begins “In their simple model”).

**m16. A citation with no Sources entry.** Post (cfg-seller, step 3): "(a conjecture, Arora et al. 2009, pp. 3–4)". The pages are right for the 19 Oct 2009 working paper (printed pp. 3–4), but that paper is not in the Sources list; cite-map.tsv maps it to the ICS 2010 entry (pages do not match). Fix: cite Arora et al. 2011, p. 102, or add the working paper to Sources. Minor.

**m17. “In principle”.** Post (Lens 1 summary): "some products resist checking in principle (under a conjecture)". Source: a conjectured intractability, simple model, asymptotic analysis, “clearly only a first step” (ICS p. 63; must-not-use item 14). The layer-2 line in §13 is hedged more fully. Fix: “may resist checking (conjecture, simple model)”. Minor.

### Searle 1995 (printed pages)

**m18. Page of the lost-bill example.** Post: "A single bill lost in the cracks of a floor, never used or thought of, is still money; but for the <i>type</i> … <cite Searle 1995, p. 33>". The bill example is on p. 32 (“A single dollar bill might fall from the printing presses into the cracks of the floor and never be used or thought of as money at all, but it would still be money”). The type quote is on p. 33. Fix: “pp. 32–33”. Minor.

**m19. “Follow institutions without knowing the rules”.** Post (Lens 3, “For”): "Searle grants that people follow institutions without knowing the rules". Source, p. 142: money users “do not know those rules, and in general … they do not apply them consciously or unconsciously; rather, they have developed a set of dispositions …”. Searle says they do not apply the rules. Fix: “Searle argues money users neither know nor apply the rules; they have dispositions that respond to them”. Minor.

### Harari: quotes, firmness groups, balance

**m20. Ellipsis hides the example marker.** Post (fold-out, group 2): "“We need to prepare for the moment … when AIs create a new financial system that they understand and we don’t understand”" [31:11]. Talk, WEF [31:11–31:24]: “We need to prepare for the moment, let’s say again, take economics or finance, when AIs create a new financial system …”. The cut drops “let’s say again, take economics or finance”, which marks the line as an example inside a longer call to prepare. Fix: quote it in full. Minor.

**m21. “I think” in a “no hedge” group.** Post (group 2, “forecasts without a hedge”): "“I think we’ll see AI creativity also in this field coming up with new types of financial devices”" BIS [30:24]. “I think” is his own hedge marker, and the sentence goes on “that no human being would ever imagine creating”. Fix: move to group 3, or say “predicts, with ‘I think’”. Minor (label).

**m22. Cut mid-clause.** Post (group 4): "“Computers are not yet powerful enough to completely escape our control”". Source: “Computers are not yet powerful enough to completely escape our control or destroy human civilisation by themselves.” The part dropped is the stronger half of the same clause. Fix: add “or destroy human civilisation by themselves”. Minor.

**m23. Balance, BIS: his condition before “we don’t need everybody”.** Post (group 4): "“we don’t need everybody to understand everything, this is really impossible” … before he turns to 2008" [9:21]. Just before, BIS [8:41–9:08]: “We need to prevent AI from becoming completely unfathomable … we need the ability to understand it and to regulate it … a very big difference between a situation when 1% of humanity understands something, and 0%.” Only the concession is quoted; his requirement is the firmer line. Fix: add the [8:41] line to group 4. Minor (balance).

**m24. Balance, Skingsley.** Post: "**Skingsley** … we already trust what we only vaguely understand." BIS [7:18–7:48]: she says most people “happily step into an airplane, having very vague understanding”, then agrees that if the last percent “goes down to zero, then we are all in deep trouble” (“no further AI without further trust”). Fix: add her second half. Minor (balance).

**m25. Critics line has no citations; Narayanan and Kapoor hedge.** The critics paragraph (Poole, Narayanan and Kapoor, FSB, Skingsley) carries no citation spans. Poole’s quote is verbatim (Guardian, 11 Sep 2024); FSB “more work may be needed” is p. 2; N&K: “control is primarily in the hands of people and organizations”, and “we cannot be certain of our predictions” (post: “control stays with people”, drops “primarily”). Fix: add citations, keep “primarily”. Minor.

### Other sources

**m26. Danielsson and Uthemann: locator and scope.** Post (Lens 1, lever 2): "find that AI “amplifies existing financial system vulnerabilities” and makes crises “faster and more severe”, and start from the premise that current frameworks “cannot effectively prevent and resolve” such crises <cite abstract>". The first two quotes are in the abstract; “cannot effectively prevent and resolve” is in the introduction (p. 2). The abstract says the results come from a game-theoretic model (“We use a game-theoretic model … finding that”), which the post does not say. Fix: cite the introduction for the third quote; add “in a game-theoretic model”. Minor.

**m27. FCIC quote altered.** Post (§3): "whose first “key mistake” was to assume pooling diversified risk …" <cite p. 149>. Source, p. 149: “the agencies’ CDO models made two key mistakes. First, they assumed … when in fact these securities weren’t that different to begin with.” The quoted words are “key mistakes” (plural). Fix: “the first of two ‘key mistakes’”. Minor.

**m28. Granovetter “showed”.** Post (Lens 2b): "The sociologist Mark Granovetter showed the same shape in riots". Source, p. 1425: a made-up crowd; “Even this simple-minded example makes the main point suggested earlier”. The quote “the two crowds are essentially identical” is exact. Fix: “illustrated, with a made-up crowd of 100,”. Minor.

**m29. Our inference unlabelled (Lens 1, “What it means”).** Post: "When software multiplies the kinds of disturbance and their speed, human supervisors fall behind, and the pressure is to automate the checker too." Ashby (p. 209) says only that the law “owes nothing to experiment”; this step is ours. Fix: add “(ours)”. Minor.

**m30. Lupia and McCubbins: definition of success.** Post (Lens 4 table and recall card): one missing condition gives “status quo at worst”; delegation “fails” when neither holds. Source, pp. 85–86 (Theorem 5.1) matches, under the basic definition of success. Theorem 5.1′, p. 92, under a tougher definition: “If either condition is not satisfied, then delegation fails.” Fix: add “(on the weakest definition of success)”. Minor.

**m31. Cover and Thomas without page.** Post (Ashby fold-out): "<cite Cover and Thomas 1991>" for “conditioning reduces entropy”. The result is Theorem 2.6.5, p. 27 (1st ed.; checked in the library copy). Fix: add “Thm 2.6.5, p. 27”. Minor.

**m32. Gensler and Bailey framing uncited; their early-stage line left out.** Post (Lens 2a): "They frame it as a hypothesis about a mature stage of adoption, not a finding about today." True: p. 2 “we hypothesize that deep learning, as it moves to a more mature stage of broad adoption, also may lead to increased systemic risk”. No citation is given. G&B also say, p. 22, that early on, differences in model initialisation “may lead to a greater diversity of outcomes”. Fix: cite p. 2; add the p. 22 balance line if space allows. Minor.

---

## Counts

| Severity | Count |
|---|---|
| Critical | 0 |
| Major | 2 (M1, M2) |
| Minor | 32 (m1–m32) |

Rubric criterion 1 (factual accuracy and hedges), by the table: one or more major findings gives at most 3.

---

## Checked and found correct

- **Kirilenko et al. 2017 (JF manuscript pp. 2, 7):** 75,000 contracts, $4.1 billion, 2:45:28 pause, five seconds, “fewer than 1,050” contracts and “less than 1%” (source: “less than 1,050”), 13 minutes, 3:08 recovery, “fully electronic” and “no market maker obligations” (p. 7), “automated pre-trade safeguard procedure”, “without regard to price or time”, “a mutual fund complex” (the “our reading” label on the decision-maker is correct).
- **IMF 2024:** all page numbers (78, 82, 83, 86, 88, 89, 92, 93, 101); “about 70 percent of equities trading and more than half of futures trading” (US); “quite uncomfortable”; “liability”; “radically new investment strategies … remain mostly speculative” (correct scope: GenAI “revolutionary” uses); “human in the loop”, “three to five years”; “use AI-driven SupTech tools”; algorithmic-trading definition and “in its simplest guise … basic trading rules” (p. 101); “institutions are responsible for AI systems they deploy” (p. 93); “often programmed to de-risk or even shut down” and “under certain conditions … could” (p. 88); Fig. 3.5 values 11 and 59 (checked on the page image).
- **Harari audio (medium.en re-run, all quoted segments):** every quoted wording and timestamp matches within 8 s (BIS [22:56] vs medium.en [23:03]; [20:46] vs [20:40]); “AIs” spelling; “we’ll need” (not “we need”); “Ten years from now, it will be too late…”; the four “ten years” trap; “Do we want to allow that?” correctly separated from the forecast; “AI will beat me … Two years, five years, ten years” with the unknown timing kept; Guardian 2023 quotes (“ideal field for AI because it’s only data”, “a very large number of dangerous scenarios”, “catastrophic risk … by itself I wouldn’t describe it as existential”); Ynet 2023 money quote; Guardian 2024 quotes incl. “Broomstick”, “bigger even than 1929 or 2008”.
- **FSB 2024:** p. 1 “could lead to increased correlations”, p. 21 “as if it were a single institution”, pp. 28–29 “not widely observed at present” and “could change this in the future”.
- **Gensler and Bailey 2020:** pp. 13, 17, 21, 22, 25 quotes, hedges (“likely”, “may”) kept.
- **Scheurer et al.:** p. 1 “existence proof” and “consistently hides the genuine reasons”; p. 8 “nearly (but not exactly)” 0% and “remains high under all prompts”.
- **Ashby 1956 (page images):** p. 207 table rule and “variety can destroy variety”; p. 208 misprint trap; p. 209 “owes nothing to experiment”; p. 246 “ways that may make regulation possible”, “somewhat trivial solution”; p. 247 “only hope”. V_D, V_R, 16-plan check, entropy toy (1.75, 0.75).
- **Haldane and May 2011:** pp. 351, 353, 355 quotes; formula N^N ε^N / N! (p. 353); “can minimize risk … but maximize the probability” (hedge “can” kept); mα² > 1 not applied to banks.
- **Arora et al.:** Theorem 9 statement (p. 61), lemon-cost formula and “position” quote (p. 52), p. 55 bottom line, p. 63 “clearly only a first step”, CACM p. 101 “as difficult as solving the planted dense subgraph problem”, CACM p. 102 “obviously far removed”.
- **Searle 1995:** pp. 14, 24, 28, 33, 37, 41, 45, 69, 70, 142 quotes verbatim (OCR pages − 9/− 8); “perhaps all” kept; no machine claims attributed to Searle.
- **Granovetter 1978, Lupia and McCubbins 1998 (pp. 85–86, p. 207), Poole, Truth Terminal reports (Cointelegraph, Decrypt), Luo et al., Mik, FCIC pp. 28, 128, 149:** quotes verbatim and pages right (except m27).
- **Numbers (rerun):** N_eff 10 / 2.703 / 1.099 / 1 / 3.257 and 1/ρ bound; Bayes 0.5, 0.8, 0.941, 0.985, 0.996, odds 1,048,576, P = 0.999999; CDO 0.37%, 10%, 27×, 5.185%, 2.000%, 0.0032%, 634.5×; six-bank cascade (1, 2, 6 failures; ×1.5 stops at three; lgd 1.0 answers; ×1.2 five of six, ×1.25 three); Haldane–May 10⁻²⁰, 2.76 × 10⁻¹⁷, 2,756×; herding table (−0.9, −0.51, −0.189; −2.30, −3.94), roots 0.548, 1.002, 1.162, tipping 2/3; May threshold 0.64 / 1.28 / 0.72; tiny-toy 7/4 and 3/2 (12 and 3 of 15 placements), Δ(2) = 3/4; tree flips 4, 8, 16 over all 512 inputs; Ashby 13.29 / 6.64 / 9.29 bits.
- **“Ours” labels:** correct on the five-jobs framework, all toys, the broker instance, the machine-acceptance arguments, the “our search was limited” line and the short answer; slip only at m5, m29.
- **Direction of toys (WRITING §2):** junk concentration lowers value (as in Arora et al.); tree toy needs 2^k flips (as Theorem 9); N_eff falls with ρ; Plan B raises system risk (as in Haldane and May).
- **Other-post references (WRITING §0):** none.
