#!/usr/bin/python3
"""Python - Network #1"""
from sys import argv
import requests


if __name__ == "__main__":
    try:
        response = requests.get(
            "https://api.github.com/user",
            auth=(argv[1], argv[2]),
            timeout=10000
        ).json()
        print(response["id"])
    except KeyError:
        print("None")
    except ValueError:
        print("Not a valid JSON")
