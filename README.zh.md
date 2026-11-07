# LOCachy 应用预设

[English](README.md)

LOCachy 应用商店提供的配方：每个一份 `apps/NAME.conf`（Edge、Firefox、微信、ChatGPT 等）。
LOCachy 系统把它们作为应用预设目录，独立于系统自身的源码；系统的更新器和安装器获取本仓库。
内置工具的预设（foot、Code - OSS）仍留在系统源码中。

ChatGPT 和其他应用一样，从 Packages 中选择配方安装。它为代理和终端申请真实系统访问。
Packages 显示该访问模式，并在授予前要求确认：根目录、home 和已装软件包都是实际系统的，
但进程命名空间、cgroup 和生命周期仍由 home 管理。它以用户身份运行，sudo 仍需认证。
普通配方默认继续隔离。

## 格式 2

```
FORMAT          一行：2
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
| `host` | `1`：申请真实系统访问；省略或 `0`：隔离 |

值中不能有 `"`、`\`、`$`、反引号或控制字符。任一文件违反规则，系统就拒绝整个目录，保留已有的那份。

格式 2 增加 `host` 申请。请先更新 LOCachy：旧系统会明确拒绝格式 2，保留之前的目录。
当前系统也兼容格式 1，但格式 1 仍不允许 `host`。

## 检查改动

把 LOCachy 源码检出放在本仓库旁边：

```
python3 -I tools/check.py ../locachy/src/link/locachy_apps.py
```

它使用该系统自己的校验器，输出 `OK` 和预设数量，或系统拒绝该目录的原因。

系统采用某个预设的新版本时，由该预设生成的配置会跟随用户未改动的那些键的变化；用户改过的键保持不变。
已经授予的 `host` 模式绝不跟随自动更新：申请不同时，Packages 提示审阅，当前访问权限保留。
`package` 或 `extras` 的变化会重建对应应用（只有已经授予真实系统访问的应用才会把包安装到实际系统上）。
这些包是宿主共享的，移除应用配方不会自动卸载它们。详见 LOCachy 源码中的 `src/tools/APPS.zh.md`。

窗口打开、网络和生命周期验证不等于已经验证账号登录或登录后代理执行终端命令；后两项需要实际账号单独验收。

## 许可

Copyright (C) 2026 Yuanzhao Niu。与 LOCachy 本身相同，采用 GPL-3.0-or-later：见 [LICENSE](LICENSE)。
