# 一、常用设置
## 1. 快捷键设置
在VSCode中设置快捷键有几种方法，我来为您详细介绍：

- 方法一：通过界面设置快捷键
打开快捷键编辑器：

使用快捷键 Ctrl+K Ctrl+S
或通过菜单：文件 → 首选项 → 键盘快捷键
在搜索框中输入命令名称，找到想要修改的命令

点击命令左侧的铅笔图标，然后按下想要设置的快捷键组合

- 方法二：编辑keybindings.json文件
打开键盘快捷键编辑器（ Ctrl+K Ctrl+S ）

点击右上角的 {} 图标，打开 keybindings.json 文件

在文件中添加自定义快捷键配置，格式如下：

json
[
    {
        "key": "ctrl+alt+a",
        "command": "workbench.action.files.saveAll",
        "when": ""
    },
    {
        "key": "ctrl+shift+d",
        "command": "editor.action.copyLinesDownAction",
        "when": "editorTextFocus"
    }
]








# 二、插件
## 1. Better Comments
1. 基本语法使用：
在注释中使用特定符号，自动高亮显示：

        !：红色（警告/关键问题）
        #! 待修复：内存泄漏风险

        ?：蓝色（疑问/需确认）
        #? 疑问：为何此处用冒泡排序？

        // 或 ///：灰色（普通高亮/划掉注释）
        #// 已弃用：旧算法保留备查

        *：绿色（突出显示重要信息）
        #* 性能优化点：此处可缓存结果

        TODO：橙色（待办事项）
        #TODO 待实现：添加异常处理


2. 自定义配置
修改颜色/符号：
Settings → Editor → Color Scheme → Better Comments → 调整各标记颜色。

    添加新注释类型：
    在配置页面点击 + → 输入符号（如NOTE）并设置颜色。
    """

    #! 紧急：需处理除零错误
    def calculate(a, b):
        # ? 是否应限制b的取值范围？
        #? 如果b为0，是否应返回None或抛出异常？
        return a / b

    #* 优化建议：使用LRU缓存装饰器
    def fibonacci(n):
        #// 旧递归方式，已替换为缓存版本
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)


## 2. BasedPyright
BasedPyright 是一个基于 Pyright 的 Python 静态类型检查器插件，它可以在 VSCode 中提供实时的类型检查和错误提示。

## 3. 
