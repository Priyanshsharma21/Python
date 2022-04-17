import random
from smtplib import SMTP
from datetime import datetime
import pandas
PLACEHOLDER = "[NAME]"

# my email
my_email = "piyuindia220@gmail.com"
password = "Piyu@412002"

# today
today = datetime.now()
today_tuple = (today.month, today.day)

# Pandas CSV
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day):data_row for (idx, data_row) in data.iterrows()}

# check if day match
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    number = random.randint(1, 3)
    with open(file=f"./letter_templates/letter_{number}.txt") as letter:
        letter_data = letter.read()
        letter_data = letter_data.replace(PLACEHOLDER, birthday_person["name"] )

    # send email
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n {letter_data}")


# finally code run at python anywhere cloud so it will run everyday at schedula time
















