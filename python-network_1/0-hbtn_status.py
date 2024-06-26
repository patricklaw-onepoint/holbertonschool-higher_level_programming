#!/usr/bin/python3
"""Python - Network #1"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request("https://intranet.hbtn.io/status")
    with urlopen(req) as response:
        body = response.read()
        print(
            f"Body response:\n"
            f"\t- type: {type(body)}\n"
            f"\t- content: {body}\n"
            f"\t- utf8 content: {body.decode('utf-8')}"
        )
