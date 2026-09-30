---
type: issue
state: closed
created: 2026-09-29T11:16:17Z
updated: 2026-09-29T13:07:46Z
author: c-vigo
author_url: https://github.com/c-vigo
url: https://github.com/vig-os/h5v/issues/12
comments: 1
labels: chore
assignees: none
milestone: none
projects: none
parent: none
children: none
synced: 2026-09-30T08:16:00.333Z
---

# [Issue 12]: [chore(deps): enable the Renovate cargo manager](https://github.com/vig-os/h5v/issues/12)

### Chore Type

Configuration change

### Description

Renovate never proposes updates for the Rust dependencies. `renovate.json` sets `enabledManagers` to `["github-actions", "pep621", "npm"]`, which leaves out `cargo`. The repo has no `pyproject.toml` or `package.json`, so `pep621` and `npm` extract nothing.

The org is moving vulnerability-fix PRs from Dependabot security updates to Renovate (vig-os/org-config#307). Renovate only opens a vulnerability PR for a dependency that an enabled manager extracts, so without `cargo` no Rust advisory would ever get a PR.

This is item 2 of #5, split out so it can land on its own.

### Acceptance Criteria

- [ ] `enabledManagers` is `["github-actions", "cargo"]`
- [ ] `renovate-config-validator --strict renovate.json` passes

### Implementation Notes

The shared preset already enables weekly `lockFileMaintenance`. With `cargo` enabled it also regenerates `Cargo.lock`, which covers in-range transitive bumps such as the open Dependabot PR #11 (rand).

### Related Issues

Part of #5 (item 2). Context: vig-os/org-config#307.

---

# [Comment #1]() by [c-vigo]()

_Posted on September 29, 2026 at 01:07 PM_

Done in #13 (merged to main).

