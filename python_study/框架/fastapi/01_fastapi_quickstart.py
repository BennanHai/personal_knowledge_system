# @Author: Benanahai
# @Time  : 2025/3/30 15:45 
# @Desc  : fastapi框架的快速入门
import sys

from fastapi import FastAPI
import uvicorn


app = FastAPI()

"""
1. 可使用uvicorn来启动服务：
     uvicorn fastapi_quickstart:app --reload  
2. 也可引入uvicorn包，添加__name__启动


"""

import os
print(sys.version)
@app.get("/")  # 路径操作装饰器
def hello_world():
    """
    快速入门
    :return: Hello World
    """
    return "Hello World"


@app.get("/sync")
async def shop():
    """
    异步测试
    :return: json
    """
    return "这是异步"


@app.get("/root")
def read_root():
    return {"hello": "world"}


if __name__ == '__main__':
    uvicorn.run("01_fastapi_quickstart:app", port=8888)  # 启动服务；模块名
