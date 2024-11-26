import socket
import time

def server():
    s = socket.socket()
    s.bind(('127.0.0.1', 6001))
    s.listen(1)
    con, _ = s.accept()
    tokens = 0  
    
    size = 10 

    while True:
        data = con.recv(1024).decode()
        if not data:
            break

        tokens = min(size, tokens + 2)
        print(f"\nTokens available: {tokens}")
             
        if int(data) <= tokens:
            print(f"accept {data}")
            tokens -= int(data)
        else:
            print(f"insufficient tokens")
        
    con.close()

server()