# FastAPI Web Application

一个前后端分离的Web服务，使用FastAPI作为后端框架。(使用AI生成)

## 项目结构

```
fastapi-web-app/
├── app/                    # 应用代码
│   ├── api/               # API路由
│   │   ├── v1/           # API v1版本
│   │   └── endpoints/    # API端点
│   ├── core/             # 核心配置
│   ├── db/               # 数据库配置
│   ├── models/           # 数据库模型
│   ├── schemas/          # Pydantic模型
│   ├── services/         # 业务逻辑
│   └── utils/            # 工具函数
├── alembic/              # 数据库迁移
│   └── versions/
├── tests/                # 测试
├── frontend/             # 前端代码（可选）
├── requirements.txt      # Python依赖
├── pyproject.toml        # 项目配置
├── .env.example          # 环境变量示例
└── README.md            # 项目说明
```

## 快速开始

### 1. 环境设置

```bash
# 克隆项目
git clone <repository-url>
cd fastapi-web-app

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 复制环境变量文件
cp .env.example .env
# 编辑.env文件，配置数据库等设置
```

### 2. 数据库设置

```bash
# 初始化数据库迁移
alembic init alembic

# 创建迁移
alembic revision --autogenerate -m "Initial migration"

# 应用迁移
alembic upgrade head
```

### 3. 运行应用

```bash
# 开发模式
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 生产模式
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 4. 访问API文档

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 技术栈

- **后端框架**: FastAPI
- **数据库**: PostgreSQL / SQLite
- **ORM**: SQLAlchemy
- **认证**: JWT
- **迁移**: Alembic
- **测试**: pytest

## API设计

采用RESTful API设计原则：
- `GET /api/v1/users` - 获取用户列表
- `POST /api/v1/users` - 创建用户
- `GET /api/v1/users/{id}` - 获取用户详情
- `PUT /api/v1/users/{id}` - 更新用户
- `DELETE /api/v1/users/{id}` - 删除用户

## 开发指南

### 代码规范

```bash
# 代码格式化
black app/

# 导入排序
isort app/

# 代码检查
flake8 app/
```

### 测试

```bash
# 运行测试
pytest

# 运行特定测试
pytest tests/test_users.py -v
```

### 数据库迁移

```bash
# 创建新迁移
alembic revision --autogenerate -m "描述变更"

# 应用迁移
alembic upgrade head

# 回滚迁移
alembic downgrade -1
```

## 部署

### Docker部署

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 环境变量

参考`.env.example`文件配置生产环境变量。

## 许可证

MIT License