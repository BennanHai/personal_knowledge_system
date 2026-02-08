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
## 基本使用
- 使用 `opencode` 命令启动
```bash
opencode
```

- 
