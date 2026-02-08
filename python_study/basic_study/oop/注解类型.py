# @Author: Benanahai
# @Time  : 2024/11/4 19:51


# 标注属性是 int 类型数据
num: int = 123
num2: int = "jsdkla"

my_list: list = [1, 55]
my_tuple: tuple = (1, 55, 88)
my_set: set = {1, "ds", 55}
my_dict: dict = {"name": "wzs", "age": 23}
print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)


my_list2: list[int] = [1, 55]
print(my_list2)
my_tuple2: tuple[int, int, int] = (1, 55, 88)
print(my_tuple2)
my_set2: set[int, str] = {1, "ds"}
print(my_set2)


my_list3 = [1, 55] # type: list[int]
print(my_list3)




def test(name: str):
    print("dsa:", name)

# test(123)
test("wzs")

# 返回值： int
def test01(a: int, b: int) -> int:
    result = a * b
    return result

# print(test01(2, "3"))
print(test01(2, 3))

