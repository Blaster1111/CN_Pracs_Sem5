import socket
import random
import time

def client():
    s = socket.socket()
    s.connect(('127.0.0.1', 6001))

    for _ in range(20):
        data = random.randint(1, 5)  
        s.send(str(data).encode())
        print(f"send {data}")
        time.sleep(random.random()*2)  

    s.close()

client()
