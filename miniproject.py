# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json
import csv
from datetime import datetime

# Enter your API key here
api_key = "87d845b0b6cf29baa1a73cc34b067a95"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

	# store the value of "main"
	# key in variable y
	y = x["main"]

	# store the value corresponding
	# to the "temp" key of y
	current_temperature = y["temp"]

	# store the value corresponding
	# to the "pressure" key of y
	current_pressure = y["pressure"]

	# store the value corresponding
	# to the "humidity" key of y
	current_humidity = y["humidity"]

	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

	# print following values
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description))

else:
	print(" City Not Found ")
	
today = datetime.now()
	
header = ['Temperature','Atmospheric pressure', 'Humidity', 'Description','Date and Time']
data = [str(current_temperature), str(current_pressure), str(current_humidity), str(weather_description),today]
with open ('test.txt', 'w', encoding = 'UTF8', newline = '') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	writer.writerow(data)

