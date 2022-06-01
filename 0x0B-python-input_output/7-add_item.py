#!/usr/bin/python3
"""

"""

import json
import os.path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
myList = []

if os.path.exists(filename):
    myList = load_from_json_file(filename)

if len(argv) > 1:
    for i in argv[1:]:
        myList.append(i)

save_to_json_file(myList, filename)
