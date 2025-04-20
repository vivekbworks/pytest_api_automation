# import requests
# import yaml

# class APIClient:
#     def __init__(self):
#         with open("config/config.yaml", "r") as file:
#             config = yaml.safe_load(file)
#             self.base_url = config["base_url"]

#     def get(self, endpoint):
#         url = f"{self.base_url}{endpoint}"
#         response = requests.get(url)
#         return response
