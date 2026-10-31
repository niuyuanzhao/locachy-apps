# LOCachy 应用预设

[English](README.md)

LOCachy 为其容器提供的预设：每个一份 `apps/NAME.conf`（Edge、Firefox、微信等）。
LOCachy 系统把它们作为应用预设目录，独立于系统自身的源码；系统的更新器和安装器获取本仓库，
其更新从不重建系统。宿主程序的预设（foot、Code - OSS）属于系统，仍留在系统源码中。

## 格式 1

```
FORMAT          一行：1
apps/NAME.conf  一份预设
```

预设是数据，从不执行：每行为空行、`# 注释` 或 `KEY="VALUE"`。NAME 为
`[a-z0-9][a-z0-9._-]{0,62}`；每个文件是不超过 16 KiB 的普通文件，UTF-8。

| 键 | 值 |
| --- | --- |
| `package`（必需） | 程序的软件包（软件源或 AUR 的） |
| `extras` | 更多软件包，空格分隔 |
| `command`（必需） | 程序，绝对路径 |
| `arguments` | 其参数，空格分隔 |
| `network` | `1`：联网 |
| `camera` | `1`：使用摄像头 |
| `directories` | 主目录中更多的目录，绝对路径，冒号分隔 |
| `desktop` | `.desktop` 文件名，空格分隔 |
| `x11` | `1`：同时使用共享的 X 服务器 |

值中不能有 `"`、`\`、`$`、反引号或控制字符。`host=` 会被拒绝：宿主程序属于系统。
任一文件违反规则，系统就拒绝整个目录，保留已有的那份。

## 检查改动

把 LOCachy 源码检出放在本仓库旁边：

```
python3 -I tools/check.py ../locachy/src/link/locachy_apps.py
```

它使用该系统自己的校验器，输出 `OK` 和预设数量，或系统拒绝该目录的原因。

系统采用某个预设的新版本时，由该预设生成的配置会跟随用户未改动的那些键的变化；用户改过的键保持不变。
`package` 或 `extras` 的变化会重建对应容器。详见 LOCachy 源码中的 `src/tools/APPS.zh.md`。

## 许可

Copyright (C) 2026 Yuanzhao Niu。与 LOCachy 本身相同，采用 GPL-3.0-or-later：见 [LICENSE](LICENSE)。
