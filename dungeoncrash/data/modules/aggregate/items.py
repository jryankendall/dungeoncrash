'''Aggregates item files in data/libs/items'''
import json
import os

def pack_folder(folder):
    full_list = []
    contents = os.listdir(folder)
    for file in contents:
        this_file = folder + file
        items = json.load(open(this_file))
        full_list.append(items)
    write_list(full_list, "items.json")


def write_list(items, name):
    with open(name, mode="w") as f:
        json.dump(items, f, indent=4)
        print("Successfully wrote to file: " + name)

pack_folder('../../libs/items/gear/worn/armor/heavy/dat/')