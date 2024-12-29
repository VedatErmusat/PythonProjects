import requests
from datetime import datetime
my_lat = 41.008240
my_long = 28.978359
parameters = \
    {
        "lat": my_lat,
        "lng": my_long,
    }

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print("Sunrise Time: ", sunrise)
print("Sunset Time: ", sunset)

time_now = datetime.now()
print(time_now)
