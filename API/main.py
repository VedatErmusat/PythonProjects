import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
#
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data. ")

"""OR"""
response.raise_for_status()  # URL yanlışsa hatayı verdirir ve if bloklarıyla uzatmaya gerek kalmaz
# Birçok hata çeşidini if'lerle yazmaktan kurtulmuş oluruz


# 1XX: Hold on
# 2XX: Here you go
# 3XX: Go away = İzin yok
# 4XX: You screwed up(Error)
# 5XX: I screwed up(Server Error)

data = response.json()
# data = response.json()["iss_position"]
# data = response.json()["iss_position"]["longitude"]
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)
