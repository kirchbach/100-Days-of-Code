import requests
from datetime import datetime
from smtplib import *

MY_GMAIL = "??????@gmail.com"
GMAIL_PW = "*********"

MY_YAHOO = "????@yahoo.com"

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def is_iss_near():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position
while True:

    if is_iss_near() and is_night():
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=GMAIL_PW)
            connection.sendmail(from_addr=MY_GMAIL, to_addrs=MY_YAHOO, msg="Subject:Look up!\n\nThe ISS is above you in the sky.")



