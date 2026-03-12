---
name: "uv-manage-project"
description: "使用 uv 初始化 Python 项目，管理依赖项，并配置带有中文镜像源的 uv.toml。当用户想要创建新的 Python 项目或设置 uv 进行依赖管理时调用。"
---

# UV 项目管理器

此技能帮助您使用 uv（一个快速的 Python 包安装器和解析器）初始化 Python 项目，管理项目依赖项，并配置 uv.toml 以通过中文镜像源获得最佳性能。

##何时使用此技能

- 用户想要创建新的 Python 项目
- 用户需要设置 uv 进行依赖管理
- 用户想要配置中文镜像源以加快下载速度
- 用户需要使用 uv 管理虚拟环境
- 用户想要从 pip/poetry 迁移到 uv

## 前提条件

- 系统上必须安装了 uv
  - 安装方式：`pip install uv` 或 `curl -LsSf https://astral.sh/uv/install.sh | sh`
- 验证版本：`uv --version`

## 核心任务

### 1. 初始化新项目

```bash
# 使用默认设置创建新项目
uv init 项目名称

# 在当前目录创建项目
uv init

# 使用特定 Python 版本创建项目（比如python 3.11）
uv init --python 3.11 项目名称

# 使用应用程序模板创建项目
uv init --app 项目名称
```

### 2. 配置 uv.toml

创建或更新 `.trae/skills/uv-manage-project/uv.toml`，使用以下配置：

```toml
# 面向中国用户的 uv.toml 配置

[pip]
# 使用中文镜像源以加快下载速度
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"
extra-index-url = [
    "https://mirrors.aliyun.com/pypi/simple/",
    "https://pypi.douban.com/simple/"
]

[cache]
# 缓存目录（可选，取消注释以自定义）
# dir = "~/.cache/uv"

[build]
# 构建后端设置
backend = "setuptools"

[virtualenvs]
# 虚拟环境设置
create = true
in-project = true
prompt = "{project_name}"

[python]
# Python 版本偏好
# default = "3.11"
```

### 3. 管理依赖项

```bash
# 添加依赖项
uv add 包名

# 添加特定版本
uv add 包名==1.2.3

# 添加开发依赖项
uv add --dev 包名

# 添加额外功能
uv add 包名[extra1,extra2]

# 移除依赖项
uv remove 包名

# 更新所有依赖项
uv lock --upgrade

# 更新特定包
uv add 包名@latest

# 安装依赖项
uv sync

# 从 requirements.txt 安装
uv pip install -r requirements.txt
```

### 4. 虚拟环境管理

```bash
# 创建虚拟环境
uv venv

# 使用特定 Python 版本创建
uv venv --python 3.11

# 激活虚拟环境（Windows）
.venv\Scripts\activate

# 激活虚拟环境（Linux/Mac）
source .venv/bin/activate

# 在虚拟环境中运行命令
uv run python script.py
uv run pytest

# 移除虚拟环境
uv venv --clear
```

### 5. 项目结构

初始化后，项目结构将为：

```
项目名称/
├── .venv/              # 虚拟环境
├── pyproject.toml      # 项目配置
├── uv.lock             # 依赖项锁定文件
├── src/
│   └── 项目名称/        # 源代码
│       └── __init__.py
└── README.md
```

### 6. 中国用户常用镜像源

| 镜像源 | URL |
|--------|-----|
| 清华大学 | https://pypi.tuna.tsinghua.edu.cn/simple |
| 阿里云 | https://mirrors.aliyun.com/pypi/simple/ |
| 豆瓣 | https://pypi.douban.com/simple/ |
| 中国科技大学 | https://pypi.mirrors.ustc.edu.cn/simple/ |
| 华为云 | https://mirrors.huaweicloud.com/repository/pypi/simple |

### 7. 故障排除

**问题：找不到 uv 命令**
```bash
# 检查安装
uv --version

# 必要时重新安装
pip install --upgrade uv
```

**问题：下载速度慢**
- 验证 uv.toml 中是否配置了镜像源
- 检查网络连接
- 尝试其他镜像源

**问题：依赖项冲突**
```bash
# 查看依赖项树
uv tree

# 手动解决冲突
uv add 包名 --resolution=lowest-direct
```

**问题：虚拟环境无法激活**
- 确保 .venv 目录存在
- 检查 Python 路径：`uv python list`
- 重新创建 venv：`uv venv --clear`

### 8. 从 pip/poetry 迁移

**从 pip 迁移：**
```bash
# 将 requirements.txt 转换为 pyproject.toml
uv add -r requirements.txt

# 或使用 pip-tools 兼容性
uv pip install -r requirements.txt
```

**从 poetry 迁移：**
```bash
# 将 pyproject.toml 从 poetry 格式转换为 uv 格式
# 手动将 [tool.poetry] 部分更新为 [project] 部分
# 然后运行：
uv sync
```

### 9. 最佳实践

1. **始终使用 uv.lock** - 将此文件提交到版本控制以实现可复现的构建
2. **固定版本** - 在生产环境中使用特定版本
3. **分离开发依赖项** - 使用 `--dev` 标志添加开发工具
4. **使用虚拟环境** - 始终在隔离环境中工作
5. **定期更新** - 定期运行 `uv lock --upgrade`
6. **镜像源** - 配置中文镜像源以加快下载速度

### 10. 示例工作流程

```bash
# 1. 初始化项目
uv init 我的项目
cd 我的项目

# 2. 配置带有中文镜像的 uv.toml
#（复制上面的 uv.toml 内容）

# 3. 添加依赖项
uv add requests pandas numpy
uv add --dev pytest black flake8

# 4. 安装依赖项
uv sync

# 5. 运行您的代码
uv run python main.py

# 6. 运行测试
uv run pytest

# 7. 更新依赖项
uv lock --upgrade
uv sync
```

## 额外资源

- uv 文档：https://github.com/astral-sh/uv
- Python 打包指南：https://packaging.python.org/
- PyPI 镜像列表：https://mirrors.tuna.tsinghua.edu.cn/help/pypi/