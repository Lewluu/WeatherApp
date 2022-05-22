from datetime import datetime

class Log:
    def init():
        global file
        try:
            # with open("../data/weather_log", "w+") as file:
            #     pass
            file = open("../data/weather_log.txt", "a+")
        except Exception as e:
            print(e)
            exit()
    def addMesage(source, message):
        file.write(datetime.now().strftime("%d/%m/%y | %H:%M:%S"))
        file.write("\n \n --- MESSAGE FROM " + source + " --- BEGIN --- \n \n")
        file.write(message)
        file.write("\n \n --- MESSAGE FROM " + source + " --- ENDS --- \n \n")
    def close():
        file.close()
