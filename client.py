import socket
import init_producer as producer
import init_consumer as consumer
import pickle

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b"Hello, world")

    producer.initWeatherData()
    data=pickle.dumps(consumer.getWeatherInfo())
    s.sendall(data)

    data = s.recv(1024)
    print(f"Received {data!r}")