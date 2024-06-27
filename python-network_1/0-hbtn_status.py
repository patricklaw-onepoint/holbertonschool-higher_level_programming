#!/usr/bin/python3
"""Python - Network #1"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    request = Request("https://alx-intranet.hbtn.io/status")
    request.add_header("User-agent", "Mozilla/5.0 (Linux x86_64)")

    with urlopen(request) as response:
        body = response.read()
        print(
            f"Body response:\n"
            f"\t- type: {type(body)}\n"
            f"\t- content: {body}\n"
            f"\t- utf8 content: {body.decode('utf-8')}"
        )
