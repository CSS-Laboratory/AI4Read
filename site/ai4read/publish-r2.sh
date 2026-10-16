#!/usr/bin/env bash
# Upload site/ai4read/dist to the R2 bucket "ai4read" (run from the website repo's web/ folder, where wrangler is logged in).
# Usage: bash publish-r2.sh /path/to/ai4read/site/ai4read/dist [slug]   (slug: upload only that post + _shared + index.html)
set -euo pipefail
DIST="${1:?path to dist}"; ONLY="${2:-}"
type_of() { case "${1##*.}" in html) echo "text/html; charset=utf-8";; js) echo "text/javascript; charset=utf-8";; css) echo "text/css; charset=utf-8";; json) echo "application/json";; mp3) echo "audio/mpeg";; svg) echo "image/svg+xml";; *) echo "application/octet-stream";; esac; }
cd "$DIST"
find . -type f | sed 's|^\./||' | while read -r f; do
  if [[ -n "$ONLY" && "$f" != "$ONLY/"* && "$f" != _shared/* && "$f" != index.html ]]; then continue; fi
  echo "put $f"
  npx wrangler r2 object put "ai4read/$f" --file "$f" --content-type "$(type_of "$f")" --remote >/dev/null
done
# audio is not kept in dist/ (git): upload it from posts/<slug>/audio/
REPO="$(cd "$DIST/../../.." && pwd)"
for d in */; do slug="${d%/}"; [[ "$slug" == _shared ]] && continue; [[ -n "$ONLY" && "$slug" != "$ONLY" ]] && continue
  for f in "$REPO/posts/$slug/audio/"*.mp3; do [[ -e "$f" ]] || continue; echo "put $slug/audio/$(basename "$f")"
    npx wrangler r2 object put "ai4read/$slug/audio/$(basename "$f")" --file "$f" --content-type "audio/mpeg" --remote >/dev/null; done; done
echo "done"
