#!/usr/bin/env python3

import atexit
import logging
import socket
import sys

import gi

gi.require_version("GLib", "2.0")
gi.require_version("GObject", "2.0")
gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib  # noqa: E402


class Server:
    def __init__(self, filepath, host, port):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

        self.filepath = filepath
        self.host = host
        self.port = port

        Gst.init(sys.argv[1:])
        self.pipeline = Gst.Pipeline.new("pipeline")

        self.source = None
        self.demuxer = None
        self.stuffer = None
        self.sink = None

    def build_pipeline(self):
        self.source = Gst.ElementFactory.make("filesrc", "source")
        self.source.set_property("location", self.filepath)
        if not self.pipeline.add(self.source):
            self.logger.error("failed to add source to pipeline")
            sys.exit(1)

        self.demuxer = Gst.ElementFactory.make("oggdemux", "demuxer")
        self.demuxer.connect("pad-added", self.demuxer_pad_added)
        if not self.pipeline.add(self.demuxer):
            self.logger.error("failed to add demuxer to pipeline")
            sys.exit(1)

        self.stuffer = Gst.ElementFactory.make("rtpopuspay", "stuffer")
        if not self.pipeline.add(self.stuffer):
            self.logger.error("failed to add stuffer to pipeline")
            sys.exit(1)

        self.sink = Gst.ElementFactory.make("udpsink", "sink")
        self.sink.set_property("host", socket.gethostbyname(self.host))
        self.sink.set_property("port", int(self.port))
        if not self.pipeline.add(self.sink):
            self.logger.error("failed to add sink to pipeline")
            sys.exit(1)

        if not self.source.link(self.demuxer):
            self.logger.error("failed to link source -> demuxer")
            sys.exit(1)

        if not self.stuffer.link(self.sink):
            self.logger.error("failed to link stuffer -> sink")
            sys.exit(1)

        if not all(
            (self.pipeline, self.source, self.demuxer, self.stuffer, self.sink)
        ):
            self.logger.error("not all elements could be created")
            sys.exit(1)

    def demuxer_pad_added(self, demuxer, pad):
        if not demuxer.link(self.stuffer):
            self.logger.error("failed to link demuxer -> stuffer")

    def broadcast(self):
        ret = self.pipeline.set_state(Gst.State.PLAYING)
        if ret == Gst.StateChangeReturn.FAILURE:
            self.logger.error("unable to set pipeline to playing state")
            sys.exit(1)

        """
        # wait until EOS or error
        bus = self.pipeline.get_bus()
        msg = bus.timed_pop_filtered(
            Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS
        )

        # parse msg
        if msg:
            if msg.type == Gst.MessageType.ERROR:
                err, debug_info = msg.parse_error()
                self.logger.error(
                    f"from element {msg.src.get_name()}: {err.message}"
                )
                self.logger.debug(f"{debug_info if debug_info else 'none'}")
            elif msg.type == Gst.MessageType.EOS:
                self.logger.info("end-of-stream reached")
            else:
                self.logger.error("unexpected message received")
        """

    def cleanup(self):
        self.pipeline.set_state(Gst.State.NULL)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <filepath> <host> <port>")
        sys.exit(1)

    server = Server(*sys.argv[1:])
    atexit.register(Server.cleanup, server)

    server.build_pipeline()
    server.broadcast()

    loop = GLib.MainLoop()
    loop.run()

    server.cleanup()
