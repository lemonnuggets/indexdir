"""
A simple script to index directories
and print files with the required filename.
Usage:
indexdir.py {filename} -dep {depth to be indexed(by default infinity)} -dir {directories to be indexed}
"""
import os
import argparse

def is_subdir(directory, path):
    """
    Arguments:
    Directory- The directory you're checking
    Path - The path you're checking
    ReturnValue:
    True if path is inside directory
    """
    path = os.path.realpath(path)
    directory = os.path.realpath(directory)
    return path.startswith(directory)

def get_dirignore():
    """
    ReturnValue: Returns list of directories in .dirignore
    """
    dirignore = []
    if os.path.isfile(os.path.join(os.getcwd(), ".dirignore")):
        with open(os.path.join(os.getcwd(), ".dirignore"), "r") as file_:
            line = file_.readline()
            if os.path.exists(line) and os.path.isdir(line):
                dirignore.append(os.path.realpath(line))
    return dirignore

def recursive_file_search(paths, filename, store, dirignore, depth):
    """
    Arguments:
        Paths: Takes a list containing paths to directories that should be traversed
        Filename: Filename to look for
        Store: List to store filepaths into that have the required filename
        Depth: Depth to which the file tree should be traversed
        Dirignore: Directories to be ignored
    """
    if depth >= max_depth:
        return 0
    paths.sort()
    for path in paths:
        path = os.path.realpath(path)
        useless_path = False
        if not os.path.exists(path):
            print("Path '" + path + "' does not exist.")
            useless_path = True
        for dir_ in dirignore:
            if is_subdir(dir_, path):
                useless_path = True
        if useless_path:
            continue
        if os.path.isdir(path):
            temp_depth = depth + 1
            if temp_depth >= max_depth:
                continue
            for file_ in os.listdir(path):
                if os.path.isdir(os.path.join(path, file_)):
                    recursive_file_search([os.path.join(path, file_)],
                                          filename,
                                          store,
                                          dirignore,
                                          depth + 1)
                elif os.path.isfile(os.path.join(path, file_)) and file_ == filename:
                    store.append(os.path.join(path, file_))
        elif os.path.isfile(path) and os.path.basename(path) == filename:
            store.append(path)

parser = argparse.ArgumentParser()
parser.add_argument("filename",
                    metavar="FILE",
                    help="The filename to look for")
parser.add_argument("-dep", "--depth",
                    metavar="DEPTH",
                    help="The depth up to which files should be indexed (default = infinity)",
                    type=int,
                    default=float("inf"))
parser.add_argument("-dir", "--directories",
                    metavar="DIRS",
                    help="The directory/directories to be indexed",
                    nargs='+',
                    default=[os.getcwd()])
args = parser.parse_args()
# print(args, args.depth, args.filename, args.directories)
results = []
max_depth = args.depth
dirs_to_be_ignored = get_dirignore()
print(dirs_to_be_ignored)
recursive_file_search(args.directories, args.filename, results, dirs_to_be_ignored, 0)
for result in results:
    print(result)
