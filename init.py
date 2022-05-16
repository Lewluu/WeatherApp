from urllib import response
import requests
import os, shutil
from datetime import datetime
try:
    import yaml
except:
    print("Module yaml doesn't exist. Importing ...")
    os.system("pip install pyyaml")
    import yaml

try:
    with open('data_in.yaml','r') as file:
        data = yaml.safe_load(file)
except Exception as e:
    print(e)
    exit()

city_name = data['city'][0]
api_key = data['api-key'][0]
base_url = data['base-url'][0]

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    curr_temp = y["temp"]
    curr_temp = round(curr_temp - 273.15, 3)
    curr_pres = y["pressure"]
    curr_hum = y["humidity"]
    z = x["weather"]
    weather_desc = z[0]["description"]

    out_yaml = [{'city':[city_name]},
            {'temperature':[str(curr_temp)]},
            {'pressure':[str(curr_pres)]},
            {'humidity':[str(curr_hum)]},
            {'description':[str(weather_desc)]}]
    try:
        with open('data_out.yaml','w') as file:
            yaml.dump(out_yaml, file)
            file.close()
            shutil.move('data_out.yaml', '../data/data_out.yaml')
    except Exception as e:
        print(e)
        exit()
    try:
        with open("../data/weather_info_" + city_name + ".txt","a+") as file:
            data_dict = dict()
            data_dict["temperature"] = curr_temp
            data_dict["humidity"] = curr_hum
            data_dict["date"] = datetime.now().strftime("%d/%m/%y")
            data_dict["time"] = datetime.now().strftime("%H:%M:%S")
            file.write(str(data_dict) + "\n")
            file.close()
    except Exception as e:
        print(e)
        exit()
else:
    print("City not found!")
