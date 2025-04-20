import pytest
import requests
import yaml


@pytest.fixture
def client():
    class APIClient:
        def __init__(self):
            with open("config/config.yaml", "r") as file:
                config = yaml.safe_load(file)
                print("Loaded config:", config)
                self.base_url = config["base_url"]


        def get(self, endpoint, params=None, headers=None):
            url = f"{self.base_url}{endpoint}"
            response = requests.get(url, params=params, headers=headers)
            return response

        def post(self, endpoint, data=None, json=None, headers=None):
            url = f"{self.base_url}{endpoint}"
            response = requests.post(url, data=data, json=json, headers=headers)
            return response

        def put(self, endpoint, data=None, json=None, headers=None):
            url = f"{self.base_url}{endpoint}"
            response = requests.put(url, data=data, json=json, headers=headers)
            return response

        def patch(self, endpoint, data=None, json=None, headers=None):
            url = f"{self.base_url}{endpoint}"
            response = requests.patch(url, data=data, json=json, headers=headers)
            return response

        def delete(self, endpoint, headers=None):
            url = f"{self.base_url}{endpoint}"
            response = requests.delete(url, headers=headers)
            return response

    return APIClient()
