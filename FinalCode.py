#import different libraries needed to interact with nanoleafs
import nanoleafapi
from nanoleafapi import digital_twin, discovery, Nanoleaf
import requests

#get nanoleaf ip addresses and authentication tokens and create corresponding lists
ipAddressList =  ["192.168.1.14", "192.168.1.13", "192.168.1.12", "192.168.1.10", "192.168.1.11", "192.168.1.9", "192.168.1.4", "192.168.1.5", "192.168.1.28", "192.168.1.2"]
tokenlist=[]

#create nanoleaf objects for each controller
wallList=[]
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

#assign auth tokens to their respective rows
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

    
#get weather data by scraping weather api and isolate weather description from it
api_key = "a359b2ff7cea7447b9cba4434f9b56de"
url = "http://api.openweathermap.org/data/2.5/weather?appid="+ api_key +"&q=calgary"
response = requests.get(url)
x = response.json()
if x["cod"]!='404':
    z=x['weather']
    weather_description=z[0]["description"]


#use to set effect use if statemetns in correspondance with the weather api and set to the correct effect
#effects are created using the flow function of the nanoleafapi, after being passed the correct rgb values for each row
if weather_description == "clear sky" or weather_description=="few clouds":
    print("sunny")
    row1.flow([(202,0,42), (255,17,0), (255,237,0)],3)
    row2.flow([(202,0,42), (255,17,0), (255,237,0)],3)
    row3.flow([(202,0,42), (255,17,0), (255,237,0)],3)
    row4.flow([(202,0,42), (255,17,0), (255,237,0)],3)
    row5.flow([(202,0,42), (255,17,0), (255,237,0)],3)
    row6.flow([(202,0,42), (255,17,0), (255,237,0)],3)
    row7.flow([(202,0,42), (255,17,0), (255,237,0)],3)
    row8.flow([(202,0,42), (255,17,0), (255,237,0)],3)
    row9.flow([(202,0,42), (255,17,0), (255,237,0)],3)
    row10.flow([(202,0,42), (255,17,0), (255,237,0)],3)

if weather_description== "scattered clouds" or weather_description=="broken clouds":
    print("cloudy")
    row1.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    row2.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    row3.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    row4.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    row5.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    row6.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    row7.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    row8.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    row9.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    row10.flow([(224,224,224), (160,160,160), (20,20,20)],3)
    


    
if weather_description== "shower rain" or weather_description=="rain" or weather_description== "thunder storm" or weather_description=="snow" or weather_description=="mist":
    print("Rainy")
    row1.flow([(0,128,255), (0,0,255), (51,153,255)],3)
    row2.flow([(0,128,255), (0,0,255), (51,153,255)],3)
    row3.flow([(0,128,255), (0,0,255), (51,153,255)],3)
    row4.flow([(0,128,255), (0,0,255), (51,153,255)],3)
    row5.flow([(0,128,255), (0,0,255), (51,153,255)],3)
    row6.flow([(0,128,255), (0,0,255), (51,153,255)],3)
    row7.flow([(0,128,255), (0,0,255), (51,153,255)],3)
    row8.flow([(0,128,255), (0,0,255), (51,153,255)],3)
    row9.flow([(0,128,255), (0,0,255), (51,153,255)],3)
    row10.flow([(0,128,255), (0,0,255), (51,153,255)],3)
