# Gate 0 research notes (2026-10-12)

Vertex AI docs now live under "Gemini Enterprise Agent Platform" (old `cloud.google.com/vertex-ai/...` URLs redirect).

## Model
- Id: **`claude-sonnet-5-5`** (no `@date` suffix; GA 2026-09-28). Resource: `publishers/anthropic/models/claude-sonnet-5-5`.
- Locations: **`global`**, **`us`** (multi-region), **`eu`** (multi-region). No single regions.
- Limits: 1M input / 128K output tokens. Online: images ≤ 5 MB, ≤ 100 per request.
- Thinking cannot be `disabled` on Sonnet 5.5; lowest setting is `between_tools`.
- Enable once in Model Garden (accepts Anthropic terms) if not done yet.
- Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/sonnet-5-5
- Endpoints: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models
  - global: `https://aiplatform.googleapis.com/v1/projects/P/locations/global/publishers/anthropic/models/M:rawPredict`
  - us: `https://aiplatform.us.rep.googleapis.com/v1/projects/P/locations/us/...`

## Batch prediction — ⚠ differs from DESIGN.md
- Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/batch
- Quote (verified): "The global endpoint for partner models isn't supported." → **batch must run in `us`** (multi-region, +10% price).
- Input: BigQuery table or GCS JSONL. Row = `{"custom_id": ..., "request": {"messages": [...], "anthropic_version": "vertex-2023-10-16", "max_tokens": N, ...}}`. BQ: job and table in same region; don't name columns `response` or `status`.
- Output: BQ `response` column or JSONL under a GCS prefix. Results after all rows finish or 24 h.
- Create: `POST https://LOCATION-aiplatform.googleapis.com/v1/projects/P/locations/LOCATION/batchPredictionJobs` with `model`, `inputConfig{instancesFormat: jsonl, gcsSource.uris}`, `outputConfig{predictionsFormat: jsonl, gcsDestination.outputUriPrefix}`. Exact host for the `us` multi-region: to confirm in smoke test.
- Default quota: 4 concurrent batch jobs per project.
- **Unconfirmed in docs → test at Gate 0:** batch in `us` works; image blocks in batch; max request size; max rows per job.
- Plan: GCS JSONL in/out (simpler than BQ for large base64 images).

## Price (per 1M tokens) — verified on pricing page
https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing

| Sonnet 5.5 | global | us / eu |
|---|---|---|
| Input / output | $2.00 / $10.00 | $2.20 / $11.00 |
| **Batch input / output** | $1.00 / $5.00 | **$1.10 / $5.50** ← what we pay |
| Batch cache hit | $0.05 | $0.055 |
| 5m batch cache write | $1.25 | $1.375 |

No long-context (>200K) premium. Cloud Billing SKU ids: not found (Catalog API needs an API key; skipped).

**Budget impact:** +10% vs DESIGN's global assumption. DESIGN rough plan ≈ $220–250 → ≈ $240–275. Tight against the $280 cap; re-forecast after the pilot. Batch prompt caching of the shared system prompt is a possible saving (see prompt-proposals if relevant).

## Project state (read-only checks)
- `gcloud` account and ADC OK; quota project `playground-491901`.
- Enabled already: aiplatform, bigquery, storage, billingbudgets.
- Cloud Billing API enabled on playground-491901 (2026-10-12, approved) so budgets can be made by CLI.
- Billing account `0183F1-3E1FCA-68DC56` ("Research") is billed in **JPY**. Our USD cost log uses list prices; Google's invoice is in yen.
- Budget `752397f5-33c1-4f4c-a64f-7cdf2c6b1d69`: **¥48,000** (≈ $300 at 160 JPY/USD), project filter playground-491901, alerts at 50% / 83.33% / 100% (¥24,000 / ¥40,000 / ¥48,000), emails to billing admins.

## Smoke test results
- Online, global: OK. 18 in / 4 out tokens, $0.000076. Model id answered as `claude-sonnet-5-5`.
- Batch, `us` (`aiplatform.us.rep.googleapis.com`, `locations/us`): job accepted (`batchPredictionJobs/8438349321925033984`), PENDING 3.5 min → RUNNING 50 min → **FAILED `{code: 13, message: INTERNAL}`** (08:39 UTC). No output files, no partial results, no Cloud Logging entries. Cause unknown: image row, text row, or `us` batch itself. Retest 18:40 JST: two 1-row jobs (text-only `207317315463675904`, image-only `4819003333891063808`) → **both FAILED `INTERNAL`** after ~50 min each (start→end 09:40→10:31 UTC). So it is not the image. All three jobs die at ~50 min with no output and no logs.
- Vertex service agent `service-628671067824@gcp-sa-aiplatform` has only `roles/aiplatform.serviceAgent`; the bucket has no explicit binding for it. Hypothesis: it cannot read/write the bucket. Untested.
- Online calls (global) work fine.

## Batch fix attempts (2026-10-12, approved by Kunhao)
- 19:47 JST: granted `service-628671067824@gcp-sa-aiplatform` **roles/storage.objectAdmin on gs://ai4read-batch-628671 only**; retried 1-row text job via GCS (`3087369277167108096`).
- 19:48 JST: created BigQuery dataset `ai4read_batch` (US); 1-row text job with BigQuery in/out (`7164815789797670912`; table `smoke_in` → `smoke_out`).
- Result: **both FAILED `INTERNAL`** after ~50 min (GCS with bucket IAM; BigQuery in/out). Total 5/5 Claude Sonnet 5.5 batch jobs in `us` failed the same way. Not the image, not GCS vs BigQuery, not bucket permission. Likely a Google-side problem (model/location/project). Online calls (global) work.

## Console check (2026-10-13, read-only, via Chrome)
- Batch job page: error is only "INTERNAL"; job shown as "canceled due to one or more errors" after ~50 min. No extra detail.
- Model Garden card (Claude Sonnet 5.5): "ready to use for your project"; feature list includes **Batch prediction** and Global endpoint. Pricing columns are "Global" and "Regional".
- Quotas (aiplatform): online Sonnet-family quotas exist for `global` (25M in TPM) and `us`/`eu` multi-region (12.5M in TPM).
- **Batch quota "Concurrent batch prediction jobs running on Anthropic MaaS model per region" = 4, listed only for single regions** (us-east5, us-central1, europe-west1, asia-…); **no `us` / `eu` multi-region entry**. Our 5 jobs all ran in `us`.
- **Leading hypothesis:** Claude batch is provisioned per single region; the `us` multi-region accepts the job but has no batch backend → `INTERNAL` after ~50 min. Next test (when resumed, < $0.001): submit the 1-row text job to `us-east5` (and/or `us-central1`). If creation is rejected at once or succeeds, we learn quickly.
- 2026-10-13: approved test — same 1-row text input submitted in **`us-east5`**: job **accepted** (`us-east5/batchPredictionJobs/2851720845590528000`) → **row succeeded within minutes**: text "OK", stop `end_turn`, usage 18 in / 4 out / 0 thinking. ✅ **Claude Sonnet 5.5 batch works in `us-east5`.** Root cause of the 5 failures: the `us` multi-region accepts Claude batch jobs but cannot run them.

## Batch facts confirmed (2026-10-13)
- Location: **`us-east5`** (`https://us-east5-aiplatform.googleapis.com`). Price = regional batch ($1.10 / $5.50 per M) — same as we budgeted.
- GCS input from the US multi-region bucket works.
- Output: `<prefix>/prediction-model-<ts>/predictions.jsonl`, rows `{custom_id, processed_time, response, status}`; `status` is "" on success. Also `incremental_predictions/*.jsonl` (duplicates — the runner ignores them).
- Still to confirm in the pilot: image rows, large requests (~10 MB), cache hits.

## Cleanup (2026-10-13, requested by Kunhao)
- Removed the test binding `service-628671067824@gcp-sa-aiplatform` → `roles/storage.objectAdmin` on `gs://ai4read-batch-628671` (bucket is back to its default project-role bindings).
- Deleted the BigQuery test dataset `playground-491901:ai4read_batch` (held only the 1-row `smoke_in` table).
- Note: the successful `us-east5` batch test ran while that binding existed. If a future batch job fails reading/writing the bucket, re-test with a 1-row job before restoring the binding.
