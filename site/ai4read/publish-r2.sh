#!/usr/bin/env bash
# Upload site/ai4read/dist to the R2 bucket "ai4read" (run from the website repo's web/ folder, where wrangler is logged in).
# Usage: bash publish-r2.sh /path/to/ai4read/site/ai4read/dist [slug]   (slug: upload only that post + _shared + index.html)
set -euo pipefail
DIST="$(cd "${1:?path to dist}" && pwd)"; ONLY="${2:-}"; WEB="$(pwd)"
type_of() { case "${1##*.}" in html) echo "text/html; charset=utf-8";; js) echo "text/javascript; charset=utf-8";; css) echo "text/css; charset=utf-8";; json) echo "application/json";; mp3) echo "audio/mpeg";; svg) echo "image/svg+xml";; *) echo "application/octet-stream";; esac; }
# wrangler 4 writes to a local simulator unless given --remote; wrangler 3 targets R2 already and rejects the flag
MAJOR="$(cd "$WEB" && npx wrangler --version 2>/dev/null | grep -oE '[0-9]+' | head -1)"
REMOTE=""; if [[ "${MAJOR:-4}" -ge 4 ]]; then REMOTE="--remote"; fi
echo "wrangler ${MAJOR:-?}.x${REMOTE:+ (--remote)}"
cd "$DIST"
# skip hidden paths (e.g. a stray .wrangler/ state folder) so they never reach R2
find . -type f -not -path "./.*" -not -path "*/.*" | sed 's|^\./||' | while read -r f; do
  if [[ -n "$ONLY" && "$f" != "$ONLY/"* && "$f" != _shared/* && "$f" != index.html ]]; then continue; fi
  echo "put $f"
  (cd "$WEB" && npx wrangler r2 object put "ai4read/$f" --file "$DIST/$f" --content-type "$(type_of "$f")" $REMOTE >/dev/null)
done
# audio is not kept in dist/ (git): upload it from posts/<slug>/audio/
REPO="$(cd "$DIST/../../.." && pwd)"
for d in */; do slug="${d%/}"; [[ "$slug" == _shared ]] && continue; [[ -n "$ONLY" && "$slug" != "$ONLY" ]] && continue
  for f in "$REPO/posts/$slug/audio/"*.mp3; do [[ -e "$f" ]] || continue; echo "put $slug/audio/$(basename "$f")"
    (cd "$WEB" && npx wrangler r2 object put "ai4read/$slug/audio/$(basename "$f")" --file "$f" --content-type "audio/mpeg" $REMOTE >/dev/null); done; done
echo "done"
