from cmath import e
from urllib import response
import requests
import os
try:
    import yaml
except:
    print("Module yaml doesn't exist. Importing ...")
    os.system("pip install pyyaml")

api_key="90b3486670d48a81220917bdefd43c68"
base_url="http://api.openweathermap.org/data/2.5/weather?"

# city_name=input("Enter city name: ")

with open('data_in.yaml','r') as file:
    data=yaml.safe_load(file);

city_name=data['city'][0]

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

    out_yaml=[{'city':[city_name]},
            {'temperature':[str(round(curr_temp-273.15,3))]},
            {'pressure':[str(curr_pres)]},
            {'humidity':[str(curr_hum)]},
            {'description':[str(weather_desc)]}]
    with open('data_out.yaml','w') as file:
        yaml.dump(out_yaml,file)

    try:
        with open("../data/temperature_"+city_name+".txt","a+") as file:
            file.write(str(round(curr_temp-273.15,3))+"\n")
            file.close()
    except:
        print("Error opening the file temperature_"+city_name)
else:
    print("City not found!")
