from fastapi.testclient import TestClient
from ..controllers import promotion as controller
from ..main import app
import pytest
from ..models import promotion as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_promotion(db_session):
    # Create a sample order
    order_promotion = {
        "promotion_id": "123",
        "customer_name": "John Doe",
        "promotion_code": "123456",
        "discount_percentage": "30%",
        "expiration_data": "12/31/2024"
    }

    promotion_object = model.Promotion(**order_promotion)

    # Call the create function
    created_promotion = controller.create_promotion(db_session, promotion_object)

    # Assertions
    assert created_promotion is not None
    assert created_promotion.promotion_id == "123"
    assert created_promotion.customer_name == "John Doe"
    assert created_promotion.promotion_code == "123456"
    assert created_promotion.discount_percentage == "30%"
    assert created_promotion.expiration_data == "12/31/2024"
