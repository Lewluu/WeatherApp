from datetime import datetime

class Log:
    def addMesage(source, message):
        try:
            with open("../data/weather_log.txt", "a+") as file:
                file.write(datetime.now().strftime("%d/%m/%y | %H:%M:%S"))
                file.write("\n \n --- MESSAGE FROM " + source + " --- BEGIN --- \n \n")
                file.write(message)
                file.write("\n \n --- MESSAGE FROM " + source + " --- ENDS --- \n \n")
                
                file.close()
        except Exception as e:
            print(e)
            exit()