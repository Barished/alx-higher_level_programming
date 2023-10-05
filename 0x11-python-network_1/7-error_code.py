#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    b = requests.get(url)
    if b.status_code >= 400:
        print("Error code: {}".format(b.status_code))
    else:
        print(b.text)
