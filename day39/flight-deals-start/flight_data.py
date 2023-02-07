class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def get_price(self, input):
        return float(input["data"][0]["price"])

    def format_data(self, input):
        data = input["data"][0]

        city_fr = data["cityFrom"]
        cityCode_fr = data["cityCodeFrom"]
        city_to = data["cityTo"]
        cityCode_to = data["cityCodeTo"]
        price = data["price"]
        currency = next(iter(data["conversion"]))
        availability = data["availability"]["seats"]
        depart = data["route"][0]['local_departure'].split("T")[0]
        arrive = data["route"][-1]['local_arrival'].split("T")[0]

        return (
            f"Offer for flight from {city_fr} ({cityCode_fr}) to {city_to} ({cityCode_to}) at price {price} {currency}.\n"
            f"Available seats {availability}\n"
            f"Departure: {depart}\n"
            f"Arrival: {arrive}")
