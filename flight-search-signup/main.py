import requests_cache
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# ==================== Conserve requests and preserve your free plan ====================
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)
# ==================== Setup ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
flight_search = FlightSearch()
# Create an instance of the NotificationManager
notification_manager = NotificationManager()

customer_data = data_manager.get_customer_emails()
# Verify the name of your email column in your sheet. Yours may be different from mine
customer_email_list = [row["email?"] for row in customer_data]


# ==================== Set the Dates and Origin Airport ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
ORIGIN_CITY_IATA = "CLT"  # London Heathrow

# ==================== Find Cheap Flights ====================

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: USD {cheapest_flight.price}")

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: USD {cheapest_flight.price}")

    # Move the notification down here, outside the indirect block, with a proper price check
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        notification_manager.send_discord_update(
            message=f"Low price alert! Only USD {cheapest_flight.price} to fly "
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                    f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )

        for user in customer_email_list:

            notification_manager.send_email(
                user=user,
                message=f"Low price alert! Only USD {cheapest_flight.price} to fly "
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                    f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )