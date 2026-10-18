---
id: 2026-10-ai-finance/review/s2b-check
stage: S2b, independent fact-check of source-brief-v2-additions.md (post 02 v2)
date: 2026-10-18
checked_against: sources/ files only (kirilenko-2017-flashcrash-jf, imf-2024-gfsr-ch3, gensler-bailey-2020-deeplearning, arora-2011-cacm (= ICS 2010), arora-2011-cacm-authorcopy (2009 WP, for the comparisons), kirilenko-cftc-flashcrash (2014 WP, for trap 32), haldane-may-2011-nature, searle-1995-construction, guardian-2024-nexus-extract, nexus-penguin-sample, mitsloan article (trap 39))
method: every quote matched by script against a fresh pdftotext extraction (letters and digits only), page by page, then compared with the stated page; partial matches read by hand. Images viewed: IMF pp. 83, 86 (Fig 3.5, 3.8); Haldane–May p. 351; Kirilenko p. 2; Searle printed pp. 14, 22, 24, 25, 27, 28, 33, 34, 37, 41, 42, 43, 45, 47, 48, 51, 55, 56, 69, 70, 96, 100, 111, 117, 118, 141, 142. Numbers rerun in Python. V6a–V6e not checked (WITHDRAWN; the deleted file was not looked for or used).
output: source-brief-v2.verified.md
---

# S2b check: source brief v2 additions

Severity follows rubric §A. "S2b fix" = what the verified brief now says.

## Per unit

| Unit | Verdict | Evidence | Change |
|---|---|---|---|
| Header / offsets table | FIXED | Searle running heads: PDF 23 = p. 14, 66 = p. 57, 67 = p. 59 (ch. 3 opener), 118 = p. 110, 149 = p. 141. No PDF page carries printed p. 58. No `ocr-searle/` folder exists; OCR is the combined `.txt` with page headers. IMF +76, Arora +48, H&M +350, KKST 0, G&B 0 all confirmed on footers. | Offset rule confirmed; p. 58 noted as absent; OCR path corrected; *Nexus* row struck out (minor, housekeeping). |
| Trap 32 | OK | JF text has no "contributed", "36 minutes", "shake the confidence", "cascade into", pause recommendation; all present in kirilenko-cftc-flashcrash.txt (lines 13, 83, 119, 155, 247). | none |
| Trap 33 | OK | p. 2 image: "At 2:32 [CT] p.m."; p. 22 windows 13:32:00–14:08:00 CT. | none |
| Trap 34 | OK | 13:32→14:08 = 36 min; JF never says "36 minutes". | none |
| Trap 35 | FIXED (minor) | p. 2: "a large fundamental trader (a mutual fund complex) initiated a sell program"; "This large fundamental trader chose to execute…". Nothing says a human decided. | "(people)" → a firm; "a person decided" labelled ours. |
| Trap 36 | OK | p. 101 glossary; p. 102 HFT sentence. | none |
| Trap 37 | FIXED (minor) | p. 86 text gives two numbers: "about 70 percent of equities trading and more than half of futures trading". Fig 3.8 image: equities ≈67, futures ≈52, options ≈44, FX ≈27, FI ≈8; regions 68/50/42/30; Euronext top ≈28, top-10 ≈89. | "the one number … US equities only" corrected. |
| Trap 38 | FIXED (minor) | p. 98: answers were "tabulated"; 27 stakeholders; 10 supervisors. | "qualitative" → "an outreach, not a representative survey". |
| Trap 39 | OK | "who's at fault" only in mitsloan txt line 55; G&B uses "mask" only for black boxes / bias (lines 171, 526). | none |
| Trap 40 | OK | G&B p. 22 "It is hypothesized…"; KKST abstract/p. 6 "did not change". | none |
| Trap 41 | OK | md5 of arora-2011-cacm.pdf = arora-ics2010.pdf = 460f8a74fde8d182a92346b791604300. | none |
| Trap 42 | OK | p. 351 image. | none |
| Trap 43 | OK | text layer "ma2 . 1", "(6) a"; image "mα² > 1", "(±) α". | none |
| Trap 44 | WITHDRAWN | rests on the deleted file. | struck. |
| Trap 45 | FIXED (part of C1) | "made of words": no hit in nexus-penguin-sample (raw and txt) or guardian extract. Full book UNSEEN. | "not in *Nexus*" → "not in the citable *Nexus* texts; it is Davos 2026". |
| Trap 46 | WITHDRAWN | rests on the deleted file. | struck. |
| Trap 47 | WITHDRAWN in part | evidence from the deleted file. | keep only "any Harari–Searle comparison is ours". |
| Trap 48 | OK | OCR regex: robot / artificial intelligence / Chinese room / strong AI = 0 hits; "Turing" = 2 OCR false positives (in "capturing", "picturing"); "computer" on pp. 14, 34, 56, 84, 140, 168, endnote, acknowledgements. | note added. |
| Trap 49 | FIXED (Harari half withdrawn) | IMF Fig 3.8 FX ≈27% confirmed on image; Harari 90% from deleted file. | Harari number removed. |
| Trap 50 | OK | p. 32 (bill in the cracks), p. 33 ("the belief that the type is a type of money is constitutive"), p. 53 (codification). | "exact answer" softened; p. 33 quote added. |
| V1 Kirilenko et al. 2017 | FIXED (minor ×2) | All 7 quotes verbatim on stated pages (pp. 2, 3, 7, 19, 28). Numbers verified on pp. 2–3, 5, 13–14, 17–19, 22–24, 28: 75,000; $4.1bn; 9%; 35,000/$1.9bn; <1,050 (<1%); 2:45:28–2:45:33; 6 pts/24 ticks; >20,000 trades, >300 securities, 60%; 3:08; 16 HFT / 189 MM / >15,000; 4,000 / 1,500 / 6,000; 33,944; 34.22→28.57%, 10.49→9.00%; 17% of a tick (p. 24); F-test 1% (p. 23). | (a) fn 3 quote: "based in part on the preliminary analysis **contained** in the original version of this paper" (the brief dropped "contained"); (b) "Decide was human" → decided by the firm; human is our reading. Also noted "15 HFTs on average" active (p. 17) and "did not significantly alter" (p. 28). |
| V2 IMF GFSR ch. 3 | FIXED (1 major, 6 minor) | See findings M1, m3–m9. Fig 3.5 image: Executing 11/11/15/4/59, Allocating 10/9/12/10/59 (sum 100); Dutch ML shares ≈88/33/11. Verified on page: p. 77 "AI may actually reduce…"; p. 78 fn 1, "human in the loop", "indicative evidence"; p. 82 fn 8 (80–100%); p. 83 three-to-five years, agent-to-agent; p. 86 70%, NBFIs "over half"; p. 87; p. 88 (235 stocks, "flighty", "same measures"); p. 89 Table 3.1, "highly uncertain", FOMC 45 s (15/15 events, p. 90 note), ETFs; p. 92 "appear contained"; p. 93 herd, shutdown, responsible, clearing houses; p. 95 26 authorities, fn 24; p. 96 circuit breakers, large traders; p. 97 OTC; p. 98 Box 3.1. | p. 78 scope fixed (major); signal quote moved to p. 82; "especially pertinent if…" requoted; collusion/winner-takes-all reattributed (pp. 89, 91); "under certain conditions" restored; critical-providers quote p. 96; SupTech ≠ AI; "indicative" located on p. 78. |
| V3 Gensler & Bailey 2020 | FIXED (minor ×2, + long quote) | All 8 quotes verbatim on stated pages (pp. 9, 12, 13, 17, 21, 22, 25, 26). Structure (9 characteristics, 3 channels, 5 pathways) p. 3; Aladdin/Venn/OpenAI p. 23; SR 11-7, TRIM, E-23 p. 28; war games p. 31; kill switches p. 32. | "not be sufficient" is p. 28 (and p. 4), not p. 32; "mono-models" pp. 4, 25; Khandani–Lo instance keeps "As hypothesized by"; 38-word p. 17 quote split; SSRN number on the file is 3766555 (MANIFEST says 3723132). |
| V4 Arora et al., ICS 2010 | FIXED (minor) | All 10 quotes verbatim on stated pages (pp. 49, 50, 55, 56, 60, 63). Theorems 1, 3 (pp. 53–54), 7–8 (p. 60), 9–10 (p. 61); bound (1 + t/2^k)/2; F = TM^k ∧ Threshold(0.4·3^k); CoC = Ω̃(n√(N/M)) p. 59; random pooling n → o(n), √D over-representation p. 55; lemon law p. 51 / §5.1 p. 59. WP comparisons confirmed in the 2009 WP text (lines 20, 140, 639–651). | Car example is pp. 50–51 ($1000, 20% on p. 50); 27-word "faulty models" sentence no longer quoted whole. |
| V5 Haldane & May 2011 | FIXED (minor, + long quotes) | p. 351 image: "for N ≫ 1 this transition occurs once mα² > 1 … and (±) α their average strength⁴". All 7 Quotes-list items verbatim. n* = 4.14; "factor of three"; "perhaps as much as two-thirds"; $25 trillion; Volcker rule; Royal Commission. Python: ε=0.01 → N=6: ratio 64.8; N=10: 1e-20 vs 2.7557e-17, ratio 2,755.7; N=20: 4.31e7; Stirling e^N/√(2πN) = 65.7, 2,778.8, 4.33e7. | Caccioli: "as n approaches n*, there is a sharp singularity" (brief: "once n passes"); "random sign" labelled our gloss; four quotes over 25 words trimmed/split (pp. 351 ×2, 353 ×2); hedge-fund line requoted. |
| V6a–V6e Harari *Nexus* | WITHDRAWN | not checked (instruction; pirate source deleted). | replaced by a stub; all cross-references removed (see C1). |
| V7 header | FIXED (minor) | see header row. | p. 58 absent; p. 142 read; Korean example is p. 89. |
| V7a Collective intentionality | OK | pp. 23, 24, 25, 26, 37, 38, 40 fn, 69, 70 verbatim (images 24, 25, 37, 69, 70). | Added p. 70 "Animals running in a pack can have all the consciousness and collective intentionality they need" (the barrier is deontic representation). |
| V7b Assignment of function | FIXED (minor) | p. 22 image: "money may simply have evolved without anyone ever thinking". | Quote word order fixed; added p. 22 "At least some of the participants … must understand, consciously or unconsciously, that money is to buy things with". |
| V7c Status functions | FIXED (minor) | p. 109: "roughly speaking, everything turns out to be deontic"; p. 47 image (limit on statuses); pp. 28, 41, 44, 51, 80, 82–83, 100, 110–111 verbatim (images 28, 41, 51, 100, 111). | Hedge "roughly speaking" restored; p. 96 honorific exception noted. |
| V7d Brute vs institutional | OK | pp. 27, 33, 34, 35, 55, 56, 69 verbatim (images 27, 33, 34, 55, 56, 69). | none |
| V7e Money | FIXED (minor ×2) | p. 46: "Anything that satisfies these conditions (X term) counts as money, i.e., U.S. paper currency (Y term)"; p. 42 image: "I am using the account only to illustrate certain logical relations". pp. 32–33, 41–43, 45, 47, 48, 53, 55 verbatim. | Y term is money (U.S. paper currency), not "legal tender"; medieval story p. 42–43; p. 47 "As long as people continue to recognize…" added. |
| V7f Continued acceptance | FIXED (minor) | p. 118 image: "where consent is essential, a great deal of pomp, ceremony, and razzmatazz…"; "Jails find these devices less necessary because they have brute force." pp. 45, 50, 96, 117, 118 verbatim. | "he concedes force can do the work" relabelled as our reading; p. 96 "aware" scoped to the mechanism. |
| V7g Background | OK (+ addition) | p. 140 "I am not satisfied with either"; p. 141 image: connectionism sentence and the "causally sensitive … without actually containing any beliefs or desires or representations of those rules" sentence. | Added p. 142 [img]: money users "do not know those rules" and, "in general, I am arguing", "do not apply them consciously or unconsciously" (balance: the strongest passage for rule-following without represented rules). |
| V7 Careful (overall) | FIXED (major, M2) | p. 69: "The status exists only if people believe it exists"; p. 33: "the belief that the type is a type of money is constitutive of its being money"; p. 47: participants think "This is money" but need not think about the imposing; p. 96: "regardless of whatever false beliefs" (beliefs about *why*). | "the bar is lower than 'belief'" deleted and replaced. |
| V8 Job-by-job table | FIXED (C1, M1, m2, m8) | Harari cells cited "PDF 227 / 292–293 / 333 / 339 / 345" (deleted file). IMF p. 78 scope (M1); IMF p. 83 → p. 82 for the signal line; SupTech 79% is not AI; KKST "person's decision" is our reading. | All Harari cells removed; Check row uses the Guardian-extract line with its turn ("Unfortunately, humanity has never been united"); "human institution ends the regress" labelled OURS. |
| Challenges 1–10 | FIXED | 1: OK (pages added). 2: OK. 3: SupTech scope; Harari PDF 339 removed. 4: major (M2) and Harari V6c removed. 5: Harari PDF 295 removed. 6–8: OK (pause untested in JF, p. 2; 36 min ours; mα² ecology only; Arora hedges p. 63). 9: withdrawn as written. 10: Harari 90% withdrawn. | rewritten in the verified file. |

## Findings by severity

**Critical (1)**
- **C1. Live citations to the withdrawn *Nexus* file.** The brief withdraws V6a–V6e at the top, but V8 (Run: "more than 90 percent", PDF 227; Check: "no purely technological solution", PDF 339; Declare: PDF 292–293; Answer: PDF 333, 345), traps 44–47 and 49, and challenges 3, 4, 5, 9 and 10 still cite it by PDF page. A writer following V8 or the challenges would cite an unverifiable pirate source. Fix: all removed or marked WITHDRAWN; the Check row now uses the Guardian extract ("As long as humanity stands united, we can build institutions that will regulate AI" + "Unfortunately, humanity has never been united"), and "a human institution ends the regress" is labelled ours.

**Major (2)**
- **M1. IMF p. 78, "mostly speculative" given the wrong subject** (V2 Humans-in-the-loop bullet; V8 Decide row). Brief: autonomous AI "generating and executing trades without human oversight" is "mostly speculative". Source (p. 78): "The more ‘revolutionary’ uses of GenAI—radically new investment strategies and processes using cutting-edge AI technology—remain mostly speculative." Autonomous trading is what "many observers envision"; participants are "quite uncomfortable with this idea". Fix: separate the two sentences; the first is a direct IMF statement on the post's own question (AI-invented strategies).
- **M2. Searle's bar for acceptance presented as "lower than belief"** (V7 Careful; Challenge 4). Source: "The status exists only if people believe it exists" (p. 69); "the belief that the type is a type of money is constitutive of its being money" (p. 33); unawareness on pp. 47 and 96 is about the mechanism, not the status (people think "This is money", p. 47). Our inference contradicted the author and was used against the card's thesis. Fix: replaced; the balancing passage that *does* exist (pp. 141–142, rules not represented) added.

**Minor (20)**
1. V1 fn 3 quote missing "contained" (p. 5).
2. V1 / trap 35 / V8: "a person decided" stated as fact; source says a mutual fund complex (p. 2).
3. V2 signal quote cited p. 83; it is p. 82 (also V8).
4. V2 "especially if trading…" not verbatim; source "especially pertinent if…" (p. 91).
5. V2 collusion: "winner takes all" attributed to Fan–Pelger–Yu simulations and p. 89; source: "empirical literature … (Baron and others 2017)", p. 91.
6. V2 p. 88 quote drops the hedge "under certain conditions".
7. V2 "capture the systemic use of common AI models" is p. 96, not p. 97.
8. V2 / V8 / Challenge 3: SupTech adoption 79%/54% presented as AI use; fn 24 p. 95 is SupTech in general.
9. V2 traps 37–38 and evidence base: "the one number … US equities only" (also futures), "qualitative" (answers tabulated), "indicative" sited in Box 3.1 (it is p. 78).
10. V3 "not be sufficient" cited p. 32 (it is p. 28, also p. 4); "mono-models" pp. 4, 25, not 22–24.
11. V3 Khandani–Lo instance dropped "As hypothesized by" (p. 22).
12. V4 car example cited p. 51; it begins p. 50.
13. V5 Caccioli et al.: "once n passes n*" vs "as n approaches n*, there is a sharp singularity" (p. 352).
14. V7b quote "simply evolved without…" vs "may simply have evolved without…" (p. 22).
15. V7c dropped "roughly speaking" before "everything turns out to be deontic" (p. 109).
16. V7e Y term given as "legal tender"; p. 46 Y term is "money, i.e., U.S. paper currency".
17. V7e "using … only to illustrate" cited p. 43; it is p. 42.
18. V7f "he concedes that where consent is not essential, force can do the work" is our inference from p. 118.
19. V7 housekeeping: printed p. 58 not in scan; `ocr-searle/` path does not exist; Korean example p. 89.
20. Eight quotes longer than 25 words (V2 p. 82, p. 91; V3 p. 17; V4 p. 63; V5 p. 351 ×2, p. 353 ×2): trimmed or split.

**Counts: critical 1, major 2, minor 20.**

## Balance check
- IMF: both directions present (risks and "AI may actually reduce financial stability risks", p. 77; Table 3.1 positive column; "appear contained", p. 92). Added: the unhedged p. 78 line on "radically new investment strategies" (M1).
- Gensler & Bailey: hedged hypothesis kept; their firmest lines ("will not be sufficient", p. 28; "if deep learning predictions were explainable, they wouldn’t be used in the first place", p. 13) now flagged as the unhedged ones.
- Searle: the brief had his hedges (p. 37 "perhaps all"; pp. 110–111 hypothesis) but softened his firmest requirement (p. 69 belief; p. 22 understanding) in the Careful note (M2). Added both, plus the strongest passage in the other direction (p. 142, users do not know or apply the rules).
- Kirilenko et al., Haldane & May, Arora et al.: hedges intact ("our results suggest", "tentative", "deliberately oversimplified", "only a first step").
- Harari: not assessable from V6 (withdrawn). Only S2 unit A4 sources may be used; WRITING §9 quote-boundary rule applies to the Guardian "humanity stands united … never been united" pair.

## Checked and found correct (not changed)
All V1 quotes and numbers except fn 3; all V3 quotes; all V4 quotes, theorems and bounds; all V5 Quotes-list items and the homogeneity numbers; Fig 3.5 and Fig 3.8 values; IMF 70%, 27 stakeholders, 10 supervisors, 26 authorities, three-to-five years, 45 seconds, 235 stocks, 79/54/50/31; Searle quotes on pp. 14, 23–28, 32–35, 37, 41, 44–48, 51, 53–56, 69–70, 80, 82–83, 96, 100, 110–111, 117–118, 140–141; traps 32–34, 36, 39–43, 48, 50.

## Writer must not use
1. Anything cited to "Nexus PDF n", V6a–V6e or the deleted `harari-2024-nexus.pdf` (incl. "computer-to-computer chains", "inter-computer realities", "cannot ‘believe’", "no purely technological solution", "bots don’t have rights", "more than 90 percent" forex, chapter placements).
2. "The IMF says autonomous AI trading is mostly speculative."
3. "For Searle, acceptance is a lower bar than belief."
4. "Searle says machines cannot be part of the 'we'" (he never discusses it; ours).
5. "'Anything made of words' is not in *Nexus*" (say: it is from Davos 2026).
6. "70% of trading is AI."
7. "79% of supervisors use AI."
8. "A person decided to sell in 2010" without "our reading".
9. "The pause stopped the crash" as the JF's finding; "HFTs contributed to the crash" from the JF (both are the 2014 WP or the CFTC-SEC report).
10. "The IMF's winner-takes-all comes from simulations."
11. "The bill counts as legal tender (Y term)."
12. "Searle concedes force can replace acceptance."
13. Any Haldane–May claim that connectivity always lowers stability, or mα² > 1 applied to banks.
14. "Arora et al. show some products cannot be checked by any realistic checker" (conjecture, simple model, asymptotic, "only a first step").
