#!/usr/bin/python3

# Basic file to send a put request to our API on localhost

import requests

r = requests.put('http://127.0.0.1:5000/play')
print(r)
