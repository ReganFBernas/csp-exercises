import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 720))
s.listen(5)
while True:
    clt, adr=s.accept()
    print(f"Connection to {adr} established")
    clt.send(bytes("Socket Programming in Python", "utf-8"))