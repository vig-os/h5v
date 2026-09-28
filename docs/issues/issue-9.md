---
type: issue
state: closed
created: 2026-09-28T19:51:37Z
updated: 2026-09-28T20:27:01Z
author: c-vigo
author_url: https://github.com/c-vigo
url: https://github.com/vig-os/h5v/issues/9
comments: 0
labels: chore
assignees: c-vigo
milestone: none
projects: none
parent: none
children: none
synced: 2026-09-28T20:28:45.678Z
---

# [Issue 9]: [chore: sync issues to a mirror branch instead of protected main](https://github.com/vig-os/h5v/issues/9)

## Context

vig-os/org-config#300 (part of vig-os/org-config#294, ADR-0008) adds a `Main protection` ruleset to this repo. The ruleset requires a PR with 1 approval and `CI Summary`. The only actor that can bypass it is `#OrganizationAdmin`, and only through a PR.

With `DEVKIT_SYNC_TARGET` empty in `.vig-os`, the scaffolded `sync-issues.yml` resolves to `main` on this trunk repo. It pushes directly as the Commit App (`commit-action-bot`). The new ruleset refuses that push (vig-os/devkit#1227), so **the nightly issue sync fails from the moment #300 is applied** and keeps failing until this issue is fixed.

We deliberately chose not to give `commit-action-bot` a bypass on `main`. The sync should target a mirror branch instead, as `vig-os/org-config` does.

## Task

- [ ] Set `DEVKIT_SYNC_TARGET=sync/issue-mirror` in `.vig-os`, matching `vig-os/org-config`.
- [ ] Re-scaffold so the sync workflow picks it up. Per the `.vig-os` comments, sync settings are realised at scaffold time (vig-os/devkit#1228).
- [ ] Confirm a sync run succeeds. The job bootstraps `sync/issue-mirror` from `main` if the branch is absent.

## Also noticed

Two `sync-issues.yml` runs dispatched on 2026-09-28 have been sitting in `queued` for hours on runner label `ubuntu-26.04`. Please check that this label is available to the repo.

