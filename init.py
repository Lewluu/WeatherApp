import yaml

import os
from datetime import datetime
import ast

threshold_temp=10.0
path='../data/data_out.yaml'

try:
    file=open(path)
    data=yaml.safe_load(file)
except Exception as e:
    print("Error: "+str(e))

city=str(data[0]['city']).replace("['","").replace("']","")
new_path="../data/temperature_"+city+".txt"

try:
    file=open(new_path)
except Exception as e:
    print("Error: "+str(e))

#getting the time from one hour ago
curr_time=datetime.now().strftime("%H:%M")
one_hour_ago_time=str(int(curr_time[0:2])-1)+curr_time[2:6]

for line in file:
    #converting string to dict and remove the seconds
    data_time=str(ast.literal_eval(line)['time'])[:-3]
    if data_time==one_hour_ago_time:
        print("Found temperature from one hour ago!")
        pass