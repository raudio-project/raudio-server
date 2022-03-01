#!/usr/bin/env python3

from flask import Flask, redirect, send_from_directory

app = Flask(__name__)


@app.route("/stream", methods=("GET",))
def playlist():
    return redirect("/stream/playlist.m3u8")


@app.route("/stream/<path:name>", methods=("GET",))
def get_stream_data(name):
    return send_from_directory("stream", name)


if __name__ == "__main__":
    # TODO: use a real WSGI server for production
    app.run(host="0.0.0.0", port=5000)
