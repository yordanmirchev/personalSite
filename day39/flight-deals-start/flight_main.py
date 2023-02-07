# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from _commons.commons import send_mail
from data_manager import *
from flight_search import FlightSearch
from flight_data import FlightData

data = DataManager()
flights = FlightSearch()
flight_data = FlightData()

city_codes = [flights.get_location_code_for_city(city) for city in data.get_city_names_from_sheet()]

#city_codes = ['PAR', 'BER', 'TYO', 'SYD', 'IST', 'KUL', 'NYC', 'SFO', 'CPT']

data.set_locaiton_codes(city_codes)

for code in city_codes:
    result = flights.search_for_flight(code)
    requested_low = data.get_locaiton_price_for_city_code(code)
    offered_low = flight_data.get_price(input=result)

    if (offered_low <= requested_low):
        send_mail(recepient="jorangel1234567@gmail.com",
                  subject=f"Flight offer for {code}",
                  message=flight_data.format_data(input=result))
