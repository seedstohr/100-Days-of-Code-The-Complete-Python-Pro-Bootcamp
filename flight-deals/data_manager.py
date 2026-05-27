import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:

    def __init__(self):
        self.sheety_url = os.getenv("SHEETY_URL")
        self.destination_data = {}

    def get_sheet_data(self):

        response = requests.get(self.sheety_url)

        data = response.json()

        self.destination_data = data["sheet1"]

        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{self.sheety_url}/{row_id}",
            json=new_data,
        )