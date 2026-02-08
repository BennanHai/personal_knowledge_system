import re

def test_email():
    """
    提取邮箱
    详细解释:
    1. \b - 单词边界
    
    - 确保匹配开始于一个单词的边界，避免在其他字符串中间匹配到类似邮箱的模式
    2. [A-Za-z0-9._%+-]+ - 用户名部分
    
    - [A-Za-z0-9._%+-] ：字符集，包含：
        - A-Za-z ：大小写字母
        - 0-9 ：数字
        - ._%+- ：特殊字符（点、下划线、百分号、加号、减号）
    - + ：匹配前面的字符集1次或多次，确保用户名不为空
    3. @ - 字面量匹配
    
    - 匹配邮箱地址中的@符号
    4. [A-Za-z0-9.-]+ - 域名部分
    
    - [A-Za-z0-9.-] ：字符集，包含：
        - A-Za-z ：大小写字母
        - 0-9 ：数字
        - .- ：特殊字符（点、减号）
    - + ：匹配前面的字符集1次或多次，确保域名为不为空
    5. \. - 字面量匹配
    
    - 匹配域名中的点号（需要转义）
    6. [A-Z|a-z]{2,} - 顶级域名部分
    
    - [A-Z|a-z] ：字符集，包含大小写字母（注意：这里的 | 是多余的，因为字符集内的 | 会被视为普通字符）
    - {2,} ：匹配前面的字符集至少2次，确保顶级域名长度至少为2（如.com、.cn等）
    7. \b - 单词边界
    
    - 确保匹配结束于一个单词的边界，避免在其他字符串中间匹配到类似邮箱的模式
    ### 匹配示例
    - 匹配： user@example.com 、 user.name@example.co.uk 、 user_name123@example-domain.com
    - 不匹配： user@.com （域名部分为空）、 user@example.c （顶级域名长度不足）、 user@ example.com （包含空格）
    """
    text = "我的邮箱是：123456@qq.com, 小胖的邮箱是：123461@163.com"
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_list = re.findall(pattern, text)
    print(email_list) # ['123456@qq.com', '123461@163.com']

def test_date():
    """
    替换日期格式
    """
    date_str = "Today is 05-15-2026"
    new_str = re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3年\1月\2日', date_str)
    print(new_str)  # 输出: "Today is 2026年05月15日"

def test_compile():
    pattern = re.compile(r'''
        ^(?P<username>\w+)  # 用户名
        :(?P<password>\S+)  # 密码
        @(?P<domain>\w+\.\w+)  # 域名
    $''', re.VERBOSE)

    m = pattern.match("john:pass123@example.com")
    if m:
        print(m.groupdict())  # 输出: {'username': 'john', 'password': 'pass123', 'domain': 'example.com'}


if __name__ == "__main__":
    test_email()
    test_date()
    