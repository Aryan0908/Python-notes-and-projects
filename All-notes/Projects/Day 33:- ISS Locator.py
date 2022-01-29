import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
import time

MY_LAT = 28.613939
MY_LONG = 77.209023

def near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT+5 >= latitude >= MY_LAT-5 and MY_LONG + 5 >= longitude >= MY_LONG:
        return True

def is_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response_1 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_1_data = response_1.json()
    sunrise = response_1_data["results"]["sunrise"]
    sunset = response_1_data["results"]["sunset"]

    sunrise_T = sunrise.split("T")
    sunrise_hrs_split = sunrise_T[1].split(":")
    sunrise_hrs = sunrise_hrs_split[0]

    sunset_T = sunset.split("T")
    sunset_hrs_spliter = sunset_T[1].split(":")
    sunset_hrs = int(sunset_hrs_spliter[0])

    now = datetime.now()
    now_time = now.time()
    now_hrs = int(now_time.hour)

    if 22 >= sunset_hrs or 2 <= sunrise_hrs:
        return True

while True:
    time.sleep(60)

    if near() is True and is_time() is True:
        my_email = "test0982002@gmail.com"
        password = "7859804175@Test."

        msg = EmailMessage()
        msg["Subject"] = "ISS Reminder"
        msg["From"] = my_email
        msg["To"] = "aryan0908@yahoo.com"
        msg.set_content("ISS is overhead. Go out and look")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg)




