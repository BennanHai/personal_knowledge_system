# Python re 模块
Python 的 re 模块是用于处理正则表达式的标准库模块。通过 re 模块，你可以在 Python 中使用正则表达式来处理字符串。

## re 模块的基本用法
1. 导入 re 模块
```python
import re
```

2. 常用函数
- `re.match(pattern, string)`：从字符串的开头开始匹配正则表达式，返回匹配对象。
- `re.search(pattern, string)`：在字符串中搜索正则表达式，返回匹配对象。
- `re.findall(pattern, string)`：在字符串中查找所有匹配正则表达式的子串，返回一个列表。
- `re.sub(pattern, repl, string)`：将字符串中匹配正则表达式的子串替换为指定的字符串。
- `re.split(pattern, string)`：根据正则表达式分割字符串，返回一个列表。
- `re.split(pattern, string)`：根据正则表达式分割字符串，返回一个列表。

实例见 `my_re01.py` 文件
```python
import re

def test_match():
    """
    测试 re.match 函数
    re.match() 函数用于从字符串的起始位置匹配正则表达式。如果匹配成功，返回一个匹配对象；否则返回 None。
    """
    pattern = r"hello"
    # string = "world hello" # 失败， 因为起始位置不是 hello
    string = "hello world hello" # 成功
    match_obj = re.match(pattern, string)
    if match_obj:
        print("匹配成功")
    else:
        print("匹配失败")

def test_search():
    """
    测试 re.search 函数
    re.search() 函数用于在字符串中搜索正则表达式的第一个匹配项。与 re.match() 不同，re.search() 不要求匹配从字符串的起始位置开始。
    """
    pattern = r"hello"
    string = "world hello" # 成功, 起始位置不是 hello, 但是匹配到了 hello
    search_obj = re.search(pattern, string)
    if search_obj:
        print("匹配成功")
    else:
        print("匹配失败")

def test_findall():
    """
    测试 re.findall 函数
    re.findall() 函数用于在字符串中查找所有匹配正则表达式的子串，返回一个列表。
    """
    pattern = r"hello"
    string = "hello world hello"
    findall_list = re.findall(pattern, string)
    print(findall_list) # ['hello', 'hello']

def test_sub():
    """
    测试 re.sub 函数
    re.sub() 函数用于将字符串中匹配正则表达式的子串替换为指定的字符串。
    """
    pattern = r"hello"
    string = "hello world hello"
    sub_string = re.sub(pattern, "hi", string)
    print(f"替换后的字符串: {sub_string}") # hi world hi

def test_split():
    """
    测试 re.split 函数
    re.split() 函数用于根据正则表达式分割字符串，返回一个列表。
    """
    pattern = r"\s+"
    string = "hello world hello"
    split_list = re.split(pattern, string)
    print(f"分割后的列表: {split_list}") # ['hello', 'world', 'hello']
    # 实例2
    pattern = r","
    string = "a,b,c,d"
    split_list = re.split(pattern, string)
    print(f"分割后的列表: {split_list}") # ['a', 'b', 'c', 'd'] 
    # 实例3
    pattern = r"\d+"
    string = "a1b2c3d4"
    split_list = re.split(pattern, string)
    print(f"分割后的列表: {split_list}") # ['a', 'b', 'c', 'd'] 

    
if __name__ == "__main__":
    test_match()
    test_search()
    test_findall()
    test_sub()
    test_split()
```


## 正则表达式的基本语法
### 特殊字符
- `.`：匹配任意字符（除了换行符）。
- `^`：匹配字符串的开头。
- `$`：匹配字符串的结尾。
- `*`：匹配前一个字符零次或多次。
- `+`：匹配前一个字符一次或多次。
- `?`：匹配前一个字符零次或一次。
- `{m}`：匹配前一个字符恰好 m 次。
- `{m,n}`：匹配前一个字符至少 m 次，至多 n 次。
- `[]`：匹配方括号中的任意一个字符。
- `()`：分组，将多个字符作为一个整体进行匹配。
- `|`：或运算符，匹配左右任意一个表达式。
- `\`：转义字符，用于匹配特殊字符。

### 正则表达式元字符（部分）
| 元字符 | 说明 | 示例匹配 |
|-------|------|----------|
| . | 匹配任意字符（除换行符） | a.c → 'abc' |
| \d | 匹配数字 | \d+ → '123' |
| \D | 匹配非数字 | \D+ → 'abc' |
| \w | 匹配单词字符（字母、数字、下划线） | \w+ → 'Ab_1' |
| \W | 匹配非单词字符 | \W+ → '!@#' |
| \s | 匹配空白字符（空格、制表符等） | \s+ → ' \t' |
| \S | 匹配非空白字符 | \S+ → 'abc' |
| [] | 字符集合 | [A-Za-z] → 任意字母 |
| ^ | 匹配字符串开头 | ^\d+ → 开头的数字 |
| $ | 匹配字符串结尾 | \d+$ → 结尾的数字 |
| * | 匹配前一个字符0次或多次 | a* → '', 'aaa' |
| + | 匹配前一个字符1次或多次 | a+ → 'a', 'aaa' |
| ? | 匹配前一个字符0次或1次 | a? → '', 'a' |
| {m,n} | 匹配前一个字符m到n次 | a{2,3} → 'aa', 'aaa' |
| \| | 或操作 | cat\|dog → 'cat' 或 'dog' |
| () | 捕获分组 | (\d+) → 提取数字 |

