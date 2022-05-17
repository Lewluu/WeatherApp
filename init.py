import requests
from datetime import datetime
import yaml

try:
    with open('data_in.yaml','r') as file:
        data = yaml.safe_load(file)
except Exception as e:
    print(e)
    exit()

if 'city' and 'api-key' and 'base-url' and 'temperature-threshold' and 'humidity-threshold' in data:
    city_name = data['city'][0]
    api_key = data['api-key'][0]
    base_url = data['base-url'][0]
    threshold_temperature = data['temperature-threshold'][0]
    threshold_humidity = data['humidity-threshold'][0]
else:
    print("Values not found in dictionary ...")
    exit()

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
x = requests.get(complete_url).json()

if x["cod"] != "404":
    y = x["main"]
    curr_temp = round(y["temp"] - 273.15, 3)
    curr_hum = y["humidity"]
    z = x["weather"]
    weather_desc = z[0]["description"]

    try:
        with open("../data/weather_info_" + city_name + ".txt","a+") as file:
            data_dict = dict()
            data_dict["temperature"] = curr_temp
            data_dict["humidity"] = curr_hum
            data_dict["date"] = datetime.now().strftime("%d/%m/%y")
            data_dict["time"] = datetime.now().strftime("%H:%M:%S")
            data_dict["temperature-threshold"] = threshold_temperature
            data_dict["humidity-threshold"] = threshold_humidity
            file.write(str(data_dict) + "\n")
            file.close()
    except Exception as e:
        print(e)
        exit()
else:
    print("City not found!")
