import os
import sys
from collections import Counter, namedtuple

File_key = namedtuple('File_key', ['file_name', 'file_size'])
File_descriptor = namedtuple('File_descriptor', ['file_key', 'file_path'])


def print_duplicates(all_duplicated_files: "list"):
    for duplicated_files in all_duplicated_files:
        print()
        for descriptor in duplicated_files:
             print("file='{}' ({}) bytes".format(descriptor.file_path, descriptor.file_key.file_size))


def find_duplicated_files(all_file_descriptors: "list") -> "list":
    counted_files_keys = Counter([descriptor.file_key for descriptor in all_file_descriptors])
    duplicated_files_keys = [file_key for file_key, repeated in counted_files_keys.items() if repeated > 1]
    all_duplicated_files = list()
    for file_key in duplicated_files_keys:
        all_duplicated_files.append(
            [descriptor for descriptor in all_file_descriptors if descriptor.file_key == file_key])
    return all_duplicated_files


def load_all_file_descriptors(path_name: "str") -> "list":
    all_file_descriptors = list()
    for path, sub_dirs, files in os.walk(path_name):
        for file_name in files:
            full_path = os.path.join(path, file_name)
            file_size = os.path.getsize(full_path)
            file_key = File_key(file_name, file_size)
            all_file_descriptors.append(File_descriptor(file_key, full_path))
    return all_file_descriptors


def main(path_name: "str"):
    all_file_descriptors = load_all_file_descriptors(path_name)
    all_duplicated_files = find_duplicated_files(all_file_descriptors)
    print_duplicates(all_duplicated_files)


if __name__ == '__main__':
    dir_name = sys.argv[1]
    if not os.path.exists(dir_name):
        print("invalid path {}".format(dir_name))
    else:
        main(dir_name)
