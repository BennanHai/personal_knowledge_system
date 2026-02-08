# @Author: Benanahai
# @Time  : 2025/3/30 16:53 
# @Desc  :

"""
#！常用的路径操作装饰器方法：
    @app.get()
    @app.post()
    @app.put()    # 全部更新
    @app.patch()  # 部分更新
    @app.delete()
    @app.optional() # 可选的
    @app.options() # 预检请求
    @app.head()    # 预检请求
    @app.trace()   # 跟踪请求


#！ 路径操作装饰器方法参数：
    tags=["这是装饰器标签：post方法"],
    summary="这是post方法的摘要",
    description="这是post方法的描述",
    response_description="这是post方法的响应描述")


"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/get", tags=["这是装饰器标签：get方法"])
def test_get():
    return {"method": "get方法"}


@app.post("/post",
          tags=["这是装饰器标签：post方法"],
          summary="这是post方法的摘要",
          description="这是post方法的描述",
          response_description="这是post方法的响应描述")
def test_post():
    return {"method": "post方法"}


@app.delete("/delete",
            status_code=204,  # 设置成功响应的状态码
            deprecated=True,  # ! 标记为弃用方法
            summary="删除资源（已弃用）",
            description="此方法已弃用，请使用新的删除接口")
def test_delete():
    return {"method": "delete方法"}


@app.put("/put")
def test_put():
    return {"method": "put方法"}


@app.patch("/patch")
def test_patch():
    return {"method": "patch方法"}


@app.head("/head")
def test_head():
    return {"method": "head方法"}


@app.options("/options")
def test_options():
    return {"method": "options方法"}


if __name__ == '__main__':
    uvicorn.run("02_路径操作装饰器方法:app", port=8088)
