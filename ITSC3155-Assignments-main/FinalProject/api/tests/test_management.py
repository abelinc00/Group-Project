import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..dependencies.database import Base
from ..main import app  # Ensure your app instance is imported here
from ..models.order_management import OrderManagement


# Database setup for testing
@pytest.fixture(scope="module")
def test_session():
    engine = create_engine("sqlite:///:memory:")  # In-memory SQLite for tests
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client(test_session, monkeypatch):
    def override_get_db():
        yield test_session

    # Override the dependency
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


# Test the POST endpoint
def test_create_order_management_endpoint(client):
    response = client.post(
        "/order-management/",
        json={
            "order_id": 1,
            "customer_name": "John Doe",
            "order_status": "Pending"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["order_id"] == 1
    assert data["customer_name"] == "John Doe"
    assert data["order_status"] == "Pending"


# Test the GET all endpoint
def test_get_all_order_management_endpoint(client):
    response = client.get("/order-management/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


# Test the GET by ID endpoint
def test_get_order_management_by_id_endpoint(client):
    response = client.get("/order-management/1")
    assert response.status_code == 200
    data = response.json()
    assert data["order_id"] == 1
    assert data["customer_name"] == "John Doe"


# Test the PUT endpoint
def test_update_order_management_endpoint(client):
    response = client.put(
        "/order-management/1",
        json={
            "order_id": 1,
            "customer_name": "Jane Doe",
            "order_status": "Completed"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "Jane Doe"
    assert data["order_status"] == "Completed"


# Test the DELETE endpoint
def test_delete_order_management_endpoint(client):
    response = client.delete("/order-management/1")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Order management record with ID 1 deleted successfully."

    # Verify deletion
    response = client.get("/order-management/1")
    assert response.status_code == 404
