import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "IKML12kCjq48m8yPui4opm1W-THQ6wFG"


class FlightSearch:
    def __init__(self):
        self.city_code = []

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {"apikey": TEQUILA_API_KEY}
        for city in city_name:
            query = {"term": city_name, "location_types": "city"}
            res = requests.get(url=location_endpoint, headers=header, params=query)
            result = res.json()["locations"]
            code = result[0]["code"]
            self.city_code.append(code)
        return self.city_code

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        flight_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        header = {"apikey": TEQUILA_API_KEY}
        search_query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }

        res = requests.get(url=flight_endpoint, headers=header, params=search_query)

        try :
            data = res.json()["data"][0]
        except IndexError:
            search_query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=header,
                params=search_query,
            )
            try:
                data = response.json()["data"][0]
                print(data)
            except IndexError:
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs = 1,
                    via_city = data["route"][0]["cityTo"]
                )

                return flight_data

        else:

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )

            return flight_data
