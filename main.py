import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API = "YOUR-API"
account_sid = "YOUR-ACCOUNT-SID"
auth_token = "YOUR-AUTHORISATION-TOKEN"

PARAMETERS = {
    "lat": YOUR-LATITUDE,
    "lon": YOUR-LONGITUDE,
    "appid": API,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today bro, take a jacket.",
        from_="+19895026250",
        to="+YOUR-PHONE-NUMBER"
    )
    print(message.status)


