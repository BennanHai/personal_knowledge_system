"""
Authentication API tests
"""
import pytest


def test_login_success(client, test_user):
    """Test successful login"""
    response = client.post(
        "/api/v1/auth/login/json",
        json={
            "username": test_user.username,
            "password": "testpassword",
        },
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client, test_user):
    """Test login with wrong password"""
    response = client.post(
        "/api/v1/auth/login/json",
        json={
            "username": test_user.username,
            "password": "wrongpassword",
        },
    )
    
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]


def test_login_nonexistent_user(client):
    """Test login with non-existent user"""
    response = client.post(
        "/api/v1/auth/login/json",
        json={
            "username": "nonexistent",
            "password": "password",
        },
    )
    
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]


def test_register_user(client):
    """Test user registration"""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "newregister",
            "password": "newpassword123",
        },
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "newregister"
    assert data["email"] == "newregister@example.com"  # Default email
    assert "id" in data


def test_get_current_user(client, auth_headers, test_user):
    """Test getting current user info"""
    response = client.get(
        "/api/v1/auth/me",
        headers=auth_headers,
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == test_user.id
    assert data["username"] == test_user.username
    assert data["email"] == test_user.email


def test_get_current_user_unauthorized(client):
    """Test getting current user without authentication"""
    response = client.get("/api/v1/auth/me")
    
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]


def test_oauth2_login(client, test_user):
    """Test OAuth2 compatible login"""
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": test_user.username,
            "password": "testpassword",
        },
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"