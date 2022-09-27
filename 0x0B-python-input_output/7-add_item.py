#!/usr/bin/python3

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


arguments = sys.argv
filename = "add_item.json"
try:
    args_list = load_from_json_file(filename)
except:
    args_list = []

for arg in range(len(arguments)):
    if arg > 0:
        args_list.append(arguments[arg])
try:
    save_to_json_file(args_list, filename)
except:
    pass
