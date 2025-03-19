import smtplib
import time
import requests
from datetime import datetime

MY_EMAIL = "thinhphu1234567@gmail.com"
MY_PASSWORD = "fzrhswqsitqiihdu"
SEND_TO_EMAIL = "beni09082004@gmail.com"

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


def is_close_to_iss():
    return abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    return False


while True:
    time.sleep(60)
    if is_close_to_iss() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=SEND_TO_EMAIL,
                msg="Subject: Look Up\n\nThe ISS is above you in the sky.",
            )
