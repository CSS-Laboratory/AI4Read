# Handoff · AI4Read English packs → Margin (MeWiki web app)

For: the agent that maintains MeWiki / Margin (`MeWiki/web`, Next.js 16, Firestore, Cloud Run `mewiki-web`, project `toolbox-437319`).
From: AI4Read quality lead (Claude). Date: 2026-10-16. Owner: Kunhao Yang. **Ask before deploying or changing IAM, rules or secrets.**

## 0. Update, 2026-10-25 (read first)
- The English material is **no longer part of the blog posts**. Each post has a separate pack built from `posts/<slug>/english/english.json` by `scripts/english_pack.py`, **C1–C2 only**. §1 below still describes the old in-post section; the item kinds and the import rules (§2–§5) are unchanged except:
  - every non-tip item has `level` (`C1`/`C2`), also in `tags`; the pack has `"levels": "C1-C2"`;
  - the shadowing item has `audio.file` = `audio/<slug>-loop.mp3` (shipped in `site/mewiki/packs/audio/`) and `audio.url` = `null`;
  - `source.url` is the post page (`https://khyang-lab.org/ai4read/<slug>/`), no `#english` anchor;
  - items dropped from the earlier packs are listed in `packs/retired-2026-10-25.json` (suspend only if Kunhao agrees; never delete history).
- Current packs: post 01, 27 items (16 expressions, 4 patterns, 4 fixes, 2 tips, 1 loop); post 02, 28 items (17, 4, 4, 2, 1). Each has a readable `.md` preview.
- Step-by-step instructions for this release: `site/mewiki/PROMPT-margin-2026-10-25.md`.

## 0. First
The whole Margin app is still **uncommitted** on top of the pre-pivot commit `ca1d354` (43 changed or untracked paths). Commit it, as Kunhao prefers, before starting this work.

## 1. Goal
Every AI4Read post ends with a "How to say it in English" section. Its contents are:
- topic phrases;
- expressions for discussing evidence (B2 → C1);
- sentence patterns;
- small error fixes;
- practice tips;
- a "paragraph to loop" with audio.

Kunhao wants these items in Margin, so he can review them with FSRS and shadow the loop paragraph. Each item must say which post it came from. Importing must be repeatable: running it again must never reset his review history.

## 2. Input: the English pack (`ai4read.english-pack/1`)
- Example: `site/mewiki/packs/2026-10-llm-next-word.json` (38 items) in the AI4Read repo.
- Generator: `scripts/english_pack.py posts/<slug>`.
- The pack top level has `{schema, post:{slug,title,url}, items:[…]}`.
- Every item has `externalId` (stable, unique), `kind`, `group`, `headword`, `sentence`, `tags[]`, and `source{label,url}`.
- Kind-specific fields:

| kind | count in post 01 | extra fields |
|---|---|---|
| `expression` | 25 | `target{text,start,end}` (UTF-16 offsets into `sentence`, checked), `definition`, `partOfSpeech`, `level` (B2/C1), `register` |
| `pattern` | 4 | `target` (first highlighted word), `definition` |
| `fix` | 4 | `definition`, `wrong`, `right` |
| `tip` | 4 | text only |
| `shadowing` | 1 | `sentence` (≈170 words), `targets[]` (the expressions it uses), `audio{url, voice}` |

## 3. Mapping to Margin
| Pack | Margin | Notes |
|---|---|---|
| `expression` | `vocabulary` card | `sentence` = `sentence` (verbatim); `start/end/targetText` = `target`; `explanation.definition` = `definition`; `partOfSpeech`; `contextNote` = "From AI4Read: " + post title; `learnerExample` = empty (Margin's explain step may fill it later, or leave it); `tags` = pack tags + `level`; `sourceLabel/sourceUrl` = `source`. |
| `pattern` | `vocabulary` card, tag `pattern` | Use the first `target` as the highlight. Later, a `pattern` card type with a cloze prompt would be better (see §6). |
| `fix` | `vocabulary` card, tag `fix` | `sentence` = the right form in context; put `wrong → right` in `contextNote`. |
| `tip` | **not a card** | Show on a small "AI4Read" info panel, or skip. |
| `shadowing` | `shadowing` card | Use the existing `/api/learning/shadowing` pipeline to annotate it (en-GB thought groups, features) and to make Margin's own TTS. Keep `audio.url` as an alternate "post voice" link; it is behind Cloudflare Access, so it only plays when Kunhao is signed in to khyang-lab.org. |

**Idempotency.** Card id = deterministic hash of (`userId`, `externalId`). This is the same idea as the current `requestId` scheme; add an `externalId` field to the card.

On re-import:
- update only the content fields: sentence, target, explanation, tags, source;
- **never touch** the FSRS fields (`dueAtMillis`, `stability`, `difficulty`, `reps`, `lapses`, `state`, …) or the review logs.

Items whose `externalId` disappears from a newer pack stay as they are. Report them; do not archive them automatically.

**Validation.** Check that `sentence.slice(start, end) === target.text`, and enforce Margin's existing limits: sentence ≤ 5,000, target ≤ 500, tags ≤ 20, definition ≤ 1,200. Reject the whole pack, with a clear error list, if any item fails.

## 4. Two ways in (build both; small)
1. **CLI (first):** `npm run import:ai4read -- <pack.json> [--dry-run]`. It runs on Kunhao's Mac with the Firebase Admin SDK and ADC (no new keys), writes through the same store functions as the API, and prints created / updated / unchanged counts.
2. **API route (later, for automation):** `POST /api/learning/import`, same auth as the other learning routes (Firebase ID token, allow-listed email). Body is the pack. Limit 200 items per call; the route batches the items internally (Margin's normal save is limited to 20 cards per call). The AI4Read pipeline can call it after each post. **No new secret in AI4Read**: Kunhao runs the CLI, or imports from the app with a file picker ("Import AI4Read pack…" in Settings).

## 5. Acceptance tests
1. Dry run on the post-01 pack prints 34 cards to create (25 expressions, 4 patterns, 4 fixes, 1 shadowing) and 4 tips skipped.
2. After import, the review queue filtered by tag `ai4read` shows 33 vocabulary cards. Their highlight offsets are right: check 5 at random, including one with a curly apostrophe (`that’s a big if`).
3. The shadowing card plays Margin's TTS in a loop. The post-voice link opens the AI4Read audio when signed in.
4. Review a few cards, then import the same pack again. The result is "0 created, 0 updated, 34 unchanged", and the FSRS state and review logs are unchanged.
5. Edit one definition in the pack and re-import. The result is "1 updated", and its FSRS state is unchanged.
6. Each card links back to the post (`sourceUrl`).

## 6. Optional next steps (ask Kunhao)
- A **production card** for C1 expressions, which shows the definition plus the sentence with a blank, and the learner says or types the expression. Recognition alone will not make the expressions usable "naturally"; production is the step that does.
- A **pattern card**: given a plain B2 sentence, rewrite it with the pattern (cleft, inversion, concession). Margin's tutor checks the answer.
- A **weekly AI4Read playlist** that loops all shadowing paragraphs from the last 4 posts.

## 7. Files
- AI4Read repo: `site/mewiki/HANDOFF-margin.md` (this file), `site/mewiki/packs/*.json`, `scripts/english_pack.py`, `posts/<slug>/english-gloss.json`.
- Margin: `web/src/lib/learning-types.ts` (add `externalId`), `learning-normalizers.ts`, `learning-store.ts`, new `scripts/import-ai4read.ts`, optional `src/app/api/learning/import/route.ts`.
