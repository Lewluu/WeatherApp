# from mail import Mail
from src import Producer, Mail
import os

Producer.init()

os.system("python src/consumer.py " + Producer.getCity())

Mail.init(Producer.getMailInfo()[0], Producer.getMailInfo()[1], Producer.getMailInfo()[2])
# Mail.addContent("First line of content ...")
# Mail.addContent("Second line of content ...")
# Mail.addContent("Third line of content ...")

# if Mail.isNotEmpty():
#     Mail.send()
# else:
#     print("Mail is empty!")

