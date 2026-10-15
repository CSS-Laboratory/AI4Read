# Digest pipeline — status

- **Stage:** P4 work maps — 80 of 80 written
- **Mode:** pause (Vertex pipeline done)
- **Spent:** $439.02 of $445 cap
- **Jobs running:** 0
- **All units:** accepted 1339
- **Updated:** 2026-10-15 10:25

- **Wave 6 accepted** (quality lead, `reviews/wave-6.md`): digestion complete, 1,339 units, 44 hand fixes in audited files (never overwritten).
- **P4 work maps done:** 80 maps, one `wiki/works/<work>/index.md` per multi-unit work (1,242 units; 97 single-unit works get no map). One Vertex batch job, prompt `work_index.md`. All 80 pass the map checks (frontmatter, five sections, paragraph ≤ 150 words, path = accepted units in order, no unknown unit links). No audited file existed or was touched.
- **Cost:** $5.28 (forecast $4.32; 648k output tokens incl. 181k thinking). Map length: median 1,597 words (628–3,664).
- **Engineering notes:** input = each unit's title, L0, L1 (+ Prerequisites), L2 and its Concepts links (needed for "Concepts introduced"); max_tokens 32k. Two fixes after the run: my section check misread "Concepts introduced" as the digest's "Concepts" (checker bug; no model call), and 1 map listed short unit ids in `units:` (expanded by hand). Proposals 7–8 in `reviews/prompt-proposals.md`.
- **Total spend:** $439.02 of the $445 cap ($5.98 left). **The Vertex pipeline is done.**
- **Paused** (`control.json`: pause). Report: `pipeline/results/p4_report.json`.
