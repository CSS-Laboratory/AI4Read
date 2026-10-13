# Gate 2b — regression test (prompts v2, spec 1.2)

Status: **Part A FAILED** → mode `pause` for waves; part B finished for diagnostics at Kunhao's request (2026-10-14).
Brief: `pipeline/reviews/gate2.md`. Raw outputs: `pipeline/results/gate2b/A/` (verifier v2 on v1 digests), `pipeline/results/gate2b/B/` (full v2 run).

## Engineering requests (all done, commit `f2179d3`)
1. `{{MANDATORY_ITEMS}}`: sentences from L0, L1, L2 and every intuition note (blockquote `> **Intuition note.**`) with only|always|never|iff|exactly|all|every|must|cannot|proves|shows; sent as a JSON list in a second, uncached system block. `<h_checks>` parsed; missing block → P2 rerun (max 2, then needs_human).
2. Printed page labels from running heads/feet: scans 5 top / 3 bottom lines (MacKay's banner lines), letter suffixes (`95e`), 2-vote threshold for short papers, dominant-offset fallback, TOC-offset fallback for text-less scans (Arrow), spread labels (Dennett). **161 of 1,283 PDF units (12.5%) still lack printed labels**: 89 in ebooks with no page numbers (Kahneman, Rogers, Pearl 2018, Mitchell, Thaler), 18 Åström (chapter-page "8-24"), 13 Ashby (irregular two-page spreads), 41 single papers/scans.
3. All catalog fields + concept spines (Jaynes, MacKay, Wiener, Centola are multi-field).
4. Residue stripping on acceptance: tags, JSON fragments, wrapping fences, verifier chatter sentences ("is correct as printed", "the digest says"…); checker warns if any remain.
5. Checks: Prerequisites line required; `(pdf N)` citations are an error when printed labels exist. `SPEC_VERSION = 1.2`.

## Part A — verifier v2 on the accepted v1 digests (4 units, $0.91)
Pass criterion: all 4 criticals and ≥ 8 of 11 majors from the audit. **Result: 2/4 criticals, 7/11 majors → FAIL.**

| ID | Sev. | Unit | Audit error | Caught? | How |
|---|---|---|---|---|---|
| C1 | crit | Cover | L2 "entropy increases only if uniform" | ✅ | critical H + edit |
| C2 | crit | Cover | Reading notes: 2nd-edition content from memory | ❌ | not mentioned |
| J1 | crit | Jaynes | L2 "same value for AB̄ and BĀ" | ✅ | critical H |
| W1 | crit | Wittg. | §249 rhetorical question → "we may be too hasty" | ❌ | not mentioned |
| C3 | major | Cover | intuition note "entropy rises only toward uniform" | ✅ | h_check not-ok + edit |
| J2 | major | Jaynes | L2 drops Gödel hedge | ✅ | critical H (bullet 9) + edit |
| J3 | major | Jaynes | added step sign after (2.52) | ✅ | critical E |
| D1 | major | Dennett | `(pdf N)` instead of printed pages | ✅ | major C |
| D2 | major | Dennett | Footnote 2 Ouija/Martian reply misread | ❌ | not mentioned (a different Martian-section omission was flagged) |
| W2 | major | Wittg. | §§262–263 challenger's question as W.'s reply; "An odd question" dropped | ❌ | not mentioned |
| W3 | major | Wittg. | §264 interlocutor thesis unattributed | ❌ | not mentioned |
| W4 | major | Wittg. | §272 private-linguist view as finding + canonical instance | ❌ | only a general flag on §§272–280 notes' content, not voice |
| W5 | major | Wittg. | L0 drops "one possibility" (§244) | ✅ | critical H |
| W6 | major | Wittg. | imported "Meaning is use" | ✅ | critical H + critical A (Concepts) |
| W7 | major | Wittg. | `(pdf N)`; "printed pages unknown" | ✅ | major C |

What v2 does well: strength checks on L0–L2 and intuition notes (mandatory items work: C1, C3, J1, J2, W5, W6), added-step arithmetic (J3), systematic citation problems (D1, W7). It also raised many new critical H findings the audit did not list (e.g. Dennett "apparently" dropped twice; Jaynes dropped conditions) — not scored, but they look plausible.

What it misses — a clear pattern:
- **Voice inside L3 walkthrough bullets** (W1–W4): sentences that quote or paraphrase an interlocutor are not in the mandatory list (no strong words) and the verifier does not check L3 voice sentence by sentence.
- **Reading notes outside knowledge** (C2): check A says "every section" but the Reading notes were not flagged.
- **Misread content deep in L3 footnotes** (D2).

Possible directions for the quality lead (engineer's view, not decided): add L3 sentences that report a view (quotes, "Reply:", "he says", interlocutor markers, question marks in the source) to the mandatory list; a separate short P2b pass only for voice/Reading notes; or a deterministic list of every L3 bullet that contains a quotation mark for the verifier to tag with a speaker.

Cost per unit (P2 v2): output 17–36k tokens, thinking 13–16k (v1: 3–9k thinking) — P2 v2 ≈ $0.19–0.28 per unit vs $0.05–0.23 in v1.

## Part B — full v2 run (5 units)
_in progress — results below when finished_
