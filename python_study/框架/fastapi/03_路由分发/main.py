# @Author: Benanahai
# @Time  : 2025/3/30 17:25 
# @Desc  :

"""
路由分发是一种将多个项目的路由方法集中管理的技术。
通过路由分发，可以将多个项目的路由方法集中管理，
从而提高代码的可读性和可维护性。


#！ 主项目：
    1. 导入子项目的路由对象
    2. 注册子项目的路由对象
    3. 启动主项目
#！ 子项目：
    1. 导入FastAPI和APIRouter
    2. 创建APIRouter对象
    3. 定义路由方法
    4. 返回路由对象
#！ 主项目和子项目的区别：
    1. 主项目是启动项目，子项目是被启动项目
    2. 主项目是主入口，子项目是子入口
"""

from fastapi import FastAPI
import uvicorn
from app03.urls import app03_router
from app02.urls import app02_router

app = FastAPI()

# prefix 统一前缀添加，子项目接口就不需要添加（不然会重复）
app.include_router(app02_router, prefix="/user", tags=["app02用户中心接口"])
app.include_router(app03_router, prefix="/shop", tags=["app03购物中心接口"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True, log_level="info")
