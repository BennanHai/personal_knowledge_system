# @Author: Benanahai
# @Time  : 2024/11/4 22:48
from abc import ABC, abstractmethod


# 抽象类（含有抽象方法）, 不能实例化
# 抽象类可以有普通方法
# 如果一个类继承了抽象类，则它必须实现抽象类的所有抽象方法，否则它仍然是一个抽象类
# 继承abc.ABC类; 至少需要一个抽象方法
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    # 注解声明为抽象方法
    @abstractmethod
    def cry(self):
        pass

    # 普通方法
    def hi(self):
        print('Hi, my name is {}'.format(self.name))


class Tiger(Animal):
    def cry(self):
        print(f'{self.name} Tiger is crying')


class Cat(Animal):
    def cry(self):
        print(f'{self.name} Cat is crying')


class Dog(Animal):
    # 没有实现抽象方法，仍然还是一个抽象类，不能实例化

    def ok(self):
        print(f'{self.name} Dog is ok')


tiger = Tiger("小老虎")
tiger.cry()
tiger.hi()

cat = Cat("小花猫")
cat.cry()


# 抽象类（含有抽象方法）, 不能实例化
# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'cry'
# animal = Animal("wzs")

# Dog 类没有实现抽象方法，它还是一个抽象类，不能实例化
# TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'cry
# dog = Dog("wzs")


# homework
class Employee(ABC):
    name = None
    age = None
    salary = None

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Manager(Employee):
    bonnus = None

    def __init__(self, name, age, salary, bonnus):
        super().__init__(name, age, salary)
        self.bonnus = bonnus

    def work(self):
        print(f'经理 {self.name} 正在工作')


manger = Manager("wzs", 23, 1000, 3000)
manger.work()