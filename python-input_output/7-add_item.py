#!/usr/bin/python3
"""Python - Input/Output
 Script that adds all arguments to a Python list,
 and then save them to a file:"""

import json
import sys

load_json = __import__("6-load_from_json_file").load_from_json_file
save_json = __import__("5-save_to_json_file").save_to_json_file

try:
    list = load_json("add_item.json")
except FileNotFoundError:
    list = []
finally:
    for i in sys.argv[1:]:
        list.append(i)
    save_json(list, "add_item.json")
