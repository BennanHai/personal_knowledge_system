# OpenClaw 问题排查与解决方案（Windows）

---
> 本文档记录了 OpenClaw 在Windows系统下配置过程中遇到的各类问题及其解决方法，供后续参考。
---

## 目录

1. [Gateway 启动失败 - 端口冲突](#1-gateway-启动失败---端口冲突)
2. [页面显示 Unauthorized - Token 未配置](#2-页面显示-unauthorized---token-未配置)
3. [HTTP 401 认证失败 - API Key 配置错误](#3-http-401-认证失败---api-key-配置错误)
4. [Kimi 模型配置失败 - baseUrl 域名错误](#4-kimi-模型配置失败---baseurl-域名错误)
5. [QQ Bot 显示 not configured - 插件未加载](#5-qq-bot-显示-not-configured---插件未加载)
6. [正确配置示例](#6-正确配置示例)

---

## 1. Gateway 启动失败 - 端口冲突

### 问题表现

```
Found stale gateway process(es): 24780.
Port 18789 is already in use.
Gateway restart timed out after 60s waiting for health checks.
```

### 问题原因

- 端口被其他进程占用
- 之前的 Gateway 进程未正常退出，形成僵尸进程

### 解决方法

**方法一：使用 OpenClaw 命令停止后重启**

```cmd
openclaw gateway stop
openclaw gateway start
```

**方法二：手动终止占用进程**

```cmd
# 查看占用端口的进程
netstat -ano | findstr :18789

# 终止进程（替换 PID）
taskkill /PID <PID> /F

# 重启 Gateway
openclaw gateway start
```

**方法三：使用不同端口**

```cmd
openclaw gateway start --port 18790
```

---

## 2. 页面显示 Unauthorized - Token 未配置

### 问题表现

访问 `http://127.0.0.1:18789/` 页面显示：

```
已断开与网关的连接
unauthorized: gateway token missing (open the dashboard URL and paste the token in Control UI settings)
```

日志显示：

```
[ws] unauthorized reason=token_missing
```

### 问题原因

Control UI 需要配置 Gateway Token 才能连接到 Gateway。

### 解决方法

**步骤 1：获取 Gateway Token**

```cmd
type %USERPROFILE%\.openclaw\openclaw.json | findstr token
```

在配置文件中找到：

```json
"gateway": {
  "auth": {
    "mode": "token",
    "token": "您的Gateway Token"
  }
}
```

**步骤 2：在 Control UI 中配置 Token**

1. 打开 `http://127.0.0.1:18789/`
2. 点击页面右上角的 **用户头像** 或 **设置图标**
3. 找到 **Gateway Token** 输入框
4. 粘贴 Token 并保存

---

## 3. HTTP 401 认证失败 - API Key 配置错误

### 问题表现

聊天时报错：

```
HTTP 401: Invalid Authentication
```

### 问题原因

API Key 配置位置错误。最初将 API Key 配置在 `auth.profiles` 下，这是不被识别的配置项：

```json
// ❌ 错误配置
"auth": {
  "profiles": {
    "moonshot:default": {
      "provider": "moonshot",
      "mode": "api_key",
      "apiKey": "sk-xxx"  // 此位置不被识别
    }
  }
}
```

### 解决方法

API Key 应该配置在 `models.providers` 下：

```json
// ✅ 正确配置
"models": {
  "providers": {
    "moonshot": {
      "baseUrl": "https://api.moonshot.cn/v1",
      "api": "openai-completions",
      "apiKey": "sk-xxx",  // 正确位置
      "models": [...]
    }
  }
}
```

**验证 API Key 是否有效：**

```cmd
curl -H "Authorization: Bearer sk-xxx" https://api.moonshot.cn/v1/models
```

---

## 4. Kimi 模型配置失败 - baseUrl 域名错误

### 问题表现

配置了正确的 API Key，但仍然报 `Invalid Authentication`：

```cmd
curl -H "Authorization: Bearer sk-xxx" https://api.moonshot.ai/v1/models
# 返回：{"error":{"message":"Invalid Authentication"}}
```

### 问题原因

**baseUrl 域名错误！**

| 域名 | 说明 |
|------|------|
| `api.moonshot.ai` | 国际版/旧域名，部分 API Key 不支持 |
| `api.moonshot.cn` | 中国区域名，大多数国内 API Key 使用此域名 |

### 解决方法

修改 `baseUrl`：

```json
// ❌ 错误
"baseUrl": "https://api.moonshot.ai/v1"

// ✅ 正确
"baseUrl": "https://api.moonshot.cn/v1"
```

**验证正确域名：**

```cmd
curl -H "Authorization: Bearer sk-xxx" https://api.moonshot.cn/v1/models
# 返回：{"object":"list","data":[...]}
```

### Moonshot 可用模型列表

| 模型 ID | 上下文长度 | 支持功能 |
|---------|-----------|---------|
| `kimi-k2.5` | 262K | 文本、图像、视频、推理 |
| `kimi-k2-thinking` | 262K | 推理 |
| `kimi-k2-turbo-preview` | 262K | - |
| `moonshot-v1-8k` | 8K | 文本 |
| `moonshot-v1-32k` | 32K | 文本 |
| `moonshot-v1-128k` | 128K | 文本 |
| `moonshot-v1-8k-vision-preview` | 8K | 文本、图像 |

---

## 5. QQ Bot 显示 not configured - 插件未加载

### 问题表现

```cmd
openclaw status --deep
```

显示：

```
│ QQ Bot   │ ON      │ SETUP  │ not configured                                        │
```

日志警告：

```
plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot
```

### 问题原因

1. **插件未显式允许加载**：需要在 `plugins.allow` 中明确指定允许的插件
2. **QQ 白名单未配置**：需要在 QQ 开放平台添加测试用户

### 解决方法

**步骤 1：配置 plugins.allow**

```json
"plugins": {
  "allow": ["qqbot"],
  "entries": {
    "qqbot": {
      "enabled": true
    }
  }
}
```

**步骤 2：配置 QQ 白名单**

1. 登录 [QQ 开放平台](https://bot.q.qq.com/)
2. 选择机器人（AppID: `1903098663`）
3. 进入 **沙箱配置** 或 **测试用户**
4. 添加测试 QQ 号或测试群

**步骤 3：重启 Gateway**

```cmd
openclaw gateway restart
```

### QQ Bot 使用方式

| 方式 | 说明 |
|------|------|
| 私聊 | 直接向机器人发送消息 |
| 群聊 | 在群里 @机器人 后发送消息 |

---

## 6. 正确配置示例

### 完整的 Kimi + QQ Bot 配置文件

```json
{
  "meta": {
    "lastTouchedVersion": "2026.3.7",
    "lastTouchedAt": "2026-03-08T10:10:32.996Z"
  },
  "wizard": {
    "lastRunAt": "2026-03-08T10:04:40.406Z",
    "lastRunVersion": "2026.3.7",
    "lastRunCommand": "onboard",
    "lastRunMode": "local"
  },
  "auth": {
    "profiles": {
      "moonshot:default": {
        "provider": "moonshot",
        "mode": "api_key"
      }
    }
  },
  "models": {
    "mode": "merge",
    "providers": {
      "moonshot": {
        "baseUrl": "https://api.moonshot.cn/v1",
        "api": "openai-completions",
        "apiKey": "您的Moonshot API Key",
        "models": [
          {
            "id": "kimi-k2.5",
            "name": "Kimi K2.5",
            "reasoning": false,
            "input": ["text", "image"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 262144,
            "maxTokens": 8192
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "moonshot/kimi-k2.5"
      },
      "models": {
        "moonshot/kimi-k2.5": {
          "alias": "Kimi"
        }
      },
      "workspace": "C:\\Users\\18220\\.openclaw\\workspace",
      "compaction": {
        "mode": "safeguard"
      },
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8
      }
    }
  },
  "tools": {
    "profile": "coding",
    "web": {
      "search": {
        "enabled": true,
        "provider": "kimi",
        "kimi": {
          "apiKey": "您的Moonshot API Key"
        }
      }
    }
  },
  "messages": {
    "ackReactionScope": "group-mentions"
  },
  "commands": {
    "native": "auto",
    "nativeSkills": "auto",
    "restart": true,
    "ownerDisplay": "raw"
  },
  "session": {
    "dmScope": "per-channel-peer"
  },
  "channels": {
    "qqbot": {
      "enabled": true,
      "appId": "您的QQ机器人AppID",
      "appSecret": "您的QQ机器人AppSecret",
      "token": "您的QQ机器人Token",
      "sandbox": true,
      "allowPrivateChat": true,
      "allowGroupAt": true
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "auth": {
      "mode": "token",
      "token": "您的Gateway Token"
    },
    "tailscale": {
      "mode": "off",
      "resetOnExit": false
    },
    "nodes": {
      "denyCommands": [
        "camera.snap",
        "camera.clip",
        "screen.record",
        "contacts.add",
        "calendar.add",
        "reminders.add",
        "sms.send"
      ]
    }
  },
  "plugins": {
    "allow": ["qqbot"],
    "entries": {
      "telegram": {
        "enabled": true
      },
      "qqbot": {
        "enabled": true
      }
    },
    "installs": {
      "qqbot": {
        "source": "path",
        "sourcePath": "C:\\Users\\18220\\.openclaw\\qqbot",
        "installPath": "C:\\Users\\18220\\.openclaw\\extensions\\qqbot",
        "version": "1.5.3",
        "installedAt": "2026-03-08T10:10:30.165Z"
      }
    }
  }
}
```

---

## 常用排查命令

| 命令 | 说明 |
|------|------|
| `openclaw status` | 查看基本状态 |
| `openclaw status --deep` | 查看详细状态 |
| `openclaw logs --follow` | 实时查看日志 |
| `openclaw gateway stop` | 停止 Gateway |
| `openclaw gateway start` | 启动 Gateway |
| `openclaw gateway restart` | 重启 Gateway |
| `openclaw config get <path>` | 获取配置值 |
| `openclaw config set <path> <value>` | 设置配置值 |

---

## 问题排查流程图

```
问题发生
    │
    ▼
检查 Gateway 状态
openclaw status
    │
    ├── Gateway 未运行 ──▶ 启动 Gateway
    │
    ├── 端口被占用 ──▶ 终止占用进程后重启
    │
    ▼
检查日志
openclaw logs --follow
    │
    ├── 401 错误 ──▶ 检查 API Key 配置
    │                └── 检查 baseUrl 域名
    │
    ├── token_missing ──▶ 配置 Gateway Token
    │
    ├── 插件未加载 ──▶ 配置 plugins.allow
    │
    ▼
问题解决
```

---

## 参考链接

- [OpenClaw 官方文档](https://docs.openclaw.ai/)
- [OpenClaw 故障排查](https://docs.openclaw.ai/troubleshooting)
- [OpenClaw FAQ](https://docs.openclaw.ai/faq)
- [Moonshot 开放平台](https://platform.moonshot.cn/)
- [QQ 开放平台](https://bot.q.qq.com/)

---

*文档生成时间：2026-03-08*




# OpenClaw 问题排查与解决方案（ubuntu）

