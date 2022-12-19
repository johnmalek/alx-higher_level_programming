#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a 
request to the URL and displays the value of the variable 
X-Request-Id in the response header
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))
