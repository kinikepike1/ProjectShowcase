#!/usr/bin/env python
# -*- coding: utf-8 -*-

#CIS245 Class Project
#this application is written by Kinnick Fox

#imports
import requests
import sys

#api information
apiToken = '*******************'
apiUrl = 'http://api.openweathermap.org/data/2.5/weather?'

#temperature converter form openweather's native kelvin to fahrenheit
def tempConvert(temp):
    new_temp = (temp - 273.15) * 1.8 + 32
    return new_temp

#main code block start
while True:
    print('Please enter a zip code or city. Enter "quit" if you would like to quit. ')
#location data input
    location = input()
    if str(location).lower() == 'quit':
        sys.exit()
    else:

#validate data
        if location.isnumeric() and len(location) != 5:
            print("Error: Please enter a five digit zip code")
        else:

#start try block
            try:
                r = requests.get(apiUrl + "appid=" + apiToken + "&q=" + location)
            except requests.exceptions.ConnectionError:
                print('Error: Connection could not be made with weather server. Please check your connection and try again.')
            finally:
                if str(r.status_code) == "404":
                    print('Error: Please enter valid city')
                elif str(r.status_code) == "200":
                    print ("Connection Successful!")
                    name = str(r.json()["name"])
                    minT = str(tempConvert(r.json()["main"]["temp_min"]))
                    maxT = str(tempConvert(r.json()["main"]["temp_max"]))
#parse description data from weather data
                    forecast = str(r.json()["weather"]).split(':')[3].split(',')[0].replace("'","")
#print line construction
                    print("\nWeather Forecast for {}: \nThe daily low is {}\u00b0F while the high is {}\u00b0F.\nLooking like{}.\n".format(name, minT[:4], maxT[:4], forecast))
                else:
                    pass   
                print('Would you like to make another search?')