# Echo client program
import threading
import socket
import threading

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

def send(s):
    while True:
        s.sendall(t)

        if t == 'Bye':
            break

def recieve(s):
    while  True:
        data = s.recv(1024)
        print(data)

        if data == 'Bye':
            sendall(data)
            break


t1 = threading.Thread(target=send, args=(s,))
t1.daemon = True
t1.start()

t2 = threading.Thread(target=recieve, args=(s,))
t2.start()

t2.join()

s.close()
