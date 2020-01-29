# Echo server program
import threading
import socket
import time
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

def recieve(conn):
    while True:
        data = conn.recv(1024)
        print data
        if data == "Bye":
            break

def send(conn):
    while True:
        conn.sendall(t)

        if t == "Bye":
            conn.sendall(t)
            break

t1 = threading.Thread(target=send, args=(conn,))
t1.daemon = True
t1.start()

t2 = threading.Thread(target=recieve, args=(conn,))
t2.start()

t2.join()

s.close()
