# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

- **Upgrade the vigOS devkit scaffold from 0.3.1 to 1.6.0** ([#1](https://github.com/vig-os/h5v/issues/1))
  - Delivery mode switched from `devcontainer` to `direnv`: the dev environment
    now comes from `flake.nix` + `.envrc` (`direnv allow`, or `nix develop`),
    and the stale `.devcontainer/` was pruned. The Rust, CMake and pkg-config
    toolchains the old `Containerfile.h5v` installed are now declared in the
    flake's `extraPackages`, together with the native libraries the workspace
    links against (fontconfig, freetype, chafa, glib) — which the container
    never provided, so `cargo build` now works out of the box.
  - Workflow model set to `trunk` (`DEVKIT_WORKFLOW=trunk`): topic branches and
    release branches target `main`, and the dead `sync-main-to-dev.yml` is gone.
  - Refreshed the whole managed scaffold: CI, CodeQL, Scorecard, sync-issues and
    the four-workflow release pipeline, plus new `promote-release.yml`,
    `devkit-upgrade.yml`, Renovate changelog automation, `.claude/` agent skills,
    `SECURITY.md`, `.typos.toml` and `zizmor.yml`.
  - The hook runner is now `prek` (the `pre-commit` binary is gone from the
    image); `.pre-commit-config.yaml` gained the commit-message, agent-identity
    and `nixfmt` hooks it had been missing, and `just lint`/`format`/`test`/
    `sync` now cover the Rust workspace as well as the Python package.

### Deprecated

### Removed

- **Legacy 0.3.1 scaffold remnants** ([#1](https://github.com/vig-os/h5v/issues/1))
  - `.cursor/` (superseded by `.claude/`), `.github/dependabot.yml` (superseded
    by Renovate, and it targeted the now-absent `dev` branch), `.hadolint.yaml`
    (no Containerfile left to lint) and the unreferenced
    `.github/actions/resolve-image` (superseded by `resolve-toolchain`).

### Fixed

### Security
