# @Author: Benanahai
# @Time  : 2024/11/3 16:35
from tkinter.font import names


class Cat:
    age = None
    name = None
    color = None
    weight = None

    def cry(self):
        print("喵喵")

# 创建Cat对象
cat01 = Cat()
# 给对象属性赋值
cat01.name = 'lsp'
cat01.age = 2
cat01.color = "red"
print(cat01.name, cat01.age, cat01.color)

cat01.cry()


cat02 = cat01
print(cat02.name, cat02.age, cat02.color)
print(f"{id(cat02.name)} {id(cat01.name)}")