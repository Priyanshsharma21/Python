import requests
import os
from datetime import datetime

# --------------------AUTH INFORMATION----------------------------
API_ID = os.environ["Api_id"]
API_KEY = os.environ["API_KEY"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["Sheet_Endpoint"]
# ---------------------------------------------------------------------


# ------------------------MY INFO-------------------------------
GENDER = "male"
WEIGHT_KG = 74.5
HEIGHT_CM = 180.18
AGE = 20
# ---------------------------Nutrix Api post---------------------------------------

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

params = {
    "query": input("Tell me which exercise you did today?: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

res = requests.post(url=exercise_endpoint, json=params, headers=header)
result = res.json()
print(result)

# -------------------Sheet api post-----------------------

todays_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": todays_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_res = requests.post(url=sheet_endpoint, json=sheet_input,
                          auth=(os.environ["Username"], "piyu23@4shreyu23#445mom3$%^43dad3*&^43dadi232"))
print(sheet_res.text)

# ------------------------Auth------------------------------------
