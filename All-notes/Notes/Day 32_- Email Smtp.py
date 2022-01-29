import smtplib

# Connecting to our email provider smtp
"""it will be different for every email provider we can search on google our email provider smtp address"""

my_email = "test0982002@gmail.com"
password = "7859804175@Test."

with smtplib.SMTP("smtp.gmail.com") as connection:

    # Securing our connection with the email server by Transport Layer Security
    """If in midway while sending our message if someone tries to read it then rhe message will be encryped"""
    connection.starttls()

    # Loging in to our email
    connection.login(user=my_email, password=password)

    # Sending email
    connection.sendmail(from_addr=my_email,
                        to_addrs="aryan0908@yahoo.com",
                        msg="Subject:This is how you put subject.\n\nThis is how you put body")
    
    # To make the message more clear and readable we use EmailMessage from email.message module
    message = EmailMessage()
        message["Subject"] = "Happy Birthday"
        message["From"] = my_mail
        message["To"] = person_email
        message.set_content(f"Hey {person_name},\n\nHAPPY BIRTHDAY,\nHope all your birthday wishes come true."
                            f" Let's go out and celebrate this awful day 🤢. Hope that you accept the truth.\n"
                            f"Anyway it's your special day - get out there and celebrate")
        
    # Adding an image as an attachment
        with open("Neon Drinks Birthday Greeting Poster.png", "rb") as file:
            birthday_image = file.read()

        message.add_attachment(birthday_image, maintype="image", subtype="png", filename="Birthday Poster")

