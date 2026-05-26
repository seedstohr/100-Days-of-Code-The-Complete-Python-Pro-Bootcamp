import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

WORKOUT_API = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
WORKOUT_KEY = os.getenv("X-APP-KEY")
WORKOUT_ID = os.getenv("X-APP-ID")

SHEETY_API = "https://api.sheety.co/51c301c9f2f7b16511893ad295b810a9/workouts/workouts"

GENDER = "male"
AGE = 40
HEIGHT = 185
WEIGHT = 113

query = input("what exercise did you do today?")

today = datetime.now()
date = today.strftime("%Y%m%d")
time= today.strftime("%H:%M:%S")

workout_parameters = {

    "query": query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER

}

headers = {

    "x-app-id": WORKOUT_ID,
    "x-app-key": WORKOUT_KEY,

}

response = requests.post(WORKOUT_API, json=workout_parameters, headers=headers)

results = response.json()

for exercise in results["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],

         }
    }

    response_two = requests.post(SHEETY_API, json=sheety_parameters)

    print(response_two.text)
    
