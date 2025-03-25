from hmac import new
from pprint import pprint
from dotenv import load_dotenv
import requests
import os

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.__endpoint = (
            "https://api.sheety.co/647674bb42965cebeeeaf53e29ad01bd/flightDeals/prices"
        )
        self.__headers = {"Authorization": os.getenv("SHEETY_SECRET_TOKEN")}
        self.destination_data = self.get_latest_data()

    def get_latest_data(self):
        # This method will access the Google Sheet.
        response = requests.get(url=self.__endpoint, headers=self.__headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return data["prices"]

    def update_destination_data(self, city, code = None, price = None):
        # This method will be used to update the IATA codes in the Google Sheet.
        if price == None:
            price = city["lowestPrice"]
        if city["iataCode"] == None:
            code = city["iataCode"]
        new_data = {
            "price": {
                "iataCode": code,
                "lowestPrice": price,
            }
        }

        response = requests.put(
            url=f"{self.__endpoint}/{city['id']}", headers=self.__headers, json=new_data
        )
        response.raise_for_status()
