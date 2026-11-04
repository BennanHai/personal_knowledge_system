# FastAPI 学习: 从基础到高级
- [FastAPI 官方文档](https://fastapi.org.cn/)
- [源代码](https://github.com/fastapi/fastapi)

FastAPI 是一个现代、快速（高性能）的 Web 框架，用于使用基于标准 Python 类型提示的 Python 构建 API。

- [特征](https://fastapi.org.cn/features/)
  - 基于标准 Python 类型提示
  - 自动生成交互式 API 文档（OpenAPI）
  - 高度可配置的路由系统
  - 支持异步操作（async/await）
  - 集成了常用的 Python 库（如 SQLAlchemy、Pydantic 等）

FastAPI 站在巨人的肩膀上
- Starlette 用于 Web 部分。
- Pydantic 用于数据部分。


## 安装
```bash
uv add fastapi
# 或者
pip install fastapi
```

## 快速开始
- [FastAPI 快速开始](../fastapi/01_fastapi_quickstart.py)
直接运行该文件，即可启动 FastAPI 服务。
访问地址：`http://127.0.0.1:8888`
API 文档： `http://localhost:8888/docs` 即可查看 。


## 学习
- [FastAPI 学习](https://fastapi.org.cn/learn/)
- [用户教程](https://fastapi.org.cn/tutorial/)

