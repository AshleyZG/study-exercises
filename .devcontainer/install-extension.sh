#!/usr/bin/env bash
# Installs the study build of the student extension from the vendored .vsix.
#
# Why this exists: devcontainer.json's "extensions" list can only name published
# Marketplace / Open VSX ids. Until the study build is published (or when it is
# newer than what is published), the exact build has to be side-loaded so every
# participant runs identical code.
#
# Non-fatal by design: if the Marketplace copy is already correct, a failure here
# should not break the Codespace.
set -uo pipefail

VSIX="$(dirname "$0")/student-extension.vsix"

if [[ ! -f "$VSIX" ]]; then
  echo "[setup] no vendored .vsix found — relying on the Marketplace copy."
  exit 0
fi

# The `code` CLI is not always on PATH the instant postCreateCommand runs.
for i in $(seq 1 30); do
  if command -v code >/dev/null 2>&1; then
    break
  fi
  sleep 2
done

if ! command -v code >/dev/null 2>&1; then
  echo "[setup] 'code' CLI unavailable; skipping side-load."
  echo "[setup] Install manually: Extensions view -> ... -> Install from VSIX."
  exit 0
fi

echo "[setup] installing $(basename "$VSIX") ..."
code --install-extension "$VSIX" --force && \
  echo "[setup] done — reload the window if the AI Feedback panel is missing." || \
  echo "[setup] side-load failed; install manually from the Extensions view."

exit 0
