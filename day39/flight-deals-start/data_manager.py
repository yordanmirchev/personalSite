import requests

SHEETY_AUTH = "Bearer 21eo2dkdfmwfjfjewf"
#SHEETY_ENDPOINT = "https://api.sheety.co/662d62744bcba66841a8f30d58efedf2/flightDeals/prices"
#new with
SHEETY_ENDPOINT = "https://api.sheety.co/5b98705668ee970add6ac603505d4c46/flightDeals/prices"

sheety_header = {
    "Authorization": "Bearer 21eo2dkdfmwfjfjewf",
    "Content-Type": "application/json"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        """ locations in form of {"city" : city, "code" : code , "price": price}"""
        self.locations = self.read_data()
        # print(self.locations)

        # self.locations = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 100, 'id': 2},
        #                   {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 101, 'id': 3},
        #                   {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 102, 'id': 4},
        #                   {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 103, 'id': 5},
        #                   {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 104, 'id': 6},
        #                   {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 105, 'id': 7},
        #                   {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 106, 'id': 8},
        #                   {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 107, 'id': 9},
        #                   {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 108, 'id': 10}]

    def read_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_header)
        response.raise_for_status()
        #print(response.json())
        return response.json()["prices"]

    def get_city_names_from_sheet(self):
        """ Reads all the rows from sheet and returns city names"""
        # TODO : may be a static method ?
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_header)
        response.raise_for_status()

        return [entry.get("city") for entry in self.locations]

    def set_locaiton_codes(self, codes):
        id = 1
        for code in codes:
            id += 1
            entry = {
                "price": {
                    "id": id,
                    "iataCode": code
                }
            }
            sheety_response = requests.put(url=f"{SHEETY_ENDPOINT}/{id}", json=entry, headers=sheety_header)
            print(sheety_response.json())

    def get_locaiton_price_for_city_code(self, city_code):
        return (float(
            [locaiton.get('lowestPrice') for locaiton in self.locations if locaiton.get("iataCode") == city_code][0]))
