from asyncio.windows_events import NULL
import errno
import os
import threading

def start_server(name):
    print("Starting server ....")
    os.system("python server.py")

def start_client(name):
    print("Starting client ....")
    os.system("python client.py")

t1=threading.Thread(target=start_server,args={"My Server"})
t2=threading.Thread(target=start_client,args={"My Client"})

t1.start()
t2.start()

t1.join()
t2.join()

print("End of program...")
