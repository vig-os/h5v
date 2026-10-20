---
type: issue
state: open
created: 2026-10-05T13:52:17Z
updated: 2026-10-19T12:24:16Z
author: vigos-devkit-upgrade[bot]
author_url: https://github.com/vigos-devkit-upgrade[bot]
url: https://github.com/vig-os/h5v/issues/15
comments: 2
labels: none
assignees: none
milestone: none
projects: none
parent: none
children: none
synced: 2026-10-20T07:22:15.427Z
---

# [Issue 15]: [chore(devkit): automated devkit upgrade is failing](https://github.com/vig-os/h5v/issues/15)

<!-- devkit-upgrade-failure -->

The managed devkit-upgrade workflow is failing, so this repo has stopped adopting new devkit releases.

- Run: https://github.com/vig-os/h5v/actions/runs/37319885620
- Failing step: Commit the upgrade in the project shell
- Pinned devkit version: 1.17.0
- Target devkit version: 1.18.0
Nothing was pushed: the adoption branch only reaches the remote once the upgrade commit is published, so there is no half-applied state to clean up. Fix the cause and re-run the workflow (or dispatch it with an explicit version) — this issue is filed, updated and closed by the workflow itself.
---

# [Comment #1]() by [vigos-devkit-upgrade[bot]]()

_Posted on October 12, 2026 at 02:40 PM_

The devkit upgrade failed again.

- Run: https://github.com/vig-os/h5v/actions/runs/38264429055
- Failing step: Commit the upgrade in the project shell
- Pinned devkit version: 1.17.0
- Target devkit version: 1.18.0

---

# [Comment #2]() by [vigos-devkit-upgrade[bot]]()

_Posted on October 19, 2026 at 12:24 PM_

The devkit upgrade failed again.

- Run: https://github.com/vig-os/h5v/actions/runs/39251576416
- Failing step: Commit the upgrade in the project shell
- Pinned devkit version: 1.17.0
- Target devkit version: 1.18.0

