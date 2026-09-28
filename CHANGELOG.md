# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

- **Sync issues and PRs to the `sync/issue-mirror` branch instead of `main`** ([#9](https://github.com/vig-os/h5v/issues/9))
  - `DEVKIT_SYNC_TARGET=sync/issue-mirror` in `.vig-os`, so the nightly
    `sync-issues.yml` push no longer depends on `main` accepting a direct push
    from the Commit App, which a require-PR ruleset on `main` refuses. The job
    creates the mirror from `main` on its first run.
  - The release train folds the mirror's `docs/issues` and `docs/pull-requests`
    archive into each final release, and resets the mirror onto `main` after
    promotion so it does not drift without bound.

- **Upgrade the vigOS devkit scaffold from 0.3.1 to 1.17.0** ([#1](https://github.com/vig-os/h5v/issues/1))
  - Delivery mode switched from `devcontainer` to `direnv`: the dev environment
    now comes from `flake.nix` + `.envrc` (`direnv allow`, or `nix develop`),
    and the stale `.devcontainer/` was pruned. The Rust, CMake and pkg-config
    toolchains the old `Containerfile.h5v` installed are now declared in the
    flake's `extraPackages`, together with the native libraries the workspace
    links against (fontconfig, freetype, chafa, glib) — which the container
    never provided, so `cargo build` now works out of the box.
  - Workflow model set to `trunk` (`DEVKIT_WORKFLOW=trunk`): topic branches and
    release branches target `main`, and the dead `sync-main-to-dev.yml` is gone.
    `prepare-hotfix.yml` is likewise not shipped — it is gitflow-only.
  - Refreshed the whole managed scaffold: CI, CodeQL, Scorecard, sync-issues,
    the release pipeline plus `promote-release.yml` and `abandon-release.yml`,
    `devkit-upgrade.yml`, `.claude/` agent skills, `SECURITY.md`, `.typos.toml`
    and `zizmor.yml`. Managed CI jobs now run on `ubuntu-26.04`.
  - The hook runner is now `prek` (the `pre-commit` binary is gone from the
    image); `.pre-commit-config.yaml` gained the commit-message, agent-identity
    and `nixfmt` hooks it had been missing, plus `actionlint` and
    `shellcheck-composite-actions` — so this repo's workflows and composite
    actions are linted, which previously nothing did. `just lint`/`format`/
    `test` now cover the Rust workspace.
  - `flake.nix` reads the `.vig-os` commit/branch policy knobs
    (`DEVKIT_BRANCH_TYPES`, `DEVKIT_COMMIT_TYPES`, `DEVKIT_REFS_POLICY`,
    `DEVKIT_REFS_OPTIONAL_TYPES`), so the flake-generated hooks, the scaffolded
    config and CI now agree from one source. All four are at their defaults.
  - The `vigos` flake input is **pinned** to `?ref=1.17.0` rather than floating
    on devkit's default branch, keeping it in lockstep with `DEVKIT_VERSION`.
  - Markdown linting no longer runs the MD029/MD031/MD046 fixers, whose
    rewrites change document meaning (vig-os/devkit#1574).

### Deprecated

### Removed

- **The unused Python scaffold surface** ([#1](https://github.com/vig-os/h5v/issues/1))
  - `pyproject.toml`, `uv.lock`, `src/h5v/__init__.py` and `tests/` were devkit
    0.3.1 template residue, never developed: a package docstring reading
    "A new Python project", a `test_example()` asserting `True`, and the
    scaffold's own `# noqa: F401 - renamed to project name by
    init-workspace.sh` placeholder marker. h5v is a Rust workspace (`h5v`
    binary + `crates/fd5`); the three `.py` files were its entire Python
    content.
  - Dropping them before the re-scaffold keeps `DEVKIT_LANGUAGES` seeded as
    `rust` alone. That key is a sticky *declaration*, never auto-removed, and
    CI fails when a declared language's marker file is missing — so a
    `pyproject.toml` left in place only to be deleted later would have pinned a
    permanent gate on a file this repo does not want.
  - Everything that referenced the surface guards on `[ -f pyproject.toml ]`
    (the `justfile.project` recipes, `setup-devkit-toolchain`'s Python/uv env
    per devkit #1028), so it all no-ops rather than breaking.

- **Legacy 0.3.1 scaffold remnants** ([#1](https://github.com/vig-os/h5v/issues/1))
  - `.cursor/` (superseded by `.claude/`), `.github/dependabot.yml` (superseded
    by Renovate, and it targeted the now-absent `dev` branch), `.hadolint.yaml`
    (no Containerfile left to lint) and the unreferenced
    `.github/actions/resolve-image` (superseded by `resolve-toolchain`).
  - `renovate-changelog-build.yml` and `renovate-changelog-commit.yml`, retired
    in devkit 1.8.0 in favor of release-time synthesis (vig-os/devkit#1423).

### Fixed

- **Drop the local C-toolchain workaround, fixed upstream** ([#1](https://github.com/vig-os/h5v/issues/1))
  - `flake.nix` exported absolute `cc-wrapper` paths as `CC`/`CXX` to stop the
    unwrapped `gcc` from shadowing the wrapper in CI, which broke the vendored
    HDF5 CMake build. devkit fixed the underlying `GITHUB_PATH` ordering in
    1.7.0 (vig-os/devkit#1351) and then denylisted `CC`/`CXX` from the
    shellHook env forward (vig-os/devkit#1358), so the workaround had been
    inert on CI since. Verified by a clean `cargo build --workspace`, vendored
    HDF5 included.

### Security
