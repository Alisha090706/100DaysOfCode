import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USERNAME ="YOUR_USERNAME"
TOKEN ="YOUR_OWN_TOKEN"
param_user = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=param_user)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "LeetCode Practice Tracker",
    "unit": "no. of problems",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# Adding a pixel to the graph
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

today = datetime.datetime.now()

pixel_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7"
}
# response = requests.post(url=PIXEL_ENDPOINT, json=pixel_param, headers=headers)
# print(response.text)

# Updating a pixel
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
update_param = {
    "quantity": "10"
}
# response = requests.put(url=UPDATE_ENDPOINT, json=update_param, headers=headers)
# print(response.text)

# Deleting a pixel
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(response.text)