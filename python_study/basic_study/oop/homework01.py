# @Author: Benanahai
# @Time  : 2024/11/3 21:12
from math import pi
from random import random


class A01:

    def max(self, list):
        return max(list)


print(max([1, 5, 99, 55]))


class Book:
    name = None
    price = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_price(self):
        if self.price > 150:
            self.price = 150
        elif self.price > 100:
            self.price = 100

        print(self.price)


book01 = Book("红楼梦", 168)
book01.update_price()



class Circle:
    radius = None
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

cicle01 = Circle(5)
print(round(cicle01.area(),2))
print(cicle01.perimeter())



class Cal:
    num1 = None
    num2 = None
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def jian(self):
        return self.num1 - self.num2

    def chen(self):
        return  self.num1 * self.num2

    def chu(self):
        if self.num2 == 0:
            print("num2 不能为零")
        else:
            return self.num1 / self.num2

cal01 = Cal(10, 0)
print(cal01.sum())
print(cal01.jian())
print(cal01.chen())
print(cal01.chu())



class Music:
    name = None
    times = None
    def __init__(self, name, times):
        self.name = name
        self.times = times

    def play(self):
        print("啦啦啦啦啦。。")

    def info(self):
        return self.name, self.times

music = Music("红豆", 5)
music.play()
print(music.info())


