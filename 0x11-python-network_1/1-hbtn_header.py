#!/usr/bin/python3
"""Takes a URL and send a request to it and displays a value found in h response 

Usage: ./1-hbtn_header.py <URL>
"""

import urllib.request, sys

if __name__ == " __main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
