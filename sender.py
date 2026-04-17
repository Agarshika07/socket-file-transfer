import socket
s = socket.socket()
s.connect(("localhost",9910))
filename = "test.txt"

with open(filename, "rb") as f:
    while True:
        data = f.read(1599)
        if not data:
            break
        s.send(data)
print("File Sent")