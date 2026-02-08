# @Author: Benanahai
# @Time  : 2025/3/30 20:19 
# @Desc  :

from fastapi import FastAPI
import uvicorn
from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03

app = FastAPI()

app.include_router(app01, prefix="/app01", tags=["01 路径参数"])
app.include_router(app02, prefix="/app02", tags=["02 查询参数"])
app.include_router(app03, prefix="/app03", tags=["03 请求体参数"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
