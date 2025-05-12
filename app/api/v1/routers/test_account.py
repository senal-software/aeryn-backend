from fastapi.testclient import TestClient
import pytest
from app.api.v1.routers.account import router
from fastapi import FastAPI

# Create a test app
app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_get_balance():
    """
    Test the GET /balance endpoint.
    Verifies that the endpoint returns the correct structure and data types.
    """
    # Arrange
    user_id = 1
    
    # Act
    response = client.get(f"/account/balance?user_id={user_id}")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert "balance" in data
    assert isinstance(data["user_id"], int)
    assert isinstance(data["balance"], int)
    assert data["user_id"] == user_id
    assert data["balance"] == 1000

def test_get_balance_different_user():
    """
    Test the GET /balance endpoint with a different user_id.
    Verifies that the endpoint works consistently with different user IDs.
    """
    # Arrange
    user_id = 999
    
    # Act
    response = client.get(f"/account/balance?user_id={user_id}")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert data["balance"] == 1000

def test_get_transactions():
    """
    Test the GET /transactions endpoint.
    Verifies that the endpoint returns the correct structure and data types.
    """
    # Arrange
    user_id = 1
    
    # Act
    response = client.get(f"/account/transactions?user_id={user_id}")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert "transactions" in data
    assert isinstance(data["user_id"], int)
    assert isinstance(data["transactions"], list)
    assert data["user_id"] == user_id
    assert len(data["transactions"]) == 0

def test_get_transactions_different_user():
    """
    Test the GET /transactions endpoint with a different user_id.
    Verifies that the endpoint works consistently with different user IDs.
    """
    # Arrange
    user_id = 999
    
    # Act
    response = client.get(f"/account/transactions?user_id={user_id}")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert isinstance(data["transactions"], list)
    assert len(data["transactions"]) == 0
