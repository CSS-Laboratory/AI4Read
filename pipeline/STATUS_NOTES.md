### wave1 measured (prompts v2.1)
- Units: 107 (107 accepted) · text pages 1098 · image pages 1005
- Cost: all-in $31.13 (first pass P1+P2 $29.61; retries/fixes +5%)
- **Per page (all-in, least squares): text $0.0118 · image $0.0156**
- Length vs target (accepted): median 1.11× · 10–90%: 0.73–1.56× · > 1.5×: 13/107
- **Re-forecast (remaining units, all-in rates):** core 924 units $229 · deep 145 units $33 · reference 163 units $53
- Total remaining ≈ $315 + spent $42 = **$357** vs $300 cap
- Scenarios: core only ≈ $271 ✅ · core + deep ≈ $304 (≈ $4 over) · + reference ≈ $357 ❌. (Remaining core includes the 11 v1 pilot units, to be redone with v2.1.)

### Smoke v2.1 (Wittgenstein ch04)
- Digest 3,998 words vs target 2,822 (1.42×; v2 was 7,357).
- **§272 (W4): not tagged** (neutral "Statement:" label) **and not flagged**: the unit has more than 80 mandatory items (12 strength, 16 reading-notes, 52+ voice) and the §272 sentence fell beyond the cap.
- The verifier needed 53k output tokens (38k thinking) → P2 limit raised 40k → 64k. Smoke cost $0.67.

### Engineering changes during wave 1 (quality lead to confirm the first)
- L1 at 121–138 words = warning, not a re-digest trigger (7 units had gone to P3 only for L1 = 121–143 words).
- Reading notes may cite `(pdf N)` for the page offset (40 false alarms); multi-`\tag` `aligned` → `align` for KaTeX.

