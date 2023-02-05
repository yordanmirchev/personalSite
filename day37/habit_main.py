import requests
import datetime
import random

GRAPH_ID = "graph1"
USERNAME = "yordan"

# If special symbols used  neeed to encode in utf8 the X-USER-TOKEN in headers
TOKEN = "%QA6vXYOb8H(r"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    # need to have encoded if special symbols in the token
    "X-USER-TOKEN": TOKEN.encode('utf-8')
}


def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(f"User creation: {response.text}")
    # {"message":"Success. Let's visit https://pixe.la/@yordan , it is your profile page!","isSuccess":true}


def delete_user():
    delete_reqiest = requests.delete(f"{pixela_endpoint}/{USERNAME}", headers=headers)
    print(f"Delete user: {delete_reqiest.text}")


def create_graph():
    print(graph_endpoint)

    graph_params = {
        "id": GRAPH_ID,
        "name": "Pages read",
        "unit": "count",
        "type": "int",
        "color": "shibafu"
    }

    graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(f"Graph creation: {graph_response.text}")
    # https://pixe.la/v1/users/yordan/graphs/graph1.html


def add_pixel(quantity, date_diff=0):
    """ Puts quantity for specified date. If date_diff is provided move based on current date"""
    pixel_url = f"{graph_endpoint}/{GRAPH_ID}"
    date = (datetime.datetime.now() - datetime.timedelta(date_diff)).strftime("%Y%m%d")
    print(f"Creating pixel for {date}")

    pixel_params = {
        "date": date,
        "quantity": quantity,
    }

    pixel = requests.post(url=pixel_url, json=pixel_params, headers=headers)
    print(pixel.text)


def add_pixel_manualy():
    """ Puts quantity for specified today in console. """
    pixel_url = f"{graph_endpoint}/{GRAPH_ID}"
    date = datetime.datetime.now().strftime("%Y%m%d")
    print(f"Creating pixel for {date}")

    quantity = ""

    while not quantity.isdigit():
        quantity = input("Please enter quantity: ");

    pixel_params = {
        "date": date,
        "quantity": quantity
    }

    pixel = requests.post(url=pixel_url, json=pixel_params, headers=headers)
    print(pixel.text)


def update_pixel(quantity, date_diff=0):
    date = (datetime.datetime.now() - datetime.timedelta(date_diff)).strftime("%Y%m%d")
    print(f"Updating pixel for {date}")

    pixel_url = f"{graph_endpoint}/{GRAPH_ID}/{date}"

    pixel_params = {
        "quantity": quantity,
    }

    pixel = requests.put(url=pixel_url, json=pixel_params, headers=headers)
    print(pixel.text)


def delete_pixel(date_diff=0):
    date = (datetime.datetime.now() - datetime.timedelta(date_diff)).strftime("%Y%m%d")
    print(f"Deleting pixel for {date}")

    pixel_url = f"{graph_endpoint}/{GRAPH_ID}/{date}"

    pixel = requests.delete(url=pixel_url, headers=headers)
    print(pixel.text)


### Test functions
def add_random_data_for_days(days=1):
    """ Randomly puts data for number of days, if days not provided only for current date"""
    for i in range(0, days):
        add_pixel(str(random.randint(0,100)), date_diff=i)

def modify_random_data_for_days(days=1):
    """ Randomly modifies data for number of days, if days not provided only for current date"""
    for i in range(0, days):
        update_pixel(str(random.randint(0,100)), date_diff=i)

def delete_data_for_days(days=1):
    """ Deletes data for number of days, if days not provided only for current date"""
    for i in range(0, days):
        delete_pixel(date_diff=i)



# add_pixel_manualy()
# delete_pixel()

add_random_data_for_days(30)
#modify_random_data_for_days(10)
#delete_data_for_days(10)