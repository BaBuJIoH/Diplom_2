import pytest
from utils.api_client import ApiClient
from utils.data import unique_user, existing_user

@pytest.fixture(scope="session")
def create_existing_user():
    ApiClient.post("/auth/register", data=existing_user)

@pytest.fixture
def auth_headers():
    response = ApiClient.post("/auth/login", data=existing_user)
    token = response.json().get("accessToken")
    return {"Authorization": f"Bearer {token}"}
