import smtplib
from twilio.rest import Client

PERSENTAGE_LIMIT: int = 0
EMAIL = "jorangel1234567@gmail.com"
PASSWORD = "tbqkchvwfoqppsna"


def get_text_ascii_only(text) -> str:
    #remove non ascii
    return  ''.join(char for char in text if ord(char) < 128)

def send_mail(recepient, subject, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=recepient,
            msg=f"Subject:{subject}\n\n{get_text_ascii_only(message)}"
        )


def send_sms(message, receiver="+359878135153"):
    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = "ACe28f22bf4e973c0679b209ea2ed3b50a"
    auth_token = "536ae0b5a51ba35e415538a7378c2f81"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = message,
        from_="+19704447472",
        to=receiver
    )

    print(f"{message.status} : {message.sid}")

