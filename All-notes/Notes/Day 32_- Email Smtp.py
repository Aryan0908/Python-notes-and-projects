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

