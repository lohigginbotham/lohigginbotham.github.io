import requests
import json
apiKey = "dfdf4b3490fe08fdfa09bdda25abe497"
url = "http://api.openweathermap.org/data/2.5/weather?"
cityName = input("Enter city name: ")

completeUrl = url + "q=" + cityName + "&appid=" + apiKey + "&units=imperial"

response = requests.get(completeUrl)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    currentTemp = y["temp"]
    currentHumidity = y["humidity"]
    z = x["weather"]
    weather = z[0]["description"]

else:
    print("City not found")

print("<!DOCTYPE html>"
      "<html>"
      "<head>"
      "<title>weather</title>"
      "</head>"
      "<body>"
      "<h1>Weather for " + cityName + "</h1>"
      "<p>temp: " + str(currentTemp) + "</p>"
      "<p>humidity: " + str(currentHumidity) + "</p>"
      "<p>weather: " + weather + "</p>"                                         
      "</body>"
      "</html>")
