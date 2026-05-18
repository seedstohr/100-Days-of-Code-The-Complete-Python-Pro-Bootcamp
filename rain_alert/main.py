import requests

API_KEY = ""
LAT = 34.7734016
LONG = -80.379904
UNITS = "imperial"
URL = "https://api.openweathermap.org/data/2.5/forecast"
CNT = 4
DISCORD_WEBHOOK = ""

parameters = {
    "lat": LAT,
    "lon": LONG,
    "units": UNITS,
    "cnt": CNT,
    "appid": API_KEY,

}

response = requests.get(URL, params=parameters)
response.raise_for_status()

weather_data = response.json()

need_umbrella = False

for i in range(4):

    if weather_data['list'][i]['weather'][0]['id'] < 600:
        need_umbrella = True

if need_umbrella:
    requests.post(DISCORD_WEBHOOK, json={"content": "Grab an umbrella."})

else:
    requests.post(DISCORD_WEBHOOK, json={"content": "No umbrella needed."})


