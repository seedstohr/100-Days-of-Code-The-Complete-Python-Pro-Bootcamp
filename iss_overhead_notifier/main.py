import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 40.741895
MY_LONG = -73.989308
MY_LOC = (MY_LAT, MY_LONG)
UPPER_BOUND = (MY_LAT + 5.0, MY_LONG + 5.0)
LOWER_BOUND = (MY_LAT - 5.0, MY_LONG - 5.0)
MY_TZ = "America/New_York"
FORMATTED = 0
EMAIL = ""
EMAIL_AUTH = ""
SMTP_SERVER = ""

response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()
data_iss = response_iss.json()

iss_latitude = float(data_iss["iss_position"]["latitude"])
iss_longitude = float(data_iss["iss_position"]["longitude"])

iss_location = (iss_latitude, iss_longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": MY_TZ,
    "formatted": FORMATTED

}

response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_sun.raise_for_status()

data_sun = response_sun.json()
sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    time.sleep(60)
    if (LOWER_BOUND[0] <= iss_location[0] <= UPPER_BOUND[0]) and (LOWER_BOUND[1] <= iss_location[1] <= UPPER_BOUND[1]):
        if sunset <= time_now.hour or sunrise >= time_now.hour:
            with smtplib.SMTP(SMTP_SERVER) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=EMAIL_AUTH)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=EMAIL,
                    msg=f"Subject:ISS Time\n\n"
                        f"Look up!"
                )
