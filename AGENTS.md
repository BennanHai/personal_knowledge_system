# AGENTS.md - Personal Knowledge System

## Overview
This is a **personal knowledge system** repository for learning Python and Go programming. It's organized as a knowledge repository rather than a traditional software project. The primary focus is on educational materials, study notes, and example code.

## Repository Structure
```
personal_knowledge_system/
├── python_study/           # Python learning materials (primary focus)
│   ├── advance_study/      # Advanced topics (logging, pandas, pytest, etc.)
│   ├── basic_study/        # Basic Python concepts
│   ├── 框架/               # Framework studies (FastAPI, Scrapy)
│   └── pyproject.toml      # Python project configuration
├── go_study/               # Go language learning
│   └── 基础/               # Basic Go concepts
└── 软件及插件/             # Software and tools documentation
```

## Build, Test, and Development Commands

### Python Development
```bash
# Install dependencies using uv (modern Python package manager)
cd python_study
uv sync

# Run individual Python files
python path/to/file.py

# Run tests for FastAPI project
cd python_study/框架/fastapi/fastapi-web-app
pytest

# Run specific test file
pytest tests/test_users.py -v

# Run single test
pytest tests/test_users.py::test_create_user -v

# Run with coverage
pytest --cov=app --cov-report=html
```

### FastAPI Web Application
```bash
# Run development server
cd python_study/框架/fastapi/fastapi-web-app
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# API documentation
# - Swagger UI: http://localhost:8000/docs
# - ReDoc: http://localhost:8000/redoc
```

## Code Style Guidelines

### Python Code Style

**General Principles:**
1. **Type Hints**: Use type hints for function parameters and return values
2. **Docstrings**: Include docstrings for modules, classes, and functions
3. **Imports**: Group imports in this order: standard library, third-party, local
4. **Naming**: Use snake_case for variables/functions, PascalCase for classes

**FastAPI Project Patterns:**
```python
# Example of proper structure
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy.orm import Session

class UserBase(BaseModel):
    """Base user schema with common fields"""
    email: Optional[str] = None
    username: Optional[str] = None
    
    class Config:
        from_attributes = True

class UserService:
    """Service class with static methods"""
    
    @staticmethod
    def get_user(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID with proper error handling"""
        return db.query(User).filter(User.id == user_id).first()
```

**Basic Study Files:**
- Files may include Chinese comments and documentation
- Author headers with timestamp are common
- Focus is on educational clarity over production code quality

### Import Organization
```python
# Standard library imports
import os
import sys
from typing import Optional, List

# Third-party imports
import pandas as pd
from fastapi import FastAPI
from sqlalchemy.orm import Session

# Local application imports
from app.models.user import User
from app.schemas.user import UserCreate
```

### Error Handling
```python
# Use explicit error types
def process_data(data: dict) -> Optional[dict]:
    try:
        result = validate_and_transform(data)
        return result
    except ValidationError as e:
        logger.error(f"Validation failed: {e}")
        return None
    except Exception as e:
        logger.exception("Unexpected error in process_data")
        raise
```

### Testing Standards
```python
# Test file structure
def test_create_user(client):
    """Test creating a new user with descriptive docstring"""
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "password123",
        },
    )
    
    # Clear assertions with messages
    assert response.status_code == 201, "Should return 201 Created"
    data = response.json()
    assert "id" in data, "Response should include user ID"
    assert data["email"] == "test@example.com"
```

## Project Configuration

### Python Dependencies (pyproject.toml)
```toml
[project]
name = "my-projects"
requires-python = ">=3.13"
dependencies = [
    "pandas>=2.3.3",
    "fastapi>=0.104.0",
    "pytest>=9.0.1",
    # ... other dependencies
]

[tool.uv]
virtualenv = "D:\\envs\\py313env"
```

### Development Environment
- **Primary IDE**: VS Code with Python extension
- **Package Manager**: `uv` with Chinese mirrors configured
- **Virtual Environment**: Pre-configured at `D:\envs\py313env`

## AI Assistant Guidelines

### Context Awareness
1. **Educational Focus**: This is a learning repository. Code should be clear and educational.
2. **Chinese Support**: Some directories and documentation are in Chinese.
3. **Knowledge Organization**: Help maintain the structured learning approach.

### Code Generation Principles
1. **Educational Clarity**: Prioritize readable, well-commented code over optimization.
2. **Consistency**: Follow existing patterns in each subdirectory.
3. **Incremental Learning**: Build on concepts progressively in study materials.

### FastAPI Project Standards
1. **Follow FastAPI Best Practices**: Use dependency injection, Pydantic models, and type hints.
2. **Test Coverage**: Include comprehensive tests with fixtures.
3. **Error Handling**: Implement proper exception handling and HTTP status codes.

## No Formal Linting/Formatting
**Note**: This repository does not have formal linting (flake8, black, isort) or formatting configurations. Code quality is maintained through:
- Manual review of educational materials
- Following Python PEP 8 guidelines where practical
- Consistency within each learning module

## Git Practices
- **Branching**: Use feature branches for significant changes
- **Commits**: Descriptive commit messages in English or Chinese
- **.gitignore**: Configured to exclude IDE files, virtual environments, and build artifacts

## Agent-Specific Instructions

### When Working in This Repository:
1. **Understand the Context**: Is this a learning example or production code?
2. **Preserve Educational Value**: Maintain comments and explanations.
3. **Follow Directory Conventions**: Different areas have different standards.
4. **Test Changes**: Run relevant tests before considering work complete.
5. **Document Additions**: Update README files when adding new learning materials.

### FastAPI Project (Production-like):
- Follow modern Python web development practices
- Include comprehensive tests
- Use type hints and Pydantic models
- Implement proper error handling

### Study Materials:
- Focus on clarity and educational value
- Include Chinese explanations where helpful
- Build concepts progressively
- Reference official documentation