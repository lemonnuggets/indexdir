"""
A simple script to index directories
and print files with the required filename.
Usage:
indexdir.py {filename} {depth to be indexed(by default infinity)} {directories to be indexed}
"""
import os
import sys
import argparse

max_depth = float("inf")

def recursive_file_search(paths, filename, store, depth):
    if depth >= max_depth:
        return 0
    paths.sort()
    for path in paths:
        if not os.path.exists(path):
            print(f"{path} does not exist.")
            continue
        path = os.path.realpath(path)
        if os.path.isdir(path):
            temp_depth = depth + 1
            if temp_depth >= max_depth:
                continue
            for file_ in os.listdir(path):
                if os.path.isdir(os.path.join(path, file_)):
                    recursive_file_search([os.path.join(path, file_)], filename, store, depth + 1)
                elif os.path.isfile(os.path.join(path, file_)) and file_ == filename:
                    # handle_file(os.path.join(path, file_))
                    store.append(os.path.join(path, file_))
        elif os.path.isfile(path) and os.path.basename(path) == filename:
            # handle_file(path)
            store.append(os.path.join(path, file_))

args = sys.argv[1:]
file_to_be_searched = ""
# max_depth = ""
results = []
# recursive_file_search(args)