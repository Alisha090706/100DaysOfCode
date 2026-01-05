import requests
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
KEY = "YOUR_OPENWEATHERMAP_API_KEY"
account_id = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"


param = {
    "lon": 77.1025,
    "lat": 28.7041,
    "cnt": 4,
    "appid": KEY
}

response = requests.get(ENDPOINT, params=param)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 600:
        will_rain = True
        break

if will_rain:
    client = Client(account_id, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR_TWILIO_PHONE_NUMBER",
        to="YOUR_VERIFIED_PHONE_NUMBER"
    )
    print(message.status)