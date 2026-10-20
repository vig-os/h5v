---
type: issue
state: open
created: 2026-09-29T11:58:49Z
updated: 2026-10-19T07:36:10Z
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
synced: 2026-10-20T07:22:15.872Z
---

# [Issue 14]: [Dependency Dashboard](https://github.com/vig-os/h5v/issues/14)

This issue lists Renovate updates and detected dependencies. Read the [Dependency Dashboard](https://docs.renovatebot.com/key-concepts/dashboard/) docs to learn more.<br>[View this repository on the Mend.io Web Portal](https://developer.mend.io/github/vig-os/h5v).

## Rate-Limited

The following updates are currently rate-limited. To force their creation now, click on a checkbox below.

 - [ ] <!-- unlimit-branch=renovate/ratatui-image-10.x-lockfile -->chore(deps): update rust crate ratatui-image to v10.0.8
 - [ ] <!-- unlimit-branch=renovate/serde-monorepo -->chore(deps): update rust crate serde to v1.0.229
 - [ ] <!-- unlimit-branch=renovate/serde_json-1.x-lockfile -->chore(deps): update rust crate serde_json to v1.0.154
 - [ ] <!-- unlimit-branch=renovate/thiserror-2.x-lockfile -->chore(deps): update rust crate thiserror to v2.0.21
 - [ ] <!-- unlimit-branch=renovate/arboard-3.x-lockfile -->chore(deps): update rust crate arboard to v3.7.0
 - [ ] <!-- unlimit-branch=renovate/hdf5-metno-0.x -->chore(deps): update rust crate hdf5-metno to 0.15.0
 - [ ] <!-- unlimit-branch=renovate/sha2-0.x -->chore(deps): update rust crate sha2 to 0.11
 - [ ] <!-- unlimit-branch=renovate/hdf5-metno-sys-0.x -->fix(deps): update rust crate hdf5-metno-sys to 0.12.0
 - [ ] <!-- unlimit-branch=renovate/itertools-0.x -->fix(deps): update rust crate itertools to 0.15.0
 - [ ] <!-- unlimit-branch=renovate/toml-0.x -->fix(deps): update rust crate toml to 0.9
 - [ ] <!-- unlimit-branch=renovate/ratatui-image-11.x -->fix(deps): update rust crate ratatui-image to v11
 - [ ] <!-- unlimit-branch=renovate/toml-1.x -->fix(deps): update rust crate toml to v1
 - [ ] <!-- unlimit-branch=renovate/lock-file-maintenance -->chore(deps): lock file maintenance
 - [ ] <!-- create-all-rate-limited-prs -->🔐 **Create all rate-limited PRs at once** 🔐

## Open

The following updates have all been created. To force a retry/rebase of any, click on a checkbox below.

 - [ ] <!-- rebase-branch=renovate/clap-4.x-lockfile -->[chore(deps): update rust crate clap to v4.6.7](../pull/16)
 - [ ] <!-- rebase-branch=renovate/ratatui-0.x-lockfile -->[chore(deps): update rust crate ratatui to v0.30.2](../pull/17)
 - [ ] <!-- rebase-all-open-prs -->**Click on this checkbox to rebase all open PRs at once**

## Detected Dependencies

<details><summary>cargo (3)</summary>
<blockquote>

<details><summary>Cargo.toml (4)</summary>

 - `hdf5-metno 0.11.0` → [Updates: `0.15.0`]
 - `sha2 0.10` → [Updates: `0.11`]
 - `serde 1` → [Updates: `1`]
 - `serde_json 1.0` → [Updates: `1.0`]

</details>

<details><summary>crates/fd5/Cargo.toml (3)</summary>

 - `hdf5-metno-sys 0.10.1` → [Updates: `0.12.0`]
 - `thiserror 2` → [Updates: `2`]
 - `tempfile 3`

</details>

<details><summary>h5v/Cargo.toml (13)</summary>

 - `arboard 3.6.1` → [Updates: `3.6.1`]
 - `bktree 1.0.1`
 - `clap 4.5.51` → [Updates: `4.5.51`]
 - `fuzzy-matcher 0.3.7`
 - `git-version 0.3.9`
 - `image 0.25.9`
 - `itertools 0.14.0` → [Updates: `0.15.0`]
 - `ndarray 0.17.1`
 - `plotters 0.3.7`
 - `ratatui 0.30.0` → [Updates: `0.30.0`]
 - `ratatui-image 10.0.2` → [Updates: `10.0.2`, `11.0.0`]
 - `toml 0.8` → [Updates: `0.9`, `1.0`]
 - `syntect 5.3.0`

</details>

</blockquote>
</details>

<details><summary>github-actions (14)</summary>
<blockquote>

<details><summary>.github/actions/setup-devkit-toolchain/action.yml</summary>


</details>

<details><summary>.github/workflows/abandon-release.yml</summary>


</details>

<details><summary>.github/workflows/ci.yml</summary>


</details>

<details><summary>.github/workflows/codeql.yml</summary>


</details>

<details><summary>.github/workflows/devkit-upgrade.yml</summary>


</details>

<details><summary>.github/workflows/prepare-release-extension.yml (1)</summary>

 - `ubuntu 26.04`

</details>

<details><summary>.github/workflows/prepare-release.yml</summary>


</details>

<details><summary>.github/workflows/promote-release.yml</summary>


</details>

<details><summary>.github/workflows/release-core.yml</summary>


</details>

<details><summary>.github/workflows/release-extension.yml (1)</summary>

 - `ubuntu 26.04`

</details>

<details><summary>.github/workflows/release-publish.yml</summary>


</details>

<details><summary>.github/workflows/release.yml</summary>


</details>

<details><summary>.github/workflows/scorecard.yml</summary>


</details>

<details><summary>.github/workflows/sync-issues.yml</summary>


</details>

</blockquote>
</details>

---

- [ ] <!-- manual job -->Check this box to trigger a request for Renovate to run again on this repository


