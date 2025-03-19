import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


NUTRITIONIX_HEADER = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

exercise_params = {"query": exercise_text}

response = requests.post(
    url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=NUTRITIONIX_HEADER
)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

SHEETY_ENDPOINT = (
    "https://api.sheety.co/647674bb42965cebeeeaf53e29ad01bd/trackSheet/workouts"
)
SHEETY_SECRET_TOKEN = os.getenv("SHEETY_HEADER_AUTHORIZATION")
SHEETY_HEADER = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_SECRET_TOKEN,
}

for exercise in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(
        url=SHEETY_ENDPOINT, json=sheety_params, headers=SHEETY_HEADER
    )
    print(sheety_response.text)
