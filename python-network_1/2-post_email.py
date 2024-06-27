#!/usr/bin/python3
"""Python - Network #1"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    # url = "http://0.0.0.0:5000/post_email"
    # value = {"email": "hr@holbertonschool.com"}
    data = urlencode(value).encode("utf-8")
    request = Request(url, data)

    with urlopen(request) as response:
        print(response.read().decode("utf-8"))
