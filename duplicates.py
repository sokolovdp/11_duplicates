import sys
import os
from collections import Counter


def print_duplicates(all_duplicate_files: "list of lists"):
    for duplicate_files in all_duplicate_files:
        print()
        for file in duplicate_files:
            print("name='{}' size={} path='{}'".format(*file))


def find_duplicates(all_files: "list of dicts") -> "list":
    # find files with duplicate names
    duplicate_names = [name for name, val in Counter([file['name'] for file in all_files]).items() if val > 1]
    potential_duplicates = list()
    for name in duplicate_names:
        names_with_sizes = [(file['name'], file['size'], file['path']) for file in all_files if file['name'] == name]
        potential_duplicates.append(names_with_sizes)

    # find files with same name and same size
    full_duplicates = list()
    for files_with_one_name in potential_duplicates:
        duplicate_sizes = [size for size, val in Counter([file[1] for file in files_with_one_name]).items() if val > 1]
        for size in duplicate_sizes:  # list sizes which have at least two or more files
            one_name_one_size_files = [file for file in files_with_one_name if file[1] == size]
            full_duplicates.append(one_name_one_size_files)

    return full_duplicates


def get_all_files_info(pathname: "str") -> "list of tuples":
    all_files = list()
    for path, sub_dirs, files in os.walk(pathname):
        for filename in files:
            full_path = os.path.join(path, filename)
            all_files.append({'name': filename, 'size': os.path.getsize(full_path), 'path': full_path})
    return all_files


def main(pathname: "str"):
    all_files_info = get_all_files_info(pathname)
    all_duplicate_files = find_duplicates(all_files_info)
    print_duplicates(all_duplicate_files)

if __name__ == '__main__':
    main(sys.argv[1:][0])
