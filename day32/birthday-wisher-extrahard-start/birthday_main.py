##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import smtplib
import datetime as dt
import pandas
import os

BIRTHDAYS_CSV = "birthdays.csv"
TEMPLATES_LOCATION = "letter_templates"
my_email = "jorangel1234567@gmail.com"
my_password = "tbqkchvwfoqppsna"

birthdays = {}


def send_mail(recepient, subject, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recepient,
            msg=f"Subject:{subject}\n\n{message}"
        )


def is_birthday_today(day, month):
    now = dt.datetime.now()
    return now.day == day and now.month == month


def get_templates_multiple():
    ### We can use this to list a dir and aoutomaticaly read all the files there, we need to keep in mind the paths relative to the OS
    global letters
    try:
        for letter in os.listdir(TEMPLATES_LOCATION):
            with open(f"{TEMPLATES_LOCATION}/{letter}") as data_letter:
                letters.append(data_letter.read())
    except FileNotFoundError:
        print(f"{TEMPLATES_LOCATION}/{letter} not found.")



def get_letter_for(name):
    letters = []
    for letter in ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]:
        with open(letter) as data_letter:
            letters.append(data_letter.read())

    return random.choice(letters).replace("[NAME]", name)




try:
    with open(BIRTHDAYS_CSV) as data:
        birthdays = pandas.read_csv(data).to_dict(orient="records")
except FileNotFoundError:
    print(f"{BIRTHDAYS_CSV} not found.")

print(get_letter_for("Yordan"))


for birthday in birthdays:
    b_year = birthday.get("year")
    b_month = birthday.get("month")
    b_day = birthday.get("day")
    b_name = birthday.get("name")
    b_email = birthday.get("email")

    if is_birthday_today(month=b_month, day=b_day):
        send_mail(b_email,subject=f"Happy Birthday {b_name}!!!", message=get_letter_for(f"{b_name}"))