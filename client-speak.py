# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = raw_input()
    s.sendto(data, (HOST, PORT))
    if data == 'bye': break
data = s.recv(1024)
s.close()
print 'Received', repr(data)
