#!/usr/bin/python3
"""Python - Network #1"""
from sys import argv
import requests


if __name__ == "__main__":
    try:
        response = requests.get(
            f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits",
            timeout=10000,
        ).json()
        for i in response:
            repository = i["sha"]
            owner = i["commit"]["author"]["name"]
            print(f"{repository}: {owner}")
    except TypeError:
        pass
