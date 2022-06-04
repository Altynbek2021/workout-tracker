
from datetime import datetime
import os
import requests

app_id = "9cad19b5"  # os.environ.get("APP_ID")
app_key = os.environ.get("APP_KEY")
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")


GENDER = "male"
WEIGHT = 72
HEIGHT = 175
AGE = 27

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get(
    "https://api.sheety.co/27af7d4ac37313da58eec154f157b0ae/workoutTracking/workouts")  # ("SHEET_ENDPOINT")
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
print(result)

#now_time = datetime.now().strftime("%X")


#
