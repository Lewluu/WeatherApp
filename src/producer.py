import requests
from datetime import datetime
import ast
import yaml

class Producer:
    def init():
        global city_name, mail_info
        mail_info = []

        try:
            with open('../data/data_in.yaml','r') as file:
                data = yaml.safe_load(file)
                file.close()
        except Exception as e:
            print(e)
            exit()

        values = [
                'city',
                'api-key', 
                'base-url', 
                'temperature-threshold', 
                'humidity-threshold', 
                'mail-sender', 
                'mail-password', 
                'mail-receiver']
        
        for value in values:
            if value not in value:
                print(value + "not found ...")
                exit()
            
        city_name = data['city'][0]
        api_key = data['api-key'][0]
        base_url = data['base-url'][0]
        threshold_temperature = data['temperature-threshold'][0]
        threshold_humidity = data['humidity-threshold'][0]
        mail_info.append(data['mail-sender'][0])
        mail_info.append(data['mail-password'][0])
        mail_info.append(data['mail-receiver'][0])

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        x = requests.get(complete_url).json()

        if x["cod"] != "404":
            y = x["main"]
            curr_temp = round(y["temp"] - 273.15, 3)
            curr_hum = y["humidity"]

            try:
                #removing captions from more than one hour ago
                with open("../data/weather_info_" + city_name + ".txt", "r+") as file:
                    lines = list()
                    curr_day = datetime.now().strftime("%d")
                    curr_time_h = int(datetime.now().strftime("%H"))
                    curr_time_m = int(datetime.now().strftime("%M"))
                    for line in file:
                        line = ast.literal_eval(line)
                        line_day = line['date'][0:2]
                        line_time_h = int(line['time'][:-6])
                        line_time_m = int((line['time'][-5:-3]))
                        if (curr_day in line_day) and ((abs(curr_time_h - line_time_h) == 0) or (abs(curr_time_h - line_time_h) == 1 and line_time_m >= curr_time_m)):
                            lines.append(line)
                    file.close()
        
                with open("../data/weather_info_" + city_name + ".txt","w") as file:
                    for line in lines:
                        file.write(str(line) + "\n")

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
                print(str(e))
                file = open("../data/weather_info_" + city_name + ".txt","w")
                file.close()
                exit()
        else:
            print("City not found!")

    def getCity():
        return city_name
    
    def getMailInfo():
        return mail_info

        