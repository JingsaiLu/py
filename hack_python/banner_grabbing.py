import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("10.192.225.198",80))
ans = s.recv(1024)
print ans