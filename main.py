import requests
import os
from twilio.rest import Client
OWM="https://api.openweathermap.org/data/2.5/weather"
api_key="e5eaaf77c484b787dbf91aaa9aa008e9"

account_sid = "AC5559bb4f8d344bbdcf4652e867dad124"
auth_token = "c08161e99342ed40ce480b01d8c54930"

parameter={
              "lat":29.216377650908733,
               "lon":70.49069724033122,
                 "appid":api_key,
    "exclude":"current,minutely,daily"

}
response=requests.get(OWM,params=parameter)
response.raise_for_status()
data=response.json()

print(data["weather"])
id=data["weather"][0]['id']
if id <600:
    will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella.☂ Faran , I Love You, I care for you Bakhtu.️☂️",
        from_='+15075007052',
        to='+923005078036'
    )

    print(message.status)
