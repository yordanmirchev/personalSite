import requests
import datetime as dt

LATITUDE = "42.697708"
LONGTITUTE = "23.321867"


def get_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longtitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    iss_position = (longtitude, latitude)

    print(iss_position)


def get_data_with_params():
    parameters = {
        "lat": {LATITUDE},
        "lng": {LONGTITUTE},
        "formatted": 0
    }

    response = requests.get(f"https://api.sunrise-sunset.org/json?", params=parameters)
    response.raise_for_status()

    sunrise_hour = response.json()["results"]["sunrise"].split('T')[1].split(":")[0]
    # the time from request us UTC we need to adjust for Sofia time
    sunrise_hour = (int(sunrise_hour) + 2) % 24
    print(f"sunrise hour: {sunrise_hour}")

    sunset_hour = response.json()["results"]["sunset"].split('T')[1].split(":")[0]
    # the time from request us UTC we need to adjust for Sofia time
    sunrise_hour = (int(sunrise_hour) + 2) % 24
    print(f"sunset hour: {sunset_hour}")

    print(f"current_hour: {dt.datetime.now().time().hour}")


def get_for_date(date):
    response = requests.get(f"https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGTITUTE}&date={date}")
    response.raise_for_status()
    return response.json()["results"]


def get_formated_data_in_UTC_for(date):
    data = get_for_date(date)

    sunrise = data["sunrise"]
    sunset = data["sunset"]
    sunset = data["sunset"]
    day_length = data["day_length"]

    print(f"\nInformation for {date}: \n\tsunrise: {sunrise}\n\tsunset: {sunset}\n\tday length: {day_length}")


def get_sunrise_sunset():
    now = dt.date
    today = str(dt.date.today())
    tomorrow = str(dt.date.today() + dt.timedelta(1))

    # Sofia : lat: 42.697708 lng: 23.321867
    get_formated_data_in_UTC_for(today)
    get_formated_data_in_UTC_for(tomorrow)


# get_sunrise_sunset()

get_data_with_params()
