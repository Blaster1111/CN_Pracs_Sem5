import socket
import time

def server():
    s = socket.socket()
    s.bind(('127.0.0.1', 6001))
    s.listen(1)
    con, _ = s.accept()
    size = 10  
    while True:
        data = con.recv(1024).decode()
        if not data:
            break
        if int(data) <= size:
            print(f"accept {data}")
            size -= int(data)
        else:
            print(f"drop {data}")
        time.sleep(1)
        size = min(10, size + 2)
    con.close()

server()
