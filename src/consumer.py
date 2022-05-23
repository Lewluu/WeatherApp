import ast
import sys
from src import Mail, Log

city = sys.argv[1]
mail_sender = sys.argv[2]
mail_password = sys.argv[3]
mail_receiver = sys.argv[4]

path = "../data/weather_info_" + city + ".txt"

Mail.init(mail_sender, mail_password, mail_receiver)

#getting the first and last line from file
try:
    with open(path, 'r') as file:
        data_file = list()
        for line in file: data_file.append(line)
    file.close()
except Exception as e:
    print(e)
    Log.addMesage("consumer", e)
    exit()

last_line = ast.literal_eval(data_file[len(data_file) - 1])
first_line = ast.literal_eval(data_file[0])

#getting info about the last captions and the one hour ago captions
values = [
    'temperature',
    'humidity',
    'temperature-threshold',
    'humidity-threshold'
]

for value in values:
    if value not in (first_line and last_line):
        print(value + " not found ...")
        Log.addMesage("consumer", value + " not found ...")
        exit()

curr_temperature = float(last_line['temperature'])
curr_humidity = float(last_line['humidity'])
one_hour_ago_temperature = float(first_line['temperature'])
one_hour_ago_humidity = float(first_line['humidity'])
threshold_temperature = last_line['temperature-threshold']
threshold_humidity = last_line['humidity-threshold']

#testing if the threshold values from temperature and/or humidity are exceeded
diff_temperature = abs(round(curr_temperature - one_hour_ago_temperature, 2))
diff_humidity = abs(round(curr_humidity - one_hour_ago_humidity, 2))

if diff_temperature >= threshold_temperature:
    Mail.addContent("Values in temperature exceeded by: " + str(diff_temperature))

if diff_humidity >= threshold_humidity:
    Mail.addContent("Values in humidity exceeded by: " + str(diff_humidity))

if Mail.isNotEmpty():
    Mail.send()
else:
    print("Weather is normal!")
    Log.addMesage("consumer", "Weather is normal!")