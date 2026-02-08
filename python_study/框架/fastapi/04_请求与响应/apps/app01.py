# @Author: Benanahai
# @Time  : 2025/3/30 20:17 
# @Desc  : 路径参数

from fastapi import FastAPI, APIRouter

app01 = APIRouter()


@app01.get("/user")
def get_user():
    return {"user_id": "Benanahai"}


@app01.get("/user/1")
def get_user():
    return {"user_id": "Benanahai root"}


# user_id -- 动态路径参数
# 路径参数有顺序：谁在前先执行谁
# 如访问/user/1, 会响应上面的接口数据："user_id": "Benanahai root"
@app01.get("/user/{user_id}", )
def get_user(user_id: int):
    # 假设查询数据库
    if user_id == 1001:
        return {"user_id": user_id}
    return {"user_id": user_id}
