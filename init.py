from producer import Producer
import os

Producer.init()

os.system("python consumer.py " + Producer.getCity())