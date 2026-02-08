# @Author: Benanahai
# @Time  : 2025/3/30 20:45 
# @Desc  : 查询参数
from typing import Union, Optional

from fastapi import FastAPI, APIRouter

app02 = APIRouter()


@app02.get("/jobs")
async def get_jobs():
    return {"jobs": "job01, job02, job03"}


# 如：http://127.0.0.1:8080/app02/search?type=python&location=beijing&experience=1~3
@app02.get("/search")
async def search_job(type: str, location: str, experience: str):  # ！ 定义查询参数
    # 根据查询参数数据库查询岗位信息
    return {"type": type, "location": location, "experience": experience}


# 定义有路径参数 也有查询参数的接口, 此时type为路径参数
# http://127.0.0.1:8080/app02/search2/python?location=beijing&experience=1~3
@app02.get("/search2/{type}")
async def search_job2(type: str, location: str, experience: str):
    # 根据查询参数数据库查询岗位信息
    return {"type": type, "location": location, "experience": experience}


# 查询参数设置默认值 - 表示可选参数
# Union[str, None]表示必须为字符型，默认值为None,但是必须传；
# 可以直接使用 Optional[str] 来代替 Union[str, None]
# Union[str, None] = None 则表示可以不传
@app02.get("/search3/{type}")
async def search_job3(type: Union[str, None], gj: Optional[str], location: Union[str, None] = None, experience=None):
    # 根据查询参数数据库查询岗位信息
    return {"type": type, "location": location, "experience": experience}
