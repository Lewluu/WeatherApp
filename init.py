import yaml

try:
    with open('./python-job1_dev-producer/data_out.yaml') as file:
        data=yaml.safe_load(file)
except:
    with open('data_out.yaml') as file:
        data=yaml.safe_load(file)

curr_temp=float(str(data[1]['temperature']).replace("['","").replace("']",""))

print(curr_temp)