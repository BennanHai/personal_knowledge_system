"""
Custom exceptions
"""
from fastapi import HTTPException, status


class AppException(HTTPException):
    """Base application exception"""
    
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail)


class NotFoundException(AppException):
    """Resource not found exception"""
    
    def __init__(self, resource: str = "Resource"):
        super().__init__(
            detail=f"{resource} not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )


class UnauthorizedException(AppException):
    """Unauthorized access exception"""
    
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


class ForbiddenException(AppException):
    """Forbidden access exception"""
    
    def __init__(self, detail: str = "Forbidden"):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_403_FORBIDDEN,
        )


class ValidationException(AppException):
    """Validation exception"""
    
    def __init__(self, detail: str = "Validation error"):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )


class ConflictException(AppException):
    """Conflict exception (e.g., duplicate resource)"""
    
    def __init__(self, detail: str = "Conflict"):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_409_CONFLICT,
        )