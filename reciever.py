import socket
s= socket.socket()
s.bind(("localhost",9910))
s.listen(1)
print("Waiting to Connect...")
conn, addr = s.accept()
print("Connected")
with open("recieved_file.txt","wb") as f:
    while True:
        data = conn.recv(1599)
        if not data:
            break
        f.write(data)
print("File recieved successfully!")
