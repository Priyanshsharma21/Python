import requests
URL = 'https://api.npoint.io/c790b4d5cab58020d391'

res = requests.get(f"{URL}")
data = res.json()
print(data)