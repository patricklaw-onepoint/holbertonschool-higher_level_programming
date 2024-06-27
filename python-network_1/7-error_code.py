#!/usr/bin/python3
"""Python - Network #1"""
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get(argv[1], timeout=10000)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
