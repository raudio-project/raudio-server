#!/usr/bin/python3

'''
This code will need to be added to the gst-server file so that the 
api can communicate with the server via the socket. 
'''
import socket

# Default local
HOST='127.0.0.1'
PORT=8080

# AF_INET is for IPv4 and SOCK_STREAM is for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            d = data.decode()
            print(d)
            if d == 'PAUSE':
                print(d)
                break
                # ideally this will go here --> GST.set_state(PAUSED)
            elif d == 'PLAY':
                print(d)
                break
                # ideally this will go here --> GST.set_state(PLAYING)
            # I think if we have data to send back is all
            conn.sendall(data) # not sure what this does but saw in tutorial
