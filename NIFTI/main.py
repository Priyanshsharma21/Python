import requests
from twilio.rest import Client


STOCK_NAME = "TESLA"
COMPANY_NAME = "Tesla Inc"
COMPANY_NAME_2 = "RELIANCE.BSE"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_stocks = "ZB18LZB00686NE2X"
API_KEY_NEWS = "3ccdd2feb04e4191a2b89d6bd724c655"

account_sid = "AC55baa23c3f99306ec5716664ae584ec8"
auth_token = "0aca884ebdbbf048d536f394958efe10"

params = {
    "function" : "TIME_SERIES_DAILY",
    "apikey" : API_KEY_stocks,
    "symbol" : "RELIANCE.BSE"
}


r = requests.get(STOCK_ENDPOINT,params=params)
data = r.json()
date_stoke_price = data['Time Series (Daily)']

date_ss = [value for (key,value) in date_stoke_price.items()]

today_ss = date_ss[0]["4. close"]
yes_ss = date_ss[1]["4. close"]

dfference_in_stocks = float(today_ss) - float(yes_ss)
updown = None
if dfference_in_stocks<0:
    updown="🔺"
else:
    updown="🔻"


percent_diff  =round((dfference_in_stocks/float(yes_ss))*100)

if abs(percent_diff)<5:
    news_params = {
        "apiKey" : API_KEY_NEWS,
        "qInTitle" : COMPANY_NAME,
    }

    new_res = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = new_res.json()["articles"][:3]

    three_article = [f"{STOCK_NAME}: {updown} {percent_diff}%\nHeading:{article['title']}\n Brief:{article['description']}" for article in articles]

    client = Client(account_sid, auth_token)

    for article in three_article:
        message = client.messages.create(
            body = article,
            from_="+15705198771",
            to="+917999937157"
        )







