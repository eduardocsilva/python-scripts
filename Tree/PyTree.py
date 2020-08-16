#!/usr/bin/env python3

from sys import argv
from os import listdir
from os.path import isfile, isdir, join


"""
    Ignores files and directories that start with a '.'
    TODO: Provide a flag that allows these files to be included
"""
hidden = lambda item: item[0] != "."


def tree(path, level):
    for item in filter(hidden, listdir(path)):

        print(f"{'    ' * level}- {item}")

        filepath = f"{path}/{item}"
        if not isfile(filepath):
            tree(filepath, level + 1)


tree(argv[1] if len(argv) == 2 else ".", 0)
