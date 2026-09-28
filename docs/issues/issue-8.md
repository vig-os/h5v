---
type: issue
state: open
created: 2026-09-28T12:27:31Z
updated: 2026-09-28T12:27:31Z
author: c-vigo
author_url: https://github.com/c-vigo
url: https://github.com/vig-os/h5v/issues/8
comments: 0
labels: chore
assignees: none
milestone: none
projects: none
parent: none
children: none
synced: 2026-09-28T20:28:46.348Z
---

# [Issue 8]: [chore(flake): adopt devkit's Rust language pack (rust module + lib.mkRustProject)](https://github.com/vig-os/h5v/issues/8)

## Context

The devkit 0.3.1 → 1.17.0 migration (#1, PR #7) deliberately left this out to
keep the scaffold bump reviewable. It is now the largest remaining gap between
what this repo does by hand and what the toolchain offers.

`flake.nix` currently hand-rolls its Rust toolchain in `extraPackages`:

```nix
pkgs.rustc pkgs.cargo pkgs.clippy pkgs.rustfmt
pkgs.cmake pkgs.pkg-config
pkgs.fontconfig pkgs.freetype pkgs.chafa pkgs.glib
```

devkit **1.9.0** shipped a Rust language pack
([vig-os/devkit#1400](https://github.com/vig-os/devkit/issues/1400),
[#1427](https://github.com/vig-os/devkit/issues/1427)) that replaces the first
line and adds a great deal more. Its `crane` and `fenix` inputs are **already in
our `flake.lock`** — every consumer carries them since 1.9.0 — so we are paying
the cost of the pack today and getting none of the benefit.

## What adopting it gives us

- **`rust` capability module** (`nix/modules/rust.nix`): toolchain plus curated
  cargo tooling on the dev-shell PATH — `nextest`, `cargo-deny`,
  `cargo-auditable`, `cargo-audit`, `cargo-about`, `cargo-shear` by default,
  extensible via `tools`, with `mold` picked up on Linux.
- **`lib.mkRustProject`** (`nix/mk-rust-project.nix`): one call returning
  `{ devShell, checks, packages, craneLib, cargoArtifacts, commonArgs,
  toolchain, src }`, wiring the shell, the check suite (fmt, clippy, nextest,
  `cargo-doc`, `doctest`, `cargo-deny` when a `deny.toml` exists) and per-crate
  builds together. It folds well-known root configs (`rustfmt.toml`,
  `clippy.toml`, `deny.toml`, `.cargo/`, `rust-toolchain.toml`) into the crane
  fileset unconditionally, so their absence from the sandbox cannot silently
  turn the checks into a rules-nobody-wrote green.
- **`checks.doctest`** — `cargo test --doc`, which nextest cannot run and
  `cargoDoc` does not. We currently run no doctests at all.
- **Tool groups + a deterministic ratchet**: `tools = [ "@perf" ]` etc., and
  `checks.perf-ratchet` (auto-enabled when `.repo/perf-baseline.toml` exists)
  which measures shipped binary size and dependency-graph size from
  `Cargo.lock` and deliberately times nothing — no benchmark needs authoring.
  Plausibly interesting for the TUI's release profile (`lto = "fat"`,
  `panic = "abort"`).

Note the `checks` option is **mandatory and has no default**: a hand-written
`modules = [ "rust" ]` fails at eval with a message naming `mkRustProject` and
the deliberate toolchain-only opt-out (`{ name = "rust"; checks = "none"; }`).
That is by design — a silently toolchain-only Rust shell is the failure the pack
exists to prevent.

## Blocked by #3

`mkRustProject`'s clippy check runs with **`--deny warnings`**. #3 records two
`always returns zero` findings in `image_preview.rs` that look like real bugs,
and `cargo clippy --workspace --all-targets` reports more. Adopting the pack
turns all of those into a red `nix flake check`, so #3 lands first.

## Scope

- [ ] Fix #3 (prerequisite).
- [ ] Replace the `extraPackages` Rust toolchain entries with the `rust` module
      via `lib.mkRustProject`; keep the native/library entries (`cmake`,
      `pkg-config`, `fontconfig`, `freetype`, `chafa`, `glib`) unless the
      `native` module covers them — check `nix/modules/native.nix`.
- [ ] Keep the vendored HDF5 build working. `hdf5-metno`'s `static` feature
      builds the C library from source, and `crane`'s sandbox is stricter than a
      plain `cargo build` — this is the main integration risk, not the toolchain
      swap. A stale CMake cache in `target/` also masquerades as a real failure
      here (seen during #1: CMake reports `CMAKE_C_COMPILER` changed, then
      `add_subdirectory given source "test"`), so verify with a clean tree.
- [ ] Decide whether the `justfile.project` Rust recipes stay as-is or defer to
      the pack's checks. Note `test-rs` pins `--test-threads=1` because the HDF5
      C library is not built thread-safe; nextest's process-per-test model may
      make that constraint unnecessary, which is worth measuring rather than
      assuming.
- [ ] Add a `deny.toml` if we want `cargo-deny` in the check suite.
- [ ] Consider `tools = [ "@perf" ]` and sealing a `perf-baseline.toml` via
      `packages.perf-seal` (follow-up, not required here).

## Acceptance

- `nix flake check` green, including `fmt`, `clippy --deny warnings`, `nextest`,
  `doctest` and `cargo-doc`.
- `cargo build --workspace` still builds the vendored HDF5 from a clean tree.
- The dev shell still provides everything the TUI links against (chart previews
  via the plotters font stack, image previews via libchafa).

## Refs

- devkit Rust pack: vig-os/devkit#1400, vig-os/devkit#1427
- Consumer hardening from the second consumer: vig-os/devkit#1450
- Perf tooling + ratchet: vig-os/devkit#1440
- ADR on why the v1 module contract does not carry `checks`:
  `docs/rfcs/ADR-capability-modules.md` in devkit

