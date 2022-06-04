
from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")


GENDER = "male"
WEIGHT = 72
HEIGHT = 175
AGE = 27

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("SHEET_ENDPOINT")
exercise_text = input("Tell me which exersice you did: \n")

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)
