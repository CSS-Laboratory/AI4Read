# Prompt for the khyang-lab.org website agent · 2026-11-04

Copy everything below the line into the agent that maintains khyang-lab.org (repo `MI&ME Unit`, folder `web/`).

---

You maintain khyang-lab.org. This task adds **Chinese reference audio** to the AI4Read posts on `https://khyang-lab.org/ai4read/`. Kunhao asked that **only his account** can hear it. Every other signed-in reader keeps the English audio only, and must not be able to fetch the Chinese files at all.

All page changes are made and tested in the AI4Read repo. Your job is to:
1. port one small Worker change;
2. upload;
3. confirm the lock works.

**Do not edit the post files yourself.** If something in them looks wrong, stop and tell Kunhao.

## Rules
- Ask Kunhao before deploying the Worker, and before any step that creates or changes Cloudflare or GCP resources, changes IAM, or costs money.
- Never read, print or create keys or tokens.
- Touch only `/ai4read/*` and `/api/ai4read/*`.
- Commit only the files you change, with a clear message.

## How the lock works
Read `site/ai4read/API.md`, the rows on `audio-zh` and `_owner`.
- The Chinese files live in R2 under the **private prefix** `_owner/<slug>/audio-zh/`. They are never in `dist/`.
- The Worker serves them at `/ai4read/<slug>/audio-zh/<file>` **only when the signed-in user's role is `owner`**, meaning their email is in `AI4READ_OWNERS`. Anyone else gets `404`, exactly as for a missing file.
- Any request to `/ai4read/_owner/...` is always `404`.
- The page shows a 中 button in the audio player only when `/api/ai4read/me` says `owner` **and** `audio-zh/chapters.json` loads. The button is a convenience; the Worker's 404 is the real lock.

## Step 0 · Get the files
```bash
cd ~/code/AI4Read && git pull --ff-only && git log --oneline -3
```
Then read `site/ai4read/API.md`. Also read the reference Worker diff, `git log -p -1 -- site/ai4read/worker/ai4read.ts`; the relevant parts are `servePage(..., role)`, the `_owner/` block, the `audio-zh` regex and `no-store`.

## Step 1 · Check the owner list (ask Kunhao)
Show Kunhao the current value of `AI4READ_OWNERS`. Do not print anything secret; it is a plain var. Confirm that it contains **only his own email address(es)**. Anyone listed there will hear the Chinese audio and also sees everyone's notes. If it needs a change, ask him first.

## Step 2 · Port the Worker change
Apply the same change to the live Worker (`web/worker/…`, where `handleAI4Read` is wired):
1. pass `role` into the page handler;
2. return `404` for any key starting with `_owner/`;
3. map `<slug>/audio-zh/<file>.(mp3|json)` to `_owner/<slug>/audio-zh/<file>` for owners, and return `404` for everyone else;
4. send `cache-control: private, no-store` for `_owner/` objects;
5. keep `Range` support (`206`): iPhone audio needs it.

Also make sure the deployed `_shared/site-shim.js` is the new one. It adds `claude.use("user")` with `isOwner()`; `publish-r2.sh` uploads it. Show Kunhao the diff, then deploy only after he says yes.

## Step 3 · Upload
```bash
bash ~/code/AI4Read/site/ai4read/publish-r2.sh ~/code/AI4Read/site/ai4read/dist
```
The script now also uploads `posts/<slug>/audio-zh/*` to `ai4read/_owner/<slug>/audio-zh/`. Check that the lines `put _owner/<slug>/audio-zh/...` appear for each post that has Chinese audio. Never copy these files to any other prefix.

## Step 4 · Acceptance tests (report each)
1. **As Kunhao**, on a phone and in a desktop browser, open each post that has Chinese audio. The player shows **中**. Tap it: the chapter title turns Chinese and playback is Chinese. Tap again: back to English at the same chapter. Seeking and the lock screen work, and Range requests return 206.
2. **As a non-owner.** Ask Kunhao to sign in with a second account that is allowed by Access but is not in `AI4READ_OWNERS`, or to ask a student to try. Check:
   - no 中 button;
   - `https://khyang-lab.org/ai4read/<slug>/audio-zh/chapters.json` returns **404**;
   - `…/audio-zh/hook.mp3` returns **404**;
   - `…/_owner/<slug>/audio-zh/hook.mp3` returns **404**;
   - the English audio still plays.
3. As anyone: `/ai4read/_owner/…` is 404, and the English chapters and widgets are unchanged.
4. There are no CSP errors in the console, and no horizontal scroll at 390 px.

## Step 5 · Record and report
- Record the change in your PROGRESS file.
- Reply to Kunhao with:
  - the Worker diff you deployed;
  - the owner list check, without printing anything secret;
  - the upload lines for `_owner/`;
  - the result of each test.
