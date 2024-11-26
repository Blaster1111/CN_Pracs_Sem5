import socket
import time

def server():
    s = socket.socket()
    s.bind(('127.0.0.1', 6001))
    s.listen(1)
    con, _ = s.accept()
    bucket_size = 10  
    current_size = bucket_size  
    while True:
        data = con.recv(1024).decode()
        if not data:
            break  
        print(f"\nBucket space available: {current_size}")
        if int(data) <= current_size:
            print(f"accept {data}")
            current_size -= int(data)
        else:
            print(f"drop {data}")
            
        time.sleep(1)  # Leak rate: 2 units per second
        current_size = min(bucket_size, current_size + 2)
    
    con.close()
server()