#import different libraries needed to interact with nanoleafs
import nanoleafapi
#from nanoleaf import setup
#from nanoleaf import aurora
from nanoleafapi import digital_twin, discovery, Nanoleaf
import requests, json
#get nanoleaf ip addresses and authentication tokens and create corresponding lists
ipAddressList =  ["192.168.1.14", "192.168.1.13", "192.168.1.12", "192.168.1.10", "192.168.1.11", "192.168.1.9", "192.168.1.4", "192.168.1.5", "192.168.1.3", "192.168.1.2"]
tokenlist=[]

#create nanoleaf objects for each controller
row1= nanoleafapi.Nanoleaf(ipAddressList[0])#ip)
row2= nanoleafapi.Nanoleaf(ipAddressList[1])#ip)
row3= nanoleafapi.Nanoleaf(ipAddressList[2])#ip)
row4= nanoleafapi.Nanoleaf(ipAddressList[3])#ip)
row5= nanoleafapi.Nanoleaf(ipAddressList[4])#ip)
row6= nanoleafapi.Nanoleaf(ipAddressList[5])#ip)
row7= nanoleafapi.Nanoleaf(ipAddressList[6])#ip)
row8= nanoleafapi.Nanoleaf(ipAddressList[7])#ip)
row9= nanoleafapi.Nanoleaf(ipAddressList[8])#ip)
row10=nanoleafapi.Nanoleaf(ipAddressList[9])#ip)

row1.get_auth_token()
row2.get_auth_token()
row3.get_auth_token()
row4.get_auth_token()
row5.get_auth_token()
row6.get_auth_token()
row7.get_auth_token()
row8.get_auth_token()
row9.get_auth_token()
row10.get_auth_token()

#digital twins
dt1 = digital_twin(row1)
dt2 = digital_twin(row2)
dt3 = digital_twin(row3)
dt4 = digital_twin(row4)
dt5 = digital_twin(row5)
dt6 = digital_twin(row6)
dt7 = digital_twin(row7)
dt8 = digital_twin(row8)
dt9 = digital_twin(row9)
dt10= digital_twin(row10)
#create effect to run when it is sunny
sunny_effect_data = {
    "command": "add",
    "animName": "Sunny",
    "animType": "flow",
    "colorType": "HSB",
    "animData": None,
    "palette": [
        {
            "hue": 0,
            "saturation": 100,
            "brightness": 100
        },
        {
            "hue": 30,
            "saturation": 100,
            "brightness": 100
        },
        {
            "hue": 60,
            "saturation": 100,
            "brightness": 100
        }
    ],
    "brightnessRange": {
        "minValue": 25,
        "maxValue": 100
    },
    "transTime": {
        "minValue": 25,
        "maxValue": 100
    },
    "delayTime": {
        "minValue": 25,
        "maxValue": 100
    },
    "loop": True
}
#create effect to run when it is cloudy
cloudy_effect_data = {
    "command": "add",
    "animName": "Cloudy",
    "animType": "flow",
    "colorType": "HSB",
    "animData": None,
    "palette": [
        {
            "hue": 0,
            "saturation": 0,
            "brightness": 100
        },
        {
            "hue": 30,
            "saturation": 0,
            "brightness": 100
        },
        {
            "hue": 60,
            "saturation": 0,
            "brightness": 100
        }
    ],
    "brightnessRange": {
        "minValue": 25,
        "maxValue": 100
    },
    "transTime": {
        "minValue": 25,
        "maxValue": 100
    },
    "delayTime": {
        "minValue": 25,
        "maxValue": 100
    },
    "loop": True
}
#create effect for rainy weather
rainy_effect_data = {
    "command": "add",
    "animName": "Rainy",
    "animType": "flow",
    "colorType": "HSB",
    "animData": None,
    "palette": [
        {
            "hue": 180,
            "saturation": 100,
            "brightness": 100
        },
        {
            "hue": 210,
            "saturation": 100,
            "brightness": 100
        },
        {
            "hue": 240,
            "saturation": 100,
            "brightness": 100
        }
    ],
    "brightnessRange": {
        "minValue": 25,
        "maxValue": 100
    },
    "transTime": {
        "minValue": 25,
        "maxValue": 100
    },
    "delayTime": {
        "minValue": 25,
        "maxValue": 100
    },
    "loop": True
}
#get weather data by scraping weather api and isolate weather description from it
api_key = "a359b2ff7cea7447b9cba4434f9b56de"
url = "http://api.openweathermap.org/data/2.5/weather?appid="+ api_key +"&q=calgary"
response = requests.get(url)
x = response.json()
if x["cod"]!='404':
    z=x['weather']
    weather_description=z[0]["description"]
    print(weather_description)
#use to set effect use if statemetns in correspondance with the weather api and set to the correct effect
if weather_description== "clear sky" or weather_description=="few clouds":
    print("sunny")
    row1.set_effect(sunny_effect_data)
    row2.set_effect(sunny_effect_data)
    row3.set_effect(sunny_effect_data)
    row4.set_effect(sunny_effect_data)
    row5.set_effect(sunny_effect_data)
    row6.set_effect(sunny_effect_data)
    row7.set_effect(sunny_effect_data)
    row8.set_effect(sunny_effect_data)
    row9.set_effect(sunny_effect_data)
    row10.set_effect(sunny_effect_data)

if weather_description== "scattered clouds" or weather_description=="broken clouds":
     print("cloudy")
     row1.set_effect(cloudy_effect_data)
     row2.set_effect(cloudy_effect_data)
     row3.set_effect(cloudy_effect_data)
     row4.set_effect(cloudy_effect_data)
     row5.set_effect(cloudy_effect_data)
     row6.set_effect(cloudy_effect_data)
     row7.set_effect(cloudy_effect_data)
     row8.set_effect(cloudy_effect_data)
     row9.set_effect(cloudy_effect_data)
     row10.set_effect(cloudy_effect_data)
    
if weather_description== "shower rain" or weather_description=="rain" or weather_description== "thunder storm" or weather_description=="snow" or weather_description=="mist":
     print('rainy')
     row1.set_effect(rainy_effect_data)
     row2.set_effect(rainy_effect_data)
     row3.set_effect(rainy_effect_data)
     row4.set_effect(rainy_effect_data)
     row5.set_effect(rainy_effect_data)
     row6.set_effect(rainy_effect_data)
     row7.set_effect(rainy_effect_data)
     row8.set_effect(rainy_effect_data)
     row9.set_effect(rainy_effect_data)
     row10.set_effect(rainy_effect_data)
