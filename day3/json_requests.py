import json

student = {
    "name": "samyuktha",
    "age": "17",
    "course": "python"
}

json_data = json.dumps(student)
print(json_data)

# ==========================
# JSON LOADS
# ==========================
json_text = '{"city": "chennai", "country": "india"}'
data = json.loads(json_text)
print(data)
print(data["city"])
print(data["country"])

import requests
response = requests.get("https://official-joke-api.appspot.com/random_joke")
data = response.json()
print(data["setup"])
print(data["punchline"])
