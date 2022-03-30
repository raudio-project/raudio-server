#!/usr/bin/env python3

import socket
import sys
import signal
import ffmpeg

IPC_HOST = "127.0.0.1"
IPC_PORT = 5001
STREAM_DIR = "stream"


# TODO: we need to handle incoming commands, not just echo them back
def process_commands(mus, path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IPC_HOST, IPC_PORT))
        s.listen(10)
        conn, addr = s.accept()
        with conn:
            print(f"connection established ({addr})")
            while True:
                data = conn.recv(1024)
                if not data:
                    d = ""
                    continue
                d = data.decode()
                if d == "PAUSE":
                    print("pause")
                    mus.send_signal(signal.SIGSTOP)
                elif d == "PLAY":
                    print("play")
                    mus.send_signal(signal.SIGCONT)
                    # stream_file(path)
                print("here")

                # conn.sendall(data)


def stream_file(path):
    # for now we put the file on "repeat", just for proof-of-concept
    process = (
        ffmpeg.input(path, re="-re", stream_loop="-1")
        .output(
            f"{STREAM_DIR}/out",
            codec="copy",
            f="hls",
            hls_segment_type="mpegts",
            hls_segment_filename=f"{STREAM_DIR}/segment-%02d.ts",
            hls_flags="delete_segments",
            master_pl_name="playlist.m3u8",
        )
        .run_async()
    )
    print(process)
    return process


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: hls.py <file.mp3>")
        sys.exit(1)

    # TODO: make this function non-blocking... ffmpeg's run_async will be
    # a start, but it's still not quite what we want
    mus = stream_file(sys.argv[1])

    # this does nothing for now :(
    process_commands(mus, sys.argv[1])
