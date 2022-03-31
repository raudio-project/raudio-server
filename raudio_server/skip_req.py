#!/usr/bin/python3

# Basic file to send a put request to our API on localhost

import requests

r = requests.put("http://0.0.0.0:5000/stream/skip")
print(r)
