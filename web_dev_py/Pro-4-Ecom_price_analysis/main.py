import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP
# ---------------------------------------------------------

URL = "https://www.amazon.in/MuscleBlaze-Performance-Informed-Certified-Chocolate/dp/B09QGCD8QK/ref=sr_1_6?crid=3FVJHBGH6RNJ8&keywords=mb%2Bbiozyme&qid=1649358103&sprefix=mb%2Bbiozyme%2Caps%2C415&sr=8-6&th=1"
EMAIL = "piyuindia220@gmail.com"
PASSWORD = "Piyu@412002"
# ----------------------------------------------------------------------
header = {
    "Accept-Language" : "en-US,en;q=0.9,hi;q=0.8",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29"
}
response = requests.get(URL, headers=header)
html = response.content
soup = BeautifulSoup(html, "lxml")
# ------------------------------------------------------------------------

pro_name = soup.select_one("span#productTitle").text.strip().encode("utf-8")
price_of_pro =soup.select(".a-offscreen")[0].text
real_price = (price_of_pro.split("₹")[1])
price_float = float(real_price.split()[0].replace(",", ""))
Target_price = price_float


if price_float<Target_price:
    message = f"{pro_name} is now {price_float}"
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="piyuindia4@gmail.com",
                            msg=f"Subject: Amazon Price Alert!!! \n\n"
                                f" {pro_name} is now {price_float}")




