import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_create_menu_item():
    response = client.post("/menu_items/", json={
        "name": "Classic Sandwich",
        "price": 5.99,
        "description": "A delicious classic sandwich.",
        "category": "Sandwich"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Classic Sandwich"

def test_get_menu_item():
    response = client.get("/menu_items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Classic Sandwich"

def test_update_menu_item():
    response = client.put("/menu_items/1", json={
        "name": "Deluxe Sandwich",
        "price": 6.99,
        "description": "A deluxe version of the classic sandwich.",
        "category": "Sandwich"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Deluxe Sandwich"

def test_delete_menu_item():
    response = client.delete("/menu_items/1")
    assert response.status_code == 200
    assert response.json()["detail"] == "Item deleted successfully"
