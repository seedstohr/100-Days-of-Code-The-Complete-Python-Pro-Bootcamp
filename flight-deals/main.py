import requests_cache
from notification_manager import NotificationManager
from dotenv import load_dotenv
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

load_dotenv()

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)
tomorrow = datetime.today() + timedelta(days=1)

six_months_from_today = datetime.today() + timedelta(days=180)

flight_data ={
  "engine": "google_flights",
  "departure_id": "JFK",
  "arrival_id": "SFO",
  "outbound_date": tomorrow,
  "return_date": six_months_from_today,
  "type": "1",
  "adults": "1",
  "currency": "USD",
 }

nm = NotificationManager()
ORIGIN_CITY_IATA = "CLT"

fs = FlightSearch()
flights = fs.check_flights(flight_data["departure_id"], flight_data["arrival_id"], flight_data["outbound_date"], flight_data["return_date"])
print(flights)

dm = DataManager()
sheet_data = dm.get_sheet_data()
print(sheet_data)

for destination in sheet_data:
    print(destination)
    print(f"Getting flights for {destination['city']}...")
    flights = fs.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_months_from_today.strftime("%Y-%m-%d"))
    print(f"{destination['city']}: USD {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        dm.update_lowest_price(destination["id"], cheapest_flight.price)

    nm.send_discord_update(message=f"Low price alert! Only USD {cheapest_flight.price} to fly "
                                   f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                                   f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")