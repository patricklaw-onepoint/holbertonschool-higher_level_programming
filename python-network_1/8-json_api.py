#!/usr/bin/python3
"""Python - Network #1"""
from sys import argv
import requests


if __name__ == "__main__":

    try:
        letter = "" if len(argv) == 1 else argv[1]
        response = requests.post(
            "http://0.0.0.0:5000/search_user", {"q": letter}, timeout=10000
        ).json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response['id']}] {response['name']}")
    except ValueError:
        print("Not a valid JSON")
