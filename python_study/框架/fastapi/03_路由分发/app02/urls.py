# @Author: Benanahai
# @Time  : 2025/3/30 17:20 
# @Desc  :


from fastapi import FastAPI, APIRouter

app02_router = APIRouter()


@app02_router.post("/login")
@app02_router.get("/login") # 为了测试方便， 实际项目中使用post
def user_login():
    return {"user": "login方法"}


@app02_router.post("/register")
@app02_router.get("/register") # 为了测试方便， 实际项目中使用post
def user_register():
    return {"user": "register方法"}
