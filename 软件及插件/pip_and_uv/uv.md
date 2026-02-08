
# uv 包管理工具

## 📖 目录

- [简介](#-简介)
- [安装](#-安装)
- [基本使用](#-基本使用)
- [命令简介](#-命令简介)
- [项目管理](#-项目管理)
- [高级功能](#-高级功能)
- [最佳实践](#-最佳实践)

## 📚 参考资料

- [官方文档](https://docs.astral.sh/uv/)
- [官方文档中文](https://uv.doczh.com/)
- [GitHub 仓库](https://github.com/astral-sh/uv)
- 知乎文档
    - [uv 包管理工具介绍](https://zhuanlan.zhihu.com/p/1897568987136640818)
    - [uv 使用指南](https://zhuanlan.zhihu.com/p/1888904532131575259)

## 🚀 简介

uv 是一个现代化的 Python 包管理工具，由 Astral 公司开发。它旨在替代 pip、pip-tools、virtualenv 等传统工具，提供更快的性能和更好的用户体验。

### ✨ 主要特性

- **⚡ 极速安装**: 比 pip 快 10-100 倍
- **🛠️ 一体化工具**: 集成了包管理、虚拟环境管理、依赖解析等功能
- **💻 跨平台支持**: Windows、macOS、Linux
- **🔄 兼容性**: 完全兼容 pip 和 PyPI
- **📦 现代化设计**: 支持 pyproject.toml、锁定文件等现代标准

## 📥 安装

### 使用 pip 安装
```bash
pip install uv
```

### 设置国内镜像

#### 临时使用
```bash
pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 永久使用
```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 使用 uv.toml 配置文件（推荐）
在项目根目录下创建 `uv.toml` 文件，内容如下：
```toml
# uv 配置文件
# 主镜像源 - 使用清华镜像提升下载速度
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple/"

# 备用镜像源
extra-index-url = [
    "https://mirrors.aliyun.com/pypi/simple/",
    "https://pypi.douban.com/simple/"
]

# 依赖解析策略 - 选择最高版本
resolution = "highest"

# 不允许预发布版本
prerelease = "disallow"

# 并发下载数
concurrent-downloads = 10

# 缓存目录
cache-dir = "~/.uv-cache"
```


## 🛠️ 基本使用

### 创建虚拟环境

进入项目目录，执行以下命令：

```bash
# 创建默认虚拟环境 (.venv)
uv venv

# 创建指定名称的虚拟环境
uv venv --name myenv
```

### 激活虚拟环境

#### Windows
```bash
# 默认虚拟环境
.venv\Scripts\activate

# 指定名称的虚拟环境
myenv\Scripts\activate
```

#### macOS/Linux
```bash
# 默认虚拟环境
source .venv/bin/activate

# 指定名称的虚拟环境
source myenv/bin/activate
```

### 退出虚拟环境

```bash
deactivate
```

## 📋 命令简介

uv 包含以下命令，前几个是比较常用的。

### 常用命令

| 命令 | 描述 | 使用频率 |
|------|------|----------|
| `uv add` | 向项目中添加依赖项 | ⭐⭐⭐⭐⭐ |
| `uv remove` | 从项目中移除依赖项 | ⭐⭐⭐⭐⭐ |
| `uv sync` | 更新项目的环境 | ⭐⭐⭐⭐⭐ |
| `uv run` | 运行命令或脚本 | ⭐⭐⭐⭐⭐ |
| `uv init` | 创建一个新项目 | ⭐⭐⭐⭐ |
| `uv venv` | 创建虚拟环境 | ⭐⭐⭐⭐ |

### 完整命令列表

| 命令 | 描述 |
|------|------|
| `run` | 运行命令或脚本 |
| `init` | 创建一个新项目 |
| `add` | 向项目中添加依赖项 |
| `remove` | 从项目中移除依赖项 |
| `sync` | 更新项目的环境 |
| `lock` | 更新项目的锁定文件 |
| `export` | 将项目的锁定文件导出为其他格式 |
| `tree` | 显示项目的依赖树 |
| `tool` | 运行和安装由 Python 包提供的命令 |
| `python` | 管理 Python 版本和安装 |
| `pip` | 使用兼容 pip 的接口管理 Python 包 |
| `venv` | 创建虚拟环境 |
| `build` | 将 Python 包构建为源代码分发包和 wheels |
| `publish` | 将分发包上传到索引 |
| `cache` | 管理 uv 的缓存 |
| `self` | 管理 uv 可执行文件 |
| `version` | 显示 uv 的版本 |
| `generate-shell-completion` | 生成 shell 自动补全脚本 |
| `help` | 显示某个命令的文档 |
| `--version` | 显示版本号 |

### 安装依赖包

```bash
# 安装最新版本
uv add requests

# 安装指定版本
uv add flask==2.3.3

# 安装开发依赖
uv add --dev pytest

# 安装多个包
uv add requests flask pandas
```

### 删除依赖

```bash
uv remove black
```

### 从 requirements.txt 安装

```bash
uv pip install -r requirements.txt
```

### 同步依赖

```bash
# 同步所有依赖
uv sync

# 同步并安装开发依赖
uv sync --dev
```

### 列出已安装包

```bash
uv pip list
```

## 📁 项目管理

[项目开发官方文档](https://uv.doczh.com/guides/projects/#_2)

### 初始化新项目

```bash
# 创建新项目
uv init myproject

# 进入项目目录
cd myproject
```

### 生成 requirements.txt

```bash
# 生成 requirements.txt
uv pip freeze > requirements.txt

# 生成包含开发依赖的 requirements.txt
uv pip freeze --dev > requirements-dev.txt
```
## 为项目创建虚拟环境并下载依赖
```bash
(TraeAI-5) D:\study\githubs\opencode\learn-claude-code [0:] $ uv venv
Using CPython 3.13.0 interpreter at: D:\Program Files\python\python3.13.0\python.exe
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate
(TraeAI-5) D:\study\githubs\opencode\learn-claude-code [0:0] $ uv pip install -r requirements.txt
Resolved 17 packages in 2.14s
Prepared 1 package in 661ms
░░░░░░░░░░░░░░░░░░░░ [0/17] Installing wheels...                                                                                                                             warning: Failed to hardlink files; falling back to full copy. This may lead to degraded performance.
         If the cache and target directories are on different filesystems, hardlinking may not be supported.
         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
Installed 17 packages in 488ms
 + annotated-types==0.7.0
 + anthropic==0.77.0
 + anyio==4.12.1
 + certifi==2026.1.4
 + distro==1.9.0
 + docstring-parser==0.17.0
 + h11==0.16.0
 + httpcore==1.0.9
 + httpx==0.28.1
 + idna==3.11
 + jiter==0.13.0
 + pydantic==2.12.5
 + pydantic-core==2.41.5
 + python-dotenv==1.2.1
 + sniffio==1.3.1
 + typing-extensions==4.15.0
 + typing-inspection==0.4.2
(TraeAI-5) D:\study\githubs\opencode\learn-claude-code [0:0] $ 
```

## 🔧 高级功能

### Python 版本管理

```bash
# 安装特定 Python 版本
uv python install 3.11

# 使用特定 Python 版本创建虚拟环境
uv venv --python 3.11
```

### 依赖树查看

```bash
# 查看项目依赖树
uv tree

# 查看反向依赖树
uv tree --reverse
```

### 包构建和发布

```bash
# 构建包
uv build

# 发布包
uv publish
```

## 💡 最佳实践

1. **🚀 新项目优先使用 uv**: 对于新项目，建议直接使用 uv
2. **🔄 渐进式迁移**: 现有项目可以逐步迁移到 uv
3. **💾 利用缓存**: uv 的缓存机制可以显著提升重复安装的速度
4. **🔒 使用锁定文件**: 在生产环境中使用锁定文件确保环境一致性
5. **📝 使用配置文件**: 使用 `uv.toml` 配置文件管理镜像源和配置
6. **🧪 分离开发依赖**: 使用 `--dev` 标记开发依赖
7. **🌐 配置国内镜像**: 使用国内镜像源提升下载速度

