#!/usr/bin/python3

#######################################################
# Get City name as user input and show weather details
#
# Vignesh Narasimhulu
#######################################################

import requests
import json

import localsecrets

#define the base url and the api-key to access weather data
baseurl = "https://api.openweathermap.org/data/2.5/weather?q="

#get from https://home.openweathermap.org/api_keys
apikey = localsecrets.APIKEY_WEATHER

def getWeather(city: str):
  city=city

  r=requests.get(baseurl + city+"&APPID="+apikey)
  #check RC
  rc=r.status_code

  weatherOutput = {}

  #if success
  if (rc == 200):
    #access the json data
    rj=r.json()
    #print(rj)
    temp=rj['main']['temp']
    ctemp=int(temp)-273.15
    humidity=rj['main']['humidity']
    wdesc=rj['weather'][0]['description']

    weatherOutput["City"] = city
    weatherOutput["Temperature"] = f"{ctemp:.2f} C" #round-off to 2 decimal points
    weatherOutput["Humidity"] = humidity
    weatherOutput["Condition"] = wdesc

  #handle city not found
  #elif (rc == 404):
  #  print ("Sorry. City not found!")
  #else:
  #  print ("Sorry, unable to retrieve the data at the moment!")

  return weatherOutput
