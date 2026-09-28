---
type: issue
state: closed
created: 2026-08-06T12:48:28Z
updated: 2026-09-28T12:22:31Z
author: c-vigo
author_url: https://github.com/c-vigo
url: https://github.com/vig-os/h5v/issues/1
comments: 1
labels: none
assignees: none
milestone: none
projects: none
parent: none
children: none
synced: 2026-09-28T20:28:47.832Z
---

# [Issue 1]: [chore(repo): upgrade devkit scaffold 0.3.1 -> 1.17.0 (direnv, trunk)](https://github.com/vig-os/h5v/issues/1)

## Context

Pinned to legacy devkit scaffold **0.3.1** (legacy `DEVCONTAINER_VERSION` key), ~13 releases behind **1.6.0**, predating the self-upgrade workflow. Manual migration per devkit `docs/MIGRATION.md` ("Upgrading an existing 0.3.x consumer").

`install.sh --preview` dry-run (1.6.0, `--mode direnv --workflow trunk`) is clean: 28 overwrite / 11 preserve / 2 delete / 53 add (incl. new `flake.nix` + `.envrc`; consumer-owned `release-extension.yml` preserved; dead `sync-main-to-dev.yml` pruned).

## Decisions

- **Workflow model `trunk`** — the repo is main-only already; trunk matches reality and drops the dead gitflow sync workflow.
- Delivery mode `direnv`; prune the stale 0.3.1-era `.devcontainer/`.

## Scope

- `install.sh --version 1.6.0 --force --mode direnv --workflow trunk --prune-devcontainer`
- Work the MIGRATION.md 0.3.x checklist: `pre-commit` → `prek` renames in preserved files (`justfile.project` recipes, extra `.githooks`), justfile append-block review, `.pre-commit-config.yaml` template-diff review, project-name re-derivation check
- Full hook suite green locally before PR

## Notes

First release after migration needs the one-time manual-promote runbook (MIGRATION.md) — `promote-release.yml` is not dispatchable until it lands on `main`.
---

# [Comment #1]() by [c-vigo]()

_Posted on September 28, 2026 at 11:45 AM_

Re-scoped: the target is now devkit **1.17.0** (released 2026-09-28), not 1.6.0.

The 1.6.0 adoption diff was built on this issue's branch in August but never merged, so \`main\` is still on the legacy 0.3.1 scaffold (\`DEVCONTAINER_VERSION=0.3.1\`) and 1.6.0 is now eleven releases stale. Rather than land 1.6.0 and immediately upgrade again, the existing branch is being carried straight to 1.17.0 as a single PR.

Retargeting the branch — rather than starting fresh from \`main\` — is deliberate. A fresh branch would inherit \`main\`'s 0.3.1-era \`.pre-commit-config.yaml\`, whose pre-devkit#1170 \`pymarkdown\` block has a hand-extended \`exclude:\`; that makes the automatic fold decline (it only fires on byte-identical devkit-shipped text), and that block breaks \`just precommit\`, local markdown commits and the \`devkit-upgrade\` commit step. It would also re-incur the whole 0.3.x manual checklist (\`pre-commit\`->\`prek\` renames, base-recipe fold, \`.devcontainer/\`/\`.cursor/\`/\`.hadolint.yaml\` pruning) and discard the preserved-file work already on the branch — \`.gitignore.project\` (absent on \`main\`), the \`.typos.toml\` allowlist, the \`justfile.project\` Rust recipes and the \`flake.nix\` \`extraPackages\` set.

Scope added on top of the original 1.6.0 work:

- Remove the unused Python scaffold surface (\`pyproject.toml\`, \`uv.lock\`, \`src/h5v/\`, \`tests/\`) — pure 0.3.1 template residue, so \`DEVKIT_LANGUAGES\` seeds \`rust\` only rather than pinning a permanent CI gate on a marker file this repo does not want.
- Port the \`.vig-os\` knob readers into the preserved \`flake.nix\` (devkit #1432/#1431/#1282/#1633, wired at #1434).
- Revert \`2b95e50\`'s \`shellHook\` \`CC\`/\`CXX\` pin — superseded by devkit #1351 and explicitly denylisted by #1358.
- Pin \`vigos.url\` to \`?ref=1.17.0\` instead of floating on \`main\`, which since #1676's release-neutral lane routinely carries landed-but-unshipped changes.

PR #2 was closed as a side effect of the branch rename; the branch itself is intact at \`2b95e50\`.

