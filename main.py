import requests

response = requests.get("http://api.icndb.com/jokes/random?exclude=explicit")
print(response.status_code)
data = response.json()
print(data["value"]["joke"])

# extra regel na eerste versie
