# Dictonary -> Key value pair,used to store related iece of information -> Like a js object

# student = {
#     "roll": "0808cs191147",
#     "class": "T-3",
#     "subject": "Scientific Appetite"
# }
# assign value
# student["grade"] = "8.9 CGPA"
# # access data by
# print(student["roll"])
# print(student["class"])
# print(student)
# Wipe out all the data
# student = {}
# print(student)
# Update ->
# student["subject"] = "Compiler Design"
# print(student)
# # Note -> Rembember the key error
#
# for key in student:
#     print(key + " " + student[key])
# ---------------------------------------------------
# Challange1 -> Hogwards house selection
#
# student_score = {
#     "Harry": 98,
#     "Ron": 92,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }
#
# student = {}
#
# for key in student_score:
#     score = student_score[key]
#     if score > 90 and score <= 100:
#         student[key] = "gryffindor"
#     elif score > 80 and score <= 90:
#         student[key] = "slytherin"
#     elif score > 70 and score <= 80:
#         student[key] = "hufflepuff"
#     else:
#         student[key] = "ravenclaw"
#
# print(student)

# -----------------------------Nested List

# Dic and Dic
# travel_log = [{
#     "India": {
#         "cities_visited": ["Indore", "Agara", "Mumbai"],
#     },
#     "America": {
#         "cities_visited ": ["Los Angeles", "New York", "Torrance"]
#     }
# }]
#
# print(travel_log[0])
# print(travel_log[0]["India"])
# print(travel_log[0]["India"]["cities_visited"])
# print(travel_log[0]["India"]["cities_visited"][1])
# --------------------------

# challange3
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
#
# def add_new_country(country,visits,cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visited"] = visits
#     new_country["cities"] = cities
#     travel_log.append(new_country)
#
#
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# -------------------Final Challange------------------
# Challange4 -> IPL Auction
from replit import clear
import Hangman

print(Hangman.logo3)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()







