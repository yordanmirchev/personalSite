import requests
import datetime
import smtplib

PERSENTAGE_LIMIT: int = 0
EMAIL = "jorangel1234567@gmail.com"
PASSWORD = "tbqkchvwfoqppsna"

COMPANY_NAME = "Tesla Inc"
SORT_BY = "popularity"
NUMBER_OF_NEWS = 3


STOCK_API_URL = "https://www.alphavantage.co/query?"
STOCK_API_FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"
STOCK = "TSLA"
STOCK_API_KEY = "RXYYLU3Z9Q4WOJ5M"

stock_parameters = {
    "function": STOCK_API_FUNCTION,
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

yesterday = str(datetime.date.today() - datetime.timedelta(1))
before_yesterday = str(datetime.date.today() - datetime.timedelta(2))

NEWS_API_KEY = "e813abbaa6e546b7b253f70a4460c684"
NEWS_API_URL = "https://newsapi.org/v2/everything?"

news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "to": yesterday,
    "sortBy": SORT_BY,
    "apiKey": NEWS_API_KEY
}


request = requests.get(STOCK_API_URL, params=stock_parameters)
request.raise_for_status()
stocks = request.json()["Time Series (Daily)"]


#print(stocks)

close_yesterday = float(stocks[yesterday]["4. close"])
close_before_yesterday = float(stocks[before_yesterday]["4. close"])
per_diff = round((close_yesterday - close_before_yesterday) * 100 / close_yesterday)

print(f"Yesteday close: {close_yesterday}\nDay before close: {close_before_yesterday}\nDiff: {per_diff} %")


news_request = requests.get(NEWS_API_URL, news_parameters)
news_request.raise_for_status()

news_list = news_request.json()["articles"][:NUMBER_OF_NEWS]


def get_news_as_string_ascii() -> str:
    text = ""
    for news in news_list:
        source = news["source"]["name"]
        text += f"source: {source}\n"
        author = news["author"]
        text += f"author: {author}\n"
        title = news["title"]
        text += f"title: {title}\n"
        description = news["description"]
        text += f"description: {description}\n"
        news_url = news["url"]
        text += f"url: {news_url}\n\n"

    #remove non ascii
    return  ''.join(char for char in text if ord(char) < 128)

def send_mail(recepient, subject, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=recepient,
            msg=f"Subject:{subject}\n\n{message}"
        )


if abs(per_diff) > PERSENTAGE_LIMIT:
    subj = STOCK
    subj += "  +" if per_diff > 0 else "  -"
    subj += f"{per_diff} %"

    send_mail(recepient=EMAIL, subject=subj, message=get_news_as_string_ascii())

