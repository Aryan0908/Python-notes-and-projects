import requests

# Getting hold of the api
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

# What different error code means
"""
1XX = Hold on the result is not final
2XX = Here you go everything succeeded
3XX = Go Away you don't have permission
4XX = This doesn't exist
%XX = The website did something wrong
"""

# Getting hold of the status code
response.status_code

# Raising an exception if any error code occurs
response.raise_for_status()

# Getting hold of the API data
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# Some API like sun rise and set API requires parameter with some specific names that are specified in the documentation
# we give them parameters in the form of dictionary

MY_LAT = 28.613939
MY_LONG = 77.209023

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response_1 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)