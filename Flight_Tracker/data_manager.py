import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d4cdc5386d46b4a513682cb48a0c3d3f/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/d4cdc5386d46b4a513682cb48a0c3d3f/flightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)


    def add_User(self):
        print("Welcome to Priyansh Flight Club")
        print("We will find best flight deals and email you")
        f_name = input("What is your first name:\n ")
        l_name = input("What is your last name: \n")
        email = input("Enter your email: \n")
        confirm_email = input("confirm your email: \n")


        if email == confirm_email:
            print("Welcome in the club....")

            params = {
                "user":{
                    "fname" : f_name,
                    "lname" : l_name,
                    "email" : confirm_email
                }
            }

            res = requests.post(url=SHEETY_USER_ENDPOINT, json=params)
            print(res.text)
        else:
            print("Email dose not match")

    def get_emails(self):
        customer_endpoint = SHEETY_USER_ENDPOINT
        res = requests.get(customer_endpoint)
        data = res.json()
        self.customer_data = data["users"]
        return self.customer_data