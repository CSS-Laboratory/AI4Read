#!/usr/bin/env bash
# Pack everything that is NOT on GitHub into files ready to copy to Google Drive
# (My Drive/Book/AI4Read/backup/). Each file stays under 25 MB (the copy tool's limit is 30 MB).
#   bash scripts/backup_drive.sh            → /mnt/user-data/outputs/ai4read-backup/
# Then copy that folder to Drive (Claude: device_commit_files; or by hand), and run `git push`.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-/mnt/user-data/outputs/ai4read-backup}"
DATE="$(date +%Y%m%d)"
rm -rf "$OUT"; mkdir -p "$OUT/sources" "$OUT/repo"
cd "$ROOT"
for d in posts/*/sources; do
  slug="$(basename "$(dirname "$d")")"
  # OCR page images are temporary; everything else (PDFs, text, saved pages, talk audio) is kept
  tar czf - --exclude='ocr-*' -C "$d" . | split -b 24m -d -a 2 - "$OUT/sources/${slug}-sources.tar.gz.part-"
done
git bundle create "$OUT/repo/ai4read-${DATE}.bundle" --all >/dev/null 2>&1
# split the bundle too (audio makes it large); restore with: cat ai4read-<date>.bundle.part-* > ai4read.bundle
split -b 24m -d -a 2 "$OUT/repo/ai4read-${DATE}.bundle" "$OUT/repo/ai4read-${DATE}.bundle.part-" && rm "$OUT/repo/ai4read-${DATE}.bundle"
cp RESUME.md "$OUT/RESUME.md"
(cd "$OUT" && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS)
find "$OUT" -type f -printf "%8k KB  %p\n" | sort -k3
