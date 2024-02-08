import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

username = "????????????"
password = "????????????"

pixela_params = {
    "token": "???????????",
    "username": "????????????",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
#response = requests.post(url=pixela_endpoint, json=pixela_params)
#print(response.text)

graph_config = {
    "id": "landgraph",
    "name": "Coding Graph",
    "unit": "h",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": password
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

today = datetime.date.today().strftime("%Y%m%d")

mygraph_endpoint = "https://pixe.la/v1/users/sefbehqjn/graphs/landgraph"

pixel_params = {
    "date": today,
    "quantity": "1.5"
}

#response = requests.post(url=mygraph_endpoint, json=pixel_params, headers=headers)
#print(response.text)

pixel_change_endpoint = mygraph_endpoint + f"/{today}"

pixel_change_params = {
    "quantity": "2"
}

# response = requests.delete(url=pixel_change_endpoint, headers=headers)
# print(response.text)