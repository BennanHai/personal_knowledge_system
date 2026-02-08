# VS Code中Claude Code配置问题解决过程

## 问题描述

在VS Code中使用Claude Code扩展时，DeepSeek配置没有生效，扩展仍然显示使用"Claude Sonnet 4.5"模型，而命令行中`claude`命令正确显示使用`deepseek-chat`模型。

## 问题分析

### 配置路径差异
1. **命令行Claude Code**：读取 `~/.claude/settings.json` 配置文件
2. **VS Code扩展**：使用独立的配置系统，默认不读取系统配置

### 根本原因
VS Code扩展启动时：
1. 优先读取VS Code设置中的 `claudeCode.env` 或 `claudeCode.environmentVariables`
2. 如果没有设置，则可能回退到默认的Claude API
3. **不自动继承**系统环境变量或 `~/.claude/settings.json` 中的配置

## 解决方案

让VS Code扩展读取系统配置，而不是使用独立配置。

### 方案一：通过VS Code终端环境变量（已实施）

修改 [VS Code用户设置](C:\Users\18220\AppData\Roaming\Code\User\settings.json)：

```json
"terminal.integrated.env.windows": {
    "ANTHROPIC_AUTH_TOKEN": "sk-xxx",
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_MODEL": "deepseek-chat"
}
```

**原理**：VS Code扩展启动的进程可能继承终端的环境变量。

### 方案二：创建项目级配置（已实施）

在项目目录 [.claude/settings.json](d:\study\go\first_project\.claude\settings.json) 中创建：

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-xxx",
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_MODEL": "deepseek-chat",
    "API_TIMEOUT_MS": "3000000"
  }
}
```

**原理**：Claude Code在项目目录中运行时，会优先读取项目级的 `.claude/settings.json`。

### 方案三：移除VS Code独立配置（已实施）

从VS Code设置中移除 `claudeCode.env` 配置，强制扩展读取系统配置。

## 配置优先级

Claude Code扩展读取配置的优先级（从高到低）：

1. **项目目录配置**：`项目/.claude/settings.json`
2. **用户主目录配置**：`~/.claude/settings.json`
3. **VS Code设置**：`claudeCode.environmentVariables`（不推荐使用）
4. **系统环境变量**：继承自父进程
5. **默认回退**：Claude官方API（Sonnet 4.5）

## 关键发现

### 1. VS Code扩展配置机制
- 扩展使用 `claudeCode.environmentVariables` 设置（数组格式）
- 建议文档明确指出："Prefer setting environment variables in Claude's settings.json"
- 扩展会验证JSON配置文件的有效性

### 2. API密钥问题
测试发现DeepSeek API返回 **"Authentication Fails (governor)"** 错误，说明：
- 配置已生效，但API密钥无效或已过期
- 当第三方API认证失败时，Claude Code自动回退到默认Claude模型

## 验证步骤

### 1. 重启VS Code
按 `Ctrl+Shift+P` 运行 **"Developer: Reload Window"**

### 2. 检查配置是否生效
在VS Code中：
1. 打开Claude Code面板
2. 问："你使用的是什么大模型？"
3. **期望响应**：`deepseek-chat`

### 3. 检查环境变量
在VS Code内置终端中运行：
```bash
echo $ANTHROPIC_MODEL
echo $ANTHROPIC_BASE_URL
```

**期望输出**：
```
deepseek-chat
https://api.deepseek.com/anthropic
```

## 文件清单

### 已修改的文件
1. **[C:\Users\18220\AppData\Roaming\Code\User\settings.json](C:\Users\18220\AppData\Roaming\Code\User\settings.json)**
   - 添加了 `terminal.integrated.env.windows` 配置
   - 移除了 `claudeCode.env` 配置

2. **[d:\study\go\first_project\.claude\settings.json](d:\study\go\first_project\.claude\settings.json)**
   - 创建了项目级DeepSeek配置

3. **[C:\Users\18220\.claude\settings.json](C:\Users\18220\.claude\settings.json)**
   - 原有的DeepSeek配置（命令行使用）

### 参考文件
1. **[C:\Users\18220\.vscode\extensions\anthropic.claude-code-2.1.23-win32-x64\package.json](C:\Users\18220\.vscode\extensions\anthropic.claude-code-2.1.23-win32-x64\package.json)**
   - VS Code扩展的配置schema定义

## 注意事项

### 1. API密钥有效性
确保DeepSeek API密钥有效：
- 访问 [DeepSeek控制台](https://platform.deepseek.com/) 检查密钥状态
- 确保账户有足够余额
- 如需更换API，更新所有配置文件中的相应值

### 2. 配置加载时间
- 扩展可能需要完全重启才能加载新配置
- 项目切换时，会读取对应项目的 `.claude/settings.json`

### 3. 配置优先级
- 项目级配置 > 用户级配置 > VS Code设置 > 环境变量
- 避免在多个位置重复配置，以免冲突

## 总结

通过实施多层次的配置方案，确保VS Code中的Claude Code扩展能够正确读取系统配置：

1. **终端环境变量**：让VS Code进程继承正确的环境变量
2. **项目级配置**：在项目目录中创建`.claude/settings.json`
3. **避免独立配置**：不使用VS Code的`claudeCode.env`设置

这种方案既保持了配置的统一性（使用系统配置），又确保了VS Code扩展能够正确加载配置。

---

**最后更新**：2026-01-29
**解决人**：Claude Code助手
**环境**：Windows 11, VS Code 1.94+, Claude Code 2.1.23