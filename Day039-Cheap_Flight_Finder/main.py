from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta
import notification_manager
import time

data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

for record in sheet_data["prices"]:
    if record["iataCode"] == "":
        city_name = record["city"]
        iata_code = flight_search.get_destination(city_name)

        if iata_code:
            print(f"Found IATA code {iata_code} for city {city_name}. Updating sheet...")
            data_manager.update_data(record["id"], {
                "iataCode": iata_code
            })
            time.sleep(2)  # To avoid hitting API rate limits

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")


for destination in sheet_data["prices"]:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )