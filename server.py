#!/usr/bin/env python3

from flask import Flask, redirect, send_from_directory
import socket

app = Flask(__name__)

HOST = '127.0.0.1'
PORT=8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

@app.route("/stream", methods=("GET",))
def playlist():
    return redirect("/stream/playlist.m3u8")


@app.route("/stream/<path:name>", methods=("GET",))
def get_stream_data(name):
    return send_from_directory("stream", name)

@app.route('/stream/play', methods=['PUT'])
def play():
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#        s.connect((HOST, PORT))
    method = 'PLAY'
    s.sendall(str.encode(method))
        #data = s.recv(1024)

#    print(f'Received {data!r}')
    return "200 OK"

@app.route('/stream/pause', methods=['PUT'])
def pause():
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#        s.connect((HOST, PORT))
    method = 'PAUSE'
    s.sendall(str.encode(method))
        #data = s.recv(1024)

#    print(f'Received {data!r}')
    return "200 OK"
  

if __name__ == "__main__":
    # TODO: use a real WSGI server for production
    app.run(host="0.0.0.0", port=5000)
