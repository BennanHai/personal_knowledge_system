# @Author: Benanahai
# @Time  : 2024/11/3 16:26

while True:
    try:
        num = int(input("输入一个数字："))
        break
    except ValueError:
        print("输入的不是数字, 请重新输入")
