import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.99.1", 21))
ans = s.recv(1024)
if ("Free FloatFtp Server" in ans):
    print "Vunerable"
elif ("Daemon server" in ans):
    print"not vulnerable"


