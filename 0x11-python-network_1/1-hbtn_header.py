#!/usr/bin/python3
"""
A script taht takes in a URL, sends a request to the URL 
and displays the value of the X-Request-ID variable
"""
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
