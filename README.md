# LOCachy app presets

[中文](README.zh.md)

The recipes LOCachy offers in its application store: one `apps/NAME.conf`
each (Edge, Firefox, WeChat, ChatGPT and the others). A LOCachy system takes
them as its catalog of app presets, apart from its own source; the system's
updater and installer fetch this repository. The built-in tools' presets
(foot, Code - OSS) stay in the system source.

ChatGPT is installed from its recipe in Packages, like the other apps. It
requests real-system access for its agent and terminal. Packages shows that
access and asks before granting it: its root/home and installed packages
are the real system's, while its process namespace, cgroup and lifecycle
remain managed by home. It runs as the user; sudo still needs authentication.
Ordinary recipes remain isolated by default.

## Format 2

```
FORMAT          one line: 2
apps/NAME.conf  a preset
```

A preset is data, never run: lines that are empty, `# comments` or
`KEY="VALUE"`. NAME is `[a-z0-9][a-z0-9._-]{0,62}`; each file is a regular
file of at most 16 KiB, UTF-8.

| Key | Value |
| --- | --- |
| `package` (required) | the program's package (the repositories' or the AUR's) |
| `extras` | more packages, separated by spaces |
| `command` (required) | the program, an absolute path |
| `arguments` | its arguments, separated by spaces |
| `network` | `1`: on the network |
| `camera` | `1`: the cameras |
| `directories` | more directories of the home, absolute, separated by colons |
| `desktop` | `.desktop` file names, separated by spaces |
| `x11` | `1`: the shared X server too |
| `host` | `1`: request real-system access; absent or `0`: isolated |

No value may hold `"`, `\`, `$`, a backquote or a control character. The
system rejects the whole catalog for the first file that breaks a rule and
keeps the one it has.

Format 2 adds the `host` request. Update LOCachy first: an older system
refuses format 2 visibly and keeps its previous catalog. The current system
also reads format 1, which still forbids `host`.

## Checking a change

With a LOCachy source checkout next to this one:

```
python3 -I tools/check.py ../locachy/src/link/locachy_apps.py
```

It uses that system's own validator and says `OK` with the number of
presets, or why the system would refuse the catalog.

When a system takes a new version of a preset, its configuration made from
that preset follows the changed keys the user left as they were; keys the
user changed stay theirs. Its granted `host` mode never follows automatic
updates: a different request is shown for review in Packages, and current
access is kept. A change of `package` or `extras` rebuilds that app (installing
packages on the real system only when that access was already granted).
Those packages are shared host packages; removing an app recipe does not
uninstall them. See `src/tools/APPS.md` in the LOCachy source.

Window, network and lifecycle tests are not account-login or authenticated
agent-terminal acceptance; those need a real account and separate verification.

## License

Copyright (C) 2026 Yuanzhao Niu. GPL-3.0-or-later, as LOCachy itself: see
[LICENSE](LICENSE).
