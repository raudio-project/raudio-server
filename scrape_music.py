#!/usr/bin/python3

import os
import requests
import re
from bs4 import BeautifulSoup

# Constants 
pattern = re.compile('/bensound-music/.*mp3')
URL = 'https://www.bensound.com'
PAGE = '/royalty-free-music/'

# Download the file and write to filesystem 
def wget(url):
    print(f'Downloading {url}...')

    response = requests.get(url)
    path = os.path.basename(url)
    with open(path, 'wb') as fs:
        fs.write(response.content)
    return path

def main():

    headers = {'User-Agent': __name__}
    
    ''' Range can go until 38 (max number of pages 
        Make request
        Parse for audio to get download link
        Match link with regex global
        wget each link
    '''
    for i in range(1,2):
        if i == 1:
            url = URL + PAGE
        else:
            url = URL + PAGE + str(i)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        audio_tag = soup.findAll('audio')
        audio_tag = list(map(str, audio_tag))
        p = list(map(pattern.findall, audio_tag))

        for link in p:
            url = URL + link[0]
            wget(url)


if __name__ == '__main__':
    main()
