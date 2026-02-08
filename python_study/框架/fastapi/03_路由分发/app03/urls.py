# @Author: Benanahai
# @Time  : 2025/3/30 17:20 
# @Desc  :

from fastapi import FastAPI, APIRouter

app03_router = APIRouter()


@app03_router.get("/food")
def shop_food():
    return {"shop": "food方法"}


@app03_router.get("/house")
def shop_house():
    return {"shop": "house方法"}
