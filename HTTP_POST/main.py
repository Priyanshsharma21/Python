import requests
from datetime import datetime

# 1.
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "piyu"
TOKEN = "dn3hrn3hn3nr2ss2e3"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixela_endpoint, json=user_params)
# -----------------------------------------------------------------
# 2.

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "priyansh191147"
graph_param = {
    "id": GRAPH_ID,
    "name": "Health Graph",
    "unit": "kilometer",
    "type": "float",
    "color": "shibafu"
}

# 3.
header = {
    "X-USER-TOKEN": TOKEN
}

# graph_res = requests.post(graph_endpoint, json=graph_param, headers=header, data=date)
# -----------------------------------------------------------------
# 4.
# pixcel_creation

pixcel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

date = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers you walked today? : ")
}

res_ponce = requests.post(url=pixcel_creation, json=date, headers=header)
# -----------------------------------------------------------------------------
# 5. PUT -> update pixels
# one_april = datetime.now(year="2022", month="04", day="01")
# one_april.strftime("%Y%m%d")
# put_pixels = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{one_april}"
#
# put_data = {
#     "quantity": "10.9"
# }
#
# ress = requests.put(url=put_pixels, json=put_data, headers=header)

# 6.Delete Pixcle
# delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{one_april}"
#
# resdelet = requests.delete(url=put_pixels, headers=header)






# https://pixe.la/v1/users/piyu/graphs/priyansh191147.html
