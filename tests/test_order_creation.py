import allure
import pytest
from utils.api_client import ApiClient

@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.story("Создать заказ с ингредиентами и авторизацией")
    def test_create_order_with_ingredients_auth(self, auth_headers):
        order_data = {"ingredients": ["1234", "5678"]}
        response = ApiClient.post("/orders", data=order_data, headers=auth_headers)
        assert response.status_code == 200

    @allure.story("Создать заказ без ингредиентов")
    def test_create_order_no_ingredients(self, auth_headers):
        response = ApiClient.post("/orders", data={}, headers=auth_headers)
        assert response.status_code == 400
        assert response.json().get("message") == "Ingredient ids must be provided"
