import requests
import os
from twilio.rest import Client

api_id = "bf7365ae8cfb2e84f314acc9676a1288"
account_sid = 'ACfcee8285d7485187739a940d3d7ce0a6'
auth_token = 'b1d754bf5fbe7cd9caea4029e139bbb5'

parameters = {
    "lat": -21.938400,
    "lon": -50.513930,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_id
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
hourly_data = response.json()["hourly"][0:12]


def rainy():
    for every_hour in hourly_data:
        weather_id = every_hour["weather"][0]["id"]
        if weather_id < 700:
            return True


if rainy():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Go out with umbrella",
            from_='+17752569049',
            to='+919971355870'
        )
    print(message.status)