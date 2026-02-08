# oh-my-zsh
- [oh-my-zsh 项目](https://github.com/ohmyzsh/ohmyzsh)
- [官方文档](https://ohmyz.sh/)
- 简介
oh-my-zsh 是一个基于 Zsh 的插件框架，它提供了许多有用的插件和主题，使 shell 操作更加方便和高效。
- 功能
oh-my-zsh 提供了以下功能：
    1. 强大的命令行补全功能，支持文件名、命令、参数等的自动补全。
    2. 丰富的插件系统，使 shell 功能更加丰富和灵活。
    3. 自定义配置选项，使 shell 符合个人需求。

## 安装
- [官方仓库安装教程](https://github.com/ohmyzsh/ohmyzsh#installation)
- [安装教程1](https://www.haoyep.com/posts/zsh-config-oh-my-zsh/)

1. Oh My Zsh 是通过在终端中运行以下命令之一来安装的。
| Method | Command |
|--------|--------|
| curl | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" |
| wget | sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" |
| fetch | sh -c "$(fetch -o - https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" |

注意，之前的任何 .zshrc 都会被重命名为 .zshrc.pre-oh-my-zsh。安装后，你可以搬家 你想保留的配置是新的.zshrc。

## 主题
oh-my-zsh 提供了许多主题，你可以在 [官方仓库](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes) 中查看。
你可以在 .zshrc 文件中设置 ZSH_THEME 变量来选择你喜欢的主题。例如：
```bash
ZSH_THEME="robbyrussell"
```
主题目录：
```bash
~/.oh-my-zsh/themes
```

## 插件
oh-my-zsh 提供了许多插件，你可以在 [官方仓库](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins) 中查看。
你可以在 .zshrc 文件中设置 plugins 变量来启用你喜欢的插件。例如：
```bash
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)
```
- 插件目录：
```bash
~/.oh-my-zsh/plugins
```
- 安装插件
    - 安装 zsh-syntax-highlighting 插件
    ```bash
    git clone https://gh-proxy.org/https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    ```
    - 安装 zsh-autosuggestions 插件
    ```bash
    git clone https://gh-proxy.org/https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    ```
- 启用插件
- 编辑 .zshrc 文件，添加插件到 plugins 变量中。
```bash
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)
```

## 配置


# python 工作目录及虚拟环境
export WORKON_HOME=/envs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/python3/bin/virtualenvwrapper.sh
export PATH="/usr/local/python3/bin:$PATH"

# NVM 配置
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # 加载 nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # 加载 nvm 命令补全
export NVM_IOJS_ORG_MIRROR=https://npmmirror.com/mirrors/iojs

