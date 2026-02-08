# @Author: Benanahai
# @Time  : 2024/11/4 20:50

class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_annual(self):
        return self.__salary * 12

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary



class Worker(Employee):
    def work(self):
        print(f"工人{self.get_name()}正在工作")



class Manager(Employee):
    __bonnus = None
    def __init__(self, name, salary, bonnus):
        super().__init__(name, salary)
        self.__bonnus = bonnus

    def manage(self):
        print(f"经理{self.get_name()}正在管理")

    def get_annual(self):
        return self.__bonnus + super().get_annual()




def show_emp_annual(e : Employee):
    print(f"{e.get_name()} 年工资 {e.get_annual()}")


def working(e : Employee):
    if isinstance(e, Worker):
        e.work()
    elif isinstance(e, Manager):
        e.manage()



worker = Worker("king", 10000)
working(worker)
show_emp_annual(worker)

manger = Manager("wzs", 1000, 500)
working(manger)
show_emp_annual(manger)
