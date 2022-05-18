from producer import Producer
import os

Producer.init()

os.system("py consumer.py " + Producer.getCity())