"""
User API tests
"""
import pytest


def test_create_user(client):
    """Test creating a new user"""
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "newpassword",
            "full_name": "New User",
        },
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert data["username"] == "newuser"
    assert data["full_name"] == "New User"
    assert "id" in data
    assert "hashed_password" not in data  # Password should not be returned


def test_create_duplicate_user(client, test_user):
    """Test creating user with duplicate email"""
    response = client.post(
        "/api/v1/users/",
        json={
            "email": test_user.email,  # Duplicate email
            "username": "differentuser",
            "password": "password123",
            "full_name": "Different User",
        },
    )
    
    assert response.status_code == 400
    assert "already exists" in response.json()["message"]


def test_get_users(client, test_user):
    """Test getting list of users"""
    response = client.get("/api/v1/users/")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_user(client, test_user):
    """Test getting user by ID"""
    response = client.get(f"/api/v1/users/{test_user.id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == test_user.id
    assert data["email"] == test_user.email
    assert data["username"] == test_user.username


def test_get_nonexistent_user(client):
    """Test getting non-existent user"""
    response = client.get("/api/v1/users/99999")
    
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_update_user(client, test_user, auth_headers):
    """Test updating user"""
    response = client.put(
        f"/api/v1/users/{test_user.id}",
        json={
            "full_name": "Updated Name",
            "email": "updated@example.com",
        },
        headers=auth_headers,
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == "Updated Name"
    assert data["email"] == "updated@example.com"


def test_delete_user(client, test_user, auth_headers):
    """Test deleting user"""
    # First create a user to delete
    create_response = client.post(
        "/api/v1/users/",
        json={
            "email": "todelete@example.com",
            "username": "todelete",
            "password": "password123",
            "full_name": "To Delete",
        },
    )
    user_id = create_response.json()["id"]
    
    # Delete the user
    response = client.delete(
        f"/api/v1/users/{user_id}",
        headers=auth_headers,
    )
    
    assert response.status_code == 204
    
    # Verify user is deleted
    get_response = client.get(f"/api/v1/users/{user_id}")
    assert get_response.status_code == 404