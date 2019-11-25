import requests

# register
url = "http://localhost:5000/register"
data = {'user': 'atlas', 'passw': 'paris'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, json=data, headers=headers)
print(r.text)

# login
url = "http://localhost:5000/login"
data = {'user': 'atlas', 'passw': 'paris'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, json=data, headers=headers)
print(r.text)

# create property
url = "http://localhost:5000/property/create"
property = {  "name": "fransa",
              "numberOfBedrooms": 15,
              "numberOfRooms": 28}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
e = requests.post(url, json=property, headers=headers)
print(e.text)

# get proporty
url = "http://localhost:5000/property"
data = {'name': 'fransa'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, json=data, headers=headers)
print(r.text)

# delete proporty
url = "http://localhost:5000/property/delete"
data = {'property_id': 1574634706585734}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, json=data, headers=headers)
print(r.text)



