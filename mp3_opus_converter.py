#!/usr/bin/python3

from pydub import AudioSegment
import sys

if len(sys.argv) < 2:
    print('Expected *.mp3 as input...')
    print('Usage:   ./mp3_opus_converter <mp3_1> <mp3_2> <mp3_3>')
    exit(1)

for audio in sys.argv[1:]:
    title = audio[0:-4] + '.opus'
    print(f'Converting to {title}...')
    AudioSegment.from_mp3(audio).export(title, format='opus')
