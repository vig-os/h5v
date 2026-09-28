---
type: issue
state: closed
created: 2026-08-07T13:05:25Z
updated: 2026-09-28T12:28:15Z
author: c-vigo
author_url: https://github.com/c-vigo
url: https://github.com/vig-os/h5v/issues/6
comments: 3
labels: chore
assignees: none
milestone: none
projects: none
parent: none
children: none
synced: 2026-09-28T20:28:46.985Z
---

# [Issue 6]: [chore(ci): bump devkit to 1.6.0 (retires numeric App-ID scaffolds)](https://github.com/vig-os/h5v/issues/6)

## Context

A 2026-08-07 fleet audit of GitHub-App credentials across `vig-os` and `exo-pet`
concluded that every App secret pair can be consolidated to **Client ID only**.
Nothing in the auth path is numerically load-bearing: `@octokit/auth-app`
accepts a client-ID string (`Iv23li…`) wherever it accepts a numeric App ID, on
every pinned action version in use.

`h5v` is one of two repos blocking the retirement of the numeric org secrets,
because it still runs a **0.3.1-era devkit scaffold** whose workflows are all
written in the `app-id: ${{ secrets.*_APP_ID }}` style.

> **Relationship to #1.** #1 already tracks the mechanics of the
> `0.3.1 -> 1.6.0` scaffold bump (direnv, trunk). This issue records the
> *credential* requirement that bump has to satisfy and the fleet-level
> dependency it unblocks. If it is simpler to fold this into #1, do that and
> close this as covered — just keep the acceptance criteria below.

## Current state on `main` (verified)

Every App token is minted with `actions/create-github-app-token@f8d387b68d61c58ab83c6c016672934102569859`
(**v3.0.0** — predates the `client-id` input, which landed in **v3.1.0**), so the
numeric IDs are not merely stylistic here: the pinned action *cannot* take a
client ID. **13 numeric-ID references across 6 workflows:**

| Workflow | Lines | Secret |
|---|---|---|
| `.github/workflows/prepare-release.yml` | `:166`, `:173` | `COMMIT_APP_ID`, `RELEASE_APP_ID` |
| `.github/workflows/release-core.yml` | `:121`, `:351`, `:358`, `:535` | `RELEASE_APP_ID` ×3, `COMMIT_APP_ID` ×1 |
| `.github/workflows/release-publish.yml` | `:96` | `RELEASE_APP_ID` |
| `.github/workflows/release.yml` | `:140`, `:148` | `RELEASE_APP_ID`, `COMMIT_APP_ID` |
| `.github/workflows/sync-issues.yml` | `:83`, `:126` | `COMMIT_APP_ID` ×2 |
| `.github/workflows/sync-main-to-dev.yml` | `:128`, `:160` | `COMMIT_APP_ID`, `RELEASE_APP_ID` |

`sync-issues.yml:124` additionally pins `vig-os/sync-issues-action@bad447d33…`
(v0.2.2), which has no `client-id` input either.

Totals: `COMMIT_APP_ID` ×6, `RELEASE_APP_ID` ×7.

## Why the devkit bump is the fix

devkit **1.6.0** already stamps client-ID-style workflows for the Release App
(`RELEASE_APP_CLIENT_ID`) and most of the Commit App path, on a
`create-github-app-token` pin that supports `client-id`. Bumping the scaffold
converts all 13 references in one move — there is no reason to hand-patch them.

The remaining sync-issues holdout in the scaffold is being fixed separately in
vig-os/devkit#1365 (which depends on vig-os/sync-issues-action#168); if the
bump lands before that release, `sync-issues.yml` will still carry
`COMMIT_APP_ID` and will pick up the client-ID form on the next devkit bump.
That is fine and expected — it does not block this work.

## Acceptance criteria

- [ ] `h5v` is on the devkit 1.6.0 scaffold (mechanics tracked in #1).
- [ ] No `RELEASE_APP_ID` reference remains in `.github/workflows/`.
- [ ] `COMMIT_APP_ID` remains **only** where the current devkit scaffold still
      requires it (`sync-issues.yml`), and is called out here so the org-secret
      retirement is not attempted prematurely.
- [ ] `create-github-app-token` is pinned to a SHA at or above v3.1.0 everywhere.
- [ ] A release and a sync-issues run are exercised (or dry-run) on the new
      scaffold before the org secrets are touched.

## Dependency / blast radius

**This blocks retirement of the `RELEASE_APP_ID` and `COMMIT_APP_ID` org secrets
in `vig-os`.** Migration principle, no exceptions: *no numeric `*_APP_ID` secret
is deleted while any pinned workflow still references it.* Cautionary precedent
— `exo-pet/playground-carlos`'s sync-issues job broke **silently for a week**
when `COMMIT_APP_ID` was unavailable: the job kept reporting success while
syncing nothing. Deleting `RELEASE_APP_ID` while this repo is on the old
scaffold would break its release train the same way.

Related: vig-os/scitadel#208 (the other old-scaffold repo),
vig-os/devkit#1365, vig-os/sync-issues-action#168.

---

# [Comment #1]() by [c-vigo]()

_Posted on August 7, 2026 at 01:08 PM_

Cross-reference correction: the sibling old-scaffold issue is **vig-os/scitadel#209** (the body above says #208, which was a placeholder written before the issue was filed). The scitadel devkit bump itself is vig-os/scitadel#207.

Full sibling set for this migration: vig-os/sync-issues-action#168, vig-os/devkit#1365, vig-os/scitadel#209, vig-os/tessera#364, exo-pet/org-config#20.

---

# [Comment #2]() by [c-vigo]()

_Posted on September 28, 2026 at 12:26 PM_

Resolved by #7 (devkit 0.3.1 -> 1.17.0). No `RELEASE_APP_ID` or `COMMIT_APP_ID` references remain in `.github/workflows/`: every `create-github-app-token` step is pinned to `bcd2ba4…` (v3, with `client-id` support) and uses `*_APP_CLIENT_ID`. `sync-issues.yml` is on `sync-issues-action@v0.5.0` with `client-id` too, so the `COMMIT_APP_ID` holdout this issue expected is gone as well.

Not yet exercised: no sync-issues or release run has happened on the new scaffold since the merge. Confirm one succeeds before retiring the numeric org secrets.

---

# [Comment #3]() by [c-vigo]()

_Posted on September 28, 2026 at 12:28 PM_

The devkit bump landed in #7 (0.3.1 → **1.17.0**, not 1.6.0 — 1.6.0 was never merged and went eleven releases stale). Verified on `main` at `27446cc`: **all 13 numeric `*_APP_ID` references across the 6 workflows are gone.** `COMMIT_APP_ID` and `RELEASE_APP_ID` now have zero references anywhere in `.github/`, replaced by `COMMIT_APP_CLIENT_ID` / `RELEASE_APP_CLIENT_ID` on `actions/create-github-app-token@bcd2ba49218906704ab6c1aa796996da409d3eb1` (v3, which takes `client-id`). `sync-issues.yml` is on a client-ID-capable `sync-issues-action` pin too.

One numeric reference remains, and it is not a blocker: `devkit-upgrade.yml` reads `secrets.DEVKIT_UPGRADE_APP_ID` as an `APP_ID_LEGACY` **fallback**, with the scaffold noting either value is accepted this release. It is a compatibility path, not a requirement, and it is a different App from the two this issue is about.

So the repo-side acceptance criteria look met and `h5v` should no longer block retiring the numeric org secrets. Leaving this open rather than closing it, since the actual secret retirement is an org-level action in `vig-os` and the other blocking repo needs confirming too.

Also opened #8 for the Rust language pack this migration made available (devkit 1.9.0's `rust` module + `lib.mkRustProject`), blocked by #3.

