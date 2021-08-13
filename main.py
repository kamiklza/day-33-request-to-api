import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# location = (longitude, latitude)
# print(location)

MY_LAT = 22.292923
MY_LNG = 114.271015

my_location = {"lat": MY_LAT,
               "lng": MY_LNG,
               "formatted": 0}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_location)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunrise_hour)
print(sunset_hour)


now = datetime.now()
print(now)

