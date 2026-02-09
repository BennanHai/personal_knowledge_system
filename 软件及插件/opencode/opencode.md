# opencode
[官方文档](https://opencode.ai/docs/)
[知乎](https://zhuanlan.zhihu.com/p/1997056000306460125)
[微信公众号](https://mp.weixin.qq.com/s/r5uTnd8OnzPR7-xD9Umlug)

## 介绍

## 安装
使用npm安装
```bash
npm install -g opencode-ai
```
验证安装
```bash
opencode --version

# C:\Users\18220>opencode --version
# 1.1.47
```

## 配置国内大模型
### 方法一
安装后，运行命令 `opencode auth login` 配置你的AI模型API密钥：
```bash
C:\Users\18220>opencode auth login

T  Add credential
|
o  Select provider
|  DeepSeek
|
o  Enter your API key
|  •••••••••••••••••••••••••••••••••••
|
—  Done


C:\Users\18220>
```

### 方法二
通过修改配置文件配置你的AI模型API密钥：
> Windows: %USERPROFILE%\.config\opencode\config.json
> macOS / Linux: ~/.config/opencode/config.json

- deepseek
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "deepseek": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "DeepSeek",
      "options": {
        "baseURL": "https://api.deepseek.com",
        "apiKey": "sk-xxx"
      },
      "models": {
        "deepseek-reasoner": {
          "name": "DeepSeek-Reasoner"
        }
      }
    }
  },
  "plugin": ["oh-my-opencode"]
}
```

公司：
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "deepseek": {
      "models": {
        "deepseek-chat": {
          "options": {
            "api_base": "https://api.deepseek.com/v1",
            "api_key":  "sk-xxx"
          }
        }
      }
    }
  },
  "plugin": [
    "oh-my-opencode@latest"
  ]
}
```

## 基本使用
- 使用 `opencode` 命令启动
```bash
cd 项目目录
opencode
```

- 


## 插件
### [oh-my-opencode](https://opencode.ai/docs)
> Oh My OpenCode 是 OpenCode 的增强插件，提供多智能体协作、LSP 集成、自动化工作流等功能。所有功能默认启用，开箱即用。

- 让 AI 智能体安装（强烈推荐）

- 交互式安装
  ```bash
  bunx oh-my-opencode install  # 推荐
  # 或
  npx oh-my-opencode install   # 备选
  ```

## 核心智能体
Oh My OpenCode 构建了一个 AI 智能体团队，每个成员有不同的职责。

- 四大核心智能体对比

| 智能体 | 角色定位 | 核心职责 | 工作方式 |
|--------|----------|----------|----------|
| Sisyphus | 主智能体 / 团队负责人 | 任务编排、委派、持续推进 | 永不停歇，直到任务 100% 完成 |
| Prometheus | 规划器 | 任务分解、制定详细计划 | 在执行前进行战略规划 |
| Hephaestus | 自主深度工作者 | 目标导向的代码实现 | 自主探索，精准执行 |
| Atlas | 重型任务承载者 | 大规模代码库处理 | 承担繁重的上下文管理 |

- Sisyphus
   - 职责：任务协调、项目管理
   - 工作方式：持续监听用户指令，协调其他智能体的工作，确保项目按计划进行。
   - 核心特性：
     - ✅ 持续推进：被 TODO 列表约束，任务未完成就不会停止
     - ✅ 智能委派：UI 任务交给 Gemini，难题召唤 Oracle
     - ✅ 上下文精简：并行派遣子智能体侦察，保持主上下文精简
     - ✅ 代码整洁：Comment Checker 确保代码与人类编写无异
- Prometheus
    - 职责：任务分解、制定详细计划
    - 工作方式：在执行前进行战略规划，确保任务分解合理、优先级正确。
    - 核心特性：
      - 📋 任务分解：将复杂需求拆解为可执行步骤
      - 🔮 需求访谈：通过对话深入理解需求
      - 🎯 计划生成：输出结构化的实施计划
      - 📝 Metis 审核：计划顾问优化方案
- Hephaestus
    - 职责：代码实现、功能开发
    - 工作方式：根据 Prometheus 生成的计划，自主探索，精准执行。
    - 核心特性：
      - 🎯 目标导向：给他目标，不是步骤，自己决定如何实现
      - 🔍 行动前探索：写代码前并行启动 2-5 个探索智能体
      - ✅ 端到端完成：有验证证据证明 100% 完成才停止
      - 🎨 模式匹配：匹配现有代码风格，无 AI 痕迹
      - ⚡ 精准极简：代码精准、最小化、只做需要的功能
- Atlas
    - 职责：大规模代码库处理
    - 工作方式：承担繁重的上下文管理，确保在复杂项目中保持效率。
    - 核心特性：
      - 💪 大规模处理：处理超大代码库和复杂项目
      - 🧠 上下文承载：管理和维护大量上下文信息
      - 🔄 持久化工作：长时间运行的任务处理
      - 📊 全局视野：维持对整个项目的宏观理解
  
- 其他辅助智能体

| 智能体 | 默认模型 | 职责 |
|--------|----------|------|
| Oracle | GPT 5.2 | 设计决策、调试、战略支援 |
| Librarian | Claude Sonnet 4.5 | 官方文档、开源实现搜索 |
| Explore | Claude Haiku 4.5 | 极速代码库 Grep |
| Frontend UI/UX | Gemini 3 Pro | 前端开发、多模态处理 |
| Metis | - | 计划顾问，优化 Prometheus 的计划 |
| Multimodal Looker | Gemini Flash | 图像/视觉内容处理 |

