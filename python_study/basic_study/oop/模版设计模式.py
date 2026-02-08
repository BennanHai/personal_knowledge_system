# @Author: Benanahai
# @Time  : 2024/11/4 23:20
import time
from abc import ABC, abstractmethod


class TemplateJob(ABC):

    @abstractmethod
    def job(self):
        pass

    # 统计计算时间的函数
    def cal_time(self):
        start = time.time()
        self.job()
        end = time.time()
        print(end - start)


class AA(TemplateJob):
    def job(self):
        num = 0
        for i in range(1, 80088981):
            num += i


class BB(TemplateJob):
    def job(self):
        num = 0
        for i in range(1, 8023131):
            num -= i

if __name__ == '__main__':

    aa = AA()
    aa.cal_time()

    bb = BB()
    bb.cal_time()
