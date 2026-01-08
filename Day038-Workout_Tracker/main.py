import requests
import datetime
import os
from dotenv import load_dotenv

# Create a copy of this google sheet : https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?usp=sharing

# Get your own api key from https://www.nutritionix.com/business/api
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_ID = os.getenv("API_ID")


GENDER = "YOUR_GENDER"
AGE = "YOUR_AGE"
HEIGHT_CM = "YOUR_HEIGHT_CM"
WEIGHT_KG = "YOUR_WEIGHT_KG"

ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")



exercise_text = input("Tell me which exercises you did: ")

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

params = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,                 
    "age": AGE,                      
    "gender": GENDER
}

response = requests.post(url=ENDPOINT, json=params, headers=header)
response.raise_for_status()
data = response.json()
print(data)

today = datetime.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

bearer_header = {
    "Authorization": f"Bearer {os.getenv('TOKEN')}"
}
for exercise in data["exercises"]:
    sheet_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # No Authentication
    # sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_input)

    # Bearer Authentication
    sheet_response = requests.post(
        url = SHEET_ENDPOINT,
        json= sheet_input,
        headers=bearer_header
    )
    print(sheet_response.text)

