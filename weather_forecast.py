# API KEY => 52d80887c3c7d34b155074ebf15656c6
import requests,json
api_key = "52d80887c3c7d34b155074ebf15656c6"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city = input("Enter your city = ")
complete_url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(complete_url)
x = response.json()
if(x["cod"] != "404"):
    y = x["main"]
    cur_temp = y["temp"]
    #Convert temperature into kelvin
    temp_in_celsius = "{:.2f}".format(cur_temp - 273.15)
    cur_pressure = y["pressure"]
    cur_humidity = y["humidity"]
    z = x["weather"]
    wind = x["wind"]
    wind_speed = wind["speed"]
    weather_description = z[0]["description"]
    print("current temperature = " + str(temp_in_celsius) + "\n" +
        "Current_pressure(in hpa) = " + str(cur_pressure) + "\n" + 
        "current humidity = " + str(cur_humidity) + "\n" + 
        "weather description = " + str(weather_description) + "\n" + 
        "Wind speed(in m/s) = " + str(wind_speed)) 
else:
    print("City not found")
   