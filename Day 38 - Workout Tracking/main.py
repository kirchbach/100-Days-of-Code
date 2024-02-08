import requests
import datetime
import os

today = datetime.date.today().strftime("%d/%m/%Y")

time = datetime.datetime.now().strftime("%X")

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_parameters = {
    "query": input("Tell me which exercises you did?")
}

nutri_headers = {
    "x-app-id": "??????????",
    "x-app-key": "?????????",
    "x-remote-user-id": "0"
}

sheety_endpoint = "https://api.sheety.co/5c00955909747cea32812b92b085bbde/kopieVonMyWorkouts/workouts"


response = requests.post(url=nutri_endpoint, headers=nutri_headers, json=nutri_parameters)
print(response.text)

exercise = response.json()["exercises"][0]["name"].capitalize()
duration = response.json()["exercises"][0]["duration_min"]
calories = response.json()["exercises"][0]["nf_calories"]


sheety_parameters = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_header = {
    "Authorization": "?????????????"
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_header)
print(sheety_response.text)
