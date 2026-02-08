"""
Items API tests
"""
import pytest


def test_create_item(client, auth_headers, test_user):
    """Test creating a new item"""
    response = client.post(
        "/api/v1/items/",
        json={
            "title": "Test Item",
            "description": "Test description",
            "price": 99.99,
        },
        headers=auth_headers,
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["description"] == "Test description"
    assert data["price"] == 99.99
    assert data["owner_id"] == test_user.id
    assert "id" in data


def test_create_item_unauthorized(client):
    """Test creating item without authentication"""
    response = client.post(
        "/api/v1/items/",
        json={
            "title": "Test Item",
            "description": "Test description",
        },
    )
    
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]


def test_get_items(client, auth_headers):
    """Test getting list of items"""
    # First create an item
    client.post(
        "/api/v1/items/",
        json={
            "title": "Test Item 1",
            "description": "Description 1",
        },
        headers=auth_headers,
    )
    
    client.post(
        "/api/v1/items/",
        json={
            "title": "Test Item 2",
            "description": "Description 2",
        },
        headers=auth_headers,
    )
    
    # Get items
    response = client.get("/api/v1/items/")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2


def test_get_item(client, auth_headers):
    """Test getting item by ID"""
    # Create an item
    create_response = client.post(
        "/api/v1/items/",
        json={
            "title": "Specific Item",
            "description": "Specific description",
        },
        headers=auth_headers,
    )
    item_id = create_response.json()["id"]
    
    # Get the item
    response = client.get(f"/api/v1/items/{item_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["title"] == "Specific Item"


def test_update_item(client, auth_headers):
    """Test updating item"""
    # Create an item
    create_response = client.post(
        "/api/v1/items/",
        json={
            "title": "Original Title",
            "description": "Original description",
        },
        headers=auth_headers,
    )
    item_id = create_response.json()["id"]
    
    # Update the item
    response = client.put(
        f"/api/v1/items/{item_id}",
        json={
            "title": "Updated Title",
            "description": "Updated description",
            "price": 49.99,
        },
        headers=auth_headers,
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["description"] == "Updated description"
    assert data["price"] == 49.99


def test_delete_item(client, auth_headers):
    """Test deleting item"""
    # Create an item
    create_response = client.post(
        "/api/v1/items/",
        json={
            "title": "Item to delete",
            "description": "Will be deleted",
        },
        headers=auth_headers,
    )
    item_id = create_response.json()["id"]
    
    # Delete the item
    response = client.delete(
        f"/api/v1/items/{item_id}",
        headers=auth_headers,
    )
    
    assert response.status_code == 204
    
    # Verify item is deleted
    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404


def test_get_items_by_owner(client, auth_headers, test_user):
    """Test getting items by owner ID"""
    # Create items for the test user
    client.post(
        "/api/v1/items/",
        json={
            "title": "Owner Item 1",
            "description": "Description 1",
        },
        headers=auth_headers,
    )
    
    client.post(
        "/api/v1/items/",
        json={
            "title": "Owner Item 2",
            "description": "Description 2",
        },
        headers=auth_headers,
    )
    
    # Get items by owner
    response = client.get(f"/api/v1/items/owner/{test_user.id}")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2
    for item in data:
        assert item["owner_id"] == test_user.id