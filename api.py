#!/usr/bin/python3

import socket
import sys
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Default local, change to momo?
HOST='127.0.0.1'
PORT=8080

class AudioFiles(Resource):

    # GET request consists of a command such as !info to
    # get the metadata about the current song
    # We could store the metadata for each song as a variable
    # in this file and then just return it for the request
    def get_song_info():
        return None

    # PUT request consists of changing the resource 
    # This would likely be an authenticated request so as 
    # to handle !play !pause !skip
    # Perhaps one function for !play !pause to flip a 
    # switch like a binary, and one function for !skip
    @app.route('/play', methods=['PUT'])
    def play():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            method = 'PLAY'
            s.sendall(str.encode(method))
            data = s.recv(1024)

        print(f'Received {data!r}')
        return "200 OK"

    @app.route('/pause', methods=['PUT'])
    def pause():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            method = 'PAUSE'
            s.sendall(str.encode(method))
            data = s.recv(1024)

        print(f'Received {data!r}')
        return "200 OK"

    def skip():
        return None

    # I do not see a need for POST or DELETE methods
    # at this time 


if __name__ == '__main__':
    app.run(debug=True)
