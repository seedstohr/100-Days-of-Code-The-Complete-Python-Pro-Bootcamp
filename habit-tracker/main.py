import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

PIXELA_TOKEN = os.getenv("TOKEN")
PIXELA_USER = os.getenv("USERNAME")
PIXELA_GRAPH = os.getenv("GRAPH")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_ENDPOINT_GRAPH = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/{PIXELA_GRAPH}"

GOONS = "0"

today = datetime.now()
date = today.strftime("%Y%m%d")



parameters_pixela = {

    "date": date,
    "quantity": GOONS,

}

headers = {

    "X-USER-TOKEN": PIXELA_TOKEN,

}

try:
    response = requests.post(url=PIXELA_ENDPOINT_GRAPH, json=parameters_pixela, headers=headers)

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")

except Exception as err:
    print(f"Other error occurred: {err}")