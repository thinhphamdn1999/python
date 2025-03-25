from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

from utils import find_cheapest_flight


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

for city in data_manager.destination_data:
    if city["iataCode"] != "":
        continue
    code = flight_search.get_city_code(city["city"])
    if city["iataCode"] != code:
        data_manager.update_destination_data(city, code)

data_manager.get_latest_data()

for city in data_manager.destination_data:
    flight_data = flight_search.get_flight_data(city["iataCode"])
    cheapest_flight = find_cheapest_flight(flight_data)
    print(
        f"Low price alert! Only £{cheapest_flight.price} to fly "
        f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
    )
    if cheapest_flight.price == "N/A":
        notification_manager.send_sms(cheapest_flight)
    if (cheapest_flight.price == "N/A" and city["lowestPrice"] != "N/A") or (
        cheapest_flight.price != "N/A"
        and cheapest_flight.price < float(city["lowestPrice"])
    ):
        data_manager.update_destination_data(city, price=cheapest_flight.price)
