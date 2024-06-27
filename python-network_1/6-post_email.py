#!/usr/bin/python3
"""Python - Network #1"""
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.post(argv[1], data={"email": argv[2]})
    print(response.text)
