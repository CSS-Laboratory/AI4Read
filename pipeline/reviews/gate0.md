# Gate 0 review — quality lead (2026-10-12)

**Verdict:** approved once the batch smoke job returns OK (both rows, including the image row). No need to wait for me after that; continue to Gate 1.

Good work: NOTES.md is clear, the prices are verified, and the JPY budget is set.

## Requests

1. **Thinking tokens.** NOTES says thinking can't be disabled on Sonnet 5.5 (lowest = `between_tools`). Thinking is billed as output. In the batch smoke results, and in every later cost record, log `thinking` (or equivalent) output tokens **separately** from visible output tokens. If thinking adds more than ~15% to output tokens on the pilot, tell me in STATUS.md; we may need to adjust the setting or prompt.
2. **max_tokens.** Use 32000 for P1 (digest) and 40000 for P2 (verify). Log `stop_reason`; any `max_tokens` stop = unit goes back to the queue split into smaller parts.
3. **Budget margin.** With the `us` batch price the plan is tight. Two savings I'm adopting now:
   - **Prompt caching:** put the system prompt (prompt + DIGEST_SPEC + concept list) in a `system` block with `cache_control`, identical for all units of the same field, and group a field's units together in the same job. Please test whether batch reports cache hits.
   - **Edit-based repairs:** `prompts/verify.md` now asks the verifier for a list of exact text edits instead of rewriting the whole digest (full rewrite only when edits can't express the fix). Apply the edits deterministically: each `find` must match exactly once; if any edit fails to apply, re-run P2 for that unit online asking for the full `<corrected>` block.
4. **Forecast at Gate 2** must include: cost per page for text-only pages vs image pages, P1 vs P2 split, thinking share, and the projected total. If the projected total exceeds $270, stop and report before any wave.
