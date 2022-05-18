import ast
import sys

city = sys.argv[1]
path = "../data/weather_info_" + city + ".txt"

#getting the first and last line from file
data_file = list()
try:
    with open(path, 'r') as file:
        for line in file: data_file.append(line)
    file.close()
except Exception as e:
    print(e)
    exit()

last_line = ast.literal_eval(data_file[len(data_file) - 1])
first_line = ast.literal_eval(data_file[0])

#getting info about the last captions and the one hour ago captions
if 'temperature' and 'humidity' and 'temperature-threshold' and 'humidity-threshold' in (first_line and last_line):
    curr_temperature = float(last_line['temperature'])
    curr_humidity = float(last_line['humidity'])
    one_hour_ago_temperature = float(first_line['temperature'])
    one_hour_ago_humidity = float(first_line['humidity'])
    threshold_temperature = last_line['temperature-threshold']
    threshold_humidity = last_line['humidity-threshold']
else:
    print("Values not found in " + path)
    exit()

#testing if the threshold values from temperature and/or humidity are exceeded
diff_temperature = abs(round(curr_temperature - one_hour_ago_temperature, 2))
diff_humidity = abs(round(curr_humidity - one_hour_ago_humidity, 2))

if diff_temperature >= threshold_temperature:
    print("Values of threshold temperature exceeded ... sending mail notification ...")

if diff_humidity >= threshold_humidity:
    print("Values of threshold humidity exceeded ... sending mail notification ...")
        