#!/usr/bin/env bash
# Recreate the local, offline TTS used for AI4Read audio (Kokoro-82M ONNX, voice af_heart).
# Usage: bash scripts/setup_tts.sh        → /tmp/ttsenv (Python venv) and /tmp/kmodel (model files, ~350 MB)
# Then:  /tmp/ttsenv/bin/python scripts/tts_post.py posts/<slug>
set -euo pipefail
python3 -m venv /tmp/ttsenv
/tmp/ttsenv/bin/pip install -q "kokoro-onnx==0.6.1" "soundfile==0.14.0" "numpy" "onnxruntime"
mkdir -p /tmp/kmodel
cd /tmp/kmodel
base="https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0"
[ -s kokoro-v1.0.onnx ] || curl -fL -o kokoro-v1.0.onnx "$base/kokoro-v1.0.onnx"
[ -s voices-v1.0.bin ]  || curl -fL -o voices-v1.0.bin  "$base/voices-v1.0.bin"
ls -la /tmp/kmodel
command -v ffmpeg >/dev/null || echo "NOTE: ffmpeg is also required (apt-get install ffmpeg / brew install ffmpeg)"
echo "TTS ready. Expected sizes: kokoro-v1.0.onnx 325,532,387 bytes; voices-v1.0.bin 28,214,398 bytes."
