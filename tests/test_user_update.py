import allure
import pytest
from utils.api_client import ApiClient
from utils.data import existing_user

@allure.feature("Изменение данных пользователя")
class TestUserModification:

    @allure.story("Изменить данные с авторизацией")
    def test_modify_user_with_auth(self, auth_headers):
        new_data = {"name": "Updated User"}
        response = ApiClient.patch("/auth/user", data=new_data, headers=auth_headers)
        assert response.status_code == 200
        assert response.json().get("name") == "Updated User"

    @allure.story("Изменить данные без авторизации")
    def test_modify_user_without_auth(self):
        new_data = {"name": "Updated User"}
        response = ApiClient.patch("/auth/user", data=new_data)
        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"
