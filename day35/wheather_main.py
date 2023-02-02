import requests
import os
from twilio.rest import Client

LAT = 42.697708
LON = 23.321867
LANG = "bg"
# get from env variable
#OMW_API_KEY= os.getenv("OMW_API_KEY")
OMW_API_KEY= "5a99b9c852d3782788fd305728355c33"
URL = "https://api.openweathermap.org/data/2.5/forecast?"
time_to_rain = ""

print(OMW_API_KEY)

params = {
    "lat": LAT,
    "lon": LON,
    "appid": OMW_API_KEY,
    "lang" : LANG
}


result = requests.get(URL, params= params)
result.raise_for_status()

data = result.json()

def is_raining_in_12_hours():
    for entry in data["list"][:3]:
        wheather = entry["weather"][0]
        tm = entry["dt_txt"]
        id = wheather["id"]
        des = wheather["description"]
        print((tm, id, des))
        if int(id) < 700 :
            global time_to_rain
            time_to_rain = tm
            return True


    return False

if (is_raining_in_12_hours()):
    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = "ACe28f22bf4e973c0679b209ea2ed3b50a"
    auth_token = "536ae0b5a51ba35e415538a7378c2f81"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = f"It will rain at {time_to_rain} ☂️☂️",
        from_="+19704447472",
        to="+359878135153"
    )

    print(f"{message.status} : {message.sid}")
