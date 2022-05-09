from urllib import response
import requests
import os
try:
    import yaml
except:
    print("Module yaml doesn't exist. Importing ...")
    os.system("pip install pyyaml")
    import yaml

def initWeatherData():
    api_key="90b3486670d48a81220917bdefd43c68"
    base_url="http://api.openweathermap.org/data/2.5/weather?"

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
            {'temperature':[str(curr_temp)]},
            {'pressure':[str(curr_pres)]},
            {'humidity':[str(curr_hum)]},
            {'description':[str(weather_desc)]}]
        with open('data_out.yaml','w') as file:
            yaml.dump(out_yaml,file)
    else:
        print("City not found!")