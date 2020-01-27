'''Aggregates item files in data/libs/items'''
import json
import os
import re

def pack_folder(folder="./dat"):
    '''
    Takes a string containing a relative path to a folder containing multiple .json files,
    combines them into one array, returns that array. Uses the containing folder to apply
    a category to the item as well.
    '''
    full_list = []
    contents = os.listdir(folder)

    item_errors = 0
    err_files = []
    for file in contents:
        this_file = folder + file
        with open(this_file) as current_file:
            try:
                items = json.load(current_file)
            except ValueError:
                items = {"flags": ["null"]}
                item_errors = item_errors + 1
                err_files.append(file)
            category = strip_path(["libs/", "dat/"], folder, 1).lstrip("./")
            items['category'] = category
            full_list.append(items)
    print("File read errors: " + str(item_errors))

    if item_errors > 0:
        print("Files with errors:")
        print(err_files)

    return full_list


def write_list(items, name='items.json'):
    '''
    Takes an array of JSON objects, writes them to a new .json file.
    '''
    with open(name, mode="w") as f_pointer:
        json.dump(items, f_pointer, indent=4)
        print("Successfully wrote to file: " + name)

def strip_path(regex, path, times):
    '''
    Takes a string, makes a regex from it, strips path of it.
    If regex is a list of strings, strips path of each one once, in order
    '''
    if isinstance(regex, list):
        for r in regex:
            pattern = re.compile(r)
            path = pattern.sub("", path, count=1)
        return path

    else:
        pattern = re.compile(regex)
        return pattern.sub("", path, count=times)

# Below is mostly for testing purposes, remove later.
write_list(items=pack_folder(folder='../../libs/items/gear/worn/armor/light/dat/'),
           name="items_test.json")
