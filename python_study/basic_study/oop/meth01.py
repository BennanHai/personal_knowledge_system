# @Author: Benanahai
# @Time  : 2024/11/3 17:03

# 方法

class A:

    def cry(self, name):
        print(name + "吃屁。。。")


    def sum(self, num):
        sum = 0
        for i in range(1, num + 1):
            sum += i
        print(sum)

    def get_sum(self, a, b):
        print(a + b)


a = A()

a.cry("小果")
a.sum(1000)
a.get_sum(12, 56)
