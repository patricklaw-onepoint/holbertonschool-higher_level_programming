#!/usr/bin/python3
"""Python - Network #1"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    request = Request(argv[1])
    request.add_header("User-agent", "Mozilla/5.0 (Linux x86_64)")

    try:
        with urlopen(request) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except HTTPError as error:
        print("Error code:", error.code)
