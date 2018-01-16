import socket
from _socket import *
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return
def checkVulns(banner):
    if ('FreeFloatFtp Server' in banner):
        print("Vulnerable")
    elif ('Daemon server' in banner):
        print("Not vulnerable")
    return
def main():
    ip1 = '192.168.35.12'
    ip2 = '192.168.35.11'
    port = 21
    banner1 = retBanner(ip1,port)
    if banner1:
        print(ip1+ ':'+ banner1.strip('\n'))
        checkVulns(banner1)
if __name__ == '__main__':
    main()