#!/usr/bin/python3
import hidden_4


def discover():
    print("\n".join(name for name in dir(hidden_4) if not name.startswith("__")))


if __name__ == "__main__":
    discover()
