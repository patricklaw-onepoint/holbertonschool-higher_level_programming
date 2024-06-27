#!/usr/bin/python3
"""Python - Network #1"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    request = Request(argv[1])
    # request = Request("https://www.google.com.au/")
    request.add_header("User-agent", "Mozilla/5.0 (Linux x86_64)")

    with urlopen(request) as response:
        print(response.info()["X-Request-Id"])
