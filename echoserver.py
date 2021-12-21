#!/usr/bin/env python3

# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8000              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #de
    s.bind((HOST, PORT)) # wird hinzugefügt wie fopen
    s.listen(1)
    while True: # client loop
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                #count = count + 1
                #print (count)
                data = conn.recv(16) # recieved from client
                if not data: break
                outdata = data[::-1] # reverse data: hello -> olleh
                print(outdata)
                conn.sendall(outdata)
