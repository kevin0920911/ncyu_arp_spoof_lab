import socket 

while True:
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(("10.10.0.30", 1234))
    except Exception as e:
        print(f"[Victim] Error connecting to server: {e}")
        continue

    data = b'FLAG{arpspoof_test}'
    conn.send(data)

