import yaml

try:
    with open('./python-job1_dev-producer/data_out.yaml') as file:
        data=yaml.safe_load(file)
except:
    with open('data_out.yaml') as file:
        data=yaml.safe_load(file)

print(data)