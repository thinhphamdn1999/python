import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = "graph1"

print(TOKEN)
print(USERNAME)

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
}
headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime(year=2025, month=2, day=3)
date_text = today.strftime("%Y%m%d")
print(date_text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params = {"date": date_text, "quantity": "200"}

# response = requests.post(
#     url=pixel_creation_endpoint, json=pixel_params, headers=headers
# )
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_text}"
new_pixel_params = {"quantity": "500"}

# response = requests.put(url=update_endpoint, json=new_pixel_params, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_text}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
