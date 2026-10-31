# LOCachy app presets

[中文](README.zh.md)

The presets LOCachy offers for its containers: one `apps/NAME.conf` each
(Edge, Firefox, WeChat and the others). A LOCachy system takes them as its
catalog of app presets, apart from its own source; the system's updater and
installer fetch this repository, and its updates never rebuild the system.
The host programs' presets (foot, Code - OSS) are the system's and stay in
its source.

## Format 1

```
FORMAT          one line: 1
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

No value may hold `"`, `\`, `$`, a backquote or a control character. `host=`
is refused: a host program is the system's. The system rejects the whole
catalog for the first file that breaks a rule and keeps the one it has.

## Checking a change

With a LOCachy source checkout next to this one:

```
python3 -I tools/check.py ../locachy/src/link/locachy_apps.py
```

It uses that system's own validator and says `OK` with the number of
presets, or why the system would refuse the catalog.

When a system takes a new version of a preset, its configuration made from
that preset follows the changed keys the user left as they were; keys the
user changed stay theirs. A change of `package` or `extras` rebuilds that
container. See `src/tools/APPS.md` in the LOCachy source.

## License

Copyright (C) 2026 Yuanzhao Niu. GPL-3.0-or-later, as LOCachy itself: see
[LICENSE](LICENSE).
