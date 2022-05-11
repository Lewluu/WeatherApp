import yaml

import os
import time
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

for line in file:
    #converting string to dict and remove the seconds
    line=str(ast.literal_eval(line)['time'])[:-3]
    print(line)


# if abs(curr_temp-last_hour_temp)>threshold_temp:
#     print("The temperature has exceeded the threshold... sending notification!")

# print(curr_temp)