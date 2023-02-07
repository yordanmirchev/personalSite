import requests
import datetime
import os

# APP_ID = "80471f2b"
# API_KEY = "dc7ad543037bbcdaa853347c94a4e9de"
#
# SHEETY_AUTH = "Basic bnVsbDpudWxs"
# SHEETY_ENDPOINT = "https://api.sheety.co/662d62744bcba66841a8f30d58efedf2/myWorkouts/workouts"

# sheet (jorangel1234567@gmail.com) https://docs.google.com/spreadsheets/d/1UhLB8rF9gjQBsDcxtHLZhrt5_y95h7uEo0JYLhgxSH0/edit#gid=0

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_AUTH =  os.environ["SHEETY_AUTH"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

GENDER = "male"
WEIGHT = 82.0
HEIGHT = 178.00
AGE = 37

trackapi_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

print(headers)
user_input = input("Enter activity information: ")
# user_input = "run 1 hour and cycle 30 minutes"

parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

request = requests.post(url=trackapi_url, json=parameters, headers=headers)
print(request.text)
result = request.json()['exercises']

sheety_url = SHEETY_ENDPOINT

sheety_header = {
    "Authorization": SHEETY_AUTH,
    "Content-Type": "application/json"
}

for data in request.json()['exercises']:
    entry = {
        "workout": {
            "date": str(datetime.date.today().strftime("%d/%m/%Y")),
            "time": str(datetime.datetime.now().strftime("%H:%M:%S")),
            "exercise": str(data["user_input"].title()),
            "duration": str(data["duration_min"]),
            "calories": str(data["nf_calories"])
        }
    }

    sheety_response = requests.post(sheety_url, json=entry, headers=sheety_header)
    print(sheety_response.status_code)
