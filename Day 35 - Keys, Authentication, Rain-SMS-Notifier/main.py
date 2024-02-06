import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = '??????????????'
auth_token = '???????????????'




parameters = {
    "lat": 47.21725,
    "lon": -1.55336,
    "appid": "??????????",
    "units": "metric",
    "exclude":["current,minutely,daily"],
}

response = requests.get(url=" http://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather = response.json()

will_rain = False

for hour in range(1,13):
    if weather['hourly'][hour]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Es regnet heute :O Regenjacke und Gummistiefel anziehen!🌧",
        from_='+18??????',
        to='+49??????'
    )
print(message.status)