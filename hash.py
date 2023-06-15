import os
import hashlib

begin_hash = []
compare_hash = []

def get_file_hash(file_path):
    hasher = hashlib.sha256()

    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(4096), b''):
            hasher.update(block)
    return hasher.hexdigest()

def begin_file_hash(directory_path):

    for root, dirs, files in os.walk(directory_path):
        files.sort()

        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = get_file_hash(file_path)
            begin_hash.append(file_hash)
    print(f'begin_hash: {begin_hash}')
    return begin_hash

def compare_file_hash(directory_path):
    for root, dirs, files in os.walk(directory_path):
        files.sort()

        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = get_file_hash(file_path)
            compare_hash.append(file_hash)
    print(f'compare_hash: {compare_hash}')
    return compare_hash

