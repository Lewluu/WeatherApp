from copyreg import pickle
import json
import yaml

def getWeatherInfo():
    try:
        with open('./python-job1_dev-producer/data_out.yaml') as file:
            data=yaml.safe_load(file)
    except:
        with open('data_out.yaml') as file:
            data=yaml.safe_load(file)
    return data