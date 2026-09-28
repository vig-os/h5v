---
type: pull_request
state: closed (merged)
branch: chore/1-upgrade-devkit-1-17-0 → main
created: 2026-09-28T12:10:20Z
updated: 2026-09-28T12:23:24Z
author: c-vigo
author_url: https://github.com/c-vigo
url: https://github.com/vig-os/h5v/pull/7
comments: 0
labels: none
assignees: none
milestone: none
projects: none
merged: 2026-09-28T12:22:29Z
synced: 2026-09-28T20:28:51.933Z
---

# [PR 7](https://github.com/vig-os/h5v/pull/7) chore(repo): upgrade devkit scaffold 0.3.1 -> 1.17.0 (trunk, direnv)

Migrates `h5v` from the legacy devkit **0.3.1** scaffold straight to **1.17.0**
(released 2026-09-28), in `direnv` delivery mode under the `trunk` workflow
model. Closes #1.

Supersedes #2, which carried the same branch to 1.6.0 in August but was never
merged; 1.6.0 is now eleven releases stale, so this goes to the current release
in one landing instead. #2 was closed as a side effect of renaming the head
branch — no work was lost, and its two triage notes are carried over there.

## Why retarget the branch rather than restart from `main`

`main`'s 0.3.1-era `.pre-commit-config.yaml` carries the pre-devkit#1170
`pymarkdown` block with a **hand-extended `exclude:`**. The automatic fold only
fires on text byte-identical to what devkit shipped, so a fresh branch would
inherit the broken block and get a warning instead of a fix — and that block
breaks `just precommit`, every local markdown commit, and the `devkit-upgrade`
commit step. Restarting would also re-incur the whole 0.3.x manual checklist
(`pre-commit`→`prek` renames, base-recipe fold, `.devcontainer/`/`.cursor/`/
`.hadolint.yaml` pruning) and discard the preserved-file work already on this
branch: `.gitignore.project` (absent on `main`), the `.typos.toml` allowlist,
the `justfile.project` Rust recipes and the `flake.nix` `extraPackages` set.

## Commits

| Commit | What |
|---|---|
| `f40ece5` | Drop the unused Python scaffold surface |
| `5e5d631` | Port the `.vig-os` knob readers into `flake.nix`; pin `vigos` to 1.17.0 |
| `2cdd678` | Regenerate the managed scaffold at 1.17.0 (`install.sh --force` output) |
| `93af989` | Fold the 1.17.0 template evolution into the preserved files |
| `77d190a` | Changelog |

Ordering is deliberate: the Python removal lands **before** the re-scaffold so
`DEVKIT_LANGUAGES` seeds `rust` alone, and the flake pin lands before it too, so
the installer reported `flake-bump: skipped — input 'vigos' is pinned to
'1.17.0'` and the lock was never advanced to devkit `main`. That also avoids
advancing the scaffold ahead of the flake input, which is devkit#1093's
documented breakage.

## Judgment calls worth a reviewer's eye

**The local C-toolchain fix is reverted.** `2b95e50` exported absolute
`cc-wrapper` paths as `CC`/`CXX` to work around vig-os/devkit#1351. devkit fixed
that upstream in 1.7.0 and **#1358 then added `CC`/`CXX` to the env-forward
denylist, naming this repo's workaround as deliberately superseded** — so it has
not reached CI since 1.7.0. Keeping it would be dead code that reads like
load-bearing infrastructure. Verified by a clean `cargo build --workspace`
(1m51s, vendored HDF5 included) and 133/133 tests.

**`pyproject.toml` and friends are gone.** They were 0.3.1 template residue: a
docstring reading "A new Python project", a `test_example()` asserting `True`,
and the scaffold's own `# noqa: F401 - renamed to project name by
init-workspace.sh` marker — three `.py` files, no development. Removing them
before the re-scaffold matters because `DEVKIT_LANGUAGES` is a *sticky
declaration* that CI gates on and an upgrade never un-declares.

**`DEVKIT_COMMIT_APP_ENVIRONMENT` is left unset.** It would bind the commit-App
token-minting jobs to a deployment environment so the App credentials stop being
org/repo secrets readable from any branch — but that closes a
branch-protection *bypass*, and `main` here carries no ruleset
(`repos/vig-os/h5v/rulesets` → `[]`; `vig-os` is on Free, where org rulesets are
unavailable). It becomes the right move alongside a ruleset, and the environment
must exist first or a bound job auto-creates an unprotected one.

**`.pymarkdown` now disables MD029/MD031/MD046** (vig-os/devkit#1574). The hook
runs `fix`, so an enabled rule is permission to rewrite: MD031 dumps the second
of two consecutive fenced list items to column 0 and **exits "success"**, MD029
renumbers deliberate continuation numbering, MD046 deletes fence markers.

**Two template changes skipped on purpose:** the `tatus`/`fnd`/`mis` typos
entries and the `^assets/guardrails/` shellcheck exclude both exist for devkit's
own vendored guardrails tree (#1488), which this repo has no equivalent of. The
`dev` clause in the template's branch guard is also not folded — this repo is
trunk.

**Three preserved files refreshed wholesale.** `CODEOWNERS` and both release
extension seams are preserved to protect customization and carried none: each
differed from its template only by the banner the 0.3.1 scaffold stripped.
`release-extension.yml` gains `permissions: contents: read`, which it had been
missing entirely, and both seams move off stale pinned runners (`ubuntu-22.04`,
`ubuntu-24.04`) onto `ubuntu-26.04`.

## What changed in the scaffold

Added `abandon-release.yml`, `.github/actionlint.yaml`, `.claude/settings.json`.
Pruned `renovate-changelog-build.yml` and `renovate-changelog-commit.yml`
(retired in 1.8.0 for release-time synthesis, #1423; removed by the #1348
retired-path manifest, gated on the pre-run 1.6.0 pin). `prepare-hotfix.yml` is
*not* added — gitflow-only, copy-excluded under trunk, like
`sync-main-to-dev.yml`. Managed jobs move to `ubuntu-26.04`.

Two hooks were auto-inserted into the preserved config (#1654) because this tree
predated them: **`actionlint`** (1.16.0, #1660) and
**`shellcheck-composite-actions`** (1.17.0, #1704). Both now pass — meaning this
repo's workflows and composite action `run:` bodies are linted, which nothing was
doing before. No `preserved-hook-drift` and no fold were reported.

## Verification

Full `prek run --all-files` green (exit 0), clean `cargo build --workspace`,
`just test` 133 passed / 0 failed.

⚠️ **After pulling this, reload direnv** (or re-enter `nix develop`). The lock
advanced, and a shell entered on the old lock has a `vig-utils` without
`shellcheck-composite-actions`, so that hook fails to spawn.

## Not in scope

- Adopting devkit's `rust` capability module / `lib.mkRustProject` (#1400/#1427,
  shipped 1.9.0) — tracked separately once this lands; `clippy --deny warnings`
  makes #3 a prerequisite.
- #5's hygiene follow-ups (`renovate.json` missing the `cargo` manager, the
  `.typos.toml` rename map, README image links).



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

### Commit 6: [f40ece5](https://github.com/vig-os/h5v/commit/f40ece51cad56de28339a7eea13f5c5a02233e36) by [c-vigo](https://github.com/c-vigo) on September 28, 2026 at 11:47 AM
chore(repo): drop the unused Python scaffold surface, 2388 files modified (CHANGELOG.md, justfile.project, pyproject.toml, src/h5v/__init__.py, tests/__init__.py, tests/test_example.py, uv.lock)

### Commit 7: [5e5d631](https://github.com/vig-os/h5v/commit/5e5d631b45308c8cdc95e123997aa61e9b3459e2) by [c-vigo](https://github.com/c-vigo) on September 28, 2026 at 11:56 AM
chore(flake): port the .vig-os knob readers and pin vigos to 1.17.0, 197 files modified (flake.lock, flake.nix)

### Commit 8: [2cdd678](https://github.com/vig-os/h5v/commit/2cdd678b48e2f4931d2c6320b4024327cac366d6) by [c-vigo](https://github.com/c-vigo) on September 28, 2026 at 12:00 PM
chore(repo): regenerate the managed scaffold at devkit 1.17.0, 2894 files modified

### Commit 9: [93af989](https://github.com/vig-os/h5v/commit/93af98928c0564df1e19de292491cc86f8438d2b) by [c-vigo](https://github.com/c-vigo) on September 28, 2026 at 12:03 PM
chore(repo): fold the 1.17.0 template evolution into the preserved files, 89 files modified (.github/CODEOWNERS, .github/workflows/prepare-release-extension.yml, .github/workflows/release-extension.yml, .pre-commit-config.yaml, .pymarkdown, .pymarkdown.config.md)

### Commit 10: [77d190a](https://github.com/vig-os/h5v/commit/77d190a51b15fcf64930016fffae6ab43d99fa4b) by [c-vigo](https://github.com/c-vigo) on September 28, 2026 at 12:09 PM
docs(changelog): describe the 0.3.1 -> 1.17.0 upgrade, 36 files modified (CHANGELOG.md)
