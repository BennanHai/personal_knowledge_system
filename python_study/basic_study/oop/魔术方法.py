# @Author: Benanahai
# @Time  : 2024/11/4 21:27

class Manger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 重写 __str__ 魔术方法
    def __str__(self):
        # return ""
        return f"{self.name} + {self.age} + {self.gender}"


manger = Manger("老色批", 500, "男")
# 默认输出：<__main__.Manger object at 0x0000016BC7E47770>
print(manger)

# 重写 __str__ 魔术方法
print(manger)



# 没有重写 __eq__ 之前， == 默认比较两个对象内存地址是否相等
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # 为防止不是Person类型的对象值也相等
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        else:
            print("类型不一致")

person1 = Person("wzs", 23)
person2 = Person("wzs", 25)
# print(person1 == person2) # False

# 重写 __eq__
print(person1 == person2) # True

# 重写 __lt__
print(person1 < person2)

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# dog = Dog("wzs", 23)
# print(dog == person1)  #True