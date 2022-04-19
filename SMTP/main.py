from smtplib import SMTP
#
# my_email = ""
# password = ""
# # gmail smtp and creating its object
# with SMTP("smtp.gmail.com", port=587) as connection:
#
#     # secure connection
#     connection.starttls()
#
#     # login
#     connection.login(user=my_email, password=password)
#
#     # sender
#     connection.sendmail(from_addr=my_email, to_addrs="piyuindia4@gmail.com", msg="Subject:Hello\n\n this is a new email")


# --------------------------------Date time----------------------------
import datetime as dt
import random
# now = dt.datetime.now()
# year = now.year
# weekday = now.weekday()
# # print(weekday)
#
# # custome date
# date_of_birth = dt.datetime(year=2002, month=1, day=4, hour=11, minute=40, second=32, microsecond=23)
# print(date_of_birth)

# ----------------------Motivational quotes--------------------------------#
day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

now = dt.datetime.now()
curr_day = now.day
my_day = day_of_week[curr_day-4]

if my_day=="Monday":
    with open(file="quotes.txt") as quotes:
        data = quotes.readlines()
        r_quote = random.choice(data)

    my_email = ""
    password = ""

    with SMTP("smtp.gmail.com", port=587) as connection:

        connection.starttls()

        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email,
                            to_addrs="",
                            msg=f"Subject: Monday Motivation \n\n "
                                f"{r_quote}")


