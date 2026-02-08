# OpenClaw
- [OpenClaw 项目](https://github.com/OpenClaw/OpenClaw)
- [OpenClaw 中文文档](https://docs.openclaw.ai/zh-CN)

- 简介
OpenClaw 是一个基于 ROS 的开源项目，用于控制和管理机器人的运动。它提供了一个简单而强大的接口，使开发人员能够轻松地控制机器人的运动和行为。
- 功能
OpenClaw 提供了以下功能：
    1. 控制机器人的运动，包括移动、旋转、抓取等。
    2. 提供一个简单而强大的接口，使开发人员能够轻松地控制机器人的运动和行为。
    3. 支持多个机器人平台，包括但不限于 ROS 机器人、模拟机器人等。

## 安装
OpenClaw 可以从官方仓库下载安装脚本：[OpenClaw 安装脚本](https://github.com/OpenClaw/OpenClaw#installation)

```bash
# 安装 OpenClaw
npm install -g openclaw@latest
# or: pnpm add -g openclaw@latest

# 安装 OpenClaw 守护进程， 引导相关配置
openclaw onboard --install-daemon
```

## 接入机器人
### qq
- [阿里云部署openclaw并接入qq机器人](https://developer.aliyun.com/article/1710195)
- [腾讯云部署openclaw并接入qq机器人](https://cloud.tencent.com.cn/developer/article/2627089)
## 使用
### 启动 OpenClaw 守护进程
OpenClaw 守护进程负责管理机器人的运行状态和连接。

```bash
# 启动守护进程
openclaw onboard --start-daemon

# 停止守护进程
openclaw onboard --stop-daemon

# 重启守护进程
openclaw onboard --restart-daemon

# 查看守护进程状态
openclaw onboard --status
```

### 常用命令
以下是一些常用的 OpenClaw 命令：

```bash
# 查看 OpenClaw 版本
openclaw --version

# 查看帮助信息
openclaw --help

# 查看所有可用命令
openclaw --list

# 运行交互式控制台
openclaw console

# 检查系统状态
openclaw doctor
```

### 配置文件
OpenClaw 的配置文件通常位于 `~/.openclaw/config.yaml` 或项目目录下的 `openclaw.config.yaml`。

配置文件示例：
```yaml
# openclaw.config.yaml
version: "1.0"
robot:
  type: "qq"  # 机器人类型：qq, wechat, telegram 等
  token: "your-bot-token-here"  # 机器人令牌
  admin_ids:  # 管理员ID列表
    - "123456789"
    - "987654321"
plugins:
  enabled: true
  directory: "./plugins"  # 插件目录
logging:
  level: "info"  # 日志级别：debug, info, warn, error
  file: "./logs/openclaw.log"  # 日志文件路径
```

### 初始化项目
创建一个新的 OpenClaw 项目：

```bash
# 在当前目录初始化 OpenClaw 项目
openclaw init

# 在指定目录初始化
openclaw init my-robot-project

# 使用模板初始化
openclaw init --template basic my-robot-project
```

### 插件管理
OpenClaw 支持插件系统，可以扩展功能。

```bash
# 安装插件
openclaw plugin install plugin-name

# 列出已安装的插件
openclaw plugin list

# 卸载插件
openclaw plugin uninstall plugin-name

# 启用/禁用插件
openclaw plugin enable plugin-name
openclaw plugin disable plugin-name
```
