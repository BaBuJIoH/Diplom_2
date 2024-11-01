import allure
from utils.api_client import ApiClient

@allure.feature("Получение заказов пользователя")
class TestOrderRetrieval:

    @allure.story("Получить заказы с авторизацией")
    def test_get_orders_with_auth(self, auth_headers):
        response = ApiClient.get("/orders", headers=auth_headers)
        assert response.status_code == 200

    @allure.story("Получить заказы без авторизации")
    def test_get_orders_without_auth(self):
        response = ApiClient.get("/orders")
        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"
