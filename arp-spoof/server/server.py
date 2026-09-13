import socket 

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("10.10.0.30", 1234))

conn.listen(1)
while True:
    client_conn, addr = conn.accept()
    print(f"[Server] Connection from {addr}")

    while True:
        data = client_conn.recv(1024)
        if not data:
            break
        print(f"[Server] Received: {data.decode()}")
    
    client_conn.close()
    print(f"[Server] Connection from {addr} closed")