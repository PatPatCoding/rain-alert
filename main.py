import requests
import smtplib

my_email = "patpat.coding@gmail.com"
password = "witkgeotqwjmcwmp"

parameters = {
    "lat": 57.708870,
    "lon": 11.974560,
    "exclude": "current,minutely,daily",
    "appid": "f94574268f87e9eee7b9f7cf8cb27b9c",
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
# print(weather_data["hourly"][0:12])
# ["weather"][0]["id"]

will_rain = False
for hour_data in weather_data["hourly"][0:12]:
    for hourly_weather in hour_data["weather"]:
        if int(hourly_weather['id']) < 700:
            will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # Securing connection
        connection.starttls()
        # Loggin in
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Rain alert!\n\nBring un umbrella!"
        )
