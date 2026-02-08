# @Author: Benanahai
# @Time  : 2024/11/3 20:51

# class Person:
#     name = None
#     age = None
#
#     # def __init__(self):
#     #     print("无参构造器被执行了")
#
#     # 多个构造器，只有最后一个生效
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("全参构造器被执行了")
#
# p1 = Person("tom", 25)
# # p1 = Person()
# print(p1)


class Person:
    name = None
    age = None

    # def __init__(self):
    #     print("无参构造器被执行了")

    # 多个构造器，只有最后一个生效
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        else:
            self.name = None
            self.age = None


p1 = Person()
# p1 = Person("tom", 25)
print(f"{p1.name} {p1.age}")
