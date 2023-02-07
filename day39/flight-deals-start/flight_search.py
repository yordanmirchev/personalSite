import requests
import datetime

CITY_FROM = 'SOF'
FLIGHT_API_KEY = "hu3PbG3zHDBbV3aPdDFsBrqnxMSuyqa9"
FLIGHT_URL = "https://api.tequila.kiwi.com/locations/query"

headers = {
    "apikey": FLIGHT_API_KEY,
    "accept": "application/json"
}



class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    pass

    def get_location_code_for_city(self, city):
        params = {
            "active_only": "true",
            "term": city,
            "location_types": "city"
        }

        response = requests.get(url=FLIGHT_URL, params=params, headers=headers)
        response.raise_for_status()

        return response.json()["locations"][0]["code"]

    def search_for_flight(self, city):
        url = "https://api.tequila.kiwi.com/v2/search?"
        #url = "https://api.tequila.kiwi.com/v2/search?fly_from=SOF&fly_to=PAR&dateFrom=01/04/2023&dateTo=02/04/2023"

        today = str(datetime.datetime.today().strftime("%d/%m/%Y"))
        end_date = str((datetime.date.today() + datetime.timedelta(180)).strftime("%d/%m/%Y"))

        params = {
            "fly_from": CITY_FROM,
            "fly_to": city,
            "dateFrom": today,
            "dateTo": end_date,
            "limit" : 1

        }

        # "dateFrom": '01/04/2023',
        # "dateTo": '01/05/2023',

        response = requests.get(url=url, params=params, headers=headers)
        response.raise_for_status()

        return (response.json())