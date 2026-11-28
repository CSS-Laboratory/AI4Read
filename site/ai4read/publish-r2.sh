#!/usr/bin/env bash
# Upload one AI4Read post to the R2 bucket "ai4read" in the blog layout (2026-11-28, website docs/AI4READ_BLOG.md).
# Run from the website repo's web/ folder, where wrangler is logged in. Kunhao approves every upload.
#   bash publish-r2.sh /path/to/AI4Read/site/ai4read <slug> [--dry-run]
# Keys written (nothing else; the old shelf keys at the bucket root are no longer served):
#   public/<slug>/audio/*.mp3   English MP3s only (posts/<slug>/audio/). Served at /blog/<slug>/audio/ once the post is
#                               published, and also read by the owner and preview views (one copy only).
#   owner/_shared/**            dist-owner/_shared/
#   owner/<slug>/**             dist-owner/<slug>/ incl. zh/ and audio-zh/, without the English audio/ folder
#   preview/<slug>/**           dist-public/<slug>/ without MP3s (the draft preview at /blog/_owner/<slug>/public/)
# Hidden paths (e.g. a stray .wrangler/) are always skipped.
set -euo pipefail
SITE="$(cd "${1:?path to AI4Read site/ai4read}" && pwd)"; SLUG="${2:?slug}"; DRY="${3:-}"; WEB="$(pwd)"
REPO="$(cd "$SITE/../.." && pwd)"
PUB="$SITE/dist-public/$SLUG"; OWN="$SITE/dist-owner/$SLUG"; OSH="$SITE/dist-owner/_shared"; AUD="$REPO/posts/$SLUG/audio"
for d in "$PUB" "$OWN" "$OSH"; do [[ -d "$d" ]] || { echo "missing $d (run build-post.mjs posts/$SLUG --public --owner)"; exit 1; }; done
type_of() { case "${1##*.}" in html) echo "text/html; charset=utf-8";; js) echo "text/javascript; charset=utf-8";; css) echo "text/css; charset=utf-8";; json|ipynb) echo "application/json";; mp3) echo "audio/mpeg";; svg) echo "image/svg+xml";; png) echo "image/png";; jpg|jpeg) echo "image/jpeg";; md|py) echo "text/plain; charset=utf-8";; *) echo "application/octet-stream";; esac; }
# wrangler 4 writes to a local simulator unless given --remote; wrangler 3 targets R2 already and rejects the flag
MAJOR="$(cd "$WEB" && npx wrangler --version 2>/dev/null | grep -oE '[0-9]+' | head -1)"
REMOTE=""; if [[ "${MAJOR:-4}" -ge 4 ]]; then REMOTE="--remote"; fi
echo "wrangler ${MAJOR:-?}.x${REMOTE:+ (--remote)}${DRY:+ · dry run}"
put() {  # key file
  echo "put $1"
  [[ -n "$DRY" ]] && return 0
  (cd "$WEB" && npx wrangler r2 object put "ai4read/$1" --file "$2" --content-type "$(type_of "$2")" $REMOTE >/dev/null)
}
upload_tree() {  # source-dir key-prefix filter(all|no-mp3|no-audio-dir)
  local src="$1" pre="$2" mode="$3"
  (cd "$src" && find . -type f -not -path "./.*" -not -path "*/.*" | sed 's|^\./||' | sort) | while read -r f; do
    [[ "$mode" == no-mp3 && "$f" == *.mp3 ]] && continue
    [[ "$mode" == no-audio-dir && "$f" == audio/* ]] && continue
    put "$pre/$f" "$src/$f"
  done
}
if [[ -d "$AUD" ]]; then for f in "$AUD"/*.mp3; do [[ -e "$f" ]] && put "public/$SLUG/audio/$(basename "$f")" "$f"; done; fi
upload_tree "$OSH" "owner/_shared" all
upload_tree "$OWN" "owner/$SLUG" no-audio-dir
upload_tree "$PUB" "preview/$SLUG" no-mp3
echo "done"
