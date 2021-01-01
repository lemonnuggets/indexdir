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
    """
    Arguments:
        Paths: Takes a list containing paths to directories that should be traversed
        Filename: Filename to look for
        Store: List to store filepaths into that have the required filename
        Depth: Depth to which the file tree should be traversed
    """
    if depth >= max_depth:
        return 0
    paths.sort()
    for path in paths:
        if not os.path.exists(path):
            print("Path '" + path + "' does not exist.")
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

parser = argparse.ArgumentParser()
parser.add_argument("depth",
                    metavar="DEPTH",
                    help="The depth up to which files should be indexed",
                    type=int)
parser.add_argument("filename",
                    metavar="FILE",
                    help="The filename to look for")
parser.add_argument("directories",
                    metavar="DIRS",
                    help="The directory/directories to be indexed",
                    nargs='+')
args = parser.parse_args()
print(args, args.depth, args.filename, args.directories)
max_depth = args.depth
results = []
recursive_file_search(args.directories, args.filename, results, 0)
for result in results:
    print(result)
