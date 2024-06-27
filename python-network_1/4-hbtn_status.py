#!/usr/bin/python3
"""Python - Network #1"""
import requests


if __name__ == "__main__":
    request = requests.get(
        "https://intranet.hbtn.io/status",
        timeout=10000,
        headers={"User-agent": "Mozilla/5.0 (Linux x86_64)"},
    )

    response_text = "OK" if request.text[0] == "<" else request.text

    print(
        f"Body response:\n"
        f"\t- type: {type(request.text)}\n"
        f"\t- content: {response_text}"
    )
