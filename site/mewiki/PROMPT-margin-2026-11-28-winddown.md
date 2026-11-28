# Margin wind-down, 2026-11-28

For: the Margin / MeWiki agent (desktop session "English learning app integration review", `~/code/mewiki-web`). From: the AI4Read session. Owner: Kunhao Yang.

Kunhao has **stopped the English-learning project**. AI4Read no longer produces English packs; the existing packs stay in `~/code/AI4Read/site/mewiki/packs/` as history.

Please:
1. **Archive first.**
   - Commit and push `mewiki-web`. It had one uncommitted path on 2026-11-28.
   - Export the Firestore data (review history, imported items, passage progress) and any stored audio to a dated archive, e.g. `My Drive/MeWiki/archive/2026-11-28/`.
   - Report where everything is, with sizes.
2. **Stop ongoing cost.**
   - In GCP project `toolbox-437319`, list everything that belongs to Margin and can bill:
     - Cloud Run `mewiki-web` and its revisions;
     - Firestore;
     - Cloud Storage buckets;
     - Artifact Registry images;
     - Cloud Scheduler jobs;
     - TTS and Gemini usage;
     - domains and DNS.
   - Propose for each: scale to zero, disable, or delete.
   - **Do not touch** the Cloud Run service `ai4read-claude` or the secret `ai4read-proxy-secret` in the same project. They serve the khyang-lab.org website.
3. **Security.**
   - Remove any API key, service account or secret used **only** by Margin. Never paste key values into chat or commit them.
   - **Before removing any Gemini or AI Studio key**, confirm it is not the AI Studio key `2024f5c2`, which Catspaw dev and prod share, and not a key in project `cats-paw-487701`.
   - Background: Google case #78006878 (a Gemini key-abuse incident, 2026-11-26).
4. **Ask Kunhao before** any step that deletes or changes cloud resources, IAM or secrets. Delete only after he confirms the archive.
5. Reply to the AI4Read session (or write the result into `~/code/mewiki-web/docs/winddown-2026-11-28.md`).
