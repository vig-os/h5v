---
type: issue
state: open
created: 2026-09-29T11:58:49Z
updated: 2026-11-21T16:13:15Z
author: renovate[bot]
author_url: https://github.com/renovate[bot]
url: https://github.com/vig-os/h5v/issues/14
comments: 0
labels: none
assignees: none
milestone: none
projects: none
parent: none
children: none
synced: 2026-11-22T09:34:21.608Z
---

# [Issue 14]: [Dependency Dashboard](https://github.com/vig-os/h5v/issues/14)

This issue lists Renovate updates and detected dependencies. Read the [Dependency Dashboard](https://docs.renovatebot.com/key-concepts/dashboard/) docs to learn more.<br>[View this repository on the Mend.io Web Portal](https://developer.mend.io/github/vig-os/h5v).

## Awaiting Schedule

The following updates are awaiting their schedule. To get an update now, click on a checkbox below.

 - [ ] <!-- unschedule-branch=renovate/serde_json-1.x-lockfile -->chore(deps): update rust crate serde_json to v1.0.154
 - [ ] <!-- unschedule-branch=renovate/thiserror-2.x-lockfile -->chore(deps): update rust crate thiserror to v2.0.21
 - [ ] <!-- unschedule-branch=renovate/arboard-3.x-lockfile -->chore(deps): update rust crate arboard to v3.7.0
 - [ ] <!-- unschedule-branch=renovate/hdf5-metno-0.x -->chore(deps): update rust crate hdf5-metno to 0.15.0
 - [ ] <!-- unschedule-branch=renovate/sha2-0.x -->chore(deps): update rust crate sha2 to 0.11
 - [ ] <!-- unschedule-branch=renovate/hdf5-metno-sys-0.x -->fix(deps): update rust crate hdf5-metno-sys to 0.12.0
 - [ ] <!-- unschedule-branch=renovate/itertools-0.x -->fix(deps): update rust crate itertools to 0.15.0
 - [ ] <!-- unschedule-branch=renovate/toml-0.x -->fix(deps): update rust crate toml to 0.9
 - [ ] <!-- unschedule-branch=renovate/ratatui-image-11.x -->fix(deps): update rust crate ratatui-image to v11
 - [ ] <!-- unschedule-branch=renovate/toml-1.x -->fix(deps): update rust crate toml to v1
 - [ ] <!-- unschedule-branch=renovate/lock-file-maintenance -->chore(deps): lock file maintenance
 - [ ] <!-- create-all-awaiting-schedule-prs -->🔐 **Create all awaiting schedule PRs at once** 🔐

## Open

The following updates have all been created. To force a retry/rebase of any, click on a checkbox below.

 - [ ] <!-- rebase-branch=renovate/clap-4.x-lockfile -->[chore(deps): update rust crate clap to v4.6.9](../pull/16)
 - [ ] <!-- rebase-branch=renovate/ratatui-0.x-lockfile -->[chore(deps): update rust crate ratatui to v0.30.2](../pull/17)
 - [ ] <!-- rebase-branch=renovate/ratatui-image-10.x-lockfile -->[chore(deps): update rust crate ratatui-image to v10.0.8](../pull/18)
 - [ ] <!-- rebase-branch=renovate/serde-monorepo -->[chore(deps): update rust crate serde to v1.0.229](../pull/19)
 - [ ] <!-- rebase-all-open-prs -->**Click on this checkbox to rebase all open PRs at once**

## Detected Dependencies

<details><summary>cargo (3)</summary>
<blockquote>

<details><summary>Cargo.toml (4)</summary>

 - `hdf5-metno 0.11.0` → [Updates: `0.15.0`]
 - `sha2 0.10` → [Updates: `0.11`]
 - `serde 1` → [Updates: `lock file @ 1.0.229`]
 - `serde_json 1.0` → [Updates: `lock file @ 1.0.154`]

</details>

<details><summary>crates/fd5/Cargo.toml (3)</summary>

 - `hdf5-metno-sys 0.10.1` → [Updates: `0.12.0`]
 - `thiserror 2` → [Updates: `lock file @ 2.0.21`]
 - `tempfile 3`

</details>

<details><summary>h5v/Cargo.toml (13)</summary>

 - `arboard 3.6.1` → [Updates: `lock file @ 3.7.0`]
 - `bktree 1.0.1`
 - `clap 4.5.51` → [Updates: `lock file @ 4.6.9`]
 - `fuzzy-matcher 0.3.7`
 - `git-version 0.3.9`
 - `image 0.25.9`
 - `itertools 0.14.0` → [Updates: `0.15.0`]
 - `ndarray 0.17.1`
 - `plotters 0.3.7`
 - `ratatui 0.30.0` → [Updates: `lock file @ 0.30.2`]
 - `ratatui-image 10.0.2` → [Updates: `lock file @ 10.0.8`, `11.0.0`]
 - `toml 0.8` → [Updates: `0.9`, `1.0`]
 - `syntect 5.3.0`

</details>

</blockquote>
</details>

<details><summary>github-actions (2)</summary>
<blockquote>

<details><summary>.github/workflows/prepare-release-extension.yml (1)</summary>

 - `ubuntu 26.04`

</details>

<details><summary>.github/workflows/release-extension.yml (1)</summary>

 - `ubuntu 26.04`

</details>

</blockquote>
</details>

---

- [ ] <!-- manual job -->Check this box to trigger a request for Renovate to run again on this repository


