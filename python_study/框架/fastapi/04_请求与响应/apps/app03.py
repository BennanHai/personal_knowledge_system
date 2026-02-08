# @Author: Benanahai
# @Time  : 2025/3/30 21:28 
# @Desc  : 请求体参数
from typing import Union, Optional

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field
app03 = APIRouter()


class User(BaseModel):
    # 有默认值为可选， 没有默认值为必填
    name: str
    age: int = Field(default=0, ge=12, le=65) # 注意类是pydantic中的，限制age的范围，必须大于等于18小于等于65
    sex: str = "man" # 设置默认值
    birthday: Union[str, None] = None
    friends: list[str] = []
    hobbies: dict[str, str] = {}
    desc: Optional[str] = None


@app03.post("/user")
def create_user(user: User):
    print(user.name)
    print(user.model_dump())
    return user


