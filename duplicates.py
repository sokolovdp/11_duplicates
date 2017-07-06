import sys
import os
from collections import Counter


def print_duplicates(all_duplicate_files: "list"):
    for duplicate_files in all_duplicate_files:
        print()
        for file_info in duplicate_files:
            print("file='{}' ({} bytes)".format(file_info['path'], file_info['size']))


def find_duplicates(all_files: "list") -> "list":
    duplicate_names = [name for name, val in Counter([f['name'] for f in all_files]).items() if val > 1]
    potential_duplicates = list()
    for name in duplicate_names:
        potential_duplicates.append([file_info for file_info in all_files if file_info['name'] == name])
    duplicate_names_and_sizes = list()
    for files_with_one_name in potential_duplicates:
        duplicate_sizes = [size for size, val in
                           Counter([file_info['size'] for file_info in files_with_one_name]).items() if val > 1]
        for size in duplicate_sizes:
            one_name_one_size_files = [file_info for file_info in files_with_one_name if file_info['size'] == size]
            duplicate_names_and_sizes.append(one_name_one_size_files)
    return duplicate_names_and_sizes


def load_all_files_info(pathname: "str") -> "list":
    all_files = list()
    for path, sub_dirs, files in os.walk(pathname):
        for filename in files:
            full_path = os.path.join(path, filename)
            all_files.append({'name': filename, 'size': os.path.getsize(full_path), 'path': full_path})
    return all_files


def main(path_name: "str"):
    all_files_info = load_all_files_info(path_name)
    all_duplicate_files = find_duplicates(all_files_info)
    print_duplicates(all_duplicate_files)


if __name__ == '__main__':
    dir_name = sys.argv[1]
    if not os.path.exists(dir_name):
        print("invalid path {}".format(dir_name))
    else:
        main(dir_name)
