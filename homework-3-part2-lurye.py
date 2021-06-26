#Sharon Lurye
#6/17/21
#Homework 3, Part 2

import requests

key = "7c5bbdc48b25448b9bb141540211706"

#What is the URL to the documentation?

#https://www.weatherapi.com/docs/

# Make a request for the current weather where you are born, or somewhere you've lived.

ridgewood_weather = requests.get("http://api.weatherapi.com/v1/current.json?key=7c5bbdc48b25448b9bb141540211706&q=07451&aqi=no").json()

print(ridgewood_weather)

# Print out the country this location is in.

print(ridgewood_weather['location']['country'])

# Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.

temp_diff = ridgewood_weather['current']['temp_f']-ridgewood_weather['current']['feelslike_f']

print("It feels", temp_diff, "degrees colder.")

# What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.

heathrow = requests.get("http://api.weatherapi.com/v1/current.json?key=7c5bbdc48b25448b9bb141540211706&q=LHR&aqi=no").json()

print("The current temperature at Heathrow airport is", heathrow['current']['temp_c'], "degrees Celsius.")


# What URL would I use to request a 3-day forecast at Heathrow?

#http://api.weatherapi.com/v1/forecast.json?key=7c5bbdc48b25448b9bb141540211706&q=LHR&days=3&aqi=no&alerts=no

# Print the date of each of the 3 days you're getting a forecast for.

heathrow_forecast = requests.get("http://api.weatherapi.com/v1/forecast.json?key=7c5bbdc48b25448b9bb141540211706&q=LHR&days=3&aqi=no&alerts=no").json()

#print(heathrow_forecast['forecast']['forecastday'][0]['date'])
#print(heathrow_forecast['forecast']['forecastday'][2]['date'])

count = 1 
for day in heathrow_forecast['forecast']['forecastday']:
    print("Day", count,":", day['date'])
    count = count + 1

# Print the maximum temperature of each of the days.

print("-----")

count = 1 
for day in heathrow_forecast['forecast']['forecastday']:
    print("Day", count,":", day['date'])
    print("Maximum temperature (Celsius):", day['day']['maxtemp_c'])
    count = count + 1

# Print the day with the highest maximum temperature.

heathrow_forecast = heathrow_forecast['forecast']['forecastday']

hottest_day = heathrow_forecast[0]['date']
hottest_temp = heathrow_forecast[0]['day']['maxtemp_c']

for day in heathrow_forecast:
    if day['day']['maxtemp_c'] > hottest_temp:
        hottest_day = day['date']
        hottest_temp = day['day']['maxtemp_c']

print("The hottest day was", hottest_day, "which was", hottest_temp, "degrees Celsius.")