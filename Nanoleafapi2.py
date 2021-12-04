import nanoleafapi
from nanoleafapi import digital_twin, Nanoleaf
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE
import requests
import time

ipAddressList =  ["192.168.1.14", "192.168.1.13", "192.168.1.12", "192.168.1.10", "192.168.1.11", "192.168.1.9", "192.168.1.4", "192.168.1.5", "192.168.1.28", "192.168.1.2"]
tokenlist=[]

#create list containing each controller
#lightList=[]
#for i in range(10):
#    x=nanoleafapi.Nanoleaf(ipAddressList[i])
#    lightList.append(x)
#
##ensure each nanoleaf item has auth token assigned ot it
#for i in range(10):
#    lightList[i].get_auth_token()
#
##create a list of digital twins for each controller
#dtList=[]
#for i in range(10):
#    x=digital_twin.NanoleafDigitalTwin(lightList[i])
#    dtList.append(x)

#get weather data by scraping weather api and isolate weather description from it
api_key = "a359b2ff7cea7447b9cba4434f9b56de"
url = "http://api.openweathermap.org/data/2.5/weather?appid="+ api_key +"&q=calgary"
response = requests.get(url)
x = response.json()
if x["cod"]!='404':
    z=x['weather']
    weather_description=z[0]["description"]

#create lists of panel ids for their corresponding row. if row has 2 in it it will be split into _1 and _2 with 1 as top and 2 as lower
row1_1=[102,101,100,99,98,97,96,95,94,93,92,91,90]
row1_2=[74,75,76,77,78,79,80,81,82,83,84,85,87,88,89]
row2=[69,70,71,72,73,74,75,76,77,78,79,80,81,9,10,11,16]
row3=[44,45,46,15,19,18,17,47,48,49,50,51,52,53,54,55,56,57,58]
row4=[38,37,36,88,89,90,91,17,13,12,11,10,92,93,94,18,95,96,41,45,97]
row5=[56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78]
row6=[69,71,78,70,64,68,85,59,79,73,80,61,33,72,67,63,62,17,65,66,75,77,31]
row7=[70,52,53,54,55,56,57,58,59,17,18,60,61,62,63,64,65,66,67,68,71]
row8=[75,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79]
row9=[29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
row10_1=[39,98,76,77,78,79,80,81,82,83,84,85,86,87,100]
row10_2=[75,55,97,96,95,94,93,92,91,90,89,10,88]

#compile into list
rows=[row1_1,row1_2,row2,row3,row4,row5,row6,row7,row8,row9,row10_1,row10_2]

#create while loop which moves "cloud" over with time delay for the whole length and 
# syncs

#dtList index should be one lower than rows as rows starts with 2 rows for controller 1

#want cloud to move across and have one which moves across but two steps behind a few rows undrr
if weather_description == "clear sky" or weather_description=="few clouds":
    print("sunny")
    for i in range(len(dtList)):
        dtList[i].set_all_colors(LIGHT_BLUE)
    for i in range(len(rows[3])):
        if i == (len(rows[3]))-1:
            dtList[2].set_color((rows[3][i]), ORANGE)
            pass
        else:
            dtList[2].set_color((rows[3][i]), ORANGE)
            dtList[2].set_color((rows[3][i+1]), ORANGE)
    for i in range(len(rows[4])):
        if i == (len(rows[4]))-1:
            dtList[3].set_color((rows[4][i]), ORANGE)
            pass
        else:
            dtList[3].set_color((rows[4][i]), ORANGE)
            dtList[3].set_color((rows[4][i+1]), ORANGE)
    for i in range(len(dtList)):
        dtList[i].sync()
    time.sleep(0.4)

if weather_description== "scattered clouds" or weather_description=="broken clouds":
    print("cloudy")
    for i in range(len(dtList)):
        dtList[i].set_all_colors(LIGHT_BLUE)
    for i in range(len(rows[3])):
        if i == (len(rows[3]))-1:
            dtList[2].set_color((rows[3][i]), (155,155,155))
            pass
        else:
            dtList[2].set_color((rows[3][i]), (155,155,155))
            dtList[2].set_color((rows[3][i+1]), (155,155,155))
    for i in range(len(rows[5])):
        if i == (len(rows[5]))-1:
            dtList[4].set_color((rows[5][i]), (144, 144, 144))
        else:
            dtList[4].set_color((rows[5][i]), (144,144,144))
            dtList[4].set_color((rows[5][i+1]), (144,144,144))
    for i in range(len(dtList)):
        dtList[i].sync()     
    time.sleep(0.4)


#for raindrops to fall vertically, it needs to add one to the id index each time until row 4(index 5) and then should subtract one after row 5(index 6)
#for that to happen, maybe have two loops with a counter
if weather_description== "shower rain" or weather_description=="rain" or weather_description== "thunder storm" or weather_description=="snow" or weather_description=="mist":
    print("Rainy")
    for i in range(len(dtList)):
        dtList[i].set_all_colors(99,99,99)
    d1rowcount=1
    for i in range(len(rows)):
        d1idcount=0
        while d1rowcount<=5:
            if d1rowcount==1:
                dtList[i].set_color((rows[d1rowcount][d1idcount]), BLUE)
                dtList[i].set_color((rows[d1rowcount-1][d1idcount-1]), BLUE)
            else:
                dtList[i].set_color((rows[d1rowcount][d1idcount]), BLUE)
            d1rowcount+=1
            d1idcount+=1
        while d1rowcount>5:
            if d1rowcount ==10:
                dtList[i].set_color((rows[d1rowcount][d1idcount]), BLUE)
                dtList[i].set_color((rows[d1rowcount+1][d1idcount+1]), BLUE)
            else:
                dtList[i].set_color((rows[d1rowcount+1][d1idcount+1]), BLUE)
            d1rowcount+=1
            d1idcount-=1
    d2rowcount=1
    for i in range(len(rows)):
        d2idcount=2
        while d2rowcount<=5:
            if d2rowcount==1:
                dtList[i].set_color((rows[d2rowcount][d2idcount]), BLUE)
                dtList[i].set_color((rows[d2rowcount-1][d2idcount-1]), BLUE)
            else:
                dtList[i].set_color((rows[d2rowcount][d2idcount]), BLUE)
            d2rowcount+=1
            d2idcount+=1
        while d2rowcount>5:
            if d2rowcount ==10:
                dtList[i].set_color((rows[d2rowcount][d2idcount]), BLUE)
                dtList[i].set_color((rows[d2rowcount+1][d2idcount+1]), BLUE)
            else:
                dtList[i].set_color((rows[d2rowcount+1][d2idcount+1]), BLUE)
            d2rowcount+=1
            d2idcount-=1
    d3rowcount=1
    for i in range(len(rows)):
        d3idcount=5
        while d3rowcount<=5:
            if d3rowcount==1:
                dtList[i].set_color((rows[d3rowcount][d3idcount]), BLUE)
                dtList[i].set_color((rows[d3rowcount-1][d3idcount-1]), BLUE)
            else:
                dtList[i].set_color((rows[d3rowcount][d3idcount]), BLUE)
            d3rowcount+=1
            d3idcount+=1
        while d3rowcount>5:
            if d3rowcount ==10:
                dtList[i].set_color((rows[d3rowcount][d3idcount]), BLUE)
                dtList[i].set_color((rows[d3rowcount+1][d3idcount+1]), BLUE)
            else:
                dtList[i].set_color((rows[d3rowcount+1][d3idcount+1]), BLUE)
            d3rowcount+=1
            d3idcount-=1
    d4rowcount=1
    for i in range(len(rows)):
        d4idcount=8
        while d4rowcount<=5:
            if d4rowcount==1:
                dtList[i].set_color((rows[d4rowcount][d4idcount]), BLUE)
                dtList[i].set_color((rows[d4rowcount-1][d4idcount-1]), BLUE)
            else:
                dtList[i].set_color((rows[d4rowcount][d4idcount]), BLUE)
            d4rowcount+=1
            d4idcount+=1
        while d4rowcount>5:
            if d4rowcount ==10:
                dtList[i].set_color((rows[d4rowcount][d4idcount]), BLUE)
                dtList[i].set_color((rows[d4rowcount+1][d4idcount+1]), BLUE)
            else:
                dtList[i].set_color((rows[d4rowcount+1][d4idcount+1]), BLUE)
            d4rowcount+=1
            d4idcount-=1
    d5rowcount=1
    for i in range(len(rows)):
        d5idcount=10
        while d5rowcount<=5:
            if d5rowcount==1:
                dtList[i].set_color((rows[d5rowcount][d5idcount]), BLUE)
                dtList[i].set_color((rows[d5rowcount-1][d5idcount-1]), BLUE)
            else:
                dtList[i].set_color((rows[d5rowcount][d5idcount]), BLUE)
            d5rowcount+=1
            d5idcount+=1
        while d5rowcount>5:
            if d5rowcount ==10:
                dtList[i].set_color((rows[d5rowcount][d5idcount]), BLUE)
                dtList[i].set_color((rows[d5rowcount+1][d5idcount+1]), BLUE)
            else:
                dtList[i].set_color((rows[d5rowcount+1][d5idcount+1]), BLUE)
            d5rowcount+=1
            d5idcount-=1
    for i in range(len(dtList)):
        dtList[i].sync() 
    time.sleep(0.4)    





