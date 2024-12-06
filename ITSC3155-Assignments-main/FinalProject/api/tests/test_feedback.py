from fastapi.testclient import TestClient
from ..controllers import feedback as controller
from ..main import app
import pytest
from ..models import feedback as model


client = TestClient(app)


class SessionLocal:
    def close(self):
        pass


@pytest.fixture(scope="module")
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_feedback(db):
    response = client.post(
        "/feedback",
        json={
            "order_id": 1,
            "feedback_text": "Great service!",
            "rating": 5
        },
    )
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["feedback_text"] == "Great service!"
    assert json_data["rating"] == 5
    assert json_data["order_id"] == 1
