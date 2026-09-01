# Researcher setup

Staging folder for the student-facing GitHub repo. Push this directory (not the
parent project) to its own repo — students create a Codespace from it.

## 1. Prerequisites, in order

These must be done **before** any student opens a Codespace.

1. **Redeploy the central server.** The System 1 / System 2 mode API and
   student-initiated conversations only exist in the updated build.
   ```bash
   cd AI-communication/deploy
   git pull && ./build-dashboard.sh && docker compose up -d --build
   curl -s https://humanaifeedback.com/api/mode      # expect {"mode":"main"}
   ```
   Also confirm `AUTO_REPLAY_ON_RESET` is **unset** in `deploy/.env`, or 76
   dataset students will appear alongside the real ones.

2. **Publish the extension** (or rely on the vendored `.vsix`, see §3):
   ```bash
   cd student-extension && npm run package && npm run publish:vsce
   ```

## 2. Create the repo

```bash
cd study-exercises
git init && git add -A && git commit -m "Study exercises"
gh repo create <org>/study-exercises --private --source=. --push
```

Give each participant **read** access. They need their own GitHub account —
a Codespace cannot be handed to someone else.

**Enable prebuilds** (repo Settings → Codespaces → Set up prebuild). Cold
creation takes 1–3 minutes; with several students starting at once that is dead
time at the top of the session. Prebuilds cut it to roughly 20 seconds.

## 3. How the extension gets installed

Two paths, and the container tries both:

| Path | Mechanism | When it applies |
| --- | --- | --- |
| Marketplace | `customizations.vscode.extensions` in `devcontainer.json` | Once the study build is published |
| Vendored VSIX | `.devcontainer/install-extension.sh` at `postCreateCommand` | Always; wins when it is newer |

The vendored copy is `.devcontainer/student-extension.vsix`. **Re-copy it after
every extension change**, or students run a stale build:

```bash
cp ../student-extension/student-extension-<version>.vsix \
   .devcontainer/student-extension.vsix
```

The side-load is deliberately non-fatal — if the `code` CLI is unavailable it
logs and exits 0 rather than failing container creation. Check the Codespace
creation log for `[setup]` lines to confirm which path ran.

## 4. Running a session

Codespaces run the extension in the **container's** extension host (the desktop
bundle, with Node and `python3`), not the browser web worker — so classifiers
run locally on each student's machine.

Per problem:

1. Set the system on the dashboard toggle (**System 1** or **System 2**).
2. Click **Start new session** — this clears classifiers, conversations, and
   code between conditions. Do this every time; mode switching alone does not
   clear state, so the previous condition's conversations would otherwise leak
   into the panel.
3. Tell students which file to open.

Counterbalance which system pairs with which problem if you run more than one
session.

## 5. AI assistants are disabled

`chat.disableAIFeatures: true` (in both `.vscode/settings.json` and the
devcontainer) hides Copilot chat, disables inline suggestions, and disables the
Copilot extensions themselves. Older per-extension settings are kept alongside it
for VS Code builds that predate it, and `settingsSync.ignoredExtensions` stops a
participant's own synced profile from pulling Copilot back in.

Verify in a real Codespace before recruiting: no chat icon in the title bar, no
ghost-text completions while typing in `problem_a.py`.

## 6. Known gaps

- **Student ids are random.** The extension generates `student-a1b2c3d4` with no
  way to set a name, so the Live Students panel cannot be mapped to people.
- **Nothing is persisted.** Conversations and student code live in memory only
  and are lost on restart or on "Start new session". Only classifier creations
  are written to disk, under `logs/classifiers/<participant>/`.

Both are worth fixing before collecting real data.
