#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "n", getattr(magic_string, "n", 0) + 1)
    return ", ".join(["BestSchool"] * getattr(magic_string, "n", 0))
