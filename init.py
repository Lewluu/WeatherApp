from urllib import response
import requests
import yaml

api_key="90b3486670d48a81220917bdefd43c68"
base_url="http://api.openweathermap.org/data/2.5/weather?"

# city_name=input("Enter city name: ")

with open('data_info.yaml','r') as file:
    data=yaml.safe_load(file);

city_name=data['weather-app']['city']

complete_url=base_url+"appid="+api_key+"&q="+city_name

response=requests.get(complete_url)

x=response.json()

if x["cod"] != "404":
    y=x["main"]
    curr_temp=y["temp"]
    curr_pres=y["pressure"]
    curr_hum=y["humidity"]
    z=x["weather"]
    weather_desc=z[0]["description"]

    print("Showing weather data for "+city_name+":")
    print("Temperature (in kelvin) = "+str(curr_temp))
    print("Pressure (in hpa) = "+str(curr_pres))
    print("Humidity (in percentage) = "+str(curr_hum))
    print("Description = "+str(weather_desc))
else:
    print("City not found!")
