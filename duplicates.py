import sys
import os
from itertools import groupby


def print_duplicates(all_duplicate_files: "list"):
    for duplicate_files in all_duplicate_files:
        print()
        for file_info in duplicate_files:
            print("file='{}' ({} bytes)".format(file_info['path'], file_info['size']))


def find_duplicates(all_files_info: "list") -> "list":
    def key_fun(file_info):
        return file_info['name'], file_info['size']

    grouped_info = [[key, list(group)] for key, group in groupby(sorted(all_files_info, key=key_fun), key_fun)]
    duplicates = [group[1] for group in grouped_info if len(group[1]) > 1]

    return duplicates


def load_all_files_info(pathname: "str") -> "list":
    all_files_info = list()
    for path, sub_dirs, files in os.walk(pathname):
        for filename in files:
            full_path = os.path.join(path, filename)
            all_files_info.append({'name': filename, 'size': os.path.getsize(full_path), 'path': full_path})
    return all_files_info


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
