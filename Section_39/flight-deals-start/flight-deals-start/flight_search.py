from datetime import datetime, timedelta
from pprint import pprint
from dotenv import load_dotenv
import requests
import os

load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.__get_city_endpoint = (
            "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        )
        self.__search_endpoint = (
            "https://test.api.amadeus.com/v2/shopping/flight-offers"
        )
        self.__apikey = os.getenv("AMDEUS_API_KEY")
        self.__apisecret = os.getenv("AMDEUS_API_SECRET")
        self.__token = self.__get_new_token()

    def __get_new_token(self):
        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": self.__apikey,
                "client_secret": self.__apisecret,
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["access_token"]

    def get_city_code(self, city):
        headers = {"Authorization": f"Bearer {self.__token}"}
        params = {
            "keyword": city,
            "max": 1,
        }
        response = requests.get(
            url=self.__get_city_endpoint, headers=headers, params=params
        )
        response.raise_for_status()
        data = response.json()
        return data["data"][0]["iataCode"]

    def get_flight_data(self, city):
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
        headers = {"Authorization": f"Bearer {self.__token}"}
        params = {
            "originLocationCode": "LON",
            "destinationLocationCode": city,
            "departureDate": tomorrow.strftime("%Y-%m-%d"),
            "returnDate": six_month_from_today.strftime("%Y-%m-%d"),
            "adults": 1,
            "max": 10,
        }
        response = requests.get(
            url=self.__search_endpoint, headers=headers, params=params
        )
        response.raise_for_status()
        data = response.json()
        return data
