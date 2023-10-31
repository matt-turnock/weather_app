import requests
import json

try:
    with open('token') as f:
        for line in f:
            api_key = line
except FileNotFoundError as error:
    print(error)

location = "London"

r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no")

json_r = json.loads(r.content)

print(f"The current temperature in {location} is {json_r['current']['temp_c']}")
