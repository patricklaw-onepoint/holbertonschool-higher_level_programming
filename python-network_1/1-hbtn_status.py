#!/usr/bin/python3
"""Python - Network #1"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    # url = "https://www.google.com.au/"
    request = Request(url)

    with urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
