from _commons.commons import send_mail


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, message):
        send_mail(recepient="jorangel1234567@gmail.com",
                  subject=f"Flight offer",
                  message= message)
