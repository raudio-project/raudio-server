<h1 align="center"><img src="https://raudio-project.github.io/assets/raudio_logo.png" alt="logo" width="35%"></h1>
<h5 align="center"><i align="center">The open platform for hosting and streaming music.</i></h5>

<p align="center">
  <img src="https://img.shields.io/badge/release-coming%20soon-blue">
  <img src="https://img.shields.io/github/license/raudio-project/raudio-server?color=red">
  <img src="https://img.shields.io/github/issues/raudio-project/raudio-server?color=green">
</p>

## Installation

For this server to work, you must make sure [FFMPEG](https://ffmpeg.org/)
is installed to your machine.

Install the package, optionally in a virtual environment:

`pip install raudio-server`

Run the HLS streaming backend:

`python3 -m raudio_server.hls /path/to/file.mp3`

Run the HTTP server in a separate terminal:

`python3 -m raudio_server.server`

## Setting a up a development environment
```sh
$ git clone git@github.com:raudio-project/raudio-server.git
$ cd raudio-server
$ python3 -m venv venv      # Create a Python virtual environment
$ source venv/bin/activate  # Activate the enviornment
$ pip3 install .            # Install the package
```

<p align="center">
<img src="https://yld.moe/raw/lOk.png" width="40%">
</p>
