import requests
from datetime import datetime
from smtplib import SMTP
import time


my_email = "piyuindia220@gmail.com"
password = "Piyu@412002"

# we request for data through endpoint and get response
def is_iss_on_top():
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    # we resive the res code -> range->100 means hold on processing......
    # range-> 200 means successful request here is your data
    # range 300-> go away not permeet
    # range 400 -> you screwed up, your side problem
    # range 500-> externalserver screwed up
    #
    data = res.json()["iss_position"]
    iss_latitude = float(data["latitude"])
    iss_longitude = float(data["longitude"])

    if MY_LATS - 5 <= iss_latitude <= MY_LATS + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# ------------------------SUnSet rise-----------------------------------
# Note -> Url constant must only hava endpoint and all the parameters we will pass in parameter dict
URL = "https://api.sunrise-sunset.org/json"
MY_LATS = 22.176401
MY_LONG = 76.068199

# Now we can get particular location data by passing parameters
def is_night():
    parameters = {
        "lat": MY_LATS,
        "lng": MY_LONG,
        "formatted" : 0
    }

    res = requests.get(URL, params=parameters)
    data = res.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now_time = datetime.now().hour

    if now_time>=sunset or now_time<=sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_on_top() == True and is_night() == True:
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="piyuindia4@gmail.com",
                                msg=f"Subject: ISS is on top of you"
                                    f"\n\n Go look at the sky ISS Satellite is on top of you")
