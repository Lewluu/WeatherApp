from datetime import datetime
import ast

city = 'Botosani'

path = "../data/weather_info_" + city + ".txt"

try:
    file = open(path,'r')
except Exception as e:
    print(e)
    exit()

#getting the current temperature, humidity from the last line of the output file
print(len(file.readline()))
for line in file: pass
line = ast.literal_eval(line)
curr_temperature = float(line['temperature'])
curr_humidity = float(line['humidity'])

#getting the time from one hour ago
curr_time = datetime.now().strftime("%H:%M")
one_hour_ago_time = str(int(curr_time[0:2]) - 1) + curr_time[2:6]

#getting the temperature from exactly one hour ago
for line in file:
    #converting string to dict and remove the seconds
    line = ast.literal_eval(line)
    file_data_time = str(line['time'])[:-3]
    if file_data_time == one_hour_ago_time:
        print("Found data from one hour ago!")

        file_data_temperature = float(line['temperature'])
        file_data_humidity = float(line['humidity'])
        diff_temperature = abs(round(curr_temperature - file_data_temperature, 2))
        diff_humidity = abs(round(curr_humidity - file_data_humidity, 2))

        print("Difference in temperature from one hour ago is: " + str(diff_temperature))
        if diff_temperature > threshold_temperature:
            print("Threshold temperature exceeded ... sending mail notification ...")

        print("Difference in humidity from one hour ago is: " + str(diff_humidity))
        if diff_humidity > threshold_humidity:
            print("Threshold temperature exceeded ... sending mail notification ...")

        break
        
        
        