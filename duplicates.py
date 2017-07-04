import sys
import os
from collections import Counter


def print_duplicates(size: "int", files: "list"):
    print("-" * 40)
    for file in files:
        if file[1] == size:
            print(file[2])


def find_duplicates(files: "list of dicts"):
    duplicate_names = [name for name, val in Counter([file['name'] for file in files]).items() if val > 1]

    duplicate_full = list()
    for name in duplicate_names:
        list_with_sizes = list()
        for file in files:
            if file['name'] == name:
                list_with_sizes.append((file['name'], file['size'], file['path']))
        duplicate_full.append(list_with_sizes)

    for files_with_one_name in duplicate_full:
        sizes = Counter([file[1] for file in files_with_one_name])
        for size in sizes:
            print_duplicates(size, files_with_one_name)


def main(pathname: "str"):
    all_files = list()
    for path, subdirs, files in os.walk(pathname):
        for filename in files:
            full_path = os.path.join(path, filename)
            all_files.append({'name': filename, 'size': os.path.getsize(full_path), 'path': full_path})

    find_duplicates(all_files)


if __name__ == '__main__':
    main(sys.argv[1:][0])
