import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.sheety_prices_endp = "sheet1"
        self.sheety_email_endp = "users"
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_PRICES_ENDPOINT}/{self.sheety_prices_endp}")
        data = response.json()
        print(data)
        self.destination_data = data["sheet1"]
        return self.destination_data

    # ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
        )

    def get_customer_emails(self):
        response = requests.get(url=f"{SHEETY_PRICES_ENDPOINT}/{self.sheety_email_endp}")
        data = response.json()
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data