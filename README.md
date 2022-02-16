# Raudio Server

Once running the "bare mimimum server" presently implemented, the following
shell command should suffice to listen to the broadcast:

```
gst-launch-1.0 \
    udpsrc port=$PORT caps="application/x-rtp,media=(string)audio,encoding-name=(string)OPUS" ! \
    rtpopusdepay ! \
    opusdec ! \
    autoaudiosink
```
