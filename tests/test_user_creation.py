import allure
import pytest
from utils.api_client import ApiClient
from utils.data import unique_user, existing_user, missing_field_user

@allure.feature("Создание пользователя")
class TestUserCreation:

    @allure.story("Создать уникального пользователя")
    def test_create_unique_user(self):
        response = ApiClient.post("/auth/register", data=unique_user)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.story("Создать пользователя, который уже зарегистрирован")
    @pytest.mark.usefixtures("create_existing_user")
    def test_create_existing_user(self):
        response = ApiClient.post("/auth/register", data=existing_user)
        assert response.status_code == 403
        assert response.json().get("message") == "User already exists"

    @allure.story("Создать пользователя с пропущенным обязательным полем")
    def test_create_user_with_missing_field(self):
        response = ApiClient.post("/auth/register", data=missing_field_user)
        assert response.status_code == 400
        assert response.json().get("message") == "Email, password and name are required fields"
