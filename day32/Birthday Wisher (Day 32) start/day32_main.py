import random
import smtplib
import datetime as dt

my_email = "jorangel1234567@gmail.com"
other_email = "jorangel1234567@yahoo.com"

#my_password = "Qwerty_123"
# We need app password from gmail
my_password = "tbqkchvwfoqppsna"

def send_mail(recepient, subject , message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recepient,
            msg=f"Subject:{subject}\n\n{message}"
        )
#Hello again
#now = dt.datetime.now()
#print(now)

# date = dt.datetime(year=1985, month=8, day=18)
# print(date)

#send_mail(recepient=other_email, subject="test", message="eeeehooo")

def send_weekly_quote(day_of_week):
    current_day = dt.datetime.now().weekday()
    quotes =[]
    if current_day == day_of_week:
        with open("quotes.txt") as data:
            for quote in data.readlines():
                quote = quote.replace("\n", "").strip()
                splitted_quote=quote.rsplit('-')
                quotes.append(splitted_quote)

    quote = random.choice(quotes)
    message = quote[0]
    author = quote[1]

    send_mail(recepient=other_email, subject=f"Weekly quote from {author}", message=message)




send_weekly_quote(0)