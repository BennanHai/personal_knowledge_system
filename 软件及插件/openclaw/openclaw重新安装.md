
# OpenClaw 在 Ubuntu 上的完整重新安装与问题解决指南

本文档记录了在 Ubuntu 系统中因升级中断导致 OpenClaw 命令不可用后，如何彻底清理残留、重新安装以及后续使用的完整过程。如果你也遇到类似问题，希望这份指南能帮助你顺利恢复。

---

## 1. 问题现象

- 执行 `openclaw update` 时意外中断，导致 `openclaw` 命令失效。
- 尝试用 `npm uninstall -g openclaw` 卸载时出现 `ENOTEMPTY` 错误，提示目录非空，无法完成重命名操作。

---

## 2. 手动彻底清理残留

在 `openclaw` 命令不可用的情况下，需要手动删除所有相关文件和服务。

### 2.1 停止可能正在运行的后台服务

```bash
systemctl --user stop openclaw-gateway.service
```

### 2.2 删除全局 npm 模块目录
根据错误信息中的路径，直接删除 OpenClaw 的模块目录（请根据你的实际 Node.js 安装路径调整）：

```bash
rm -rf /root/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw
```

### 2.3 删除用户配置和数据目录
```bash
rm -rf ~/.openclaw
```

### 2.4 移除 systemd 用户服务（防止开机自启残留）

```bash
systemctl --user disable --now openclaw-gateway.service
rm -f ~/.config/systemd/user/openclaw-gateway.service
systemctl --user daemon-reload
```

### 2.5 清理 npm 缓存（可选）

```bash
npm cache clean --force
```

## 3. 重新安装 OpenClaw
为了避免未来再次出现升级混乱，建议选择以下两种方式之一，并坚持使用统一的方法进行升级。

**方式一：官方一键脚本（最推荐）**

此方式将安装和升级统一为再次运行同一脚本，简单可靠。

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

升级方法：以后需要升级时，只需重新执行上述命令。

**方式二：npm 全局安装（备选）**

如果一键脚本暂时无法访问，可以使用 npm 安装官方最新版本。

```bash
npm install -g openclaw@latest
```

升级方法：重新运行 `npm install -g openclaw@latest`。

> **重要提示**：无论选择哪种方式，请避免混用 `openclaw update` 和包管理器升级，以免再次出现状态不一致。

### 3.1 验证安装
```bash
openclaw --version
```

### 3.2 初始化配置
```bash
openclaw onboard
```

根据提示完成 API Key、工作目录等基础设置，并确保网关服务正常启动：

```bash
openclaw gateway start
openclaw gateway status
```

## 4. 日常使用：TUI 命令行交互
安装完成后，可以通过以下命令启动终端交互界面：

```bash
openclaw tui
```

### 4.1 退出 TUI 不会停止服务
在 TUI 界面中：

- 按一次 **Ctrl + C**：清空当前输入
- 连续按两次 **Ctrl + C**：退出 TUI 界面，但 OpenClaw 的后台网关服务（Gateway）仍在运行，不会中断

这是因为 TUI 只是一个客户端界面，服务端独立运行。你可以随时再次输入 `openclaw tui` 重新连接。

### 4.2 正确停止后台服务的方法
如果需要真正停止 OpenClaw，请使用：

```bash
openclaw gateway stop
```

## 5. 接入 QQ 机器人的备选思路
由于官方文档可能暂时无法访问，这里提供几种常见的接入思路，待环境稳定后可进一步尝试：

- 尝试内置插件命令：
  ```bash
  openclaw plugin search qq
  openclaw plugin install @openclaw/plugin-qqbot   # 假设名称
  ```

- 独立部署 QQ 机器人框架（如 go-cqhttp），然后通过 OneBot 协议与 OpenClaw 连接

- 自行编写 Agent 调用 QQ API（适合有开发能力的用户）

## 6. 最终成功标志
完成以上步骤后，OpenClaw 已恢复正常工作，你可以顺利通过以下方式与 AI 助手交互：

- 命令行交互：`openclaw tui`
- 网页控制台：`openclaw dashboard`（默认地址 http://127.0.0.1:18789）

---

**总结**：遇到升级中断导致命令失效时，手动清理残留 + 重新安装 是最快捷的恢复方法。选择官方一键脚本可以统一升级方式，避免后续混乱。日常使用中注意区分客户端和服务端的停止操作，即可长期稳定运行。
