import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPAPI_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:

    def __init__(self):
        self.serp_api = os.getenv("SERP_KEY")

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "USD",
            "api_key": self.serp_api,
        }
        flight_search = requests.get(url=SERPAPI_ENDPOINT, params=query)

        if flight_search.status_code != 200:
            print(f"check_flights() response code: {flight_search.status_code}")
            return None

        data = flight_search.json()

        if "error" in data:
            print(f"API error: {data['error']}")
            return None

        return data
