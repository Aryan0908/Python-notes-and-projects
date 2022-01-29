import pandas
import datetime as dt
import smtplib
from email.message import EmailMessage


data = pandas.read_json("birthday_list.json")
new_data = data.to_dict()

my_mail = "aryan0908@yahoo.com"
password = "7cabsnllusskgoegh"

now = dt.datetime.now()
day = now.day
month = now.month

for (key, value) in new_data.items():
    person_name = key
    person_day = int(value["day"])
    person_month = int(value["month"])
    person_email = value["email"]

    if person_day == day and person_month == month:

        message = EmailMessage()
        message["Subject"] = "Happy Birthday"
        message["From"] = my_mail
        message["To"] = person_email
        message.set_content(f"Hey {person_name},\n\nHAPPY BIRTHDAY,\nHope all your birthday wishes come true."
                            f" Let's go out and celebrate this awful day 🤢. Hope that you accept the truth.\n"
                            f"Anyway it's your special day - get out there and celebrate")

        with open("Neon Drinks Birthday Greeting Poster.png", "rb") as file:
            birthday_image = file.read()

        message.add_attachment(birthday_image, maintype="image", subtype="png", filename="Birthday Poster")
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.ehlo()
            connection.login(user=my_mail, password=password)
            connection.send_message(message)
