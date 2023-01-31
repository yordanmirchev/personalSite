import requests
import datetime as dt
import smtplib
import time
from config import parameters, MARGIN, MY_LAT, MY_LONG, my_password, my_email, WAIT_TIME

iss_latitude = ""
iss_longitude = ""
sunrise_hour = 0
sunset_hour = 0
current_hour = 0


def get_iss_position():
    global iss_latitude, iss_longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.


def get_current_times():
    global sunset_hour, sunrise_hour, current_hour
    response = requests.get(f"https://api.sunrise-sunset.org/json?", params=parameters)
    response.raise_for_status()

    sunrise_hour = response.json()["results"]["sunrise"].split('T')[1].split(":")[0]
    # the time from request us UTC we need to adjust for Sofia time
    sunrise_hour = int((int(sunrise_hour) + 2) % 24)
    print(f"sunrise hour: {sunrise_hour}")

    sunset_hour = response.json()["results"]["sunset"].split('T')[1].split(":")[0]
    # the time from request us UTC we need to adjust for Sofia time
    sunset_hour = int((int(sunset_hour) + 2) % 24)
    print(f"sunset hour: {sunset_hour}")

    current_hour = int(dt.datetime.now().time().hour)

    print(f"current_hour: {current_hour}")


def is_after_sunset():
    if current_hour >= sunset_hour or current_hour<=sunrise_hour:
        print("Is after sunset")
        return True
    else:
        print("During day")
        return False


def is_iss_at_sight():
    if abs(float(MY_LAT) - iss_latitude) <= MARGIN and abs(float(MY_LONG) - iss_longitude) <= float(MARGIN):
        print("ISS is at sight.")
        return True
    else:
        print("ISS not at sight.")
        return False


def send_mail(recepient, subject, message):
    print("Sending an email")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recepient,
            msg=f"Subject:{subject}\n\n{message}"
        )




get_iss_position()
get_current_times()

while True:
    time.sleep(WAIT_TIME)
    print("Checking for ISS position and time.")
    if is_after_sunset() and is_iss_at_sight():
        send_mail(recepient=my_email, subject="Look up for ISS",
                  message=f"Current ISS position\n\tiss_latitude: {iss_latitude}\n\tiss_longitude: {iss_longitude}")
