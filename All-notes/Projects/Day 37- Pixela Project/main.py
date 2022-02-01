import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "7859804175@Aryan."
USERNAME = "aryan0908"
GRAPH_ID = "graph1"

# Creating Profile (Commented because a profile with a username can be created only once)
pixela_params = {
    "token": "7859804175@Aryan.",
    "username": "aryan0908",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

# Creating Graph

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding Hours",
    "unit": "Hrs",
    "type": "float",
    "color": "sora",

}

# Authentication ourself with HTTP Header
"""It is more secure way so that our API keys don't get leak"""

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=header)
# print(response.text)

# Creating Pixels
create_pixel_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}"

now = dt.datetime.now()
formatted_date = now.strftime("%Y%m%d")

creating_pixel_params = {
    "date": formatted_date,
    "quantity": "5.2"
}

# response = requests.post(url=create_pixel_endpoint, json=creating_pixel_params, headers=header)
# print(response.text)

# Putting in the new data

pixela_put_endpoint = f"{create_pixel_endpoint}/{formatted_date}"

put_params = {
    "quantity": "6"
}

# response = requests.put(url=pixela_put_endpoint, json=put_params, headers=header)
# print(response.text)

# Deleting the existing data
delete_endpoint = f"{create_pixel_endpoint}/{formatted_date}"
response = requests.delete(url=delete_endpoint, headers=header)
print(response)


