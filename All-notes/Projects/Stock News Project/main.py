import math
import os
import requests
import smtplib
from email.message import EmailMessage


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key =  os.environ.get("NEWS_API_KEY")
my_email = "test0982002@gmail.com"
password = os.environ.get("EMAIL_PASSWORD")

news_api_from = "https://newsapi.org/"
stock_api_from = "https://www.alphavantage.co/"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = list(stock_data.values())
stock_date = list(stock_data.keys())
sliced_data = stock_data_list[:2]

yesterday_opening_date = stock_date[0] + "T09:00:00"
yesterday_closing_date = stock_date[0] + "T012:00:00"
yesterday_closing_value = float(sliced_data[0]["4. close"])
previous_closing_value = float(sliced_data[1]["4. close"])

percentage_change = math.trunc(((yesterday_closing_value - previous_closing_value) / previous_closing_value) * 100)


symbol: str
if percentage_change >= 5:
    symbol = "🔺"
elif percentage_change <= -5:
    symbol = "🔻"

if percentage_change >= 5 or percentage_change <= -5:

    news_parameters = {
        "apiKey": news_api_key,
        "q": COMPANY_NAME,
        "from": yesterday_opening_date,
        "to": yesterday_closing_date,
        "pageSize": 3
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()["articles"]

    for news in news_data:
        print(news)
        title = news["title"]
        description = news["description"]

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)

        msg = EmailMessage()
        msg["From"] = my_email
        msg["To"] = "aryan0908@yahoo.com"
        msg["Subject"] = f"TSLA: {symbol}{percentage_change}"
        msg.set_content(f"Headline: {title}\n\nBrief: {description}")

        connection.send_message(msg)








