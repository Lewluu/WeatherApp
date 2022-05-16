import yaml
from datetime import datetime
import ast

threshold_temperature = 10.0
path = '../data/data_out.yaml'

try:
    file = open(path)
    data = yaml.safe_load(file)
except Exception as e:
    print(e)
    exit()

city = str(data[0]['city']).replace("['","").replace("']","")
curr_temp = float(str(data[1]['temperature']).replace("['","").replace("']",""))
new_path = "../data/temperature_"+city+".txt"

try:
    file = open(new_path)
except Exception as e:
    print(e)
    exit()

#getting the time from one hour ago
curr_time = datetime.now().strftime("%H:%M")
one_hour_ago_time = str(int(curr_time[0:2]) - 1) + curr_time[2:6]

#getting the temperature from exactly one hour ago
for line in file:
    #converting string to dict and remove the seconds
    line = ast.literal_eval(line)
    file_data_time = str(line['time'])[:-3]
    if file_data_time == one_hour_ago_time:
        print("Found temperature from one hour ago!")
        file_data_temp = float(line['temperature'])
        diff_temp = abs(round(curr_temp - file_data_temp, 2))
        print("Difference in temperature from one hour ago is: " + str(diff_temp))
        if diff_temp > threshold_temperature:
            print("Threshold temperature exceeded ... sending mail notification ...")
        break
        
        
        