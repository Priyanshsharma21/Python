from twilio.rest import Client
from smtplib import SMTP
account_sid = "AC55baa23c3f99306ec5716664ae584ec8"
auth_token = "0aca884ebdbbf048d536f394958efe10"
Verified_number = "+15705198771"
My_Number = ""
my_email = ""
password = ""

class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)


    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=Verified_number,
            to=My_Number
        )

        print(message.sid)

    def send_emails(self, emails,message, google_flight_link):
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()

            connection.login(user=my_email, password=password)

            for email in emails:
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8'))



