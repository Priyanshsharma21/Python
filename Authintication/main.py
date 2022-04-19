import os
from smtplib import SMTP
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


# --------------Sms------------------------
def send_sms(message):
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['http_proxy']}
    account_sid = os.environ.get("MYAPI")
    auth_token = os.environ.get("MY_AUTH")
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body=f"Hello Today weather is {message}",
        from_="+15705198771",
        to=""
    )


API_Key = "f7cd520b1c47239d2ab0ab7be491dad8"
URL = "https://api.openweathermap.org/data/2.5/onecall"
my_email = ""
password = ""

parameters = {
    "lat": 22.176401,
    "lon": 76.068199,
    "exclude": "current, minutely, daily",
    "appid": API_Key
}

res = requests.get(URL, params=parameters)
res.raise_for_status()

data = res.json()
weather_slice = data["hourly"][:12]


# wether_data = data["hourly"][0]["weather"][0]


# ------------------------------------------email -----------------------------
def send_email(message):
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="",
                            msg=f"Subject:Weather Message Today\n\n {message}")


# -------------------------------email-----------------------------------------

for wether_data in weather_slice:
    condition_rain = wether_data["weather"][0]["id"]
    condition_rain = int(condition_rain)

    if 200 <= condition_rain < 300:
        send_email("Thunder Strome today , be careful")
        send_sms("Thunder Strome today , be careful")
        break
    elif 300 <= condition_rain < 400:
        send_email("Dizzle weather today, bring umbrella today")
        send_sms("Dizzle weather today, bring umbrella today")
        break
    elif 500 <= condition_rain < 600:
        send_email("Rain today,bring umbrella")
        send_sms("Rain today,bring umbrella")
        break
    elif 600 <= condition_rain < 700:
        send_email("Snow today, bring umbrella")
        send_sms("Snow today, bring umbrella")
        break
    elif 700 <= condition_rain < 800:
        send_email("Foggy weather today")
        send_sms("Foggy weather today")
        break
    elif condition_rain == 800:
        send_email("Enjoy the clear sky today")
        send_sms("Enjoy the clear sky today")
        break
    else:
        send_email("Cloudy weather today")
        send_sms("Cloudy weather today")
        break
