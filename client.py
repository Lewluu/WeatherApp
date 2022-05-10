import json
import socket
import init_producer as producer
import init_consumer as consumer

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    producer.initWeatherData()
    data=consumer.getWeatherInfo()
    for info in data:
        info=json.dumps(info)
        s.sendall(info.encode("utf-8"))
        data = s.recv(1024)
        print(f"Received {data}")