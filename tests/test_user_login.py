import allure
import pytest
from utils.api_client import ApiClient
from utils.data import existing_user

@allure.feature("Логин пользователя")
class TestUserLogin:

    @allure.story("Логин с верными данными")
    def test_login_valid_user(self):
        response = ApiClient.post("/auth/login", data=existing_user)
        assert response.status_code == 200
        assert response.json().get("accessToken") is not None

    @allure.story("Логин с неверными данными")
    @pytest.mark.parametrize("email, password", [
        (existing_user["email"], "wrongpassword"),
        ("wrongemail@example.com", existing_user["password"]),
    ])
    def test_login_invalid_credentials(self, email, password):
        response = ApiClient.post("/auth/login", data={"email": email, "password": password})
        assert response.status_code == 401
        assert response.json().get("message") == "email or password are incorrect"
