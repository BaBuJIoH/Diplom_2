import requests
from utils.config import BASE_URL

class ApiClient:
    @staticmethod
    def post(endpoint, data=None, headers=None):
        url = f"{BASE_URL}{endpoint}"
        return requests.post(url, json=data, headers=headers)

    @staticmethod
    def get(endpoint, headers=None):
        url = f"{BASE_URL}{endpoint}"
        return requests.get(url, headers=headers)

    @staticmethod
    def patch(endpoint, data=None, headers=None):
        url = f"{BASE_URL}{endpoint}"
        return requests.patch(url, json=data, headers=headers)
