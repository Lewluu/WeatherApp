from src import Producer
import os

from src.mail import Mail

Producer.init()

Mail.init(Producer.getMailInfo()[0], Producer.getMailInfo()[1], Producer.getMailInfo()[2])
Mail.addContent("random content")
Mail.send()

os.system("python src/consumer.py "
 + Producer.getCity() + " "
 + Producer.getMailInfo()[0] + " "
 + Producer.getMailInfo()[1] + " "
 + Producer.getMailInfo()[2]
 )