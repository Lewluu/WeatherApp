import yaml

import os
import time

path='../python-job1_dev-producer/data_out.yaml'

try:
    file=open(path)
    data=yaml.safe_load(file)
except:
    file=open('data_out.yaml')
    data=yaml.safe_load(file)

last_modification=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(path)))

curr_temp=float(str(data[1]['temperature']).replace("['","").replace("']",""))
last_hour_temp=0
threshold_temp=10.0

if abs(curr_temp-last_hour_temp)>threshold_temp:
    print("The temperature has exceeded the threshold... sending notification!")

print(curr_temp)