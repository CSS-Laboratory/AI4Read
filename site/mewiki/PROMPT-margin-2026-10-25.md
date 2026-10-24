# Prompt for the Margin (MeWiki) agent · 2026-10-25

Copy everything below the line into the agent that maintains Margin (`MeWiki/web`, Next.js, Firestore, Cloud Run `mewiki-web`, project `toolbox-437319`).

---

You maintain Margin, Kunhao's English-learning app. This task imports the new English packs for AI4Read posts 01 and 02.

**What changed.** Kunhao asked that each AI4Read post's English material be separated from the blog. The material must be **C1 or C2 only**. The AI4Read repo now builds a separate pack for each post from `posts/<slug>/english/english.json`; the blog pages no longer contain English sections. The pack format is still `ai4read.english-pack/1`, with these changes:
- every item except tips has a `level` field (`"C1"` or `"C2"`), and the same value is also in its tags;
- the pack has a top-level `"levels": "C1-C2"`;
- the shadowing item's audio is now a **file** that comes with the pack. It is not a khyang-lab.org URL any more: `audio.file` = `audio/<slug>-loop.mp3` and `audio.url` = `null`;
- some earlier items are gone (B2 items, the old loop paragraphs). They are listed in `site/mewiki/packs/retired-2026-10-25.json`.

**Do not edit the pack files.** If a pack fails validation, stop and tell Kunhao.

## Rules
- Ask Kunhao before deploying, or before changing IAM, Firestore rules, secrets or storage buckets. Never read, print or create keys; use ADC as before.
- Never reset or rewrite FSRS fields (`dueAtMillis`, `stability`, `difficulty`, `reps`, `lapses`, `state`, …) or review logs.
- Never delete a card. "Retire" means suspend, and only after Kunhao says yes.

## Step 0 · Get the files
On Kunhao's Mac the AI4Read repo is at `~/code/AI4Read`.
```bash
cd ~/code/AI4Read
git remote set-url origin https://github.com/CSS-Laboratory/AI4Read.git   # the repo was renamed
git pull --ff-only
```
Read `site/mewiki/HANDOFF-margin.md`, including its §0 update dated 2026-10-25. The inputs are:

| File | What it is |
|---|---|
| `site/mewiki/packs/2026-10-llm-next-word.json` | post 01 pack: 16 expressions, 4 patterns, 4 fixes, 2 tips, 1 loop paragraph |
| `site/mewiki/packs/2026-10-ai-finance.json` | post 02 pack: 17 expressions, 4 patterns, 4 fixes, 2 tips, 1 loop paragraph |
| `site/mewiki/packs/<slug>.md` | readable previews of the same items |
| `site/mewiki/packs/audio/<slug>-loop.mp3` | the recorded loop paragraphs (about 59 s and 53 s), tagged "AI4Read from CSS Lab" |
| `site/mewiki/packs/retired-2026-10-25.json` | externalIds from the earlier packs that are no longer included (29 for post 01, 16 for post 02) |

## Step 1 · Importer
- **If `import:ai4read` exists** (HANDOFF-margin.md §4), extend it:
  - store `level` on the card, and keep it in the tags;
  - accept `audio.url = null` together with `audio.file`;
  - keep the same idempotency rule: card id = hash(userId, externalId).
- **If it does not exist yet**, build it as HANDOFF-margin.md §3–§4 describe (CLI first), with the changes above.

Validation must check:
- `sentence.slice(start, end) === target.text`, in UTF-16;
- every non-tip item has `level` ∈ {C1, C2};
- Margin's existing length limits.

If any item fails, reject the whole pack and list the errors.

## Step 2 · Loop audio
If Margin can store and play an uploaded audio file for a shadowing card, upload `audio/<slug>-loop.mp3` and set it as the card's "post voice". Ask Kunhao before creating any new bucket or folder. If Margin cannot do that yet, use Margin's own TTS for the shadowing card, as it does now, and tell Kunhao that the file is waiting.

## Step 3 · Dry run, then import
```bash
npm run import:ai4read -- ~/code/AI4Read/site/mewiki/packs/2026-10-llm-next-word.json --dry-run
npm run import:ai4read -- ~/code/AI4Read/site/mewiki/packs/2026-10-ai-finance.json --dry-run
```
- **Expected for post 01:** 25 cards (16 expressions, 4 patterns, 4 fixes, 1 shadowing) and 2 tips skipped.
- **Expected for post 02:** 26 cards (17 expressions, 4 patterns, 4 fixes, 1 shadowing) and 2 tips skipped.
- If the earlier packs were imported before, some cards already exist: 9 for post 01 and 8 for post 02. They report as "updated" (new definition, level or tags) or "unchanged". Their FSRS state must not change.

Show Kunhao the dry-run output, then run the same two commands without `--dry-run`.

## Step 4 · Retired items (Kunhao decides)
Use `retired-2026-10-25.json` to find the earlier cards that are no longer in any pack. Show Kunhao how many exist in his account, with a few headwords as examples. Then ask whether to:
- (a) suspend them, which keeps their history;
- (b) keep them active.

Kunhao asked for C1/C2 only, so (a) is the likely answer. Wait for his reply.

## Step 5 · Acceptance tests
1. Filtering the review queue by tag `ai4read` and `C2` shows only C2 items; filtering by `C1` shows only C1 items. No card from these packs is tagged B2.
2. Highlight offsets are right: check 5 cards at random, including `that’s a big if` (curly apostrophe), `an Achilles' heel` (straight apostrophe) and `to throw something into sharp relief` (long target).
3. Fix cards show the wrong → right pair.
4. The shadowing card loops, and the post voice plays if Step 2 was possible.
5. Re-import both packs. The result is 0 created, 0 updated and all unchanged, and the FSRS state of a card you reviewed is unchanged.
6. Every card's source link opens the post: `https://khyang-lab.org/ai4read/<slug>/`. It needs Kunhao to be signed in.

## Step 6 · Record and report
- Commit the importer changes with a clear message.
- Reply to Kunhao with:
  - the created / updated / unchanged counts;
  - the result of each test;
  - the retired-items question;
  - whether the loop audio is hosted or still waiting.
