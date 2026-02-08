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
