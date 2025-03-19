import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# print(longitude, latitude)

response = requests.get(
    url="http://api.sunrise-sunset.org/json",
    params={"lat": 52.520008, "lng": 13.404954},
)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise, sunset)

