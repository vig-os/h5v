---
type: pull_request
state: closed
branch: chore/1-upgrade-devkit-1-6-0 → main
created: 2026-08-07T08:13:20Z
updated: 2026-09-28T11:44:57Z
author: c-vigo
author_url: https://github.com/c-vigo
url: https://github.com/vig-os/h5v/pull/2
comments: 3
labels: none
assignees: none
milestone: none
projects: none
synced: 2026-09-28T20:28:53.633Z
---

# [PR 2](https://github.com/vig-os/h5v/pull/2) chore(repo): upgrade devkit scaffold 0.3.1 -> 1.6.0 (trunk, direnv)

## Summary

Migrates h5v off the legacy devkit 0.3.1 scaffold (pre-auto-upgrade, legacy `DEVCONTAINER_VERSION` key) to **devkit 1.6.0**:

- **Trunk workflow model** (repo was already main-only; dead `sync-main-to-dev.yml` pruned) and **direnv delivery** — new `flake.nix`/`.envrc`, old `.devcontainer/` pruned. `flake.lock` pins `vigos` to the 1.6.0 release commit.
- Full MIGRATION.md 0.3.x checklist. The preserved `.pre-commit-config.yaml` was a stale 0.3.1 copy with zero repo customization, so it was refreshed to the 1.6.0 template (trunk-rendered) — this was load-bearing: the old config left **commit-message validation and the agent-identity gate as silent no-ops**, and its upstream-repo `typos`/JSON hooks were hard-red on NixOS.
- `justfile.project` recipes now cover **both toolchains** (Cargo + uv/pytest; `test-py`/`test-rs` split; `test-rs` single-threaded because the linked HDF5 is not thread-safe).
- `flake.nix` dev shell carries the packages the workspace actually needs to build (`fontconfig`, `freetype`, `chafa`, `glib`) — the old Debian container never provided them either, so `cargo build` was broken there too. No `pkgs.hdf5`: `hdf5-metno`'s `static` feature vendors its own.
- Legacy 0.3.1 remnants the installer doesn't prune removed by hand (`.cursor/`, `dependabot.yml`, `.hadolint.yaml`, `resolve-image` action) — same installer gap as vig-os/devkit#1348.

## Verification

- `prek run --all-files` → exit 0 (verified independently after review)
- `just test` → Python 2 passed, Rust 135 unit tests passed
- **Zero scaffold drift**: re-running the 1.6.0 installer over the committed tree leaves `git status` empty

## Reviewer notes

- `.typos.toml` allowlists 7 **real pre-existing misspellings** in h5v identifiers (`DatasetPlotingData`, `LineSerie`, …) with a commented rename map — renaming is a source refactor out of scope here (follow-up issue).
- `just lint` (clippy) fails on 3 pre-existing deny-by-default lints — two of them (`image_preview.rs:1249`/`:1261`, "operation will always return zero") look like real bugs (follow-up issue). CI's gates run `prek`/`just test`, not `just lint`, so this does not block.
- `crates/fd5`'s 12 conformance tests need fixtures that don't exist in the repo; excluded from `just test` (follow-up issue).

## Post-merge follow-ups (GitHub-side)

1. Disable default code-scanning setup (Settings → Code security) or the advanced CodeQL config's SARIF uploads will reject (devkit #1025).
2. First release needs the one-time manual-promote runbook (devkit MIGRATION.md) — the repo has never released, `promote-release.yml` isn't dispatchable until it lands on `main`.
3. `renovate.json` enables no `cargo` manager — Rust deps are never updated (follow-up issue).

Closes #1


---
---

# Comments (3)

## [Comment #1](https://github.com/vig-os/h5v/pull/2#issuecomment-5214452214) by [@c-vigo](https://github.com/c-vigo)

_Posted on August 7, 2026 at 08:22 AM_

CI triage of the first run (31160809242): **Tests** failed on the unwrapped-gcc PATH-order bug now filed as vig-os/devkit#1351 — fixed consumer-side in `2b95e50` (absolute `CC`/`CXX` from the shellHook; verified by rebuilding `hdf5-metno-src` under a reversed store PATH). **Dependency Review** failed because the org creates repos with the dependency graph disabled (devkit MIGRATION.md provisioning step) — enabled via `gh api -X PUT repos/vig-os/h5v/vulnerability-alerts`. Both should be green on the re-run.

---

## [Comment #2](https://github.com/vig-os/h5v/pull/2#issuecomment-5215050507) by [@c-vigo](https://github.com/c-vigo)

_Posted on August 7, 2026 at 09:02 AM_

cc @gerchowl — heads-up: this migrates h5v from the legacy devkit 0.3.1 scaffold to 1.6.0 (trunk workflow, direnv delivery; details and judgment calls in the PR description). Also worth your eyes: the follow-up issues it surfaced — #3 flags two clippy `always returns zero` findings in `image_preview.rs` that look like real bugs, and #4 covers the fd5 conformance suite's missing fixtures. The typos allowlist in `.typos.toml` carries a rename map for pre-existing misspelled identifiers (#5) if you'd rather fix them at the source.

---

## [Comment #3](https://github.com/vig-os/h5v/pull/2#issuecomment-5869184229) by [@c-vigo](https://github.com/c-vigo)

_Posted on September 28, 2026 at 11:44 AM_

Closed as a side effect of renaming the head branch to \`chore/1-upgrade-devkit-1-17-0\` (the GitHub branch-rename API closes a PR whose head ref it replaces rather than retargeting it). No work was lost — the branch and all five commits are intact at \`2b95e50\`.

Superseded by a single PR that carries this branch all the way to devkit **1.17.0** (released 2026-09-28) instead of stopping at 1.6.0, since 1.6.0 was never merged and is now eleven releases stale. Continues to track #1.

Carrying forward the two notes from this thread:

- **Provisioning (done, one-time):** the dependency graph was disabled at repo creation, which failed **Dependency Review**; enabled via \`gh api -X PUT repos/vig-os/h5v/vulnerability-alerts\`.
- **The \`Tests\` failure** was the unwrapped-gcc PATH-order bug, filed upstream as vig-os/devkit#1351 and fixed consumer-side here in \`2b95e50\`. devkit **fixed it upstream in 1.7.0** (#1351 reverses the \`GITHUB_PATH\` write order) and **#1358 then added \`CC\`/\`CXX\` to the env-forward denylist**, naming this repo's workaround explicitly as superseded. So \`2b95e50\` is inert on CI from 1.7.0 on and is reverted in the new PR.

---
---

## Commits

### Commit 1: [5b1b49e](https://github.com/vig-os/h5v/commit/5b1b49e30947bcfb802f107a68307b5613cfcdd8) by [c-vigo](https://github.com/c-vigo) on August 7, 2026 at 08:12 AM
chore(repo): adopt devkit 1.6.0 scaffold (trunk, direnv), 12183 files modified

### Commit 2: [731d7f5](https://github.com/vig-os/h5v/commit/731d7f508cc13fa92e62b7da5058e92142a7236d) by [c-vigo](https://github.com/c-vigo) on August 7, 2026 at 08:12 AM
style: strip trailing whitespace and stray final blank lines, 7 files modified (LICENSE, h5v/src/error.rs, h5v/src/ui/app.rs, h5v/src/ui/attributes.rs)

### Commit 3: [974c26d](https://github.com/vig-os/h5v/commit/974c26d24fe8589028f5dc539bd4b70af60e6edc) by [c-vigo](https://github.com/c-vigo) on August 7, 2026 at 08:12 AM
chore(repo): migrate the project files to the 1.6.0 toolchain, 86 files modified (.gitignore, .gitignore.project, flake.nix, justfile.project)

### Commit 4: [7edb5fa](https://github.com/vig-os/h5v/commit/7edb5fa63fa3acd85a2622faf2fc9e3a8e145c88) by [c-vigo](https://github.com/c-vigo) on August 7, 2026 at 08:12 AM
chore(repo): drop legacy 0.3.1 scaffold remnants, 3783 files modified

### Commit 5: [2b95e50](https://github.com/vig-os/h5v/commit/2b95e5006d49bb6393f76f95333c5a7993594527) by [c-vigo](https://github.com/c-vigo) on August 7, 2026 at 08:21 AM
fix(flake): pin wrapped C toolchain so CI PATH order cannot break C builds, 14 files modified (flake.nix)
