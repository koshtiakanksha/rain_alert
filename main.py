import requests
from twilio.rest import Client

api = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your_api_key"
parameters = {
    "lat": 44.314842,
    "lon": -85.602364,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

account_sid = "your_api_sid"
auth_token = "your_auth_token"
phone_number = "your_twilio_phone_no"

response = requests.get(api, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Don't forget to bring an umbrella!",
        from_=phone_number,
        to="phone number to whom you want to send the message"
    )
    print(message.status)
