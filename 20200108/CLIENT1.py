import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 720))
while True:
    msg=s.recv(7)
    print(msg.decode("utf-8"))
