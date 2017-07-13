import sys
import os
from collections import Counter


def print_duplicates(all_files_info: "list", duplicated_files: "list"):
    for file in duplicated_files:
        print()
        for info in all_files_info:
            if info[0] == file:
                print("file='{}' ({}) bytes".format(info[1], info[0][1]))


def find_duplicated_files(all_files_info: "list") -> "list":
    return [file for file, count in dict(Counter(info[0] for info in all_files_info)).items() if count > 1]


def load_all_files_info(pathname: "str") -> "list":
    all_files_info = list()
    for path, sub_dirs, files in os.walk(pathname):
        for filename in files:
            full_path = os.path.join(path, filename)
            all_files_info.append(((filename, os.path.getsize(full_path)), full_path))
    return all_files_info


def main(path_name: "str"):
    all_files_info = load_all_files_info(path_name)
    duplicated_files = find_duplicated_files(all_files_info)
    print_duplicates(all_files_info, duplicated_files)


if __name__ == '__main__':
    dir_name = sys.argv[1]
    if not os.path.exists(dir_name):
        print("invalid path {}".format(dir_name))
    else:
        main(dir_name)
