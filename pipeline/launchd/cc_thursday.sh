#!/bin/zsh -l
# Claude Code route, weekly run (pipeline/CLAUDE_CODE_ROUTE.md). Started by launchd on Thursdays 13:00 JST.
# Uses the Claude subscription (claude -p, Sonnet); stops by 20:30, before the 21:00 weekly reset.
set -u
REPO="$HOME/code/AI4Read"
LOG="$REPO/pipeline/_work/logs/cc-run-$(date +%Y%m%d).log"
mkdir -p "$REPO/pipeline/_work/logs"
cd "$REPO" || exit 1
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/bin:/bin:$PATH"
echo "=== cc-run start $(date)" >> "$LOG"
caffeinate -i uv run python -m pipeline cc-run --until 20:30 >> "$LOG" 2>&1
echo "=== cc-run end $(date) exit $?" >> "$LOG"
