import yaml

try:
    with open('./python-job1_dev-producer/data_out.yaml') as file:
        data=yaml.safe_load(file)
except:
    with open('data_out.yaml') as file:
        data=yaml.safe_load(file)

curr_temp=float(str(data[1]['temperature']).replace("['","").replace("']",""))
last_hour_temp=0
threshold_temp=10.0

if abs(curr_temp-last_hour_temp)>threshold_temp:
    print("The temperature has exceeded the threshold... sending notification!")

print(curr_temp)