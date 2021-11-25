#import different libraries needed to interact with nanoleafs
from nanoleaf import setup
from nanoleaf import aurora
import requests, json
#get nanoleaf ip addresses and authentication tokens and create corresponding lists
ipAddressList = setup.find_auroras()
tokenlist=[]
for i in ipAddressList:
    tokenlist.apend(setup.generate_auth_token(ipAddressList[i-1]))
#create nanoleaf objects for each controller
row1= aurora.Aurora(ipAddressList[0], tokenlist[0])#ip)
row2= aurora.Aurora(ipAddressList[1], tokenlist[1])#ip)
row3= aurora.Aurora(ipAddressList[2], tokenlist[2])#ip)
row4= aurora.Aurora(ipAddressList[3], tokenlist[3])#ip)
row5= aurora.Aurora(ipAddressList[4], tokenlist[4])#ip)
row6= aurora.Aurora(ipAddressList[5], tokenlist[5])#ip)
row7= aurora.Aurora(ipAddressList[6], tokenlist[6])#ip)
row8= aurora.Aurora(ipAddressList[7], tokenlist[7])#ip)
row9= aurora.Aurora(ipAddressList[8], tokenlist[8])#ip)
row10=aurora.Aurora(ipAddressList[9], tokenlist[9])#ip)
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
    #row1.effect_set_raw(sunny_effect_data)
    #row2.effect_set_raw(sunny_effect_data)
    #row3.effect_set_raw(sunny_effect_data)
    #row4.effect_set_raw(sunny_effect_data)
    #row5.effect_set_raw(sunny_effect_data)
    #row6.effect_set_raw(sunny_effect_data)
    #row7.effect_set_raw(sunny_effect_data)
    #row8.effect_set_raw(sunny_effect_data)
    #row9.effect_set_raw(sunny_effect_data)
    #row10.effect_set_raw(sunny_effect_data)

if weather_description== "scattered clouds" or weather_description=="broken clouds":
     print("cloudy")
     #row1.effect_set_raw(cloudy_effect_data)
     #row2.effect_set_raw(cloudy_effect_data)
     #row3.effect_set_raw(cloudy_effect_data)
     #row4.effect_set_raw(cloudy_effect_data)
     #row5.effect_set_raw(cloudy_effect_data)
     #row6.effect_set_raw(cloudy_effect_data)
     #row7.effect_set_raw(cloudy_effect_data)
     #row8.effect_set_raw(cloudy_effect_data)
     #row9.effect_set_raw(cloudy_effect_data)
     #row10.effect_set_raw(cloudy_effect_data)
    
if weather_description== "shower rain" or weather_description=="rain" or weather_description== "thunder storm" or weather_description=="snow" or weather_description=="mist":
     print('rainy')
     #row1.effect_set_raw(rainy_effect_data)
     #row2.effect_set_raw(rainy_effect_data)
     #row3.effect_set_raw(rainy_effect_data)
     #row4.effect_set_raw(rainy_effect_data)
     #row5.effect_set_raw(rainy_effect_data)
     #row6.effect_set_raw(rainy_effect_data)
     #row7.effect_set_raw(rainy_effect_data)
     #row8.effect_set_raw(rainy_effect_data)
     #row9.effect_set_raw(rainy_effect_data)
     #row10.effect_set_raw(rainy_effect_data)