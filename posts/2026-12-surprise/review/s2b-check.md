---
id: 2026-12-surprise/review/s2b-check
stage: S2b (addendum to the verified brief)
checker: independent fact-checker (fresh agent)
date: 2026-11-28
input: requests.md items 1–2; outline.md layers 1 and 5 → output: units 16–23 appended to source-brief.verified.md
method: units written from the source pages (Mills OUP 2000 printing; Pierce Harper 1961). 71 quotes and quoted phrases matched by script against the pdftotext page (dashes, quotes, hyphenation normalised); 68 matched. Of the 3 misses, 2 came from OCR or a page break and were read on the page image (U18), and 1 was a wrong page in the script: "quite different" is on Pierce p. 23 (pdf 39), not p. 24, and is cited as p. 23. Page images rendered with pdftoppm: Mills pdf 11–16, 78, 80, 218–222; Pierce pdf 39–41 (p. 23 also at 220 dpi). Printed page numbers read from the running heads. Numbers rerun in Python. Network not used.
---

# S2b check: Mills and Pierce units

## Summary
- **New units:** 8 (16–23), all **VERIFIED**. Units 1–15 untouched (the first 217 lines of the brief were diffed against the prior copy: identical).
- **Mills edition:** OUP 2000 printing with Gitlin afterword (copyright 1959, 2000). Printed = pdf − 7 (checked on pp. 4–10, 71, 73, 208–216). Pagination of the 1959 first printing: UNSEEN.
- **Pierce:** same 1961 Harper file as S2; printed = pdf − 16 confirmed on pp. 23–25.

## One line per unit
- **U16** VERIFIED. Imagination as a "quality of mind" that grasps history, biography and their relations. Mills pp. 4–6 (pdf 11–13); four quotes matched and read on the images. Trap: Mills' "Age of Fact" *information* is the everyday sense, not Shannon's.
- **U17** VERIFIED. "The capacity to shift from one perspective to another". p. 7 (pdf 14), unhedged; p. 211 (pdf 218) with "in considerable part"; p. 8 "Correctly or incorrectly". All matched.
- **U18** VERIFIED. Troubles of milieu vs issues of social structure; unemployment 1 in 100,000 vs 15 million of 50 million employees. pp. 8–10 (pdf 15–17). Two script misses explained: (a) the p. 8 quote ends "structure.'" on the image, but the OCR reads "structure/" and drops the period; (b) "unlike even widespread trouble" runs across the p. 8/9 break, so it is cited pp. 8–9. Problem for the writer: the numbers are hypothetical, and the rate is ambiguous (30% or 23%), so state no rate.
- **U19** VERIFIED. Cross-classification, "in many ways ... the very grammar of the sociological imagination", with Mills' own hedges ("I believe", p. 212; "I do not think I can really answer that", p. 211). pp. 208–213 (pdf 215–220). The 16-cell example: 2^4 = 16 (Python).
- **U20** VERIFIED. Extremes and opposites; a variety of viewpoints (political scientist, experimental psychologist, historian); "a moving prism". pp. 213–214 (pdf 220–221). Trap: Mills' extremes are opposite *types*, not a parameter at zero or infinity; the H = 0 reading is ours.
- **U21** VERIFIED. Inverting the sense of proportion ("can sometimes be achieved"); villages of 30 millions; the comparative grip. p. 215 (pdf 222), note 5 (Burke). "*comparative*" is italic on the page.
- **U22** VERIFIED. Pierce p. 23 (pdf 39): one of ten possible messages conveys less information than one of a million. OCR garbled. Both quotes were read on the page image at 220 dpi; the reader's underlining hides no word. Problem: the sentence does not say "equally likely"; our 3.32 vs 19.93 bits need that assumption, labelled ours.
- **U23** VERIFIED. Pierce pp. 24–25 (pdf 40–41): E gets one dot; frequencies "were estimated by counting the number of types" in a printer's type box; "about 15 per cent" possible speed gain; code devised by 1838 "While Morse was working with Alfred Vail". All matched and read on the image. Problem: the topic card's "Morse ... estimated letter frequencies" over-attributes. Pierce uses the passive and names Vail.

## Problems found in planning documents (not in the units)
1. **topic-card.md line 65** (minor): "Morse (1838) gave E a single dot, and estimated letter frequencies by counting a printer's type box (Pierce p. 25)". Pierce does not say who estimated the frequencies. The code "had been devised by 1838" while Morse worked with Vail (p. 24). Fix: use the passive, or "Morse and Vail's code".
2. **topic-card.md line 66** (minor): "a message that is one of ten possible messages tells less than one that is one of a million". This is fair as a paraphrase. The comparison assumes comparable chances, which Pierce leaves unstated (U22 trap a).
3. **WRITING §1b / outline layer 5** (note, not an error): the four move names are ours, not Mills'. "Another discipline's eyes" is part of Mills' item (4); it is not a numbered habit of its own. Mills lists seven (pp. 212–216). §1b's "15 million unemployed in a nation of 50 million employees" matches p. 9 as a paraphrase, but quotes must keep "15 million men".
4. **Outline Move 1** (risk, for S5): the "issue at scale" framing can turn Mills' distinction into a matter of headcount. Mills says an issue is "unlike even widespread trouble" (pp. 8–9). U18 trap (b) gives the fix.
5. **Balance** (WRITING §9): Mills' ch. 3 stance on statistics is two-sided (p. 73: abstracted empiricism "eliminates the great social problems", and "one should always try to use" statistical procedures where they fit). Both lines are in the addendum's balance note. The post should not cite Mills as for or against quantitative work without both.

## Still open
- The pagination of Mills' 1959 first printing: UNSEEN.
- The Pierce provenance decision (S2 G2): still with Kunhao.
