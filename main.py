import requests
import json

try:
    with open('token') as f:
        for line in f:
            api_key = line
except FileNotFoundError as error:
    print(error)

location = input("Please input the location, this can be postcode, zip code, area, etc: ")

r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no")

json_r = json.loads(r.content)

option = input("Do you want to display in C or F: ").lower()

if option == 'c':
    print(f"The current temperature in {location} is {json_r['current']['temp_c']}C")
elif option == 'f':
    print(f"The current temperature in {location} is {json_r['current']['temp_f']}F")
